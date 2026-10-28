# Alpha primary-source and priority audit

Access date: 2026-10-28. No novelty claim. Read-only primary-source retrieval
preceded implementation; no external author was contacted and no paper was
redistributed into the repository.

## Zhang, fixed version

Yuhan Zhang, *Tight instances of the Lonely Runner Conjecture: one-entry
modifications and the growth of speeds*,
[arXiv:2608.13599v3](https://arxiv.org/html/2608.13599v3), 18 October 2026.
The complete HTML text, all sections and proofs, was read. The fetched HTML
SHA-256 was
`1653d5bb478dfd1657b331880f5f897b259d875d885a1ae3bb804db20cb82fc8`.
Dynamic HTML chrome can change this transport hash without changing the paper;
the version identifier and theorem locations are the semantic receipt.

Theorem 2.9 gives the inverse-modulus witness `2/D` for any coprime
`D>=n+r`; Corollary 2.10 supplies a sufficient interval-length condition.
Lemma 2.4's proof already uses the centre `1/r` when `2r>n-1`.
Section 2.3 explicitly attributes the exact middle-range deletion values
to Liu Theorem 18. Question 8.4 asks strictness against `1/(n-1)` for
`n>=5`, `r<=n-2`. Combining the centre case with the elementary middle
congruence witness answers it. Thus the proposed result is a clarification
and corollary of existing ingredients, not a new general conjecture proof.
The sharp minimum in ALPHA-03 is also a corollary of those exact values.

## Liu, original theorem and glyph check

Daphne Der-Fen Liu, *From rainbow to the lonely runner: a survey on coloring
parameters of distance graphs*, Taiwanese Journal of Mathematics 12 (2008),
851–871, [DOI 10.11650/twjm/1500404981](https://doi.org/10.11650/twjm/1500404981).
The [author-hosted PDF](https://www.calstatela.edu/sites/default/files/surveyrevisionnew.pdf)
was downloaded and the full Theorem 18 proof read, together with definitions,
Proposition 2, Theorem 17, and its surrounding context. Its SHA-256 was
`45f7a32668fe95a2ce31800bee7e2fbeb09322a09d98f15e14582ee8d8375b6b`.
This author version has 25 PDF pages; Theorem 18 is on printed page 16
(zero-based PDF page 15), continuing on page 17.

The hypothesis is **`m >= (s+1)k`**, not strict inequality: local PDF text
extraction preserves the `⩾` glyph that the web parser renders incorrectly.
For `D=[m]\{k,2k,...,sk}`, with `t` the least positive integer satisfying
`gcd(m+t,k)=1`, the formula is `(s+1)/(m+sk+t)`, except for the specified
even-`s` exceptional branch. Setting `s=1,m=n-1,k=r` removes that branch
and gives exactly `2/D_r`. Theorem 17 gives `1/k` when `m<(s+1)k`,
attributing this to X. Zhu, Discrete Mathematics 265 (2003), 337–350.
Our large-range proof needs no external result beyond pigeonhole.

## Falsified ancillary remark; preserved priority boundary

The author version's paragraph after Theorem 18 asserts a stronger
cardinality bound with only `{1,3,4}` excepted. This fails also for
`{1,3,4,5}`: its exact value is `2/9`, less than `1/4`. The strict
version also fails for many equality cases, for example the deletion
`r=n-2` when `n>=7`. This does not refute Theorem 18 or erase its priority;
the mistake belongs to the following prose. The dossier proves the needed
one-deletion formula separately and includes the counterexample as a test.
Whether the final published PDF changes this sentence remains a source
comparison task, not a presumed correction. The DOI resolved to the primary
Project Euclid landing page, but its PDF endpoint returned an HTML security
page, not a PDF. We therefore confine this textual correction to the fetched
author version; the unavailable journal body is not claimed as read.

## Reproducibility and epistemic limits

The supplied proof, primary sources, modular arithmetic proof, exact envelope
enumeration, and Lean kernel are different checking mechanisms. They are not
all independent source families: Zhang cites Liu; the closed-form executable
implements that same formula. Same-model agent reviews are explicitly
correlated. Finite scans do not establish universal sharpness; the paper
derivation supplies it. Literature search found the decisive exact formula,
so academic novelty of ALPHA-01–04 is neither claimed nor required for their
use as a reliable baseline.
