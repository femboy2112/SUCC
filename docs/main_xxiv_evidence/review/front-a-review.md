# Main XXIV Front A independent integration review

Review date: 2026-11-11. Scope: #589, #591, #592. Read-only source audit plus isolated runtime probes. This is a separate same-model agent, with a distinct environment-denotation and rational-CDF implementation; it is not external mathematical refereeing or kernel formalization.

## Verdict

**SURVIVES, with one small paper endpoint correction.** The canonical #591 source compiler and finite backend, together with #592's seed-resolution microscope, are suitable for integration within their declared finite/paper scopes. No source-selected asymptotic statistical contraction, original-zero parity, pi normality or RH is proved. The only confirmed incorrect mathematical statement found is the strict K=0 endpoint of #592 MS12; see below.

## Exact origins and ancestry

| Contribution | Pinned head | Parent/dependency | Role |
|---|---|---|---|
| #589 alternate compiler | `f4d79c6e0573ec9257d9e3f07b504ad3da24c25a` | #579 `3f1b67d6c319bf4ee9f42941da829cd1f778a3af` | Independent typed evaluator, recovered rational seed, guarded source intervals, cyclic and Pascal/cyclotomic controls |
| #591 canonical source compiler/backend | `41bbbe56bbb36bcbf2a171669bf508caea6f688b` | #584 `50481e49592af00d87c602f671a28f3503709de0` | Recompiling typed compiler, explicit SourceState passport and three-path seed verification, source-bound phase grid, signed chronological overlap, error-floor barriers |
| #592 microscope | `81c2dccb443e951b890ae55ad7a6f837c5609366` | #591 exact head above | Sixteen child seed-cell energy decomposition, fixed/deep-scale boundary, all-N first h=8 detail sign, fixed-depth signed fingerprint limit |

The #592 tree is `0df79db09f323078a640caee0b025d773b5c03fa`. At this tree `observational_succ/duck_bbp.py` has blob `34cb7b64f6975e05586ec220a4655961a8e7b636` and `provenance/IMPORT_MANIFEST.json` has blob `a8805a8e4d64f35ff61937a36755d9b6d1ba3fae`. Both are unchanged between #589 and #591.

## Canonicalization and collision handling

There is an add/add path collision at `research/2026-11-10/zero_anchored_lambda_haar/README.md`. #589 and #591 independently added different substantive documents there. The documents are not byte duplicates: comparing the two blobs reports 141 insertions and 173 deletions. Choosing either side without retaining the other would lose provenance and useful mathematical exposition.

Prefer #591's maintained README and compiler/backend as the canonical contract:

- `observational_succ/zero_anchored_lambda.py`
- `observational_succ/zero_anchored_haar.py`
- `scripts/zero_anchored_lambda_haar_probe.py`
- `research/2026-11-10/zero_anchored_lambda_haar/{COMPILER,CONSTRUCTION,BACKEND_PROOFS,HOLE_CONTRACT,ADVERSARIAL}.md`

Preserve #589's original README as a clearly identified alternative archive and preserve its meaningful tests/controls. Its `observational_succ/zero_anchored_lambda_haar.py` has a distinct module name, so it does not create a Python import collision. It need not be exposed as a second canonical runtime API: its value is an independent finite reference implementation and the cyclic/Pascal tests. If relocated to research, preserve original bytes and adapt only the import/path wrapper and record the destination. Its direct source-function calls and Q(seed) conversions have weaker boundary checking than #591, so it should not inherit #591's hardened source-certificate claims.

The seed-state presentations are compatible but distinct: #589's State stores `(n,u)` and derives the seed; #591's SourceState also stores the claimed seed and passport, then checks forward/prefix/reverse agreement. Do not alias these classes or imply an identical certificate format.

## Confirmed repair

**P3: MS12 strict inequality fails at K=0.**

Location: `research/2026-11-10/zero_seed_microscope/MICROSCOPE_THEOREMS.md:264`, also the proof's strict inequality at line 279. The statement quantifies K>=0 (line 246). For K=0, MS1 gives E_(N,0)=1/N and the sum A_(0,h)=0 is empty. Therefore the claimed strict bound reads `0 < 0`, which is false. The implementation correctly returns zero from `fixed_depth_scaled_limit_tail(0,h,N)`.

Repair: use `<=` in MS12 and in the final rational-tail comparison, adding that equality holds at K=0 and strictness holds for K>=1. Alternatively separate K=0 explicitly and restrict the strict formula to K>=1. This does not weaken the fixed-depth limit or any normality boundary. An additive erratum can preserve the historical dossier bytes if archive policy requires it.

No P2 or higher defect was established in the audited finite/compiler/overlap claims.

## Executed verification

All commands were run in clean detached worktrees, using the genuine repository package rather than a test shim. Full native suite and hosted CI were deliberately not run by this reviewer; they belong to root's final-candidate gate.

1. At #592 exact head:

   `python -W error -m unittest -v tests.test_zero_anchored_lambda tests.test_zero_anchored_haar tests.test_seed_microscope`

   **PASS: 71 tests in 1.525 seconds.** Raw log: `front-a-focused.log`.

2. At #589 exact head:

   `python -W error -m unittest -v tests.test_zero_anchored_lambda_haar`

   **PASS: 19 tests in 1.215 seconds.** Raw log: `front-a-alt-focused.log`.

3. Additional seeded independent probe, seed 20261111:

   `PYTHONPATH=/tmp/succ-xxiv-front-a-audit python /tmp/succ-main-xxiv-evidence/front-a-independent-probe.py`

   **PASS:** 500 generated closed well-typed rational/source expressions, each checked under both normal and applicative beta/delta strategies against an environment-based evaluator using independently written polynomial forcing. Zero-step exhaustion retained unresolved status and no value. **PASS:** 300 randomized exact rational CDF partitions checked all three block defects and the signed-overlap identity against a separate Fraction-valued atomic integrator, including radix branch seams. Script and complete output are retained in this evidence directory.

## Mathematical audit bearings

- The de Bruijn lowering in #591 uses the corrected shift/substitute/unshift implementation from `c_monoid_succ_embedding`; nested lambda/open-in-binder cases are exercised independently by the generated environment oracle.
- Source-state replay preserves the unwrapped seed and literal zero. A 1/16 rational seed can alias later fractional phases while failing the original-zero requirement. The source contract retains all four signed poles. The compiler's finite tail contraction is explicitly distinguished from the open sample-length statistical contraction.
- The source grid enclosure correctly accounts for each floor loss and the positive tail, checks an entire small cell before assigning its digit, and rejects unresolved seams. The backend's 2/q defect error and 4/q signed-overlap error are valid within those certified charts; they are not global Lipschitz claims for the discontinuous interval projector.
- The signed overlap implementation exactly integrates `min(|H_-|,|H_+|)` where CDF signs differ and uses `D_union=(D_-+D_+)/2-Omega`. Negative/constant-orbit controls retain zero overlap and nonzero defect. A positive overlap on finitely many windows does not establish its missing asymptotic lower bound.
- Sixteen-child seed-cell Haar details in #592 are distinct from chronological CDF overlap in #591. The fixed-K fingerprint coefficient is a convergent signed series with geometric truncation bound, while deep K=N-o(N) cancellation remains the original Weyl-equivalent open problem. The all-N first h=8 seed-cell detail sign is O(N^-2) information, not digit parity.
- The first-detail sign proof uses rational Machin bounds to place delta in (3/8,2/5), an alternating sine estimate and an absolute geometric tail. Its source/phase scope is stated: any source with selected value pi/16 has that same first packet.
- The no-all-N theta<1/2, epsilon_N=O(1/N) remainder corollary in #591 was checked against the primary paper: Kritzinger and Pillichshammer, *Exact order of extreme L_p discrepancy of infinite sequences in arbitrary dimension*, Theorem 1, explicitly includes d=1,p=1. The abstract only says p>1, so checking the theorem itself matters. Primary PDF: https://link.springer.com/content/pdf/10.1007/s00013-021-01688-9.pdf ; theorem appears on printed page 172. The inequality from extreme L1 discrepancy to star L1 discrepancy follows by integrating the triangle inequality over u<=v, and star L1 discrepancy equals N times interval W1.

## Remaining gates and next discriminant

Root must replay the focused suites against the reconciled final paths and exact final candidate, verify provenance/catalog, run the mandatory native suite, and check hosted review/protection requirements. This review does not certify those future bytes.

The next result that would change the mathematical frontier is a source-derived, uniform all-large-window signed estimate on the actual original-zero innovation or CDF overlap, retaining integer carries and future-tail/branch payments, that rejects both coherent wrong seeds and the positive four-pole telescoping mutant. Neither evaluator convergence, source identity, spatial seed averaging, finite certificates nor one fixed-K positive Fourier packet supplies it.
