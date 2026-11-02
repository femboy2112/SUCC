# Operation Riemann-Sphere BBP Path Seam — research-only

**Parent:** SUCC PR #441 at exact head `ab87a8d825d41dce846da2d93e776e2c760e9bf1`, stacked source program. Original four signed rational poles and `U0=0` unchanged. π normality and RH remain OPEN.

**Motivation:** Can the finite unit-SUCC, symplectic action, and real-circle character be source-authentic readouts of related paths on a Riemann sphere? **Answer, with scope:** for every finite horizon N there is an explicit rational one-form on the sphere whose contour integrates to the original BBP partial action; its exponentiated period is the same real-circle phase. The four original source poles define a logarithmic differential. Noncommutative actual path ordering is *not* recoverable from this Abelian period alone.

## Results

- `RSP-01`: exact logarithmic original source one-form, four punctures with residues summing zero, source cross ratio 8/5 and a genus-one double-cover model with j=470596/225.
- `RSP-02`: exact finite Newton/Pascal sampling polynomial, rational meromorphic one-form `Omega_N`, contour equals original finite BBP sum = source symplectic pairing; exponentiated contour recovers the selected real-circle character.
- `RSP-03`: global residue theorem splits the same action into source-pole residues plus an explicitly computable infinity residue; exact independent Laurent/moment formula.
- `RSP-04`: enlarging N adds exactly one sampled pole; old residues persist. Source/infinity complementary residue changes by the negative original SUCC increment.
- `RSP-05`: original source-pole side grows as +log(N)/8; infinity residue as −log(N)/8, with exact Euler–Mascheroni/π/log algebraic finite part.
- `RSP-06`: decisive source-original 2-step affine noncommutativity (12301/273) invisible to a scalar contour integral. Retain the history in a separate path-ordered object.
- `RSP-07`: no all-horizon signed Weyl saving or new RH theorem. A contour identity is not a path-space integral or a normality proof.

Run `python -m unittest discover -s tests -p 'test_riemann_sphere_path_seam.py' -v` from a full checkout; focused tests are self-contained. See [PROOFS](PROOFS.md), [CLAIMS](CLAIMS.md), [NEXT](NEXT.md), [VALIDATION](VALIDATION.md).
