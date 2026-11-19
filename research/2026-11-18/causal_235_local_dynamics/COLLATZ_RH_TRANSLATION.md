# Causal affine dynamics at 2 and 3: BBP, Collatz, and the RH boundary

Research date: 2026-11-18, America/New_York. Read-only reconstruction of SUCC main
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`. No academic priority claimed.
The identities below are elementary/classical; this note integrates their precise causal
roles. General Collatz, R0, base-16 normality of pi, and RH remain OPEN.

## 1. Exact proposition: a forward path has a vector of precision changes

Let `x_(j+1)=a_j x_j+b_j`, with nonzero rational `a_j` and rational `b_j`.
Two initial states following the **same ordered affine branches** satisfy

    x_N-y_N = A_N (x_0-y_0),    A_N = product_(j<N) a_j.

Consequently, for every prime p and nonzero difference,

    v_p(x_N-y_N) = v_p(x_0-y_0) + sum_(j<N) v_p(a_j).

This follows by subtracting each forward update and iterating. It is a theorem at every
finite horizon, not an assertion about an infinite observed history. The translation is

    B_N = sum_(j<N) b_j product_(j<l<N) a_l,
    x_N = A_N x_0+B_N.

The order of the translations matters even when `A_N` agrees. If each `a_j` is a rational
2,3-unit (a signed product of powers of 2 and 3), unique factorization gives exactly

    |A_N|_infinity |A_N|_2 |A_N|_3 = 1.

This only balances absolute sizes of this **one diagonal rational slope**. It supplies
neither its affine translation nor an orbit-frequency or signed-phase theorem. The same
three-place formula can fail for states: `q=1/5` requires the missing 5-adic factor.

### Two source-faithful specializations

| System and same-path convention | Slope A_N | Change in binary precision | Change in ternary precision | Real error multiplier |
| --- | --- | --- | --- | --- |
| Authentic BBP, fixed source times 1 through N | `16^N` | `+4N` digits | 0 | `16^N` |
| Shortcut Collatz, realized N-bit parity word with s odd steps | `3^s/2^N` | `-N` digits | `+s` digits | `3^s/2^N` |

For Collatz the same-branch qualification is essential. Two integers in the same residue
class modulo `2^N` realize the same first N parities. Within that cylinder the precision
identity is exact; beyond it the branch selector can change. For BBP the source is the
literal four-pole `r(n)` and the authentic selected seed is `U_0=0`. Comparing different
seeds diagnoses sensitivity; it does not replace that source.

This quantifies a useful distinction in the observer's internal model. BBP suppresses
old seed error locally at 2 while retaining it at 3 and amplifying it at the real place.
Shortcut Collatz loses binary precision as it consumes the branch word, while its fixed
branch maps suppress ternary error. A local contraction at one place does not mean a
forward observer has recovered, or controlled, the full real state.

## 2. What the ordered Collatz history adds

Use the shortcut convention

    T(x)=x/2 if x is even, and (3x+1)/2 if x is odd,

on positive integers. For a word `epsilon=(epsilon_0,...,epsilon_(N-1))`, put

    s=sum epsilon_j,
    b_epsilon=sum_(j:epsilon_j=1) 2^j 3^(sum_(l>j) epsilon_l).

On its realized cylinder,

    T^N(x)=(3^s x+b_epsilon)/2^N,
    x = -3^(-s)b_epsilon mod 2^N.

The second statement is both necessary and sufficient. Inductively, a parity prefix of
length N occupies one class modulo `2^N`; its two lifts modulo `2^(N+1)` have terminal
states differing by `3^s`, an odd integer, so exactly one lift realizes either next bit.
This proves the cylinder bijection without assuming termination. The translation formula
then follows by induction from `b_(j+1)=3^(epsilon_j)b_j+epsilon_j 2^j`.

The existing SUCC result is `observational_succ/black_sun_collatz.py`, claims BS-C1--3 in
`research/2026-10-14/BLACK_SUN_INDEPENDENT_CAMPAIGN.md`, and
`docs/CLAIM_SUPPLEMENT_BLACK_SUN.md`. These are antecedents, not new discoveries here.

**Chronology witness.** Words `(1,0)` and `(0,1)` both have slope `3/4`; their affine maps
are `(3x+1)/4` and `(3x+2)/4`, with cylinders `x=1 mod4` and `x=2 mod4`. Counts alone
lose the selected branch and its offset. A forward observer may calculate an inverse
word from its model, but this is not a legal backward carrier transition.

**Quantifier repair.** The existing BS-C2 prose says `v_3(b_epsilon)=0` and
`v_3(2^N-3^s)=0` for every word. The needed hypothesis is **s at least 1**. The last odd
position supplies a 3-adic unit while earlier odd positions contain a factor of 3; the
denominator is then `2^N mod3`. For an all-zero word, `b=0`; at N=2 the denominator is 3.
The old corollary that no positive Collatz cycle contains a multiple of 3 survives,
because a positive cycle cannot consist only of halving steps. No archival source was
modified for this audit.

**Long-expansion control.** For every N, the positive seed `x=2^N-1` realizes N successive
odd steps and reaches `3^N-1`. Thus no fixed finite horizon guarantees real contraction
for every positive input. On the explicitly enlarged signed-integer domain, `-1` has
the same all-odd word forever and is a fixed point. Cylinder completeness on `Z_2`
therefore cannot be read as positive-integer termination.

**A real 2--3--5 arithmetic relation, with its type stated.** For possible Collatz cycle
denominators, `5 | (2^N-3^s)` iff `N=3s mod4`. More generally 2 is primitive modulo `5^r`
(order `4*5^(r-1)`, by the elementary lifting identity
`v_5(2^(4m)-1)=1+v_5(m)`). If `a_r` is the unique discrete logarithm of 3 to base 2,

    5^r | (2^N-3^s)  iff  N=a_r s mod (4*5^(r-1)).

Exact computed `a_r` for r=1,...,6: `3,7,7,107,607,8107`. This refines the old BS-C2
prime-5 gate. It is a congruence condition on a cycle **candidate**, not a 5-cycle,
not a Fibonacci intertwiner, and not a proof that such a cycle exists.

## 3. The closest real analytic template is Tao's conditional 3-adic mixing

For the odd accelerated map, an actual odd input yields

    S(x)=(3x+1)/2^a,    a=v_2(3x+1) >=1.

Conditioned on a prescribed legal valuation sequence `a_1,...,a_n`, the finite causal
solution has slope `3^n/2^(a_1+...+a_n)` and translation

    sum_(j=1)^n 3^(n-j) 2^(-(a_j+...+a_n)).

Older inputs are damped by powers of 3 in `Q_3`. This is the precise analogue of the
finite BBP history `sum_(j=1)^n 16^(n-j)r(j)`, where damping occurs in `Q_2`.
The BBP source has genuine 3-adic poles and its analogous backward Green series fails
to converge, as already proved in `BBP_PRIMAL_RECURSION_2ADIC_3ADIC.md`, TR-2.

Tao's paper makes a sophisticated version of this interaction useful: binary valuation
statistics feed a skew walk on ternary residue groups, and conditional high-frequency
mixing supports transport of a first-passage distribution. The stationary law is not
uniform even modulo 3 (probabilities `0,1/3,2/3`); local contraction alone is not the
mixing theorem. The conclusion concerns logarithmic-density almost all positive seeds,
not every seed. Reversing finite input order to express a stationary law is a model
identity, not physical travel into the past. [Primary source 2, Section 1.4.]

**BBP dependency cut.** Source-attested 2-adic time coordinates and 3-adic pole/offset
coordinates can index a conditional observation problem. To transfer this template,
one must establish a source-selected signed estimate for the actual real phases inside
those classes, or a transport bound strong enough to imply one. Uniform arithmetic
marginals, a stationary local law, and local contraction do not supply it. SUCC already
states this missing edge after CRT-1 in `BBP_PRIMAL_RECURSION_2ADIC_3ADIC.md`; adding
Tao's theorem name does not close it. The comparison is a construction guide, not an
application of Tao's hypotheses to pi.

## 4. RH: distinguish composite interaction from a new primitive source

On the absolutely convergent Euler domain, the two local factors are

    Z_23(s)=1/((1-2^(-s))(1-3^(-s))).

As a formal power series in `u=2^(-s),v=3^(-s)`, its coefficient of `uv` is 1, whereas

    log Z_23 = sum_(a>=1) u^a/a + sum_(b>=1) v^b/b

has no mixed term. Multiplicative formation of the integer 6 is real; a primitive
Euler place at 6 is false. Adding `(1-(uv))^(-1)` changes the coefficient at 6 to 2 and
inserts a false primitive log-source. Every coefficient below 6 remains unchanged.

The corresponding fixed-observer test is exact. Hold the Gamma, pole and contact
terms and a single admissible test function fixed; let Q_S denote the source Weil
form retaining prime places in S. Because its prime terms add linearly,

    Q_{2,3} - Q_{2} - Q_{3} + Q_empty = 0.

This is a complete four-cell contrast on the fixed functional. A nonzero contrast
between separately optimized eigenvalues reflects the nonlinear selection of test
vectors; it does not establish a new primitive 6 source term. Genuine global coupling
can enter the common diagonal rational lattice, the test domain, Fourier normalization,
and optimization; their maps must be specified.

SUCC already has the relevant boundary in `SOURCE_MODEL_ANALYTIC_GLUING.md`, SI-01--05:
the same diagonal rational source supplies finite Euler factors and one real Gamma
factor, but global theta/Poisson transport is an additional classical theorem. Every
fixed finite prime set has a nonzero normalized modular defect in the limit described
there. A finite 2,3 sector does not inherit the all-prime identity by extrapolation.

An RH handoff would need an exact identification with the completed, signed Weil form
on its valid test domain and an all-support sign theorem, including Gamma/pole/contact
and half-density data. Generic observer covariance, an adic norm identity or a finite
positive matrix supplies none of these. The source guards and fake-6 control in
`docs/RH_HANDOFF.md` apply. Connes--Consani's primary article explicitly distinguishes
the positive compression trace from the Weil distribution and controls their
difference in a specified archimedean support window. [Primary sources 3 and 4.]

## 5. Verification and classification

`test_local_affine.py`: 8 unittest methods passed on 2026-11-18. Exact Fraction and
integer arithmetic, no approximate pi digits or zeta zeros used as construction inputs.

- All 2,046 binary words of lengths 1 through 10: distinct residue cylinders and exact
  cocycle checked by actual execution at two positive representatives each.
- All words through length 8: exact local precision change checked on same-cylinder
  pairs; mutant translations differing by 1 rejected.
- BBP steps 1 through 20: original four-pole recurrence and rational seed difference
  checked at primes 2,3,5.
- Positive all-odd expansion through length 100 and signed fixed-point control -1.
- All-zero valuation exception and authentic-versus-fake6 Euler coefficient controls.

These finite checks calibrate implementations. The universal affine and cylinder
statements are supported by the elementary derivations above. They are local proof
steps and source-typed translations, not proofs of an infinite global conjecture.

## Primary references read during this task

1. Daniel J. Bernstein and Jeffrey C. Lagarias, *The 3x+1 Conjugacy Map* (1996),
   author-hosted paper: https://websites.umich.edu/~lagarias/doc/bernstein.pdf .
   Introduction and parity-map formula: the conjugacy is on `Z_2`.
2. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*,
   Forum of Mathematics, Pi 10 (2022), e12; current arXiv v7, 2026-07-16:
   https://arxiv.org/html/1909.03562v7 . Theorem 1.3 and Section 1.4,
   Propositions 1.14 and 1.17; version history states corrected typos, including Lemma 7.9.
3. Alain Connes and Caterina Consani, *Weil positivity and Trace formula, the
   archimedean place* (2021), author-hosted paper:
   https://alainconnes.org/wp-content/uploads/Selecta.pdf . Introduction, equations
   (1)--(6), and Appendix C state domains, normalizations, and positivity criterion.
4. Alain Connes, Caterina Consani and Matilde Marcolli, *The Weil proof and the geometry
   of the adeles class space* (2007): https://arxiv.org/abs/math/0703392 .
   Positivity of the relevant trace pairing is an RH-equivalent missing condition,
   not a consequence of constructing the geometric representation.

No source is used as evidence for a stronger theorem than it states. The specific
3--13--5 holonomy mentioned in conversational context was not located in the read
main files and is not relied upon here.
