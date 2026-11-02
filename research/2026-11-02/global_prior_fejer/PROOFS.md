# Global-first Fejér gate: bounded energy, not near-Haar purity

**2026-11-02 · RESEARCH ONLY · exact conditional theorems, NO π-normality proof.**
Stacked on Pisot × Gamma draft #470, exact parent b682b1f8ea21a1ae1efd529b6011e87453a7e0b6; ancestors #468 → #465 → #461 → Main XIX. Sibling #469 examined but not merged. Original four signed BBP poles and literal U_0=0 unchanged. This is a scoped refinement of SUCC's earlier Fejér/Gram identity (PR #296, IMW) and authentic cylinder/collision criterion (PR #407); do not claim independent invention of Fejér kernels, normality criteria or unique absolutely continuous invariant measures.

## GF-01. Start with the GLOBAL real circle before selecting finite observations

Let α=π/16 and x_n={16^n α} on T=R/Z. Define e(t)=exp(2πit), c_N(m)=N^{-1}Σ_{n=0}^{N-1}e(m x_n), and the nonnegative Fejér kernel

\[
F_H(t)=\frac{1}{H+1}\left|\sum_{j=0}^{H}e(jt)\right|^2
=\sum_{|m|\le H}\left(1-\frac{|m|}{H+1}\right)e(mt).
\]

Its authentic completed-orbit energy is

\[
\boxed{\mathcal E_{N,H}(\alpha)=\frac1{N^2}\sum_{n,k<N}F_H(x_n-x_k)
=1+2\sum_{m=1}^{H}\left(1-\frac m{H+1}\right)|c_N(m)|^2\ge1.}
\]

This is the same classical positive spectral purity as the earlier SUCC internal Fourier matrix: for dimension H+1, tr(A²)/(H+1)=\mathcal E_{N,H}. The source-specific unknown is a UNIFORM upper bound for the selected α, not the identity or positivity. A Haar prior assigned to the ambient circle is not evidence that this orbit approaches Haar.

## GF-02. Exact radix Ward ladder converts ANY constant energy cap into fixed-h decay

The expanding-circle dynamics gives the exact telescoping identity

\[
c_N(16^k h)=N^{-1}\sum_{n=k}^{N+k-1}e(h16^n\alpha),
\quad |c_N(16^k h)-c_N(h)|\le 2k/N
\]
for integer h≠0 and 0≤k≤N. Fix any integer K with 1≤K≤N and 2|h|16^{K-1}≤H. Every weight on the frequencies |h|16^k is at least 1/2. Therefore

\[
\mathcal E_{N,H}-1\ge\sum_{k=0}^{K-1}|c_N(16^k h)|^2,
\]

and triangle inequality plus Cauchy–Schwarz give the **effective bound**

\[
\boxed{|c_N(h)|\le\sqrt{\frac{\mathcal E_{N,H}-1}{K}}+\frac{K-1}{N}.}\tag{GF-02}
\]

No independence, spectral randomness, physical quantum analogy, original-source positive covariance, or per-node signed Haar loss is assumed. Notice that even a cap \mathcal E≤1000 works; it NEED NOT approach 1.

If some deterministic H_N→∞ satisfies sup_{N≥N_0}\mathcal E_{N,H_N}(\alpha)≤C<∞, take
K_N=min(floor(log_16(H_N/(2|h|)))+1,floor(sqrt N)), after omitting finitely many N. Then K_N→∞ and K_N/N→0 for every FIXED nonzero h, so c_N(h)→0. Classical Weyl proves base-16 normality of π. For H_N=floor(sqrt N), K_N=0.5 log_16 N+O_h(1) and the explicit conditional rate is O_{h,C}((log N)^{-1/2}).

**Quantifier firewall:** this is a proven implication with an UNPROVED selected-source energy premise. It does not assert that the original π energy is bounded for unbounded N. A predetermined bandwidth such as floor(sqrt N) is stronger than mere normality; a slowly growing EXISTENTIAL bandwidth with energy ≤2 eventually is equivalent to normality by the diagonal argument below.

## GF-03. Why the bounded-energy gate is a genuinely weaker sufficient target

IMW (#296) proposed tr(A²)=H+o(H), namely Fejér energy→1, for growing bandwidths. The GF-02 gate needs only tr(A²)=O(H). The improvement is valid because the selected target is a single expanding T_16 orbit, not an arbitrary sequence of phases. Shift-invariant weak limits have Fourier coefficients fixed along h,16h,16²h,...; a bounded L² Fourier budget forces those coefficients to vanish.

Conversely, if π is normal, for each fixed finite H, \mathcal E_{N,H}→1. By diagonal selection there EXISTS a nondecreasing H_N→∞ with \mathcal E_{N,H_N}≤2 for all sufficiently large N. This is an equivalence of criteria, NOT an algorithm to choose a certified scale from the original source, and NOT a new proof. A source-independent sequence of unit phases does not obey the radix Ward ladder; the relaxation cannot simply be applied to every SUCC Fourier construction.

## GF-04. Exact Gamma-to-finite rational energy transport

Keep exactly
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
Set α_B=Σ_{j=1}^{B}16^{-j}r(j)∈Q, and C_B=(8B+1)(8B+2). Inherited #465/#468 positive Beta/Gamma theorem proves

\[
0<\alpha-\alpha_B\le16^{-B}/C_B.
\]

Define the exact finite, source-selected rational orbit y_n={16^n α_B} and its Fejér energy \mathcal E_{N,H}(α_B). For B≥N≥1,

\[
|c_N(m;\alpha)-c_N(m;\alpha_B)|
\le\frac{2\pi|m|}{15NC_B}16^{N-B}.
\]

Using |\,|z|²-|w|²\,|≤2|z-w| for unit-averaged characters and Σ_{m=1}^H m(1-m/(H+1))=H(H+2)/6 yields

\[
\boxed{|\mathcal E_{N,H}(\alpha)-\mathcal E_{N,H}(\alpha_B)|
\le\frac{4\pi H(H+2)}{45NC_B}16^{N-B}.}\tag{GF-04}
\]

For the particularly economical choice B=N and H=floor(sqrt N), the error is O(N^{-2}). With the classical upper bound π<22/7, the right-hand side has a pure **rational strict upper bound**
88 H(H+2)/[315 N C_B 16^{B-N}].
This is a bound on completed-orbit spectral energy, not only fixed-h phases; it uses the SOURCE-SPECIFIC exact rational cutoff, not external digits of π.

Thus the genuinely FINITE arithmetic target

\[
\boxed{\sup_{N\ge N_0}\frac1{N^2}
\sum_{n,k<N}F_{\lfloor\sqrt N\rfloor}
(16^n\alpha_N-16^k\alpha_N)<\infty}\tag{GF-GATE}
\]

would, via GF-04 + GF-02, prove base-16 normality of π. **GF-GATE is OPEN.** Its expression is positive but its difficult off-diagonal pair interactions preserve the selected original source/carry; mere positivity is not an upper bound.

## GF-05. Transport to the literal zero-seeded rational BBP orbit

From the original positive Green tail U_n=16^nα-T_n for n≥0, T_0=α and 0<T_n≤1/(64n²) for n≥1, hence Σ_{n≥0}T_n≤α+π²/384. For each fixed h,

\[
\left|\frac1N\sum_{n<N}e(hU_n)-c_N(h;\alpha)\right|
\le\frac{2\pi|h|}{N}\left(\frac\pi{16}+\frac{\pi^2}{384}\right).
\]

This O_h(N^{-1}) source-faithful bridge makes the completed α gate equivalent to the literal U_0=0 Weyl gate. It is inherited Green transport, not a new cancellation estimate. Do not confuse finite 2-adic source-local Haar (#469) with real-circle Fejér boundedness.

## GF-06. Hostile controls and limitations

1. Keep the SAME original four poles but change only the real seed to s=1/5−α. Its completed circle orbit is x_n=16^n/5=1/5 mod1; then \mathcal E_{N,H}=F_H(0)=H+1 exactly. Therefore positivity, Gamma derivatives, exact finite source sewing and both Pisot conjugate formulas do NOT imply GF-GATE.
2. The rational completed seed 1/7 gives a three-atom periodic orbit. Its energy grows linearly in H rather than staying bounded, despite nontrivial lag separation; a single-lag lower bound does not imply this global energy cap.
3. A local 16-adic permutation observer is Haar on its own finite carrier (#469) but need not have bounded REAL Fejér energy; the entire real phase is in the cofiber.
4. Original pi arithmetic is unresolved in the off-diagonal pair upper bound. Numerical finite samples cannot be extrapolated.
5. The proof makes no statement about RH, Weil positivity, normality in every base, physics, or computation speedup.

**Claim ledger:** GF-01/02 = classical algebra plus this scoped constant-cap criterion, paper derivation; GF-03 = conditional / equivalence proof; GF-04 = paper-proved source transport, using inherited Gamma inequality; GF-05 = inherited Green transport; GF-06 = exact countermodels; GF-GATE = **UNVERIFIED/OPEN**. The paper proofs and local tests are not a Lean receipt or independent referee. 
