# Independent hostile review of the signal frontier

**Verdict: no correctness defect found in the reviewed paper statements.**
This is a separate assignment and implementation within the same model family,
with inherited repository context. It is not external scholarly refereeing.
The source cancellation gate remains OPEN.

## Reviewed claims and independent checks

- **PR1 selector:** independently checked the small-order prime count, Ford
  parameter range y<=sqrt(X), 2y<=z<=y², u=O(log(X)^(-1/2)), and domination
  of the rejected-prime count by the fixed-modulus PNT interval count for
  B<eta_F/2. The absent effective onset is disclosed. Independently read
  [Agrawal–Pollack Proposition4.3](https://www.pollack-math.net/nearprimitive.pdf).
  Its attribution to Ford is one theorem lineage, not independent support.
- **PR2–4:** the quotient X^m-xi^m has exactly the source coset as simple
  roots; constant remainder is necessary and sufficient for modulus-one
  phase locking. The lifting has multiplicity q=(p-1)/m, and D<m gives
  Dq<p, so the additive Weil degree/coprimality hypotheses apply. Independently
  read [Kowalski Theorem3.2, printed31](https://people.math.ethz.ch/~kowalski/exponential-sums-elementary.pdf).
  The finite actual-epoch p_A²>16A qualification prevents nonintegral local
  residues from being inserted into a finite-field polynomial. PR8 retains
  the signed resonant coefficient and separately charges approximation debt.
- **FD1–5:** checked the discrepancy bridge identity, cancellation of cell
  denominators including empty cells, sinc² averaging multiplier, centered
  marginal correction, and telescoping before charging depth errors. The
  finite origin-menu variation bound is uniform in M. It supplies a calibrated
  equivalent signal, not its decay.
- **FG1–6:** checked the three-point inverse, common-anchor curvature transport,
  alternating Fibonacci sign, two-resolution Richardson coefficient, and
  all constants in the u<=1/64 perturbation argument. The angle lift is safe
  because its error is at most1/15 and the true principal return is below2/5.
  Integer winding, source clock versus probe clock, and independent gauge
  controls are retained.
- **FC1–10:** checked the one-sided perturbed-grid count, circular endpoint
  cases, finite variation pairing, local-phase split preservation, disjoint
  short-arc operator bound, Fourier derivative Parseval factor, noisy-frame
  factor, and finite-band curvature multiplier. Fourier reconstruction is
  conditional on its declared finite-band probe; a full-profile tail is
  explicitly charged as noise. Phase-blind aliases, periodic completions and
  coherent wrong-seed controls retain the exact source distinction.
- **Root source event sweep:** inspected update direction, coincident events,
  zero endpoints, rational integration weights and outward interval arithmetic.
  Its bound comparison uses an upper enclosure of the error and a lower
  enclosure of the positive bound. Previously independent exact sweep
  comparisons are separate evidence, not rerun or re-counted here.

## New independent computational receipt

`oracle.py` imports no production or research theorem/oracle implementation.
Executed with one BLAS thread. Its numerical arithmetic is explicitly
**corroboration, not an interval proof**:

- 86,016 adversarial coordinate-noise cases at the maximum admitted
  u=1/64: all16^4 phase-direction assignments at the diameter return, and
  4,096 deterministic assignments at each of five golden return depths.
- Every declared gain, center, radius, curvature, recovered phase and return
  angle bound survived. The return-ratio bound was tested tightly: the
  maximum observed ratio to that bound is approximately0.999947.
- 24 independent sampling-frame cases, including near-Nyquist bandwidths,
  survived the operator and singular-value bounds. The circular discrepancy
  bound survived all nine Fibonacci clocks used.
- A q=13,15-unknown Fourier system has rank13: inadequate sampling remains
  an explicit failed inversion control.

Run:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/2026-11-08/signal_frontier/referee/oracle.py --output /tmp/succ-frontier-referee.json
```

`RECEIPT.json` pins the inspected proof and implementation hashes. The
Fibonacci implementation/oracle files were still being completed during
this review, so this review does **not** certify their later code or their
future receipt totals. It reviews the FC/FG mathematical statements and
its own independent probes. Later changes require their own scoped check.

## Surviving limitation, with concrete receipts

The exact coherent complement b=conjugate(a) has W=1 while the origin-averaged
or Fibonacci-acquired observer approaches its nonzero sinc² calibration.
The same fixed circle geometry accompanies the same-forcing real seed
-pi/16, whose Weyl means tend to1. Neither has been confused with the
literal rational zero source. Likewise P=-hX+c+(X^m-xi^m)Q is exactly resonant
and is deliberately retained by PR8. These controls demonstrate why the new
observer and local-polynomial theorems do not yet supply original-zero
signed covariance decay.

**Pi base-16 normality: OPEN. RH: OPEN.**
