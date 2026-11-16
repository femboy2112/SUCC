# Carrier probe code audit

**Verdict: PASS; no blocking defect found.** This is a same-model review with
targeted independent calculation paths, not external refereeing or formal
kernel verification. No implementation file was changed by the reviewer.

Inspected `carrier_probe.py` with SHA256
`1722d79b75eb4d4ae8db891ebf2686a50bdc1704c8a279a3a98340912e99833d`
and `receipts/CARRIER_REPORT.json`. All three source hashes in that receipt
matched the files inspected. The recorded check groups sum to 691. The
reviewer did not rerun the full 691-check probe or the native repository suite.

## Targeted replays actually performed

- Independently enumerated both transported endpoints over `2..98`, testing
  the explicit coherent addition equation `f(f(a)+f(b))=100`. Exactly 12
  ordered prime-like pairs survived:
  `(3,49), (9,47), (11,45), (15,41), (17,39), (27,29)` and their reversals.
- Confirmed rejection of distributions containing probabilities `3/4` and
  `3/8`. The entropy routine supports probabilities that are powers of two,
  not all dyadic probabilities; its module documentation states this scope.
- Replayed a weighted Cauchy-product control: squaring `3*z^2*w+2*z^3*w`
  gives coefficients 9, 12, and 4 at positions/degrees `(4,2)`, `(5,2)`,
  and `(6,2)`.
- Checked receipt/source hashes and the arithmetic sum of the check ledger.

## Mathematical and implementation review

`omega` uses trial-factor division, while the reference `sieve_mask` marks
multiples. These are different arithmetic paths. The reported comparison
covers every integer target from 4 through 512, including odd targets.
The finite horizon `X>=N-2`, premature-prefix example, unit contamination,
and square-versus-absolute-square controls have the stated meanings.

The nested transport expression is correct. The supplied `f` is an
involution and fixes 100. The coherently transported partner of `n` is
`m=f(100-f(n))`, and its transported primality predicate is
`Omega(f(m))=Omega(f(f(100-f(n))))==1`. The independent pair enumeration
above checks the unsolved addition relation directly instead.

The entropy implementation correctly records
`H(C)+sum H(X_i|C)-H(X) = H(C|X)+sum H(X_i|C)-H(X|C)`.
The shared, opposite, independent, unexplained, bloated-carrier, and parity
controls distinguish redundancy, orientation, unnecessary carrier state,
and residual or higher-order dependence. Carrier entropy counts the random
carrier state within a declared known probability model; describing the
model/codebooks/decoder remains a separate description-length cost.

The approximate-braid group is a quarter-turn scalar phase calibration of
the bound. Its 16 recorded checks are not a general numerical campaign over
arbitrary perturbed operators. The histogram assignment count and 198-bit
fixed-width bound belong to the stated uniform-assignment experiment, not
to a lower bound on the actual arithmetic source's shortest description.

The receipt explicitly declines claims of universal compression superiority,
exclusion of all object-based proofs, or a Goldbach proof. Finite prefix
and permutation controls are not presented as completed infinite runs.

`CARRIER_COUPLING.md` was absent at the initial inventory and was not part
of this audit. The report covers the executable, its dependencies as needed,
and the recorded receipt.
