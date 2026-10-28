# Operation BBP Ground Floor: Two Quadratic SUCC Atoms, Eight-Step Holonomy, and a Finite Radial Zero

**Date:** October 26, 2026. **Status:** classical BBP derivation plus a source-typed SUCC organization and exact finite certificates; no independent academic-priority claim. **Requested problem:** explain whether the apparently composite BBP step 8 is primitive, and construct either lower-level atomic dynamics or a global analytic shape whose finite approximations exhibit a controlled defect. **Both constructions are available below.**

**Standing firewall:** The source is exactly the authenticated four-pole BBP forcing, `U_0=0`, `U_(n+1)=16 U_n+r(n+1)`. No original source is edited. Nothing here proves π base-16 normality, selected Fourier cancellation or RH. The signed *linear* cancellation of an integral is a different problem from cancellation of `exp(2πi h U_n)`.

## 1. The global source and its two genuine quadratic poles

The classical BBP formula, with source time `n=k+1`, is

$$
\pi=\sum_{k\ge0}\frac1{16^k}\left(\frac4{8k+1}-\frac2{8k+4}-\frac1{8k+5}-\frac1{8k+6}\right)
=\int_0^1\frac{P(t)}{1-t^8/16}\,dt,
$$

$$P(t)=4-2t^3-t^4-t^5=(1-t)(t^2+2)(t^2+2t+2).$$

Now factor the denominator **over Q[t]**:

$$
1-\frac{t^8}{16}
=\underbrace{(1-t^2/2)(1-t+t^2/2)}_{D_{\min}(t)}
\underbrace{(1+t^2/2)(1+t+t^2/2)}_{D_{\mathrm{cancel}}(t)}.
$$

The numerator is exactly `4(1-t) D_cancel(t)`, so two entire quadratic factors cancel, leaving

$$
\boxed{
K(t)=\frac{P(t)}{1-t^8/16}
=\frac{4(1-t)}{(1-t^2/2)(1-t+t^2/2)}
=\frac{16(1-t)}{(2-t^2)[(t-1)^2+1]}.
}
$$

**Terminology warning.** The original four denominators `8k+1,8k+4,8k+5,8k+6` are *Mellin moment labels*, not four poles of this rational function. The octic rational denominator originally has 8 roots (on the circle `|t|=√2`); four roots are canceled by the numerator and four survive: `±√2` (real) and `1±i` (complex). Thus the reduced rational transfer has precisely two irreducible quadratic denominator factors over Q.

This integral simplification is classical; compare Adamchik–Wagon, *A Simple Formula for π* (American Mathematical Monthly 1997), https://doi.org/10.1080/00029890.1997.11990729, and Barsky–Muñoz–Pérez-Marco, *On the genesis of BBP formulas* (Acta Arithmetica 2021), https://doi.org/10.4064/aa200619-28-9. The claim here is not scholarly discovery of that identity; it is a fully certified, source-preserving factorization aligned to SUCC's observational apparatus.

### Conditional rigidity within the chosen two-atom construction

If one fixes the octic scalar return `1-t^8/16`, requires cancellation of `D_cancel`, and additionally requires a **simple source endpoint zero at t=1**, any nonzero polynomial numerator of minimal degree is a scalar multiple of `(1-t)D_cancel`. The degree is 5. Requiring the constant coefficient to be 4 fixes that multiple and recovers precisely `P(t)=4-2t³-t⁴-t⁵`. Thus the four BBP weights are *forced within this specifically declared atomic cancellation/normalization class*. They are not asserted unique among all possible BBP formulas for π.

## 2. The two 2×2 atomic successor systems

On a rational two-dimensional carrier define

$$
G=\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix},\qquad
H=\begin{pmatrix}0&1\\1/2&0\end{pmatrix}.
$$

Their transfer determinants are precisely the two uncanceled factors:

$$\det(I-tG)=1-t+t^2/2,\qquad\det(I-tH)=1-t^2/2.$$

They are distinct dynamics, not interchangeable 2×2 labels. `G` is multiplication by the Gaussian-rational number `z=(1+i)/2=1/(1-i)`; it contracts Euclidean lengths by `1/√2` and rotates by 45°. `H` is a two-way *split* real quadratic transfer with eigenvalues `±1/√2`. Both are rational matrices.

Their powers give an exact, nontrivial source-coherence square:

| Step | Real atom H | Rotating atom G |
|---|---|---|
| 2 | `I/2` | quarter-turn `/2` |
| 4 | `I/4` | `-I/4` |
| 8 | `I/16` | `I/16` |

Hence **8 is the smallest shared positive scalar-return clock**, though neither atom needs eight-dimensional state. The half-clock 4 retains the essential relative minus sign: a chiral/sign defect which disappears at the common eighth return. In Gaussian arithmetic `z^4=-1/4`, `z^8=1/16`. No golden-ratio hypothesis is involved in this eightfold return.

The rational transfer is

$$\boxed{K(t)=\frac{4(1-t)}{\det(I-tH)\det(I-tG)}.}$$

Its **reduced denominator has degree 4**, and numerator `4(1-t)` is coprime to it since the denominator is nonzero at `t=1`. Thus among ordinary rational linear time-invariant state-space realizations over Q, **four scalar states are minimal** (McMillan-degree theorem); the displayed pair of 2×2 atoms attains that size. The pair's common eighth power is an observable equality of endpoints, not equality of the intermediate source histories.

## 3. A fourth-order SUCC recurrence with the four-pole pattern as its eightfold impulse

The reduced denominator expands surprisingly simply:

$$D_{\min}(t)=1-t+\frac12t^3-\frac14t^4.$$

Write `K(t)=Σ_{m≥0}c_m t^m`. Then `D_min K=4(1-t)` and the exact coefficient recurrence is

$$
\boxed{c_m=c_{m-1}-\tfrac12c_{m-3}+\tfrac14c_{m-4}
+4\mathbf1_{\{m=0\}}-4\mathbf1_{\{m=1\}},}
$$

with `c_m=0` at negative indices. The first eight coefficients are

$$\boxed{(c_0,\dots,c_7)=(4,0,0,-2,-1,-1,0,0).}$$

Because `K=P/(1-t^8/16)` with `deg P<8`, the entire infinite sequence obeys the *strong return law*

$$\boxed{c_{8k+r}=16^{-k}c_r\quad(0\le r<8).}$$

Integration of the impulse response gives

$$\pi=\sum_{m\ge0}\frac{c_m}{m+1}
=\sum_{k\ge0}\frac1{16^k}\left(\frac4{8k+1}-\frac2{8k+4}-\frac1{8k+5}-\frac1{8k+6}\right).$$

So the famous four Mellin denominators and sparse signed coefficients arise from a **fourth-order rational linear filter driven by two quadratic 2-state atoms**. The number 8 is an emergent synchronization/holonomy period, not a required primitive system dimension.

### An intermediate signed/unsigned radix-4 factorization

Even the eight-step shell itself splits into two four-step streams:

$$
\boxed{
K(t)=\frac{4+2t-t^3}{1+t^4/4}
-\frac{2t+t^3}{1-t^4/4}.
}
$$

The first is a **signed** base `-4` geometric return and the second an **unsigned** base `+4` return. For each $j$, the pair of stages $k=2j$ and $k=2j+1$ reproduces the single original base-16 BBP block `j` exactly. This is a useful finite staging correspondence, not a new proof of anything about digit frequencies.

## 4. The integrand is literally an exact logarithmic zero + surviving angular transport

Define

$$ A(t)=(1-t)^2+1,\qquad
F(t)=\frac{2-t^2}{A(t)}. $$

For `0≤t≤1`, `F(0)=F(1)=1` and

$$F(t)-1=\frac{2t(1-t)}{A(t)}>0\quad(0<t<1).$$

Exact partial fractions give

$$
\boxed{K(t)dt=2\,d\log F(t)+4\,d\arctan(t-1).}
$$

The **logarithmic** channel carries nontrivial positive interior information but zero endpoint period:

$$2\int_0^1d\log F=2\log\frac{F(1)}{F(0)}=0.$$

The complex/angular channel carries `4[atan(0)-atan(-1)]=π`. Equivalently put `w(t)=1-t+i`, whose argument increases by `π/4`, and observe `w(1)/w(0)=i/(1+i)=(1+i)/2=z` and `z^8=1/16`.

**This matches the user's “Seinfeld zero” framing literally:** the complete radial observable evaluates to zero while its internal source-labelled path is nonzero. The angular observable is the surviving cycle/angle. It does not yet imply cancellation of the much harder nonlinear, time-indexed characters `e(hU_n)`.

### An exact null BBP formula and a separate angular BBP formula

Both channels can be expanded using **the same** octic denominator. The eight-shell polynomials are

$$
P_{\rm ang}(t)=2+2t+t^2-\frac12t^4-\frac12t^5-\frac14t^6,
$$

$$
P_{\rm rad}(t)=2-2t-t^2-2t^3-\frac12t^4-\frac12t^5+\frac14t^6.
$$

They satisfy `P=P_ang+P_rad`,

$$\frac{P_{\rm ang}}{1-t^8/16}=\frac4{A(t)},\qquad
\frac{P_{\rm rad}}{1-t^8/16}=2(\log F(t))'.$$

Integrating yields a **nontrivial convergent null BBP identity** with the seven signed taps of `P_rad`, and a separate base-16 BBP formula for π with the seven taps of `P_ang`. The classical literature on BBP null formulas is directly relevant; see Barsky–Muñoz–Pérez-Marco (2021) cited above. We claim no priority for this null identity.

The original sparse four taps result when the seven-tap angular and seven-tap radial streams add: four moment channels survive; their other taps cancel. This explains the four-pole vector as an **interference pattern** of lower-level source channels, in the strictly linear integral sense.

## 5. The exact finite virtual-world defect and rational radial completion

Define the finite original BBP prefix

$$P_N=\sum_{k=0}^{N-1}16^{-k}r(k+1).$$

For each time stage take the weight `w_k(t)=t^(8k)(1-t^8/16)`. Then

$$\sum_{k=0}^{N-1}16^{-k}w_k(t)=1-(t^8/16)^N,$$

and in the infinite limit the weights form a pointwise **partition of unity**. The logarithmic source cancellation happens only after the full source-complete sum (or its explicit residual) is accounted for.

Set

$$
\begin{aligned}
\mathcal A_N&=4\int_0^1 \frac{(t^8/16)^N}{A(t)}dt,\\
\mathcal R_N&=2\int_0^1 \frac{d}{dt}(t^8/16)^N\log F(t)\,dt.
\end{aligned}
$$

Then for every positive integer $N$,

$$\boxed{\pi-P_N=\mathcal A_N-\mathcal R_N>0.}$$

Both terms are positive and are individually of order `16^(-N)/N`, but their difference is of order `16^(-N)/N²`. The missing angular mode and the uncompleted logarithmic zero **cancel to one extra asymptotic order**.

A surprising exact arithmetic consequence: `R_N` is **rational** for every integer `N`. Indeed, because `(1±i)^8=16`, the polynomial

$$J_N(t)=\frac{t^{8N}-16^N}{(t-1)^2+1}\in\mathbb Z[t]$$

has integer coefficients, and we can calculate the log-channel partial sum without numerical logs:

$$\boxed{\mathcal R_N=P_N+\frac4{16^N}\int_0^1J_N(t)dt\in\mathbb Q.}$$

For example: `R_1=2/105`, `R_2=67/90090`, `R_3=1443053/42833831040`. Its positivity is separately proved by `log F(t)>0` on `(0,1)`. The finite rational result is *not* a contradiction to the logarithmic primitive; it comes from completing the Gaussian eighth return and its endpoint normalization.

## 6. A certified finite BBP truncation defect from the same primitive geometry

The precise original unwrapped state is `U_N=16^(N-1) P_N`. The authentic future Green correction is `T_N=16^(N-1)(π-P_N)` and has the independent **positive** integral

$$\boxed{T_N=\int_0^1\frac{t^{8N}(1-t)}{(2-t^2)A(t)}dt.}$$

Put `m=8N`. Since `D(t)=(2-t²)A(t)>=1` on `[0,1]`, and

$$0\le1-\frac1{D(t)}\le3(1-t)$$

(the last follows from `D(t)-1=(1-t)(t³-t²-t+3)≤3(1-t)`), the authentic Green correction has a *fully rational finite enclosure*:

$$\boxed{
\frac1{(m+1)(m+2)}-\frac6{(m+1)(m+2)(m+3)}
\le T_N\le \frac1{(m+1)(m+2)}.
}$$

Hence

$$T_N\sim\frac1{64N^2},\qquad
\pi-P_N\sim\frac{16^{-N}}{4N^2}.$$

The signed angular and radial *separately* have leading asymptotics

$$\mathcal A_N\sim\mathcal R_N\sim \frac{16^{-N}}{2N},$$

so their difference loses a whole leading order—an exact, nontrivial **cancellation of the finite source's linear analytic boundary channels**. This cancellation does not imply the nonlinear Weyl cancellation necessary for base-16 normality.

## 7. The Gamma(2) shape and the genuine Euler/logarithmic interface

The reference positive Beta carrier `B_N(dt)` has normalized density proportional to `t^(8N)(1-t)dt`. If `Y_N=8N(1-t)`, the distribution tends to `Gamma(shape=2, rate=1)` with density `y exp(-y)dy`. The true Green-tail carrier differs by the smooth source weight `g(t)=1/D(t)`, which tends to 1 at the endpoint. In fact, if `δ_N=6/(8N+3)`, then

$$\|\operatorname{Law}_{\rm Green}(t)-\operatorname{Law}_{\rm Beta}(t)\|_{\rm TV}\le\frac{\delta_N}{1-\delta_N}=\frac6{8N-3},$$

so the source-conditioned law shares the same Gamma(2) limit with an explicit bounded-observable error.

The reference finite logarithmic readout is **exactly**

$$\boxed{\mathbb E_{B_N}[\log(8N(1-t))]=\log(8N)+1-H_{8N+2}\longrightarrow1-\gamma.}$$

This is the same additive-vs-logarithmic Gamma successor described in the Oily Macaroni #307 research. Crucially **γ is not inserted as a finite fit**; it emerges from harmonic SUCC and the rescaled endpoint Gamma law. The golden `φ^-1` remains a separately declared Laplace fixed-point reference, not a consequence of the two quadratic BBP matrices. A theorem selecting the golden comparison for the original source is still owed.

## 8. Hostile source mutant: equal 8-clock and equal first endpoint jet do not select π

Even this apparently complete ground-floor geometry has a source-selection obstruction. Define for every rational `ε>0`

$$P_\varepsilon(t)=P(t)+\varepsilon(1-t)^2D_{\rm cancel}(t).$$

Then `P_eps` is positive on `(0,1)`, retains the **same** octic return `1-t⁸/16`, canceled factors, simple endpoint zero, and exactly the same first endpoint derivative `P_eps'(1)=-15`. It also retains the leading `n^-2` source asymptotic. Yet

$$\int_0^1\frac{P_\varepsilon(t)}{1-t^8/16}dt
=\pi+\varepsilon\int_0^1\frac{(1-t)^2}{D_{\min}(t)}dt>\pi.$$

Thus a common eighth return, a two-atom carrier, positivity and leading endpoint jets **do not uniquely authenticate the original BBP π source**. The complete angular/boundary normalization and exact polynomial coefficients remain load-bearing. No nonnormality of the mutant is claimed.

## 9. Falsifiable π-normality follow-up, not a theorem yet

The above reduces BBP's analytic scalar source to a 4-state rational filter and gives a complete **finite error** construction. It provides no bound on

$$S_N(h)=\sum_{n=1}^N e(hU_n),\qquad h\ne0,$$

because passage from linear source moments to nonlinear selected rational-circle phases does not preserve the angular/radial cancellation automatically. In particular the null BBP channel is zero after source completion, but its finite prefixes are rational **and nonzero**. Applying complex characters before and after completion is an unproved and generally noncommuting operation.

**Next research targets:** (a) integrate the primitive `G/H` histories and their relative `-` four-step seam with SUCC's `seinfeld_phase`, `succ_internal_matrix_walk` and `prime_clock_yoneda`; (b) compute signed cross-channel coherence at finite true `U_n`, not merely complete scalar π; (c) prove a source-specific error/transport theorem showing how the rational logarithmic null prefix affects actual future integer carries; (d) test against #304 coherent-seed and positive-carry counterfeit families; and (e) compare the new two-atom signed channels to Oily Macaroni #307's Gamma/Mellin positive-field representation without assuming a golden selector. If no saving survives these tests, preserve the exact obstruction.

### Implementation, tests and authority

- `observational_succ/bbp_quadratic_atoms.py`: pure integer/Fraction polynomial identities, exact 2×2 transfers and powers, exact impulse recurrence, signed-base4 clock, finite null-channel rationals, source mutants, certified Green-tail enclosures.
- `tests/test_bbp_quadratic_atoms.py`: 15 local exact/adversarial test groups with optional mpmath holdouts; suite independently validated in isolated research staging, **not** preclaimed as a successful full 8,742-test repository suite.
- No changes to original `authentic_r`, historical source manifests, RH theorem files or committed baselines. No Lean certificate for these new statements; the identities are paper-proved/classical with exact finite software replay.

**Status: π normality OPEN; RH OPEN; academic novelty unverified.**
