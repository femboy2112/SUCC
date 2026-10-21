# Academic Main VIII: independent exterior and simplex audit

Audit date: 2026-10-21. Incoming PR #214 head:
`9372c669892a2a29fb8c16f0fa20c11815f650df`. Reviewed on the unreviewed
integration union `c82f5e34145661d96e87612d0a8cc633759409b7`, based on main
`b5f9591033db2022bda6a2f16a935c06466f9eff`.

Scope: `DUAL_SLOPE_EXTERIOR_ASCENT.md`, `exterior_cofactor_ascent.py`, and its
focused tests. This is a separate same-model review with a different lattice
index derivation; it is neither an external referee report nor Lean verification.

## Verdict and reconstructed proofs

**PROVED (paper proof, classical mathematics/new-to-project application):** the
cofactor budget, exterior divisibility and rank-drop implications, the explicit
unbounded three-summand multiplicity family, and the stated dimension-uniform
simplex discrepancy bound survive this audit. No new positivity, abc, or RH
conclusion is licensed. The infinite-clock claims are assigned to a separate
review; they are not promoted by this report.

For the cofactor budget, `DU = c product(x_i)` is an identity and AM–GM gives
`product(x_i) <= (c/m)^m`. Positivity and the sum relation are essential.

Here is an independent route to the stronger shared-prime exterior modulus.
Let `P=product(d_i)`, `g=gcd(d_i)`, and

```
Lambda = {x in Z^m : d_i divides x_i for every i, q divides sum(x_i)}.
```

The diagonal lattice has index `P`. Its sum map to `Z/qZ` has image generated
by the `d_i`, of order `q/gcd(q,g)`. The kernel therefore has ambient index
`E=P*q/gcd(q,g)`. Determinants of `m` lattice vectors are multiples of that
index. Thus the dossier's `E` is the actual lattice index, not merely a
divisibility lower bound. Hadamard and `||x||_2 <= ||x||_1 <= X` give
`|det| <= X^m`. If `E>X^m`, every full minor vanishes and the entire source
span has rational dimension at most `m-1`. A single globally primitive source
point forces `g=1`; pairwise coprimality of all moduli is unnecessary in this
case. None of this bounds cardinality by one in dimension at least three.

The advertised family has source vectors
`((k-1)n,(2k-1)(n+1),2n+1,k(3n+2))`, `2<=k<=K`.
The sum identity holds exactly. For odd `n` the four moduli are pairwise
coprime. Every possible prime factor of `gcd(k-1,2n+1)` is excluded by the
chosen divisibility of `n`; the prime 2 is excluded because `2n+1` is odd.
Hence each source vector is primitive. Its first three coordinates are an
affine function of `k` with independent constant and slope vectors, so rank
is exactly two. Finally `D>6n^4`, `X<=4Kn`, and `n>12K^3` imply `D>X^3`.
This independently confirms unbounded multiplicity after rank drop.

For one residue class choose positive representatives `rho_i in [1,W]` and
set `n=floor((X-sum(rho_i))/W)`. Stars and bars gives `binom(n+m,m)` for
`n>=0`, zero otherwise. Put `t=X/W`. Each of the `m` factors `n+j` differs
from `t` by at most `m` and belongs to `[0,t+m]`. Telescoping the product
therefore bounds the discrepancy by `m^2(t+m)^(m-1)/m!`. If `n<0`, then
`t<m` and the same bound dominates the missing main term. Summation over
distinct residues is legitimate; no equidistribution assumption is used.
The relative bound is at most `a exp(a)`, `a=m^2 W/X`, for a nonempty residue
set and positive cutoff. Thus `m^2 W/X -> 0` is sufficient uniformly over
residues. It is not asserted necessary for each specially chosen family.

At `W=1`, integer `N>=m`, the exact volume ratio is
`product_{j=0}^{m-1}(1-j/N)`. Expanding its logarithm with a bounded positive
remainder gives the stated limit `exp(-c^2/2)` at `m~c sqrt(N)`.

## Validation receipt and scope

Command on this union:

```
/workspace/scratch/0a4459d8f487/vii-venv/bin/python -m unittest discover -s tests -p test_exterior_cofactor_ascent.py -v
```

Result: **11 tests passed**, 0.023 seconds, exit 0. These include exhaustive
small residue counts, direct two-by-two determinants, the rank-two family,
shared-prime sharp controls, and the global-versus-pairwise primitive control.
The initial attempt to use pytest did not run tests because pytest is absent;
the repository's unittest runner was then used successfully. This is not a
full-suite or exact-final-integration-head receipt.

## Boundaries and next falsifiers

* Rank drop is linear dependence, not bounded multiplicity. The rank-two
  family is the permanent counterexample.
* An ambient lattice index need not remain the index on a rational section.
  Counts after rank drop need the saturated section lattice, its actual
  congruence index, and a boundary error. That is the next owned research task.
* The uncorrected volume term fails at the square-root dimension scale even
  for `W=1`. Any stronger asymptotic needs a dimension correction or a
  different normalization.
* Finite rational tests support the paper proofs; they do not authenticate a
  universal formal theorem. The formal lane owns kernel verification.

No imported originals, existing source modules, or central claim identifiers
were modified by this audit.
