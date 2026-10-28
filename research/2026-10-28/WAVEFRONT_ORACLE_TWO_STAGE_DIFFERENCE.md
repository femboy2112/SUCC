# Wavefront Oracle → E1 → E2: a source-conditioned second finite-difference theorem

**Date:** 2026-10-28. **Branch target:** `research/pisot-hopf-arithmetic-relativity-2026-10-28`, based on Main XIII `b763ba8ef375fbac221e29e4396989a635a6ef36`. **Status:** locally rederived and exactly tested observer/filter theorem. **π normality, RH, GR physics, and observer-optimality: NOT PROVED.** Do not merge to `main` without reviewed independent validation.

## 0. Steelman and type discipline

The wavefront is an ideal **oracle** `W_t` that has the current source state. `E1_t` is the first observer with at least one tick causal delay; `E2_t` is **constructed from the reports of E1**, also with at least one further tick. The source may have independent innovations (stochastic epistemic model), predetermined arithmetic forcing (authentic BBP model), or a declared finite symbolic language. These are different source types. Being unable to receive an event is not the same as being unable to predict its content. A geometric ray traveling with maximum speed is a null process, not a massive timelike observer worldline.

Existing SUCC relations to preserve:
- Main XIII `research/2026-10-12/COVARIANT_PERCEPTUAL_MOMENTUM_AND_CAUSAL_DESCENT.md` CV1–CV10 distinguishes causal ancestry/downsets, coordinate simultaneity, and evidence verification. No simultaneous slice is assumed.
- Main XIII `research/2026-10-18/INSTITUTE_CAUSAL_DESCENT.md` requires kernel/fiber congruence for lawful observable transport; an attractive observer diagram alone is insufficient.
- Main XIII `research/2026-10-13/SUZUKI_FIRST_PRIME_WAVEFRONT.md` is a genuine **prime spectral** wavefront at `2a=log 2`, not the moving-front model below. There is no asserted physical identity.
- Main XIII `research/2026-10-27/OILY_ZERO_ONE_LOG_GERM_BRIDGE.md` and `observational_succ/rank_two_chiral_towers.py` supply the literal positive Oily packets and authentic *signed* BBP forcing separately; the expanding original zero-seeded phase remains the π-normality target.
- Local staged `research/2026-10-28/CAUSAL_WAVEFRONT_GAMMA_INFORMATION_DEFECT.md` supplies causal geometry, harmonic sampling, and Oily Gamma(2) KL comparison; this is a **new, complementary** exact recursion, not a rewrite of those results.

## 1. The bare wavefront transport equation (no probabilistic assumptions)

Let the oracle be `W(t)` for t in the nonnegative integers, extended by zero to negative t. A perfectly faithful k-step **receipt** observer has `E_k(t)=W(t-k)` for t≥k. It obeys the exact discrete traveling-wave law

`E_(k+1)(t+1)=E_k(t)`.

If L shifts time backward, `(L f)(t)=f(t-1)`, then `E_k=L^k W`. The discrete transport can be written `(T_t T_k-I)E=0`, with `T_t E_k(t)=E_k(t+1)` and `T_k E_k(t)=E_(k+1)(t)`; this only means exact **causal retardation** on a shared clock. In particular `E1(t)=W(t-1)`, `E2(t)=W(t-2)`, and the depth difference `E1(t)-E2(t)=W(t-1)-W(t-2)` is an exact first finite difference of the source.

This is not yet an information deficit, because W might be fully deterministic and reconstructible. It has no Euler–Mascheroni constant without additional source structure.

## 2. An exact two-stage Oily source-conditioned realization

The actual Oily positive BBP packet source has

`u(x)=x-x²/2`, `v(x)=x²/2`,

`p_j(x)=(1-x)/4 Σ_(k=0)^j u(x)^k v(x)^(j-k)` for x in [0,1].

The total ungraded positive source is

`R(x)=Σ_j p_j(x)=(1-x)/[(2-x²)(x²-2x+2)]`.

For x<1 normalize a grade distribution `q_j(x)=p_j(x)/R(x)`. Its **unique normalized PGF** is

`G_x(z)=Σ_(j≥0) q_j(x)z^j=[(1-u)/(1-uz)] [(1-v)/(1-vz)]`.

This factorization *permits* a model in which independent conditional geometric waiting times `J1`, `J2` have `P(J1=k)=(1-u)u^k`, `P(J2=k)=(1-v)v^k`, and `J=J1+J2` has grade probabilities q_j. Independence of these constructed latent waiting times is **not a theorem about BBP's physical observation process or its integer carry sequence**. Other hidden interpretations can yield the same marginal law.

Define retarded causal finite filters at fixed x:

`E1(t) - u E1(t-1) = (1-u) W(t-1)`,

`E2(t) - v E2(t-1) = (1-v) E1(t-1)`;

all negative-time states are zero. Each additional stage has at least one tick of latency. Eliminating E1 gives the *exact second-order recursion*

**(WEO-01)**

`E2(t) - x E2(t-1) + [x³(2-x)/4] E2(t-2) = (1-u)(1-v) W(t-2)`.

Equivalently, using the shift operator L,

`(1-u L)(1-v L) E2 = (1-u)(1-v) L² W`.

This has impulse response `E2(2+j)=q_j(x)` to the oracle input W(0)=1, W(t>0)=0. The original source distribution enters *exactly* as the relative waiting-time response; no fitted coefficients are involved. The one- and two-step rates are source-derived; **the statement that they are optimal observer processing laws is a separate unproved model-choice premise**.

## 3. A direct recursive knowledge boundary differential

Let `D(t)=E1(t)-E2(t)`. The second filter equation yields

**(WEO-02)** `D(t)-v D(t-1)=E1(t)-E1(t-1)`.

Meanwhile the first filter gives

`E1(t)-E1(t-1)=(1-u)[W(t-1)-E1(t-1)]`.

Combining:

**(WEO-03)**

`D(t)=v D(t-1)+(1-u)[W(t-1)-E1(t-1)]`.

This is the requested explicit observer-depth finite difference: the E1-to-E2 lag is the sum of a retained earlier lag and the *newly received oracle-versus-E1 innovation*. No causality is violated; the input is W(t-1), never W(t). The scalar D(t) may have either sign and therefore is **not** an information entropy, a GR curvature invariant, or a KL divergence.

## 4. Critical double-root collision exactly at the Oily endpoint

`u+v=x`, `uv=x³(2-x)/4`, and the observer characteristic discriminant is

`(u+v)²-4uv=(u-v)²=x²(1-x)²`.

As x→1, `u=v=1/2`: the observer modes coalesce in a repeated eigenvalue, not just a visually similar curve. The transfer equation becomes

**(WEO-04)** `E2(t)-E2(t-1)+(1/4)E2(t-2)=(1/4)W(t-2)`.

The grade PGF at x=1 is `G_1(z)=(2-z)^-2`, and the exact limit distribution is

`w_j=(j+1)/2^(j+2)`.

Its second-order grade difference is

`w_(j+2)-w_(j+1)+(1/4)w_j=0`;

or, after rescaling `a_j=2^(j+2)w_j`,

**(WEO-05)** `a_(j+2)-2a_(j+1)+a_j=0`, where `a_j=j+1`.

The apparent linear growth of a_j reflects the Jordan/repeated-root polynomial prefactor; the actual w_j remain summable. The two-stage total physical **minimum** latency is 2 ticks, while its endpoint expected latency is `2+E[J]=4` ticks and variance of the extra latency is 4. A spatial observer remaining exactly one step behind a null front can still have a longer *information-processing* age. Do not conflate positional lag and signal age.

A distinct exact earlier observation is that the normalized anisotropy `(u-v)/(2-x)=x(1-x)/(2-x)` reaches the silver-ratio value `(1+sqrt(2))^-2`; the collision at x=1 and the sharp maximal anisotropy are two aspects of the same two-loop source.

## 5. Where Euler–Mascheroni DOES and DOES NOT follow

The actual continuous positive source additionally satisfies `R(x)=(1-x)L(x)`, `L(1)=1`; conditioned on x^(8n), `Y=8n(1-x)` approaches `Gamma(2,1)`. The **declared comparison source** L(x) gives `Gamma(1,1)`. The familiar classical identities are

`E_Gamma(1)[log Y]=-gamma`, `E_Gamma(2)[log Y]=1-gamma`,

`D_KL(Gamma1||Gamma2)=gamma`, `D_KL(Gamma2||Gamma1)=1-gamma`.

This is a mathematically legitimate source-conditioned logarithmic finite-part bridge, not proof that E1's belief is Gamma1 or E2's belief is Gamma2. In fact the fixed-rate **discrete** geometric/negative-binomial observer stages at x=1 have different relative entropies:

`D_KL(Geom(1/2) || NB(2,1/2)) ≈0.1853132576915`,

`D_KL(NB(2,1/2) || Geom(1/2)) ≈0.1999946403098`,

neither equals gamma. This is a decisive negative control against identifying the two-stage grade convolution with the Gamma endpoint KL without paying for a scaling bridge.

There *is* a classical family connection: for two independent geometric waits with success probability ε→0, the rescaled total `ε(J1+J2)` converges in law to Gamma(2,1), because its Laplace transforms converge to `(1+s)^-2`. However the authenticated Oily endpoint has ε=1/2, **not** ε→0. This latter limit is a deformation/control, not the original BBP source.

## 6. An optimal epistemic tower as a separate, provable construction

Let `X∈L²` be a target oracle variable and `F2⊂F1⊂F0` nested source-observation sigma-algebras. Define

`M1=E[X|F1]`, `M2=E[M1|F2]=E[X|F2]`.

This is the **optimal mean-squared-error predictor** at each available information level. The ordinary conditional-expectation tower and orthogonality yield

**(WEO-06)** `E[(X-M2)²] = E[(X-M1)²] + E[(M1-M2)²]`.

For finite entropy and finite-valued X, the corresponding conditional information difference is

**(WEO-07)** `H(X|F2)-H(X|F1)=I(X;F1|F2)≥0`.

These quantify precisely the additional uncertainty introduced by E2's strictly poorer evidence, *provided* the source information is nested. They are model-independent classical theorems. A positive defect is not universal: if X is already determined by F2, all errors and conditional entropies vanish. If independent innovations with variance σ² enter one per tick and `X=W_t` is the cumulative sum, then one-step and two-step lagged *conditional-mean* MSE values are σ² and 2σ². Neither is Euler's constant. In an arithmetic deterministic source with public seed/law and unlimited computation, the oracle's next value can be mathematically predictable even before its measurement.

The source-conditioned geometric filter E2 above is a **chosen linear processing law**. It is not identical to the sigma-algebra-optimal predictor M2 for arbitrary source distributions. Proving such an identification requires an explicitly specified Bayesian source/probe model.

## 7. Wavefront geometry and physics boundary

Take event coordinates (t,x) and `c=1`. A frontier event `(t,t)` cannot influence a tracker event `(t,t-1)` at the same time. It *can* influence `(t+1,t)` one tick later. Thus a fixed lagging front is a **temporary causal accessibility boundary**, not automatically a global event horizon.

To remain one spatial cell behind a wavefront moving at exactly c for indefinitely many ticks, a tracker must itself move at c (a null idealization). A timelike physical observer `|v|<c` cannot maintain exact constant one-cell separation indefinitely. No Lorentz metric, Einstein equation, quantum uncertainty lower bound, physical photon/black-hole identification, or cosmological infinity follows from the recurrence alone.

The genuine SUCC `S`/`V_p` affine braid and its source-labelled inverse residues continue to live on the arithmetic carrier; a Hopf S4 is a separate **observer/gauge** quotient, not a source-inferred physical spacetime. One may transport clock conventions between Lorentz coordinate frames via existing CV1–CV10 if physical coordinates are declared, but that is not evidence for actual gravitational time dilation in integer arithmetic.

## 8. Claim ledger, controls, and next verdict-changing probe

| ID | Statement | Status | Explicit limitation or falsifier |
|---|---|---|---|
| WEO-01 | Oily-conditioned two-stage observer filter has the exact order-two source-parameter difference | PROVED PAPER / exact rational finite tests | The chosen filters are mathematical realizations, not proven causal-optimal knowledge models |
| WEO-02 | E1−E2 depth difference obeys a forced first-order memory recurrence | PROVED PAPER / exact rational finite tests | Signed D is not necessarily a positive epistemic loss |
| WEO-03 | The forcing in WEO-02 equals the first observer's newly available oracle lag discrepancy | PROVED PAPER / exact rational finite tests | Not the current W(t) frontier signal; one tick is compulsory |
| WEO-04 | Oily endpoint has a double characteristic root 1/2 and NB2 grade response | PROVED PAPER / exact source identity | Does not imply BBP carry mixing; collision is source-conditional |
| WEO-05 | Exponentially renormalized endpoint grade has vanishing second finite difference | PROVED PAPER / exact arithmetic | Growth belongs to rescaled grade, not probability mass |
| WEO-06 | Nested conditional-mean evidence losses split orthogonally | CLASSICAL | Strict positive gap requires nontrivial conditional variance |
| WEO-07 | Nested evidence information gap is conditional mutual information | CLASSICAL | Zero for predictable/sufficient evidence; not automatically gamma |
| WEO-08 | Authentic Oily Γ2 endpoint KL is *the* one-step knowledge deficit | UNVERIFIED | Discrete stage KL differs; source-conditioned observation kernel is missing |
| WEO-09 | The stage recurrence implies π-normality or RH | UNVERIFIED | Genuine expanding zero-seeded BBP selected Weyl sum not bounded |

**Positive control:** original u,v and p_j/R exact rational equalities; impulse grade identifies w_j and exact repeated-root recurrence. **Negative control:** third independent geometric stage alters w_0; changed BBP U0 with same forcing leaves the filters identical, so they cannot certify seed selection; independent fair innovations give MSE 1,2 rather than gamma; constant predictable signal gives zero posterior defect. **Mutation control:** removing the compulsory `L²` delay produces contemporaneous frontier access, violating the wavefront contract. **Source-map control:** no morphism between two-stage filter and original BBP expanding selected phase orbit is claimed.

**Next probe with a potential verdict change:** Specify the **same actual source/probe law** from W to E1 to E2 and prove that the fixed Oily `u,v` are *optimal evidence-update kernels*, not merely a convenient factorization of p_j. Then test whether its conditional information law has the exact Γ2/Gamma1 KL relation, or whether different valid belief kernels with the same grade marginal give different defects. If a source-selected cross-time real Weyl factor can be derived, test it against changed-seed controls. Do not promote an endpoint covariance or a source-only positive packet algebra to signed π-normality cancellation.

## 9. Reproduction and provenance

- `observational_succ/wavefront_oracle_two_stage.py`: pure Fraction exact rational recurrences and grade probabilities.
- `tests/test_wavefront_oracle_two_stage.py`: exact packet/pulse/source/geometry/seed/finite controls; run via `PYTHONPATH=. python -m unittest tests.test_wavefront_oracle_two_stage -v` after checkout.
- `scripts/wavefront_oracle_two_stage_probe.py`: standalone JSON receipt for core identities and mutation controls.
- Existing source module: `observational_succ/rank_two_chiral_towers.py`, `research/2026-10-27/OILY_ZERO_ONE_LOG_GERM_BRIDGE.md`, and original four-pole source instructions in AGENTS.md.

References: NIST DLMF §5.2, 5.4, 5.9 (Gamma, digamma and Euler constant); classical conditional expectation orthogonal projection and tower property, as presented e.g. in Tropp *Probability Theory* CMS 117 (Caltech, 2024), §19.3.4, `https://tropp.caltech.edu/notes/Tro24-Probability-Theory-LN.pdf`. Any claimed independent novelty is UNVERIFIED. No hosted CI or Lean kernel runs have been claimed.
