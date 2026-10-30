# Operation Kepler III — Exact shrinking-target BBP carries, information locking, and a sharp normality obstruction

**2026-10-29 · Research-only.** Exact source parent: SUCC draft PR #382 at `0a1e6ffef8823711104ca8b4d1de5bdbdfa6cd26` (inherits #380/#377/#376, merged Main XIV ancestry). Read-only siblings: #378 (relative observation), #379 (normal form), #383 (Oily logarithm/ternary orientation). Do **not** edit the original four signed poles, `U_0=0`, archival sources or existing claim identifiers. No base-16 normality of pi, RH, a physical entropy law or scholarly novelty is claimed.

## I. The Kepler reduction: an exact shrinking-target window

Preserve the original source for each integer `n>=1`:

\[
r_n=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_n(s)=16U_{n-1}(s)+r_n,\quad U_0(s)=s.
\]

The exact original Green tail is
\[
T_n=\sum_{j\ge1}16^{-j}r_{n+j}>0,
\qquad 16T_{n-1}=r_n+T_n.
\]

By the inherited BBP identity, `sum_{k>=1}16^{1-k}r_k=pi`, and hence for `n>=1`
\[
U_n(s)=16^{n-1}(\pi+16s)-T_n.
\]

Write `x_n(s)={U_n(s)}`, the unforced circle position `y_n(s)={16^{n-1}(pi+16s)}`, the bare same-state digit `d_n(s)=floor(16 x_{n-1})` and the literal source carry `kappa_n(s)=floor(16 x_{n-1}+r_n)`. For `n>=2` we have `0<r_n<1` and `T_n+r_n<1`.

**K3-01 (EXACT source-selected shrinking target).** For every seed `s in R`, every `n>=2`, and all endpoint conventions fixed to half-open intervals,
\[
\boxed{
 E_n(s):=\kappa_n(s)-d_n(s)
 =\mathbf 1_{\{16^{n-1}(\pi+16s)\}\in[T_n,T_n+r_n)}.
}\tag{1}
\]
This is a 0-or-1 indicator. On this event, `x_n(s)=y_n(s)-T_n in [0,r_n)`.

**Proof:** Let `v=y_n`, `t=T_n`, `r=r_n`, and use `16T_{n-1}=r+t`. Then `{16x_{n-1}}={v-(t+r)}`. The increment from `d_n` to `kappa_n` is 1 iff the latter fractional part is at least `1-r`. Since `t+r<1`, this happens exactly when `t<=v<t+r`. This holds for every seed. No circle equidistribution assumption is involved.

The forcing has the source-positive regrouping
\[
r_n=\frac{6}{a(a+3)}+\frac4{a(a+4)}+\frac5{a(a+5)},\quad a=8n-7.
\]
The inherited exact polynomial certificate in #382 gives `r_n<1/(2n²)` for all `n>=3`, and the positive regrouping gives the **additional explicit lower bound** `r_n>15/(8n-2)²>15/(64n²)`. The inherited Green tail bound `T_n<(8n+1)^(-2)<1/(64n²)` then gives
\[
\boxed{0<T_n+r_n<\frac{33}{64n²}<\frac1{n²}\quad(n\ge3).}\tag{2}
\]
Also `r_n=15/(64n²)+O(n^(-3))` and `T_n=1/(64n²)+O(n^(-3))`, with exact source coefficients in #369/#379.

## II. One correction forces a source-selected word of ordinary pi-radix digits

Put `L_n=floor(log_{16} n²)` using the exact integer condition `16^L_n<=n²<16^(L_n+1)`.

**K3-02 (DIRECT pure-radix zero-cylinder theorem).** Every event `E_n(s)=1` at `n>=3` forces the next `L_n` ordinary base-16 digits of the *pure* circle orbit of `beta=pi+16s`, beginning at digit position `n`, to equal zero:
\[
\boxed{\{16^{n-1+j}\beta\}<1/16\quad(0\le j<L_n).}\tag{3}
\]
Indeed `y_n<T_n+r_n<1/n²<=16^{-L_n}`; no wrap can occur during the first `L_n-1` shifts, and each corresponding leading hexadecimal digit is zero. This is slightly stronger in type than the inherited #382 theorem: the exact **unforced pure-radix word** is zero, not merely the literal corrected-carry word.

As before, the same event forces literal carries `kappa_(n+1),...,kappa_(n+L_n)` all zero: this also follows from the zero-word threshold in III, without assuming any normality. These event-zero-word intervals are disjoint for distinct correction times. Therefore the inherited `O(N/log N)` all-seed event count follows.

## III. Exact posterior of a directional event; bounded information mismatch

Take Haar measure **only as a reference over possible physical seeds**, never as the probability law of the actual zero seed. Under Haar, `y_n` and `x_n` are individually uniform on the circle. Equation (1) implies
\[
\boxed{P_H(E_n)=r_n,\quad x_n\mid E_n\sim \operatorname{Unif}[0,r_n).}\tag{4}
\]

Define `Z_(n,L)` to be the event of `L` consecutive **literal zero carries after time n**. Direct iteration of the actual affine recurrence shows that, for `L>=1`, this is precisely `0<=x_n<B_(n,L)`, where
\[
\boxed{ B_{n,L}=16^{-L}(1+T_{n+L})-T_n.}\tag{5}
\]
At `L=0`, set `B_(n,0)=1` and `Z_(n,0)` to the sure event. The displayed formula also equals 1 when L=0, by cancellation. For the original `L=L_n`, the source inequalities (2) give
\[
 r_n<B_{n,L_n}<16^{-L_n}\quad(L_n>=1).
\]
The lower bound follows from `B>=16^(-L)-T_n>r_n`; the upper bound from the strictly positive first L terms of `T_n`. Thus `E_n subset Z_(n,L_n)` exactly, for **every seed**. Under Haar the latter event has mass exactly `B_(n,L_n)` and conditional state `x_n` uniform on `[0,B)`.

**K3-03 (bounded information-lock).** The KL cost of selecting the smaller source-correction event after already observing the guaranteed zero word is
\[
\boxed{D(P_H(x_n\mid E_n)\Vert P_H(x_n\mid Z_(n,L_n)))
=\log\frac{B_{n,L_n}}{r_n}\in[0,\log(1024/15)).}\tag{6}
\]
Its unconditional event surprise is `I_n=-log r_n`; for all `n>=3`,
\[
\boxed{\log2<I_n-L_n\log16<\log(1024/15).}\tag{7}
\]
The proof of (7) uses precisely `15/(64n²)<r_n<1/(2n²)` and `16^L_n<=n²<16^(L_n+1)`. This is a **relative Shannon/KL information comparison**, not a measured work, heat or physical collapse budget.

Writing `theta_n=n²/16^L_n in [1,16)`, exact tail asymptotics give, uniformly in `theta_n`,
\[
\boxed{P_H(E_n\mid Z_(n,L_n))
=\frac{15}{64\theta_n-1}+O(1/n).}\tag{8}
\]
The original endpoint zero (Gamma rank 2) fixes the exponent `2 log n` in (7), and the authentic source slope `Q'(0)=15=16-1` fixes the coefficient 15. Euler's constant appears in the *distinct harmonic comparison*
\[
\boxed{\lim_{n\to\infty}[-\log r_n-2H_n]
=\log(64/15)-2\gamma.}\tag{9}
\]
The Oily inverse-golden fixed point is a separately marked packet reference, **not forced** by this entropy calculation. This is a genuine source-to-Gamma/Euler bridge, with its normalization type stated.

## IV. Exact signed current on the full 17-bin carry register

For *any* complex mark `z_n` attached to the selected circle state (particularly `z_n=e(hx_n)`), the following is a pointwise identity for each integer `c=0,...,16`:
\[
\boxed{
\mathbf 1_{\kappa_n=c}z_n
=\mathbf 1_{d_n=c}z_n
+E_n(\mathbf 1_{d_n=c-1}-\mathbf 1_{d_n=c})z_n.}\tag{10}
\]
Missing indices are zero. This is a **discrete divergence of the signed carry-correction current**: flux arrives from bin `c-1` and leaves bin `c`. Summing c gives back the unprojected selected phase exactly; never discard the integer lift before constructing the tensor.

For q=6, multiply (10) by the exact original Pascal weight `q_n(j)` and both selectors `1_{gcd(j,6)=a}`, `1_{gcd(j+2,6)=b}`, evaluated at the true selected offset `m=n+j`. Equation (10) then holds coefficientwise in all **4 x 17** tensor bins, preserving absolute rational phase labels. It does not assume an independent distribution of carries. This is the signed selected evolution we can prove unconditionally.

For a hypothetical Haar-distributed seed, `d_n` is uniformly distributed over 16 inverse branches conditional on the correction interval. Each branch carries the same signed event-current
\[
\boxed{J_{n,h}=\frac1{16}\int_0^{r_n}e^{2\pi ihu}\,du
=\frac{e^{2\pi i h r_n}-1}{32\pi i h}\quad(h\ne0).}\tag{11}
\]
Interior bins receive and lose the same current, so their nonzero-h signed expectation vanishes; the two boundary bins carry `-J` and `+J`, respectively. This recovers the inherited #377 signed-Haar edge law from the explicitly source-labelled correction current; it **does not** infer cancellation at the actual seed `s=0`.

The only genuinely selected current estimate presently obtained is the existing #382 sparse-event bound: the normalized total current, with or without source/totient sectors, is `O(1/log N)` **for every seed**. No signed saving for ordinary digit bulk is proved.

## V. A quantitative Haar mixing/renewal statement, and its firewall

For the same Haar seed, correction events are rare `P(E_n)=r_n` and the source's `r_n<1/(2n²)` makes their total expected future count finite. In particular, for `N>=3`,
\[
\boxed{P_H(\exists n\ge N:E_n)\le\sum_{n\ge N}r_n<1/[2(N-1)].}\tag{12}
\]
The first Borel-Cantelli lemma implies Haar-almost-every physical seed has **only finitely many** corrections, without any independence assumption.

For `m>n`, write `k=m-n`. The full joint is an exact interval-overlap of the two original shrinking targets under the pure `x -> {16^k x}` map. The elementary full-grid-cell decomposition gives the mixing bound
\[
\boxed{|P_H(E_n\cap E_m)-r_nr_m|\le2r_m16^{-k}.}\tag{13}
\]
Moreover it is **exactly zero** if `1<=k<=L_n`, because a correction forces literal zeros through those times. This is a source-specific hard-core/weak-mixing law under the declared Haar reference, not a selected-zero-seed mixing claim.

## VI. Sharpness: why the universal N/log N saving cannot solve normality

The inherited #382 no-correction spacing proves, uniformly in all physical seeds, that
\[
\boxed{\limsup_{N\to\infty}\frac{E_s(N)\log N}{N}
\le\frac{\log16}{2},\quad E_s(N)=\sum_{n=3}^N E_n(s).}\tag{14}
\]
Here and below `log` is natural. Proof: discard the first `M=floor(N/log²N)` times; each later correction is separated from the next by at least `L_M+1=(2/log16)(log N-2loglogN)+O(1)` steps. Divide the maximal packing by N.

**K3-04 (constructive SHARPNESS, a same-source counterseed).** There exists a *single real physical preparation* `s_*` (generally not 0) with the original four-pole forcing such that
\[
\boxed{E_{s_*}(N)\sim\frac{\log16}{2}\frac{N}{\log N}.}\tag{15}
\]
**Construction:** define the inner interval `J_n=[T_n+r_n/4,T_n+3r_n/4] subset I_n`, width `r_n/2`. Choose `n_1>=8`; recursively choose the least integer `g_k>=1` with `16^g_k r_(n_k)>=8`, and let `n_(k+1)=n_k+g_k`. At each stage choose a closed inverse image under `x -> {16^(n_k-1) x}` of `J_(n_k)`, nested inside the previous inverse image. Existence follows because the image of the previous interval at the next clock has length at least `16^g*r_(n_k)/2>=4`, so it contains an entire integer translate of `J_(n_(k+1))`. Nested compact intervals have nonempty intersection; their diameters tend to zero. Call the resulting number `beta`, choose `s_*=(beta-pi)/16`. Then every `n_k` is an exact correction time. Since `g_k=2log_16 n_k+O(1)`, standard Stolz-Cesaro/integral comparison gives `#{k:n_k<=N}~(log16/2)N/log N`. Combine with universal upper bound (14) to obtain (15). This is a mathematically engineered **nonnormal counterseed**, not a claim about pi.

An executable exact-rational nested-cylinder construction independently certifies the first 160 prescribed events without approximating pi as a float. The infinite construction is the proof, not the finite test.

## VII. A conditional selected normality obstruction stronger than universal sparsity

**K3-05 (NORMALITY IMPLIES STRICTLY SUBMAXIMAL CORRECTION RATE).** For any physical seed `s` for which `beta=pi+16s` is normal to base 16,
\[
\boxed{E_s(N)=o\bigl(N/\log N\bigr).}\tag{16}
\]
Proof: an event `E_n` with `n>=sqrt N` forces a full pure-base-16 zero word of length `L_n >= log_16 N-O(1)` at positions `n,...,n+L_n-1`. These zero words are disjoint for distinct corrections. For each **fixed** K, a zero run of length L yields L-K+1 occurrences of the K-word `0^K`. Base-16 normality makes the total number of such K-word occurrences through `N+O(log N)` equal `N/16^K+o(N)`. Hence
\[
\limsup_{N\to\infty}\frac{E_s(N)\log N}{N}
\le\frac{\log16}{16^K}.
\]
Since K is arbitrary, the limsup is zero. The first `sqrt N` events are negligible on this scale. This is a rigorously conditional theorem **not** a proof that pi is normal. Its contrapositive gives a new quantitative nonnormality certificate from *excessive original-source corrections*.

**Counterexample against the converse/finiteness shortcut:** There are base-16 normal numbers `beta` with infinitely many correction events. Start from any base-16 normal beta and overwrite its hexadecimal digits on widely separated blocks `n_k,...,n_k+O(log n_k)` with a cylinder wholly inside `I_(n_k)`; choose, for example, superexponential n_k. Such a cylinder exists because `r_n>15/(64n²)`. The total overwritten positions up to N are o(N), preserving normality for every fixed block length. Every prescribed event still occurs. Thus even a *proof* of pi normality would not imply that the original BBP correction events are finite.

At the opposite extreme, the coherent same-forcing seed `s=-pi/16` makes `beta=0`, has no correction events for `n>=2`, and is blatantly nonnormal. Therefore `E(N)=0` is not sufficient for normality either.

## VIII. Actual selected pi verification and research boundary

At the original neutral `s=0`, all identities above apply with `beta=pi`. Direct exact-Fraction recurrence checks and independent Machin arctangent **rational intervals** verify the shrinking-window identity through n=44. This is a finite certificate, not an all-time no-event theorem; the full source's selected long-run digit statistics remain unknown.

**What this research genuinely adds:** (a) the exact shrinking-target characterization of all carry corrections, (b) the bounded-information lock and its exact zero-word posterior, (c) the signed 17-bin current with four complete q6 primitive/rank sectors, (d) sharpness of the existing all-seed sparsity exponent AND leading coefficient, and (e) a strictly stronger **conditional** normality obstruction for source-corrected events. The known source's small forcing and the distinguished zero seed are retained, but none of (a)-(e) establishes `sum_(n<=N)e(hU_n(0))=o(N)`.

**Next real proof gate:** Prove an independently sourced signed bound for the bulk sixteen ordinary carries, or a substantive bound `E_0(N)=o(N/log N)` for the actual zero-prepared pi selector, then recognize that even the latter is not sufficient for normality. The q3 Oily-log orientation instrument from sibling #383 can track the branch integer, but its invertible tomography and the total-current cancellation alone do not produce a signed Weyl saving.

**External context:** Bailey & Crandall (2001), *On the Random Character of Fundamental Constant Expansions*, formalize the still-open dynamics hypothesis. Lagarias (2001), *On the Normality of Arithmetical Constants*, warns that generic orbit bridges do not prove the needed distribution. Standard first Borel-Cantelli, Bernoulli coding, and shrinking-target results are classical; no scholarly originality priority is asserted for the basic methods.
