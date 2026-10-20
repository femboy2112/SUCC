# Academic Main VII: independent hostile referee

Status: **PROVED LOCAL** for the elementary derivations below; **TESTED MODEL**
for finite controls. This is an independently tasked internal agent of the same
model family, not an external referee or independent formal kernel. It is a
new-to-project audit, not a claim of academic novelty.

## Pinned historical replay

The unchanged `scripts/cloud_hostile_holdouts.py` was actually executed in fresh
Python processes against clean detached checkouts, using Python 3.12.14,
SymPy 1.14.0 and NumPy 2.5.4. The adjacent raw JSON receipts contain all four
target source SHA256 hashes and the exact outputs. They are historical receipts,
not evidence about the final integrated tree.

| Finding | PR #201 `cbc4010458c00be995b8af3f229c9bba410301e2` | PR #209 `3e1ef648896821321423e6642f1de4a458a0c791` |
|---|---|---|
| F01 source-authentic flag contradicts synthetic witness | STILL EXPOSED | STILL EXPOSED |
| F02 mutation supplies an unsupported proved status | STILL EXPOSED | STILL EXPOSED |
| F03 dependency metadata contradicts the quantifier prefix | STILL EXPOSED | STILL EXPOSED |
| F04 nonexistent theorem reference supplies proof backing | STILL EXPOSED | STILL EXPOSED |
| F05 shallow negative cone lacks rational witness | STILL EXPOSED | FIXED |
| F06 rational prime cutoff returns a false enclosure | STILL EXPOSED | STILL EXPOSED |
| F07 whole exponent tail is attributed to BBLT's small remainder | STILL EXPOSED | STILL EXPOSED |
| F08 twin constant is identified with every even singular series | STILL EXPOSED | FIXED, with the qualification below |
| F09 float ordering returns the larger exact eigenvalue | STILL EXPOSED | STILL EXPOSED |

F08's original automated oracle only looks for a stale string and returned
`source_review_required` at #209. Reading the actual corrected formula establishes
the original defect is fixed: `S(N)=2*C2*prod_{p|N,p odd}(p-1)/(p-2)`. A new
documentation defect remained in the following sentence: “only in the limit”
overlooks exact equality at every positive power of two. The exactness lane was
notified and repaired that sentence. This does not invalidate the corrected
Euler-factor formula.

The nine reproductions, expected/actual values, mathematical explanations and
original claim scope remain in the cloud F dossier and the raw receipts. In
particular F09 returns `10^30+3` in both old heads, whereas the true minimum is
`10^30+1`; the vector `(1,-1)` gives shifted quadratic form `-4`. F06 returns
`[1/3,1]` although the independently derived lower bound is `135/128>1`.

`main_vii_hostile_replay.py --require-fixed` is the repaired-head gate. An exposed
historical bug is never counted as a successful repaired regression. Exceptions
are not automatically success: unexpected import/API failures are **INVALID
TEST**, and unknown outcomes are **NEW FAILURE**. An unreviewed documentation
oracle is **INAPPLICABLE**, not silently green. Formal/source authority is
separately challenged by `test_main_vii_authority_holdout.py`.

### Repaired combined-head replay

The exact combined commit `0b0306544c31fa8af04c52868b2af5a35d6b60ee` was checked
out into a separate clean detached worktree and the same nine fixtures replayed.
All nine are **FIXED**, with exact observed outputs and source hashes in
`repaired-0b030654-replay.json`. The first classifier run treated the intentional
`GoldbachCircleError` domain rejection as **INVALID TEST**, because the adapter
only listed its standard `ValueError` parent by name. That initial receipt is
preserved. The adapter was repaired to recognize this documented domain
exception; the production test and mathematical expectation were unchanged.

The separate authority holdout also passed on this exact combined head. It
checks all 125 symmetric 2-by-2 integer matrices with entries from -2 to 2 against
the independent principal-minor criterion; exact matrix/dimension/predicate
binding; negative-witness binding; deep input snapshotting; rational domains;
subclass-verifier rejection; forged successful JSON; and closed callback
registration. A mandatory additional control uses the actual archived
`formal/mathlib_bridge/axiom_audit.json` and confirms it cannot authorize the
English assertion that RH is true. Archived receipt contents alone have no
authority. A genuine positive formal-reference test is **INAPPLICABLE** at this
commit: the reviewed build catalogue is intentionally empty pending the actual
hosted Lean build. That pending positive gate is not reported as verified.

The exactness lane's additional prime-cutoff defect was independently reproduced
at #209: `singular_series_via_transport(2,2)=3/2`, but the direct finite product is
`singular_series_truncated(2,2)=2`. Its repair keeps the actual requested prime
range and is separate from the nine historical findings. No claim of exhaustive
absence of certification defects is made from this finite hostile suite.

### Actual formal admission holdout

After the coordinator authenticated the actual hosted Lean build, the separate
`test_main_vii_admitted_formal_holdout.py` gate ran successfully: six tests,
including positive typed claims for all ten admitted theorem exports. The
record's canonical SHA256 is
`9de79bcbe52c79f1829361c611d97a77b82dc08d9a5fe6181931b78865c8a9f4`.
All 15 checked-source hashes match the installed files. The test does not
patch the catalogue, install a test checker, or fabricate positive admission.
Missing admission is an error, never a silently skipped positive gate.

Using that same real record, the actual Mason–Stothers and polynomial Fermat
propositions verify; exchanging them does not. An English RH assertion does
not verify. Changing a claim's type, forging matching claim/evidence types,
changing names/toolchain/dependency/environment, using an unqualified name,
or modifying the receipt's type, recomputed type hash, axioms, universe
parameters, or build commit all fail authority checks. The receipt
`admitted-formal-holdout.json` records exact content hashes and the genuine
kernel commit/tree. It honestly marks the installed worktree dirty because
admission was then awaiting the coordinator's commit; it is not a final
combined-commit CI receipt. The coordinator still owns that final gate.

This resolves the earlier **INAPPLICABLE** positive test at `0b030654` for
the subsequently admitted content, without rewriting that historical result.
Level D source identification remains unavailable. No English mathematical
claim is authenticated merely because its label names a real theorem.

## Reconstruction of the primitive moment theorem

Let `X>=2` be real, let `a,b` be positive integers, `c=a+b<=X`, and impose
`gcd(a,b)=1`. Write `H=abc/rad(abc)`. The following reconstruction starts from
these definitions; the finite controls import no production arithmetic code.

**Reduced slopes.** For pairwise coprime positive integers `d,e,f`, restrict to
`d|a,e|b,f|c`, and put `D=def`. Since `gcd(a,c)=1`, a reduced slope `a/c`
identifies its pair `(a,c)`. For two distinct pairs the determinant
`a'c-ac'=a'b-ab'` is nonzero. The first expression is divisible by `d` and
`f`; the second by `e`. Pairwise coprimality gives divisibility by `D`. Ordered
slopes therefore have successive distances at least `D/X^2`. Their interval is
contained in `(0,1)`, so `N_X(d,e,f)<=1+X^2/D`. This geometric proof uses neither
CRT density nor an asymptotic estimate. For `D<=X^2` it implies `N<=2X^2/D`.
For `D>X^2` the singleton remains essential.

**Positive expansion.** Möbius inversion of `f_t(n)=H(n)^t` gives a multiplicative
`g_t` with `g_t(1)=1`, `g_t(p)=0`, and
`g_t(p^k)=p^{t(k-1)}-p^{t(k-2)}` for `k>=2`. For `t>=0` it is nonnegative and
supported on powerful integers (with only 1 surviving when `t=0`). If `g_t(d)>0`
and `d|n`, then `d<=ris(d)^2<=ris(n)^2`: prime by prime, `k<=2(k-1)` for `k>=2`.
The three divisor variables are pairwise coprime, because the primitive triple
is pairwise coprime. Hence an occupied product `D` satisfies `D<=H^2`.

**Low weights.** On `H<=X`, only `D<=X^2` occurs. It is valid to discard the
condition `H<=X` only *after* imposing this product cutoff. The slope bound then
gives at most `2 X^2 E_3(t)`, where

\[
 E_3(t)=\prod_p(1+3A_p(t)),\qquad
 A_p(t)=\frac{p^t-1}{p^2(1-p^{t-1})}.
\]

This product converges for `0<=t<1`; the factor 3 records exclusive occupation
of the three slots, not an additive/multiplicative convolution interchange.

**High weights.** For `eta>0` the positive Euler product

\[
 C_\eta=\sum_{(m,n)=1}\frac{(mn)^{-\eta}}{\operatorname{rad}(m)\operatorname{rad}(n)}
 =\prod_p\left(1+\frac{2}{p(p^\eta-1)}\right)
\]

converges. A coprime ordered pair with `m,n<=X` and `rad(m)rad(n)<=R`
contributes at least `X^{-2eta}/R`; hence its count is at most
`C_eta R X^{2eta}`. If `H>y`, then `rad(abc)<X^3/y`, and one of the three
slot-pair radical products is at most `X^2 y^{-2/3}`. Each chosen slot pair
determines at most one triple. Thus
`T_X(y)<=3 C_eta X^{2+2eta} y^{-2/3}`.

The finite layer-cake formula gives, for `0<t<2/3`,

\[
 \sum_{H>X}H^t
 =X^tT_X(X)+t\int_X^\infty y^{t-1}T_X(y)\,dy
 \le\frac{2C_\eta}{2/3-t}X^{2+2\eta+t-2/3}.
\]

At `t=0` the sum is `T_X(X)` directly. Choosing `eta=(2/3-t)/2` proves the
claimed uniform quadratic bound with
`K_t=2E_3(t)+2C_eta/(2/3-t)`. All constants depend on `t` alone.

**Density and mean.** At an occupied prime power `p^k` the triple divisibility
condition and primitivity have two-variable density `p^{-k}(1-1/p)`; at an
unoccupied prime the density is `1-1/p^2`. Fixed-prime CRT gives their finite
product. After normalizing by `X^2`, the missing-common-prime tail is at most
`(1/2)sum_{p>P}p^{-2}`: a triple with common prime `p` has at most
`X^2/(2p^2)` pairs. Taking `X` to infinity for fixed `P`, then `P` to infinity,
gives

\[
 \lim_{X\to\infty}\frac{N_X(d,e,f)}{X^2}
 =\frac1{2\zeta(2)D}\prod_{p\mid D}\frac p{p+1}.
\]

For `t<s<2/3`, truncating each divisor at `L` omits nothing when `H<=sqrt(L)`;
the omitted positive weight elsewhere is bounded by
`H^t <= L^{-(s-t)/2}H^s`. The `s`-moment controls this uniformly in `X`.
Fixed finite sums can therefore pass to the density limit, followed by increasing
`L`. The resulting constant is

\[
 C_t=\frac1{2\zeta(2)}\prod_p
 \left(1+\frac{3p}{p+1}A_p(t)\right).
\]

This verifies the required order of limits and the stronger-moment input.
An Euler product converging for `t<1` does not extend this theorem past `2/3`.
The proof has survived this reconstruction; it is not a proof of integer abc.

## Independent audit of the effective-rate candidate

This subsection was derived in response to the arithmetic lane's proposed
statement, before reading its implementation. It supplies a second derivation
and exact arithmetic controls, not a new independent external referee.

For arbitrary pairwise coprime `d,e,f` and real `X>=0`, count the *nonprimitive*
points by `a=d u`. For fixed `u`, the admissible positive `b` occupy one class
modulo `ef`. Their count differs from `(X-du)/(ef)` by less than 1. Write
`m=floor(X/d)` and `r=X/d-m`. The exact floor-sum defect is

\[
 \frac{X^2}{2d}-\sum_{u=1}^m(X-du)=\frac d2(m+r^2)\in[0,X/2].
\]

Consequently the raw lattice count has error at most
`X/d+X/(2ef)<=3X/2`, uniformly even when a modulus exceeds `X`.

Use the *full* Möbius sum over `k<=M=floor(X/2)`. The reduced moduli are
`d/gcd(d,k),e/gcd(e,k),f/gcd(f,k)` and remain pairwise coprime. Their product
is `D/gcd(D,k)`. Summing the raw errors gives `(3/2)X H_M`. The absolutely
convergent main coefficient is

\[
 \sum_{k\ge1}\frac{\mu(k)\gcd(D,k)}{Dk^2}
 =\frac1{\zeta(2)D}\prod_{p\mid D}\frac p{p+1}=\rho_D.
\]

Because `gcd(D,k)/D<=1`, its tail beyond `M` is at most `1/M`. Thus

\[
 |N_X-\rho_DX^2/2|
 \le\tfrac32X H_M+\frac{X^2}{2M}
 \le\tfrac72 X(1+\log X),\quad X\ge2.
\]

There is no hidden modulus dependence. Restricting Möbius to `(k,D)=1` is
invalid: the exact control `(X,d,e,f)=(12,2,1,1)` returns 28 instead of 14.

For `t>=0`, `alpha>t`, `2alpha-t>1`, the weighted divisor sum is

\[
 E(t,\alpha)=\prod_p\left(1+
  \frac{3(p^t-1)p^{-2\alpha}}{1-p^{t-\alpha}}\right)<\infty.
\]

On the product cutoff `D<=Y`, its unnormalized mass is at most
`Y^alpha E(t,alpha)`. The omitted weight is at most
`K_s Y^{-(s-t)/2}X^2` by `D<=H^2`. The limiting omitted constant obeys the same
bound, by positivity and the already established mean. Therefore

\[
 |S_t(X)/X^2-C_t|
 \le \tfrac72E(t,\alpha)Y^\alpha\frac{1+\log X}{X}
     +2K_sY^{-(s-t)/2}.
\]

Choose `0<h<2/3-t`, `s=2/3-h`, `alpha=(1+t+h)/2`, and
`Y=(X/(1+log X))^{6/5}`. Then `alpha+(s-t)/2=5/6`, and the error is at most

\[
 \left[\tfrac72E(t,\alpha)+2K_s\right]
 \left(\frac{1+\log X}{X}\right)^{(2-3t-3h)/5}.
\]

Thus every positive pure-power exponent `delta<(2-3t)/5` is available after
absorbing the logarithm into a constant depending on `t,delta` and the chosen
slack. The endpoint is not included. The rate derivation survives this audit.

## Exact controls and boundaries

`main_vii_arithmetic_holdout.py` imports no SUCC arithmetic implementation. It
generates reduced slopes by the neighboring-Farey recurrence, cross-checks that
set against direct gcd enumeration, checks signed consecutive determinants,
and computes the integer first moment using trial-division radicals. The full
run checks 8,398 slope cases, 17,784 raw lattice cases at integer and half-integer
cutoffs, 8,398 full Möbius identities, and 600 Möbius-inverted divisor expansions.
The raw census and its hash are in `arithmetic-holdout.json`.

The `t=1` integer census is an exact finite identity control only; it lies
outside the moment theorem's range and makes no bounded-mean claim. The
powerful singleton `(441,400,841)` falsifies deletion of the slope singleton:
`D=148352400>X^2=841^2`. At `t=2/3` the stated high-tail integral diverges;
that is a demonstrated boundary of this estimate, not a counterexample to the
endpoint moment theorem. Removing primitivity also invalidates the theorem:
triples `(n,n,2n)` have `ris(2n^3)>=n^2`, so their moment grows faster than `X^2`
when `t>1/2`.

No claim here depends on BBLT's exceptional-set theorem. The exact divisor
expansion, Farey geometry, Möbius density and lattice slicing are classical
ingredients. Academic novelty remains unverified; external literature review
and an external mathematical referee remain required before publication.
