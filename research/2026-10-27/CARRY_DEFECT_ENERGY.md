# All-center carry defects and the finite signed Green energy

**PAPER-PROVED finite instruments; exact rational implementation.** This
round charges all nonmodal lifted integer branches, without first assuming
an extremely small Fourier loss. It does not prove a growth estimate for
those branches on the original BBP orbit. The complete Green minimization
is explicitly identified with circular quadratic variance; it is not an
independent arithmetic saving. A quantitative ceiling below shows why this
quadratic instrument alone cannot prove normality.

The original source remains

$$r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_{n+1}=16U_n+r(n+1).$$

The generic finite lemmas also permit other real seeds and forcing. The
implementation authenticates the original zero seed separately; it never
promotes recurrence compatibility into source authentication.

## 1. A count bound for every integer-branch defect

Let $T\ge1$, $X_{i+1}=16X_i+r_{i+1}$ for $0\le i<T$, and let
$h\ne0$ be an integer. Write

$$D=(T+1)-\left|\sum_{i=0}^T e(hX_i)\right|,
\qquad R=|h|(\max_jr_j-\min_jr_j)<1.$$

Choose a resultant direction $e(\theta)$; when the resultant vanishes,
choose any unit direction. Choose centered lifts

$$q_i=hX_i+\ell_i-\theta\in[-1/2,1/2],\qquad \ell_i\in\mathbb Z.$$

Set $Q=\sum_iq_i^2$, $a_i=q_{i+1}-16q_i$, and

$$k_i=a_i-hr_{i+1}-15\theta=\ell_{i+1}-16\ell_i\in\mathbb Z.$$

Let $M$ be the largest multiplicity of an integer in the list
$(k_0,\ldots,k_{T-1})$, let $K=T-M$, and let
$C=\operatorname{card}\lbrace (i,j):0\le i<j<T,\ k_i\ne k_j\rbrace $. Then

$$
\boxed{D\ge\frac{8(1-R)^2}{289T}C
\ge\frac{4(1-R)^2}{289}K.}
\tag{CD-1}
$$

This requires no hypothesis such as $D\le1/14$ and does not discard
negative or positive branch signs. It is a deterministic finite estimate,
not a stochastic model for carries.

**Proof.** The resultant identity and circle chord inequality give
$D=\sum_i(1-\cos(2\pi q_i))\ge8Q$. The exact signed endpoint identity is

$$
289Q-17q_0^2-272q_T^2-\sum_{i<T}a_i^2
=16\sum_{i<T}(q_{i+1}+q_i)^2\ge0.
\tag{CD-2}
$$

In particular $\sum a_i^2\le289Q$. Notice the **sum** inside the
last square: importing the adjacent-difference remainder from the
unsigned distance comparison would be a sign error.

If $k_i\ne k_j$, integrality and the forcing range imply
$|a_i-a_j|\ge1-R$. The elementary pairwise variance identity therefore gives

$$
(1-R)^2C\le\sum_{i<j}(a_i-a_j)^2
=T\sum_i(a_i-\bar a)^2\le289TQ.
$$

This proves the first inequality in (CD-1). If $n_b=\operatorname{card}\lbrace i:k_i=b\rbrace $,
then $\sum_bn_b=T$, $n_b\le M$, and

$$2C=T^2-\sum_bn_b^2\ge T^2-MT=TK.$$

This proves the second inequality. QED. The same statement with
$(1-R)_+^2$ is trivially valid for $R\ge1$.

The factor 289 comes from the inherited forcing norm comparison, credited
in [the preceding source-curvature dossier](GLOBAL_SOURCE_CURVATURE.md).
The modal counting application and all-center finite certificate are the
scope of this extension. No academic priority claim is made.

## 2. The optimal signed inverse and the boundary that survives

Let $A:\mathbb R^{T+1}\to\mathbb R^T$ be defined by

$$ (Aq)_i=q_{i+1}-16q_i. $$

Its matrix $B=AA^\top$ is tridiagonal with
diagonal 257 and both neighboring diagonals $-16$. For $0\le i\le j<T$,
its inverse is the rational matrix

$$
\boxed{G_{ij}=
\frac{16^{j-i}(16^{2(i+1)}-1)(16^{2(T-j)}-1)}
{255(16^{2(T+1)}-1)},\qquad G_{ji}=G_{ij}.}
\tag{CD-3}
$$

Both finite boundary corrections remain in this expression. One direct
proof uses the principal determinants
$d_s=(16^{2(s+1)}-1)/255$, including $d_0=1$.
For $s\ge2$ they obey $d_s=257d_{s-1}-256d_{s-2}$, with $d_1=257$.
Cofactor expansion gives
$G_{ij}=16^{j-i}d_i d_{T-1-j}/d_T$ for $i\le j$, yielding (CD-3).
Equivalently, multiplication by the tridiagonal matrix verifies the
interior recurrence and both endpoint rows directly. The full row rank
of $A$ also proves that $B$ is positive definite.

Put $v_i=16^i$ for $0\le i\le T$. For every real vector $q$, with $a=Aq$,

$$
\boxed{\lVert q\rVert _2^2=a^\top Ga+
\frac{\langle q,v\rangle^2}{\langle v,v\rangle}.}
\tag{CD-4}
$$

Indeed $A^\top Ga$ has the same image under $A$ as $q$, and is orthogonal
to $\ker A=\mathbb Rv$. Thus the two displayed terms are the orthogonal
components of $q$. In particular $a^\top Ga$ is the exact minimum
of $\lVert q\rVert _2^2$ among solutions of $Aq=a$.

The homogeneous term cannot be deleted when an equality, or the actual
phase energy, is needed. For $q_i=16^{i-T}/10$, $Aq=0$ while $Q>0$;
all energy lies in this term. This is an admissible unforced finite orbit.
It imposes no unauthorized zero future boundary. Conversely, replacing
the signed cross terms by absolute values overestimates the minimum:
for $T=2$, the energies of $a=(1,1)$ and $a=(1,-1)$ differ by
$4G_{01}>0$. The signs carry actual information.

## 3. Eliminate the unknown resultant center by exact rational cuts

Suppose now the given states and forcing are rational. Put
$s_i=\lbrace hX_i\rbrace \in[0,1)$ and retain the literal frequency carries

$$c_i=16s_i+hr_{i+1}-s_{i+1}\in\mathbb Z.$$

The centered lift changes only at the cyclic cutpoints
$\theta=s_i+1/2\pmod1$. Enumerate the distinct cuts in increasing order
and lift one full circle to an interval $[c,c+1]$. There are at most
$T+1$ positive-length intervals $J$. For the rational midpoint $\mu_J$,
set

$$j_i=\left\lfloor s_i-\mu_J+\frac12\right\rfloor,
\qquad b_i=s_i-j_i,
\qquad k_i=-c_i-j_{i+1}+16j_i.$$

For every interior center $\theta\in J$, the centered offsets are
$q_i=b_i-\theta$, and exactly

$$Aq=k+hr+15\theta\mathbf1.$$

The pattern also gives a lawful centered lift on both endpoints of the
closed interval. Adjacent intervals retain both choices at a half-circle
tie, so no observation at a cut is dropped. Crossing a single cut for
state $i$ increases $b_i$ by one. It changes the incoming integer branch
by $+1$ and the outgoing branch by $-16$, when those branches exist.
Coincident cuts apply all their state updates together.

Let $K_J,C_J$ be the counts of Section 1 for this pattern. An actual
resultant center belongs to at least one closed interval, so (CD-1) gives
the center-free, exactly computable statements

$$
\boxed{D\ge\frac{8(1-R)^2}{289T}\min_J C_J,
\qquad D\ge\frac{4(1-R)^2}{289}\min_J K_J.}
\tag{CD-5}
$$

No complex resultant is computed or guessed to select the favorable
carry histogram. The minimum is over every possible center, and the
integer list is reconstructed from the original forcing and ordered
states. The two minima may occur in different intervals; no joint
minimizer is presumed.

The complete Green formula on a cut is

$$
E_J(\theta)=
(k+hr+15\theta\mathbf1)^\top G(k+hr+15\theta\mathbf1)
+\frac{(\langle b,v\rangle-\theta\langle\mathbf1,v\rangle)^2}
{\langle v,v\rangle}
=\sum_{i=0}^T(b_i-\theta)^2.
\tag{CD-6}
$$

Its constrained minimum occurs at the rational center obtained by
clamping $(\sum_i b_i)/(T+1)$ to the closed interval $J$. Consequently

$$D\ge8\min_J\min_{\theta\in J}E_J(\theta)
=8\min_{\theta\in\mathbb R/\mathbb Z}
\sum_{i=0}^T\lVert s_i-\theta\rVert _{\mathbb R/\mathbb Z}^2.
\tag{CD-7}$$

Equation (CD-6) retains the signed source/branch cross terms and the
homogeneous boundary. Its final equality is also a warning: this full
finite optimization is circular quadratic variance in exact source
coordinates. Presenting it as a new source-specific decay estimate would
be incorrect. The independently missing statement in (CD-5) is an
arithmetic lower bound for the selected all-center counts, not their
definition or exact computation on a finite prefix.

## 4. A ceiling and adversarial controls

For any $L=T+1$ circle points, averaging their squared distances over the
center gives $L\int_{-1/2}^{1/2}x^2\,dx=L/12$. Thus

$$8\min_\theta\sum_i\lVert s_i-\theta\rVert ^2\le\frac{2L}{3}.$$

This particular quadratic lower bound can never certify loss
$L-o(L)$. Equispaced phases make the issue explicit: their Fourier sum
is zero but their minimum squared distance is
$(L^2-1)/(12L)$, so (CD-7) certifies only
$\frac23(L-1/L)$. The modal and pair bounds are even smaller, at most
$4T/289$ when $R\ge0$. This is a limitation of the displayed inequalities,
not a theorem forbidding other signed estimates from using branch data.

The controls retain their precise failed assumptions:

- Zero forcing at seed zero has a constant branch on a suitable cut;
  every bound is zero, as required by maximal Fourier reinforcement.
- The rational unforced period-two orbit with seed $1/255$ has positive
  first-mode branch dispersion, but mode 255 is constant and has zero
  bound. One mode of dispersion cannot establish equidistribution.
- A changed rational initial state preserves every forcing transition
  and is admitted by the generic lemmas, but fails zero-source authentication.
- A changed pole with an unrepaired trajectory fails the recurrence;
  repairing the trajectory restores the generic lemma, not its BBP passport.
- The outgoing homogeneous example and opposite-sign Green example above
  falsify deleted-boundary and unsigned-cross-term shortcuts.
- The same-forcing Green selector $V_n=-T_n$ has eventual constant
  branches in a small centered arc and is consistent with the bound;
  it is not the original zero-selected orbit.

Sparse nonnormal selectors and averaged prime carriers are not excluded
by this finite energy theorem. No lower bound on their selected all-center
counts is assumed. Odd conductors or exact carry reconstruction alone do
not supply such a lower bound for the authentic source either.

## 5. Exact instruments and finite formal scope

`observational_succ/carry_defect_energy.py` uses integers and `Fraction`.
It checks ordered forcing and full rational states before producing literal
frequency carries, all cyclic cut intervals, and both Green components. Its finite
budget is 128 transitions and source replay through index 2000.
`tests/test_carry_defect_energy.py` passed **11 tests in 0.057 seconds**.
Independent checks include rational Gauss--Jordan inversion, an alternative
center-minimum enumeration, literal four-pole source holdouts, native
outward Fourier intervals, and the intentional mutations above.

An initial scratch check copied the unsigned adjacent-difference remainder
into (CD-2); six exact vector holdouts rejected it. The correct signed
adjacent-sum identity passed all six and is retained as an explicit
negative test. No failed equality was promoted to a theorem.

The new finite Lean file is `formal/CarryDefect.lean`; its scoped checker
is `scripts/check_carry_defect_lean.py`. The four declarations cover the
signed endpoint identity, histogram pair budget, the scalar modal-loss
implication with its separation/chord hypotheses explicit, and the scalar
periodic-terminal identity used by the parallel template argument.
They do not formalize the circle lifts, Green inverse, cut enumeration,
BBP count growth, cosine/chord theorem, irrationality measure, or limits.
The completed run is **KERNEL_CHECKED: four declarations and four paired
positive/false controls**, using pinned Lean 4.14.0 and mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`, serially with a 2048 MB
compiler cap. Every source hash and exported theorem-type hash was
rechecked afterward. Only `propext`, `Classical.choice`, and `Quot.sound`
occur. The actual receipt is
[`carry_defect_validation/lean/kernel-observation.json`](carry_defect_validation/lean/kernel-observation.json).

```sh
python scripts/check_carry_defect_lean.py \
  --dependency-project /home/leah/SUCC-rf/formal/mathlib_bridge \
  --output research/2026-10-27/carry_defect_validation/lean
```

The next useful source theorem would bound $\min_J K_J$ or the retained
signed residual energy on all sufficiently large authentic windows.
A positive density would supply a genuine relative loss through (CD-5),
while superlogarithmic growth would improve the prior absolute-loss order.
Neither follows from this finite calculus, and neither is claimed here.
Even those improvements would remain weaker than the full fixed-mode
cancellation required for π normality.
