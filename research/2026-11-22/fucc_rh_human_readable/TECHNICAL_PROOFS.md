# Technical proofs for the SUCC–RH human-readable reconstruction

**All claims in this file are paper derivations with explicitly stated domains.** They are elementary/classical results placed in FUCC-compatible coordinates. External use of the zeta continuation, Landau criterion, theta-lift integrality and lattice slopes is separately labelled in `HUMAN_READABLE_PROOF_SPINE.md`.

## T1. FUCC logarithmic derivative and exact prime-power current

Let `H=ell^2(N_{>0})` with orthonormal basis `e_n`. Define `V_m e_n=e_{mn}`, initially for every natural m>=1. Each V_m is an isometry on the full H. Let the (unbounded) self-adjoint multiplication operator `D e_n=(log n)e_n`, with the finite-support core `c_00`.

For each n,m the commutator on that core is

```
(D V_m-V_m D)e_n=(log(mn)-log n)e_{mn}=(log m)e_{mn}.
```

It agrees there with the bounded operator `(log m)V_m`, so has this unique bounded extension. For X>=1, the finite Euler-logarithm operator is

```
L_X=sum_{p prime, k>=1, p^k<=X} V_{p^k}/k.
```

Linearity gives `[D,L_X]=sum_{p^k<=X}log(p)V_{p^k}` on `c_00`, with a bounded extension because the sum is finite. A composite m with two distinct prime factors appears in no term; in particular the fake prime 6 must have coefficient zero. No time-order or phase has been silently discarded.

## T2. Exact Riesz prime sum as a vacuum-to-observer amplitude

For X>=1 define `r_X=sum_{n<=X}(X/n-1)e_n`. It is finite and real. Then

```
<r_X,[D,L_X]e_1>
 = sum_{p^k<=X}(X/p^k-1)log(p)
 = sum_{n<=X} Lambda(n)(X/n-1).
```

The first equality uses the inner product in the canonical basis. The second is the definition of Λ. There is no infinite Hilbert-norm limiting assertion or expectation over random primes here.

## T3. Riesz Mellin transform and cancellation of the pole at 1

Let `S(x)=sum_{n<=x}Lambda(n)(x/n-1)`. For Re(s)>1, the prime Dirichlet series converges absolutely, permitting Tonelli/termwise integration after a standard absolute-majorant argument:

```
int_n^infty ((x/n)-1)x^(-s-1)dx
 = (1/n)*n^(1-s)/(s-1)-n^(-s)/s
 = n^(-s)/(s(s-1)).
```

Therefore `M[S](s)=[-ζ'(s)/ζ(s)]/[s(s-1)]`. Put `G(x)=S(x)-xlog x+(1+γ)x`. Integration of the two elementary terms yields

```
M[G](s) = [-ζ'(s)/ζ(s)]/[s(s-1)]
            - 1/(s-1)^2 + (1+γ)/(s-1), Re s>1.
```

The classical Laurent series `ζ(1+u)=1/u+γ+O(u)` gives `-ζ'(1+u)/ζ(1+u)=1/u-γ+O(u)`. Also `1/[s(s-1)]=1/u-1+O(u)`, so the first term's Laurent principal part is `1/u²-(1+γ)/u`. It is exactly cancelled by the two elementary terms. Hence M[G] has a removable singularity at s=1 after meromorphic continuation. Poles at nontrivial zeros must be ruled out by an independently proved one-sided estimate; the identity alone does not do it.

## T4. Local arithmetic multiplicity through a height-two formal inverse

Fix a prime p. In Q_p[[T]], set

```
l(T)=T+sum_{j>=1}p^(-j)T^(p^(2j)).
```

The formal inverse U(z) exists uniquely because l(0)=0 and l'(0)=1. Write `U(z)=sum_{a>=1}u_a z^a`, with u_1=1. Define `L=p²-1`. Claim `v_p(u_a)>=-(a-1)/L` for every a.

**Induction.** From the defining inverse equation,

```
U(z) = z-sum_{j>=1} p^(-j)U(z)^(p^(2j)).
```

For a>1, coefficient u_a is a finite sum over indices j with `r=p^(2j)<=a` and compositions `a=i_1+...+i_r`, `i_h>=1`, of terms `-p^(-j)u_{i_1}...u_{i_r}`. Since r>=p²>=4, every `i_h<a`. By induction, the valuation of each product is at least

```
- sum_h (i_h-1)/L = -(a-r)/L.
```

Dividing by p^j costs j. Since `j <= (p^(2j)-1)/(p²-1)=(r-1)/L` (a geometric-series inequality), this is at least `-(a-1)/L`. Nonarchimedean valuation of a sum is bounded below by the minimum term valuation. Hence the inductive bound holds.

For `f(T)=sum_{r>=0} f_r T^r ∈ Z_p[[T]]`, the coefficient `[z^a]f(U(z))` is a sum of terms `f_r u_{i_1}...u_{i_r}` with `i_1+...+i_r=a`. Every term has valuation at least `-(a-r)/L>=-(a-1)/L`, so the same bound holds for the coefficient. The a-th derivative at zero is `a![z^a]f(U(z))`. Thus

```
v_p((f∘U)^(a)(0)) >= v_p(a!)-(a-1)/(p²-1).
```

Now Legendre's formula `v_p(a!)=sum_{h>=1}floor(a/p^h)` yields

```
v_p((f∘U)^(a)(0)) >= a*(1/(p-1)-1/(p²-1)) - O(1+log_p a)
                        = a*(1/p+1/p³+1/p⁵+...) - O(1+log_p a).
```

**Precision and provenance:** This is an elementary local formal-group-model lemma, based on the calculation in Michael Rubinstein's 21 November 2026 guide Part II §2. It does not assert that an actual theta kernel has integral coefficients in these coordinates. That source-specific integrality is a **separate imported theorem** of the released Lean construction and the first major missing human-readable bridge.

## T5. A nonzero determinant's divisibility cannot exceed its size

Fix `A∈M_r(Z)` with `det A≠0`; suppose `p^{e_p}` divides det A for a finite set of primes. Then `prod_p p^{e_p}≤|det A|` by unique factorization. Taking logarithms gives the first inequality. Hadamard gives `|det A|≤prod_i||row_i(A)||_2`, proving

```
sum_p e_p log p ≤ log|det A| ≤ sum_i log ||row_i(A)||_2.
```

This is the finite-dimensional version of a **global capacity constraint**. The arithmetic RH proof uses lattices over number fields, Hermitian slope filtrations, trace formulas, and normalizations that are not contained in this elementary result. They cannot be inferred merely from the determinant inequality.

## T6. An explicit source-map no-go for unmodified FUCC

For a prime p and a>=1, `(V_p)^a e_1=e_(p^a)`. In the standard integer lattice freely generated by the basis vectors, all coordinates of that vector except one vanish and the remaining coordinate is 1. The gcd of its coordinates is 1. Therefore no positive power of p divides the **full vector** (i.e. it is not in `p Z^(N)` in any finite truncation containing its support). Every nonzero unit minor of the matrix of V_p similarly has p-adic valuation 0.

The functional `ell(e_n)=n` produces `p^a` on this vector, but it is not bounded on H because its values on unit-norm basis vectors are unbounded. The multiplicative *index* is not an automatically bounded integral *matrix coefficient*. An operator supplying a useful RH multiplicity proof needs an additional integral representation and independently bounded Archimedean pairing.

A higher derivative `ad_D^a(V_p)=(log p)^a V_p` has no ordinary p-adic valuation over Q, since real log p is not a specified algebraic integer. This is a **typed obstruction** to treating logarithmic weights as arithmetic divisibility. It does not forbid constructing a new integral model.

## T7. Root witness and hostile controls

- **Fake-six:** `V_6` does not appear in `L_X`, because 6 is not a prime power. Adding it as a new primitive destroys the authentic von Mangoldt support.
- **Changing the source:** substituting Beurling primitive generators with noninteger labels can reproduce a formal Euler product and commutator, but does not authenticate the standard primes; the source map matters.
- **Removing a denominator:** defining the Euler logarithm with coefficients 1 instead of 1/k would give `k log p` for `p^k`, not Λ. The exact normalization is load-bearing.
- **Infinite versus finite:** the finite identity is exact for all X; the formal infinite Dirichlet identity requires Re(s)>1 for absolute convergence. Extending it to zeros without analytic continuation is invalid.
- **Wrong positivity:** positivity of `||[D,L_X]e_1||²` is true for any source but yields no one-sided estimate on the signed, subtracted G(X).
- **Local versus global:** T4 holds for the declared height-two power series, not for an arbitrary FUCC matrix or theta kernel.

Every result above has an exact mathematical boundary and no RH conclusion by itself.
