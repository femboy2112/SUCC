# Independent cross-reviews of the conic and finite Fourier packages

Date: 2026-10-21. Reviewer: separate Main VIII hostile-referee agent.
These are mathematical reconstructions by a separate agent, not an external
human referee or formal-kernel verification. No universal theorem is inferred
from the finite test receipts. Neither package changes an unrestricted open
problem's status.

## Conic high-divisor theorem

Final verified source commit: `b013a937497c652a7665d6808bda7b7d250d2758`.
The initial review read **uncommitted working-tree files** atop checkout
`fb5e36a0aa326172624a9d5471906bdba7309567`; that commit contained the preceding
arithmetic audit and did not contain the conic files. The earlier wording
“reviewed commit” for that checkout was incorrect and is corrected here.

| File | SHA-256 |
|---|---|
| `research/2026-10-21/VIII_HIGH_DIVISOR_CONICS.md` | `984903675d0e7b635f9895e4a6acd4879d15539480100e1d49b14f7c640efb0a` |
| `observational_succ/viii_high_divisor.py` | `cc5cd6b8e5ca62a962a12a0438f29cd95656f07ee538be33311e82bdcacb8306` |
| `tests/test_viii_high_divisor.py` | `d4d7d84288d518b18c134f32c04793058a25af3fbebb45183acaa59069e8677a` |

These hashes were calculated from `git show` at the final commit, not merely
from the checkout. The implementation hash is identical to the initial review.
The dossier gained an appended “Reproduction receipt” section: removing that
section reproduces the original reviewed file byte-for-byte, SHA-256
`10f99dd1dcf6bdc4d1e134a02b79a85a3654aefb7e9721714bcb6fa59becfe00`.
The appended receipt has now also been read. The theorem and proof text are
unchanged; this reconciliation does not silently equate unequal file hashes.

**Verdict: SURVIVES as a restricted-family paper theorem.** The following
load-bearing steps were reconstructed directly from the displayed formulas.

1. For `Q=u n^2+v m^2`, `L=u r0 n+v s0 m` and the stated quadratic map F,
   expanding the quadratic form cancels both cross terms and gives the source
   conic. If `g=gcd(F1,F2,F3)`, the two coordinate identities and Bezout for
   `(n,m)=1` give `g|2 z0 L`, while `g|z0 Q`. Hence
   `g|2 z0 gcd(Q,L)`. The two remaining identities force
   `gcd(Q,L)|w z0^2 gcd(v m^2,u n^2)`. Prime by prime the last gcd divides uv,
   proving `g|2uvw z0^3` without a coefficient-coprimality assumption.
2. A rational point other than the displayed point determines a rational line
   direction, reducible to coprime signed integers. Its second intersection is
   the displayed F formula. Division by g gives the unique primitive root
   vector with positive z. The seed exception adds at most one vector.
3. The height implies `Q<=2uv sqrt(w) z0^2 sqrt(X)`. Rectangle enumeration,
   including redundant signs, bounds the number by
   `(10+4 sqrt(2))z0^2 sqrt(uvwX)<16z0^2 sqrt(uvwX)`. The constant genuinely
   includes both boundary terms and the exceptional seed.
4. Source primitivity is stronger than root primitivity and is explicitly
   retained. The selected square weights are at most `(rsz J)^t`. The full
   source weight is at most `(uvw rsz J)^t`, because
   `rad(uvw r^2s^2z^2)>=rad(rsz)`. This remains true when roots and coefficients
   share primes. The two distinct weights are not identified.
5. AM–GM gives `rsz<=X^(3/2)/(2 sqrt(uvw))`. Multiplying by the conic count
   yields the two stated catalog factors with exponents `(1-t)/2` and
   `(1+t)/2`. The catalog `w=u+v` supplies the seed `(1,1,1)` uniformly;
   arbitrary catalogs still require explicit seeds and their height factors.
6. At `(t,kappa,theta)=(5/7,1/2,1/100)`, independent rational arithmetic gives
   selected exponent `1367/700` and source exponent `691/350`. Both are less
   than 2. For a nonempty dyadic shell, `Q<D<=X^3/(4uvw)<X^3`; therefore the
   total subquadratic bound implies the displayed `33/700` dyadic saving.
   This last step uses the bounded support of Q, not a new uniform CRT estimate.

The root-depth restriction, selected-divisor multiplicity, source-union
overcount and growing-catalog dependence are stated and paid. No proof was
found for removing the depth restriction, covering nonsquare powerful divisors,
or summing unrestricted cofactors. Those remain separate obligations. The
squarefree-Pythagorean-root proposal is correctly identified as empty: the even
leg of a primitive Pythagorean triple is divisible by 4.

Focused receipt in the reviewed worktree:

```sh
python -m unittest discover -s tests -p test_viii_high_divisor.py -v
```

The **initial uncommitted working-tree run passed 10 tests**, Python 3.12.
After the independent-review control for primitive roots with nonprimitive
sources was added, the **replay at the clean final commit passed 11 tests**,
also Python 3.12. The original 10-test receipt is retained as historical
evidence, not described as a run of the later 11-test file. Neither replay is
claimed to be an independently implemented second census; the independent
evidence here is the separate proof reconstruction above. Existing constructor
tests already compare different finite enumeration mechanisms.

## Finite polygon-source Fourier enclosure

Reviewed commit: `41e12b57dffa618f4231cbccf48429dad8ba5e32`.

| File | SHA-256 |
|---|---|
| `observational_succ/pi_fourier_certificate.py` | `7acaf600b028029a828a3b863695002e5dc4e8fbbc08869398f3632f840ab737` |
| `research/2026-10-21/PI_FOURIER_CERTIFIED_FINITE_ORACLE.md` | `cbb9cf00de74452329a0b0ac573b40f08c843bb764b778bcebcd6da62d21192d` |

**Verdict: SURVIVES as a finite exact-enclosure package.** Its two uses of pi
are correlated but do not require independence. The first triangle-inequality
step transports the orbit source from pi to the rational polygon midpoint
under the **true** Fourier character, whose Lipschitz constant is below
`8|frequency|`. The second step changes the radian conversion constant for
each now-exact rational phase, with coordinate error `2|turns|*radius`.
Both error budgets are explicitly added.

The phase is reduced modulo **one turn before** multiplication by the rational
pi approximation. Thus no approximate radian period is incorrectly treated as
exact. Negative frequency and wraparound are safe under the circle-distance
Lipschitz estimate. The cosine and sine polynomials have the next odd/even
Taylor coefficient zero, so the claimed Lagrange remainder orders are valid
without an alternating-term monotonicity assumption.

The coordinate rectangle contains the true mean. Summing minimum coordinate
squares gives a valid lower squared-modulus bound even with correlated errors;
summing maximum squares gives an upper bound. Intersecting the upper bound
with 1 is valid because an average of unit characters has norm at most 1.
Coarse valid brackets can give `[0,1]`; the module does not claim precision
independently of its resource parameters. Internal public results are data
records, not admitted formal/source proof authority.

Focused receipt in the reviewed worktree:

```sh
python -m unittest discover -s tests -p test_pi_fourier_certificate.py -v
```

**6 tests passed**, Python 3.12, including the supplied Machin/nested-radical
holdout. The separate evaluation mechanisms share the elementary Lipschitz
transport inequality. This replay does not create a third numerical method.
The enclosure for the single horizon N=32 is accepted only at that finite
scope. No normality, asymptotic cancellation or uniform-horizon conclusion
follows from it.
