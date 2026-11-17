# Virtual-Field Form Distance — Periodic Shadows, Terminal BBP Rational Norm, and the Moving Horizon

**Research continuation, 2026-11-16.**  
**Originating hypothesis (Leah):** find a metric/norm of the zero/virtual field in which distance is a function of **form approximation**. In particular, compare an authenticated infinite BBP computation with finite periodic computational paths that shadow its observations; preserve the source label, transport, and horizon rather than identifying apparently equal endpoint values.

**Claims:** VFM-01–07 are classical/elementary paper derivations in declared observer classes. VFM-08 is a new-to-SUCC exact bridge from a *single terminal rational BBP state* to the still-OPEN R0 criterion, not a new proof of any statistical bound. VFM-09 is an exact finite rational source certificate, not all-shell evidence. VFM-10 is a conditional normality/topology contrast. π base-16 normality and R0 remain **OPEN**. Mathematical priority, physical metric, quantum vacuum, temperature, entropy and universal numerical optimality of BBP are **not** claimed.

## 1. A relative norm on source-labelled forms (semidefinite before quotient)

A **form** F has a typed source passport and an evaluation/transport law. Choose a countable **declared toolkit** of bounded normalized probes O_j(F) in the complex unit disk, with positive summable weights w_j and sum w_j=1. For finite formal signed combinations v=sum_F a_F[F] in the free complex vector space on forms, set

\[
\boxed{
\|v\|_{\mathsf{Virt},\mathcal O}^2
=\sum_{j\ge1}w_j\left|\sum_Fa_F O_j(F)\right|^2.
}
\tag{VFM1}
\]

This is a positive **seminorm** in the pre-Hilbert space, and an actual norm after quotienting by the joint kernel of the probe family. For individual forms,

\[
\boxed{
d_{\mathcal O}(F,G)^2
=\sum_{j\ge1}w_j|O_j(F)-O_j(G)|^2.
}
\tag{VFM2}
\]

**VFM-01 (CLASSICAL/EXACT):** by the canonical Hilbert embedding F -> (sqrt(w_j) O_j(F)) in ell², d is a pseudometric; it is a metric exactly on the quotient by equality under all declared probes. Choosing more lawful source/pair/lag probes shrinks the kernel but does not prove source identity unless the family separates the admitted source class. The norm is **toolkit relative**. No single canonical scalar length for all coherent formal expressions follows from the concept of mathematical zero.

For w_j=2^(-j), the truncated squared distance through j=H obeys
\[
0\le d_\mathcal O(F,G)^2-d_{\mathcal O,\le H}(F,G)^2\le4\cdot2^{-H}.
\tag{VFM3}
\]
This is a bound on the *unmeasured probe weight*, not on the intrinsic causal cost of a source. Source labels, observation gradients, integer winding and gauge are typed channels; they cannot be manufactured by minimizing the numeric endpoint distance.

Connection: existing [Contextual Zero Backbone](../../../docs/CONTEXTUAL_ZERO_BACKBONE.md) and [Restricted Yoneda/CY-02–06](../../2026-11-10/cursed_categories_dedekind_yoneda/CUT_YONEDA_THEOREMS.md). The rational-cut features O_q(x)=1[q<x], enumerated across all rational q, separate irrational points; any finite probe subset leaves alternatives. Retaining source-law/action features can distinguish two forms with the same endpoint but different computation paths. An endpoint-only O does not.

## 2. A two-scale metric: finite cylinder agreement versus dynamical disagreement

Let x,y in R/Z, e(t)=exp(2πit), and define the circle-phase orbit observation
z_n(x)=e(16^nx). The **shell observer** sees n in I_B=[B,2B), with the exact phase norm

\[
\boxed{
D_B(x,y)
=\left(\frac1B\sum_{n=B}^{2B-1}|z_n(x)-z_n(y)|^2\right)^{1/2}.
}
\tag{VFM4}
\]

**VFM-02 (CLASSICAL/EXACT):** D_B is a pseudometric on the circle. Its kernel is exactly
\[
\boxed{D_B(x,y)=0\iff x-y\in16^{-B}\mathbb Z\pmod1.}
\tag{VFM5}
\]
Proof: the first sample n=B forces 16^B(x-y) integral; then all later samples agree. Thus an observer's horizon can discard *true numeric source differences*, even when both full source paths are coherent. Recording original seed and chart history avoids falsely promoting this quotient to source identity.

Let x have canonical hexadecimal digits d_1d_2..., and let L(x,y) be its common-prefix length with y (nonterminating, no infinite F ambiguity). The **symbolic cylinder ultrametric**
\[
d_{\rm cyl}(x,y)=16^{-L(x,y)}
\tag{VFM6}
\]
is an exact metric on the sequence space, but is not a canonical physical metric or globally equal to Euclidean distance on the circle. If x,y share m digits, |x-y|<=16^{-m}. The complex phase has the elementary Lipschitz bound
\[
|z_n(x)-z_n(y)|\le2\pi\,16^n|x-y|
\tag{VFM7}
\]
for selected real representatives; hence for n<=2B-1<m,
\[
\boxed{D_B(x,y)\le2\pi\,16^{2B-1-m}.}
\tag{VFM8}
\]

**VFM-03 (CLASSICAL/EXACT; periodic finite-shadow obstruction):** repeat the first m digits of x followed by one zero forever; it defines a rational periodic path q_m with the same first m digits and |x-q_m|<16^{-m} for irrational x. Choosing m=2B+K makes D_B(x,q_m)<=2π16^{-K-1}. Thus **every finite shell** can be mimicked to arbitrarily high precision by a rational periodic form if its period/budget may grow with the shell. This bound does not say the surrogate is a *short* periodic path or that it follows the authentic original BBP forcing.

The number of source digits required by this generic constructive guarantee grows linearly with B. This is a sufficient approximation cost, not a complexity-theoretic lower bound or a proof that every irrational has random digits.

## 3. One BBP rational endpoint shadows the entire shell

Retain without modification the original authenticated four signed poles:
\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\tag{VFM9}
\]

Define \(P_m=\sum_{j=1}^m16^{-j}r(j)\) in Q, and
\(x=\pi/16=P_m+16^{-m}T_m\), with **strict original-source tail**
\[
0<T_m<\beta_m:=r(m+1)/15<
\frac1{(8m+1)(8m+2)}\quad(m\ge1).
\tag{VFM10}
\]
The last rational inequality is an inherited source-four-pole bound, not a probabilistic model. Each P_m is rational, hence has an **eventually periodic** base-16 expansion; its eventual period may be enormous. It need not preserve the complete forcing/zero-seed chronology when used as a standalone radix orbit. It is a terminal *value/form approximation*, not an authenticated alternate historical source.

For shell I_B, select the single canonical source form
\[
q_B=P_{2B}=16^{-2B}U_{2B}.
\]
Then at n=2B-k with 1<=k<=B,
\[
\boxed{
16^nq_B=U_{2B}/16^k.
}
\tag{VFM11}
\]
Thus the entire **forward orbit shell** of the finite rational form is readable as a sequence of **backwards radial projections of one exact terminal BBP state**.

### VFM-04 — quantitative dynamic form-shadow norm (PROVED PAPER)

Set \(D_B=D_B(x,q_B)\). From (VFM7) and \(x-q_B=16^{-2B}T_{2B}\),
\[
D_B^2\le\frac{4\pi^2T_{2B}^2}{B}
\sum_{n=B}^{2B-1}16^{2(n-2B)}
=\frac{4\pi^2T_{2B}^2}{255B}(1-16^{-2B}).
\]
Therefore
\[
\boxed{
D_B(x,P_{2B})
\le\frac{2\pi T_{2B}}{\sqrt{255B}}\sqrt{1-16^{-2B}}
<\frac{2\pi\,r(2B+1)}{15\sqrt{255B}}
=O(B^{-5/2}).
}
\tag{VFM12}
\]

The right side contains a **strict rational source bound** and explicit constants; no π digits, random clocks or Gamma sampling are needed. The quadratic scaling as a Hilbert **phase norm** is not an intrinsic linear norm on the circle-valued points themselves. The observer metric D_B changes with the shell and source passport.

## 4. The virtual-field terminal rational norm

Define the torus distance \(\|t\|_{\mathbb T}:=\min_{m\in\mathbb Z}|t-m|\) and the **fully rational terminal energy**
\[
\boxed{
\mathcal R_B:=
\frac1B\sum_{k=1}^B
\left\|\frac{U_{2B}}{16^k}\right\|_{\mathbb T}^{\,2}.
}
\tag{VFM13}
\]
By (VFM11), this is exactly the shell average of squared circular distances of the finite rational form q_B from the distinguished zero phase.

For 0<=d<=1/2, the elementary sine inequalities give
\[
8d^2\le 1-\cos(2\pi d)\le2\pi^2d^2.
\tag{VFM14}
\]
So for the rational shadow q_B,
\[
8\mathcal R_B\le1-\Re W_B(q_B)\le2\pi^2\mathcal R_B.
\tag{VFM15}
\]

### VFM-05 — exact bridge to the original π R0 frontier (PROVED PAPER)

Let \(A_B(x)=1-\Re W_B(x)\) and W_B(y)=B^(-1)sum_{n=B}^{2B-1}e(16^n y). The source approximation, averaged **before** bounding, yields
\[
|A_B(x)-A_B(q_B)|
\le\frac{2\pi T_{2B}}{15B}(1-16^{-B})
<\frac{8\,r(2B+1)}{225B}
=:\rho_B.
\tag{VFM16}
\]
Proof: use |\cos a-\cos b|<=|a-b|, sum the finite geometric series of powers 16^n, insert the exact source tail bound and π<4. The source-selected signed phase is not replaced by a random variable.

Combining (VFM15–16) gives the main rational-form sandwich:
\[
\boxed{
8\mathcal R_B-\rho_B
\le1-\Re W_B(\pi/16)
\le2\pi^2\mathcal R_B+\rho_B,
\quad \rho_B=\frac{8r(2B+1)}{225B}=O(B^{-3}).
}
\tag{VFM17}
\]
The **lower bound** on the center quantity is **fully rational**; the upper bound contains the known constant π but no unknown π digits.

**Consequently**
\[
\boxed{
\text{Main XXVI R0 for π}
\iff
\liminf_{B\to\infty}\mathcal R_B>0.
}
\tag{VFM18}
\]
Proof: \(\rho_B\to0\). The lower inequality yields a positive eventual gap when liminf R_B>0; conversely an eventual gap A_B>=η and the upper inequality imply R_B>η/(4π²) eventually. This is a rigorously equivalent **source-rational** criterion. It does NOT prove liminf R_B>0. The unknown statistical claim has become a quantitative source recurrence/cofactor problem rather than disappeared.

In particular, the previous R0 gate in [Main XXVI PI_NORMALITY_FRONTIER](../../../docs/PI_NORMALITY_FRONTIER.md) is **not** promoted in status. The statement is an exact equivalence and a new compact form-interface in SUCC, not a resolution of an open number-theoretic problem.

## 5. A purely combinatorial sufficient condition from terminal hexadecimal digits

Let \(U_{2B}=C_{2B}+u_{2B}\) with integer \(C_{2B}=\lfloor U_{2B}\rfloor\) and \(0\le u_{2B}<1\). For k>=1, write the kth least significant hexadecimal digit of C as \(d_k(C)\in\{0,\ldots,15\}\).

If \(d_k(C)\in\{4,\ldots,11\}\), then
\[
\frac14\le\left\{\frac{C+u}{16^k}\right\}<\frac34
\]
and therefore \(\|(C+u)/16^k\|_{\mathbb T}\ge1/4\).

**VFM-06 (EXACT source-digit certificate):** writing
\(M_B=\#\{1\le k\le B:d_k(C_{2B})\in\{4,\ldots,11\}\}\),
\[
\boxed{
\mathcal R_B\ge\frac{M_B}{16B}.
}
\tag{VFM19}
\]
Hence if the **literal original four-pole zero-seeded** \(C_{2B}\) has a positive fraction of central hexadecimal digits in its terminal B-digit window on **every sufficiently late shell**, then R0 follows.

This condition is substantially stronger than R0 and is **OPEN**. It is not a novel digit-frequency theorem, nor a full normality criterion; normality would imply various digit frequencies, but the converse is false. The source-specific bridge is that the digits are read from one **rational terminal state**, not assumed as independent outcomes.

## 6. Executed finite exact-rational certificates

The isolated stdlib Fraction implementation takes the literal original source through \(U_{512}\); the two routes (chronological U_m recurrence and direct P_m sum) agree exactly. The following entries are **decimal views of exact rational values**, not floating π phase calculations. The lower comparison A_B>3/5 is tested with full Fractions for each listed B:

| B | Rational terminal \(\mathcal R_B\) | Exact-rational lower bound \(8\mathcal R_B-\rho_B\) | Central terminal digits \(M_B\) |
|---:|---:|---:|---:|
| 16 | 0.075084310973 | 0.600673990707 | 6 |
| 32 | 0.079825201617 | 0.638601550083 | 14 |
| 64 | 0.088161132374 | 0.705289051089 | 33 |
| 128 | 0.089051047282 | 0.712408377266 | 66 |
| 256 | 0.089039450341 | 0.712315602606 | 142 |

**VFM-07 (OBSERVED FINITE EXACT):** for B in {16,32,64,128,256}, the original π source has the rigorously *finite-shell* bound
\[
\boxed{1-\Re W_B(\pi/16)>\frac35.}
\tag{VFM20}
\]
The calculations exploit the earlier classical BBP identity, inherited source tail and elementary trigonometric inequalities; the finite shell statistics had already been investigated in prior SUCC work. **No new held-out all-shell fact, digit normality, Gamma independence, or physical temperature is inferred.**

The exact tested implementation and SHA are in [the validation receipt](VIRTUAL_FIELD_FORM_METRIC_VALIDATION.md).

## 7. Why metric approximation can be accurate while inference still fails

**VFM-08 (NO-GO / classical topology):** rational periodic forms are dense in the digit-prefix (cylinder) topology. Every finite set of time observations can be matched arbitrarily well by a periodic rational shadow. Therefore no finite-prefix similarity or arbitrarily small D_B(x,q_B) certifies that the infinite target is normal or nonnormal.

The *asymptotic* orbit pseudometric
\[
\boxed{
d_{\mathrm{asym}}(x,y)=
\limsup_{N\to\infty}\left(
\frac1N\sum_{n=0}^{N-1}|e(16^nx)-e(16^ny)|^2
\right)^{1/2}
}
\tag{VFM21}
\]
is a pseudometric (triangle by Minkowski and limsup) and can identify distinct irrational/rational endpoints, for example an irrational with increasingly sparse nonzero digits can lie at asymptotic zero distance from the locked source. In symbolic dynamics, the related upper-density/Hamming version is the classical **Besicovitch pseudometric**; see [Generic points for dynamical systems with average shadowing](https://link.springer.com/article/10.1007/s00605-016-1002-1), and [Aveni–Leonetti, Most numbers are not normal](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/most-numbers-are-not-normal/1009E3D2347D089271A324BF6DC43EFE), for relevant dynamical/topological context.

**VFM-09 (CONDITIONAL, NOT ABOUT π):** if some x is already known to be normal to base 16, then for each **fixed** rational q the cross-phase average of e(16^n x)conj(e(16^n q)) vanishes by splitting into residue classes of q's eventually periodic radix orbit and the normality of x in radix powers. Thus \(\lim_{B\to\infty}D_B(x,q)=\sqrt2\). Conversely for each fixed B, the periodic prefix shadows q_m satisfy \(\lim_{m\to\infty}D_B(x,q_m)=0\). In the normal case, these two orders of limits disagree. **Nothing here presumes or proves normality of π.**

In fact, the earlier sparse irrational hostile source \(x_\star=3/16+\sum_{j\ge1}16^{-4^j}\) has subsequential \(D_{B_j}(x_\star,0)\to0\). The presence of an irrational endpoint and infinitely many unbounded source distinctions does not force positive asymptotic escape from the zero-phase reference.

No positive physical heat, entropy production, computation-time lower bound, or claim that BBP is maximally compressed is deduced from these pseudometrics. The "virtual field" is a **chosen observation space with a stated source passport**, and its zero is a toolkit-relative equivalence class.

## 8. The exact source-specific frontier is now one endpoint's trailing digit/CRT problem

The decisive claim would be:
\[
\boxed{
\exists \delta>0,\ B_0\ \forall B\ge B_0:
\quad
\frac1B\sum_{k=1}^B
\left\|\frac{U_{2B}}{16^k}\right\|_{\mathbb T}^2\ge\delta.
}
\tag{VFM22 — OPEN}
\]

This is an exact reformulation of R0, not a novel proof method by itself. The more restrictive central-digit criterion in VFM19 is sufficient, not necessary. The actual pressure point is to exploit the **odd-denominator/coprime cofactor ancestry and zero-seed** of the rational terminal state to prevent most k from simultaneously lying near integer-aligned radix sublattices. Equivalently, identify a source-derived obstruction to a long approximate fixed-point shadow by one highly structured finite rational form.

Required hostile controls before status promotion:
- Coherent changed seed s=-x gives U_m(s)=-T_m, hence terminal radial energy tending to zero; source-only forcing cannot exclude this without the literal zero seed.
- Other rational locked and fixed-nonunit orbits, including x=0,1,1/15, separate R0 from generic rational periodicity.
- Generic periodic prefix shadows with period allowed to grow with B show why finite source approximation alone is insufficient.
- Source coboundary g(n)=2n² with corrected tail preserves completed π but changes integer/terminal rational winding. VFM13 is gauge/source-presentation dependent and must NOT be called invariant under such mutants without a separately transported corrected gauge.
- Phase-erased or Gamma-only scalar readouts cannot authenticate the signed source; retaining the full complex phase, time and source labels is essential.
- Approximating an asymptotic pseudometric with one finite shell is not a universal certificate. Finite checks cannot validate the liminf.

**Next action:** derive a nontrivial lower bound in (VFM22) from the source prime/cofactor clock or certified integer-carry digits. Predeclare quantifiers, exclude mutant aliases, and prove the needed weighted density. A fresh holdout beyond n=131072 is useful for testing new finite predictions only after a source-derived inequality is stated; computation never upgrades finite evidence into the all-B proof.

**Dependencies and provenance:** [SUCC CY-02–08, Dedekind–Yoneda](../../2026-11-10/cursed_categories_dedekind_yoneda/CUT_YONEDA_THEOREMS.md); [BBP source and R0](../../../docs/PI_NORMALITY_FRONTIER.md); [moving frame](MOVING_FRAME_THIRD_LAW_INTERFEROMETRY.md); [source-shadow pair energy](SOURCE_SHADOW_INTERFEROMETRY.md); [adaptive Gamma complex defect](ADAPTIVE_GAMMA_ICE_CLIMB.md); [original Gamma source/Haar knowledge](../../2026-11-14/gamma_volume/THEOREMS.md); [Method](../../../docs/METHOD.md). Classical harmonic inequalities and original BBP coefficients are inherited/shared; repeating them in another observer basis is not independent mathematical source evidence.
