# Moonshot triangulation: source-faithful phase echo

Research-only child of PR444, pinned at `661553f182c425b06b5339ed02d7739a0ae72380`.
Main XVIII was `4eb411e3730a9e7b95480369a438b89d9a433a4b`. No original source,
production, formal, workflow, archival proof or canonical claim status is changed.
**No pi-normality or RH proof is claimed.**

## What survived six rounds

The original four-pole unitary propagator P_n admits the exact loop

    E_(n,h)=P_n^* M_h P_n M_(-h16^n)=exp(2pi i h U_n) I.

Every control branch returns its data register to the SAME state, retaining only
the authenticated arithmetic phase. Coherently recombining N branches gives
return probability exactly `|sum_(n<=N)exp(2pi i h U_n)/N|^2`, for any normalized
data state. This removes Gaussian seed averaging without using a delta vector.
An exact finite implementation also exists on the growing common ODD source
conductor, not on the insufficient 2-adic clock alone. Neither version proves
the phases cancel. The controlled inverse dynamics and exponentially growing
modulation are declared mathematical resources, not available hardware or speedup.

Three independently checked improvements accompany that construction:

- Raw averaged quantum probes converge strongly to zero for every fixed L2 state,
  while their operator norms approach one. They can therefore falsely suggest
  normality on the genuine coherent nonnormal counterseed.
- A Gaussian probe at initial width 16^-m recovers the first m arithmetic terms
  within a constant depending only on h. Normalize by RESOLVED m, not the total
  horizon N. The original pointwise-last-phase condition is stronger than this
  averaged criterion; it is not contradicted.
- The Feynman regulator produces an exact, previously unaccounted echo translation
  and chirp. A calibrated translation/phase correction cancels both. Parent
  fixed-band norm estimates cannot be reused after exponential countermodulation.

## Executed triangulation

`PROOFS.md` gives derivations, domains, countermodels and source provenance.
`PREREGISTRATION.md` predates fresh measurements. `CERTIFICATES.tsv` supplies 30
exact rational interval records: calibration N=48,96; fresh N=384,768,1537,3072;
h=1,3,5,7,11; K=floor(log_4 N). Both lag signs occur. These are finite facts, not
an asymptotic saving. Selected arithmetic certificates use the original four
poles and literal zero initial state. Countermodels are separately labeled;
original-source error budgets fail closed on arbitrary streams.

51 new exact tests, 368 combined snapshot tests in both forward/reverse order,
separate symbolic operator audit, and 150/150 scalar high-precision cross-checks
passed. See `VALIDATION.md` for the exact scope and retained execution failures.
Full repository validation, new Lean and external peer review were NOT run.

## Reproduce

    python -m unittest discover -s tests -p 'test_moonshot_phase_echo.py' -v
    python research/2026-11-01/moonshot_phase_echo/run_probe.py 384

The probe writes raw rational JSON; displayed decimals are not proof authority.
No optional numerical package is needed by the tests or certificate generator.
All local labels M00-M08 are dossier-local, not registered proof authorities.
