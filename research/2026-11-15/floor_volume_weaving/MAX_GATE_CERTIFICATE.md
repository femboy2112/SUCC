# A sharp positive carry gate forced by two uniform marginals and a maximum law

**Status: PROVED LOCAL.** This is a theorem about specified joint probability
laws and an exact finite empirical inequality. It is a sufficient diagnostic
for the original BBP carry gate when its hypotheses hold there. Those
source-specific hypotheses remain unproved. No novelty priority outside this
repository is asserted.

## 1. Object and sharp result

Let `(X,Y)` be any random pair in `[0,1)^2`, both coordinates marginally
uniform. Assume

\[
\Pr(\max(X,Y)<r)=r^2\qquad(0\le r\le1).
\]

Independence is not required. Set `J=floor(4X)`, `K=floor(4Y)`, and

\[
H=\Pr((J-K)\bmod4\in\{1,2\}).
\]

Then the **sharp range** is

\[
\boxed{\frac1{16}\le H\le\frac78.}
\]

Both endpoints are attained by explicit absolutely continuous densities below.
Convex mixtures of these densities attain every value in the interval, while
retaining both uniform marginals and the entire maximum distribution. Thus the
root/maximum law does force a positive gate under the stated marginal
conditions, although it leaves substantial signed ambiguity.

## 2. Exact dual certificate: only three coarse quantities are needed

For every `j,k` in `{0,1,2,3}`, the following pointwise inequality holds:

\[
\mathbf1_{\{(j-k)\bmod4\in\{1,2\}\}}
\ge\mathbf1_{\{k=1\}}+\mathbf1_{\{j=k=0\}}
 -\mathbf1_{\{j<2,\ k<2\}}.
\]

Subtracting the right side from the left gives the nonnegative table

\[
\begin{pmatrix}
0&0&1&1\\
2&0&0&1\\
1&0&0&0\\
0&0&1&0
\end{pmatrix}.
\]

Taking expectations proves, for **every** joint law on these residues,

\[
\boxed{
H\ge\Pr(K=1)+\Pr(J=K=0)-\Pr(J<2,K<2).
}
\]

The specified uniform marginal of `Y` gives the first term `1/4`; the maximum
law at `r=1/4` and `r=1/2` gives the next two terms `1/16` and `1/4`.
Therefore `H>=1/16`.

This is an exact linear-program dual certificate, independently verifiable
without an optimizer. Its lower bound needs **neither all four marginal masses
nor the full continuous maximum law**. Only the single marginal cell `K=1`
and the two diagonal-square probabilities appear.

For the upper bound, the hypotheses give `p_00=1/16` and, by inclusion–exclusion,

\[
p_{33}=1-\Pr(X<3/4)-\Pr(Y<3/4)
 +\Pr(X<3/4,Y<3/4)=1/16.
\]

Both cells are outside the gate, so `H<=1-p_00-p_33=7/8`.

## 3. Sharp lower table and continuous density

The following probability table has uniform row and column sums and cumulative
top-left `q`-square mass `q^2/16` for `q=1,2,3`:

\[
(p_{jk})=\frac1{16}
\begin{pmatrix}
1&3&0&0\\
0&0&4&0\\
0&1&0&3\\
3&0&0&1
\end{pmatrix}.
\]

The only occupied gate cell is `(2,1)`, of mass `1/16`. The carry-difference
distribution is `(2,1,0,13)/16`, far from uniform.

This coarse extremizer extends to the **entire** continuous maximum law. Let
`I_j=[j/4,(j+1)/4)` and define a density on `I_j x I_k` by the following table;
all omitted entries are zero:

| cell `(j,k)` | density `p_-(x,y)` |
|---|---|
| (0,0) | `1` |
| (0,1) | `8y` |
| (1,2) | `4` |
| (2,1) | `16(2x-1)(1-2y)` |
| (2,3) | `8(1-x)` |
| (3,0) | `3` |
| (3,3) | `1` |

Every density is nonnegative on its specified cell. Integrating across each
row interval gives the `X` density identically one:

\[
\begin{array}{c|c}
x\text{ interval}&\int_0^1p_-(x,y)\,dy\\\hline
I_0&1/4+3/4=1\\
I_1&1\\
I_2&(2x-1)+(2-2x)=1\\
I_3&3/4+1/4=1.
\end{array}
\]

The column densities are likewise one: on `I_0` and `I_3` they are
`1/4+3/4`; on `I_1` they are `2y+(1-2y)`; on `I_2` they are one.

For `D(r)=Pr(X<r,Y<r)`, direct cell integration gives

\[
D(r)=\begin{cases}
r^2,&0\le r\le1/4,\\
1/16+\int_{1/4}^{r}2u\,du=r^2,&1/4\le r\le1/2,\\
1/4+\int_{1/2}^{r}[1+(2u-1)]\,du=r^2,&1/2\le r\le3/4,\\
9/16+\tfrac32(r-3/4)+(r-3/4)^2=r^2,&3/4\le r\le1.
\end{cases}
\]

Thus the sharp lower bound survives the strongest continuous version of the
proposed root/maximum hypothesis; extra intermediate thresholds do not improve
the constant.

## 4. Sharp upper density

For completeness, the upper endpoint is attained by the following density,
again zero on every omitted quarter cell:

| cell `(j,k)` | density `p_+(x,y)` |
|---|---|
| (0,0) | `1` |
| (0,2) | `4(2y-1)` |
| (0,3) | `2` |
| (1,0) | `8x` |
| (1,3) | `4(1-2x)` |
| (2,1) | `4` |
| (3,2) | `8(1-y)` |
| (3,3) | `1` |

Its quarter table is

\[
\frac1{16}
\begin{pmatrix}
1&0&1&2\\
3&0&0&1\\
0&4&0&0\\
0&0&3&1
\end{pmatrix}.
\]

Row densities are `1`, `2x+(1-2x)=1`, `1`, and `3/4+1/4=1`;
column densities are `1/4+3/4=1`, `1`, `(2y-1)+(2-2y)=1`, and
`1/2+1/4+1/4=1`. The four expressions for `D(r)` are the same as in the
previous section, with the corresponding row and column contributions
interchanged. All occupied cells except `(0,0)` and `(3,3)` hit the gate, so
`H=7/8`.

## 5. Why the cofactor marginal condition matters

The original source clock `J=n mod4` is asymptotically uniform, and exactly
uniform on shells whose length is divisible by four.
That fact and even the **full** maximum law are insufficient without an
additional cofactor restriction. An explicit continuous control has density

| cell `(j,k)` | density `p_0(x,y)` |
|---|---|
| (0,0) | `1` |
| (0,1) | `8y` |
| (1,2) | `4` |
| (2,2) | `1` |
| (2,3) | `4(2y-1)` |
| (3,0) | `4` |

All other cells have zero density. Its `X` marginal is uniform, and direct
integration on the four diagonal intervals again gives `D(r)=r^2`. In the
third interval, `D(r)=1/4+(r-1/2)+(r-1/2)^2`; in the fourth, its derivative
is `1+(2r-1)=2r`.

However its quarter table is

\[
\frac1{16}
\begin{pmatrix}
1&3&0&0\\
0&0&4&0\\
0&0&1&3\\
4&0&0&0
\end{pmatrix},
\]

which contains **no gate hits**. Its `Y` density on the four quarters is
`5/4`, `2y`, `5/4`, `2y-1`, with quarter masses `(5,3,5,3)/16`.
In particular `Pr(K=1)=3/16`, exactly enough to collapse the lower certificate
to zero. This control changes the joint source law; it is not a BBP trajectory.

## 6. Finite empirical source criterion and tolerances

For the original source, use the inherited authentic coordinates

\[
J_n=n\bmod4,\qquad K_n=[y_n]_4,\qquad
C_n\equiv J_n-K_n\pmod4.
\]

On any finite index set, let `q` be the empirical frequency of `K_n=1`, `d_1`
that of `J_n=K_n=0`, and `d_2` that of `J_n<2,K_n<2`. Then the exact same
pointwise certificate gives

\[
\boxed{\text{selected carry frequency}\ge q+d_1-d_2.}
\]

Consequently the one-sided bounds

\[
q\ge\tfrac14-\epsilon_q,\quad
d_1\ge\tfrac1{16}-\epsilon_1,\quad
d_2\le\tfrac14+\epsilon_2
\]

imply a carry-hit frequency of at least

\[
\tfrac1{16}-(\epsilon_q+\epsilon_1+\epsilon_2).
\]

These statements are finite exact implications. If their errors have a
uniform eventual bound whose sum is strictly below `1/16` on every sufficiently
late integer shell `[B,2B)`, `B in N`, they prove the positive-density carry target. Establishing such bounds
for the original zero-seeded four-pole recurrence is the remaining source
obligation. It has not been obtained by constructing the control densities.

The criterion is strictly weaker than full joint independence with uniform
marginals: such independence implies the three displayed masses, while the
sharp lower control meets them without being independent. That control also
shows the criterion does not force carry-Haar, since its carry distribution is
`(2,1,0,13)/16`. A converse implication from carry-Haar to these clock/cofactor
statistics is not asserted here. The criterion would suffice for the selected
non-locking step without proving all residue classes equidistributed.

## 7. Receipt and limitations

A floating-point LP suggested the dual coefficients and an extremal table.
Those are discovery tools only: the displayed 16-cell nonnegative slack table
and explicit densities prove the result without trusting numerical optimization.
Separate executed symbolic integrations, with exact rational coefficients,
verified every quarter-cell mass, all marginal-density polynomials, all four
diagonal-CDF polynomials, and the gate masses `1/16`, `7/8`, and `0` for the
three controls. The dossier's integrated audit supplies the reproducible receipt.

No imported theorem or production code was changed. No inference is made from
a finite simulation to an infinite BBP orbit. The result identifies an exact,
robust, finitely observable sufficient condition and the minimal quantities
used by its certificate; it does not assert that these quantities follow from
the source's existing arithmetic isometry.
