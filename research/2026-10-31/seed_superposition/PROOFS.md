# Operation SELECTED SEED × SUPERPOSITION — exact cylinder Gram, Pascal moment cutoff, aliasing and resistance

**2026-10-31. Research only.** Exact parent: SUCC draft PR #431 at `cf23b8cfc39f56935c432ed764adf0a33efb0d7e`; main baseline `e8598cfa5d32fd1de8e94a3e458a366a0850d59e`. Original signed four-pole BBP forcing, literal `U_0=0`, historical contracts, formal source, CI and production remain unchanged. **π base-16 normality and RH remain OPEN.** The underlying orthogonality, moment and Bernoulli/Markov tools are classical, and the base-16 carry threshold r=17 is previously established in SUCC PR #404. This round adds a carefully typed **local-cylinder superposition theorem, an exact arbitrary-finite-grid aliasing no-go, and a quantitative resistance/point-selection price**. No independent scholarly priority is claimed.

## 0. What is meant by the superposition measure

The new PR #431 constructs carrier-relative positive path measures, graph effective resistance and independently phased path amplitudes. Do **not** identify its chosen Gaussian-Pascal root-of-unity phases with the authentic BBP phases; PR #431 proves this would be invalid. Here is a source-authenticated compatible construction using the actual one-parameter family of trajectories **of the same unchanged forcing**:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0(s)=s,\quad U_{n+1}(s)=16U_n(s)+r(n+1).
\]

The original selected orbit is **exactly** `s=0`. Induction proves

\[
\boxed{U_n(s)=U_n(0)+16^n s.}\tag{SH1}
\]

For an integer frequency `h≠0`, define the source-selected phase `z_n(s;h)=exp(2πi h U_n(s))`. Its phase at `s=0` is an *actual* rational BBP observable, unlike an attached q-binomial model phase. Define a depth-`M` seed cylinder `I_(M,a)=[a/16^M,(a+1)/16^M]`, `0≤a<16^M`, carrying **uniform normalized Lebesgue probability** `μ_(M,a)`. This is an auxiliary model of an observer who knows only `M` base-16 digits of a possible seed. It is not the true probability law of π or of the distinguished seed `0`. We also allow translated cylinders `[s0,s0+16^(−M)]` for the coherent counterseed.

Distinguish precisely: source arithmetic; selected point `s=0`; auxiliary seed-family path states; prior probability measure `μ`; scalar path Fourier readout; local-to-real boundary maps. The observer's virtual paths are *not* presumed to be independent realizations of π.

## SS-01 — exact conditional Haar and path Gram on EVERY cylinder (PROVED LOCAL, elementary)

Write `s=(a+t)/16^M`, `t∈[0,1]`. For every `n≥M`,

\[
z_n(s;h)=e(hU_n(0))\,e(h16^{n-M}t),\qquad e(x)=e^{2π ix}.
\]

The integer factor `16^(n−M)a` drops out exactly; no statistical assumptions are used. Integration in the continuous *auxiliary seed parameter* therefore yields

\[
\boxed{\mathbb E_{μ_(M,a)}z_n=0,\quad
\mathbb E_{μ_(M,a)}z_n\overline{z_m}=\delta_{n,m}\quad(n,m≥M).}\tag{SS01}
\]

Thus for any `N≥M` and `K=N−M`,

\[
\boxed{\mathbb E_{μ_(M,a)}\left|\sum_{n=M}^{N-1} z_n\right|^2=K.}\tag{SS02}
\]

**Exact signed-superposition bridge:** PR #431's full off-diagonal path Gram becomes the identity for the *continuous seed-cylinder tail*, independently of the original four-pole source values. The PR #431 positive path/resistance measure is NOT an alternative source for these phases. Conversely the point-selected `z_n(0)` has no such orthogonality guarantee. SS01 is therefore a correct ***auxiliary*** superposition theorem and a sharp source-selection firewall.

For `n<M`, the elementary Lipschitz inequality `|e(x)-e(y)|≤2π|x-y|` and a uniform `t` average imply

\[
\boxed{\left|\mathbb E_{μ_(M,a)}S_N(s;h)-S_{\min(N,M)}(a/16^M;h)\right|
\le\pi|h|\sum_{n=0}^{\min(N,M)-1}16^{n-M}
<\frac{\pi|h|}{15}.}\tag{SS03}
\]

Here `S_N=Σ_(0≤n<N)z_n`. The continuous superposition average loses **ALL later terms `n≥M`**, while retaining the first `M` selected phases within a bounded approximation. Neither mean is asserted to equal the actual `S_N(0)` when `N≫M`. The zero seed is the left boundary of the `a=0` cell and has zero continuous measure.

## SS-02 — all first 16 balanced even moments mimic independent uniform phases (PROVED LOCAL, extension of SUCC #404)

For an integer `1≤r≤16`, expand the `2r`-th moment of the same late sum. Every term is an integral of a circle character with frequency

\[
h\Bigl(\sum_{j=1}^r16^{n_j-M}-\sum_{j=1}^r16^{m_j-M}\Bigr).
\]

It vanishes unless the two sums of `r` powers of 16 are *equal as integers*. For `r≤16`, equality forces the same multiplicity vector. Proof: let `e_i` be the difference of two count vectors, with `Σe_i=0` and `Σe_i16^i=0`. If `e` is nonzero, let `j` be its smallest nonzero index. Reducing the second equality modulo `16^(j+1)` gives `16|e_j`. As each side contains at most 16 terms, necessarily `e_j=±16`, exhausting the entire positive (or negative) count budget. All later nonzero differences then have the opposite sign. Their weighted sum has magnitude at least 16 times that of `e_j16^j`, impossible. Hence `e=0`.

For `K=N−M` let `c_1+...+c_K=r`, `c_i≥0`. The exact moment is

\[
\boxed{\mathbb E_{μ_(M,a)}|S_{M:N}|^{2r}
=\sum_{c_1+...+c_K=r}\left(\frac{r!}{\prod_i c_i!}\right)^2
\le r!K^r,\quad 1≤r≤16.}\tag{SS04}
\]

In particular the second moment is `K` and fourth is `2K²−K`. This **same full-Haar moment cutoff** was already proven by SUCC PR #404; the added result is that the entire moment law holds on *each separately resolved finite seed cylinder*, for its **future tail**. Direct ordered-tuple frequency enumeration and a distinct multiplicity-vector computation independently check the lower moment formulas.

At `r=17`, the first distinct equal-length power relation appears:

\[
\boxed{16\cdot16^n+16^{n+2}=17\cdot16^{n+1}.}\tag{SS05}
\]

The corresponding real source phase is the authentic signed difference `e(h[r(n+2)-r(n+1)])`, not a model-chosen phase. This source-dependent 34th moment phenomenon is exactly in the SUCC #404 provenance, not a new discovery of its threshold.

A Markov bound gives an exact normalized auxiliary-seed concentration estimate for every `r≤16`, `K≥1`, `ε>0`:

\[
\boxed{\mu_{M,a}\bigl\{|S_{M:N}|≥εK\bigr\}
\le\min\{1,r!/(ε^{2r}K^r)\}.}\tag{SS06}
\]

For `r=2`, these bounds are summable over K; Borel–Cantelli gives generic future cancellation for almost every auxiliary seed inside any fixed cylinder. This is a classical normality-type consequence for the seed ensemble. The *chosen zero seed* is not proven typical. The identical estimate also holds in every translated cylinder anchored at the coherent, nonnormal counterseed `s*=-π/16`.

## SS-03 — source-attested 17-factor resonance is nearly maximally COHERENT (PROVED LOCAL / SUCC #404 refinement)

Induction on the unchanged source yields the pointwise exact identity for EVERY real seed:

\[
\boxed{z_n(s;h)^{16}\overline{z_{n+1}(s;h)}=e(-h r(n+1)).}\tag{SS07}
\]

The `16` seed-scaling cancels in the left exponent exactly. This is a genuine source-attested high-order path-phase relation—yet it is ***seed-blind***. Since the original four-pole positive forcing satisfies `0<r(n+1)<15/(64n²)` for n≥1, for every `M≥2` and every `N>M`,

\[
\boxed{\left|\sum_{n=M}^{N-2}e(-hr(n+1))-(N-M-1)\right|
<\frac{15\pi|h|}{32(M-1)}.}\tag{SS08}
\]

This uses `Σ_(n≥M)n^{-2}<1/(M-1)` and the elementary phase Lipschitz inequality. The authentic source's *first* nontrivial carry resonance is therefore **asymptotically maximally coherent**, not a mechanism that automatically cancels the selected Weyl sum. It is a falsification target for future nonflat-path proposals.

## SS-04 — fixed finite path ensembles alias back into PERFECT coherence (PROVED LOCAL)

Replace the continuous `t∈[0,1]` by a finite `16^d`-point grid in the same seed cylinder,

\[
s_j=\frac{a}{16^M}+\frac{j}{16^{M+d}},\quad j=0,...,16^d-1.
\]

For each `n≥M`, exact finite cyclic-character orthogonality gives

\[
\boxed{\frac1{16^d}\sum_{j=0}^{16^d-1}e(hU_n(s_j))
=e(hU_n(0))\,\mathbf 1_{16^d\mid h16^{n-M}}.}\tag{SS09}
\]

For primitive frequency `h=1` this is **zero** at `M≤n<M+d` but **exactly the selected phase** for every `n≥M+d`. By contrast the *true continuous cylinder* average SS01 remains zero at EVERY n≥M. A fixed finite measure cannot represent the full infinitely refined observable as if no aliasing occurred.

**Stronger finite path theorem:** for any finite probability measure on dyadic rational seed offsets `s_j∈Z[1/2]/Z`, there is a finite integer `D` such that `16^n s_j` is integral for every path once `n≥D`. Then

\[
\boxed{\sum_jw_j e(hU_n(s_j))=e(hU_n(0))\quad\forall n≥D,\ h∈Z.}\tag{SS10}
\]

The time-tail phase Gram under this finite ensemble is the **rank-one** matrix `z_n(0)overline(z_m(0))`, whereas the continuous-cylinder Gram SS01 is **identity** for any finite set of distinct late times. These are demonstrably different observation functors. There is no finite `D` for non-dyadic rational offsets such as `1/3`: the denominator contains a persistent odd prime. Exact cyclotomic reduction by `X^(16^d/2)+1` is an independent test of SS09, with no approximate complex exponentials.

## SS-05 — the effective-resistance/Dirichlet observation cost grows exponentially (PROVED LOCAL)

The path-measure connection to PR #431's **effective resistance** is operational. On a real seed interval, the continuum Dirichlet inequality

\[
|F(s)-F(t)|^2\le |s-t|\int_{[s,t]}|F'(u)|^2du
\]

is the one-dimensional Thomson–Poincaré bound. Apply this to the **authentic** source-phase tail `F_(M,N)(s)=Σ_(M≤n<N)z_n(s;h)`. Differentiating SH1 gives `F' =2πih Σ16^n z_n`. Exact conditional cylinder orthogonality SS01 then yields

\[
\boxed{\mathbb E_{μ_{M,a}}|F'_{M,N}(s)|^2
=(2\pi h)^2\sum_{n=M}^{N-1}16^{2n}
=(2\pi h)^2\frac{16^{2N}-16^{2M}}{255}.}\tag{SS11}
\]

The mean-square gradient is **exponential** in N even though the source-averaged phase sum has variance only `N−M`. This explains why a generic resistance/positive path measure cannot supply a uniform evaluation inequality at `s=0`. For all terms `S_N` and the anchored interval of width `16^{-M}`, the derivative/Lipschitz estimate yields only

\[
\boxed{\left|\mathbb E_{μ_{M,a}} S_N-S_N(a/16^M)\right|
\le\frac{\pi|h|(16^N-1)}{15\cdot16^M}.}\tag{SS12}
\]

For N≫M this is vacuous. It is NOT a theorem that the actual π-selected phases must grow or concentrate; it identifies the explicit *source-uniform point-evaluation cost* a new arithmetic rigidity result must overcome.

## SS-06 — changed-seed hostile holdout; the source/observer gap is strict (PROVED LOCAL)

The established BBP identity gives `16^(n−1)π=U_n(0)+T_n`, with `0<T_n<1/(64n²)` for n≥1. For the **same forcing** and altered real seed `s*=-π/16`, we have `U_n(s*)=-T_n` and

\[
\boxed{\left|\sum_{n=M}^{N-1}e(hU_n(s*))-(N-M)\right|
\le2\pi|h|\sum_{n≥M}T_n<\pi|h|/16\quad(M≥1).}\tag{SS13}
\]

This particular **point-selected** late sum has magnitude asymptotic to N−M, even though averaging over a seed cylinder `[s*,s*+16^{-M}]` gives *zero* mean, identity tail Gram, and all moment/concentration identities SS01–SS06. The source forcing and first carry resonance SS07 are unchanged. Thus the inference

> auxiliary superposition measure gives Haar conditional phase averages ⇒ actual selected seed is normal

is **REFUTED, with an exact same-forcing hostile control**. This does not refute normality of the true zero seed. It proves that **seed-local arithmetic exclusion of exceptional selected points is genuinely necessary**.

## SS-07 — final theorem gate and next falsifiable research

The entire suite is additive source-faithful *observer machinery*, not a proof of the open selected signed Weyl estimate. For fixed h≠0, what remains is still

\[
\boxed{\sum_{n≤N}e(hU_n(0))=o(N).}
\]

Superposition/seed averaging proves an excellent typical-seed result but cannot discriminate the singleton `s=0`; the concentrated altered seed disproves any universal promotion. PR #431's arbitrary q-Pascal root-of-unity phase likewise cannot substitute for the real selected character.

**Next discriminating instrument:** an authenticated **source-selected capacity/anti-concentration** estimate that bounds the pointwise signed future sum from arithmetic, rather than from auxiliary seed Haar. One possible approach is to construct a source-derived nonflat path connection in the existing `ObservationPathCategory` and prove a signed real-character saving on a family of time blocks that actually covers all N. It must retain the selected `U_0=0`, full four original poles, and the Green tail, fail for `s*`, and not use a chosen independent q-Pascal path phase. Any statement merely rewriting SS13 or the Weyl criterion is not an advance. A strong candidate must also beat SS11's exponentially growing resistance/gradient price.

**Claim firewall:** SS01–SS13 are classical algebra/analysis with new-to-project cylinder scope and exact signed source interface, not academic originality; source-seed pointwise normality **UNVERIFIED**; no RH theorem or physical quantum/black-hole identity. Conditional moment r≤16 and source first-carry at r=17 are explicitly inherited from SUCC PR #404 for full Haar and newly transported to every seed cylinder's future tail. The parent CRPM path-resistance and gauge-flatness limitations remain valid.
