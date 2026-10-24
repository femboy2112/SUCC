# Operation pi Source Genesis: mathematical execution report

**PI NORMALITY PROVED: NO.** This run proves source-specific approximation,
transport and conductor theorems. It also derives a weak all-horizon estimate
for pi using a separate classical irrationality-measure theorem. It does not
prove a sublinear bound for any actual pi Fourier mode.

Research branch: `research/pi-source-genesis-2026-10-24`.
Parent: PR #252, commit `364962ac0c0e8fb4d06c37468a5d50336d68a9ee`.
The existing worktree and all historical sources were preserved. The new
worktree is `SUCC-pi-source-genesis`. Main was not modified.

## What was actually proved

1. **A Pell-number hierarchy for the exact BBP tail.** If
   `h(t)=(4+4t+4t^2+2t^3+t^4)/(16-t^8)`, then
   `h(1+s)=1/(1-2s-2s^3-s^4)`. Its Taylor coefficients satisfy
   `a_(2m)=P_(m+1)^2`, `a_(2m+1)=P_(m+1)P_(m+2)` for Pell numbers P.
   For every fixed finite K and all n>=0,
   `0<(-1)^K(T_n-A_K(n))<a_K B(8n+1,K+2)`, with explicit rational A_K.
   The signed remainder is itself a positive Hausdorff moment sequence.

2. **Uniform control of the signed correlation transport error.** Define
   `D_d(N)=sum_(j<N-d)e(h(y_(j+d+1)-y_(j+1)))`, where the forcing and y0=0
   are authentic. Then for every nonzero integer h and all N>d>=1,
   `|C_d(N;pi)-D_d(N)|<pi*|h|/30`.
   With the Kth rational correction and starting offset M, the error is at
   most `pi*|h|*a_K*B(8M+2,K+1)/4`, independently of lag and length.
   This comparison retains the Fourier signs and avoids exponential lag
   amplification. **It does not estimate the size of D_d.**

3. **Full-conductor rational approximation at the required horizon.** One
   BBP truncation with M=N+K terms controls every admissible lag to absolute
   error at most `128|h|/[15*16^K*(8M+1)*(8M+2)]`. For odd M, its reduced
   denominator has exactly `4(M-1)` factors of two. Its base-16 preperiod is
   exactly M-1, so almost the whole required window precedes its periodic
   regime. Complete-period cancellation cannot be substituted for this sum.

4. **A weak actual-pi cancellation baseline from a different source.** The
   published bound mu(pi)<8 implies, for every fixed nonzero integer h,
   `|sum_(j<N)e(h16^j*pi)| <= N-log(N)/(162 log(8))+O_h(1)`.
   The dossier supplies an all-N version with a constant expressed in terms
   of an irrationality constant for pi. That constant has not been computed
   here. This is an unconditional mathematical consequence of an external
   theorem, not a BBP-kernel breakthrough; division by N still gives a bound
   tending to one. The same argument applies to each fixed lag frequency.

5. **A stronger source-typed counterexample family.** Set F(t)=g(t)/(16-t^8)
   and `V_m(t)=F(t)-(1-t)^(4m)/(4(1+(1-t)^2))`, m>=1. Each V_m is a positive
   density with rational total mass, all Hankel ranks positive, rational
   forcing, and a nonzero rational-coboundary invariant. Its selected phase
   is purely periodic. Yet its tails differ from actual BBP tails by between
   `B(8n+1,4m+1)/8` and `B(8n+1,4m+1)/4`, for every n>=0. Thus any prescribed
   finite tail jet can be matched under these stronger structural premises.
   For m=1 the selected phase is fixed at2/3 and every lag correlation is
   exactly N-d. The counterfeit has an extra forcing-index pole class3/4;
   it is not a counterexample to the complete BBP source. The
   [full construction and invariant proof](PI_SOURCE_GENESIS_NONCOBOUNDARY.md)
   close this hostile-control question without closing the BBP research lane.

Complete proofs and domains: [Green/Pell/operator dossier](PI_SOURCE_GENESIS_GREEN.md)
and [signed correlations/conductors/arithmetic dossier](PI_SOURCE_GENESIS_SIGNED.md).
The [claim ledger](../../docs/CLAIM_SUPPLEMENT_PI_SOURCE_GENESIS.md) assigns
separate authority labels. Academic novelty is unverified.

The new [Lean module and proof-scope report](PI_SOURCE_GENESIS_LEAN.md)
contain **41 freshly checked declarations**, including actual complex
lag-sum transport. The formal uniform bound is the coarser
`|P-Q|<=|a|/[32(J+1)]`, with a=2*pi*h. Its exact finite-window version
retains the difference of the two boundary tail sums. All four calibrated
mutation pairs passed. Only propext, Classical.choice and Quot.sound occur
as axiom dependencies. The all-order analytic hierarchy and sharper pi|h|/30
constant remain paper proofs. A first run's memory-cap abort is preserved
separately; the final serial kernel run passed.

## What the source audit established

The repaired PR #252 claims survived independent derivation: signed moments
m0=0 and m1=15/64; the positive integral kernel; all-order Hausdorff complete
monotonicity; all-size positive Hankel matrices; infinite time-homogeneous
linear realization rank; and strict beta bounds. The original BBP identity,
backward recurrence and exact circle distance were already proved in PR #232.
They are not presented as discoveries of this run.

The operator formulation specifies the spaces and actual intertwining maps:
the left shift on bounded sequences, `(16I-S)^(-1)`, the source multiplication
operator with spectrum [0,1], and the clocked expanding circle map.
Backward errors contract; forward phase errors expand until wrapping.
The source multiplication operator converges strongly to zero under powers,
but its operator norm stays one. Positive continuum modes do not imply
uniform exponential contraction or selected-orbit mixing.

Moment determinacy, Gaussian quadrature and the signed Markov/Padé remainder
are developed with their actual hypotheses. Their exact coefficients already
depend on T0; reconstructing pi from that supplied mass is circular. This is
a limited obstruction to that argument, not a universal impossibility result.

## Hostile controls and failed implications

| Source | Verified contract | What it controls |
|---|---|---|
| Actual BBP with y0=0 | Exact four-pole forcing, bounded tail, T0=pi/16 | All source-specific positive claims |
| Same forcing, y0=1/3 | First forced state 7/15; selected orbit translated by 1/3 | Initial-state separation; lag observations alone cannot distinguish these states |
| Unforced x=1/3 | Fixed point of multiplication by16, no BBP forcing | Generic circle counterexample only |
| Positive rational infinite-rank tail | Tn=1/((n+1)(n+2)), positive rational forcing | Positivity and infinite memory do not imply normality |
| Arbitrary finite-jet rational counterfeits | Positive polynomial density matching a prescribed endpoint jet, rational mass/forcing | Any fixed number of matching asymptotic coefficients is insufficient; not a rational non-coboundary or exact BBP source |
| Explicit non-coboundary finite-jet family V_m | Positive rational t-density, rational total mass and forcing, invariant -1/4 in pole class3/4, arbitrary matching jet | Even adding the non-coboundary premise is insufficient; exact extra pole class distinguishes it from BBP |
| Arbitrary-order rational non-coboundaries | K!/[n...(n+K)], invariant (-15)^K | Non-coboundary obstruction does not fix a decay exponent |
| delta at1/8 | Genuine circle probability, exact prime paths | Old min-plus ceiling is false |
| 3-adic periodic circles | Actual full base-16 orbit modulo3^r | Periodic lag resonance; not a BBP source |
| Sparse alpha=sum16^(-2^k) | Explicit irrational source, proved mu(alpha)<=3, A_h,N->1 | Finite irrationality exponent permits almost maximal sums |
| Authentic polygon and BBP sources | Source constructions, no input pi digits | Cross-representation finite source validation; no polygon-ensemble genericity inference |

An independently implemented rational interval test caught a factor-of-16
error in an intermediate horizon-error bound. The repaired factor is explicit
in both the proof and regression test. This is not an error in inherited PR #252.

## Direct answers to the mission

**What is new about pi's actual selected trajectory?** Explicit all-order
rational shadowing with signed completely monotone errors; lag-uniform
transport of actual complex correlations; and a precise conductor/preperiod
theorem for its certified approximants. A separate arithmetic theorem gives
an unbounded logarithmic deficit in actual Fourier sums. General circle
dynamics supplies none of the BBP constants or the irrationality input.

**Which exact source information is necessary?** Pell coefficients and the
signed correction hierarchy use the particular rational kernel g and its
endpoint derivatives. Identification of the orbit uses the BBP integral and
y0=0. The uniform lag mechanism generalizes to decreasing summable tails;
its small numerical constant and rational corrections are BBP-derived.
The denominator theorem uses the exact odd-denominator collapsed forcing.
The logarithmic deficit uses external Diophantine information instead.

**Which signed correlations are now controlled?** Their transport errors are
bounded uniformly in every lag and horizon. Each fixed pi lag also has the
weak logarithmic deficit derived from irrationality measure. No fixed-lag
o(N) estimate, let alone the full required growing-lag estimate, is proved.

**Where is new information still needed?** In the incomplete exponential sum
for the source-selected rational phases. Positivity, high-order approximation,
finite-type irrationality and eventual periodic averages do not supply it.

The next smallest useful source-specific theorem is a sublinear estimate for
one fixed nonzero authentic forced Fourier mode, or a signed lag aggregate
that implies one. This would change the cancellation ledger, not prove full
normality by itself. To prove normality, the sufficient all-mode statement
must still be established with all its quantifiers.

## Reproduction and validation boundaries

Local validation passed: **7,424 tests in 840.235 seconds**, including the
15 new source-genesis tests; all 72 import-provenance items; and both required
observer/ordinal probes. The targeted 15-test and 11-test repaired-source
suites also passed separately. The full-suite environment and exact log hash
are in [the receipt](pi_source_genesis_receipts/full_suite.json).
The source oracle additionally checked the polygon-selected phase and the
stronger non-coboundary family after the full-suite discovery began; its
final deterministic receipt is separate from that test count.

```sh
python -m unittest discover -s tests -p 'test_pi_source_genesis.py' -v
python -m unittest discover -s tests -p 'test_bbp_source_memory.py' -v
python scripts/pi_source_genesis_oracle.py --output /tmp/pi-source-genesis.json
cmp /tmp/pi-source-genesis.json research/2026-10-24/PI_SOURCE_GENESIS_FINITE.json
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

The deterministic [finite oracle receipt](PI_SOURCE_GENESIS_FINITE.json)
includes symbolic identities, positive Hankel determinant intervals, actual
signed complex intervals, independent source overlap, full rational numerator
and denominator, prime powers and CRT character inverses. Finite cases are
not a held-out normality experiment and never establish an infinite limit.

Exact live starting PR heads and workflow results are preserved in
[the start receipt](PI_SOURCE_GENESIS_START_STATE.json). At retrieval, the
source-fidelity workflow on #252 had passed, while its general validation
was still in progress. Final local and hosted results are recorded separately
in the delivery receipt, so earlier green checks are not transferred to the
new commit. The original import manifest and archival files remain unchanged.

The derivation tracks share a model family and source dossier. Their
independent algebra, exact implementations and kernel checks provide
cross-checks, not external academic refereeing. Source correctness, survival
under tested probes, tool contact and enthusiasm for the goal are kept
separate. The phases throughout are ordinary Fourier-character phases.
