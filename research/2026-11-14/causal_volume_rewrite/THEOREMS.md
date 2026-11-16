# Principia Observatoris × BBP — Causal-Volume Rewrite Calculus

**2026-11-14.** Research-only child of [draft #634](https://github.com/femboy2112/SUCC/pull/634), following #632's pointed-zero rigidity and SUCC's original arithmetic/gauge frontier. **π base-16 normality, R0, original Weil positivity and RH remain OPEN.** This package is a systematic *typed normal form* for the original zero-seeded BBP source, not a proof that abstract Gamma wavefronts force digit equidistribution.

**Origin of the question:** What happens if *every occurrence* of an original BBP pole, source register, completion, future tail, observer coordinate, and phase is expanded into a causal-volume representation first, and algebraic cancellations are performed **without changing the source or commuting nonlinear observers through integration**? Do the simplifications furnish reusable rules? **Answer: yes, within a declared Mellin-polynomial/radix grammar.** The pointwise Oily/BBP cancellation was already written in [GG-05 of #634](../gamma_genesis/THEOREMS.md); the contribution here is a general normal form, a signed finite-difference/Gamma hierarchy, a new moving-Mellin-twist inequality, and exact hostile models showing the domain of each inference.

## A. Grammar and provenance: no imaginary physical source

For integers `a>=1`, `b>=2`, a nonzero polynomial `Q(t)=sum_j c_j t^j in Q[t]`, and **pointed zero**, define

\[
 r_Q(n)=\int_0^1t^{a(n-1)}Q(t)dt=\sum_j\frac{c_j}{a(n-1)+j+1},\quad
 U_0=0,\quad U_{n+1}=bU_n+r_Q(n+1).
\tag{CV0}
\]

For the original, non-negotiable four-pole BBP passport, take

\[
(a,b)=(8,16),\quad Q(t)=4-2t^3-t^4-t^5,
\quad r_Q(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\tag{BBP0}
\]

The geometric-series completion is absolutely convergent because `b>1` and `Q` is bounded on `[0,1]`. Set `D(t)=b-t^a`, `R(t)=Q(t)/D(t)` and

\[
 \mathcal M(s)=\int_0^1t^s R(t)dt,\quad \Re s>-1.
\tag{CV1}
\]

This is a Mellin-transform chart on one source-attached measure, not a new latent independent stochastic carrier. In the original BBP instance, `R(t)>=0` on `[0,1]` by the exact factorization in §B. A generic polynomial `Q` need **not** be positive; positivity and all ensuing inequalities require a separate source certificate.

## CV-01 — Pole expansion and rational causal-volume normal form (PROVED PAPER / CLASSICAL)

One finite source step has source polynomial `Q`; expanding the original recurrence from its root yields the **finite causal-volume polynomial**

\[
 H_n(t)=\sum_{j=0}^{n-1}b^{n-1-j}t^{aj},\quad H_0=0,\qquad
 (b-t^a)H_n=b^n-t^{an}.
\tag{CV2}
\]

Define the signed-pole prefix `P_n=sum_{j=1}^n b^{-j}r_Q(j)`, the future Green tail `T_n=sum_{j>=1} b^{-j}r_Q(n+j)`, and `\alpha=sum_{j>=1}b^{-j}r_Q(j)`. Termwise integration (absolute, uniform convergence) gives **simultaneously**

\[
\boxed{\begin{aligned}
\alpha&=\mathcal M(0),\\
T_n&=\mathcal M(an),\\
P_n&=\int_0^1R(t)[1-(t^a/b)^n]dt,\\
U_n&=\int_0^1Q(t)H_n(t)dt
    =b^n\mathcal M(0)-\mathcal M(an),\\
r_Q(n+1)&=b\mathcal M(an)-\mathcal M(a(n+1)).
\end{aligned}}
\tag{CV3}
\]

The **pointed zero is the equalizer at n=0**, `U_0=M(0)-M(0)=0`, and the successor follows by subtracting the last two identities. No extra initial real or all-future oracle is inserted into the finite recurrence.

**Regular calculus:** `POLE→MELLIN MOMENT`, `RADIX SUM→FINITE RESOLVENT`, `GEOMETRIC COMPLETION→SINGLE MEASURE`, `SAMPLED MOMENT DIFFERENCE→FORCING`, and `POINTED ZERO→ORIGIN EQUALIZER`. Each is exact for all lawful `n`, not finite-pattern extrapolation.

The canonical reduced rational kernel is obtained by `g=gcd(Q,D)` over `Q[t]`, `R=(Q/g)/(D/g)`. Rational-field uniqueness makes the reduced form independent of factorization route (up to an overall invertible scalar). The executable standard-library engine implements Euclidean polynomial gcd and exact division with `Fraction`, without inserting a presumed special function.

## CV-02 — Recover the exact Oily source by *two* simultaneous cancellations (EXISTING SOURCE IDENTITY, RECONSTRUCTED)

For BBP, the signed pole numerator has **a positive factorization**:

\[
\begin{aligned}
Q(t)&=(1-t)(t^2+2)(t^2+2t+2),\\
16-t^8&=(2-t^2)(t^2+2)(t^2-2t+2)(t^2+2t+2).
\end{aligned}
\]

Therefore, cancelling exactly `(t²+2)` and `(t²+2t+2)` **inside the same integral**, we get

\[
\boxed{R(t)=\frac{Q(t)}{16-t^8}
=\frac{1-t}{(2-t^2)(t^2-2t+2)}.}
\tag{CV4}
\]

This is **exactly** the original positive Oily source of Main XIII and GG-05, not merely another integral with the same total. Every authentic moment `T_n`, partial prefix `P_n`, rational state `U_n`, and forcing `r(n)` is therefore a different **typed operation on the same function**. The identity is pointwise, with no stochastic interpretation necessary.

**The full causal two-register realization cancels to the very same kernel.** Keep the *original* Oily stage weights (no fitted parameters)

\[
u(t)=t-t^2/2,\qquad v(t)=t^2/2,
\qquad M(t)=\begin{pmatrix}u(t)&1\\0&v(t)\end{pmatrix},
\quad e_2=(0,1)^\mathsf T.
\]

Then `u+v=t`, and

\[
4(1-u)(1-v)=(2-t^2)(t^2-2t+2).
\]

Therefore the *three* source representations form an exact triangle:

\[
\boxed{\frac{Q(t)}{16-t^8}
=\frac{1-t}{4(1-u(t))(1-v(t))}
=\frac{1-t}{4}\,[ (I-M(t))^{-1}e_2]_1.}
\tag{CV4b}
\]

Taking a Neumann expansion of the last expression yields **every actual Oily positive grade**

\[
R(t)=\sum_{j\ge0}p_j(t),\qquad
p_j(t)=\frac{1-t}{4}\sum_{k=0}^ju(t)^k v(t)^{j-k}.
\]

The exact finite tail bound from the historical oscillator work, `0<=R−sum_(j<=N)p_j <= (1−t)(N+3)/2^(N+2)`, is reproduced in exact rational tests. This is the requested *causal volume → linear state evolution → analytic realization* written **on the same BBP parameter t**, not a putative equality of unrelated stochastic devices. It identifies the two-register positive transfer as a lawful representation of the source kernel, but it does **not** assert that the signed BBP carry phase is the Oily state variable.

The positivity is transparent: for `0<=t<1`, numerator `(1-t)>0`, both denominator factors are positive, and `R(1)=0`. The signed BBP residues have not been discarded; their algebraic recombination is what produces the positive polynomial `Q`.

**Sign-sum cancellation:** with coefficients `c=(4,-2,-1,-1)` and exponents `k=(0,3,4,5)`, `sum c_j=Q(1)=0`. The first nonvanishing boundary derivative is `-Q'(1)=15`. These are explicit source-jet identities, not a proof that chronological circle phases cancel.

## CV-03 — Each discrete causal difference produces an additional Gamma boundary face (PROVED; elementary moment theorem)

Write `T_n=M(8n)`. For **every** pair of integers `n,k>=0`, finite differences in the causal index satisfy

\[
\boxed{(-1)^k\Delta^k T_n
=\int_0^1t^{8n}(1-t^8)^kR(t)dt>0.}
\tag{CV5}
\]

The proof is literally `Δ t^(8n) = t^(8n)(t^8-1)`, iterated under the integral; strict positivity holds on `(0,1)` for the authentic positive R. This is the Hausdorff complete-monotonicity hierarchy. Its **forcing companion** is entirely rational:

\[
(-1)^k\Delta^k r(n+1)
=\int_0^1t^{8n}(1-t^8)^kQ(t)dt
=\sum_{j=0}^k(-1)^j\binom kj r(n+j+1)>0.
\tag{CV6}
\]

This is an **exact set of generic inference rules**: each lawful successor difference multiplies the common source integrand by one more nonnegative local boundary factor. It also proves ordinary log-convexity `T_n²<T_(n-1)T_(n+1)` and `r(n)²<r(n-1)r(n+1)` in the nondegenerate continuous source by Cauchy–Schwarz.

The endpoint source has `R(1−δ)=δ+O(δ²)`, and `1−t^8=8δ+O(δ²)`. Standard endpoint rescaling `y=8nδ`, dominated by an exponential tail, proves for **each fixed k**

\[
\boxed{(-1)^k\Delta^kT_n
\sim\frac{\Gamma(k+2)}{64\,n^{k+2}}\quad(n\to\infty).}
\tag{CV7}
\]

Hence even without adding independent observer stages, the *finite-difference filtration of the actual positive BBP source* generates a Gamma-shape ladder `2,3,4,...` in its endpoint behavior. This is the concrete algebraic origin of a succession of effective higher-dimensional volume faces in this declared Mellin grammar. It is **not** the same statement as independent stochastic waits or the physical number of spatial dimensions.

**Each face has its own moving signed Mellin spectrum.** For each fixed `k>=0` and real `lambda`, let

\[
F_{n,k}(\lambda)=
\frac{\int_0^1t^{8n(1+i\lambda)}(1-t^8)^kR(t)dt}
{\int_0^1t^{8n}(1-t^8)^kR(t)dt}.
\]

The same endpoint substitution `y=8n(1-t)` shows that the **normalized k-th causal face** converges to `Gamma(k+2,1)` and

\[\boxed{F_{n,k}(\lambda)\longrightarrow (1+i\lambda)^{-(k+2)}.}\tag{CV7b}\]

The numerator is a complex character of **one** source measure, not a sum of independent amplitudes. Proof: the unnormalized transformed integrand, divided by its `n^(-(k+2))` scale, tends pointwise to `y^(k+1)e^(-y)` times the common constant; the bounds `t^(8n)<=e^(-y)`, `(1-t^8)^k<=(8y/(8n))^k`, and `R<=y/(8n)` supply a global integrable `y^(k+1)e^(-y)` envelope. The extra factor `t^(8ni lambda)` converges to `e^(-i lambda y)` in modulus one. Dominated convergence and Gamma's Laplace transform prove the limit. This extends the k=0 convergence in §CV-04 qualitatively; the explicit **quantitative** bound in CV-09 is currently only claimed for k=0.

**Generic version.** If a grammar's positive kernel has `R(1−δ)=C δ^d+o(δ^d)` with `C>0`, then `(-1)^k Δ^kT_n ~ C Γ(d+k+1)/(a^(d+1)n^(d+k+1))`, for fixed k, provided R is suitably bounded and has no pathological endpoint behavior. The effective Gamma shape is `d+k+1`. This describes a boundary-jet universality class, not a proof of universality across arbitrary untyped sources.

## CV-04 — Source-attached moving Mellin twist has a **quantitative signed** Gamma limit (PROVED PAPER; new bound)

For `m>0` put `I_m=M(m)` and normalize the **actual source measure** by

\[
\mu_m(dt)=\frac{t^mR(t)}{I_m}\,dt,
\quad Y_m=m(1-t).
\]

The previously proved GG-06 endpoint bridge gives `TV(Law(Y_m), Gamma(2,1)) <=7/m`. We derive a new **moving-frequency Mellin transform** result:

\[
\boxed{\frac{\mathcal M(m(1+i\lambda))}{\mathcal M(m)}
\longrightarrow \frac1{(1+i\lambda)^2}
\qquad(m\to\infty),\quad \lambda\in\mathbb R.}
\tag{CV8}
\]

This is a *signed phase* of the **authentic positive source**, sampled at imaginary Mellin frequency `omega=lambda*m`. Unlike a fixed-frequency transform (which tends to 1), this moves with the boundary layer and measures its Gamma volume.

**Explicit uniform error bound.** For integer `m>=14` and **every real** λ,

\[
\boxed{
\left|\frac{\mathcal M(m(1+i\lambda))}{\mathcal M(m)}-
\frac1{(1+i\lambda)^2}\right|
\le\frac{14+12|\lambda|}{m}+2m^2 2^{-m}.
}
\tag{CV9}
\]

**Proof (no fitted constants).** Let `delta=1−t`. The original `D(delta)=(2−t²)(t²−2t+2)=1+2delta+2delta³−delta⁴>=1`, and source pointwise bounds include `delta(1−2delta)<=R(t)<=delta`. Thus

\[
I_m\ge B_1(m)-2B_2(m)=\frac{m-1}{(m+1)(m+2)(m+3)},
\]

and `1−m²I_m<=7/m`. Under `y=m(1−t)`, the **unnormalized** density multiplied by `m²` is pointwise ≤ `y e^(−y)` and has total mass `m²I_m`. Consequently the normalized Y-law has TV distance ≤ `1−m²I_m<=7/m` from Gamma(2,1). For `m>=14`, this also gives `I_m>=1/(2m²)`.

Since `R(t)<=1−t` and `B_3(m)=6/[(m+1)...(m+4)]<=6/m⁴`,

\[
\mathbb E_{\mu_m} Y_m^2
=\frac{m^2}{I_m}\int t^m(1-t)^2R(t)dt\le12.
\]

Also `Pr_mu(Y_m>m/2)<=m²2^(−m)`. For `0<=y<=m/2`, elementary logarithmic series give `0<=−m log(1−y/m)−y<=y²/m`, hence the phase mismatch between `exp(i λ m log t)` and `exp(−i λ y)` is bounded by `|λ|y²/m`. The remaining tail contributes at most `2m²2^(−m)`. Finally, replacing the Y-law by its Gamma(2,1) limit changes an expectation of a unit-modulus function by at most twice total variation, `14/m`. The Gamma Laplace transform is `(1+iλ)^−2`. Add these terms to obtain (CV9). QED.

The limit holds uniformly for bounded λ by the stated bound. Its modulus for λ≠0 is `1/(1+λ²)<1`: **authentic-source log-Mellin cancellation, with an explicit analytic interface**. It is not digit-orbit Weyl cancellation because the actual chronological phase `e(hU_n)` is neither `t^(i λm)` nor a conditional average over t.

The independent SymPy/mpmath oracle checks this identity for 15 frequency/depth pairs at 60 digits; exact local tests verify the rational certificate and its source assumptions.

## CV-05 — A precise phase/branch firewall: integrating before exponentiating is NOT optional

Define the actual **selected, unwrapped** real phase and integer lift by

\[
U_n=16^n\mathcal M(0)-\mathcal M(8n),\qquad
\kappa_n=\lfloor U_n\rfloor-16\lfloor U_{n-1}\rfloor,
\]

and `E_{n,h}=exp(2πi h U_n)` for integer h. The source recurrence gives the exact **frequency ladder**

\[
\boxed{E_{n+1,h}=E_{n,16h}\,e^{2\pi i h r(n+1)}.}
\tag{CV10}
\]

This is a complex multiplicative cocycle over the actual deterministic source clock. It retains phase, forcing signs, original zero, and chronological ordering. It does **not** yield nontrivial cancellation on summing `E_{n,h}` over n.

The dangerous illicit rewrite is

\[
\color{red}{e^{2\pi i h\int f(t)dt}\ \overset{\mathrm{FALSE}}{=}\ \int e^{2\pi i h f(t)}dt.}
\]

A universal counterexample uses `f(t)=t`, `h=1`: the left is `e^{πi}=−1`, the right is `∫_0^1e^{2πit}dt=0`. Phase is a **nonlinear observer** of the source-integrated volume. Its interchange with integration requires a new jointly justified approximation, cumulant estimate, special intertwiner, or source-defined coupling. Likewise integer floor/carries cannot be pushed through Mellin integrals or forgotten when reconstructing digit words. `16−t^8` polynomial cancellation and Gamma endpoint positivity are not substitutes for the signed all-large-N Weyl estimate.

**What a legitimate new theorem must produce:** an explicit source-preserving map or inequality from the moving-Mellin phase/correlation operators in CV-08/CV-09 to the selected `E_(n,h)` cocycle, uniform enough in the chronological sample length N to prove R0 or `sum_(n<N)E_(n,h)=o(N)`. A phase transport with only bounded error does not bound the source sum.

## CV-06 — Source gauge, finite-horizon impersonation, and why positivity is not normality

A change of variable `t=phi(u)` in the same integral is an allowed **representation change** when the source measure and Jacobian are transported together; it does not change π, the original forcing, or the source's initial zero. The exact code verifies the reflection `t=1−u` (with reversed bounds) through finite moments. Changing `Q`, radix, root or source law without a proven compensated source map is NOT a gauge transformation merely because an integral looks similar.

**Hostile zero-seeded Gamma(2) model.** Keep `(a,b)=(8,16)` and **the zero origin**, but take

\[
R_\mathrm{rat}(t)=1-t,\qquad Q_\mathrm{rat}(t)=(16-t^8)(1-t).
\]

It has the SAME order-one endpoint zero with coefficient 1, and all the Gamma(2) asymptotics and CV-05 Hausdorff positivity rules. Yet

\[
\alpha_\mathrm{rat}=\int_0^1(1-t)dt=\frac12,
\qquad T_n^{\rm rat}=\frac1{(8n+1)(8n+2)}.
\]

Thus its completed base-16 orbit is rational and emphatically **nonnormal**. This source changes `Q` and its pole grammar, so it is **not** a counterexample to a theorem about the genuine four poles. It does refute any proposed *general* rule “positive Gamma(2) volume + pointed zero + coherent finite differences ⇒ radix normality.” The exact test instantiates the full alternative zero-seeded recurrence.

**Positive finite-depth source impostor with the same completed π value.** For a fixed integer M, define `L=8M+1` and

\[
f_M(t)=\frac{d^{L}}{dt^L}[t^{L+2}(1-t)^{L+2}],\quad
R_\varepsilon(t)=R(t)+\varepsilon f_M(t),\quad
Q_\varepsilon(t)=(16-t^8)R_\varepsilon(t).
\]

For every `0<=k<=M`, integration by parts `L` times (the boundary derivatives vanish) gives

\[
\int_0^1t^{8k}f_M(t)dt=0.
\]

At `k=M+1`, that integral is **nonzero**: after L integrations by parts it becomes a nonzero signed multiple of a positive Beta integral. The polynomial `f_M` vanishes at least quadratically at `t=0,1`; choose a sufficiently small nonzero rational epsilon so that `R_epsilon(t)>=0` on `[0,1]` and its leading `(1−t)` endpoint coefficient remains one. The source's **completed total is exactly unchanged**, since the zeroth moment is preserved; the first M Green moments and first M forcing steps also agree. Yet the `(M+1)`-st moment and later source forcing differ. A precise rational epsilon based on coefficient bounds is implemented and tested.

**Interpretation:** there are real, source-distinct polynomial representations with the same completed π point and arbitrarily long identical finite observation prefixes. They do **not** give two different normality answers because their completed point is identical. This is a target-relative *representation* ambiguity, not a counterexample to the original unique four-pole source. It illustrates why an observed finite tower does not by itself attest the source polynomial. The original source passport is an additional hypothesis, not an observation inferred from positive Gamma shape.

## CV-07 — A usable rewrite rulebook, with explicit proof boundaries

| Rule | Required type/hypothesis | Guaranteed output | Does NOT guarantee |
|---|---|---|---|
| Pole-to-Mellin | Actual rational-pole source plus a declared offset/stride | Exact polynomial moment forcing | Positivity without Q sign proof |
| Geometric volume | Fixed radix b>1, pointed zero, same polynomial Q | Exact finite H_n and unique recurrence solution | Selected digit statistics |
| Rational cancellation | Polynomial gcd with nonzero denominator on domain | Unique reduced Oily-like kernel (up to unit) | A physical stochastic realization |
| Positive boundary jet | Certified R≥0, R~C(1−t)^d | Gamma(d+1) endpoint and moments | A new physical dimension |
| Causal differences | Same R sampled at an | Complete monotonicity / Gamma-shifted finite-difference faces | Signed Weyl cancellation |
| Complex Mellin twist | Declared source measure and log-character | Source-specific signed frequency response and error | Chronological phase or carry control |
| Coordinate gauge | Invertible source chart plus Jacobian/typed labels | Invariant integral/readout | Permission to mutate Q or seed |
| Signed phase cocycle | Original U0=0, forcing and integer lift | Exact frequency ladder | Sublinear exponential sum |
| Normality conclusion | Source-selected all-mode signed saving or equivalent criterion | π base-16 normality | Available from positivity alone |

**Verdict (relative to current SUCC toolkit):** The expansion-and-cancel approach genuinely yields a **regular symbolic calculus** for a large class of Mellin-polynomial source constructions. It identifies exactly where cancellations are structural and where new arithmetic estimates are necessary. It solves a **pathway gap** in representing the same BBP source across Oily/Gamma and rational recurrence coordinates, **not** the remaining signed-coherence gap for π. The physical/source adequacy of Poisson/Gamma waiting-time interpretations remains independently UNVERIFIED.

## Next falsifier / genuine proof frontier

Build a source-authentic **twisted cross-time transfer** whose input is the actual BBP polynomial measure, literal carry, and zero-selected frequency ladder, and whose output is a quantitative signed chronological margin. Predeclare an explicit mixed Mellin/chronological identity, then try to refute it on a held-out original-source epoch and on authentic source-preserving chart changes. Separate true root/recurrence statements from broad polynomial-source controls. If no such operator can be constructed in the current algebra, certify the toolkit-relative gap, not a universal impossibility theorem.

Provenance: SUCC [GG-05/GG-06](../gamma_genesis/THEOREMS.md) (source Mellin/Oily and Gamma TV), [PI_NORMALITY_FRONTIER.md](../../../docs/PI_NORMALITY_FRONTIER.md) (original Weyl, R0 and carries), [zero-anchor #632](../seed_source_rank/POINTED_ZERO_THEOREM.md), [Oily wavefront #344](../../2026-10-28/WAVEFRONT_OSCILLATOR_COMPLETION_AND_CAUSAL_INVERSE.md). Classical Hausdorff moment/Gamma and Mellin mathematics not claimed as academic novelty. This work does not alter any historical source files.
