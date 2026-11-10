# Prospective exact controls

Written before the first local oracle run. These are proof-oracle holdouts, not a
statistical discovery protocol. Candidate theorem: finite prime principal parts,
finite 2-adic precision, exact finite carry history and arbitrarily accurate finite
real history cannot justify a uniform future Weyl-saving estimate over rational
same-forcing seeds unless literal zero is separately enforced.

Freeze rows `(J,A,L,K,eta)`:

- `(5,17,19,9,1/2^18)`
- `(11,37,41,17,1/2^22)`
- `(17,73,79,31,1/2^26)`
- `(23,137,139,47,1/2^30)`

For each row P contains ALL odd primes <= 8B, B=A+L-1, hence every prime that
can divide any original source state up to B. The seed denominator is coprime to
all of P. The initially registered primary path used literal four-fraction unwrapped
recurrence. Before final publication, root review required the production path
to reuse main's `selected_orbit.original_forcing`; the independent literal
four-fraction check is retained. This implementation change does not alter the
prospectively fixed rows or mathematical construction.
The independent path uses an integer common denominator and the combined
rational source polynomial; it must reproduce every original and mutant phase,
not import the primary recurrence implementation.

Required exact checks: source identity, 2-adic residues, every P principal part,
original zero rejection, prefix floor and carry identity, prefix error envelope,
finite backward tail identity, positive-seed construction, future phase envelope,
and rational lower bound on the real part of h=1,2,3,5 Weyl means. No complex
floating point is used as a proof certificate.

Mutants: force exact-zero acceptance; erase carry; use a bad seed denominator at
an observed prime; flip a source coefficient; claim the horizon-dependent seeds
are one fixed nonnormal seed. The last is a logical quantifier test, not a numeric
phase sample. Source mutation must be rejected by exact four-pole authentication.
