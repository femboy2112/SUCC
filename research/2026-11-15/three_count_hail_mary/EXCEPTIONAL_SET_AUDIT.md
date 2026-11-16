# Audit: the zero-density shell exceptional set has dimension 7/8

**2026-11-16. Status: proof survives with the explicit conventions below.**
This is a focused independent audit of the parent's candidate, using the
already audited seam-matched tail transfer T3. It concerns arbitrary real
completed endpoints with one fixed BBP tail. It does not exclude the
authentic endpoint `pi/16` from the exceptional set.

## Statement and transfer

Fix the original BBP tail `0<T_n<1/(64n^2)`, and for `beta in [0,1]` set

\[
C_n(\beta)=\lfloor16^n\beta-T_n\rfloor,\qquad
Q_n(\beta)=\lfloor16^n\beta\rfloor,
\]

\[
d_B(\beta)=\frac1B\#\{B\le n<2B:C_n(\beta)\bmod4\in\{1,2\}\},
\]

with the analogous completed statistic `dtilde_B` using `Q_n`. All shell
starts `B` below are positive integers. The claimed set is

\[
E=\{\beta\in[0,1]:\liminf_{B\to\infty}d_B(\beta)=0\}.
\]

T3 gives `|d_B-dtilde_B|<=epsilon_B`, uniformly in beta, with
`epsilon_B->0`. Therefore **the raw and completed exceptional sets are
exactly equal**, not merely equal up to measure zero. The conclusion is

\[
\boxed{\dim_H E=\frac78.}
\]

## Upper bound: the counting argument is correct

Work first on `[0,1)`; adding the endpoint one does not change dimension.
Use canonical hexadecimal digits, with eventual zeros at terminating
endpoints. The selected alphabet is
`S={1,2,5,6,9,10,13,14}`; its complement `A` also has eight symbols.
For `0<epsilon<1/2`, a shell of length B with at most `epsilon B`
selected digits has exactly

\[
8^B\sum_{k=0}^{\lfloor\epsilon B\rfloor}\binom Bk
\le2^{B(3+H_2(\epsilon))}
\]

possible words, where `H_2` is binary entropy **in bits**. The `B-1`
preceding digits are free. Thus the bad-shell set is covered by at most

\[
2^{4(B-1)+B(3+H_2(\epsilon))}
\]

cylinders of depth **`2B-1`**, each of diameter `16^(-(2B-1))`.
Every endpoint with completed liminf zero belongs to the limsup of these
bad-shell sets for each fixed positive epsilon. For

\[
s>\frac{7+H_2(\epsilon)}8,
\]

the sum over **all integer B** of the s-powers of these covering diameters
converges. Tail covers give zero s-dimensional Hausdorff measure. Letting
epsilon decrease to zero proves `dim_H E<=7/8`.

**Proof details to preserve:** the depth is `2B-1`, not B; fixed epsilon
must precede the limsup argument; entropy units must agree with logarithm
units. If using natural exponentials, replace `H_2` by
`h(epsilon)=H_2(epsilon) ln2`.

## Lower bound: product measure, with a strict-exponent estimate

For example choose `B_k=2^(2^k)`, `k>=1`. These shells are disjoint and
`sum_(j<k) B_j=o(B_k)`. At digit positions `[B_k,2B_k)` allow only the
eight symbols in A; at all other positions allow all sixteen symbols.
Let K be the image of this digit-product set in `[0,1]`.

Every point of K has completed selected density zero along the shells
`B_k`, apart from possible alternate-expansion conventions. Those
exceptions are terminating endpoints and also lie in E, because their
canonical future digits are zero. Thus `K subset E` exactly.

Let `F(n)` count the restricted positions among digits `1,...,n`.
During a restricted block the ratio `F(n)/n` increases for all sufficiently
large blocks; between them it decreases. At the right endpoints,

\[
\frac{F(2B_k-1)}{2B_k-1}
=\frac{\sum_{j<k}B_j+B_k}{2B_k-1}\longrightarrow\frac12.
\]

Consequently `limsup_n F(n)/n=1/2`. Assign independent uniform
probabilities to the allowed symbols at every position and push this
measure forward to K. Every admissible depth-n cylinder has mass

\[
\mu(I_n)=16^{-(n-F(n))}8^{-F(n)}=2^{-(4n-F(n))}.
\]

Every individual endpoint has measure zero, since each symbolic cylinder
has mass at most `8^(-n)` and a real point has at most two expansions.
Thus cylinder endpoint conventions do not affect the mass formula.

Fix **any `s<7/8`**. For all sufficiently large n,
`4n-F(n)>=4sn`, so `mu(I_n)<=16^(-sn)`. Given an interval I of length r,
choose n with `16^(-n-1)<r<=16^(-n)`. It meets at most two depth-n
cylinder interiors; boundary points have zero mass. Hence

\[
\mu(I)\le2\,16^{-sn}\le2\,16^s r^s
\]

for all sufficiently small r. The mass-distribution argument now gives
`dim_H K>=s`. Letting `s` increase to `7/8` proves the matching lower bound.

**Important repair:** a uniform Frostman bound at the critical exponent
`s=7/8` is not supplied by this construction. At `n=2B_k-1`, its ratio to
the critical cylinder scale is

\[
\frac{\mu(I_n)}{16^{-7n/8}}
=2^{F(n)-n/2}=2^{\sum_{j<k}B_j+1/2},
\]

which is unbounded. The estimates for every strict `s<7/8` suffice for the
exact dimension. Also, the assertion that an interval meets at most two
cylinders requires choosing its depth as above; it is not true for
arbitrary interval lengths at a fixed depth.

## Duplication and scope check

A targeted repository search of Markdown mathematical records for
Hausdorff dimension, exceptional-set dimension, and dimension `7/8` found
no prior exact result for this gate-liminf set. The current
`TRANSLATOR_NOTES.md`, T12, proves an upper bound approximately
`0.9974244748506521` for the **different** event that the signed budget
`L_B<=0` on infinitely many shells. The present exact gate result does not
replace that signed-budget theorem. This is a repository duplication
check, not an external literature or academic-priority claim.

**Final audit verdict:** the exact `7/8` theorem is valid with the stated
all-integer-shell quantifiers, fixed tail, canonical digit conventions,
entropy units, and strict-exponent mass bound. It is a theorem about the
size of the exceptional endpoint set. Whether the one selected endpoint
`pi/16` belongs to that set remains an independent arithmetic question.
