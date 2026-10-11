# SUCC-shadow selection: finite transverse windows, Gamma uniqueness, and why weighting logarithm branches is not enough

**Research date:** 2026-10-10. **RH OPEN.** Parent: aletheia/gamma-succ-prime-transport-2026-10-10 at commit 20378ead23de4b4e5e3ec120ac1c0958c0b6f5de. Main at start: 22b6dadbd1983159e6c5d8cc32fb9aeff6925ec6, untouched.

**User hypothesis:** for functions that become indistinguishable under finite SUCC endpoint observations, a canonical/primal realization may be selected by measuring and weighting their complete, potentially infinite, SUCC-shadow paths. Their earlier framing insists that no single finite stage must be the global object.

**Mathematical repair:** replace an unspecified Feynman-type measure/complexity prior by a DECLARED and falsifiable family of transverse finite-difference (log-convexity) probes; show exactly why this selects Gamma, what any limited probe class misses, and why a naive damping weight on complex-log winding cannot preserve composition.

**Files:** actualization/succ_shadow_window.py and tests/actualization/test_succ_shadow_window.py. No zeta zeros, theta-series zero inputs, or full Weil positive form used.

**Authoritative mathematical cross-checks:**
- NIST DLMF §5.5(iv), [Bohr–Mollerup theorem](https://dlmf.nist.gov/5.5.iv): positive, normalized, log-convex solution of F(x+1)=x F(x) is Gamma.
- NIST DLMF §5.15.1, [trigamma positive series](https://dlmf.nist.gov/5.15.E1): ψ'(x)=Σ_(k≥0)(x+k)^(-2).
- NIST DLMF §4.2, [complex logarithm branches](https://dlmf.nist.gov/4.2): Log z differs by 2πik; principal branch is analytic only off a branch cut.
- Mathlib4, [BohrMollerup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gamma/BohrMollerup.html): independently formalized result including the Euler sequence.
- Prior branch research/2026-10-10/SUCC_GAMMA_PRIME_PATH_GERMS.md: factorial data and Gamma recurrence do not determine the extension; eps*sin(2πx) periodic gauges are counterexamples without convexity.

## 1. The exact canonical-selection theorem as an infinite realization

Let F:(0,∞)->(0,∞) be continuous, F(1)=1 and

\[
F(x+1)=xF(x)\quad(x>0).
\]

Since Γ has the same recurrence, the function

\[
q(x)=\log F(x)-\log\Gamma(x)
\]

is **continuous and 1-periodic**. At every integer n, F(n)=Γ(n)=(n−1)!, but between integers q can carry arbitrary nonzero information.

Fix a rational fractional offset θ, rational h>0, and sufficiently large integer n so n+θ±h>0. Define the *finite SUCC-shadow window*

\[
W_{n,\theta,h}(F)=
\log F(n+\theta-h)+\log F(n+\theta+h)
-2\log F(n+\theta).
\]

This is a real three-point observation of the same function, a finite window translated n times by SUCC. It reads curvature *transverse* to the integer orbit.

By the trigamma series ψ'(x)=Σ_(k≥0)(x+k)^(-2) and integral comparison,

\[
0<\psi'(x)\le\frac1x+\frac1{x^2}\quad (x>0).
\]

The Gamma contribution satisfies for fixed θ,h

\[
0\le W_{n,\theta,h}(\Gamma)
=\int_{-h}^{h}(h-|t|)\psi'(n+\theta+t)\,dt
\longrightarrow0.
\]

The periodic q contribution is exactly independent of n. Therefore

\[
\boxed{\lim_{n\to\infty}W_{n,\theta,h}(F)
=q(\theta-h)+q(\theta+h)-2q(\theta).}
\]

If F is log-convex on all of (0,∞), every W is nonnegative. Hence the limiting second differences of q are nonnegative. Because rational θ,h form a dense set, continuity yields midpoint convexity on the entire real line; a continuous midpoint-convex function is convex. A convex 1-periodic function is constant. F(1)=Γ(1)=1 forces q=0. Thus F=Γ.

**This is the Bohr–Mollerup theorem rewritten as an observable SUCC/limit-selection lemma**, not an original proof of a new theorem. Conversely Γ satisfies the recurrence and log-convexity, so selection is nonempty and exact.

Crucial quantifier structure:

- Each W is finite and computable when F can be evaluated at three rational offsets.
- The condition quantifies over **all** such windows and **unbounded** integer shifts.
- Every noncanonical continuous periodic q violates some finite window at sufficiently large n, because a nonconstant continuous periodic function cannot be convex.
- A restricted family may fail forever. This is why **probe completeness** is load-bearing, not an arbitrary normalization chosen after the fact.
- Nothing implies that a realizable observer executes all windows; the mathematical theorem is about the infinite coherent family.

## 2. Exact finite witness for a noncanonical periodic Gamma gauge

Take

\[
F_{\epsilon,r}(x)=\Gamma(x)\exp(\epsilon\sin(2\pi r x)),
\qquad r\in\mathbb N,\quad\epsilon\in\mathbb Q\setminus\{0\}.
\]

The SUCC recurrence and every positive integer factorial value are identical to Γ. Let

\[
h=\frac1{4r},\qquad
\theta=
\begin{cases}
1/(4r), & \epsilon>0,\\
3/(4r), & \epsilon<0.
\end{cases}
\]

At exactly these rational offsets, the periodic gauge's second difference is **exactly** \(-2|\epsilon|\). The Gamma contribution obeys the rational upper bound

\[
0<W_{n,\theta,h}(\Gamma)
\le h^2\left(\frac1n+\frac1{n^2}\right)
\]

since all sampled x are ≥n. The explicitly constructible stage

\[
\boxed{n=\max\left(1,\left\lfloor\frac{1}{16r^2|\epsilon|}\right\rfloor+1\right)}
\]

ensures that the upper bound is strictly smaller than \(2|\epsilon|\). Hence **one finite window provably rejects every nonzero gauge of this family**, without numerically evaluating Γ or any π constants. Larger frequencies can be detected by correspondingly narrower shadow offsets.

A complementary exact *finite blindness* certificate: for a fixed horizon N the trigamma lower bound ψ'(x)≥1/x² and x≤n+1 on these matched windows gives

\[
W_{n,\theta,h}(\Gamma)\ge\frac{h^2}{(n+1)^2}.
\]

Thus if \(2|\epsilon|\le h^2/(N+1)^2\), every matched shadow window with \(1\le n\le N\) stays nonnegative. No uniformly bounded horizon detects all nonzero deformations; the stage needed can grow arbitrarily large.

This is a precise operational example of the user's "you can keep walking forever, no single finite horizon globally certifies the structure" distinction. It does not imply mathematical undecidability.

## 3. The important hostile control: same-cell windows can fail FOREVER

Consider a completely different continuous periodic gauge

\[
q_\epsilon(x)=\epsilon\left(\{x\}^2-\{x\}\right),\quad\epsilon>0
\]

with fractional part {x}. q is continuous and 1-periodic: q(0)=q(1)=0. On every **open integer cell** \((n,n+1)\), \(q''(x)=2\epsilon>0\).

Therefore Gamma multiplied by \(e^{q_\epsilon}\) has *positive log curvature everywhere strictly inside every successor cell*. **Even an infinite scan of same-cell-only convexity windows cannot distinguish it from Gamma by their signs.**

At the integer seam, however, q' jumps DOWN by 2epsilon. For rational h=1/4:

\[
\Delta_h^2q_\epsilon(n)
=q_\epsilon(n-h)+q_\epsilon(n+h)-2q_\epsilon(n)
=-2\epsilon h(1-h)=-3\epsilon/8<0.
\]

Gamma's contribution at this **boundary-straddling shadow window** is bounded by

\[
W_{n,0,h}(\Gamma)
\le h^2\left(\frac1{n-1}+\frac1{(n-1)^2}\right)\quad(n\ge2).
\]

Selecting \(n=\max(2,\lfloor 1/(3\epsilon)\rfloor+2)\) gives an exact strictly negative total.

**Verdict:** merely increasing the observation horizon is insufficient unless the probe family actually crosses the correct structural seams. The direction/window coverage can matter more than the number of SUCC steps. A fixed quarter grid is also blind to the gauge q(x)=epsilon*sin(4πx), while an eighth-grid is not.

This result is a direct warning for attempts to replace RH by finite-prime window exhaustion: a missed probe direction may persist at every horizon. It is not a new zeta theorem.

## 4. Can an explicit positive "SUCC measure" select the primal gamma?

**Yes as a mathematical selection functional, with one nonnegotiable caveat: its selection law must be independently justified.** Enumerate a countable, dense, complete set of rational transverse windows \(W_j\), including windows crossing integer seams and integer stages going to infinity. Assign **arbitrary strictly positive summable weights** \(w_j\) with \(\sum_jw_j=1\), e.g. \(2^{-j}\).

Define

\[
\boxed{
\mathcal A(F)=\sum_{j\ge1}
w_j\min\left(1,\left[\max(0,-W_j(F))\right]^2\right).
}
\]

This is a well-defined number in [0,1]. Every legitimate Γ window is ≥0, so \(\mathcal A(\Gamma)=0\). Every noncanonical continuous recurrence solution has a **strict negative window**, and by continuity it can be found in the rational exhaustive family, giving \(\mathcal A(F)>0\). Therefore under the recurrence and normalization

\[
\boxed{\mathcal A(F)=0\iff F=\Gamma.}
\]

The exact program implements a source-independent **rational lower bound on a witnessed positive action contribution**:

\[
\mathcal A(F)\ge w\min(1,m^2)>0,
\qquad
m=-\left(W^{\rm upper}_\Gamma+\Delta^2q\right).
\]

This makes the user's weighted-path idea precise without fabricating a quantum path integral. The numerical penalty weights are **not uniquely canonical**; all full-support choices have the same zero set, but they may differ arbitrarily in convergence rates and which violation is detected first. No "simplest possible function" theorem follows from an unspecified Occam prior.

A different theoretical foundation (entropy, action, semigroup representation, independent geometry, or physical measure) is needed to justify any particular weights as more than a deliberate mathematical probe design.

## 5. Complex logarithm: why this is related, and importantly different

The complex exponential is a single-valued map \(\exp:\mathbb C\to\mathbb C^\times\), but its inverse requires a lift. For closed paths around 0, all integer winding classes have the same exponentiated endpoint:

\[
e^{2\pi i k}=1,\qquad k\in\mathbb Z.
\]

The logarithmic lifts differ by \(2\pi ik\). Continuing around a loop of winding k changes log by \(2\pi ik\). This is *monodromy/topology*, not a family of arbitrary positive real periodic gamma gauges.

The finite trace WindingHistory stores the signed winding word, its inverse and concatenation; endpoint evaluation deliberately forgets winding. This realizes a tiny exact path-vs-value example, not a complex-log reconstruction algorithm.

Suppose a Feynman-inspired weight for a winding sector were proposed:

\[
W(k)=e^{-\alpha k^2},\qquad\alpha>0.
\]

If one insists on a scalar weight respecting path concatenation, W(k+l)=W(k)W(l), it FAILS:

\[
\log\frac{W(k+l)}{W(k)W(l)}=-2\alpha kl.
\]

In particular concatenating a loop and its inverse has total winding 0, weight 1, while their individual damped weights multiply to \(e^{-2\alpha}\), not 1.

There is an exact elementary no-go: if W is a positive, symmetric, strictly composition-preserving scalar weight on integer winding classes, then

\[
W(k)W(-k)=W(0)=1,\quad W(-k)=W(k)>0
\implies W(k)=1.
\]

So **no nontrivial symmetric damping survives these gluing axioms**. This does NOT prohibit more general path integrals, transfer operators, matrix-valued weights, nonlocal actions, or weights with an explicit gluing correction; it tells us the naive weighting prescription is insufficient.

A global holomorphic logarithm on \(\mathbb C^\times\) cannot be restored by weighting away monodromy: \(\oint_{|z|=1}dz/z=2\pi i\). One must either retain the universal cover/path lift or restrict to a simply connected branch domain. The Gamma-gauge problem instead admits a unique positive real solution selected by log-convexity and normalization.

## 6. Relevance to RH, and the next falsifiable construction

- **Disclosed:** SUCC gamma uniqueness can be recast as a concrete infinite family of finite shifted windows; the sine and piecewise-quadratic gauges supply explicit finite witnesses and controls. These are presentations/elementary consequences of established special-function and convexity mathematics.
- **Disclosed:** endpoint/cancellation loses path and winding data; generic symmetric scalar damping is not compatible with inverse loop composition.
- **Observed:** numeric gamma window readouts checked against the independent exact rational inequalities; mutation suite/CI scope stated by runs.
- **Conjectured:** a source-derived family of mixed finite/archimedean SUCC-shadow windows could discriminate genuine Euler arithmetic and normalize a global geometry.
- **UNVERIFIED:** the key RH bridge: an operator-form-domain analogue of this selection law that both (i) identifies its limit with the full completed Weil functional, and (ii) derives its required positivity independently of the desired zero locations.
- **Not supported:** that "minimum complexity" picks the truth automatically, that convexity of Gamma implies the RH sign, or that branch weights turn a multivalued log into a global holomorphic function.

The next useful probe is **not** merely another large horizon. Specify finite prime-event and gamma transport data as enriched observables with cross-SUCC seam tests, then search for an arithmetic sign/monotonicity law whose low-complexity controls fail under fake n=6 and Davenport–Heilbronn but the true Euler source satisfies it. Determine exactly which finite probe directions are omitted and whether their omission is perpetual even under N→infinity. Only then attempt a completed Weil-form identification on a declared Schwartz/Mellin core.

**Result:** a valid, source-explicit model of how canonical selection can arise from infinitely many finite transversely placed windows. **No proof of RH.**
