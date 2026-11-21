# Source-first BBP → Collatz: oriented prime response, 2-adic port obstruction, and Fourier-parity oracle

**2026-11-20 | SUCC stacked DRAFT research.** This note studies user-proposed direct arithmetic transport from the original zero-seeded BBP source into four-step 2-adic Collatz parity, with primary context in SUCC [#681](https://github.com/femboy2112/SUCC/pull/681), [#670](https://github.com/femboy2112/SUCC/pull/670), [#678](https://github.com/femboy2112/SUCC/pull/678), [#677](https://github.com/femboy2112/SUCC/pull/677), and sibling `femboy2112/collatz` plus `collatz-proof`. All proofs are paper derivations; finite exact checks and separately coded oracles live in this directory. **No claim of π base-16 normality, R0, Collatz termination for all positive integers, RH, quantum measurement or energy conservation.** No global scholarly priority claimed.

## Authentic source, types and notation

All *target* claims fix the original BBP source and literal zero seed:

\[
r(j)=\frac4{8j-7}-\frac2{8j-4}-\frac1{8j-3}-\frac1{8j-2},\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Write \(c_j=16^{-j}r(j)\), \(P_M=\sum_{j\le M}c_j\), and \(x=\sum_{j\ge1}c_j=\pi/16\), using the *classical* BBP identity as an imported premise. The completed circle orbit is \(\theta_n=\{16^n x\}\). Its digit register is \(d_{n+1}=\lfloor16\theta_n\rfloor\). The source tail satisfies the strict rational enclosure

\[
0<x-P_M<\varepsilon_M:=\frac{r(M+1)}{15\cdot16^M},\qquad M\ge0.
\]

The shortcut Collatz map is \(C(a)=a/2\) when \(a\) is even and \((3a+1)/2\) when odd, extended continuously to \(\mathbb Z_2\). Its classical parity encoder \(\mathcal Q(a)=\sum_{k\ge0}(C^ka\bmod2)2^k\) is a \(\mathbb Z_2\) homeomorphism with \(\mathcal QC^4=S_{16}\mathcal Q\). For arbitrary real hexadecimal words the source-selected 2-adic *constructed shadow* is \(\alpha=\mathcal Q^{-1}(\sum_{n\ge0}d_{n+1}16^n)\); it is **not** an identification of real π with a canonical 2-adic π, nor a known positive integer.

## SFC-01. The source-filter root split is *not* an integral 2-adic Collatz parity split — PROVED (source-specific)

The original Mellin mask factors exactly:

\[
Q(t)=4-2t^3-t^4-t^5=(1-t)H(t),\qquad H(t)=(t^2+2)(t^2+2t+2).
\]

Put \(A=t^2+2\) and \(B=t^2+2t+2=A+2t\). Then

\[
\boxed{\operatorname{Res}_t(A,B)=\operatorname{Res}_t(A,2t)=8.}
\]

For every odd prime \(p\), the resultant is a \(p\)-unit, hence the Chinese remainder decomposition of \(\mathbb Z_p[t]/(H)\) into \(\mathbb Z_p[t]/(A)\times\mathbb Z_p[t]/(B)\) exists as an integral algebra decomposition. But mod 2 both factors become \(t^2\):

\[
(\mathbb Z_2[t]/H)/2\simeq\mathbb F_2[t]/(t^4),
\]

which is local and has only idempotents 0 and 1. **No nontrivial idempotent exists in \(R_2=\mathbb Z_2[t]/H\).** Proof: an idempotent reducing to zero mod2 lies in \(2R_2\); the equality \(e=e^2\) then forces membership in \(2^kR_2\) for every \(k\), hence \(e=0\) by separatedness. Apply this to \(1-e\) when its reduction is 0. Therefore the factor projector does not preserve the integral 2-adic root algebra.

Over \(\mathbb Q_2\), the distinct factors split, and the rational projectors are genuine:

\[
E_+=\frac{1+t^4/4}{2}\equiv-\frac{t^3}{4}-\frac{t^2}{2}-\frac t2\pmod H,\qquad E_-=1-E_+.
\]

These satisfy \(E_\pm^2=E_\pm, E_+E_-=0\), with \(E_+=1\bmod A\), \(E_+=0\bmod B\). In the ordinary coefficient-supremum norm on the \(\mathbb Q_2\) companion basis \((1,t,t^2,t^3)\), multiplication by \(E_+\) has operator norm exactly **4**: multiplying integral polynomials by this reduced projector costs at most two binary digits of precision, and testing the input 1 attains the bound. This is a precisely **basis-declared precision bill**, not a universal information or physical energy bound.

**Stronger no-go:** Every endomorphism of the source algebra's regular module commuting with multiplication by \(t\) is multiplication by its value on 1. A 2-adically integral, \(t\)-equivariant projector would be a nontrivial idempotent in \(R_2\), impossible. Thus the two root Haar sectors cannot be obtained by a naive integral 2-adic equivariant splitting. An additional lift, orientation/phase head, different module or paid precision is indispensable. The existing 5/11 determinant signature at the **auxiliary** Fibonacci evaluator is compatible with this obstruction but is not a π-real-phase factor map.

## SFC-02. A signed Fourier (Rademacher) BBP source oracle for each individual Collatz parity — PROVED, finite source algorithm

For any fixed \(n\ge0\), \(j\in\{0,1,2,3\}\), define \(m_{n,j}=2^{3-j}16^n\). Then the actual Collatz parity bit selected by the *original* BBP source is

\[
\boxed{\epsilon_{4n+j}(\alpha_\pi)
=\frac{1-\operatorname{sgn}\sin(2\pi m_{n,j}x)}{2}
=\bigl\lfloor2^{4-j}16^nx\bigr\rfloor\bmod2.}
\]

The equality is literal: \(\lfloor16\{16^nx\}\rfloor\) is the next hexadecimal digit, and the relevant low-to-high binary bit is the scaled floor parity. \(x=\pi/16\) is irrational, so none of the stated sine arguments is a zero; there is no unrecorded endpoint convention. Substituting the authenticated source integral

\[
x=\int_0^1\frac{Q(t)}{16-t^8}\,dt
\]

turns the bit into the sign of a **specified analytic Fourier character of the original four-pole source**, without using a hexadecimal digit value as input to the predictor.

An executable *exact* rational stopping certificate is available. For \(q=2^{4-j}16^n\), use the original BBP interval and compute

\[
a=qP_M,\qquad b=q(P_M+\varepsilon_M).
\]

When \(\lfloor a\rfloor=\lfloor b\rfloor\), this common integer modulo 2 is the certified bit. Because \(q x\notin\mathbb Z\), the interval eventually lies inside a single unit cell as \(M\to\infty\). **Every fixed bit is eventually certified**, but no single *uniform precision bound* or asymptotic digit-density estimate follows merely from irrationality. This is mathematically an equivalent way to query source-selected digits, not evidence of a new arithmetic saving. It is source-first in *execution*, not independent of the full analytic value of \(x\).

In the current finite receipt the oracle certifies all 48 parities of the known first twelve hexadecimal digits, corresponding to parity address `0xA5888A6F3423`, with no decoded hexadecimal digit fed to the bit predictor. By the classical \(\mathcal Q^{-1}\) map this gives the selected positive integer residue `0x138D4B466283` modulo \(2^{48}\), as already found in SUCC #681.

## SFC-03. The quarter-circle BBP root thresholds select an exact *two-bit XOR observer* — PROVED, universal formula; source-selected instance

The original BBP source-filter left-interior roots occupy \(\theta=1/4,3/4\) in the **declared** normalized left-semicircle chart. On the *independent* real phase coordinate, the same numerical thresholds define the following parity observable:

\[
\boxed{q_n=\epsilon_{4n+2}\oplus\epsilon_{4n+3}
=\mathbf1_{\{\cos(2\pi\theta_n)<0\}}.}
\]

The two bits are the **third and fourth chronological Collatz parity bits** of a four-step block: they are the *two most significant bits* of the corresponding hexadecimal digit. They are not the first two parity bits of a Collatz state, and the chart coincidence is not a source-filter-to-phase conjugacy. Proof: digits 4–11 have high-bit pattern `01` or `10`, while digits 0–3 and 12–15 have pattern `00` or `11`. For the actual irrational \(x\), no phase lands exactly at 1/4 or 3/4.

Let \(\mathcal A_B=B^{-1}\sum_{n=B}^{2B-1}(1-\cos2\pi\theta_n)\), the open SUCC R0 statistic, and \(Q_B=B^{-1}\sum_{n=B}^{2B-1}q_n\). Then the exact universal pointwise comparison gives

\[
\boxed{\mathcal A_B\ge Q_B.}
\]

**A positive lower density of these source-selected signed quarter-sector responses would prove R0.** This is a conditional theorem, *not* an established density. It is strictly sufficient, not necessary: digits chosen only from `0,1` can have positive phase displacement while \(Q_B=0\) forever. The root positions themselves do not force the frequency of such events.

## SFC-04. Ordered BBP prime-square forcing produces an *oriented* future interferometric response — PROVED, counterfactual experiment

For prime \(p\ge7\), define \(j_p=(p^2-1)/8\). The actual first-pole \(4/p^2\) enters at forcing clock \(j_p+1\). **Do not swap these clocks.** Consider a separately labeled, zero-seeded counterfactual source that exchanges just the authentic adjacent inputs \(r(j_p),r(j_p+1)\), leaving every other source value in place. The two complete BBP-source values differ by

\[
\boxed{x-x^{\rm swap}=16^{-(j_p+1)}D_{j_p},\quad D_j=15(r(j)-r(j+1)).}
\]

The original source's Mellin integral gives

\[
D_j=15\int_0^1 t^{8j-8}(1-t^8)Q(t)\,dt>0,
\]

and shows \(D_{j+1}<D_j\). At the least prime-square order clock \(j_7=6\), \(D_6=111593821/3151825677<1/4\). Hence every \(p\ge7\) has \(0<D_{j_p}<1/4\). Define the source-computable delay

\[
d_p=\min\{d\ge0:16^dD_{j_p}\ge1/64\},\qquad
\Delta_p=16^{d_p}D_{j_p}.
\]

Then universally

\[
\boxed{1/64\le\Delta_p<1/4,\qquad d_p=6\log_{16}p+O(1).}
\]

The delay follows from the previously established and independently derivable asymptotic \(D_{j_p}\sim3600/p^6\). At future clock \(N_p=j_p+1+d_p\), let \(z=e(16^{N_p}x)\) and \(z'=e(16^{N_p}x^{\rm swap})\), where \(e(y)=\exp(2\pi iy)\). Their **genuinely oriented** two-head interference is

\[
\boxed{\operatorname{Im}(\overline{z'}z)=\sin(2\pi\Delta_p)\ge\sin(\pi/32)>0.}
\]

This is an exact source-derived *signed* lower bound with a prime-clock logarithmic delay. Its existence does **not** use the values of either phase or any decoded digit. Measuring it physically would require lawful repeatable preparations and a calibrated coherent comparison; here it is a mathematical counterfactual.

## SFC-05. The signed response forces two-digit / eight-Collatz-parity divergence — PROVED

The circular distance between \(\{16^{N_p}x\}\) and \(\{16^{N_p}x^{\rm swap}\}\) is \(\Delta_p\ge1/64\), since \(\Delta_p<1/4\). A two-hexadecimal-digit cylinder has width \(1/256\); if both real phases had the same first two digits, their circular separation would be less than \(1/256\). Contradiction. Consequently their two successive hexadecimal symbols differ, and under the **classical** four-step Collatz parity conjugacy, at least one of the corresponding **eight** Collatz parity bits differs.

Writing \(\epsilon_b,\epsilon_b'\in\{0,1\}\) and \(\chi_b=(-1)^{\epsilon_b}\), at the eight relevant Collatz clocks:

\[
\boxed{\sum_{b=4N_p}^{4N_p+7}(\chi_b-\chi_b')^2\ge4.}
\]

This is an exact finite signed-parity **response norm**, not a sign prediction for a particular individual bit, a physical energy, or a positive density assertion for the unperturbed π path. It identifies an unavoidable **cross-source counterfactual** distinction.

## SFC-06. A single source-anchored carry head supplies the lexicographic response sign — PROVED, target relative

Let \(\vartheta=\{16^{N_p}x\}\) and \(\vartheta'=\{\vartheta-\Delta_p\}\). Two-digit blocks \(B=\lfloor256\vartheta\rfloor\), \(B'=\lfloor256\vartheta'\rfloor\) are unequal by SFC-05. Therefore

\[
\boxed{\operatorname{sgn}(B-B')=\begin{cases}+1,&\vartheta\ge\Delta_p,\\-1,&\vartheta<\Delta_p.\end{cases}}
\]

The only missing datum beyond the source-derived \(\Delta_p\) is the **carry across the circle cut**. The original source supplies a finite certificate for that carry: scale its rigorous rational \([P_M,P_M+\varepsilon_M]\) by \(16^{N_p}\), verify both endpoints have the same integer floor, subtract that floor, and compare the residual interval to the rational \(\Delta_p\). Because \(\pi/16\) is irrational and \(\Delta_p\) rational, the comparisons terminate at some finite \(M\) for every fixed prime.

Unlike an unsigned phase separation, this is a **signed prediction before either two-digit block is explicitly decoded**. It needs a calibrated source/phase carry head. For the first tested primes, exact BBP interval certificates give signs:

| prime p | source order clock j_p | delay d_p | phase clock N_p | signed block orientation |
|---:|---:|---:|---:|:---:|
| 7 | 6 | 0 | 7 | + |
| 11 | 15 | 1 | 17 | + |
| 13 | 21 | 2 | 24 | + |
| 17 | 36 | 2 | 39 | + |
| 19 | 45 | 2 | 48 | **−** |
| 23 | 66 | 3 | 70 | + |
| 29 | 105 | 3 | 109 | + |
| 31 | 120 | 3 | 124 | + |
| 37 | 171 | 4 | 176 | + |
| 41 | 210 | 4 | 215 | + |
| 43 | 231 | 4 | 236 | + |

The negative \(p=19\) sign explicitly refutes the tempting claim that positive oriented source-phase response always makes the *digit-block* lexicographic difference positive. The missing winding/carry is consequential. The table is a finite certified observation, not an asymptotic sign law.

## SFC-07. Finite 2→3 reciprocity from the original source, without an unrestricted 2-adic→3-adic morphism — PROVED, inherited arithmetic

From SFC-02, assemble \(K\) source-certifiable chronological parity bits \(\epsilon_0,\ldots,\epsilon_{K-1}\), and let \(a_K\) be the unique residue modulo \(2^K\) having exactly that shortcut Collatz parity prefix (classical Bernstein–Lagarias inverse). For every ordinary **positive integer representative** \(a\equiv a_K\pmod{2^K}\), the first \(K\) parities agree. If a one-bit occurs at clock \(j\) and the next occurs at \(j+v<K\), the odd accelerated return obeys

\[
C_{\rm odd}(C^ja)=\frac{3C^ja+1}{2^v}\equiv 2^{-v}\equiv(-1)^v\pmod3.
\]

The sign, returned ternary residue, and waiting time are therefore determined *for every positive integer in that common binary cylinder*. This is the **2-adic valuation → 3-adic quadratic-character coupling** already studied in `femboy2112/collatz` (`RECON_COLLATZ_RECIPROCITY.md`, C-0245/C-0250), instantiated for a source-selected finite π parity prefix without assuming integer Collatz termination. We **cannot** apply a literal \(\mathbb Z_2\to\mathbb Z_3\) continuous field map to the completed arbitrary 2-adic state \(\alpha_\pi\): none is supplied. The diagonal ordinary-integer representatives make the finite cross-place statement well typed.

## SFC-08. Three explicit no-gos — PROVED countermodels

1. **Same-forcing locked seed:** the original forcing with homogeneous seed \(s=-x\) has identical ordered source differences \(D_j\), prime-square marks, root algebra, and signed cross-source *difference* response when subjected to the same swap, but its unperturbed completed phase is exactly zero at all clocks. Thus SFC-04/05 **cannot imply R0 or π normality**. The authentic source-head \(U_0=0\) rejects the altered seed, but no *uniform* source/order-only response bound can stand in for a signed statement on the unperturbed selected phase.
2. **Wrong source/mutant:** the matched-leading-jet mutant \(Q_*=Q+(1-t)^2\) retains the original leading forcing asymptotic but changes prime-square p-primary mark \(4/p^2\to5/p^2\) and destroys the original common root circle. A generic monotonic-order response does not authenticate the original source; a separately retained p-primary root/source head is necessary. Constant forcing has \(D_j=0\), killing the counterfactual response entirely.
3. **No universal parity sign without a carry head:** hold fixed a source-derived \(\Delta\in[1/64,1/4)\), then vary the homogeneous seed. An original phase with \(\vartheta=\Delta/2\) yields a negative block-order comparator; a phase with \(\vartheta=1/2\) yields a positive comparator. The same \(\Delta\) and prime-source difference cannot determine this sign unless the absolute phase/carry information is retained.

## SFC-09. The exact remaining mathematical barrier — OPEN

The new source-first signed response SFC-04 belongs to **two different, deliberately compared sources**; SUCC's normality rung concerns the single unchanged authentic source. A genuinely useful new π theorem must derive, from the original zero-seeded four signed poles and independently sourced prime/cofactor/carry chronology, an all-large-shell lower bound for one of the *unchanged orbit's* signed phase, quarter-sector or Gaussian observables. A conditional sufficient quarter-sector criterion is

\[
\boxed{\liminf_{B\to\infty} B^{-1}\sum_{n=B}^{2B-1}
(\epsilon_{4n+2}(\alpha_\pi)\oplus\epsilon_{4n+3}(\alpha_\pi))>0
\ \Longrightarrow\ \mathrm{R0}.}
\]

This is not known from the source and is not equivalent to full normality. Neither a source-root idempotent, Fourier sign identity, first-48-bit certificate, partner observer code, nor a counterfactual positive imaginary response proves the premise. More generally normality still requires all fixed nonzero Weyl frequencies to have vanishing chronological means.

**Research verdict:** SFC-01 to SFC-08 are proved in the exact declared algebraic/finite counterfactual domains, or are attributed to classical results; they provide a quantified 2-adic source-port obstruction and a source-derived signed prime-to-Collatz response without prior digit decoding. The first nontrivial *original-zero, no-source-mutation all-shell* signed Fourier inequality is **UNVERIFIED**. Neither π-normality nor the positive-integer Collatz conjecture has been proved.
