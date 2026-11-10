# Intrinsic arithmetic Hamiltonian and its operator domain

The carrier is `ℓ²(N_{≥1})` with unit basis `e_n`. The result below
extends the intrinsic-carrier import's norm convergence for
`Re s > 1/2` to a densely defined operator at the endpoint. The real
endpoint is essentially self-adjoint and unbounded.

## Single radix and the marked boundary

For each integer `p ≥ 2`, define `Se_n=e_{n+1}`,
`V_pe_n=e_{pn}`, `T_{p,a}=S^a V_p` for `0 ≤ a < p`, and
`W_p=p^{-1/2} Σ_a T_{p,a}`. The child isometries have orthogonal ranges
with sum the span of `e_n` for `n ≥ p`. The omitted positive-integer
boundary has rank `p−1`. The isometries obey `V_p S = S^p V_p`.

On each block `pm,…,pm+p−1` with `m ≥ 1`, the orthogonal
projections `B_p=W_pW_p*` and `Q_p=V_pV_p*` have matrices
`J_p/p` and `E_{00}`. The operator `H_p=i[B_p,Q_p]` acts by
`e_{pm} ↦ (i/p)Σ_{a=1}^{p−1} e_{pm+a}` and
`e_{pm+a} ↦ −(i/p)e_{pm}` for `a>0`. It vanishes on the
boundary. On the orthonormal pair formed by the hub and the normalized
sum of its leaves it has matrix

```text
sqrt(p−1)/p · [ 0  −i ]
              [ i   0 ]
```

The remaining `p−2` block coordinates are null. The bounded
self-adjoint operator has domain all of `ℓ²` and pure point spectrum
`{−sqrt(p−1)/p, 0, sqrt(p−1)/p}`. Each nonzero eigenvalue has infinite
multiplicity. The zero eigenspace has dimension one for `p=2` and is
infinite dimensional for `p>2`. Complex conjugation sends `H_p` to
`−H_p`. The same calculation holds at composite radices, and every
pair of divisibility projections `Q_p,Q_q` commutes.

For `[B_2,B_3]`, the invariant decomposition is the boundary
`1,…,5` and the bulk blocks `6m,…,6m+5` for `m≥1`. The boundary
`B_3` has rank one with normalized range vector
`(e_3+e_4+e_5)/sqrt(3)`, whose `B_2` projection has squared norm
`5/6`. In a bulk block, use the two normalized triple averages as
the basis of the range of `B_3`. The compression of `B_2` to that
range has matrix with diagonal `5/6` and off-diagonal `1/6`, hence
eigenvalues `1,2/3`. For an eigenvalue `λ∈(0,1)` of this
compression, the two projections give a skew commutator with eigenvalues
`±i sqrt(λ(1−λ))` on its principal two-plane. This follows by
taking the normalized residual of the first projection of a unit
compression eigenvector after removing its component in the second
range. Thus the Hermitian `i[B_2,B_3]` has nonzero eigenvalues
`±sqrt(5)/6` on the boundary and `±sqrt(2)/3` in each bulk block,
with three and four null coordinates, respectively. The bulk oscillator
is available before choosing a BBP source or seed.

## Weighted field and maximal domain

Set `D=c₀₀(N_{≥1})` and
`K_s=Σ_{p prime} (log p)p^{-s}H_p` on `D`. A basis vector
`e_n` only meets `p≤n`, and its image is supported at indices below
`2n`. Every row and column of the formal matrix is finite, since each
`H_p` is Hermitian. For every complex `s`, the adjoint of this
initial-domain operator is the maximal matrix realization of
`K_{conj(s)}`, with domain the vectors for which the coordinatewise
matrix product belongs to `ℓ²`. Testing on each basis vector proves
necessity, and taking finite linear combinations gives sufficiency.
In particular, the adjoint contains `D`, so the initial operator is
closable for every complex `s`. For real `s` it is symmetric.

If `Re s > 1/2`, the estimate
`Σ_p (log p)p^{-Re s} ||H_p|| ≤ Σ_{n≥2} (log n)n^{-Re s−1/2}`
gives norm convergence, locally uniform in `s`. For real `s≥0` a
different bound proves essential self-adjointness. Write
`K_s=i(A_s−A_s*)` on `D`, with `A_s` the hub-to-leaf operator
of coefficient `(log p)p^{-s-1}` on each oriented edge. For input
supported in `[1,N]` we may retain only `p≤N` and compress all
matrices to `[1,2N]`. In the resulting nonnegative oriented matrix,
each row has at most one parent per prime, giving row sum at most
`Σ_{p≤N} (log p)/p ≤ 2 log N` for `N≥2`. The last bound follows
from `log(N!) ≥ Σ_{p≤N} floor(N/p) log p` and
`floor(N/p) ≥ N/(2p)`. A column at index `m≤2N` has at most
`p−1` leaves for each `p|m`, giving sum at most
`Σ_{p|m} log p ≤ log m`. The Schur bound on the matrix and its
transpose implies

```text
||K_s f|| ≤ 2 sqrt(2) log(2N) ||f||,     supp(f) ⊂ [1,N].
```

At each iteration the support bound at most doubles. Taking
`N≥2`, we get `||K_s^j f|| ≤ (2 sqrt(2) log(2N))^j j! ||f||`
because `log(2^{k+1}N) ≤ (k+1)log(2N)`. Hence all vectors of
`D` are analytic vectors for the symmetric operator. Nelson's
analytic-vector theorem gives essential self-adjointness. For real
`s≥0` the self-adjoint closure therefore has exactly the maximal
domain described above. The analytic-vector theorem applies to the
operator argument, while holomorphy refers separately to the
norm-convergent family in `Re s > 1/2`.
[Edward Nelson, *Analytic Vectors*, Ann. Math. 70 (1959), 572–615](https://doi.org/10.2307/1970331).

### Unboundedness at the endpoint

Let `n_Y=∏_{p≤Y}p`. For positive integers `a` the upward
coordinates of `K_s e_{n_Y}` are exactly

```text
(K_s e_{n_Y})_(n_Y+a) = i Σ_{a<p≤Y} (log p) p^{-1-s}.
```

Downward leaf-to-hub edges cannot enter these coordinates. At real
`s=1/2`, the prime number theorem in the form
`θ(x)=Σ_{p≤x}log p ~ x` gives `θ(2a)−θ(a) ≫ a` for
sufficiently large `a`. For `a≤Y/2` this makes the absolute
value of the coordinate at least a constant times `a^{-1/2}`.
Thus `||K_{1/2}e_{n_Y}||² ≫ log Y`. The same lower bound holds
for every real `s≤1/2` by positivity of the terms. This witnesses
unboundedness on the actual unit vectors of the integer carrier,
including at the self-adjoint endpoint.

In fact the whole complex line `Re s=1/2` is unbounded on `D`.
For fixed `s` with `σ=Re s>0`, partial summation of
`θ(x)=x+o(x)` gives
`Σ_{p>a}(log p)p^{-1-s} = a^{-s}/s+o_s(a^{-σ})`.
The remainder bound follows by integrating the error in `θ(x)`
against the derivative of `x^{-1-s}` and bounding its endpoint term.
Removing `p>Y` costs `O_s(Y^{-σ})`. For sufficiently large
`a≤sqrt(Y)` the coordinate is therefore bounded below in modulus by
a constant times `a^{-σ}`. Its squared sum diverges as `Y→∞`
whenever `0<σ≤1/2`.
[Forster, *The Chebyshev Functions Theta and Psi*, Corollary 11.6](https://www.math.lmu.de/~forster/v/ann/annth_11.pdf).

## Logarithmic covariance and RH boundary

The log-energy operator `H_0 e_n=(log n)e_n` is self-adjoint on
the vectors `f` with `Σ_n (log n)² |f_n|²<∞`. Its unitary flow
`U_t=e^{itH_0}` preserves this domain. The dilation `V_p` also
preserves it and satisfies `U_t V_p U_t*=p^{it}V_p`.
The hop `pm→pm+a` in `H_p` has Bohr phase
`((pm+a)/(pm))^{it}`, with the reciprocal phase on the reverse hop.
This ratio follows from conjugating the matrix unit by `U_t`.

For real `s>0`, the field closure is also covariant in the
following domain sense. The upward matrix of `[H_0,A_s]` has
entry `(log p)p^{-s-1} log((m+a)/m)` at an edge from hub `m`
to leaf `m+a`. Its row sums are bounded by
`(log 2)Σ_p (log p)p^{-s-1}`. Its column sum at hub `m` is
bounded by `m^{-1}Σ_{p|m} (log p)p^{1-s}`, at most
`m^{-min(s,1)} log m` by prime factorization. These two bounds
give a bounded commutator on `D` by Schur, for both orientations.
Integrating the conjugated commutator on `D` gives a bounded
difference `U_t K_s U_t*−K_s` of norm at most
`|t| ||[H_0,K_s]||`. Closure on the common core `D` shows
`U_t Dom(cl K_s)=Dom(cl K_s)`, since a bounded perturbation has
the same closure domain.

The known Bost–Connes energy representation is
`Tr(e^{-sH_0})=ζ(s)` in `Re s>1`, exactly the trace-class
region of this diagonal operator. A positive Gibbs density comes
from real `s=β>1`. The full Bost–Connes observable algebra
requires its additional rational phase operators. The logarithmic
energy has the prime occupation decomposition
`log n=Σ_p v_p(n)log p`, and the prime-power diagonal observable
`Λ` gives `Tr(Λ e^{-sH_0})=−ζ'(s)/ζ(s)` in `Re s>1` by
the absolutely convergent Euler expansion. The normalized thermal
mean `Tr(e^{-βH_0}H_p)/ζ(β)` vanishes, and the variance is

```text
Tr(e^{-βH_0} H_p²)/ζ(β)
 = (1 + (p−2)p^{-β} − Σ_{a=1}^{p−1} a^{-β}/ζ(β)) / p².
```

This follows by summing the diagonal weights `(p−1)/p²` on the
hubs and `1/p²` on their leaves. At `p=2` it reduces to
one quarter of the Gibbs mass outside `e_1`. Inserting an independent
composite mode with weight `log q` into the Euler product preserves
all Dirichlet coefficients below `q` and doubles the coefficient at
`q`. It counts both the original prime factorization and one
occupation of the new mode. Conversely, exchanging the energies of
`e_2,e_4` by a unitary permutation keeps the trace exactly but
violates the actual covariance on `V_2e_1=e_2`. An
energy diagonal in the actual integer basis is fixed by requiring
energy zero at `e_1` and the covariance on each actual prime dilation.
Evaluating on basis vectors gives `E(pn)=E(n)+log p`, and
factorization gives `E(n)=log n`. Trace agreement
alone does not authenticate the carrier. The local graph formulas
accept composite radices and therefore cannot justify the choice of
prime indices independently.
[Bost and Connes, original paper, §2 and Proposition 7](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf).

**Status.** The endpoint and covariance statements above are operator
theorems. The signed completed explicit-formula identification remains
open. An identification would need the Archimedean Gamma term, pole
terms and the exact signed pairing on a specified admissible test
space, in addition to the prime-power trace. The spin spectrum, the
Gibbs normalizer and the positive thermal variance yield no such
pairing. The separate adelic trace-formula program explains the
distinction between the absorption/explicit-formula problem and this
energy representation.
[Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068).

## Which logarithmic frequencies the hops can see

Each `H_p` hop changes log-energy by less than `log 2`. By
telescoping along a path, any fixed `r`-fold product of these hops
has zero matrix entries when `|log(m/n)| ≥ r log 2`, including with
diagonal insertions or the locally finite sums on `D`. Conjugation by
`U_t` therefore gives each matrix coefficient only frequencies in
`[−r log 2,r log 2]`. A fixed-degree construction from these hops
alone cannot reproduce the prime-power term with frequencies
`k log p` of unbounded size.

The actual dilation supplies that missing frequency. Write
`φ_β(X)=Tr(e^{-βH_0}X)/ζ(β)` for real `β>1`. The range projection
`V_p^k(V_p^k)*=Q_{p^k}` has Gibbs mass `p^{-kβ}). Hence
`φ_β(U_t V_p^k U_t* (V_p^k)*)=p^{-kβ} exp(it k log p)`. Summing
with weight `log p` over primes and `k≥1` is absolutely convergent
and yields `−ζ'(β−it)/ζ(β−it)`. The order matters because the reverse
multiplication of the isometry and its adjoint gives the identity
instead of the range projection. This exact factor-jet coupling supplies
the prime-power side in its original half-plane. The signed completed
pairing remains open.

## Reproduction

From the repository root, run

```bash
python research/2026-11-10/main_xxiii/hamiltonian_endpoint_probe.py
```

The probe compares exact rational upward-edge enumeration with an
independent quotient-row calculation, including at a primorial.
Four inserted composite modes fail the exact Euler coefficient control.
For the actual real endpoint weights the squared upward norms are
approximately `2.782, 5.877, 10.078, 14.798, 19.911` at cutoffs
`32, 128, 512, 2048, 8192`. These are finite diagnostics. The
unboundedness claim rests on the primorial estimate above.
