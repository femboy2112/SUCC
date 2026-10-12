# Integration audit — research stack consolidation (2026-10-11)

**Status of this document:** an auditable record of the consolidation that merged the
stacked research PRs #6–#22 into `main`. It records *what was merged, what was checked, and
what remains open*. It does **not** establish any mathematical result, and it is **not** the
canonical theory document.

**Canonical sources of truth** (do not duplicate theorem descriptions elsewhere):

- [docs/CLAIM_LEDGER.md](CLAIM_LEDGER.md) — every claim, its exact scope, and its status label.
- [docs/ARCHITECTURE.md](ARCHITECTURE.md) — the subsystem architecture and typed boundaries.
- [docs/METHOD.md](METHOD.md) — the steelman → crucible → verdict discipline.
- [AGENTS.md](../AGENTS.md) — mandatory research discipline and the positivity firewall.

## 1. What was consolidated

A single linear stack of 17 draft PRs, each based on the previous one and rooted on `main`:

| PRs | Theme |
| --- | --- |
| #6–#8 | ideal observational-frame completion; absorbing Hard SUCC; knowledge-ladder synchronization |
| #9–#11 | relative deltas / evolving bases; circle cross-language translation; twin-observer invariance |
| #12–#14 | proof-carrier backaction; basis-indexed boundary transport; discrete finite-difference integration |
| #15–#17 | Euler local/global ζ(−1) transport; residue-one adeles; Mahler/Kummer clocks |
| #18–#19 | proto-SUCC variable-unit lift; source-relative precision transport |
| #20–#22 | proof-backaction debt / Zeno; noncommuting source-proof transport / holonomy; operational Yoneda / policy descent |

**Topology (Verified).** `main` (`4a8e581`) is a strict ancestor of the stack tip
`research/operational-yoneda-policy-descent-2026-10-11` (`f060d465`): **274 ahead / 0 behind**,
89 files changed (+21318 / −5). Every one of the 17 PR head commits is an ancestor of the tip,
each appearing exactly once (0 duplicate patch-ids, 0 merge commits in range). The 5 deleted
lines are **not** file deletions: 4 are a README list renumber (items reappear verbatim), 1 is a
content replacement of the ledger's "General theory" outstanding-goal bullet (old wording
recoverable in history). **No file was deleted; `provenance/` is byte-for-byte untouched.**

**Merge strategy.** A single `--no-ff` merge commit of the tip into `main`, preceded by one
"integration corrections" commit (the two README fixes below + this document). A rehearsal merge
on a throwaway worktree produced a tree byte-identical to the tip's tree
(`f2d3aede…`), confirming the integration is **lossless**. The 17 research branches are
preserved on `origin`; nothing was force-pushed, rebased, or deleted.

**Reversibility (Operation Phoenix).** The integration is a single merge commit; it reverts with
one `git revert -m 1 <merge-sha>`. `origin/main` prior state recorded as `4a8e581`.

## 2. Validation receipts

Run against the exact integration content.

| Check | Command | Result |
| --- | --- | --- |
| Provenance | `python scripts/verify_provenance.py` | exit 0 — `SOURCE_PROVENANCE_VERIFIED`, 72 items, 17 byte-identical archives, `establishes_mathematical_truth: false` |
| Tests (local) | `python -m unittest discover -s tests -p 'test_*.py'` | **Ran 566 tests — OK** (Python 3.12) |
| Tests (CI) | GitHub Actions matrix `['3.10','3.13']` | success on tip `f060d465` |
| Probe | `python scripts/observer_foundations_probe.py` | exit 0; `universal_positivity_proved: false`, `first_observed_counterexample: 19` |
| Probe | `python scripts/ordinal_succ_report_probe.py` | exit 0; `positive_definiteness_proved: false` |
| Packaging | `pip install .` in a clean venv (`python -I`) | exit 0; `observational-succ 0.3.0`; 47 submodules import clean |
| Public API | module set `main` vs tip | 25 → 48 modules, **additive only** (0 removed/renamed/modified); version unchanged |

**Boundary:** local tests ran on Python 3.12; the 3.10/3.13 evidence is the GitHub Actions run on
the tip, not a local reproduction. Local `mpmath` is 1.2.1 (below the `>=1.3` pin) with no observed
effect on the 566-test run.

## 3. Adversarial audit (three independent read-only bearings)

The consolidation was gated on an overstatement audit, not merely on green tests. Three
orthogonal bearings plus the orchestrator's own checks were run; findings triangulated.

**Bearing — math claims (attacked, with exact recomputation).** No kill.
- O200/O202 noncommutativity is **genuine** algebra: `A=[[1,0],[1,1]]`, `B=[[1,1],[0,1]]` over
  GF(2), `AB≠BA`, distinct post-states at source `(1,0)`; both ordered reports reconstruct all
  four sources; route-blinding collides `original-a` but preserves `original-XOR`.
- Positivity firewall exact: `Ψ=t⁴` Gram at `±1` has **det −192**, all-ones energy **−24**;
  `Ψ=1−cos t` is Gram-PSD with sign-changing `Ψ″`; fake `a(6)=2` yields PSD covariance (a true
  tautology, correctly `UNVERIFIED`). The report path hard-codes a non-PSD-certificate status and
  `global_PSD_predicate_proved: false`; **nothing downstream relies on the refuted
  pointwise⇒global implication.**
- Prime-clock defect `d(1−q)` is **q-independent** (confirmed for composite `q=6`, `q=15`);
  primality enters only via an external trial-division predicate, with an in-source disclaimer.
  O232's REFUTED label is correctly earned.
- O131's analytic bound `0 < V_X − ζ(−1) ≤ 1/(12X)` holds (audited + confirmed at X=5,11,47).

**Bearing — integration mechanics.** All clean (see §1 topology, §2 packaging/API, provenance
untouched, 0 dead doc links of 88).

**Bearing — documentation prose.** **No clear overstatement in any human-facing doc.** The
firewall holds in every doc: no sentence claims RH proved/progressed/reduced, no completed-Weil
positivity from pointwise/physical/semantic positivity, no achieved supertasks, no Gödel
mechanized in PA. Arithmetic in the prose (det −192, E_p tail valuation, 721=7·103, δ₈=13, the
F/G zero-locus counterexample) was hand-rechecked and matches.

## 4. Corrections applied in this integration

Two README defects (flagged by the prose bearing, re-verified against the ledger and the source):

- **README.md** — "all-finite-protocol" narrowed to "every finite one-bit-per-action protocol",
  matching the actual scope of ledger **O176** (`PROVED LOCAL, PROTOCOL-RELATIVE`). The prior
  wording read literally broader than the theorem.
- **README.md** — notation typo `ℚ/4→ℚ/2` corrected to `ℤ/4→ℤ/2` (`ℚ/4ℚ` is the zero group; the
  prime-clock construction is on `ℤ/pʳ`, as the memo correctly writes).

No code, test, ledger status, provenance file, or archived original was modified by this
integration beyond these two README lines and the addition of this document.

## 5. Known issues and recommended follow-ups (not merge blockers)

Recorded rather than silently edited; benign in substance, inside research memos or editorial.

1. **Memo ↔ ledger ID/label drift.** Several `research/**` memos cite ledger IDs or labels that
   drifted from the canonical ledger (e.g. a memo lists `O82` as `UNVERIFIED` where the ledger
   records `O82` as `REFUTED`; polarity-inverted ID cites around O106/O110/O113/O91; O71 cited as
   "PROVED LOCAL/symbolic classical" vs ledger `CLASSICAL`). The **ledger is canonical and
   correct**; the memo cross-references should be reconciled to it.
2. **METHOD vs O24 status.** METHOD.md's worked example calls the "semantic positivity ⇒ RH"
   framing a *productive failure* with a receipt (fake `a(6)=2`), yet ledger O24 is `UNVERIFIED`
   rather than `REFUTED-as-inference` (cf. O12, O35). An under-claim, but a status inconsistency
   worth reconciling.
3. **O28 / balanced_theta_li.py.** The `< 2⁻ᵏ` Li-window accuracy claim is `PROVED LOCAL under
   stated analytic bounds`; the executable check uses a non-directed `mp.erfc` floating comparison,
   **not** rigorous interval arithmetic (AGENTS.md rule 8). Both the module docstring and the
   ledger qualifier already flag this, so it is honestly labeled — but the proof lives in the
   `BALANCED_THETA_LI_WINDOW` memo, not in the code. Do not lean on O28 as if the code certified it.
4. **RH handoff provenance.** `handoffs/rh/2026-10-10-prime-source-certification.md` lacks the exact
   originating SUCC commit SHA that `RH_HANDOFF.md` item 3 requires ("Pin its exact SHA when
   integrating"); it is also not linked from the ledger per `RH_HANDOFF.md:22`.
5. **Stale stack references.** Some memos hard-code "stacked draft PR #N", branch names and SHAs
   that are stale now that the stack is consolidated onto `main`.

## 6. Honest status summary

Grounded in the claim ledger; see it for per-claim scope.

- **Proves (CLASSICAL / PROVED LOCAL, exact, many with matched fake/control counterexamples):**
  measurement-order dependence of noncommuting quantum records (O03); genuine GF(2)
  noncommutativity with full source reconstruction (O200/O202); the positivity-firewall
  counterexamples (O12/O13, with exact indefinite Grams); finite-observer version-space
  contraction and trap partitions (O47–O53); source-relative p-adic precision transport and its
  composition/debt algebra (O166–O172); unconditional finite Newton/Pascal jet inversion within an
  observed horizon (O126); exact Euler-factor and ζ(−1) transport facts and the finite-cutoff bound
  (O128–O134); Mahler/Kummer unit-clock identities (O149–O154); the operational-Yoneda path
  category, bisimulation, and optimal-proof-rank preservation (O210–O234); the prime-clock quotient
  commuting with SUCC/FUCC (O227).
- **Models (TESTED MODEL / HYPOTHESIS, not theorems of the physical world):** the physical-carrier
  premise (O01); quantum record/engine tamper models (O02); semantic log-partition covariance
  models; observer-trap and twin-observer focus simulations.
- **Conjectural / UNVERIFIED:** **every RH bridge** — the Li-positivity equivalence (O29,
  RH-equivalent, **RH open**), the missing noncircular source-to-Weil identification (O33), and the
  full wall of "this construction yields RH / Weil positivity / holography / a proof-independence
  result" claims (O46, O54, O73, O83, O92, O101, O107, O117, O125, O135, O148, O155, O164, O174,
  O183, O198, O209, O222, O235). Also: Gödel coding not mechanized in PA (O19); RH's independence
  from PA/ZFC unknown (O34).
- **Refuted (kept as labeled corpses with receipts):** pointwise ⇒ global PSD (O12); PSD needs
  pointwise-nonnegative second derivative (O13); provenance ⇒ truth (O35); the long list of
  "finite/local structure ⇒ universal/RH-strength" inferences (O08, O15, O17, O21, O23, O80, O82,
  O89, O113, O129, …).

## 7. Next most valuable experiment

The single bridge whose absence keeps the entire RH direction `UNVERIFIED` is a **rigorous
Archimedean/pole interval-arithmetic oracle** (replacing the floating `erfc` comparison flagged in
§5.3 / O28) together with a **noncircular identification of a source-derived positive distribution
with the completed Weil form** — built from authentic Euler/prime-power sources, correct
half-density, Gamma and pole completion, with the fake-composite and matched non-Euler controls,
and **no nontrivial zero positions used as construction inputs**. Until that identification is
supplied, no amount of finite positivity or Yoneda faithfulness advances RH, by the project's own
firewall.
