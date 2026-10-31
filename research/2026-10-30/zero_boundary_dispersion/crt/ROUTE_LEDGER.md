# CRT route survival and refutation ledger

Authority: same-model paper derivations and separately implemented exact arithmetic; neither blind independent referee nor Lean authority. Internal predeclarations are in `PREREGISTRATION.md`; they were written before their respective runs, but were not externally timestamped preregistrations. Every authentic computation retains coefficients `(4,-2,-1,-1)` and zero seed. Changed seeds/sources are expressly typed controls.

| Route | Strongest result | Status | Specific boundary / next falsifiable obligation |
|---|---|---|---|
| Fixed filter conductor dichotomy | CG03 already proves fixed P(16)!=0 exponential conductor and P(16)=0 polynomial bound | INHERITED, NON-IMPROVEMENT | Initially considered here, recognized as prior work before promotion; do not count it as new |
| Sublinear moving filters, CT01 | Exact denominator sandwich plus a short-interval LCM yields `log den(P_n(E)U_n)=6n+o(n)` for degree o(n), log height o(n), P_n(16)!=0 | PROVED LOCAL | No real-distance or signed conclusion; test any claimed stronger distribution implication against null/coherent controls |
| Complete finite-field character family, CT07 | Full character-value field contains a cofiber root of odd order D iff `D|p^f-1`; minimum f=`ord_D(p)` and f>=(6n+o(n))/log p | PROVED LOCAL | Exact field operations only; approximate maps/arbitrary externally supplied coefficient fields remain open; need a naturally selected coupling with a signed norm bound |
| Source-forcing inverse cylinders, CT02 | Exact rational possibly empty interval for a whole small-lag window, with measure <=2delta16^-(L-1) | PROVED LOCAL REPRESENTATION | Small Haar measure does not exclude the authentic point; prove arithmetic exclusion from the union allowing rho L bad steps |
| All odd-primary snapshots force finite-window dispersion, CT03 | Arbitrarily small dyadic rational shadow seeds preserve every odd-primary trajectory and have a chosen long coherent window | REFUTED AS STATED | Literal zero boundary is different; rational shadows eventually alias and cannot refute asymptotic normality. All odd-primary data classify rational seeds modulo dyadics |
| Authentic selected positive fraction, CT04/06 | 48 fresh finite joint rows pass >=1/2 slips at distance1/20, including24 SC-06-eligible rows | OBSERVED; uniform SC-06 DARK | No source-derived exclusion of positive-density low-energy cylinders; the pointwise zero boundary must supply it |
| Prime-power Gauss period lifting, CT05 | Pure top mod-p shadow survives; complete p^a-primary orbit receives lower-layer forcing | Pure full-primary lift REFUTED | Exact failures at Q=343,121,169,361,5329; any proposed completion must retain those injections |
| Exact annihilator branch, CT08 | For fixed P=(z-16)Q, den(P(E)U_n)=Theta(n^(4s)), s=#nonzero coefficients of Q | PROVED LOCAL | Pole/resultant arithmetic; not a signed estimate and not a new generic positive-filter certificate |
| Source-family discrimination | Seven-pole null has no declared-window slips; wrong-ratio, same-ratio, rank-matched mutants have many | OBSERVED / inherited exact control proofs | A positive lag-energy test alone cannot identify the authentic source or imply normality |

The genuinely surviving new arithmetic results are CT01, CT07 and the secondary CT08 refinement. None improves the inherited logarithmic **fixed-frequency zero-boundary** signed saving. The direct SC-06 attempt reached an explicit rational cylinder test and exact finite exclusions, then stopped at an unpaid asymptotic exclusion theorem. It did not infer independence of the two CRT factors.

## Raw run inventory

`receipts/probe.{json,log}`: 41 exact filter certificates,25 LCM cases,48 fresh signed-factor rows,2 dyadic shadows,5 prime-power failures,5 source controls and p19/p73 cancellation checks.

`receipts/tests.{json,log}`: 13 focused tests passed.

`receipts/oracle.{json,log}`: reduced-source integer-orbit implementation checked all48 rows, both shadows,12 inverse-branch cylinders and27,786 prime-valuation cases.

`receipts/field-polynomial.{json,log}`: five exact least extension degrees with component orders and minimality checks; four nonzero polynomial resultants and20 exact evaluated-denominator checks.

The runner is a byte-identical copy of PR401 `gamma_twist/run_receipt.py`, relocated here so all outputs stay inside the assigned directory. It captures the exact command, UTC times, local parent SHA, exit status, memory cap, thread cap, and output SHA256. No failed command run is suppressed. Read-only exploration encountered two nonexistent guessed filenames before using `rg`; those were file-location misses, not failed mathematical probes. All four recorded computational runs exited0.
