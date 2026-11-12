# Indirect boundary observation: access, disturbance, and resolution

2026-11-12. **Status: classical finite operator identities with locally proved
specializations and exact controls.** No quantum model of BBP, physical
experiment, new quantum advantage, universal energy cost, formal undecidability
result, or arithmetic asymptotic is asserted.

The constructive interpretation of indirect observation is to provide a
calibrated coupling that transfers a previously hidden target to an available
readout. This changes the available observation map. It can make a target
observable while leaving other targets hidden; it can preserve some source
properties while disturbing others. Those are separate, testable claims.

The fresh link to this round is a quantitative one: a smooth indirect sensor
still has to supply the derivative budget required by the arithmetic-grid
certificate. Renaming the sensor a transducer does not remove that cost.

## 1. IT-01: the effective observation is the operational object

Let `H` be a finite-dimensional source space, `K` a meter space, and prepare
one fixed unit meter vector `a`, independent of the unknown source state
`rho`. Write `J psi=psi tensor a`. For a declared unitary interaction `U`
and meter effect `0<=M<=I_K`, the observed probability is

$$
p_M(\rho)=\operatorname{Tr}\!\left[U J\rho J^*U^*
(I_H\otimes M)\right]
=\operatorname{Tr}(\rho E_M),\qquad
\boxed{E_M=J^*U^*(I_H\otimes M)UJ.} \tag{1}
$$

The compressed operator is an effect: positivity follows from its quadratic
form and the upper bound from `J*J=I`. This is the Heisenberg pullback of the
readout, proved by trace cyclicity. A fixed mixed meter can be handled by a
partial expectation or a fixed purification; arbitrary unknown source-meter
correlations require another declared preparation map.

For any collection of allowed interactions and readouts, let `S` be the real
span of `I` and all their effective effects. Two source states are equivalent
for that experiment class exactly when they have the same expectation on
`S`. A Hermitian target `T` is determined by those probabilities for **every**
source density matrix iff `T in S`.

**Proof of the converse:** if `T` is not in `S`, choose a nonzero Hermitian
`Z` orthogonal to `S` in the trace inner product, with `Tr(TZ) != 0`.
Because `I in S`, `Tr Z=0`. For sufficiently small positive `epsilon`, the
matrices `rho_+=I/d+epsilon Z` and `rho_-=I/d-epsilon Z` are densities.
They agree on every effect in `S` but disagree on `T`. The forward implication
is linearity. This is the finite operator counterpart of target-relative
duality, not a new general reconstruction theorem.

At `U=I` the meter probabilities are independent of `rho`, and all effective
effects are scalar. A real interaction can enlarge `S`. Merely rearranging
or postprocessing the original scalar data cannot.

**Closed-access corollary.** Let `A` be a unital finite-dimensional star
algebra of accessible source operators. If every supplied interaction lies
in `A tensor End(K)`, then all the effects (1) still lie in `A`: expand the
interaction as `sum_j A_j tensor B_j`; the compression contains only
`A_j* A_k` multiplied by meter scalars. Adaptive protocols with Kraus
operators in `A` also stay in `A`, because branch effects are finite sums
of products in that algebra. States agreeing on `A` therefore agree on all
branch probabilities, including an adaptively chosen experiment tree.
Reaching outside this equivalence requires a genuinely additional accessible
coupling, not an amplifier built solely from the same closed algebra.

## 2. IT-02: an exact active meter with a remaining hidden sector

Choose real rational `c,s >= 0` with `c^2+s^2=1`, and use the controlled
rotation whose input isometry is

$$
W|0\rangle=|0\rangle|0\rangle,\qquad
W|1\rangle=|1\rangle(c|0\rangle+s|1\rangle).
$$

The meter click `M=|1><1|` has

$$
E_M=s^2|1\rangle\langle1|,\qquad p_M=s^2\rho_{11}. \tag{2}
$$

Thus an initially blind meter now measures a diagonal source property. Direct
partial traces give the retained source and meter states:

$$
\mathcal N(\rho)=
\begin{pmatrix}\rho_{00}&c\rho_{01}\\c\rho_{10}&\rho_{11}\end{pmatrix},
\qquad
\sigma_K(\rho)=
\rho_{00}|0\rangle\langle0|+
\rho_{11}|\eta_1\rangle\langle\eta_1|,
\quad\eta_1=c|0\rangle+s|1\rangle. \tag{3}
$$

Even full meter tomography is blind to the source's off-diagonal entries.
In particular `|+><+|` and `|-><-|` give the same meter state. A coupling
that reveals one previously hidden target is not automatically complete.

For the two source basis labels, the meter records are the pure states
`|0>` and `eta_1`. Their density difference is traceless and squares to
`s^2 I`, so its eigenvalues are `+s,-s`. Its trace distance is `D=s`.
The retained off-diagonal visibility is `c`, giving

$$
c^2+D^2=1. \tag{4}
$$

This is a standard two-record distinguishability relation, here derived
for the explicitly supplied isometry. **The particular click measurement
has probability separation `s^2`, not the optimal distinguishability `s`.**

At `c=3/5,s=4/5`, the meter carries information and the source's coherence
is reduced. Nevertheless, for the declared source Hamiltonian `H_source=Z`,
equation (3) preserves `Tr(rho Z)` for every source state, and the controlled
interaction commutes with `Z tensor I`. Disturbance of coherence therefore
does not imply a positive change of this source energy. This does not
declare the meter, control apparatus, or laboratory process cost-free;
their Hamiltonians and preparation resources were not modeled.

## 3. IT-03: a calibrated complete readout pays coupling and preparation costs

If a specified source rotation `R` is available before the coupling, the
effective effect becomes `R* E_M R`. Choose rotations satisfying
`R* ZR=P`, for each Pauli coordinate `P=X,Y,Z`. Equation (2) becomes

$$
p_P=\frac{s^2}{2}\left(1-\operatorname{Tr}(\rho P)\right),
\qquad
\operatorname{Tr}(\rho P)=1-\frac{2p_P}{s^2}. \tag{5}
$$

For known `s != 0`, the three expectations determine the qubit density.
A probability error at most `epsilon` gives coordinate error at most
`2 epsilon/s^2`. Weak coupling makes this particular inversion ill
conditioned. At `s=0` the readout is exactly constant and inversion fails.

The three probabilities require repeated fresh preparations, or a separate
validated ensemble model. Equation (5) does not reconstruct an arbitrary
single unknown quantum state from one specimen, and its rotations are
additional operational resources. Nor is one uncalibrated click sufficient
to identify source population and coupling separately: for example
`s^2=16/25,rho_11=1/2` and `s^2=1,rho_11=8/25` both give `p=8/25`.
This last counterexample concerns that single click channel, not all possible
meter tomography or additional calibration experiments.

## 4. IT-04: cancelling a matched background requires the actual order

If a known accessible unitary background `B` follows the informative
interaction `U`, applying `B*` before measurement restores the response of
`U`. Equivalently, measure the correctly transported effect. This is an
operational calibration statement. Subtracting two intensity readings is
not generally the inverse unitary, and an unavailable inverse has not been
implemented by writing its matrix.

Calibration errors have an explicit effect budget. For unitaries `U,U_hat`
with `||U-U_hat||<=epsilon`, the same fixed isometry `J`, and the same effect
`0<=M<=I`, adding and subtracting `U_hat* M U` gives
`||E_M-E_hat_M||<=2 epsilon`. Compression by `J` does not increase the
operator norm. An additional readout-effect error `delta` adds at most
`delta`, so every source probability differs by at most `2 epsilon+delta`.
In particular, using a calibrated inverse `B_hat*` with
`||B-B_hat||<=epsilon` leaves a compensated unitary within `epsilon` of
the desired informative interaction, before any separate implementation
error is added. Perfect knowledge of the background is not implicit in a
physical use of the ideal cancellation formula.

For simultaneous noncommuting evolution, cancellation is less trivial.
Let `H_0,A` be finite Hermitian matrices, and assume the background inverse
is available. The compensated propagator is

$$
R_g(t)=e^{itH_0}e^{-it(H_0+gA)},\qquad
\left.\frac{\partial R_g(t)}{\partial g}\right|_{g=0}
=-i\int_0^t e^{isH_0}Ae^{-isH_0}\,ds. \tag{6}
$$

The derivative follows by differentiating the matrix exponential through
Duhamel's integral. If `[H_0,A]=0`, exact factorization gives
`R_g(t)=exp(-igtA)`. Without commutation, the ordered transported coupling
in (6) must be retained; that factorization is not generally valid.

In an eigenbasis of `H_0`, the first-order response on entry `j,k` is
`-i A_jk integral_0^t exp(is(E_j-E_k)) ds`. For a nonzero gap it vanishes
when `(E_j-E_k)t` is a nonzero multiple of `2 pi`. For example a gap
`2 pi` is invisible at first order at `t=1` but visible at `t=1/2`.
Here visibility presumes a nonzero coupling entry `A_jk`. This is a precise
reason to use calibrated times and ordered filters.
**First-order blindness is not equality of the full finite-coupling
responses:** higher orders can remain informative.

Informative record retention is also different from reversing an interaction.
For the controlled rotation in Section 2, applying its inverse immediately
restores the full state. If the meter's computational-basis record is first
copied to a new inaccessible register, then applying only that original
inverse leaves the source off-diagonal entries multiplied by `c^2`, as a
direct three-register calculation shows. The retained record is part of
the physical channel; omitting it from the inverse does not erase it.

This distinction is already established in
[PR #601, CCH-01--05](https://github.com/femboy2112/SUCC/blob/774191e7679cd63c56bdb105541ce21c8ee27448/research/2026-11-12/prime_fixed_point_observer/COHERENT_CHANNELS.md):
exact preservation/recovery of arbitrary logical inputs requires the
inaccessible complementary channel to contain no logical information.
That source was inspected. The present record example is a finite
calibration and reuse, not a replacement or novelty claim for its theorem.

## 5. IT-05: indirect transduction retains a quantitative resolution budget

Now let `x` be a real parameter and consider a finite sensor

$$
p(x)=\langle a,U(x)^*M U(x)a\rangle,\qquad
\|a\|=1,\quad 0\le M\le I,
$$

with fixed input and readout. Suppose `U` is twice continuously
differentiable and unitary. Differentiating the product and applying
Cauchy--Schwarz gives

$$
|p'(x)|\le2\|U'(x)\|,\qquad
|p''(x)|\le2\|U''(x)\|+2\|U'(x)\|^2. \tag{7}
$$

For example, the two first-derivative terms are conjugates and each has
modulus at most `||U'||`; the second derivative has the two `U''` terms
and the term `2<U'a,MU'a>`. The same estimates hold for a fixed mixed
input by convexity.

For `U(x)=exp(-i tau H(x))`, with a finite C² Hermitian Hamiltonian family,
assume uniform bounds `||H'||<=h_1` and `||H''||<=h_2`. Duhamel's formula
and its derivative imply

$$
\|U'\|\le|\tau|h_1,\qquad
\|U''\|\le|\tau|h_2+\tau^2h_1^2.
$$

The second bound has one `H''` integral and two time-ordered `H'`
insertions; twice the simplex area `tau^2/2` gives `tau^2`. Consequently

$$
\boxed{|p'|\le2|\tau|h_1,\qquad
|p''|\le2|\tau|h_2+4\tau^2h_1^2.} \tag{8}
$$

For a boundary potential `V_n(x)=b_(n,0)+sum_j b_(n,j) p_(n,j)(x)`
with coefficient mass at most `B`, and sensors satisfying common budgets
in (8), its derivative bounds are at most `B` times the displayed sensor
bounds. If these potentials are intended to satisfy the BBP
[grid certificate](DUAL_CERTIFICATE_BARRIER.md), they must also satisfy
that certificate's necessary bound

$$
\max_{A\le n\le2A}\|V_n''\|_\infty\ge
\frac{8q_A^2(\eta-O_A/A)-4\pi^2}{257}.
$$

Thus a positive certificate with small endpoint oscillation forces enough
coefficient mass, interaction duration, or parameter variation in this
**declared sensor model**. A smooth indirect coupling cannot be assumed
to provide denominator-scale resolution for free.

The circle application requires periodic C² sensor responses or an explicit
lift and seam treatment. A periodic Hamiltonian family is sufficient for
periodicity; the theorem does not silently identify a nonperiodic parameter
with a circle coordinate. Parameter-dependent source preparation is another
cost: if the input is `rho(x)`, extra derivative terms occur. In particular

$$
|p'|\le\|\rho'\|_1+2\|U'\|,\qquad
|p''|\le\|\rho''\|_1+4\|\rho'\|_1\|U'\|
+2\|U''\|+2\|U'\|^2.
$$

Those terms cannot be omitted by putting the fine target information into
the initial state. All derivative statements concern calibrated finite
operators and their parameter dependence. They are not universal lower
bounds on physical energy, and they do not assert that quantum hardware
implements the arithmetic source or proves its signed estimates.

## 6. Verification and remaining obligation

[Implementation](intervention_transducer_probe.py) and
[tests](test_intervention_transducer_probe.py) use exact Gaussian-rational
matrices. The existing `arithmetic_tfd.Gaussian` scalar is reused without
modification; matrix contractions, partial traces, and effects are locally
implemented. Run from the repository root:

~~~sh
PYTHONPATH="$PWD" python -m unittest discover -s research/2026-11-12/boundary_filter_complexity -p 'test_intervention_transducer_probe.py' -v
~~~

**Observed:** the initial ten tests passed in 0.064 seconds, exit 0. They check a passive
blind port, the active effect, its remaining coherence blindness,
distinguishability versus click separation, source-energy preservation
despite coherence loss, three calibrated axes, inversion errors, background
reversal, retained-record failure, and malformed inputs. The derivative
and time-order statements have the written finite-dimensional proofs above;
these tests are not a numerical proof of them. A further exact small-rotation
test calibrates the operator-norm error payment; **all 11 tests passed**
in 0.058 seconds, exit 0, after that addition. No new native-suite,
hosted-CI, formal-kernel or external-referee result is claimed here.

The next arithmetic step is to exhibit a source-realized coupling/readout
whose effective effects retain the desired zero-selected target, and whose
response admits an independently proved uniform bound. Supplying an
informative finite transducer is a construction step; supplying the missing
BBP signed estimate remains a separate theorem.
