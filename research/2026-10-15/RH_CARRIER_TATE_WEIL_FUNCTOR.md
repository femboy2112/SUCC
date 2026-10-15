# RH carrier geometry: minimal, maximal, and Goldilocks; Tate→Weil functor audit

**Date:** 2026-10-15. **Branch:** \`research/rh-carrier-tate-functor-2026-10-15\`.
**Parent:** \`research/tate-lattice-finite-global-descent-2026-10-15@1a1123d2f4cc7112fab4c12e1556ad5df6309117\`, draft PR #113.
**RH PROVED: NO.** No unsolved Weil positivity is assumed or certified; physical source authentication is not achieved. Several theorems below are classical, not novel SUCC mathematical discoveries.

## 0. Recover what "carrier containing RH" can mean

There are at least four incompatible uses of "contains":

- **Expression:** a formal language/source has a formula equivalent to RH.
- **Computable specification:** for any finite query or counterexample candidate, a terminating procedure can construct a certified answer (possibly one-sided if equality is unresolved).
- **Analytic realization:** a source-indexed space/operators represent all prime, Gamma, pole, half-density and Fourier data, on honest test domains.
- **Proof-sufficient positivity:** from source laws, prove a form equal to the complete Weil form is PSD for ALL legitimate tests.

The last is RH-hard. No implication from first three to fourth without a new theorem. Define categories/morphisms and a cost/performance target before claiming a least or greatest carrier.

## 1. CR-01 — A small arithmetic RH carrier exists; "the minimum" has not been proved

**Lagarias (American Mathematical Monthly 109 (2002), Theorem 1.1):**

Let sigma(n)=sum_(d|n) d and H_n=sum_(j=1)^n 1/j. Then

    RH <=> for all integers n>=1:
       sigma(n) <= H_n + exp(H_n)*log(H_n),

with equality only at n=1 in the desired criterion. This equivalence is a CLASSICAL THEOREM. The underlying source is integer factorization/divisor sums plus harmonic rational arithmetic and computable real exp/log. The analytic equivalence theorem is nontrivial and imported, NOT derivable merely from tests of finitely many n.

**Low carrier:** (N,+,×,divisibility, harmonic sums, effective approximations to exp/log) and a universal statement. Complex zeros need not occur as data inputs in the inequality. If RH were false, the negation of Lagarias' universal inequality admits an integer n with **strict** excess, hence sound rational intervals could eventually certify such a violation. This establishes a constructive *one-sided refutation route*, not a bound on the first violating n or an algorithm proving RH true.

A Boolean "RH truth bit" would be the smallest possible *information* quotient but inserts the unanswered result as an oracle; it is excluded by the no-zero-reading, source-derived construction contract. There is **no established initial object / minimum** across all allowed carrier languages, proof rules, categories of simulations and resource measures. Arithmetic *sufficiency for statement* is not minimality for proof.

**Source** (primary): https://websites.umich.edu/~lagarias/doc/elementaryrh.pdf
An alternative strict source criterion: Robin (1984), RH iff sigma(n)<exp(gamma)*n*log(log n) for all n>5040, with gamma Euler's constant. Published statement and context: https://link.springer.com/article/10.1007/s11139-022-00683-0

## 2. CR-02 — There is no unrestricted maximal RH carrier

Assume carriers can be extended by irrelevant independent source coordinates, and comparison regards faithful state embeddings or recoverability of the original source and RH target. For any carrier C, choose a set D of cardinality strictly larger than |C|, extend to C'=C×D, and let the RH target be G'(c,d)=G(c). Then C' still expresses/preserves RH, but cannot inject into C in the ordinary set-carrier category (cardinality). Hence no maximal object under unbounded state extension. Category-dependent existence of a terminal carrier cannot be inferred from "RH is contained"; a *chosen* restricted size/morphism universe may behave differently.

The exact opposite danger is a 'minimal' quotient W/~_G containing only true/false: this is a nonconstructive tautology whenever G has not been proved to factor through accessible observations. It is neither a source-generated formula nor a computational reduction.

## 3. CR-03 — Three practically useful, non-equivalent carriers

**Low / arithmetic:** Lagarias/Robin predicate on natural integers. Good for finding finite counterexamples and proving uniform divisor bounds. Lacks, as a primitive, a continuous Fourier test space on which a Weil quadratic form is already defined.

**Middle / Tate:** adeles A_Q, ideles A_Q^×, Schwartz–Bruhat S(A_Q), Haar measures, additive character ψ_A, Fourier transform F, Mellin idelic zeta integrals and Poisson summation on Q. Finite primes supply valuation shells; real place supplies the Gaussian Gamma factor. The function space and Fourier/multiplicative intertwining are mathematically classical. Source-indexed SUCC lifts/history, analytic continuity and a trusted source-to-Weil identification are still distinct obligations.

**High / Suzuki–Weil sign:** compactly supported smooth log-scale tests φ∈C_c^∞(R), the full **signed** Weil functional W, or Suzuki's completed continuous screw kernel and its full family of Gram forms. Suzuki (2023) and Suzuki (2026) supply equivalent RH conditions involving positivity, NOT unconditional proofs of the positivity. Kernel PSD on every test family is the hard statement.

Suggested **Goldilocks interface** is not a single conveniently named space but a *typed fibered construction*:

    source-labelled SUCC event paths and arithmetic prime jets
           ↘ truthful Laurent/valuation source maps ↙
       restricted-product Schwartz–Bruhat test functions
               -- Fourier + Mellin + Poisson -->
          fully completed real/log-test Weil distribution
               -- sign, continuity, all-test density -->
          source-derived complete PSD (OPEN / RH HARD)

At every arrow require explicit source ID, epoch, functorial composition, norm/topology, Haar normalization, domain, Gamma and pole, half-density, fake-composite and non-Euler mutation controls. Do not replace the actual Weil form by a positive auxiliary object.

**Optimization criterion:** minimize the proof obligations or source-irrelevant degrees of freedom, subject to retaining analytic completeness, true arithmetic input, and an honest kernel-of-observation map. There is no proven global optimum. A source-specific choice of compact support and Hilbert/Sobolev completion may reduce analytic complexity *locally* but could lose directions needed for all-test positivity.

## 4. TF-01 — Local Tate Fourier functor on Schwartz–Bruhat atoms (CLASSICAL; EXACT RATIONAL CHART TESTED)

Fix one genuine prime p, normalized additive Haar measure vol(Z_p)=1, and additive character

    ψ_p(y) = exp(-2πi {y}_p),

with p-adic principal part {y}_p ∈ Q/Z, matching the *negative p-sign* in the SUCC Tate lattice convention; the Archimedean character has the opposite sign. For rational a and integer k let

    B_(a,k)=a+p^k Z_p,
    f_(a,k)=1_(B_(a,k)).

All such f are compact-open Schwartz–Bruhat functions on Q_p. The implementation stores the canonical rational representative of the coset and exact level k. The elementary Haar formula is

    ∫_(Q_p) f_(a,k)(x) dx = p^(-k).

For any ξ∈Q_p, Fourier transform under the declared ψ_p satisfies

    F_p[f_(a,k)](ξ) =
         p^(-k) ψ_p(a ξ) 1_(p^(-k) Z_p)(ξ).                     (4.1)

Proof: translate the subgroup, then integrate its character; ∫_(p^k Z_p) ψ_p(xξ) dx is p^-k iff ξ is in the annihilator p^-k Z_p, else zero by Haar translation invariance. Local finite rational tests are not an implementation of full Haar integration; (4.1) is an established classical identity, imported/derived.

Define on functions T_d f(x)=f(x-d), D_q f(x)=f(x/q), d∈Q_p, q∈Q_p^×. Then

    F_p[T_d D_q f](ξ)=ψ_p(dξ)|q|_p F_p[f](qξ).                (4.2)

This is an exact local Fourier intertwiner, a genuinely nontrivial missing step from finite cyclotomic clocks. It remains valid when q=p or q=1/p, which are **invertible scalars on Q_p**, though multiplication by p is not a unit permutation on Z/p^k Z. Formula (4.2) includes the exact Haar multiplier |q|_p; deleting it is a testable false mutation.

Source-word operations form the affine semidirect group: composition of "translate by d" and "multiply by q" is x↦A x+B. The exact tests preserve the ordered original receipt list and check (4.2) against both the independent accumulated affine pair and explicit action on the ball. The action **on the ball/function alone is NOT history-faithful** (different words may have identical effects); the receipt-decorated free path category retains chronological identity. Source IDs are declared metadata, not physical authentication.

**Important scope boundary:** rational a and ξ are a dense chart, not a complete Q_p evaluator. A nonzero rational-valued function can be tested on this chart, but finite tests of finitely many ξ do not prove continuous Fourier equivalence on all Q_p. The general identity (4.1) is the separate classical proof that justifies it.

## 5. TF-02 — Local Mellin, valuation atoms, and the critical half-density

Normalize multiplicative Haar d^×x such that vol(Z_p^×)=1. Let f=1_(p^j Z_p) with any integer j. For Re(s)>0,

    Z_p(f,s)=∫_(Q_p^×) f(x)|x|_p^s d^×x
            =Σ_(k≥j) p^(-ks)
            =p^(-js)/(1-p^(-s)).                            (5.1)

The code computes exact Fraction values for integer s>=2 and arbitrary finite prefix/tail and rejects fake prime places. With j=0, (5.1) is Tate's local unramified Euler factor. It does not construct Γ_R or analytic continuation. Coefficients are produced with genuine p-valuation shells, and fake composite 6 is rejected as a *place*, though 6 is a lawful scalar on Q_2.

For h a compactly supported log-test and the multiplicative test F(x)=x^(-1/2) h(log x) on positive real x,

    ∫_0^∞ F(x)x^s dx/x
        =∫_R h(t) exp((s-1/2)t) dt.                          (5.2)

At s=1/2+iτ, this is the additive Fourier character ∫ h(t) exp(iτt)dt. If the source half-density is shifted by δ, the transformed exponent gains a REAL drift δt; one accidental cancellation at shifted s does not restore the true source normalization. This is the exact algebraic bridge between multiplicative Mellin and additive log-phase Fourier. The code records the exponent condition as Fraction logic, not proof by floating samples.

## 6. TF-03 — Finite prime observations do NOT determine arbitrary-support Weil tests (a controlled no-go)

Fix an integer cutoff P≥2. Consider two *DECLARED candidate arithmetic source tapes* that agree on every n≤P. One follows the authentic von Mangoldt source Λ(n) for all n; the other changes Λ(p) by δ·log p at the first prime p>P and changes no earlier coefficient. **The mutant is not the authentic Q zeta Euler law, hence NOT a second source-valid candidate once the full source law has been supplied.** This distinction is essential.

For any real even compact test h, the symmetric prime contribution to the completed Weil expression includes

    -2 Σ_(n≥2) Λ(n) n^(-1/2) h(log n).

Under the mutant, the test evaluation changes by

    ΔW(h) = -2 δ log(p) / sqrt(p) * h(log p),                  (6.1)

with the same Gamma and pole pieces in both models.

Construct an explicit compactly supported smooth autocorrelation detecting it. Set ℓ=log p and 0<ε<ℓ/4. Let η(t)=exp(-1/(1-(t/ε)^2)) for |t|<ε and zero otherwise, and φ(t)=η(t-ℓ/2)+η(t+ℓ/2). Then h=φ*tilde φ is C_c^∞, real even, supported in [-(ℓ+2ε),ℓ+2ε]. At t=ℓ, the cross-term yields

    h(ℓ) = ∫_R η(t)^2 dt >0.

Indeed on |t|≤ε/2, η(t)^2≥exp(-8/3), so h(ℓ)≥ε exp(-8/3)>0. Thus finite prime transcripts alone do not identify W on the UNION of all compact support windows across the enlarged candidate-source class.

**Positive control:** if one fixes test functions φ supported in [-a,a] and only mutates p with log p>2a, the prime impulse cannot affect W(φ*tildeφ), since h(log p)=0. Local prime-source finiteness is real and useful. **Negative control:** allowing arbitrary support, or a missing p below exp(2a), breaks that observed-data factorization. Neither control proves or disproves actual Weil positivity.

This is a BOUNDED OBSERVER obstruction, not an intrinsic FuckedField result for authentic ζ. The true Λ tape is defined by a finite arithmetic algorithm for each coefficient; the source law itself can produce the omitted prime when requested. Distinguish incomplete observation from incomplete mathematics.

## 7. CR-04 — Current classification of RH under Simple/IdealHard/Fucked (no unjustified promotion)

- **Finite refutability of falsehood:** Lagarias makes a hypothetical strict counterexample at one integer sufficient to refute RH, and the analytic Weil criterion has a finite negative quadratic-form witness if it fails. This is semidecision of *falsity* in suitable effective certified encodings, not proof of true RH or a universal first-witness bound.
- **IdealHard:** would require proving the relevant global RH target by an accepted finite proof but demonstrating no finite executable construction in a specified execution model. We have **neither** for the actual all-test positivity.
- **Fucked-impossible:** an actual no-go would require a source-certified proof impossibility in a clearly specified theory/toolkit (not merely absence of a known proof), or impossibility of a particular proposed carrier realization. Finite source aliases/fake arithmetic candidates do not establish the former.
- **Fucked-phantom:** would require two *lawful* source realities not distinguishable by every permitted probe but with different RH target. A fake Λ(p) mutant is disallowed by the full authentic arithmetic law and is therefore not such a proof.
- **Current correct label:** RH remains UNRESOLVED; the present research has an **analytic identification + uniform all-test sign proof gap**, plus carrier-specific access obstructions. Do not confuse phi/toolkit, sigma/source-map or mu/probe with a scalar truth probability.

## 8. Nontrivial proof dependencies, falsification gates, and next work

1. **Functor expansion:** build the full restricted adelic tensor functor, not merely rational Qp atoms. Establish compatible S->T bonding of *test functions* and their Fourier transforms with correct Haar scaling (function-level projection/integration, not naïve coordinate deletion). Preserve original event path/cocycle.
2. **Source reconstruction:** prove the analytic Tate idelic zeta integral, Poisson summation, Gamma, pole and half-density match exactly the fully completed original source on the full allowed test class, with quantified truncation error and no nontrivial zero positions imported.
3. **Weil identification:** supply an honest map from multiplicative Tate test functions to compact log tests whose resulting source-derived W equals the signed Weil form, not a mere positive spectral/covariance lookalike. External classical explicit-formula imports must be attributed.
4. **Sign gate:** formulate a coercivity/positivity proof that covers every compact support size and every admissible test, not just bounded finite matrices. Refute with fake 6, shifted log p, non-Euler source, half-density and Gamma mutations, negative spectral directions, and failure of uniform operator convergence.

**Immediate strongest independent test:** Fourier of the local p-adic ball after q=p scaling, contrasted with the blocked finite-ring multiplier. Independently recover (4.1) from orthogonality and (5.1) from valuation shells. Then test a global stage extension over two primes and a continuous Archimedean Gaussian. This splits valid source-map naturality from fake transported-phase diagrams before any RH claim.

## 9. Claim ledger summary and reproducibility

- CR-01 / CR-02: CLASSICAL / MATHEMATICAL ARGUMENT with source dependencies and category qualifiers.
- CR-03: RESEARCH PROPOSAL / UNVERIFIED as a globally optimal carrier; established local objects are classical.
- TF-01: CLASSICAL FOURIER IDENTITY / EXACT RATIONAL-CHART MODEL TESTED.
- TF-02: CLASSICAL MELLIN and variable-substitution / EXACT FRACTION finite tests.
- TF-03: PROVED PAPER bounded-source ambiguity relative to a specifically enlarged candidate class; **NOT** two valid ζ worlds.
- CR-04: UNRESOLVED RH; no proof of undecidability/independence/IdealHard/Fucked class.

Code: \`observational_succ/tate_schwartz_functor.py\`
Tests: \`tests/test_tate_schwartz_functor.py\`
Existing independently constructed finite cyclotomic oracle: \`observational_succ/finite_fourier_carrier.py\`
Existing signed prime/Gamma/pole/half-density source: \`observational_succ/completed_weil_transport.py\`
Existing source-correct Suzuki hierarchy: \`observational_succ/source_weil_hierarchy.py\`
Parent: \`observational_succ/tate_lattice_descent.py\`.

Commands:

    python -m unittest discover -s tests -p 'test_tate_schwartz_functor.py' -v
    python -m unittest discover -s tests -p 'test_tate_lattice_descent.py' -v
    python scripts/verify_provenance.py
    python -m unittest discover -s tests -p 'test_*.py' -v
    python scripts/observer_foundations_probe.py
    python scripts/ordinal_succ_report_probe.py

Citations / primary provenance:
- Tate (1950), *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*, reprinted Cassels–Fröhlich 1967.
- B. Poonen, *Tate's Thesis*, MIT lecture notes, https://math.mit.edu/~poonen/786/notes.pdf .
- J. C. Lagarias, *An Elementary Problem Equivalent to the Riemann Hypothesis* (2002), https://websites.umich.edu/~lagarias/doc/elementaryrh.pdf .
- M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, JLMS 108 (2023), https://doi.org/10.1112/jlms.12785 .
- M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096 (2026), https://arxiv.org/abs/2606.09096 .
- Notes on Tate's thesis, local characteristic Fourier test, https://mcm.amss.cas.cn/people/members/202108/W020140919372982530643.pdf .


## 10. TF-07 — Standard adelic Gaussian tensor with exact original-source phase and volume (CLASSICAL IDENTITY; EXACT RATIONAL-LATTICE RECEIPT)

Consider the actual Schwartz–Bruhat tensor on the rational adeles

    Φ_(q,d,t)(x) =
       exp(-π t ((x_inf-d)/q)^2)
       * product_(all primes p) 1_(d+q Z_p)(x_p),

with q∈Q^×, d∈Q, t∈Q_{>0}, real Archimedean Gaussian and p-adic indicators. **Only finitely many factors differ from the standard 1_(Z_p)**: those with v_p(q)≠0 or v_p(d)<0. The implementation records exactly this finite exceptional atlas plus the original rational generator (q,d,t), which is a legitimate *finite specification of a mathematically infinite object*.

Choose the global additive Fourier pairing with real + phase exp(2πixξ) and p-adic - phase exp(-2πi {xξ}_p), and normalized additive Haar vol(Z_p)=1. By the elementary real Gaussian transform and the local formula (4.1),

    F_A[Φ_(q,d,t)](ξ)
      = (|q|_infty * product_p |q|_p) / sqrt(t)
          * ψ_A(d ξ)
          * exp(-π (q ξ_inf)^2/t)
          * product_p 1_(q^-1 Z_p)(ξ_p).

For rational nonzero q, the coefficient in parentheses is EXACTLY ONE by the product formula. For a **diagonally embedded rational** ξ∈Q, ψ_A(dξ)=1 by additive reciprocity, and the non-Archimedean support condition is equivalent to qξ∈Z (since a rational number belongs to every Z_p exactly when it is an integer). Hence

    F_A[Φ_(q,d,t)](ξ) =
       { t^-1/2 exp(-π (qξ)^2/t),  if qξ∈Z,
         0,                            otherwise }.         (10.1)

Likewise, on diagonal rationals x∈Q,

    Φ_(q,d,t)(x) =
       { exp(-π t ((x-d)/q)^2), if (x-d)/q∈Z,
         0,                    otherwise }.                  (10.2)

**Exact source-indexed receipt:** For each n∈Z, the two surviving rational-lattice points are x=d+qn and ξ=n/q. The primal and Fourier terms have Gaussian exponents respectively t n² and n²/t, with zero global phase and no residual q modulus. Therefore, the classical ADELIC Poisson formula for this bona fide Schwartz test reduces precisely to

    Σ_(n∈Z) exp(-π t n²)
      = t^-1/2 Σ_(n∈Z) exp(-π n²/t).

This derivation **uses genuine analytic Poisson summation**; matching individual terms and index maps is not a proof of equality of the two infinite sums. The existing SUCC theta source and Tate framework import Poisson separately. No RH consequence follows from theta symmetry alone.

**Independent hostile controls:**
- Real scaling |q| without all local |q|_p factors leaves a source-dependent nontrivial modulus.
- Real plus phase without p-adic minus phase leaves a nonzero rational diagonal character at dξ=1/30.
- A finite selection of only the q/d primes misses a new probe prime dividing ξ (e.g. ξ=1/97); the evaluator expands the probe atlas using the original rational source.
- A pure finite ring Z/p^k cannot invert multiplication by p; the actual Q_p-ball carrier can, with the level shift k→k+1 and the correct Haar factor p^-1.
- The translation d is a *real source event* in the event log, even though its diagonal phase cancels in Fourier and one can re-index the integer theta sum; the observed quotient can forget causal history.

Implementation: observational_succ/adelic_schwartz_source.py. Exact rational controls: tests/test_adelic_schwartz_source.py and scripts/tate_schwartz_functor_probe.py. No float is used to assert Gaussian equality; exponent and amplitude are symbolic rational expressions.

## 11. TF-08 — Uniform *finite-source* cutoff for one Weil test-support window (CLASSICAL FINITENESS / EXACT SOURCE CERTIFICATE)

Suppose φ∈C_c^∞(R) is supported in [-a,a] with a>0 rational. Then h=φ*tildeφ is supported in [-2a,2a]. The prime-power side of the completed Weil form can therefore involve only n=p^k with log n<2a (boundary values also vanish for smooth compactly supported h).

Define L=ceil(2a), and N=3^L. Since e<3, one has

    exp(2a) ≤ exp(L) < 3^L=N,

so EVERY active arithmetic impulse satisfies n<N. We can construct all genuine (n,p) with n=p^k<N *using integer arithmetic alone*, without evaluating any exp, gamma or zeta zeros. The conservative finite list is a source cover: it may include extra n with log n>2a, but never misses a relevant genuine event.

This is the exact finite-to-global SUCC receipt for the **PRIME SIDE ONLY** at one support size. The complete Weil evaluation additionally contains a pole part and an Archimedean Gamma distribution, requiring independent analytic bounds. The code does not silently declare the local finite list complete for the full signed form.

For the exhaustive global positivity goal, let a_m=m/2 (m=1,2,...). The supports [-a_m,a_m] are cofinal among compact supports, so global Weil positivity is equivalent (given the classical distributional continuity/identification) to positivity for EVERY m and EVERY test in the corresponding space. Checking finitely many windows cannot close this universal claim.

**Countable dense-test lemma (CLASSICAL):** Each fixed C_c^∞([-a,a]) is a separable Fréchet space under all smooth seminorms; choose a countable dense rational-complex linear span D_a. If Q_a(φ)=W(φ*tildeφ) is continuous on that space, Q_a≥0 on D_a implies Q_a≥0 everywhere by continuity. Conversely, a strict negative witness persists on a neighborhood and can be approximated by an element of D_a, giving a finite-support finite-combination witness. This is a mathematically honest reduction to COUNTABLY MANY finite checks, **not** a finite check or a computation establishing their uniform sign. Actual effective enumeration and rigorous sign bounds require extra work.

**Test-domain caveat:** a fixed signed auxiliary covariance or a finitely sampled Gram matrix may be positive while this entire graded family contains negative directions; moving boundary leakage and lack of uniform lower bounds remain live obstructions.

Implementation: observational_succ/tate_weil_window.py and tests/test_tate_weil_window.py. Genuine prime powers are imported from existing completed_weil_transport.von_mangoldt_labels, not a fitted sample or standalone fake 6.


## 12. TF-09 — The Euler logarithmic derivative is the exact prime-jet-to-Weil arithmetic interface

This is the most direct mathematical answer to the question "how do Tate's multiplicative shells become SUCC's additive log-time impulses?"

Start from the true Tate unramified local zeta integral, initially in Re(s)>0,

    Z_p(s) = Σ_(k>=0) p^(-ks) = (1-p^-s)^(-1).

The **negative logarithmic derivative** is

    -d/ds log Z_p(s)
      = (log p) Σ_(k>=1) p^(-ks).                            (12.1)

At a fixed true prime p the k-th term is carried by the actual multiplicative prime jet p^k; its additive log-time address is t=k log p=log(p^k), with authentic coefficient Λ(p^k)=log p. No zeros or scattering matrix are consulted.

The global Euler product is absolutely convergent in Re(s)>1; there,

    -ζ'(s)/ζ(s)
      = Σ_p -d/ds log Z_p(s)
      = Σ_(n>=2) Λ(n) n^(-s).                                (12.2)

**Domain firewall:** It is INVALID to treat the rightmost Dirichlet series as an ordinarily convergent global sum at Re(s)=1/2. On the Weil side, the compact support of a log-test selects finitely many source impulses, and the Archimedean/pole completion supplies the distributional continuation. A source-positive local log-jet does **not** imply a positive completed Weil form.

**SUCC source-level formalization:** \`local_euler_logjet\` computes exact rational finite prefixes and remainders of Σ_(k>=1)p^(-ks) while storing the real factor as the typed symbolic generator "log p"; \`finite_source_logjets\` independently generates all p^k<=N by true prime-power arithmetic and compares its labels to the existing \`completed_weil_transport.von_mangoldt_labels\` oracle. It rejects the fake standalone n=6 impulse and fake prime p=6. This directly connects Tate's local Mellin factors to the authentic prime-power input consumed by the signed Weil machinery already in SUCC.

**Status:** (12.1) and (12.2) are CLASSICAL theorems/identities, **PROVED PAPER and EXACT FINITE TESTED** in the appropriate declared domains; they do NOT pay the global sign debt.

## 13. CR-05 — An unavoidable two-sided Goldilocks requirement

The source-complete **arithmetic** carrier (integers, true Λ) already determines a unique signed Weil distribution through the classical explicit formula once analytic continuation and domains are imported. There is no known duplicate *authentic* ζ-world with different RH outcome. Thus the Fucked/phantom category is not justified for the true arithmetic source merely by inventing a fake coefficient.

On the other hand, the mere **positive Hilbert-space Fourier representation** of Tate's test functions exists for both genuine and arbitrary mutated arithmetic source labels: Fourier unitarity/Parseval do not depend on the ζ Euler tape at all. Therefore

    Schwartz–Bruhat Fourier compatibility + positive L² norm
          DOES NOT ENTAIL signed completed Weil positivity.

This is an elementary counterexample to the cheap "transport any positive covariance" strategy: the same positive harmonic-analysis framework can be equipped with distinct source distributions, some of which exhibit negative signed Weil-type test values. The source-to-quadratic **identification** is the missing typed morphism.

A useful Goldilocks carrier must simultaneously satisfy:

1. **Fidelity:** source true Λ(p^k), the original finite+real places, phase, Gamma/poles, correct half-density.
2. **Continuity:** a test topology enabling passage from exact finite source windows to the completed Weil distribution.
3. **Rigidity:** sufficiently restrictive structure to derive a sign inequality, not merely to state an equivalent positivity criterion.
4. **Probe completeness:** all compact supports and all legitimate test directions, with honest error/closure bounds.
5. **History:** input source-event/cocycle records remain distinguishable even where quotient states and Fourier characters coincide.

No argument here proves these five conditions can be realized by a sign-positive carrier, let alone that the chosen interface is mathematically optimal. The fourth gate remains exactly RH-hard.

## 14. Next hostile theorem experiment

Attempt to define the source-indexed **log-test Weil functor**

    Tate Schwartz–Bruhat generator Φ
       -> multiplicative norm pushforward f(t)
       -> full prime/Gamma/pole completed Weil distribution W(f*tilde f)

with an honest map of test domains, and compute BOTH original-source signed evaluations and any candidate positive operator evaluations on a DENSE family.

A valid identification must hold for a general generating family (not a single tent), commute with transition/refinement maps, survive fake 6 and χ_4/non-Euler controls, and have errors uniform enough to survive the inductive-limit test topology. **Falsification:** produce φ with rigorously different two sides, or show one side is undefined. **Ambiguity:** finite numerical agreement without a certified bound. **Pass:** a theorem of distributional equality with proven domains, independent derivation or accepted classical source proof. Positivity requires its own further universal proof.
