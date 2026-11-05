# Critical-Chirp Ratchet: the sharp coherent high-frequency threshold

**Research dossier (2026-11-04).** Parent: Gamma Prybar PR #501 at `af5c7ba30ea57d725bd334310798357d50f12fce`. This is an additive research child. It **does not prove π base-16 normality, a zero-seed signed estimate, or RH**. Scope is the authentic four-pole forcing with the deliberately wrong, same-forcing coherent real seed `s_*=-π/16`. All statements below have paper derivations, exact-rational source checks and separately labeled noncertifying integral quadrature; no new Lean authority or external independent referee.

## Contracts and one dimensionless target

The original genuine source is

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Set `α=π/16` (the independently authenticated BBP completed boundary), and let

\[
 T_n=\sum_{k\ge1}16^{-k}r(n+k),\quad U_n(0)=16^n\alpha-T_n.
\]

For an **arbitrary seed** `s`, `U_n(s)=16^n(s+α)-T_n`. The special *counterseed* `s_*=-α` gives `U_n(s_*)=-T_n`, **not** the original. For integer H≠0 and integer A≥2 write

\[
 M_A^{(s)}(H)=\frac1A\max_{A\le a<b\le2A}\left|\sum_{n=a}^{b-1}e(HU_n(s))\right|,\qquad e(x)=e^{2\pi i x}.
\]

The parent's F4 paper theorem says for fixed `h≠0` and `H=|h|16^j≤A³`:

\[
 M_A^{(0)}(h)\le j/A+(1+C H/A^2)M_A^{(0)}(H).
\]

The intended critical depth is `j=floor(log_16(A² log A/|h|))`, so `Λ_A=H/A²∈(log A/16,log A]`. Its **OPEN sufficient gate** is the original-source `Λ_A M_A^{(0)}(H)→0` for each fixed `h≠0`. This statement is a direct normalization of inherited F4, **not a new source-selected cancellation estimate**. We quantify the coherent wrong-seed obstruction to this exact gate.

## CC-01: globally uniform, explicit positive Green-tail error (paper PROVED)

The original signed source has the positive Mellin density

\[
 r(n)=\int_0^1 t^{8n-8}(1-t)B(t)\,dt,\qquad
 B(t)=(t²+2)(t²+2t+2)=t⁴+2t³+4t²+4t+4.
\]

By monotone convergence,

\[
 T_n=\int_0^1 t^{8n}(1-t)F(t)\,dt,\quad F(t)=\frac{B(t)}{16-t^8}.
\]

For `t∈[0,1]`, `0<F(t)≤1`, `F(1)=1`, `0≤B′(t)≤22`, `B(t)≤15`, and `16−t⁸≥15`, so

\[
 0\le F'(t)=\frac{B'(t)}{16-t^8}+\frac{8t^7B(t)}{(16-t^8)^2}
 \le\frac{22}{15}+\frac{120}{225}=2.
\]

Therefore `0≤1−F(t)≤2(1−t)` and elementary beta integrals yield

\[
 0<\frac1{(8n+1)(8n+2)}-T_n
 <\frac4{(8n+1)(8n+2)(8n+3)}.
\]

Finally

\[
 0<\frac1{64n²}-\frac1{(8n+1)(8n+2)}
 =\frac{24n+2}{64n²(8n+1)(8n+2)}
 \le\frac{26}{4096n³}.
\]

The previous beta correction is `≤32/(4096n³)`. Since `26+32<64`, for **every integer n≥1**,

\[
 \boxed{0<\frac1{64n²}-T_n<\frac1{64n³}.}\tag{CC-1}
\]

This is an explicit analytic uniform estimate, not a numerically fitted rate. It allows an exact comparison with the leading model without ever generating π digits.

## CC-02: sharp maximal coherent chirp with explicit leading constant (paper PROVED)

**Theorem.** Let `(A,H_A)` be any integer epochs `A→∞` and positive integer frequencies. Put

\[
 \Lambda_A=H_A/A²,\qquad \Lambda_A\to\infty,\qquad \Lambda_A²/A\to0.
\]

Then the genuine four-pole recurrence with the changed coherent seed `s_*=-π/16` has

\[
 \boxed{M_A^{(s_*)}(H_A)=\frac{256}{\pi\Lambda_A}
 +O(\Lambda_A^{-2}+\Lambda_A/A),}\tag{CC-2}
\]

and in particular

\[
 \boxed{\lim_{A\to\infty}\Lambda_A M_A^{(s_*)}(H_A)=\frac{256}{\pi}.}\tag{CC-3}
\]

The big-O is uniform for the stated regime, with absolute constants. The result holds along any sequence of epochs (including dyadic) and integers H satisfying the hypotheses; it is not a theorem about the zero-seeded orbit.

**Proof.** By CC-1, uniformly on the epoch,

\[
 |e(-H T_n)-e(-H/(64n²))|\le2\pi H/(64 A³)=\pi\Lambda/(32A).
\]

Let `μ=Λ/64` and `g_μ(u)=e(-μ/u²)` on `[1,2]`. For each contiguous discrete index interval, the normalized sum of `g_μ(n/A)` differs from its exact mesh-aligned integral by at most `2πμ/A` using `|g_μ'(u)|≤4πμ`. Thus the maximal source sum differs from the maximal continuous integral

\[
 \mathcal M(\mu)=\sup_{1\le a<b\le2}\left|\int_a^b g_\mu(u)du\right|
\]

by `O(Λ/A)` (including the `O(1/A)` rounding of continuous endpoints).

Twice integrate by parts, using `g_μ'(u)=(4π iμ/u³)g_μ(u)`, to obtain uniformly for all `a,b`:

\[
 \int_a^b g_\mu(u)du=
 \left[\frac{u³}{4\pi i\mu}g_\mu(u)\right]_a^b+O(\mu^{-2}).
\]

The endpoint difference is at most `(a³+b³)/(4πμ)≤4/(πμ)`. For a matching lower bound take `b=2` and

\[
 a=2(1+2/\mu)^{-1/2}.
\]

For sufficiently large `μ`, `a∈[1,2)` and `μ/a²−μ/4=1/2`, so `g_μ(a)=−g_μ(2)`. The endpoint modulus is `(8+a³)/(4πμ)=4/(πμ)+O(μ^{-2})`. Hence

\[
 \mathcal M(\mu)=4/(\pi\mu)+O(\mu^{-2}).
\]

Substituting `μ=Λ/64` and the source/mesh errors gives CC-2. Multiplying by Λ gives `256/π+O(Λ^{-1}+Λ²/A)`, which proves CC-3 in the declared regime.

**Numerical calibration is separate from this proof.** The independently performed fixed-μ half-turn quadrature at μ=8,32,128 confirms convergence of `μ|∫_a² e(-μ/u²)du|` towards `4/π`; it is not used to prove the upper bound or the limit.

## CC-03: exact margin at the parent F4 critical radix frequency (paper PROVED; obstacle)

For fixed integer `h≠0`, define

\[
 j_A=\left\lfloor\log_{16}\frac{A²\log A}{|h|}\right\rfloor,\qquad H_A=|h|16^{j_A}.
\]

For all sufficiently large `A`, `\Lambda_A=H_A/A²∈(\log A/16,\log A]`, and CC-3 applies. Consequently

\[
 \boxed{\frac{H_A}{A²}M_A^{(s_*)}(H_A)\longrightarrow\frac{256}{\pi}\ne0.}\tag{CC-4}
\]

The parent F4 gate demands the **same expression tends to zero** at the actual source seed `0`. Thus no argument using only the four-pole forcing shape, the prime support, and seed-independent high-frequency dephasing can supply F4's chosen-depth saving: the coherent seed falsifies it.

This *calibrates* the necessary saving. It neither proves that the original zero seed has it nor that `256/π` is universal over arbitrary seeds.

**Finite-regime warning:** because the prefactor is large, numerical epochs at `A≤10^6` and `H≈A²log A` are nowhere near the limiting asymptotic for the coherent control. For example `Λ≈log A` remains much smaller than `256/π≈81.49`. Finite experiments should calibrate the oscillatory integral at large independent `μ` or use explicit rigorous errors, not mistake high coherence for a contradiction.

## CC-04: finite exact nonasymptotic coherent obstruction (paper PROVED)

A separate original-source integral bound gives for all `n≥1`:

\[
 0<T_n-T_{n+1}\le\frac{16}{(8n+1)(8n+2)(8n+3)}<\frac1{32n³}.
\]

Indeed `r(s)-r(s+1)≤240/[(8s−7)(8s−6)(8s−5)]` from its positive moment integrand and `1−t^8≤8(1−t)`; sum the 16-adic tail and use `s=n+k`.

For `H=A²Λ` and any integer block length `1≤m≤min(A, floor(4A/Λ))`, the phases `−HT_n` on **any m consecutive epoch indices** lie in an interval of length at most `H(m−1)/(32A³)<1/8` cycles. Rotating the midpoint of that arc gives

\[
 \boxed{M_A^{(s_*)}(H)\ge\frac{m}{A}\cos(\pi/8)>\frac{m}{2A}.}\tag{CC-5}
\]

This is an all-finite rationally bounded lower certificate; tests check source values and its exact phase-span inequality, not a numerical value for cosine.

## What these results do *not* establish

- No asymptotic cancellation for original `U0=0`, no theorem approaching π normality, and no physical randomness/entanglement inference.
- Replacing `U_n` by the coherent seed retains the exact genuine `r(n)` but changes the global source-selected boundary; a proof exploiting that boundary may still work.
- F1's many-depth Bessel estimate can make **some** high coefficient small but does not identify the exact chosen critical depth or prove a `o(A²/H)` rate there.
- The quotient `Λ_A M_A(H_A)` is a useful diagnostic because CC-3 assigns the coherent obstruction an exact nonzero constant. It is not a new unconditional source-selected inequality.

**Next lamp:** derive an explicit arithmetic sign/carry/cofactor identity that makes the actual zero-seeded critical quotient tend to zero while the coherent and radial controls remain nonzero. Demand independent source oracles, preregistered holdouts and proof of the asymptotic, not only finite numerical trends.
