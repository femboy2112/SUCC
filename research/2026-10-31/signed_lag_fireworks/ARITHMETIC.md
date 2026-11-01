# Exact 3-by-5 conductor shadows of the original BBP forcing

**Status: PROVED LOCAL, paper proof and exact finite instruments.** This is
a counterexample to a restricted proof route, not a counterexample to the
zero-selected pi orbit. No external mathematical priority is asserted.
The four signed poles remain

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

The distinction in this result is the **entire explicit signed lag spectrum
of a single periodic orbit with arbitrarily deep 3/5 conductor**, transported
to that same forcing and placed arbitrarily close to seed zero. The older
finite-band and nearzero-seed firewalls are not claimed as new discoveries.

## A1. Exact principal-unit orbit and complex lag means

Fix integers a,b>=1 and c with gcd(c,15)=1. Set

\[
q=3^a5^b,\qquad P=q/15=3^{a-1}5^{b-1}.
\]

Classical LTE gives

\[
v_3(16^k-1)=1+v_3(k),\qquad
v_5(16^k-1)=1+v_5(k).
\]

Thus the orders modulo 3^a and 5^b are 3^(a-1) and 5^(b-1).
Their least common multiple is P. Every power of 16 is 1 modulo 15,
and there are exactly P residues modulo q with that property. Consequently

\[
\boxed{\langle16\rangle\pmod q=\{1+15j:0\le j<P\}.}\tag{A1}
\]

Multiplication by the unit c gives the complete coset c mod15, visited once
in each period. For the actual deterministic completed orbit
x_n=c16^n/q modulo one, its exact full-period Fourier mean is therefore

\[
M_h=\frac1P\sum_{n=0}^{P-1}e(hx_n)
=e(hc/q)\frac1P\sum_{j=0}^{P-1}e(hj/P)
=\begin{cases}0&P\nmid h,\\ e(hc/q)&P\mid h.\end{cases}\tag{A2}
\]

This is an ergodic invariant measure on **one finite orbit**: multiplication
by 16 permutes its P points in one cycle. It is not Haar measure.

For every k>=1 the full-period pair-phase mean is equally explicit:

\[
\boxed{A_{h,k}=\frac1P\sum_{n=0}^{P-1}e(h(x_{n+k}-x_n))
=\begin{cases}
0&P\nmid h(16^k-1),\\
e(hc(16^k-1)/q)&P\mid h(16^k-1).
\end{cases}}\tag{A3}
\]

In particular A_(h,k) is nonzero precisely on the lag progression

\[
\boxed{
3^{\max(0,a-2-v_3(h))}5^{\max(0,b-2-v_5(h))}\mid k.
}\tag{A4}
\]

The surviving **complex root of unity in A3 must be retained**. Counting
the nonzero support in A4, or replacing those roots by their absolute
values, loses the signed cancellation. These are authentic arithmetic
frequencies 16^k-1, with both exceptional prime filtrations present.

An exact small witness is q=225, P=15, c=h=1. The binomial formula gives
16^k-1=15k modulo225, so **every** lag is supported and A_(1,k)=e(k/15).
The limiting weighted signed score is zero, whereas replacing each
supported phase by its modulus gives a limit of one. The independent
cyclotomic oracle rejects the corresponding erroneous phase-one mutation.

## A2. Transport to the identical four-pole forcing

Let alpha_0=pi/16=sum_(j>=1)16^(-j)r(j) and
T_n=sum_(j>=1)16^(-j)r(n+j). The symbolic seed

\[
s_{q,c}=c/q-\alpha_0
\]

is irrational and nonzero. The exact same source recurrence gives

\[
\boxed{U_n(s_{q,c})=16^nc/q-T_n.}\tag{A5}
\]

This is an explicitly altered seed, never a replacement for U_0=0.
The original positive four-pole regrouping yields, for n>=1,

\[
0<r(n+1)<\frac{15}{64n^2},\qquad
0<T_n<\frac1{64n^2}.
\]

The second inequality follows by applying the first to each n+j and
summing the geometric factor sum_(j>=1)16^(-j)=1/15. For h!=0 set
B_h=ceil(sqrt(|h|)). A bounded-character estimate, split at the **integer**
m=B_h4^k, proves the all-horizon comparison

\[
\begin{aligned}
|D_{h,k}^{s_{q,c}}(N)-D_{h,k}^{\rm per}(N)|
&\le\sum_{n=1}^{N-k}
\min\left(2,\frac{\pi|h|(16^k-1)}{32n^2}\right)\\
&\le2m+\frac{11|h|(16^k-1)}{112m}
<3B_h4^k.
\end{aligned}\tag{A6}
\]

Here D^per uses the completed rational phase from A3; sum_(n>m)n^-2<=1/m
and pi<22/7 were used. This is a source transport estimate, uniform in
the altered seed parameters; it is not selected cancellation.

For the exact Fejer weights of PR #434, let

\[
R_{N,K}(h)=\frac{6B_h}{K^2N}\sum_{k=1}^{K-1}(K-k)4^k
=\frac{2B_h(4^{K+1}-12K-4)}{3K^2N}
\le\frac{8B_h4^K}{3K^2N}.\tag{A7}
\]

It bounds the absolute difference between the true source-reduced signed
score and its periodic completed score. At K=floor(log_16 N), it is at
most 8B_h/(3K^2 sqrt(N)). All statements also apply to any K(N)<=N with
K(N)->infinity, K(N)/N->0 and 4^K/(K^2N)->0.

## A3. Exact limiting signed lag spectrum and finite bounds

Suppose first that P does not divide h. The periodic sequence z_n=e(hx_n)
has mean zero over a full period by A2. Every consecutive partial sum has
absolute value at most P: delete all complete periods and bound the fewer
than P remaining unit terms. Extend a window of N such terms by zero.
Every length-K sliding window V_t then also has absolute value at most P,
including both boundary windows, since its nonzero support is a consecutive
segment of the original periodic sequence. Expanding the square exactly,

\[
\frac1K+\mathcal L^{\rm per}_{N,K}(h)
=\frac1{K^2N}\sum_{t=1}^{N+K-1}|V_t|^2.
\]

Thus for **every** N>=K>=1,

\[
\boxed{
-\frac1K-R_{N,K}(h)
\le\mathcal L^{s_{q,c}}_{N,K}(h)
\le\left(1+\frac{K-1}{N}\right)\frac{P^2}{K^2}
-\frac1K+R_{N,K}(h),\quad P\nmid h.
}\tag{A8}
\]

If P divides h, z_n=e(hc/q) is constant because 16=1 modulo15.
All its completed pair phases are one, and the finite weighted sum is

\[
\mathcal L^{\rm per}_{N,K}(h)
=\frac{K-1}{K}\left(1-\frac{K+1}{3N}\right).
\]

The source score is within R_(N,K)(h) of this expression. In particular,
for each **fixed** a,b,c,h, with K_N=floor(log_16 N),

\[
\boxed{
\lim_{N\to\infty}\mathcal L^{s_{q,c}}_{N,K_N}(h)
=\begin{cases}0&P\nmid h,\\1&P\mid h.\end{cases}}
\tag{A9}
\]

The same dichotomy follows for the squared limiting Weyl mean from A2
and the summability of T_n. In particular h=P is a fixed witness of
nonnormality. The detector is P, rather than the less precise denominator q.

**Decisive consequence.** Given any finite harmonic cutoff H, choose P>H.
Every one of the actual signed lag criteria at 0<|h|<=H is satisfied by
this nonnormal same-forcing trajectory, while h=P fails maximally. Exact
3/5 prime-conductor identities, exact complex pair-phase recovery, and
arbitrarily many fixed low harmonics cannot by themselves justify extending
the inequality to all harmonics. This does not refute any argument that
uses an additional exact zero-boundary property.

These irrational-seed real trajectories do **not** preserve the original
diagonal rational state sequence U_n(0), or its canonical 2-adic state
interpretation. They preserve the rational forcing, its source-pole laws,
and the specified real completed-conductor data. Accordingly this theorem
does not refute a fully authenticated adelic-to-real argument that retains
exact diagonal rational states and the zero selector; that stronger
transference is precisely an unpaid obligation.

## A4. The same conductor shadows can approach seed zero

This placement uses only a rational prefix of the original source. Fix
M>=1 and let alpha_M=sum_(j=1)^M16^(-j)r(j). Choose

\[
c=15\left\lfloor\frac{q\alpha_M-1}{15}\right\rfloor+1.
\]

Then gcd(c,15)=1, c/q<=alpha_M<(c+15)/q, and

\[
\boxed{0<|s_{q,c}|=\alpha_0-c/q
<\frac{15}{q}+\frac{16^{-M}}{64M^2}.}\tag{A10}
\]

For every epsilon>0, finite observed horizon N_0, and harmonic cutoff H,
choose M and a,b sufficiently large that P>H and the right side of A10
is smaller than epsilon*16^(-N_0). Then
|U_n(s)-U_n(0)|<epsilon for every 0<=n<=N_0. Nevertheless the **one fixed
chosen seed** is nonnormal, has exactly the low-band limits A9, and has
the fixed failing harmonic h=P. This choice does not assert a uniform
in-P convergence rate as N grows: P is fixed before taking the limit.

## Source audit, prior art within this repository, and claim boundary

- PR #434 at `030ee84b8b7f655fcf433375bfc0b347e0483c89` supplies the
  source, signed-score normalization, classical VdC identity and the
  original open zero-selected limit. Its reduction is not its conclusion.
- PR #430 at `ba8bc0d3636af19c93f5983094456e44ecac457c` was read directly
  via GitHub, including `multiplace_bbp_difference/PROOF.md` and
  `multiplace_difference.py`. Its four-pole 3-adic noncancellation and
  deep-pole deletion statements concern r and hold for these same-forcing
  countermodels too. Its unbounded p3 norm firewall does not license a
  real-character estimate. No #430 files were imported or changed.
- `PERIODIC_TEMPLATE_COERCIVITY.md` (2026-10-27) already proves selected
  logarithmic modulus loss with a classical irrationality input. A9 does
  not improve that selected loss.
- `PI_MIXING_FINITE_SPECTRUM_OBSTRUCTION.md` (2026-10-27) already gives
  stronger abstract finite-band counterexamples, even mixing and of finite
  irrationality type. The increment here is the explicit prime-smooth
  periodic orbit, its complete complex conductor-stratified lag spectrum,
  rational finite bounds, and its dense placement among BBP shadow seeds.
- PR #433 `NEAR_ZERO_SHADOW.md` already provides nearzero irrational
  nonnormal same-forcing seeds from exact source prefixes. A10 specifies
  the new 3/5 conductor family; it does not claim density as a new theorem.
- Fixed rational changes to the **BBP seed** are not these controls.
  Our c/q is the rational **completed carrier**; the BBP seed c/q-pi/16
  is irrational. Wall's rational-shift normality invariance is respected.

**Aletheia ledger.** The surviving rival is exact forcing with a different
global boundary. The operational common basis is e(hx), with explicit
Green-tail transport A6. The original four-pole source map is preserved,
but the zero-seed map is deliberately false for the controls. Full-period
CRT algebra and generic cyclotomic polynomial reduction are different
implementation routes, not independent mathematical sources. Finite
tomography and imported source claims are not additional witnesses of
normality. Contact with the source and finite arithmetic is present;
identification of zero-seed cancellation remains an open proof gap.

**Validation.** `python -m unittest discover -s tests -p
'test_signed_lag_fireworks_arithmetic.py' -v` executed 13 tests, all passing.
They include a generic independently implemented cyclotomic-polynomial
division oracle for complete complex means, full chronological orbit
enumeration, deeper v3/v5 lag classes, fresh h=3,5,7,11, independent original
source evaluation, rational tail budgets and outward rational finite cosine
bounds. This is finite implementation validation, not kernel formalization.

The deterministic raw receipt is regenerated by
`python research/2026-10-31/signed_lag_fireworks/arithmetic.py >
research/2026-10-31/signed_lag_fireworks/arithmetic_receipt.json`.
It preserves exact zero-versus-root phase labels for three conductor
families and four independently selectable original-source prefix seeds.
The limit labels explicitly cite A9; they are not inferred from a finite run.

**Next falsification probe.** Any proposed transfer from source-pole/CRT
data or finitely many harmonic lag limits must state exactly which
infinite zero-boundary hypothesis excludes A5/A10, then evaluate that
hypothesis on both the selected source and these shadows. The selected
inequality remains OPEN; these controls eliminate the seed-blind transfer.
