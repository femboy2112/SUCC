#!/usr/bin/env bash
# Standalone, pinned NO-GHOST proof-kernel and axiom gate.
set -euo pipefail

no_ghost_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$no_ghost_root"
test "$(cat lean-toolchain)" = 'leanprover/lean4:v4.14.0'
no_ghost_lean="${NO_GHOST_LEAN:-lean}"
no_ghost_tmp="$(mktemp -d)"
trap 'rm -rf "$no_ghost_tmp"' EXIT

# Some container runtimes permit /proc/self/exe but reject the equivalent
# /proc/<own-pid>/exe spelling used by Lean 4.14. This optional compatibility
# adapter changes only that spelling, never the compiler or proof kernel.
# It grants no access to another process and is unnecessary on normal hosts.
if [[ "${NO_GHOST_SELF_PATH_COMPAT:-0}" == 1 ]]; then
  cat > "$no_ghost_tmp/self_path.c" <<'C'
#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
ssize_t readlink(const char *path, char *buf, size_t bufsiz) {
    ssize_t (*original)(const char *, char *, size_t) = dlsym(RTLD_NEXT, "readlink");
    if (!original) { errno = ENOSYS; return -1; }
    char own_path[64];
    snprintf(own_path, sizeof own_path, "/proc/%ld/exe", (long)getpid());
    const char *normalized = strcmp(path, own_path) == 0 ? "/proc/self/exe" : path;
    return original(normalized, buf, bufsiz);
}
C
  cc -shared -fPIC -O2 "$no_ghost_tmp/self_path.c" -ldl -o "$no_ghost_tmp/self_path.so"
  export LD_PRELOAD="$no_ghost_tmp/self_path.so${LD_PRELOAD:+:$LD_PRELOAD}"
  printf '%s\n' 'Compatibility: own executable path normalized to /proc/self/exe.'
fi

no_ghost_version="$("$no_ghost_lean" --version)"
printf '%s\n' "$no_ghost_version"
case "$no_ghost_version" in
  'Lean (version 4.14.0,'*) ;;
  *) printf '%s\n' 'ERROR: expected pinned Lean 4.14.0.' >&2; exit 1 ;;
esac

# Calibrate the actual compiler, not merely source scanning or version output.
# This deliberately invalid source exists only in the temporary directory.
printf '%s\n' 'theorem noGhostFalse : False := by decide' \
  > "$no_ghost_tmp/NoGhostNegative.lean"
no_ghost_negative_status=0
"$no_ghost_lean" "$no_ghost_tmp/NoGhostNegative.lean" \
  > "$no_ghost_tmp/negative.log" 2>&1 || no_ghost_negative_status=$?
python - "$no_ghost_tmp/negative.log" "$no_ghost_negative_status" <<'PY'
from pathlib import Path
import sys
status = int(sys.argv[2])
diagnostic = Path(sys.argv[1]).read_text()
assert status == 1, f'Expected False-proof rejection (exit 1), got {status}'
expected = "error: tactic 'decide' proved that the proposition\n  False\nis false"
assert expected in diagnostic, f'Unexpected negative-control failure: {diagnostic}'
print('Negative control: False proof rejected with exit 1 and expected decide diagnostic.')
print(expected)
PY

python - <<'PY'
from pathlib import Path
import re
text = Path('formal/NoGhost.lean').read_text()
# Strip nested Lean block comments and line comments before token checks.
out = []
i = depth = 0
while i < len(text):
    if text.startswith('/-', i):
        depth += 1
        i += 2
    elif depth and text.startswith('-/', i):
        depth -= 1
        i += 2
    elif depth:
        i += 1
    elif text.startswith('--', i):
        end = text.find('\n', i)
        i = len(text) if end == -1 else end
    else:
        out.append(text[i])
        i += 1
assert depth == 0, 'Unclosed block comment'
code = ''.join(out)
for token in ('sorry', 'admit', 'axiom', 'unsafe', 'native_decide'):
    assert re.search(r'\b' + token + r'\b', code) is None, token
assert re.search(r'^\s*import\s', code, flags=re.M) is None, 'Unexpected import'
print('Source gate: no placeholders, custom axioms, unsafe code, or native_decide.')
PY

"$no_ghost_lean" -o "$no_ghost_tmp/NoGhost.olean" formal/NoGhost.lean \
  > "$no_ghost_tmp/axioms.log"
cat "$no_ghost_tmp/axioms.log"
python - "$no_ghost_tmp/axioms.log" <<'PY'
from pathlib import Path
import re
import sys

prefix = 'ObservationalSUCC.NoGhost.'
expected = {
    'ConstraintCover.glue_restricts': [],
    'ConstraintCover.glue_unique': ['Quot.sound'],
    'ConstraintCover.glue_preserves_complete_constraints': [],
    'ConstraintCover.source_supported_constraint_gluing': ['Quot.sound'],
    'CompleteKernel.complete_kernel_implies_all_prior_laws': [],
    'CompleteKernel.source_indexed_all_priors_iff_complete_kernel': [],
    'RigidTransport.path_preserves_invariant': [],
    'RigidTransport.invariant_transport_path_independent': [],
    'RigidTransport.invariant_comparisons_are_inverse': [],
    'Countermodels.bit_comparison_involutive': [],
    'Countermodels.bit_comparisons_fail_braid': [],
    'Countermodels.omitted_joint_constraint_blocks_gluing': [],
}
observed = {}
for line in Path(sys.argv[1]).read_text().splitlines():
    empty = re.fullmatch(r"'([^']+)' does not depend on any axioms", line)
    nonempty = re.fullmatch(r"'([^']+)' depends on axioms: \[(.*)\]", line)
    assert empty or nonempty, f'Unexpected compiler output: {line}'
    match = empty or nonempty
    name = match.group(1)
    assert name.startswith(prefix), name
    short = name.removeprefix(prefix)
    assert short not in observed, f'Duplicate axiom report: {short}'
    observed[short] = [] if empty else [x.strip() for x in match.group(2).split(',')]
assert observed == expected, (observed, expected)
print(f'PASS: {len(expected)} declarations kernel-checked; exact axiom sets verified.')
PY
