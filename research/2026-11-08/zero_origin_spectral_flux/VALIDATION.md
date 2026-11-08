# Executed validation and provenance — zero origin spectral flux

**2026-11-08; exact scope:** This checkout is a minimal working copy of the main `duck_bbp` source API (the local immutable `forcing`, `source_tail_budget`, `tail_interval` functions were copied as-is for execution), plus new files. It is **not a full SUCC clone** because the local environment cannot resolve `github.com` for `git clone`. The GitHub connector is used for authoritative code/file comparison and submission. The full native root suite, provenance script, observer and ordinal probes must run in GitHub CI or a complete checkout. No such pass is claimed from this local sandbox.

## Mandatory arithmetic and algebra checks

- `python -m unittest discover -s tests -p 'test_zero_origin_spectral_flux.py'`: **24 tests PASS** on Python 3.13.5 in this local package. Exact `Fraction` pole-source decomposition, channel chronology, floor-tail envelopes, independent Machin rational arctan, cyclic word marginals, depth-energy flux, linear arrival update, de Bruijn controls, temporal Parseval, coherent/periodic spectra and signed van der Corput comparisons.
- Original source: `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)` for n>=1; `U0=0`; no imported π digit array is provided. The positive three-channel decomposition is exact for every tested n; the paper proof is independent of tests.
- Independent calibration: Machin identity `π=16 atan(1/5)-4 atan(1/239)` with rational alternating-series remainder proves first128 digits coincide with the BBP-tail certified stream. The identities are classical inputs, not a new proof of π.
- 16,384-digit source certification: **16,384/16,384** unique digits; **0** additional tail-depth refinements were needed on this finite horizon. The source-only channel-history exact reconstruction is checked for **the first 1,024** steps; the remaining digits/orbit states retain full exact `Fraction` source update, not independent channel tracking.
- All energies, depth fluxes and linear-arrival signed work are exact rational `Fraction` values internally. Temporal FFT, mean complex phases and signed lag values use ordinary `float`/`complex` and are explicitly **numerical diagnostics**, with symbolic identities separately proved. No claim of rigorous complex interval bounds from binary float.

## Executed finite results

The N=8,192 development run gave E1=0.0015363693, E2=0.0303344727, E3=0.4964599609 and highest non-DC normalized temporal power=0.0011955903.

The extension protocol `PROTOCOL.md` was committed to the remote research branch **at `7a4afebec6f162992fde98280363ba71acd5a9d3` before** the N=16,384 run. The N=16,384 output digest in the working container is

`bc8889b46094103714d771706f8874dfd1550674d8b6d9af81b7e4b0d703ca0b`

for its complete deterministic `finite_receipt.json` UTF-8 bytes (canonical sorted pretty JSON with trailing newline). The earlier N=8192 receipt digest is

`fdd649d5523109fa5c6b68141b4a91ad0cd7438385cffe24e0686a476b978d4f`.

At N=16,384, source digits have E1=0.0006529093, E2=0.0152759552, E3=0.2445373535, and largest non-DC power=0.0006002976. Sixteen shuffle replicas were **exactly** permutations of the same BBP digit histogram; depth2 range [0.01321220,0.01735687], depth3 [0.23654175,0.25967407], temporal peak [0.00051235,0.00068765]. These data are finite and no p-value or rate inference was attempted.

- Balanced period16: E1=0, E2=15, E3=255; single h1 temporal spectral line of power1.
- Repeated deBruijn(3): E1=E2=E3=0, E4=15; periodic despite perfect lower-depth counts.
- Same-count sorted permutation: E1 identical to BBP, E2≈14.97923, E3≈254.16861, temporal peak≈0.98707.
- Coherent zero shadow: E1=15, E2=255, E3=4095, DC power1; illustrates why looking only at nonzero temporal modes misses coherence.
- Toy periodic-mode feedback: E2≈0.01593, E3≈0.26187, top line≈0.001019, worse than BBP and most matched shuffles on these overall measures. It is a declared simulated feedback process, *not* evidence for BBP dynamics.

## No-go, source-identity and further tests

Observed 16,384-digit energy decay resembles same-histogram controls. This does NOT show that the authentic orbit has a self-correcting spectral force; a process with independent digits has zero conditional signed work in the single-symbol historical simplex while still accumulating noise energy. Low-order energy/spectral fits and finite independent samples cannot prove normality. The target remains source-selected signed covariance decay, not the identity used to represent it.

**Reproduction:** `python research/2026-11-08/zero_origin_spectral_flux/experiment.py --n 16384 --depth 3 --shuffles 16 --out /tmp/zero_origin_16384`; compare the JSON receipt SHA256 above. The expected Python `random.Random` sequence is deterministic under the environment used, but the program's exact identities do not depend on its shuffle algorithm.
