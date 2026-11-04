# Next discriminating probe — pay the high-frequency input RENORM-2 isolates

RENORM-2 proves that single-frequency ×16 transport is self-referential: it reduces the SC-8
low band to an equal-size high band near `|h|≈A^{3/2}` with `o(1)` budget. So the entire proof
debt is now a **high-frequency signed estimate**, not a low-frequency one. Concrete next steps:

1. **Second-moment over the transported high band.** Target
   `Σ_{A^{3/2}≤|h|<2A^{3/2}} |c_A(h)|² = o(K_A)` using the authentic split/inert prime clocks
   (#485 range `|h|≤A` must be *extended* to `|h|≈A^{3/2}` — check whether the passport nonalias
   survives, or quantify where it breaks). This is where RENORM-2 says the real cancellation
   must live; a Galois average is still not a source bound.
2. **Pay the forcing cross-term, don't drop it.** RT-1's `ε_A(h)` carries the signed factor
   `e(16hU_{n-1})(e(hr(n))-1)`. Its *signed* sum (not the triangle bound) may cancel; measure
   `Σ_n e(16hU_{n-1})(e(hr(n))-1)` directly and seek a source-derived saving below `2π|h|Σr(n)`.
3. **Predeclared falsifiers.** Any proposed high-band bound must FAIL for: the `x=1/5` fixed
   point (c_A(h)=e(h/5), modulus 1 ∀h — no decay), the counterseed `s*=−π/16` (Main XIX), and a
   same-forcing changed seed. If a candidate passes all three, it is source-blind and wrong.
4. **Held-out & two oracles.** Extend `HELDOUT_A` to fresh epochs; keep the odd-conductor blind
   source and add an interval-arithmetic `c_A(h)` oracle before trusting any near-threshold number.
5. **Decision gate.** A proved `o(K_A)` high-band bound on an unbounded A-family, or a decisive
   counterexample to the best candidate with its corpse retained. **π normality stays OPEN until
   then; do not report a rearranged equivalent as progress.**
