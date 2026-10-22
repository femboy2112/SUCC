# Prime Bridge claim supplement — PBR-01–20

Baseline: `b116841f12b41aaf7600da39bbb40577f25b6295`. Research branch:
`research/prime-bridge-2026-10-22`; [draft PR #233](https://github.com/femboy2112/SUCC/pull/233).
The project labels below distinguish complete paper proofs, exact finite
calibration, numerical observation and kernel checks. No scholarly priority,
physical source authentication, gravitational duality or RH claim is made.

All proof paths below are relative to `research/2026-10-22/`. Each linked
section states domains/quantifiers, proof and countercontrol. The receipt
pins source hashes, commands and their observed results; it does not promote
a theorem by test count. Original imported claims and IDs remain unchanged.

| ID | Precisely scoped claim | Status / evidence | Boundary and next discriminator |
|---|---|---|---|
| PBR-01 | On ℓ²(N≥1), the logarithmic Gibbs/TFD coefficients are normalizable iff real β>1; entropy, Rényi, fidelity and faithful reductions have the displayed convergent formulas | CLASSICAL / PAPER PROVED; `ARITHMETIC_ER_EPR_FOUNDATIONS.md` A1–A4; exact Q(i) controls | No positive density by analytic continuation; test domains, not finite sums alone |
| PBR-02 | Fixed-basis prime mirrors have a nonzero solution iff every |c_p|>1 and Σ|c_p|^−2<∞, then a_n=a_1∏c_p^−v_p(n), unique up to scalar | CLASSICAL / PAPER PROVED; `PRIME_MIRROR_RIGIDITY.md` B1–B4 | Finitely many prime constraints leave arbitrary rough-source seeds; phases require transported probes |
| PBR-03 | Full cutoff mirror residual²=(Z_N−Z_floor(N/p))/Z_N, tending to0 for β>1 but not monotonically | PROVED LOCAL + PAPER TAIL; B5–B6 | p2 β2 residual1/5→13/49; compressed residual zero is not an infinite certificate |
| PBR-04 | Weighted complete mirror residual sum bounds distance² to the reconstructed state; declared finite-support β=2s sources admit exact finite fidelity certificates plus tail | PROVED PAPER / EXACT RATIONAL CERTIFICATES; `PRIME_MIRROR_STABILITY.md` S2–S5 | Unweighted energy is infinite on nonzero finite supports; no unknown-source tail inference |
| PBR-05 | Gibbs standard representation has explicit Tomita weighted swap, modular operator and no-signaling local-channel law | CLASSICAL / PAPER PROVED; foundations A5–A8 | Type I, not local-QFT type III; arbitrary bounded operators need not have bounded mirrors |
| PBR-06 | Concrete C*(E(r),V_m) has point-norm continuous logarithmic dynamics and faithful β>1 Gibbs KMS states | CLASSICAL / PAPER PROVED; `ARITHMETIC_OPERATOR_INTERFACE.md` §§2–3; independent cyclotomic oracle | No abstract full BC faithfulness/classification claim; B(H) point-norm extension refuted by e_n↦e_n² |
| PBR-07 | β↓1 gives ψ(V_mE(r)V_n*)=δ_mnδ_r0/m, a 1-KMS state on the concrete algebra with Haar profinite restriction and no normal vacuum extension | CLASSICAL / PAPER PROVED reconstruction; operator interface §7 | No normalized ℓ² TFD at β1; no arbitrary B(H) limit |
| PBR-08 | H_g is self-adjoint on D(H0), compact-resolvent, with log n±2|g| eigenvalue bounds and exact Gibbs threshold β>1 | CLASSICAL / PAPER PROVED; `INTERACTING_ARITHMETIC_TFD.md` B1–B2 | Scalar min–max proof, not operator-monotone exponential |
| PBR-09 | exp(itA)ψ0 is prime/odd entangled for0<|t|<1/32 with explicit linear-entropy bound; exp(itH_g) has an explicit g-dependent window | PROVED PAPER + EXACT TAYLOR CONTROLS; interacting B3–B4 | Fixed factorization; numerical propagation is not universal proof |
| PBR-10 | Every g≠0,β>1 Gibbs density is nonproduct in valuation2/odd factorization | PROVED PAPER; interacting B5 | Mixed-state entanglement remains UNVERIFIED; free prefix cutoff already correlated |
| PBR-11 | Lattice projective spheres construct genuine BT balls; full determinant-contact boundary data uniquely reconstruct the rooted unit-edge ball | CLASSICAL / PAPER PROVED / EXACT FINITE; `PADIC_GEOMETRIC_CARRIER.md` G1–G3 | Root, unit lengths and complete contacts are inputs; EPR spectra do not determine them |
| PBR-12 | j_p:C(Z_p)→B(ℓ²N) is faithful/isometric, sends finite characters to E(k/p^r), and respects refinement and p-compressions | CLASSICAL / PAPER PROVED / EXACT PHASE TESTS; geometric G6–G7 | Infinity chart invisible to integers; q≠p range projections cannot lie in one p-local algebra |
| PBR-13 | Coherent |n>↦|n mod q> is unbounded; the Kraus measurement repair is CPTP and entanglement-breaking | PROVED PAPER; geometric G4–G5 | Finite injective source subspaces can encode coherently; full residue coarsening cannot |
| PBR-14 | Arithmetic-weighted qutrit W_f on genuine BT2 is isometric and recovers B(C³) on pair12; all singleton erasures iff uniform weights | CLASSICAL uniform code / PROVED LOCAL weighted law; `PADIC_BULK_RECONSTRUCTION.md` QEC1–4 | Explicit arithmetic compression K_p; at p2 β2 failed erasure leaks trace distance5/7 |
| PBR-15 | Actual BT2 copy refinement preserves encoders; access sets at every radius are exactly classified | PROVED LOCAL; code QEC5–6; all64 radius2 regions for each of two codes and radius3 holdouts | Rooted anisotropic code, not homogeneous perfect-tensor bulk |
| PBR-16 | Cut rank bounds entropy; radius1 uniform pure code saturates, arithmetic weights and lawful radius2 refinement can give strict gaps | CLASSICAL bound / PROVED LOCAL controls; code QEC7 | No unconditional RT equality or original-bond-entropy capacity |
| PBR-17 | Bare O_AW=WO for every logical matrix unit does not imply operational erasure recovery | REFUTED SUFFICIENCY / explicit non-*-preserving similarity; code §6 and hostile H11 | Demand adjoint-preserving observables, CPTP decoder or complete KL |
| PBR-18 | Positive weighted root code has full S3 geometric invariance iff uniform; arithmetic weights retain exactly the privileged-direction stabilizer | PROVED LOCAL; code QEC8 and all GL2(F2) permutations | Add frame/cocycle data or construct a different equivariant code |
| PBR-19 | Same-source CRT/profinite observables glue, but incompatible nested charts, nonrational adeles and compact→Archimedean recovery obstruct stronger source realization | CLASSICAL / PAPER PROVED / EXACT CONTROLS; geometric §5, hostile H10 | A formal local product is not a diagonal-source or gravitational duality |
| PBR-20 | Finite decoder/count/intertwiner identities, conditional mirror word transport and disjoint-reconstruction commutation have explicit bare Lean targets | Formal source plus observed kernel execution status in `PRIME_BRIDGE_FORMAL_RECEIPT.md` | Kernel scope and axiom lists only as actually exported; no automatic analytic certification or trusted-catalogue admission |

Synthesis and typed maps: [ARITHMETIC_HOLOGRAPHY_OBSTRUCTIONS.md](../research/2026-10-22/ARITHMETIC_HOLOGRAPHY_OBSTRUCTIONS.md).
Receipt: [ER_EPR_RESEARCH_RECEIPT.json](../research/2026-10-22/ER_EPR_RESEARCH_RECEIPT.json).
Reproduction: `python scripts/prime_bridge_probe.py`, focused test modules and
the four repository-required commands recorded in the receipt. No benchmark
output is accepted without its command/source scope.
