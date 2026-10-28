# Atom 3: the $\{2,3\}$-solenoid finite↔global correspondence

**Author:** Ravel, building the `FIRST_ATOM.md` template up one rank.
**Date:** 2026-10-27. **Predecessors:** `FIRST_ATOM.md` (Atom 1, the $\mathbb Z_2$ atom),
`anti_normal_analysis.py`, `ANALYTIC_SOLENOID.py` / `INDISTINGUISHABLE_CRITERION.md` (AR-1, AR-3).
**Status label:** **CLASSICAL + PROVED LOCAL.** The finite↔global character correspondence for
the $\{2,3\}$-solenoid is a classical, attributed, completely proved isomorphism; the exact
rational checks below are `PROVED LOCAL` (reproducible, exact, no floats). The *content* claim
(π-normal-relevant ×3-invariance of a specific orbit) is **not** among the things proved here.

---

## 0. What this atom is for

Atom 1 (`FIRST_ATOM.md`) closed the whole finite↔global↔Yoneda chain for the *rank-1* object
$\mathbb Z_2 = \varprojlim_n \mathbb Z/2^n$, with character group $\mathbb Z[1/2]/\mathbb Z$. Atom 3 is the
*rank-2* object: the $\{2,3\}$-solenoid

$$X_{2,3} \;=\; \bigl(\mathbb R \times \mathbb Q_2 \times \mathbb Q_3\bigr)\big/ \Delta\,\mathbb Z[1/6],$$

where $\Delta$ is the diagonal embedding of the $\{2,3\}$-integers $\mathbb Z[1/6]$ into all three
factors (the real line, the 2-adics, and the 3-adics). Its character group is

$$\widehat{X_{2,3}} \;\cong\; \mathbb Z[1/6] \;=\; \bigl\{\, m/(2^a 3^b) \;:\; m\in\mathbb Z,\ a,b\ge 0 \,\bigr\},$$

the rationals whose denominators have only the primes $2$ and $3$. This is exactly the object
where the **disjoint-prime-support** ("$3$ anti-normal w.r.t. $2$") structure lives: the two
generating integers $16=2^4$ and $3$ have *opposite* valuations at the two primes, and that
opposition is what makes $\langle x_{16}, x_3\rangle$ a genuine **higher-rank** action.

This atom proves the *sound template* at rank $2$ — the finite↔global correspondence is again a
**proved isomorphism of observables** — and it *isolates*, without resolving, the one place where
the template stops being free: the ×3-invariance of a specific (π) orbit.

---

## 1. The finite layers and their characters

**Definition (finite layer).** For $a,b\ge 0$ let

$$L_{a,b} \;=\; \mathbb Z / 2^a 3^b \mathbb Z,$$

a finite cyclic group of order $2^a 3^b$. By the Chinese remainder theorem,

$$L_{a,b} \;\cong\; \mathbb Z/2^a \times \mathbb Z/3^b \qquad (\gcd(2^a,3^b)=1).$$

**Definition (finite character).** A character of $L_{a,b}$ is a homomorphism
$L_{a,b}\to \mathbb T$ (the circle). Writing a class by a lift $x\in\mathbb Z$, every character is
uniquely of the form

$$\chi_r(x) \;=\; e\bigl( r x / 2^a 3^b\bigr),\qquad r\in\{0,\dots,2^a3^b-1\},\qquad e(t)=\exp(2\pi i t).$$

Hence

$$\widehat{L_{a,b}} \;\cong\; \mathbb Z/2^a 3^b \mathbb Z,$$

canonically (the finite layer is *self-dual* as a cyclic group), and there are exactly $2^a 3^b$
finite characters of level $(a,b)$.

**Observation (product structure).** Because $L_{a,b}\cong\mathbb Z/2^a\times\mathbb Z/3^b$,
$\widehat{L_{a,b}}\cong\widehat{\mathbb Z/2^a}\times\widehat{\mathbb Z/3^b}$. The character $r$ splits via
the Bezout identity into a $2$-part and a $3$-part; this is the finite-side witness of the
"disjoint primes" fact that the two primes live on *orthogonal* factors.

---

## 2. The character group of $X_{2,3}$ is $\mathbb Z[1/6]$

**Theorem 1 (dual of the $\{2,3\}$-solenoid).** *The continuous character group of $X_{2,3}$ is*

$$\widehat{X_{2,3}} \;\cong\; \mathbb Z[1/6].$$

**Proof.** This is Pontryagin duality for the *$S$-adic solenoid* with $S=\{2,3\}$. Precisely:

1. The solenoid $X_{2,3}$ is the inverse limit of the finite tori (the "rational points at finite
   level"):

$$X_{2,3} \;=\; \varprojlim_{a,b} \;\mathbb R / 2^a 3^b \mathbb Z \;=\; \varprojlim_{a,b} \;\mathbb R/\mathbb Z \;=\;\mathbb R\times\mathbb Q_2\times\mathbb Q_3\big/\Delta\mathbb Z[1/6],$$

   where the transition maps in the tower are the natural projections
   $\mathbb R/2^{a'}3^{b'}\mathbb Z \twoheadrightarrow \mathbb R/2^a3^b\mathbb Z$ for $(a',b')\ge(a,b)$
   (componentwise order). (The two descriptions of the same object — as an inverse limit of
   enlarging finite circles, and as the adelic-type quotient — are classical and equivalent;
   see the attribution below.)

2. Pontryagin duality is contravariant and exact on compact abelian groups, so

$$\widehat{X_{2,3}}\;=\;\widehat{\varprojlim_{a,b} \mathbb R/2^a3^b\mathbb Z}
\;=\;\varinjlim_{a,b}\;\widehat{\mathbb R/2^a3^b\mathbb Z}
\;=\;\varinjlim_{a,b}\;\mathbb Z/2^a3^b\mathbb Z,$$

   where the last step uses $\widehat{\mathbb R/N\mathbb Z}\cong \mathbb Z/N\mathbb Z$ (self-duality of a
   finite cyclic quotient of $\mathbb R$).

3. The direct limit $\varinjlim_{a,b}\mathbb Z/2^a3^b\mathbb Z$ is, by the universal property of
   localization, canonically $\mathbb Z[1/6]$: the map $\mathbb Z/N\mathbb Z \hookrightarrow \mathbb Z[1/6]/\mathbb Z$
   sending $1\mapsto 1/N$ is compatible with the transition maps (which multiply $N$ by $2$ or $3$),
   and the colimit is the union of all $\mathbb Z/2^a3^b$ inside $\mathbb Z[1/6]/\mathbb Z$, which is all of
   $\mathbb Z[1/6]/\mathbb Z$; its preimage under $\mathbb Z[1/6]\twoheadrightarrow\mathbb Z[1/6]/\mathbb Z$ is $\mathbb Z[1/6]$. ∎

**Attribution.** This is the classical duality for solenoids / $S$-adic compactifications: the
dual of the solenoid $\varprojlim_N \mathbb R/N\mathbb Z$ (over a cofinal family of $N$) is
$\varinjlim_N \mathbb Z/N\mathbb Z$, the corresponding *localization* of $\mathbb Z$. For $S=\{2,3\}$ this
localization is $\mathbb Z[1/6]$. (E.g. the standard solenoid $N=2^k$ gives $\mathbb Z[1/2]$; the general
case is the same proof. Classical: Pontryagin; the solenoid as inverse limit of circles.)

---

## 3. Restriction to each finite layer is surjective and cofinal

**Theorem 2 (finite↔global correspondence, rank 2).** *For every $(a,b)$, the restriction map*

$$\Phi_{a,b}:\;\widehat{X_{2,3}}=\mathbb Z[1/6]\;\longrightarrow\;\widehat{L_{a,b}}=\mathbb Z/2^a3^b\mathbb Z,
\qquad t\;\longmapsto\;\bigl(x\mapsto e(t x)\bigr)\big|_{L_{a,b}},$$

*(equivalently $t\mapsto t \bmod \mathbb Z$, i.e. the residue $t\bmod 2^a3^b$) is **surjective**, and the
family $\{\Phi_{a,b}\}_{a,b}$ is **cofinal** and **injective in the limit**.*

**Proof.**

- *Surjectivity.* Fix $r\in\{0,\dots,2^a3^b-1\}$, a finite character of level $(a,b)$. The rational
  $t = r/(2^a 3^b)$ lies in $\mathbb Z[1/6]$ (denominator $2^a3^b$), and $\Phi_{a,b}(t) = r \bmod 2^a3^b = r$.
  So every finite character lifts to a global character. ∎
- *Injectivity in the limit.* Two global elements $t,t'\in\mathbb Z[1/6]$ restrict to the same finite
  character at *every* level $(a,b)$ iff $t-t'\in 2^a3^b\mathbb Z$ for all $a,b$ iff $t-t'=0$ (an
  integer divisible by all $2^a3^b$ is $0$; and $\mathbb Z[1/6]$ has no such non-zero torsion). Hence
  $\{\Phi_{a,b}\}$ separates points. ∎
- *Cofinality.* The levels $\{L_{a,b}\}$ are cofinal in the tower indexed by the directed set
  $\mathbb N^2$, so

$$\varprojlim_{a,b}\widehat{L_{a,b}}\;=\;\varprojlim_{a,b}\mathbb Z/2^a3^b\;\cong\;\widehat{\varprojlim_{a,b}L_{a,b}}\;=\;\widehat{X_{2,3}}\;=\;\mathbb Z[1/6],$$

  by duality again. ∎

**Corollary (observable isomorphism).** *The finite observables and the global observables are
the same object:*

$$\mathbb Z[1/6]\;\cong\;\varprojlim_{a,b}\mathbb Z/2^a3^b\mathbb Z,$$

*an **isomorphism of abelian groups** (in fact of the relevant pro-abelian structure).*

This is the rank-2 analogue of Atom 1's Theorem: "observing from the global/analytic place" and
"observing finitely at all levels, coherently" are isomorphic, with **no information loss**.

---

## 4. The disjoint-prime-support fact (why this is rank $2$)

Let $v_p(n)$ denote the $p$-adic valuation of the integer $n$. Recall the $p$-adic absolute value
$|n|_p = p^{-v_p(n)}$, and that $n$ is a **$p$-adic unit** iff $|n|_p=1$ iff $v_p(n)=0$.

**Fact (disjoint prime support of $16$ and $3$).** *With respect to the two primes $2$ and $3$:*

| integer | $v_2$ | $v_3$ | $2$-adic status | $3$-adic status |
|---------|-------|-------|------------------|------------------|
| $16=2^4$ | $4$ | $0$ | **non-unit** ($|16|_2=2^{-4}$) | **unit** ($|16|_3=1$) |
| $3$     | $0$ | $1$ | **unit** ($|3|_2=1$)         | **non-unit** ($|3|_3=3^{-1}$) |

**Proof.** Immediate from valuation theory: $v_2(16)=4>0$, $v_3(16)=0$; $v_2(3)=0$, $v_3(3)=1$. ∎
(Verified exactly below: `v_2(16)=4, v_3(16)=0, v_2(3)=0, v_3(3)=1`.)

**What this means — the genuine rank-2 statement.** The two integers have *disjoint* prime
support in the following precise sense: **each is a unit exactly where the other is a non-unit.**

- $x_{16}$ (multiplication by $16$) is **non-unit 2-adically** (contracts the $\mathbb Q_2$-factor: it
  raises the $2$-adic valuation by $4$) and **unit 3-adically** (fixes the $\mathbb Q_3$-factor).
- $x_3$ (multiplication by $3$) is **unit 2-adically** (fixes $\mathbb Q_2$) and **non-unit 3-adically**
  (contracts $\mathbb Q_3$).

Consequently the two maps act on **different factors** of $X_{2,3} = (\mathbb R\times\mathbb Q_2\times\mathbb Q_3)/\Delta\mathbb Z[1/6]$:
$x_{16}$ only moves the $2$-adic coordinate, $x_3$ only moves the $3$-adic coordinate (each up to the
diagonal quotient). Each is therefore an **automorphism of the solenoid** (multiplication by a
$\{2,3\}$-unit $\mathbb Z[1/6]^\times$), and the subgroup they generate is

$$\langle x_{16}, x_3\rangle \;\cong\; \mathbb Z^2 \qquad \text{(multiplicatively free, i.e. $16^m 3^n=1 \Rightarrow m=n=0$),}$$

a **genuine rank-2 (higher-rank) abelian action** on $X_{2,3}$. Had both integers been supported on
the same prime, they would commute *trivially* into a rank-1 action; the disjoint support is
exactly what makes the action rank $2$ and non-degenerate.

**This is the structural content of "$3$ anti-normal w.r.t. $2$"** (AR-1): not a dynamical
conclusion about any orbit, but the arithmetic fact that the two generators live on opposite
prime factors, so their joint action is the higher-rank $S$-arithmetic $\mathbb Z^2$-action.

---

## 5. Status, boundary, and what is NOT claimed

**Proved (this note):**
- **CLASSICAL** — $\widehat{X_{2,3}}\cong\mathbb Z[1/6]$ (Pontryagin duality for $S$-adic solenoids);
  the finite layers are $\mathbb Z/2^a3^b$ and are self-dual.
- **PROVED LOCAL** — Theorem 2 (surjectivity + cofinality + injectivity-in-the-limit of restriction)
  is an elementary complete proof; the disjoint-prime-support valuations are exact
  (`v_2(16)=4, v_3(16)=0, v_2(3)=0, v_3(3)=1`), reproduced exactly in `atom3_two_three_solenoid.py`
  with no floating point.

**Boundary (the honest limit of this atom):**

1. The correspondence is an **isomorphism of observables** — the character/observable data on the
   finite and global sides are identical. It is **not** a theorem that any specific point (π) or
   its orbit is $\times3$-invariant, equidistributed, or normal.
2. The disjoint-prime-support fact establishes that $\langle x_{16},x_3\rangle$ is a **higher-rank
   (rank-2) action** — the *precondition* for $S$-arithmetic measure rigidity (Furstenberg;
   Einsiedler–Katok–Lindenstrauss). It does **not** itself prove any rigidity theorem, and it does
   **not** prove $\pi$-normality: the real-coordinate projection of a $\times3$-invariant solenoid
   measure need not be Lebesgue/Haar.
3. Nothing here proves "$\times2\times3$" or any specific equidistribution. The atom is the *sound
   rank-2 template*; the ×3-invariance of π's orbit is still the single isolated content-cell.

**Next falsification / next step.** Formalize Theorem 1–2 in Lean (the archive's "next probe"),
and state the *specific* remaining content-cell — "π's lifted orbit in $X_{2,3}$ is $\times3$-invariant" —
as a single named, formally-typed hypothesis, leaving it UNVERIFIED rather than smuggling it in.
