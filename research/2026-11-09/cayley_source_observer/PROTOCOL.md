# Frozen finite probe protocol

This file is committed before reading this runner's output. Parent research
head: `afabc458323ef2e3a20ce2bae77239c4190819c5`; main baseline:
`43886e830cee5ff6d6b37719e18d809819673bd9`.

The probe is a verification of exact finite certificates, not a fitted
normality model or an independent measurement of pi. Its original-source
epochs are **A=257 and A=509**, chosen now, with Fourier cutoff **H=1023**,
boundary width **delta=1/256**, common source horizon **L=2A**, Taylor
**terms=16**, and dyadic precision **bits=48**. No parameter will be selected
from the observed parity response. These epochs are not asserted to be
previously unseen by the entire repository; they were not inspected in this
round before freezing the protocol.

For each epoch:

1. Compute original-zero common-horizon rational phase enclosures using the
   canonical four-pole source. Compute the exact Fejer truncation, boundary,
   and clipped source payments. Enclose the finite Fourier mean with rational
   Taylor arithmetic, then check that the certified parity interval contains
   the independent local-tail exact digit mean.
2. Compute the exact three-level two-fiber recursion on the common-horizon
   lower-endpoint orbit, including its final endpoint and the fourteen
   other preimage fibers. Every recurrence residual must be zero.
3. Construct the rational same-forcing seed `s=-P_(2A+12)`. It is a control
   with all completed epoch digits certified zero, not the PPP-08 p-integral
   control; no prime-coordinate agreement is claimed. Its truncated completed
   orbit is zero and must retain maximal boundary mass and parity bias.
4. Record source/code SHA-256 hashes, rational budgets, conservative dyadic
   Fourier intervals, exact parity counts, and raw recursion rows. No pi
   decimal oracle enters the certificate.

Also record the exact n=128 quadratic-resonance certificate and the A=1024,
H=16^32 common-horizon mean budget. Those are analytic calibration controls,
not source digit holdouts.

**Pass:** every exact containment, recurrence and hostile control succeeds.
**Fail:** a violated rational enclosure/identity, or the wrong-seed control
appearing to satisfy a false vanishing certificate. **Ambiguous:** a finite
budget that contains both signs; this is an honest weak bound, not failure
of the mathematical estimate. No finite result proves any all-epoch signed
claim. Any implementation correction after first execution is disclosed in
VALIDATION.md and rerun with these same parameters.
