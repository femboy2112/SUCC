# Claim ledger — dual-radix Collatz seam

| Claim | Status | Scope and exact receipt | Boundary / mutation |
|---|---|---|---|
| DRCS-01 | **PROVED (classical)** | Point mirror `(d,r)↦(15−d,1−r)` off digit boundaries and `UR=R̃U` on L²; algebraic substitution | Boundary convention essential; NOT physical slit experiment |
| DRCS-02 | **PROVED (classical)** | Real/2-adic digit completions, opposite complement signs, symbolic shift intertwinement, normality iff shadow shift Haar | No continuous field isomorphism or new normality theorem |
| DRCS-03 | **PROVED (elementary)** | `3(5J_n)+1=5(3J_n)+1=16^n`, mirrored digits, real/2-adic ±1/q completions | `5x+1` is NOT the standard Collatz map; period-one fixed point is nonnormal |
| DRCS-04 | **PROVED (LTE)** | Exact p=3,5 clock valuation, 2-adic attraction to q roots, precision table | p-adic **clock extension** isn't chronological 3-adic convergence |
| DRCS-05 | **PROVED (elementary)** | `16^k|3N+1` iff N ends in k hexadecimal 5s; `C^(4k)(N)=3A+1`; exact finite-state Collatz path | No universal Collatz convergence, no fast proof for arbitrary seeds |
| DRCS-06 | **PROVED (elementary)** | Positive odd sequences `5J_n` and `5J_n+2·16^n` approach same root with distinct accelerated outputs 1,7 | The **unaccelerated** shortcut T extends continuously at −1/3; no false singularity |
| DRCS-07 | **PROVED (elementary)** | First-mismatch valuation `4k+v₂(dnext−d)`, with explicit higher-digit cancellation bound | Requires original symbolic digit order and k matching digits |
| DRCS-08 | **PROVED (CRT)** | Three calibrated heads mod3, mod5, mod2 reconstruct next 16-valued digit given prior mod15 | Head independence, real precision and fault correction not automatic |
| DRCS-09 | **PROVED finite/source-selected** | Original signed source rational tail certifies `3243F6A8885A`, `v₂(5Yπ+1)=4`, `v₂(3Yπ+1)=1` | Not π normality or 11-adic source-filter conjugacy |
| DRCS-10 | **PROVED equivalence; conditional R0** | Constant-digit cylinders iff 2-adic valuation condition; positive lower shell density of d=1/3/5 gives R0 | **UNVERIFIED premise** for authentic BBP every late shell; testing one word insufficient for full normality |
| DRCS-11 | **PROVED no-go** | Continuous additive `Z₂→Z₃` vanishes (2-adic 2^k→0 but 3-adic unit 2^k) | A shared rational source can still have 2/3-adic representations |
| DRCS-12 | **OPEN source-specific joining** | Need independent original-zero signed cofactor/phase estimate | Same-forcing wrong seed, period-1 normality countermodel, matched-jet mutation, phase alias |

**Provenance:** Most statements are elementary classical facts. The composite digit-shadow/Collatz/SUCC interpretation is new to this dossier but not certified scholarly novel. `test_dual_radix.py` and `independent_audit.py` are mathematical model checks, not independent theorem provers or external referees. **R0, full π-normality, universal Collatz, RH remain OPEN.**
