# Preregistration — hostile Gamma–prime pinning holdouts (before execution)

**2026-11-04.** Frozen original merged main a673ec95dfac4ef6a61c60222be8b615fd08535d. This preregistration commit is written BEFORE the first holdout measurements listed below. The analytic theorem and initial development probes have already been derived using p=17,41,73,89,97,113,137 and some exploratory large examples; they are NOT blind evidence.

## Fresh held-out prime births

Use p = 193, 241, 257, 281, 337, 353, i.e. n=(p+7)/8 = 25,31,33,36,43,45. These are explicit non-development primes p≡1 mod8. Independently implement (i) source from the original four terms, (ii) source from the collapsed polynomial (15p²+121p+240)/(p(p+3)(p+4)(p+5)), (iii) original zero-seeded integer LCM clock, and (iv) four-term *rational* Euler successor enclosures without floating-point log.

For every held-out p predict ALL: p-local residue =4; β denominator C_p=(p+3)(p+4)(p+5)/8; original forcing reduced denominator pC_p; Gamma four-term rational correction interval contains r and has C_p·width<1; the affine p-primary coset contains exactly ONE point in the corrected interval and that value equals independent polynomial forcing; source LCM state p-local residue stays 4. Test the mutant r+1/C_p: same p-residue, inside COARSE Gamma window, outside corrected interval.

**Failure:** any mismatched exact Fraction, number of corrected candidates ≠1, mutant surviving corrected interval, residue not 4, or newly born p already dividing the prior source LCM. Do not remove failures or silently change this set.

**Interpretation:** passing finite tests corroborates algebraic paper theorem but cannot establish π normality or external novelty priority. Pigeonholing finite possible forcing candidates is not a theorem about selected orbit visit frequencies.
