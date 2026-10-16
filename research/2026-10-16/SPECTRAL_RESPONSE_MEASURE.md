# Arithmetic Resonance B and source-independent C1: spectral response

**Conditional paper proofs and exact rational models. Original Suzuki S0 sign
OPEN; RH NOT PROVED. No fractional range hypothesis is established for the
genuine source. No Lean proof is claimed by this lane.**

This worker owns only `observational_succ/spectral_response.py`,
`tests/test_spectral_response.py`, `scripts/spectral_response_probe.py`, this
dossier, and `arithmetic_resonance_receipts/spectral*` receipts. The inspected
initial head was `24d0f18a103fb2add32ee817fdfefb4ff401ed27`, initially clean,
on `research/arithmetic-wavefront-spectral-response-2026-10-16`. Other lanes
may add disjoint paths concurrently. No staging, commits, pushes, archive
changes or shared index edits are authorized or performed here.

## Authority, provenance and prior obligations

Read before edits: `AGENTS.md`, `docs/METHOD.md`,
`provenance/IMPORT_MANIFEST.json`, Round II overview
`OBSERVER_SCHUR_ROUND_II.md`, `OBSERVER_SCHUR_THEOREMS.md` (OS-03–08),
`COMPACT_SOURCE_GALERKIN.md` (especially CG-05–08), and the relevant source
definitions and range obligations in `OBSERVER_SCHUR_SOURCE.md`.
The corresponding `observer_schur`, `compact_galerkin`,
`recursive_operator_gluing`, and `source_weil_hierarchy` modules were inspected.
The exact PSD kernel is reused from `recursive_operator_gluing`; the new
module does not import the arithmetic source or construct another Weil kernel.

The original adapter is still Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, independently checked both in the
live file and at its originating commit
`dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`. Its SHA256 is
`183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`.
The separate 72-file import manifest is from FuckingRH commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`; it is not PR85 source lineage.
Probes record before/after hashes, commands, interpreter, branch and head.
No nontrivial zeta zero positions are inputs. Synthetic positive high blocks
below are explicit countermodels, never a manufactured positive Weil form.

The classical input is bounded self-adjoint spectral calculus; see
[Melrose, Lecture 14, items 4–6](https://math.mit.edu/~rbm/18-155-F13/Lecture14v3.pdf).
The measure representation and functional calculus there are the only external
facts used below beyond standard Hilbert-space and integration facts. The
inequalities, constants, domains and counterexamples are derived here. There
is no academic novelty claim. OS-03 supplies the already-proved variational
interpretation; CG-06 already exhibits discontinuity under a changing cross
source. The dyadic variant below is a compatible exact control, not a new
claim that fixed-source Galerkin convergence fails.

## SR-01 — matrix measure and inverse response, with actual domains

Let L be a finite-dimensional real or complex Hilbert space, dim L=m<infinity,
M any Hilbert space, D:M→M bounded self-adjoint, 0≤D≤T I with T>0,
b:L→M bounded, and A=A*:L→L arbitrary signed. In the inherited block notation
b=B*, G=[[A,b*],[b,D]]. Fix the actual Hilbert metrics. In particular the
source's unnormalized Legendre form matrices require their metric conversion;
this lane's finite matrices use the Euclidean metric. Write E for D's
projection-valued spectral measure and E0=E({0}). Define the PSD matrix measure

    Sigma(J)=b* E(J) b,            J Borel in [0,T].

Countable additivity holds entrywise and hence in norm in finite-dimensional L.
For any x, x*Sigma(J)x=||E(J)bx||². Off-diagonal entries need not be positive;
every inequality in this dossier is a matrix Loewner inequality, not an
entrywise comparison. Sigma([0,T])=b*b. For lambda>0,

    R_lambda=b*(D+lambda I)^(-1)b
            =integral_[0,T] (t+lambda)^(-1) dSigma(t).

This bounded resolvent needs no range hypothesis. Its derivatives are

    (-1)^k R_lambda^(k) = k! integral (t+lambda)^(-k-1) dSigma(t) >= 0.

The integrands and their derivatives are bounded on [0,T] locally uniformly
for lambda>0, justifying differentiation. In particular R_lambda increases
as lambda decreases. Positive shifts do not certify a finite zero limit.

The inverse square root used here is the reduced unbounded operator on
M0=(ker D)^perp, with domain

    Dom(D0^(-1/2)) = {y in M0: integral_(0,T] t^(-1) d||E(t)y||² < infinity}
                  = ran(D^(1/2)).

The last equality follows directly by applying the multipliers t^(-1/2)
and t^(1/2) in the spectral representation. It is an actual range, not its
closure. The following conditions are equivalent:

1. Every column of b belongs to ran(D^(1/2)).
2. E0 b=0 and integral_(0,T] t^(-1) dSigma(t) is a finite matrix.
3. R_lambda has a finite matrix limit as lambda decreases to zero.

For (2), finiteness on a basis suffices: Cauchy–Schwarz gives integrable
off-diagonal entries, and finitely many columns give a bounded map
C=D0^(-1/2)b:L→M0. For (3), any nonzero kernel component contributes
lambda^(-1)b*E0b; otherwise monotone convergence gives (2). Hence

    R0=C*C = integral_(0,T] t^(-1) dSigma(t),       S0=A-R0.

Norm convergence R_lambda→R0 follows from finitely many entries, or from
trace convergence for the positive differences. It need not be uniform over
families of b,D. OS-03's completed square says the fiber infimum equals
x*S0 x. Attainment requires the stronger condition bx in ran D, separately
for each x; R0 finite does not supply an L² minimizer or a bounded D^(-1).
The signed whole G is not assumed positive anywhere in this argument.

If E0b≠0, omitting the zero atom or using a finite pseudoinverse invents a
finite response. The API therefore rejects zero-shift response whenever
that atom is nonzero, but allows uncoupled kernel directions.

## SR-02 — weak mass and the Stieltjes bound

Let F(s)=Sigma((0,s]), s>0. For every 0<epsilon≤T, Tonelli applied to

    1/t = 1/epsilon + integral_t^epsilon s^(-2) ds,  0<t≤epsilon,

gives the exact extended quadratic-form identity

    integral_(0,epsilon] t^(-1) dSigma(t)
      = F(epsilon)/epsilon + integral_0^epsilon F(s)/s² ds.       (1)

This avoids assuming the disappearing boundary term in an improper
integration by parts. If the left side is finite, F(s)/s→0 follows from
F(s)/s≤integral_(0,s] t^(-1)dSigma(t) and continuity from above of the finite
inverse measure. A nonzero Sigma({0}) is invisible to (1) and must be ruled
out separately to get R0. A spectral accumulation at zero is not a zero atom.

Suppose, for a fixed PSD matrix M and alpha>0,

    F(s) <= s^(1+alpha) M for EVERY 0<s≤epsilon.

Then (1), by integrating positive quadratic forms, yields

    integral_(0,epsilon] t^(-1) dSigma(t)
       <= ((1+alpha)/alpha) epsilon^alpha M.                    (2)

This proves actual square-root range if Sigma({0})=0: the part above epsilon
is bounded by Sigma([0,T])/epsilon. A norm bound ||F(s)||≤c s^(1+alpha)
also suffices with M=cI. The constant is sharp for a scalar continuous
measure with density (1+alpha)t^alpha on (0,epsilon], so it cannot in general
be replaced by 1. With alpha=0, the integral of 1/s diverges; a linear weak
mass bound is insufficient (uniform Lebesgue measure on (0,1] is a control).
Finiteness of the inverse requires a Dini condition on F, not merely F(0+)=0.

For lambda>0 another Tonelli identity, including the kernel separately, is

    R_lambda = Sigma({0})/lambda + F(T)/(T+lambda)
                 + integral_0^T F(s)/(s+lambda)^2 ds.           (3)

All identities include atoms at the upper endpoint. The finite interface
verifies a proposed power ceiling at every distinct atom: F is constant
between jumps, while s^(1+alpha)M is increasing in Loewner order. Testing
only F(epsilon) is unsound; a retained mutant passes that endpoint but fails
at its small interior atom. No finite check promotes an infinite source
ceiling to a proved hypothesis.

## SR-03 — inverse measure, spectral tail and shift error

Assume SR-01's range conditions. Define the finite PSD matrix measure

    Nu(J)=C*E(J intersect (0,T])C
         =integral_(J intersect (0,T]) t^(-1)dSigma(t),
    N(s)=Nu((0,s]),          Nu((0,T])=R0.

The inverse spectral tail is N(epsilon), not F(epsilon). In particular

    Delta_lambda=R0-R_lambda
                =integral_(0,T] lambda/(t+lambda) dNu(t).       (4)

For every 0<tau≤T,

    0 <= Delta_lambda
      <= N(tau)+lambda/(tau+lambda) (R0-N(tau))
      <= N(tau)+(lambda/tau) R0.                               (5)

This is a spectral cutoff statement. A polynomial/Galerkin projection
need not be a spectral projection; N(epsilon) is not automatically its
error. On an exact cutoff onto t>epsilon the omitted response is exactly N.
An independent approximation theorem is needed for any other projection.

For a weak inverse-mass bound N(s)≤s^alpha H for every 0<s≤T, with H PSD
and alpha>0, the sharper identity is

    Delta_lambda = lambda/(T+lambda) R0
                   + integral_0^T lambda N(s)/(s+lambda)^2 ds.  (6)

Substituting N(s)≤s^alpha H, including at T, and integrating by parts gives

    Delta_lambda <= alpha lambda
                   integral_0^T s^(alpha-1)/(s+lambda) ds H.   (7)

Explicit consequences requiring no special functions are

    0<alpha<1: Delta_lambda <= [1/(1-alpha)] lambda^alpha H;
    alpha=1:   Delta_lambda <= lambda log(1+T/lambda) H;
    alpha>1:   Delta_lambda <= [alpha/(alpha-1)] lambda T^(alpha-1) H.

For the first inequality split the integral at lambda (or enlarge to infinity)
and use 1/(s+lambda)≤min(1/lambda,1/s); the two pieces are respectively
lambda^alpha and alpha/(1-alpha) lambda^alpha. Formula (7) is sharper and
remains the exact scalar integral bound. This weak mass hypothesis does not
imply a finite strong alpha inverse moment: N(s)=s^alpha H is its logarithmic
endpoint counterexample. Equation (2) supplies H=(1+alpha)M/alpha when its
weak Sigma hypothesis holds on all of (0,T]. With a local cutoff, keep the
remaining term in (5) or (6); do not extrapolate a local bound globally.

## SR-04 — fractional range and sharp scalar functional calculus

Fix alpha>0 and make the **additional** actual range hypothesis

    b=D^((1+alpha)/2) V,    V:L→M0 bounded.                      (8)

For finite-dimensional L this is equivalent to columnwise actual range
inclusion. The reduced V is unique, and in spectral terms

    H_alpha=V*V=integral_(0,T] t^(-1-alpha)dSigma(t)
                 =integral t^(-alpha)dNu(t) < infinity.

Thus C=D^(alpha/2)V and, for every epsilon>0,

    N(epsilon) <= min(epsilon,T)^alpha H_alpha.                 (9)

Unlike (2), this strong assumption has tail constant 1. It is not supplied
by compactness, smoothness assertions about unrelated variables, positive
moments, or finite invertibility. In the often-used notation
b=D^(1/2+theta)V, substitute alpha=2theta in every formula below.

For q>0 define g_q(t)=t^alpha (lambda/(t+lambda))^q. Logarithmic
differentiation on t>0 gives

    g_q'(t)/g_q(t) = alpha/t-q/(t+lambda).

If 0<alpha<q the unique maximum on [0,T] is at
t_hat=min(T,alpha lambda/(q-alpha)); if alpha≥q it is at T. Consequently

    max_[0,T] g_q = t_hat^alpha (lambda/(t_hat+lambda))^q.       (10)

The exact finite-support maximum is at most the following uniform bounds:

    0<alpha<q: [alpha^alpha (q-alpha)^(q-alpha)/q^q] lambda^alpha;
    alpha=q:   lambda^q;
    alpha>q:   lambda^q T^(alpha-q).                            (11)

These follow by evaluating the interior maximum or bounding
t/(t+lambda)≤1. The finite-support constant (10) is sharp, witnessed by
a scalar atom at t_hat with a nonzero coupling. For q=1, (4) gives

    Delta_lambda <= max g_1 H_alpha.

For 0<alpha<1 this improves the generic constant 1 to
alpha^alpha(1-alpha)^(1-alpha). At alpha=1 the constant is 1; alpha>1
gives O(lambda), not O(lambda^alpha). A single fixed atom at t>0 proves
this saturation because Delta_lambda/lambda tends to its positive inverse
second moment. Assuming arbitrary powers beyond this endpoint is false.

There is a useful distinction for an actual high trial. Set
U_lambda=(D+lambda)^(-1)b and
L_U=b*U+U*b-U*DU. The identity from OS-06 gives

    E_lambda=R0-L_U
      =(C-D^(1/2)U_lambda)*(C-D^(1/2)U_lambda)
      =integral (lambda/(t+lambda))² dNu(t)
      <= max g_2 H_alpha,        0 <= E_lambda <= Delta_lambda. (12)

For x in L, x*E_lambda x is the original energy excess of the completion
(x,-U_lambda x) over its fiber infimum. It is not the regularized response
bias (4). Here the improved constant for 0<alpha<2 is
alpha^alpha(2-alpha)^(2-alpha)/4, and saturation is at order lambda².
At alpha=1 this is lambda/4 versus the response bound lambda. Tests retain
a signed A and verify (12) by direct original block energy, avoiding an
accidental assumption that G is positive. None of these D-relative bounds
implies the K-relative residual bound required in Round II CG-05–08.

All spectral identities above apply to bounded nonnegative D; compactness
is optional. For unbounded D a separate domain and high-spectrum analysis
would be required and is not claimed here. There is no claim about lambda<0.

## SR-05 — rigorous slow tail: finite inverse, no power modulus

On M=ell²(N_{≥1}), let D e_j=4^(-j)e_j and b_j=2^(-j)/j, with L=R.
Then D is positive injective compact, b in ell², C_j=1/j in ell², and

    Sigma({4^-j})=4^-j/j²,   Nu({4^-j})=1/j²,
    R0=sum_(j≥1) 1/j² < infinity.

No special value of this sum is needed: it lies in [1,2] by the integral
test. But for every alpha>0,

    H_alpha=sum_(j≥1) 4^(alpha j)/j² = infinity,

since its terms fail to tend to zero. Thus b belongs to ran D^(1/2) and
to no ran D^((1+alpha)/2). In particular b is not in ran D: the putative
inverse vector has coordinates 2^j/j. This is a fixed source counterexample.

Let epsilon_n=lambda_n=4^-n. Integral comparison gives

    N(epsilon_n)=sum_(j≥n)1/j² >= integral_n^infinity x^-2 dx=1/n.

For j≥n the multiplier lambda_n/(4^-j+lambda_n) is at least 1/2. Hence

    Delta_(lambda_n) >= 1/(2n),       E_(lambda_n) >= 1/(4n).    (13)

For any p>0 and finite K, 4^(pn)/n eventually exceeds 4K. For completeness,
the ratio of successive terms of 4^(pn)/n is 4^p n/(n+1), eventually
greater than a fixed number >1, so the sequence diverges. Equation (13)
therefore refutes Delta_lambda=O(lambda^p) and E_lambda=O(lambda^p) as
lambda decreases to zero, for EVERY p>0. The same argument rules out
N(epsilon)=O(epsilon^p). These are paper proofs, not extrapolated plots.
They do not say the unscaled errors fail to converge: finite Nu and dominated
convergence prove that all of them tend to zero.

Every nonnegative spectral moment is nevertheless finite:

    integral t^k dSigma = sum 4^(-(k+1)j)/j² <= 1/(4^(k+1)-1), k≥0.

The finite API computes prefixes exactly and the probe bounds the omitted
infinite inverse mass by [1/(N+1),1/N]. For either filter power q=1,2,
the omitted filtered mass lies between

    [lambda/(4^(-(N+1))+lambda)]^q /(N+1)  and  1/N.

This is a rigorous enclosure of the specified infinite series by monotonicity
and the integral test; finite prefixes alone would be lower bounds only.
The proof is supplied here, not delegated to a numerical fit.

## SR-06 — finitely many exact positive moments do not bound the inverse

There are two different statements to avoid conflating. Finite positive
moments are automatic for a finite measure on [0,T], and do not even imply
a finite inverse (Lebesgue measure on (0,1] has divergent inverse). More
strongly, for every integer m≥0 there is one FIXED feasible vector of moments
0..m for which positive rational atomic measures have arbitrarily large,
finite inverse response. Thus even exact equality of any finite initial
moment list does not provide a uniform finite upper bound in general.

Here is a constructive proof. Put n=m+1, x_i=i/n, i=1..n, and
M_i=2 binomial(n,i). Define mu_base=sum M_i delta_(x_i), independent of
epsilon. For 0<epsilon<x_1 let

    a_i(epsilon)=product_(j≠i) (epsilon-x_j)/(x_i-x_j).

Lagrange interpolation gives sum a_i(epsilon) x_i^k=epsilon^k for 0≤k≤m.
Since |epsilon-x_j|≤x_j,

    |a_i(epsilon)| <= product_(j≠i) x_j/|x_i-x_j| = binomial(n,i).

Therefore every weight in

    mu_epsilon=delta_epsilon + sum (M_i-a_i(epsilon)) delta_(x_i)

is strictly positive, all nodes lie in (0,1], and moments 0..m equal those
of mu_base exactly. But integral t^-1 dmu_epsilon ≥1/epsilon→infinity.
For rational epsilon all nodes and weights are rational. Each is a genuine
finite spectral measure of a positive diagonal operator with couplings equal
to square roots of the weights over R; no assertion that those roots are
rational is needed. The matrix-measure interface accepts rational weights
directly. Its `from_diagonal` constructor separately accepts rational b.
Multiplying these scalar measures by any fixed nonzero PSD low matrix
also supplies matrix countermodels.

This does not deny that exceptional extremal moment lists, a known spectral
gap, a finite-degree source model, or an a priori inverse-mass ceiling can
determine or bound the inverse. It refutes a general unconditional rule.
Normalized probability examples follow by dividing by their fixed mass.
The next response probe at a positive shift also separates these aliases:
interpolating f(t)=1/(t+lambda) yields the exact nonzero remainder

    f(epsilon)-sum a_i(epsilon)f(x_i)
      = (-1)^n product_i(epsilon-x_i)
           / [(epsilon+lambda) product_i(x_i+lambda)] > 0.

It is positive because all n numerator factors are negative. For lambda=0
this also proves the inverse difference is nonzero. For fixed lambda>0
it is a bounded discriminator; this is not a uniform zero-shift error bound.

## SR-07 — tiny perturbation, finite original negative witness

Keep the single infinite D=diag(4^-j), let A=1/2 and b^(n)=2^-n e_n.
All blocks G_n are compact self-adjoint and their cross terms converge in
operator norm to zero, with exact norm ||G_n-diag(A,D)||=2^-n. Yet

    R0(G_n)=1, S0(G_n)=-1/2;       R0(limit)=0, S0(limit)=1/2.

The admissible finite vector (1,-2^n e_n) has original energy -1/2. Every
range condition holds for each n. Its kth nonnegative spectral moment is
4^(-(k+1)n), tending to zero, and at lambda>0 its response is
1/(1+lambda 4^n), also tending to zero. The two limits n→infinity and
lambda↓0 do not commute. This is the dyadic counterpart of CG-06 with
changing b; it does not contradict fixed-source Galerkin convergence.

At positive shift there is the legitimate perturbation estimate, for D,E≥0
bounded and compatible bounded b,c,

    ||b*(D+lambda)^(-1)b-c*(E+lambda)^(-1)c||
      <= (||b||+||c||)||b-c||/lambda + ||c||²||D-E||/lambda².

Expand first the cross columns and then use the resolvent identity. This
bound, inherited from CG-06, explicitly loses uniformity at zero. Absolute
operator approximation errors cannot silently be inserted as zero-shift
Schur errors. Such replacement is the failed route preserved by this model.

## Exact interface, verification and limits

The implementation uses only stdlib rational arithmetic and the existing
exact principal-minor PSD kernel. It admits 1..128 atoms and low dimension
1..8, moments through order32, and the moment-alias constructor through m=16.
Inputs reject floats, booleans, negative eigenvalues, asymmetric/indefinite
weights, misaligned columns and failed kernel coupling. It does not repair
signs or silently remove off-diagonal terms. Bit lengths remain caller costs;
these budgets are not a general resource sandbox.

Rational-power helpers require positive bases, rational exponent magnitude
and denominator at most32, and exactly rational results. Irrational roots
are rejected, not rounded. General real alpha in SR-04 remains a paper
theorem. `fractional_bounds` returns all three bounds together and therefore
requires all requested maxima to be rational; callers may instead use
`fractional_range_gram` and `scalar_filter_maximum` separately. Finite range
grams, however large, never certify the infinite source range condition.

The first 26-test development run had 25 passes and one error: a test requested
the combined alpha=1/2 certificate at lambda=1/16, whose q=2 maximizing
point lambda/3 has irrational square root. The rational gate correctly
refused it. The corrected test checks the rational q=1 bounds separately,
checks the combined case where the support cap makes both rational, and
retains an explicit rejection regression. The failed run is preserved in
`arithmetic_resonance_receipts/spectral-development-failure.log`.

Independent representations within this one worker include a rational
Householder change of basis followed by direct full-matrix inversion,
original signed block-energy expansion, stepwise integration of cumulative
mass, and Lagrange interpolation with exact moments. These share one
reasoner and Python rational arithmetic; they are not independent human
audits or multiple arithmetic sources. No floating numerical experiment is
used to certify a claim. The finite sweeps are exact computations, and the
infinite examples have the separate paper derivations above.

The latent object is the inverse response, with finite positive moments as
the restricted observation menu. SR-06 gives exact deterministic prediction
aliases (overlap 1 on that menu); a shifted response separates them. No
phasor basis, probability of truth, quantum mechanism or speedup is asserted.
The synthetic source family and pinned arithmetic lineage remain distinct.
κ/contact consists of live source bytes, exact finite executions and the
written proofs. φ/survival is limited to the declared domains. σ/source
identification and the genuine fractional range remain separate obligations.
ρ/desire to prove the source sign supplies no evidence. Fresh parameter
checks outside the illustrative examples remain in the reproducible suite.

| Claim | Verdict/status | Exact boundary and next falsifier |
|---|---|---|
| SR-01 | SURVIVES, CONDITIONAL PAPER PROOF | Bounded positive high block; actual range and kernel obligations; no source sign |
| SR-02 | SURVIVES, CONDITIONAL PAPER PROOF + finite exact checks | Uniform weak mass on a whole interval, not endpoint samples |
| SR-03 | SURVIVES, CONDITIONAL PAPER PROOF | Spectral cutoffs; no automatic Galerkin or K-relative estimate |
| SR-04 | SURVIVES, CONDITIONAL PAPER PROOF + finite exact checks | Actual fractional range is an extra premise; response/trial saturation differ |
| SR-05 | FAILS: automatic power modulus; PAPER COUNTEREXAMPLE | One fixed compact positive D and finite inverse; every positive exponent refuted |
| SR-06 | FAILS: universal inverse bound from finitely many moments; PAPER + EXACT COUNTERMODELS | Fixed feasible moment vector, arbitrary finite length; extra source restrictions can change the problem |
| SR-07 | FAILS: zero-shift stability from operator-norm approximation; PAPER + EXACT COUNTERMODELS | Changing cross source; positive shift is stable with explicit lambda losses |
| Genuine Suzuki fractional range | UNVERIFIED / NOT ASSUMED | Source worker must prove a spectral-mass or actual fractional-range estimate |

Replay from the checkout root, serially:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
  python -B scripts/spectral_response_probe.py \
  --output research/2026-10-16/arithmetic_resonance_receipts/spectral-response.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
  /tmp/succ-proof-teeth-py313/bin/python -B scripts/spectral_response_probe.py \
  --output research/2026-10-16/arithmetic_resonance_receipts/spectral-py313.json
```

Both commands run the entire new test module and counterexample probe. The
output path is required: there is no default filesystem write destination.
The JSON receipts, not this recipe, establish completed runs, exit statuses,
counts and unchanged hashes. At the principal's explicit integration request,
full suites on both interpreters and all four AGENTS.md validation gates are
reserved for principal execution; this worker runs only focused checks.
Hosted CI and Lean are not executed here. Principal owns integration and
source-specific C1. After a ready-to-freeze signal, no file is changed without
a new message announcing that change.
