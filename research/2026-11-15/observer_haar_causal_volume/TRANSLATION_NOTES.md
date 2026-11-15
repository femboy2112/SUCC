# Adaptive observations, Haar detail, Gamma memory, and quantum boundaries

**Date:** 2026-11-15. **Read baseline:** `2c73e6388b24c7a66683d089733105d14acda08a`, draft #639. **Branch:** `research/observer-haar-causal-volume-2026-11-15`.

**Scope:** translator/provenance reconstruction and direct derivations. Existing source files were read, not changed. The derivations and accompanying [translation_audit.py](translation_audit.py) were completed before reading the new production implementation; the later read-only implementation review is separately recorded below. No other current-round agent notes were used. The standalone audit imports no SUCC modules, and its numerical quadratures are explicitly diagnostic. This is methodological separation, not a claim of independent empirical sources or scholarly novelty.

**Result:** the strongest source-faithful bridge is already available inside the authentic Oily carrier. Its inherited positive Gamma-depth covariance has an exact weighted Haar expansion with strictly positive oriented coefficients and a uniform finite-resolution remainder. Separately, a reversible finite Markov source makes the general inherited compression defect a positive Gram operator, with an exact zero-defect criterion. Both are classical probability/operator constructions. Entanglement requires additional declared quantum state and measurement structure; ER=EPR requires a further gravitational model.

## 1. Historical objects that must receive credit

| Inherited source | Exact useful content | Boundary retained here |
| --- | --- | --- |
| [zero_anchored_haar.py](../../../observational_succ/zero_anchored_haar.py), `certified_phase_grid`, `certified_haar_defect`, `signed_block_overlap` | Authenticated four-pole source enclosures; finite interval-Wasserstein transfer defect with error at most `2/q`; exact signed overlap of chronological blocks | The source orbit is deterministic. This transfer defect is not automatically an orthogonal `L2` projection energy, a sampling law, or an asymptotic contraction theorem. |
| [OMEGA_HAAR_WAVELET.md](../../2026-11-10/omega_bbp_operational_completion/OMEGA_HAAR_WAVELET.md), sections 2–5 | Inserted chronological pair/triple projections have a rank-two skew commutator; a 16-channel inverse-fiber character packet has exact Parseval reconstruction; parity is an antiperiodic section | The pair/triple partitions overlap and are not a nested dyadic filtration. Their noncommutation is observer-induced; exact source clock foldings commute. No quantum or gravitational interpretation follows. |
| [aphex_haar_feedback.py](../../../observational_succ/aphex_haar_feedback.py), `fit_sign_coupling`, `aphex_step` | Exact finite fit `beta=Cov(a,b)/Var(a)` and descent `eta(1-eta Var(a)/2) grad^2`, valid for `0<eta<2/Var(a)` | Offline least squares on authenticated finite streams, not Bayesian source evidence, an online convergence theorem, or a physical energy law. Constant source variance is rejected. |
| [observer_choice_action/RESEARCH.md](../../2026-11-14/observer_choice_action/RESEARCH.md), OC-1–OC-6, #625 | Choice does not establish source identity; nondisturbing finite probes separate exactly when their lawful reports separate source pairs; current state need not recover history | A selectable abstract point or a stochastic section does not supply an actual source-sensitive interaction. Identity quantum evolution on every state cannot also reveal an unknown state. |
| [choice_trichotomy/THEOREMS.md](../../2026-11-14/choice_trichotomy/THEOREMS.md), #626; [probe_budget/THEOREMS.md](../../2026-11-14/probe_budget/THEOREMS.md), #627 | Point, stochastic, and absent equivariant sections; finite lawful probe costs and adaptive identification; the three-state static-section obstruction | Extra observation need not preserve a static lifting property. Guaranteed identification and expected Bayesian utility are different objectives. |
| [recursive_observer_fixed_point/THEOREMS.md](../../2026-11-14/recursive_observer_fixed_point/THEOREMS.md), RFO-01–04, 07–08, #628 | Joint source kernel `J_a(x,x',o)`; original/current posterior recursion; finite-horizon Bayes decision recursion; predictive-span fixed point; information increases only in conditional expectation | A guessed post-state sensor can erase the source's pre-reset information. A predictable action is not independent evidence. Finite self-consistency does not authenticate a source. |
| [source_auth_field_frontier/THEOREMS.md](../../2026-11-14/source_auth_field_frontier/THEOREMS.md), FSA-01–06, #629 | Executable source commitment/replay; source-conditioned posterior; same-policy likelihood-ratio test martingale; finite-horizon delayed-mutant and full predictive-equivalence controls | Execution identity, statistical model fit, and physical source adequacy are separate. The stated likelihood theorem has a specified action/output filtration; unmodeled timing or commitment information cannot be silently included. |
| [gauge_anchored_source/THEOREMS.md](../../2026-11-14/gauge_anchored_source/THEOREMS.md), #630 | Source-attached covariant reference and Bayesian filtering through genuine gauge quotients | A declared invariant reference does not authenticate the physical source or make every target gauge-invariant. |
| [gamma_volume/THEOREMS.md](../../2026-11-14/gamma_volume/THEOREMS.md), GV-04–07, #635 | Gamma/negative-binomial operator subordination; source-retained fractional Oily semigroup; shared-source covariance; general compressed composition defect; source-depth Hankel rank | GV-06 already gives the algebraic defect. It explicitly does not claim arbitrary operator positivity. Haar localization and the reversible positive specialization below are the added interfaces. |
| [bbp_volume_algebra/THEOREMS.md](../bbp_volume_algebra/THEOREMS.md), #637; [causal_negative_orders/THEOREMS.md](../causal_negative_orders/THEOREMS.md), #639 | Exact source convolution powers, positive finite-difference faces, causal negative-order distributions, and distinctions among convolution depth, chronology, and Mellin order | None supplies a stochastic BBP sensor or a reversible BBP transition generator. A Gamma integral identity does not identify these different clocks. |
| [ARITHMETIC_ER_EPR_FOUNDATIONS.md](../../2026-10-22/ARITHMETIC_ER_EPR_FOUNDATIONS.md), A2–A3 and A8 | The normalized arithmetic TFD exists for real `beta>1`; its dephased separable mixture has the same marginals; explicit negative partial-transpose compression; local-channel no-signalling | Normalization cannot be obtained by zeta continuation at `beta<=1`. Formal arithmetic quantum states do not supply a gravitational dual or a physical preparation. |
| [INTERACTING_ARITHMETIC_TFD.md](../../2026-10-22/INTERACTING_ARITHMETIC_TFD.md), sections 3 and 5 | Successor entangles a particular prime-valuation tensor factorization; CRT successor has different locality; interacting Gibbs state is nonproduct | Nonproduct mixed-state correlation is explicitly weaker than entanglement. Tensor factorization is load-bearing. |

The broader hidden-memory mechanism is also inherited: [HIDDEN_MEMORY_SCHUR_AND_TEMPORAL_OBSERVERS.md](../../2026-10-17/HIDDEN_MEMORY_SCHUR_AND_TEMPORAL_OBSERVERS.md), HM-01–03, derives a classical eliminated-state memory kernel `B exp(-tD) B*`. These are antecedents, not fresh discoveries of hidden memory in this round.

## 2. Finite reversible Gamma compression: exact theorem and hypotheses

**Disclosed; elementary spectral and projection algebra.** Let `X` be a finite set, let `pi(x)>0` be a stationary probability vector, and let `L` act on functions by

\[
(Lf)(x)=\sum_{y\ne x}q(x,y)(f(y)-f(x)),\qquad q(x,y)\ge0.
\]

Assume detailed balance `pi(x)q(x,y)=pi(y)q(y,x)`. In the Hilbert space with inner product `sum pi(x) conjugate(f(x)) g(x)`, this gives `L=L*<=0`. Irreducibility is not required for the identities below. With `W=diag(pi)`, the matrix adjoint is `A*=W^(-1)A^T W` for real matrices; ordinary transposition is generally wrong.

For `alpha>0`, `lambda>0`, let the integration clock be `T_alpha ~ Gamma(alpha, rate lambda)` and define

\[
G_\alpha=\mathbb E[e^{T_\alpha L}]
=\frac{\lambda^\alpha}{\Gamma(\alpha)}
\int_0^\infty t^{\alpha-1}e^{-\lambda t}e^{tL}\,dt
=(I-L/\lambda)^{-\alpha}.
\tag{T1}
\]

Diagonalizing the finite self-adjoint `L` reduces the equality to the positive scalar Gamma integral. The resulting operators are self-adjoint positive contractions, preserve constants and `pi`, and obey `G_alpha G_beta=G_(alpha+beta)`. The limiting identity is `G_0=I`; an ordinary Gamma density at shape zero is not asserted. The subordination construction is classical; the finite version needs no unbounded-operator domain extension.

Let `P=P*=P^2` be a fixed orthogonal projection and `Q=I-P`. The observer's compressed operator acts on `ran(P)` as `P G_alpha P`. Then

\[
\boxed{
D_\alpha:=P G_{2\alpha}P-(P G_\alpha P)^2
=P G_\alpha QG_\alpha P
=(QG_\alpha P)^*(QG_\alpha P)\ge0.
}
\tag{T2}
\]

The proof inserts `I=P+Q` between the two factors of `G_alpha`. Self-adjointness is exactly what identifies the first factor with the adjoint of the second. In particular,

\[
\langle f,D_\alpha f\rangle=\|QG_\alpha Pf\|_\pi^2,
\qquad 0\le D_\alpha\le\tfrac14P.
\tag{T3}
\]

For the upper bound, `0<=G<=I` implies `G^2<=G`. Write `B=PGP` on `ran(P)`; then `D<=B-B^2<=I/4` there. This is a dimensionless squared prediction contrast in the declared norm, not a measured physical energy.

### Exact criterion for zero loss

For any one `alpha>0` and `lambda>0`,

\[
\boxed{D_\alpha=0\iff QG_\alpha P=0
\iff[P,G_\alpha]=0\iff[P,L]=0.}
\tag{T4}
\]

The first equivalence follows from a zero Gram operator. Invariance of `ran(P)` under self-adjoint `G_alpha` also makes its orthogonal complement invariant, giving the second. The scalar function `ell -> (1-ell/lambda)^(-alpha)` is injective on the finite real spectrum of `L`; consequently `L` is a polynomial in `G_alpha` on that spectrum. Commutation with `G_alpha` therefore implies commutation with `L`, and the reverse direction follows directly from functional calculus. Vanishing for one strictly positive depth is equivalent to vanishing at every depth.

For a partition observer,

\[
(Pf)(x)=\frac{\sum_{y\in C(x)}\pi(y)f(y)}{\pi(C(x))}.
\]

In this reversible setting (T4) is equivalent to strong lumpability of the generator: for every pair of blocks `C,D`, `sum_(y in D)L(x,y)` is independent of `x in C`. To see this, apply `L` to each block-indicator function; these span `ran(P)`. Thus a source-respecting quotient needs an invariant observable subspace, not merely a normalized average.

**Degeneracies:** at `alpha=0`, the defect is zero regardless of `[L,P]`, so the last equivalence requires positive depth. The cases `P=0`, `P=I`, `L=0`, or any invariant partition also have zero defect. A constant-only observer commutes with every stationary reversible source. Nonzero leakage for one coarse observable does not imply leakage for every observable in that coarse space.

### Haar resolution of the Gram operator

Let `P=P_0<=P_1<=...<=P_m=I` be nested orthogonal projections in the same fixed `L2(pi)` space. Put `E_j=P_j-P_(j-1)`. They are pairwise orthogonal projections and `sum E_j=Q`; hence

\[
\boxed{D_\alpha=\sum_{j=1}^m
(E_jG_\alpha P)^*(E_jG_\alpha P).}
\tag{T5}
\]

For each coarse input this resolves the composition loss into detail levels. If the finite chain stops at `P_m!=I`, the omitted contribution is the nonnegative Gram term with `I-P_m`; it cannot be dropped. A weighted dyadic partition supplies a Haar realization, but arbitrary nonnested projections do not satisfy this decomposition. Changing the posterior weights changes the inner product and projections: coefficients calculated under different posteriors do not automatically form one orthogonal decomposition.

### Hostile domains

1. **Nonreversible source.** Let `S` be the directed four-cycle shift, `L=S-I`, `lambda=1`, and let `P` average adjacent pairs. With `v=(1,1,-1,-1)^T`, direct rational multiplication gives

   \[
   P(2I-S)^{-2}P-\bigl(P(2I-S)^{-1}P\bigr)^2
   =-\frac{vv^T}{100}.
   \tag{T6}
   \]

   Its eigenvalue on `v` is `-1/25`. Stationarity alone does not give the claimed positivity.
2. **Unequal depths.** `P G_(alpha+beta)P-(PG_alpha P)(PG_beta P)=PG_alpha QG_beta P` remains an algebraic identity. It need not be self-adjoint, even with reversible `L`. Thus it is not generally a positive Gram operator. The scalar Oily covariance below is positive for a different, explicitly verified comonotonicity reason.
3. **Depth is not accumulated energy.** On an irreducible source with a conditional-expectation `P`, `G_alpha` tends as `alpha->infinity` to the constant projection, so `QG_alpha P->0` and `D_alpha->0`. Also `D_alpha->0` as `alpha->0`. A nonzero intermediate defect therefore cannot obey a universal monotone-growth law in depth. Reversibility and the Gamma law alone do not generate attraction, work, or entanglement.

## 3. Authentic Oily covariance has a complete weighted Haar expansion

**Disclosed; source-specific specialization of conditional expectation and Parseval.** Retain the exact source from GV-05–06:

\[
R(x)=\frac{4-2x^3-x^4-x^5}{16-x^8},\quad
\mu(dx)=\frac{16}{\pi}R(x)dx,\quad 0\le x\le1,
\]
\[
u(x)=x-\frac{x^2}{2},\quad v(x)=\frac{x^2}{2},\quad
G_x(z)=\frac{(1-u(x))(1-v(x))}{(1-u(x)z)(1-v(x)z)}.
\tag{O1}
\]

The inherited original-source identity is `int_0^1 R dx=pi/16`; the density is positive throughout `(0,1)`. Fix real `0<=z<1` and `alpha,beta>0`, and put `f_alpha(x)=G_x(z)^alpha`. These functions are positive, continuous and strictly decreasing. GV-06 gives

\[
A_{\alpha+\beta}(z)-A_\alpha(z)A_\beta(z)
=\operatorname{Cov}_\mu(f_\alpha,f_\beta)>0.
\tag{O2}
\]

This is the same source coordinate retained through both depth factors. Replacing the left side by the product of averages redraws that coordinate.

### O3 — finite-resolution identity, including the omitted remainder

Let `F_J` be the dyadic partition into intervals of length `2^(-J)` and `P_J=E_mu[ . |F_J]`; let `P_0` project to constants. For `Delta_j=P_j-P_(j-1)`, orthogonal decomposition gives

\[
\begin{aligned}
\operatorname{Cov}_\mu(f_\alpha,f_\beta)
&=\sum_{j=1}^J\langle\Delta_jf_\alpha,\Delta_jf_\beta\rangle_\mu
 +\mathcal R_J(\alpha,\beta;z),\\
\mathcal R_J
&=\langle f_\alpha-P_Jf_\alpha,
 f_\beta-P_Jf_\beta\rangle_\mu.
\end{aligned}
\tag{O3}
\]

For equal depths this is an exact sum of squared Haar norms plus a squared residual. All cross terms disappear because of the nested conditional expectations; no independence between dyadic levels is assumed.

For a dyadic parent interval `I` with children `I_L,I_R`, write `m_L=mu(I_L)`, `m_R=mu(I_R)`, `m_I=m_L+m_R`. All three masses are positive. Define the oriented weighted Haar atom

\[
h_I=\sqrt{\frac{m_R}{m_Lm_I}}\,1_{I_L}
-\sqrt{\frac{m_L}{m_Rm_I}}\,1_{I_R}.
\tag{O4}
\]

Its mean is zero and its norm is one. Its coefficient is

\[
c_I(\alpha;z)
=\sqrt{\frac{m_Lm_R}{m_I}}
\bigl(\mathbb E[f_\alpha\mid I_L]
-\mathbb E[f_\alpha\mid I_R]\bigr)>0.
\tag{O5}
\]

The strict inequality follows because each point in the interior of the left child lies below each point in the interior of the right child, `f_alpha` is strictly decreasing, and both conditional measures have positive density. Every nontrivial dyadic parent therefore contributes positively with this fixed left-positive orientation. Flipping a Haar atom changes both coefficients' signs, leaving their product unchanged.

Consequently the finite sum in (O3) is `sum_(I, level(I)<J)c_I(alpha;z)c_I(beta;z)`. The remainder is also nonnegative: on each terminal cell it is the cell mass times the conditional covariance of two decreasing functions. The identity

\[
2\operatorname{Cov}(f(X),g(X))
=\mathbb E[(f(X)-f(Y))(g(X)-g(Y))]
\]

with independent conditional copies proves this without a numerical sign test.

### O6 — all resolutions, with a uniform certified remainder

Since `u',v'>=0`, `u'+v'=1`, and `0<=u,v<=1/2`, direct differentiation gives

\[
-\partial_x\log G_x(z)
=(1-z)\left[
\frac{u'}{(1-u)(1-uz)}
+\frac{v'}{(1-v)(1-vz)}\right]
\le\frac{4(1-z)}{2-z}.
\]

Also `0<f_alpha<=1`. Therefore a valid uniform Lipschitz constant is

\[
L_{\alpha,z}=\frac{4\alpha(1-z)}{2-z}.
\tag{O6}
\]

On a cell of diameter `2^(-J)`, the range of `f_alpha` is at most `L_(alpha,z)2^(-J)`. A bounded real variable with range width `d` has variance at most `d^2/4`: center at the range midpoint, then use the minimum-square-error property of its actual mean. Conditional Cauchy–Schwarz now proves

\[
\boxed{0\le\mathcal R_J(\alpha,\beta;z)
\le\frac{L_{\alpha,z}L_{\beta,z}}4\,4^{-J}.}
\tag{O7}
\]

Hence

\[
\boxed{
A_{\alpha+\beta}(z)-A_\alpha(z)A_\beta(z)
=\sum_{\text{all dyadic }I}c_I(\alpha;z)c_I(\beta;z).
}
\tag{O8}
\]

The finite partial sums increase to the source covariance. At equal depth this is Parseval energy; at unequal depths it is a positive cross-detail sum. The result is a theorem for all stated real depths and all dyadic resolutions, with a proved tail bound. Finite quadratures do not establish its quantifiers.

At `z=1` or depth zero, the appropriate function is constant and its details vanish. If the source coordinate is already fixed, the source law is a point mass and the covariance vanishes; formulas dividing by empty child masses must then be replaced by conditional expectations on the nonempty atoms. Positivity at every level concerns the original diffuse source and the stated nondegenerate parameter range.

There is a direct operator interpretation without inventing a BBP Markov generator. On `L2(mu)`, multiplication by `G_x(z)^alpha` forms a self-adjoint contraction semigroup in depth. Compressing it to constant functions gives (O2); at equal depth its Gram defect is exactly the variance in (O3). This multiplication family generally does **not** preserve constants, so it is not the conservative Markov semigroup of section 2. Its source coordinate, measure, and conditional Oily generating law are inherited and fixed.

### O9 — native unit depth has rational source integrals and a sharper bound

At `alpha=beta=1,z=0`,

\[
a(x)=G_x(0)=1-x+\frac{x^3}{2}-\frac{x^4}{4},
\quad a(x)R(x)=\frac{1-x}{4},
\quad \int aR=\frac18,\quad\int a^2R=\frac7{80}.
\]

The derivative satisfies

\[
a'(x)+1=x^2(3/2-x)\ge0,\qquad
a'(x)+1/2=-(1-x)^2(x+1/2)\le0.
\]

Thus `Lip(a)<=1`, improving (O7) to

\[
\boxed{\frac{7\pi-20}{5\pi^2}
=\sum_{\operatorname{level}(I)<J}c_I(1;0)^2+\mathcal R_J,
\qquad 0\le\mathcal R_J\le\frac{4^{-J}}4.}
\tag{O9}
\]

No external pi-digit oracle is necessary to enclose these source integrals. Put `P_source(x)=4-2x^3-x^4-x^5=(1-x)(x^2+2)(x^2+2x+2)`, and take the first `N` geometric terms, indexed `0,...,N-1`:

\[
R_N(x)=\sum_{n=0}^{N-1}\frac{P_{\rm source}(x)x^{8n}}{16^{n+1}},
\quad
0\le R(x)-R_N(x)
=\frac{P_{\rm source}(x)x^{8N}}{16^N(16-x^8)}
\le\frac4{15}\,16^{-N}.
\tag{O10}
\]

Every rational interval `[l,r]` therefore has a rational integral enclosure whose width is at most `(4/15)16^(-N)(r-l)`. The lower integral uses the exact polynomial `R_N`. Nonempty intervals have positive true mass; division requires a strictly positive certified lower bound.

Write unnormalized cell quantities `r_I=int_I R`, `A_I=int_I aR`, `B_I=int_I a^2R`, and `Z=int_0^1R`. Both `A_I` and `B_I` are rational polynomial integrals for rational endpoints. The coefficient energy is

\[
c_I(1;0)^2
=\frac{(A_Lr_R-A_Rr_L)^2}{Zr_Ir_Lr_R}.
\tag{O11}
\]

On the terminal cells at depth `J`, exact telescoping gives

\[
\sum_{\operatorname{level}(I)<J}c_I^2
=\frac1Z\sum_{I\in F_J}\frac{A_I^2}{r_I}
-\left(\frac{A_{[0,1]}}Z\right)^2,
\quad
\mathcal R_J=\frac1Z\left(B_{[0,1]}-
\sum_{I\in F_J}\frac{A_I^2}{r_I}\right).
\tag{O12}
\]

These are the source-faithful formulas a rational interval instrument should enclose. Roundoff comparisons are unnecessary to prove (O9); the interval evaluator must still handle correlated interval occurrences conservatively rather than treating repeated masses as independent exact numbers.

**Operational boundary.** This is a declared dyadic revelation of the authentic source variable under its authenticated mathematical measure. It does not establish that a physical observer can measure that variable, that successive physical reports are independent, or that the selected deterministic BBP chronology samples `mu`. An actual sensor requires its own joint readout/backaction law. Weighted Haar here means a basis for nested conditional expectations; it is not a claim that the nonuniform density is group-invariant Haar measure.

## 4. Adaptive evidence and probe attraction: required conditions

The primitive already present in RFO-01 is a joint instrument `J_a(x,x',o)`, with lawful action menu and a declared source prior. Probability weights cannot be inferred solely from the set of possible automaton outputs. An observation that changes the source uses that same joint law; Bayes conditioning alone is a change in the observer's state of information.

Let `C` be a fixed binary structural hypothesis and `h` the recorded past. Posterior odds update by

\[
\frac{p(C=1\mid h,a,o)}{p(C=0\mid h,a,o)}
=\frac{p(C=1\mid h)}{p(C=0\mid h)}
\frac{p(o\mid C=1,h,a)}{p(o\mid C=0,h,a)}.
\tag{A1}
\]

Repeated observations strictly raise these odds only when their **conditional** likelihood ratios exceed one. A copy of an already recorded datum has conditional probability one under both surviving hypotheses and adds no evidence. A posterior for a zero-probability observed event is a model conflict. These distinctions are inherited from FSA-03–04.

For a specified unresolved target `Theta`, the expected information value of a probe is

\[
U_h(a)=I(\Theta;O\mid h,a)
=\mathbb E_{O\mid h,a}
D_{\rm KL}(p(\Theta\mid h,a,O)\Vert p(\Theta\mid h)).
\tag{A2}
\]

This is classical Bayesian experimental design. Structural evidence can increase this value when it changes the probe's predicted coupling to an unresolved target. Evidence that resolves the target itself can decrease it. RFO-08 already proves expected entropy reduction and gives an individual outcome that increases posterior entropy; monotonicity on every realized history is false.

A declared stochastic policy can optimize `sum rho(a)U_h(a)-tau KL(rho||rho_0)`, with `tau>0` and a fixed prior policy on the legal menu. Its unique optimizer on that support is

\[
\rho_h(a)=\frac{\rho_0(a)e^{U_h(a)/\tau}}
{\sum_b\rho_0(b)e^{U_h(b)/\tau}},\quad
\log\frac{\rho_h(a)}{\rho_h(b)}
=\log\frac{\rho_0(a)}{\rho_0(b)}+
\frac{U_h(a)-U_h(b)}\tau.
\tag{A3}
\]

Substituting this optimizer into the objective leaves a constant minus `tau KL(rho||rho_h)`, which proves the formula. Thus relative utility, not the absolute utility of one probe alone, determines odds. A base-policy zero remains zero; reweighting does not create a new legal action. This specified utility potential is a mathematical meaning for attraction; it is not a force or an energy calibration.

For random adaptive actions, likelihood cancellation remains valid when the **same** policy kernel is used under both source hypotheses and its randomization is conditionally independent of the hidden source given the recorded past. Include observed actions in the transcript; their common factors cancel. If the policy has a hidden source-dependent input, the action carries extra information and its likelihood cannot be dropped. Predictable design selection and hindsight fitting of an alternative after seeing its outcome are different operations.

The stationary `pi` in section 2, source measure `mu` in section 3, and Bayesian posterior after data in this section have distinct roles. They must be related by an explicit source model before formulas are transported between them. No universal equation identifies an information-gain scalar with a Haar energy or a physical energy.

## 5. Quantum tests and the ER=EPR boundary

For a declared bipartite density matrix `rho_AB` and a local instrument with Kraus operators `K_(a,r)` satisfying `sum_(a,r)K_(a,r)^* K_(a,r)=I`, define

\[
\sigma_{B,a}=\operatorname{Tr}_A\sum_r
(K_{a,r}\otimes I)\rho_{AB}(K_{a,r}^*\otimes I),\quad
p_a=\operatorname{Tr}\sigma_{B,a}.
\]

At `p_a>0`, the conditional report is `rho_(B|a)=sigma_(B,a)/p_a`; with the outcome ignored, `sum_a sigma_(B,a)=rho_B`. This exact local-channel no-signalling law is already A8 of the arithmetic TFD dossier. A conditional remote state can change while the unconditional marginal does not. An outcome flag is required to identify which conditional ensemble was prepared.

The Bell state `(|00>+|11>)/sqrt(2)` and its fully dephased mixture have the same one-party marginals and the same joint computational-basis records. They differ in complementary-basis coherence. For trusted two-qubit Pauli observables, every separable state obeys

\[
|\langle X\otimes X\rangle|+|\langle Z\otimes Z\rangle|\le1.
\tag{Q1}
\]

For a product state this follows from Cauchy–Schwarz on the two relevant components of its Bloch vectors; convexity extends it to separable mixtures. The coherent Bell state has value two, while the dephased control has value one. A single large `XX` correlation alone would not be a witness: the product state `|++>` also has `XX=1`. The witness requires the joint specified measurements and the quantum measurement model. Device-independent conclusions need different, explicitly satisfied Bell-test assumptions.

Steering is stronger than the fact that a conditional state changes. With settings `x`, an assemblage is unsteerable if one common collection of local quantum states can represent every setting:

\[
\sigma_{a|x}=\sum_\lambda q_\lambda
p(a|x,\lambda)\tau_\lambda.
\tag{Q2}
\]

For one setting alone such a representation always exists by taking the outcome itself as the hidden label. Multiple settings and a witness excluding a common representation are necessary to demonstrate steering. Entanglement, steering, and Bell nonlocality are distinct operational criteria. The classical Gram identities (T2), (O3), and Bayesian odds updates cannot by themselves certify any of them.

Maldacena–Susskind's original ER=EPR paper distinguishes a special entangled black-hole state with a weakly coupled Einstein-gravity description from its broader conjectural extension. It does not prove that an arbitrary correlation, Hilbert-space factorization, or positive Gram matrix carries a spacetime wormhole. A declared arithmetic TFD is mathematically useful, but the inherited dossier explicitly leaves the gravitational map open.

Traversability needs a further qualification: Gao–Jafferis–Wall render the bridge traversable by coupling the two boundaries and generating negative averaged null energy in their model. Their decoupled boundary systems cannot transmit signals to one another. Thus local no-signalling and interaction-enabled traversability have different hypotheses; neither permits source-free or superluminal communication.

## 6. Primary and author-supplied references inspected live

Only the formulas and scopes described here are imported. Direct proofs above carry the new source specialization; these references establish its classical antecedents.

| Source | Verified location and applicable statement |
| --- | --- |
| Adam Foster, Desi R. Ivanova, Ilyas Malik, Tom Rainforth, [Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design](https://proceedings.mlr.press/v139/foster21a/foster21a.pdf), ICML/PMLR 139 (2021), 3384–3395 | Equation (1), section 2, and section 2.1 give the expected log-likelihood ratio / mutual-information design objective and adapt each design using the preceding design/outcome history. This is a primary research paper; no claim that this round invents adaptive Bayesian design. |
| Rick Durrett, [Probability: Theory and Examples, fifth-edition author manuscript](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf), version 11 January 2019 | Theorems 4.1.13 and 4.1.15, printed pp. 212–213, establish nested conditional expectation and its orthogonal `L2` projection characterization; Theorems 4.4.6–4.4.8 give convergence, orthogonal increments and conditional variance. This is an author-supplied mathematical exposition, not a priority claim for Haar or martingale theory. |
| Ivan Gentil and Patrick Maheux, [Super-Poincare and Nash-type inequalities for subordinated semigroups](https://arxiv.org/pdf/1105.3095), arXiv:1105.3095v2 | Section 1, equations (4) and (6), gives the subordinator Laplace law and integrated semigroup; example ii on PDF p. 3 identifies the Gamma exponent `g(x)=log(1+x)` and generator `log(I+A)`. Taking `A=-L/lambda` gives (T1). The spectral assumptions are symmetric contraction semigroup and nonnegative self-adjoint `A`. |
| H. M. Wiseman, S. J. Jones, A. C. Doherty, [Steering, Entanglement, Nonlocality, and the EPR Paradox](https://arxiv.org/pdf/quant-ph/0612147), Phys. Rev. Lett. 98, 140402 (2007) | PDF pp. 1–2 define steering by exclusion of local hidden quantum states and distinguish it from separability and Bell nonlocality. The paper proves strict separation using mixed-state families. Conditional ensemble updates alone are not the operational witness. |
| Juan Maldacena and Leonard Susskind, [Cool horizons for entangled black holes](https://arxiv.org/pdf/1306.0533), arXiv:1306.0533v2, Fortschr. Phys. 61 (2013), 781–811 | Introduction, printed p. 2, states the special weakly coupled gravitational description and labels broader bridges speculative; section 2.7, printed p. 13, discusses nontraversability, and section 3.1, printed p. 16, states the no-superluminal-signal boundary. The general ER=EPR proposal is a conjectural bridge, not an identification theorem for this arithmetic source. |
| Ping Gao, Daniel Louis Jafferis, Aron C. Wall, [Traversable Wormholes via a Double Trace Deformation](https://arxiv.org/pdf/1608.05687), JHEP 12 (2017), 151 | Abstract and introduction, PDF pp. 1 and 4, specify an interaction between the two boundaries, negative averaged null energy, and the no-signal property of the decoupled Hamiltonian. These conditions qualify the original nontraversability discussion. |

## 7. Bounded audit receipt and remaining source obligation

Run:

```text
python research/2026-11-15/observer_haar_causal_volume/translation_audit.py
```

**Observed:** exit 0 in 0.89 seconds; Python 3.12.14, SymPy 1.14.0, mpmath 1.3.0. Script SHA-256: `fd9cc7cc3c8270cb813df49b596c827210274caedd345e9f02e04009d5744d85`.

The script passed **111 exact checks** over 18 reversible rational matrix cases, with stationary weights `(1/4,1/4,1/4,1/4)` and `(1,2,3,4)/10`, rates `1,2,3/2`, and integer depths `1,2,3`. It checks the weighted adjoint, nested Gram identity, positivity through all principal minors, the `1/4` cap, constant-observer nulls, depth-zero nulls, the wrong-Euclidean-adjoint mutation, the directed-cycle negative defect, a non-self-adjoint unequal-depth defect, and original-source polynomial/moment identities. These are finite controls; the preceding proofs establish the quantified statements.

The **separate diagnostic** directly integrates the original rational `R`, without importing production or using a source approximation, at 50 decimal digits. It reports total variance `0.040349106087955854377356684604129658079051909384292`; its difference from the closed formula is about `5.01e-52`. The partial Haar sums and residuals are:

| Depth `J` | Partial Haar energy | Residual | Proved bound `4^(-J)/4` |
| --- | ---: | ---: | ---: |
| 0 | 0 | 0.0403491060879559 | 0.25 |
| 1 | 0.0274765586637190 | 0.0128725474242368 | 0.0625 |
| 2 | 0.0369556831522618 | 0.00339342293569402 | 0.015625 |
| 3 | 0.0394870997040519 | 0.000862006383903962 | 0.00390625 |
| 4 | 0.0401325241297992 | 0.000216581958156665 | 0.0009765625 |
| 5 | 0.0402948771197655 | 0.0000542289681903147 | 0.000244140625 |

The displayed decimals are not certified intervals. The script prints the raw values, versions, exact-case counts, source parameters, and its digest for replay. No full repository suite, hosted CI, physical observation, or finite-to-universal statistical conclusion is claimed here.

### Subsequent read-only implementation review

The later review inspected [haar_gamma_bridge.py](../../../observational_succ/haar_gamma_bridge.py), SHA-256 `c92982fc181d86a783f995152485b8554fbe104ac33ad920ca79ecb42d67d244`, and [test_haar_gamma_bridge.py](../../../tests/test_haar_gamma_bridge.py), SHA-256 `489a9a6a60382978b890ea40a9141913c78375a11ee38505f603baa7d6074898`. **No formula or interval-enclosure defect was found in these revisions.** The following is a separate implementation probe, not part of the no-production-import standalone audit.

- **48 exact moment comparisons:** for powers `1,...,16` and cells `[0,1]`, `[2/11,4/7]`, `[127/128,1]`, an independent SymPy expansion and antiderivative of `(1-x)a(x)^(power-1)/4` agreed exactly with the production moment routine.
- **9 diagnostic mass enclosures:** direct original-`R` quadrature on those three cells lay inside the production rational intervals for `terms=1,3,11`, at 60-digit working precision.
- **36 diagnostic energy/residual enclosures:** direct original-`R` quadrature of cell masses and moments agreed with the production enclosures for `power=1,4,8`, `level=0,2,5`, `terms=1,3`. Each comparison tested both the exact coefficient-energy formula (O11) and the conditional-variance formula (O12). These floating comparisons do not certify endpoints; the interval proof does.
- **Two extreme-domain controls:** `level=7,power=8,terms=1` returned ordered nonnegative intervals for both level energy and residual variance.

The reviewed interval logic uses positivity of `A_I`, `r_I`, and the signed numerator in (O11). Clipping a negative lower numerator bound to zero is valid; its upper bound remains positive. In the residual, `B_I-A_I^2/r_I` increases with `r_I`, so the selected mass endpoints have the correct direction. Dividing nonnegative totals by the enclosing `Z` endpoints is conservative, and intersecting the residual upper bound with `power^2 4^(-J)/4` is justified by `|(a^power)'|<=power`. Repeated occurrences of an uncertain mass can widen these enclosures, but do not invalidate them.

The matrix implementation deliberately restricts to uniform stationary weights and symmetric generators; ordinary transpose is therefore the correct adjoint within that API. Its explicit operator trace is unchanged by choosing normalized counting measure, while a raw vector quadratic form must use the declared inner-product normalization. General weighted reversibility remains a theorem in section 2, not a claimed production capability.

One mathematical wording issue was reported at the reviewed module's line 108: nonreversible sources still obey the same finite Gamma-resolvent subordination law; it is the positive Gram certificate that requires reversibility. The root corrected the docstring, and that correction was read back at module SHA-256 `c7759061e0ae01d5abb84e64ae3eda54a04f7e82c9b82158960b3fe1fc3c519b`. No formula changed, so the earlier computational receipt remains attached to its original hash.

The exact executed comparison command is retained here separately from the standalone audit:

```sh
python - <<'PY'
from fractions import Fraction as F
import hashlib
from pathlib import Path
import sympy as s
import mpmath as m
from observational_succ import haar_gamma_bridge as h
x=s.symbols('x')
a=(1-x+x*x/2)*(1-x*x/2)
cells=((F(0),F(1)),(F(2,11),F(4,7)),(F(127,128),F(1)))
exact=0
for power in range(1,17):
    primitive=s.integrate(s.expand((1-x)*a**(power-1)/4),x)
    for left,right in cells:
        expected=primitive.subs(x,s.Rational(right.numerator,right.denominator))-primitive.subs(x,s.Rational(left.numerator,left.denominator))
        actual=h.source_power_moment(left,right,power)
        assert s.Rational(actual.numerator,actual.denominator)==expected
        exact+=1
m.mp.dps=60
def mpq(v): return m.mpf(v.numerator)/v.denominator
def r(t): return (4-2*t**3-t**4-t**5)/(16-t**8)
def av(t): return (1-t+t*t/2)*(1-t*t/2)
def inside(v,i): return mpq(i.lower)<=v<=mpq(i.upper)
z=m.quad(r,[0,1])
mass_checks=0
for left,right in cells:
    direct=m.quad(r,[mpq(left),mpq(right)])
    for terms in (1,3,11):
        assert inside(direct,h.source_mass_interval(left,right,terms=terms))
        mass_checks+=1
interval_checks=0
for power in (1,4,8):
    for level in (0,2,5):
        detail=m.mpf('0'); residual=m.mpf('0')
        for j in range(2**level):
            left=m.mpf(j)/2**level; right=m.mpf(j+1)/2**level; middle=(left+right)/2
            ml=m.quad(r,[left,middle]); mr=m.quad(r,[middle,right])
            al=m.quad(lambda t:av(t)**power*r(t),[left,middle]); ar=m.quad(lambda t:av(t)**power*r(t),[middle,right])
            detail+=(al*mr-ar*ml)**2/(z*(ml+mr)*ml*mr)
            second=m.quad(lambda t:av(t)**(2*power)*r(t),[left,right])
            residual+=(second-(al+ar)**2/(ml+mr))/z
        for terms in (1,3):
            assert inside(detail,h.source_haar_level_energy(level,power=power,terms=terms))
            assert inside(residual,h.source_residual_variance(level,power=power,terms=terms))
            interval_checks+=2
for call in (lambda:h.source_haar_level_energy(7,power=8,terms=1),lambda:h.source_residual_variance(7,power=8,terms=1)):
    interval=call(); assert 0<=interval.lower<=interval.upper
print({'exact_source_moment_checks':exact,'diagnostic_direct_mass_enclosures':mass_checks,'diagnostic_energy_residual_enclosures':interval_checks,'highest_level_low_precision_domain_controls':2,'precision':m.mp.dps,'production_sha256':hashlib.sha256(Path('observational_succ/haar_gamma_bridge.py').read_bytes()).hexdigest(),'tests_sha256':hashlib.sha256(Path('tests/test_haar_gamma_bridge.py').read_bytes()).hexdigest()})
PY
```

Its raw final output was:

```text
{'exact_source_moment_checks': 48, 'diagnostic_direct_mass_enclosures': 9, 'diagnostic_energy_residual_enclosures': 36, 'highest_level_low_precision_domain_controls': 2, 'precision': 60, 'production_sha256': 'c92982fc181d86a783f995152485b8554fbe104ac33ad920ca79ecb42d67d244', 'tests_sha256': '489a9a6a60382978b890ea40a9141913c78375a11ee38505f603baa7d6074898'}
```

**Novelty boundary:** inherited general compression algebra, classical subordination, conditional expectation, Bayesian design, no-signalling, and the arithmetic TFD controls receive explicit credit. The added source interface is the authentic Oily covariance's oriented Haar decomposition with a uniform remainder and polynomial-integral implementation route, together with the reversible finite zero-defect criterion and its hostile domains. Academic priority beyond these identified antecedents is unverified.

**Final bounded theorem review: PASS for AH-05, AH-06, and AH-10 at [THEOREMS.md](THEOREMS.md) SHA-256 `ab8b42d1d0429db3bd1bac1fe170061f9d6103c09717df20ab09909a62d3dfee`.** The review checked the attraction potential's factor `1/2`, weighted-adjoint Gram normalization, the positive-depth commutation criterion, the directed-cycle negative control, all-resolution Oily covariance and strict residual domains, the `1/4` remainder factor, and the rational source-mass/moment formulas. AH-02's Haar normalization was read as the supporting definition. The final AH-06 explicitly fixes `alpha,beta>0`; zero depth and `z=1` are separately degenerate. The final AH-10 explicitly starts from a density matrix and requires each action's CP outcome maps to sum to a trace-preserving map. Its history coarsening retains the performed interventions and adaptive feedback. The source-coordinate versus completed-phase-coordinate distinction and the unverified gravitational correspondence are stated correctly. No shared theorem or implementation file was edited by this review, and no physical verification is claimed.

**Refreshed final review: PASS at theorem SHA-256 `eb7c26b99eac112364db19a746e45e979cfc0abf98f34a29e34487586f0b9125`.** The assigned AH-05, AH-06, and AH-10 results retain their reviewed validity. The additional edits were inspected: Ville's threshold parameter is explicitly in `(0,1)`; the finite-action policy assumes finite real utilities and a normalized reference; its infinite-inverse-temperature limit correctly selects supported maximizers with reference-proportional tie weights, without claiming monotone concentration for a nonuniform reference; and the no-signalling sum omits zero-probability branches whose normalized conditional states are undefined. These clarify domains without altering the source/Haar identities. No additional experiments were needed or run for this refresh.

**Remaining lamp:** specify a real source/readout/backaction channel that makes a deeper arithmetic detail observable, then compare its fresh conditional predictions against dependent-copy, source-redraw, nonreversible, and dephased controls. A physical entanglement claim additionally needs an authenticated quantum preparation and incompatible measurement witnesses; a gravitational claim additionally needs a gravitational model and matching observables. The current theorems make those obligations concrete without declaring them satisfied.
