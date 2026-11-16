# OpenAI Yang–Mills existence: source and verification audit

**Audit date:** 2026-11-13. **Scope:** the public October 28 submission and the
working group's November 10 assessment. **Local result:** source integrity and
four normalized declaration correspondences passed. No Yang–Mills Lean theorem
was compiled or kernel-replayed by this SUCC round.

## 1. Verdict and provenance

The Facebook report has a substantial mathematical event behind it. The
Yang–Mills working group endorses an existence construction of a four-dimensional
relativistic quantum field theory from Wilson lattice gauge theory. Its stated
scope does not include a positive mass gap or uniqueness of the infinite-volume
limit. Consequently this release does not complete the Yang–Mills Millennium
problem. This is a report of the committee's judgment and its formal evidence,
not a claim that this SUCC audit independently proved the construction.

The following revisions were retrieved from GitHub. The assessment repository
was also cloned, and its local HEAD was checked.

| Source | Pinned revision | Role |
|---|---|---|
| `yang-mills-group/YM` | `55ba9fc36293b3f4d52c6b1f813169a0be76ee98` | Assessment, original-source copy, review specifications, dated verification records |
| `yang-mills-group/OpenAI-YM-20261028` | `3456e5e75cf8d4cd558955a5c7638fba2d68f464` | Separate original submission repository |

The [committee README][committee] identifies its assessment as November 10 and
lists the November 4 submission as unfinished review work. That later submission
is outside this audit. The November 9 [committee announcement][statement] and
October 26 [OpenAI announcement][announcement] establish the release chronology;
the later public files establish the inspected technical scope. No attempt was
made to identify the user's particular Facebook post.

[upstream_manifest.json](upstream_manifest.json) lists 24 inspected upstream
files, their exact byte lengths and SHA-256 hashes, immutable URLs, and the scope
of reading. Hashing an entire file does not mean every declaration in that file
was semantically audited. The assessment PDF was extracted to text; the relevant
construction, validation, and selected glossary sections were read. The underlying
proof library was not exhaustively reviewed.

A subsequent bounded native-code audit is recorded in
[RG_IMPORT_MAP.md](RG_IMPORT_MAP.md). Its 14 linked files have a separate
`native_rg_inspected_files` section in the manifest. This supplement traces
one genuine uniform-correlation theorem and its immediate inputs; it is not
a claim to understand or replay the entire renormalization construction.

## 2. Exact existence statement and its common witnesses

The public input in `PublicTheory.lean` is a closed matrix subgroup
\(G\subset U(m)\), with a real Lie algebra identified through one-parameter
subgroups. `GaugeGroup.IsSimple` requires noncommutativity and the absence of
proper nonzero Lie ideals. Thus the nonabelian condition is explicit.

The public `JointExistence` in [ChallengeSpec.lean][challenge] has this order of
choices:

\[
\forall G\text{ allowed},\quad
\exists C\text{ a Wilson family},\quad
\operatorname{Regular}(C)\ \land\
\forall p:\mathbb N\to\mathbb N\text{ strictly increasing},\quad
\exists q:\mathbb N\to\mathbb N\text{ strictly increasing},\quad
\exists T\text{ a hierarchy for }C,
\quad \operatorname{Properties}(T,p\circ q).
\]

The family precedes the requested volume sequence. The properties combine the
lattice limit, reconstruction, separated operator product expansion (OPE), and
the specified trace nonfreeness test for the same hierarchy.

The [assessment][assessment], section 9, identifies a weakness in that public
endpoint: it exposes fewer connections to the native lattice construction than
the proof establishes. The working group's stronger
`YMReview.Acceptance.combined_acceptance` retains the construction certificates.
Its [specification][acceptance] and [assembly proof][combined] quantify as

\[
\forall G,\ h_G,\ b>0,\quad
\exists C,\ \operatorname{penalty}(C)=b\ \land\
\forall p\text{ an extraction order},\quad
\exists q,S,F,\quad \operatorname{Accepted}(G,h_G,C,p\operatorname{.refine}q,S,F).
\]

Here one `Spec.Final` witness \(F\) carries all accepted clauses. The lattice
clause uses the full chosen ultraviolet order and the refined infrared order.
There are no fresh per-clause selections of theory, centered trace, or stress
tensor. This is the most direct proof-engineering transfer to SUCC: source
binding and shared witnesses are part of the theorem statement.

The separate `YMReview.OPE.constructed` endpoint has its own existential
hierarchy. Its verification alone does not identify that hierarchy with the
one selected by combined acceptance. The adapter `from_source` can instead be
applied to an OPE property already available on a chosen common witness. The
[check-scope document][checks] states this distinction explicitly.

## 3. Construction and limits

The public Wilson family starts with normalized finite-lattice plaquette laws
against product Haar measure. Insertions are continuous and gauge invariant;
each insertion has a fixed finite stencil in lattice units across cutoffs and
volumes. An independently specified lattice-law adapter checks agreement after
the convention change \(\beta_{\rm submission}=m\beta_{\rm lgt}\).

At suitable fixed physical volumes, separated test-function correlations converge
along the complete lattice-spacing sequence chosen by the construction. The
inverse bare coupling has the required positive logarithmic growth, uniformly
in volume. The construction does not establish convergence for every possible
regulator sequence or universality under arbitrary regulator choices.

After that ultraviolet limit, every increasing volume sequence admits a
subsequence on which all finite correlation lists and admissible tests converge
together. This is a compactness/extraction result. It neither interchanges the
two limits nor identifies the limits of different volume subsequences. These
statements and their quantifier boundaries are exposed in the
[OctoberChain walkthrough][chain].

The mixed limiting hierarchy is decomposed using the character space of a
commutative ground-state operator algebra. The algebra consists of actual field
word operators compressed to the vacuum subspace of the reconstructed Hilbert
space. Gelfand representation and Riesz–Markov produce the phase space and
probability measure. Products of phase readings are tied to products in this
algebra, not merely to a fitted barycenter.

The component hierarchies cluster and reconstruct to Wightman theories. The
selected theory has positive energy, a normalized cyclic vacuum, fields on a
common dense domain, Poincaré covariance, spacelike locality, and a unique
translation-invariant vacuum within that component. This last conclusion is
different from uniqueness of the mixed vacuum, agreement of all components, or
uniqueness across volume limits. [Public reconstruction definitions][publictheory]
and [OctoberChain][chain] make the objects behind those assertions inspectable.

For SUCC, none of these analytic conclusions automatically follows from having
operators, a positive covariance matrix, or gauge terminology. The exact
arithmetic source and the required limit estimates would need their own proof.

## 4. Nontriviality, OPE, and the missing mass gap

For the selected component's centered stress trace \(\Theta\), the submission
proves the short-distance law

\[
\lim_{r\downarrow0}r^8\log^2(1/r)
 S_{\Theta,\Theta}(-re_0/2,re_0/2)
 =\frac{3\dim_{\mathbb R}\mathfrak g}{\pi^4}>0.
\]

The source also excludes a stated class of finite combinations of finite-mass
free-field Wick profiles. This is meaningful nontriviality evidence, but it is
not a theorem excluding every description by composites of Gaussian fields or
continuous-mass generalized free fields. `Hierarchy.TraceTest` gives the exact
predicate; the [original README][original] distinguishes its public and stronger
native countertests.

The separated OPE has common coefficients and remainder bounds at every fixed
field-degree truncation, uniformly over phases and the stated separated
configurations. Degree is not a perturbative loop order. The [OPE
specification][opespec] and [adapter][opecheck] do not prove all-orders
perturbative matching or coefficients independent of every choice of
infinite-volume subsequence.

The mass-gap assertion would require some \(\Delta>0\) with
\(\operatorname{spec}(H)\subset\{0\}\cup[\Delta,\infty)\) in the relevant
continuum theory. Positive energy alone does not give this separation. Neither
the October construction nor its committee acceptance claims that bound. A
positive fixed smeared two-point probe, called `MassLimit` in one review
interface, does not establish a positive intrinsic reference mass or a spectral
gap. This naming distinction is documented in [check scope][checks].

The assessment's remaining tasks also include a continuum probability measure
realizing these correlations, Wilson-loop observables and their relation to the
local fields, an area law, and a particle/spectrum analysis. No corresponding
SUCC result is claimed here.

## 5. Independent OS comparison and its domain

The review translates the selected centered-trace scalar hierarchy into OS
axioms formulated independently before this submission. It preserves the
chosen field, state, and correlations; its analytic proof input still comes
from the submitted construction. An independently chosen specification is not
an independent construction of the analytic estimates.

The comparison uses Schwartz functions flat to every order on coincidence
diagonals. Such tests may approach a diagonal but cannot detect distributions
supported on it. The adapter establishes the required integrability and growth
on that domain. It does not separately translate every tensor field into a
full unrestricted Euclidean OS interface. The source separately reconstructs
tempered Wightman distributions, and supplies Euclidean contact extensions;
those statements must not be silently substituted for one another. The
independent comparison does not establish uniqueness or unrestricted Euclidean
positivity of all contact extensions. See [check scope][checks] and assessment
section 10.

## 6. Three verification layers that must remain separate

| Layer | Evidence and result | Boundary |
|---|---|---|
| Submitted verifier | Original reports describe statement/definition comparison, axiom audit, and fresh-environment Lean kernel replay of 100,168 project declarations supporting 17 headline results | The original package reports that its standalone Comparator executable was not run |
| Committee verification | Later dated records report a clean source build and separate upstream Comparator runs for public existence, combined acceptance, and the OPE endpoint | These later runs do not turn every unused declaration into an audited theorem or validate unasserted physics |
| This SUCC audit | Fresh execution of the upstream `integrity` stage passed | No Lean build, theorem replay, or Comparator stage ran here |

The original declaration inventory covers 250,319 imported project declarations;
100,168 are in the dependencies of its 17 audited results. The documented
permitted axioms are `propext`, `Classical.choice`, and `Quot.sound`. The
deliberate reference theorem in `Challenge.lean` uses `sorry`; `Solution.lean`
imports construction and definitions without importing that reference proof.
The solution's dependency check, not a raw text search for `sorry`, is the
relevant formal test. These facts are documented in the [original verifier
description][original] and later [evidence chronology][evidence].

The committee reports Comparator acceptance of the public endpoint on October
30, combined acceptance on November 3, and the OPE endpoint on November 5.
Its negative controls reject a changed proposition, an added axiom, and a
changed definition; a valid control is accepted. These are recorded upstream
runs, not controls rerun by this SUCC audit.

Those Comparator runs used pinned tools and the built-in Lean kernel in the
recorded macOS development mode, without Linux/Landrun isolation or an additional
external kernel implementation. The checks therefore concern statement,
definition, axiom, and kernel acceptance in that mode. They do not establish
isolation from hostile build processes. The assessment also acknowledges that
human mathematical understanding is incomplete and used model assistance during
review. Kernel acceptance does not resolve whether an incorrectly chosen
definition expresses the intended physical problem. [Reproduction
instructions][rerun] disclose these limitations.

## 7. What was run here

From the pinned assessment package, the following command completed successfully:

```sh
python3 scripts/verify.py integrity \
  --run-dir /workspace/scratch/87e770cb18ab/ym-integrity-20261113
```

The working directory was the cloned repository's
`submissions/openai-20261028/`. The original JSON receipt is preserved byte for
byte as [upstream_integrity_receipt.json](upstream_integrity_receipt.json). Its
SHA-256 is
`7d6dfc3f12c52dd612c7a5387d10b03d4debaf900965249190205c5907b894dd`.

The run checked 9,508 submitted files, 43 review modules, and packaged inputs
against their manifests before and after the stage. It also compared four whole
OS declarations after the upstream's documented text normalizations:
`OSInnerProduct`, `OsterwalderSchraderAxioms`, `OSArityLinearGrowthCondition`,
and `BorchersSequence`. All passed. The receipt explicitly records no initial
submission build. Its `comparator_mode` field describes the runner's available
configuration; it is not evidence that Comparator ran in this integrity stage.

**Status:** `OBSERVED / TESTED ARTIFACT` for these exact bytes and checks.
**Not performed:** full theorem compilation, original verifier replay, Comparator
replay, or independent physical validation. The next test for reproduction is a
fresh pinned source build and the three documented Comparator endpoints. A hash
failure would reject source identity before those later tests begin.

## 8. Reproduction commands and resource boundary

These commands describe a future full replay, not an executed result from this
round. They use a new checkout and preserve upstream files and pins:

```sh
git clone https://github.com/yang-mills-group/YM.git YM-replay
cd YM-replay
git checkout --detach 55ba9fc36293b3f4d52c6b1f813169a0be76ee98
cd submissions/openai-20261028
python3 scripts/verify.py integrity
LEAN_NUM_THREADS=1 python3 scripts/verify.py all
```

The final command downloads pinned dependencies, builds the submitted targets,
freshly compiles the review modules, bootstraps the pinned tools, checks controls,
checks all three endpoints, and saves dated results. It reproduces the documented
development verification mode, including its isolation limitations. Thread
limiting reduces concurrency; it is not a guarantee of a particular memory
footprint or completion time.

For the source package's additional submitted-verifier workflow, after its
dependencies and targets are built, the original instructions specify:

```sh
cd submission
lake env lean -j1 -DmaxHeartbeats=0 -DmaxRecDepth=4096 VerifyJoint.lean
lake env lean -j1 -DmaxHeartbeats=0 verification/Usage.lean
lake env lean -j1 verification/CompactCheck.lean
```

| Requirement | Upstream documentation |
|---|---|
| Basic tools | Git, Python 3.10+, Elan/Lean, native build tools, initial dependency network access |
| Submission and review | Lean 4.32.0 |
| Comparator | Revision `d03acab154d269c06e60e4de7e4cc85deebff94b`, Lean 4.34.0 |
| Exporter | Revision `4e7915201d3f9f04470d9eae002fa695f7cdc589`, Lean 4.32.0 |
| Direct Mathlib pin | `81a5d257c8e410db227a6665ed08f64fea08e997` |
| Recorded source build | About 184 minutes on the documented Apple Silicon machine, using Mathlib cache and no existing project build |
| Recorded completed dependency/build tree | About 52 GiB; tools and temporary verification files require additional space |

These resource figures come from the assessment and [rerun instructions][rerun].
They were not measured by SUCC and are not predictions for another machine.
Changing Lean versions or running `lake update` would change the reproduction
inputs. A successful future replay must retain the generated receipt, exact
inputs, platform, cache reuse, and scope. A partial or stopped build is not a
successful proof reproduction.

## 9. Bounded transfer opportunity

The OPE adapter proves a useful exact pattern. If two phases use the same
coefficients and each remainder is bounded by \(r^\gamma\), then subtraction
preserves those coefficients and the difference remainder is bounded by
\(2r^\gamma\). The positive radius is chosen before the two phases and all
allowed configurations. [OPECheck.lean][opecheck] supplies the proof by linear
algebra and the triangle inequality.

This is a legitimate template for source-specific multiscale arithmetic
estimates. It does not imply phase equality: the lower-degree channel
differences remain. A contraction, uniqueness theorem, or separate cancellation
estimate must control them. The present audit supplies provenance and a precise
interface to study; it does not supply that missing arithmetic estimate or a
proof of normality, RH, or the Yang–Mills mass gap.

[committee]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/README.md
[assessment]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/docs/assessment-1.pdf
[checks]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/docs/checks.md
[evidence]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/evidence/README.md
[rerun]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/docs/rerun.md
[original]: https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/README.md
[challenge]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/ChallengeSpec.lean
[publictheory]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/PublicTheory.lean
[acceptance]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/checks/AcceptanceSpec.lean
[combined]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/checks/CombinedAcceptance.lean
[chain]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/docs/examples/OctoberChain.lean
[opespec]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/checks/OPESpec.lean
[opecheck]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/checks/OPECheck.lean
[statement]: https://www.kitp.ucsb.edu/sites/default/files/3rd-Statement-About-Quantum-YangMills-Theory_Nov-9.pdf
[announcement]: https://openai.com/index/building-scientific-understanding-with-academic-communities/
