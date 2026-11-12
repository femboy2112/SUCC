# Prime-wave adversarial audit

Date: 2026-11-12. Parent publication: `b3ddf81c4e893866aac04903f682fb5aa01830e2`.

**Verdict: PASS within the stated finite and analytic domains, after two
input-contract repairs.** No remaining mathematical or executable blocker
was found in this review. This is a same-model adversarial decomposition,
not independent external refereeing or formal-kernel certification.

## Scope and inspected snapshot

Read `AGENTS.md`, `docs/METHOD.md`, the preceding carrier/cylinder source
boundaries, and all of `PRIME_WAVES.md`, `prime_waves.py`, `wave_probe.py`,
and `test_prime_waves.py`. Only this audit document was written by the
auditor; implementation repairs were made by the root agent.

The repaired executable snapshot inspected was:

| File | SHA256 |
|---|---|
| `prime_waves.py` | `68604be9c4655281be1926029c55aaddc36fe72c5521f358a9b187411898db30` |
| `wave_probe.py` | `026cf807aa84c1a85031f8bc7f45fa854b2f16e014a226694475a942ac25ab01` |
| `test_prime_waves.py` | `8082e86e310e69e020e427ffb8d5dbcf79a38faf0fbf0bf73103cf0b25752b8b` |

The main receipt and full dossier-suite replay are the root agent's separate
validation. Their counts are not included in this audit's checks.

## Mathematical review

1. **Category and maps.** Finite-support graded vector spaces with the
   additive convolution tensor have the indicated canonical associativity,
   symmetry, and unit. Dilation is strong symmetric monoidal because
   `m(a+b)=ma+mb`. The action-category composition has the correct order:
   `(k,g) o (m,f) = (km, g o D_k(f))`. The selected positive-label arrows
   form a copy of Div, rather than the full subcategory with all scalar
   and zero maps. The author added the requested explicit wave target for
   action arrows: covering-pullback intertwiners with the same composition
   law. These are not ordinary intertwiners between different circle
   characters. The added paragraph was reread and accepted.
2. **Hilbert domains.** The positive-frequency Fourier carrier is appropriate
   for `ell^2(N_{>=1})`. The operators S and V_m are isometries, while U_alpha
   is unitary. The projection identity `V_m V_m* = mean_j U_(j/m)` is exact.
   The sum of prime-power divisor projections defining N_Omega is locally
   finite on the declared finite-support core; its diagonal extension has
   the stated weighted domain. The note explicitly excludes zero here and
   explicitly records that the unrestricted addition map on a Hilbert
   tensor product is unbounded.
3. **Prime sieve.** The exception `n=p` is necessary and correctly restored.
   Integer cutoff `z >= floor(sqrt(X))` is sufficient on `2..X`, including
   the minimal windows X=2 and X=3. A fixed cutoff retains omitted prime
   squares, which correctly prevents a global operator-norm convergence
   claim.
4. **Signed interference.** In the reflected local correlation, expansion
   gives `e((a-b)n/p) e(bN/p)`, so averaging retains a=b. This produces
   `c_p(N)` with the claimed orientation. In the ordinary additive source,
   F squared records sums and absolute-F squared records differences.
   A cyclic coefficient product uses frequency addition, including signed
   frequency representatives; it is not conjugation or subtraction.
5. **Complete periods and intervals.** The CRT product is an exact full-period
   count. It does not describe an arbitrary finite interval without a
   remainder term. For Q=30 and N=16, the survivor residues 17,23,29 give
   normalized period correlation 45/32, while the target interval 2..14
   has no bulk survivors. The four genuine prime pairs use the removed
   small-prime exceptions. The endpoint expansion handles this correctly.
6. **Reference reconstruction.** The imaginary-part formula has the correct
   sign: `(|F+i|^2 - |F-i|^2)/4 = Im(F)`. The reference constant is the
   zero additive frequency, not the wave of multiplicative unit 1. For
   support 0..X, M>X is sufficient to recover F and M>2X to recover its
   square by a single uniform discrete Fourier bank. These are sufficient
   finite-window bounds, not a fixed global resolution claim.

## Exact adversarial receipts

The homometric pair is

```text
A = (2, 3, 6, 12, 14, 19)
B = (2, 3, 10, 13, 15, 19)
positive differences in both = (1,2,3,4,5,6,7,8,9,10,11,12,13,16,17)
each positive difference has multiplicity 1; zero has multiplicity 6
ordered sum8 counts = (2, 0)
```

This defeats determination of every sum fiber from complete Fourier
intensity for arbitrary finite indicator sources. It does not establish
ambiguity restricted to a class already specified to be the actual primes.
The known pair was checked against the primary full text of
Ranieri--Chebira--Lu--Vetterli, *Phase Retrieval for Sparse Signals:
Uniqueness Conditions* (2013), section IV-A:
<https://arxiv.org/html/1308.3058v2>. The shift by 2 and the sum8 observation
are explicit applications of that classical control.

For the modulo30 transport, an independent square-root trial-primality and
factorization script verified the swaps
`7<->217, 11<->341, 13<->403, 17<->527, 19<->589, 23<->713`.
It found 127 genuine and transported prime labels in 2..713, identical
complete `(n mod30, Omega)` histograms, and ordered sum30 counts 6 versus0.
The first V_2/S braid mismatch occurs at basis index6, with outputs434
and14; V_2 at the unit still gives2. The note gives a universal finite-swap
argument for every window X>=713, rather than inferring it from these runs.

## Executed independent checks

A separate inline Python audit ran **10,999 exact checks, zero failures**:

| Group | Exact checks | Method / scope |
|---|---:|---|
| Signed cyclic products | 117 | Rational sparse inputs, including negatives and cancellation; independent SymPy polynomial product modulo z^m-1, m=1..13 |
| Endpoint expansion at all selected cutoffs | 5,335 | Every N=4..100 and every cutoff1..N+3, compared with direct construction of the screened-plus-exception source |
| Certified endpoint result | 4,827 | Every above cutoff at least isqrt(N-2), compared with a fresh direct trial-primality pair count |
| Signed complete-period counts | 336 | Empty bank and banks (3,11), (2,7), (5,7), targets -2Q..2Q |
| Signed CRT factor equality | 336 | Same banks/targets, exact rational comparison |
| Pulse unit and signed arguments | 36 | Moduli1,2,4,6,9,25 and arguments-100,-1,0,1,2,100 |
| Empty/minimal prime producer | 3 | Bounds0,1,2 |
| Minimal prime windows | 2 | Windows2,3 |
| Multiplicative unit valuation | 1 | v_2(1)=0 |
| Rational reference recovery | 6 | Three nonintegral/zero complex amplitudes, two components each |

These counts are finite software checks. They are not additional universal
theorems or a replacement for the written proofs.

An additional explicit input matrix produced **80 expected ValueError
rejections**, including invalid exact-integer types, prime moduli,
nonpositive divisibility moduli, invalid windows/cutoffs, nonpositive
valuation arguments, targets below4, invalid source labels, invalid
transport flags, nonbinary mask entries, and a bad rational coefficient
paired with an empty spectrum. Legitimate signed periodic arguments and
the additive label0 were separately retained where their APIs allow them.

The repaired regression method was independently rerun:

```bash
PYTHONPATH=research/2026-11-12/prime_fixed_point_observer \
  python -m unittest \
  test_prime_waves.PrimeWaveTests.test_prime_modulus_and_exact_input_guards -v
```

Actual result: **Ran 1 test; OK**. This targeted replay is separate from
the root agent's complete new test-suite run.

## Defects found and repaired

- The first inspected `pair_count` validated target and mask length but did
  not validate mask entries. A fractional mask entry could produce a
  fractional result despite the binary-mask/int-result interface. Root
  added exact-int bit validation over the whole mask and regression cases
  for float, bool, out-of-range int, and Fraction inputs.
- The first inspected `cyclic_product` validated the right spectrum inside
  the left-product loop. An empty left input could therefore skip an invalid
  coefficient on the right. Root moved validation of both spectra before
  the product loops and added the empty-left regression.

The repaired code rejected both reported cases during the independent
10,999-check execution and again in the input matrix. These guard repairs
do not alter the valid-input formulas or the mathematical claims.

## Reproduce the independent arithmetic check

Run the following Python from the repository root. It uses exact fractions
and symbolic polynomial quotients; it does not use floating tolerances.

```python
import sys
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import gcd, isqrt
import sympy as sp
sys.path.insert(0, str(Path(
    'research/2026-11-12/prime_fixed_point_observer').resolve()))
import prime_waves as w
checks = Counter()
def check(condition, group):
    checks[group] += 1
    if not condition:
        raise AssertionError(group)
def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))
z = sp.Symbol('z')
lefts = ({-3:F(2,3), 0:F(-1,2), 5:F(1)}, {-1:F(1), 2:F(-1)}, {})
rights = ({-2:F(3), 1:F(1,4), 4:F(-1)}, {0:F(1), 7:F(-2)}, {})
for m in range(1, 14):
    for a in lefts:
        for b in rights:
            pa = sum(sp.Rational(v.numerator,v.denominator)*z**(k % m)
                     for k,v in a.items())
            pb = sum(sp.Rational(v.numerator,v.denominator)*z**(k % m)
                     for k,v in b.items())
            rem = sp.Poly(pa*pb,z,domain=sp.QQ).rem(
                sp.Poly(z**m-1,z,domain=sp.QQ))
            expected = {k:F(rem.nth(k)) for k in range(m) if rem.nth(k)}
            check(w.cyclic_product(a,b,m) == expected,
                  'signed_cyclic_polynomial')
for N in range(4, 101):
    expected = sum(prime(n) and prime(N-n) for n in range(2,N-1))
    for cutoff in range(1, N+4):
        row = w.endpoint_decomposition(N,cutoff)
        ps = [p for p in range(2,cutoff+1) if prime(p)]
        source = [0,0] + [int(prime(n) if n <= cutoff else
                              all(n % p for p in ps))
                          for n in range(2,N-1)]
        expanded = sum(source[n]*source[N-n] for n in range(2,N-1))
        check(row['total'] == expanded, 'endpoint_all_cutoffs')
        if cutoff >= isqrt(N-2):
            check(row['total'] == expected, 'certified_endpoint_cutoffs')
for ps in ((), (3,11), (2,7), (5,7)):
    m = 1
    for p in ps:
        m *= p
    for N in range(-2*m, 2*m+1):
        row = w.periodic_pair_receipt(ps,N)
        survivors = sum(gcd(n,m) == 1 and gcd(N-n,m) == 1
                        for n in range(m))
        check(row['count'] == survivors, 'signed_period_targets')
        check(row['normalized_correlation'] == row['factor_product'],
              'signed_period_factor')
for m in (1,2,4,6,9,25):
    for n in (-100,-1,0,1,2,100):
        check(w.divisor_pulse(m,n) == int(n % m == 0), 'pulse_units_signed')
for n, expected in ((0,()), (1,()), (2,(2,))):
    check(w.primes_through(n) == expected, 'empty_prime_bound')
check(w.corrected_prime_mask(2) == (0,0,1), 'minimal_prime_window')
check(w.corrected_prime_mask(3) == (0,0,1,1), 'minimal_prime_window')
check(w.valuation_from_pulses(2,1) == 0, 'unit_valuation')
for real,imag in ((F(-2,7),F(11,3)), (F(0),F(0)), (F(1,9),F(-5,4))):
    plus1,minus1 = (real+1)**2+imag**2, (real-1)**2+imag**2
    plusi,minusi = real**2+(imag+1)**2, real**2+(imag-1)**2
    check((plus1-minus1)/4 == real, 'rational_reference_recovery')
    check((plusi-minusi)/4 == imag, 'rational_reference_recovery')
print(sum(checks.values()), dict(checks))
```

## Boundaries and next falsifier

The primary-source framework, analytic derivations, and exact finite checks
support the proposed category extension and its observation formulas.
They do not establish physical radiation, a computational speedup, a
uniform binary Goldbach estimate, or a machine-checked proof. The code is
an exact rational finite implementation; the written complex-source
identities have broader algebraic domains than this implementation.

A future positive estimate must retain its source coupling, handle the
small-prime exceptions, and bound the actual interval/Fourier remainder.
Reproducing a local positive density or a shared spectral intensity remains
insufficient, with the receipts above available as regression controls.
