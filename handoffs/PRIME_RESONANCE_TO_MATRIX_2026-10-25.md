# Arithmetic resonance handoff to the matrix walk

Independent branch: `research/pi-prime-clock-resonance-killer-2026-10-25`.
Pinned parent: PR #296, `461942c0bf616518e668d236d1c6b1596665a7dd`.
Read [full report](../research/2026-10-25/PRIME_CLOCK_RESONANCE_REPORT.md),
[claim supplement](../docs/CLAIM_SUPPLEMENT_PRIME_CLOCK_RESONANCE.md) and
[validation](../research/2026-10-25/PRIME_RESONANCE_VALIDATION.md).

**No authentic W=o(D), J=o(1), collision saving, or Fejer-purity estimate was
obtained. Do not combine two conditional criteria and call their premises proved.**

## Exact interface

Same original four poles, same U0=0, no pi digits as construction inputs.
For p=8m+1 prime: n0=m+1, D=3m, L=ord_p16|m,
W=sum_(t<D)e(hU_(n0+t)); canonical primary is4*16^t/p and complement p-free.
Every h is a fixed nonzero integer in asymptotic statements. Primes dividing
h are excluded only from nontrivial local BGK estimates, and are finitely many.

For synchronized d|D, set g=gcd(d,L). The new identity is J_d=J_g, with
retained sector (Q_L-Q_g)v. Exact data within fibers of Q_L that sum to zero
cannot couple to any L-periodic clock. Enlarging d without changing g is
provably redundant. The Python certificate checks three orthogonal sectors
in formal Q[Q/Z], with the actual source prefix and integer lift retained.

The inherited BGK estimate controls the low sector if L/g>=p^gamma for a
fixed positive gamma. No effective exponent is invented. The retained signed
interaction remains the unknown. This interface can be evaluated against
matrix Fourier entries, but has no decay to insert into their purity bound.

The inherited normalized true-circle transport costs less than
11|h|/(336m²) on each full prime window. Fixed-d prime progression and
good-order coverage plus scale-four descent are audited in the coverage note.
A sparse good-prime subsequence is not enough. An averaged squared-window
criterion is also sufficient, but is another unproved reformulation.

## New barriers that a proposed proof must pass

1. **Source-forced gap with sharp exponent:** every initial state following
   exact forcing has 1-|W/D|>=h²/(1331712m⁴) for m>=11,m²>=|h|. There are
   explicit rational odd p-free altered initial states, preserving the exact
   forcing and selected prime clock, whose deficit is O_h(m^-4). Thus forcing
   nonconstancy cannot deliver cancellation uniformly over initial states.
   The source-specific zero initialization must do real work.
2. **Near-perfect inverse theorem:** at deficit O(1/D), high coherence
   localizes the start to exponentially narrow finite source-defined arcs.
   There are fifteen seeds for the harmonic phase, or 15|h| for the source
   circle phase. Avoidance by the true selected start is not proved. Use
   exact centers and intervals; do not treat tiny Lebesgue measure as a
   guarantee about this deterministic point.
3. **Lag conductor obstruction:** ordinary P(E)=product(E^k-1) retains
   P(16) times the initial state. At fresh prime birth at its final endpoint,
   residue4 survives. U6-U4 kills17 and retains41. The mixed-tail bound has
   only polynomial lag cost, but its completed target frequency is hP(16).
4. **Conductor-only anti-concentration fails:** counterfeit complement
   phases can be rounded on their authentic allowed denominator grids,
   without any new prime or larger conductor, to make every phase collide.
   This control fails the recurrence; prove a temporal numerator statement.

## Next execution target

Attack a property of the true zero-selected arithmetic prefix that fails for
both the exact-forcing altered-initial family and the allowed-conductor
altered-recurrence family. Candidate: a signed estimate on the gcd-reduced
sector, or the **weaker inherited** trimmed collision target at prescribed
logarithmic depth. The attachment's E=o(log N) suffices; entropy already
permits E=N^o(1). Carry all interactions, exceptional times, prime coverage,
and real-circle tail costs. The exact-source selection must enter the proof,
not merely the name of the measured sequence.

Reuse the new formal finite reindexing kernel as such. It proves no analytic
bound. Keep this branch and the concurrent Gram branch separate until a
reviewed integration is authorized; do not merge main in this round.
