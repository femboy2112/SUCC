# BBP lag/carry adversarial review and a finite-authentication no-go

**2026-10-24. Base:** `ea5f92bbc52468e55b597e52455f24bceedb47b3`.
**Authority:** paper proof and exact rational tests; no Lean declaration here.
**Normality of the actual selected source remains OPEN.** This is a scoped
failure of uniform finite-window inference, not independence from a formal theory.

## 1. Audit of the inherited bridge

Read: the complete handoff, SCE dossier and supplement, validation record,
production module, probe, tests, and exact collision receipt. The SCE-02
entropy proof retains the end-window shift error and diagonal pairs. Its
continuity function is used on the stated domain `d/N <= 1/2`. SCE-04's
factor-two transport retains wrap carries. The SCE-05 grid argument includes
the `Delta^2/L` identical-local-phase pairs. The SCE-06 product argument and
SCE-07 geometric decomposition of windows are coherent at paper level. No
defect in their conditional implication was found in this audit. This review
is not a new kernel proof or an independent recheck of every external source.

The old small diagnostic rows, including `p=97,M=16`, must not be called
observations at the canonical `c=2/5` scale: that prime's canonical `M` is 1.
At `M=1`, the literal radius is 1 and all pairs qualify; the small-ball
implementation deliberately accepts only radii below 1/2. This finite-domain
restriction does not affect the sufficiently-large-prime asymptotic statement.

The dyadic controls of pinned #259
`a777aa99f541df2a0e2a0b8d57fef3f0940e465c`, CSI-04/05/08, already preserve
all odd-primary circle data, authentic forcing, and prescribed finite odd
modular lift probes while spoiling a finite signed window. They explicitly
do **not** preserve literal integer carry histories. The result below adds
any fixed early literal carry prefix, an arbitrarily small initial change,
and exact maximal collision at the requested window, using finite rational
source sums only. It is a strengthening of that finite-control mechanism,
not a new proof that initial-state changes are possible.

## 2. Exact data and the theorem

Use the authentic rational forcing and selected states

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
y_0=0,\quad y_n=\{16y_{n-1}+r(n)\}.
$$

For an initial rational `delta` in `[0,1)`, denote the changed orbit by
`y_n(delta)` and its literal one-step integer carries by

$$
c_n(\delta)=\lfloor16y_{n-1}(\delta)+r(n)\rfloor.
$$

Let `J >= 0` be fixed, `D >= 1` an odd integer, `1 <= A <= B`, and `M >= 1`
an integer. Require `A > J`, and put

$$
\epsilon_J=\min_{1\le n\le J}\frac{1-y_n}{16^n}
\quad(\epsilon_0=1),\qquad
\beta_A=\frac1{(8A+1)(8A+2)}.
$$

Assume `2*16^(-A) < epsilon_J` and `beta_A < 1/(2M)`.
These are explicit, decidable finite rational premises.

**Theorem (fixed-carry-prefix saturation).** There is a constructive nonzero
rational `delta` and an integer `K >= B`, with

$$
0<\delta<2\,16^{-A},\qquad
\delta\in D\mathbb Z[1/2],\qquad 16^K\delta\in\mathbb Z,
$$

such that all of the following hold:

1. The complete forcing is unchanged at every time, and
   `c_n(delta)=c_n(0)` for every `1 <= n <= J`.
2. For every time `n >= 0` and **every odd prime**, all prime-power primary
   components of `y_n(delta)` and `y_n(0)` in `Q/Z` agree.
3. For unwrapped lifts
   `U_n(delta)=16^n delta + sum_{j=1}^n 16^(n-j) r(j)`,
   `U_n(delta)-U_n(0)` lies in `D Z[1/2]` for every `n`. Thus every prescribed
   odd prime-power divisibility in `D` is retained in the difference of the
   lifts, even when the lifts individually have poles at that prime.
4. Every pair in the window `A,...,B` has circular distance strictly less
   than `1/M`. Its scaled ordered close-pair count, diagonals included, is
   **exactly M**, the largest possible value.
5. For every `n >= K`, `y_n(delta)=y_n(0)` exactly.

Item 3 is **not** equality of arbitrary floor or carry readouts modulo `D`.
The theorem preserves the first `J` literal carries; later carries generally
change. The initial state is explicitly nonzero, so this is not membership
in the authenticated selected-source class.

## 3. Proof and rational construction

First, `epsilon_J > 0`, since every selected state belongs to `[0,1)`.
If `0 <= delta < epsilon_J`, then for `n <= J`,

$$
0\le y_n+16^n\delta<1.
$$

The identity `y_n(delta)={y_n+16^n delta}` follows by induction from the
common forcing. The displayed inequalities therefore give equality of each
literal one-step carry through time `J`; they do not merely compare
cumulative carries modulo an integer.

Define finite backward tails, all rational, by

$$
h_n=\sum_{j=n+1}^B16^{n-j}r(j),\qquad A\le n\le B.
$$

Thus `h_B=0`, `16h_n=r(n+1)+h_(n+1)`, and `0 <= h_n < t_n <= t_A < beta_A`.
Only positivity of the authentic forcing and its established Green-tail
bound are used here; no supplied digits of pi enter the construction.
Set

$$
\eta=\{-y_A-h_A\},\qquad \delta_* =16^{-A}\eta.
$$

The recurrence gives `y_n(delta_*)=-h_n mod 1` for `A <= n <= B`.
Choose the least `K >= B` with `16^(K-B) >= 2MD`, put `lambda=D/16^K`,
and perform **strict upward** rounding:

$$
\delta=\lambda\left(\left\lfloor\frac{\delta_*}{\lambda}\right\rfloor+1\right),
\qquad e=\delta-\delta_*.
$$

Then `0 < e <= lambda`, including when `delta_*` is a grid point. Also
`lambda <= 16^(-B)/(2M) <= 16^(-A)/2`, so
`0 < delta < 2*16^(-A) < epsilon_J`. This pays for the literal carry prefix
and proves that the changed initial state is nonzero.

The target phases have simultaneous real lifts

$$
z_n=-h_n+16^n e\in(-\beta_A,D16^{B-K}],\qquad A\le n\le B.
$$

That interval's length is
`beta_A + D16^(B-K) < 1/(2M)+1/(2M)=1/M`.
Circular distance is at most the distance of these chosen real lifts, so
every ordered pair qualifies, including when the lifts cross zero and the
representatives wrap between near-zero and near-one.

Finally `delta` has a power-of-two denominator and belongs to `D Z[1/2]`.
The exact difference `16^n delta` proves all odd-primary and modular-lift
claims. It is integral for `n >= K`, proving eventual equality. This proves
all five assertions without any asymptotic sampling argument.

## 4. Canonical-prime consequence and exact scope of the no-go

Fix `J,D` first. For all sufficiently large good primes `p=8u+1`, use

$$
A=u+1,\quad B=4u,\quad M=16^{\lfloor(2/5)\log_{16}p\rfloor}.
$$

The two rational size premises hold eventually: `A` tends to infinity,
`epsilon_J` is fixed, and `beta_A=O(p^-2)` whereas `M <= p^(2/5)`.
The constructed family therefore satisfies

$$
K_p(\delta_p)=M\ge p^{2/5}/16.
$$

Consequently **no bound `K_p <= p^epsilon` with any fixed epsilon < 2/5 can
hold uniformly over this observation class for all sufficiently large good
primes**. The class retains authentic forcing, every odd-primary component
at all times, any fixed finite odd-modulus lift probes, any fixed literal
carry prefix, and arbitrarily accurate initial-state proximity to zero.

This is the precise impossibility mechanism: the omitted dyadic initial
precision supports an expanding finite-window degree of freedom. It is not
an algorithmic undecidability argument. It does not say that the actual
selected `delta=0` fails the collision criterion, and it does not rule out
a theorem using its full initial-state commitment or the full carry history
through the observation window. Every **fixed** constructed `delta` eventually
has exactly the same future as pi's selected source; the counterfeit is
chosen anew as the prime window changes.

**Growing-prefix sharpening.** The result need not retain only a fixed
number of carries. For each `n <= J`, every denominator in the four-pole
forcing up to time `n` divides `(8J)!`; multiplication by powers of 16 and
integer floor subtraction introduce no denominator. Hence the reduced
denominator of `y_n` divides `(8J)!`, so

$$
\epsilon_J\ge\frac1{16^J(8J)!}.
$$

An explicit sufficient prefix budget is therefore

$$
2\,16^J(8J)!<16^A.
$$

For example the deterministic choice
`J(A)=floor(A/(16*log_16(A)))` satisfies this for all sufficiently large
`A`: `8J <= A` eventually, `(8J)! <= A^(8J)`, and
`J+8J log_16 A <= A/(16 log_16 A)+A/2 < A-log_16 2` eventually.
It grows on the order of `A/log A`. This is a sufficient bound, not an
optimal precision lower bound. Its finite premise can always be checked
using integers, without floating logarithms. The fixed observation class
can thus be replaced by this explicitly growing early carry record.

**Stronger linear-prefix bound.** Let `L(N)=lcm(1,...,N)`. The exact
denominator statement improves to `denominator(y_n) | L(8J)` for `n <= J`.
We give an elementary exponential estimate rather than importing a prime
number theorem. For every `n >= 1`,

$$
\frac{L(2n)}{L(n)}\ \bigm|\ {2n\choose n}.
$$

For each prime its exponent on the left is either zero or one. In the
second case a power `p^a` belongs to `(n,2n]`, and its term in the factorial
valuation of the binomial coefficient is
`floor(2n/p^a)-2 floor(n/p^a)=1`; all other terms are nonnegative. This
proves divisibility. Since `binom(2n,n)<4^n`, induction gives
`L(2^r)<4^(2^r)` (also valid at `r=0`). For the least power of two
`P >= N`, one has `P < 2N`, hence

$$
L(N)\le L(P)<4^P<16^N.
$$

Consequently `epsilon_J > 16^(-9J)` for `J >= 1`; `J=0` is separate and
already covered. The completely predetermined choice

$$
J(A)=\left\lfloor\frac{A-1}{9}\right\rfloor
$$

therefore satisfies `2*16^(-A)<epsilon_(J(A))`. Thus a **linear number of
initial literal carries** may be retained while the later prime window has
maximal collision. The constant `1/9` is sufficient, not claimed optimal.
This strengthening was suggested by the arithmetic track and independently
checked here; the two reviews share model family and are not external
scholarly referees.

The odd modulus may likewise grow if chosen before the control: the proof
works for **every finite odd D**, paying the explicit additional depth
`K-B=ceil(log_16(2MD))`. It does not preserve all odd-modulus unwrapped lift
congruences simultaneously for a single nonzero perturbation, and it does
not preserve the complete literal carry record through `B`.

The proof also does not establish that finite-observer limitations imply
independence of pi-normality from PA, ZFC, or any named theory. No such
metamathematical mechanism is asserted.

## 5. Exact finite certificate and adversarial calibration

Production construction:
`observational_succ/pi_carry_prefix_control.py`.
Independent replay:
`tests/test_pi_carry_prefix_control.py`, which evaluates the forcing through
its unified rational formula and evolves the altered orbit forward. It
does not reuse the production backward-tail lift calculation.

The preregistered requested large case is `p=2081`, `u=260`, `A=261`,
`B=1040`, canonical `M=16`, `J=8`, `D=17^2*41=11849`.
The exact construction chooses `K=1045`. The shared initial carry prefix is

```text
3, 2, 4, 3, 15, 6, 10, 8.
```

The prefix-cylinder radius is
`72441298374705525479/665391252333213642907031961600`.
The real phase enclosure is

$$
\left(-\frac1{4366010},\frac{11849}{1048576}\right],
$$

whose width is `25866950533/2289046650880 < 1/16`.
The exact sufficient factorial criterion also holds for `J=20` at this
same `A=261`; the independently evolved trajectories share those first
20 literal carries as well. The choice of initial perturbation does not
depend on `J` once its cylinder premise is verified.
The stronger universal lcm budget chooses `J=floor(260/9)=28`; the same
exact forward test verifies all 28 initial carries and the identical
constructed perturbation.
All `780^2=608400` ordered counterfeit pairs qualify. Independently counted
authentic pairs number `76544`, yielding actual finite `K=5888/2925`.
This difference is a finite certificate distinguishing source selection,
not a fitted exponent or a lower bound on the actual asymptotic `K_p(1)`.

Tests additionally check smaller windows by direct quadratic all-pair
enumeration, exact forward coalescence, all observed dyadic differences,
finite odd-modulus divisibility, strict input domains and insufficient
prefix/tail-budget rejection. A calibration example `delta=1/16` coalesces
at the first step but changes the first carry from 3 to 4; it rejects the
false inference that eventual equality alone preserves literal carries.

During construction one invalid-domain test incorrectly expected the
admissible tuple `(A,B,M,J,D)=(3,10,16,2,1)` to fail. The mathematical
domain was rechecked and the test was repaired, adding the actually
inadmissible prefix-radius tuple `(5,10,16,4,1)`. No production relaxation
was made to force that test to pass.

## 6. Lag-claim guards and the next useful discriminator

For a centered difference `D_n` in `[-1/2,1/2)`, the recurrence contains an
integer carry, not just the small forcing difference. If consecutive
differences have absolute value at most `tau`, and
`17*tau + |r(n+l+1)-r(n+1)| < 1`, that centered carry must be zero.
This is a valid local restriction. It does not bound how often the selected
orbit enters the shrinking interval that permits a long run. The negative
tail orbit from changed initial state `-t_0 mod 1` supplies an exact infinite
stable tracker for the same forcing; it violates initial zero. The rational
finite controls above preserve substantially more observations, including
the fixed early carry record, while retaining the same obstruction.

The next discriminator must use growing literal carry information, an exact
source commitment unavailable to this family, or a genuinely new estimate
of the selected orbit's visits. Bounding returns from all odd clocks plus
a fixed carry prefix is now refuted with an explicit source-class witness.
Even the displayed linear prefix is insufficient; a successful argument
must use information beyond that retained prefix or a mechanism that
specifically uses the exact initial value zero.

## 7. Independent audit of the certified interval instrument

The interval module's binary-splitting atan identity, alternating remainder,
integer outward rounding, BBP-tail residual and sorted interval pair sweeps
were read separately from their construction. No sign, wrap or threshold
defect was found on the stated domains. The compact oracle
`scripts/pi_lag_interval_independent_oracle.py` uses ordinary exact
alternating Fractions, an independently written four-pole state recurrence,
and brute-force ordered pairs for all tested endpoint assignments.
Its source-hashed receipt is `PI_LAG_INTERVAL_ORACLE.json`:
414 atan enclosures, 570 actual rational state enclosures, 511 accepted pair
certificates, 413 ambiguous pair cases rejected and 3,140 endpoint pair
checks. One intentionally low-resolution source enclosure was refused.
These are finite calibration results; the universal enclosure claims
depend on the paper bounds, not on the number of successful checks.
