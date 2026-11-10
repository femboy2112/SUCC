# Hostile proof and instrument review

Reviewed against parent `1990b05117d84b33094c8e0f53f7d19b60f48060`.
This is a separate same-model reasoner and independent exact implementation,
not external scholarly refereeing. Proof status and execution status remain
separate.

| Claim | Verdict | Scope and receipt |
|---|---|---|
| Original covariance -> full Weyl -> normality | SURVIVES, proved conditional chain | H5 supplies explicit arbitrary-prefix gluing and Green-tail indexing. Every integer A and every fixed nonzero h are required. |
| Exact transported lag gate | SURVIVES, proved equivalent reduction | H1--H3 retain signed terms, all source forcing, and boundary support. No source-selected upper decay estimate is proved. |
| Dropping forcing at polynomial aperture | UNSUPPORTED by the derived bound | H4 retains the exponential phase-error budget. Exact forcing transport avoids that approximation. This does not prove such an untwisted estimate false. |
| Large local cancellation implies full cancellation | REFUTED as a general inference | Coherent and periodic completed orbits have energy tending to1; prior rational shadows have matching local clocks and covariance tending to1. Literal-zero authentication rejects these sources. |
| Energy decay with an unrestricted aperture proves Weyl decay | REFUTED | H6: f=1, H=A² gives E_H->0 but W=1. The finite support factor is indispensable. |
| It suffices to check dyadic starts A=2^j for arbitrary bounded sequences | REFUTED | H5 first-half-plus/second-half-minus control has zero complete dyadic blocks but prefix limit along 3*2^(j-1) equal to1/3. |
| CH1--CH6 local history laws | SURVIVES, paper review | Checked modular versus integer resonance, finite Fourier normalization, interval rounding, TV factors, next-birth endpoint count, sensor margin and carry inverse-limit fiber. These concern the changing prime component. |
| CQ1--CQ6 local cubes and improved sparse budget | SURVIVES, paper review | Checked exact final-shift squared mean, degeneration count, growing-depth necessity, finite-group cube Cauchy--Schwarz convention and fourth-moment support bound. The same complement residual remains unpaid. |
| EC1--EC4 quantitative selector and explicit local exponent | SURVIVES, paper review | Independently checked short-interval prime count versus logarithmically restricted order exceptions, all normalized Cochrane--Pinner exponents and rational eighth powers, gluing, observer budgets and signed-gate overhead. |
| Root interval energy/covariance implementation | SURVIVES, exact finite replay | `INDEPENDENT_REVIEW.json`: 3,759 energy containments and 1,360 covariance containments against independent Gaussian-rational arithmetic. Reviewed source files are hash-qualified. |
| Root explicit integer selector | SURVIVES, exact finite replay | 384 maximality checks at A=1..128, C=1,2,3 against trial-division primes and literal multiplication orbits, independent of the production sieve and factor-stripping order routine. |
| Integer recurrence transport | KERNEL-CHECKED, narrow algebraic scope | Lean4.14 core proves zero boundary, exact transport, seed dependence and window composition; axiom report has only `propext` for the nontrivial theorems, no `sorryAx`. Four rational poles and asymptotic analysis remain outside this file. |

The root runner's `unsigned_energy_bound` uses absolute values of the **real
lag correlations**, not the modulus of each complex correlation. This is a
valid upper replacement for the signed energy. Its failure to decay diagnoses
the loss incurred by discarding signs, without asserting that every possible
unsigned bound fails.

For EC1--EC4, this front independently reopened the
[Cochrane--Pinner author manuscript](https://www.math.ksu.edu/~cochrane/research/binsum7.pdf),
including Theorem1.1 and the paragraph after1.2 confirming validity outside
the displayed optimality ranges. The normalized third estimate gives
delta<=lambda p^(-1/16)b(p)^(3C/8), and lambda^8=256/9 exactly. The
[fixed-modulus PNT/AP statement](https://www.math.tau.ac.il/~rudnick/courses/sieves2015/fixed%20progressions.pdf)
has the error needed when subtracting endpoints separated by X/(log X)^B.
All are classical imported results, not finite-test consequences.

The gluing calculation has an especially simple check: p<=4A and p=1mod4
force d=A-(p-1)/4>=1. Then the exact overlap is max(0,A-2d+1), so
epsilon<= (4d-2)/A <=4d/A. Thus both the initially conservative +3/A
and the simpler +1/A asymptotic remainders are valid; a d=0 case is
unreachable for this selector. No power saving in the epoch-gluing error
is claimed by this argument.

The runner independently checks exact rational source-phase transport at
three selected lags per frequency, checks direct modular source sums at four
selected times per epoch, and retains the omitted-forcing mutations. Those
checks complement the Gaussian-rational tests here; both still reuse the
same declared original source contract. The interval phase instrument is
inherited from the preceding audited round, not independently reimplemented
again in this front.

`exact_oracle.py` passed **73,484 counted exact checks**, plus six focused
unit tests. The largest family is exhaustive finite moving-energy algebra
over 1,364 Gaussian-unit sequences of lengths1 through5, not 73,484
independent asymptotic experiments. The exact rational source grid and all
combinatorial budgets were fixed before these checks ran. The successful
signed-control receipt is length32/aperture8: energy1/256, while replacing
signed real correlations by their absolute values gives235/256.

Commands:

```sh
python3 -m unittest discover -s research/2026-11-08/signed_covariance_round2/hostile -p 'test_*.py'
python3 research/2026-11-08/signed_covariance_round2/hostile/exact_oracle.py --output /tmp/succ-hostile-exact.json
python3 research/2026-11-08/signed_covariance_round2/hostile/review_instrument.py --output /tmp/succ-hostile-instrument.json
```

The Lean command is
`/usr/bin/lean research/2026-11-08/signed_covariance_round2/hostile/ExactTransport.lean`.
The first development attempt failed because rewriting did not match a
normalized Nat-addition expression. Replacing that step with a direct
congruence proof compiled successfully; the final axiom output, rather than
the failed development output, is retained in `LEAN_RECEIPT.json`.

No independent proof of the authentic signed upper bound and no RH theorem
is supplied here. **pi base16 normality: OPEN. RH: OPEN.**
