# Harmonic–Pisot boundary: exact thresholds, residual memory, and an anti-normality theorem

**Research dossier, 2026-11-07.** Parent: main at d32342d375f44ddf62221ad6aff2f534abdc0a03. **Research-only / no imported theorem promotion.** Status: model theorems proved below using classical analysis and Pisot algebra; numerical values are finite controls, not interval certificates. Original BBP source and zero seed untouched; pi base-16 normality, the selected signed Weyl gate, and RH remain OPEN.

## 0. Steelman / typed problem

Author's hypothesis: harmonic accumulation may parameterize the margin separating an observer-created future boundary from zero; Pisot-type contracting conjugate modes may yield observational lock-in while a historical residual remains. This is a *dynamical model*, not a claim of quantum collapse, neurological mechanism, or a known physical law.

Distinguish **phase** z_n on the circle, **history** sum_n (z_n-1)/n, **real budget** b_N, **controller latch** (optional physical interpretation), and **the authentic original-source base-16 pi orbit**. These are different typed objects; no unproved map from one to the other is silently imposed.

Notation: e(t)=exp(2 pi i t), ||t||=distance of t to Z, H_N=sum_{n=1}^N 1/n, gamma=lim_N(H_N-log N). For any real t_n put z_n=e(t_n), q_n=1-Re z_n=2 sin^2(pi t_n), Q_N=sum_{n=1}^N q_n/n, and

\[
b_N(B;t)=B+\sum_{n=1}^N\frac{\cos(2\pi t_n)}n-\log N
       =B+H_N-\log N-Q_N,\quad N\ge1.
\]

A hypothetical **latching controller** forbids future controls once b_N<=0. Whether a real observer implements such a latch is not asserted.

## HPB-01 — universal phase-budget classification (DERIVED / mathematical proof)

**Theorem.** For *every* real phase sequence (t_n), for every real B and all N>=1, b_{N+1}<b_N. Set Q_infty=sum_{n>=1}q_n/n in [0,+infinity].

(a) If Q_infty<infinity then b_N decreases to B+gamma-Q_infty. Put B_crit=Q_infty-gamma. At B>B_crit the margin stays strictly above zero; at B=B_crit it is **positive for every finite N** and decreases to zero; at B<B_crit it crosses zero at a finite index.

(b) If Q_infty=infinity then b_N decreases to -infinity and crosses zero at a finite index for every finite B.

(c) The finite-boundary condition is characterized exactly by

\[
Q_\infty<\infty\quad\Longleftrightarrow\quad
\sum_{n\ge1}\frac{\|t_n\|^2}{n}<\infty.
\]

**Proof.** For every N,
\[
b_{N+1}-b_N
 =\frac{\cos(2\pi t_{N+1})}{N+1}
  -\log(1+1/N)
 \le\frac1{N+1}-\log(1+1/N)<0.
\]
The last inequality follows by integrating 1/x over [N,N+1]. The harmonic remainder H_N-logN tends to gamma, while Q_N increases to Q_infty (finite or infinite), giving both limiting alternatives. Strict monotonicity implies the stated finite-time/critical cases.

For 0<=d=||t||<=1/2, sin(pi d) lies between 2d and pi d, hence

\[
8d^2\le1-\cos(2\pi t)\le2\pi^2d^2.
\]

Summing these bounds divided by n establishes (c). QED.

**Interpretation boundary:** gamma is the universal remainder of *our chosen logarithmic subtraction*. Changing the counterterm by an arbitrary constant shifts B_crit; gamma is not inferred to be a fundamental physical constant governing freedom.

## HPB-02 — Pisot carrier and explicit residual (CLASSICAL Pisot fact + DERIVED theorem)

Let alpha>1 be a real Pisot algebraic integer of degree d, with algebraic conjugates beta_2,...,beta_d satisfying |beta_j|<=rho<1. Algebraic trace gives an integer
\[
T_n=\alpha^n+\sum_{j=2}^{d}\beta_j^n\in\mathbb Z.
\]
Thus
\[
e(\alpha^n)=e\!\left(-\sum_{j=2}^d\beta_j^n\right),\qquad
\| \alpha^n\|\le(d-1)\rho^n.
\]
This identity is exact, including the stable conjugate mode; no large-power floating-point phase reduction is allowed.

**Theorem.** The complex defect series
\[
D_\alpha=\sum_{n\ge1}\frac{e(\alpha^n)-1}{n}
\]
converges absolutely, obeying
\[
\left|D_\alpha-\sum_{n=1}^N\frac{e(\alpha^n)-1}n\right|
\le\frac{2\pi(d-1)\rho^{N+1}}{(N+1)(1-\rho)}.
\]
Its real part equals -Q_infty. Consequently
\[
\lim_{N\to\infty}\left(\sum_{n=1}^N\frac{e(\alpha^n)}n-\log N\right)
=\gamma+D_\alpha,
\quad
B_{\mathrm{crit}}=-\gamma-\Re D_\alpha.
\]

**Proof.** |e(u)-1|<=2pi|u| and the integer trace provide a summable majorant 2pi(d-1)rho^n/n. The tail bound follows by replacing 1/n with 1/(N+1) and summing the geometric progression. Split the partial sum into H_N-logN and the absolutely convergent defect. QED.

For the *real* margin, the stronger bound holds:
\[
0<b_N-(B-B_{\mathrm{crit}})
=H_N-\log N-\gamma+\sum_{n>N}\frac{q_n}{n}
<
\frac1{2N}
+\frac{2\pi^2(d-1)^2\rho^{2(N+1)}}{(N+1)(1-\rho^2)}.
\tag{HPB-02-tail}
\]
Here 0<H_N-logN-gamma<1/(2N) is the standard harmonic inequality. Unlike the complex defect, the source-dependent real tail decays quadratically in the conjugate phase error.

**Golden specialization.** For phi=(1+sqrt5)/2, psi=(1-sqrt5)/2=-phi^{-1}, Lucas trace L_n=phi^n+psi^n in Z, and regulator R=log(phi), we have
\[
e(\phi^n)=e(-\psi^n),\qquad
q_n=2\sin^2(\pi\psi^n),\qquad
\rho=e^{-R}.
\]
The source-specific real tail has rate exp(-2R N) / N. The classical identity R=(sqrt5/2)L(1,chi_5), recovered in SUCC's quadratic Galois/Tate bridge PR #537, ties this *rate* to a genuine Dirichlet L-value without proving any zero-location statement.

**Reproducible numerical control (not an interval proof):**
\[
D_\phi\approx -3.054525125464687875-0.809499157698021766\,i,\quad
B_{\mathrm{crit}}\approx2.4773094605631550145.
\]
Numerical evaluation must use the conjugate psi^n (not naive phi^n modulo 1). For B=2.45 the first nonpositive margin is N=19; for B=2.50 the limiting margin is approximately 0.022690539436845. The symbol B=B_crit means the **exact** real constant, not a rounded decimal; any rounded value just below it eventually crosses zero.

## HPB-03 — logarithmic Abel transform (DERIVED / mathematical proof)

For Pisot alpha define the analytic defect generating function
\[
G_\alpha(w)=\sum_{n\ge1}\frac{e(\alpha^n)-1}{n}w^n.
\]
The conjugate bound makes G analytic on |w|<rho^{-1}, including a neighborhood of w=1. For |w|<1,
\[
\boxed{\sum_{n\ge1}\frac{e(\alpha^n)}{n}w^n=-\log(1-w)+G_\alpha(w).}
\]
Here G_alpha(1)=D_alpha. The Abel singularity -log(1-w) is universal; its finite part is *source-sensitive*. Under sharp N-cutoff, the corresponding universal finite part is gamma. **These two regularization conventions differ:** gamma is not the Abel constant G_alpha(1).

**Proof.** Add/subtract 1 termwise, use sum_{n>=1}w^n/n=-log(1-w), and the absolutely convergent geometric majorant. QED.

## HPB-04 — no-go for normality: finite boundary implies maximal first Fourier coherence (DERIVED / proof)

**Theorem.** If Q_infty<infinity for an arbitrary phase sequence z_n=e(t_n), then
\[
\lim_{N\to\infty}\frac1N\sum_{n=1}^N z_n=1.
\]
Therefore the sequence t_n mod 1 is **not** uniformly distributed. In particular every Pisot power sequence phi^n mod1 fails Weyl's h=1 criterion; this is a deterministic anti-normality negative control, not a route to pi normality.

**Proof.** Let q_n=|z_n-1|^2/2>=0. Given epsilon>0, pick M with sum_{n>=M} q_n/n<epsilon. Then
\[
\frac1N\sum_{n=1}^Nq_n
\le\frac1N\sum_{n<M}q_n+\sum_{n=M}^N\frac{q_n}{n}
\longrightarrow\le\epsilon.
\]
Thus average q_n->0, and Cauchy–Schwarz gives
\[
\left|\frac1N\sum_{n=1}^Nz_n-1\right|
\le\left(\frac1N\sum|z_n-1|^2\right)^{1/2}\to0.
\]
Weyl's criterion requires all nonzero integer-frequency Cesaro averages to tend to zero, in particular the first. QED.

**Reverse obstruction / source-sensitive criterion.** If (t_n) is uniformly distributed mod1, then 1/N sum z_n ->0. Abel summation implies sum_{n<=N}z_n/n=o(log N); hence
\[
Q_N=(1+o(1))\log N,\qquad
b_N(B;t)=-\log N+o(\log N)
\]
for every fixed B. Thus uniform distribution and finite B_crit are mutually exclusive. The *converse* Q_N/logN->1 does NOT establish uniform distribution; harmonic/logarithmic averages are much weaker than the fixed-h dyadic Weyl gate.

**Crucible mutant:** mere z_n->1 does not imply Q_infty<infinity. Take t_n=1/[4 sqrt(log(n+2))]; then t_n->0 but
\[
q_n/n\ge1/[2n\log(n+2)]
\]
and Q_infty diverges. The pointwise null observation fails to preserve a finite boundary. This mutant distinguishes phase convergence from the weighted square-distance criterion in HPB-01.

## HPB-05 — stability of phase-boundary memory (DERIVED / proof)

Equip complex sequences with weighted norm ||a||_w^2=sum_{n>=1}|a_n|^2/n when finite. Let z_n and w_n be unit-circle phase histories. Then
\[
\sqrt{Q(z)}=\frac1{\sqrt2}\|z-1\|_w,\qquad
\left|\sqrt{Q(z)}-\sqrt{Q(w)}\right|
\le\frac1{\sqrt2}\|z-w\|_w.
\]
Proof: the triangle and reverse-triangle inequalities in weighted ell^2. In particular any finite weighted ell^2 change to a finite-energy history preserves finite-energy classification, with a quantified change in critical B. This is a robust **model-level** history-transport result, not evidence of physical or source-derived invariance.

## 6. How this meets SUCC, and where it fails to meet it

1. **PR #537 / quadratic Pisot–Galois–Tate.** The same Q(sqrt5) conjugate psi=-phi^-1 and the regulator R enter HPB-02 exactly. One authentic L(1,chi_5) value sets the Pisot error decay scale. This does NOT transport relative Weil positivity or zeta-zero information.
2. **PR #470 / Pell–Pisot Gamma gluing, and PR #471 / golden observer.** The disappearing conjugate must not be discarded before transport, precisely as their coupled-channel seam emphasizes. Our sequence is a *different observer chart*: no zero-seed BBP selected-time mixing is proved. The Pisot chart here is a useful adversarial lock-in control.
3. **PR #534 / holographic triangle and Gamma source.** Its field obstruction matters. The original BBP source is
\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2).
\]
The four coefficients sum to zero, and sum of coefficient-times-offset is 15. Hence r(n)=15/(64n^2)+O(n^{-3}), **not** a leading 1/n kernel. The universal -gamma terms in the corresponding digamma partial sums cancel after balancing. Our gamma arises from an EXTERNAL 1/n observation weight and counterterm, not intrinsically from r(n). That is a source-map firewall.
4. **No unproved Q-linear time intertwiner.** Multiplication by phi has characteristic polynomial X^2-X-1; 16 is not an eigenvalue (16^2-16-1=239). Therefore a Q-linear intertwiner from golden multiplication to scalar x16 on Q has to vanish. For silver 1+sqrt2 the obstruction is 16^2-2*16-1=223. Any genuinely useful BBP transfer must be nonlinear, carry-labelled, source-specific and independently justified.
5. **Main's pi frontier** (docs/PI_NORMALITY_FRONTIER.md): the authenticated orbit remains U_0=0, U_n=16U_(n-1)+r(n), and the missing gate remains fixed-h signed cancellation S_N(h)=o(N), or the declared LS/H2* alternatives. A finite harmonic-Pisot budget for the real selected orbit would actually *contradict* the desired Weyl condition. Do not relabel a sign-free or auxiliary phase energy as temporal cancellation.

### Source provenance / prior art

- Root contracts: AGENTS.md, docs/METHOD.md, docs/PI_NORMALITY_FRONTIER.md and provenance/IMPORT_MANIFEST.json at pinned main parent.
- Related *draft* SUCC work: PR #470, #471, #534, #537. Their unmerged additions are referenced as prior research, not present on this branch.
- Classical Pisot definition and conjugate almost-integer property: https://mathworld.wolfram.com/PisotNumber.html
- Harmonic Euler–Maclaurin finite part: https://aofa.cs.princeton.edu/40asymptotic/
- Weyl's criterion: https://link.springer.com/article/10.1007/s40687-026-00647-6
- The HPB-01...HPB-05 proofs are elementary deductions under the declared model. No novelty or external peer-review claim.

### Claim ledger (local; no status promotion elsewhere)

| Claim | Label | Evidence | Boundary |
|---|---|---|---|
| HPB-01 monotone classification + iff square defect | DERIVED mathematical proof | inequalities above | model-dependent B |
| HPB-02 Pisot finite complex residue + explicit tails | CLASSICAL premise / DERIVED corollary | integer trace + geometric bound | not physical or BBP orbit |
| HPB-03 Abel finite-part split | DERIVED mathematical proof | log power series | Abel and hard cutoff not identical |
| HPB-04 finite boundary excludes uniform distribution | DERIVED mathematical proof | weighted energy + Weyl | anti-normality control |
| HPB-05 weighted transport stability | DERIVED mathematical proof | norm inequality | no source identifications |
| HPB-NUM golden Bcrit digits and crossing | OBSERVED numerical (non-certified) | focused finite checks; analytic tail formula | no interval arithmetic certificate |
| HPB-π source-specific usefulness beyond a negative control | UNVERIFIED / OPEN | no exact selected BBP phase map | source-selective signed Weyl required |
| HPB-PHYS observer-induced physical constraint | CONJECTURED (model only) | requires measured feedback/latch | no physical experiment |

See NEXT.md for preregistered falsification criteria and follow-up proof targets.
