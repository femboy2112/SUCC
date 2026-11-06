# Selected zero-boundary signed-lag attack (post-Main-XIX research)

**Status: research-only, negative/obstruction round. No π normality, no RH, no signed-saving
claim.** This is the post-merge research assault the Main XIX directive called for (Fronts A/B/C),
executed against the **literal zero seed** `U_0=0`. It produced no advance on the gate — as
expected — but it sharpens exactly why the available tools cannot, and names the one discriminator
they lack.

## What this round establishes

- **SZB-01 (exact):** the zero-seed corrected lag phase splits as *(counterseed corrected phase)* +
  *(Fejér-weighted autocorrelation of π's hex digits)*. So at the compensated clock the attack IS
  the gate; a route must add new content.
- **SZB-02 — a refuted lemma:** the natural positivity shortcut ("the compensated-clock corrected
  zero-seed score is one-sided") is false — persistently negative per-lag correlations across the
  whole tested grid.
- **SZB-03 — Front B, a representation identity:** the angular-period identity (AC-13) is seed-blind;
  it holds identically for the normal-candidate zero seed and the nonnormal `q=1/5` orbit of the
  same source, so it cannot be a normality mechanism.
- **SZB-04 — Front C, an obstruction:** the within-cell signed phase equals the gate at a shifted
  harmonic (digit-shift invariant), and the resolution ceiling blocks any affordable universal
  resolution.
- **SZB-05 — the remaining discriminator:** every available route (seed-uniform transport, angular
  period, entropy/within-cell) is seed-blind or gate-equivalent; a sufficient route must be
  genuinely seed-specific — sensitive to the completed point via the exact `U_0=0` boundary and
  diagonal rationality.

## Files

- `PROOFS.md` — the five results and their boundaries.
- `CLAIMS.md` — the scoped claim ledger (prefix `SZB`, local only).
- `probe.py` — self-contained three-front probe (stdlib + mpmath/numpy; run WITHOUT `python -I`).
- `COMBINED_LOG.txt` — captured probe output (the receipts).
- `test_selected_zero_boundary.py` — exact/finite regression for SZB-01..04.
- `VALIDATION.md` — how it was checked.

## Firewall

Base-16/base-3 π normality, the signed Weyl gate `∀h≠0: S_N(h)=o(N)`, RH, Weil positivity, general
Collatz, and shifted Lonely Runner n=18..94 remain **OPEN**. Nothing here is a Lean theorem or an
externally reviewed result; finite experiments do not prove all-horizon limits.
