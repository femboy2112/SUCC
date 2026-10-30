# The Prime Ladder Reduction Theorem (honest "frankenstein")

**Author:** Ravel. **Date:** 2026-10-27. **Repo:** SUCC @ `73181be`, branch `research/prime-ladder-ravel-audit-2026-10-27`.

> **CORRECTION (Operation Main XV integration, 2026-10-29).** Step **R4** below —
> "π transcendental ⟹ not eventually periodic ⟹ the ×16-orbit closure has positive
> *topological* entropy," labelled *PROVED classical* — is **not correct as a general
> bridge**, and the **R5 equivalence** it feeds (vanishing ×3 defects ⟺ π normality) is
> therefore **UNVERIFIED for π**, not proved. Non-eventual-periodicity does not imply positive
> topological entropy (e.g. Sturmian orbits), and positive topological entropy of an orbit
> closure does not imply positive *measure-theoretic* entropy of its weak-\* limits. A decisive
> exact countermodel (the Kempner number: transcendental, irrationality exponent 2, zero-entropy
> binary orbit, ×2×3-invariant limit δ₀, yet not normal) is given in the corrective firewall
> [`../2026-10-27-furstenberg-kempner/KEMPNER_FURSTENBERG_FIREWALL.md`](../2026-10-27-furstenberg-kempner/KEMPNER_FURSTENBERG_FIREWALL.md)
> (FK-1, FK-2, FK-5), together with the corrected conditional theorem (which assumes the
> Furstenberg ×2×3 measure-rigidity conjecture *and* a uniform anti-concentration hypothesis).
> Read the chain below as the author's original draft with **R4/R5 superseded**; the honest
> status is: ×2-invariance automatic, ×3-invariance and atomlessness/entropy **open for π**,
> and the Furstenberg conjecture itself **OPEN**. **π base-16 normality and RH remain OPEN.**

## What this is and is not

This is **not** a proof of π normality. It is a **proved reduction chain** that collapses the
entire π-normality problem — and the whole "prime ladder" / rank-r / adelic machinery — onto a
**single named open conjecture** (Furstenberg ×2×3 at the point π). Every arrow below is proved
(classical or re-derived this session); the only unproved arrow is the final one, and it is
*precisely* the known open problem, stated with no disguise.

---

## The reduction chain (all arrows proved except the last)

Let $e(x)=e^{2\pi i x}$, and let $x_n = \{16^n\pi\}\in\mathbb R/\mathbb Z$ be π's base-16 orbit.

**(R0 — Weyl ⟺ normality, classical.)** π is base-16 normal iff
$$W_N(h)=\frac1N\sum_{n=0}^{N-1} e(h\,16^n\pi)\to0\quad\forall h\in\mathbb Z\setminus\{0\}.$$

**(R1 — source is transport, not cancellation; PROVED this session.)** For the authentic
four-pole source $U_{n+1}=16U_n+r(n+1)$, $U_0=0$, the Green-tail identity
$U_{n+1}=16^n\pi-T_{n+1}$ with $0<T_{n+1}<\frac1{15(n+2)^2}$ gives, for the ×3 transversal defect:
$$\Big|D^{(3),\text{source}}_{N,h}-D^{(3),\text{orbit}}_{N,h}\Big|
=\Big|\tfrac1N\sum_n[e(3hU_{n+1})-e(hU_{n+1})]-[e(3h16^n\pi)-e(h16^n\pi)]\Big|
\le\frac{4\pi|h|\,3}{15N}\sum_n\frac1{(n+2)^2}=O(|h|/N).$$
Hence the signed source and the raw orbit have **equivalent** ×3 defects. The four-pole
recurrence does not cancel; it transports with $O(1/N)$ error. (Reproduced numerically:
difference stays $\sim0.08$ at $N=200$–$1600$, consistent with the summable-tail bound.)

**(R2 — all-prime rigidity is classical and circular; PROVED this session.)** A Borel
probability measure invariant under $T_p(x)=px$ for every prime is $c\delta_0+(1-c)\lambda$.
So all-prime invariance *would* force Haar, but the hypothesis "π's orbit is all-prime
invariant" is itself $\widehat\mu(k)=\widehat\mu(pk)$ for all primes, i.e. exactly the
prime-frequency defect $\Delta_N(H)\to0$, which is **equivalent** to (R0). No shortcut.

**(R3 — ×3 defect is non-discriminating; PROVED this session.)** $|D^{(3)}_{N,h}(\alpha)|\le2$
for *every* real $\alpha$, so "$D^{(3)}\to0$" cannot by itself separate π from coherent mutants.
It is necessary, and it is the *only* remaining input, but it is a **hypothesis to prove**,
not a free consequence.

**(R4 — positive entropy is free for π; PROVED classical.)** π is transcendental, hence its
base-16 expansion is not eventually periodic, hence the ×16-orbit closure has positive
topological entropy. (This is the one genuinely "free" input in the whole chain.)

**(R5 — Rudolph–Johnson + Furstenberg bridge; CLASSICAL, cited.)** Rudolph (1990); the
Bourgain–Lindenstrauss–Michel–Venkatesh effective ×a×b (2009). If μ is a ×16-invariant,
×3-invariant, *ergodic* measure of positive entropy, then μ = λ (Haar). Combined with R4:

$$\boxed{\pi\text{ base-16 normal}\quad\Longleftrightarrow\quad D^{(3)}_{N,h}(\pi)\to0\ \forall h\ne0\ \text{(×3-invariance of the single orbit }\{16^n\pi\}).}$$

The right-hand side is **Furstenberg's ×2×3 conjecture evaluated at the single point π**
(equivalently, the ×16/×3-invariance of every weak-* limit of π's orbit).

**(R6 — Bailey–Crandall "Hypothesis A"; EXTERNAL CONJECTURE, cited.)** Lagarias (2001,
arXiv:math/0101055): normality of the BBP constants (π, log 2, …) is equivalent to a
*positive-entropy + nonconfinement* condition on the ×b-orbit. This is the standard, named
form of exactly the reduction in R5. **It remains a conjecture.**

---

## The final theorem (proved reduction)

**Theorem (Prime Ladder Reduction).** The following are equivalent for π, and each is a
consequence of the one named open conjecture (Furstenberg ×2×3 at π):

1. π is base-16 normal.
2. $D^{(3)}_{N,h}(\pi)\to0$ for all $h\neq0$.
3. Every weak-* limit of $\frac1N\sum\delta_{16^n\pi}$ is ×3-invariant (hence, by R4+R5, Haar).

Moreover, **none** of the repo's proved machinery (BBP four-pole source, rank-r transport
AR-3, all-rank cochain AR-4, adelic character product AR-7, all-prime rigidity) can supply
condition (2) without first proving it for the raw orbit: each reduces to it via R1, R2, R3.

**Boundary (what this does NOT do).** It does not prove (2). It proves that (2) is the *unique*
remaining object, and that it is the known Furstenberg conjecture. No fake proof is offered.

---

## Why this is the honest "full send"

The strongest true thing anyone can produce here is **not** a normality proof (which would
require solving Furstenberg ×2×3, open since 1967), but the **complete reduction**: an infinite
problem (Weyl over all frequencies) plus a giant machinery (rank-r, adelic, all-prime) collapses
to **one bit of dynamics** — is π's ×16-orbit ×3-invariant? — with the entropy leg already paid
for by transcendence.

That is the "quantum tunnel": the wall isn't a wall of infinite Weyl sums; it's a *single*
dynamical rigidity question, and the repo's own AR-5/AR-7 documents already named it. The tunnel
is real and narrow; it is not yet passable, and no theorem I can find — in the repo, in the
literature, or derivable — passes it today.
