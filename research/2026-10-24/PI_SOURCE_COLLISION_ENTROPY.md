# π source collision entropy: a coherent proof target and its exact boundary

**Date:** 2026-10-24. **Research branch:** `research/pi-source-collision-entropy-2026-10-24`.
**Parent:** PR #264, `de005af44cb4592d7a8be73f46fa1983f627da27`.
**Status:** paper proofs and exact finite checks. No new Lean declaration; scholarly originality unverified.
**π normality is OPEN. Independence of π-normality from PA, ZFC, or another theory is NOT ESTABLISHED.**

This round audits the live branches, proves a correction to the regret frontier,
and constructs a source-preserving collision/entropy bridge. Its new averaging
theorem controls the **full** complementary BBP phase. The remaining selected-source
estimate is stated with its quantifiers, rather than silently supplied by an average.

## 1. Live frontier and source provenance

Observed `main` is `b116841f12b41aaf7600da39bbb40577f25b6295`.
Academic Main IX is staged in #250 at `f986507851e34636f60bee657dcdf0771a934380`;
it already incorporates the 28 older research PRs, including #245 and #246.
The new pre-round leaf tips are #255, #259, #260, #261, #262, #263, and #264.
This branch extends #264 only. Siblings were read from their exact Git objects;
their implementations and formal authority are not silently imported.

| Source | Exact head | Contribution used or audited |
|---|---|---|
| #252 | `364962ac0c0e8fb4d06c37468a5d50336d68a9ee` | Correct BBP source, positive Green tail, withdrawal of the false four-pole closure |
| #253 | `2ab8a8527b7ba3f990d75fd618a4bfd034b26b4b` | Signed source transport and carefully scoped Lean authority |
| #254 | `fceb04645926898bb5f72346dca54f3134b06cea` | Source rank/tail duality |
| #256 | `0683f8f166b9106ab8405a2d6538415b5ac84ba3` | First prime window and later p² carry contribution |
| #259 | `a777aa99f541df2a0e2a0b8d57fef3f0940e465c` | Twisted local cancellation, selected-source gap |
| #260 | `654e9c9984ced49cee454d99cff20415072d1ffc` | Moving gauge and missing-prime nonidentification |
| #261 | `4b52cb87a19c2f599e5386fc12a9758bab12cba8` | Galois source family, all-prime births, selected outlier |
| #262 | `34f8e040a6f86a9e583bad428f3d4e20940e1ac8` | First carry, origin moments, no autonomous stable-source intertwiner |
| #263 | `d7b5a5b91d142717ce7898417eed7a5dc603e019` | Exact reachability preservation under observation quotients |
| #264 | `de005af44cb4592d7a8be73f46fa1983f627da27` | Poisson circle energy and regret formulation |

The #259 temporal-character theorem is stronger than the alternate square-root
Gauss bound in #260. #258/#261 forked before the final #256 p² update; PR base
labels alone do not establish ancestry. #260 and #261 independently created
different `bbp_minimal_path.py` modules and reused MP claim identifiers. The
Claude handoff gives a preservation-first integration procedure for these collisions.

The `provenance/IMPORT_MANIFEST.json`, imported archival originals, and their
claim authority are untouched. Mathematical sources are cited at the end.

## 2. Hole contract and the change of proof technology

**Exact target.** Prove π normal to base 16, hence to base 2. Decimal and absolute
normality require additional work: base 16 and base 10 are multiplicatively independent.

**Current frame.** The object is the authentic orbit $x_j=\{16^j\pi\}$; the usual
observable is a signed Fourier sum. Local cyclotomic cancellation is available,
but its coupling to the entire complementary source remains uncontrolled.

**Chosen sufficient statement.** Fix $c=2/5$ before examining samples. For primes
$p=8u+1$ satisfying $L_p=\mathrm{ord}_p(16)>\sqrt p/\log p$, set

$$
d_p=\lfloor c\log_{16}p\rfloor,\qquad M_p=16^{d_p},\qquad \Delta_p=3u.
$$

Let $y_n$ be the exact BBP rational states defined below. The proposed bound is

$$
K_p(1)=\frac{M_p}{\Delta_p^2}
\#\{(s,t)<\Delta_p:
\|y_{u+1+s}-y_{u+1+t}\|_{\mathbb T}\le 1/M_p\}=p^{o(1)}.
$$

The quantifiers mean: for every $\varepsilon>0$ there is $P_\varepsilon$ such
that every such good prime $p>P_\varepsilon$ satisfies $K_p(1)\le p^\varepsilon$.
A bound $K_p(1)\le C(\log p)^A$ would suffice. One fixed positive exponent does not.

**Truth state:** UNVERIFIED. **Dependency cut:** this bound, the proved entropy
bridge, and relative density of good primes imply binary normality. **Novelty
tax:** it is a strict quantitative sufficient condition at a predetermined scale;
normality alone need not satisfy such a scale. It is not a proved weaker statement
than normality, and its establishment for π remains the major arithmetic problem.

**What has actually been paid:** the exact source/carry transport, finite entropy
inequality, good-prime order estimate, and a complement-uniform Galois collision
average. **Cheapest falsifiers:** literal selected-is-average, local-only source
substitution, dropped carries, and omitted repeated-prime phases all have exact
counterexamples. A finite large $K_p(1)$ does not refute a subpower asymptotic.

**Why this is a useful reframe:** collisions retain all cross-clock interactions
in a nonnegative counting problem. They can be attacked by incidence bounds,
source recurrences, or arithmetic counting without first proving individual signed
Fourier cancellations. The change does not make source selection disappear.

## 3. SCE-01 — positive regret is also an equivalence (PROVED PAPER)

For arbitrary circle points $z_j$, let

$$
K(z,w)=\frac3{1+2|z-w|^2},\quad
\mu_n=\frac1n\sum_{j<n}\delta_{z_j},\quad
E_n=\iint K\,d\mu_n\,d\mu_n,\quad
\Phi_n(z)=\sum_{j<n}K(z,z_j).
$$

The Fourier coefficients of $K$ are $2^{-|h|}$. Cauchy–Schwarz gives, uniformly
in the probe point $z$,

$$
\left|\frac{\Phi_n(z)}n-1\right|^2\le 2(E_n-1).
$$

Indeed the sum of the nonzero Fourier weights is 2. Equality holds for a point
mass probed at its own support, so the constant 2 is sharp.

Write $a_n=\Phi_n(z_n)-n$, $R_N=\sum_{1\le n<N}[a_n]_+$, and
$Q_N=\sum_{1\le n<N}(\Phi_n(z_n)-\min_z\Phi_n(z))$. Then

$$
R_N\le\sqrt2\sum_{n<N}n\sqrt{E_n-1},\qquad
Q_N\le2\sqrt2\sum_{n<N}n\sqrt{E_n-1}.
$$

Consequently $E_n\to1$ implies both regret sums are $o(N^2)$. Conversely the
exact identity from #264,

$$
E_N=1+\frac2N+\frac2{N^2}\sum_{n<N}a_n,
$$

and $a_n\le[a_n]_+\le\Phi_n(z_n)-\min\Phi_n$ prove the reverse implications.
Thus weak convergence of $\mu_N$ to Haar, $E_N\to1$, $R_N=o(N^2)$, and
$Q_N=o(N^2)$ are **equivalent**. For an actual base-$b$ orbit each is equivalent
to base-$b$ normality. The positive-regret condition is not an asymptotically
stronger condition that independently advances the proof.

This corrects the description of PGM-05/10 without invalidating their sufficient
implication or finite calculations. The geometric formulation remains useful if
another source theorem controls it. A new name for the same missing limit is not
that source theorem.

## 4. SCE-02 — a finite collision-to-entropy inequality (PROVED PAPER)

Take an infinite word over $b\ge2$ digits. For $N$ consecutive starting positions,
let $p_{N,d}$ be the law of its length-$d$ blocks, including the actual $d-1$
future digits needed at the end. Define

$$
C_{N,d}=b^d\sum_w p_{N,d}(w)^2.
$$

For fixed $k\le d$, put $q=\lfloor d/k\rfloor$, $\delta=d/N\le1/2$, and
$\eta_k(\delta)=h_2(\delta)+\delta\log(b^k-1)$, using natural logarithms.
Then

$$
D(p_{N,k}\Vert u_{b^k})\le
\frac{\log C_{N,d}}q+\eta_k(d/N).
$$

**Proof.** Partition a random observed $d$-block into $q$ consecutive $k$-blocks
and a remainder. At internal offset $rk$, its $k$-block law differs from
$p_{N,k}$ by total variation at most $rk/N$: only the ends of the starting window
changed. Entropy continuity and subadditivity imply

(The continuity bound follows by maximally coupling two laws: reveal whether
their symbols differ, costing at most $h_2(\delta)$, and on disagreement reveal
one of at most $b^k-1$ alternatives, costing at most $\delta\log(b^k-1)$.)

$$
H(p_{N,d})\le qH(p_{N,k})+q\eta_k(d/N)+(d-qk)\log b.
$$

Jensen's inequality gives $H(p_{N,d})\ge-\log\sum_w p_{N,d}(w)^2
=d\log b-\log C_{N,d}$. Combine the two bounds and divide by $q$.
Pinsker's inequality gives total variation at most the square root of half the
displayed KL bound. These are classical entropy tools with their finite
starting-window error made explicit.

**Corollary.** If $d(N)\to\infty$ and $\log C_{N,d(N)}/d(N)\to0$ through all
sufficiently large horizons, the word is normal. The apparently additional
condition $d=o(N)$ is automatic: there are at most $N$ sampled words, so
$C_{N,d}\ge b^d/N$, and the premise forces $d\le(1+o(1))\log_b N$.
The proof applies unchanged to windows whose starting position depends on $N$;
its conclusion there is convergence of those windows' fixed-block laws.

The finite collision count includes the diagonal. It is never legitimate to
discard self-pairs when assessing a claimed high-resolution bound.

### SCE-03 — fixed logarithmic scale is strictly stronger (PROVED PAPER)

Let $B_k$ be a cyclic de Bruijn word of order $k$, of period $b^k$. Concatenate
stage $k$ consisting of $B_k$ repeated $b^{k^2-k}$ times. Its length is $b^{k^2}$.
The resulting word is normal. For each fixed block length $\ell$, complete
cycles in stages $k\ge\ell$ have the exact $\ell$-block frequencies. Errors from
the last partial cycle are $O(b^k)$, and stage joins contribute $O(k\ell)$.
Even at the beginning of stage $k$, the earlier length is at least
$b^{(k-1)^2}$, so these relative errors vanish.

At the endpoints $N_k=\sum_{j\le k}b^{j^2}$, the final stage has mass $1-o(1)$
but its interior $d$-blocks occupy at most $b^k$ words. Hence
$C_{N_k,d}\ge b^{d-k}(1-o(1))^2$. For any fixed
$d=\lfloor c\log_b N_k\rfloor\sim ck^2$,

$$
\frac{\log C_{N_k,d}}d\longrightarrow\log b,
$$

not zero. Thus the prescribed-scale collision condition has extra content. An
arbitrarily slow source-adapted schedule would only recover an equivalent
criterion by diagonalization. An arbitrary favorable subsequence is also
insufficient; control must cover all horizons or a relatively dense cofinal set.

The same example directly tests the prime-window schedule used below. Set
$b=16$ and choose good primes $p_k\sim(8/5)N_k$, available by SCE-06. Then
$u_k=(p_k-1)/8\sim N_k/5$, so the entire window $[u_k,4u_k)$ and its
$d_{p_k}-1$ future digits lie inside stage $k$. Its blocks occupy at most
$16^k$ labels. Its scaled small-ball count is at least its cell collision,
which is at least $16^{d_{p_k}-k}$. Since $d_{p_k}\sim ck^2$, its collision
logarithm divided by $d_{p_k}$ tends to $\log16$, despite normality. This is a
different source, and establishes strictness of the prescribed observation
criterion in general; it does not counterfeit the authentic BBP law.

## 5. SCE-04 — exact BBP source and carry-safe collision transport (PROVED PAPER)

Use the classical BBP identity in its actual index variable:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
y_0=0,\quad y_n=\{16y_{n-1}+r(n)\}.
$$

Its Green tail is

$$
t_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
\{y_{n+1}+t_{n+1}\}=\{16^n\pi\}.
$$

For completeness, the positive source representation is

$$
t_n=\int_0^1\frac{t^{8n}(4-2t^3-t^4-t^5)}{16-t^8}\,dt.
$$

The numerator is $(1-t)(4+4t+4t^2+2t^3+t^4)$. The second factor is positive and
at most 15, while $16-t^8\ge15$. Therefore, for every $n\ge0$,

$$
0<t_n<\int_0^1t^{8n}(1-t)\,dt
=\frac1{(8n+1)(8n+2)}.
$$

These are source identities and all-$n$ bounds, not numerical fits. A forced
recurrence/normality correspondence has classical ancestry in Bailey–Crandall;
the relevant theorem is not newly invented here.

**Carry lemma.** Suppose two finite samples obey $x_i=y_i+e_i\pmod1$ with
$0\le e_i<1/M$. Let $C_M$ denote $M$ times the squared cell-mass sum for the
uniform $M$-cell partition. Then

$$
\frac12 C_M(y)\le C_M(x)\le2C_M(y).
$$

**Proof.** Each source cell sends mass only to itself and its next cell, including
wraparound. If $a_j,b_j$ are the two nonnegative pieces of the mass in source
cell $j$, its destination mass is $a_j+b_{j-1}$. Thus
$\sum_j(a_j+b_{j-1})^2\le2\sum_j(a_j^2+b_j^2)
\le2\sum_j(a_j+b_j)^2$. Reverse the allocation to obtain the other inequality.
The factor 2 is sharp: two equal masses in adjacent cells can move into one cell.

No digit-boundary avoidance assumption is used. The count retains the carry
state rather than suppressing it. For source phases in the first prime window
below, $e_i\le t_{u+1}<1/((p+8)(p+9))$ (the positive integral is decreasing in
its index), so the hypothesis holds for every
$M\le(p+8)(p+9)$. In particular it holds for the predetermined $M_p$.

An alternative for signed or less precise tails is the direct small-ball
inclusion $Q_x(\tau)\le Q_y(\tau+2\epsilon)$ when every circular displacement
is at most $\epsilon$. The widened radius must be retained until paid for.

## 6. SCE-05 — full-source Galois collision counting (PROVED PAPER)

Take $p=8u+1$ prime. Put $L=\mathrm{ord}_p(16)$ and $\Delta=3u$. Quadratic
reciprocity gives $(2/p)=1$, so $16^u=1\pmod p$ and $L\mid u$.
The first denominator divisible by $p$ in the forcing is $8(u+1)-7=p$.
The next is $8(4u+1)-4=4p$. Hence, throughout $0\le t<3u$,

$$
y_{u+1+t}=\frac{4\,16^t}{p}+w_t\pmod1,
$$

where every $w_t$ has denominator prime to $p$. The complete complement is
kept, including its numerator, all other prime powers, and CRT interactions.
Define its actual relative cyclotomic Galois family

$$
z_t(a)=\frac{4a16^t}{p}+w_t\pmod1,\quad 1\le a<p,
$$

and $Q_p(a,\tau)=\Delta^{-2}\#\{(s,t):\|z_s(a)-z_t(a)\|_{\mathbb T}\le\tau\}$.
For $0\le\tau<1/2$, writing $v=\lfloor2p\tau\rfloor$, one has

$$
\left(1-\frac1L\right)\max\left(0,\frac{v-1}{p-1}\right)
\le\frac1{p-1}\sum_{a=1}^{p-1}Q_p(a,\tau)
\le\frac1L+\left(1-\frac1L\right)\min\left(1,\frac{v+1}{p-1}\right).
$$

**Proof.** Every local phase appears $\Delta/L$ times. Exactly $\Delta^2/L$
ordered pairs therefore have identical local $p$-phase; their contribution is
between 0 and 1. For each remaining pair the nonzero coefficient of $a$ runs
through all nonzero residues. Its difference phases form a translated $p$-grid
with one point removed. A closed circular arc of length $2\tau<1$ contains
between $v$ and $v+1$ points of the full grid; deleting one point gives the
stated bounds. Sum over pairs. No BGK estimate or independence premise is used.

Therefore, whenever $M\to\infty$ and $M=o(L)$,

$$
\frac1{p-1}\sum_{a=1}^{p-1}M Q_p(a,1/M)\longrightarrow2,
$$

uniformly over **all** complementary phases. This theorem includes the authentic
BBP complement; it does not replace it with a product distribution.
For $M\asymp p^c$, Markov consequently gives a proportion $O(p^{-\varepsilon})$
of embeddings with scaled collisions greater than $p^\varepsilon$.
It supplies no certificate that the selected embedding $a=1$ avoids them.

## 7. SCE-06 — a density-one prime-order bound (PROVED PAPER)

For fixed base 16,

$$
\#\{p\le X:\mathrm{ord}_p(16)\le\sqrt p/\log p\}
=O\left(\frac X{(\log X)^3}\right),
$$

ignoring the one nonunit prime 2. On a dyadic shell $(X/2,X]$, put
$A=\lfloor\sqrt X/\log(X/2)\rfloor$. Every bad prime divides
$\prod_{j\le A}(16^j-1)$, so

$$
(\#\text{bad})\log(X/2)
\le\log\prod_{j\le A}(16^j-1)
<\frac{\log16}{2}A(A+1).
$$

The shell bound follows by division. Summing shells down to $\sqrt X$ and
bounding the remaining primes by $\sqrt X$ proves the claim.

The classical prime number theorem for the fixed progression $1\pmod8$ gives
asymptotically $X/(4\log X)$ eligible primes. Removing the above exceptional
set leaves a good prime in every interval $[X,(1+\epsilon)X]$ for all large
$X$ and each fixed $\epsilon>0$. Consecutive good primes thus have ratio tending
to 1. For every fixed $0<c<1/2$, $M_p\asymp p^c=o(L_p)$ on this family.
No primitive-root conjecture, RH assumption, or selected-orbit genericity is used.

## 8. SCE-07 — the complete conditional bridge to binary normality

**PROVED CONDITIONAL.** If the hole contract's exact-source bound
$K_p(1)=p^{o(1)}$ holds on all sufficiently large good primes, π is normal
in base 16 and therefore base 2.

**Proof.** Use the $M_p=16^{d_p}$ cells and the true orbit window
$x_u,\ldots,x_{4u-1}$. The carry lemma and same-cell-to-small-ball inclusion give

$$
C_{\Delta_p,d_p}(\text{true π window})
\le2C_{M_p}(y_{u+1},\ldots,y_{4u})\le2K_p(1).
$$

Since $d_p\asymp\log p$ and $\Delta_p\asymp p$, the entropy theorem proves
uniformity of every fixed digit-block law on these windows. Their starts $u$
are relatively dense by SCE-06. For any bounded centered fixed-block indicator
$f_j$, write $W(n)=\sum_{n\le j<4n}f_j$. Approximating any large $n$ by a good
start $u$ with $u/n\to1$ changes the sum by at most $5|u-n|\sup|f|$, so
$W(n)=o(n)$ for all $n$.

Let $S(N)=\sum_{j<N}f_j$. For $N=4n+r$, $0\le r<4$,
$S(N)=S(n)+W(n)+O(1)$. Repeated division by 4 and a geometric-series bound
give $S(N)=o(N)$. All fixed digit blocks have their correct limiting frequency.
Normality in multiplicatively dependent integer bases gives the binary conclusion.

The proof uses no unknown zero coordinates and no RH implication. It does not
prove the selected collision hypothesis. It also does not prove decimal normality.

## 9. SCE-08/09 — why the averaged theorem still cannot select π

### The p-free aligned counterfeit (PROVED PAPER, REFUTATION of local-only inference)

Choose an integer $q>2M$ coprime to $p$. For each $t$, round $-4\,16^t/p$
up to the nearest $q$-grid point and call the result $\widetilde w_t$. Every
complementary denominator is prime to $p$, while all selected phases
$4\,16^t/p+\widetilde w_t$ lie in one interval of length $1/q<1/M$.
Their scaled collision is exactly $M$. The Galois average theorem still holds.

This counterfeit changes the complete BBP source. It proves that the p-free
condition, local order, and ensemble estimate alone are insufficient. It is
not another false claim that a rational fixed point shares π's full source.

### Entropy cost of changing the selected conjugate (PROVED PAPER)

The $a$-window differs from the selected one by a periodic translation of period
dividing $L$. Let $X$ and $Y$ be their cell labels at a uniformly sampled time,
and $R$ the time modulo $L$. Given $X,R$, at most two labels $Y$ are possible,
because one boundary carry remains. Thus

$$
H(Y)\le H(X)+\log L+\log2.
$$

Even $H(Y)\approx\log M$ yields only
$H(X)\ge\log M-\log L-\log2$, which is vacuous in the averaging theorem's
regime $M=o(L)$. The local prime clock can supply the whole observed entropy.
This is an explicit information cost, not an appeal to unspecified randomness.

Each associated complete orbit is a rational translate of π. Rational
translation preserves normality for a fixed translate, but the translating
rational and the observed horizon here depend on $p$. That invariance theorem
does not authorize exchanging these limits.

### Why the ordinary absolute Fourier budget is not obviously easier

For arbitrary unit weights, Haar-averaged lacunary phases have second moment
$1/\Delta$ and fourth moment at most $2/\Delta^2$. Consequently the expected
nonzero temporal Fourier mass on an $L$-clock is at least
$(L-1)/\sqrt{2\Delta}$. For $\Delta=BL$ with bounded $B$, this is order
$\sqrt L$, not a small norm. This standard moment calculation explains why
short source description does not imply small absolute spectral mass. It does
not prove that π realizes this obstruction or that bounded-$B$ primes are infinite.

## 10. SCE-10 — what can and cannot be called unknowable

Every finite digit prefix has a computable normal extension (append a
Champernowne sequence) and a computable irrational nonnormal extension (put
ones at factorial positions and zeros elsewhere). Finite edits preserve either
normality or nonnormality, so adaptive finitely many digit queries also cannot
decide the property for all inputs. This is an observer-relative no-go theorem.
The two extensions do not preserve π's exact source.

Becher–Heiber–Slaman, Theorem 3.2, prove a stronger **general** obstruction:
every arithmetic $\Pi^0_3$ sentence can be computably transformed into a
computable real that is absolutely normal if the sentence is true and
absolutely abnormal otherwise. Their Corollary 3.4 also covers any fixed base.
Thus no universal algorithm decides normality from an arbitrary real-computing
program. This is an attributed published theorem, not a new SUCC independence proof.

A genuine π independence claim must specify a theory $T$, the formal sentence
for normality, and metatheoretic assumptions under which neither that sentence
nor its negation is provable in $T$. No inspected result or result here supplies
that theorem. Failure of a source quotient, finite experimental saturation,
general undecidability, and failure of one analytic criterion are different claims.

The base-$b$ normality sentence can be written as all block lengths/words and
all rational error tolerances, followed by an eventual horizon and all later
horizons. Its decidable finite count predicate is accessible from π's computable
digits. This explains the quantifier structure; it does not establish independence.

## 11. Experiments, controls, and current verdict

The production module uses exact BBP fractions and a sorted circular-pair
counter. An independent oracle uses direct all-pair enumeration and a different
pairwise Galois-grid aggregation. Independent Machin alternating-series intervals
certify actual π cell labels and verify the one-cell carry assertion. No supplied
π digit file, floating sign decision, or assumed genericity is an input.

The finite suite checks: polynomial versus partial-fraction forcing; first-birth
source reconstruction; p-free complement; complete-period multiplicity; sorted
versus exhaustive pairs with duplicate/wrap/threshold cases; the Galois bounds;
sharp carry transport; actual π bins; positive tail bounds; and hostile controls.

Controls include an omitted equal-phase term (wrong bound $1/16$ versus actual
$1/2$), a weakened carry constant, a source-aligned p-free counterfeit, an
underresolved π interval, a truncated Poisson kernel, and a weakened potential
constant. The independently generated regret receipt verifies 6,240 potential
inequalities, 780 energy identities, and 2,150 one-step bounds.

At $p=97,M=16$, the exact selected scaled close-pair count is $80/27$, while
the Galois mean is $4615/1944$. Thus selected-is-at-most-average is already
false in this collision observable. This finite outlier is fully compatible
with the open subpower bound. Additional prime windows and larger exact source
holdouts are recorded in `PI_SOURCE_COLLISION_RECEIPT.json`; they are diagnostics,
not fitted exponents or evidence sufficient for the all-prime limit.

**Dominance boundary.** This machinery unifies the actual BBP source, carry-safe
observation, cyclotomic symmetry, local-to-global window coverage, and entropy.
It proves a full-source averaged theorem and a complete conditional route. It
does not eliminate the selected-source arithmetic problem. The next major theorem
must estimate the actual pair count, or provide an explicit counterexample to
the prescribed sufficient bound. Another equivalent energy or Fourier criterion
does not discharge that obligation.

## 12. Primary references and prior-art boundary

1. Bailey, Borwein, Plouffe, *On the Rapid Computation of Various Polylogarithmic
   Constants* (1997), Theorem 1, original BBP identity:
   <https://www.davidhbailey.com/dhbpapers/digits.pdf>.
2. Bailey, Crandall, *Random Generators and Normal Numbers*, author's 2003
   version, Theorem 3.1 and explicitly conjectural Hypothesis A:
   <https://www.davidhbailey.com/dhbpapers/bcnormal.pdf>.
3. Bailey, Misiurewicz, *A Strong Hot Spot Theorem* (2006), especially weak-hot-spot
   Theorem 1.1 and the stronger nested conclusion:
   <https://www.davidhbailey.com/dhbpapers/dhb-mm-hotspot.pdf>.
4. Bourke, Hitchcock, Vinodchandran, *Entropy Rates and Finite-State Dimension*;
   classical entropy/finite-state background, not the selected-source estimate:
   <https://www.eecs.uwyo.edu/~jhitchco/papers/erfsd.shtml>.
5. Becher, Heiber, Slaman, *Normal numbers and the Borel hierarchy*,
   Fundamenta Mathematicae 226 (2014), Theorem 3.2 and Corollary 3.4:
   <https://math.berkeley.edu/~slaman/papers/pi3.pdf>.
6. Kedlaya, *Notes on analytic number theory*, §4.4, fixed-modulus PNT:
   <https://kskedlaya.org/ant/chap-primes-in-ap.html>.

The conditional synthesis, carry estimate, elementary order strengthening, and
finite Galois bounds have explicit proofs above. Their scholarly priority has
not been established. This document does not claim a newly solved classical
problem, a new Lean theorem, or a physical law of minimality.
