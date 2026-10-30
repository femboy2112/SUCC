# The First Atom: a proved finite↔global↔Yoneda template for SUCC

**Author:** Ravel, building Leah's "finite lattice → point → categorical → Yoneda" intuition.
**Date:** 2026-10-27. **Predecessor:** `research/2026-10-12/LOCAL_GLOBAL_YONEDA_GLUE_2026-10-12.md` (LG1–LG7).
**Status:** the toy where the *entire* chain closes, proved. Serves as the atom to scale up.

---

## 0. The intuition, made precise

Leah's proposal, translated into mathematics:

1. **Finite lattice** — a finite amount of data, constructible in finite work.
2. **Extending to infinity** — take the inverse limit (zoom out orthogonally / infinitely fast).
3. **Looks like a point** — the inverse limit is a single well-defined object (compact by Tychonoff).
4. **A point in a categorical system** — that object is an object of a category C.
5. **Invoke Yoneda** — the presheaf of "observables" $\operatorname{Hom}(-,X)$ fully determines $X$,
   giving a **finite ↔ analytic/global correspondence**.
6. **Build the right atoms** — assemble enough such objects that the real target (π normality)
   becomes a gluing/cofinality problem, not a raw analytic one.

The archive (LG1–LG7) already built steps 1–3 and *warned* (LG7) that Yoneda alone gives
**structure, not content**: it says local sections glue *iff* holonomy vanishes, but not *whether*
it vanishes. The first atom is the object where the correspondence is a **proved isomorphism**,
so we have a *correct template* whose boundary is known exactly.

---

## 1. The atom: $\mathbb Z_2$ as inverse limit, with the character presheaf as the dual

**Finite layer.** For each $n\ge1$, $L_n=\mathbb Z/2^n\mathbb Z$, a finite lattice of $2^n$ points.
These are the *finite probes*: an observable of level $n$ is a character
$\chi_a(x)=e(ax/2^n)$, $a\in\{0,\dots,2^n-1\}$.

**Inverse limit.** $\mathbb Z_2=\varprojlim_n \mathbb Z/2^n\mathbb Z$ — the 2-adic integers. This is the
"point at infinity": the finite lattices, zoomed out, are the compact profinite group $\mathbb Z_2$.

**The point in a category.** $\mathbb Z_2$ is an object of the category of compact abelian groups.

**The dual (analytic/global) side.** The continuous characters $\widehat{\mathbb Z_2}\cong\mathbb Z[1/2]/\mathbb Z$
— the *global observables*. A global observable is $e(tx)$ for a dyadic rational $t$.

---

## 2. THE THEOREM (the atom's payload — proved)

**Theorem (finite ↔ global correspondence for the atom).** The restriction map
$$\Phi_n:\widehat{\mathbb Z_2}\to\widehat{\mathbb Z/2^n},\qquad (t\mapsto e(t\cdot))\ \mapsto\ (a\mapsto e(ta/2^n))$$
is **surjective** for every $n$, and the family $\{\Phi_n\}$ is **cofinal** and **injective in the
limit**: the global observables are exactly the inverse limit of the finite observables.

**Proof.**
- *Surjectivity:* a finite character $\chi_a$ of level $n$ lifts to the global character with
  $t=a/2^n$ (a dyadic rational), and $\Phi_n(t)=\chi_a$. ∎
- *Injectivity in the limit:* two global dyadics $t,t'$ agree as observables at every finite level
  iff $t-t'\in\mathbb Z$, i.e. they are the *same* element of $\widehat{\mathbb Z_2}=\mathbb Z[1/2]/\mathbb Z$. ∎
- *Cofinality:* the finite levels $\{\mathbb Z/2^n\}$ are cofinal in the tower, so the inverse limit of the
  finite observables *is* $\widehat{\mathbb Z_2}$ by definition of profinite duality. ∎

**Verified:** at $n=4$, all $16$ finite characters are reached from global dyadic observables
(surjectivity check passed exactly).

---

## 3. Where Yoneda enters — and exactly what it does and does not buy

Yoneda says: the representable presheaf $\operatorname{Hom}_{\mathbf{Ab}^{\mathrm{c}}}(-,\mathbb Z_2)$ fully
determines $\mathbb Z_2$. Its content here is the *duality*

$$\widehat{\mathbb Z_2}\ \cong\ \varprojlim_n \widehat{\mathbb Z/2^n},$$

i.e. **"observing from the global/analytic place" (characters of $\mathbb Z_2$) is *isomorphic* to
"observing finitely" (characters of all $\mathbb Z/2^n$) with the inverse-limit coherence.** That
is a *true, proved* correspondence — for this atom, there is **no information loss** between finite
and global.

**The boundary (carried over from LG7, now sharp).** The correspondence is an *isomorphism of
observables*, not a *solution to any specific holonomy/equidistribution problem*. It says the
observable data are the same on both sides; it does **not** say the specific object (π) has the
specific property (normality). The atom proves the *template is sound*; it does not fill in the
*content* (which for π is the Weyl/×3-invariance statement, still open).

---

## 4. Why this is the right first atom — and the scale-up plan

This atom is *meaningful* (it is literally the 2-adic clock already in SUCC, #321/#330), it closes
*completely* (the correspondence is a proved isomorphism), and it has a *known, precise boundary*
(the correspondence is structural, not content).

The scale-up is now well-defined:

- **Atom 2** — the dyadic solenoid $\mathbb R\times\mathbb Z_2/\Delta\mathbb Z$ (already in #330):
  its character group $\mathbb Z[1/2]$, and the *same* finite↔global Yoneda correspondence.
- **Atom 3** — the $\{2,3\}$-solenoid $X_{2,3}$ (AR-1): characters $\mathbb Z[1/6]$, the rank-2
  object where ×16 and ×3 both act. Here the finite↔global correspondence is *still* a proved
  isomorphism of observables — but the *content* question (is π's orbit ×3-invariant?) is exactly
  the one place where Yoneda stops being free.
- **The goal** — assemble atoms 1–3 so that "π normality" is expressed as a **gluing/cofinality
  condition** on observables (a Čech-style descent, LG1-style), and the *single* remaining
  content-cell is the ×3-invariance of π's orbit, now formally typed and isolated.

---

## 5. Status and boundary (honest)

- **Proved:** the finite↔global character correspondence for $\mathbb Z_2$ (the atom), with
  surjectivity/cofinality/injectivity and an exact finite check.
- **Not proved:** anything about π normality. The atom is a *sound template*, and it *sharpens*
  the categorical side of the ×2×3 wall — it does not remove it.
- **Next:** Atom 2 (dyadic solenoid) and Atom 3 ($X_{2,3}$), then formalize the correspondence in
  Lean (the archive's own "next probe" #4). The payoff is a *machine-checked* finite↔global bridge
  that turns the π-normality wall into a single, named, formally-typed cofinality/descent condition.
