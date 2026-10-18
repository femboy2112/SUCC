# OM — Oriented Möbius counting, projective-to-Tate local transport and Connes tests

**Parent:** research/connes-oriented-local-trace-2026-10-18@64aa0810d9016c9c6948034d0543424f46db011e (draft PR #169).
**Source note:** research/2026-10-18/ORIENTED_COUNTING_TO_ADELIC_TRACE.md.
**Implementation:** four modules oriented_mobius_adelic.py, radial_projective_trace_bridge.py, full_prime_tower_transport.py and connes_compact_open_test_bridge.py in observational_succ; four corresponding test files in tests; focused workflow for Python 3.10/3.13.
**Provenance:** classical Grothendieck completion, Möbius/Boolean incidence algebra, Tate local zeta integrals, Bruhat–Tits PGL2(Qp) p+1 tree, Connes fixed-point local trace formula and normalization, idelic product formula. New-to-project exact interfaces and counterexamples, **no new academic mathematical priority asserted**.

| ID | Status and strict result |
|---|---|
| OM-01 | **PROVED CLASSICAL:** signed count is group completion of finite-set disjoint-union monoid, pairs (a,b) mod simultaneous cancellation. Sign reversal is additive but not multiplicative/unital (maps 1 to -1). |
| OM-02 | **PROVED CLASSICAL:** on every finite Boolean squarefree prime-set poset, incidence Möbius M = J Z J = Z^-1, J(S)=(-1)^|S|. The negative first form is an exact orientation conjugate of coordinatewise nonnegative cumulative incidence counting. INCIDENCE Z is non-Hermitian, not asserted PSD. |
| OM-03 | **PROVED COUNTERMODEL:** full chain 1,p,p² has true Möbius 0 at (1,p²) versus parity JZJ coefficient +1. Liouville λ(p²)=+1 versus Möbius μ(p²)=0. Actual original integer SUCC sign cocycle is nonconstant. |
| OM-04 | **PROVED SOURCE-TYPED / CLASSICAL:** conditioned full local Tate geometric shell P(k)=(1-p^-β)p^-βk on k<=1 yields projective two-state p/(p+1), 1/(p+1) at β=1; distinct from coarse P(k>=1)=1/p. Actual full p^k Tate Euler for β>1 is (1-p^-β)^-1, sign-twisted local linear factor is (1+p^-β)^-1. Ramified chi_-3 omitted local Euler p=3 handled separately. |
| OM-05 | **PROVED EXACT LOCAL THREE-ROUTE:** PGL2 tree spheres N_k=(p+1)p^(k-1), k>=1; declared normalization ((p+1)/p)/N_k=p^-k equals authentic squared Connes half-density and one-place Tate idèle norm. Recover magnitudes for ALL prime-power jets and cross-check a finite entire p^k tape against the pinned original von Mangoldt labels, not global trace. Radial root boundary defect is indefinite rank two and not identified with canonical Weil contact. |
| OM-06 | **PROVED CLASSICAL GENUINE TEST:** for p-adic compact-open B=u0+p^r Zp disjoint from zero/identity, the Connes local off-identity pairing is p^-r/((1-p^-1)|u0|p|1-u0|p); normalized Haar independently counted on unit source balls. Reciprocal half-density pairing invariant. Does NOT resolve singular principal value. |
| OM-07 | **PROVED NO-GO WITH HYPOTHESES:** finite idelic valuation parity χ_f=∏(-1)^vp cannot be canceled on diagonal all rationals by one continuous unitary Archimedean norm character x^(it); 2 and3 already contradict unique factorization. Not a no-go for ramified global Hecke characters. True norm phases p^-it do descend by rational product formula. |
| OM-09 | **PROVED CLASSICAL ON Re(s)>1:** true number-theoretic Möbius inversion 1*μ=δ cancels every genuine finite Euler factor, leaving the real Tate Γ_R(s) from Γ_R(s)ζ(s)·1/ζ(s); finite prime stages and even-integer Γ_R=integer·π^integer cross-checked with original Tate source. Incorrect p+1 norm, uniform negative full-tower factor and omitted prime mutants DO NOT cancel. No inversion at unknown critical-line zeros, no all-test Weil PSD. |
| OM-08 | **UNVERIFIED:** PGL2-to-GL1 spherical trace intertwining on full all-place test algebra; completed Connes principal-value/global signed Weil distribution identity including one Γ and poles/contact; source-derived all-test Weil PSD and RH. |

**Positive and hostile controls:** original p2,p3,p5, higher p^k, fake p6, Boolean Möbius and p² repeat mutation, exact signed Grothendieck unit, Liouville orientation of real SUCC, exact product-formula phase coefficients, full tower against inherited Tate Euler, projective conditioning != coarse-graining, authentic p-adic compact-open Haar independent residues, reciprocal scaling, χ_-3 conductor/ramified p3, known missing singular trace and Gamma/poles.

**Reproduction:**

python -m unittest discover -s tests -p 'test_oriented_mobius_adelic.py' -v

python -m unittest discover -s tests -p 'test_radial_projective_trace_bridge.py' -v

python -m unittest discover -s tests -p 'test_full_prime_tower_transport.py' -v

python -m unittest discover -s tests -p 'test_connes_compact_open_test_bridge.py' -v

python scripts/verify_provenance.py

**RH PROVED: NO.** All universal statements are justified by paper proof/classical theorem, not by exhaustive sampling. No new physical causal source authentication.
