# Dynamic boundary certificates: the endpoint complexity budget

2026-11-12. Main XXV parent `db9fb4b84672050efa79b13377f1e73364598a14`.

**Verdict: proved local necessary-condition theorem and conditional certificate,
with exact finite calibrations.** A source-uniform local filter inequality can
certify a persistent positive escape only by paying a linear endpoint
oscillation budget, or by using a genuinely smaller source-selected domain.
Bounded filter potentials cannot supply that gain. This statement does not
exclude unbounded potentials, source-selected proofs, other proof methods, or
base-16 normality of pi. R0 and normality remain **OPEN**.

These are elementary telescoping proofs. Exact rational tests check the finite
implementation and controls; they do not supply the universal quantifiers.
No external peer review, formal-kernel verification, or priority claim is made.

## 1. Hole contract and relation to the archive

The steelman is to combine ordered boundary filters with known dynamical
relations, so that a target has a positive dual lower certificate. The question
is whether dynamical relations alone make that certificate positive.

- **Target:** on every sufficiently large integer shell `[A,2A)`, prove a
  positive constant lower bound for the authentic completed escape average
  `A^-1 sum (1-Re e(U_n(0)+T_n))`. This is the existing R0 rung.
- **Candidate instrument:** a pointwise local inequality plus an exactly
  telescoping boundary potential, valid on declared domains at each time.
- **Weakest proved statement:** when the domains also admit the coherent
  completed-zero history, the actual certified gain is at most the difference
  of two endpoint separations from that history. Sublinear endpoint
  oscillation therefore gives no positive limiting shell margin.
- **Novelty tax:** this is a necessary complexity budget for a specified
  certificate class, not a sufficient reformulation of normality. It is valid
  even when the selected trajectory demonstrably has positive escape.
- **Cheapest falsifier:** substitute the coherent history in every local
  inequality. A claimed uniform margin with small endpoint budget is then an
  explicit contradiction. Check the exact two-fixed-point calibration below.
- **Next lamp:** construct source-selected domains whose exclusion of the
  coherent history is proved from the authentic zero source, or construct
  potentials with paid growth, endpoint signs, and measurement errors.

The archive already supplies the core source distinction:

- [APH-01/02](../../2026-11-07/pinbed_yoneda_oscillators/ANCHORED_PATHS_VS_HOLONOMY.md)
  proves seed-blindness of source-corrected temporal holonomies and finite
  periodic impersonation with explicit observation tolerance.
- [The current frontier](../../../docs/PI_NORMALITY_FRONTIER.md) distinguishes
  literal zero authentication, the rational `1/16` circle alias, and the
  coherent `-pi/16` nonnormal seed.
- [PR #605, PT-01--03](https://github.com/femboy2112/SUCC/blob/f4151c4ae877ee43c4b7d130174b6bec1dbab9d6/research/2026-11-12/holographic_boundary_filters/PHASE_AND_TARGET.md)
  gives target-relative linear duality and approximation/noise budgets.
  Its dynamical rows require endpoint payments on empirical orbits.

The addition here is an explicit lower bound on those endpoint payments, after
the same-forcing coherent history is substituted. It quantifies a limitation
already suggested by the archive; it is not a claim to have discovered the
general idea of a coboundary certificate.

## 2. DC-01: a constructive finite-window certificate

Let `D_n` be arbitrary nonempty state sets, and let
`F_n:D_n -> D_(n+1)` be declared transitions for `A <= n < B`. Let `g_n` and
`V_n` be real functions on their stated domains, and let `c_n` be real numbers
and `epsilon_n >= 0`. Suppose the following inequality has been proved for
**every** `x in D_n`:

$$
g_n(x)\ge c_n+V_{n+1}(F_nx)-V_n(x)-\epsilon_n. \tag{1}
$$

Every admitted trajectory `x_(n+1)=F_n(x_n)` then obeys

$$
\sum_{n=A}^{B-1}g_n(x_n)\ge
L_{A,B}(x):=\sum_{n=A}^{B-1}(c_n-\epsilon_n)
+V_B(x_B)-V_A(x_A). \tag{2}
$$

**Proof:** sum (1); every interior potential occurs once with each sign. No
invariance of an empirical law is assumed. This is a usable certificate when
the local inequality and the two endpoint values are independently bounded.
It can use different filters at each time, and can include finite memory by
taking the observer's augmented state as `D_n`.

For measured endpoint values `v_A,v_B` with rigorous errors `delta_A,delta_B`,
the paid lower bound is

$$
\sum(c_n-\epsilon_n)+v_B-v_A-\delta_A-\delta_B. \tag{3}
$$

Strict positivity of (3) is a valid finite-window conclusion. A uniform R0
conclusion requires a positive constant after division by `A`, for **all**
sufficiently large integer `A`, with the authentic history proved to belong
to every asserted domain. Checking a sampled mesh does not prove (1) between
mesh points without a separate error theorem.

## 3. DC-02: a zero-cost rival forces endpoint separation

Assume the same domains admit another trajectory `z_n` with `g_n(z_n)=0`
for all `A <= n < B`. Define

$$
\Delta_n=V_n(x_n)-V_n(z_n).
$$

Then the certificate (2), regardless of whether it is a sharp bound for the
actual target, satisfies

$$
\boxed{L_{A,B}(x)\le \Delta_B-\Delta_A
\le \operatorname{osc}_{D_B}V_B+\operatorname{osc}_{D_A}V_A.} \tag{4}
$$

Here `osc_D V=sup_D V-inf_D V`; the result is useful when these quantities
are finite. Indeed, (2) on the rival says
`sum(c_n-epsilon_n)+V_B(z_B)-V_A(z_A) <= 0`. Subtract this expression from
`L_(A,B)(x)` to obtain the first bound. The second follows by bounding each
endpoint difference by its oscillation.

For `B=2A`, if `osc V_A+osc V_(2A)=o(A)`, then the certified normalized
gain has `limsup <= 0`. Thus this certificate class cannot prove a positive
R0 margin with sublinear endpoint oscillation. The conclusion concerns the
**certificate**, not the truth of escape on the actual orbit.

The oscillation, rather than the absolute size of `V_n`, matters: adding any
time-dependent constant `b_n` to `V_n` and subtracting `b_(n+1)-b_n` from
`c_n` changes neither (1) nor the lower bound. A large state-independent
linear drift is no escape from (4).

## 4. DC-03: application to the actual BBP transition law

Retain the exact original source and the separately authenticated zero seed:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_{n+1}=16U_n+r(n+1),\quad U_0=0.
$$

The true positive tail obeys `16 T_n=r(n+1)+T_(n+1)` and
`U_n(0)+T_n=16^n pi/16`. On the circle set

$$
F_n(x)=\{16x+r(n+1)\},\qquad
g_n(x)=1-\operatorname{Re}e(x+T_n),\qquad e(t)=\exp(2\pi i t).
$$

The authentic trajectory is `x_n={U_n(0)}`. The coherent wrong seed
`s_*=-pi/16` supplies the exact rival

$$
z_n=\{-T_n\},\qquad F_n(z_n)=z_{n+1},\qquad g_n(z_n)=0.
$$

Hence (4) applies to every proposed inequality (1) valid on the entire
circle, or any declared domains containing both histories. Its truth does
not require computing pi, approximating the tail, or assuming anything about
the authentic phase distribution.

If the local certificate uses the raw escape `g(x)=1-Re e(x)` instead,
the true-tail transfer must be paid. The chord inequality and the existing
[canonical tail budget](../../../observational_succ/duck_bbp.py) give

$$
|g_n(x)-g(x)|\le2\pi T_n
\le\frac{94\pi}{225(n+1)^2}.
$$

Thus a raw certificate implies a completed lower bound after subtracting
`sum 2 pi T_n`; on `[A,2A)` the **normalized** payment is at most
`94 pi/[225(A+1)^2]`. The rival's raw cost is correspondingly small rather
than exactly zero. This vanishing tail payment does not create the missing
positive margin.

**Domain firewall.** The rival is not an admissible original-zero source.
This theorem deliberately applies only when a purported local estimate has
relaxed its domain enough to admit that rival. A proof with domains `D_n`
that verifiably retain `U_0=0` and exclude the rival may evade the result.
Its required source-dependent inequalities still have to be proved.
Restricting `D_n` to an asserted good phase region without proving actual
membership simply relocates the open escape estimate.

Similarly, an unwrapped potential or an augmented observer retaining a
source selector is not automatically covered. Apply (4) only after checking
that both trajectories belong to the **same** declared domains and that the
required endpoint oscillations are finite. Access to an integer lift is a
different observation contract from access to circle phases.

## 5. DC-04: Fourier coefficient and precision budgets

For a real finite Fourier potential, write

$$
V_n(x)=a_{n,0}+\sum_{h\in H_n}a_{n,h}e(hx),\qquad
H_n\subset\mathbb Z\setminus\{0\},\qquad
M_n=\sum_{h\in H_n}|a_{n,h}|.
$$

Reality requires conjugate coefficients. No bound on degree is assumed.
Since `|e(hx)-e(hy)|<=2`,

$$
\operatorname{osc}V_n\le2M_n,\qquad
L_{A,2A}(x)\le2(M_A+M_{2A}). \tag{5}
$$

In particular, a certified gain `L_(A,2A) >= eta A`, with `eta>0`, requires
`M_A+M_(2A) >= eta A/2`. Increasing only the number or frequency of filters
while keeping this coefficient mass bounded cannot achieve that certificate.
Linear coefficient mass is **necessary here, not sufficient**: signs and
the local inequality remain essential.

If each Fourier reading at endpoint `n` has complex absolute error at most
`delta_n`, evaluating the potential has error at most `delta_n M_n`, provided
the constant coefficient is known exactly. Formula (3) then pays

$$
E_{A,2A}\le\delta_A M_A+\delta_{2A}M_{2A}. \tag{6}
$$

This is the ordinary worst-case coefficient-norm budget. It does not assert
that actual errors attain it or that independent errors are physically
necessary. A calibrated correlated-error model may improve it. Nor does
linear coefficient mass alone force exponentially precise observations:
with mass `O(A)`, fixed sufficiently small endpoint error can preserve a
fixed normalized margin. To make this particular normalized error budget
vanish requires a correspondingly vanishing product in (6) divided by `A`.

If an implementation has a source-derived phase uncertainty `d_n`, each
mode error is at most `2 pi |h| d_n`. Its sharper endpoint payment is
`2 pi d_n sum_h |h a_(n,h)|`; large frequency and coefficient mass are
different costs and must not be conflated.

## 6. DC-05: discrete arithmetic exclusion has a spatial resolution cost

The coherent history is irrational, while the authentic `U_n(0)` is rational.
It is therefore legitimate to ask whether restricting (1) to authentic
arithmetic grids defeats the barrier. It removes the literal rival from the
domain, but a quantitative version survives for sufficiently smooth filters.

Define a **deliberately unreduced** denominator envelope

$$
D(j)=(2j-1)(4j-1)(8j-7)(8j-3),\quad
Q_0=1,\quad Q_n=\operatorname{lcm}_{1\le j\le n}D(j),\quad
\Gamma_n=Q_n^{-1}\mathbb Z/\mathbb Z.
$$

The combined rational form in the canonical `duck_bbp.forcing` shows that
each reduced forcing denominator divides `D(j)`. Therefore
`F_n(Gamma_n) subset Gamma_(n+1)` and the authentic zero-seed orbit lies
in these grids. The `Q_n` are monotone under divisibility, and
`Q_n >= 2n-1`. We do not identify `Q_n` with the reduced denominator of
`U_n`, and we need no exponential growth assertion.

Suppose `V_n` are real Lipschitz functions on the **entire** circle, but (1)
has only been proved on `Gamma_n`. The residual

$$
R_n(x)=g_n(x)-c_n-V_{n+1}(F_nx)+V_n(x)+\epsilon_n
$$

has a valid circle-geodesic Lipschitz bound

$$
\ell_n=2\pi+16\operatorname{Lip}(V_{n+1})+
\operatorname{Lip}(V_n).
$$

Indeed `g_n` has Lipschitz bound `2 pi`, and `F_n` has bound 16. Every
circle point is within `1/(2Q_n)` of `Gamma_n`. Since the residual is
nonnegative on that grid, its value on the coherent history satisfies

$$
R_n(z_n)\ge-\frac{\ell_n}{2Q_n}.
$$

Repeating the proof of (4) gives the exact budget

$$
\boxed{L_{A,B}(x)\le\Delta_B-\Delta_A+
\sum_{n=A}^{B-1}\frac{\ell_n}{2Q_n}
\le\operatorname{osc}V_B+\operatorname{osc}V_A+
\sum_{n=A}^{B-1}\frac{\ell_n}{2Q_n}.} \tag{7}
$$

The oscillations in (7) are on the **whole circle**, not just the grids.
All uses of the functions between grid points are paid by their declared
Lipschitz bounds. A grid-only arbitrary function without a controlled
extension is outside this statement.

For `B=2A`, put `K_A=max_(A<=n<=2A) Lip(V_n)` and
`O_A=osc V_A+osc V_(2A)`. Monotonicity of the denominator envelope yields

$$
\frac{L_{A,2A}}A\le\frac{O_A}A+
\frac{2\pi+17K_A}{2Q_A}. \tag{8}
$$

Consequently a certified normalized gain of at least `eta>0` requires

$$
\boxed{K_A\ge
\frac{2Q_A(\eta-O_A/A)-2\pi}{17}.} \tag{9}
$$

If `O_A=o(A)`, this forces `K_A >= (2 eta Q_A-o(Q_A)-2 pi)/17`.
Thus merely keeping exact rational denominator compatibility, while using
small endpoint potentials, requires filters capable of resolving the
denominator-scale spacing. Exact exclusion of an irrational rival is not
uniformly robust under a smooth observation relaxation.

This is a **source-attested necessary condition** for this grid-certificate
class. It does not show that denominator-scale filters can prove R0, nor that
the entire original carrier has been reduced to these grids. Stronger
source constraints may shrink the domains substantially; their construction
and membership proof are separate obligations.

**Reduced-forcing-grid corollary.** The deliberately unreduced envelope is
not necessary for the theorem. Define
`q_0=1` and `q_n=lcm_(1<=j<=n) denominator(r(j))`, with each forcing
denominator reduced to lowest terms. These denominators are also monotone
under divisibility, `q_n` divides `Q_n`, the authentic orbit lies in
`q_n^-1 Z/Z`, and `F_n` maps this grid into the next one. If the local
inequality is proved on these **smaller declared grids**, formulas (7)--(9)
hold with every `Q_n` replaced by `q_n`. No assertion
`q_n >= 2n-1` is needed or made, and `q_n` is not asserted to equal the
reduced denominator of the accumulated state `U_n`. More generally, the
same proof applies to any stated forward-closed uniform grid family with
monotone denominators. The resolution requirement is relative to the grid
on which the certificate actually claims validity; it is not a requirement
on every possible BBP filter.

For Fourier potentials,
`Lip(V_n) <= 2 pi sum_h |h a_(n,h)|`. Therefore (9) also forces the
maximum of this weighted coefficient mass over the shell to be sufficiently
large. The same weighted mass appears in the phase-uncertainty payment in
Section 5: resolving the arithmetic spacing and controlling observation
error are the same quantitative constraint on this instrument.

The grid-extension constant is sharp for general Lipschitz residuals:
`R(x)=-L d_circle(x,Gamma_Q)` is zero on every grid point and reaches
`-L/(2Q)` at each midpoint. This is an exact residual calibration, not a
claim that this residual has been realized by a BBP certificate.

### C² refinement: a quadratic resolution budget

When the potentials are twice continuously differentiable **periodic**
functions, smooth interpolation gives a stronger bound. Let a residual `R`
be nonnegative at both endpoints `a,b` of a grid cell of width `1/q`, and
let `||R''||_infinity <= M` on that cell. Its affine interpolant `J` is
nonnegative there. The interpolation remainder satisfies

$$
R(x)\ge J(x)-\frac M2(x-a)(b-x)
\ge-\frac{M}{8q^2}. \tag{10}
$$

For completeness, set
`H(x)=R(x)-J(x)+(M/2)(x-a)(b-x)`. Then `H''=R''-M<=0` and
`H(a)=H(b)=0`; concavity gives `H(x)>=0`. The quadratic
`R(x)=(M/2)(x-a)(x-b)` attains the deficit at the midpoint, proving
**cell-local sharpness**. This does not assert that this quadratic has a
globally C² periodic extension with the same derivative bound.

For the BBP residual, the periodic lift makes composition through the
modulo-one seam smooth. There is no seam delta term: the values and first
two derivatives of each potential match at the endpoints of its circle
chart. Differentiation gives the valid bound

$$
\|R_n''\|_\infty\le
4\pi^2+256\|V_{n+1}''\|_\infty+\|V_n''\|_\infty=:m_n.
$$

Apply (10) on the cell containing `z_n`. The rightmost term in (7) can
therefore be replaced by `sum_(n=A)^(B-1) m_n/(8q_n^2)`, using either
the reduced-forcing grids or the envelope grids, provided (1) is valid on
the grid being used. When both smoothness bounds are available one may
pay the smaller of the two justified deficits at each time.

With `C_A=max_(A<=n<=2A)||V_n''||_infinity`, monotonicity of the reduced
denominator sequence gives

$$
\frac{L_{A,2A}}A\le\frac{O_A}A+
\frac{4\pi^2+257C_A}{8q_A^2}. \tag{11}
$$

A certified normalized gain at least `eta>0` thus requires

$$
\boxed{C_A\ge
\frac{8q_A^2(\eta-O_A/A)-4\pi^2}{257}.} \tag{12}
$$

For sublinear endpoint oscillation this requires curvature of order at
least `q_A^2`. Fourier potentials obey
`||V_n''||_infinity <= 4 pi^2 sum_h h^2 |a_(n,h)|`; this second frequency
moment must therefore pay (12). The statement remains a necessary
condition for this explicit grid-certificate class, and supplies no
source-selected signed estimate by itself.

## 7. DC-06: exact positive and negative calibrations

The barrier is sharp at the endpoint-difference stage even in a system
whose selected trajectory plainly has positive escape. Restrict
`T(x)={16x}` to its two fixed points `D={0,1/3}`. The escape values are
exactly `g(0)=0`, `g(1/3)=3/2`. Set

$$
c_n=\frac32,\quad\epsilon_n=0,\quad
V_n(0)=-\frac32n,\quad V_n(1/3)=0.
$$

Then (1) is **equality at both states**. On the selected fixed trajectory
`x_n=1/3`, formula (2) certifies `3(B-A)/2`; on the coherent trajectory
it certifies zero. Moreover `Delta_n=3n/2`, so the first inequality of (4)
is equality. The linear endpoint separation is exactly what makes the
positive certificate possible.

These two values are restrictions of the Fourier polynomial
`V_n(x)=-n/2-n cos(2 pi x)`, with nonconstant coefficient mass `M_n=n`.
**The local equality is asserted only on the two-point domain.** It is
not asserted on the entire circle for this polynomial.

Two distinct controls calibrate the scope:

1. Set both potentials to zero while retaining positive `c_n`: (1) fails
   at the zero fixed point. The exact verifier rejects it.
2. Restrict the declared domain to `{1/3}`: zero potentials with
   `c_n=3/2` become valid. This does not violate DC-02 because its rival
   hypothesis has been removed. For BBP, an analogous restriction needs a
   source proof, not a manual omission of the unfavorable history.

The executable checks also verify constant-potential gauge invariance,
paid versus omitted errors, malformed domains and inexact-input rejection.
A separate exact four-pole calculation uses a **finite terminal tail**
`T_N=0` to check the coherent transport algebra. That finite tail is never
identified with the true infinite BBP tail.

## 8. Validation and next verdict-changing probe

Files: [finite verifier](dual_certificate_probe.py) and
[exact tests](test_dual_certificate_probe.py). From the repository root:

~~~sh
PYTHONPATH="$PWD" python -m unittest discover -s research/2026-11-12/boundary_filter_complexity -p 'test_dual_certificate_probe.py' -v
~~~

The initial ten-test run passed in 0.114 seconds, exit 0. The grid extension
adds exact sharp-Lipschitz-debt, source-grid closure, and malformed-budget
controls. **The resulting 13-test run passed** in 0.187 seconds, exit 0.
The reduced-forcing-grid corollary is checked by extending the existing
forward-closure test to both grid families. **All 13 tests passed again**
in 0.052 seconds, exit 0, after that extension.
The C² extension adds three exact tests for cell-local sharpness,
interpolation signs with nonzero endpoint data, and input rejection.
**All 16 tests passed** in 0.064 seconds, exit 0, after that extension.
These tests use one model family and shared source provenance; the graph
checker and algebraic proof are different checks, not independent referees.
The full repository gates are recorded by the integrating round separately.

The next concrete test is to take a proposed source filter inequality and
declare its state domain before optimizing it. Run the coherent history
through that domain and calculate its endpoint debt. A surviving certificate
must exhibit either (a) a proved zero-selected exclusion, or (b) sufficient
potential growth with a favorable authentic endpoint difference and a paid
measurement budget. A positive finite fitted example alone establishes
neither the source exclusion nor the all-shell asymptotic statement.
