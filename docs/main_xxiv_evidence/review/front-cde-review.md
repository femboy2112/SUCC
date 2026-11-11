# Main XXIV independent C/D/E audit

Reviewer scope: same-model read-only mathematical review, followed by a narrowly
authorized runtime/test repair in a private detached audit worktree. No branch
push, merge, source archive rewrite, hosted certification, or full native suite
was performed by this reviewer.

## Exact inputs and audit assembly

| PR | Exact head | Role |
|---|---|---|
| #594 | 4a319fdf68b905c52f184ad06862d0eef17bca06 | Independent strict irrational-cut / category dossier |
| #595 | 857a159c69899ad556b0069834a4fbe7affd7b54 | Latest geometric observer plus aperiodic Round V |
| #596 | 88cd40b478ec823151cb6c08b04b67596efb3ada | Eight additive height-shield files |
| #597 | bc19dea9339b7a39b4761dc52a38126ade43ed67 | Nine additive zero-anchor files |

Worktree `/tmp/succ-xxiv-cde-audit` is detached at #597. It contains #595's
earlier 4e311d0 core. The exact #595 Round V directory and exact #594 dossier
were extracted from their heads into untracked audit directories. This is an
audit assembly, not a claimed integration commit. The Round IV core imported
by Round V is unchanged between 4e311d0 and latest #595. All checks below were
run freshly here; inherited logs are not substituted for execution.

`cde-eight-nine-file-hashes.json` records parent, tree, Git blob and SHA-256 for
each of #596's eight and #597's nine additions. Both ancestor-relative diffs
contain only additions, zero inherited edits/deletes. The repair below changes
two #596 runtime/test files, explicitly listed in the patch; all original bytes
remain reachable at the exact donor head.

## Findings and corrections

### F-E1: repeated height requests lose certificate ancestry (P2, repaired)

Original `height_shield/farey_height_shield.py:279` clears `runs` for every
`shield` call, but keeps `self.b` and `self.steps`. Concrete receipt:

```python
o = MacroObserver('circle_beta')
a = o.shield(10)    # steps=7, runs=2; verifier returns True
b = o.shield(100)   # steps=20, runs=1
verify_height_certificate(b)  # ValueError: broken arrow ancestry
```

The same defect applies after calling `next_run` before `shield`. The mathematical
Farey theorem remains sound; the producer emits a certificate its own independent
checker rejects. Repair retains the complete run history from the root. A request
whose smaller height would contradict the accumulated H-1 step receipt is now
rejected before issuing a certificate; `certify_height` remains the fresh entrypoint
for arbitrary independent heights. Regression compares expanded arrows with the
separate one-arrow source implementation at H=10,100,1000 for both source routes,
checks repeated H, verifies retained earlier runs, and covers explicit run then shield.

### F-E2: fractional final source clocks pass replay (P3, repaired)

Original verifier at `farey_height_shield.py:345` checks final clock order but
not integer type. Concrete receipt:

```python
c = certify_height(1)  # final_source_stage = 2
verify_height_certificate(replace(c, final_source_stage=1.5))  # True
```

The loop silently advances from stage 0 to stage 2 for a claimed stage 1.5.
This does not falsify the resulting rational separation, but accepts a false
exact source-clock receipt. Repair requires exact nonnegative integers for
`final_source_stage` and `steps`, and an actual Boolean for `complete_run`.
Mutation tests reject fractional, float, Boolean and negative count metadata.

Patch: `front-e-fixes.patch`, two runtime/test files only. No historical theorem,
receipt, or proof archive was edited. The updated height suite passes all 18
tests with the native source import enabled, zero skips.

## Mathematical review verdicts

- Numerical monoid categories, Karoubi corner maps, right-action categories over
  the base monoid, affine incidence inversion, matrix-family functors and divisor
  arithmetic retain their actual typing and composition. A bare monoid is not
  promoted to a CCC. Equivalences explicitly preserve their required base labels.
- #594 uses strict cuts on irrational objects. #595 Round III uses the closed
  restricted nerve `Hom_R(q,x)` on all real objects, and also separately uses
  rounded strict cuts for arithmetic. Strict/closed versions coincide on
  irrational targets but differ at rational endpoints. Preserve both descriptions
  with that boundary; do not deduplicate them as globally identical functors.
- Rational affine action groupoids are distinct from the real order category.
  On irrational affine orbits the action is free; on nonquadratic projective
  orbits the rational projective action is free. Bare groupoid equivalence forgets
  computational source and probe labels. The dossiers state this correctly.
- Stern–Brocot endpoint matrices have determinant -1 under column convention;
  L/R update matrices have determinant +1 and multiply on the right. The residual
  chart swaps generator conventions. Circle conic lifts act through PGL, so
  scalar representatives are not claimed faithful.
- The geometric source derives the Euclidean circumference/diameter ratio from
  the pulled-back metric. Rational beta and rational-rotation computations have
  exact strict intervals; neither supplies a runtime pi-value oracle. The
  nontrivial rational metric-distortion cocycle is retained. Fair L/R counting
  is not silently identified with geometric arclength.
- Productivity needs shrinking correct intervals and irrationality. Pairwise
  normalized-state distinction and universal periodic-tail rejection additionally
  require nonquadraticity. Strict state-potential decrease alone does not prove
  nonperiodic output; the quadratic periodic control is retained.
- The escape construction uses only N+p actual outputs before declaring its
  deadline. The first-mismatch witness index is j-p, not j. Exact polynomial
  ranges include an interior vertex, and strict cylinder widths pay the root
  separation cost. The mixed width contraction is <1/5; its stronger false
  1/6 rival retains the rational 35/204 counterexample.
- The Waldschmidt 1978 Corollary 3.2 import was freshly checked against the
  author-hosted primary PDF, printed page 452. Its height convention and
  `2^40 D(log H+D log D)(1+log D)` measure match the dossier. With D=2 and H>=16,
  the conservative exponent 2^43 follows. This import proves an enormous
  theoretical budget, not its physical execution or a new transcendence result.
  Source: https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/JAustralMS25-1978-445-465.pdf
- The Farey denominator identity `q=d(bp-aq)+b(cq-dp)>=b+d` is correct. It gives
  one universal H-bounded certificate, a strict rational margin and a source-
  refinement existence theorem. H-1 bounds emitted arrows, not source precision,
  bit complexity or wall time uniformly over arbitrary irrational inputs.
- The symbolic seed module Q+Qx with x=pi/16 has unique coordinates under imported
  irrationality. `16^-n U_n-P_n=s` is exact; the coherent seed (0,-1) and rational
  alias (1/16,0) remain distinguishable even when fractional phases alias.
  This is exact equality in the declared module, not arbitrary real equality.
- #597's finite Weyl budgets retain x=pi/16 versus alpha=pi scaling and Fourier
  turns versus geometric radians. Its signed-overlap interval-W1 error estimate
  uses a common hexadecimal chart; its exact seam counterexample excludes a
  global translation-Lipschitz claim. Neither finite overlap nor root identity
  proves statistical contraction.

## Fresh execution receipts

Python 3.12.3; commands use warnings-as-errors unless noted. Log files are in
the same evidence directory as this report.

| Gate | Result | Evidence |
|---|---|---|
| #594 two focused suites | 14 PASS | cde-cut.log |
| #596 original height suite with repository PYTHONPATH | 15 PASS, zero skips | cde-height-with-native-import.log |
| #596 repaired height suite | 18 PASS, zero skips | cde-height-repaired.log |
| #597 zero-anchor suite | 20 PASS | cde-zero.log |
| #597 build_receipt replay | PASS, generated finite_receipt.json byte-identical to donor | cde-zero-receipt-replay.log; git diff --exit-code |
| #595 Round II probe | PASS | cde-round-ii.log |
| #595 Round III order/computation/compiler probes | All PASS | cde-round-iii-{order,computation,compiler}.log |
| #595 geometric observer probe | PASS | cde-observer.log |
| Latest #595 aperiodic probe | PASS: 46 periods, 48 runs, 13 rejected mutations | cde-aperiodic.log |
| Latest #595 independent cycle probe | PASS: 1,016 algebra cases, 24,051 matched outputs | cde-independent-cycle.log |
| Long holdout (4003,31) | Deadline 24,121; first mismatch 24,050; witness 24,019 | independent-cycle log |
| compileall on all C/D/E Python sources | PASS | command executed, exit 0 |
| scoped git diff --check | PASS | command executed, exit 0 |

The first standalone height run skipped the optional native source import;
it was immediately rerun with the worktree root on PYTHONPATH, with zero skips.
This initial skip is not counted as native-source validation.

## Integration recommendation and remaining gates

Integrate exact #594 and latest #595 histories, then #597 (which carries #596)
without replacing #595 by the older 4e311d0 checkpoint. Regenerate one canonical
catalog after combining histories. Preserve independent category formulations,
counterexamples and tests under their distinct research namespaces; no conflicting
runtime import namespace was found. Apply the two-file height repair and rerun
the focused 18 tests plus all appropriate final-candidate gates.

C/D/E mathematics SURVIVES within the declared classical hypotheses. No remaining
P2+ mathematical defect was found in inspected claims. Full source-to-typed-lambda
reflection remains UNVERIFIED. Source-selected signed cancellation, original-zero
parity balance, base-16 pi normality and RH remain OPEN. This review is not external
refereeing or a formal proof-kernel check and grants no whole-tree/hosted CI pass.
