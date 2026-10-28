# Atom 2: the dyadic solenoid — a proved finite↔global correspondence on $\widehat{\mathbb X} = \mathbb Z[1/2]$

**Author:** Ravel, building on Atom 1 (`FIRST_ATOM.md`, the $\mathbb Z_2$ atom) and the SUCC solenoid object #330.
**Date:** 2026-10-27. **Branch:** `research/prime-ladder-ravel-audit-2026-10-27`.
**Companion code:** `atom2_dyadic_solenoid.py` (exact `Fraction` arithmetic, no floats).

---

## 0. What this atom is, and how it differs from Atom 1

Atom 1 closed the finite↔global chain for the **2-adic integers** $\mathbb Z_2$, whose character
group is the *torsion* group $\widehat{\mathbb Z_2} \cong \mathbb Z[1/2]/\mathbb Z$ (the Prüfer 2-group).
The dyadic solenoid is the *other* classical $\{2\}$-completion object: it is **connected** (not
totally disconnected), and its character group is the **full** discrete dyadic group
$\mathbb Z[1/2]$, with *no* quotient by $\mathbb Z$.

The mathematical content is therefore the same shape of correspondence — surjective at every finite
level, cofinal, injective in the inverse limit — but the dual object is **torsion-free** ($\mathbb Z[1/2]$)
instead of torsion ($\mathbb Z[1/2]/\mathbb Z$). Both atoms are *sound templates*; the difference matters
when, at Atom 3, the $\{2,3\}$-solenoid $X_{2,3}$ brings in a *rank-2* dual $\mathbb Z[1/6]$ that mixes the two.

---

## 1. Objects, definitions, domains (all quantifiers explicit)

**The dyadic solenoid.** Let $\mathbb Z_2 = \varprojlim_n \mathbb Z/2^n\mathbb Z$ be the 2-adic integers,
and embed $\mathbb Z \hookrightarrow \mathbb R$ (additively) and $\mathbb Z \hookrightarrow \mathbb Z_2$
(diagonally, $n \mapsto (n \bmod 2^k)_k$). Define the *diagonal* subgroup
$\Delta\mathbb Z = \{(n,n) : n\in\mathbb Z\} \subset \mathbb R\times\mathbb Z_2$, and the dyadic solenoid

$$\mathbb X \;=\; (\mathbb R \times \mathbb Z_2)\,/\,\Delta\mathbb Z .$$

$\mathbb X$ is a compact, connected, one-dimensional abelian group (the standard dyadic/adler solenoid).
It is *connected* because the $\mathbb R$-factor is, and *compact* because $\mathbb R/\mathbb Z$ and
$\mathbb Z_2$ are compact and the quotient is proper.

**Finite layers.** The natural projection to the 2-adic coordinate induces, for each $n\ge 1$, a
surjective continuous homomorphism

$$\pi_n : \mathbb X \;\twoheadrightarrow\; \mathbb Z/2^n\mathbb Z ,\qquad (r, z) \bmod \Delta\mathbb Z \;\mapsto\; z \bmod 2^n .$$

The finite layer $L_n := \mathbb Z/2^n\mathbb Z$ has $2^n$ elements. Its (continuous, hence all) characters
are, for $a\in\{0,1,\dots,2^n-1\}$,

$$\chi_a(x) = e\!\left(\frac{a x}{2^n}\right),\qquad x\in L_n,$$

where $e(u)=\exp(2\pi i u)$. Thus $\widehat{L_n} \cong \mathbb Z/2^n\mathbb Z$ (canonically).

**The character group of the solenoid.** The continuous characters of $\mathbb X$ are indexed by the
dyadic rationals:

$$\widehat{\mathbb X} \;\cong\; \mathbb Z[1/2] \;=\; \{\, m/2^k : m\in\mathbb Z,\ k\ge 0\,\},$$

with the character $\chi_t\in\widehat{\mathbb X}$ given on a class $[r,z]$ by $\chi_t([r,z]) = e(t r)$
(well-defined precisely because $t$ is dyadic: if $[r,z]=[r',z']$ then $r-r'=n\in\mathbb Z$ and
$e(tn)=1$ for dyadic $t$).

**Status of these identifications.** The isomorphisms $\widehat{L_n}\cong\mathbb Z/2^n$ and
$\widehat{\mathbb X}\cong\mathbb Z[1/2]$ are **CLASSICAL** (Pontryagin duality for the solenoid; see e.g.
Hewitt–Ross, and the standard adelic/dyadic-solenoid description). They are stated here as the
*domain* of the theorem, not re-derived from scratch. What Atom 2 *proves locally* is the **correspondence
theorem** in §2, which is elementary and verified exactly.

---

## 2. THE THEOREM (finite ↔ global correspondence for the solenoid)

**Theorem (Atom 2, PROVED LOCAL).** For every $n\ge 1$ the restriction (dual of $\pi_n$)

$$\Phi_n : \widehat{\mathbb X} = \mathbb Z[1/2] \;\longrightarrow\; \widehat{L_n} = \mathbb Z/2^n\mathbb Z ,\qquad
t \;\longmapsto\; \bigl(x \mapsto e(t x)\bigr),\ \ x\in L_n,$$

is **surjective**. The family $\{\Phi_n\}_{n\ge 1}$ is **cofinal** and the induced map to the inverse limit

$$\Phi : \mathbb Z[1/2] \;\longrightarrow\; \varprojlim_n \widehat{L_n}, \qquad t \longmapsto (\Phi_n(t))_n,$$

is an **isomorphism** of abelian groups. Consequently every finite character of every layer lifts to a
unique global dyadic character, and two global dyadic characters are equal **iff** they agree at every
finite level.

**Proof.**
1. *Surjectivity at each level.* Given a finite character $\chi_a\in\widehat{L_n}$ ($a\in\mathbb Z/2^n$),
   choose the dyadic $t = a/2^n \in \mathbb Z[1/2]$. For $x\in L_n$,
   $\Phi_n(t)(x) = e(a x / 2^n) = \chi_a(x)$. Hence $\Phi_n(t) = \chi_a$. ∎
2. *Injectivity in the inverse limit.* Suppose $t, t'\in\mathbb Z[1/2]$ with $\Phi_n(t)=\Phi_n(t')$ for
   all $n$. For every $n$, the finite characters $\Phi_n(t)$ and $\Phi_n(t')$ coincide, i.e.
   $t-t' \equiv 0 \pmod{2^n}$ as an index in $\mathbb Z/2^n$ (since $e((t-t')x)=1$ for all
   $x\in\mathbb Z/2^n$ forces $t-t'\in 2^n\mathbb Z$). Thus
   $t-t' \in \bigcap_{n\ge 1} 2^n \mathbb Z = \{0\}$, so $t = t'$. ∎
3. *Cofinality.* The system of maps $\{\pi_n : \mathbb X\to L_n\}$ is cofinal (the tower $L_{n+1}\to L_n$
   is the reduction $\mathbb Z/2^{n+1}\to\mathbb Z/2^n$). By Pontryagin duality of the inverse limit,
   $\widehat{\varprojlim_n L_n} \cong \varinjlim_n \widehat{L_n} = \bigcup_n \frac{1}{2^n}\mathbb Z = \mathbb Z[1/2]$.
   The maps $\Phi_n$ are exactly the inclusions of this colimit, so $\Phi$ is the identity of
   $\mathbb Z[1/2]$. ∎

**Exact verification** (`atom2_dyadic_solenoid.py`, `Fraction`, no floats):
- *Surjectivity*: for $n=1,\dots,8$, every finite character $a\in\mathbb Z/2^n$ is reached as
  $\Phi_n(a/2^n)$; count of distinct images equals $2^n$ at every level.
- *Injectivity in the limit*: over all dyadics $t=m/2^K$ with $0\le m<2^K$ for $K=1,\dots,8$, the map
  $t\mapsto(\Phi_n(t))_{n\le K}$ is injective (distinct $t$ give distinct finite signatures).
- *Cofinality*: the union $\bigcup_{n\le 8}\frac{1}{2^n}\mathbb Z \cap [0,1)$ is nested and its size is
  exactly $2^8$ (the largest denominator reached), matching the inverse-limit index set.

---

## 3. Where the correspondence lives — and its exact boundary

The correspondence is a **structural isomorphism of observable data**: the finite characters of the
layers $\{L_n\}$ and the global dyadic characters $\mathbb Z[1/2]$ carry *the same* information, related
by restriction and lifting, with no loss. This is the precise finite↔global statement the atom was built
to make. It is **PROVED LOCAL** (elementary, and exactly checked), sitting on top of the **CLASSICAL**
Pontryagin identifications of the duals.

**Boundary (explicit, carried from Atom 1 and sharpened).**

- The theorem establishes an **isomorphism of observables** (character groups). It says *nothing* about
  any **equidistribution**, **normality**, or **ergodic** statement for any particular point such as $\pi$.
- In particular: surjectivity + injectivity-in-the-limit do **not** assert that $\pi$'s orbit is
  $\times 2$- (or $\times 3$-) invariant, nor that its digit sequence is normal. Those are *content*
  questions (measure-level invariance), and Yoneda / duality provides *structure*, not content — the
  exact LG7 caveat from the archive.
- The correspondence is over the **dyadic** dual $\mathbb Z[1/2]$ only. It does not extend, and is not
  claimed to extend, to the $\{2,3\}$-solenoid $X_{2,3}$ until Atom 3 treats the rank-2 dual
  $\mathbb Z[1/6]$ *separately*; even then the structural correspondence will be proved while the
  $\times 3$-invariance content remains open.
- **No claim** that any finite computation certifies an infinite statement: the exact checks below are
  finite witnesses for the finite-scope assertions (surjectivity up to $n=8$, injectivity up to $K=8$),
  while the *general* proof is the elementary algebra of §2.

**Status labels used.** `CLASSICAL` for the Pontryagin dual identifications; `PROVED LOCAL` for the
correspondence theorem (finite-scope elementary proof + exact finite check); `UNVERIFIED`/`OPEN` for
anything touching π-normality or ×3-invariance (explicitly *not* addressed here).

---

## 4. Position in the scale-up plan (from Atom 1 §4)

- **Atom 1** — $\mathbb Z_2$, dual $\mathbb Z[1/2]/\mathbb Z$ (torsion): closed, proved. ✓
- **Atom 2** (this note) — dyadic solenoid, dual $\mathbb Z[1/2]$ (torsion-free): **closed, proved**. ✓
- **Atom 3** — $\{2,3\}$-solenoid $X_{2,3}$, dual $\mathbb Z[1/6]$ (rank 2): the *same* correspondence is a
  proved isomorphism of observables, but the $\times 3$-invariance of π's orbit is exactly the content
  cell where duality stops being free.

The next cheapest step is Atom 3: state the rank-2 correspondence on $\mathbb Z[1/6]$ and verify the
surjectivity/cofinality/injectivity exactly, then *isolate* (not solve) the ×3-invariance content as a
single named condition.
