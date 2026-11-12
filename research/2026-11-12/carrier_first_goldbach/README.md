# Carrier-first arithmetic: additive–multiplicative coproduct coupling

**Date:** 2026-11-12 · **Role:** additive research extension of SUCC's prime-fixedpoint-cylinder draft PR #600 · **Status:** elementary proved identities + finite exact tests + an OPEN Goldbach coupling estimate. No merge to main authorized or attempted.

## Main statement

The `2..X` prime–prime interaction table `A[a,b]=1_prime(a)1_prime(b)` has `(X-1)^2` entries but rank at most one, being `p p^T`. The diagonal recovers the complete one-body mask. Thus the *class* of all binary-mask outer-product tables has exactly `2^(X-1)` members and admits an optimal worst-case `(X-1)`-bit fixed-length encoding, versus `(X-1)^2` entries in an uncompressed dense table. This is a rigorous compression advantage **against a particular naive encoding**, not a theorem that every object-oriented model is inefficient. For the *actual* prime mask, the table has constant conditional Kolmogorov description length given `X`, since a fixed primality program regenerates it. Time, memory, and mathematical proof complexity are separate.

The more structural construction uses **two reduced coproducts on one carrier**. Multiplicative splitting detects primes as primitive elements; additive splitting pairs the number coordinates. Projecting both additive children to the multiplicative primitive sector yields a positive diagonal operator with exactly the ordered Goldbach representation numbers as its eigenvalues. Proving this operator uniformly positive on the even subspace is *equivalent to Goldbach*, not accomplished by this construction.

## CARR-01 — The finite carrier information theorem (PROVED LOCAL)

Fix `X>=2`, put `M=X-1`, and let `v=(v_2,...,v_X)` be an arbitrary binary mask. Define the `M x M` pair table `A_v(a,b)=v_a v_b`. Then:

1. `A_v=v v^T`, hence `rank A_v <= 1` (rank zero for `v=0`).
2. `diag(A_v)=v` because binary values satisfy `v_a^2=v_a`. Therefore `v -> A_v` is injective, and there are exactly `2^M` possible tables of this form.
3. Any *fixed-length* lossless binary code for **every member of this class** requires at least `M` bits in the worst case, and storing `v` attains this bound. A raw dense table uses `M^2` bits. For the **specific actual-prime vector**, conditional plain Kolmogorov complexity `C(A_primes | X)=O(1)` because trial division is a uniform total program.
4. For arbitrary independent binary `M x M` tables, there are `2^(M^2)` possibilities; at least one needs `M^2` bits in a fixed-length representation, and all but a fraction `2^-k` have conditional plain Kolmogorov complexity at least `M^2-k` up to fixed machine constants. This comparison does **not** make prime bits random, or give a universal information lower bound for every conceivable object model.

This is a model-class statement: counting distinct admissible tables measures information after enforcing the shared-source constraint.

## CARR-02 — Two coassociative reduced coproducts (PROVED LOCAL)

Work on the algebraic finite-support core of `H=ell^2({2,3,...})`, with basis `|n>`. Define

```
Delta_times |n> = sum_{ab=n, a,b>=2} |a,b>
Delta_plus  |N> = sum_{a+b=N, a,b>=2} |a,b>.
```

Each sum is finite. Both are coassociative in the reduced sense: the two possible orders of three-way splitting yield each ordered triple `abc=n` or `a+b+c=N` (with every coordinate `>=2`) exactly once. Neither reduced coproduct is being asserted to be a counital bialgebra or to obey an undeclared compatibility law with the other. Both are generally unbounded as Hilbert-space operators; the finite-support domain and closed diagonal extensions are distinguished.

For multiplicative splitting,

```
Delta_times^* Delta_times |n> = (tau(n)-2)|n>.
```

Because `n>=2`, the zero subspace is precisely the closed span of the prime basis vectors (the unit is deliberately excluded). Write

```
P_pr = 1_{ {0} }(Delta_times^* Delta_times),
P_pr |n> = 1_prime(n)|n>.
```

This is the source-specific prime detector already present, with the unit exception removed by domain choice.

## CARR-03 — The coupling operator (PROVED LOCAL equivalence, OPEN positivity)

Compose the additive split with the two prime projectors:

```
Gamma = (P_pr tensor P_pr) Delta_plus.
G     = Gamma^* Gamma.
```

Then on every basis vector `|N>` with `N>=4`,

```
Gamma |N> = sum_{a+b=N, a,b prime} |a,b>
G |N> = R(N)|N>,  R(N)=sum_{a+b=N} 1_prime(a)1_prime(b).
```

To check the second identity, distinct sums `N` have disjoint pair-basis supports, so orthogonal images. The closure of `Gamma` is the weighted diagonal-pair operator with domain `sum_N |c_N|^2 R(N)<infty`; `G` is the positive self-adjoint diagonal operator with eigenvalues `R(N)`. On the even-number subspace:

```
Strong Goldbach  <=>  G >= I as quadratic forms
                 <=>  ker(G) intersects H_even trivially
                 <=>  Gamma|N> != 0 for each even N>=4.
```

`G>=I` is an honest *operator reformulation of the unsolved conjecture*, not something obtained merely from positivity `G>=0`.

## CARR-04 — Position versus phase: the shared carrier has a Fourier chart (CLASSICAL)

For a finite cutoff `X`, use `P_X(z)=sum_{2<=a<=X} v_a z^a`. Then

```
P_X(z)^2 = sum_N R_X(N) z^N.
R_X(N)    = integral_0^1 (sum_{a<=X}v_a exp(2pi i a theta))^2
               exp(-2pi i N theta) dtheta.
```

This gives all ordered pair counts as one convolution. Directly enumerating all ordered pairs is `Theta(X^2)` elementary iterations; exact fast polynomial multiplication/NTT computes the convolution in quasi-linear arithmetic complexity with appropriate modular coefficient reconstruction. **No implementation of a fast NTT is claimed or timed here**; the finite test uses an exact naive convolution. The Fourier representation alone cannot force `R_X(N)>0`: nonzero-frequency contributions may cancel the main term. The original primes' arithmetic structure and adequate prime-correlation estimates are the unresolved input.

## CARR-05 — Coupling changes apparent matrix rank and Schmidt rank (PROVED LOCAL)

The one-body endpoint network `A[a,b]=p(a)p(b)` has rank one. Define an observer chart on midpoint/displacement coordinates:

```
B[n,d] = p(n-d)p(n+d),   valid n-d>=2.
```

This is *not* a local row/column change of basis on `A`. The `n in {5,6}`, `d in {0,1}` restriction is exactly

```
B = [[1,0],
     [0,1]],
```

because `(5,5)` and `(5,7)` are prime pairs but `(4,6)` and `(6,6)` are not. Thus one rank-one endpoint table can become a rank-two observation table after a non-product reindexing. The distinction is a change in **observer partition**, not an increase in source information.

With the formal finite prime vector `|P_X>=sum_{p<=X}|p>`, the pair state `|P_X> tensor |P_X>` is separable. The sum-conserving projection onto `a+b=N` produces

```
|Psi_N> = sum_{a+b=N, prime a,b} |a,b>.
```

When `R_X(N)>0`, the normalized state has `R_X(N)` equal Schmidt coefficients, hence Schmidt rank `R_X(N)` and von Neumann entanglement entropy `log R_X(N)` (natural logarithm). This is a **formal Hilbert-space coupling**, not a claim that physical electrons perform arithmetic. Post-selection changes the state and must not be confused with independently existing particle correlations.

## CARR-06 — A local oracle lower bound (PROVED LOCAL, adversarial class)

For fixed midpoint `n>=2`, the `n-1` unordered candidate pairs `(n-d,n+d)`, `0<=d<=n-2`, are **disjoint in their integer endpoints**. Give an algorithm only a black-box membership oracle `v(k) in {0,1}`, without any number-theoretic constraint relating different membership bits.

On the all-zero oracle, any deterministic correct algorithm distinguishing `R_v(2n)=0` from `R_v(2n)>0` must query at least **one endpoint in each pair**, hence at least `n-1` membership bits. If it fails to query either endpoint of some pair, modify only those two unqueried bits to 1: the transcript is identical but the answer changes.

This is an exact worst-case lower bound on a *source-blind local-query model*. It is **not** a lower bound on using genuine prime arithmetic, on proof length, or on an algorithm using global structure. It shows why simply treating pair status as independent observations cannot bypass the required coupling.

## CARR-07 — Adversarial nonidentification (PROVED LOCAL negative control)

Replace the true prime source with the subsource `S={p prime: p==1 mod 4}`. It still produces a rank-one endpoint matrix, a coherent global carrier, exact Fourier convolution, and legal sum projection. But all sums `a+b` with `a,b in S` are `2 mod 4`, so every `N=0 mod 4` has zero witnesses. Low description complexity, Hilbert positivity, rank-one factorization, wavelet bases, or domain-theoretic fixed points **cannot by themselves force Goldbach**. A decisive proof needs input specific to *all actual primes*.

This follows the source-discrimination limitation also explained in Terence Tao's *Heuristic limitations of the circle method* (2012): generic Fourier estimates can remain compatible with sources intentionally missing some Goldbach sums.

## The new exact target (OPEN)

Find a genuinely arithmetic lower frame bound on the common carrier:

```
forall even N >= N0,
    ||(P_pr tensor P_pr) Delta_plus |N>||^2 >= 1.
```

To make this non-tautological, prove the bound from **independently derived prime-local source estimates**, such as a quantitative source-locked signed Fourier/CRT/Haar inequality that distinguishes the full primes from altered prime alphabets, with a justified error smaller than the positive contribution. In the Scott-language, these estimates must permit a positive certificate *without running individual endpoint primality tests for each midpoint*. All proposed phase/commutator arguments must pay that source debt; generic positivity does not.

## Tests and provenance

- `python -m unittest -v test_carrier.py`
- `python carrier_probe.py > RECEIPT.json`

Exact finite tests check two distinct prime oracles, both coproduct coherences, the multiplicative primitive kernel, independent direct versus convolution Goldbach counts, all masks at size 8, local-query adversary disjointness, changed observational rank, Schmidt-rank counts, and counterfeit sources. **Finite tests validate examples and implementations, not the universal Goldbach conjecture.**

Related SUCC source: `research/2026-11-12/prime_fixedpoint_cylinder/THEOREMS.md`, `research/2026-11-12/scott_relative_defect/SCOTT_PATH_RELATIVITY.md`, `research/2026-11-12/prime_interferometer_legacy/RESEARCH_NOTE.md`.

External background: Li and Vitanyi, *An Introduction to Kolmogorov Complexity and Its Applications* (Springer, 2019) https://link.springer.com/book/10.1007/978-3-030-11298-1 ; Tao, *Heuristic limitations of the circle method* (2012) https://terrytao.wordpress.com/2012/05/20/heuristic-limitations-of-the-circle-method/ ; FLINT FFT multiplication documentation https://flintlib.org/doc/algorithms/integers/multiplication.html . No priority claim for convolution, rank-one factorization or additive/ multiplicative coproducts.