# The bidirectional universal-*structure* conjecture: graded channels and the selection defect

**Research continuation, 2026-11-12.** Parent: PR #604, commit `d70a93bcea27f96b76a4de7e6cbd2292975cb030` (Main XXV parent `db9fb4b8`). **π base-16 normality, R0, Goldbach and RH remain OPEN.** A common eigenvector for all the relevant noncommuting operators has **not** been shown to exist; in general it cannot. "Universal eigenstructure" names a *candidate common source/diagram with representations*, not a spectral theorem.

## 1. Steelman: two roots, same carrier, reversed proof cost

A fixed source-labelled path system admits two observational routes:

- **Source-rooted** (`0→∞`): specify origin, successor and causal realizability, retain exact rational histories, then add higher-arity channels, interaction tensors, completed/measure-theoretic probes and laws. The difficulty is constructing enough globally coherent information while keeping the literal source.
- **Global-rooted** (`∞→0`): impose an ambient Hilbert/measure-theoretic representation, symmetry and averaging laws; then descend to one selected arithmetic orbit. The difficulty is reintroducing the source pin **without** losing the exceptional information that averaging erased.

The index 0,1,2,3,4,5 is a design filtration, not a universal time/proof-hardness rank. Hardness requires specifying the allowed oracle/proof language and resource metric. In particular, "universal eigenvector" requires an explicit family of operators and a nonzero vector satisfying **all** eigenrelations, which can fail for noncommuting observables. The proven object is a common **carrier** (`Z`, or SUCC's source-indexed BBP carrier) with multiple observer representations (the PR #604 `Γ=Z` triangle/boost/GNS examples).

## 2. The proposed graded, unit-typed channel basis

Declare channels `i ∈ I` with independent observational slots `V_i` and unit types `U_i`; model a vector `v=Σ_i a_i e_i`, where `a_i ∈ U_i`. Declare complexity grade `g_i=(interaction arity, finite path depth, resource cost) ∈ N^3`. These are **metadata/filtration**, not absolute mathematical Kolmogorov complexity. With a finite observation matrix `A`, operational independence is `rank_Q(A)` (not the number of printed basis vectors).

For an output channel `o` and input hyperedge `S ⊆ I`, a typed multilinear interaction requires a gain

`T_(S→o) : ⊗_(i∈S) U_i → U_o`, i.e. scalar gain unit `U_o / ∏_(i∈S) U_i`.

This is a graded **hypergraph**, not merely a graph. It can be implemented as a colored operad or a multisorted category, but those coherence/naturality laws are **not** certified here. Ordinary direct sums mix like-typed values, tensor products combine units, and a morphism must declare a unit conversion. Simply writing a unit beside a number cannot encode arbitrary coupling.

The finite pure-stdlib implementation `observational_succ/bidirectional_channel_basis.py` includes `Unit`, `Quantity`, `Channel`, `HyperCoupling`, and exact rational independence rank. Tests include a three-input/one-output typed hyperedge, mistyped addition rejection, and rank collapse under redundant observations.

## 3. An exact theorem: irreducible k-way equivalence is invisible to every smaller probe

Put `X_i∈{−1,+1}` for `i=1,...,d`. Let `μ_+` be uniform on sign vectors satisfying `∏_i X_i=+1`; similarly `μ_-` for `−1`. For *every* proper coordinate subset `S⊊{1,...,d}`, the marginal distribution of `X_S` is uniform under both sources. Proof: once values on S are fixed, the final unassigned coordinate is determined by the parity constraint, so exactly `2^(d-|S|-1)` completions exist, regardless of sign.

But `E_(μ_±)[∏_(i=1)^d X_i]=±1`. Thus **all** moments of arity `<d` agree and the d-ary correlation distinguishes the two sources.

The complete Walsh basis `χ_S(x)=∏_(i∈S) x_i` gives exact inversion

`μ(x)=2^(−d) Σ_(S⊆[d])  μhat(S) χ_S(x)`, where `μhat(S)=E_μ χ_S`.

**PROVED LOCAL (classical finite Fourier); exact exhaustive tests d=1..6 and parity inversion.** This is a precise source-map/no-ghost constraint: *a pairwise Aphex-style interaction language cannot in general distinguish all genuine three-way carriers*. A nonlinear pairwise term with access to the full joint history may simulate higher-arity interactions; this counterexample concerns languages whose observations are restricted to pairwise marginals.

## 4. Global-root Fourier energy vs single-source selection

For integer `b≥2`, nonzero integer h, and `T_b x={b x}`, put

`W_(N,h)(x)=N^(−1) Σ_(n=0)^(N−1) exp(2πi h b^n x)`.

Under circle Haar Lebesgue measure, character orthogonality yields **for every N≥1**

`∫_[0,1) |W_(N,h)(x)|² dx = 1/N`.

Proof: expanding the square yields `N^−2 Σ_(n,m) 1_{h b^n=h b^m}` and `h≠0,b≥2` makes only diagonal pairs survive. This is a genuine all-N statement and requires no source information.

**Countermodel (selection failure):** `W_(N,h)(0)=1` for every N,h. For `x=1/(b−1)` the orbit is fixed, and the modulus of the average is 1. No estimate at `x=π/16` follows from global `L²` convergence. Point evaluation is unbounded on `L²` equivalence classes; on span of N distinct characters, evaluation has operator norm `sqrt(N)` (Cauchy–Schwarz is sharp by the normalized reproducing kernel), so even this finite-frequency test space has growing selection cost. This is a *quantitative continuity/selection obstruction*, not a computational-complexity lower bound.

## 5. Stronger theorem: finite temporal and observer-resolution limits fail to commute

Take the uniform grid `G_K={j/b^K:0≤j<b^K}`, and let `E_(K,N)` denote the grid average of `|W_(N,h)|²`. **When gcd(h,b)=1:**

`E_(K,N) = [min(K,N) + max(N−K,0)^2]/N²`.

Proof: grid orthogonality retains a pair `(m,n)` iff `h(b^n−b^m)≡0 mod b^K`. Since gcd(h,b)=1 and `b^r−1` is coprime to b, all frequencies for `n<K` are distinct modulo `b^K`; all `n≥K` alias to frequency zero. There are `min(K,N)` singleton diagonal contributions and one block of size `max(N−K,0)`, contributing its square. No numerical approximation is used.

Consequently,

`lim_(K→∞) lim_(N→∞) E_(K,N)=1` but `lim_(N→∞) lim_(K→∞) E_(K,N)=0`.

This is a concrete finite/continuum, local/global **noncommuting-limits certificate**, *not* a paradox and not a π estimate. A finite grid observer eventually sees every orbit as the 0 fixed point after its resolution has been exceeded; the full Haar observer sees independent characters. It is precisely the kind of finite-to-infinite information loss the two-root picture must handle.

## 6. Source-locked BBP version: the exact reverse-seed selection seam

Now use the **unaltered** SUCC original source

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, `U_0(0)=0`, `U_n(s)=U_n(0)+16^n s`, `x_n={U_n(0)}`.

For a finite integer index set J, frequency h and uniform seed grid `s=j/16^K`, let

`E^BBP_(K,J)(h)=(1/16^K) Σ_(s∈G_K) |Σ_(n∈J) e(h U_n(s))|² / |J|²`.

Finite-character orthogonality gives, **exactly in the group algebra `Q[Q/Z]` before complex evaluation,**

`|J|² E^BBP_(K,J)(h) = Σ_(m,n∈J; h(16^n−16^m)≡0 (mod 16^K)) e(h(x_n−x_m))`.

For gcd(h,16)=1 and a contiguous shell J=[B,2B), let `r=|{n∈J:n<K}|`; the remaining indices `J_tail={n∈J:n≥K}`. Then

`B² E^BBP_(K,[B,2B))(h) = r + |Σ_(n∈J_tail)e(h x_n)|²`.

Three cases:

1. **K≤B:** every seed-grid orbit phase aliases; `E=|W_B(h)|²`. Global-looking averaging has contributed **zero** source-specific cancellation.
2. **K≥2B:** the source drops out, and `E=1/B` automatically. This is *representation orthogonality*, not proof of the selected estimate.
3. **B<K<2B:** the energy explicitly separates source-independent early diagonals from the remaining source-selected signed tail.

The exact code keeps the numerator as a rational-phase **formal group ring** (an exponent→integer-coefficient dictionary) rather than replacing it with a positive real norm and losing the relevant phase sign. Hostile tests replay finite original BBP rational prefixes, rational seed alias `s=1/16`, and null source. The continuation needs a **new source-specific inequality** on the remaining signed term; otherwise the gate is exactly Main XXV R0/normality written in another coordinate. Do not import a generic GNS positivity argument as that inequality.

## 7. Steelman–crucible–verdict

- **SURVIVES / PROVED LOCAL:** graded typed channel arithmetic; finite Walsh reconstruction; exact global Haar second moment; finite-grid noncommuting limits; formal source-locked seed-grid identity.
- **FAILS with receipt:** a single literal “universal eigenvector” follows just from knowing operators; choose Pauli X and Z, which have no common nonzero eigenvector. Every pairwise channel description is complete; the even/odd parity distributions are an exact counterexample. Global L² decay proves the source-selected Weyl bound; source 0 is an exact counterexample. Five numeric coordinates force Hilbert spaces; prior #604 countermodels refute it.
- **HYPOTHESIS / UNVERIFIED:** a natural equivalence/adjunction between source-rooted and global-rooted observers preserving authentic carrier and signed quantitative force; a usable mathematical resource rank on a certified proof-tool category; an all-B `R0` estimate.

**Links and provenance:** [Main XXV π frontier](../../../docs/PI_NORMALITY_FRONTIER.md) §9, [source observer zero anchor](../../2026-11-10/circle_line_lr_observer/zero_anchor_identity/THEOREMS.md), [graded channel code](../../../observational_succ/bidirectional_channel_basis.py), [exhaustive tests](../../../tests/test_bidirectional_channel_basis.py). None of this makes any physically tested claim, RH inference, Goldbach inference, or copyright claim of mathematical novelty.
