# Operation ZAK–JACKSON BAND: a source-canonical finite/analytic alias-to-prefix theorem

**Research date:** 2026-10-31 (New York). **Parent:** `research/seeded-zak-arithmetic-seam-2026-10-31`, original head `6a23d0735f30c68200a93ff4725c54c0cc8b5975`, stacked on Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`. This is an *additive mathematical laboratory*, not a rewrite of imported proof/production code or original BBP. π base-16 normality and RH remain **OPEN**.

The statements labeled **CLASSICAL** use standard finite Fourier, approximate-identity and first-derivative oscillatory integration arguments. **PROVED PAPER / source-scoped** means a complete derivation is supplied here under declared hypotheses, checked by finite exact implementations; it does **not** assert external review, novelty priority or Lean kernel proof. Distinct original-source facts are cited explicitly below.

## 0. The exact source; no source substitution

For all integer `n>=1`, retain all FOUR ORIGINAL SIGNED POLES:

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
 \quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Use the inherited strictly positive original Green tail for `x>=0`:

\[
 T(x)=\sum_{j\ge1}16^{-j}r(x+j)
 =\int_0^1 \frac{t^{8x}P(t)}{16-t^8}\,dt,\qquad
 P(t)=(1-t)(t^2+2)(t^2+2t+2).
\tag{J0}
\]

It obeys `16T(x)-T(x+1)=r(x+1)` and `alpha=T(0)=pi/16`; hence, for the authentic source and literal zero boundary, `U_n=16^n alpha-T(n)`. These formulas are **inherited**, not independent new discoveries. Define the canonical continuous lift for arbitrary **declared** `q in [3/16,1/4]`:

\[
 U_q(x)=q16^x-T(x). \tag{J1}
\]

The one original source with `U_0=0` is `q=alpha`; `q=1/5` is a strictly **changed, nonzero initial seed** of the SAME forcing and is the hostile coherent orbit. The interval restriction is used only to derive uniform constants and includes both cases. The periodic-`Q` interpolation family from parent PR #438 is a separate possible lift and is **not silently treated as canonical**.

Let `e(u)=exp(2 pi i u)`. Choose once and for all a *smooth, real, even plateau bump* `psi` with `0<=psi<=1`, `psi(s)=1` for `|s|<=1/8`, `psi(s)=0` for `|s|>=1/4`, and nonincreasing for `s>=0`; thus `||psi'||_1=2`. Define

\[
 g_{N,q,h}(x)=\sum_{n=1}^N\psi(x-n)e(hU_q(x)),\qquad
 I_{N,\ell}(q,h)=\int_{\mathbb R}g_{N,q,h}(x)e(-\ell x)\,dx.\tag{J2}
\]

The compactly supported smooth `g` yields an absolutely convergent Fourier alias series at each finite horizon:

\[
 S_N(q,h):=\sum_{n=1}^N e(hU_q(n))=\sum_{\ell\in\mathbb Z}I_{N,\ell}(q,h).
\tag{J3}
\]

That is the exact Zak/Poisson seam of PRs #437/#438. It is not itself signed cancellation.

## 1. A FINITE, nonnegative-frequency, EXACT flat-top filter (ZJB-01, CLASSICAL / derived)

Fix an integer `L>=16`, and set

\[
 D_L(t)=\sum_{j=0}^{L-1}e(jt),\quad
 H_L(t)=\frac{|D_L(t)|^4}{L^4},\quad
 \mathcal D_{3L}(t)=\sum_{k=-3L}^{3L}e(kt),\quad
 \boxed{K_L(t)=H_L(t)\,\mathcal D_{3L}(t).}\tag{J4}
\]

The normalized fourth power `H_L` has Fourier coefficients `b_j>=0`, supported on `|j|<=2L-2`, with `sum_j b_j=H_L(0)=1`. Explicitly, if `t_j=(L-|j|)_+`, then

\[
 L^4 b_j=\sum_{v\in\mathbb Z} t_v t_{j-v}.\tag{J5}
\]

The `K_L` Fourier coefficients are

\[
 c_{L,\ell}=\sum_{k=-3L}^{3L}b_{\ell-k}.
\]

They have exact **finite** rational certificates:

\[
 \boxed{0\le c_{L,\ell}\le1,\quad
 c_{L,\ell}=1\ \text{for}\ |\ell|\le L+2,\quad
 c_{L,\ell}=0\ \text{for}\ |\ell|>5L-2.}\tag{J6}
\]

Moreover `c_(L,0)=int_0^1 K_L=1`, and
`sum_ell c_(L,ell)=K_L(0)=6L+1`. **The real-space kernel `K_L` need not be nonnegative:** only its Fourier coefficients are. Mistaking this for a probability kernel is forbidden; our proofs use absolute integral bounds.

The exact Dirichlet fourth-moment normalizer is

\[
 \int_0^1|D_L(t)|^4\,dt
 =\sum_{j=-(L-1)}^{L-1}(L-|j|)^2
 =\frac{L(2L^2+1)}3.
\tag{J7}
\]

This formula is not needed to normalize `H_L`, but is a separate Pascal/path-convolution check. The code verifies J5 in two independent ways: triangular coefficient convolution and direct four-index enumeration (all `16^4` paths at `L=16`).

### A stronger idealized exact demultiplexer (ZJB-02, finite algebra)

On a **toy linearized cell carrier** (not the original nonlinear BBP analytic lift), prescribe cell characters `f_n(s)=z_n e(16^n s)` for arbitrary `|z_n|=1`, with `s` on the unit circle and `n>=1`. Its Fourier coefficient is supported exactly at `ell=16^n`. Set `L=16^M`, `1<=M<=N`. Then from J6:

\[
 \boxed{\sum_{n=1}^N z_n c_{16^M,16^n}=\sum_{n=1}^M z_n.}\tag{J8}
\]

At `n<=M`, `16^n<=L+2`, while at `n>=M+1`, `16^n>=16L>5L-2`. This is **exact finite Pascal/Fourier alias selection**, not a proof about the original analytic phase. The next theorem establishes a *uniform error* for the actual original source.

## 2. Universal kernel concentration inequalities (ZJB-03, elementary)

For `|t|<=1/2`, `L>=16`, elementary sine bounds give

\[
 |D_L(t)|\le\min(L,(2|t|)^{-1}),\quad
 |\mathcal D_{3L}(t)|\le\min(6L+1,(2|t|)^{-1}).
\]

Consequently, with `K_L` extended 1-periodically,

\[
 |K_L(t)|\le
 \begin{cases}
 7L,& |t|\le1/L,\\
 (32L^4|t|^5)^{-1},&1/L<|t|\le1/2.
 \end{cases}\tag{J9}
\]

Integrate these two explicit envelopes, obtaining

\[
 \boxed{\int_{-1/2}^{1/2}|K_L(t)|dt<15,\quad
 \int_{-1/2}^{1/2}|tK_L(t)|dt<8/L,\quad
 \int_{|t|>1/8}^{1/2}|K_L(t)|dt<64/L^4.}\tag{J10}
\]

For example, the first moment is bounded by `7/L+1/(48L)<8/L`; the outside-plateau tail is `4080/(64 L^4)<64/L^4`. These are uniform for every `L>=16` and are **not** fitted to BBP output. In particular, because `psi=1` on `[-1/8,1/8]`,

\[
 \left|\int_{-1/2}^{1/2} \psi(t)K_L(t)dt-1\right|<64/L^4.\tag{J11}
\]

## 3. Certified original-source analytic derivatives (ZJB-04, source specialization)

`P(t)/(16-t^8)<=1-t` for `0<t<1`: indeed `P/(1-t)=(t^2+2)(t^2+2t+2)<=15`, whereas `16-t^8>=15`. Differentiating the **convergent original source integral** (J0) therefore gives, for `x>=3/4`,

\[
 0<-T'(x)<\frac8{(8x+1)^2}<1,\qquad
 0<T''(x)<\frac{128}{(8x+1)^3}<1.\tag{J12}
\]

For every `q in [3/16,1/4]` and `x>=3/4`,

\[
 \boxed{q(\log16)16^x<U_q'(x)<q(\log16)16^x+1,\quad U_q''(x)>0.}\tag{J13}
\]

Indeed `U_q''=q(log16)^2 16^x-T''`, whose first term exceeds 10 even at the smallest allowed q,x, while `T''<1`. The elementary strict rational bounds `8/3<log16<3` follow from the positive atanh series for log2, and `3<pi<22/7` are classical. All subsequent explicit constants can be checked using these rational comparisons without evaluating pi or log16 numerically.

## 4. The main theorem: a FINITE ALIAS BAND retrieves the actual arithmetic prefix (ZJB-05, PROVED PAPER)

For an integer `h!=0`, integers `N>=M>=1`, and `L=16^M`, define the **source-typed flat-top alias band**

\[
 \boxed{\mathcal B_{N,M}(q,h)
 :=\sum_{|\ell|\le5L-2}c_{L,\ell}I_{N,\ell}(q,h)
 =\int_\mathbb R g_{N,q,h}(x)K_L(x)\,dx.}\tag{J14}
\]

**Theorem.** For every original forcing `r`, canonical constant-q lift with `3/16<=q<=1/4`, fixed integer `h!=0`, and every `N>=M>=1`,

\[
 \boxed{\left|\mathcal B_{N,M}(q,h)-\sum_{n=1}^M e(hU_q(n))\right|<99|h|.}\tag{J15}
\]

The right-hand side depends on neither M nor N. This is an **all-horizon analytic transport theorem**; it is *not* `o(M)` signed cancellation or a π-normality proof.

**Proof, with exact nonasymptotic budget.** Partition J14 into integer cells `n`. For early `1<=n<=M`, subtract `e(hU_q(n))` using `int K_L=1`. Apply `|e(x)-e(y)|<=2pi|x-y|`, J11, J13, and the first moment J10:

\[
 \sum_{n=1}^M|\text{cell}_n-e(hU_q(n))|
 <\frac{16\pi|h|}{L}
 \sum_{n=1}^M(q\log16\,16^{n+1/4}+1)+\frac{64M}{L^4}.
\]

Since `L=16^M`, `16^(1/4)=2`, `sum_(n=1)^M16^n<16L/15`, `M/L<=1/16`, `M/L^4<=1/16^4`, `q<=1/4`, `log16<3`, `pi<22/7`, this is

\[
 \boxed{\text{early error}<\frac{2926}{35}|h|+\frac1{1024}.}\tag{J16}
\]

The single transition cell `n=M+1`, if present, has modulus `<int|K_L|<15` by J10.

For `n>=M+2` and all aliases in J14, `|ell|<=5L-2`. Since `q log16>(3/16)(8/3)=1/2`, J13 implies

\[
 |hU_q'(n+t)-\ell|\ge\tfrac12|h|q(\log16)16^{n-1/4}
 \quad(-1/4\le t\le1/4).\tag{J17}
\]

For each such phase, the derivative has constant sign and is monotone because `U_q''>0`. Integrate `psi(t)e(hU_q(n+t)-ell t)` by parts. The van der Corput first-derivative argument, `||psi'||_1=2`, `||psi||_infty=1` and total variation of `1/f'` yield

\[
 |I_{n,\ell}|\le\frac3{\pi|h|q(\log16)16^{n-1/4}}.\tag{J18}
\]

All `c_(L,ell)` are nonnegative, and their sum is `6L+1<=7L`. Therefore, summing geometric `16^-n` for all late cells *to infinity* gives

\[
 \boxed{\text{late error}\le\frac7{40\pi |h|q\log16}<\frac7{60|h|}.}\tag{J19}
\]

Combining J16, transition and J19, using `|h|>=1`, gives

\[
 \frac{2926}{35}|h|+\frac1{1024}+15+\frac7{60|h|}<99|h|.
\]

QED. No M-dependent observation error was hidden, and no cancellation of selected Weyl phases was assumed. Strong bounds on each **late integral** follow from its high real-time phase derivative; the coherent sum at integer points still may be N-scale because the complementary high alias frequencies remain.

### Entire normality gate recast in a controllable, explicitly bandlimited observable (ZJB-06)

For the genuine selected `q=alpha=pi/16`, for **any** finite sequence `N_M>=M` and every fixed nonzero h, J15 implies

\[
 \lim_{M\to\infty}\frac{\mathcal B_{N_M,M}(\alpha,h)}{M}=0
 \iff \lim_{M\to\infty}\frac{S_M(\alpha,h)}{M}=0.
\tag{J20}
\]

By the existing SUCC Green/Weyl bridge, π is base-16 normal **if and only if J20's left-hand convergence holds for every fixed h!=0**. This is a **proved equivalence and source-faithful finite-to-analytic realization**, not a proof of the convergence. It does NOT lower the harmonic quantifier to only h=1.

## 5. A genuinely high-alias coherent counterseed barrier (ZJB-07, PROVED PAPER)

Take the SAME four-pole forcing but *changed nonzero seed* `q=1/5`; the selected seed is NOT zero here. Because `16^n=1(mod5)`,

\[
 e(hU_{1/5}(n))=e(h/5)e(-hT(n)),\quad
 \sum_{n\ge1}T(n)<1/32\quad\text{(inherited exact source tail).}
\]

Hence every `N>=M>=1` satisfies

\[
 \left|S_N(1/5,h)-S_M(1/5,h)-(N-M)e(h/5)\right|
 <\pi|h|/16<11|h|/56.
\tag{J21}
\]

By J15 and J21,

\[
 \boxed{\left|S_N(1/5,h)-\mathcal B_{N,M}(1/5,h)\right|
 >N-M-99|h|-11|h|/56.}\tag{J22}
\]

**Not merely a positivity observation:** since the flat-top coefficient is *exactly one* for `|ell|<=L+2`, the difference equals the **SIGNED HIGH-ALIAS COMPLEMENT**

\[
 S_N-\mathcal B_{N,M}=\sum_{|\ell|>L+2}(1-c_{L,\ell})I_{N,\ell},
 \quad c_{L,\ell}=0\ \text{for }|\ell|>5L-2.
\tag{J23}
\]

For every fixed `0<theta<1`, choose `M=floor(theta N)` with `N->infty`. The alias range `|ell|<=16^M+2` is *fully retained*, yet J22 forces the signed complementary contribution to have asymptotic modulus at least `(1-theta)N-O_h(1)`. **The exponential moving high band is mathematically necessary** for the coherent altered seed. This does not prove that the selected π seed has the opposite asymptotic; its signed complement is OPEN.

## 6. The analytic horizontal seed can be specified by a finite-action principle (ZJB-08, elementary)

Parent PR #438 classifies every C1 real-time successor lift as

\[
 U_Q(x)=16^xQ(x)-T(x),\quad Q(x+1)=Q(x),\quad Q(0)=\alpha
\]

for the original integer source and zero seed. Define the SOURCE-RELATIVE normalized horizontal action

\[
 \boxed{\mathcal E_T(U_Q)=\int_0^\infty
 |\partial_x[16^{-x}(U_Q(x)+T(x))]|^2dx
 =\int_0^\infty |Q'(x)|^2dx.}\tag{J24}
\]

Since `Q'` is 1-periodic, its period-one energy is `e_Q=int_0^1|Q'|^2>=0`, and `\mathcal E_T=lim_(K->infty) K e_Q`. The action is finite **iff** `e_Q=0`, so `Q'=0` and `Q(x)≡alpha`. Thus the horizontal analytic seed is the **unique finite-action C1 extension** *once finite horizontal action is included as a NEW hypothesis*. The same selector follows from requiring `lim_(x->infty)16^{-x}(U_Q(x)+T(x))` to exist continuously in x. These are principled selector conditions, but **neither is entailed by the integer orbit alone**. Do not call the action a physical energy, a universal vacuum law, or an automatic π theorem.

For the exact periodic mutant `Q(x)=alpha+epsilon sin(2pi x)` with `epsilon!=0`, each unit interval has action `2pi^2 epsilon^2`; over K intervals the action is `2K pi² epsilon²` and diverges. This gives an explicit hostile control without evaluating pi numerically.

## 7. Analytic cell phases are almost ORTHOGONAL, even for a coherent arithmetic seed (ZJB-09A, PROVED PAPER)

This is a stronger and genuinely source-authenticated statement about the *one-dimensional Zak slice*, not merely the universal two-dimensional Zak isometry of parent PR #438. It sharpens the finite/analytic geometry without asserting a physical chirality law.

For `q in [3/16,1/4]`, integer h!=0, and integer n>=1, define the **source stationary-frequency window**

\[
 \mathcal W_n(q,h)=\left[|h|U_q'(n-1/4),\ |h|U_q'(n+1/4)\right].
\tag{J25}
\]

Since `T''>0` and `T'''<0` (differentiate the positive Laplace integral J0), `T'` increases and `T''` decreases. The real-source derivatives obey the strict adjacent-cell gap

\[
 \boxed{\inf\mathcal W_{n+1}-\sup\mathcal W_n
 >|h|(6q\log16\,16^n-1)
 >|h|(3\cdot16^n-1)>0.}
\tag{J26}
\]

The identity `16^(1/4)=2` and `16^(3/4)=8` makes the separation elementary. In particular, **no real alias frequency can have a stationary point in TWO different integer cells**. That does not mean the full Fourier transforms have disjoint support: they have nonstationary tails, which must be bounded.

Now define the source-specific continuous Zak slice at dual frequency `xi=0`:

\[
 Z_{N,q,h}(t,0)=\psi(t)\sum_{n=1}^{N}e(hU_q(n+t)),
 \qquad -1/2\le t\le1/2.
\tag{J27}
\]

**Theorem (uniform analytic orthogonality).** For ALL q in the declared range, ALL integers `N>=1`, and ALL nonzero integer h,

\[
 \boxed{\left|\int_{-1/2}^{1/2}|Z_{N,q,h}(t,0)|^2dt
  -N\int_{-1/2}^{1/2}|\psi(t)|^2dt\right|
 <\frac8{75\pi |h|}<\frac8{225|h|}.}
\tag{J28}
\]

This is `N||psi||²+O_h(1)` with an EXPLICIT all-horizon error, irrespective of the arithmetic seed q. The proof does **not** assume normality, randomness, independent channels, positivity of a fictitious Weil form or cancellation of the sampled `S_N`.

**Proof.** Expand the square; the diagonal contribution is exactly `N int psi²`. For every pair `1<=n<m<=N` consider

\[
 C_{n,m}=\int_{-1/4}^{1/4}\psi(t)^2
    e\bigl(h(U_q(m+t)-U_q(n+t))\bigr)dt.\tag{J29}
\]

The derivative of its phase divided by h is

\[
 U_q'(m+t)-U_q'(n+t)
 =q\log16(16^m-16^n)16^t-[T'(m+t)-T'(n+t)].
\]

Because `T'` increases and both values lie between -1 and 0, the bracket lies in `(0,1)`. Also `16^m-16^n>=15*16^m/16` and `16^t>=1/2`. Therefore, using `q log16>1/2`,

\[
 U_q'(m+t)-U_q'(n+t)>
 (15/64)16^m-1 >16^m/8,\quad m>=2.\tag{J30}
\]

The derivative is itself strictly increasing in t: its derivative equals `q(log16)^2(16^m-16^n)16^t-[T''(m+t)-T''(n+t)]`, which is positive because T'' is decreasing. For h<0 the full phase derivative is decreasing but still monotone and bounded away from zero. The same integration-by-parts first-derivative test as J18, now with amplitude `psi²` of variation 2 and supremum 1, yields

\[
 |C_{n,m}|<\frac{12}{\pi |h|16^m}.\tag{J31}
\]

Sum the ordered off-diagonal contributions with the exact geometric identity `sum_(m=2)^infty (m-1)/16^m=1/225`:

\[
 |2\operatorname{Re}\sum_{n<m}C_{n,m}|
 <\frac{24}{\pi|h|}\frac1{225}=\frac8{75\pi|h|}.
\]

This proves J28. QED.

**Strong negative control.** Take q=1/5 and the EXACT SAME original four signed poles. The integer seam has `|Z_(N,1/5,h)(0,0)|=N+O_h(1)` (inherited coherent source), while J28 proves its **one-dimensional continuous Zak slice** has energy `N||psi||²+O_h(1)`, just as for the original q=pi/16. Hence **even source-derived analytic phase orthogonality at every continuous within-cell offset does not force cancellation at the singled-out arithmetic seam**. A direct restriction from this `L²(t)` bound to the point `t=0` would be mathematically invalid without an additional, seed-sensitive trace estimate.

The source-specialized disjoint stationary windows are potentially useful for designing non-overlapping signed alias instruments. Yet the evidence is stronger as a **proof of where the remaining issue lives** than as a proof that the selected seam is small: the missing quantity is a source/seed-selected complex trace, not global band energy.

## 8. Falsification/claim boundary

- `r` is authentic at **all x>=1**, not just the first eight pole jets.
- `q=alpha` is selected only from the literal `U_0=0`; changed coherent q=1/5 is an explicit nonzero seed of the same forcing.
- Every J15 theorem uses a canonical **constant-Q** real-time lift. Replacing it by an arbitrary periodic interpolant invalidates the U'' and high-band bounds; J3's full alias sum nevertheless remains invariant at the integers.
- `K_L` is **not** pointwise positive. Its Fourier weights are positive, exactly flat and finitely supported; all estimates pay `int|K_L|`.
- Existing PR #437 pairwise-Haar triple lock refutes product-of-marginals substitutes; its Beta eight-jet fake refutes finite source signatures alone; nearzero rationalized seeds refute finite-horizon normality inference.
- Source-local `2/3/5` prime clocks, signed Hankel and complete monotonic forcing are retained, not promoted into an Archimedean signed cancellation theorem.
- The numerical grid diagnostic shows very accurate finite prefix recovery for small M but is **not interval-certified**, and the theoretical `<99|h|` bound is numerically vacuous for many short horizons. It is nonvacuous as a uniform **asymptotic transport O(1)**.

**OPEN gate:** prove for the genuine original four-pole `q=alpha`, with every fixed `h!=0`, an upper bound `|mathcal B_(N_M,M)(alpha,h)|=o(M)` on some declared `N_M>=M`; by J20 this proves π base-16 normality. J15 supplies the faithful map and uniform error, not the required smallness. A real advance beyond this paper must exploit source-specific signed joint-channel / real cofiber / selected-lag information to separate alpha from the coherent q=1/5 model.

### Classical instrument provenance

- Zak/Poisson: Hernández, Šikić, Weiss, Wilson, *The Zak Transform(s)*, https://verso.mat.uam.es/~eugenio.hernandez/Papers/Zak-2010-June.pdf (classical Fourier sampling identity).
- Jackson-type fourth-power approximate kernels: Korevaar, *Distributional Wiener–Ikehara*, https://staff.fnwi.uva.nl/j.korevaar/DisWieIke.pdf (fourth-power/positive approximate identities; the explicit finite flat-top convolution and constants are derived here).
- Oscillatory first-derivative lemma: Shapiro, *Notes on Oscillatory Integrals*, https://www.joelshapiro.org/Pubvit/Downloads/OscNotes/oscint.pdf (standard derivative monotonicity proof; constants derived here).
- Source provenance: Main XVIII original `research/2026-10-31/selected_lag_tomography/PROOFS.md`, `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`; sibling PR #437 `research/2026-10-31/four_pole_path_interference/PROOFS.md`; parent PR #438 `research/2026-10-31/seeded_zak_seam/PROOFS.md`. These are the same source, not independent corroborations of original mathematics.
