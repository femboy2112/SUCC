# SUCC Research Dependency DAG

One canonical proof-dependency graph, from carrier mathematics through to the RH application. Every
arrow carries a status so the reader sees immediately **which arrows are closed and which remain
open**. This is the *conceptual* proof DAG; for the *git* PR-dependency DAG of the Academic Main
consolidation see
[ACADEMIC_PR_DEPENDENCY_GRAPH_2026-10-15.json](ACADEMIC_PR_DEPENDENCY_GRAPH_2026-10-15.json).

Arrow status legend:
`[C]` classical imported theorem · `[P]` proved within declared assumptions · `[X]` exact finite
model · `[I]` implementation only · `[U]` unverified construction · `[R]` refuted inference.

## The graph

```
                    CARRIER MATHEMATICS
  B(N) --group completion [C,X]--> Z --localize [C,X]--> Q --adjoin i / complete [C,X]--> Q(i),C
  {Z/nZ} --inverse limit + CRT [C,X]--> Ẑ ≅ ∏Z_p --localize [C,X]--> A_f --× R [C]--> A_Q
                                   |
                                   v
                    SOURCE-INDEXED OBSERVATION
  carrier --finite source chart [X]--> observer interface
         --proof-access classify [P]--> {Simple | IdealHard | Fucked | Unresolved}
         --compact gluing (FIP) [C, nonconstructive]--> global section
         --noncompact escape [P]--> empty limit (no-go)
         --phantom source-map [P]--> ∀N∃z, ¬∃z∀N (no-go)
                                   |
                                   v
                    REPRESENTATION / DUALITY
  Ẑ --Pontryagin [C]--> Q/Z ;  A_f/Ẑ ≅ Q/Z [C] ;  (A_Q/Q)^∨ ≅ Q [C], self-dual, Q^⊥=Q
  S(Q_p) --local self-dual Fourier [C,X]--> S(Q_p)
  S(A_f) --integer-scale rational-translate span [C,P] (CTW-02; REFUTES [R] noninteger-necessity)
                                   |
                                   v
                    ARITHMETIC / ANALYTIC TRANSPORT
  S(A) --adelic Poisson [C,P | conditional on real Poisson]--> Σf = Σf^
  canonical Gaussian⊗∏1_{Z_p} --idelic Mellin [C,P]--> Gamma_R(s)·ζ(s), Re(s)>1
       --classical continuation/poles/FE [C import]--> completed ξ
  log-derivative scalar --[R] recoverable from log-deriv (CTW-11); NOT universal impossibility
                                   |
                                   v
                    WEIL / RH APPLICATION
  completed ξ --signed completed Weil distribution [X]--> W_ζ(f)
       --high-subspace / short-window positivity [P, scoped]--> Q_ζ(f) > c‖f‖²  (codim / a≤1/12)
       --K-relative transport [P]--> D_r ⪰ κ Q_r K Q_r   (relative to K=V*V, NOT κI)
       --zero-shift Douglas range [P]--> 0 ⪯ R0 ⪯ (11/40)²/κ·I   (no D^{-1}/K^{-1} at λ=0)
   ======================  FIREWALL  ======================
       --low Schur sign S0=A−R0 ................................ [U] OPEN
       --"all high positive ⇒ full Weil positive" ............. [R] REFUTED generally
       --source→Weil-sign typed morphism (K_g ⪰ 0) ............ [U] missing; assuming it restates RH
       --all-a / prime-active global positivity ............... [U] RH-equivalent, OPEN
       ==> RH ................................................. OPEN. RH PROVED: NO.
```

## Closed vs open — the one-line summary

- **Closed `[C]/[P]/[X]`:** every arrow from carrier construction through Pontryagin duality,
  finite-adèle spanning, adelic Poisson, idelic Mellin and the completed ξ. These are classical
  theorems (or exact finite models of them); their truth does not depend on any sign.
- **Scoped-closed `[P]`:** high-subspace and short-window Weil positivity, K-relative transport, the
  zero-shift residual bound — each true on a restricted domain / metric, none global.
- **Open `[U]` / refuted shortcuts `[R]`:** the low Schur sign, the "high ⇒ full" shortcut, the
  source→Weil typed morphism, and all-a positivity. **This is exactly where RH sits, and it is
  OPEN.**

Cross-references: [CARRIER_ATLAS.md](CARRIER_ATLAS.md) · [OBSERVER_PROOF_ACCESS.md](OBSERVER_PROOF_ACCESS.md)
· [RESEARCH_FRONTIER_2026-10-15.md](RESEARCH_FRONTIER_2026-10-15.md) · [CLAIM_LEDGER.md](CLAIM_LEDGER.md).
