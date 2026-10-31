# Where snapshots lose arrows, and what recovers them

**Status:** PROVED LOCAL paper arguments below; exact finite probes and a
separate Beta/interpolation implementation. No external refereeing, Lean
certificate, scholarly-priority claim, universal physical category, or new
selected signed bound is asserted. Parent405 is
`6cf5050ff2cfd92e7a0c8876da5233be6ff117f5`.

The user's intuition has a precise useful realization: a family of snapshots
can conceal different composable histories. But scalar constants do not, in
general, identify those histories. This dossier gives an exact counterfeit
that retains **every one-time posterior snapshot at every horizon**, then a
finite theorem locating invisible arrows and a constructive recovery method.
It uses the original BBP positive source, not a fitted Gamma replacement.

## 1. Typed carrier and the actual question

Keep

    Q(x)=4−2exp(−3x)−exp(−4x)−exp(−5x),
    R(a)=4/a−2/(a+3)−1/(a+4)−1/(a+5),
    μ_a(dx)=exp(−ax)Q(x)dx/R(a),  a>0,
    p(x)=1−exp(−8x).

The original auxiliary sensor draws X~μ_a once, then draws conditional-iid
Bernoulli(p(X)) bits B_1,B_2,…; J_m=Σ_{i≤m}B_i. Its full snapshot is the joint
measure (X,J_m), retaining the source posterior. This is precisely the
repository's declared source sensor, not a probability law for π's digits.
The chronological arithmetic U_0=0, U_n=16U_{n−1}+R(8n−7) is unchanged.

Objects may be these finite posterior state spaces; arrows are source-labelled
conditional transitions, with composition by summing intermediate states.
Realization into a coarse snapshot forgets some path coordinates. We use this
as an instance of the repository's existing operational category, not a second
incompatible universal-category implementation. The pertinent question is
whether a declared collection of realizations is **jointly faithful on arrows**.

Yoneda's classical reconstruction involves an entire natural family of
representable observations, including their action on morphisms. It does not
say that a few scalar invariants of objects determine arrows. See Emily
Riehl, [Category Theory in Context, §§2.1–2.2](https://emilyriehl.github.io/files/context.pdf).
The proofs below do not require Yoneda as an unproved shortcut.

## 2. CA-01: all-horizon, full-posterior snapshot aliases

**Theorem.** For every a>0 there is a distinct positive source sensor with the
same law of (X,J_m) for **every integer m≥0**, but a different conditional
history update. In particular every integrable one-time harmonic, logarithmic,
Gamma, endpoint-PGF, golden-root, or Oily–Macaroni readout of those snapshots is
identical, at every finite horizon and in every limit where the original
readout is defined.

**Construction and proof.** Given X=x write p=p(x), t=1−p. Modify only the
conditional law of the first three bits by the signed four-word perturbation

| word | 010 | 011 | 100 | 101 |
|---|---:|---:|---:|---:|
| added conditional probability | +δ | −δ | −δ | +δ |

where δ=½p²t². All other three-bit probabilities are unchanged. Afterwards
sample bits independently with Bernoulli parameter p, independent of the first
three conditional on X.

The four affected base probabilities are pt²,p²t,pt²,p²t. Since
δ/(pt²)=p/2≤1/2 and δ/(p²t)=t/2≤1/2, subtraction preserves positivity (strict
for 0<p<1). Total added mass is zero. At prefix length1 the perturbations cancel
within each first bit. At length2 they cancel within each word01 and10.
At length3 they cancel separately within each grade1 and2. Thus all grade
marginals for m≤3 agree pointwise in x. For m>3, convolve the identical J_3
law with the same independent Binomial(m−3,p) law. This proves equality at
every m, pointwise in x, and therefore equality of the full (X,J_m) measures.
No limiting exchange or numerical extrapolation is used.

Nevertheless

    P'(B_3=1 | B_1B_2=01,X)=p−p(1−p)/2,
    P'(B_3=1 | B_1B_2=10,X)=p+p(1−p)/2.

Their difference p(1−p)>0 is an actual hidden causal-order effect. In the
original sensor both probabilities equal p. The full-source-integrated
increase of word010 has the exact positive rational value

    Δ_a = [R(a+16)−2R(a+24)+R(a+32)]/[2R(a)].

For rational a this is rational; positivity follows by integrating ½p²t²
against the strictly positive source density. All one-time posterior moments,
not merely their finite Taylor jets, agree. Because this holds for every a,
it also holds along the native diagonal a_m=8m−7.

**What this refutes.** The endpoint triangle, even retained with its entire
source posterior at each separate time, cannot alone identify causal arrows.
The same argument preserves all16 Walsh functions of J_m mod16 and every
one-time grade statistic. It does **not** preserve all joint path/Walsh
statistics; those are precisely available discriminating probes. It changes
the auxiliary sensor's conditional-iid rule, so it is neither an admissible
replacement for the authentic declared update nor a counterexample to π
normality. The original four-pole source and selected zero trajectory are
identical throughout.

**Smallest repair in this model.** Retain the two history-conditioned
predictions above, or impose and verify the original conditional-iid/Markov
update given X. Full marginal snapshots are weaker information. An unverified
Markov assumption must not be smuggled in as a property of every carrier.

## 3. CA-02: exactly how temporal coarsening hides finite arrows

Fix m,d≥1. Let J be a joint coupling from grade i∈{0,…,m} to grade
k∈{0,…,m+d}, supported on i≤k≤i+d, with strictly positive mass on every
allowed edge. The native conditional-iid sensor has exactly this support:

    J_{ik}=C(m,i) C(d,k−i) q_{m+d}(k)/C(m+d,k),

where q_l is its endpoint distribution. Integrating the positive source
makes every allowed entry positive. Its two margins are q_m and q_{m+d}.

**Theorem.** The affine space of endpoint-preserving perturbations has
exact dimension m(d−1). An explicit basis is given by four-edge cycles
Z^{i,k}, for 0≤i<m and i+1≤k<i+d, with entries

    Z_{i,k}=Z_{i+1,k+1}=+1,
    Z_{i,k+1}=Z_{i+1,k}=−1,

and zero elsewhere. Consequently every nonzero sufficiently small multiple
of such a direction changes the arrow while preserving both snapshots.

**Proof.** The bipartite support graph is connected: row i and row i+1 share
columns i+1,…,i+d, and every column is incident. It has
E=(m+1)(d+1) edges and V=2m+d+2 vertices. The row/column sum map has rank V−1:
a linear relation between its vertex rows assigns numbers u_i,v_k with
u_i+v_k=0 on every edge; connectedness forces one free constant. Hence its
kernel dimension is E−V+1=m(d−1).

The displayed cycles lie in the kernel. They are independent: in the first
row, a combination of adjacent column differences can vanish only when every
coefficient for i=0 vanishes; proceed row by row. Their count is m(d−1), so
they are a basis. Strict positivity provides an open neighborhood of zero in
this kernel inside the coupling polytope. This proves the dimension assertion
for feasible arrows, not merely formal signed matrices.

**A positive uniqueness result, d=1.** The support graph is a tree. Consecutive
complete endpoint laws p_j,q_k uniquely fix the one-step joint arrow:

    A_j = Σ_{k=0}^j q_k − Σ_{k=0}^{j−1} p_k,
    B_j = p_j−A_j,

where A_j is mass on j→j and B_j on j→j+1. Division by p_j recovers its
transition probabilities when p_j>0. Existence is conditional on these
masses being nonnegative, which the native source guarantees.

This is not a contradiction with CA-01: pairwise arrows do not identify an
arbitrary history-dependent path law. With a declared Markov law, the
one-step arrows do compose to determine every finite path distribution.
Without it, CA-01 shows that coarse grade0,…,grade_m snapshots can conceal
history dependence. If the entire realized history remains part of each
object, the two sensors are distinguishable.

## 4. CA-03: what the triangle constants see on a cycle

For scalar observations f_i,g_k, a cycle perturbation εZ^{i,k} changes the
two-time observable E[f(J_m)g(J_{m+d})] by exactly

    ε(f_i−f_{i+1})(g_k−g_{k+1}).

This is an actual composition-sensitive quantity. A separable edge readout
u_i+v_k is blind to every cycle; conversely every readout blind to all cycles
is such a vertex-potential sum on this connected graph, by orthogonal
complements of the incidence matrix. Thus a scalar constant repeated at
vertices does not encode the missing cycle coordinate.

For harmonic numbers H_j=Σ_{l=1}^j1/l and ε>0, the mixed harmonic defect is

    ε/[(i+1)(k+1)] > 0.

So harmonic observations can be load-bearing **when paired across times**.
Replacing H_j by H_j−c or by any common additive offset leaves this defect
unchanged. In particular ψ(j+1)=H_j−γ has precisely the same cycle defect:
Euler–Mascheroni drops out. The Gamma recurrence and this classical digamma
identity are recorded in [DLMF §5.5](https://dlmf.nist.gov/5.5) and
[§5.4](https://dlmf.nist.gov/5.4). The golden probe g_j=λ^j, λ=(√5−1)/2, also
detects each elementary cycle, since its adjacent differences are nonzero.
The same is true at every rate λ∈(0,1); this detection does not uniquely
select the golden value.

A single probe does not identify a multidimensional cycle space: different
cycle contributions may cancel. More generally, if Z_1,…,Z_b form the cycle
basis and c_1,…,c_l are edge-observable arrays, then complete finite arrow
identification is equivalent to

    rank( [Σ_edges c_r(e) Z_s(e)]_{r,s} ) = b.

If rank is deficient, a nonzero null direction can be scaled to preserve
positivity. If rank is full, identical readouts and margins force identical
arrows. This is a necessary-and-sufficient criterion under the stated finite
support hypothesis, not a sufficient statistic assumed from matching constants.

**A stronger executed adversary.** At m=4,d=4, b=12. The complete two-time
moment matrix for the three-dimensional probe space

    V = span_R{1,H_j,λ^j}

has only four non-marginal products HH,Hλ,λH,λλ. Since λ lies in Q(√5), these
supply at most seven rational linear constraints on rational cycle directions.
Hence a nonzero rational invisible direction always exists. The exact probe
constructs one by rational elimination, normalizes max|Z_ik|=1, and verifies
all nine V×V products using a separate Q(λ) implementation.

The construction can retain the *one-time full X-posterior* as well. At fixed
X, M=m+d=8, add

    (1/2) p(X)^M[1−p(X)]^M Z_{ik}

to the native conditional joint probabilities. Each native allowed entry is
an integer at least1 times p^k(1−p)^{M−k}; the ratio of the perturbation's
magnitude is at most1/2. This preserves positivity. Its row and column sums
are zero pointwise in X, and every V×V moment defect is zero pointwise in X.
After source integration its scale is ½E_mu[p^8(1−p)^8], an exact positive
rational at rational a. Fresh a=17,97,233 produce different arrows matching
all these triangle observations. This includes every two-time readout of
H_j−γ−λ^j and every affine combination of the three probes. It does not claim
to match arbitrary nonlinear functions of those probes, which can separate
finite grades.

Thus γ and Ω_OM remain meaningful anchored vertex values in the author's
triangle; their common additive pieces are not new loop coordinates here.
A golden mixed observation detects some internal arrows, but its presence
alone is not sufficient to recover them.

## 5. CA-04: exact harmonic-resolvent tomography repairs the ambiguity

Let latent marks x_1,…,x_r be distinct nonnegative reals and probe parameters
a_1,…,a_r distinct positive reals. Let C_ij=1/(a_i+x_j). Similarly use a
square Cauchy matrix D for the target marks. For any r×s real joint matrix J,
the two-time resolvent matrix

    M = C J D^T

uniquely determines J, with J=C^(−1) M D^(−T). Hence a finite family of
**two-time** harmonic resolvents is jointly faithful on these arrows. The
constants γ,λ are not needed as extra unknowns in this inversion.

**Proof without a determinant formula.** Suppose Cv=0. The rational function
F(t)=Σ_j v_j/(t+x_j) has numerator of degree at most r−1 over
D_x(t)=Π_j(t+x_j). It vanishes at r distinct positive a_i, so the numerator
is identically zero. The residue at −x_j is v_j, hence v=0. Thus C is
invertible, and similarly D. Equivalently, reconstruct the numerator from
its values F(a_i)D_x(a_i) by Lagrange interpolation and recover each residue.
The primary implementation uses exact Gaussian elimination; the separate
oracle uses this interpolation/residue route.

**Finite-precision cost.** If every measured entry has error at most ε,

    ||ΔJ||_max ≤ ||C^(−1)||_∞ ||D^(−1)||_∞ ε.

This follows entrywise by the triangle inequality. These inverse norms may
be enormous. The receipt reports the exact amplification for each native
fixture. Identifiability is not a stable reconstruction theorem uniform in
horizon, and is not a signed cancellation estimate. Repeated or dependent
probe parameters destroy invertibility; that negative control is tested.

At m4,d4 a resolvent entry detects the triangle-matched direction from CA-03.
This is a concrete discriminating experiment, not only an existence theorem.
The complete matrix recovers it exactly.

## 6. What remains dark for the selected π orbit

All category constructions here are source-marginal or auxiliary-sensor
statements. They remain the same when the arithmetic seed changes from0 to
the coherent seed −π/16. Retaining an actual selected-phase evaluation is
additional structure; the earlier BBP source and Green transport already
identify that structure exactly but do not bound its signed sums.

A next useful interaction must be both:

1. arrow-sensitive beyond the kernel of the declared snapshot probes; and
2. quantitatively tied to the chronological arithmetic, including U_0=0,
   full literal carries, complete16-state characters, and complementary CRT
   phase, with a signed norm estimate.

CA-04 supplies finite identifiability; it does not supply the second item.
CA-01 supplies a sharp falsifier for inferring causal arrows from even the
full collection of one-time constants and posteriors. CA-02 tells exactly
when temporal thinning creates hidden dimensions under the declared support.
Neither the user intuition nor its countermodels establish a universal carrier
category, and no claim of complete characterization of a mathematical
“fabric” is made. π normality, SC-06 and RH remain open.

## 7. Provenance and execution

The full-posterior sensor and original triangle are inherited from
`docs/OPERATIONAL_TRIANGLE.md` and
`research/2026-10-29/operational_triangle_frontier/operational_triangle.py`.
Author nomenclature is Leah / femboy2112, preserved by
`research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md`.
The earlier nonuniversal-sufficiency example motivates CA-01, but did not
provide this all-horizon source-faithful marginal alias. No priority claim
is made for the elementary transportation/cycle/Cauchy facts.

Exact original-source moment route: finite differences of R(a).
Separate route: substitution t=exp(−8X), then rational Euler Beta products.
Primary matrix route: rational elimination. Separate route: rational
interpolation and residues. Both are implemented by the same model and share
the declared source; they are computationally distinct, not independent
human or external proof authorities. Raw receipts include every executed
validation run. The dossier's unrestricted claims rest on the proofs above,
not on the finite census.
