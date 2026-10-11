# Development method: steelman, crucible, verdict

**Version:** adopted October 2026. **Status:** governing methodology for turning informal proposals into ledger-labeled claims. This document fixes a *process*; it does not itself establish any mathematical result.

## Purpose

Observational SUCC advances in large part from physically- and semantically-motivated intuition, expressed first as informal prose and analogy (see [FOUNDATIONS.md](FOUNDATIONS.md)). This document fixes the discipline that converts such raw proposals into claims carrying a defensible [claim-ledger](CLAIM_LEDGER.md) status. It applies to maintainers, contributors and coding agents alike, and **complements — does not replace** — the mandatory research discipline in [AGENTS.md](../AGENTS.md).

The method has one governing commitment: **charity in the reading, rigor in the testing.** A proposal is first reconstructed in its strongest faithful form, then tested adversarially against established mathematics. It is never dismissed on a weak reading, and never promoted on an attractive one.

## The loop

Apply to each proposal — a hypothesis, an analogy, a proposed arrow between pipeline levels, a suggested diagram, a candidate theorem.

### Stage 1 — Steelman (faithful reconstruction)

Reconstruct the strongest version of the proposal that the author would still recognize as their own.

- **Preserve the author's framing.** Keep the proposed object and the structure of the analogy. Do not silently replace it with the nearest existing textbook construction.
- **Faithful-strong, not maximal-strong.** Do not inflate the claim into something stronger than intended and then attack that; a strawman in heroic costume is still a strawman. The steelman is the strongest reading *consistent with what was actually said*.
- **Surface the reading when it is load-bearing or ambiguous; apply it silently when it is unambiguous.** When a proposal admits more than one serious reading, state the chosen reading in one or two lines and let the author correct it before effort is spent. Testing a misread steelman wastes work and attacks a position no one holds.
- Record the explicit objects, domains, hypotheses and quantifiers the steelman commits to (AGENTS.md discipline, item 4).

### Stage 2 — Crucible (adversarial test)

Stress the steelman against reality and attack it where it is weakest. Instruments:

- established theorems (CLASSICAL results) with which the claim must be consistent;
- explicit counterexamples, and the existing REFUTED corpses recorded in the claim ledger;
- the typed-boundary discipline of [ARCHITECTURE.md](ARCHITECTURE.md) — does the proposed arrow actually respect `observation → history → semantics → proof → report`, or does it quietly cross a boundary?;
- the **positivity firewall** (AGENTS.md item 6; [FOUNDATIONS.md](FOUNDATIONS.md) §3–4): pointwise / physical / semantic covariance positivity does **not** entail completed-Weil positivity, and fake arithmetic sources reproduce the cheap positivity. Any proposal that relies on this implication is suspect by default;
- exact algebra or sound interval arithmetic for any finite sign or positivity claim (AGENTS.md item 8) — floating-point agreement is never a certificate.

**The receipt rule (hard constraint).** A refutation must carry a receipt: a concrete counterexample, a cited established theorem, an existing ledger REFUTED entry, or a typed contradiction — *demonstrated*, not asserted. If no receipt can be produced, the proposal is **not** refuted: it is recorded as `UNVERIFIED` with the precise wall that blocked the test named explicitly. A refutation without a receipt is a category error and is not permitted.

### Stage 3 — Verdict

Every pass ends in exactly one of three outcomes, each emitting a claim-ledger label and an explicit scope — never a shrug:

- **SURVIVES** — state what the claim buys, at what ledger label (CLASSICAL / PROVED LOCAL / TESTED MODEL / HYPOTHESIS), and its **boundary**: what it does *not* establish. Surviving a test is not a status promotion; an upgrade still costs an independent proof (see the CLAIM_LEDGER.md policy).
- **FAILS** — state the exact conflict with its receipt, then the options:
  - **repair** — restrict the domain, weaken a quantifier, or change the arrow so the claim becomes defensible;
  - **pivot** — the nearby *true* statement the proposal was approximating;
  - **retire** — record the labeled REFUTED corpse and keep it. Do not delete rejected countermodels (see CONTRIBUTING.md).
- **PRODUCTIVE FAILURE** — a failed proposal frequently leaves a true residual constraint or a lemma target. Record it as the next falsification opportunity; this is often the most valuable output of the loop. Example: the "semantic positivity is sufficient for an RH conclusion" framing failed, and left behind the *source-faithfulness architectural constraint* now attached to claims O33 and O37.

## Recording a result

A completed loop produces a ledger-ready record: the steelmanned statement with its scope, the verdict label, the receipt (or the named wall), and the next falsification opportunity. Load-bearing results are entered in [CLAIM_LEDGER.md](CLAIM_LEDGER.md) with provenance, per the ledger's update policy — *"An update to a theorem's status must link to an actual proof or regression evidence."* Numerical agreement alone never promotes a claim.

## Worked example (illustrative; ledger entry O12)

- **Proposal, steelmanned:** if a second-order observable is pointwise nonnegative everywhere, the global two-time correlation (Gram) should inherit positive-definiteness — positivity usually propagates from local to global in analysis.
- **Crucible, with receipt:** `Ψ(t) = t⁴` has nonnegative value and nonnegative `Ψ″` everywhere, yet the two-time Gram at `t = ±1` is `[[2, −14], [−14, 2]]`, determinant `4 − 196 = −192 < 0` (indefinite). Receipt: existing ledger entry **O12, REFUTED**.
- **Verdict — productive failure:** the intuition was mis-located, not worthless. Positivity for this theory lives in the correlation / observable algebra, not pointwise. Residual constraint: derive covariance positivity only from bona fide positive states on the correct observable algebra (see Stage 3 of [ROADMAP.md](ROADMAP.md)).

## What this method is not

- It is not a source of mathematical truth; it labels and scopes claims, it does not prove them.
- It does not authorize status upgrades by accumulation of agreeing observations.
- It does not override AGENTS.md discipline, the provenance gates, or the licensing and branch policy.
