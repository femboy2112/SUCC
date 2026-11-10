# Operation Lambert-W × Entropy Amplification — source-locked π research

**Research branch, 2026-11-08. π normality OPEN.** The full four-pole BBP source, U0=0, integer carries, source manifests and historical proofs are unchanged. Stacked on #559 at `44a4a96d2180a66524f882e4a1d50309fc8c97a9`; protocol was committed **before the newly generated 40,960-digit source prefix**, at `c207e377143818f95ec12957849834e1d3113661`.

## Result

The central **finite deterministic specialization of SUCC's earlier strong Piatetski–Shapiro and trimmed-entropy machinery** is

\[
\boxed{\lfloor k/t\rfloor\,D_{KL}(p_t\Vert u_t)\le\log(1+E_k(N))},\qquad 1\le t\le k\le N,
\]

for cyclic hexadecimal word counts. Thus a persistent fixed-length word bias forces collision-entropy deficit growing *linearly* with observation depth. If the **original selected zero-seeded** BBP path satisfies `log(1+E_(k_W(N))(N))=o(log N)` at all large N, or at relative-gap-dense checkpoints, its digits must be base-16 normal. Equivalently, an all-N `D_(kW)(N)≤N^(1+o(1))` or all-N `max count_(kW)(w)≤N^o(1)` would suffice. **Those original-source hypotheses are still OPEN.** They are substantially less demanding than `D=O(N)`, but are not consequences of Parseval, coverage or the previous signed-covariance reductions.

The Lambert-W clock is the inverse independent-coupon **full word coverage** benchmark, not an intrinsic dynamical law: `B=16^k`, `E T_B=B H_B=B(log B+γ)+1/2+o(1)`, and `k_cont=(W(e^γN)−γ)/log16`. The idealized missing-coupon expectation at its threshold tends to `e^(−γ)`. These are classical reference results; the actual π stream consists of **overlapping deterministic words**.

The **new exact source experiment** certifies the first **40,960** hex digits from the unchanged BBP formula in a single outward rational integer interval (no π digit oracle). The previous first 16,384 per-step certificate matches byte-for-byte. At N=40,960, all 4096 depth-3 words have appeared, `D3=40850`, `D3/N≈0.997314`, `E3=817/8192`, and the exact off-diagonal signed collision term is **−50**. The actual first chronological 4096-type coverage occurs at digit **31,816**; the independent-coupon mean for coverage is about 36,434.35. The source lies within the observed range of 16 fixed-seed same-histogram shuffle controls. No all-time conclusion follows.

An exact cyclic **trimmed** extension retains original time labels and allows rare high-density hotspots to be discarded at a provably small density; the authentic BBP asymptotic trimmed estimate remains unproved.

**Decisive negative control:** base-16 normal sequences can contain sparse giant zero blocks; those produce superdiffusive moving-depth energy despite normality. The W-energy condition is *strictly stronger* than normality. Do not confuse it with a necessary anti-clumping law.

## Read and reproduce

- [THEOREMS.md](THEOREMS.md): LWE-01…LWE-09 exact derivations, scope, normal-but-spiky counterexample.
- [PROTOCOL.md](PROTOCOL.md): precommitted analysis/holdout plan, with no post-holdout threshold fitting.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): status, controls and pending theorem debt.
- [COUNTERMODELS.md](COUNTERMODELS.md): source-blind failures, normal sparse spike and depth staircase.
- [VALIDATION.md](VALIDATION.md): actual commands, exact hash receipts, incomplete validation gaps.
- [NEXT.md](NEXT.md): path to an original-zero microscopic occupancy bound and signed #544 covariance coupling.
- [experiment.py](experiment.py): source-checked heldout epoch and signed lag diagnostics.
- [bbp_bulk_certificate.py](bbp_bulk_certificate.py): efficient original-source exact integer interval generator.
- [FINITE_RECEIPT_40960.json](FINITE_RECEIPT_40960.json): actual finite counters and controls.
- [CERTIFIED_HEX_40960.txt](CERTIFIED_HEX_40960.txt): authenticated digit prefix, not proof input to normality.
- `observational_succ/lambert_entropy_forge.py`: reusable deterministic instruments; `tests/test_lambert_entropy_forge.py`: hostile regression checks.

**Key boundary:** entropy amplification makes normality *easy after a strong enough microscopic collision/occupation estimate*. It does not pay that arithmetic estimate for the source-selected BBP orbit. Normality of π remains OPEN.
