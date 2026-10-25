# Binary carry refinement and finite prime observations

**Date:** 2026-10-24.
**Research baseline:** [twisted-observer PR #268](https://github.com/femboy2112/SUCC/pull/268),
head `06f6b03eed2521c6bd5c02db618cb421ac6b5a51`, built over coherent
`main@e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
**Authority:** elementary paper proofs and exact finite Python controls.
No Lean authority or asymptotic selected-source estimate is claimed here.

The question is whether the factorization $16=2^4=4^2$, or observations at
small odd primes, can close the gap between a proposed half-retention bound
and the sixteenth-retention bound used by the existing collision argument.
The half bound itself remains an unproved source-specific premise.

This report constructs an exact common observable: a bounded **centered
carry** that simultaneously labels a real-circle inverse branch and admits
finite prime-power readouts. Four conditional binary losses multiply exactly.
Two ternary digits suffice to identify the central branch. Separate
prime-11 and prime-13 marginals reconstruct the entire bounded carry law,
with a sharp stability constant. A cumulative logarithmic-excess criterion
also permits individual bad bits and scales.

None of these observation or algebraic facts proves that the authentic
BBP-selected source pays the required frequency bound. That arithmetic
obligation remains **OPEN**.

## 1. Exact object and implementation

The production instrument is
[pi_binary_branch.py](../../observational_succ/pi_binary_branch.py), with
[exact controls](../../tests/test_pi_binary_branch.py). Its main entry point
`binary_branch_profile` accepts exact current phases, exact forcing values,
an exact successor radius, and optionally independently supplied successor
phases. Inconsistent successors and malformed inputs are rejected.

The mathematical statements below apply to real arrays where indicated.
The implementation uses integers and `Fraction` values, and every threshold,
carry and residue decision is exact. Its pair enumeration is quadratic in
the sample size. It is a finite diagnostic oracle, not an efficient algorithm
for arbitrarily large windows.

The inherited arithmetic application uses the authentic recurrence

$$
y_0=0,
\qquad
y_n=\{16y_{n-1}+r(n)\},
$$

where

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}
-\frac1{8n-3}-\frac1{8n-2}.
$$

For a good prime $p=8m+1$, the overlapping windows are
$W=\{m+1,\ldots,4m-1\}$ and $W^+=W+1$, of length $n=3m-1$.
The full selected window has length $N=3m$.
The source, windows, initial zero and later carries are retained throughout.

## 2. A bounded integer between the circle and finite places

Define the centered representative

$$
\langle x\rangle=x-\left\lfloor x+\frac12\right\rfloor
\in[-1/2,1/2).
$$

The endpoint convention is part of the definition. In particular,
$\langle1/2\rangle=-1/2$.

### Theorem 1: bounded carry and central-branch identification — PROVED

Let $b=2^a$ with $a\ge1$. Let a nonempty finite array obey

$$
y_s=\{b x_s+f_s\}.
$$

Write $\epsilon=\max_s f_s-\min_s f_s$, and choose

$$
0\le\tau\le1/4,
\qquad \epsilon+\tau<1/2.
$$

For an ordered pair with $|\langle y_t-y_s\rangle|\le\tau$, put

$$
\delta=\langle x_t-x_s\rangle,
\quad e=f_t-f_s,
\quad\delta'=\langle y_t-y_s\rangle,
\quad\kappa=b\delta+e-\delta'.
$$

Then

$$
\kappa\in\mathbb Z,
\qquad |\kappa|\le b/2,
$$

and

$$
|\delta|\le\frac1{2b}
\quad\Longleftrightarrow\quad
\kappa=0.
$$

**Proof.** Each fractional-part or centered reduction subtracts an integer,
so the recurrence makes $b\delta+e-\delta'$ integral. Moreover,

$$
|\kappa|\le b/2+\epsilon+\tau<b/2+1/2.
$$

Since $b/2$ is integral, $|\kappa|\le b/2$. If
$|\delta|\le1/(2b)$, then
$|\kappa|\le1/2+\epsilon+\tau<1$, hence $\kappa=0$.
Conversely, $\kappa=0$ implies

$$
|\delta|=\frac{|\delta'-e|}{b}
\le\frac{\tau+\epsilon}{b}<\frac1{2b}.
$$

This proves both directions. The equality threshold is retained by the
implementation; the strict forcing/radius hypothesis makes the conclusion
unambiguous. $\square$

At radix $16$, the bounded support is exactly the allowed range
$\{-8,\ldots,8\}$. The theorem identifies the central inverse branch with
the event $\kappa=0$. This is a centered carry; equality of the two literal
source carries is a different condition.

### Theorem 2: the authentic 2-adic readout — PROVED

The authentic forcing admits the regrouping

$$
r(n)=\frac4{8n-7}-\frac1{8n-3}
-\frac{3n-1}{(2n-1)(4n-1)}.
$$

Every displayed denominator is odd for integral $n$. Starting from $y_0=0$,
the forced recurrence therefore preserves rational phases with odd reduced
denominator. The corresponding differences $\delta,e,\delta'$ belong to
$\mathbb Z_2$, and

$$
\boxed{\kappa\equiv e-\delta'\pmod {16}.}
$$

**Proof.** Combine the two even-denominator terms in the original formula:

$$
-\frac2{8n-4}-\frac1{8n-2}
=-\frac{3n-1}{(2n-1)(4n-1)}.
$$

Addition, multiplication by $16$, and subtraction of an integer preserve
odd reduced denominators. A centered representative also subtracts an
integer. The occurrence of $1/2$ inside the floor in its definition does
**not** mean that a literal half is added to the retained rational phase.
Thus centering preserves the same 2-adic domain. Reducing
$\kappa=16\delta+e-\delta'$ modulo $16$ proves the claim. $\square$

This is an exact operational connection between a real-circle branch label
and a finite 2-adic residue. It includes the choice of real centered lift.
It is not a continuous identification of the real and 2-adic topologies.
At an odd prime, multiplication by $16$ is a unit, so the current-difference
term does not disappear from the corresponding residue equation.

## 3. The four binary refinements

### Theorem 3: conditional factorization — PROVED

Under Theorem 1, let $E_0$ be the successor-close ordered pairs. Define

$$
E_j=\{(s,t)\in E_0:2^j\mid\kappa_{s,t}\},
\qquad S_j=|E_j|,
\qquad 0\le j\le a.
$$

Then $E_a$ is exactly the central branch. Every $E_j$ contains all self-pairs,
so its count is positive. Consequently,

$$
\frac{S_a}{S_0}
=\prod_{j=1}^{a}\frac{S_j}{S_{j-1}}.
$$

**Proof.** The sets are nested. Since $|\kappa|\le b/2<b$, the only possible
multiple of $b=2^a$ in the support is zero. Theorem 1 identifies this terminal
fiber with the central branch. Every self-pair has $\delta=e=\delta'=0$,
hence $\kappa=0$. The displayed product then telescopes. $\square$

The binary observations are low bits of the **same** centered carry, with
each later count restricted by the earlier retained bits. They are not four
independently collected digit histograms.

### Corollary 3.1: four conditional halves — PROVED_CONDITIONAL

At radix $16$, suppose

$$
S_j\le\frac12S_{j-1}+Cn,
\qquad j=1,2,3,4,
$$

for a common $C\ge0$. Then

$$
\boxed{S_4\le\frac1{16}S_0+\frac{15}{8}Cn.}
$$

Indeed, repeated substitution gives the coefficient $2^{-4}$ and the
allowance $Cn(1+1/2+1/4+1/8)$. More generally, assumptions
$S_j\le\theta_jS_{j-1}+C_jn$, with $0\le\theta_j\le1$, give

$$
S_a\le
\left(\prod_{j=1}^{a}\theta_j\right)S_0
+n\sum_{j=1}^{a}C_j\prod_{\ell=j+1}^{a}\theta_\ell.
$$

The algebraic implication is proved. These inequalities have not been
established uniformly for the authentic BBP-selected pair sets.

### Why four marginal halves do not suffice

Give the two binary words $0000$ and $1111$ equal probability. Each individual
bit is fair, but all four zero events coincide: their intersection has mass
$1/2$, not $1/16$. This is an exact counterexample to multiplying four
marginal half probabilities. It is a logical calibration control, not a
claim that the actual BBP carry law has this distribution.

### What $16=4^2$ does and does not supply

The same refinement groups as

$$
\frac{S_4}{S_0}
=\frac{S_2}{S_0}\frac{S_4}{S_2}.
$$

Two conditional quarter losses give $1/16$. Two conditional half losses
give $1/4$.

Both behaviors have exact finite odd-denominator controls. With zero forcing,
take $x_j=16j/257$.

| Index set | Successor radius | Nested counts $(S_0,\ldots,S_4)$ | Total retention |
|---|---|---|---|
| $j=0,\ldots,15$ | $15/257$ | $(256,128,64,32,16)$ | $1/16$ |
| $j\in\{0,1,4,5\}$ | $5/257$ | $(16,8,8,4,4)$ | $1/4$ |

The second row has grouped quaternary retentions $1/2$ and $1/2$.
The first row has four exact conditional binary halves. These controls test
the readout and its interpretation; they do not replace the selected BBP
source or its initial condition.

## 4. How much base-3 information is enough?

### Theorem 4: finite modular identification — PROVED

For any integer $\kappa$ with $|\kappa|\le8$ and any integer modulus $q>8$,

$$
\kappa=0\quad\Longleftrightarrow\quad\kappa\equiv0\pmod q.
$$

A modulus $q>16$ identifies the entire integer in $[-8,8]$.

**Proof.** The only multiple of $q>8$ inside $[-8,8]$ is zero. For full
identification, two distinct integers in the interval differ by at most
$16$, so their difference cannot be a nonzero multiple of $q>16$.
$\square$

The resulting finite observation contracts are:

| Readout | Zero carry identified? | Entire signed carry identified? |
|---|---|---|
| Modulo $3$ | No: $\pm3,\pm6$ also map to zero | No |
| Modulo $9=3^2$ | Yes | No |
| Modulo $27=3^3$ | Yes | Yes |
| Joint modulo $3$ and modulo $5$ | Yes, by the combined modulus $15$ | Not in general |
| Modulo $11$ | Yes | No |
| Modulo $13$ | Yes | No |
| Separate modulo $11$ and modulo $13$ marginals | Yes | The full law is recoverable by Theorem 5 |

Thus two ternary digits suffice to **identify** the branch whose frequency
must be bounded. This gives a precise finite version of the base-3 intuition.
It does not provide that frequency bound. Uniformity modulo $9$ would give
zero mass $1/9$, which is larger than $1/16$.

Nor can one demand uniformity in every odd residue ring. For example, uniform
modulo-$11$ and modulo-$13$ marginals would require the same singleton zero
fiber to have masses $1/11$ and $1/13$ simultaneously. Those requirements
are inconsistent.

### Joint modulo 3 and 5 versus their separate marginals

The joint residue pair identifies the zero fiber, but its separate marginals
need not. Consider the signed perturbation

$$
v_0=1,\qquad v_3=-1,\qquad v_5=-1,\qquad v_8=1,
$$

with all other entries zero. Its total mass is zero. Modulo $3$, the terms
at $0,3$ cancel and the terms at $5,8$ cancel. Modulo $5$, the terms at
$0,5$ cancel and the terms at $3,8$ cancel. Thus both separate residue
marginals vanish, despite $v_0\ne0$.

Adding $v/17$ to the uniform law on $\{-8,\ldots,8\}$ gives a second
nonnegative probability law. The two laws have identical separate modulo-3
and modulo-5 marginals, while their zero masses are $1/17$ and $2/17$.
This exact countermodel prevents a marginal observation from silently
replacing a joint one.

## 5. Two small-prime marginals reconstruct the entire law

### Theorem 5: separate 11/13 tomography — PROVED

Let $c_k\ge0$ be any finite measure supported on $-8\le k\le8$.
Define its separate residue marginals

$$
a_r=\sum_{k\equiv r\ (11)}c_k,
\qquad
b_r=\sum_{k\equiv r\ (13)}c_k.
$$

These marginals determine the full measure. The reconstruction is

$$
c_k=b_{k\bmod13},\qquad -4\le k\le4,
$$

followed by

$$
\begin{aligned}
c_{-8}&=a_3-c_3,&c_{-7}&=a_4-c_4,\\
c_7&=a_7-c_{-4},&c_8&=a_8-c_{-3},\\
c_5&=b_5-c_{-8},&c_6&=b_6-c_{-7},\\
c_{-6}&=b_7-c_7,&c_{-5}&=b_8-c_8.
\end{aligned}
$$

**Proof.** Each residue represented by $k\in[-4,4]$ modulo $13$ has only
that representative in the permitted support. The first line therefore
recovers these nine entries. The remaining identities list the two permitted
representatives in the relevant residue fibers. For instance,
$a_3=c_{-8}+c_3$ and $b_5=c_{-8}+c_5$. Substituting the already recovered
entries gives every remaining coefficient. $\square$

This is more than a generic Chinese remainder statement: the observations
are separate marginals, and the support restriction makes them sufficient.
The preceding modulo-3/modulo-5 counterexample shows why this feature requires
a proof.

### Theorem 6: sharp stability constant — PROVED

For two such measures, suppose their respective marginal differences have
sup-norm bounds $\epsilon_{11}$ and $\epsilon_{13}$. Then

$$
\|\Delta c\|_\infty
\le\epsilon_{11}+2\epsilon_{13}
\le3\max\{\epsilon_{11},\epsilon_{13}\}.
$$

The constant $3$ in the final bound is sharp, even among symmetric probability
laws.

**Proof of the bound.** The nine singleton entries have error at most
$\epsilon_{13}$. The next four entries have error at most
$\epsilon_{11}+\epsilon_{13}$. The last four have error at most
$\epsilon_{11}+2\epsilon_{13}$. These are direct applications of the
reconstruction identities and the triangle inequality.

**Sharpness witness.** Define the symmetric integer array

$$
\begin{array}{c|rrrrrrr}
|k|&1&3&4&5&6&7&8\\ \hline
v_k&-1&1&-1&3&-2&2&-2
\end{array}
$$

and $v_0=v_{-2}=v_2=0$. Its total is zero, its sup norm is $3$, and direct
residue summation gives sup norm $1$ for each of its modulo-11 and modulo-13
marginals. Let $c_k=1/17$ and $\widetilde c_k=c_k+v_k/34$. Since
$v_k\ge-2$, both are nonnegative probability laws. Their full sup difference
is $3/34$ while the larger marginal sup difference is $1/34$. This realizes
the ratio $3$. $\square$

The implementation checks that reconstructed entries are nonnegative and
that both observed marginals are recovered. Inconsistent marginals are
rejected rather than interpreted as an approximate probability law.

### The relevant reference law

For an unforced Haar-distributed centered circle difference $\delta$, condition
on $|\langle16\delta\rangle|\le\tau$, where $0<\tau<1/4$.
Every interior signed carry $-7,\ldots,7$ has mass $1/16$; each endpoint
carry $\pm8$ has mass $1/32$. Indeed, the interior inverse intervals each
have length $2\tau/16$, the two endpoint pieces have length $\tau/16$, and
the conditioning event has total length $2\tau$.

Modulo $16$, the endpoint pieces join to form the remaining branch of mass
$1/16$. Its projections to odd moduli are generally nonuniform; in particular,
the zero mass modulo $9$, $11$ and $13$ is $1/16$ in each case.

This unforced reference law is an exact calibration model. A source with
pair-dependent forcing needs its own distributional proof and endpoint
accounting. The signed endpoint split is not silently transferred to such
a source.

## 6. A cumulative target that allows bad bits and scales

This section uses the proved inverse-branch inclusion and endpoint estimate
from [the pinned #268 report](https://github.com/femboy2112/SUCC/blob/06f6b03eed2521c6bd5c02db618cb421ac6b5a51/research/2026-10-24/PI_TWISTED_OBSERVER_AGREEMENT.md#111-an-exact-inverse-branch-step-toward-a-first-arithmetic-saving).

At the prescribed refinement scales, write

$$
Q_j=Q_W(\tau_j),
\qquad
\theta_j=\frac{Z_W(\tau_j)}{Q_{W^+}(\tau_j)},
$$

where

$$
\tau_0=\frac14,
\qquad
\tau_{j+1}=\frac{\tau_j-\epsilon_p}{16},
\qquad
\epsilon_p=r(m+2)-r(4m).
$$

The retained diagonal makes $0<\theta_j\le1$. The inherited theorems give

$$
Q_{j+1}\le Z_W(\tau_j)
\le\theta_j(Q_j+2n).
$$

### Theorem 7: aggregate retention implication — PROVED_CONDITIONAL

For any admissible number $J$ of refinement steps,

$$
\begin{aligned}
Q_J
&\le n^2\prod_{j=0}^{J-1}\theta_j
+2n\sum_{k=0}^{J-1}\prod_{j=k}^{J-1}\theta_j\\
&\le n^2\prod_{j=0}^{J-1}\theta_j+2nJ.
\end{aligned}
$$

**Proof.** Iterate the preceding inequality, using $Q_0\le n^2$. Every
inhomogeneous endpoint contribution receives the product of the retention
factors from its own step through the final step. Since each factor is at
most one, the sum of those products is at most $J$. $\square$

Let

$$
d=\left\lfloor\frac25\log_{16}p\right\rfloor,
\quad M=16^d,
\quad J=d-1.
$$

For sufficiently large good primes, the inherited source bound ensures that
all these scales are admissible and $\tau_J\ge1/M$. Restoring the last
sample costs at most $2N-1$ ordered pairs. Therefore

$$
K_p(1)=\frac{M}{N^2}Q_{\mathrm{full}}(1/M)
\le
M\prod_{j<J}\theta_j+O\!\left(\frac{M(J+1)}{N}\right).
$$

It follows that the existing subpower collision contract is satisfied if

$$
\boxed{\prod_{j<J}\theta_j\le16^{-J}p^{o(1)}.}
$$

Indeed, $16^J=M/16$, and $M(J+1)/N=O(p^{-3/5}\log p)$. Hence the resulting
bound is $K_p(1)=p^{o(1)}$.

At scale $j$, denote the four conditional binary ratios of Theorem 3 by
$\rho_{j,\ell}$, for $1\le\ell\le4$. Since
$\theta_j=\prod_\ell\rho_{j,\ell}$, define the total logarithmic excess

$$
\mathcal E_p=
\sum_{j<J}\sum_{\ell=1}^{4}\log(2\rho_{j,\ell})
=\log\left(16^J\prod_{j<J}\theta_j\right).
$$

A sufficient form is

$$
\mathcal E_p\le a_p\log p,
\qquad a_p\ge0,\quad a_p\longrightarrow0.
$$

An upper bound $\mathcal E_p\le C\log\log p$ would give a polylogarithmic
collision bound. The individual conditional ratios may exceed $1/2$, and
individual scale retentions may exceed $1/16$. What matters for this contract
is their cumulative logarithmic excess.

This improves the formulation of the sufficient premise. It supplies no
unconditional bound on $\mathcal E_p$ for the authentic selected source.

### A strict boundary: an isometric source can retain every real pair

The following countermodel CHANGES the fixed BBP four-pole forcing. It
proves that the source's newly established dyadic properties, even together
with positive quadratic real forcing decay and initial zero, cannot by
themselves establish a real half-retention bound.

Write P_n(t)=t(t-1)...(t-n+1), and construct

$$
H(t)=a_1t+\sum_{n\ge2}a_nP_n(t),
\qquad a_1\in\mathbb Z_{(2)}^\times,\quad
a_n\in2^n\mathbb Z_{(2)}.
$$

Here Z_(2) is the rational ring with odd reduced denominator. Choose the
coefficients inductively so that, at each positive integer n,

$$
H(n)=16^n-\eta_n,\qquad
\frac1{2(n+1)^2}<\eta_n<\frac1{(n+1)^2}.
$$

This is possible because P_n(n)=n!, later terms vanish at earlier integer
arguments, and the allowed rational coefficient cosets are dense in the
real line. For completeness, rationals whose denominators are odd and whose
numerators lie in any fixed class modulo 2^k are real-dense: choose increasing
odd denominators and approximate the target numerator within 2^k. Scaling
by the nonzero integer n! preserves density. At n=1 the unit condition is
handled in the same way. Concrete first choices are a_1=79/5 and
a_2=2804/25, giving eta_1=1/5 and eta_2=2/25.

For every 1<R<2, on the 2-adic disk |t|_2<=R,

$$
|a_nP_n(t)|_2\le(R/2)^n.
$$

The series is therefore one analytic function on the open radius-2 disk.
Its difference quotient on Z_2 is a_1 plus a multiple of 4, hence a unit.
Thus H is a bijective isometry and H(0)=0. Set

$$
s(t)=H(t)-16H(t-1).
$$

Its difference quotient is also a unit. Moreover,

$$
\sum_{j=0}^{J}16^j s(t-j)
=H(t)-16^{J+1}H(t-J-1)\longrightarrow H(t)
$$

uniformly for t in Z_2. This preserves the contracting particular-solution
identity and its exact initial zero.

At positive integer times all values are rational. We have s(1)>0 and,
for n>=2,

$$
s(n)=16\eta_{n-1}-\eta_n,\qquad
0<\frac8{n^2}-\frac1{(n+1)^2}<s(n)<\frac{16}{n^2}.
$$

Nevertheless, the zero-initial real source has fractional states
z_n=1-eta_n. Its cumulative carry is 16^n-1 and its literal local carry is
constantly 15. On late windows with indices comparable to p, every real
pair distance is O(p^-2). All pairs are therefore successor-close and
central at every prescribed radius down to p^(-2/5):

$$
Z_W(\tau_j)=Q_{W^+}(\tau_j)=n^2,\qquad \theta_j=1.
$$

For any fixed C, half retention with allowance Cn fails when n>2C.
The exact dyadic residue collision refinements still hold, since H remains
an isometry.

This countermodel locates the missing BBP-specific dependency: the fixed
four-pole source and its actual carry history must prevent e and delta'
from agreeing modulo 16 too often CONDITIONED on real successor closeness.
Marginal residue balance does not control this joint conditional alignment.
In the countermodel the alignment is complete and kappa=e-delta' modulo 16
is always zero on the late close-pair sample.

## 7. Verification and failure products

The focused test module contains 18 tests. The final focused run completed
successfully with all 18 tests passing; exact runtime and the complete
integration gates belong in the round's consolidated validation record.

Its checks include:

- Independent supplied successors, centered half-turn conventions, and
  rejection of inconsistent forced transitions.
- Exact four-factor profiles and the two distinct $16=4^2$ controls.
- Authentic BBP windows at $p=41,73,97,193$, preserving initial zero and
  checking the factorization, 2-adic carry identity and modular zero fibers.
- All seventeen point-mass laws for the 11/13 reconstruction theorem, plus
  an authentic source carry-count table.
- The exact symmetric sharpness witness for stability constant $3$.
- Rejection of mutually incompatible uniform odd-prime marginals.
- The separate-modulo-3/modulo-5 countermodel and the joint observation
  distinction.
- Positive and negative finite controls, including a constant array that
  retains every pair.

The exploratory floating linear program used to locate the stability witness
is not proof evidence. The retained witness consists of exact integers and
is verified by direct residue sums. No finite measurement is promoted to an
all-prime estimate, and none of these tests fits a normality exponent.

## 8. Hole contract, novelty tax and next falsifier

**Exact open statement.** For every sufficiently large good prime in the
inherited coverage family, evaluate the authentic selected source, its fixed
overlapping windows and prescribed scales. Prove the cumulative upper bound
$\mathcal E_p\le a_p\log p$ for some $a_p\to0$, or another source-specific
estimate that implies the same subpower collision contract.

**Dependency closed by the present work.** A proposed finite prime observation
can now be translated into a precise central-branch statistic. The exact
conditional factors and required aggregate budget are explicit. A claim that
small-prime observations determine the bounded carry can be tested separately
from a claim about its frequencies.

**Dependency still open.** No argument here converts the authentic forcing,
initial zero and full later carry history into the required frequency law.
Identification does not create equidistribution. Source-specific zero-carry
retention, including a first uniform nontrivial saving, remains **OPEN**.

**Novelty tax.** Conditional probability multiplication, residue reconstruction
and finite linear inversion are elementary mathematical tools. Their present
role is to identify the exact information and conditional sample sets needed
by this source program. The aggregate criterion is a less restrictive
contract for the existing collision mechanism, not an independently proved
arithmetic bound and not a proof of pi normality. Academic novelty is
unverified.

**Cheapest falsifiers for a proposed next bridge.** Reject a proof that
multiplies four marginal halves, replaces joint mod-3/mod-5 observations by
their marginals, assumes uniformity in every odd residue ring, drops the
diagonal allowance, or changes the selected initialization. The controls
above provide exact receipts for those failures. For a source-specific
retention proposal, retain the complete conditional profile on fresh prime
windows and state in advance which quantitative upper bound it claims.

**Scoped verdict.** The finite observer theory is stronger and more explicit:
base 3 can identify the target branch at finite precision, primes below 16
can recover its entire bounded law, and the dyadic mechanism composes exactly.
The selected-source frequency theorem and pi normality remain unproved.
