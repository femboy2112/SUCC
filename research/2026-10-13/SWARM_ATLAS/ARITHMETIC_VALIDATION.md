# Arithmetic cohort validation — E33–E40

Base: 5eb09e7cba36ec01b8f9d6834b78b5766fd93935.
Branch: research/swarm-e-2026-10-13. Independent arithmetic cohort.
No main merge, push, release, tag, default change or archival edit performed.

## Actual successful commands

| Exact command | Observed result |
| --- | --- |
| python -m unittest discover -s tests -p test_swarm_arithmetic.py | 21 tests, 0.327s, OK |
| python -m unittest discover -s tests -p 'test_*.py' | 1623 tests, 88.232s, OK |
| python scripts/verify_provenance.py | SOURCE_PROVENANCE_VERIFIED; 72 items, 17 byte-identical archives, 55 namespace migrations |
| python scripts/observer_foundations_probe.py | exit 0; expected source/semantic distinctions retained; RH_proved=false |
| python scripts/ordinal_succ_report_probe.py | exit 0; global_PSD_predicate_proved=false; no actual infinite ordinal computed |
| python scripts/swarm_arithmetic_probe.py --output research/2026-10-13/SWARM_ATLAS/ARITHMETIC_RECEIPT.json | exit 0; exact E33–E40 JSON receipt saved |
| /workspace/scratch/79b9e8091cb9/lean-root/lean-4.14.0-linux/bin/lean formal/Swarm_ArithmeticTransport.lean | exit 0, no output; six scoped theorem declarations checked under pinned 4.14.0 |

The Lean file includes affine representation/application and associativity,
successor shape, slope-2 rigidity, and a generic report-fiber no-classifier
lemma. It does not formalize the cyclic stabilizer classification, Euler
log support equivalence, Gamma completion, concrete covariance arithmetic,
Gaussian prime classification or a Weil sign. The compiler path is a
root-provided wrapper around the unmodified official 4.14.0 executable,
using the session's own-procfs compatibility fallback.

## Failure retained

The first targeted verbose run had 20 tests and one failure because the
expected unit-step Gaussian component size was written as 4. The exact
source enumeration returned {(1,1),(1,2),(2,1)}, size 3. The expectation
and budget mutation control were corrected, then all 20 passed. One
separate rational similarity positive control was added; the final 21
tests passed. No incorrect four-vertex receipt was frozen.

## Exact strongest witnesses

- At clock modulus 12, preserving successor and odd prime dilations
  3,5,7 leaves translation offsets 0 and 6; including dilation 2 leaves
  only 0. All permutations for moduli 1..7 were independently exhausted.
- Independent Omega-derivation convolution logarithms agree with ordered
  factor histories on 24 seeded random complex-rational prefixes to 24.
  Authentic zeta/chi5, fake-six, non-Euler mixture, nonunit-2 and altered
  prime-2-phase controls remain separated by distinct gates.
- True zeta coefficients and a(6)=-1 have exactly identical positive
  definite prime-valuation covariance at squared half-density weights,
  but b(6) is respectively 0 and -2. Thus covariance-only authentication
  fails even with genuine valuation features and the correct exponent.
- Actual Gaussian-prime components from 1+i have 3,100,720 vertices at
  squared step bounds 1,2,4; exhaustive neighbor closure verifies each.
- At N=17,z=2 the finite Gamma recurrence ratio is 17/10 and its retained
  boundary defect is 3/10. Projection zeros 6/5,3/2,9/5 move while source
  poles remain 1,2.

## Primary-source provenance correction

Search returned arXiv:2401.08441. Its primary record identifies Johann
Christian Stumpenhusen, a withdrawn manuscript and an incorrectly
computed moat width. It was rejected as theorem evidence; E39 preserves
this failed source lead explicitly. Its valid background instead uses
Gethner/Wagon/Wick publisher metadata and Conrad's Gaussian-integer
author notes. No local arithmetic certificate uses the withdrawn claim.

## Hole contract and dominance boundary

The paid dependency cut is source-faithful affine transport plus exact
coefficient interaction detection, not completed Weil positivity. The
two proven weak statements are the finite cyclic gauge classification
and log-support/multiplicativity equivalence. Both hold for declared
sources without assuming RH; fake-source controls prove that none
secretly identifies the missing Weil sign.

The unresolved statement is a phase-retaining identification of a
source-derived positive operator with Suzuki's completed form on its
actual smooth compactly supported zero-integral test domain. Its
hypotheses must include authentic Euler coefficients, true log-prime
frequency, half-density, conductor and Gamma/pole completion with the
appropriate limiting topology. Covariance-only routes are refuted;
the full identification remains unproved. A next verdict-changing
probe would mutate log 2 while leaving finite coefficient gates intact
and test the proposed analytic transport square. No unknown zero
position, source-invariant spectral zero, physical observer mechanism
or academic novelty is inferred from these finite runs.
