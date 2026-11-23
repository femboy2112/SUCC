# OPERATION IROH — Dirichlet-GRH prime spectrum ↔ authentic π BBP observer

**23 November 2026. ADDITIVE RESEARCH DRAFT.** Stacked after SUCC #687 (FUCC/RH human-readable spine) and #686 (π analytic/symbolic no-go), ultimately Main XXVI `81be6b897ae980b801a3b9de9e22ef81e8360bfb`.

## Outcome

**New-to-SUCC exact bridge:** The unmodified four-pole BBP zero-seeded endpoint `x=π/16` equals `L(1,χ₄)/4`. A genuine prime-power character twist of SUCC/FUCC's source dilation commutator has a finite vacuum matrix coefficient `Sχ(X)` such that `exp(Sχ(X))/4 → x`. Assuming the **Dirichlet-GRH for χ₄** furnished by the externally Lean-verified Alpöge–Claude argument, the error is `O(X^(-1/2) log X)`. Choosing `X_B=16^(4B) B^6` transfers every fixed-mode late-shell Weyl mean to this second, prime-defined observer with error `O_h(B^-2)`.

The same research also transports the external `μ(π)=2` theorem into a lower bound on the **reduced denominators of the exact original BBP rational prefixes**, `q_n>(64n²16^n)^(1/(2+ε))` eventually. This is a genuinely source-derived *representation, error and Diophantine-shadow packet*, **not a signed Weyl saving**. Its prime-product approximation is computationally vastly more expensive than the BBP recurrence and does not prove R0 or normality. See [THEOREMS.md](THEOREMS.md), the primary-source [π exponent-two proof transport](PI_MU2_PROOF_TRANSPORT.md), and [NEXT.md](NEXT.md).

## Why the new source matters

The user's "primes as spectral data" intuition becomes an exact statement, not a randomness assumption. Distinguish:

1. `χ₄`-twisted *prime-power spectrum* `Sχ(X)` and its GRH-controlled limit;
2. smooth *BBP source-time* generating series and zero-seeded rational history;
3. *real-circle* radix-16 temporal Weyl phases.

The theorem constructs a common endpoint and quantitative transport (1) → (3) and (2) → (3). **Neither transport supplies temporal independence.** In particular primes of the special form `8n−7` occupy only `O(B/log B)` of the `B` source clocks on `[B,2B)`; prime-slot marginals alone cannot force a positive proportion of nonlocked clocks without an exact mechanism propagating information through the integer-carry/cofactor history.

## External dependencies and authority

- **AUTHENTIC SUCC SOURCE:** [`docs/PI_NORMALITY_FRONTIER.md`](../../../docs/PI_NORMALITY_FRONTIER.md), [`docs/MAIN_XXVI_HANDOFF.md`](../../../docs/MAIN_XXVI_HANDOFF.md), and the unchanged four-pole `U₀=0` data; #686 and #687 are stacked draft ancestors.
- **CLASSICAL:** Dirichlet beta identity `L(1,χ₄)=π/4`; character Euler product for `Re s>1`; von Mangoldt logarithmic derivative; Abel partial summation; classical implication `GRH(χ₄) ⇒ ψχ(t)=O(√t log²(4t))`.
- **EXTERNALLY VERIFIED, NOT REBUILT HERE:** Alpöge–Claude RH / Dirichlet GRH Lean proof: [official Lean community statement (2026-11-21)](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), [M. Rubinstein's checker](https://mrubinst.github.io/grh-lean-verification/), [working exposition v2 (2026-11-22)](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf). The prose guide's difficult inequality (M) remains imported from the Lean development.
- **SEPARATE EXTERNAL π DIOPHANTINE CLAIM:** [OpenAI, *The irrationality exponent of π is 2* (2026-09-24)](https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026), [Lean scope](https://github.com/openai/math/blob/main/lean/docs/017.md), [main formal theorem](https://github.com/openai/math/blob/main/lean/OAI/NumberTheory/PiExponent/Main.lean). No claim of a local Lean rebuild or specialist referee. #686 already proves via generalized Kempner that even `μ=2` does not imply R0.

## Validation

`python -m unittest discover -s research/2026-11-23/iroh_prime_beta_bridge -p 'test_prime_beta_bridge.py' -v` tests the finite arithmetic source via two distinct exact algorithms, rejects fake composite `6` and `1/k`/character-sign mutations, checks original BBP Mellin identity and literal-zero recurrence, and verifies finite prime-to-orbit Jacobian rank-one minors. **8/8 focused tests passed** on the locally authored test file before the remote PR upload. This is not a run of the full SUCC AGENTS gates, nor any proof assistant, and not a test of GRH or infinite asymptotics.

**Review only. No merge, source modification, status promotion, tag, or release.**
