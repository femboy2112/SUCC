# A precise information-theoretic carrier advantage

**2026-11-12.** Additive result under an explicitly declared hypothetical probability law. This is not an entropy model proven for genuine primes, nor a proof that a carrier-style proof of Goldbach is logically necessary.

## CARR-09 — Shared-source joint entropy versus marginal-only encoding (PROVED LOCAL)

Let `M>=1` and `0<q<1`. Let `X_1,...,X_M` be *independent* Bernoulli(q) random variables, and let `A=(A_ij)` be the `M x M` binary matrix with `A_ij=X_i X_j`. Binary entropy is `h2(t)=-t log2(t)-(1-t)log2(1-t)`.

**Theorem.** The complete matrix has joint Shannon entropy

```
H(A) = M h2(q).
```

But the sum of its **individual-entry marginal entropies** is

```
sum_(i,j) H(A_ij) = M h2(q) + M(M-1) h2(q^2).
```

For fixed `q` strictly between 0 and 1, the second quantity exceeds the first by `Theta(M^2)` bits. The second quantity corresponds to separately encoding each entry with its optimal marginal distribution **without joint source-sharing**. It is not an information-theoretic lower bound for every conceivable object-oriented encoder, since an object-oriented implementation may itself exploit shared state and attain the joint bound.

**Proof.** The map `X -> XX^T` is injective for binary `X`: `A_ii=X_i^2=X_i`. Hence `X` and `A` determine each other, and `H(A)=H(X)=sum_i H(X_i)=M h2(q)`. On the diagonal `A_ii=X_i` is Bernoulli(q); off the diagonal `A_ij` is Bernoulli(q^2) by independence. There are `M` diagonal and `M(M-1)` off-diagonal entries. Summing their separate entropies proves the claimed formula. QED.

At `q=1/2`, `h2(1/4)=0.811278124459...`, so

```
H_joint = M;
H_marginal_only = M+0.811278124459... M(M-1).
```

The true Goldbach source is a **deterministic prime mask**, not an i.i.d. Bernoulli law. Its Shannon entropy is undefined without a chosen probability distribution (or zero if viewed as a point mass); however its finite interaction table still has the exact low-rank deterministic representation in CARR-01. The plain Kolmogorov description length given the cutoff `M` remains O(1), since primality is computable by one fixed finite algorithm. This is a description-length statement, *not* a runtime or proof-length bound.

## Independent finite enumeration check (OBSERVED)

All binary masks up to `M=8` were exhaustively enumerated at `q=1/2`, and the marginal entropy computed from the observed frequencies matched the formula. Outputs:

```
M=3: H_joint=3, sum H_marginal=7.86766875
M=4: H_joint=4, sum H_marginal=13.73533749
M=6: H_joint=6, sum H_marginal=30.33834373
M=8: H_joint=8, sum H_marginal=53.43157497
```

These finite enumerations calibrate the implementation of the formula; the theorem above is the elementary proof. None speaks to actual-prime randomness or proves Goldbach.

## Practical interpretation and proof debt

A representation of pair interactions as unrelated independent facts repeatedly pays for the same source bits. The shared-carrier model stores the one-body source and computes `A_ij` through the fixed coupling law. Reindexing into midpoint/displacement coordinates (and, more generally, conditioning the separable prime-pair vector on a fixed sum) may reveal high-rank *observed* structure without adding independent source information. This is a precise way to distinguish **representation entropy** from **observational relational complexity**.

It does not show that every source can be compressed or that no object-based proof is possible. In particular, strong Goldbach still requires a genuine source-specific lower bound on the mixed additive–multiplicative intertwining defect `D` in [MIXED_COUPLING.md](MIXED_COUPLING.md). That estimate is **OPEN**.

References: [CARR-01 dossier](README.md); Ming Li and Paul Vitanyi, *An Introduction to Kolmogorov Complexity and Its Applications*, 4th ed. (2019), https://link.springer.com/book/10.1007/978-3-030-11298-1 .