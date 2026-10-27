# Independent finite source-fiber instrument

Status: exact finite identities and certified numerical enclosures. No normality, asymptotic cancellation, or growing signed saving is proved.

## Reproduction and independence

Run from the repository root:

```sh
python scripts/pi_prime7_source_fiber_probe.py --output research/2026-10-27/pi_prime7_source_fiber_receipt.json
```

The unchanged upstream probe can be recovered with `git show 95ee2f1fab851afe1517d8ec5a0589885842426f:scripts/bbp_prime_ramification_probe.py`; it was rerun before this round's independent instrument.

The original PR325 probe was extracted without edits from commit `95ee2f1fab851afe1517d8ec5a0589885842426f` and passed. The new probe independently implements the original four signed source poles, the zero-seed recurrence, A/D comparison, Bareiss/Sylvester resultants, projective fibers, and signed-energy assembly using standard-library rational arithmetic. It shares and labels the inherited `phase_interval`, outward rounding, and square-interval primitives; this is not a fully independent trigonometric implementation. Rational phases are reduced before approximation. No floating-point phase evaluation is used. Decimal strings are display only; the JSON stores outward rational endpoints.

Predeclared grid: q=7,11,13,241,49,343; h=1,2; N=2q,4q,8q. Models: authentic U; coherent one; changed seed -T; and #320 mutant. The changed-seed tail is enclosed by 16 exact terms and the proven remainder `1/(15*16^16*(n+17)^2)`; each phase coordinate is enlarged using derivative bound 2pi<44/7. This includes n=0 without invoking a nonexistent exact rational value of pi.

## Exact source algebra

The independent determinant calculations give:

- Res(A,D) = -7372800 = -2^15*3^2*5^2.
- Disc(D) = 3774873600 = 2^24*3^2*5^2.
- Homogeneous resultant = -1932735283200 = -2^33*3^2*5^2.

A separate SymPy calculation returned the same three integers; it is secondary and is not needed to run the probe.

A fresh identity, checked by rational polynomial coefficient arithmetic, is obtained for c=89/120:

`D(x)-D(c-x) = -(240x-89)(930A(x)-1243)/50625`.

Since A(c-x)=A(x), its projective cross-product version is

`A(x)D(c-x)-A(c-x)D(x) = (240x-89)A(x)(930A(x)-1243)/50625`.

This distinguishes numerator-fiber reflection from equality of the full rational source, and remains valid at poles. At p=7 the denominator-equal mirror residues are 2,3,6; 2 and 3 are both poles, and 6 is the branch point. At p=11 only the branch point survives. These are local source identities, not phase constraints.

## Finite signed-energy results

Let E=q/N^2 sum_r |Z_r|^2, C=q/N^2 sum_a |sum_{r:A(r)=a} Z_r|^2, and O=C-E. All intervals below are recorded exactly in JSON; the displayed decimals are shortened.

| q | h | N | C | O | mixed-stratum O |
|---|---:|---:|---:|---:|---:|
| 7 | 1 | 56 | 0.172655691344 | -0.014528058110 | 0 |
| 7 | 2 | 56 | 0.313854972360 | +0.026594910760 | 0 |
| 11 | 1 | 88 | 0.100200913341 | -0.046040171714 | 0 |
| 11 | 2 | 88 | 0.182776296279 | -0.000352967392 | 0 |
| 13 | 1 | 104 | 0.079853336730 | -0.035235197844 | 0 |
| 13 | 2 | 104 | 0.122735915808 | +0.019389928357 | 0 |
| 241 | 1 | 1928 | 0.134452041911 | +0.001027086127 | 0 |
| 241 | 2 | 1928 | 0.136560799433 | +0.012175562846 | 0 |
| 49 | 1 | 392 | 0.140863303237 | +0.002183980417 | -0.010584385588 |
| 49 | 2 | 392 | 0.136537704067 | +0.025074674480 | +0.011919648864 |
| 343 | 1 | 2744 | 0.148428170646 | +0.025736877115 | +0.019317585679 |
| 343 | 2 | 2744 | 0.116762744252 | -0.009231054131 | +0.004602998734 |

All 36 authentic cases have C strictly below all three coherent controls. This distinguishes only these controls and does not identify a source-specific asymptotic mechanism. For coherent phases, balanced N yields C=collision_count/q, namely 13/7 at q7, 19/7 at q49, and 25/7 at q343; C is not bounded by 1.

Predeclared simple conjectures receive explicit finite counterexamples:

1. **Always nonpositive authentic mirror contribution: refuted.** Overall 20 signed off-diagonal intervals are positive and 16 negative. Every p241 row is positive; p7,h2 is positive at all three N. At prime moduli, O is the nonfixed signed mirror term, with the branch subtraction already accounted for.
2. **Monotone C under doubling N: refuted.** p11,h1 increases from 0.416089567720 at N22 to 0.445918750657 at N44. p7,h2 increases from 0.303846609402 at N28 to 0.313854972360 at N56.
3. **Use only diagonal plus full mirror at prime powers: refuted.** All 12 q49/q343 cases have nonzero certified mixed-stratum contributions, of both signs.

The valid prime-power collision counts are 133 at q49 and 1225 at q343. The phase-free exact Gaussian control checks C=E+O and O=full-mirror+mixed on each tested q. Certified phase intervals are consistent with the same identity and the exact Cauchy inequality Weyl_square<=C.

## Geometric controls

| q | A-fiber collision count on affine residues | full rational-source collision count on P1(Z/q) | P1 domain size |
|---|---:|---:|---:|
| 7 | 13 | 20 | 8 |
| 11 | 21 | 28 | 12 |
| 13 | 25 | 38 | 14 |
| 241 | 481 | 500 | 242 |
| 49 | 133 | 266 | 56 |
| 343 | 1225 | 2744 | 392 |

The projective domain uses both affine (x:1) and (1:y) with p dividing y. Output equality uses unit-normalized projective coordinates, so poles are retained rather than inverted illegally. A and D have no common residue zero modulo any tested prime. Projective fibers are an arithmetic control, not extra physical observations or real-circle mixing channels.

The N=q*(2,4,8) grid does not establish q(N)=o(N); only a finite ratio change was tested. A universal signed-saving estimate remains open. The independent instrument was then integrated on the separate child research branch; validation is recorded in PI_PRIME7_ROUND2_VALIDATION.md.
