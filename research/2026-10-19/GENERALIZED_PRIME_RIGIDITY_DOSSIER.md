# Moonshot C: finite Euler reflection and the positive Poisson boundary

Date: 2026-10-19. Branch: `research/forge-ii-arithmetic-2026-10-19`.
Base: PR179 `81684b4b8956f9f5da56c376ba7e4339277eb665`.
Status: **PROVED LOCAL within the displayed hypotheses; scholarly novelty
UNVERIFIED; RH PROVED: NO.**

The complete proofs are in `PAPER_C_GENERALIZED_PRIME_RIGIDITY.tex`. The new
Python module supplies exact finite falsifiers and arithmetic identities,
not finite evidence promoted to an analytic proof.

## Claim ledger

| ID | Domain and quantifiers | Result and dependency closed | Evidence / next falsifier |
|---|---|---|---|
| FER-01 | Every pair of finite multisets U,V of real bases greater than one, every nonzero real c | Meromorphic reflection F(s)=F(c-s) forces identical multisets. Equal counts are a conclusion. | Paper Theorem 1: factor inversion, real-axis limit, period, least unmatched base. c=0 mutation fails exactly. |
| FER-02 | Every positive tempered Radon measure with mass one at zero, no mass in the punctured interval (-1,1), and Fourier self-duality | The measure is the integer Dirac comb. | Paper Theorem 3: Gaussian-regularized sinc squared, positivity, integer support, Fourier translation. Any noninteger positive atom is an obstruction. |
| FER-03 | Every locally finite positive integer-multiplicity source B in [1,infinity), unit mass at 1, some right-half-plane absolute convergence, the same Gamma completion, only poles 0,1 with residues -rho,+rho for rho>0, reflection, and uniform O(abs(t)^-2) on one contour strip [1-c,c] | B is ordinary positive integers, rho=1; if B is a Beurling word source, its primitives are exactly ordinary primes. | Paper Theorem 4: justified Mellin shift, even Gaussian separation, FER-02. Full strip control is a premise, not inferred from finite jets. |
| FER-04 | Finite observations, residue, density and right-half-plane zero divisor alone | These still do not authenticate the full source or completion. | Inherited ASM-01; explicit p=3,q=11 failure F(2) != F(-1). No new impossibility theorem for universal proofs is claimed. |

## Strengthening relative to the initial contract

The finite theorem removes equal cardinality and permits arbitrary nonzero
real reflection parameter c. It handles factors with repeated bases,
coincident powers and imaginary-axis zeros/poles without a divisor shortcut.
The infinite result does not assume density one or fix the residue to one:
absolute convergence supplies polynomial source growth; unit source mass
at one forces the residue after Poisson rigidity. It does assume a strong
completed analytic continuation and uniform strip decay. Those are explicit
infinite requirements, not a locally verified replacement for global UDC.

The precise new useful boundary is therefore conditional source rigidity:
the exact standard completion, with enough growth control to support the
contour argument, excludes nonordinary positive Beurling sources. The
repository has not derived that completion contract from its observer axioms.

## Exact adverse receipts

- Prescribed pair: p=3, q=11, a=9/2, b=77/17. The Euler ratio has F(1)=1,
  F(2)=504/517, F(-1)=34/21. The reflection equation fails exactly.
- Count mismatch: U=(2,2), V=(4) has order one at zero even though generator
  products agree. This cannot reflect about 1/2 because F(1) is regular.
- Coincident powers and repeated generators: U=(2,2,4), V=(2,4,4) leave
  least unmatched base 2 of signed multiplicity one. Powers do not hide it.
- Zero-center mutation: U=(2,6), V=(3,4) has F(s)=F(-s), F nonconstant.
  Counts and products agree; the nonzero-center assumption is necessary.
- Gap mutation: mu=(2/3) delta_(2Z)+(1/3) delta_(Z/2) is positive and
  self-dual with mass one at zero, but has mass 1/3 at 1/2. Its generalized
  Dirichlet multiplier (2^s+2^(1-s))/3 preserves reflection and residue one.
  It is deliberately not a Beurling source with primitives greater than one.
- Self-duality mutation: delta_Z + delta_(3/2) + delta_(-3/2) keeps positivity,
  normalization and the gap but fails the sinc identity.
- Rational noninteger atom x with positive symmetric weight w gives the
  strict lower bound 8w dist(x,Z)^2/x^2 for pi^2 times the sinc-square
  excess. At x=9/2,w=1 this contribution is exactly 8/81.
- Fresh exact late-source checks use (p,q)=(3,101),(5,29),(7,53),(11,127),
  (13,997), all with F(1)=1 and F(2) != F(-1).

The tests evaluate no zeta zero ordinates and perform no floating-point
analytic identity checks. They do not purport to classify infinite products
by enumerating finite factors.

## Proof audit and delicate domains

Root independently rederived the finite and Poisson mechanisms. The paper
incorporates these audit requirements:

1. Do not apply Poisson directly to sinc squared against a merely tempered
   measure. Multiply by exp(-pi epsilon x^2), use the nonnegative tent
   convolution on the Fourier side, dominate its tails using polynomial
   measure growth, then use monotone convergence on the original side.
2. At the support endpoints plus/minus one the tent is zero; approximate
   identity convergence remains valid even for atoms there.
3. The integer-supported Fourier object is a measure, so multiplication by
   exp(2 pi i xi)-1 annihilates it; no hidden derivative-of-delta inference
   is used to obtain period one.
4. Centered Gaussians separate even tempered distributions, not arbitrary
   distributions. Evenness is explicit; derivatives in t and Schwartz
   convergence of Hermite expansions prove separation.
5. The completed functional equation alone does not justify a contour shift.
   Uniform decay on the entire stated strip, the only two poles and their
   exact residues are separately assumed and used.
6. Generalized integer counts retain word multiplicities. Once the integer
   comb is identified, composite or repeated primitive labels give duplicate
   words and are excluded, rather than silently collapsing their values.

The formal-audit lane independently rederived the finite Euler theorem and
confirmed the unequal-cardinality and coincident-power arguments. No machine
formalization of this lane's theorems is claimed.

## Primary literature and provenance

The paper gives narrow comparisons with full primary sources inspected on
2026-10-19:

- Hilberdink and Lapidus (2006), Theorem 3.2 and its Mellin/modular setting:
  <https://arxiv.org/pdf/math/0410270>;
  DOI <https://doi.org/10.1007/s10440-006-9063-0>.
- Burnol (2011), version 2, ordinary-support Hamburger converse and generalized
  exponent extensions: <https://arxiv.org/pdf/1106.4749>.
- Baake, Spindeler and Strungaru (2023), Fourier eigenmeasures, the lattice
  formula and Hermite conventions:
  <https://doi.org/10.1007/s00041-023-10045-z>.

No inspected source was treated as proving that all Beurling systems have
the ordinary fixed completion. No classical integer-support converse was
used to assume the desired integer support. An exact scholarly predecessor
for the positive unit-gap formulation has not been established; its proof
uses classical Fourier ingredients and has no priority claim.

Inherited files read at the pinned base:

| File | Git blob |
|---|---|
| `research/2026-10-18/ARITHMETIC_SOURCE_MINIMALITY.md` | `9185abc3e0696a44fbc56ce04c8ff56cfcf6d039` |
| `observational_succ/arithmetic_source_minimality.py` | `feaf0b2d746e578bb9651a615f35c502efa263be` |

These are inspected inherited blobs, not claims about the originating commit
of every earlier sentence. No archival file or imported theorem was edited.
PR178 is not an ancestor premise and was not needed for this lane.

## Validation receipts

- Before development: `test_arithmetic_source_minimality.py`, 10/10 passed.
- New `test_finite_euler_rigidity.py`, 9/9 passed (0.014 seconds final run).
- `scripts/verify_provenance.py`: SOURCE_PROVENANCE_VERIFIED, 72 items.
- `scripts/observer_foundations_probe.py`: exit zero, RH_proved false.
- `scripts/ordinal_succ_report_probe.py`: exit zero, identification/positivity
  gaps remain explicit.
- Paper C: two pdflatex passes, 6 pages; second pass has no warnings. Text
  extraction and visual inspection of the analytic proof page found no
  clipping or unresolved references.
- Full repository tests are reserved for root's integrated validation, to
  avoid overlapping heavy analytic runs across isolated agent worktrees.

## Exact remaining dependency

Derive the full fixed Gaussian completion, pole residues and valid contour
control from independently justified source axioms, rather than taking
them as an identification premise. A finite Euler prefix, a positive local
kernel, residue one and the critical-strip zero divisor do not supply this
step. FER-03 identifies what would suffice; it does not complete that source
derivation or prove signed Weil positivity.
