# Zero–One SUCC research validation scope — 2026-10-27

**Parent context:** SUCC PR #335 (log Dirac/sawtooth source) read via authenticated GitHub; original signed four poles and U0=0 preserved. This is a new *additive* research module, not a direct edit of any existing source or proof.

**Local execution:** Python 3.13.5, standard-library fractions.Fraction, unittest and isolated namespace.

- python -m unittest discover -s tests -p test_bbp_zero_one_characters.py -v: **15 tests discovered, 14 PASS, 1 SKIP** (the isolated tree has no native SUCC module succ_internal_matrix_walk; its native-source comparison must run in the actual repo). Raw log in ZERO_ONE_FOCUSED_TEST.log.
- python scripts/bbp_zero_one_probe.py: **PASS**. 256 original signed four-pole/Mellin moment exact identities, 25 finite 0/1 jet counterfeit controls, 294 eventual 2-adic source isometry checks, 22 formal-evaluation discontinuity witnesses. Source-selected beta=1/16. Receipt: ZERO_ONE_EXACT_PROBE.json.
- Both depths 1 and 2 of the mutant's complete 16/256-residue cycle passed exact rational modular enumeration; original q=0 coefficients and q=1 finite polynomial jets were compared with independent exact oracle identities.
- Source module/test/script compiled successfully with python -m compileall.
- An independent mpmath 65-decimal-digit numerical evaluation of the genuine Mellin integral verified G(1/16)=pi, G(1)=R, and the renormalized slope d to the expected O(s log(1/s)) numerical rate. These are numeric corroborations only; the dossier supplies the proofs.

**Not run:** the full native SUCC test suite; provenance, observer foundations and ordinal probes; hosted GitHub CI; Lean; external blind peer review. No assertion about mathematical novelty or π normality.

**Theory authority:** direct elementary exact proofs for the mutant, formal completions, polynomial coefficient maps and rational bounds; classical Gauss digamma/polylogarithm/ideal-adic facts are cited. A numerical probe is not a proof of any infinite limit. False shortcuts are retained as REFUTED claims.
