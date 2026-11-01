# Adaptive arctangent reciprocal frames: a uniformly conditioned original-BBP harmonic gate

**Research-only paper proofs, 2026-11-01.** Stack on SUCC PR #451 at `8ccec135f8abf64f0ea44fab555d9ac1e1b787e1`. New work here is an explicit *uniform* harmonic frame and a quantitative discrepancy transfer, not an all-horizon selected cancellation proof. π normality and RH remain OPEN. No new Lean/kernel or external scholarly-priority claim.

## 0. Source and objects (do not change)

For each positive integer n, the *original four signed poles* are

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{D(n)},\quad D(n)=(2n-1)(4n-1)(8n-7)(8n-3).
\]

The authentic orbit has `U_0=0`, `U_n=16U_{n-1}+r(n)` and `e(x)=exp(2πix)`. For `h>=1`, write

\[
A_N(h)=\frac1N\sum_{n=1}^{N}e(hU_n).
\]

The source `r(n+1)>0`, its decay, and the bound

\[
|A_N(16h)-A_N(h)|<\frac{2+165h/56}{N}\tag{0.1}
\]

are inherited from #451 AR-04 (derived by telescoping the exact original recurrence). The previous #451 chooses the *single* angle `θ=arctan r(2)`. Its mirror bound divides by `|sin(15hθ)|`. This is nonzero for every h, but has no uniform positive lower bound in h (see AAF-01).

## AAF-01: The fixed-axis conditioning obstruction is real

The inherited `γ=e^{2i arctan r(2)}=(819+106i)/(819-106i)` is not a root of unity in Q(i). Thus `15 arctan(r(2))/π` is irrational. Dirichlet's pigeonhole approximation (or density of an irrational circle rotation) gives arbitrarily large h with

\[
|\sin(15h\arctan r(2))|<\varepsilon.
\]

An exact **finite** counter-receipt occurs at `h=13`:

\[
\frac{\bigl(\Im(819+106i)^{195}\bigr)^2}{681997^{195}}<\frac1{400}.
\]

The inequality is verified by integer multiplication in the earlier mirror module (not a float). So the fixed irrational mirror's inverse condition number can grow without bound across harmonics, even though it is safe for each fixed h. This is an analytic conditioning boundary, not a contradiction of #451's normality equivalence.

## AAF-02: Exact source-polynomial brackets

Let `A(n)=120n²-89n+16` and `D(n)` above. For all `n>=2`:

\[
\frac{15}{64n^2}<r(n)<\frac8{15n^2},\qquad
\bigl((n-1)^2+1\bigr)r(n)>\frac15.\tag{2.1}
\]

For all `n>=8`:

\[
r(n)<\frac9{32n^2}.\tag{2.2}
\]

Here are complete **integer** positivity certificates (the order of coefficients is descending, t>=0):

1. `64n²A-15D` at `n=t+2` equals `9664t³+48328t²+80434t+44553`.
2. `8D-15n²A` at `n=t+2` equals `2296t⁴+11511t³+19418t²+11364t+576`.
3. `9D-32n²A` at `n=t+8` equals `768t⁴+18208t³+147976t²+442690t+248013`.
4. `5((n-1)²+1)A-D` at `n=t+3` equals `88t⁴+435t³+621t²+641t+1090`. At n=2 it equals 723.

Every coefficient is strictly positive. The independent `polynomial_oracle.py` constructs `A,D` from their original factors, multiplies and translates polynomials over **Z[t]**, and compares all resulting coefficients. This checks genuine polynomial identities, not finitely many samples or an unchecked symbolic text assertion.

For 0<=x<=2/15, the real principal arctan obeys

\[
\arctan x\ge x-x^3/3\ge \frac{671}{675}x.\tag{2.3}
\]

It follows directly by integrating `1/(1+t²)>=1-t²`. No complex branch transport is used.

## AAF-03: Original-source harmonic index and 1/8 frame theorem

For each positive integer h, write `h=16^v m` with `16∤m`. Define

\[
k(h)=\begin{cases}
\lceil\sqrt h\rceil,&v\text{ even},\\
\lceil2\sqrt h\rceil,&v\text{ odd},
\end{cases}\qquad
q_h=r(k(h)),\quad\theta_h=\arctan(q_h),\quad\varphi_h=h\theta_h.
\tag{3.1}
\]

**Theorem (uniform transverse mirrors).** For every h>=1,

\[
\boxed{|\sin(\varphi_{16h}-\varphi_h)|>\frac18.}\tag{3.2}
\]

**Proof:** For h with even v and h>=2, let k=ceil sqrt(h). Then k>=2, and `h>=((k-1)²+1)`. By (2.1)-(2.3),

\[
\varphi_h=h\arctan r(k)>\frac{671}{675}\,h r(k)>
\frac{671}{3375}.\tag{3.3}
\]

Also `h<=k²` and `(2.1)` give `φ_h<h*8/(15k²)<=8/15<π/2`. The one exceptional even-v frequency h=1 has `k=1`, `r(1)=47/15>1`, so

\[
\pi/4<\varphi_1=\arctan(47/15)<\pi/2.
\]

For h with odd v, h>=16, `k=ceil(2sqrt h)>=8`, and `k²>=4h`. Thus (2.2) yields

\[
0<\varphi_h<h r(k)<\frac9{32}\frac{h}{k^2}\le\frac9{128}.\tag{3.4}
\]

Multiplication by 16 toggles v parity. Therefore the angles φ_h and φ_16h lie on opposite sides of the gap

\[
\delta_0=\frac{671}{3375}-\frac9{128}
=\frac{55513}{432000}>\frac18,
\]

and both belong to `(0,π/2)`. For h=1 the larger-angle bound is even stronger, since `π/4>3/4>671/3375`. Hence

\[
\delta_0<|\varphi_{16h}-\varphi_h|<\pi/2.
\]

Sin is increasing on `[0,π/2]`, while its alternating Taylor bound gives

\[
\sin\delta_0\ge \delta_0-\delta_0^3/6
=\frac{61989274639109303}{483729408000000000}>\frac18.
\]

This proves (3.2) **for every positive integer h without approximation of π or a finite harmonic cutoff**. The source dependence is paid by (2.1)-(2.2); changing the forcing invalidates those certificates. □

## AAF-04: Exact two-quadrature reconstruction at ALL harmonics

For each h>=1 define ONE real signed scalar at that harmonic:

\[
B_N(h)=\frac1N\sum_{n=1}^N\sin(2\pi hU_n-\varphi_h)
=\Im(e^{-i\varphi_h}A_N(h)).\tag{4.1}
\]

For an arbitrary complex number z and two angles φ,ψ with sin(ψ-φ) nonzero, set `b_φ=Im(e^{-iφ}z)`, `b_ψ=Im(e^{-iψ}z)`. Exact elimination of `conj(z)` gives

\[
\boxed{z=\frac{b_\varphi e^{i\psi}-b_\psi e^{i\varphi}}{\sin(\psi-\varphi)}.}\tag{4.2}
\]

For z=A_N(h), φ=φ_h, ψ=φ_16h, let `w=A_N(16h)=z+E_N(h)`. The actual b_ψ differs from B_N(16h) by at most `|E_N(h)|`. Combining (4.2), AAF-03 and inherited (0.1) yields for **all N,h>=1**:

\[
\boxed{\displaystyle
|A_N(h)|<8\left(|B_N(h)|+|B_N(16h)|
+\frac{2+165h/56}{N}\right).}\tag{4.3}
\]

Unlike #451's fixed-angle mirror inequality, there is **no resonance-dependent denominator**. Crucially, `B_N(16h)` uses its OWN axis `θ_16h`, not the axis `θ_h`. Substituting a fixed mirror for both would change the determinant proof.

Thus the following are equivalent for the exact original source and literal U0=0:

\[
\boxed{\pi\text{ base-16 normal}\quad\Longleftrightarrow
\quad\forall h\in\mathbb Z_{>0},\ B_N(h)\longrightarrow0.}\tag{4.4}
\]

Right to left: (4.3) and Weyl criterion. Left to right: the original BBP Green telescope `U_n=16^n(pi/16)-T_n`, with bounded summable `T_n`, identifies the real-circle orbit's equidistribution with base-16 normality of π; hence every fixed signed sine projection tends zero. The BBP identity and Weyl criterion are prior inputs, not re-proved here.

## AAF-05: Quantitative growing-band discrepancy transfer

Let `D_N` denote supremum of the normalized interval discrepancy of the original first N circle states. Import the classical Erdős–Turán inequality with **some absolute** constant C_ET:

\[
D_N\le C_{ET}\left(\frac1{H+1}+\sum_{h=1}^H\frac{|A_N(h)|}{h}\right).
\]

Insert (4.3) and sum the source-error terms *exactly*:

\[
\boxed{\displaystyle
D_N<C_{ET}\left[
\frac1{H+1}
+8\sum_{h=1}^H\frac{|B_N(h)|+|B_N(16h)|}{h}
+\frac8N\left(2H_H+\frac{165H}{56}\right)
\right],}\tag{5.1}
\]

where `H_H=sum_{h=1}^H 1/h`. This is a quantitative conditional digit-distribution gate at simultaneous harmonics, not a proof that its signed sums vanish. In particular if some `H_N->infinity` with `H_N=o(N)` has the displayed weighted signed projection sum `o(1)`, then `D_N->0`.

For h<=H, every required source index is bounded by `k(16h)<=8sqrt H+1`, so the observer uses **O(sqrt H)** authentic source-time data to define all mirrors. If H=o(N), that source demand is o(sqrt N) and eventually fits within the observed N-step history. No hidden infinite-future source oracle is assumed for this finite band, although identifying the full original rational forcing remains separate.

## AAF-06: Exact Gaussian-integer phase transport

Write q_h=b_h/a_h in reduced positive integers. Each reflection is rational projective:

\[
J_h(t)=\frac{q_h-t}{1+q_h t},\quad
\begin{pmatrix}-a_h&b_h\\b_h&a_h\end{pmatrix}^2=(a_h^2+b_h^2)I.
\]

The signed observable is obtained from integer Gaussian powers:

\[
B_N(h)=\frac{\Im\big((a_h-ib_h)^h A_N(h)\big)}{(a_h^2+b_h^2)^{h/2}}.
\]

Similarly

\[
\sin^2(\varphi_{16h}-\varphi_h)
=\frac{\left[\Im\left((a_h-ib_h)^h(a_{16h}+ib_{16h})^{16h}\right)\right]^2}
{(a_h^2+b_h^2)^h(a_{16h}^2+b_{16h}^2)^{16h}}
>\frac1{64}.\tag{6.1}
\]

This lets a finite certificate verify the determinant with integer operations (and the exact rational square) for any declared finite h. The all-h theorem is AAF-03's polynomial argument, not a computational induction from finite Gaussian powers.

**Typed categorical reading:** these are a harmonic-indexed pair of observation maps on the SAME complex phase state, with different but source-attested reflection labels. Their determinant provides a uniform faithful two-coordinate observer. They are **not** a claim that a single invariant probability measure respects all these moving involutions, that a spatial Riemann-sphere rotation is a finite Hilbert Fourier transform, or that projective quotienting may erase its phase.

## AAF-07: Hostile controls and unpurchased proof debt

- The **fixed-axis** PR #451 source-native mirror is infinitely often ill-conditioned as h grows (AAF-01); finite exact h=13 proves even a ≥1/20 universal lower bound false for that old angle.
- The **new adaptive frame** holds for arbitrary complex A_N and therefore for coherent/non-normal sources too, *provided the source supplies the authenticated E_N(h) error budget*. The frame does not force B_N(h)->0.
- Nonselected same-four-pole changed real seed `s=1/5-pi/16` (irrational, NOT an original finite rational-register state) has `A_N(h)->e(h/5)`. The pair of well-conditioned projected limits cannot both vanish; it is a valid real-circle hostile comparator.
- Source mutants sharing a few r(n) do not inherit the full all-n polynomial certificates. A fake forcing with the same first k samples is not an all-horizon original-four-pole source identity.
- The real-signature projection is not a positive norm or a Haar-energy estimate. The missing estimate is a signed, source-selected all-horizon limit of `B_N(h)` (or stronger Fejér signed-lag bound).
- The adaptive angular labels are generally not elements of SUCC's finite odd-Q root-of-unity register. Use the complexified phase/continuous-circle fiber when multiplying non-torsion Gaussian-rational angular factors.

See also [FINITE_OBSERVER_BARRIER.md](FINITE_OBSERVER_BARRIER.md) (AAF-08): an explicit positive, strictly decreasing source agrees on every finite window and all sampled mirror labels, while completing to a rational nonnormal point. It changes the original four-pole law beyond the matched window and cannot be invoked against a proof that uses that law globally.

**Verdict:** A uniformly conditioned, source-constructible, rational-projective, one-real-observable-per-harmonic criterion, plus a quantitative discrepancy inequality. No unconditional cancellation, π normality, RH or physical quantum interpretation.

## External mathematical provenance

- NIST DLMF §§4.23–4.24: arctangent principal branches and alternating expansion: https://dlmf.nist.gov/4.23 and https://dlmf.nist.gov/4.24
- Classical Weyl equidistribution criterion and Erdős–Turán discrepancy inequality; the latter imported with an unspecified absolute constant. Yukio Ohkubo, *Notes on Erdős–Turán inequality*, J. Austral. Math. Soc. A 67 (1999), 51–57, DOI:10.1017/S1446788700000860. No academic priority claim for that classical tool.
- Inherited SUCC main XVIII + draft PR #451: original source, signed lag and mirror projections. Main proof-status ledger unchanged.
