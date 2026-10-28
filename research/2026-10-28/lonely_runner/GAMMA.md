# Gamma: a cubic speed bound for every two-entry modification

**Abstract.** Replace any two distinct speeds of `1,...,n-1` by integers
`n<=w1<w2`, where `n>=5`. We prove that an all-time cover at radius `1/n`
forces `w1<B_n` and `w2<=2(n-1)w1<4n^3`, where `B_5=56`, `B_6=60`,
and `B_n=(n-2)^2(n-1)/(n-4)` for `n>=7`. This supplies a polynomial
growth bound for the two-entry case of Zhang's Question 8.2, with arbitrary
deleted speeds. The proof combines the cover form of the established
one-entry classification, an explicit escape from a shared multiple,
rational endpoint spacing, and sharp periodic occupancy. Classical exact
deletion values improve the constant. The result gives complete finite
search bounds, without assuming the Lonely Runner Conjecture. Priority
of this unrestricted consequence remains under review.

**Status:** PROVED LOCAL on paper; exact implementation and 11 passing focused tests.
The full theorem below is not Lean-formalized. A stronger prior classification
was located for the **upper-half restriction**. The general two-deletion theorem
below removes that restriction by using Zhang's one-entry classification.
Academic priority of this unrestricted consequence is UNVERIFIED. The restricted
upper-half bound alone is an elementary alternative to the located prior result.
No general Lonely Runner Conjecture or complete tight-set classification is claimed.
Same-model adversarial reviews are correlated checks, not independent witnesses.

**Main theorem (GAMMA-05).** Let `n>=5`, `1<=r1<r2<=n-1` and
`n<=w1<w2` be integers. For
`V=([n-1]\{r1,r2}) union {w1,w2}`, with zero starting shifts, if
`LR(V)<=1/n`, then

\[
 \boxed{\quad
 w_1<B_n,\qquad
 w_2\le2(n-1)w_1,\qquad w_2<4n^3,
 \quad}
\tag{G5}
\]

where `B_5=56`, `B_6=60`, and
`B_n=(n-2)^2(n-1)/(n-4)` for every `n>=7`.
An even stronger bound for a specified deleted pair is given in (G5d).

Thus **every fixed n has an explicit complete finite search domain** for all
two-entry tight modifications, without a bound imposed on the deleted speeds
or an assumed Goddyn–Wong criterion. Section 6 proves the unrestricted theorem.
Sections 2–5 provide its elementary geometric ingredients and a sharper bound
in the upper-half regime. This is a growth theorem, not a classification of the
surviving tight sets and not a new numerical exception.

## 1. Upper-half refinement and exact scope

Let `n,r1,r2,w1,w2` be integers satisfying

\[
 n\ge5,\qquad {n-1\over2}<r_1<r_2\le n-1,
 \qquad n\le w_1<w_2.
\]

Put `S=[n-1]\{r1,r2}`, `V=S union {w1,w2}`, and

\[
 \operatorname{LR}(V)=\max_{t\in[0,1]}\min_{v\in V}\|vt\|,
 \qquad \|x\|=\min_{k\in\mathbb Z}|x-k|.
\]

All shifts are zero. There are `n-1` moving speeds in V. Write `s=n-r1`.

**Theorem GAMMA-04.** If `LR(V)<=1/n`, then

\[
 \boxed{\quad
 w_1< {2(n-2)r_1(n-1)\over (n-4)(n-r_1)},
 \qquad w_2\le2(n-1)w_1,
 \qquad w_2<4n^3.
 \quad}
\tag{G4}
\]

In particular every tight set in this family satisfies these bounds. No
Goddyn–Wong gcd criterion is assumed. The proof even permits the hypothetical
case `LR(V)<1/n`; it does not invoke the Lonely Runner Conjecture to exclude it.

The main structural step is that **one inserted speed never covers the region
left by these two deletions**, including when that speed is a common multiple
of both removed speeds. The second step uses exact spacing of actual source
endpoints, not a numerically estimated gap. The final step controls the smaller
inserted speed by periodic interval occupancy.

## 2. Source-faithful safe intervals

For `r in {r1,r2}`, no retained speed is a multiple of r: every original speed
is strictly between 0 and `2r`, and the sole possible multiple r was removed.
Therefore at `t=1/r` every retained speed has distance at least `1/r`.
The circle-distance function is 1-Lipschitz, so for any retained i,

\[
 \|i(1/r+u)\|\ge {1\over r}-(n-1)|u|.
\]

Consequently the open interval

\[
 J_r=\left({1\over r}-a_r,{1\over r}+a_r\right),
 \qquad a_r={n-r\over nr(n-1)},
\tag{G0}
\]

lies in the region where **all** retained speeds exceed `1/n`. It is contained
in `(0,1)`. Its length is `2a_r`. The strictness is only at the open endpoints;
measure computations are unaffected by these two points.

The familiar centre divisibility condition follows: if `LR(V)<=1/n`, then for
each removed r, at least one of `w1,w2` is divisible by r. This does **not**
imply a distinct assignment of inserted speeds to removed speeds. The common
multiple possibility must be treated, and is treated next.

## 3. GAMMA-01: a strict hole after any single insertion

**Theorem.** For every integer `w>=n`,

\[
 \operatorname{LR}(S\cup\{w\})>{1\over n}.
\tag{G1}
\]

Moreover a rational witnessing time can be constructed by the following cases.

**Nonmultiple case.** If some removed r does not divide w, then at `t=1/r`
the inserted speed also has distance at least `1/r>1/n`. This is the witness.

**Common-multiple case.** Suppose both removed speeds divide w. Let

\[
 g=\gcd(r_1,r_2),\quad r_1=ga,\quad r_2=gb,
 \quad \gcd(a,b)=1,\quad a<b.
\]

Then `w>=lcm(r1,r2)=b r1`. Since `r2<=n-1`,

\[
 b(n-r_1)=bn-a r_2
 \ge (b-a)n+a>n-1.
\tag{G1a}
\]

Thus `1/(nw)<a_(r1)`. Choose a rational displacement satisfying

\[
 {1\over nw}<u<
 \min\left(a_{r_1},{n-1\over nw}\right).
\tag{G1b}
\]

The interval is nonempty: its first upper bound was just proved larger than
the lower bound, and its second is larger because `n>2`. Take its midpoint.
The time `t=1/r1+u` lies in the retained safe interval. Meanwhile `w/r1` is
an integer and

\[
 1/n<wu<1-1/n,
\]

so the inserted runner is also strictly farther than `1/n` from every integer.
This proves (G1), with an exact rational witness. QED.

The upper restriction `(n-1)/(nw)` is essential: the entire rest of the safe
interval need not avoid subsequent bad bands of a very large common multiple.
The proof chooses a point immediately after the central bad band and before
the next one. It does not assume that one band is the only band on all of J.

## 4. GAMMA-02: exact endpoint spacing bounds the second speed

Set `W=S union {w1}` and let `U_W={t in (0,1): ||vt||>1/n for every v in W}`.
By GAMMA-01, U_W is nonempty. It is a finite union of open intervals: its
complement is the finite union of source-labelled closed bands

\[
 \left[{nk-1\over nv},{nk+1\over nv}\right]\cap[0,1],
 \qquad v\in W, k\in\mathbb Z.
\]

Every component `(a,b)` of U_W has both endpoints in `(0,1)`, because 0 and 1
have neighborhoods covered by the bad bands. Each endpoint is an actual
source endpoint `(nk +/- 1)/(nv)` for some v in W.

**Lemma.** Every such nonempty component has

\[
 b-a\ge {1\over n w_1(n-1)}.
\tag{G2a}
\]

**Proof.** If the endpoints come from distinct velocities u,v, their positive
difference is a positive integer divided by `nuv`; the shared factor n is
cancelled before the denominator is estimated. There is only one velocity
larger than `n-1`, namely w1, so `uv<=w1(n-1)`. If both endpoints come from
the same velocity v, their difference is a positive integer divided by nv,
and `v<=w1`; this is an even larger lower bound. This explicitly handles
the case when both endpoint labels equal w1. QED.

If `LR(V)<=1/n`, the whole connected interval `(a,b)` must lie in the bad set
of w2 alone. Its bands are disjoint because `1/n<1/2`; a connected interval
cannot jump across their positive gaps. Therefore

\[
 b-a\le {2\over nw_2}.
\]

Together with (G2a), this proves

\[
 w_2\le2(n-1)w_1.
\tag{G2}
\]

No uncomputed positive margin or numerical precision assumption enters this
bound. It follows from source endpoints and a proved existence of a hole.

## 5. GAMMA-03: sharp periodic occupancy and the smaller speed

For positive integer w define `B_w={t: ||wt||<=1/n}` and put `alpha=2/n`.
For every real interval J of length ell,

\[
 |B_w\cap J|\le {2\ell\over n}
                  +{2(n-2)\over n^2w}.
\tag{G3a}
\]

**Proof.** Rescale by w and write `w ell=m+u`, where m is a nonnegative integer
and `0<=u<1`. Every full period contributes alpha. The remaining arc of length
u on the unit circle meets the bad arc in measure at most `min(u,alpha)`.
Hence the discrepancy from `alpha*(m+u)` is at most

\[
 \min(u,\alpha)-\alpha u\le\alpha(1-\alpha).
\]

Divide by w. The constant is sharp for an interval consisting of one complete
bad band, whose length is `alpha/w`. No limit in w or averaging over phases
is used. QED.

Use `J=J_(r1)` from (G0), of length

\[
 \ell={2(n-r_1)\over nr_1(n-1)}.
\]

If the final speeds cover at level `1/n`, their two bad sets cover J. By (G3a)
and the union bound,

\[
 \ell\le{4\ell\over n}
   +{2(n-2)\over n^2}\left({1\over w_1}+{1\over w_2}\right)
 <{4\ell\over n}+{4(n-2)\over n^2w_1}.
\]

The last inequality uses `w2>w1`, and `n>4` permits rearranging. Substituting
ell gives the **strict** first bound in (G4).

Since `r1<=n-2`, also `r1/(n-r1)<=(n-2)/2`. Thus

\[
 w_1<{(n-2)^2(n-1)\over n-4}<2n^2.
\]

The final strict inequality is equivalent to

\[
 2n^2(n-4)-(n-2)^2(n-1)
 =(n-5)(n^2+2n+2)+14>0.
\]

Combine this with (G2) to obtain `w2<4n^2(n-1)<4n^3`, proving GAMMA-04.

## 6. GAMMA-05: remove the upper-half restriction

The new hypothesis for this section is only
`n>=5`, `1<=r1<r2<=n-1`, `n<=w1<w2`. Retain `S=[n-1]\{r1,r2}`.

### 6.1 The cover form of Zhang's one-entry classification

For `T_r=([n-1]\{r}) union {w}`, `w>=n`, the proof of Zhang's Theorem 1.2
establishes the following stronger formulation:

> If `LR(T_r)<=1/n`, then either r lies in the upper half and `w=mr`
> satisfies the Goddyn–Wong gcd condition, or
> `(n,r,w)=(5,2,7)` or `(6,2,9)`.

This is not inferred merely by replacing equality in the theorem's statement.
Here is the proof audit needed to justify the cover formulation:

* For `2r>n-1`, the centre argument in Lemma 2.4 uses only the assumption
  `LR<=1/n` to force `r|w`. Goddyn–Wong's Theorem 2.3 (Zhang's Theorem 1.1) gives `LR>=1/n`
  for this multiple replacement, so the cover is an equality case and its
  gcd condition follows.
* For `r=1`, every w is an integer multiple of r. The same Goddyn–Wong
  theorem gives `LR>=1/n`, while the gcd condition fails because every
  integer is coprime to 1; hence no cover is possible.
* For `3<=r<=(n-1)/2`, the contradiction in Zhang's Proposition 3.4 uses
  only coverage of `U(n,r)` by the inserted bad set, through Lemma 2.2,
  the component-length bound, and the conflicting window inequalities.
  Lemma 2.2 itself explicitly assumes `LR<=1/n`, so no unproved Lonely
  Runner lower bound is used in this case.
* For `r=2`, Proposition 3.5 likewise uses only shell coverage, its endpoint
  and length constraints, and an explicit point excluding the remaining
  candidates. Exactly the two listed sporadic cases remain.

These cases exhaust all r. Thus the stated cover-form implication follows
from the cited proofs, including their required domains, rather than from
an unstated conjecture about equality versus strict counterexamples.

### 6.2 No single insertion covers after any two distinct deletions

**Lemma.** For all such n,r1,r2 and every `w>=n`,

\[
 \operatorname{LR}(S\cup\{w\})>1/n.
\tag{G5a}
\]

**Proof.** Suppose the contrary. Adding either missing original speed keeps
the cover property, so both one-entry sets `T_(r1)` and `T_(r2)` have
`LR<=1/n`. Apply the cover classification just justified. If both removed
speeds lie in the upper half, GAMMA-01 already contradicts the supposed
cover, including its common-multiple case.

Otherwise one removal must be r=2 in a sporadic case. If `(n,w)=(5,7)`,
the other removal cannot be 1 and the only upper-half possibilities are
3 and 4, neither dividing 7; there is no second cover. If `(n,w)=(6,9)`,
the other removal is 1 or one of 3,4,5. The first is excluded; 4 and 5
do not divide 9. At r=3 the multiplier is m=3 and `n-r=3`; the required
gcd condition includes the integer 4 in `[3,8]`, but `gcd(3,4)=1`.
Thus that cover is impossible too. This exhausts both sporadic cases. QED.

This finite use of the two sporadic cases is exact and complete. It is not
an extrapolation from a census. The lemma allows r1=1 or r2=n-1.

### 6.3 Source endpoints and density give the bound

The retained-only uncovered region `U_S` is nonempty. Indeed, `r1<=n-2`,
and the deleted-speed witness in ALPHA-01 gives
`LR([n-1]\{r1})>=2/(2n-3)>1/n`; deleting r2 cannot reduce the minimum.
Choose a component J of `U_S`. Its endpoints come from baseline source
velocities at most `n-1`. The same endpoint argument as in Section 4 gives

\[
 \ell=|J|\ge{1\over n(n-1)^2}.
\tag{G5b}
\]

For different endpoint velocities u,v, cancel the shared n before using
`uv<=(n-1)^2`; for the same velocity the denominator is only nv. Every
source has a positive bad neighborhood of 0 and 1, so a component cannot
acquire an unaccounted boundary endpoint there.

If the two inserted speeds cover J, the sharp periodic estimate (G3a)
and `w2>w1` imply

\[
 \ell(1-4/n)<{4(n-2)\over n^2w_1}.
\]

Use (G5b) and `n>4` to obtain the preliminary bound
`w1<4(n-2)(n-1)^2/(n-4)`.
By (G5a), `U_(S union {w1})` also has a nonempty component. Its endpoint
spacing is exactly as in Section 4: there is at most one velocity above
`n-1`. Thus that argument gives `w2<=2(n-1)w1` without any restriction
on the positions of the removed speeds.

Finally,

\[
 2n^2(n-4)-(n-2)(n-1)^2
 =(n-5)(n^2+n)+2>0,
\]

so the preliminary bound is strictly below `8n^2`, already giving
`w2<16n^3`. The next step sharpens it using Alpha's exact source margin.

### 6.4 Alpha's exact deletion margin improves the cubic constant

Let

\[
 \mu=\max\bigl(L(n,r_1),L(n,r_2)\bigr).
\]

These are the exact classical deletion values proved in ALPHA-02. At a rational
maximizing time t0 for the larger value, the retained minimum `f_S(t0)` is at
least mu, because S is contained in each one-deletion speed set. The function
f_S is `(n-1)`-Lipschitz. Thus its safe region contains the open interval

\[
 \left(t_0-{\mu-1/n\over n-1},\quad
       t_0+{\mu-1/n\over n-1}\right).
\tag{G5c}
\]

This interval does not wrap around 0: `f_S(0)=0` and circle Lipschitz continuity
give `dist(t0,Z)>=mu/(n-1)`, larger than the displayed radius. Apply (G3a) to
its length `2(mu-1/n)/(n-1)` to obtain the parameter-dependent refinement

\[
 \boxed{\quad w_1<
 {2(n-2)(n-1)\over n(n-4)(\mu-1/n)}.\quad}
\tag{G5d}
\]

Since `r1<=n-2`, ALPHA-03 supplies
`mu>=m_n`, where `m_5=2/7`, `m_6=2/9`, and `m_n=1/(n-2)` for `n>=7`.
Substituting these exact values into (G5d) gives precisely the displayed B_n.
For `n>=7`, the polynomial identity at the end of Section 5 gives `B_n<2n^2`,
so `w2<4n^3`. At n=5 the sharper second bound is `w2<8*56=448<500`;
at n=6 it is `w2<10*60=600<864`. This completes the strongest form of
GAMMA-05. QED.

**Dependencies.** This unrestricted extension uses the classical one-entry
classification, Alpha's exact values and sharp minimum, and the elementary source
endpoint and periodic occupancy lemmas. It does not use the externally located
two-entry upper-half classification as a proof dependency.

## 7. Effective completion of the finite search domain

For each fixed n and upper-half pair, define

\[
 B={2(n-2)r_1(n-1)\over(n-4)(n-r_1)},\qquad M_1=\lceil B\rceil-1.
\]

Every tight candidate lies in the completely proved finite domain

\[
 n\le w_1\le M_1,\qquad
 w_1<w_2\le2(n-1)w_1.
\]

`effective_bounds` computes the ceiling exactly, including integer B. Centre
divisibility provides an additional safe filter. The all-time interval checker
then decides `LR<=1/n`, while the complete breakpoint theorem decides equality.
For arbitrary deletions use the stronger B from (G5d), or the uniform B_n,
and the same ceiling and second-speed formulas. `general_effective_bounds`
implements the parameter-dependent bound and reports the uniform and
endpoint-only bounds separately for audit.
This is a **complete finite reduction for every fixed n and every pair of
deleted speeds**, not an enumeration result for all n and not a proof that
all surviving sets satisfy the Goddyn–Wong condition.

The known examples `n=74`, deletions `{70,72}`, replacements `{140,144}`, and
`n=284`, deletions `{280,282}`, replacements `{560,564}`, satisfy the bounds
and are replayed by exact full-circle interval coverage. They are prior-art
positive controls, not newly discovered exceptions.
The additional hostile positive control `n=5`, `R={1,3}`, `W={6,8}` gives
`V={2,4,6,8}=2*[4]` and is tight at `1/5`. Its speed gcd is 2. No primitive
gcd-one assumption is imposed or silently introduced; it lies outside the
upper-half regime and must survive the unrestricted theorem and checker.

## 8. Prior art and unresolved priority

The fixed primary source is [Zhang, arXiv:2608.13599v3](https://arxiv.org/html/2608.13599v3).
The complete text was read during Alpha and Sections 5–6 plus Questions 8.1–8.2
were re-read for this derivation. Lemma 5.3 supplies the centre divisibility
observation; Corollary 5.4 bounds speeds under individual Goddyn–Wong hypotheses.
Lemma 6.1 uses a weaker periodic occupancy slack. Theorem 6.10 is a finite census
with `w2<=8n`. Questions 8.1–8.2 ask about classification and bounds beyond those
conditions. Our proof obtains a cubic bound in the stated upper-half two-deletion
regime without assuming the gcd criterion and without extrapolating the census.

[Goddyn and Wong, Integers 6 (2006), A38](https://zenodo.org/records/8275490)
is the primary multi-acceleration source. Its theorem supplies positive examples;
our bound does not depend on its necessity or sufficiency. The missing converse
and simultaneous accelerations are discussed in its Section 3. Their work retains
priority for those constructions.

The downloaded Goddyn–Wong PDF from Zenodo has SHA-256
`dc9b2a9a8fd9849ee5f05664b83899df83b8ab23a622300625e50465cf463197`.

The priority search located a stronger prior classification:
[JenW1N, Conjectures.io source04 result](https://conjectures.io/results/4c651db1-3b53-48da-ac31-0b0020a8d87c),
verified 7 October, approved 8 October and certified 9 October 2026 according
to the site's primary record. The accepted source states that every tight
two-entry modification in this same upper-half regime has the individual
Goddyn–Wong conditions in one of the two matchings. Combined with Zhang's
growth theorem, it gives the stronger `O(n log n)` bound here. The downloaded
Lean source has SHA-256
`a1aad65e807a968e03cf186b80a17a399b234ea13d725b42d188cc45814957bd`.
The integration literature audit records the statement-level check; this run
does not claim a local kernel replay of that external 6,500-line proof.

Accordingly (G4) is retained as a direct, short, independently inspectable
argument handling the common-multiple case, not presented as a first answer
to the restricted question. The unrestricted (G5) goes beyond that result's
upper-half domain and yields a polynomial growth bound for all two-entry
modifications. Its academic priority remains unverified; the literature audit
must not conflate the two scopes. General two-entry classification and growth
for arbitrary numbers of modifications remain open obligations here.

## 9. Tests, countermodels, and claim ledger

The implementation is `observational_succ/lonely_runner_two_entry.py`; the focused
suite is `tests/test_lonely_runner_two_entry.py`. The final focused replay
passed **11 tests in 3.120 seconds**. Tests check:

* all three one-insertion witness branches over a bounded exact sweep, including
  a common multiple multiplied by `10^40`;
* safe intervals, exact component endpoints and their minimum spacing;
* the sharp occupancy constant and a counterexample to dropping its boundary term;
* the known tight positive controls at n=74 and n=284;
* the nonprimitive low-deletion tight set `{2,4,6,8}` at n=5;
* arbitrary deletion pairs, the n=8 sporadic two-entry set, and every second
  deletion accompanying either sporadic one-entry exception;
* exact strict-to-integer bounds and the cubic algebra;
* incorrect source domains, floating inputs, and exhausted enumeration budgets.

The deterministic finite receipt is
`research/2026-10-28/lonely_runner/receipts/gamma.json`. Replay it without mutation:

```sh
python scripts/lonely_runner_two_entry_probe.py --verify research/2026-10-28/lonely_runner/receipts/gamma.json
```

The probe defaults to JSON stdout and accepts `--output` for an arbitrary fresh
path. Its exact rational controls and bounds are replay evidence, not a kernel
proof of the universal result. It preserves the distinction between unrestricted
priority, the stronger previously published upper-half classification, and local
finite verification.

The strongest bound explicitly imports the proved classical Alpha formula;
the general Lonely Runner Conjecture is not assumed. `uncovered_intervals`
independently enumerates the actual source bands,
whereas `single_insert_hole` uses the analytic construction. Finite sweeps test
these implementations; Sections 2–6 prove the universal statements.

**Hostile scope controls.** The upper-half hypothesis is essential to the centre
argument: the known tight set `{1,4,5,6,7,11,13}` removes 2 and 3 at n=8, and
neither replacement is divisible by 2. That is a countermodel to extending the
centre filter, not a countermodel to the proved broader cubic bound. Shifted
starting positions likewise invalidate the exact unshifted centres and endpoint
grid. The assumption `n>4` is required by this density argument; its failure
does not itself establish a counterexample at smaller n.

| Claim | Scope | Verdict | Next falsifier |
|---|---|---|---|
| GAMMA-01 | Every single insertion w>=n after two upper-half deletions | PROVED LOCAL, rational witness | Shared multiple with extreme speed and gcd |
| GAMMA-02 | Any genuine gap after one insertion has width at least `1/[nw(n-1)]` | PROVED LOCAL, source-endpoint proof | Both endpoints from the inserted speed |
| GAMMA-03 | Periodic occupancy with sharp slack `2(n-2)/(n^2w)` | CLASSICAL ELEMENTARY estimate rederived | A full bad band saturates the constant |
| GAMMA-04 | All-time covers in the exact family obey (G4) | PROVED LOCAL on paper; stronger prior classification located | Independent measure and endpoint audit |
| GAMMA-X1 | Ignore the common-multiple assignment case | INVALID proof route | Explicit common-multiple escape branch |
| GAMMA-X2 | Use density alone with zero boundary slack | REFUTED | One short complete bad band |
| GAMMA-05 | All two-entry covers, arbitrary distinct deletions, obey (G5) | PROVED LOCAL on paper using Zhang cover classification; priority UNVERIFIED | Audit strict-cover versus equality distinction and both sporadic cases |
| GAMMA-X3 | Infer all tight sets are Goddyn–Wong from the cubic bound | UNPROVED; false without a restricted classification | The n=8 middle-range sporadic example must survive |

No Lean theorem presently exports GAMMA-01–05. A next formalization target is the
common-multiple witness, followed by exact source-endpoint spacing; the occupancy
argument needs genuine finite-union length or measure semantics. Arithmetic-only
formalization must not be advertised as a kernel proof of the full cubic theorem.
