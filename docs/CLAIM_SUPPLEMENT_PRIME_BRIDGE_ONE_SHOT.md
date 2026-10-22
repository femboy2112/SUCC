# Prime Bridge One-Shot — source and claim supplement

**Date:** 2026-10-22. **Parent:** `main@b116841f12b41aaf7600da39bbb40577f25b6295`. **Non-main branch:** `research/prime-bridge-one-shot-2026-10-22`. **Research only; no main merge or archival changes.**

Full paper/proof: [PRIME_BRIDGE_ONE_SHOT.md](../research/2026-10-22/PRIME_BRIDGE_ONE_SHOT.md). Code: [arithmetic_epr_star.py](../observational_succ/arithmetic_epr_star.py). Hostile tests: [test_arithmetic_epr_star.py](../tests/test_arithmetic_epr_star.py). Exact receipt generator: [arithmetic_epr_star_probe.py](../scripts/arithmetic_epr_star_probe.py).

| ID | Statement | Verdict | Boundary / hostile control |
|---|---|---|---|
| PB-01 | Actual p=2 Bruhat–Tits first shell has three index-2 lattice neighbors; known [[3,1,2]]_3 code corrects any one erased qutrit | CLASSICAL, explicit proof + exact local checks | Assignment of F3 qudits to F2-lattice branches is **chosen**, not canonical; no p-adic CFT |
| PB-02 | Three exact Dirichlet samples s=1,2,3 recover chart {1,2,4}; compressed genuine V2 has exact representations on each two-leg boundary region | PROVED LOCAL + exact finite tests | Not a global unitary from infinite analytic Hilbert carrier to finite code |
| PB-03 | At beta=2, the finite prime-weighted EPR state (4,2,1)/sqrt21 satisfies the mirror equation after every one of 9 independent left/right two-leg region choices | PROVED LOCAL + integer-exact support oracle | Mutant (4,2,2) still encodes quantum information but breaks the fixed prime mirror |
| PB-04 | After erasure decoder, rho_AB is unitarily equivalent to rho_bulk tensor I3/3; entropy splits exactly as S(AB)=S(bulk)+log3 | CLASSICAL perfect code + explicit reconstruction proof and direct density-matrix checks | No Einstein equations, black-hole entropy formula, global RT/QES extremization |
| PB-N1 | Projecting S and V2 separately to {1,2,4} preserves their global affine braid | REFUTED | T B e1=e4, B² T e1=0; intermediate projection erases source paths |
| PB-N2 | A three-qutrit boundary exactly realizes the full infinite arithmetic TFD | REFUTED | Infinite Schmidt rank and a strictly positive finite-rank approximation deficit |
| PB-05 | For all real g, H_g=log n+g(S+S*) has trace-class Gibbs factor iff beta>1 (beta positive) | CLASSICAL / PAPER PROVED by compact resolvent and eigenvalue min–max | No interacting bulk metric, no new KMS classification |
| PB-06 | Source-natural multi-depth p-adic/adelic functor preserving **both** S and Vp, including complete histories | UNVERIFIED | Requires path/exit accounting and controlled limits |
| PB-07 | SUCC obtains genuine gravitational ER=EPR duality or signed completed Weil positivity | UNVERIFIED / RH OPEN | No spacetime dynamics, genuine gravitational bulk, or signed-Weil source identification |

**Validation statement:** 12 exact local unittest cases passed under Python 3.13, plus a deterministic receipt with module hashes. This is **not** a claim that current remote CI, full tests, or Lean kernel certification passed. The mathematical code of Pastawski et al. and the Hardy–Dirichlet realization of Hedenmalm–Lindqvist–Seip are classical inputs. The source/analytic/mirror/geometric commuting network is **new to this project's implementation only**, without a priority claim.

**Next falsification opportunity:** construct a genuinely source-faithful, cofinal, multi-depth tower of arithmetic charts and quantum codes. Demand non-tautological commuting diagrams for S and Vp, reversible analytic reconstruction, controlled boundary exits, norm limits and certified local-to-global gluing. A precise obstruction would also constitute success.
