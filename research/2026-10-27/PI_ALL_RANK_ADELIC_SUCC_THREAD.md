# Operation Rank-2 → All Ranks: adelic SUCC and the selected π thread

**October 27, 2026. Draft research child of #330** (which is based on #328). Read this with the claim supplement and exact Python instruments. The full signed four-pole source, its authentic zero initial state, frozen provenance and main are unchanged. π base-16 normality and RH are **OPEN**. Classical higher-rank solenoids and the Rudolph–Johnson theorem are attributed; scholarly priority for the new source-relative derivations is unverified.

## 0. Object and the real/adic type boundary

Retain the original canceled signed BBP source and zero-selected recurrence:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
$$

Inherited from #323–#324, for n≥1:

$$
U_n=16^{n-1}\pi-T_n,\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
0<T_n<\frac1{15(n+1)^2}.
$$

The authentic 2-adic U clock in #321, 3-adic **cleared numerator** A(n) clock in #322, and real winding memory in #330 are different observable types. A(n) is *not* a 3-adic U state; source poles invalidate that identification. Two coordinates do not yet give dynamical rank two. The latter requires multiplicatively independent commuting generators.

## AR-1: a canonical thread through every finite rank (CLASSICAL)

For a finite nonempty prime set S, let Z[S^{-1}] be the localization of Z. The compact S-arithmetic solenoid is

$$
X_S=\frac{\mathbb R\times\prod_{p\in S}\mathbb Q_p}
{\Delta\mathbb Z[S^{-1}]},\qquad
\widehat X_S\cong\mathbb Z[S^{-1}].
$$

For S={2}, this is the dyadic SUCC solenoid of #330. For S={2,3}, **both ×16 and ×3 act by automorphisms**, defining a genuine commuting rank-2 Z²-action. ×3 on the **2-only** solenoid is NOT an automorphism, because its dual action on Z[1/2] is not surjective. Enlarging S repairs that precise type error.

For S⊂S', dualizing Z[S^{-1}]⊂Z[S'^{-1}] gives a surjective factor X_{S'}→X_S. The union of all such character groups is Q, so the common all-rank carrier is

$$
X_{\mathrm{all}}=\mathbb A_{\mathbb Q}/\Delta\mathbb Q
\cong\widehat{\mathbb Q}
\cong\varprojlim_S X_S.
$$

Multiplication by every nonzero rational acts as an automorphism on this universal compact group. Each actual real state u has a continuous real-leaf lift j_R(u), and its projections to each finite S are coherent. **This is a common carrier; it is not independence or Haar genericity.**

Sources: [Einsiedler–Lindenstrauss, commuting automorphisms on tori and solenoids](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/rigidity-properties-for-commuting-automorphisms-on-tori-and-solenoids/B5B7471AB9A282B5B179E35040809159); [Garrett, adeles and solenoids](https://www-users.cse.umn.edu/~garrett/m/mfms/notes_2013-14/12_1_adeles.pdf); [Bourgain–Lindenstrauss–Michel–Venkatesh, effective ×a×b](https://math.stanford.edu/~akshay/research/blmv.pdf).

## AR-2: authenticated flat rank-r source lattice (PROVED LOCAL)

Fix independent integer multipliers q_2,...,q_r≥2, e.g. 3,5,7,..., and for a transverse multi-index m=(m_2,...,m_r) put

$$
Q_m=\prod_{j=2}^rq_j^{m_j},\qquad
V_{n,m}=Q_mU_{n+1}\quad(n\ge0).
$$

The source-retaining horizontal and unforced transverse updates are exactly

$$
V_{n+1,m}=16V_{n,m}+Q_m r(n+2),\qquad
V_{n,m+e_j}=q_jV_{n,m}.
$$

Both paths around each elementary square agree:

$$
q_j(16V_{n,m}+Q_mr(n+2))
=16q_jV_{n,m}+q_jQ_mr(n+2).
$$

The general compatibility condition, for W(v+e_i)=q_iW(v)+ω_i(v), is

$$
q_j\omega_i(v)+\omega_j(v+e_i)
=q_i\omega_j(v)+\omega_i(v+e_j).
$$

Consequently path-comparison across all finite ranks is exact. It **does not prove mixing**. The same squares close for the source-preserving changed real selector U'_n=−T_n (initial seed −π/16), whose real phases converge to one. Thus source identity + flatness without the zero selector has an explicit bad control.

## AR-3: NEW quantitative all-rank Green-tail transport corridor (PROVED LOCAL)

For an integer h, N≥1 and widths M_j≥1, write e(t)=exp(2πit) and

$$
F^{SUCC}_{N,\mathbf M}(h)=
\frac1{N\prod_jM_j}\sum_{n=0}^{N-1}
\sum_{0\le m_j<M_j}e(hQ_mU_{n+1}),
$$

$$
F^{\pi}_{N,\mathbf M}(h)=
\frac1{N\prod_jM_j}\sum_{n=0}^{N-1}
\sum_{0\le m_j<M_j}e(h16^nQ_m\pi).
$$

**Theorem AR-3 (paper derivation with full quantifiers):**

$$
\boxed{
|F^{SUCC}_{N,\mathbf M}(h)-F^{\pi}_{N,\mathbf M}(h)|
\le \frac{4\sqrt{\pi|h|/15}}{N\prod_jM_j}
\prod_{j=2}^r\frac{q_j^{M_j/2}-1}{\sqrt{q_j}-1}.
}
$$

For h=0 the difference is identically zero.

**Proof.** From the authentic Green tail, Q_mU_{n+1}=16^nQ_mπ−Q_mT_{n+1}. Hence the absolute phasor difference is at most

$$
\min(2,2\pi|h|Q_mT_{n+1})
\le\min\left(2,\frac{2\pi|h|Q_m}{15(n+2)^2}\right).
$$

For any t≥0, monotone summation yields the explicit integral majorant

$$
\sum_{n=0}^\infty\min(2,t/(n+2)^2)
\le\int_0^\infty\min(2,t/x^2)\,dx
=2\sqrt{2t}.
$$

Take t=2π|h|Q_m/15, sum over the finite transverse box, use the product identity
Σ_m sqrt(Q_m)=∏_j (q_j^{M_j/2}−1)/(sqrt(q_j)−1), and divide by N∏M_j. QED. No independence, mixing, or Haar input occurs anywhere in the proof.

**Rank two, q_2=3:**

$$
\boxed{
|F^{SUCC}_{N,M}(h)-F^{\pi}_{N,M}(h)|
\le\frac{4\sqrt{\pi|h|/15}}{NM}
\frac{3^{M/2}-1}{\sqrt3-1}.}
$$

For M=floor(2log_3 N), this is O_h(1/log N)→0. More generally M=c log_3 N+O(1) for 0<c≤2 is allowed. At arbitrary fixed finite rank, widths M_j=c_j log_{q_j}N+O(1) with c_j>0 and Σ c_j≤2 give vanishing normalized transport error; the boundary equality uses ∏M_j as a log denominator. This is a genuine growing-width source-to-target theorem, **not a new signed cancellation bound**.

The committed Python module implements a conservative *rational certificate* of the bound using π<22/7 and integer square-root ceilings, and preserves exact original rational source values.

## AR-4: the missing rank-one slice is a weighted cochain boundary (PROVED LOCAL)

Let f_0,...,f_{M−1} be arbitrary complex values, e.g.

$$
f_m=\frac1N\sum_{n=0}^{N-1}e(h3^mU_{n+1}).
$$

Exact telescoping gives

$$
\boxed{
f_0=\frac1M\sum_{m=0}^{M-1}f_m
+\frac1M\sum_{m=0}^{M-2}(M-1-m)(f_m-f_{m+1}).}
$$

The first term is the two-dimensional bulk average. The second is the weighted **transverse trace defect**, which does not vanish automatically. Exact hostile receipt f=(1,−1): bulk 0, transverse defect 1, original slice 1. Any argument deducing base-16 normality from rank-2 Haar without controlling that defect is **REFUTED**.

For all ranks, let A_j be averaging along axis j and D_j this weighted finite difference. Evaluation of an array at all transverse indices zero factors as

$$
\boxed{
f(\mathbf0)=\prod_{j=2}^{r}(A_j+D_j)f
=\sum_{I\subseteq\{2,\ldots,r\}}
\left(\prod_{j\in I}D_j\right)
\left(\prod_{j\notin I}A_j\right)f.}
$$

This is an exact all-rank SUCC cochain/homotopy decomposition. The rank-r Haar bulk is just the empty-subset term. There are 2^{r−1}−1 further signed trace/mixed-difference obligations; geometric rank raising cannot erase them.

## AR-5: what rank-two measure rigidity WOULD actually buy

For a real α define the unaveraged rank-one empirical measure

$$
\mu_N^\alpha=\frac1N\sum_{n=0}^{N-1}\delta_{\{16^n\alpha\}}.
$$

Every weak-* limit is ×16-invariant by the trivial telescoping boundary. The **genuine transversal hypothesis**, not automatic rank-2 averaging, is

$$
\boxed{
D^{(3)}_{N,h}(\alpha)=\frac1N\sum_{n=0}^{N-1}
\big[e(3h16^n\alpha)-e(h16^n\alpha)\big]\to0
\quad\text{for each fixed }h\ne0.}
$$

If this is proved, every rank-one weak-* limit is also ×3-invariant, because trigonometric polynomials uniformly approximate continuous functions. For the actual four-pole source the analogous U_{n+1} defect differs by O_h(1/N), from inherited summable Green transport. **This condition remains UNVERIFIED for π.**

Rudolph–Johnson: a jointly ×16/×3-invariant *ergodic* measure with positive ×16 entropy is Haar. For a nonergodic invariant μ of entropy η log16, the general result is only μ≥η Haar; a singular zero-entropy component might survive. Therefore a sufficient route for π normality is (i) the unaveraged transverse defects vanish and (ii) **every** jointly ergodic component of **every** resulting weak limit has positive ×16 entropy. These hypotheses are much stronger than the presently proved 2-adic clock and source reconstruction.

**Strong hostile counterfeit:** Becher–Slaman show existence of α normal to base 3 but not base 16. For each fixed n and h≠0, the m-average e(h16^n3^mα) tends to zero by base-3 normality. Choose successively N_j→∞ and M_j so large that all fixed-frequency rank-2 rectangle means are <1/j. Then along rectangular Følner subsequences the rank-two empirical measures are Haar, yet α is **not** base-16 normal. Hence even perfect rank-2 rectangle Haar along a schedule does not recover the original slice. The AR-4 transverse defect is the precise missing information.

Sources: [Rudolph 1990](https://doi.org/10.1017/S0143385700005629), [effective Rudolph–Johnson theorem](https://math.stanford.edu/~akshay/research/blmv.pdf), [Becher–Slaman 2014](https://academic.oup.com/jlms/article-abstract/90/2/472/2939245). Furstenberg rank-two **orbit density** is known for irrational α but density is not equidistribution.

## AR-6: the next verdict-changing source-specific probe

The genuine open normality criterion is still

$$
\forall h\in\mathbb Z\setminus\{0\}:\qquad
N^{-1}\sum_{n=0}^{N-1}e(hU_{n+1})\to0.
$$

Two serious routes now have explicit acceptance criteria:

1. **Rank-two rigidity:** prove the *unaveraged* ×3-invariance defect of π vanishes, using authenticated signed rational cofactors and the independent, exact ternary digit interface in sibling PR #331; separately rule out zero-entropy components of any source-selected joint-invariant limit. Only then apply Rudolph–Johnson.
2. **All-rank trace:** establish genuine signed cancellation of the rank-r bulk (whose source-to-target transport is now paid for logarithmic widths), *and* prove decay of the rank-r weighted transverse cochain correction. This must distinguish the authentic U0=0 trajectory from the unchanged-forcing future-selector −T_n and #320's nonnormal 2-adic-isometric source mutant.

The exact original source is never replaced by artificial iid digits, adic marginal Haar, a generic positive measure, or a spurious independent 3-adic U clock. A nonzero gain in the selected Weyl order must be independently tested with declared frequencies, windows, coefficients and hostile holdouts before a normality status promotion.

## Reproducibility/authority

Local isolated standard-library execution: **11 tests collected, 10 PASS, 1 SKIP** (full-native SUCC import unavailable); separate probe PASS: **150 independent four-pole identities, 45 exact finite Green identities, 1,428 exact flat squares** across ranks 2,3,4. A numerical complex-phase comparison was a finite check against an independently derived *rational* error majorant; it is not a proof. All three added Python Git blobs were byte-matched against the executed local files before committing. Full native SUCC provenance/tests, hosted CI and Lean require separate execution and are NOT claimed.

**Ledger:** AR-1 CLASSICAL; AR-2/AR-3/AR-4 PROVED LOCAL with stated assumptions; AR-5 conditional classical rigidity and exact hostile failure; π normality UNVERIFIED/OPEN.
