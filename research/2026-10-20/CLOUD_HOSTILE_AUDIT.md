# Cloud independent referee: exact holdouts and proof audit

## Scope, ownership, and verdict

**Target:** PR #201, `cbc4010458c00be995b8af3f229c9bba410301e2`, including
PR #200 at `e2f92a6b7e3835c3223abc294688ad9b85045811`.
Both heads were rechecked through GitHub during the audit and still matched.
The target checkout was clean. **Own base:** main at
`0e56e0ae26f3d52a2ea34c0a4288478139fcb634`.

This branch adds a read-only, parameterized fixture runner and exact controls.
It does not modify the target modules, Claude's branches, imported archives,
or common claim indexes. This is a new-to-project adversarial audit, not an
original theorem claim. The target's existing green tests and earlier audit
approvals are evidence about their tested cases, not a proof of these APIs.

**Verdict:** nine exact findings are recorded below. Several attack obligations
already named in the brief; F01–03, F06, and F09 give additional concrete failure
mechanisms. The smallest novel counterexample is the accepted fractional prime
cutoff: a function advertised as a certified enclosure returns an interval that
provably excludes its target. No inference about RH, abc, or Goldbach follows.

### Hole contract

Proposed claim under attack: a target `verify()` or exact arithmetic certificate
cannot report more proof/source/quantitative authority than its verified inputs
support. Quantifiers range over all inputs admitted by each public API, including
mutation after construction. Weakest sufficient repair: immutable, validated
records; explicit source/statement binding; trusted checked theorem artifacts;
and exact ordered arithmetic with fail-closed input validation. The cheapest
falsifiers are one false proposition, one mismatched source flag, one malformed
cutoff, and a 2-by-2 rational matrix. A finite successful audit can refute a
universal guarantee; passing finitely many holdouts cannot prove one.

The committed JSON records exact target SHA and source hashes, environment,
observed outputs, and the independent slope-count calibration. Fixture states
`exposed`, `not_exposed`, and `rejected_or_exception` are audit results, never
mathematical proof-status promotions. An arbitrary exception can be a safe
rejection or a usability defect and requires interpretation.

## Findings against the pinned target

### F01 — authentic contract accepted with a synthetic witness

**Minimal reproduction.** Construct an `UNVERIFIED` `ProofContract` with
`source_authentic=True`; attach
`SourceRealizationWitness("unrelated synthetic object", authentic=False)`.
`CarryingContract(...).verify()` returns `source_authentic: True` and no source
identification is performed.

**Expected:** reject the inconsistent authentic/synthetic pair.
**Actual:** an authentic-source record is emitted.
**Explanation:** the carrier only tests witness presence. The witness's own
`verify()` immediately accepts when its independent `authentic` field is false.
The emitted field comes from the contract, not the witness. No dishonest callback
is needed. This is distinct from the brief's `lambda: True` attack.
**Affected status:** the advertised source-authority consistency guarantee is
**REFUTED** on this target; the attached mathematical statement remains
UNVERIFIED. **Repair:** bind source identity and authenticity in one immutable
verified object, and reject mismatched flags and identities before returning.
**Regression:** this exact authentic-contract/synthetic-witness combination must
fail; a properly bound genuine witness and a consistent synthetic contract are
separate positive controls.

### F02 — post-construction status mutation bypasses proof backing

**Minimal reproduction.** Construct an `UNVERIFIED` contract and an empty
`CarryingContract`; then assign `contract.status = "PROVED LOCAL"` and call
`verify()`.

**Expected:** reject a proof status with neither certificate nor theorem.
**Actual:** the record says `PROVED LOCAL` with both backing lists empty.
**Explanation:** backing checks occur only in `__post_init__`; both contracts and
their lists are mutable, while `verify()` never repeats those invariants.
**Affected status:** proof-backing persistence is **REFUTED**. This does not prove
that any particular previously checked theorem was false.
**Repair:** immutable proof objects and immutable collections, plus verification
of all load-bearing invariants at the authority boundary. Merely freezing the
outer dataclass while retaining mutable nested lists is insufficient.
**Regression:** try status mutation, deleting the last certificate, replacing a
source witness, and changing a statement after construction; require rejection
or creation of a fresh unverified object.

### F03 — contradictory constant-dependency metadata passes uniformity checks

**Minimal reproduction.** Use the prefix `exists C, forall N`, but also provide
`constant_dependencies={"C": ["N"]}`. `is_uniform_in("C", "N")` returns true.

**Expected:** reject contradictory metadata instead of declaring uniformity.
**Actual:** the emitted record simultaneously says C is before N, C depends on N,
and C is uniform in N.
**Explanation:** prefix dependencies and `constant_dependencies` are independent
unchecked descriptions; the latter never participates in validation or the
uniformity query. **Affected status:** consistent uniformity bookkeeping is
**REFUTED** for malformed but admitted contracts. This does not by itself enact
an analytic quantifier swap; it defeats the advertised guard against one.
**Repair:** a single dependency graph generated from a validated prefix; require
unique bound names and existential constant roles. **Regression:** reject the
exact conflict above and duplicate/shadowed names; retain a correctly ordered
`forall eps, exists C(eps), forall N` positive control.

### F04 — a nonexistent external theorem supplies apparent proof backing

**Minimal reproduction.** Attach
`TheoremReference("NoSuchTheorem", "NoSuchKernel")` to a `PROVED LOCAL` contract
whose statement is `0=1`. `verify()` emits the proof status without an exception.

**Expected:** a reference alone cannot discharge a statement.
**Actual:** the arbitrary string reference satisfies the constructor's proof
backing test. **Explanation:** external references are useful metadata, but no
artifact is checked, no theorem type is recovered, and no implication connects
the named theorem to the contract's proposition. A genuine but unrelated theorem
would expose the same missing binding. This corroborates a concern already named
in the brief and is not counted as a new trust-model discovery.
**Affected status:** authority from this interface is **UNVERIFIED**; the claim
that metadata cannot impersonate proof is **REFUTED** as an implementation
guarantee. **Repair:** separate references from checked proof authority, with
pinned kernel-check receipts and an explicit statement/type bridge.
**Regression:** nonexistent references, unrelated valid theorem types, changed
source artifacts, forged axiom lists, and wrong Lean versions must not acquire
proof authority. Do not substitute another caller-defined callback.

### F05 — shallow negative directions defeat the witness search

For every integer `n>=3` and rational `0<epsilon<1/2`, set

\[
M=nI-(1+\epsilon)J,\qquad v=(1,\ldots,1)^T.
\]

Then `v^T M v = -n^2 epsilon < 0`. Coordinate directions have value
`n-1-epsilon>0`; pair directions `e_i-e_j` have value `2n>0`, and
`e_i+e_j` have value `2n-4(1+epsilon)>0`. These are exact polynomial identities.
Thus a coordinate-and-pair fallback is incomplete even if all its cases pass.

**Minimal executed case:** `n=3, epsilon=10^-14`.
The target correctly says non-PSD, but `negative_witness` raises `RuntimeError`
although the integer vector `(1,1,1)` has value `-9/10^14`.
**Expected:** return a rational negative witness.
**Explanation:** the floating eigenvalue threshold suppresses the only negative
eigendirection, and the fallback cannot see it. Raising `max_denom` does not fix
this family: denominator 1 already suffices.
**Affected status:** completeness of this algorithm is **REFUTED**; the classical
rational negative-witness existence theorem is unaffected.
**Repair:** exact pivot/congruence extraction or another terminating exact
procedure. **Regression:** vary n and epsilon, including arbitrarily shallow
negative cones, and exact PSD/null mutations. The independent test controls
verify all coordinate and pair values without NumPy or SymPy.

### F06 — fractional cutoff produces a provably false singular-series enclosure

**Minimal reproduction:**
`singular_series_enclosure(2, Fraction(5,2))` returns `[1/3, 1]`.
**Expected:** reject the noninteger cutoff, or correctly count primes up to it.
**Actual:** `_primes_upto` silently returns an empty list for nonintegers while
the caller continues its rational tail computation.

The true `S(2)=2*C2` has the independent lower bound

\[
S(2)\ge2(1-1/4)(1-1/16)(1-1/4)=135/128>1.
\]

Here the first factors are the genuine primes 2, 3, 5; the tail at prime cutoff
5 is at least `1-sum_{n>=6}(n-1)^-2 >= 1-1/4`. The latter sum is bounded by
the integral from 4 to infinity. Thus the returned interval excludes the true
infinite object by a strict rational inequality, without numerical evaluation
of the twin-prime constant.

**Affected status:** this admitted-input certified enclosure is **REFUTED**.
The documented integer-cutoff theorem itself survives.
**Repair:** enforce integer cutoff and minimum range at every public entry,
rejecting booleans, floats, and rational objects if those are outside the domain.
**Regression:** this exact `Fraction(5,2)` input, integer-valued fractions/floats,
boolean cutoffs, and correct integer cutoffs. Lane C added the exact hostile input
to its independently owned implementation.

### F07 — whole high-exponent tail is not the BBLT small remainder

**Minimal reproduction:** `bblt_anatomy(256,4)` returns `n0=256`; but
`256^(1/4)=4`. More generally, with n a prime power of exponent greater than d,
the code's entire high-exponent tail is n, not `<=n^epsilon` for epsilon<1.

**Expected:** distinguish an exact layer truncation from the differently
reorganized small-remainder construction in BBLT Lemma 2.2.
**Actual:** the docstring attributes the small-remainder conclusion to this whole
tail. **Explanation:** BBLT folds high exponents into a fixed retained power and
puts only remainder exponents in n0; whole-tail truncation is a different map.
The lane B source reconstruction provides the primary-paper comparison.
**Affected status:** the attributed small-remainder inference is **REFUTED**;
the code's exact reconstruction identity remains **PROVED LOCAL**.
**Repair:** rename and document exact truncation honestly, or implement the actual
BBLT regrouping as a separate function. **Regression:** pure prime powers with
arbitrarily high exponent, including a multiple of the regrouping depth.

### F08 — 2*C2 is not S(2p), even when p exceeds the cutoff

The `twin_prime_constant_enclosure` docstring asserts this equality.
Take `p=5`, `P=3`. The exact local-factor quotient is

\[
\frac{S(10)}{S(2)}=
\frac{1+1/(5-1)}{1-1/(5-1)^2}=\frac43.
\]

**Expected:** `S(10)=(4/3)*(2*C2)`.
**Actual claim:** equality with `2*C2`.
**Affected status:** the documentation identity is **REFUTED**. The function's
enclosure for `2*C2` itself is not refuted by this example.
**Repair:** use `S(2^k)=2*C2`; for even nonzero N include all factors
`(p-1)/(p-2)` for odd prime divisors p of N, including those beyond a cutoff.
**Regression:** compare N=2, 6, 10, powers of 2, and odd N, with the prime 2
handled separately. Prime and modulus cutoffs must remain distinct.

### F09 — float ordering turns an exact eigenvalue into the wrong minimum

Let `H=10^30` and

\[
M=\begin{pmatrix}H+2&1\\1&H+2\end{pmatrix}.
\]

**Expected:** `min_eigenvalue_exact(M)=H+1`.
**Actual:** `H+3`.
**Explanation:** the exact eigenvalues are H+3 and H+1, but the floating ordering
keys coincide. The first enumerated eigenvalue wins the tie. Returning an exact
algebraic object does not make its selection an exact inequality proof.
The vector `(1,-1)` gives

\[
v^T(M-(H+3)I)v=-4,
\]

an exact certificate that the reported minimum is not a lower bound.
**Affected status:** exact least-eigenvalue certification is **REFUTED** on this
family. This can contaminate downstream reported gap values; it is independent
of the separate `certified_pd_margin` procedure, which rechecks its candidate.
**Repair:** exact real-algebraic root ordering or certified isolating intervals;
if a float proposes a bound, verify the shifted matrix before calling it one.
**Regression:** large scalar shifts of fixed non-diagonal matrices, extremely
close eigenvalues, and independently verified Rayleigh quotient controls.

## Independent review of cloud mathematics

These reviews are separate reasoning passes by a same-model agent, not blind
external refereeing. They do not establish independence of common source data.

### Lane B: primitive moment extension to t<2/3

The proposed proof survived a line-by-line algebraic audit. Its decisive step is
the following slope bound. If d,e,f are pairwise coprime, and primitive positive
triples satisfy `d|a, e|b, f|c, a+b=c, c<=X`, distinct reduced slopes a/c are
separated by at least `def/X^2`: the nonzero determinant `ac'-a'c` is divisible
by d and f directly, and by e because `c≡a` modulo e. Consequently there are at
most `1+X^2/(def)` triples. Primitivity ensures slopes cannot repeat.

The independent enumerator checked **19,812** parameter cases with integer
`2<=X<=40` and `1<=d,e,f<=12`, with no failures. The nonprimitive mutation fails:
`X=34,(d,e,f)=(8,9,17)` permits `(a,c)=(8,17),(16,34)`, giving count 2, greater
than `1+34^2/(8*9*17)=35/18`. This calibrates the necessity of primitive slopes.

For the divisor expansion `f_t=1*g_t`, nonzero g_t(d) is supported on powerful
integers. Such d obey `d<=ris(d)^2`. Thus, on `H=ris(abc)<=X`, supported divisor
products have `def<=H^2<=X^2`, allowing the slope count's +1 to be absorbed.
The low portion is at most `2 M(t)^3 X^2`, where `M(t)=sum g_t(d)/d<infinity`
for t<1. On `H>X`, the radical product is at most `X^3/H`, so some pair radical
product is at most `(X^3/H)^(2/3)`. The independent Rankin factor is

\[
C_\epsilon=\prod_p\left(1+\frac{2}{p(p^\epsilon-1)}\right)<\infty
\quad(\epsilon>0).
\]

It gives the tail count `3 C_epsilon X^(2+2epsilon) H^(-2/3)`. Layer-cake
integration bounds the high weighted portion by
`2 C_epsilon/(2/3-t) * X^(2+2epsilon+t-2/3)`.
Choosing `epsilon=(2/3-t)/4` makes this `O_t(X^2)` for `0<=t<2/3`.
No endpoint t=2/3, individual abc bound, or novelty claim is licensed.

### Lane C: singular-series truncation

Independent review of the complete dossier found no gap in the fixed-nonzero-N
absolute convergence argument, the residual-factorization-free prime cutoff,
or the different modulus tail `12 D(N)/Q`. In particular, the identity
`n^2/phi(n)^2=sum_{d|n}h(d)` and the explicit Euler bound
`sum h(d)/d <=2004725/338688<6` imply
`sum_{n>Y}phi(n)^-2<12/Y` for every real Y>0, including Y<1.
The q=dr split preserves the coefficient `1/(phi(d)phi(r)^2)` before dropping
restrictions. The N dependence remains explicit; N=0 is correctly excluded.
This review is of the paper proof, not independent reimplementation of every
cyclotomic computation or external source attestation.

### Lane D: constrained inverse correction

For bounded self-adjoint `B>=kappa I>0` and independent constraint columns Q,
the claimed inverse of the compressed operator on `E=ker Q*` is

\[
B^{-1}-B^{-1}Q(Q^*B^{-1}Q)^{-1}Q^*B^{-1},
\]

restricted to E. Lagrange multipliers or direct multiplication on E verify this
identity. For orthogonal constraint columns h_j, the inequality
`Q*B^-1 Q <= kappa^-1 diag(||h_j||^2)` gives the stated positive correction
lower bound. The implemented moving-shift error was independently checked:
the classification boundary moves on total measure at most 2delta, the inverse
sup norm is at most `||h||inf/kappa`, and outside those cells the polynomial
translation has the advertised derivative bound. The Young/Frobenius charge
correctly handles both residual columns.

This audits the new mathematical correction. It does **not** independently
re-authenticate all inherited Gamma, pole, source, or error estimates; those
remain explicit dependencies in lane D. No signed S4 or RH verdict follows.

### Lane E: complete rational elimination

The independent line-by-line review of `cloud_schur_certificates.py` found no
gap in negative diagonal extraction, the zero-diagonal/nonzero-coupling vector,
positive-pivot Schur recursion, or lifting a positive weighted Gram. The separate
checker recomputes the finite inequality or every Gram entry and does not call a
user-supplied verifier. Its rational-to-real implication follows from the sum of
positive weighted real squares, not from a floating eigenvalue test.

A fresh execution applied lane E's generator/checker to F05's family with
`n in {3,5,8}` and `epsilon in {10^-14,10^-100,10^-400}`. All **9** cases returned
exact negative vectors that passed exact recomputation. This includes the case
that the pinned PR201 implementation misses. The Python refinement is not a
kernel-verified program; this referee did not execute Lean elaboration and does
not certify its formal status.

## Reproduction and integration boundary

```sh
python scripts/cloud_hostile_holdouts.py \
  --target-repo /absolute/path/to/pinned/PR201 \
  --slope-audit --output /tmp/cloud-hostile-receipt.json
python -m unittest discover -s tests -p 'test_cloud_hostile_holdouts.py' -v
```

The target needs its research dependencies. The new fixture-control tests use
only the Python standard library. The committed receipt uses Python 3.12.14,
SymPy 1.14.0 and NumPy 2.5.4. Formal verification status: **not Lean formalized**.
The control suite passed 4 tests; broad required repository validation is owned
by the coordinator. The target's legacy focused tests also passed: 7 proof-contract
tests, 10 witness-contract tests, and 14 quantitative-rigidity tests, **31 total**.
A green baseline does not override these counterexamples. `git diff --check`
and Python compilation of the new runner passed.

This branch is independently mergeable from pinned main and touches no files
owned by Claude. Recommended integration: retain it as hostile regression data,
then rerun the same target-parameterized runner against Claude's repaired head.
Do not automatically turn `not_exposed` into a general correctness claim.

**Next verdict-changing probe:** obtain the repaired exact target SHA and rerun
all nine cases; then review the trusted checker and statement/source binding
against the explicit F01–F04 mechanisms. These are demonstrated implementation
boundaries with known repairs, not evidence of an impossibility theorem.
