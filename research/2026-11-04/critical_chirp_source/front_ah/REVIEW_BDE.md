# Independent hostile review of BDE-1 and BDE-3

**Verdict: both paper arguments survive this review.** No defect requiring a
change to the proofs, code, or native tests was found. This is a separate
same-model reasoning pass, not an external mathematical referee or Lean proof.

Reviewed files:

- `front_bde/PROOFS.md`, SHA-256
  `7a661b3a7be46a9b89568265ecdf965203fa20ea1406a16d64dfbc4f2ca51842`.
- Parent `gamma_prybar/front7/TERNARY_DEPTH.md`, SHA-256
  `439e734ce255374198dbb784eac441eb333931fb6c835a6880ceb23796bfe74e`.

The reviewed source remains the original U plus explicitly named sibling or
changed-forcing controls. Neither result establishes selected cancellation
for U. BDE-2 is an inherited corollary and was not the target of this pass.

## BDE-1: an independent zero-period derivation

This derivation removes the need to trust PF-6 for the radial completion.
The coefficients of `d=rsharp-2r`, ordered by descending pole offset, are

`(-8,7), (8,6), (4,5), (8,4), (2,3), (2,2), (-1,1)`.

Thus

\[
d(n)=\int_0^1 t^{8n-8}D(t)\,dt,\qquad
D(t)=-8+8t+4t^2+8t^3+2t^4+2t^5-t^6.
\]

Absolute convergence permits geometric summation under this finite-interval
integral. Direct rational algebra gives

\[
\begin{aligned}
\sum_{n\ge1}16^{-n}d(n)
 &=\int_0^1\frac{D(t)}{16-t^8}\,dt,\\
\frac{D(t)}{16-t^8}
 &=\frac{t}{2-t^2}+\frac{t-1}{t^2-2t+2}
 =\frac12\frac d{dt}\log\frac{t^2-2t+2}{2-t^2}.
\end{aligned}
\]

Both logarithm arguments are positive on `[0,1]`; their ratio equals 1 at
both endpoints. The completed period is therefore exactly zero. Since the
zero-seeded radial recurrence has forcing `-d/4`, its partial sum equals the
negative of the future tail, with the two minus signs cancelling:

\[
Z_n=-\frac{16^n}{4}\sum_{j\le n}16^{-j}d(j)
    =\frac14\sum_{k\ge1}16^{-k}d(n+k).
\]

This verifies the sign and normalization of the smooth radial extension from
the raw rational taps, independently of the inherited radial assertion.

## BDE-1: derivative constants and maximal estimate

The tap sum is 15, the signed offset sum is 53, and the absolute offset sum
is 167. For `x>=2`, every shifted denominator satisfies
`x-e/8 >= (9/16)x`. Applying the mean value theorem to each differentiated
pole gives the stated uniform d-derivative remainder. The two geometric sums
are exactly `sum 16^-k=1/15` and `sum k16^-k=16/225`.
They give

`C_m=(m+1)![1/30+(167/3840)(16/9)^(m+2)]`.

Exact rational arithmetic confirms

`C_2=18413/6561`, `C_3=5708452/295245`,
`32 C_2<128`, and `(16/3)C_3<128`.

Hence for `A>=128`, `Z''` is positive with the claimed factor-two margins,
and `Z'''<0`. Multiplication by H gives the uniform lower bound
`Lambda/(256A)` and upper bound `Lambda/(8A)` on `[A,2A]`.

For `g_d(x)=HZ(x+d)-HZ(x)`, the derivative is positive and decreasing.
Taking `d<=A/Lambda` confines each discrete increment to
`[d Lambda/(256A),1/8]`. The last telescoping endpoint is still valid:
for a correlation of a subinterval ending before or at `2A`, evaluating
`g_d(n+1)` uses `Z(n+1+d)` at most at the endpoint `2A`.
The reciprocal denominator has monotone imaginary part, so its total
variation gives `|C_d|<=C A/(d Lambda)`, with one-point correlations covered
by the same absolute constant. There is no unproved avoidance of integers in
this step; the increment interval explicitly supplies it.

For a subinterval of N points, the zero-extended L-shift Cauchy--Schwarz
identity actually has weights `(1-d/L)` in front of the correlations. Dropping
these weights yields exactly inequality (3) in BDE-1. With
`L=min(N,floor(A/Lambda))`, the range `Lambda<=A/2` ensures the floor is at
least two. In the long-interval case the prefactor is `O(Lambda)` and the
bracket is `O(A+(A/Lambda)log(2A))`; in the short case the prefactor is two.
Both give `O(A Lambda+A log(2A))` for the squared sum. This proves the
uniform maximal-subinterval bound, not just a full-epoch estimate.

At the critical schedule, multiplication by `Lambda<=log A` gives
`O((log A)^(3/2)/sqrt A)->0`. Fixed-h characters nevertheless tend to one
because `Z_n=O(1/n)`. This is consistent: the radial forcing is of order
`1/n`, so its retrieval variation has a different scale from original F4's
`1/n²` forcing. The radial channel must not be required to fail a ratchet
whose implication to normality uses the original four-pole forcing.

## BDE-3: grid lock and quantifiers

At a reset, let `a=nearest_integer(D B(x+L))` and choose
`B k=-a (mod D)`. Since B is a power of 16 and D a power of 3, the inverse
exists. Then `B(V+L)` differs from an integer by at most `1/(2D)`.
The truncated tail identity is exact, and

`B(T-L)<B/(64t²16^K)<=1/(64D)`.

This independently gives the advertised `33/(64D)` lock. Between resets,
`V_n+T_n=16^(n-t)(V_t+T_t)` holds exactly; it is the original forcing identity
at those times, not a conjectured approximate flow.

For sufficiently large t the reset gap equals
`105 floor(log_16(m_t)/105)`, is asymptotic to `log_16(m_t)`, and has
`16^gap<=m_t`. The finite early region where the max selects 1 is harmless.
The reset count is `O(N/log log N)`: after `sqrt N`, each gap is bounded below
by a constant times `log log N`, while the earlier region has at most
`sqrt N` resets. The predecessor t of any point in `[A,2A)` satisfies
`t>=A-O(log log A)` and `t<2A`, uniformly.

For **each fixed h**, eventually `log A>64|h|`, so

`16^j=H_A/|h| > A² log A/(16|h|) > t² >= B_t`.

Both `16^j` and B_t are powers of 16; therefore B_t divides H_A exactly.
Also `B_t>t²/16`, so `H_A/B_t=O(log A)` uniformly on the epoch. Using the
reset lock, `16^(n-t)<=m_t`, and `D_t>m_t^6/3` gives phase error
`O((log A)^-4)`. The exponential Lipschitz estimate and two maximal-sum
triangle inequalities prove BDE-4; multiplication by Lambda leaves an
`O((log A)^-3)` error, which vanishes before invoking CC-02.

The sequence of resets and corrections is chosen without h or A. Only the
onset of the argument depends on h. Thus the conclusion genuinely concerns
one fixed recurrence and every fixed nonzero h, not a family selected after
the frequency. The formula uses finitely many rational future injections and
makes no causal or pi-digit-input claim.

## BDE-3: births, denominator preservation, and inherited scope

At `t=86 (mod 105)`, the factors `8t-7`, `8t-3`, `4t-1` are divisible by
3, 5, 7 respectively. For primes outside this fixed small set, the resulting
proper-factor bounds in the proof are valid. A split odd prime first appears
by `(p+7)/8`; an inert prime first appears at `(p+1)/4` through the raw `2p`
channel. The second raw denominator has odd factor `2t-1`, so its primes also
appeared earlier. For primes greater than 5, that earliest pole is unique
among the four denominators and its numerator coefficient is a p-unit; hence
it survives in the **reduced** forcing denominator. The small primes 3,5,7
already occur by time 2, which is before the chosen reset threshold. Prime 2
is absent from the original collapsed odd denominator and from the ternary
reset. No reset is a first-prime birth, including beyond the designated
`8t-7` class.

Parent T1 is stated for `n>=11`, not for every positive n. BDE-3 uses it only
after a sufficiently large t_0; before t_0 the two recurrences agree exactly.
This handles its actual scope. The nondecreasing powers D_t make every state
perturbation ternary with denominator at most the latest D_t. T1 and the
threshold `D_t<8(t-1)/27` ensure that this pole is strictly shallower than the
authentic state's ternary pole, so addition cannot cancel its leading pole.
At every other prime the perturbation is integral. All state denominators
therefore agree exactly, and all nonternary principal parts agree. The latter
is correctly distinguished from equality of every p-adic digit.

For any zero-seeded integer-radix recurrence, the state-prefix denominator
LCM equals the forcing-prefix denominator LCM: each state is an integer
combination of preceding injections, and each injection is a difference of
two integer-multiple states. Exact state-denominator equality therefore proves
the claimed forcing-prefix LCM equality, including possible cancellation in
individual changed injections. Also `D_t` divides the authentic preceding
prefix LCM by T1 at `t-1`.

Parent T3 is uniform over all rational targets and all `1<=D<=A` on
sufficiently large epochs. Applying it to the **authentic** target U_t with
`D=sqrt A` is legitimate for each t. The lag perturbation has ternary
height at most `O(log^6 A)<sqrt A`; every authentic lag above that height
retains its ternary denominator, and all other prime parts agree identically.
T3 bounds the remaining possible exceptions by `O(A^(3/2))` ordered pairs.
Their normalized tent contribution is bounded by `O(q_A/sqrt A)=o(1)`.
No real occupancy conclusion is smuggled into this p-adic assertion.

## Reproducible algebra check executed during this review

The following command exited zero with
`BDE_INDEPENDENT_SYMBOLIC_IDENTITIES_AND_RATIONAL_CONSTANTS_PASS`.
It verifies the finite symbolic algebra and rational constants; the quantified
analysis and construction are proved in the preceding paragraphs.

```sh
python - <<'PY'
from fractions import Fraction as Q
from math import factorial
import sympy as s
t=s.symbols('t')
D=-8+8*t+4*t**2+8*t**3+2*t**4+2*t**5-t**6
log_derivative=(t-1)/(t*t-2*t+2)+t/(2-t*t)
assert s.cancel(D/(16-t**8)-log_derivative)==0
C2=factorial(3)*(Q(1,30)+Q(167,3840)*Q(16,9)**4)
C3=factorial(4)*(Q(1,30)+Q(167,3840)*Q(16,9)**5)
assert C2==Q(18413,6561) and C3==Q(5708452,295245)
assert 32*C2<128 and Q(16,3)*C3<128
assert (8*86-7)%3==(8*86-3)%5==(4*86-1)%7==0
print('BDE_INDEPENDENT_SYMBOLIC_IDENTITIES_AND_RATIONAL_CONSTANTS_PASS')
PY
```

No shared tests or code were changed during full native validation. Original
zero-seed fixed-h Weyl, critical ratchet, coarse energy, and pi normality all
remain OPEN; RH remains a separate OPEN program.
