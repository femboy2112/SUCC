# Next discriminating probe — pay the high-frequency input RENORM-2 isolates

RENORM-2 (corrected) proves that common-depth ×16 transport is self-referential: it injects the
SC-8 low band into a distinct high band up to `|h|≤A^{3/2}` (in fact any `16^jH=o(A²)`) with `o(1)`
budget. So the entire proof debt is now a **high-frequency signed estimate**, not a low-frequency
one.

**Routes this round proved are NOT shortcuts (obstructions, see `COUNTERMODELS.md`):**
- *Near-pair* `P_A(q_A)=o(A²K_A/q_A)` (AT1) reduces to — and loses a `K_A` factor against — the open
  Weyl bound `Σ_{A≤n<2A}e(hU_n)=o(A)`. Genuine `P_A(q)≈2A²/q` (equidistribution level), no saving.
  Also note `K_A=0` until `A≈e¹⁶`, so the criterion is only non-vacuous for enormous `A`.
- *Branch-current contraction* (AT2) requires finite-window digit-independence of π's hex expansion,
  which the recurrence does **not** supply (pure `×16` shift + `O(1/n²)`, no mixing/gap). Open, circular.

So the decisive probe is the **direct high-band exponential sum**, not a reformulation of it:

1. **Second-moment over the transported high band.** Target
   `Σ_{A^{3/2}≤|h|<2A^{3/2}} |c_A(h)|² = o(K_A)` using the authentic split/inert prime clocks
   (#485 range `|h|≤A` must be *extended* to `|h|≈A^{3/2}` — check whether the passport nonalias
   survives, or quantify where it breaks). This is where RENORM-2 says the real cancellation
   must live; a Galois average is still not a source bound.
2. **Pay the forcing cross-term, don't drop it.** RT-1's `ε_A(h)` carries the signed factor
   `e(16hU_{n-1})(e(hr(n))-1)`. Its *signed* sum (not the triangle bound) may cancel; measure
   `Σ_n e(16hU_{n-1})(e(hr(n))-1)` directly and seek a source-derived saving below `2π|h|Σr(n)`.
3. **Predeclared falsifiers.** Any proposed high-band bound must FAIL for the `x=1/5` fixed point
   (`c_A(h)=e(h/5)`, modulus 1 ∀h — no decay; the one true nonnormal contrast) and the counterseed
   `s*=−π/16` (Main XIX). **Do NOT use a rational changed seed as a falsifier:** for rational `s`,
   `frac(16ⁿs)` is a measure-preserving rotation (`16≡1 mod 3,5`), so `U_0=1/7` only rotates the
   orbit and cannot test normality (AT2). A candidate passing `1/5` and `s*` is source-blind and wrong.
4. **Held-out & two oracles.** Extend `HELDOUT_A` to fresh epochs; keep the odd-conductor blind
   source and add an interval-arithmetic `c_A(h)` oracle before trusting any near-threshold number.
5. **Decision gate.** A proved `o(K_A)` high-band bound on an unbounded A-family, or a decisive
   counterexample to the best candidate with its corpse retained. **π normality stays OPEN until
   then; do not report a rearranged equivalent as progress.**
