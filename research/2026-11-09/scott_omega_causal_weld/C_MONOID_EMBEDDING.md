# Front A — lambda fragment, arithmetic actions and the unproved C-monoid embedding

**Corrected status:** TESTED FINITE MODEL; full C-monoid/source embedding
**UNVERIFIED**. The parent draft at
`afabc458323ef2e3a20ce2bae77239c4190819c5` claimed more than its implementation
established. The [semantic audit](../cayley_source_observer/SEMANTIC_AUDIT.md)
records capture, operator, budget and axiom-list defects and their repairs.
The archived session files are unchanged.

## 1. What is actually implemented

`c_monoid_succ_embedding.py` implements a de Bruijn lambda syntax with products,
projections, beta contraction, eta and surjective-pairing sample reductions.
Capture-free beta contraction uses shift/substitute/unshift. A global reduction
budget returns a normal form only when one is reached within the budget;
exhaustion does not decide whether the term has a normal form.

The displayed combinators include identity, composition, pairing, projections,
evaluation and currying. Their finite test reductions are useful operational
evidence. A universal confluence/model theorem for this exact presentation is
not supplied by that evidence.

## 2. The historical C1–C9 checker has restricted authority

The function name `check_cmonoid_equations` and its C1–C9 keys are retained for
compatibility. They name **sample equations**, not a verified transcription of
the complete Lambek–Scott axioms. In particular, old C8/C9 were derived equations,
and C9 originally returned hardcoded True. It now evaluates the equation.

A successful comparison demonstrates a common reduct for the displayed terms.
A mismatch or budget exception does not decide their equality in the full
intended equational theory. Independent named-variable substitution and generic
AST regressions test the evaluator, not the existence of a nontrivial model.

## 3. Karoubi direction remains conditional

The proposed route through the idempotent splitting of a **genuine** C-monoid
retains its classical Lambek–Scott motivation. To apply it here, a complete
presentation and a consistency/nontrivial-model argument must first be supplied.
Finite identity checks do not establish this premise.

The sample projector `e(x)=<fst x,fst x>` is idempotent by two projections.
The corrected test checks this retract and rejects `PROJ1` alone as idempotent.
The earlier finite transformation-monoid proxy remains a proxy, not a C-monoid
model; the Set self-power obstruction is unchanged.

## 4. Natural affine action and chronological BBP action are distinct

On natural numbers, for every n>=0 and integer p>=1,

```math
S(n)=n+1,\qquad V_p(n)=pn,\qquad V_p S=S^p V_p.
```

Church numeral terms implement these maps: successor sends n to n+1 and
multiplication by p sends n to pn. The identity follows by unfolding them;
the tests include the false-commutation control `V_p S != S V_p` for p>1.

The exact indexed BBP action instead sends
`SuccState(n,u)` to `SuccState(n+1,16u+r(n+1))`. Its iterates live under the
separate `iterate_bbp_steps` API. Substituting a time iterate for V_p did not
prove the natural-number affine relation, and does not prove source faithfulness.
The carrier rejects negative/Boolean clocks and inexact floating states.

## 5. What remains to prove

The follow-up now gives a [faithful source-clock action](../cayley_source_observer/AFFINE_SOURCE_ACTION.md)
on indexed rational states, with actual BBP successor and a declared clock
dilation obeying the affine relation. It does not identify dilation with
multiplication of the rational value or supply the C-monoid realization.

A faithful computational source embedding needs an explicit encoding of the
clock, rational state, source history and retained observations; preservation
of each intended reduction; and a reflection/non-alias theorem on the declared
source domain. The completed Green tail needs its own compatible observational
limit contract. None follows merely from the numeral action.

CW-18 therefore remains **UNVERIFIED**. Original-zero parity balance, pi
base-16 normality and RH remain **OPEN**. See the follow-up validation record
for executed finite checks and their distinct authority.
