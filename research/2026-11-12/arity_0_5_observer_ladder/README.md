# Operation arity 0→5 — the same carrier, enriched observer representations

**Research-only · 2026-11-12 · Main XXV parent `db9fb4b84672050efa79b13377f1e73364598a14`.** Source untouched. **π normality, R0, Goldbach, completed Weil positivity and RH remain OPEN.** No academic priority, physics experiment or kernel-checked general theorem asserted.

## Steelman: the index is a contract, not a number magic trick

The same arithmetic/path carrier can be represented by observers with additional laws. Read 0–5 as an *observer-design sequence*. Different target spaces do **not** imply new carrier elements or nested observer subspaces.

| Index | Proposed interpretive contract | Exact example | Necessary caveat |
|---|---|---|---|
| 0 | Pin source/potential | A distinguished origin; original BBP `U_0=0` | A pin by itself supplies no dynamics |
| 1 | Identity and successor consistency | Path concatenation / natural successor | A one-object monoid already can be dynamic |
| 2 | Opposite/reversal symmetry | Reversed simple edge cancels its transport | Not intrinsically static |
| 3 | First cycle-sensitive motion | **Simple undirected graph** triangle `C₃` has `π₁(C₃)=Z` and character `χ(k)=ω^k` | Directed loops or parallel edges yield shorter cycles; linear algebra preexists |
| 4 | Tetrahedral face coherence and four-real-dimensional Lorentz chart | `d²=0` and `det Herm₂(C)=t²−x²−y²−z²` | Complex involution, determinant and time-orientation are chosen; no GR field equations |
| 5 | Positive-type correlations, null-space quotient, Cauchy completion | GNS/RKHS on the *same* `Z` with `φ(k)=ρ^|k|ω^k` | A fifth **rule**, not five points; positivity alone gives no signed arithmetic estimate |

The exact common-carrier witness is:

~~~text
Γ=π₁(C₃)=Z ─┬─ 3: χ(k)=ω^k                        (cyclic phase)
            ├─ 4: B(k)=diag(2^k,2^-k) ∈ SL₂(Q)   (Lorentz congruence)
            └─ 5: φ(k)=ρ^|k|ω^k → GNS(H,U,ξ)     (Hilbert completion)
~~~

For fixed `0<ρ<1`, consecutive Gram determinants satisfy

`det[K(m,n)]_(0≤m,n<N) = (1−ρ²)^(N−1) > 0`,

so the minimal cyclic Hilbert realization has **infinite dimension** while the loop carrier is still `Z`. See [THEOREMS.md](THEOREMS.md) for the all-N proof, assumptions, phase conventions, countermodels and scope.

**Important correction.** A complex line is already a Hilbert space; the four-stage spinor model already relies on the adjoint of the standard finite-dimensional `C²` geometry. The fifth contract is not the first appearance of *any* Hilbert space: it explicitly **forces completion of a globally infinite-dimensional history representation** for the particular positive kernel.

## What does and does not transport into SUCC

- Source remains `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)` and the literal zero seed `U_0=0`. No frozen file changed.
- Exact three-phase sliding triads on any sequence telescope to four boundary coefficients. Even a nonnormal constant stream has zero k=1,2 triads. **No signed Weyl estimate follows**.
- Four-component Minkowski determinant is an **indefinite** quadratic form; the positive Hilbert–Schmidt and GNS norms are different and not Lorentz-invariant in general. This construction is compatible with a Lorentz action, not with a derived physical Einstein theory.
- The phase Gram `K_h(m,n)=e(h(x_n−x_m))` is always positive semidefinite and rank one, on both the actual source and hostile counterseeds. Generic GNS data **cannot** prove R0 or normality.
- Three-, four- and five-stage representations need not nest or admit canonical intertwiners. At `0<ρ<1`, the GNS representation has no eigenvector for the single-frequency character `χ` (nonatomic Poisson spectral measure).

## Navigation and scope

[THEOREMS.md](THEOREMS.md) · [CLAIM_LEDGER.md](CLAIM_LEDGER.md) · [NEXT.md](NEXT.md) · [VALIDATION.md](VALIDATION.md).
Exact stdlib adapters: `observational_succ/arity_four_bridge.py`, `observational_succ/arity_five_hilbert.py`. Hostile finite checks: `tests/test_arity_four_bridge.py`, `tests/test_arity_five_hilbert.py`.

Canonical repo sources: [π Main XXV frontier](../../../docs/PI_NORMALITY_FRONTIER.md), [Main XXV handoff](../../../docs/MAIN_XXV_HANDOFF.md), [categorical atlas](../../../docs/CATEGORICAL_OBSERVER_ATLAS.md), [recursive meta-SUCC holonomy](../../../docs/CLAIM_SUPPLEMENT_RECURSIVE_META_SUCC.md), [Hilbert carrier](../../../docs/CLAIM_SUPPLEMENT_HILBERT_CARRIER.md), [collective polarization](../../../docs/CLAIM_SUPPLEMENT_COLLECTIVE_OBSERVER.md), [method](../../../docs/METHOD.md), and [AGENTS.md](../../../AGENTS.md).

Classical ingredients: graph fundamental groups; graph connection holonomy and gauge conjugacy; coboundary `d²=0`; Pauli matrices and `SL₂(C)` spinor action; Jordan–von Neumann; positive-kernel Moore–Aronszajn/Kolmogorov–GNS; Herglotz/Poisson kernel; AR(1) Toeplitz covariance. No external scholarly priority claimed for combining them.
