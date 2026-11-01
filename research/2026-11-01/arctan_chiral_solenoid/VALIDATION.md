# Exact validation and limitations: original BBP arctan–chiral solenoid bridge

**2026-11-01 final source bytes.** This document records actual executed probes, their hypotheses, known tool limitations and repairs. No full SUCC repository suite or Lean kernel run is inferred from these receipts.

## Direct exact tests

```
python -m unittest discover -s tests -p 'test_arctan_chiral_solenoid.py' -q
# Ran 65 tests in ~0.28 s — OK

python research/2026-11-01/arctan_chiral_solenoid/symbolic_probe.py
# PASS: source isometry, 2-adic derivative residue classes,
# Gaussian integer Machin factor, SU(2) inversion, angular orientation,
# full source Mellin→angular+coboundary identity, original vs completed j.

python -m compileall -q research/2026-11-01/arctan_chiral_solenoid tests
# PASS
```

The exact test suite covers: original signed four poles vs independent combined rational source for negative and positive integer time indices; entire source residue permutations at Q=16,256,4096,65536 (all 69,904 residue evaluations, full enumeration not sample); source mod16 parity formula; derivative 3/11 congruences and higher-clock modular Taylor; complete 256-entry K16 matrix in Z[zeta16] via two distinct algorithms; independent character orthogonality; positive extra-pole source-mutant Fourier changes; projective reciprocal/Cayley algebra; unwrapped chiral forward carries; non-independent joint Fourier correlation; original vs dual source denominator classes; odd-torsion solenoid embedding, unique [4] inverse and commuting naturality square; halfturn history kernel; fractional-source character shift; finite even 2Q chiral coset permutations at Q=15/4095; DFT² parity; exact Gaussian integer Machin factor and two independent rational Machin bounds; true four-pole P(t) Mellin coefficient integration; P/(16-t^8) rational reduction; the exact angular-plus-coboundary differential; zero-boundary log potential; positive beta mutant; separate Machin/BBP rational brackets; Cauchy Jacobian identities; 2-adic to real source-phase noncontinuity controls.

## Independent symbolic route (optional SymPy)

The symbolic implementation is separate from the stdlib helper. It checks:

1. `H(x,y)=(A(x)D(y)-A(y)D(x))/(x-y)` is an integer polynomial, identically odd mod2.
2. Derivative congruence numerator modulo16 reduces to `8x(x+1)`, divisible16 on Z2.
3. All 16 base source and derivative residues.
4. Gaussian identity `(5+i)^4=2(1+i)(239+i)` and `i sigma_x` is SU2.
5. `P/(16-t^8)=(1-t)/((2-t²)(t²-2t+2))` and source density `=(1/8)eta+dG`, including `G` endpoint zero.
6. Definite original completed integral equals `pi/16` by direct primitive.
7. Source-index four-pole cross ratio `8/5`, `j=470596/225`; completed Mellin t-pole cross ratio `-1`, `j=1728`; no direct Möbius pole-set equivalence.

These are exact symbolic identities, not numerical approximate equalities; they are still not Lean-kernel machine proofs.

## Combined research-snapshot integration proxy

14 pre-existing research ZIPs supplied in the conversation are available as source/test snapshots. 150 unique research/test paths were loaded without conflicts from those archives; the 14 new package files were overlaid in their own paths. No full GitHub checkout was available from the container. The previous research snapshots contributed **539 tests**; the new suite added **65** for **604 total tests**.

```
python -m unittest discover -s /mnt/data/succ_arctan_chiral_integration/tests -p 'test_*.py' -q
# Ran 604 tests in 2.146s — OK

# Independently enumerate and reverse discovered test-method order:
# Ran 604 tests in 2.074s — OK
```

These share Python, tests and original mathematical source; reversing order checks import/cache sensitivity, **not** independent proof authority. They are not the original repository's >10,000-test integration suite.

## Negative controls and source-map failures

- **REFUTED:** source-time 2-adic Fourier Haar implies selected real-circle Weyl cancellation. The true source phase `n->e(r(n))` admits no continuous Z2 time extension (`1+16^j ->1` 2-adically but its real phase tends to 1, unlike e(r1)).
- **REFUTED:** chiral arctan is independent second Fourier witness. Exact `Sdual=(-1)^h conjugate S`; joint `(h,h)` mode is exactly `(-1)^h`.
- **REFUTED:** native global `x->16x+b` is a permutation of even clock 2Q; gcd(16,2Q)=2. Two separately labelled Q-point torsors repair the valid part of the analogy.
- **REFUTED:** four original rational SOURCE-index poles can simply rotate by a Möbius map to the completed Mellin rational t-plane poles; j-invariants are unequal.
- **REFUTED:** original four-pole completed angular period is generic for every positive/source-altered Mellin density. An explicit extra positive Beta(8n,9) mutant changes the period strictly.
- **REFUTED:** universal invariant Cauchy measure forces the actual zero-seeded orbit to be normal; unchanged forcing q=1/5 is a coherent nonnormal orbit.
- **OPEN:** a new signed all-horizon estimate for original `S_N(h)`/Main XVIII Fejer lag. No such saving was proved or is claimed by this package.

## Failures, corrections and reproducibility debt

The first pass of the finite chiral-coset code mistakenly attempted to invert the fraction denominator modulo Q even though Q is a MULTIPLE of that denominator; the corrected code computes the integer source label `Q*r` as required. The two affected tests initially errored, then the final exact suite passed. Some inert test scaffold checks were removed before the final test-source hash. No post-hoc harmonic/horizon selection, numerical tolerance fitting or assertion weakening was used to conceal a falsified mathematical result.

The combined snapshot suite is a partial integration proxy. It does not run `scripts/verify_provenance.py`, the complete root unittest suite, `observer_foundations_probe.py` or `ordinal_succ_report_probe.py` from a full repository checkout. Hosted exact-head CI is a separate source of validation and must be observed after the branch is pushed. Source oracles share the four-pole mathematical identity, and optional SymPy is not an independent mathematician/external referee. No new Lean declaration or physical quantum experiment is claimed.

**Source provenance**: SUCC Main XVIII at `4eb411e3730a9e7b95480369a438b89d9a433a4b`, stacked PR #448 at exact parent `74de5c986c5bce2e8486450ce6475b3b6c1f68e0`, original rational source unchanged. All new files research/test additive only.
