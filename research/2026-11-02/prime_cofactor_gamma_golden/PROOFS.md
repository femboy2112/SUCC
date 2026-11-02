# OPERATION PRIME–COFACTOR × GAMMA–GOLDEN: original-source circle collision gate

**2026-11-02 · RESEARCH ONLY · Paper derivations, not π normality.**
Parent [#471](https://github.com/femboy2112/SUCC/pull/471) at SHA 92f7d4684a1ec68bf0346e0e74ec763e03d8c3b4; inherited #470, #468, #465, #461 and Main XIX. The parallel 2-adic/real PR #469 is context only. Preserve the original four BBP signed poles, literal zero seed, production, formal/Lean, historical archives and main.

## The single selected-object target

Put \(e(x)=\exp(2\pi ix)\). Use the authentic signed original forcing and initial state

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Let \(\alpha_N=\sum_{j=1}^N16^{-j}r(j)\in\mathbb Q\), \(\alpha=\pi/16\), and

\[
F_{M-1}(t)=\frac1M\left|\sum_{j=0}^{M-1}e(jt)\right|^2,\quad
N=L^2,\quad M=L+1,\quad
\mathscr Q_L=\frac1{N^2}\sum_{n,m<N}F_{M-1}(16^n\alpha_N-16^m\alpha_N).
\]

Parent GF-07 proves the **conditional** implication \(\sup_L\mathscr Q_L<\infty\Rightarrow\pi\) base-16 normal via exact Gamma energy transport and the radix Ward/Fejér ladder. No bound on this selected source is proved yet.

## PGC-01. Exact long newborn-prime clean interval and first reinjection

Let \(p=8k+1>5\) be prime, \(b=k+1\). No denominator in \(r(j)\), \(j<b\), is divisible by \(p\). At birth:

\[
U_b=\frac4p+B_0,\quad B_0=16U_{b-1}-\frac2{p+3}-\frac1{p+4}-\frac1{p+5}\in\mathbb Z_{(p)}.
\]

**Original-source theorem:** for **every** \(0\le t<3k\),

\[
\boxed{U_{b+t}=\frac{4\,16^t}{p}+B_t,\quad B_t\in\mathbb Z_{(p)},\quad B_{t+1}=16B_t+r(b+t+1).}
\tag{PGC-01}
\]

The exact clean interval is \(n\in[k+1,4k]\), of length \(3k\). Proof: the four denominator forms lie in residue classes \(1,4,5,6\bmod8\); since \(p\equiv1\bmod8\), their first multiples following the initial first-pole \(p\) are \(9p,4p,5p,6p\), occurring at \(n=9k+2,4k+1,5k+1,6k+1\), respectively. No secondary \(p\)-divisible source denominator occurs earlier. Therefore in \(\mathbb Z_{(p)}\),

\[
\boxed{pU_{b+t}\equiv4\,16^t\pmod p,\quad0\le t<3k.}
\]

At the first secondary injection \(n=4k+1\), the original \(-2/(8n-4)=-1/(2p)\) gives

\[
\boxed{pU_{4k+1}\equiv 4\,16^{3k}-\tfrac12\pmod p.}
\tag{PGC-01b}
\]

This genuinely uses all four original poles and the original \(U_0=0\) boundary. Its large clean time window is new to this dossier; it does **not** assert temporal cancellation.

## PGC-02. Selected complementary cofactor and integer carry

For \(0\le s<t<3k\), let \(B_t-B_s=A_{ts}/Q_{ts}\) in lowest terms, \(p\nmid Q_{ts}\). Then

\[
U_{b+t}-U_{b+s}=
\frac{4(16^t-16^s)Q_{ts}+pA_{ts}}{pQ_{ts}}.
\]

Let \(K_{ts}=4(16^t-16^s)Q_{ts}+pA_{ts}\) and \(c_{ts}=\min_{\ell\in\mathbb Z}|K_{ts}-\ell pQ_{ts}|\). The actual **selected Archimedean** circle separation is

\[
\boxed{\|U_{b+t}-U_{b+s}\|_{\mathbb R/\mathbb Z}=\frac{c_{ts}}{pQ_{ts}}.}
\tag{PGC-02}
\]

Near collision at radius \(1/M\) is exactly the integer test \(M c_{ts}\le pQ_{ts}\). The prime residue is \(K_{ts}\equiv4(16^t-16^s)Q_{ts}\pmod p\). Nonalias prime times cannot give an exact integer collision, but their lower bound is merely \(1/(pQ_{ts})\), useless when complementary rational height is large. This identifies, rather than hides, the missing selected real cofactor estimate.

## PGC-03. Exact cyclotomic average and its source-selection firewall

Let \(d=\operatorname{ord}_p(16)\), \(a_t=4\,16^t\bmod p\), \(w_t=e(hB_t)\), \(1\le T\le3k\), \(p\nmid h\). For \(u\in\mathbb F_p^\times\) define

\[
S_{u,h}=\sum_{t<T}\zeta_p^{uha_t}w_t,\qquad
V_a=\sum_{t:a_t=a}w_t.
\]

Since the complementary denominators are all coprime to \(p\), the automorphisms rotating \(\zeta_p\) leave \(w_t\) fixed. The classical prime Ramanujan-sum identity gives the **exact** equality

\[
\boxed{
\frac1{p-1}\sum_{u=1}^{p-1}|S_{u,h}|^2
=\frac p{p-1}\sum_{a\in\mathbb F_p}|V_a|^2
-\frac1{p-1}\left|\sum_{t<T}w_t\right|^2.
}
\tag{PGC-03}
\]

Every clock class has at most \(\lceil T/d\rceil\) members; hence the Galois **mean** of normalized window Fejér energy satisfies, for \(H<p\),

\[
\boxed{\frac1{p-1}\sum_u \mathcal E_{T,H}^{(u)}
\le 1+\frac{Hp}{(p-1)T}\lceil T/d\rceil.}
\tag{PGC-03b}
\]

This is an average over Galois embeddings; \(u=1\) is the ONE actual real embedding. A mean is NOT a bound for the actual selected embedding, and the source-selected cofactor may be correlated with the clock. In particular \(p=257\) has \(d=4\), despite a 96-step clean interval. Prime clock order may be small.

**Hostile control PGC-04:** for any finite \(p,T,H\), choose \(Q\) coprime to \(p\) and put \(B_t^*=-\operatorname{round}(Q a_t/p)/Q\). Then \(B_t^*\) has \(p\)-free denominator and \(\|a_t/p+B_t^*\|\le1/(2Q)\). If \(Q>\pi H\),

\[
\boxed{\mathcal E_{T,H}^{\rm selected}\ge1+H(1-\pi H/Q)^2.}
\]

It can approach the maximal \(H+1\), even with large prime-clock order. **These \(B_t^*\) are NOT the original BBP cofactor recurrence.** The counterexample refutes denominator-only and Galois-mean inference, not an original-source theorem.

## PGC-05. Universal one-mesh Fejér-to-INTEGER collision bound

For ANY \(N\) real circle points \(x_n\) and integer \(M\ge2\), partition the circle into \(I_j=[j/M,(j+1)/M)\) and let \(c_j=\#\{n<N:\{x_n\}\in I_j\}\). Define \(\mathcal B_{N,M}=(M/N^2)\sum_jc_j^2\).

**Proof:** for \(F_{M-1}\), the exact nonnegative kernel satisfies \(F\le M\) and \(F(t)\le 1/[4M\|t\|^2]\) (use \(|\sin\pi t|\ge2\|t\|\)). Two bins at cyclic separation \(j\ge2\) are at real-circle distance \(\ge(j-1)/M\), giving \(F\le M/[4(j-1)^2]\). For same/neighbor bins use \(F\le M\). For every cyclic shift \(q\), Cauchy gives \(\sum_j c_jc_{j+q}\le\sum_jc_j^2\). Summing one diagonal, two neighbors and two orientations for all farther shifts yields

\[
\boxed{
\mathcal E_{N,M-1}(x)\le
\left(3+\frac{\pi^2}{12}\right)
\frac{M}{N^2}\sum_{j=0}^{M-1}c_j^2.
}
\tag{PGC-05}
\]

The exact coefficient comes from \(1+2+\frac12\sum_{a\ge1}a^{-2}=3+\pi^2/12\). This is a universal classical positive-kernel bound, NOT source-selected mixing.

For the original zero-seeded rational BBP completion \(\alpha_N=A_N/D_N\), define **purely integer** positions and bins

\[
a_0=A_N\bmod D_N,\quad a_{n+1}=16a_n\bmod D_N,\qquad
b_n=\left\lfloor\frac{M a_n}{D_N}\right\rfloor,\qquad
c_j=\#\{n<N:b_n=j\}.
\]

Take \(N=L^2,M=L+1\). The exact **source-selected integer collision energy** is

\[
\boxed{\mathscr B_L=\frac{L+1}{L^4}\sum_{j=0}^{L}c_j^2.}
\tag{PGC-INTEGER}
\]

For every finite \(L\), \(\mathscr Q_L\le(3+\pi^2/12)\mathscr B_L\). Consequently this single OPEN arithmetic inequality is **sufficient for base-16 π normality** by the parent's proved GF-07:

\[
\boxed{\exists C<\infty\ \forall L\gg1:\quad\mathscr B_L\le C.}
\tag{OPEN-INTEGER-GATE}
\]

Equivalently one may target the **stronger** exact near-pair condition

\[
\#\{(n,m)<L^2:\|16^n\alpha_{L^2}-16^m\alpha_{L^2}\|\le 1/(L+1)\}
\le C\, L^4/(L+1),
\tag{OPEN-PAIR-GATE}
\]

since all same-bin pairs satisfy this proximity. The integer histogram is exact, no trigonometric approximations or π digits required. This is closely related to prior SUCC #407 arithmetic cylinder/collision and #296 Fejér matrix work; the new contribution is an explicit square-checkpoint, **single-mesh** inequality and exact source/carry probe, not an all-horizon upper bound. Both OPEN gates are stricter than the parent's Fejér bound.

## PGC-06. ORIGINAL BBP positive Gamma tail < square of Euler–Mascheroni defect

Define the actual finite discrete/continuous defect

\[
D_n=H_n-\log n-\gamma=\psi(n+1)-\log n>0.
\]

A **classical sharp digamma inequality** (Euler–Maclaurin/Binet) states

\[
\frac1{2n}-\frac1{12n^2}<D_n<\frac1{2n}\qquad(n\ge1).
\]

References: [NIST DLMF §5.11](https://dlmf.nist.gov/5.11), [Huang et al. (2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5959998/). Combine its lower bound with the **inherited exact original positive four-pole Gamma tail** \(0<T_n\le[(8n+1)(8n+2)]^{-1}\) to obtain, for every \(n\ge2\),

\[
\frac{D_n^2}{16}>
\frac{(6n-1)^2}{2304n^4}>
\frac1{(8n+1)(8n+2)}
\ge T_n>0.
\]

The complete universal rational sign certificate is

\[
(6n-1)^2(8n+1)(8n+2)-2304n^4
=96n^3-152n^2+2>0\quad(n\ge2).
\]

**Original-source global theorem**

\[
\boxed{0<T_n<\frac1{16}(H_n-\log n-\gamma)^2,\qquad n\ge2.}
\tag{PGC-06}
\]

This additionally certifies the selected phase transport

\[
|e(hU_n)-e(h16^n\pi/16)|\le2\pi|h|T_n
<(\pi|h|/8)\,D_n^2.
\]

From the existing original-source Laurent clocks (#461 WB-03) and classical Euler–Maclaurin,

\[
T_n=\frac1{64n^2}-\frac7{512n^3}+O(n^{-4}),
\quad D_n=\frac1{2n}-\frac1{12n^2}+O(n^{-4}),
\]

so the **sharper original-source continuum comparison** is

\[
\boxed{T_n=\frac{D_n^2}{16}-\frac{13}{1536n^3}+O(n^{-4}),\qquad
\lim_{n\to\infty}\frac{16T_n}{D_n^2}=1.}
\tag{PGC-07}
\]

The nonzero cubic mismatch makes this a quantitative coupling, NOT an exact identity or cancellation mechanism. The factor 1/16 comes from the original BBP tail coefficient \(1/64\) versus the universal harmonic coefficient \(1/2\).

## PGC-08. Inverse golden is the FINITE Fibonacci circle-renormalization of the γ defect

Let \(\varphi=(1+\sqrt5)/2,\ \eta=\varphi^{-1}\), and \(F_0=0,F_1=1\). The exact integral-ring/golden rotation identity is

\[
\boxed{F_k\eta-F_{k-1}=(-1)^{k-1}\eta^k\quad(k\ge1).}
\tag{PGC-08a}
\]

Therefore the return of a rotation by \(\eta\) on the **actual real circle** after \(F_k\) steps has arc size \(\eta^k\). Binet and classical defect asymptotics give

\[
\boxed{
D_{F_k}=\frac{\sqrt5}{2}\eta^k+O(\eta^{2k}),
\qquad
T_{F_k}=\frac5{64}\eta^{2k}+O(\eta^{3k}).
}
\tag{PGC-08b}
\]

In particular

\[
\lim_{k\to\infty}\frac{D_{F_{k+1}}}{D_{F_k}}=\eta,\quad
\lim_{k\to\infty}\frac{T_{F_{k+1}}}{T_{F_k}}=\eta^2,\quad
\lim_{k\to\infty}\frac{D_{F_k}}{|F_k\eta-F_{k-1}|}=\frac{\sqrt5}{2}.
\]

Crucially an observable needing **no inserted numerical γ** is the finite shell differential

\[
J_k=H_{F_{k+1}}-H_{F_k}-\log(F_{k+1}/F_k)
=D_{F_{k+1}}-D_{F_k}<0.
\]

It satisfies \(J_{k+1}/J_k\to\eta\). Thus inverse golden is an exact renormalization eigenvalue of the **finite harmonic/continuous Gamma defect on Fibonacci-selected circle return scales**. This is a mathematically precise version of the proposed “inverse golden as Euler–Mascheroni viewed in finite circle geometry.” It is NOT a numerical identity \(\eta=\gamma\), NOT a unique intrinsic base-16 parameter (other sampled scales have other contraction factors), and NOT an inference about the signed temporal phase distribution. The original BBP Gamma source's **native scalar silver regulator** \(\log(1+\sqrt2)\) remains as proven in #468.

## Claim-status and next decisive discriminator

**Paper proved (within stated boundary):** PGC-01/02 original-source clean prime/cofactor and selected real integer carry; PGC-03 exact classical Galois mean; PGC-04 explicit p-free hostile counterfeit; PGC-05 universal Fejér/single-mesh bound; PGC-06 original Gamma-to-harmonic global inequality; PGC-07 asymptotic cubic difference; PGC-08 Fibonacci circle-renormalization. **Observed finite:** original exact source prime/carry and histogram examples plus diagnostic complex Galois values in tests/FINITE_RECEIPT.json. **UNVERIFIED/OPEN:** selected all-L \(\mathscr B_L=O(1)\), \(\mathscr Q_L=O(1)\), prime-window pair COVERAGE, and original real cofactor nonconspiracy. **π base-16 normality and RH remain OPEN.**

The next lamp must prove quantitative **selected real cofactor proximity counts** AND a legitimate covering of the all-pairs square-checkpoint geometry by source-attested prime windows (possibly jointly using #460's other prime family). A Galois average, exact prime nonzero result, local Haar, positive Gamma mass, or golden defect scaling is not that estimate. No merging, publication, or theorem-status promotion without independent review and the repository's AGENTS.md checks.
