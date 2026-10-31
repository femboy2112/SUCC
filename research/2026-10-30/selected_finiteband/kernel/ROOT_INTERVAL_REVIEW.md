# Complementary review of the root interval implementation

Reviewed `../certified_band.py`, SHA256
`ae4349d8fee04b3da04351202f48ad2cde68daac4ec59b991c652be43c0cd947`.
This is a same-model extra derivation and implementation check, not an external
referee or formal verification.

**Verdict: no unsound enclosure found in the reviewed code.**

1. The BBP pi interval uses `count=floor(bits/4)+1` positive terms. Each integer
   floor loses less than one fixed unit. The omitted positive tail is at most
   `16^(1-count) r(count+1)/15`; the code's `tail_units` has exactly this scale
   and verifies it is below one. Hence its `count+1` upper correction is valid.
2. Modulo reduction applies one common integer lift to both endpoints. If an
   interval crosses a seam it remains an interval in a real lift, and periodic
   trigonometric evaluation is valid. The source tail enclosure has independent
   outward rounding per term plus the correct geometric remainder.
3. For `|angle|<4`, degree126 cosine and degree127 sine Taylor remainders have
   absolute bounds `4^127/127!` and `4^128/128!`. The checked first bound is below
   one 128-bit fixed unit; the second is smaller by a factor `4/128`. Interval
   multiplication may overestimate correlated powers but cannot omit them.
4. In `unit_powers`, let the true complex generator `z` have modulus one, the
   numerical center be `z_c` with error at most `R/S`, and the old power-center
   error be `E/S`. Product error is bounded by
   `E/S+R/S+ER/S²`, using `|old center|<=1+E/S`. Flooring two coordinates adds
   Euclidean error less than `sqrt(2)/S`, safely rounded to `2/S`. Thus the
   recurrence `E_next=E+R+ceil(ER/S)+2` is valid. It is essential that the
   mathematical generator is a unit complex phase; this is proved by `trig`'s
   intended `cos+isin` target, not by its interval rectangle.
5. Squared real/imaginary sum intervals are outward rounded before positive
   Fejer weights are applied. All weighting denominators are positive. The
   final decimal formatting uses directed integer floor/ceiling, including
   negative endpoints.

`root_interval_review.py` executed successfully (exit 0), recording
`root_interval_review.json`:

- 100 exact rational checks of interval operations.
- Four independent rational Machin pi enclosures, at 97,193,389,521 bits,
  strictly inside the BBP enclosures.
- 4,004 exact rational complex-power checks on four non-axis rational points
  of the unit circle, through exponent1,001. These use integer Gaussian powers,
  so this part does not rely on floating-point phase comparisons.
- Four exact trigonometric axis cases and six 120-digit rational-angle checks.
- Five independent 48-term rational Green enclosures inside the root intervals.
- 53 exact original-source recurrence states inside the selected phase lifts.
- Four fresh finite energy enclosures checked using a separate 120-digit
  direct frequency implementation (`N=11,23`, `H=7,19`).

The root module is imported as the implementation **under test**; the reference
Machin bounds, four signed poles, rational powers and direct phases do not call
its arithmetic helpers. Finite testing does not formally certify every input.
The proof of the algorithm's intervals is the preceding audit.

Reproduce from repository root:

```sh
/media/leah/SPANKBANK/SUCCYBOI/SUCC-zero-dispersion/.venv/bin/python research/2026-10-30/selected_finiteband/kernel/root_interval_review.py
```

## Complementary Stoneham/low-slip paper review

Read `../cylinders/CYLINDERS_AND_STONEHAM.md` independently after constructing
K01--K04. The C3 stage has `q=c^(p-1)` points and multiplicity `c(c-1)`:
`ord_(c^p)(16)=c^(p-1)` and a birth numerator congruent to one modulo c give
exactly the required grid. The finite Fourier grid bound is valid: writing
`v=H/q` and `k=floor((H-1)/q)`, its remainder is controlled by
`v²-2kv+k²+k=(v-k)²+k>=0`. Replacing each incomplete stage by its full
multiplicity grid is legitimate by Fejer nonnegativity, and the aggregate
grid cardinality is `c^(P+1)-c<cN`. The summed future tail is exactly
`sum_p(1-16^(-c^p))/(15c^p)<1/[15(c-1)]`; multiplying by twice the kernel
Lipschitz constant gives the displayed `4pi(H²-1)/[45(c-1)N]`.

C1's fixed-point neighborhoods use the strict `17 epsilon<1` no-wrap gate;
the special center zero is split by its two digit sides and both are preserved
on consecutive good positions. C1b's two extra digits are sufficient.
C2's period-two phases have distance `1/17`, so the pair count is precisely
`(H+F_H(1/17))/2` for even N, while every sufficiently late lag-one position
slips. This is a valid counterexample to the source-blind implication from
positive lag-slip density to small full pair energy.

No defect was found in these scoped proofs. They do not supply the missing
authentic zero-seed finite-band upper bound.
