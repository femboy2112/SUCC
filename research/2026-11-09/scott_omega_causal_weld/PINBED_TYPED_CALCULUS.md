# Pinbed typed calculus: exact dimensional relations, CRT, and higher cells

**Front C** of the Scott × Omega × SUCC causal weld. Companion to
`observational_succ/pinbed_typed_calculus.py` and
`tests/test_pinbed_typed_calculus.py`.

Status legend: **PROVED (structural)** = exact finite proof, no analysis
needed; **PROVED (finite)** = exhaustive finite check; **CLASSICAL** =
known theorem, not a SUCC discovery; **OPEN** = unsolved target.

---

## 0. What this is and is not

The proposed "dimensional relations"

    Omega_5 ~ 3 Omega_3 ~ Omega_3 + Omega_4 ~ 2 Omega_4 - Omega_3

are **compiler-mediated proposals**, not literal λ-term identities. CW-14
already refuted the naive reading: a single one-clock `m -> m+d` orbit is
one orbit, which cannot reach a generic `(i,j)`, and an equal-period
diagonal torus misses 240 of 256 sites.

This document builds the *typed finite substrate* in which a faithful
higher-dimensional reading would have to live, and proves exactly which
parts are genuine and which parts collapse:

| Construction | Status | Meaning |
|---|---|---|
| `Pin_d(H) = H^(N^d)` with curry/uncurry | PROVED (structural) | genuine CCC exponential-object law on finite products |
| `d` commuting, separately-addressable successors | PROVED (finite) | genuinely `d` independent directions |
| single clock spans `N^d` | REFUTED (finite) | one orbit, `≤ N` sites on the diagonal |
| fiber-product gluing `(x,y)×(y,z)→(x,y,z)` | PROVED (structural) | genuine universal property |
| CRT coprime = full group isomorphism | PROVED (finite) / CLASSICAL | all Fourier characters preserved |
| CRT non-coprime `(16,16)` = alias | PROVED (finite) | 240/256 characters destroyed |
| affine square `V_p S = S^p V_p` | PROVED (finite) | genuine commuting square |
| interchange on affine 2-cells | PROVED (finite) | coherence where it applies (see CW-19 caveat) |
| any of the above yields π arithmetic information | OPEN | **not established** |

---

## 1. `Pin_d(H)` and the currying law

**Definition.** For a finite axis set `N^d = {0,…,N−1}^d` and a carrier type
`H`, define

    Pin_d(H) = H^(N^d),

the set of `d`-ary arrays with entries in `H`. This is the finite slice of
the exponential object `H^X` evaluated at `X = N^d`.

**Theorem 1 (curry/uncurry round-trip).** *PROVED (structural).*
For any split `0 < k < d`, there are mutually inverse maps

    curry    : Pin_d(H)  ->  Pin_k( Pin_{d−k}(H) ),
    uncurry  : Pin_k( Pin_{d−k}(H) ) -> Pin_d(H),

and `uncurry(curry(f)) = f` for every `f` (exact elementwise identity).

*Proof.* `curry(f)` is the `k`-array whose `(i_1,…,i_k)`-entry is the
`(d−k)`-array `(j_1,…,j_{d−k}) ↦ f(i_1,…,i_k,j_1,…,j_{d−k})`. `uncurry`
reads a nested array back into a flat `d`-array by concatenation of the
outer and inner indices. The two are inverse because index concatenation is
injective and every `d`-index decomposes uniquely into a `k`-prefix and a
`(d−k)`-suffix. This is the standard finite witness of the CCC law

    Hom(X_1 × … × X_d, H) ≅ Hom(X_1, Hom(X_2 × … × X_d, H)),

with the index and evaluation maps surviving exactly (CW-07). ∎

*Test:* `test_roundtrip_identity`, `test_curry_shapes`, `test_rejects_wrong_arity`.

**Boundary.** This proves array-level currying on finite products. It does
*not* identify `H^(N^d)` with any infinite-dimensional analytic object, and
it does not turn an `Ω_{d+2}` term into `d` directions (CW-02/CW-14).

---

## 2. `d` commuting successor operators vs. a single clock

**Definition.** For axis lengths `(N_1,…,N_d)`, define `S_i : N^d → N^d` by

    S_i(x_1,…,x_d) = (x_1,…, x_i+1 mod N_i, …, x_d).

**Theorem 2 (independent commuting successors).** *PROVED (finite).*
For all `i,j`, `S_i ∘ S_j = S_j ∘ S_i`, and `S_i` is *separately
addressable*: it changes only coordinate `i`.

*Proof.* `S_i` and `S_j` act on disjoint coordinates, so their compositions
agree regardless of order. Addressability is immediate from the definition.
∎

**Theorem 3 (one clock does not span `N^d`).** *REFUTED (finite), = CW-14.*
Let `T : N^d → N^d` be any single map and let `O` be the orbit of
`(0,…,0)` under `T`. Then `|O| ≤ N^d`, and for the diagonal clock
`T(x)=(x_1+1,…,x_d+1)` on equal axes `N_1=…=N_d=N`, `|O| = N < N^d`
whenever `N ≥ 2`.

*Proof.* An orbit is a subset of `N^d`, so `|O| ≤ N^d`. The diagonal clock
returns to `(0,…,0)` after `N` steps (each coordinate increments with period
`N`), and never leaves the diagonal `{x_1=…=x_d}`, which has `N` elements.
For `N=16, d=2` this is 16 of 256 — 240 sites unreachable. A single
`m → m+d` growth map is precisely such a one-orbit clock. ∎

*Tests:* `test_independent_commute`, `test_separately_addressable`,
`test_successors_together_span`, `test_single_clock_does_not_span_n2`,
`test_diagonal_scan_misses_240_of_256`.

**Significance.** The `d` commuting successors are what the compiler must
*produce* to earn "`d` independent directions". A one-clock map is provably
insufficient. This is the executable form of CW-14.

---

## 3. Fiber-product gluing and its universal property

**Definition.** For two tables `A = N×N` (coordinates `(x,y)`) and
`B = N×N` (coordinates `(y,z)`) glued over the shared middle coordinate `y`:

    A ×_C B = { ((x,y),(y,z)) : y matches }.

The gluing map sends `((x,y),(y,z)) ↦ (x,y,z)`, a triple.

**Theorem 4 (fiber product ≅ three coordinates).** *PROVED (structural).*
`A ×_C B ≅ N × N × N`, where the legs are the projections
`(x,y,z) ↦ (x,y)` and `(x,y,z) ↦ (y,z)`.

*Proof.* The gluing map is a bijection onto `N×N×N`: every triple
`(x,y,z)` comes from the unique pair `((x,y),(y,z))`, and the two pairs map
to the same triple iff they agree in all three slots. This is the
*fiber-product dimensional gluing* of CW-07, not a union of two planes and
not a literal β-equivalence of `Ω_5` and `Ω_4×Ω_4`. ∎

**Theorem 5 (universal property).** *PROVED (finite).*
For any source object `T` of agreed pairs `((x,y),(y,z))`, there is a unique
map `T → A ×_C B` making the two projection triangles commute.

*Proof.* Existence: send each agreed pair to its glued triple; the legs
recover the pair. Uniqueness: gluing is injective on agreed pairs, so any
map commuting with both legs is forced to equal the gluing map. Verified
exhaustively over `T = N×N×N` (all `N^3` agreed triples). ∎

*Tests:* `test_universal_property`, `test_glue_mismatch_rejected`,
`test_three_coordinate_bijection`.

**Boundary.** The gluing is a genuine fiber product in the category of
finite sets and functions. It says nothing about a "sum of dimensions" as
an analytic statement about `Ω_5`.

---

## 4. CRT: coprime = full, non-coprime = alias

**Definition.** For moduli `(m_1,…,m_r)`, the CRT clock reconstructs a
unique residue `x mod M` (`M = ∏ m_i`) from `(x mod m_1, …, x mod m_r)`.

**Theorem 6 (CRT is a full group isomorphism iff coprime).** *CLASSICAL /
PROVED (finite).* The map

    Z/MZ → Z/m_1Z × … × Z/m_rZ

is a group isomorphism iff the `m_i` are pairwise coprime.

*Proof.* Classical CRT. Verified finitely for `(3,4)`: the `3·4 = 12`
residue tuples are hit exactly once, i.e. all `M = 12` group elements are
covered, and modular inverses (`pow(Mi, −1, m)`) exist iff `gcd` is 1. ∎

**Theorem 7 ((16,16) is an alias, loses Fourier characters).** *PROVED
(finite).* The synchronous diagonal scan on `(Z/16)^2` covers 16 of 256
states, missing 240. The 256 Fourier characters

    χ_{(a,b)}(x,y) = exp(2πi (a x + b y)/16)

collapse along the diagonal to the `16` characters indexed by the sum
`(a+b) mod 16`, so `256 − 16 = 240` distinct characters are *lost* (aliased).

*Proof.* Along the diagonal `x = y = t`, `χ_{(a,b)}(t,t) = χ_{(a+b,0)}(t,t)`
for all `t`, so the orbit cannot distinguish `(a,b)` from `(a+b, 0)`. The
equivalence classes `{ (a,b) : a+b = s }` (one per `s mod 16`) give exactly
16 resolvable characters; the remaining 240 are aliased. This is the CW-07/
CW-08 negative: a single unlicensed clock loses Fourier information, and
low-order marginal agreement does not imply full Haar. ∎

*Tests:* `test_crt_combine_inverse`, `test_crt_full_recovery_3_4`,
`test_crt_not_full_16_16`, `test_fourier_characters_lost`.

**Boundary.** CRT full recovery is a *group-theoretic* statement about
cyclic clocks. It is **not** a claim that the selected BBP orbit is Haar
equidistributed, and it produces no π arithmetic information.

---

## 5. Source-attested affine squares and higher cells

**Definition.** On `Z/nZ`, let `S(x)=x+1` and `V_p(x)=p·x`. The affine
relation is

    V_p ∘ S = S^p ∘ V_p,

checked at every `x`:

    V_p(S(x)) = p(x+1) = px + p = S^p(px) = S^p(V_p(x))  (mod n).

**Theorem 8 (affine square).** *PROVED (finite).* For every prime `p` and
modulus `n ≥ 2`, `V_p S = S^p V_p` holds at every `x ∈ Z/nZ`.

*Proof.* Direct modular arithmetic above; verified exhaustively for
`(p,n) ∈ {(2,7),(3,11),(5,13),(3,16),(2,16)}`. ∎

**Theorem 9 (prime-pair cube and interchange).** *PROVED (finite).*
For distinct primes `p,q`, the dilations `V_p,V_q` commute, so
`V_q V_p S = V_p V_q S`, and the interchange of the two affine squares
agrees in both pasting orders.

*Proof.* `V_p V_q = V_{pq} = V_q V_p` because multiplication commutes. Both
pasting orders collapse to the same `V_{pq} S` square, so interchange holds
exactly. ∎

*Tests:* `test_relation`, `test_prime_pair_cube_commutes`, `test_interchange`.

**CW-19 boundary (important).** These are *diagrams* in the category of
affine maps. The interchange "2-cell" here is coherent because the two
squares are `V_p S = S^p V_p` and `V_q S = S^q V_q`, and the pastings
collapse to a single affine map. This does **not** manufacture genuinely
*nontrivial* higher morphisms: an iterated arrow category contains higher
diagrams, not automatically new 2-cells. A real 2/3-cell calculus requires a
declared rewrite/polygraph with its own coherence (pentagon, interchange as
a separate axiom on generators) — which remains **UNVERIFIED** (CW-19).

---

## 6. Hostile controls (mandatory, executed)

1. **Single clock ≠ N^2.** `single_clock_spans` on the 16×16 diagonal
   returns `(False, 16)`: one orbit, 16 sites, not 256. *Test:
   `test_single_clock_does_not_span_n2`.*
2. **Diagonal scan misses 240/256.** `diagonal_scan_coverage(16,2) =
   (16, 256, 240)`. *Test: `test_diagonal_scan_misses_240_of_256`.*
3. **(16,16) loses 240 Fourier characters.** `fourier_characters_lost(16,2)
   = 240`. *Test: `test_fourier_characters_lost`.*

---

## 7. Honest limitations

- **Proved (structural/finite):** currying round-trip; `d` commuting
  successors; fiber-product universal property; CRT coprime↔full and
  non-coprime↔alias; affine square and interchange on the *specific*
  affine generators.
- **Classical (not a SUCC discovery):** CRT group isomorphism.
- **OPEN (not established):** any of this producing π arithmetic
  information, signed cancellation, or normality. The "dimensional
  relations" `Omega_5 ~ …` remain compiler-mediated proposals; no literal
  λ-identity or analytic dimensionality claim is asserted here.

---

## 8. Reproduction

```sh
python -m unittest tests.test_pinbed_typed_calculus -v
```

Expected: 18 tests, all `ok`, exit code 0.
