# Two completions, one BBP source: an exact 2-adic zero, a Haar source graph, and the real π invariant

**2026-11-06 — original-source research.** Scope: original four signed Bailey–Borwein–Plouffe rational poles, literal `U_0=0`, arithmetic of the real completion and the 2-adic integer clock. `PROVED LOCAL` below denotes elementary proofs in this dossier, NOT Lean, externally established priority, physical quantum dynamics, or π-normality.

## 0. The specific source and the invariant the observer sees forever

Let `b=16` and for integer n≥1 define

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{A(n)}{D(n)},\quad
A(z)=120z^2-89z+16,\quad
D(z)=(2z-1)(4z-1)(8z-7)(8z-3).
\]

Let `U_0=0`, `U_{n+1}=16U_n+r(n+1)`. For REAL n≥0 define the absolutely convergent future tail

\[
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad 16T_n=r(n+1)+T_{n+1}.
\]

Original BBP gives `T_0=π/16`. Consequently

\[
\boxed{16^{-n}(U_n+T_n)=T_0=\pi/16\quad\text{for every }n\ge0.}\tag{DB1}
\]

Thus `16^{-n}U_n=sum_{j=1}^n16^{-j}r(j)` increases to π/16 (r(j)>0). For n≥1, the original SUCC source bound `T_n<1/[15(n+1)^2]` yields an explicit rational-prefix gap

\[
0<\frac\pi{16}-16^{-n}U_n<\frac{16^{-n}}{15(n+1)^2}.\tag{DB2}
\]

DB1 is already latent in SUCC #521 and #525; we are *reinterpreting* it as an invariant of the fully realized source+observer system, not claiming priority. The normalized, unwrapped value is fixed while `\{U_n+T_n\}` exposes successive hexadecimal digits. The modulo-one projection drops the integer carry, NOT the globally conserved source-completed value.

## 1. A genuinely different source completion in Z₂ — PROVED LOCAL

`D(z)` is odd (a 2-adic unit) for EVERY `z in Z_2`, so `r(z)=A(z)/D(z)` extends to a 1-Lipschitz rational analytic function `Z_2 -> Z_2`. Define the **past-directed 2-adic completion**

\[
\boxed{V(z)=\sum_{j=0}^{\infty}16^j r(z-j),\qquad z\in\mathbb Z_2.}\tag{DB3}
\]

Since `|16^j|_2=2^{-4j}` and `r(Z_2) subset Z_2`, DB3 converges uniformly, is 1-Lipschitz, and obeys

\[
\boxed{V(z+1)=16V(z)+r(z+1).}\tag{DB4}
\]

**Uniqueness:** If `W:Z_2 -> Z_2` is any other (not necessarily continuous) solution of DB4 for ALL z in Z₂, then `E=W-V` satisfies `E(z)=16^m E(z-m)` for every `m>=0`. As `E(z-m) in Z_2`, `E(z)` belongs to `intersection_m 16^m Z_2={0}`. Hence W=V. Uniqueness refers to *entire 2-adic clock* solutions valued in Z₂, NOT real circle trajectories.

## 2. The authentic, literal zero-seed equals the 2-adic entire-clock boundary — PROVED LOCAL

**Theorem DB5:**

\[
\boxed{V(0)=\sum_{j=0}^{\infty}16^j r(-j)=0\quad\text{in }\mathbb Q_2.}\tag{DB5}
\]

*Exact 2-adic logarithmic proof.* The original four poles at negative indices give the convergent source sum

\[
V(0)=\sum_{j\ge0}16^j\left(\frac{-4}{8j+7}+\frac2{8j+4}+\frac1{8j+3}+\frac1{8j+2}\right).
\]

Define the formal antiderivative `F(0)=0` over Q₂ by the convergent power series

\[
F(x)=\sum_{j\ge0}16^j\left(
-\frac{4x^{8j+7}}{8j+7}+\frac{2x^{8j+4}}{8j+4}
+\frac{x^{8j+3}}{8j+3}+\frac{x^{8j+2}}{8j+2}\right).
\]

At `x=1` it equals V(0). Its **exact rational derivative**, verified by a differently implemented SymPy oracle, is

\[
\begin{aligned}
F'(x)&=\frac{-4x^6+2x^3+x^2+x}{1-16x^8}\\
&=\frac{x}{2(1-2x+2x^2)}+\frac{x}{2(1-2x^2)}.
\end{aligned}\tag{DB6}
\]

Work in `K=Q_2(i)`, where `i^2=-1`, and put `a=1+i`, `b=1-i`, `Q(x)=1-2x+2x²=(1-ax)(1-bx)`. Since `v_2(a)=v_2(b)=1/2`, all power-series logarithms `log(1-ax)` and `log(1-bx)` converge for `x in Z_2`; likewise `log(1-2x²)`. An antiderivative with zero constant term is

\[
\begin{aligned}
F(x)={}&\tfrac18\bigl[\log(1-ax)+\log(1-bx)\bigr]\\
&+\tfrac1{8i}\bigl[\log(1-bx)-\log(1-ax)\bigr]
-\tfrac18\log(1-2x^2).
\end{aligned}\tag{DB7}
\]

Differentiate DB7 to recover DB6 exactly. At `x=1`, `1-a=-i`, `1-b=i`, and `1-2x²=-1`. These are torsion units of orders 4,4,2, and the convergent 2-adic logarithm of each is **exactly zero**: `m log(ζ)=log(ζ^m)=0` for a root of unity ζ of order m. Hence `F(1)=0`, proving DB5. There is NO appeal to finite modular testing or to a real/2-adic identification of π.

**Consequence:** For n≥0, both `V(n)` and the original rational forward history `U_n(0)` solve DB4 on the nonnegative integers and start at zero. Therefore

\[
\boxed{U_n(0)=V(n)\text{ in }\mathbb Z_2\quad\forall n\ge0.}\tag{DB8}
\]

Thus the original zero-seeded rational history has a UNIQUE continuous, source-compatible interpolation to the **entire 2-adic integer clock**. It is not a claim that physical elapsed time extends to all 2-adic integers.

## 3. Stronger: the actual original BBP history is exactly Haar-equidistributed in the 2-adic carrier — PROVED LOCAL

**Theorem DB9 (isometry).** For distinct `x,y in Z_2`,

\[
\boxed{|r(x)-r(y)|_2=|x-y|_2,\qquad |V(x)-V(y)|_2=|x-y|_2.}\tag{DB9}
\]

*Proof.* `D(z)` is odd and `D(x)-D(y)` is divisible by `2(x-y)` because each linear denominator factor has even slope. Also

\[
\frac{A(x)-A(y)}{x-y}=120(x+y)-89\equiv1\pmod2.
\]

The divided difference of `r` is therefore an odd unit: the term from A has odd residue, and the term from D has even residue. Thus `r` is a 2-adic isometry. From DB3,

\[
V(x)-V(y)=\bigl(r(x)-r(y)\bigr)
+\sum_{j\ge1}16^j\bigl(r(x-j)-r(y-j)\bigr).
\]

The first term has 2-adic valuation `v_2(x-y)`; the sum has valuation at least `v_2(x-y)+4`. By the ultrametric inequality the leading valuation cannot cancel, so V is an isometry. Consequently each induced map `V mod 2^k` is a permutation of Z/(2^k).

Because `U_n=V(n)` for every nonnegative n, **every consecutive block of 2^k original BBP times visits each possible 2-adic state residue exactly once**. In particular, for any `a mod 2^k` and any N≥1,

\[
\boxed{\left|\#\{0\le n<N:U_n\equiv a\pmod{2^k}\}-\frac{N}{2^k}\right|<1,}\tag{DB10}
\]

with exact equality zero when `2^k|N`. Thus the authentic zero-seeded rational BBP states are unconditionally Haar-generic in Z₂, with a finite-count discrepancy <1 for every fixed 2-power residue observation. This is a **2-adic distribution theorem**, NOT the still-open Archimedean base-16 normality of π.

## 4. Where the 2x+1 analogy is exact — and where it breaks

For odd integer m under `m -> 2m+1`, the shifted coordinate `y=m+1` satisfies `y' = 2y`, so

\[
\boxed{m_t+1=2^t(m_0+1),\quad m_t\to-1\text{ in }\mathbb Z_2,\quad m_t\equiv1\pmod2.}\tag{DB11}
\]

After four consecutive odd updates, `m_{t+4}+1=16(m_t+1)`. BBP has the **same homogeneous difference dynamics**: for two seeds `s,s'` with the SAME original forcing,

\[
\boxed{U_n(s)-U_n(s')=16^n(s-s').}\tag{DB12}
\]

This is an exact conjugacy of the homogeneous difference channels, NOT an equivalence of the full systems, not Collatz, and not a proof of real circle mixing. For rational nonzero `q=s-s'`, the opposite local metrics yield the balanced identity

\[
|16^n q|_\infty |16^nq|_2=|q|_\infty|q|_2.
\]

Example `q=1/5`: the difference tends to zero in Z₂ at rate `2^-4n` but the real-circle fractional difference is constantly `1/5` because `16^n≡1 (mod 5)`. Erasure in one observer topology is NOT erasure of the joint source/history information.

## 5. The crucial hostile test: 2-adic Haar + zero boundary does NOT force real Haar — REFUTED implication

Let `H(z)=z/(2z-1)^4`, which is an isometry of Z₂ (odd divided difference) and tends to ZERO in the usual real topology at positive integers. Define a **different** rational source

\[
\widetilde r(n)=H(n)-16H(n-1),\quad \widetilde U_0=0.
\]

Then `\widetilde U_n=H(n)` exactly. The unique 2-adic entire-clock completion of `\widetilde r` is `\widetilde V(z)=H(z)`, so `\widetilde V(0)=0` and `\widetilde U_n mod2^k` permutes ALL residues at every k. Nevertheless `\widetilde U_n\to0` in R, so its real fractional phases approach the fixed point 0. They are emphatically **not** Haar. This source has decaying rational terms and odd denominators but is signed and is NOT the original four-pole BBP source.

**Status:** The universal inference `zero 2-adic boundary + exact 2-adic Haar => real-circle Haar` is REFUTED by this complete model; the genuine original-source π-normality problem is not refuted.

## 6. Gauge redundancy: even BOTH boundaries and 2-adic Haar fail to identify a source — PROVED LOCAL / source-uniqueness REFUTED

Let any `H:Z_2->Z_2` be bounded and admit a real-decaying rational sequence `H(n)` for n≥0 with `H(0)=0`. Define the discrete source coboundary

\[
\delta r(n)=H(n)-16H(n-1),\quad r_H(n)=r(n)+\delta r(n).
\]

When both tails converge in R,

\[
\boxed{U^H_n=U_n+H(n),\quad T^H_n=T_n-H(n),\quad V_H(z)=V(z)+H(z).}\tag{DB13}
\]

Proof: finite telescoping in BOTH orientations; the boundary terms disappear in their respective topologies. The preserved initial condition is `U_0^H=U_0` when `H(0)=0`. Thus `16^-n(U^H_n+T^H_n)=π/16` and `V_H(0)=0`. If `H(n)→0`, the completed circle phases are IDENTICAL, and the raw real-phase normality verdict is unchanged.

The explicit `H(z)=z/(2z-1)^4` is such a nonzero gauge. Furthermore choose `H_even=2H`; its difference quotient is divisible by 2, so `V+2H` is still a Z₂-isometry. The **non-original** modified source `r+2H(n)-32H(n-1)` therefore preserves (a) the real π invariant, (b) literal U₀=0, (c) the exact 2-adic zero boundary, (d) full 2-adic Haar distribution, and (e) the real-completed circle orbit. It is a decisive counterexample to calling those five properties a unique fingerprint of the four signed BBP poles. Exact pole-level source authentication remains a separate requirement.

## 7. What would actually change π normality?

The newly proved Z₂ Haar theorem is **not** a signed real Weyl bound. The real-circle character for the single original zero-seeded orbit remains

\[
W_A(h)=A^{-1}\sum_{n=A}^{2A-1}e^{2\pi i h U_n(0)}\quad (h\ne0),
\]

and `W_A(h)->0` remains OPEN for each fixed nonzero h. An extra **cross-place** hypothesis would have to connect distributions of `U_n mod2^k` to distributions of fractional real phases while retaining exact source-and-carry chronology. DB10 alone cannot do this, as §5 shows.

**Next decisive probe:** preregister a proposed cross-place inequality, including the exact source rational poles and zero initial seed, which implies a nontrivial bound for W_A(h); require it to fail the H(n) shadow control, the irrational coherent `β=1/5` real completion, and source-coboundary gauge mutants as appropriate. The transport must not identify real π with a 2-adic number or use physical quantum language without an operational basis.

**Provenance:** Original Bailey–Borwein–Plouffe (1997) formula; SUCC #521 (source and selected tail), #522 (history and observer), #525 (real realization gyroscope), #526 (joint source entropy). All copied formulas are rederived as elementary identities; no claim of worldwide priority. Source-original files, historical contracts, `formal/` and main are untouched.
