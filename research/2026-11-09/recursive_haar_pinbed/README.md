# Recursive Haar pin bed — from one conditional digit to all depths

**Research-only, 2026-11-09. π base-16 normality: OPEN.**

The user's proposed recursion can be made into an exact theorem: let T be the base16 shift and Q the operator that replaces the *first* digit by an independent uniform digit while **retaining the actual future tail**. For a T-stationary probability law, Q invariance implies and is implied by Haar. Uniform *unconditional* one-digit frequencies do not suffice.

[THEOREMS.md](THEOREMS.md) gives a fully explicit splitting `T_* C=id`, `C T_*=Q`, a sharp one-symmetry Wasserstein inequality, and the exact future-conditioned finite-word recursion. [CLAIM_LEDGER.md](CLAIM_LEDGER.md) distinguishes proved reductions, finite tests and the original zero-seed arithmetic debt. [NEXT.md](NEXT.md) specifies the prime-birth/carry/source-specific discriminator. [VALIDATION.md](VALIDATION.md) records actual executed tests.

RHY-10 identifies the exact finite signed moment where the recursion meets prime carry and real complementary slip; its source-selected decay is open. RHY-09 additionally proves the *literal grouped-forcing identity*: two consecutive base-16 BBP recurrence steps are exactly a single radix-256 step with forcing `16r(2k−1)+r(2k)`, retaining every original source pole and intermediate history. This source-anchored dynamical equivalence is not itself a measure-theoretic independence claim.

The authenticated source remains `U0=0`, `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`. Its completed path is the genuine ×16 circle orbit via the classical BBP identity. The new arithmetic claim is NOT that the source is already conditional-Haar: the required symmetry defect remains unproved. Same-forcing coherent counterseeds refute any seed-blind argument.

Implementation: `observational_succ/recursive_haar_pinbed.py` (exact `Fraction` laws, Wasserstein bounds, conditional digit counts), `tests/test_recursive_haar_pinbed.py` (21 focused tests), `FINITE_RECEIPT.json` and an exact, **reused** 40,960-digit source datum from sibling PR #561 (not a fresh data collection). No imported source, formal contracts, workflows or main are touched.
