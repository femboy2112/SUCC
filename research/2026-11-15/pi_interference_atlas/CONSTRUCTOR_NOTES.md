# Source-labelled finite interference compiler

Date: 2026-11-15. Constructor bearing; written independently of the other
bearings' conclusions. Parent: #643,
`8097d9e802da1d83a615d8812e74279820f5ae7e`. Active contract:
[HOLE_CONTRACT.md](HOLE_CONTRACT.md). This constructor owns only this note,
`observational_succ/interference_forms.py`, and its corresponding test file.

## Verdict, dependency cut, and provenance

**PROVED finite algebra / implemented bounded instrument.** Every Hermitian
quadratic form over the Gaussian rationals has an explicit rational signed
decomposition into normalized one- and two-channel intensities. A declared
reference supplies both components of every complex linear response. Two
Hermitian decompositions supply every complex sesquilinear quadratic
response. Explicit source-character products extend the same construction
to finite Laurent-polynomial interactions.

This is a classification of a declared finite response grammar, with
normalization, sign, orientation and sampling costs. It is not a
classification of all mathematical experiments, a source distribution
theorem, or a source-specific arithmetic saving. R0, R1 and all-mode Weyl
cancellation for the original source remain **OPEN**.

The algebra is classical polarization and Gram algebra. The repository
already implements exact Gaussian polarization in
`observational_succ/collective_spectral.py` and transported two-wire products
in `observational_succ/twisted_pair_transport.py`. The former uses a
linear-first Hermitian convention; the present response matrix uses
conjugate-first `z* H z`. Only its strict Gaussian arithmetic is reused.
The original state is imported from
`observational_succ/bbp_binwindow_conjugacy.py`; that implementation checks
the canceled forcing against the native four-pole source. No inherited
source function or archived theorem is changed.

The source obligations are those of `docs/PI_NORMALITY_FRONTIER.md`,
especially Main XXV's ladder, and `docs/PI_FRONTIER_CONTRACT.md`, especially
the signed Weyl and Fourier-purity gates. The previous collision-frame
dossier supplies a separate way to recover source phases; it is not an
assumption of the finite compiler.

The confidence inequality below is the bounded-variable inequality of
Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*,
JASA 58 (1963), 13–30,
[doi:10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).
A [primary-paper scan](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf)
was located. The short proof below makes the exact constants used here
independently checkable; they are not a new concentration theorem.

## IF-01. Authentic source characters and the declared grammar

Fix, without alteration,

\[
U_0=0,\qquad U_{n+1}=16U_n+r(n+1),\qquad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

For a finite integer family `(k_n)` and rational reference turn `theta`, a
source character is

\[
\chi_{k,\theta}=e\!\left(\theta+\sum_n k_nU_n\right),\qquad
e(t)=\exp(2\pi i t).
\tag{1}
\]

Its source clocks and harmonics are labelled data. They are not independent
random variables. Empty support gives a declared reference `e(theta)`.
The implementation combines equal clocks, keeps the zero-source clock as
an explicit label when present, and records reference turns modulo one.
It does not claim that different labels always give different values.

**PROVED.** Products and conjugates are source-faithful:

\[
\chi_{k,\theta}\chi_{l,\psi}=\chi_{k+l,\theta+\psi},\qquad
\overline{\chi_{k,\theta}}=\chi_{-k,-\theta}.
\tag{2}
\]

Proof: substitute (1) and use the exponential addition law. The result
uses the same `U_n` at every repeated clock. Replacing repeated appearances
by independently redrawn states does not implement this identity.

For a fixed ordered tuple of `d` characters, write their values as
`z=(z_1,...,z_d)`. The first grammar permits Gaussian-rational row
coefficients `a_j`, intensities `|sum_j a_j z_j|^2`, and finite rational
signed sums of those intensities. A reference coordinate may be added
explicitly. A higher-interaction grammar additionally permits the products
and conjugates in (2) before forming those rows.

The mathematical identities hold on the indicated finite complex spaces,
and in particular on the authentic source values. Code fixture evaluation
is exact on Gaussian-rational values in the unit disk, but the fixture
values are **not authenticated by their labels**. The separate
`authentic_turns` function evaluates (1)'s turns using the inherited source.
Generic `e(U_n)` is not Gaussian rational. `quarter_turn_value` refuses
conversion unless the authentic phase is a quarter turn; it does not round
or substitute a fixture. Completed `Y_n`, digits, carries and prime clocks
are not silently accepted as this source type.

## IF-02. Exact classification and signed compilation

Let `H` be a `d` by `d` Hermitian matrix over `Q(i)`. Use

\[
Q_H(z)=z^*Hz=\sum_{i,j}\overline{z_i}H_{ij}z_j.
\]

For `i<j`, write `H_ij=a_ij+i b_ij`, with rational `a_ij,b_ij`.

**PROVED.** For all `z` in `C^d`,

\[
\begin{aligned}
Q_H(z)={}&\sum_i H_{ii}|z_i|^2\\
&+\sum_{i<j}\frac{a_{ij}}2
 \bigl(|z_i+z_j|^2-|z_i-z_j|^2\bigr)\\
&+\sum_{i<j}\frac{b_{ij}}2
 \bigl(|z_i+i z_j|^2-|z_i-i z_j|^2\bigr).
\end{aligned}
\tag{3}
\]

Proof: put `u=conj(z_i) z_j`. The Hermitian pair contributes
`2 Re((a+ib)u)=2a Re(u)-2b Im(u)`. The first intensity difference is
`4 Re(u)` and the second is `-4 Im(u)`. This proves the sign and
orientation in (3). The diagonal entries of a Hermitian matrix are real.

Normalize every two-coordinate row in (3) by two; its row modulus sum is
one, and its intensity is at most one whenever every `|z_i|<=1`. The
corresponding weights become `+/-2a_ij` and `+/-2b_ij`. Coordinate rows
already have intensity at most one. Omitting zero terms gives at most

\[
d+4\binom d2=2d^2-d
\]

normalized measurements. Their total absolute weight is exactly

\[
C(H)=\sum_i|H_{ii}|+
4\sum_{i<j}(|a_{ij}|+|b_{ij}|).
\tag{4}
\]

This decomposition requires no eigenvalues, irrational square roots,
positive-definiteness hypothesis or oracle for the value of `Q_H`. The
weights and rows are computed from the supplied matrix. The cost in (4)
is an explicit sufficient cost, not an optimal one.

Conversely, any finite rational signed sum

\[
\sum_\ell\beta_\ell |a_\ell z|^2
\]

has the Hermitian coefficient matrix

\[
H_{ij}=\sum_\ell\beta_\ell\overline{a_{\ell i}}a_{\ell j}.
\tag{5}
\]

Thus this grammar gives exactly the Hermitian quadratic forms. Arbitrary
nonzero rows can first be normalized by the rational upper bound
`sum_j(|Re a_j|+|Im a_j|)`, multiplying the outer weight by its square.
That normalization does not restrict the representable class.

The classification is of formal quadratic forms, not a claim that the
matrix is identifiable from one source trajectory. On all of `C^d`, the
Hermitian matrix is determined by its form. On the unit torus diagonal
differences of trace zero already vanish, and the particular source may
have additional identities or repeated labels. The compiler does not
solve a minimal-representation or source-identifiability problem.

## IF-03. Complex responses and the phase reference

Let `L(z)=sum_j c_j z_j` with `c_j` Gaussian rational, and let `rho` be a
declared unit phase reference. On `w=(rho,z_1,...,z_d)`, set

\[
H^{\rm re}_{0j}=c_j/2,\quad
H^{\rm im}_{0j}=-ic_j/2,\quad
H_{j0}=\overline{H_{0j}},
\]

with all other entries zero.

**PROVED.** These two Hermitian forms give

\[
Q_{H^{\rm re}}(w)=\Re(\overline\rho L(z)),\qquad
Q_{H^{\rm im}}(w)=\Im(\overline\rho L(z)).
\tag{6}
\]

Proof: each pair `(0,j)` contributes twice the real part of
`conj(rho) H_0j z_j`; `Re(-iu)=Im(u)`. Choosing the known reference
`rho=1` recovers the original components. Changing the reference changes
the measured orientation and must not be suppressed.

For an arbitrary complex matrix `K` over `Q(i)`, put

\[
H=(K+K^*)/2,\qquad J=(K-K^*)/(2i).
\]

Both matrices are Hermitian and `K=H+iJ`. Therefore
`z* K z=Q_H(z)+i Q_J(z)`, and (3) compiles both components. This is
implemented by `complex_quadratic_forms`. A term `z_i z_j` without
conjugation belongs instead to the explicitly lifted product grammar.

**Reference obstruction.** For every pure quadratic response,

\[
Q_H(e^{i\phi}z)=Q_H(z).
\tag{7}
\]

Consequently any collection or postprocessing of these responses alone
is blind to a common phase. It cannot recover an oriented nonconstant
linear response on a class containing `z` and all its rotations. A fixed
reference breaks this ambiguity because it is held fixed while the source
channels rotate. Rotating the reference too restores the ambiguity.

An unknown target value may not be supplied as the reference. The code's
default is the declared phase `e(0)=1`; a different source or rational
reference must be explicitly passed. Its availability and precision are
part of the observation assumptions.

## IF-04. Exact expectation, confidence, and error cost

Consider any normalized signed program

\[
Q(z)=\sum_{\ell=1}^L\beta_\ell I_\ell(z),\qquad
I_\ell(z)=|a_\ell z|^2\in[0,1],\qquad
C=\sum_\ell|\beta_\ell|.
\]

If `C=0`, the response is the known zero polynomial and needs no trials.
Otherwise draw a row `J` with the exact probabilities
`P(J=ell)=|beta_ell|/C`. Conditional on that row, use a Bernoulli response
`X` of success probability `I_J(z)`, and report

\[
Z=C\,\operatorname{sgn}(\beta_J)X.
\tag{8}
\]

**PROVED.** `E[Z]=Q(z)` and `|Z|<=C`. Indeed each row contributes
`(|beta|/C) C sign(beta) I=beta I`. Replacing the signed score by a
positive score estimates a different response. Rows of nonzero weight
cannot be silently removed from the selection support.

For `m` fresh independent trials with this fixed target and law,

\[
\Pr\{|\overline Z_m-Q(z)|\ge\epsilon\}
\le 2\exp\left(-\frac{m\epsilon^2}{2C^2}\right),\qquad\epsilon>0.
\tag{9}
\]

One proof of the constant is as follows. For a variable supported in
`[-C,C]`, the log moment-generating function of its centered value has
second derivative equal to a tilted variance. Every such tilted law is
still supported in `[-C,C]`, so its variance is at most `C^2`. Integrating
twice from zero gives `log E exp(t(Z-EZ))<=C^2 t^2/2`. Independence adds
these bounds over trials. Exponential Markov and minimization at
`t=epsilon/C^2` give each one-sided tail in (9); their sum gives the stated
two-sided bound. The variance bound follows from
`E[(Z+C)(C-Z)]>=0`, or its centered interval form.

Thus a sufficient count is

\[
m\ge\left\lceil\frac{2C^2}{\epsilon^2}\log\frac2\delta\right\rceil,
\qquad 0<\delta<1.
\tag{10}
\]

The implementation uses the exact integer
`L=ceil(log_2(2/delta))` and returns
`ceil(2 C^2 L/epsilon^2)`. Since `ln(2/delta)<=L`, this is sufficient
without floating logarithms. It reports a trial budget; it executes no
random trials. For a complex response, one may estimate both real
components to error `epsilon/2` and failure `delta/2`, then take a union
bound. No independence between those two completed estimates is needed
for that union bound.

Each normalized row's intensity is a specified mathematical observation,
not a primitive physical capability proved by the compiler. Implementing
it requires coherent phase access or an independently justified numerical
evaluation with its error charged. Source rational turns are computable;
this does not make their generally non-Gaussian phases free exact inputs.
Duplicating one random outcome `m` times does not satisfy (9). Adaptive
row selection requires a new conditional-unbiasedness and concentration
argument; the present code does not declare that argument automatically.

Two deterministic error bounds are also explicit:

1. If every reported intensity differs from its target by at most `eta`,
   then the compiled response error is at most `C eta`.
2. Suppose both the true and perturbed coordinates are unit phases, with
   turn errors at most `tau_j`. Put
   `b_lj=|Re a_lj|+|Im a_lj|`; the normalization gives `sum_j b_lj<=1`.
   Then

\[
|\Delta Q|\le
4\pi\sum_\ell|\beta_\ell|\sum_j b_{\ell j}\tau_j.
\tag{11}
\]

For (11), `|e(t+dt)-e(t)|<=2pi|dt|`; each row's amplitude error is
at most `2pi sum b_lj tau_j`, and both row amplitudes have modulus at most
one. The difference of squared moduli is at most twice the amplitude
error. Reference errors must be included. No independence of errors is
assumed. A product character's turn error must first include the sum of
the absolute harmonic-weighted factor errors.

## IF-05. R0, R1, weighted channels, Haar and purity

Let `w_j>=0`, `sum_j w_j=1`, `|z_j|=1`, and
`W=sum_j w_j z_j`. The following are distinct compiled responses.

| Response | Exact form | Positive intensity realization |
| --- | --- | --- |
| Oriented escape from `rho` | `1-Re(conj(rho) W)` | `sum_j 2w_j |(z_j-rho)/2|^2` |
| Pair dispersion | `1-|W|^2` | `sum_(i<j) 4w_iw_j |(z_i-z_j)/2|^2` |
| Mean energy | `|W|^2` | `|sum_j w_j z_j|^2` |
| Signed complex mean | `W` | the two referenced components in (6) |

**Proof.** Expand the squared distances. The oriented expression uses
the known unit modulus of both source and reference. The pair identity is

\[
\frac12\sum_{i,j}w_iw_j|z_i-z_j|^2
=\sum_iw_i|z_i|^2-|W|^2.
\tag{12}
\]

It becomes `1-|W|^2` on unit phases. This also proves the exact disk-fixture
interpretation used by the code. Its measurement mass is
`4 sum_(i<j)w_iw_j=2(1-sum_iw_i^2)`, while oriented escape has mass exactly
two. Both are usually cheaper than applying the generic signed compiler
to their full matrices. Independent index draws with replacement realize
the ordered sum in (12). Forcing the second index to equal the first
produces zero dispersion for every source.

On an actual shell, take `w_n=1/B` and `z_n=e(hU_n)`. At `h=1`, a positive
all-large-shell lower bound for reference escape is exactly R0 after the
established Green transfer. A positive all-large-shell lower bound for
pair dispersion is exactly R1: `limsup |W_B(1)|<1` iff
`liminf (1-|W_B(1)|^2)>0`. For example a fixed unit value `i` has oriented
escape one and zero pair dispersion. That is a free-phase calibration
example, not an asserted alternative orbit of the original source.

The same oriented response at `h=15` and `h=16^k-1` represents the signed
forms of `(CH)` and `(CH_k)`, respectively; their digit/carry equivalences
come from the existing ladder theorems and retain their separate source
and branch hypotheses. Compilation does not prove any of those lower
bounds. Nonuniform probability weights give weighted means; a signed
weighting instead belongs directly to the linear-response compiler and
its normalization must remain visible.

For unweighted `d`-point data and any unitary temporal transform whose
first row is the normalized constant vector,

\[
\sum_{j\ge1}|(Hz)_j|^2=d(1-|W|^2).
\tag{13}
\]

This is Parseval and the constant-coordinate formula, hence the same
pair-dispersion observable. Weighted orthonormal coordinates use square
roots of the weights, which need not be Gaussian rational; (12) compiles
the resulting quadratic response rationally without pretending those
square roots belong to the exact coefficient field. Temporal Haar here
is not the source-coordinate or prime-fiber Haar construction.

For a frequency window `L>=2`, let
`v_j=(1,z_j,...,z_j^(L-1))` and `A=sum_j w_j v_j v_j*`. Then

\[
\operatorname{tr}(A^2)-L
=2\sum_{h=1}^{L-1}(L-h)|W(h)|^2,
\qquad W(h)=\sum_j w_j z_j^h.
\tag{14}
\]

Proof: the diagonal entries of `A` equal one, and each off-diagonal at
distance `h` has squared modulus `|W(h)|^2`. Sum the squared moduli of all
entries; Hermitian `A` makes this `tr(A^2)`. The frequency lift and the
positive weights `2(L-h)` are implemented directly. Their total
measurement mass is `L(L-1)`. Thus confidence costs must account for the
chosen normalization and for a growing window; Gram positivity itself
supplies no small purity excess.

Finite mode fixtures such as the four quarter phases have zero first,
second and third Fourier means but fourth mean one. The tests use that
algebraic fixture to falsify a finite-mode-to-all-mode inference; it is
not represented as a genuine consecutive BBP orbit. The authentic
all-mode/all-large-scale obligations remain separate quantified limits.

## IF-06. Finite higher interactions: justified extension and boundary

A finite Laurent polynomial in primitive unit phases has the form

\[
P(z)=\sum_{k\in E}c_k z_1^{k_1}\cdots z_d^{k_d},
\qquad E\subset\mathbb Z^d\text{ finite},\quad c_k\in\mathbb Q(i).
\tag{15}
\]

**PROVED.** Declare each monomial in (15) as a product character using
(2), then compile the real and imaginary components of the resulting
linear response by IF-03. Conversely finite additions, products,
conjugations and rational Gaussian linear combinations of primitive unit
characters produce only finite Laurent polynomials. Squaring a row
modulus multiplies it by its conjugate and stays in the same class.
Ordinary polynomials in `z` and `conj(z)` reduce to this class because
`conj(z_j)=z_j^-1` on unit phases. These observations prove the declared
finite higher-interaction classification.

This extension requires joint access to each product's factors. It does
not infer a product probability law from individual marginals. For a
concrete discriminator, the uniform law on the eight sign triples has
the same one-coordinate and two-coordinate marginals as the uniform law
on the four triples of product `+1`. All means of degree one or two are
zero for both laws; the triple product has mean zero under the first and
one under the second. The implemented tensor-character fixture separates
them exactly. These are explicit joint-law controls, not claims about
actual prime signs or BBP phases.

Formal tensor dimensions can grow multiplicatively and product turn
errors add with the corresponding harmonics. The code bounds tensor
factor count and final channel count. It does not turn higher-order
access, phase multiplication or joint sampling into a free observation.

Not every named frontier observable is a finite Laurent polynomial.
Literal digit cells, integer carries, discontinuous parity, absolute CDF
defects and the minimum defining signed CDF overlap require their
separate certified input types, branch cells and/or additional operations.
A finite cell truth table can be analyzed after those inputs are supplied;
it is not obtained by silently replacing a digit predicate with a smooth
circle character. Infinite Basel tails, all-mode mixtures and asymptotic
limits likewise need their explicit tail and convergence theorems.
Completed Weil positivity or a different base's joining problem acquires
no pi implication from formal membership of a finite response algebra.

## IF-07. Source transport, frames, and the unpaid estimate

For a completed phase `Y_n=U_n+T_n`, the character word in (1) changes by
at most

\[
2\pi\sum_n |k_n|T_n
\tag{16}
\]

in complex value. This is a direct exponential Lipschitz bound. Applying
(11) transports a finite compiled response with all its coefficient,
harmonic and reference costs. A growing frequency or degree cannot be
covered by merely invoking a fixed-mode `O(1/B^2)` statement.

The earlier source echo can enter this grammar as the labelled character
`e((h-16K)U_n+K U_(n+1))`. The inherited recurrence identifies it with
`e(hU_n+K r(n+1))`. This statement reuses that source identity; the present
module does not duplicate the earlier polynomial recurrence compiler.
Promoting the known modulation to a source-character factor also avoids
pretending a general root of unity is a Gaussian-rational coefficient.

Stable frame inversion, when available, can supply the labelled complex
inputs of the present program with its explicit noise cost. Conversely
the program can prescribe a particular reference or pair comparison of
those inputs. Neither step proves that a signed target is small, that an
escape target is bounded below, or that a positive frame energy is
source-sensitive. The next verdict-changing lamp remains an authentic
source inequality for the compiled response that survives the declared
controls on every required scale.

### Independent check of root's positive all-mode mixture

After the core construction, root proposed the separate response

\[
E_B=\sum_{h\ge1}2^{-h}|W_B(h)|^2.
\]

This proposal is mathematically sound: nonnegative terms imply
`|W_B(h)|^2<=2^h E_B`, while a finite head plus the geometric tail proves
the converse implication from all fixed-mode Weyl limits. Thus
`E_B->0` is equivalent to the full Weyl obligation. Independent uniform
shell indices `I,J` with replacement and harmonic law `P(H=h)=2^-h`
give mean phase-click probability `(1-E_B)/2`.

The unnormalized cutoff satisfies
`0<=E_B-sum_(h<=L)2^-h|W_B(h)|^2<=2^-L`; normalizing a truncated harmonic
law changes the experiment. The law has finite first moment two. Since
`|W_Y(h)-W_U(h)|<=2pi h B^-1 sum T_n` and both means have modulus at most
one,

\[
|E_B^Y-E_B^U|\le\frac{8\pi}{B}\sum_{n=B}^{2B-1}T_n
<\frac{\pi}{8B^2},
\tag{17}
\]

using the inherited `T_n<1/(64n^2)`. Click-mean error is half this bound.
This check pays the summed growing-harmonic transfer explicitly. It is
an equivalent observable, not a new arithmetic bound. Root owns its
production implementation, concentration choices and broader synthesis.

## Implementation bounds and finite receipt

The implementation accepts strict exact integers, Fractions and the
inherited Gaussian class. Float, bool and string coefficients are
rejected. Finite tuple/list sizes are checked before expansion. The
declared ceilings are 32 channels, 4096 intensity terms, 32 source
factors, eight tensor factors, source clock 512, and absolute harmonic
1,000,000. A reference consumes one channel. Input rational bit lengths
are not uniformly capped: exact arithmetic time, memory and output size
also depend on those lengths. A potentially very large confidence count
is returned as an integer and is never allocated as a sample array.

Within the Hermitian dimension cap, the `2d^2-d` compiler bound fits the
term ceiling. No mathematical theorem is inferred from the runtime caps;
the paper algebra is for arbitrary finite dimensions. Tensor and source
operations reject results outside the declared executable budgets.

Predeclared tests use dimensions 1–8 for development, fresh dimensions
11, 13 and 17, and independent literal-four-pole source clocks 19–41.
Direct tuple-of-Fractions arithmetic checks dense complex forms against
the signed program; a separately constructed frequency Gram checks the
purity identity. Meaningful mutation controls detect reversed imaginary
cross-term signs, discarded signed weights, missing orientation,
duplicated pair indices, duplicated Bernoulli trials, finite-mode
impostors and a hidden third-order joint constraint. An exact binomial
tail checks a concrete confidence budget. Source phase values that
cannot be represented exactly in the Gaussian field are rejected.

Final focused execution, after the arbitrary-complex-matrix split:

```text
python -m unittest tests.test_interference_forms -v
Ran 25 tests in 0.479s
OK
```

Production and tests are frozen at:

| File | SHA256 |
| --- | --- |
| `observational_succ/interference_forms.py` | `e3ad03fe74f51da65603041dfb98ffa98a9bac005cbc3c26a81bb8acb41a8350` |
| `tests/test_interference_forms.py` | `29c32a4c319ebf8da27f1384fe8525dec08775fde6b97fb87ed25baa4c1243f6` |

Only the assigned new files were written. No full suite, branch change,
stage, commit or publication was initiated by this constructor. Root owns
the integrated verification and atlas publication. The finite tests are
observations within the stated regions; universal algebraic claims are
supported by the proofs above, and every source asymptotic saving remains
outside their conclusion.

## Bounded review of root synthesis — initial snapshot

On 2026-11-15 the constructor reviewed `THEOREMS.md` at SHA256
`9d1b3008c32fa56d017993d8ac8c3a435fa948f182bf44228f9f3242390b5850`,
prioritizing IA-01, IA-02, IA-04, IA-05, IA-06, IA-07 and IA-10.
The root detector module and its tests were read statically; this review
did not execute another test suite or edit those files.

No algebraic, cross-term sign or normalization defect was found in the
signed compiler, reference/pair clicks, Gamma(1, scale 1)-Poisson-plus-one
law, geometric tail, all-mode Green transfer, fixed-polynomial Fourier
bound or source-resonance formula. The sampling laws preserve independent
index draws with replacement, and the concentration calculation charges
the factor two in `1-2*mean(click)` correctly. The observation-consistency
claim is an infinite-experiment statement, not a finite normality test.

The exact antecedent was checked directly in
`research/2026-10-24/PI_SOURCE_COLLISION_ENTROPY.md`, SCE-01, section 3.
Its kernel is `3/(1+2|z-w|^2)=3/(5-4*cos(theta))` on unit-circle points.
Consequently its energy is exactly `1+2*mathcal_E`, as IA-05 states.
The all-mode energy criterion is inherited, not newly discovered here.

Three paper clarifications were requested for closure:

1. IA-02 must explicitly use unit phases. IA-01's disk domain includes
   zero, where negative character exponents are undefined; conjugation
   also equals inversion only on unit phases.
2. IA-06 must explicitly sample the U-based detector for its U-energy
   concentration statement and state positive `epsilon_B` and confidence
   parameters before their sampling budgets.
3. IA-10 should identify its conditional pair response as
   `E[Z_1*conj(Z_2)]` under the declared conditional gluing. For the
   carry response, the exact inequality
   `|C_tilde|^2<=sum_b p_b|m_b|^2` retains the valid one-way implication
   from conditional-energy decay to decoder decay. Merely implementing
   either observable supplies no decay, and the reverse implication
   between decay criteria is not valid in general.

The detector's public factory paths, rational-circle fixture convention,
cutoff accounting, inherited integer-filter validation and exact rational
transfer constants have no identified defect in this static review.
The fixture tests explicitly distinguish removed diagonals, phase
rotations, geometric-frequency tails and retained versus forgotten labels.
This paragraph does not claim to have run the root's tests or to have
audited every later statistical theorem or catalogue entry.

### Closing bounded review receipt — 2026-11-15

**PASS within the stated scope.** Readback of `THEOREMS.md` at SHA256
`00066c945a9e8896f09e08405ffb89172ac7542a7dc5c0f4fdf3453cd4f7ea5e`
confirms that all three requested corrections above are resolved:

- IA-02 explicitly restricts the character grammar to unit phases and
  distinguishes it from IA-01's optional disk domain.
- IA-06 explicitly uses fresh independent U-based trials, positive
  integer sample counts, positive errors tending to zero and confidence
  parameters strictly between zero and one.
- IA-10 explicitly orients the conditional cross product and states
  `|C_tilde|^2<=sum_b p_b|m_b|^2`, with the correct one-way implication
  between decay criteria and no decay inferred from merely constructing
  either readout.

The bounded proof review covers IA-01, IA-02, IA-04, IA-05, IA-06,
IA-07 and IA-10. The earlier exact SCE-01 antecedent check remains valid.
It is not a blanket review of every theorem, catalogue entry or the
integrated test suite.

The statically reviewed root detector files remain unchanged at:

| File | SHA256 |
| --- | --- |
| `observational_succ/universal_interference_detector.py` | `19deabb504a4072e80aff4c4a9485395a1b4a6880ad715b1c484db81a82d9392` |
| `tests/test_universal_interference_detector.py` | `57e7ac3022d93687dca1dc8d5e29d99efaf29e1ba54eec5813987dbc69ecd76b` |

No code or tests changed during this review, and no additional tests were
run. The constructor's frozen implementation and 25-test receipt above
also remain unchanged. Only this owned note was amended. The algebra,
source transfers and observation models retain their stated boundaries;
the original R0 and normality estimates remain open.

## Bounded canonical coverage audit — 2026-11-15

Compared only the current canonical files
`docs/PI_NORMALITY_FRONTIER.md` and `docs/PI_FRONTIER_CONTRACT.md`
against the 72-row `FRONTIER_TARGETS.json` snapshot with SHA256
`9c79e573ebcd30d8b934b8543eb5466c23f5ff5f45c90eef9097802a59cee083`.
This was a bounded document comparison, not a new archive census or a
claim that finite enumeration captures every possible proof route.

**Two coverage corrections were reported to root before this appendix:**

1. **Missing weaker-rung threshold gates.**
   `docs/PI_NORMALITY_FRONTIER.md`, section 9, “Thresholds in the canonical
   units of section 5,” explicitly gives shell thresholds
   `limsup D<1/4 => R1`, `limsup D<1/60 => CH`, and
   `limsup D<1/[4(16^k-1)] => CH_k` for specified fixed k. The same
   thresholds apply to `W_1(nu_B,lambda)`; the prefix thresholds are
   `limsup D_N<15/256 => R1` and `limsup D_N<1/256 => CH`.
   F18 records only `D->0` as a normality equivalence, while F20–F23
   record the destination rungs. The positive-threshold sufficient gates
   themselves are absent from the audited JSON. They require an explicit
   entry or nested target, with the weaker destination named. They must
   not be described as full-normality equivalences or sufficient
   conditions for full normality.
2. **Route C's arithmetic target needs distinct registration.**
   `docs/PI_FRONTIER_CONTRACT.md`, “Route C — source-selected four-bit
   Walsh / Fourier jet (#271),” asks for a nontrivial/power-saving bound
   on the selected `M_{1,2,3,4}`. F58's exact target is the finite Walsh
   identity and its classification is OBSERVER_ONLY. Its prose mentions
   an additional saving, but does not separately register that open
   selected arithmetic target or the canonical statement's incomplete
   rate/window normalization. Retain the valid observer identity and
   add or nest the selected bound as an auxiliary/underspecified
   obligation. The canonical wording does not establish a standalone
   full-normality implication from this one interaction.

The remaining named canonical mathematical gates have identifiable
coverage: Weyl/Basel and microscope in F01/F03/F04/F08/F09/F65; projector
defect and chronological overlap in F18/F66; parity/complement and
joining in F28–F30/F71; R0/R1/CH/CH_k and restricted-exponent debt in
F20–F23/F31; IMW/OSP/PSF in F36–F38; arrival/parity and signed decoder
in F48/F07; old Routes A/B/D/E/F in F51, F46/F49, F50, F71 and F72.
Their necessary, sufficient, conditional and separate-program
qualifications were retained. In particular F62 explicitly names R0
as the target of its conditional equivalence, so its EQUIVALENT label
does not silently claim equivalence to full normality under the stated
catalogue convention.

No catalogue, production or test file was changed, and no tests were run.
This receipt records the identified differences against the pinned
72-row snapshot; it is not a closing claim that those differences have
already been repaired.

### Canonical coverage readback — 2026-11-15

**Both reported coverage findings are resolved on readback.** The reviewed
catalogue has 74 distinct row identifiers and is pinned at SHA256
`3d0e1feaa86a7be589573d02764dd643f5eaf420b326de993c3241a75fc4b839`.
Its referenced map has matching SHA256
`6a109bb6975adee6c208c4db890198b87b51e3e156c71240fbf7f92c4619c553`.

F73 now states every shell and prefix threshold listed in the canonical
section, names the weaker R1/CH/CH_k destinations, preserves the interval
metric and strict all-large-horizon margin, and explicitly disclaims a
full-normality sufficient condition. F74 separately registers Route C's
selected top interaction, marks its rate/window normalization as
underspecified, and assigns AUXILIARY status without claiming a normality
implication. F58 remains the finite reconstruction identity. The map and
JSON agree on these corrections.

The corrected F52 entry also visibly retains every fixed nonzero h,
the existential positive delta_h, every fixed j, all integer shells,
and the raw two-time lag with its stated uniform tail transfer. This
readback records those qualifiers; it is not an additional proof audit
of the originating archive.

No further named, mathematically specified gate omission or relation
misclassification was found in the bounded comparison with
`docs/PI_NORMALITY_FRONTIER.md` and `docs/PI_FRONTIER_CONTRACT.md`.
This is coverage relative to those two documents and the declared
catalogue convention, not universal exhaustiveness of mathematics.
No production, test, map or catalogue file was changed by this
constructor, and no tests were run for this coverage audit.

### Final coverage PASS and freeze — 2026-11-15

**Bounded PASS; both constructor coverage findings are closed.** Final
readback pins `FRONTIER_TARGETS.json` at SHA256
`86855b345af42b52ad8c53deb00e6d4e45eb30c479f4c1970d9b518edd7bc42c`
and `FRONTIER_MAP.md` at SHA256
`6a109bb6975adee6c208c4db890198b87b51e3e156c71240fbf7f92c4619c553`.
Direct counts give 74 rows, 74 distinct identifiers and 42 distinct
source paths. F73 and F74 preserve the corrections verified above.

The final F60 entry now cites the inherited
`research/2026-10-27/BBP_ECHO_DELAY_TRANSPORT.md` rather than treating the
new atlas as an inherited source. Its presence in parent
`8097d9e802da1d83a615d8812e74279820f5ae7e` was checked with `git cat-file -e`.
This is a provenance presence check, not an additional theorem audit.
The mathematical coverage findings remain resolved after that correction.

This final receipt is restricted to the stated comparison with
`docs/PI_NORMALITY_FRONTIER.md` and `docs/PI_FRONTIER_CONTRACT.md`.
No universal exhaustiveness claim is made. No production or test file
changed and no tests were run during closure. This owned note is now
frozen; integrated validation and publication remain with root.
