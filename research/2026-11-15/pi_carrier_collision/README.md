# Source-coupled probabilistic detectors for pi

Continuation of [draft #641](https://github.com/femboy2112/SUCC/pull/641),
at parent 85a14bb68aeae31d3a2796350529fda9a5c39072. The author's collider
analogy asks for deliberately designed probabilistic forms which couple to
the actual BBP carrier, preserve its hidden phase structure, and make useful
observations increasingly reliable.

## The constructive result

Keep the literal four-pole source and U_0=0. The two adjacent-state taps

\[
(h-16K)U_n+KU_{n+1}=hU_n+K r(n+1)
\]

retain the target Fourier frequency h while adding an exactly known source
modulation. On a block B<=n<2B, the forcing nodes r(n+1) have spacing
asymptotic to 15/(256 B^3). This leads to a source-specific detector scale:
frequency spread of order B^3 resolves the neighboring clocks.

Choose an external Gamma--Poisson integer probe law of shape 2 and scale
Lambda comparable to B^3. Its source Gram has an explicit positive lower
bound. A bounded triangular integer law provides a second construction.
With O(B log(B/delta)) independent labelled probes, matrix Chernoff gives a
failure probability at most delta and a measurement-matrix condition
number at most sqrt(5), for the stated conservative constants.

There is an all-scale probability-one statement: allocating
delta_B=1/[B(B+1)] makes all but finitely many designs well conditioned,
almost surely. The event concerns detector faithfulness and is uniform
over all coefficient vectors and Fourier targets. It does not prove
that the recovered original phase average vanishes.

The exact finite frame transports directly to temporal Haar coordinates.
Its constant Haar coefficient is sqrt(B) times the original Weyl mean.
The full complex, clock-labelled response reconstructs those coefficients;
total output energy alone cannot locate the energy among them.

## The calibrated arithmetic target

Let F_c(K)=B^(-1)sum c_n e(K r(n+1)) with c_n=e(hU_n), and subtract the
locked reference coherently. With
D_B=E|F_c(K)-F_1(K)|^2 and population Gram deviation eta<1,

\[
\frac{B D_B}{2(1+\eta)}
\le A_B:=\frac1B\sum_n(1-\Re c_n)
\le\frac{B D_B}{2(1-\eta)}.
\]

For h=1 and uniformly eta<=eta_*<1, a positive uniform lower bound
on B D_B is exactly the R0 escape rung. This is a new calibrated readout
of the same arithmetic obligation, not an independent estimate of it.

Raw high-intensity energy is approximately 1/B for every unit phase vector,
including a locked source. A high central frequency without adequate
spread also fails: any finite-variance probe law has
lambda_min(G)<=2 pi^2 delta_B^2 Var(K). Thus Var(K)=o(B^6) cannot provide
a uniformly stable inverse for arbitrary coefficient vectors.

## A genuine source-sensitive amplification corollary

The inherited GB-12 theorem already supplies a weak signed loss on the
authentic interval (m,8m]. Beyond an unextracted onset, a uniformly chosen
phase followed by acceptance with probability
(1-cos(2 pi hU_n))/2 has success probability >1/(196m).

Taking ceil(196m log m) fresh trials gives authentic success >=1-1/m.
For the same-forcing counterseed -pi/16, the false-hit probability tends
to zero as O_h(log m/m^3), for fixed h. This separates the two sources
asymptotically using inherited arithmetic. Its growing trial budget does
not establish a uniform positive event rate or normality.

On dyadic shells the counterseed's single-trial rate is asymptotic to
7 pi^2/(98304 B^4). A sufficiently growing dose can therefore make even
this locked completed orbit produce a detection with high probability.

## Why Gamma rotation needs a retained clock

An independent Gamma phase multiplier attenuates a forgotten-clock mean by
(lambda/(lambda-i omega))^alpha. It can make a locked source appear to
cancel. Recorded clocks permit samplewise demodulation; dividing only the
mean by the multiplier pays an exact mean-square cost
[((1+(omega/lambda)^2)^alpha)-1]/N.

Concurrent [#640](https://github.com/femboy2112/SUCC/pull/640) is credited
for its complex-coherence Gamma channel and complementary quadratures.
Its quantum carrier is a separate declared model. The present Gamma
integer tap law is an external probe choice, not an identification of the
original arithmetic successor with a random quantum instrument.

## What was checked

- 211 focused tests pass, including 60 new tests.
- A standalone audit performs 6,622 exact checks without production imports.
- A preregistered numerical diagnostic uses exploration blocks B=4,8 and
  fresh holdouts B=13,29. Labelled reconstruction succeeds for authentic,
  locked, zero-mean and same-forcing counterseed controls. Numerical
  eigenvalues and phase means are labelled as diagnostics.
- Three bounded reviews check the final proof and its exact source domains.
- The [validation record](VALIDATION.md) gives the isolated inherited
  discovery result, required repository probes, raw logs, hashes and scope.

## Read and reproduce

- [Theorems PC-01--PC-10](THEOREMS.md).
- [Initial hole contract](HOLE_CONTRACT.md).
- [Reframe and novelty assessment](REFRAME.md).
- [Claim ledger](CLAIM_LEDGER.json).
- [Provenance](PROVENANCE.md).
- [Next signed estimate](NEXT.md).
- [Constructor notes](CONSTRUCTOR_NOTES.md).
- [Adversary notes](ADVERSARY_NOTES.md).
- [Translation and primary-source audit](TRANSLATION_NOTES.md).
- [Exact source frames](../../../observational_succ/bbp_collision_frame.py).
- [Random design budgets](../../../observational_succ/random_probe_frames.py).
- [Phase and detection controls](../../../observational_succ/phase_detection.py).

All additions are research-only. The work proves detector laws and a
corollary of existing signed arithmetic. R0, pi normality, an effective
GB-12 onset, a cheaper collective readout, and physical entanglement of
the BBP source remain open.
