# Coupled lag Bessel saving and the surviving mixed correlation

**Paper mathematics, not a zero-seed normality proof.** Use exactly the #506
source `U=Y+Z`, with all three original initial states zero. Define

\[
 e(t)=\exp(2\pi i t),\quad
 C_{A,H}^{\ell}(I)=A^{-1}\sum_{n\in I}e(HY_n)e(HZ_{n+\ell}),\quad
 M_{A,H}^{\ell}=\max_{I\subset[A,2A)}|C_{A,H}^{\ell}(I)|.
\]

Intervals have integer endpoints and are contiguous. H is a positive integer,
`Lambda=H/A^2`. A different angular sequence, when used as a countermodel,
is explicitly marked. The same radial Z is retained throughout.

## CF-1. A genuine maximal signed saving across delayed coupled frames

For every integer A>=128, positive integer H with `1<=Lambda<=A/2`, and
integer `0<=L<=floor(A/Lambda)`,

\[
 \boxed{\sum_{\ell=0}^{L}(M_{A,H}^{\ell})^2
 \le1+\frac{1728}{\Lambda}\mathcal H_L,\qquad
 \mathcal H_L=\sum_{d=1}^{L}\frac1d,\quad\mathcal H_0=0.} \tag{CF1}
\]

This applies to the **actual coupled original zero-seed source**. More
generally it holds for every real angular sequence Y, without any independence
assumption. Consequently it is a seed-blind average saving, not a selected
lag-zero estimate.

At the exact mission schedule `log A/16<Lambda_A(h)<=log A`, take
`L=floor((log A)^3)`. For every fixed nonzero h this is allowed eventually,
and

\[
 \min_{0\le\ell\le L}M_{A,H_A(h)}^{\ell}
 \le\sqrt{\frac{1+O(\log\log A/\log A)}{L+1}}
 =O((\log A)^{-3/2})=o((\log A)^{-1}). \tag{CF2}
\]

The minimizing lag can depend on A,h and the source; CF2 supplies **no** such
saving at the prescribed lag zero.

### Source derivative prerequisites, with constants

The authentic radial extension is `z(x)=Z_x` at integer x, with
`z(x)=(1/4)sum_(k>=1)16^-k d(x+k)` and `d=rsharp-2r`. Its seven nonzero
rational taps `(coefficient,offset)` in `c/(8x-offset)` are

`(-8,7),(8,6),(4,5),(8,4),(2,3),(2,2),(-1,1)`.

Their coefficient sum is 15 and their absolute offset sum is 167. Expanding
and differentiating these literal rational functions, then summing the
geometric zeroth/first moments, gives for m=0,1,2,3 and x>=2

\[
 \left|z^{(m)}(x)-\frac{(-1)^m m!}{32x^{m+1}}\right|
 \le C_m x^{-m-2},\quad
 C_m=(m+1)!\left[\frac1{30}+\frac{167}{3840}
                         (16/9)^{m+2}\right]. \tag{CF3}
\]

For completeness, each differentiated pole has leading term
`(-1)^m m!/(8x^(m+1))`. Since `x-offset/8 >=9x/16` for x>=2, the mean
value theorem bounds its difference from this term by
`(m+1)! |c| offset (16/9)^(m+2)/(64x^(m+2))`.
The weighted tail sums `sum16^-k=1/15` and `sum k16^-k=16/225` then give
CF3, including the error from replacing `(x+k)^(-m-1)` by `x^(-m-1)`.
Geometric domination justifies all fixed derivatives.

Exactly `C_2=18413/6561`, `C_3=5708452/295245`, and
`32C_2<128`, `(16/3)C_3<128`. Thus for all real x>=128,

\[
 \frac1{32x^3}\le z''(x)\le\frac1{8x^3},\qquad z'''(x)<0. \tag{CF4}
\]

This rederives the prerequisites of #505 BDE-1 from the raw taps; no presumed
distribution of the radial or angular orbit enters.

### Uniform off-diagonal and maximal intervals

Take `0<=k<ell<=L`, `d=ell-k`, and
`f(x)=H[z(x+ell)-z(x+k)]`. For any consecutive summation interval in
`[A,2A)`, its phase increments are

\[
 \theta_n=f(n+1)-f(n)
   =H\int_n^{n+1}\int_k^\ell z''(u+t)\,dt\,du.
\]

Every argument lies in `[A,2A+L]`, hence in `[A,3A]`, including the final
telescoping endpoint n+1. CF4 proves these increments are positive,
decreasing, and satisfy

\[
 \frac{d\Lambda}{864A}\le\theta_n\le
 \frac{d\Lambda}{8A}\le\frac18. \tag{CF5}
\]

Let `b(theta)=(1-e(theta))^-1=1/2+(i/2)cot(pi theta)`.
Discrete summation by parts in
`e(f(n))=b(theta_n)[e(f(n))-e(f(n+1))]` gives two endpoint terms and the
variation of b. For `0<theta_min<=theta<=1/8`,
`|b|<=1/(4theta_min)` and `Var(b)<=1/(2pi theta_min)`, so their total is
strictly less than `1/theta_min`. This also covers singleton intervals;
empty intervals give zero. Therefore for every such interval I,

\[
 \left|A^{-1}\sum_{n\in I}e(H[Z_{n+\ell}-Z_{n+k}])\right|
 \le\frac{864}{d\Lambda}. \tag{CF6}
\]

On normalized counting measure in `[A,2A)`, let `v(n)=e(HY_n)` and
`b_ell(n)=1_(I_ell)(n)e(-HZ_(n+ell))`, where each I_ell separately maximizes
its coupled mean. Every Gram diagonal is at most one. An off-diagonal is
exactly the CF6 character restricted to `I_ell intersect I_k`; this
intersection is empty or one contiguous interval. No endpoint shifts or
common maximizing interval are assumed. The row sum is at most
`1+1728 H_L/Lambda`. The operator norm bound and dual Bessel, with
`||v||_2=1`, prove CF1.

## CF-2. Common-gauge Gram geometry cannot select lag zero

For the uncut coupled vectors
`v_ell(n)=e(H[Y_n+Z_(n+ell)])`, every Gram entry is exactly

\[
 \langle v_\ell,v_k\rangle
 =A^{-1}\sum_n e(H[Z_{n+\ell}-Z_{n+k}]). \tag{CF7}
\]

It is independent of Y, of its forcing, of its initial seed, and of every
common pointwise unit phase multiplying all columns. The same is true with
any fixed predeclared interval cuts. It does **not** follow that the overlap
of each column with the constant vector is unchanged: those are the selected
signed means that the Gram does not determine.

There is an exact rank obstruction to repairing this by parallel transport.
Multiplying column ell by its **column-dependent** inverse Wilson factor
`e(H[Z_n-Z_(n+ell)])` turns every uncut column into `e(HU_n)`. Its transported
Gram is therefore the all-ones matrix, of rank one and operator norm L+1.
The near-orthogonal raw Gram of CF1 and equality of the transported columns
cannot be used simultaneously: the latter transformation is not one common
unitary operator acting on all columns. Bessel after that transport gives
only `(L+1)|C^0|^2 <= L+1`, the trivial bound. This exactly pays for the
apparent opportunity to average the good delayed frames and then identify
their compensated values with the original one.

For any prescribed lag ell0, the artificial companion
`Y_n^star=-Z_(n+ell0)` gives `M^ell0=1` under exactly this Gram. This changes
the angular forcing and is a counterexample only to a Gram-only selected-lag
claim. A stronger same-forcing control is the fixed coherent seed `s*=-pi/16`
placed in Y, for which `Y_n^*=Y_n+16^n s*` and
`Y_n^*+Z_n=-T_n`. Read-only #505's independently reviewed coherent theorem
gives `Lambda M^0 ->256/pi` at the prescribed depth, while CF1/2 still hold.
The normal same-forcing seeds of #505 CFG-1/2 preserve even qualitative
normality while respectively retaining or diverging in this critical ratio.
Thus normality plus the coupled Gram bound still does not select the rate.

The 1/5 seed is a different type of control: since `16^n/5=1/5 (mod1)`,
it multiplies every coupled character by the same constant `e(H/5)`.
All coupled maximal moduli and all Gram entries are exactly unchanged, for
every integer H and every radial lag. This is an exact failure of source
**identification** by these moduli, not a counterexample to a cancellation
statement that may be true for both seeds. Radial-only Y=0 is yet another
source: its small critical sums cannot authenticate the original forcing.

## CF-3. The mixed van der Corput term can be maximally correlated

This gives a source-compatible, quantified falsifier of the most tempting
direct coupled Weyl estimate. Fix an integer d>=1, use the original radial Z,
and use the same-four-pole coherent counterseed in the angular channel as
above. On `I_d=[A,2A-d)` let E denote the normalized average over its A-d
indices, and define

\[
 a_n=e(H[Y^*_{n+d}-Y^*_n]),\qquad
 b_n=e(H[Z_{n+d}-Z_n]).
\]

At the mission's critical schedule, for each fixed d,

\[
 |E a_n|=\Theta_d(\Lambda^{-1}),\quad
 |E b_n|=\Theta_d(\Lambda^{-1}),\quad
 E(a_nb_n)=1+O_d(\Lambda/A), \tag{CF8}
\]

and hence the complex covariance without conjugation satisfies

\[
 \boxed{E(a_nb_n)-(E a_n)(E b_n)
       =1+O_d(\Lambda^{-2}+\Lambda/A).} \tag{CF9}
\]

**Proof.** The exact source identity `Y^*+Z=-T` gives
`a_nb_n=e(-H[T_(n+d)-T_n])`. The positive source moment implies
`0<T_n-T_(n+1)<1/(32n^3)`, hence

\[
 |E(a_nb_n)-1|\le\frac{\pi d\Lambda}{16A}. \tag{CF10}
\]

Also `a_n=conjugate(b_n)e(-H[T_(n+d)-T_n])`, so
`|Ea-conjugate(Eb)|<=pi d Lambda/(16A)`. The #506 OR-03 sharp radial-lag
formula, or its two direct integrations by parts, gives

\[
 E b_n=\frac8{\pi i d\Lambda}
 \left[8e(-d\Lambda/128)-e(-d\Lambda/32)\right]
 +O_d(\Lambda^{-2}+\Lambda/A+A^{-1}).
\]

Removing d final indices and renormalizing costs O_d(1/A). The two endpoint
magnitudes differ by 7, so the leading modulus is bounded above and below by
positive constants divided by Lambda. At critical Lambda, all errors are
o(1/Lambda). The preceding comparison proves the same for Ea, then CF9.
No probabilistic argument is present: the maximal correlation is a source
identity and a uniform rational-tail bound.

### The attempted original zero-seed saving and its first missing estimate

For original `u_n=e(HU_n)` on an interval of N points, Cauchy differencing
with `1<=D<=N` gives

\[
 |\sum u_n|^2\le\frac{N+D}{D}
  \left[N+2\sum_{d=1}^{D-1}(1-d/D)
   \Re\sum_{n,n+d\in I}e(H\Delta_dY_n)e(H\Delta_dZ_n)\right].
\]

To turn this into a useful critical bound requires a **mixed** signed
correlation estimate. CF8 explicitly falsifies the proposed replacement of
the inner product by its separately small marginal means, even while keeping
every original forcing injection and the same radial source. The literal
zero seed excludes this counterseed, but that exclusion alone is not an
estimate for the original mixed correlation.

We then retained all literal carries. Write `x_n={U_n}` and
`c_(n+1)=floor(16x_n+r(n+1))`. With
`S_d(n)=sum_(j=1)^d16^(d-j)r(n+j)` and
`K_d(n)=sum_(j=1)^d16^(d-j)c_(n+j)`, exact iteration gives

\[
 x_{n+d}=16^d x_n+S_d(n)-K_d(n),\qquad
 e(H\Delta_dU_n)=e(H[(16^d-1)x_n+S_d(n)]). \tag{CF11}
\]

The integer carries vanish from the integer character, but cannot be declared
irrelevant: the full carry word restricts x_n by the simultaneous inequalities
`0<=16^j x_n+S_j(n)-K_j(n)<1`, j=1,...,d. Partitioning the sum by these
literal words is exact. The first unavailable estimate is an upper bound or
signed bound on the **realized zero-seed visits** to these moving carry cells.
Replacing their visit counts by cell lengths assumes the desired distribution;
using their worst-case counts yields only the trivial correlation bound.
Choosing d large enough to resolve H does not provide the missing counts.
Thus this carry-aware attempt reaches a precise source-selected estimate,
not a proof or an impossibility claim for the unique original orbit.

CF1 cannot repair this step: the amplitudes `e(H Delta_dY_n)` depend on d,
so these correlations are not projections of one common vector onto the
radial test family. Treating them as one vector is a distinct invalid inference.

## CF-4. Delayed compensation removes a tail jet, not the unknown signed mean

For any real angular seed s, keep Z unchanged and put

\[
 W_n(s)=U_n(s)-\tfrac12(Z_{n+1}-Z_n),\qquad n\ge1.
\]

The source expansions proved from the rational Mellin/Laplace densities give

\[
 T_n=\frac1{64n^2}-\frac7{512n^3}+O(n^{-4}),\quad
 Z_{n+1}-Z_n=-\frac1{32n^2}+\frac9{128n^3}+O(n^{-4}).
\]

Thus, with `y=s+pi/16`,

\[
 \boxed{W_n(s)=16^ny-\frac{11}{512n^3}+O(n^{-4}).} \tag{CF12}
\]

For fixed nonzero integer h, integer j>=0 with j<=A and
`H=|h|16^j=A^2 Lambda`, the maximal sharp-interval means satisfy

\[
 \boxed{|M_A^{W(s)}(H)-M_A^{U(s)}(h)|
       \le\frac{2j}{A}+O\left(\frac\Lambda A+
                                      \frac{|h|}{A^2}\right).} \tag{CF13}
\]

The constants in the O term come from the original tail and are independent
of s,j. Indeed the W character differs from `e(H16^ny)` by O(H/A^3),
uniformly on the epoch. The latter is `e(|h|16^(n+j)y)`. Shifting an
interval family by j and clipping costs at most 2j/A in their maximal sums.
Finally the completed fixed-h character differs from `e(hU_n(s))` by
O(|h|/A^2); conjugation handles negative h. These comparisons apply in both
directions, proving CF13.

At critical H the error is O_h(log A/A). This is much smaller than the
earlier variation cost, but it compares the unknown compensated high mean
with the **unknown original low mean**. For the coherent seed W tends to
zero so this high mean tends to one. No normality is obtained by eliminating
successive tail jets. Returning from W to U requires the nonconstant
half-radial-lag multiplier and restores its critical variation cost.

## Source/authority boundary

#506 supplies the radial source, OR-03 and the source-jet context. #504 supplies
its exact zero completed period. Read-only #505 supplies the sharper tail
expansion and coherent/normal-seed controls; CF3's derivative prerequisite is
also rederived here from raw taps. No sibling file is edited or silently
adopted as original zero-seed evidence. CF1 and CF9 are actual signed results
with the stated scopes. CF13 is a transport result, explicitly not an advance
in cancellation. Every proof shares BBP provenance and the same model family;
finite exact checks do not establish universal asymptotics.

Original fixed-h Weyl, the original critical maximal ratchet, coarse J=o(K),
and pi base-16 normality remain **OPEN**. RH is **OPEN, separate**.
