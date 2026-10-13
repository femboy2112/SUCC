# A-cohort validation receipt

Frozen parent: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.

Actual executed checks in isolated worktree `swarm-A`:

| Command | Result |
|---|---|
| `python -m unittest discover -s tests -p test_swarm_categories.py -v` | 20 tests passed; final observed run 0.204 s |
| `python scripts/swarm_categories_probe.py --output research/2026-10-13/SWARM_ATLAS/A_CATEGORIES_RECEIPT.json` | 20 tests passed; saved exact witness/count receipt |
| `python scripts/verify_provenance.py` | 72 entries verified: 17 byte-identical archival originals and 55 mechanical namespace migrations |
| `python -m unittest discover -s tests -p 'test_*.py'` | **1622 tests passed**, observed runtime 84.454 s |
| `python scripts/observer_foundations_probe.py` | Exit 0, retained explicit unproved PA/RH/Weil boundaries |
| `python scripts/ordinal_succ_report_probe.py` | Exit 0, retained finite/omega distinction and unproved completed-Weil positivity |

No formal file was changed. No new Lean result or independent physical source authentication is claimed. Root separately reports a verified frozen-parent Lean baseline; this cohort did not rerun it.

One earlier targeted gate failed because its anticipated enumeration count was 4320 while the executed exhaustive enumeration returned 7200. All base-change mathematical assertions passed in that run. The count was corrected, and the final gates above passed. The receipt preserves this failure explicitly.

Prior-art/source checks: the author's current Riehl text was retrieved, including Definition 6.5.11 and pointwise Kan-extension statements; the CWI Rutten publication metadata and Stacks tag 02ZC were retrieved; the Abramsky–Brandenburger arXiv abstract was retrieved. A stronger search-service call returned 503 and direct Rutten/Lawvere PDF endpoints failed. No result is attributed to unread PDF content. Each dossier states its own complete derivation and exact novelty boundary.

Every A01–A08 dossier contains the ten required contract fields. No shared claim ledger, architecture, roadmap or README was modified. The new implementation uses no existing SUCC quotient/holonomy helper; independent word and global-section enumeration witnesses are preserved in the tests. The Yoneda regression examples intentionally use the existing naturality evaluator to audit that existing interface.
