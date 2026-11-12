# Separate audit of the source-bound signed pi filter

**2026-11-12; constructor bearing reviewing the root's separate implementation.**
This is a same-model, separately tasked proof and implementation audit, not
an external referee or an independent mathematical source. The independent
replay below uses a different numerical representation and does not import
`pi_filters.py`.

## Verdict

The displayed statements PF1-PF8 in `PI_FILTERS.md` are sound within their
stated domains. The original source is `x=pi/16`; the shell indices are
`B<=n<2B`; source tails are retained; rounding error is amplified correctly;
and the finite counts do not establish uniform R0. Every one of the **18
published count vectors** and its three rational fields was independently
reproduced through source index **2181**.

One minor verifier schema defect was found: Python dictionary equality
identifies `True` with `1` and an integer with an equal-valued float. The
initial `verify_receipt` therefore accepted those two malformed output-field
mutations. Neither mutation changes the mathematical value or forges a
stronger bound, but they bypass the intended exact-integer receipt schema.
The root was informed to use type-sensitive canonical comparison or explicit
recursive schema checks. This finding is separate from the proof verdict.

## 1. Source identity, inequality and indexing

The four signed poles combine exactly into

\[
r(n)=\frac{120n^2-89n+16}
 {(2n-1)(4n-1)(8n-7)(8n-3)}.
\]

This was checked by clearing polynomial denominators, not only by evaluating
finite values. With `t=n-1`, the original four-pole common numerator is
`376+1208t+960t^2`, exactly eight times `47+151t+120t^2`;
its common denominator is eight times the new denominator.

Write `D=(2n-1)(4n-1)(8n-7)(8n-3)` and `N=120n^2-89n+16`.
In `t=n-1>=0`, independent polynomial arithmetic gives

\[
47D-15n^2N
=5443t+26429t^2+42263t^3+22264t^4\ge0.
\]

The numerator `47+151t+120t^2` and every denominator factor are positive.
Thus `0<r(n)<=47/(15n^2)` holds for **all integers n>=1**, with equality
in the upper bound at `n=1`. The geometric sum then gives

\[
0<T_n=\sum_{j\ge1}16^{-j}r(n+j)
\le\frac{47}{225(n+1)^2},\qquad n\ge0.
\]

The recurrence has `U_1=47/15`; the completed value is `Y_1=pi`, so the
normalization is indeed `Y_n=16^n(pi/16)`, not `16^n pi`. The identity
with geometric pi is the repository's imported BBP theorem. The new
experiment computes no supplied pi digits and does not re-prove that import.

## 2. Signed minorant and the tail payment

For `d(t)=dist(t,Z)`, the lower inequality
`8d(t)^2<=1-cos(2pi t)` follows from the sine chord on `[0,pi/2]`.
The upper inequality is also valid. Since `d(x)+d(y)<=1`,
`|d(x)^2-d(y)^2|<=d_T(x,y)<=|x-y|` holds across circular seams as well.

The proposed cell weight is the actual infimum on the **closed** cell,
including odd values of `q`. It is nonnegative, so discarding unresolved
indices is sound. Replacing raw `U_n` by completed `Y_n` costs at most
`8T_n`, not zero. On the shell the average payment is bounded by
`376/[225(B+1)^2]`. Clipping a negative result at zero uses the unconditional
nonnegativity of `1-Re W_B(1)`. No missing factor of 16, B, pi or 2 was found.

The equivalence qualification near PF8 is warranted for **exact complete
counts**: the upper cosine bound converts R0 to a positive mean square
distance; the tail difference tends to zero; and the uniform cell error
`8/q` can be made smaller than that fixed saving by choosing one sufficiently
large fixed `q`. The reverse implication is PF5. Thus this is an instrument
for R0, not an independently easier hypothesis smuggled in as a new theorem.

## 3. Circular interval proof and a falsified precision mutant

An interval represented modulo one still admits a real lift
`U_n=a_n/S+e+k`, with `0<=e<=w_n/S`. Multiplication by 16 sends the error
to `16e`; floor rounding adds a number in `[0,1/S)`. Modular reduction of
the lower endpoint removes only an integer lift, so PF6 preserves enclosure.
The recurrence `w_n<=16w_(n-1)+1` proves PF7. Keeping `4N+g` scale bits
pays for all amplification through index N. These are growing integers,
not a constant-space numerical claim.

The cell classifier's equal **unwrapped endpoint** floors are a sufficient
condition for unique membership in a half-open cell. Wraparound or an exact
right endpoint can cause a conservative unresolved result. It cannot assign
a wrapped interval to an incorrectly certified cell.

An independently implemented deliberate mutant replaced
`w_n=16w_(n-1)+rounding_bit` with `w_n=rounding_bit`. With scale 256 it
already failed at **n=2**: lower endpoint 65, asserted width 1, actual scaled
circular offset `9281/4095>1`. This supplies a concrete negative control for
the load-bearing amplification rule.

## 4. Independent full replay of all 18 finite results

The replay used the unwrapped rational recurrence
`U_n=16 U_(n-1)+4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`
in Python `Fraction`. It did not use fixed-point intervals, the combined
rational forcing formula, pi digits, or the production module.

For each shell index, the exact cell was computed by
`floor(q*U_n) mod q`. The following were checked separately for all six
shells and all three resolutions:

- Every entire count vector equals its published vector.
- The sum of each vector equals B.
- The exact raw rational lower sum equals `raw_minorant`.
- The independent rational `376/[225(B+1)^2]` equals `tail_payment`.
- The clipped exact difference equals `signed_gap_lower`.

**Observed:** all 18 comparisons in every category succeeded, through
index 2181. There was no unresolved mass in the published experiment.

The essential independently executed replay was:

```python
from fractions import Fraction as F
import json
from pathlib import Path

receipt = json.loads(Path("PI_RESULTS.json").read_text())
shells, qs = receipt["shells"], receipt["resolutions"]
counts = {(b, q): [0] * q for b in shells for q in qs}
u = F(0)
for n in range(1, 2 * max(shells)):
    r = F(4,8*n-7) - F(2,8*n-4) - F(1,8*n-3) - F(1,8*n-2)
    u = 16 * u + r
    for b in shells:
        if b <= n < 2*b:
            for q in qs:
                counts[b, q][(q*u.numerator // u.denominator) % q] += 1
for row in receipt["entries"]:
    b, q = row["shell"], row["q"]
    vector = counts[b, q]
    raw = F(8 * sum(c * min(a, q-a-1)**2
                    for a, c in enumerate(vector)), b*q*q)
    payment = F(376, 225*(b+1)**2)
    assert vector == row["counts"] and sum(vector) == b
    assert raw == F(row["raw_minorant"])
    assert payment == F(row["tail_payment"])
    assert max(F(0), raw-payment) == F(row["signed_gap_lower"])
```

The audit also checked the displayed decimals against the exact rational
structure; they are lower bounds, not numerical values of the cosine means.

## 5. A same-source counterseed with its completed tail retained

For the symbolic coherent seed `s=-x`, exact algebra gives

\[
U_n(-x)=U_n(0)-16^n x=-T_n,\qquad U_n(-x)+T_n=0.
\]

The completed counterseed is therefore constant zero **because the source
tail cancels the raw state**, not because the tail was discarded. Its signed
gap is zero. For the present shells/resolutions, `q*T_n<1`, so every raw
state is in the last q-cell and every cell minorant is zero as well.

An executed rational control avoids needing an irrational number in code.
Set `M=2186`, `P_M=sum_(k=1)^M 16^(-k)r(k)` from the four original poles,
and choose `s_M=-P_M`. The independent Fraction recurrence found all **18**
raw count vectors entirely in the final q-cell. Every resulting minorant
is zero; retaining the positive source payment still gives zero.

The completed orbit was not declared zero. Algebra gives, for `n<=M`,

\[
U_n(s_M)+T_n=16^{n-M}T_M>0.
\]

At every observed index `n<=2181`, its value is bounded by the exact rational

\[
0<16^{n-M}T_M\le
\frac{47}{225(2187)^2\,16^5}
=\frac{47}{1128443962982400}.
\]

This is a finite same-forcing shadow, not a claim that this rationally shifted
source is universally nonnormal. The exact symbolic seed supplies the
all-time constant countermodel; the rational execution tests the finite
instrument with its residual tail still accounted for.

## 6. Refinement does not erase ambiguous mass

The current prose correctly states the limitation. A simple exact receipt
shows why the qualification is necessary: let an enclosure have
`scale=80, low=29, width=2`, namely `[29/80,31/80]`.

At q=4 it lies within cell 1 and gives raw lower weight `1/2`. At q=8 it
straddles the `3/8` seam, so the production rule returns unresolved and its
discard-unknown lower weight becomes zero. Thus this algorithm's lower bound
is **not unconditionally monotone under refinement**. The documented remedies
(retain a certified coarse lower bound, or minimize over intersected cells)
are sound. The published experiment's zero unresolved mass makes its
reported monotonic comparisons valid.

## 7. Exact scope, hashes and follow-up

The initial inspected bytes had SHA-256:

| File | SHA-256 |
|---|---|
| `pi_filters.py` | `0834ced156e34558b671d0ca870ef9881a93350c685700807cd15d831868f639` |
| `test_pi_filters.py` | `5898ebc732a142df611176e146f3c238cb3540845736d98c16f338fad1121723` |
| `PI_FILTERS.md` | `80863110a22a8c4f86150fd83947ed9573555e2e497f144ab6b470aad9e31a7b` |
| `PI_RESULTS.json` | `aede1461f23d4841d649198b324499ef63e37deb16683b20a8057c5dabf25be5` |

The audit ran its own recurrence, polynomial identities, rational counterseed,
precision mutation and refinement control. It did not rerun the repository
native suite. A later receipt-schema repair must have its own replay entry;
the initial hashes above are retained as audit provenance, not silently
updated to a different inspected object.

**Remaining proof concern:** none found in the displayed finite-bound
derivations. **Remaining mathematical gap:** a source-specific uniform lower
bound for all sufficiently large shells. No finite result in this audit pays
that gap or proves any higher signed rung or pi normality.
