# Effective escape from every proposed L/R cycle

**Constructor bearing, Round V. Status: PROVED PAPER for the statements below;
OBSERVED for the explicitly reported finite checks.** This note uses the
circle-derived rational source from Round IV. Its universal termination claim
imports the classical fact that pi is not rational or quadratic. An individual
accepted escape certificate is checked by finite rational arithmetic and the
source-enclosure theorem; it does not query a transcendence oracle.

Baseline inspected: `4e311d03e3ac9c3dbcbdc32477cd113f2ac0743b` on
`aletheia/cursed-categories-dedekind-yoneda-2026-11-10`. The checkout and remote
were not modified by this bearing. Only this staging note was written.

## 1. The target and its boundary

Let `w_0 w_1 ...` be the productive L/R word of a real `x` in `(3,4)`.
The application is the Euclidean circumference/diameter ratio `x=pi`.
Fix integers `N>=0`, `p>=1`, and a proposed period block

$$
v=v_0\cdots v_{p-1}\in\{L,R\}^p.
$$

The observer first certifies its actual prefix of length `N`. If the proposal
is a start/period pair `(N,p)` rather than an explicitly supplied word, it also
reads the next `p` arrows and sets `v_j=w_(N+j)`. Those observed letters are
the proposed first block; no later arrow is used in constructing the deadline.

The theorem constructs a finite certificate and an integer `r>=1` such that
the actual output cannot agree with `v^r` throughout positions
`N,...,N+rp-1`. Thus a mismatch appears by the displayed finite deadline.
If `v` is the observed first block, necessarily `r>=2` for a valid certificate.

This theorem holds for every computable nonquadratic irrational with strict
shrinking rational enclosures and the specified prefix chart. The actual
implementation uses the circle source. It is an effective nonperiodicity and
escape result, not a signed cancellation or radix-frequency estimate.

## 2. Endpoint convention and hypothetical periodic cylinders

The certified prefix chart is

$$
E=\begin{pmatrix}a&c\\b&d\end{pmatrix},\qquad
J_0=[a/b,c/d]\subseteq[3,4],\qquad
b,d>0,\quad bc-ad=1.
$$

In particular `det(E)=-1`, and `E` is invertible over the integers. The output
matrices are

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
$$

They update endpoint columns on the right. Put

$$
W=G_{v_0}\cdots G_{v_{p-1}},\qquad
E_r=EW^r=\begin{pmatrix}a_r&c_r\\b_r&d_r\end{pmatrix},
\qquad J_r=[a_r/b_r,c_r/d_r].
$$

These are hypothetical repeated-block cylinders. Computing them requires only
the already known prefix and proposed block. It does not inspect the actual
future output. Every `J_(r+1)` is a nonempty subinterval of `J_r`, and

$$
|J_r|=\frac1{b_rd_r}.
$$

The bounds below show that these widths tend to zero. Consequently the
intersection of all the `J_r` is a single candidate value, denoted `xi_v`.

## 3. A proposed cycle becomes an exact polynomial

Form the conjugate

$$
F=EWE^{-1}=\begin{pmatrix}A&B\\C&D\end{pmatrix}\in SL_2(\mathbb Z).
$$

This formula deliberately uses the stored endpoint matrix `E`; no generator
swap is omitted. If one instead uses the increasing residual chart `ES`, the
period word must be conjugated by `S=[[0,1],[1,0]]` as well, giving the same
global transformation `F`.

The map `F` takes `J_r` to `J_(r+1)` and has no pole on `J_0`. By continuity,
it fixes their unique limiting point `xi_v`. Its fixed-point polynomial is

$$
\boxed{P_F(X)=CX^2+(D-A)X-B.}
$$

Indeed, where the denominator is nonzero,

$$
F(X)-X=-\frac{P_F(X)}{CX+D}.
$$

The polynomial is not identically zero. Otherwise `B=C=0` and `D=A`, making
`F` a scalar identity and therefore making `W` a scalar identity. A nonempty
positive L/R word cannot be a scalar identity: at least one off-diagonal entry
is positive, all entries are nonnegative, and each generator has determinant 1.

### Mixed-letter periods

If `v` contains both letters, every entry of `W` is a positive integer and
`tr(W)>=3`. To see positivity, stop at the first change of letter: the
product is `L^j R` or `R^j L` with `j>=1`, whose four entries are positive.
Further right multiplication by either generator preserves positivity. Conjugation preserves trace and determinant, so

$$
\operatorname{disc}(P_F)
=(D-A)^2+4CB
=(A+D)^2-4
=\operatorname{tr}(W)^2-4.
$$

For an integer `t>=3`, `t²-4` lies strictly between `(t-1)²` and `t²`, so it
is not a square. Also `C` cannot vanish: an integral upper-triangular matrix
with determinant 1 has diagonal entries both1 or both-1, hence trace 2 or -2.
Thus the fixed polynomial is genuinely quadratic and has two irrational
roots; exactly one is selected by the nested cylinders in `J_0`.

Divide its integer coefficients by their positive gcd and choose the sign
with positive leading coefficient. This primitive polynomial is the canonical
certificate polynomial `P`. Primitive reduction does not change its roots.
Nonprimitive period blocks such as `(LR)^j` are permitted; no assumption that
`p` is the minimal period is needed.

### Single-letter periods: remove the artificial double root

For `v=L^p`, direct conjugation gives

$$
P_F(X)=p(bX-a)^2,
\qquad \xi_v=a/b.
$$

For `v=R^p`, it gives

$$
P_F(X)=-p(dX-c)^2,
\qquad \xi_v=c/d.
$$

Use the linear minimal polynomial instead:

$$
P(X)=bX-a\quad(L^p),\qquad P(X)=dX-c\quad(R^p).
$$

This improves the separation estimate and avoids paying a squared small gap.
Both leading coefficients are positive, and unimodularity makes these linear
polynomials primitive. The reduction is justified by the displayed identities;
an arbitrary quadratic may not be replaced by a linear expression.

## 4. The circle source certifies separation from the cycle

Let `I_k=[ell_k,u_k]` be a strict rational source enclosure of `x`, with widths
tending to zero. For `P(X)=q_2X²+q_1X+q_0`, compute its exact range on `I_k`.
The extrema occur among

$$
P(\ell_k),\quad P(u_k),\quad
P\!\left(-\frac{q_1}{2q_2}\right)
\quad\text{when }q_2\ne0
\text{ and the vertex lies in }I_k.
$$

All values are rational. If the range excludes zero, set

$$
\epsilon=\min_{y\in I_k}|P(y)|>0.
$$

Then `|P(x)|>=epsilon`. Because `x` is nonquadratic and `P` is a nonzero
polynomial of degree at most two, `P(x)!=0`. Continuity and shrinking enclosures
therefore guarantee that refinement eventually finds such a stage `k`.

For a sharp rational derivative bound on the prefix bracket, use

$$
\boxed{M=\max\{|P'(a/b)|,\ |P'(c/d)|\}.}
$$

The derivative is affine, so its absolute value takes its maximum at an
endpoint. Here `M>0`: `P` is nonconstant and `J_0` has positive width.
Since `P(xi_v)=0` and both `x,xi_v` lie in `J_0`, the mean-value bound gives

$$
\epsilon\le |P(x)-P(\xi_v)|\le M|x-\xi_v|.
$$

Thus the certificate provides a positive rational distance bound

$$
\boxed{\Delta=\epsilon/M\le |x-\xi_v|.}
$$

The source interval need not already be contained in `J_0`; its role is to
enclose the actual target and certify `P(x)`. Prefix correctness separately
guarantees `x in J_0`, which is what licenses the derivative bound there.

In the pure-letter cases this becomes especially simple. After source
refinement separates it from the relevant endpoint,

$$
\Delta=\ell_k-a/b\quad(L^p),\qquad
\Delta=c/d-u_k\quad(R^p).
$$

The source theorem plus these rational inequalities are sufficient to verify
an individual certificate. Transcendence/nonquadraticity is needed for the
universal assertion that every candidate's refinement search terminates.

## 5. Quantitative contraction of repeated blocks

### Mixed blocks: a sharp universal real constant

Write `W=[[u,v],[w,z]]` with all entries positive integers and `uz-vw=1`.
One block sends the denominator row to

$$
b'=bu+dw,\qquad d'=bv+dz.
$$

A simple rational estimate is

$$
\begin{aligned}
b'd'&=uvb^2+(uz+vw)bd+wzd^2\\
&\ge b^2+3bd+d^2\ge5bd.
\end{aligned}
$$

Therefore

$$
\boxed{|J_{r+1}|\le\frac15|J_r|,
\qquad |J_r|\le\frac{5^{-r}}{bd}.}
$$

In particular the weaker factor 1/4 also holds. The sharper optimal real factor
can be identified. Put `t=b/d>0` and `m=vw>=1`. Then

$$
\frac{b'd'}{bd}
=uvt+(2m+1)+\frac{wz}{t}
\ge2\sqrt{m(m+1)}+2m+1
\ge3+2\sqrt2.
$$

Hence the optimal universal width factor is

$$
\boxed{3-2\sqrt2.}
$$

For `W=LR`, the denominator ratio is `2t+3+1/t`, tending to `3+2sqrt(2)`
as rational `t` tends to `1/sqrt(2)`. Such coprime denominator pairs can occur
in Farey brackets inside `(3,4)`: for coprime `b,d>1`, choose the unique
`a` with `3b<a<4b` and `ad=-1 mod b`, and set `c=(1+ad)/b`.
Then `bc-ad=1` and both endpoints lie in `(3,4)`.
Thus the real bound is sharp even in this domain. Equality is not attained
at rational `b/d`; it is a supremum. The implementation can use the purely
rational factor 1/5 or the sharper exact matrix powers below.

**Calibration against an overstrong bound.** A uniform factor 1/6 is false.
For `E=[[17,24],[5,7]]` and `W=LR`, the width ratio is

$$
\frac{|J_1|}{|J_0|}=\frac{35}{204}>\frac16.
$$

### Pure blocks: exact parabolic widths

For every integer `r>=0`,

$$
|J_r|=\frac1{b(d+rpb)}\quad(v=L^p),
$$

$$
|J_r|=\frac1{d(b+rpd)}\quad(v=R^p).
$$

Both tend to zero. For example, a sufficient strict-escape block count for
`L^p` is

$$
r=\max\left\{1,
\left\lfloor\frac{\Delta^{-1}-bd}{pb^2}\right\rfloor+1\right\};
$$

replace `b²` by `d²` for `R^p`. The floor-plus-one pays the strict inequality,
including the exact integer-threshold case.

## 6. Escape deadline theorem and exact indexing

Choose any integer `r>=1` such that

$$
\boxed{|J_r|<\Delta.}
$$

If the actual target followed `v^r` after the certified prefix, it would lie
in `J_r`. The periodic candidate `xi_v` also lies there. This would imply

$$
|x-\xi_v|\le|J_r|<\Delta\le|x-\xi_v|,
$$

a contradiction. Therefore some candidate-word mismatch occurs at an output
index `j` satisfying

$$
\boxed{N\le j\le B:=N+rp-1.}
$$

If `v` is the already observed first block of the actual stream, the first
such mismatch has `j>=N+p`. All earlier positions agree with the periodic
candidate, so

$$
w_j\ne w_{j-p}.
$$

Thus the witness for the period test convention

$$
F(N,p)=\min\{n\ge N:w_{n+p}\ne w_n\}
$$

is `n=j-p`, and its bound is

$$
\boxed{F(N,p)\le B-p=N+(r-1)p-1.}
$$

The deadline `B` is the last output index that needs to be read, not the
earlier comparison index `F(N,p)`. These must not be interchanged.

### Computing the deadline without reading the future

For mixed blocks, one may choose `r` by multiplying an integer power of 5
until `5^r bd Delta>1`. Alternatively, compute the exact width of `EW^r`.
It is strictly decreasing, so integer doubling followed by binary search
finds the least successful `r`. Matrix powers use exact repeated squaring.
The pure-letter formulas avoid this search entirely.

All this uses the prefix chart, the proposed period block, and geometric
source enclosures. It never looks ahead in the actual L/R stream. Further
source refinement can improve `epsilon` and tighten the deadline. No universal
small bound on the necessary source stage is claimed; termination is proved,
and each returned bound is independently checkable.

## 7. A finite certificate format

A sufficient certificate records:

1. The authenticated prefix and its endpoint matrix `E`, with `bc-ad=1`.
2. The proposed word `v`, declared length `p`, product `W`, and `F=EWE^-1`.
3. The canonical polynomial `P`, including justified pure-letter reduction.
4. The source stage and strict enclosure `I_k` from the Euclidean generator.
5. The exact polynomial range, positive `epsilon`, endpoint derivative bound
   `M`, and `Delta=epsilon/M`.
6. The block count `r`, exact `EW^r` endpoints, and `|J_r|<Delta` check.
7. The predicted last output index `B=N+rp-1`.
8. When executed, the actual mismatching letters at `j` and `j-p`, their
   individual source certificates, and the check `j<=B`.

A verifier recomputes the arithmetic rather than trusting supplied values.
Changing a polynomial, period length, chart, gap, exponent, deadline, or
witness must invalidate the corresponding equality/inequality.

For a quadratic target with a valid periodic tail, its source intervals always
contain a zero of the correct fixed polynomial. The separation stage must
remain unresolved, and the procedure must not manufacture an escape. This is
the essential negative control distinguishing state freshness from output
aperiodicity.

## 8. Actual finite checks by this bearing

The checks used Python `fractions.Fraction` and the pinned Round-IV observer
with bytecode writing disabled. A separate short implementation constructed
period products, global fixed polynomials, exact polynomial ranges, derivative
bounds, matrix powers and deadlines. No production file was changed.

**Algebraic regression.** For nine actual prefix charts at output lengths
`0,5,...,40`, all 126 words of lengths 1 through 6 were checked: **1,134 cases**.
Each case checked determinant/trace under conjugation, the exact rational
identity for `F(x)-x` at two safe rational samples, and four successive
repeated-cylinder steps. Mixed blocks satisfied the rational 1/5 contraction;
pure blocks matched the exact denominator formulas. The 1/6 mutation was
rejected by the exact 35/204 example above. All assertions passed.

An initial set of nine pi-path examples was inspected retrospectively and is
regression evidence, not a holdout. It showed that accepting the first positive
polynomial separation can leave a loose but valid deadline. In particular,
start 22 and period 1 first separated at source stage 17 and gave deadline 765,
while the first mismatch was 314. The validity of that bound does not imply
optimality.

**Prospective execution order.** In a separate run, the fixed cases below
were declared before future output was generated. For each case, the code
generated exactly `N+p` arrows, computed a deadline using the first separating
source stage plus a predetermined eight further source refinements, asserted
that the output count remained `N+p`, printed the prediction, and only then
continued the output until the first mismatch.

| Start N | Period p | Observed block | Source stage | Predicted last output index | Actual first mismatch j | Period witness j-p |
|---|---|---|---:|---:|---:|---:|
|6|1|`R`|14|22|21|20|
|22|1|`R`|25|315|314|313|
|1009|7|`LLLLLLL`|340|1022|1018|1011|
|1009|31|`LLLLLLLLLRRLLLLLRRRRLRRLLRRRRRR`|365|1070|1040|1009|
|1337|13|`RRRRRRRRRRRRR`|516|1362|1357|1344|
|2048|9|`RLLLRLLLR`|881|2065|2057|2048|

The first two rows reuse known illustrative regions. The last four were fresh
regions beyond the 512-arrow prefix used in this bearing's initial algebraic
work; no source parameter was fitted to their future mismatch. All deadlines
held. This is a finite validation of the proved interface, not a universal
proof inferred from six cases.

**Exact long-run illustration.** At output start 22, the chart is
`E=[[333,355],[106,113]]`. The residual is

$$
z=\frac{106\pi-333}{355-113\pi}.
$$

The source bounds gave residual-floor ranges `[44,743]` at stage 17,
`[287,293]` at stage 25, and exactly `[292,292]` at stage 28. Thus rational
geometry certifies the complete next run `R^292` by a floor decision, before
reading those 292 future arrows. This is the sharper run-length interface,
consistent with the general escape deadline above.

## 9. Provenance, novelty and remaining obligation

The Euclidean source identity, strict interval bounds, endpoint convention and
productivity are established in the pinned
[Round-IV translation note](https://github.com/femboy2112/SUCC/blob/4e311d03e3ac9c3dbcbdc32477cd113f2ac0743b/research/2026-11-10/circle_line_lr_observer/LR_TRANSLATION.md).
The imported irrationality/transcendence theorems have explicit proofs in
[David H. Bailey's author-hosted paper](https://www.davidhbailey.com/dhbpapers/dhb-pi-trans.pdf).
No normality or transcendence theorem is inferred from an observed finite run.

Fixed-point descriptions of periodic continued fractions, interval separation,
and positive-matrix contraction are classical mechanisms. The local proof step
is their exact certificate assembly for this geometric source, including sharp
mixed-block contraction, minimal polynomials for parabolic cycles, prospective
escape deadlines, and correct output/witness indexing.

The result resolves every fixed proposed period in finite time and supplies
a computable deadline for each candidate. The companion `UNIFORM_BOUNDS.md`
separately imports an explicit classical transcendence measure to obtain an
astronomical bound uniform in polynomial height. Thus a uniform quantitative
separation theorem is available; the practical issue is the strength of its
rate, not its existence. The adaptive certificates here are much smaller in
the executed examples and make no claim of optimal complexity.

Neither result supplies an all-large-epochs signed statistic. A further
statistical theorem must control the selected observable with source, seed
and clocks retained. The finite-program/infinite-execution claim is fully
compatible with every emitted certificate being finite.

## 10. Independent audit of the staged producer

`cycle_independent_probe.py` independently reconstructs the prefix chart,
conjugated primitive polynomial, exact polynomial range, derivative bound,
root gap, and smallest positive escape count. Its matrix expectations use
integer tuples and its escape expectation uses a linear cylinder scan, rather
than the producer's matrix helpers and doubling/binary search. An in-memory
observer guard rejects any preparation that calls for an arrow beyond `N+p`.
All eight tested preparations emitted exactly `N+p` arrows.

The declared fresh inputs were `(2309,1)`, `(2371,7)`, `(3001,19)` and
`(4003,31)`, fixed with eight extra source refinements before their candidate
words were observed in this bearing. Known-region controls were `(0,4)`,
`(25,5)`, `(315,2)` and `(320,7)`. The new long-run case is particularly useful
for checking the distinction between output index and period-witness index:

| Start N | Period p | Candidate | Source stage | Smallest escape r | Predicted deadline B | Actual mismatch j | Witness j-p |
|---:|---:|:---|---:|---:|---:|---:|---:|
|2309|1|`L`|1036|386|2694|2693|2692|
|2371|7|`L^7`|1036|47|2699|2693|2686|
|3001|19|`LRRLRLRRRLRLRRLRLRL`|1295|2|3038|3020|3001|
|4003|31|`L^31`|1451|649|24121|24050|24019|

The first two fresh inputs unexpectedly lie in the same run; they are not
independent dynamical regions. All eight complete emitted prefixes matched
the preceding round's separate observer implementation, through 24,051
outputs. Both observers share the circle source, so this comparison checks
emission implementation and is not an independent proof of the source theorem.

The saved probe also passed 1,016 polynomial/matrix/width cases (all words of
lengths 1 through 7 on four Farey charts), 120 strict-equality escape controls,
four exact polynomial-range controls including an internal vertex with
positive endpoint values, three invalid-request controls, and two period
cases using the rotation source. The first exploratory invocation stopped
after the eight period cases because its fourth synthetic Farey chart had
its endpoints reversed. `Bracket` correctly rejected it. Correcting only
that fixture gave a passing synthetic suite; this history is retained in
`cycle_independent_receipt.json`.

The complete saved probe was then rerun successfully after the producer
tightened its integral-matrix validation. Its tested producer SHA-256 is
`07126c2f5ea63f7b40ea58a4d735f374abe19a4dc15952a9b2b0488d6e9fde72`;
the receipt also records the probe's own SHA-256. Reproduce from the artifact
directory with:

```sh
python cycle_independent_probe.py --output cycle_independent_receipt.json
```

No production fault was found in period preparation or rejection. These
executed checks corroborate the finite certificate interface. Its universal
totality remains the theorem proved above with its disclosed classical imports.
