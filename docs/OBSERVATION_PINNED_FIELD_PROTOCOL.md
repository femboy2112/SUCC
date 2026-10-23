# Field protocol — physically pinning an arithmetic geometry without fitting the answer

**Status:** proposed preregistered experiment, NOT performed. The observed source, provenance, full state sensor, and independent higher-rung observation must be supplied by a human investigator. This protocol can validate an apparatus/model relation. It does **not** establish that physical spacetime is p-adic or uniquely holographic.

## 1. State the family before observing

The working family consists of *oriented cyclic p-clock source quotients* that might extend to a compatible ring tower Z/p^k. Candidate prime values must be declared in advance. A first-stage phase period p selects the member **within this family**, provided all p purported states are distinctly observable and the one-step event is identified independently.

The unverified empirical assumptions are: sensor faithfulness (no hidden aliases), reproducibility/stationarity of the one-step transition, source identity across stages, and validity of higher clock/ring quotients. The p-adic inverse limit is a conditional mathematical consequence of the full family law, never a theorem about an arbitrary natural phenomenon derived from one trace.

## 2. Pre-register two independent readouts

* Source A: choose a real system with a reproducible event and a reset origin. Independently label its actual phase outputs under repeated *single* events; no fabricated or simulator-generated phase labels can count as physical evidence.
* First-stage sensor: record at least two full cycles, verifying p distinct phase identities, cycle closure, and absence of drift. Verify p is one of the declared genuine primes. Do not silently assume the observations exhaust the physical hidden states.
* Holdout sensor: physically independent from the first readout if possible, with resolution capable of distinguishing p² fine phases. Record a full oriented cycle and coarse reduction to the first sensor, without using those values to reselect p.
* Holdout action: for all p² fine input states, independently enact and record the result of FUCC-p scaling. The model predicts output fine phase indexed by p*n mod p², *and* a total image of size p. Nonagreement rejects the source ring map or its physical realization.

A two-stage electronic binary counter makes the **apparatus** test concrete: low bit must cycle A,B and its independently measured two-bit register must cycle 00,01,10,11. Multiplication by two modulo four must hit only 00 and 10. This does not show that an unconstrained physical system has binary ontology; it checks whether a stated clock and its carry law are physically reproduced.

## 3. Exact input to the available protocol checker

Run:

`PYTHONPATH=. python scripts/physical_clock_observation_contract.py --input /path/to/independently_recorded_phases.json`

This is an **illustrative synthetic fixture** (NOT an actual observation; replace every value with independently collected source records):

```json
{
  "source_id": "SYNTHETIC_EXAMPLE_NOT_OBSERVED",
  "instrument_id": "SYNTHETIC_EXAMPLE_SENSOR",
  "candidate_primes": [2, 3, 5, 7],
  "phase_labels": ["A", "B", "A", "B", "A"],
  "second_level": {
    "phase_labels": ["00", "01", "10", "11", "00"],
    "coarse_phase_for_fine_sequence": ["A", "B", "A", "B"],
    "multiplier_p_outputs": ["00", "10", "00", "10"]
  }
}
```

The script accepts no physical sensor connection, and cannot authenticate the provenance of the JSON. A passed report says only that the **recorded statements** satisfy the preregistered finite source contracts. It deliberately reports `physical_measurement_authentication_by_script=false` and `source_hypotheses_global_verified=false`. Missing held-out observations remain NOT_SUPPLIED, never success by default.

## 4. Independent falsifiers and no-go controls

- Missing or aliased p phases, or an observed nonprime primitive cycle outside the candidate family, cannot be silently upgraded.
- A physically four-state source read through parity alone mimics a two-state clock; this observer/source-alias defect must be ruled out separately.
- The second-level ring model F_p[t]/t² has the **same first-shell residue cardinality** as Z/p² but behaves differently under p-fold multiplication: zero instead of a nonzero state. The holdout is designed to expose that difference.
- Even genuine agreement at finite depth K cannot rule out a compatible counterfeit tower that matches through K and changes at K+1. The *full p-power tower axiom* is a mathematical/empirical commitment not validated by finite checking.
- Equivalent source topology admits different metrics and quantum states. A further **held-out geometric or quantum correlation** is necessary before promoting a particular physical geometry.

## 5. What is being selected

Under the complete source tower and rank-two projective lift, the mathematical source uniquely determines the Z_p coset tree, the full PGL2(Q_p) Bruhat–Tits tree, the SUCC p-cycle/fixed-infinity root-shell signature, and the FUCC-p canonical axis. The physical experiment may select p and corroborate specific maps on a real apparatus, but a claim of universal physical geometry must earn additional independent evidence and source realization.

The next mathematical objective is to identify an actual measured correlation whose value differentiates two genuine SUCC-equivariant quantum states on that canonical p-adic geometry.
