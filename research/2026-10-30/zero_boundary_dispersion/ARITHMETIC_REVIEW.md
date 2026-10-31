# Complementary arithmetic review

Reviewer: a separate agent in the same model/context family. This is a
complementary derivation and implementation check, **not** an independent
external referee or kernel proof. Parent403 remains
`5f350af7808532e55d74e80c948c02bb385c6e70`.

**Verdict:** no substantive defect found in CT-01, CT-07 or CT-08 under their
stated hypotheses. The exact cylinder argument also checks. One minor
clarification was requested and adopted: CT8's interval can be empty, and
its length is then0. No selected signed saving follows from these results.

## Independently reconstructed arguments

For CT-01, write the filtered value as M U_n+R. If D=den(U_n), Q is the
LCM of the new forcing denominators and V is the filtered denominator,
then V divides DQ and D/gcd(D,M) divides VQ. This establishes the finite
sandwich D/(|M|Q)≤V≤DQ without any distribution hypothesis. Prime valuations
prove the consecutive-interval LCM divisibility: powers above log_p(s) each
contribute one to the binomial valuation until the maximum interval
valuation is reached; lower levels contribute nonnegatively. With s=8d,
the logarithmic cost is O(d log((n+d)/d)+d). It is o(n) for every d=o(n),
including d much larger than n/log n. The coefficient-height hypothesis
likewise makes log|M|=o(n). Inherited CG01 then yields the claimed rate6.
The zero-filter-at16 case is expressly excluded from this branch.

For CT-07, ordinary additive characters contribute p-th roots and all
multiplicative characters contribute (p^f−1)-th roots. Their complete
character-value field is Q(zeta_(p(p^f−1))). A primitive root of odd order D
coprime to p belongs to it exactly when D divides p^f−1: adjoining any
missing odd prime power strictly increases the cyclotomic degree. Thus the
least allowed f is ord_D(p). This field-membership equivalence does not
construct a particular Gauss sum equal to the selected cofiber. Extra
2-primary roots and the declared Tate square-root normalization do not alter
the odd-order obstruction. Arbitrary external coefficient fields or roots
are outside the theorem, as the dossier states. Since deleting one primary
factor costs at most log(8n), the inherited exponential order gives the
displayed extension-degree lower bound, uniformly in the removed prime.

For CT-08, each nonzero coefficient of Q(E)r(n+1) contributes four distinct
simple poles. The four fractional pole classes are different, and shifting
time by integers produces no collisions. The reduced rational function
therefore has denominator degree4s. Its nonzero fixed resultant bounds all
integer evaluation gcds, giving Θ(n^(4s)). A fixed polynomial and its fixed
support count are essential here.

CT8 follows by bounding the possible integer wrap by17delta+|f_j|<1.
The finite dyadic shadows retain every odd-primary coordinate because their
seed differences have only power-of-two denominators; eventual circle
aliasing is preserved. Their finite coherence does not refute normality of
rational translates. These controls expose information loss in the proposed
finite-window arithmetic data, not a counterexample to authentic seed0.

## Executed separate checks

[The exact review probe](receipts/arithmetic-review-probe.py) imports none of
the CRT implementation. It uses direct unrolled BBP prefixes, a combined
rational source, cyclotomic-degree comparisons and SymPy multiplicative
orders as distinct checks. The [raw output](receipts/arithmetic-review-calibration.log)
and [command metadata](receipts/arithmetic-review-calibration.json) record:

- 1,260 exact short-interval LCM divisibility checks, including starts10^6;
- 26 moving-filter identities and denominator sandwiches at fresh indices;
- 1,024 cyclotomic-degree checks of the odd-order inclusion criterion;
- all five recorded cofiber orders and minimum extension degrees, independently
  reproduced using direct prefixes and `n_order`;
- three fresh annihilator polynomials, with reduced denominator degrees12,8,4.

The p1033 and p1061 minimum-degree coincidence is reproduced exactly; it
remains a finite observation. The asymptotic rate6 is inherited paper
authority, not established by these finite cases.

## Reviewed input hashes

SHA256 of the final reviewed inputs:

| Path relative to this directory | SHA256 |
|---|---|
| `crt/CRT_DOSSIER.md` | `89ff64ed17d069420a309360b62cfc66ac26fd393f678ebf8723fcbdaa7d86b2` |
| `crt/crt_probe.py` | `7f8d15e6fbc625e9625aae8f8ad23d2912692c5e8bdb08511e83e5cbae5a9dc2` |
| `crt/character_field_probe.py` | `c40a5e726f788284837d19f3d3222c9788f822c97feb1b3e8416620da384da83` |
| `crt/independent_oracle.py` | `5077b22919cef73597251a0efbd356146472a81dad7d450a587fbd878e73bf57` |
| `../arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md` | `c707cf382ba098f2895d71529f065d832e212b9f24529090896da9df0f8dd7b2` |

The declared theorem scopes survived this review. SC-06, positive-density
selected fixed-frequency dispersion, π normality and RH remain open.
