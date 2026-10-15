# CLAIM SUPPLEMENT — finite genuine Weil hierarchy and sign frontier

**2026-10-14, draft research.** Branch: \`research/finite-source-weil-negative-depth-2026-10-14\`. Exact parent SUCC PR #76 \`3270d4b9d992042c7c2bebbe784916f544ac565c\`; prior E38/completed-Weil PR #71/adelic source PR #73. Parallel PRs #80–#83 are independent, not ancestry. Full detailed proofs: [FINITE_SOURCE_WEIL_NEGATIVE_DEPTH.md](../research/2026-10-14/FINITE_SOURCE_WEIL_NEGATIVE_DEPTH.md). **RH PROVED: NO.** No new academic priority, physical carrier attestation, infinite-zero oracle or full generalized RH claimed.

| ID | Mathematical claim | Status & boundary |
|---|---|---|
| FSW-01 | Suzuki genuine \(g\) from original p-power/half-density/Gamma/poles, \(Q_W(v)=\langle G_aDv,Dv\rangle\) on \(H_0^1\) | CLASSICAL IMPORT, checked against Suzuki 2026 v3 Eq (1.3),(1.8), code no unknown zeros |
| FSW-02 | Fully signed finite J Gamma/finite-cell N hierarchy with \(E_{a,J,N}=2a(\tau_J+ (2a/N)L_J+\eta)\) operator-norm error and \(E_{a,J,J^2}\to0\) on fixed a | PROVED LOCAL using classical compact kernel/Suzuki; no sign assumption |
| FSW-03 | \(d_-(G)=\operatorname{dist}(G,\mathrm{PSD})\), 1-Lipschitz and two-sided source error; \(d_-(G_a)=0\) all a iff RH | CLASSICAL spectral/Weil equivalence, finite source implementation |
| FSW-04 | Exact nested Galerkin negative depth is nondecreasing to true depth; source-truncated matrices need not share monotonicity | CLASSICAL / PROVED LOCAL theorem |
| FSW-05 | Certified exact rational \(\pi,\gamma,\log,\exp,1/\sqrt{n}\), true p-power tape, finite signed g enclosures, shifted rational LDL bound, source replay | PROVED LOCAL at a rational 0<a<=1, J<=36,N<=24; classical Euler–Maclaurin remainder imported; physical authenticity UNVERIFIED |
| FSW-06 | Generic effective compact smooth rank-one families with uniform exponential norm modulus but undecidable exact positivity via nonhalting | PROVED mathematical reduction, code only toy halting-time scalar calibration; NOT zeta-source lawful |
| FSW-07 | Pairwise positive meanzero contrasts may conceal a negative 3-way interaction; rational \(M=I-\frac15 uu^T\), \(u=(1,1,-2)\) | PROVED LOCAL exact countermodel, not genuine Weil mutation |
| FSW-08 | Genuine \(a\mapsto d_-(G_a)\) continuous/nondecreasing, source prime-power activation at \(2a=\log n\), monotonic sign witness across enlarged supports | PROVED LOCAL / CLASSICAL compact-continuity, radius wavefront instrument |
| FSW-09 | Exact coupled refinement gate \(E_{J+1,N}-E_{J,N}\) changes sign at specified N; too many Gamma modes with coarse spatial mesh *worsens certified error* | PROVED LOCAL exact rational instrumentation; this is an error-bound property, not change of true arithmetic sign |
| FSW-CACHE | Default untyped lru_cache alias \(0.5=Fraction(1,2)\) bypassed proof input-type guard after cache warming | OBSERVED CI failure on prior head; FIXED via typed cache, hostile regression |
| FSW-RH | Negative spectral depth of true signed hierarchy vanishes for every a | UNVERIFIED (RH equivalent). Not inferred from any current finite successes |
| FSW-PHYSICAL | Actual observer accessing empirical Higgs/arithmetic places or physical cost intrinsic to RH | UNVERIFIED. Analogy not proof |

**Source/test boundary:** fake prime-power n=6, omitted p=3, incorrect p-label on 8, type-laundered floats and forged matrix/error metadata rejected. Independent mpmath tests are numerical calibration, *not* proof of arbitrary transcendental interval certification. Classical analytic inequalities + rational interval arithmetic are the stated proof basis. Full repository and Lean proof states are separate from the dedicated focused GitHub Actions workflow.

**Reproduce:**
\`\`\`sh
python -m unittest discover -s tests -p 'test_source_weil_hierarchy.py' -v
python scripts/source_weil_hierarchy_probe.py --verify research/2026-10-14/FINITE_SOURCE_WEIL_RECEIPT.json
python scripts/verify_provenance.py
\`\`\`

**Next decisive probe:** adapt the source-true signed hierarchy from first wavefront windows to arbitrary a with validated complex/real source quadrature, improve N vs J certified error by high-order or wavefront-aligned Galerkin approximations, and derive a genuine source-specific *uniform* nonnegative all-test inequality or an independently identified source-first positive operator. Full test-domain lower bound cannot be replaced by source-positive theta moments, first critical-line zero witnesses, zero-count contours or auxiliary chiral baths.


## Round 002: positive-tail theorem and recursive source-model diamond

- **FSW-10 — PROVED LOCAL using CLASSICAL Fourier positivity:** The original Suzuki Gamma kernel rung \(-4(1-e^{-(4J+1)|x-y|/2})/(4J+1)^2\) becomes **positive** on \(L_0^2\), because its constant part is annihilated. Consequently \(G_{a,J+1}-G_{a,J}\succeq0\), and \(T_{a,J}=G_a-G_{a,J}\succeq0\) with actual operator norm \( \|T_{a,J}\|\le 2/(4J+1)^2+16/(4J+1)^3=O(J^{-2})\). This refines GWC-5's symmetric \(O(J^{-1})\) kernel bound, but does **not** assert \(G_a\succeq0\).
- **FSW-10a — PROVED LOCAL, conditional on source and interval certification:** with \(E_{\mathrm{spatial}}=2a((2a/N)L_J+\eta)\), the original completed operator has the **one-sided source Loewner sandwich** \(\widetilde G-E_{\mathrm{spatial}}I\preceq G_a\preceq\widetilde G+(E_{\mathrm{spatial}}+\widehat\tau_J)I\). A finite negative Rayleigh needs the positive-tail **upper bound**; a finite whole-space lower-sign certificate does **not** pay a Gamma-tail penalty. Code API \`original_source_one_sided\` regenerates genuine stage and rejects forged matrix/error.
- **FSW-11 — PROVED LOCAL, classical compact-Galerkin/order argument:** define \(b_{J,N}=d_-(P_NG_{a,J}P_N)\) on nested dense original meanzero test spaces. Then \(b_{J,N}\) is nondecreasing in N and nonincreasing in J, and uniform \(O(J^{-2})\) Gamma convergence yields \(\inf_J\sup_N b_{J,N}=\sup_N\inf_J b_{J,N}=d_-(G_a)\). This is **the source-faithful higher-order interaction limit**, not the desired zero value. RH iff this invariant vanishes for all a.
- **FSW-11-MUT — REFUTED shortcuts:** infinitely many authentic positive Gamma increments do not certify an initially signed operator; arbitrarily many finite Galerkin “passes” do not certify a zero negative-depth limit. The exact positive-tail mode is not an optional chiral source or a statistical Gaussian prior. Removing mean-zero would invalidate the constant-kernel cancellation used by this special proof.

The source-first module, rational tests and 2026-10-14 dossier XIII implement these scoped claims. Dedicated GitHub Action at exact code+dossier head \`edda87625d32e4a9c7b87ea02e4314153def8898\` passed both Python 3.10 and 3.13. The full repository suite is separately pending. No Lean kernel proof or external academic priority claimed.


- **FSW-12 — PROVED LOCAL / CLASSICAL conditional source theorem:** the original mean-zero missing Suzuki Gamma tail is **strictly** positive on every nonzero vector, by Fourier multiplier \(2\alpha/(\alpha^2+\xi^2)>0\). If a true \(G_a\) has a nonzero null vector, its every finite authentic Gamma-cutoff predecessor \(G_{a,J}\) has a negative Rayleigh direction. This does **not** assert such a true null vector exists. An exact scalar toy \(G_J=-1/(4J+1)\nearrow0\) independently refutes the shortcut “positive limit entails eventually PSD finite approximants.” Its use in RH claims is disallowed absent authentic identification.
