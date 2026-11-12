# Independent audit: fixed damped lower filters eventually fail on average

**2026-11-12. Status: PROVED LOCAL using a verified classical mean-value
import.** This is a separately tasked same-model derivation. It checks the
parity, triangular summation and unordered-pair normalization independently
of the originating arithmetic bearing. No numerical asymptotic fit is used.

## Verdict

For every fixed even degree `d>=2` and fixed `0<t<=1/2`, the actual
Goldbach-grade lower response in `DAMPED_FILTERS.md` satisfies

\[
\sum_{2\le n\le X}B_{d,t}(n)
\sim a_1K_t X^2(\log X)^{2t-2},\qquad a_1<0,
\tag{FR1}
\]

where X tends to infinity through positive integers and

\[
K_s=\frac{C_s^2}{s^2}
\left[\left(1-\frac{s}{2}\right)^2+
\left(\frac{s}{2}\right)^2\right]>0,
\qquad
C_s=\frac1{\Gamma(s)}
\prod_p\frac{(1-1/p)^s}{1-s/p}.
\tag{FR2}
\]

In particular the sum is negative for every sufficiently large X and tends
to minus infinity. The fixed filter has negative responses at arbitrarily
large genuine arithmetic midpoints. This **does not** say each sufficiently
large individual response is negative, and it says nothing against
Goldbach itself. A negative minorant is inconclusive about a positive count.

The same obstruction applies to every nontrivial fixed finite damped-response
bank on distinct nodes in `(0,1)` whose grade response is a pointwise lower
minorant of the grade-zero indicator. The bank corollary is proved below.

## 1. Imported theorem and checked hypotheses

**Classical input, not re-proved here:** for fixed `0<s<1`,

\[
A_s(y):=\sum_{m\le y}s^{\Omega(m)}
=C_s y(\log y)^{s-1}(1+o(1)).
\tag{MS}
\]

The exact mean and Euler product are displayed in F. Cellarosi,
[*Smooth Sums over Smooth k-Free Numbers and Statistical Mechanics*](https://arxiv.org/pdf/1304.6610),
page 5, equations (10)-(11), in the larger fixed-parameter range `|s|<2`.
They were freshly inspected for this audit. The separate primary theorem in
R. de la Breteche and G. Tenenbaum,
[*Remarks on the Selberg-Delange method*](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf),
Acta Arith. 200.4 (2021), Theorem 2.1, equation (2.1), was also inspected.

For its direct application set `f(m)=s^Omega(m)`, theorem parameter `r=s`,
`sigma=3/4`, and `A=2`. The prime condition follows from
`sum_(p<=y) f(p)log p=s theta(y)=sy+O_s(y/log^2 y)`. Its prime-power
condition follows because
`s^2/p^(3/2)+sum_(nu>=2)s^nu/p^(3nu/4)=O_s(p^(-3/2))`.
The hypotheses therefore hold for this actual arithmetic function.

Each Euler factor in FR2 is positive. Its logarithm is `O_s(p^-2)`, since
the two first-order terms cancel, so the product converges to a positive
finite number. `Gamma(s)>0` as well. Thus `C_s>0`.

The remainder and constants are used only for a **fixed finite** set of
parameters. No uniform limit as `s->0`, no growing degree theorem, and no
Goldbach hypothesis are being imported.

## 2. Exact parity split

Put `w_s(m)=s^Omega(m)`. Since `Omega(2k)=Omega(k)+1`,

\[
A_{s,e}(y):=\sum_{\substack{2\le m\le y\\m\ {\rm even}}}w_s(m)
=s A_s(y/2),
\]

and, with endpoint one excluded,

\[
A_{s,o}(y):=\sum_{\substack{3\le m\le y\\m\ {\rm odd}}}w_s(m)
=A_s(y)-sA_s(y/2)-1.
\]

The expressions use floor conventions implicit in the sum `A_s`.
For fixed s, MS and `log(y/2)/log y -> 1` give

\[
A_{s,e}(y)\sim c_e y(\log y)^{s-1},\quad
A_{s,o}(y)\sim c_o y(\log y)^{s-1},
\]

\[
c_e=\frac{s}{2}C_s,\qquad c_o=\left(1-\frac{s}{2}\right)C_s.
\tag{FR3}
\]

Both constants are positive. Treating the two parity classes as having equal
weighted mass would give the wrong constant. The prime two changes Omega
by exactly one, which is why the factor `s/2` is forced.

## 3. Triangular convolution from cumulative means

Here is the precise lemma used, with a direct elementary proof.

**Lemma.** Let `u_m>=0` and suppose
`A(y)=sum_(m<=y)u_m ~ c y(log y)^alpha`, where `c>0` and alpha is fixed.
Then

\[
\sum_{m+k\le y}u_m u_k
\sim\frac{c^2}{2}y^2(\log y)^{2\alpha}.
\tag{FR4}
\]

**Proof.** Normalize the measure with atoms `u_m/A(y)` at `m/y` for
`m<=y`. For each fixed `0<z<=1`, its cumulative mass up to z is

\[
\frac{A(zy)}{A(y)}\longrightarrow z,
\]

because `log(zy)/log y -> 1`. The mass at zero is zero. For any fixed
integer J, the J intervals `((j-1)/J,j/J]` therefore each have mass tending
to `1/J`. The product measure of each of their J-squared rectangles tends
to `1/J^2`.

The triangle `x+z<=1` contains every grid rectangle whose two upper
endpoints sum to at most one. It is contained in the union of those
rectangles and a strip meeting only `O(J)` additional rectangles.
Consequently its product-measure mass has liminf and limsup between the
corresponding grid areas. Letting J tend to infinity makes both areas tend
to one half. The triangle's mass is exactly
`A(y)^(-2) sum_(m+k<=y) u_m u_k`. Multiplying by the assumed asymptotic
for `A(y)^2` proves FR4. QED.

This handles the small-endpoint regions and the diagonal boundary without
an unjustified uniform replacement of `log(y-m)` near zero. It is also not
a claim of independence at a fixed arithmetic midpoint. The original
additive coupling remains the triangular constraint; summing over the
midpoint produces this product-weight double sum **exactly**.

Apply FR4 separately to the even and odd weight sequences in FR3. Thus
the ordered, parity-matched triangle

\[
T_s(y)=\sum_{\substack{m,k\ge2\\m+k\le y\\m\equiv k\pmod2}}
w_s(m)w_s(k)
\]

satisfies

\[
T_s(y)\sim\frac{c_e^2+c_o^2}{2}
y^2(\log y)^{2s-2}.
\tag{FR5}
\]

No unproved prime-pair asymptotic appears in this step.

## 4. Exact midpoint and unordered-pair normalization

For the actual grade source,

\[
F_n(s)=\sum_{a=0}^{n-2}s^{\Omega(n+a)+\Omega(n-a)-2}.
\]

The map `(n,a) -> (m,k)=(n-a,n+a)` is a bijection between
`2<=n<=X, 0<=a<=n-2` and unordered representatives
`2<=m<=k, m+k<=2X, m equiv k mod 2`.
It is invertible by `n=(m+k)/2`, `a=(k-m)/2`.

Write

\[
D_s(X)=\sum_{2\le m\le X}w_s(m)^2.
\]

The exact identity is

\[
\boxed{\sum_{2\le n\le X}F_n(s)
=\frac{T_s(2X)+D_s(X)}{2s^2}.}
\tag{FR6}
\]

The diagonal has a **plus** sign: the ordered sum counts each off-diagonal
pair twice and each diagonal once, so adding the diagonal and dividing by
two gives the unordered sum. Since `0<s<1`, `0<w_s(m)<=1`, hence
`D_s(X)<=X`. This is negligible relative to
`X^2(log X)^(2s-2)`, because `log^(2-2s) X / X -> 0`.

Substitute `y=2X` into FR5 and use FR6. The factor four from `(2X)^2`,
the triangular factor one half, and the unordered factor one half cancel.
The resulting constant is

\[
\sum_{2\le n\le X}F_n(s)
\sim \frac{c_e^2+c_o^2}{s^2}X^2(\log X)^{2s-2}
=K_sX^2(\log X)^{2s-2},
\tag{FR7}
\]

which is precisely FR2. As a normalization check, at the additional
parameter `s=1` one has `F_n(1)=n-1` exactly; the same constant formula gives
`C_1=1` and `K_1=1/2`, matching `sum_(n=2)^X(n-1)=X(X-1)/2`.
This check is not needed to import a parameter outside the bank's domain.

## 5. Fixed even filters: the first response dominates

For the fixed even-degree family,

\[
B_{d,t}(n)=\sum_{r=1}^d a_r F_n(t^r),\qquad
a_1=-\frac{t^{d(d-1)/2}}{\prod_{j=1}^{d-1}(1-t^j)}<0.
\]

Set `s_r=t^r`. These are finitely many distinct fixed nodes, with
`s_1>s_r` for every `r>=2`. Applying FR7 individually and dividing by
`X^2(log X)^(2t-2)` gives

\[
\frac{\sum_{n\le X}B_{d,t}(n)}
 {X^2(\log X)^{2t-2}}
=a_1K_t(1+o(1))+
\sum_{r=2}^d a_rK_{t^r}
(\log X)^{-2(t-t^r)}(1+o(1)).
\]

Every term in the finite remainder sum tends to zero. The limit is the
strictly negative constant `a_1K_t`, establishing FR1. The magnitude scale
tends to infinity. Thus finitely many early negative responses cannot
explain the result: there must be negative responses at arbitrarily large n.

For any fixed `0<alpha<1`, subtracting the cumulative asymptotics at
`floor(alpha X)` and X also gives

\[
\sum_{\alpha X<n\le X}B_{d,t}(n)
\sim a_1K_t(1-\alpha^2)X^2(\log X)^{2t-2}<0.
\]

Every sufficiently large such multiplicative shell therefore contains at
least one negative response. This is still a statement about a sum and an
existence in each shell, not eventual pointwise negativity.

## 6. General fixed finite damped-bank obstruction

Let `0<s_m<...<s_1<1` be a fixed finite list of distinct nodes, and let
the fixed real coefficients satisfy

\[
q(h)=\sum_{j=1}^m b_j s_j^h,\qquad
q(0)=1,\qquad q(h)\le0\quad\text{for every integer }h\ge1.
\tag{FR8}
\]

Combine duplicate nodes and delete zero coefficients first, so `b_1!=0`.
Dividing FR8 by `s_1^h` and sending the integer h to infinity gives

\[
b_1=\lim_{h\to\infty}\frac{q(h)}{s_1^h}\le0.
\]

Hence `b_1<0`. The actual arithmetic lower response
`L(n)=sum_j b_j F_n(s_j)` obeys, by the same finite-sum domination argument,

\[
\boxed{\sum_{2\le n\le X}L(n)
\sim b_1K_{s_1}X^2(\log X)^{2s_1-2}<0.}
\tag{FR9}
\]

The condition `q(0)=1` makes this a normalized grade-zero minorant and
ensures the bank is nontrivial. The sign proof actually needs only a
nontrivial bank with the all-positive-grade lower condition. A finite bank
of this type cannot yield a positive lower certificate at every sufficiently
large authentic midpoint, even if the desired prime pair always exists.

## 7. Exact boundaries and earned research consequence

This proves a source-specific obstruction for **fixed finite pointwise
minorant banks**. It strengthens a finite failure observation into a
classically supported asymptotic theorem. It is not a finite-scan inference.

The proof does not apply to:

- Growing degree or a growing number of nodes as the target grows.
- Nodes tending to zero, or weights depending on the target.
- Bounds that use actual source restrictions instead of a minorant on every
  nonnegative integer grade.
- Other observable families, nonlinear source bounds, or access to `F(0)`
  itself.
- A claim about every individual midpoint's sign or a claim of negative
  prime count.

The fixed-node result is compatible with the existing finite reconstruction
theorem: allowing the degree to grow until `epsilon_d(n-1)<1` can recover
the count from exact responses. The new theorem says why leaving that
degree fixed cannot turn the successful small certificates into a uniform
Goldbach proof. It does not prove that a growing-bank method will succeed
without already resolving the original coupled arithmetic problem.

**Authority:** verified classical mean-value theorem plus the explicit
parity, positive-measure triangle, pair bijection and finite-exponent
comparison above. This audit browsed the two stated primary papers and
checked the derivation; it did not run or claim an asymptotic numerical fit,
a native-suite pass, a Lean proof or external referee agreement.

## 8. FR04 audit: growing resolution recovers the known positive average

The proposed growing-degree statement is sound, with a quantifier that must
remain explicit: **one degree `d_X` is chosen at cutoff X and applied to
every midpoint `2<=n<=X` in that sum.** It is not automatically the different
sum that uses degree `d_n` at each individual midpoint.

Let `G(n)` count unordered prime pairs with sum `2n`, using the same endpoint
and diagonal convention as above. The classical prime number theorem gives
`pi(y)~y/log y`. This is a separate established input: the prime case of the
fixed-almost-prime count displayed after Theorem 2.2 in the Cellarosi paper
already inspected also states it. No binary Goldbach hypothesis is needed.

Write `P_o(y)` for the number of odd primes at most y. Then
`P_o(y)=pi(y)-1~y/log y`. Apply the proved triangular lemma to the odd-prime
indicator sequence. Its ordered triangle is

\[
T_o(2X):=\#\{(p,q):p,q\text{ odd primes},\ p+q\le2X\}
\sim2X^2(\log X)^{-2}.
\]

The exact unordered conversion, for integers `X>=2`, is

\[
\sum_{n=2}^XG(n)=\frac{T_o(2X)+P_o(X)}2+1.
\tag{FR04-A}
\]

The additional one is the pair `(2,2)`. A pair containing exactly one even
prime has an odd sum and cannot occur here. The odd-prime diagonal has size
`P_o(X)=O(X/log X)`, hence

\[
\boxed{\sum_{n=2}^XG(n)\sim\frac{X^2}{(\log X)^2}.}
\tag{FR04-B}
\]

This checks the leading constant **one**. It is a recovery of a classical
averaged counting result, not a proof that every even target has a witness.

Fix `0<t<=1/2`. For every integer X choose an even `d_X>=2` and put
`epsilon_X=t^[d_X(d_X+1)/2]`. The exact filter envelope, which is valid for
every even degree and every finite source histogram, gives at each midpoint

\[
0\le G(n)-B_{d_X,t}(n)
\le\epsilon_X\bigl((n-1)-G(n)\bigr)
\le\epsilon_X(n-1).
\]

The same degree is used throughout, so summation yields the exact bound

\[
\boxed{0\le\sum_{n=2}^X\bigl[G(n)-B_{d_X,t}(n)\bigr]
\le\epsilon_X\frac{X(X-1)}2.}
\tag{FR04-C}
\]

If `epsilon_X=o((log X)^(-2))`, the right-hand side is
`o(X^2/(log X)^2)`. Combining FR04-B and FR04-C proves

\[
\boxed{\sum_{n=2}^XB_{d_X,t}(n)
\sim\sum_{n=2}^XG(n)
\sim\frac{X^2}{(\log X)^2}>0.}
\tag{FR04-D}
\]

The final inequality denotes eventual positivity of the **sum**, not of
every summand. The argument uses the uniform exact filter envelope and PNT;
it does not pretend that the earlier fixed-parameter Selberg-Delange
asymptotic is uniform over a growing node bank.

For any fixed `delta>0`, let `d_X` be the least even integer at least two
and at least

\[
\sqrt{\frac{(4+\delta)\log\log X}{\log(1/t)}}
\quad(X>e).
\tag{FR04-E}
\]

Then `d_X(d_X+1)/2>=d_X^2/2` gives

\[
\epsilon_X
\le\exp\bigl(-(2+\delta/2)\log\log X\bigr)
=(\log X)^{-2-\delta/2}
=o((\log X)^{-2}).
\]

Thus the stated rounded-even schedule is sufficient, with no sign or factor
error. Arbitrary finitely many small X may use degree two. The result counts
required response channels; it does not pay for computing or approximating
the changing responses.

**Remaining boundary.** FR04 restores mean positivity by changing the
resolution. It establishes no individual large-midpoint lower estimate,
does not automatically control `sum_(n<=X)B_(d_n,t)(n)`, and does not resolve
the source-specific pointwise Goldbach gap. The fixed-bank obstruction and
this growing-bank consistency result concern different limits and coexist
without contradiction.

This final addition was audited algebraically against the prior triangle
lemma, the exact filter envelope and the classical PNT input. No numerical
asymptotic fit or additional broad test campaign was run for it.
