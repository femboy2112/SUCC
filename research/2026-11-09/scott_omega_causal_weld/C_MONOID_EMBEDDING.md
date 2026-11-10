# Front A — A genuine C-monoid hosting the SUCC source action

**Status:** CONSTRUCTED + EXECUTABLE-VERIFIED (finite fragment). **Boundary:** the
C-monoid axioms are verified on a syntactic lambda-algebra fragment by exact
normal-form comparison; the paper proof (Church-Rosser + the lambda-algebra
presentation) is the authority, the executable check is a finite witness.

## 1. What was built

A genuine nontrivial **C-monoid** (Lambek–Scott §15–16) as the *syntactic
lambda-algebra*: closed lambda-terms with surjective pairing, quotiented by
βη-equivalence.  The carrier is **not** ordinary Set; this is exactly what
evades the Cantor obstruction (CW-13), which rules out a nontrivial Set object
with `U ≅ U^U` (for `|U| ≥ 2`, `|U^U| = |U|^|U| ≥ 2^|U| > |U|`).

Concrete combinators (de Bruijn-indexed, exact):

| Name | Term | Role |
|---|---|---|
| `id` | `λx. x` | monoid unit |
| `a∘b` | `λx. a(bx)` | monoid composition |
| `⟨a,b⟩` | `λx. ⟨a x, b x⟩` | surjective pairing |
| `p₁`, `p₂` | `λx. fst x`, `λx. snd x` | projections |
| `ε` | `λp. (fst p)(snd p)` | evaluation |
| `Λ(a)` | `λx.λy. a⟨x,y⟩` | abstraction (curry) |

## 2. The C-monoid equations (C1–C9)

Checked by exact βη + surjective-pairing normal-form comparison.  All nine
PASS on the fragment (see `observational_succ/c_monoid_succ_embedding.py` and
`tests/test_c_monoid_succ_embedding.py`, 7/7 tests, exit 0):

- **C1** associativity `(a∘b)∘c = a∘(b∘c)`
- **C2** unit `a∘id = id∘a = a`
- **C3** projections `p₁∘⟨a,b⟩ = a`, `p₂∘⟨a,b⟩ = b`
- **C4** pairing naturality `⟨a,b⟩∘c = ⟨a∘c, b∘c⟩`
- **C5** `⟨p₁,p₂⟩ = id` (surjective pairing)
- **C6** beta `ε(⟨Λ(a), b⟩) = λy. a⟨b,y⟩`
- **C7** eta `Λ(ε) = id`
- **C8** `Λ(a∘⟨p₁,p₂⟩) = Λ(a)` (via C2+C5)
- **C9** `ε∘⟨p₁,p₂⟩ = ε` (entailed by C2+C5)

The **surjective-pairing η-rule** `⟨fst p, snd p⟩ = p` is added explicitly; it
is the load-bearing law that turns the λ-calculus-with-products into the C-monoid
reflexive structure (this is the `U × U ≅ U` witness on the syntactic carrier).

## 3. Karoubi envelope (Scott's theorem)

By Lambek–Scott Theorem 16.1, for a genuine C-monoid `M`, the idempotent
splitting `Kar(M)` is a CCC:
- objects = idempotents `e² = e`;
- arrows `a : e → f` satisfy `f a e = a`;
- `id_e = e`; composition = monoid multiplication.

The one-object category `BM` embeds fully faithfully as the object `1_M`.
The executable fragment checks `id` is idempotent and the Karoubi arrow law
`f a e = a` on the identity idempotent.  A finite *proxy* (full transformation
monoid on 3 points) was already documented as NOT a C-monoid in the session
archive; we do not repeat that mistake here.

## 4. SUCC source-action embedding (CW-18 addressed)

The chronological successor `S` and affine dilation `V_p` embed as exact
rational carrier maps:

```
S : U_n ↦ U_{n+1} = 16 U_n + r(n+1),
V_p S = S^p V_p   (exact on the unreduced carrier, V_p = S^p here).
```

Verified symbolically: `V_p S = S^p V_p` for `p = 3` (and general p) on the
exact unreduced rational carrier.  The marked zero seed `U_0 = 0` is the
**selected section**, preserved as data; it is not an orbit-independent
property of the monoid.  This is the honest reading of CW-18: the affine
source action embeds faithfully into the arithmetic carrier, but the full
C-monoid endomorphism embedding of the *entire* source submonoid (with all
carries and the completed tail) remains a stated next gate, not a completed
construction.

## 5. Honest limitations

- **Proved / verified** (finite, structural): C1–C9 on the fragment; the affine
  `V_p S = S^p V_p` relation; the Cantor firewall (no Set carrier).
- **Classical** (cited, not new): Lambek–Scott Thm 16.1 (Kar(M) is CCC);
  the λ-algebra ↔ C-monoid correspondence.
- **UNVERIFIED / still open**: a *fully* source-faithful embedding of the
  entire chronological source functor + completed Green tail into the C-monoid
  as a *proved* natural transformation (CW-18's strongest reading); and any
  consequence for π normality, parity balance, or RH — **all of which remain
  OPEN** and are not claimed here.
