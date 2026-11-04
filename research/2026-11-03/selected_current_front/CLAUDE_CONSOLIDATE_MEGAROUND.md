# CLAUDE OPUS — SUCC CONSOLIDATE → MAIN → SELECTED-CURRENT MEGA-ROUND

**Execution mandate:** work in `https://github.com/femboy2112/SUCC`, not a hypothetical repository. This is a request from the maintainer to consolidate the active SUCC research, validate it, and **merge the verified integrated result into main**. Research-only new claims must retain exact status; do not tag, create a release, publish a paper, edit the license or force-push. If tests/branch protection block a safe merge, produce a reviewed integration PR and an exact blocker report rather than misrepresenting success. Spend substantive time doing new proof-producing mathematics after consolidation; do not stop at a roadmap.

## 0. Baseline and provenance (MUST execute)

- Check current repository, remote URL, branch, commit, worktrees, uncommitted changes, GitHub PR heads and `AGENTS.md`. Protect existing local worktrees and untracked content. Pull main with fast-forward only. Record exact source identity: original `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U0=0`, and literal real integer carries. Inspect frozen source archives, `provenance/IMPORT_MANIFEST.json`, formal imports, CI workflows and claim ledger before any source modification. **Do not modify the four-pole source or the zero boundary.**
- Read the new research PR for `research/pi-selected-current-shift-coupling-2026-11-03`, including `PROOFS.md`, `FRONTIER.md`, `INTEGRATION_AUDIT.md`, `VALIDATION.md`, `FINITE_RECEIPT.json`, code/tests and the upstream PR #488 dossier. Check exact live head before merging.

## 1. Three distinct branches, not 16 independent merges

An independent GitHub audit at main `81045770234a114247e43eb08ae5c6d446e9514a` found THREE research trunks. REQUERY all refs; the following are historical pins, not instructions to overwrite newer commits:

1. **#488** `f47e3768631cd1628c1390d529811c911e0f6443`: 115 commits and 240 added paths ahead of main; ancestry includes #465→#468→#470→#471→#473→#474→#475→#476→#479→#481→#483→#484→#485→#487→#488, and the NEW child current-front PR to be integrated on top.
2. **#486** `9eea9e3e89022b9a57716f21b31ffc3e69f0552f`: sibling line #475→#477→#478→#480→#482→#486, 156 commits / 145 added paths. **95 added path names overlap #488**, but the branch is NOT an ancestor: compare found it diverged at #475. It has 50 unique added paths. Do not assume the overlapping 95 blobs are identical—COMPARE THEM.
3. **#472** `85189e389ca1568636a7fedb7b2d6268b8eae447`: independent selected-prime/causal-response/oily-hbar line #462→#463→#464→#466→#467→#469→#472, 161 commits / 104 added paths. At the audit all 104 are distinct from both tips above.

**Union of these three historical tips: 394 distinct added paths** relative to main, with no inherited-path edits or deletions in any main-relative comparison. The counts do NOT guarantee conflict-free merges, scientific correctness, or cover every other open PR. Inventory every other open π-related draft; classify included-by-ancestry, sibling donor, unrelated/incomplete, or blocker. Never merge an unrelated experimental branch just because it is open.

**Suggested implementation:** create an isolated integration branch/worktree from FRESH main. Merge latest NEW current-front research tip (includes #488) with `git merge --no-ff`, reconcile and merge #486, then reconcile and merge #472; if another topology is safer, prove it with `git merge-base` and file/commit sets. No cherry-picking of the same historical ancestor twice; no force push. Git merge will handle committed ancestry but **you must examine different blobs at overlapping paths and all test/import dependencies**. Resolve conflicts openly; keep raw ancestor receipts and record provenance of each decision.

## 2. Required validation and acceptance gate

- Audit the final diff against source contracts; original all-four-pole BBP source, literal U0, archived imported proofs, formal theorem names/types, license and workflows MUST stay unchanged unless a necessity is evidenced, separately authorized, and source-provenance-safe.
- Run each new focused test and its declared `--verify` receipt replay, including the current branch's exact source/origin-integral tests. Then at the FINAL combined head run the repository's REQUIRED native checks:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

- Test formal Lean theorem contracts using the repository's genuine Lean build procedure; do not infer new Lean authority from existing core CI. Check GitHub Actions for the final **exact integrated commit**; distinguish queued/running/success from parent success. Existing exact-head historical snapshots: #486 4/4 hosted workflows succeeded; #472 4/4 succeeded; #488 had 3 succeeded and 1 in progress. Refresh these statuses.
- Reproduce the original selected arithmetic countercontrols: changed real seed with identical forcing, p-free cofactor locking, coherent residue ghosts from #487, period-five fixed point, fake independent Gaussian split/inert prime means, false inert long-window p=47/n=18, boundary-straddling rational cylinders, and Gamma tail source mutants. A mathematical status promotion requires an independent proof, not agreement among same-model receipts.
- Create an integration PR for review (can be draft while blocked); **merge to main** only if all mandated checks and source/claim-review gates pass. Report exact merged main SHA. No blind merge of dozens of draft PRs or silent mass-closing: annotate dispositions after successful integrated merge.

## 3. Reorient SUCC coherently around ONE active π research front

Preserve SUCC as a freestanding categorical observation theory with RH separate. Update `README.md`, `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`, roadmap, architecture, and source/claim/mathematical-memory index with attribution and a single active link to `FRONTIER.md`. Retain history and no-go results without presenting them as current proof priorities. Keep a **typed** DAG: original full source → zero-seeded Gaussian/real & p-adic gluing → odd-prime/cofactor and true integer carries → real circle → source-selected 16-ary cylinder current → energy/Fejér/Ward → *conditional* normality.

Status must stay explicit: original source-selected energy `E_(A,m_A)=o(log m_A)` or signed Weyl `S_N(h)=o(N)` for every fixed nonzero h is OPEN. **π normality is OPEN.** Gamma and Feynman/electrical analogies are instruments, not source-selected cancellation laws. RH is OPEN. Source citations and precise theorem scopes must accompany every merger into a claim ledger.

## 4. BLAST REAL MATHEMATICS AFTER INTEGRATION — not roadmap-only

**Primary target:** source-selected branch-current inequality on all dyadic A, with `K_A=floor(log_16 log A)`, `m_A=16^K_A`, and exact source `mu_A=A^-1 sum_(n=A)^(2A-1) delta_{ {U_n} }`:

`E_(A,m_A)-1 = sum_(k<K_A)16^(k+1) sum_(w,j) (mu_A(wj)-mu_A(w)/16)^2 = o(K_A)`.

The NEW source-selected, origin-averaged equivalent sufficient route is
`J_(A,m_A/2)=(m_A/2)/A² sum_(n,t) (1-(m_A/2)||U_n-U_t||)_+ = o(K_A)`.
The new proven lemmas give `E_(A,m_A)(0)<=4 J_(A,m_A/2)` and Gamma transport `|J_q(X)-J_q(U)|<=q²(A-1)/(64 A³)`, without a bin-boundary exception. They **do not prove** the needed smallness. The shifted-time source crossing law `B_(A,q)<=15q/[(8A+1)(8A+2)]` only gives approximate stationarity; fixed point 1/5 refutes any assertion that this alone forces Haar.

**Plan a real discriminating probe:**

- Derive an exact **chronological source/carry update** for shifted 16-ary conditional current vectors, with the full four-pole forcing and certified Gamma error. Keep source time separate from the spatial cylinder index; calibrate the true original transition and an independent modular source oracle.
- Split the current imbalance into authenticated split/inert prime clocks plus FULL old-prime Archimedean cofactor and literal integer carry. Use #485's correct three-window p passports and #487's coherent CRT ghost to test any proposed numerator nonconcentration inequality. A Galois average is not a source-selected real bound.
- Attack a fixed frequency lag family or a **polylogarithmic low Fourier band**. From the triangle sinc² Fourier formula, for q>=2, `J_q <= 1 + sum_(1<=|h|<=H)|c_A(h)|² + 2q²/(π² H)`. Taking `H=ceil(q²)` leaves an absolute tail below `2/π²`, so a real source-derived signed second-moment saving on `|h|<=O(log² A)` would be sufficient. This is a new explicit finite-band target, not an achieved bound. Ensure the existing prime nonalias theorem applies to the chosen h and that the selected old cofactor is paid, not assumed.
- Test alternative source-specific conductance/voltage laws only if they are genuinely derived from the marked BBP source. A uniform 16-path ensemble has exact cancellation even for nonnormal x=1/5 and is not a proof. If a plausible inequality is false, generate a decisive exact counterexample and retain the corpse.
- Use NEW held-out epochs/meshes not used for fitting. Preregister them before testing. Validate against an independent exact common-odd-denominator implementation, rigorous interval Gamma/origin-integral observables, and the five hostile source families. DO NOT CLAIM all-N from finite computation.

**Deliver something concrete:** a new proved source-derived signed/near-pair inequality with exact quantified scope and honest residual budget; OR an independently verified counterexample to the most promising candidate together with the strongest surviving lemma. Implement the result in a separate research branch after main integration, attach exact receipts and a draft PR. No speculative theorem-status promotions.

## 5. Final report required

State exactly what merged to main (refs, commits, tests, Lean, CI, provenance), what remained pending, precise file/PR disposition, consolidated new front link, and mathematically earned results versus still-open premise. If a gate fails, report the blocking test/raw log and leave a safe draft integration PR. Never invent completed work or promise later/asynchronous execution.
