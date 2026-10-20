# Academic Main VII: proposition-bound authority

Status: **PROVED LOCAL** for the mathematical finite-certificate implications;
**TESTED MODEL** for the software boundary. The formal build admission remains
pending until an actual pinned kernel run is reviewed and installed in the
catalogue. This document is not itself a proof receipt.

## Historical refutations

On exact `proof_authority.py` from PR #209 head
`3e1ef648896821321423e6642f1de4a458a0c791`, both of these returned `VERIFIED`:

1. `Claim("RH", "The Riemann hypothesis is true.", "C", scope="global")`
   with the real recorded `polynomial_fermat` theorem name and historical
   `formal/mathlib_bridge/axiom_audit.json`.
2. `Claim("wrong", "The matrix [[-1]] is PSD.", "B")` with a valid PSD
   certificate whose matrix is `[[1]]`.

Run `python scripts/probe_proof_authority_boundary.py` to reproduce. The probe
loads the exact historical authority module and uses the present arithmetic
backend; it is not represented as a historical full-suite run. The independent
referee owns the complete historical/current replay.

The failure is logical, independent of any numerical algorithm: matching a
receipt name or scope does not imply the claimed proposition.

## The finite theorem and exact domain

For a finite rational symmetric matrix `M`, `MatrixProposition("psd", M)`
means `vᵀMv ≥ 0` for every real column vector of its stated dimension.
`MatrixProposition("not_psd", M)` is its negation. A negative rational witness
with `vᵀMv < 0` proves the latter directly. The PSD check uses the exact
principal-minor criterion implemented by the existing rational kernel. The
finite Schur checker also recomputes its actual Schur obligations.

No theorem about an infinite kernel, a different matrix, a normalization change,
or an original arithmetic source follows from these conclusions. Those require
additional, independently checked hypotheses and transport proofs.

The trusted checker extracts the exact matrix proposition from immutable input
snapshots. Every matrix entry, dimension, and predicate must match the claim.
Only integer, `Fraction`, and SymPy rational entries are accepted; floats,
booleans, strings and non-rational symbolic expressions are outside this
advertised authority domain. `n_A` is a strict integer, with both blocks nonempty.
The local scope is always finite and cannot be relabelled by the caller.

```python
from observational_succ.proof_authority import Claim, LocalCertificate, MatrixProposition

certificate = LocalCertificate("psd_matrix", {"matrix": [[2, 1], [1, 2]]})
claim = Claim("finite PSD", MatrixProposition("psd", [[2, 1], [1, 2]]), "B")
assert claim.discharge(certificate).status == "VERIFIED"
```

English claim statements are still representable as research metadata, but are
`INAPPLICABLE` for discharge. No English similarity heuristic is used.

## Formal proposition and build admission

`FormalProposition` includes the complete Lean-exported type expression, full
canonical declaration name, environment digest, toolchain and mathlib revision.
The type expression contains the quantified variables and hypotheses. The
installed record additionally binds source hashes and the complete audited
build environment. An admitted reference asserts precisely that universal type.
There is no implicit parameter substitution, hypothesis discharge, equivalence,
English interpretation, or transport. Each such operation needs another checked
Lean declaration with the desired conclusion.

`FormalTheorem.from_receipt(full_name, record)` requires all of:

- An exact canonical JSON digest in the installed immutable catalogue.
- The `succ.lean.kernel.v1` record schema and matching current source hashes.
- The exact theorem type and type digest, environment, toolchain and revision.
- Actual exported axioms within the fixed standard envelope
  `propext`, `Classical.choice`, `Quot.sound` and any stricter caller subset.

The catalogue has **no runtime registration API**. Its entries are admission
decisions made only after the coordinator has inspected the genuine pinned
kernel build, complete declaration types, source hashes, negative elaboration
controls and axiom output. A digest authenticates a reviewed record under this
installed-code trust model; it is not mathematical proof that a process ran.
`build_succeeded: true` alone never suffices. Historical axiom JSON is preserved
but is not admitted evidence.

The catalogue starts empty. The formal lane generates the real kernel artifact;
the coordinator admits it only after review. Thus absence of authenticated
kernel contact fails closed, rather than silently trusting a synthetic receipt.
For an admitted record, the exact positive interface is:

```python
from observational_succ.proof_authority import Claim, FormalTheorem

# record must be the actual coordinator-admitted kernel record.
theorem = FormalTheorem.from_receipt(full_canonical_name, record)
claim = Claim("exact imported theorem", theorem.proposition, "C", scope="global")
assert claim.discharge(theorem, receipt=record).status == "VERIFIED"
```

The formal lane's post-admission check exercises this for each exported theorem,
including Mason–Stothers and polynomial Fermat. Without the real build and
admission, no positive formal verification is claimed by these Python tests.

## Source and legacy boundaries

The former `polynomial_identity` callback compared two arbitrary supplied
polynomials. It neither identified the theorem's parameters nor an original
source. It cannot confer Level D authority. `SourceRealization` is retained as
metadata and always fails closed until a genuine proposition-bound source
transport is admitted. This does not refute the mathematical source-identification
problem; it identifies missing evidence.

`ProofContract`, `CarryingContract`, callback diagnostics and external theorem
references are non-authoritative research metadata. They are immutable, with
immutable nested collections. Contradictory dependency/source flags and duplicate
bound variables are rejected. `CarryingContract.verify()` runs diagnostics but
returns `status="UNVERIFIED"`, with the historical assertion separately recorded
as `claimed_status`. A `lambda: True` or unrelated external reference cannot
promote that record. Final metadata invariants are rechecked.

## Threat model, verdicts, and verification limits

Inputs are untrusted **data**; installed Python checker code, its dependencies,
and the reviewed catalogue form the trusted computing base. The process is not
a sandbox for arbitrary Python code executing within it. Monkeypatching modules,
replacing installed files or modifying the catalogue is outside this model.
Public checker/source registration is closed. Exact artifact types prevent
subclasses from overriding verification at the data boundary.

`REFUTED` means offered evidence failed its obligation; it does **not** mean the
claimed mathematical theorem has been refuted. `INAPPLICABLE` covers a different
proposition, missing typed claim, scope, level or normalization mismatch.
`UNKNOWN` preserves undecidable exact obligations.

Focused validation:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest \
  tests.test_proof_authority tests.test_proof_contracts \
  tests.test_proof_contracts_witnesses tests.test_proof_authority_legacy_boundaries
```

The 43 controls include positive rational PSD/non-PSD/Schur cases and negative
controls for wrong matrices, predicates, witnesses, scope, type/environment,
forged JSON, fake source identification, callbacks, subclasses, mutation and
contradictory dependencies. These tests support the boundary; they are not a
universal proof of software defect absence. The actual formal gate is separate.
