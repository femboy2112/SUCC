# Claim supplement — selected branch transport and obstructions

**2026-10-26; scoped research, no new registry namespace.** SB-1–SB-10 are
local references only. Parent #312 is pinned at
`0c306a889f425418c29cbea3193205fb80c0575e`; inspected sibling #311 at
`a34c4484059e667202b97d5ab4102560987b1406` is not an ancestor of this
continuation. [Synthesis and full provenance](../research/2026-10-26/SELECTED_BRANCH_SYNTHESIS.md).
**π normality and selected sublinear cancellation: OPEN.** No scholarly
priority claim. No change to historical source artifacts or claims.

| Ref | Statement and domain | Authority | Boundary / adversary |
|---|---|---|---|
| SB-1 | Odd-torsion inverse uniqueness, failure of continuous extension; source-compatible finite affine permutations preserve norms | CLASSICAL / inherited SS-05–06; PAPER-PROVED application; finite LEAN KERNEL core | No selected-orbit mixing; a permutation is not the 16-predecessor Haar average. |
| SB-2 | For any probability law on the odd grid $D_Q$, $\Delta\ge16/\min(16,\lceil Q/M\rceil)-1$; authentic $M\ge Q_N$ gives $E(h)=1$, $\Delta=15$ | PAPER-PROVED; EXACT FINITE; Lean deterministic-row core only | All $N$, multiplicities allowed. Does not exclude slowly growing coarse partitions. |
| SB-3 | Authentic scaled spills force $L_a(k)$ zero carries; explicit packing bound $K_{N,a}\le B(N,a)$ and $B(N,a_N)=o(N)$ whenever $a_N=o(N^2)$ | PAPER-PROVED; EXACT FINITE | Holds every seed under this forcing; no zero-selector cancellation is inferred. |
| SB-4 | At $a=M=8N^2$, all $N$ authentic transitions spill and all remainder-bin labels change | PAPER-PROVED; EXACT FINITE; positive polynomial LEAN KERNEL | Sharp order of the vanishing spill-density allowance, not optimal constant or energy lower bound. |
| SB-5 | Changing $K$ labeled/bin records changes $E(h)$ by at most $4K/N$, $\Delta$ by at most $32K/N$; constants sharp | PAPER-PROVED; EXACT FINITE; finite parity-perspective LEAN KERNEL component | Bin changes must be counted. The full replacement theorem is not Lean-formalized. |
| SB-6 | Original branch and genuine carry/arrival energies differ by at most $4[B(N,1)+B(N,M)]/N$, full defects by $32[B(N,1)+B(N,M)]/N$ | PAPER-PROVED; EXACT FINITE | Difference tends to zero at prescribed subquadratic scales; neither energy is proved small. |
| SB-7 | Carry-translated endpoint primitive statistic satisfies $\widetilde E(8)=324\sum_b\widetilde p_b(\Phi_b-1/2)^2$; quarter-turn requires an additional opposite-pair term | PAPER-PROVED; EXACT FINITE | Native #311 scalar identity is credited; new quantitative edge uses SB-6. Parity balance permits quarter-turn energy $1/2$. |
| SB-8 | Same complete forcing, one changed fixed seed per finite band: finite-band means vanish while all conditional energies tend uniformly to one for $M\ge q$; sparse refinement also has exponent two and donor-level logarithmic absolute loss | PAPER-PROVED + CLASSICAL Diophantine input; EXACT FINITE interval controls | Zero seed and original state passport fail. Higher fixed mode survives. No all-mode cancellation counterexample. |
| SB-9 | Signed carry/arrival bin amplitude approximates actual Weyl mean with explicit $O_h(1/M+1/N)$ error for all $N,M$ | PAPER-PROVED; outward-rational EXACT FINITE | Continuous transport, not a new asymptotic saving. Formal group-algebra equality is never substituted for evaluated character equality. |
| SB-10 | Carry-conditioned energy decay or signed cross-bin cancellation at prescribed growing resolution implies normality through the authentic Green transport | CONDITIONAL implication; hypothesis OPEN | The arbitrary-slow-schedule equivalence is inherited from #312, not the breakthrough. |

**REFUTED shortcuts, with reusable receipts.** Exact-tail source restriction
inherits the real Haar transfer gap (SB-1/2); every quadratic bin scale has
vanishing record changes (SB-4); changing only digit labels pays for moving
bins (SB-5); marginal packet mass or parity balance supplies all branch
energies (SB-7); finite-band cancellation plus finite Diophantine type and
full forcing forces conditional energy decay (SB-8); positive conditional
energy retains all signed cross-bin cancellation (SB-9).

**LEAN KERNEL scope.** Ten exported finite declarations and four paired
controls were checked with the pinned Lean 4.14.0/mathlib toolchain. The
receipt records the exact statements, source/export hashes and standard
axioms. It does not formalize the BBP denominator induction, complete
complex-operator theorem, analytic spill asymptotics, sparse control's
infinite limits, or π normality. See [kernel receipt](../research/2026-10-26/selected_branch_validation/lean/kernel-observation.json).
