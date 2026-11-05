# Validation and reproducibility — Gamma sphere solenoids (2026-11-05)

**Scope:** New additive research branch based on SUCC draft #513 at exact parent `727a97a006e929243e0fee1ab44cf52dc68e2c8f`. No modifications to original BBP forcing, its literal zero seed, source contracts, Lean, production, historical tests or main.

## Executed local test run (not an exact checkout of the full 12k+ repository)
Tests were authored as three standalone files, executed using **Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0**, and their Git **content blob SHA hashes were reconciled with the committed GitHub files**, avoiding a mismatch between tested code and committed code. The full repository has NOT been cloned or run here.

```
cd /mnt/data/succ_sphere_round
python -m unittest discover -q -p 'test_gamma_sphere*.py'
----------------------------------------------------------------------
Ran 19 tests in 10.913s
OK

python -m compileall -q .
# exit 0
```

Exact locally executed bytes vs remote GitHub blob SHA:

| Repository file | Independently verified Git blob SHA |
|---|---|
| `tests/test_gamma_sphere_solenoid.py` | `eda3138ffeae14b5b60f5936ee5b4cd92c392c6a` |
| `tests/test_gamma_sphere_branchlift.py` | `e88a083fb0e909a1990b1194aba90e42c0ed469a` |
| `tests/test_gamma_sphere_torsion_lift.py` | `7bc510b7a10af03e875eca01b1ab3bec8ccb3184` |

### Instruments and control scope

- **Exact SymPy rational/algebraic:** original P_o/D_8=K_a+K_r, Gaussian u8=1/16, rational W semicircle, chiral log derivatives and residues ±√2,1±i, exact Beta Jacobian X(t), SU(2) Möbius projective 8-step composition, nonzero commutator and sphere metric.
- **Source-sensitive Fraction controls:** original U0=0 and three inherited angular/radial forcings at n=11,19,37; original odd-denominator source through n=80; source one-tap mutation and coherent wrong seed `-T_n` (without using digits of π as an input). The analytic identities persist for same-forcing wrong seed.
- **Gamma 35+ digit diagnostic:** independent periodized density quadrature vs Gamma Fourier coefficients at k=0,1,3,4,8. Nonzero k=1 coefficient magnitude approximately 0.107343569604. This nonzero value REJECTS Gamma-induced Haar.
- **Finite-cyclotomic controls:** 25 ordered pairs of cyclotomic polynomials with m,n in {1,3,5,7,9}; resultant is nonzero, validating small odd-torsion deck rigidity. The ALL-odd-order theorem is argued by prime-reduction in ARITHMETIC_DECK_RIGIDITY.md, not inferred from finite tests. Even-order mutant J(-1)=i succeeds, proving the odd-order hypothesis is essential.
- **Distribution countermodels:** complete input root grids of sizes 53,97; output S-sphere Fourier characters approach `eta^h` (Poisson law, NOT Haar); J-flipped grids produce same S observations but nonzero original first Fourier moment; odd-order approximate lifts with conductor `2N^2+1` reproduce arbitrarily near-equal sphere observations while retaining nonHaar source distribution. These are finite diagnostics plus independent analytic limiting reasoning, not proof of selected arithmetic normality.

### Development failures transparently retained

1. An early **affine** sideways Möbius iteration raised a division-by-zero error at iteration 4 for z=3/5: the correct map passed through the point at infinity. Replaced by homogeneous `CP^1` matrix iteration. Exact projective identity then passes; the pole case is retained as a regression control.
2. A finite root-grid convergence tolerance was initially too tight (a nonzero O(c^N) finite-grid residue). Calibrated finite-grid tolerance for N=53 separately from N=97; the analytic target is derived independently through the holomorphic mean-value property. No finite discrepancy was suppressed by claiming exact numerical equality.

### Authority boundaries

Claims GS1–GS8, DL1–DL10 are **paper algebra/analysis** backed by independent local finite probes but not Lean-kernel certified or externally reviewed. There is **no full original SUCC native/hosted CI pass claimed** for this branch, no independent global novelty verification, no new signed source Weyl estimate, no base-16 normality proof, and no RH proof. Gamma non-Haar, deck instability and same-forcing wrong seed are adversarial falsifiers. Other historical SUCC test results are inherited, not rerun.
