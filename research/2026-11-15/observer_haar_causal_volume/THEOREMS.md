# Adaptive observation, Haar information, causal volumes, and quantum controls

**Status.** Mathematical proofs in the stated models, supported by exact finite
implementations and hostile controls. These are not a physical measurement of
BBP, a Lean certificate, or a new general theorem of quantum gravity. Classical
Bayesian, Haar, operator, and quantum results are credited in `PROVENANCE.md`.

## AH-01. A chosen frame and a stochastic probe are different objects

Fix a finite source state space X, an admissible action set A, an outcome
alphabet Y, and the source-labelled joint instrument

\[
J_a(x,x',y)\ge0,\qquad\sum_{x',y}J_a(x,x',y)=1.
\]

This is inherited Principia RFO-01: transition and measurement must be derived
from one joint law. A post-state-only likelihood is not universally adequate.
For prior/current belief b and action a, the outcome probability and posterior
are

\[
p(y\mid a,b)=\sum_{x,x'}b(x)J_a(x,x',y),\quad
b'(x')=\frac{\sum_x b(x)J_a(x,x',y)}{p(y\mid a,b)}.
\]

The posterior is defined only for a positive-probability outcome. Retrospective
targets about the original state require retaining its joint law with the
current state, as in the inherited recursive observer.

A policy pi_t(a|h) is selected from the known past record h and declared
randomness that is conditionally independent of the hidden source given that
record. For a hidden path and a fixed policy, the causal history volume is

\[
\Pr(x_{0:n},a_{1:n},y_{1:n})
=b_0(x_0)\prod_{t=1}^n\pi_t(a_t\mid h_{t-1})
 J_{a_t}(x_{t-1},x_t,y_t).
\]

Summing future states/actions/outcomes yields the shorter history law. This
consistency is the operational meaning of a probability volume. It is separate
from a geometrical drawing of knowledge layers.

A **knowledge slice** is a chosen report/sigma-algebra. A finer admissible
instrument can reveal distinctions absent from that slice. An action outside
the frame, or assigned zero policy support, cannot be created merely by
reweighting the supported actions. Enlarging the frame needs a specified new
instrument or program, its source coupling, and its cost.

For two predeclared full-support source hypotheses with the same predictable
policy, action factors cancel from their likelihood ratio. Under the null,
the outcome likelihood-ratio process has conditional mean equal to its previous
value. Thus it is a unit-start nonnegative martingale, with Ville bound for
0<epsilon<1:

\[
\Pr_0\{\sup_t E_t\ge1/\epsilon\}\le\epsilon.
\]

This is inherited sequential-testing mathematics, not a probability that the
null is false. It requires the declared filtration and conditional likelihoods.
A copied observation, already determined by the record, has conditional
likelihood one under both models and adds no evidence. Hidden side channels or
outcome-fitted alternatives require a different model and invalidate the
unqualified calibration. See inherited #628--630 and the explicit copy/action
controls in this round's tests.

## AH-02. Haar detail and the observer's bounded information accumulation

Fix ONE probability measure mu and nested sigma-algebras F_j. On L2(mu), let
P_j f=E_mu[f|F_j] and D_j=P_(j+1)-P_j. Conditional expectation gives

\[
P_jP_k=P_{\min(j,k)},\qquad D_jD_k=0\ (j\ne k),
\]

and consequently

\[
\|P_Jf-P_0f\|_2^2=\sum_{j=0}^{J-1}\|D_jf\|_2^2.
\]

On a cell C split into children L,R of positive mass, the normalized detail is

\[
h_C=\sqrt{\frac{\mu(R)}{\mu(L)\mu(C)}}\mathbf1_L
 -\sqrt{\frac{\mu(L)}{\mu(R)\mu(C)}}\mathbf1_R,
\]

with coefficient and squared energy

\[
c_C(f)=\sqrt{\frac{\mu(L)\mu(R)}{\mu(C)}}(\bar f_L-\bar f_R),
\quad |c_C(f)|^2=\frac{\mu(L)\mu(R)}{\mu(C)}|\bar f_L-\bar f_R|^2.
\]

This is weighted Haar, not automatically the equal-mass textbook normalization.
The coefficient is a difference of predictive conditional means.

For a persistent hidden bit S and a history filtration H_t with deterministic
initial prior p_0 (for example, trivial H_0), write p_t=E[S|H_t]. Then p_t is a
bounded martingale and

\[
\boxed{\mathbb E p_n^2-p_0^2
=\sum_{t=1}^n\mathbb E(p_t-p_{t-1})^2
\le p_0(1-p_0).}
\]

**Proof.** Each increment has zero conditional mean; distinct increments are
orthogonal. Expand the square and use p_n^2<=p_n and E p_n=p_0. The left side
is also Var(S)-E Var(S|H_n). This is a temporal Haar/innovation decomposition
on the source's history tree.

Resolved structural information therefore accumulates in this bounded expected
squared-error sense. Individual p_t paths can rise or fall. Neither these
dimensionless quantities nor squared signal contrasts are calibrated joules.
If a posterior measure changes, its Haar inner product changes too; do not
add coefficients from different posterior metrics as though they shared one
orthogonal basis.

## AH-03. A hidden connection makes a deeper probe informative

Let S~Bernoulli(p), theta uniform on {-1,+1}, initially independent. A structural
probe C depends only on S, with

\[
\Pr(C=+\mid S=1)=a,\qquad\Pr(C=+\mid S=0)=b.
\]

The deep probe Y reports theta if S=1 and a fresh fair sign if S=0. No source
state changes in this model; conditional noise freshness is an assumption.
After structural observations only, theta remains fair and independent of S,
and p denotes the updated structural probability. Then

\[
\Pr(\theta=t,Y=y)=\frac{1+pty}{4},\qquad
\mathbb E[\theta Y]=p,\quad \mathbb E[\theta\mid Y]=pY.
\]

Relative to the uniform product reference, the joint density is 1+p theta Y.
Its mixed Haar coefficient is p; its squared detail is p^2. Equivalently,

\[
\operatorname{Var}(\mathbb E[\theta\mid Y])=p^2,
\]

the exact reduction in squared-error target Bayes risk.

With natural logarithms the expected information gain is

\[
I(p)=I(\theta;Y)
=\frac{(1+p)\log(1+p)+(1-p)\log(1-p)}2
=\sum_{k\ge1}\frac{p^{2k}}{2k(2k-1)}.
\]

The endpoints use continuous extension. Differentiation gives I'(p)=atanh(p)
and I''(p)=1/(1-p^2) on (0,1). The positive series proves

\[
\boxed{\tfrac12p^2\le I(p)\le(\log2)p^2.}
\]

Thus this declared channel quantitatively links Haar detail energy to expected
target information. It does not assert this calibration for arbitrary channels.

For n conditionally fresh favorable structural reports,

\[
p_n=\frac{p_0a^n}{p_0a^n+(1-p_0)b^n}.
\]

For 0<p_0<1 and 0<b<a<=1, p_n and the subsequent deep-probe value strictly
increase. Adverse observations can decrease both. Replaying a stored result
does not license this fresh-sample formula.

**Full-state boundary.** After a deep observation, S and theta are generally
correlated and theta is no longer fair. The scalar p is then insufficient for
future probe value. The implementation retains all four probabilities
Pr(S,theta) and uses the full posterior. Resetting to the independent family
is an explicitly rejected mutation.

## AH-04. A probe with no immediate target information can open a useful path

Before any deep observation, C is independent of theta, so I(theta;C)=0.
Let q=pa+(1-p)b and p_C=Pr(S=1|C). When 0<q<1,

\[
\boxed{\operatorname{Var}(p_C)
=\frac{p^2(1-p)^2(a-b)^2}{q(1-q)}.}
\]

For an almost-surely constant report (q=0 or q=1), this variance is zero.
An informative deterministic report, such as C=S, need not have zero variance.
To prove the formula,
subtract p from pa/q and p(1-a)/(1-q) and average their squared differences.
This is the squared weighted Haar coefficient of S on the C split. It is also

\[
\mathbb E[p_C^2]-p^2,
\]

the increase in expected deep-probe detail energy. Since I(p)-p^2/2 is convex,

\[
\boxed{\mathbb E I(p_C)-I(p)
\ge\tfrac12\operatorname{Var}(p_C).}
\]

This is strict for an interior prior and informative a!=b. The chain rule gives
I(theta;C,Y)=E I(p_C), so the first probe genuinely increases the information of
the two-step causal experiment despite its zero immediate target information.

**Certified example.** Take p=1/2, a=3/4, b=1/4. The posteriors are 1/4 and 3/4,
equally likely; Var(p_C)=1/16. Charge the specified costs c_C=1/100 and
c_Y=3/20 in nats of utility. Both single-step utilities are negative:

\[
0-c_C<0,\qquad I(1/2)-c_Y<0.
\]

But the fixed two-step plan has positive utility:

\[
\tfrac12[I(1/4)+I(3/4)]-c_C-c_Y>0.
\]

The tests certify these inequalities by rational positive-series enclosures,
not floating-point threshold decisions. The implemented planner also permits
stopping after C instead of always paying for Y; this improves the displayed
example's utility by declining the unfavorable branch. The fixed two-step
inequality is separately tested. These comparisons concern the declared plan
menu, not global optimal planning over all future policies.

For finite admissible actions with finite real utilities J_a and reference
probabilities r_a>=0 summing to one, optimize over policies supported on
{a:r_a>0}. A specified
entropy-regularized decision objective is

\[
\max_\pi\left\{\sum_a\pi_a J_a
-\beta^{-1}\sum_a\pi_a\log(\pi_a/r_a)\right\},\quad\beta>0.
\]

On the supported actions, strict concavity yields the unique maximizer

\[
\pi_a=\frac{r_ae^{\beta J_a}}{\sum_b r_be^{\beta J_b}},\qquad
\log\frac{\pi_a}{\pi_b}=\log\frac{r_a}{r_b}+\beta(J_a-J_b).
\]

Take J to be the declared expected information less its specified cost, or an
explicit multi-step value. Holding competitors and costs fixed, stronger
structural evidence raises deep-probe odds in the AH-03 family. Zero reference
support remains zero. As beta tends to infinity, mass concentrates on the
utility-maximizing supported actions, with reference-proportional weights
among ties. Concentration need not increase monotonically with beta for a
nonuniform reference. This action-selection limit is not a proof of the
hypothesis or a derivation of quantum-to-classical physics.

## AH-05. A precise attraction model and its Gamma/Haar coupling law

For a declared symmetric graph of nonnegative weights w_ij, set

\[
\mathcal E(u)=\frac12\sum_{i<j}w_{ij}(u_i-u_j)^2,
\quad L_{ij}=w_{ij}\ (i\ne j),\quad L_{ii}=-\sum_{j\ne i}w_{ij}.
\]

Then

\[
-\nabla\mathcal E(u)=Lu,\qquad
(Lu)_i=\sum_jw_{ij}(u_j-u_i).
\]

This is an exact differential-coupling/attraction analogy: connected prediction
coordinates relax toward each other. The mathematical potential decreases
along dot u=Lu. Inferring w from observations needs a source model; the analogy
does not turn statistical information into physical force.

More generally let L be a finite reversible Markov generator, self-adjoint
and nonpositive in L2(pi), for full-support stationary pi. For alpha>0 and
lambda>0,

\[
G_\alpha=\frac{\lambda^\alpha}{\Gamma(\alpha)}
 \int_0^\infty t^{\alpha-1}e^{-\lambda t}e^{tL}\,dt
=(I-L/\lambda)^{-\alpha}.
\]

The spectral theorem proves the equality. The integrand is a Markov semigroup
with a positive unit-mass Gamma clock. Consequently G is self-adjoint, a
positive contraction in Hilbert-space order, and G_alpha G_beta=G_(alpha+beta).

For any orthogonal report projection P and Q=I-P,

\[
\boxed{\mathcal D_\alpha
=PG_{2\alpha}P-(PG_\alpha P)^2
=PG_\alpha QG_\alpha P
=(QG_\alpha P)^*(QG_\alpha P)\succeq0.}
\]

If the hidden complement resolves as orthogonal Haar slices Q=sum_j D_j,

\[
\boxed{\mathcal D_\alpha
=\sum_j(D_jG_\alpha P)^*(D_jG_\alpha P).}
\]

This is a sum of hidden-detail energies: keeping the fine carrier through both
depths differs from projecting it away between depths. It sharpens inherited
GV-06's general defect by specifying an inner product, reversibility and a
resolution into Haar slices.

Because G^2<=G, the compression A=PGP on Ran P obeys

\[
0\preceq\mathcal D_\alpha\preceq A-A^2\preceq\tfrac14P.
\]

For alpha>0, D_alpha=0 iff [G_alpha,P]=0 iff [L,P]=0. The first equivalence
uses the Gram identity and self-adjointness; the second uses injectivity of
x -> (1-x/lambda)^(-alpha) on the finite real spectrum. At alpha=0, the defect
is zero for every P and gives no such inference.

The same Gram identity holds for any self-adjoint contraction semigroup
S_alpha, independently of a Markov interpretation. This includes the original
source multiplication model in AH-06.

**Exact classical control.** The four-state symmetric path generator with unit
edge rates has, at lambda=alpha=1,

\[
G_1=\frac1{21}
\begin{pmatrix}13&5&2&1\\5&10&4&2\\2&4&10&5\\1&2&5&13\end{pmatrix}.
\]

For P averaging consecutive pairs and v=(1,1,-1,-1),

\[
\mathcal D_1=vv^T/196,\qquad\operatorname{tr}\mathcal D_1=1/49>0.
\]

This nonzero hidden-slice response is entirely classical. For the directed
four-cycle generator L=S-I under the same report, the positive stochastic
Gamma operator instead gives D_1=-vv^T/100, with eigenvalue -1/25. Reversibility
cannot be omitted. Unequal-depth defects need not be self-adjoint, and PSD
does not mean entrywise nonnegative. On an irreducible reversible source,
large depth approaches the constant-state projection and may erase the
detectable defect; increasing volume depth is not monotone information gain.

## AH-06. The authentic BBP causal-volume covariance is weighted Haar energy

Retain the inherited original source exactly:

\[
R(x)=\frac{4-2x^3-x^4-x^5}{16-x^8}
=\frac{1-x}{4a(x)},\quad
a(x)=1-x+x^3/2-x^4/4,
\quad\mu(dx)=\frac{16}{\pi}R(x)dx.
\]

The normalization integral R dx=pi/16 is the original BBP identity. Fix
alpha,beta>0 and 0<=z<1. For u=x-x^2/2 and v=x^2/2, let

\[
G_x(z)=\frac{(1-u)(1-v)}{(1-uz)(1-vz)},\qquad f_\alpha(x)=G_x(z)^\alpha.
\]

These are the inherited conditional source-depth probability generating laws.
Multiplication by f_alpha gives a self-adjoint positive-contraction depth
semigroup on L2(mu). Its constant-report composition defect is

\[
\operatorname{Cov}_\mu(f_\alpha,f_\beta).
\]

Use DYADIC intervals in x and their actual mu masses, with P_0 the mean. For
every finite J>=0,

\[
\boxed{\operatorname{Cov}_\mu(f_\alpha,f_\beta)
=\sum_{j=0}^{J-1}\sum_{C\in\mathcal P_j}
 c_C(f_\alpha)c_C(f_\beta)
+\langle(I-P_J)f_\alpha,(I-P_J)f_\beta\rangle.}
\]

**Proof.** Apply the mutually orthogonal conditional-expectation decomposition
in AH-02 to the two centered functions. Source positivity gives positive mass
to every nondegenerate cell. For alpha>0,z<1, f_alpha is strictly decreasing,
so every oriented left-minus-right coefficient c_C(f_alpha)>0. The residual
covariance is a positive average of within-cell covariances of two strictly
decreasing functions, hence is strictly positive at each finite J.

There is a quantitative infinite-resolution lift. Since u'+v'=1 and
0<=u,v<=1/2,

\[
|f_\alpha'|\le L_\alpha:=\frac{4\alpha(1-z)}{2-z}.
\]

In each width-2^(-J) cell, the variance bound by one quarter of squared range
and Cauchy--Schwarz give

\[
0<\langle(I-P_J)f_\alpha,(I-P_J)f_\beta\rangle
\le\frac{L_\alpha L_\beta}{4}\,4^{-J}.
\]

Therefore the full original covariance is the convergent sum of weighted
Haar coefficient products. Equal depths give a sum of squares. At z=1 or
depth zero the relevant function is constant and the strictness is absent.

At alpha=beta=1,z=0, f=a and the inherited moment calculation gives

\[
\boxed{\operatorname{Var}_\mu(a)
=\frac{7\pi-20}{5\pi^2}
=\sum_{j\ge0}\sum_{C\in\mathcal P_j}|c_C(a)|^2>0.}
\]

Here a'=-1+(3/2)x^2-x^3 increases from -1 to -1/2, so Lip(a)<=1. The native
finite remainder obeys the sharper bound

\[
0<\|(I-P_J)a\|_2^2\le\frac14\,4^{-J}.
\]

This directly connects Haar detail to the existing four-channel causal volume.
The carrier x is the original Oily source coordinate; it is NOT the completed
radix phase of U_n. The existing zero-anchored phase-grid Haar observer and
the present weighted source-coordinate Haar observer need a further declared
intertwiner before their outputs can be identified.

### A rational certificate for the actual source

Let P(x)=4-2x^3-x^4-x^5. On [0,1], 0<=P<=4. With N>=1,

\[
R_N(x)=\sum_{n=0}^{N-1}\frac{P(x)x^{8n}}{16^{n+1}},\qquad
0\le R-R_N\le\frac4{15}16^{-N}.
\]

Consequently every rational cell mass r_C=integral_C R has a rational
enclosure of width at most |C|(4/15)16^(-N). For integer m>=1,

\[
A_C^{(m)}=\int_C a^mR
=\frac14\int_C(1-x)a^{m-1}
\]

is an exact rational polynomial integral. Writing Z=integral R and splitting
C into L,R, the normalized coefficient energy is

\[
|c_C(a^m)|^2
=\frac{(A_L^{(m)}r_R-A_R^{(m)}r_L)^2}{Zr_Cr_Lr_R}.
\]

All denominators are positive. Strict monotonicity supplies the numerator's
orientation. The remaining conditional variance is

\[
\frac1Z\sum_{C\in\mathcal P_J}
\left(A_C^{(2m)}-\frac{(A_C^{(m)})^2}{r_C}\right).
\]

The implementation encloses these expressions by outward rational inequalities
and uses Lip(a^m)<=m to cap the residual by m^2 4^(-J)/4. No pi value or
floating-point quadrature is needed for the certificates.

## AH-07. The same coarse data can hide either classical mixing or entanglement

Specify a bipartite Hilbert space C2 tensor C2 and trusted local qubit axes
Z=diag(1,-1), X=[[0,1],[1,0]]. The two-point normalized Haar/Hadamard matrix H
satisfies H Z H=X. This is a change of local measurement basis; a local unitary
does not itself create bipartite entanglement.

For real -1<=c<=1, define

\[
\rho(c)=\tfrac12(|00\rangle\langle00|+|11\rangle\langle11|)
+\tfrac c2(|00\rangle\langle11|+|11\rangle\langle00|).
\]

Its nonzero eigenvalues are (1+c)/2,(1-c)/2, so it is a density matrix. Both
local marginals are I/2, and

\[
\langle ZZ\rangle=1,\qquad\langle XX\rangle=c.
\]

Every c has identical joint Z-basis probabilities. At c=0 this is a separable
classical mixture; c=1 is the coherent Bell state. Partial transpose has
eigenvalues 1/2,1/2,c/2,-c/2; every c!=0 is entangled in this specified tensor
factorization.

For every separable two-qubit state,

\[
\boxed{|\langle XX\rangle|+|\langle ZZ\rangle|\le1.}
\]

**Proof.** For a product state, local Bloch coordinates obey x^2+z^2<=1.
Cauchy--Schwarz bounds |x_Ax_B|+|z_Az_B| by one. Convexity extends the bound to
separable mixtures. For rho(c) the score is 1+|c|, strictly above one when c!=0.
This is a trusted-qubit witness. A score at most one is inconclusive for
general states; arbitrary classical devices are not constrained by the
single-qubit Bloch disk.

Indeed two independent shared classical signs lambda_X,lambda_Z reproduce ALL
four X/Z setting-pair distributions of the c=1 Bell example: each party outputs
the shared sign for its selected axis. Thus an X/Z score of two, without the
trusted qubit measurement model, is not a device-independent Bell test.

## AH-08. Detectable back-action respects no-signalling

For a local instrument with Kraus operators K_y on A, a selected branch with
positive probability p_y>0 has

\[
p_y=\operatorname{Tr}[(K_y\otimes I)\rho(K_y^*\otimes I)],\quad
\rho_{AB|y}=\frac{(K_y\otimes I)\rho(K_y^*\otimes I)}{p_y}.
\]

Zero-probability branches have no normalized posterior. Outcome probabilities
must accompany normalized postselected states. For the
complete instrument sum_y K_y^*K_y=I, forgetting the outcome gives

\[
\boxed{\sum_{y:p_y>0}p_y\rho_{B|y}=\rho_B.}
\]

**Proof.** Pair either side with an arbitrary Bob observable B; cyclicity of
trace and completeness give sum_y Tr[rho(K_y^*K_y tensor B)]
=Tr[rho(I tensor B)]. This proves equality of reduced densities.

For rho(c), selected Alice Z outcomes give Bob |0> or |1> with probability
one half, for both c=0 and c=1. Conditional remote updates alone therefore do
not distinguish entanglement from classical correlation. Discarding Alice's Z
result maps every rho(c) to rho(0), killing its XX coherence while leaving Bob
at I/2. A subsequent JOINT complementary-basis experiment can see the effect;
Bob's unconditional local statistics cannot reveal Alice's choice.

Classical instruments may also disturb a hidden state and change subsequent
outcomes. Order dependence, hidden memory, noncommuting lossy projections, or
the classical Gamma defect in AH-05 are not by themselves quantum witnesses.

## AH-09. A fully rational rotated-setting Bell discriminator

Choose A0=Z,A1=X and

\[
B_0=(4Z+3X)/5,\qquad B_1=(4Z-3X)/5.
\]

These are unit qubit axes, and all their projectors have rational entries. For
rho(c), the CHSH combination is

\[
\boxed{S=\langle A_0B_0\rangle+\langle A_0B_1\rangle
+\langle A_1B_0\rangle-\langle A_1B_1\rangle
=\frac85+\frac65c.}
\]

It is 8/5 at the dephased control c=0, 5/2 at c=3/4, and 14/5 at c=1.
For deterministic local outcomes a0,a1,b0,b1 in {-1,+1},

\[
a_0(b_0+b_1)+a_1(b_0-b_1)\in\{-2,2\}.
\]

Convex mixtures obey |S|<=2. The exact tests enumerate all sixteen tables and
compute all selected quantum probabilities. This is a model-predicted
discriminator. A physical Bell interpretation additionally requires appropriate
setting independence, no inter-wing communication and controlled selection
loss; none is established merely by running this mathematical simulator.
The fixed axes do not detect every c!=0, though AH-07's trusted witness does.

## AH-10. What the bridge permits, and the ER=EPR dependency still missing

The mathematical history law extends to quantum instruments with initial
density matrix rho_0. For each admissible action a, require outcome maps
I_(a,y) to be completely positive and trace-nonincreasing, with sum_y I_(a,y)
trace-preserving. Then replace classical transition matrices by those maps:

\[
\Pr(h)=\left(\prod_t\pi_t(a_t\mid h_{t-1})\right)
\operatorname{Tr}[\mathcal I_{a_n,y_n}\circ\cdots\circ
\mathcal I_{a_1,y_1}(\rho_0)].
\]

For each declared adaptive instrument tree, outcome disposal gives consistent
coarser history probabilities. Coarsening forgets records while retaining the
performed channels and their actual adaptive feedback; it does not delete an
intervention. The compressed record may need hidden memory to describe that
protocol. This does not license one common table of predetermined outcomes
for all incompatible measurement contexts.

Thus the user's hidden-state hypothesis has an operational test: identify the
carrier, subsystem factorization, admissible interventions, and matched
classical controls; then compare joint response laws across measurement
contexts. The unmeasured target, the observer's posterior and the carrier's
post-intervention state are three different objects.

The inherited arithmetic thermofield state and its diagonal classical mixture
already demonstrate this distinction on SUCC's declared Hilbert carrier.
Their shared diagonal source probabilities and local marginals do not identify
the coherent state. A mathematical purification is not evidence that a
physical source implements it.

Original ER=EPR concerns a proposed connection between entanglement and
Einstein--Rosen geometry, with specific black-hole/holographic realizations and
a broader conjectural extension. A causal graph, Haar transform, positive
Gamma volume or Bell-state simulation supplies no gravitational dual by
itself. Traversable holographic examples require an added boundary interaction
and still obey causality. A SUCC ER=EPR claim needs an actual dual dictionary,
dynamics and matching operational observables; that edge is UNVERIFIED here.

The concrete results are the structural-probe/Haar/information bridge, its
two-step option value, the original-source Haar decomposition of causal-volume
covariance, the reversible Gamma leakage identity, and the conditional/joint
quantum discriminators. Source authenticity and TLICA source-map adequacy are
separate from model-internal confidence. No result here establishes pi
normality, RH, a physical force between abstract truths, or entanglement of
mathematical reality itself.
