# Independent Bost–Connes cross-check: positive prime ladders versus signed Weil jets

**2026-11-05, post-preregistration.** This is a source/representation consistency check against the ORIGINAL Bost–Connes framework (1995), not a new quantization theorem or independent proof of RH. It qualifies the “negative-energy prime reservoir” intuition: arithmetic primes HAVE an exact positive Hamiltonian realization, while the minus signs in Guinand–Weil are signed test-function contributions, not literal negative occupation energies.

**Primary source:** J.-B. Bost and A. Connes, *Hecke Algebras, Type III Factors and Phase Transitions with Spontaneous Symmetry Breaking in Number Theory* (1995), IHES preprint https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf ; publication Selecta Math. (N.S.) 1 (1995), 411–457. The elementary free-prime-Fock description below is a special algebraic aspect of that system, not a substitute for its full Hecke algebra or KMS analysis.

## 1. Prime arithmetic atoms actually have a positive quantized ladder

Unique factorization identifies each positive integer n with a finite-occupation sequence \(n=\prod_p p^{k_p}\), \(k_p\in\mathbb N_0\). On \(\ell^2(\mathbb N)\), equivalently on the incomplete tensor product \(\bigotimes'_p\ell^2(\mathbb N_0)\) anchored at the all-zero vacuum, define
\[
\boxed{H|n\rangle=(\log n)|n\rangle,\qquad
H=\sum_p(\log p)N_p.}\tag{BC1}
\]
Each prime is an independent arithmetic oscillator with genuinely quantized nonnegative energy ladder
\[
\boxed{E_{p,k}=k\log p,\qquad k=0,1,2,\ldots.}\tag{BC2}
\]
These are energies in an explicitly specified quantum statistical mathematical model, not physical measurements of SUCC BBP prime jets.

For real \(\beta>1\), the trace converges absolutely:
\[
\boxed{Z(\beta)=\operatorname{Tr}e^{-\beta H}
=\sum_{n\ge1}n^{-\beta}
=\prod_p(1-p^{-\beta})^{-1}
=\zeta(\beta).}\tag{BC3}
\]
Every local factor is a positive geometric partition function. The global spectral gap above the vacuum is **\(\log2>0\)**. Thus an infinite number of arithmetic prime modes need NOT make a Hamiltonian gapless. SUCC #516's alternative solenoid operator \(H\chi_q=\kappa q^2\chi_q\) has zero gap because its domain and eigenlabels are different; it is NOT the same operator, and no intertwiner can equate the two spectra.

The 2-primary sub-Hamiltonian has exact four-quantum scale
\[
E_{2,4}=4\log2=\log16.
\]
This is the rigorous arithmetic connection to the Γ log16 carrier: its period is commensurate with exactly four prime-2 energy steps. For any odd p, \(\log p/\log16\) is irrational by unique factorization, so its positive ladder is incommensurate with that base-16 scale.

## 2. Where the arithmetic log(p) weight originates

For \(\operatorname{Re}s>1\), differentiating the ABSOLUTELY convergent Euler product gives
\[
\boxed{-\frac{\zeta'}{\zeta}(s)
=\sum_p\sum_{k\ge1}(\log p)\,e^{-s k\log p}.}\tag{BC4}
\]
For real \(\beta>1\), this is also the positive thermal mean energy:
\[
-\frac{d}{d\beta}\log Z(\beta)
=\langle H\rangle_\beta
=\sum_p\frac{\log p}{p^\beta-1}>0.
\]
In the Weil explicit formula the prime power contribution to a compactly supported autocorrelation is instead
\[
\boxed{-2\,\frac{\log p}{p^{k/2}}\operatorname{Re}g(k\log p).}\tag{BC5}
\]
Its sign varies with the *test-function phase correlation*. The negative sign comes from the explicit-formula balance/traces; the factor \(p^{-k/2}\) reflects the critical-line half-density. It does **not** turn the Bost–Connes positive energy klogp into a negative physical energy.

**Domain firewall:** The prime expansion BC4 is valid termwise for Re(s)>1. It CANNOT be evaluated termwise at s=1/2+it, where it diverges; the Guinand–Weil formula and its compact-support smearing supply a distinct rigorous analytic statement in the critical strip. The physical mathematical partition function is defined at real \(\beta>1\); a zero of the analytic continuation of ζ is not a negative-temperature Gibbs zero.

## 3. Exact sign obstruction to a unitary equivalence

The Bost–Connes H in BC1 is nonnegative, with spectral set \(\{\log n:n\ge1\}\) and a positive vacuum gap. For any L with a prime-power a<2L, THEOREMS.md's signed self-adjoint Weil jet \(J=-w(S_a+S_a^*)\) has a strictly negative eigenvalue on a positive-measure path fiber, with an equally positive partner. Since a unitary equivalence preserves spectrum, **no unitary operator can identify H with J.** This is a concrete typed no-go, not a failure of the analogy: the two models encode different aspects of the same arithmetic prime log-energy data.

A richer trace formula/relative Hamiltonian may carry *both* models, but it must be explicitly constructed with a common Hilbert space, a signed functional and correct Gamma completion before one can speak about source-derived “negative energy reservoirs.” Connes's separate absorption-spectrum interpretation of critical zeros is mathematically relevant prior art (https://arxiv.org/abs/math/9811068), not an identification with the finite J path eigenvalues.

## 4. Controls and next genuine advance

- **Positive:** All prime occupations have klogp≥0, and Z(β)>0 for β>1. At finite prime set P and occupation cutoff K, the partition function factorization is a literal finite distributive identity; no analytic continuation required.
- **Negative:** J has negative test-function expectations even though every BC oscillator has nonnegative energy. This falsifies a literal identification of signed Weil corrections with negative Bost–Connes occupations.
- **Critical:** The sum \(\sum_{p,k}\log p p^{-k/2}e^{-itk\log p}\) diverges as an ordinary series and cannot be substituted as the critical-line log derivative without smoothing/continuation.
- **Cross-SUCC:** #499's χ_-4 prime source action and #515/516's \(\log16\) circle reflect congruence and scale structures, but do not supply the missing intertwiner from authenticated BBP rational carries to BC H or the full Weil zero-side.

**Claim status:** BC1–BC5 classical/elementary proof within their domains; unitary spectral no-go disclosed; source-specific synthesis new to SUCC, priority unverified; RH and π normality OPEN.
