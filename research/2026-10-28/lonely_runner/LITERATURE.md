# Priority audit and external proof boundary

Audit date: 2026-10-28. This is a bounded primary-source comparison, not an
exhaustive priority certification. Mathematical validity, prior publication,
external platform acceptance, and our own Lean replay are separate claims.
No external proof below was submitted to or replayed by our local Lean kernel.

## Beta: what is already present, and what this campaign adds

[Poliakova, arXiv:2609.23952v1](https://arxiv.org/html/2609.23952v1), submitted
20 September 2026, is the direct source. Definitions 3 and 5 already specify
affine radius-dependent phases and universal locality. Theorem 7 substitutes
`qt=k+delta*z` and proves its particular rule by covering `[-1,1]` with
resonant rescue intervals. Its Section 3 example has gain one and largest
affected speed 192. Table 1 contains further rules, including another
192-speed example and a better asymptotic coefficient, `1/224`.

Accordingly, the tangent substitution, interval-cover mechanism, published
rule, and original threshold are **prior work**. LRU-1's sufficiency packages
that existing argument. The additional direction proved here is necessity,
using genuinely responsible times as the radius tends to zero, together with
the exhaustive residue condition `gcd(k,q/2)=1`. LRU-5 reverses the argument
within its explicitly fixed phases and binary/3 support family. That family
classification is not a global optimality assertion; Table 1 already shows
that different phase patterns exist. The paper does not state the converse,
the family classification, or an added-speed compression/decision theorem.

**Assessment of LRU-3/4.** Once necessity is proved, finite phase menus and
rational linear feasibility use elementary methods. The decisive further
step is the exact odd-speed compression: reduce each residue class modulo
`lcm(Q)` to its smallest distinct positive representatives, and rescale each
beta by the speed ratio. This preserves resonance and expands every credited
interval. It removes an actual unbounded quantifier from the existence
problem, rather than merely selecting an experimental speed cap. The proof
survived a separate read-only algebraic review, including distinctness,
arbitrary real phases, unused rescuers, and the case of zero additions.

These are plausible scoped additions to the inspected source, but their
academic priority remains **UNVERIFIED**. A direct extension of a recent
proof can be mathematically useful without meeting a journal's novelty or
significance threshold. Recommended description: an exact converse,
finite decision reduction, and classification for a prescribed family.
Do not claim a new shifted counterexample or a universal minimum of 192.

## Exact cover checking and breakpoint evaluation are established methods

[Blanco, Criado and Santos, arXiv:2603.24784v4](https://arxiv.org/html/2603.24784v4),
24 October 2026, explicitly points readers to an exact rational certificate
checker. Their pinned
[verify_solution.py](https://github.com/criado/shifted_lonely_runner_conjecture_counterexample/blob/fd0dbc5f2c7450ae8d7b784e855019507d5a8efd/scripts/verify_solution.py)
advances through intervals covered by individual runners. Thus neither
finite interval certification nor all-time exact verification is new here.
Our separately implemented source-labelled JSON format, hostile mutations,
integer-only checker, and generic Lean semantics are verification engineering.

[Zhang's associated repository](https://github.com/Qinrayn/lonely-runner-tight-II/tree/2d7220cac00ba23478697ae1c565a8d3845d6139),
commit dated 16 October 2026, already evaluates unshifted loneliness at
finitely many rational breakpoints, with independent interval-based checks.
The current shifted opposite-slope formula is an elementary specialization
of piecewise-linear maximization; no algorithmic-novelty claim is warranted.
The implementation was written independently before inspecting these
algorithms. Their code has not been copied into the repository.

## Gamma: a stronger accepted proof on the upper-half subdomain

The [Conjectures.io target page](https://conjectures.io/problems/math15catalog-source04)
and [recorded review](https://conjectures.io/results/4c651db1-3b53-48da-ac31-0b0020a8d87c)
identify a proof submitted by **JenW1N**. The site reports verification on
7 October, approval on 8 October, and certification on 9 October 2026.
It reports that tight two-entry modifications with both removals in the
upper half and inserted speeds at least `n` satisfy the individual
multiplicative gcd criteria, under either matching. This is stronger than
the present direct cubic bound on the same tight configurations.

The [accepted Lean source](https://conjectures.io/results/4c651db1-3b53-48da-ac31-0b0020a8d87c/solution/download)
was downloaded and selected interfaces inspected. The terminal proof
constructs `remaining_window_assertion` and supplies it to
`Classification.target_of_remaining_window`. Its common-insertion and
exclusive-matching helpers assume `ML(modified)<=1/n`, so merely weakening
our hypothesis from tightness to cover does not avoid the overlap.
`replacementCondition_iff` identifies the multiplicative gcd window.

This is primary evidence of a stronger previously accepted result. We have
**not** independently replayed the 6,500-line source or audited every proof
step. The correct response is to preserve the independently derived short
bound as an alternative argument and remove any first-solution claim for
that frontier. The source record is sufficient to defeat an unqualified
novelty claim even though local verification remains unperformed.

Exact source receipts:

| Item | Receipt |
|---|---|
| Download bytes | 309195 |
| Download SHA256 | `a1aad65e807a968e03cf186b80a17a399b234ea13d725b42d188cc45814957bd` |
| Submission/result id | `4c651db1-3b53-48da-ac31-0b0020a8d87c` |
| Reported source commit | `4b69a7dca3e731dd1f28cb523b9ebd2ea32527f4` |
| Reported target type hash | `fc9ddfec4d0d1725aa3a0a9d06329d3accbe40fc8bfcfa6480ddf9d8ba13ae22` |
| Reported report digest | `667a650f33b5b3c105f60e4f240a9386fced87aed0b4676fd5c135b7e9eb927b` |

The hash was computed from the downloaded bytes, twice with matching results.
The public download required an ordinary browser User-Agent; unadorned
Python requests returned HTTP 403. No authentication was used. The source
has not been vendored, modified, compiled, or treated as a local kernel receipt.
No proof text is quoted here.

The task's
[activation record](https://github.com/conjectures-io/conjectures-tasks/blob/bd5b6f0ad05b0c1cb8b16de282d69cb25433292e/staged/research-targets/ACTIVATION.md)
independently describes the intended both-large-removals converse. The
`Challenge.lean` wrapper by itself only names `Math15.LonelyRunner.Target04`;
its descriptive title is not a substitute for checking that interface.
An upstream conjecture declaration depending on `sorryAx` is not, by itself,
evidence that the accepted replacement proof depends on that declaration.
The platform reports checking the submitted proof's permitted dependencies.

## Gamma's unrestricted two-deletion extension

The subsequent theorem removes the upper-half hypothesis entirely: for
`n>=5`, arbitrary `1<=r1<r2<=n-1`, and `n<=w1<w2`, coverage at `1/n` forces

```
w1 < B_n, where B_5=56, B_6=60, B_n=(n-2)^2*(n-1)/(n-4) for n>=7,
w2 <= 2*(n-1)*w1 < 4*n^3.
```

The accepted source04 classification does not, by its inspected interface,
include this unrestricted removal domain. In particular, its classification
cannot simply be cited as a proof of the new universal cubic bound.
[Zhang v3, Question 8.2](https://arxiv.org/html/2608.13599v3#S8)
asks for a polynomial bound for modifications of size at least two; this
extension supplies the two-entry case, conditional only on the explicitly
cited established results used in its proof. It does not address three or
more replacements, prove an `O(n log n)` bound, or classify the tight sets.

A read-only audit checked the potentially dangerous transition from
classification of equality to classification of coverage. Zhang's Lemma 2.2
already assumes `LR<=1/n`. The contradictions in Proposition 3.4 and the
necessity argument of Proposition 3.5 use only that coverage condition. The
upper-half case first forces divisibility and then invokes Goddyn--Wong's
unconditional lower bound; `r=1` is multiplicative from the outset. Thus the
cover version used here does not silently assume the Lonely Runner Conjecture.
The two sporadic cases cannot supply a cover after two deletions and one
insertion; the remaining common-multiple case is excluded by the direct safe
interval argument. Exact source endpoint spacing and periodic occupancy then
provide the displayed bounds. This is a mathematical dependency audit, not a
Lean replay of the classification.

The first endpoint-only derivation gave the weaker constant `16*n^3`.
Using the exact classical deletion margin and a Lipschitz safe interval
improves it to the displayed `4*n^3`; both derivations are preserved in
GAMMA.md. Neither version uses the earlier upper-half two-entry result as
a dependency.

The [accepted source05 review](https://conjectures.io/results/31ab8532-c253-4e14-95c7-be44878a02fa)
was also inspected. Its statement concerns four-element primitive speed sets
with restricted pairwise gcd and their loneliness spectrum. It is not an
arbitrary-number-of-runners growth theorem. Its page reports verification on
8 October, approval on 12 October, and certification on 14 October 2026.
No local replay or full source audit of source05 was performed.

[Jain and Kravitz, *Relative Lonely Runner spectra*](https://arxiv.org/html/2411.12684v2)
provides another relevant finite-computation precedent, for relative spectra
inside two-dimensional subtori. That result does not state this uniform
polynomial bound for two-entry modifications. Their general framework is
relevant background, not a priority-disjointness proof.

The primary-source search located no prior unrestricted two-entry cubic
bound. Zhang's repository still has the pinned 16 October commit as its head.
These facts support a precise scoped comparison; they do not certify academic
novelty. Expert checking of the universal bound and its relation to known
quantitative spectrum results remains the next priority test.

## Scope of the supplementary corpus search

The live [Conjectures.io catalog](https://conjectures.io/problems?field=3)
was fetched and its embedded records decoded: 290 unique task keys were
present. Title/summary checks for runner, loneliness, shifted, Poliakova,
resonance, compression, and local uniform rules found the two-entry
classification and four-speed spectrum tasks, but no Beta local-rule,
added-speed-compression, or shifted-18-through-94 target. The separately
linked six-speed denominator result is a different ordinary-loneliness
problem. This is a catalog screen, not a search through every lemma in
every accepted solution or through unpublished work.

The inspected older precedent is
[Goddyn and Wong, *Tight Instances of the Lonely Runner* (2006)](https://zenodo.org/records/8275490),
especially Theorem 3.1 and Lemma 3.2. Those give sufficient arithmetic
conditions for simultaneous unshifted accelerations and cover local gaps
using residue information; they do not state the affine shifted-rule
decision theorem. This supplies clear methodological ancestry.

Additional bounded searches used local-uniform, resonance, tangent/residue
covering, velocity-compression, binary-ladder, and Poliakova/192 variants.
No exact matching primary statement was located for LRU-1's converse or
LRU-4. Absence from these searches is **not** evidence sufficient to claim
academic novelty. The next meaningful priority check is expert comparison
of LRU-1/4 with the actual source author's methods and any unpublished
rule-generation work; no messages to authors have been sent.
