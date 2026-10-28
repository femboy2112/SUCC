# Lonely Runner: exact certificates and effective growth

Base: Main XIII `b763ba8ef375fbac221e29e4396989a635a6ef36`, checked against the
remote on 2026-10-28. Branch:
`research/succ-lonely-runner-exact-certificates-2026-10-28`.
[Draft PR #351](https://github.com/femboy2112/SUCC/pull/351).
Main, archives, authentic BBP sources and sibling research are untouched.

## Mathematical results

* **General two-entry growth.** [GAMMA.md](GAMMA.md) proves that for every
  `n>=5`, arbitrary deletions `1<=r1<r2<=n-1`, and insertions `n<=w1<w2`,
  an all-time `1/n` cover forces `w1<B_n` and `w2<=2(n-1)w1<4n^3`.
  Here `B_5=56`, `B_6=60`, and `B_n=(n-2)^2(n-1)/(n-4)` for `n>=7`.
  This supplies an effective polynomial bound for the two-entry case of
  Zhang's Question 8.2, including deletions outside the upper half. The
  proof imports the audited cover form of his one-entry classification.
  **PAPER PROOF; no full Gamma Lean claim.** Stronger prior classification
  covers the upper-half restriction. Unrestricted academic priority remains
  unverified after a primary-source search.
* **Local-rule converse and finite decision.** [MANUSCRIPT.md](MANUSCRIPT.md)
  proves a finite iff criterion for affine-phase local replacement rules,
  an exact compression of unbounded added odd velocities, a finite rational
  feasibility reduction for every affected-speed cap and gain, and a sharp
  obstruction in the prescribed binary/3 ladder. Its first saving rule has
  cap 192; this is a family classification, not a global optimality theorem.
  These are paper proofs extending Poliakova's resonant-interval method.
* **Question 8.4.** [ALPHA.md](ALPHA.md) proves the supplied lower bound and
  the sharp minimum over deleted speeds. Equality in `2/(2n-3)` occurs
  exactly at `(n,r)=(5,2),(6,2)`. [ALPHA_PRIORITY.md](ALPHA_PRIORITY.md)
  identifies the result as a corollary of Liu's classical exact formula.
  The complete universal rational-time metric witness is kernel checked;
  the exact maximum formula and minimizer classification are paper proofs.

[The claim supplement](../../../docs/CLAIM_SUPPLEMENT_LONELY_RUNNER.md) separates
proved, formalized, certified, unverified and refuted claims.
[The literature audit](LITERATURE.md) preserves priority overlaps explicitly.
Same-model agent reviews are correlated checks, not external peer review.

## Independent exact certificates

[CENSUS.md](CENSUS.md) completes the two-entry classification for every
`5<=n<=20` over **all** inserted speeds. The only covers are the classical
`n=5, R={1,3}, W={6,8}` and `n=8, R={2,3}, W={11,13}`. Proved width
exclusions and 8,231 individual exact gap tests cover a finite domain of
79,648,374 cases supplied by Gamma. A separate Fraction implementation,
using the larger uniform speed bound, independently reproduces n=5..8.
Both surviving covers have separately verified certificates and exact maxima.
No complete-census Lean claim is made.

[Certificate soundness](CERTIFICATE_THEOREM.md) connects source-labelled rational
arcs to an all-real-time statement. The Fraction-based generator and independent
integer-pair checker share no implementation import. Published strict shifted
controls at n=5,13,95 are in [certificates](certificates/), with exact maxima
also independently evaluated at n=5 and n=13. They are reproductions, not new
shifted cases. The n=17 source data was not located. No new shifted case in
18 through 94 is claimed. Bounded failed searches and their limits are retained.

```sh
python scripts/check_lonely_runner_source.py --output /tmp/lonely-source
python scripts/check_lonely_runner_lean.py --output /tmp/lonely-kernel
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
```

The Lean runner requires the repository's pinned Lean 4.14/mathlib dependencies;
`--dependency-project` may name an existing matching dependency checkout.
It checks source and dependency hashes, exact proposition/axiom exports, and
paired false-theorem controls. It does not formalize the Python parser or the
new analytic theorems. Source receipts and raw logs distinguish local, kernel,
and hosted observations. See [VALIDATION.md](VALIDATION.md) and
[the next handoff](HANDOFF.md) for execution status and remaining obligations.
