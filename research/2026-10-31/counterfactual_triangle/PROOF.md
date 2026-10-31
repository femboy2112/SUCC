# Counterfactual Triangle Carrier Rigidity — source-faithful reductio

**2026-10-31. Research only. π base-16 normality, the selected Weyl gate, and RH remain OPEN.** Results CT-01–CT-09 below are elementary paper derivations from classical facts and already integrated SUCC lemmas, with new-to-project exact triangular arithmetic probes. No academic priority or proof of normality claimed.

## Source and types

Retain the authentic four signed poles and exact original zero seed:
\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]
Set \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\) and \(y_n=\{U_n+T_n\}=\{16^{n-1}\pi\}\). The established source estimates give \(T_n<1/(64n^2)\) and \(B=\sum_{n\ge1}T_n<1/32\). Rational \(U_n\), completed circle \(y_n\), and internal probability models are separately typed.

## CT-01/02 — continuous triangular sensor and source transport (PROVED LOCAL)

For \(q=16^m\), \(m\ge1\), define periodic hat functions on \(\mathbb R/\mathbb Z\):
\[
\phi_{q,j}(x)=\max(0,1-q\|x-j/q\|),\quad j=0,\ldots,q-1,\quad
\Phi_q(x)=(\phi_{q,j}(x))_j.
\]
On the cell \(x=(i+t)/q\), \(0\le t\le1\), the only nonzero coordinates are \(i,i+1\), with values \(1-t,t\). Thus \(\sum_j\phi_{q,j}=1\), \(\int\phi_{q,j}d\lambda=1/q\), and
\(\|\Phi_q(x)-\Phi_q(z)\|_1\le2q\|x-z\|\).

Put \(P^U_{q,N}=N^{-1}\sum_{n=1}^N\Phi_q(U_n)\), similarly \(P^y_{q,N}\), and \(D^U_{q,N}=\|P^U_{q,N}-q^{-1}{\bf1}\|_1\). Exact original source tail control gives
\[
\boxed{\|P^y_{q,N}-P^U_{q,N}\|_1
\le (2q/N)\sum_{n=1}^NT_n < q/(16N).}\tag{CT-01}
\]
For continuous \(f\) on the circle write \(\omega_f(\eta)=\sup_{\|x-z\|\le\eta}|f(x)-f(z)|\) and \(f_q(x)=\sum_j f(j/q)\phi_{q,j}(x)\). Convex interpolation yields \(\|f-f_q\|_\infty\le\omega_f(1/q)\), giving
\[
\boxed{\left|\frac1N\sum_{n=1}^N f(y_n)-\int f\,d\lambda\right|
\le 2\omega_f(1/q)+\|f\|_\infty(D^U_{q,N}+q/(16N)).}\tag{CT-02}
\]
Consequently π is base-16 normal **iff** for every fixed \(m\ge1\), every \(j<16^m\), \(P^U_{16^m,N}(j)\to16^{-m}\). The forward implication uses continuity and CT-01; the converse takes \(N\to\infty\) at fixed \(q\), then \(q\to\infty\). In particular, **if π is nonnormal, one fixed finite triangular carrier sensor must have persistent nonzero asymptotic deviation**. This avoids discontinuous-cylinder seam/atom assumptions. A sufficient but not necessary moving-scale certificate is \(q_N\to\infty\), \(q_N=o(N)\), \(D^U_{q_N,N}\to0\).

## CT-03/05 — exact 16-fold extruded-triangle Ward identity (PROVED LOCAL)

The hats satisfy a *pointwise* 16-to-1 refinement identity
\[
\boxed{\phi_{q,j}(16x)=\sum_{t=0}^{15}\phi_{16q,j+tq}(x).}\tag{CT-03}
\]
Proof: both sides are continuous, linear between adjacent nodes of the \(1/(16q)\) grid, and agree at every node. Let \((Ap)_j=\sum_{t=0}^{15}p_{j+tq}\). The empirical source defect \(\mathcal W_{q,N}=P^U_{q,N}-AP^U_{16q,N}\) satisfies the *exact rational* identity
\[
\boxed{\mathcal W_{q,N}
=\frac{\Phi_q(U_1)-\Phi_q(U_{N+1})}{N}
+\frac1N\sum_{n=1}^N
 [\Phi_q(U_{n+1})-\Phi_q(16U_n)].}\tag{CT-04}
\]
Since \(U_{n+1}=16U_n+r(n+1)\) and \(\|\Phi_q(x)-\Phi_q(z)\|_1\le2q\|x-z\|\),
\[
\boxed{\|\mathcal W_{q,N}\|_1
\le\frac{2+2q\sum_{n=1}^Nr(n+1)}N<\frac{2+8q}N.}\tag{CT-05}
\]
The latter uses \(r(1)=47/15\) and for \(n\ge2\), \(r(n)<15/[64(n-1)^2]\), hence \(\sum_{n\ge1}r(n)<47/15+(15/64)\zeta(2)<4\). This is a genuine all-horizon source-faithful carrier consistency theorem at \(q=o(N)\), but it is **seed-blind**. The non-Haar invariant law \(\delta_0\) satisfies CT-03 exactly and has \(D_q=2(1-1/q)\). Thus the Ward identity does **not** imply Haar, independence, or normality. It is not a Pascal combinatorial identity or evidence of physical curvature.

## CT-06 — finite Walsh-current localization (PROVED LOCAL)

For the *completed* hexadecimal digit stream, let \(p_{m,N}(w)\) be the frequencies of length-\(m\) words from the same \(N\) starting positions. Define for contexts \(v\) and nontrivial four-bit Walsh masks \(b=1,\ldots,15\)
\[
J_{v,b,N}=\sum_{a=0}^{15}(-1)^{\operatorname{popcount}(a\land b)}
p_{|v|+1,N}(va),\quad
M_{k,N}=\max_{|v|<k,1\le b\le15}|J_{v,b,N}|.
\]
Walsh inversion gives \(p_{|v|+1,N}(va)-p_{|v|,N}(v)/16
=(1/16)\sum_{b=1}^{15}\chi_b(a)J_{v,b,N}\).
Telescoping the prefix deviation \(\Delta_{va}=\Delta_v/16+\text{child error}\), from \(\Delta_\emptyset=0\), proves
\[
\boxed{|p_{k,N}(w)-16^{-k}|\le(1-16^{-k})M_{k,N}.}\tag{CT-06}
\]
If π is nonnormal, there are fixed \(k,w,\varepsilon>0\) and infinitely many \(N\) with \(|p_{k,N}(w)-16^{-k}|\ge\varepsilon\). Finite pigeonhole then forces *one fixed* context/mask with \(\limsup_N|J_{v,b,N}|\ge\varepsilon/(1-16^{-k})\). Conversely all fixed-context currents vanishing implies normality. This is a sharper explicit finite-cell witness than just an aggregate Parseval energy. Direct transport of these **discontinuous** currents to rational \(U_n\) requires seam control: CT-01 offers a different **continuous** witness, not an unjustified identification.

## CT-07/09 — quantitative counterfactual collision radiation (DERIVED from existing lemmas)

Let the same \(k,w,\varepsilon\) witness nonnormality along unbounded horizons. At any such \(N\) and \(m\ge k\), the total word-\(L^1\) discrepancy is at least \(2\varepsilon\). Main XVII's inherited MS-01 entropy inequality gives
\[
\boxed{\log Q_{m,N}\ge
\tfrac12\lfloor m/k\rfloor(2\varepsilon-2m/N)_+^2.}\tag{CT-07}
\]
At \(m=\lfloor\log_{16}N\rfloor\), \(H=16^m/2\), combine PR411 FB-01 and PR415 K01 to get
\[
\boxed{\sqrt{\mathcal F_{H,N}(U)}\ge
(\sqrt2/\pi)\exp\!\left[
\tfrac14\lfloor m/k\rfloor(2\varepsilon-2m/N)_+^2\right]
-C_*H/N,\qquad C_*^2=\pi/(8\sqrt3).}\tag{CT-08}
\]
Since \(H/N\le1/2\), this forces
\[
\boxed{\limsup_{N\to\infty}
\frac{\log\mathcal F_{16^{\lfloor\log_{16}N\rfloor}/2,N}(U)}{\log N}
\ge \frac{2\varepsilon^2}{k\log16}>0.}\tag{CT-09}
\]
**Status:** proof of a counterfactual *necessary defect*, NOT of its impossibility. It composes existing MS-01, FB-01, K01 and is not source-derived selected upper saving. The moving-depth subpower energy bound sufficient to contradict CT-09 remains OPEN; PR415 K04 shows it is strictly stronger than normality in general.

## Crucible / anti-overclaim controls

- The coherent **same-forcing changed-seed** \(s_*=-\pi/16\) has \(U_n(s_*)=-T_n\to0\) and completed law \(\delta_0\). Its Ward defect tends to zero while its hat bias tends to \(2(1-1/q)\). Therefore source-only Ward closure cannot force Haar; this seed violates \(U_0=0\).
- A periodic de Bruijn order-two stream has \(Q_1=Q_2=1\), yet \(Q_3=16\). Balanced low-depth observers do not force global truth.
- Main XVII/AQ-02 Gaussian positive rational sources match arbitrary rational-state BBP prefixes while becoming nonnormal globally. This refutes finite-prefix-only uniformity, not a theorem using the *complete* original law.
- Prime-primary Gauss saving NET-XVII-1 does not control the full complementary real phase, even when the displayed primary group is uniform.
- New hat/ward witnesses may improve the *route* and its precision accounting. They do not produce an all-horizon bound on the actual selected observable, certify numerical normality, or require new axioms.

## Exact next theorem: CT-10 OPEN

Prove from **all four authentic signed poles and selected \(U_0=0\)** either:
(a) for every fixed \(q=16^m,j\), \(P^U_{q,N}(j)\to1/q\); or
(b) for every fixed context \(v\) and nontrivial Walsh mask \(b\), the selected \(J_{v,b,N}\to0\); or
(c) a genuinely source-selected all-horizon bound \(\mathcal F_{H_N,N}(U)=N^{o(1)}\) at a safe growing clock (sufficient, stronger than necessary).
Test any proposed inequality against coherent changed seeds, seven-pole AT-07, de Bruijn, and Gaussian finite-prefix shadows; pay full primary×cofiber signed weights and cross-window coverage. Do NOT infer CT-10 from CT-03/05 or finite readings. RH and π normality remain OPEN.

**Provenance:** Main XVII selected arithmetic and claim registry; PR407 CTC-02/03; PR410 MS-01/02; PR411 FB-01; PR415 K01/K04; PR414 observer-vs-carrier adequacy; older source-tail exact identities. All new exact arithmetic code is under this research directory; source archives and production interfaces unchanged.


## CT-12 — a genuinely certified finite-to-global *source forcing charge* (PROVED LOCAL)

Define the full original-source (zero-selected) triangular forcing current
\[
C_q=\sum_{n=1}^{\infty}\left[\Phi_q(U_{n+1})-\Phi_q(16U_n)\right].
\]
Unlike a formal infinite digit census, this is an **effectively computable real vector with a finite symbolic proof of every requested precision**. Its prefix \(C_{q,N}\) is exactly rational, and every term has \(\ell^1\) norm at most \(2q\,r(n+1)\). Since the positive original four-pole regrouping gives \(r(n+1)<15/(64n^2)\) for \(n\ge1\), the convergent series has a rigorous, source-derived uniform tail modulus
\[
\boxed{\|C_q-C_{q,N}\|_1
< 2q\sum_{n>N}\frac{15}{64n^2}
\le \frac{15q}{32N}.}\tag{CT-12}
\]
Moreover \(\sum_j C_q(j)=0\), since each hat vector has coordinate sum 1. The resulting all-horizon forcing charge is **source-selected**, unlike the seed-blind Ward error *bound*. It can be enclosed with exact rational arithmetic and a prescribed error radius, but it does not itself bound the limiting selected occupation measure. In particular, the Ward identity becomes \(N\mathcal W_{q,N}=\Phi_q(U_1)-\Phi_q(U_{N+1})+C_{q,N}\); the first term need not converge. No Haar/normality assertion follows. This is a concrete finite↔global certificate for a source forcing observable, **not** the global normality predicate.

The exact implementation records \(C_{q,N}\), its tail certificate and coordinate-sum conservation. Independent finite Cauchy comparisons at \(q=16,256\) and \(N=128,256,512\) lie inside the analytic tail budget. No unperformed infinite computation or numerical extrapolation is claimed.
