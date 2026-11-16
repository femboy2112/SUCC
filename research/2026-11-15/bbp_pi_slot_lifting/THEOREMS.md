# OPERATION π-SLOT — From the BBP coin to a source-closed phase path

**Date:** 2026-11-15. **Status:** Additive SUCC research; paper derivations and finite tests; π base-16 normality and R0 remain OPEN. **Original source:** literal four signed poles and `U_0=0`; see `observational_succ/duck_bbp.py`, Main XXV `docs/PI_NORMALITY_FRONTIER.md`, and research PRs #646, #648, #649. This dossier corrects an earlier PR #648 statement about the coboundary mutant's π target; it does not alter that branch.

## Definitions and exact source authentication

Let

\[
Q(t)=4-2t^3-t^4-t^5=(1-t)(2+t^2)(2+2t+t^2),\quad
 g(t)=\frac{Q(t)}{16-t^8},\quad
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

Then `r(n)=∫_0^1 Q(t)t^{8(n-1)}dt`, `0<g(t)≤1-t` for `0≤t<1`, and, **using the classical imported BBP identity**, `x=∫_0^1g(t)dt=π/16`. Preserve the original `U_0=0`, `U_n=16U_{n-1}+r(n)`; the real Green correction is `T_n=Σ_{j>=1}16^{-j}r(n+j)`.

On one probability space, take a uniform threshold `τ∼U(0,1)`. Using **independent conditional auxiliary uniforms given τ** define:

\[
A_\tau=\mathbf1_{U_0>\tau},\quad
B_\tau=2+\mathbf1_{\max(U_1,U_2)\le\tau},\quad
C_\tau=2+2\mathbf1_{V_1\le\tau}+\mathbf1_{\max(V_2,V_3)\le\tau}.
\]

With independent `W∼U(0,1)`, define **one Bernoulli source click** `C=1[W≤A_τB_τC_τ/(16-τ^8)]`. Names `C` (click) and `C_τ` (source factor) are distinct. This is the exact, already tested #649 π-free random program, now **retained jointly** with the threshold:

\[
\Pr(C=1\mid\tau=t)=g(t),\qquad\mathbb EC=x=\pi/16.
\tag{PS0}
\]

Every meaningful result below depends on **the same** `(τ,C)` across source times. Resampling an independent source pair at every time destroys the stated Hankel covariance. All physical quantum/Higgs interpretations are expressly outside the mathematical claims.

## PS-01 — Unfold every expanding-π orbit slot (EXACT)

Put `Y_n=C τ^{8n}`. For **all** `n,m≥0`:

\[
\boxed{\mathbb EY_n=T_n=\int_0^1 t^{8n}g(t)dt,\quad
\mathbb E[C(16^n-\tau^{8n})]=U_n,\quad
\mathbb E[Y_nY_m]=T_{n+m}.}
\tag{PS1}
\]

**Proof:** Conditional expectation gives the first formula. The second follows from the polynomial identity `(16^n-t^{8n})/(16-t^8)=Σ_{j=0}^{n-1}16^{n-1-j}t^{8j}`; integration gives the authentic recurrence and literal zero. The last formula uses `C²=C`, so `Y_nY_m=Cτ^{8(n+m)}`. No π oracle is inserted. In particular the unwrapped real lift is *exactly* `16^n x=U_n+T_n`, where the integer winding has **not** been reduced prematurely.

## PS-02 — One source operator generates the whole BBP π path (EXACT)

On the Hilbert space `L²(Ω,P)` of the **chosen random program**, let `L` be multiplication by `τ^8`, so `0≤L≤I`, and let `1` denote the constant readout vector. Then

\[
\boxed{r(n)=\langle1,(16I-L)L^{n-1}C\rangle,\quad
T_n=\langle1,L^nC\rangle,\quad
U_n=\langle1,(16^nI-L^n)C\rangle.}
\tag{PS2}
\]

The first identity follows pointwise after conditioning: `(16-t^8)g(t)=Q(t)`. The finite operator geometric series telescopes **in operator norm**:

\[
\boxed{\sum_{j=1}^N16^{-j}(16I-L)L^{j-1}=I-16^{-N}L^N.}
\tag{PS3}
\]

Taking the readout against `C`, and then letting `N→∞` (because `||L||≤1`), yields the original BBP constant `x=⟨1,C⟩` and proves its finite rational/source-tail decomposition. This **realization is chosen from the known source identity**, not an independent proof that the BBP series equals geometric π. The operator is multiplication, not a physical time-Hamiltonian.

## PS-03 — Positive Hankel source geometry; genuine correlated time states (EXACT)

For all finitely supported real or complex coefficients `a_n`,

\[
\boxed{\mathbb E\left|\sum_n a_nY_n\right|^2
=\sum_{n,m}a_n\overline{a_m}T_{n+m}\ge0.}
\tag{PS4}
\]

The matrix `T_{n+m}` is positive semidefinite. It is not a constant or independent-time covariance: `T_{n+m}>0` whenever n,m are finite. The moment sequence is strictly completely monotone:

\[
\boxed{(-1)^k\Delta_\ell^kT_n
=\int_0^1g(t)t^{8n}(1-t^{8\ell})^kdt>0}
\tag{PS5}
\]

for integers `n≥0,ℓ,k≥1`, with `Δ_ℓT_n=T_{n+ℓ}-T_n`. This includes a genuine **four-time strictly positive** source lift at `(n,n+ℓ,n+q,n+q+ℓ)`.

The chiral sign `χ(n)=(-1)^{floor(n/2)}` from SUCC #648 yields the **completed-source Green version** of #649's r-moment Gram:

\[
G^T_{nm}=\chi(n)\chi(m)T_{n+m},\qquad
\mathcal E_k^T(n)=\int_0^1g(t)t^{16n}(1-t^{16})^{2k}dt
=\sum_{j=0}^{2k}(-1)^j{2k\choose j}T_{2n+2j}>0.
\tag{PS6}
\]

Using `g(t)=(1-t)+O((1-t)^2)` at t=1 and the classical beta integral gives, for every fixed integer k≥0,

\[
\boxed{\lim_{n\to\infty}n^{2k+2}\mathcal E_k^T(n)=\frac{\Gamma(2k+2)}{256}.}
\tag{PS7}
\]

This is a **different kernel** from #649's `r(2n+2j+1)` energy; it directly uses the actual future Green tail and has a different coefficient. No real Weyl saving follows from Gram positivity.

## PS-04 — The critical nonlinear trap: do not Fourier-transform before averaging (REFUTED INFERENCE)

The circle character is `e(t)=exp(2πit)`, with 2π **angular normalization**, distinct from the arithmetic target π/16. Since `C∈{0,1}`, for *every* integer n≥0 and h≠0,

\[
\boxed{\mathbb E[e(h16^n C)]=1\quad\text{but}\quad e(h16^n\mathbb EC)=e(h16^n\pi/16)\ne1.}
\tag{PS8}
\]

The inequality uses the imported irrationality of π. Thus **moving the expectation through the nonlinear Fourier character erases the real target completely**. Likewise `floor(q E C)` cannot be replaced by `E floor(q{C})`: for q=16 the true first digit of π/16 is 3, while `floor(16{C})=0` on every sample. These are decisive hostile controls against a naive stochastic π substitution.

More generally, a nonconstant unbiased representation of an exact unit phase cannot have modulus ≤1 almost surely: `|EZ|=1` with `|Z|≤1` implies Z is constant a.s. by equality in the triangle inequality. A nontrivial finite randomized phase path must use **complex nonunitary weights** or additional limiting operations.

## PS-05 — Exact marked-Poisson phase lift (EXACT CLASSICAL)

Fix an arbitrary intensity λ>0. Draw `N∼Poisson(λ)` and **independent source rows** `(τ_j,C_j)` from the genuine BBP-coin experiment, using the *same* rows across all time channels in one detector shot. For any finite integer mode vector `h_s` and source times `n_s`, let

\[
H=\sum_s h_s U_{n_s},\qquad
M_j=\sum_s h_s C_j\tau_j^{8n_s},\qquad c=2\pi.
\]

Define the randomized complex observable

\[
\boxed{\mathscr Z_{\lambda}=e(H)
\prod_{j=1}^{N}\left(1+\frac{icM_j}{\lambda}\right).}
\tag{PS9}
\]

It has **exact expectation equal to the original source's coherent real phase**:

\[
\boxed{\mathbb E\mathscr Z_\lambda
=e\!\left(\sum_s h_s (U_{n_s}+T_{n_s})\right),}
\tag{PS10}
\]

and its exact complex mean-square error is

\[
\boxed{\mathbb E|\mathscr Z_\lambda-\mathbb E\mathscr Z_\lambda|^2
=\exp\!\left(\frac{c^2}{\lambda}
 \sum_{s,t}h_s h_t T_{n_s+n_t}\right)-1.}
\tag{PS11}
\]

**Proof:** Condition on Poisson N, average the iid marks in each product factor, and sum the exponential generating series `Σe^{-λ}λ^N/N!`. For the squared modulus use `(1+i cM/λ)(1-i cM/λ)=1+c²M²/λ²`; `E[M²]=Σh_sh_tT_(n_s+n_t)`. Both the mean and squared norm are *exact*, not a CLT/large-λ approximation. The phase estimator is nonunitary on samples; its expected complex phase has modulus one. This is the standard finite Poisson probability-generating functional applied to **complex but bounded** factors.

At one time, the variance simplifies to `exp((2πh)²T_(2n)/λ)-1`, with `T_(2n)~1/(256n²)`. Using the unconditioned one-coin estimator for *the whole* `16^n x` instead would give variance `exp((2πh)²16^(2n)x/λ)-1`; the literal rational history extracts the enormous amplification exactly, leaving a vanishing tail-variance cost. This compares two explicitly declared instruments, not a lower bound on every possible algorithm.

The source is also accessible in a **Rao–Blackwellized** path: replace each `C_jτ_j^(8n)` by its conditional mean `g(τ_j)τ_j^(8n)`. This preserves (PS10) and reduces (PS11)'s quadratic moment to `∫g(t)^2(Σ h_st^(8n_s))²dt`. Since `g(t)≤1-t`, a single-time variance has exponent ≤`(2πh)²·2/[λ(16n+1)(16n+2)(16n+3)]`, decaying as `O_h(λ^-1 n^-3)`. This pays the variance cost of the additional source coin noise instead of assuming that a stochastic phase equals its expectation.

## PS-06 — Source-signed temporal taps and four-time real-circle return (EXACT)

For positive integer lag ℓ, the **common-row** difference is `Y_(n+ℓ)-Y_n=-Cτ^(8n)(1-τ^(8ℓ))`; the Bernoulli squared norm is

\[
\boxed{\mathbb E[(Y_{n+\ell}-Y_n)^2]
=T_{2n}-2T_{2n+\ell}+T_{2n+2\ell}>0.}
\tag{PS12}
\]

At fixed ℓ>0 it is asymptotic to `3ℓ²/(512 n^4)`; the Rao–Blackwellized norm is asymptotic to `3ℓ²/(2048 n^5)`. The shared-sample signed difference buys *two* extra powers of time decay relative to the single Bernoulli mark, and conditional-mean filtering buys a third. Independent rows at each time cannot reproduce these signed-difference norms. **Main XXVI boundary correction:** at ℓ=0 the difference and its squared norm are exactly zero; the prior nonnegative-lag wording with strict positivity was false at that endpoint.

For **any** integers n≥0, q≥1, ℓ≥1,

\[
\boxed{\begin{aligned}
\Delta_q\Delta_\ell(16^n x)&=\Delta_q\Delta_\ell U_n+D_{n;q,\ell},\\
D_{n;q,\ell}&=T_{n+q+\ell}-T_{n+q}-T_{n+\ell}+T_n\\
&=\mathbb E[C\tau^{8n}(1-\tau^{8q})(1-\tau^{8\ell})]>0.
\end{aligned}}
\tag{PS13}
\]

Here the first part is an exactly rational finite-source **integer-winding-retaining** lift. `D` is a strictly positive **signed real correction** with uniform and fixed-q bounds

\[
0<D_{n;q,\ell}\le \min\left(
 \frac{16\ell}{\prod_{j=1}^3(8n+j)},
 \frac{384q\ell}{\prod_{j=1}^4(8n+j)}
\right).
\tag{PS14}
\]

The bounds use only `g(t)≤1-t`, `1-t^m≤m(1-t)`, and Euler beta integration. In particular `D=O_ℓ(n^-3)` **uniformly in q**, and `D=O_(q,ℓ)(n^-4)` when q,ℓ are fixed. For fixed q,ℓ, the exact asymptotic is `D~3qℓ/(32 n^4)`.

The **four-time phase** is consequently, for h integer,

\[
\boxed{
 e\!\left(h\Delta_q\Delta_\ell(16^nx)\right)
 =e\!\left(h\Delta_q\Delta_\ell U_n\right)
  \exp(2\pi i h D_{n;q,\ell}).}
\tag{PS15}
\]

This is an identity with **no arithmetic-target π constant in its right-hand side**. Source-supplied time differencing removes the enormous factor `(16^q-1)(16^ℓ-1)` from the unresolved integral, replacing it by an `O(n^-3)` correction uniform in the potentially enormous carrier-loop length q. It is a stronger source-to-real phase transport estimate than the generic one-time `O(n^-2)` tail, although it does not bound the rational phase itself.

For the prior #648 holonomy, fix `q=16^k`, `ℓ=2`, and original n≥k+1. Its exactly calibrated source operator yields the four-tap interferometer

\[
\boxed{V_{n+2,k}(h)\overline{V_{n,k}(h)}
=-e(h\Delta_q\Delta_2 U_n)\exp(2\pi i h D_{n;q,2}).}
\tag{PS16}
\]

The Poisson product (PS9) with four integer coefficients `(+1,-1,-1,+1)` and times `(n,n+ℓ,n+q,n+q+ℓ)` gives an **exact unbiased randomized realization of (PS15)**, using a finite a.s. number of coin rows. Its un-Rao–Blackwellized variance is

\[
\exp\left(\frac{(2\pi h)^2}{\lambda}
 \mathbb E[C\tau^{16n}(1-\tau^{8q})^2(1-\tau^{8\ell})^2]
\right)-1.
\tag{PS17}
\]

For fixed q,ℓ, this underlying square moment is asymptotic to `15 q²ℓ²/(512 n^6)`. Rao–Blackwell improves it to `45q²ℓ²/(4096 n^7)`. For moving/huge q the simpler uniform-q first-lag upper bound remains valid. The **sampling variance** is controlled; the average signed phase over large original-source shells is **not** proved small.

## PS-07 — Previous source-gauge claim corrected (EXACT COUNTERMODEL)

For any **integer-valued** sequence g(n) with g(0)=0 and g(n)=o(16^n), set

\[
\widetilde r(n)=r(n)+g(n)-16g(n-1),\quad
\widetilde U_0=0,\quad
\widetilde U_n=16\widetilde U_{n-1}+\widetilde r(n).
\]

Exact telescoping gives `tilde U_n=U_n+g(n)` and `tilde x=x+lim_(N→∞)16^-Ng(N)=x`, while the **true new source tail** is `tilde T_n=T_n-g(n)`. Thus `tilde U_n+tilde T_n=U_n+T_n` for all n. For #648's explicit `g(n)=2n²`, the prior statement "changes the real source/π target" is **REFUTED**: the source presentation changes, but the selected π/16 value and all completed circle phases do not. This mutation loses the canonical four-pole forcing's positivity and small forcing and changes the source's 2-adic holonomy, so it is **not** an authenticated alternative BBP source. Invariance of completed circle data under coboundaries is distinct from source provenance or preservation of the 2-adic phase operator.

This is a decisive ablation: the specific chirality from original forcing is **not** a gauge invariant of the target real number. A theorem converting it into real Fourier cancellation must use genuinely source-restricted hypotheses, not simply the target's value or the formal shape of the 2-adic basis.

## PS-08 — Verdict and falsifier (OPEN FRONTIER)

The new-to-project value here is an **exact, original-source, phase-sensitive connection** among (i) the screenshot's shared BBP Bernoulli coin, (ii) the complete finite-time zero-seeded rational orbit, (iii) the future Green Hankel Gram, (iv) the source-coupled Poisson product, and (v) the four-time chiral interferometer with a small nonvanishing signed correction. These are *reformulations and transport/variance theorems*, not Fourier cancellation or an academic-priority claim.

**Actual new arithmetic obligation:** For the original four-pole forcing, integer winding and true zero seed, prove a uniform-in-B signed all-shell restriction on the *rational* multi-time phases `e(h Δ_qΔ_2 U_n)` at a **fixed q=16^k**, strong enough to force `1-Re W_B(1)` bounded below, or all fixed harmonics tending to zero. (PS14) then transports a proved estimate to completed π with a uniform paid error. Existing finite experiments and any source-independent positive moment inequality cannot substitute for this arithmetic bound.

**Hostile failures required before promotion:** same-forcing coherent wrong seed (`s=-π/16`), rational periodic nonnormal seeds, #648's integer coboundary which preserves the real target but changes 2-adic chirality, forgotten common source threshold, independent-time mark resets, angle forgotten, and swapping `E` with `exp`/`floor`. The BBP input and the Euclidean circle normalization remain distinct types. No physical qubits/Higgs/Joules are asserted.

### Source provenance

- Original `observational_succ/duck_bbp.py`, `docs/PI_NORMALITY_FRONTIER.md`, `AGENTS.md` on Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`.
- SUCC draft [#646](https://github.com/femboy2112/SUCC/pull/646) (zero-source, real/2-adic source geometry), [#648](https://github.com/femboy2112/SUCC/pull/648) (the chiral holonomy and coboundary mutation), [#649](https://github.com/femboy2112/SUCC/pull/649) (source `A/B/C` coin and shared randomized-norm observables).
- Classical Poisson probability-generating functional: e.g. [Cambridge, *The probability generating functional*](https://doi.org/10.1017/S1446788700011095). The complex bounded-factor version follows from the elementary finite `Poisson(λ)` conditioning calculation above.
- Gamma/Beta endpoint integral: [NIST DLMF §5.12](https://dlmf.nist.gov/5.12). The `r`/`T` source status and BBP identification remain imported; original Bailey–Crandall normality program was conditional: [Bailey and Crandall (2001)](https://doi.org/10.1080/10586458.2001.10504441).

## PS-09 — One finite-expected-cost stochastic probe for the COMPLETE normality energy (EXACT INSTRUMENT; DECAY OPEN)

SUCC draft #644 already defines a **positive full-support** Oily frequency law `q_h=(h+1)/(3·2^h)`, h≥1, with `Σq_h=1`. Its first and second moments are **finite and exact**:

\[
\boxed{\mathbb E_q H=\frac83,\quad\mathbb E_q H^2=\frac{32}3.}\tag{PS18}
\]

The target complete energy is `\mathcal C_B=Σ_(h≥1)q_h |W_B(h)|²`, and the classical Weyl criterion makes `\mathcal C_B→0` **equivalent to** π base-16 normality. No decay is established. We can nevertheless give this *entire infinite harmonic sum* an **exact finite-almost-surely random-product readout** without supplying π as an arithmetic input:

1. Sample one harmonic H according to q. Pick base intensity λ₀>0 and choose the harmonic-dependent intensity `λ_H=λ₀H²`.
2. Conditional on H, draw **two independent whole-shell replicas** A,B of the Poisson-marked BBP source phase (PS9), each sharing its one Poisson mark field across every n in the requested shell, and each using the **same H** but fresh source rows across replicas.
3. For replica a, write `\widehat W_B^{(a)}(H)=B^-1Σ_(n=B)^(2B-1)\mathscr Z_{n,H}^{(a)}`. Return the *real signed* product `Z_B=Re(\widehat W_B^{(A)}(H)\overline{\widehat W_B^{(B)}(H)})`.

Conditional independence across replicas, coupled with exact unbiasedness inside each replica, gives

\[
\boxed{\mathbb E Z_B=\sum_{h\ge1}q_h|W_B(h)|^2=\mathcal C_B.}\tag{PS19}
\]

The cost is finite in expectation **despite all harmonics being accessible**:

\[
\boxed{\mathbb E[N_A+N_B]
=2\lambda_0\mathbb E_q H^2=\frac{64}{3}\lambda_0.}\tag{PS20}
\]

The harmonic-normalized source variance is uniformly bounded: let `δ_B=exp((2π)² T_(2B)/λ₀)-1`. For **every** h≥1,

\[
\boxed{0\le\mathbb E|\widehat W_B(h)|^2-|W_B(h)|^2\le\delta_B,\quad
\mathbb E[Z_B^2]\le(1+\delta_B)^2.}\tag{PS21}
\]

**Proof:** In one replica, *the same Poisson marked rows occur at all shell times*. Direct two-time generating-functional multiplication gives

\[
\boxed{\mathbb E[\mathscr Z_{n,h}\overline{\mathscr Z_{m,h}}]
=e(h(z_n-z_m))\exp\left(\frac{(2\pi h)^2}{\lambda_h}T_{n+m}\right).}\tag{PS22}
\]

The extra factor is source-selected and depends on the **same original Green Hankel kernel**. Its excess over `|W_B(h)|²` is exactly a nonnegative variance. Since `n+m≥2B`, `0<T_(n+m)≤T_(2B)`, and `λ_h=λ₀h²`, its absolute value is ≤δ_B. With two independent replicas, `|Z_B|²≤|\widehat W^{(A)}|²|\widehat W^{(B)}|²`; conditional expectation separates, giving (PS21). This is uniform in h; a fixed λ independent of h would leave exponential `h²` second moments and **could not** justify summing over q_h. The `h²` intensity is essential to the declared all-frequency finite-variance contract.

Because `T_(2B)=O(B^-2)` for the Bernoulli coin and `O(B^-3)` for the Rao–Blackwellized mark squared norm, the noise term δ_B vanishes for fixed base λ₀. The observable `Z_B` itself can be negative or greater than 1 on some trials: only **its expectation** is the nonnegative normality energy. The procedure does **not** prove that this expectation tends to zero. It establishes calibrated, all-harmonic **target access**, including its exact stochastic cost and the source's nontrivial two-time correlations.

The finite executable smoke test of this hierarchy uses the original rational U_n and π-free coin construction, with ordinary double-precision circle characters; it is not a rigorous arbitrary-h computational certificate. The exact (PS18–22) proofs do not depend on floating-point runs.
