# Local prime resonance and interval audit

**Verdict: PASS within the declared scope, after one quantifier repair.**
This is a same-model research decomposition, not external refereeing or
formal-kernel verification. I read the complete `PRIME_WAVES.md` draft and
focused the audit on its finite sieve, Ramanujan correlation, CRT product,
singular-series limit, and endpoint / interval controls. I also checked the
displayed modulo30 transport and its braid mismatch directly.

## Derivation checks

- The phase is operationally fixed as `exp(2*pi*i*a*n/p)`, with ordinary
  reflection `n -> N-n`. Orthogonality leaves precisely matching frequencies;
  the normalized local correlation is `1+c_p(N)/(p-1)^2`.
- The resulting factors are `p/(p-1)` when `p|N`, and
  `p*(p-2)/(p-1)^2` otherwise. For `p=2`, the zero at odd targets concerns
  the screened bulk; an actual pair involving 2 requires the explicit
  exception term.
- CRT factorization applies to a full uniformly counted residue period.
  The finite Ramanujan expansion and primitive-denominator orthogonality
  give the same result without an infinite-series interchange.
- All primes through `floor(sqrt(X))` suffice to exclude a composite in
  `2..X`. Restoring a prime removed by its own filter gives the exact finite
  indicator. The pointwise product and the commuting operator product
  describe the same corrected filter on the stated window.
- For `Q=30, N=16`, the complete-period survivors are 17, 23, 29. Their
  normalized mean is 45/32, yet the interval 2..14 has no survivor. The four
  true ordered prime pairs all use the removed small-prime exceptions.
- The permutation preserving residues modulo 30 in WAV-08 leaves the specified
  finite observation bank unchanged. Direct evaluation gives the displayed
  `V_2^f S e_6=e_434` and `S^2 V_2^f e_6=e_14`; the small anchor alone
  therefore does not enforce the ordinary mixed relation.

One quantifier defect was found and corrected by the note's author: the
singular-series paragraph initially said only "fixed even N" and
"increasing finite prime sets". The corrected statement requires `N>=4`
even and sets exhausting all primes. At `N=0`, every prime divides N and
the proposed positive finite-limit argument would fail; a nonexhaustive
sequence also need not converge to the displayed full product. I inspected
the corrected wording. "Ramanujan characters" was also clarified to
"Ramanujan sums".

## Independent finite replay actually executed

From the repository root:

```bash
python research/2026-11-12/prime_fixed_point_observer/waves_independent_audit.py
```

The script imports no implementation from `prime_waves.py`. It computes
Ramanujan sums using the integer Mobius divisor formula, computes normalized
sieve fields and pair counts by gcd enumeration, and uses direct bounded
trial division for the finite prime comparison. All arithmetic comparisons
use integers or `Fraction`; no floating tolerance is used. Failure conditions
are explicit and the command exits nonzero if any comparison fails.

The persisted result is `receipts/WAVE_INDEPENDENT_AUDIT.json`, with the
script's SHA256 recorded inside it. The actual run returned **10,424 checks,
zero failures, PASS**:

| Calibration | Checks | Exact finite scope |
|---|---:|---|
| Finite Ramanujan expansion |249| Every residue for Q=1,2,6,30,210 |
| Reflected count versus CRT product |498| Every integer 0<=N<2Q for those Q |
| Reflected count versus Ramanujan diagonal |498| Same target range |
| Primitive-denominator orthogonality |1920| Every d,e dividing 30 and every N modulo 30 |
| Adaptive prime reconstruction |7140| Every 2<=n<=X<=120, z=isqrt(X) |
| Endpoint-corrected ordered pairs |117| Every integer 4<=N<=120 |
| Period and interval countercontrol |2| Q30,N16 |

These checks test the implemented finite identities and their boundary
conventions. They do not establish a universal additive lower bound, an
algorithmic speedup, or independence from the shared mathematical derivation.

## Primary provenance checked

- Ramanujan's original 1918 text, as a
  [transcription](https://ramanujan.sirinudi.org/Volumes/published/ram21.html),
  sections 1–2: divisor comb, Ramanujan sum, and Mobius relation. I did not
  inspect an archival facsimile.
- Tao's [sieve notes](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/):
  exact Legendre inclusion/exclusion, CRT counts, accumulated interval
  errors, and Exercise 25's Goldbach singular series. The note correctly
  distinguishes that factor from a proved binary asymptotic.
- Helfgott's [MFO snapshot](https://publications.mfo.de/bitstream/handle/mfo/429/Snapshot-2014-003-Helfgott.pdf),
  printed pages 4–6: Fourier convolution and the remaining binary remainder
  problem. The finite representation is not substituted for its estimate.

No infinite Ramanujan expansion of a prime indicator or von Mangoldt
function is used. In particular, increasing an uncorrected sieve product
over all primes eventually deletes every fixed integer at least 2, including
prime inputs; it is not a pointwise prime-indicator limit. The draft retains
that boundary explicitly.
