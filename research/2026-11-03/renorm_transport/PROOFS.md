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

## RT-00 — the sufficiency chain is one-directional (P0-A correction)

The merged selected-current front proves, with all terms nonnegative,
$$\text{(SC-8)}\quad J_{A,q}\le 1+\sum_{1\le|h|\le H}|c_A(h)|^2+\tfrac{2}{\pi^2},\qquad
\text{(SC-3)}\quad E_{A,m}(0)\le 4J_{A,m/2},$$
and SUCC #476 gives $E_{A,m_A}=o(\log m_A)\Rightarrow$ base-16 normality. Hence the **sufficiency chain**
$$\boxed{\ \textstyle\sum_{1\le|h|\le q_A^2}|c_A(h)|^2=o(K_A)\ \Longrightarrow\ J_{A,q_A}=o(K_A)\ \Longrightarrow\ E_{A,m_A}=o(\log m_A)\ \Longrightarrow\ \pi\text{ base-16 normal}\ }$$
is **one-directional**. Separately, the proved #293/SGO-09 bounded Green-tail transport
$\big|\sum_{n\le N}e(h\,16^{\,n-1}\pi)-\sum_{n\le N}e(hU_n)\big|<\tfrac{119}{648}|h|$ gives the genuine
$$\boxed{\ \pi\text{ base-16 normal}\ \Longleftrightarrow\ S_N(h)=\textstyle\sum_{n\le N}e(hU_n)=o(N)\ \ \forall\,h\ne 0.\ }$$

**The only $\Longleftrightarrow$ is the last one.** Earlier integration summaries that wrote
"$\sum|c_A|^2=o(K_A)$ *equivalently* $J=o(K_A)$ *equivalently* $S_N=o(N)$" overclaimed: `band`$\Rightarrow$`J`
and `J`$\Rightarrow E\Rightarrow$`normal` are not reversible as stated. The generic converse
$J=o(K)\Rightarrow\sum_{|h|\le q^2}|c_A(h)|^2=o(K)$ is **false**: for the equally-spaced cloud
$x_j=j/q$ one has $c(h)=\mathbf 1_{q\mid h}$, so $\mathrm{sinc}^2(\pi h/q)=0$ at every nonzero
multiple of $q$ and (SC-2) gives $J_q=1$, while the **unweighted** band
$\sum_{1\le|h|\le q^2}|c(h)|^2=2q\to\infty$. The $\mathrm{sinc}^2$ weight annihilates exactly the
frequencies carrying this cloud's mass; the unweighted SC-8 band is **strictly stronger** than $J$.
(`band_vs_J_cloud`, `test_D0_band_to_J_converse_is_false`.) This disproves the *universal* converse,
not a hypothetical BBP-specific one — so SC-8 stays a genuine (strictly sufficient) target, not an
equivalent restatement of $J$.

*(Kernel convention.* The $J$ instrument uses the physical tent $k_q(d)=(1-q\|d\|)_+$, whose
frequency weight is $\mathrm{sinc}^2(\pi h/q)$ — the triangle function transforms to $\mathrm{sinc}^2$,
matching SC-2, which is the identity used above. Both $\mathrm{sinc}^2(\pi h/q)$ and the Fejér weight
$(1-|h|/q)_+$ vanish at every nonzero multiple of $q$, so $J_q=1$ holds under either convention and
the counterexample is robust to it; verified exactly for $q=4,8,16,32$.)*

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
$A\in\{40,50,64,100,128,200,256\}$ and the frequency grid
$h\in\mathrm{HELDOUT\_H}=\{1,2,3,5,8,13,21,50,100,200\}$: **0 bound violations**, grid-worst
$|\varepsilon_A(h)|/\text{bound}=0.9809$ (tight, non-vacuous), and the independent odd-conductor
source matching the zero-seed source to $0$. Calibration: $c_A(0)=1$ to full precision. An
independent referee confirmed **0 violations over the full $h=1,\dots,200$** (worst ratio
$\approx0.9876$ at the untested $h=4$) and over $A=2,\dots,40$ with $|h|\le5000$ — so the *grid* is a
sample, but the proved inequality holds beyond it.

## RT-03 — the transport barrier RENORM-2 (Demonstrated structural / obstruction)

**Corrected 2026-11-03.** The first draft (i) used a per-frequency depth
$j^\*(h)=\lfloor\tfrac12\log_{16}(A^{3/2}/|h|)\rfloor$ that reaches only
$16^{j^\*}|h|\asymp A^{3/4}\sqrt{|h|}$, **not** $A^{3/2}$ — the leading $\tfrac12$ is wrong (D1);
(ii) called $h\mapsto16^{j^\*(h)}h$ a **bijection**, but a frequency-dependent depth is **not
injective** (at $A=16^8$, $h=1$ and $h=16$ both map to $16^6$) (D2); and (iii) wrote the
accumulated-error denominator as $8\cdot16^iA-15$, which is frequency-dependent, stays linear in
$j$, and masks the true geometric growth (D3). All three are locked by `test_D1/D2/D3`. The
corrected barrier uses a **common depth** across the whole band.

**Accumulation (correct).** Iterating RT-1 at a single depth $j$, with the frequency at step $i$
equal to $16^i h$ and the denominator $8A-15$ depending only on $A$:

$$ c_A(h)=c_A(16^{\,j}h)+\sum_{i=0}^{j-1}\varepsilon_A(16^i h),\qquad
\Big|\sum_{i=0}^{j-1}\varepsilon_A(16^i h)\Big|
\le \frac{2j}{A}+\frac{15\pi|h|}{4A(8A-15)}\sum_{i=0}^{j-1}16^{\,i}
=\boxed{\frac{2j}{A}+\frac{\pi|h|\,(16^{\,j}-1)}{4A(8A-15)}}, \tag{RT-3a}$$

using $\sum_{i<j}16^i=(16^j-1)/15$ (the $15$ cancels). Held-out true error $\le$ this bound, **0
violations**; grid-worst ratio $0.923$ (receipt grid $h\in\{1,3\},\,j\le3$), $\approx0.94$ over a
wider grid ($h\in\{1,2,3,5,13\},\,j\le5$) — tight, non-vacuous either way (`acc_error_bound`, `test_D3`).

**Common-depth barrier.** Fix the band $\{1\le|h|\le H\}$ and the single depth
$j=\lfloor\log_{16}(A^{3/2}/H)\rfloor$, so $16^{\,j}|h|\le A^{3/2}$ for every $|h|\le H$. Then

- $h\mapsto16^{\,j}h$ is multiplication by a fixed nonzero integer, hence **injective**: the band
  maps to $H$ (with signs $2H$) **distinct** high frequencies, all $\le A^{3/2}$ (`test_D2`);
- by (RT-3a) the transport error is $\le \dfrac{2j}{A}+\dfrac{\pi A^{3/2}}{4A(8A-15)}
  =O\!\big(\tfrac{\log A}{A}\big)+O(A^{-1/2})=o(1)$ **uniformly** over the band — and any
  $16^jH=o(A^2)$ keeps it $o(1)$, so $A^{3/2}$ is a safe instance, not a ceiling;
- hence $|c_A(h)|=|c_A(16^{\,j}h)|+o(1)$ for each $|h|\le H$, onto distinct targets.

$$\boxed{\ \text{Common-depth }\times16\text{ transport relocates the low band onto an
equal-cardinality high band }(\le A^{3/2}),\ \text{each modulus preserved up to }o(1).\ } \tag{RT-3}$$

**Why this is a barrier.** Proving $\sum_{1\le|h|\le H}|c_A(h)|^2=o(K_A)$ by iterating RT-1
re-expresses it, up to the uniform $o(1)$, as an **equal-cardinality** sum of the **same** moduli
at higher frequencies. The map is injective: no two low coefficients merge and no mass cancels —
the band is **relabelled, not reduced**. Driving the moment to $o(K_A)$ therefore requires
*knowing* the high-frequency coefficients are small — a genuine high-frequency equidistribution
estimate, the OPEN input. The receipt sample ($A=256$:
$|c_A(1)|,|c_A(16)|,|c_A(256)|\approx0.074,0.073,0.072$) shows mass **transported up the ladder,
not annihilated**. RT-3 refutes the shortcut "iterate the $\times16$ relation until the coefficient
is small"; it is **not** a bound on the size of $c_A$.

## RT-04 — scope and relation to the open gate

RT-1/RT-2 are a *quantitative* statement of the digit self-similarity, with an explicit,
tight error whose constant is derived from the BBP source (via SC-6). They are, however,
**general**: the identity and the shape of the bound hold for any `U_n=16U_{n-1}+f(n)` with
small `f`, and RT-2 is **not** a source discriminator. The sharpest reason (verified by control C2):
because `U_0=0`, the scaled-forcing mutant `r'(n)=s·r(n)` gives, by linearity of the recurrence,
`U'_n=s·U_n` **exactly**, hence `c'_A(h)=c_A(s h)` — the mutant is literally the genuine orbit read
at rescaled frequency, so it satisfies the same `|h|`-form bound (gap `0.0` to 50 digits; worst
ratio `0.730`). So this is structure, not a BBP-specific cancellation law. They do **not** bound $|c_A(h)|$ from above by anything
$<1$ at a fixed scale — DC-1 of the selected-phase forge already supplies the known $\log$-scale
*modulus* loss, and that is a modulus bound, not cancellation. RT-3 is a barrier on a specific
method. None of this is progress on $\sum_{|h|\le q_A^2}|c_A(h)|^2=o(K_A)$.

### Claim ledger

| Claim | Status | Earned authority | Unpaid debt |
|---|---|---|---|
| RT-00 chain direction | Demonstrated | SC-8/SC-3/#476 (band⟹J⟹E⟹normal) + #293/SGO-09 (normal⟺$S_N{=}o(N)$); converse killed by `band_vs_J_cloud` | band⟹J is **not** reversible (generic converse false) |
| RT-01 identity | Demonstrated | exact algebra of $U_n=16U_{n-1}+r(n)$ | — |
| RT-02 bound | Demonstrated | triangle ineq + $|\sin x|\le|x|$ + merged SC-6 numerator bound; held-out receipt, 0 violations | — |
| RT-03 barrier (corrected) | Demonstrated (method obstruction) | **common-depth** $\times16$ injective + corrected geometric accumulation (RT-3a), 0 violations worst $0.923$ | not a size bound on $c_A$; reaches $\le A^{3/2}$, not the old $A^{3/4}\sqrt{|h|}$ |
| $\sum_{|h|\le q_A^2}|c_A(h)|^2=o(K_A)$ | **OPEN** | — | real high-frequency signed cancellation |
| π base-16 normality | **OPEN** | — | the above |

**π base-16 normality, the signed Weyl gate $S_N(h)=o(N)$, and RH are OPEN / not claimed.**
This uses established constructions; no original-priority claim.

### References
- Selected-current front SC-1..SC-8 (merged main), especially SC-6 numerator factorization
  `P(t)=(1-t)(t²+2)(t²+2t+2)`, `r(n)<15/((8n-7)(8n-6))`.
- Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions* (BBP ×16 orbit ↔ base-16 normality).
- Standard $|e(t)-1|=2|\sin\pi t|\le 2\pi|t|$.
