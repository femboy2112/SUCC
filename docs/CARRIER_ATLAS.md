# Carrier Atlas

[Principia and ancestral closure](PRINCIPIA_CONNECTION.md) supplies historical
context for successor constructions. The accompanying
[reachability criterion](CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md) checks whether
composing observed arrows creates endpoints unavailable from the selected source;
it does not replace the stronger action, cost, and trace contracts below.

**The mathematical backbone of Observational SUCC.** Every row is a *carrier reconstruction*:
a smaller source carrier and a set of admissible categorical operations build an equivalent
interface to a larger or transformed carrier. The point is never "bigger sets"; it is
**constructing a lawful interface to the larger carrier from smaller source carriers and their
admissible edges**, with explicit accounting of which structure survives.

**Read the types literally.** A proper embedding is **not** an isomorphism; a dense inclusion is
**not** an equality; a finite executable chart is **not** the full (often uncountable) carrier; and
**no carrier equivalence in this atlas produces Weil positivity or bears on RH** — that arrow is
isolated as RH-hard (see [RESEARCH_FRONTIER_2026-10-15.md](RESEARCH_FRONTIER_2026-10-15.md)).
Status vocabulary follows [AGENTS.md](../AGENTS.md). **RH remains OPEN. RH PROVED: NO.**

Canonical source of the master table: `observational_succ/edge_carrier_reconstruction.py::carrier_interface_contract()`.
All arithmetic is exact (`Fraction`/`int`); finite code certifies only its coded examples.

## 1. Algebraic and topological carrier reconstructions

| Original carrier | Construction | Resulting carrier | Comparison map | Strength | Preserved | Lost / embedding | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| free one-object successor-loop category B(N), Hom(*,*)=N | group completion: formally invert generating loop s | one-object groupoid B(Z), Hom(*,*)=Z | group-completion unit N→Gr(N) | iso (Gr(B(N))≅B(Z)); source inclusion N→Z is a proper embedding | identity, composition, inverses, Z-torsor action | nothing (N cancellative ⇒ injective); B(N)≄B(Z) as categories | CLASSICAL / PROVED PAPER / FINITE EXACT TESTED | edge_carrier_reconstruction.py:488; EC-01 |
| ring Z | localize at S=Z∖{0} (invert every nonzero integer) | fraction field Q | localization map Z↪S⁻¹Z=Q | iso (S⁻¹Z≅Q); source inclusion Z→Q is a proper embedding | 0,1,+,*, inverses of nonzero integers | nothing (domain ⇒ injective) | CLASSICAL / PROVED PAPER / FINITE EXACT TESTED | edge_carrier_reconstruction.py:497; EC-02 |
| polynomial presentation Z[X]/(X²+1) | quotient ring by relation X²+1 | Gaussian integers Z[i] | evaluation X↦i | iso (genuine ring isomorphism) | complex multiplication, conjugation, norm | nothing | CLASSICAL / PROVED PAPER / FINITE EXACT TESTED | edge_carrier_reconstruction.py:505; EC-03 |
| inverse system {Z/nZ, divisibility bonding n\|m} | inverse limit limₙ Z/nZ; CRT across all n | profinite ring Ẑ ≅ ∏_p Z_p | canonical projections; diagonal Z→Ẑ | iso by definition (inverse limit IS Ẑ; CRT gives ∏Z_p); diagonal Z→Ẑ is a proper DENSE embedding, NOT a ring iso | all compatible residues, +,*, profinite topology, CRT idempotents | finite-code description of a general point (Ẑ uncountable; only a subclass has finite programs) | CLASSICAL / PROVED PAPER / FINITE EXACT CRT TESTED | edge_carrier_reconstruction.py:513,517,557; EC-05 |
| Gaussian rational field Q(i) | metric completion w.r.t. complex absolute value | field of complex numbers C | inclusion Q(i)↪C | iso (completion≅C as complete topological field); Q(i)→C is a proper dense subfield embedding | field operations, complex norm, complete topology | finite computable name of a general point (uncountable; non-computable points exist) | CLASSICAL / PROVED PAPER + EXACT √2+ir SPECIMEN | edge_carrier_reconstruction.py:523,525; complex_cauchy_edge.py; EC-04 |
| profinite ring Ẑ with nonzero integers inverted | localization S⁻¹Ẑ (equivalently Q⊗_Z Ẑ) | finite adele ring A_f(Q), restricted product (Q_p,Z_p) | inclusion Ẑ↪A_f | iso (A_f≅Q⊗Ẑ≅S⁻¹Ẑ); Ẑ→A_f is a proper compact-open subring embedding | ring operations, restricted-product (Haar-compatible) topology | finite-code description of a general adele; equality not decided by finitely many residues | CLASSICAL / PROVED PAPER / FINITE-RATIONAL PRESENTATIONS TESTED | edge_carrier_reconstruction.py:531,533; finite_adele_localization.py; EC-06 |
| R together with full finite adele ring A_f(Q) | product of archimedean and finite-adelic carriers | full adele ring A_Q = R × A_f | identity product map | iso (A_Q=R×A_f) | true Archimedean topology + restricted finite places | full R (a rational Archimedean coordinate is only a dense local chart, not R) | CLASSICAL | edge_carrier_reconstruction.py:539; finite_adele_localization.py (RationalArchimedeanAdeleChart); EC-06 |
| profinite ring Ẑ | Pontryagin dual Hom_cont(Ẑ, Circle) with compact-open topology | discrete group Q/Z | Φ: r=a/n ↦ χ_r, χ_r(x)=exp(2πi·a·x_n/n) | iso (topological group isomorphism onto Q/Z discrete) | additive group law, naturality under residue reduction, conductor | nothing at dual level (each character has finite conductor); no single finite clock detects all characters | CLASSICAL (PONTRYAGIN) / finite phase layer EXACT TESTED | pontryagin_source_duality.py:1-13; PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md:87 |
| finite adeles modulo Ẑ: A_f/Ẑ | quotient by Ẑ; p-primary principal parts | discrete Q/Z ≅ ⊕_p (Q_p/Z_p) | principal-part map pp; diagonal Q | iso (A_f/Ẑ≅Q/Z) | p-primary local classes, additive structure | no additive group section (quotient does not split) | CLASSICAL | tate_adele_quotient_descent.py:1-9,88; PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md:145 |
| adele class group A_Q/Q (with Tate self-dual pairing) | additive quotient; ψ pairing (x,y)↦ψ(xy) | compact solenoid A/Q≅(R×Ẑ)/Z; Pontryagin dual (A/Q)^∨≅Q | self-dual pairing, Q^⊥=Q | iso / self-dual (Q discrete cocompact, self-annihilating, vol(A/Q)=1) | additive structure, self-duality | n/a (discrete Q is the full dual) | CLASSICAL | PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md:215; CARRIER_TATE_WEIL_SYNTHESIS.md §2 |
| finite 4^k dyadic Hilbert address cells (finite executable chart) | nested 2D Hilbert ordering, order→∞ limit | continuous measure-preserving surjection [0,1]→[0,1]² | Hilbert limit map | quotient/surjection (NOT injective, NOT bi-Lipschitz/Sobolev); finite path is NOT the limit | Lebesgue measure, L² inner products | injectivity, H¹ derivatives, inverse locality; finite centers never cover the continuum | CLASSICAL (Hilbert/Butz/Schoenfeld) + PROVED LOCAL finite (bijective/self-inverse through k=5) | hilbert_carrier.py:1-10; CLAIM_SUPPLEMENT_HILBERT_CARRIER.md HC-01..HC-03 |

## 2. Harmonic / dual carrier interfaces

| Local / harmonic object | Construction / formula | Resulting interface | Strength | Exactness | Preserved | Lost / boundary | Status | Evidence |
|---|---|---|---|---|---|---|---|---|
| Q_p local additive character + Haar | psi_p(y)=exp(-2πi {y}_p), vol(Z_p)=1, F[1_{a+p^kZ_p}](ξ)=p^{-k}psi_p(a·ξ)1_{p^{-k}Z_p}(ξ) | self-dual local Fourier on a dense rational chart of S(Q_p) | embedding (rational chart ⊂ Q_p), NOT isomorphism onto full S(Q_p) | exact (Fraction phases/volumes), classical statements imported | translation/dilation Fourier intertwining, self-dual Haar, affine covariance | completeness of Q_p (only dense rational chart) | CLASSICAL / FINITE EXACT TESTED | tate_schwartz_functor.py:66-142 |
| Rational adelic solenoid A/Q | (R×Ẑ)/Z via A_f=Q+Ẑ, Q∩Ẑ=Z | compact carrier, covolume 1, Q discrete+closed | topological isomorphism (proved, not assumed) | classical (half-open domain=covolume, compact closure=compactness) | compactness, covolume 1, discreteness of diagonal Q | profinite points lack finite names (access boundary only) | CLASSICAL / PAPER PROVED | adelic_solenoid_duality.py; reviews/2026-10-15_CARRIER_POISSON_INDEPENDENT_AUDIT.md §3 |
| Pontryagin duality of carrier | Ẑ^∨=Q/Z (each char finite conductor), (A/Q)^∨=Q_discrete, χ_q([t,z])=exp(2πi[qt-pp(qz)]) | full discrete dual Q; jointly-faithful character family | isomorphism onto dual (classical) | classical + exact cyclotomic orthogonality oracle | character group laws, finite-conductor factorization | no uniform finite clock detects every continuous character (flagged, not a defect) | CLASSICAL / FINITE EXACT TESTED | pontryagin_source_duality.py:178-304 |
| Schwartz–Bruhat finite-adele span | S(A_f)=span 1_{u+D Ẑ}; **integer scale D with rational u suffices** by disjoint coset refinement | exact finite-tensor spanning set for S(R)⊗_alg S(A_f) | spanning/basis equality (EXACT, not merely dense) | PAPER PROVED; probe-verified disjoint decomposition | algebraic exact span; integer-scale sufficiency (CTW-02) | restricting BOTH scales and translates to integers fails | CLASSICAL / PAPER PROVED (**corrects parent necessity claim**) | adelic_poisson_reconstruction.py:288-308; CLAIM_SUPPLEMENT_CARRIER_TATE_WEIL.md:11 (CTW-02) |
| Adelic Poisson summation | Σ_{q∈Q} f(q)=Σ_{q∈Q} f^(q) on S(A)=S(R)⊗_alg S(A_f), two routes | genuine Schwartz–Bruhat adelic Poisson theorem | reduction/equality via real-Poisson route and compact-quotient Fourier-inversion route | PAPER PROVED CONDITIONAL on classical real Poisson / LCA; explicit seminorm tail bounds | absolute convergence, negative inverse sign, Haar 1/D, rational reciprocity ψ(q)=1 | not a proof of real Poisson from SUCC axioms; no infinite numeric ω-sum | CLASSICAL / PAPER PROVED | ADELIC_SOLENOID_POISSON_RECONSTRUCTION.md §8 |
| Mellin / idelic zeta integral | Gaussian⊗∏1_{Z_p} → Gamma_R(s)ζ(s), Re(s)>1; Z_R(e^{-πx²},s)=π^{-s/2}Γ(s/2) | completed Mellin transform of the canonical Tate source | identification on Re(s)>1 then classical continuation/poles/FE (import) | PAPER PROVED; exact shell/source finite tests | unit-shell Haar mass 1, meromorphic residues, functional equation | infinite Euler product needs absolute convergence; no numeric proof of continuation | CLASSICAL / PAPER PROVED | tate_idelic_zeta.py:181-271; classical_tate_arch_global.py:33 |
| Archimedean Gamma factor | Gamma_R(s)=π^{-s/2}Γ(s/2) (explicitly **not** Γ(s) nor Gamma_R(s)/2) | the single correctly normalized completed-zeta archimedean factor | exact equality on positive even integers; digamma log-derivative elsewhere | EXACT π-monomial chart | π^{-s/2}Γ(s/2) normalization, log-derivative (ψ(s/2)-log π)/2 | general noninteger s uses actual Γ (analytic, not rational-exact) | CLASSICAL / EXACT | tate_idelic_zeta.py:181-190; tate_central_reflection.py:184 |
| Root-number / log-derivative kernel | overall nonzero scalar vanishes under d/ds log; differentiated FE drops displayed root constant | exact observation kernel + narrow recovery boundary | REFUTED (scalar recoverable from log-deriv) but NOT universal impossibility | exact scalar kernel; w=(-1)^{ord_{1/2}F} from full data + self-duality | atoms -Λ(n)χ(n)/√n recoverable; central-order parity route to w | finite coefficient/formula check alone cannot authenticate supplied root metadata | REFUTED (CTW-11), with correct recovery caveat | tate_weil_distribution.py:97-114; TATE_TO_WEIL_DISTRIBUTION.md:400 |

## 3. Typed status — which arrows are isomorphisms, which are embeddings

- **Genuine algebraic isomorphisms** (the *construction* of the source is isomorphic to the target):
  Gr(B(N))≅B(Z); S⁻¹Z≅Q; Z[X]/(X²+1)≅Z[i].
- **Complete topological isomorphisms:** completion(Q(i))≅C; limₙ Z/nZ≅Ẑ≅∏Z_p; S⁻¹Ẑ≅A_f;
  R×A_f≅A_Q; Ẑ^∨≅Q/Z; A_f/Ẑ≅Q/Z; (A_Q/Q)^∨≅Q.
- **Proper embeddings (NOT isomorphisms of the un-completed sources):** N→Z; Z→Q; Z→Ẑ; Q→A_f;
  Q(i)→C; Z[i]→C. *An equivalence between completed objects does not mean the original smaller
  carriers were already equivalent* — e.g. `Gr(B(N))≅B(Z)` does not say the monoid N≅Z.
- **Finite executable fragments only:** loop words, `RationalSpan`, `GaussianRational`, rational
  Cauchy names, finite-recipe `ProfiniteProgram`/`FiniteAdeleSpan`, 4^k Hilbert cells. The full
  inverse limit / completion is uncountable; only a subclass has finite programs.

## 4. Dependency arrows

```
B(N) --group completion--> Z --localize S⁻¹--> Q --adjoin i--> Q(i) --metric completion--> C
{Z/nZ} --inverse limit--> Ẑ --(CRT)--> ∏Z_p --localize--> A_f --×R--> A_Q
Ẑ --Pontryagin--> Q/Z ;  A_f/Ẑ ≅ Q/Z ;  A_Q/Q self-dual, (A_Q/Q)^∨ ≅ Q
local self-dual Fourier → solenoid + Q^⊥=Q → Pontryagin dual Q → finite-adele integer-scale span
    → adelic Poisson → idelic Mellin → Gamma_R·ζ → completed signed Weil distribution
                                                                     ↓  [FIREWALL]
                                              autocorrelation positivity / RH  (OPEN)
```

Every arrow above the firewall is a CLASSICAL theorem (real Schwartz Poisson, LCA/Pontryagin
duality, compact-group character orthogonality, Stone–Weierstrass) realized as an exact finite
source chart. **The final arrow — carrier ⇒ source-derived PSD Weil form ⇒ RH — is UNVERIFIED
RH-HARD (EC-09) and does not follow from any equivalence in this atlas.**

## 5. Firewall

A positive Hilbert/measure covariance is **never** identified with the signed completed Weil form.
Weil-positivity shortcuts CTW-12 (ζ Weil distribution negative on a log2 bump, W<−19/75) and CTW-13
(self-duality + Euler factors + normalized poles do not force positivity) are **REFUTED** with
explicit negative certificates. The completed signed Weil distribution is isolated as a separate
RH-hard arrow (PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md §9; CARRIER_TATE_WEIL_SYNTHESIS.md §1).
**RH remains OPEN.**

## Evidence

`observational_succ/`: `edge_carrier_reconstruction.py`, `finite_adele_localization.py`,
`complex_cauchy_edge.py`, `pontryagin_source_duality.py`, `pontryagin_tate_atlas.py`,
`tate_adele_quotient_descent.py`, `source_field_inverse_limits.py`, `prime_completion_obstructions.py`,
`hilbert_carrier.py`, `tate_schwartz_functor.py`, `tate_idelic_zeta.py`, `tate_weil_distribution.py`,
`rh_arithmetic_carrier.py`, `hilbert_weil_atlas.py`. Docs:
`CLAIM_SUPPLEMENT_EDGE_CARRIER_RECONSTRUCTION.md`, `CLAIM_SUPPLEMENT_HILBERT_CARRIER.md`,
`CLAIM_SUPPLEMENT_CARRIER_TATE_WEIL.md`. Research: `research/2026-10-15/PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md`,
`CARRIER_TATE_WEIL_SYNTHESIS.md`, `ADELIC_SOLENOID_POISSON_RECONSTRUCTION.md`,
`EDGE_CARRIER_RECONSTRUCTION_LAB.md`.
