# Minimal Genesis / first-carry source proof ledger (research-only)

Research branch: research/minimal-genesis-first-carry-2026-10-24,
parent #257 at 5435497dc77a313d1ebbc56ac96c11e593db2619.
Main and the original signed sources were not changed.

| Local ID | Precisely scoped mathematical statement | Authority | Hostile control |
|---|---|---|---|
| MG-01 | Haar-origin base-b orbit 2k-moments equal independent-phase moments for 0<=k<=b, all N | CLASSICAL/PROVED PAPER; exact independent oracles | Source x=0 still nonnormal |
| MG-02 | The first nonzero 2k-moment carry occurs k=b+1; exact excess 2(b+1)(N−2)+(b+1)^2(N−2)(N−3) | PROVED PAPER / EXACT FINITE TESTED | Adjacent/nonadjacent carry channels and b=2 two-carry edge |
| MG-03 | Exact Haar high-moment finite q-grid iff no source k-sum aliases mod q, for k<=b; necessary q>=C(N+k−1,k) | CLASSICAL / PROVED PAPER / TESTED | Composite/nonunit clocks and aliased residues |
| MG-03a | For b16,N3,k16 the minimal unit clock is q277; the nonunit grid q274 is smaller but does not preserve multiplier bijectivity | EXACT FINITE PROOF BY EXHAUSTIVE SEARCH; not a universal asymptotic | All smaller q checked; root-of-unity moment re-evaluated |
| MG-04 | Authentic BBP Green tail is the unique ell²/ell¹ causal section; ||(16I-L)^−1||=1/15 exactly | CLASSICAL SHIFT RESOLVENT / PROVED PAPER; rational finite tests | Rational nonnormal source obeys same finite-energy principle |
| MG-05a | No nonzero bounded linear intertwiner J between strongly stable BBP spectral multiplication U and Haar Koopman isometry K16 | PROVED PAPER; finite exact permutation controls | Spectral atom u=1 invalidates strong stability |
| MG-05b | Continuous autonomous semiconjugacy from connected strongly stable Hilbert source to expanding circle is constant; π orbit cannot be image even on one source orbit by a continuous-at-zero equivariance | PROVED PAPER, not Lean checked | Preperiodic rational phases can be mapped on selected countable orbit |
| MG-06 | Source-blind least squared-chord-motion action is minimized exactly at b−1 rational fixed origins | CLASSICAL / PAPER / EXACT FINITE TESTED | For b16 all 15 minimizers nonnormal |
| MG-07 | Actual π-signed cyclotomic lag and prime-clock high-mode overlap cancellation | **OPEN / UNVERIFIED** | #258 synchronized anti-clock creates maximal interference with a one-step rule |

No newly added Lean theorem. The Python 3.10/3.13
dedicated workflow and frozen receipt are finite checks
only. Full inherited suite must be evaluated at the
single submitted commit, not inferred from parent
#257 and #253. All statements of independent academic
novelty are UNVERIFIED.

Proof source: research/2026-10-24/MINIMAL_GENESIS_CARRY_AND_GREEN.md
Rational implementations:
observational_succ/minimal_circle_carry.py,
observational_succ/minimal_moment_clock.py,
observational_succ/minimal_green_obstruction.py.
Tests: test_minimal_circle_carry.py, test_minimal_moment_clock.py.
