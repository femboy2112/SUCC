# RENORM transport: the exact ×16 Fourier renormalization of the original BBP source

**Date:** 2026-11-03. **Authority:** elementary paper derivation over the exact rational
source; a calibrated fixed-precision exponential-sum instrument; an independent odd-conductor
blind source. **No new Lean theorem, no original π-normality proof, no independent referee.**
**Parent:** the selected-current front (merged main `a673ec95…`), using its proved SC-6
numerator bound. **Immutable source:**

$$ r(n)=\frac{4}{8n-7}-\frac{2}{8n-4}-\frac{1}{8n-3}-\frac{1}{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n). $$

Write $x_n=\{U_n\}$, $e(t)=e^{2\pi i t}$, and the epoch exponential-sum coefficient

$$ c_A(h)=\frac1A\sum_{n=A}^{2A-1} e(h\,U_n),\qquad c_A(0)=1,\ |c_A(h)|\le 1. $$

The SC-8 sufficient target (merged) is $\sum_{1\le|h|\le q_A^2}|c_A(h)|^2=o(K_A)$,
$q_A=m_A/2\asymp\log A$, $K_A=\lfloor\log_{16}\log A\rfloor$. **OPEN.**

## RT-01 — exact renormalization identity (Demonstrated)

Since $U_n=16U_{n-1}+r(n)\pmod 1$, we have $e(hU_n)=e(16hU_{n-1})\,e(hr(n))$. Summing over
$n\in[A,2A)$ and writing $e(hr(n))=1+(e(hr(n))-1)$,

$$ A\,c_A(h)=\sum_{n=A}^{2A-1} e(16hU_{n-1})\;+\;\sum_{n=A}^{2A-1} e(16hU_{n-1})\big(e(hr(n))-1\big). $$

The first sum is $\sum_{n=A-1}^{2A-2}e(16hU_n)=A\,c_A(16h)+e(16hU_{A-1})-e(16hU_{2A-1})$. Hence

$$ \boxed{\,c_A(h)=c_A(16h)+\varepsilon_A(h)\,},\qquad
\varepsilon_A(h)=\frac{e(16hU_{A-1})-e(16hU_{2A-1})}{A}
+\frac1A\sum_{n=A}^{2A-1} e(16hU_{n-1})\big(e(hr(n))-1\big). \tag{RT-1}$$

This is exact for every integer $h$ and every $A\ge2$. It is the arithmetic ×16 self-similarity
of the digit source written at the level of Fourier coefficients; it is not an original Fourier
theory and claims no cancellation.

## RT-02 — rigorous error bound (Demonstrated)

**Boundary term.** Two unit phasors over $A$: $\;\big|A^{-1}(e(16hU_{A-1})-e(16hU_{2A-1}))\big|\le 2/A$.

**Forcing term.** $|e(hr(n))-1|=2|\sin(\pi h r(n))|\le 2\pi|h|\,r(n)$ (as $|\sin x|\le|x|$; here
$r(n)>0$). Thus $\big|A^{-1}\sum e(16hU_{n-1})(e(hr(n))-1)\big|\le \frac{2\pi|h|}{A}\sum_{n=A}^{2A-1}r(n)$.
By the merged selected-current result **SC-6**, $0<r(n)<\dfrac{15}{(8n-7)(8n-6)}<\dfrac{15}{(8n-7)^2}$, so

$$ \sum_{n=A}^{2A-1}r(n)<15\sum_{n\ge A}\frac1{(8n-7)^2}<15\int_{A-1}^{\infty}\frac{dx}{(8x-7)^2}=\frac{15}{8(8A-15)}\quad(A\ge2). $$

Combining,

$$ \boxed{\,|\varepsilon_A(h)|\le \frac2A+\frac{15\pi|h|}{4A(8A-15)}\,}\;=\;\frac2A+\frac{15\pi}{32}\frac{|h|}{A^2}\big(1+O(1/A)\big). \tag{RT-2}$$

**Receipt.** `FINITE_RECEIPT.json` reports, over preregistered held-out epochs
$A\in\{40,50,64,100,128,200,256\}$ and $h\in\{1,\dots,200\}$: **0 bound violations**, worst
$|\varepsilon_A(h)|/\text{bound}=0.9809$ (tight, non-vacuous), and the independent odd-conductor
source matching the zero-seed source to $0$. Calibration: $c_A(0)=1$ to full precision.

## RT-03 — the transport barrier RENORM-2 (Demonstrated structural / obstruction)

Iterating RT-1, for any $j\ge1$,

$$ c_A(h)=c_A(16^{\,j}h)+\sum_{i=0}^{j-1}\varepsilon_A(16^i h),\qquad
\Big|\sum_{i<j}\varepsilon_A(16^i h)\Big|\le \frac{2j}{A}+\frac{15\pi|h|}{4A}\sum_{i<j}\frac{16^i}{8\cdot16^iA-15}
\le \frac{2j}{A}+\frac{15\pi\,|h|\,16^{j}}{\,4\cdot 8\,A^2\,}\cdot\frac{1}{1}. $$

Choosing $j^\*=\lfloor \tfrac12\log_{16}(A^{3/2}/|h|)\rfloor$ keeps $16^{j^\*}|h|\le A^{3/2}$, so the
accumulated error is $O(\log A/A + A^{-1/2})=o(1)$ and

$$ |c_A(h)|=|c_A(16^{\,j^\*}h)|+o(1),\qquad |16^{\,j^\*}h|\asymp A^{3/2}. \tag{RT-3}$$

Because $h\mapsto16h$ is **injective** on $\mathbb Z$, the band $\{1\le|h|\le H\}$ is carried
bijectively onto a high band near $A^{3/2}$. Therefore any attempt to bound the SC-8 low-band
second moment $\sum_{|h|\le H}|c_A(h)|^2$ **using RT-1 alone** reduces it, up to the $o(1)$
budget, to an equal-cardinality **high-band** second moment: the recursion is
information-preserving and self-referential. It **cannot** by itself produce $o(K_A)$ smallness.
A genuine high-frequency equidistribution estimate — the OPEN input — is required.

The receipt's barrier sample ($A=256$) shows $|c_A(1)|,|c_A(16)|,|c_A(256)|\approx0.074,0.073,0.072$:
mass is **transported up the frequency ladder, not annihilated**. This refutes the shortcut
"iterate the ×16 relation until the coefficient is small."

## RT-04 — scope and relation to the open gate

RT-1/RT-2 are a *quantitative* statement of the digit self-similarity, with an explicit,
tight error whose constant is derived from the BBP source (via SC-6). They are, however,
**general**: the identity and the shape of the bound hold for any `U_n=16U_{n-1}+f(n)` with
small `f`, and RT-2 is **not** a source discriminator — scaled-forcing mutants `s·r(n)` (s=3,5)
also satisfy it (verified; see `VALIDATION.md`), because the triangle bound discards the forcing
sum's own cancellation. So this is structure, not a BBP-specific cancellation law. They do **not** bound $|c_A(h)|$ from above by anything
$<1$ at a fixed scale — DC-1 of the selected-phase forge already supplies the known $\log$-scale
*modulus* loss, and that is a modulus bound, not cancellation. RT-3 is a barrier on a specific
method. None of this is progress on $\sum_{|h|\le q_A^2}|c_A(h)|^2=o(K_A)$.

### Claim ledger

| Claim | Status | Earned authority | Unpaid debt |
|---|---|---|---|
| RT-01 identity | Demonstrated | exact algebra of $U_n=16U_{n-1}+r(n)$ | — |
| RT-02 bound | Demonstrated | triangle ineq + $|\sin x|\le|x|$ + merged SC-6 numerator bound; held-out receipt, 0 violations | — |
| RT-03 barrier | Demonstrated (method obstruction) | injectivity of ×16 + RT-2 telescoped | not a theorem about the *size* of $c_A$ |
| $\sum_{|h|\le q_A^2}|c_A(h)|^2=o(K_A)$ | **OPEN** | — | real high-frequency signed cancellation |
| π base-16 normality | **OPEN** | — | the above |

**π base-16 normality, the signed Weyl gate $S_N(h)=o(N)$, and RH are OPEN / not claimed.**
This uses established constructions; no original-priority claim.

### References
- Selected-current front SC-1..SC-8 (merged main), especially SC-6 numerator factorization
  `P(t)=(1-t)(t²+2)(t²+2t+2)`, `r(n)<15/((8n-7)(8n-6))`.
- Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions* (BBP ×16 orbit ↔ base-16 normality).
- Standard $|e(t)-1|=2|\sin\pi t|\le 2\pi|t|$.
