# Zero-anchored finite lambda compiler

**Status: PROVED PAPER for the stated finite semantics; TESTED MODEL for the
Python implementation.** This is a typed lambda compiler with explicit exact
arithmetic primitives. It is not a pure-lambda encoding of all arithmetic, a
complete C-monoid realization, a decision procedure for untyped conversion, or
a proof of statistical normality.

Pinned inherited implementation base:
`50481e49592af00d87c602f671a28f3503709de0` (Main XXIII integration candidate).
The implementation is additive:
[`zero_anchored_lambda.py`](../../../observational_succ/zero_anchored_lambda.py)
and [`test_zero_anchored_lambda.py`](../../../tests/test_zero_anchored_lambda.py).
The repaired beta substitution comes from
[`c_monoid_succ_embedding.py`](../../../observational_succ/c_monoid_succ_embedding.py);
the canonical rational source and proved tail bound come from
[`duck_bbp.py`](../../../observational_succ/duck_bbp.py). No inherited source or
archival contract is modified.

## 1. Exact language and trusted arithmetic boundary

Types are `Rational`, `SourceState`, and `Arrow(A,B)`. Source terms are

```text
Literal(q) | Variable(i) | Lambda(A,e) | Apply(e,f) | Primitive(name).
```

Variables use de Bruijn indices, with index zero naming the nearest binder.
Literal rational inputs are exact integers or `Fraction` values; floats and
booleans are rejected. The typing rules are the usual simply typed variable,
abstraction and application rules, plus this closed primitive table:

| Primitive | Type | Meaning |
|---|---|---|
| `origin` | Rational → SourceState | `s ↦ (0,s,s)` |
| `step` | SourceState → SourceState | `(n,u,s) ↦ (n+1,16u+r(n+1),s)` |
| `recover` | SourceState → Rational | `(n,u,s) ↦ 16^(-n)u-P_n` |
| `add` | Rational → Rational → Rational | exact addition |
| `divide16` | Rational → Rational | exact division by 16 |
| `forcing:n`, n≥1 | Rational | the fixed four-pole BBP value r(n) |

There are no callbacks, arbitrary Python evaluation, source replacement
primitive, distribution-randomizing primitive, or normality assertion.
Clocks and seeds are preserved runtime indices in `SourceState`; they are not
dependent indices in the static type checker.

The compiler erases the lambda argument annotations into the inherited target
`VAR`, `ABS`, `APP`, and `CONST` grammar. It lowers rational literals into
canonical rational tokens and primitive names into a reserved token family.
The evaluator applies capture-free beta substitution and exactly the displayed
arithmetic delta rules. It deliberately does not inherit the unrelated eta or
pairing rules of the larger target reducer.

Each `Program` retains its source term, target term, result type and fixed source
digest. Before execution, `verify_program` recompiles the source term and checks
all those fields. Source syntax and type constructors, every target node and
field, and all passport/status strings must have their exact declared Python
types before equality is used. In particular, a string subclass with a custom
equality method cannot forge a source digest, success status or rational token.
A mutated code body, type or digest therefore fails before execution. The source
digest is a reproducibility identifier for the literal
formula, not a source of mathematical authority. Every executed forcing
primitive is also checked by comparing the canonical factored rational function
with the original four partial fractions.

## 2. Compiler preservation theorem

**C-01 (finite semantic preservation).** Let `e` be a well-typed source term in
context Γ, and interpret its variables in the declared types. Interpret
`SourceState` as the carrier

```math
\mathcal S_r=\{(n,u,s)\in\mathbb N_0\times\mathbb Q^2:
u=16^n(s+P_n)\},\qquad
P_n=\sum_{j=1}^n16^{-j}r(j).
```

The compiled term has the same denotation. Every finite admitted beta or delta
reduction preserves that denotation. Consequently, whenever a compiled closed
ground program successfully returns a rational or source state, that value is
the denotation of the source term.

**Proof.** The compiler theorem is structural induction on `e`. Variables retain
their de Bruijn indices and therefore their environment lookups. Literals retain
their exact rational values. Primitive tokens denote the corresponding table
entry. Application and abstraction commute with compilation by construction,
so the two induction hypotheses establish those cases. For a beta contraction,
the substitution lemma says that the denotation of substitution into the body
equals evaluation in the environment extended by the argument. The binder case
of this lemma shifts free indices when entering a binder and lowers indices
when removing one, exactly the capture-avoiding operations used by the inherited
reducer. This is the usual syntactic substitution proof; the test suite also
uses an environment evaluator that does not perform substitution. Each delta
rule has the same input and output denotation by its displayed defining
equation. Closure under application and abstraction contexts then proves
preservation for one step; induction on the finite number of contractions proves
the result. ∎

The theorem concerns this specified mathematical grammar and reduction
semantics. Python execution tests are finite calibrations of the implementation;
they are not machine-checked formalization of the substitution theorem. No
termination or equality decision for arbitrary untyped lambda terms is inferred.

## 3. The exact zero survives every arithmetic path

**C-02 (source authentication and visible counterseed).** For every n≥0 and
rational seed s, let U₀(s)=s and Uₙ(s)=16Uₙ₋₁(s)+r(n). Then

```math
U_n(s)=16^n(s+P_n),\qquad
\mathcal Z(n,U_n(s))=16^{-n}U_n(s)-P_n=s.
```

Moreover the same s is obtained by applying the inverse affine maps
`u ↦ (u-r(j))/16` for j=n,n−1,…,1. The source successor preserves `Z`.

**Proof.** At n=0 the formula is immediate. The successor case follows from
`P_(n+1)=P_n+16^(-(n+1))r(n+1)`. This proves the forward identity by induction;
rearrangement gives `Z=s`. Each reverse map is the exact inverse of the
corresponding forward map, so their reverse composition recovers s. Substituting
the successor formula into `Z` proves preservation. ∎

`certify_state` replays all three paths: a direct prefix using the factored
rational source, backward iteration using the four partial fractions, and
forward iteration using the four partial fractions. The last two have shared
source provenance; they are different arithmetic decompositions, not three
independent mathematical witnesses. Certificates are replayed field by field,
including declared rational/boolean types. A label saying `original_zero` cannot
replace the calculation.

The source type admits authentic nonzero-seed paths for hostile testing. The
default `require_zero=True` rejects them. In particular, s=1/16 agrees with the
zero-seed completed *fractional* orbit for every n≥1 because their difference is
the integer 16^(n−1), while the unwrapped certificate still returns s=1/16.
Thus source identity remains visible even when a chosen observation aliases it.

## 4. Actual lambda iteration and guarded tails

`compile_state(n,s)` builds n applications of

```text
lambda state : SourceState. step state
```

to `origin s`. It does not precompute Uₙ and put the result in a constant. A
successful normal-order run has exactly n beta contractions and n+1 delta
contractions. Applying `lambda state. recover state` to that program reduces to
the literal rational seed. For the authentic source it reduces to `q:0/1`.

The bounded-tail operator is

```math
(\mathcal F_r t)_n=\frac{r(n+1)+t_{n+1}}{16}.
```

On bounded sequences this is a 1/16 contraction: subtraction cancels r, and the
supremum of the shifted difference is no larger than the original supremum.
The source r is bounded, so the map preserves bounded sequences. The explicit
fixed point is

```math
T_n=\sum_{j\ge1}16^{-j}r(n+j).
```

Absolute convergence gives the fixed-point equation. If t and v are two bounded
fixed points, `||t-v||∞ ≤ ||t-v||∞/16`, hence t=v. The uniqueness argument is
about the analytic future tail, not a unique empirical orbit law.

`guarded_tail_term(n,k)` compiles the finite unfolding `(F_r^k 0)_n`, using k
lambda abstractions of the form `lambda t. (r(j)+t)/16`. A normal-order run uses
k beta and 3k delta contractions and returns the exact finite sum
`Σ_(j=1)^k16^(-j)r(n+j)`. The code never runs an infinite Y combinator; its finite
answer is completed analytically using the next theorem.

**C-03 (bounded source completion).** Let L≥n≥0 and define
`T_n^(L)=Σ_(j=n+1)^L16^(n-j)r(j)`. Then

```math
U_n(s)+T_n^{(L)}=16^n(s+P_L),
```

and the exact completed value lies in the rational enclosure

```math
U_n(s)+T_n\in
\left[16^n(s+P_L),\;
16^n(s+P_L)+16^{n-L}\frac{r(L+1)}{15}\right].
```

**Proof.** Combine the two disjoint finite source sums. For the remainder,
the inherited original-source positivity and monotonicity bound gives
`0<T_L≤r(L+1)Σ_(j≥1)16^(-j)=r(L+1)/15`; rescaling by 16^(n−L) gives the
enclosure. All source terms are unchanged. Classical BBP supplies the separate
identification `lim P_L=pi/16`. ∎

At a common horizon L≥m≥n the two endpoints scale exactly by 16^(m−n). This is
a finite commuting completion square. Circle projection may cross a seam;
`complete_state` intentionally returns the unwrapped enclosure so a subsequent
Haar observer must pay its own boundary error.

## 5. Execution limits and truth states

`run` accepts `normal` and `applicative` strategies. Each has a global budget in
the number of beta/delta contractions. Exhaustion returns `UNRESOLVED_BUDGET`
with the last reduct, no value, and the exact step counters. It is not evidence
of inequivalence, a nonexistent normal form, or a failed mathematical conjecture.
Integer bit complexity and Python recursion depth are additional host limits;
the contraction budget is not a resource bound on those quantities.

The compiler has no rule which converts source authentication, tail convergence,
or successful beta normalization into a vanishing Haar defect. Such a rule would
need a separate source-specific statistical theorem. The execution record always
has `statistical_contraction_proved=False`.

## 6. Verification and next falsifier

The focused suite has 29 test methods. They include:

- Direct closed-sum arithmetic against the compiled source recurrence, across
  zero, nonzero, negative and rational observational-alias seeds.
- Normal and applicative reduction against a separate closure/environment
  evaluator, plus nested binders that retain an outer state or rational argument.
- Source-function mutation, tail-budget mutation, stale passport, target-code,
  clock, seed, value, and certificate-field mutations that must be rejected.
- In-process equality-spoofing string subclasses, AST/type/target subclasses,
  and malformed inactive target fields that must be rejected before comparison.
- Exact guarded-tail coefficients, nested enclosures, common-horizon transport,
  and budget exhaustion without statistical promotion.

The next compiler falsifier is a well-typed finite source term whose environment
denotation differs from its compiled beta/delta result, or a mutated source
certificate accepted by replay. The next mathematical gate is an independently
proved bound on the authenticated statistical residual; the finite source
compiler does not supply that bound by normalization alone.
