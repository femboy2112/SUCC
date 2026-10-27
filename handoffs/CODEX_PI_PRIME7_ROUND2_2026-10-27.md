# CODEX handoff: prime-7 mirror / Gaussian descent, second round

**Research verdict:** π normality remains OPEN. The round proves new
source-arithmetic theorems and a stronger counterexample to prescribed
moving conditional-energy gates. No source rewrite, main merge, release,
or inherited proof-status promotion is authorized or performed.

Actual parent is #327 at `76f3799658fde8a2eff649b0bd4926a2173918d0`.
Own child branch: `research/pi-prime7-mirror-source-descent-2026-10-27`.
#325 (`95ee2f1fab851afe1517d8ec5a0589885842426f`) and Claude's #326
(`681f79cc1f045bef7cf2aa9e2b20ba1e9f7f27b2`) were read-only context.
No shared worktree writes, integration commits, or sibling merges occurred.
The final live check also found and audited the two-bit sibling
`91d908b775241df6a7f91e9de843c88e6774e0c9`, announced on #325. Its original
ten tests and source probe were rerun unchanged in an isolated namespace.

Start with [the synthesis](../research/2026-10-27/PI_PRIME7_ROUND2_SYNTHESIS.md),
[claim ledger](../docs/CLAIM_SUPPLEMENT_PRIME7_ROUND2.md), and
[validation](../research/2026-10-27/PI_PRIME7_ROUND2_VALIDATION.md).

## Earned results to preserve

1. **Proper conditional-energy obstruction.** For every fixed prime p≥7
   and prescribed q(N)=p^{L(N)}→∞,q=o(N), there is one normal α with μ≤4
   and, along N=2^j for every fixed h≠0, C_A liminf≥1/4 and both proper
   Haar H_A and empirical conditional Q_A liminf≥p/[8(p+1)]. This uses
   an augmented common word selection, not a separate α for each norm or
   frequency. The same-forcing changed-selector corollary is explicit.
2. **Full-source delay reconstruction.** At 7 and 11, two consecutive
   projective source samples have exactly one unordered off-diagonal
   pair at every depth; three samples are an isometric embedding. At 241
   two suffice. Exact one-source critical collision counts are also proved.
   Energy consequently returns to E, exactly or with O(1/q) signed error.
3. **Actual modular source cancellation.** At q=7^L,L≥2, complete sums
   over D-unit inputs are ≤2√q, and the regular numerator-mirror sum is
   zero. Its A-energy is nevertheless exactly 2/7. Every excluded pole
   disk, conductor and character convention is specified.
4. **Gaussian descent and real-phase obstruction.** The natural orbit
   stays in one rational odometer leaf. Odd/even finite descent differs.
   Arbitrary finite-clock observables have uniform real-phase error
   >47/39168, at every depth and nonzero integer h. This is not an
   empirical-L² bound or a zero-selector advantage.
5. **Denominator resolution.** Exact joint-(A,D) identities classify
   generic collisions and the observation exceptions 109,251; unit
   shifted numerator observations resolve time immediately. These
   exceptional primes are not additional bad-reduction primes of r.
6. **Fresh two-bit extension.** Any deterministic residue partition with
   positive limiting label fraction κ has the same proper-energy
   obstruction κ/4. For partial (A,sheet,pole), this is 7/32 at prime 7;
   the complete code returns E exactly. Every autonomous quotient
   retaining A is injective. The partial code has exact order-two finite
   Markov behavior and zero entropy rate despite positive one-step
   conditional entropy. See [the proof](../research/2026-10-27/PI_TWO_BIT_PARTITION_MEMORY_OBSTRUCTION.md).

## Audit safeguards

- The local analytic lemma requires integral Taylor coefficients in the
  chosen coordinate. Unit derivative alone for an unrestricted analytic
  function is insufficient; x−x^p/p^{p−1} on pZ_p is a counterexample.
- Preserve the distinction between affine input time and all P¹ input
  points: source counts at p=241,L=1 are 497 versus 500 respectively.
- Haar weights are m_a/q, and empirical weights are c_a/N. Correcting
  these weights changes the norm but does not remove the new obstruction.
- “Same α” refers to the augmented intersection of all good-word events.
  Its proof does not assert that a previously fixed lexicographic choice
  happens to satisfy the added events.
- L≥2 is essential to exact modular mirror vanishing and energy 2/7.
- The O(1/q) joint-(A,D) energy comparison is not valid at 109/251.
- Exact scalar-label refinement is monotone at every N. Joint labels can
  have a different branching count, so the same formula cannot be copied.
- Irrationality exponent ≤4 does not mean a uniform C/q^4 lower bound.
- All internal audits used the same model family. Their agreement is
  not external mathematical validation. No new Lean theorem is claimed.

## Failed hypotheses and next verdict-changing obligation

Certified authentic sums have both signs for C_A−E. Full-source delay
information reconstructs time, and modular cancellation omits a real
cofactor which can undo it. Extra Gaussian states are not extra natural-time
observations. These are specific failures with proofs or exact receipts,
not a generic claim that arithmetic methods cannot work.

The next proof must control the signed real complementary phase for the
original rational U_n and use U_0=0 in an estimate which fails for changed
selectors. Any proposed arithmetic Fourier expansion must bound its error,
coefficient norm, frequency range and conductor together; a small local
factor alone is insufficient. A sufficient energy gate is still possible
at π, but it must be proved rather than inferred from normality, finite
type, fiber geometry, or conditional Haar normalization.

The inherited nonzero-boundary result, zero-seam obstruction, nonlinear
lag saturation and finite-mode countermodels remain active. This round
does not improve the selected real Fourier order from #319.

For integration: review the additive papers, probes and tests as research.
Do not promote a normality claim, replace the source, or modify historical
archives. Root alone publishes this child branch; Claude's integration
branch remains independent.
