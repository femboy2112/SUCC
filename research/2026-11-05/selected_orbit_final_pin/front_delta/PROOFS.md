# A finite causal cut for the regularized determinant

**Paper derivation independently checked by the campaign's hostile reviewer
and coordinator; no formal or external certification.** No base-16 normality
or source-selected cancellation is claimed. All statements below concern real
deterministic forcing unless explicitly specialized to the original BBP source.
The distinction matters: universal screening cannot select the zero seed.

## 1. Audit of the sibling Clausen contract

Read-only input is commit `9911dc3421ff0b5b56ee04fb2e86ec34eb2e21fa`, with
common ancestor `4243b6c5dda90d49969c62f99b3f3aae73300ebe`; it is not an
ancestor of this branch's #518 parent. No sibling implementation is imported.

Put `g(t)=log|1-e(t)|^2`. Its Fourier series in the integrable/Abel sense is
`-2 sum_(h>=1) cos(2 pi h t)/h`. Integrating gives the continuous periodic
primitive `L(t)=-sum sin(2 pi h t)/(pi h^2)` and therefore
`L=-Cl_2(2 pi t)/pi`. The factor of two in `g` is essential. For
`q=16^j-16^i`, `alpha=u_j-u_i`, and zero cylinder width `16^-K`, substitution
gives exactly `[L(alpha+Q)-L(alpha)]/Q`, `Q=q16^-K`.

If `i>=K`, `Q` is an integer and the mean is zero. If `i<K<=j`, write
`Q=16^b-delta`, `b=j-K`, `delta=16^{i-K}`. Periodicity gives the numerator
`L(alpha-delta)-L(alpha)`, hence the **negative** short integral on
`[alpha-delta,alpha]`. These agree with CM1–CM4, including arbitrary cylinder
words after replacing `alpha` by `alpha+q d16^-K`.

For `0<delta<=1/16`, use `sin(pi ||t||)>=2||t||`. The negative part of `g`
is bounded by the radially decreasing function `[-2log(4||t||)]_+`, whose
integral over a length-delta arc is maximized at the centered arc and equals
`2delta[1-log(2delta)]`. The positive part is at most `delta log4`.
The absolute signed integral is bounded by the larger of these two bounds,
and hence by `2delta[1+log(1/delta)]`. This proves CM5 without assuming that
the positive and negative parts have disjoint maximizers on the same arc.

Summing `(32/15)16^(-a-b)(1+a log16)`, `a>=1,b>=0`, gives exactly
`C_cross=(512/225)(1/15+16log16/225)`. The past-past sum of `(K-j)` has
`sum_(u=1)^(t-1) u(t-u)=t(t-1)(t+1)/6`. Thus the factor `log16/3` and the
source-uniform `o(A^(2/3))` range are correct. At the unforced zero branch,
`Q^-1 integral_0^Q g=2log(2pi Q)-2+O(Q^2)` uniformly for `Q<=1/16`.
This yields the inherited cubic negative onset. These are rederivations of
existing results, not new claims. Numerical 48-digit sibling receipts do not
become rigorous sign certificates through this audit.

## 2. Definitions for the new regularized cut

Fix **one** `r` with `0<r<1`, independently of `A`. Define

```
g_r(t) = log(1-2r cos(2pi t)+r^2)
       = -2 sum_(h>=1) r^h cos(2pi h t)/h,
L_r(t) = -sum_(h>=1) r^h sin(2pi h t)/(pi h^2),
B_r = -2log(1-r),       LIP_r = 4pi r/(1-r),
C_r = 256 B_r/3375.
```

The series and their differentiated forms used below converge absolutely.
Thus `|g_r|<=B_r`, `|g_r'|<=LIP_r`, and
`|g_r''|<=8pi^2 r/(1-r)^2`. Let `u_0=0` and
`u_(n+1)=16u_n+r_(n+1)` for any prescribed real forcing. As before,
`U_n(s)=u_n+16^n s`. For integers `A>=2`, put

```
E_(A,r)(s) = A^-2 sum_(A<=i<j<2A) g_r(U_j(s)-U_i(s)),
P_(A,K,r) = 16^K integral_0^(16^-K) E_(A,r)(s) ds.
```

The original four-pole forcing, unwrapped `u_n`, literal `u_0=0`, and the
selected real orientation are unchanged. Only the observation kernel changes.

## 3. RC-01: source-uniform linear neutrality and its sharpness

For `A<=K=A+t<=2A`, future-future pair means vanish exactly. The same short
boundary calculation as above gives for a cross pair

```
|M_(ij,r)| <= B_r delta/(16^b-delta)
           <= (16 B_r/15)16^(-a-b).
```

Since `sum_(a>=1)16^-a=1/15` and `sum_(b>=0)16^-b=16/15`, the entire cross
contribution is bounded by `C_r/A^2`. There are `t(t-1)/2` past-past pairs.
Consequently, uniformly in **all sources and all cylinder words**,

```
|P_(A,A+t,r)| <= [C_r+B_r t(t-1)/2]/A^2.                 (RC1)
```

In particular `t=o(A)` guarantees mean neutrality. This is a larger universal
neutral layer than the singular kernel's `o(A^(2/3))`; it does not imply more
neutrality for the singular kernel.

The linear scale is sharp. In the unforced zero model, every past-past phase
is zero. The Lipschitz bound gives

```
|Q^-1 integral_0^Q g_r(v)dv-g_r(0)| <= LIP_r Q/2.
```

Moreover `sum_(A<=i<j<K) Q_ij <= sum_(j=A+1)^(K-1)(j-A)16^(j-K)<t/15`.
Thus

```
|P_(A,A+t,r)-log(1-r)t(t-1)/A^2|
    <= C_r/A^2 + LIP_r t/(30 A^2).                       (RC2)
```

For `t/A->c` in `[0,1]`, the limit is `c^2 log(1-r)`. At any positive
linear cut fraction it is negative. This exact countermodel rules out
source-uniform neutrality through all cuts even for the smooth kernel.

## 4. RC-02: finite seed resolution selects the regularized energy

For any deterministic source, any real initial seed `s_0`, and integer
`ell>=0`, average over `[s_0,s_0+16^(-2A-ell))`. For each pair the mean differs
from its value at `s_0` by at most `LIP_r q16^(-2A-ell)/2`. Also

```
sum_(A<=i<j<2A) q16^-2A
  <= sum_(j=A+1)^(2A-1)(j-A)16^(j-2A) < A/15.
```

Therefore

```
|16^(2A+ell) integral_(s_0)^(s_0+16^(-2A-ell)) E_(A,r)(s)ds
      -E_(A,r)(s_0)| <= LIP_r 16^-ell/(30A).              (RC3)
```

In particular the zero branch needs only the finite cut `K=2A`, with no
minimum-spacing hypothesis, no infinite sum of shells and no control of
logarithmically singular pairs. This estimate survives coherent wrong seeds;
it transports their negative energy faithfully.

## 5. RC-03: a strictly weaker replacement for the singular Fekete obligation

For `c_A(h)=A^-1 sum_(A<=n<2A)e(hU_n(0))`, absolute Fourier convergence gives

```
E_(A,r)(0) = -sum_(h>=1) (r^h/h)|c_A(h)|^2
             -log(1-r)/A.                              (RC4)
```

Thus, for any **single fixed** `0<r<1`, the following are equivalent:

1. `liminf_A P_(A,2A,r)>=0`;
2. `E_(A,r)(0)->0`;
3. `c_A(h)->0` for every fixed nonzero integer `h`.

For (1) to (2), use RC3 and the upper bound `E_(A,r)<=-log(1-r)/A` from RC4.
For (2) to (3), every summand in RC4 is nonnegative. The converse follows by
dominated convergence since `|c_A(h)|<=1` and `sum r^h/h<infinity`. Epoch
equidistribution for every integer `A` gives prefix equidistribution by
successively halving the prefix into such epochs, leaving a bounded initial
part. For the authentic BBP source, the already authenticated Green transport
then gives base-16 normality of pi. **None of the three equivalent premises
has been proved for this source.** Choosing `r=1/2` fixes the observation once.

This is strictly weaker than Gate C on general sequences: take an irrational
rotation `x_n={n theta}` and replace the density-zero set of indices
`n=2^k,2^k+1` by zero. The sequence remains equidistributed, so (1) holds;
on every epoch `A=2^k`, its singular Fekete energy is `-infinity` because of
the repeated pair. RC3 is valid on exactly those collision epochs too.

Classification: **C relative to singular Fekete / total negative Clausen
variation**, because the singularity, distinctness and infinite seed
resolution assumptions are removed. **B relative to direct Weyl**, because
the final limiting comparison is equivalent to Weyl. This is not a new
original-source signed bound and cannot be advertised as such.

## 6. First unpaid source-phase comparison

For the exact original rational `alpha_ij=u_j-u_i` and
`Q_ij=(16^j-16^i)16^-2A`, the remaining comparison, with fixed `r=1/2`, is

```
liminf_(A->infinity) A^-2 sum_(A<=i<j<2A)
   [L_(1/2)(alpha_ij+Q_ij)-L_(1/2)(alpha_ij)]/Q_ij >= 0.  (OPEN)
```

The coherent original-source completion has `U_n=-T_n->0`, so RC4 or direct
continuity gives `E_(A,r)->log(1-r)<0`. Periodic completions have limiting
energy `-sum_(h>=1)(r^h/h)|mu_hat(h)|^2<0`, because their finite supported
periodic measure is not Haar. These quantitatively fail the open comparison.
The rational seed `1/5` is not a required failure: its completed phase has the
same base-16 normality verdict as the original by rational-shift invariance.
No arithmetic hypothesis currently proves this comparison for literal zero
while excluding the coherent and periodic completions.

## 7. Finite certificate method

`regularized_cut.py` uses exact Fraction states and carries, checks the signed
four-pole source against the independent collapsed polynomial, and evaluates
the transcendental observation with outward mpmath interval arithmetic. An
average on an interval of length `q<=1/16` is enclosed by four midpoint panels
plus/minus `M_2 q^2/(24*4^2)`, where `M_2=8pi^2r/(1-r)^2`. This remainder is
analytic, not an empirical quadrature tolerance. Cross means retain the
negative orientation and scale `delta/Q`; future means are exactly zero.
Green tails use 24 original rational terms plus the inherited positive bound
`16^-24/[(8(n+24)+1)(8(n+24)+2)]`. Exact binary interval endpoints are retained
as rational strings in the receipt. Finite signs do not certify (OPEN).
