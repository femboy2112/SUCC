# Atomic and Haar multiplicative shifts: a sharp interface theorem

Status: **PROVED LOCAL, PAPER**; exact finite controls are supplementary.
No Lean claim is made for the measure-theoretic theorems in this document.
Independent Stream B derivation, 2026-10-18, based on repository commit
`610efacf02556e1c5922bc5d4e87d0087f19b446`. No archival source was changed.

The relevant unmerged comparison is [PR #176](https://github.com/femboy2112/SUCC/pull/176),
head `a17197697c0ea0259592500b233419fbedf691cf`, especially
[`MOBIUS_INDEX_INFINITY_SOURCE_TRANSPORT.md`](https://github.com/femboy2112/SUCC/blob/a17197697c0ea0259592500b233419fbedf691cf/research/2026-10-18/MOBIUS_INDEX_INFINITY_SOURCE_TRANSPORT.md).
Its finite sieve and Schwartz–Bruhat correspondence motivate the comparison;
they are not dependencies of the independently derived proofs below. A PR
description or passing check on that head is not integration into this base.

The result is independent of RH, zeta zeros, Suzuki's form and Connes' trace
formula. Its purpose is to decide which proposed arithmetic comparison maps
actually exist. It is not a positivity theorem for a signed Weil distribution.

## 1. Carriers, adjoints and the calibration theorem

Let `H_d = ell²(N_{>=1})` with orthonormal basis `e_n`. Let
`H_c = L²(Zhat,mu)` for normalized **additive** Haar measure. For each integer
`a >= 1`, multiplication `m_a:x -> ax` is an injective homeomorphism of
`Zhat` onto the clopen subgroup `a Zhat`, with index `a`. Indeed
`Zhat = product_p Z_p`; injectivity and the index follow coordinatewise.
Haar uniqueness, or counting finite congruence cylinders, gives
`mu(m_a A) = mu(A)/a` for every measurable `A`.

Define

```
V_a e_n = e_(an),
U_a f(x) = sqrt(a) 1_(a Zhat)(x) f(x/a).
```

Division occurs only on `a Zhat`. The Haar change of variables proves
`||U_a f||² = ||f||²` and, with either consistent complex inner-product
convention,

```
V_a* e_n = e_(n/a) if a divides n, and 0 otherwise;
U_a* g(y) = a^(-1/2) g(ay);
U_a U_a* = multiplication by 1_(a Zhat).
```

These formulas define operators on equivalence classes: a null set and its
image/preimage under the restricted scaling remain null. Both families are
multiplicative, and for distinct primes `p,q` they doubly commute:
`U_p U_q* = U_q* U_p`, and likewise for `V`. For the Haar identity, use
`qx in p Zhat iff x in p Zhat` when `p != q`.

**AH1 (bounded all-prime disjointness).** For every bounded complex-linear
`T:H_d -> H_c`, if for every prime `p`

```
T V_p = U_p T     and     T V_p* = U_p* T,
```

then `T=0`. The same conclusion holds for bounded intertwiners in the reverse
direction preserving both actions.

**Proof.** Put `g=T e_1`. Every `V_p* e_1` vanishes, hence `U_p* g=0`.
The kernel of `U_p*` consists exactly of functions vanishing on `p Zhat`.
Consequently `g` is supported, up to null sets, on

```
Zhat^times = intersection_p (Zhat \ p Zhat).
```

For finite `F`, the Chinese remainder theorem gives
`mu(intersection_(p in F) (Zhat \ p Zhat)) = product_(p in F)(1-1/p)`.
The all-prime product is zero. One elementary proof is that its reciprocal,
over primes at most `N`, is the sum of `1/n` over integers supported on those
primes, hence at least `sum_(n<=N)1/n`, which diverges. Continuity of measure
from above therefore gives `mu(Zhat^times)=0`, so `g=0`. Every `e_n=V_n e_1`,
and multiplicativity gives `T e_n=U_n g=0`. Boundedness extends zero from the
dense finite-support subspace to `H_d`. Taking adjoints reduces the reverse
direction to the same proof. QED.

The conclusion uses the actual **vacuum** `e_1`, not an arbitrary Hilbert
unit vector. A generic Haar unit vector need not be killed by all adjoints.

**AH2 (incompatible strong limits).** For finite prime sets `F`, put

```
P_F^d = product_(p in F)(I - V_p V_p*),
P_F^c = product_(p in F)(I - U_p U_p*).
```

Their finite Möbius expansions are
`sum_(d | product(F)) mobius(d) V_d V_d*` and its Haar counterpart.
As `F` increases to all primes, `P_F^d` converges strongly to the rank-one
projection onto `C e_1`, whereas `P_F^c` converges strongly to zero.

**Proof.** The first acts diagonally by `1_[no p in F divides n]`. This
indicator converges to `1_[n=1]`, and dominated convergence for the summable
sequence `|a_n|²` proves strong convergence. The second is multiplication by
`1_(E_F)`, where `E_F` decreases to the Haar-null unit set. Dominated
convergence for `|f|²` proves its strong limit. Finite commutation follows from
double commutativity; expansion is ordinary finite inclusion-exclusion. QED.

Neither limit is operator-norm convergence: every finite `P_F^c` is a nonzero
projection of norm one, and `P_F^d - |e_1><e_1|` has norm one because a prime
outside `F` survives. This is the exact topology that must not be changed.

## 2. The sharp prime-subset threshold

For any subset `S` of the primes, let `M_S` be the positive integers with all
prime factors in `S`, and let `C_S` be the positive integers divisible by no
prime in `S`. Let `E_S = intersection_(p in S)(Zhat \ p Zhat)` and
`alpha_S = mu(E_S) = product_(p in S)(1-1/p)`.

**AH3 (necessary and sufficient interface criterion).** The following are
equivalent, including `S=empty`:

1. `sum_(p in S) 1/p < infinity`.
2. `alpha_S > 0`.
3. There exists a nonzero bounded intertwiner `T:H_d -> H_c` preserving
   `V_p,U_p` and their adjoints for every `p in S`.
4. The restricted tuples `(V_p)_(p in S)` and `(U_p)_(p in S)` are unitarily
   equivalent.

If the sum diverges, every bounded intertwiner in either direction is zero.

**Proof.** The inequalities
`1/p <= -log(1-1/p) <= 2/p` prove `(1) iff (2)`. The common atomic wandering
space is `W_d = closure(span{e_m:m in C_S})`; the Haar common wandering
space is `W_c=L²(E_S,mu)` extended by zero. If `alpha_S=0`, an intertwiner
annihilates every `e_m` for `m in C_S`, since each is killed by every
selected adjoint. Every positive integer has a unique factorization
`n=km` with `k in M_S,m in C_S`. The forward identities and boundedness
give `T=0`, proving `(3) implies (2)`.

Suppose `alpha_S>0`. The subsets `k E_S`, `k in M_S`, are pairwise disjoint:
they have different selected-prime valuation vectors. They have masses
`alpha_S/k`, and

```
sum_(k in M_S) mu(k E_S)
  = alpha_S sum_(k in M_S) 1/k
  = alpha_S product_(p in S)(1-1/p)^(-1) = 1.
```

The countable Euler identity follows by monotone limits of the finite
geometric products; the reciprocal is finite here. The shells therefore
cover Haar-almost every point, and scaling gives orthogonal decompositions

```
H_d = direct_sum_(k in M_S) V_k W_d,
H_c = direct_sum_(k in M_S) U_k W_c.
```

The complement of `S` is infinite, since the sum over all primes diverges.
Thus `C_S` is countably infinite. The Haar space `W_c` is separable and
infinite dimensional: unselected prime coordinates remain independent Haar
coordinates on the positive-measure set `E_S`. Both wandering spaces have
Hilbert dimension `aleph_0`. Choose any unitary `B:W_d -> W_c`. Define
`T(V_k w)=U_k B w` on the orthogonal sum. This is unitary and preserves
both the shifts and their adjoints; the action on the shell index is
respectively multiplication and partial division by the selected prime.
Thus `(2) implies (4)`, while `(4) implies (3)` is immediate. QED.

The proof gives **all** bounded such intertwiners when `alpha_S>0`:
they are `I_(ell²(M_S)) tensor B` in the displayed decompositions, for
arbitrary bounded `B:W_d -> W_c`, with norm `||B||`. Indeed an intertwiner
must restrict to such a `B` on the common kernel and is determined on
every shifted summand by its forward identities.

In particular every finite prime set admits a unitary equivalence, even
though the all-prime tuples are disjoint. For a single multiplicity-one
orbit, the normalized vacuum is `alpha_F^(-1/2) 1_(E_F)`; its shifted
vectors have disjoint valuation-shell supports. Finite-prime success alone
cannot certify an all-prime transport.

**AH4 (countable Wold counterexample).** A countable doubly commuting family
of individually pure isometries need not be generated by its joint
wandering space. The family `(U_p)` is a counterexample.

**Proof.** For each fixed `p`, the range of `U_p^r` is `L²(p^r Zhat)`.
The intersection of these supports has measure `lim_r p^(-r)=0`, so
`intersection_r range(U_p^r)={0}`: each isometry is pure. Double
commutativity was proved above. The joint wandering space is zero by AH1,
whereas `H_c` is nonzero. QED.

This is a quantifier warning, not a refutation of finite-tuple Wold theory.

## 3. A precise distributional replacement

Let `D=D(Zhat)` be the complex locally constant functions, equipped with
the locally convex inductive limit topology over the finite-dimensional
cylinder spaces `D_(r!)`. This is the Schwartz–Bruhat test space on the
compact totally disconnected group. Let `D'` denote its continuous linear
dual, with bilinear distribution pairing `<eta,phi>`. Both `U_p` and
`U_p*` preserve `D` continuously: a period-`m` cylinder is taken to a
period-`pm` cylinder by the cutoff-division action and to a period-`m`
cylinder by multiplication pullback.

Extend the operators to distributions by the **opposite test adjoint**:

```
<U_p^dist eta, phi> = <eta, U_p* phi>,
<A_p^dist eta, phi> = <eta, U_p phi>.
```

These agree with `U_p` and `U_p*` on distributions given by `L²` densities
against Haar. The symbol `A_p^dist` denotes the transposed test operator;
no Hilbert adjoint on `D'` is being asserted. On point masses,

```
U_p^dist delta_x = p^(-1/2) delta_(px),
A_p^dist delta_x = sqrt(p) delta_(x/p) if x in p Zhat, else 0.
```

**AH5 (classification of algebraic distributional intertwiners).** Linear
maps `J:c_00(N_{>=1}) -> D'` satisfying for every prime `p`
`J V_p = U_p^dist J` and `J V_p* = A_p^dist J` are in bijection with
distributions `eta` supported on `Zhat^times`. The correspondence is

```
J_eta e_n = n^(-1/2) (m_n)_* eta,      eta=J_eta e_1,
<(m_n)_* eta,phi> = <eta,phi(n .)>.
```

Every nonzero such `eta` yields an injective map on `c_00`.

**Proof.** The forward identities force the formula from the value at
`e_1`. The adjoint identities at `e_1` force `A_p^dist eta=0` for every
prime. Since `U_p D` is exactly the test functions supported in `p Zhat`,
this means `eta` vanishes on all such functions. A locally constant test
supported away from `Zhat^times` has compact support covered by finitely
many `p Zhat`. A finite clopen partition subordinate to that cover shows
that `eta` vanishes on the test. This is precisely support in the units.

Conversely a unit-supported `eta` is killed by every `A_p^dist`. If `p`
divides `n`, applying the formulas gives
`A_p^dist J_eta e_n = (n/p)^(-1/2)(m_(n/p))_* eta`.
If `p` does not divide `n`, the support `n Zhat^times` misses `p Zhat`,
so the result is zero. This proves both intertwining identities.
Finally the compact sets `n Zhat^times` for distinct positive integers
are disjoint and any finite collection can be separated by clopen
valuation cylinders. Multiplying a finite linear relation of their
distributions by these indicators isolates each term. The pushforward
by `m_n` is injective, since locally constant functions on `n Zhat`
pull back to all of `D`. Thus a nonzero `eta` gives linear independence.
QED.

Taking `eta=delta_1` gives the canonical exact repair
`J e_n=n^(-1/2)delta_n`. It preserves the stated operator algebra and
test pairings, **not** a Hilbert inner product, Haar absolute continuity,
or an identification with the completed signed Weil distribution.

**AH6 (extension domain and its sharp unweighted obstruction).** Define
`X={a: sum_n |a_n|/sqrt(n)<infinity}` with that weighted `ell¹` norm.
Then `J a=sum_n a_n/sqrt(n) delta_n` defines a finite complex measure,
isometrically in total variation, and embeds `X` into `D'`. Both shifts
preserve `X`, with norms `p^(-1/2)` and at most `sqrt(p)` respectively.
For every `s>0`, it also gives a continuous injection

```
ell²(N,n^s) -> finite measures -> D',
||J a||_TV <= sqrt(sum_n n^(-1-s)) ||a||_(ell²(n^s)).
```

There is no continuous extension of the canonical `J` from unweighted
`ell²` to `D'` even with the weak dual topology.

**Proof.** Absolute convergence and distinct point masses give exactly the
stated total-variation norm. Index substitution gives the shift bounds;
Cauchy–Schwarz gives the weighted Hilbert bound. For the obstruction,
evaluation at the test `phi=1` would be a continuous functional on
`ell²` extending `a -> sum a_n/sqrt(n)`. Its restriction to the first
`N` coordinates has norm squared `sum_(n<=N)1/n`, which diverges. QED.

For clarity, `ell²(n^s)` is invariant under both original shifts:
their operator norms there are `p^(s/2)` and at most `p^(-s/2)`.
The two original shift operators are not mutual Hilbert adjoints under
that changed weighted inner product. This is a domain repair, not a
hidden unitary equivalence. No globally weakest topology among all
possible interfaces is claimed; AH5 classifies the specified algebraic
interface, and AH6 supplies explicit continuous domains.

**AH7 (the canonical unweighted graph is not closable).** Regard the canonical
`J` as an operator from the dense domain `c_00` in `ell²` to `D'` with its
weak dual topology. Its graph closure is not a graph. This rules out even a
closed extension in those topologies, a stronger conclusion than AH6.

**Proof (principal derivation; independently checked in the hostile review).**
Put `H_N=sum_(n<=N)1/n` and
`a^(N)=H_N^(-1) sum_(n<=N)n^(-1/2)e_n`. Then
`||a^(N)||²=1/H_N -> 0`, whereas
`J a^(N)=H_N^(-1) sum_(n<=N)n^(-1)delta_n`.
For a residue `r mod m` let `A_r(k)` count its representatives in `[1,k]`.
The exact discrepancy satisfies `|A_r(k)-k/m|<=1`. Summation by parts gives

```
sum_(n<=N, n=r mod m) 1/n - H_N/m
 = (A_r(N)-N/m)/N
   + sum_(k=1..N-1)(A_r(k)-k/m)(1/k-1/(k+1)).
```

Its absolute value is at most `1/N + 1 - 1/N = 1`. Therefore each normalized
residue mass differs from `1/m` by at most `1/H_N`. Every test in `D` is a
finite linear combination of residue indicators; hence `J a^(N)` converges
weakly to additive Haar measure, which is nonzero. The graph closure contains
both `(0,0)` and `(0,Haar)`, so cannot be an operator graph. QED.

This uses classical harmonic equidistribution and graph topology; independent
academic novelty is not asserted. It does not contradict the continuous
weighted domains in AH6. Exact cylinder discrepancies and source norm squares
are retained by `harmonic_graph_witness` and its regression test.

## 4. Prior art and novelty boundary

- M. Slocinski, *On the Wold-type decomposition of a pair of commuting
  isometries*, Ann. Polon. Math. 37 (1980), 255–262,
  [publisher, DOI 10.4064/ap-37-3-255-262](https://www.impan.pl/en/publishing-house/journals-and-series/annales-polonici-mathematici/all/37/3/102951/on-the-wold-type-decomposition-of-a-pair-of-commuting-isometries).
  This is classical provenance for doubly commuting Wold decompositions.
- J. Sarkar, *Wold decomposition for doubly commuting isometries*, Linear
  Algebra Appl. 445 (2014), 289–301,
  [arXiv:1304.7454v2](https://arxiv.org/abs/1304.7454v2),
  [author PDF](https://www.isibang.ac.in/~jay/papers/wold_n_var.pdf).
  Corollary 3.2 and Theorem 3.3 give the finite-tuple wandering-space
  structure used for comparison. Their finite quantifier is essential.
  The final remark on printed page 9 suggests extension to arbitrary
  families; a literal extension of Corollary 3.2 is contradicted by AH4.
  This observation concerns that reading of the remark, and does not
  question the finite-tuple theorem.
- J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase
  transitions with spontaneous symmetry breaking in number theory*,
  Selecta Math. 1 (1995), 411–457,
  [IHES preprint](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf),
  [DOI 10.1007/BF01589495](https://doi.org/10.1007/BF01589495).
  This is adjacent arithmetic semigroup representation literature, not
  evidence that the exact intertwiner theorem has already appeared.
- H. Dan and K. Guo, *Dilation theory and analytic model theory for doubly
  commuting sequences of C_.0-contractions*,
  [arXiv:1907.05815v2, 20 April 2020](https://arxiv.org/abs/1907.05815v2),
  [paper](https://arxiv.org/pdf/1907.05815v2).
  Definition 1.1 distinguishes the extra Beurling-type generation condition;
  Corollary 1.4 characterizes it. Proposition 3.4 and Remark 3.5 give pure
  doubly commuting sequences with zero joint defect. Theorem 3.2 supplies
  an even stronger example with zero defect after every coordinatewise
  disk-automorphism transformation. Thus the broad AH4 phenomenon is
  **already known**; our arithmetic construction is a calibration example.
- C. H. Namitha, S. Veerabathiran and S. Sundar, *Doubly Commuting
  Semigroups of Isometries*,
  [arXiv:2509.00409v1 (2025), Section 4](https://arxiv.org/html/2509.00409v1).
  Proposition 4.7 and Remark 4.8 treat infinite-family failures using diffuse
  direct integrals. Their failure of a decomposition into joint pure/unitary
  parts is distinct from AH4, whose tuple is already individually pure.

The proofs above were derived before reading these operator-theoretic
references. They use classical Haar scaling, Euler products, wandering
subspaces and transposition of test operators. **Academic novelty is
UNVERIFIED and is not claimed.** The prime-subset dichotomy and full
distributional parameterization are project-local results with explicit
proofs, not established new literature contributions. A search located
close classical structure and known infinite-family obstructions; it did
not establish absence of exact prior art for AH3 or AH5. In particular
this dossier must not use a finite Wold theorem with an unchecked
countable quantifier.

## 5. Exact controls, claim graph and remaining work

The implementation `observational_succ/institute_atomic_haar.py` uses
`Fraction` arithmetic on genuine congruence cylinders. Its division action
increases the modulus; it does not pretend that a nonunit has an inverse
in a fixed residue ring. The tests separately enumerate residues, compare
Möbius coefficients with divisibility, check isometry/adjoint pairings,
and verify shell orthogonality.

Retained negative controls:

| Mutation | Exact witness | Verdict |
|---|---|---|
| Omit `sqrt(2)` in `U_2` | Constant one has image norm squared `1/2` | REFUTED isometry |
| Omit prime 7 from `{2,3,5,7}` | `e_7` survives the three-prime projector | REFUTED same projector |
| Use `e_n -> delta_n` | At `p=2`, constant-test forward squared pairings are `1` and `1/2` | REFUTED exact intertwining |
| Use composite 4 as a prime index | Input validation rejects it | Invalid declared family |
| Promote finite tuples to all primes | AH1 versus AH3 | REFUTED promotion |
| Promote strong convergence to norm convergence | All finite projection norms are 1 | REFUTED topology claim |
| Extend canonical `J` continuously from unweighted `ell²` | Harmonic functional norms | REFUTED extension |
| Close its unweighted graph in weak `D'` | AH7 has graph limit `(0,Haar)` | REFUTED closability |

Proof dependency graph: Haar scaling and CRT -> AH1/AH2;
Euler-product criterion and shell decomposition -> AH3;
AH1 plus fixed-prime purity -> AH4;
test-space invariance and clopen support separation -> AH5;
absolute convergence and harmonic divergence -> AH6.
Harmonic divergence and bounded residue discrepancy -> AH7.
Finite tests exercise formulas and mutations, and do not certify any
infinite claim. No source identification, nontrivial zeta zero input,
analytic continuation, or Weil positivity premise occurs in this graph.

Next discriminating work: independently audit AH3 for arbitrary sparse
prime sets and AH5 for arbitrary unit-supported distributions; inspect
the countable-family Wold literature for exact prior art; formalize the
measure-theoretic support/strong-limit steps rather than treating finite
regressions as their replacement. Run receipts live under
`research/2026-10-18/institute/haar/`.
