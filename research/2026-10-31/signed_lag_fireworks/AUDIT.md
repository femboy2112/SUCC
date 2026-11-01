# Integration and adversarial source audit

The starting integration commit is `030ee84b8b7f655fcf433375bfc0b347e0483c89`.
This audit reads the actual PR #431 carrier, #432 edge/seed tomography,
#433 selected-seed superposition, and #434 signed-lag modules, their independent
oracles, proofs, and root tests as integrated at that commit. All 15 Git blob
identities tabulated in the parent `INTEGRATION.md` match the local bytes:
eleven #432 imports and four #434 authored source/test files. The original
72-item archival import verifier also passes. These checks establish source
identity, not mathematical truth. Historical source and test bytes are preserved.

The four focused imported suites pass separately: 20 carrier, 21 edge, 28 seed,
and 28 lag tests. Their raw results, exact commands, hashes, and timings belong
to the baseline receipts accompanying `VALIDATION.md`. Full regression is a
separate check. Copies of a shared BBP formula or imported proof are not counted
as independent mathematical witnesses.

## Two inherited interpretation traps, with exact regressions

**Modulus versus signed real part.** The parent helper
`selected_lag.coherent_lag_lower_bound(N,k,h)['normalized_lower']` returns
`max(0,N-k-error)/N`. It is a valid lower bound for the normalized **modulus**
of the coherent lag sum. It is not generally a lower bound for its signed real
part. The parent weighted coherent certificate instead uses the unclipped
`mass-error` and is unaffected.

An exact counterexample to the signed reading is `N=2,k=1,h=4` at the symbolic
coherent seed `s*=-pi/16`. There is one term,

```
D = e(-60 T_1),    T_1=sum_(j>=1)16^-j r(1+j).
```

The independent combined rational source
`r(n)=(120n²-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)]` and four positive tail terms
give rational `a<T_1<b`, with remainder bounded by
`16^-4/[(8*5+1)(8*5+2)]`. Exact arithmetic verifies
`1/4<60a<60b<3/4`, proving `Re(D)<0` without numerical trigonometry. The
parent outward cosine oracle plus its Lipschitz error further verifies
`Re(D)/2<-49/100`. The helper returns zero. It must therefore never be used
as a signed lower bound. No historical helper is rewritten or silently given
a new contract.

**Source label versus literal selector.** The inherited
`seed_superposition.seed_phase_boundary(s,depth,h)` returns the constant label
`original-four-pole-BBP-U0=0` for both `s=0` and, for example, `s=1/7`.
Its `point_seed` field correctly retains the supplied exact seed. The label
alone therefore cannot authenticate the zero boundary. New consumers must
check the literal exact seed and the actual recurrence/source parameters.
The new regression exhibits the identical label and unequal `point_seed`
fields, while preserving the old implementation. A rational changed seed is
a source-authentication counterexample, not a claimed nonnormal orbit; Wall's
rational-shift correction remains in force.

All coherent, dyadic-completed, and 3/5-completed hostile seeds in this dossier
are irrational BBP seeds. They do not refute a theorem quantified only over
rational seeds. Such a theorem could use exact rationality or denominator
information to exclude them; it would still need an actual arithmetic proof.

These tests are in `tests/test_signed_lag_fireworks_audit.py`. They prevent
semantic promotion of inherited finite instruments. Neither is evidence
against the original zero-selected pi orbit or a replacement proof of its
signed asymptotics.

## New proof and interval audit

The clipped transport coefficient was derived separately from
`F_(n,k)<(16^k-1)/(64n²)` and the two chord bounds. Integrating the decreasing
majorant gives `sqrt(11|h|(16^k-1)/14)`, agreeing with `TRANSPORT.md`. The
triangular geometric sum gives the stated `8 B_h 4^K/(9K²N)` error. The
rounded square-root budget remains below the integer grid point `B_h4^k`.

The independent phase instrument's positive BBP pi enclosure, initial sine
and cosine enclosures, interval squares/products, angle doubling, and outward
rounding were checked at the level of their formulas. The interval comparison
test uses the **upper** possible difference `max(actual_hi-reduced_lo,
reduced_hi-actual_lo)`, not merely the separation of the two intervals.
Independent interval overlap is finite implementation evidence; the proofs
of the analytic error bounds remain paper mathematics.

The boundary two-scale inequality follows from Jensen on full zero-extended
windows, including the nondivisible remainder. The necessity proof fixes the
small window before taking the horizon limit, so no uniform convergence at
growing frequencies is assumed. The conductor spectrum retains the complex
root in each surviving 3/5 lag class; support counts alone would erase the
signs. The general actual-versus-reduced error symbol in that necessity proof
must not be reused as a coherent-versus-one error without its source-tail
bound; the explicit inherited and clipped budgets both supply that bound.

The coherent-seed clock barrier in `SHARPNESS.md` was also independently checked:
the positive original tail integral gives derivative coefficients 15 and 16,
integration by parts gives the stated endpoint bound, and comparison of each
unit cell with the integral costs the total phase variation. On the high lag
band, the normalized errors are `O(A/N³+N²/A)`, uniformly vanishing for the
explicit `2<c<3` regime. The triangular weights retain the limiting signed
profile `4/c-4/c²`. This is a theorem about the authentic forcing at the
explicitly altered coherent seed, not about the selected zero boundary.

**Verdict:** source identities, finite instruments, and the stated paper
reductions survive this audit. The authentic all-horizon signed upper bound,
pi normality, independent kernel formalization, and external peer review
remain separate open obligations. No audit count is a proof-authority upgrade.
