# Claim supplement: Tate finite-S lattice and observer descent (2026-10-15)

**Branch:** research/tate-lattice-finite-global-descent-2026-10-15, parent main@03db442.
**Dossier:** [TATE_LATTICE_FINITE_GLOBAL_DESCENT.md](../research/2026-10-15/TATE_LATTICE_FINITE_GLOBAL_DESCENT.md).
**RH PROVED: NO.** This work is a classical adelic representation layer for SUCC, not an original proof of the product formula or of any zeta-zero assertion.

| ID | Exact statement and hypotheses | Status | Receipt / limitation |
| --- | --- | --- | --- |
| TL-01 | For finite genuine prime S, Gamma_S=Z[S^-1] is discrete cocompact in G_S=R x product Q_p, and the Haar-covolume is 1 under standard normalizations | CLASSICAL / PAPER PROOF | Principal part representative in [0,1) x product Z_p; full topological carrier not code-generated |
| TL-02 | With opposite real / finite Fourier phase signs, Gamma_S^perp=Gamma_S and (X_S)^=Gamma_S | CLASSICAL / PAPER PROOF | Exact annihilator argument using tests 1/p^k, all k; code finite holds on rational charts |
| TL-03 | q an S-unit implies qGamma_S=Gamma_S and Delta_S(q)=1, yielding Q product formula | CLASSICAL (Tate/Poonen) | Positive finite Haar-covolume / Poisson scaling; arithmetic check is not a new analytic proof |
| TL-04 | Delta_S(q)=product outside S ell^v_ell(q); for q in Gamma_S, [Gamma_S:qGamma_S]=Delta_S(q) | CLASSICAL / PROVED LOCAL | Exact 30 with S={2,3} defect 5; 1/7 not a valid lattice endomorphism |
| TL-05 | Principal-part bonding maps X_T -> X_S preserve quotient classes and all q in Gamma_S characters; nested composition is coherent | CLASSICAL / PROVED LOCAL RATIONAL CHARTS | Exact seeded holdouts, 2-adic character deletion negative control |
| TL-06 | inverse_limit_S X_S is naturally A_Q/Q as a compact group using dual limit of Gamma_S=Q | CLASSICAL THEOREM IMPORT | Pontryagin duality, adelic self-duality; NOT a finite physical completion |
| TL-07 | For any p and depth k, nonzero class (0,p^k) aliases zero for all j/p^r (r<=k), but not r=k+1 | PROVED LOCAL / EXACT FAMILY | Finite character-depth proof; no claim of logical undecidability |
| TL-08 | A nonzero Gamma_S SUCC displacement changes its lift but not its quotient point, so pure-quotient state encoding cannot be faithful to source histories | PROVED LOCAL / EXACT COUNTEREXAMPLE | Signed transition cocycle/lift must be retained |
| TL-09 | Arbitrary SUCC source histories and operators admit a history-faithful, analytic Tate/Weil functor | HYPOTHESIS / UNVERIFIED | Need construct functor and compare actual source event laws |
| TL-10 | Source-derived completed Weil form is PSD on entire legitimate test space | UNVERIFIED, RH-HARD | No construction or proof from TL-01–TL-09; preserve fake-composite and non-Euler controls |

## Steelman / crucible / verdict

**Steelman:** Additive Fourier phase compatibility and the discrete arithmetic lattice provide the missing mechanism for multiplicative reciprocity, while recursively compatible finite-place observer models have a canonical global object.

**Crucible:** Additive phase cancellation by itself cannot force the Jacobian. Haar scaling, compact quotient, and lattice preservation are essential. Naive dropping of p-adic coordinates breaks Fourier naturality. The quotient alone erases nontrivial SUCC events. Finite-depth characters can hide nonzero states arbitrarily long. An S-stage positive number is not the completed Weil quadratic functional.

**Verdict:** Classical exact local/global construction, useful typed SUCC interface and a sharper historical-data obstruction. No RH implication beyond the established Tate functional-equation route.

## Validation scope

Isolated local tests performed against a temporary local copy of the existing prime/principal-part helper interface; the full repository suite and independent CI require checking the committed branch. Run:

    python -m unittest discover -s tests -p 'test_tate_lattice_descent.py' -v

Also run the mandatory repository gates listed in AGENTS.md. Tests exercise a dense **rational** submodel, not all p-adic real/analytic topological statements.

## Primary provenance

John Tate (1950 thesis, Chapter XV, Cassels–Fröhlich 1967); Bjorn Poonen, *Tate's Thesis*, MIT 18.786 (2015), §§5.2–5.7: https://math.mit.edu/~poonen/786/notes.pdf.
Existing repo source: observational_succ/diagonal_adele_zeta.py and its prior exact reciprocity theorems; do not assign these classical facts new academic priority.
