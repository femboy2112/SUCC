# Property Bootstrap — claim supplement (PB series)

**Research branch:** `research/property-proof-graph-bootstrap-2026-10-13`, parent zero-centered PR #59 `b7fbba74fedd6e6734b1d2b129a72bdff4dd9843`; main ancestor `6e0d88f1b235b85188393bbcd64ac0436cb71a70`. **RH PROVED: no.** No zero locations are construction inputs.

| ID | Exact statement/scope | Status | Evidence and next falsifier |
|---|---|---|---|
| PB-01 | For any K>=1 and M>K, bounded self-adjoint A+=I, A-=I-2P_M have identical K-corner quadratic observations but A- has value -1 at e_M. | CLASSICAL / PROVED LOCAL | Direct rank-one projection proof; exact rational `property_obstruction_controls.py` and focused tests. Not actual Weil source; model counterexample only. |
| PB-02 | For a **fixed bounded** self-adjoint operator, positivity on every compatible finite compression over a strong-dense exhaustion implies global positivity. | CLASSICAL / PROVED LOCAL | Density plus bounded continuity; fails as an argument for finitely checked corners or an unbounded/distributional form without a valid core/domain proof. |
| PB-03 | The 83-node property graph has typed scope, status, valid dependency IDs and DAG order, three OR exits to RH, and refuses unsupported promotion. | TESTED MODEL / planned CI | `scripts/verify_succ_property_graph.py` is a checker of the **research map**, not a proof checker of nodes; test malformed dependency, REFUTED input and false exit labeling. |
| PB-04 | Success of all *checked* finite positive Gram blocks implies the global completed Weil form is PSD. | REFUTED | PB-01 is a decisive counterexample to the finite-input inference; does not rule out an all-K analytic theorem. |
| PB-05 | Existing source-first SUCC operators, Archimedean Gamma limit or PR59 critical boundary intrinsically identify a globally positive completed Weil form. | UNVERIFIED | Missing source-authenticated full Gamma/poles/conductor, universal test-domain identity and sign. Fake 6/non-Euler/self-dual completion controls required. |
| PB-06 | The three RH-facing exits (Weil sign / Nyman L2 closure / genuine self-adjoint spectral source) are mathematically the same proved theorem. | REFUTED as a claimed *proved* SUCC identification | They are alternative classical or conjectural strategies; no constructed SUCC intertwiners identify their source first. Their abstract equivalence to RH where established must be cited externally, not re-proved by DAG edges. |
| PB-07 | Suzuki 2026 finite-interval self-adjoint construction yields the conjectural uniform global spectral limit in Cor. 1.6. | UNVERIFIED | Primary source https://arxiv.org/abs/2606.09096 proves finite-interval machinery and states the RH-yielding limit conditionally. Next probe: source-derived compact-uniform estimates independent of the zeros. |

**No priority claim** for PB-01/PB-02, Hilbert-space positivity, Nyman–Beurling, Weil, Suzuki or Wold. The novel research artifact here is the scoped SUCC property/provenance map and falsification program, not a new theorem about the Riemann zeros.

Validation (do not pre-claim outcomes):

```sh
python scripts/verify_succ_property_graph.py
python -m unittest discover -s tests -p 'test_succ_property_graph.py'
python -m unittest discover -s tests -p 'test_property_obstruction_controls.py'
```

**Next verdict changer:** a correctly identified source-to-completed-Weil operator together with an all-test global sign, or a source-first globally convergent Nyman approximation; each must survive explicitly matched bad-source and wrong-completion controls.
