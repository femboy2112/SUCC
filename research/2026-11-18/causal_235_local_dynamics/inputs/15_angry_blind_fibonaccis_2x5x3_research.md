# 15 Angry Blind Fibonaccis — 2×5×3 and BBP prime resonance

**Research note — 18 November 2026.** Research derived against `femboy2112/SUCC`, main `81be6b897ae980b801a3b9de9e22ef81e8360bfb`. Read-only. The original BBP four-pole source and zero seed are unchanged. The script `fibonacci_2x5x3_probe.py` passes 711 exact standard-library assertions. **R0, full base-16 normality of π, and any signed all-shell estimate are OPEN.** This is not externally refereed and does not claim academic priority for classical Fibonacci identities.

## 1. Definitions and source contract

For all `n >= 1`:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\qquad U_n=16U_{n-1}+r(n).
\]

The auxiliary original-source signed Mellin mask and its unique positive five-channel factorization are

\[
Q(t)=4-2t^3-t^4-t^5=(1-t)H(t),\quad H(t)=4+4t+4t^2+2t^3+t^4.
\]

These are **Mellin-lag operators**, not the native BBP chronological successor. The five memory coefficients are `(4,4,4,2,1)`.

## 2. Two Fibonacci channels, five source frames, three quadratic observation channels

Let `A=[[1,1],[1,0]]`, so `A^5=[[8,5],[5,3]]`, `A^10=[[89,55],[55,34]]`, and `A^10=11A^5+I`. Consequently

\[
F_{n+10}=11F_{n+5}+F_n,\qquad F_{10}=F_5L_5=5\cdot11=55.
\]

A two-component real state `(a,b)` evolves by `(a+b,a)`. The three quadratic observations `(a²,ab,b²)` evolve by

\[
\operatorname{Sym}^2(A)=\begin{pmatrix}1&2&1\\1&1&0\\1&0&0\end{pmatrix},\quad
\chi(\lambda)=(\lambda+1)(\lambda^2-3\lambda+1).
\]

Its eigenvalues are `φ², -1, φ^{-2}`. The quadratic combination `a²-ab-b²` changes sign at each step. If five frame positions are carried along, this gives an exact 10-coordinate underlying `2×5` system with 15 `3×5` quadratic readouts, provided every frame carries a real two-state vector and its prescribed successor. The lift is **not bijective**: `v` and `-v` have identical quadratic readouts. The sign/seed label must survive as extra memory. This is not Tribonacci dynamics and is not a derivation of BBP's hexadecimal digit law.

## 3. Why the original source's Fibonacci norm equals 55

The inverse Fibonacci transfer `M=A^{-1}=[[0,1],[1,-1]]` has eigenvalues `φ^{-1}` and `-φ`, the two roots of `1-t-t²`. Polynomial reduction modulo `1-t-t²` gives `Q(t) ≡ 7-6t`. Hence

\[
Q(M)=7I-6M=\begin{pmatrix}7&-6\\-6&13\end{pmatrix},\qquad \det Q(M)=55.
\]

The same matrix has the source-specific expression

\[
Q(M)=15I-A^5-M,
\]

where `15=-Q'(1)=H(1)`. Its eigenvalues `10±3√5` equal the two squared nonconstant pentagon Fourier amplitudes of `H`. Thus `det Q(M)=F_{10}` is a true exact identity using *this* source and the Fibonacci transfer; whether this numeric equality is a mechanism for Weyl cancellation is unverified.

## 4. An exact source-to-pentagon spectral intertwiner

Let `R` cyclically permute five coordinates, `C=R+R^{-1}`, `J` be the five-by-five all-ones matrix, `D` the index-doubling permutation `D(e_j)=e_{2j (mod5)}`, and `G=H(R)H(R^{-1})` the nonnegative source-memory Gram operator. Exact polynomial algebra yields:

\[
G=13I+6C+40J,\quad
Q(C)=7I-6C-11J,\quad
DCD^{-1}=J-I-C.
\]

Therefore

\[
\boxed{DGD^{-1}-Q(C)=57J.}
\]

On `V_0={v:sum_j v_j=0}`, the `J` term vanishes, so the two operators are exactly conjugate. Both have eigenvalues `10±3√5` (each double). The doubling map interchanges the two golden Fourier sectors. This is a genuine, source-specific spectral identity, not a native chronological BBP intertwiner. The mutation `H(t) -> H(t)+t^4` (hence `Q -> (1-t)(H+t^4)`) preserves the zero factor but *breaks* this conjugacy, as tested by exact matrices.

## 5. The rank-of-appearance resonance theorem

For odd primes `p`, define `d_p=ord_p(16)` and for positive integers `m`, `z(m)=min{k>=1:m|F_k}`. Classical Fibonacci strong divisibility gives:

\[
16^{F_k}\equiv1\pmod p
\quad\Longleftrightarrow\quad d_p\mid F_k
\quad\Longleftrightarrow\quad z(d_p)\mid k.
\]

The five-step sequence `x_m=F_{5m}` obeys `x_{m+2}=11x_{m+1}+x_m`. Modulo 5, all `x_m` are zero. Modulo 11, `x_{m+2}=x_m` and `x_0=0,x_1=5`, so `x_m≡0` for even `m` and `5` for odd `m`. Thus period-5 prime clocks resonate at *every* five-index block, period-11 clocks every *second* block. `k=10`, `F10=55` is the first common positive resonance.

More generally, five-step indices `k=r+5m` admit a resonance for a given prime-clock order `d_p` if and only if `gcd(5,z(d_p)) | r`, by elementary linear congruence. This partitions prime clocks by permitted pentagonal index classes.

## 6. Exact authentic BBP calibration at the common resonance F10=55

Choose `L=55`, start at clock 1, end at clock 56 (`2B=56`, `B=28`). In the simple-pole range `p²>8×56` and `p<=8×56`, the complete set of primes satisfying `16^55≡1 mod p` is

| p | ord_p(16) | [p U_56]_p | first BBP denominator birth |
|--:|--:|--:|--:|
| 23 | 11 | 9 | 6 |
| 31 | 5 | 19 | 8 |
| 41 | 5 | 33 | 6 |
| 89 | 11 | 30 | 12 |
| 397 | 11 | 4 | 50 |

Every listed residue is nonzero. As a result, `23*31*41*89*397 = 1,032,889,589` divides the actual reduced denominator of the original `U_56`. Every local value was checked by two routes: exact `Fraction` recurrence and the independent mod-p recurrence

\[
[pU_{n+1}]_p=16[pU_n]_p+[pr(n+1)]_p.
\]

Because `16^55≡1 (mod p)`, the homogeneous part cancels over the chosen lag and the local increment equals the signed source innovation. This is a **finite, source-faithful** five-prime resonance, not a statistical estimate for π.

An independent order-9 example falls outside the `k=10` synchronous 5/11 families: for `p=73`, `ord_73(16)=9`, `z(9)=12`, and `F12=144`. On the original source interval clocks `130 -> 274`, `[73 U_130]_73=8` and `[73 U_274]_73=0`, so the source innovation is `65 mod 73`; again `73²>8·274` allows simple-pole reduction. This demonstrates a different pentagonal index class (`12 mod 5 = 2`), not an all-shell mechanism.

### Resonance can also suppress old prime information

If `v_p(U_n)=-1` and `p | (16^L-1)`, then `v_p((16^L-1)U_n) >= 0`. A resonant lag *annihilates* the old p-primary pole from its homogeneous part; only the new signed source innovation can reintroduce a p-primary pole in `U_{n+L}-U_n`. Therefore resonance is not intrinsically mixing; it can increase coherence. Source-local pole cancellation and real-circle Fourier cancellation remain distinct phenomena.

## 7. Hostile controls and the asymptotic obstruction

1. **Source mutation:** The perturbed five-channel mask retains the null factor `(1-t)` but destroys the pentagon Gram intertwiner. Therefore the intertwiner captures authentic coefficient structure within the declared source class.
2. **Wrong seed:** Same-forcing real solutions can have different completed circle trajectories. Every source-only mask identity still holds for them. Hence no source-only spectral norm proves R0.
3. **Local-to-real failure:** A prime-local residue `[pU_n]_p` does not control `e^{2πi U_n}` without full Archimedean integer winding. CRT fractions and real phases are different observables; SUCC's existing cofactor-clone controls defeat source-blind lifts.
4. **Simple-pole horizon:** For any fixed prime p, `p²>8(n+L)` eventually fails as n or a Fibonacci lag L grows. The above mod-p construction cannot be extrapolated to arbitrarily late shells at a fixed p; either p must grow or a correctly valued higher-p-adic tower must be used.
5. **Resonance supply:** No theorem here guarantees sufficiently many growing primes of suitable radix orders and BBP denominator births on every large shell. Even supplying them would still leave a source-selected signed real-phase estimate unpaid.

## 8. Target for a verdict-changing probe

For a frozen moving Fibonacci lag `L_B=F_{k(B)}`, let `P_{B,L}` be the original-source, actually surviving prime registers with `p²>8(2B+L_B)` and `ord_p(16)|L_B`. Pre-register a signed joint response using both the actual Archimedean phase

\[
\exp\{2\pi i h(U_{n+L_B}-U_n)\}
\]

and their full prime/cofactor/winding tags. First prove existence and size of the selected prime register family; then bound the **actual** signed time average, retaining its source and reference labels. Test coherent wrong-seed, near-locking and cofactor clones first. A bound on positive prime energy alone is insufficient.

For the original completed orbit, the Pascal difference gives

\[
U_{n+L}-U_n=(16^L-1)16^n\pi/16 +T_n-T_{n+L},\qquad T_n-T_{n+L}>0.
\]

This supplies a lawful source-to-real transfer with a separately payable error. It does not supply a nontrivial cancellation bound. The universal targets remain R0 `liminf_B (D_B+J_B)/B>0` and full normality `W_B(h)->0` for every fixed nonzero integer h.

**Verdict:** Exact 2×5/3-channel duality, source-specific pentagon Gram intertwiner, Fibonacci–Lucas F10 synchronization, and finite prime-innovation calibration. The source-selected asymptotic arithmetic-to-real-correlation bridge remains **UNVERIFIED**.

### Repository background

- Original source mask: https://github.com/femboy2112/SUCC/blob/7e406514ffdd1dac932cdfa6a0e1bf12b8059ebf/research/2026-11-17/causal_clock_scrambling/BBP_IMPULSE_MELLIN_FILTER.md
- Source prime survival: https://github.com/femboy2112/SUCC/blob/2f0b160c52c5a2126dc8b783c8368127874ddb13/research/2026-11-17/pro_pi_crucible/EFFECTIVE_PRIME_SURVIVAL.md
- Original golden circle triangulation: https://github.com/femboy2112/SUCC/blob/07b218efadf6daa91dab6e2637485860a1b0cef2/research/2026-11-08/fibonacci_circle_triangle/PROOFS.md
- Full frontier: https://github.com/femboy2112/SUCC/blob/main/docs/PI_NORMALITY_FRONTIER.md
