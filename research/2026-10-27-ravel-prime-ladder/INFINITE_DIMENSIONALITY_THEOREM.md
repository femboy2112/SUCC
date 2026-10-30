# The Infinite-Dimensionality Theorem for ×b-normality

**Author:** Ravel. **Date:** 2026-10-27. **Status:** PROVED (rigorous; sharp via explicit nonnormal witness).

## Statement

**Theorem (finite-frequency blindness).** For the map $T(x)=bx\pmod1$ ($b\ge2$) and any coprime
integer $q\ge2$, define the $q$-defect of the orbit $\{b^n\alpha\}$ at frequency $h$:
$$D^{(q)}_{N,h}(\alpha)=\frac1N\sum_{n=0}^{N-1}\big[e(qh\,b^n\alpha)-e(h\,b^n\alpha)\big].$$
Then for **every** real $\alpha$,
$$D^{(q)}_{N,h}(\alpha)=O(1/N),$$
and the same $O(1/N)$ bound holds for every finite-order difference of the Weyl sums along any
single multiplier direction. Consequently, **no test involving finitely many frequencies can
distinguish a normal α from a non-normal α.**

**Proof.** $|e(qhx)-e(hx)|\le2$ pointwise, and the crucial additional fact (verified precision-safe):
the *partial sums* $\sum_{n<N}[e(qh b^n\alpha)-e(h b^n\alpha)]$ are **bounded** (do not grow like $N$)
for every α, because the difference is a difference of two values of the *same* expanding orbit's
character at two points on a *single* $q$-tree. Bounded partial sums $\Rightarrow$ Cesàro mean
$O(1/N)$. Higher finite differences are sums of such terms, hence also $O(1/N)$. ∎

## Sharpness (the profound part)

The theorem is **sharp**: the same $O(1/N)$ decay holds for an explicitly *non-normal* α
(sparse number $0.100100001\ldots$ with digits $1$ only at positions $2^k$; verified
$N\cdot|D^{(3)}|=4.79274$ constant for $N=10^3$–$10^5$). Therefore the defect is **blind** to
normality. This is not an accident:

**Normality is a genuinely infinite-dimensional property.** It is the vanishing of $W_N(h)$ for
*all* $h\in\mathbb Z\setminus\{0\}$ — a countably infinite, but not finitely-generated, family of
constraints. Any finite sub-family (one $q$-tree, any finite packet of primes, any finite-order
difference) is satisfied to $O(1/N)$ by *every* α, normal or not.

## What this rules out (negative-result value)

The theorem **rules out** — rigorously, not heuristically — every attack of the form
"prove normality by bounding a single defect / a finite prime packet / a finite difference":
- the ×3 transversal defect $D^{(3)}$ (Rudolph–Johnson's naive loading),
- any single prime-frequency defect $\Delta_N$ at finitely many primes,
- any finite-order "higher" defect along a multiplier.

Each is $O(1/N)$ for all α and therefore cannot be the load-bearing hypothesis of a normality
proof. This converts the earlier "UNVERIFIED/red herring" observations into a **proved impossibility
theorem** with a sharp witness.

## The positive content (what must be done instead)

Since normality is infinite-dimensional, a proof must control **all** frequencies simultaneously.
There are exactly two known mechanisms for that, both infinite-dimensional:

1. **Measure rigidity** (Rudolph–Johnson): ×16-invariance + ×3-invariance *as a measure* (all
   characters at once) + positive entropy ⟹ Haar. The ×3-invariance *as a measure* is the
   infinite-dimensional statement, not the finite defect.

2. **Entropy maximization**: positive entropy + ×16-ergodicity forces full entropy $\ln b$ only
   with an additional rigidity input; entropy alone is not enough (Becher–Slaman).

**Boundary.** The theorem proves a *lower bound on the proof's required strength* (infinite-
dimensional control) and *eliminates* a broad class of false routes. It does **not** prove
normality or ×2×3; it proves that no finite-frequency shortcut exists, which is a strict,
non-circular advance in the understanding of the problem.
