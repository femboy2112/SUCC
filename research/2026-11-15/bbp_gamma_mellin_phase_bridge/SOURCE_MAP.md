# Provenance, source interfaces and independence

- **Original BBP forcing / zero seed:** [SUCC maintained source](https://github.com/femboy2112/SUCC/blob/main/observational_succ/duck_bbp.py), Main XXV `docs/PI_NORMALITY_FRONTIER.md` and `docs/PI_FRONTIER_CONTRACT.md`. Original donor import manifest in `provenance/IMPORT_MANIFEST.json` at main; none of these files is modified.
- **Previously established Gamma-source endpoint and bounds:** [Gamma Genesis #634](https://github.com/femboy2112/SUCC/pull/634), especially GG-05/06, `I_m` rational bounds and TV `<=7/m`. Current GM-03 adapts that envelope to the different exact log-source coordinate `Y=-8n log X` and extends the joint character to `exp(-i xi Y)Y^(i omega)`. Shared source denominator means these are dependent mathematical arguments, not blind independent witnesses.
- **Gamma causal semigroup:** [SUCC #638](https://github.com/femboy2112/SUCC/pull/638) and [SUCC #66](https://github.com/femboy2112/SUCC/pull/66). Those Gamma stages are a distinct stochastic observer carrier; this dossier does not assert that the BBP physical source actually generates exponential waiting times.
- **2-adic zero anchor / signed time holonomy:** [SUCC #646](https://github.com/femboy2112/SUCC/pull/646), [#648](https://github.com/femboy2112/SUCC/pull/648), [#649](https://github.com/femboy2112/SUCC/pull/649). The original index-dependent signed real phase is not discarded in the proposed follow-up.
- **π target lifted to an expectation:** [SUCC #651](https://github.com/femboy2112/SUCC/pull/651). `x=E C=pi/16`, `T_n=E[C tau^(8n)]`, and the biased reordering `E[e(h C)]` control originate there. This research is an additive child, not a rewrite.
- **Classical Gamma analytic facts:** [NIST DLMF §5.2](https://dlmf.nist.gov/5.2) for Euler's integral, meromorphic continuation and zero-freeness; [DLMF §5.11](https://dlmf.nist.gov/5.11) for exponential high-frequency attenuation.

## Validation provenance

`gamma_phase.py` is the numerical implementation of the declared exact BBP source, not an oracle for pi normality. `test_gamma_phase.py` uses finite source Fractions and high-precision quadrature. `independent_audit.py` does not import `gamma_phase.py`; it independently implements the original rational source algebra and t-domain integrals, including a positive endpoint mutant. All implementations are **same-session / same-model** and do not count as independent mathematical refereeing.

The all-frequency Gamma2 TV rate reuses an inherited GG-06 rational beta lower bound, not an independently discovered primary theorem. The complex two-axis Watson expansion, exact phase transport, and four-time q/n crossover are paper derivations to be independently reviewed. No new Lean kernel result is asserted.
