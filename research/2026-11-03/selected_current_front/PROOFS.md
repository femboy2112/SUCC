# Operation Selected Current: gauge-stable BBP branch imbalance and source Gamma transport

**Date:** 2026-11-03. **Authority:** elementary paper derivation, exact rational source and an independent piecewise-constant bin-origin integration oracle. No new Lean theorem, original π-normality proof or independent human referee. **Parent:** draft SUCC PR #488 at `f47e3768631cd1628c1390d529811c911e0f6443`, with preregistration committed before fresh holdouts. **Immutable** source: 

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

For integer A>=1 put `x_n={U_n}` for n in `[A,2A)` and `X_n=16^n π/16=U_n+T_n`. Inherited SUCC original-source theorems give `0<T_n<1/(64 n²)` and strictly decreasing positive T_n for n>=1. The **actual original real arithmetic** is always evaluated from the exact rational recurrence, not from imported π digits. Write `||x||` for circle distance to the nearest integer and `k_q(x)=(1-q||x||)_+` for integer q>=2.

## SC-01 — common-origin translation average is an exact original-source triangular energy

For a *single shared origin* `τ∈R/Z`, let `b_(q,τ)(x)=floor(q*{x+τ})` and let

\[
E_{A,q}(τ)=\frac{q}{A^2}\sum_{n,t=A}^{2A-1}{\bf1}_{\{b_{q,τ}(x_n)=b_{q,τ}(x_t)\}}.
\]

Only the observational bin origin changes, not the orbit `x_n`. A pair with circular displacement δ in `[0,1/2]` occupies the same translated q-bin for a proportion `(1-qδ)_+` of origins τ: when δ<1/q the forbidden origins consist of q boundary arcs of total length qδ, while if δ>=1/q one translated bin cannot contain the pair. The half-open endpoint choices affect only finitely many origins of measure zero. Thus **for every finite source cloud and every q>=2**

\[
\boxed{J_{A,q}:=\int_0^1 E_{A,q}(τ)dτ
=\frac q{A^2}\sum_{n,t=A}^{2A-1}k_q(x_n-x_t).}\tag{SC-1}
\]

No Galois or inverse-branch averaging is used. `J` is translation-invariant as a function of the point cloud, and `1<=J<=q`; both inequalities also follow from source-independent histogram Cauchy and positivity. It is a *selected* real-circle energy, not an ensemble average over the source.

## SC-02 — exact positive Fourier representation (classical B-spline)

The periodic tent kernel has Fourier coefficients, for h integer,

\[
\widehat{k_q}(h)=\int_{-1/q}^{1/q}(1-q|x|)e^{-2\pi ihx}dx
=\frac1q\left(\frac{\sin(\pi h/q)}{\pi h/q}\right)^2,
\]

with the continuous value at h=0 understood as `1/q`. The Fourier series is absolutely convergent (`O_q(h^-2)`). Setting `c_A(h)=A^-1 sum_(n=A)^(2A-1)e(hU_n)` gives

\[
\boxed{J_{A,q}=1+\sum_{h\ne0}
\operatorname{sinc}^2(\pi h/q)|c_A(h)|^2.}\tag{SC-2}
\]

All terms are nonnegative. This is the familiar triangle/B-spline convolution Fourier identity and should not be advertised as original Fourier theory. **It is not a signed saving**: for a point mass, the sum equals `q-1`.

Reference: Grafakos, *Classical Fourier Analysis*, martingale/Haar square-function chapter; any elementary Fourier analysis treatment of the triangular window has the sinc-square transform.

## SC-03 — recover the ORIGINAL canonical 16-adic partition from translated energy

Let m>=4 be EVEN and put q=m/2. Whenever two points lie in the **same canonical m-cell**, their circle distance is <1/m=1/(2q), hence `k_q(x-y)>1/2`. Therefore

`1_(same canonical m-cell) <= 2 k_q(x-y)` for every pair (and zero pairs are trivial).

Summing proves the **universal deterministic inequality**

\[
\boxed{E_{A,m}(0)\le4J_{A,m/2}.}\tag{SC-3}
\]

This holds for every finite cloud, including the original source and coherent hostile clouds. We do not choose a lucky origin and we do not average the source. The constant 4 is sufficient, not asserted optimal.

For the inherited explicit logarithmic mesh `m_A=16^K`, `K=floor(log_16(log A))` at all sufficiently large dyadic A, m_A is even and grows with log A. If the **original selected source** can be proved to satisfy `J_(A,m_A/2)=o(K)`, then (SC-3) yields the exact ORIGINAL `E_(A,m_A)=o(log m_A)` premise of SUCC #476, and its already-proved Fejér/Ward theorem implies base-16 normality of π. **The J bound is OPEN.** It is not produced by SC-1..SC-3.

## SC-04 — strict source-selected Gamma coupling without bin-boundary exceptions

Let `\mathcal J_q(X)` denote the same triangular pair energy on the completed points `X_n`, n in `[A,2A)`. Because `k_q` is q-Lipschitz under circle distance and `X_n-X_t=(U_n-U_t)+(T_n-T_t)` modulo one,

\[
|J_{A,q}(X)-J_{A,q}(U)|\le\frac{q^2}{A^2}
\sum_{n,t=A}^{2A-1}|T_n-T_t|.
\]

The TRUE original T_n is positive and strictly decreasing. Group positive differences by d=t-n>0. The chronological telescope is

\[
\begin{aligned}
\sum_{n=A}^{2A-1-d}(T_n-T_{n+d})
&=\sum_{j=0}^{d-1}T_{A+j}-\sum_{j=0}^{d-1}T_{2A-d+j}\\
&\le\frac d{64A^2}.
\end{aligned}
\]

Summing both orientations over d=1,...,A−1 gives

\[
\sum_{n,t}|T_n-T_t|\le\frac{A-1}{64A},\qquad
\boxed{|J_{A,q}(X)-J_{A,q}(U)|\le\frac{q^2(A-1)}{64A^3}.}\tag{SC-4}
\]

At any `q≈log A`, the unnormalized **energy** discrepancy is `O(log² A/A²)`. This is a genuine original-source real completion transport, not a computed π energy. Crucially it pays NO unknown event count at the canonical bin boundaries: the triangular kernel is Lipschitz even when phases lie exactly on a bin edge.

This is an alternative exact comparator to inherited SUCC #475/#476 Fejér-Hilbert transport, not a replacement proof of the source-selected energy saving.

## SC-05 — authentic chronological forcing as a translated-boundary flux

For every original phase, put `z_n={16x_n}`, `x_(n+1)={z_n+r(n+1)}`. The translated q-cell labels of these two points differ on a set of origins of measure exactly

\[
\min(1,q\|r(n+1)\|),\qquad q>=2.
\]

Thus the **actual source-driven** averaged fraction of boundary crossings in epoch [A,2A) is exactly

\[
\boxed{B_{A,q}=\frac1A\sum_{n=A}^{2A-1}\min(1,q\|r(n+1)\|).}\tag{SC-5}
\]

The original Mellin numerator has the positive factorization

`P(t)=(1-t)(t²+2)(t²+2t+2)`, so on `[0,1]`, `0<P(t)<=15(1-t)` (strict interior). This proves, for every integer n>=1,

\[
0<r(n) < \frac{15}{(8n-7)(8n-6)}.
\]

Consequently for all A>=1,

\[
\boxed{B_{A,q}<\frac{15q}{(8A+1)(8A+2)}=O(q/A^2).}\tag{SC-6}
\]

More precisely, the L1 norm of the vector of q-bin masses of `mu_A−T_*mu_A`, averaged over τ, is bounded by

`2/A + 2 B_(A,q) <= 2/A + 30q/((8A+1)(8A+2))`.

Proof: telescope the endpoints `δ_(x_A)−δ_(x_(2A))` and pay at most 2 for each genuine source-forced label crossing. The forcing and source time remain fully marked. **This is approximate source stationarity, NOT mixing.** A delta at the 16-fixed point 1/5 is exactly stationary but has energy J_q=q forever.

## SC-06 — shifted 16-ary electrical-current square, same source

For each τ, the actual 16^k cylinder current `mu_(A,τ)(w)` satisfies current conservation and the all-finite identity from parent #488:

\[
E_{k+1}(τ)-E_k(τ)
=16^{k+1}\sum_{|w|=k}\sum_{j=0}^{15}
\left(\mu_{A,τ}(wj)-\frac{\mu_{A,τ}(w)}{16}\right)^2.
\]

Integrating gives

\[
\boxed{J_{A,16^K}-1=
\sum_{k=0}^{K-1}16^{k+1}\int_0^1\sum_{|w|=k,j}
\left(\mu_{A,τ}(wj)-\frac{\mu_{A,τ}(w)}{16}\right)^2dτ.}\tag{SC-7}
\]

The k=0 convention is a single circle cylinder, `E_0=J_(A,1)=1` regardless of τ; the triangular formula is used ONLY for mesh>=2. This is a positive exact martingale square-function, not a physical resistive network or a Feynman amplitude. It is an analytically smoother version of the same original-source branch imbalance.

## SC-08 — an explicit polylogarithmic selected Fourier attack band (NEW conditional reduction)

From the exact Fourier expression (SC-2), `0<=sinc²<=1` and, for every integer h≠0,

`(sin(πh/q)/(πh/q))² <= q²/(π² h²)`.

For integer H>=1, `sum_(h>H)1/h² <=1/H` by the integral test. Also `|c_A(h)|<=1`. Thus for all q>=2 and all H>=1,

\[
\boxed{J_{A,q}\le 1+\sum_{1\le |h|\le H}|c_A(h)|^2
+\frac{2q^2}{\pi^2H}.}\tag{SC-8}
\]

Taking `H=ceil(q²)` makes the entire infinite-frequency tail smaller than `2/π²<2/9` (classical π>3). So **one sufficient, still UNPROVED ORIGINAL-source estimate** is

\[
\sum_{1\le|h|\le q_A^2}|c_A(h)|^2=o(\log q_A),\qquad
q_A=m_A/2\asymp\log A.
\]

This is a polylogarithmic low-frequency-band statement for the actual signed BBP time orbit, NOT an average over Galois automorphisms and NOT a proof. It could be attacked with corrected split/inert prime clocks: for sufficiently large A, all tested `|h|<=q_A²` are in #485's authenticated range `|h|<=A`. The selected complementary real cofactor remains unpaid. This criterion can be stronger than inherited Fejér requirements; its merit is a rigorously bounded high-frequency tail and no dependence on arbitrary canonical bin boundaries.

## SC-07 — hostile controls and true next obstruction

- **Selected nonnormal fixed point:** `x_n=1/5` all n is fixed by ×16. Every translated histogram has E_q=q and J_q=q. It passes exact stationarity but fails SC-3's desired o(log m). Thus neither shift averaging nor (SC-5) manufactures Haar.
- **Wrong initial seed:** source forcing alone and conditional stationarity are seed-blind; the original marked `U0=0` is essential for π. A nonnormal coherent completed orbit can have the same forcing and a different initial seed.
- **Prime/cofactor clock:** source-selected split/inert p passports of #485, large conductor of #487 and Gamma boundary shear cannot be substituted for an actual small J. Large p denominators alone provide no real near-pair spacing.
- **No periodic-boundary shortcut:** SC-1 averages ONLY over the measurement partition origin; as Fourier (SC-2) shows, all original signed characters are retained. It does not replace the selected orbital measure by Haar.
- **Finite holdouts:** original A=40/80/160 at meshes m=8/16/32, independent common-odd-denominator source orbit and piecewise-exact translation integration A=12/24. These test the algebraic formulas and source provenance; they do NOT extrapolate to all A.

### Claim ledger

| Claim | Earned authority | Unpaid debt |
|---|---|---|
| SC-1 | Classical exact translated-bin/tent identity, source instantiated | Selected energy size |
| SC-2 | Classical B-spline Fourier positivity | Signed Fourier cancellation |
| SC-3 | Exact deterministic original unshifted domination | `J=o(K)` on all large dyadic epochs |
| SC-4 | Exact original-Gamma transported-energy inequality (dependent on inherited T bound) | π distribution |
| SC-5/6 | Exact original forcing crossing law, stationarity cap; negative periodic control | Source-selected mixing versus invariant periodic measures |
| SC-7 | Exact averaged 16-branch martingale-current square, inherited finite identity | Quantitative branch saving |
| SC-8 | Elementary exact Fourier tail control; new explicit selected polylog band sufficient condition | Original signed second moment over that band |

**π base-16 normality, RH, physical Feynman amplitudes, a source-selected electrical minimum, and new compiled Lean authority are OPEN / not claimed.** This project uses established mathematical constructions; no original academic priority claim.

### Classical references

- Loukas Grafakos, *Classical Fourier Analysis*, Haar/martingale square-function chapter: https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf
- Standard triangle/sinc-square Fourier computation (convolution of two box functions), e.g. Shirley et al., *Fundamentals of Computer Graphics*, signal-processing chapter.
- SUCC primary dependencies: #488 CE-01..06 (arithmetic inverse and exact current square); #487 OMC-01..08 (original Gamma tail, source-lift CRT ghost); #476 WM-06/07 (sublog mesh to all-prefix normality, conditional).
