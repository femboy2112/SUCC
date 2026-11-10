# Semantic repairs to the Scott × Omega branch

**Audited parent:** PR #576, `afabc458323ef2e3a20ce2bae77239c4190819c5`.
**Scope:** executable lambda substitution, natural-number actions, restricted omega
syntax, cofinal schedules and one Scott-continuity argument. This is not a
certificate of a genuine C-monoid or a compiler for the completed BBP source.

All three repaired modules are absent from the frozen
[`IMPORT_MANIFEST.json`](../../../provenance/IMPORT_MANIFEST.json). Their original
versions remain available at the exact parent commit. No archival snapshot,
authentic four-pole source or source seed was edited.

## 1. Reproduced defects despite a green baseline

The following baseline command passed **27 tests**, while the displayed hostile
examples exposed the underlying failures:

```sh
python -m unittest tests.test_c_monoid_succ_embedding \
  tests.test_omega_trace_interpreter tests.test_scott_cofinal_schedule -v
```

| Finding | Exact parent behavior | Correct statement | Verdict |
|---|---|---|---|
| Variable capture | `λz.((λx.λy.x) z)` reduced to `λz.λy.y` | It reduces to `λz.λy.z` | REFUTED implementation, repaired |
| Missing binder removal | The beta helper did not lower free indices after removing a binder | Contract using an argument up-shift, capture-free substitution and a result down-shift | Repaired |
| Affine relation | `V_p` was defined as repeated BBP time advance; checker compared commuting iterates | On natural numbers, `S(n)=n+1`, `V_p(n)=pn`, and `V_p S=S^p V_p` | REFUTED identification, domains separated |
| Invented redexes | `E_4(3)` reported two available beta-redexes `(0,1)` | `((ω_4 ω_4) ω_4)` has exactly one, in its left child | REFUTED positions, repaired |
| Cofinality tautology | A constant prefix of `(0,0)` returned `True` | A finite prefix cannot certify its infinite extension | REFUTED checker, replaced |
| Invalid exact carrier | `SuccState` accepted negative clocks and floating-point values; `forcing` accepted invalid indices | Require natural integer clocks, exact int/Fraction states and positive integer source indices | Repaired |
| Hardcoded identity | Historical C9 returned unconditional `True` | Evaluate its displayed equation using the reducer | Repaired |
| Claimed decreasing beta measure | Documentation claimed every reduction decreased size/depth | Omega can reproduce itself, and beta can increase size | REFUTED explanation, global budget added |

These are receipts against the implementations and their overstatements. They do
not refute the user's broader goal of a sound computational observation calculus.

## 2. Capture-free lambda semantics

The conventional zero-based de Bruijn beta rule is

```math
(\lambda b)\,a\longrightarrow
\operatorname{shift}_{-1}\bigl(
  \operatorname{subst}(b,0,\operatorname{shift}_{+1}(a))
\bigr).
```

Under an abstraction, substitution increments the target index and shifts the
replacement once before entering the body. The initial up-shift reserves the
binder being eliminated; the final down-shift removes it. Bound occurrences
inside the replacement remain bound to their original binders, and free
occurrences are not captured by binders traversed in the destination.

The repaired reducer contracts one leftmost-outermost rule at a time and counts
all contractions against one global budget. A beta contraction is recorded even
when its result is syntactically unchanged, as in Omega. An unused divergent
argument is discarded by a surrounding beta-redex before that argument is
normalized. Exhausting the budget means **UNKNOWN**, not “no normal form.”

The finite tests include an independent **named-variable** substitution oracle
using explicit alpha-renaming. It compares 140 combinations of body, argument
and external binder depth to the de Bruijn result, including shadowed names and
arguments dependent on external binders. This gives an implementation with a
different failure mechanism; it is not a machine-checked universal metatheorem.

**Primary provenance:** N. G. de Bruijn, *Lambda calculus notation with nameless
dummies, a tool for automatic formula manipulation, with application to the
Church-Rosser theorem*, 1972, pp. 381–392,
[DOI](https://doi.org/10.1016/1385-7258(72)90034-0),
[author institution record](https://research.tue.nl/en/publications/lambda-calculus-notation-with-nameless-dummies-a-tool-for-automat/).
The code uses its own zero-based convention and tests, not a claim that the
historical paper verified this Python implementation.

### Authority of the identity checker

The old `check_cmonoid_equations` function name and C1–C9 result keys are retained
for compatibility. They are **finite sample identity labels**. In particular,
the old C8/C9 formulas are derived identities and were not a verified transcription
of the complete Lambek–Scott axiom list. An equality result supplies a common
reduct for the displayed inputs; unequal outputs or a budget exception do not
decide the full intended equational theory.

No result here promotes CW-18 to a faithful source-action embedding or proves
that the implementation constructs a genuine nontrivial C-monoid. Those tasks
still require a full presentation, a consistency/model argument, and a faithful
encoding of the indexed rational source, history and observations.

## 3. Genuine SUCC/FUCC actions versus BBP time advance

The repaired API distinguishes three operations:

| Operation | Carrier | Definition |
|---|---|---|
| `arithmetic_successor` | natural numbers | `S(n)=n+1` |
| `dilation_Vp` | natural numbers | `V_p(n)=pn`, for integer `p>=1` |
| `iterate_bbp_steps` | indexed rational `SuccState(n,u)` | repeated application of `(n,u)↦(n+1,16u+r(n+1))` |

For every natural `n` and positive integer `p`, direct arithmetic gives
`V_p(S(n))=p(n+1)=pn+p=S^p(V_p(n))`. In contrast, `V_p S=S V_p` is false for `p>1`.
The new tests check this negative control, so commuting iterates cannot pass as
the affine law again.

The actual lambda terms are:

```math
\overline n=\lambda f\,x.\,f^n(x),\qquad
S=\lambda n\,f\,x.\,f(nfx),\qquad
V_p=\lambda n\,f\,x.\,n(\overline p f)x.
```

Unfolding the Church numeral shows `S n̄=(n+1)̄` and `V_p n̄=(pn)̄`; hence their
affine relation on Church numerals follows for all `n,p`. The test checks
`p∈{1,2,3,5,7}` and `0<=n<=5` with exact lambda reductions as finite calibration.
The exact carrier now rejects negative or Boolean clocks, floating-point or
string source states, and nonpositive or noninteger forcing indices. Integer
states are normalized to `Fraction`; callers cannot silently enter an inexact
carrier through those APIs. The four-pole BBP action remains a separate exact
rational evaluation. A sound
compiler taking that indexed action into these lambda terms is **UNVERIFIED**.

The projector `e(x)=<fst x,fst x>` is a genuine sample idempotent:
`e(e(x))=e(x)` by two pair projections. The original test's comment that it was
not idempotent was incorrect; the repaired test checks this nontrivial retract
and rejects `PROJ1` alone as an idempotent.

## 4. Actual omega redex positions

Write `ω_k=λx.(...((xx)x)...x)` with `k>=2` occurrences, and let `E_k(m)` be the
left-associated application chain of `m` copies of `ω_k`. An address is a tuple
of application-child labels; `()` denotes the root and `("f",)` its left child.

For `m=1`, `ω_k` is beta-normal. For `m>=2`, there is exactly one beta-redex:
`ω_k ω_k`, at address `("f",)*(m-2)`. Each outer application has an **application**
on its left, not an abstraction. Each abstraction body contains only variable
applications, so it contains no additional beta-redex.

Contracting this unique redex replaces two copies by `k` copies and gives
`E_k(m+k-2)`. The same description then applies again. Consequently every beta
reduction of a chain with `m>=2` must continue forever; this follows from the
unique-redex structure, not merely from observing one divergent strategy.

The executable object remains a compressed representation of this restricted
family. Its `syntax()` method materializes a generic de Bruijn AST. A separate
recursive AST enumerator and addressed beta contraction test agree with the
compressed formula for `2<=k<=8`, `1<=m<=9`. They also reject contraction at the
root of `E_4(3)`.

The arity and complete copy-count history already determine the addresses in
this restricted family. No independent spatial dimension or general
count-versus-address separation theorem follows. A deliberately weaker summary
retaining only the **first reached count** does conflate `E_4(2)` and `E_3(3)`;
both reach count four but contract at `()` and `("f",)` respectively.

The historical `compile_succ_step` function terminates as a fixed finite rational
evaluation. Its three integer “addresses” are operation slots, distinct from
lambda-tree paths. The repaired documentation no longer calls that an
omega-to-source compiler.

## 5. Cofinality: generator proofs, not prefix guesses

A subset `C` of the product-ordered natural pairs is cofinal exactly when

```math
\forall N,L\ \exists(n,\ell)\in C:\quad n\ge N\ \text{and}\ \ell\ge L.
```

Separate unbounded projections are insufficient for an arbitrary sequence:
`s(2k)=(k,0)` and `s(2k+1)=(0,k)` have unbounded coordinate images, but never
jointly dominate `(1,1)`. This also exposes a missing hypothesis in the old
paper statement, independent of the implementation tautology.

For a **coordinatewise nondecreasing sequence**, unboundedness of each coordinate
is sufficient. Choose an index meeting the first threshold and one meeting the
second, then take the later index. Necessity is immediate from cofinality.

The repaired module certifies only the explicitly declared affine family

```math
s(k)=(a+bk,c+dk),\quad a,b,c,d\in\mathbb N_0.
```

It is cofinal iff `b>0` and `d>0`. For any target `(N,L)`, the exact witness is

```math
k=\max\!\left(0,
\left\lceil\frac{N-a}{b}\right\rceil,
\left\lceil\frac{L-c}{d}\right\rceil\right).
```

The code handles bounded coordinates separately: an unreachable target raises
an exception. It rejects the old two-list `is_cofinal_schedule` call. Finite
prefix diagnostics explicitly return `cofinal=None` and
`UNVERIFIED_FROM_FINITE_PREFIX`, even for long increasing prefixes. This API does
not pretend to decide cofinality for arbitrary programs.

### Scott continuity and the product-topology qualification

The old D-3 argument should use the **product dcpo's directed suprema**, not assume
that its Scott topology equals the product of the two factor Scott topologies.
The useful order-theoretic statement has a direct proof:

Let `P,Q,R` be dcpos and let `f:P×Q→R` be Scott-continuous separately in each
variable. Then it is jointly monotone. For a nonempty directed set `D⊆P×Q`, put
`A=π_P(D)` and `B=π_Q(D)`. Separate preservation of directed suprema gives

```math
f(\sup A,\sup B)=\sup_{a\in A}\sup_{b\in B}f(a,b).
```

For every `a∈A,b∈B`, choose corresponding members of `D`; directedness supplies
one member dominating both. Monotonicity then bounds `f(a,b)` by its value at
that member. Conversely every value `f(p,q)` with `(p,q)∈D` occurs in the
rectangular family. Its supremum is therefore exactly `sup f(D)`, establishing
joint directed-supremum preservation. This proves the required Scott continuity
without identifying those topologies. It still does not imply equality of two
unrelated limit observations.

## 6. Verification and remaining obligations

Executed locally after the repairs:

```sh
python -m unittest tests.test_c_monoid_succ_embedding \
  tests.test_omega_trace_interpreter tests.test_scott_cofinal_schedule \
  tests.test_scott_omega_semantic_soundness -v
```

**47 tests PASS**: 27 retained cases (with corrected redex expectations and the
idempotent assertion) plus 20 new adversarial cases. The named substitution
oracle, generic AST traversal, arithmetic negative control, budget exhaustion
and finite-prefix refusal exercise different failure mechanisms.

These local passes are not the repository-wide validation or hosted CI result.
The containing research round records those gates separately. Neither a full
C-monoid source embedding, a faithful omega-to-BBP compiler, original-zero parity
balance nor π base-16 normality is certified by this repair.
