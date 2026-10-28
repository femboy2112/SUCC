# Operation E² — exact rank-two chiral SUCC and authentic BBP source

**2026-10-27 · Research-only child of [#331](https://github.com/femboy2112/SUCC/pull/331).** This is an additive construction using the literal original four signed BBP poles and the genuine zero seed. Main, archives, source import manifest and historical proof contracts are unchanged. **π normality (base 16 or 3) and RH remain OPEN.** Paper algebra here is distinct from external novelty priority, finite Python tests, Lean kernel checks and full hosted CI.

## 0. Recovered load-bearing E-tower context

- [#26](https://github.com/femboy2112/SUCC/pull/26): separate A/B diagonal climbing towers deliver independently checked receipts to E. E's final epistemic acceptance never erases upstream work.
- [#27](https://github.com/femboy2112/SUCC/pull/27): local Čech/Yoneda source sections glue iff all overlap holonomy obstructions vanish; local resemblance is not automatically global.
- [#28](https://github.com/femboy2112/SUCC/pull/28) and [#29](https://github.com/femboy2112/SUCC/pull/29): one common source and two abstract marginals do not construct a legal joint product or nonzero correlation. Source fibers, actual joint observations, shared target and flux must be paid.
- [#61](https://github.com/femboy2112/SUCC/pull/61): the NO-GHOST countermodel refutes inferring independent joint preparation/action from two individually surjective mini-carrier projections.
- [#308](https://github.com/femboy2112/SUCC/pull/308): the already established *classical* two-quadratic BBP kernel consists of one Gaussian rotating block and one real split block, with minimal rational transfer dimension four.
- [#319–#331](https://github.com/femboy2112/SUCC/pull/331): original selected real Weyl cancellation remains open; exact finite adic clocks and certified ternary digits do not prove it.

The new contribution is to express these earlier results as one **explicit rank-two Gaussian carrier with an actual chiral source successor and a faithful four-pole output**.

## 1. Carrier rank, two independent multiplications and chiral grading

Let $K=\mathbb Q(i)$ and define the unital coordinatewise algebra

$$
\mathcal E^{(2)}=K\oplus K,\qquad
(z,w)\cdot(u,v)=(zu,wv).
$$

It has rank **two over K**, rational dimension **four**. Its two carrier multiplications are independent. Put $g=(1+i)/2$. The two separately addressable gain actions

$$
L_+(z,w)=(gz,w),\qquad L_-(z,w)=(z,\bar g w)
$$

commute. These gains are K-linear **module actions**, not unital ring endomorphisms. They do not, by themselves, establish probabilistic independence.

Define a source-aware involution

$$
\boxed{J(z,w)=(\bar w,\bar z),\quad J^2=I,\quad J L_+ J=L_-.}
$$

The rational projectors $P_\pm=(I\pm J)/2$ yield the even and odd sectors

$$
E_+=\{(u,\bar u):u\in K\},\qquad
E_-=\{(v,-\bar v):v\in K\}.
$$

Every point is uniquely their sum. Componentwise multiplication respects the $\mathbb Z/2$ grading: $E_+E_+\subset E_+$, $E_+E_-\subset E_-$, $E_-E_-\subset E_+$. **E− is not itself a subring.** The *coordinate* carriers are independently multiplicative, while the even/odd subspaces are correlated chiral sectors.

A rigid constraint $w=\bar z$ is preserved by the paired gain $L_-L_+$ but **not by either independent one-sided gain**. The complete K² carrier is needed if independent one-sided operations are truly allowed. This is the exact #61 no-ghost distinction.

## 2. Source-selected successor: four steps expose chirality, eight steps return

For a uniquely decomposed point $x=(u,\bar u)+(v,-\bar v)$ define the rational-linear successor

$$
\boxed{
\mathcal T(x)=(gu,\bar g\bar u)+(g\bar v,-\bar g v).
}
$$

On E+ this is the Gaussian rotation $G:z\mapsto gz$. On E− it is the conjugation-twisted $H:z\mapsto g\bar z$, which obeys $H^2=I/2$. Since $g^4=-1/4$ and $g^8=1/16$, for **all** joint states

$$
\boxed{\mathcal T^4=-\frac14J,\qquad \mathcal T^8=\frac1{16}I.}
$$

The half-clock contains a genuine chiral sign; the full clock agrees across both sectors. The successor $\mathcal T$ is Q-linear but **not K-linear**, and not a unital ring map. Both statements are essential: calling it K-linear or multiplying source outputs independently would invalidate the construction.

Use bases $(1,i)$ of even and $(1,1+i)$ of odd. The rational block matrices become

$$
G=\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix},\qquad
H=\begin{pmatrix}0&1\\1/2&0\end{pmatrix}.
$$

Thus the earlier distinct two-quadratic BBP atoms arise **from a single chiral source-selected operator on rank-two Gaussian carrier**.

## 3. One macro-point generates every original signed BBP impulse

Set input $b=(2,0)\in K^2$, with even coordinate $u=1$ and odd coordinate $v=1$. Define the exact rational readout

$$
\ell((u,\bar u)+(v,-\bar v))=4\,\Re(u)-4\,\Im(v),
\qquad c_m=\ell(\mathcal T^m b).
$$

In the above rational bases, $b=(1,0,1,0)^T$, $\ell=(4,0,0,-4)$. Direct matrix inversion gives

$$
\boxed{\sum_{m\ge0}c_m t^m
=\ell(I-t\mathcal T)^{-1}b
=\frac{4(1-t)}{(1-t+t^2/2)(1-t^2/2)}.}
$$

The first 8 taps are **exactly** $(4,0,0,-2,-1,-1,0,0)$, with $c_{8k+j}=16^{-k}c_j$ for every $k\ge0$. The finite 4×4 Hankel determinant $\det[c_{i+j}]_{0\le i,j<4}=4$, so rational linear time-invariant realization dimension at least four is required; this rank-two K carrier attains rational dimension four. This does **not** assert minimality among nonlinear source-changing realizations.

The Mellin moment of this actual first shell is

$$
\boxed{r(n)=\sum_{j=0}^7\frac{c_j}{8(n-1)+j+1}
=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.}
$$

This is the immutable original BBP forcing, NOT a substitute. The zero-selected recurrence $U_0=0$, $U_n=16U_{n-1}+r(n)$ is recovered. For each finite N,

$$
\sum_{m=0}^{8N-1}\frac{c_m}{m+1}
=\sum_{n=1}^N16^{1-n}r(n).
$$

The infinite limit π uses the pre-existing original BBP identity.

## 4. A proved, source-specific rank-two cancellation

Separate the exact even/odd source shell into

$$
c^+=(4,2,0,-1,-1,-1/2,0,1/4),\quad
c^-=(0,-2,0,-1,0,-1/2,0,-1/4).
$$

Their signed masses and combined first moment are

$$
\sum_jc_j^+=15/4,\quad \sum_jc_j^-=-15/4,\quad
\sum_j j(c_j^++c_j^-)=-15.
$$

Let $r_\pm(n)=\sum_{j=0}^7c_j^\pm/[8(n-1)+j+1]$. Expanding each **finite, exact** rational sum in $1/n$ gives

$$
r_+(n)=\frac{15}{32n}+\frac{1}{2n^2}+O(n^{-3}),
\quad r_-(n)=-\frac{15}{32n}-\frac{17}{64n^2}+O(n^{-3}).
$$

Consequently

$$
\boxed{r_+(n)+r_-(n)=r(n)=\frac{15}{64n^2}+O(n^{-3}).}
$$

Each individual ordinary sum $\sum_nr_\pm(n)$ has a **logarithmic divergence**. The paired original forcing is absolutely summable. This is genuine signed arithmetic cancellation, not a stochastic model.

The two source-resolvent channels are

$$
F_+(t)=\frac{4(1-t/2)}{1-t+t^2/2},\qquad
F_-(t)=-\frac{2t}{1-t^2/2}.
$$

Their exact integrals satisfy

$$
\boxed{\int_0^1F_+(t)\,dt=\pi+2\log2,\qquad
\int_0^1F_-(t)\,dt=-2\log2.}
$$

This is a concrete version of the earlier SUCC source-labelled zero/cancellation and PR #308's established angular/radial geometry. Academic priority is unverified.

## 5. Two real independent recurrences, one authentically selected state

Define separate zero-seeded rational recurrences on the two chiral source histories:

$$
U_\pm(0)=0,\qquad U_\pm(n)=16U_\pm(n-1)+r_\pm(n).
$$

Then **for all finite positive integer n**,

$$
\boxed{U_n=U_+(n)+U_-(n),\qquad
e(hU_n)=e(hU_+(n))\,e(hU_-(n)),}
$$

where $e(x)=\exp(2\pi ix)$ and $h\in\mathbb Z$. The character product is exact **but the factors are strongly source-correlated**, not independent random draws.

The real future Green tails have asymptotic behavior

$$
T_+(n)=\frac{1}{32n}+O(n^{-2}),\quad
T_-(n)=-\frac{1}{32n}+O(n^{-2}),\quad
T_++T_-=\frac{1}{64n^2}+O(n^{-3}).
$$

Thus each lane's absolute total future-tail mass **diverges**, while the *paired* tail is summable. This explains mathematically why the O(1) Green Fourier-transport budget inherited from #323 works for the paired source but **cannot simply be applied to two unrelated independently completed sources**. The correlation is a necessity, not a free assumption.

## 6. Categorical zoom-out, correlation and false joint-state detection

The **entire typed tuple**

$$
E=(K^2,\cdot,J,L_+,L_-,\mathcal T,b,\ell,\text{source version})
$$

is one object in the category of source-labelled arithmetic carrier diagrams. A global **underlying state point** is $1\to|E|$ with both actual coordinates. The lawful complete history is the equivariant orbit map $(\mathbb N,+1)\to(E,\mathcal T)$, NOT generally an equivariant morphism from a terminal one-point dynamical system. The commuting gain square, J-intertwining square and four-step source holonomy are literal map equalities. Local receiver charts must have matching source version and overlap evidence; separate marginals are not sufficient to invent a joint point.

Calibrated common-source statistical **control** (not a physical or π probability model): B uniform on {0,1}; X,Y independent conditional on B, with success chance 1/4 if B=0 and 3/4 if B=1. The joint law is $P(00)=P(11)=5/16$, $P(01)=P(10)=3/16$ and covariance **1/16**, with all four joint states permitted. The fully diagonal law $P(00)=P(11)=1/2$ forbids independent one-sided flips: exactly #61's no-ghost problem. The two-tower operations require genuine full-carrier support; covariance cannot be assumed from equal marginal labels alone.

## 7. Absolute obstruction: contracting taps do not prove π normality

The impulse coefficients obey $\sum_m|c_m|=(16/15)\sum_{j<8}|c_j|=128/15$. Therefore for every nonzero fixed h and every N,

$$
\boxed{\left|\sum_{m<N}e(hc_m)-N\right|\le \frac{256\pi|h|}{15},\qquad
\frac1N\sum_{m<N}e(hc_m)\longrightarrow1.}
$$

So the linear rank-two source taps are *maximally nonuniform phases* on their own. Substituting them for the expanding selected $U_n$ orbit is **refuted**. The actual missing theorem is still

$$
\boxed{\sum_{n=1}^Ne\big(h(U_+(n)+U_-(n))\big)=o(N)
\qquad\forall h\in\mathbb Z\setminus\{0\}.}
$$

A plausible but **UNPROVED** rank-two approach must supply a genuinely source-specific signed *cross-character* decorrelation statement that rejects #320's zero-seeded real-nonnormal source, changed-seed control, and #327/#328's finite-type normal carriers defeating overstrong moving conditional energies. Commuting multiplication and source cancellation are not enough. A bilinear covariance estimate plus a vanishing marginal is a sufficient algebraic criterion, but neither premise is proved. Alternative direct signed methods must retain full source provenance and phase carry.

## 8. Validation, new tests and scope

The exact stdlib Fraction/Gaussian implementation and **17/17 focused local tests** check: all 128 full-source coefficients, exact four/eight clock across unrelated carrier points, the ring involution and grading, rational Hankel determinant 4, even/odd signed cancellation, 47 full original zero-seeded rational BBP states, 64 paired phase congruences, actual full-eight-shell Mellin prefix identities, valid source labels, a full-support correlated common-bit control, invalid diagonal independent-action control, and wrong chirality/source mutations. A standalone exact source receipt is generated/replayed. The first local test run had a keyword-only-call error; corrected and rerun 17/17. Exact tested code Git blob identities and focused logs are recorded separately. **Full native SUCC, hosted CI, Lean and external publication are separate authority; no successes are preclaimed.**

Related primary mathematical caution: [Lagarias 2001](https://arxiv.org/abs/math/0101055) shows perturbed radix shadowing alone is too generic to force normality; [category-theoretic conditional independence](https://doi.org/10.1016/j.entcs.2018.03.028) specifies the independent products that must actually exist.
