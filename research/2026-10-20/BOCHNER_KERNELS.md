# Bochner / Schoenberg negative-type kernels

**Operation Rigidity Forge — Part VI (harmonic-analysis bearing)**
Branch: `research/rf-bochner-2026-10-20` (off `e2f92a6`)
Module: `observational_succ/bochner_kernels.py` · Tests: `tests/test_bochner_kernels.py`
Date: 2026-10-20 · Author: `vandettalm@gmail.com` (harmonic-analysis specialist)

All certificates in this dossier are **exact** (sympy `Rational` / symbolic, signs
decided by `.is_nonnegative` or exact rational comparison). A float is never a
certificate; the API refuses Python floats (`_exact` raises). Status vocabulary:
CLASSICAL / PROVED LOCAL / TESTED MODEL / HYPOTHESIS / CONJECTURED / UNVERIFIED /
REFUTED.

---

## 0. Object

For an **even** function `Ψ : ℝ → ℝ` with `Ψ(0) = 0`, define the kernel

```
K_Ψ(s, t) = Ψ(s) + Ψ(t) − Ψ(s − t).
```

Because Ψ is even, `Ψ(s−t) = Ψ(t−s)`, so `K_Ψ` is symmetric and `K_Ψ(t,t) = 2Ψ(t) − Ψ(0) = 2Ψ(t)`.

**Sign bridge to the repo.** `observational_succ/one_object_kernel_certificates.py`
studies `K_g(x,y) = g(x−y) − g(x) − g(−y) + g(0)`. For even `g` with `g(0)=0`
this is `−(g(x)+g(y)−g(x−y)) = −K_Ψ` with `Ψ=g`. So the authentic SUCC Weil
kernel and the Bochner kernel here are **the same algebraic family up to an
overall sign**. The only thing the authentic module has that this one does not
is a *source* (the exact SHA-pinned Suzuki/zeta data). That gap is the entire
point of Part VI (see §5–§6).

---

## 1. The classical Schoenberg relationship  — status **CLASSICAL**

**Theorem (Schoenberg 1938; Lévy–Khintchine).** Let `Ψ : ℝ → ℝ` be even with
`Ψ(0)=0`, and `K_Ψ(s,t) = Ψ(s)+Ψ(t)−Ψ(s−t)`. Then the following are equivalent:

- **(a) PSD kernel.** `K_Ψ` is positive semidefinite on *every* finite node set:
  for all `n`, all `t₁,…,tₙ ∈ ℝ`, all `c ∈ ℝⁿ`, `Σᵢⱼ cᵢcⱼ K_Ψ(tᵢ,tⱼ) ≥ 0`.
- **(b) Conditionally negative definite (CND).** `N(s,t) := Ψ(s−t)` is of negative
  type: `N` symmetric, `N(t,t)=0`, and `Σᵢⱼ cᵢcⱼ Ψ(tᵢ−tⱼ) ≤ 0` for every `c`
  with `Σᵢ cᵢ = 0`.
- **(c) Lévy–Khintchine representation** *(additional hypothesis: Ψ continuous)*:
  ```
  Ψ(x) = c·x² + ∫_{ℝ\{0}} (1 − cos(x u)) dν(u),
  ```
  with `c ≥ 0` and `ν ≥ 0` a symmetric Lévy measure, `∫ min(1, u²) dν(u) < ∞`.

**Exact hypotheses, per arrow.**
- **(a) ⇔ (b)** is *pure finite linear algebra* — it needs only evenness and
  `Ψ(0)=0`. **No continuity, no moment conditions.** The engine is the exact
  polarisation identity in §4.
- **(b) ⇔ (c)** needs Ψ **continuous** (real, even, `Ψ(0)=0`); then the
  representing measure exists and is unique. The two CND "atoms" are `x²`
  (the Gaussian/`c`-term) and `1 − cos(xu)` (one per spectral point `u`) —
  which is exactly why §3's benchmark is `1 − cos` and why §2's `x⁴` cannot work.

**Provenance.** I.J. Schoenberg, *Metric spaces and positive definite functions*,
Trans. AMS **44** (1938) 522–536; Berg–Christensen–Ressel, *Harmonic Analysis on
Semigroups* (1984), Thm 3.2.2 / §II.3. Classical; imported as a *statement about a
generic function*, not about an arithmetic source (`source_authentic = False`).

Encoded as a `ProofContract` (`schoenberg_contract()`): status `CLASSICAL`,
`source_authentic=False`, `finite_to_infinite` records that
"finite PSD Grams ⇒ (b)/(c)" is **not finitary**, open obligation records that
no map to the authentic signed Weil form is supplied.

---

## 2. NEGATIVE benchmark: `Ψ(t) = t⁴`  — status **REFUTED** (as CND)

On nodes `t ∈ {−1, 1}` (`Ψ(±1)=1`, `Ψ(±2)=16`, `Ψ(0)=0`):

```
K(−1,−1) = 1 + 1 − 0  =   2
K( 1, 1) = 1 + 1 − 0  =   2
K(−1, 1) = 1 + 1 − 16 = −14
K( 1,−1) = 1 + 1 − 16 = −14

Gram = [[  2, −14],
        [−14,   2]],      det = 2·2 − (−14)² = 4 − 196 = −192 < 0.
```

Characteristic polynomial `λ² − 4λ − 192`, eigenvalues `16, −12`. The `−12 < 0`
certifies **NOT PSD** (`is_psd_exact → False`). Hence **`t⁴` is not conditionally
negative definite** and `K_{t⁴}` fails as a kernel. Reproduced exactly in
`t4_negative_benchmark()`; `det = −192` and `is_psd = False` are asserted in the
tests. This is the clean refutation that the *shape* `Ψ(s)+Ψ(t)−Ψ(s−t)` carries
no automatic positivity — the function matters.

---

## 3. POSITIVE benchmark: `Ψ(t) = 1 − cos t`  — status **PROVED LOCAL**

**Explicit finite-dimensional feature factorisation.** Using
`cos(s−t) = cos s cos t + sin s sin t`:

```
K_Ψ(s,t) = (1−cos s) + (1−cos t) − (1 − cos(s−t))
         = 1 − cos s − cos t + cos s cos t + sin s sin t
         = (1 − cos s)(1 − cos t) + sin s · sin t
         = ⟨ φ(s), φ(t) ⟩,        φ(t) = ( 1 − cos t ,  sin t ) ∈ ℝ².
```

So `K_Ψ` is the Gram of the **2-dimensional** real feature map
`φ(t) = (1 − cos t, sin t)`. A Gram matrix of inner products of real vectors is
PSD **on every node set, by construction** — this is a *proof*, not a numerical
check. The identity `K_Ψ(s,t) = ⟨φ(s),φ(t)⟩` is verified **symbolically for free
`s,t`** in `verify_one_minus_cos_identity()` (`sympy.simplify(LHS − RHS) == 0`).

**Exact rational Gram certificates (finite, float-free).** To exhibit concrete
exact PSD Grams I index nodes by **rational points on the unit circle**
`(a,b) = (cos θ, sin θ)`, `a²+b²=1` (Pythagorean points `(1,0)`, `(3/5,4/5)`,
`(5/13,12/13)`, `(8/17,15/17)`, `(20/29,21/29)`, `(−3/5,4/5)`, `(−7/25,24/25)`).
Then `Ψ(θᵢ)=1−aᵢ` and `cos(θᵢ−θⱼ)=aᵢaⱼ+bᵢbⱼ`, so every Gram entry
`(1−aᵢ)(1−aⱼ)+bᵢbⱼ` is **exactly rational** — no transcendental evaluation. For
every nested node set (2…7 nodes) the exact rational Gram is certified PSD
(`is_psd_exact`) **and** verified equal to `Φ Φᵀ` with `Φ` the matrix of feature
rows (`one_minus_cos_positive_benchmark()`). Secondary CND examples: `Ψ=x²`
(`c=1`, `ν=0`) is CND; see §4/§3-LK.

This `1 − cos` kernel is the **negative control** referenced in §6.

---

## 4. The exact intermediate lemma: Schoenberg polarisation  — status **PROVED LOCAL**

`schoenberg_polarization_check` verifies, as an **exact algebraic identity** (no
analysis, no limits), the engine of (a)⇔(b):

```
Σᵢⱼ cᵢcⱼ K_Ψ(tᵢ,tⱼ) = 2 (Σᵢ cᵢ)(Σⱼ cⱼ Ψ(tⱼ)) − Σᵢⱼ cᵢcⱼ Ψ(tᵢ−tⱼ).
```

On the hyperplane `Σᵢ cᵢ = 0` the first term vanishes, so
`Σ cᵢcⱼ K_Ψ = − Σ cᵢcⱼ Ψ(tᵢ−tⱼ)`; thus `K_Ψ` PSD on `{Σc=0}` **iff** `Ψ(·−·)`
is CND. This is the only genuinely transferable analytic content of the module,
and it is a **firewall lemma**: it makes precise that
`finite PSD ⇏ global PSD ⇏ positive spectrum ⇏ source identification`.
Tested on rational nodes for `Ψ=t²` (general `c`) and `Ψ=t⁴` (`Σc=0` reduction).

---

## 5. The four SEPARATE certified predicates (i)–(iv)

These are **distinct** predicates with **distinct certificates**. Conflating them
is the error the firewall forbids.

| # | Predicate | Certificate | Decidable by finite exact arithmetic? | `1−cos` | `t⁴` |
|---|-----------|-------------|----------------------------------------|---------|------|
| **(i)** | A given finite Gram `M` is PSD | `is_psd_exact(M)`: signs of charpoly coeffs (eigenvalues ≥ 0) | **Yes** (one node set) | ✓ | ✗ (`det −192`) |
| **(ii)** | `K_Ψ` PSD on *every* finite node set (global PSD kernel — the `1−cos` feature map is rank 2, so Grams on ≥3 nodes are singular: PSD, not PD) | feature map `φ` with `K_Ψ=⟨φ,φ⟩` (symbolic) **or** CND; single failing Gram refutes | **No** (not finitary); refutable by one witness | ✓ (`φ=(1−cos,sin)`) | ✗ (witness `{−1,1}`) |
| **(iii)** | Positive spectral / Lévy–Khintchine measure | exhibit `(c,ν)`, `c≥0`, `ν≥0`, verify `Ψ=c x²+∫(1−cos xu)dν` | Representation exhibited exactly here; nonexistence proved via (i)-witness | ✓ (`c=0, ν=δ₁`) | ✗ (no positive measure; `t⁴` not CND) |
| **(iv)** | Source-IDENTIFIED signed Weil kernel | a *derived* map to the completed signed Weil distribution with correct source / Γ / pole / half-density / conductor / phase | **Not available** | **None** | **None** |

`is_psd_exact` uses the characteristic-polynomial criterion (a real symmetric
matrix is PSD iff `(−1)ᵏ aₙ₋ₖ ≥ 0` for the monic charpoly coefficients), which is
a genuine **PSD** test. Leading principal minors / Sylvester
(`is_positive_definite_exact`) only test positive **definiteness** — e.g.
`[[0,0],[0,−1]]` has leading minors `0,0` (Sylvester cannot reject) yet is
indefinite; `is_psd_exact` correctly rejects it (tested). That gotcha is why PSD
is tested by the charpoly, not by leading minors alone.

---

## 6. (iv) — the honest boundary: **NO** connection to the signed Weil form

**Verdict: `iv_source_identified_signed_weil = None` for every kernel here. This
is a BOUNDARY, recorded as a firewall negative control, not a gap to be papered
over.**

A generic even `Ψ` with `Ψ(0)=0` is **not an arithmetic source**:

- there is **no Γ-factor / archimedean place**, no completed-ξ structure;
- there is **no prime / von-Mangoldt / pole term** (contrast
  `tate_signed_weil_bridge.compare_signed_weil_tent`, which guards exactly these);
- there is **no half-density, no conductor, no phase / functional-equation data**;
- there is **no source map** of the kind `one_object_kernel_certificates`
  authenticates by SHA-pinned blob identity.

Therefore the hypotheses required by AGENTS.md §6 ("positive physical/semantic
covariances are **not** automatically source-derived positive Weil forms — never
silently assert the missing identification") and §7 (original prime-power/source
data, completed Γ/pole, valid test-function domains, correct
half-density/conductor/phase, no nontrivial zeros as inputs) are **not met and
cannot be met** by an abstract `Ψ`. I **do not** construct a map; I record its
absence.

**Why this is useful (the negative control).** `Ψ = 1 − cos` gives a kernel of
the *exact* shape `Ψ(s)+Ψ(t)−Ψ(s−t)` that is:
(i) finite-PSD, (ii) globally PSD (2-D feature map), (iii) positive-spectrum
(`ν=δ₁`) — and yet (iv) is empty and **RH is untouched**. This is a concrete,
reusable witness that

> a fully positive kernel of the signed-Weil *algebraic shape* carries, by
> itself, **zero** arithmetic / RH content.

So any future SUCC argument that infers Weil positivity (or RH) from PSD-ness of
a kernel in this family is refuted-in-shape unless it *separately* supplies the
(iv) source identification. `1 − cos` is the counterexample that keeps (i)→(iv)
inference honest. The sign bridge of §0 (`K_Ψ = −K_g`) places this control in the
same family as the authentic module, which makes it directly reusable there.

---

## 7. Claims ledger

| Claim | Status | Receipt |
|-------|--------|---------|
| Schoenberg (a)⇔(b)⇔(c) with stated hypotheses | CLASSICAL | Schoenberg 1938; BCR 1984; `schoenberg_contract()` |
| `t⁴` Gram on `{−1,1}` = `[[2,−14],[−14,2]]`, `det −192`, not PSD; `t⁴` not CND | REFUTED (as CND) | `t4_negative_benchmark()`, exact |
| `1−cos` feature map `φ=(1−cos t, sin t)`, `K_Ψ=⟨φ,φ⟩` for all `s,t` | PROVED LOCAL | `verify_one_minus_cos_identity()` symbolic |
| `1−cos` Gram PSD on 2…7 nested rational-circle nodes, `=Φ Φᵀ` | PROVED LOCAL | `one_minus_cos_positive_benchmark()`, exact rational |
| Lévy–Khintchine: `1−cos → (c=0, ν=δ₁)`; `t² → (c=1, ν=0)`; `t⁴ →` none | CLASSICAL / REFUTED | `levy_khintchine_benchmarks()`, exact |
| Polarisation identity (engine of (a)⇔(b)) | PROVED LOCAL | `schoenberg_polarization_check()`, exact |
| Four predicates (i)–(iv) are distinct; (iv) empty for all kernels here | PROVED LOCAL (firewall) | `four_way_spectral_report()` |
| Any map `K_Ψ → authentic signed Weil form` | **NOT SUPPLIED / NOT CLAIMED** | §6 boundary |
| RH | **OPEN** | unchanged |

**Next falsification opportunity.** If a later bearing claims a *specific* even
`Ψ` that is genuinely source-derived (real Γ/pole/prime data, correct
half-density, no zero inputs), re-run (i)–(iii) on *that* `Ψ` and then — and only
then — attempt (iv) by exhibiting the derived map; the `1−cos` control must be
re-checked to confirm the new argument does not also "prove" the trivially-safe
control. Until such a map is derived, (iv) stays `None` and RH stays OPEN.

---

## 8. Reproduction

```sh
cd /home/leah/SUCC-rf-boch
PYTHONPATH=. python -m unittest tests.test_bochner_kernels -v   # 29 tests, OK
python scripts/verify_provenance.py                            # SOURCE_PROVENANCE_VERIFIED, 72 items
```
