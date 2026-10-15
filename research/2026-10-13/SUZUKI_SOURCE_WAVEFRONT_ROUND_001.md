# SUZUKI / OPERATION WAVEFRONT — Source-correct positive bath, sharp prime activation, and finite small-interval certification

**Date:** 2026-10-13 (New York). **Base:** `femboy2112/SUCC` branch `research/dsv4-periodic-tail-enclosure-2026-10-13` at **`fb4fb91d46218ac121f4a4887f7322e79d3d0b70`**. **Research branch:** `research/suzuki-source-boundary-wavefront-2026-10-13` (draft, intentionally not `main`). **Reference:** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, **arXiv:2606.09096v3** (23 Sep 2026), https://arxiv.org/html/2606.09096v3 , particularly (1.3), (1.5)–(1.8), (2.3)–(2.5), (8.2), (8.7). **Status:** exact classical/source-derived functional analysis, **PROVED LOCAL** new-to-project explicit inequalities, **TESTED FINITE** exact rational implementation, **UNVERIFIED** global RH implication/novel priority/Lean refinement. **RH PROVED: no.** No nontrivial zero locations are read in any construction. No merge to main authorized.

## 0. Research question and what is different from previous SWARM work

Suzuki's localized real-even continuous screw function is

\[
\boxed{g(t)=-4(e^{|t|/2}+e^{-|t|/2}-2)
-\frac{|t|}{2}(\psi(1/4)-\log\pi)
-\frac14\bigl(\Phi(1,2,1/4)-e^{-|t|/2}\Phi(e^{-2|t|},2,1/4)\bigr)
+\sum_{p^k\le e^{|t|}}\frac{\log p}{p^{k/2}}(|t|-k\log p).}
\tag{SW-0}
\]

The source is the **actual** von Mangoldt function, not an Euler-looking arbitrary impulse. Define `G_a=P_a(g*·)P_a` on the mean-zero Hilbert space `L_0²(-a,a)`. For `v\in C_c^\infty(-a,a)` put `u=i v'`. Suzuki identifies
\[
Q_W^a(v)=\langle G_a u,u\rangle,
\qquad \|v\|_2^2=\langle K_a u,u\rangle,
\quad K_a=(-\Delta_N)^{-1}.
\]

This project does **not** manufacture an arbitrary positive covariance and identify it with Weil. Instead it takes Suzuki's *already authenticated analytic explicit formula* as input, decomposes it into a genuine positive part and genuine signed parts, and proves what a finite observer can and cannot certify.

## SW-1. Exact prime-wavefront operator theorem (PROVED LOCAL; classical distributions)

For a prime power `n=p^k`, let `ell=log n`, `c=log p/sqrt(n)>0` and `g_n(t)=c(|t|-ell)_+`. If `2a<=ell`, `g_n(x-y)=0` almost everywhere on `(-a,a)^2`. If `ell/2<a<ell`, let `delta=2a-ell\in(0,a)`, and define left and right boundary strips
\[
L=(-a,a-\ell),\qquad R=(-a+\ell,a),\qquad |L|=|R|=\delta.
\]

Then the raw *unprojected* convolution integral operator has the exact Hilbert–Schmidt norm
\[
\boxed{\|G_{n,a}^{\mathrm{raw}}\|_{\mathrm{HS}}^2=\frac{c^2\delta^4}{6}.}\tag{SW-1a}
\]

**Proof.** The kernel is supported on the two triangles `|x-y|>ell`; the measure density of pairs of separation `r` is `2(2a-r) dr`. Thus the integral of the squared kernel is `2c² int_ell^(2a) (2a-r)(r-ell)^2 dr = c²delta⁴/6`. The zero-mean projected `P_a G_{n,a}^{raw}P_a` has HS norm no greater than this; **do not conflate the raw and projected norms**.

Distributionally, `g_n''=c(delta_Dirac(t-ell)+delta_Dirac(t+ell))`. Integrate by parts against `u=i v'` for `v\in H_0^1(-a,a)` to obtain
\[
\boxed{Q_n(v)=-2c\operatorname{Re}\int_{-a}^{a-\ell}v(x+\ell)\overline{v(x)}\,dx.}\tag{SW-1b}
\]
This is exactly Suzuki (2.5)'s finite prime contribution, not a new sign convention. Relative to `L²(L)\oplus L²(R)\oplus L²(( -a,a)\setminus(L\cup R))`, the bounded quadratic-form operator is
\[
B_{n,a}=c\begin{pmatrix}0&-I&0\\-I&0&0\\0&0&0\end{pmatrix}
\]
where the identity uses the lawful translation `x\mapsto x+ell` from L to R. Thus **its operator norm is exactly `c` for every `delta>0`**, with both signs `+c,-c`, but is zero at `delta=0`.

\[
\boxed{\|B_{n,a}\|_{\rm op}=c \quad(\ell/2<a<\ell),\qquad
\lim_{a\downarrow\ell/2}\|G_{n,a}^{raw}\|_{HS}=0.}\tag{SW-1c}
\]

This is a **sharp, source-correct operator-topology obstruction**: tiny continuous-kernel/HS error does not control the differentiated Weil-form (or generalized `G_a,K_a`) relative error. The operator families act on changing intervals; under canonical zero extension to `L²(R)`, `B_{n,a}` **does** tend strongly to zero on fixed vectors, because the strips shrink. It does not converge in operator norm. There is no contradiction with Suzuki's continuous `lambda_a`.

For the first prime wavefront, choose `a=(3/5)log2`. Then `2a=(6/5)log2<log3` follows **exactly** from `2^6=64<3^5=243`; thus `n=2` is the **only** active prime-power source. The completed Archimedean contribution is still nonzero and must not be omitted.

## SW-2. Explicit chiral boundary tests (PROVED LOCAL; exact rational)

In units `ell=1`, take the tent `t(s)=min(s,delta-s)` on `[0,delta]`, extend by zero, and put `v_+=t_L+t_R`, `v_-=t_L-t_R` with `t_R(x)=t_L(x-ell)`.

\[
\|v_\pm\|_2^2=\frac{\delta^3}{6},\quad
\|v_\pm'\|_2^2=2\delta,\quad
\int t_L(x)t_R(x+\ell)dx=\frac{\delta^3}{12}.
\]
Consequently
\[
\boxed{Q_n(v_+)/\|v_+\|_2^2=-c,\qquad
Q_n(v_-)/\|v_-\|_2^2=+c,\qquad
\|v_\pm'\|_2^2/\|v_\pm\|_2^2=12/\delta^2.}\tag{SW-2}
\]

The ratios remain exact upon restoring physical length `ell`; the derivative ratio becomes `12/delta_physical²`. The nonzero source coupling is preserved despite endpoint width shrinking, but H¹ energy explodes like `delta^-2`. This is a **concrete realization cost** in a mathematical Sobolev carrier, not a verified physical energy-law or a sign for the full Weil form.

## SW-3. Uniform logarithmic-energy localization theorem (PROVED LOCAL, source-independent analytic tool)

Fix Fourier normalization `hat v(xi)=int_R v(x)e^{i xi x}dx`, and define the positive logarithmic energy
\[
\mathcal E(v)=\frac{1}{2\pi}\int_{\mathbb R}\log(e+|\xi|)|\widehat v(\xi)|^2d\xi.
\]
Let `E_delta` be both endpoint strips of length `delta` and `Q_n(v)` be SW-1b. For every `R>=1` and `v` in the `H^{log}` form domain,
\[
\boxed{\frac{|Q_n(v)|}{c}\le
\frac{4\delta R}{\pi}\|v\|_2^2+
\frac{2\mathcal E(v)}{\log(e+R)}.}\tag{SW-3a}
\]

**Proof.** `|Q_n(v)|/c <= int_{E_delta}|v|²` by Cauchy–Schwarz. Split `v=v_{<=R}+v_{>R}` in Fourier frequency. Cauchy–Schwarz/Plancherel yields `||v_{<=R}||_∞² <= R ||v||²/pi`. The union of strips has length `2delta`, hence `int_E |v_{<=R}|² <=2delta R||v||²/pi`. Also `||v_{>R}||² <= E(v)/log(e+R)`. Apply `|a+b|²<=2|a|²+2|b|²`. QED.

Set `R=2^m`. The **completely rational bound**
\[
\boxed{\frac{|Q_n(v)|}{c}\le\frac43\delta 2^m\|v\|_2^2+\frac3m\mathcal E(v)}\tag{SW-3b}
\]
follows from `pi>3` and `log(e+2^m)>m log2>2m/3`. Taking `delta=2^{-2m}`, any unit-norm state realizing the *full* chiral response `|Q_n(v)|=c` obeys the **rational lower bound**
\[
\boxed{\mathcal E(v)\ge\frac m3\left(1-\frac{4}{3\,2^m}\right)\|v\|_2^2.}\tag{SW-3c}
\]

Therefore the prime contribution vanishes uniformly on bounded logarithmic-energy balls at wavefront onset, despite its fixed L² operator norm. The math is stronger than the analogy: it exhibits explicitly **which carrier energy budget prevents the Hilbert-space norm jump from destabilizing regular low-energy observers**. Neither bound alone proves RH or even positivity past first activation.

## SW-4. Exact Archimedean source factorization into positive OU bath and signed finite-rank terms (PROVED LOCAL)

Use the classical exact special value `psi(1/4)=-gamma-pi/2-3log2`. Set
\[
\alpha_j=2j+\frac12,\qquad
C=\gamma+\frac\pi2+3\log2+\log\pi,
\qquad R_{\alpha,a}u(x)=P_a\int_{-a}^a e^{-\alpha|x-y|}u(y)dy.
\]

Since
\[
e^{-t/2}\Phi(e^{-2t},2,1/4)=4\sum_{j=0}^\infty e^{-\alpha_jt}/\alpha_j^2,
\]
the **exact complete** nonprime part of (SW-0), for `t=|t|`, is
\[
g_\infty(t)=-8(\cosh(t/2)-1)+\frac C2 t
-\sum_{j\ge0}\frac{1-e^{-\alpha_jt}}{\alpha_j^2}.
\]

On `L_0²(-a,a)`, the constant-kernel terms annihilate all input. By `int int |x-y|u(x)conj u(y)=-2<K_a u,u>` and `cosh((x-y)/2)=cosh(x/2)cosh(y/2)-sinh(x/2)sinh(y/2)`, we have **the exact operator identity**
\[
\boxed{G_a^{\infty}=
\sum_{j\ge0}\alpha_j^{-2}R_{\alpha_j,a}
-C K_a+8|P_a\sinh(x/2)\rangle\langle P_a\sinh(x/2)|
-8|P_a\cosh(x/2)\rangle\langle P_a\cosh(x/2)|.}\tag{SW-4}
\]

The OU bath is **source-derived positive**: `Fourier[e^{-alpha|t|}](xi)=2alpha/(alpha²+xi²)>0`; hence `R_alpha,a` is PSD for every finite interval. It is not the full Weil form. In particular, the signed `-C K_a`, pole rank-one modes, and the authentic von Mangoldt shift pieces cannot be silently dropped to claim RH.

**Certified tail.** For `A=2N+1/2`, the monotone integral bound yields
\[
\frac1{2A}\le\sum_{j\ge N}\frac1{\alpha_j^2}\le\frac1{2A}+\frac1{A^2}.
\]
On `L_0²(-a,a)`, the **positive** omitted OU bath has operator norm at most
\[
\boxed{2a\left(\frac1{2A}+\frac1{A^2}\right).}\tag{SW-4tail}
\]
This bound is *valid for compact G_a*, not directly for `D* G_a D` relative to the `L²(v)` metric.

**Full source-sign problem.** Given the genuine arithmetic prime source, the missing RH-strength inequality is **precisely**
\[
\sum_j\alpha_j^{-2}R_{\alpha_j,a}+
8|P_a\sinh\rangle\langle P_a\sinh|
\quad\succeq\quad C K_a +8|P_a\cosh\rangle\langle P_a\cosh| - \sum_{p^k\le e^{2a}}G_{p^k,a}
\tag{SW-4goal}
\]
on `L_0²(-a,a)` for **all** `a>0`, with the sign convention `G_prime=+c(|x-y|-ell)_+` on `u`, a genuinely indefinite contribution. **This global inequality is NOT established.** Finite-dimensional PSD probes do not establish it.

## SW-5. Explicit **unconditional full-space positivity** for `a<=1/12` (PROVED LOCAL with rational certificates)

This is an actual non-numerical spectral lower bound, not an empirical plot. Work first with `v\in C_c^\infty(-a,a)`, `u=iv'`. Before the first prime (`2a<log2`), the exact source expression SW-4 gives
\[
Q_W^a(v)=\sum_{j\ge0}\left[
\frac{2}{\alpha_j}\|v\|_2^2-
\iint e^{-\alpha_j|x-y|}v(x)\overline{v(y)}dxdy\right]
-C\|v\|_2^2
+2\left|\int v\cosh(x/2)dx\right|^2
-2\left|\int v\sinh(x/2)dx\right|^2.
\tag{SW-5a}
\]

Every bracket is PSD, since it equals `alpha_j^-2 <R_alpha u,u>`. Schur's bound for the exponential kernel on `(-a,a)` gives
\[
\sup_x\int_{-a}^a e^{-\alpha|x-y|}dy
=\frac2\alpha(1-e^{-\alpha a}),
\]
and hence
\[
\frac2\alpha\|v\|_2^2-\iint e^{-\alpha|x-y|}v(x)\overline{v(y)}dxdy
\ge\frac{2e^{-\alpha a}}\alpha\|v\|_2^2.
\]

Drop the **positive** remaining OU tail and the positive cosh rank-one form. Use Cauchy–Schwarz and
`int_(-a)^a sinh²(x/2)dx = sinh(a)-a`. It follows **for every** `N>=1` and `2a<log2` that
\[
\boxed{\lambda_a\ge
\sum_{j=0}^{N-1}\frac{2e^{-\alpha_j a}}{\alpha_j}
-C-2(\sinh a-a).}\tag{SW-5b}
\]

The RHS decreases with `a`, so a positive bound at `a0` holds for **every** `0<a<=a0`. We implement **outward rational bounds**, not floating numerical constants, for:
- `pi=16 arctan(1/5)-4 arctan(1/239)` with alternating rational Taylor enclosures;
- `log 2` and `log pi` by nonnegative `atanh((x-1)/(x+1))` series with certified geometric tails;
- Euler `gamma` via `H_M-log M -1/(2M) < gamma < H_M-log M -1/(2(M+1))`;
- `exp(±q)` with positive rational Taylor and a geometric majorant of the remainder;
- every finite gamma bath coefficient from its authenticated `alpha_j=2j+1/2`.

Take **a0=1/12, N=64**. The exact interval computation produces a rigorous, downward-rounded bound
\[
\boxed{\lambda_a\ge\frac{281025667}{10^{10}}=0.0281025667>0\quad \forall 0<a\le1/12.}\tag{SW-5c}
\]

It uses the **whole function space** `C_c^\infty` and extends through Suzuki's Friedrichs closed-form core; the 64 exponentials supply a finite *analytic lower bound*, not a 64-dimensional Galerkin truncation. This is an explicit constructive instance of Suzuki's already known "lambda_a>0 for a sufficiently small", not a newly discovered route to RH. It is independently reproduced by `certified_prime_free_small_interval(1/12,64)` and exact Python regressions.

**Falsification:** this crude universal Schur bound does **not** remain positive up to the first prime threshold: at `a=(log2)/2`, even the full infinite sum evaluates to a bound around `-1.539...`. This REFUTES an attempted shortcut "keep taking more OU modes and the elementary Schur bound will prove positivity beyond prime onset." The loss is in the inequality itself, not its finite cutoff.

## SW-6. A second sharp no-go: small compact Gamma tail does not control differentiated tail (PROVED LOCAL)

Fix any `N>=1` and let `R_N=Σ_(j>=N)alpha_j^-2 R_alpha,a`, the **positive** omitted bath on mean-zero `u`. SW-4tail yields `||R_N||_op=O_a(1/N)`. But after applying `D=i d/dx` to `v`, the full-line Fourier multiplier of the differentiated tail is
\[
m_N(\xi)=\sum_{j\ge N}\frac{2\xi^2}{\alpha_j(\alpha_j^2+\xi^2)}.
\]
For every `alpha_j<=|xi|`, the summand is at least `1/alpha_j`; therefore
\[
m_N(\xi)\ge\sum_{N\le j:\alpha_j\le|\xi|}\frac1{\alpha_j}
\xrightarrow[|\xi|\to\infty]{}\infty.
\]
Choose a nonzero fixed `chi\in C_c^\infty(-a,a)` and `v_omega(x)=chi(x)e^{i\omega x}`. Its Fourier mass translates to frequencies near omega, so `Q_tail(v_omega)/||v_omega||²\to\infty`. Consequently **the differentiated tail is unbounded relative to the bare `L²(v)` norm for every finite OU cutoff**, despite the compact `G_a` tail tending to zero in operator norm.

This is precisely the dangerous **change-of-carrier-metric** effect that naive Galerkin/Schur certificates ignore. The crucial constructive repair is that the tail is **positive**: it can be dropped in any lower quadratic-form estimate without estimating its absolute differentiated norm! SW-5 exploits exactly this one-sided direction. This route is a better foundation for source-derived inequality certificates than attempting norm convergence of the unbounded Weil operator.

## SW-7. Complete real-place source interval evaluator (PROVED finite pointwise enclosure; TESTED)

`observational_succ/suzuki_arch_intervals.py` implements SW-0 at *exact rational arguments* `t in [0,2]` with rational outward intervals; all terms of the complete nonprime source are present: exponential pole pair, Euler/digamma term, and infinite Lerch/Gamma tail. It does **not** treat an arbitrary Gaussian test state as the original arithmetic source. For the Lerch component
\[
H(t)=\sum_{j\ge0}\frac{1-e^{-\alpha_jt}}{\alpha_j^2}
\]
and finite prefix through `j=N-1`, with `A=2N+1/2`, the remaining tail satisfies
\[
\boxed{\frac{t}{2(1+At)}\le H(t)-H_{<N}(t)\le\frac1{2A}+\frac1{A^2}.}\tag{SW-7}
\]
The lower bound follows from `1-e^{-At}>=At/(1+At)` and the decreasing-integral test; the upper uses `1-e^{-At}<=1` and the same test. Every exponential is bracketed with rational Taylor bounds. Numerically difficult very-small-`t` inputs may yield *wide* intervals, but they remain mathematically valid.

The implemented `first_source_screw_interval(t)` enforces `0<=t<(6/5)log2` by rational log2 lower enclosure and adds **only** genuine prime 2 with coefficient `log2/sqrt2` above its activation. Sample `t=3/4` yields, with 40 Lerch modes and 12-place outward rounding,
\[
-0.050505970992\le g(3/4)\le-0.050247605540.
\]
At `t=4/5`, it yields `[-0.042311733571,-0.042059406445]`. These brackets have independently been tested against `mpmath` evaluation of Suzuki's *original* digamma/Lerch formula at 50 digits; **the proof authority is the rational enclosures**, not the comparison with mpmath.

**Boundary:** Pointwise certified kernel values are not operator PSD certificates or certified `lambda_a` bounds at first-prime onset. The finite analytic positivity result SW-5 is independently whole-space and uses the exact source; it does not extrapolate sampled intervals to a spectrum.

## SW-8. Hostile mutants and negative controls

- **Fake 6:** `Lambda(6)=0`; no fake prime-6 jet appears. `n=4,8,9` are authenticated prime powers, correctly carrying `log p/sqrt(p^j)` and phase `log(p^j)`.
- **Wrong half-density:** claiming `n^{-2/3}` instead of `n^{-1/2}` is rejected by the *typed source contract*, not by fitting measured zeros.
- **Wrong phase:** claiming `log2` instead of `log4` for jet `n=4` fails source authentication.
- **Wrong threshold:** at `a=3/5 log2` the only active jet is 2 by exact `2^6<3^5`; inserting jet 3 or composite 6 would be a fabricated observation.
- **Weak-limit/strong-limit:** raw `G_n` is small in HS as the wavefront approaches, but `B_n` has constant norm. Finite operator-norm transport is a REFUTED shortcut.
- **Finite OU cutoff:** the omitted gamma tail is positive on `u`, but unbounded after differentiating on bare `L²(v)`; using its small compact-kernel norm as an `A_a` bound is REFUTED.
- **Physical interpretation:** an OU exponential kernel is a positive mathematical covariance, not a measured thermal bath. The entire signed factorization comes from Suzuki's authentic explicit formula; no claim of Higgs-source identification is made.

## SW-9. Verdict, practical connection to MATRYOSHKA, and next rounds

**Survives:** exact source-typed prime operator onset, explicit chiral boundary test vectors, two distinct operator topologies, quantitative log-energy cost, a complete source-derived signed OU factorization, an explicit all-source small-interval positivity lower bound, and exact rational pointwise real-place completion certificates. These are genuinely on the Suzuki route and require *no* nontrivial-zero oracle. Mathematical components (Schur estimates, OU PSD, Fourier splitting, compact positive tails) are classical; this particular verified assembly is new to the project, and academic novelty is **unreviewed**.

**Does not survive:** treating positive OU covariance as completed Weil positivity, deducing differentiated-form control from small `G_a` HS error, or extrapolating the crude Schur lower bound to prime thresholds. RH still requires a **new source-sensitive domination inequality**, global over `a`, or a source-faithful compact-normal spectral limit of Suzuki (1.12) without circularly assuming the sign.

**Next verified challenge:** at and past `a=(log2)/2`, derive a stronger two-boundary **positive OU versus signed prime-shift** inequality than the global L2-Schur envelope. MATRYOSHKA can certify the decomposed left/right boundary modes, but must preserve their coupling and its `H^{log}` energy debt. A candidate improvement should be tested against chiral endpoint tents and high-frequency localized waves before declaring positivity. Build full-operator form intervals on a dense mathematical core with rigorously bounded *negative* errors, not source-blind positive finite matrices. An all-`a` theorem (equivalent to RH) remains **UNVERIFIED**.

## Reproduce, exact arithmetic, and literature

- `python -m unittest tests.test_suzuki_prime_boundary -v`
- `python -m unittest tests.test_suzuki_arch_intervals -v`
- `python -m unittest tests.test_suzuki_bath_factor -v`
- `python scripts/suzuki_wavefront_probe.py --output /tmp/suzuki-wavefront.json`
- The research snapshot `research/2026-10-13/SUZUKI_WAVEFRONT_RECEIPT.json` is a deterministic **mathematical** receipt, not a physical-source signature.

The local *isolated* implementation passed **23 new tests**. The exact parent SUCC branch integrated CI is separately validated; remote CI for this child head must complete before claiming integrated success. The first-prime and Gamma formulae derive from Suzuki's primary arXiv paper; the OU Fourier transform, Schur test, Leibniz differentiation, Poincare/Plancherel are classical. **No theorem or numerical receipt here proves RH.**

## SW-10. Independent source-form numerical scouting through the **original** Weil functional (TESTED MODEL, not a proof)

To distinguish a genuine completed-source operator from an arbitrary positive OU background, `scripts/suzuki_weil_sine_scout.py` independently evaluates Suzuki's Weil functional *before* rewriting it with the screw kernel. For `a>0`, `j>=1`, the legal Dirichlet test is
\[
v_j(x)=\sin\left(\frac{j\pi(x+a)}{2a}\right)\mathbf 1_{[-a,a]}(x),\quad
C_j(t)=\int v_j(x+t)v_j(x)dx=\frac12\left[(2a-t)\cos(k_jt)+\frac{\sin(k_jt)}{k_j}\right],\quad k_j=\frac{j\pi}{2a}
\]
for `0<=t<=2a`, with `C_j(0)=a`. The exact original Weil expression simplifies to
\[
\begin{aligned}
Q_W(v_j)=&\;4\int_0^{2a}C_j(t)\cosh(t/2)dt
-2\sum_{p^k\le e^{2a}}\frac{\log p}{p^{k/2}}C_j(k\log p)
-(\log4\pi+\gamma)a\\
&-\int_0^{2a}\frac{C_j(t)e^{t/2}-a}{\sinh t}dt
+2a\,\operatorname{artanh}(e^{-2a}).
\end{aligned}
\tag{SW-10}
\]
The last term is the **exact missing infinite tail** of the Archimedean functional beyond support `2a`; dropping it would be a source-identity error. Formula SW-10 follows directly by inserting the autocorrelation in Suzuki's displayed definition of `W`, splitting its integral at `2a`, and evaluating `int_(2a)^inf dt/(e^t-e^-t)=artanh(e^-2a)`.

A standalone *uncertified* deterministic floating-point Simpson routine gives the following **minimum Rayleigh quotients among tested `j in {1,2,3,4,6}`** (not the true bottom eigenvalue):

| `a` | Smallest tested `Q_W(v_j)/||v_j||²` | Active arithmetic jets |
|---|---:|---|
| `1/12` | `0.67209` | None |
| `1/4` | `0.04984` | None |
| `log2/2` | `0.00266` | None (boundary measure zero) |
| `3 log2/5` | `0.00859` | `2` |
| `0.45` | `0.00515` | `2` |
| `0.50` | `0.00322` | `2` |

**Scope:** These small positive values make the first-wavefront **spectral proof numerically delicate**; they do not establish positivity on an untested subspace. The scout recomputes true prime-power coefficients, includes full pole/Gamma infinite-tail terms, and has no zero inputs. It is an **independent formula route** from the `g`-kernel analysis but shares Suzuki's original arithmetic source. An independent scipy Gaussian quadrature run agreed with the stdlib Simpson diagnostic to better than `4e-14` for the displayed finite trials; neither supplies certified quadrature error. The JSON receipt is `research/2026-10-13/SUZUKI_NUMERICAL_SINE_SCOUT.json` and carries explicit `qualified=false` and `RH_proved=false` fields.

**Verdict:** A generic coarse lower bound does not prove positivity near the real first-prime threshold. Next build rigorously interval-enclosed **trial-family quadratic values and full complementary spectral tails**, not simply larger floating-point matrices; a finite sampled positive Rayleigh test is always only an upper bound on the actual lowest eigenvalue.
