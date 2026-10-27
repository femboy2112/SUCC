# Prime-7 / Gaussian second-round claim ledger

Actual parent: #327, `76f3799658fde8a2eff649b0bd4926a2173918d0`.
Read-only source sibling: #325, `95ee2f1fab851afe1517d8ec5a0589885842426f`.
`PROVED` means a paper proof with an internal audit, not a Lean theorem,
external peer review, or a priority claim. All inherited statuses remain as
recorded upstream. π normality and the selected real signed-cancellation
estimate remain OPEN.

| ID | Exact domain and claim | Status | Proof, countermodel and next falsifier |
|---|---|---|---|
| P7R-01 | Fixed prime p≥7, q=p^L: exact quadratic fiber spectrum, Haar masses m_a/q, and largest fiber p^{L/2} for even L or 2p^{(L−1)/2} for odd L | PROVED | [Quadratic proof §1](../research/2026-10-27/PI_QUADRATIC_FIBER_ENERGY_OBSTRUCTION.md); critical fibers and p=241 are explicit controls |
| P7R-02 | For every prescribed q(N)=p^{L(N)}→∞, q=o(N), one base-16 normal α with μ(α)≤4 has liminf C_A(2^j,q(2^j),h)≥1/4 for every fixed integer h≠0 | PROVED | Same proof §4; complete bounded-fiber truncation, dependent cyclic-phase moments, marker and all-prefix argument. A proof relying only on fine/coarse monotonicity is rejected |
| P7R-03 | One augmented choice of the same α also has liminf H_A and empirical conditional norm Q_A at least p/[8(p+1)] | PROVED | Same proof §7; orthogonal averaging projection, weighted Cauchy and exact empirical-bin counts. Tests N<q and empty bins; not a claim about every previously selected α |
| P7R-04 | P7R-02/03 transfer under the authentic Green tail to the same forcing at V_0=(α−π)/16; H_A error ≤4π|h|B(1+q/N)/N and Q_A error ≤4π|h|B/N | PROVED | Same proof §§3,7.4–7.5; changed selector explicitly retained, no invented p-adic state for irrational V_n |
| P7R-05 | Full projective source on affine time at 7: C_1=(12L+7)7^{L−1}, C_2=7^L+2, C_3=7^L for every L≥1; three consecutive samples are minimal for reconstruction | PROVED | [Delay proof](../research/2026-10-27/PI_FULL_SOURCE_DELAY_RECONSTRUCTION.md); pole disks retained, integral Morse lemma, unit two-variable Jacobian. Pair {24,30} at depth 2 refutes two-sample injectivity |
| P7R-06 | Corresponding all-level holdouts at 11: ((10L+17)11^{L−1},11^L+2,11^L); at 241: ((240L+257)241^{L−1},241^L,241^L) | PROVED | Same lifting proof plus exact finite certificates; fresh opposite-chart 241² counts (177617,58081,58081) |
| P7R-07 | For all N≥1 and unit-bounded phases, two-delay energy at 7/11 differs from E by one signed term of absolute value ≤(2/q)(1+q/N)²; three-delay energy equals E | PROVED | Delay proof §6; positive and negative Gaussian-weight controls, future-selected −T_n. Real cancellation sign remains missing |
| P7R-08 | Exact joint (A,D) collision laws: generic Legendre criterion, p31 injectivity, exceptional p109/251 counts; unit numerator shifts reconstruct time, arbitrary shift count q+min(v_p(s),L)(p−1)p^{L−1} | PROVED | [Joint-source proof](../research/2026-10-27/PI_JOINT_SOURCE_OBSERVATION.md); all constants checked as polynomial coefficients. O(1/q) energy comparison fails at 109/251 and is not claimed there |
| P7R-09 | For q=7^L,L≥2,7∤a, complete source character sum over D-unit inputs has magnitude ≤2√q; regular numerator-mirror sum vanishes | PROVED | [Modular proof §§2–3](../research/2026-10-27/PI_PRIME7_MODULAR_REAL_BRIDGE.md); elementary Morse/Gauss proof. First-depth mirror value 1 rejects extension to L=1 |
| P7R-10 | The periodic regular modular source-character model has C_A=2/7 on every complete number of periods, despite scalar O(q^{-1/2}) | PROVED | Modular proof §4; triangular modular model, zero pole weights, not a fixed π orbit. L=1 energy is 3/7 |
| P7R-11 | Scalar A-label and ordinary time-label refinement obey an exact nonnegative child-difference identity for every N, without balance or endpoint error | PROVED | Modular proof §5; sharpens the earlier approximate comparison. Joint labels with the same prefactor do not satisfy the same p-child premise |
| P7R-12 | Ψ exactly preserves Z₂ and its transverse valuations; finite λ^m successor has 2^{floor(m/2)} cycles of length 2^{ceil(m/2)}; even-depth conjugation-fixed set is twice the rational sector | PROVED | [Gaussian proof §§2–3](../research/2026-10-27/PI_GAUSSIAN_DESCENT_PHASE_OBSTRUCTION.md); i mod2 refutes finite fixed⇒rational, odd-level quotients tested separately |
| P7R-13 | For every h≠0,m≥1 and arbitrary finite-clock g, sup_n |e(hU_n)−g(U_n modλ^m)|>47/39168; no continuous completed-clock extension exists | PROVED | Gaussian proof §§4,7; explicit positive source bounds and phase-pair recurrence. Uniform norm only, not an L² or density obstruction and not a zero-selector advantage |
| P7R-14 | Rational modular/real cofactor identities; actual real source echo tends to 1 while the modular source sum has square-root cancellation | PROVED | Modular proof §6; genuine local conductor versus artificial conductor explicitly separated. u=1/2 is an exact missing-cofactor control |
| P7R-15 | Authentic finite signed mirror contribution is always nonpositive; authentic C_A decreases with N doubling; prime-power collisions are only diagonal and full reflection | REFUTED in stated finite scopes | [Instrument findings](../research/2026-10-27/PI_PRIME7_INSTRUMENT_FINDINGS.md): rigorous intervals of both signs, doubling increases, and nonzero mixed-valuation contributions |
| P7R-16 | 144 rational-enclosed phase rows; 108 exact modular/refinement/kernel cases; Gaussian and projective holdouts; exact proper-Haar stability cases | VERIFIED_FINITE | [Validation](../research/2026-10-27/PI_PRIME7_ROUND2_VALIDATION.md), raw receipts and SHA-256 manifest; finite checks do not prove limits |
| P7R-17 | Source-and-zero-selected real cofactor decorrelation, authentic C_A/H_A/Q_A→0, o(N) π Weyl sum, π normality | OPEN | No conditional independence or signed saving has been assumed. A new estimate must actually exclude same-forcing changed selectors and the #320 rational-source control |
| P7R-18 | Any prescribed deterministic partition of q(N) residues with q→∞,q=o(N),k_q/q→κ>0 admits a normal α with μ≤4 and dyadic proper-Haar/empirical energy liminf≥κ/4 for every fixed h; any fixed finite collection can be simultaneous | PROVED | [Fresh two-bit extension §3](../research/2026-10-27/PI_TWO_BIT_PARTITION_MEMORY_OBSTRUCTION.md); partitions must be fixed before auxiliary word selection. Partial (A,sheet,pole) gives p/[4(p+1)], or 7/32 at 7; full code is E |
| P7R-19 | Any autonomous successor quotient retaining A is injective; partial two-bit code at L≥2 has exact Markov order two, conditional entropy log(p)(1−p^{-floor(L/2)})/(p−1), and entropy rate zero | PROVED | Same extension §6; uniform finite-time probability, realized cells only, not a π-phase stochastic model. Adjacent A-values reconstruct x exactly |

The decisive new implication failure is P7R-02/03, including the proper
empirical conditional norm. The strongest positive source-specific results
are exact reconstruction and modular cancellation. These are kept separate
from P7R-17. No theorem here claims that all countermodels satisfy every
authentic zero-selected arithmetic hypothesis simultaneously.

See [the round synthesis](../research/2026-10-27/PI_PRIME7_ROUND2_SYNTHESIS.md)
for the explicit next proof obligation and the limits of Hypothesis A,
Gaussian Haar averaging and p-adic stationary phase.
