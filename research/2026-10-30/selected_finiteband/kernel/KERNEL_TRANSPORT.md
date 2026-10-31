# Fejer transport at the sampling scale and its coherent sharpness

**PROVED LOCAL, paper proofs.** These are stronger source-to-phase comparison
bounds and exact hostile-control asymptotics. They are **not** a selected
zero-boundary cancellation theorem. Base-16 normality of pi remains open.
Classical Fejer, Hilbert-space and entropy facts retain their classical status;
no scholarly-priority claim is made.

## K01. A square-root transport inequality through the full sampling range

Keep the authentic source

\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j).
\]

For any real seed `s`, let `U_n(s)=16U_(n-1)(s)+r(n)`, `U_0(s)=s`, and
`y_n(s)=U_n(s)+T_n` modulo one. The authentic selected case is exactly `s=0`.
For an integer `H>=2`, write `F_H(t)` for the Fejer kernel and
`E_H(x)=N^-2 sum_(i,j) F_H(x_i-x_j)` for the finite-band energy.
Define

\[
D_H=2\pi\sqrt{H(H^2-1)/6},\qquad C_*^2=\frac\pi{8\sqrt3}.
\]

Then, for every `N>=1`, `H>=2`, and `s` independently of `N,H`,

\[
\boxed{\left|\sqrt{E_H(y(s))}-\sqrt{E_H(U(s))}\right|
\le\frac1N\sum_{n=1}^N\min\{\sqrt{2H},D_HT_n\}
\le\frac{C_*\sqrt H(H^2-1)^{1/4}}N
<\frac{C_*H}N.}\tag{K01}
\]

**Proof.** With `a=8n-7`, the exact positive decomposition is

\[
r(n)=\frac6{a(a+3)}+\frac4{a(a+4)}+\frac5{a(a+5)}.
\]

Each summand is decreasing. Since `sum_(j>=1)16^-j=1/15`,

\[
0<T_n\le r(n+1)/15\le[(8n+1)(8n+4)]^{-1}<\frac1{64n^2}.
\tag{K01a}
\]

Use the finite Hilbert vector
`Phi_H(x)=(sqrt(1-|h|/H)e(hx))_(|h|<H)`. Its squared norm is `H`, its
inner product is the real nonnegative `F_H(x-y)`, and

\[
\|\Phi_H(x)-\Phi_H(y)\|^2=2[H-F_H(x-y)]\le2H.
\]

The exact finite coefficient sum is
`sum_(|h|<H) h²(1-|h|/H)=H(H²-1)/6`, so `||Phi_H'||=D_H`.
Apply the reverse triangle inequality to the two averaged vectors. This proves
the first inequality, including seams because the vectors are periodic.
For `A=sqrt(2H)` and `B=D_H/64`, the decreasing function
`f(x)=min(A,B/x²)` satisfies

\[
\sum_{n\ge1}f(n)\le\int_0^\infty f(x)\,dx=2\sqrt{AB}
=C_*\sqrt H(H^2-1)^{1/4}.
\]

This proves the bound. No source-pair independence is used. ∎

An alternative scalar verification is
`||Phi(x)-Phi(y)||²=2 sum_h w_h[1-cos(2pi h(x-y))]`.
The source-specific input is the exact native tail bound. The Hilbert argument
itself applies to any matched pair of samples with summable corrections.

**Consequence at the natural sample size.** Let
`m_N=floor(log_16 N)`, `q_N=16^m_N`, `H_N=q_N/2`. The old hard-cylinder bound gives

\[
Q_{m_N,N}(y(0))\le\frac{\pi^2}{2}
\left(\sqrt{E_{H_N}(U(0))}+C_*H_N/N\right)^2.\tag{K01b}
\]

Here `H_N/N<=1/2`: the correction is bounded, and therefore an independently
proved `log E_(H_N)(U(0))=o(m_N)` would still imply normality. For every fixed
`0<c<1`, the analogous depth `floor(c log_16 N)` has a vanishing square-root
correction. This improves PR411's `O(H²/N)` *energy transport* range. It does
not supply the needed energy upper bound at any of these scales. The diagonal
floor `E_H>=H/N` independently rules out subpower energy when `H/N` grows as a
fixed positive power of `H`.

## K02. The order `H/N` is sharp for the coherent same-forcing seed

At the deliberately changed seed `s_*=-pi/16`, the completed orbit is zero and
the forced points are `-T_n`. Let

\[
\Delta_{H,N}=\sqrt H-\sqrt{E_H((-T_n)_{1\le n\le N})}\ge0.
\]

For any joint integer sequence with `H→∞` and `N/sqrt(H)→∞`,

\[
\boxed{\frac NH\Delta_{H,N}\longrightarrow\frac\pi{15}.}\tag{K02}
\]

Thus the uniform same-forcing comparison cannot have `o(H/N)` error in that
regime. This obstruction does **not** assert sharpness for the authentic zero
seed; it prevents mistaking source-only transport for selected dispersion.

**Proof of the original source constant.** Dominated convergence in the exact
positive Green series gives `n²T_n→1/64`: each fixed source term has
`n²r(n+j)→15/64`, and its geometric weights sum to `1/15`; K01a supplies a
uniform dominating bound. Put

\[
A_H=\sum_{n\ge1}[H-F_H(T_n)].
\]

The exact Fourier coefficients, `1-cos z<=z²/2`, and K01a imply

\[
0\le 1-F_H(T_n)/H\le
\min\{1,\pi^2H^2/(12288n^4)\}.\tag{K02a}
\]

For `n/sqrt(H)→x>0`, the summand tends to
`1-sinc²(pi/(64x²))`, where `sinc z=sin(z)/z`.
On every compact `x` interval away from zero convergence is uniform, because
`n²T_n→1/64` uniformly on every sufficiently far tail and `sin(pi T_n)/(pi T_n)→1`.
K02a controls the large-x tail; the number of mesh points in `(0,epsilon)`
divided by `sqrt H` is at most `epsilon`. Riemann sums therefore give

\[
\frac{A_H}{H^{3/2}}\longrightarrow
K:=\int_0^\infty[1-\operatorname{sinc}^2(\pi/(64x^2))]\,dx=\frac\pi{15}.
\tag{K02b}
\]

For completeness, the last integral is evaluated, rather than fitted. Substitute
`t=pi/(64x²)` and use

\[
\operatorname{sinc}^2t=2\int_0^1(1-u)\cos(2ut)\,du,
\qquad
\int_0^\infty(1-\cos(at))t^{-3/2}dt=\sqrt{2\pi a}\quad(a\ge0).
\]

The latter follows by integration by parts and the classical sine Mellin
integral at `z=1/2`, `Gamma(1/2)=sqrt(pi)`. The nonnegative `1-cos` integrand
justifies Tonelli. Hence

\[
K=\frac{\sqrt\pi}{16}\,2\int_0^1(1-u)\sqrt{4\pi u}\,du
=\frac{\sqrt\pi}{16}\frac{16\sqrt\pi}{15}=\frac\pi{15}.
\]

This is a load-bearing Gamma-half/Mellin evaluation with a source-selected
tail coefficient, not the original Oily–Macaroni constant or an emergent golden
parameter. For a tail `T_n~A/n²` the same calculation gives `8pi sqrt(A)/15`.
Sources with the same tail coefficient share this coherent asymptotic.

**Explicit joint-regime error.** Let `A_(H,N)=sum_(n<=N)[H-F_H(T_n)]` and
`V=sum_(n<=N)[Phi_H(-T_n)-Phi_H(0)]`. K01 gives `||V||<=C_*H` and

\[
E_H(-T)=H-2A_{H,N}/N+\|V\|^2/N^2.
\]

Since `0<=Delta<=||V||/N`, exact squaring yields

\[
0\le\frac{A_{H,N}}{N\sqrt H}-\Delta_{H,N}
=\frac{\|V\|^2/N^2-\Delta_{H,N}^2}{2\sqrt H}
\le\frac{C_*^2H^{3/2}}{2N^2}.
\]

Also K02a and the integral test give
`0<=A_H-A_(H,N)<=pi²H³/(36864 N³)`. Consequently

\[
\left|\frac NH\Delta_{H,N}-\frac\pi{15}\right|
\le\left|\frac{A_H}{H^{3/2}}-\frac\pi{15}\right|
+\frac{\pi^2}{36864}\left(\frac{\sqrt H}N\right)^3
+\frac{C_*^2}2\frac{\sqrt H}N.
\tag{K02c}
\]

Every term tends to zero in the declared joint regime. ∎

## K03. A cheaper finite band and an improved cylinder constant

For `q>=2` and an integer `1<=H<q`, put `a=H/q`. On `||t||<=1/q`, monotonicity
of `sin z/z` on `(0,pi)` and `|sin(pi t)|<=pi||t||` give

\[
F_H(t)\ge H\left[\frac{\sin(\pi a)}{\pi a}\right]^2.
\]

Therefore for all finite circle samples, including half-open cell seams,

\[
\boxed{Q_q(x)\le\frac{\pi^2a}{\sin^2(\pi a)}E_H(x).}\tag{K03}
\]

For hexadecimal `q=16^m`, `H=q/4` retains the inherited factor `pi²/2` with
half as many frequencies. The choice `H=3q/8` improves the factor to
`3pi²/[2(2+sqrt2)] < pi²/2`. These are elementary kernel optimizations, not new
source arithmetic. The continuous optimum for this particular lower bound is
the unique `a in (0,1/2)` satisfying `tan(pi a)=2pi a`; no global optimality over
all nonnegative kernels is claimed.

## K04. Fixed polynomial clocks need not certify even a normal stream

Fix `0<c<=1`. Start with any normal base-16 digit sequence. At positions
`M_j=16^(j²)` replace the next `L_j=floor(M_j/j)` digits by zero (use `j>=2`).
The replacement set has density zero: during the j-th edited interval the new
fraction is at most `1/j`; earlier edits total `o(M_j)`, and between intervals
the fraction decreases. Changing `D(N)=o(N)` digits changes every fixed k-word
count by at most `k D(N+k)=o(N)`, so the modified sequence is still normal.

At `N_j=M_j+L_j`, `m_j=floor(c log_16 N_j)`, at least `L_j-m_j+1` of the first
`N_j` starting positions carry the word `0^m_j`. Thus

\[
Q_{m_j,N_j}\ge16^{m_j}\left(\frac{L_j-m_j+1}{N_j}\right)^2,
\quad
\frac{\log Q_{m_j,N_j}}{m_j}\longrightarrow\log16.
\]

The same conclusion holds for the Fejer energy at `H_j=16^m_j/2`, by the lower
bound `E_H>=2Q/pi²` and the universal upper bound `E_H<=H`. Therefore prescribed
polynomial-clock subexponential energy is **strictly sufficient**, not necessary
for normality. It may demand much more quantitative information than normality.
The modified number can be realized as a changed seed for the original forcing;
K01 transfers this failure to that forced trajectory too. It is not the
authentic `U_0=0` trajectory and is not an arithmetic counterexample to its
unproved estimate.

## Audit of the inherited bridges and the exact remaining debt

PR411 FB01/02/04 are valid as written: same-cell distance is strictly below
`1/q`; Fejer nonnegativity handles all other pairs; the derivative sum is
`2pi(H²-1)/3`; the two-point Green coupling uses `T_i+T_j`. Its hot-spot partition
overcounts harmlessly for small H. The factor `<3` is conservative. Finite
double-precision tests in that PR do not constitute interval proofs.

Sibling410 MS01 is valid with overlapping sampled words: after sampling one
start, the *coordinate subblocks* inside its m-word are disjoint, so KL against
the product uniform reference dominates the sum of marginal KL values without
independence assumptions. A shifted-start marginal differs by at most `2jk/N`;
this bound remains valid even when it exceeds two. The diagonal floor forces
`m_N=O(log N)` under its subexponential premise. MS02's converse is existential
in the clock `m_N`, fully consistent with K04. Its source premise is unproved.

Sibling409 RS-MaxCyl is valid in symbolic space: cylinders are clopen; every
empirical cluster measure is stationary; a nonuniform fixed block law forces
a positive linear entropy deficit at every larger depth. Taking max over the
finite cylinder set commutes with the relevant subsequence limit. None of this
establishes a selected arithmetic occupancy bound. Stationarity is essential:
a forced first digit followed by independent uniform digits violates the desired
conclusion while having only a constant maximum-cylinder overhead.

**Smallest missing arithmetic interaction remains:** prove a subpower bound on
the actual selected finite-band energy, or a genuine source-conditioned upper
bound on its complementary signed CRT correlation. K01/K02 show why removing
the source-tail error more accurately cannot itself supply that bound. Source
Gamma geometry, the harmonic/golden/Euler triangle and the author's
`Omega_OM=phi^-1-gamma` remain preserved; no theorem here forces those constants
into the selected energy. The only new Gamma appearance above is the explicit
Mellin evaluation in the *coherent changed-seed control*.

## Provenance and proof authority

Read-only parent PR411 `fa598e3a5a1111c3445200f1ddf48dcdea6bdc09`; sibling410
`5a54cd1a4200f3b0e673f6c3feecff76bf6b6dc6`; sibling409
`3857e70472cac7c572528cc6d4198246e57d36df`. Exact local source hashes appear in
`SOURCE_MANIFEST.json`. No sibling was merged or copied as an implementation.
The primary classical input for the integral is
[NIST DLMF 5.9.7](https://dlmf.nist.gov/5.9.E7) at `z=1/2`, and
[NIST DLMF 5.4.6](https://dlmf.nist.gov/5.4.E6).
The printed finite tests and distinct oracle validate implementations and fresh
cases; they are not external mathematical refereeing or Lean kernel proofs.
