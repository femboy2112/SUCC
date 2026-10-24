# Twisted-pair BBP observer claims — research only (2026-10-24)

**Branch:** research/bbp-twisted-pair-dual-observers-2026-10-24.
**Parent:** main@e648df3e4fca73ab6b942232b5ca4b310e9cac08.
**Sibling:** PR #266 lag/carry, not imported into this research tree.
**Status:** paper-proved elementary/source-theoretic mathematics, exact rational
finite checks, BGK as an external theorem. No new Lean declarations.
No π-normality or RH proof; academic novelty not established.

| Local claim | Correctly typed outcome | Status and falsifier |
|---|---|---|
| TPD-01 | Two affine SUCC trajectories under the same drive have autonomous difference; orientation swaps require Z₂ transport | CLASSICAL/PAPER; fake wire sign cancellation |
| TPD-02 | Full-source Galois pair ratio cancels all shared p-free phase exactly | PROVED PAPER/EXACT TESTED; not selected-source cancellation |
| TPD-03 | Contragredient p-label \(a_t=16^{-t}a_0\) preserves pairing and recovers p-free temporal differences | PROVED PAPER/EXACT TESTED; time-varying label not a fixed Galois embedding |
| TPD-04 | Opposite Galois pairs reveal doubled common phase; ±a, ±2a yield gain at least 1/2 | PROVED PAPER/EXACT TESTED; no unauthenticated physical channel |
| TPD-05 | Uniform distinct-pair chord moments equal p/(p−1) times binomial Haar for k<p; first alias at k=p | CLASSICAL FOURIER/PAPER/EXACT TESTED, p∤h |
| TPD-06 | BGK gives signed DIFFERENTIAL power saving on good growing p-clock windows | EXTERNAL THEOREM + PROVED TRANSPORT, not absolute π sum |
| TPD-07 | Complete time-averaged Galois channel Gram has exact rank L and spectrum independent of w | PROVED PAPER/EXACT TESTED; cross-time raw data still may retain w |
| TPD-08 | p-free complement can fake any finite selected phase transcript at accuracy O_h(1/q) with a changed forcing | PROVED FINITE/EXACT TESTED; h>1 and negative h checked |
| TPD-09 | π-selected signed high-mode correlation, selected collision bound, or full normality | OPEN / UNVERIFIED |
| TPD-10 | One authenticated absolute BBP forcing/curvature comparison fixes initially unknown p-primary wire | PROVED PAPER/EXACT TESTED; assumes absolute source readout |
| TPD-11 | One ZERO-forcing p-free complement with exponentially fine initial source phase can fake near-perfect cancellation failure on a declared finite window | PROVED FINITE/EXACT TESTED; NOT BBP initial or source |

The full paper source is research/2026-10-24/BBP_TWISTED_PAIR_GALOIS.md;
the exact oracles are observational_succ/bbp_twisted_pair.py and
tests/test_bbp_twisted_pair.py. Work must not be promoted to main without
its actual final-head focused/full validation and source review.

**Core no-go:** pair differences and even the complete Galois
channel Gram cancel w by construction, so alone they cannot
distinguish an authentically π-selected complement from
an adversarial p-free complement that locks the absolute phase.
One must preserve (and use) a source anchor, not invent independence.
