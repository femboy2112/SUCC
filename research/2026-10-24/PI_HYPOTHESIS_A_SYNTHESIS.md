# Hypothesis A, all observers together, and the remaining BBP theorem

**Date:** 2026-10-24. **Branch:**
`research/pi-hypothesis-a-joint-observers-2026-10-24`.
**Parent:** Pascal/Lucas draft #274 at
`d942c4707d750f788f39acb137a04e871a93e0a6`.
**Authority:** elementary paper proofs, explicitly named classical results,
exact finite certificates and same-model proof audits. No new Lean authority
or independent external refereeing is claimed. **Pi normality remains OPEN.**

## 1. The outcome

The user's suggestion is correct at the level that matters: **the joint
observer law contains information absent from every separate marginal.**
This round makes that statement constructive, proves a weaker collision
criterion that can discard a vanishing exceptional set, and proves an
alternative all-gain classification requiring no positive-entropy premise.
It also shows exactly how all fixed local observations can be asymptotically
correct while a changed source has arbitrary real statistics.

There is no unique syntactic "weakest sufficient hypothesis": many
equivalent criteria exist. The useful choices are now explicit:

1. **Classical upper-only blocks.** It is enough that no long word appears
   more than a subexponential factor too often, along unbounded word lengths.
   Exact one-sixteenth equalities need not be assumed.
2. **New trimmed collision extension.** Discard a vanishing fraction of
   selected positions and control the full remaining real-cell collision
   excess. The authentic BBP tail costs at most a factor two.
3. **All gains plus origin escape.** Preserve the selected occupation law
   under the average of all integer gains, in the stated order of limits,
   and prevent concentration at zero. An elementary classification then
   forces Haar measure.

The qualitative versions are equivalent to normality when applied to this
one source. They become research progress only when a separate arithmetic
argument bounds one of their terms. This round proves bridges, improves
the collision premise, supplies stronger falsifiers, and sharpens source
authentication. It does not supply that last BBP statistical estimate.

Full dossiers:

- [Joint conditional interactions and trimmed entropy](PI_TRIMMED_JOINT_ENTROPY.md).
- [All-gain classification and finite Fourier certificate](PI_ALL_GAIN_RIGIDITY.md).
- [All-length Pascal rank countermodel](PI_ALL_RANK_OBSERVERS.md).
- [Joint primary carriers and moving-prime source controls](PI_JOINT_PRIMARY_OBSERVERS.md).
- [Positive rational-source authentication theorem](PI_RATIONAL_SOURCE_AUTHENTICATION.md).
- [Late joint-prime update and adelic compactness boundary](PI_JOINT_ADELIC_COMPACTNESS.md).
- [Validation and authority](PI_HYPOTHESIS_A_VALIDATION.md).

## 2. The updated repository frontier

The local checkout was clean at #273. Three subsequent drafts were inspected
at their actual commits before the new contract and code were written.

| Draft | Pinned head | What it establishes | Statistical boundary |
|---|---|---|---|
| #274, inherited parent | `d942c4707d750f788f39acb137a04e871a93e0a6` | Exact Lucas incidence, Pascal rank quotient, ternary coding, positional kernel and carry-information obstruction | Rank or support counts do not identify the selected joint carry law |
| #275, inspected sibling | `7c5d5b8856a1d132fb941ae40c946c0565918b36` | Positive prime charts, coherent dyadic transport, sharp source errors, denominator-three multiplier 81 | Constructing another-base readout does not preserve the original empirical law |
| #276, inspected sibling | `8c94abd984ff99ad32a38ef2415c1e5cabf08d05` | Pascal-Tauber bridge, signed integer tripling stencil and exact prime-chart composition defect | Small deterministic source correction does not bound the main selected Fourier mean |
| #277, inspected after this round's code freeze | `e9ad0fc3479c8182d19046831006c423ea68ee85` | Four distinct forcing-pole classes at every prime p>=7, exact finite-family CRT activation laws, exceptional 3/5 cancellation and an adelic source-extension obstruction | Instantaneous forcing activation is not independence of the propagated carrier phases |

The #275/#276 implementations are not silently merged. Their statements are
used only with these provenance pins. The inherited #273 projectors,
selection-depth theorem, history-preservation limits and finite-prime
correlation controls remain in force. Original imported archives are unchanged.

Draft #277 is likewise inspected, not merged. Its rational numerator identity
and dyadic isometry already occur in the inherited source-isometry dossier;
its all-prime reassembly and mixed-covariance identities overlap the algebra
proved here. No priority claim is made for these overlaps. The additional
four-pole residue constraints are useful new arithmetic input. The linked
adelic note derives density-zero compact occupation from those constraints.
A stronger elementary proof shows that the authentic forcing eventually
leaves every compact subset of the finite adeles; inherited denominator
growth gives the same conclusion for the states. Neither occupation family
has a weak probability limit there. This constrains an attempted compact
all-local limit, not the compact real-circle law used for normality.
The standard finite-adelic circle character remains continuous; the weaker
primary-product topology and profinite-time source extension are different maps.

## 3. What Bailey--Crandall Hypothesis A actually says

In its original form, choose any integer b>=2 and proper rational function
`R(n)=P(n)/Q(n)`, with integer polynomials and no positive-integer pole.
Starting from zero, define

$$
x_n=\{b x_{n-1}+R(n)\}.
$$

Hypothesis A says that this selected trajectory either has a finite attractor
or is uniformly distributed. The finite-attractor/rational-sum equivalence
is proved in Bailey--Crandall, Theorem 3.1; the dichotomy itself is their
hypothesis. See [BC1], original statement and Theorems 1.1 and 3.1.

For this project, the authentic recurrence is already fixed:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad y_n=\{U_n\}.
$$

The sum is pi/16, which is irrational. Therefore the single-source version
of Hypothesis A simply says that the y_n orbit is uniform; it is equivalent
to the desired base-16 normality. Removing the universal forcing quantifier
is sensible, but does not by itself prove a new arithmetic statement.

Lagarias explicitly distinguishes a **Weak Dichotomy**, finite limit set or
dense orbit, from the **Strong Dichotomy**, finite limit set or uniform orbit.
The former gives occurrence of every finite word, not correct frequencies.
His orbit-shadowing theorem works for perturbations tending to zero that
can encode arbitrary real numbers. His G-function and simple-pole results
give arithmetic/transcendence restrictions, not frequency estimates. [L]

An especially important weakening trap: an irrational orbit can have an
atomic occupation limit without a finite trajectory attractor. The number
`sum_(m>=1)16^(-m^2)` is irrational but has nonzero digits of density zero,
so its occupation law tends to a point mass at zero. Irrationality cannot
remove the atomic branch of an invented "atomic or Haar occupation" dichotomy.

The later Bailey--Crandall paper proves normality for carefully synchronized
sparse constructions. It also describes the unsolved difficulty with the
continually changing generators and amplified tails of the original
constants. Those positive examples are useful controls, not a theorem for
this four-pole source. [BC2]

## 4. The weakest useful classical statistical target found here

Let `F_N(w)` be the frequency of a length-k base-16 word among N consecutive
starting positions. The strong Piatetski--Shapiro criterion permits

$$
\limsup_{N\to\infty}F_N(w)\le c_j16^{-k_j}
\quad\text{for every word of length }k_j,
$$

where `k_j -> infinity` and

$$
\frac{\log c_j}{k_j}\longrightarrow0.
$$

Only unbounded lengths are needed. Neither a polynomial rate in N nor a
lower frequency bound for each word is assumed. Constants, polynomials
in k, and `exp(sqrt(k))` are examples of permitted excess factors.
Kozachinskiy--Shen state and prove this classical strong version and its
subsequence refinement in Section 4.2. [KS]

The quantifiers are essential: fix a word length, then control all sufficiently
large horizons. A pleasant finite table, or one favorable horizon per length,
is insufficient. Normality itself implies the criterion, so it must be
described as an equivalent criterion at the qualitative level.

The elementary entropy mechanism is transparent. If every depth-d cell has
probability at most `c_d16^(-d)`, its block entropy is at least
`d log16-log c_d`. A nonuniform fixed short-block law has a positive entropy
deficit which repeats across longer blocks. Subexponential total deficit
cannot sustain that positive loss per digit.

## 5. The proved improvement: trim rare hotspots and retain all joint information

Let G_N be retained positions among `1,...,N`, with discarded fraction
`delta_N=1-|G_N|/N`. At depth d, use the actual source cells

$$
q_{N,d}(j)=\frac1{|G_N|}
\#\{n\in G_N:\lfloor16^d y_n\rfloor=j\},\qquad
C_{N,d}=16^d\sum_jq_{N,d}(j)^2.
$$

An explicit sufficient target is

$$
\boxed{d_N\to\infty,\qquad\delta_N\to0,\qquad
\frac{\log C_{N,d_N}}{d_N}\to0.}
$$

At unspecified source-adapted depths this too is an equivalent criterion;
fixing a depth schedule before measuring creates a stronger, testable
quantitative target. The inherited `d=floor((2/5)log_16 N)` is one possible
schedule, not a theorem obtained from the finite measurements below.
The source-selected estimate is OPEN.

### Why the BBP tail can now be paid explicitly

The authentic positive tail gives

$$
\{16^n\pi/16\}=y_n+T_n\pmod1,
\qquad0<T_n<[(8n+1)(8n+2)]^{-1}.
$$

When `(8n+1)(8n+2)>=16^d`, mass in a source cell stays there or moves to
the next cell. Write its split as `q_j=a_j+b_j`; the true mass is
`p_j=a_j+b_(j-1)`. Then

$$
\sum_jp_j^2\le2\sum_j(a_j^2+b_j^2)\le2\sum_jq_j^2.
$$

Thus true collision excess is at most **twice** source collision excess.
The factor is sharp and its logarithm is harmless at growing depth. The
mandatory unsafe prefix has length `O(16^(d/2))`. Since the collision
diagonal gives `C>=16^d/N`, the proposed bound forces
`d<=(1+o(1))log_16 N`; consequently that prefix is `N^(1/2+o(1))=o(N)`.
Discarding it and renormalizing changes the logarithmic collision budget
by o(1). This removes an unproved carry-boundary count from this route.

### Why rare exceptions can matter

The finite law `(1-1/d)uniform+(1/d)delta_(0^d)` loses only O(1/d) entropy
per digit after trimming, but its untrimmed collision excess is
`1+(16^d-1)/d^2`, exponentially large in d. The extension therefore permits
exceptional concentrations that the old raw L2 premise would reject.
This finite-law separation is not a claim that every such family is the
block law of one consistent infinite source.

For the full original N-window and fixed short length k, the proved bound is

$$
D(p_{N,k}\Vert u_{16^k})\le
\frac{\delta d\log16+(1-\delta)\log C_G}{\lfloor d/k\rfloor}
+h_2(d/N)+(d/N)\log(16^k-1).
$$

The arbitrary subset G is never declared stationary. Entropy subadditivity
and the endpoint-shift estimate are applied to the original full window.

### What "all observers together" means in the bound

For a complete joint history law P and a coherent reference law R, put

$$
M_k=\sum_v\frac{P_k(v)^2}{R_k(v)},\qquad
\zeta_k(v)=\frac{P_k(v)^2}{R_k(v)M_k}.
$$

The exact factorization proved in this round is

$$
\boxed{\frac{M_{k+1}}{M_k}
=1+\mathbb E_{\zeta_k}
\chi^2(P(\cdot\mid v)\Vert R(\cdot\mid v)).}
$$

R can be correlated. The actual history v stays in each conditional law;
separate marginal uniformity cannot substitute for it. A valid common
decoder to carries decreases this second moment. Bounding these conditioned
defects using the exact four-pole source is a concrete remaining arithmetic
task. Choosing R so that its carry law is uniform without proving that
property would hide the target in the reference measure.

## 6. An infinite countermodel that isolates positional information

Use independent four-bit blocks with

$$
P_t(x)=\frac1{16}[1+t(\chi_{124}(x)-\chi_{134}(x))],\qquad |t|\le1/2,
$$

and randomize the four block alignments. An explicit skew-shift proof shows
that the resulting process is stationary and ergodic. Every contiguous
window of every length has exactly the fair binomial distribution for its
number of ones. Every pair of bits is independent, and contiguous words
through length three have fair frequencies.

Nevertheless, at t=1/4,

$$
\Pr(0010)=9/128,\qquad\Pr(0100)=7/128,
$$

rather than `1/16=8/128`. Opposite signed positional triple correlations
`+1/16` and `-1/16` cancel under rank symmetrization. A finite symbol map
from a normal base-32 sequence supplies a computable deterministic example.

This strengthens the finite rank-quotient obstruction in #274. It does not
refute a genuinely joint proposal: the full joint sequence of prefix ranks
recovers bits by subtraction. It refutes the inference that collecting all
separate rank distributions supplies that joint sequence.

## 7. All primary clocks: exact recovery, real instability and a sharp source control

On a known denominator carrier D, observing a prime family leaves a residual
fiber of R equally spaced circle points. The optimal worst-case real
reconstruction radius is `(R-1)/(2R)`, at least `1/4` whenever R>1. Knowing
almost all prime coordinates does not force a small real error uniformly.

Conversely demanding a full-carrier uniform law is much too strong. N
sampled states have support at most N, so their total variation from uniform
on D points is at least `1-N/D`, and their scaled collision is at least
`D/N`. The authentic carrier grows exponentially. Real coarse cells and
specific mixed characters are the appropriate resolution for a frequency
argument; microscopic full-carrier independence is not a viable premise.

The new source-matching construction goes further than fixed finite prime
controls. For any prescribed real constant C it constructs rational H_n
such that:

- At time n, its state and forcing match every authentic primary component
  at every prime `p<=8n`.
- For every fixed prime, the full p-adic differences from the authentic
  state and forcing tend to zero. Every fixed finite local Pascal jet also
  agrees asymptotically; fixed dyadic valuation orders eventually match.
- Denominator logarithmic heights retain the same leading upper/lower
  bounds as the authentic source.
- Its real occupation statistics are those of `{16^n C}`.

The construction adds a prime greater than `16n`, with subexponential
additional denominator cost. This **violates the exact authentic conductor
and fixed four-pole rational-function identity**. It is not a counterexample
to Hypothesis A or pi normality. A paper variant using a truncated authentic
Green tail makes the real forcing difference smaller than every power of
1/n, while retaining the same exclusions. The executable controls test the
simpler explicit quadratic-tail variant.

This is the precise limit-order failure: every fixed observer may eventually
agree, while a moving unobserved place carries the real discrepancy. It
does not justify saying that complete exact primary data at a fixed time
are insufficient to identify that time's rational phase.

### A positive rigidity theorem restores the exact source class

Inside proper rational **functions**, that escape is impossible. If two
such forcings differ, choose an integer a where their difference has real
absolute value strictly between zero and one. A prime in its reduced
denominator has negative valuation. Polynomial congruence preserves that
valuation on a fixed arithmetic progression. Thus one fixed prime detects
the difference at positive density.

Therefore, if every prime's **time-aligned** forcing disagreement has density
zero, two proper rational forcings must coincide exactly. Full absolute
p-adic convergence of their difference to zero at even one prime also
forces identity by continuity. This proves a strong source-identification
consequence of joint local agreement; it does not yet bound the unique
source's real carry frequencies.

## 8. The alternate all-gain route

For any circle probability define

$$
A_Q\mu=\frac1Q\sum_{q=1}^Q(T_q)_*\mu,\qquad T_q(x)=qx\pmod1.
$$

The weak limit exists for every mu: irrational points average to Haar and
rational points average over their complete finite torsion grids. Comparing
the resulting mass at zero proves

$$
R\mu=\mu\quad\Longleftrightarrow\quad
\mu=c\delta_0+(1-c)\lambda.
$$

Consequently these two actual-source estimates would suffice:

$$
\lim_{Q\to\infty}\limsup_{N\to\infty}W_1(A_Q\mu_N,\mu_N)=0,
$$

$$
\lim_{\rho\downarrow0}\limsup_{N\to\infty}\mu_N(B(0,\rho))=0.
$$

This needs no positive-entropy estimate, but preservation of the full gain
average is unproved. Prime multiplication gains and p-primary projections
are distinct maps. Exact prime charts do not identify their law-preservation
defects. The nested limit fixes Q first; an arbitrary diagonal is not claimed.

The finite certificate is also explicit. Given valid bounds C_q for
`W1(T_q mu,mu)`, for h nonzero,

$$
|\widehat\mu(h)|\le\mu(B(0,\rho))+\frac1{2Q\rho}
+2\pi\left(C_{|h|}+\frac1Q\sum_{q=1}^QC_q\right).
$$

Prime bounds propagate by `C_(ab)<=C_a+a C_b`. The implementation computes
actual rational W1 certificates, accounts for every prime divisor, and uses
a rational upper bound for pi. All integer readouts themselves are already
exact from the source stencil
`y_(n+1)+(q-16)y_n-r(n+1)=q y_n mod1`.

## 9. Finite measurements and their limits

All twelve registered gain-preservation rows are retained. Values below are
certified lower endpoints of intervals of width `10^-8`.

| Source prefix N | Q=2 | Q=4 | Q=8 |
|---:|---:|---:|---:|
| 32 | 0.02142899 | 0.04355696 | 0.04153308 |
| 64 | 0.02239241 | 0.02706882 | 0.02718374 |
| 128 | 0.00739759 | 0.01146816 | 0.01236686 |
| 256 | 0.01294302 | 0.01106944 | 0.01158782 |

Neither horizon nor gain depth is monotone. The finite Fourier bound is
trivial at three of the four registered source horizons, and only slightly
below one at N=128. No rate is fitted and no asymptotic premise is inferred.
Independent Machin enclosures also certify 345 true source-cell comparisons;
these calibrate the factor-two transfer, not an infinite collision bound.

## 10. Differential agreement and the proposed path average

The useful distinction is between equality of states and equality after an
observation. In an additive faithful state space, `u=u+w` implies `w=0`.
For an observer O, `O(u)=O(u+w)` instead says that w lies in the observer's
kernel. Intersecting kernels of a separating observer family can remove the
ambiguity. For complete primary observations of rational states it determines
the circle phase; a separate integer-lift condition determines the whole state.
The fixed forcing and initial state already determine the authentic U_n uniquely.

What remains is a time average over that unique state history. Source-consistent
observer agreement does not automatically force its unobserved signed
correlations to vanish. The full conditional collision chain above is one exact
way to retain the interactions that a differential or rank quotient can lose.

A coherent signed sum over observer histories may project onto the common
constraint space. To prove normality, one must additionally identify the
projected measure with the empirical law of the authentic selected history.
The all-gain theorem makes this issue concrete: averaging q*x for a single
irrational x already gives Haar, even when the base-16 orbit of x is a
sparse-digit nonnormal orbit. The observer average's uniformity does not
identify that orbit's time distribution. Condition (P) is the missing equality
between the two measures, expressed in a metric and with a fixed order of limits.

Thus the path-integral intuition suggests an operator and a cancellation
identity to seek, but it does not supply a source-derived amplitude, phase,
or law-preservation estimate. The exact BBP identity must enter the proof of
that estimate, rather than appearing only as the label on the selected path.

## 11. The next theorem to prove

The direct counting target is a **source-derived subexponential bound on
retained real carry collisions**, with an explicitly vanishing discarded
mass and the full joint conditional interactions retained. This avoids
assuming exact one-sixteenth branch probabilities and avoids needing a
second multiplication symmetry. The all-gain preservation/origin-escape
pair supplies a separate route with different obligations.

The exact four-pole identity and conductor are the important arithmetic
inputs. All fixed p-adic and real asymptotic observations, even together,
can be spoofed by a changed nonrational forcing. Within the exact rational
class, local agreement does authenticate the source. A new temporal estimate
must now exploit that class restriction; uniqueness alone is not the estimate.

No independence result for pi normality in a foundational theory has been
proved or needed here. The problem is an open source-specific arithmetic
lemma, not an identified need for a new axiom.

## Primary references

- **[BC1]** David H. Bailey and Richard E. Crandall, *On the Random Character
  of Fundamental Constant Expansions*, 2000 manuscript / Experimental
  Mathematics 2001. [Author PDF](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf).
- **[L]** Jeffrey C. Lagarias, *On the Normality of Arithmetical Constants*,
  [arXiv math/0101055](https://arxiv.org/pdf/math/0101055), especially
  Theorems 3.1, 4.1, 5.2--5.3 and Sections 4 and 6.
- **[KS]** Alexander Kozachinskiy and Alexander Shen, *Automatic Kolmogorov
  complexity, normality and finite-state dimension revisited*,
  [arXiv:1701.09060v6](https://kozmath.github.io/papers/1701.09060.pdf),
  Section 4.2, Theorem 3 and following remark; Section 4.3 for the classical
  computable normal input used by the rank countermodel.
- **[BC2]** Bailey and Crandall, *Random Generators and Normal Numbers*,
  [author manuscript](https://www.davidhbailey.com/dhbpapers/bcnormal.pdf),
  especially the cascaded-generator discussion and stated positive examples.
