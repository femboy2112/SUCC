# Focused validation — gauge-coded sphere tower + optional quantum spectra

**Executed on 2026-11-05.** Standalone Python stdlib tests in \`tests/test_gauge_sphere_spectral.py\` were executed in the container with \`python ... -v\` twice, including after improving the projective/homogeneous section controls; **10/10 PASS**. \`py_compile\` PASS on the first version. Final committed test blob SHA **\`e3bc44de4f5d96f23b1095b0a19269b393bfdcc8\`** was matched to the locally executed bytes by \`git hash-object\`; this confirms the actual focused file was run, not only a similar reimplementation. No test run of all SUCC imports, full native 12k+ suite, Lean, CI or formal proof kernel is claimed.

Tests cover:
- authentic four signed BBP poles vs the independent collapsed rational source for n=1..26; exact unwrapped zero-seed recurrence; odd denominator contract;
- direct forward circle map composition n=1..3 versus \`U_n\` phase, projective fixed endpoints 0/infinity;
- finite rational future-tail boundary gauge identity with exactly aligned truncation horizons (not using a numerical pi oracle);
- homogeneous section monomial degree/spacing and source coefficient \`e(jU_n)\` transport;
- Fubini–Study curvature equality for source phase rotations, d=1,16,256 on three distinct complex chart points;
- chosen constant-curvature monopole energies, spacing and degeneracy for d=1,16,256,4096 and first five Landau levels;
- fixed round sphere scalar eigenvalues, source- and degree-independent;
- direct-limit character label consistency and inverse-square gap collapse;
- exact odd-order inverse 16th root and noncontinuous branch selection (m=16k+1).

Independent numerical calibration (not an interval proof) with **mpmath at 45 decimal digits**:
\`2d²*quad[r^(2d-1)/(1+r^(2d))², r=0..infty]\` recovers \`d=1,16,256\` at displayed 30 digit precision. Independent finite heat/Mellin experiment for s=2.25 and ell=1..6:
\`Gamma(s)*sum((2ell+1)/(ell(ell+1))^s)\` agrees with
\`quad(t^(s-1)*sum((2ell+1)e^(-t ell(ell+1))),t=0..infty)\`
at displayed 30 digit precision (observed value **0.865942155650375282681873090922**).
These numerical values are checkers only; proofs are in \`QUANTIZED_ARITHMETIC_ATOMS.md\`.

**No claim that SUCC's actual BBP source produces a physical magnetic monopole, any observed energy spectrum, a source-dependent eigenvalue gap, source-selected Weyl cancellation, base-16 normality of pi, or RH.** Base is draft #515 SHA \`2ea21654...\` and main is untouched.
