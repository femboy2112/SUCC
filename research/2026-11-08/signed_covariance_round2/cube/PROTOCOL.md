# Cyclic cube protocol, fixed before numerical evaluation

Parent research head: `1990b05117d84b33094c8e0f53f7d19b60f48060`.
This front owns only `signed_covariance_round2/cube/`. The finite tests below
are algebraic falsifiers, not experiments establishing an asymptotic theorem.

Candidate CQ1: for the original clean prime clock `a(r)=e(xi*16^r/p)`,
the cyclic Gowers cube has an exact nonnegative last-shift decomposition
into squared subgroup sums, with degeneracy probability
`1-(1-1/m)^(d-1)`. The predicted bound uses the square of the BK bound,
not the BK bound itself. A formal coefficient mismatch refutes the identity.

Candidate CQ2: the resulting local cube norm tends to zero exactly below
the depth scale `2^d=o(log p)`, on the existing selected good-prime family.
This is to be proved analytically; no finite numerical trend certifies it.

Candidate CQ3: bounded multilinear cube atoms admit a certificate for the
folded original complement, charging coefficient variation and residual.
The original complement is NOT assumed to have a cheap representation.
The resonant control `B=conjugate(a)` must retain full correlation one.

Fixed exact arithmetic grid:

- Development: primes 17, 41, 73, 89, 97, 113; every cube depth 1 through 4;
  nonzero source coefficients xi=1,2. Enumerate alternating cube vertices
  directly and compare the root-of-unity coefficient histogram with a
  separate final-shift pair expansion. Work entirely in integer coefficients.
- Holdout: primes 137,193,241; depths 1 through 3; xi=3,5.
- Independently enumerate all preceding shift tuples and compare the number
  with at least one zero residue against `m^(d-1)-(m-1)^(d-1)`.
- Read literal unwrapped four-pole rational states for clean source clocks
  at primes 41,73,97,137,193,241. Compare canonical p-principal parts with
  the clock formula; zero and mutated pole/boundary controls must separate.
- Exact rational complex box-Cauchy-Schwarz and dual-atom identities on
  cyclic groups of orders 2,3,4 and depths 2,3, using fixed deterministic
  arrays declared in the implementation. Do not infer the general inequality
  from these checks.
- Negative controls: xi=0; a full-period shift; the resonant complementary
  phase; and omission of alternating cube conjugations. The latter must be
  rejected by at least one member of the fixed grid.

No empirical BK exponent will be fitted. No use of seed 1/5 as a nonnormal
control. Every test receipt records source/code hashes, counts and exact
parameters. Independent proofs and exact tests remain separate evidence.
