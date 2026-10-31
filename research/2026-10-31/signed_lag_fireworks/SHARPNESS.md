# A sharp leading clock barrier for seed-uniform lag transport

**Status: unconditional paper theorem about the original forcing at the explicitly
altered coherent seed. It does not bound the zero-selected signed statistic.**
This result shows why the doubled logarithmic clock in TRANSPORT.md is a genuine
leading-order boundary for a transport error required to work uniformly in seeds.

Fix a nonzero integer h and a real constant `2<c<3`. Put

```
K_N = floor(c log_16 N),       s* = -π/16,
L^C_(N,K) = (2/(K N)) sum_(1<=k<K)(1-k/K) Re C_(h,k)(N;s*).
```

Then the original signed four-pole BBP tail satisfies

```
lim_N L_(N,K_N)(h;s*) = 4/c - 4/c²,
lim_N L^C_(N,K_N)(h;s*) = 1,
lim_N [L^C_(N,K_N)-L_(N,K_N)(h;s*)] = (1-2/c)² > 0.       (S1)
```

Thus no bound on the actual-minus-reduced weighted signed statistic that is
uniform over all real seeds can tend to zero at any such clock. The threshold
leading coefficient two is sharp in this precise sense. The restriction c<3
belongs to the elementary proof below; no claim is made for c>=3 or for an
estimate exploiting the selected seed zero.

## 1. The source tail has a controlled real derivative

For real x>=0 define the authentic positive tail interpolation

```
T(x) = integral_0^1 t^(8x) P(t)/(16-t^8) dt,
P(t) = 4-2t³-t⁴-t⁵ = 2(1-t³)+(1-t⁴)+(1-t⁵).
```

At integer n this is exactly `T_n=sum_(j>=1)16^-j r(n+j)`, by summing a positive
geometric series under the original four-pole integral. Substitution `t=e^-u`
gives

```
T(x) = integral_0^infinity e^(-(8x+1)u) P(e^-u)/(16-e^-8u) du.
```

For u>=0, `a u e^-a u <= 1-e^-a u <= a u`, so
`15u e^-5u <= P(e^-u) <=15u`, and the denominator lies in `[15,16]`.
Differentiation under this exponentially dominated integral is legitimate and
therefore proves, for every real x>=0,

```
15/(8x+6)³ <= -T'(x) <=16/(8x+1)³,        T''(x)>0.        (S2)
```

Also `P(t)=(1-t)(t²+2)(t²+2t+2)`, whose final two factors have product at most
15 on `[0,1]`, whereas `16-t^8>=15`. Hence
`0<T(x)<integral_0^1 t^(8x)(1-t)dt=1/[(8x+1)(8x+2)]<1/(64x²)` for x>0.
These are source-derived smooth real estimates, not local residue statistics.

## 2. An explicit finite bulk cancellation bound

Let integers `1<=m<=b` and real `A>0` be given. Then

```
|sum_(n=m)^b e(-A T_n)|
 <= 1 + π A/(32m²) + (8b+6)³/(15π A)
 <  1 + 11 A/(112m²) + (8b+6)³/(45 A).                  (S3)
```

Here `e(x)=exp(2πix)`. To prove it, set `f(x)=-A T(x)`. It has positive decreasing
first derivative by S2. Direct integration by parts gives

```
|integral_m^b e(f(x)) dx| <=1/(π f'(b))
                            <=(8b+6)³/(15π A).
```

In detail the two endpoint terms have total magnitude at most
`(1/f'(m)+1/f'(b))/(2π)`, and the integral of
`|f''|/(2π f'^2)` is `(1/f'(b)-1/f'(m))/(2π)`. This is also valid when m=b,
where the integral is zero. Comparing the sum through b-1 to the integral on
unit cells costs at most `integral_m^b |(e(f))'|`; the last summand costs one.
That derivative integral is `2π A[T(m)-T(b)]<π A/(32m²)`. Finally use
`π<22/7` and `π>3` for the strict rational bound in S3. No exponential-sum
black box or asymptotic derivative expansion is required.

## 3. Uniform low and high lag bands

At the coherent seed, `U_n(s*)=-T_n`, so

```
D_(h,k)(N;s*) = sum_(n=1)^(N-k) e(-h(16^k-1)T_n).
```

Write `ell=log_16 N`. Fix small `epsilon>0` and `delta in (0,1)`, and ignore at
most `ceil(delta N)` initial summands. They cost at most `delta+o(1)` after
normalization by N, uniformly for all `k<K_N=O(log N)`.

For `1<=k<=(2-epsilon)ell`, put `A=|h|(16^k-1)`. On the remaining bulk,
`A T_n=O_(h,delta)(N^-epsilon)`. The elementary phase Lipschitz inequality
therefore gives, uniformly in that low band,

```
D_(h,k)(N;s*)/N = 1 + O(delta) + o_(h,delta,epsilon)(1).    (S4)
```

For `(2+epsilon)ell<=k<K_N`, use S3 with `m=ceil(delta N)` and `b=N-k`.
The normalized bulk bound is

```
O_(delta)(1/N + A/N³ + N²/A)
 = O_(h,delta)(1/N + N^(c-3) + N^-epsilon) ->0.            (S5)
```

This is uniform over the high band because h and c are fixed, c<3, and
`A` lies between constant multiples of `N^(2+epsilon)` and `N^c` for large N.
Negative h is handled by complex conjugation. First let N grow, then delta tend
to zero. Thus the normalized real D tends uniformly to one below the threshold
and zero above it, outside an epsilon-width band.

## 4. Retain the weights and take the limit

The remaining transition band has at most `2 epsilon ell+O(1)` lags. Each
normalized real D has magnitude at most one; its total contribution to L has
absolute magnitude `O(epsilon)` because `K_N/ell->c`.
For the low band, the Riemann sum with `u=k/K_N` converges as epsilon tends to
zero to

```
2 integral_0^(2/c) (1-u) du = 4/c-4/c².
```

S4-S5 and the transition bound prove the first limit in S1. This does not fit an
inequality to finite samples; it is a uniform analytic estimate on both bands.

For actual coherent lag correlations, monotonicity gives

```
|C_(h,k)(N;s*)-(N-k)|
 <=2π|h| sum_(n=1)^(N-k)(T_n-T_(n+k))
 <=2π|h| sum_(n>=1)T_n < π|h|/16,
```

uniformly over every lag k. Weighting costs `O_h(1/N)`. The coherent total mass
`(K-1)/K [1-(K+1)/(3N)]` tends to one for K=O(log N), proving the remaining
limits in S1.

## Claim boundary and falsification

This is a signed all-horizon theorem on a **genuine original-source counterseed**,
not a selected π cancellation theorem. It adds a decisive obstruction beyond
mere continuity or seed-Haar averaging: transporting to the reduced arithmetic
lag frequency loses a definite signed amount just beyond the doubled leading
clock, even though the actual lag correlations remain coherent.

A proposed seed-uniform vanishing transport at `K~c log_16 N`, `2<c<3`, is refuted
by S1. A source-selected estimate at zero is unaffected. Falsification probes
are the derivative inequalities S2, the exact finite bulk bound S3, and separate
low/high-band coherent-tail measurements; none may substitute for the proof.

## Exact finite control

`sharpness_receipt.json` certifies the actual original-source coherent-tail sum
for `m=256`, `b=512`, `A=16^6-1`. Each T_n is enclosed by 20 exact future BBP
terms plus the rational remainder `16^-20/[64(n+20)²]`. The independent interval
oracle measures both real and imaginary components, paying the tail width by
the phase Lipschitz bound and rounding the final intervals outward. It gives

```
Re sum in [8970081093/1000000000, 44850405467/5000000000],
Im sum in [-81769220227/2500000000, -40884610113/1250000000],
|sum|² <= 5751276075336161442841/5000000000000000000,
S3 bound = 13295809335180319/113092617830400 < 257.
```

The certified norm is below the analytic bound, which itself improves on the
trivial 257-term bound. This is a finite control of S3, not evidence replacing
the all-horizon limit proof. Four exact regression tests pass, including this
control, the weighted profile, rational limiting constants, and scope rejection.
Reproduce with:

```
python -m unittest discover -s tests -p test_signed_lag_fireworks_sharpness.py -v
python research/2026-10-31/signed_lag_fireworks/run_sharpness_receipt.py
```
