# Validation and reproduction boundaries

The exact implementation and three finite mathematical routes were checked
before publication. The final published commit is then replayed; its SHA,
commands, outcomes and any repository-wide failure are recorded in the draft
PR body. This avoids placing a self-referential final-commit receipt inside
that same commit.

## Reproducible finite checks

From the repository root:

```sh
python -m unittest discover -s tests -p 'test_ym_*.py'
python scripts/yang_mills_coupled_probe.py
python scripts/yang_mills_succ_probe.py
python scripts/yang_mills_qm_bridge_probe.py
```

The continuation adds 30 tests: 12 coupled-source, 8 reflection-order and
10 trace-observer tests. The complete Yang–Mills pattern includes 76 parent
tests and therefore selects 106 tests. The trace-observer adapter was also
run with its existing quaternion dependency: 44 tests passed. These executions
are finite validation, separate from the paper proofs.

[probe_receipt.json](probe_receipt.json) is deterministic stdout of the new
probe. It records compact-group moment checks, 20 exact character reconstructions,
fresh rational conjugations, the nonfactorizing partition `1771/1728`, and
the source interaction `E[x]=E[y]=0`, `E[xy]=1/33`. Its small certificate
returns expectation `16/513` with error at most `1/128`, meeting tolerance
`1/100`. Re-running the script reproduces the JSON byte for byte.

The reflection test directly integrates a declared shared-link density with
19,593 polynomial monomials. It obtains partition `81/64` and reflected
Gram `diag(1,1/18,1/81)`, as predicted by the character calculation.
The negative controls include normalized reflected squares `-1` and
`-71/1104`, a gauge-invariant Z2 negative reflected form, and a deterministic
coarse map whose CP/reflection covariance does not preserve positive-half
support. Controls were not discarded after the repair.

## Formal scope

The portable runner and exact pinned invocation are in
[FORMAL_REPLAY.md](FORMAL_REPLAY.md). Fresh execution passed upstream
integrity (9,508 source files, 43 review modules and four normalized-text
correspondences), the original dependency-light proof-transport generator,
a correct transported proof, a rejected semantic mutation, five small
rational Gram theorem checks, and a rejected sign mutation. The official
Lean 4.32.0 release archive hash was verified.

The preserved receipts include an initial command-root error. An unsuccessful
`leanchecker --help` inventory invocation is disclosed in the formal note and
does not count as another kernel check. No `native_decide`, `sorry`, or
additional axiom is used in the new accepted rational certificate.

**Not run:** the full Yang–Mills dependency graph, acceptance endpoint,
Comparator controls/endpoints, or an independent external kernel. Source
integrity and a bounded replay are not full proof reproduction. The analytic
identification of the finite moment table with Haar integration is supplied
by the paper derivation, not by the small Lean arithmetic certificate.

## Required repository gates

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Final execution must identify the actual commit and a clean tree. If the
full discovery is split into whole-module processes, report that fact and
verify every discovered test ID is executed exactly once; it is not identical
to a single-process order-sensitive run. A partial or interrupted run is not
a full-suite pass. Existing global mpmath precision interactions are not to
be hidden by selectively reporting passing modules.

All agent cross-checks in this continuation share a model family. Different
quaternion, matrix, character and Lean presentations improve fault detection,
but are not represented as independent external mathematical verification.
