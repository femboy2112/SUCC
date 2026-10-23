# Restricted high-divisor incidence from primitive conic parametrization

Date: 2026-10-21. Status: **PROVED PAPER**, subject to independent review.
The conic parametrization and its linear-height point count are **CLASSICAL**.
The exact weighted cofactor application is **NEW TO PROJECT**. Academic novelty
is **UNVERIFIED**. None of the results below proves the unrestricted moment
bound at `t=2/3`, integer abc, or a new theorem about all rational points.

## Hole contract and concrete gain

For ordered positive primitive `a+b=c<=X`, put `H=abc/rad(abc)` and use the
nonnegative multiplicative coefficients

\[
g_t(1)=1,\quad g_t(p)=0,\quad
g_t(p^k)=p^{t(k-1)}-p^{t(k-2)}\quad(k\ge2).
\]

Each divisor selection `d|a,e|b,f|c` has its own weight
`g_t(d)g_t(e)g_t(f)` and cofactors `a=du,b=ev,c=fw`. Primitivity implies
pairwise coprimality of the divisors. The relation `DU=abc<=X^3/4`, where
`D=def,U=uvw`, is exact, but does not by itself bound the number or weight of
incidences. The unrestricted high-divisor sector remains **OPEN**.

We prove a different, restricted-family theorem with all restrictions visible:
square divisor selections `d=r^2,e=s^2,f=z^2`, controlled root excess
`J=rsz/rad(rsz)`, and a finite or explicitly growing cofactor catalog.
Primitive conic geometry counts the sources, including the difficult
`D>X^2` range where a density-only divisor count fails.

One concrete consequence is the following. For real `X>=2`, let `F_X` be the
set of primitive triples having at least one representation

\[
a=ur^2,\quad b=vs^2,\quad c=(u+v)z^2\le X,
\quad 1\le u,v\le X^{1/100},\quad
\frac{rsz}{\operatorname{rad}(rsz)}\le X^{1/2}.
\]

Then

\[
\boxed{\sum_{(a,b,c)\in F_X}H^{5/7}\le23X^{691/350}.}\tag{1}
\]

The sum counts each source once. It is bounded by a sum retaining every
permitted representation, so overlap between catalog entries causes no
undercount. The exponent is strictly below two; `5/7>2/3`.
The theorem concerns this explicit thin family, not every primitive triple.
It does not assert that this family has positive density, or establish an
asymptotic for its size.

For the corresponding square-divisor selections, retaining multiplicity,
the total weight is at most `23 X^(1367/700)`. Consequently, if only selections
with `Q<D<=2Q` are retained, `Q>X^2`, then

\[
\boxed{I_{5/7}^{\mathrm{catalog}}(X,Q)
 \le23X^2(X^2/Q)^{33/700}.}\tag{2}
\]

This is an actual positive-saving high-divisor incidence estimate on the
declared family, including balanced large divisors. The arithmetic depth
condition is indispensable to this proof. It has not been removed by a new
name or hidden in an implied constant.

## Lemma 1: exact bounded cancellation on a diagonal conic

Let `u,v,w` be positive integers, and display positive integers
`r0,s0,z0` with

\[
u r_0^2+v s_0^2=wz_0^2.
\]

For coprime integers `(n,m)`, put

\[
Q=un^2+vm^2,\quad L=ur_0n+vs_0m,
\quad F=(r_0Q-2nL,\ s_0Q-2mL,\ z_0Q).
\]

Then `uF1^2+vF2^2=wF3^2`, and

\[
\gcd(F_1,F_2,F_3)\mid 2uvw z_0^3.\tag{3}
\]

**Proof.** Expanding the quadratic identity leaves
`Q^2(ur0^2+vs0^2)-4QL^2+4QL^2=wz0^2Q^2`.
Write `g=gcd(F1,F2,F3)`. The identities
`z0 F1=r0 F3-2z0 nL` and
`z0 F2=s0 F3-2z0 mL`, together with `gcd(n,m)=1`, give
`g|2z0 L`. Also `g|z0 Q`. Hence
`g|z0 gcd(Q,2L)`, which divides `2z0 gcd(Q,L)`.

Let `h=gcd(Q,L)`. Two polynomial identities give

\[
ur_0^2Q-L^2+2vs_0mL=vwz_0^2m^2,
\]
\[
vs_0^2Q-L^2+2ur_0nL=uwz_0^2n^2.
\]

Thus `h` divides `w z0^2 gcd(v m^2,u n^2)`. Since `(m,n)=1`, prime by
prime `gcd(v m^2,u n^2)|uv`: a prime dividing `m` cannot divide `n`,
and conversely, while a prime dividing neither contributes at most the
valuation in `uv`. Therefore `h|uvwz0^2`, proving (3). This is a divisibility
bound, not a floating-point estimate of cancellation. No coprimality of
`u,v,w` is required. QED.

Every positive rational point on `u x^2+v y^2=w`, except the displayed
point `(r0/z0,s0/z0)`, is the second intersection with a rational line
through that point. Choose its direction `(n,m)` in coprime integers.
The second-intersection formula is exactly `(F1/F3,F2/F3)` above.
Dividing `F` by its gcd produces the unique primitive integer representative
with positive third coordinate. The displayed point contributes at most one
additional primitive representative. This proves coverage; using all signed
directions can only overcount.

## Theorem 2: explicit primitive conic count

For every real `X>=1`, the number of positive integer roots `(r,s,z)` with

\[
ur^2+vs^2=wz^2\le X,\qquad \gcd(r,s,z)=1
\]

is at most

\[
\boxed{16z_0^2\sqrt{uvwX}.}\tag{4}
\]

In particular (4) bounds roots with the stronger source condition
`gcd(ur^2,vs^2)=1`. Root primitivity does **not** replace that stronger
condition in the weighted arithmetic application.

**Proof.** For a parametrized point, `z=z0 Q/g`, where (3) bounds
`g<=2uvwz0^3`. The height restriction gives

\[
Q\le T=2uv\sqrt w\,z_0^2\sqrt X.
\]

Ignoring coprimality and counting the enclosing rectangle bounds the number
of directions by

\[
(2\sqrt{T/u}+1)(2\sqrt{T/v}+1)
=\frac{4T}{\sqrt{uv}}+2\sqrt{T/u}+2\sqrt{T/v}+1.
\]

The leading term is `8 z0^2 sqrt(uvwX)`. Each boundary term is at most
`2 sqrt(2) z0^2 sqrt(uvwX)`, because `u,v,w,z0,X>=1`. Add the possible
displayed point and use `1<=z0^2 sqrt(uvwX)`. The total is at most
`(10+4 sqrt(2)) z0^2 sqrt(uvwX)<16 z0^2 sqrt(uvwX)`. QED.

This weak but fully explicit constant was chosen to avoid imported implicit
coefficient dependence. It is not an optimized conic point count.

## Theorem 3: faithful weights and finite catalog transport

Let `C` be a finite set of positive cofactor triples. Supply a displayed
integral conic point `(r0,s0,z0)` for each member. Fix real `X>=2`, `Z>=1`,
and `t>=0`. Sum over primitive sources `a=ur^2,b=vs^2,c=wz^2<=X` with
`(u,v,w) in C` and `J=ris(rsz)<=Z`.

The square-divisor selection sum, with each representation counted, satisfies

\[
\sum g_t(r^2)g_t(s^2)g_t(z^2)
\le 16\,2^{-t} Z^t X^{(1+3t)/2}
\sum_{C}z_0^2(uvw)^{(1-t)/2}.\tag{5}
\]

The full arithmetic moment over the union of those sources satisfies

\[
\sum H^t
\le16\,2^{-t} Z^t X^{(1+3t)/2}
\sum_{C}z_0^2(uvw)^{(1+t)/2}.\tag{6}
\]

Both statements hold without an asymptotic qualification. Neither requires
the conic coefficients to be pairwise coprime. An empty coefficient family
contributes zero; a seed is explicit data, not an assumed decision procedure
for rational solvability.

**Proof.** Source primitivity implies the three roots are pairwise coprime.
For any integer `n>=1`, `ris(n^2)=n ris(n)`, and positivity gives
`g_t(n^2)<=ris(n^2)^t`. Thus the selected weight is at most
`(rsz J)^t`. This remains valid at `t=0`, when only the all-unit divisor
selection has nonzero weight.

Also `rad(uvw r^2s^2z^2)>=rad(rsz)`, so the actual full source weight is
at most `(uvw rsz J)^t`. This inequality remains correct when roots share
primes with the coefficients. AM--GM on `a+b=c` gives

\[
uvw (rsz)^2=abc\le X^3/4,
\quad rsz\le X^{3/2}/(2\sqrt{uvw}).
\]

Multiply these pointwise weight bounds by (4), then sum over the catalog.
Overlapping source representations are retained on the right of (6), which
is an upper bound for the once-counted union. On the left of (5) each
representation is a distinct divisor selection and is deliberately retained.
QED.

## Corollary 4: an explicitly growing catalog and a `5/7` moment

For real `B,Z>=1`, take `1<=u,v<=B`, `w=u+v`. Every conic has the displayed
point `(1,1,1)`. There are at most `B^2` ordered pairs and `uvw<=2B^3`.
For `0<=t<=1`, (5) and (6) give respectively

\[
23 B^{(7-3t)/2} Z^t X^{(1+3t)/2},\tag{7}
\]
\[
23 B^{(7+3t)/2} Z^t X^{(1+3t)/2}.\tag{8}
\]

Indeed the constants before rounding are `16*2^((1-3t)/2)` and
`16*2^((1-t)/2)`, both at most `16 sqrt(2)<23`.
The restriction `t<=1` is needed to bound the nonnegative power
`(uvw)^((1-t)/2)` by its maximum in (7).

Set `B=X^theta,Z=X^kappa`. The exact exponents are

\[
E_{\rm sel}=(1+3t)/2+\kappa t+\theta(7-3t)/2,
\]
\[
E_{\rm src}=(1+3t)/2+\kappa t+\theta(7+3t)/2.
\]

Thus either corresponding sector is subquadratic whenever its displayed
exponent is less than two. For `theta=1/100,kappa=1/2,t=5/7`, they are
`1367/700` and `691/350`, proving (1) and the total selected bound.

If the dyadic selected sector is nonempty, then
`Q<D<=X^3/(4uvw)<=X^3/4<X^3`. Hence for
`sigma=2-E_sel>0`, `X^E_sel<=X^2(X^2/Q)^sigma`.
If it is empty the inequality is automatic. This proves (2), uniformly in
every real `Q>X^2`. It is a consequence of a stronger total bound on the
restricted family, not an unjustified moving-modulus CRT asymptotic.

The theorem is nonvacuous in the high-divisor range: roots `(7,17,13)` and
cofactors `(1,1,2)` give source `(49,289,338)`, `J=1`,
`D=49*289*169=2393209>338^2`, with all three divisor moduli exceeding one.
The source lies in the explicit catalog at `X=338`. No claim of infinitely
many squarefree-root conic points is needed or inferred from this example.

## Hostile controls and the remaining inequality

* **Dropping depth is false.** At `t=1`, `g_1(81)=18>sqrt(81)=9`.
  In general `g_t(r^2)<=r^t` is not valid for non-squarefree roots. The
  factor `ris(r)^t` in (5) is mathematically necessary to this majorant.
* **A tempting empty family.** Requiring all three primitive Pythagorean
  roots to be squarefree gives no examples: the even leg is divisible by
  four, since the two odd squares sum to two modulo four and one even
  square has the parity obstruction modulo sixteen unless its root is
  divisible by four. More directly, odd squares modulo sixteen are one
  or nine, so their difference is zero or eight; an even square is zero
  or four, forcing zero. Our theorem allows non-squarefree roots and
  retains `J`. The non-Pythagorean catalog example above has squarefree
  roots.
* **Global source primitivity.** The conic census checks
  `gcd(ur^2,vs^2)=1`; `gcd(r,s,z)=1` alone is a weaker condition.
* **Multiplicity.** Every powerful divisor choice is preserved in exact
  source expansion controls. A conic source cannot stand in for all of
  its divisor choices. Formula (6) separately bounds the genuine full
  weight, so it is not deduced by pretending (5) exhausts those choices.
* **No hidden uniformity.** For a general catalog, the explicit seed heights
  and coefficient sums in (5)--(6) remain. Only the particular catalog
  `w=u+v` has the supplied unit-height seed for every member.

The unresolved arithmetic input for removing the `J<=Z` restriction even
on a fixed conic is an average such as

\[
\sum_{\substack{ur^2+vs^2=wz^2\le X\\\gcd(ur^2,vs^2)=1}}
\operatorname{ris}(rsz)^t
\ll_{u,v,w,t}X^{2-3t/2}.
\tag{9}
\]

Together with the proved pointwise weight bound this is sufficient for a
quadratic full moment on that conic. We have not proved (9), do not label
it equivalent to the unrestricted abc problem, and do not import generic
divisor-correlation theorems whose growth hypotheses fail for `ris(n)^t`.
Passing from a fixed conic to all cofactors additionally requires summable
uniform coefficient dependence and coverage of nonsquare powerful divisors.
Those are separate pathway gaps. The conic parameter space genuinely has
dimension two and supplies the `sqrt(X)` source count; it does not prove
the missing arithmetic-depth estimate.

## Prior art, independent checks, and formal status

The primary source inspected is E. Sofos, *Uniformly counting rational
points on conics*, Acta Arithmetica 166 (2014),
[arXiv:1305.0374v4](https://arxiv.org/abs/1305.0374v4), Theorem 1.1 and
Sections 2--3. It treats nonsingular isotropic ternary integral quadratic
forms, with a norm isometric to the maximum norm, and proves a linear main
term with a coefficient-uniform square-root-height error. Its parametrization
and bounded cancellation confirm that this conic-count mechanism is
classical. Our displayed elementary constant is independently derived here;
no theorem of that paper is needed for the proof. Its unweighted result
does not supply the radical-weight estimate (9).

The exact companion code is `observational_succ/viii_high_divisor.py`.
Focused tests compare direct source census with conic enumeration, and a
separate symbolic expansion verifies the quadratic and cancellation
identities. They check finite implementations and negative controls; they
are not proofs of the universal counting theorem. The full conic theorem
and weighted transport are not Lean-formalized. An external mathematical
referee and a broader priority search remain publication prerequisites.

## Reproduction receipt

Run, with the repository's Python dependencies installed:

```sh
python -m unittest discover -s tests -p test_viii_high_divisor.py -v
python scripts/viii_high_divisor_probe.py
```

The focused suite passes 11 tests, including 6,144 exact signed parameter
directions. The probe checks five polynomial identities by symbolic expansion
and encloses every `5/7`-power by rational endpoints verified through integer
seventh powers. At `X=100000`, the `(1,1,2)` conic census has 73 primitive
sources, all within this finite probe's root-depth budget, including 50
high-divisor selections. The recorded finite counts do not predict the
unrestricted endpoint. No floating-point root, eigenvalue, or asymptotic
density is used as exact authority.

The initial test run had one fixture bookkeeping failure: the expected number
of coprime signed direction pairs across six seeds was written as 6,120;
the actual count is 6,144. Every mathematical assertion in that run passed.
The count assertion was corrected; no mathematical inequality was weakened.
The receipt records its pre-commit checkout and actual source hashes, including
the fact that new research files were uncommitted when the probe ran.
