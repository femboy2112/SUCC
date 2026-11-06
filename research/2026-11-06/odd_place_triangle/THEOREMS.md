# Operation ODD-PLACE TRIANGLE: the exact missing adelic character and its source-born prime clocks

**2026-11-06. Research-only child of SUCC #528, exact parent `45c5d41435fdf94998d81901b0e58b9fa7775106`.** Original four signed BBP poles and literal `U_0=0` remain unchanged. π base-16 normality and all-prefix signed real Weyl cancellation remain OPEN. `PROVED LOCAL` below means a displayed exact argument with its stated scope, not academic priority or a Lean certificate.

## 0. Authentic rational source and the three-layer question

Use

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

The combined denominator `D(n)` is odd; each rational `U_n` has odd reduced denominator. Parent #527 proves its entire-clock 2-adic interpolation `V(n)=U_n` and Haar permutation of every `Z/2^k`. Parent #528 proves exact reconstruction of each real fraction from high-precision 2-adic state **plus genuine integer carry and odd denominator**, but no low-resolution cross-place distribution transfer. This round adds the **missing odd-prime character** layer to the joint-source map.

## AT-01 — exact adelic transport by ALL odd-prime principal parts (CLASSICAL / PROVED LOCAL instance)

For a rational `x=a/d` reduced, `d` odd, and any prime `p|d`, write `d=p^e d'` with `gcd(d',p)=1`, and set

\[
[x]_p=\frac{t_p}{p^e},\qquad t_p\equiv a(d')^{-1}\pmod{p^e},\quad 0\le t_p<p^e.
\]

At all other finite primes `[x]_p=0`; in particular **`[x]_2=0`**. The Chinese remainder theorem gives

\[
\boxed{x\equiv\sum_{p\mid d}[x]_p\pmod{\mathbb Z}.}\tag{AT1}
\]

Indeed multiply by `d`: modulo `p^e` the `p` term equals `a` and every other term vanishes; CRT then yields equality modulo `d`. Thus for EVERY integer `h` and original finite time `n`, with `e(t)=exp(2πit)`, 

\[
\boxed{e(hU_n)=\prod_{\substack{p\text{ odd}\\p\mid\operatorname{den}(hU_n)}}e([hU_n]_p),\quad
W_A(h)=\frac1A\sum_{n=A}^{2A-1}\prod_{p\text{ odd}}e([hU_n]_p).}\tag{AT2}
\]

This is the canonical additive adele product formula in the sign convention `ψ_∞(x)=e(x)`, `ψ_p(x)=e(-[x]_p)`. Only finitely many factors at each n. The **entire Fourier phase of each rational U_n lives in the odd-prime principal-part correlation**. Haar at the prime2 does not supply a signed estimate for this *product*. No ad hoc identification of π as a 2-adic number is used.

**Carry nuance.** Every integer `C_n=floor(U_n)` is p-integral for every p, hence `[U_n]_p=[\{U_n\}]_p`: the complete odd-place character representation is carry-independent. Integer carries ARE needed for the different operation in #528 of recovering a rational fractional numerator from `V(n) mod2^K` and known denominator. These are two typed reconstruction pathways; neither overwrites the other.

**Source provenance of supports.** For n≥1, every denominator prime of `U_n` divides at least one `D(j)` for 1≤j≤n, so all its denominator primes are odd and ≤8n−3. This finite, explicitly growing support is source-specific; the carrier's odd-place genealogy is not an arbitrary infinite collection at fixed n.

## AT-02 — exact birth of new odd-prime poles in the source (PROVED LOCAL)

For **each prime p>5**, let `n_p` be the least positive integer index for which `p|D(n_p)`, and `c_p=p r(n_p) mod p`. Then the first pole is unique and simple, and

\[
\boxed{
(n_p,c_p)=
\begin{cases}
((p+7)/8,\quad 4),&p\equiv1\pmod8,\\
((p+3)/8,\quad-1),&p\equiv5\pmod8,\\
((p+1)/4,\quad-1/2),&p\equiv3,7\pmod8.
\end{cases}}
\tag{AT3}
\]

The coefficients are interpreted in `F_p` (`-1/2` means minus the inverse of2). Proof: compare positive occurrences of the four integer linear factors `8n−7`, `8n−3`, `4n−1`, `2n−1`, including possible higher odd multiples of p. The displayed index is the first positive common divisor occurrence in each residue class. Distinctness at this index follows because the pairwise pole collisions are supported only at exceptional primes 2,3,5; it can also be verified directly by substituting the displayed expressions. At p>5 the relevant factor is exactly p, while the other factors are p-units. In the original signed partial fractions, the residues are respectively `4/p`, `−1/p`, `−1/(2p)`; all other terms are p-integral.

Before n_p the rational history is `Z_p`-integral. Therefore `v_p(U_{n_p})=-1` and `pU_{n_p}≡c_p (mod p)`. Let n'_p be the **next** integer index with `p|D(n'_p)`. For every `0≤t<n'_p−n_p` the intervening source terms are p-integral, so

\[
\boxed{v_p(U_{n_p+t})=-1,\quad
[U_{n_p+t}]_p=\frac{c_p16^t\bmod p}{p}.}\tag{AT4}
\]

The original four-pole source therefore *births a new p-local character* at a predictable moment, then evolves it by the Frobenius-like multiplier16 until the next pole collision. This is **not** the same thing as global real-circle genericity.

## AT-03 — classical Gauss cancellation inside a complete clean prime clock (PROVED LOCAL / CLASSICAL BOUND)

Let `m_p=ord_p(16)` and assume `m_p≤n'_p−n_p`. On the first `m_p` steps following birth, the p-local principal part visits exactly the multiplicative coset `c_p<H_p>` of `H_p=<16> in F_p^×`. The classical Gauss-sum / multiplicative-character estimate says

\[
\boxed{\left|\frac1{m_p}\sum_{t=0}^{m_p-1}
 e([U_{n_p+t}]_p)\right|\le\frac{\sqrt p}{m_p}.}\tag{AT5}
\]

Proof sketch: let `d=(p−1)/m_p`. Project onto the index-d subgroup with multiplicative characters; the principal character contributes −1 to the nontrivial additive-character sum, and each nonprincipal Gauss sum has magnitude √p. Averaging gives absolute value ≤`(1+(d−1)√p)/d < √p` before dividing by m_p. This standard finite-field estimate is **independent of π**, though its application uses the original p-birth mechanism AT3–AT4.

**Exact identity isolating the remaining arithmetic coupling.** Set `a_t=e([U_{n_p+t}]_p)` and `b_t=e(U_{n_p+t}-[U_{n_p+t}]_p)`, so `e(U)=a_tb_t`. Write uniform sample mean `E_m` and signed covariance `Cov_m(a,b)=E_m(ab)-E_m(a)E_m(b)`. Then

\[
\boxed{\left|E_m e(U)\right|\le\frac{\sqrt p}{m_p}+|\operatorname{Cov}_m(a,b)|.}\tag{AT6}
\]

**The exact remaining cross-place gate is the original-source signed covariance of the newborn prime clock against all OTHER odd-prime characters.** The local Gauss saving is unconditional; the needed covariance saving is OPEN. Current finite values are in FINITE_RESULTS.json. This is not a proof that a single bounded prime clock forces normality: time windows are short and do not cover all selected n.

**Hostile second-prime control (PROVED LOCAL).** Fix a full p-local cycle `a_t^* in {0,...,p−1}` and a distinct odd prime q. Choose integer `b_t` nearest `−q a_t^*/p`, and put

\[
\widetilde U_t=\frac{a_t^*}{p}+\frac{b_t}{q}.
\]

Then the p-local principal part is EXACTLY `a_t^*/p`, while `|\widetilde U_t|≤1/(2q)`, hence

\[
\boxed{\left|\frac1m\sum_te(\widetilde U_t)\right|\ge1-\frac\pi q.}\tag{AT7}
\]

This produces **almost perfectly aligned real phases from a highly canceling p-local character**, just by adding a different odd prime. It refutes any claimed universal implication `local Gauss bound => real Weyl saving`. It is a rational-sequence countermodel, NOT the authentic SUCC forced recurrence.

## AT-04 — the exact harmonic–Gamma/Pisot edge of the original source (PROVED LOCAL, CLASSICAL DIGAMMA)

Let the *unweighted* original-source harmonic accumulation be `H_source(N)=sum_(n=1)^N r(n)`. Set weights `w=(4,-2,-1,-1)` and shifts `a=(7,4,3,2)`. The exact digamma telescoping identity is

\[
H_{source}(N)=\frac18\sum_{j=1}^4w_j\left[\psi\left(N+1-\frac{a_j}{8}\right)-\psi\left(1-\frac{a_j}{8}\right)\right].\tag{AT8}
\]

Since `sum_j w_j=0`, all large-`N` `log N` terms cancel; the shared `−γ` part of each rational digamma value cancels too. Gauss's digamma theorem for denominator8 reduces the resulting exact sum to

\[
\boxed{\sum_{n=1}^{\infty}r(n)=
\frac{(4+5\sqrt2)\pi}{16}
+\frac58\log2+\frac{5\sqrt2}{8}\log(1+\sqrt2).}\tag{AT9}
\]

The apparent `γ` is a **normalization-relative finite part**, not a surviving physical constant in the balanced source. For a SOURCE MUTANT with first weight `4→5`, the total weight becomes1. Its unweighted sum instead has the asymptotic logarithmic divergence `+(1/8)log N`, and its finite part contains `+γ/8`, relative to the displayed digamma regularization. This is a load-bearing source-weight diagnostic: the harmonic `1/n` leading contribution is canceled by the original BBP weights.

The number `δ=1+√2` is the **silver Pisot unit** (its conjugate `1−√2` has |·|<1). The golden unit `φ=(1+√5)/2` does NOT appear automatically in AT9. This supports looking at a *family* of Pisot–harmonic–Gamma charts rather than assuming the native 8-fold BBP source specifically selects the golden chart. The exact formula is mathematical; an explicit functor linking φ or the previous extruded triangle to the selected π Weyl bound remains UNVERIFIED.

## AT-05 — the proposed extruded co-dual triangle, type-checked as an INSTRUMENT, not a source theorem

The earlier SUCC extruded triangle used `λ=φ^-1` and
`D(r)=ψ(r)−λ^r=H_(r−1)−γ−λ^r` (at positive integral r), with `D(2)=φ^-1−γ`, Fibonacci/Pisot transport and Gamma(2) carrier. This is a DIFFERENT analytic chart from the authentic 8-fold BBP digamma/silver calculation above.

To represent the *co-dual suggestion* cleanly, take formal placeholders (H,P,G) standing for harmonic, Pisot, Gamma orientations and map them to pairwise edge coordinates

\[
\boxed{E(H,G,P)=(H+G,\ H+P,\ G+P).}\tag{AT10}
\]

The proposed interpretation is: `H+G ↔ 2-adic state`, `H+P ↔ integer carry`, `G+P ↔ real fractional phase`. Algebraically `det E=-2` and, over Q,

\[
H=(E_1+E_2-E_3)/2,\quad
G=(E_1+E_3-E_2)/2,\quad
P=(E_2+E_3-E_1)/2.
\]

Over `F_2` its kernel is the one-dimensional diagonal subspace `(1,1,1)`, so a **shared parity bit is lost under pairwise observation**. This is a suggestive structural parallel to RS1b's genuine next-bit flip, but NOT evidence of a canonical relation to that source identity. `γ` and `φ` are real constants; no map into Q₂ is declared or implied here. The co-dual is currently a finite-dimensional linear-algebra *probe specification*, not an established category equivalence. A nontrivial theorem would have to give explicit, source-faithful compatible maps and a testable Fourier estimate, not just match triangles visually.

## Exact frontier after this round

1. **PROVED LOCAL**: original finite BBP real phases equal the product of odd-place local characters, with p=2 trivial; all odd conductor primes born before time n are ≤8n−3.
2. **PROVED LOCAL**: predictable p-birth residue, exact interval p-local power-of-16 orbit, and rigorous Gauss cancellation bound on a complete clean cycle.
3. **PROVED LOCAL**: exact harmonic–Gamma finite part of the original source; γ cancels and silver Pisot unit emerges. Abstract pair-edge co-dual has a mod2 parity kernel.
4. **OPEN**: a bound on signed cross-prime covariance or another source-selected all-horizon criterion that actually yields `W_A(h)->0` for every nonzero fixed h. Local cancellation, exact CRT, and a triangle correspondence alone do not deliver it.

**Primary prior art / references:** canonical adelic additive-character product formula (e.g., Brian Conrad, *The Character Group of Q*, Stanford lecture notes); finite-field multiplicative subgroup Gauss bounds (Kurlberg, *Bounds on Exponential Sums over Small Multiplicative Subgroups* 2007, quoting the classical Gauss-sum argument); Gauss's digamma theorem and classical rational argument expansions. Original BBP Bailey–Borwein–Plouffe 1997; SUCC source inherited from #521, #527, #528. No priority asserted. Tests do not substitute for external proof verification.
