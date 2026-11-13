# Gauge-complete normality probes: taxonomy, source transport and oracle discipline

**Research date:** 2026-11-13. **Base:** Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`. **Status:** the original zero-seeded BBP source, proof contracts and all historical files remain frozen. **π normality / R0 / RH / Goldbach / Collatz general conjecture remain OPEN.** This is a *gauge audit and an exact classical-source synthesis*, not a claim of new world-level mathematics.

## Steelman: what the objection fixes

A hostile counterexample to a *stronger* instrument requirement is not a counterexample to the target property. Normal base-16 radix orbits can have moving-lag correlations arbitrarily close to one. Thus `sup_{1<=ell<=H_N}|c_N(ell)| -> 0`, for unsuitable growing schedules, is **not necessary for normality**. The authentic endpoint target is weak Haar convergence of the empirical radix-orbit measures; a probe is **complete** only if the proposed asymptotic criterion is equivalent to that convergence on its declared carrier class, or **sufficient** if a proof establishes its forward implication. Probe failure by itself does not imply target failure unless necessity has been established.

There are two distinct questions: (1) whether an observer detects *normality* modulo a lawful observational gauge; (2) whether an exact observation is *authenticated as the original BBP zero seed*. A normality-preserving gauge can erase origin identity. Never infer (2) from (1).

## Proven archive foundations, not to be reinvented

- `research/2026-11-07/fourier_yoneda_pinbed/THEOREMS.md`, Theorems 2/5 and section 9: continuous Bernoulli pinbed, exact rational energy, characteristic kernel, source-to-pi `O(B^-2)` norm transfer, and `pi normal iff E(mu^U_B)->0` on every shell. These are proved reformulations, *not* a new cancellation estimate.
- Draft PR #611, `research/2026-11-13/joint_time_lag_response/LAG_COMPLETENESS.md` and `ABSOLUTE_LAGS.md` (read at `7306e766c0bc212af1d93bb349358bebb579ff42`): fixed nonzero lag with **all** Fourier modes is normality-complete on radix orbits, while one mode or a moving-lag maximum is not. Signed/absolute Fejer aggregates are complete under their declared all-mode/diverging-window quantifiers. Do not silently import the unmerged branch into main.
- Main XXV `docs/PI_NORMALITY_FRONTIER.md`: zero-seed authenticated four-pole source, exact Green tail; no all-scale signed normality estimate. `docs/PI_FRONTIER_CONTRACT.md` already distinguishes fixed-frequency Weyl from moving-frequency conductors and quantifier swaps.
- `observational_succ/bbp_minimal_path_gauge.py`, `holonomy_proof_transport.py`, `selected_orbit.py`: legitimate source/gauge distinctions and finite countermodels. Nonflat *model* holonomy is not a physical curvature measurement.

## GCN-01: fixed-lag pinbed oracle is exactly normality-complete (PAPER DERIVATION)

For `T(x)=16x mod 1` and `alpha=pi/16`, write `Y_n=16^n alpha=U_n+T_n`, where `U_0=0` and `U_n=16 U_(n-1)+r(n)` for the frozen four-pole BBP forcing. Fix **one** integer lag `ell>=1`. On each full shell `n=B,...,2B-1`, define

\[
\nu^Y_{B,\ell}=\frac1B\sum_{n=B}^{2B-1}\delta_{\{Y_{n+\ell}-Y_n\}},\qquad
\nu^U_{B,\ell}=\frac1B\sum_{n=B}^{2B-1}\delta_{\{U_{n+\ell}-U_n\}}.
\]

Let the *already existing* Fourier–Yoneda characteristic pinbed energy be

\[
E(\nu)=\|B_2*\nu\|_{L^2(\mathbb T)}^2
=\sum_{h\ne0}\frac{|\widehat\nu(h)|^2}{4\pi^4h^4}
=-\frac16\iint B_4(\{x-y\})\,d\nu(x)d\nu(y).
\]

Here `B_2(t)=t^2-t+1/6`, `B_4(t)=t^4-2t^3+t^2-1/30` on `t in [0,1)`. For a finite exact rational source law, its pair expression is a rational certificate. For **each fixed ell>=1**, the following criterion is a true equivalence:

\[
\boxed{\pi\text{ normal in base 16}\ \Longleftrightarrow\ \lim_{B\to\infty} E(\nu^U_{B,\ell})=0.}
\]

**Proof:** `Y_(n+ell)-Y_n=(16^ell-1)Y_n`, so `nu^Y_(B,ell)` is the pushforward of the source's radix shell measure under multiplication `q=16^ell-1`. The characteristic pinbed theorem says its energy tends to zero iff that pushforward tends weakly to Haar. The invariant-cover theorem from #611 says: any `T`-invariant probability measure whose `q`-pushforward is Haar must itself be Haar (for *nonzero* integer `q`). Empirical radix-shell limits are `T`-invariant; their invariance defect for bounded tests is at most `2/B`. Therefore shell pushforward-Haar convergence implies shell Haar convergence. Full-shell convergence is equivalent to prefix convergence via dyadic decomposition. Classical radix Weyl criterion gives normality. The converse follows by continuity of `q_*` on circle probability measures and invariance of Haar under multiplication by `q`. Finally, GCN-02 below replaces completed `Y` by exact rational `U` with vanishing error. **Every quantifier here matters:** `ell` is fixed before `B->infinity`, the entire pinbed spectrum is retained, the shell is full (not a zero-padded Fejer record), and the original source is pinned. This synthesis does not establish the limiting hypothesis for pi.

## GCN-02: completion transport is uniform in arbitrary moving lag (PAPER DERIVATION)

The unchanged BBP source has the positive decreasing complementary Green tail `0<T_n<r(n+1)/15`. The positive decomposition

\[
r(n)=\frac6{p(p+3)}+\frac4{p(p+4)}+\frac5{p(p+5)},\qquad p=8n-7
\]

makes `T_n` decreasing and gives `r(n+1)/15<1/(64n^2)` for all `n>=1` by taking `p=8n+1`. Hence `|T_(n+ell)-T_n|<=T_n<1/(64 n^2)`, **uniformly over all integer `ell>=1`**. The periodic Bernoulli surface satisfies

\[
\|B_2(\cdot-a)-B_2(\cdot-b)\|_2\le|a-b|\,\|B_2'\|_2=|a-b|/\sqrt3.
\]

Minkowski and `n>=B` give, for every integer `B,ell>=1`,

\[
\boxed{\left|\sqrt{E(\nu^Y_{B,\ell})}-\sqrt{E(\nu^U_{B,\ell})}\right|
 < \frac1{64\sqrt3 B^2}.}
\]

The squared error *budget* is exactly `1/(12288 B^4)` (not a certified bound on either energy). This is a genuine selected-source transport statement, stronger than an `O_h` bound in that it is a single all-frequency *integrated* inequality and its error is independent of `ell`. Yet **it does not require** the energies of moving-lag packets to tend to zero. Transport completeness and statistical decay are different proof obligations.

## GCN-03: legal gauge group versus illegal signal laundering (EXACT)

For `j in Z`, let `s=j/15`. Because `16^n s=s mod 1`, the same-forcing seed-mutated orbit is a constant translate of the zero-seed orbit:

\[
U_n(s)=U_n(0)+16^n s,
\quad \{U_(n+ell)(s)-U_n(s)\}=\{U_(n+ell)(0)-U_n(0)\}.
\]

Therefore fixed-lag records, the associated pinbed energy and the **normality truth value** are invariant under the order-15 torsion gauge. The actual source-identity predicate `U0=0` is *not invariant*. For arbitrary finite empirical laws, the pinbed energy also survives a **common** circle rotation and inversion of the observation coordinates. These are distinct transformations; do not identify common chart rotation with a legal change of underlying radix initial condition for arbitrary angle.

Arbitrary **sample-dependent** rephasing is NOT a gauge: it can transform a constant all-zero signal into an evenly-spaced grid, dramatically decreasing pinbed energy while preserving no lawful common carrier transition. A suitable coordinate connection and source passport would be required to justify it. Gauge consistency does not imply Lorentzian physics.

## GCN-04: audit of instrument validity (VERDICTS)

| Instrument | Correct inferential status | False requirement / missing control |
|---|---|---|
| Fixed-word cylinder frequencies, every fixed word length | **CLASSICAL EQUIVALENT** | `sup_k D_(N,k)->0` is false for every finite N, including normal sequences |
| Fixed-h Weyl coefficients for every nonzero integer h | **CLASSICAL EQUIVALENT** | Uniform suppression of arbitrary moving h not required; finite rational orbit has exact moving-h resonances |
| Fourier–Yoneda characteristic pinbed energy of original source | **EXISTING EQUIVALENT REFORMULATION** | Numerical finite near-zero alone insufficient; finite grid impostors have positive `1/(180q^4)` |
| Full fixed-lag all-mode records; now fixed-lag characteristic pinbed | **EQUIVALENT on radix orbits** | Single mode or missing spectral families not complete; require invariance of weak limit |
| All-mode Fejer signed/absolute aggregates on any lawful diverging schedule | **EQUIVALENT on orbit**, as proved #611 | Individual moving-lag maximum may approach one on normal examples |
| Original BBP exact source/zero seed and analytic Green completion | **SOURCE AUTHENTICATION + TRANSPORT** | Does not itself provide signed Fourier saving; zero seed is not a gauge-invariant identity |
| Finite numerical Weyl, exact carry/prefix counts, finite prime clocks | **CERTIFIED FINITE diagnostics** | Universal `N->infinity` and complete mode conditions not certified |
| Generic positive-Gram, curvature, spectral bulk and gauge diagrams | **MODEL / REQUIRES SOURCE MAP** | Positivity/coherence does not imply statistical decay or completed Weil positivity |
| Coarse or missing-primary torsion channels | **PROVED ACCESS GAP / COUNTERMODEL** | Different carriers may be indistinguishable with incomplete readouts |
| Individual R0, parity, one-mode and Goldbach/RH partial observables | **PARTIAL GOALS / NECESSARY OR CONDITIONAL** | Do not falsely promote to the full conjecture without an actual implication theorem |

**Audit coverage:** The GitHub API recursive tree for main at pinned `db9fb4b...` contains **10,944 files**, of which **946 `tests/test_*.py`** and **509 Python `scripts/*.py`**. This covers every path in the main-branch tree, **not** every file's contents or proof authority. The probe/test taxonomy above is based on inspection of key primary modules, main contracts and PR #611, not an exhaustive 946-module manual review. The new `scripts/normality_probe_contract_inventory.py` can inventory *every installed path and AST test name*, hash the source and flag candidate families, with all theorem statuses intentionally marked `UNREVIEWED`. No static filename classifier is promoted to mathematical proof.

## GCN-05: mandatory gate for future mathematical probes (METHOD)

A proposal for a truth-classification probe must declare its (1) carrier and source pin; (2) target predicate; (3) observable family and its missing modes; (4) the **actual quantifiers** (fixed vs moving, finite vs asymptotic, point vs measure, prescribed vs existential scale); (5) lawful gauge group and transport; (6) iff / necessary / sufficient / diagnostic proof status; (7) residual countermodel; and (8) the next target-splitting arithmetic calculation.

**Calibrated controls:** positive explicit normal sequences (e.g. base-16 Champernowne, by the classical theorem, not a finite numerical certificate); negative eventually periodic and biased nonnormal sequences; **null** legal gauge translations `j/15`; illicit samplewise-gauge mutation; missing-mode `{0,1/2}` mixture with zero first Fourier coefficient but positive pinbed energy; finite `q`-grid with arbitrarily tiny but nonzero energy; same-forcing wrong seed and nonoriginal forcing; and a de Bruijn normal sequence with substantial moving-lag coherence as constructed in #611. These controls cannot all be certified for their asymptotic truth by a finite test; the mathematical construction/proof is the authority, while tests check implementations and finite witnesses.

For RH, gauge equivalence must preserve the original **completed signed Weil form** including prime powers, archimedean Gamma, contact and poles; for Goldbach it must preserve **pointwise** even-integer representation positivity (averages are not sufficient); for Collatz it must preserve the **actual dynamical transition graph and universal termination predicate**, not only finite trajectories. These are methodological requirements, not cross-domain proof transfers.

## Next theorem, not a circular oracle

The fixed-lag pinbed is a normality-complete *observer*, but proving `E(nu^U_(B,1))->0` is still exactly the open normality problem. The next proof-carrying step must use the actual centered integer carries / original-source selected signed currents (see PR #608) to establish a genuinely uniform-in-B **statistical saving** on these exact rational lag measures. A sufficient quantitative hypothesis would be `E(nu^U_(B,1))<=rho(B)` for all B>=B0 with `rho(B)->0`, but asserting that hypothesis as an axiom or obtaining it from numerical fitting would just rename the problem. Try hostile same-forcing wrong seeds first, preserve full signed cross terms, and quantify the source tail and chart transport separately.

## Claim ledger / validation limits

- **GCN-01:** PAPER DERIVATION (existing characteristic pinbed + classical invariant covering; new SUCC combination). All-B limit criterion is **equivalent**, not established for pi.
- **GCN-02:** PAPER DERIVATION (original BBP source, positive Green tail, Bernoulli L2 translation); finite exact checker in `normality_gauge_bridge.py`; signed cancellation OPEN.
- **GCN-03:** EXACT ALGEBRA + FINITE TEST (15-torsion and chart symmetries). Gauge-of-normality does not authenticate zero seed.
- **GCN-04:** ARCHIVE CROSSWALK, not an exhaustive theorem audit; statuses inherit source provenance. Missing full content coverage remains an access/time gap, not a mathematical no-go.
- **GCN-05:** PROPOSED METHOD; not a theorem.
- **Local isolated validation:** 12/12 tests passed with a minimal exact replication of `duck_bbp.forcing`. That shadow is **not** a complete repo checkout or independent source implementation. Source four-pole equality is tested, and independent B4-pair and sorted-energy formulas agree. Full `AGENTS.md` gates, hosted CI and proof-assistant authority must be checked on the published branch before any integration.

**Files:** `observational_succ/normality_gauge_bridge.py`, `tests/test_normality_gauge_bridge.py`, `scripts/normality_probe_contract_inventory.py`. No merge/release or source mutations. This report is steelman → crucible → verdict, with refutations limited to their exact quantified targets.