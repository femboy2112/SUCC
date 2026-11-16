# Validation — Source-attached Interferometer Atlas, 2026-11-15

## Scope and original source

Staged on pinned [SUCC #642](https://github.com/femboy2112/SUCC/pull/642) commit `89c6f645938c3f1e4f002f5e81411f458db1689c`. Original source: the four signed rational poles and **literal** `U0=0`; none of its archived code, provenance manifest, CI/workflows or source contracts is edited. The Oily2 frequency distribution is a *declared observer law* motivated by the original critical positive Oily grade, and the true π orbit remains deterministic. The reference conditional Gamma quantum source is not declared a physical model of π. The RH signed form is never replaced by a positive generic Gram.

**Local runtime:** Python 3.13.5, standard library `Fraction`; independent SymPy 1.14.0, mpmath 1.3.0 for an explicitly labelled high-precision smoke check only. No fresh physical data or actual stochastic hardware detector run. The test suite runs on a **staged isolated package**, not the full root SUCC worktree; root suite, Lean, native provenance gate, and hosted CI are **not claimed**.

## Actual locally executed commands

```bash
cd staged-root
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -q
PYTHONPATH=. python research/2026-11-15/interferometer_atlas/independent_oracle.py
python research/2026-11-15/interferometer_atlas/independent_symbolic.py
PYTHONPATH=. python research/2026-11-15/interferometer_atlas/probe.py
python -m compileall -q observational_succ/interferometer_atlas.py \
 tests/test_interferometer_atlas.py research/2026-11-15/interferometer_atlas/*.py
```

**Observed, exact arithmetic:**

- **30/30 focused local tests PASS** (`receipts/FOCUSED_TESTS.log`). These include the original rational forcing/source zero, 16-ary signed Haar and independent pair histograms, Oily weights/tails, Gram/Fejér pair identities, original integer-conductor marking, adaptive propensity controls, and malformed-argument rejection.
- **6,820** independent *exact rational* quarter-grid full Oily kernel / finite-frequency-plus-tail comparisons, from an implementation that does **not import** the primary module (`receipts/INDEPENDENT_ORACLE.json`). The infinite kernel is exact on four roots of unity, including its negative pointwise values; every aggregate remains nonnegative as required.
- **360** separate exact pair-vs-histogram Haar comparisons on combinatorial synthetic words; **48** separate source-generated original BBP Haar comparisons using a different implementation of exact rational BBP digit certification.
- **12** independent SymPy derivation checks including actual Oily/BBP rational function factorization, conditional PGF, unit-root kernel, arbitrary symbolic child Haar identity, iid diagonal-null `1/B`, Oily mean-harmonic `8/3`, and source transport coefficient `7/12` (`receipts/SYMBOLIC_ORACLE.json`). These are mathematically related implementations, not independent empirical source witnesses.
- **5** high-precision *noncertificate* phase comparisons using `mp.pi` and independently reconstructed rational `U_n` for B=1,2,4,8,16. They fall within the already proved source transport budget. Their numeric values **do not certify** any asymptotic theorem.
- **4 independently generated finite exact original-π shell readouts**, B=4,8,16,32, `H=16` and Haar depth K=8 (`receipts/CERTIFIED_SOURCE_SHELLS.json`). The Oily readout encloses π via rational Machin alternating brackets, rational trigonometric Taylor error, original four-pole Green tail and explicit infinite-h tail. The Haar readout uses only certified original-source hexadecimal digits. Outward 10-decimal endpoints are stored, but arithmetic before rounding is all exact `Fraction`.
- `compileall` PASS for staged scripts.

**Initial defects found and corrected before the final replay:** an illustrative first-version test miscopied the two-geom grade tail `sum_{j>=13}w_j` as `15/32768` instead of its correct value `15/16384`. The actual source formula was unchanged. A symbolic oracle first compared two algebraically equal factorizations with `==` (unsimplified SymPy trees) and first compared an unsimplified infinite sum. Both were repaired to polynomial expansion or exact simplification. Final byte checks refer only to the corrected source.

## Certified finite original source intervals

The actual rigorous outward values are stored in `receipts/CERTIFIED_SOURCE_SHELLS.json` with error components and `strict_global_conclusion: UNVERIFIED`.

| B | original π Oily full mode energy | original π Haar full depth energy |
|---:|---:|---:|
| 4 | [0.1265643593, 0.1996743040] | [0.2240234375, 0.2279296875] |
| 8 | [0.0995382771, 0.1179607219] | [0.1437825520, 0.1476888021] |
| 16 | [0.0957956977, 0.1005462675] | [0.0693522135, 0.0732584636] |
| 32 | [0.0279846476, 0.0293172486] | [0.0311279296, 0.0350341797] |

These deterministic finite observations cannot establish the sign or rate of **any all-large-B inequality**. The first two detector geometries measure different energies; they are not expected to give equal finite values.

## Epistemic and statistical firewall

- **DISCLOSED (paper mathematics, under stated conditions):** full-support Oily weighted Weyl equivalence; new Haar cylinder-energy normality equivalence; exact positive Fourier/Haar pair energies; Oily truncation tail; iid null `1/B` expectation; RH negative-witness randomizer only under the full valid Weil test domain and sign-availability premises.
- **PROVED SOURCE-SPECIFIC (paper derivation):** completed-to-rational original BBP all-harmonic energy error at most `7/(12B²)`, using authenticated inherited Green bound.
- **OBSERVED/FINITE CERTIFIED:** four source readout intervals above, focused and oracle tests. High-precision mpmath smoke is **not** finite rigorous certification.
- **UNVERIFIED:** any `C_B->0`, `H_B->0`, prescribed spectral purity, uniform two-epoch signed Haar overlap, R0, π normality, global original signed Weil positivity, RH, original BBP→physical quantum channel, or a new all-source γ/Haar phase intertwiner.
- **REFUTED implication controls:** R0⇒normality (`1/15` counterexample), balanced root digits⇒normality (period-16 deterministic second digit), zero parity⇒all-child uniformity, positive source Gamma spectrum⇒chronological cancellation, one finite shell⇒all-large-shell result, lack of negative Weil sample⇒RH, negative heat parameter counterexample⇒not RH.

The 30-family inventory in `INSTRUMENT_LEDGER.json` is a **frontier inventory**, not a list of 30 independent mathematical proofs. Many are equivalent views of the same still-open target. Claim statuses are descriptive evidence boundaries and do not imply scholarly priority or external peer review.

## Remote integration gate

Before merge: verify pinned parent head; create **non-main draft PR**, compare against pinned parent for only additive files, re-read remote blob SHA against staged original bytes, inspect the exact new GitHub CI SHA; run the repository's four required `AGENTS.md` validation commands in a real checkout. No existing CI success or older PR badge certifies this new branch.
