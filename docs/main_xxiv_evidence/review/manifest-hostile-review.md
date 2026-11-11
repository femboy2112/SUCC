# Independent hostile review: Main XXIV manifest replay

Reviewer: Front A agent, same-model independent read-only pass. Target files: `scripts/main_xxiv_manifest.py` and `tests/test_main_xxiv_manifest.py`, shared integration checkout. No repository edits made by reviewer.

## Confirmed falsifiers

1. **Regular file to symlink with identical blob falsely passed.** Initial tree()/identity() omitted Git mode and kind. Tiny Git fixture used `git update-index --cacheinfo 120000,<existing-blob>,research/result.md` and committed; checker returned `[]` although canonical path was now a symlink. The owner repaired identity to include mode/kind and added a regression. Reviewer executed the resulting six-test suite: all pass in 1.157s.

2. **Row source owner could disagree with frozen origin and erase a contribution.** With an ordinary generated fixture manifest, retain origins and expected_contribution_ids but replace its sole contribution row's head_commit/head_tree with baseline identities, contribution_parent/contribution_commit with baseline, contribution_tree with baseline tree, contribution_commits=[], files=[]. Delete research/result.md in a newer integration commit. Checker returned `[]`. It checked row-local Git coherence but never bound row head/parent/branch to origins[row.originating_pr]. Require those equalities and require the contribution checkpoint to be an ancestor of its origin head. Recompute checkpoint IDs/parents/heads/commit lists from frozen origins and Git to catch a row replaced by an empty or wrong checkpoint.

3. **Protected-set omission is not detected by initial checker.** Clearing protected=[] removes every protected-byte comparison while baseline_main still identifies the immutable expected protected set. Reconstruct and compare expected protected paths from baseline_main before checking their identities. This is the same internal completeness boundary as row coverage.

Findings 2 and 3 concern consistency of a supplied manifest against its own declared frozen anchors, not cryptographic resistance to rewriting every anchor. The generator emits normal complete data. CLI replay should either enforce this consistency or explicitly narrow its contract to trusted manifest structure. The integration mission requires lossless row and protected-source coverage, so enforcement is preferable.

## Sound inspected behavior

- Final checks use resolved commit objects and preserve newer documentary commits without self-hash circularity.
- Source blob SHA-256 is independently derived from Git; final destination bytes are pinned.
- Unaccounted paths and new nonreviewed changes to recorded final bytes are rejected.
- Explicit archive redirects require byte identity with origin head; repaired/superseded paths require declared reason/authority.
- Independent descendants with competing content do not silently choose a newest unrelated version: generator requires explicit decisions when the final differs from its ancestry-derived expected source.
- A manifest remains a provenance/collision receipt. It supplies no mathematical theorem, native-suite result, hosted-CI result or external review.
