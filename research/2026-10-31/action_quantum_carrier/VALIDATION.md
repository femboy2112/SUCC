# Validation and provenance receipt — action quantum carrier

**Parent branch:** `research/unit-succ-pascal-gamma-seam-2026-10-31`, exact SHA `7833a238012bb8e70ff363a3bcf6d60354ecb795`. Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`. Original 4 signed BBP poles, literal U0=0, frozen proofs, production, `formal/`, workflows untouched. Files are additive and research/test-only.

**Executed locally, stdlib Python3, exact rational/integer arithmetic:**

```
python -m unittest discover -s tests -p 'test_action_quantum_carrier.py' -v
```

**35/35 test methods PASS locally, exit zero**. No floating-point assertion or phase rounding is used in this suite. Representative scopes:

- Complete 16^3 finite digit partitions and orthogonality, 16-th successor vs all carry channels, full first-level 16x16x16 Weyl exponents, refined clock scalar congruences.
- Original four poles against a combined rational source and separate convolution oracle at n<=100; odd denominators; two independently written exact modular residue algorithms (modular pow inverse vs Euclid), source carries through r=4 and n<=22; source initial r(1)=47/15 with digit1,carry14.
- Exact local/real nonfactor witness for r=1..5 and Eisenstein polynomial norm `(1-zeta_3)(1-zeta_3²)=3`, no float trigonometry.
- All algebraic Pisot division digits on [-12,12]^2, matrix square, unit norm and parity quotient, no fourth-root characters on `(Z2)^2`.
- Finite graph kinetic scaled-stride intertwinement for every branch and every coarse basis state at r=1,2; independent second-power graph operator; native fine kinetic failure; exact symplectic determinant/dual-momentum counterexample.
- Original BBP canonical symplectic source recurrence, `p_n=16^(-n)`, exact action sum `U_n/16^n` via **three** arithmetic paths, positive source increment and failure under naive unscaled momentum. One initially malformed test oracle attempted to unpack three values from a two-value map; it was corrected and rerun, retaining the final passing receipt.
- Sharp subgroup-support saturation in Z16 and (Z2)^2; algebraic exact cyclotomic Phi16 character sum versus independent modular annihilator; invalid input and false support floors.

**Independent finite methods:** combined polynomial rational source vs four signed poles, recurrence vs closed finite rational convolution, modular inverse by extended Euclid vs Python `pow`, kinetic sparse-basis action vs second independent linear-combination stencil, cyclotomic polynomial vector vs modular character annihilator, Pisot matrix vs algebraic multiplication. These share the declared mathematical carrier/source inputs and are not independent scholarly proof witnesses.

**Paper proofs** in PROOFS.md cover universal group/basis identities, support uncertainty, local→real no-factor, and Pisot second-level quotient. No external mathematical referee and no new Lean kernel run. The suite tests finite instances and guards implementation, not a universal normality theorem.

**Additional compatibility replay:** Three preceding locally available PR research packages (#438, #439, #440) were extracted into the same isolated test root without modifying their file contents. `python -m unittest discover -s /mnt/data/succ_action_quantum_round/tests -p 'test_*.py' -q` reports **117/117 methods PASS in one process**. This verifies the local combined snapshot, **not the full GitHub repository** or hosted CI.

**Independent symbolic check:** SymPy 1.14 independently simplified the original four signed poles to the odd-denominator combined numerator, computed the Pisot multiplication matrix determinant and characteristic polynomial, and checked the unimodular `beta²/2` matrix; PASS. This is still a derivation from shared mathematics.

**Not run locally:** all 10k+ SUCC root tests, `scripts/verify_provenance.py`, observer-foundations/ordinal probes, or a complete local Git checkout (container network DNS inaccessible). Check hosted GitHub exact-head CI after draft PR creation; no imaginary CI success.
