# Theorems and obstruction map — primitive primes and the arithmetic cylinder

Date: 2026-11-12. Paper derivations checked by finite independent implementations on stated ranges, **not** Lean/theorem-prover proofs, mathematical peer review, or a new universal number-theoretic theorem.

## T1. Coassociative reduced multiplicative coproduct

Take the complex Hilbert space `H=l2(N_{>=1})` with orthonormal basis `|n>`, and `K=l2(N_{>=2} x N_{>=2})`. On the finite-support domain define

`Delta|n> = sum_{a,b>=2:ab=n} |a,b>`.

Every sum is finite. The map is coassociative in the algebraic finite-support sense: `(Delta tensor id)Delta|n> = (id tensor Delta)Delta|n> = sum_{a,b,c>=2:abc=n}|a,b,c>`. It is cocommutative under interchange of `a,b`. Distinct `n` have orthogonal images (the product `ab` is invariant), and `||Delta|n>||^2 = c(n)`, with `c(1)=0` and `c(n)=tau(n)-2` for `n>=2`. Thus the unique closed extension has domain `{sum_n x_n|n>:sum_n c(n)|x_n|^2<infinity}`. It is densely defined and is **unbounded**: `c(n)` is unbounded.

Its kernel is exactly `span{|1>,|p>:p prime}` (Hilbert closure). No composite basis vector is primitive; every prime and the unit are. The formal coalgebra counit belongs to the **unreduced** divisor coproduct. This reduced map is not incorrectly called counital.

## T2. The compressed commutator and exact fixed-point semigroup

On `H direct-sum K`, define `Q=[[0,0],[Delta,0]]` and `Q*= [[0,Delta*],[0,0]]` with their closed operator domains. On the algebraic core and whenever the products are defined,

`[Q*,Q] = diag(Delta*Delta, -Delta Delta*)`.

**Sector restriction:** the full commutator has additional zero vectors in the two-factor sector. Only the `H`/number-sector compression has precisely the primes and 1 as fixed states. Put `A=Delta*Delta`, the positive self-adjoint diagonal operator

`A|1>=0`, `A|n>=(tau(n)-2)|n>` for `n>=2`.

Then for every `t>0`, `exp(-tA)` is a bounded positive contraction and its fixed-point subspace is exactly `ker A`. For composites `n`, `tau(n)-2>=1`, whence the operator-norm identity `||exp(-tA)-P_primitive||=exp(-t)` (there exist prime squares with eigenvalue exactly 1). Also `P_primitive=(1/2pi) integral_0^(2pi) exp(i theta A) dtheta` as a **strong operator integral**, by integer spectra and character orthogonality. Restricting to finite support makes the identity elementary.

This is a selected Hilbert realization of a coalgebraic primitive condition. It is *not* an intrinsic commutator defined by category axioms alone.

## T3. A cheaper prime-birth commutator and recursive grade

Let `Omega(n)` count prime factors with multiplicity (`Omega(1)=0`), and set `b(n)=max(Omega(n)-1,0)`. Define `B|n>=b(n)|n>`. Again `ker B=ker A`. For each actual prime `p`, define the isometry `V_p|n>=|pn>` on `H`. On the finite-support core,

`[B,V_p]=V_p(I-P_vac)`, where `P_vac=|1><1|`.

Proof: at `n=1`, both `b(1)` and `b(p)` are zero. At `n>=2`, `Omega(pn)=Omega(n)+1`, so `b(pn)-b(n)=1`. The resulting commutator extends boundedly to all of `H`, even though `B` is unbounded. More generally for integer `m>=2`, `[B,V_m]=V_m(Omega(m)I-P_vac)`.

The multiplicative recursion for `a,b>=2` is `b(ab)=b(a)+b(b)+1`. Thus crossing the initial prime boundary and adding subsequent factors have different, explicitly encoded grades. The Fock interpretation `|n> <-> |(v_p(n))_{p prime}>` identifies `Omega` with the bosonic particle-number operator. This identification and the number-sector claims are mathematical constructions; no physical quantum-computation mechanism is asserted.

## T4. A genuine category with only terminal prime active coordinates

Objects: pairs `(m,F)` with `m>=1` and `F` a finite multiset of primes. Semantic evaluation `v(m,F)=m*product(F)`. Let `p=minprimefactor(m)` if `m` is composite, and define a total step

`T(m,F)=(m/p,F union {p})` for composite `m`, and `T(m,F)=(m,F)` if `m=1` or prime.

Define a thin category `C` with a unique arrow `s -> t` whenever `t=T^k(s)` for some `k>=0`, and no arrow otherwise. Because the active integer strictly decreases whenever a nonidentity step occurs, there are no nontrivial directed cycles. `T` is an endofunctor since `T(T^k(s))=T^k(T(s))`. Its fixed **objects** are exactly those whose *active* `m` is 1 or prime; do not claim that the context components are unique numbers or that arbitrary categorical identities are only present at primes (every object has an identity by definition). Semantic evaluation is preserved on every arrow. From `(n,empty)`, the process reaches a fixed object after `max(Omega(n)-1,0)` nontrivial steps, terminating in a complete prime factorization context and an active prime (or the unit for `n=1`). Unique factorization proves the returned prime multiset is independent of legal factor splitting after quotienting permutations/coherence.

A finite observer program enumerates `n=2,3,4,...` by SUCC successor and runs the finite terminating reduction on each. It outputs `n` when the initial object `(n,empty)` is fixed. The program has finite text and unbounded registers, outputs **all and only primes**, and runs indefinitely in the mathematical operational semantics. Every individual beta/delta-normalization path is finite; `omega`-length enumeration is the unbounded *outer* iteration, not an infinite beta reduction of one finite term. Infinitely many outputs follows from Euclid, not from an infinite physical computation.

## T5. One twisted circle at every midpoint: exact composite cancellation

Fix integer `n>=2`, `D_n={0,1,...,n-2}`, `H_n=l2(D_n)`, and the nonnegative integer-valued midpoint defect

`h_n(d)=b(n+d)+b(n-d)=Omega(n+d)+Omega(n-d)-2`.

The equality uses both endpoints `>=2`. Since `Omega(k)>=1` for `k>=2`, `h_n(d)=0` iff both `n+d,n-d` are prime. Define `H^(grade)_n|d>=h_n(d)|d>` and the unitary `U_n(theta)=exp(i theta H^(grade)_n)`. With `s_n=sum_(d in D_n)|d>`, put

`F_n(z)=sum_(d in D_n) z^(h_n(d))` and `G(n)=(1/2pi) integral_0^(2pi) <s_n,U_n(theta)s_n> dtheta`.

Character orthogonality gives `G(n)=[z^0]F_n(z)=#{d in D_n: n+d,n-d prime}`. This is an exact representation of the unordered Goldbach count, including `d=0` when `n` prime. Strong Goldbach is precisely `G(n)>0` for all `n>=2`. Nothing about unitarity, existence of the projectors, or exact cancellation forces `G(n)>0`.

**Finite exact rotations.** For any integer `M>max_d h_n(d)`, `G(n)=(1/M)sum_(j=0)^(M-1) F_n(exp(2pi i j/M))`. Because `Omega(a)+Omega(b)<=log_2(ab)<=2log_2(n)`, the simple executable choice `M=2*bit_length(n)` is sufficient for every `n>=2`. This is an exact roots-of-unity identity, NOT an efficient Goldbach algorithm: computing the grades requires factorization/primality information. For smaller `M`, nonzero grades divisible by `M` alias the target. At `n=10`, `F_10(z)=2+2z+3z^2+2z^4`, so `G(10)=2`, but `M=2` falsely returns 7; `M=8` returns 2.

The *extruded cylinder* is the lattice of midpoint heights `n>=2`, angular circle `theta mod 2pi`, and internal displacement fibers `D_n`. The angular winding is **source arithmetic data** (`Omega`), not an arbitrary choice of a pretty spiral. The fibers have varying finite ranks; one should not call this a globally trivial rank-fixed vector bundle.

## T6. The back-and-forth operator, commutator, and flat-gauge obstruction

Within `H_n`, let `W_2|d>=|d-2>+|d+2>` for permitted neighbors, with boundary terms omitted. On the parity-admissible subspace `(n+d)` odd for `n>2`, the same formula is self-adjoint. On the finite fiber,

`[H^(grade)_n,W_2]|d>=sum_(e=d+/-2 eligible) (h_n(e)-h_n(d))|e>`.

The exact Hilbert-Schmidt square is `2 sum_(edges d<e=d+2)(h_n(e)-h_n(d))^2`. This is a *grade-gradient diagnostic*, not a witness count, and has no fixed sign as an operator. A no-witness fake grade `(1,2,1,2,1)` has positive commutator energy 8. Thus **commutator activity alone does not imply Goldbach**.

Phase-conjugating the wiggle gives `W_2(theta)=U_n(theta)W_2 U_n(theta)^*`, a unitary conjugate with the **same spectrum** as `W_2`. On a 2D midpoint/displacement lattice, phase edges of the form `exp(i theta(h(destination)-h(source)))` have product 1 around every closed plaquette: differences telescope. The proposed twist is a pure-gauge connection; no nontrivial Wilson-loop holonomy or physical magnetic flux follows. A new curvature would require a genuinely non-gradient transport prescription, with its own source and coherences.

## T7. Chen's theorem provides a rigorous first-excited-sector bound

**CLASSICAL IMPORT.** Chen's theorem: every sufficiently large even integer `2n` is a sum of a prime `p` and an integer `q>=2` having at most two prime factors counted with multiplicity (a prime or a semiprime). Then choose `d=|p-q|/2`. Since `p+q=2n`, the displacement is integral and `0<=d<=n-2`. We have `b(p)=0`, `b(q)<=1`, hence `h_n(d)<=1`. Therefore

`forall sufficiently large n: min_(d in D_n) h_n(d)<=1`.

This is a **proved corollary of an imported classical theorem**; it is not a new proof of Chen's theorem and does NOT establish `min h_n=0`. An explicit published Chen theorem provides `2n>exp(36)` as one sufficient range; no finite verification up to that threshold is asserted here. Source: [Matteo Bordignon, *An explicit version of Chen's theorem*, Bull. Aust. Math. Soc. 105 (2022), 344–346](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/an-explicit-version-of-chens-theorem/2E6F5B87A198E00561CF2C21D147346A).

The difference from `<=1` to `=0` is the binary Goldbach obstruction. The classical sieve parity problem is a warning: positive counts of prime + semiprime states need not imply positive counts of prime + prime states without further source-sensitive estimates.

## T8. Source-dependence and countermodel

Replace the full prime alphabet by any infinite proper subset of primes, e.g. `S={p prime : p=1 mod 4}`. Its multiplicative monoid still has the free factorization/Fock structure, primitive-sector projections, birth commutator, finite normal-form observer and phase circle. But every sum of two elements of `S` is `2 mod 4`, so no multiple of 4 is a Goldbach-style sum in this model. Its fixed-point machinery is perfect; its additive coverage fails. This is a source substitution countermodel to any claim that the *categorical/Hilbert formalism alone* implies Goldbach. It does not refute any source-locked theorem specifically exploiting all rational primes.

A second countermodel: counterfeit midpoint grade `(1,2,1,2,1)` has no zero sector yet nonzero back-and-forth commutator; angular averaging yields zero. A finite-angle alias control (`n=10,M=2`) catches accidental composite survival.

## Exact next research obligation (no proof claim)

Can one use genuine prime-source short-interval/CRT estimates (not already-counted Goldbach witnesses), plus a signed Haar/Weyl bound, to show for every sufficiently large midpoint `n` that `dim ker H^(grade)_n>0`? Equivalent formulations: a uniform positive lower bound on `G(n)`, or a nontrivial estimate separating the grade-zero and grade-one sectors guaranteed by Chen. The phase projector and unitary wiggle rearrange arithmetic data; they do not provide this estimate. The earlier [CRT–Haar lower certificates](../prime_interferometer_legacy/RESEARCH_NOTE.md) offer finite sound probes; analytic completion remains UNVERIFIED.
