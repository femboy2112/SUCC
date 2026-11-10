# The folded complement is a law before it is a phase

This front proves an actual-source obstruction to a tempting model class.
A bounded positive mixture of genuinely nonlinear polynomial phase branches
cannot approximate the full folded conditional law arbitrarily well on the
strong prime clocks, when its degree/discrepancy budget is small. Fixed
branch count K, fixed degree D and weights at least w_min force asymptotic
Wasserstein error at least w_min/(17K). Arbitrary fixed unit phase anchors
are allowed. The first-moment approximation required by PR8 is a larger,
less demanding class and remains OPEN.

[Complete proofs](THEOREMS.md) retain the original four-pole source, U0=0,
replica averaging, chronology and the one cyclic boundary. The key results:

- **CBM1:** the actual folded laws obey approximate x->16x / z->z^16
  transport, with source forcing and boundary cost explicitly separated.
- **CBM2:** an exact raw-versus-folded variance decomposition, and a proved
  price for replacing a law's sixteenth moment by its mean raised to16.
- **CBM3:** exact positive K-branch polynomial law transport with KD<m
  forces homogeneous linear branches and constant weights. The native
  K<=q case lies inside this regime throughout the earlier arithmetic budget.
- **CBM4:** a precision-qualified stability bound for constant-offset and
  nonlinear branches; its shrinking scale is not mistaken for decay.
- **CBM5:** a stronger macroscopic full-law error floor for genuinely nonlinear
  branches, using polynomial character bounds, a finite arc DFT, and an
  integral of nearest-branch distance tails. A separate agent found the
  layer-cake improvement; the root supplied the arbitrary-anchor extension.

The coherent graph e(-x/p) survives exact transport and carries signed
signal1. Thus lawfulness still leaves the resonant coefficient unpaid.
Positive law models, complex signed phase expansions, and their first
moments are deliberately distinguished.

[Exact finite implementation](model.py), [tests](test_model.py),
[outward source/model oracle](oracle.py), [raw receipt](RECEIPT.json),
[validation/provenance](VALIDATION.md), [claim ledger](CLAIM_LEDGER.md).

Pi base-16 normality: **OPEN**. RH: **OPEN**.
