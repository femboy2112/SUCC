# Operation Wavefront Oscillator — Main XIII / draft #344 continuation

**Status:** Research-only; additive to the existing Pisot/Hopf/arithmetic-relativity draft. The original four signed BBP forcing, its zero seed and previous provenance remain immutable. **π base-16 normality and RH remain OPEN**. All source/causal/quantum/GR statements are typed and scoped in the linked dossier.

## Start here

- [Full exact mathematical dossier](WAVEFRONT_OSCILLATOR_COMPLETION_AND_CAUSAL_INVERSE.md)
- [Source-conditioned two-register oscillator and decoder](../../observational_succ/wavefront_oscillator_completion.py)
- [Exact stage/source/hostile tests](../../tests/test_wavefront_oscillator_completion.py)
- [Deterministic Fraction receipt](../../scripts/wavefront_oscillator_probe.py)
- [Independent SymPy packet, source-integral, and decoder oracle](../../scripts/wavefront_oscillator_independent_oracle.py)
- [Independent SymPy chiral oscillator invariant graph](../../scripts/chiral_invariant_graph_oracle.py)
- [Research claim ledger](WAVEFRONT_OSCILLATOR_CLAIMS.json)

## Main results

1. **Source-exact wavefront completion**: the original Oily source is the stationary Neumann sum of a two-state triangular matrix with eigenvalues u,v≤1/2. Its integral is exactly π via the existing authenticated BBP/Oily identity, with explicit finite-grade error certificates. This does *not* show pi normality.
2. **Source-minimal causal two-stage realization**: the authenticated normalized grade law has nonzero rank-two Hankel minor at all x>0; x=0 is a pure two-unit delay. Two registers are necessary and sufficient among linear causal realizations.
3. **Exact local re-emission**: source W(t−2) is recovered by a second-order finite difference of E2(t),E2(t−1),E2(t−2). At the critical endpoint this is `4E2(t)−4E2(t−1)+E2(t−2)`. Sharp noise amplification is 9, and for m stages it is 3^m.
4. **Conditional maximum-entropy emitter**: two Bernoulli microchannels maximizing entropy under expected combined occupancy x have p=x/2; occupancy size-bias produces the two source rates u,v. Identifying these rates with geometric memory retention is an additional model assumption; maximum information *about the source* is not the same optimization as maximum emitted microstate entropy.
5. **Autonomous oscillator and complete invariant graph**: normalized chiral source `Q=√2 T` has exact order eight and is orthogonal in the correct standard real/imaginary basis; for all its phase states, the observer has a unique source-indexed stationary section `H Q=A H+B ell`. The non-normalized original T is a contracting source, so sustained emissions require a declared pump. The simple repeated original shell taps and the continuously rescaled chiral Q have **different** time means (0 and −√2), a normalization-gauge control.
6. **Negative high-depth result**: repeated uncorrected observers suppress non-DC Fourier modes; an infinite-depth cascade averages a zero-mean period-eight tap waveform to zero. The oscillator's attracting periodic response is *not* a universal information-complete observer, a physical horizon, or a signed Weyl estimate.

## Validation / provenance

Local exact-rational suite **31 tests: 30 passed, 1 skipped** (the latter imports the genuine Main XIII chiral module, unavailable in the mini-checkout; it is intended to run in this PR's GitHub checkout). Both independent symbolic oracles and the deterministic Fraction receipt passed. Check [validation receipt](WAVEFRONT_OSCILLATOR_VALIDATION.json). Hosted CI and full SUCC native suite are independent gates, not preclaimed.

Required follow-up after PR upload: verify full chiral passport import, run `scripts/verify_provenance.py`, full `python -m unittest discover -s tests -p 'test_*.py'` with `PYTHONPATH=.`, observer/ordinal source probes, and inspect hosted CI. Do not merge, tag, release, or publish without reviewed authorization.
