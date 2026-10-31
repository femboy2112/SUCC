# Operation Pisot Ramification — Non-Pisot finite dynamics through Pisot arithmetic carriers

Research-only continuation of [Universal N PR #416](https://github.com/femboy2112/SUCC/pull/416), date 2026-10-30. Exact parent head 725377a64748ab0c442d16a61509b99687412505. Root merged Main XVI. No source, archive, selected U0=0, production, historic contracts, workflows or main edits.

**The author's proposal:** finite counting dynamics with non-Pisot dominant growth may be decomposed or **ramified through Pisot components**. Precise affirmative constructions are available:
- Integer **binomial time transform** converts a_n=a_(n-1)+3a_(n-2), root (1+sqrt13)/2 non-Pisot, into b_n=3b_(n-1)+b_(n-2), root (3+sqrt13)/2 Pisot unit, and inverses recover the original.
- A completely **positive Fibonacci path decomposition** of 1/(1-z-3z²) into convolution powers of 1/(1-z-z²).
- A cubic with non-Pisot root of x³-x²-3 cannot be shifted affinely into Pisot, but a positive polynomial B=2I+A+A² is a **Pisot unit** integer matrix, with A=2I-B^(-1). The fields have **identical integral orders**, discriminant -255, and genuinely ramified primes 3,5,17.
- For any real algebraic number field, a classical theorem guarantees a Pisot-unit field generator. This is **field-coordinate existence**, not an automatic positive finite path decomposition.

Start with [mathematical proofs](PISOT_RAMIFICATION.md), [scoped claims](CLAIMS.md), [focused stdlib regression source](pisot_ramification_probe.py), [independently executed SymPy oracle](independent_oracle.py), [validation](VALIDATION.md), and [next falsification gate](NEXT.md).

**Boundaries:** Pisotization changes the time generator and often requires expanding inverse/signed operations. The equivalence cannot be used to infer normality of the authentic zero-seeded BBP digits without a separate source/carry adequacy proof. π normality, RH, physical geometry, and a universal positive Pisotification theorem remain OPEN.
