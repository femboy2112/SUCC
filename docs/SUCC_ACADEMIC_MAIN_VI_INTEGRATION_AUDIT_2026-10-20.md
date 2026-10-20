# SUCC Academic Main VI — Integration Audit (2026-10-20)

**Operation.** Academic Main VI, *The Proof Forge* — integration phase. Consolidate the seven sibling
draft PRs **#192–#198** into `main`, then build proof machinery (separate research lane; see the
Mason–Stothers proof-forge branch).

**Verified base.** `origin/main = 455600a2e013895c36238a3a97e0f470fd7ba197` (Academic Main V, PR #191).
**Integration branch.** `integration/succ-academic-main-vi-proof-forge-2026-10-20`.
**Integration head.** `65b839d6a3bb0e6858a5e3f8fdc035929cb6e97d`.

**Firewall (load-bearing, unchanged).** RH PROVED: **NO**. ABC **OPEN**. The authentic signed Suzuki
`S₄ = A₄ − R₄` sign is **OPEN (AMBIGUOUS)**. No positive analytic/Hilbert Gram is the signed completed
Weil form. No nontrivial zeta-zero ordinate is a construction input. `Λ(p^k)=log p`; one real archimedean
Γ. The #181/#182 prime-two inverse estimates are **alternatives** — never summed. Frozen imported originals
untouched. Exact arithmetic (Fraction / sound interval); a float is never a certificate. A green suite is
not a proof.

---

## §0 — Intake (verified, not assumed)

Known snapshot (Oct 20): `main = 455600a`, seven open sibling draft PRs #192–#198. All verified from
disk against `git rev-parse`:

| PR | head (short) | branch | area |
|----|------|--------|------|
| #192 | `2ede8b26` | amv-moonshot-c-hologram-naturality | arithmetic/transport |
| #193 | `fbb056dd` | amv-moonshot-b-maxcut-repair | foundations/proof-authority |
| #194 | `9952e672` | amv-moonshot-a-beck-chevalley | foundations/proof-authority |
| #195 | `ba6c2c9f` | amv-moonshot-e-rh-source | RH-facing interface |
| #196 | `52adcea7` | amv-moonshot-d-abc-moment | global arithmetic analysis |
| #197 | `10cac570` | portable-prime-sundial-rational-succ | arithmetic/transport |
| #198 | `8cf59485` | carrier-relative-lem-fuckedfields | foundations/proof-authority |

#192–#196 are the Academic Main V Thinker-Dome moonshots (A–E), previously built and verified from disk;
#197 and #198 are genuinely new (branches fetched this session). All seven had **green CI on their exact
heads** (verified via `gh pr checks`).

## §1 — True dependency DAG (git ancestry, not PR labels)

Recovered by a pairwise `git merge-base --is-ancestor` matrix plus `git rev-list --count <head> ^main`:

- **Every head forks directly from `main=455600a`** (merge-base = main for all seven).
- **The pairwise ancestry matrix is all-negative** — no head is an ancestor of any other. The seven are
  **independent siblings**, not a stack.
- Unique-commit counts: #197 = 27 commits; the other six = 1 commit each.

There is therefore no double-count hazard and no mandated merge order. Merges done history-preserving with
`--no-ff`, one per head, in semantic order **#194, #193, #198, #192, #197, #196, #195**.

| PR | merge commit |
|----|------|
| #194 | `260bad1` |
| #193 | `bee7b09` |
| #198 | `b8ddab3` |
| #192 | `0d25df3` |
| #197 | `0cceb42` |
| #196 | `d1d5216` |
| #195 | `65b839d` (head) |

All seven heads verified **ancestors of the integration head**.

## §2 — Merge, conflict, completeness

- **Conflict surface: none.** Six branches are disjoint new-file-only sets; only **#197** touches shared
  docs (`README.md`, `docs/CLAIM_INDEX.md`, `docs/CLAIM_NAMESPACE_REGISTRY.json`), and #197 forked *from*
  the Academic Main V registry, so its edits are additive. The `ort` strategy auto-merged all seven with
  zero conflicts. Total: **32 files changed, +8702, 0 deletions** (union = 7 disjoint sets; #197's 11
  include the 3 shared-doc edits).
- **Namespace registry.** 24 namespaces (#197 added `PORTABLE_PRIME_SUNDIAL`/`PSD`). Live guard
  `unregistered_prefix_collisions() == []`.
- **Completeness repair.** Six of the seven dossiers had **no** navigation from `CLAIM_INDEX.md`. Added an
  Academic Main VI research-intake navigation block (prose links, not claim-table rows — so the collision
  guard stays clean) and a README top-level pointer. Research-status dossiers are **not** promoted to
  registered claim families (Academic Main V precedent): fresh dossier prefixes `PR` (#193), `ABC-TMB`
  (#196), `CRL` (#198) live in their dossiers; #197's `PSD` is the only promoted family this round.
- **Status discipline.** Only #197 (`PSD-01…14`, MIXED CLASSICAL/PROVED PAPER/TESTED FINITE/UNVERIFIED) is
  a promoted claim family. #196's `ABC-TMB-01` is PROVED LOCAL (and labeled strictly inferior to BBLT).
  #195 is a firewall scaffold that **cannot** certify RH. Nothing here promotes a conditional equivalence
  to a proof.

## Coherence map (Part II)

- **Layer A — arithmetic.** #196 (primitive ABC-triple ris-moments, exact Fraction census) and #197
  (rational dual-unit sundial, CRT prime-power phases, RAD/RIS births). Exact arithmetic throughout.
- **Layer B — categorical / logical transport.** #194 (Beck–Chevalley realization firewall), #198
  (carrier-relative LEM, Diaconescu choice/LEM firewall preserved), #193 (F₂ parity obstruction / repair
  cost). The choice/LEM distinction and the formal-compatibility-vs-lawful-realization distinction are
  preserved.
- **Layer C — harmonic-analytic.** #192 (hologram transport calculus: sampling-range reconstruction,
  composition law, off-lattice nonrecoverability). Reconstruction holds on the range only — never
  globalized to point evaluation on L².
- **Layer D — global certificates / RH interface.** #195 (source→signed-Weil obligation checker). No path
  to `identified:True`; five negative controls each rejected; `S₄` sign AMBIGUOUS.

## §4 — Validation gates (integrated head `65b839d`)

| Gate | Result |
|------|--------|
| `scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, 72 items, source `ba075348…` |
| `python -m compileall observational_succ tests scripts` | OK (2 pre-existing docstring `SyntaxWarning`s inherited from `main`, not introduced here) |
| `scripts/observer_foundations_probe.py` | exit 0 |
| `scripts/ordinal_succ_report_probe.py` | exit 0 |
| Lean 4.14.0 — `formal/PortablePrimeSundial.lean` (only new Lean file) | compiles clean (exit 0); `#print axioms` = `{propext, Quot.sound}` — **no `Classical.choice`** |
| Full `unittest discover -s tests` | **`Ran 6135 tests — OK`** (py3.12 local, 608s; 6135 = 6001 Academic Main V + the #192–#198 suites) |
| Per-head CI (all 7) + consolidated-head CI | all green per head (verified `gh pr checks`); consolidated head via PR #199 (see addendum) |

**Validation addendum (full suite).** Full `python -m unittest discover -s tests` on the integrated head
(records commit `c1a8cfb`, tree identical to merge head `65b839d` + doc commit) ran **6135 tests, OK**, local
Python 3.12 with `PYTHONPATH` set (one probe test subprocess needs the package importable; CI's editable
install covers it). Hosted CI on the exact consolidated head is the authoritative multi-version (3.10/3.13)
gate — see PR #199.

## §5 — Disposition

- **Integrate → `main`:** all seven PRs (#192–#198), the integration object explicitly authorized for this
  operation. `--no-ff`, history-preserving, no squash, no force-push, no rewritten originals.
- **Deferred to a separate research lane:** the Proof Forge machinery and the Mason–Stothers proof
  certificate (new feature family — per the operation's own rule, integration finishes before new families,
  and new machinery ships on its own draft branch for independent review even when the math is classical).
- **Branches retained;** no deletions, no force-push.

**Verdict: GO** for the integration object (pending the full-suite addendum + consolidated-head CI green).
RH, ABC, and the signed `S₄` sign remain **OPEN**. Firewall intact.
