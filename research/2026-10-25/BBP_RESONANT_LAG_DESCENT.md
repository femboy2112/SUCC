# Resonant lag filters: old-clock annihilation and fresh-clock survival

Date: 2026-10-25. Baseline: `461942c0bf616518e668d236d1c6b1596665a7dd`.
Scope: the original signed four-pole BBP source, with integer lifts retained.
This is an arithmetic filter analysis independent of the Gram-purity program.

**Verdict:** exact new source-filter and prime-birth identities, a quantitative
mixed-tail transport extension, and an obstruction to automatic conductor
descent. No signed lag saving, no selected-window cancellation, and no proof of
base-16 normality is obtained.

## Hole contract and outcome

The candidate was that differencing at a complete prime-clock period removes
the difficult arithmetic state, leaving a simpler source to which cancellation
theorems can be reapplied. The valid part is strictly local: that old prime's
first torsion digit disappears. The stronger state/conductor-descent claim is
refuted below by the authentic source itself, with no counterfeit forcing.

The still-open sufficient statement is decay of the actual signed lag averages
needed by van der Corput, uniformly over the lags and windows used there. An
individual difference identity or smaller real tail does not establish this.
The next lamp is a signed estimate that handles the surviving old-state
multiplier together with the new prime births. A count of denominator primes
alone is not a real-circle separation estimate.

## 1. Exact finite filter passport

Write

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
$$

Let the positive integer lags be $k_1,\ldots,k_s$, let $E$ denote forward
translation of the index, and set

$$
P(X)=\prod_{i=1}^s(X^{k_i}-1)=\sum_{j=0}^{D}c_jX^j,
\qquad D=\sum_i k_i,\qquad A=P(16)=\prod_i(16^{k_i}-1)>0.
$$

**RLD-01 — PROVED, finite algebra.** For every integer $n\ge0$,

$$
P(E)U_n=A U_n+
\sum_{j=0}^D c_j\sum_{a=1}^j16^{j-a}r(n+a).
$$

Proof: iterate the original recurrence to obtain
$U_{n+j}=16^jU_n+\sum_{a=1}^j16^{j-a}r(n+a)$, then sum with the
coefficients $c_j$. This retains every intermediate signed forcing term and
every integer carry. It remains valid modulo one afterwards.

If two lawful sequences have different initial states, their difference at
time $n$ is $16^n\delta$. Applying a finite integer-coefficient filter $Q(E)$
changes this to $16^nQ(16)\delta$. Consequently:

**RLD-02 — PROVED, state-erasure classification.** A finite polynomial filter
erases arbitrary initial-state dependence exactly if $Q(16)=0$, equivalently
if $X-16$ divides $Q(X)$. Every nonempty ordinary mixed lag filter above fails
this condition because $A>0$.

This is a statement about rational lifts and arbitrary initial states. Modulo
one, isolated initial differences can vanish at particular frequencies; that
does not imply arbitrary-state independence. The genuinely state-erasing
filter $(E-16)U_n=r(n+1)$ still leaves the original rational forcing. It is
not the ordinary correlation difference used in van der Corput.

**Fixed-filter character dichotomy (paper corollary).** For any fixed
integer polynomial Q, put A=Q(16). The inherited exact Green identity gives

$$Q(E)U_n=A16^n\alpha-Q(E)T_n.$$

Because the coefficients and shifts of Q are fixed and the positive Green
tail is summable, `sum_(n>=1)|Q(E)T_n|` is finite. For each fixed integer h,
the character sums of Q(E)U_n and A16^n alpha therefore differ by a bounded
amount, using `|e(x)-e(y)|<=2*pi*|x-y|`. If A=0 the normalized filtered
character sum tends to **one**. If A is nonzero, its cancellation is exactly
the remaining original-orbit cancellation at frequency hA, with a paid O(1)
transport error. Thus a fixed linear filter either erases the selected
boundary and leaves a noncancelling character, or retains that boundary at
another frequency. This is a classification of these filters, not an
obstruction to more general nonlinear or growing-filter arguments. Growing
filters require their own uniform tail costs, supplied below only in the
declared mixed-lag class.

## 2. A source-authenticated fresh-prime obstruction

Fix a genuine prime $q\equiv1\pmod8$ and set $b=(q+7)/8$. In the interval
$b\le j<b+3(q-1)/8$, the $q$-primary component of $U_j$ is
$4\cdot16^{j-b}/q$ modulo one. Before $b$, it is zero. These are the original
first-birth and no-new-pole facts, not a model with independent clocks.

**RLD-03 — PROVED, complete birth-cut formula.** If
$n+D<b+3(q-1)/8$, the first $q$-primary digit of $P(E)U_n$ is

$$
4\sum_{\substack{0\le j\le D\\n+j\ge b}}
c_j16^{n+j-b}\pmod q.
$$

Proof: primary decomposition in $\mathbb Q/\mathbb Z$ is additive. Apply it
to each endpoint, using the genuine birth formula above. No denominator has
acquired a second $q$-pole in the stated domain.

Two consequences distinguish old-clock cancellation from new-clock creation.

1. If $n\ge b$, the digit is $4\cdot16^{n-b}P(16)\pmod q$.
   A lag divisible by $\mathrm{ord}_q(16)$ kills this old component.
2. If $n+D=b$, only the last endpoint has reached the birth. Since $c_D=1$,
   the digit is exactly **4 modulo $q$**, independently of every lag choice.

In particular the reduced denominator of $P(E)U_{b-D}$ is divisible by $q$
exactly once, whenever $b\ge D$. Thus every fixed mixed lag filter has
unbounded prime support on the original source. Infinitely many primes
$q\equiv1\pmod8$ can be established here without any asymptotic prime theorem:
if there were finitely many, take an even integer $a$ divisible by all of
them; every prime divisor of $a^4+1$ is odd and gives $a$ multiplicative order
exactly eight, hence is $1\pmod8$, but divides none of $a$'s prime factors.

The finite source-authenticated receipt is particularly small:

$$
\mathrm{ord}_{17}(16)=2,\qquad
U_6-U_4:\quad \text{17-primary digit }0,
\quad\text{41-primary digit }4.
$$

Both $U_4$ and $U_6$ lie in the first 17-window (indices 3 through 8).
The new 41-clock is born at index 6. The exact same correlation difference
therefore kills the selected old clock while retaining a new prime.

**Limit of the obstruction:** this does not say the full denominator grows
monotonically at every time, nor that new primes prevent cancellation. It
refutes the general implication “selected prime disappears, so the source
conductor has descended.” Real near-collisions can occur despite large or
new denominators.

## 3. Mixed-lag Green-tail transport with polynomial lag cost

The inherited BBP Green identity is

$$
U_n=16^n\alpha-T_n,\qquad \alpha=\pi/16,
\qquad
T_n=\int_0^1\frac{x^{8n}g(x)}{16-x^8}\,dx,
\quad g(x)=4-2x^3-x^4-x^5.
$$

We use this existing identity, not a new proof of its orbit transport. The
new extension here permits arbitrary mixed positive lags. Define

$$
R_{n,\mathbf k}=(-1)^sP(E)T_n
=\int_0^1\frac{x^{8n}g(x)}{16-x^8}
\prod_{i=1}^s(1-x^{8k_i})\,dx>0.
$$

**RLD-04 — PROVED, exact positive enclosure.** Put

$$
D_{n,\mathbf k}=(-1)^sP(E)r(n+1)>0.
$$

Then for every integer $H\ge1$,

$$
L=\sum_{a=0}^{H-1}16^{-a-1}D_{n+a,\mathbf k}
<R_{n,\mathbf k}
<L+\frac{D_{n+H,\mathbf k}}{15\,16^H}.
$$

Proof: the same positive kernel without $(16-x^8)^{-1}$ represents $D$;
expand that denominator geometrically. The $D$ terms decrease strictly in
$n$, so the omitted positive sum is bounded by its first moment times the
geometric tail. There is no subtraction of independently rounded tails.

Write $g(x)=(1-x)H(x)$, where
$H(x)=4+4x+4x^2+2x^3+x^4$. The inherited elementary bounds
$1/4<H(x)/(16-x^8)<1$ hold on $(0,1)$. Therefore, for the exactly rational
positive integral

$$
K_{n,\mathbf k}=\int_0^1x^{8n}(1-x)
\prod_i(1-x^{8k_i})\,dx
=(-1)^s\sum_{j=0}^D
\frac{c_j}{(8(n+j)+1)(8(n+j)+2)},
$$

we have $K/4<R<K$. Also $1-x^{8k}\le8k(1-x)$ gives the explicit bound

$$
0<R_{n,\mathbf k}<
\min\left\{
\frac1{(8n+1)(8n+2)},\quad
\frac{8^s(\prod_i k_i)(s+1)!}
{\prod_{a=1}^{s+2}(8n+a)}
\right\}.
$$

This is uniform for all positive lags; no fixed-lag asymptotic is being
silently used in a growing-lag regime. For fixed $s$, it yields the useful
bound $O_s((\prod_i k_i)n^{-s-2})$ when $n\ge1$.

**RLD-05 — PROVED transport, OPEN cancellation.** The completed-circle
identity is

$$
P(E)U_n=A16^n\alpha-(-1)^sR_{n,\mathbf k}.
$$

For every integer $h$,

$$
\left|e(hP(E)U_n)-e(hA16^n\alpha)\right|
\le\frac{44|h|}{7}R_{n,\mathbf k},
\qquad e(x)=\exp(2\pi i x).
$$

Sum the displayed rational majorant over any finite window to get a
certified finite transport bound. The frequency on the completed circle
is $hA=h\prod_i(16^{k_i}-1)$, which can grow exponentially in the lags.
This theorem does **not** supply cancellation at those growing frequencies.
It also does **not** replace the completed-circle phase by $e(hA U_n)$:
that different comparison additionally costs $A T_n$ and can be exponentially
larger. This distinction prevents the polynomial tail gain from hiding the
original frequency/initial-state debt.

For unit lags this recovers the already established Pascal-tail calculus in
[PI_PASCAL_REAL_KERNEL.md](../2026-10-24/PI_PASCAL_REAL_KERNEL.md), so only
the arbitrary mixed-lag extension and its combined prime-birth passport are
claimed here. The earlier ordinary lag-cost bound is in
[PI_ONE_SHOT_NATURAL_CARRIER_SPECTRAL_FORGE.md](../2026-10-24/PI_ONE_SHOT_NATURAL_CARRIER_SPECTRAL_FORGE.md).

## 4. Reproducible verification and claim boundary

Implementation: `observational_succ/bbp_resonant_lags.py`.
Independent controls: `tests/test_bbp_resonant_lags.py`.

Command actually run:

```sh
python -m unittest discover -s tests -p 'test_bbp_resonant_lags.py' -v
```

Observed result: **11 tests passed**. Controls use a separately written
literal four-pole forcing, repeated differences rather than filter expansion,
completed-source rational interval checks, exact old/fresh primary residues,
unit-lag recovery of the inherited Pascal kernel, one-coefficient mutation,
invalid/composite primes, exceptional primes 3 and 5, and second-pole rejection.
These finite checks calibrate the implementation; the universal statements
are justified by the paper proofs above. They are not formal Lean proofs.

| Claim | Status | What remains unpaid |
|---|---|---|
| RLD-01 filter identity | PROVED, finite algebra | None inside its stated source |
| RLD-02 state-erasure classification | PROVED | Does not estimate selected-state averages |
| RLD-03 birth-cut formula and fresh-prime survival | PROVED | No real-circle separation follows |
| Automatic conductor descent from resonant differencing | REFUTED | Authentic 17/41 receipt |
| RLD-04 mixed positive tail enclosure | PROVED | Tail size is not signed cancellation |
| RLD-05 completed-circle mixed-lag transport | PROVED reduction | Growing-frequency estimate remains OPEN |
| Authentic resonant-lag decorrelation | UNVERIFIED | Need a new signed source-specific estimate |

The source-compatible mechanism that survives this attack is now explicit:
ordinary differencing retains $P(16)$ times the selected historical state,
even when its residue annihilates a chosen prime, while the causal forcing
introduces fresh prime births. A successful next argument must control that
joint signed object, not merely the vanished old prime or the small smooth
tail.
