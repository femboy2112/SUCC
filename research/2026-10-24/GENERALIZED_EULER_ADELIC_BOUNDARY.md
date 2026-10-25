# Generalized Euler–Mascheroni as an SUCC/FUCC/adelic boundary

**Date:** 2026-10-24. **Research branch:** research/generalized-euler-adelic-boundary-2026-10-24. **Inspected base:** main@e648df3e4fca73ab6b942232b5ca4b310e9cac08.
**Source question:** The author's generalized Euler–Mascheroni construction is a finite discrete successor against continuum unit-scaling boundary. Does its complete analytic form constrain prime/adelic geometry, and what source information is still missing? Existing provenance in the repository's Pontryagin, Tate-Mellin, circle-Gamma and orbit-clock supplements remains intact.

**Status:** classical analytic proofs made explicit, exact rational finite probes, negative source controls and numerical diagnostics. No claimed new academic priority for zeta, Basel or Tate. No RH or pi-normality proof.

## 1. Original generalized SUCC boundary: exact domain and a sharp endpoint obstruction

For complex s and positive N, set

\[
D_N(s)=\sum_{n=1}^N n^{-s}-\int_1^N x^{-s}\,dx,
\qquad
\Delta_s(n)=n^{-s}-\int_n^{n+1}x^{-s}\,dx.
\]

**EAB-01 (classical, paper proved).** For each complex s satisfying \(\Re(s)>0\),

\[
\boxed{\lim_{N\to\infty}D_N(s)=G(s)=\zeta(s)-\frac1{s-1},\quad G(1)=\gamma.}
\]

The limit is locally uniform on that half-plane. The function G then admits a unique *entire analytic continuation*; continuation is not the original limit outside its convergence region.

**Proof.** For \(\sigma=\Re(s)>0\), by the fundamental theorem of calculus,

\[
\Delta_s(n)=s\int_n^{n+1}\int_n^x u^{-s-1}\,du\,dx,\qquad
|\Delta_s(n)|\le\frac{|s|}{2n^{\sigma+1}}.
\]

The series of cells converges absolutely and locally uniformly for \(\sigma>0\). The exact finite identity

\[
D_N(s)=\sum_{n=1}^{N-1}\Delta_s(n)+N^{-s}
\]

shows its limit is the cell series. For \(\sigma>1\), summation and integration converge separately, giving \(\zeta(s)-1/(s-1)\). The identity theorem extends this to \(\sigma>0\). The standard meromorphic continuation of zeta, with its single pole of residue one, extends G entire. QED.

For real r>0 every cell is nonnegative. The same derivative bound gives the exact analytic tail

\[
\boxed{0\le G(r)-\sum_{n=1}^N\Delta_r(n)\le\frac{1}{2N^r}.}
\]

At integral r>=2 the finite sum and endpoints are entirely rational and are implemented with Python Fraction.

**EAB-02 (decisive endpoint counterexample).** For *every* N, the literal original cutoff at s=0 is \(D_N(0)=N-(N-1)=1\). But the analytically continued G obeys \(G(0)=\zeta(0)+1=1/2\), so

\[
\lim_{s\to0^+}\lim_{N\to\infty}D_N(s)=\frac12
\ne1=\lim_{N\to\infty}\lim_{s\to0^+}D_N(s).
\]

The half-unit is the Euler–Maclaurin endpoint discrepancy. The author's original expression uses N atoms but N-1 continuum cells. At nonzero purely imaginary s, the \(N^{-s}/2\) endpoint typically oscillates; at negative real s the finite expression typically diverges. Neither is legitimately covered by the original limit theorem.

An exact centered-geometry formula for \(\Re(s)>0\) is

\[
G(s)=1-s\int_1^\infty\{x\}x^{-s-1}dx
=\frac12-s\int_1^\infty(\{x\}-1/2)x^{-s-1}dx.
\]

This is integer counting against Lebesgue measure; the centered sawtooth is the periodic first Bernoulli function, giving a genuine circle-Fourier/Mellin route. **This additive/real construction alone is not adelic**: authentic p-adic local factors, diagonal Q, Haar normalizations and Poisson compatibility must be supplied.

**EAB-05 (all Stieltjes jets).** The conventional Stieltjes constants satisfy

\[
\zeta(s)=\frac1{s-1}+\sum_{m\ge0}\frac{(-1)^m\gamma_m}{m!}(s-1)^m,
\]

hence the locally uniform derivative series gives

\[
\boxed{
(-1)^m\gamma_m=G^{(m)}(1)=
\sum_{n=1}^\infty\left[
\frac{(-\log n)^m}{n}
-\int_n^{n+1}\frac{(-\log x)^m}{x}dx
\right].
}
\]

The complete infinite jet determines the *entire* G by its Taylor expansion, and therefore determines zeta. Any finite jet need not determine the source. Do not conflate mathematical exact infinite data with finite causal access.

## 2. Hurwitz source gauge: the finite unit is not baseless without normalization

For h>0 and q>0, define the matched N-cell chart

\[
D_N^{q,h}(s)=\sum_{k=0}^{N-1}(h(q+k))^{-s}
-\frac1h\int_{hq}^{h(q+N)}x^{-s}dx.
\]

The classical Hurwitz zeta recurrence and the same cell proof yield for \(\Re(s)>0\):

\[
\boxed{
G_{q,h}(s)=h^{-s}\left[\zeta(s,q)-\frac{q^{1-s}}{s-1}\right],
\qquad
G_{q,h}(1)=\frac{-\psi(q)+\log q}{h}.
}
\]

For q=h=1 it equals gamma. Changing q=2,h=1 gives gamma-1+log(2), not gamma; changing h scales the result. For the matched N-cell convention, the finite original value at s=0 is 0 (N atoms minus N cells), whereas continuation is 1/2. Both the source chart and endpoint convention change the scalar. This is a **refutation of gauge-free scalar identification**, not an obstruction to source-normalized adelic transport.

## 3. Authentic FUCC prime jet and noncommuting limit square

For \(\Re(s)>1\) the classical genuine-prime Euler-product identity is

\[
P(s)=-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{p\text{ genuine prime}}\sum_{k=1}^\infty(\log p)p^{-ks}.
\]

Because \(\zeta=G+(s-1)^{-1}\), algebra yields the exact SUCC/FUCC compatibility relation

\[
\boxed{
G'(s)+P(s)G(s)=\frac1{(s-1)^2}-\frac{P(s)}{s-1}.
}
\]

Operator packaging uses \(S|n\rangle=|n+1\rangle\), \(V_p|n\rangle=|pn\rangle\), and \(D|n\rangle=(\log n)|n\rangle\), giving

\[
[D,S]|n\rangle=\log(1+1/n)|n+1\rangle,\quad
[D,V_p]|n\rangle=(\log p)|pn\rangle.
\]

The transport relation is **classical**, not a new theorem about independent SUCC axioms. Fake composite p=6 changes the Euler product and fails original-source authentication.

For real s>1, let \(P_X(s)=\prod_{p\le X}(1-p^{-s})^{-1}\). Its convergent Dirichlet series enumerates X-smooth positive integers and therefore includes every n<=X. Thus the missing terms obey

\[
\boxed{
0\le\zeta(s)-P_X(s)
\le\sum_{n>X}n^{-s}
\le\frac{X^{1-s}}{s-1}.
}
\]

For any **fixed finite** X, \(P_X(s)\) is regular at s=1, so \(P_X(s)-1/(s-1)\to-\infty\) as s decreases to 1. Taking X to infinity first and then s to 1 produces gamma. The prime-completion/pole-subtraction square **does not commute**. By contrast the additive SUCC cell limit is locally uniform at one, so its limit and s=1 evaluation commute.

**EAB-08, explicit cofinal source path.** Choose q>=2 integer, \(\varepsilon=1/q\), \(X=q^{2q}\). The preceding exact inequality specializes to

\[
\boxed{
0\le\zeta(1+1/q)-P_{q^{2q}}(1+1/q)\le1/q.
}
\]

Consequently the properly ordered diagonal limit has

\[
\boxed{\lim_{q\to\infty}
\left(P_{q^{2q}}(1+1/q)-q\right)=\gamma.}
\]

No prime number theorem is needed. The chosen cutoff is astronomically large and cannot be reinterpreted as finite-time complete knowledge. The module verifies integer cutoff formulas and small cases q=2,3,4; the analytic theorem follows independently from the smooth-number inclusion.

### EAB-11: a finite-jet source-selection countermodel

Fix m>=0 and distinct genuine primes p_1,...,p_(m+3). Write \(L_p(s)=-\log(1-p^{-s})\). Choose a nonzero real vector a satisfying

\[
\sum_{j=1}^{m+3}a_jL_{p_j}^{(k)}(1)=0,\quad k=0,\ldots,m+1.
\]

There are m+3 unknowns and m+2 linear constraints, so such a vector exists. Rescale to ensure every 1+a_j>0. Set

\[
F(s)=\zeta(s)\prod_j(1-p_j^{-s})^{-a_j}.
\]

The multiplier is \(1+O((s-1)^{m+2})\); since zeta has a simple pole, \(F(s)-\zeta(s)=O((s-1)^{m+1})\). Thus F has the same residue and first m+1 regular Laurent coefficients, including gamma when m=0. However F is not identically zeta: the local logarithmic Dirichlet series at distinct prime powers are linearly independent. **This is a generalized positive-exponent Euler product with modified, nonauthentic Tate local exponents**, not an alternative legitimate source for Q. The finite gamma jet cannot distinguish the products; authenticated local factors can.

## 4. Genuinely adelic object: complete BOTH poles

The rational adelic Tate/Poisson completion is

\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\Lambda(s)=\Lambda(1-s).
\]

Its two poles are at s=1 with residue +1 and s=0 with residue -1. Define the *balanced* global remainder

\[
\boxed{B(s)=\Lambda(s)-\frac1{s-1}+\frac1s.}
\]

It is entire, reflection-invariant \(B(s)=B(1-s)\), and has the honest Poisson/theta heat representation

\[
\boxed{
B(s)=\int_1^\infty
\left(\sum_{n=1}^\infty e^{-\pi n^2t}\right)
\left(t^{s/2}+t^{(1-s)/2}\right)\frac{dt}{t}.
}
\]

**Proof sketch:** Start from the Mellin representation of \((\theta(t)-1)/2\) for Re(s)>1, split at t=1, apply the classical Poisson identity \(\theta(t)=t^{-1/2}\theta(1/t)\), and integrate the two elementary power-law contributions \(1/(s-1)-1/s\). Exponential heat decay makes the remainder entire and its integrand is symmetric. This is a precise reformulation of classical Poisson/Tate, not a new physical or analytic source proof.

The real Gamma factor gives the regular value

\[
\boxed{B(0)=B(1)=1+\frac\gamma2-\log(2\sqrt\pi)
=0.0230957089661210338\ldots.}
\]

This is much closer to a normalized **adelic boundary signature** than bare gamma: its archimedean place, p-adic product and both reflected poles enter.

On s=1/2+it, B is a Fourier cosine transform of a positive measure:

\[
B(1/2+it)=2\int_1^\infty
\left(\sum_{n\ge1}e^{-\pi n^2u}\right)
u^{1/4}\cos(t\log(u)/2)\frac{du}{u}.
\]

Thus B as a function of real t is positive definite, but that does **not** imply positivity of the completed Weil form or confinement of zeros to the critical line. Exact hostile model:
\(f(t)=2+\cos(t)\) has strictly positive values for real t, and the Gram decomposition
\(f(t_i-t_j)=2+\cos t_i\cos t_j+\sin t_i\sin t_j\)
shows positive definiteness; nevertheless
\(f(\pi+i\,\mathrm{arcosh}(2))=0\) off the real line.

**EAB-12, functional-equation-preserving mutant:** For each m>=0 and c nonzero,

\[
A_m(s)=1+c[s(1-s)]^{m+2}
\]

is invariant under s↔1-s, equals one at the two poles, and differs from one by \(O((s-1)^{m+2})\) at one. Multiplying completed zeta by A_m preserves the reflection equation, both pole residues and the first m+1 regular coefficients, but changes values elsewhere. This construction need not be a genuine Tate/Euler source; it *refutes* using reflection plus finite jets alone as identification criteria.

## 5. New-to-SUCC exact finite hexadecimal pi certificate

For r=2, the discrete-vs-continuous cell simplifies:

\[
\Delta_2(n)=\frac1{n^2}-\left(\frac1n-\frac1{n+1}\right)
=\frac1{n^2(n+1)}.
\]

The **external classical Basel theorem** \(\zeta(2)=\pi^2/6\) now gives

\[
\boxed{\pi^2=6\left(1+\sum_{n=1}^\infty\frac1{n^2(n+1)}\right).}
\]

Use the proved rational tail to obtain exact rational lower and upper bounds:

\[
\boxed{
6\left(1+\sum_{n=1}^N\frac1{n^2(n+1)}\right)
\le\pi^2\le
6\left(1+\sum_{n=1}^N\frac1{n^2(n+1)}
+\frac1{2N^2}\right).
}
\]

Integer square roots of the endpoint fractions times \(16^{2d}\) certify a hexadecimal prefix whenever both floors coincide. **At N=50, 3.243 is certified; at N=300, 3.243F is certified.** No floating-point value of pi, cached digits or zeta values enter the finite certification. Basel is a declared external prerequisite. This is an \(O(N^{-2})\) enclosure, not a practical BBP replacement and **not a normality-frequency bound**.

## 6. Existing clock source, verdict, and next decisive probe

The inherited SUCC OCG-05 exact period-clock jump says
\(L_n/L_{n-1}=p\) if n is p^k, otherwise one, with \(L_n=\mathrm{lcm}(1,\ldots,n)\). Thus it recovers the von Mangoldt current by taking logarithms; the classical PNT further implies
\(\gamma=\lim_N(\log N-\sum_{n=2}^N\Lambda(n)/n)\).
The finite probes recover prime-power jumps, not the global completion.

**SURVIVES:** generalized Euler defect as source-charted additive boundary; exact Fucc/current transport; explicit prime cofinal limit; genuine balanced Tate/theta finite-part; rational SUCC-to-pi digit enclosures.

**REFUTED or restricted by concrete witnesses:** universal literal limit outside Re(s)>0; interchange at s=0; gauge-free gamma; fixed-prime pole subtraction; uniqueness from finite gamma jets; uniqueness from FE plus finite jets; positive-type Fourier kernel implies RH; computing any number of pi digits implies pi normality.

**UNVERIFIED:** a source-authenticated unique adelic geometry from physically accessible probes; uniform original signed-Weil positivity; any BBP carry-correlation decay implying 1/16 hexadecimal frequencies.

**Next falsifier:** use the finite-jet-matched prime mutant as a rival and apply a separately sourced local character/valuation signature at p=2,3,5. Check that authentic Tate Fourier/Poisson transport excludes it rather than merely matching regular Laurent constants. For pi normality, transport the *actual* base-16 BBP circle/carry orbit into nonzero-frequency estimates. Missing source-specific long-range correlation control remains the load-bearing obstruction.

## Reproduction and references

Classical references: [NIST DLMF 25.2](https://dlmf.nist.gov/25.2), [NIST DLMF 25.11](https://dlmf.nist.gov/25.11), classical Tate/Poisson (also inherited adelic theta module), classical Basel and PNT. No original frozen archival source was modified.

New files: observational_succ/generalized_euler_adelic.py, tests/test_generalized_euler_adelic.py, scripts/generalized_euler_adelic_probe.py, docs/CLAIM_SUPPLEMENT_GENERALIZED_EULER_ADELIC.md.

**Observed local isolated baseline:** Python 3.13, twelve targeted unittest groups passed before GitHub integration. Run the targeted test and diagnostic script, followed by all AGENTS.md mandated repository-wide checks. Numerical theta quadrature is never an exact interval proof, and hosted CI status must be checked independently. **RH PROVED: NO. PI NORMALITY PROVED: NO.**
