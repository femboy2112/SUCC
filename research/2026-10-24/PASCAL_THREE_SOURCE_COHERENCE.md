# Operation Pascal-3 — exact source-coherent prime factorization and selected π frontier

**Date:** 2026-10-24. **Stack:** research draft on [SUCC PR #275](https://github.com/femboy2112/SUCC/pull/275) at pinned head \`7c5d5b8856a1d132fb941ae40c946c0565918b36\`; inherited PR #272 at \`6e8fa8b77886b13f1f533ed8083fd88c849d14b3\`. PR #273 (path selection), #274 (Pascal/Lucas), and #269/#271 (carry/Walsh) were **read as siblings** and not silently merged. Coherent main inspected: \`e648df3e4fca73ab6b942232b5ca4b310e9cac08\`.

**π normality in bases 2,3,16: OPEN. Selected source-law tripling, all-scale real-circle collision dimension and signed 1/16 retention: UNVERIFIED.** Paper-level proofs and exact finite local oracles are not Lean declarations, external review, or full-repository CI. **Important prior-art boundary:** PR #275 already proves positive affine prime charts and the sharp 225/256 base-3 shadow; shared discoveries are NOT new claims of priority.

## P3-01 — Pascal generates 3^n with TWO distinct readings (CLASSICAL EXACT)

For all n≥0,

\[
2^n=\sum_{k=0}^n\binom nk,\qquad
3^n=\sum_{k=0}^n\binom nk\,2^k
=\sum_{k=0}^n\binom nk\,16^k(-13)^{n-k}.
\]

At n=4 the unweighted row is (1,4,6,4,1) with total 16; weighting by 2^k gives (1,8,24,32,16), total 81. Ternary words are binary support masks with two choices at each selected position. This is exact counting, not a BBP digit frequency result. The signed (16−13)^n identity is a second operation and must be transported through the actual source phase and integer carries rather than substituting expectations for products.

The common *positive* Pascal binomial mean on bounded complex time arrays is

\[
B_n(a)=3^{-n}\sum_{k=0}^{n}\binom nk2^k a_k.
\]

This is the expectation of a_K for K~Binomial(n,2/3). Note: the operator (I+2E)/3 has eigenvalue 11 on a homogeneous 16^k mode; it is not the positive affine base-3 operator of PR #275.

## P3-02 — exact Bernoulli stopping-time Tauber contract (PROVED elementary)

For |a_k|≤A, let S_m=Σ_(k<m) a_k and m=floor(2N/3). Couple K_n as partial sums of i.i.d. Bernoulli(2/3) indicators. Pathwise S_(K_(n+1))-S_(K_n)=X_(n+1)a_(K_n); taking expectations and Cauchy–Schwarz gives

\[
\boxed{\left|S_m-\frac23\sum_{n=0}^{N-1}B_n(a)\right|
\le A\sqrt{\frac{2N}{9}+1}.}
\]

Thus for the authentic BBP states y_(k+1), proving B_n(e(hy_(k+1)))→0 for every fixed h≠0 would imply vanishing base-16 Weyl sums and therefore hexadecimal/binary normality of π. This is a strong **sufficient criterion**; it does not currently hold by any proved estimate. General normality does NOT imply such short binomial-window cancellation: sparse long deterministic blocks preserve global normality while defeating local windows. Euler/Knopp-type transforms and probabilistic Tauber arguments are classical, priority unverified.

## P3-03 — BBP-selected phase transfer with rational precision budget (PROVED)

Preserve the original signed four-pole source and initial state:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
y_0=0,\quad y_n=\{16y_{n-1}+r(n)\}.
\]

The authenticated tail identity is y_(k+1)+T(k+1)=16^k π (mod1), 0<T(k+1)<1/[64(k+1)^2]. For K~Binomial(n,2/3), an elementary reciprocal-binomial moment calculation gives E[(K+1)^(-2)]≤9/[2(n+1)(n+2)]. Hence

\[
\boxed{
\left|B_n(e(hy_{k+1}))-B_n(e(h16^k\pi))\right|
<\frac{99|h|}{224(n+1)(n+2)}.}
\]

Actual-source signed complex observation transport: PROVED. The magnitude of either weighted mean: UNBOUNDED asymptotically. A standalone independent Machin arctangent rational enclosure and rational Taylor trigonometric interval oracle certified ten finite h=1,3, n=8/16/32/64/96 means; h1 magnitudes are nonmonotone. No π digit file, floating threshold decision or fitted exponent.

## P3-04 — source-positive universal small-prime charts (CORROBORATED PR #275)

PR #275 already proves the unique positive affine normalized filter

\[
P_q(E)=\frac{(16-q)I+(q-1)E}{15}
\quad(2\le q\le16),\qquad P_q(1)=1,\ P_q(16)=q.
\]

It covers q∈{2,3,5,7,11,13} and gives unwrapped rational shadows
\(P_q(E)^nU_0=q^n(\pi/16)-R_{q,n}\), \(R_{q,n}>0\), with the source-positive integral and sharp \(\lim n^2 R_{q,n}=225/[64(q-1)^2]\). For q3, \(P_3=(13+2E)/15\) and n=64 yields an independently certified \(0<R_{3,64}<0.000306\). **This is not a new source-normality theorem.**

Critical noncommuting carry projection: for q3 at order1 the authentic rational output is \(94/225\), whereas substituting fractional input before applying the rational operator produces \(4/225\); discrepancy \(2/5\). The 15^n integer-carry coordinate must be retained (possibly reducible with a separate proof). The #275 source already contains broader sharp dyadic-chart theorems.

## P3-05 — alternative signed INTEGER ×3 filter and authentic correction (PROVED)

The signed integral polynomial \(D_3(E)=E-13I\) has D3(16)=3 without division by 15. For t≥1 and depth j≥1,

\[
\boxed{\sum_{k=0}^j\binom jk(-13)^{j-k}y_{t+k}
\equiv 3^jy_t+C_{t,j}\pmod1.}
\]

The integer coefficients make this observable well-defined on circle states without introducing a new division-cover residue. All original source carries remain encoded implicitly in the mod-one equality.

With \(P(x)=4+4x+4x^2+2x^3+x^4\), the explicitly sourced rational correction is

\[
C_{t,j}
=\sum_{a=1}^j\left[\sum_{k=a}^j\binom jk(-13)^{j-k}16^{k-a}\right]r(t+a)
=\int_0^1 x^{8t}(1-x)P(x)\frac{3^j-(x^8-13)^j}{16-x^8}\,dx.
\]

Its sign is \((-1)^{j-1}\) and **sharp elementary safe bound** is

\[
\boxed{0<(-1)^{j-1}C_{t,j}
\le\frac{13^j-(-3)^j}{16}\,r(t+1).}
\]

On first-birth good prime windows p=8m+1 with t≥m+1 and j≤floor((2/5)log_16 p), this costs \(O(p^{-2+(2/5)\log_{16}13})=O(p^{-1.630\ldots})\). Thus an authentic growing hierarchy of ×3 circle *readouts* exists with no added rational division carry, but we **cannot** infer that its empirical law equals that of y_t.

Scoped obstruction: a nonconstant polynomial with nonnegative *integer* coefficients evaluated at E=16 is at least16, so no such positive integer finite-stencil operator realizes eigenvalue3. The signed-vs-positive information tradeoff is real, not a theorem about all nonlinear observers.

## P3-06 — exactly factorized prime-chart composition defect (PROVED; priority unverified)

For 2≤q,r, qr≤16,

\[
\boxed{P_q(E)P_r(E)-P_{qr}(E)
=\frac{(q-1)(r-1)}{225}(E-I)(E-16I).}
\]

These polynomials commute. This is *NOT* a commutator, and no quantum transported phase is defined.

On the authentic unwrapped zero-initial BBP source \(U_{t+1}=16U_t+r(t+1)\),

\[
\boxed{(P_qP_r-P_{qr})U_t
=\frac{(q-1)(r-1)}{225}[r(t+2)-r(t+1)]<0.}
\]

The positive moment representation gives the explicit strict estimate

\[
0<r(t+1)-r(t+2)
<\frac{240}{(8t+1)(8t+2)(8t+3)}.
\]

Moreover \(t^3[r(t+1)-r(t+2)]\to15/32\), hence the exact leading coefficient

\[
\boxed{\lim_{t\to\infty}t^3 (P_qP_r-P_{qr})U_t
=-\frac{(q-1)(r-1)}{480}.}
\]

For 3×5 the limit is −1/60. If \(\Delta(q,r)=P_qP_r-P_{qr}\), the three-way associativity coherence is the exact polynomial identity \(\Delta(q,r)P_s+\Delta(qr,s)=P_q\Delta(r,s)+\Delta(q,rs)\), on every shared domain qrs≤16. All two- and three-factor cases were exact rational tested.

**Boundary:** vanishing of this deterministic source-observable defect as t→∞ does not establish Haar mixing or same-law ×3 invariance. A zero-forcing rational fixed-point countermodel has zero defect and nonnormal digits.

## P3-07 — cross-prime selected-path Fourier interferometer and limit-order no-go (PROVED identity)

For the full coherent initial-selector family \(Y_t(x)=y_t^{(0)}+16^t x\bmod1\), define \(A_{N,L}(x;h)=(NL)^{-1}\sum_{t<N,j<L}e(h3^j Y_t(x))\). Every input frequency h16^t3^j is distinct by multiplicative independence, so for arbitrary deterministic forcing

\[
\boxed{\int_\mathbb T|A_{N,L}(x;h)|^2dx=\frac1{NL}.}
\]

A Fejér root selector bandwidth \(B=|h|16^N3^L\) recovers its selected x=0 rectangle with provable absolute weight loss

\[
\boxed{\frac{(1-16^{-N})(1-3^{-L})}{30NL}<\frac1{30NL}.}
\]

As a negative control, if 3 is replaced with q=4, frequencies collide; at N4,L5, zero-forcing L2=21/200, not 1/20. A rational changed-selector x=1/5^r can make every Fourier mode in an arbitrary prescribed *finite* h-band vanish under a complete 3-period, although its base16 orbit is periodic and nonnormal. This observation family does NOT retain the authentic π initial condition and cannot disprove a correctly source-selected statement. Haar L2 average of all paths cannot be promoted to the selected x0=0 value. Root-bandwidth grows as 16^N3^L, reproducing the selection/time limit obstruction of sibling PR #273.

## P3-08 — finite tripling-law discriminator, with no asymptotic claim (VERIFIED FINITE)

The relevant SUCC #270 hypothesis is same-window \(\beta_p(3)=W_1((T_3)_*\mu_p,\mu_p)\to0\), not normality of separate 3^nπ digits. Exact source and independent Machin/Taylor Fourier interval probes certify positive **lower bounds**:

| selected prime p | full first-window samples | certified \(\beta_p(3)\) lower bound |
| ---: | ---: | ---: |
| 41 | 15 | 0.032893107846 |
| 97 | 36 | 0.063450449496 |
| 257 | 96 | 0.006379229829 |

Nonmonotone; no infinite inference. The signed integer filter shows a tiny source correction between its selected output law and \(T_3{}_*\mu_p\), but **does not** control the difference from original \(\mu_p\). The positive all-scale *real-circle* collision dimension required in the classical measure-rigidity alternative is likewise unproved; dyadic source 1/16 is a different statistic.

## P3-09 — validation, authority and next falsifier

The standalone scientific package includes a 494-line independent module, a 242-line rational Machin/Taylor oracle, 23 exhaustive source math unit methods, frozen detailed JSON receipt and full derivation. The additive compact bridge is \`observational_succ/pi_pascal_three_bridge.py\` and \`tests/test_pi_pascal_three_bridge.py\` (**9/9** methods), both Git blob byte-identical to isolated locally tested source before staged Git publishing. Earlier source API was independently compared on 160 forcing and 161 zero-initial state values. The 23 full-lab methods plus compact nine passed locally, compileall succeeded, and the frozen detailed JSON receipt replayed byte-for-byte. NO complete SUCC checkout suite, hosted new-head CI or Lean kernel theorem is claimed. An isolated local BBP source API stub is included only in the downloadable lab, **not the GitHub commit**, because SUCC already owns that authoritative module.

**Verdict:** the new-to-this-round prime-factorization coherence identity, signed ×3 integer readout and Pascal-Taub criterion have mathematically precise proofs and exact finite controls. External scholarly novelty unverified. π normality, selected ×3 invariance, source-selected Walsh cancellation and selected real-circle 1/16 retention remain OPEN.

**Next mathematical discriminator:** prove for some fixed h≠0 or, ultimately all fixed h, a genuinely source-specific asymptotic bound on
\[
\frac1{|W_p|}\sum_{t\in W_p}
\left[e(h(y_{t+1}-13y_t))-e(hy_t)\right]
\]
with authentic signed four-pole forcing, \(y_0=0\), all carries, real circle geometry and endpoints preserved. This is equivalent up to a controlled \(O(p^{-2})\) error to the #270 Fourier test of same-window tripling invariance and cannot be inferred from the small forcing remainder by itself. To prove binary normality by #270's Rudolph–Johnson criterion requires *also* positive all-scale selected real collision dimension; alternatively prove the stronger selected signed Walsh 1/16 retention. Failed-source countermodels must be tested.

**References:** Bailey–Borwein–Plouffe, original digits identity https://www.davidhbailey.com/dhbpapers/digits.pdf; Lucas theorem https://math.hmc.edu/funfacts/lucas-theorem/; classical Euler–Knopp methods https://encyclopediaofmath.org/wiki/Euler_summation_method; SUCC donor PR #275 positive filter and #270 conditional base3-rigidity route. All links and proofs must be audited independently before admission to main.
