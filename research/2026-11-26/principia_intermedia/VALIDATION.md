# Validation and reproducibility

## Executed

Standalone deterministic JavaScript/BigInt probe was executed in the available JavaScript tool runtime before publishing code. Source functions were serialized directly from the exact functions that executed and assembled with the CLI entry point; the stored source was fetched at commit fe0f5a366cba92f048fe457a60c8f247a411af2e and verified byte-for-byte against the generated source. Git blob 34eaec37b6385bc815cf889955566b6043376d0a.

- 32 exact original-four-pole vs direct/factored source moment comparisons and parity.
- 626 different odd-denominator cut subsets, 8,764 exact signed moment observations (two formula routes, both signs, k=0,...,6); k=0 exact denominator lower bound.
- Ten odd median grids up to denominator 59,049; real approximation bound and persistent 2-adic unit.
- Five exact finite atomic LP enumerations (126 feasible vertex records, possibly repeated degenerate vertices, not 126 independent observers); full rational Gaussian elimination and all sign-assignment patterns per free coordinate set. These are exact atomic quadratures, not exact continuous higher moments.
- 250 deterministic finite layered graph comparisons: forward/backward reachability vs exhaustive path enumeration.
- 25 rational Gram-volume telescope controls; 36 rational height/product-formula and reciprocal-family controls; five other positive/negative checks (uniform two-null, rational candidate, pairwise compatibility failure, independent-normalizer mutant, synthetic endgame budget).

Raw results: FINITE_RECEIPT.json. For atom LP, the counts listed per instance sum to 126; duplicates not silently counted as rank. Multiple algorithms share the same source definitions and runtime; these are independent formulas / enumerations, not blind independent research agents. The mathematical proofs are separate. No numerical fit used for universal claims.

## Not run / access boundary

The container's git ls-remote failed DNS resolution for github.com; there is no full local repo checkout. GitHub connector was used to pin, create and update a non-main branch and to fetch sources. Full SUCC provenance, inherited root unittest suite, observer foundations probe, ordinal probe, remote hosted CI, external peer review, Lean compilation and independent kernel replay were NOT RUN in this round. The external compact Lean verification is separately cited in RH_ORACLE.md, not a local result. Standalone script's Node CLI entry point was generated from the executed code; Node itself was not separately launched in this round. No proof-assistant certification of I1–O4 is claimed. Review/draft only; do not merge until maintainer and required root gates pass.
