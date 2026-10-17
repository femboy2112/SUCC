# Claim supplement — four-Schur primitive-dual quotient (PDQ)

**Branch:** `research/dual-variational-schur-source-gates-2026-10-16`, child of draft PR #149. Mathematical proofs: [`FOUR_SCHUR_PRIMITIVE_DUAL_QUOTIENT.md`](../research/2026-10-16/FOUR_SCHUR_PRIMITIVE_DUAL_QUOTIENT.md). **RH PROVED: NO.** These results do not decide `S_4=A_4−R_4`.

| ID | Status | Theorem / actual scope | Limit and falsifier |
|---|---|---|---|
| PDQ-01 | PROVED PAPER / CLASSICAL | `closure_{L2}(V Q4 H)=ker P_poly<=3` on the original meanzero interval. | Requires the exact low Legendre P1..4 and primitive boundary conditions; fails for an arbitrary untyped projector. |
| PDQ-02 | PROVED PAPER | The exact high `K=V*V` dual energy of `Q4 h` equals `||(I−P_poly<=3)h′||²` for `h∈H¹`. | Not `||(Q4 h)′||²`; exact `h=P5−P3` derivative-energy expansion 36→60 is a hostile control. |
| PDQ-03 | PROVED CONDITIONAL / SOURCE-GATED | For authentic `G`, `||g′||_1<11/40` and `D4>=K/50`, any rational response U gives a genuine alternate lower `V*G V−(121/32) V*V <= S4`, with exact finite-Gamma interval enclosures. | May be weaker than U=0; independent source `g′` and coercivity hypotheses remain load bearing. |
| PDQ-04 | PROVED PAPER / EXACT SOURCE INTERVAL for TWO channels | For four derivative moments E, residual dual Gram = H'−E*P⁻¹E. **Two endpoint-vanishing combinations are now authentically certified:** the primitive quotient subtracts source rows `30 c₁*c₁ + 210 c₂*c₂`, with rigorous finite-J original Gamma-tail errors. | Remaining two derivative-moment channels need original-source endpoint values; full H' energy and decisive S4 sign OPEN. No caller-supplied E may be laundered as source. |
| PDQ-05 | PROVED PAPER | Young-only U-transport minus U0 floor is exactly `−L_U−(121/32)U*U`; if `L_U>=0`, an optimized U cannot improve that old floor by this method. | Scope: the universal Young bound, not sharper source-specific derivative energy. No all-method no-go. |
| PDQ-06 | PROVED FINITE / CONDITIONAL | Nested Loewner shorts are monotone if the discarded middle compression of the lower packet is PD, after verifying packet order. | `L<=U` without middle positivity is insufficient: exact 2x2 signed switch gives `Short(L)=+1>−1=Short(U)`. The actual source 30-mode packet is not yet implemented. |

## Source identification and next proof debt

All mathematical abstraction modules explicitly refuse to claim authentic ζ source authority. Only the parent `certified_four_schur_trial.py` has the original SHA-gated source channels and uses the PDQ-03 alternative. Two true-source endpoint-free derivative moments for PDQ-04 are now certified; the remaining full derivative-moment channels, tighter full source derivative energy, and a source-certified S30 packet for PDQ-06 remain open. `precision` now returns an explicit achieved/unmet flag instead of merely echoing the requested number. Claim FQID registry refuses undeclared/wrong-prefix claims. No nontrivial-zero coordinates were read.

**Next decisive artifact:** a source-authenticated rational interval enclosure for the remaining two endpoint-dependent polynomial channels of `(G(e_i−Ue_i))′`, and/or a source-specific full differentiated-convolution energy estimate. The two endpoint-free combinations are already source-certified through authentic low Galerkin rows. Evaluate the PDQ-04 moment correction on real source data; report the sign `AMBIGUOUS` until a rigorous lower or negative trial actually clears zero.
