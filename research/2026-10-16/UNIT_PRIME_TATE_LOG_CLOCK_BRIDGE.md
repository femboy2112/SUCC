# UNIT → PRIME → TATE: a canonical convergent-domain log-clock bridge

**Date:** 2026-10-16. **Status:** classical mathematics with explicit paper proofs and a new-to-SUCC typed source interface; exact finite \`Fraction\`/interval tests are separate evidence. **RH PROVED: NO.** The original completed Weil sign and the authentic Suzuki zero-shift Schur sign remain open.

**Parent:** SUCC \`research/unit-prime-succ-equivalence-2026-10-16\` at \`53c53e91bd1b46071d6437fed0e68c9b337892a0\`. This work is a child of that research line and does not rewrite canonical source files. Load-bearing inherited source: \`observational_succ/tate_idelic_zeta.py\`, \`tate_schwartz_functor.py\`, \`all_places_zeta.py\`, \`completed_weil_transport.py\`, \`source_weil_hierarchy.py\`, and \`tate_weil_distribution.py\`. Canonical authentic signed Suzuki source blob, **unchanged**, is \`0cc8510b71d178fc79e8d410a86d8b6014cf9178\`.

## 1. Three meanings of the unit that must not be conflated

1. **Dirichlet unit:** the basis state \(e_1\), the empty prime valuation word, and the unique coefficient \(1\) in the Euler expansion.
2. **Norm-one rational gauge:** for *every* \(q\in\mathbb Q^\times\), \(|q|_\infty\prod_p|q|_p=1\), a real/finite relation across the common rational diagonal.
3. **Local residue-one congruence:** in \(\mathbb Z_p\), \((1-p)^{-1}\equiv1\bmod p\). This says nothing about the divergent real Euler product at \(s=-1\), and does not select \(\zeta(-1)\) without analytic continuation.

The user hypothesis is strengthened into a precise question: **can the same weighted global arithmetic state obtained from additive \(S\) and prime \(V_p\) be identified, with source-correct Haar factors, with Tate's canonical multiplicative Mellin integral, and what additional independent structure is supplied by the real Gaussian?** The answer is yes to the first identification on \(\operatorname{Re}s>1\); the real Gamma input is additional data, not forced by the flat prime path law.

## 2. UPT-01: a commuting mathematical bridge on the genuine zeta source

On \(\ell^2(\mathbb N_{>0})\) define \(Se_n=e_{n+1}\) and \(V_pe_n=e_{pn}\), for **genuine primes**. As proved in the parent unit–prime dossier,

\[
V_pS=S^pV_p,\qquad
\Psi_s=\sum_{n\ge1}n^{-s}e_n
=\sum_{k\ge0}A_s^ke_1
=\lim_{P\to\infty}\prod_{p\le P}(I-p^{-s}V_p)^{-1}e_1.
\]

The vector equality holds for \(\operatorname{Re}s>1/2\) in \(\ell^2\), with the product interpreted **only after applying to \(e_1\)**. This does not mean the additive and multiplicative operators are unitarily equivalent. In the smaller domain \(\operatorname{Re}s>1\), scalar coefficient summation also converges absolutely and is the Euler product \(\zeta(s)\).

Now take the authentic Tate test on the additive adeles,

\[
\Phi_0(x_\infty,x_f)=e^{-\pi x_\infty^2}
\prod_p{\bf1}_{\mathbb Z_p}(x_p).
\]

Use Lebesgue additive Haar at infinity and finite additive Haar normalized by \(\operatorname{vol}(\mathbb Z_p)=1\). On multiplicative groups use

\[
d^\times x_\infty=\frac{dx_\infty}{|x_\infty|},
\qquad
d^\times x_p=\frac{dx_p}{(1-p^{-1})|x_p|_p}.
\]

The additive volume of \(p^k\mathbb Z_p^\times\) is \(p^{-k}(1-p^{-1})\), so **each local multiplicative valuation shell has mass one**. Consequently, for \(\operatorname{Re}s>0\),

\[
\int_{\mathbb Q_p^\times}{\bf1}_{\mathbb Z_p}(x)|x|_p^s\,d^\times x
=\sum_{k\ge0}p^{-ks}=(1-p^{-s})^{-1}.
\]

For the real Gaussian, both signs of \(\mathbb R^\times\) matter:

\[
\int_{\mathbb R^\times}e^{-\pi x^2}|x|^s\frac{dx}{|x|}
=2\int_0^\infty e^{-\pi r^2}r^{s-1}\,dr
=\pi^{-s/2}\Gamma(s/2)=:\Gamma_{\mathbb R}(s).
\]

The substitution \(t=\pi r^2\) derives the real factor and fixes its normalization. Restricted-product Haar/Tonelli, with \(\operatorname{Re}s>1\), gives the authentic global Tate integral

\[
\boxed{\quad
Z(\Phi_0,s)=\Gamma_{\mathbb R}(s)\zeta(s)
=\Gamma_{\mathbb R}(s)\sum_{n\ge1}n^{-s}
=\Gamma_{\mathbb R}(s)\prod_p(1-p^{-s})^{-1}.
\quad}
\]

Thus weighted additive SUCC and prime-valuation FUCC generate **the same finite-place mass** inside Tate's full source; the real Gaussian supplies its separately normalized Archimedean factor. This is a reconstruction of a classical theorem, not a new Euler product or an empirical claim.

**Crucial finite-cutoff firewall.** The product \(Z_P(s)=\prod_{p\le P}(1-p^{-s})^{-1}\) is a perfectly lawful finite observer approximation. But requiring \({\bf1}_{\mathbb Z_p^\times}\) at *every* omitted prime \(p>P\) does **not** produce another additive Schwartz–Bruhat test: it imposes infinitely many nonstandard coordinate restrictions. At the all-one finite adele, any basic restricted-product neighbourhood leaves infinitely many prime coordinates unrestricted inside \(\mathbb Z_p\); set a sufficiently large omitted coordinate to zero and the proposed product of indicators jumps from one to zero. It is not locally constant there. It can be meaningful as a function on the multiplicative **idele** carrier, which has a different restricted-product topology; it is not an input to Tate's additive Poisson theorem. Therefore a finite Euler product is never silently promoted to a complete global Schwartz source.

If \(\sigma=\operatorname{Re}s>1\), expanding the finite product by unique factorization gives precisely the \(P\)-smooth integer coefficients. Every omitted integer exceeds \(P\), so

\[
\boxed{\left|\zeta(s)-Z_P(s)\right|
\le\sum_{n>P}n^{-\sigma}
\le\frac{P^{1-\sigma}}{\sigma-1}.}
\]

The source implementation reuses \`finite_euler_stage\`, \`euler_exhaustion_bound\`, \`StandardTateSource.local_test\` and an **independent** weighted prime-word enumerator. Finite stages and source epochs remain typed; the full-place theorem is imported with explicit hypotheses.

## 3. UPT-02: genuine logarithmic prime-power current

The local Euler logarithmic derivative is **negative**:

\[
-\frac{d}{ds}\log(1-p^{-s})^{-1}
=\frac{\log p}{p^s-1}
=\sum_{k\ge1}(\log p)p^{-ks}.
\]

Locally uniform absolute convergence on \(\operatorname{Re}s>1\) justifies termwise differentiation. Therefore

\[
\boxed{
C(s):=-\frac{\zeta'(s)}{\zeta(s)}
=\sum_p\sum_{k\ge1}\log(p)\,p^{-ks}
=\sum_{n\ge2}\frac{\Lambda_{\rm ar}(n)}{n^s},
\quad\operatorname{Re}s>1,}
\]

with \(\Lambda_{\rm ar}(p^k)=\log p\), zero at all other integers. **The ordinary Dirichlet coefficient of \(\zeta\) at 6 is one; the logarithmic coefficient at 6 is zero.** A fake independent \(V_6\) generator violates the prime-place model.

For integer \(\beta\ge2\) and genuine cutoff \(P\), exact finite coefficients \((p^\beta-1)^{-1}\) multiply existing rigorously enclosed \(\log p\) values from \`source_weil_hierarchy.log_iv\`. The bridge independently checks its coefficient tape against \`StandardTateSource.logarithmic_coefficients\`, which uses the previously authenticated prime-power oracle. The full prime-current error satisfies

\[
0\le C(\beta)-\sum_{p\le P}\frac{\log p}{p^\beta-1}
\le P^{1-\beta}
\left(\frac{\log P}{\beta-1}+\frac1{(\beta-1)^2}\right).
\]

Replace \(\log P\) by the integer \(L=\lceil\log_2 P\rceil\), using \(\log2<1\), for the implemented rational upper bound. The inequality is the classical decreasing integral comparison \(\Lambda(n)\le\log n\); it does **not** license evaluation of the prime Dirichlet series at \(s=1/2\).

## 4. UPT-03: SUCC's Gibbs prime clocks and Tate's continuous real log clock

Set \(H e_n=(\log n)e_n\) on its natural diagonal domain. For **real \(\beta>1\)**, the parent Hilbert vector \(\Psi_{\beta/2}\) exists and

\[
\|\Psi_{\beta/2}\|^2=\sum_n n^{-\beta}=\zeta(\beta).
\]

Measuring its normalized basis probabilities yields \(P_\beta(n)=n^{-\beta}/\zeta(\beta)\), the same **diagonal** distribution as the Gibbs density \(e^{-\beta H}/\zeta(\beta)\). Those are **not identical states on all observables**: on \(\operatorname{span}(e_1,e_2)\) at \(\beta=2\), both normalized diagonal laws are \((4/5,1/5)\), but the coherent superposition has exchange expectation \(4/5\) for \(|1\rangle\langle2|+|2\rangle\langle1|\), while the diagonal mixture has expectation zero.

Under the valuation coordinates \(n=\prod_p p^{k_p}\), the Gibbs law factors:

\[
P(K_p=k)=(1-p^{-\beta})p^{-k\beta},\quad
\mathbb E K_p=\frac1{p^\beta-1},\quad
\operatorname{Var}K_p=\frac{p^\beta}{(p^\beta-1)^2}.
\]

For \(\beta>1\), \(\sum_pP(K_p>0)=\sum_pp^{-\beta}<\infty\). Borel–Cantelli gives only finitely many occupied prime coordinates almost surely; their product is an actual positive integer. By absolute convergence, the prime clock mean and variance are

\[
\mathbb E_\beta H=\sum_p\frac{\log p}{p^\beta-1}
=-\frac{\zeta'(\beta)}{\zeta(\beta)},\qquad
\operatorname{Var}_\beta H
=\sum_p\frac{(\log p)^2p^\beta}{(p^\beta-1)^2}
=(\log\zeta)''(\beta)>0.
\]

**The Archimedean place introduces an independent continuous log clock.** Under normalized Gaussian Mellin probability, \(r=|x_\infty|>0\) has density

\[
f_\beta(r)=\frac{2e^{-\pi r^2}r^{\beta-1}}
{\Gamma_{\mathbb R}(\beta)},\qquad
\pi r^2\sim\operatorname{Gamma}(\beta/2,1).
\]

Consequently, with digamma \(\psi\) and trigamma \(\psi_1\),

\[
\mathbb E_\beta\log r=\frac{\psi(\beta/2)-\log\pi}{2}
=:A_\infty(\beta),\quad
\operatorname{Var}_\beta\log r=\frac14\psi_1(\beta/2)>0.
\]

At even \(\beta=2m\) these become exact classical special-value identities

\[
A_\infty(2m)=\frac{H_{m-1}-\gamma-\log\pi}{2},\qquad
\operatorname{Var}\log r=\frac14
\left(\frac{\pi^2}{6}-H_{m-1}^{(2)}\right).
\]

The actual existing SUCC outward rational \`gamma_iv\`, \`pi_iv\`, \`log_interval\` and harmonic fractions enclose them. The continuous **real-place log norm** and the discrete **negative p-adic valuation log norm** are independent under the normalized \(\Phi_0(x)|x|^\beta d^\times x\) product measure. Set

\[
Y=\log|x|_{\mathbb A}
=\log r-\sum_p K_p\log p.
\]

The full normalized source is supported on actual ideles almost surely, since only finitely many \(K_p\) are positive. Its first two cumulants are therefore

\[
\boxed{\mathbb E_\beta Y
=A_\infty(\beta)-C(\beta)
=\frac{\Lambda'(\beta)}{\Lambda(\beta)},}
\]
\[
\boxed{\operatorname{Var}_\beta Y
=\frac{\psi_1(\beta/2)}4+
\sum_p\frac{(\log p)^2p^\beta}{(p^\beta-1)^2}
=(\log\Lambda)''(\beta)>0.}
\]

**The minus sign in the mean is essential:** \(|p^k|_p=p^{-k}\) and so \(\log|p^k|_p=-k\log p\). This is a precise, classical version of the proposed **Archimedean balancing mechanism**: all local logarithmic contributions are read through a single adelic norm/Mellin coordinate. It does not say their mean is zero; nor does positive variance entail signed Weil positivity.

**A new exact rational variance-tail interface.** For integer \(\beta\ge2\), \(P\ge3\), \((\log x)^2x^{-\beta}\) is decreasing on \(x\ge3\), and \((1-p^{-\beta})^{-2}\le(1-2^{-\beta})^{-2}\). Integral comparison and \(\log P\le L=\lceil\log_2P\rceil\) give the proven bound

\[
\boxed{
\sum_{p>P}
\frac{(\log p)^2p^\beta}{(p^\beta-1)^2}
\le\frac{P^{1-\beta}}{(1-2^{-\beta})^2}
\left[
\frac{L^2}{\beta-1}
+\frac{2L}{(\beta-1)^2}
+\frac2{(\beta-1)^3}
\right].
}
\]

It uses no prime number theorem and is deliberately conservative. The source code constructs complete \(\Lambda(\beta)\), \(\Lambda'/\Lambda(\beta)\) and the log-norm variance intervals with explicit finite-prime remainders. These are convergent-domain statements, not a critical-line oracle.

## 5. UPT-04: the real-place two-step Mellin successor

Gaussian integration by parts, or the classical Gamma recurrence, gives

\[
\boxed{\Gamma_{\mathbb R}(s+2)=\frac{s}{2\pi}\Gamma_{\mathbb R}(s),
\quad\operatorname{Re}s>0.}
\]

For \(s=2m\), the exact source law is \(\Gamma_{\mathbb R}(2m)=(m-1)!\pi^{-m}\). The implementation keeps exact rational coefficients and an explicit power of \(\pi\), not a floating approximation. This is a lawful **Archimedean Mellin ladder**, distinct from the additive integer \(S\) and prime \(V_p\), but acting on their common Mellin exponent.

A rigorous normalization crucible: replace the real Gaussian with \(\phi_a(x)=e^{-\pi ax^2}\), \(a>0\). It has the same finite Euler factors but

\[
\mathcal M_\infty\phi_a(s)=a^{-s/2}\Gamma_{\mathbb R}(s),\quad
\widehat{\phi_a}(y)=a^{-1/2}e^{-\pi y^2/a}.
\]

With the fixed Fourier/Haar conventions, a Gaussian in this family is self-dual only for \(a=1\). At \(a=4,s=2\), the real Mellin factor is exactly **one quarter** of the canonical one; no finite-place prime weight detects that alteration. Both are legitimate real Schwartz tests, but only the \(a=1\) choice is the **canonical completed zeta test**. We are not claiming Fourier self-duality characterizes a unique arbitrary Schwartz function; the conclusion is limited to this Gaussian family.

As a classical independent special-value calibration, \(\Lambda(2)=\Gamma_{\mathbb R}(2)\zeta(2)=\pi/6\) by Euler's Basel formula. The finite-stage rational enclosure contains that known value; the finite Euler prefix does not prove Basel.

## 6. UPT-05: where completed poles and signed Weil *actually* arise

On the zero-free input half-plane \(\operatorname{Re}s>1\),

\[
\frac{\Lambda'(s)}{\Lambda(s)}
=\frac{\psi(s/2)-\log\pi}{2}-C(s).
\]

The functional equation \(\Lambda(s)=\Lambda(1-s)\) and the poles at \(s=0,1\) come from **Tate's full adelic Fourier–Poisson source**, not from a finite Euler prefix or positivity of the Gibbs measure. For \(\Phi_0\), the two \`TateZeroModes\` residues are \((-1,+1)\). The entire symmetrized function \(\xi(s)=\tfrac12s(s-1)\Lambda(s)\) satisfies, in the input half-plane,

\[
\boxed{
\frac{\xi'(s)}{\xi(s)}
=\frac1s+\frac1{s-1}
+\frac{\psi(s/2)-\log\pi}{2}
-\sum_{n\ge2}\Lambda_{\rm ar}(n)n^{-s}.
}
\]

The two rational terms are zero-mode/polar contributions, not new prime weights. The full **signed Weil distribution** on compact log tests additionally needs the already established analytic continuation and contour/test-domain identification. Its prime-power atoms have the real signed half-density \(-\Lambda_{\rm ar}(n)n^{-1/2}\) at \(\pm\log n\), accompanied by Gamma and pole terms. **Do not evaluate the divergent Dirichlet current directly at \(s=1/2\)**. The positive Gibbs log-energy variance is not an RH-equivalent Weil positivity proof. The original four-low Suzuki sign remains open.

This bridge is typed for the canonical unramified zeta \`StandardTateSource\` only. The real/ramified \(\chi_4\) source has a different parity/conductor/Gamma test, and \(\chi_4(2)=0\) as an integer coefficient while the local multiplicative 2-adic character is nonzero on \(2\). It cannot silently use this even-Gaussian passport.

## 7. Adversarial controls and known limitations

- **Fake prime:** a made-up independent \(V_6\) double counts prime occupation and produces a false log-current at six. Rejected by generator and true \(\Lambda(n)\) tape.
- **Wrong multiplicative Haar:** omitting \((1-p^{-1})^{-1}\) gives local unit-shell mass \(1-p^{-1}\), not one.
- **Wrong real sign multiplicity:** integrating only the positive real component gives half the canonical \(\Gamma_{\mathbb R}\).
- **Wrong Gaussian:** scale \(a=4\) preserves every Euler factor but changes the real Mellin factor and self-duality.
- **Cutoff-as-Tate mutant:** substituting \(1_{\mathbb Z_p^\times}\) at infinitely many omitted additive places is not a Schwartz–Bruhat test.
- **Pure-versus-mixed state:** matching integer diagonal distributions does not yield full quantum state equality.
- **Prime-current direction:** \(-\zeta'/\zeta\) is positive on real \(s>1\); \(\zeta'/\zeta\) is its negative. The completed derivative has the Archimedean term **minus** the prime current.
- **Character mismatch:** source \(\chi_4\) is excluded from the standard even Gaussian source instead of laundered.
- **Domain violation:** all Euler-current rearrangements require \(\operatorname{Re}s>1\); no \(\operatorname{Re}s=1/2\) shortcut.
- **Source authentication:** source IDs and epochs are mathematical declarations; hashes and bounded tests do not attest physical measurements or prove a universal analytical theorem.
- **Positivity firewall:** a variance is a positive covariance on a probability space, not the original signed completed Weil quadratic form.

## 8. Reproduction and next consequential gate

Implementation: \`observational_succ/unit_prime_tate_bridge.py\` (reuses existing source kernels), \`tests/test_unit_prime_tate_bridge.py\`, \`scripts/unit_prime_tate_bridge_probe.py\`; ledger: \`docs/CLAIM_SUPPLEMENT_UNIT_PRIME_TATE_BRIDGE.md\`. Focused commands:

\`\`\`sh
python -m unittest discover -s tests -p 'test_unit_prime_tate_bridge.py' -v
python scripts/unit_prime_tate_bridge_probe.py
\`\`\`

Research paper proofs of the infinite equalities depend on classical Haar, uniqueness of prime factorization, convergence, Mellin/Gamma, and adelic Poisson theorems as identified in \`TATE_IDELIC_ZETA_RECONSTRUCTION.md\`. The finite code checks exact instances and rigorous numerical **enclosures** under declared budgets; it does not recreate the infinite theorem by enumeration.

**Next route, in order:** (i) cross-check the full source's additive Fourier/Poisson normalization with the multiplicative clock/Gaussian construction without replacing the Gaussian by an arbitrary test; (ii) extend to the authenticated *odd, ramified* \(\chi_4\) case, preserving local Hecke versus zero-extended integer character; (iii) prove or refute source-specific spectral-range decay of the **true signed** Suzuki operator, not just Gaussian Gibbs variance; (iv) formalize only manageable finite shell, logarithmic clock and source-gauge theorems in YEAN; (v) preserve negative source-mutation cases and the analytic-continuation firewall.

**Verdict:** classical additive/prime/Tate identification and independently bounded discrete/continuous log-clock cumulants, source-typed reproducible interfaces, and strict countermodels. The missing RH-hard Weil positivity arrow remains missing.

### Classical references
- J. Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (1950 thesis); B. Poonen, *Tate's thesis* (MIT 18.786 notes, 2015), for source Haar, idelic Mellin and Poisson.
- NIST Digital Library of Mathematical Functions, Gamma/zeta/digamma chapters and Euler special values.
- J.-B. Bost and A. Connes, *Hecke Algebras, Type III Factors and Phase Transitions with Spontaneous Symmetry Breaking in Number Theory*, Selecta Math. 1 (1995), for the logarithmic Hamiltonian and zeta partition-function setting; its full C*-algebra, KMS states and phase transition are **not** established here.
