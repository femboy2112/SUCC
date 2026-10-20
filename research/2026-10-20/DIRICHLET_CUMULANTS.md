# Formal Dirichlet cumulants and the multiplicativity characterization

**Operation Rigidity Forge — Part V, Deliverable D**
Module: `observational_succ/dirichlet_cumulants.py` · Tests: `tests/test_dirichlet_cumulants.py`
Status of everything below unless noted: **CLASSICAL** (standard formal
Dirichlet-algebra theory). The SUCC contribution is the *exact, tested*
implementation and the explicit formal/analytic firewall.
RH: untouched and **OPEN**. No zero ordinate, half-density, conductor, or phase
appears in this lane.

---

## 0. Setting and definitions

Arithmetic functions `a : Z>=1 -> R` (R = Q or a symbolic ring) with `a(1) = 1`.
The convolution is the **Dirichlet / multiplicative** one

```
(f *x g)(n) = sum_{d | n} f(d) g(n/d),     identity delta(1)=1, delta(n>1)=0.
```

This is the same operation as `arithmetic_interactions.dirichlet_convolution`;
the module works with 1-indexed exact coefficient arrays so convolution *powers*
are cheap. Put `h = a - delta` (so `h(1) = 0`). The **formal Dirichlet
logarithm** / cumulant generator is

```
b = log_* a = sum_{k >= 1} (-1)^(k+1)/k * h^{*k}.
```

**Finiteness (no convergence question).** In `h^{*k}(n)` every factor is `>= 2`
(because `h(1) = 0`), so a nonzero term needs `2^k <= n`, i.e. `k <= floor(log2 n)`.
Hence `b(n)` is a *finite* exact combination of the values `a(d)`, `d | n`. The
object lives in the completed Dirichlet-convolution ring; it is pure algebra.
We call `b(n)` the *n-th formal Dirichlet cumulant*; the mixed ones `b(pq)`,
`b(pqr)`, … are the connected mixed-prime correlations (the moment/cumulant
wording is an **analogy**, not a theorem).

Because the Dirichlet ring is **commutative**, `log_*` and `exp_*` are mutually
inverse group isomorphisms

```
log_* : (G, *x)  <->  (g, +) : exp_* ,     G = {a : a(1)=1},  g = {b : b(1)=0},
```

and in particular `exp_*(b + b') = exp_*(b) *x exp_*(b')` (the identity used
throughout). Implemented as `dirichlet_log` / `dirichlet_exp`; cross-checked
against the independent `dirichlet_lambert.star_log_unit` / `star_exp`.

---

## 1. First mixed-prime cumulant identity  (PROVED, FORMAL)

> For distinct primes `p, q`:  **`b(pq) = a(pq) - a(p) a(q)`.**

*Proof.* Divisors of `pq` that are `>= 2` are `p, q, pq`. Ordered factorizations
into factors `>= 2`: `k=1`: `(pq)`, contributing `h(pq) = a(pq)`; `k=2`: `(p,q)`
and `(q,p)`, contributing `2 h(p) h(q) = 2 a(p) a(q)`; `k >= 3`: impossible
(`Omega(pq) = 2`). Hence
`b(pq) = (+1/1) a(pq) + (-1/2)(2 a(p) a(q)) = a(pq) - a(p) a(q)`.  ∎

Implemented and self-checking in `mixed_prime_cumulant(a, p, q)` (it recomputes
`b(pq)` from the full `log_*` and raises unless it equals the closed form
`first_mixed_cumulant_closed_form`). Tested symbolically (free `a2, a3, a6`) and
on all multiplicative controls (`b(pq) = 0`), plus a defect case `b(6) = 4`.

Note `b(p) = a(p)` for every source (single prime, no higher terms).

---

## 2. Characterization theorem  (PROVED, FORMAL; CLASSICAL)

> **Theorem.** Let `a(1) = 1` and `b = log_* a`. Then
> **`a` is multiplicative  ⟺  `b(n) = 0` for every `n` with `omega(n) >= 2`**
> (equivalently, `b` is supported on prime powers `{p^k : k >= 1}`).

Here *multiplicative* means `a(mn) = a(m) a(n)` whenever `gcd(m, n) = 1`.

### Prime-power support decomposition

For a prime `p` let `a_p` be the restriction of `a` to powers of `p`
(`a_p(p^k) = a(p^k)`, `a_p(1) = 1`, else `0`), and `b_p = log_*(a_p)`. Since
`a_p - delta` is supported on `{p^k}` and the Dirichlet product of
`p`-power-supported functions is again `p`-power-supported, `b_p` is supported on
`{p^k}`.

### Proof

**(⟹)** If `a` is multiplicative then `a = *x_p a_p` (the classical Euler
product in the convolution ring; formally finite at each `n`). Applying the
homomorphism `log_*`,
`b = log_*(*x_p a_p) = sum_p log_*(a_p) = sum_p b_p`,
a sum of prime-power-supported functions, hence `b(n) = 0` whenever `n` has `>= 2`
distinct prime factors.

**(⟸, converse — the load-bearing direction)** Suppose `b` is supported on prime
powers. Write `b = sum_p b_p` with `b_p` its restriction to `{p^k}` (formally
finite at each `n`). Then
`a = exp_*(b) = exp_*(sum_p b_p) = *x_p exp_*(b_p)`.
Each `a_p := exp_*(b_p)` is supported on powers of `p` with `a_p(1) = 1`, so for
`n = prod_p p^{e_p}`, `a(n) = prod_p a_p(p^{e_p})`, which is exactly
multiplicativity: for `gcd(m, n) = 1` the prime sets are disjoint and
`a(mn) = a(m) a(n)`.  ∎

### Completely multiplicative refinement

If `a` is completely multiplicative (`a(p^k) = a(p)^k`) then the local factor is
`sum_k a(p)^k x^k = 1/(1 - a(p) x)`, whose log is `sum_k (a(p)^k / k) x^k`, so

```
b(p^k) = a(p)^k / k.
```

Thus `a` completely multiplicative ⟺ `a` multiplicative **and**
`b(p^k) = b(p)^k / k` for all `p, k`.

### Implementation / tests

- `is_multiplicative_via_cumulants(a, bound)` — `all(b(n) == 0 for mixed n <= bound)`.
- `first_nonzero_mixed_cumulant(a, bound)` — least offending `n`, or `None`.
- `multiplicative_extension` / `formal_euler_product_matches` — see §4.
- Controls `constant_one, mobius, liouville, tau(=divisor_count), phi`: all have
  empty mixed support up to 64. `constant_one` and `liouville` satisfy the
  `b(p^k) = a(p)^k / k` refinement exactly. Converse tested by building an
  arbitrary prime-power-supported `b`, exponentiating, and confirming the result
  is multiplicative. Cross-checked against `star_log_unit`; round trip
  `exp_*(log_* a) = a` confirmed exactly.

---

## 3. Exact controls

| Source | kind | mixed support | notes |
|---|---|---|---|
| `tau = divisor_count` | multiplicative, not completely | empty | `tau(4)=3 ≠ tau(2)^2=4` |
| `phi` (totient) | multiplicative, not completely | empty | |
| `constant_one` (≡1) | completely multiplicative | empty | `b(p^k)=1/k`; DGF `= zeta(s)` |
| `liouville` | completely multiplicative | empty | `b(p^k)=(-1)^k/k`; DGF `= zeta(2s)/zeta(s)` |
| `a(6)=5`, else 1 | counterfeit | first defect **n=6** | `b(6)=5-1=4` |
| `a(12)=100`, else 1 | correct semiprimes, higher defect | first defect **n=12** | all `b(pq)=0`, `b(12)=99` |
| `a(30)=2`, else 1 | correct semiprimes, higher defect | first defect **n=30** | all `b(pq)=0`, `b(30)=1` (3-prime cumulant) |
| `factorial_completely_multiplicative` (`a(p)=p!`) | completely multiplicative | empty | **formal fine**, analytic UNAVAILABLE |

The two "correct semiprime, higher defect" sources show that vanishing of **all**
distinct-prime semiprime cumulants `b(pq)` does **not** force multiplicativity:
the obstruction can first appear at a prime-squared-times-prime (`12 = 2^2·3`) or
a three-distinct-prime (`30 = 2·3·5`) argument. (Starting from the multiplicative
base `a ≡ 1` and perturbing only `a(N)`: since `b(n)` depends only on `a(d)` for
`d | n`, the value `a(N)` affects `b(n)` solely when `N | n`. The coefficient of
`a(N)` in `b(N)` is `+1` (the `k=1` term; no `k >= 2` factorization of `N`
contains `N` itself), so `b(N)` equals the perturbation and every smaller mixed
cumulant stays `0`.)

### Formal-fine-but-analytically-divergent source (the firewall case)

`a` completely multiplicative with `a(p) = p!`. The **formal** object is perfect:
`b(p^k) = (p!)^k / k` exactly, mixed support empty, `exp_*(b) = a` exactly
(all tested at bound 32). But the **Dirichlet series** `sum_n a(n) n^{-s}`
diverges for **every** `s`:

> For any `sigma = Re(s)` the general term along primes is
> `|a(p) p^{-s}| = p! · p^{-sigma} -> infinity` (since `p!/p^sigma -> infinity`),
> so the necessary condition `term -> 0` fails. **PROVED LOCAL.**

Exhibited exactly (no floats) by `completely_multiplicative_term_test_failure`,
which for each `sigma` returns a prime `p` with `p! > p^sigma`
(tested `sigma = 1, 5, 10, 50`). The formal Euler product
`prod_p 1/(1 - p! · p^{-s})` exists as a formal power series in each `p^{-s}`;
the analytic product does not.

---

## 4. Formal Euler product vs analytic convergence (kept SEPARATE)

> **Formal statement (PROVED).** `a` is multiplicative ⟺ its formal Dirichlet
> series factors as `prod_p ( sum_{k>=0} a(p^k) p^{-ks} )` as formal power series
> in each `p^{-s}` ⟺ `a(n) = prod_{p^e || n} a(p^e)` for all `n`.

*Proof.* The `n^{-s}` coefficient of the product (for `n = prod p^{e_p}`) is
`prod_p a(p^{e_p})`; the series coefficient is `a(n)`. Equality for all `n` is
precisely `a(n) = prod a(p^{e_p})`, which is multiplicativity.  ∎

Implemented by `multiplicative_extension(a, bound)` (the array
`hat-a(n) = prod a(p^e)`) and `formal_euler_product_matches(a, bound)`
(`hat-a == a`). `local_euler_factor_coeffs(a, p, bound)` returns the local factor
coefficients `[(k, a(p^k))]`.

> **Analytic statement (SEPARATE, labeled).** Carried by `AnalyticConvergenceClaim`
> / `analytic_convergence_claim(name)`, each with an explicit half-plane and a
> proof_contracts status. **One converges:** `constant_one` → `zeta(s)`, absolute
> convergence `Re(s) > 1` (CLASSICAL). **One does not:**
> `factorial_completely_multiplicative` → diverges for all `s` (PROVED LOCAL,
> §3). The formal and analytic claims are never identified.

The firewall: a correct formal or analytic Euler product does **not** imply Weil
positivity. RH stays OPEN.

---

## 5. Finite detection of the first mixed cumulant (honest result)

**Part A — fixed window is exact (PROVED).** For any fixed bound `B`, the least
mixed-prime cumulant `<= B` is found by inspecting the finitely many `n <= B` with
`omega(n) >= 2` (ascending: `6, 10, 12, 14, 15, …`); each `b(n)` uses only the
divisor data `a(d)`, `d | n <= B`. Equivalently, "`a` is multiplicative up to `B`"
(all coprime `m,n` with `mn <= B`) ⟺ `b(n) = 0` for all mixed `n <= B`. This is
`is_multiplicative_via_cumulants` / `first_nonzero_mixed_cumulant`. The smallest
argument that must ever be inspected is `6`.

**Part B — no single window works for all sources (PROVED, by counterexample).**

> There is **no** fixed finite `B` such that, for every source `a`,
> "`b(n) = 0` for all mixed `n <= B`" implies `a` is multiplicative.

*Construction (`window_evasion_source(B)`).* Let `N = next_mixed_integer_above(B)`
(least integer `> B` with `omega >= 2`; always exists). Take `a = 1` everywhere
except `a(N) = 2`. Then `b(n) = 0` for every mixed `n <= B` (the perturbation at
`N > B` cannot affect any `b(n)` with `n < N`, since `b(n)` depends only on
divisors of `n`), yet `b(N) = 1 != 0`, so `a` is non-multiplicative. Tested at
`B = 6, 10, 20, 37, 50`.  ∎

**Quantifier reading.** Part A is the *sound* `(forall a)(exists B_a)` — the
window depends on the source (`pointwise_window_contract`, PROVED LOCAL). Part B
refutes the *illegal* uniformization `(exists B)(forall a)`
(`uniform_window_contract`, REFUTED). Feeding the two to
`proof_contracts.assert_not_uniformized_from` fires the quantifier-swap guard —
the same `(forall)(exists) -> (exists)(forall)` firewall used elsewhere in the
Forge. A finite experiment can detect a defect that is present `<= B`; it can
never certify global multiplicativity.

---

## Verdict

- **PROVED (formal, CLASSICAL):** the first mixed-prime cumulant identity
  `b(pq) = a(pq) - a(p)a(q)`; the characterization theorem `a multiplicative ⟺ b
  supported on prime powers` (both directions, with the prime-power support
  decomposition); the completely-multiplicative refinement `b(p^k) = a(p)^k/k`;
  the formal Euler-product equivalence; finite-window Part A and the no-uniform-
  window Part B.
- **PROVED LOCAL:** divergence of the factorial source's Dirichlet series for all
  `s` (term test), via an exact witness prime for each `sigma`.
- **TESTED (exact, 34 cases, `OK`):** every statement above on concrete sources,
  the `star_log_unit` / `star_exp` cross-checks, the exp/log round trip, the
  exactness firewall (floats rejected), and the quantifier-swap guard.
- **OPEN / untouched:** RH. Weil positivity is **not** inferred from any correct
  Euler product. Analytic convergence beyond the two curated sources is not
  claimed; absence of a term-test witness in a finite prime window is explicitly
  **not** a convergence certificate.

### Exact statements to quote

- **Characterization:** For `a(1)=1`, `a` is multiplicative ⟺ `log_* a (n) = 0`
  for every `n` with at least two distinct prime factors.
- **Finite detection:** For each fixed `B`, inspecting `{n <= B : omega(n) >= 2}`
  decides "multiplicative up to `B`" and returns the least defect exactly; but for
  every `B` there is a non-multiplicative source passing that test, so no finite
  window certifies global multiplicativity.
