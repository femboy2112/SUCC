# Independent semantic review of the repair working tree

Review scope: the three repaired executable modules and `SEMANTIC_AUDIT.md` in
`/workspace/scratch/6411c4073100/SUCC`. This is a same-model independent bearing,
not an external referee or formal verification. I changed none of these files.

**Follow-up:** the runtime `SuccState` carrier issue reported below was then repaired
with strict natural-index and exact rational checks and two regression tests.
The following hashes identify the reviewed pre-repair snapshot, not the final
carrier-validation revision. The affine source-admissibility caveat remains.

## Reviewed file bindings

| File | SHA-256 |
|---|---|
| `observational_succ/c_monoid_succ_embedding.py` | `d18dce48238dc7f0a04b709ce9d576a54ed67762dbd77fe63feda48633386160` |
| `observational_succ/omega_trace_interpreter.py` | `3b97a2eab20187daf47dfc62b3a146bec049a63bf507781d5576aae1778ff2a9` |
| `observational_succ/scott_cofinal_schedule.py` | `437c4e4c4bf068a76ab21ed74bd18d85845d088c0122d218ec755aadb51ec73a` |
| `research/2026-11-09/cayley_source_observer/SEMANTIC_AUDIT.md` | `ad4776e5ad7ceab635ad7e5fb98276b6278a8378678ca5de75bce6015768261b` |

## Verdict

The mathematical repairs are sound on their stated domains. No remaining
blocking counterexample was found in capture avoidance, the reduction-step
budget, the restricted omega redex theorem, the Church numeral affine action,
or affine-family cofinality. The source-action compilation and full C-monoid
claims are now explicitly withheld, as they should be.

The following two API boundaries should remain visible; neither contradicts
the mathematical results on the documented domains.

1. `SuccState` annotations do not enforce its rational-state contract at runtime.
   `succ_step(SuccState(0, 0.1)).u` is a `float`. Negative source-clock values
   can also be constructed. A `__post_init__` natural-index check plus explicit
   rational coercion or rejection would prevent callers from silently leaving
   the exact carrier. Otherwise explicitly retain the precondition that
   `n` is a nonnegative integer and `u` is a `Fraction`.
2. `AffineSchedule` correctly certifies cofinality in all of `N_0 x N_0`.
   It does not certify the additional source-horizon constraint `L>=n`.
   `AffineSchedule(0,2,0,1)` is genuinely cofinal but outputs `(2,1)` at time one.
   A consumer using CW-04's finite source cone must separately impose source
   admissibility. The current module does not falsely claim otherwise; do not
   call every supported affine schedule a valid BBP refinement schedule.

The normalizer budget counts admitted reduction transitions, not CPU work or
AST traversal. To decide whether the last allowed reduct is normal it calls
`reduce_once` once more; a discovered additional contraction is computed and
discarded before raising the budget exception. This does not falsify its
within-limit-normal-form contract, but it is not a strict bound on evaluation
work, allocation, or Python recursion depth.

## Derivation audit

### Capture-free substitution

The rule is the conventional zero-based construction:
`shift(-1, subst(body,0,shift(+1,arg)))`. On entering each abstraction, both the
target index and the replacement's free indices advance by one. The final
down-shift removes the contracted binder. This handles the old capture example,
free arguments under newly introduced lambdas, and outer variables formerly
indexed above the eliminated binder.

The eta guard `not occurs(f,0)` uses a binder-aware occurrence check. It therefore
cannot drop a lambda whose variable remains free in `f`. Pair projections and
the extensional pairing contraction are valid stated equations. Their presence
does not prove consistency or completeness of a complete C-monoid presentation;
the module now expressly avoids that assertion.

`reduce_once` carries an explicit contraction flag, so syntactically unchanged
Omega contractions cannot be mistaken for normal forms. `norm` has one budget
for all admitted reductions. Normal-order contraction correctly discards an
unused divergent argument. A failure to produce a normal form is reported as
unknown, not as a general nonnormalization theorem.

### Church action versus indexed source action

The Church numeral and successor definitions are conventional. In
`lambda n f x. n (church_p f) x`, the closed numeral `church_p` needs no context
shift: its action replaces each `f` application by `p` applications. Thus the
result on `church_n` is `church_(pn)`. The affine relation follows from
`p(n+1)=pn+p` and is distinct from commuting powers of one BBP time-step map.
The revised API rejects `SuccState` as input to `dilation_Vp`, preserves the
indexed BBP recurrence under `iterate_bbp_steps`, and leaves the unimplemented
compiler open. This is the needed separation.

The proposed retract `x -> <fst x,fst x>` is idempotent by direct pair
projection; `fst` itself is not an idempotent on the unrestricted term carrier.

### Omega positions and nonnormalization

For the restricted left-associated chain, every outer application except the
leftmost pair has an application as its left operand; it is not a beta redex.
Each omega body consists solely of a variable application tree. Thus the unique
redex is precisely at `('f',)*(m-2)` when `m>=2` and absent at `m=1`.
Contracting it replaces two copies by `k`, preserving the same family with
`m+k-2>=2`. The uniqueness makes the infinite-reduction statement independent
of strategy within this family. This proof does not extend automatically to
arbitrary lambda syntax.

The finite rational operation trace's integer addresses are correctly separated
from the lambda AST's child-path addresses. The repair no longer calls that
finite arithmetic evaluator a proven omega-to-BBP compiler.

### Cofinality and Scott continuity

For an affine generator with nonnegative slopes, positive slope in each
coordinate is necessary and sufficient for cofinality. The implemented maximum
of two ceiling thresholds is the least simultaneous witness. Zero slopes are
handled as bounded coordinates, with unreachable targets rejected.

The alternating-axis counterexample correctly refutes separate unbounded
projections implying product cofinality for arbitrary sequences. Adding
coordinatewise monotonicity repairs that proposition. Finite prefixes now
produce an unknown truth state and are not accepted by the infinite checker.

The order-theoretic proof of joint Scott continuity from separate Scott
continuity is also valid: the projected sets of a directed subset are directed;
their rectangular product is directed; every rectangular pair is dominated by
a member of the original directed subset; joint monotonicity identifies the
two suprema. It avoids the unjustified topological-product identification.

## Executed probes

The focused existing suite was rerun:

```sh
python -m unittest tests.test_c_monoid_succ_embedding \
  tests.test_omega_trace_interpreter tests.test_scott_cofinal_schedule \
  tests.test_scott_omega_semantic_soundness -q
```

Result: **45 tests passed**, local Python run, 0.132 seconds. No full-suite or
hosted-CI result is inferred from this.

A separate scratch probe, deterministic seed `271828`, did not reuse the
existing named-substitution oracle. It generated simply typed open terms with
base integers, arrows and products, interpreted them directly in Python
environments, and compared the semantics before beta contraction, after direct
beta contraction, and after full normalization. This provides a different
implementation failure mode from syntactic substitution comparison.

| Probe | Scope | Result |
|---|---|---|
| Direct environment semantics | 400 generated open typed beta redexes, two independent environments each; functional results compared on three base arguments | 800 comparisons PASS |
| Exact budget boundary | Nested identity chains needing 1 through 49 beta steps; one-short budget must fail and exact budget must succeed | 49 cases PASS |
| Generic AST redex enumeration | Fresh holdout `2<=k<=13`, `1<=m<=15` | 180 cases PASS |
| Affine witness reachability/minimality | All starts/slopes in `{0,1,2}` and both target coordinates in `{0,...,5}` | 2,916 cases PASS |
| Runtime exact-state domain | Float initial state passed to the typed rational state API | Float result observed; boundary noted above |
| Source-horizon admissibility | Cofinal `(2k,k)` schedule | Correctly cofinal in product; outside `L>=n` for positive k |

All finite probes passed within their declared claims. They corroborate the
repair but do not prove universal reducer metatheory, a faithful BBP compiler,
or any original-zero arithmetic cancellation estimate.
