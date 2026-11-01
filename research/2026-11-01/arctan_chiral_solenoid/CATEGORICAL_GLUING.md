# Typed source-to-circle-to-Fourier diagrams: reuse SUCC's existing categorical spine

**Scope:** specify mathematical objects, arrows, commutative/twisted squares, and exact counterexamples. This document is a research-only adapter SPECIFICATION, not a replacement `Category` or `Functor` implementation for `operational_yoneda_descent.ObservationPathCategory` and `yoneda.FiniteFunctor` on Main XVIII.

## The objects are NOT interchangeable

1. **Source-index object:** (Z2, rational r:Z2->Z2), with 16-adic finite quotients X_a=Z/(16^a). Morphisms include index unit SUCC n->n+1 and prime-local source map r (isometry).
2. **Chronological rational arithmetic:** actual original n in N, U0=0, U_n=16U_(n-1)+r(n), carries and original four-pole provenance; the direct ordinal/time index is not the Z2 topology.
3. **Projective circle:** CP1 with real equatorial chart t=tan(pi U), Cayley `z=e(U)`; step F_n(z)=e(r_n)z^16, arctan J:t->1/t, transported source r_n^vee=1/2-r_n.
4. **Full inverse-limit/solenoid:** Sigma16 with compatible inverse coordinate towers and odd-source-labeled canonical lift iota(r_n). This repairs four-cover invertibility but does not identify the original partial-history quotient with a full lift.
5. **Finite quantum source and chiral torsor:** odd Q-source clock H_A=C[Z/Q]; its Fourier polarization dual H_Ahat; augmented even clock is the DISJOINT UNION of two q-point torsors A+B, with block conjugate source dynamics.
6. **Completed Mellin differential:** rational t-plane source form P(t)/(16-t^8)dt. It is NOT the original source-index meromorphic 1-form r(z)dz (different poles and j-invariant).
7. **Relative angular period:** (I=[0,1],boundary,eta(t-1),G) modulo `dG` with G=0 at boundary. This is a true target of the Mellin arrow and gives BBP's π/16 without changing the original 4-pole source.

## Declared diagrams and exact verdicts

**A. Four-sheet square (PROVED):** On Sigma16, `[4]*G_n=F_n*[4]` with `G_n=[16]+[4]^-1 iota(r_n)`. Original/source label must be transported to its unique odd-torsion fourth root. `[4]*F_n=F_n*[4]` with unchanged label generally FAILS. On base circle, a four-sheeted cover does not have a global continuous inverse section; on inverse-limit it has a genuine inverse.

**B. Reciprocal/chiral naturality (PROVED):** `J_tau F_n J_tau^-1=[16]+(1-[16])tau-iota(r_n)` with explicit compatible halfturn tau. At base circle `r_n^vee=1/2-r_n`; at fractional Fourier characters a change in tau by kernel-of-projection element changes phases. The diagrams commute only with the correctly TRANSFORMED source label, not with a silently reused original one.

**C. Finite Hilbert gluing (PROVED):** On odd-Q clock, original affine P_n is unitary. On even 2Q the naive ×16 is NOT bijective; gluing A=(1/Q)Z/Z and B=1/2-A by separately typed conjugate P_n^vee produces one block-diagonal PERMUTATION. `J_Q=S_Q DFT_(2Q)^2` is exact on the augmented carrier. No standalone geometry alone supplies a global 16-state Fourier transform as a coordinate permutation of CP1; a Q-state quantum system has pure-state space CP^(Q-1).

**D. Fourier source permutation (PROVED):** At each 2-primary X_a, the time-index source permutation has cyclotomic Fourier kernel K^(a), with support conditions F2/F3. At each odd-Q finite chronological source register, the DFT of F_n produces a different, source-character-weighted inverse-frequency permutation. These are DIFFERENT Fourier functors and require explicit comparison. Their existence does NOT supply a cross-place signed mean estimate.

**E. Cross-completion obstruction (PROVED NEGATIVE):** There is NO continuous extension of time-index source phase e(r(n)) from Z2 to R/Z retaining all actual rational n. n=1+16^j->1 p-adically but e(r(n))->1≠e(r1). Any alleged continuous Beck–Chevalley or source-identification square along this edge is FALSE without changing the object or carrying a separate Archimedean coordinate.

**F. Mellin → relative de Rham/angular quarter-turn (PROVED):** This is the actual new geometric identification: M(source four rational poles) = P(t)/(16-t^8)dt, and `M(source)-(1/8)eta=dG`, `G|boundary=0`. Hence the relative period classes coincide. This is an honest, NON-MÖBIUS arrow. A direct Möbius-equivalence square from source-index four poles to completed t-plane four poles is REFUTED by unequal j-invariants 470596/225 and 1728.

**G. Source/seed signed character (OPEN):** The actual target `S_N(h)=sum e(h U_n)` is not automatically natural or small under A-F. Chiral conjugation gives only `(-1)^h conjugate(S)`, all finite dyadic source characters cancel on COMPLETE CLOCKS, and the Cauchy equilibrium measure is universal. A PASS requires a NEW signed original-four-pole, literal U0=0, all-N source/real cofactor estimate and must fail for coherent same-forcing q=1/5.

## Dependence/independence

These diagrams reuse SUCC Main XVIII `operational_yoneda_descent.ObservationPathCategory`, `yoneda.FiniteFunctor`, `prime_clock_yoneda`, `signed_pushforward`, `tate_schwartz_functor` and `docs/CATEGORICAL_OBSERVER_ATLAS.md` conceptually. No production adapter has been installed and no Lean proof is asserted. The exact maps are derived in PROOFS.md and implemented as finite research probes with explicit source/phase labels. All external mathematics is imported classical; finite algebra + independent source oracles are implementation triangulation, not blind witness independence.
