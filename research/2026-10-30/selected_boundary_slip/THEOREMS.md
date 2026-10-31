# Selected-boundary noncoherence: a logarithmic signed saving

**Status:** paper derivation / locally proved conditional-on-published-classical-input theorem. Authentic source and zero-seed BBP are unchanged. Results are NEW TO THIS SUCC RESEARCH ROUND, not a claim of scholarly priority. The published irrationality-exponent estimate for π is a load-bearing external theorem. Nothing below proves π normality, the uniform sparse prime-window conjecture SC-06, or RH.

**Lineage:** Parent PR #401 `abf51bf061f583d0e38a915c2e1bae5e28ddaace`, stacked above #400/#399/#398, rooted in Main XVI. Original source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Use \(e(t)=\exp(2\pi i t)\). The classical original BBP identity is \(U_n=16^{n-1}\pi-T_n\), where \(T_n=\sum_{j\ge1}16^{-j}r(n+j)>0\). For a changed real seed \(s\), \(U_n(s)=16^{n-1}(\pi+16s)-T_n\). Define

\[
D_n=T_n-T_{n+1},\quad z_n(h,s)=e(hU_n(s)),\quad E_n(h,s)=1-\Re(z_{n+1}\overline{z_n}).
\]

## SB-01 — a source-exact **effective** Gamma/Laplace lag bound

The original positive Laplace representation is

\[
r(n)=\int_0^\infty e^{-(8n-7)x}Q(x)\,dx,\quad
Q(x)=2(1-e^{-3x})+(1-e^{-4x})+(1-e^{-5x}).
\]

Since \(0<Q(x)\le15x\) for \(x>0\) and \(0<1-e^{-8x}\le8x\),

\[
0<r(k)-r(k+1)
=\int_0^\infty e^{-(8k-7)x}Q(x)(1-e^{-8x})\,dx
\le120\int_0^\infty x^2e^{-(8k-7)x}\,dx
=\frac{240}{(8k-7)^3}.
\]

Sum with weights \(16^{-j}\), whose total is \(1/15\). The source's *exact native* tail satisfies, for **every** integer \(n\ge1\),

\[
\boxed{0<D_n=T_n-T_{n+1}\le\frac{16}{(8n+1)^3}.}\tag{SB1}
\]

This directly supplies the finite-index correction threshold: for fixed \(h\ne0\), \(|h|D_n<1/180\) whenever \((8n+1)^3>2880|h|\). The leading asymptotic \(D_n\sim1/(32n^3)\) agrees with the parent source analysis. We claim no novelty for positivity or the leading expansion.

## SB-02 — no long zero-seed coherent window (proved using Diophantine input)

Let \(\mu(\beta)\) denote the irrationality exponent of an irrational real \(\beta\). Fix \(h\ne0\), \(0<\delta_0<\delta<1/17\), and \(\kappa>\mu(\beta)-1\). Assume the exact affine form

\[
U_n(s)=16^{n-1}\beta-T_n,\quad\beta=\pi+16s,
\]

where \(\mu(\beta)<\infty\) and \(D_n\to0\). Put \(\eta=1-\cos(2\pi\delta_0)>0\).

**Theorem.** For every sufficiently large integer \(A\), in every window \([A,A+L-1]\) of length \(L\ge\lceil\kappa A\rceil\), there exists \(n\) for which

\[
\boxed{E_n(h,s)\ge\eta.}\tag{SB2}
\]

*Proof.* Suppose all such energies are less than \(\eta\). Because \(t\mapsto1-\cos(2\pi t)\) increases with \(\|t\|\in[0,1/2]\), the lag phases satisfy

\[
\|h(U_{n+1}(s)-U_n(s))\|<\delta_0.
\]

The exact selected recurrence gives

\[
U_{n+1}(s)-U_n(s)=15\,16^{n-1}\beta+D_n.
\]

For all large \(A\), \(|h|D_n<\delta-\delta_0\) whenever \(n\ge A\), so \(\|15h16^{n-1}\beta\|<\delta\) throughout the window. Let \(\epsilon_n\in(-\delta,\delta)\) be the signed nearest-integer residue of \(15h16^{n-1}\beta\). Then \(16\epsilon_n-\epsilon_{n+1}\in\mathbb Z\) and has magnitude strictly less than \(17\delta<1\), hence it is zero. Therefore \(\epsilon_{A+j}=16^j\epsilon_A\) and

\[
|\epsilon_A|<\delta\,16^{-(L-1)}.
\]

Set \(q=15|h|16^{A-1}\). There is an integer \(p\) with

\[
0<|\beta-p/q|<\frac{\delta}{q16^{L-1}}.\tag{*}
\]

For any exponent \(\nu\) with \(\mu(\beta)<\nu<\kappa+1\), the definition of finite irrationality exponent supplies some \(c_\nu>0\) such that \(|\beta-p/q|\ge c_\nu q^{-\nu}\) for every integer \(p,q\ge1\), including unreduced rationals (the finitely many small reduced denominators can be absorbed into \(c_\nu\)). Combining with (*) gives

\[
16^{L-1}<\frac{\delta}{c_\nu}\,(15|h|16^{A-1})^{\nu-1},
\]

contradicting \(L\ge\kappa A\) as \(A\to\infty\), because \(\kappa>\nu-1\). QED.

**Authentic concrete specialization.** Zeilberger–Zudilin's published upper bound \(\mu(\pi)\le7.103205334137\ldots\) permits \(\nu=15/2\) and \(\kappa=7\). Choose \(\delta_0=1/20\), \(\delta=1/18\), so \(\eta=1-\cos(\pi/10)\). For each fixed nonzero integer \(h\), there exists \(A_0(h)\) such that

\[
\boxed{\forall A\in\mathbb Z,\ A\ge A_0(h):\quad
\max_{A\le n<8A} E_n(h,0)\ge1-\cos(\pi/10).}\tag{SB3}
\]

Only the Diophantine threshold in \(A_0\) is non-effective here; the source-tail threshold is explicit by SB1. The theorem is derived from published Diophantine arithmetic and the exact BBP Green-tail bridge, **not** from the Gamma/Gauss source geometry alone.

Primary literature: Doron Zeilberger and Wadim Zudilin, *The Irrationality Measure of Pi is at most 7.103205334137...*, Moscow J. Comb. Number Theory 9 (2020), 407–419. https://arxiv.org/abs/1912.06345 , https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/pimeas.pdf . Later claims of a sharper exponent are not required and are not relied upon.

## SB-03 — genuinely unbounded selected lag energy and an all-horizon signed gain

Let \(S_N(h)=\sum_{n=1}^N z_n(h,0)\). Apply SB3 successively to disjoint blocks \([A_0 8^j,A_0 8^{j+1})\) for \(j=0,1,\ldots\). For every sufficiently large \(N\), the number of complete blocks contained in \([1,N)\) is at least

\[
K_N=\max\{0,\lfloor\log_8(N/A_0)\rfloor\}.
\]

Each complete block contributes at least \(\eta\) to the total nonnegative energy. Hence

\[
\boxed{\sum_{n=1}^{N-1}E_n(h,0)\ge\eta K_N
\ge\frac{\eta}{\log8}\log N-O_h(1).}\tag{SB4}
\]

This is **authentic-zero-seed selected**: the source-only minimization of parent #401 gives only \(O(A^{-6})\) average energy on comparable windows and is attained by its coherent nonzero seed.

For arbitrary unit complex \(z_1,\ldots,z_N\), set \(\bar z=S_N/N\). The elementary variance inequality gives

\[
\sum_{n=1}^{N-1}|z_{n+1}-z_n|^2
\le4\sum_{n=1}^N|z_n-\bar z|^2
=4\bigl(N-|S_N|^2/N\bigr).
\]

Since \(|z_{n+1}-z_n|^2=2E_n\), this implies

\[
N-|S_N|\ge\frac14\sum_{n=1}^{N-1}E_n.
\]

Thus, for **every fixed** \(h\ne0\),

\[
\boxed{|S_N(h)|\le N-\frac{\eta}{4\log8}\log N+O_h(1),
\qquad \eta=1-\cos(\pi/10).}\tag{SB5}
\]

This is a genuine all-horizon nontrivial improvement over the trivial \(N\), with logarithmically diverging **absolute** saving. It remains \(|S_N|/N\le1-O_h(\log N/N)\), therefore **not** the needed \(S_N=o(N)\), not a fixed-fraction saving, and not a proof of π normality. The assertion that this argument is a new mathematical discovery beyond SUCC is **UNVERIFIED**.

## SB-04 — countermodels, seed scope, and why this does not settle SC-06

**Coherent same-forcing seed.** At \(s_*=-\pi/16\), \(U_n(s_*)=-T_n\). Therefore \(E_n(h,s_*)=1-\cos(2\pi hD_n)\le2\pi^2h^2D_n^2\), and by SB1

\[
\sum_{n\ge1} E_n(h,s_*)\le512\pi^2h^2\sum_{n\ge1}(8n+1)^{-6}<\infty.
\]

Thus the authentic seed has logarithmically divergent lag-energy while the original-forcing coherent seed has **finite** lag-energy. The same forcing/Gamma/prime snapshot geometry cannot yield this dichotomy without selected-boundary information.

**Rational seed changes.** If \(s\in\mathbb Q\) is fixed, \(\beta=\pi+16s\) has the same irrationality exponent as \(\pi\) (rational affine translations preserve it); SB2–SB5 also apply. They are not unique-zero-seed identification results. In particular no rational translated seed is required to fail asymptotic normality.

**Liouville-type controls.** An irrational \(\beta\) with arbitrarily long zero-digit runs (for example \(\sum_{j\ge1}16^{-j!}\)) can have arbitrarily long coherent relative windows. Irrationality alone does NOT supply SB2 with the 7A scale. The finite irrationality-exponent input is load bearing.

**SC-06 remains OPEN.** The available rigorous irrationality bound permits \(\kappa=7\), but an eligible prime-birth window starts near \(p/8\) and has length at most \((p-1)/4\), i.e. at most about twice the starting time. SB3 does not even guarantee a single slip on each such short window; still less a positive fraction or a fixed lower bound on its average energy. The signed CRT cofiber bridge in #399/#401 is not solved.

## Scope and next test

**PROVED LOCAL (paper):** SB1–SB5 under the external published irrationality input, subject to independent mathematical review. **OBSERVED:** finite source/phase checks in the accompanying tests and oracle. **UNVERIFIED:** new scholarly priority, any O(N) or positive-density lower bound, Gamma-Gross–Koblitz to selected-phase transport, SC-06, π normality, RH.

**Next mathematically discriminating probe:** seek a selected-zero-boundary **positive-density** phase-slip estimate, or a joint signed CRT cofiber estimate, on the native prime windows. It must use more than the finite irrationality exponent and source-only Green bound; test changed-source seven-pole null and coherent seed, rational translations, matched Gamma jets, and normal Stoneham controls. No geometric/gauge representation by itself is a substitute for signed analysis.
