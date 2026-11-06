# Validation — 2026-11-06 Original BBP Prime–Frobenius Spectral

## Exact provenance and permissions

Connected GitHub repository femboy2112/SUCC, additive child of PR #531 at exact pinned SHA 06b46d5715153412215947a0e9ee4800c9bd9a5f. Branch research/prime-frobenius-denominator-and-spectral-gap-2026-11-06. Root AGENTS.md consulted in prior parent research, no inherited source, U0, history, formal Lean, production, workflow, licensing, tag, main, or release edits.

Preregistration committed BEFORE first new finite holdouts at 5bf2668a948af77881b36fddcc26cf177eb8ab8c. Its already-seen n=10,p=23 red mismatch and n≤160 denominator checks were disclosed as calibration. Stronger n<p≤2n analytic extension was preregistered BEFORE fresh n=389..557 holdouts in PREREGISTRATION_PRIME_EXTENSION.md at 8631d43431f6d2ca119bc3ad9ef11f493bdeb8d2. PNT/AP theorem is external mathematical proof input, not finite inference.

## Local execution, 2 independent source oracles

All code Python 3.13 / stdlib, using fractions.Fraction and integer modular arithmetic for prime residues. Reproduce:

    cd research/2026-11-06/prime_frobenius_spectral
    python -m compileall -q prime_certificate.py full_prime.py spectral_probe.py test_prime_spectral.py
    python -m unittest discover -v -s . -p 'test_*.py'
    python prime_certificate.py > PRIME_BAND_RESULTS.raw.json
    python full_prime.py > FULL_PRIME_RESULTS.raw.json
    python spectral_probe.py > SPECTRAL_GAP_RESULTS.raw.json

**7/7 focused unit tests PASS**, 0 failures, 0 errors, stdlib compileall PASS. Four-pole combined rational A/D exactly agrees with independent partial fractions over n=1..558; exact rational U_n from literal U0=0. Test module independently enumerates all original linear poles at prime multiples p and calculates their principal parts, rather than importing closed Frobenius case coefficients. Also checked lcm source denominator containment and p>5 factor disjointness. Exact Galois Ramanujan formula calibrated on small odd moduli. Floats only used to display log ratios / complex phases; no finite real signed-energy certification is asserted.

**First holdouts** n=161,173,199,211,257,293,317,383; 1116 exact pU residues in bands (2n,4n] and (4n,8n−7] class1mod4, all PASS.
**Second fresh holdouts** n=389,401,433,463,509,557; 1847 exact pU residues in full bands (n,4n] and (4n,8n−7] class1mod4, all PASS. Five possible normalized coefficients each observed; no case retuned. The p19 predicted red failure n10..16 and restoration n17,18 also PASS.

Finite dyadic wavelet contrasts N=128,256,512,1024; h=1,2,3, original source vs H-shadow, β1/17 period-two and fixed seeded IID. **FLOAT DIAGNOSTICS**, not asymptotic proof or rigorous interval enclosure. Key h1 original gaps ≥1/4 at 7/7, 8/8, 6/9, 9/10 levels; known finite counterexamples to an across-every-level η=1/4 gap, so no threshold promotion. Nonnormal shadow nearly zero gap energy; periodic control one nontrivial level. The exact wavelet product identity is separately proved in THEOREMS.md.

## Exact GitHub source readback

Source code GitHub blob identity (SHA1, tested local git hash-object):
- prime_certificate.py: 027e82bd00d33e368025749dd28f64dd73e56006 MATCH.
- full_prime.py: 05b57872ad87b7327d0302c714e0473938149a63 MATCH.
- spectral_probe.py: b5ee0676f5fb6075cbfbbf3f5abd0000b87bbc56 MATCH.
- test_prime_spectral.py: 3db874037a04dfc915c8a7d2e38ebc4be24aca2f MATCH.

README / CLAIM ledger / finite compact results are reproducibility aids, not standalone asymptotic evidence. Raw Python JSON outputs are fully regenerable from exact GitHub scripts; compact FINITE_RESULTS.json retains the preregistered selection and statistics without falsely claiming byte-identical stdout.

## Remaining gates

Not executed locally on full repository: native SUCC 12k+ suite, scripts/verify_provenance.py, observer_foundations_probe.py, ordinal_succ_report_probe.py, formal Lean, external academic review. Hosted exact-head CI must be checked after PR opening. No all-scale source-selected Poisson contraction, real phase Weyl cancellation, π normality, RH or claim of original-world novelty.

Arithmetic theorems are locally proved from standard Euler/Fermat, prime-arc residue combinatorics, PNT/AP, and Ramanujan sums. Two private implementations of the same source do not count as independent outside referees.

**Exact source cleanup:** after the initial tests, replaced a redundant ternary p19 probe with the identical direct exact Fraction reduction and corrected a THEOREMS.md cross-reference; both revised Python blobs were rehashed locally against live GitHub, and the complete 7-test suite plus compileall were rerun cleanly at these final bytes.


## Additional exact character theorem and fresh finite calibrations

After initial PR #532 denominator/Frobenius audit, a new preregistration at [PREREGISTRATION_GALOIS_SELECTOR.md](PREREGISTRATION_GALOIS_SELECTOR.md) was committed before the character-table tests. **The algebraic Galois-selection theorem was already derived and was openly recorded as non-blind; tests check the proof, not discover it.** Theorem in GALOIS_SELECTOR_THEOREM.md uses orthogonality and Parseval in the finite group (Z/d_n)^× and the already proven PF-04 source denominator bound; real temporal cancellation remains OPEN.

Local standard-library Python:
    python -m compileall -q galois_selector.py test_galois_selector.py
    python -m unittest -v test_galois_selector.py
    python -m unittest discover -q -s . -p 'test_*.py'
    python galois_selector.py > GALOIS_SELECTOR_RESULTS.generated.json

**5/5 new tests PASS, 12/12 complete research-local tests PASS**, 0 failures/errors. Character table construction explicitly uses C2×C4 for d=15, prime primitive-root exponents for p∈{7,11,17}, orthogonality, inverse Fourier reconstruction of selected complex phase, Parseval, and signed/trivial mean mutation. Finite complex calculations use float and error tolerance <5×10^-12, not rigorous intervals. GALOIS_SELECTOR_RESULTS.json is a compact semantic digest, not byte-identical regenerated raw JSON.

GitHub blob readbacks match *tested* local git hash-object:
- galois_selector.py 54fdb76819a5e8015616aec39dd44538b382388d
- test_galois_selector.py 21d2fa239a094409c1864d7bc04d28ef240bab2c

This has not executed the full native SUCC suite or independent Lean kernel for the new theorem. No original-source π real Weyl saving is claimed.
