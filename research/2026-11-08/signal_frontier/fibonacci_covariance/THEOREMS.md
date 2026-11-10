# An integer Fibonacci clock can acquire the signed signal faithfully

**PROVED PAPER / finite certificates. Original-zero signed covariance,
pi base-16 normality and RH remain OPEN.** This is an observer acquisition
and conditioning theorem, not an arithmetic decay theorem. It uses the
new FD calibration with its exact source dependence. No worldwide novelty
or new classical equidistribution theorem is claimed.

There are two time axes. The BBP source time n retains its original forcing,
chronology and literal zero boundary. The integer probe clock j rotates a
sensor's origin around a calibrated circle. We do **not** assume that the
BBP source has golden-rotation dynamics, and do not replace n by Fibonacci
times. A usable apparatus supplies this probe intervention, a common phase
anchor, and the source response at each selected origin. The learning state
is the existing SUCC finite transcript and its memory, not a new category.
Exact golden rotation is a declared authenticated apparatus model. Finitely
many approximate returns do not identify an arbitrary real rotation exactly;
the calibration protocol must retain its angle interval and propagate its
error by FC4. A successful finite test is not an infinite source certificate.

## FC1. Exact return and grid transport, using only integer clock ticks

Let alpha=(sqrt5−1)/2, F_0=0, F_1=1, F_(k+1)=F_k+F_(k−1). For k>=2 put
q=F_k, p=F_(k−1). Then

    q alpha−p = (−1)^(k−1) alpha^k,
    gcd(p,q)=1,
    q alpha^k < 1.                                      (FC1)

The first identity follows by induction from alpha²=1−alpha; the gcd
identity follows backwards through the Fibonacci recurrence. For the last
inequality, the Binet identity gives
q alpha^k=[1−(−1)^k alpha^(2k)]/sqrt5<1. Alternatively induction gives the
same bound. Define actual and reference probe positions

    theta_j=theta_0+j alpha (mod1),
    y_j=theta_0+j p/q (mod1),       0<=j<q.

The y_j are exactly one translated q-grid. Each theta_j is obtained from y_j
by a displacement of the same sign, of magnitude at most

    epsilon_k=(q−1)alpha^k/q < 1/q.                      (FC2)

Thus the entire q-sample acquisition has an explicit, coherent transport
from a rational clock grid. The total clock phase theta_0 is arbitrary but
shared; it is not silently independently reset at each observation.

## FC2. Finite acquisition has a discrepancy and calibration error budget

Write D(nu)=sup_I |nu(I)−|I|| for circular half-open intervals I. The empirical
law nu_k=q^(-1) sum_j delta_(theta_j) satisfies

    D(nu_k) <= 1/q+epsilon_k < 2/q.                      (FC3)

**Proof.** A translated q-grid has interval discrepancy at most1/q. Suppose
the displacements in FC2 are nonnegative; the other direction is identical.
If a displaced point belongs to [a,b), its original point lies in
[a−epsilon_k,b). Conversely every original point in [a,b−epsilon_k) stays
inside [a,b). Apply the grid count bound to those enlarged/shrunken circular
intervals. If their length exceeds1 or is negative, the corresponding
trivial bound1 or0 supplies the same inequality. This proves FC3, including
wrapping intervals and all endpoint conventions. No random probe origin or
Denjoy–Koksma theorem is required.

If measured positions tilde(theta_j) differ from theta_j by circular distance
at most rho, their empirical law obeys

    D(tilde(nu_k)) <= 1/q+epsilon_k+2rho.                (FC4)

Expand and shrink each circular interval at both endpoints; the added Haar
length is2rho. An error exceeding a semicircle only makes this bound
uninformative, not invalid. If the apparatus estimates alpha with error
eta and the initial anchor with error rho_0, one may take
rho=rho_0+(q−1)eta. Hence refining the return clock requires a correspondingly
more accurate angular step. A common exact anchor shift alone leaves FC3
unchanged.

Now let Omega be any finite probability space, x:Omega→T its local phase,
mu=x_*Pr, a=e(hx), |b|<=1, W=E(ab), and h a fixed nonzero integer. Here
`e(t)=exp(2pi i t)`. For M>=1, P_theta averages on the pullback of the M
half-open cells with boundaries theta+r/M. Define the finite integer-clock
response

    F_(M,k)=q^(-1) sum_(j<q) E[(P_(theta_j)a)(P_(theta_j)b)],
    c_(M,h)=sinc²(pi h/M).

Then, uniformly over M, b, theta_0 and finite source families,

    |F_(M,k)−c_(M,h)W|
      <= 2pi|h|D(mu)+4pi|h|(1/q+epsilon_k).             (FC5)

For noisy probe positions add8pi|h|rho to the right side.

**Proof.** FD1 gives, at every individual origin,
E_mu|P_theta^mu a−P_theta^Haar a|<=2pi|h|D(mu), even with empty cells.
Conditional averaging is symmetric in the bilinear pairing, so the retained
mean is E[b P_theta^mu a]. For fixed x, the function
f_x(theta)=P_theta^Haar a(x) has total variation at most4pi|h| on the circle:
between its M jumps its derivative modulus is at most2pi|h|, and the sum of
jump magnitudes is at most2pi|h|. Each jump changes an adjacent-cell average,
whose difference is at most2pi|h|/M. The elementary integration-by-parts
bound for a periodic function of bounded variation is

    |integral f d(nu−Haar)| <= D(nu) Var(f).

For this piecewise smooth f it follows directly by integrating its derivative
against the cumulative signed interval masses and adding its finitely many
jumps, with the same half-open convention. All such interval masses have
modulus at most D(nu). Its Haar integral is exactly c_(M,h)a(x), by FD2.
Apply FC3 or FC4, multiply by b, average, and use |b|<=1. QED.

If C=Cov(a,b)=W−(Ea)(Eb) and C_(M,k)=F_(M,k)−(Ea)(Eb), all covariances being
bilinear, then add `(1−c_(M,h))|Ea|` to FC5. No conjugate or marginal term is
dropped. The origin labels and the same a,b are retained across resolutions.

## FC3. A source-faithful reduction with finite acquisition costs

Keep exactly

    r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2),
    U_0=0, U_n=16U_(n−1)+r(n).

On J_A={A,...,2A−1}, use the preceding authenticated prime selector p_A and
x_n=[U_n]_(p_A), a_n=e(hx_n), b_n=e(h(U_n−x_n)). The already proved source
local discrepancy d_A in FD3 tends to0 for every integer A→infinity. Hence
for any fixed M>|h| and any k_A→infinity,

    |F_(A,M,k_A,h)−c_(M,h)W_A(h;0)|
       <=2pi|h|d_A+4pi|h|(1/F_(k_A)+epsilon_(k_A)) ->0.  (FC6)

For calibrated noisy positions it is sufficient additionally that rho_A→0.
The fixed-resolution coefficient c_(M,h) is positive. Therefore decay of
this **finite integer-clock response** is equivalent to original Weyl decay.
Acquisition may grow arbitrarily slowly with epoch A; the proof does not
require matching Fibonacci probe times to BBP source times.

This pays an observer realization/resource debt. It does **not** make the
remaining arithmetic claim weaker. The one unproved statement is still a
signed source estimate for this retained response, or equivalently the
original-zero covariance. The classical covariance-to-Weyl and Green-tail
to-normality arrows remain as in the preceding handoff.

The three-return geometry theorem FG3–FG5 in
`../fibonacci_geometry/THEOREMS.md` supplies one concrete calibration route.
Its authenticated winding p=F_(k−1) is necessary: a return phase modulo1
alone does not recover alpha. With point error epsilon, radius R, and
`t=|e(q alpha)−1|`, its bound
`eta<=2epsilon/[q(Rt−2epsilon)]` implies a q-tick origin error no greater
than `rho_0+2epsilon/(Rt−2epsilon)`, where rho_0 is the separately retained
anchor error. Use this value in FC4–FC6. Its stronger curvature/source-phase
reconstruction requires epsilon/(Rt²)→0. Thus the full chain explicitly
charges the tightening geometric precision when return scales shrink.

A causal implementation records ticks0,...,2q and the source-probe responses,
then uses the completed three-return certificate to calibrate the retained
first q readings. Alternatively it applies that learned clock to a later
source epoch. The theorem describes these finite history statistics; it does
not assume a strictly-past predictor was given future measurements for free.
The records must preserve source signatures, integer time, winding, common
anchor and calibration errors across resolution.

A source-preserving local phase calibration error can also be included.
If |x'_n−x_n|_T<=rho_x, put a'_n=e(hx'_n) and b'_n=z_n conjugate(a'_n), where
z_n=e(hU_n) is measured in the same coherent reference. Then a'b'=z exactly
and D(mu')<=D(mu)+2rho_x. Applying FC5 to this new split adds at most
4pi|h|rho_x, with no hidden independence assumption. Independently rotating
the two channel gauges without the inverse transport does not preserve z.

## FC4. Fibonacci clocks give stable Fourier frames at linear acquisition cost

Let H>=1, q=F_k>2H, and let

    f(theta)=sum_(m=−H)^H c_m e(m theta),
    (A_k c)_j=q^(-1/2)f(theta_j).

Let A_grid use y_j from FC1. Since q>2H, exact finite Fourier orthogonality
gives `||A_grid c||_2=||c||_2`. Furthermore

    ||A_k−A_grid||op <= tau_k,
    tau_k=2pi H sqrt(epsilon_k/q) <2pi H/q.              (FC7)

Consequently

    max(0,1−tau_k)² ||c||² <= ||A_k c||²
                              <=(1+tau_k)² ||c||².     (FC8)

**Proof.** Join y_j to theta_j along its declared displacement direction.
These q short arcs are disjoint except for endpoints: their starts form a
q-grid, all directions agree, and their lengths are <=epsilon_k<1/q.
Cauchy–Schwarz on each arc gives

    |f(theta_j)−f(y_j)|²
       <=epsilon_k integral_(arc_j) |f'(t)|²dt.

Sum, divide by q, and use Parseval:
`integral|f'|²=4pi² sum m²|c_m|²<=4pi²H²||c||²`.
This proves FC7. The triangle and reverse triangle inequalities with the
grid isometry prove FC8. In particular q>2piH suffices for stable injectivity;
choosing the first Fibonacci q>8H gives an explicit linear sample budget.
The bound is sufficient, not an asserted sharp frame constant.

For independent position errors of size at most rho, a further operator
perturbation bound is

    ||A_noisy−A_k||op
       <=2pi rho sqrt(H(H+1)(2H+1)/3).                 (FC9)

This follows from the pointwise derivative bound
`|f'|<=2pi sqrt(sum_(−H)^H m²)||c||` and Cauchy–Schwarz in coefficient space.
Replace tau_k in FC8 by tau_k plus FC9. This exposes the phase-precision
cost instead of calling the clock self-calibrated without an error budget.

## FC5. Curvature transports Fourier information, with its exact noise cost

A declared finite-band pin probe of a circle law mu uses the kernel

    B_(2,H)(t)=sum_(0<|m|<=H) e(mt)/(2pi²m²),
    F_H(theta)=integral B_(2,H)(theta−x) dmu(x).

Thus its nonzero Fourier coefficients are
`c_m=mu_hat(m)/(2pi²m²)`, where
`mu_hat(m)=integral e(−mx)dmu(x)`. Equivalently,
`−(1/2)F_H''` has nonzero moments mu_hat(m). This is the finite-band version
of the established Bernoulli pin curvature inverse, with its sign convention
explicit. It reconstructs these moments of a law, not its generating source
history or literal initial boundary.

If tau_k<1, least-squares inversion of the clock frame recovers c exactly
from noiseless samples. If the sample noise has RMS at most nu, then

    ||c_est−c||_2 <=nu/(1−tau_k),
    ||mu_hat_est−mu_hat||_(2,0<|m|<=H)
          <=2pi²H² nu/(1−tau_k).                      (FC10)

The least-squares inverse has norm at most1/(1−tau_k) by FC8; the curvature
multiplier is at most2pi²H². For the actual normalized circle coordinate,
a physical radius change does not change these angular multipliers; a
change of angular coordinate must carry its derivative scaling explicitly.

For H'<H, truncating the reconstructed coefficient vector to |m|<=H'
commutes exactly with taking the H'-probe and with common phase rotations.
Under an angular shift x→x+beta, mu_hat(m) acquires e(−m beta); the observed
profile acquires the corresponding pullback. These are the declared phase
and curvature transports across resolution. No independently rotating
per-resolution gauges may be identified without that transport.

The finite-band kernel is part of the allowed probe menu. If an apparatus
instead measures the full Bernoulli profile, its unmodeled Fourier tail is
an additional sample error and must be charged to nu. A low-frequency
reconstruction cannot simply assume that arbitrary source laws are
band-limited. Curvature inversion amplifies noise; it does not create it or
prove an energy decay statement.

## FC6. What the calibrated geometry does and does not constrain

The combined geometry and acquisition package constrains the error of the
measured signed statistic. It retains a source-selected signal; it does not
supply a one-sided arithmetic bound on that signal. Explicit receipts:

1. **Perfect geometry, maximally correlated complement.** Take x Haar,
   a=e(hx), b=conjugate(a). Then W=1, and FC5 implies
   F_(M,k)→sinc²(pi h/M), nonzero for M>|h|. The same perfectly calibrated
   Fibonacci circle can accompany a zero-mean complement. Geometry alone
   cannot choose between these opposite signed outcomes.
2. **Same-forcing coherent seed.** For s*=−pi/16, the exact Green identity
   gives U_n(s*)=−T_n and W_A(h;s*)→1 for every fixed h. A probe circle has
   the same Fibonacci returns, radius, curvature and frame bounds for this
   source as for seed0. These geometric facts cannot authenticate the
   original boundary. This control does not claim a rational p-primary
   decomposition of the irrational seed; the source-independent observer
   geometry is the common hypothesis being tested.
3. **Periodic completions.** If s=k/(16^p−1)−pi/16, the completed source is
   periodic modulo1. At h=16^p−1 every completed phase is1 and the authentic
   tail again gives W_A→1. The same clock geometry remains valid. Neither
   seed is substituted into the zero-source claim.
4. **Sensor alias.** If h is a nonzero multiple of M, c_(M,h)=0. With Haar
   x and b=conjugate(a), the full W is1 while the origin-averaged retained
   mean is0. M>|h| is a sufficient explicit anti-alias condition.
5. **Independent clock gauges.** Choosing a separate rotation
   g_j=−j alpha (mod1) makes every effective origin equal theta_0. Each
   single sample still lies on the same circle, but the acquisition law
   becomes one atom with discrepancy1. A common operational reference is
   necessary; untransported per-sample gauges cannot use FC3.
6. **Magnitude-only homometric aliases.** Uniform laws on
   {0,1,4,6}/12 and {0,1,3,7}/12 have the same directed difference multiset,
   hence identical Fourier magnitudes at every integer frequency. They
   are neither translates nor reflections in this12-grid. Their complex
   Fourier coefficients differ. Perfect circle curvature plus phase-blind
   spectra therefore cannot reconstruct the anchored law. The exact
   difference histograms are checked independently by the oracle.

7. **Finite nodes without a bandwidth contract.** For any q distinct probe
   nodes theta_j, let
   `v(theta)=product_j[1−cos(2pi(theta−theta_j))]` and
   `g(theta)=v(theta)cos(2pi(q+1)theta)`. This real trigonometric polynomial
   is nonzero, vanishes at every node, and has mean0 because v has degree
   at most q. It has degree at most2q+1. Its second derivative is nonzero.
   Choose nonzero t with `|t| ||g''||_infinity<=1`. The probability density
   `1−(t/2)g''` is at least1/2 and has Bernoulli pin profile t g. It and
   Haar measure therefore give identical zero pin readings at every node,
   despite different curvature and Fourier moments. This is an exact
   positive-law countermodel, not only an arbitrary signal alias. The
   finite-band hypothesis or a charged tail budget is indispensable.

These countermodels refute only the specified shortcuts. They do not refute
a future source-selected signed covariance inequality. The next useful
arithmetic theorem must control the **retained complex cell charges** after
this acquisition error has been paid, and must use original chronology or
boundary data absent from the common geometric controls.

## Provenance and certificate scope

Read-only premises: AGENTS.md; the original selected source; FD1–FD5 in
`../fixed_depth/THEOREMS.md`; prior Bernoulli pin convention and finite
history/transcript machinery. FC1–FC10 are proved here from elementary
Fibonacci algebra, interval counts, finite conditional expectation,
Cauchy–Schwarz and Parseval. No external analytic estimate is imported.
The clock identities and partition assignments are checked in exact
Q(sqrt5), while all source Fourier readouts use inherited outward rational
rectangles. Neither is called a Lean kernel proof. The frame finite tests
are certificates on specified inputs, not substitutes for its operator
proof. Shared source code/data and shared model-family provenance remain
explicit; this is not external scholarly review.
