# A Carrier-First Foundation for Observational SUCC

**A synthesis of the October 2026 carrier-reconstruction program.** 2026-10-15. Integration head
`42f5485`.

## Abstract

Observational SUCC is reframed here as a mathematical research framework for **constructing,
relating, completing, and observing mathematical carriers through lawful source-indexed
transitions**, with explicit accounting of which structure, information, proof authority, and causal
history survive each transformation. The central object is not "a bigger set" but an *equivalent
interface* to a larger carrier built from smaller source carriers and their admissible categorical
edges. We take the classical carrier reconstructions (group completion, localization, quotient
presentation, profinite/CRT inverse limit, metric completion, finite/full adèles, Pontryagin
duality, Tate/Mellin/Poisson transport) as the established mathematical starting point, and propose
*source-indexed observational structure* — which transition was lawfully available to a finite
observer, and what it costs in information — as the SUCC-specific extension. The framework is
**independent of the Riemann hypothesis**; RH is a demanding downstream application. **RH remains
OPEN; no construction in this synthesis certifies Weil positivity.**

## 1. Notation and conventions

Carriers: `N, Z, Q, R, C, Ẑ=lim Z/nZ≅∏_p Z_p, Q_p, A_f=Q⊗Ẑ, A_Q=R×A_f`. One-object categories
`B(M)` with `Hom(*,*)=M`. Local additive character `psi_p(y)=exp(-2πi{y}_p)`; global
`psi(x)=exp(2πi[x_∞ - Σ_p{x_p}_p])`; forward Fourier `f^(y)=∫_A f(x)psi(xy)dx`. Haar: `vol(Z_p)=1`,
`vol(D·Ẑ)=1/D` for rational `D>0`; real Lebesgue. Archimedean factor `Gamma_R(s)=π^{-s/2}Γ(s/2)`.
All computational witnesses are exact (`Fraction`/`int`) unless a transcendental `Γ`/`ψ` evaluation
is explicitly used with an outward-rounded enclosure.

## 2. The carrier reconstruction certificate (proposed general schema)

A **carrier reconstruction certificate** is the typed record we attach to every reconstruction.
Treat the schema as a *proposed* general SUCC object; no theorem establishes its universality.

1. **Source category and law** — the smaller carrier and the algebraic/topological law it carries.
2. **Allowed morphisms and completion** — the admissible edges (completion, localization, quotient,
   limit, duality, Fourier/Mellin/Poisson) and their legal compositions.
3. **Target carrier** — the larger or transformed carrier produced.
4. **Universal property** — the property the construction satisfies (initial/terminal, adjoint
   unit, limit cone, self-dual pairing).
5. **Source-preserving comparison map** — the explicit map from source into / onto target, with its
   exact direction.
6. **Faithfulness and information-loss conditions** — isomorphism vs embedding vs quotient vs dense
   inclusion; what is preserved, and the exact kernel/quotient/inaccessible distinction lost.
7. **Observation / proof-access conditions** — which finite observer toolkit can realize the
   interface (Simple / IdealHard / Fucked / Unresolved; see
   [OBSERVER_PROOF_ACCESS.md](../../docs/OBSERVER_PROOF_ACCESS.md)).
8. **Reproducible verification** — the exact finite test and its receipt.

The master instance of this schema is `edge_carrier_reconstruction.py::carrier_interface_contract()`;
the complete populated table is [CARRIER_ATLAS.md](../../docs/CARRIER_ATLAS.md).

## 3. Core propositions (status-labeled)

All are CLASSICAL mathematics realized as exact finite source charts; the finite code certifies only
its coded examples.

- **P1 (group completion).** `Gr(B(N)) ≅ B(Z)`; the unit `N→Z` is an injective, **non-surjective**
  embedding. An equivalence of completions does **not** assert `N ≅ Z`.
- **P2 (localization).** `S⁻¹Z ≅ Q` for `S=Z∖{0}`; `Z→Q` proper embedding.
- **P3 (presentation).** `Z[X]/(X²+1) ≅ Z[i]`; genuine ring isomorphism.
- **P4 (profinite limit + CRT).** `limₙ Z/nZ ≅ Ẑ ≅ ∏_p Z_p`; the diagonal `Z→Ẑ` is a proper **dense**
  embedding; CRT idempotents close exactly (`e_2+e_3≡1`, `e_2·e_3≡0 mod 12`). A general profinite
  point has **no** finite program (Ẑ uncountable).
- **P5 (metric completion).** `completion(Q(i)) ≅ C`; `Q(i)→C` proper dense subfield; an exact
  `√2+ir` Cauchy specimen with a parity-irrationality proof witnesses non-computable points.
- **P6 (adèles).** `S⁻¹Ẑ ≅ A_f ≅ Q⊗Ẑ`, `A_Q = R×A_f`; equality of adèles is **not** decided by
  finitely many residues; a rational Archimedean coordinate is a dense **chart**, not R.
- **P7 (Pontryagin duality).** `Ẑ^∨ ≅ Q/Z`, `A_f/Ẑ ≅ Q/Z ≅ ⊕_p Q_p/Z_p`, `(A_Q/Q)^∨ ≅ Q` with the
  self-dual pairing and `Q^⊥=Q`; each character has finite conductor; no uniform finite clock sees
  all characters.
- **P8 (adelic Poisson).** `Σ_{q∈Q} f(q) = Σ_{q∈Q} f^(q)` on `S(R)⊗_alg S(A_f)`, proved two
  dependency-distinct ways; **CONDITIONAL** on classical real Poisson / LCA duality (imports, not
  SUCC outputs).
- **P9 (idelic Mellin).** canonical `Gaussian⊗∏1_{Z_p}` integrates to `Gamma_R(s)ζ(s)` on `Re(s)>1`;
  continuation/poles/functional equation are classical imports; the archimedean factor is the single
  `Gamma_R(s)=π^{-s/2}Γ(s/2)` (not `Γ(s)`, not halved).
- **P10 (finite-adèle spanning — corrects parent).** `S(A_f)=span{1_{u+DẐ}}`, and **integer scales
  `D∈Z_{>0}` with rational translates already span** by disjoint coset refinement. The earlier
  "noninteger scales necessary" necessity claim is **REFUTED** (CTW-02).

## 4. Counterexamples and no-go results preserved

- **Nonexistence / noncompact escape:** every finite horizon satisfiable, empty global limit.
- **Phantom source-map:** `∀N∃z`, `¬∃z∀N` (profinite CRT ghost; even-coordinate phantom).
- **Toolkit nonidentifiability:** hidden-tag states indistinguishable for all words.
- **Signed Weil countermodels:** CTW-12 (ζ Weil distribution negative on a log2 bump, W<−19/75),
  CTW-13 (self-duality + Euler factors + poles do not force positivity), and the ordinal negative
  control (a terminating normalizer reaches schur=−3). **Finite PSD Grams never certify the global
  sign; strong operator convergence need not be norm convergence.**

## 5. Computational verification

`python -m compileall -q observational_succ tests scripts` (exit 0); `python scripts/verify_provenance.py`
(`SOURCE_PROVENANCE_VERIFIED`, `establishes_mathematical_truth: false`, 72 items);
`python -m unittest discover -s tests -p 'test_*.py'` (4338 tests OK at the integration head).
Per-reconstruction exact receipts live beside each module and in `research/2026-10-15/`.

## 6. Bounded originality statement

The carrier reconstructions in §3 are **classical mathematics**; SUCC does **not** claim to have
invented group completion, localization, profinite limits, completion, adèles, Pontryagin duality,
or Tate/Poisson transport. What the project proposes as its own contribution is the **source-indexed
observational layer**: the typed certificate schema of §2, the Simple/IdealHard/Fucked/Unresolved
proof-access taxonomy, the no-ghost gluing discipline, and the exact finite source charts and
preserved counterexamples. None of these establishes RH, Weil positivity, or any physical ontology;
the physical-carrier motivation is kept strictly separate from the mathematics. **RH remains OPEN.**
