# Acquisition, calibration, and carrier-relative truth

## 1. Four nonnegative phase settings

Use the forward proper aperture from CONTINUOUS_THEOREMS.md. Let epsilon be a
known amplitude in (0,1]. At a fixed translated location y, the oscillator phase
theta changes the real nonnegative probe weight to

`alpha^-1 1_[0,alpha)(s) [1+epsilon cos(2*pi*s-theta)]`.

The observed profile is

`Y_theta = R0 + epsilon Re(exp(i theta) R1)`.

At theta=0,pi/2,pi,3pi/2, exact demodulation gives

`R0=(Y0+Ypi)/2=(Ypi/2+Y3pi/2)/2`,

`Re R1=(Y0-Ypi)/(2 epsilon)`,

`Im R1=(Y3pi/2-Ypi/2)/(2 epsilon)`.

The agreement of the two DC reconstructions is a necessary consistency check.
If each real phase reading has error at most eta, the static error is at most
eta and each recovered quadrature error at most eta/epsilon. The combined
two-channel L2 error is at most `eta sqrt(1+2/epsilon²)` under uniform profile
error bounds. This is an instrument error, not an arithmetic truth probability.

The four readings must refer to the SAME law. This is supplied mathematically
by an immutable stored empirical history, or physically by simultaneous
channels, valid replay, a stationary source, or a separately quantified drift
model. The sequential random-reference alternative has its own theorem in
LOCKIN_AND_CONTROLS.md. The protocols are not silently interchanged.

## 2. Exact finite implementation

`SourceSnapshot` records a rational probability, source label, epoch and trace
hash. `WindowProtocol` records the finite clock, proper window and amplitude.
`PhaseFrame` binds those two fingerprints and a phase label to the complete
translated real readout. `demodulate` checks complete distinct phases, common
source/protocol and DC consistency before assembling the complex channel.

With zeta=exp(2*pi*i/m), omega=zeta^-L, the local decoder is

`p(y)=[zeta^-1 R1(y+1)-R1(y)-omega(R0(y+1)-R0(y))]/(omega-1)`.

The decoder then checks rationality, nonnegativity, total mass one, and exact
reanalysis of BOTH channels. The last check is essential: the positive inverse
alone admits incoherent extra channel signals. When an expected source snapshot
is supplied, its fingerprint and recovered probability must both match.

`bbp_snapshot(A,m)` uses the original integer conductor engine and bins the
source on [A,2A). `verify_bbp_snapshot` rebuilds that source and compares the
entire snapshot; a human-readable source label alone is never accepted as
authentication. These are digital mathematical source checks, not physical
attestation of a sensor or free access to the source.

## 3. Calibration with a declared instrument model

For one unknown common complex gain g on R1, total source mass supplies its
nonzero known channel mean. The code computes g exactly and inverts it using
the cyclotomic Galois norm. This is a finite field operation, not a claim about
BBP cancellation or an invocation of arithmetic Galois equidistribution.

A nonzero fixed gain can be removed. A zero gain loses the channel. Arbitrary
position-dependent gain is a larger instrument class: the explicit G4
even/odd control in LOCKIN_AND_CONTROLS.md is a realizable source substitution
with unchanged mean, so gain normalization and range checks alone cannot
authenticate it. An actual known reference fixture passed through the same
stationary instrument could identify g(y) pointwise; that access is an extra
assumption, not an inferred capability.

## 4. The user's requested truth output is retained

Let C be the declared admissible carrier/source class and q its complete
chosen observation. For a target P, the positive relative proposition is

`may_P(q(x)) iff exists y in C: q(y)=q(x) and P(y)`.

`must_P(q(x))` requires P on every admissible member of that fiber. The existing
PR541 resolver and explicit true/false witnesses retain these as distinct
claims. Completing a drive menu refines the observation fibers. It can remove
a false representative, decide a target without reconstructing unrelated
state, or preserve an indefinitely valid relative equivalence.

For noisy data z with a certified error epsilon, define the realized constraint
set `C(z,epsilon)={x in C: ||q(x)-z||<=epsilon}`. Existence and universal target
claims are taken over this set, with witnesses or target error bounds. Pairwise
closeness within epsilon is not transitive and is not called an equivalence
relation. Empty compatible sets are OUT_OF_MODEL, not vacuous target proofs.

The new H1 and interval inequalities turn a bound on observation error into
a bound on a target. For example, against Haar, a certified half-bed energy
upper bound E gives every arc's occupancy error at most

`min(1, 3 E^(1/3)/2^(5/3))`.

An interval-frequency tolerance larger than this bound is a proved finite
target on that admissible observation set. Proving this error vanishes on the
original source's every sufficiently large epoch remains a separate theorem.

## 5. Source-preserving drive semantics

Modulating probe weights and retaining the oscillator reference enrich the
observer's tests. A common additive input to a fixed linear source leaves
candidate differences unchanged, as PR542 already proves. A physical drive
that changes the BBP forcing or its seed changes the source problem.

The exact registered-clock identity `e(-h(x-theta)) e(-h theta)=e(-h x)`
restores the source frame. Erasing theta can make a locked source appear
uniform. The erased-clock fiber can legitimately contain a uniform model;
that is the relative truth claim. Source uniformity itself is not determined
by that fiber. Keeping the clock supplies the discriminator.
