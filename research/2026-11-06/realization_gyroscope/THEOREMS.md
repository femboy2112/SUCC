# Recursive carrier–observer realization and radix-gauge covariance

**Date:** 2026-11-06. **Status:** research dossier, not an announcement of π normality.  All claims are typed; `PROVED LOCAL` means an elementary mathematical derivation presented here, not a Lean/kernel certificate or independent scholarly priority.

## 0. The source, the carrier, and the map that is *not* arbitrary

The authentic four signed BBP source and the **literal** zero initial condition are

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Work on the additive circle \(\mathbb T=\mathbb R/\mathbb Z\); all trajectories and decimal/hexadecimal observations are represented modulo one.  Introduce the **convergent future source tail**

\[
T_n=\sum_{j\ge1}16^{-j}r(n+j).
\]

The original BBP identity gives \(T_0=\pi/16\).  Since \(16T_n=r(n+1)+T_{n+1}\),

\[
\boxed{C_n=\{U_n+T_n\}=\{16^n\pi/16\}}.\tag{RG1}
\]

This is an exact source-to-completed-circle relation; it does **not** require any assumption of normality.  The radix 16 is an actual choice in this BBP algorithm, not a privileged ontology of the carrier.  Other observer representations can be chosen, but they must transport the arithmetic action and the source history faithfully.

## 1. RG-02: explicit selected source-to-completion transport budget — PROVED LOCAL

For every integer \(n\ge2\), the genuine rational source obeys

\[
0<r(n)<n^{-2}.\tag{RG2}
\]

**Proof with an integer positivity certificate.**  Put
\(A(n)=120n^2-89n+16\) and
\(D(n)=(2n-1)(4n-1)(8n-7)(8n-3)\).  Direct common-denominator calculation yields \(r(n)=A(n)/D(n)\).  For \(n=t+2\), \(t\ge0\),

\[
A(t+2)=120t^2+391t+318>0,\\
D(t+2)-(t+2)^2 A(t+2)
=392t^4+2201t^3+4494t^2+3902t+1185>0.
\]

Hence (RG2).  For all \(n\ge1\),

\[
0<T_n<\sum_{j\ge1}\frac{16^{-j}}{(n+j)^2}
\le\frac1{15(n+1)^2}.\tag{RG3}
\]

For any integer Fourier mode \(h\) and any epoch \([A,2A)\), \(A\ge1\), the elementary inequality \(|e^{2\pi ihu}-e^{2\pi ihv}|\le2\pi|h|d_{\mathbb T}(u,v)\) implies

\[
\boxed{\left|\frac1A\sum_{n=A}^{2A-1}e(hU_n)-
\frac1A\sum_{n=A}^{2A-1}e(hC_n)\right|
\le\frac{2\pi|h|}{15(A+1)^2}.}\tag{RG4}
\]

A computable rational interval for any \(T_n\) is \([L_{n,d},L_{n,d}+16^{-d}/(15(n+d+1)^2)]\), with \(L_{n,d}=\sum_{j=1}^d16^{-j}r(n+j)\) and \(n\ge1\), \(d\ge0\).  This is a rigorous **transport-error** bound, not a cancellation bound.  It is coarser than other SUCC source-specific estimates, but it is short, explicit, source-authenticated, and works for all frequencies with stated \(|h|\) dependence.

## 2. RG-03: radix 16 is an observer chart, yet radix 2 has exactly the same normality verdict — CLASSICAL, with proof

Let \(E_b(x)=bx\bmod1\) and \(\nu_N=\frac1N\sum_{n<N}\delta_{E_{16}^n\beta}\).  Define \(\mu_{4N}=\frac1{4N}\sum_{m<4N}\delta_{E_2^m\beta}\).  For every \(N\),

\[
\boxed{\mu_{4N}=\frac14\sum_{j=0}^3(E_2^j)_*\nu_N,}\tag{RG5}
\]

because \(E_2^{4n+j}=E_2^jE_{16}^n\).  Equivalently for every integer \(h\),

\[
\boxed{\widehat\mu_{4N}(h)=\frac14\sum_{j=0}^3\widehat\nu_N(2^j h).}\tag{RG6}
\]

Four binary digits reconstruct a hexadecimal digit EXACTLY (ignoring the standard double-expansion rational boundary convention).

**Forward implication.** If \(\nu_N\to\lambda\) (Haar), then (RG5) implies \(\mu_{4N}\to\lambda\).  Incomplete binary blocks of at most three terms do not alter the limit.

**Reverse implication (positive lift, not a formal inverse to (RG6)).** Suppose \(\mu_M\to\lambda\).  Any subsequential weak limit \(\nu\) of \(\nu_N\) is invariant under \(E_{16}\) by telescoping.  Taking a subsequential limit in (RG5) yields

\[
\lambda=\tfrac14\sum_{j=0}^3(E_2^j)_*\nu,\qquad \nu\le4\lambda.
\]

Thus \(\nu\) has an \(L^1\) density with respect to \(\lambda\).  Invariance gives \(\widehat\nu(h)=\widehat\nu(16h)=\widehat\nu(16^kh)\).  The Riemann–Lebesgue lemma forces each of these to be zero for \(h\ne0\).  Hence \(\nu=\lambda\).  Every subsequential limit is Haar, so \(\nu_N\to\lambda\).  Wall's circle-orbit characterization of normality and the classical multiplicatively dependent base theorem give

\[
\boxed{\beta\text{ normal base 16}\iff\beta\text{ normal base 2}.}\tag{RG7}
\]

Applying \(\beta=\pi/16\), shifting four binary places does not affect normality; thus the same equivalence holds for \(\pi\).  This does **not** assert equivalence with arbitrary independent bases (e.g. 3), arbitrary time-dependent coordinates, or arbitrary lossy observation maps.

## 3. RG-04: recursive observer/carrier closure — PROVED LOCAL, CONDITIONAL ON EXACT IMPLEMENTATION

Define a carrier state \(g_n=(x_n,o_n)\), where the **realized observer** contains \(o_n=(m_n,\ell_n,n,H_n)\): its internally predicted world \(m_n\), previous observed cell \(\ell_n\), clock, and finite transcript.  Its action is

\[
a_n=\mathcal P(o_n)\in\{1,2,\dots\},\quad
z_n=\lfloor16^{a_n}x_n\rfloor,\quad
x_{n+1}=\{16x_n+r(n+1)\},
\]

and its **physically/carrier-realized internal computation** updates \(m_{n+1}=\{16m_n+\widehat r(n+1)\}\), with its transcript and next policy updated from \(z_n\).  The action selects depth and does **not** alter the immutable BBP source or \(\pi\).

The mathematical model \(\widehat g_n\) predicts the *whole observer transition*, not just \(x_{n+1}\).  Write \(\rho(g)=o\) and \(\widehat\rho(\widehat g)=\widehat o\). If both paths have equal complete initial states, source, policy, and observation functions on all reachable states, then by induction for each \(n\),

\[
\boxed{\rho(F^n(g_0))=\widehat\rho(\widehat F^n(\widehat g_0)).}\tag{RG8}
\]

This is a **conditional simulation/commutation theorem**, not evidence that the observer's adopted physical model is true.  In particular:

* A changed source invalidates the equality even when the first coarse cell agrees.
* Forgetting the unresolved subcell phase makes a coarse observation generally non-Markov (as #522 demonstrates independently).
* A fully self-consistent **wrong seed** also commutes, but may be non-normal. Exact coherence is required for proof transfer, not sufficient for Haar.

## 4. RG-05: joint gauge log is the lost causal information — PROVED LOCAL

A policy may choose a rotation \(a_n\in\mathbb T\) of its observation chart (possibly adaptively, based on its entire realized memory):

\[
y_n=x_n+a_n\pmod1.
\]

The observed marginal alone is \(\eta_N=N^{-1}\sum\delta_{y_n}\).  The **joint action–observation measure** is

\[
\Gamma_N=\frac1N\sum_{n<N}\delta_{(a_n,y_n)},\qquad
D(a,y)=y-a\pmod1.
\]

No independence, stationarity, or choice of radix is needed. **Pathwise**, including for feedback policies,

\[
\boxed{\mu_N=\frac1N\sum_{n<N}\delta_{x_n}=D_*\Gamma_N,}\tag{RG9}
\]

and for each integer \(h\),

\[
\boxed{W_N(h)=\frac1N\sum_{n<N}e(hx_n)
=\int_{\mathbb T^2}e(h(y-a))\,d\Gamma_N(a,y).}\tag{RG10}
\]

**This is precisely the information lost by an observer who marginalizes the chosen chart away.**  The virtual-field reading can be made mathematically exact as a retained conditional/joint law.  It does **not** imply literal quantum energy, a random physical π orbit, or a new cancellation estimate.

If an internal model reports \((\widehat a_n,\widehat y_n)\), and its physical/observer comparisons certify mean circle errors

\[
\epsilon_N^{\mathrm{real}}=\frac1N\sum d_{\mathbb T}(a_n,\widehat a_n),\quad
\epsilon_N^{\mathrm{obs}}=\frac1N\sum d_{\mathbb T}(y_n,\widehat y_n),
\]

then the **two-connection transport certificate** is

\[
\boxed{|W_N(h)-\widehat W_N(h)|\le
2\pi|h|(\epsilon_N^{\mathrm{real}}+\epsilon_N^{\mathrm{obs}}).}\tag{RG11}
\]

If the model sees only base-16 cells of depth \(m_n\), choose any representative \(\widehat y_n\) in the observed cell.  The observation error is at most \(16^{-m_n}\), so the model may instead use

\[
\boxed{|W_N(h)-\widehat W_N(h)|\le2\pi|h|\left(
\epsilon_N^{\mathrm{real}}+\frac1N\sum_{n<N}16^{-m_n}\right).}\tag{RG12}
\]

This is a genuine **proof-transport theorem**: if a separately justified model result makes \(\widehat W_N(h)\to0\) for every nonzero *fixed* \(h\), while the two errors vanish, then the realized carrier orbit is Haar-generic. Without the first independently derived source-selected input, it is only a valid implication.

## 5. RG-06: even sublinear chart variation can fake Haar — PROVED LOCAL COUNTEREXAMPLE

Take a **constant carrier orbit** \(x_n=0\) (clearly not normal). Choose an irrational \(\theta\), and let the observer use the chart \(a_n=k\theta\bmod1\) for a consecutive block of **length \(k\)**, for \(k=1,2,3,\ldots\).  The observed orbit is \(y_n=a_n\). By the end of block \(K\), \(N_K=K(K+1)/2\), and for any \(h\ne0\), write \(z=e(h\theta)\ne1\). Then

\[
\frac1{N_K}\sum_{n<N_K}e(hy_n)
=\frac1{N_K}\sum_{k=1}^Kkz^k
=\frac{z(1-(K+1)z^K+Kz^{K+1})}{N_K(1-z)^2}
=O_h(1/K)\to0.
\]

The unfinished last block contributes at most \(K/N_K\), so **all** horizons satisfy Weyl's criterion. Thus \(y_n\) is Haar-generic although \(x_n\equiv0\).

The chart changes only \(K-1=O(\sqrt N)\) times through \(N_K\) observations, with total circle variation at most \(K/2=O(\sqrt N)=o(N)\). Therefore ***even sublinear chart total variation is not an adequate gauge-fixing condition***. Every individual rotation preserves Haar, and the moving-chart evolution is causally consistent if the observer records \(a_n\).

But the joint law \(\Gamma_N\) lives on the diagonal \(y=a\); its decoded measure is always \(\delta_0\), and the joint character in (RG10) equals **1** for every \(h\), not zero. The missing correlation is exactly exposed.

### A useful sufficient alternative — PROVED LOCAL

If for some **fixed** \(a\in\mathbb T\) the gauge satisfies
\(N^{-1}\sum_{n<N}d_{\mathbb T}(a_n,a)\to0\), then for every Lipschitz \(f\),

\[
\left|\frac1N\sum f(y_n)-\frac1N\sum f(x_n+a)\right|
\le \mathrm{Lip}(f)\frac1N\sum d_{\mathbb T}(a_n,a)\to0.
\]

Hence \(y_n\) is Haar-generic iff \(x_n\) is.  The original source tail \(a_n=T_n\) is exactly such a gauge by (RG3).  **But this sufficient condition is deliberately stronger than necessary:** exact logged invertible gauges can be decoded even if they never settle.

## 6. RG-07: the bounded-radix countermodel survives changing encoding — PROVED LOCAL

Keep the **same** original four-pole source and choose the completed seed \(\beta=1/5\), formally obtained from initial \(s=1/5-\pi/16\).  The exact identity (RG1), generalized to real seeds, gives completed orbit \(\{16^n/5\}=1/5\) at all times since \(16\equiv1\pmod5\).  In base 2, \(\{2^n/5\}\) has period 4. Both orbits are non-Haar.

The original zero seed is the authenticated target, **not** this control. This is only a *logical obstruction* to asserting that faithful source, closed-loop observers, duality, or chart covariance alone imply normality. The hexadecimal chart was not the fundamental cause of the obstruction.

## 7. What could actually prove π normality from here?

For the authentic zero-seeded source and an explicitly calibrated observer/encoding policy, prove for every fixed \(h\ne0\)

\[
\lim_{A\to\infty}\underbrace{\frac1A\sum_{n=A}^{2A-1}
 e\bigl(h(y_n-a_n)\bigr)}_{\text{joint observer–action character}}=0.\tag{RG13 OPEN}
\]

By RG9–RG11 and the BBP completion, this is precisely the genuine selected Weyl condition (up to the proved tail transport), not a newly smaller arithmetic obligation. **Re-expression does not discharge its cancellation proof.** What the new instrument contributes is an unambiguous basis-independent *proof-transfer contract*: any claimed source-specific route must show a genuine arithmetic saving for the authenticated orbit, and demonstrate that the two observer/realization errors are controlled. An adaptive chart, marginal Haar test, all-seed \(L^2\) bound, or self-consistent model cannot substitute.

A falsifiable extension is to identify a **source-computable, seed-sensitive coupling** among the original four signed BBP rational residues, the actual chosen carries, and the joint character, with a signed estimate that rejects the \(1/5\) completion and the no-source constant orbit on held-out intervals. No such inequality is established here.

## Citations and SUCC provenance

- Original BBP formula: Bailey, Borwein, Plouffe, *On the Rapid Computation of Various Polylogarithmic Constants* (Math. Comp. 66, 1997), DOI `10.1090/S0025-5718-97-00856-9`; Bailey's author exposition: https://www.davidhbailey.com/dhbpapers/bbp-alg.pdf.
- Classical base-power normality: Maxfield, *Normal k-tuples* (1953); summarized in *Distribution Modulo One and Diophantine Approximation*, chapter 6: https://doi.org/10.1017/CBO9781139017732.008. Wall's orbit/normality characterization also appears in https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/descriptive-complexity-in-cantor-series/19EAD3B2B426D3826A6DA9405DFB7D81.
- SUCC frozen original source and completion: PR #521 `research/2026-11-05/critical_carry_jets/`, PR #522 `research/2026-11-05/history_shell/PROOFS.md`, and Main XX proof-forge PR #524. All are **read-only inputs** to this add-only branch.
- `AGENTS.md` and `docs/METHOD.md` govern status and countermodel policy. No Lean, frozen original, production default, provenance import or `main` change is made.
