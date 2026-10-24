# Base-three rigidity and coherent prime-base carries

**Date:** 2026-10-24. **Branch:**
`research/pi-dyadic-prime-base-rigidity-2026-10-24`.
**Inherited frontier:** twisted-observer draft #268 at
`06f6b03eed2521c6bd5c02db618cb421ac6b5a51`, over coherent main
`e648df3e4fca73ab6b942232b5ca4b310e9cac08`.

**π normality remains OPEN.** The inherited one-half retention premise is
also OPEN. This report proves a conditional alternative to the one-sixteenth
route: a positive **all-scale** collision exponent, together with vanishing
tripling defect of the **same selected source-window laws**, forces Haar
distribution by classical measure rigidity. Neither source-specific premise
is established here.

There is also an exact bounded carry joining the circle to every prime-adic
inverse-cover coordinate. That construction transports branch labels. It does
not by itself transport the selected source's statistical law.

## 1. Results, assumptions and authority

| Statement | Status | Boundary |
|---|---|---|
| Inverse-circle branch labels have a bounded, coherent carry under every integer multiplier | PROVED | Elementary identity; classical inverse-limit structure |
| A common invariant circle law with positive all-scale collision exponent is Haar | PROVED | Uses the cited Rudolph–Johnson theorem; no ergodicity assumption is omitted |
| Authentic all-scale retention below one plus vanishing tripling defect implies binary normality of π | PROVED CONDITIONAL | Both arithmetic premises remain OPEN |
| Terminal-scale collision saving plus tripling defect alone suffices | REFUTED | Stationary alternating free/zero-block countermodel below |
| The selected BBP windows satisfy the proposed tripling or all-scale bounds | OPEN | Finite measurements do not discharge either quantified premise |
| Normality in base 16 transfers automatically to base 3 or all prime bases | REFUTED as a general implication | Multiplicatively independent bases require additional information |

The abstract reduction is an application of established mathematics, not an
independent scholarly novelty claim. Its proof is written below. The finite
code checks arithmetic and transport instruments; it supplies no Lean or
kernel authority for the analytic theorem.

Related records and executable instruments:

- [Inherited twisted-observer inverse-branch contract](PI_TWISTED_OBSERVER_AGREEMENT.md), §11.1.
- [Inherited source collision and window-coverage proof](PI_SOURCE_COLLISION_ENTROPY.md), §§7–8.
- [This round's preregistration](PI_DYADIC_BASE_PREREGISTRATION.md).
- [Finite inverse-cover carry implementation](../../observational_succ/prime_base_carry.py)
  and [its tests](../../tests/test_prime_base_carry.py).
- [Selected-source coupling implementation](../../observational_succ/pi_base_transport.py)
  and [its tests](../../tests/test_pi_base_transport.py).

## 2. The bounded differential on the inverse circle

Let $T_q(x)=qx\pmod1$ on $\mathbb T=\mathbb R/\mathbb Z$, with the canonical
root represented in $[0,1)$. For any positive cover degree $m$, label the
solutions of $T_mz=x$ by

$$
z_{m,a}(x)=\frac{x+a}{m},\qquad 0\le a<m.
$$

Define the integer carry

$$
c_q(x)=\lfloor qx\rfloor\in\{0,\ldots,q-1\}.
$$

### 2.1 Exact affine transport

Direct substitution gives

$$
T_qz_{m,a}(x)
=z_{m,\,qa+c_q(x)\bmod m}(T_qx).
$$

Indeed, write $qx=T_qx+c_q(x)$ and reduce the integer $qa+c_q(x)$ modulo
$m$. Thus multiplication by $q$ transports the root and label as

$$
(x,a)\longmapsto(T_qx,qa+c_q(x)\bmod m).
$$

If $\gcd(q,m)=1$, this is a permutation of the fibre labels. For dyadic
degrees $m=2^d$, every odd prime acts by such a permutation. Tripling needs
only the three possible carry values $0,1,2$.

When $d\mid m$, reducing the label modulo $d$ commutes with this transport.
At the level of actual circle points, that reduction is multiplication by
$m/d$. In particular, the degree-$16$, degree-$4$ and degree-$2$ diagrams
commute exactly. These identities preserve a source's labels; they do not
assert that the labels occur with equal frequencies.

### 2.2 Composition is coherent

The carries obey

$$
c_{qr}(x)
=q c_r(x)+c_q(T_rx)
=r c_q(x)+c_r(T_qx).
$$

For example, write $rx=\lfloor rx\rfloor+\{rx\}$, multiply by $q$, and take
the floor. This proves the first equality; exchanging $q$ and $r$ proves
the second. Consequently the two multiplication orders induce the same
root, label and total carry at every finite depth.

### 2.3 All prime coordinates can share the same carry

Consider the inverse system of **all** integer circle covers. A point is a
family $(z_m)_{m\ge1}$ satisfying

$$
T_{m/d}z_m=z_d\qquad(d\mid m).
$$

It can be represented by a root $x\in[0,1)$ and compatible residue labels
$a\in\widehat{\mathbb Z}$ through

$$
z_m=\frac{x+(a\bmod m)}m\pmod1.
$$

Chinese remainder compatibility identifies
$\widehat{\mathbb Z}$ with $\prod_p\mathbb Z_p$. The compact topology is the
usual boundary gluing $(1,a)\sim(0,a+1)$, rather than the topology of a
disconnected direct product with a half-open interval. This is the universal
inverse-cover circle, also called the universal solenoid.

Multiplication by $q$ acts as

$$
(x,a)\longmapsto(T_qx,qa+c_q(x)).
$$

The **same bounded integer carry** enters every prime coordinate. At a prime
not dividing $q$, the fibre map is an affine unit map. At a prime dividing
$q$, multiplication on that fibre alone loses a branch. The circle root
retains precisely the corresponding missing choice.

The combined map is invertible when all coordinates are retained. Given
$(x',a')$, take the representative $k=a'\bmod q$ in $\{0,\ldots,q-1\}$ and
set

$$
x=\frac{x'+k}{q},\qquad a=\frac{a'-k}{q}.
$$

The second quotient exists uniquely in the profinite integers because its
numerator is divisible by $q$. Substitution verifies the inverse.

### 2.4 Finite precision and the missing-coordinate control

The infinite inverse must not be confused with an impossible finite one.
An image label known modulo $qm$ determines the preimage label only modulo
$m$. This spends one factor of $q$ in precision. Labels $a,a+m,\ldots,
a+(q-1)m$ modulo $qm$ have the same image; the code retains this ambiguity.

If instead the available modulus $m$ is coprime to $q$, there are exactly
$q$ possible inverse roots. For each $k\in\{0,\ldots,q-1\}$ they are

$$
x_k=\frac{x'+k}{q},\qquad
a_k=q^{-1}(a'-k)\pmod m.
$$

Every candidate maps to the same observed image. The missing $q$-coordinate
is needed to select one. The implementation returns all candidates and does
not choose a preferred source.

This construction is a common carrier with different prime coordinates. It
is not a continuous field identification of $\mathbb Q_3$ with
$\mathbb Q_2$, nor a theorem transferring p-adic digit frequencies to real
digit frequencies. A point mass on one branch remains a point mass after
an affine relabeling. The selected source's **weights** are the missing
statistical information.

## 3. The exact source-law question

Retain the authentic BBP forcing and initial condition:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad y_0=0,\qquad y_n=\{16y_{n-1}+r(n)\}.
$$

For the inherited good primes $p=8m+1$, use

$$
A=m+1,\quad B=4m,\quad N=3m,\qquad
\mu_p=\frac1N\sum_{n=A}^{B}\delta_{y_n}.
$$

Here the good-prime condition is
$\mathrm{ord}_p(16)>\sqrt p/\log p$. These primes have the relative coverage
proved in the inherited source collision report; no new density or
primitive-root premise is introduced. The metric $W_1$ is the infimum of
the mean circular distance over couplings with the prescribed two marginals.

### 3.1 Multiplication by 16 is already an approximate symmetry

Match $T_{16}y_n$ to $y_{n+1}$ at every interior point, and match the last
point to the first. This is a genuine permutation. Since circular distance
is at most one-half,

$$
W_1((T_{16})_*\mu_p,\mu_p)
\le\frac1N\left(
\frac12+\sum_{n=A}^{B-1}\min\!\left(\frac12,r(n+1)\right)
\right).
$$

The forcing is $O(p^{-2})$ on the window, so the right side tends to zero.
Consequently every weak limit of $\mu_p$ is $T_{16}$-invariant. Endpoint
loss is included, not discarded.

### 3.2 Tripling is the new OPEN premise

The useful additional symmetry is

$$
\beta_p(3):=W_1((T_3)_*\mu_p,\mu_p)\longrightarrow0.
$$

On the compact circle, this is equivalent to weak equality of the two laws.
It is enough to prove, for every fixed integer $h$,

$$
\frac1N\sum_{n=A}^{B}
\bigl(e(3hy_n)-e(hy_n)\bigr)\longrightarrow0,
\qquad e(t)=\exp(2\pi i t).
$$

This asks that two Fourier averages agree asymptotically. It does not first
assume that either average vanishes. It concerns the **same base-16 source
window law**, not the separate sequence $3^n\pi$.

An explicit sufficient witness is a permutation $\sigma_p$ of the window
indices such that

$$
\frac1N\sum_{n=A}^{B}d_{\mathbb T}(3y_n,y_{\sigma_p(n)})\longrightarrow0.
$$

The sorting implementation provides an admissible finite coupling and its
exact cost. It does not claim optimal circle transport or an asymptotic
decay rate. A merely bounded cost is insufficient: all circular distances
are already at most one-half.

### 3.3 A bounded fractional-time translator and its discrete sampling debt

There is an exact source-derived translator for every integer multiplier
q>1, but its sampling boundary must be retained. For real s>=1, the original
four-pole formula has the positive integral representation

$$
r(s)=\int_0^1 x^{8s-8}(1-x)P(x)\,dx,\qquad
P(x)=4+4x+4x^2+2x^3+x^4.
$$

For real t>=0, positive-term summation therefore gives

$$
T(t)=\sum_{j\ge1}16^{-j}r(t+j)
=\int_0^1\frac{x^{8t}(1-x)P(x)}{16-x^8}\,dx.
$$

On 0<x<1, one has 0<P(x)<15<16-x^8. Thus T strictly decreases and

$$
0<T(t)<B(t):=\frac1{(8t+1)(8t+2)}.
$$

Define the real interpolation V(t)=16^t T(0)-T(t). The BBP identity gives
T(0)=pi/16. Its recurrence is V(t+1)=16V(t)+r(t+1), and V(0)=0;
consequently V(n)=U_n at every nonnegative integer. This real interpolation
is not obtained by treating the 2-adic Green series as real-convergent.

Put a=log_16(q)>0. The exact bounded translator is

$$
V(t+a)-qV(t)=qT(t)-T(t+a),\qquad
0<V(t+a)-qV(t)<qB(t).
$$

For q=1 both the shift and the difference are zero. For q>1, let mu be the
law of the N integer samples {V(n)} beginning at A, and let mu_a use the
N shifted samples {V(n+a)}. Matching the same n gives

$$
W_1((T_q)_*\mu,\mu_a)\le qB(A),
$$

and the triangle inequality gives the exact equivalence audit

$$
\left|W_1((T_q)_*\mu,\mu)-W_1(\mu_a,\mu)\right|\le qB(A).
$$

Thus the remaining fractional-shift discrepancy is asymptotically equivalent
to the original q-invariance obligation. No integer-time arithmetic saving
has been proved by this reformulation.

For a CONTINUOUS average nu over [A,A+L], with L>=a, interval overlap couples
the shifted and original laws at cost at most a/(2L), using circle diameter
one-half. The translator consequently proves

$$
W_1((T_q)_*\nu,\nu)\le qB(A)+\frac{a}{2L}.
$$

Replacing the integer-sampled law by this continuous average would be the
unjustified step. The rapidly expanding real interpolation gives no uniform
small Riemann-sum error at unit time spacing. The proved continuous bound is
a control that exposes the discrete sampling obligation, not its solution.

## 4. Positive collision dimension plus tripling forces Haar

For a probability measure $\mu$ on the circle, define

$$
Q_\mu(\rho)=(\mu\otimes\mu)
\{(x,z):d_{\mathbb T}(x,z)\le\rho\}.
$$

### Abstract theorem

Suppose that $\mu$ is invariant under $T_{16}$ and $T_3$, and that there
exist $C<\infty$, $s>0$ and $\rho_0>0$ such that

$$
Q_\mu(\rho)\le C\rho^s
\qquad(0<\rho\le\rho_0).
$$

Then $\mu$ is Haar measure $\lambda$. **No ergodicity assumption is needed.**

**Classical input.** The nonergodic Rudolph–Johnson theorem, as stated in
BLMV Theorem 1.3, says that a probability measure $\nu$ invariant under
multiplicatively independent $T_a,T_b$, with
$h_\nu(T_a)=\eta\log a$, satisfies $\nu\ge\eta\lambda$ as measures.
Rudolph's original theorem already covers the relatively prime pair $16,3$.
Positive average entropy alone does not assert equality with Haar.

**Proof of the stated corollary.** We may decrease $s$ so that $0<s<1$.
Let $\mathcal P_k$ partition the circle into $16^k$ half-open intervals.
Pairs in the same interval are within distance $16^{-k}$, hence

$$
\sum_{I\in\mathcal P_k}\mu(I)^2\le C16^{-sk}
$$

for all sufficiently large $k$. Shannon entropy dominates order-two Rényi
entropy, giving

$$
H_\mu(\mathcal P_k)
\ge-\log\sum_{I\in\mathcal P_k}\mu(I)^2
\ge sk\log16-\log C.
$$

The base-16 digit partition is generating. Invariance therefore gives

$$
h_\mu(T_{16})
=\lim_{k\to\infty}\frac1kH_\mu(\mathcal P_k)
\ge s\log16.
$$

The classical theorem implies $\mu\ge s\lambda$. To remove a possible
zero-entropy remainder, form

$$
\mu_1=\frac{\mu-s\lambda}{1-s}.
$$

This is a probability measure invariant under both maps. Domination
$\mu_1\le\mu/(1-s)$ implies

$$
Q_{\mu_1}(\rho)\le\frac{C}{(1-s)^2}\rho^s.
$$

The same entropy argument applies to $\mu_1$ and yields
$\mu_1\ge s\lambda$. Repeating, for every integer $j\ge1$,

$$
\mu\ge\bigl(1-(1-s)^j\bigr)\lambda.
$$

For each fixed repetition the collision constant is finite; it disappears
after division by $k$ in the entropy limit. Letting $j$ tend to infinity
gives $\mu\ge\lambda$. Both measures have total mass one, so
$\mu=\lambda$. This proves the theorem.

This subtraction argument is essential. A single application of positive
average entropy would leave a possible non-Haar component.

## 5. Applying the theorem to the proposed half bound

Use the overlapping windows $W=\{A,\ldots,B-1\}$ and
$W^+=\{A+1,\ldots,B\}$ of length $n=N-1$. Let
$\epsilon_p=r(A+1)-r(B)=O(p^{-2})$ and define the inherited scales

$$
\tau_0=\frac14,\qquad
\tau_{j+1}=\frac{\tau_j-\epsilon_p}{16}.
$$

The inherited OPEN premise, for fixed $0<\theta<1$ and $C_0\ge0$, is

$$
Z_W(\tau_j)\le\theta Q_{W^+}(\tau_j)+C_0n
$$

at every prescribed scale through $J_p$, with $J_p\to\infty$. Its exact
inverse-branch inclusion and endpoint estimate already prove

$$
\frac{Q_W(\tau_j)}{n^2}
\le\theta^j+
\frac{C_0+2\theta}{(1-\theta)n}.
$$

### 5.1 Passing to weak limits without reversing Portmanteau

For each fixed $j$, the radius $\tau_j(p)$ tends to
$r_j=(1/4)16^{-j}$. The normalized $W$-window measures have the same weak
limits as the full windows, since removing one sample has vanishing total
variation cost.

Take one such weak limit $\mu$. For fixed $0<r<r_j$, eventually
$r<\tau_j(p)$. The set $\{d_{\mathbb T}<r\}$ is open. Weak convergence of
the product measures, followed by the preceding finite upper bound, gives

$$
(\mu\otimes\mu)\{d_{\mathbb T}<r\}
\le\liminf_p(\mu_p^W\otimes\mu_p^W)
\{d_{\mathbb T}<r\}
\le\theta^j.
$$

For a closed target radius $\rho<r_j$, choose $r$ strictly between
$\rho$ and $r_j$. Then $Q_\mu(\rho)\le\theta^j$ as well. Choosing a
scale with $\rho<r_j\le16\rho$, including the adjacent coarser scale in an
equality case, gives

$$
Q_\mu(\rho)\le(64\rho)^s,
\qquad s=-\log_{16}\theta>0.
$$

In particular, the hypothetical all-scale $\theta=1/2$ premise supplies
$s=1/4$. This is sufficient for the abstract theorem once tripling
invariance is added. It does not require the stronger $\theta=1/16$ premise
used by the earlier single-symmetry collision-entropy route.

### 5.2 A prefix-uniform weakening

It suffices to have at least $\alpha j-D$ contracting scales among the first
$j$ scales, uniformly for every $j\le J_p$, with fixed $\alpha>0$ and finite
$D$. Use factor one and the endpoint error on the remaining scales. The
product is bounded by $\theta^{\alpha j-D}$, while the normalized additive
error is $O(j/n)$. For each fixed $j$ that error vanishes. The same argument
then gives exponent $s=-\alpha\log_{16}\theta>0$.

Having $\alpha J_p$ contracting scales somewhere in the entire schedule is
insufficient for this conclusion. They could all drift to increasingly fine
radii. A terminal-scale bound alone also fails, as §6 proves.

### 5.3 From source windows to binary normality

Assume the preceding positive all-scale bound and $\beta_p(3)\to0$ for all
sufficiently large inherited good primes. Compactness gives weakly
convergent subsequences. Every limit has both symmetries and the collision
bound, so §4 makes every limit Haar. Therefore $\mu_p\to\lambda$.

The authentic Green tail satisfies

$$
\{16^{n-1}\pi\}=\{y_n+T_n\},\qquad
0<T_n<\frac1{(8n+1)(8n+2)}.
$$

Its vanishing window error transports Haar convergence to the true orbit
window indexed by $m,\ldots,4m-1$. For any fixed centered digit-block
indicator, weak convergence to Haar gives a centered sum $o(m)$; the
indicator's finitely many boundary points have Haar mass zero.

The good-prime starts are relatively dense in multiplicative scale. The
inherited coverage argument therefore promotes
$W(m)=\sum_{m\le j<4m}f_j=o(m)$ to every large integer start. Writing
$S(L)=\sum_{j<L}f_j$ gives

$$
S(4m+r)=S(m)+W(m)+O(1),\qquad 0\le r<4.
$$

Repeated division by four and a geometric-series estimate yield
$S(L)=o(L)$. Every fixed hexadecimal word has the correct frequency. Thus
π is normal in base 16 and consequently in bases 4 and 2.

**This is a conditional theorem.** The authentic positive all-scale saving
and authentic tripling symmetry remain unproved arithmetic obligations.

## 6. Why terminal collision saving is not enough

Here is a countermodel even with exact $T_{16}$-invariance.

For each positive integer $L$, alternate blocks of $L$ independent uniform
hexadecimal digits with blocks of $L$ forced zeros. Randomize the phase
uniformly among the $2L$ positions; all active digits are independently
uniform. Map the stationary one-sided digit sequence into the circle and
call its law $\nu_L$.

1. **Exact base-16 invariance.** Shifting the sequence cycles its uniform
   phase and preserves the independent uniform active digits.
2. **Non-Haar weak limit.** For every fixed word length $k$, the probability
   of straddling a block boundary is at most $(k-1)/L$. Otherwise the first
   $k$ digits are all uniform or all zero, with asymptotic weights one-half.
   Hence $\nu_L\to(\lambda+\delta_0)/2$.
3. **Vanishing tripling defect.** This limit is $T_3$-invariant. Continuity
   on the compact circle gives
   $W_1((T_3)_*\nu_L,\nu_L)\to0$.
4. **Positive terminal collision exponent.** At length $d=L^2$, every
   conditional phase has at least $d/2-L$ active digits. Its sum of squared
   word probabilities is at most $16^{-d/2+L}$. Convexity of squared norm
   preserves this upper bound after averaging phases. A radius $16^{-d}$
   close pair lies in equal or adjacent cells, and Cauchy–Schwarz gives

$$
Q_{\nu_L}(16^{-d})\le3\,16^{-d/2+L}.
$$

Thus a fixed positive terminal collision exponent coexists with a non-Haar
limiting law and vanishing tripling defect. This refutes the proposed
generic shortcut. It does not counterfeit the authentic BBP source;
excluding this behavior there requires a source-specific theorem.

## 7. Other controls and the source-selector debt

### 7.1 Half retention with an exact tripling defect

Let $\mu_C$ be the base-16 Bernoulli law with independent fair digits in
$\{0,1\}$. It is $T_{16}$-invariant and has entropy $\log2$. Its population
zero-branch retention is one-half, as in the inherited control.

For $X$ with this law, its support is $[0,1/15]$ and
$\mathbb E X=1/30$. The natural coupling to $3X$ has circular cost
$\mathbb E(2X)=1/15$. The circle-1-Lipschitz observable
$f(x)=d_{\mathbb T}(x,0)$ equals $x$ on both supports and gives the same
lower bound. Therefore

$$
W_1((T_3)_*\mu_C,\mu_C)=\frac1{15}.
$$

For $k$ truncated digits the exact cost is $(1-16^{-k})/15$. The coupling
tests verify both matching upper and observable lower bounds. This control
satisfies positive dimension and fails tripling symmetry.

### 7.2 Joint invariance with a zero-entropy remainder

For $0<c<1$, the law $c\lambda+(1-c)\delta_0$ is invariant under both maps
and has entropy $c\log16$. It is not Haar and obeys
$Q(\rho)\ge(1-c)^2$ at every positive radius. This defeats an argument that
uses average positive entropy once and discards the remainder. It explains
why the residual iteration in §4 is necessary.

### 7.3 Fixed-index comparison is the wrong coupling

Under Haar law,

$$
\int d_{\mathbb T}(3x,16^k x)\,d\lambda(x)=\frac14
\qquad(3\ne16^k).
$$

Multiplication by the nonzero integer $3-16^k$ preserves Haar measure, and
the mean circular distance to zero is one-quarter. Thus a same-index or
fixed-time-shift defect need not vanish when the desired law is exactly
uniform. A genuine permutation/coupling is required.

### 7.4 A small forcing correction changes the selected initial state

The authentic tail obeys $16T_{n-1}=r(n)+T_n$. Consequently

$$
w_n=3y_n+2T_n\pmod1
$$

obeys the same forcing recurrence as $y_n$:
$w_n=\{16w_{n-1}+r(n)\}$. But

$$
w_0=2T_0=\frac\pi8\ne0=y_0.
$$

The correction is small at late times yet changes the selected initial
state. This identity therefore does not prove equality of the selected
source laws.

For an already specified coupling, the true π shadow has a controlled cost:
multiplication by $q$ is $q$-Lipschitz, and a permutation uses each destination
once, so the source-to-shadow cost difference is at most

$$
\frac{q+1}{N}\sum_{n=A}^{B}\frac1{(8n+1)(8n+2)}=O_q(p^{-2}).
$$

This budget transfers a valid coupling estimate. It does not create one.

## 8. What “base 3 is enough” does and does not mean

The pair $(16,3)$ is relatively prime and multiplicatively independent.
For the common-law rigidity theorem, no further primes below 16 are needed.
Any odd prime could replace 3. In contrast, $16=4^2=2^4$ gives dependent
actions; these preserve many non-Haar laws and do not provide the second
symmetry in §4.

The theorem concerns the law sampled along $16^n\pi$. Its invariance under
tripling is not a frequency theorem for $3^n\pi$. The conclusion is base-16
normality followed by dependent-base transfer to 4 and 2. Base-3 normality
requires an additional argument on its own orbit.

Becher–Slaman, Theorem 5, proves that any multiplicative-dependence-closed
set of bases can occur as exactly the normal bases of a real number, with
failure of simple normality outside that set. In particular, normality at
all prime bases alone does not imply base-6 or absolute normality.

## 9. Verification and the remaining research contract

The finite inverse-cover implementation was checked by

~~~sh
python -m unittest discover -s tests -p 'test_prime_base_carry.py'
~~~

All 14 tests passed. They compare transported labels with actual rational
circle points, check the carry cocycle and degree reductions, compare
different prime-coordinate projections, preserve missing-coordinate
ambiguity, and reject lost carry and invented precision. The independent
coupling module checks genuine permutations, circular endpoint budgets and
the exact Cantor control. These checks establish their finite scope only.

The exact remaining source contract is:

- **All-scale nonconcentration:** every weak limit of the authenticated
  selected windows satisfies a positive power collision bound. The proposed
  half-retention or prefix-uniform refinement estimates would suffice.
- **Same-law tripling transport:** the selected windows satisfy
  $\beta_p(3)\to0$, preferably through a coupling constructed or bounded from
  source arithmetic with $y_0=0$ retained.

The two obligations are mathematically separable, as the controls show.
Their conjunction invokes a completed classical rigidity theorem. Finite
branch bijections, Galois averages, bounded carries, a single terminal
collision exponent, or a changed initial state cannot replace either
obligation. The next decisive probe is a concrete authenticated tripling
coupling, with a bound or a counterexample stated before its interpretation.

## 10. Primary references

1. Daniel J. Rudolph, **“×2 and ×3 invariant measures and entropy,”**
   *Ergodic Theory and Dynamical Systems* 10 (1990), 395–406,
   [DOI 10.1017/S0143385700005629](https://doi.org/10.1017/S0143385700005629).
   [Official full paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/64243AD8323B37089540F911F8CC77EB/S0143385700005629a.pdf/2_and_3_invariant_measures_and_entropy.pdf).
   The abstract and introduction cover relatively prime multipliers and
   joint-semigroup ergodicity. No unproved zero-entropy classification is used.
2. Jean Bourgain, Elon Lindenstrauss, Philippe Michel and Akshay Venkatesh,
   **“Some effective results for ×a × b,”**
   [author-hosted primary paper](https://www.math.ias.edu/~akshay/research/blmv.pdf).
   Theorem 1.3 is the nonergodic domination input. Theorem 1.4 is an effective
   result but is not treated here as a selected-source rate theorem.
3. Verónica Becher and Theodore A. Slaman,
   **“On the Normality of Numbers in Different Bases,”**
   [author-hosted primary paper](https://math.berkeley.edu/~slaman/papers/bases.pdf).
   Theorem 5 supplies the precise independent-base counterboundary.

**Final boundary:** coherent inverse-cover carries are proved and finite
transport instruments are implemented. The base-three alternative is a
rigorous conditional reduction. π-specific tripling invariance, positive
all-scale collision decay, and π normality remain OPEN.
