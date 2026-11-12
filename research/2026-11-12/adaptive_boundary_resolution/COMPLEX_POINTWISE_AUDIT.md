# Adversarial proof audit: complex banks and the pointwise gap

Date: 2026-11-12. Baseline: `5d9917031855f806fd5c1f9d8b4543ad3ca24bbf`.

**Verdict:** no proof defect was found in the inspected statements of
[COMPLEX_BANKS.md](COMPLEX_BANKS.md) or
[POINTWISE_GAP.md](POINTWISE_GAP.md). The classical imports were checked
against primary papers, including the complex endpoint and the genuine
prime-pair normalization. The conclusions remain within the stated
fixed-bank, averaged, density-one, or source-blind quantifiers. None of
these results proves positivity at every large arithmetic midpoint.

This audit was performed after both authors' derivations were available.
It is an independently checked argument by another instance of the same
model, with shared classical sources, not a blind external referee or a
formal proof. No new broad scan, asymptotic fit, code change, test-suite
run, or publication was performed for this audit. Algebraic controls
below are explicit calculations, not claims of fresh computational runs.

## 1. Inspection provenance and primary-source verification

The inspected proof-note snapshots have SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `COMPLEX_BANKS.md` | `d2b27fecdb75eaa6a567c25202ddd9073ddc56102fc792c921f889cf68c0bbbc` |
| `POINTWISE_GAP.md` | `26cb8901871b6fc424958b2aeeaca666a28c8d0444fa25b73982fb38dc642a8c` |

The following primary passages were personally retrieved and inspected:

- [Cellarosi, arXiv:1304.6610](https://arxiv.org/pdf/1304.6610), printed
  page 5, equations (10)-(11): the mean of `z^Omega(n)` for `|z|<2`,
  with additive error `O_z(x(log x)^(Re z-2))` and its Euler product.
  The unversioned URL returned the document marked v2. The explicit v2
  URL failed on one retrieval attempt; this was a retrieval issue, not a
  substituted theorem.
- [de la Breteche-Tenenbaum, *Remarks on the Selberg-Delange method*](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf),
  printed page 3, Theorem 1.2 and equations (1.10)-(1.12): the genuinely
  complex-valued formulation. Theorem 2.1 on the next page is explicitly
  nonnegative and is not a valid replacement for this complex step.
- [Vaughan, *A new estimate for the exceptional set in Goldbach's problem*](https://personal.science.psu.edu/rcv4/personal/Publications/StLouis72.pdf),
  printed page 315: the definition of `R_s` as the cardinality of ordered
  prime tuples, the reciprocal-logarithm sum `J_s`, the singular product,
  and the uncorrected logarithmic mean-square estimate preceding
  equation (1). The printed page was also visually inspected from the
  root's cached render. The separately displayed equation (1), which
  contains an exceptional-zero correction, is not the imported formula.

An independent direct retrieval of the Vaughan URL returned a 91,688-byte,
five-page image PDF. Its primary-content hash, checked on the root's
cached copy, is
`fc5af6e2a60baadc82a2fda2cd57c21368ca8814e8e473ed2d1fa31218a01ea2`.
The initial web open failed; opening the root's successfully retrieved
reference subsequently exposed the same first-page definitions and
formula. Shared retrieval provenance is not counted as an independent
arithmetic proof.

## 2. Complex mean: the closed unit disk is actually covered

Write `r=|z|` and `a=Re z`, with `0<r<=1`. To apply the complex
Theorem 1.2, take `f(n)=z^Omega(n)`, `rho=z`, `sigma=3/4`, and
`A=4`. The prime residual `f(p)-rho` is exactly zero. The reciprocal
prime condition is the usual Mertens bound multiplied by `r`.
For the prime-power condition, the geometric ratio is at most
`2^(-3/4)<1`, and

\[
\sum_p\left\{\frac{r^2}{p^{3/2}}+
\sum_{\nu\ge2}\frac{r^\nu}{p^{3\nu/4}}\right\}
\ll\sum_p p^{-3/2}<\infty.
\]

The theorem's expansion includes terms through index three and has
remainder `O_z(x(log_3 x)^beta (log x)^(r-5))`. The exact power
comparison needed to absorb it into the displayed first-order error is

\[
(a-2)-(r-5)=3+a-r\ge3-2r\ge1.
\]

Thus there is a spare positive power of `log x` throughout the whole
closed unit disk, including `z=-1`. The finite higher expansion terms
have size at most `O_z(x(log x)^(a-2))`. Consequently the weaker prefix
bound used by the proof is legitimate:

\[
\left|\sum_{m\le x}z^{\Omega(m)}\right|
\ll_z x(\log x)^{a-1}.
\]

**Endpoint controls.** At `z=-1`, the reciprocal gamma factor is zero.
The proof needs an upper bound and never divides by that constant or
asserts an asymptotic equivalent to zero. At `z=1`, the Euler product
and gamma factor give `C_1=1`; the mean is also checked directly by
counting integers. At non-real unit nodes, absolute weights have size
one, but the signed prefix still has the required cancellation bound.
The puncture at zero is substantive: the normalized formulas divide
by `z`, and a zero node would directly supply the target projector.

The leading Euler factor is well-defined on this disk: no denominator
`1-z/p` vanishes, the real logarithm defines `(1-1/p)^z`, and the
normalized factors have logarithms `O_z(p^-2)`. These observations do
not assert a positive real constant for a non-real node. Positivity is
used only at the positive real node `R`.

## 3. The outer-circle sign lemma survives phase and period attacks

After dividing the bank by `R^h`, write the outer-radius part as
`T(h)=sum_j b_j u_j^h`, where `|u_j|=1` and the unit nodes are distinct.
Conjugation pairing makes `T` real. The inner-radius remainder tends
to zero, so eventual nonpositivity of the full bank forces the Cesaro
mean of `T_+` to vanish.

Finite geometric averages give

\[
\operatorname{Cesaro}(T)=b_R,\qquad
\operatorname{Cesaro}(|T|^2)=S:=\sum_j|b_j|^2>0.
\]

For `L=sum_j|b_j|`, the pointwise inequality
`|T|^2<=L(-T+2T_+)` then yields

\[
b_R\le-S/L<0.
\]

This argument neither assumes a common period nor takes a nonexistent
pointwise limit of the oscillatory sequence. Rational and irrational
phases are both covered by the same geometric average. Removing zero
coefficients and merging duplicate nodes is necessary before asserting
`S>0` from a declared nonempty outer bank; the note explicitly starts
with nonzero coefficients and distinct nodes.

A finite prefix of grade inequalities cannot replace eventual or
all-grade nonpositivity. The root-of-unity example in the note has
`q(h)=-1/(L-1)` at grades `1,...,L-1` and `q(L)=1`. Its missing
positive real outer mode is consistent with the theorem because it
fails the hypothesis. This is a genuine quantifier control, not an
asymptotic exception to the sign lemma.

## 4. Triangle, endpoint, diagonal and strict dominance

Set `w_z(m)=z^(Omega(m)-1)` for `m>=2`. The parity formulas are exact:

\[
W_{z,e}(x)=A_z(x/2),\qquad
W_{z,o}(x)=A_z(x)/z-A_z(x/2)-1/z.
\]

In particular the odd formula deletes the endpoint one explicitly.
The prefix bounds are uniform in the summation variable for each fixed
node, after enlarging the constant to cover bounded arguments. Also
`|w_z(m)|<=1`, and its total absolute mass below `Y` is
`(A_r(Y)-1)/r=O_z(Y(log Y)^(r-1))`.

For the ordered parity-matched triangle, put `v=Y-u`. On `v>=sqrt(Y)`,
the prefix estimate is at most a fixed multiple of
`Y(log Y)^(a-1)`: the logarithms lie within a factor two, even when the
exponent is negative. Summing against absolute `u`-weights gives

\[
O_z\bigl(Y^2(\log Y)^{a+r-2}\bigr).
\]

On the remaining strip, the bound is at most
`sum_(v<=sqrt(Y)) v=O(Y)`. Since `a+r>=0`, the claimed large term
is at least the order `Y^2/log^2Y`, which dominates `Y`. The endpoint
strip is therefore paid rather than discarded. This argument uses
cancellation in one prefix and an absolute bound in the other variable;
it does not require unsupported product convergence for complex measures.

The exact pair identity is

\[
\sum_{n=2}^X F_n(z)=\frac{T_z(2X)+D_z(X)}2,
\qquad D_z(X)=\sum_{m=2}^Xw_z(m)^2.
\]

The diagonal has a **plus** sign and no conjugation. Its modulus is
at most `X`. An elementary mutation check is `X=4,z=i`: the correct
diagonal is `1+1+i^2=1`, while replacing the square by modulus squared
would incorrectly give three. At `X=3`, direct enumeration gives
`sum F_n(z)=2+z`, `T_z(6)=2+2z`, and `D_z(3)=2`, checking the
half factor and sign independently.

For the positive node `R`, the nonnegative triangle argument gives

\[
K_R=C_R^2\left[\frac14+\left(\frac1R-\frac12\right)^2\right].
\]

The factors are consistent: changing cutoff from `X` to `2X` contributes
four, the triangular region contributes one half, and unordered conversion
contributes one half. At `R=1`, this is `K_1=1/2`, agreeing with
`sum_(n=2)^X(n-1)=X(X-1)/2`.

For every other node,

\[
\operatorname{Re}z+|z|\le2|z|\le2R,
\]

and equality throughout would force `z=R`. Hence the difference from
`2R` is strictly positive for each other node. A finite fixed bank has
a strictly positive minimum gap, so every such term is little-o of the
`R`-node main term. The negative coefficient from Section 3 then proves
eventual negative cumulative response and negative sums in every large
fixed-ratio shell.

**Limit-order boundary.** A non-real outer node approaching `R` can
make this exponent gap arbitrarily small. Nothing here supplies a
uniform adaptive estimate as nodes, phases, coefficients, or bank size
vary with the cutoff. A negative sum forces at least one negative
summand in a shell; it does not force every summand to be negative.

## 5. Sharp pointwise and noisy thresholds

For even filters the exact source inequality is
`0<=k-B<=epsilon(M-k)`, with integer `k=c_0` and integer mass budget
`M>=1`. When `k>=1`, its smallest possible guaranteed lower response is

\[
1-\epsilon(M-1).
\]

This is attained by the integer histogram `c_0=1,c_d=M-1` because
the filter tail attains `-epsilon` exactly at grade `d`. Therefore
`epsilon(M-1)<1` is necessary and sufficient for universal sign
completeness over this mass-only class. Equality cannot be included:
the positive target can have `B=0`.

The same strict threshold proves
`k=max(0,ceil B)`. For a positive integer target the downward error
is less than one; for zero target the clamp removes every nonpositive
ceiling. The extremal histogram also defeats this rule when the budget
fails. This is stronger than the earlier unclamped sufficient condition,
without changing the source model.

With `|Bhat-B|<=E`, the reported lower certificate is `Bhat-E`, which
can lie `2E` below the true response. The same extremal source and the
adverse report `Bhat=B-E` attain
`1-epsilon(M-1)-2E`. Thus the noisy strict threshold in the note is
sharp for its declared adversarial-error and reporting rule.

For authentic midpoints `M=n-1`, this means `epsilon_n(n-2)<1`.
Where that condition holds, response positivity is equivalent to
Goldbach at the same midpoint. The necessity argument is source-blind:
it does not assert that an arithmetic histogram attains the extremal
shape. Conversely, failure of the universal budget does not imply
failure for a particular arithmetic source.

The masked-tail correction also has the right direction. For `h>=d`,

\[
\frac{-q(h)}{t^h}
=\frac{t^{d(d-1)/2}}{\prod_{j=1}^{d-1}(1-t^j)}
\prod_{j=1}^{d-1}(1-t^{h-j}).
\]

The product increases from its grade-`d` value toward one. Hence the
loss lies between `lambda_d U_d` and `K_d U_d`, giving a lower and an
upper correction to `B`, respectively. This uses a genuinely additional
masked observable. It does not manufacture the mask from a finite bank
of unmasked samples.

## 6. Individual schedules: the changing-cutoff gap is closed correctly

For an already fixed sequence of individual degrees `d_n`, the relevant
error is `sum_(n<=X) epsilon_n(n-1)`, not one common cutoff error.
If `epsilon_n=o(log^-2 n)`, fix `eta>0` and put the small-o inequality
into effect above a fixed index. For sufficiently large `X`, split at
`sqrt(X)`. The lower part is `O(X)` since `epsilon_n<=1/8`; on the
upper part the error is at most `2 eta X^2/log^2X`. Taking the limit
in `X` first and then in `eta` proves the needed little-o estimate.

No monotonicity of `d_n` is used. Together with the previously proved
prime-pair mean, this gives the individual-schedule aggregate with
constant one. The same summation argument pays reported errors when
their sum is `o(X^2/log^2X)`. The fixed-ratio shell assertion follows
by subtracting cumulative asymptotics of the **same fixed sequence**.

This is a real extension of the earlier common-`d_X` statement. It
does not use a uniform moving-node Selberg-Delange theorem. The proposed
rounded-even `sqrt((4+delta) log log n / log(1/t))` schedule gives
`epsilon_n<=(log n)^(-2-delta/2)` with the correct factor four.

## 7. Quantitative density-one transfer and its exact missing quantifier

The inspected Vaughan page defines ordered genuine-prime counts and
states the classical logarithmic mean-square estimate

\[
\sum_{N\le Y}|R_2(N)-J_2(N)\mathfrak S(N)|^2
\ll_A Y^3(\log Y)^{-A}.
\]

Its singular product at even `N` is
`2 C_2 prod_(p|N,p>2)(p-1)/(p-2)>=2C_2>0`.
The reciprocal-logarithm sum has exactly `N-3` terms, each at least
`1/log^2N`. Therefore every even `N` with
`R_2(N)<J_2(N) mathfrak S(N)/2` in `(Y,2Y]` has squared error at
least a positive constant times `Y^2/log^4Y`. Applying the imported
estimate with exponent `A+4` gives at most `O_A(Y/log^A Y)` such
integers. To pass to a whole prefix, split below `sqrt(Y)` and sum
the remaining dyadic intervals; this retains the same logarithmic
power, rather than losing an extra logarithm.

The arithmetic normalization is exact:

\[
G(n)=\frac{R_2(2n)+\mathbf1_{\{n\text{ prime}\}}}{2}.
\]

Using `2n-3>=n` and `log(2n)<=2 log n` for `n>=3` proves the
stated safe constant `kappa=C_2/8` in
`G(n)>=kappa n/log^2n` outside the inherited exceptional set.
This does not substitute a weighted prime-power count for genuine primes.

Now `epsilon_n(n-1)=o(n/log^2n)` is eventually smaller than half
that lower bound at every good midpoint. Hence only the inherited
exceptions and finitely many early midpoints can have nonpositive
filtered response. This proves the stated
`O_A(X/log^A X)` exceptional-count bound for every **fixed** `A`.
The constants and starting point may depend on the schedule and on
the imported theorem; no numerical threshold is extracted. The same
reasoning pays an additional `2E_n=o(n/log^2n)` for lower reports.

The load-bearing import is a quantitative representation count, not
merely almost-all existence. With only `G(n)>=1`, the coarse schedule
can leave `epsilon_n n` much larger than one and cannot guarantee a
positive lower filter. Thus this transfer neither improves the classical
exceptional set nor removes it.

The note's counterfeit sequence gives a particularly strong control:
it has mass `n-1`, grades only zero and one, the authentic leading
aggregate, and a density-one positive response, while all powers of two
remain failed targets. Its exceptional count is only `O(log X)`, which
is even compatible with every fixed logarithmic exceptional bound
above. Therefore no accumulation of those aggregate and density-one
successes supplies the missing universal quantifier.

## 8. Audit boundary and next decisive checks

No correction to either proof note was required by this audit. The
fragile steps are now explicitly constrained: complex rather than
nonnegative mean imports; additive errors at zero gamma coefficients;
an endpoint-paid triangle bound; an unconjugated diagonal; a fixed
positive exponent gap; strict integer and noisy thresholds; and a
quantitative, rather than existential, density-one import.

The remaining mathematical questions are outside those proofs. A
parameter-uniform estimate for a changing bank requires new control
of the collapsing exponent gap and node-dependent constants. A positive
bound at every arithmetic midpoint requires a pointwise source estimate
or an independently justified source restriction. At the complete
integer resolution, that sign assertion is exactly the target assertion.
Neither primary-source verification nor agreement between model instances
has been counted as paying this outstanding arithmetic obligation.
