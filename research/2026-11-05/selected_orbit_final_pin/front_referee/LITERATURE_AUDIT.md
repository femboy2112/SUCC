# Front ETA: primary-source arithmetic-dynamics audit

Read live author-hosted papers and the original arXiv submission on 2026-11-05.
This is a focused theorem-assumption audit, not an exhaustive literature search
or a claim that no unknown route exists.

1. Bailey–Crandall, [On the Random Character of Fundamental Constant
Expansions](https://www.davidhbailey.com/dhbpapers/baicran.pdf), author preprint,
03 October 2000, pp.2–3: the paper explicitly gives the same degree2/degree4
rational recurrence used here for pi. Its Hypothesis A starts at literal zero
and posits equidistribution or a finite attractor. The resulting normality
statement is conditional. Our exact original forcing meets the polynomial
shape assumptions; what remains unavailable is a proof of the dynamical
hypothesis for that forcing. Wrong-seed controls do not refute Hypothesis A,
because its zero start is an explicit hypothesis.

2. Bailey–Crandall, [Random Generators and Normal Numbers](https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf),
Experimental Mathematics 11 (2002), pp.527–546: Theorem3.2 is the unconditional
normality/perturbed-orbit equivalence. Theorem4.8 proves normality for a sparse
PRNG family subject to denominator structure and growing run-length hypotheses.
The original BBP four-pole recurrence has new nonzero forcing at every step;
no conversion into that sparse family satisfying its run-length hypotheses was
proved. Substituting the BBP denominator LCM for a fixed prime-power modulus
would discard the selected numerator and does not verify those assumptions.
The paper also proves rational-shift preservation; our seed1/5 control admits
the stronger exact termwise phase identity in R-07.

3. Lagarias, [On the Normality of Arithmetical Constants](https://arxiv.org/pdf/math/0101055),
v2, Theorems3.1/3.3/4.1: the perturbed and multiplication orbits have matching
asymptotic behavior when forcing tends to zero; finite-limit-point behavior
corresponds to a rational completion. The strong dichotomy is explicitly a
hypothesis, with normality conditional on it. Its G-function and invariant-measure
connections do not supply a deterministic selected-orbit discrepancy estimate.
R-06 here shows why excluding finite attractors plus adding weak regularity and
a small finite irrationality exponent still does not isolate Haar.

The inference made by this audit is narrow: none of these cited theorems, with
assumptions checked only from the actual four-pole formula, proves the needed
selected zero orbit inequality. Transfer-operator mixing for distributions or
almost-everywhere normality also needs a separate step selecting this one seed;
R-06 gives explicit existence countermodels to any seed-uniform shortcut.
