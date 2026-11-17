# Calibration and correction history

1. The first isolated test invocation reported **8 PASS / 1 FAIL**: `test_prime_character` expected `c_30(6)=+2`, while the implementation returned `-2`. The signed local decomposition gives `c_2(6)=1, c_3(6)=2, c_5(6)=-1`, hence the correct product is `-2`. The expected value was corrected; the production code was not altered for this failure. The original terminal failure was observed, not preserved as an output file; this note is a faithful reconstruction of that outcome.
2. A separate exact SymPy Bernoulli audit and a differently implemented Fourier character sum independently verified `c_30(6)=-2` and all committed sign conventions.
3. The primary module was minimally hardened to use integer `isqrt` rather than floating square-root truncation for its elementary prime verifier. This change was made before the final passing local tests.
4. Final passing receipts: `TEST_LOG.txt` and `AUDIT_LOG.txt`. They are isolated local tests of the exact files in this dossier, not full repository tests, a Lean proof, or outside refereeing.
