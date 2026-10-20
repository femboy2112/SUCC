# Residue-constrained integer-box counting (Proof Forge III, Part IV)

**Status:** CLASSICAL (elementary geometry of numbers / lattice-point counting).
This is the quantitative-ascent *benchmark*: a provable local-to-global transport
with an **explicit modulus-dependent error** and a **known failure boundary**. No
new mathematics is claimed; the value is a trustworthy, exactly-tested estimate
whose constants track the arithmetic carrier, ready for the abc lane (Part V).

Module: `observational_succ/residue_box_counting.py`.
Tests: `tests/test_residue_box_counting.py` (22 tests).

---

## 1. Theorem

Let `W ≥ 1` be an integer, `R ⊆ (ℤ/Wℤ)²` a set of allowed residue pairs, and
`X ≥ 1` an integer. Define

```
N_R(X) = #{ (a,b) ∈ ℤ_{>0}² : a + b ≤ X,  (a mod W, b mod W) ∈ R }.
```

**Theorem.**
```
N_R(X) = (|R|/W²)·(X²/2) + E_R(X),      with   |E_R(X)| ≤ 5·|R|·(X/W + 1).
```

- **Local density** `|R|/W²` — the fraction of residue pairs that are allowed.
- **Main-term shape** `X²/2` — the area of the simplex `{a,b>0, a+b ≤ X}`.
- **Explicit constant** `5`, absolute (independent of `X, W, R`).

The statement holds verbatim for real `X ≥ 0` as well; we state it for integer
`X` because that is the case the arithmetic application needs, and the boundary
conventions (`a,b ≥ 1`, `a+b ≤ X`) are then unambiguous.

---

## 2. Lattice-point proof

Represent each residue class by its representative in `{1,…,W}` (class `0 ↦ W`);
write `t_r, t_s ∈ {1,…,W}`. For a fixed allowed pair `(r,s) ∈ R`, the admissible
`a ≡ r, b ≡ s (mod W)` with `a,b ≥ 1` are exactly

```
a = t_r + W·i,   b = t_s + W·j,   i, j ≥ 0,
```

because `t_r, t_s ≥ 1` forces `a, b ≥ 1` automatically. The constraint `a+b ≤ X`
becomes `t_r + t_s + W(i+j) ≤ X`, i.e. `i + j ≤ Y` with `Y = (X − t_r − t_s)/W`.
The number of nonnegative lattice points under the triangle `i+j ≤ Y` is, with
`n = ⌊Y⌋ ≥ 0`,

```
#{i,j ≥ 0 : i+j ≤ Y} = Σ_{m=0}^{n}(m+1) = (n+1)(n+2)/2      (and 0 if Y < 0).
```

So `N_R(X) = Σ_{(r,s)∈R} (n_{r,s}+1)(n_{r,s}+2)/2`. This is `residue_box_count`.

**Error accounting, per pair.** With `n = ⌊Y⌋`, `|n − Y| < 1`, `0 ≤ Y < X/W`:

```
|(n+1)(n+2)/2 − Y²/2| = |(n−Y)(n+Y) + 3n + 2|/2
                      ≤ (1·(2X/W+1) + 3X/W + 2)/2  <  3X/W + 2.
```

And `Y²/2 = (X − t_r − t_s)²/(2W²)` differs from `X²/(2W²)` by
`|−2X(t_r+t_s) + (t_r+t_s)²|/(2W²) ≤ (4XW + 4W²)/(2W²) = 2X/W + 2`
(using `t_r+t_s ≤ 2W`). Hence per pair

```
|(n+1)(n+2)/2 − X²/(2W²)| ≤ 5X/W + 4 ≤ 5(X/W + 1).
```

Summing over the `|R|` pairs gives `|E_R(X)| ≤ 5|R|(X/W + 1)`. ∎

---

## 3. Independent floor-sum derivation (second route)

Summing in `a` first and counting admissible `b` in the window `[1, X−a]`:

```
N_R(X) = Σ_{a=1}^{X−1} Σ_{s : (a mod W, s)∈R} c_s(X−a),
  where  c_s(M) = #{1 ≤ b ≤ M : b ≡ s (mod W)}.
```

The key one-line lemma `|c_t(M) − M/W| < 1` (representative convention, all
`M ≥ 0`) gives, with `R_r = {s : (r,s)∈R}`,

```
Σ_{s∈R_r} c_s(X−a) = |R_r|·(X−a)/W + δ_a,   |δ_a| < |R_r|,
Σ_{a=1}^{X−1}|δ_a| < Σ_r |R_r|·c_r(X−1) < |R|(X/W + 1),
```

and the smooth main part `Σ_a |R_{a mod W}|(X−a)/W` reduces, by the same
`c_t` lemma applied in `a`, to `(|R|/W²)(X²/2) + O(|R|(X/W+1))`. This is
`residue_box_count_floorsum`. It is a genuinely different computation; on every
input it agrees exactly with the 2D formula and with the `O(X²)` brute-force
oracle `residue_box_count_bruteforce` (tested on a 250-sample corpus).

---

## 4. Local density and W-dependence

`local_density(W,R) = |R|/W²` exactly. Two genuine arithmetic constraint builders
exhibit the dependence:

- `coprime_pair_residues(W)` = `{(r,s): gcd(r,W)=gcd(s,W)=1}`, `|R| = φ(W)²`,
  density `(φ(W)/W)²`.
- `coprime_sum_residues(W)` = `{(r,s): gcd(r+s,W)=1}` (the primitive-sum / "`c`
  prime to the modulus" constraint), `|R| = W·φ(W)`, density `φ(W)/W`.

These are the model shapes for a genuine `a+b=c` prime-power constraint; the abc
lane (Part V) composes them from `squarefree`/`exponent-cap` predicates via
`residues_from_predicate`.

---

## 5. Growing modulus `W = W(X)` — the explicit failure boundary

The main term `|R|·X²/(2W²)` beats the proved error bound `5|R|(X/W+1)` iff

```
X²/(2W²) > 5(X/W + 1)   ⟺   X² > 10 W X + 10 W²   ⟸   X > 10 W,
```

independently of `|R|` (both sides scale with `|R|`). So:

- for a modulus growing slower than `X/10` the asymptotic is informative;
- at `W ≍ X` the error bound is ≥ the main term and the estimate is **vacuous**.

`growth_regime(X,W,R)` reports `main_dominates` and the explicit threshold
`dominance_threshold_X = 10W+1`. This is the honest boundary the campaign asked
for: the elementary error term (`O(X/W)` relative) becomes too large exactly when
the window `W` reaches the scale of the box `X`. Pushing past it needs a genuinely
different input (Fourier/large-sieve/dispersion) — that is the open research edge,
not a renaming.

---

## 6. Controls

- **Three-route exact agreement** (2D formula = floor-sum = brute force) on a
  randomized corpus — the independent-oracle cross-check.
- **Invalid inputs rejected**: residue outside `(ℤ/Wℤ)²`, `W < 1`, non-integer
  `X` all raise `ResidueBoxError`.
- **Additivity / mutation**: `N` is additive over disjoint `R`; removing one
  allowed pair drops the count by exactly that class's contribution.
- **Boundary**: `X=1 → 0`; class-`0` representative is `W` (so `(0,0) mod 4`
  first appears at `a+b=8`).

---

## 7. What this is and is not

It **is** a rigorous local-to-global quantitative transport with explicit
constants and a proved degeneration boundary. It is **not** new mathematics, not
an abc result, and not a bound that survives `W ≍ X`. RH / ABC / integer-abc /
signed `S₄` remain **OPEN**; nothing here touches them. The deliverable is a
trustworthy estimate the abc moment lane can actually stand on.
