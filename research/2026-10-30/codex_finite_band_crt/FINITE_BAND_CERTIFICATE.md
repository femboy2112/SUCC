# Codex finite-band certificate — hard cylinders through a Fejér spectral window

**Research only; classical Fourier inequalities specialized to the authentic SUCC BBP selected orbit.** No base-16 normality of pi, fixed-frequency Weyl cancellation or RH theorem is claimed. Starting parent PR #407, `5f05181339ea97a56999ca8b8ab10a2009c6c84d`. Read sibling DeepSeek PR #410 and RAW STATE PR #409 *without merging them*. The source and zero initial condition are immutable:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n),
\]
\[
y_n=\{16^{n-1}\pi\}=\{U_n+T_n\},\quad T_n=\sum_{j\ge1}16^{-j}r(n+j)>0,\quad B=\sum_{n\ge1}T_n=(\sum_n r(n)-\pi)/15<1/32.
\]

## FB-01. Finite Fourier band dominates hard digit cylinders — proved locally

For **any** finite list of N circle points `x_1,...,x_N`, integer `m>=1`, let `q=16^m`, `H=q/2` and

\[
Q_{m,N}(x)=\frac q{N^2}\#\{(i,j):x_i,x_j\text{ lie in the same half-open }q\text{-cell}\}.
\]

Define the **Fejér kernel**, a nonnegative trigonometric polynomial with exactly `2H-1` frequencies:

\[
F_H(t)=\frac1H\left|\sum_{a=0}^{H-1}e^{2\pi iat}\right|^2
 =\sum_{|h|<H}\left(1-\frac{|h|}{H}\right)e^{2\pi iht},
\]
\[
\mathscr F_{H,N}(x)=\frac1{N^2}\sum_{i,j}F_H(x_i-x_j)
 =\sum_{|h|<H}\left(1-\frac{|h|}{H}\right)\left|\frac1N\sum_{n=1}^Ne^{2\pi ihx_n}\right|^2\ge1.
\]

**THEOREM:**
\[
\boxed{Q_{m,N}(x)\le\frac{\pi^2}{2}\,\mathscr F_{H,N}(x),\qquad H=16^m/2.}\tag{FB1}
\]

*Proof.* If two points occupy the same q-cell then their circular distance is **strictly** below `1/q=1/(2H)`. In this distance range `|sin(pi Ht)|>=2H||t||`, while `|sin(pi t)|<=pi||t||`. Hence `F_H(t)>=4H/pi²` (with the same true bound at t=0 by continuity). Since `q=2H`, `q 1_(same cell) <= (pi²/2) F_H(x_i-x_j)` **termwise**; outside a common cell the left side vanishes and the right side is nonnegative. Sum pairs. No source assumptions or independence of times are involved. ∎

The Fejér band is a **finite polynomial**; unlike the translated-tent Fourier formula in PR407 it has no infinite spectral tail. This is an alternate probe, **not** a source-derived bound or a claim of originality for Fejér analysis.

## FB-02. Authentic source-to-completed-phase transport — proved locally

The derivative Fourier bound is
\[
\|F_H'\|_\infty\le2\pi\sum_{|h|<H}|h|(1-|h|/H)
=\frac{2\pi}{3}(H^2-1).
\]

The exact same index coupling between rational states and completed states gives

\[
\boxed{\big|\mathscr F_{H,N}(y)-\mathscr F_{H,N}(U)\big|
\le\frac{4\pi B}{3N}(H^2-1)
<\frac{\pi(H^2-1)}{24N}\le\frac{\pi 16^{2m}}{96N}.}\tag{FB2}
\]

*Proof.* For each pair, the circular perturbation between differences is at most `T_i+T_j`. Apply the global Lipschitz bound, average all `N²` ordered pairs, and use `sum_{n<=N}T_n<=B<1/32`. This controls complete two-time signed phases, not hard word indicators across a discontinuous cell seam. ∎

## FB-03. A single moving-frequency sufficient normality certificate — conditional / open premise

Choose
\[
m_N=\lfloor\tfrac13\log_{16}N\rfloor,\quad q_N=16^{m_N},\quad H_N=q_N/2.
\]
For sufficiently large N, these are valid positive integers, `m_N->infty`, and `H_N²/N=O(N^{-1/3})`. If the **authentic, selected, zero-seed rational** orbit satisfies
\[
\boxed{\log\mathscr F_{H_N,N}(\{U_1(0)\},\ldots,\{U_N(0)\})=o(m_N),}\tag{FB3-OPEN}
\]
then pi is base-16 normal.

*Proof of the implication, not its hypothesis.* FB2 transports the pair energy from U to y with o(1) additive error; FB1 bounds the hard digit-cylinder collision energy by `(pi²/2)(F_U+o(1))`. Thus `log Q_{m_N,N}(y)=o(m_N)`. Parent DeepSeek PR410's independently auditable single-moving-depth entropy theorem MS-02 implies normality. Alternatively use the classical invariant-measure entropy proof in PR407. ∎

**Proof debt:** no authentic source-derived estimate for FB3-OPEN is known here. It is closely related to the selected signed Weyl problem; expanding the finite Fourier sum alone is a restatement, not progress. It demands cancellation over the growing band `1<=|h|<H_N~N^(1/3)`. PR405's high-frequency estimates concern `|h|~A²..A³` and do **not** enter this band. The coherent same-forcing seed `s*=-pi/16` has F_H(y)=H and fails FB3-OPEN.

## FB-04. A source-to-occupancy sufficient alternative — conditional / open for pi

For any empirical probability measure `mu_N=(1/N)sum delta_(x_n)` and any integer H>=2 put
\[
C_N(H)=\sup\{\mu_N(I):I\text{ a circle arc of length }1/H\}.
\]
Then
\[
\boxed{\mathscr F_{H,N}(x)\le(2+\pi^2/12)H C_N(H)<3H C_N(H).}\tag{FB4}
\]

*Proof.* Fix y and partition the circle into the H half-open arcs `[y+j/H,y+(j+1)/H)`. On the two arcs adjacent to y, `F_H<=H`. For any other arc at integer distance j>=1 from the adjacent pair, `F_H(t)<=H/(4j²)` since `sin(pi||t||)>=2||t||`. There are at most two such arcs for each j. Summing the suprema gives `2H+(H/2)sum_{j>=1}j^-2=H(2+pi²/12)`. Each arc has measure at most C_N(H). Integrate against `mu_N(y)` to get FB4. ∎

So a selected **moving weak-hot-spot estimate** `C_N(H_N)<=H_N^{-1+o(1)}` implies FB3-OPEN and normality. This is **stronger than necessary** and NOT established for pi.

**Positive calibration:** for the published normal Stoneham `alpha_(16,c)`, c=3 or5, the source-proved hot-spot bound from PR395 gives `N mu_N(I) <= c N|I|+O_c(log N)` for every interval. With H_N=O(N^(1/3)), FB4 yields `F_H<=3c+O_c(H log N/N)=O_c(1)`, an actual certificate for that **different source**. The c=2 source lacks this bound and is a nonnormal countercontrol.

## FB-05. Scope and adversarial test contract

- Positive tests: full Haar digit law in expectation, original exact BBP rational prefix finite holdout, normal Stoneham 3/5 source arithmetic, exact Fejér Fourier-vs-Dirichlet equality.
- Negative controls: coherent changed seed `-pi/16` (full phase band H), all-zero, periodic de Bruijn order two (Q1=Q2=1 but Q3=16), biased Bernoulli, sparse Kempner, zero-seed seven-pole null source.
- Source mutants: Gamma-matched, 59-jet/higher-jet matched and J-involution-matched; none automatically has known normality status.
- Keep original literal carries, exact rational full source and zero boundary separate from positive Gamma/Pascal auxiliary observer and CRT prime marginals.
- Finite float / high-precision checks **calibrate implementation only**. Theorems FB1/FB2/FB4 are elementary paper proofs. FB3's source-selected bound is **OPEN**.

**Next verdict-changing action:** prove FB3-OPEN or a genuine selected source-derived moving-interval estimate in FB4, by arithmetic rather than criterion restatement. Attack full `p`-primary **times complementary** real-character correlation, source Green-tail closure and zero-seed selected cylinder frequencies; rotate representation to test independent derivations. If only a sparse-window bound is proved, explicitly prove how it covers enough time and the required frequencies before claiming normality.
