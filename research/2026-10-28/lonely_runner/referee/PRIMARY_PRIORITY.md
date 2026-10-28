# Primary-source referee and priority record

Date: 2026-10-28. Base: `27af9600ddd8acacea7a1822921083821c5dbf6e`.
This record separates theorem inspection, proof reconstruction, publication
priority, platform acceptance, and local kernel replay. No author was contacted.
No downloaded third-party proof or paper is redistributed here.

## Zhang: fixed source and the coverage question

[Yuhan Zhang, arXiv:2608.13599v3](https://arxiv.org/html/2608.13599v3),
18 October 2026, remains the latest version reported by the
[arXiv record](https://arxiv.org/abs/2608.13599) at this audit.
Fresh HTML: 716591 bytes, SHA256
`1653d5bb478dfd1657b331880f5f897b259d875d885a1ae3bb804db20cb82fc8`.

The relevant complete arguments were re-read: Lemmas 2.1--2.4,
Proposition 2.5 and its component proof, Corollaries 2.7--2.8,
Theorem 2.9, Lemmas 3.1--3.3, Propositions 3.4--3.5, and the completion of
Theorem 1.2. Lemma 2.2 explicitly admits coverage at radius 1/n. Every
contradiction in the middle-window and speed-two necessity arguments uses
that coverage property, not equality. Their geometric content has priority.
Sections 5--6 and Questions 8.1--8.2 were compared with the new growth scope.

The referee proof writes the coverage assumption from the outset, proves
only the safe-window inclusions actually needed, and replaces the numerical
Jacobsthal input by an explicit elementary unit construction. It thereby
removes the potentially misleading dependence on an equality-only interface.
The quadratic theorem is not a restatement of the paper's finite speed-capped
census. A search finding no matching explicit theorem does not establish
academic novelty.

## Goddyn--Wong: an exact priority correction

[Luis Goddyn and Erick B. Wong, *Tight Instances of the Lonely Runner*,
Integers 6 (2006), A38](https://math.colgate.edu/~integers/g38/g38.pdf).
Fresh journal PDF: 272456 bytes, SHA256
`dc9b2a9a8fd9849ee5f05664b83899df83b8ab23a622300625e50465cf463197`.
The entire 14-page paper was read, including Theorem 2.3's necessity proof,
Theorem 3.1's sufficiency proof, and the missing-converse discussion.

**Lemma 2.1 already states** the bound `j(r)<=floor(r/2)+1` used in the
referee proof. Its proof uses Bertrand's postulate. The explicit four-unit
construction is an alternative proof of this established bound; the bound
must not be presented as new. The r=1 safe interval also appears in their
Theorem 2.3 proof. Their multiplicative classification includes an
unconditional Lonely Runner lower bound, so the original Gamma dependency
was legitimate; the new proof simply avoids needing it. Theorem 3.1 supplies
known simultaneous-acceleration controls, not a classification of arbitrary
two-entry modifications. No novelty is claimed for those constructions.

Zenodo and the author-hosted URL returned HTTP 403 on the fresh direct fetch;
the journal-hosted PDF succeeded and matches the previously recorded bytes.

## Liu: exact values are prior work, but not a new theorem's premise

[Daphne Der-Fen Liu, *From rainbow to the lonely runner: a survey on coloring
parameters of distance graphs*, Taiwanese J. Math. 12 (2008), 851--871](https://doi.org/10.11650/twjm/1500404981).
Fresh [author PDF](https://www.calstatela.edu/sites/default/files/surveyrevisionnew.pdf):
196489 bytes, SHA256
`45f7a32668fe95a2ce31800bee7e2fbeb09322a09d98f15e14582ee8d8375b6b`.
Theorems 17--18 and the complete proof of Theorem 18 were re-read. Local
PDF extraction confirms the hypothesis is non-strict `m>=(s+1)k`.
The s=1 specialization is the exact one-deletion formula already credited
in ALPHA.md. The new quadratic proof uses only its directly proved modular
lower witness, not the exact upper bound or the erroneous ancillary paragraph.

## Earlier accepted upper-half proof: genuine overlap, limited authority

[Conjectures.io source04 result](https://conjectures.io/results/4c651db1-3b53-48da-ac31-0b0020a8d87c)
reports JenW1N's proof as verified 7 October, approved 8 October, and certified
9 October 2026. Its [download](https://conjectures.io/results/4c651db1-3b53-48da-ac31-0b0020a8d87c/solution/download)
was fetched again: 309195 bytes, 6840 lines, SHA256
`a1aad65e807a968e03cf186b80a17a399b234ea13d725b42d188cc45814957bd`.

Selected proof interfaces were reinspected, especially lines 3823--3842,
3889--3906, and 6832--6840. The common and exclusive insertion helpers
require both deletions to be upper-half and assume coverage, not merely
equality. The terminal theorem assembles the remaining-window proof into
the fixed source04 target. This is substantial prior overlap: combined
with Zhang's multiplicative growth result, it gives a stronger growth rate
on that subdomain. It was not fully audited or locally compiled in this
run. The direct quadratic proof neither imports it nor escapes its priority
by changing equality to coverage. The contribution is a shorter independent
proof route and an unrestricted removal domain, subject to expert review.

## Geometric finite-checking precedents

[Beck--Everett, *Lonely Runner Relations*, arXiv:2609.06259v2](https://arxiv.org/html/2609.06259v2),
23 September 2026, gives bounded-coefficient integer relations for tight
instances and covers through Fourier and lattice-width arguments. A relation
can involve only retained baseline speeds, so that necessary condition alone
does not bound inserted speeds. The preceding campaign read the complete
geometric proof; its version and byte hashes remain in the committed
literature-supplement receipt. This is important geometric context, not a
printed two-entry polynomial bound.

[Malikiosis--Santos--Schymura, arXiv:2411.06903v2](https://arxiv.org/html/2411.06903v2),
21 June 2025, subsequently Forum Math. Sigma 13, e164,
[DOI 10.1017/fms.2025.10107](https://doi.org/10.1017/fms.2025.10107),
proves general conditional finite-checking reductions. Its projection may
combine or delete generators and lowers dimension. The printed ordinary
statement assumes the preceding-dimensional conjecture; its shifted analogue
has additional hypotheses. Neither inspected statement is the present
unconditional bound for every vector in the fixed two-entry family.
Finite checking itself is established methodology.

## Fast-runner perturbation is established

[Kravitz, arXiv:1912.06034v1](https://arxiv.org/pdf/1912.06034v1),
12 December 2019, pp. 13--15, is direct methodological prior.
Proposition 8.1 preserves loneliness at least `L-epsilon` after adding
a speed at least `((L-epsilon)/epsilon)*v`, where `v` is the previous
maximum speed and `0<epsilon<L`. Lemma 8.4 gives cutoff `v*(2v-1)`
at threshold `1/m`, assuming the prefix exceeds `1/m` and there are
`m` final moving speeds. This is quadratic in `v`; our Lemma 7 uses
source endpoint labels to obtain `2(n-1)*w1`. The shared mechanism
is known. The [bounded search receipt](receipts/priority-final.json)
records four primary-source comparisons; it supplies no novelty certification.

## Bounded search and final scope

Fresh searches included the exact paper title and queries for two-entry
Lonely Runner quadratic/polynomial bounds and one insertion after two
deletions. The actual source04 result, rather than a search snippet, was
checked again. No matching unrestricted quadratic theorem was located in
these inspected primary sources. The search is not exhaustive, does not
cover unpublished work, and cannot certify novelty or significance.

The precise defensible result is: **a self-contained elementary paper proof
that every zero-shift two-entry cover with n>=5 has w2<28n^2**, together with
exact source tests and separately scoped formal evidence. The proof relies
on Zhang's known window mechanism, Goddyn--Wong's known unit-gap bound
(reproved), basic CRT, and exact interval geometry. Priority of this scoped
consequence remains **UNVERIFIED**. No breakthrough, general Lonely Runner
proof, RH result, or shifted counterexample is claimed.

The new manuscript must credit those dependencies even though their external
theorem interfaces are no longer assumptions of its self-contained proof.
