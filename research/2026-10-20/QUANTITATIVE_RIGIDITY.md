# The quantitative rigidity core (Deliverable B, Part III)

**Date:** 2026-10-20. **Branch:** `research/rigidity-forge-2026-10-20`.
**Module:** `observational_succ/quantitative_rigidity.py`. **Tests:**
`tests/test_quantitative_rigidity.py` (**14 OK**). Everything is exact
(sympy `Rational`/symbolic); a float is never a certificate. Status of the named
theorems: **CLASSICAL** (Schur/Haynsworth, Douglas, closed-form theory); the
contribution is a reusable exact certificate layer plus the counterexample corpus
that separates a genuine global certificate from an invalid finite surrogate.

The module is deliberately **not** organized around one scalar "rigidity score."
Rigidity is a vector of independent obligations (`RigidityDiagnostics`): source
adequacy, range inclusion, spectral gap, inverse-response sign, true Schur
positivity, and the (separate, non-load-bearing) sufficient surrogate.

---

## 2.1 Finite exact Schur theorem

**Theorem (D > 0).** Let `M = [[A, B],[B*, D]]` be real symmetric with `D ≻ 0`. Then
`M ⪰ 0  ⇔  A − B D⁻¹ B* ⪰ 0`.

**Proof (square completion).** For `x ⊕ y`,
`Q(x⊕y) = ⟨A x, x⟩ + 2⟨B* x, y⟩ + ⟨D y, y⟩
        = ⟨(A − B D⁻¹ B*) x, x⟩ + ⟨D (y + D⁻¹B* x), (y + D⁻¹B* x)⟩.`
Since `D ≻ 0`, the second term is `≥ 0` and vanishes for `y = −D⁻¹B* x`. Hence the
infimum of `Q` over `y` at fixed `x` is `⟨(A − B D⁻¹B*)x, x⟩`, so `Q ⪰ 0` on the whole
space iff the Schur complement `S = A − BD⁻¹B*` is PSD. ∎
The identity is verified exactly (`square_completion_identity`), with no irrational
`D^{1/2}`: the completed term is written `⟨D(·),(·)⟩`, not `‖D^{1/2}(·)‖²`.

**Exact certificates.**
- PD: Sylvester (leading principal minors `> 0`). PSD: **all** principal minors `≥ 0`
  (the leading-only criterion is for PD; the trap `[[0,0],[0,−1]]` has leading minors
  `0,0` yet is indefinite — caught by the full-minor test).
- Negative witness: when `M` is not PSD, `negative_witness` returns an **exact**
  rational `v` with `vᵀMv < 0` (a numeric eigenvector only *guides* the search; the
  returned `v` is verified exactly).
- `coupling_negative_vector`: given `x` with `⟨Sx,x⟩ < 0`, returns the exact
  full-space `v = (x; −D⁻¹B*x)` realizing `vᵀMv = ⟨Sx,x⟩` — the direct negative
  vector that exposes a compressed/restricted "certificate" (Gemini 1.1).

**Hostile controls (tests).** wrong-inverse surrogate (1.1/1.2); wrong high block
`D ⊁ 0` (1.7, `A=(1),D=(−1),B=0`: complement `= A > 0` but `M` indefinite);
range-inclusion failure.

**Extension (D ⪰ 0 singular).** With the Moore–Penrose pseudoinverse `D⁺` and the
**range inclusion** `ran(B*) ⊆ ran(D)` (equivalently `(I − D D⁺)B* = 0`), the shorted
operator `A − B D⁺ B*` governs, and `M ⪰ 0 ⇔ shorted ⪰ 0`. If the range inclusion
**fails**, `M` cannot be PSD (the coupling leaks outside `ran(D)`). This is the
correct generalized Schur / shorted-operator form; `shorted_complement`,
`range_inclusion_holds`, `finite_schur_certificate` implement and test all cases.
**Classical comparison:** Douglas's lemma (`B* = D^{1/2}W` solvable with `W` bounded
iff `ran(B*) ⊆ ran(D^{1/2})` iff the range inclusion); Haynsworth Schur-complement
PSD criterion.

## 2.2 Gapped vs gapless (infinite-dimensional statement)

Write `B* = D^{1/2} W` (Douglas; `W` bounded under the range condition). The
square-completion identity becomes
`Q(x⊕y) = ⟨(A − W*W) x, x⟩ + ‖D^{1/2} y + W x‖²`, with `W*W = B D⁻¹ B*` (gapped) or
its shorted analogue (gapless). Two regimes:

- **Gapped** `D ⪰ κ I`, `κ > 0`: `D⁻¹` is bounded (`‖D⁻¹‖ ≤ κ⁻¹`), `W = D^{−1/2}B*`
  bounded, and the finite theorem extends verbatim; the Schur complement is a bounded
  form and positivity transports.
- **Gapless** `D ⪰ 0`, `0 ∈ σ(D)`: `D⁻¹` is unbounded; one must use `D⁺`/`D^{1/2}`
  with the range condition `ran(B*) ⊆ ran(D^{1/2})`, and may not freely compose a
  symbolic `D†` with every vector. **Witness that the gap genuinely fails:**
  `D = diag(1, 1/2, 1/3, …)` (`inverse_decay_block`): every finite compression is
  strictly coercive (`min eig = 1/N > 0`), yet `inf σ(D) = 0`, so no uniform gap `κI`
  survives the limit (`uniform_gap_profile` tabulates `1/N → 0`, exact). This is the
  obstruction class the Gemini master identity omitted (1.8).

The valid high-subspace positivity is relative to the original metric, **not
automatically a gap `κI`** — the standing SUCC caution, here made exact.

## 2.3 Form-core positivity transport

**Theorem.** Let `q` be a closed, lower-bounded quadratic form on a Hilbert space
`H`, with lower bound `m` and form norm `‖f‖_q² = q[f] + (1−m)‖f‖²`. Let `C ⊆ Q(q)`
be a **form core** (dense in `Q(q)` in the form norm). If `q[f] ≥ 0` for all `f ∈ C`,
then `q[f] ≥ 0` for all `f ∈ Q(q)`.

**Proof.** `f ↦ q[f]` is continuous in the form norm (`|q[f]−q[g]|` is controlled by
`‖f−g‖_q(‖f‖_q+‖g‖_q)` via the polarization of the closed form). For `f ∈ Q(q)` take
`f_n ∈ C` with `‖f_n − f‖_q → 0`; then `q[f] = lim q[f_n] ≥ 0`, since `{q ≥ 0}` is
closed under form-norm limits. ∎

**Necessity of a true form core (the negative control).** Form-norm density is
essential — mere `L²`-density is insufficient. `form_core_negative_control(N)` builds
an exact finite truncation of an **unbounded indefinite** form on `ℓ²`: coordinate 1
carries weight `−9` (so `q[e₁] = −9 < 0`), coordinates `2..N` carry weight `n²`, and
the test subspace is `ker φ`, `φ(f) = f₁ − a·Σ_{n≥2} f_n`, with `a` the coefficient of
a **discontinuous** functional (so `ker φ` is `L²`-dense yet its form-closure misses
`e₁`). On the test subspace the restricted Gram is `G = diag(j²) − 9a²·𝟙𝟙ᵀ`, which is
**PD** for every finite `N` when `a² < 1/(9 Σ_{j=2}^N j⁻²)` (certified exactly, with a
certified rational coercivity margin). So `q > 0` on an `L²`-dense set while
`q[e₁] = −9 < 0` globally: **"q ≥ 0 on an L²-dense set" does not certify "q ≥ 0".**
The certifying set must be a genuine form core.

**Distinctions kept separate** (each a predicate, never merged): Hilbert-norm density;
form-norm density; closedness; uniform coercivity; simple nonnegativity; source
identification. Connection: this is exactly the discipline
`research/2026-10-19/ORIGINAL_SOURCE_FORM_CLOSURE.md` needs for the original
Suzuki/Γ source domain — positivity on a convenient dense test space transfers to the
authentic form only when that space is a form core for the authentic form.

## 2.4 Uniform-limit failure and repair (exact examples, not one score)

| phenomenon | exact witness |
|------------|---------------|
| uniform coercivity survives completion | `D = 2·I` (gap `2` for all `N`) |
| positive finite forms lose strict coercivity | `D = diag(1,1/2,…,1/N)` (gap `1/N → 0`) |
| finite compression hides an inverse-response direction | Gemini 1.1 (`⟨De₁,e₁⟩=1` but Schur `−62/19`) |
| local bound constants → 0 | form-core Gram coercivity `→ 0` as `N → ∞` |
| observation quotient loses information | two-state collapse (1.3): `2ⁿ` lifts |
| sufficient lower bound negative while source positive | Gemini 1.2 (surrogate `−3`, Schur `24/25`) |

`RigidityDiagnostics` records six independent fields and
`is_genuine_certificate()` requires the TRUE Schur complement PSD + source
identification + (if `D` singular) range inclusion; the sufficient surrogate is
**not** part of the conjunction. There is deliberately **no** `.score()`.

---

## Success criterion (met)

At least one genuine infinite-dimensional transport theorem (2.3, form-core
positivity transport, with proof) **and** an exact counterexample to a tempting
invalid strengthening (2.3 negative control: `L²`-density is not form-core density),
each with complete stated hypotheses. The finite Schur theorem (2.1) and its
`D ⪰ 0` shorted extension provide the exact, hostile-tested foundation that the
Gemini Crucible (Part II) reuses to refute the restricted-coercivity transfer.
