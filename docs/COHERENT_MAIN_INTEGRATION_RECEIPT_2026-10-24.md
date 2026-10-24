# Coherent-main integration receipt (2026-10-24)

**Successor to** `docs/ACADEMIC_MAIN_IX_INTEGRATION_REPORT.md`, whose pre-push "STAGED,
NOT MERGED" status and `5bafd77` / `7374 tests` figures describe the earlier 17-PR tree and
are now historical. This receipt records the actual current heads and checks for the
coherent-main consolidation. Historical runs are not rewritten.

## Scope and authorization

Consolidation of the reviewed SUCC π-source / circle / prime-clock frontier into `main`,
per `handoffs/CLAUDE_COHERENT_MAIN_AND_CLEANUP_2026-10-24.md`. Merging the reviewed,
validated candidate and deleting fully-integrated inactive branches are authorized. No
release, tag, license change, archive deletion, or force-push.

## Heads

- **Starting `main`:** `b116841f12b41aaf7600da39bbb40577f25b6295` (Academic Main VIII).
- **Reviewed #250 base (Academic Main IX):** `f986507851e34636f60bee657dcdf0771a934380`
  — already contains current `main`; #245/#246 already folded in (not re-merged).
- **Integration branch:** `integrate/coherent-main-2026-10-24`, built from the #250 head
  with ancestry-preserving `--no-ff` merges of the audited leaf set.

## Inclusion manifest (leaf set merged, with observed heads)

| PR | head | role |
|---|---|---|
| #265 | `ea5f92bbc52468e55b597e52455f24bceedb47b3` | π source collision entropy (SCE-01..10); descendant of #264 (Poisson minimum geometry) — used in place of bare #264 |
| #263 | `d7b5a5b91d142717ce7898417eed7a5dc603e019` | Principia ancestral bridge (main-based) |
| #255 | `68def05ad1dd92b78f8d6bd646ff28ab1ed85c59` | CYCLOFRAME cyclotomic origin gauges |
| #259 | `a777aa99f541df2a0e2a0b8d57fef3f0940e465c` | cyclotomic selected source |
| #262 | `34f8e040a6f86a9e583bad428f3d4e20940e1ac8` | Minimal Genesis first 34th-moment carry |
| #260 | `654e9c9984ced49cee454d99cff20415072d1ffc` | BBP minimal path gauge/missing-prime no-go; **carries final #256 p² Witt head `0683f8f166b9106ab8405a2d6538415b5ac84ba3`** |
| #261 | `4b52cb87a19c2f599e5386fc12a9758bab12cba8` | BBP minimal path Galois selection |

Transitively this pulls in the full #250→#265 DAG (#251 cyc03, #252 source-fidelity repair,
#253 source genesis, #254 green-rank tail, #256 p² Witt, #257 origin gauge, #258 prime-window
projection, #264 Poisson minimum). All 18 nodes (`main` + #250→#265 + the #256 p²-Witt head)
were verified ancestors of the integration tip with `git merge-base --is-ancestor`. PR base
metadata was not trusted as a substitute.

## Semantic conflict decisions

1. **#263 README / CLAIM_LEDGER** — additive-union (both Principia and the existing frontier
   blurbs kept).
2. **#260 ↔ #261 path collision (Hazard A)** — both families preserved as **distinct canonical
   modules** plus a scoped compatibility shim:
   - #260 (gauge / missing-prime / spectral-bulk) → `observational_succ/bbp_minimal_path_gauge.py`,
     `scripts/bbp_minimal_path_gauge_probe.py`, `tests/test_bbp_minimal_path_gauge.py`,
     `docs/CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH_GAUGE.md`,
     `.github/workflows/bbp-minimal-path-gauge.yml`.
   - #261 (odd-prime births / minimal recurrence / Galois) →
     `observational_succ/bbp_minimal_path_births.py` and the `_births_` probe/test/supplement/workflow.
   - `observational_succ/bbp_minimal_path.py` is now a compat surface re-exporting both disjoint
     public APIs (empty intersection, verified) plus `gauge`/`births` submodule namespaces; the two
     private `_prime` helpers stay module-local (gauge permits `p=2`, births requires odd `p≥3` —
     verified by execution). The ambiguous shared probe and workflow were removed; the two canonical
     ones replace them. #261-unique modules (`bbp_galois_tomography.py`, `bbp_prime_window_*`) merged
     unchanged. `bbp_cyclotomic_birth.py`: #261 == base, #260 == base+54 additions (strict superset),
     taken cleanly.
3. **Claim-ID collision (Hazard B)** — resolved structurally, not textually. Bare `MP-01..06`
   (#260) and `MP-01..09` (#261) preserved; registered namespaces `BBP_MINIMAL_PATH_GAUGE`
   (`MP.GAUGE`) and `BBP_MINIMAL_PATH_BIRTHS` (`MP.BIRTHS`) with a `resolved_collisions` entry for
   bare `MP`. #261's intra-file duplicate `MP-05` and later IDs were renumbered `+1` so each bare ID
   is unique in its file. `docs/CLAIM_SUPPLEMENT_BBP_MINIMAL_PATH.md` is now the dotted-FQID
   crosswalk (SHA-qualified originals → canonical FQIDs). `unregistered_prefix_collisions() == []`.
4. **#255** — clean.

## Scientific-account reconciliation

- `#252` source-fidelity correction promoted in README, CLAIM_INDEX, ROADMAP; the withdrawn
  "BBP four-pole lane closed" verdict routes to `BBP_SOURCE_MEMORY_REPAIR.md` and the corrected
  `CYC03_LANE_CLOSED.md` (R1–R8). Historical bytes kept in the `CYC03_*_HISTORICAL` reports.
- `docs/PROOF_MECHANISMS.md` current prose rewritten coherently (M2 `1/3` is a generic negative
  control, not an authenticated-source member; M4 `16^{-n}` **is** a coboundary, illustrated with
  `r_K`; §12.4 transient criterion requires a *faithful* pushforward and the four-pole lane was the
  misapplication; "equivalent reformulation" reframed to *no proof credit but still a useful
  representation*). Code verdict strings untouched.
- **SCE-01**: positive Poisson regret and minimum-relative regret are asymptotically **equivalent**
  to normality; the original *sufficient* direction remains valid and the equivalence is **not a new
  proof step**. The new route is the prescribed-scale collision bound `K_p(1)=p^{o(1)}` at `c=2/5`
  (SCE-07) with an explicit, still-**unverified** remaining hypothesis.
- A new plain-language "proved / finite-tested / open" split for source, finite observers, circle
  geometry, prime clocks, carry transport, Galois averaging and entropy is in `README.md`, with the
  visit-frequency caution. **π normality, its independence, RH, and absolute/decimal normality
  remain OPEN.**

## Validation evidence (combined tree, local)

Python 3.12.3. Gates run on the combined code at `dd6ca94` (the subsequent prose commit `bdb8538`
is **docs-only**: `git diff --stat dd6ca94 bdb8538` = README / CLAIM_INDEX / PROOF_MECHANISMS /
ROADMAP only); provenance re-confirmed on `bdb8538`.

| Gate | Result |
|---|---|
| `scripts/verify_provenance.py` | exit 0 — `SOURCE_PROVENANCE_VERIFIED`, 72 items, 17 byte-identical archives (re-confirmed on `bdb8538`) |
| `PYTHONPATH=$PWD python -m unittest discover -s tests -p 'test_*.py'` | exit 0 — **Ran 7601 tests in 922.8s, OK** |
| `scripts/observer_foundations_probe.py` | exit 0 |
| `scripts/ordinal_succ_report_probe.py` | exit 0 |
| focused: both MP families + shim + galois + prime-window + cyclotomic + namespace gate | 72 + 15 tests OK |
| gauge probe vs `BBP_MINIMAL_PATH_FINITE_RECEIPT.json` | `cmp` byte-identical |

The `7601` figure is the combined coherent-main tree; the historical `7374` in the #250 report was
the earlier 17-PR tree. Hosted (GitHub) CI on the pushed head is the separate required signal;
green donor-branch CI does not certify the combination. This receipt records the local evidence;
the hosted-CI result and final merge SHA are recorded in the campaign report.

## Distinct scopes

Paper proofs, exact finite experiments, and Lean kernel authority have distinct scopes. No Lean
kernel authority propagates to a neighbouring unformalized theorem. Finite numerical agreement is
not a proof certificate.

## Newest work, not included

PR #266 `research/pi-lag-carry-rigidity-2026-10-24` (`e821a90d…`) was created after the handoff,
stacked on #265, adding a new "linear-prefix source no-go / certified selected collisions" track
(27 new files). It is **not** part of the audited leaf set and is **not** folded into this merge;
it is retargeted onto `main` for the next research round.
