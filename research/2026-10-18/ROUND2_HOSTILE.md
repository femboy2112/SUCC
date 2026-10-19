# Hostile review of the whole-residual prime inverse bound

Date: 2026-10-18. Target checkout: `SUCC-round2-signed`.
Reviewer: the operator stream, separately authored within the same model
family and shared project provenance. This is not a blind source witness.
No target files were changed and no full source calculation was rerun.

**Verdict:** the source decomposition, all-high Bessel argument, form-core
passage, ambient inverse inequality, and correlated-error accounting
survive this review. One theorem-quantifier repair was requested and
verified as applied: Section 4 now fixes a parity sector when choosing
kappa. The actual calculation already separates parity sectors.
With that explicit scope, the new enclosure is a valid paper result with exact rational
instance evidence. It remains a negative sufficient lower enclosure,
not a proof of source positivity or a negative-energy source witness.

## 1. Source and domain checks

The original screw function was checked directly against
[Suzuki, equation (1.3)](https://arxiv.org/html/2606.09096v3).
Distributionally differentiating its channels with the sign `-g''`
gives the stated contact, prime translates, rank-two pole, and the
Gamma rung `4/d I - E_(d/2)`. The prime coefficient is the original
`log(2)/sqrt(2)`; the window difference length is 1, so only the n=2
hinge occurs. This is a direct normalization check, not validation
of every theorem in the source paper or every inherited interval routine.

Integration by parts sends derivative orthogonality to Legendre modes
0 through 4 into primitive orthogonality to polynomials of degree at
most 3. Even primitives consequently start at Legendre degree 4;
odd primitives start at degree 5. The parity swap under integration
is accounted for in the code's derivative-parity names.

The weighted closure argument is sound. For dilation
`F_r(x)=F(x/r)`, its Fourier transform is `r Fhat(r xi)`. For r near 1,
the inequality `m(xi/r) <= max(1,r^-2)m(xi)` gives uniformly bounded
dilation operators in `L2((1+m) dxi)`. Strong continuity follows first
on compact-frequency functions and then by density. Shrinking support
before convolution keeps mollifications inside the interval. Four
fixed interior bump-polynomials have a positive definite moment Gram;
their correction coefficients converge to zero because the moments
are L2-continuous. Reflection then gives parity-preserving cores.
Thus the claimed form completion is supported by an actual core
argument, rather than an extrapolation of finite matrices.

The code's clamped h satisfies both endpoint trace conditions, so its
zero extension is H2. The inherited H1 multiplier estimate
`m(xi)<=5|xi|` independently follows from
`16 xi²/[d(d²+4xi²)]<=4|xi|/d²` and `sum 4/d²<=5`.
It puts these trials in the full Gamma operator domain. Projecting
`H h` into the high space therefore defines a genuine L2 residual.

## 2. All-high inequality

For the normalized Legendre basis on the interval of length 1, the
Fourier transform of its ell-th vector is
`sqrt(2ell+1)(-i)^ell j_ell(xi/2)`. Cauchy–Schwarz on the entire allowed
Legendre tail gives the manuscript's pointwise Fourier bound. Applying
Plancherel on both frequency half-lines and changing xi=2z yields
the factor `2/pi` in the leakage integral. The multiplier at cutoff
256 is increasing in absolute frequency and lies below the infinite
positive multiplier, so no finite-spectrum positivity inference occurs.

The factorial coefficient formula agrees with the
[NIST spherical Bessel power series](https://dlmf.nist.gov/10.53.E1).
The ratio after the first omitted term is bounded by
`Z²/[2(K+2)(2ell+2K+5)]`, and decreases thereafter. The stated
geometric remainder therefore bounds the whole absolute tail. The
integral representation of spherical Bessel functions gives
`|j_ell(z)|<=z^ell/(2ell+1)!!`. Integrating the angular tail gives terms
`Z^(2ell+1)/(2ell+1)!!²`, whose ratios are bounded by
`Z²/(2L+3)²`. Including both parities beyond L is conservative.

For odd primitives, moments through degree 4 eliminate the first
two sinh terms. On |x|≤1/2 the remaining sinh series is at most
`2(1/4)^5/5!` in absolute value. Its negative rank-one contribution
is therefore bounded by `8(1/4)^10/(5!)²`, as used. The even sector
has zero sinh contribution. Retaining the exact prime mismatch after
subtracting the scalar prime budget is an algebraic identity and does
not spend the prime term twice.

The saved outward lower margins exceed the stated kappas by at least
`100390719483/10^15` and `221035947909/10^15`, in derivative odd/even
order. These are independent checks of the exported brackets, not a
fresh recomputation of the large Bessel rational sums. The separate
authoring stream's factorial replay and inherited recurrence share
the same analytic Bessel theorem and source constants.

## 3. Inverse and error checks

For a fixed parity sector, the closed high form satisfies D≥B_E.
For r in that sector,

`<r,D^-1 r> = sup_(v in form domain) [2 Re<r,v>-q(v)]`

is at most the same supremum over the whole ambient L2 space using B.
This proves the ambient `B^-1` upper bound even though the high
projection does not commute with the cutoff translation. The center
and two-edge blocks directly give the stated alpha and beta savings.

For arbitrary, fully correlated errors e_i, the estimate
`||sum z_i e_i||² <= (sum delta_i²)||z||²` is valid. Young's inequality
in the ambient inverse norm then pays the existing source errors once.
The saving terms use the nominal p_i, so no additional action error is
needed inside those terms. The translation uncertainty is different:
it concerns the exact source shift acting on the known nominal left
polynomial, and is separately charged by epsilon_i.

The geometry checks imply that R0 lies in the actual and nominal
right regions, C0 lies in both centers, and every point between
`x-b0` and `x-b` stays in the nominal left cell. The fundamental
theorem of calculus, followed by translation-invariant L2 integration,
therefore gives the derivative translation error used by the code.
Reverse Young with theta gives the full matrix lower `E_lower`.
No correlation assumption or positive-part clipping is required.

**Resolved scope repair.** The original Section 4 called D the
operator on all E, while kappa=153/500 had only been proved for odd
primitives. The theorem must fix a parity sigma and use E_sigma and
its restricted D, with the residuals in E_sigma. The nominal p_i and
errors can remain ambient vectors because the comparison uses B on
the full ambient space. Alternatively, the smaller kappa works on
full E. Actual code already treats the parity blocks separately.
The revised manuscript was read: it now fixes sigma, E_sigma and the
corresponding kappa, and expressly allows the nominal/error vectors
to remain ambient. No remaining material gap was found in the stated
paper argument within the review boundary below.

Three exact countercontrols distinguish the valid argument from
tempting false replacements:

1. If e_1=e_2=1 and z=(1,1), the squared combined error is 4, whereas
   the correlation-blind diagonal budget is 2. The manuscript's
   trace budget is 4 and survives.
2. For B=[[2,1],[1,2]] and E=span(e_1), the compressed inverse is 1/2
   while the compression of the ambient inverse is 2/3. Replacing the
   variational inequality by equality would fail.
3. Let A=[[1,1],[1,3/2]] and L=diag(-1,1). Then A is positive definite
   and A-L is positive semidefinite. But A-positive_part(L) has
   determinant -1/2. Spectral clipping of a signed lower matrix is
   therefore unsound; the implementation correctly avoids it.

## 4. Actual J8 and J24 receipts

An independent Fraction-only calculator parsed the saved receipt and
reconstructed alpha, beta, the translation penalty, E_lower, the
saving G, the gain `(1+eta)G`, and `new=old+gain`, checking every entry.
Both G and gain are positive definite by exact leading minors. Both
negative new matrices are positive definite by the same exact test,
so the new lower matrices themselves are negative definite.

The gain determinants, for display only, are approximately
`7.413909446436326e-10` (odd derivative) and
`3.208358533238546e-10` (even derivative). The comparisons establishing
their signs used exact rational arithmetic, not these decimals.
The three false-shortcut controls above also passed exact arithmetic.

Reviewed snapshot hashes:

| Artifact | SHA256 |
|---|---|
| `ROUND2_FULL_PRIME_J8.json` | `fcf50928078e512452f2a0c7d4d044eaa5ba69f29faba4877f92e7c222bd718d` |
| `full_prime_resolvent.py` | `9514a7e172e032f95bba39d2ceb1ab09e6fb4e8712df3c9382c307aedf27de7b` |
| Manuscript before parity clarification | `a77ff75722ffd52263ec5454be35802438850a63654ca706bded7f940fee564e` |

The subsequently completed J24/M192/P18 receipt received the same
independent exact reconstruction, including all translation and gain
identities. Both gains are positive definite, and both improved lower
matrices are negative definite. The gain determinant displays are
`5.894872420887756e-10` (odd derivative) and
`1.6825800057067465e-9` (even derivative). Again, signs were checked
as exact rational inequalities. Additional snapshot hashes:

| Artifact | SHA256 |
|---|---|
| `ROUND2_FULL_PRIME_J24.json` | `7bd25ee59e856836870b7fb856a873dd2e59e289b4630d9c9fa34d329502f04e` |
| Manuscript after parity clarification and J24 update | `87e2d22aa0afb880912fd2b8b4c12461e58cbd99194db913422b242f7e3f8c15` |

This check does not independently regenerate the fitted source
polynomials, the original finite signed energy intervals, or the
large all-high rational audit. Those remain linked inherited/replayed
ingredients with their own receipts. J24 source execution was not
repeated; its stored exact decomposition and matrix algebra were checked.
No kernel proof of the analysis is claimed. A
negative sufficient lower matrix settles neither actual source
positivity nor RH.
