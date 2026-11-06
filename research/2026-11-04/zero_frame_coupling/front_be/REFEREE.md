# Independent same-model referee pass

This front independently derived the indicated arguments before comparing the
other campaign proofs. Shared source and model provenance remain explicit;
this is not an external scholarly referee or kernel proof.

## Parent #506 and #504 audit

Read all files under `observer_relative_return/` and
`virtual_gauge_circle/`, with parent HEAD
`bc2d7b01b6b0a37cb79994e180758e98681aa68e`.

Reviewed SHA-256s:

- TWO_CLOCK_THEOREMS.md:
  `d90b19b07840d480f9498abf39d6c919bbb4d53fbeffbb571a2bb6b88d7ee8ab`.
- RECIPROCAL_CLOCK.md:
  `311953770b575361b523d12b46fe36887d0a832bfb4d47eb97a334163169d4b8`.
- SOURCE_JET_TRANSPORT.md:
  `78c26e2c3a740211b82081217f9f718e2cb62fc7443e98e933a380bf22092be9`.

OR-01/02 survive: exact affine iteration preserves the time labels, the fixed
lag changes Z by O(n^-2), and its fixed-h character discrepancy is summable.
The flat U(1) and frequency-twisted cocycles are different exact identities;
neither identifies the selected orbit's distribution.

OR-03's derivative is `ell q/(16x³)`, giving the endpoint factor
`8/(pi i ell q)` and magnitudes 8 and 1. The reverse triangle inequality
therefore gives 56 and 72 as the stated lower/upper numerators. Its errors
become o(1/q) on the required schedule because q²/A tends to zero.
For negative ell, conjugation supplies the same magnitude bounds.
OR-04's compact smooth **whole-window** argument is valid; maximizing over
subintervals reintroduces endpoints, now quantified in BE-02.

RC-01's reciprocal Jacobian integrates to one. The exact transformed interval
has length 3/4 and midpoint 5/8, giving phase `e(-5 ell q/256)` and sinc
argument `3 pi ell q/128`. Tuned q=128k zeros are correct continuum zeros;
the original dyadic/radix schedule is not thereby tuned. RC-04's transported
frequency is indispensable and correctly positioned.

**Finite-domain correction:** RC-02 literally states 'every integer A>=1'
while allowing signed ell. The finite response is undefined if A+ell<1.
Its statement must be read with `A>=max(1,1-ell)`, consistent with OR-03's
explicit valid-index qualification; the asymptotic estimates concern
sufficiently large A. The large-A theorem survives. The inherited file was
not edited; this additive audit records the qualification.

SJ-01/02's rational coefficients survive an independent formal-recurrence
oracle: use `z(x+1)-16z(x)=r_rad(x+1)` to solve successive Laurent coefficients,
without the parent's geometric-moment algorithm. The Vandermonde determinant
in SJ-03 has the stated sign and factors. Every fixed m has a valid uniform
remainder; no growing-m conclusion follows. SJ-04 is an exact source phase
identity and a termwise error bound for arbitrary bounded observer amplitudes.
It is seed-blind and does not estimate either unknown individual sum.

The #504 radial zero, sign change, exact return, and time-gauge formulas also
survive. The real logarithmic derivative has equal endpoint values; its
nonconstant test integral need not vanish. The radical extremum
`t=2-sqrt(2)` is consistent with the source's interior zero used in BE-03.

## Front A/D: positivity and divergent canonical jets survive

Reviewed front_ad/PROOFS.md SHA-256:
`ce152cb06897b167cbbc51f75baeec657c52fe10c5fbce729b851dd09cefbdeb`.

The source ratio `A(1-s)=4v(s)(16/(1-s)-1)/(1-2v(s)-v(s)²)` is correct.
Every coefficient of v(s) in positive degree is positive; the geometric
inverse in the denominator has nonnegative coefficients. Thus every b_k is
strictly positive. The alternating signs in the delay vector follow by
expanding `-(1-E)^k` and match the parent coefficients.

For residual positivity, the pointwise split is decisive. Above tau, the
radial density is positive and A minus its positive Taylor partial sum is
positive. Below tau, the radial density is negative, A is negative, and the
positive polynomial is subtracted, so their product is again positive. At
tau the original nonzero density remains. This proves every finite residual
positive, with no finite-test extrapolation.

The fixed-m asymptotic constant was independently computed in u=t^8:
`rho(1)/8=1/32`, so the first surviving beta moment contributes exactly
`(m+1)! b_(m+1)/32`. The original n^-2 forcing has no hidden extra factor 8.

Let tau=2-sqrt(2), sigma=1-tau^8. The principal eighth root maps |s|<1
away from the other denominator root 2+sqrt(2), so sigma is the only pole in
that disk. Directly,

`lim_(s->sigma)(sigma-s) A(1-s)
 =32(tau-1)(16-tau^8)/(tau(tau-(2+sqrt(2))))
 =8(16-tau^8)`.

Subtracting this pole leaves an analytic function on |s|<1, justifying the
Cauchy coefficient estimate for every sigma<R<1.

For the high difference, `rho(0)=-1/8` and the Jacobian contributes another
1/8, hence

`(1-E)^k Z_n = -Gamma(n+1/8)/64 * k^(-n-1/8)
              +O_n(k^(-n-1/4))`.

This agrees with AD-3's exponent `-a-1/8`, where a=n+1/8. Multiplying by
b_k and summing the geometrically increasing terms adds exactly the factor
`1/(1-sigma)` to the last term. The resulting constant
`K Gamma(a)/(64 sigma(1-sigma))` is correct. Thus the noncommutation of
fixed-m large-n and fixed-n large-m limits is proved, not a fitted trend.

The finite shift pole obstruction, weighted-residue cohomology, seed gcd,
1/5 resonance, and literal-carry observability formulas also check. These
identify sources or exclude specified substitution operators; they do not
bound the authentic carry-word visit counts.

## Front C/F: maximal many-lag Bessel theorem survives

Reviewed front_cf/PROOFS.md SHA-256:
`d5c2f9e1a3d4d973772f53b30e539365f685bd69f6bab5aff6525950e92f24fe`.

CF-1's derivative constants are the same independently derived rational-tap
bounds audited in #505. On the enlarged interval [A,3A], including the final
telescoping endpoint, they give
`d Lambda/(864A)<=theta_n<=d Lambda/(8A)<=1/8`.
The reciprocal difference denominator obeys
`|b|<=1/(4 theta_min)` and total variation
`<=1/(2 pi theta_min)`, so two endpoints plus variation are strictly below
`1/theta_min`. Thus 864 is a valid off-diagonal constant, and the two sides
of a Gram row give the displayed 1728 harmonic-sum constant.

Each lag can choose its own maximizing interval: intersections of two such
intervals are still empty or contiguous, so the same bound applies. The
angular factors form one common unit-modulus vector and cancel out of the
Gram. Dual Bessel therefore proves the stated actual-source maximal many-lag
saving, while its proof remains angular-blind. Choosing L=floor(log³ A) is
allowed eventually and proves some delayed coefficient is o(1/log A); it
cannot select lag zero.

CF-2 correctly distinguishes a common unitary gauge from a different
compensation for each column. The latter makes all columns identical and
changes the Gram to rank one; it cannot retain the former Bessel gain.

CF-3's coherent counterseed satisfies exactly `a_n b_n=e(-H Delta_d T_n)`.
The source tail decrement gives `|E(ab)-1|<=pi d Lambda/(16A)`.
Its two marginal means have order 1/Lambda by the unequal endpoint terms,
so the covariance tends to one with the stated errors. This is a same-forcing
changed-seed falsifier of marginal-decoupling, not of the original source.
The literal carry equations correctly retain the missing realized-cell counts.

CF-4's compensated coefficient is `7/512-18/512=-11/512` at order n^-3.
The two-way sharp interval clipping and the summable fixed-h tail comparison
justify its bound, with seed-independent constants. This transports unknown
means; the proof does not claim their cancellation.

All reviewed original zero-seed normality and signed-cancellation claims
remain OPEN. No imported proof authority was raised by these audits.

## Subsequent joint-order A/D addendum

The later uniform estimate
`epsilon_m(n)<=C sigma^-m[B(n+1/8,m+2)+256^-n]`
was independently checked. Subtracting the interior pole leaves an analytic
remainder on |s|<1. On t>=1/2, the fixed remainder radius 511/512 exceeds
`s<=255/256`; multiplying by rho cancels the pole at t=tau and yields a
uniform `C sigma^-m s^(m+1)` bound. On t<=1/2 the original density's t^-8
factor integrates to O(256^-n) for every n>=1, and the finite Taylor sum is
O(sigma^-m). These two pieces give the stated beta bound with one absolute
constant. At m=n, `B(n+1/8,n+2)<=(64/9)4^-n`; hence the exponentially small
residual is valid, with n steps of future observation and coefficient norm
Theta((2/sigma)^n). It does not contradict fixed-n divergence or BE-03's
fixed-stencil obstruction. BE-04 records the surviving source multiplier's
explicit variation cost.
