# Validation and authority boundaries — prime-character primal quotient

**Parent:** SUCC PR #497 pinned `4383bd31340af700e312f13d7ef28af090c152d5`. The first declaration `f41b75c8fbb28ef52e6e696f492ec7e6193e0c65` precedes new prime source holdouts; the second primal-saturation declaration `f1723146dd5141d65a3891cca95fe9418a7ff37a` precedes new big-N denominator/pulse holdouts. The initial group-action derivation and first small prime signs were DEVELOPMENT before preregistration, **not falsely presented as blind validation**. Mathematical proofs and finite source executions share one reasoner and one source lineage.

## Commands actually executed in isolated staging

```
cd /mnt/data/succ_prime_primal
python -m unittest discover -s tests -p 'test_prime_character_primal.py' -v
python research/2026-11-04/prime_character_primal/symbolic_oracle.py
python research/2026-11-04/prime_character_primal/probe.py --verify
python -m compileall -q research/2026-11-04/prime_character_primal tests/test_prime_character_primal.py
```

- **26/26 exact focused tests PASS, 0 errors/skips**, final stdout/stderr in TEST_LOG.txt.
- **Independent SymPy source action/pole oracle PASS:** 16 group composition cells on the full Q^8, 4 character projectors and eigen-dimensions, source p#/P action and 2×2 minimal Hankel, rational kernels, odd-denominator source identity, **32 symbolic all-k primal p-pulse identities**, strict positive prefix bound and leading n−1 source cancellation.
- **63 predeclared original p,k prime readouts PASS**, with independent direct original-time p-local recurrence. Actual full Fraction `pU_(kp)` compared separately on a nine-prime/two-time subset. Further 8-tap basis probes (all 8 slots across multiple p classes) passed: generic group representation is not a fitted identity on P.
- **Four original/primal source-selected triangular J-energy finite exact checks PASS**, including q=8 at A=32. Signed original U and source primal Y are read from distinct source moment functions, no artificial Galois ensemble.
- **Fresh all-event angular p holdouts** at multiplier indices m=17,37,71,113,191 and classes a=1,3,5,7: 20 exact rational pulse states match an independently accumulated original p-event clock.
- **Fresh reduced denominators** at n=128,257,509,911,1511: original angular eight-tap Fraction recurrence agrees with an independent source-polynomial / integer-LCM recurrence. Reduced denominator log-per-N values are recorded in FINITE_RECEIPT.json and approach ~8; they do **not** prove the asymptotic, which comes from all-pulse strict positivity and classical PNT.
- **Primal real-state p-survival finite checks** at n=128/257/509: 159+295+542=**996** original selected simple-pole primes, all predicted modular residues agree with exact unwrapped state; no cancellation in those declared finite simple-pole ranges. Finite small-prime cancellation is still permitted by the all-N asymptotic theorem.
- **Source mutation controls:** altered coefficient tap, false Legendre sign, full p-primary congruences for arbitrary eight-tap basis, exact p-integral wrong-seed blind spot, primitive 2-adic odd inverse branch, positive nonvanishing radial finite channel, signed-base-4 recurrence, source fixed real Weyl comparison and selected J bound. No use of externally supplied π digits.
- **Deterministic receipt replay PASS**, with SHA256 digests over finite p pulses, large integer reduced denominators (big-endian representation), source state rational hashes and selected current energies.
- Python `compileall` PASS for new code and root test. A simple SymPy expression **structural equality** assertion was corrected to rational cancellation; one Python >=3.11 integer-to-decimal string length guard in the new receipt was repaired by hashing the actual big-endian denominator bytes. These were test/instrument issues, not changes to the source or mathematical claim; final rerun passed.

## What this does NOT establish

**NOT CLAIMED:** full native 11k+ SUCC suite; root provenance, observer and ordinal tests in the actual repository checkout; new Lean compilation; global mathematics academic-first novelty; blind independent proof referee; original fixed-h Weyl saving; selected current o(K); π normality; RH; physical quantum amplitudes. The exact all-k V4 and primal pulse identities are paper proofs with independent-implementation checks, not published referee certificates. The prime-number theorem in fixed-modulus progressions is an imported classical theorem.

For native integration, obey AGENTS.md and re-run exactly on the integration HEAD:

```
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Verify hosted CI separately on the actual PR HEAD; earlier ancestral workflow passes cannot certify this new head.
