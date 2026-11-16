# Three coarse masses force an oriented carry event

**Second-pass status:** proved finite inequality and sharp constant; original
zero-seeded source hypotheses remain unproved. This is an elementary
source-attached sufficient criterion, not an empirical-law identification.
Parent asked independently whether a few maximum-CDF and marginal constraints
could force the selected carry event. This derivation did not consult the
parallel LP lane or its output.

## 1. Definitions and an exact nonnegative-slack identity

Let `(J,K)` have any joint probability distribution on `{0,1,2,3}^2`. Write

\[
p_{jk}=\Pr(J=j,K=k),\qquad
F_q=\Pr(J<q,K<q),\qquad c_1=\Pr(K=1),
\]

\[
H=\Pr((J-K)\bmod4\in\{1,2\}).
\]

Here `F_q=Pr(max(J,K)<q)` is a coarse maximum-CDF value. Independent uniform
quarter labels have `F_q=q^2/16`, the quarter-cut version of the user's
square-root/maximum law. That reference is used only to specify numbers;
the theorem does **not** assume independence.

For every pair of labels, the pointwise inequality is

\[
\mathbf1_{(J-K)\bmod4\in\{1,2\}}
\ge
\mathbf1_{J<1,K<1}+\mathbf1_{K=1}-\mathbf1_{J<2,K<2}.
\tag{M1}
\]

The right side is `+1` on `(2,1),(3,1)`, `-1` on `(1,0)`, and zero
elsewhere. Its positive cells are selected events, which proves (M1).
Equivalently, direct expansion gives the exact identity

\[
\boxed{
H=F_1+c_1-F_2
+2p_{10}+p_{02}+p_{03}+p_{13}+p_{20}+p_{32}.}
\tag{M2}
\]

Every term after `F_1+c_1-F_2` is nonnegative. Thus

\[
\boxed{H\ge F_1+c_1-F_2.}\tag{M3}
\]

No marginal hypothesis, limiting argument, source model, or normality
assumption enters this universal finite identity.

## 2. A sharp 1/16 bound from two maximum cuts and one marginal cell

If

\[
F_1=\frac1{16},\qquad F_2=\frac14,\qquad c_1=\frac14,
\]

then

\[
\boxed{H\ge\frac1{16}.}\tag{M4}
\]

Neither the third maximum cut nor the full marginal distributions are needed.
The constant is sharp even if both marginals are exactly uniform and **all
three** maximum cuts match the independent uniform reference. An extremizer is

\[
(p_{jk})=\frac1{16}
\begin{pmatrix}
1&3&0&0\\
0&0&4&0\\
0&1&0&3\\
3&0&0&1
\end{pmatrix}.
\tag{M5}
\]

All row and column sums equal `4/16`, the three upper-left square masses are
`1/16,4/16,9/16`, and the only selected mass is `p_21=1/16`. The difference
residue distribution is `(2,1,0,13)/16`, far from uniform. Hence these
conditions force some oriented mass while allowing substantial nonuniformity;
they do not imply a Haar carry law.

## 3. Robust one-sided error budget

For nonnegative errors `eta_1,eta_2,kappa`, if

\[
F_1\ge\frac1{16}-\eta_1,\qquad
c_1\ge\frac14-\kappa,\qquad
F_2\le\frac14+\eta_2,
\]

then

\[
\boxed{H\ge\frac1{16}-\eta_1-\kappa-\eta_2.}\tag{M6}
\]

Thus a total one-sided defect at most `1/32` forces `H>=1/32`.
Two maximum-CDF errors each at most `eta` and a `K` marginal total-variation
error at most `kappa` give `H>=1/16-2eta-kappa`. The one-cell bound is weaker
than requiring full marginal total variation.

These are deterministic inequalities between probabilities or empirical
frequencies. They supply no statistical confidence claim; any confidence or
sampling model must be separately declared.

## 4. Literal source attachment

For the authentic zero-seeded BBP source, keep

\[
U_n=C_n+y_n,\qquad C_n=\lfloor U_n\rfloor,\quad0\le y_n<1.
\]

The inherited original-source clock is `[U_n]_4=n mod4`. Its odd-denominator
dyadic residue makes

\[
J_n=n\bmod4,\qquad K_n=[y_n]_4,
\qquad C_n\equiv J_n-K_n\pmod4.
\tag{M7}
\]

The brackets in `K_n` mean dyadic reduction of the rational fractional
cofactor, **not** real quarter binning of `y_n`. The real floor was already
used in defining that cofactor. The finite maximum in this note acts on the
declared labels `J_n,K_n`; it is not an undeclared norm on the original real
circle.

On every integer shell `B<=n<2B`, use the empirical distribution of these
label pairs. The left side of (M3) is exactly the selected carry frequency:

\[
\frac1B\#\{B\le n<2B:C_n\bmod4\in\{1,2\}\}
\ge F_{1,B}+c_{1,B}-F_{2,B}.
\tag{M8}
\]

This is exact for every `B>=1`, with no endpoint correction. The `J` clock's
known approximate uniformity is not needed in proving it. Consequently,

\[
\liminf_{B\to\infty}(F_{1,B}+c_{1,B}-F_{2,B})>0
\tag{M9}
\]

is a sufficient source restriction for the open positive-density anti-lock
target. Alternatively, establish the one-sided bounds in (M6) on every
sufficiently late shell, with total defect strictly below `1/16`.

This gives a concrete way to use the maximum-law idea without identifying
the full joint law or proving all-depth normality first. Whether the authentic
source meets these three coarse restrictions remains **OPEN**.

## 5. Calibrated failures identify the necessary data

**Missing marginal cell.** The matrix

\[
\frac1{16}
\begin{pmatrix}
1&3&0&0\\
0&0&4&0\\
0&0&1&3\\
3&0&0&1
\end{pmatrix}
\]

has uniform `J`, all three correct maximum cuts, and **zero** selected mass.
Its `K=1` marginal is `3/16`, exactly the deficit that exhausts (M6).
Thus matching the coarse maximum law and the authentic uniform clock alone
does not suffice.

**Missing middle maximum cut.** Put mass `1/16` at every diagonal cell and
`3/16` at every cell `K=J+1 mod4`. Both marginals are uniform, and
`F_1=1/16,F_3=9/16`, but `F_2=5/16`. Again the selected mass is zero. The
middle maximum cut's discrepancy is exactly `1/16`.

An independent exact integer/Fraction check verified all 16 pointwise cases,
the sharp matrix, both controls, their row/column sums, all stated square
masses, and selected-event counts. These finite cases calibrate (M1)--(M6);
the universal result is the displayed algebra, not an extrapolation.

## 6. Finite application to the inherited certified source receipt

The parent dossier's `carry_quadrature_assault/receipts/carry_residues_mod4.txt`
contains the certified carry residues for `n=1,...,32768`. The indexing was
checked against `scripts/carry_quadrature_probe.py`: character `n-1` records
`C_n mod4`. Reconstruct `K_n=(n-C_n) mod4` using (M7), then count the three
masses. The resulting exact integer counts are:

| Shell start B | B F1 | B c1 | B F2 | B(F1+c1-F2) | Actual selected count |
|---:|---:|---:|---:|---:|---:|
| 64 | 4 | 16 | 19 | 1 | 28 |
| 256 | 13 | 63 | 61 | 15 | 132 |
| 1024 | 61 | 285 | 269 | 77 | 509 |
| 4096 | 246 | 1076 | 1047 | 275 | 2083 |
| 16384 | 1008 | 4146 | 4130 | 1024 | 8178 |

At `B=16384`, this particular certificate is exactly `1/16`. The sum of
one-sided deviations from the three reference masses is `25/8192`, below
`1/32`. These are new statistics of the **same inherited finite certified
source data**, not an independent source family or new proof of its infinite
behavior. The reference cutoffs were chosen from the exact theorem, not fitted
to these counts. No asymptotic confidence statement is licensed.

## Verdict and next discriminating probe

**Disclosed finite theorem:** a maximum law can leave orientation ambiguous
and still, together with a small amount of marginal information, force a
strictly positive amount of the orientation needed by the carry gate.

**Unpaid source theorem:** bound the three original empirical masses in
(M8), with the literal four poles and zero seed. Measure them separately on
fresh source shells and on the inherited coherent-seed controls; determine
which term supplies discrimination. Finite observed success would remain
an observation. A uniform eventual defect bound below `1/16` would establish
the original positive-density anti-lock statement.
