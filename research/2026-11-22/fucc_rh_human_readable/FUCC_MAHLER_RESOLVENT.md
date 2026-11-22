# Prime-square FUCC resolvent exactly produces the local height-two formal logarithm

**22 November 2026 — new-to-this-SUCC source/operator identification; all proof statements scoped.** This is a constructive equality using the original prime-dilation **operators** of FUCC, but with a **declared different weighting** from the critical Suzuki/FUCC tower. It does not establish any theta-kernel integrality or RH theorem.

## R1 — Exact bounded Neumann resolvent on FUCC Hilbert space (PROVED)

Let `H=ℓ²(N_{>0})`; for any integer m>=2, let `V_m e_n=e_(mn)`. Each V_m is an isometry, `||V_m||=1`. Fix a genuine arithmetic prime p. Since `||(1/p)V_(p²)||=1/p<1`, the norm-convergent inverse exists:

```
R_p = (I - p^(-1) V_(p²))^(-1)
    = sum_(j>=0) p^(-j) V_(p^(2j)).
```

In particular,

```
R_p e_1 = sum_(j>=0) p^(-j) e_(p^(2j)),
||R_p e_1||² = sum_(j>=0) p^(-2j) = p²/(p²-1),
||R_p|| <= p/(p-1).
```

This is an actual bounded real-Hilbert-space operator identity; no asymptotic fit or smoothing has been used.

## R2 — Exact transfer to the height-two formal logarithm (PROVED)

Define the coefficient dictionary `Φ(e_n)=T^n` and extend it **coefficientwise** from the rational finite-support vectors, then to the particular rational-coefficient vector `R_p e_1`. This is not claimed to be a Hilbert-space unitary into a p-adic function space; only the specific coefficientwise formal image is needed.

Then

```
Φ(R_p e_1)
 = l_p(T) = T + sum_(j>=1) T^(p^(2j))/p^j.
```

Because substitution by T^(p²) corresponds to `V_(p²)` on monomial labels,

```
l_p(T) - p^(-1) l_p(T^(p²)) = T.
```

So l_p solves the **p²-Mahler functional equation** `l_p(T)=T+(1/p)l_p(T^(p²))`. This is exactly the formal local logarithm used in Rubinstein's model of the Alpöge–Claude arithmetic derivative (working guide, Part II §2, equations (II.4)–(II.5)). The coincidence is at the level of an exact constructible series, **not** of actual automorphic period coefficients.

## R3 — Combine with the p-adic derivative theorem (PROVED, within formal-model hypotheses)

Since l_p has constant term 0 and linear coefficient 1, it has a unique formal compositional inverse U_p. For any `f(T)∈Z_p[[T]]`, the proof in `TECHNICAL_PROOFS.md` establishes for every a>=1

```
v_p((f∘U_p)^(a)(0)) >= v_p(a!) - (a-1)/(p²-1).
```

Thus the explicit FUCC resolvent **constructs the formal-logarithm input** to the local valuation-gain theorem. The resulting derivative growth is `a(1/p+1/p³+...)-O(log a)`, precisely the *local model's* arithmetic-multiplicity signature. The proof is an induction on formal-series coefficients, not a statistical or Gaussian argument.

## R4 — What the result does NOT give (explicit boundary)

1. **Original source weighting:** the scalar `1/p` in this resolvent is **selected by the height-two formal-logarithm model**, not deduced from the earlier critical FUCC tower coefficient `sqrt(log p)*p^(-k/4)`. The native shift channel is original FUCC; the weighting is a new declared operator choice. Source-faithfulness to Alpöge's theta lifts therefore remains to be proved.
2. **Unbounded p-adic denominators:** `l_p(T)` has coefficients p^(-j); they are not all in Z_p. The reverse/compositional operation U_p and the factorial derivative produce valuation gains when f is integral. One cannot simply label the resolvent itself as p-adically integral.
3. **No actual theta period map:** the proven identity does not show that Alpöge's CM theta kernel, its algebraic coordinate system, or its lattice minors are represented by `Φ R_p`. Those are the load-bearing imported inputs of (M).
4. **Hilbert norm is not an Arakelov slope:** `||R_p e_1||²=p²/(p²-1)` is a genuine real norm on a **single coefficient vector**, but it is not the independently normalized Archimedean size bound for the actual algebraic period map. In particular there is no nonzero integral determinant whose local positive valuations and real norm are both controlled by these equations alone.
5. **Primes versus fake sources:** any integer m>=2 can be used to write `I-(1/p)V_(m²)` as an operator, but only the genuine prime p and the exponent p² agree with the asserted local formal-logarithm/valuation construction. A Beurling fake generator has no automatic p-adic interpretation.

## Discriminating next theorem

Find a source-authenticated map from the specific, normalized **theta-kernel integral lattice** in the released Lean proof to an integral FUCC/Mahler module in which (a) the formal-logarithm inverse U_p is the actual change of local coordinate, (b) the same normalized period minor retains nonzero rank, and (c) its global Hermitian norm is independently bounded. This is a theorem target, not a claimed identification.

**Verdict:** the previously missing *formal-series source* is constructible exactly from FUCC, but the actual automorphic theta-integrality and global arithmetic inequality (M) remain **UNVERIFIED in SUCC**.
