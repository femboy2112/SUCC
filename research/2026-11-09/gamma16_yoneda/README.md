# Operation Γ16: a BBP source-twisted 16×16 matrix with a literal q-Gamma blocking law

**2026-11-09 | Research-only | π base-16 normality OPEN**

Starting from draft #565 at `35a664c19e91ab5bd11678c82566ce88336e0309`, this branch adds only a new module, root-discovered tests and this research directory. Original source `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, literal `U0=0`, source contracts, imported provenance, Lean and main are untouched.

## What the 16×16 is

1. `M_ab` is the **actual zero-seed π two-hex-digit empirical transition law**. Its Haar reference is `J/256`. The group DFT `F16` is a true 16-dimensional linear operator; `16 F M F^T` exposes the 256 two-digit character correlations and SUCC's primitive order 1/2/4/8/16 sectors.
2. Averaging simultaneous digit translations is an exact orthogonal projector, so the non-Haar energy splits into two **separate** sources of discrepancy: basis-locking and relative-digit resonance. Both are generally present.
3. The **full carrier Yoneda-shaped object** is NOT just 256 probabilities. A 16×16 matrix of measures on the entire future tail is needed. It has an explicit inverse to the original circle law. The de Bruijn(16,2) countermodel has a precisely Haar scalar 16×16 matrix but is periodic and has E3=15.
4. The true original radix blocking `U_(2k)=256 U_(2k−2)+16r(2k−1)+r(2k)` induces a positive Laplace density transform `Q_2(x)=(16+e^(−8x)) Q(x)` with simple endpoint-zero amplitude 255, preserving Gamma(2) rank. At arbitrary fixed block depth g, `Q_g(x)=Q(x)*B_g(e^(−8x))`, `B_g(t)=sum_(j<g)16^(g−1−j)t^j`. It composes exactly under further blocking and has the *literal classical q-Gamma quotient* representation `B_g(e^(−8x))=16^(g−1) Gamma_q(g+1)/Gamma_q(g)`, `q=e^(−8x)/16`. [DLMF §5.18.7](https://dlmf.nist.gov/5.18.E7).
5. The old #564 source-twisted floor Fourier formula lifts to an **exact two-frequency matrix lattice** `m+16ℓ`, with explicit source phases, finite Fejér truncation and named moving-boundary error. No old π normality gate is silently solved.

## Finite observed result (reused source data, not a new holdout)

- **N=40,960** source-certified fractional hexadecimal digits of π (reuse #561/#565, verified SHA-256).
- 16×16 exact pair counts range **129 to 189**, with Haar reference **160** per cell.
- `E2=981/163840≈0.00598755`; `E_basis=284071/52428800≈0.00541822` (**90.49%**); `E_relative=29849/52428800≈0.000569324` (**9.51%**).
- *Source clock and integer time matter:* radix-256 samples in two staggered frames have different finite energies; their mean equals all-start pair energy plus an explicitly accounted nonnegative frame-energy term.
- Original three-channel prime-birth clocks from #554 cut the real epoch into four source-labelled stages. They obey exact positive between-stage variance decomposition, but the identity holds for every partition and does not itself supply real complementary-phase cancellation.
- 25 new focused exact tests (plus independent NumPy FFT / SymPy endpoint-jet oracle), 16 shuffled same-count controls, periodic and de Bruijn controls. All input data, counts, proof and test scopes are declared.

## Interpretation and status

**Disclosed/proved within the finite algebra and declared classical imports:** 16×16 Fourier change of basis, orthogonal translation twirl, full-tail measure reconstruction, exact q-Gamma blocking, BBP original-source two-frequency lattice, finite count receipts and countermodels.

**Unproved:** any source-selected all-epoch bound on `E_basis`, `E_relative`, moving-boundary occupation or the full-tail conditional first-digit Fourier pins. Their joint vanishing at two-digit level alone still fails to imply normality. The **correct all-depth** asymptotic gate is the inherited #565 conditional Haar symmetry defect or equivalently #544's selected signed covariance, still OPEN.

Figures: [observed 16×16 counts](pair_counts_16x16.png) and [joint Fourier-mode magnitudes](fourier_modes_16x16.png). Each uses reused certified data, not a new oracle.

Read [THEOREMS.md](THEOREMS.md) for full quantifiers/proofs/anti-results; [CLAIM_LEDGER.md](CLAIM_LEDGER.md) for statuses; [NEXT.md](NEXT.md) for discriminating probes; [VALIDATION.md](VALIDATION.md) for commands and limits.
