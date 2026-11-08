# Validation — INFINITY THREAD

## Provenance, exact scope

Strict child branch: research/bbp-infinity-thread-mesoscopic-gluing-2026-11-06, pinned exact parent #530 SHA 9b53501e37f6bb9ab5bd6f63cadf4cbfc1607749. The original four signed BBP source and literal rational U0=0 are immutable. No edits to main, inherited frozen source contracts, archived proofs, Lean, production, workflows, source licenses, or release.

Preregistration first committed on the connected GitHub repository at 6dc9759cba17de24910700da4f7b8181e2889ed6, **before the new A=2048,4096 holdout run**. Already-seen exploration A=128,256,512,1024 was explicitly disclosed as non-blind. The analytic gluing theorem is universal algebra and was not statistically discovered.

## What was executed, and with what authority

Executed Python 3.13 stdlib, isolated local directory. The exact remotely stored Python code was byte-matched against locally run copies:

- probe.py remote & local Git blob SHA: **2f84201be3dd82797bdd95d5145d4ecd6af63327**
- test_probe.py remote & local Git blob SHA: **60197724eb1f4429ff6ca0e4f214f7997567a1b5**

Reproduction from this directory:

    python -m compileall -q probe.py test_probe.py
    python -m unittest -v test_probe.py
    python probe.py > FINITE_RESULTS.generated.json

**5/5 focused tests PASS** in 4.644 seconds, 0 failures/errors. Original rational source checks via combined A/D vs independently summed four poles n=1..256 PASS. Original literal-zero recurrence generates exact Fraction x_n through n=8191. The unit-modulus all-prefix gluing inequality was checked on constant, alternating, IID-seeded synthetic and original orbit finite samples, but its universal proof is analytic in THEOREM.md, not a conclusion of these tests. The dyadic martingale telescoping was checked on two synthetic complex arrays. The Poisson kernel Fourier normalization checked against its elementary closed form. The coherent periodic and H-shadow negative controls behave as predicted.

The preregistered A=2048,4096 exact-source samples have, respectively, mesoscopic Q=32 and Q=64, M=64..128 (65 horizons each). With Poisson t=1/2 and |h|<=12:
- original literal zero: partial P≈0.021933033343 and 0.021751152481;
- nonoriginal isometric H-shadow: partial P≈1.999415881886 and 1.999463800223;
- nonoriginal periodic β=1/17: partial P=1.99951171875 at both;
- synthetic IID calibration: partial P≈0.018430203463 and 0.023122515807.

The omitted |h|>12 Poisson tail is bounded **exactly** by 1/2048 for EVERY finite test. All printed character and energy values otherwise use floating complex arithmetic; none is interval-certified. This is finite pattern discrimination only; it does not imply that the source P tends to zero or obeys a contraction.

**Initial local replay time-out:** A first end-to-end container command timed out without producing a result file; subsequent segmented timing showed the original exact Fraction recurrence completed quickly, and rerunning the full exact committed code completed with results and clean 5/5 tests. The initial empty generated file was not used or cited as evidence.

## Explicit uncompleted gates

- The missing source-selected inequality IT5 or direct P_(2^k)→0 is UNVERIFIED for the literal zero seed.
- No full native SUCC 12k+ suite, root provenance/observer/ordinal scripts, external peer review, formal Lean, or exact-head GitHub CI authorization claimed.
- No claim that a positive source moment, finite gamma/silver analytic constant, exact 2-adic return clone, or finite signed calibration gives a real asymptotic saving.
- No claim of novelty priority against classical harmonic/Poisson kernel, Weyl, conditional expectation or martingale literature. IT1–IT4 are derived elementary criteria and source-focused organization.

## Next discriminating probe

Find a source-specific inequality bounding IT4's **joint signed real carry/denominator/source pair kernel** and show it implies P_(2^(k+1))<=ρP_(2^k)+o(1) on ALL large scales. The inequality must explicitly fail for the H-shadow and coherent wrong seed; choose h-independent Poisson energy or a valid summable all-h kernel. Frozen controls should include a nonnormal digit process with nontrivial pair separation, and fresh exact/interval signed probes beyond the calibration scales. Finite truncations cannot substitute for a uniform theorem.
