# OPERATION ZENO — Source-indexed finite-to-global proof calculus

**Date:** 2026-10-14. **Working branch:** `research/zeno-finite-global-proof-calculus-2026-10-14`, a draft child of WILD ADELIC SUCC PR #88 head `721778bf7df28ab52a57346c8d8f4f31bf2b2c13`; this descends from completed signed Weil PR #71 and Arithmetic Meta-Weil PR #86. **Main unchanged. RH PROVED: NO.** No physical supertask, empirical sensor, zero-reading arithmetic oracle, global RH sign, or academic priority is claimed. Code is a pure standard-library **finite exact model**; universal mathematical assertions below are independently proved on paper, not established by its finite test counts.

## 0. Author's hypothesis, strongest version, and essential correction

The user's idea: reconstruct Zeno fully in SUCC because many hard finite-to-global proofs have the same causal form—successor steps accumulate information locally, yet global truth depends on a limit law that is not any individual observation. **Steelman:** build a *typed completion certificate* which states (1) authentic source/generative law, (2) the finite successor recursion, (3) a quantified remainder and its topology/domain, (4) an inference rule preserving the target under completion, and (5) whether the limit belongs to the original source or only its mathematical completion. Track resource cost and physical realization separately.

**Correction:** finite-to-global mathematics is broader than convergent sequences. Direct induction, polynomial identities, compactness, transfinite recursion, and algebraic universal properties need not be Zeno-series arguments. However, a large class of analytic and operator problems **does** have exactly the above proof shape. A completed limit does not mechanically become a performed event, a valid original-source state, or a proved signed invariant.

Historical Zeno's four motion arguments are Dichotomy, Achilles, Arrow, and Stadium; the alternating lamp is Thomson's modern *supertask* control, not historically Zeno's own fifth paradox. Background: Stanford Encyclopedia of Philosophy, *Zeno's Paradoxes*, §§3.1–3.4; *Supertasks*, and SUCC's prior `research/2026-10-11/PROOF_BACKACTION_DEBT_ZENO.md`, SWM F45 proof-cost theory, SWM B09 (Lean-checked inverse-family/actualization), VOYAGER, and PR #77's Global Model Sandwich. Novelty of their classical results is NOT claimed.

## 1. The complete SUCC Zeno reconstruction: four different proof failures

### ZS-01. Dichotomy: recursive source law, exact finite proof, no omega event (CLASSICAL, DERIVED)

Take the fixed source of rational half-distances `d_k=2^{-k}`, `k>=1`, with state `x_0=0` and lawful mathematical update `x_(n+1)=(x_n+1)/2`. Induction gives, **for every** `n>=0`,

\[
 x_n=1-2^{-n},\qquad 0< 1-x_n=2^{-n},\qquad x_\infty=1.
\]

Given target absolute precision `2^{-k}`, stage `n=k` is a *finite certified observer horizon*; no infinite number of steps was executed to obtain this symbolic proof. The declaration that an actual physical runner traversed all points in finite time is additional physics/semantics, not an output of a formula. `FormalLimit` intentionally has no constructor permitting an executed `omega` event.

### ZS-02. Achilles and the tortoise (CLASSICAL, DERIVED)

Let starting gap `d>0` and constant `v_A>v_T>=0`. Put `r=v_T/v_A<1`. The completion of the `n`-th catch-the-previous-position event occurs at

\[
 t_n=\frac{d}{v_A-v_T}(1-r^n),\quad
 \operatorname{gap}_n=d r^n,
 \quad t_*=\frac{d}{v_A-v_T}.
\]

Proof: initial `t_0=0`; the next segment takes `gap_n/v_A`; the gap after this increases by `v_T (gap_n/v_A)`, hence shrinks by ratio `r`. Induction and geometric summation prove the exact identities. At the limit the two **stipulated continuous trajectories** meet. Real-world velocity law, continuity and model-to-carrier realization are explicit premises. No finite chase is forced to meet the moving tortoise when `v_T>0`.

### ZS-03. The Arrow: positions-at-one-instant do not determine velocity (CLASSICAL COUNTERMODEL)

The paths `x(t)=0` and `y(t)=t` have identical observation `x(0)=y(0)=0` and zero displacement at that zero-duration instant, but derivatives `x'(0)=0` and `y'(0)=1`. Motion is **temporal-jet data**. If an independently justified source law gives `|x''(t)|<=M` over `[0,h]`, Taylor's theorem yields the true finite-observer bridge

\[
 \left|\frac{x(h)-x(0)}h-x'(0)\right|\le Mh/2.
\]

Without the source-bounded acceleration law, a snapshot cannot authenticate derivative/velocity. This is a legitimate representation-language extension, not merely “more samples”.

### ZS-04. The Stadium: a model-to-model frame-square defect (CLASSICAL COUNTERMODEL)

With stationary `A` and velocities `v_B=v`, `v_C=-v` in that A-frame, in elapsed time `h`, `B` travels `vh` relative to A and `2vh` relative to C. Relative speed B-versus-C is `2v`; each gives the SAME `h` after division. Comparing displacement in the BC frame with velocity in the BA frame silently mixes source-indexed charts and produces the false half-time paradox. The correct diagram tracks transformations of both position and velocity. These are Galilean source-contract equalities, not Lorentz claims.

### ZS-05. The modern Thomson lamp: elapsed-time convergence is not state convergence (REFUTES WRONG ZENO RULE)

At `t_n=1-2^{-n}`, set the lamp value `b_n=n mod 2` in discrete `{0,1}`. The clock has a finite endpoint `lim t_n=1`, but the lamp sequence is not eventually constant and thus has **no limit in the discrete state space**. A numerical Cesàro average of 1/2 would not be a possible lamp state either. Missing is a state-space completion law, not another decimal place on the time coordinate. Conversely, an infinite series of *mathematical lengths* is not necessarily a list of separately executable physical operations.

## 2. The reusable global mathematical theorem

### ZS-06. Certified Zeno convergence in a complete metric space (CLASSICAL / PROVED HERE)

Let `(X,d)` be a complete metric space and `(x_n)_(n>=0)` satisfy, for actual declared constants `A>=0`, `0<=q<1`,

\[
 d(x_{n+1},x_n)\le A q^n \quad\text{for EVERY }n\ge0.
\]

Then a unique `x_infty in X` satisfies `x_n -> x_infty`, and

\[
 \boxed{d(x_n,x_\infty)\le \frac{Aq^n}{1-q}.}\tag{ZS-6}
\]

**Proof:** for `m>n`, triangle inequality gives `d(x_m,x_n)<=sum_(k=n)^(m-1)Aq^k <=Aq^n/(1-q)`. This is Cauchy; completeness yields the unique limit. Let `m->infty` in the last finite bound. The proof is finite and establishes its quantified all-n statement by geometric law, not by testing chosen stages. When data and q are computable rationals, `Aq^n/(1-q)` gives an effective modulus, and for a rational error target one can find n by exact multiplication. A generic convergent sequence without a source-proved modulus does NOT inherit this certificate.

### ZS-07. Completion versus original-source actualization (SHARP NEGATIVE CONTROL)

In the incomplete mathematical carrier `X=Q` with usual distance, bisect the exact rational interval `[1,2]` against the law `x²=2`. The nested closed intervals `[l_n,h_n]` have `l_n²<2<h_n²` and width `h_n-l_n=2^-n`. Every finite stage is rational and internally source-lawful. The complete real carrier determines exactly one endpoint `sqrt(2)`, but **no rational original source realizes it**: if `(a/b)²=2` in lowest terms, both a and b are even. Thus finite compatibility + a completion theorem does NOT guarantee realization in the original source type, matching SUCC VOYAGER/B09 and WILD ADELIC. A mathematical completion is not an empirical or causal supertask.

### ZS-08. Closed-target Zeno transport, including negative witnesses (CLASSICAL / PROVED HERE)

Under ZS-06, let `C subset X` be **closed**. Suppose the source provides certificates `d(x_n,C)<=delta_n` with `delta_n->0`. The distance function `d(.,C)` is 1-Lipschitz, so `d(x_infty,C)<=d(x_infty,x_n)+delta_n->0`. Thus `x_infty in C`.

Conversely, if `d(x_n,C)>Aq^n/(1-q)` at some `n`, then `x_infty notin C` by the triangle inequality; if `x_infty notin C`, closedness gives `d(x_infty,C)>0`, and sufficiently deep n necessarily satisfies the strict finite witness inequality. This is a TWO-SIDED logical **limit certificate**, provided distance-to-C enclosures can actually be sourced and evaluated. An existence theorem for the limit alone does not provide that separate decision oracle.

For a real-valued `L`-Lipschitz target `phi`, `|phi(x_n)-phi(x_infty)|<=L Aq^n/(1-q)`. Therefore positive strict margin is finitely witnessed when `phi(x_n)>L Aq^n/(1-q)`, and negative strict margin similarly. But a critical `phi(x_infty)=0` may never receive strict positive or negative finite evidence. The target `{x:x<1}` is OPEN: every dichotomy stage lies in it while `x_infty=1` does not. This refutes a property-preservation rule lacking closedness, uniform slack or continuity.

### ZS-09. Non-effective convergence obstruction (CLASSICAL SPECKER RESULT; NOT COMPUTATION CLAIM)

There exist computable, monotonically increasing, bounded sequences of rational numbers whose limit is a *noncomputable real* (Specker, 1949). Hence bounded monotonicity and exact successor computability do **not** imply an effective modulus. SUCC F45 already invokes this no-go correctly; **new is its typed placement** among ZS-06's dependencies. It prevents a universal “each step is finite ⇒ algorithmically know when the error is below ε” conclusion. No halting oracle is simulated in this code.

### ZS-10. Fixed finite-prefix blindness (EXACT SOURCE COUNTERMODEL)

For any stage `N`, compare `x_n=1-2^-n` with `y_n=x_n` for `n<=N` and `y_n=x_n+1` thereafter. The two complete source laws have the same finite observed prefix, are both eventually convergent, but converge to 1 and 2. The added later discontinuity makes the second source fail the FIRST source's geometric increment/tail contract. Therefore **sourced generative-law identification is load-bearing**: finite samples cannot license the ZS-06 bound unless its all-stage law is established. This is a constructed negative control, not a hypothesis about real physical observers.

## 3. Two-dimensional Zeno: test depth and operator/Gamma depth

### ZS-11. CORRECTED source-specific finite-Gamma signed Weil tail (PROVED LOCAL, genuine coefficients)

For the actual completed Weil quadratic form on fixed `(-a,a)`, let `v in C_c^infinity(-a,a)`, set `u=i v'` with `int u=0`, and keep **every** authentic prime-power, half-density, one-Gamma contact, conductor (when relevant), and both polar terms unchanged. The prior SUCC PRs #71/#76 derive the Gamma-resolvent spectral component

\[
 B_\Gamma(\xi)=\sum_{j\ge0}\frac{4}{d_j(\xi^2+d_j^2/4)},\qquad d_j=4j+1.
\]

Define the **signed** partial form `Q_J` by truncating **only this positive bath** after `j=J-1`, *not* by dropping any negative prime/contact/pole term. Then the exact difference is

\[
 Q_\zeta(v,v)-Q_J(v,v)
 =\frac1{2\pi}\int_{\mathbb R}\left(\sum_{j\ge J}\frac4{d_j(\xi^2+d_j^2/4)}\right)|\hat u(\xi)|^2d\xi \ge0.
\]

For all `xi`, the multiplier tail is bounded above by `sum_(j>=J)16/(4j+1)^3`. The sum is majorized (for decreasing positive `f(x)=16/(4x+1)^3`) by its first term plus an integral:

\[
\boxed{0\le Q_\zeta(v,v)-Q_J(v,v)
 \le\left(\frac{16}{(4J+1)^3}+\frac{2}{(4J+1)^2}\right)\|v'\|_2^2,
 \quad J\ge1.}\tag{ZS-11}
\]

This is a genuine, unconditional **effective Zeno error bound** for the completed arithmetic source on its declared Sobolev domain. It is a conservative explicit version of already-known `O(J^-2)` estimates; **it does not prove sign**. It repairs the erroneous Gemini `1/(8J²)` coefficient: at `J=1` the very first scalar-frequency `xi=0` term is `16/125>1/8`. This contradicts that *purported pointwise multiplier* bound. A bound limited to a *fixed* short support interval requires separate analysis; scalar counterexamples are not automatically normalized compact test vectors on that interval.

**Finite negative witness theorem.** For one fixed admissible `v`, if a mathematically authenticated enclosure `Q_J(v,v)<=U_J` satisfies

\[
 U_J+\varepsilon_J\|v'\|_2^2<0,
\]

then `Q_zeta(v,v)<0`. Conversely, if `Q_zeta(v,v)<0`, sufficiently deep truncation and sufficiently accurate source-authenticated interval evaluation yield such a negative certificate. The converse uses `Q_J->Q` and `epsilon_J->0`; a **finite negative test-function witness is not the same as an algorithm proving positivity on all tests**. Code tests only rational logical gates, NOT actual signed-Weil interval values.

**All-test conditional equivalence:** on each common fixed Sobolev test domain,

\[
\boxed{Q_\zeta\ge0\quad\Longleftrightarrow\quad
 Q_J(v,v)\ge-\varepsilon_J\|v'\|_2^2\quad
 \forall J\ge1,\ \forall v,}
\]

where `epsilon_J` is the displayed valid upper bound. Forward follows from `Q_J>=Q-epsilon_J||v'||²` and backward by `J->infinity`. This is an equivalent restatement, **not independent source positivity**; proving the right side from Euler arithmetic is precisely the outstanding RH-hard arrow. A single finite `J` calculation on finitely many `v` proves neither universal claim. The full RH Weil criterion requires every interval `a>0`, not just first-prime `a=1/2`.

### ZS-12. Dense form-domain Zeno (CLASSICAL AND ESSENTIAL DOMAIN GATE)

Let `D` be the domain of a closed semibounded quadratic form `Q`, with form norm `||.||_D`. Suppose `V_1 subset V_2 subset ...` are finite-dimensional subspaces whose union is dense **in the form norm**, and `Q` is continuous in that norm. If `Q(v)>=0` for all `v` in each `V_N`, then by approximation `Q>=0` on D. This is a complete mathematical proof using infinitely quantified finite-dimensional inequalities. Checking only one `V_N` is inadequate; checking only convergence in underlying `L²` rather than the form norm is inadequate for an unbounded Gamma/derivative form. For example `v_n(x)=sin(n pi x)/n` tends to zero in `L²(0,1)` but `||v'_n||²_2=pi²/2` does not tend to zero.

If both V-depth `N` and Gamma-depth `J` vary, a lawful diagonal schedule requires `v_N->v` in the form norm, `Q_J(v_N)` known on the **same** source/domain, and `epsilon_J||v'_N||²->0`. Interchanging limits without such bounds is not licensed. This is source-indexed two-dimensional Zeno completion.

### ZS-13. Finite/infinite Schur-complement Zeno certificate (CLASSICAL / PROVED HERE)

Let `H=F\oplus K`, where `F` is finite-dimensional and `K` is a closed Hilbert complement. On `F\oplus D_K`, a real closed symmetric form is

\[
 Q(f+k)=f^TMf+2\langle Bf,k\rangle+Q_K(k),
 \quad Q_K(k)\ge\kappa\|k\|^2,\ \kappa>0,
\]

where B:F->K is bounded (finite F). Let `R` be a positive semidefinite **certified upper matrix** satisfying `B*B <= R` in the Loewner order. Then

\[
 Q(f+k)\ge f^T(M-\kappa^{-1}R)f.
\]

Indeed `kappa||k||²+2<Bf,k> = kappa||k+Bf/kappa||² -||Bf||²/kappa`. Consequently

\[
\boxed{M-\kappa^{-1}R\succeq0\quad\Longrightarrow\quad Q\succeq0.}\tag{ZS-13}
\]

The code checks **only** the rational finite-matrix PSD assertion via exact Schur recursion, even with zero pivots. The hypotheses `Q_K>=kappa ||k||²`, `R>=B*B`, the fidelity of the source, and the operator-form domain are **not** proved by supplying numeric matrices. A failing sufficient matrix is not a negative witness for Q. For actual Weil analysis, PR #86 reports a 30-vanishing-moment infinite-dimensional complement bound `kappa=369/10000` on `a=1/2`—**conditional on independent audit of that proof**. To complete the new interface, choose explicit dual moment test functions, prove they lie in the common operator/form domains, and produce rigorous source-driven enclosures for `M` and `R`. The H¹ error in ZS-11 cannot be silently substituted for an L² operator norm on all test functions. Neither a finite Gram scan nor a generic covariance is permitted to replace the signed Weil form.

**Critical-margin obstruction:** if the Schur matrix is PSD but has zero eigenvalues, interval arithmetic by itself may never produce a *strict* positive gap; structural equalities, exact factorization, or symmetry may be indispensable. This is the close analogue of Zeno's finite stages never equaling their limit, without implying the limit's sign.

## 4. Operational meaning: a hierarchy of proof certificates

A useful minimal scheme is:

- `SOURCE`: original mathematical law `S`, source ID, epoch, basis and domain.
- `SUCC`: checkable finite construction/recurrence (not an actual empirical event unless separately authenticated).
- `TAIL`: a universally proved error budget in a specified topology (not merely convergence demonstrated at sampled cutoffs).
- `COMPLETION`: choice of complete ambient mathematical space and an actualization condition for the original source.
- `TARGET`: stability of the target under the limit (closedness, continuity, compactness, exact algebra or quantified operator form convergence).
- `RESOURCE`: effective modulus and causal/physical feasibility, typed separately.
- `PROOF`: paper/Lean/interval certificate status, not model confidence.

**NO-GHOST theorem-practice rule:** a `FormalLimit` record does not create a physical receipt; a source stamp does not authenticate a real source; a failed target test does not automatically validate a different source; and a finite grid is not the full test-function domain.

`observational_succ/zeno_certificate.py` implements rational geometric clocks, Achilles, rational sqrt2 brackets, arrow and stadium source-frame controls, Thomson lamp, delayed-tail mutations, Gamma upper budgets, authenticated-interval logical gates, and finite/infinite rational Schur sufficiency. No arbitrary lambda can declare a universal mathematical theorem to be true merely because it passed `n=1000`.

## 5. Precise RH dependency and immediate next experiment

\[
\boxed{
\begin{array}{c}
\text{True Euler }\Lambda(p^k),\;\text{one }\Gamma_\mathbb R,\;\text{poles/contact/half-density}\\
\downarrow\ \text{signed common Weil form } Q_\zeta\\
\downarrow\ \text{finite }Q_J\text{ plus valid }H^1\text{ Zeno tail }\varepsilon_J\\
\downarrow\ \color{red}{\text{MISSING: signed source lower bound for all tests}}\\
Q_\zeta\ge0\Longleftrightarrow RH.
\end{array}}
\]

The current Zeno theorem discharges **the topological/analytic tail-certification arrow**, not the arithmetic sign. It does not magically convert positive Gamma Markov rungs into positivity of the full signed object. What it does add is a modular checkable structure for any attempt that claims it has crossed the last arrow, and a concrete 30-moment finite-bottleneck candidate (PR #86) where structural progress might be achievable.

**Next falsifiable lemma (explicit):** At `a=1/2`, choose explicit smooth test functions `f_0,...,f_29` dual to the first 30 moments, and a closed complementary subspace `K={v:∫x^jv=0, 0<=j<30}` in the **correct** form topology. Prove `Q|K>=kappa||.||²` from original arithmetic for some `kappa>0` (audit PR #86), prove the mixed form defines a bounded `B:F->K` on the chosen topology, and produce *rational outward enclosures* of `M` and `R>=B*B` sufficiently strong that exact Schur positivity succeeds. Against it run wrong-half-density, contact ±2log2, fake composite6 beyond its activation window, source-parity χ4 and high-frequency near-null controls. Declare FAILURE rather than alter the target if the Schur matrix fails.

**Epistemic classification:** This paper's Banach/contraction/closed-property/dense-domain/Schur techniques are classical. Their source-indexed assembly is **new to SUCC**; academic originality has not been established. Universal theorems have paper proofs and finite exact examples, *not Lean kernel proofs*. External physical source calibration not established; no nontrivial zeta zero coordinates read; RH, ABC, Goldbach and Collatz not solved.
