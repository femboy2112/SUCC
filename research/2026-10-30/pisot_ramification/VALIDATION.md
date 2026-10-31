# Validation — NonPisot/Pisot ramification, 2026-10-30

**Source boundaries:** pure toy recurrence research stacked on PR #416 at 725377a64748ab0c442d16a61509b99687412505; authentic original BBP forcing, U0=0, source and main unchanged.

**Actually executed independent exact SymPy source:** independent_oracle.py, byte-matched to remote Git blob a98d20b3b6b180b16804f124d7261176bdf347ad. PASS after one calculation harness repair. Checks original quadratic and cubic characteristic polynomials, irreducible cubic field setup, exact integer matrix B=2I+A+A², B^(-1)=2I-A, det B=1, unimodular integral-basis change, identical discriminants -255, exact factorization 3·5·17, complex conjugate bounds and non-Pisot affine-shift obstruction, 22 degrees of strictly positive coefficientwise Fibonacci/length-3 Pisot grammar decomposition.

**Additional locally executed independent numerical/exact checks:** full SymPy matrix polynomial and inverse identities, field-discriminant and basis tests, positive grammar expansions at lengths 2 and 3 through degree 24, and 29×29 quadratic positive recurrence parameter family with nearest-integer Pisot shifts. All PASS. A second 2x2 positive matrix with both conjugates >1 refutes the naive nonnegative-coefficient P(A) universal claim.

**Prepared stdlib regression probe:** pisot_ramification_probe.py contains 14 exact integer/Fraction test methods, committed to this branch for replay. Its SHA 7a8f240b065925a25dcb2178a0e132a3a8d21f71 was verified by remote GitHub fetch. **The complete committed 14-method source has NOT been executed byte-for-byte in this environment.** Do not claim 14/14 test pass merely because its independent mathematical calculations succeeded.

**Disclosed repairs:** The first independent oracle used unrestricted symbolic expansion of high powers of a rational generating function, causing a timeout. Replaced with finite exact coefficient convolution and reran to PASS. An initial inert vacuous assertion was removed before uploading the final byte-matched source. No mathematical theorem status was promoted on the basis of those failures.

**NOT RUN:** complete root AGENTS provenance, 10k+ repository unit suite, observer/ordinal probes, hosted CI, Lean, independent external math review. Field theorem in PR-05 is known published prior work, not a new discovery. This finite toy treatment supplies no original-source zero-seed pi-normality estimate or RH proof.
