# Claude — consolidate the actual SUCC frontier, merge, and clean working branches

## Authorization and outcome

Leah requests coherent consolidation of the latest validated SUCC state into
`main`, followed by branch cleanup. **Merging the reviewed combined candidate
and deleting fully integrated, inactive working branches are authorized.**
No release, tag, license change, archive deletion, force-push, or loss of unique
work is requested. Do not stop for another routine merge confirmation once the
concrete gates below pass. If a tool approval or access boundary actually blocks
the action, report that exact block.

Repository: <https://github.com/femboy2112/SUCC>.
Execute the work. A plan-only response is insufficient.

## 1. Reconstruct live state before changing it

Read `AGENTS.md`, `docs/METHOD.md`, `docs/FOUNDATIONS.md`, the provenance manifest,
the claim registry, and the integration reports. Fetch all relevant refs, inspect
status/worktrees, and preserve unrelated work. The observed main was
`b116841f12b41aaf7600da39bbb40577f25b6295`; never overwrite a newer main.

Academic Main IX is already staged in PR #250:

- Branch `integrate/academic-main-ix-pi-circle-source-2026-10-23`.
- Observed head `f986507851e34636f60bee657dcdf0771a934380`.
- It preserves 28 older research PRs through 17 leaf tips. #245 and #246 are
  already included. Recheck ancestry rather than merging their content again.

New pre-round leaves:

| PR | Observed head |
|---|---|
| #255 | `68def05ad1dd92b78f8d6bd646ff28ab1ed85c59` |
| #259 | `a777aa99f541df2a0e2a0b8d57fef3f0940e465c` |
| #260 | `654e9c9984ced49cee454d99cff20415072d1ffc` |
| #261 | `4b52cb87a19c2f599e5386fc12a9758bab12cba8` |
| #262 | `34f8e040a6f86a9e583bad428f3d4e20940e1ac8` |
| #263 | `d7b5a5b91d142717ce7898417eed7a5dc603e019` |
| #264 | `de005af44cb4592d7a8be73f46fa1983f627da27` |

**This round adds a descendant of #264:**
`research/pi-source-collision-entropy-2026-10-24`.
Resolve its final head live and use it in place of bare #264 in the leaf set.
Read `research/2026-10-24/PI_SOURCE_COLLISION_ENTROPY.md`, its validation record,
and `docs/CLAIM_SUPPLEMENT_PI_SOURCE_COLLISION.md`.

Search for any additional recent PRs or changed donor tips. Record all final
heads, base commits, source paths, and coverage in a machine-readable manifest.
PR base metadata is not a substitute for `git merge-base --is-ancestor`.

## 2. Integrate locally in one isolated branch

Use a fresh integration branch from the current reviewed #250 candidate or
reconcile its history with current main if main advanced. Preserve donor history
with ancestry-aware merges; do not squash away the source graph. Merge the leaf
set locally before pushing one coherent candidate. Parallel agents may audit
disjoint sources, but the principal owns the checkout and all conflict decisions.

Two concrete hazards must be resolved semantically:

### A. #260 and #261 are complementary implementations with path collisions

Both independently created different versions of:

```text
observational_succ/bbp_minimal_path.py
scripts/bbp_minimal_path_probe.py
tests/test_bbp_minimal_path.py
docs/CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH.md
.github/workflows/bbp-minimal-path.yml
```

#260 contains moving gauge, missing-prime counterfeits, periodic proxies, and
signed bulk diagnostics. #261 contains all-prime/prime-power births, minimal
rational recurrence, Galois tomography, and different nonnormal controls.
Preserve both bodies of mathematics, both API families, both independent probes,
and both old receipts. Distinct canonical modules/scripts plus a clearly scoped
compatibility surface are preferable to one ambiguous file. The `_prime` helpers
have different domains: one permits 2, the other requires odd primes.

Also review their shared `bbp_cyclotomic_birth.py`, tests, claim supplement,
source dossier, handoff, and workflow. **#258 and #261 do not contain final
#256 head `0683f8f166b9106ab8405a2d6538415b5ac84ba3`.** #260 does. Preserve the
later filtered p² Witt contribution as well as #261's Galois additions.

### B. Claim identity collisions

#260 and #261 reuse MP-01..MP-06 for different propositions; #261 also repeats
MP-05 within its own supplement. Keep original branch/SHA-qualified identities,
assign distinct canonical FQIDs, and write an explicit crosswalk. Do not rewrite
archival originals or pretend different claims were one theorem. Merge the
namespace registry structurally by identity, not textually.

The new SCE research claims must remain paper/conditional/finite claims. The
#259 Lean declarations and #263 core-Lean reachability theorems have their own
exact scope. No kernel authority propagates to a nearby unformalized theorem.

## 3. Reconcile the scientific account and make main readable

Promote #252's source-fidelity correction in current navigation. The #251
four-pole-closure claim was withdrawn: index poles are not orbit points, and a
fixed-point 1/3 replacement did not preserve the complete BBP source/initial state.
Keep the historical report and add a clear corrected-current route.

`docs/PROOF_MECHANISMS.md` still contains contradicted old examples below its
corrigendum. Rewrite the current explanatory prose coherently; a banner above
false current guidance is not enough. Preserve the old bytes in their historical
source location. Correct the geometric-decay non-coboundary example and the
overbroad suggestion that an equivalent criterion can never be useful.

Integrate SCE-01: positive Poisson regret and minimum-relative regret are both
equivalent to normality asymptotically. The original sufficient direction remains
valid; the stronger-looking formulation was not a new proof step. The new route
is a prescribed-scale collision bound with an explicit remaining hypothesis.

Update README/frontier/roadmap navigation to explain, in plain language:

- What is proved about the source, finite observers, circle geometry, prime clocks,
  carry transport, Galois averaging, and entropy.
- What is only tested at finite horizons.
- The exact selected-source collision/Fourier problem still open.
- Why π-normality, its independence, RH, and absolute/decimal normality are not proved.

Do not erase the framework's broader observer mission. Show how the machinery
connects without claiming that reachability or geometric minimality supplies
quantitative visit frequencies. Keep GitHub math renderable: standard `$...$`
and `$$...$$`, simple supported commands, no fragile custom macros. Inspect
links and representative rendered pages if a permitted rendering surface exists.

The old #250 integration report has a stale pre-push status. Add a successor
receipt with actual current heads and checks; do not rewrite historical runs.

## 4. Validate the combined state, once coherently

First run focused suites for every semantically merged module, both MP families,
the #259/#262 carry tests, #263 reachability, Poisson minimum, and SCE collision.
Replay all preserved exact receipts against their original source scope. When
renames change hashes, keep the old receipt and create a separate integration
receipt. Rebuild changed Lean contracts with actual theorem types and axiom lists;
use serial bounded-memory jobs when necessary.

Then run the repository's complete required gates on the combined candidate:

```sh
python scripts/verify_provenance.py
PYTHONPATH="$PWD" python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Use the declared environment/test dependencies. The explicit PYTHONPATH matches
the importable-package setup used by CI; do not confuse the known subprocess
import-path problem with a mathematical failure. Record actual exit codes,
counts, versions, hashes, and any failed attempts. No tests written solely to
repeat an implementation; keep independent and adversarial verification useful.

Push the coherent candidate once. Inspect required hosted checks on its exact
head and, where relevant, verify the tested merge tree against the delivered tree.
Green donor branches do not certify the combination. Avoid needless rebases,
empty pushes, and repeated full-suite CI triggers. Repair concrete failures;
rerun only necessary failed gates and the final required integration gate.

## 5. Merge, then clean verified redundant working refs

When provenance, mathematical review, focused checks, and required combined CI
pass, merge to main under the authorization above. Record the actual merge SHA
and re-fetch main to verify the result. Close covered/superseded PRs only after
their actual tips are preserved. Retarget any still-active research PR coherently.

Before deleting any working branch, verify its exact current tip is an ancestor
of merged main, no unpushed/uncommitted work depends on it, and it is not active
in another session. Retain branches with unique work, moved heads, active users,
or uncertain coverage. Preserve `archive/...` branches and tags. Never use blanket
branch deletion. If a branch changed since the manifest, inspect the new commits.

Finish with the final main SHA, coverage manifest, semantic conflict decisions,
validation evidence, removed/preserved branch list and reasons, and the next
research branch base. Point Codex to
`handoffs/CODEX_PI_SOURCE_COLLISION_NEXT_2026-10-24.md`.
