# Operation REALIZED PATH — Forward History, Doob Momentum and the Original BBP Band

**Research date:** 2026-10-31. **Base:** SUCC draft PR #442, `4f49abd7bf50ceebf5281a39a3f3d4dca8841450`, stacked on PR #441. Canonical main at research start: Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`. All additions remain under this directory and one root discoverable test; no production, historical source, Lean, CI, license, release or main changes. **π normality and RH remain OPEN.**

## Research question

A realized path does more than select an endpoint: it fixes an ordered history, changes the conditional set and weights of its still-possible futures, and can have a directional cost-to-go. Can SUCC represent all three *without* mistaking observer probability for the selected deterministic BBP arithmetic orbit?

**Steelman:** yes, via (i) positive path measures and Bayes/Doob conditioning, (ii) explicit action/geodesic choice with a declared cost, and (iii) history-preserving source-labelled matrix transport. They are different layers, not freely interchangeable.

## Main exact products

1. **RP-01:** Finite stochastic path support conditioned on a realized prefix: `Q_new=Q(.|prefix)`; realization surprisal `-log Q(prefix)` is nonnegative. Prefix update changes all remaining weights. No law of *increasing Shannon entropy* or thermodynamic heat was assumed.
2. **RP-02:** Exact finite Gibbs variational principle, soft Bellman recursion, Doob `h`-transform and zero-temperature shortest-cost path selection (only when cost and admissibility are declared). Local log transition probabilities add the prior surprisal, declared cost and a telescoping future-potential difference.
3. **RP-03:** A positive rational counterexample: two histories with the SAME current visible state but different continuation supports/target odds. Target-conditioned, cost-tilted first-action probabilities are **12/13 vs 1/13**. Coarse endpoint observation fails the dynamical-descend condition.
4. **RP-04:** Exact affine source **ordered matrix** product and independent-step *finite noncommutative path-sum* factorization; a naive time-marginal product provably fails if transition laws depend on history.
5. **RP-05:** The *original, unchanged* BBP source gives a **right-zero idempotent band** `G_i G_j=G_j` and `F_n=I+15G_n`, hence `F_N...F_1=I+15 Σ_{j=1}^N 16^(N-j) G_j`. Exhaustive `2^N`-subset expansion independently reproduces this law. All computations use the genuine four signed poles and literal U0=0.
6. **RP-06:** The original BBP symplectic step is the **time-one Hamiltonian flow** of `H_n=(log16) p(x+r(n)/15)`. Its canonical momentum contracts by 16; `d(xp)/dt` integrates to the exact source action increment `r(n)/16^n` along the selected orbit.
7. **RP-07 / negative:** Different microscopic expressions of a single authentic affine step may carry different intermediate histories but the SAME endpoint/real-circle character. If action depends only on the authentic source and endpoint, it cannot select a unique realization among them. Likewise positive path weights or entropy can be identical under maximally coherent and perfectly cancelling phase assignments; a new source-attested signed phase is needed for a π theorem.
8. **RP-11 / source no-go:** The authentic BBP accumulated action approaches its limit with a total summable defect `<1/1024`. Any fixed positive Lipschitz reweighting by this scalar action changes an N-term signed Weyl mean by only `O_f(1/N)`; canonical Gibbs `exp(-beta A_n)` gives `<beta*exp(beta/5)/(512N)` for beta>0. Thus scalar-action Gibbs cannot manufacture normality.
9. **RP-08 / negative:** The **full** original four-pole BBP law plus U0=0 gives ONE deterministic path. Assigning probabilities to alternate source histories is an *observer or control model*, not a newly proved physical indeterminacy or new quantum process. Nonnormal changed seeds and source mutations remain hostile checks.

## Files

- [PROOFS.md](PROOFS.md): rigorous domains, variational and source-specific derivations, controls, and literature provenance.
- [CLAIMS.md](CLAIMS.md): scope-by-scope ledger; paper/classical vs exact finite vs conjecture.
- [SOURCE_MAP.md](SOURCE_MAP.md): observation and category adequacy, source/phase/energy firewall.
- [VALIDATION.md](VALIDATION.md): exact tests and independent implementation receipts.
- [NEXT.md](NEXT.md): verdict-changing experiments against the selected π signed Weyl gate.
- `realized_path.py`, `independent_oracle.py`: stdlib `fractions.Fraction` implementations.
- `tests/test_realized_path_dynamics.py`: root-discoverable, unique test-module imports.

## The unresolved question

Prove for the genuine four signed BBP poles and selected zero-seed orbit:

`S_N(h)=Σ_{n=1}^N exp(2πihU_n)=o(N)` for every fixed nonzero integer `h`.

A positive stochastic path construction cannot achieve this by itself. Source-specific signed phase, all-time cancellation and the real Archimedean cofiber remain first-class proof obligations.
