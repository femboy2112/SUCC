# Original-zero BBP: two signed carry currents and the analytic-boundary obstruction

**2026-11-21 · isolated, additive SUCC research · proposed stacked child of #684.** The source is **exactly**
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad
x=\sum_{j\ge1}16^{-j}r(j)=\pi/16.
\]
The final equality imports the classical BBP identity. For arbitrary **explicitly changed** seed `s`, put `U_n(s)=16^n(s+P_n)`; no changed seed is the authentic target. Prior SUCC #652 proves a distinct digit-mask borrow transfer; #684 proves source-lag and singular seed-derivative results. The results here split *source-kick* carry from *analytic completion* carry and give a signed coboundary, a uniform kick-carry sparsity theorem, and an independent counterexample showing exactly why none of this proves R0.

## TCD-01 — The native four-pole source has all strictly oriented moment differentials (PROVED PAPER; classical positivity, exact source specialization)

The original source factorization is `Q(t)=4-2t³-t⁴-t⁵=(1-t)H(t)` with `H(t)=4+4t+4t²+2t³+t⁴>0` on `[0,1]`. Set `u=t⁸`; then
\[
r(n)=\int_0^1u^{n-1}\,d\mu(u),\qquad
d\mu(u)=\frac{Q(u^{1/8})}{8u^{7/8}}du.
\]
This is a positive, nonatomic measure charging every open subinterval of `(0,1)`. For every `n>=1,k>=0`, with `Delta r(n)=r(n+1)-r(n)`, the exact `k`th chronological differential is
\[
\boxed{(-1)^k\Delta^k r(n)=\int_0^1u^{n-1}(1-u)^k\,d\mu(u)>0.}
\]
The source therefore admits a complete strict Hausdorff-moment signature; it is neither inferred from digits nor from the Gaussian observer. For every `m>=1`, the *native innovation* Hankel determinant is strictly positive:
\[
\boxed{\det[r(n+i+j)]_{i,j=0}^{m-1}
=\frac1{m!}\int_{(0,1)^m}\prod_{a<b}(u_b-u_a)^2\prod_{a=1}^m u_a^{n-1}d\mu(u_a)>0.}
\]
Proof: write the Gram matrix of monomials `1,u,...,u^(m-1)` in the positive weighted measure; symmetrize its determinant (Andreief/Vandermonde identity). In particular the signed native source hierarchy has infinite exact Hankel rank. This is a statement about forcing, NOT about π's temporal phase Hankel rank (already handled separately in SUCC's HBC work).

For each **fixed** `k`, a beta-integral or Laplace endpoint expansion at `t=1`, using `H(1)=15`, yields
\[
\boxed{(-1)^k\Delta^k r(n)\sim\frac{15(k+1)!}{64 n^{k+2}}\quad(n\to\infty).}
\]
The `k` is fixed before the limit; no uniform-in-derivative-order bound is asserted. Mutation `Q+(1-t)²` also has positive real support, so this positivity hierarchy is NOT itself an original-source identity test; original poles, zero seed and p-primary labels are retained separately.

## TCD-02 — Two distinct causal crossings and their **signed exact coboundary** (PROVED ALL CLOCKS)

For any seed `s`, take `phi_n={U_n(s)}`, `T_n=sum_(k>=1)16^(-k)r(n+k)` (the unchanged authentic tail) and `theta_n={U_n(s)+T_n}={16^n(x+s)}`. Define the analytic crossing (the mathematical future head)
\[
\delta_n=\lfloor\phi_n+T_n\rfloor\in\{0,1\},\qquad
\theta_n=\phi_n+T_n-\delta_n.
\]
The source phase transport has `T_n=16T_(n-1)-r(n)`. For `n>=2`, since `0<r(n)<1`, define the source-kick crossing (the finite forward head)
\[
b_n=\lfloor16\phi_{n-1}\rfloor,\quad
\kappa_n=\lfloor16\phi_{n-1}+r(n)\rfloor,\quad
e_n=\kappa_n-b_n\in\{0,1\}.
\]
`b_n` is a *pre-forcing raw radix digit*, not the completed π digit. The selected completed digit is `d_n=floor(16 theta_(n-1))`. Exact substitution, **including the integer lift**, gives
\[
\boxed{\quad d_n=b_n+e_n+\delta_n-16\delta_{n-1}\quad(n\ge2).}
\]
Proof: `16theta_(n-1)=16phi_(n-1)+16T_(n-1)-16delta_(n-1)=kappa_n+phi_n+T_n-16delta_(n-1)=kappa_n+theta_n+delta_n-16delta_(n-1)`, then take floors. This is not an equality merely modulo 16; the signed coefficient `-16` is essential. The source and completion crossings belong to different observer heads and cannot be replaced by a single positive energy count.

For a shell `[B,2B)` the **signed differential transfer** telescopes exactly:
\[
\sum_{n=B}^{2B-1}(d_n-b_n)
=\sum_{n=B}^{2B-1}e_n
-15\sum_{n=B}^{2B-2}\delta_n
+\delta_{2B-1}-16\delta_{B-1}.
\]
(The same formula holds for arbitrary integer windows with corresponding endpoints.) This is a genuine original-zero identity at `s=0`; it also holds for declared changed-seed controls, which is why the anchor must be kept for claims about π.

## TCD-03 — Source-kick events have an explicit logarithmic **refractory period** (PROVED EVERY SEED)

The authentic forcing is positive, strictly decreasing, and `r(n)~15/(64n²)`; also `r(n)<1` for `n>=2`. If `e_n=1`, then the new raw fractional state satisfies `0<=phi_n<r(n)`. For every `j>=0`, using positivity, decreasing forcing and the fact that a fractional part never exceeds its unreduced positive argument,
\[
\boxed{0\le\phi_{n+j}<r(n)\frac{16^{j+1}-1}{15}.}
\]
Define the **rationally computable** shell cooldown, for `B>=2`, as
\[
L(B)=\max\bigl\{\ell\ge0:\ r(B)(16^{\ell+1}-1)/15<1\bigr\}.
\]
For every source-kick event at `n>=B`, the next `L(B)` clocks satisfy `e_(n+1)=...=e_(n+L(B))=0`. Indeed for `1<=h<=L(B)`, the previous bound gives `16phi_(n+h-1)+r(n+h)< r(n)(16^{h+1}-1)/15 <= r(B)(16^{L(B)+1}-1)/15<1`. Thus the source kick cannot produce another digit carry during the cooldown. Consequently, for **every seed, every integer B>=2**,
\[
\boxed{\#\{n\in[B,2B):e_n=1\}\le \left\lceil\frac{B}{L(B)+1}\right\rceil,\qquad L(B)=2\log_{16}B+O(1).}
\]
In particular `B^-1 sum e_n=O(1/log B)` uniformly in the initial seed. This result uses the *actual* monotone original four-pole forcing; it is not the raw/completed selected-mask transfer already proved in #652. A similarly decaying positive forcing can enjoy the same structural bound, so this result alone does not authenticate the π endpoint.

## TCD-04 — The source-kick and analytic-tail crossings are mutually exclusive, with oriented near-zero consequences (PROVED)

For all `n>=2` the authenticated positive tail satisfies `0<T_n<r(n+1)/15<r(n)/15`. If `e_n=1`, `phi_n<r(n)` and hence
\[
\boxed{\delta_n=0,\qquad 0<\theta_n<r(n)+T_n<\frac{16}{15}r(n).}
\]
The strict bound `(16/15)r(2)<1` and source monotonicity justify `delta_n=0` for all later clocks. Conversely `delta_n=1` forces
\[
\boxed{e_n=0,\qquad0\le\theta_n<T_n<r(n+1)/15.}
\]
Both event types therefore select exceptionally small positive completed phases at late clocks, but with **opposite raw seam orientations**: source kick exits near raw zero, while analytic tail carry enters from just below raw one. For large n either event forces a (source-computable) block of succeeding zero hexadecimal digits, of length asymptotic to `2 log_16 n` when the event occurs. This conditional digit prediction uses only rational forcing/tail bounds, not a precalculated digit. The events do **not** exhaust all near-zero orbit states: an ordinary digit run can have neither event.

## TCD-05 — Generic seeds have **eventual exact digit agreement**, not just weak-law agreement (PROVED, ensemble only)

Give the homogeneous seed `s` uniform Haar measure on `R/Z` while keeping the exact same forcing and tail. The maps `s -> {U_(n-1)(s)}` and `s -> {U_n(s)}` preserve Haar measure, so for every `n>=2`
\[
\boxed{\Pr_s(e_n=1)=r(n),\qquad\Pr_s(\delta_n=1)=T_n.}
\]
Both sums over clocks converge, since `r(n)=O(n^-2)` and `T_n=O(n^-2)`. By the first Borel-Cantelli lemma (no independence assumed), for almost every **changed seed** `s`, both types of event occur only finitely many times. The signed identity TCD-02 then gives the surprisingly strong statement
\[
\boxed{\exists N(s)<\infty:\quad d_n(s)=b_n(s)\quad\forall n\ge N(s)\quad\text{for almost every }s.}
\]
One explicit tail probability bound is
`Pr(exists n>=B with e_n=1 or delta_n=1) <= sum_(n>=B)(r(n)+T_n)=O(1/B)`, with constants calculated from the unchanged source. **This is ensemble/measure-theoretic; the authentic fixed seed `s=0` is a single point and is not covered by the almost-everywhere quantifier.** A seed-independent absolute carry-count theorem is TCD-03; generic eventual stabilization is stronger but not selected-point information.

## TCD-06 — Exact source certification through 16,000 clocks (FINITE OBSERVED, not asymptotic)

A stdlib `fractions.Fraction` replay from literal `U0=0` through clock 16,000 performs no floating-point decisions. At every clock `n>=2` it tests `e_n=0` exactly. At every clock `n>=1`, `phi_n+r(n+1)/15<1` proves `delta_n=0` using a strict analytic upper bound rather than a fitted π approximation. Therefore `d_n=b_n` for n=2..16000 and `d_1=kappa_1=3` precisely; **16,000 actual π/16 hexadecimal digits** are thereby certified by the unchanged source and its analytic tail, conditional on the classical BBP identity.

The reproducible record contains the first and last 32 digits, a SHA256 of all 16,000 digit symbols, complete event and ambiguity counts, and four **predeclared** quarter-sector shell lower bounds. For each `B∈{128,512,2048,8000}`, with `q_n=1_{theta_n∈(1/4,3/4)}` and `A_B=B^-1 sum_(n=B)^(2B-1)(1-cos2πtheta_n)`, the exact digits certify
\[
A_B\ge B^{-1}\sum q_n=
\begin{cases}
66/128,&B=128,\\262/512,&B=512,\\1017/2048,&B=2048,\\3940/8000,&B=8000.
\end{cases}
\]
These are **finite signed-source certificates only**, with no extrapolation to all large shells. The independent implementation recomputes 4,096 clocks via an algebraically independent rational expression for `r(n)`, and directly checks selected phase states using modular BBP terms. None of these numerical tests is claimed to prove irrationality, normality, or R0.

## TCD-07 — A strict hostile control: **even if both carry types disappear, R0 need not follow** (PROVED countermodel)

Define a nonnormal real `beta=Σ_(k>=1)16^(-n_k)` where `n_1=16`, `n_(k+1)=n_k+ceil(log_16(n_k+1))` (a deterministic, growing-gap 0/1 digit word). The gaps diverge but are at most `log_16(n+1)+1`; digits `1` have zero asymptotic density. Hence the radix orbit of beta spends density one at arbitrarily small phases and `A_B(beta)->0`. Yet for every sufficiently large n, the next nonzero digit lies at distance at most `ceil(log_16(n+1))+1`, giving `theta_n(beta)>=c/(n+1)` for an absolute `c>0`. The unchanged original BBP tail satisfies `T_n=O(n^-2)`, so `theta_n(beta)>T_n` eventually.

Choose the **explicitly changed seed** `s=beta-x` in the original forced recurrence. Then `U_n(s)+T_n=16^n beta`, so `delta_n(s)=0` for all sufficiently large n; TCD-03 separately gives `e_n(s)` density zero. Nevertheless `R0(beta)` **fails**. This kills both shortcuts: `analytic completion carry rare ⇒ R0`, and `both signed carry corrections negligible ⇒ R0`. The source-only forcing and its Mellin differentials still agree with the authentic forcing; the root/seed head correctly rejects `s!=0`. The remaining signed distribution of the *regular* digit head is load-bearing.

A second critical control is `s=-x`: then `U_n(s)=-T_n`, so `phi_n=1-T_n` and `delta_n=1` at **every** clock, while the completed phase and every π-phase digit are zero. For n>=2, `kappa_n=b_n=15` and `e_n=0`. The exact identity reads `0=15+0+1-16`. This demonstrates why source-kick sparsity must never be transferred to the analytic completion crossing without the literal `U0=0` anchor.

## TCD-08 — The precise upgraded π-normality proof interface (OPEN)

The universal source-kick channel is now quantitatively controlled, and the source's all-order differential signature is strict. The original zero seed fixes one exact rational orbit and a nonzero analytic cofactor at every time. **What remains unproved is the signed distribution of ordinary radix digits and, separately, the zero-seed shrinking-target behavior `delta_n`.** The latter is not by itself equivalent to R0 (TCD-07). To advance R0, derive from the exact four-pole source, root anchor, prime-square marks `4/p²`, the complete integer winding and the oriented cofactor a **uniform all-large-integer-shell constraint on the regular quarter-sector/digit head**, not merely a generic seed/derivative statement. A candidate must survive `s=-x`, the changed-seed sparse-word TCD-07, the matched-jet mutant `Q+(1-t)^2`, fixed-frame Gaussian attenuation, and the differentially signed prime swap controls `p=7,79,131` of #684.

## TCD-10 — An explicit original-source all-shell R0 lower bound with a paid forcing-carry cost (PROVED CONDITIONAL BRIDGE)

Retain the *literal zero seed*, original forcing, all integer carries and analytic tail. Define, for **every integer B>=2**, the raw rational quarter-sector count

\[
H_B^{\rm raw}=\frac1B\sum_{n=B}^{2B-1}\mathbf 1_{\{4\le b_{n+1}\le11\}},\qquad
D_B=\frac1B\sum_{n=B}^{2B}\delta_n.
\]

Let `L(B)` be the source-computable positive cooldown from TCD-03. The actual completed R0 energy satisfies the **nonasymptotic inequality**

\[
\boxed{\mathcal A_B=\frac1B\sum_{n=B}^{2B-1}\bigl(1-\cos(2\pi\theta_n)\bigr)\;\ge\;
H_B^{\rm raw}-\frac{\lceil B/(L(B)+1)\rceil}{B}-2D_B.}
\]

**Proof.** On clocks `n>=B`, the signed integer identity TCD-02, shifted to `n+1`, gives
`d_(n+1)=b_(n+1)+e_(n+1)+delta_(n+1)−16delta_n`. If all three exceptional bits `e_(n+1),delta_n,delta_(n+1)` are zero, the completed digit equals the raw digit exactly. Thus, for the quarter-sector detector `q_n=1_{theta_n in (1/4,3/4)}`,

\[
q_n\ge\mathbf1_{\{4\le b_{n+1}\le11\}}-e_{n+1}-\delta_n-\delta_{n+1}.
\]

The completed point `x=pi/16` is irrational by the classical irrationality of pi, so no `theta_n` is a digit boundary. Moreover `1−cos(2pi theta_n)>=q_n`. Sum over `[B,2B)`, apply TCD-03 to source-kicks on `[B+1,2B]` (all indices are >=B), and bound `Σ_(n=B)^(2B−1)(delta_n+delta_(n+1)) <= 2Σ_(n=B)^(2B)delta_n`. This gives the formula. If desired, the right side may be clipped at zero, because `A_B>=0` by definition. No probabilistic assumption or *additional* source is used. QED.

**New exact sufficient criterion, not yet established:** If the original zero-seeded arithmetic satisfies `liminf_(B→∞) H_B^raw > 2 limsup_(B→∞) D_B` (where the latter limsup exists as an extended finite value in `[0,1]`), then the proven `kick_count/B→0` gives `liminf A_B>0`, hence R0. This is a sufficient *raw-quarter versus analytic-crossing* source contract, not an equivalent reformulation and not an already-proved lower density of the raw quarter-sector head. In particular neither positivity of the native source Hankel matrices nor a bound on the source kick alone pays it. The exact countermodel TCD-07 has negligible kick and completion crossings but insufficient raw quarter mass; the wrong-seed lock TCD-07 has dense completion crossing.

A bounded exact implementation `conservative_r0_lower(B,raw_quarter_hits,completion_hits)` returns the source-theorem lower bound (clipped at zero); its new test verifies all intermediate raw digits and exact completed digits independently from rigorous finite source interval enclosures for the original and changed-seed controls. **This gives a source-derived all-B inequality but not a uniform positive lower bound**. R0 and full base-16 pi normality remain OPEN.

**Ledger:** TCD-01–05, TCD-07 and TCD-10 are paper-proved within their declared mathematical models; TCD-06 is a finite, reproducible arithmetic certificate; TCD-08 and both π normality and the R0 rung remain **UNVERIFIED/OPEN**. No physical information/energy conservation, quantum superfluid, or Collatz termination claim follows.
