# ASTRA ULTRA / CODEX — π Pascal–Walsh–Fourier proof forge (next execution)

**Repository:** https://github.com/femboy2112/SUCC.
**Required first actions:** refresh current main, PR #268/#269 and this Pascal branch before work; inspect AGENTS.md, frozen BBP source/PROVENANCE, exact head, branch ancestry, local test suites and returned CI. Preserve immutable original source. No merge or release without authorization. Work on a new non-main stacked draft PR, commit and push actual tested code.

Read the complete [PASCAL_CARRY_INTERFEROMETRY.md](../research/2026-10-24/PASCAL_CARRY_INTERFEROMETRY.md), the [PASCAL_CARRY_SELECTED_RECEIPT.json](../research/2026-10-24/PASCAL_CARRY_SELECTED_RECEIPT.json), PASC-01–09 ledger and all #269 TWA source definitions. Preserve the actual signed four-pole BBP forcing and selected y0=0.

## Verified starting point

- A four-bit carry zero-branch is exactly the 16-term Walsh product with Pascal order multiplicities (1,4,6,4,1). The four Ramanujan primitive shells are its highest-bit slice sums. All 15 Walsh interactions must be retained unless a source-specific argument bounds their weighted total.
- Uniform every 1-,2-,3-bit marginal does **NOT** force central occupancy 1/16: even-parity code has exactly 1/8. Odd unit symmetries 3,5,7,11,13 also fail via the δ0 model.
- BBP forcing r(n) is a strictly completely monotone Hausdorff moment: (-1)^k Δ^k r(n) has an exact positive integral and an exact rational beta upper bound. The Pascal source jet Δ^k y_n−15^k y_n has O(p^(-1.609...)) source correction at specified logarithmic order, **but that holds for all initial states** and does not prove selected cancellation.
- All 15 primitive cyclic additive carry characters have exact source-selected transport into **15 ordinary circle integer frequencies** with the forcing correction. Taylor degree R=2 gives rigorous absolute o(D) transfer error at terminal τ≈4/M, M≈p^(2/5); degree ceil(log p) gives uniform o(1) absolute error on all prescribed scales.
- The actual cancellation theorem is still absent. π normality (base 16/2/3/decimal and absolute) and π-specific independence are OPEN.

## Moonshot A — source-selected signed Fourier jet, not generic symmetry

Keep p=8m+1 and W, E_tau, D, κ, η, δ and δ+ exactly as defined in the dossier. Fix H={-7,...,-1,1,...,8} and

    J_R = sum_{h in H} sum_{(s,t) in E_tau} exp(2*pi*i*h*(y_t-y_s)) *
          sum_{l=0}^R (2*pi*i*h*(eta-delta+)/16)^l / l!.

PASC-08 **proves**:
    |16 Z - Q0 - J_R| <= 15*Q0*((22/7)*(tau+eps))^(R+1)/(R+1)!.

The whole proof route would close if source arithmetic yielded a bound on the real signed J_{ceil(log p)} <= C D uniformly at all needed scales (or sufficient cumulative budget via a correctly proved variable-retention recurrence). On the terminal scale, J_2 <= C D is already enough for that one scale, but that alone DOES NOT prove normality. No input from Galois averages, fake initial states or full-phase character independence.

Try exact Fourier expansion of the successor-arc cutoff with a rigorously controlled trigonometric majorant/minorant (Fejér, Selberg or Poisson). The resulting bilinear twisted Weyl amplitudes involve real source frequencies h+16k and the actual small r(n+1). Work out the exact domain, cutoff errors, and whether the finite frequency range k~M can be handled without presuming normality. This is a candidate mathematical tool, not yet a successful bound.

## Moonshot B — exploit Pascal prime arithmetic without illicit transfer

Prove/use Lucas, Kummer, and binomial p-adic carry valuations on the *correct* integer lift; determine whether their mod-2^j structure defines a source-preserving transport through each κ gate. Prime 3 and prime 5 divide 16−1 and thus are exactly annihilated under Δ of a homogeneous 16-clock, while good p≥17 see an invertible factor 15; do not call 3-adic/5-adic disappearance binary cancellation. Test one selected source-dependent nonunit map or rigorous obstruction beyond the δ0 unit symmetry.

Investigate complete 16-cell conditional interactions (including 4-body order) and whether an actual BBP source identity forces cancellations across Pascal subset orders. Demand a bound or a counterexample; an identity with zero new source restriction does not repay the theorem debt.

## Moonshot C — adversarial numerics, exact source and proof artifacts

Re-run 21 focused tests (9 inherited and 12 new) in a genuine checkout, compare hash-identical source and Git receipts. Expand actual-source held-out good primes, preregister p/radius/masks, retain signs and diagonals. Use a compressed source-independent interval counter for large windows to avoid O(D^2) full exact enumeration if possible; independently certify border and carry decisions. Plot all 15 Walsh terms and the four Ramanujan shells without fitting an exponent from finite data.

Calibrate:
- even-parity 3-wise independent (4th-order survives);
- all odd-unit invariant δ0 carry law;
- same-forcing initial 1/3,1/5,1/15 gauges;
- changed-zero-initial dyadic fake from #266;
- source wire-twist/gauge anti-joining from #268;
- omitted η and miscentered κ mutation;
- arbitrary sample ellipses and endpoint threshold failures;
- nonsmooth arc cutoff and illegally swapped infinite Fourier series.

For any claimed signed saving require a new source-specific hypothesis or exact derivation, a hostile countermodel that could falsify it, full status ledger with weak premises, and an independent holdout. Do not invent Lean compilation; optionally formalize the 16-point Walsh/Ramanujan and beta-integral recurrence in Lean if actually available, keeping classical imports explicit.

## Completion contract

Concrete deliverables: new proof or bound / decisive no-go, exact source witnesses, runnable tests, deterministic receipts, an independently audited paper-level derivation, claim namespace with earned statuses, coherent handoff. Review correct branch ancestry and hosted new-head CI; preserve provenance and signed original archives; commit/push a draft PR. Never assert π normality without a legitimate source-specific all-scale \(O(D)\) or equivalent sufficiently strong cumulative estimate.


## PASC-10 donor: initial-selector Haar averaging (DO NOT PROMOTE)

The addendum \`research/2026-10-24/PASCAL_SOURCE_GAUGE_AVERAGE.md\` proves an unconditional **ensemble** theorem: averaging the genuine forcing recurrence over Haar \(x_0\) gives exact \(\mathbb E(16Z-Q_0)=15D\), and a finite prime grid has an explicit \(64D(D-1)/q\) error. The selected \(x_0=0\) is allowed to be exceptional. New exact tests explicitly detect selected vs ensemble divergence. Use this only as a positive calibration and to design a source-specific *point-selection/derandomization* instrument; using the ensemble theorem directly as π cancellation is a fatal false proof.
