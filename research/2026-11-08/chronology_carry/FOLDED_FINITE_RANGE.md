# A finite-range obstruction for two-replica approximation

Status: **PROVED PAPER**, elementary finite inequality and explicitly conditional
asymptotic corollary. This does not prove normality, disprove normality, or assert
infinitely many selected two-replica clocks. It identifies an unnecessary
approximation demand that can conflict with the intended normality conclusion.

Write e(t)=exp(2 pi i t). This theorem concerns the *full* coherently transported
fold F=aB, rather than the complement B in a moving local-prime frame. Every
norm comparison uses the same frame. It applies directly to the frozen carry
predictors in [CCM1](model/THEOREMS.md).

## FR1. Quantitative finite inequality

Let m>=1, and z_r,w_r be unit complex numbers, 0<=r<m. Set

    F_r=(z_r+w_r)/2,
    e_r=|F_(r+1) - (z_r^16+w_r^16)/2|,  0<=r<m-1.

Let Delta be the discrepancy of the first marginal z_r over all connected arcs
of the circle, against normalized arc length. Let D be any nonempty set of at
most M points in the closed unit disk, M>=1, and

    rho_D=(1/m) sum_r dist(F_r,D),   delta=1/(2048 M^2).

Then

\[
\rho_D\ge {1\over2048M^2}
\left({1\over4}-{1\over2m}-{16\over15m}\sum_{r<m-1}e_r-2M\Delta\right).
\tag{FR1}
\]

A negative right side is harmless. The same lower bound applies to the error
of any assigned predictions t_r in D, since |F_r-t_r|>=dist(F_r,D). D may be
selected after seeing every source value: the bound is uniform over D.

**Proof.** Put a=1/32. Since 16 is even, factorization of powers gives

    |w^16-z^16|=|w^16-(-z)^16|<=16|w+z|,
    |(z^16+w^16)/2|>=1-16|(z+w)/2|.

Therefore an edge with e_r<=1-17a=15/32 cannot have both |F_r|<a and
|F_(r+1)|<a. At most (32/15)sum e_r edges violate that error threshold. Each
vertex meets at most two edges, so the proportion of vertices with |F_r|>=a
is at least

    (m-1)/(2m) - (16/(15m))sum e_r.                    (1)

Apart from at most m*rho_D/delta vertices, dist(F_r,D)<=delta. At a remaining
vertex with |F_r|>=a choose d in D with |F_r-d|<=delta. Then |d|>=a-delta>=a/2.
Because |w_r|=1,

    ||2d-z_r|-1|<=2delta,
    |Re(z_r conjugate(d))-|d|^2|<=delta(1+delta).

Consequently z_r lies in the cosine band

    |cos(arg(z_r)-arg(d))-|d|| <= 4delta/a.             (2)

For 0<epsilon<1 a band |cos(theta)-t|<=epsilon consists of at most two arcs
with total normalized length at most sqrt(epsilon). To prove the bound,
intersect with [0,pi], obtaining [u,v]. Since

    cos u-cos v
      =2sin((u+v)/2)sin((v-u)/2)
      >=2sin^2((v-u)/2)>=2((v-u)/pi)^2,

its width is at most pi*sqrt(epsilon); reflection accounts for the other
half-circle. Empty bands and point bands satisfy the same bound. Open/closed
endpoints can be handled by slightly enlarging arcs and taking a limit.

Thus (2) contains at most a fraction 2sqrt(delta/a)+2Delta of the observed
z_r. Taking the union over D bounds its fraction by
2M sqrt(delta/a)+2M Delta=1/4+2M Delta. Subtract this from (1), and charge
the discarded vertices by rho_D/delta. Rearranging proves FR1. QED.

The first marginal assumption matters. The homogeneous two-cycle
z=e(8/17),w=e(9/17), with the entries swapped at each step, has a constant
nonzero F and hence zero error for a one-point quantizer. Its marginal is not
Haar. Evolution matters too: Haar z with w=-z makes F=0 identically, but its
image under simultaneous sixteenth powers is the diagonal and leaves this law.

## FR2. Application to the original four-pole source

At a q=2 clean clock, L=2m, n0=2m+1, put

    z_r=e(h U_(n0+r)(0)),  w_r=e(h U_(n0+r+m)(0)).

The exact recurrence, including its literal zero seed, implies

    e_r <= pi |h| [r(n0+r+1)+r(n0+r+m+1)].             (3)

Here r is the authentic positive *sum of the four signed poles*; coefficients
or source chronology have not been replaced. The elementary decomposition

    r(n)=6/[d(d+3)]+4/[d(d+4)]+5/[d(d+5)], d=8n-7,

gives 0<r(n)<15/(8n-7)^2. Therefore

    (1/m)sum e_r <= 30 pi |h|/(8n0+1)^2.              (4)

Proof of (3): e(h U_(n+1))=e(h r(n+1))*e(h U_n)^16;
use |e(t)-1|<=2pi|t| on each branch and average. No replacement of a
two-atom law's sixteenth moment by its first moment's sixteenth power occurs.

If pi is base16-normal, the first marginal discrepancy Delta tends to zero
along any such clocks with m->infinity. Indeed Green transport gives
U_n+T_n=16^(n-1)pi with T_n=O(n^-2). Normality gives Haar equidistribution of
the completed orbit; multiplication by a fixed h!=0 preserves Haar. Prefix
subtraction transfers it to the macroscopic interval [2m+1,3m]. Vanishing
circle perturbations preserve arc equidistribution, and a finite grid of arc
endpoints upgrades it to uniform arc discrepancy.

Consequently, **if infinitely many selected q=2 clocks exist and pi is
base16-normal**, then for every fixed M and fixed h!=0,

\[
\liminf_{q=2\text{ clocks},\ m\to\infty}
\inf_{|D|\le M}\ {1\over m}\sum_r\operatorname{dist}(a_rB_r,D)
\ \ge\ {1\over8192M^2}>0.                         \tag{FR2}
\]

Both hypotheses in bold are conditional here. In particular, FR2 cannot be
used as an unconditional estimate on the original-zero orbit.

If a predictor g takes at most K different values, its two-replica fold has
at most M=K(K+1)/2 values. Therefore its CCM1 error rho cannot tend to zero under
the hypotheses of FR2, even if its labels use arbitrary source history and
its K values vary with the epoch. This covers a fixed categorical carry table
and its unseen-value convention. The bound is small but positive; it is an
asymptotic incompatibility, not a claim about this experiment's optimal finite
error. Growing output alphabets, continuous-phase models and unbounded replica
counts are outside this statement. Signed residual decay remains possible.

## FR3. A compactness proof of the qualitative obstruction

For an independent proof architecture, take the compact set of probability
measures on the two-torus invariant under (z,w)->(z^16,w^16), with Haar
marginals. It is nonempty (product Haar). The product with M disk centers is
compact; integrating min_j |(z+w)/2-d_j| is continuous. Its minimum is attained.

That minimum cannot be zero. For any nonzero d, the equation (z+w)/2=d has
at most two possible z, so it has zero mass under a Haar first marginal.
A zero minimum would therefore force w=-z almost surely. Simultaneous even
powers send this antidiagonal to the diagonal, and these two unit-circle
subsets are disjoint. Invariance is impossible. Thus the minimum is positive.

Actual source empirical pair laws have invariant subsequential limits by the
componentwise bounds
`|z_(r+1)-z_r^16|<=2 pi |h| r(n0+r+1)` and
`|w_(r+1)-w_r^16|<=2 pi |h| r(n0+r+m+1)`, together with the one deleted
endpoint. These follow directly from the original recurrence; a bound on the
folded first moment alone would not suffice. Their marginals are Haar under the same
conditional normality hypothesis. This yields the positive qualitative FR2
floor without its explicit constant, triangulating the finite arc proof.

## Contribution and boundary

The equal-weight two-point inverse from the previous observer round supplies
the nonzero finite-fiber geometry. Here it is combined with actual time
transport and marginal discrepancy to constrain *all finite-range folded
predictors*. This is a source application with complete local proofs; worldwide
novelty is not asserted. It is not a new sufficient normality premise.

The useful consequence is to pursue signed residual window energy rather than
demanding fixed-table L1 reconstruction. The former can vanish while the
residual remains large pointwise. The original-zero estimate needed for that
route is still OPEN.
