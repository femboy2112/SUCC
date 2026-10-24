# Twisted observer agreement — source-scoped claim supplement

**Namespace:** TWA. **Date:** 2026-10-24. **Base:** main e648df3.
**Authority:** paper proofs and exact finite checks. No new Lean declarations.
**Pi normality: OPEN. Independence: NOT ESTABLISHED. Scholarly priority: UNVERIFIED.**

Full hypotheses, proofs and source boundaries are in the
[dossier](../research/2026-10-24/PI_TWISTED_OBSERVER_AGREEMENT.md).
Validation is recorded [separately](../research/2026-10-24/PI_TWISTED_OBSERVER_VALIDATION.md).

| ID | Statement | Earned status and boundary |
|---|---|---|
| TWA-01 | The authentic four-pole forcing, zero-initial states and first-window complements have odd reduced denominators | PROVED LOCAL, all indices; exact independent forcing implementation. This excludes literal half-turn source states |
| TWA-02 | A target character descends through an observation quotient exactly when it annihilates its kernel; no nonzero archimedean character descends through a single p-primary observer | PROVED LOCAL / classical factorization. Does not invalidate equality of quotient observations |
| TWA-03 | A recorded Z2 wire connection recovers every signed lag correlation and sum magnitude up to an irrelevant global sign | PROVED LOCAL / exact finite controls. Dropping transport can manufacture cancellation |
| TWA-04 | Same-forcing synchronous differences erase the common source selector; even-radix antiphase error has sharp lower bound 1/(2(b+1)) across two times | PROVED LOCAL, all forcing sequences; 1/34 at radix 16. Does not exclude time-index pairing |
| TWA-05 | Doubling is injective on odd torsion but its inverse is not uniformly continuous; sharp q-torsion metric constant (q-1)/2 | PROVED LOCAL with exact witnesses. Exact agreement is distinct from stable agreement |
| TWA-06 | Finite gain probes have full-circle injectivity and uniform coercivity iff gcd=1; odd-torsion injectivity iff gcd is a power of two | PROVED LOCAL via kernel, Bezout and density arguments. No physical access is assumed |
| TWA-07 | Gains 2 and 3 obey the sharp residual squared-norm inequality with constant 4/3 | PROVED LOCAL with exact algebraic equality witness. Small actual-source mismatch is not proved or necessary for normality |
| TWA-08 | Shared time-residue projections leave an unrestricted signed residual covariance; the exact difference-pair formula preserves it under pair orientation swaps | PROVED LOCAL; residual examples +1,-1,i have identical shared readouts and energies |
| TWA-09 | Every T16-invariant sum law admits a joint law with identical Haar marginal and differential history laws; all variation within this constructed family sits on the (h,h) Fourier diagonal | PROVED LOCAL / classical Haar ingredients / exact finite controls. Countermodels do not preserve selected BBP y0=0; joint observer laws are a stronger probe |
| TWA-10 | Actual prime-window joint empirical measures are approximately T16 x T16 invariant, with an explicit boundary and forcing bound | PROVED LOCAL. Invariance and Haar marginals cannot exclude the resonant Fourier diagonal |
| TWA-11 | Common initial shifts preserve both wire forcing laws and their all-time differential while changing a selected finite-window collision count | PROVED LOCAL construction / TESTED MODEL. Explicitly changes initial selector and specified primary data; not an authentic-source or asymptotic counterexample |
| TWA-12 | Signed zero-extended temporal energy gives the exact finite van der Corput factor and an all-width O_h(p^-2) BBP-to-pi transport budget | CLASSICAL inequality / PROVED LOCAL source application / exact interval checks. Transport does not estimate cancellation |
| TWA-13 | Vanishing iterated-limit temporal energy for every fixed nonzero h on the dense good-prime family is equivalent to base-16 normality | PROVED LOCAL / CLASSICAL EQUIVALENCE. Inner p-limit fixes H; the source-specific limit remains UNVERIFIED |
| TWA-14 | Actual p41/p73 near-half-turn witnesses, prescribed temporal energies and p2081 collision replay are certified; the absolute coprime-gain cancellation budget is vacuous on fresh p193/353/577 windows | TESTED MODEL / VERIFIED EXACT FINITE. No fitted exponent, infinite inference, or new Lean authority |
| TWA-15 | Authentic collisions satisfy an exact inverse-branch inclusion and centered-carry gate; uniform central-branch loss across all or a positive proportion of prescribed scales would give a first polynomial collision saving | PROVED LOCAL finite geometry / PROVED CONDITIONAL implication. The selected-source branch-loss premise is OPEN; theta=1/2 yields only K=O(p^(3/10)) in the all-scale case. Cantor comparison is a population analogue |

## Reproduction

```sh
python -m unittest tests.test_twisted_observer_probe tests.test_twisted_pair_transport tests.test_twisted_observer_joining tests.test_twisted_source_energy
python -m scripts.twisted_pair_transport_oracle
python -m scripts.twisted_observer_joining_oracle
python scripts/twisted_source_energy_probe.py --output /tmp/twisted-source-energy.json
python scripts/twisted_observer_common_shift_probe.py
python scripts/twisted_coprime_gain_probe.py
python scripts/twisted_inverse_branch_oracle.py
```

The full validation record retains exact source hashes and required repository
gates. The single-gain, independent-marginals, omitted-transport and same-forcing
antiphase failure mechanisms remain explicit regression controls.
