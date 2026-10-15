# Suzuki 2606.09096 — exact proved/conjectural boundary (primary-source read)

**Date:** 2026-10-13. **Branch:** `research/dsv4-periodic-tail-enclosure-2026-10-13`. **RH PROVED: no.**
Source read directly: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (Sep 25 2026), https://arxiv.org/abs/2606.09096 . MSC 11M26 42A82 46E22 47B25.

This note pins, from the paper's own text, exactly what is **proved unconditionally** and what is **conditional/conjectural**. It corrects no prior repo claim (the bootstrap III-B characterization was already accurate) but records the precise statements and quotes so future work does not re-derive the boundary from memory.

## Proved unconditionally (no RH assumed — the paper says so explicitly)

**Framework (Theorem 1.1, §1.2).** For each finite interval the Weil quadratic form, restricted, admits an explicit self-adjoint operator `A_a` via screw functions, replacing the abstract quadratic-form existence of the prior line (Yoshida 1992; Bombieri 2001/2003; Connes–Consani 2023; Connes–Consani–Moscovici). The difference kernel `k(t) = Σ_{ξ(1/2+iγ)=0} e^{-iγt}` (a distribution) is integrated twice to a continuous function, and Weil's explicit formula yields a continuous kernel — *but note: this kernel itself is expressed through the zero set `{γ}`; it is a completed-Weil object, not a zero-independent construction*.

**Theorem 1.3.** The lowest eigenvalue `λ_a` of the finite-interval Weil form is **continuous in `a`**, proved without RH. Corollary: a new proof of Yoshida's result that **RH ⇔ the finite-interval Weil form `Q_W^a` is nondegenerate for every `a > 0`**. (Failure of RH ⇔ `∃a` with `λ_a < 0`; since `λ_a > 0` for small `a`, continuity forces degeneracy at some `a` if RH fails.)

**Theorem 1.5.** On `[-a,a]`, the self-adjoint operator `𝒟̄_{a,θ}` (nonlocal realization of the first-order differential operator, with boundary/extension parameter `θ ∈ [0,2π)`) has eigenvalues **precisely the zeros of** the entire function `W(a,θ;z)`, and **all zeros of `W(a,θ;z)` are real**. (Finite-interval self-adjointness + real-rootedness of the finite-interval characteristic function — the proved local spectral machinery.)

## Conditional / conjectural (the actual frontier)

**Corollary 1.6 (the key statement) is conditional.** Its hypothesis is:

> "If one can choose `λ = λ(a) < λ_a`, `θ = θ(a)`, and `φ(a,z)` for all sufficiently large `a > 0` such that `φ(a,z)` is analytic in the upper half-plane and
> `lim_{a→∞} e^{φ(a,z)} W(a,θ;z) = ξ(1/2−iz)/(ξ(1/2−iz) + ξ'(1/2−iz))`  (1.12)
> holds uniformly on every compact subset of the upper half-plane, **then RH holds.**"

The paper states plainly that (1.12) is "**expected** to hold," "**motivated** by" the structure of the limit space under RH and by the Hilbert–Pólya construction of the cited prior work — it is **not proved**. The **main conjecture** (from the abstract/intro) is that a self-adjoint operator whose eigenvalues are the imaginary parts of the nontrivial zeros is obtained as the limit `a → ∞` of the finite-interval operators.

## The precise gap, restated for this program

1. **Finite-interval → global operator limit is NOT established.** Theorem 1.5 is local; the compact-uniform convergence (1.12) and the existence of a limit self-adjoint operator are the conjecture, not a theorem.
2. **The normalization `e^{φ(a,z)}` and extension choice `θ(a)` must be constructed** with analyticity in the upper half-plane and uniform convergence — the paper does not supply these for all `a`.
3. **The limit target is the completed `ξ` object.** (1.12) targets `ξ(1/2−iz)/(ξ(1/2−iz)+ξ'(1/2−iz))`, which depends on the full completed zeta (including all its zeros in the kernel `k`). A route that *proves* (1.12) is therefore **not** a zero-independent construction; it is a genuine global analysis of the completed Weil form. This is exactly why the repo's "no nontrivial zero positions as construction inputs" firewall (AGENTS.md item 7) is hard to satisfy on this route: the *target* of the limit is ξ itself.
4. **Yoshida equivalence (Theorem 1.3 corollary) is the clean positivity bridge.** RH ⇔ `Q_W^a` nondegenerate ∀`a`. This is a genuine equivalence (classical, via Suzuki's continuity proof), *not* a proof of RH. It converts "global Weil positivity" into "nondegeneracy of every finite-interval restriction" — but the finite-interval forms still carry the completed-Weil data, and "for every `a`" is the global quantifier the bootstrap B-01/B-02 obstruction is about.

## Relevance to the three routes

- **Route A (Weil positivity):** Yoshida+Suzuki reduce it to `λ_a ≥ 0` ∀`a`. The B-01/B-02 obstruction applies verbatim: a bounded self-adjoint operator positive on *every* compression over a strong-dense exhaustion is positive, but the *finite-interval* forms must be identified with the *completed* Weil form, and "every `a`" plus the correct topology is precisely what is not yet earned.
- **Route B (Nyman–Beurling):** independent of Suzuki; unaffected.
- **Route C (spectral realization):** Theorem 1.5 gives the finite-interval half. The missing half is exactly (1.12) and the global limit operator — the conjecture.

**No new theorem is claimed in this note.** It is a primary-source boundary record.
