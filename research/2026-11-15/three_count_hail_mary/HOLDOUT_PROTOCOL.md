# Frozen finite holdout protocol

Frozen before computing the extension, 2026-11-15 UTC.

- Compute the original zero-seeded BBP source through n=131072, using the
  existing outward integer BBP enclosure and certified tail-borrow algorithm.
- The earlier study ended at n=32768. Fresh observations start at n=32769.
- Evaluate every integer shell [B,2B) with 32769 <= B <= 65536. All of its
  observations are fresh. Do not select only powers of two.
- Report the minimum exact three-count budget L_B, the minimum selected-event
  density d_B, and the maximum one-sided error budget eta1+kappa+eta2 relative
  to (F1,c1,F2)=(1/16,1/4,1/4), including all extremizing B values.
- Finite pass: each such shell has one-sided error budget <=1/32, so its
  certified lower bound is at least 1/32. Finite failure: one or more shells
  exceed this predeclared budget. An uncertified carry is an ambiguous probe,
  never a silently dropped observation.
- Compare the overlap 1..32768 with the earlier receipt and report the source
  hashes. Repeat the existing exact rational recurrence cross-check through
  512. These algorithms share the same BBP source; they are not independent
  evidence for normality.
- Regardless of outcome, this tests only the stated finite interval. It does
  not establish an eventual bound, positive lower density, R0, or normality.

The fixed target and tolerance come from the parent three-mass theorem; no
threshold, shell range, or source is to be fitted to this holdout.
