# Candidate handoff — genuine Gamma OU orientation and source-typed prime-place chart obstruction

**Source:** SUCC research branch `research/prime-categorical-sphere-gamma-sieve-2026-10-14`, parent `5a3f5cf4d415266b3c647e1eab3326acb04d3cbd`; resolve this note's exact commit at PR review. Mathematical derivation in [PRIME_CATEGORICAL_SPHERE_GAMMA.md](../../research/2026-10-14/PRIME_CATEGORICAL_SPHERE_GAMMA.md). **RH PROVED: no.** This is an exploratory candidate, **NOT yet exported to or merged into femboy2112/FuckingRH**. No nontrivial zero coordinates enter this work.

## Source and theorem

Start with Suzuki's true Archimedean real-place OU bath `B_+ = sum_(j>=0) (2j+1/2)^-2 R_(2j+1/2)` as a whole-line bounded positive convolution operator; `R_alpha` has kernel `e^-alpha|t|`. Define the explicitly **auxiliary** companion bath `B_- = sum_(j>=0) (2j+3/2)^-2 R_(2j+3/2)`. This companion is NOT part of Suzuki's original completed Weil form and is not permitted to be silently added to it.

**Proved local/source-derived identities:**

1. Actual source ladder labels `n=4j+1` force a `3 mod4` companion when multiplied by a true prime p=3 mod4, and a new dyadic conductor level when multiplied by 2. For p=1 mod4, the original ladder is preserved. On L2 real, `p^-3 Dp B_chart Dp^-1` is a source-typed subset of its correct target Gamma chart, leaving a positive OU-mode remainder. These are *spectral scalar-dilation models*, NOT proved effects of a genuine arithmetic FUCC apparatus.
2. `C=B_+-B_- >=0` on L2(R) and every interval compression. Its exact Fourier multiplier is `pi(1-sech(pi xi))/xi²=(pi-|Gamma(1/2+i xi)|²)/xi²`, removable at xi=0 with value pi³/2. Distributional kernel identity: `k_C'' = 1/2 sech(t/2) - pi delta0`. The diagonal kernel difference is `4*Catalan`, a genuine `L(2,chi4)` Euler product. This positive signed companion is an auxiliary **new-to-project** spectral factor, not the Weil form.
3. Quantitative positive metric `(8/3)||f||_H-1² <= <f,Cf> <=22||f||_H-1²`, but no L2 uniform gap. A high-frequency endpoint wave packet shows the *first true Suzuki prime-2 negative overlap* is NOT uniformly controlled by this auxiliary H-1 norm alone. This is a concrete no-go against a tempting source-blind shortcut.
4. A four-phase double cone creates a finite S² whose actual prime mod4 automorphism degree equals `chi4(p)` for odd p. This is an exact source-indexed **toy topology**; it does not identify the adele-class or Suzuki global space with S².

## Correct differentiated-variable bonus: an honest Markov jump energy (PS-10/11)

This revises the bare-H^-1 no-go above: the correct Suzuki variable is u=i v', so the auxiliary chiral metric after differentiating has bounded multiplier `pi(1-sech(pi xi))`. Let `q(t)=sech(t/2)/(2pi)` and P=convolution by q. It is a genuine symmetric probability jump kernel with variance pi² and Fourier characteristic `sech(pi xi)`, and exactly **`D*C D=pi(I-P)`** with Dirichlet energy `(pi/2) intint q(x-y)|v(x)-v(y)|² dx dy`. The Markov semigroup is the norm-convergent Poissonized finite-SUCC series `e^-pi*t sum (pi*t)^k/k! P^k` with a rigorous rational tail at mean-one time. These are mathematical source-derived from the auxiliary paired Gamma sectors; no physical execution or true completed Weil identification.

Further, normalizing the N-jump source and the N-step symmetric Pascal source to the same variance yields finite characteristic functions `sech(theta)^N` and `cos(theta)^N`, both approaching the canonical Gaussian `exp(-pi xi²)`, with a proved *two-sided Fourier sandwich* for `|theta|<pi/2`. This gives two lawful **probability-law** hemispheres meeting at one real Gaussian limit; the original arithmetic sources remain distinct, so it is not a global arithmetic-source gluing proof.

## Construction, domain, adversaries, and test status

The whole-line OU sums converge in L2 operator norm (`||alpha^-2 R_alpha||=2/alpha³`), so the Fourier multiplier comparisons and interval compression are legitimate. The only Gamma modes identified with **actual** Suzuki source are `n=4j+1`; 3-mod-4 companion and dyadic completion are strictly labeled generated/test candidates. Fake composite 6 is rejected as a primitive Euler factor, 2+6 overlap gives a negative sieve coefficient at mode 6, dyadic normalization and source residue losses are recorded, and swapped/missing chart controls are present.

**Reproduce:** `observational_succ/prime_categorical_sphere.py`; `tests/test_prime_categorical_sphere.py`; `scripts/prime_categorical_sphere_probe.py` and independent 70-digit `scripts/prime_sphere_independent_oracle.py`. Exact rational proofs and a separate numeric holdout; CI must be evaluated against the exact committed head. New-to-project packaging, classical Fourier/Dirichlet beta/Gamma identities; no independent academic priority claim.

## The missing RH-bearing theorem

Find a source-forced intertwiner from *original* SUCC/FUCC integer prime paths and their complete place phases to Suzuki's correct **completed** real-place operator including the inverse-Neumann, pole rank-one terms and authentic von Mangoldt shifts. Show whether the chiral auxiliary operator supplies a valid controllable correction **without changing the actual Weil form**, and obtain a correct whole-space signed inequality across the first prime-2 wavefront. RH still requires all-a positivity (Suzuki/Yoshida) or the specified global spectral limit; this candidate proves neither.
