# Ω₃: strong infinitary convergence without a head value

**2026-11-10 follow-up to [operational completion](README.md), draft PR #579.** This is an established classical infinitary-lambda phenomenon, with an explicit proof in SUCC's `E_k(m)` notation; it is not a π-normality theorem and claims no discovery priority.

## The two normal-form predicates must be kept apart

Let `ω_k = λx. x x ... x` with `k≥2` left-associated copies, and let `E_k(m)` be the left-associated application of `m` copies of `ω_k`.

**Finitary theorem (already in [OMEGA_INTERPRETER](../scott_omega_causal_weld/OMEGA_INTERPRETER.md)):** the unique beta-redex of `E_k(m)`, for `m≥2`, is at the left-child address `f^(m-2)`, and
```math
E_k(m)\to_\beta E_k(m+k-2).
```
For `k≥2`, `Ω_k=E_k(2)` has no **finite** beta-normal form or finite head normal form. With `k=2`, a beta step returns the same term at depth zero.

**Additional infinitary theorem (classical setting, made explicit here):** for `k≥3`, in the **unrestricted infinite lambda-term tree space** (the 111/unrestricted metric setting), the infinite leftmost reduction
```math
E_k(2)\to E_k(k)\to E_k(2+2(k-2))\to\cdots
```
is strongly convergent to the infinite left spine `L_k` satisfying the coinductive tree equation
```math
L_k = (L_k\;\omega_k).
```
The limit is a beta-normal infinite tree: every finite left prefix has only application nodes, every right child is `ω_k`, and the bodies of the `ω_k` contain only bound-variable applications. No subterm at a finite address is a beta-redex.

**Proof.** After `j` contractions, the copy count is `m_j=2+j(k-2)`; the redex contracted next is at depth `m_j-2=j(k-2)`, which tends to infinity for `k≥3`. The term trees stabilize at every fixed finite depth. More precisely, with the usual tree ultrametric, the first mismatch from `L_k` is at depth `m_j-1`; hence `d(E_k(m_j),L_k)=2^{-(m_j-1)}\to0`. Redex depths tend to infinity, so the reduction is **strongly** convergent (not merely Cauchy). The displayed limit has no finite-address beta redex. ∎

For `k=2`, this argument fails: every contraction is at the root and does not yield a strongly convergent infinitary reduction to normal form. This is a precise `k=2` vs `k≥3` distinction.

## Why this does not produce the BBP digits

`L_k` is an **infinite left spine without a head constructor**. It does not provide a natural-number selector or a numeral at a fixed position. In Böhm-tree semantics, the head-unsolvable term has bottom/undefined observation; in the permissive unrestricted infinitary syntax, the infinite left spine can nevertheless be a beta-normal **tree**. Those statements coexist because the observables and allowed infinite terms differ.

Thus `Ω₃` supplies **topologically stabilizing syntax**, not a productive arithmetic stream. The BBP source has a different, *guarded*, numerical limit: its backwards future-tail operator `(Ft)_n=(r(n+1)+t_(n+1))/16` contracts in sup norm and each finite rational prefix terminates. To identify the two one needs an *internal*, source-labelled operational compiler that maps reduction addresses and clocks to exact BBP transition, integer lift and boundary crossing. Simply decorating the `Ω₃` step count `n→n+1` with arbitrary forcing is a generic path map, not that compiler.

**Potential probe:** distinguish (1) `Ω₂` root stagnation, (2) `Ω₃` increasing-depth strongly convergent left spine but no head value, and (3) a guarded BBP prefix iterator with a terminating `nth` query. Compare ordinary Böhm trees, clocked Böhm trees, integer/carry output and finite exact source prefixes. A sound compiler must preserve **and reflect** the data claimed, not silently convert an unsolvable head into a productive digit source.

## Provenance and authority

- Kennaway, Severi, Sleep, de Vries, *Infinitary Rewriting: From Syntax to Semantics*, **Example 37(3)**: `Ω₃` reduces to an infinite left spine; Lemma 38 distinguishes weak-head/head undefinedness. [Primary PDF](https://www.cs.le.ac.uk/people/fdv1/fdv1/Distribution/kssv2005.pdf).
- Endrullis, Hendriks, Klop, Polonsky, *Discriminating Lambda-Terms Using Clocked Böhm Trees*, *Logical Methods in Computer Science* **10(2:4)**, 2014: computational clocks distinguish certain extensionally identical infinite terms. [Publisher](https://lmcs.episciences.org/880).
- [Current SUCC exact growth law, corrected redex addresses and separate rational evaluator](../scott_omega_causal_weld/OMEGA_INTERPRETER.md).

**Claims:** infinite-left-spine convergence = **CLASSICAL, reconstructed proof**; exact finite rational carry cocycle = **PROVED** in [README](README.md), finite tested; source-faithful guarded omega compiler = **UNVERIFIED**; original-zero parity balance and pi normality = **OPEN**.
