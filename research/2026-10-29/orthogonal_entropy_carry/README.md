# Operation Kepler II — sparse directional carry corrections and orthogonal entropy observers

**Research-only, 2026-10-29.** Direct additive continuation of the ORIGINAL four-pole source through SUCC [draft PR #380](https://github.com/femboy2112/SUCC/pull/380), which already proves asymmetry of directed source KL and sparse exceptional carry `16`. Related, unmerged siblings: [PR #379](https://github.com/femboy2112/SUCC/pull/379) (Kepler/Gamma normal form), [PR #378](https://github.com/femboy2112/SUCC/pull/378) (origin-free normality observer), [PR #375](https://github.com/femboy2112/SUCC/pull/375) (Eisenstein observer), [PR #271](https://github.com/femboy2112/SUCC/pull/271) (all 4-bit Walsh interactions), [PR #373](https://github.com/femboy2112/SUCC/pull/373) (pointed zero preparation). This round does **not** claim to discover their inherited theorems, identify physical thermodynamic heat, or prove π-normality/RH. Main, four signed poles, `U_0=0`, imports and claim registry remain unchanged.

## 0. Steelman / Kepler versus epicycles

A successful observational representation may fail to identify a simple underlying law. The user's proposal is stronger than stochastic digit-modeling: realize a *directed path* and account for the arithmetic information added by its selection, then compare genuinely independent observation directions. The minimal test is to establish a source-selected dynamical constraint **that holds even without assuming the desired normality limit**, and to check whether orthogonal entropic observers carry new or redundant information. This round establishes an all-seed **deterministic carry-correction sparsity law**, its subextensive symbolic entropy, and a complete (but unproved-to-vanish) selected-carry normality criterion.

The historical epicycle/ellipse comparison is only a methodology analogy. No physical model of planetary dynamics is imported.

## 1. Exact source passport and the ordinary digit/carry distinction

For integer `n>=1`, the only forcing used here is

\[
r_n=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r_n.
\]

For **any** initial seed (used only for hostile tests), put `x_n={U_n}` and, for each step,

\[
d_n=\lfloor16x_{n-1}\rfloor\in\{0,\ldots,15\},\qquad
\kappa_n=\lfloor16x_{n-1}+r_n\rfloor,\qquad
x_n=16x_{n-1}+r_n-\kappa_n.
\]

Call `E_n=1[κ_n != d_n]` the **forcing-induced correction**. For `n>=2`, `0<r_n<1`, and hence `κ_n-d_n` is exactly **zero or one**. (`r_1=47/15>1` is a separately retained transient.) A correction at any of the 16 boundaries, including but not limited to `κ=16`, obeys `0<=x_n<r_n` exactly, by floor arithmetic.

This is a relation between the literal source carry and the **unforced digit at the same actual state**; it does not equate those digits with an independently invented random source or assume a decimal/hexadecimal digit-frequency law.

## 2. New all-boundary zero-run theorem — the source pays for each intervention

**OE-01 (original-four-pole source bound).** For all integers `n>=3`,

\[
0<r_n<\frac1{2n^2}.
\]

The second strict inequality has an exact positive-integer certificate:

\[
\frac1{2n^2}-r_n
=\frac{P(n)}{2n^2(2n-1)(4n-1)(8n-7)(8n-3)},
\]

where

\[
P(n)=272n^4-846n^3+680n^2-206n+21
\]

and, setting `m=n-3>=0`,

\[
P(m+3)=272m^4+2418m^3+7754m^2+10408m+4713>0.
\]

The positivity and strict decrease of `r_n` also follow from the original source's positive Laplace representation; no altered forcing is introduced.

**OE-02 (ALL correction classes, every seed).** Fix `n>=3` with `E_n=1`. Put

\[
L(n)=\max\{\ell\in\mathbb N_0:16^\ell\le n^2\}=\lfloor\log_{16}(n^2)\rfloor.
\]

Then the next `L(n)` **literal carries** are exactly zero:

\[
\boxed{\kappa_{n+1}=\kappa_{n+2}=\cdots=\kappa_{n+L(n)}=0.}
\]

The bare digits at those positions are also zero, so **no new correction** occurs within that interval.

**Proof.** At the event, `x_n<r_n`. If the next `j` carries vanish, monotonicity `r_{n+i}<=r_n` gives

\[
x_{n+j}<\left(16^j+\frac{16^j-1}{15}\right)r_n<\frac{16^{j+1}}{15}r_n.
\]

For `j+1<=L(n)` the *next* unwrapped value satisfies

\[
16x_{n+j}+r_{n+j+1}
<\left(\frac{16^{j+2}}{15}+1\right)r_n
<\frac8{15}+\frac1{2n^2}<1.
\]

This proves the carry is zero by induction, including the equality boundary `16^(j+1)=n²`. Unlike PR #380's exceptional-only statement, the proof never assumes the corrected carry was `16`; it needs only `κ_n>d_n`.

**OE-03 (density and explicit horizon).** Define `E(N)=#{1<=n<=N:E_n=1}`. For any integers `3<=M<=N`, the zero runs forbid corrections at distances `<=L(M)` after each correction at or after `M`. Hence

\[
\boxed{ E(N)\le M+\left\lfloor\frac{N-M}{L(M)+1}\right\rfloor. }
\]

Taking `M=ceil(sqrt N)` (for N>=9) shows `E(N)=O(N/log N)` **uniformly in the seed**. This is a rigorous all-horizon constraint derived from the actual source. It does **not** imply that any of the ordinary digit values 0..15 has uniform density.

The source-bound `1/(2n²)` is stronger than the earlier rough `15/(16n²)` and is essential to the presented exact `L(n)` endpoint proof.

## 3. Realized directional weighting has subextensive correction information

Repair the literal carry by the declared finite observation `c_n=κ_n mod16`. Except for the finite time-one transient, `c_n` differs from the unforced `d_n` exactly at `E_n=1`. Let `P^c_(N,k)` and `P^d_(N,k)` be the empirical distributions of length-k consecutive words in positions `1,...,N`, using the same start-index convention.

**OE-04 (all block observables, simultaneously).** For all `1<=k<=N`,

\[
\boxed{\operatorname{TV}(P^c_{N,k},P^d_{N,k})
\le \min\left(1,\frac{k E(N)}{N-k+1}\right).}
\]

Proof: couple the distributions by choosing the *same* uniform starting index. A discrepancy requires at least one corrected coordinate in that window, and each correction lies in at most `k` windows. This is valid uniformly over **all** events, including totient/cototient residue filters, and over all `16^k-1` nontrivial Walsh characters.

For any real local potential `f` with `|f(word)|<=B` and empirical log-partition

\[
\mathcal P_{N,k}(f;P)=\log \sum_w P(w)e^{f(w)},
\]

we obtain by the same coupling and `e^(-B)<=Z<=e^B`,

\[
\boxed{ |\mathcal P_{N,k}(f;P^c)-\mathcal P_{N,k}(f;P^d)|
\le 2e^{2B}\operatorname{TV}(P^c,P^d). }
\]

This is the exact **arithmetic weight of realizing the corrected direction** within a declared bounded Gibbs observation. Its per-time effect vanishes for every fixed `k,B`, and even for `k=o(log N)` with fixed `B`. This is mathematical information/pressure, **not** physical heat/work absent a specified apparatus.

**OE-05 (Shannon entropy continuity).** Let `δ=TV(P^c,P^d)`, and let `h2` denote binary entropy in nats. By coupling, for `δ<=1-16^(-k)`,

\[
|H(P^c)-H(P^d)|\le h_2(\delta)+\delta\log(16^k-1).
\]

For larger δ use the trivial `<=k log16`. Thus for `k=o(log N)`, the **per-symbol entropy difference** tends to zero. Moreover the number of binary correction masks with at most E(N) events obeys

\[
\#\mathrm{masks}\le\sum_{j=0}^{E(N)}\binom Nj
\le \exp\{N h_2(E(N)/N)\}
=\exp\left(O\left(\frac{N\log\log N}{\log N}\right)\right)
\]

for sufficiently large N, where `E(N)/N<=1/2`. This is a **combinatorial uncertainty bound**, not the Shannon entropy of the one deterministic trajectory (a point mass has entropy zero). Realizing the forcing direction changes the data only through a subextensive correction description **in this specific observation channel**.

## 4. Actually orthogonal observers: four-bit Walsh versus entropy direction

Let `p(d)` be a one-symbol empirical law on `{0,...,15}`. Under the uniform **reference** `u(d)=1/16`, the sixteen Walsh characters `W_A(d)=(-1)^popcount(A&d)` are orthogonal:

\[
\sum_{d=0}^{15}W_A(d)W_B(d)=16\delta_{AB}.
\]

Set `m_A=E_p W_A`. The exact unnormalized chi-square divergence has the **Parseval identity**

\[
\boxed{\chi^2(p\Vert u)=\sum_{A=1}^{15}|m_A|^2.}
\]

This bridges genuinely orthogonal four-bit observations to the entropic deficit

\[
D_{\rm KL}(p\Vert u)=\log16-H(p)
\quad\text{and}\quad
2TV(p,u)^2\le D_{\rm KL}(p\Vert u)\le\log(1+\chi^2(p\Vert u)).
\]

Every Walsh moment changes by at most `2E(N)/N` upon carry repair. **Orthogonal under the reference** does *not* mean independent under the selected empirical source. The known SUCC parity countermodel, uniform on the eight even-parity 4-bit words, has all Walsh moments of orders 1,2,3 equal to zero, but full four-bit moment `m_15=1`, `KL=log2`. Its exact control is replayed here; see inherited [PR #271](https://github.com/femboy2112/SUCC/pull/271). Therefore the four-body channel must not be thrown away.

## 5. A complete entropy-normality criterion in literal carries (NOT a proof of its limit)

For the authentic zero-seeded source the inherited tail identity is

\[
x_n=\{16^{n-1}\pi-T_n\},\qquad T_n\downarrow0.
\]

Therefore equidistribution of `x_n` is equivalent to base-16 normality of π (inherited from the original BBP source and Weyl criterion).

**OE-06 (carry code ⇔ circle normality, exact domain).** For *any* fixed seed in this authentic forcing and the corrected carry word `c_n=κ_n mod16`, the following are equivalent:

1. The source circle phases `x_n` are equidistributed in `[0,1)`.
2. For every fixed `k>=1`, empirical consecutive k-block frequencies of `c_n` tend to `16^(-k)`.
3. For every fixed `k>=1`, empirical k-block entropic deficits `D_(N,k)=k log16-H(P^c_(N,k))` tend to zero.

**Proof (2→1).** By OE-03/04, bare digit k-block statistics match repaired carry k-block statistics asymptotically. On a start index whose next k positions have no correction, iterate the **actual** recurrence backwards:

\[
x_n=\sum_{j=1}^k16^{-j}d_{n+j}+
16^{-k}x_{n+k}-\sum_{j=1}^k16^{-j}r_{n+j}.
\]

The last two terms have absolute size at most `16^(-k)+r_{n+1}/15` (using monotonicity), uniformly on the good windows. The bad windows have density zero. If all k-block laws are uniform, empirical expectations of any Lipschitz function of `x_n` approach its regular base-16 Riemann sums to within `O(16^(-k))`; let k→∞. This yields Haar.

**Proof (1→2).** For each fixed k, the asymptotically unforced dynamics `x_{n+1}={16x_n+r_{n+1}}` has future k-digit bare itinerary equal to the standard base-16 cylinder itinerary of `x_n`, except when `x_n` lies in shrinking neighborhoods of the finite set of k-depth cylinder boundaries. Since the phases are Haar-equidistributed, those neighborhoods have limiting density zero; the standard 16-ary cylinder has Haar mass `16^(-k)`. OE-04 transfers the result to `c`. Finally `(2⇔3)` is the unique maximizer property of Shannon entropy on a finite alphabet, equivalently positivity of KL to uniform.

For `U0=0`, **these equivalent assertions are precisely the open π-normality problem**, not a new proof. They provide an *origin-free, thermodynamic observation criterion on the actual literal carry history* without assuming random generation.

Define the single convergent thermodynamic energy using **cyclic** empirical k-block distributions (a cyclic/noncyclic discrepancy is at most `O(k/N)` for fixed k):

\[
\boxed{ \mathfrak F_N=\sum_{k=1}^\infty 2^{-k}\,
\frac{D_{\rm KL}(P^c_{N,k,\rm cyclic}\Vert u_{16^k})}{k}. }
\]

Every term lies in `[0,log16]` after division by k, so `0<=F_N<=log16` and uniform summability applies. Thus

\[
\boxed{\mathfrak F_N\to0 \iff\pi\text{ is base-16 normal}.}
\]

This criterion is **normality-complete** but its zero-seeded value is **UNVERIFIED at infinity**. It should not be presented as an independent entropy estimate. In particular, a random sample from an auxiliary Pascal/Gamma carrier is no substitute for the true source-selected carry law.

## 6. Two temporal directions can agree while hiding irreversibility

For any cyclic finite word of length N, both forward and backward conditional k-letter entropies are **identically** `H_(k+1)-H_k`, because the k-letter prefix and suffix distributions coincide by cyclic stationarity. Therefore simple equality of the two scalar entropy rates is **NOT** evidence for normality or thermodynamic reversibility; this identity holds even for a constant word or a nonnormal de Bruijn periodic word.

A genuine direction-sensitive statistic must retain orientation. Example: a three-state stationary Markov chain with clockwise transition probability `3/4`, counterclockwise `1/8`, and stay `1/8` has uniform stationary distribution and equal forward/backward conditional Shannon entropy, yet path-reversal relative entropy production equals

\[
\boxed{\sigma=\left(\frac34-\frac18\right)\log\frac{3/4}{1/8}
=\frac58\log6>0.}
\]

This is a **different declared source**, a calibrated countermodel, not a claim about BBP's actual physical entropy production. It demonstrates why orientation and complete joint histories matter more than separate scalar entropy measurements.

A periodic de Bruijn cycle of order K on 16 symbols is **exactly uniform in every block test of depth ≤K** but is globally nonnormal when repeated forever. It can have zero observed entropy deficits at all tested depths while failing the actual infinite criterion. That is the required finite-to-global negative control, inherited from #375 and reexecuted for K=2.

## 7. What survives the Kepler test, and the genuine next proof debt

**New within this research round:** The universal all-boundary correction-zero-run theorem (OE-02), all-seed correction-density saving, finite-block/pressure/entropy transport, all-band Walsh robustness, and the selected literal-carry entropy criterion. These are mathematical consequences of the authentic forcing plus standard coding/probability identities. Scholarly originality is NOT verified. The earlier carry-16-only zero density, all-source directional KL, and Gamma/Oily marking are **inherited**, not rebranded.

**What remains OPEN:** No bound on the time distribution of the ordinary `d_n in 0..15`. Zero density of the correction mask is compatible with every normality and nonnormality scenario, including the coherent changed seed. The missing source-specific signed estimates on original zero-prepared carries remain exactly the user's π frontier. Our tests include a forcing-constant mutant that causes a correction **every** step, proving the summable-decay assumption matters, and a four-bit parity model that defeats lower-order Walsh-only observation.

Next discriminator: derive a quantitative all-scale signed bound or entropy-deficit bound for the **bare radix digit process itself**, from the actual four poles and zero seed—not from the repair operation or from a random-origin ensemble. Keep the full 16 bins and 4-bit interactions, test the 15-torsion aliases and coherent same-forcing seed, and validate any improved asymptotic estimate in independent exact arithmetical code.
