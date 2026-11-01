# Two-scale lag equivalence and fixed-harmonic near-zero coherent shadows

**Status: paper proofs, with exact finite controls. No Lean authority, scholarly
priority, or proof of π normality is claimed.** These are additive results over
PR #434 at `030ee84b8b7f655fcf433375bfc0b347e0483c89`. Original four-pole forcing
and exact selected boundary remain unchanged. Counterfactual seeds are explicitly
separate mathematical objects. The earlier single-scale gate was sufficient;
BND-02 below now establishes necessity for the actual BBP family as well.

## BND-01 — an exact two-scale inequality

Let `z_1,...,z_N` be any complex sequence with `|z_n|<=1`, extended by zero to all
integer times. For every integer `K>=1`, define

```
W_K(t) = sum_(j=0)^(K-1) z_(t-j),
B_(N,K) = (1/(N K²)) sum_(t in Z) |W_K(t)|².
```

There are only `N+K-1` possibly nonzero summands. For `1<=m<=K`, write
`K=q m+r`, `0<=r<m`. Then

```
0 <= B_(N,K) <= ((K-r)/K) B_(N,m) + r/K <= B_(N,m)+m/K.     (B1)
```

**Proof.** Decompose the normalized K-window into q shifted normalized m-windows,
each with weight `m/K`, and (if `r>0`) one normalized r-window with weight `r/K`.
Their weights add to one. Convexity of squared complex modulus gives the same
weighted inequality after summing over all t; shifts preserve the full sum.
Thus `B_(N,K) <= (qm/K) B_(N,m)+(r/K) B_(N,r)`. Jensen again gives
`sum_t |W_r(t)/r|² <= sum_n |z_n|² <= N`, so `B_(N,r)<=1`. If `r=0`, omit that
term. This proves B1 without square roots, limiting exchanges, or probability.

For unit phases, exact expansion gives

```
B_(N,K) = 1/K + (2/(K N)) sum_(1<=k<K)(1-k/K) Re C_k(N),    (B2)
C_k(N) = sum_(1<=n<=N-k) z_(n+k) conjugate(z_n),
```

when `K<=N`. (For `K>N`, use only the nonempty correlations.) This is precisely
the finite Gram behind PR #434. The two-scale inequality is classical convex
analysis; its use to settle this dossier's moving-lag necessity is new here.

## BND-02 — the critical signed-lag criterion is necessary and sufficient

Retain every original signed pole, and let `U_0=s` be any **fixed real seed**;
`s=0` is the selected case. Write `z_n=e(h U_n(s))`, `h` a fixed nonzero integer,
and let `L_(N,K)(h;s)` be PR #434's reduced signed lag statistic. Let `E_(N,K)(h)`
be any proved nonnegative bound for the weighted difference between actual and
reduced correlations. In particular PR #434 supplies its original explicit E.
For every schedule with

```
K_N -> infinity, 1<=K_N<=N, E_(N,K_N)(h)->0 for every fixed h != 0,              (B3)
```

the following are equivalent:

1. The completed point `π/16+s` is base-16 normal.
2. `L_(N,K_N)(h;s)->0` for every fixed nonzero integer h.
3. `limsup_N L_(N,K_N)(h;s)<=0` for every fixed nonzero integer h.

**Necessity.** Assume 1. The summable Green-tail comparison gives
`S_N(a;s)/N->0` for every fixed nonzero integer a. For a **fixed** lag k,
PR #434's source transport proves

```
C_(h,k)(N;s) = S_(N-k)(h(16^k-1);s) + O_(h,k)(1),
```

so `C_(h,k)(N;s)/N->0`. Fix m, and apply B2 to obtain
`B_(N,m)->1/m`. Then B1 with `K=K_N` gives
`limsup_N B_(N,K_N)<=1/m`. This holds for every m, so
`B_(N,K_N)->0`. Finally

```
|L_(N,K_N)(h;s) - (B_(N,K_N)-1/K_N)| <= E_(N,K_N)(h)        (B4)
```

proves 2. This argument does **not** assume uniformity in the growing frequency
`h(16^k-1)`; it takes N to infinity at each fixed m, then lets m increase.

**Sufficiency.** Statement 2 implies 3. PR #434's van der Corput inequality bounds
`|S_N(h;s)/N|²` by `(1+(K_N-1)/N)` times
`1/K_N+L_(N,K_N)(h;s)+E_(N,K_N)(h)`. The prefactor is at most two under B3;
3 therefore forces every fixed-h Weyl average to vanish. The same source-tail
comparison proves 1. This uses all fixed h, never a single Fourier coefficient.

Consequently `K_N=floor(log_16 N)` is **equivalent** to normality in the source
family, because the inherited `E<=11|h|/(420K_N)` vanishes. Any larger schedule
proved to satisfy B3 by the clipped-transport theorem of this dossier is also
equivalent. In particular, the doubled clock `K_N=floor(log_4 N)` satisfies
`E*<=8 ceil(sqrt(11|h|/14))/(9 K_N²)` by TRANSPORT.md, so it too is necessary
and sufficient. The caution in PR #434 was reasonable absent this proof; it is now
resolved for this domain. No blanket claim is made for a freely chosen unrelated
uniformly distributed phase sequence, which need not have vanishing fixed-lag
correlations.

A useful finite form of the proof, for `K=q m+r<=N`, is

```
L_(N,K)(h;s) <= ((K-r)/K) [1/m+L_(N,m)(h;s)+E_(N,m)(h)]
                +r/K-1/K+E_(N,K)(h).                     (B5)
```

This is an exact multiscale reduction. It supplies **no unconditional selected
upper bound**: the small-scale signed correlations on the right remain unpaid.
It does eliminate the proposed escape route that the critical gate might simply
be stronger than normality for the actual BBP orbit.

## BND-03 — near-zero shadows with eventual coherence at every fixed harmonic

PR #433 constructs near-zero nonnormal seeds using rational source truncations;
its explicit nonnormality witness harmonic depends on their denominator. The
following dyadic rounding removes that limitation while retaining a vanishing
**unnormalized** selected-prefix error and an explicit short delay to coherence.

Let `M>=1` and `J>=0` be integers. Using the original rational lift `U_M(0)`, set

```
a_(M,J) = floor(16^J U_M(0)),
q_(M,J) = a_(M,J)/16^(M+J),
delta_(M,J) = U_M(0)-a_(M,J)/16^J,  0<=delta_(M,J)<16^(-J),
s_(M,J) = q_(M,J)-π/16.                                   (B6)
```

The rational q and delta are exactly computable from the source, with no supplied
π digits. The seed s is an **irrational symbolic real**, since q is rational.
From `π/16=16^-M(U_M(0)+T_M)` and `0<T_M<1/(64M²)`,

```
s_(M,J) = -16^-M [T_M+delta_(M,J)],
0 < |s_(M,J)| < 16^-M [1/(64M²)+16^-J].                    (B7)
```

The same unmodified forcing gives for every n

```
U_n(s_(M,J)) = 16^n q_(M,J)-T_n.                          (B8)
```

For `n>=M+J`, the first term is an integer. Thus, for **every integer h at once**,

```
e(h U_n(s_(M,J))) = e(-h T_n),  n>=M+J.                   (B9)
```

Each fixed shadow therefore has `S_N(h;s)/N->1` for **every** fixed integer h.
In particular h=1 is already a nonnormality witness independent of M or J.
A quantitative all-N bound is

```
|S_N(h;s)-N| < 2(M+J-1)+π|h|/16,                         (B10)
```

because at most `M+J-1` early terms cost at most two apiece and
`sum_(n>=1)T_n<1/32`. This is a source-identical nonnormal trajectory, not a
counterexample to the selected boundary `U_0=0`.

For the first M observations, the exact homogeneous seed difference and the
phase Lipschitz bound give

```
|S_M(h;s)-S_M(h;0)|
  <= 2π|h| |s| sum_(n=1)^M 16^n
  < (32π|h|/15) [1/(64M²)+16^-J].                        (B11)
```

Choose `J=ceil(log_16(64M²))`. Then the right side is
`<π|h|/(15M²)<22|h|/(105M²)`, while B9 starts at time
`M+ceil(log_16(64M²))`. Thus the entire M-term complex sum is spoofed to
`O_h(M^-2)`, followed only `O(log M)` steps later by coherence at every fixed h.
Increasing M defeats any prescribed finite list of harmonics and any strictly
positive finite observation tolerance. This strengthens the older countermodel;
it does not claim undecidability, computational hardness, or mathematical
nonidentifiability once the exact seed is known.

## BND-04 — exact signed-lag hostility and prefix budget

Write `d=16^-M[1/(64M²)+16^-J]`. For `1<=K<=N<=M`, elementary cosine Lipschitz
with `2π<44/7` gives the strict rational sensitivity bound

```
|L_(N,K)(h;s)-L_(N,K)(h;0)|
 < [88|h| d/(7 K N)]
   sum_(k=1)^(K-1) (1-k/K)(16^k-1) [16(16^(N-k)-1)/15].   (B12)
```

For K=1 both scores and the bound are zero, so replace the strict sign by equality
there. This coefficient is obtained from the complete double sum, including the
large arithmetic lag factor; it does not silently ignore its amplification.

For a **fixed** shadow, let `L=M+J`. At every reduced-lag sample with `n>=L`,
B8 implies exactly the same phase as the coherent seed `s*=-π/16`. The early
samples differ by at most two, hence for all `1<=K<=N`,

```
L_(N,K)(h;s) >= (K-1)/K [1-(K+1)/(3N)] - E_(N,K)(h)
                -[4/(K N)] sum_(k=1)^(K-1)(1-k/K)min(N-k,L-1).               (B13)
```

Here E is specifically the inherited explicit PR #434 budget used by
`shadow_lag_lower`, not an arbitrary C-D comparison budget from BND-02.
Indeed the coherent reduced phase is `e(-h(16^k-1)T_n)`, so
`T_n<1/(64n²)` gives exactly the same pointwise majorant as the source forcing.
The root's clipped budget is also valid in B13 by this pointwise argument;
an unrelated or optimized C-D budget need not control the coherent tail.

The last term is at most `2(L-1)/N`. The score is at most its total mass, which
tends to one. Consequently at the critical logarithmic clock,

```
lim_(N->infinity) L_(N,floor(log_16 N))(h;s_(M,J)) = 1
```

for every fixed M,J and every fixed nonzero h. This explicitly retains the order
of limits: M and J fixed before N grows. B12 concerns finite-prefix spoofing as M
grows; these are distinct quantified statements.

## Provenance, validation, and remaining obligation

The authentic BBP recurrence, positive tail and four-pole estimates are inherited
from the selected frontier and PR #431/#432/#433/#434. B1 uses classical convexity;
BND-02 combines that independent decomposition with the inherited source bridge.
BND-03 uses exact floor rounding of the actual source lift, rather than auxiliary
seed Haar or a fitted phase model. This is one source family; reusing its identity
is not counted as several independent witnesses.

`boundary.py` computes only rational finite instruments. The root-discoverable
`tests/test_signed_lag_fireworks_boundary.py` has 12 tests: exhaustive exact
Gaussian-window versus pair-Gram comparisons, all two-scale splits, rational
subunit controls, a counterexample against dropping the remainder, source
recurrence versus closed finite pole sum, exact dyadic target coherence at fresh
harmonics 3/5/7/11, independently bracketed Machin seed signs/distances, and direct
geometric/double-sum budget comparisons. An initial attempted remainder-mutation
fixture used alternating phases and did not refute the mutant; it was rejected
and replaced by the exact coherent two-point witness (`B_2,3=5/9 > (2/3)B_2,2=1/2`).
The 12-test rerun passed. This history is a fixture correction, not evidence for
a false inequality.

Reproduce with:

```
python -m unittest discover -s tests -p test_signed_lag_fireworks_boundary.py -v
python research/2026-10-31/signed_lag_fireworks/run_boundary_receipt.py
```

**What survives:** the critical gate is exactly as hard as normality for the
source family; near-zero nonnormal shadows survive even a fixed h=1 monitor and
become universally coherent after an explicitly controlled short delay.
**What remains open:** an all-horizon signed upper estimate using the exact
selected seed zero. Every bound above applies to changed seeds or transports an
unproved signed quantity; none improves the selected cancellation itself.
**Next falsification:** subject any claimed finite-prefix or bounded-harmonic
selection rule to B6 with a larger M, and test whether its proof uses exact zero
rather than a numerical seed neighborhood. For a genuine new arithmetic bound,
verify B5 without assuming any small-scale signed term already vanishes.
