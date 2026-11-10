# Independent read-only audit: parity boundary certificate

Reviewed the current shared versions of:

- `observational_succ/parity_boundary_certificate.py`
- `tests/test_parity_boundary_certificate.py`
- `research/2026-11-09/cayley_source_observer/BOUNDARY_PROOFS.md`
- inherited `duck_bbp.py` and `SelectedOrbit` source-enclosure interfaces.

No edits were made to these files. Review method: direct derivation, separate
rational-orbit enumeration, high-precision trigonometric diagnostics, hostile
assumption deletion, and inspection of all boundary conventions.

## Verdict

**No blocking mathematical or enclosure-soundness defect was found in this
review.** The code's arithmetic boundaries match the required analytic bounds.
This is a scoped audit, not a formal verification or independent proof of the
BBP identity. Two documentation gaps should be closed before finalizing the
package; both are stated precisely below.

## 1. Rational sine enclosure

Let `T=terms`. The polynomial

`P(y)=sum_(j=0)^(T-1) (-1)^j y^(2j+1)/(2j+1)!`

is also the Taylor polynomial **through degree 2T**, since sine's degree-2T
coefficient is zero. Taylor's theorem with a derivative bound of one therefore
gives remainder at most `|y|^(2T+1)/(2T+1)!`. The code's use of order `2T+1`
is correct; it does not require a missing degree-2T term.

The authenticated source interval `[plo,phi]` encloses pi. Sorting
`2*t*[plo,phi]` handles the negative representative after reduction to
`[-1/2,1/2]`. Flooring the lower endpoint and ceiling the upper endpoint on a
dyadic grid preserve containment. Their midpoint `y` is within the radius of
the true argument. The additional radius payment is justified by sine's global
1-Lipschitz property. The runtime check `abs(y)<=22/7` gives the polynomial
remainder's compact bound; intersecting with `[-1,1]` is valid.

I separately checked the exact rational inequalities `plo>0` and
`phi+2^-16<22/7` for the fixed source enclosure. They show that the range guard
cannot fail merely due to outward rounding at any permitted `bits>=16` and
`|t|<=1/2`.

**Documentation gap A:** BOUNDARY_PROOFS currently says certified interval
arithmetic is required but does not yet include this actual rational
Taylor/rounding proof, including the degree-2T observation and pi-enclosure
dependency. The code is sound under the stated imported BBP identity, but the
user-facing proof certificate should contain the argument, not leave it only
in implementation comments.

The finite Fejer evaluator uses positive coefficients and all four endpoint
quotients `slo/plo`, `slo/phi`, `shi/plo`, `shi/phi`; this safely encloses
`sine/pi` even when the sine interval changes sign. Correlation between the two
uses of pi can only make the box enclosure conservative, not unsound.

## 2. Source intervals and Fejer payment

`PhaseEnclosure.digit()` compares unreduced floors of both real endpoints.
Thus an interval crossing a whole-turn seam, or spanning a full circle, cannot
be falsely certified merely because its reduced endpoints have the same digit.
The exact closed-endpoint convention is conservative and correct.

`SelectedOrbit.state(n)` is reduced modulo one; adding a certified Green-tail
interval yields an enclosure of the completed phase in a possibly seam-crossing
real chart. All subsequent operations are periodic, so it need not equal the
unwrapped completed lift. `common_horizon_enclosures()` starts from the actual
rational source prefix `P_L`; subtracting an integer deck value preserves exact
radix-16 consecutiveness modulo one. Widths grow by sixteen, as required.

The boundary upper count uses
`d(center,B)<=delta+radius`. If the true point lies in an open delta-strip,
this inequality follows from the distance function's 1-Lipschitz property.
The sign of the offset within the interval does not matter.

The derivative coefficient `L_H` is correct: summing the positive derivative
coefficients at zero gives `64K_H-512K_H^2/(H+1)`. Hence both the Lipschitz
payment `L_H*radius` and its cap at two are justified. The whole error can also
be capped at two, because the true parity mean and the true Fejer mean belong
to `[-1,1]`.

**Documentation gap B:** CBO-B03 states its certificate using a lower endpoint
`a<=y<=a+epsilon`, while the implementation uses a midpoint and radius. The
proof only needs the more general hypothesis `|y-a|<=epsilon`, so the midpoint
version is valid. State that general condition, or explicitly include the
midpoint/radius corollary, to align the theorem with the executable witness.

The average common-horizon widths, the `O(H/A^3)` unclipped comparison, and the
clipped `log(1+H_A)=o(A)` comparison were algebraically checked. Those are paid
transport costs. The proof does not turn them into cancellation estimates.

## 3. Exact open-ball recursion

For folded orbit `u_n=8*t_n mod1`, let `a=nu(I_j)` and `b=nu(J_j)`. Exact
consecutiveness gives

`nu(R^-1 I_j)=a+(1_(I_j)(u_N)-1_(I_j)(u_0))/N`.

The two chosen inverse fibers are exactly `I_(j+1),J_(j+1)`; the code's
remaining preimage count includes all fourteen other fibers. Therefore

`b_(j+1)=(b_j+q_j)/2+endpoint-other_fourteen`

has the correct sign on both added terms. Iterating the upper bound
`endpoint<=1/N` gives exactly `2(1-2^-J)/N`. The code neither drops endpoints
nor changes an equality to a false equality after removing the fourteen
fibers.

The open convention is necessary at radius `1/4`: closed arcs centered at zero
and one-half both contain one-quarter and three-quarters. A point mass there
would give a sum of masses two. The code uses strict inequalities, and the
independent enumeration included these exact dyadic endpoints.

A useful assumption-deletion control: for Haar, the exact scaling is
`b_(j+1)=b_j/16`, not `b_j/2`; the difference is precisely the fourteen-fiber
mass. Retaining it in the identity while discarding only its nonnegative value
in an upper bound is correct.

## 4. Strong stationary half-shift gate, CBO-B05

The proof's major steps survive direct audit:

1. Consecutive segments of length A have continuous-observer stationarity error
   at most `2||g||_infinity/A`, even when their starting points depend on A.
2. Any weak limit is radix-16 invariant. Its folded law has every odd Fourier
   coefficient zero by the explicit fixed-pin hypothesis.
3. Fourier uniqueness implies folded half-translation invariance.
4. Radix invariance and half-translation invariance give the small-ball
   contraction factor one-half at each scale factor sixteen.
5. Iterating gives the stated fourth-root bound. The constants in the
   transfer back to the sixteen original cuts are conservative and valid.
6. Closed-set Portmanteau bounds plus monotonicity give zero mass for any
   shrinking sequence of strips, with no claimed convergence rate.
7. The limits have no mass at parity jumps; half-translation oddness then
   gives zero parity mean. The discontinuity passage is paid explicitly.

The stationarity premise is load-bearing. The measure
`mu=(delta_0+delta_(1/16))/2` kills every indicated odd parity pin but puts all
mass on digit boundaries. It fails radix-16 invariance. Thus the result would
be false if someone later applied it to arbitrary clouds of pin values rather
than consecutive orbit laws or a separately justified stationary limit.

The `{0,1}` Bernoulli-digit model really is a strictly non-Haar invariant law
satisfying the entire fixed parity-pin hypothesis: averaging its first digit
kills the factor for every odd frequency. Folding by eight gives the `{0,8}`
Bernoulli law; at `r=(8/15)*16^-j` its mass near zero is `2^-j`, so the claimed
fourth-root scaling is also correct.

The `{2,4}` nonperiodic-digit control has parity constantly one and uniformly
positive distance from every digit boundary. It correctly refutes inferring
parity from boundary tightness alone. The coherent wrong seed `-pi/16` also
survives as required. No new zero-seed estimate is smuggled into these controls.

## 5. Independent probes executed

A separate temporary script checked:

| Probe | Cases | Result | Authority |
|---|---:|---|---|
| Sine enclosures, denominators 1,2,4,8,16,31,32,33,64,127; negative and positive phases; Taylor terms 1,2,4,8,16; bits=16 | 3,230 | PASS | 100-digit numerical diagnostic, not a universal proof |
| Exact orbit recursion, every rational starting numerator with denominator 1 through 65; length 7 and depth 4 | 2,145 | PASS | Exact rational finite identities and bound checks |
| Fejer budgets over ten cutoffs, seven ordinary/seam/jump centers, five radii, five possible points in each enclosure | 1,750 | PASS | 100-digit numerical diagnostic of the exact budgets |

The probe used no implementation tolerances for rational recursion. Sine and
Fejer comparisons allowed only `1e-90` for the independent mpmath diagnostic.
Their universal authority remains the explicit analytic proof above. All
finite checks passed; this audit did not modify the shared implementation.
