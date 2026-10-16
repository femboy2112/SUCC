# ASTRA ULTRA — SUCC: FROM CLASSICAL ADELIC POISSON TO SOURCE-COMPLETE TATE/WEIL

You are continuing a serious mathematical research program in **femboy2112/SUCC**. Use the GitHub connector directly, plus primary literature and exact execution capabilities when available. Use maximum available reasoning effort and execute research, proofs, counterexamples, implementations, hostile tests, commits and draft PR updates **in this session**. Do NOT provide only a proposal. RH REMAINS OPEN.

## 0. Actual source baseline, branch and provenance

- Research repository: https://github.com/femboy2112/SUCC
- **Active research branch:** research/pontryagin-finite-adelic-duality-2026-10-15; stacked **draft PR #129** on research/edge-carrier-reconstruction-2026-10-15 (draft PR #127). Earlier work includes Tate lattice descent draft PR #113 and Tate/RH carrier draft PR #120. Never edit main or merge/tag/release/publish without explicit authorization.
- Immediately fetch **current branch HEAD**, the actual state of both draft PRs and CI; do not assume that the commit recorded below is still the latest. The original parent of this branch is 7cc16f9a3a23b0a2f87bd7c9639cd5bd0757209b.
- The completed mathematical core at the Oct 15 checkpoint is documented in:
  - research/2026-10-15/PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md (PD-01–PD-13)
  - research/2026-10-15/ADELIC_SOLENOID_POISSON_RECONSTRUCTION.md (AS-01–AS-12)
  - reviews/2026-10-15_ADELIC_POISSON_HOSTILE_AUDIT.md
  - docs/CLAIM_SUPPLEMENT_PONTRYAGIN_ADELES.md
  - docs/CLAIM_SUPPLEMENT_ADELIC_SOLENOID_POISSON.md
- Working implementation:
  - observational_succ/pontryagin_source_duality.py
  - observational_succ/finite_adelic_character_bridge.py
  - observational_succ/pontryagin_tate_atlas.py
  - observational_succ/finite_cyclic_poisson.py
  - observational_succ/adelic_solenoid_duality.py
  - observational_succ/adelic_poisson_reconstruction.py
  - observational_succ/adelic_gaussian_interval.py
  - scripts/pontryagin_finite_adelic_probe.py
  - .github/workflows/pontryagin-finite-adeles.yml
- Source dependencies: observational_succ/edge_carrier_reconstruction.py, finite_adele_localization.py, tate_lattice_descent.py, adelic_schwartz_source.py, tate_schwartz_functor.py, all_places_zeta.py, completed_weil_transport.py, source_weil_hierarchy.py, source_character_interaction.py, and existing finite_fourier_carrier.py.
- Obey AGENTS.md and provenance/IMPORT_MANIFEST.json. Preserve archival origins; distinguish **mathematical source declarations** from physically authenticated measurements. Inspect/replay actual existing assertions before extending them.
- At commit 8dc7e714dc53e9027610988e13b12e16626ba438, the **focused Python 3.10 and 3.13 suites passed 52/52 tests each**, including exact rational outward Gaussian-tail checks and source provenance verification (https://github.com/femboy2112/SUCC/actions/runs/38816772603). Later review-document commits must be independently rechecked. Full repo validation was still running at that checkpoint; verify current actual status, never invent success.

## 1. Mathematical anchor — what has REALLY been reconstructed

Let Zhat = lim_(n|m) Z/nZ, Af = product'_p(Qp,Zp), A_Q=R x Af, Haar vol(Zp)=1 and real Lebesgue. Choose real Fourier character exp(+2πix) and finite local character exp(-2πi{x}_p). We have classically and in source-indexed exact models:

1. Zhat^vee ≅ (Q/Z)_discrete, with chi_(a/n)(z)=exp(+2πia z_n/n); dual arrows n|m change label a→a(m/n). Every individual continuous character has finite conductor, while **no universal finite conductor exists**.
2. Af/Zhat ≅ Q/Z via pp(x)=sum_p{x_p}_p mod Z; 0→Zhat→Af→Q/Z→0 is exact but has **NO additive group section** (Af torsion-free, Q/Z torsion).
3. A_Q/Q ≅ (R x Zhat)/diag(Z), compact, covolume one; its continuous dual is Q_discrete. The adelic additive pairing is selfdual, and diagonal Q is self-annihilating, Q^perp=Q.
4. The finite-adèle Schwartz–Bruhat space is **exactly spanned by finite rational compact-open indicators** 1_(u+D Zhat), u∈Q, D∈Q_{>0}. Crucial proof ingredients: Af=Q+D Zhat, local constancy, compact support and D Zhat neighborhood base.
5. The Fourier transform of 1_(u+D Zhat) is (1/D) ψ_f(u y) 1_(D^-1 Zhat)(y). At rational diagonal y=m/D, phase equals exp(-2πi um/D).
6. Every f=phi_real ⊗ 1_(u+D Zhat), phi_real Schwartz, reduces global adelic Poisson summation to ordinary real Poisson:
   sum_n phi_real(u+D n) = (1/D) sum_m F_plus(phi_real)(m/D) exp(-2πi um/D).
   Finite linear span proves it for **all** S(A_Q). The analytical input is the CLASSICAL real Schwartz Poisson theorem, not finite sampling.
7. For a shifted Gaussian, the RHS gains the honest phase exp(2πi(a-u)m/D) and amplitude 1/(D sqrt(t)). Fraction-based Gaussian interval tails reject a wrong Haar factor D=2 **rigorously**, but numeric overlap is NOT a global theorem or sign proof.
8. Independent prior SUCC Tate/S atlas and finite adèle phase implementations agree on exact representative charts. This agreement is finite model evidence; mathematical topological proofs are independently documented and credited as CLASSICAL.

Academic priority of Poisson, Pontryagin, Tate, CRT and classical duality is NOT SUCC's. The useful SUCC innovation target is an operational, typed, source-faithful reconstruction/proof calculus and its genuine countermodels.

## 2. MAIN MISSION — execute the NEXT solved-problem benchmark

**Recover the complete classical Tate zeta integral and its functional equation through the newly established source-indexed rational-coset Poisson interface.** Don't merely repeat a textbook statement; create actual SUCC operators, comparisons and theorem-level audits with precise domains.

Start with the standard self-dual mathematical source test
  Phi(x) = exp(-π x_infty²) · product_p 1_(Zp)(x_p).
Build idelic multiplicative Haar d^×x, the norm |x|_A, the original source character, and the global zeta integral Z(Phi,s). For Re(s)>1, recover the **genuine** Euler product ∏_p(1-p^-s)^-1 and real Γ_R(s)=π^-s/2 Γ(s/2) with zero fake composite prime places. Derive continuation and functional equation from the adelic Poisson theorem by splitting norm ≤1 / ≥1 in A^×/Q^×, recording the zero-mode, pole terms, test-function hypotheses and every Haar/covolume factor. Zero positions are NEVER construction inputs.

Independently triangulate:
(A) source-indexed Poisson/idelic Mellin derivation,
(B) original real theta/Mellin derivation with quantified errors,
(C) earlier SUCC all_places_zeta / completed_weil_transport / source_character_interaction.
Require equality of actual analytic objects, not just matching numerical samples. If an attempted equality fails, provide an exact witness and leave it as a no-go claim.

**Crucible:** Next do a nontrivial arithmetic source, preferably primitive odd chi_4 (Dirichlet beta), preserving conductor 4, odd theta weight n*chi_4(n), parity, epsilon/Gauss sum, local Euler factors and Gamma((s+1)/2). This is a required mutation control against a zeta-only or non-Euler black box. Deliberately break (i) real/finite sign, (ii) finite Haar scaling 1/D, (iii) missing prime place, (iv) fake impulse n=6, (v) wrong half-density, (vi) omitted poles/Γ, (vii) wrong conductor/root number, (viii) non-Euler coefficient tape. Failure must be detectable by a typed theorem, exact source counterexample, or independently bounded interval—not handwaving.

## 3. SECOND MISSION — approach the Weil arrow without cheating

Define explicitly an *admissible source-derived log-test or Schwartz–Bruhat test functor* from Tate data to the **COMPLETE signed** Weil distribution on its legitimate test space. Quantify source identity, continuous domains, norms, topology, prime Λ(p^k), Gamma, poles, half-density, conductor and Archimedean corrections. If classical Weil's explicit formula is imported, LABEL IT AS AN EXTERNAL CLASSICAL THEOREM and explain what SUCC independently derives versus assumes. Prove commuting/naturality squares with actual maps and provide uniform error domains; one tent test is not an all-test identification.

Investigate exactly what additional source arithmetic rigidity might yield full sign positivity **without assuming RH**. The GNS Hilbert completion with inner product equal to Weil's form exists as a positive carrier iff the form is PSD; treating it as unconditionally positive is circular. A positive Fourier/Parseval Hilbert norm is NOT automatically the signed Weil form. Require fake 6, non-Euler, half-density and signed negative controls.

If full identification fails or an obstruction is proved, preserve a precise theorem/counterexample. Do not claim RH solved, nor categorize RH as IdealHard/Fucked without a proof relative to an explicit carrier, observer, toolkit and logical system.

## 4. Academic execution contract and outputs

Work only on a **fresh child non-main branch**, starting from the latest source branch head. Keep existing PRs and archival source untouched; create a clearly stacked DRAFT PR, unless an existing designated research branch/PR is explicitly the correct landing area. Write theorem statements with objects, hypotheses, domains, quantifiers and sign conventions; split CLASSICAL IMPORT / PROVED PAPER / TESTED MODEL / UNVERIFIED / REFUTED. Include an abstract, independent citation/provenance section, source-vs-proof status table, failure controls and a detailed reproduction recipe.

Build executable exact Fraction/cyclotomic/CRT and source-authentic prime controls. Use externally derived analytical bounds or rigorous interval arithmetic for numerical claims. Maintain the existing Python 3.10/3.13 focused checks, then run provenance and full repository validation:
  python scripts/verify_provenance.py
  python -m unittest discover -s tests -p 'test_*.py'
  python scripts/observer_foundations_probe.py
  python scripts/ordinal_succ_report_probe.py
Also examine existing Lean infrastructure; formalize one manageable discrete lemma if available and build-verifiable, but do NOT pretend to have formalized infinite Tate Poisson without a proof assistant run.

Commit coherent research checkpoints, push the branch, preserve logs, update a claim ledger and review dossier, and report the **exact head SHA, draft PR URL, CI outcomes, genuinely established claims, genuinely refuted ideas, and remaining proof debts**. If context/time is limited, prioritize a smaller rigorous theorem and saved exact failure cases over impressive but unsupported breadth.

Do not ask me to restate context already in the repository. Make discoveries, try to break them, refine, preserve the strongest defensible result and **continue moving SUCC from mathematical demos toward professionally reviewable, source-faithful theorem construction**.

**Mandatory final line in research artifacts:** RH PROVED: NO (unless a complete globally audited proof genuinely exists).
