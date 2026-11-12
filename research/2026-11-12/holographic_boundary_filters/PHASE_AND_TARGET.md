# Boundary filters: target completeness, phase, and the cost of inversion

Date: 2026-11-12. Parent: Main XXV,
db9fb4b84672050efa79b13377f1e73364598a14.

**Verdict.** Boundary reconstruction has an exact target-dependent meaning:
the boundary must distinguish every pair of admissible interiors on which the
target differs. For a finite linear observation contract this gives an explicit
dual certificate or an explicit indistinguishable pair. Ordered triple
observations can recover phase lost by pair observations, under a checkable
support condition. Even then, inversion can become poorly conditioned near
the uniform law. None of these statements supplies an all-large-epoch
estimate for the selected BBP orbit.

Authority: the derivations below are local paper proofs; executable checks use
exact integer/Fraction arithmetic. They are not Lean results, external peer
review, or a scholarly priority claim. Classical completeness results are
identified as such. π normality, the signed R0 rung, and Goldbach remain OPEN.

## 1. What is already present

This dossier does not restart the observer program.

- The [2026-11-04 delayed-bispectrum audit](../../2026-11-04/zero_frame_bispectrum_audit/PROOFS.md)
  already proves that a cubic delayed observer can retain one authentic
  angular factor erased by a pair Gram. It pays a source-derived curvature
  error and explicitly leaves its signed mean OPEN.
- The [2026-11-07 continuum two-tone theorem](../../2026-11-07/driven_pinbed_observability/CONTINUOUS_THEOREMS.md)
  already constructs a full-profile inverse, checks channel compatibility,
  proves an H^{-1} frame estimate, and transports the authentic BBP tail.
  The selected energy decay remains equivalent to an unproved statistical
  condition.
- The [Main XXV frontier](../../../docs/PI_NORMALITY_FRONTIER.md) distinguishes
  zero-seed identification, finite computation, and signed statistical
  estimates. In particular its R0 target is weaker than all-mode normality.

The additions here are target-relative dual certificates, exact ambiguity
diameters, explicit phase-support failures, and a quantified conditioning
failure at the uniform boundary. The finite bispectrum theorem is a
classical phase-retrieval specialization, not a new arithmetic mechanism.

## 2. PT-01: the exact target-completeness test

**PROVED LOCAL; elementary finite linear algebra.**

Let Ω have n elements. Let f_0,...,f_m be real functions on Ω, with
f_0=1. Write F for the matrix with these rows. An unknown probability vector
p produces the boundary data y=Fp. Let t be a real target function and
V=span{f_0,...,f_m}.

The following are equivalent:

1. For every pair of probability vectors p,q, Fp=Fq implies t·p=t·q.
2. t belongs to V.
3. There is a coefficient vector c such that t=Fᵀc, hence t·p=c·y
   for every probability p.

**Proof.** The implications 2⇒3⇒1 are immediate. If t is not in the
row span of F, there is z in ker F with t·z≠0. Because the mass row is
present, ∑z_i=0. Its positive and negative parts have equal nonzero mass s.
The vectors p=z_+/s and q=z_-/s are probabilities with Fp=Fq and
t·p−t·q=(t·z)/s≠0. This proves the converse and constructs the failure
receipt. ∎

The statement is universal over probability laws. At one particular y,
positivity constraints may collapse the feasible fiber even if t is not in
V; PT-01 does not deny this stronger data-dependent conclusion.

The implementation returns either exact rational coefficients c or the
two actual probability laws p,q. A numerical rank threshold is unnecessary.
Adding a redundant filter does not change the answer.

### PT-02: the exact ambiguity diameter

**PROVED LOCAL; finite norm duality with proof supplied.**

Define the worst ambiguity remaining after these filters by

$$
\Delta_F(t)=
\sup_{\substack{p,q\ge0,\;\sum p=\sum q=1\\Fp=Fq}}
|t\cdot(p-q)|.
$$

Then

$$
\boxed{\Delta_F(t)=2\,\inf_{v\in V}\|t-v\|_\infty.}
$$

**Upper bound.** For every v∈V, the difference has zero v-moment, while
its ℓ¹ norm is at most two. Thus
|t·(p−q)|≤2||t−v||∞.

**Attainment.** A best approximation v* exists because V is a closed
finite-dimensional subspace. Put r=t−v* and d=||r||∞. The case d=0 is
settled. For d>0, consider the active coordinates I where |r_i|=d and
their signs σ_i. There are nonnegative weights α_i summing to one such that
z=∑_{i∈I}α_i σ_i e_i annihilates V. Indeed, if no such convex combination
annihilated V, finite-dimensional strict separation would give v∈V with
σ_i v_i>0 for every active i. Moving v* a sufficiently small positive
distance in direction v would reduce every active error and keep all
inactive errors below d, contradicting optimality.

This z obeys ||z||₁=1, z·t=z·r=d, and ∑z_i=0 because 1∈V. Consequently
p=2z_+ and q=2z_- are probabilities with equal F-data and target difference
2d. ∎

This converts “we need better boundary filters” into a numerical
mathematical question: how closely does their span approximate the target?
The current exact implementation constructs a nonzero witness or an exact
span certificate; it does **not** claim to solve the minimax optimization
in every input case. The four-atom calibration attains the displayed bound:
F has rows (1,1,1,1),(0,0,1,1), while t=(0,1,0,1).
The best error is 1/2 and the remaining target diameter is one.

### PT-03: pay approximation and measurement errors separately

**PROVED LOCAL.** Suppose the true data satisfy
|(Fp)_j−y_j|≤ε_j. For any supplied coefficient vector c,

$$
\boxed{
|t\cdot p-c\cdot y|
\le
\|t-F^\mathsf Tc\|_\infty+\sum_j|c_j|\epsilon_j.
}
$$

This follows by adding and subtracting c·Fp. With common uncertainty ε,
the noise term is ε||c||₁. A perfectly separating filter bank can therefore
be unstable when reconstructing the desired target requires large
coefficients.

For a one-sided conclusion, a pointwise inequality t≥Fᵀc−η gives
t·p≥c·y−η−∑|c_j|ε_j. It may be much cheaper to certify one lower
bound than to reconstruct p.

These statements remain valid if authenticated exact dynamical constraints
are added as rows. In a finite invariant-measure problem, for example,
rows g−g∘T have known expectation zero. The constraints must actually
hold in the claimed domain; a finite empirical orbit has endpoint errors.

## 3. PT-04: what a triple filter recovers

**CLASSICAL SPECIALIZATION, with an elementary local proof.**

Let f be a real or complex signal on G=Z/q. Use the unnormalized DFT

$$
a_h=\sum_{x\in G} f_x e^{-2\pi i hx/q}.
$$

The power and bispectrum are

$$
P_f(h)=|a_h|^2,\qquad
B_f(h,k)=a_h a_k\overline{a_{h+k}}.
$$

Assume every a_h is nonzero. If g has the same power and the same
bispectrum, then g is a cyclic translation of f.

**Proof.** Let b_h be the DFT of g and z_h=b_h/a_h. Power equality gives
|z_h|=1. Bispectrum equality gives
z_h z_k conjugate(z_{h+k})=1, hence z_{h+k}=z_h z_k.
In particular z_0=1, z_h=z_1^h, and z_1^q=1. Thus z_h is a character
of G. Multiplication of the Fourier coefficients by that character is
exactly a cyclic translation of the signal. ∎

This is the precise sense in which phase relationships on triangles can
remove ambiguities that survive pairwise intensity. It describes algebraic
phase transport, not physical quantum interference.

**Anchoring.** A known nonzero Fourier coefficient at h=1 fixes the
remaining translation. More generally, authenticated coefficients at
indices generating Z/q do so. A mass measurement at h=0 does not fix
translation; an anchor at h alone leaves gcd(h,q) possible shifts.
A source anchor can be used only after its map into this translation
action has been declared and verified.

The primary phase-retrieval source [S1] proves broader support-dependent
identification results. The theorem above uses the stronger full-support
hypothesis to make every division and every character relation explicit.

### Support zeros are structural, not a numerical nuisance

Let S={h:a_h≠0}. Power data reveal S. Bispectrum observations constrain
phase ratios only for h,k,h+k all in S. Define the finitely generated
abelian group

$$
\mathcal U(S)=
\langle e_h,\ h\in S\mid
e_h+e_k=e_{h+k}\text{ whenever }h,k,h+k\in S\rangle.
$$

Relative phases are characters of this group. There is a natural map
σ:𝒰(S)→⟨S⟩⊆Z/q, e_h↦h. Translational phases are exactly the
characters that factor through σ. Thus, for arbitrary complex signals on
this fixed support, completeness up to translation holds precisely when
ker σ=0. Every character of the cyclic subgroup ⟨S⟩ extends to Z/q.
Characters of finitely generated abelian groups separate points, which
proves the converse.

For nonnegative signals a subset of these phase choices may be
inadmissible; the explicit positive example below shows that positivity
alone does not repair every support defect. For real signals with symmetric
support containing zero, the triangle relations already include
z_{-h}=conjugate(z_h).

The exact code reports the rational rank of the relation matrix only.
A deficient rank detects continuous freedom. A full rational rank does
not exclude extra finite torsion, so it is deliberately **not** reported
as a complete support certificate. A graph-connectivity slogan would
lose this distinction.

The separate [phase audit](PHASE_AUDIT.md) supplies a concrete torsion
receipt: on Z/21, take S={0,1,2,4,8,11,16}. Apart from zero, the supported
triangles form the doubling cycle
1→2→4→8→16→11→1. Consequently every generator is a multiple of e_1
and the final relation is 64e_1=e_1, giving 𝒰(S)=Z/63. The natural
map to Z/21 has kernel Z/3 even though the relation matrix has full
rational rank seven. The phase assignment with exponents
(e_1,e_2,e_4,e_8,e_16,e_11)=(1,2,4,8,16,32) modulo 63 respects
every supported triangle but cannot be a translation character on
Z/21, since 21e_1 is nonzero modulo 63. This is a complex-signal
countermodel; positivity is not asserted. The regression test checks
the triangle relations in exact modular integers and rejects every
translation, without floating phases or a numerical rank tolerance.

## 4. Exact hostile controls

### PT-05: complete power data can hide additive existence

**PROVED LOCAL / VERIFIED FINITE.**

In Z/12 let

$$
A=\{0,1,4,6\},\qquad B=\{0,1,3,7\}.
$$

For either indicator, the cyclic difference counts C(s)=∑_x f_x f_{x+s}
are

$$
(4,1,1,1,1,1,2,1,1,1,1,1).
$$

Their complete power spectra are therefore identical. But the ordered
additive representation count R_f(n)=∑_x f_x f_{n-x} satisfies

$$
R_A(3)=0,\quad R_B(3)=2,\qquad
R_A(5)=2,\quad R_B(5)=0.
$$

The distinction is elementary:

$$
\widehat C(h)=|a_h|^2,\qquad
\widehat R(h)=a_h^2.
$$

Autocorrelation retains a difference; additive representation requires a
sum. Losing phase can therefore erase even zero versus positive additive
support. Third correlations distinguish these two examples.

This is an exact finite analogue of a Goldbach observation defect. It is
not a counterexample to Goldbach, nor does a filter preserving phase prove
that the prime sum coefficient is positive. The sets are a classical
homometric pair [S2]; all counts used here are independently recomputed.

### PT-06: all triples can still alias a support-defective interior

**PROVED LOCAL / VERIFIED FINITE.**

In Z/6 take

$$
f=(28,21,7,0,7,21),\qquad
g=(16,3,1,12,25,27).
$$

Both are nonnegative and sum to 84. After division by 84 they are
probabilities. Their second correlations are exactly

$$
(1764,1470,882,588,882,1470),
$$

and their entire third-correlation tables agree. Hence their complete
power and bispectra agree. They are not translates: f has a zero
coordinate and g has none.

Both Fourier supports are S={0,1,5}. Its triangle constraints say
e_0=0 and e_5=−e_1 but never impose 6e_1=0. Thus 𝒰(S)≅Z, while
⟨S⟩=Z/6. A continuous extra phase survives.

One direct parametrization is f_x=14+14cos(πx/3), and

$$
g_x=14+2\cos(\pi x/3)-8\sqrt3\sin(\pi x/3).
$$

The two oscillations have equal amplitude 14. With this support, every
nonzero triple-frequency relation either includes zero or pairs 1 with
−1, so the phase cancels. This proves the equality of the entire
bispectrum; the code also verifies the third tables directly in integers.

### PT-07: a sharp obstruction to stable inversion near Haar

**PROVED LOCAL; a specialized conditioning theorem, no priority claim.**

On Z/3 set

$$
u=(14,-7,-7),\quad v=(2,11,-13),\quad
p_\epsilon=\tfrac13\mathbf1+\epsilon u,\quad
q_\epsilon=\tfrac13\mathbf1+\epsilon v,
\qquad 0<\epsilon\le1/100.
$$

Both p_ε and q_ε are strictly positive probabilities with full Fourier
support. Their means and power spectra agree. For every ε in this
interval,

$$
\boxed{
\min_{s\in Z/3}\|p_\epsilon-\tau_s q_\epsilon\|_1
=18\epsilon,
\qquad
\|C_3(p_\epsilon)-C_3(q_\epsilon)\|_\infty
=3078\epsilon^3.
}
$$

**Proof.** The two centered vectors have the same second-correlation
table (294,−147,−147). The ℓ¹ distances from u to the three translates
of v are 36,54,18. Their third tables are

$$
C_3(u)=
\begin{pmatrix}
2058&-1029&-1029\\
-1029&-1029&2058\\
-1029&2058&-1029
\end{pmatrix},
\qquad
C_3(v)=
\begin{pmatrix}
-858&-1191&2049\\
-1191&2049&-858\\
2049&-858&-1191
\end{pmatrix}.
$$

For a zero-sum vector w on Z/3 and c=1/3, expansion gives

$$
C_3(c\mathbf1+\epsilon w)(s,t)
=3c^3+c\epsilon^2
\big(C_2(w)(s)+C_2(w)(t)+C_2(w)(t-s)\big)
+\epsilon^3 C_3(w)(s,t).
$$

The constant and quadratic parts agree, and the linear part vanishes.
The largest cubic table difference is 3078. Nonzero Fourier modes
have magnitude 21ε; the zero coefficient is one. This proves every
assertion, including full support. ∎

Consequently there is no uniform inverse Hölder estimate with exponent
greater than 1/3 from mass, power and third correlation to the signal
modulo translation in any neighborhood of the uniform probability.
Indeed, such an estimate would require
18ε≤C(3078ε³)^α for arbitrarily small ε, impossible for α>1/3.
In particular, no uniform Lipschitz constant survives. The same exponent
obstruction holds for bispectrum data because the finite double Fourier
transform changes norms by fixed constants.

This is compatible with local inverse-function estimates at a fixed
nondegenerate signal. The problem is uniform conditioning as nonzero
Fourier modes approach zero. For the π program this is a relevant
distinction: the desired limiting law is exactly the law where all
nonzero Fourier modes vanish.

The obstruction does not prove that an inverse estimate with exponent
exactly 1/3 is achievable for every nearby signal. It proves the stated
failure of every larger exponent; the constants in the exhibited family
are exact.

## 5. Reading the boundary without reconstructing everything

A calibrated coherent reference can reveal a scalar amplitude a from
intensity measurements. For complex a,b,

$$
|a+b|^2-|a-b|^2=4\operatorname{Re}(a\overline b),\qquad
|a+ib|^2-|a-ib|^2=4\operatorname{Im}(a\overline b).
$$

Known b≠0 then determines a. This requires the operational ability to
form those coherent combinations; it is not provided by separate
intensity observations of a and b. A filter on the observation and an
intervention changing the arithmetic source are different contracts.

This elementary polarization identity and PT-01 give the useful reading
of the user's “correct order and twist”:

1. Declare exactly what can be observed and coherently combined.
2. Compile the desired target into those observables.
3. If compilation fails, produce the indistinguishable pair.
4. If it succeeds, pay the approximation, measurement and conditioning
   costs before asserting the target.

Complete identification is sufficient for every well-defined property
constant on the residual gauge class; it does not automatically provide
an effective or short proof of every property.

## 6. The source-selected statistical cut remains explicit

For the authentic completed BBP orbit
Y_n=16^nπ/16, write μ_A for the empirical law on A≤n<2A.
The R0 target can be expressed as a positive lower bound

$$
\liminf_{A\to\infty}
\mu_A\big(1-\cos(2\pi x)\big)>0.
$$

It is therefore enough to certify **this one target**, without inverting
every Fourier phase. A possible dual contract is:

- Prove uniformly on an authenticated admissible carrier that
  1−cos(2πx)≥∑_j c_{A,j}f_{A,j}(x)−η_A.
- Establish, from the original source and literal zero boundary, an
  all-large-A bound
  ∑_j c_{A,j}μ_A(f_{A,j})≥δ+η_A for some δ>0.
- Pay certified source-tail, cell, measurement, and endpoint errors
  within the positive margin.

Then R0 follows immediately. The first step is a checkable finite
certificate problem; the second is the missing source-selected
arithmetic estimate. Merely including the unknown target as one filter
does not solve it. Constraints valid equally for the coherent changed
seed cannot give this δ: that seed has completed orbit zero and target
expectation zero.

For full normality, proving |W_{A,h}|²→0 for every fixed nonzero h
**would suffice**: it implies W_{A,h}→0. Phase loss is not an
obstruction to that particular target once the requisite power decay is
actually proved. The finite power counterexamples above concern
reconstructing interiors and additive sum targets, not this elementary
implication. Likewise, R0 is a real-part saving from one, and must not
be silently strengthened to all-mode magnitude cancellation.

No finite noncommutative reconstruction theorem supplies the missing
decay by itself. A finite response model can be periodic, and a finite
rank observed block does not prove a global rank bound without a
structural closure or dimension hypothesis. The remaining cut is an
authenticated asymptotic estimate, not another representation of the
same unknown signed mean.

## 7. Reproduction, provenance, and next falsifiers

Files:

- [Exact implementation](phase_filters.py)
- [Exact calibration and mutation controls](test_phase_filters.py)

Run from this directory:

~~~sh
python -m unittest -v test_phase_filters.py
python phase_filters.py
~~~

The first recorded run passed 18 tests. It includes an independent
direct double Fourier transform of the integer/rational third table,
compared with a product-of-Fourier-coefficients implementation in
Q[z]/Φ_q(z); no floating trigonometry is used. All 30 full-support binary
signals on Z/5 are also checked against translation classes. This is a
calibration of the implementation, not the proof of the universal
full-support theorem.

The later recorded run passed all 20 tests after adding the exact Z/21
finite-torsion control and a public-input regression. The latter rejects
float, Boolean and string inputs to the target, approximate-certificate,
Fourier and triple-correlation interfaces while accepting exact Fraction
inputs. This run used the root constructor's tightened rational-input
validation; the audit agent added the regressions without editing that
implementation.

Adversarial next checks are explicit: remove a Fourier support hypothesis,
replace bispectrum by power, mutate a conjugation, omit the mass row,
let a dual coefficient grow while suppressing its uncertainty, or claim
a uniform inverse constant near Haar. Each changes a condition used in
a proof and is caught by a retained control.

### Primary and existing sources

**[S1]** Tamir Bendory, Nicolas Boumal, Chao Ma, Zhizhen Zhao and Amit
Singer, *Bispectrum Inversion with Application to Multireference
Alignment*, IEEE Transactions on Signal Processing 66(4), 2018.
[Author-hosted paper](https://web.math.princeton.edu/~amits/publications/1705.00641.pdf).
Proposition II.1 gives explicit support conditions for identification up
to cyclic shift; the discussion after it qualifies stability by the
nonvanishing Fourier hypothesis. The locally proved full-support version
above does not import any probabilistic noise-model conclusions.

**[S2]** Emmanuel Amiot and William A. Sethares, *An Algebra for Periodic
Rhythms and Scales*, Journal of Mathematics and Music 5(3), 2011,
pp. 149–169. [Publisher record](https://www.tandfonline.com/doi/abs/10.1080/17459737.2011.640469).
Example 9 in the [search-indexed manuscript](https://citeseerx.ist.psu.edu/document?doi=a6b49464326488d1f46344ffe490c735667a13da&repid=rep1&type=pdf)
records the homometric pair. Direct manuscript retrieval returned HTTP
403; no uninspected proof from it is imported. The independent integer
identities above are the authority for the specific receipt used here.

**[S3]** B. L. Ho and R. E. Kalman, *Effective Construction of Linear
State-Variable Models from Input/Output Functions*, 1966.
[NASA bibliographic record](https://ntrs.nasa.gov/citations/19670049337).
This supports historical attribution of finite-dimensional boundary
realization, not an imported proof for BBP.

**[S4]** Jean Berstel and Christophe Reutenauer, *Noncommutative Rational
Series with Applications*, Chapter 2, “Minimization.”
[Publisher summary](https://www.cambridge.org/core/books/abs/noncommutative-rational-series-with-applications/minimization/ACD53CC08C3CB9451564D3488D24FE22).
Minimal-representation similarity and Hankel-rank realization are
classical. A finite numerical rank observation cannot replace their
global finite-rank hypotheses.

Sources were checked during this round. The full proofs actually used
for PT-01–PT-07 are supplied in this file; no unread literature theorem
is silently made load-bearing.
