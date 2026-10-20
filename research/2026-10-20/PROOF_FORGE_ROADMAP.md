# Proof Forge roadmap — organized by proof capability, not subproject count

**Date:** 2026-10-20. Each level has an explicit completion criterion and at least one established theorem
as benchmark. Levels gate: do not claim a higher level until the lower one's benchmark is actually met.

## Level 1 — exact elementary arithmetic & source identities  — **STATUS: MET**
- **Benchmark:** exact additive/Dirichlet convolution identities; the von Mangoldt convolution distinction.
- **Completion criterion:** both convolutions constructed exactly; the illegal interchange refuted with an
  exact witness. ✅ `arithmetic_interactions.py`, witness `N=5`, BS-G3 corrected.

## Level 2 — polynomial abc / Mason–Stothers  — **STATUS: MET**
- **Benchmark:** Mason–Stothers over a char-0 field.
- **Completion criterion:** complete proof + exact certificate + char-p counterexample + honest Lean core +
  two independent verification routes. ✅ `mason_stothers.py`, `MasonStothersDegreeDescent.lean`, 380-triple
  oracle, 0 violations. CLASSICAL.
- **Next within-level:** discharge the Lean polynomial-lemma debt against a pinned mathlib project; extend
  the certificate to the function-field / higher-genus Mason theorem and to `K[x,y]`.

## Level 3 — uniform prime-power & additive-correlation estimates  — **STATUS: PARTIAL**
- **Benchmark (reach):** the Bernert–Browning–Lichtman–Teräväinen abc exceptional-set exponent `3/5+ε`
  (arXiv 2410.12234).
- **Have:** the elementary ris-moment bound `S_t(X) ≤ M(t)M(2t)X²` for `t<1/2` (#196, PROVED LOCAL),
  re-derived and confirmed here; strictly inferior to BBLT. The `t<1/2` ceiling is a Cauchy–Schwarz method
  limit, not a growth threshold.
- **Completion criterion:** either reach `t ∈ [1/2,1)` with a new (sieve/large-sieve/Fourier) input, or a
  rigorous no-go explaining why the SUCC moment method cannot. The honest proof-obligation ladder toward
  BBLT (exceptional-set indicator → large-sieve → determinant method) is in `ABC_MOMENT_REDERIVATION.md`.

## Level 4 — deep analytic arithmetic (Dirichlet characters, sieve, L-functions)  — **STATUS: NOT STARTED**
- **Benchmark:** a genuine circle-method lemma for `R_Λ(N) = Σ_{a+b=N} Λ(a)Λ(b)` with major/minor-arc
  separation and prime-support certification (Goldbach-shaped), recovering an established analytic result.
- **Completion criterion:** a reconstructed classical theorem (e.g. Vinogradov-type minor-arc bound) under a
  strict source contract, with the additive Fourier carrier `F_N(θ)^2` (not the `|F_N|²` difference
  shortcut). Foundation laid: BS-G1/G2/G4 + the corrected BS-G3 + `arithmetic_interactions`.

## Level 5 — authentic signed-Weil source inequalities (RH lane)  — **STATUS: OPEN, TIGHTLY GOVERNED**
- **Benchmark:** the signed Suzuki first-window `S₄ = A₄ − R₄` sign.
- **Completion criterion:** a certified source→signed-Weil morphism on a declared test space with correct
  Γ/pole/conductor/half-density, true prime-power weights, and positivity of the *actual indefinite* form —
  not an auxiliary positive Gram. **STATUS: AMBIGUOUS/OPEN** (#195 is a firewall scaffold with no path to
  `identified:True`). The #181/#182 inverse estimates are alternatives, never summed.

## Final applications — RH, integer abc, Goldbach — **ALL OPEN**
- Integer abc: the Wronskian/size-drop mechanism has no archimedean integer counterpart
  (`integer_transfer_obstruction`). RH: no positive Gram is the signed Weil form; no zeta-zero is a
  construction input. Goldbach: binary Goldbach not asserted; the target is intermediate quantitative lemmas.

**Principle.** Every important construction must produce a proof, a useful invariant, a genuine
counterexample, or a sharply stated missing obligation. Demonstrated on established mathematics (Levels 1–2),
limits calibrated (Level 3), the rest named honestly as open.
