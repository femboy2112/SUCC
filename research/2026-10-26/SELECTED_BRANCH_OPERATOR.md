# Exact odd-conductor selection obstructs the fully conditioned Haar inverse

**Authority:** inherited CLASSICAL/PAPER results, a PAPER-PROVED quantitative
conditional-resolution obstruction, and exact finite executable witnesses.
**Source:** original four signed BBP poles, original integer lift and $U_0=0$.
**Boundary:** no selected Fourier saving and no proof of normality.

The inherited conditional branch energy is not a monotone route to stronger
cancellation as more source information is retained. On the authentic source,
conditioning on the exact future remainder determines the inverse digit and
maximizes every conditional character energy. This is an arithmetic
obstruction on the actual source, not a changed-seed counterexample.

Provenance: the lambda interface and source verifier are imported unchanged
from PR #312 head `0c306a889f425418c29cbea3193205fb80c0575e`.
The odd-denominator source property and unique odd-torsion inverse were
already proved in [Seinfeld SUCC, SS-05](../2026-10-25/SEINFELD_SUCC_NOTHING_THEOREMS.md),
and the absence of a continuous circle extension in its SS-06, at source
commit `82f4617e31e06b84fdbe52b4b217b92dcd4732dd`. These are inherited
classical results, not discoveries of this round. Section 1 supplies the
equivalent digit-congruence presentation needed by the conditional table.
The signed-cartesian firewall is imported unchanged from PR #306's source
commit `7989be5753341c5e74d570e8fea51e00129d2d0a`.
The native `FiniteMap` and `Square` are reused. No generic replacement
category, lambda interpreter, or unstated source-to-Haar coercion is added.

The new quantitative application here is Section 2: the support lower
bound $\Delta\ge16/\min(16,\lceil Q/M\rceil)-1$, its authentic all-$N$
consequence $M\ge Q_N\Rightarrow\Delta_{N,M}=15$ and $E_{N,M}(h)=1$,
and the resulting restriction on resolution schedules. The finite unitary
operator is a classical consequence of SS-05. Section 4 adds an explicit
all-sixteen-label construction near every tail; it strengthens the written
two-sequence witness in SS-06, without claiming new general discontinuity
theory or scholarly priority.

## 1. Source arithmetic makes the inverse unique

Let $D_{\rm odd}\subset\mathbb Q/\mathbb Z$ consist of rational circle
points whose reduced denominator is odd. For an odd positive integer $Q$,
write $D_Q=\{a/Q:0\le a<Q\}$, with circle addition.

The original forcing has the exact regrouping

$$
r(n)=\frac4{8n-7}-\frac1{8n-3}
      -\frac{3n-1}{(2n-1)(4n-1)}.
$$

All three displayed denominators are odd. This is an identity retaining
the original four signed poles, not a modification of the source. Therefore
$r(n)$ has odd reduced denominator. Induction from $U_0=0$ shows that every
$U_n$ and $x_n=\{U_n\}$ has odd reduced denominator. Define

$$
Q_N=\mathop{\rm lcm}_{1\le n\le N}\operatorname{den}(r(n)).
$$

Then $Q_N$ is odd and $x_n,t_n=\{16x_n\}\in D_{Q_N}$ for $n\le N$.
This is the **cumulative forcing conductor**, not necessarily the reduced
denominator of the last state.

In fact $Q_N=\mathop{\rm lcm}_{n\le N}\operatorname{den}(U_n)$: the
recurrence proves that every state denominator divides $Q_N$, while
$r(n)=U_n-16U_{n-1}$ proves the reverse divisibility of the two least
common multiples. The zero anchor has denominator one. Hence $Q_N$ is
the minimal common conductor of the actual prefix, not an artificially
enlarged carrier.

**Theorem 1 (inherited SS-05, digit-coordinate form).** For $t=a/q\in[0,1)$ reduced,
with $q$ odd, the sixteen real inverse points under $x\mapsto16x\pmod1$
are $x_j=(j+t)/16$. Exactly one belongs to $D_{\rm odd}$:

$$
\boxed{j(t)\equiv-aq^{-1}\pmod {16},\quad 0\le j(t)<16,\qquad
       S(t)=\frac{j(t)+t}{16}.}
$$

Here $q^{-1}$ is taken modulo 16. To prove the assertion, write
$x_j=(jq+a)/(16q)$. Its reduced denominator is odd exactly when
$16\mid jq+a$. Since $q$ is odd, multiplication by $q$ permutes
$\mathbb Z/16\mathbb Z$, giving exactly one solution. This proves both
existence and uniqueness. The same computation using any common odd
denominator $Q$ gives $j\equiv-aQ^{-1}\pmod {16}$ for $t=a/Q$;
reduction of the fraction is immaterial.

Thus the authentic source satisfies $j_n=j(t_n)$ and $x_n=S(t_n)$.
**No injectivity of the time map $n\mapsto t_n$ is needed or claimed.**
If two times have the same exact tail, they necessarily have the same
digit and circle state. Exact time identification would be a different,
unnecessary theorem.

The conclusion is not confined to empirical measures: for any probability
measure supported on the countable set $D_{\rm odd}$, the digit is a
measurable function of the exact tail. Its exact conditional character
mean therefore has modulus one almost surely, at every integer frequency.
This does not pass to an arbitrary weak limit on the real circle: a weak
limit of measures supported on $D_{\rm odd}$ may give that set mass zero.

## 2. An explicit all-N ceiling on conditional resolution

For any probability distribution supported on $D_Q$, partition
$t=\{16x\}$ into $M$ half-open equal bins, and let $p_b$ be the occupied
bin probabilities and $w_{bj}$ the conditional selected-digit probabilities.
The empirical source is the special case with mass $1/N$ at each time,
including multiplicity. Set

$$
\Delta=\sum_b p_b\left(16\sum_{j=0}^{15}w_{bj}^2-1\right),
\qquad E(h)=\sum_b p_b\left|\sum_jw_{bj}\zeta_{16}^{hj}\right|^2.
$$

**Theorem 2 (resolution lower bound).** Put
$s=\min(16,\lceil Q/M\rceil)$. Then

$$
\boxed{\Delta\ge\frac{16}{s}-1.}
$$

Indeed, a half-open bin of length $1/M$ contains at most
$\lceil Q/M\rceil$ points of the $1/Q$ grid. Each tail has just one
digit by Theorem 1. Therefore the digit law in that bin has support of
size at most $s$. Cauchy--Schwarz gives
$1=(\sum_jw_{bj})^2\le s\sum_jw_{bj}^2$. Multiply by $p_b$ and sum.

In particular, for the authentic source, every $N\ge1$ and every
$M\ge Q_N$ satisfy

$$
\boxed{\Delta_{N,M}=15,\qquad E_{N,M}(h)=1
       \quad\hbox{for every integer }h.}
$$

At this resolution each occupied bin contains a single distinct tail,
and hence a point-mass conditional digit law. Its Fourier coefficient
is a unit root of unity, including for the primitive characters. Repeated
tail values simply increase the bin mass. The upper bound $\Delta\le15$
and the theorem's lower bound give equality.

The code computes sparse occupied tables, so this certificate does not
allocate $Q_N$ cells. The theorem is an all-N argument from the exact
source denominator law; finite certificates check instances independently.
The threshold is sufficient, not claimed optimal. A bin may already
contain one selected digit at much lower resolution.

**Consequences for the proof gate.** Any schedule with
$\Delta_{N,M_N}\to0$ must eventually avoid every fixed positive lower
bound in Theorem 2. For example, eventually it must have
$\lceil Q_N/M_N\rceil\ge16$, hence $M_N<Q_N/15$.
This is a necessary condition only, and the conductor is large. More
importantly, the exact-tail conditional expectation cannot be the proposed
contracting operator: its primitive-character energy is identically one
on the authentic source at every horizon.

If normality were true, the inherited fixed-$M$ theorem would give
$\lim_{N\to\infty}\Delta_{N,M}=0$. Nevertheless the result just proved
gives unconditionally

$$
\lim_{N\to\infty}\lim_{M\to\infty}\Delta_{N,M}=15.
$$

Under that **explicitly conditional** normality premise the reversed
iterated limit is zero. There is no legitimate exchange of these limits
without a quantitative theorem. A slowly growing coarse partition remains
a possible proof instrument; exact conditioning is not its limit for free.

## 3. The source-compatible finite operator is unitary

Fix $N$ and use the common carrier $D_{Q_N}$ for this prefix. For every
$0\le n<N$, the authentic affine step

$$T_n(x)=16x+r(n+1)\pmod1$$

is a permutation of $D_{Q_N}$. To see this, write $x=a/Q_N$ and
$r(n+1)=b/Q_N$; then the residue map is $a\mapsto16a+b\pmod{Q_N}$.
Its inverse exists because $\gcd(16,Q_N)=1$.

**Theorem 3 (classical finite operator corollary of SS-05).** On
$\ell^2(D_{Q_N},\text{uniform})$, pullback by each $T_n$ and its inverse
are unitary. Every finite composition preserves norms, including on
the mean-zero subspace. When $Q_N>1$, no strict operator-norm contraction
on that subspace is possible.

The proof is permutation reindexing of the finite sum of squared moduli.
This does not claim an invariant probability law for the selected
trajectory; uniform counting measure is used only to define a finite
operator norm. The prefix carrier changes with $N$. No limit of these
operators is asserted in operator norm.

The Haar Perron operator on the real circle is a different, legitimate
operator: it averages sixteen real predecessors. For each rational
odd-denominator tail, fifteen of those predecessors have even denominator
and lie outside **every** $D_Q$ with $Q$ odd. The arithmetic restriction
is therefore not merely a choice of unequal weights inside an already
source-compatible sixteen-point fiber. That fiber has only one arithmetic
point. This is the precise missing source-map assumption in the attempted
promotion of Haar inverse cancellation to the selected orbit.

## 4. Why a weak or continuous limit does not repair the inverse

SS-06 already proves noncontinuity at zero and rules out a continuous
circle extension. Since the inverse is a group homomorphism, translating
that failure already implies discontinuity at every point of
$D_{\rm odd}$. We do not count that implication as a new obstruction.
The explicit refinement below realizes every one of the sixteen branch
labels near every real tail, with a rational distance budget.

The inverse $S:D_{\rm odd}\to D_{\rm odd}$ is discontinuous at every
point for the subspace topology from the real circle. More strongly, each
branch label $j\in\{0,\ldots,15\}$ occurs arbitrarily close to every
tail $t_0\in[0,1)$, with

$$S(t_k)\longrightarrow (j+t_0)/16.$$

Here is a quantitative construction. Given rational $t_0$ and rational
$\varepsilon>0$, choose

$$L\ge\max(1,\lceil1/\varepsilon\rceil,
                 \lceil1/(1-t_0)\rceil),\qquad q=16L+1.$$

Take $k=\lfloor qt_0\rfloor$ and let $a$ be the first integer at least
$k$ with $a\equiv-j\pmod {16}$. Then $k\le a\le k+15$,
$0\le a<q$, and $|a/q-t_0|<16/q<\varepsilon$. Because $q\equiv1$
modulo 16, Theorem 1 gives $j(a/q)=j$, even if the fraction reduces.
Letting $L\to\infty$ proves the assertion. The same construction for
real centers is a paper existence proof; executable witnesses use exact
rational centers. At $t_0=0$ it approaches from within $[0,1)$, so the
circle endpoint causes no exception.

This recovers the inherited SS-06 conclusion that no continuous extension
of $S$ to the circle exists. Dense
odd torsion and its inverse permutation do not supply a continuous inverse
for the sixteen-fold circle covering. Weak convergence or low-frequency
transport must pay for this discontinuous digit selector; continuity of the
forward map is not a substitute.

## 5. Typed source-map and signed base-change test

For a fixed tail, let $E_t$ be all sixteen real predecessors and let
$A_t=E_t\cap D_{\rm odd}$, a singleton. The square with top inclusion
$A_t\hookrightarrow E_t$ and both bottom objects the singleton $\{t\}$
commutes, but its comparison map into the fiber product misses fifteen
points. It is not cartesian. A signed amplitude supported on any missing
point has full-fiber pushforward one and selected-fiber pushforward zero.
This is an explicit failure of the signed Beck--Chevalley identity, using
the existing PR #306 implementation.

A family of identifications preserving **all** evaluations would in
particular preserve that missing-point indicator, so cannot identify
these two source fibers. Currying/Yoneda representability does not remove
the cardinality or evaluation mismatch. A map collapsing all sixteen
predecessors onto the selected one exists as a set map, but does not
preserve the observable evaluations. Assigning the empirical conditional
weights correctly preserves the actual measure; at full resolution those
weights are a point mass, not uniform.

The paired native donor control also retains the other failure mode:
redundant realizers can preserve all Prop-valued existential statements
and realize every formal witness, yet duplicate signed amplitudes. The
all-amplitudes signed firewall requires cartesianness; source labels or
ghost-freedom alone are insufficient. Formal phase sums remain in
$\mathbb Q[\mathbb Q/\mathbb Z]$ for those tests. Uniform character
annihilation is checked separately in the inherited $\mathbb Q(\zeta_{16})$
carrier, so no formal-to-cyclotomic equality is silently imposed.

## 6. Controls, authority, and surviving obligation

- Independent enumeration of all sixteen preimages for all odd denominators
  through 61 confirms uniqueness, including unreduced presentations.
- An independent regrouping of the original poles checks the source
  denominator law. Dropping part of the negative even pole produces an
  even denominator and fails the hypothesis.
- The synthetic state $x=1/16$ shares the tail zero with $x=0$, showing why
  the odd-denominator assumption is necessary. A repeated-tail control
  rules out an accidental assumption that times must be distinct.
- Exact source certificates use held-out horizons and enormous sparse
  bin labels; coarse tables are compared against the inherited dense code.
- Permutation pullback preserves independently chosen nonconstant rational
  vectors' squared norms. Even conductors and foreign forcing denominators
  are rejected. The source authenticator rejects changed seeds and lifts.
- Nearby-tail witnesses realize all sixteen labels around several centers
  at successively smaller rational radii. Cartesian failure is tested with
  a signed amplitude that isolates an actual missing point.

Odd inverse uniqueness and the nonextension obstruction are inherited
SS-05/SS-06 classical results. The quantitative resolution lower bound and
its all-$N$ application to the original BBP conditional gate are the
source-specific obstruction established here. The every-label nearby-tail
witness is an explicit refinement of the inherited example. Neither the
finite permutation corollary nor the native source-fiber square is claimed
as a new general operator or category theorem, or as scholarly priority.
The selected Fourier cancellation problem remains open. A route through
these conditional energies must control an admissible coarse resolution;
signed cross-bin control or a direct selected-sum estimate remain possible.
It cannot replace the selected operator
by the uniform inverse ensemble, take exact empirical conditioning as
an improved energy gate, or interchange the resolution and source-time
limits without a quantitative comparison.

## 7. Actual finite Lean authority and replay

`formal/SelectedBranch.lean` was checked by the pinned Lean 4.14.0 kernel
against mathlib `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`.
Ten exported declarations establish:

1. Odd $q$ is a unit modulo 16, and 16 is a unit modulo odd $q$.
2. Uniqueness of the inverse digit from its modular equation, and
   injectivity of the affine step on `ZMod q`.
3. Preservation of finite squared norms by a declared permutation.
4. Deterministic one-row defect 15 and its probability-mass mixture.
5. An explicit even-modulus noninjectivity counterexample.
6. The real parity-perspective estimate
   $|s^2/n-t^2/n|\le2|s-t|$ for $n>0$, $|s|,|t|\le n$.
7. Positivity of
   $448m^4+1976m^3+2904m^2+1478m+87$ for every real $m\ge0$.
   This is the scalar polynomial used in the companion critical-scale
   spill obstruction; the complete BBP comparison is not kernel formalized.

The parity estimate in item 6 is a finite scalar core for the accompanying
carry-replacement analysis; its complex and source-counting extensions
are not formalized here. The kernel file does **not** prove the BBP
denominator induction, the rational-grid resolution theorem, the
discontinuity/limit statements, or any complex normality criterion.

Replay:

```sh
python -m unittest discover -s tests -p 'test_selected_branch_operator.py' -v
python scripts/check_selected_branch_lean.py \
  --dependency-project /home/leah/SUCC-rf/formal/mathlib_bridge \
  --output research/2026-10-26/selected_branch_validation/lean
```

The exact Python run passed 14 tests in 3.361 seconds. The Lean checker
verified every dependency revision and clean tracked source, used one
compiler thread with a 2048 MB memory cap, exported all ten declaration
types and their hashes, and rejected four semantic false-claim controls
after checking their positive counterparts. The recorded axioms are only
`propext`, `Classical.choice`, and `Quot.sound`. All recorded source and
declaration hashes were rechecked after the run. The receipt is
`selected_branch_validation/lean/kernel-observation.json`.

Two initial local elaborations failed before the successful run: numeric
normalization needed a separate tactic and closed `ZMod` arithmetic needed
`decide`; then adjacent absolute-value/multiplication notation needed
spaces. These were compiler-facing proof-script errors, not mathematical
counterexamples. No failed run is labelled kernel checked. The receipt
checker rejects unapproved axioms, source mutation, missing exports, and
false controls that fail merely because of missing dependencies.
