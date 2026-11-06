# HISTORY-FIRST SUCC: chiral shell duality, arithmetic branch pinning and causal observation bookkeeping

**2026-11-05. Research-only mathematical dossier.** Strict additive descendant of #521 exact head 7f26807a26ec3167005ed5bec7a021da49fe9b7a. No change to the original four signed BBP poles, literal U_0=0, frozen contracts, main, production or Lean. Classical probability ensembles and optional Hilbert encodings are not physical quantum claims or a proof of π base16 normality.

## Source, history and the exact finite shell

Use original \(r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)\in\mathbb Q\), \(U_0=0\), \(U_{n+1}=16U_n+r(n+1)\). Let \(x_n=\{U_n\}\), and let
\[
S_k(n)=\sum_{j=1}^{k}16^{k-j}r(n+j),
\quad x_{n+k}=\{16^k x_n+S_k(n)\}.
\]
The source bookkeeper \(H_N\) records all unwrapped rational \(U_n\), literal signed \(r(n)\), and integer carries \(c_{n+1}=\lfloor16x_n+r(n+1)\rfloor\) for \(0\le n<N\). Forgetting the latest source step defines consistent chronological restriction maps \(H_{N+1}\to H_N\). This is deterministic evidence **within the authenticated source model**, not a finite oracle for all-time orbit frequencies.

### HS-01: one exact binary microstate decision closes any finite shell

For m,k≥1 write
\[
a=\lfloor16^{m+k}x_n\rfloor,\quad
\theta=\{16^{m+k}x_n\},\quad
q=\lfloor16^m S_k(n)\rfloor,\quad
\delta=\{16^m S_k(n)\}.
\]
Since \(16^{m+k}x_n=a+\theta\), the future output m-digit cell is exactly
\[
\boxed{
\lfloor16^m x_{n+k}\rfloor
=\left(a+q+\mathbf1_{\{\theta+\delta\ge1\}}\right)\pmod{16^m}.}\tag{HS1}
\]
This is valid for all input real states, all source values, and all finite depths. A fixed input prefix a and known source admit at most TWO adjacent future m-digit outcomes. The actual rational SUCC state determines θ and therefore chooses one. No random variable is needed for the TRUE path.

If the observer explicitly chooses **uniform conditional measure inside that fine input cylinder**, θ is Haar on [0,1), so predicted outcome probabilities are exactly \(1-\delta,\delta\). These probabilities belong to the internal ensemble and do not determine the selected bit unless θ is observed.

Using the uniform all-m original bound from #521, for n≥2:
\[
\boxed{
\left|16^m S_k(n)-\frac{16^m(16^k-1)}{64n^2}\right|
<\frac{16^{m+k}}{10n^3}.}\tag{HS2}
\]
Thus this source-induced branch threshold becomes order one when \(16^{m+k}\asymp n^2\), providing a rigorous **spatial resolution versus causal lookahead tradeoff**. It does not itself guarantee a particular selected branch frequency.

### HS-02: the dual direction is actual pushforward/pullback, NOT automatic physical chirality

For a continuous map F and a finite Borel measure μ, define state transport \(F_*\mu\) and observable transport \(F^*f=f\circ F\). The exact duality is
\[
\boxed{\int f\,dF_*\mu=\int(F^*f)\,d\mu.}\tag{HS3}
\]
At each source step, \(T_r(x)=16x+r\bmod1\) is a degree16 orientation-preserving circle cover. Its CP1 stage on the boundary is \(P_r(z)=e(r)z^{16}\), exactly the #516 source-covering stage.

The **fine radix prefix** \(a_m(x)=\lfloor16^m x\rfloor\) obeys \(a_m=\lfloor a_{m+1}/16\rfloor\), forming a rooted 16-branch LEFT-prefix system. Conversely a FIXED endpoint z0 has 16 inverse-root choices per stage under \(P_r\). Choosing any reference compatible inverse-root history \((z_j^0)\), all others differ by multipliers \(\xi_j=z_j/z_j^0\) with \(\xi_{j-1}=\xi_j^{16}\), \(\xi_0=1\). Thus the fixed-endpoint fiber is a torsor for
\[
\boxed{\varprojlim_m\mu_{16^m}\cong
\varprojlim_m\mathbb Z/(16^m)=:\mathbb Z_{16}.}\tag{HS4}
\]
The finite index \(j_m\) is reduced modulo \(16^{m-1}\), whereas the prefix integer a_m is truncated by division by16. Reversing the ordered digit sequence gives an isomorphism of underlying ROOTED SYMBOLIC TREES: \(a_m=\sum_{i=1}^md_i16^{m-i}\) versus \(j_m=\sum_{i=1}^md_i16^{i-1}\). It is NOT generally a group isomorphism, a conjugacy of source dynamics, or a canonical probability transport. The inverse-root fiber is Cantor-like; the full solenoid inverse limit of circles is connected. The real-digit symbolic space maps onto the circle with countable radix-expansion ambiguity.

**Chronological orientation:** The actual original source orbit satisfies \(z_{n+1}=P_{r(n+1)}(z_n)\) FORWARD. A fixed-endpoint backward inverse-root history in HS4 is a family of counterfactual past roots, not automatically this same forward record. A selected source root and a chosen time endpoint are additional data.

### HS-03: arithmetic odd torsion selects ONE branch in the 16-fold sphere cover

Every authentic r(n) has ODD reduced denominator; from U0=0 and integer ×16, every U_n also has odd reduced denominator. Let \(\mu_{\mathrm{odd}}\subset S^1\) denote ALL roots of unity of odd order. The source phase e(r(n)) lies in \(\mu_{\mathrm{odd}}\).

**Arithmetic inverse theorem:** The map
\[
\boxed{P_{r(n)}:\mu_{\mathrm{odd}}\to\mu_{\mathrm{odd}},\
z\mapsto e(r(n))z^{16}}
\tag{HS5}
\]
is a BIJECTION for every source step. Indeed raising to the 16th power is an automorphism on every finite odd-order cyclic group (16 is coprime to its order), and translation by an odd-order root preserves the subgroup. Given one odd-order output and an odd-order source twist, of the 16 circle roots EXACTLY ONE has odd order; the other 15 have an even-order factor. The original source arithmetic therefore selects a unique backward branch among the 16 geometric inverse sheets.

This is a precise source-admissibility result, NOT a proof of normality: the inverse restricted to the DENSE, nonclosed subgroup \(\mu_{\mathrm{odd}}\) is not continuous in the ambient circle topology. To see this at the trivial source twist, take odd denominators \(q_t^+=16t+1\), \(q_t^-=16t-1\). Inputs \(e(1/q_t^\pm)\to1\), but their unique odd-order 16th roots have phases
\[
\frac{15}{16}+\frac{1}{16q_t^+}\to\frac{15}{16},
\qquad
\frac{1}{16}+\frac{1}{16q_t^-}\to\frac{1}{16},
\]
whereas the unique odd-order root of 1 is 1 itself (phase0). Thus exact odd-order branch selection is DISCONTINUOUS in the ordinary circle observation topology. Exact finite-state arithmetic is stronger than geometric branch identification, but it is not a stable inverse for empirical distribution limits.

Changing the original source taps while retaining odd denominators may preserve HS5. Odd-torsion membership authenticates an arithmetic DOMAIN, not the four-pole formula nor its unique zero seed. Original rational odd initial shifts also remain admissible, and nonnormal unforced odd-torsion examples exist.

### HS-04: coarse reinjection of uniformity breaks source-causal composition

Consider an observer who starts with a UNIFORM microstate on one fine depth-(m+2) input cylinder, observes the middle depth-(m+1) cell after T_{r1}, and finally predicts a depth-m cell after T_{r2}. Define
\[
\delta_1=\{16^{m+1}r_1\},\quad\delta_2=\{16^m r_2\},\quad0<\delta_j<1.
\]
The correct direct two-step transition is driven by the ONE shared latent remainder and has two adjacent outcomes with the second-step carry offset \(\lfloor\delta_1+\delta_2\rfloor\) and final split \(\{\delta_1+\delta_2\}\).

If the observer forgets that remainder and RESETS the conditional distribution to uniform across each entire middle cell, it instead convolves two independent Bernoulli decisions with parameters δ1 and δ2, allowing three outcomes. A direct finite calculation (for 16^m≥3, so labels are distinct) gives
\[
\boxed{
\mathrm{TV}(P_{\mathrm{direct}},P_{\mathrm{reuniformized}})
=2\min(\delta_1\delta_2,(1-\delta_1)(1-\delta_2)).}\tag{HS6}
\]
**Proof:** if δ1+δ2≤1, the correct distribution on relative indices 0,1,2 is (1−δ1−δ2, δ1+δ2,0); the reset distribution differs by (a,−2a,a), a=δ1δ2. If δ1+δ2≥1, the correct distribution is (0,2−δ1−δ2,δ1+δ2−1), and a=(1−δ1)(1−δ2). The half L1 norm is 2a.

**Exact base16 falsifier:** initial x uniform on [0,1/4096), stage r1=1/512, stage r2=1/32. Direct output is uniform on [1/16,1/8), entirely within final cell1. Resetting to Haar within the two intermediate cells predicts cells0/1/2 with weights 1/4,1/2,1/4. TV=1/2. The same phenomenon appears with ORIGINAL four-pole source at n=13,m=2, with exact rational δ1,δ2 and TV≈0.2161680649233 (original-source numerical display of exact rational).

This is a rigorous **non-lumpability of a particular history-conditioned coarse projection**. It does NOT say the true circle dynamics are stochastic or that every coarse observer law fails Markovianity. The correct repair is to preserve the conditional microstate distribution/support intervals and source history until after propagation; then update the posterior using the actually observed output.

### HS-05: nested classical probability and nested quantum-state functors are compatible, but not automatically entangled

Given a consistent family of prefix-cylinder probabilities \(p_m(w)\), with \(p_m(w)=\sum_{d=0}^{15}p_{m+1}(wd)\), define a diagonal density matrix on \(H_m=(\mathbb C^{16})^{\otimes m}\):
\[
\boxed{\rho_m=\sum_{w\in\{0,\ldots,15\}^m}
 p_m(w)|w\rangle\langle w|,\qquad
 \mathrm{Tr}_{m+1}\rho_{m+1}=\rho_m.}\tag{HS7}
\]
This is a faithful embedding of classical prefix MEASURES into compatible QUANTUM-STATE FORMATS, but every such diagonal density is separable across the tensor factors. The pure actual full-history basis state is also a PRODUCT state. Nontrivial entangled/offdiagonal amplitudes require independent new Hilbert/phase choices (as in SUCC #512). Neither the 16-adic inverse-root torsor nor the classical probability restriction selects those phases canonically.

### HS-06: exact Haar-SEED digits are IID for ALL deterministic source forcing

Let initial seed S be uniform on circle, x0=S and x_(n+1)={16x_n+r(n+1)}. Let \(D_n=\lfloor16x_n\rfloor\in\{0,\ldots,15\}\). For ANY deterministic forcing, EVERY finite word \((d_0,\ldots,d_{L-1})\) has probability
\[
\boxed{\Pr_S(D_0=d_0,\ldots,D_{L-1}=d_{L-1})=16^{-L}.}\tag{HS8}
\]
**Proof by induction:** x0 is Haar. Conditional on any past digit word through n−1, x_n is Haar because the previous x_{n-1}, after conditioning on its digit, is uniform on that one cell of length1/16, and \(T_r\) carries each full digit cell bijectively (mod endpoints) onto the entire circle with normalized Haar measure. Thus D_n is uniform and independent of previous digits, and conditioning on D_n again gives uniform x_n in its digit cell. Repeating yields HS8.

This is an important baseline NO-GO: the randomized initial-seed virtual field has a PERFECTLY NORMAL first-digit process even for ZERO forcing, whose actual selected s=0 orbit is the constant zero. All SOURCE fingerprints are lost from this one-digit Haar-ensemble output distribution. They remain in exact real-phase multitime observables and the deterministic history record. No probability-one statement about S includes the actual chosen zero seed by logic alone.

The existing #521 ensemble second and third source carry moments refer to DIFFERENT source-dependent moving-window observables, so HS8 does not contradict their nonzero higher-order correlations.

### HS-07: Koopman–transfer chiral pair, exactly source labelled

On Haar \(L^2(\mathbb T)\), define \(K_r f=f\circ T_r\) and its adjoint Perron–Frobenius \(P_r=K_r^*\), given by uniform averaging over the 16 geometric preimages:
\[
\boxed{
(P_r g)(y)=\frac1{16}\sum_{j=0}^{15}
g\!\left(\left\{\frac{y-r+j}{16}\right\}\right).}\tag{HS9}
\]
Because T_r preserves Haar, \(K_r\) is an isometry and \(P_rK_r=I\). With \(e_h(x)=e(hx)\):
\[
\boxed{
K_re_h=e(hr)e_{16h},\quad
P_re_k=\begin{cases}
e(-\tfrac{k}{16}r)e_{k/16},&16\mid k,\\0,&16\nmid k.
\end{cases}}\tag{HS10}
\]
Therefore \(K_rP_r=\Pi_{16}\) is the ORTHOGONAL projection onto characters at multiples of16, independent of source. The complementary subspace
\[
\boxed{\ker P_r=\overline{\mathrm{span}}\{e_k:16\nmid k\}}
\tag{HS11}
\]
is the exact inverse-branch information discarded by Haar fiber averaging. This is an actual one-way isometry/coisometry duality—the mathematically defensible "chiral" pair. The source phase survives in the maps themselves but not in the projection \(\Pi_{16}\). The kernel is classical harmonic-analysis information, NOT virtual quantum energy or a π digit distribution theorem.

**The point-evaluation barrier is quantified exactly:** for fixed h≠0 and actual source states \(u_n=U_n(0)\), let
\[
W_{A,h}(s)=\frac1A\sum_{n=A}^{2A-1}e(hu_n)e(h16^n s).
\]
The frequencies h16^n are distinct, so for EVERY forcing
\[
\boxed{\int_0^1 W_{A,h}(s)\,ds=0,\quad
\|W_{A,h}\|_{L^2(ds)}^2=\frac1A.}\tag{HS12}
\]
But the observation at the exact selected seed s=0 is
\(W_{A,h}(0)=A^{-1}\sum e(hU_n(0))\), the original STILL-OPEN Weyl sum.
On the A-dimensional frequency space spanned by these character modes, evaluation at0 has operator norm \(\sqrt A\); its amplification cancels the ensemble's \(A^{-1/2}\) norm saving exactly. With unforced r=0, W(0)=1 even though the ensemble norm→0.

This is a particularly transparent diagnostic of why source-neutral virtual-field concentration cannot prove the actual selected orbit mixes. Keeping the exact historical coefficient phases e(hu_n) is necessary; a new arithmetic restriction on THEIR sum is what remains unproved.

### HS-08: an observer that predicts, probes and BOOK-KEEPS—but cannot declare π normal

Fix a hypothesis family \(\mathcal H\) with explicit priors or admissibility constraints and an observation filtration \(\mathcal F_{n,m}\). Conditional predictions must be \(\nu(\cdot\mid\mathcal F_{n,m})\) computed from the ACTUAL propagated underlying measure, not a fresh full-cell Haar reset each time. The exact source history supplies the realized branch bit \(b_{n,m,k}=\mathbf1_{\{\theta_n+\delta_n\ge1\}}\). Given a chosen uniform-microstate model, the discrepancy
\[
J_{A,m,k}(0)=\frac1A\sum_{n=A}^{2A-1}(b_{n,m,k}-\delta_{n,m,k})
\]
tests that model against the exact arithmetic path. The source alone computes the delta and its binary-entropy forecast; actual U0=0 computes the branch. One may choose next experiments by predicted information gain, **after declaring the hypothesis class and preregistering the holdout**.

Original predeclared finite epochs A=173,347,691 and k=1,2 show the model's expected branch counts differ from actual selected counts; both are exactly computed Fractions, not independent random samples. No law of large numbers for J at s=0 has been proved, and J→0 for one critical schedule is not known to imply \(\mathcal Q_{1/2}(\mu_A)\to0\).

**A full exact seed and source history already has a Dirac posterior over the actual dynamical state.** Nontrivial probabilities must represent explicitly incomplete observations, alternative source hypotheses, unknown parameters, or limited computational resources. They are not additional metaphysical randomness in π.

## Verdict

Disclosed within stated models: exact two-cell source shell, inverse-root torsor, unique but unstable odd-torsion arithmetic inverse, non-lumpability, classical/quantum nested-state compatibility, IID Haar initial-seed single-digit process, Koopman/transfer defect subspace and the exact \(1/A\) ensemble L² vs point-evaluation amplification. These are exact classical/categorical tools newly integrated into this SUCC research line; worldwide scholarly priority is NOT established.

**OPEN:** arithmetic bound on the genuine source-selected J or on original \(\mathcal Q_{1/2}(\mu_A)\to0\), original signed fixed-h Weyl sums, π base-16 normality, RH. A virtual ensemble trained or conditioned only on its own source-neutral observations cannot settle the selected history's distribution. The next theorem must use zero-selected rational numerator/carry phases beyond an equivalent representation.

Supporting classical references: inverse-limit solenoid fiber https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/robert.pdf ; source-parent SUCC #516 sphere coverings, #512 compatible quasilocal states, #521 critical source truncation. No physical quantum phenomena are inferred from these mathematical analogies.
