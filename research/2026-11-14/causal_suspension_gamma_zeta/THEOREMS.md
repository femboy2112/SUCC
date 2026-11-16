# Principia Observatoris — Positive causal volume, negative integers, Gamma suspension, and zeta's trivial zeros

**Date:** 2026-11-14. **Scope:** Additive research continuation of SUCC draft PR #636 at `397eec34c3637c876ab4e4f71f7c9a5359f75535`, informed by SUCC Orbit Clock Genesis PR #165. **No main, source, historical theorem or frozen BBP change.** π base-16 normality, completed Weil positivity and RH remain OPEN. The constructions below are classical in their mathematical ingredients; their source-typed combination is new-to-SUCC, not a claim of academic priority.

## Thesis, with source-type firewall

The author's geometry asks whether a **continuous, source-covariant causal volume** can connect a zero-pointed SUCC successor's positive finite clocks to *negative* arithmetic coordinates. **Yes, within an explicit suspension of those clocks.** That suspension is extra structure, not forced by compactness. A *second* forward-only method, Euler–Hasse finite differences, constructs actual `ζ(-m)` from positive integers and makes every `ζ(-2m)` vanish by signed parity. Gamma convolution carries the suspension wave, and analytically negative Gamma-depth becomes a signed distribution at the origin. A third, entirely authentic zeta reflection supplies the reciprocal-Gamma zero. There is a precise normalization contact between the BBP `k+2` Gamma-face tower and zeta's trivial-zero *derivative*, but the contact **does not** construct the missing arithmetic BBP→zeta source intertwiner.

Declare four incompatible yet interoperable types: finite clock source, continuous suspension flow, positive Gamma observer averaging, analytically continued signed distribution / completed zeta. A clock quotient, a gauge change, a physical intervention, and a completed analytic value are not silently the same arrow.

## PSV-01 — Finite source clocks construct negative residues by forward counting (CLASSICAL / PROVED)

Take the existing SUCC minimal synchronized clock tower
\[
L_N=\operatorname{lcm}(1,\ldots,N),\qquad C_N=\mathbb Z/L_N\mathbb Z,\qquad L_N\mid L_{N+1}.
\]
Every cyclic state has a positive forward successor `a↦a+1`. Its formal inverse on `C_N` is already the **positive** iterate `S^{L_N-1}`; no primitive backward operation is needed. For each *requested* positive integer `m`, the compatible tuple
\[
\boxed{a_N(m)=(L_N-m)\bmod L_N=-m\bmod L_N}
\]
represents the ordinary negative integer `−m` in `\widehat{\mathbb Z}=\varprojlim_N C_N`. Bonding holds because integer reduction commutes with the divisibility maps. If `m<L_N`, `L_N−m` is an explicitly **nonnegative forward clock index**; it is not an ordinary positive integer limit in `\mathbb R`.

**Honest source caveat:** specifying the target `−m` in the theorem is not the same as secretly supplying a negative *starting state*; the root is always `0`. Merely choosing its finite-clock representative does not construct a continuous path across the totally disconnected profinite space. The original integers embed densely, not surjectively, into the profinite completion.

## PSV-02 — The causal volume is the forward odometer suspension (CLASSICAL / PROVED)

Introduce one additional **continuous causal phase** `u∈[0,1]` per profinite clock state. Form the mapping torus
\[
\boxed{\mathscr S=(\widehat{\mathbb Z}\times[0,1])/
\bigl((a,1)\sim(a-1,0)\bigr).}\tag{S1}
\]
This is equivalently `(\mathbb R×\widehat{\mathbb Z})/\Delta\mathbb Z`, with `(t,a)∼(t+n,a+n)`. On each finite clock layer it is a circle `\mathscr S_N=\mathbb R/L_N\mathbb Z`, with compatible projection
\[
\pi_N([a,u])=(a-u)\bmod L_N.
\]
The seam is lawful because `a−1` and `a−1` agree at its two endpoints. The finite circles' quotient maps commute with all prior SUCC reduction maps; the inverse-limit volume is compact and connected. See the classical odometer/solenoid suspension literature in the provenance section.

Define the **forward-only flow** `\Phi_t([a,u])=[a,u+t]` for `t≥0`, interpreted in the quotient; this descends to `\pi_N\Phi_t=\pi_N−t\pmod{L_N}`. Starting at `o=[0,0]`, for any integer `m≥1`,
\[
\boxed{\Phi_m(o)=[0,m]=[-m,0],\quad\pi_N\Phi_m(o)=-m\bmod L_N.}\tag{S2}
\]
This is an **actual continuous path** through the volume from the origin to the profinite negative integer, using only positive elapsed time and the forward compatible seam. The sign is an orientation convention; reversing the seam reverses the label of the endpoint. Negative arithmetic has not been generated ex nihilo without extra structure: the finite cyclic successor supplies invertibility, and the suspension supplies the continuous bridge.

### The precise non-path-connected boundary

`\widehat{\mathbb Z}` alone is compact **and totally disconnected**, so has no nonconstant continuous path. The suspension is connected but **not path connected**. One path component is the image of the real line `t↦[0,t]`, whose intersection with the profinite transverse section is exactly the embedded ordinary integers `\mathbb Z`. Proof: any interval path lifts locally through the diagonal discrete quotient to `\mathbb R×\widehat{\mathbb Z}`. Its profinite coordinate is constant by connectedness of the interval and total disconnectedness of the profinite factor. To land in the transverse section at `(0,a)` from `(0,0)` the elapsed real coordinate must be an integer, and then `a∈\mathbb Z`.

Every **forward** leaf is dense because its projection onto each finite `\mathscr S_N` visits every circle point infinitely often. Therefore every nonintegral profinite target can be approximated arbitrarily closely at finite clock levels by positive forward time, but it is **not** exactly reached by any finite continuous path from the origin. This is a rigorous *finite-compatible versus analytic-global* distinction. Compactness without the suspension never implies a path.

**Explicit phantom control.** In the full profinite completion choose the CRT point with 2-adic component `1` and every odd-prime component `0`. At each finite synchronized clock, CRT supplies one **nonnegative** integer representative with the correct residues, and these representatives bond coherently. Yet no ordinary integer realizes the full thread: divisibility by every power of `3` forces such an integer to be `0`, contradicting its odd 2-adic residue. So the phantom is a genuine point of the compact suspension transversal, approximated at every finite stage, but never reached by any finite path from zero. Our exact `noninteger_crt_thread()` checks its first 18 levels. This is SUCC's preexisting phantom-source phenomenon in a new **path-lifting** interface, not proof that the physically available instruments cover the entire completion.


## PSV-03 — Gamma turns the continuous forward path into a coherent causal volume (CLASSICAL / PROVED)

For any continuous bounded observable `f` on the compact suspension, define the rate-one **Gamma-averaged forward flow**
\[
\boxed{(\mathcal G_\alpha f)(x)
=\frac1{\Gamma(\alpha)}\int_0^\infty t^{\alpha-1}e^{-t}
 f(\Phi_t x)\,dt,\quad\alpha>0;
\qquad\mathcal G_0=I.}\tag{G1}
\]
This is a positive, unital Markov operator on continuous functions. Gamma convolution, via the beta integral, proves the exact observer-depth semigroup
\[
\boxed{\mathcal G_\alpha\mathcal G_\beta=\mathcal G_{\alpha+\beta}.}\tag{G2}
\]
As `α↓0` the Gamma law converges weakly to a point mass at zero, so `\mathcal G_0=I` is continuous on each continuous observable. This is an **observer averaging**, not the source's deterministic forward successor, and not a physical stochastic law authenticated by the arithmetic source.

Finite-layer clock harmonics `\chi_{N,h}([a,u])=e^{2\pi i h(a-u)/L_N}` obey
\[
\boxed{\mathcal G_{\alpha,\lambda}\chi_{N,h}
=\left(1+\frac{2\pi i h}{\lambda L_N}\right)^{-\alpha}\chi_{N,h}.}\tag{G3}
\]
Here `\lambda` is the Gamma rate, equal to one in (G1). This is the exact log-Gamma Laplace/Fourier transform on the **same forward causal suspension**. Its finite clocks form a genuine compatible diagram: for `L_N|L_{N+1}`, the harmonics satisfy `\chi_{N+1,h}^{L_{N+1}/L_N}=\chi_{N,h}` when **both** functions are evaluated at the same orbit coordinate (not simple equality without exponent). All `\mathcal G` operators commute with projection/pullback of actual finite-clock observables.

### An explicit Gamma volume collapsing onto a negative endpoint

Let `T_{m,k}` be the sum of `mk` independent `Exp(k)` waiting times (`m,k` **positive integers**). Then
\[
\mathbb ET_{m,k}=m,\qquad\operatorname{Var}(T_{m,k})=m/k.
\]
Therefore `T_{m,k}→m` in probability as `k→∞`. For every uniformly `L`-Lipschitz observable along the forward orbit,
\[
\boxed{\left|\mathbb E f(\Phi_{T_{m,k}}o)-f(\Phi_m o)\right|^2
\le L^2m/k.}\tag{G4}
\]
If `t↦f(\Phi_t o)` has second derivative bounded by `M`, its error is at most `M m/(2k)`. Thus a growing **positive causal Gamma volume** approximates the exact endpoint `[-m,0]` with a quantified observer cost. At each finite clock, the **exact** character is
\[
\mathbb E\chi_{N,h}(\Phi_{T_{m,k}}o)
=\left(1+\frac{2\pi i h}{kL_N}\right)^{-mk}
\xrightarrow[k\to\infty]{}e^{-2\pi i hm/L_N}.
\tag{G5}
\]
All finite input waits are forward, positive and independent **by the declared model**; deterministic `\Phi_m` already reaches the integer target, while Gamma supplies coherent volume transport and its analytic interpolation. An unspecified physical carrier is not proved to generate exponential clocks.

## PSV-04 — Negative Gamma stages produce distributions, not backwards probabilities (CLASSICAL / PROVED)

The continuous rate-one Gamma family has Laplace symbol `\mathcal L g_\alpha(p)=(1+p)^{-\alpha}` for real `p≥0`. Analytically extending the **convolution algebra of causal distributions** to negative integer stage count gives
\[
\boxed{g_{-m}=(1+\partial_t)^m\delta_0
=\sum_{j=0}^m\binom mj\delta_0^{(j)},
\quad\mathcal Lg_{-m}(p)=(1+p)^m.}\tag{G6}
\]
This is the exact convolution inverse `g_m*g_{-m}=\delta_0`, as distributions supported on the nonnegative half-line. The analytic extension changes **type**: `g_{-m}` is a signed generalized function, not a probability distribution or a state travelling into physical negative time. A probability on `[0,∞)` must have `\mathbb E e^{-pT}≤1` for `p>0`, whereas `(1+p)^m>1`, proving the impossible probabilistic interpretation. At `m=0`, the distribution is the original `δ_0`.

**Critical cancellation distinction:** The normalized distribution family `t_+^{\alpha-1}e^{-t}/Γ(α)` survives at negative integral `α` as a nonzero distribution because the singular distribution numerator cancels the reciprocal-Gamma zero. Conversely `1/Γ(s/2)` as a scalar **does** vanish at `s=-2m`. One may not identify those two completions.

## PSV-05 — Entire negative zeta values from finite positive Pascal/SUCC faces (CLASSICAL; imported Euler–Hasse/Sondow)

For `m,n≥0`, define the finite signed Pascal face from **positive inputs only**
\[
D_{n,m}=\sum_{j=0}^n(-1)^j\binom nj(j+1)^m,
\qquad A_m=\sum_{n=0}^{m}2^{-n-1}D_{n,m}.
\tag{Z1}
\]
Finite difference degree annihilation gives `D_{n,m}=0` whenever `n>m`, so **every negative integer value requires finitely many positive source coordinates.** The classical Euler transformation/Hasse–Sondow continuation of the alternating zeta gives
\[
\boxed{A_m=\eta(-m),\qquad\zeta(-m)=\frac{A_m}{1-2^{m+1}}.}\tag{Z2}
\]
The identification with `\zeta` requires the imported analytic continuation of the **authentic zeta source**, rather than summing the divergent `1^m+2^m+\cdots` by fiat. This is exactly the route proved in Jonathan Sondow, *Analytic continuation of Riemann's zeta function and values at negative integers via Euler's transformation of series*, Proc. AMS 120 (1994), 421–424, DOI 10.1090/S0002-9939-1994-1172954-7.

A completely formal positive-SUCC proof of the **parity cancellation** now follows. Write the exponential generating function
\[
E(z)=\sum_{m\ge0}A_m\frac{z^m}{m!}.
\]
Since `D_{n,m}=0` for `n>m`, the finite differences may be rearranged coefficientwise as formal power series:
\[
E(z)=\sum_{n\ge0}2^{-n-1}e^z(1-e^z)^n
=\boxed{\frac{e^z}{1+e^z}.}\tag{Z3}
\]
Thus `E(z)+E(-z)=1`, so `E(z)-1/2` is odd and **every positive even coefficient vanishes**:
\[
\boxed{A_{2m}=0\quad\Longrightarrow\quad \zeta(-2m)=0,\quad m\ge1.}\tag{Z4}
\]
Unlike an infinite observational guess, this finite rule proves the **entire family** in the declared authentic analytic continuation. It is a recovery of the known trivial zeros, not a statement about RH's nontrivial zeros.

The independent exact recurrence from `(1+e^z)E=e^z` is
\[
2A_m=1-\sum_{j=1}^m\binom mj A_{m-j},\quad A_0=1/2.
\tag{Z5}
\]
This gives a finite SUCC-generated decision program for each requested negative integer value. Checks: `ζ(0)=-1/2`, `ζ(-1)=-1/12`, `ζ(-2)=0`, `ζ(-3)=1/120`, `ζ(-4)=0`, `ζ(-5)=-1/252`. A raw divergent power sum is **not** assigned a value by numerical extrapolation.

## PSV-06 — Independent Gamma reflection: trivial zeros are normalization zeros (CLASSICAL)

Use the **actual** theta/Mellin completed zeta
\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad\xi(s)=\xi(1-s),
\]
with its known entire continuation. Fix `m≥1`; the positive endpoint `s_+=2m+1>1` has `ξ(s_+)>0` by the Euler product and Gamma positivity. Reflection gives
\[
\boxed{\xi(-2m)=\xi(2m+1)>0.}\tag{R1}
\]
But `1/Γ(s/2)` has a **simple** zero at `s=-2m`. Solving the completed identity for `ζ(s)` therefore gives the *exact simple trivial zero* and its nonzero derivative:
\[
\boxed{\zeta'(-2m)=(-1)^m\frac{(2m)!}{2(2\pi)^{2m}}\zeta(2m+1).}\tag{R2}
\]
The zeta zero appears at the inverse-Gamma **return from the completed analytic volume to the original uncompleted function**. This is a mathematically precise version of a sign/normalization defect at the negative boundary. It is **not** a theorem about traversing a physical wormhole or observing a causal signal from negative time. The analytic reflection is not a gauge redundancy to quotient away: it carries actual source-normalization data.

## PSV-07 — The precise BBP `k+2` ↔ trivial-zero slope bridge (NEW-TO-SUCC INDEX CONTACT; CLASSICAL CONTENT)

The authentic **positive** BBP source in draft PR #636 gives, for each fixed `k≥0`,
\[
B_k:=\lim_{N\to\infty}64N^{k+2}(-1)^k\Delta^kT_N=\Gamma(k+2).
\tag{B1}
\]
Here `T_N` is the true original zero-seeded Green tail, *not* an invented zeta sequence. At the odd face `k=2m-1`, the coefficient is exactly
\[
B_{2m-1}=\Gamma(2m+1)=(2m)!.
\]
Substituting the *same number* into the classical authentic zeta derivative formula yields a rigorous normalization identity:
\[
\boxed{\zeta'(-2m)=(-1)^m\frac{B_{2m-1}}{2(2\pi)^{2m}}\zeta(2m+1).}\tag{B2}
\]
**This is the mathematically legitimate form of the author's suspicion about the Gamma shift `k↦k+2`.** At BBP difference depth `2m−1`, its Gamma boundary normalization equals precisely the factorial appearing in the slope of the zeta trivial zero at `-2m`.

**Critical source-morphism debt:** This is an identity of positive **normalization constants** *after invoking the real zeta functional equation*. It does not show that BBP's source-generated moment, phase or carries map to the zeta Euler/theta source, nor that their signed quadratic forms agree. The step importing `ζ(2m+1)` and the zeta functional equation is not derived from BBP. The equality of `Γ(2m+1)` is not an intertwining law, and cannot prove π normality, RH, or any nontrivial zeta-zero statement.

## PSV-08 — Steelman, crucible, and next hostile probe

| Claim | Status | Boundary / adversary |
|---|---|---|
| Finite forward clocks represent negative integers | CLASSICAL / PROVED | A residue is not the ordinary real negative coordinate |
| A continuous forward curve connects to each negative clock integer in suspension | CLASSICAL / PROVED | Suspension is supplied; compactness alone is insufficient |
| Entire pro-finite transversal is reachable by one continuous path | REFUTED | Path component intersects transversal precisely in ordinary `Z` |
| Gamma forward averaging composes and concentrates on endpoint | CLASSICAL / PROVED | Extra independent exponential clock; not physical BBP sensor |
| Negative Gamma-stage is a positive future-time law | REFUTED | Laplace symbol `(1+p)^m>1` for `p>0` |
| Finite positive differences reproduce authentic negative zeta values | CLASSICAL / PROVED via Sondow | Requires authentic zeta analytic continuation; no raw divergent sum |
| `ζ(-2m)=0` all m≥1 | CLASSICAL / REPRODUCED | Trivial zeros; not RH |
| BBP Gamma face coefficient equals factorial in `ζ'(-2m)` | PROVED FORMAL COMPOSITION of imported identities | Equality of scalars is not authenticated BBP→Weil intertwiner |
| New all-mode BBP Weyl cancellation / universal Weil positivity | UNVERIFIED / OPEN | Needs genuinely signed source-selected bound, not merely Gamma kernels |

**Verdict-changing probe:** Declare one same-carrier source/operator map which takes the *full* BBP signed `Q(t)`, pointed `U_0=0`, origin clock, carries, and Mellin `Γ(k+2)` faces to the genuine theta/prime-power source without replacing Euler factors. Check an equality of **complex source-paired observables**, not just shared factorials, against wrong-radix, fake-composite six, null source, rational nonnormal and phase-inverted controls. A failure yields an explicit map/provenance obstruction; a success would justify revisiting a signed estimate. Retain independent future holdouts and all-global quantifiers.

## Provenance and primary sources

- SUCC [OCG #165](https://github.com/femboy2112/SUCC/pull/165): `L_N`, prime-power clock jets and `\widehat{\mathbb Z}` inverse-limit contraction.
- SUCC [#634](https://github.com/femboy2112/SUCC/pull/634) and [#636](https://github.com/femboy2112/SUCC/pull/636): genuine zero-seeded BBP, causal-volume Gamma sources and the `k+2` face limit.
- Jonathan Sondow (1994), *Analytic continuation of Riemann's zeta function and values at negative integers via Euler's transformation of series*, Proc. AMS **120**, 421–424, DOI [10.1090/S0002-9939-1994-1172954-7](https://doi.org/10.1090/S0002-9939-1994-1172954-7).
- NIST DLMF [§3.9 Euler transformation](https://dlmf.nist.gov/3.9), [§25.10 zeta zeros](https://dlmf.nist.gov/25.10), [§25.4 functional equation](https://dlmf.nist.gov/25.4), [§5.2 Gamma](https://dlmf.nist.gov/5.2).
- Nekrashevych, *Groups and Topological Dynamics*, Ch. 1, solenoid suspension/odometer (https://people.tamu.edu/~nekrash/teaching/19S/chapter1.pdf); Dranishnikov–Keesling, *Embedding of Higson compactification into the product of adelic solenoids* (adelic solenoid `(R×Zhat)/Z`).

**No academic-priority claim:** mapping tori, solenoids, Gamma subordination, Fourier/Laplace, finite differences, and the zeta functional equation are established mathematics. The user-motivated source-typed juxtaposition and exact tests are an architectural contribution to SUCC, not a discovery of previously unknown zeta zeros.
