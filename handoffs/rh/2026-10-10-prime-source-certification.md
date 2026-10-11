# Certified finite prime-source contribution to Suzuki’s correlation report

**Status:** PROVED LOCAL + computationally verified bounded exact rational instrument

**RH PROVED:** No

**Source:** observational_succ/source_prime_certificates.py; tests/test_source_prime_certificates.py; scripts/prime_source_certificates_probe.py

**Historical provenance:** femboy2112/FuckingRH commit ba075348b7bcc66d938b3e0ca96c26e95bba340a; source file actualization/source_prime_certificates.py; original detailed derivation in provenance/origins/fuckingrh/research/2026-10-10/CERTIFIED_FINITE_PRIME_TRANSPORT.md. Native SUCC bootstrap branch: research/observational-succ-foundation-import-2026-10-10. Pin its exact SHA when integrating a future RH PR.

## Statement

Given a *fully integrated* finite arithmetic source \(a(1),\ldots,a(N)\), normalized by \(a(1)=1\), and its finite Dirichlet-convolution logarithm \(b=\log_*a\), define

\[
\Psi_{\mathrm{prime},a}(t)=
-\sum_{n\ge2}b(n)\frac{\log n}{\sqrt n}
(\lvert t\rvert-\log n)_+.
\]

For every finite rational time window of displacement at most \(M\), the conservative integer horizon \(N\ge3^{\lceil M\rceil}\) contains all active prime events. The response admits exact rational enclosures: logarithms use the positive atanh series with a proved geometric remainder after binary argument reduction; inverse square roots use exact integer square-root bounds; the positive-part ramp is enclosed without guessing the activation side. Arithmetic is performed in exact Fractions, **not** arbitrarily narrowed floating approximations.

For genuine zeta \(a(n)=1\), \(b(p^k)=1/k\) and \(b(n)=0\) off prime powers, so \(b(n)\log n=\Lambda(n)\). The interval therefore encloses exactly the **prime part** of Suzuki's source-defined screw function.

For counterfeit \(a(6)=2\), the new connected coefficient is \(b(6)=1\); within the first exposed interval \(\log6<t<\log12\),

\[
\delta\Psi_{\mathrm{prime}}(t)=
-\frac{\log6}{\sqrt6}(t-\log6)<0.
\]

The implementation certifies the strict sign with rational upper bounds.

## What this establishes

- A source-faithful, no-zero-input, **finite** arithmetic component of a candidate RH-kernel witness instrument.
- Exact causal horizon protection and explicit journal integration in the migrated baseline.
- A real counterfeit arithmetic source control with a rigorously signed difference.

## What this does NOT establish

- An independently certified **archimedean Gamma and pole** interval oracle.
- A strict negative finite witness for the **completed** Weil/Suzuki kernel.
- Positive definiteness of the complete Weil form or RH.
- Any result for arbitrary complex Dirichlet characters without proper conductor, Gamma and positivity/sign conventions.

**Next RH engineering step:** derive rational interval enclosures for \(A_\infty(t)\) (including its singular/boundary normalizations), combine them with the verified prime-side intervals on the admissible Suzuki domain, and rerun a zero-blind finite rational Gram witness search. Only after that consider an independently derived source-specific positive type theorem.

## Reproduction

~~~sh
python -m pip install -e ".[test]"
python -m unittest discover -s tests -p 'test_source_prime_certificates.py' -v
python scripts/prime_source_certificates_probe.py
~~~

The source manifest records the Git blobs; final SUCC merge commit must be added when the recipient integrates.
