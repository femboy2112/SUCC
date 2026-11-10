# Signed Basel tails are exactly a Weyl/Cesaro gate (source-selected Omega trace)

**Research continuation, 2026-11-10; child of draft PR #585.** This note fixes a strict misconception: the scalar Basel identity, unphased positive Gibbs expectations and an O(1/A) tail bound do **not** establish normality. What can establish it is an **o(1/A) signed cancellation bound on every translated Basel tail**; for the original BBP phase, this criterion is rigorously equivalent to Weyl decay. All statements here are elementary summation-by-parts/Tauberian equivalences for *bounded* sequences, not a proof of the missing signed estimate.

## T1. Signed Basel tail criterion — theorem and exact quantitative bounds

Let `(a_n)_(n>=1)` be an arbitrary complex sequence with `|a_n|<=1`. For each integer `A>=1`, put

```math
F(A)=\sum_{n=A}^{\infty}\frac{a_n}{n^2},\quad
W_A=\sum_{n=A}^{2A-1}\frac1{n^2},\quad
B_A=\frac{F(A)-F(2A)}{W_A},\quad
c_A=\frac1A\sum_{n=A}^{2A-1}a_n.
```

Every `F(A)` converges absolutely, and `1/(2A) <= W_A <= 1/A` by integral/pointwise comparison. Write

```math
\delta_A=\sup_{n\ge A}n|F(n)|,\qquad
\eta_A=\sup_{B\ge A}|B_B|.
```

Then for every integer `A>=1`, the **exact discrete inverse Abel identity** is

```math
\boxed{\sum_{n=A}^{2A-1}a_n=A^2 F(A)-(2A-1)^2F(2A)
+\sum_{n=A+1}^{2A-1}(2n-1)F(n).}
\tag{INVERSE-ABEL}
```

Consequently

```math
\boxed{|c_A|\le 5\delta_A\le10\eta_A,\qquad |B_A|\le3\delta_A.}
\tag{TAIL-DOMINANCE}
```

**Proof of first inequality.** Divide INVERSE-ABEL by `A`, use `|F(n)|<=delta_A/n`, and bound the three contributions by `A delta_A`, `(2A)delta_A`, and `2(A-1)delta_A`. The sum is at most `5A delta_A`.

**Proof of second inequality.** The absolutely convergent dyadic dissection is

```math
F(n)=\sum_{j=0}^{\infty}\big[F(2^j n)-F(2^{j+1}n)\big]
=\sum_{j=0}^{\infty}W_{2^j n}B_{2^j n}.
```

For `n>=A`, `|F(n)|<=eta_A sum_j (2^j n)^(-1)=2eta_A/n`, hence `delta_A<=2eta_A` and `|c_A|<=10eta_A`. Finally `|F(A)-F(2A)|<=delta_A/A+delta_A/(2A)` and `W_A>=1/(2A)` imply `|B_A|<=3delta_A`. QED.

**Full equivalence.** For any bounded complex sequence,

```math
\boxed{\quad c_A\to0\quad\Longleftrightarrow\quad
A F(A)\to0\quad\Longleftrightarrow\quad B_A\to0
\quad(A\to\infty,\ A\in\mathbb N).}
\tag{BASEL-TAUBERIAN}
```

The right-to-left implications are immediate from TAIL-DOMINANCE. For the remaining direction, `c_A->0` implies the ordinary prefix sums `S(N)=sum_(n=1)^N a_n=o(N)`: partition `[1,N]` recursively into approximately halved consecutive intervals `[A,2A)`, where each large block contributes `o(A)` and boundedness controls the finitely many small endpoints. A direct dyadic recurrence is `S(2A-1)=S(A-1)+A c_A`; the even endpoint contributes at most 1. Then finite summation by parts, followed by the absolutely convergent limit, gives

```math
F(A)=-\frac{S(A-1)}{A^2}
+\sum_{n=A}^{\infty}S(n)\left(\frac1{n^2}-\frac1{(n+1)^2}\right).
```

For `n>=A`, `|S(n)|<=epsilon_A n` with `epsilon_A->0`; `sum_(n=A)^infty n(1/n²-1/(n+1)²)<=2/A`, so `A|F(A)|<=o(1)+2epsilon_A->0`. Then `|B_A|<=3 delta_A->0`. This proves all three equivalences without assuming any special independence or random digits. QED.

## T2. The Basel × six-frame Omega trace criterion for pi

The previous [PHASE_OBSERVER.md](PHASE_OBSERVER.md) constructs directed shifts `A_t`, `t=0,...,5`, from **actual** intrinsic two-/three-block chronological Omega-Haar commutators, with exact six-frame weights on the successor edges for every `n>=11`.

Retain the immutable zero-based four-pole source `R(j)` and `P_infty=pi/16`, with real-lift phase

```math
Y_n(s)=16^n(s+\pi/16),\quad
D_{h,s}e_n=\exp(2\pi i(h/15)Y_n(s))e_n.
```

For every integer `h!=0`, define `a_n(h;s)=exp(2pi i h Y_n(s))`. For each `A>=11`, both trace operators below are well-defined (diagonal thermal weight is trace-class):

```math
\boxed{F_h(A;s)=\sum_{n=A}^{\infty}\frac{e^{2\pi i hY_n(s)}}{n^2}
=18\sum_{t=0}^5\operatorname{Tr}\left(
P_{\ge A}e^{-2H_0}A_tD_{h,s}A_t^*D_{h,s}^*\right).}
\tag{OMEGA-BASEL-TAIL}
```

Here `H0 e_n=(log n)e_n`, `P_(>=A)=sum_(n>=A)|n><n|`, and the coefficient of the edge `n -> n+1` is retained before weighting. The equality is **exact**, not a fit: the six shifted squared coefficients sum to 1, and `(h/15)(Y_(n+1)-Y_n)=hY_n` on the real lift.

Thus the following *fully specified*, source-and-seed-selected trace criterion is equivalent to Weyl decay for the zero seed:

```math
\boxed{\forall h\in\mathbb Z\setminus\{0\}:\quad
\lim_{A\to\infty} A\!\sum_{t=0}^5
18\operatorname{Tr}(P_{\ge A}e^{-2H_0}A_tD_{h,0}A_t^*D_{h,0}^*)=0.}
\tag{PI-NORMALITY-EQUIVALENT}
```

By classical Weyl's criterion applied to the radix-16 orbit, this is **equivalent to** pi's base-16 normality. It is not a proof that the condition holds. For only `h=8k`, odd `k`, the criterion matches the corresponding signed odd-eight necessary input for SUCC's conditional parity-word theorem; it alone does not give full hexadecimal normality.

**Magnitude and missing saving.** The trivial positive trace norm gives

```math
|F_h(A;s)|\le\sum_{n=A}^{\infty}n^{-2}=\frac1A+O(A^{-2}).
```

The actual proof obligation is the **strictly stronger** estimate `F_h(A;0)=o(1/A)` for every nonzero integer mode. Any replacement by a bound with a fixed constant times `1/A` is not progress toward normality.

## T3. Crucible: negative and mutation controls

- **Fixed coherent wrong seed:** `s*=-pi/16` makes every `a_n=1`; then `F_h(A;s*)=sum_(n>=A)1/n²`, so `A F_h(A;s*) ->1`, not zero, and `B_A=c_A=1`. All unphased Omega and Basel identities still hold.
- **Alternating control:** `a_n=(-1)^n` has `|F(A)|<=1/A²` by alternating-series remainder, hence `A F(A)->0`, and its Cesaro and Basel-shell means vanish. This is a check that cancellation, not positive mass, is measured.
- **Log-scale block control:** `a_n=(-1)^floor(log2 n)` is bounded but has constant sign over `[2^k,2^(k+1))`; `|B_(2^k)|=|c_(2^k)|=1`, and the equivalence correctly refuses normality. The parity of the exponent must be computed from *integer* dyadic block boundaries, not floating `log2` for large n.
- **Source mutant:** Changing the original BBP four poles while keeping a positive Mellin source can preserve many unphased moments, so phase selection must explicitly use the four-pole source and `U0=0`, with all carries. A finite moment match is not an infinite signed certificate.
- **Arithmetic/transport boundary:** the original Basel measure is not continuous as a function of the 2/3-adic completion alone (e.g. `1+6^k ->1` p-adically while reciprocal squares go to 0 real). The **Archimedean height** in `e^-2H0` remains necessary, not optional cosmetic notation.

## Claim verdict / next falsifier

**DISCLOSED (paper algebra):** T1 and T2, with stated bounded sequence/phase/source domains. **OBSERVED (finite):** companion tests `test_signed_basel_tauberian.py` and the prior frame/Gamma tests. **UNVERIFIED / OPEN:** signed source-selected `o(1/A)` for `s=0`, all h or odd-eight h. **REFUTED:** inferring normality from the unphased identity zeta(2)=pi²/6 or source-free positive Gibbs traces. These statements are based on classical summation-by-parts and SUCC's already-defined operator realization; no external novelty or formal proof claimed.

**Next discriminating theorem:** Derive a genuinely source-locked cancellation inequality on the *signed* Basel tail trace using the original four-pole BBP source and the 2/3–CRT complementary phase, with the fixed wrong-seed and p-integral PPP-08 controls. A finite strict contrast is not enough; a bound `sup_(B>=A)|B_B(8k;0)|=o(1)` would be decisive for signed parity. The whole mode family is needed for normality.
