# Translator: the signed budget, boundary transfer, and entropy costs

**Parent:** `bf27f7ec8e757482613808bff693ba520ac13b3b` (draft #650).
**Scope:** independent first-pass derivation from the parent frontier and hole
contract; no neighboring agent report was used. Root later independently
confirmed the boundary-transfer argument and requested the weaker gate-entropy
comparison. No full suite, source holdout, commit, or publication was performed
by this agent.

**Verdict:** a new deterministic boundary-transfer lemma and sharp conditional
entropy thresholds are proved below. No lower entropy bound or positive
three-count budget has been proved for the original BBP orbit. Pi normality,
the selected carry-density theorem, and the signed budget remain open.

## 1. Exact signed observable

Keep the literal source and notation from `HOLE_CONTRACT.md`. Put

\[
\ell(j,c)=1_{\{j=2,c=1\}}+1_{\{j=3,c=2\}}
              -1_{\{j=1,c=1\}},\qquad j,c\in\mathbb Z/4\mathbb Z.
\]

Then, exactly on every finite shell,

\[
L_B=\frac1B\sum_{B\le n<2B}\ell(n\bmod4,C_n\bmod4).                 \tag{T1}
\]

**Proof.** Substitute `K=J-C mod4` into
`1_{J=K=0}+1_{K=1}-1_{J<2,K<2}`. The row `J=0` cancels identically;
the other nonzero cells are `(J,C)=(1,1),(2,1),(3,2)` with weights
`-1,+1,+1`. This is a sixteen-cell identity, not a source estimate. In
particular,

\[
\ell(j,0)=\ell(j,3)=0,\qquad
|\ell(j,c)-\ell(j,c-1)|\le1.                                     \tag{T2}
\]

The selected mask `A(c)=1_{c in {1,2}}` has the same two properties.
This matching across the `0/3` boundary is the usable extra structure.

## 2. A deterministic transfer from the carry to completed digits

This result does not assume normality, equidistribution, a density estimate,
or absence of atoms at zero in a limiting circle law.

### Theorem T3 (mask transfer with explicit error)

Let `alpha` be any real number, and suppose

\[
U_n=16^n\alpha-T_n,\qquad 0<T_n<\frac1{64n^2}\quad(n\ge1).
\]

Write

\[
Q_n=\lfloor16^n\alpha\rfloor,\quad C_n=\lfloor U_n\rfloor,
\quad D_n=Q_n\bmod16.
\]

For every integer `B>=1`, let

\[
m_B=\left\lfloor\log_{16}(64B^2)\right\rfloor,\qquad
\varepsilon_B=\frac{1+\left\lfloor(B-1)/(m_B+1)\right\rfloor}{B}.
                                                                    \tag{T3a}
\]

Define the completed-digit statistics

\[
\widetilde L_B=\frac1B\sum_{B\le n<2B}\ell(n\bmod4,D_n\bmod4),
\qquad
\widetilde d_B=\frac1B\sum_{B\le n<2B}A(D_n\bmod4).
\]

Then

\[
|L_B-\widetilde L_B|\le\varepsilon_B,\qquad
|d_B-\widetilde d_B|\le\varepsilon_B,
\qquad\varepsilon_B=O(1/\log B).                                  \tag{T3b}
\]

**Proof.** Write `x_n={16^n alpha}`. Since `T_n<1`,

\[
C_n=Q_n-b_n,\qquad b_n=1_{\{x_n<T_n\}}.
\]

Either mask can differ only if `b_n=1` and `Q_n mod4 !=0`, because
the comparison at residue zero is between the matching values at zero and
three. In particular a discrepancy at `n` has `D_n!=0` and

\[
0\le x_n<T_n<1/(64B^2).
\]

For each `1<=s<=m_B`, we have `16^s x_n<1`, including the case
`16^{m_B}=64B^2` because the preceding inequality is strict. Therefore

\[
Q_{n+s}=16^sQ_n,\qquad D_{n+s}=0.
\]

No second discrepancy can occur at any of those next `m_B` indices.
Discrepancy indices inside the shell are separated by at least `m_B+1`.
There are at most `1+floor((B-1)/(m_B+1))` such indices, each contributing
at most one to either difference. Divide by `B`.

The BBP source satisfies exactly these hypotheses with `alpha=pi/16`, by
the inherited source-tail theorem. Thus T3 applies to the authentic source.
It removes a discontinuous-floor obstruction for these two masks while
leaving the arithmetic digit-count problem intact. In particular,

\[
\liminf_B L_B=\liminf_B\widetilde L_B,
\qquad \liminf_B d_B=\liminf_B\widetilde d_B.                       \tag{T4}
\]

**Boundary mutation.** The matching hypothesis cannot be removed. At
`alpha=0`, `Q_n=0` and `C_n=-1` for all `n`; the mask `1_{c=0}` differs
at every index. No analogous all-mask transfer follows merely from
`T_n ->0`. This is why estimating every moving floor-boundary visit is
unnecessarily strong for the current signed witness.

**Next falsifier.** Check the transfer on exactly constructed long-zero
words, with a nonzero last digit just before the zero run. Those approach
the packing mechanism in the proof. A constant-zero word is the mutation
control for a mask whose endpoint values do not match.

## 3. Clocked empirical laws and the correct entropy quantifier

For `alpha in [0,1)`, `D_n` is its nth hexadecimal digit, with the terminating
expansion at rational endpoints. Integer parts do not affect the statement.
Consider the compact space

\[
X=(\mathbb Z/4\mathbb Z)\times\{0,\ldots,15\}^{\mathbb N},
\quad
S(j,(d_0,d_1,\ldots))=(j+1,(d_1,d_2,\ldots)),
\]

and the empirical measures

\[
\nu_B=\frac1B\sum_{B\le n<2B}
\delta_{(n\bmod4,(D_n,D_{n+1},\ldots))}.
\]

Every weak subsequential limit is `S`-invariant and has a uniform clock.
Invariance follows by telescoping `nu_B(f circ S-f)` to two endpoint
terms for each continuous `f`. Uniformity follows by counting clock
residues. The phase-zero conditional law is invariant under a four-digit
shift; the entropy rate used here is **per hexadecimal digit**, one fourth
of the corresponding four-digit block rate. The observable
`f(j,d)=ell(j,d mod4)` is continuous on this symbolic space and
`integral f d nu_B = tilde L_B`.

All source entropy conditions below concern **every subsequential limit
from every integer shell**. A high entropy value on one shell, a limsup
along a chosen subsequence, or a marginal histogram does not establish
this premise. No such source entropy premise is proved in this note.

## 4. Sharp pressure threshold for the signed three-count budget

For real `t`, set

\[
M(t)=\frac{(3+e^t)^2(3+e^{-t})}{64}.
\]

### Theorem T5 (elementary pressure inequality)

For every invariant clocked digit law `nu`, with entropy rate `h(nu)` in
nats per digit and `a=integral f d nu`,

\[
h(\nu)\le\log16+\tfrac14\log M(t)-ta\qquad(t\in\mathbb R).        \tag{T5}
\]

**Proof.** Let `p_j` be its one-digit distribution conditional on clock `j`.
The entropy chain rule and conditioning give
`h(nu)<=sum_j H(p_j)/4`. For any probability vector `p` and weights
`exp(t f_j(d))`, nonnegativity of relative entropy gives

\[
H(p)\le\log Z_j(t)-t\sum_dp(d)f_j(d).
\]

Here

\[
Z_0=16,\quad Z_1=4(3+e^{-t}),\quad
Z_2=Z_3=4(3+e^t).
\]

Averaging the four inequalities yields T5. No mixing, decay of
correlations, or source independence was used.

For `0<=delta<1/16`, define

\[
I(\delta)=\sup_{t\le0}
  \left(\delta t-\tfrac14\log M(t)\right)>0.
\]

If `a<=delta`, T5 yields

\[
h(\nu)\le\log16-I(\delta).                                     \tag{T6}
\]

This constant is sharp. At the optimizing `t`, choose digits independently
conditional on the clock, with each `p_j(d)` proportional to
`exp(t f_j(d))`; initialize the clock uniformly. The resulting invariant
law has `a=delta` and equality in T6. This is a valid symbolic law and,
through its radix coding, a law of completed real endpoints. It is not
a source-selected law for `alpha=pi/16`.

At `delta=0`, write `u=e^t`. The stationarity equation is

\[
\frac{2u}{3+u}-\frac1{3u+1}=0,
\quad 6u^2+u-3=0,
\quad u_0=\frac{\sqrt{73}-1}{12}.
\]

Thus

\[
I(0)=-\frac14\log\left(
\frac{(3+u_0)^2(3+u_0^{-1})}{64}\right)
\simeq0.0142817439658537.
\]

The entropy threshold is approximately **3.979395798805217 bits per
hexadecimal digit**. Applying the same proof directly to the mod4 residue
process gives the separate sufficient threshold **1.979395798805217 bits
per residue**. These entropy premises are not logically equivalent: the
high two bits may be deterministic even when the residue process has high
entropy. The full-digit premise implies the residue premise because
`h(full)<=h(residue)+2 bits`; the converse need not hold.

At `delta=1/32`, the optimizer satisfies
`45u^2-2u-27=0`, hence `u=(1+8 sqrt(19))/45`, and
`I(1/32) ~=0.00351812263520410`. The corresponding entropy threshold is
approximately **3.994924421920952 bits per hexadecimal digit**.

### Conditional source consequence

If every shell-empirical limit for the authentic completed point has

\[
h(\nu)>\log16-I(0),                                              \tag{T7}
\]

then `liminf_B L_B>0`. More generally, replacing zero by `delta` in T7
forces `liminf_B L_B>delta`.

Indeed T6 excludes any limit with `integral f<=delta`. The set of empirical
limits is compact and `nu -> integral f d nu` is continuous, so its minimum
is strictly above `delta`; T3 transfers this result to the authentic carries.
This argument does not interchange entropy limits or infer a uniform entropy
bound from finite data.

**Cost of the route.** Nearly four bits per hexadecimal digit are required
by this entropy-only proof of the signed budget. A positive entropy rate,
or even one extremely close to maximal, can coexist with zero budget.
The tilted independent law above is an exact sharp witness. It already
has many selected carries; failure of the budget is not failure of
anti-lock.

**Histogram mutation.** The periodic completed expansion
`0.overline{123456789abcdef0}` has a uniform one-digit hexadecimal
histogram, entropy rate zero, and `D_n mod4=n mod4`. Therefore
`tilde L_B -> -1/4`. Its periodic fractional parts stay away from zero,
so the same-forcing real recurrence `U_n=16^n alpha-T_n` eventually has
`C_n=Q_n` and the same budget. This changes the seed; it is a counterexample
to a seed-uniform or histogram-only inference, not to the authentic theorem.

## 5. A genuinely weaker entropy route to the selected carry event

The eight selected hexadecimal symbols are those whose residue mod4 is
one or two. Call their total probability `d`. For every invariant digit
law, clocked or unclocked,

\[
h(\nu)\le H(D_0)\le\log8+H_2(d),                               \tag{T8}
\]

where `H_2(d)=-d log d-(1-d) log(1-d)`.

**Proof.** Split a digit into its selected/unselected indicator and its
position among the eight symbols in that group. The entropy chain rule
gives `H(D_0)<=H_2(d)+log8`; entropy rate is at most one-letter entropy.
The bound is sharp for independent digits, uniform within each group,
with group probabilities `d` and `1-d`.

Consequently, if some fixed `0<epsilon<=log2` satisfies

\[
h(\nu)\ge\log8+\epsilon                                         \tag{T9}
\]

for **every** shell-empirical limit of the original completed point, then

\[
\liminf_B d_B\ge H_2^{-1}(\epsilon)>0,                            \tag{T10}
\]

where the inverse is the branch taking values in `[0,1/2]`. Compactness,
continuity of the selected cylinder, and T3 justify the passage to the
actual carries. For an eventual lower bound rather than the liminf, take
any smaller positive constant. The inherited fourth-root bridge then gives
the corresponding real-phase anti-lock margin.

This pays a different and much smaller entropy cost: **more than three
bits per hexadecimal digit**. A separate, potentially weaker criterion
works directly on the mod4 residue process `R_n=D_n mod4`:

\[
h(R)\le\log2+H_2(d).
\]

Thus a uniform margin `h(R)>=log2+epsilon` for every residue-process
shell limit also gives T10. The full-digit entropy premise implies this
residue premise, since the high two bits can add at most `log4` to the
entropy rate:

\[
h(D)\le h(R)+\log4.
\]

The reverse implication is false when the high two bits are deterministic.
For example, independent uniform digits in `{0,1,2,3}` have residue entropy
two bits and full-digit entropy two bits. Exactly three full-digit bits
are compatible with no selected digits at all:
choose independent uniform digits from
`{0,3,4,7,8,11,12,15}`. T3 ensures zero limiting selected density for the
associated same-forcing carry recurrence as well.

T9 is a strictly sufficient entropy criterion, not an equivalent version
of the target. A periodic sequence consisting of one selected digit has
selected density one and entropy rate zero. T9 is also weaker than full
normality: any biased independent digit law of entropy above three bits
with nonuniform probabilities is an explicit non-Haar example satisfying it.
No argument here derives T9 from the four BBP poles, dyadic isometry,
Gamma positivity, or the zero seed.

## 6. What an exponentially small exceptional set does and does not buy

Under **uniform random completed digits**, one four-digit clock block
has signed score

\[
Z=B_2+B_3-B_1,
\]

where the three `B_i` are independent Bernoulli variables of parameter
`1/4`. Its exponential moment is exactly `M(t)`. For `N=4m`, Chernoff's
inequality gives the entirely finite count

\[
\#\{\text{hexadecimal words of length }N:
             \text{signed average}\le\delta\}
\le16^N e^{-NI(\delta)}.                                        \tag{T11}
\]

At most three remaining clock slots change only constant boundary factors
for other lengths. This is also an elementary transfer-operator
calculation; its four-step partition function is the displayed product.
The tilted law in Section4 is the entropy-maximizing bad ensemble.

Combining T3 with T11, the set of completed endpoints for which the actual
budget has `L_B<=0` on infinitely many integer shells has Hausdorff
dimension at most

\[
1-\frac{I(0)}{2\log16}\simeq0.9974244748506521.                   \tag{T12}
\]

**Derivation of the upper bound.** A bad shell uses digit positions
`B,...,2B-1`. Digits before it are unrestricted. T3 changes its threshold
from zero to `epsilon_B=o(1)`, so the number of length-`2B-1` cylinders
needed is at most
`exp((2B-1)log16-B I(0)+o(B))`. Each cylinder has diameter
`16^{-(2B-1)}`. The sum of the s-powers of these diameters converges
whenever `2s log16>2 log16-I(0)`, which proves the claimed upper bound.
This statement concerns the fixed positive BBP tail with an arbitrary
completed real endpoint, not a varying family of tails.

This is a quantitative sparseness result, **not** an arithmetic exclusion
of the one point `pi/16`. A set of very small measure, even of dimension
strictly below one, may contain specified transcendental numbers. The
inherited finite-irrationality-exponent, zero-selected-carry controls
already rule out replacing the missing exclusion by a finite irrationality
exponent alone. Generic-seed estimates do not select seed zero.

## 7. Primary-source comparison and the missing source premise

1. **Bailey--Crandall, _On the Random Character of Fundamental Constant
   Expansions_, author-hosted version dated3 October2000.**
   <https://www.davidhbailey.com/dhbpapers/baicran.pdf>, Hypothesis A on
   page2 and equation(3) on page3 (PDF page indices1 and2).
   Their displayed pi recurrence is literally this rational forcing:
   numerator `120n^2-89n+16`, denominator
   `512n^4-1024n^3+712n^2-206n+21`, radix16, and initial point zero.
   Equidistribution is a conjectural conclusion there, not an available
   transfer-operator theorem. This application would be an instance of
   their central hypothesis, not a consequence of expansion alone.

2. **Lagarias, _On the Normality of Arithmetical Constants_,
   arXiv:math/0101055v2.** <https://arxiv.org/pdf/math/0101055>.
   Theorem3.1 formalizes the orbit relation for far more general vanishing
   perturbations; the introduction explains why that generality cannot
   imply normality. His Section5 locates split-denominator BBP series in
   the G-function setting. Section6 compares Hypothesis A with
   multiplicative measure rigidity, without asserting an implication.
   Thus the endpoint integral/Gamma representation supplies an exact
   analytic model but does not itself select a generic symbolic orbit.

3. **Rudolph, _x2 and x3 invariant measures and entropy_ (1990), primary
   journal abstract.**
   <https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/2-and-3-invariant-measures-and-entropy/64243AD8323B37089540F911F8CC77EB>.
   Positive entropy plus joint invariance and joint ergodicity under two
   relatively prime multiplication maps forces Lebesgue measure. The
   current shell limits have the radix16 invariance, but no independent
   odd multiplication invariance or entropy lower bound has been derived.
   Multiplication by2 and by16 does not supply the independent action.
   An identity that rewrites a Gamma index or the four poles is not such
   measure invariance. This theorem supplies an orthogonal possible route
   only after additional source-derived premises have been paid.

These checks use primary sources. They establish the scope of the cited
results, not an exhaustive theorem-of-nonexistence claim about all future
methods. The algebra and pressure lemmas above are derived here and do not
depend on the literature conjectures.

## 8. Claim ledger and next discriminating probe

| Claim | Status | Boundary / next lamp |
|---|---|---|
| T1 signed clock/carry identity | PROVED | Sixteen-cell algebra |
| T3--T4 transfer for matching masks | PROVED | Positive explicit tail bound; fails for generic masks |
| T5--T6 sharp pressure threshold | PROVED | Arbitrary invariant symbolic laws; source entropy unproved |
| T7 implies positive original budget | CONDITIONAL THEOREM | Requires every source shell limit to meet strict entropy threshold |
| T8--T10 weaker entropy route | CONDITIONAL THEOREM | Requires uniform entropy margin above3 bits for every limit |
| T11 cylinder-count bound | PROVED | Uniform word counting, not probability of a fixed source theorem |
| T12 exceptional-set dimension upper bound | PROVED | Arbitrary completed endpoints with the fixed source tail |
| Original source pays either entropy condition | OPEN | No estimate from exact poles and zero seed supplied |
| Original positive carry density / pi normality | OPEN | Neither follows from finite source observations |

**Concrete next probe.** Test any proposed source-conditioned entropy or
transfer argument on the period16 word `123456789abcdef0`, on the exact
tilted clock law at `u=(sqrt(73)-1)/12`, and on the eight-symbol zero-gate
law. A valid proof must identify exactly which authentic source hypothesis
excludes each relevant rival. A theorem strong enough to force only
`h>3 bits` for every empirical limit would already close the current gate
without paying the much larger signed-budget threshold. Finite block
entropies on held-out BBP shells can falsify a quantitative conjecture;
they cannot establish that all-limit entropy premise.

**Local verification performed.** An inline exact-rational check reproduced
all sixteen cells of T1, the endpoint equalities and unit difference bound,
and88 rational-endpoint/shell cases of the T3 spacing bound (eight rational
endpoints, eleven shells, with `T_n=1/(128n^2)`). The periodic-word witness
was independently counted as budget `-1/4`. Floating-point values in the
entropy table are illustrations of exact displayed formulas, not numerical
proof certificates. Two local harness mistakes were corrected before the
reported pass: row zero has difference bound zero rather than equality to
one, and hexadecimal digits must be reduced mod4 before applying `ell`.
The proofs, not these finite checks, establish the universal claims.

### Second-pass audit of the root's source receipt

After the independent first pass, this agent read `independent_audit.py` and
its completed receipt. The shell prefix indices
`p[2*B-1]-p[B-1]` correctly count `n=B,...,2B-1`. The tested range
`B=32769,...,65536` contains32768 integer shells. Its first shell is
`[32769,65537]` and its last is `[65536,131071]`, with inclusive endpoints;
the certified state at131072 is extra. All tested shell indices are beyond
the parent's old horizon32768. This is a finite range, not an eventual
quantifier.

An independently written sliding sixteen-cell recount removed the cell at
`B` and added the cells at `2B,2B+1` when advancing from shell `B` to shell
`B+1`. It shared the certified residue file but did not use the root's
prefix-sum arrays. It reproduced all three extrema and locations exactly:

| Statistic | Exact extremum | Shell start |
|---|---:|---:|
| Minimum budget | `1997/33657` |33657|
| Minimum selected density | `16393/32911` |32911|
| Maximum one-sided error | `136/33785` |33785|

Every one of these32768 shells satisfied the predeclared `1/32` defect
budget. A separate exact integer pass through all131072 supplied residues
checked the index shift for `alpha=pi/16`: completed digit3 at `n=1`,
thereafter pi-prefix character `n-2`; completed fractional phase begins
at pi-prefix character `n-1`. Each eight-hex-digit lower phase bound obeyed
`64*n*n*phase_word>=16^8`, independently confirming all reported no-borrow
decisions conditional on the supplied certified prefix. The BBP prefix
generation was not rerun and is shared provenance, not a second independent
pi computation. No indexing or quantifier defect was found in these checks.
