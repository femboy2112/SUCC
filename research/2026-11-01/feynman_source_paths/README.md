# OPERATION FEYNMAN — exact source quantum path integrals

**Status:** research-only draft child of PR #443, original four-pole signed BBP source and literal `U_0=0` unchanged. π base-16 normality / RH remain OPEN. This is a rigorous mathematical quantum **model** built from source-authenticated affine dynamics, not a claim that number theory is a physical quantum system.

## Executive finding

The previous SUCC classical Hamiltonian `H_n=log(16) p(x+r(n)/15)` admits an exact unitary Weyl-quantized propagator on `L²(R)`. A finite time-sliced phase-space Feynman **oscillatory distribution** integrates to the original BBP affine map. A declared quadratic kinetic regulator gives a nondegenerate finite Gaussian/Fresnel path integral with explicit stationary phase, exact Gaussian covariance and convergence to the authentic operator. Fourier-bandlimited inputs have a new uniform-in-horizon regulator error `<epsilon*hbar*K²/510`.

The strongest negative test is equally important: **a fixed-width Gaussian initial quantum packet produces vanishing Fourier expectations for ANY completed orbit, including the provably nonnormal same-forcing `q=1/5` control**. Therefore wavepacket smoothing / generic unitary evolution cannot prove point-selected π normality. Selected seed resolution must shrink exponentially with the arithmetic horizon; the separate positive/Wick Gaussian regulator likewise requires `epsilon_N*16^(2N)->0` for point-seed character recovery.

A second constructive result: controlled coherent superposition of the first two BBP affine steps in opposite orders has a nontrivial exact quantum overlap with source commutator `12301/273`, hence an operational way to test history interference if one explicitly adds a controlled-order experimental model. This is not hidden in the deterministic BBP recurrence.

## Files

- `PROOFS.md`: assumptions, domain, exact propagator, finite Feynman integral and regulator, operator bound, false-positive and interferometer.
- `CLAIMS.md`: scoped local ledger and next falsification opportunities.
- `SOURCE_MAP.md`: typed source/quantum model/physical realization distinctions, counterseed firewall.
- `NEXT.md`: precise next source-selected proof obligation and research plan.
- `VALIDATION.md`: executable tests, known positive/negative controls, proofs-versus-probes caveats.
- `feynman_source.py`: exact Fraction arithmetic source, affine, stationary-phase, Fresnel covariance, spectral and Gaussian-point bounds.
- `finite_probe.py` / `FINITE_DIAGNOSTICS.json`: optional high-precision Gaussian-interference quadrature, explicitly diagnostic only.
- `independent_oracle.py`: separate rational source and direct covariance oracles.
- `tests/test_feynman_source.py`: root-discoverable focused regression methods.
- `FINITE_RECEIPT.json`: local finite receipts (not a symbolic proof authority).

## Reproduction

```sh
python -m unittest discover -s tests -p 'test_feynman_source.py' -v
```

Full-repository gates (must run in a complete checkout on exact branch head):

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

**Conventions**: use `\hbar_*` only as a chosen positive Fourier/action scale, never assert physical \(\hbar\) was derived; `epsilon` is a *declared* kinetic regulator; the original BBP source has one deterministic arithmetic history. No merged/main modifications authorized.
