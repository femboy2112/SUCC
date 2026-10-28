# Lonely Runner research campaign

Base: Main XIII `b763ba8ef375fbac221e29e4396989a635a6ef36`, rechecked against the remote on 2026-10-28. Dedicated research branch; main, original sources, archives, and sibling research are untouched.

## Validated first milestone

[Alpha dossier](ALPHA.md) proves the supplied deleted-speed bound and the sharp minimum over the removed speed, with all equality cases. [Priority audit](ALPHA_PRIORITY.md) identifies these as corollaries of Liu's classical exact formula; academic novelty is not claimed. The strict inequality asked in Zhang v3 Question 8.4 follows from the middle-range formula and the elementary upper-half witness.

The stronger minimum is 2/7 at n=5, 2/9 at n=6, and 1/(n-2) for every n>=7. Equality in the user's weaker 2/(2n-3) bound occurs exactly at (5,2) and (6,2). All eleven focused tests passed, including a separate exact lower-envelope implementation. These universal results are paper proofs; Lean work is in progress.

## Baseline receipt

Before implementation, provenance, 33 relevant native tests, observer foundations and the ordinal probe passed. `scripts/build_math_memory.py --check` failed on the untouched base with STALE/MISSING mathematics catalog. Raw outputs and hashes are in [receipts/baseline](receipts/baseline). The stale catalog is inherited, not silently counted as passing. Full native and hosted validation have not yet been completed for this campaign.

## Continuing frontier

The active work is independent exact circle-cover certificates, reproduction of published shifted examples, a finite necessary-and-sufficient local-rule criterion, and bounded searches below Poliakova's n>=95 threshold. No new shifted case is claimed at this milestone. Completed results will be committed while further research continues.

Literature correctness, mathematical correctness, exact finite certification, kernel authority, and academic novelty are separate gates. Agent reviews use the same model and are not independent human or external review.
