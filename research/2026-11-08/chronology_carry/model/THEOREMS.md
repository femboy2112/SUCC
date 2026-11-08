# Frozen causal carry models and their charged arithmetic certificates

Status: **PROVED PAPER** for CM1--3 below. These are finite accounting and
source-transport statements. They do not establish original-zero covariance
decay. The model table's later-clock success is a separate finite experiment.

The source is the authenticated four-pole recurrence with literal `U0=0`.
Write `x_n={U_n}`, `k_n=floor(U_n)`, and the literal carry

    kappa_n=k_n-16 k_(n-1)=floor(16 x_(n-1)+r(n)).

At time n the model can read kappa_n and kappa_(n-1). It never reads
kappa_(n+1). The initial convention kappa_0=0 is used only before training.
For a clean prime clock `S=xi<16>`, let `n=n0+r+jm`, `0<=r<m`, `0<=j<q`,
`a_r=e(h*x_r/p)`, and `B_r=q^-1 sum_j e(h*(U_n-x_r/p))`. Then
`W=mean_r a_r B_r=mean_n e(hU_n)` exactly. The symbol x_r in this finite-field
formula denotes the principal numerator; it is distinct from the real x_n.

## CM1. The frozen carry-prediction certificate

Let `g_h` be *any fixed table*, with values in the closed unit disk, on either
literal carry feature `kappa_n` or `(kappa_(n-1),kappa_n)`. The table is fitted
on earlier source times and held fixed. Values outside its recorded domain
are defined to be zero. Put

    F_r=q^-1 sum_j g_h(feature_(n0+r+jm)),
    V_r=conjugate(a_r)*F_r,   M=mean_r F_r,
    rho=mean_r |B_r-V_r|.

Then

    |W| <= |M|+rho.                                      (CM1)

Proof: `a_r V_r=F_r`, while `|a_r|=1`. Subtract and average. QED.

This table is nonlinear as a function of source history, but linear in its
fixed table entries after training. It does not become an arithmetic estimate
merely because it is nonlinear. The required source obligations remain a
bound for its carry occupancy sum M and a bound for its residual rho.

If N_c is the later-clock count of feature c and L=mq, then
`M=sum_c N_c g_h(c)/L`. This is the exact carry-occupancy statistic evaluated
by the instrument. The experiment does not replace N_c/L by an iid or uniform
law. Neither masked sums nor table coefficients receive free Weil bounds.

## CM2. An honest signed-orbit certificate for the prediction

Extend **V**, not B, by zero from S to F_p. Its Fourier coefficients are
`c_t=p^-1 sum_S V(x)e(-t*x/p)`. Fourier inversion reconstructs V on S,
so the residual in CM1 is unchanged. The QCO1 orbit calculation gives

    R=c_(-h)=(m/p) M,
    C_O=sum_(d in O)c_(d-h)=(m/p) M G_O,
    G_O=sum_(d in O)e(-d*xi/p),

where O ranges over multiplicative H-cosets in F_p^* and `H=<16>`.
Consequently, with `beta=min(1,sqrt(p)/m)`,

    |W| <= rho + (m/p)|M| + beta*(m/p)|M| sum_O |G_O|.   (CM2a)

This formula retains the named resonance and all signed orbit sums. Unlike
expanding B itself canonically, construction of V uses no held-out phase
value B_r. Nevertheless, CM2a is a more expensive upper bound than the direct
CM1 identity: the exact signed orbit reconstruction already averages to M.
It is reported to disclose the arithmetic accounting, not as a manufactured
improvement. It is not a bound on M derived from local prime geometry.

The periods satisfy the exact identity

    sum_O |G_O|^2=p-m.                                 (CM2b)

Proof: use unscaled periods `eta_c=sum_(u in H)e(cu/p)`. Each coset contributes
m identical values as c ranges over F_p^*. Orthogonality gives

    sum_(c!=0)|eta_c|^2
      =sum_(u,v in H) [p*1_(u=v)-1]
      =pm-m^2=m(p-m).

Division by m proves the assertion; multiplication by nonzero -xi permutes
the period labels. If d=(p-1)/m, Cauchy--Schwarz yields the explicit a-priori
cost bound

    K_p=(m/p)[1+beta*sqrt(d*(p-m))],
    |W| <= rho+K_p |M|.                                (CM2c)

The code encloses sqrt(p) and sqrt(d*(p-m)) outward with integer square roots.
It reports `(m/p)|M|` and the nonresonant term separately. Exact period phases
need not be evaluated, and no held-out B is used to choose K_p. The cost is
only an upper bound; lower comparison between certificates uses the direct
CM1 expression, never treats K_p as the exact quotient cost.

## CM3. Rigorous finite data and model-selection discipline

The table is defined, rather than merely approximated, by Gaussian dyadics
with denominator 2^24. In each old training cell, the inherited outward Taylor
boxes enclose the empirical phase mean. The midpoint is rounded toward zero
in each coordinate to the declared grid. While its Euclidean norm exceeds
one, both nonzero coordinates move one grid unit toward zero. Termination
is immediate from the strictly decreasing sum of coordinate magnitudes, and
the final table belongs exactly to the closed disk. Thus table uncertainty
is absent. Different sound interval evaluators could define a neighboring
table; this experiment commits the actual table bytes before later access.

The exact source implementation uses one common denominator D for all poles
up to the final source time. For forcing numerator F_n=D*r(n), it updates

    N_n=16 N_(n-1)+F_n,
    (kappa_n,R_n)=divmod(16 R_(n-1)+F_n,D),
    k_n=16 k_(n-1)+kappa_n.

Induction gives `N_n=D*k_n+R_n`, `0<=R_n<D` and `U_n=N_n/D`. It retains
full unwrapped numerator and carry stream hashes; the exact literal source
is not replaced by a modular-only history. Selected checkpoints are also
verified by the independent BBP finite power-sum algorithm.

All phase values use inherited 80-bit outward integer rectangles and exact
rational range reduction. For a box z, its squared-norm interval [l,u]/S
implies the modulus interval

    [floor(sqrt(max(0,l)*S)), ceil(sqrt(max(0,u)*S))]/S.

Every residual and mean modulus is enclosed by this rule. Summation and
rational division preserve outward endpoints. A finite failure therefore
refutes a declared finite certificate threshold, not pi normality or the
possibility of another model.

## Controls and boundaries

For the zero prediction, rho is exactly mean|B|. A two-replica source can have
large rho even when W is tiny. For coherent control B=conjugate(a), W=1, and
CM1 must remain at least one for every frozen table. This complement control
is an observer stress test, not a different authentic U0=0 history.

An independently reset observer gauge without simultaneous transport changes
aB and invalidates CM1's displayed identification. A future carry encodes
current-state information and is excluded from the model's feature contract.
A finite successful certificate, were one obtained, would still leave its
all-epoch and every-fixed-nonzero-h arithmetic estimate unpaid.

Inherited dependencies: [QCO1--5](../../frontier_connections/crucible/THEOREMS.md),
[exact source tool](../../complement_budget/source_budget.py),
[integer phase intervals](../../covariance_forge/intervals.py), and the prior
[carry-history experiment](../../covariance_forge/HISTORY_PREREGISTRATION.md).
This round differs by freezing a trained table and transferring it to a later
clock with explicit signed-orbit accounting. It is not SUCC's first carry model.
