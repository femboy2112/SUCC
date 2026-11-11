# Source-zero cylinder microscope: a 16-adic observational tower with a signed BBP witness

**Research dossier, 2026-11-10.** Parent is SUCC draft **#591** at pinned
`41bbbe56bbb36bcbf2a171669bf508caea6f688b` (itself based on
Main XXIII draft #584). The source is the frozen authentic four-pole

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad \alpha=\sum_{n\ge1}16^{-n}r(n)=\pi/16.
\]

This is an **additional exact source-zero observation**, not a replacement
for `observational_succ/zero_anchored_lambda.py` or the signed CDF overlap
of #591. Source identity uses the classical BBP formula. No proof of the
normality of pi or of its even-digit parity frequencies is claimed.

## MS-01: exact base-16 cylinder orthogonality — PROVED PAPER

Let `e(t)=exp(2*pi*i*t)` and for every fixed nonzero integer `h` put

\[
W_{N,h}(s)=\frac1N\sum_{n=0}^{N-1}e\big(h16^n(\alpha+s)\big),\quad
I_K=[0,16^{-K}],\quad
\langle f\rangle_K=16^K\int_{I_K}f(s)\,ds,
\]

\[
\mathcal E_{N,K}(h)=\langle |W_{N,h}(s)|^2\rangle_K.
\]

The point `s=0` is **literally the original SUCC zero seed**. Other seed
values in `I_K` are *not* accepted as authentic sources. Averaging is a
mathematical probe of that distinguished point, not a seed replacement.

For integer `q` define

\[
\Phi_K(q)=16^K\int_0^{16^{-K}} e(qs)\,ds
=\begin{cases}1,&q=0,\\
\dfrac{e(q16^{-K})-1}{2\pi i q16^{-K}},&q\ne0.
\end{cases}
\]

In particular, **if `q` is a nonzero multiple of `16^K`, `Phi_K(q)=0` exactly**.
Thus the late-index characters `e(h16^n s)` for `n>=K` are pairwise
orthonormal on the seed cell `I_K`, independent of alpha, source, or seed.
The exact finite second moment is

\[
\boxed{\mathcal E_{N,K}(h)=\frac1{N^2}
\sum_{0\le m,n<N}
 e\!\left(h(16^n-16^m)\alpha\right)
 \Phi_K\!\left(h(16^n-16^m)\right).}\tag{MS1}
\]

For `K=0`, every off-diagonal term vanishes; therefore
`E_(N,0)(h)=1/N` for every alpha. This is **spatial annealed
cancellation**, NOT the cancellation of `W_(N,h)(0)`.

## MS-02: quantitative coarse and deep scales — PROVED PAPER

Split `W` into early indices `0<=n<K` and late indices `K<=n<N`.
The early part has sup norm at most `K/N`; exact pairwise orthogonality
gives L2 norm `sqrt(N-K)/N` for the late part. Hence for
`0<=K<=N`:

\[
\boxed{\sqrt{\mathcal E_{N,K}(h)}\le
\min\left(1,\frac{K+\sqrt{N-K}}N\right).}\tag{MS2}
\]

For **every** `K(N)=o(N)`, the right-hand side tends to zero for any
irrational or rational alpha, even the coherent constant-zero orbit.
This impressive-looking cancellation is therefore *not source-selected*.

For **fixed `K`** one can do better. All late/late off-diagonal terms
vanish, there are at most `K(K-1)` ordered early/early pairs, and for
`n>=K>m` the exact sinc bound yields

\[
|\Phi_K(h(16^n-16^m))|
\le\frac{16^{K-n+1}}{15\pi|h|}.
\]

The mixed sum is bounded by `512 K/(225*pi*|h|)`. Since `pi>3`, the
fully rational, uniform-in-source estimate is

\[
\boxed{\left|\mathcal E_{N,K}(h)-\frac1N\right|
\le\frac{K(K-1)+512K/(675|h|)}{N^2}.}\tag{MS3}
\]

For `K=o(sqrt(N))`, this proves `E_(N,K)=1/N+o(1/N)`, universally.
The small-scale Pascal/Haar details cannot by themselves identify pi.

In the opposite direction, **point recovery at the exact natural zero**
uses `|e(t)-e(u)|<=2*pi|t-u|<7|t-u|`. For every `0<=K<=N`,

\[
\boxed{\sup_{s\in I_K}|W_{N,h}(s)-W_{N,h}(0)|
\le \frac{2(N-K)}N+\frac{7|h|}{15N}.}\tag{MS4}
\]

For `K>=N` the sharper bound is

\[
\sup_{s\in I_K}|W_{N,h}(s)-W_{N,h}(0)|
\le \frac{7|h|}{15N\,16^{K-N}}.\tag{MS5}
\]

Thus when `K(N)=N-o(N)`, the cell energy tends to zero **if and only if**
`|W_(N,h)(0)|^2` tends to zero. For every fixed `h!=0` simultaneously,
Weyl's criterion then gives **an equivalent** normality gate. This
identifies an exponential observation-resolution boundary; it does not pay
the arithmetic signed estimate required to cross it.

## MS-03: exact zero-child Haar packet / scale telescope — PROVED PAPER

The sixteen child seed cells of `I_K` are
`I_(K,a)=[a/16^(K+1),(a+1)/16^(K+1)]`, `0<=a<16`.
Define their conditional energies `E_(N,K+1,a)` by averaging `|W|^2`
within each cell. Then

\[
\mathcal E_{N,K}=\frac1{16}\sum_{a=0}^{15}
\mathcal E_{N,K+1,a}.
\]

The unique **zero-child** is `a=0`, as required by the authentic
source-zero selector. Its signed Haar detail is

\[
\mathcal J_{N,K}=
\mathcal E_{N,K+1,0}-\mathcal E_{N,K}.
\]

It is NOT universally positive and is NOT time-chronological Haar
energy. It is an index-`K` seed-address filter. Ordinary finite DFT of
the sixteen child energies reconstructs `J` from its 15 nontrivial
character components. Exact telescoping gives

\[
\boxed{\mathcal E_{N,N}
=\frac1N+\sum_{K=0}^{N-1}\mathcal J_{N,K}.}\tag{MS6}
\]

By MS5, `|E_(N,N)-|W_(N,h)(0)|^2|<=14|h|/(15N)`.
Therefore

\[
\boxed{|W_{N,h}(0)|^2
=\frac1N+\sum_{K=0}^{N-1}\mathcal J_{N,K}
+O_h(1/N).}\tag{MS7}
\]

This is a **source-anchored tower with an exact arithmetic phase
integrand**: pi's four-pole source enters the complex phases of MS1,
while the zero selector follows a specific nested branch of the
sixteen-child pinbed. All the *formal* tower identities are valid for
counterseeds too. To prove normality one must derive a genuinely
original-zero signed estimate for their cumulative scale flux,
not assume it vanishes by lambda beta reduction.

## MS-04: an all-N, source-selected signed first detail — PROVED PAPER

**Theorem.** For the *authentic* zero seed `alpha=pi/16`, the
real-circle frequency `h=8` and every integer `N>=2`, the first
zero-child packet is **strictly positive**:

\[
\boxed{\mathcal J_{N,0}(8)
>\frac{16}{225\pi N^2}>0.}\tag{MS8}
\]

This theorem is **not** digit parity balance. The real-circle character
`e(8x)` is distinct from the step function `(-1)^floor(16x)`; the
latter has an infinite real Fourier expansion. The positive `N^-2`
packet does not prove any mean-decay or statistical contraction.

**Exact derivation.** When `K=1`, high/high cross terms vanish; only
pairs with one index zero survive. For `q_n=16^n-1` (always odd),

\[
\Phi_1(8q_n)=\frac{2i}{\pi q_n},
\qquad
\mathcal J_{N,0}(8)
=-\frac4{\pi N^2}\sum_{n=1}^{N-1}
\frac{\sin\big(16\pi q_n\alpha\big)}{q_n}
=-\frac4{\pi N^2}\sum_{n=1}^{N-1}
\frac{\sin\big(\pi^2(16^n-1)\big)}{16^n-1}.\tag{MS9}
\]

We now prove the sign, without fitting a sample. The classical Machin
identity `pi=16*arctan(1/5)-4*arctan(1/239)`, combined with the
alternating arctan series and its first omitted-term bound, produces
**exact rational** enclosures

\[
314159/100000<\pi<314160/100000.
\]

Therefore direct rational arithmetic gives

\[
\frac38<\delta:=\pi(15\pi-47)<\frac25.
\]

As `15*pi^2=47*pi+delta` and `47` is odd,
`sin(15*pi^2)=-sin(delta)`. The alternating sine bound gives

\[
\sin\delta\ge\delta-\delta^3/6
>\frac38-\frac{(2/5)^3}{6}
=\frac{1093}{3000}>\frac13.
\]

Thus the `n=1` summand in MS9 is `<-1/45`.
For every `n>=2`, use `|sin|<=1` and
`16^n-1>15*16^(n-1)` to get

\[
\sum_{n=2}^\infty\frac1{16^n-1}<\frac1{225}.
\]

The entire signed sum is therefore `<-1/45+1/225=-4/225`,
proving MS8 for **all `N>=2`**, with no analytic inference from finite
examples. The implementation's `certify_first_weyl8_detail` returns the
exact rational inputs to this argument. An independently evaluated
closed-form trigonometric formula matches the original finite
seed-integral computation for `N=2,4,8,16`.

**Hostile control.** For the coherent wrong seed `s*=-pi/16`, the
completed phase is alpha+s*=0. In MS9 every sine is zero, hence
`J_(N,0)(8;s*)=0`, while `W_(N,8)(s*)=1` for all N. This
separates the authentic finite packet sign from one important same-forcing
control, but does not establish uniqueness among possible source values.

**Scope:** This all-N signed fact uses the authentic completed value pi
and the correct origin. It does NOT use a new four-residue cancellation
bound: any source whose selected value is pi/16 has the same first packet.
It is genuine source-selected finite-*scale* information, not a proof
of the missing global source-specific innovation estimate.

## MS-05: next proof obligation (OPEN)

Fix any `K_N=N-o(N)`, e.g. `N-floor(sqrt(N))`. A sufficient and
necessary Weyl target is, for **every fixed nonzero integer h**,

\[
\boxed{\mathcal E_{N,K_N}(h)\longrightarrow0.}\tag{MS10}
\]

By MS7 this is equivalent to controlling the **signed cumulative**
zero-branch innovation `sum_(K<N) J_(N,K)`; the statistical contraction
in SUCC #590 would then follow indirectly from normality, although
its independently bounded `epsilon_N` is still to be constructed.

An actual advance would derive **from the exact BBP residues, zero seed,
all real carries, full future tail and global CRT winding** a bound on
a nontrivial range of the *deep* packets, say `K/N∈[c,1]` for fixed
`c>0`, that rejects `s*=-pi/16`, rational finite shadows, and the
quadratic-moment four-pole false source of #591. Merely proving MS8
for a fixed `K` is too weak: MS3 already bounds that contribution by
`O_K(N^-2)` for arbitrary alpha. A positive packet is NOT a
source-specific signed cancellation *across all levels*.

### Cross-branch provenance

- **#591** (`41bbbe56...`): corrected typed compiler, exact signed
  chronological CDF overlap, hostile source/seed barriers and full-suite
  validation. This dossier **adds** the seed-resolution dimension; it
  does not replace the time-block overlap.
- **#586**: authentic long-lag BBP difference sheet and Gaussian-circle
  anticlustering as a separate conditional route. Our all-N packet is
  a seed-window Fourier observable, not a source-attested Gaussian pullback.
- **#588**: prime–Archimedean 3/2 fiber and real sign certificates.
  Those finite signs do not give the all-epoch Fourier decay needed here.
- **#581**: analytic graph fixed point and strong non-Haar source
  mutants; uniqueness of a guarded analytic fixed point does not
  determine its selected digit law.
- **Bailey–Crandall 2001**: BBP-type orbit equivalence to normality is a
  classical imported source result, DOI 10.1080/10586458.2001.10504441.

### Claim ledger

| ID | Status | Boundary |
|---|---|---|
| MS-01 orthogonality, sinc kernel | PROVED PAPER | All real sources, all integer h!=0 |
| MS-02 spatial/local limits and fixed-depth bound | PROVED PAPER | No selected-zero signed decay |
| MS-03 zero-child packet and telescope | PROVED PAPER | Representation of existing Weyl obstruction |
| MS-04 first authentic h=8 sign | PROVED PAPER + finite exact rational arithmetic | O(N^-2), not hexadecimal digit parity |
| MS-05 cumulative deep-packet decay | OPEN | Equivalent to original pi Weyl gate |
| Statistical D_N dyadic contraction | OPEN | No independently vanishing epsilon_N derived |
| Exact numerical sign from float diagnostics | OBSERVED only | Rational analytic sign witness is separate |
