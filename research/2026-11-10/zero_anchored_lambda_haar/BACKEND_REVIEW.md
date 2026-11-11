# Independent finite-backend review

**Status: OBSERVED FINITE adversarial replay; all four identified attack families
are rejected by the repaired implementation.** This review is from the compiler
subagent, using a separate arithmetic inspection and hostile input construction.
It is same-model review, not external refereeing or formal verification.

Reviewed implementation:
`observational_succ/zero_anchored_haar.py`.

SHA-256 at replay:
`bd86fa1909f61f73948287762ac987449ecc31b9fcd680666550a7bbd4bac6f4`.

No implementation file was edited during this final review. The final replay was
a single Python process, exited successfully, and printed
`ALL_TARGETED_ATTACK_REPLAYS_REJECTED` after checking every case below. It did not
rerun the full suite or claim an infinite mathematical conclusion.

## 1. Duplicate digit-character frequencies

The original implementation allowed a tuple such as `(8,8)`. Its dictionary
merged the repeated key while its accumulation loop visited that key twice.
For `certified_phase_grid(0,6,depth=3)`, the genuine degree-zero parity coefficient
is exactly `-1/5`. The duplicate request returned `-2/5`, with advertised error
zero. This was a false exact output on an authentic source window.

**Current replay:** the ordinary `(8,)` request still returns exactly `-1/5`.
The `(8,8)` request raises `ValueError: duplicate digit characters are not
allowed`.

## 2. Source-verification bypass and false orbit bounds

Construct a cyclic de Bruijn word of order two over 16 symbols, of length 256.
For each symbol d, substitute the phase-grid point `d*q/16`, and append the first
point as a 257th entry. This artificial table is not the shift orbit required by
the theorem. Its first 256 points have the uniform 16-grid empirical law and
exact interval Wasserstein distance `1/32` from Lebesgue measure.

At degree 9, all the formal Pascal-character coefficients computed from that
table vanish: each current digit is paired equally with each following symbol.
The former public `verify=False` path therefore yielded the purported upper bound

```text
135792617 / 6039797760 ≈ 0.02248297416501575,
```

which is strictly less than the actual `1/32 = 0.03125`. This was a false
mathematical bound, beyond simply mislabeling the source.

**Current replay:** `verify_phase_grid(fake)` returns `False`. Both public
functions reject the removed `verify=False` keyword with `TypeError`. Calling
`certified_pascal_characters(fake,9)` or `pascal_haar_upper(fake,9)` raises
`ValueError: invalid source phase certificate`. The independently computed
hostile-law distance remains exactly `1/32`.

The hostile table can be reproduced with this generator:

```python
from dataclasses import replace
from observational_succ.zero_anchored_haar import certified_phase_grid

a, word = [0] * 33, []
def db(t, p):
    if t > 2:
        if 2 % p == 0:
            word.extend(a[1:p+1])
    else:
        a[t] = a[t-p]
        db(t+1, p)
        for j in range(a[t-p]+1, 16):
            a[t] = j
            db(t+1, t)
db(1, 1)
c = certified_phase_grid(0, 257, depth=8)
fake = replace(c, points=tuple(
    d * (c.denominator // 16) for d in word + [word[0]]))
```

## 3. Forged character arrays and negative errors

The former upper-bound API accepted caller-supplied `PascalCharacter` arrays
and an unrelated count. Zeroing the coefficients could create arbitrarily
optimistic bounds without source evidence. Setting every degree-one
`modulus_error` to `-100` produced a negative claimed W₁ upper bound,
`-15299111/4800`, in the original reproduction.

**Current replay:** creating a replacement character with negative error raises
`ValueError: eight exact coefficients and a nonnegative exact error required`.
Passing a complete, structurally well-formed all-zero coefficient array to
`pascal_haar_upper` also raises `ValueError`; the API now requires an authenticated
`PhaseGridCertificate` and a degree. It recomputes the consecutive sample count
and the full character family together. No supplied array is treated as proof.

## 4. Numeric equality hiding wrong stored types

The original `verify_phase_grid` relied on dataclass equality against a rebuilt
certificate. A short certificate with integer-valued floats substituted for
`horizon`, `integer_lower`, and `integer_upper` compared equal and was accepted.
This violated the promised exact integer certificate format.

**Current replay:** replacing those fields with equal-valued floats makes
`verify_phase_grid` return `False`, and the certified defect API raises
`ValueError`. Replacing the integer point tuple by equal-valued `Fraction`
coordinates also makes verification return `False`.

The associated endpoint check was replayed as well: `finite_verdict((0.0,0.0))`
and `finite_verdict((False,False))` both raise `ValueError: two exact Fraction
endpoints are required`. The function documents that its classification is
conditional on the supplied enclosure, not proof of that enclosure's provenance.

## Mathematical scope reviewed

The underlying finite identities survived this review:

- The common-horizon integer enclosure accounts for every flooring loss and the
  inherited positive source-tail budget.
- Certifying a full hexadecimal grid cell fixes the leading digit and avoids an
  unrecorded interval/circle seam crossing. Both the empirical law and its
  conditional-digit average move by at most `1/q`, giving the stated `2/q`
  defect error.
- Current digit `d_n` is paired with the following phase `z_(n+1)`, as required.
- Bernstein derivatives satisfy `|B'_(m,j)|≤m`, supporting the stated `m/q`
  observation error.
- The signed-CDF overlap identity uses the correct equal-block normalization.

These are finite correctness findings and paper-proof checks within the stated
source and interval conventions. They do not prove decay of the authentic
statistical defect or the requested all-scale contraction inequality.
