# Path-preserving SUCC/Gamma prime-moment transport: m=1 is NOT an informationless quotient

**2026-10-10. RH OPEN.** Based on the frozen infinite-realization research head e534563676cfe5f72e1c594d3d1e89179cf04272. User's load-bearing correction: "Who said cancellation commutes in succ? By quotienting away m=1, you give up the encoding path data." This report takes that literally as a demand for an explicit path/germ object, **not** a claim that scalar cancellation is invalid.

Implementation: actualization/gamma_succ_path.py. Tests: tests/actualization/test_gamma_succ_path.py. Replay: scripts/gamma_succ_path_probe.py. Do not merge to main without review.

### External mathematical anchors

- DLMF §25.4.2: zeta functional equation (https://dlmf.nist.gov/25.4.E2).
- DLMF §27.4.3: absolutely convergent Euler product for Re s>1 (https://dlmf.nist.gov/27.4.E3).
- DLMF §5.5.1: gamma recurrence (https://dlmf.nist.gov/5.5.E1).
- Classical Euler gamma limit and Bohr–Mollerup characterization (e.g. DLMF Chapter 5 https://dlmf.nist.gov/5).
- Earlier repo actualization/infinite_realization.py and actualization/gamma_interferometer.py: Ind-Yoneda finite realization and exact finite Suzuki wavefront; neither constructs a positive Weil form.

## 1. Separate the scalar, the path, and the analytic germ

For \(u\) near 1 define the two positive-half-plane Euler routes

\[
Z_P(s)=\prod_{p\le P}(1-p^{-s})^{-1},\qquad
R_P(u)=\frac{Z_P(2u)}{Z_P(2)^u}.
\]

The **numerator** is the Euler product at the reflected argument \(2u\).
The **denominator** arises because an archimedean \(\pi^{2u}\) factor is
encoded using \(\pi^2=6\zeta(2)\), with exponent \(u\).
These are *two provenance-distinct operations*, even though

\[
R_P(1)=1
\]

holds identically at every finite cutoff and for every choice of valid
formal Euler factors. This is elementary cancellation at the scalar level,
NOT an invalid algebraic step. The lost information is the relation among
the analytic *families*.

A point-evaluation map from analytic germs \(E_1:f\mapsto f(1)\) is not
injective; the derivative functional \(f\mapsto f'(1)\) cannot factor through
this scalar evaluation (constants and \(e^{u-1}\) have the same value at 1,
but different derivatives). Therefore one cannot first quotient to R_P(1)=1,
then expect to reconstruct its infinitesimal transport from that value.

The exact first/second logarithmic germs are

\[
\begin{aligned}
J_P&=\left.\partial_u\log R_P(u)\right|_{u=1}
=\sum_{p\le P}
\left[\log(1-p^{-2})-\frac{2\log p}{p^2-1}\right],\\
H_P&=\left.\partial_u^2\log R_P(u)\right|_{u=1}
=\sum_{p\le P}\frac{4p^2(\log p)^2}{(p^2-1)^2}.
\end{aligned}
\]

For every nonempty true prime prefix, J_P<0 and H_P>0.
The fact that H_P is positive is GENERIC even for artificial
prime-like Euler slots and is **not** a Weil sign or RH argument.

This is a rigorous "cancellation does not preserve path jets" statement.
It is NOT a claim that a lawful scalar quotient ceases to be associative,
nor an assertion of noncommutativity among the actual Euler factors.

### A proved finite-to-infinite jet bound

For \(p\ge2\), let \(x=p^{-2}\le1/4\). The elementary inequalities

\[
|\log(1-x)|\le x/(1-x)\le \tfrac43 p^{-2},
\qquad
\frac{2\log p}{p^2-1}\le\tfrac83(\log p)p^{-2}
\]

and integral comparison against *all integers* after P give the **explicit**
tail estimate for the true prime source:

\[
\boxed{
|J_\infty-J_P|\le\frac{4(2\log P+3)}{3P}
\qquad(P\ge2).
}
\]

This is an honest unconditional finite certificate for the first analytic
transport jet. Its infinite value is

\[
J_\infty=2\frac{\zeta'(2)}{\zeta(2)}-\log\zeta(2).
\]

This derivative uses only the safe Euler half-plane; it has no direct
information about off-line zeros.

## 2. Exact finite gamma from the entire factorial successor path

Preserve the event sequence \(1,2,\ldots,N\) and its prime valuations:

\[
\prod_{k=1}^N k=N!
=\prod_{p\le N}p^{\sum_{j\ge1}\lfloor N/p^j\rfloor}.
\]

This is Legendre's valuation identity and is checked exactly (the
ordered SUCC transcript is retained separately from the factorial
endpoint).

The classical finite Euler gamma approximation is

\[
\boxed{
G_N(z)=\frac{N!\,N^z}{z(z+1)\cdots(z+N)}
\longrightarrow\Gamma(z)\qquad(\Re z>0).
}
\]

Its **finite successor defect** is explicit:

\[
\frac{G_N(z+1)}{G_N(z)}
=\frac{Nz}{N+z+1}\ne z,\qquad
z-\frac{G_N(z+1)}{G_N(z)}
=\frac{z(z+1)}{N+z+1}
\longrightarrow0.
\]

Thus the exact analytic gamma SUCC recurrence is recovered **in the
limit**, even though the finite approximants carry a nonzero boundary
error. This is a direct source-faithful example of an infinite
realization bearing a law absent at every finite cutoff.

An anti-uniqueness check is essential. For any epsilon≠0,

\[
\Gamma_\epsilon(z)
=\Gamma(z)\exp(\epsilon\sin(2\pi z))
\]

has **all the same integer factorial values** and obeys the **same
successor recurrence** \(\Gamma_\epsilon(z+1)=z\Gamma_\epsilon(z)\).
But on the positive real line

\[
(\log\Gamma_\epsilon)''(x)
=\psi'(x)-(2\pi)^2\epsilon\sin(2\pi x),
\]

and since \(\psi'(x)\to0^+\), it eventually violates log-convexity for
every nonzero real epsilon. Hence SUCC plus integer endpoints do not
uniquely select the canonical archimedean Gamma; Bohr–Mollerup's
normalization/log-convexity supplies an essential additional analytic
selection law. No "Gamma determined by factorial values alone" claim
is permissible.

## 3. Replace ALL explicit pi factors, retaining both finite boundaries

The user's previous instruction was to replace instances of pi by
finite/infinite prime expansions, *without erasing the path when the
quotient happens to have scalar value one*.

Define

\[
\pi_P=\sqrt{6Z_P(2)}.
\]

For genuine complete prime prefixes, unique factorization gives

\[
\sum_{n\le P}n^{-2}\le Z_P(2)\le\zeta(2),
\]

so

\[
\boxed{0\le\pi^2-\pi_P^2\le 6/P.}
\]

It follows that \(\pi_P\uparrow\pi\). A nice exact checkpoint:
\(Z_3(2)=(1-1/4)^{-1}(1-1/9)^{-1}=3/2\), hence
\(\boxed{\pi_3=3}\). This is a finite identity, not evidence of an RH
mechanism.

Introduce a SECOND independent finite cutoff for Gamma, \(N\ge2\):

\[
\boxed{
T_{P,N}(u)=
\frac{2^{1-2u}G_N(2u)\cos(\pi_Pu)}{6^u}\,
\frac{Z_P(2u)}{Z_P(2)^u}.
}
\]

All explicit pi symbols have been *replaced in the finite construction*
by the rational prime moment \(Z_P(2)\). Gamma has been replaced by its
fully finite factorial SUCC approximation, and both Euler paths are
retained. For **true** Euler data, **as both P and N go to infinity**,
the classical Euler product, gamma limit and zeta functional equation
imply, locally uniformly for Re(u)>1/2,

\[
\boxed{\lim_{P,N\to\infty}T_{P,N}(u)=\zeta(1-2u).}
\]

At \(u=1\), scalar Euler cancellation occurs within a manifestly
nontrivial finite two-parameter construction:

\[
\boxed{
T_{P,N}(1)=
\frac{N^2}{12(N+1)(N+2)}\,\cos(\pi_P).
}
\]

This is **not** \(-1/12\) at any ordinary finite pair (P,N).
Its joint limit is \(-1/12\), respecting both the prime moment and
Gamma boundary paths. No claim is made that an ordinary divergent
sum/product has a literal total mass of -1/12.

The first displacement jet is richer:

\[
\boxed{
\frac{T'_{P,N}(1)}{T_{P,N}(1)}
=
\underbrace{2\left(\log N-\sum_{k=2}^{N+2}\frac1k\right)}_{\text{finite Gamma/SUCC}}
-\underbrace{2\log2+\log6}_{\text{scalar powers}}
-\underbrace{\pi_P\tan\pi_P}_{\text{sine rotation}}
+\underbrace{J_P}_{\text{finite prime moments}}.
}
\]

In the joint limit (true sources), this reduces to the classical
functional-equation derivative identity

\[
\boxed{
-2\frac{\zeta'(-1)}{\zeta(-1)}
=
2\psi(2)-2\log2-\log6
+2\frac{\zeta'(2)}{\zeta(2)}-\log\zeta(2).
}
\]

The negative-one value is a *zero-jet*, while the first jet retains
arithmetic and archimedean response contributions previously erased.
Higher jets can be computed, but they are not automatically RH-bearing.

## 4. Hostile tests and the "fake arithmetic" verdict

All controls are declared before claiming arithmetic significance.

1. **Scalar collapse:** prime sets (2) versus (2,3), nonunit alpha_2=3/2,
   or synthetic Euler base 6 all give R(1)=1, but their first jets differ.
   Source-validation flags the fake/composite control as not genuine zeta.
2. **Gamma recurrence ambiguity:** periodic Gamma gauge agrees on all
   integer factorials and exact SUCC ratios, but fails log-convexity.
3. **Finite boundary:** G_N(z+1)/G_N(z) deviates from z by the proven
   positive rational defect; it is not silently set to zero.
4. **Pi proxy:** only genuine complete prime prefixes receive the
   explicit \(\pi^2\) tail certificate; mutant sources are denied it.
5. **Analytic holdout:** the joint transport agrees increasingly well
   against a direct mpmath evaluation of \(\zeta(1-2u)\) at real and
   complex u with Re u>1/2. This is a numerical check of a classical
   limit and uses no zero ordinates.
6. **Infinite first jet:** actual finite prime-jet errors are bounded
   by the proven O(log P/P) envelope, checked against independent
   evaluation from \(\zeta'(2)/\zeta(2)\).
7. **Full first jet:** direct \(\zeta'(-1)/\zeta(-1)\) agrees with the
   analytically derived gamma/prime decomposition. No -1/12 mass sum.

Important negative result: **The local jet's sign survives artificial
Euler slots**. The first jet is a *provenance-sensitive diagnostic*, but
its negativity is NOT a separator for RH or even for primality.
Additionally, the safe transport Re u>1/2 corresponds to the zeta
half-plane Re(1-2u)<0: it DOES NOT REACH the critical strip of RH.
Going beyond the safe Euler/prime convergence domain requires an analytic
continuation/renormalization mechanism with its own justified topology;
the functional equation's validity alone does not supply the Weil sign.

## 5. What the mathematics earns

**DISCLOSED (classical algebra, exact scope):** the finite successor Gamma
ratio and boundary; the Legendre prime valuations of factorial; the two
distinct analytic Euler paths and the loss of first-jet data under scalar
evaluation; finite prime-jet formulae; explicit unconditional tail
bounds; finite two-cutoff formula and its locally uniform limit as a
classical functional equation.

**OBSERVED (calibrated, bounded software):** mpmath regression against
independent Gamma/zeta values on the Euler-safe half-plane, synthetic
arithmetic mutation readings, CI output.

**REFUTED:** "m=1 produces no relevant path data because the scalar
ratio is one"; "integer SUCC recurrence alone uniquely determines
Gamma"; "a negative or positive finite moment jet is already Weil sign".

**UNVERIFIED:** an enriched Ind/Yoneda transport of true finite arithmetic
source data across the critical-strip boundary into a signed, closed
Hilbert-form construction satisfying the full Weil identity and a
source-derived positivity theorem. This is gate four; RH stays open.

## 6. Next verdict-changing mathematical probe

Define a *coherent analytic-germ functor* on the successive finite
prime/SUCC diagrams, retaining **values, first and higher jets, labels,
ordered events, and domain data**. Prove compatibility and compact-local
convergence of its finite analytic sections on the safe half-plane,
then attempt a genuinely source-derived continuation/correspondence
whose target is the full Weil form on a common Mellin/Schwartz core.

The decisive comparison must include genuine zeta Euler, a matched
Hecke L-function, and non-Euler Davenport–Heilbronn arithmetic **with
their actual completed factors**, plus composite, clock and half-density
mutations. Passing any scalar cancellation or safe-half-plane reflection
test is not a new RH brick. To promote a claim, derive a non-circular
positivity or geometric intersection law valid on the completed domain
and prove the relevant limits preserve it.

**Status:** a faithful and testable reconstruction of the user's path
insight, not an RH proof or hidden-source oracle.
