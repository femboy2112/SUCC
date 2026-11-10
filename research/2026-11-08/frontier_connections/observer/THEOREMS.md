# Equal-weight moment memory and the two-replica disk observer

Status: **PROVED PAPER**, under the stated finite hypotheses. Newton–Prony
reconstruction and Chebyshev identities are classical. Their application to
the authenticated folded BBP source, the odd-denominator removal of an exact
alias, and the explicit chronology error below are this dossier's derived
connections. No worldwide novelty or Lean certification is claimed.

The source remains

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    U_0=0, U_n=16 U_(n-1)+r(n).

Take a clean source prime p=1 mod8, m=ord_p(16), L=(p-1)/4, q=L/m,
n0=L+1. The actual folded law is the equal-weight law of
z_(r,j)=e(h[U_(n0+r+jm)-x_r/p]), where x_r is the authenticated p-principal
residue, 0<=r<m, 0<=j<q. Here h is an integer and e(t)=exp(2 pi i t).
Weights are empirical replicas of ONE original history, not a seed ensemble.
The clean principal-part law and source provenance are inherited from PE/PR
and [CBM1](../../complement_budget/model/THEOREMS.md).

## OMC1. Known equal replica weights give finite moment closure

For any q>=1 and unit complex z_1,...,z_q, put M_k=q^-1 sum z_j^k.
The q complex readings M_1,...,M_q determine the complete unordered multiset
with multiplicities and hence every positive and negative moment.

Proof. Put P_k=q M_k and e_0=1. Newton's recursion

    k e_k = sum_(i=1)^k (-1)^(i-1) e_(k-i) P_i,   1<=k<=q,

computes all coefficients of the monic polynomial
Q(Z)=Z^q-e_1 Z^(q-1)+...+(-1)^q e_q. Its roots, with multiplicity, are exactly
the multiset. For k>q each root satisfies Q(z)=0, so

    M_k = sum_(i=1)^q (-1)^(i-1)e_i M_(k-i).

Negative moments are conjugates. This is an exact algebraic codec; its
conditioning is a separate question. No new category class is needed:
the codec is a report map on the existing authenticated-history carrier.

Uniformly on all equal-weight q-atom circle laws, the consecutive prefix
M_1,...,M_(q-1) does NOT suffice: the laws supported on all qth roots of
eta have these moments zero and M_q=eta, for arbitrary unit eta. This is a
prefix lower bound, not a statement about every possible adaptive probe menu.
The known equal weights matter; arbitrary unknown weights require different
moment assumptions. A finite q here does not imply a uniform q as p varies.

### An even-replica half-moment chart

The authentic split-prime clock has even q (HCB1). Write q=2d. If the middle
elementary symmetric coefficient e_d is nonzero, the first d moments already
determine the complete law. Compute e_1,...,e_d from Newton's recursion using
P_k=q M_k. Unit roots satisfy

    e_(q-k)=e_q conjugate(e_k),

because complementing a k-element subset multiplies its conjugate product
by the full product e_q. In particular e_q=e_d/conjugate(e_d). This recovers
all remaining coefficients and hence all moments. It is a conditional chart
on the space of equal-weight laws, not a uniformly valid global codec.
The odd-denominator condition alone does NOT guarantee e_d!=0 for q>2:
the four angles 0,0,1/3,2/3 give polynomial Z^4-Z^3-Z+1, whose e_2 is zero.
The q-moment codec remains valid on that exceptional set. This reduction uses
the classical reciprocal-coefficient symmetry of polynomials with unit roots.

## OMC2. For two replicas, one nonzero mean determines the law

Let mu=(delta_z+delta_w)/2, |z|=|w|=1, and s=(z+w)/2.
If s!=0, then

    z*w = s/conj(s),
    {z,w} = roots of Z^2-2sZ+s/conj(s),
    M_k = (s/|s|)^k T_k(|s|),

where T_k(cos theta)=cos(k theta). In particular the unforced sixteenth
moment is the explicitly defined disk map

    F(s)=(s/|s|)^16 T_16(|s|),       0<|s|<=1.              (1)

Proof. Since conj(z)+conj(w)=(z+w)/(zw), division gives zw=s/conj(s).
Write s=a c with |a|=1 and 0<c<=1. The two roots are
a(c +/- i sqrt(1-c^2)), proving the Chebyshev formula. The formulas allow
coincident atoms. At s=0 the law can be ANY antipodal pair, and M_16 is an
arbitrary unit number. One additional moment M_2 determines its product,
because zw=2s^2-M_2, and removes that alias.

This does not contradict CBM2's counterexample to M_16=M_1^16. The correct
two-replica closure is (1), not the sixteenth power of the mean. For larger
or unknown replica families there is no such first-moment assertion.

### Original-zero arithmetic removes the exact singular point

The canonical unchanged forcing is

    r(n)=(120n^2-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)].

Its denominator is odd. Induction in the unwrapped recurrence proves that
every U_n(0) has odd reduced denominator. Subtracting x_r/p preserves this
property. Therefore for every integer h the difference of the two folded
angles has odd reduced denominator, and can never equal 1/2 modulo one.
Consequently **every actual q=2 folded mean is nonzero**, and its exact
complex value determines the entire two-replica law of e(h t) by (1).
At h=1 this is the original complementary circle law; at |h|>1 it is its
hth-power pushforward, and an unrecorded hth-root alias is not recovered.
One exact complex value is an ideal mathematical report, not a claim that
a fixed finite number of bits encodes arbitrary real phases.

More quantitatively, if d is the odd reduced denominator of h(t_2-t_1),

    |B_r(h)| >= sin(pi/(2d)) >= 1/d.                       (2)

Indeed distance from an odd-denominator rational to 1/2 mod1 is at least
1/(2d), and |(1+e(v))/2|=sin(pi dist(v,1/2)). The final inequality is the
chord lower bound for sine on [0,pi/2]. This may be an extremely small bound;
no polynomial precision estimate or uniform separation from zero follows.
The argument also applies to same-forcing odd-denominator rational seeds.
It distinguishes an arithmetic domain, not the selected seed's typicality.

## OMC3. Exact sufficiency does not give uniformly stable decoding

For s,t in the closed unit disk with |s|,|t|>=epsilon>0,

    |F(s)-F(t)| <= (256+32/epsilon)|s-t|.                  (3)

Proof. |T_16'|<=256 on [-1,1], since T_16'=16 U_15 and
|U_15(cos theta)|=|sin(16 theta)/sin theta|<=16. Thus the radial part costs
256||s|-|t||. Normalizing to unit direction costs at most
2|s-t|/epsilon; taking the sixteenth power costs another factor16. Since
|T_16|<=1, triangle inequality gives (3).

There is no continuous extension at zero and no uniform Lipschitz constant
on the punctured disk. For a fixed unit a with a^16!=1, compare s=epsilon
and t=a epsilon. Their input difference tends to zero, but their output
difference tends to |1-a^16| because T_16(0)=1. The implementation checks
this with the exact rational unit a=(3+4i)/5 and rational epsilon. Valid
circle pairs exist for each input even when their coordinates are irrational.

Retaining (M_1,M_2) instead uses the division-free recurrence with product
p=2M_1^2-M_2. It avoids this particular division singularity; it does not
remove long-time expansion or give a precision-independent future predictor.

## OMC4. One chronology bit and an exact minimax prediction error

Knowing the unordered two-atom law does not say which atom belongs to which
source time. Let its next labelled phases be

    z' = z^16 e(h f),       w' = w^16 e(h g),

where f,g are the known two forcing values. If the assignment is unrecorded,
the possible next means are

    y_+ = (z^16 e(hf)+w^16 e(hg))/2,
    y_- = (w^16 e(hf)+z^16 e(hg))/2.

Assume the DECLARED observation fiber contains both labelled assignments
and supplies no further source information that selects one. Among all
complex predictions based only on that fiber, the exact
worst-case error is |y_+-y_-|/2. It is attained by their midpoint

    C = e(h(f+g)/2) M_16 cos(pi h(f-g)),

and equals

    R = (|z^16-w^16|/2) |sin(pi h(f-g))|
      <= pi |h| |f-g|.                                  (4)

Proof. Two disks centered at y_+,y_- with radius below half their separation
cannot intersect, while their midpoint attains half the separation. The
formulas follow by factoring e(hf)+/-e(hg). If y_+!=y_-, one bit selecting
the assignment is necessary and sufficient for exact next-mean prediction.
If y_+=y_-, no bit is needed for THAT target. This is an exact finite instance
of LY2 target-sufficient memory, not a claim of physical nonlocality.

This lower bound is toolkit/fiber-relative. The literal deterministic zero
source with known times, full forcing and unlimited exact replay has a
singleton history; its labels can be recomputed and no extra information bit
is mathematically necessary. Both swapped assignments need not be admissible
original-zero histories. Computational working memory or restricted access
must be declared before applying a memory lower bound to that source.

For the genuine q=2 fold, use n=n0+r, f=r(n+1), g=r(n+m+1),
0<=r<m-1. All these steps are inside the clean interval. Then the actual
next B_(r+1) is one of y_+,y_-, and (4) is a source-authenticated error bound.
The upper error remains valid even if source replay already selects the
actual assignment; the two-assignment minimax LOWER bound then need not apply.
No cyclic boundary transition and no next pole birth is silently included.
An exact next-time mean alone need not recover the original branch label
when the target is degenerate.

## OMC5. The original four poles bound the cost of forgetting chronology

For every n>=1 and m>=1,

    0<r(n)-r(n+m)
      <= 240m/[(8n-7)(8n-6)(8n-5)].                     (5)

Proof. Integrating the original four poles term by term gives

    r(n)=integral_0^1 x^(8n-8) (1-x) Q(x) dx,
    Q(x)=x^4+2x^3+4x^2+4x+4,       0<Q(x)<=15.

Thus the difference adds a factor 1-x^(8m), bounded by 8m(1-x).
Finally integral_0^1 x^(8n-8)(1-x)^2 dx
=2/[(8n-7)(8n-6)(8n-5)]. Strict positivity follows on (0,1).
Combining (4) and (5), at every internal two-replica source step,

    R_r <= 240 pi |h| m/[(8n+1)(8n+2)(8n+3)].            (6)

For fixed h and q=2, this is O_h(L^-2). The smaller exact R_r includes the
factor |z^16-w^16|/2 and can vanish. This is a controlled observation error,
not cancellation of the retained signed statistic.

## Boundary: a closed observer can retain nonzero signal forever

The map (1) is the multiplication-by16 dynamics on unordered circle pairs,
expressed by their barycenter, away from the antipodal singularity. This is
a concrete connection between circle geometry, finite moment memory and
arithmetic transport. It is not an ergodicity theorem.

For example the law with atoms e(4/17),e(-4/17) is invariant under z->z^16,
because 16=-1 mod17 swaps the atoms. Its mean
cos(8pi/17)=sin(pi/34)>0 is a fixed point of F. It has odd-denominator
angles, exact finite memory closure, and a nonzero constant first moment.
The one-atom coherent inverse graph is another surviving control. The
authentic source forcing is never replaced by this unforced model in a
source claim; the example refutes inferring cancellation from the observer
structure alone.

The remaining original-zero obligation is still an all-epoch signed bound
on mean_r e(h x_r/p) B_r(h), or the equivalent selected covariance. OMC2
reduces the exact state needed to represent a q=2 fold; OMC4–5 quantify the
chronology information lost by that reduction. Neither bounds that signed
mean. General-q clocks and their moment memory remain necessary in the
all-epoch route. Pi base-16 normality: **OPEN**. RH: **OPEN**.
