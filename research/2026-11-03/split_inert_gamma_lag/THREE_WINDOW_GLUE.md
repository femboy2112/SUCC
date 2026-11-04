# GL-09 — Three-window deterministic gluing into the dyadic π-normality gate

**2026-11-03, additive research corollary of the source prime windows in draft PR #485.** This is a proved deterministic reduction, NOT proof of the original source-specific near-pair saving. The original BBP source and literal U0=0 are untouched. Every `E=o(log m)` assertion below is explicitly CONDITIONAL.

## Exact covering algorithm

Let A≥1 be an integer, m≥2 a common integer mesh, and recursively set

`B0=A`, `B_(j+1)=ceil(4 B_j/3)` for j=0,1,2.

Then `B3≥(4/3)^3 A > 2A`. Consequently the three adjacent intervals

`I_j=[B_j,min(B_(j+1),2A)) ∩ Z`, j=0,1,2,

partition the original dyadic (or arbitrary integer) epoch `[A,2A)` exactly. Each lies in the FULL original split/inert source-prime passport window

`J_j=[B_j,ceil(4 B_j/3)) ∩ Z`

proved in GL-05/GL-06, since that theorem holds for all sufficiently large INTEGER bases B, not only dyadic B. This is why the clipped inert prime clocks can still cover the full dyadic epoch without inventing an invalid [k,2k) inert window.

## An exact universal three-window inequality

For each full J_j let

`P_j(m)=#{(n,t)∈J_j×J_j : m||U_n-U_t||_(R/Z) ≤ 1}`

with diagonals and ordered pairs included, ORIGINAL real selected source states and zero seed. Let v^(j) be the m-bin histogram for the truncated I_j, and v=v^(0)+v^(1)+v^(2) the full `[A,2A)` m-bin histogram. Every same-bin ordered pair has circle distance <1/m, so

`||v^(j)||_2² ≤ P_j(m)`.

By the triangle inequality in ℓ² and Cauchy–Schwarz,

`||v||_2 ≤ Σ_j sqrt(P_j(m))`,

`E_(A,m)=(m/A²)||v||_2² ≤ (m/A²)(Σ_j sqrt(P_j(m)))² ≤ (3m/A²)Σ_j P_j(m)`.     (GL-11)

This is an EXACT finite inequality for every integer A,m. It uses no density assumptions, Gaussian prime class averages, or asymptotic source assertions. Note that the P_j cover full clean source windows and may include indices beyond 2A; this only makes the bound larger and still valid.

## Explicit conditional implication to PR #476

Let A=2^q→∞, choose the inherited explicit mesh `m_A=max(2,2^floor(log2 q))` (m_A≈log A), and the three B_j(A) above. If the ORIGINAL source-selected real near-pair counts satisfy

`max_(j=0,1,2) P_(B_j(A),m_A) = o(A² log(m_A)/m_A)`

for EVERY sufficiently large dyadic A, then GL-11 gives `E_(A,m_A)=o(log m_A)`. Parent #476's already-proved conditional Fejér/radix Ward theorem then yields base-16 π normality. The source-selected near-pair premise in this statement is STILL OPEN; no such bound was proved by GL-05 (exact phase nonrepeat) or GL-06 (Galois-averaged kernel).

If instead one can prove a B-uniform near-pair inequality on EVERY original clean split/inert J_B at all logarithmic meshes comparable to log B, it supplies the displayed three B_j bound and hence the full dyadic criterion (the mesh m_A is comparable to log B_j). An estimate only for one specific subwindow or only on a sequence of B would not suffice without an additional covering argument.

## Exact finite cover check

For A=96: B=(96,128,171,228), clipped intervals `[96,128)`, `[128,171)`, `[171,192)` partition `[96,192)`. For A=192: B=(192,256,342,456), clipped intervals `[192,256)`, `[256,342)`, `[342,384)` partition `[192,384)`. Source residues were not recalculated here; this checks only the deterministic geometry. Same check executed for A=8,384,768,8192.

**Proof debt:** derive the genuine selected Archimedean cofactor/carry signed or near-pair saving on all these short source intervals. No local p exact nonalias or ensemble Ramanujan factor can be inserted in place of that estimate. The positive number theory result is the simultaneous authentic prime-cover geometry; the remaining quantitative real-circle hypothesis is UNVERIFIED.
