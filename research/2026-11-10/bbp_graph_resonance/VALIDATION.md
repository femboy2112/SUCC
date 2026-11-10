# Claim authority and replay — BBP graph-resonance research

- **Parent:** `3f1b67d6c319bf4ee9f42941da829cd1f778a3af` (PR #579 source-first fold); no files from the parent modified.
- **Environment:** Python 3.13.5; SymPy 1.14.0.
- **Executed:** `python /mnt/data/bbp_graph_shapes_probe.py` on the local exact symbolic source; exit 0. Output:
```text
Exact BBP computational graph: all 21 assertion families PASS
Source resonance resultant = -(z - 1)*(16*z - 1)**4
Reduced root = 16*(x - 1)/((x**2 - 2)*(x**2 - 2*x + 2))
Holonomic identity: Π(8θ+a) Φ(z) = 8(16z²+177z+47)/(1-z)³
Disjoint decimated source pole sets: 25
Hostile resonance source P_fake(x) = (x - 1)*(x**2 + 2)*(x**2 + 2*x + 2)*(8*x**4 - 17*x**3 + x**2 + 34*x - 38)/80
Its analytic fixed point integral = 1 ; endpoint zero and positive on [0,1)
Nonnormal 2-cycle alpha=1/255 has Fourier mode h=255 identically 1
No π normality/parity decay has been proved.
```
- **Re-run:** `python research/2026-11-10/bbp_graph_resonance/bbp_graph_shapes_probe.py` with SymPy installed.
- **Scope:** R-01/R-02/R-03/R-05/R-06 are paper identities plus same-algorithm SymPy tests, not independent refereeing or Lean kernel proofs. R-04 is a standard probability-measure resolvent identity. The algebraic BBP partial-fraction shortcut is classical.
- **Countermodels:** R-04 periodic orbit α=1/255; R-05 same-resonance, positive quadratic-decay integral-1 source; R-06 exact oscillator no-gain identity.
- **Tests not run on this pushed branch:** full SUCC unittest suite, provenance script, observer foundation/ordinal probes, hosted CI exact head, independent oracle implementation.
- **Verdict-changing probe:** Derive a zero-seed-only Fourier cancellation or carry/winding/moment intertwiner that fails on both the R-05 fake source and PR #579's source-compatible wrong-seed controls. No representation or fixed-point uniqueness alone discharges this.
- **Claim status:** π normality, original-zero parity and RH all OPEN.
