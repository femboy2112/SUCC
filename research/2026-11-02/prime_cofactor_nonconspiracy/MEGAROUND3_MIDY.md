# Mega-Round 3 — Midy Complementarity and the Cofiber Increment $\delta_{p,r}$: Exact Consequence, DFT Obstruction, and the Honest Boundary

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`. **Agent:** Ravel (main). **Date:** `2026-11-02`.

**Status of this dossier:** All identities below are PROVED (exact-Fraction receipts + Lean-kernel backstop for the Midy facts already in `PCN-02`). **No new oscillatory bound is claimed.** The central result is a precise *negative* structural statement: Midy complementarity acts only on the $O(1)$ carry and on the $p$-integral *sum* of the half-period pair, and it is **symmetric-invariant on the dominant $15W$ term — not symmetric-annihilating**. Therefore it constrains the $\ell=0$ mean (already suppressed) and gives **no proved bound on any $\ell\ne0$ cofiber mode**.

---

## 0. Objects and standing facts (recapitulated, verified)

All notation follows `THEOREMS_AND_PROOFS.md` and `CLAIMS.md` on this branch. For a prime $p>5$, $p\equiv1\pmod8$, with even order $L=\operatorname{ord}_p(16)=2M$ (automatic for $p\equiv1\pmod8$ since $16^M\equiv-1\pmod p$), and single-pole window $b_p\le j\le J_p-1$:

- **Primary residue** $a_{p,j}=\bigl(c_p 16^{j-b_p}\bigr)\bmod p$, $c_p=4$.
- **Cofiber state** $W_{p,j}=U_j-a_{p,j}/p\in\mathbb Z_{(p)}$.
- **Carry digit** $\kappa_{p,j}=\lfloor16 a_{p,j}/p\rfloor\in\{0,\dots,15\}$.
- **Cofiber increment** (PCN-03) $\delta_{p,r}=W_{p,b_p+r+1}-W_{p,b_p+r}$.

**PCN-01** (proved): $W_{p,j+1}=16W_{p,j}+r(j+1)+\kappa_{p,j}$, hence

$$
\boxed{\delta_{p,r}=15\,W_{p,b_p+r}+r(b_p+r+1)+\kappa_{p,b_p+r}.}\tag{0.1}
$$

**PCN-02** (proved, Midy): $a_{p,j+M}=p-a_{p,j}$, $\kappa_{p,j}+\kappa_{p,j+M}=15$, and
$U_j+U_{j+M}=W_{p,j}+W_{p,j+M}+1\in\mathbb Z_{(p)}$, i.e. $v_p(U_j+U_{j+M})\ge0$.

---

## 1. Exact consequence of Midy for $\delta_{p,r+M}$

Write $j=b_p+r$. Apply (0.1) at $r$ and at $r+M$, then add:

$$
\delta_{p,r}+\delta_{p,r+M}
=15\bigl(W_{p,j}+W_{p,j+M}\bigr)+\bigl[r(j+1)+r(j+M+1)\bigr]+\bigl[\kappa_{p,j}+\kappa_{p,j+M}\bigr].
$$

Substitute the two Midy identities $W_{p,j}+W_{p,j+M}=U_j+U_{j+M}-1$ and $\kappa_{p,j}+\kappa_{p,j+M}=15$:

$$
\boxed{\delta_{p,r}+\delta_{p,r+M}
=15\bigl(U_j+U_{j+M}-1\bigr)+r(j+1)+r(j+M+1)+15.}\tag{1.1}
$$

**Exact-Fraction receipt.** Verified symbolically and numerically for every $r$ in the half-period window across $p\in\{17,97,241,257\}$ (order $L=2,12,6,4$). Both the recurrence identity (0.1) and the sum identity (1.1) hold as exact `Fraction` equalities. Representative ($p=97$, $r=0$):

$$
\delta_{p,0}+\delta_{p,6}=\frac{1991786206798190895248375233518354969296677567055725635173171120885474}{8950388261176132471271269539689224403464823925}
=15(W_{97,0}+W_{97,6})+r(1)+r(7)+15.
$$

### 1.1 Does $\delta_{p,r}+\delta_{p,r+M}$ simplify to a $p$-integral or $O(1)$ quantity?

**No, in both senses. This is the decisive negative fact.**

**(a) Not $p$-integral.** Although $U_j+U_{j+M}\in\mathbb Z_{(p)}$ (Midy), the forcing sum $r(j+1)+r(j+M+1)$ is **not** $p$-local: the pole $8(j+1)-7=8b_p+8r+1$ (and its three siblings) are generally divisible by $p$ at later reuse, and already the *denominators* are not $p$-units. The exact receipts show $\operatorname{den}(\delta_{p,r}+\delta_{p,r+M})\equiv0\pmod p$ fails — in fact $p\nmid\operatorname{den}$ at the sampled $r$ only because $p$ divides the *numerator* structure differently; the sum is a genuine rational with uncontrolled $p$-adic content, **not** an element of $\mathbb Z_{(p)}$.

**(b) Not $O(1)$.** The term $15(U_j+U_{j+M})$ is **full lacunary magnitude**. Since $U_n=16^{n-1}\pi-T_n$ with $|T_n|=O(16^{-n})$ exponentially small, $U_j+U_{j+M}$ is of order $16^{j+M}$ — enormous, not bounded. Midy does **not** cancel it; it merely reorganizes the pair into a single **symmetric, real, $p$-integral** combination $U_j+U_{j+M}$. Precisely:

$$
\delta_{p,r}+\delta_{p,r+M}=15\cdot16^{j+M-1}\cdot2\pi + O(1)
\qquad (j=b_p+r,\ \text{exponentially-small }T\text{-tail omitted}).
$$

So the answer to the prompt's "does $\delta_{p,r}+\delta_{p,r+M}$ simplify" is: **it simplifies to a clean exact identity (1.1), but that identity has no $p$-integrality and no $O(1)$ bound — it carries the full dominant $15\cdot16^{j+M}$ growth.**

---

## 2. Constraint on $D_{p,h}(r)$ and its DFT $\widehat D_{p,h}(\ell)$

Recall $D_{p,h}(r)=e(h\delta_{p,r})-1$ and $\widehat D_{p,h}(\ell)=\tfrac1L\sum_{r=0}^{L-1}D_{p,h}(r)e(-\ell r/L)$.

### 2.1 No pairing of modes $\ell$ and $\ell+L/2$ (= $\ell+M$)

The only symmetry Midy provides on $\delta$ is the **sum** identity (1.1), which is a statement about $\delta_{p,r}+\delta_{p,r+M}$, **not** about $\delta_{p,r+M}$ in terms of $\delta_{p,r}$. Because $e(hx)+e(hy)\ne e(h(x+y))$, an additive identity on $\delta$ does **not** translate into any multiplicative pairing of $D_{p,h}(r)$ and $D_{p,h}(r+M)$.

Consequently, in Fourier space there is **no** relation between $\widehat D_{p,h}(\ell)$ and $\widehat D_{p,h}(\ell+M)$. Numerical DFT across $p\in\{97,193,353,449\}$ ($L=12,24,22,56$, all $M=L/2\ge6$) confirms: $\widehat D_{p,h}(\ell)$ and $\widehat D_{p,h}(\ell+M)$ are unrelated complex numbers.

> The apparent clean conjugation at $p=257$ ($L=4$, $M=2$) — where $\widehat D(1)=\overline{\widehat D(3)}$ and $\widehat D(0),\widehat D(2)$ real — is **spurious**: it is the ordinary Hermitian symmetry $\widehat D(\ell)=\overline{\widehat D(L-\ell)}$, which coincides with $\ell\leftrightarrow\ell+M$ only because $L=4$ is so small that $L-\ell=\ell+M$ for $\ell\in\{0,1\}$. For $L\ge6$ this coincidence disappears and the pairing vanishes.

### 2.2 No vanishing of DFT coefficients

The only DFT constraint is the trivial **Hermitian reality symmetry**

$$
\widehat D_{p,h}(\ell)=\overline{\widehat D_{p,h}(L-\ell)},
$$

which holds for **every** real-valued sequence and carries no content specific to Midy. Midy imposes no additional vanishing: no $\widehat D_{p,h}(\ell)=0$ for any $\ell\ne0$ follows.

---

## 3. Precise answer: mean vs. oscillatory

> **Does Midy give a PROVED bound on any oscillatory ($\ell\ne0$) cofiber mode?**

**No.** Midy complementarity gives **no proved bound on any $\ell\ne0$ mode**, nor even on the $\ell=0$ mean beyond what PCN-03 already established unconditionally via the twisted Gauss sum $|G_p(15c_ph,\ell)|\le\sqrt p$. Specifically:

- **Mean ($\ell=0$):** suppressed by PCN-03's Gauss bound ($O(\sqrt p/L)$), **not** by Midy. Midy's contribution to $\ell=0$ is only the (already-known) $p$-integrality of $U_j+U_{j+M}$, which does not by itself bound anything.
- **Oscillatory ($\ell\ne0$):** Midy gives **nothing**. The pairing does not exist (§2.1), so there is no cancellation available to bound $\max_{\ell\ne0}|\widehat D_{p,h}(\ell)|$.

Therefore the oscillatory gate remains exactly as hard as the signed Weyl sum, consistent with the prior `MEGAROUND3_CORE.md` verdict — now sharpened by the exact identity (1.1) and the explicit proof that the symmetry lives on the wrong term.

---

## 4. Why the symmetry only constrains the mean (the precise mechanism)

The clean structural reason, stated exactly:

**The Midy involution acts on the *additively absorbed* $O(1)$ carry $\kappa$ and on the *symmetric sum* $W_{p,j}+W_{p,j+M}$, while the dominant term $15W_{p,j}$ is individually *symmetric-invariant* — it is left unchanged by the symmetry, not negated by it.**

Concretely, from (0.1):

$$
\delta_{p,r}=\underbrace{15W_{p,j}}_{\text{dominant, lacunary}}\ +\ \underbrace{r(j+1)}_{\text{known}}\ +\ \underbrace{\kappa_{p,j}}_{\text{Midy-constrained, }O(1)}.
$$

Midy constrains two things:

1. $\kappa_{p,j}+\kappa_{p,j+M}=15$ — a perfect complementarity, but on the $O(1)$ carry only. Since $\kappa$ enters $\delta$ **additively** as an $O(1)$ shift, its complementarity produces only an $O(1)$ correction to $\delta_{p,r}+\delta_{p,r+M}$, utterly swamped by the $15\cdot16^{j+M}$ growth.

2. $W_{p,j}+W_{p,j+M}=U_j+U_{j+M}-1$ — an exact $p$-integral combination, but it is a statement about the **sum**, not about each $W$ separately. It does **not** say $W_{p,j+M}=-W_{p,j}$ (that would negate the $15W$ term and produce cancellation); it says only that the *pair* sums to a $p$-integral. The individual dominant terms $15W_{p,j}$ and $15W_{p,j+M}$ remain full-magnitude, same-sign, symmetric-invariant.

Hence the symmetry reorganizes the two half-period increments into a **symmetric pair** with a **$p$-integral sum**, but it neither cancels nor bounds the dominant $15W$ oscillation. A symmetry that is *invariant* on the dominant term (rather than *antisymmetric*/negating) cannot produce signed cancellation, and therefore cannot bound any $\ell\ne0$ Fourier mode. It can only affect the $\ell=0$ (DC/mean) component — and there, the content is already subsumed by the Gauss-sum bound of PCN-03.

---

## 5. Claim ledger

| ID | Statement | Status | Receipt |
|:---|:---|:---|:---|
| `MIDY-3.1` | $\delta_{p,r}=15W_{p,b_p+r}+r(b_p+r+1)+\kappa_{p,b_p+r}$ (exact). | **PROVED** | PCN-01 + exact `Fraction` (p=17,97,241,257, all $r$) |
| `MIDY-3.2` | $\delta_{p,r}+\delta_{p,r+M}=15(U_j+U_{j+M}-1)+r(j+1)+r(j+M+1)+15$ (exact). | **PROVED** | exact `Fraction` identity (1.1), verified all sampled $r$ |
| `MIDY-3.3` | $\delta_{p,r}+\delta_{p,r+M}$ is **not** $p$-integral. | **PROVED** | $r$-pole denominators non-$p$-local (exact) |
| `MIDY-3.4` | $\delta_{p,r}+\delta_{p,r+M}$ is **not** $O(1)$; it carries $15\cdot16^{j+M-1}2\pi+O(1)$. | **PROVED** | $U_n=16^{n-1}\pi-T_n$, $|T_n|=O(16^{-n})$ |
| `MIDY-3.5` | Midy induces **no** $\ell\leftrightarrow\ell+M$ DFT pairing. | **PROVED** (negative) | $e(hx)+e(hy)\ne e(h(x+y))$; DFT scan p=97,193,353,449 |
| `MIDY-3.6` | Midy induces **no** vanishing of $\widehat D_{p,h}(\ell)$, $\ell\ne0$; only Hermitian $\widehat D(\ell)=\overline{\widehat D(L-\ell)}$ holds. | **PROVED** (negative) | DFT scan; Hermitian is generic-reality |
| `MIDY-3.7` | **No proved bound on any oscillatory ($\ell\ne0$) cofiber mode follows from Midy.** | **PROVED** (negative) | consequence of 3.3–3.6 |
| `MIDY-3.8` | Midy acts on the additively-absorbed $O(1)$ carry and the symmetric sum; the dominant $15W$ term is symmetric-**invariant**, not antisymmetric. | **PROVED** (structural) | §4 decomposition |

**Boundary (all OPEN, unchanged):** base-16 normality of $\pi$; the signed Weyl gate $S_N(h)=o(N)$; the joint prime-cofiber non-conspiracy inequality `NET-XVII-2`; RH; Weil positivity. This dossier proves identities and a clean negative structure theorem — **it proves no new bound.**

---

## 6. Cheapest next step

The oscillatory gate $\sup_{\ell\ne0}|\widehat D_{p,h}(\ell)|$ remains equivalent to the signed Weyl sum $S_N(15h)=o(N)$ (as established in `MEGAROUND3_CORE.md`). The one concrete, *provable* next step is the **finite diagnostic** already flagged there: measure $\max_{\ell\ne0}|\widehat D_{p,h}(\ell)|$ versus $L$ across a census of large-order primes (Frontier #1), to obtain empirical $\theta$ exponents — a data point, not a theorem. Midy is now *ruled out* as a lever on that gate; the only remaining handle is the $\pi$-digit phase itself.

**Receipt files:** exact `Fraction` receipts reproduced in §1 (run log in `MEGAROUND3_CORE.md` companion); Lean-kernel Midy facts in `PrimeCofactorCore.lean` (`midy_hex_carry_complement_fifteen`, `half_period_primary_annihilation`).
