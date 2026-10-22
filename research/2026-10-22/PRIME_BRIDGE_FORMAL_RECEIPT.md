# Prime Bridge formal targets and execution receipt

Date: 2026-10-22. Parent baseline: `b116841f12b41aaf7600da39bbb40577f25b6295`.
Branch: `research/prime-bridge-2026-10-22`.

## Current status: LEAN-KERNEL VERIFIED; formal authority admission not installed

The finite theorem source is `formal/PrimeBridge.lean`. It imports only
`Std.Tactic` from pinned Lean 4.14.0. It contains no proof placeholders,
custom axioms, native-decision shortcuts, or analytical claims. The validator
exports each actual theorem type and its transitive axiom dependencies using
SUCC's existing `formal/kernel_audit/ExportCommand.lean`.

The dedicated `Prime Bridge finite kernel certificates` workflow **passed** at
commit `73ecf86467b3a62cbe6b4bbef989c02c3b2b16cf`, push run
[39734454757](https://github.com/femboy2112/SUCC/actions/runs/39734454757),
job `119676779117`. All eleven actual theorem types were exported, all axiom
dependencies were checked, and all three negative controls were rejected.
The untouched official Lean 4.14.0 archive passed the pinned SHA256 gate.

The downloaded artifact `12406501833` has ZIP SHA256
`d3d60bce46593b8f234c8c7e525928d211288845c6b81830e2b607ba9292221b`.
Its exact sources, log hashes and theorem-expression hashes were checked against
the local integrated source, and all matched. Source SHA256:
`03a48ee884b65cf90ef65fa87d34cb4456aad8e1f3066c540838c68a1be5871f`.
Raw theorem types, axioms, positive/negative outputs and the machine receipt are
in `prime_bridge_receipts/formal_73ecf864/`.

The source-bound record remains `KERNEL_CHECKED_UNADMITTED`; it does not alter
the trusted formal catalogue or claim SUCC Level C admission. Eight declarations
use only standard `propext`; the braid counterexample, abstract commutation
obstruction and conditional mirror-word theorem have empty axiom sets. No
`sorryAx`, custom axiom, native-decision axiom, `Classical.choice`, or
`Quot.sound` appears in the eleven exported dependency lists.

## The eleven precise finite/conditional targets

1. `decode_codeword`: for each erased share and each pair `(k,r)` in F3², the
   explicit two-share decoder returns `(k, erased-share-value)`.
2. `decode_encodePair`: each decoder is left inverse to its declared pair encoder.
3. `encodePair_decode`: it is also right inverse; this is a permutation of the
   nine two-qutrit basis labels.
4. `codeword_gram_count`: unnormalized support inner products equal `3 δ_kl`.
5. `singleton_partial_trace_count`: every matrix element of the unnormalized
   singleton partial trace equals `δ_kl δ_xy`. With the common normalization
   `1/3`, this is the coefficient identity for `Tr_other(W E_kl W*) = δ_kl I/3`.
6. `singleton_label_alias`: each singleton has a common support value for two
   distinct logical basis labels.
7. `wrong_middle_decoder_receipt`: deleting the inverse of 2 in F3 fails at
   logical input 1 and randomizer 0.
8. `wrong_semigroup_braid_receipt`: ordinary SUCC/FUCC commutation fails at
   `p=2,n=1`.
9. `commuting_reconstructions_force_logical_commutation`: for arbitrary types,
   an injective encoding and two physical actions intertwining logical actions,
   physical commutation implies logical commutation. The physical tensor-factor
   and operator interpretation is a separately justified application.
10. `mirror_recurrence_along_words`: a specified generator recurrence propagates
    to every finite word whose generators satisfy a declared admissibility
    predicate. This theorem does not prove unique prime factorization or analytic
    square summability; those remain explicit premises/arguments in the dossier.

11. `matrix_unit_intertwining_count`: all 2,187 finite coefficient identities
    for `D_A*(E_ab ⊗ I)D_A W = W E_ab`, over every erasure, logical matrix unit,
    logical input, and full output basis triple. The common normalization cancels.

The quantum code formula is
`W|k> = 3^(-1/2) Σ_(r∈F3) |r,r+k,r+2k>`.
The complete finite support counts are kernel decidable propositions; they are
not a sample of an infinite universal claim. Complex Hilbert linear extension,
normalization by a square root, the Bruhat–Tits identification, and all infinite
TFD/operator-analysis results are **not** included in this formalization.

## Local toolchain observations

Commands actually run:

```sh
curl --fail --location --retry 2 --max-time 240 \
  https://github.com/leanprover/lean4/releases/download/v4.14.0/lean-4.14.0-linux.tar.zst \
  -o /tmp/prime-bridge-lean-4.14.0-linux.tar.zst
sha256sum /tmp/prime-bridge-lean-4.14.0-linux.tar.zst
tar --no-same-owner --zstd -xf /tmp/prime-bridge-lean-4.14.0-linux.tar.zst -C /tmp
/tmp/lean-4.14.0-linux/bin/lean --version
python scripts/prime_bridge_lean_probe.py \
  --lean /tmp/lean-4.14.0-linux/bin/lean \
  --output /tmp/prime-bridge-formal-local
python -m py_compile scripts/prime_bridge_lean_probe.py
```

The official archive hash exactly matched
`320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a`, already pinned
by SUCC's existing formal workflow. Extraction succeeded with `--no-same-owner`.
The first extraction without that option emitted ownership errors and failed;
it did not produce a valid build receipt.

Compiler startup returned exit 1, `error: failed to locate application`, before
any theorem was elaborated. The original Lean 4.14 `src/runtime/io.cpp` lines
1032–1041 call `readlink("/proc/<getpid>/exe",...)`. A direct Python control
confirmed that this container permits `/proc/self/exe` but denies the numeric
self-PID form with `PermissionError`, errno 13. `LEAN_SYSROOT` and `--help` did
not avoid startup failure. Actual `Lean/Util/Path.lean` shows that compiler
`initSearchPathInternal` calls `getBuildDir`, which unconditionally uses
`IO.appDir`; `LEAN_SYSROOT` only affects separate `findSysroot`.

No permission workaround or compiler shim was used. No local Lean success is
claimed. Python syntax compilation of the validator succeeded.

## Reproduction and promotion gate

```sh
python3 scripts/prime_bridge_lean_probe.py --output /tmp/prime-bridge-kernel
```

The validator deletes stale success metadata before running. It requires:

- actual Lean 4.14.0 startup and elaboration success;
- all eleven fully qualified theorem types exported from the compiled environment;
- a transitive axiom envelope contained in the standard `propext` axiom;
  no `sorryAx`, custom axiom, native decision axiom, or other dependency is allowed;
- three negative controls rejected specifically because `decide` proves the
  proposition false: wrong separated-pair inverse, spurious off-diagonal
  singleton coherence, and incorrect semigroup braid.

The JSON records source/checker/workflow hashes, Git commit, actual compiler
version, theorem expression hashes, and log hashes. The hosted workflow also
verifies the official compiler archive before execution. The passing push run and downloaded logs were inspected before the status
above was promoted. The local startup failure remains an accurate separate
observation about this container.

## Next formal boundary

After finite kernel verification, formalize the complex linear-extension lemma
from these support counts to isometry, partial trace, and full matrix-algebra
intertwining. Infinite tensor products, trace-class Gibbs operators, modular
operators, and spectral min–max analysis require independently selected analytic
libraries and are not consequences of this finite source.

## Additional exact sanity check (not a kernel certificate)

An independent Python enumeration of arithmetic in `range(3)` checked all 27
`(erased,logical,randomizer)` decoder inputs and all 243
`(erased,k,l,x,y)` singleton partial-trace support counts. All passed. A separate exact loop checked all 2,187 matrix-unit
intertwining coefficients and also passed. This
corroborates the intended finite statements but does not establish Lean
elaboration or identify the entire quantum-channel proof with a finite check.
The raw local compiler-startup failure is preserved in
`prime_bridge_receipts/formal_local_startup.log`.

## First hosted attempt: concrete elaboration repair

The untouched official compiler ran successfully on GitHub Actions run
`39733348628`, commit `9292bb854a0bf6193fb92176df5182c9bb16f42d`.
The first ten-target attempt failed to synthesize a decidability instance for
an existential statement in `singleton_label_alias`. This is an elaboration
failure, not a mathematical counterexample. The repaired source provides the
constructive witnesses `r=0,t=-e` and checks only their finite universal identity.
The failed environment's placeholder dependency is preserved in its error log;
it is not accepted as a certified theorem.

The same output established that ordinary finite `decide` proofs on these `Fin`
identities use Lean's standard `propext` axiom. The initial validator's proposed
empty envelope was therefore unnecessarily strict. The repaired validator allows
only `propext`; generic constructive transport/commutation proofs have empty
axiom sets. Every actual list remains exported, and `sorryAx` remains forbidden.
Raw attempt logs: `prime_bridge_receipts/formal_attempt1/`.
