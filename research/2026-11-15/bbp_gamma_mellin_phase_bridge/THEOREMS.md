# Exact successor–Gamma phase transport from the original four-pole BBP source

**Research dossier, 2026-11-15.** This is an additive theoretical construction, not a resolution of base-16 normality of pi, R0, completed Weil positivity or RH. These mathematical statements are paper derivations or classical facts under explicitly stated hypotheses; independent numerical/symbolic tests are weaker validation. Historical provenance: Main XXV; SUCC #634 and #638 Gamma; #646/#648/#649/#651 exact source and observers. No mathematical priority claim.

## 0. Source, types, and phase convention

Original source **unchanged**:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Let
\[
Q(t)=4-2t^3-t^4-t^5=(1-t)(t^2+2)(t^2+2t+2),
\quad g(t)=\frac{Q(t)}{16-t^8}
=\frac{1-t}{(2-t^2)(t^2-2t+2)}.
\]

The *classical imported BBP identity*, not proved by the new Gamma manipulations, gives `x=int_0^1 g(t)dt=pi/16`. Define `T_n=int_0^1 t^(8n)g(t)dt`, so `16^n x=U_n+T_n` and `r(n+1)=16 T_n-T_(n+1)`. This identity requires the actual zero-seeded rational history; in general the same forcing with seed s completes to `16^n(x+s)`.

Put `v=-8 log t` and
\[
K(v)=\frac18 e^{-v/8}g(e^{-v/8})\ge0,\qquad
T_n=\int_0^\infty e^{-nv}K(v)\,dv.
\tag{GM0}
\]

Complex powers below use the principal positive-real logarithm for `1-e^-v` and principal complex logarithm for powers of `1+i xi`. The circle Weyl character is `e(hz)=exp(2 pi i h z)`; the `2 pi` there fixes angle units and is NOT the opaque arithmetic input x.

## GM-01. The exact continuous-computational-depth successor law (PROVED PAPER)

For `Re z>0`, `Re beta>-2`, define
\[
\mathscr H(z,\beta)=\int_0^\infty e^{-zv}(1-e^{-v})^\beta K(v)\,dv.
\tag{GM1}
\]

This is jointly holomorphic on the displayed open domain by dominated convergence on compact subdomains. At `v->0`, `K(v)~v/64`, ensuring integrability whenever `Re beta>-2`; at infinity, `K(v)=O(e^{-v/8})`, ensuring convergence. At positive integral `beta=k`, binomial expansion yields
\[
\mathscr H(n,k)=\sum_{j=0}^k(-1)^j\binom kj T_{n+j}=(-1)^k\Delta^kT_n.
\]

For general complex beta the binomial expansion gives an absolutely convergent source-Newton series:
\[
\mathscr H(n,\beta)=\sum_{j\ge0}(-1)^j\binom\beta j T_{n+j},\quad \Re\beta>-2.
\tag{GM2}
\]
The coefficient asymptotic is `|binom(beta,j)|=O_beta(j^(-Re beta-1))` away from terminating integer series; `T_(n+j)=O((n+j)^-2)` makes the sum absolutely convergent. The source retains the same four rational poles at every term.

**Exact commuting square:** Multiplying the integrand by `1-e^-v` proves
\[
\boxed{\mathscr H(z,\beta+1)=\mathscr H(z,\beta)-\mathscr H(z+1,\beta).}\tag{GM3}
\]
Define `S f(z)=f(z+1)`. Then source production uses `(16-S)T_n=r(n+1)`, whereas observer fractional depth uses `(1-S)^beta T_n=\mathscr H(n,beta)` in this declared moment-domain functional calculus. The **phase coordinate transport is compulsory**: if `z=n(1+i xi)`, then `z+1=(n+1)(1+i xi')` with `xi'=n xi/(n+1)`. Holding xi fixed does not follow the same arrow.

## GM-02. All-four-pole endpoint jets and the complex Gamma expansion (PROVED PAPER)

The exact rational source yields, near `v=0`,
\[
\boxed{K(v)=\frac v{64}-\frac{7v^2}{1024}+\frac{55v^3}{24576}+O(v^4).}\tag{GM4}
\]
This follows by substituting `t=e^-v/8` in the original **factorized** `g(t)`, not fitting moments. Set `w=1+i xi`, real `xi`, and fixed `beta` with `Re beta>-2`. Then
\[
(1-e^{-v})^\beta K(v)
=\frac{v^{\beta+1}}{64}\left[
1-\frac{8\beta+7}{16}v
+\frac{48\beta^2+100\beta+55}{384}v^2+O_\beta(v^3)
\right].
\tag{GM5}
\]
Rescaling `y=nv`, integrating term-by-term against `e^(-w y)`, and using Euler's Gamma integral (principal branches) yields
\[
\boxed{\begin{aligned}
64 n^{\beta+2}\mathscr H(nw,\beta)
={}&\frac{\Gamma(\beta+2)}{w^{\beta+2}}
-\frac{8\beta+7}{16n}\frac{\Gamma(\beta+3)}{w^{\beta+3}}\\
&+\frac{48\beta^2+100\beta+55}{384n^2}
\frac{\Gamma(\beta+4)}{w^{\beta+4}}
+O_{\mathcal C}(n^{-3}).
\end{aligned}}\tag{GM6}
\]

The **additive** remainder is uniform for all real xi and beta in any fixed compact subset `C` of `Re beta>-2`: on rescaled y, `|exp(-i xi y)|=1`, and the local Taylor remainder can be bounded with an integrable `e^-y y^(Re beta+4)` majorant; the tail y>n^a is exponentially negligible. Uniform **relative** error is not asserted when |xi| grows, because the leading Gamma response decays.

This includes the source-fixed result `T_n=1/(64n^2)-7/(512n^3)+55/(4096n^4)+O(n^-5)`. At fixed beta, the exact source square (GM3) has the Gamma functional equation `Gamma(beta+3)=(beta+2)Gamma(beta+2)` as its leading asymptotic shadow. That is a mathematical source-to-continuum bridge, not an independent analytic continuation of every SUCC operation.

## GM-03. A calibrated *all-frequency* Gamma interferometer (PROVED PAPER; source-bound inherited from #634)

Define the original conditional Green source law (a **declared observer**, not a claim that pi's digits are random):
\[
\Pr(X_n\in dt)=\frac{t^{8n}g(t)}{T_n}\,dt,
\qquad Y_n=-8n\log X_n\in(0,\infty).
\tag{GM7}
\]
The rescaled density is `p_n(y)=e^-y K(y/n)/(n T_n)`. Write `h_n(y)=64n K(y/n)` and `Z_n=64n^2 T_n`. Because `D(t)=(2-t^2)(t^2-2t+2)>=1` for 0<=t<=1,
\[
0\le K(v)=\frac{t(1-t)}{8D(t)}\le\frac v{64},
\qquad 0\le h_n(y)\le ye^{-0y}=y.
\]
The **Gamma(2,1) density** `q(y)=y e^-y` therefore decomposes *pointwise* as
\[
q(y)=Z_n p_n(y)+[q(y)-e^{-y}h_n(y)],
\]
and the bracket has total mass `1-Z_n>=0`. This gives
\[
\boxed{\operatorname{TV}(\mathrm{Law}(Y_n),\operatorname{Gamma}(2,1))
\le1-64n^2 T_n\le\frac7{8n}.}\tag{GM8}
\]
The last explicit rational bound is the inherited original-source beta lower bound in SUCC Gamma Genesis #634, with `m=8n`; it is not independently sourced from the finite numerical audit.

Now preserve **both independent phase labels**:
\[
\Psi_n(\xi,\omega)=
\mathbb E[e^{-i\xi Y_n}Y_n^{i\omega}],\quad \xi,\omega\in\mathbb R.
\]
Since the observable has modulus one, the `2 TV` dual inequality and classical Gamma integration imply
\[
\boxed{\sup_{\xi,\omega\in\mathbb R}
\left|\Psi_n(\xi,\omega)-
\frac{\Gamma(2+i\omega)}{(1+i\xi)^{2+i\omega}}\right|
\le2(1-64n^2 T_n)\le\frac7{4n}.}\tag{GM9}
\]
No observed source digit or rational phase has been randomized by this theorem. The observable is defined on the **source-conditioned endpoint law** only. The all-frequency statement is an *additive error*, not a uniform invertibility assertion; at high frequencies the reference signal is tiny.

**Operational transport defect:** the fractional finite-difference observer uses `(n(1-e^-v))^(i omega)` whereas the calibrated log-source observer uses `(nv)^(i omega)`. Their ratio is the explicit phasor `[(1-e^-v)/v]^(i omega)`. For fixed omega, this tends one under the conditioned source as n grows. For omega growing with n, its phase deviation can remain order one; the two charts are NOT silently identical. This is a concrete phase-frame transport that must be paid before claiming high-frequency coherence.

## GM-04. Four-time causal-lag crossover creates Gamma shape 3 (PROVED PAPER)

For positive integer lag ell and positive integer q, define the authentic source-time difference window
\[
\mathscr D_{n,q,\ell}(\xi,\beta)
=\int_0^\infty e^{-(1+i\xi)nv}
(1-e^{-qv})(1-e^{-\ell v})(1-e^{-v})^\beta K(v)dv.
\tag{GM10}
\]
At zero twist it is the **actual positive four-time Green defect**:
\[
D_{n;q,\ell}=T_n-T_{n+q}-T_{n+\ell}+T_{n+q+\ell}>0.
\tag{GM11}
\]
For fixed xi,beta (`Re beta>-2`) and ell, if `q_n/n->c in (0,infinity]`, then
\[
\boxed{\begin{aligned}
\lim_{n\to\infty} n^{\beta+3}\mathscr D_{n,q_n,\ell}(\xi,\beta)
=\frac{\ell\Gamma(\beta+3)}{64}
\left[w^{-(\beta+3)}-(w+c)^{-(\beta+3)}\right],
\end{aligned}}\tag{GM12}
\]
where the second term is 0 for c=infinity and `w=1+i xi`.
If `q_n=o(n)` (including fixed q), instead
\[
\boxed{\frac{n^{\beta+4}}{q_n}\mathscr D_{n,q_n,\ell}(\xi,\beta)
\to\frac{\ell\Gamma(\beta+4)}{64w^{\beta+4}}.}\tag{GM13}
\]
Both follow by `y=nv`, `K(y/n)~y/(64n)`, `1-e^(-ell y/n)~ell y/n`, and dominated convergence. If `q_n/n->c`, the remaining factor converges to `1-e^(-cy)`; for c=0 divide by q_n/n first. The corresponding Laplace integrals are exactly the displayed Gamma expressions.

For beta=xi=0, ell=2:
- q fixed: `D_(n;q,2) ~ 3q/(16n^4)`;
- `q/n->c>0`: `D_(n;q,2) ~ [1-(1+c)^(-3)]/(16 n^3)`;
- `q/n->infinity`, including original BBP circle-critical `q~64n^2`: `D_(n;q,2) ~ 1/(16n^3)`.

The last is a **sharp** asymptotic strengthening of the earlier #651 uniform `O(n^-3)` upper bound. The log-phase at saturated large q tends to the **Gamma(3+i omega)** form, because the small additional time lag supplies one further boundary power. The different thresholds `q~n` (source-moment saturation) and `q~n²` (circle carry from `q T_n~1`) must never be merged without an explicit two-scale transport argument.

## GM-05. Reconstruction and conditioning: Gamma cancellation is not information annihilation (CLASSICAL/PROVED)

Let `T_z=int_0^infinity e^-zv K(v)dv` for `Re z>-1/8`, which is analytic there because `K(v)=O(e^-v/8)` as v->infinity. For every fixed `c>0`, the complex vertical Fourier response `omega->T_(c+i omega)` reconstructs the whole source density:
\[
\boxed{K(v)=\frac{e^{cv}}{2\pi}\int_{-\infty}^\infty T_{c+i\omega}e^{i\omega v}d\omega,\qquad v>0.}\tag{GM14}
\]
The integral is absolutely convergent: extend `e^-cv K(v)` by zero to v<0. It is continuous and piecewise smooth, vanishes at 0, and its second derivative is integrable. Two integrations by parts give `T_(c+i omega)=O_c(|omega|^-2)`. Thus a **full complex** Fourier basis recovers the source. Magnitudes alone do not generally determine phase or source location.

For the canonical log-Gamma window, `Gamma(sigma+i omega)` is zero-free, with `|Gamma(sigma+i omega)|~sqrt(2pi)|omega|^(sigma-1/2) exp(-pi|omega|/2)` at fixed sigma>0. Hence its high-frequency inverse is exponentially ill-conditioned even though individual frequencies have not been exactly erased. These classical facts are documented in NIST DLMF §§5.2 and 5.11.

**Noncommuting square:** For a nondegenerate positive T, `E exp(i omega log T)=Gamma(sigma+i omega)/Gamma(sigma)` for T~Gamma(sigma,1), whereas `exp(i omega E log T)=exp(i omega psi(sigma))` has modulus exactly one. The correct Fourier operation is the *expectation of the phase*, not the phase of the expectation. SUCC #651's Bernoulli pi coin gives an even more severe wrong-order control: `E e(h16^n C)=1` although `e(h16^n E C)` equals the actual nonconstant pi circle phase.

## GM-06. No-go and actual π-normality gate (PROVED COUNTERMODEL / OPEN ARITHMETIC)

All quantities above built only from `r(n),g,K,T_n` are **seed-blind**. Keep precisely the original forcing but choose the coherent counterseed `s=-x`. Then `U_n(s)=-T_n`, so completed real orbit `U_n(s)+T_n=0` for every n; this orbit is nonnormal, despite having *identical* `Gamma` source windows, mixed moments and four-time Green defects. Therefore **source-only Gamma cancellation, positive energy and phase transport cannot entail pi normality** without a source-selected phase/zero-anchor cross-correlation estimate.

With the actual zero seed `s=0`, the real phase is
\[
e(h16^nx)=e(hU_n)\exp\left(2\pi ih\int_0^\infty e^{-nv}K(v)dv\right).
\tag{GM15}
\]
At fixed h, `|exp(2pi i h T_n)-1|<=2pi|h| T_n=O_h(n^-2)`; the difficult long-time behavior is in `e(hU_n)` and full winding, not the small positive source tail. Since finite fixed-depth Gamma windows converge to explicit nonzero coefficients, multiplying Weyl summands by them merely reweights the still-open sum; it does not prove decay.

**Verdict-changing condition:** establish a genuinely source- and seed-attached signed inequality that constrains `e(h U_n)` jointly with phase-preserving `Gamma`/Mellin observations, full odd-denominator and CRT winding, and a predetermined finite time-lag family. It must separate original zero seed from coherent wrong seed and the #648 coboundary mutant. Show an all-large-shell fixed-h saving (or a prescribed positive R0 margin), not merely an all-harmonic detector, a Gamma response, finite checks or a moving-lag phase contrast. The attempt to infer pi normality from source-only Gamma attenuation is REFUTED by the counterseed; whether a strengthened joint operator gives such a saving is **UNVERIFIED**.
