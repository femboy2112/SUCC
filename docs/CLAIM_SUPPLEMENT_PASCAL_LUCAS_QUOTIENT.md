# PLQ — Pascal/Lucas quotient and prime operator bridge

**Date:** 2026-10-24. **Parent:** source-selection draft #273 at `8d89711db77fea81920321d32f831eed3dec1e68`, itself stacked on Pascal-source draft #272. **Pi normality OPEN.** No new Lean kernel authority or independent external review.

| Claim | Scope and precise proposition | Status | Evidence / next falsifier |
|---|---|---|---|
| PLQ-01 | Odd Pascal cells with `n<2^m` biject with ordered ternary digit words, via `d_i=n_i+k_i` | CLASSICAL/PROVED PAPER | Lucas theorem + inverse digit coding; compare all pairs against integer `comb(n,k) % 2` |
| PLQ-02 | `P_m Z_m = T_m P_m` for Boolean-incidence zeta and rank-average | PROVED PAPER | Permutation equivariance, fixed-rank subset counting; exhaustive rational-vector tests |
| PLQ-03 | The kernel of rank-average has dimension `2^m-(m+1)` and is zeta-invariant | PROVED PAPER | Surjectivity, rank-nullity, PLQ-02; explicit signed kernel mutant |
| PLQ-04 | Common bivariate enumerator is `(1+u+uv)^m`; no residual parity cells after identifying weighted-binomial triples | PROVED PAPER | Digitwise product expansion and finite coefficient checks |
| PLQ-05 | Prime `p` Lucas support is `J_p^tensor m`; support total `[p(p+1)/2]^m` and digit-prefix coding coherent | CLASSICAL/PROVED PAPER | Lucas + digitwise multiplication + exhaustive enumeration |
| PLQ-06 | Symmetric histogram quotient of `J_p^tensor m` has coefficient polynomial `product_a (x_0+...+x_a)^h_a` | PROVED PAPER | Permutation equivariance and counting; independent tensor vs quotient checks |
| PLQ-07 | Residue-valued Pascal matrix modulo `p` equals tensor of digit-binomial residue blocks, but support-only lift fails for `p=3` | CLASSICAL/REFUTED MUTANT | Lucas and `(2 choose 1)=2 mod 3`; direct integer modular oracle |
| PLQ-08 | Under natural `p<q` digit inclusion, uniform-Lucas-state TV gap is `1-(L_p/L_q)^m` | PROVED PAPER | Explicit intersection of finite uniform measures; `2->3,m=4` yields `15/16` TV, *not* pi carry |
| PLQ-09 | Ternary successor cannot be defined on rank or histogram quotient compatibly with exact ternary coding | REFUTED QUOTIENT DESCENT | Words `(0,1),(1,0)` have same histogram, successor words `(1,1),(2,0)` do not |
| PLQ-10 | Under synthetic uniform `m`-bit `n`, `k=0`, optimal rank-only four-bit-gate MSE has the exact overlap formula; `m=5` gives `1/40`, limit `15/256` | PROVED PAPER/VERIFIED FINITE | Hypergeometric conditional expectation + two-subset overlap; full binary enumeration |
| PLQ-11 | Lucas ternary coding extends to a snowflake homeomorphism from `Z_3` onto a Lucas-pair Cantor subset of `Z_2 x Z_2` but is not additive | PROVED PAPER | First-difference digit valuation and explicit nonadditivity |
| PLQ-12 | Every continuous additive homomorphism `Z_p -> Z_q` with distinct primes is zero | CLASSICAL/PROVED PAPER | Continuity on `p^n ->0`, prime-to-q unit norm; no claim that digit homeomorphisms are additive |
| PLQ-13 | Lucas quotient identities imply the source-selected BBP four-bit carry bound or pi normality | UNVERIFIED | No authenticated factor/source fiber cancellation. Next probe: source-preserving lift + actual selected signed correlation bound |
| PLQ-14 | For any source probability `mu` and [0,1]-gate `G`, the symmetrization fiber defect is bounded by `TV(mu,mu_sym)`, sharply | PROVED PAPER/VERIFIED FINITE | Finite signed-measure duality; point at `n=16` among five binary positions yields equality `4/5` |

**Steelman–crucible–verdict:** canonical identification kills a spurious numerical residual; the surviving operator quotient has a concrete nonsymmetric kernel. Prime support omits residue phase; histogram quotient loses SUCC. Preserve the full fiber and literal BBP integer carry. Do not convert these exact source-agnostic results into real-orbit frequencies without an authentic source estimate.

Complete proofs and boundaries: [PI_PASCAL_LUCAS_QUOTIENT.md](../research/2026-10-24/PI_PASCAL_LUCAS_QUOTIENT.md). Implementation and controls: [module](../observational_succ/pascal_lucas_quotient.py), [tests](../tests/test_pascal_lucas_quotient.py), [probe](../scripts/pascal_lucas_quotient_probe.py).
