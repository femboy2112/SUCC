# Seeded arithmetic–analytic seam: a horizontal selector and a Zak band

**2026-10-31 research-only.** Exact source is the original unmodified signed four-pole BBP recurrence with literal `U_0=0`; the source is fixed throughout, except where a counterseed is explicitly declared. **π base-16 normality and RH remain OPEN.** Most instruments here (difference equations, Poisson summation, Zak transforms, Mellin change of variable, Fourier orthogonality) are classical; the source-specific synthesis is newly organized for SUCC and does not claim academic priority.

## 1. Declared objects and the real-time successor problem

For every real `x >= 1`, define the *authentic* rational function

\[
r(x)=\frac4{8x-7}-\frac2{8x-4}-\frac1{8x-3}-\frac1{8x-2}.
\]

For `t >= 0` its positive future Green tail is

\[
T(t)=\sum_{j\ge1}16^{-j}r(t+j)
=\int_0^1 \frac{u^{8t}P(u)}{16-u^8}\,du,
\qquad P(u)=4-2u^3-u^4-u^5>0\quad(0<u<1).
\]

The sum converges locally uniformly and `T` is real analytic for `t >=0`; differentiating under the integral is valid there. Direct index shift gives

\[
16T(t)-T(t+1)=r(t+1),\quad
\alpha:=T(0)=\sum_{j\ge1}16^{-j}r(j)=\pi/16.
\tag{SZ-1}
\]

These are *inherited source facts* from the authentic BBP/Green program. The exact finite telescope, for `T_J(t)=sum_{j=1}^J16^{-j}r(t+j)`, is

\[
16T_J(t)-T_J(t+1)=r(t+1)-16^{-J}r(t+J+1).
\tag{SZ-1F}
\]

On positive integers the zero-seeded recurrence is

\[
U_0=0,\quad U_{n+1}=16U_n+r(n+1),\quad U_n=16^n\alpha-T(n).
\tag{SZ-2}
\]

All statements on π depend on keeping the literal original four poles and the selected zero boundary. A source-moment fake, finite-jet match, or freely chosen q must NOT be substituted.

## 2. The missing continuum degree of freedom is precisely a 1-periodic function

**Theorem SZ-03 (elementary, all-continuum-solution classification).** Let `U:[0,infty)->R` be continuous and satisfy

\[
U(t+1)-16U(t)=r(t+1)\quad\forall t\ge0.
\]

Then

\[
Q(t):=16^{-t}(U(t)+T(t))
\quad\text{obeys}\quad Q(t+1)=Q(t).
\tag{SZ-3}
\]

Conversely every continuous 1-periodic `Q` defines a solution `U_Q(t)=16^tQ(t)-T(t)` satisfying that real-time recurrence. If `U(0)=0`, then the only restriction imposed by the integer initial condition is `Q(0)=T(0)=alpha`. Therefore the original integer samples do not uniquely determine the analytic continuum section.

*Proof.* Adding `T(t+1)-16T(t)=-r(t+1)` to the U-equation makes `U+T` multiply by 16 under `t->t+1`; division by `16^t` yields periodicity. The converse follows by reversing the algebra. At `t=0`, `U(0)=Q(0)-T(0)`. QED.

**Hostile exact interpolation.** For ANY real epsilon,

\[
Q_\epsilon(t)=\alpha+\epsilon\sin(2\pi t),\quad
U_\epsilon(t)=16^tQ_\epsilon(t)-T(t).
\tag{SZ-4}
\]

All integer source states and the original `U_0=0` are identical to the canonical ones; the full real-time successor law still holds. At `t=j+1/4`, however, the change is *exactly* `2*16^j*epsilon`, and at `t=j+3/4` it is exactly `-8*16^j*epsilon`. Thus this is an honest, source-preserving **interpolation** mutation, not a changed arithmetic forcing, changed integer seed, or claim about physical chirality.

**Chosen horizontal selector / extra structure (not a theorem from integer data).** The Mellin/Green interpolation used in SUCC imposes

\[
\nabla Q:=dQ/dt=0\quad\text{on each unit cell},\qquad Q(0)=\alpha.
\tag{SZ-5}
\]

This selects the constant Q=alpha and hence the canonical U(t)=16^t alpha-T(t). The first requirement is a declared source/analytic transport convention; neither the initial integer condition nor the difference equation forces it. It provides a *typed seam-adequacy gate* for a proposed continuum-to-arithmetic proof.

## 3. Exact Zak construction: two orthogonal coordinates, one coherent seam

Fix `h in Z\{0}`, `N>=1`, and a C-infinity real bump `psi` supported in `(-1/4,1/4)` with `psi(0)=1`. Let `w_N(t)=sum_{n=1}^N psi(t-n)` and `g_{N,h,Q}(t)=w_N(t)e^{2 pi i h U_Q(t)}` (zero outside window support). This is smooth compactly supported. Set

\[
Z(t,\xi)=\sum_{k\in\mathbb Z}g(t+k)e^{-2\pi i k\xi}.
\tag{SZ-6}
\]

Every sum here is finite at fixed t. By substituting `k'=k+1`,

\[
Z(t+1,\xi)=e^{2\pi i\xi}Z(t,\xi),\quad
Z(t,\xi+1)=Z(t,\xi).
\tag{SZ-7}
\]

The transition `exp(2 pi i xi)` has winding one, so the Zak band is a section of a nontrivially glued complex line bundle over the 2-torus. Its twist is **UNIVERSAL** and **SEED-BLIND**; it does not predict nontrivial arithmetic curvature or π normality. All such sections necessarily have topological zeros somewhere, not necessarily at the selected sampling seam.

At the declared corner, because g(n)=e(h U_n) for `1<=n<=N` and vanishes at other integers,

\[
\boxed{Z(0,0)=\sum_{n=1}^N e(hU_n)=S_N(h).}\tag{SZ-8}
\]

The periodized function `Z(t,0)` has Fourier coefficients

\[
I_\ell=\int_{\mathbb R}g(t)e^{-2\pi i\ell t}dt.
\]

Since g is smooth compactly supported, Poisson/Fourier reconstruction converges absolutely:

\[
Z(t,0)=\sum_{\ell\in\mathbb Z}I_\ell e^{2\pi i\ell t},\quad
\sum_{\ell\in\mathbb Z}I_\ell=S_N(h),\quad
\int_0^1|Z(t,0)|^2dt=\sum_{\ell\in\mathbb Z}|I_\ell|^2.
\tag{SZ-9}
\]

The Fourier characters are L2-orthogonal over t, but the **point sampling functional** at t=0 adds their complex amplitudes. This is the exact sense in which the two modes can evolve orthogonally and cohere at the discrete seam. One must retain all off-diagonal cross terms in `|S_N(h)|^2` rather than claim L2 orthogonality automatically suppresses the point value.

A second Parseval identity uses the `xi` direction:

\[
\int_0^1\!\int_0^1|Z(t,\xi)|^2d\xi\,dt
=\int_{\mathbb R}|g(t)|^2dt
=N\int_{\mathbb R}|\psi(t)|^2dt.
\tag{SZ-10}
\]

This GLOBAL norm is independent of source/seed because the phase has unit modulus and window supports are disjoint. The same-source coherent counterseed `q=1/5` from SUCC FP-06 yields `S_N(h)=N e(h/5)+O_h(1)` for each fixed h. Hence

\[
\frac{|Z(0,0)|}{\|Z\|_{L^2([0,1]^2)}}\asymp_h\sqrt N.
\tag{SZ-11}
\]

No uniform-in-N point trace bound by this norm exists on the allowed same-source seed family. A claim deducing selected π normality solely from universal Zak/Parseval energy is **REFUTED** by this authentic-forcing hostile seed.

## 4. Exact Mellin-frequency version of the aliases

For the SOURCE-SELECTED constant section `Q=alpha` only, put `y=16^t` and use `dt=dy/(y log16)`:

\[
\boxed{I_\ell(q,h)=\frac1{\log16}\int_0^\infty
w_N(\log_{16}y)
\exp\!\left(2\pi ih\left(yq-T(\log_{16}y)\right)\right)
\,y^{-1-2\pi i\ell/\log16}\,dy.}\tag{SZ-12}
\]

This is a genuine Mellin–Fourier sampling formula on the multiplicative positive-real group. The lattice `ell in Z` is the dual of discrete additive successor in logarithmic time. **This equation is an exact change of variables, not a signed estimate**. It shows where the rational original source, continuous Green tail and sampled radix phases meet in one operational band.

## 5. Interpolation ambiguity is measurable: individual aliases are NOT arithmetic invariants

The exact integer-sampled S_N is unchanged under the periodic Q-epsilon mutation SZ-4, but individual I_l generally change. This is not merely an assertion: in the r=0 toy, set q=0, N=1, any smooth even positive bump `psi` as above. Then

\[
I_0(\epsilon)=\int\psi(t-1)\exp(2\pi ih\epsilon16^t\sin2\pi t)dt,
\]

so at `epsilon=0`,

\[
I_0'(0)=2\pi ih16\int_0^{1/4}\psi(s)
\left(16^s-16^{-s}\right)\sin(2\pi s)\,ds\ne0\quad(h\ne0).
\tag{SZ-13}
\]

Each real factor inside the last integral is positive for `0<s<1/4`; the derivative is nonzero imaginary. All INTEGER sample values nevertheless remain 1 for this toy and all `epsilon`, so `sum_l I_l(epsilon)=1`. Thus alias contributions redistribute under a continuum interpolation gauge even though their recombined arithmetic seam is invariant. The same periodic deformations SZ-4 exist for the authentic four-pole recurrence; the toy furnishes a decisive elementary noninvariance receipt for the general alias-component claim.

This yields a source-map rule: **aliases by themselves are NOT invariants of the sampled source**. To cite an individual alias as arithmetic evidence, SUCC must declare and authenticate the interpolation (here the actual Mellin/Green T plus the horizontal Q=alpha) and retain any residual dependence on the chosen smooth window.

## 6. What this does and does not buy for π

- **Disclosed / classical**: SZ-1–4 exact finite/source identities, Q-periodic interpolation classification, universal Zak sewing/isometry, Fourier/Mellin Poisson reconstruction, seed-blind norm no-go, explicit alias-gauge counterexample.
- **New-to-SUCC structural use**: separate (a) exact arithmetic seed `U_0=0`, (b) source-attested Mellin tail `T`, (c) chosen constant horizontal section `Q`, (d) Zak line-bundle twist, (e) selected seam evaluation. Do not conflate them.
- **OPEN**: derive an authentic zero-seeded all-horizon **signed** inequality for `sum_{ell !=0} I_ell(alpha,h)=o(N)` or the inherited equivalent `S_N(h)=o(N)` for every fixed nonzero integer h. The known selected zero-mode O_h(1) bound alone does not do this. No RH inference.

**Next verdict-changing probe**: construct a source-sensitive horizontal-section constraint or joint three-channel/lag alias estimator with a NONTAUTOLOGICAL inequality that holds at `Q=alpha` and has an explicit failure on `q=1/5`; control its alias tails uniformly as N grows, with independent altered-interpolation Q-epsilon tests and positive Beta source mutants. A re-expression of the Weyl criterion under Zak/Mellin without signed saving is NOT a proof breakthrough.

**References (classical instruments)**: Zak quasi-periodic unitary band: https://link.springer.com/article/10.1007/s00208-018-1719-3 ; Mellin–Poisson sampling: https://www.eurasip.org/Proceedings/Ext/SampTA2013/papers/p277-butzer.pdf ; Poisson summation: https://www2.math.upenn.edu/~gressman/analysis/14-poisson.html ; exact original source/alias counterseed: SUCC PR #437 `research/2026-10-31/four_pole_path_interference/PROOFS.md`; canonical selected lag frontier: Main XVIII `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`.
