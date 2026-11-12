# The mixed additive–multiplicative intertwining defect

**2026-11-12; additive follow-up to CARR-03.** This is a precise operator identity and source-specific no-go control, **not a proof of Goldbach**.

## Statement (PROVED LOCAL)

On `H = ell^2(N_{>=2})` use basis `|n>`. On finite support define

```
Delta_plus|N> = sum_{a+b=N, a,b>=2} |a,b>,
Delta_times|n> = sum_{ab=n, a,b>=2} |a,b>,
P = 1_{ {0} }(Delta_times* Delta_times),
```

where `P|n>=1_prime(n)|n>`. Write `p(n)=1_prime(n)`. The two plausible ways to transport prime detection through additive splitting define a *naturality/intertwining square*:

```
H -------- P --------> H
|                       |
Delta_plus               Delta_plus
|                       |
v                       v
H tensor H -- P tensor P --> H tensor H
```

Its difference is the operator

```
D = (P tensor P) Delta_plus - Delta_plus P.
```

**This is not literally an ordinary endomorphism commutator:** the input is in `H`, output in `H tensor H`. On every finitely supported basis vector,

```
D|N> = sum_{a+b=N, a,b>=2} [p(a)p(b)-p(N)] |a,b>.
```

Images from different total sums have disjoint pair-basis supports, hence `D*D` is diagonal on the finite-support core, with eigenvalues

```
c(N) = sum_{a+b=N, a,b>=2} [p(a)p(b)-p(N)]^2 >= 0.
```

If `N>=4` is **even**, then `p(N)=0`, and therefore

```
D|N> = (P tensor P) Delta_plus|N>
||D|N>||^2 = c(N) = R(N).
```

Thus **binary Goldbach is equivalent to the nonvanishing of the mixed defect on every even basis vector `|N>` with `N>=4`**, and to the quadratic-form inequality `D*D >= I` on that even sector. The equivalence is a structural recoding, not a proof of the inequality. Bare positivity `D*D>=0` is insufficient.

## Why this is a meaningful coupling

A *multiplicative* primitive-state detector cannot be pushed across an *additive* coproduct without a precisely measured discrepancy. For even numbers, that discrepancy is exactly the Goldbach witness vector. Unlike assigning phases `exp(i theta(b(y)-b(x)))` along arrows, this defect is not a telescoping gradient by construction. It is also **not** evidence of nontrivial gauge holonomy or physical entanglement. It is a noncommuting square of *different arithmetic operations*.

This is the correct candidate to combine with the Scott interval-of-certificates layer, prime-local CRT/Haar estimates, and the cylinder wave packet. A useful next step would be to bound `||D|N>||` strictly away from zero using independently derived information about the actual prime source, without relying on preknown witnesses.

## Hostile source control (PROVED LOCAL negative)

If `p` is replaced by the indicator of `S={q prime: q=1 mod 4}`, the same Hilbert definitions, Fourier conversion and projection structures exist (with `P` understood as the mutated source projector). Every even `N=0 mod 4` has `p(N)=0` and `p(a)p(b)=0` on the sum fiber, hence `D|N>=0`. Generic operator coherence, low-rank source compression and Scott continuity cannot establish the needed nonvanishing without **genuine full-prime arithmetic**.

This does not refute a theorem using the actual prime projector built from `Delta_times` on the integers. It refutes any source-blind implication from the abstract categorical/hilbert structure alone.

## Finite check (OBSERVED, exact)

In the package's exact `carrier_probe.py`, compare `two_color_goldbach(N,p)` against the squared coefficient vector of the above defect for even `N<=256`; `p(N)=0` and each coefficient is a literal integer `0` or `1`. The existing `test_prime_pair_adjoint_composition` verifies the same Gram equality via an independent direct trial-division predicate and endpoint convolution. The altered 1-mod-4 source kills every tested multiple of 4. These are finite sanity checks, not verification of the universal assertion.

**Provenance:** [parent carrier dossier](README.md), [prime fixed-point source](../prime_fixedpoint_cylinder/THEOREMS.md), [Scott-relative factorization certificates](../scott_relative_defect/SCOTT_PATH_RELATIVITY.md). External context: Tao, *Heuristic limitations of the circle method* (2012), https://terrytao.wordpress.com/2012/05/20/heuristic-limitations-of-the-circle-method/ .