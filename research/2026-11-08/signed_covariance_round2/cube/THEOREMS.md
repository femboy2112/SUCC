# Local-source cubes, exact degeneration, and a nonlinear observer certificate

**Status: PROVED PAPER from the declared prime-epoch and BK inputs.**
Finite exact checks are separate. No Lean certificate, external scholarly
priority, or original-zero full Weyl decay is claimed. The original signed
covariance, pi base-16 normality, and RH remain **OPEN**.

## Source and domains

The source is exactly

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`,
`U_0=0`, `U_n=16 U_(n-1)+r(n)`.

Retain its unwrapped rational states and canonical p-principal parts. Import
PE1--9 from `learning_yoneda/arithmetic/PRIME_EPOCH_THEOREM.md` at parent
`1990b05117d84b33094c8e0f53f7d19b60f48060`: for the deterministic selected
prime p=p_A, p=1 mod8, m=ord_p(16)>p^(1/3), p/(4A)->1. Put
L=(p-1)/4, n0=L+1 and I=[n0,n0+L). Then m divides L and the actual original
source satisfies, on I,

`a_n=e(h[U_n]_p)=e(xi*g^(n-n0)/p)`,

where g=16 modp and xi=4h*g^(n0-(p+7)/8) is nonzero for p not dividing h.
All finite theorems below hold for **every** xi in F_p^*, not merely a fixed h.

Write `G=Z/mZ`, `a(r)=e(xi*g^r/p)` and
`S(c)=m^-1 sum_(r in G)e(c*g^r/p)`. The sole analytic finite-field input is
the same Bourgain--Konyagin theorem as PE9:

`sup_(c!=0 modp)|S(c)| <= delta_p=p^(-gamma)`,

for one fixed gamma=gamma_(1/3)>0. No numerical gamma is supplied or fitted.
The exact identities also hold with any separately proved finite upper bound
delta>=max_(c!=0)|S(c)|. They do not require BK to be tested numerically.

All sums in the cube theorems are over the finite **temporal clock G**.
Wrapping an arbitrary physical BBP history modulo m is not asserted lawful.
Only the authenticated local character is m-periodic on the clean epoch.
The full complement is first folded explicitly when used below.

## CQ1. Exact cube reduction to squared subgroup sums

For any complex f on G and integer d>=1 define

`Q_d(f)=E_(r,h_1,...,h_d in G) product_(omega in {0,1}^d)
 C^(|omega|) f(r+omega dot h)`,

where C denotes conjugation. Write `||f||_(U^d)=Q_d(f)^(1/2^d)`, taking the
nonnegative root. The expression Q_d is real and nonnegative by the final
shift identity below. U^1 is a seminorm; only d>=2 is used for dual norms.

Let q=d-1 and

`D_(m,q)=1-(1-1/m)^q`, with D_(m,0)=0.

Then the original local clock has the exact identity

`Q_d(a) = D_(m,q)
 + m^(-q) sum_(h_1,...,h_q in G\{0})
       |S(xi product_(j=1)^q (1-g^(h_j)))|^2`.                 (CQ1)

An empty tuple/product is allowed when d=1, giving Q_1(a)=|S(xi)|^2.
Consequently,

`D_(m,d-1) <= Q_d(a)
 <= D_(m,d-1)+(1-D_(m,d-1))*delta_p^2
 <= (d-1)/m+delta_p^2`.                                    (CQ2)

The middle bound is at most one. This is a **signed identity before the
upper bound**; no local positive energy is being mistaken for negative
interference.

**Proof.** For fixed preceding shifts h'=(h_1,...,h_q), let

`F_(h')(r)=product_(omega in {0,1}^q) C^(|omega|) a(r+omega dot h')`.

Expanding its exponent in F_p gives exactly

`F_(h')(r)=e(xi*g^r product_j(1-g^(h_j))/p)`.

The final pair of cube faces is F_(h')(r) conjugate(F_(h')(r+h_d)). Since
(r,h_d)->(r,r+h_d) is a bijection G^2->G^2, its average is
`|E_r F_(h')(r)|^2`. This also proves Q_d(f)>=0 for any f. A coefficient
vanishes precisely when some h_j=0 in G, because g has **exact** order m
and F_p is a field. There are m^q-(m-1)^q such preceding tuples, each
contributing one. Every other tuple has nonzero coefficient and contributes
the displayed squared subgroup mean. Apply the declared BK bound and the
union bound D_(m,q)<=q/m. QED.

Taking absolute values separately over all d shifts would instead pay
`D_(m,d)+(1-D_(m,d))*delta_p`. Averaging the final shift exactly first saves
one degeneration dimension and squares the analytic error. This improvement
is not a new exponential-sum import.

## CQ2. The exact growing-depth threshold for the local cube instrument

Let A tend to infinity through all integer epochs and d_A>=1 be any sequence
of integers. Then, uniformly over xi in F_(p_A)^*,

`sup_xi ||e(xi*16^r/p_A)||_(U^(d_A)(Z/m_A Z)) -> 0`

**if and only if**

`2^(d_A)=o(log p_A)`.                                      (CQ3)

Moreover the necessity holds for **every** choice of nonzero coefficients
xi_A: if the displayed scale condition fails, the cube norm cannot tend to
zero even on one such coefficient sequence.

**Proof, sufficiency.** Write t_A=2^(d_A). The condition implies
d_A=O(log log p_A). Since m_A>p_A^(1/3), for every fixed
`0<c<min(1/3,2 gamma)`, eventually

`(d_A-1)/m_A+p_A^(-2 gamma) <= p_A^(-c)`.

CQ2 yields the explicit eventual bound
`||a||_(U^(d_A)) <= exp(-c log(p_A)/2^(d_A)) -> 0`.

**Proof, necessity.** If t_A/log p_A does not tend to zero, there are
epsilon>0 and an infinite subsequence with t_A>=epsilon log p_A. Along
that subsequence d_A>=2 eventually. CQ2 gives

`Q_(d_A)(a)>=D_(m_A,d_A-1)>=1/m_A>=1/p_A`,

so `||a||_(U^(d_A))>=exp(-log(p_A)/t_A)>=exp(-1/epsilon)>0`.
This is independent of xi. QED.

Thus the depth threshold previously sufficient for arbitrary polynomial
chirps is an unavoidable threshold for **this cyclic cube instrument**.
It is not proved necessary for arbitrary temporal polynomial correlation
decay, and it places no restriction on the possible true Weyl cancellation.
At and above the threshold, diagonal cube degeneracies alone block a vanishing
U^d certificate. Deleting those cubes does not retain the norm or its usual
Cauchy--Schwarz properties without a new proof.

## CQ3. Bounded nonlinear cube observations

For d>=2 and a family of arbitrary functions
`f_omega:G->C`, `omega in {0,1}^d\{0}`, with |f_omega|<=1, define the
declared observer response

`D_d(f_omega)(r)=E_(h in G^d)
 product_(omega!=0) C^(|omega|) f_omega(r+omega dot h)`.       (CQ4)

The functions can be selected after observing the entire finite history;
the bound below is uniform. This is an offline finite-history measurement,
or a measurement made after the epoch closes. It is not a prediction based
on a strict past filtration. It uses the source's common phase basis.

For every such atom,

`|E_r a(r) D_d(f_omega)(r)| <= ||a||_(U^d)
 <= [D_(m,d-1)+(1-D_(m,d-1))*delta_p^2]^(1/2^d)=:u_(p,d)`.
                                                               (CQ5)

**Classical finite algebra used here.** The Gowers--Cauchy--Schwarz inequality
on **any finite abelian group** is

`|E_(r,h) product_omega C^(|omega|) F_omega(r+omega dot h)|
 <= product_omega ||F_omega||_(U^d)`.

It follows by repeated ordinary Cauchy--Schwarz in cube coordinates. One
standard derivation writes r=sum_i y_i^0 and h_i=y_i^1-y_i^0; the map from
the 2d independent y-coordinates to (r,h) has constant fiber size m^(d-1).
The box Cauchy--Schwarz inequality then applies to
`F_omega(sum_i y_i^(omega_i))`. Its proof doubles one coordinate at a time
by ordinary Cauchy--Schwarz; after all d coordinates the factor for each
vertex is exactly its 2^d-th box moment. The same constant-fiber map
identifies that moment with Q_d(F_omega). This proof requires neither
division by d! nor a prime-order temporal group. In particular it is lawful
when m is even or highly composite. Taking F_0=a and the other F's equal
to the declared bounded functions proves CQ5 because their U^d norms are
at most one. This elementary inequality is classical, not a new SUCC claim.

The atoms include conjugates of cyclic phase polynomials of degree<d:
if a unit phase psi has every d-fold multiplicative derivative one, then
choosing every f_omega=psi gives D_d(f_omega)=conjugate(psi). Arbitrary real
polynomials evaluated on [0,m) need not obey the cyclic wrap law. Therefore
CQ5 does not silently replace the earlier noncyclic polynomial theorem.
It controls a different, nonlinear observer class and gives an exact depth
obstruction unavailable from the old sufficient bound alone.

## CQ4. A complete complement certificate, with its missing premise exposed

Keep the exact full source factorization

`a_n=e(h[U_n]_p)`, `b_n=e(h(U_n-[U_n]_p))`, `a_n b_n=e(hU_n)`.

Let q=L/m and fold only the complement:

`B(r)=q^-1 sum_(j=0)^(q-1) b_(n0+r+jm)`, `|B(r)|<=1`.

Then `W_I=E_r a(r) B(r)` exactly. Suppose a finite proposed model is

`V(r)=sum_(ell=1)^M c_ell D_d(f_(ell,omega))(r)`,
`K=sum_ell |c_ell|`, `eta=E_r|B(r)-V(r)|`.

It follows that

`|W_A(h;0)| <= eps_A+u_(p,d) K+eta`,                         (CQ6)

where `eps_A=sum_n|1_[A,2A)(n)/A-1_I(n)/L|->0` is the exact inherited
interval weight distance. Linearity, CQ5, |a|=1 and this weight distance
prove CQ6. Neither V nor its coefficients need be independent of source data.
There is no uncharged statistical generalization claim: the bound holds for
every specified finite family on the actual finite clock.

For d_A below the CQ3 threshold, the explicit sufficient arithmetic premise
is `u_(p_A,d_A) K_A -> 0` and `eta_A -> 0` for the **original zero-source**
folded complement. That premise remains **OPEN**. The certificate is stronger
than cancellation alone; it is not advertised as a weaker equivalent Weyl
criterion or as a proof that learning supplies the missing structure.

## CQ5. Hostile controls and sharp logical boundaries

1. **Uniform local cubes do not cancel an adversarial complement.** On every
   clock take B=conjugate(a). Then W_I=1 exactly while CQ1--3 still hold for a.
   Any CQ4 predictor of this B obeys `u_(p,d) K+eta>=1`. The same-forcing
   wrong-seed family PE14 inherits this asymptotically after interval gluing;
   it is not the authenticated literal-zero source.
2. **Zero frequency.** If p divides h, then xi=0, a=1 and Q_d=1. Applying
   BK to this coefficient is invalid. The field coefficient must be nonzero.
3. **Full-period shifts.** h=m is zero in G. Such a shift has g^h=1 and
   erases the local source coefficient. Calling it a nonzero integer shift
   does not remove the degeneration.
4. **Magnitude or unsigned cubes.** Replacing alternating conjugations by
   an unsigned product changes the exponent from product(1-g^h) to
   product(1+g^h). It is a different observable and fails CQ1 in the fixed
   exact oracle. No independently rotating phase references are allowed.
5. **Chronology.** The cyclic clock is authenticated only on its clean source
   epoch. A later pole birth changes the p-primary dynamics. The proof does
   not license cyclic continuation of the full unwrapped history.
6. **Critical-depth norm floor.** The lower bound in CQ2 is source-exact and
   defeats a vanishing cube-norm strategy at critical depth even before any
   complement is fitted. It is an instrument obstruction, not a no-go theorem
   for source-selected signed covariance.

## CQ6. Fourth-moment dispersion widens the sparse-predictor budget

Write the normalized temporal Fourier coefficients
`A_k=E_r a(r)e(-kr/m)` and `B_k=E_r B(r)e(-kr/m)`.
Finite Fourier orthogonality and CQ1 with d=2 give

`sum_k |A_k|^4 = Q_2(a)
 = 1/m + m^-1 sum_(t!=0) |S(xi(1-g^t))|^2
 <= 1/m+(1-1/m)delta_p^2 =: V_p`.                          (CQ7)

**Proof of the Fourier identity.** Expand the fourth powers, sum over k,
and use `sum_k e(kj/m)=m` when j=0 modm and zero otherwise. The surviving
four indices obey r1-r2+r3-r4=0. Set r1=r, r2=r+h1, r4=r+h2,
r3=r+h1+h2. This is a bijection with G^3 and gives exactly Q_2(a).
The last two steps are CQ1. No further exponential-sum estimate is used.

Consequently, for **every** subset S of s temporal frequencies,

`sum_(k in S)|A_k|^2 <= sqrt(s V_p)`,
`||P_S conjugate(a)||_2 <= (s V_p)^(1/4)`.                 (CQ8)

The first inequality is Cauchy--Schwarz on S applied to |A_k|^2; taking its
square root proves the second. The projection uses frequencies reflected
by k->-k, which does not change their count. These bounds are uniform over
data-selected supports. Combining with CFS1 gives the valid improved leakage
bound `min(1, beta_p sqrt(s), (s V_p)^(1/4))`; the new fourth-moment bound
need not beat the old pointwise bound at every finite s.

For a support S contained in the nonzero frequencies let
`nu^2=sum_(k!=0)|B_(-k)|^2` and
`eta_S^2=sum_(k!=0,k notin S)|B_(-k)|^2`. Then

`|W_A(h;0)| <= eps_A+delta_p
 +(s V_p)^(1/4) sqrt(nu^2-eta_S^2)+eta_S`.                (CQ9)

This follows from the exact bilinear Fourier identity W_I=sum_k A_k B_(-k),
the bound for the zero mode, CQ8 on S, and Parseval on its complement. Thus

`s_A*(1/m_A+p_A^(-2 gamma))->0` and `eta_(S_A)->0`         (CQ10)

are sufficient for the full original Weyl gate. A simpler uniform power
budget is `s_A=o(p_A^min(1/3,2 gamma))`.

The older CFS4 bound demanded
`s_A*(1/m_A+p_A^(-gamma))->0`. CQ10 is a weaker size restriction on the
**same proposed support and same residual**. In the regime gamma<1/6,
supports of order p^(3 gamma/2) satisfy the new leakage rate and fail the
old sufficient leakage rate, because m>p^(1/3). No assertion is made that
the original complement has such supports. Sparse prediction already has
finite failures recorded in the previous round; those are not erased.

More generally Hoelder gives the explicitly charged nonsparse certificate

`|W_I| <= V_p^(1/4) * (sum_k |B_(-k)|^(4/3))^(3/4)`.      (CQ11)

The generic bound on the second factor is m^(1/4); combined with V_p>=1/m
this supplies no automatic saving. A complement selected to resonate with a
cannot evade the bill: B=conjugate(a) gives W_I=1 and forces every right-hand
side above to be at least one. The strictly improved conditional support
budget is the positive contribution to the remaining proof chain; the
required original-source spectral tail estimate remains **OPEN**.

## Provenance and independent-check scope

- Pinned parent PE1--9 and CFS1--7 supply source genealogy, epoch gluing and
  comparison results. The source signature itself is untouched.
- [Bourgain--Konyagin (2003), Theorem 2.1, printed page 78](https://www.numdam.org/item/10.1016/S1631-073X(03)00281-4.pdf)
  was reopened this round. The imported exponent is uniform in the nonzero
  additive coefficient. Its proof is not formalized by this front.
- [Tao, Higher Order Fourier Analysis, Notes 3](https://terrytao.wordpress.com/2010/04/23/254b-notes-3-linear-patterns/)
  supplies classical context for the finite cube/Cauchy--Schwarz formalism.
  The exact degeneration identity and threshold above are derived directly.
- `cube_oracle.py` compares independently constructed **integer formal
  root-of-unity coefficient histograms**, rather than matching two floating
  evaluations of the same expression. Gaussian-rational finite functions
  check the dual-atom convention and classical inequality separately.
- These checks can falsify algebra and source transport. They do not prove
  BK, certify asymptotic growth, or establish an authentic complement model.

The next result that would pay theorem debt is an original-zero upper bound
for K_A and eta_A, or a direct signed residual estimate that avoids requiring
this stronger predictor hypothesis. The local cube theorem alone supplies
neither. **Pi base-16 normality: OPEN. RH: OPEN.**
