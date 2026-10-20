# Cloud lane A: quantitative local-to-global arithmetic transfer

**Base:** `0e56e0ae26f3d52a2ea34c0a4288478139fcb634` (`main`).
**Ownership:** cloud CRT lane; new files only. No edits to Claude's elementary
counting, proof contracts, or stacked PRs #200/#201.
**Truth state:** the elementary theorems below are **PROVED LOCAL** (meaning proved
on their stated mathematical domains, including all stated infinite quantifiers).
The mechanisms are **CLASSICAL**; their explicit combined error budget is
new-to-project. Academic novelty is **UNVERIFIED** and is not asserted. RH,
integer abc, and Goldbach remain open. No formal-kernel verification is claimed.

## Hole contract

The target is a uniform transfer from a finite set of genuine integer residue
constraints to counts of positive integer pairs, with all dependence on modulus,
sparsity, cutoff, and global coprimality explicit. The weakest useful result is a
boundary error smaller than the proposed main term in a declared moving-modulus
regime. This closes the fixed-CRT-to-integer-count edge; it does not control
unbounded weighted moments or infer arbitrary moving-prime independence.

Two methods can fail differently: exact floor enumeration, and geometric unit-cell
covering. Global primitivity additionally requires a Möbius remainder or a
prime-tail bound. Cheapest falsifiers are a residue class beyond the triangle at
`W=X`, a pair with an unobserved common prime, and a thin rectangle. These are
retained as tests, not explained away. The next missing theorem is a better sparse
primitive-residue discrepancy beyond the sufficient growth range proved here.

## A1. Triangle counts with a sharp leading boundary constant

Let `W>=1` be an integer, `X>=0` real, and
`R ⊆ (Z/WZ)^2` a **set**, with `r=|R|`. Define

\[
N_R(X)=\#\{a,b\in\mathbb Z_{\ge1}:a+b\le X,\;(a,b)\bmod W\in R\}.
\]

For the unique representatives `u,v∈{1,...,W}` of a class, put
`n=floor((X-u-v)/W)`. Then

\[
N_{(u,v)}(X)=
\begin{cases}(n+1)(n+2)/2,&n\ge0,\\0,&n<0.\end{cases}                 \tag{1}
\]

In particular, uniformly over every such `X,W,R`,

\[
\boxed{\left|N_R(X)-\frac{rX^2}{2W^2}\right|
 \le r\left(\frac{3X}{2W}+1\right).}                              \tag{2}
\]

### Floor-sum proof

Write `a=u+Wm`, `b=v+Wn` with `m,n>=0`. The number of pairs with
`m+n<=L` is `sum_{m=0}^L(L-m+1)=(L+1)(L+2)/2`, proving (1).
Let `t=X/W`, `z=(u+v)/W+{(X-u-v)/W}`. If the class is nonempty,
`0<z<3`, and (1) is

\[
\frac{(t+1-z)(t+2-z)}2
=\frac{t^2}2+\frac{3-2z}{2}t+\frac{(z-1)(z-2)}2.
\]

The last two coefficients have absolute values at most `3/2` and `1`.
If empty, `t<(u+v)/W<=2`, so its discrepancy `t²/2<=t` also obeys
(2). Summing over disjoint classes proves the result for arbitrary `R`.
No integrality of `X` was used. The implementation accepts exact rational `X`;
the theorem applies to all real `X`.

**Sharp leading coefficient.** For `R={(1,1)}`, `X=mW+2`,

\[
\frac{N_R(X)-X^2/(2W^2)}{X/W}\longrightarrow\frac32-\frac2W
\quad(m\to\infty).
\]

Consequently no bound `r(C X/W+C₀)` valid for every `W,X,R`, with
absolute fixed `C₀`, can have `C<3/2`. This asserts optimality of that uniform
linear coefficient, not optimality of the entire two-parameter envelope.

### Independent geometry-of-numbers proof

Scale by `W`: the class consists of anchors `(α+m,β+n)` with
`α,β∈(0,1]` and `m,n>=0`. Assign anchor `(α+m,β+n)` the disjoint
unit cell `[m,m+1)×[n,n+1)`. An anchor's coordinate sum differs from that
of any point of its cell by at most `2`. Therefore the union of cells whose
anchors have sum at most `t=X/W` contains the positive-quadrant triangle of
radius `max(t-2,0)` and is contained in the one of radius `t+2` (boundary
sets of area zero do not matter). Its area is exactly the number of anchors.
Thus, independently of (1),

\[
\frac r2\max(t-2,0)^2\le N_R(X)\le\frac r2(t+2)^2,
\qquad |N_R(X)-rt^2/2|\le 2r(t+1).                              \tag{3}
\]

This is a direct lattice-cell proof of the candidate's error order. It has a
weaker constant than (2), so the two methods are not misreported as two
independent derivations of the sharp constant.

### Moving moduli, sparse sets, high prime powers

For `r>0`, division of (2) by its positive main term gives

\[
\frac{|N_R(X)-rX^2/(2W^2)|}{rX^2/(2W^2)}
\le3W/X+2(W/X)^2.                                               \tag{4}
\]

Thus for **any** sequences `W(X)=o(X)` and nonempty residue sets `R(X)`,
the relative error tends to zero uniformly, independently of sparsity.
The modulus is the full modulus required by the event, not merely the largest
prime, the support size, or the largest prime-power factor.

If `W=X` is an integer and `R={(0,0)}`, the actual count is zero whereas the
main term is `1/2`. Even local primitivity does not save arbitrary `W=X`:
`R={(W-1,W-1)}` is locally primitive and has no point when `W>2`.
These refute an unrestricted moving-modulus asymptotic, not all possible
structured special families at that scale.

## A2. Actual global coprimality: exact identity and explicit tail

For arbitrary `R`, replace it by

\[
R^*=\{(a,b)\in R:\gcd(a,b,W)=1\},\qquad r=|R^*|.
\]

This does not change the globally primitive count `P_R(X)`. For `X>=2` put
`M=floor(X/2)`; for an integer `1<=D<=M` put `H_D=sum_{d<=D}1/d`. Let

\[
\kappa_W=\sum_{(d,W)=1}\frac{\mu(d)}{d^2}
=\prod_{p\nmid W}(1-p^{-2}),\qquad
A_D(W)=\sum_{\substack{d\le D\\(d,W)=1}}\frac{\mu(d)}{d^2}.
\]

Every series here converges absolutely, since it is dominated by
`sum d^-2`. Expanding finite Euler products and passing through an absolutely
convergent sum proves the product identity; it is not a merely formal identity.
Moreover,

\[
\frac12\le\kappa_W\le1,\qquad |\kappa_W-A_D(W)|\le1/D.            \tag{5}
\]

For the lower bound compare with
`prod_{n=2}^K(1-1/n²)=(K+1)/(2K)→1/2`; removing factors increases a product
of numbers in `(0,1)`. The tail estimate follows from
`sum_{d>D}d^-2<=integral_D^∞u^-2 du=1/D`.

**Exact identity.** With `d^-1 R*` meaning multiplication of both coordinates
by the inverse of `d mod W`,

\[
\boxed{P_R(X)=\sum_{\substack{d\le M\\(d,W)=1}}
\mu(d)N_{d^{-1}R^*}(X/d).}                                      \tag{6}
\]

Indeed `1_{gcd(a,b)=1}=sum_{d|a,d|b}μ(d)`, proved by expanding
`prod_{p|gcd(a,b)}(1-1)`. All sums are finite. A common divisor of a locally
primitive pair must be coprime to `W`; division by it induces exactly the stated
bijection of residue sets and preserves cardinality. These facts justify every
term in (6).

Define the fully explicit omitted-divisor budget

\[
T(X,D)=\sum_{d=D+1}^{M}\binom{\lfloor X/d\rfloor}{2}.
\]

It is zero if `D=M`, and otherwise

\[
0\le T(X,D)\le\frac{X^2}{2}\sum_{d>D}d^{-2}\le\frac{X^2}{2D}.
\]

Equation (2), applied only to `d<=D`, and (6) give

\[
\boxed{\left|P_R(X)-\frac{rX^2}{2W^2}A_D(W)\right|
\le r\left(\frac{3X}{2W}H_D+D\right)+T(X,D).}                    \tag{7}
\]

For the omitted part, discard signs and residue restrictions: all pairs
`a=d u,b=d v,a+b<=X` number `binom(floor(X/d),2)`. This proves the
bound on the entire Möbius remainder, including overlaps; no independence
assumption or illicit prime truncation is involved. Combining (5) and (7),

\[
\boxed{\left|P_R(X)-\frac{r\kappa_W X^2}{2W^2}\right|
\le r\left(\frac{3X}{2W}H_D+D\right)+T(X,D)
 +\frac{rX^2}{2W^2D}.}                                         \tag{8}
\]

For fixed `W,R`, choose `D=M`; then `T=0` and the error is
`O(r X log X/W+rX+rX/W²)`, hence `O_{W,R}(X log X)`. For moving
parameters, use the explicit expression (8), not this fixed-parameter notation.
The code improves (7) by dropping `μ(d)=0` and `(d,W)>1` from its lattice
error. The finite-center interval is rational and can be independently checked.

### Uniform primitive correlation transfer

If `r(X)>0`, `r(X)<=W(X)²`, `X→∞`, and

\[
\boxed{\frac{W\log X}{X}\to0,\qquad
       \frac{W^2}{X\sqrt r}\to0,}                              \tag{9}
\]

then, uniformly over every such sequence of residue sets,

\[
\boxed{P_R(X)\sim\frac{r\kappa_W X^2}{2W^2}.}                   \tag{10}
\]

**Proof with all dependencies exposed.** Choose
`D=min(floor(X/2),floor(X/sqrt(r)))`. Under (9), `W=o(X)` and
`sqrt(r)<=W`, so eventually `D>=1`, `D<=X/sqrt(r)`, and
`D>=X/(4sqrt(r))`. Since the main term is at least `rX²/(4W²)`, (8) and
the coarse tail bound yield relative error at most

\[
6WH_D/X+4W^2D/X^2+2W^2/(rD)+2/D.
\]

Use `H_D<=1+log X` and the bounds on `D`: this is at most

\[
6W(1+\log X)/X+12W^2/(X\sqrt r)+8\sqrt r/X,
\]

which tends to zero by (9). No constant depends secretly on `W,R,X`.

- A singleton primitive class has the sufficient range `W=o(sqrt(X))`.
- If `r` is bounded below by a fixed positive multiple of `W²`,
  `W log X=o(X)` suffices.
- A very sparse growing-prime pattern must pay for its actual `r`, even when
  the nonprimitive count already has small relative error.
- These are **sufficient**, not proved necessary or optimal, ranges. No failure
  of the asymptotic outside them is inferred from failure of this bound.

### Separate finite-prime sieve view

Let `Y>=1` be an integer and impose, in addition to `R`, the constraints that
for each prime `p<=Y`, `a,b` are not both divisible by `p`. Their joint modulus is
`W_Y=lcm(W,prod_{p<=Y}p)`, and their finite count `P_{R,Y}(X)` is an exact CRT
count. Then

\[
0\le P_{R,Y}(X)-P_R(X)
\le\sum_{p>Y}\binom{\lfloor X/p\rfloor}{2}
\le X^2/(2Y).                                                  \tag{11}
\]

The first inequality uses the existence of a prime factor of every common
divisor greater than one; any excluded pair has a common prime larger than `Y`.
The last step sums over all integers greater than `Y`. For relative precision
on a density `δ`, this crude tail requires `Yδ→∞`, while CRT boundary error
requires control of the *enlarged* `W_Y/X`. This explicitly shows the cost of
promoting finite-prime primitivity. For example `(5,5)` passes the clocks at
2 and 3 but is not globally primitive.

## A3. Genuine prime-power occupations and CRT products

For a genuine prime `p`, prescribed finite nonnegative `i,j,k`, and
`L=1+max(i,j,k)`, exact valuations of `(a,b,a+b)` are determined modulo `p^L`.
Under local primitivity at most one valuation is positive: if a prime divides
any two slots, it divides the third and divides both `a,b`.

For all-zero occupations, modulo `p` there are `(p-1)(p-2)` pairs, giving density
`(p-1)(p-2)/p²` (zero at `p=2`). For one slot of exact exponent `h>=1`,
modulo `p^(h+1)` there are `p^h(p-1)²` pairs, giving density

\[
(1-1/p)^2p^{-h}.
\]

Proof for the `a` slot: there are `p-1` residues of exact valuation `h` and
`p^h(p-1)` unit choices for `b`; `a+b` is automatically a unit. Exchange slots
using the invertible linear maps `(a,b)↦(b,a)` and `(a,b)↦(a,a+b)` to obtain
the other cases. This recovers the existing local clock law by a finite count.

For a finite genuine prime set `S`, CRT gives `W=prod_{p∈S}p^(L_p)` and
`r=prod r_p`. Its unconditional integer-pair local density is `r/W²`.
The global primitive density is **not** that number: it is

\[
\frac r{W^2}\prod_{p\notin S}(1-p^{-2}).                         \tag{12}
\]

Equations (8)-(10) quantify when (12) transports to the integer triangle even
as `S` and the exponent depths grow. A prime power at the scale of `X` can
violate (4); the product modulus can violate it even when every factor is small.
An incompatible occupation gives `r=0` and identically zero count; relative
error expressions requiring `r>0` are then deliberately inapplicable.

**Divisibility corollary for correlation expansions.** If positive integers
`d,e,f` are pairwise coprime, impose `d|a,e|b,f|(a+b)` and global primitivity.
For each fixed `d,e,f`,

\[
\frac1{X^2}\#\{a+b\le X:(a,b)=1,\;d|a,e|b,f|(a+b)\}
\longrightarrow\frac1{2\zeta(2)def}\prod_{p|def}\frac p{p+1}.    \tag{13}
\]

At each `p^h||def`, the occupied-slot divisibility and other-slot unit condition
have unconditional density `p^-h(1-1/p)`. Divide by `1-p^-2` to compare with
the unrestricted primitive density `1/ζ(2)`. CRT and (8) at fixed modulus prove
(13). This does not justify summing (13) over an unbounded divisor family without
a separately proved dominated-convergence or uniform-integrability argument.

## A4. Highly unbalanced boxes

For real `A,B>=0`, let `B_R(A,B)` count `1<=a<=A,1<=b<=B` in `R mod W`.
Each one-dimensional class has count `A/W+ε`, `|ε|<=1`; multiplying and summing
proves

\[
\left|B_R(A,B)-rAB/W^2\right|\le r((A+B)/W+1).                  \tag{14}
\]

For `A,B,r>0`, relative discrepancy is at most
`W/A+W/B+W²/(AB)`. Thus increasing only the long side does not suffice: the
short side must also resolve the modulus for this uniform theorem. The same
Möbius proof, with `M=floor(min(A,B))`, gives a primitive version of (8):
replace the main term by `rκ_W AB/W²`, the lattice term by
`r((A+B)H_D/W+D)`, and `T` by
`sum_{d>D}floor(A/d)floor(B/d)<=AB/D`; its density-tail term is
`rAB/(W²D)`. Every constant remains explicit. The implementation supplies
exact nonprimitive rectangle counts/enclosures; the primitive rectangle formula
is proved here but not advertised as an implemented API.

## Verification, provenance, and remaining boundary

Files: `observational_succ/cloud_crt_ascent.py`,
`tests/test_cloud_crt_ascent.py`, `scripts/cloud_crt_ascent_probe.py`, and the
adjacent JSON receipt. The 13 focused tests use direct integer enumeration and gcd checks,
not the production floor-sum/Möbius route. Exact valuation cardinalities are
checked by independent finite residue enumeration; a composite-prime mutation
and noncoprime CRT moduli are rejected. Universal proofs are the derivations
above, not the finite census.

The geometric method is an elementary instance of classical lattice-point
boundary counting; historical primary reference: H. Davenport, *On a Principle
of Lipschitz*, J. London Math. Soc. 26 (1951), 179–183,
[doi:10.1112/jlms/s1-26.3.179](https://doi.org/10.1112/jlms/s1-26.3.179).
The publisher metadata was checked during this campaign; no inaccessible theorem
statement or constant from that paper is imported. All needed arguments are
proved above. The local laws independently recover
`research/2026-10-19/ABC_CLOCK_GREEN_TAO.md` §1; its fixed-modulus caveat is now
replaced by the explicit sufficient ranges, not removed.

**Boundary:** arbitrary near-scale moduli are refuted; optimal primitive sparse
ranges remain **UNVERIFIED**; weighted infinite products require an additional
summability/uniform-integrability theorem. This package closes a genuine
quantitative transport edge but makes no arithmetic breakthrough claim.


### Lane-local claim ledger

| Claim | Status | Boundary / falsifier |
|---|---|---|
| A1, (1)-(4): all real X>=0, all W and residue sets | PROVED LOCAL; CLASSICAL mechanisms | Relative asymptotic requires W=o(X); 3/2 sharp uniformly |
| A2, (5)-(8): exact global primitive identity and certified finite remainder | PROVED LOCAL; CLASSICAL Möbius inversion | Actual global gcd is enforced; finite prime clocks alone fail |
| A2, (9)-(10): uniform moving primitive family | PROVED LOCAL, explicit sufficient regime | No optimality or extension outside the two conditions asserted |
| A3, (12)-(13): source-prime density and fixed-divisor bridge | PROVED LOCAL; CLASSICAL CRT | Infinite weighted summation needs an additional argument |
| A4, (14): unbalanced boxes and primitive variant | PROVED LOCAL | Short side also controls relative error |
| Arbitrary W comparable to X suffices | REFUTED | Empty residue-class controls; deep 2-power occupation receipt |
| Finite-prime primitivity implies gcd=1 | REFUTED | (5,5) passes primes 2,3 |
| Outside-literature novelty / formal kernel certification | UNVERIFIED | No novelty or Lean certificate claimed |

A separate cloud researcher audited the full proof and ran 96 fresh sparse
primitive-budget/gcd comparisons. The sole reported correction was the
all-primes/not-all-primes wording in (11), now repaired. That check is a
same-model independent algebraic review plus differently implemented finite
controls, not a different formal kernel or a second derivation of the Möbius
estimate. The independent geometry method proves (3); the floor method proves
(2). The stronger real-cutoff negative-discrepancy sharpness control proposed by
the reviewer is preserved in the reproducible probe.

Reproduce locally with:

```sh
python -m unittest tests.test_cloud_crt_ascent -v
PYTHONPATH=. python scripts/cloud_crt_ascent_probe.py
```

The receipt hashes every deliverable except itself. Broad repository regression
and provenance gates are coordinated centrally; this lane does not claim they
passed on the strength of its focused tests.
