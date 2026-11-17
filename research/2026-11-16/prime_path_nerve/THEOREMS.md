# PRIME-PATH NERVE — signed computational paths and the authenticated prime state

**Research status, 2026-11-16:** Exact classical arithmetic recast as a source-typed SUCC interface. No claim of new mathematical priority, RH, Weil positivity, or pi normality. The key interpretation is the user's hypothesis: *the signed superposition of previously realized prime paths at a current integer and the signed superposition of source-labelled paths to that integer are two presentations of the same observable when the path category is the squarefree divisibility category.* This is **not** a general equivalence of arbitrary causal graphs and prime arithmetic. The choice and authentication of the prime-source labels are required hypotheses.

## PPN-01. Finite prime source and divisibility-path nerve (EXACT)

Fix a finite set `S` of **distinct actual rational primes** and `Q=prod_(p in S) p`, with `Q=1` for the empty set. For positive integer `n`, put

`D_S(n)={p in S : p divides n}`.

Define `K_S(n)` to be the full simplex on this vertex set: a subset `A subset D_S(n)` is a face, including the empty face. Such a face represents a *simultaneous source-labelled factorization constraint* `prod_(p in A) p | n`. It is not a distinct physical trajectory and does not assert that all ordered programs with the same endpoints are equivalent.

The empty-face-normalized signed face sum is

`I_S(n)=sum_(A subset D_S(n)) (-1)^|A| = prod_(p in S)(1-1_[p|n])`.

It equals `1` iff `gcd(n,Q)=1`, and equals `0` otherwise. With the **ordinary unreduced** simplicial Euler characteristic and `chi(empty)=0`, `I_S(n)=1-chi(K_S(n) without empty face)`. A nonempty full simplex is contractible, hence has ordinary Euler characteristic 1; the empty complex has characteristic 0. This gives a qualitative *incidence/topological predicate* on incoming authenticated factor paths. It is not a primality oracle without enough source primes.

Because the subset-to-squarefree-divisor map is a bijection, the same observable is

`I_S(n)=sum_(d|gcd(n,Q)) mu(d)`.

**Adversaries:** For `S={2,3,5}`, `I_S(49)=1` though 49 is composite; adding the genuine prime 7 changes it to zero. Including the candidate number itself as a factor would falsely disqualify that prime. The relevant prime inventory for `n>=2` is all primes `p<=sqrt(n)` (or all genuine primes `p<n`). Thus `n` is prime iff it has no *nonunit incoming multiplication factorization*: equivalently `I_{S(n)}(n)=1` for `S(n)={p prime : p<=sqrt(n)}`. This is the classical atomicity definition/sieve in a categorical vocabulary, not a new complexity result. By contrast the mere claim that an arbitrary set of paths with common endpoints is a prime-state simplex is REFUTED by, for instance, two parallel graph edges with no multiplicative/divisibility labels.

## PPN-02. CRT prime basis and an exact coherent Fourier representation (EXACT)

For authenticated squarefree `Q`, the Chinese remainder isomorphism gives

`Z/QZ ~= prod_(p|Q) F_p`, with the current state `n` represented by `(n mod p)_p`.

Each local survival predicate has the exact additive-character expansion

`1_[p does not divide n] = 1 - (1/p) sum_(h=0)^(p-1) exp(2 pi i h n/p)`.

Tensoring these local identities is **the same** prime-state projector `I_S(n)`, but now expressed in a local Fourier basis. Let `c_Q(h)=sum_(a mod Q, gcd(a,Q)=1) exp(2 pi i ha/Q)` be the Ramanujan sum. Orthogonality yields the global identity

`I_S(n) = (1/Q) sum_(h mod Q) c_Q(h) exp(-2 pi i hn/Q)`.

For squarefree Q, `c_Q(h)=prod_(p|Q) c_p(h)` with `c_p(h)=p-1` if `p|h`, and `-1` otherwise. Equivalently, `c_Q(h)=sum_(d|gcd(Q,h))d mu(Q/d)` is an **integer** coefficient. All amplitudes and phase orientations are fixed by the actual source, not fitted. This is algebraic Fourier superposition, **not physical quantum superposition or a probability law for pi digits**. The inverse DFT and the divisibility-path nerve produce the same function `I_S(n)`; arbitrary path categories do not.

## PPN-03. Prime insertion and the exact finite boundary defect (EXACT)

For a new genuine `p` not in S, `I_(S union {p})(n)=I_S(n)(1-1_[p|n])`. On the finite Q-level, this is adding an authentic local CRT factor and restricting the observed current states. The prime-insertion square commutes because both the divisor-face sum and the CRT Fourier projector equal this same source-bound predicate.

Define for Re s>1 the **restricted arithmetic Dirichlet source**

`Z_Q(s)=sum_(n>=1) I_S(n)n^(-s)`.

A finite Möbius expansion, legitimate in absolute convergence, yields

`Z_Q(s)=zeta(s) F_Q(s)`, `F_Q(s)=prod_(p|Q)(1-p^(-s))`.

Independently, using the ACTUAL reduced residue classes gives the Hurwitz realization

`Z_Q(s)=Q^(-s) sum_(1<=a<=Q,(a,Q)=1) zeta(s,a/Q)`.

Both have the same meromorphic continuation by uniqueness. At `s=-1` Hurwitz's classical special value produces the exact finite-state term

`R_Q(-1):=Z_Q(-1)=-(Q/2) sum_((a,Q)=1,1<=a<=Q) B_2(a/Q)`.

Meanwhile the finite-prime Euler multiplier `P_Q(-1)=prod_(p|Q)(1-p)^(-1)` is rational. The source-typed **compensation identity** is

`P_Q(-1) R_Q(-1)=zeta(-1)=-1/12`.

Prime insertion updates `P_(Qp)(-1)=P_Q(-1)/(1-p)`, `R_(Qp)(-1)=(1-p)R_Q(-1)`. Each finite step preserves the completed endpoint. **The raw infinite Euler product at -1 has NOT been equated to zeta(-1)**. This is a Q-indexed family of finite exact cancellation ledgers; the residuum is a continuation supplied by Hurwitz, not an ordinary sum of positive naturals.

For m>=1, the all-negative-odd tower obeys

`Z_Q(1-2m)= -Q^(2m-1)/(2m) sum_((a,Q)=1) B_(2m)(a/Q) = zeta(1-2m) prod_(p|Q)(1-p^(2m-1))`.

It is the exact finite-prime counterpart of SUCC's finite-Pascal positive-clock construction of `zeta(-m)`; their inputs and algorithms remain distinct. The shared special value does not identify all internal source histories.

## PPN-04. The analytic-order obstruction is essential (EXACT negative control)

Let S grow through all primes. For each fixed n, `I_S(n)` tends to `1_[n=1]`. For Re s>1, dominated convergence therefore gives `Z_Q(s)->1`. The completed function of this limiting one-point Dirichlet source is identically one.

But along the same prime prefixes,

`Z_Q(-1)=(-1/12)prod_(p|Q)(1-p)` has unbounded absolute magnitude. Likewise `P_Q(-1)` tends to zero in real absolute value while their product is exactly `-1/12` at every finite Q. Thus **taking the all-prime/pointwise limit and continuing the finite-prime paths to -1 do not commute**. This is a rigorously demonstrated source-map/boundary defect, not evidence that arbitrary infinite products are assigned special zeta values by convergence.

An additional adversary is the **fake composite 6**: appending `(1-1_[6|n])` to the established `{2,3}` projector changes nothing (it is redundant), but adding the spurious Euler factor `(1-6^(-s))^(-1)` changes the analytic object. Therefore the sieve projector does not by itself authenticate prime factor labels. Actual multiplicative atoms and correct Euler multiplicities must be checked separately.

## PPN-05. Reflection and the authenticated BBP scale (EXACT classical composition)

Write `x_BBP=sum_(n>=1)16^(-n) r(n)=pi/16`, with the **original four-pole BBP source**, its literal `U_0=0`, and exact completion `U_n+T_n=16^n x_BBP`. The classical imported BBP evaluation identifies the endpoint with geometric pi. The actual completed zeta is

`xi(s)=(1/2)s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)` and satisfies `xi(s)=xi(1-s)`.

Then `xi(-1)=xi(2)=pi/6=(8/3)x_BBP`. More generally `xi(1-2m)=xi(2m)` and the positive even values can be written with Bernoulli numbers and the fixed BBP scale via the classical even-zeta evaluation. This is an exact **scalar completion** with source provenance, not a component-by-component map from genuine prime powers to BBP integer winding.

Define `xi_Q(s)=F_Q(s)xi(s)` and the *finite-prime reflection defect*

`D_Q(s)=F_Q(s)/F_Q(1-s)` (as a meromorphic quotient). Its cross-multiplied identity is `xi_Q(s)=D_Q(s)xi_Q(1-s)`. On the critical line `s=1/2+it`, `|D_Q(s)|=1`; the continuous phase at t=0 has derivative

`theta'_Q(0)=2 sum_(p|Q) log(p)/(sqrt(p)-1)`.

This phase velocity is an exact **finite source measurement**. It does not assert that finite Euler truncations have the same functional equation as xi, that all their zeros are critical, or that the accumulated phase velocity is bounded as Q grows. In fact `F_Q` has zeros at `s=2 pi i k/log p` on `Re s=0`. The finite defect does NOT establish RH or the Weil form's required global sign.

## PPN-06. Exact information boundary between prime states and BBP carry (NO-GO)

All of `I_S(n), Z_Q(s), F_Q(s), xi(s), D_Q(s)` are independent of the BBP initial seed. The original zero seed `s=0` and the same-four-pole coherent counterseed `s=-pi/16` therefore share all these arithmetic/analytic prime readouts, while their completed radix-16 trajectories differ: the counterseed completes to the constant zero phase. Accordingly, no inference from *only* the source-blind scalar bridge or prime-side finite projector to a signed all-shell BBP carry estimate is valid without an additional joint arrow carrying the authentic zero-selected chronology.

The candidate new arrow is a phase- and provenance-preserving joint measurement combining `I_S(n)` / local characters / prime-power current with `C_n=floor U_n`, `u_n={U_n}`, and the completed phase. Before asserting a nonzero asymptotic cross-term it must (i) fix a common observation time/lag, (ii) retain the actual odd denominator, winding and boundary source, (iii) declare the phase and normalization basis, (iv) discriminate the wrong seed, fake six and the coboundary `g(n)=2n^2` with its CORRECTED tail, and (v) prove a nontrivial all-large-shell saving, rather than fitting finite examples.

**Status:** Primordial prime objects, the nerve, CRT characters, and finite Hurwitz identities are CLASSICAL/EXACT within these definitions. The SUCC multi-observer synthesis is a new-to-project typed organization. **No novel primality theorem, RH proof, source-selected pi normality or universal path-to-prime isomorphism is claimed.**
