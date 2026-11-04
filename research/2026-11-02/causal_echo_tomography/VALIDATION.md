# VALIDATION — causal echo tomography, source-conditioned countermodels

**Parent:** Exact draft PR #466 head c71b18dba200c2d227d9c084bbb9d8399f81ede3; stacked on #464/#463/#462/#460/#459 and Main XIX. Only ADDITIVE research and root test files, no frozen source, default branch, historical theorem contract, formal Lean or production change.

## Actual executed local exact arithmetic

The **final exact byte-identical GitHub standalone source** was executed locally:
~~~sh
python research/2026-11-02/causal_echo_tomography/causal_echo_probe.py
~~~
Local result: **9/9 pure-stdlib unittest methods PASS**, 0 skips, about 0.743 seconds; original four poles versus combined rational source n=1..29; all polynomial moment-null constraints for M=1..6; zero-seed source/state exact equality through M; all original/altered integer unit jets 95%-105% on a finite grid; rational atomic M=4 weights, source values and rational completion; Machin rational π enclosure; exact Green finite path; and complete causal pair Fourier angles through M for TWO changed-source controls.

Final uploaded Git blob fetched back and compared with locally executed git hash-object:
- causal_echo_probe.py = 87818af8c4025880269c3fa1ead1a22823a22922, **MATCH**.

**Rational atomic M=4:** 4 positive rational weights match original r(1)..r(4) and U0..U4 exactly; completed q=4062342947075618/20689342837729335. The fourth moment certificate and rational q are exact independent of any normality test.

**Exact causal echo:** for M=4, ε=1/(1000 B_4), chosen rational and satisfying a pointwise 95%-105% original source-density inequality, the first four rational states coincide. At n=18, the actual lifted difference modulo one has exact circle distance
\[
260840294718179115804391693/837084962009298606489600000
\]
strictly between 1/4 and 2/5.

## Independent symbolic route

~~~sh
python research/2026-11-02/causal_echo_tomography/independent_symbolic_oracle.py
~~~

**SYMPY_INDEPENDENT_EXACT_PASS.** The independent routine uses SymPy's symbolic differentiation/integration and matrix inversion, instead of the main oracle's Fraction polynomial convolution. It independently recovers:
- all vanishing moments and first nonzero source moment for M=1..6;
- the EXACT M=4 state-18 fraction above;
- the positive rational atom weights from the four original source moments and q above.

The uploaded SymPy file's verified remote SHA-1 Git blob equals locally executed source:
- independent_symbolic_oracle.py = 908946d6711bca6d4e62a11f268d4483c8efa010, **MATCH**.

These are two implementation routes in one assistant session, NOT an external blind mathematical proof check.

## Failed attempt preserved

The first exact-rational atomic test asserted a false over-tight bound \(T_n<(1/2)^n\) although a positive atom sits at \(x=63/80>1/2\). This produced ONE failed local test. The bound was repaired to \(T_n<(63/80)^n\), justified by total mass 47/15 and \(\sum_i w_i/(16-x_i)\le47/225<1\). **The final run then passed all 8 tests**, followed by a ninth exact causal-Fourier prefix-identity test, and the 9/9 run is the final locally tested source.

**New generalized weight-span theorem (CE-05B):** paper proof uses independent continuous evaluation functions and k+1 disjoint smooth compact bumps to construct a finite linear-system nullspace witness. This is a mathematical finite-dimensional linear algebra / approximation argument, NOT an unperformed numerical general-rank experiment. The original explicit ψ_M test is its polynomial-source special case. The theorem is for finitely many LINEAR source observables; it is not a claim of arbitrary nonlinear or exact four-pole model indistinguishability.

**Exact relative-period theorem (CE-05C):** the same symbolic positive integral β_M from CE-02 yields the endpoint primitive difference. This is a paper-level 1D de Rham boundary statement, NOT a separately executed Lean cohomology verification or new physical curvature. The original endpoint-vanishing AC-13 identity is an inherited #452 theorem; our intentionally changed source has nonzero endpoint period.

## Root-discoverable integration adapter, staged verified

The NEW root adapter tests/test_causal_echo_tomography.py was also placed in a local miniature checkout with the exact locally tested source under its correct relative research/ path. The command
\[
\texttt{python -m unittest discover -s tests -p 'test_causal_echo_tomography.py' -v}
\]
executed **9/9 PASS** (0.681 seconds), with all methods discovered and no import/path skip. GitHub re-fetch matched the executed adapter's local Git hash:
tests/test_causal_echo_tomography.py = 7d6678def3f1de81d335659c6e1aeb8a04ccfdb5 (**MATCH**). This is a *staged adapter test*, NOT a claim to have executed the full actual SUCC checkout.

## Paper proof versus finite checks

The quantified arbitrary-M compact ψ_M bump, pointwise 95%-105% density inequality, all-(n,d) complete monotonicity, entire time correction, and norm/normality control are **paper derivations** in PROOFS.md. They do not follow from M<=6 test loops. The arbitrary-M rational-positive quadrature theorem uses the rational interior convex-hull argument; the independent exact M=4 example only checks an instance. A known base16 normal q is selected by a classical rational translate of Champernowne; the parameter ε may be irrational, so the altered normal/nonnormal source *is not necessarily rational valued*.

**NOT RUN / NOT CLAIMED:** genuine full SUCC 11k+ checkout suite, root AGENTS.md provenance/foundations/ordinal, new Lean declarations, hosted exact-head CI success, independently blind external proof review, any original-source all-X signed Weyl saving or π normality. The local container cannot clone GitHub via its network, so source files were uploaded through the connected GitHub tool. Reproduce the full suite and check hosted CI on the exact PR head separately.

## Reproduction from repository root

~~~sh
python research/2026-11-02/causal_echo_tomography/causal_echo_probe.py
python -m unittest discover -s tests -p 'test_causal_echo_tomography.py'
python research/2026-11-02/causal_echo_tomography/independent_symbolic_oracle.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
~~~

No historical claim-status promotion, publishing, merge or tag is authorized.
