# Factorial Borwein hologram claim supplement (FBH-01–FBH-09)

Full derivations, hypothesis boundaries, source mappings, controls and next falsifier:
[Factorial Borwein arithmetic hologram](../research/2026-10-19/FACTORIAL_BORWEIN_HOLOGRAPHIC_CLOCK.md).

**Branch:** `research/factorial-borwein-holographic-clock-2026-10-19`, stacked on Borwein/prime-clock draft #189, pinned source commit `414efb07f396af4a8d15ffed9fe36d6567fda95a`.
**Global firewall:** ABC OPEN, RH OPEN, true signed completed Weil/Suzuki S4 sign OPEN. Academic priority UNVERIFIED. Parent branch and frozen source archives unchanged.

| ID | Exact scope, assumptions, quantifiers | Status / validation |
| --- | --- | --- |
| FBH-01 | Every N>=4, factorial-labelled uniform convolution B_N has positive plateau width >1/12, support inside (-23/24,23/24), cardinal integer samples, and integer translates partition unity | **PROVED LOCAL**: Borwein convolution, sum of repeated prime-power reciprocal widths <11/12 |
| FBH-02 | All N>=4, canonical `I_N : ell²(Z)->L²(R)` is a bounded, injective lift with `(1-S_N)||c||²<=||I_N c||²<=||c||²`; range-sampling reverses it | **PROVED LOCAL**: disjoint protected islands and Jensen; R only bounded on range, not arbitrary L2 |
| FBH-03 | Every N>=2, variance difference `V_N-V_(N-1)` equals the exact positive new prime-power window sum and vanishes iff N prime | **PROVED LOCAL**: Legendre occupation; does not furnish a new primality oracle |
| FBH-04 | Finite N Fourier log-sinc germ gives even power sums and Newton reconstruction of all source-labelled uniform width squares | **PROVED LOCAL**: Euler sine product and Newton identities; TESTED with independent polynomial factors |
| FBH-05 | Every N>=4, continuous L2 Gram has `g_j=0` for `|j|>=2`, `g0+2g1=1`, `g1>0` and `g0-2g1>=1-S_N>1/12` | **PROVED LOCAL**, TESTED exact rational independent B-spline oracle; **not** an orthogonal or signed-Weil identification |
| FBH-06 | Infinite genuine prime-power uniform convolution exists and for each N>=4 satisfies `||B_infty-B_N||_infty<=2E_N`, where E_N is explicit finite rational and tends to zero | **PROVED LOCAL**: absolutely convergent widths, coupling, uniform 4-Lipschitz, telescoping tail |
| FBH-07 | Authentic `+1/-1/nonzero` prime-clock gate lifted by `I_N P R`; finite factorial SUCC Poisson series has nonnegative exact rational coefficients and tail at most `t^(M+1)/(M+1)!` | **PROVED LOCAL**: discrete projector, Poisson falling factorial moments; not Borwein simplex factorial |
| FBH-08 | All N>=4, integer and half-integer samples do not identify factorial label N, whereas a selected rational off-grid point distinguishes N=4 from N=6; a different rational point remains flat | **PROVED LOCAL / TESTED MODEL**: explicit exact CDF and independent width-spectrum source |
| FBH-09 | Replacing repeated prime occupations by first prime reciprocal widths p=2,3,5 preserves lattice delta | **REFUTED**: exact `B_mutated(1)=1/43200>0` and reciprocal budget 31/30>1 |

**Execution:** `python -m unittest discover -s tests -p 'test_factorial_borwein_hologram.py' -v`; `python scripts/factorial_borwein_hologram_probe.py`. Local isolated test harness in Python 3.13 reported **13/13 passed**, with a mathematical surrogate of the upstream Borwein CDF API. Hosted CI against the complete parent implementation is the separate acceptance gate. No Lean proof or large-scale number-theoretic inference is claimed.

**External primary source:** D. Borwein and J. M. Borwein, *Some Remarkable Properties of Sinc and Related Integrals* (2001), Ramanujan J. 5, 73–89, https://gwern.net/doc/math/humor/2001-borwein.pdf. Their sinc/convolution theorem is **classical**, not a proof of our indexing or academic priority.

**Next discriminator:** The actual source-triple constraint `a+b=c` with simultaneous (p^k)-clock gates for three pairwise-coprime slots and noncircular, family-uniform analytic bounds; compare explicitly against published ABC exceptional-set estimates, not only fitted examples.
