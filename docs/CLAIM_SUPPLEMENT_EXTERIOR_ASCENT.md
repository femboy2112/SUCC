# Cofactor, exterior and simplex ascent

These identifiers preserve the names in PR #214 at
`9372c669892a2a29fb8c16f0fa20c11815f650df`. Full hypotheses and paper proofs:
[original dossier](../research/2026-10-20/DUAL_SLOPE_EXTERIOR_ASCENT.md).
The independent [geometry review](../research/2026-10-21/MAIN_VIII_GEOMETRY_AUDIT.md)
and [hostile review](../research/2026-10-21/MAIN_VIII_HOSTILE_AUDIT.md) use a
lattice-index derivation and separate exact counting oracles. They are
same-model reviews, not external refereeing or formal kernel verification.

| ID | Precisely scoped claim | Status | Boundary |
| --- | --- | --- | --- |
| COF-01 | For positive integer summands x_i=d_i u_i, c=q w=sum x_i<=X, D=q product d_i and U=w product u_i satisfy DU=c product x_i<=X^(m+1)/m^m | PROVED PAPER / CLASSICAL | Small cofactor product does not bound aggregate incidence multiplicity |
| EXT-01 | Pairwise-coprime positive moduli d_1,...,d_m,q force D=q product d_i to divide determinants of m source vectors satisfying the coordinate and sum congruences | PROVED PAPER / CLASSICAL | Vectors must obey the same moduli |
| EXT-02 | Under EXT-01, D>X^m and positive sum cutoff X force the rational span of all source vectors to have dimension at most m-1 | PROVED PAPER / CLASSICAL | Rank drop does not imply bounded cardinality |
| EXT-03 | The proposed implication D>X^m implies at most one primitive source point is false for m>=3 | REFUTED AS INFERENCE | Explicit rank-two, three-summand family with arbitrarily many points |
| EXT-04 | Without coprime moduli, E=(product d_i)q/gcd(q,gcd_i d_i) divides every full determinant; one globally primitive point forces gcd_i d_i=1 | PROVED PAPER / CLASSICAL | E is the actual full lattice index, not necessarily its index on a rational section |
| SMP-01 | Positive m-simplex counts for residues R modulo W have error at most |R| m^2 (X/W+m)^(m-1)/m! from |R|(X/W)^m/m!, for integer m,W>=1 and real X>=0 | PROVED PAPER / CLASSICAL | Preserve the sharper two-dimensional Main VII constant |
| SMP-02 | For nonempty residue sets and X>0, m^2 W/X -> 0 is sufficient for a uniform relative simplex asymptotic; at W=1 and m~c sqrt(X), the uncorrected volume ratio tends to exp(-c^2/2) | PROVED PAPER | Not arbitrary growing dimension or moving modulus uniformity |

Executable finite controls: `observational_succ/exterior_cofactor_ascent.py`,
`tests/test_exterior_cofactor_ascent.py`, and
`tests/test_viii_hostile_exterior.py`. Academic novelty is unverified; these
are classical constructions and new-to-project applications. No claim here
extends the complete abc weighted moment beyond `t<2/3`.
