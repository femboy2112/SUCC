# Theorem Forge II: source, claim and dependency audit

**Research branch:** `research/theorem-forge-ii-2026-10-19`.
**Integration base:** PR179 `81684b4b8956f9f5da56c376ba7e4339277eb665`.
**Verdict:** five scoped research targets completed with full paper proofs,
countermodels, exact certificates and a preserved analytic obstruction.
No established academic novelty is claimed. **RH PROVED: NO.**

## 1. Live state, ancestry and preservation

The live heads were fetched before development. Exact metadata and the four
successful PR-triggered baseline CI runs are in `BRANCH_SOURCE_SNAPSHOT.json`.

| Object | Pinned head | Relationship to this work |
|---|---|---|
| main | `610efacf02556e1c5922bc5d4e87d0087f19b446` | Integrated historical base, unchanged |
| PR176 | `a17197697c0ea0259592500b233419fbedf691cf` | Separate arithmetic/operator line; not an ancestor of PR179 |
| PR177 | `f309d9104ba480c1999c962af1df7c50f19e1bfe` | Direct parent of PR179; original continuum source evaluator |
| PR178 | `e42096ec0186228dd0f748767599e470f2ca2e1d` | Sibling from main; selectively reconstructed, never merged wholesale |
| PR179 | `81684b4b8956f9f5da56c376ba7e4339277eb665` | This branch's implementation baseline |

All four PRs were open drafts, not merged. Six isolated worktrees began at
PR179. Scoped commits were reviewed and cherry-picked, with distinct histories
retained. No frozen source, license, toolchain pin, main branch, tag or release
was changed. The original signed Suzuki blob remains
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`.

The inherited PR179 full local run had 5,356 passing tests; its four observed
hosted workflows are now successful. Fresh predevelopment checks included
source provenance (72 items), the academic probe, future-safe quotient (18),
arithmetic source minimality (10), Gamma refinement (8), and the extracted
PR178 atomic/Haar suite (10). These are baseline evidence, not the new branch's
CI status. Integrated validation is recorded separately in
`VALIDATION_RECEIPT.json` and its compressed full-suite log.

## 2. Compatible interfaces, with their universal properties

The theory uses a source carrier, existing representation, declared task outputs,
and lawful operations. Every theorem is relative to that complete model; none
authenticates a physical source from an internal label.

| Question | Object and exact property | Missing implication / countermodel |
|---|---|---|
| Can reports predict chosen future outputs? | Behavioral equivalence for the chosen task language | A refinement of a predictive quotient need not update autonomously |
| Can the representation update itself? | Greatest stable equivalence `R*` refining `ker(q)` and all declared task/cost/refusal outputs | Equality of original behavior intersected with `ker(q)` need not be stable; future `q` must also propagate |
| What is the least autonomous repair? | Every sufficient surjective repair factors uniquely **onto** `X/R*`; auxiliary alphabet is the maximum number of `R*` classes per `q` fiber | An encoder's existence supplies neither a lawful instrument nor free access to private state |
| Can the original repair class be learned? | Beliefs carry `(original,current)`; exact terminating acquisition values and ranks | Destructive acquisition can learn an original class while destroying the current carrier's task capability |
| How much prior advice suffices at cost C? | Weak coloring of minimal infeasible source subsets | Pairwise distinction does not characterize joint acquisition; three-way hyperedges are necessary |
| Does each finite abstract history lift? | Original-preserving private-history existence, separately for each request word | PR179 three-state example lifts every finite word but has no online resolver |
| Can requests be realized causally? | Finite safety greatest fixed point; public version uses declared commands and complete outcome rows | Identical private edges can have opposite public winners under different command interfaces |
| Can probes repair public control? | One-step fixed bundles hit every minimal conflict hyperedge | Full-information structural losers cannot be repaired by nondestructive observations; no coarsest winning partition in general |
| Can finite interfaces pass to infinity? | Uniformly bounded operator transport tested in WOT; or completion in a stated test topology | Finite-prime unitaries converge weakly to zero and have no strong limit; distributional completion loses the atomic Hilbert interface |

The finite hereditary-family lemma is the common mechanism behind advice
coloring and fixed-probe hitting sets. It does **not** identify their resources:
arbitrary prior advice, a prescribed lawful probe menu, final stored state, and
temporary controller memory differ. A combined theorem for destructive probes,
bounded controller memory and subsequent online task execution remains open.

PR178 treats its source label as a private invariant. PR179's machine semantics
preserve source as an output. Their successful-run adapters require an explicit
current-report law. PR178's `Option.none` loses an executed prefix that PR179's
trace retains. The Lean adapters prove precisely the compatible part and include
countermodels for the unsupported identifications. A general sheaf of event
histories or physically authenticated source theory has not been reconstructed
by renaming these finite interfaces.

## 3. What is proved

| ID | Statement | Proof and exact authority |
|---|---|---|
| F2-A1 | Greatest stable repair and sharp fixed-width auxiliary label bound | Paper A, classical partition refinement and counting; exact finite verifier |
| F2-A2 | Exact proper acquisition cost with all-action lower and decreasing-rank upper certificates | Paper A, finite proof; stored 13-belief certificate independently replayed without synthesis |
| F2-A3 | Minimal prior advice at budget C equals chromatic number of minimal-infeasible hypergraph | Paper A; exact frontier `(2 bits,0),(1 bit,1),(0 bits,2)`; three-source destructive countermodel |
| F2-B1 | Exact private and public sure-safety winning regions and losing rank certificates | Paper A/game dossier; declared `forall request exists command forall outcome` quantifiers |
| F2-B2 | Structural observation no-go, exact fixed-probe hitting-set repair, no coarsest winning observation | Paper A; explicit command-interface and triple-conflict countermodels |
| F2-C1 | Finite Euler reflection about any nonzero real center forces identical multisets | Paper C; equal cardinality is a conclusion; multiplicities and coincident powers covered |
| F2-C2 | Positive tempered Fourier-selfdual measure with normalized unit gap is the integer comb | Paper C; Gaussian-regularized sinc-squared extremal argument, no premature distribution pairing |
| F2-C3 | Positive generalized word source with exact Gaussian completion, stated poles/residues and uniform strip decay is ordinary arithmetic | Paper C; Mellin contour proof, Gaussian separation and atom at one force residue one; source contract not derived from observer axioms |
| F2-D1 | Uniformly bounded finite-prime **forward** intertwiners tend WOT to zero when reciprocal primes diverge | Paper B; adjoints are unnecessary; finite backward eigenvector norm and dense cylinder tests |
| F2-D2 | Star intertwiners have exact shell support and sharp coefficient bound; summable-prime complement classified | Paper B; bound `M ||g||infinity sqrt(alpha_F/d_F(n))`; no strong subsequence for finite-prime unitaries |
| F2-D3 | A chosen integer-Dirac map completes to weak distributions for the locally constant test topology | Paper B; explicit dense interpolation and universal extension; normed-target maps factor through a finite cylinder |
| F2-E1 | Source-relative finite-rank inverse upper and nonorthogonal-coefficient residual identity | Analytic dossier; classical closed-form projection/inverse order; genuine high-domain premise |
| F2-E2 | Every response matrix and PSD payment in the retained rank-two certificate family fails | Analytic dossier and exact interval receipt; eight strictly negative rational witnesses, not negativity of the source form |
| F2-E3 | Explicit Gamma form closure, constrained compact core and primitive response domains | `ORIGINAL_SOURCE_FORM_CLOSURE.md`; classical paper proof, independently audited; source identity/coercivity remain separate premises |
| F2-F1 | Exact quotient adapters and positive/negative source-game certificate soundness | 15 new actual Lean declarations, 14 historical rebuilt; eight game declarations axiom-free |

The most substantial new repository-level theorem is F2-D1: forward equations
alone force bounded atomic-to-Haar disjointness in the divergent-prime regime.
It strictly strengthens the hypothesized star-only result. The positive-gap
rigidity lemma supplies a separate infinite arithmetic identification route.
Neither has a verified academic-priority claim.

## 4. Dependency cuts and remaining analytic obligations

F2-A1 depends on deterministic partial transitions and declared task semantics.
F2-A2/A3 use a separate lawful acquisition interface. F2-B1/B2 depend on complete
private outcomes and public commands; the source relation alone is insufficient.
The finite realizability theorems do not imply an infinite uniform completion.

F2-C1 depends only on finite positive bases and exact meromorphic reflection.
F2-C2 depends on positivity, the unit gap and distributional self-duality.
F2-C3 derives self-duality only after continuation, pole and contour-decay
hypotheses are supplied. Density one and residue one need not be separate
hypotheses under that stronger contract. Deriving that contract from independent
source axioms remains an open source-identification problem.

F2-D1 is RH independent and has no signed-Weil premise. Adjoint equations are
load-bearing for F2-D2's support bound, not F2-D1's weak collapse. The summable
star classification is not a classification of all forward intertwiners.
The universal property in F2-D3 is relative to the explicit initial test
topology; it does not select the unit vacuum or preserve the Hilbert norm.

For F2-E1, low primitives are not orthogonal coordinates on `E^perp`.
The correct source formula uses a finite coefficient map F, `A=F*HF`,
`B=Q_EHF`, and the closed high form D. The separate closure/core proof shows
that the inherited all-input core estimate extends legitimately. It does not
prove the signed-Weil source identity or re-prove the inherited Bessel bounds.
The compact E2 verifier checks the retained enclosure arithmetic and archive
digest; it does not authenticate those enclosures by repeating the costly
source extraction. That extraction and fresh source holdouts are separately
recorded. Nontrivial zeta-zero ordinates are not construction inputs.

The rank-two optimistic e1 caps are below `-0.000482157981535073` (odd
derivative block) and `-0.000458846398602338` (even block). This excludes all X
only with the **fixed retained** `T,M,K_upper,V_hat` and PSD payments.
It does not bound the ideal family with improved true-source K,V enclosures.
No first-window Schur positivity certificate was obtained; no negative
original-source test was obtained either.

## 5. Hostile audits and corrections

Independent work means separate derivations and code paths here, not external
human review or independent model training. Six bounded agents and the principal
worked from pinned sources; the principal read all three complete manuscripts.

* Arithmetic proof checked by principal and formal lane: remove equal-count
  hypothesis; retain the necessary nonzero reflection center; use dilated
  Hermite functions with the correct Gaussian scaling.
* Operator proof checked by principal and formal lane: forward adjoint equation
  is legitimate without assuming star intertwining; all-prime weak collapse
  survives. The normed-target finite-rank obstruction limits universality.
* Closure checked independently: correct the wording from Fourier transform
  to convolution multiplier under unitary normalization; use a nonnegative
  unit-mass mollifier and nonredundant parity constraints.
* Analytic result rederived by arithmetic lane: all eight rational caps reproduced,
  retained M/K lower matrices positive definite. A real checker defect was found:
  missing `M>=0` would accept `T=-2I,M=-I,K=I,V=0` although positive Young
  parameters can reverse that conclusion. The verifier now checks this premise,
  interval symmetry, and archive SHA256, with a failing-input regression.
* Games checked against explicit strategy enumeration (256 tiny arenas and 60
  fresh three-state models), plus a raw-private-history policy-tree oracle
  (256 command tables, 768 initial-belief cases).
* Acquisition checks use exhaustive partitions on 160 fresh four-state models
  and direct original-state policy simulation on 90 fresh models. The latter
  shares the generated belief universe, so its independence is limited; a
  separate raw-policy audit now rebuilds beliefs from raw tables: 6,561 exhaustive
  two-carrier tables, 140 fresh three-origin models, 482 advice-budget comparisons,
  1,527 false-value and 497 false-rank rejections, no skips. See
  `FOUNDATIONS_ACQUISITION_AUDIT.md`. It also repaired a proof sentence:
  root-optimal trees can have suboptimal slack branches. The corrected minimal-
  value/shortest-tree argument proves completeness of optimal-action ranks.

The Lean kernel checks soundness declarations, not Python fixed-point generation,
belief compilation, cardinality bounds, real analysis or RH. One positive
calibration is accepted and four false controls rejected under unchanged Lean
4.14. No `sorry`, extra axioms, `unsafe`, or `native_decide` are admitted.

## 6. Prior art and manuscript status

Paper A compares Moore/Nerode refinement, Rutten coalgebra, Witsenhausen
zero-error coloring, adaptive/incomplete distinguishing sequences, safety games,
alternating simulation and imperfect-information subset constructions.
Hierons--Turker's incomplete-sequence covering is particularly close to the
feasible-block formulation. The full combined formulation's novelty is unverified.

Paper B compares finite Wold decompositions (Sarkar), infinite Beurling-generation
conditions and missing joint defects (Dan--Guo), and arithmetic operator-algebra
context. Countable Wold failure and generic topological completion are classical.
No theorem is inferred merely from an adjacent Bost--Connes citation.

Paper C compares Hilberdink--Lapidus generalized functional equations, Hamburger
converses and Burnol's distributional extensions, and Fourier eigenmeasure work
of Baake--Spindeler--Strungaru. Positivity and a unit gap are real extra hypotheses;
self-dual nonlattice controls are supplied. The sinc argument is classical in
method; priority for this formulation remains unverified.

The analytic inverse ingredients are classical Schur/shorting and finite-rank
inversion (Anderson--Trapp context). Suzuki's primary source already establishes
localized closed-form/operator theory; the explicit repository core proof is
not presented as discovery of form closure.

The three PDFs are technical manuscript drafts with complete local proofs,
countermodels and references. They are not claimed publication-ready or refereed.

## 7. Reproduction

The source comparison reads a receipt from sibling PR178. A fresh shallow
checkout must fetch that exact object first; ancestry is not changed by fetching:

```sh
git fetch --no-tags --depth=1 origin e42096ec0186228dd0f748767599e470f2ca2e1d
```

The first hosted exact jobs at `ec9895d4baab1b8c5a0713f87bdbd5aadfc07338`
passed all 47 tests but failed at that missing Git object. The dedicated workflow
now fetches and verifies the pinned commit before replay. This is a checkout
repair, with no mathematical implementation or certificate changed.
The fetch was reproduced in a fresh shallow repository and the extracted
130,168-byte receipt matched its pinned SHA256 exactly.

```sh
python scripts/verify_provenance.py
python scripts/theorem_forge_probe.py
python -m unittest tests.test_information_repair tests.test_online_source_games tests.test_finite_euler_rigidity tests.test_forge_operator_transport tests.test_directional_source_inverse -v
python scripts/directional_source_inverse_probe.py --verify --source-holdouts --reconstruct-pr178
python scripts/verify_forge_formal.py --lean /path/to/lean-4.14.0
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The costly original J24 source calculation is optional, explicit and serial:
`python scripts/directional_source_inverse_probe.py --run-source --verify --output /tmp/forge.json --raw-gzip /tmp/forge-raw.json.gz`.
Build papers from `research/2026-10-19` with two pdflatex passes; Paper A must
include its companion online-realization section. Render every final PDF page
for layout review. The dedicated workflow repeats finite checks, fresh analytic
holdouts and actual pinned-kernel validation; general CI runs the full suite.

## 8. Final research ledger and next verdict-changing lemma

| State | Scope |
|---|---|
| PROVED | F2-A through D paper theorems; E identities, selected-family obstruction and explicit closure/core; listed countermodels |
| CLASSICAL | Partition refinement, safety games, subset beliefs, hypergraph mechanism, Wold models, completion, Schur/inverse principles |
| KERNEL-CHECKED | 15 new declarations and 14 historical dependencies; exact declaration/axiom manifest, not whole manuscripts |
| SOURCE-CONDITIONAL | Application of original inverse theorem to canonical Weil source and inherited high coercivity; deriving the completed arithmetic contract |
| TESTED EXACT MODEL | Finite oracle comparisons, rational certificates, signed original-source holdouts and retained J24 family witnesses |
| CONJECTURED | A sharper source-valid response family could yield a positive S4 margin; no assertion that it will |
| UNVERIFIED | Academic novelty, publication readiness, physically authenticated carrier semantics, all-radius positivity and RH |
| REFUTED | Pairwise distinction suffices for joint acquisition; offline lifts ensure online policy; edges determine public control; coarsest online repair always exists; adjoints are necessary for weak collapse; these fixed rank-two certificates can be rescued by tuning X/Young/PSD payments |

**Exact next analytic lemma:** construct source-valid high response columns whose
paid mixed-action enclosures yield a certified positive lower for the actual
original four-coordinate Schur form, in the correct derivative metric. An
optimistic finite PSD compression or a different contact is not that lemma.
Even its proof would leave all-radius Weil positivity and RH separate.

**Next unification lemma:** characterize the minimal retained advice and bounded
controller memory needed for destructive lawful acquisition followed by a
source-faithful winning online policy. Require an explicit restoration/simulation
condition; diagnosis of the original class alone is insufficient.
