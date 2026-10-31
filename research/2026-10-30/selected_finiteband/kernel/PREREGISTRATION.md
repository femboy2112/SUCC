# Kernel audit: hypotheses and discriminating probes

Recorded before executing this front's new tests. Parent: PR411,
`fa598e3a5a1111c3445200f1ddf48dcdea6bdc09`. All edits are additive here.

| Claim | Predicted PASS | Predicted FAIL / boundary | Small decisive probe |
|---|---|---|---|
| K01 Fejer feature transport improves the original source error to `C H/N` in square-root energy | Authentic source at zero and rational seeds; same source coherent seed | This is not a zero-seed discriminator; an inferred cancellation theorem must fail on coherent seed | Exact coefficient moments, rational source tails, independent pair/frequency evaluations |
| K02 Native `T_n~1/(64n²)` makes transport order sharp with coherent coefficient `pi/15` | Coherent same-forcing seed, `H→∞`, `N/sqrt(H)→∞` | Zero-seed sharpness is AMBIGUOUS; no inference from coherent control | Separately evaluated Mellin constant and fresh coherent pair energies |
| K03 Smaller band `H=q/4` keeps the inherited cylinder constant; `H=3q/8` improves it | Every finite sample, including seams, singleton, coherent and rational aliases | Does not constrain source-selected energy | Rational seam grids and symbolic constants |
| K04 Prescribed polynomial moving depths are sufficient but not necessary for normality | Slow-normal zero-density surgery preserves normality and fails the certificate | Universal fixed-clock necessity is REFUTED | Exact inserted-zero counts and asymptotic density proof |
| K05 Parent entropy implications and fixed-depth maximum-cylinder criterion survive independent audit | Deterministic overlapping streams, all `N,m,k`; stationarity of cluster limits | No source upper bound is obtained; fixed-depth calibration alone is insufficient | Exact small binary census and periodic controls |

Numerical tests of trigonometric values are calibration, not interval proofs.
The all-parameter conclusions are paper proofs. The separate oracle uses a
different source formula and pair-kernel evaluation; it is another implementation
by the same model, not an independent referee. No Lean claim is made.

Fresh holdouts after the initial suite: `(N,H)=(19,7),(41,29),(73,127)`,
rational seeds `2/9,-7/13`, and coherent `(N,H)=(1536,768),(4096,2048)`.

PASS means the stated exact identities or proved inequalities survive the
declared finite calibration. FAIL means an explicit mathematical counterexample
or violated assertion. AMBIGUOUS means numerical uncertainty or a claim about an
unproved infinite limit; no finite count promotes the latter.
