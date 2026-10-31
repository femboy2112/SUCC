# Selected transport bearing: declarations before new probes

Parent PR417 `1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`.
Read-only input PR421 `e14916aa2b4dfc2cce948facc729fb02ce1efafa`
already supplies first-order and centered prime-frame transport. Its PF1–PF4
are credited; this bearing tests growing-order, bounded-radius frames.

## ST1. High-order genuine prime-frame derivative

Let `f_n(u)=log B_n(u)` for the authentic zero-seed BBP multiplicative
carrier. For integer m>=1 use nodes `u=j/(2m)`, -m<=j<=m, and the derivative
of the degree-2m interpolation polynomial at zero. Predicted theorem:

`0 < (-1)^m (U_n-A_(n,m)) <= E_(n,m)` for n>=1,

`E_(n,m)=8(16^n-1)/(15(2m+1)) * (m!/m^m)^2`.

PASS: exact stencil moments and signed rational log intervals validate the
inequality, a repeated-Rolle proof establishes it for all n,m, and fresh
SymPy Vandermonde weights plus high-precision direct source provide a
separate implementation. FAIL: wrong stencil/sign, a certificate violating
the interval, or failure to bound the actual source derivative. AMBIGUOUS:
interval too wide; increase certified log precision without changing cases.

Predictions: authentic source PASS; positive rank-two mutant also admits its
own derivative constants (therefore not a normality discriminator); coherent
seed requires its own initial-germ term; any finite frame family has a
polynomial seed-germ alias unless initial B0 is fixed. Altered poles do not
inherit the authentic constant without a proof. No cancellation claim.

Discovery cases: (n,m)=(1,1),(2,2),(3,3),(5,4),(8,6).
Fresh holdouts: (4,5),(7,7),(11,10),(17,13). All use the literal four poles.

## ST2. All-horizon precision transport

Use `m_n=4n+ceil(log2((n+1)^2))+4`. Predict summable state/character error
with only O(1/n) frame spacing, but O(n) or more log-value accuracy bits.
PASS: exact factorial inequality, rational error budget and stencil norm
prove the declared uniform Weyl comparison. FAIL if spacing savings are
misrepresented as cancellation or an overall computational speedup.

## ST3. Fibonacci coverage

Try a uniform signed bound over Fibonacci blocks attached to a Zeckendorf
tiling. Prediction: gluing preserves the actual source and literal zero
boundary, but bare partitioning gives only the triangle inequality.
Fibonacci-prefix cancellation alone is predicted insufficient for all
horizons among general unit complex sequences; construct an exact control.
PASS: exact coverage bound with all quantifiers and counterexample.
FAIL: any claim of BBP cancellation from Fibonacci eigenvalues alone.

## ST4. Actual selected cancellation

Target: one fixed-frequency uniform macroscopic BBP saving stronger than
the inherited logarithmic loss. Keep full CRT products and literal source.
Any finite positive result remains OBSERVED; a bound shared by coherent
same-forcing controls cannot prove normality. Status initially DARK.

Same-model agents and implementations are not independent external referees.

Before the new signed probe, fix primes 4201,5009,6013,7001, frequencies17,19,
and64 terms beginning at each prime's first authentic pole encounter.
PASS for the finite calibration means the **full** normalized signed
sum has squared modulus below1/4 by outward integer intervals; FAIL means
the interval proves it is at least1/4; crossing the threshold is AMBIGUOUS.
Primary-only and full products are both reported, never modeled independent.
These finite windows are not claimed to cover all large times. A failure of
primality or order>=64 is an instrument/domain failure, preserved as such.
Coherent and period-01 controls should expose lack of universal dispersion;
the seven-pole null source should give zero late low-threshold lag slips.

Domain failure before any signed window was measured: 6013=7*859 is not
prime. The initial source and failed receipt are preserved. Repair rule,
declared before any replacement phase measurement: replace6013 by the least
larger integer congruent1 mod4 that is prime and has order16>=64. Retain
all other primes, windows, frequencies, thresholds and controls unchanged.

## Retained control replay and analytic crosscheck

Before replay, expect PASS for the inherited 19-test `arithmetic_barrier/transfer`
suite at PR415 commit `f650aab0c8710b502f3e08ec1cb2b351c26b2b3f`.
This checks the already proved Stoneham 3/5 controls and conductor-2
adversary, p73 disappearance, rational aliases, all Walsh characters,
positive/Gamma/higher-jet mutants, periodic de Bruijn, sparse Kempner,
biased laws and a finite Champernowne prefix. PASS reproduces the inherited
tests; it does not independently establish their asymptotic theorems.
FAIL preserves a changed test/runtime result. No sibling file is integrated.

For the analytic front A01--A03, independently construct its d=1 Gaussian
source from the first three rational source moments. Predict strict enclosure
inside the direct 40-term BBP interval, agreement of the first two source
values, strict third-value deficit, rational completed boundary and the
exact tail-budget identity. Also check the biased full-support collision
factor 64/15 and non-Pisot polynomial x^2-x-3 by rational sign witnesses.
These are finite algebraic crosschecks alongside a separate written proof
audit, not external mathematical review.
