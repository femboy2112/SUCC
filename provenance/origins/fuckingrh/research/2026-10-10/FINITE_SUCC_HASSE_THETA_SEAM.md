# The finite-Euler / archimedean Gamma seam: Hasse, theta, trivial-zero jets, and Riemann–Siegel

**Date:** 2026-10-10. **RH IS OPEN.** Research branch \`aletheia/finite-succ-hasse-theta-seam-2026-10-10\`, created at \`7daba0106f4feedfee016e5c1620beaed9b4d6c9\` from the prior Dirichlet-Lambert branch. Main was \`22b6dadbd1983159e6c5d8cc32fb9aeff6925ec6\` at creation and is not changed.

**User hypothesis, preserved in the user's terms:** "Gamma reflection and analytic continuation cause the zeros to be most easily found in the wrong half of the plane, when the data is in the finite bulk that Euler is defined in." The research must not erase finite actualization path data merely because an analytically continued scalar value is zero, one, or otherwise simple.

**Precise repaired reading:** The arithmetic Dirichlet/Euler product is defined and zero-free in Re(s)>1; reflecting that safe region through s->1-s establishes a second zero-free region Re(s)<0 except for *trivial* zeros. Nontrivial zeros live in the "gap" 0<Re(s)<1. We can recover zeta in the gap from *finite SUCC differences* without invoking Gamma reflection, and independently recover the completed xi from *integer Gaussian heat data* and Poisson duality. The overlap and correct source identification are essential; analytic continuation and reflection alone are not positivity. At negative even integers, the Gamma pole cancels the arithmetic zero, so derivative jets, not vanishing endpoint values, carry a **positive Euler-prime log-derivative**. This last identity is classical, but it is an unusually exact operational model of the proposed finite/archimedean coupling.

**Implementation:** \`actualization/hasse_theta_seam.py\`; \`tests/actualization/test_hasse_theta_seam.py\`; \`scripts/hasse_theta_seam_probe.py\`. No fitted nontrivial zero ordinates, zero lists, or RH sign assumptions enter the code. The trivial-zero indices -2m are fixed by Gamma poles and the known Bernoulli parity identity, not inferred from a numerical zero search.

**Primary/authoritative sources**
- NIST DLMF §25.10 [zeros and Riemann–Siegel formula](https://dlmf.nist.gov/25.10), particularly Eq. 25.10.3.
- DLMF §25.2 [Euler product and alternating η function](https://dlmf.nist.gov/25.2), Eq. 25.2.3; §25.4 [functional equation](https://dlmf.nist.gov/25.4).
- Jonathan Sondow (1994), *Analytic continuation of Riemann's zeta function and values at negative integers via Euler's transformation of series*, Proc. AMS 120:421–424, [DOI 10.1090/S0002-9939-1994-1172954-7](https://doi.org/10.1090/S0002-9939-1994-1172954-7).
- Iaroslav V. Blagouchine (2018), *Three Notes on Ser's and Hasse's Representations for the Zeta-Functions*, INTEGERS 18A, [author manuscript](https://math.univ-cotedazur.fr/u/coppo/Iaroslav.pdf), §1 equations (1) and (3), §2.
- Griffin–Ono–Rolen–Thorner–Tripp–Wagner (2019), [Jensen Polynomials for the Riemann Xi Function](https://arxiv.org/abs/1910.01227): equivalence of RH to complete Jensen hyperbolicity, proven regions, NOT a complete proof.
- Jonathan Holland (August 2026), [a hyperbolicity wedge](https://arxiv.org/abs/2608.08682), a recent preprint illustrating the known partial degree/shift region; independently verify before any formal use.

## 1. Two zero-free half-planes and the genuine unknown middle

\[
\zeta(s)=\prod_p(1-p^{-s})^{-1},\qquad \Re(s)>1
\]

is absolutely convergent and nonvanishing. From \(\zeta(s)=\chi(s)\zeta(1-s)\), the reflected Euler-safe half-plane \(\Re(s)<0\) is nonzero except for the simple trivial zeros at -2,-4,-6,.... The nontrivial zero problem occurs only for \(0<\Re(s)<1\). DLMF §25.10 also rules out zero locations on \(\Re(s)=0\) and \(\Re(s)=1\).

This corrects the strong phrase "zeros are most easily found in the wrong half": what is easy to *derive* by reflection in the negative real region are the **trivial zeros**, not the nontrivial RH-zero geometry. The full infinite Euler source *uniquely determines* the analytic continuation and thus all zeros, but no established prime-only structural theorem forces every nontrivial zero onto Re(s)=1/2.

## 2. A Gamma-free SUCC continuation from Euler's finite differences

Let \(\Delta_-f(k)=f(k)-f(k+1)\) and \(\Delta_-^n f(1)=\sum_{j=0}^n(-1)^j\binom nj f(j+1)\). Define

\[
\eta(s)=(1-2^{1-s})\zeta(s)
=\sum_{n=0}^{\infty}\frac{\Delta_-^n[k^{-s}]_{k=1}}{2^{n+1}},
\]

a classical globally convergent Euler transform (Sondow 1994).

Independently, Hasse's other pole-normalized series is

\[
\boxed{\zeta(s)=\frac1{s-1}
  \sum_{n=0}^{\infty}\frac{\Delta_-^n[k^{1-s}]_{k=1}}{n+1}.}
\]

This formula has no artificial \(1-2^{1-s}\) denominator (and no Gamma); it is an independent SUCC weighting on the SAME integer sequence. For the genuine zeta source and nonnegative integer m, \(k^m\) is a polynomial: \(\Delta_-^n k^m=0\) for all n>m. Thus at s=-m the eta formula TERMINATES after n=m, and the pole-normalized Hasse formula TERMINATES after n=m+1. This is an exact finite computation in rational arithmetic, conditional only on the classical identity that the completed infinite formula analytically continues ζ.

At s=-1:

\[
\eta(-1)=1/2-1/4=1/4,\qquad
\zeta(-1)=\frac{1/4}{1-4}=-1/12,
\]

and Hasse gives separately

\[
\zeta(-1)=\frac{1-3/2+2/3}{-2}=-1/12.
\]

At s=-2,-4,-6,... the same finite arithmetic gives the genuine **trivial zeros**, even without introducing a Gamma factor. This is evidence that the *integer SUCC field* already determines analytic continuation values; Gamma is the analytic *dual completion/transport*, not an oracle injecting previously absent numerical data.

**Causality:** \`SUCCDifferenceSource\` requires complete, actualized a(1),...,a(N), refusing guesses for pending events. It records journal head and rational finite-difference rows. For a true zeta prefix through m+2, both finite formulas are cross-checked exactly. Mutated source values are kept as finite diagnostics and not mislabeled zeta values.

## 3. Two fragile normalizations and their hostile non-Euler controls

The eta route is *numerically and algebraically robust* for a **finite sparse source perturbation**, but the usual local prime-two quotient is source-dependent. For arbitrary \(D_a(s)=\sum a(n)n^{-s}\) with absolute convergence and \(E_a(s)=\sum(-1)^{n-1}a(n)n^{-s}\), the exact identity is

\[
\boxed{
E_a(s)-(1-2^{1-s}a(2))D_a(s)
=-2^{1-s}\sum_{m\ge1}\bigl[a(2m)-a(2)a(m)\bigr]m^{-s}.
}
\]

For the true zeta source, every bracket vanishes. For a deliberate complete countermodel a(n)=1 at all n except a(6)=2, the defects are +1 at m=3 and -1 at m=6. In particular

\[
E_{\rm fake}(s)-(1-2^{1-s})D_{\rm fake}(s)
=(-2+2^{1-s})6^{-s}.
\]

This is a **source-sensitive obstruction to a wrongly assumed commuting diagram**. For arbitrary Hecke L-functions, the all-m identity \(a(2m)=a(2)a(m)\) is too strong; only odd m test coprime multiplicativity, so never promote this simple local control to an all-L-function proof.

The Hasse \(1/(n+1)\)-weighted alternative is *more fragile*. Alter a(6) by δ. The corresponding Hasse term for any n>=5 changes by

\[
\frac{\delta\,(-1)^5\binom n5\,6^{1-s}}{(s-1)(n+1)}.
\]

Its magnitude grows like a power of n; the resulting Hasse series DIVERGES rather than analytically continuing \(D_{\rm fake}(s)=\zeta(s)+\delta6^{-s}\). The fake Dirichlet series itself of course admits a meromorphic continuation, so this demonstrates failure of the *source-inappropriately reused Hasse algorithm*, not lack of continuation.

At the other extreme, eta has extra zeros at s=1+2πik/log2 for every nonzero integer k: those are zeros of the factor \(1-2^{1-s}\), not nontrivial zeta zeros. The prime-2 scalar divisor must not be used to claim zero locations without checking cancellation/removable singularities.

**Diagnostic lesson:** analytic transport is **not merely value-preserving**, **not necessarily source-natural under mutations**, and **not positivity**. Its arithmetic compatibility law is an additional gate.

## 4. A second, genuinely archimedean transport: theta and its Gamma completion

Poisson self-duality of the Gaussian gives the *entire* completed xi via

\[
\boxed{
\xi(s)=\frac12+\frac{s(s-1)}2
 \sum_{n\ge1}\int_1^\infty e^{-\pi n^2x}
    \bigl[x^{s/2-1}+x^{(1-s)/2-1}\bigr]\,dx.
}
\]

The two terms are related by \(s\mapsto1-s\). Each n contributes two
upper-incomplete-gamma terms, so the implementation uses

\[
I_n(s)= (\pi n^2)^{-s/2}\Gamma(s/2,\pi n^2)
 +(\pi n^2)^{-(1-s)/2}\Gamma((1-s)/2,\pi n^2).
\]

**Rigorous tail:** on 0<=Re(s)<=1, x>=1 implies
\(|x^{s/2-1}|,|x^{(1-s)/2-1}|\le1\). Therefore, after M terms,

\[
\boxed{
|\xi(s)-\xi_M(s)|\le
\frac{|s(s-1)|}{\pi}
\frac{e^{-\pi(M+1)^2}}
{(M+1)^2(1-e^{-\pi(2M+3)})}.
}
\]

This is an established analytic estimate, not numerical convergence
guessed from a plot. The mpmath evaluation is not directed-rounding
interval arithmetic. The source is every positive integer n, not a
synthetic prime-only spectral zero list.

**Hostile control:** Replace a(6)=1 by 2 in a supposed "theta coefficient
source" and simply sum its symmetrized heat terms. The result is still
exactly symmetric under s->1-s because both orientations were included
BY CONSTRUCTION. Yet it is NOT the completed Dirichlet function of
the mutated source. At s=2 the actual mutated completion differs from
the genuine value by exactly \(1/(36\pi)\), while the fake theta
symmetrization differs from genuine theta by only exponentially tiny
\(O(e^{-36\pi})\).

**Verdict:** formal reflection symmetry can be manufactured for fake
arithmetic. The *Poisson/Dirichlet identification* is what must be
source-derived; a manufactured gamma-symmetric form isn't an RH brick.

## 5. Pole-zero cancellation: "the value dies; its path jet survives"

At s=-2m, m>=1,

\[
\Gamma(s/2)\sim\frac{2(-1)^m}{m!(s+2m)}
\]

while zeta has a simple zero. The product has finite limit

\[
\lim_{s\to-2m}\Gamma(s/2)\zeta(s)
=\frac{2(-1)^m}{m!}\zeta'(-2m).
\]

Reflection to the absolutely convergent Euler region yields

\[
\boxed{
\zeta'(-2m)=(-1)^m\frac{(2m)!}{2(2\pi)^{2m}}
\zeta(2m+1).
}
\]

The literal finite-difference value eta(-2m)=0 terminates after 2m
difference stages. But differentiation with respect to spectral s gives

\[
\eta'(-2m)=-
\sum_{n\ge0}2^{-n-1}
  \Delta_-^n[k^{2m}\log k]_{k=1},
\]

which does **not terminate**. The second derivative involves
\(k^{2m}(\log k)^2\), also nonterminating. This makes the distinction
between finite endpoint scalar and *infinite coherent realization of
finite derivative events* particularly explicit.

These are CLASSICAL identities, now given a source-provenance/SUCC
interpretation, not a new RH result.

## 6. Gamma-subtracted negative-side jet = positive Euler prime current

Write \(f(s)=2^s\pi^{s-1}\Gamma(1-s)\), so \(\chi(s)=f(s)\sin(\pi s/2)\).
At \(s_0=-2m\), the sine has a simple zero, \(f(s_0)\ne0\), and

\[
\frac{\chi''(s_0)}{2\chi'(s_0)}
=\frac{f'(s_0)}{f(s_0)}
=\log(2\pi)-\psi(2m+1).
\]

Twice differentiating \(\zeta(s)=\chi(s)\zeta(1-s)\) at s0 gives

\[
\boxed{
\frac{\zeta''(-2m)}{2\zeta'(-2m)}
+\psi(2m+1)-\log(2\pi)
=-\frac{\zeta'(2m+1)}{\zeta(2m+1)}
=\sum_p\sum_{k\ge1}\frac{\log p}{p^{k(2m+1)}}>0.
}
\]

This is exactly an algebraic instance of "negative-side Gamma
curvature subtraction reveals the finite-prime positive current",
and reads PRIME-POWER LOGARITHMS in a natural way.

The code computes left side from **first and second finite SUCC
derivatives of eta(-2m)**, correctly subtracting the local factor's
log derivative \(C'(s_0)/C(s_0)\), \(C(s)=1-2^{1-s}\). It independently
computes the right from ζ'/ζ at \(2m+1>1\), and also from explicitly
summed genuine primes, proving a finite tail bound for \(\sigma=2m+1\):

\[
\boxed{
0\le J_m-
\sum_{p\le P}\frac{\log p}{p^{\sigma}-1}
\le\frac{P^{1-\sigma}}{1-2^{-\sigma}}
\left[
\frac{\log P}{\sigma-1}
+\frac1{(\sigma-1)^2}
\right].
}
\]

The inequality follows from majorizing omitted primes by all integers
\(n>P\), using monotonicity of \((\log x)x^{-\sigma}\), integral
comparison, and \(1/(n^\sigma-1)\le n^{-\sigma}/(1-2^{-\sigma})\).

**A real limitation:** this positivity is already implied by the
convergent Euler product. It is a special family indexed by integers
m>=1, outside the RH critical strip. It cannot establish full Weil
positivity without an independently justified extension law preserving
the appropriate form sign over *all* admissible probes. In particular,
finite differences and Gamma subtraction are not themselves that law.

## 7. A familiar real SUCC/factor-square window: Riemann–Siegel

DLMF §25.10, equation 25.10.3, already contains a remarkable
finite-to-archimedean relation on the **actual critical line**:

\[
\boxed{
Z(t)=
2\sum_{n\le\lfloor\sqrt{t/(2\pi)}\rfloor}
\frac{\cos(\vartheta(t)-t\log n)}{\sqrt n}
+R(t),
}
\]

where \(\vartheta(t)=\Im\log\Gamma(1/4+it/2)-(t/2)\log\pi\).

The archimedean Gamma phase dictates a **square-root observation
window in finite integers**. This is strikingly close to the
\`factor-square-moving-window\` and SUCC/FUCC half-density cone
already discussed in the repo. It must not be called an original
identity or the complete correction-free answer: the remainder R(t)
matters, especially when deciding signs near zeros.

The source-sensitivity is crisp. Integer n=6 becomes visible in the
Riemann–Siegel leading sum only after

\[
t\ge2\pi\cdot36=72\pi.
\]

A countermodel with fake coefficient a(6)=2 is invisible to this
specific finite leading window below that spectral height, but changes
the leading sum above it by exactly

\[
\Delta Z_{\rm lead}(t)=
\frac{2}{\sqrt6}
\cos\bigl(\vartheta(t)-t\log6\bigr).
\]

This is a *probe-locality* statement, NOT a Riemann–Siegel formula for
the fake L-function and not evidence about zeros at any sample t. The
spectral height t is NOT being identified with the actualization
engine's clock by assumption.

**Outstanding**: an independently derived remainder sign/global
coupling theorem that can enforce Weil positivity. The existing
approximate functional equation does not supply one.

## 8. Reflection and positive values ON the critical line do not imply RH

Take \(x=s-1/2\) and the elementary polynomial

\[
P(x)=x^4+\frac38x^2+\frac{25}{256}.
\]

It is even and real (hence symmetric under \(s\mapsto1-s\) and
complex conjugation). Its roots have s-real parts 1/4 and 3/4,
so ALL of its zeros are off the critical line. Yet for real t

\[
\boxed{P(it)=
\left(t^2-\frac3{16}\right)^2+\frac1{16}>0.}
\]

Thus even reflection symmetry **plus strict pointwise positivity
along the critical line** is insufficient. This does not model a
genuine Euler source; it isolates precisely what a purported generic
gamma/symmetry proof would miss. Our tests evaluate this equality in
exact rational arithmetic and verify its constructed roots
independently.

## 9. Best next proof-bearing target: positivity of the correct completed operator, not phase

The \(\xi\) function is an even real entire function in \(z=s-1/2\).
Pólya's criterion makes RH equivalent to hyperbolicity of **all**
Jensen polynomials formed from the appropriate central Taylor
coefficients, with the full degree/shift quantifiers. This offers an
alternative finite-observable hierarchy for the global sign/real-zero
property. Results by Griffin et al. and the 2026 Holland preprint
establish increasingly large hyperbolic regions, but NOT the global
uniform theorem.

A potentially useful way to organize our program is:
1. **Source:** genuine \(\Lambda(p^k)\), \(\log p\), half-density and
   actualization journal, including independent multiplicativity
   controls.
2. **Two transports:** Euler/Hasse SUCC windows plus Poisson/Gamma
   (theta) completion; prove a **source-natural** commuting seam,
   not just numerical agreement for ζ.
3. **Signed form:** build an arithmetic Hilbert/Weil pairing whose
   positivity follows from a non-circular law compatible with all
   SUCC-shadow windows and boundary terms, OR derive source-dependent
   Jensen hyperbolicity uniformly in all d and n.
4. **Falsification:** true zeta vs fake n=6, altered half-density and
   conductor/character controls, including matched genuine Hecke and
   non-Euler Davenport–Heilbronn with their correct archimedean factors.

The current work completes NOTHING of the missing global Weil-sign
gate. It constructs more exact paths, exposes the sign-free seam,
and recovers **special positive prime currents from negative-side
Gamma-cancelled derivatives**.

## 10. Claim ledger

| Mathematical statement | Status |
|---|---|
| Nontrivial zeros confined to critical strip by Euler zero-freeness and reflection | Classical, DLMF |
| Two SUCC difference continuations give zeta(-1)=-1/12 exactly | Classical Hasse/Sondow, exact Fraction check |
| All negative even trivial zeros are recoverable by finite differences | Classical, exact rational tests |
| Differentiated finite-difference paths do not terminate at negative even arguments | Classical analytic series + explicit nonvanishing windows |
| Gamma pole and zeta trivial zero cancel to derivative data linked to ζ(odd positive) | Classical functional equation |
| Gamma-corrected second jet equals positive prime current with explicit omitted-prime bound | Classical, algebraically derived and numerically cross-checked |
| Poisson/theta entire xi equals completed Dirichlet zeta with Gaussian tail bounds | Classical, independent numerical confirmation |
| Fake a(6)=2 invalidates naïve parity quotient and Hasse source extension; symmetric fake theta ≠ completed fake Dirichlet | Exact algebra / analytic countermodel |
| Riemann–Siegel uses sqrt(t/2π) integer bulk and Gamma phase | Classical, DLMF |
| Reflection + on-line positivity can coexist with off-line zeros | Exact synthetic quartic counterexample |
| Any of this proves Weil positivity or RH | **UNVERIFIED / NOT CLAIMED** |

**Reproduce**
~~~bash
python -m unittest discover -s tests/actualization -p 'test_hasse_theta_seam.py' -v
python scripts/hasse_theta_seam_probe.py
~~~

All implementation choices preserve the distinction between (i) exact
symbolic proof, (ii) known external theorem, (iii) numerical
calibration, and (iv) new conjectural research target.


## 11. A fully positive SUCC moment space from negative-side Gamma jets—and its fatal blindness

A new distinction emerges by sampling the Gamma-subtracted trivial-zero
curvature at successive negative EVEN arguments. Define

\[
J_m=\frac{\zeta''(-2m)}{2\zeta'(-2m)}
+\psi(2m+1)-\log(2\pi)
=-\frac{\zeta'(2m+1)}{\zeta(2m+1)}
=\sum_{n\ge2}\frac{\Lambda(n)}{n^{2m+1}},\quad m\ge1.
\]

Introduce the **finite positive Hausdorff measure**

\[
\boxed{
\mu=\sum_{n\ge2}\frac{\Lambda(n)}{n^3}\,
\delta_{n^{-2}},\qquad
\mathrm{supp}(\mu)\subseteq[0,1/4].
}
\]

Its mass is finite because \(\sum_{n\ge2}\Lambda(n)n^{-3}\)
converges absolutely. Then

\[
\boxed{J_m=\int_{0}^{1/4}x^{m-1}\,d\mu(x).}
\]

Two immediate and **rigorous** forms of positivity follow:

1. Full Hankel moment matrices \(H_{ij}=J_{i+j+1}\) are PSD:
   for a polynomial \(P(x)=\sum_jc_jx^j\),
   \(\sum_{ij}c_ic_j H_{ij}=\int P(x)^2 d\mu(x)\ge0\).
   The shifted matrices \(H'_{ij}=J_{i+j+2}\) are also PSD,
   as is \((1/4)H-H'\) by support constraints.
2. The sequence is *completely monotone under the integer spectral
   SUCC shift* \(m\to m+1\):

\[
\boxed{
(-1)^r \Delta^r J_m
=\sum_{n\ge2}\frac{\Lambda(n)}{n^{2m+1}}
(1-n^{-2})^r\ge0,\qquad r\ge0.
}
\]

This is a mathematically sharp **positive signal architecture**
constructed from exactly the original negative-side Gamma-corrected
jet and infinitely many finite arithmetic prime events. Given
*all* moments J_m, the measure is uniquely determined by the
classical determinacy of the Hausdorff moment problem on compact
[0,1/4]: finite polynomials are dense in continuous functions there.
It is a rigorous version of Yoneda-flavored infinite realization:
a complete family of finite moment probes identifies a global source.

**But the hostile control is absolutely decisive:** append an
artificial **positive** composite source \(c\log6\) at n=6, giving
\(\mu_{\rm fake}=\mu+c\log6/6^3\,\delta_{1/36}\) with c>0.
Every Hankel PSD inequality, all complete-monotonicity signs, and
every positive polynomial-energy test remain valid! Yet the
modified source is NOT the true Euler prime-power logarithmic
derivative, and a fake a(6)=2 already violated the connected
arithmetic condition.

So these positive signs, despite being source-constructive and
recovering a unique measure from their FULL values, remain
**entirely insufficient for RH**. Information completeness,
positivity in a chosen representation, and a source-exclusive
Weil-sign theorem are three logically different properties.

This locates the missing power source quite precisely:
an RH proof must construct a sign or geometric invariant
that distinguishes **primitive Euler multiplicative source
structure** from arbitrary positive signed/unsigned event
injections AND identifies it with the complete Weil form on its
genuine infinite test-function domain.

The code implements the finite Hankel polynomial energy (with a
positive composite-6 countermodel) and independent finite
\((-1)^r\Delta^rJ_m\) / positive-integral calculations. Every
assertion above follows from ordinary moment-problem algebra,
not numerical positivity and not a new zeta-zero proof.

**Final verdict:** SUCC + Gamma do produce genuine, source-based,
globally coherent positive signals in a mathematically exact way.
But the **same generic positivity is compatible with an invalid
positive composite source**. The RH-bearing sign must contain
additional cross-channel arithmetic polarization and spectral
phase information not present in this Hausdorff moment cone.
