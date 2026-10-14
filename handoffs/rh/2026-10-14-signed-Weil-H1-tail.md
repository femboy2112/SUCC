# RH candidate handoff — unconditional signed Weil high-spectrum tail on H₀¹

**Status:** PROVED LOCAL, classical techniques, new-to-SUCC source-specific quantitative assembly. **RH PROVED: NO.** Main unchanged. This is a candidate **for review**, not a push into `FuckingRH`.

Source: completed original Gaussian integer theta / completed xi from SUCC PRs #73/#74/#78, plus authentic first zero contour from PR #82 `bb5b6f96f78df0d9472a60441501024e0e2b904e`; immutable first-pair blob `8f5ae1135701a933ba4946cb0b584bba4a355a47`. External identity: classical completed Weil spectral/prime-Gamma distribution, Suzuki 2026 v3 §1.

For `a>0` and `T>=2`, on real or complex `H₀¹(-a,a)`, original Weil spectral contribution from *all* nontrivial `xi` zeros `rho` with `|Im rho|>T` obeys

    |Q_high(v,w)| <= 70 a e^a log(16T)/T ||v||H¹ ||w||H¹.

**Proof mechanism:** theta source yields a first-principles order-one xi growth bound and `F(0)>59/120`. Classical Jensen gives all-zero count `N_abs(t)<7t log(4t)` without RH or a zero list. Dyadic shell summation gives `sum_(|gamma|>T)1/|gamma|² <=28 log(16T)/T`. One integration by parts for each spectral transform (using the unconditional fact `0<=Re rho<=1`) gives the theorem, including multiplicities and off-critical signed contributions. Smooth tests are dense; Suzuki's bounded derivative-kernel map validates H¹ extension.

**Quantified error:** a=.5, T=1e6 gives a rigorously enclosed signed operator/form-norm tail <.001 on `H₀¹` (not an L² coercivity or global positivity gap). This is a significantly improved test space compared with PR #83's C⁷ smooth-specific construction, not an independent academic-priority claim.

**Honesty gate:** the earlier source-certified pair contributes a positive rank≤2 kernel `2cos(gamma(x-y))` with midpoint operator error <=8a²/500, but all other zeros of height <=T remain unclassified. Their signed middle contribution cannot be discarded. Even a zero high tail with positive first pair leaves an exact finite toy negative-middle countermodel. An all-height sign or source-positive factorization of the original Weil form is still required for RH.

**Controls:** fake independent six-prime data fail original source provenance, receipt hash mutation refused; wrong-half-density/pole/contact invariance is not presumed; concentrated bounded-H¹ tent refutes overgeneralized six-derivative obstruction; source-free generic signed form with invisible negative middle remains negative; no numerical zeta-zero inputs.

**Files:** `observational_succ/signed_weil_h1_tail.py`, `tests/test_signed_weil_h1_tail.py`, `scripts/signed_weil_h1_tail_probe.py`, exact frozen JSON and `research/2026-10-14/SIGNED_WEIL_H1_SPECTRAL_TAIL.md`. No new physically certified observer instrument; no Lean kernel proof. Dedicated CI and full repository checks must be read from the exact branch head before claiming success.

**Next missing lemma:** a source-derived lower bound on the *unknown finite-middle signed spectral form*, or a complete original arithmetic prime/Gamma/pole all-vector inequality; the present high-tail theorem is not that bound.
