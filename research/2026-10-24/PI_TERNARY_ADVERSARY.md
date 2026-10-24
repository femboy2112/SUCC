# Pascal tripling: finite carries, binary windows, and the law that remains open

**Date:** 2026-10-24. **Inherited head:** `6e8fa8b77886b13f1f533ed8083fd88c849d14b3`
from draft #272. **Authority:** paper proofs and separately stated exact finite
checks. The results below concern actual maps, arbitrary probability laws, and
the specified BBP source where explicitly stated. They do not prove pi normality.
No academic priority or external-referee authority is claimed.

## 1. Frozen question and verdict

The question is whether the weighted Pascal identity

$$
\sum_{j=0}^k\binom kj2^j=3^k
$$

can make the base-three rigidity route pay its missing symmetry premise. The
strongest faithful version keeps the actual circle points, their temporal
dependence, and every carry. The inherited source is

$$
U_0=0,\quad U_{n+1}=16U_n+r(n+1),\quad y_n=\{U_n\},
\quad U_n=16^n\alpha-T_n,\quad\alpha=\pi/16.
$$

The source and its positive tail are defined in
[the inherited kernel dossier](PI_PASCAL_REAL_KERNEL.md). The four-pole forcing
is never changed in claims explicitly about this source.

**Verdicts.** Pascal gives an exact division-free tripling readout on binary
circle orbits. Finite binary digit readout has a sharp, explicitly described
exceptional set: two alternating suffixes. A four-phase averaged symmetry is a
sufficient and formally weaker symmetry target than tripling every original
base-16 law. However, even a doubling-invariant law with positive entropy and a
positive all-scale collision exponent need not preserve its law under the
Pascal tripling map. The remaining same-law premise is OPEN for the BBP source.

The cheapest falsifiers used below are a biased Bernoulli binary law, a
four-point periodic orbit, and exact non-dyadic digit-cut locations. These are
counterexamples to general implications, not counterexamples to the fixed BBP
source. The new useful cut is the averaged symmetry in Section 6; the finite
coding lemma in Section 5 supplies its explicit boundary budget.

## 2. Phase addition and observable averaging are distinct

Write $T_qx=qx\pmod1$ on $\mathbb T=\mathbb R/\mathbb Z$. For every $x$,

$$
\boxed{\ T_3x=x+T_2x\pmod1,\qquad
T_{3^k}x=\sum_{j=0}^k\binom kjT_{2^j}x\pmod1.\ }
\tag{TA-1}
$$

All coefficients are integers, so these are well-defined operations on circle
points without choosing real lifts. The proof is the binomial theorem applied
to integer multipliers. In particular, a new division-cover coordinate is not
intrinsic to tripling after binary deblocking. The modulus $5^k$ in the earlier
rational Pascal filter is a cost of that particular filter, not a universal
cost of the circle map $T_{3^k}$.

If $X$ has law $\mu$, phase addition in TA-1 gives law $(T_{3^k})_*\mu$.
By contrast, a normalized Pascal average of observables is

$$
\mathcal A_kf(x)=2^{-k}\sum_{j=0}^k\binom kjf(T_{2^j}x).
$$

For every $T_2$-invariant $\mu$ and every bounded measurable $f$,
$\int\mathcal A_kf\,d\mu=\int f\,d\mu$. This follows term by term.
Neither identity equates the law of the phase sum with the law of $X$.
The variables $X,T_2X,\ldots$ are deterministic functions of the same variable;
no independent choices have been introduced by counting Pascal paths.

There is a quantitative information boundary as well. For a fixed integer
$q\ge2$, put $\nu=(T_q)_*\mu$ and let $H_m$ be the entropy of the dyadic
depth-$m$ partition. The image of one input cell intersects at most $q+1$
output cells, while one output cell has $q$ preimage intervals, each meeting
at most two input cells. Conditional entropy therefore gives

$$
H_m(\nu)\le H_m(\mu)+\log(q+1),\qquad
H_m(\mu)\le H_m(\nu)+\log(2q).
$$

Thus fixed-$q$ multiplication preserves the entropy rate whenever it exists.
For a $T_2$-invariant law this includes its binary block entropy rate. In
particular, a fixed Pascal phase sum does not create an independent source of
entropy. The constants depend on $q$; this statement does not assert uniformity
when the Pascal order and hence $q=3^k$ grow with the measured block length.

## 3. A non-atomic, positive-collision-dimension counterexample

Let $0<p<1$, and let $\mu_p$ be the law of

$$
X=\sum_{j\ge1}B_j2^{-j},\qquad
\Pr(B_j=1)=p,
$$

where the bits are independent. Removing the first bit shows directly that
$(T_2)_*\mu_p=\mu_p$, hence $(T_{16})_*\mu_p=\mu_p$. Every point has zero
mass because its length-$m$ cylinder has mass at most
$\max(p,1-p)^m\to0$. The length-$m$ block entropy is exactly
$m[-p\log p-(1-p)\log(1-p)]>0$.

For the dyadic cells $I_{m,j}=[j2^{-m},(j+1)2^{-m})$, independence gives

$$
\sum_j\mu_p(I_{m,j})^2=[p^2+(1-p)^2]^m.
$$

Let $Q_\mu(\varepsilon)=\iint1_{\|x-y\|_{\mathbb T}\le\varepsilon}
\,d\mu(x)d\mu(y)$. Same-cell pairs are close. At distance at most $2^{-m}$,
only the same and adjacent cells can contribute, except null boundaries.
The inequality $2ab\le a^2+b^2$ bounds the adjacent-cell terms. Thus

$$
[p^2+(1-p)^2]^m\le Q_{\mu_p}(2^{-m})
\le3[p^2+(1-p)^2]^m.
\tag{TA-2}
$$

Monotonicity extends this to a positive all-scale power bound, with exponent
$\beta=-\log_2[p^2+(1-p)^2]>0$.

Nevertheless, tripling changes this law unless $p=1/2$. Here is an exact
one-bit witness, requiring no entropy theorem. Write $F(t)=\mu_p([0,t))$ and
$d=1-p+p^2$. The two self-similar equations at $1/3$ and $2/3$ are

$$
F(1/3)=(1-p)F(2/3),\qquad F(2/3)=1-p+pF(1/3).
$$

Consequently

$$
F(1/3)=\frac{(1-p)^2}{d},\quad F(2/3)=\frac{1-p}{d},\quad
F(1/6)=\frac{(1-p)^3}{d},\quad
F(5/6)=\frac{(1-p)(1+p^2)}d.
$$

The preimage of $[0,1/2)$ under $T_3$ is
$[0,1/6)\cup[1/3,1/2)\cup[2/3,5/6)$. Therefore

$$
\boxed{
(T_3)_*\mu_p([0,1/2))
=(1-p)+\frac{p(1-p)(2p-1)}{1-p+p^2}.
}
\tag{TA-3}
$$

At $p=1/4$, the original and tripled probabilities are $3/4$ and $33/52$;
their difference is $3/26$. The collision exponent is $\log_2(8/5)>0$.
This defeats the proposed implication even for a non-atomic law invariant
under binary shifts and possessing positive collision dimension at every scale.
It strengthens the calibration relevant to binary deblocking; it does not
replace the earlier fixed-source countermodels or claim their arithmetic data.

## 4. Exact digit lookahead and its two exceptional words

Use the non-eventually-one binary expansion, so dyadic numbers have terminating
expansions. For integers $m\ge1$ and $L\ge1$, consider predicting the first $m$
binary digits of $T_3x$ from the first $m+L$ binary digits of $x$.

The output digit cuts occur at $j/(3\cdot2^m)$. The cuts with $3\mid j$ are
dyadic and already coincide with input cell boundaries. Every other cut lies
strictly inside a unique input cell of depth $m+L$. In each cell of depth $m$,
their relative locations are $1/3$ and $2/3$, whose binary expansions are
$0.010101\ldots$ and $0.101010\ldots$. Their depth-$L$ cells are distinct
for $L\ge1$. Therefore:

**Exact coding theorem.** The ambiguous depth-$m+L$ cells are precisely those
whose last $L$ digits are one of the two alternating words. There are exactly
$2^{m+1}$ such cells, and their total Lebesgue mass is

$$
\boxed{2^{1-L}.}
\tag{TA-4}
$$

Every other input cell determines the requested output word uniquely. Every
ambiguous cell contains two inputs with different output words. Thus no finite
lookahead works for every input, even for the first output bit. This statement
is about a fixed left-to-right lookahead; it does not deny finite-state
multiplication or the continuous division-free circle map in TA-1.

The binary carry gives an equivalent constructive proof. To add $x$ and $2x$,
let $b_j$ be the input bits and let $c_j\in\{0,1\}$ be the carry from column
$j$ to its left. Then

$$
c_j=\left\lfloor\frac{b_j+b_{j+1}+c_{j+1}}2\right\rfloor.
$$

An adjacent pair $00$ sets $c_j=0$ independently of the distant tail; $11$
sets $c_j=1$; and $01$ or $10$ passes $c_{j+1}$ unchanged. Any nonalternating
suffix therefore fixes the needed incoming carry. Infinite alternation is
the boundary ambiguity at the non-dyadic cuts.

For the preceding Bernoulli control, the ambiguous-set probability is exactly

$$
\mu_p(\mathrm{Amb}_{m,L})=
\begin{cases}
2[p(1-p)]^{L/2},&L\text{ even},\\
[p(1-p)]^{(L-1)/2},&L\text{ odd}.
\end{cases}
\tag{TA-5}
$$

It tends to zero exponentially while the same-law defect in TA-3 stays
nonzero. Fast carry synchronization and law preservation are distinct claims.

More generally, for an odd integer $q\ge3$ and $2^L\ge q$, the first $m$
digits of $T_qx$ have exactly $(q-1)2^m$ ambiguous depth-$m+L$ cells, of total
Lebesgue mass $(q-1)2^{-L}$. Indeed, among the $q2^m-1$ internal output cuts,
exactly $2^m-1$ are dyadic; the remaining cuts are separated by more than one
input cell width and are internal to distinct cells. This is a counting
statement under Lebesgue measure, not a law for the BBP source.

## 5. A finite-block law test with an explicit boundary budget

Let $P_m\mu$ denote the distribution of the first $m$ binary digits under
$\mu$. For each input word $w$ of length $m+L$, complete it with zeros and
apply $T_3$; call its first $m$ output digits $\tau_{m,L}(w)$. Set

$$
\mathcal D_{m,L}(\mu)=
\operatorname{TV}((\tau_{m,L})_*P_{m+L}\mu,P_m\mu),
$$

where total variation is $\sup_A|\nu(A)-\mu(A)|$, equivalently half the
$\ell^1$ difference for these finite distributions. Outside
$\mathrm{Amb}_{m,L}$, the finite rule gives the exact output. Hence

$$
\operatorname{TV}(P_m(T_3)_*\mu,P_m\mu)
\le\mathcal D_{m,L}(\mu)+\mu(\mathrm{Amb}_{m,L}).
\tag{TA-6}
$$

Quantizing to dyadic midpoints costs at most $2^{-m-1}$ per measure, and
the diameter of the circle is $1/2$. Thus its Wasserstein distance satisfies

$$
W_1((T_3)_*\mu,\mu)
\le2^{-m}+\frac12\mathcal D_{m,L}(\mu)
+\frac12\mu(\mathrm{Amb}_{m,L}).
\tag{TA-7}
$$

If $\mu$ is $T_2$-invariant, the ambiguous set is $T_2^{-m}$ of the two
alternating depth-$L$ cells. Let their masses be $a,b$. Same-cell pairs give
$a^2+b^2\le Q_\mu(2^{-L})$, so

$$
\mu(\mathrm{Amb}_{m,L})=a+b
\le\sqrt{2Q_\mu(2^{-L})}.
$$

Under the all-scale hypothesis $Q_\mu(\varepsilon)\le C\varepsilon^\beta$,

$$
\boxed{
W_1((T_3)_*\mu,\mu)
\le2^{-m}+\tfrac12\mathcal D_{m,L}(\mu)
+\sqrt{C/2}\,2^{-\beta L/2}.
}
\tag{TA-8}
$$

This isolates an actual finite-block discrepancy and an explicit carry-boundary
budget. The inherited collision premise would automatically control the latter.
No estimate on $\mathcal D_{m,L}$ has been proved for the authentic source.
The lemma is an operational reduction, not a replacement of the open invariance
condition by a secretly assumed frequency assertion.

## 6. Four binary phases suffice for the rigidity target

The following conditional reduction weakens which empirical law must acquire
the additional symmetry. Let $\mu$ be a $T_{16}$-invariant probability measure,
and define its four-phase average

$$
\overline\mu=\frac14\sum_{r=0}^3(T_{2^r})_*\mu.
\tag{TA-9}
$$

Then $\overline\mu$ is $T_2$-invariant, by telescoping and $T_{16}\mu=\mu$.
Suppose $Q_\mu(\varepsilon)\le C\varepsilon^\beta$ for all small positive
$\varepsilon$ and some $\beta>0$. The same type of bound holds for
$\overline\mu$. For completeness, at $\varepsilon=2^{-m}$ partition the
circle into $2^m$ cells. For $a=2^r$, each cell has $a$ preimage cells of
length $\varepsilon/a$. Cauchy--Schwarz gives

$$
\sum_j[((T_a)_*\mu)(I_{m,j})]^2
\le a\sum_{i=0}^{a2^m-1}\mu(I_{a2^m,i})^2
\le aQ_\mu(\varepsilon/a).
$$

Convexity of the square for the average, followed by the adjacent-cell bound,
therefore gives

$$
Q_{\overline\mu}(2^{-m})
\le\frac{3C}{4}\sum_{r=0}^3(2^r)^{1-\beta}\,2^{-m\beta}.
\tag{TA-10}
$$

Non-atomicity follows already from the original collision bound, so partition
boundaries cause no exceptional terms. Monotonicity fills the intervening scales.

**Conditional closure theorem.** In addition to the preceding hypotheses,
assume only $(T_3)_*\overline\mu=\overline\mu$. The all-scale version of the
Rudolph--Johnson rigidity argument in
[the inherited base-three theorem](PI_BASE_THREE_RIGIDITY.md), now with bases
2 and 3, implies $\overline\mu$ is Haar measure $\lambda$. Since
$\mu\le4\overline\mu$, $\mu$ is absolutely continuous with respect to
$\lambda$. Write $d\mu=f\,d\lambda$, $f\in L^1$. The Fourier coefficients
of an $L^1$ density tend to zero, whereas $T_{16}$-invariance gives
$\widehat\mu(k)=\widehat\mu(16^jk)$ for every $j\ge0$. For $k\ne0$ this
forces $\widehat\mu(k)=0$, hence $\mu=\lambda$.

This use of rigidity retains its positive all-scale collision hypothesis; mere
positive averaged entropy in a nonergodic law is not silently substituted.
Here is the residual step explicitly. Decrease the exponent to $0<s<1$ if
necessary. At depth $k$, the binary cylinder collision sum is at most
$C'2^{-sk}$, so Shannon entropy is at least $sk\log2-\log C'$ and the
invariant measure has entropy at least $s\log2$. The classical nonergodic
Rudolph--Johnson theorem gives $\overline\mu\ge s\lambda$. Its normalized
residual $(\overline\mu-s\lambda)/(1-s)$ has the same two invariances and
collision bound with constant multiplied by $(1-s)^{-2}$. Repetition yields
$\overline\mu\ge[1-(1-s)^j]\lambda$ for every $j$, hence equality with
Haar. Cross terms in the four-phase collision estimate have already been
controlled by convexity and the cellwise Cauchy--Schwarz inequality in TA-10;
they are not being discarded.
The Fourier decay fact follows, for example, by approximating $f$ in $L^1$
by step functions and explicitly integrating each step's Fourier coefficient.

The symmetry condition is strictly weaker at the measure level. Take
$\mu=\delta_{1/5}$. Then $T_{16}\mu=\mu$ and $T_3\mu=\delta_{3/5}\ne\mu$,
but $\overline\mu$ is uniform on $\{1,2,3,4\}/5$ and is $T_3$-invariant.
This control has no positive collision exponent, so it does not contradict
the conditional closure theorem.

### 6.1 The four phases are exactly the deblocked BBP window

For an authentic source window $I=\{A,\ldots,B\}$ of length $N$, let
$\mu_I=N^{-1}\sum_{n\in I}\delta_{y_n}$. The points

$$
\{2^rU_n\},\qquad n\in I,\quad r=0,1,2,3,
$$

have empirical law exactly $\overline\mu_I$ from TA-9. These are rational
source states, with the full integral carries kept. The deblocked unwrapped
source $B_{4n+r}=2^rU_n$ obeys $B_{j+1}=2B_j$ except at a block boundary,
where the additional forcing is precisely $r(n+1)$.

The one-step invariance defect is bounded explicitly:

$$
W_1((T_2)_*\overline\mu_I,\overline\mu_I)
\le\frac14W_1((T_{16})_*\mu_I,\mu_I)
\le\frac1{4N}\sum_{n\in I}r(n+1)+\frac1{8N}.
\tag{TA-11}
$$

The first inequality couples the three identical summands. For the second,
couple $T_{16}y_n$ to $y_{n+1}$ using the actual forcing, then replace the
last point by the first at circle cost at most $1/2$. Thus late long windows
have $T_2$-invariant limiting four-phase laws.

The remaining symmetry test can be written without another orbit construction:
for every fixed nonzero integer $h$, prove

$$
\frac1{4N}\sum_{n\in I}\sum_{r=0}^3
\big[e(3\cdot2^rh y_n)-e(2^rh y_n)\big]\longrightarrow0,
\qquad e(t)=e^{2\pi it},
\tag{TA-12}
$$

on the same selected window family. This allows cancellation among the four
binary phases. The inherited all-scale collision premise is still needed.
Equation TA-12 is the new weaker symmetry target, not an estimate proved by
the Pascal row identity. The circle identity TA-1 makes it exact to evaluate;
TA-8 describes one finite symbolic route to estimating it.

## 7. Verification scope and next falsification opportunity

The mathematical authorities above are the displayed proofs and the explicitly
inherited classical rigidity theorem. A small exact-arithmetic calibration
separately checks the non-dyadic cut counts, their alternating suffix labels,
the Bernoulli formulas, and the periodic four-phase witness. It is not evidence
for the authentic statistical premise at untested indices.

The preserved [carry calibration](../../scripts/pi_ternary_carry_calibration.py) executed **26,165 exact assertions** with integers and
`Fraction` arithmetic. Its scopes were $m=1,\ldots,8$, $L=1,\ldots,12$ for
the tripling cuts; every odd $q=3,5,\ldots,31$, $m=1,\ldots,7$, and six
lookahead lengths starting at $\lceil\log_2q\rceil$ for the general cut count;
six rational Bernoulli biases and alternating-word lengths through 19; and
the exact four-phase orbit modulo 5. Each tripling cut was also bracketed by
two rational points in the same input cell with different output words. The
all-parameter assertions above rest on the proofs, not these finite ranges.

The next useful authentic test is the four-phase defect TA-12 on fresh selected
windows, retaining its sign and comparing with each phase separately. The next
theorem must quantitatively estimate that defect or the finite-block discrepancy
in TA-8. A small source coupling error or a long-run bound by itself is not the
needed cancellation. The biased Bernoulli control must continue to fail any
claim that the general Pascal/carry machinery supplies it automatically.
