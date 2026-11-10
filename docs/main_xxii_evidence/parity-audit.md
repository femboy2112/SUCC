# Main XXII parity-cluster proof audit

Reviewed 2026-11-09, read-only against Git objects. This is a same-model proof/code audit plus separately implemented arithmetic oracles, not independent scholarly refereeing. No historical source file was edited.

| PR | exact head | disposition | reason |
|---|---|---|---|
| #571 | 1597ddab8c4dab909b84e698eb47008b5e3ae46f | INTEGRATE-SCOPED | Valid finite Haar/successor inequalities and sufficient moving-depth criterion; criterion remains unpaid for the source. |
| #572 | 259238b7d71277605b26ab0a391334b5891b0e3c | INTEGRATE-SCOPED | Exact full-CRT parity identity and hostile p-integral seed; local prime saving inherits conditional #554 analytic input. |
| #573 | c8763d74b0db0145f574db9bde67d922430080fa | INTEGRATE-SCOPED | Correct finite regression/descent; fit uses observed real complement and does not predict source cancellation. |
| #574 | df624aa98579303d3ca0e2a312e7ca6423f4a0c9 | INTEGRATE-SCOPED | Correct conditional two-fiber identification, sharp finite parity and precision bounds; asymptotic contrast is OPEN. |

## Proof bearing

* `research/2026-11-09/tenacious_d_haar/PROOFS.md` TDH-01..04: the source and target marginals of the same oriented de Bruijn edge law give H-L exactly. Expanding squares gives K_low=E_(j+1)-E_j and K_high-K_low=16^j(||p||²-||q||²). The finite chronological orbit difference is exactly the two endpoint atoms/N. The child-label difference multiplier has squared gap 2-sqrt(2+sqrt(2)) and maximum 4, with both attained on real perturbations of uniform laws. J5 has the correct finite-DFT normalization.
* TDH-05: the interval inverse-branch operator contracts W1 by 1/16; applying triangle inequality gives the stated 16/15 and 1/15 constants. Coupling within depth j+1 cells costs at most 16^(-j-1), and unmatched mass costs TV. Cauchy-Schwarz yields the stated sqrt(K_high)/2. Combined J9 is a valid sufficient inequality, not a proved source estimate. Its 16^j/N endpoint payment is essential.
* TDH-07: E_k>=16^k/N-1 follows for every N-atom word law. At 16^k near N² it forces order-N energy even for normal sequences. This is a finite-sample resolution floor, not an anti-normality theorem.
* `research/2026-11-09/pi_parity_pressure/PROOFS.md` PPP-01/02: writing the original forcing over its positive odd common denominator gives numerator parity n. For Q=lcm of reduced forcing denominators, A=QU has parity n. The complete prime-power CRT reconstruction is A mod Q=Q(sum k_m/m-ell). Reducing A-(A mod Q)=Q floor U modulo 2 gives floor U congruent n+sum k_m+ell. The authentic positive real future tail contributes epsilon. Thus completed real sign is exactly (-1)^(n+sum k_m+ell+epsilon). No prime power, global winding or real boundary may be dropped.
* PPP-03/04: selecting one simple-pole prime gives s=a*b. Fourier inversion for canonical odd-modulus parity has zero mode 1/p and l1 norm <=2+log p. Therefore the local mean bound follows only from the inherited all-nonzero-frequency character bound, with its analytic inputs and uniformity. This does not bound the Archimedean covariance.
* PPP-06: for N=qB+r the integer identity for E and excess is correct, including empty cells. Sparse B>N support produces the universal B/N-1 floor and nonnegative repeats.
* `research/2026-11-09/aphex_haar_feedback/PROOFS.md` APH-01: loss derivative V*beta-C and decrease eta*(1-eta*V/2)*(V*beta-C)^2 are exact. V>0 and 0<eta<2/V are needed. Gains are declared model parameters, not inferred physical masses.
* `research/2026-11-09/aphex_two_fiber_haar/PROOFS.md:7` explicitly requires both sign fibers. Then u_plus,u_minus exist, m=p_plus-p_minus, t=(u_plus+u_minus)/2 and beta=(u_plus-u_minus)/2. Direct two-point summation gives E[b]=t+m*beta, E[ab]=beta+m*t and Cov=(1-m²)*beta. This proves regression identification independently of the code.
* TFH-02 (`PROOFS.md:32`): P=beta+m*t and |t|<=1 prove |P-beta|<=|m|. Taking constant b=+1 saturates the coefficient 1 with any biased nondegenerate a, so the constant is sharp.
* TFH-04 (`PROOFS.md:63`): distributing the total mean absolute complement error epsilon among fibers gives |delta beta|<=epsilon/(2*p_min)=epsilon/(1-|m|). Perturbing only the minority fiber with constant sign attains equality. No claim about arithmetic cancellation follows.

## Adversarial bearing and exact receipts

1. Continuous e(8x) and digit parity differ already at x=1/32: digit parity is +1 and e(8x)=i. The parity step function has infinitely many nonzero real-circle Fourier frequencies congruent to 8 modulo 16. A single Weyl frequency is insufficient.
2. Uniform-on-even global canonical CRT representatives has exactly biased real parity while each fixed odd local marginal approaches Haar. The exact TV formula in PPP-07 is independently reproduced by counts in the tests. This defeats marginal-to-real descent absent the winding/section.
3. PPP-08 (`pi_parity_pressure/PROOFS.md:134`) constructs an A-dependent rational odd-denominator, p-integral seed from an original-source prefix. The unchanged forcing then gives completed phases strictly in (0,1/16) for the specified finite epoch, while the p-primary history and 2-adic clock match the zero seed. Hence s=+1, b=a, u_plus=1, u_minus=-1, beta=1 and conditional contrast=2 whenever both fibers occur. Regression minimum loss is zero. This is a finite-epoch family, not one fixed rational seed certified maximally coherent for all epochs.
4. The periodic 0..F cycle is first-digit Haar but fails at depth two; de Bruijn(16,2) has first/two-digit Haar but fails at depth three. Their seam can vanish while common Haar current remains positive. Pure time differences telescope on every bounded path and do not detect normality.
5. The Pascal successor hierarchy attenuates a fixed h=1 non-Haar mode exponentially with difference order. Uncalibrated higher-order smallness cannot prove Haar.
6. #574's fit uses b=a*s, with s the observed completed real parity (`observational_succ/aphex_two_fiber_haar.py`, original_bbp_two_fiber). The coefficient is retrospective; it is not a source-only predictor. No test score earns an all-epoch asymptotic theorem.

## Scope supplement recommended (do not rewrite historical dossiers)

* Maintain the #554 hypothesis on the local prime estimate and on every parity/covariance/beta equivalence. The exact finite parity certificate itself is unconditional finite algebra.
* Say explicitly that the p-integral wrong seed is an epoch-dependent family. Its contrast is 2 on the certified epoch; the docs do not construct a single rational seed with contrast 2 for all A.
* `pi_parity_pressure/PROOFS.md:9` should be read as an L2/a.e. Fourier expansion. At the digit jump points, the usual symmetric Fourier series converges to 0, not the half-open parity value ±1. The half-open convention defines the original step function but does not change the Fourier midpoint limit. Authentic completed pi phases avoid these rational jumps by irrationality; the exact CRT identity and tests do not use the series at jumps. Record this qualification in an additive supplement.
* Binary Haar on a=±1 is distinct from #565's 16-child future-tail twirl and from Haar on the complete real circle. A small single parity contrast establishes neither other digit modes nor word laws.

## Execution

An isolated `git archive df624aa98579303d3ca0e2a312e7ca6423f4a0c9` was extracted into `/tmp/succ-main-xxii-parity-audit`. It contains the full canonical `observational_succ.duck_bbp`, not the test-only source fixture used in the original PR publications.

`PYTHONPATH=/tmp/succ-main-xxii-parity-audit OPENBLAS_NUM_THREADS=1 python` (Python 3.12.3) loaded and ran exactly:

- test_haar_successor_junction.py
- test_haar_pascal_successor.py
- test_bbp_parity_pressure.py
- test_bbp_parity_holdout_512.py
- test_aphex_haar_feedback.py
- test_aphex_two_fiber_haar.py

Result: **55 tests, 15.279 seconds, OK**. Raw log: `parity-focused-tests.log`. This does not certify the eventual merged integration head or supported-Python CI matrix.

A separate 2x2-count Fraction oracle enumerated all 5,208 admissible ±1 sign-pair streams of lengths <=6, compared beta/t/P/minimum-loss against production outputs, and verified P=beta+m*t and the sharp inequality. PASS, raw log `parity-exhaustive-oracle.log`. The two implementations share the same mathematical definition and are not independent source evidence.

A512 canonical-source replay reproduces u_plus=6/127, u_minus=-4/129, beta=641/16383, t=133/16383, P=5/128 and error 133/2097024. It reuses #572's spent holdout; it is not a fresh holdout.

## Verdict and next falsification

No substantive correctness defect found in the new #574 module or central #571–#574 proofs. Integrate all historical content with the listed qualifications, retain every hostile control, and require full native and hosted exact-head gates before main. The strongest new imported finite statement is the sharp source-relative parity certificate and calibrated binary Haar identity; it does not prove decay. The genuine next theorem is an all-integer-epoch, literal-zero-source bound u_plus(A)-u_minus(A)->0, retaining complete prime powers, winding and real tail and using information that fails on PPP-08's same-forcing p-integral counterseed family. One exact finite counterseed or low-loss fit must remain fatal to any claimed seed-blind shortcut.

**Pi base-16 normality: OPEN. Original-zero hexadecimal parity balance: OPEN. RH: OPEN.**
