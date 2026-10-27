# Astra next: actual signed arithmetic cancellation from coherence-group checkpoints

**Source pin:** PR #313 commit `79344c62c39c96755b742700b3d4d22fa60d86da`; follow-up Seinfeld selection+memory branch. Start with the full [coherence-group dossier](../research/2026-10-26/SEINFELD_COHERENCE_GROUPS.md), [current selected branch synthesis](../research/2026-10-26/SELECTED_BRANCH_SYNTHESIS.md), and the ordinary SUCC `AGENTS.md` discipline. Do not claim or imply a proof of π normality.

## Precise author intuition

The author sees one underlying operation across apparently different carriers. Their current strongest proposal: **do not naively enumerate all virtual paths; identify equivalence classes/coherence groups within which finite source-respecting integration/realization can be performed exactly.** Keep the entire well-ordered chain of working probability fields as memory checkpoints. Evaluation of a reference average can equal zero while nonzero signed source-labelled information survives inside its fibers. Work backward to the reference using explicit likelihood ratios, not by pretending a chosen history is uniformly sampled. Source selection is a read; independently specified reinforcement is a write. Neither is a quantum-measurement claim.

## New exact results on this branch

- Finite path disintegration plus signed group amplitudes is exact; no saving.
- `D(selected||reference)` splits exactly into the KL cost of the group and the unresolved conditional fiber. Uniform 16^N reference and prefix t selected memory: `N log 16 = t log 16 + (N-t) log 16`.
- **Minimal phase-preserving coherence groups:** a frequency h on C16 factors through modulus `16/gcd(16,h)`; parity aliases the quarter-turn. One mode's correct quotient may be inadequate for another.
- **Future-stability gate:** an exact group quotient of a transition kernel exists iff it is strongly lumpable; tests include a false quotient. Source-indexed, nonautonomous transitions require the corresponding typed generalization.
- **Global vs working Fourier energy:** on a fixed reference, finer checkpoint conditional projection can only INCREASE accessible L² energy. The increment is the squared checkpoint martingale difference. It says nothing about source-selected cancellation.
- **Hostile Pólya memory law:** 16-color reinforced paths have zero unconditional Fourier mean yet mean-square selected coherence approaching `1/17`; every likelihood update is exactly normalized relative to Haar.
- The real original-source parity checkpoints use the native `lambda_source_duality.original_history` and exact `branch_defect` table. Their working energy is measured, not proved to vanish.

## The research objective

Build a source-authenticated quotient/graded-coherence-group architecture for the **authentic zero-seed four-pole BBP recurrence** that (i) retains the original selected path, complex characters, real-circle digit/remainder and integer carry, (ii) compresses histories as operations and values, and (iii) **proves a new signed estimate**, not merely a factorization of the selected Weyl sum.

The current sufficient instrument from PR #313 is the signed carry/arrival mean

$$\widetilde C_{N,M}(h)=\frac1N\sum_{n=1}^N\exp\left(\frac{2\pi ih(c_{n+1}+(b_n+1/2)/M)}{16}\right),\quad b_n=\lfloor M\{U_{n+1}\}\rfloor.$$

Its distance from `N^-1 sum exp(2πih U_n)` is `≤ π|h|/(16M)+(π|h|/(8N))Σ r(n+1)`. Prove this signed mean tends to zero for every fixed nonzero h at one preset growth schedule M_N, or establish a genuinely new source-specific intermediate lemma stronger than PR #311's `N-(1/29) log_8 N` absolute-loss order.

## Mathematical challenges to actually solve

1. Try **time-dependent lumpability**: classify state histories so source update induces exact coherent group transport. Do not assume parity/phase equivalence is dynamically sufficient.
2. Try a **signed quotient operator** on class amplitudes, not on positive class masses. Determine whether a source-authentic quantitative spectral/anti-concentration estimate on the selected grouped operator exists. Exact permutations of odd-denominator torsion admit no generic mean-zero spectral contraction.
3. Test grouping by Gaussian signed four-step holonomy, Oily–Macaroni primitive grade, literal integer carry, prime source conductor and future remainder **jointly**, keeping zero seed. Beware the conditioning-at-full-conductor energy saturation on PR #313 and the matched-moment/sparse changed-seed controls.
4. Instead of insisting each conditional energy vanish, test **cross-group signed cancellation**—the real arithmetic vector sum may cancel even when working conditional energy is large.
5. Search for phase-sufficient groupings with provable *future source stability* and sublinear effective class count. Derive an explicit non-tautological gap between authenticated path laws and a coherent nonnormal control.
6. Steelman/Falsify/Conclude every proposal. An exactly commuting diagram, KL chain rule, martingale isometry or finite group decomposition is not a normality proof.

## Validation, integration and permission boundaries

Preserve raw original source and imported snapshots; additive child research branches/draft PRs only, **no merge to main** without maintainer authorization. Run focused tests and source hash receipt, then all mandatory provenance/full Python/observer/ordinal checks on combined source. Pinned Lean proof authority for actual finite claims only. No CI pass until it actually reports success. Commit and push one coherent update with exact source/test hashes, rigorous proofs, adversarial controls, and the *actual* remaining selected Fourier bound. If genuine π normality proof emerges, demand detailed independent hostile audit of every quantifier before announcement.

**Ultimate target:** for all fixed h≠0, `N^-1 Σ_{n≤N} exp(2πihU_n)→0` for authentic `U_0=0, U_{n+1}=16U_n+r(n+1)`. No claim in this branch proves it.
