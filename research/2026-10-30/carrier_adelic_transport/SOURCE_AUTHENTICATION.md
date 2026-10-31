# Source authentication, rational summability, and finite-place blindness

Research bearing against parent `1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`.
This bearing is imported into the additive research directory. Paper proofs
below have exact finite probes; no new selected BBP Weyl saving or normality
theorem is claimed.

## 0. Novelty and source audit first

The repository already has more of the necessary arithmetic than the newest
PR summaries reveal:

* `docs/CLAIM_SUPPLEMENT_NATURAL_BBP_CARRIER.md`, NCB-05 and NCB-07,
  already give the odd-denominator property and exact all-odd-primary Q/Z
  reconstruction of the real-circle phase. Adding that map to a log-jet
  carrier is a useful coherent extension, not a newly discovered CRT bridge.
* `research/2026-10-24/PI_SOURCE_GENESIS_NONCOBOUNDARY.md`, section 3,
  already proves the NECESSARY weighted simple-residue obstruction
  `I_a(R)=sum_k 16^(-k) Res_(a+k) R=0` for rational Green tails.
  Its sections 6 and 7 also construct positive non-coboundary rational-phase
  sources matching any PRESCRIBED FINITE authentic asymptotic jet. Therefore
  simply excluding rational coboundaries cannot prove normality.
* `observational_succ/bbp_source_memory.py` already has the broad rational
  tail control `1/((n+1)(n+2))`; the Green paper has a leading-coefficient
  matched control. The four-pole integer-log-potential control below
  specializes that known mechanism so it can enter the new carrier exactly.
* Sibling PR415 `f650aab0c8710b502f3e08ec1cb2b351c26b2b3f`,
  `research/2026-10-30/selected_finiteband/kernel/KERNEL_TRANSPORT.md`,
  K01--K04 was read. The Hilbert transport constant, coherent Mellin
  sharpness and sparse-edit normality control survive this paper audit.
  They do not bound the selected energy.

Classical literature: discrete residues and rational summability are standard;
see Chen--Singer, *Residues and telescopers for bivariate rational functions*,
Advances in Applied Mathematics 49 (2012), 111--133,
<https://singer.math.ncsu.edu/papers/YAAMA1465.pdf>, and Arreche--Sitaula,
*Computing discrete residues of rational functions*, ISSAC 2024,
<https://arxiv.org/abs/2402.07328>. The constant-twist formula below is proved
directly; no scholarly-priority claim is made for it.

## 1. Complete twisted rational summability criterion

**PROVED LOCAL / classical difference-algebra construction.** Let `b` be a
nonzero rational number other than 1. Let `F(z)` be a rational function with
rational poles, specified by its full partial fractions and polynomial part.
In each orbit `a+Z` and each pole order `j>=1`, write `r_(k,j)` for the
coefficient of `(z-a-k)^(-j)` in F, and define

    I_(a,j)(F) = sum_(k in Z) b^(-k) r_(k,j).

All sums are finite. There exists a rational function T satisfying

    F(z) = b T(z-1) - T(z)

if and only if EVERY `I_(a,j)` vanishes. The solution is unique. Changing the
representative a scales the corresponding invariant by a nonzero power of b
and therefore does not alter its zero/nonzero verdict.

**Necessity.** Let `t_(k,j)` be T's partial-fraction coefficients. The operator
gives `r_(k,j)=b t_(k-1,j)-t_(k,j)`. Multiplication by `b^(-k)` and finite
summation telescopes to zero. Polynomial parts do not contribute poles.

**Sufficiency.** For each orbit/order, start below the minimum occupied k
with `t_(k,j)=0`, and recurse

    t_(k,j) = b t_(k-1,j) - r_(k,j).

At the largest occupied k=K, the result is
`-b^K sum_(k<=K)b^(-k)r_(k,j)=0`; thus the reconstructed coefficients have
finite support. Substitution recovers every principal part exactly. On
polynomials the operator is upper triangular in the monomial basis, with
diagonal `b-1`, so its polynomial restriction is bijective. This solves the
remaining polynomial part.

**Uniqueness.** A rational homogeneous solution with a pole would have
infinitely many translates of that pole. Hence it is polynomial, and the
invertible polynomial operator kills it only when it is zero.

The implementation accepts rational poles. The same argument over C is
valid orbitwise, and uniqueness gives descent to the coefficient field
when the complete solution is Galois invariant; no factorization-free
algebraic-pole algorithm is claimed here.

**Why all orders matter.** `F(z)=1/(z-1/3)^2` has zero ordinary residue at
every point but nonzero order-two invariant. A simple-residue-only test
is incomplete for general rational functions. The new code tests that
mutation and constructs full antidifferences, including polynomial parts.

## 2. The authentic source fails rational telescoping for a specific reason

For the original source

    r(z)=4/(8z-7)-2/(8z-4)-1/(8z-3)-1/(8z-2),

the poles `7/8,1/2,3/8,1/4` occupy four distinct Z-orbits. Their residues
are respectively `1/2,-1/4,-1/8,-1/8`, all nonzero. Consequently there is
no rational-function T with `r(z)=16T(z-1)-T(z)`.

In particular the true Green tail cannot equal one rational function of n
at all nonnegative integers: the recurrence would hold at infinitely many
points, hence as a rational-function identity, contradicting the invariants.
This recovers a source-level obstruction already implicit in the repository's
earlier necessary invariant. It is not a new irrationality proof and is not
a digit-frequency theorem. The older non-coboundary source counterexamples
show why this exclusion is insufficient even with positivity and zero seed.

## 3. Four simple poles, integer logarithmic potential, same Gamma rank: still nonnormal

**PROVED LOCAL calibration.** Put

    t_n = 1/[(8n+1)(8n+2)]  (n>=0),
    r*_n = 16 t_(n-1) - t_n  (n>=1).

With `a=8n-7`, elementary partial fractions give

    R*(a)=16/a-16/(a+1)-1/(a+8)+1/(a+9).

Thus this is a rational four-SIMPLE-pole source with integer residues. It is
positive, because t decreases and `16 t_(n-1)-t_n>15t_n>0`. Its Laplace source is

    Q*(x)=(1-e^(-x))(16-e^(-8x))>0 for x>0.

It has `Q*(0)=0`, `Q*'(0)=15`, so its leading source is `15/(64n^2)`, exactly
the authentic rank-two coefficient. The generic rank-two Gamma/Pascal/golden
observer limits therefore do not distinguish these sources. Their second
jets do distinguish them: `Q*''(0)=1`, whereas the authentic value is `-59`.

The source has a literal rational logarithmic potential

    V*(a)=a^16(a+9)/[(a+1)^16(a+8)],   d(log V*)/da=R*(a).

Thus the general rational log-jet multiplicative carrier, including its
all-prime arithmetic, accommodates this source with no extension of scalars.
For `B*_0(u)=1`, its first jet has the same literal zero initial condition.
But finite telescoping proves exactly

    U*_n = 16^n/2 - t_n,
    sum_(n>=1) 16^(-n) r*_n = t_0=1/2.

Every completed radix state is zero for n>=1, and the forced circle states
are `1-t_n`. For every fixed integer h,

    |(1/N) sum_(n=1)^N e(hU*_n)-1|
      <= (2*pi*|h|/N) sum_(n>=1)t_n
      < pi*|h|/(16N),

using `t_n<1/(64n^2)` and `sum_(n>=1)n^-2<2`. This is coherence with a
quantified O(1/N) error, not cancellation.

The source authenticator catches the mutation without using digits:
its pole orbits occur in canceling pairs; its next source jet is wrong;
and at the native a its potential satisfies `v2(V*)=-15` instead of -5.
In the extruded product this is `v2(B*_N(0))=-(16^N-1)` instead of
`-(16^N-1)/3`. The control changes authentic source membership explicitly.
It is a tight carrier calibration, not a counterexample to pi normality.

## 4. Finite-place observations are insufficient even over the entire same-source future

**PROVED LOCAL observation-fiber theorem.** Fix any finite prime set S,
nonnegative integer precisions `k_p`, any integer radix b>=2, any common
rational forcing sequence, and a rational initial seed s. Choose a prime
ell outside S not dividing b, set `L=product_(p in S)p^(k_p)`, and change
the seed to `s+L/ell`.

The two unwrapped paths differ exactly by `b^n L/ell`. For each p in S
this lies in `p^(k_p) Z_p` for EVERY n>=0. Hence all observations in
`Q_p / p^(k_p) Z_p`, including the local fractional part and the retained
integral digits, agree along the entire future. Their real phases differ
at every n, because ell divides neither L nor b. Thus no function of the
entire finite-place history can reconstruct the real circle on this class.

The theorem concerns exact phase/state recovery. It makes no claim that
these two rationally translated selected boundaries have different normality
status. Requiring every rational seed mutation to become nonnormal would be
an invalid calibration criterion.

The genuine irrational coherent seed `-pi/16` is a real-extension control;
it cannot silently be embedded as a diagonal element of Q or assigned a
canonical value in every Q_p. One must keep the rational log-jet module and
its real scalar extension typed separately.

For authentic U_n, the ordinary local fractional character at p=2 is
identically trivial, since its denominator is odd. This does not make the
2-adic integral clock useless; it says that clock and fractional-character
observations are different, as NCB-05 already records.

## 5. Hostile verification of the root's all-asymptotic-jet flat countermodel

The following is an independent audit of a construction supplied by the
root agent, not a separate discovery. Write b=16. Fix M>=0,K>=1 and

    q=sum_(j=1)^(M+K)b^(-j)r(j).
    L_n=M+K-n for n<=M; L_n=K+n-M for n>=M.
    d_n=sum_(j=1)^(L_n)b^(-j)r(n+j).
    U~_n=b^n q-d_n.

`L_0=M+K` gives U~_0=0. For n<=M, `L_(n-1)=L_n+1`, so the exact new
forcing is r_n. For n>M, put `ell=K+n-M-1`; then `L_(n-1)=ell`,
`L_n=ell+1`, and direct subtraction yields exactly

    r~_n=r_n-b^(-ell)r(n+ell)-b^(-ell-1)r(n+ell+1).

Since ell>=K and authentic r is positive and decreasing,

    0 <= (r_n-r~_n)/r_n <= b^(-K)(1+1/b)<1.

Thus positivity and arbitrarily small uniform relative perturbation are
certified. At fixed M,K the defect is exponentially small in n, so the
Dirichlet difference is entire in s by local uniform convergence. For the
shifted rational source r(n,u), on every compact u-domain avoiding its
finite poles, each u derivative has a polynomial n bound; exponential
decay therefore survives every mixed derivative. Consequently ALL pole
residues in s and their u jets agree, while the completed boundary is the
rational q, hence nonnormal.

**Required distinctions.** The regular Laurent finite parts generally
change, as does the full analytic function. Equal polar data is not equal
analytic germ. The modified time source is not one fixed finite-pole
rational function of n. This is a genuinely stronger all-asymptotic-jet
obstruction in the enlarged sequence class than the older finite-jet
counterfamilies, not a refutation within the exact four-pole BBP class.

## 6. Validation

`coboundary_probe.py`: 13/13 stdlib Fraction tests passed, covering full
pole-order reconstruction, mixed polynomial parts, wrong-residue and
wrong-order mutation controls, source/zero-seed telescoping, exact partial
sums, rank-two/second-jet separation, ordinary local characters, finite
integral precision and authentic odd denominators. The bearing's initial
raw receipt is `receipts/adversary_coboundary_tests.log`; all 13 methods
also passed in the root's final 60-method `receipts/focused.log` replay.

`receipts/adversary_symbolic_receipt.json`: a separately expressed SymPy
1.14.0 calculation run by the adversarial bearing
passed five exact symbolic identities for the log potential, telescoping,
leading coefficient and two source jets. Shared theorem definitions remain
shared provenance; this is not an external blind referee.

Two exploratory path reads used nonexistent guessed source filenames,
and one unused literature URL resolved to an unrelated paper; neither is
a mathematical validation result or a cited source. Discovery was repaired
with rg and title search. The mathematical test suite had no failed case.
