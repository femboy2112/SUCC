# Alpha: a sharp corollary for one deleted speed

**Status:** proved on paper; classical exact formula independently rederived;
Python exact certificates and regression tests; the full universal rational
witness and real metric strict bound are Lean-kernel checked locally. No general Lonely
Runner Conjecture, academic novelty, or independently witnessed discovery is
claimed. Same-model agents supplied adversarial review, not blind witnesses.

## 1. Objects and provenance

For integers `n >= 3`, `1 <= r <= n-1`, let

\[
 V_{n,r}=\{1,\ldots,n-1\}\setminus\{r\},\qquad
 L(n,r)=\max_{t\in[0,1]}\min_{v\in V_{n,r}}\|vt\|,
 \quad \|x\|=\min_{z\in\mathbb Z}|x-z|.
\]

The maximum exists by continuity and compactness. Speeds are unshifted,
positive, distinct integers. Deleting one speed leaves `n-2` speeds. Changing
the convention to `n-1` retained speeds changes the target denominator.

Liu's 2008 Theorem 18, specialized to one missing multiple, supplies the
middle-range exact value below. The large-range value is elementary and also
appears in Liu's Theorem 17, attributed there to Zhu. The result here is a
corollary with explicit equality classification and executable certificates.
See [ALPHA_PRIORITY.md](ALPHA_PRIORITY.md) for primary-source receipts,
the distinction from Zhang's question, and an erroneous ancillary source
remark that is not used. All proofs below were checked directly.

## 2. Universal rational witness (ALPHA-01)

**Theorem.** For every integer `n >= 5` and `1 <= r <= n-2`,

\[
 L(n,r)\ge {2\over 2n-3}>{1\over n-1}.
\]

**Proof.** If `2r > n-1`, take `t=1/r`. A retained speed lies strictly
between `0` and `2r` and is not `r`, so its distance is at least `1/r`.
Since `r <= n-2`, this is strictly larger than `2/(2n-3)`.

Suppose `2r <= n-1`. We construct `D=kr+1` in `[n+r,2n-3]`.
If `n=2r+1`, then `r>=2`; use `k=3`, `D=3r+1`, and
`3r+1<=4r-1=2n-3`. Otherwise `n>=2r+2`; use

\[
 k=\left\lfloor{n+r-2\over r}\right\rfloor+1.
\]

Euclidean division gives `n+r <= kr+1 <= n+2r-1 <= 2n-3`.
Set `t=k/D`. Then `kr=D-1`, so multiplication by `k` modulo `D`
is invertible. For a retained speed `i`, `ki` is not `0` modulo `D`.
If `ki` were `-1` or `1`, multiplication by `r` would give `i=r`
or `i=D-r>=n`, respectively. Both are excluded. Therefore the least
nonnegative residue lies in `[2,D-2]`, giving
`||it|| >= 2/D >= 2/(2n-3)`. Finally `2(n-1)>2n-3` gives strictness
against `1/(n-1)`. All times are rational and belong to `[0,1]`. QED.

This proves the supplied construction including the short boundary interval
`n=2r+1`, where a generic assertion about `r` consecutive integers would
not apply. The choice `t=k/D` is the reflected version of the inverse of
`r`: `kr=-1 mod D` rather than `+1`. Reflection preserves every distance.

## 3. The exact deletion formula (ALPHA-02, classical)

Let `D_r` be the least integer `D>=n+r` with `gcd(D,r)=1`. Then

\[
 L(n,r)=
 \begin{cases}
  2/D_r,&2r\le n-1,\\
  1/r,&2r>n-1.
 \end{cases}
\tag{A2}
\]

**Proof, large range.** The lower bound at `1/r` was proved above and
also works for `r=n-1`. The retained speeds contain `[r-1]`. Among the
`r` points `0,t,...,(r-1)t` on the circle, two have circular distance at
most `1/r`, so some retained speed is at most `1/r`. This proves equality.

**Proof, lower bound in the middle range.** Choose `a` with
`ar=1 mod D_r`. For `1<=i<n`, the residue `ia` cannot be `0`, and it
cannot be `+1` or `-1` unless `i=r` or `i>=D_r-r>=n`. Thus `a/D_r`
attains at least `2/D_r`. This argument needs only `D_r>=n+r` and
coprimality; outside the middle range it need not be optimal.

**Proof, upper bound when `r>=2`.** An integer congruent to `1 mod r`
in `[n+r,n+2r-1]` shows `D_r<=n+2r-1<=2n-2`; hence
`2/D_r>1/n`. It is enough to consider a time where all retained speeds
exceed `1/n`. Dirichlet's circle pigeonhole argument for the full set
`[n-1]` then forces

\[
 t=p/r+\delta\pmod1,\qquad |\delta|\le1/(rn).
\]

If `g=gcd(p,r)>1`, the retained speed `r/g` has distance at most
`1/(gn)`, a contradiction. Thus `p` is a unit modulo `r`. For
`delta>0`, let `F` be the largest retained speed with `Fp=-1 mod r`;
for `delta<0`, choose `Fp=1 mod r`. Put `u=|delta|`. The speed `2r`
is retained and has distance `2ru` because `2ru<=2/n<1/2`. The chosen
speed `F` has distance at most `1/r-Fu`, a nonnegative number because
`F<=n-1` and `u<=1/(rn)`. Consequently

\[
 \min_{v\in V_{n,r}}\|vt\|
 \le\min(2ru,1/r-Fu)\le {2\over 2r+F}.
\]

The final bound follows by comparing `u` with `1/[r(2r+F)]`.
The largest representatives of unit residue classes modulo `r` lie in
the block `[n-r,n-1]`. If `I` is the least integer in that block coprime
to `r`, then `F>=I` and `D_r=2r+I`. The latter identity follows by
translation by `2r`, which preserves coprimality and maps the first block
to `[n+r,n+2r-1]`. Hence the upper bound is at most `2/D_r`.
The case `delta=0` has retained speed `2r` at distance zero.

**Proof, `r=1`.** Here `D_1=n+1`. If the retained minimum exceeds
`1/n`, the deleted speed forces `t` within `1/n` of an integer. Reflect
and write `0<=u<=1/n`. Speeds `2` and `n-1` give the upper bound
`min(2u,1-(n-1)u)<=2/(n+1)`. If they coincide (`n=3`), both bounds
still hold for that same speed. This completes (A2). QED.

The proof uses the same classical trap and modular structure as the cited
literature; it is included to make the claimed corollaries auditable, not
to relabel an existing exact formula as new.

## 4. Sharp minimum and equality (ALPHA-03)

**Theorem.** For every integer `n>=5`,

\[
 \min_{1\le r\le n-2}L(n,r)=
 \begin{cases}2/7,&n=5,\\2/9,&n=6,\\1/(n-2),&n\ge7.\end{cases}
\]

The complete minimizing sets of deleted speeds are `{2}` for `n=5,6`,
`{3,5}` for `n=7`, and `{n-2}` for every `n>=8`.

**Proof.** For `n=5`, formula (A2) gives `1/3,2/7,1/3` as `r` runs
from `1` to `3`. For `n=6`, it gives `2/7,2/9,1/3,1/4`.
Let `n>=7`. In the large range, `1/r>=1/(n-2)` with equality exactly
at `r=n-2`. It remains to show `D_r<=2n-4` in the middle range,
with equality only at `(n,r)=(7,3)`.

* If `n>=2r+4`, the generic congruence witness gives
  `D_r<=n+2r-1<=2n-5`.
* If `n=2r+1`, then `r>=3`, `D_r=3r+1<=4r-2=2n-4`;
  equality holds exactly when `r=3`.
* If `n=2r+2`, then `r>=3`. The integer `4r-1` is coprime to `r`
  and at least `n+r=3r+2`; hence `D_r<=4r-1<2n-4`.
* If `n=2r+3`, the cases `r=2,3` give `D_r=9,13`, respectively,
  strictly below `2n-4`. For `r>=4`, the integer `4r-1` is at least
  `n+r=3r+3`, so again `D_r<=4r-1<2n-4`.

These cases exhaust the middle range. Formula (A2) proves the result. QED.

**Corollary (ALPHA-04).** Equality in the requested bound
`L(n,r)>=2/(2n-3)` occurs exactly at `(5,2)` and `(6,2)`.
For `n>=7`, the sharper lower bound is strictly greater; the two small
tables prove both equalities and exclude all other small cases.

**Additive optimality.** No larger bound depending only on `n` can replace
ALPHA-03: every listed minimum is attained by the stated actual speed set.
This is not a claim about arbitrary speed sets of the same cardinality.

## 5. Hostile controls and exact boundaries

1. **Keep the excluded endpoint excluded.** At `r=n-1`, the retained
   set is `[n-2]`, whose exact value is `1/(n-1)`; the strict target
   and `2/(2n-3)` both fail.
2. **Keep the size assumption when classifying equality.** At `(n,r)=(4,1)`, the value is `2/5`,
   equal to rather than strictly greater than the displayed uniform
   bound; the classification of equality for `n>=5` cannot be extended
   unchanged. At `(3,1)`, `1/2<2/3` refutes the uniform bound itself.
3. **Do not use the inverse formula outside its range.** At `(5,3)`,
   `D_r=8`, but the exact value is `1/3>2/8`.
4. **The extra equality is essential.** `(6,2)` has value `2/9`; a
   claim that `(5,2)` is the sole equality case is false.
5. **No shifted starting positions.** The witness proof requires
   the exact points `it`, not arbitrary `s_i+it`. Reintroducing speed
   `r` destroys the excluded-residue argument.
6. **A literature statement remains falsifiable.** The prose following
   Liu's Theorem 18 omits `{1,3,4,5}` from its exceptions to a stronger
   cardinality bound; the exact value `2/9<1/4` is a counterexample.
   The formula (A2), not that remark, is used.

## 6. Executable evidence and authority

`observational_succ/lonely_runner_deletion.py` uses integer arithmetic and
`Fraction`. It implements the explicit user witness, an optimal modular
witness, the classical exact value, and the sharp minimizing set. It rejects
floating input and invalid domains. `DeletionWitness.verify()` checks only
the lower bound at the supplied time; it does not pretend to certify the
global upper bound.

`tests/test_lonely_runner_deletion.py` includes an independent exhaustive
piecewise-linear envelope oracle, using all times `a/(v+w)`, including
`v=w` peaks. That oracle does not call the deletion formula. Bounded sweeps
test the implementations, while Sections 2–4 prove the universal claims.

Run the focused test with

```sh
python -m unittest discover -s tests -p 'test_lonely_runner_deletion.py' -v
```

`formal/LonelyRunnerDeletion.lean` was accepted locally with Lean 4.14.0
and pinned Mathlib 4.14.0. Its seven audited exports prove the integer gap,
the centre gap, transport to real distance, the Euclidean denominator
construction, a universally quantified rational witness, the real-time
metric bound, and the strict real-time bound. In particular, the last export
has the full quantifiers `for all n>=5 and 1<=r<=n-2, there exists a common
t in [0,1], for all retained integer speeds i and all integers z,
1/(n-1)<|it-z|`. No residue correctness or finite scan is an antecedent.
All seven axiom audits contain only `propext`, `Classical.choice`, and
`Quot.sound`; there are no admitted proofs or custom axioms.

The exact maximization formula and sharp-minimum classification remain paper
proofs. Local kernel evidence is distinct from hosted CI and independent
mathematical review. The focused Python suite passed **11 tests**, including
the independent exact envelope comparison through `n=18`.

## 7. Claim ledger and next falsifiers

| ID | Exact scope | Status / evidence | Next falsifier |
|---|---|---|---|
| ALPHA-01 | All integers `n>=5`, `1<=r<=n-2`, universal rational witness | PROVED COROLLARY; Section 2; full real-metric witness KERNEL CHECKED LOCALLY | Attack boundary `n=2r+1` and integer residue gap |
| ALPHA-02 | All `n>=3`, `1<=r<=n-1`, piecewise exact value | CLASSICAL; Liu plus direct Section 3 proof | Challenge upper-envelope trap, especially `r=1` |
| ALPHA-03 | Exact minimum and all minimizers for every `n>=5` | PROVED COROLLARY; Section 4 | Check each of four near-boundary denominator cases |
| ALPHA-04 | Equality in `2/(2n-3)` iff `(5,2)` or `(6,2)` | PROVED COROLLARY; small tables plus ALPHA-03 | Wrong singleton equality control |
| ALPHA-X1 | Extend strict bound to `r=n-1` | REFUTED; `[n-2]` | Preserve as regression |
| ALPHA-X2 | Inverse witness always optimal outside middle range | REFUTED; `(5,3)` | Preserve as regression |
| ALPHA-X3 | Liu ancillary stronger cardinality remark as printed | REFUTED in the fetched author version; `{1,3,4,5}` | Compare published version / possible erratum |

## 8. Frontier

This closes the stated deleted-speed question within its precise family and
clarifies the sharp constants. It does not supply a new general-case Lonely
Runner method. The consequential next target must involve speed sets beyond
this classical deletion formula, or a certified inference rule that makes a
previously inaccessible infinite family tractable. No promotion by analogy,
finite search, or repetition of the same reasoner's argument is warranted.
