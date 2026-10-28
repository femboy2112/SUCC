# SUCC Topic Atlas — domain map, genesis, and natural-language crosswalk

Companion to `INDEX.md` and `RELATION_GRAPH.json`. Each domain resolves a human question to concept nodes (`MM-*`), claim families (via `CLAIM_CATALOG.json`), and the open gate. **Nothing here promotes a status**; π/RH are OPEN.

## Natural-language aliases (vague query → where it lives)

| If you half-remember… | It is… | Entry points |
|---|---|---|
| "that lattice that zoomed out into a Yoneda point" | the finite-local → global **conjectural** strategy (not an automatic proof) | `MM-I-016`, `MM-T-013/014/015` (PRs #22/#27/#28) |
| "the circle, triangle, golden-ratio and Euler–Mascheroni thing" | the genesis: pointed circle → Farey triangles → φ⁻¹ fixed point → γ discrepancy → Ω | `MM-I-001`,`MM-T-003..006`,`MM-D-007` |
| "the two golden numbers that weren't the same" | φ⁻¹ (Farey/Gauss) vs φ⁻² (Oily packet PGF) — distinct lineages, same Ω value | `MM-T-004` vs `MM-T-045`; edge `MM-T-045 --does_not_imply--> MM-T-004` |
| "the hammer/echo that was secretly π" | causal Green convolution `U_n=Σ16^s r(n−s)` + the LTI delay no-go | `MM-N-039` (PR #323) |
| "the clock that was 2-adic and 3-adic at once" | joint 2×3 CRT source clock + p-adic isometries | `MM-T-034/035/036` (PRs #320/#321/#322) |
| "the certified base-3 digits of π" | a certified digit *computation* (not a spigot; base-3 normality OPEN) | `MM-T-047`,`MM-O-050` (PR #331) |
| "the one categorical thing that actually worked" | the `is_cartesian` signed-transport firewall | `MM-T-040` (PR #306) |
| "the Kempner number that killed the entropy argument" | the counterexample refuting transcendence→entropy | `MM-N-021`,`MM-N-051` (PR #337) |
| "the x2/x3 rigidity bridge" | conditional Rudolph–Johnson route (two unproven hypotheses) | `MM-C-043` (PR #332) |

## Genesis — the original intuition, corrected (Mission III)

The author's image: mark one point on a circle, cut it open to a line, triangulate recursively in an arithmetic way; take φ⁻¹ as the ideal coherent path and γ as its logarithmic/realized counterpart, with **Ω = φ⁻¹ − γ** the ideal-vs-realized defect (`MM-I-001`, `MM-I-008` — *intuition/conjecture, not established*).

The Farey–Gauss realization makes **one** precise common system: ideal Farey triangles on the modular boundary {0,1,∞}; the all-ones continued fraction has fixed point **λ = φ⁻¹** (`MM-T-004`); the Gauss digit-tail law ×log2 is log(1+1/k), whose discrepancy against the harmonic 1/k accumulates to **γ** (`MM-T-005/006`). This makes Ω a *declared same-dynamical-system comparison* (`MM-D-007`) — **not** a canonical invariant of the bare circle, and **not** a proof of the ideal/realized interpretation (`MM-I-008` stays UNVERIFIED).

**Keep the lineages separate (no proven functor):**
- **Farey/Gauss**: λ = **φ⁻¹** (continued-fraction fixed point). `MM-T-004`.
- **Oily packet** (PRs #309/#310): PGF `G(z)=1/(2−z)²` ⇒ fixed point q\* = **φ⁻²**, with its own Γ(2)-centered log giving the same Ω value; third-order shadow carries `−(8/27)(φ⁻¹−γ)`. `MM-T-045/046`, and `MM-T-046 --shares_value_with--> MM-D-007` (equal Ω **value**, not a common source).
- **PR #303**: projective triangle + an *extra chosen* golden cross-ratio and a separately normalized Kronecker γ cusp. `MM-T-009`.

Matching Ω across these is a shared scalar, not an isomorphism of sources.

## π / BBP / Weyl — the gate and its moat

- **Reduction** (`MM-T-030`, SGO-09/#293): π base-16 normal **IFF** `Ŝ_N(h)=Σe(hU_n)=o(N)` ∀h≠0; the carrier is normality-neutral. The gate is `MM-O-022`.
- **Authentic source** (`MM-T-017`): four-pole `r(n)=A(n)/D(n)`, `U_n=16^{n−1}π−T_n`.
- **Best proven moat** (`MM-T-031/032`): carry packing `K_N=O(N/log N)` and the absolute logarithmic loss `|S_N|≤N−(1/14)·(log-count)` — **N−O(log N), normalizes to 1, never o(N)**.
- **CRT energy gate** (`MM-T-033`, `MM-O-022`): exact CRT Plancherel identity; decay of `E_{N,M}` along admissible `M=16^k3^L=o(N)` would close the gate — **unproved, strictly stronger than normality**.
- **Counterfeits/no-gos** (`MM-N-038/039/041`): per-band nonnormal counterfeit (SB-4); LTI delay no-go (echo); signed-pushforward obstruction map. These cap finite-resolution and linear-transport routes.

## p-adic clocks / adelic / rank / Furstenberg

- 2-adic source isometry + odometer (`MM-T-034`, PR #320); 2-adic zero boundary `C_past=0` (`MM-T-035`, PR #321); joint 2×3 CRT clock + 3-adic isometry (`MM-T-036`, PR #322).
- **Rank-1 obstruction** (`MM-T-048`, AR-4): the transverse p-adic Haar bulk is decoupled from the archimedean rank-1 slice; p-adic coordinates are *contracting charges*, not a second expanding momentum. Rank-2-bulk→rank-1-slice is **REFUTED** (`MM-N-049`).
- **Conditional bridge** (`MM-C-043`, AR-5): unaveraged ×3 defect decay + positive entropy ⇒ normal via Rudolph–Johnson — both hypotheses unproven.
- **Furstenberg** (`MM-N-021/051`, PRs #334/#337, both STALE): all-prime rigidity is a *reformulation* (`MM-T-052`); the transcendence→entropy leg is refuted by the Kempner number (zero entropy).

## Observer / Yoneda local-to-global

`MM-T-013/014/015` (PRs #22/#27/#28): restricted-probe Yoneda; Čech/Yoneda gluing holds **only** with complete-overlap holonomy vanishing; source-fiber descent — pairwise-consistent local reports need **not** be jointly realizable. The "zoom out to one point ⇒ global theorem" step (`MM-I-016`) is a **conjectural design**, not an automatic proof of π or RH.

## Categorical signed transport, formal authority, RH

- **`is_cartesian` firewall** (`MM-T-040`): signed amplitude base change is lawful iff the square is cartesian; realization-faithfulness is necessary-not-sufficient. The one positive classical product of the Skeleton-Key round.
- **Formal authority**: Lean kernel receipts (pinned mathlib 4.14.0) back the *finite* algebraic cores only; `proof_authority.py` levels gate what counts; no Lean result claims normality or RH.
- **RH / Weil** (`MM-O-023`): OPEN; positivity without original source + completed Γ/pole/Weil domains does not count.

## Current frontier (smallest open obligation)

Prove `E_{N,M_N}(h)→0` for **one** admissible `M_N=16^{k}3^{L}=o(N)` and every fixed h≠0 — equivalently (`MM-T-030`) the selected real Weyl `o(N)`. Everything above either reduces to this, bounds it from above at `N−O(log N)`, restates it as an equivalence, or refutes a shortcut past it.
