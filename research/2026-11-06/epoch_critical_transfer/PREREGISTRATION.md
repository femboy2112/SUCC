# Preregistration — epoch-critical Fejér Hilbert transport

Date 2026-11-06; source parent #536 exact head e463a191d82355c707662bdbfb4bf2150fdd4eb7. This is original four-pole BBP, literal U0=0, strictly add-only research.

## Mathematical hypotheses, fixed BEFORE new finite probes
1. For I_A=[A,2A) and original rational BBP x_n={U_n}, completed z_n={U_n+T_n}, the known source tail bound T_n<1/[15(n+1)^2] yields a NEW unconditional epoch Hilbert transport:
   |sqrt(C_(A,H)(z))-sqrt(C_(A,H)(x))| <= [pi/(15 A^2)] sqrt(H(H+1)(H+2)/6),
   using averaged tail <=1/(30 A^2) and exact Fejér h² weight sum. At H=A this is O(A^-1/2), rather than the O(1) critical-prefix norm loss of parent CC1.
2. For the pure completed ×16 orbit, the exact epoch ray |W_I(16h)-W_I(h)|<=2/A, so for J=floor(log_16((A+1)/(2|h|)))>=0,
   |W_I(h)| <= sqrt((C_(A,A)(z)-1)/(J+1))+2J/A.
   If C_(A,A)(x)=o(log A) for every A→∞, normality follows, via dyadic decomposition of arbitrary prefixes. This premise is OPEN.
3. A relocation of #536 CC4 to epochs: if K>=2 and B_A(delta)=#ordered pairs (n,m in I_A with circle gap <=delta) <= A+K A² delta uniformly on [1/(A+1),1/2] for ALL large A, then C_(A,A)(x) <= 2K+4(A+1)/(3A), and π normality follows. This premise is OPEN.

## Fixed finite tests and controls
- Exact Fraction source through times 2A for A=16,32,64,128,256. Use Fourier diagnostics (float) for C_(A,A), exact pair counts for δ=1/(A+1) and δ=1/2 on A=16,32,64,128. Verify exact source and independent polynomial A(n)/D(n).
- Check ∑_{h}w_h h² = H(H+1)(H+2)/6 for H=1..128 exactly.
- Independently test the source tail average inequality from known rational bounds; phase reconstruction use at least 32 exact Fraction terms for T_n and rational remainder.
- Ghosts: constant x=0, pure periodic completed β=1/5, and rational H(n)=n/(2n−1)^4. All should violate o(log A) energy, showing compatibility alone does not create mixing.
- All finite numbers are diagnostics; no asymptotic normality or originality claimed. Parent source files, main, Lean, workflows and provenance immutable. Record failed tests and model limitations.

## Hostile criteria
A mismatch in the exact sum or a ratio exceeding the theorem bound refutes the lemma. If tests succeed but source epoch energies grow, report failure of proposed arithmetic savings; do NOT promote. Never infer all-horizon bounds from finite samples.
