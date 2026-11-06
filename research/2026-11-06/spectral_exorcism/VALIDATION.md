# Validation and provenance — Spectral Exorcism

2026-11-06. Child branch pinned to SUCC PR #531 head 06b46d5715153412215947a0e9ee4800c9bd9a5f. Root AGENTS.md read. Original four-pole r(n), literal U0=0, archived contracts, Lean, main, workflow and license unchanged. Preregistration was committed at 207ab30c0574a07a2618a7e12fd55e711432dd89 **before** new finite samples.

Theorem SE1–SE6 is elementary mathematics derived in THEOREMS.md, not formally Lean-certified or independently refereed. Key all-scale error bound SE4 uses original positive source-tail summability and real Fejér kernel Lipschitz estimate, not any π digit normality assumption.

Executed locally in isolated Python with exact Fraction recurrence for n≤1023 and float complex Fourier diagnostics; source/original recurrence verified against four-pole formula in existing parent research. Finite outputs at N=256,512,1024, H=8,16,32 recorded in FINITE_RESULTS.json. Source orbit Fejér energies at N=1024: H8≈1.0084666, H16≈1.0140789, H32≈1.0253417. H-shadow energy escape at N=1024≈0.000024444; original≈0.9981767; periodic β=1/17≈0.1304955. Finite periodic Fejér H=16,256,4096≈8.5,128.50677,2048.5.

A local invariant script verified Fejér energies≥1, all 9 dyadic wavelet telescoping cases to float tolerance 1e-7, and sample horizon lists. This is **NOT** an execution of the complete newly committed test_probe.py byte-for-byte, so its 4 unittest methods remain **UNVERIFIED ON EXACT HEAD** until replay. The committed probe.py and test_probe.py are provided for reproducibility; no invented CI/Lean or test-count certification.

Commands from this directory:

    python -m compileall -q probe.py test_probe.py
    python -m unittest -v test_probe.py
    python probe.py > FINITE_RESULTS.generated.json

No full native 12k+ suite, root provenance/observer/ordinal scripts, Lean kernel, independent mathematical review or exact-head hosted CI reported as passed. **No source-selected uniform mesoscopic collision upper bound** has been proved. Any claim of π normality or RH is OPEN.
