# Three-entry growth: the missing prefix hole and a false GW converse

**Status:** conditional paper theorem, plus an exact countermodel to a different
naive claim. No unconditional three-entry growth theorem is asserted here.

Let n>6, let R be three distinct elements of [n-1], and let
`S=[n-1] minus R`. Insert `n<=w1<w2<w3`, with all shifts zero. Write
`W_j=S union {w1,...,wj}` and `U_j={t: ||vt||>1/n for every v in W_j}`.
Suppose `LR(W_3)<=1/n`.

The baseline hole U_0 is nonempty by Alpha's deletion witness: S is contained
in a one-deletion source with a deleted speed at most n-2. The first-prefix
hole U_1 is nonempty by Gamma's general one-insertion theorem, since S is
contained in the baseline obtained by deleting any two members of R. Removing
the third baseline constraint can only increase the minimum distance.

The additional assertion `U_2` nonempty is not supplied by those arguments.
If U_2 were empty, W_2 would have n-2 distinct positive integer speeds and
`LR(W_2)<=1/n<1/(n-1)`: it would refute the ordinary Lonely Runner bound for
n-2 speeds. No such countermodel is known or claimed here. Conversely, the
ordinary conjecture for these specific prefix sources would supply the hole.

## Conditional quintic growth theorem

**REF-K3.** If U_2 is also nonempty, then

\[
 w_1<\frac{3(n-2)^2(n-1)}{2(n-6)},\qquad
 w_2<\frac{4(n-2)(n-1)}{n-4}w_1,\qquad
 w_3\le2w_1w_2.
\tag{K3}
\]

In particular

\[
 w_3<\frac{18(n-2)^5(n-1)^3}{(n-4)(n-6)^2}=O(n^5).
\]

**Proof.** Put `mu=max_{r in R} L(n,r)` for the exact one-deletion values.
Since R has a member at most n-2 and n>=7, Alpha gives `mu>=1/(n-2)`.
At its rational maximizing time, every retained source in S is at distance
at least mu. The retained minimum is (n-1)-Lipschitz, so U_0 contains an
interval of length `ell=2(mu-1/n)/(n-1)`. Three inserted bad sets cover it.
The sharp periodic occupancy estimate and distinct ordering give

\[
 \ell(1-6/n)<\frac{6(n-2)}{n^2w_1}.
\]

Substitute the lower bound for mu and rearrange to obtain the first bound.

Every nonempty component of U_1 has two actual source endpoints. Distinct
endpoint velocities have product at most `(n-1)w1`, since only w1 exceeds
n-1; equal endpoint velocities give an even larger spacing. Thus some gap
has length at least `1/[n(n-1)w1]`. It is covered by the two remaining bad
sets, and their occupancy estimate gives

\[
 \ell(1-4/n)<\frac{4(n-2)}{n^2w_2}.
\]

The second bound follows. Finally, U_2 is nonempty by hypothesis. Its source
endpoint products are at most w1*w2, so a component has length at least
`1/(n*w1*w2)`. Only w3 remains to cover it. A connected gap lies in a single
closed w3-band, of length `2/(n*w3)`, which gives the final bound. QED.

The argument explains why replacing `(n-1)w1` by `(n-1)w2` at the last step
is unjustified: both gap endpoints may now be supplied by inserted velocities.
It also explains why an automatic cubic conclusion does not follow from
this particular induction.

## General conditional prefix induction

For k>=2 and n>2k, suppose every U_j is nonempty for `0<=j<k`. Put
`P_0=(n-1)^2`, `P_1=(n-1)w1`, and `P_j=w_(j-1)*w_j` for j>=2.
Source endpoint spacing gives a component of U_j of length at least
`1/(n*P_j)`. With m=k-j remaining insertions, occupancy gives

\[
 w_{j+1}<\frac{2m(n-2)}{n-2m}P_j\quad(m\ge2),
 \qquad w_k\le2P_{k-1}\quad(m=1).
\]

Using Alpha's source margin for the initial interval yields `w1=O(n^2)` for
fixed k. The subsequent exponents are 3,5,8,...: in this argument the largest
speed is `O(n^{F_(k+2)})`, with F_1=F_2=1. These are conditional bounds,
not a proof that every needed prefix hole exists.

If any proper prefix already covers at radius 1/n, adding arbitrarily large
distinct remaining velocities preserves coverage. Thus a universal finite
largest-speed bound cannot bypass that obstruction by mere endpoint algebra.

## A genuine countermodel to a naive GW classification

The assertion that all three-entry tight sources arise by three individually
Goddyn-Wong-admissible accelerations is false in the unrestricted gcd domain:

\[
 n=7,\quad R=\{1,3,5\},\quad W=\{8,10,12\},\quad
 V=\{2,4,6,8,10,12\}=2[6].
\]

Dilation invariance and the circle pigeonhole theorem give `LR(V)=1/7`.
The time t=1/7 gives the matching lower witness. Every matching of removed
to inserted speeds pairs r=1 with an integer multiplier at least 8. Its
GW condition would require `gcd(1,b)>1` on a nonempty integer interval,
which is impossible. The actual speed gcd is 2 and may not be normalized
away while retaining this source's deletion/insertion labels.

This countermodel attacks a necessity claim for individual GW conditions;
it does **not** refute the prefix-hole assertion. Its two-insertion prefix
has a strict hole, as the independent Fraction source replay confirms.
Goddyn and Wong explicitly discuss the failure of an unrestricted converse
to simultaneous-acceleration sufficiency in Section 3 of
[*Tight Instances of the Lonely Runner*](https://zenodo.org/records/8275490).
This example is an elementary instance of that known obstruction, not an
academic novelty claim.

The next proof gate is precise: establish `LR(S union {w1,w2})>1/n` for every
three-deletion source, or identify a distinct argument that handles every
possible prefix without assuming the ordinary conjecture. Finite searches
and known GW constructions cannot silently close this gate.
