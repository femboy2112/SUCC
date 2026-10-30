# Complementary review of the general-rank harmonic composition theorem

Reviewed Section5A / FC07 of `constants/CONSTANTS_AND_COMPOSITION.md`.
The precise reviewed SHA256 is in `receipts/general-composition-review.json`.
This is a complementary same-model proof review and separate implementation,
not an external independent referee or a Lean proof.

**Verdict: no substantive mathematical gap found.** For every fixed real
`a>0` and integer `k>=2`, the stated source-correct iid composition obeys

    E log(X_1+...+X_k)−E log X_1−(H_(2k−1)−1)
      >= (k−1)/(2k+1) * (1379/900) * a^4/(a+5)^6 >0.

It is an inequality for independent draws from the authentic positive source
law. It does not assert independence of actual BBP arithmetic times or imply
selected zero-seed Weyl cancellation.

## Independent reconstruction of the critical factors

Let τ be the declared native bounded rate law on[0,5], with variance
σ²=1379/900. The normalized mixture uses

    dν_a/dτ(t) = (a+t)^(-2) / E_τ (a+T)^(-2).

Since the denominator is at most a^(-2), this density is at least
`r²=[a/(a+5)]²`. Taking the minimum squared distance to a constant gives
`Var_ν(T)>=r² Var_τ(T)`. This argument does not incorrectly replace variance
by an uncentered second moment.

For iid T_i~ν_a and iid independent G_i~Gamma(2,1), put
`X_i=G_i/(a+T_i)` and `z_i=−log(a+T_i)`. Define

    F(z)=E_G log(Σ_i e^(z_i)G_i)−mean(z)−ψ(2).

After averaging over T, `E_T F(z)=E log S_k−E log X_1` by iid symmetry.
For each fixed T, subtracting mean(z) is the correct symmetric function;
it need not equal the conditional log increment relative to a specified X_1
before the final averaging.

The log-sum Hessian is `diag(p)−pp^T`. At every point of the segment from
mean(z) to z, coordinate range is at most log((a+5)/a), and
`p_i>=r w_i`, where `w_i=G_i/ΣG_j`. Thus, for every zero-sum direction d,

    d^T Hess(F) d
      = E_G Σ_(i<j) p_i p_j(d_i−d_j)²
      >= r² * 2/[k(2k+1)] * Σ_(i<j)(d_i−d_j)²
      = r² * 2/(2k+1) * Σ_i d_i².

The Dirichlet cross moment is exactly `E w_iw_j=2/[k(2k+1)]` for i≠j.
At the diagonal the gradient of F is zero. The integral Taylor remainder
therefore gives one half of the displayed curvature. Averaging centered
squares yields `(k−1) Var_ν(log(a+T))`. The independent-pair variance formula
and derivative `1/(a+t)>=1/(a+5)` imply

    Var_ν(log(a+T)) >= Var_ν(T)/(a+5)².

Multiplying these factors gives precisely
`(k−1)/(2k+1) * σ² a^4/(a+5)^6`. There is no missing k or factor2.
All differentiated log-sum derivatives needed here are bounded uniformly in
the Gamma variables, so expectation and differentiation are justified.

The asymptotic coefficient is also correct for each fixed k. The tilted rate
law converges to τ; z differs from its mean by centered `−T/a+O(a^-2)`;
the exact diagonal Hessian eigenvalue is2/(2k+1). A bounded third derivative
and bounded T support yield an O(a^-3) Taylor remainder, giving the stated
limit `σ²(k−1)/(2k+1)`. Uniformity for k growing with a is not asserted.

## Golden continuation

The previously established native interval `λ²<ℓ<λ` and strict concavity of
`x−x^k` suffice. Its endpoint difference is
`λ³−λ^k(1−λ^k)>=0`, because `λ^k<=λ²<1/2` and x(1−x) is increasing there.
For k=2 the endpoint values coincide and interior strict concavity still
makes the correction positive. For k>2 the upper endpoint is larger.
Hence FC07's all-rank golden correction is positive with the declared mark.
This does not supply an independent reason for choosing that mark in an
arbitrary observation system.

## Fresh checks and limits

`general_composition_review.py` imports no constants implementation. It
checks exact rational Dirichlet Hessian identities for k2..17; 60 pointwise
Hessian comparisons including a=1/100; and3 bounded-rate tilt/variance
comparisons. It separately calibrates9 fresh `(k,a)` cases using the positive
three-term source and the Frullani integral in logarithmic t-coordinates,
at70 and100 decimal digits. The two computations agree within1e-60.
The omitted integration tails have analytic bounds, but the quadrature
inside the interval is not certified: these9 rows are explicitly numerical
calibration, not universal or interval proof authority.

The all-a/all-k conclusion rests on the proof above. Pure Gamma with a
degenerate rate law has σ²=0 and the exact harmonic equality, as required;
nondegenerate native rate variance supplies the strict correction.
The same composition law is unchanged by switching the arithmetic seed to
−π/16, so the selected signed obstruction remains open.

Minor exposition feedback: F already includes the G expectation, so an
additional E_G before Hess(F) is redundant; and displaying `E_T F` as the
wanted log increment makes the symmetric centering explicit. Neither issue
changes the result. Any subsequent textual clarification must be distinguished
from the exact dossier hash reviewed in the receipt.

## Addendum: FC09 sharp mark classification

Reviewed the completed Section5B at dossier SHA256
`216d707e7d583c790a53f7e0f290c37fa72e06f0cb024040ab952b2f05d45ead`.
It also includes the two harmless FC07 clarifications above.
**No mathematical issue found.** The all-a sharpness statement is correctly
restricted to the continuous clock a>0, not claimed for native integer times.

For t=1/(1+η)∈(0,1), direct factorization gives

    (t−t^k)−(t²−t^(2k))
      =t(1−t)[1−Σ_(j=k−1)^(2k−2)t^j].

The sum is continuous and strictly increasing from0 to k; it has exactly one
unit-interval root of value1. For t at or below this root, strict concavity
of x−x^k ensures its value at every interior ℓ_a∈(t²,t) exceeds the lower
endpoint value. Equality of the endpoint values at the threshold causes no
failure of the **strict interior** inequality. Above the root, the upper
endpoint value is smaller, and ℓ_a→t as a↓0 provides finite positive-a
counterexamples. Thus the claimed iff is valid.

The k2 threshold is λ. At t=λ, the earlier proof gives the correct endpoint
sign for every k; strict monotonicity of the defining sum then gives every
smaller t. Therefore the simultaneous all-a/all-k criterion is precisely
η>=λ. This is a sharp threshold for the specified comparison family; it
does not assert that every arbitrary observation must use that mark.

`mark_classification_review.py` independently checks19 symbolic
factorizations and19 exact unit-interval root counts (k2..20). It then checks
18 fresh positive source cases at k4,6,9 and t1/2,3/5, and3 exact negative
small-a cases at k4,6,9. The negative cases use a=1/4096 and the full positive
three-term source formula. Raw rational excesses are retained in
`receipts/mark-classification-review.json`; all checks passed.
