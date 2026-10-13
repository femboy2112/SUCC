# Evolutionary obstruction synthesis — research entry point

This is the bounded implementation of the six-part continuation of genetic fusion PR #43. It lives on `research/evolutionary-obstruction-synthesis-2026-10-13`, draft PR #45, and does not change main or rewrite earlier research claims.

## Read first

- [Complete EO1–EO11 proofs and limitations](../research/2026-10-13/EVOLUTIONARY_OBSTRUCTION_SYNTHESIS.md).
- [Namespaced claim supplement](CLAIM_SUPPLEMENT_EVOLUTIONARY_SYNTHESIS.md). Namespaced IDs avoid repeating the branch-local O-number collisions recorded by the consolidation audits. The inherited canonical ledger is left intact.
- [Precommitted experiment design](../research/2026-10-13/DISCOVERY_PRECOMMIT.json), committed before holdout evaluation at `93d67f25b1552f0aa78aff0589ca1a59baa32f7a`.
- [Exact generated receipt](../research/2026-10-13/EVOLUTIONARY_OBSTRUCTION_RECEIPT.json).
- [Universal Lean kernel](../formal/obstruction_synthesis/RepairKernel.lean) and [the actually learned finite instance](../formal/obstruction_synthesis/DiscoveredInstance.lean).

## Six requests and their implemented boundaries

| Requested direction | Constructed | Boundary |
|---|---|---|
| Richer categorical alphabet | Experiment words, behavioural quotient objects, induced action functors, comparison maps, predicate adjunction, action monoids | These metaconstructors are supplied; arbitrary categories are not invented |
| Counterexample-driven evolution | Necessary separations; immutable learned bridge alleles; genuine constrained permutation crossover/mutation | Strong complete finite verifier supplies the progress guarantee |
| Source-aware probabilities | Conditional products, Bayes/gluing square, uncertain coupling family, bridge-population likelihood adapter | Independence/calibration are hypotheses, confidence is not proof |
| Partial/noisy/changing source | Open transition entries, exact original/current posterior, delayed causal replay, transactional rejection | No unknown-domain universal certification or physical source authentication |
| Formalization | 15 universal Lean declarations and 9 finite learned-table theorems; explicit axiom inventory and false-theorem control | Python implementation, finite runtime bound and stochastic subsystem are not fully mechanized |
| Unknown-to-E invariant | Opaque-label calibration/holdouts discover a central nontrivial commutator and minimal state size | Complete mathematical source tables; classical finite Heisenberg-type result, not human novelty |

## Interfaces

`evolving_observer_categories.py` constructs the coarsest action-stable observer from primitive readouts. Failed update squares create new experiment programs. A backward pair-automaton oracle checks the final quotient independently.

`evolving_bridge_search.py` extends the existing typed genetic capsules. Counterexamples become permanent semantic constraints; no factorial rescue is used. Original unsuccessful seeds remain checked as failures of the predecessor search.

`source_aware_amalgamation.py` handles conditional probability crossover and noisy state-changing evidence. It retains the original source coordinate after destructive updates, and rejects source/basis changes, duplicated events and unlicensed independence.

`obstruction_discovery_lab.py` keeps latent coordinates in the simulator. The learner sees source tables and readouts only. A generic law miner constructs compositions, inverses, centers and orders from the learned action object; no target group law is passed as an answer.

## Reproduction from this branch

```sh
python -m pip install -e '.[test]'
python -m unittest discover -s tests -p 'test_evolving_*.py' -v
python scripts/evolutionary_obstruction_probe.py > /tmp/evolution.json
diff -u research/2026-10-13/EVOLUTIONARY_OBSTRUCTION_RECEIPT.json /tmp/evolution.json
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
# With Lean 4.19.0 installed:
lean -DwarningAsError=true formal/obstruction_synthesis/RepairKernel.lean
lean -DwarningAsError=true formal/obstruction_synthesis/DiscoveredInstance.lean
```

The dedicated CI job pins the Lean release and checks an intentionally false theorem is rejected. A printed compiler error from that negative control is expected; the enclosing workflow must succeed only when the rejection occurs.

## Highest-value next work

Replace the complete-model verifier by justified experiment access without silently treating sampling as equivalence certification. Then extend stochastic minimality to carry complete joint dependence and formalize program-to-kernel refinement. The current framework grows its experiment language, not its unrestricted meta-language. No RH, Weil positivity, physical entanglement or independent scholarly novelty follows.
