# Constant circular windows: geometry, Fourier information, and source selection

**2026-11-07 — research-only appendix to HPB-01…HPB-05, draft PR #539.** Classical antecedents and elementary derivations; no novelty, physics, π-normality, RH, or formal-kernel priority asserted. This is an additional observation chart, not an alteration to the literal BBP source or zero seed.

## Hypothesis, clarification, and typed objects

**Author's insight:** Even as a trajectory approaches zero, the curvature/closure of a circle keeps a nonzero *local window of possible motions* around the point. An observed phase approaching a target is not the same as a collapse of the ambient space.

We must distinguish (i) **geometric capacity**, (ii) **actually accessible controls**, (iii) **fixed angular observation window**, and (iv) **the selected temporal orbit**. None implies the others without an explicit map.

Work with \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) and normalized Haar probability \(m(d\theta)=d\theta/(2\pi)\). A plane circle of fixed radius \(R\) has constant **extrinsic** curvature \(\kappa=1/R\); its 1D intrinsic Riemann curvature vanishes. Invariance of the window is a consequence of circle *rotations*, not an implication from a nonzero intrinsic curvature.

## HPB-C1 — a fixed window survives phase locking (PROVED MODEL)

For \(0<\delta<\pi\), let \(A_\delta(c)=\{\theta:\operatorname{dist}_{\mathbb T}(\theta,c)\le\delta\}\). For *every* center \(c\),

\[
\operatorname{length}(A_\delta(c))=2R\delta,\qquad
m(A_\delta(c))=\delta/\pi.
\]

The action \(c\mapsto c+a\) transports these arcs by an isometry, so even when \(c_n\to0\), neither their geometric length nor normalized volume shrinks.

If a controlled system is explicitly prescribed by
\[
\theta_{n+1}=F_n(\theta_n)+u_n\pmod{2\pi},
\qquad u_n\in[-\delta,\delta],
\]
and **every** such \(u_n\) is genuinely available, its one-step reachable set is precisely \(A_\delta(F_n(\theta_n))\), independent of state. This is a conditional *controllability* theorem, not an assertion about the uncontrolled π orbit. Countermodel: \(F(\theta)=16\theta\bmod2\pi\), \(\theta_0=0\), and \(u_n=0\) for all \(n\); the actual trajectory stays fixed at zero despite the unchanged circle.

**Repair of the earlier harmonic-budget interpretation:** HPB-01's optional latch may restrict *available actions* when a budget crosses zero. It never removes the geometric tangent direction or the circle itself. An actuation constraint is not a collapse of manifold dimension.

## HPB-C2 — fixed aperture as an exact Fourier observer (PROVED)

Let \(\nu_\delta\) be the probability measure with uniform angular density \(1/(2\delta)\) on the arc \([-\delta,\delta]\), periodized around the circle. For any circle probability measure \(\mu\), convolution \(\mu*\nu_\delta\) has density relative to \(m\)

\[
f_{\mu,\delta}(c)=\frac{\pi}{\delta}\mu(A_\delta(c))
\quad\text{(almost everywhere)}.
\]

Writing \(\widehat\mu(h)=\int e^{-ih\theta}\mu(d\theta)\), direct integration yields

\[
\widehat{\nu_\delta}(h)=
\begin{cases}1&h=0,\\
\frac{\sin(h\delta)}{h\delta}&h\ne0.
\end{cases}
\]

Thus Parseval gives an *always finite* nonnegative scalar measuring window occupancy:

\[
\boxed{
E_\delta(\mu):=\int|f_{\mu,\delta}-1|^2\,dm
=\sum_{h\ne0}|\widehat\mu(h)|^2
\left(\frac{\sin(h\delta)}{h\delta}\right)^2.
}
\]

Convergence holds since \(|\widehat\mu(h)|\le1\) and \(|\sin(h\delta)/(h\delta)|\le1/(|h|\delta)\). This is a measurement of **actual source occupancy**, not merely the geometric presence of an aperture.

**Injectivity/equidistribution theorem.** If \(\delta/\pi\notin\mathbb Q\), then all integer modes \(h\ne0\) have nonzero multipliers, so for *any* sequence of circle probability measures \(\mu_N\),

\[
\boxed{E_\delta(\mu_N)\to0
\quad\Longleftrightarrow\quad
\mu_N\Rightarrow m.}
\]

*Proof:* The forward direction bounds each \(|\widehat\mu_N(h)|\) by \(\sqrt{E_\delta(\mu_N)}/|\widehat{\nu_\delta}(h)|\), then applies Fourier polynomial density to obtain weak Haar convergence. The reverse uses weak convergence for each fixed \(h\), followed by dominated convergence over the summable bound \(1/(\delta^2h^2)\).

**Hostile rational-aperture control:** If \(\delta/\pi=p/q\) in lowest terms, the multiplier at \(h=q\) vanishes. The non-Haar law \(d\mu=(1+\epsilon\cos(q\theta))\,dm\), \(0<\epsilon\le1\), satisfies \(\mu*\nu_\delta=m\) *exactly*. Fixed width by itself does not guarantee information preservation.

## HPB-C3 — a golden window sees every Fourier mode quantitatively (PROVED)

Take a *fixed observation half-width*, not a multiplying dynamical carrier,

\[
\alpha=\varphi^{-1}=(\sqrt5-1)/2,\qquad \delta=\pi\alpha.
\]

Let \(\alpha'=(-1-\sqrt5)/2=-\varphi\). For each integer \(h\ne0\), choose the nearest integer \(k\) to \(h\alpha\). Its nonzero algebraic norm is

\[
(h\alpha-k)(h\alpha'-k)=k^2+hk-h^2
\in\mathbb Z\setminus\{0\}.
\]

Because \(|h\alpha'-k|\le(\sqrt5+\tfrac12)|h|\), we have

\[
\|h\alpha\|_{\mathbb R/\mathbb Z}
\ge\frac{1}{(\sqrt5+\tfrac12)|h|}.
\]

Using \(|\sin(\pi t)|\ge2\|t\|\), it follows for **every** nonzero integer \(h\) that

\[
\boxed{
\left|\frac{\sin(h\delta)}{h\delta}\right|
\ge\frac{2}{\delta(\sqrt5+\tfrac12)h^2}>0.
}
\]

Hence Parseval yields the quantitative, finite-data Fourier recovery bound

\[
\boxed{
|\widehat\mu(h)|
\le \frac{\delta(\sqrt5+\tfrac12)}2\,
h^2\sqrt{E_\delta(\mu)}.
}
\]

This is an exact polynomial conditioning guarantee from quadratic irrationality. It does **not** create a bound on \(E_\delta(\mu)\) from arithmetic dynamics. The same number \(\varphi\) plays distinct roles in the source-independent **observation aperture** here and the Pisot/Galois carrier in PR #537; they must not be conflated.

## HPB-C4 — persistent window and complete phase locking coexist (PROVED)

The Pisot trace \(\varphi^n+\psi^n\in\mathbb Z\), \(\psi=-\varphi^{-1}\), gives \(e(\varphi^n)=e(-\psi^n)\to1\). Its circle empirical measures \(\mu_N\Rightarrow\delta_0\), rather than Haar. For every \(0<\delta<\pi\), the smoothed measures tend to \(\nu_\delta\), and

\[
\boxed{
E_\delta(\delta_0)=\frac{\pi}{\delta}-1>0.
}
\]

*Proof:* The \(m\)-density of \(\delta_0*\nu_\delta\) is \((\pi/\delta)\mathbf1_{A_\delta(0)}\). Integrate its squared difference from 1.

With the golden aperture \(\delta=\pi/\varphi\), the exact locked-phase residual is
\[
E_{\pi/\varphi}(\delta_0)=\varphi-1=\varphi^{-1}.
\]
This memorable constant is **only** a geometric/convolution identity; it is not an authenticated digit-distribution result.

**Moving-frame countermodel:** Keep \(x_n=0\) for every \(n\), but rotate an observer's window center as \(c_n=2\pi n/\varphi\bmod2\pi\). The centers scan the circle uniformly while the *source* remains a point mass. Without a declared common-basis transport, the apparent scanning is not source equidistribution.

## HPB-C5 — the uniquely self-calibrating aperture is golden (PROVED, conditional normalization)

There is a particularly clean reason to consider the golden aperture beyond its Diophantine robustness.

Let \(a=\delta/\pi\in(0,1)\). Define two quantities from the *same, declared* geometric/observational model:

1. **Geometric capacity fraction** \(C(a)=m(A_\delta(c))=a\), independent of center \(c\).
2. **Locked-point deviation from Haar** \(L(a)=E_\delta(\delta_c)=1/a-1\), also independent of center \(c\).

Demand the explicit **self-calibration condition** \(C(a)=L(a)\). Then
\[
a=\frac1a-1\quad\Longleftrightarrow\quad a^2+a-1=0.
\]
The **unique** solution in \((0,1)\) is
\[
\boxed{a=(\sqrt5-1)/2=\varphi^{-1}.}
\]

*Proof:* \(C(a)\) strictly increases from 0 to 1 while \(L(a)\) strictly decreases from infinity to 0, so they intersect once; solving the quadratic gives the stated value. This is an exact equality of two distinct, typed observables: window measure and \(L^2\) discrepancy for a maximally locked orbit.

**Boundary:** The equality \(C=L\) is an *optional design/normalization criterion*. Circle geometry alone does not require the geometric aperture and statistical discrepancy to be equal, and changing the discrepancy functional changes the selected number. We have found a coherent way to **choose** a golden observation window, not derived \(\varphi\) from a physical law or from the original BBP source. Once chosen, HPB-C3 additionally proves no Fourier mode is erased and provides explicit polynomial inverse-conditioning.

## Original-source SUCC integration and critical gate

Use the authentic BBP rational forcing and \(U_0=0\), not \(\varphi^n\) as an invented π source:
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_n=16U_{n-1}+r(n).
\]
For the dyadic empirical measure
\[
\mu_A=A^{-1}\sum_{n=A}^{2A-1}\delta_{2\pi\{U_n\}},
\]
the already proved source/gauge + Weyl equivalence in [the maintained π frontier](../../../docs/PI_NORMALITY_FRONTIER.md) combines with HPB-C2 to give the **conditional reformulation**
\[
\boxed{\text{π normal in base 16}
\iff E_{\pi/\varphi}(\mu_A)\to0.}
\]
It is not a proof that either condition holds. This is an alternative *positive energy instrument* for the same unresolved selected fixed-\(h\) signed Weyl gate.

**Next hostile probe:** Prove a truly *source- and zero-seed-selective* upper bound on \(E_{\pi/\varphi}(\mu_A)\), and demonstrate that the argument fails on the coherent wrong seed \(s_*=-\pi/16\) (source phases lock), the nonstationary CB-3 seed, periodic completions, and rational-aperture Fourier-annihilation controls. A window theorem without an authentic estimate is not progress on normality. Conversely, such an estimate would transfer to each fixed Fourier mode with explicit \(O(h^2)\) conditioning.

**Relation to Euler–Mascheroni:** HPB-01's \(\gamma\) arises from an *externally imposed harmonic weighting and logarithmic subtraction*, whereas the original BBP source is balanced and \(r(n)\sim15/(64n^2)\). Circle curvature does not select \(\gamma\) or the golden aperture. Those identifications remain UNVERIFIED until a source-preserving map is supplied.

## Provenance and claim ledger

- HPB-C1 — geometry and conditional actuation: **PROVED MODEL**; actual BBP controls absent.
- HPB-C2 — aperture Fourier/Parseval equivalence and rational-angle mutant: **PROVED elementary analysis**.
- HPB-C3 — golden Diophantine inverse bound: **PROVED elementary quadratic algebra**.
- HPB-C4 — locked-phase residual/moving-frame mutant: **PROVED MODEL**.
- HPB-C5 — unique self-calibrated golden aperture under the explicitly chosen Haar/\(L^2\) equality: **PROVED MODEL**; not a physical selection law.
- π original-source aperture-energy decay: **OPEN**. Physical window of future freedom: **UNVERIFIED**.
- Classical context: https://mathworld.wolfram.com/BadlyApproximable.html (quadratic irrationals); https://mccuan.math.gatech.edu/courses/6455/curvature.pdf (intrinsic/extrinsic); SUCC main frontier and draft PRs #470, #471, #534, #537.

No changes to original source, frozen proofs, formal kernel, main, archive, provenance, license, or release state.
