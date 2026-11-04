# Operation ANALYTIC EXILE — finite counterexamples, Gamma completion, and selected Fourier obstruction visibility

**November 4, 2026. Research-only paper proofs + exact original-source arithmetic.** Additive descendant of draft PR #493 (`de5e7cef12453e7efa8f41488d09d2e8ace64235`) over merged main `a673ec95dfac4ef6a61c60222be8b615fd08535d`. Preregistration was committed first at `be35e9935a01f714f466b9bed8f73c1f03e48dd6`. No academic priority claim for Weyl, normal numbers, Fourier/Fejér, Ward telescoping, Green tails or classical Champernowne construction. This file preserves the original-source and tool-closure contracts and does NOT prove π normality.

## The research question, faithfully distinguished

Hypothesis: perhaps every falsifying configuration that the observer can construct is forced into an analytic channel truncated by its finite observation, and the completed global theory cancels that channel. There are three different mathematical claims to keep apart:

1. **Physical/source completion residual** `T_n`: the authentic BBP Green tail between the finite rational source phase and the completed π orbit. Does a possible *fixed-frequency π-nonnormality witness* live only in `T_n`? **NO, ruled out by a convergent error bound.**
2. **Observation/Fourier truncation residual** beyond frequency `H_A`: can all of the current-energy obstruction be exiled to high unobserved Fourier modes? **NO if `H_A=q_A²` in the sinc-weighted observation; the total high-mode energy is bounded independently of A.**
3. **Finite counterexample models** approximating a global source under an unbounded, nonuniform, dynamical map: each finite model might be nonnormal while the limit is normal. **YES, this can happen, because the two limits generally do not commute.** It establishes a proof-access danger, not an identity about π's normality.

All three are *observable-relative* statements. For moving frequencies `h_A` comparable to `A²`, even a source tail `O(A^-2)` is not uniformly invisible after multiplication by `h_A`.

## Source contract and named extant results

For every `n>=1` the IMMUTABLE original source is

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Let `α=π/16`, `X_n=16^n α`, and `T_n=X_n-U_n`. The source BBP integral / original SUCC Gamma source proof gives

\[
 0<T_n<\frac1{(8n+1)(8n+2)}<\frac1{64n²}.
\]

The mathematical statement `X_n=U_n+T_n` is an all-n identity from the original full BBP expansion, not a π digit input. The original source moment positivity provides `0<r(n+1)<15/((8n+1)(8n+2))`, since `r(n+1)=∫_0^1t^(8n)(1-t)(t²+2)(t²+2t+2)dt` and both factors are bounded by 3 and 5.

Define `e(x)=exp(2πix)`, `S_N^Y(h)=∑_(n=1)^N e(hY_n)` and epoch mean `c_A^Y(h)=A^-1∑_(n=A)^(2A-1)e(hY_n)` for integer `h≠0`. For rational-source calculations the program evaluates `U_n mod1` with exact `Fraction`, or independently with a common odd denominator modular orbit. The unwrapped state remains separately source-typed: `U_n mod1` is NOT a legal substitute for the 2-adic unwrapped value.

## AE-01 — physical Gamma tail cannot carry a fixed-h nonnormality witness (DISCLOSED / inherited + sharpened explicit constant)

The chord inequality and source tail give, for ALL positive N and fixed integer h,

\[
\begin{aligned}
|S_N^X(h)-S_N^U(h)|
&\le2π|h|\sum_{n=1}^NT_n\\
&<\frac{π|h|}{32}\sum_{n=1}^\infty\frac1{n²}
=\frac{π^3}{192}|h|.
\end{aligned}
\]

Thus `S_N^X(h)/N-S_N^U(h)/N=O_h(N^-1)`, and the limsup of the **modulus** of the normalized Weyl sum is identical for X and U. Original π is base-16 normal iff the literal zero-seeded rational source has vanishing Weyl mean for every fixed nonzero h (the already-established SGO/#293 and #476 equivalence).

On every integer epoch A, `sum_(A<=n<2A) T_n < A/(64A²)=1/(64A)`. Consequently,

\[
\boxed{|c_A^X(h)-c_A^U(h)|<\frac{π|h|}{32A²}.}\tag{AE-1}
\]

Using `||a|²-|b|²|<=2|a-b|` for |a|,|b|<=1, sum |h|<=H gives the moving-band but explicitly bounded transfer

\[
\boxed{\sum_{1\le|h|\le H}\big||c_A^X(h)|²-|c_A^U(h)|²\big|
<\frac{π H(H+1)}{16A²}.}\tag{AE-2}
\]

For H≈(log A)² this tends to zero, so an obstruction visible at such frequencies cannot be concealed in `T_n`. This is a NEGATIVE theorem against the proposed physical-tail exile strategy, not a proof that the rational source mixes.

## AE-02 — weighted Fourier observation has a provably negligible analytic truncation tail (DISCLOSED / sharpened type)

From the merged selected-current front, for integer `q>=2` and real original phase cloud,

\[
\mathcal J_{A,q}=1+\sum_{h\ne0}w_q(h)|c_A^U(h)|²,\qquad
w_q(h)=\left(\frac{\sin(π h/q)}{π h/q}\right)^2.
\]

Let `W_(A,q,H)=∑_(1<=|h|<=H) w_q(h)|c_A^U(h)|²`. Then for ALL A,q,H,

\[
\boxed{0\le(\mathcal J_{A,q}-1)-W_{A,q,H}\le\frac{2q²}{π²H}.}\tag{AE-3}
\]

This follows because `w_q(h)<=q²/(π²h²)`, `|c_A(h)|<=1`, and `sum_(h>H)1/h²<=1/H`. In particular, with **H=⌈q²⌉**, the tail is at most `2/π²<2/9`, uniformly in A. If `q_A=16^(K_A)/2`, with `K_A=floor(log_16 log A)->infinity`, then

\[
\boxed{\mathcal J_{A,q_A}=o(K_A)\ \Longleftrightarrow\ W_{A,q_A,\lceil q_A²\rceil}=o(K_A).}\tag{AE-4}
\]

This equivalence concerns the **WEIGHTED** Fourier band. It does NOT assert equivalence for an *unweighted* band: the sinc factor is ZERO for each nonzero h divisible by q. PR #491 gives an explicit equally spaced cloud counterexample to the unweighted converse. The further implication `J=o(K) ⇒ π normal` uses the established source-specific #476 Fejér/Ward theorem, NOT this algebra alone.

## AE-03 — an original-source low-frequency counterexample becomes a finite-frequency ladder (DISCLOSED / source-derived estimate)

The original AFFINE source satisfies `U_(n+1)=16U_n+r(n+1)`. For integer frequency k,

\[
e(16kU_n)=e(kU_(n+1))e(-kr(n+1)).
\]

Summing over n∈[A,2A) and applying a shifted endpoint telescope,

\[
|c_A^U(16k)-c_A^U(k)|
\le\frac2A+\frac{2π|k|}{A}\sum_{n=A}^{2A-1}r(n+1)
<\frac2A+\frac{15π|k|}{32A²},
\]

since `r(n+1)<15/(64A²)` for every n in the epoch. Iterate over k=h,16h,...,16^(j-1)h:

\[
\boxed{|c_A^U(16^j h)-c_A^U(h)|
\le\frac{2j}{A}+\frac{π|h|(16^j-1)}{32A²}.}\tag{AE-5}
\]

Fix a nonzero INTEGER h and epsilon>0. For a chosen q with q>=2|h|, let

\[
L=\left\lfloor\log_{16}\frac q{2|h|}\right\rfloor.
\]

If an actual independent source observation shows `|c_A^U(h)|>=epsilon`, and the right side of AE-5 at j=L is <epsilon/2, then for every j=0,...,L,

\[
|c_A^U(16^j h)|\ge epsilon/2,
\qquad w_q(16^j h)\ge\frac4{π²}.
\]

The frequencies `±16^j h` are pairwise distinct (h≠0). Therefore their positive contributions to the triangular energy prove the **quantitative obstruction visibility**

\[
\boxed{\mathcal J_{A,q}-1\ge\frac{2epsilon²}{π²}(L+1).}\tag{AE-6}
\]

At the SUCC schedule `q=q_A=16^K/2` with `K≈log_16 log A`, we have `L=K-O_h(1)` and the AE-5 error tends to zero. Hence **IF** a fixed-frequency h has limsup epoch magnitude bounded below along infinitely many large dyadic A, the energy is Ω(K_A) along those A: a persistent low-mode obstruction **cannot disappear into the high-frequency tail of the proof's observation**.

***Important quantifier firewall.*** AE-6 is conditional on an independently witnessed (or hypothetically assumed) lower bound on the ORIGINAL source `|c_A^U(h)|`; it does NOT establish that such a witness exists for π, does not prove normality, and does not claim that every full-prefix obstruction automatically appears on all dyadic full blocks without an extra argument. It is a transparent quantitative specialization of SUCC's existing Ward frequency-ladder approach, not independent scholarly novelty.

## AE-04 — finite nonnormal truncations can converge to a normal completed source (CLASSICAL decisive counterexample)

Let `C_16` be the classical base-16 Champernowne number: concatenate `1,2,3,...` represented in base16 after the radix point. Its base-16 normality is classical (Champernowne 1933). Let `C_M=floor(16^M C_16)/16^M` be its first M **hexadecimal digit** prefix, a terminating rational. For every fixed M and n>=M, `{16^n C_M}=0`, so

\[
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}e(16^n C_M)=1.
\]

For every FIXED finite N, continuity of the finite sum under `C_M→C_16` gives the true normal orbit sample as M→infinity; by the classical Weyl criterion its normalized mean tends to zero as N→infinity. Hence the two honest iterated limits DO NOT commute:

\[
\boxed{\lim_{M\to\infty}\lim_{N\to\infty}c_N(1,C_M)=1,
\qquad\lim_{N\to\infty}\lim_{M\to\infty}c_N(1,C_M)=0.}\tag{AE-7}
\]

This is a theorem about a **KNOWN normal** completed source, deliberately not π. It refutes the inference that “the false behavior of all finite truncations disappears at infinity, therefore the limit's normality can be proved without a uniform-in-N bound.” Normality is not continuous under ordinary real approximation. It illustrates the user's finite-world vs analytic-completion hypothesis faithfully, while showing the missing uniformity requirement.

For authentic BBP α_M=U_M/16^M (NOT the terminating-hexadecimal prefix above), the exactly synchronized finite rational source satisfies

\[
16^n\alpha=16^n\alpha_M+16^{n-M}T_M.
\]

Choose M=2A and sample n in [A,2A). Summing the genuine source `T_M<B(M)` through the geometric weights gives

\[
\boxed{\left|c_A^X(h)-A^{-1}\sum_{n=A}^{2A-1}e(h16^n\alpha_{2A})\right|
<\frac{2π|h|B(2A)}{15A}.}\tag{AE-8}
\]

This is O(|h|/A³), **with the rational prefix chosen in synchronization with the requested horizon**. It does NOT imply the finite rational prefix phase mean itself tends to zero; its selected signed statistics are the remaining hard arithmetic problem.

## AE-05 — where Euler–Mascheroni actually enters (INHERITED exact offdiagonal source normalization)

From the prior Gaussian/real quadratic source splitting (#481, #485), for integer h,k and λ=k−h,

\[
 hU_n^H+kU_n^G=16^n\theta_{h,k}-\frac{\lambda}{32n}+\eta_n,
\qquad |\eta_n|<\frac{|k|+|\lambda|}{64n²}.
\]

The cumulative phase error has `−λ(H_N)/32 = −λ(logN+gamma)/32+o(1)`, while the corrected residual `η_n` is **absolutely summable**. For the actual π diagonal h=k, λ=0 identically: the 1/n Euler-Mascheroni slip cancels BEFORE taking a limit. This **explains the source normalization and its boundary**, but cannot create the missing original signed Weyl saving. Any proposed analytic-exile proof must derive an additional source-selected signed inequality not already contained in these tail comparisons.

## AE-06 — observer/toolkit interpretation and next discriminating instrument

- In SUCC's preloaded line+circle experiment, supply each carrier and its internal operations, but DO NOT preload the bridge or Haar distribution. The original rational source and zero seed may be supplied as source-authenticated generators.
- An analytic remainder may be irrelevant for a declared Lipschitz/fixed-frequency query but relevant for a moving-band or discontinuous cylinder query. Record the observation **resolution**, frequency cutoff and quantitative modulus of continuity.
- If an observer hopes to prove all countermodels are exiled into a disappearing remainder, the proof must quantify over ALL surviving source-compatible rivals and supply a UNIFORM bound for the actual target observable. Pointwise-in-model finite certificates do not suffice.
- PR #493's finite bridge impostors, Busy Beaver falsifier delays and toolkit-nonseparating ghosts are DIFFERENT obstructions. None should be relabeled π nonnormality evidence.
- The immediate honest proof target remains `J_(A,q_A)=o(K_A)` for the UNIQUE original source; by AE-4 the **sinc-weighted** band up to `q_A²` is an equivalent diagnostic target. By AE-6 a fixed low-h failure forces a frequency ladder of positive energy, rather than vanishing inside the omitted analytic high-mode tail. **No claim that the needed energy saving has been proved.**

## AE-07 — Gamma-regularized Abel boundary is an **equivalent** Weyl/normality gate (CLASSICAL bounded Tauberian + original source)

For each fixed nonzero integer h, define the actual SOURCE-SELECTED Fourier character sequence, not an ensemble:

\[
a_n(h)=e(hU_{n+1}),\quad |a_n(h)|=1,\quad
F_h(z)=\sum_{n=0}^{\infty}a_n(h)z^n\quad(|z|<1).
\]

This converges on the unit disc by boundedness, with no normality assumption. Let the *Abel boundary observation* be

\[
\boxed{\mathcal A_h(\rho)=(1-\rho)F_h(\rho),\qquad 0<\rho<1.}\tag{AE-9}
\]

The **classical bounded-sequence Abel-to-Cesàro Tauberian theorem** states: if a complex sequence \(a_n\) is bounded and its Abel means \((1-\rho)\sum a_n\rho^n\) converge to L as \(\rho\uparrow1\), then its Cesàro means \(N^{-1}\sum_{n<N}a_n\) converge to the same L. The converse is classical Frobenius/Abel. For complex values, apply the real-vector formulation to real and imaginary parts. The REQUIRED Tauberian hypothesis \(|a_n|\le1\) is automatically satisfied here, without an observer probability assumption. Primary mathematical sources: Mario Ponce (2012), *Hyperbolization of cocycles by isometries of the euclidean space*, Theorems 10–11, https://mat.uc.cl/prepublicaciones/download/36 ; and L. A. Rubel (1960), *Maximal Means and Tauberian Theorems*, Pacific Journal of Mathematics 10(3), corollary to Theorem 3.1, https://msp.org/pjm/1960/10-3/pjm-v10-n3-p24-p.pdf . These theorems are classical imports, not SUCC discoveries.

Together with SUCC's already established original-source Weyl↔π normality bridge,

\[
\boxed{\pi\text{ normal in base 16}\quad\Longleftrightarrow\quad
\forall h\in\mathbb Z\setminus\{0\},\ \lim_{\rho\uparrow1}(1-\rho)F_h(\rho)=0.}\tag{AE-10}
\]

This is a **newly articulated analytic frontier**, not a proof of the boundary limit. A false hypothesis could generate a *nonzero* boundary residue or nonconvergent order-\((1-\rho)^{-1}\) behavior; there is no promise that every obstruction is a literal simple pole.

The original completed orbit \(X_n=U_n+T_n\) has its own Fourier series \(F_h^X\). By AE-01,

\[
\sum_{n\ge1}|e(hX_n)-e(hU_n)|\le\frac{\pi^3}{192}|h|.
\]

Therefore the difference \(F_h^X-F_h^U\) has **absolutely summable Taylor coefficients**: it converges uniformly on the CLOSED unit disc, and

\[
\boxed{\lim_{\rho\uparrow1}(1-\rho)(F_h^X(\rho)-F_h^U(\rho))=0.}\tag{AE-11}
\]

This is the exact analytic-exile result that the genuine BBP Gamma completion **does** pay: the omitted Green tail is in the Wiener algebra and has zero order-one Abel boundary residue. Hence it cannot hide a surviving fixed-h Weyl/Abel counterexample. That counterexample, if there is one, resides in the selected rational-source \(F_h^U\) boundary—not in an already bounded correction.

## AE-08 — the analytic observer's sampling kernel is EXACTLY negative-binomial, converging to Gamma(2) (CLASSICAL, exact finite-algebra specialization)

Let \(S_n(h)=\sum_{k=0}^{n}a_k(h)\) and \(c_{n+1}(h)=S_n(h)/(n+1)\). Summation by parts holds as an **exact identity for every** \(0<\rho<1\):

\[
\begin{aligned}
\mathcal A_h(\rho)
&=(1-\rho)^2\sum_{n\ge0}S_n(h)\rho^n\\
&=\boxed{\sum_{n\ge0}(n+1)(1-\rho)^2\rho^n\,c_{n+1}(h).}
\end{aligned}\tag{AE-12}
\]

The nonnegative weights \(p_\rho(n)=(n+1)(1-\rho)^2\rho^n\) sum to one, exactly. They form a **negative-binomial shape-two** law. This is a *mathematical averaging operator on the actual selected source's prefix means*, not a replacement of the physical source by independent random samples.

Put \(\varepsilon=1-\rho\), let \(N_\rho\) have these prescribed weights, and set \(Y_\rho=\varepsilon(N_\rho+1)\). Its Laplace transform is exactly

\[
\mathbb E e^{-sY_\rho}
=\frac{\varepsilon^2 e^{-s\varepsilon}}{[1-(1-\varepsilon)e^{-s\varepsilon}]^2}
\longrightarrow\frac1{(1+s)^2}\quad(s\ge0).
\]

Thus \(Y_\rho\) converges in distribution to a **Gamma(shape=2, rate=1)** law. Its logarithmic mean is

\[
\boxed{\mathbb E_{Y\sim\Gamma(2,1)}\log Y=\psi(2)=1-\gamma.}\tag{AE-13}
\]

**This is the actual load-bearing Euler–Mascheroni/Gamma interface.** The same \(1-\gamma\) appears in SUCC's authentic BBP endpoint Beta→Gamma(2) zoom. It is NOT a new π-normality estimate: the Gamma(2) law is the universal time-smoothing kernel from Abel/Cesàro, whereas SUCC's Beta kernel is source-specific. Their shared shape provides a legitimate comparison/transport question, not a source identity.

On logarithmic scales the Gamma(2) smoothing has Mellin/Fourier multiplier

\[
\int_0^\infty y^{1+i\xi}e^{-y}\,dy=\Gamma(2+i\xi),
\]

which has no zeros. This explains why a classical Tauberian inverse exists under the declared boundedness/regularity conditions, but it does NOT establish the missing original-source boundary limit \(\mathcal A_h(\rho)\to0\). Additional assumptions are not to be imported tacitly into the selected BBP orbit.

## AE-09 — a perfect *analytic-boundary ghost* can hide from every finite coefficient window (EXACT negative control)

For any integer \(M\ge0\), put

\[
G_M(z)=\frac{z^M}{1-z}=\sum_{n\ge M}z^n,\qquad |z|<1.
\]

The first M coefficients of \(G_M\) are identically zero. As \(M\to\infty\), \(G_M\to0\) uniformly on every compact subdisk \(|z|\le r_0<1\). Yet for EVERY FIXED M,

\[
\boxed{\lim_{\rho\uparrow1}(1-\rho)G_M(\rho)=1.}\tag{AE-14}
\]

There is even a **unit-modulus phase-sequence** version: two streams \(a_n=1\) for all n and \(b_n=1\) before M, \(b_n=-1\) at/after M agree EXACTLY under the first M source-free observations and individually have |a_n|=|b_n|=1. Their analytic character difference is \(-2z^M/(1-z)\), whose interior limit vanishes as M→infinity but whose normalized boundary residue remains \(-2\) at fixed M. These are SOURCE-MUTATED illustrative sequences, not both lawful original BBP orbits.

**Interpretation:** a growing-haystack impostor can move its boundary obstruction beyond every finite analytic Taylor cutoff. The identity theorem does not repair this: each stage is a DIFFERENT analytic function, and its pointwise/compact convergence does not control the singular boundary. A valid analytic-exile proof requires a **UNIFORM source-derived boundary modulus** (or the exact bounded Tauberian limit), not merely vanishing finite coefficients or ordinary holomorphy.

Analytic growth comparison: the coherent constant stream has \(1/(1-z)\) and a nonzero normalized boundary; a harmonic correction has \(-\log(1-z)\), so \((1-z)\log(1-z)\to0\); and a summable \(O(n^{-2})\) correction has bounded generating function, hence vanishing normalized boundary. Euler's \(\gamma\) enters via the harmonic and Gamma(2) logarithmic normalization, but these standard facts do NOT prohibit the **selected** original Fourier series from having order-one boundary behavior. The open source test is precisely AE-10.

## References and authority

- SUCC merged main: `research/2026-10-25/SIGNED_GAMMA_BBP_GREEN_COHERENCE.md`, `research/2026-11-03/selected_current_front/PROOFS.md`, and draft #491 `PROOFS.md` (unweighted-band false converse and corrected Ward transport).
- Classical B-spline / triangle/sinc Fourier, Weyl normality criterion and base-16 Champernowne normality. For Champernowne overview see Clay Mathematics Institute, *Normal Numbers and Randomness* (2006), https://www.claymath.org/library/annual_report/ar2006/06report_normalnumbers.pdf .
- All finite source input is exact Fraction or independent integer modular data. No π digits, no computation of busy-beaver values, no RH/signed-Weil claim. The local tests certify finite algebra, not the all-horizon estimates, which are proved on paper here where marked.

## AE-10 — source-forced analytic frequency renormalization (DISCLOSED, but invariant boundary is not Haar)

For the full source-character series starting at the original ZERO boundary,

\[
G_h(z)=\sum_{n\ge0}e(hU_n)z^n\quad (|z|<1),\qquad U_0=0,
\]

the genuine original recurrence yields the exact functional equation

\[
\boxed{G_h(z)=1+zG_{16h}(z)+zE_h(z),}\tag{AE-15}
\]

where

\[
E_h(z)=\sum_{n\ge0} e(16hU_n)\big(e(hr(n+1))-1\big)z^n.
\]

The source error has ABSOLUTELY summable coefficients: `r(1)=47/15`, and for n>=2, `r(n)<15/[64(n−1)²]`. Thus `∑_(n>=1)r(n)<47/15+15/32<4` and, for every |z|<=1,

\[
\boxed{|E_h(z)|\le2π|h|\sum_{n\ge1}r(n)<8π|h|.}\tag{AE-16}
\]

This genuinely uses the original positive four-pole source, not an ensemble over other paths. Put \(A_h(z)=(1-z)G_h(z)\). The analytic recurrence becomes

\[
\boxed{A_h(z)=z A_{16h}(z)+(1-z)\,[1+zE_h(z)].}\tag{AE-17}
\]

For every FIXED h, the source-dependent correction vanishes in the Abel boundary limit as `z↑1`. Hence any existing limits obey `lim A_h=lim A_(16h)`; this is the exact analytic analogue of the source Ward frequency ladder. It does **not** force zero: a coherent periodic circle source has nonzero Fourier boundary limits invariant along its 16-frequency orbit. The original zero-seed term also contributes only `(1-z)` at the boundary and is not itself a normality theorem.

**Potential actual lamp:** prove a source-authenticated *uniform Rajchman condition* for the Fourier coefficients of EVERY Abel cluster measure of the original zero-seeded source: the coefficients tend to zero as |h|→∞. Any such cluster is T_16-invariant by the original `r(n)→0` law, and a T_16-invariant Rajchman probability measure must be Haar, because `\hat\mu(h)=\hat\mu(16^j h)→0` as j→∞. This would supply the original Weyl/Abel boundary zero. The Rajchman premise is **UNVERIFIED** and cannot be inserted as an observer oracle or inferred from the old prime Galois-average data. This is a candidate theorem-producing way to attack the analytic boundary rather than the completed Green tail.
