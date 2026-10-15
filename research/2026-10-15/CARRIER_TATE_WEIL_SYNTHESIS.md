# Carrier → Tate → Weil: research synthesis and live boundary

**Date:** 2026-10-15. **Parent:** `d239c27d3759de71de316180f48dfc097be6aff5`.
**Branch:** `research/carrier-tate-weil-2026-10-15`, stacked above draft PR #129.
**Status:** classical reconstruction, exact source interfaces, analytic bounds,
and scoped refutations. Internal adversarial review is not external peer review.

## 1. Hole contract and verdict

The chosen dependency cut was the following statement: the reconstructed
adelic Schwartz–Bruhat Poisson interface, with its actual Haar and character
conventions, transports the canonical zeta and primitive chi4 sources to their
completed Mellin functions and then to the complete signed Weil distribution
on every compact smooth log test, continuously on fixed supports.

The hypotheses are classical Haar/Fourier theory, the exact restricted-product
arithmetic source, genuine multiplicative characters, and the stated classical
contour growth estimates. Quantifiers are over all Schwartz–Bruhat inputs in
the Tate theorem and all `C_c^infinity(R)` tests in the Weil identification.
Finite code accepts declared finite representations and resource budgets;
it does not instantiate these universal quantifiers.

**Verdict: the classical identification cut closes under these declared
classical analytic inputs. The positivity cut remains open.** The novelty tax
is paid by labeling the analytic theorems as classical, not by presenting an
RH-equivalent sign condition as a newly proved lemma. The useful contribution
is the explicit source maps, shared implementation adapters, error budgets,
information-loss analysis, and preserved counterexamples.

The cheapest falsifiers were single-place sign errors, shell Haar mass,
omitted-prime and non-Euler coefficients, odd-character parity, and a false
identification of an arbitrary Tate test integral with the canonical L-object.
The resulting proofs and controls are recorded in the linked dossiers below.

## 2. What now composes

| Interface | Exact mathematical content | Dossier / implementation |
| --- | --- | --- |
| Additive carrier and duality | `A/Q=(R×Zhat)/Z`, full dual `Q`, rational self-annihilator | [independent audit](../../reviews/2026-10-15_CARRIER_POISSON_INDEPENDENT_AUDIT.md), existing solenoid modules |
| Complete Poisson | Rational-coset reduction and separate compact-quotient inversion proof with uniform tails | Same audit; existing `adelic_poisson_reconstruction.py` |
| Idelic normalization | `I=Q*×R_+×Zhat*`, quotient measure `dr/r du`, unit shell mass 1 | [Tate reconstruction](TATE_IDELIC_ZETA_RECONSTRUCTION.md), `tate_idelic_zeta.py` |
| Canonical zeta | Gaussian times all integer indicators gives `Gamma_R(s) zeta(s)` for Re(s)>1, then continuation, poles and FE | Same Tate dossier; reuses `all_places_zeta.py` |
| Genuine primitive chi4 | Ramified two-coset test at 2, odd real Gaussian, Gauss/root phases, conductor 4 | [character crucible](TATE_CHI4_ARITHMETIC_CRUCIBLE.md), `tate_chi4.py` |
| Complete signed distribution | Poles + Gamma/conductor − genuine half-density prime powers, all compact smooth log tests | [Weil identification](TATE_TO_WEIL_DISTRIBUTION.md), `tate_weil_distribution.py` |
| Approximation | Explicit fixed-support C1 continuity, rational prime coverage, O(J^-1) and accelerated O(J^-2) Gamma tails | Same Weil dossier and adapter |

The all-test formula is linear in the test function after fixing the normalized
arithmetic source. **Logarithmic differentiation is nonlinear in that source.**
In particular, `Z(Phi_g,s)=H_g(s)L(s)` is not permission to replace `L'/L`
by `Z'/Z`: the latter contains `H_g'/H_g`. The adapter
`TateWeilSource.from_tate` accepts precisely the two canonical upstream source
types and preserves their declared source identity and epoch.

## 3. Earned obstructions and corrections

### 3.1 Exact arithmetic survives in the atoms

Off the origin, the Weil distribution is a locally finite atomic measure plus
an explicit smooth density. Its atoms are exactly
`-Lambda(n) chi(n)/sqrt(n)` at `±log(n)`. Uniqueness of the Lebesgue
decomposition makes those coefficients recoverable from the full distribution.
A smooth Gamma/pole correction cannot conceal a fake impulse at 6. A bounded
window only sees its bounded set of atoms; the universal arithmetic source law
is additional information, not an observed tail.

### 3.2 Two distinct failures of positivity shortcuts

First, the **authentic** zeta Weil distribution is not positive on all
pointwise nonnegative tests. A unit-height smooth bump of width `1/100` around
`log 2` has a strictly negative value, bounded above by `-19/75`. This blocks a
positivity-preserving pushforward of a positive measure on that cone. It does
not block positivity on convolution autocorrelations: that is a different cone.

Second, let `D=x d/dx+1/2`, `G=exp(-pi x²)`, and
`A=(16/3)(D²-1/16)`. The legitimate Schwartz tests `A^N G` are Fourier
self-dual, preserve origin/integral normalization and every finite Euler factor,
but their Mellin transform is multiplied by

`P(s)^N`, where `P(s)=1+(16/3)s(s-1)`.

The derived polynomial roots are `1/4,3/4`; no actual zeta zero is used.
For `N=4096`, the complete modified divisor form is negative on an explicitly
given autocorrelation, with rational upper bound `-127388/99225`.
The Archimedean test is signed, and this changes the Tate test integral, not the
canonical arithmetic L-function. Subtracting the test multiplier's logarithmic
derivative restores the canonical form. See the
[obstruction proof](../../reviews/2026-10-15_TATE_WEIL_POSITIVITY_OBSTRUCTION.md)
and exact polynomial/moment implementation `tate_positivity_obstruction.py`.
Existing stronger positive-source Hermite/mixture countermodels are credited
there rather than claimed anew.

Thus self-duality, Poisson, all genuine finite Euler factors and correct pole
residues do not by themselves identify a canonical positive Weil form. This is
a precise failed inference, not a no-go theorem against source-specific RH work.

### 3.3 Information the downstream map loses

An overall nonzero scalar disappears under logarithmic differentiation: this
is an exact observation kernel. Differentiating the functional equation also
removes its displayed root constant, so a finite coefficient/formula check
does not authenticate independently supplied root metadata. This is **not**
a global impossibility of root recovery: full logarithmic data and self-duality
recover it from central-order parity, `w=(-1)^ord_(1/2) F`. A preliminary
overstatement conflating these claims was caught and corrected during audit.
Upstream real/finite Fourier and Mellin normalization receipts are retained.
Real self-dual distributions also factor through the even part of the test
and can conceal orientation.

### 3.4 Errors caught rather than archived as truths

- The parent table's claim that noninteger rational scales are *necessary* for
  finite-adèle test spanning is false. Integer scales with rational translates
  suffice by explicit disjoint coset refinement. The original is preserved;
  the correction is in the new audit and ledger.
- The half-open fundamental domain proves covolume; its compact closed cover
  proves compactness. The two arguments are separated in the audit.
- A preliminary extra factor 2 in idelic quotient Haar was rejected: the two
  rational orbit signs already account for it.
- A draft Gamma-bound sentence incorrectly used `Gamma_R(sigma)` over the
  entire right half-plane. The correct pointwise majorant is
  `Gamma_R(Re(s))`, or a supremum on a declared bounded real strip. At `s=20`
  versus `sigma=2`, `9!/pi^9>9!/4^9>1` is an exact counterexample to the draft.
- The Weil contour sum is over all completed zeros in the **closed** strip;
  this avoids silently importing boundary nonvanishing just to write an
  open-strip index. No critical-line assumption is involved.

## 4. Observer-relative field semantics

Every classification requires a tuple `(carrier, target, proof theory,
permitted experiments, execution model)`. The mathematical completion alone
does not fix such a classification.

| Declared target/toolkit | Finite execution / certification | Remaining access boundary |
| --- | --- | --- |
| Rational-chart idele normalization and a specified finite residue | Exact integer/Fraction execution; SimpleField for this target | Does not cover arbitrary real/profinite points |
| A fixed compact test with effective smoothness and integration bounds | Finite prime tape plus certified analytic approximation to requested accuracy | No automatic total algorithm for a black-box function without bounds |
| Universal Poisson/Tate/Weil identities in classical analysis | Finite symbolic proofs over infinite spaces | A proof is not an infinite elapsed source experiment |
| Full equality of arbitrary profinite programs from bounded residue queries | Bounded observations can agree while a later prime separates | No uniform query horizon; not a phantom under all separating probes |
| Full all-support Weil autocorrelation positivity | Not proved by this work | No assignment of RH to IdealHardField or FuckedField is licensed |

Source IDs and epochs are declarations that prevent accidental cross-source
joins. They are not physical authentication. Test-generated countermodels are
lawful mathematical alternatives with their altered source made explicit;
they are not claimed observations of the canonical arithmetic source.

## 5. Validation policy and next verdict-changing experiment

See `CARRIER_TATE_WEIL_VALIDATION.json` for executed commands, exact source
state and checked CI. The parent exact head's full Python 3.10/3.13 repository
CI was independently observed successful before this branch was published.
The local runtime is Python 3.12; dependencies were initially missing, then
installed from the project's declared test extra. The initial incomplete run
is not reported as passing. Focused exact tests and numerical cross-oracles are
separate evidence classes. No floating output is upgraded by an analytic tail
bound that omits rounding or quadrature error.

The repository has Lean sources and a pinned 4.14.0 toolchain declaration, but
this workspace has no `lean` or `lake` executable. No new formal verification
claim is made. Provenance originals remain unchanged.

The next consequential experiment is to specify a candidate positive carrier
and an explicit map for *arbitrary* convolution autocorrelations on a fixed
support/Sobolev window. Compare it to the entire signed form with a uniform
operator error, using both zeta and chi4. Its first failure must be retained
as a test/source mismatch or a signed counterexample. Only after exact identity
and source-specific positivity hold may support-uniform extension be attempted.
This targets the remaining sign mechanism; re-proving additive Poisson or
testing more finite zeros would not close it.

RH PROVED: NO
