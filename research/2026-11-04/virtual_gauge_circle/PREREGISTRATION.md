# Operation Virtual Gauge × Cyclotomic BBP Circle — source contract

Date: 2026-11-04. Research-only **additive child of #502** at `7e91606f15dc5e4dbf4d9105f5110df3c4b7d6cd`. Inherited #499/#500 source-primal theorem is paper mathematics, not independently peer-reviewed; sibling #501 is read-only context.

## Exact baseline (do not modify)

Original source: `P=(4,0,0,-2,-1,-1,0,0)`, `U_0=0`, `U_n=16U_(n-1)+r_P(n)`, `r_w(n)=sum_{j=1}^8 w_j/(8(n-1)+j)`. Dual `Psharp=(0,8,4,4,0,0,-1,0)`. Inherited primal source `A=(2P+Psharp)/4`, radial null `R=(2P-Psharp)/4`; `U=Y+Z` with `0<Z_n<1/(32n+16)`.

## Exploratory observations BEFORE this preregistration

The following were derived/tested interactively **before** committing this document and are NOT preregistered novel discoveries: (i) `P_lambda=A+lambda R` appears to share the same completed π period; (ii) its endpoint moment appears to vanish only for lambda=1; (iii) (u=(1+i)/2) and its quarter-turns appear to give a four-point Gaussian family of BBP-type arctangent forms; (iv) the radial null has (Z_n=1/(32n)-5/(256n^2)+O(n^{-3})) and appears to oscillate at (H\asymp A^2\log A). Early exploratory finite A=128,256,512,1024,2048,4096 are **fit/development** observations.

## New prospective falsifiers, specified before holdout

1. Exact 8-tap polynomial identities for the angular kernel, radial logarithmic derivative, and all four rational Gaussian rotations, using a separately written Fraction implementation.
2. Exact Frobenius `S_3 P_lambda = -P_{-lambda}` (including odd-denominator rational lambda classes).
3. A continuous eight-cell degree-one circle based on normalized angular+radial integrated phase, not a claim of selected time mixing.
4. Source-specific radial-tail second derivative `Z''(x)=1/(16x^3)+O(x^-4)`. Apply the **classical** second-derivative exponential-sum test, with explicit scope (H\asymp A^2\log A), to predict `A^-1 sum_{n in [A,2A)} e(H Z_n) = O(sqrt(log A/A))`.
5. Independent integer epoch holdouts `A=(307,953,1901)`, high frequencies `H=16^floor(log_16(A^2 log A))`, and same original radial source. Predicted: absolute normalized high-frequency radial sum < 0.25; at h=1 normalized radial sum > 0.99. These finite thresholds are calibration, NOT asymptotic proofs.
6. **Hostile model:** any inference that `sum e(H Z_n)=o(A)` forces `sum e(H(Y_n+Z_n))=o(A)` for an unspecified companion `Y_n` is invalid: `Y_n=-Z_n` makes the product constant 1. This countermodel is not an authentic primal source and cannot refute π normality.

## Scope and authority

No original source edits, seed changes, merges, tags, releases, RH/GRH/π normality theorem, quantum-mechanics claim, or worldwide priority claim. Real-parametric circle `lambda in R` is geometric; rational BBP taps require `lambda in Q`. In the odd-denominator rational carrier we restrict to rational lambda with odd reduced denominator. Distinguish the finite root-of-unity **orbit** from the parameterized **null-period fiber** and from the time-ordered selected real-circle orbit.

**Verdict-changing goal:** find or disprove a genuinely SOURCE-COUPLED signed estimate for `e(HY_n)e(HZ_n)`, not one-factor cancellation, abstract circle geometry, denominator growth or ordinary projection averaging.
