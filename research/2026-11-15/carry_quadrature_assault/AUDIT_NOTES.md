# Independent constructor audit of the source controls and excitation

**Date:** 2026-11-15. **Reviewer:** the constructor agent, reviewing the
adversary's `CONTROLS.md` and translator's `SOURCE_EXCITATION.md` after
writing `WINDING_PACKETS.md`. **Verdict:** no mathematical gap found in
the audited claims below, within their stated source and seed scopes.
No original-source positive-density estimate was proved by this audit.

## 1. Mahler controls: universal algebraic review

The construction in `CONTROLS.md`, Section 5, passes the following checks.

- **Rational choices and error control.** Each prescribed dyadic coset
  is dense in the real line because its odd denominators are unbounded.
  The triangular identity \(\binom nn=1\) lets the next coefficient
  meet the new real error target without changing earlier integer
  values. All forward values and source differences have odd rational
  denominators, and \(F(0)=0\) follows exactly from the missing constant
  Mahler coefficient.
- **Analytic convergence.** For \(k\ge2\), every power coefficient of
  \(b_k\binom tk\) has valuation at least
  \(2k-v_2(k!)\ge k+1\). The polynomial terms therefore converge in
  the coefficient sup norm. Their sum is a restricted power series:
  the coefficient of degree \(j\ge2\) has valuation at least \(j+1\).
  This supplies analytic convergence on the closed unit disc, beyond
  merely continuous Mahler convergence.
- **All-\(\mathbb Z_2\) isometry.** The nonlinear difference quotient
  has valuation at least 3. It cannot cancel the unit linear coefficient
  \(b_1\), so \(v_2(F(t)-F(s))=v_2(t-s)\) for all distinct
  \(s,t\in\mathbb Z_2\). This gives bijections of every finite
  quotient, and compatible inverses give surjectivity on
  \(\mathbb Z_2\). The source difference
  \(\widetilde r=F-16F(\cdot-1)\) is also an isometry: its two
  difference terms have valuations separated by exactly four.
- **Backward zero pin.** The finite backward sum telescopes to
  \(F(t)-16^{J+1}F(t-J-1)\). Since \(F(\mathbb Z_2)\subseteq
  \mathbb Z_2\), the remainder tends to zero uniformly. At \(t=0\)
  the limit is exactly zero.
- **Real positivity and asymptotic coefficient.** The monotone positive
  sequence \(\tau_n\) and the stated error tolerance give the lower
  bound \(15.84\tau_{n-1}-1.01\tau_n>0\) for \(n\ge2\).
  At \(n=1\), the separate formula \(\widetilde r(1)=F(1)>0\)
  is necessary and is correctly used. Errors are \(O(n^{-3})\), so
  the leading coefficient is \(15/64\).
- **Endpoint and floor decisions.** An explicit common bound is
  \[
  0<\tau_n-\varepsilon_n
  <(201/200)\tau_1=67/4500<1/5\qquad(n\ge1).
  \]
  Here \(\tau_1=2/135\) and
  \(\delta_n\le\tau_n/200\). This proves both floor formulas
  for \(a=1\) and \(a=1/5\) at every declared index. The approximation
  formula is correctly restricted to \(n\ge1\); extending it to zero
  when \(a=1/5\) would be false. The completed endpoint is the limit
  of \(16^{-n}F(n)\), and the positive source tail equals
  \(\tau_n-\varepsilon_n\).

### Fixed-precision strengthening

The later strengthening that retains the authentic source modulo any
**fixed** \(2^L\) also passes algebraic review. For
\(g_k\in2^{2k+L}\mathbb Z_{(2)}\), the correction satisfies

\[
G(0)=0,\qquad G(t)\in2^{L+2}\mathbb Z_2,
\qquad
v_2(G(t)-G(s))\ge v_2(t-s)+L+2.
\]

Thus adding \(G\) to the authentic isometry preserves its isometry
and zero value. Both the interpolation and its recurrence difference
retain the claimed finite-precision congruences at every
\(t\in\mathbb Z_2\). The same real approximation proves the previous
positivity and floor conclusions. This review imports the authentic
analytic interpolation and its zero pin from the named DSI source; it
does not replace that source proof by finite congruences.

The quantifier order \(\forall L\,\exists\widetilde r_{L,a}\) is
essential. No single changed source is asserted to agree at every
precision. These controls change the forcing and allow freely chosen
odd-denominator heights. They do not contradict the literal four-pole,
zero-seeded target.

## 2. Uniform excitation and readout: universal algebraic review

The source polynomial expansions in SE-01 give the stated strict bounds.
Summing their geometric majorant gives SE-02. With
\(m=\lceil\log_4n\rceil\), one has
\(n^2\le16^m<16n^2\). The finite echo equals
\(R_n=16^mT_n-T_{n+m}\). Its lower estimate at \(n=4\) is
\(43/5120>1/128\), and that lower estimate increases thereafter;
the upper bound is strictly \(1/4\). Both declared response parameters
\(\theta=1\) and \(\theta=1/4\) stay on the increasing sine interval.

The reference orientation is correct:
\(\Delta=e(\theta U_{n+m})J\), so multiplying by \(\overline J\)
and dividing by \(|J|^2\) returns the stated phase. The perturbation
bound assumes an exact fixed reference \(J\), as the text specifies.
Recovering the carry also uses the real fractional correction; it is
not supplied for free by the echo. The delayed-index comparison is
valid: its injective sample set and the ordinary shell differ in at
most \(2m(2B)\) integer points.

The next-bit flip correctly follows from the inherited all-index
isometry, including index zero. The cofactor transport sign is correct.
The modular numerator and denominator reductions in SE-08 give the
claimed low nibble; both parity cases leave an even multiple of 8.
The final cofactor recurrence re-encodes the unknown carry, as the text
explicitly states.

**Seed qualification.** For \(n\ge1\), the low-nibble formula also
persists under every 2-integral rational seed perturbation, since
\(16^n\) times that seed vanishes modulo 16. The clock formula alone
does not identify the real zero seed. In the signed readout that
selection remains in the actual fractional cofactor. This is compatible
with the stated open-gate verdict.

The source-only filter cancellation in `CONTROLS.md` is also exact:
\(P(E)U_n(s)-P(E)U_n(0)=16^nP(16)s\). Clearing the four-pole
denominator and then taking finite differences does not restore the
homogeneous seed coordinate after it has been eliminated.

## 3. Finite executed checks, separate from proofs

The reviewer wrote fresh exact `fractions.Fraction` calculations rather
than calling the authors' finite audit implementations. Their results were:

| Check | Exact finite scope | Result |
|---|---|---|
| Source echo identity and \(1/128<R_n<1/4\) | \(4\le n\le512\), 509 indices | Passed |
| Low-nibble, low-two-bit, and carry-cofactor identities | \(0\le n\le512\), 513 indices | Passed |
| Delayed-shell symmetric-difference bound | \(4\le B\le512\), 509 shells | Passed |
| Next-bit loop residues | \(0\le n\le16\), \(0\le k\le8\), 153 pairs | Passed |
| Independently rounded Mahler coefficient prefixes | First 32 coefficients, each of \(a=1,1/5\) | Positive sources, errors, divisibilities, and floors passed |
| Prefix polynomial isometry and source-isometry checks | 190 pairs per endpoint, from integers \(-8,\ldots,8\) and \(1/3,5/7,2/5\) | Passed |
| Prefix backward telescoping identities | Three rational 2-adic arguments per endpoint, \(J=6\) with seven summands | Passed |

The Mahler checks use the finite prefix polynomials. They do not turn
a finite sample into a proof about the infinite analytic function; the
valuation argument in Section 1 supplies that proof. The fixed-\(L\)
strengthening was reviewed algebraically, without a new finite test run.

The explicit rounding grid used for a new coefficient of scale \(S\)
and tolerance \(\delta\) was
\(q=2\lceil S/\delta\rceil+1\), an odd denominator, followed by
nearest-integer rounding of the required coefficient times \(q/S\).
The first coefficient includes its specified unit offset. This makes
the finite construction reproducible without an existence oracle.

The earlier constructor winding checks are recorded in
`WINDING_PACKETS.md`. No repository-wide gate or external CI run is
claimed here.

## 4. Review provenance, corrections, and boundary

This is an additional derivation and implementation pass within the same
multi-agent session and model family. The reviewer saw the proposed
claims, shared the repository and historical sources, and used the same
Python rational-arithmetic library. It is not a blind independent
reasoner, a fresh external source family, or formal proof-kernel
verification. The separate scripts reduce shared implementation risk;
they do not remove shared mathematical provenance.

The reviewed source-excitation text has had its malformed inline math
delimiters repaired by the coordinating/translation pass. The reviewed
controls explicitly retain the \(n\ge1\) real approximation domain
and separate first-step positivity; both guards prevent an origin
error for endpoint \(1/5\). No unresolved mathematical correction
was identified in the audited claims. The seed qualification above
records an additional scope clarification, not a refutation.

The earned result is a stronger separation of source premises and a
uniformly conditioned source-response construction. The winding count
remains logarithmic and inherits the existing irrationality argument.
There is no newly proved positive lower shell density for the authentic
fourth-root event, no closure of the original real anti-locking target,
and no proof of pi normality.
