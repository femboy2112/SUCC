# Upstream scope for the coupled Wilson continuation

**Date:** 2026-11-13. **Status:** primary-source audit; no new continuum
Yang–Mills theorem. This is a fresh verification of the external scope relevant
to this continuation. The larger audit, historical build records, and source
manifest remain in [UPSTREAM_AUDIT.md](../UPSTREAM_AUDIT.md); they are not
replaced or promoted by this note.

## Fresh source checks

Both `main` branch heads were requested again through the GitHub API during
this continuation. They agree with the earlier dossier:

| Primary repository | Verified commit |
|---|---|
| [`yang-mills-group/YM`](https://github.com/yang-mills-group/YM/tree/55ba9fc36293b3f4d52c6b1f813169a0be76ee98) | `55ba9fc36293b3f4d52c6b1f813169a0be76ee98` |
| [`yang-mills-group/OpenAI-YM-20261028`](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464) | `3456e5e75cf8d4cd558955a5c7638fba2d68f464` |

The local assessment checkout also has the first commit as its HEAD. The
[November 10 assessment][assessment], pp. 1–20, was freshly read from its
extracted PDF text. The actual [construction][construction], [solution][solution],
[acceptance specification][spec], and [assembly proof][proof] were read, as
were the pinned [check-scope][checks], [reproduction][rerun], and
[tool-pin][pins] files. This is a bounded source inspection, not a semantic
audit of every dependency in the submitted proof library.

The committee's judgment is that the submission constructs a four-dimensional
Wightman quantum field theory from Wilson lattice gauge theory for simple
compact gauge groups. Its report does **not** claim a positive mass gap or
uniqueness of the infinite-volume limit. The complete existence-and-mass-gap
problem therefore is not solved by the stated result. The assessment also
discloses model assistance and incomplete human understanding of the proof;
neither those disclosures nor this audit replace the formal and semantic checks.

## The source-binding mechanism that transfers

The strongest inspected acceptance endpoint has the schematic quantifier order

\[
\forall G\text{ allowed},\ \forall b>0,\quad
\exists C:\ \operatorname{penalty}(C)=b\ \land\
\forall p\text{ an extraction order},\quad
\exists q,S,F:\ \operatorname{Accepted}(C,p\operatorname{.refine}q,S,F).
\]

Here `C` is one Wilson family, `S` is one correlation table, and `F` is its
native final-construction witness. The proof obtains `C` once from
`YangMills.constructed`; all lattice, phase, scalar OS, field-content, Ward,
leading-trace, and source-conclusion clauses then concern the same `F`.
The family is fixed before the requested extraction order. The assessment
explains that the original public target exposed fewer lattice-construction
connections; the stronger combined endpoint retains `C.Makes` and `Spec.Final`.

This is an actual mathematical interface for SUCC: transport a **specified
source and its observables together**, and require all compared representations
to share witnesses. It does not turn observational agreement into an analytic
limit theorem. In particular, a finite character transform or a gauge-orbit
reconstruction is not an instance of the continuum construction until the
Wilson law, renormalized insertions, calibration, and limit estimates have
been identified.

The separate OPE review endpoint has its own existential hierarchy and
Comparator record. That endpoint alone does not identify its chosen hierarchy
with the combined endpoint's witness. The source construction already retains
OPE data; the `from_source` adapter can be applied when those data belong to an
already chosen hierarchy. This distinction prevents an accidental splice of
different existence witnesses.

## Quantifier and domain boundaries

| Established scope reported upstream | Additional statement not established |
|---|---|
| Full fixed-volume UV convergence along the construction's chosen spacing sequence | Universality over arbitrary spacing sequences |
| One extracted infinite-volume subsequence works for all finite correlation lists and allowed tests | Convergence without extraction or uniqueness across subsequences |
| Each phase reconstructs with its own unique vacuum | A unique mixed vacuum or agreement of every phase |
| Independent OS comparison for the selected centered-trace scalar hierarchy on diagonal-flat Schwartz tests | A separate all-field comparison or unrestricted Euclidean contact-term positivity |
| Nonzero leading stress-trace asymptotic and a specified free-field exclusion | Positive mass gap, or exclusion of every generalized Gaussian description |
| OPE coefficients and controlled remainders at every fixed field-degree truncation | All-orders perturbative matching or phase equality from common coefficients |
| Normalized finite Wilson laws and a nonzero smeared continuum probe | Wilson-loop area law or identification of that probe with a spectral gap |

The independent lattice-law adapter includes the convention conversion
\(\beta_{\mathrm{submission}}=m\beta_{\mathrm{lgt}}\), where \(m\) is the
matrix representation dimension. A new finite SU(2) implementation must keep
its own explicit convention rather than silently borrowing a coefficient from
a differently normalized Wilson action.

## Reproduction and claim boundary

The fixed submission/review environment is Lean 4.32.0. The pinned Comparator
is `d03acab154d269c06e60e4de7e4cc85deebff94b` on Lean 4.34.0; the exporter is
`4e7915201d3f9f04470d9eae002fa695f7cdc589` on Lean 4.32.0. The published runner
uses the development launcher and records `external_kernel: false`. Its
documented mode does not reproduce Linux Landrun process isolation.

From `submissions/openai-20261028/`, `python3 scripts/verify.py integrity`
checks manifests and four normalized OS declaration correspondences.
`python3 scripts/verify.py all` additionally builds the source, review modules,
tools, controls, and three Comparator endpoints. A source hash check is not a
kernel replay; a completed build is not a new analytic derivation; a checked
formal statement still requires semantic identification with its intended
mathematical problem. Fresh execution receipts from this continuation must
state which stages actually ran. This source-reading task itself ran none of
those build or proof stages.

**Verdict:** the external result supplies a concrete common-witness template
and reusable formal interfaces. The finite coupled-Wilson work must earn its
own finite claims. A continuum import remains conditional on the specified
source-preserving adapter and multiscale estimates. The next falsifying probe
is a mismatch in the actual normalized Wilson law, ordered observable, or
retained witness—not merely a mismatch in descriptive terminology.

[assessment]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/docs/assessment-1.pdf
[construction]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/Construction.lean
[solution]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/Solution.lean
[spec]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/checks/AcceptanceSpec.lean
[proof]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/checks/CombinedAcceptance.lean
[checks]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/docs/checks.md
[rerun]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/docs/rerun.md
[pins]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/verification/tool-pins.json
