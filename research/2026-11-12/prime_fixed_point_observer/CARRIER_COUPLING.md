# Shared carrier, information cost, and arithmetic coupling

Research addendum to [THEOREMS.md](THEOREMS.md) and
[CYLINDER.md](CYLINDER.md), based on the published dossier at commit
836d03806183c1f73488dca1d37e149a9826eb53.

**Status.** The information identities are classical consequences of finite
entropy and coding theory. The operator and generating-series statements below
have explicit elementary proofs in their stated domains. This document makes
no historical novelty claim, no physical-carrier identification, and no
Goldbach, pi-normality, or RH proof claim. Same-model review and finite replay
are separate from formal-kernel certification.

The motivating proposal is to describe objects as patterns and disturbances
in a common carrier, with the carrier's rules and couplings represented once.
The strongest justified version has two parts:

1. Shared structure can save description length relative to a specified
   independently decoded representation.
2. An arithmetic observation must preserve the coupling between multiplicative
   structure and ordinary additive position if its conclusion depends on that
   coupling.

The first is a coding comparison. The second is an information-sufficiency
requirement. Neither, alone, proves that every description using objects is
inefficient or that every proof formulated with objects must fail.

## Hole contract

| Item | Precise commitment |
|---|---|
| Object | Finite joint observations, computable finite arithmetic records, and the ordinary anchored carrier on the positive integers |
| Proposed local statements | Exact coding gains with the carrier cost included; rigidity from the successor/multiplier coupling; faithful joint arithmetic coefficients |
| Current truth state | CAR-01 through CAR-10 below have written proofs within their stated domains; the universal additive lower bound remains OPEN |
| Quantifiers | Entropy identities hold for every declared finite joint law; rigidity holds for every bounded operator satisfying the anchor and intertwining equations; coefficient identities hold for every integer target at least 4 |
| Weakest sufficient distributional target | An independently derived positive lower bound for every sufficiently large even sum, with a stated finite exceptional range |
| Dependency edge | Authentic source and retained coupling -> quantitative two-sided overlap -> nonempty prime-pair fibers |
| Novelty tax | The assertion that the exact pair coefficient is positive for every even target is Goldbach-equivalent. Re-encoding that coefficient does not pay for its positivity |
| Cheapest falsifiers | Independent variables; an unnecessarily large carrier; equal information measures with opposite overlap; an anchor-free multiplier; transported multiplication with the ordinary successor retained |
| Finite boundary | Every finite coefficient can be computed and certified. A directed limit or an increasing test range is not itself a uniform arithmetic proof |
| Next discriminating probe | Require a proposed estimate to distinguish the ordinary and transported joint sources before treating it as an estimate of ordinary additive overlap |

The companion [carrier_probe.py](carrier_probe.py) and
[finite carrier report](receipts/CARRIER_REPORT.json) record finite checks
separately. No universal claim below rests on a test count.

## 1. Shared structure has an exact finite information cost

All entropies in this section are in bits. Let
$X=(X_1,\ldots,X_m)$, with $m\ge1$, have a declared joint probability
distribution on finite alphabets. Use the convention $0\log 0=0$.

The comparison is between an ideal joint code and codes that describe each
marginal separately:

$$
L_{\rm joint}=H(X),\qquad
L_{\rm sep}=\sum_{i=1}^{m}H(X_i).
$$

Here “separate” means that each marginal has its own self-contained code.
It does not include every possible distributed encoder with a joint decoder,
nor a description that already retains a shared generative program.

**CAR-01 — CLASSICAL IDENTITY, proof restated.** Define total correlation by

$$
\operatorname{TC}(X)
=
\sum_i H(X_i)-H(X).
$$

Then

$$
\boxed{
L_{\rm sep}-L_{\rm joint}
=
\operatorname{TC}(X)
=
D_{\rm KL}\!\left(P_X\middle\|\prod_iP_{X_i}\right)
\ge0.
}
$$

Equality holds exactly when the variables are mutually independent.

**Proof.** On every tuple of positive joint probability, all corresponding
marginal probabilities are positive. Expanding the logarithm in the relative
entropy gives

$$
\begin{aligned}
D_{\rm KL}\!\left(P_X\middle\|\prod_iP_{X_i}\right)
&=\sum_xP_X(x)\log_2P_X(x)
-\sum_i\sum_xP_X(x)\log_2P_{X_i}(x_i)\\
&=-H(X)+\sum_iH(X_i).
\end{aligned}
$$

Nonnegativity of relative entropy follows from the log-sum inequality;
its equality condition gives the independence statement. QED.

This gives a rigorous saving for shared statistical structure relative to the
specified separate baseline. The size of a state space, by itself, does not
force a strict saving.

### Encoding the carrier rather than assuming it for free

Let $C$ be another finite random variable on the same probability space.
Consider the particular two-stage architecture that first encodes $C$, then
encodes each $X_i$ conditionally on that carrier:

$$
L_C=H(C)+\sum_iH(X_i\mid C).
$$

For this operational interpretation, the encoder must have access to the
carrier value or a declared method of obtaining it. The probability law and
the coding procedure must also be available to both sides.

Define conditional total correlation as

$$
\operatorname{TC}(X\mid C)
=
\sum_iH(X_i\mid C)-H(X\mid C).
$$

It is the average, over $C$, of the relative entropy of the conditional
joint law against the product of its conditional marginals, and is
nonnegative.

**CAR-02 — CLASSICAL CHAIN-RULE CONSEQUENCE, proof stated.**

$$
\boxed{
L_C-H(X)
=
H(C\mid X)+\operatorname{TC}(X\mid C).
}
$$

Consequently,

$$
\boxed{
L_{\rm sep}-L_C
=
\operatorname{TC}(X)
-
H(C\mid X)
-
\operatorname{TC}(X\mid C).
}
$$

**Proof.** Add and subtract $H(X\mid C)$, then use
$H(C)+H(X\mid C)=H(X)+H(C\mid X)$. QED.

The formula accounts for two distinct costs. The carrier may contain
information that cannot be recovered from the requested observations,
measured by $H(C\mid X)$. The conditionally separate residual codes may
still duplicate dependencies, measured by $\operatorname{TC}(X\mid C)$.
A good carrier can eliminate both costs, but an arbitrary carrier need not.

If the residual observations are encoded jointly conditional on $C$, their
ideal rate becomes $H(C)+H(X\mid C)$; the conditional-total-correlation
penalty disappears. If also $C$ is a deterministic function of $X$, the
resulting rate is exactly $H(X)$.

### What these ideal lengths mean operationally

For independent repetitions of the declared joint source, the entropy
expressions are asymptotically achievable rates per observation. With block
length $b$, a binary prefix code for one finite source has expected length
at least its entropy and less than entropy plus one. Thus the expected
overhead for one joint block can be less than one bit; separate marginal
blocks can add fewer than $m$ bits; the carrier plus $m$ conditional
blocks can add fewer than $m+1$ bits. Dividing by $b$ makes these overheads
vanish. Operational use presumes that the declared codes can be constructed.

These are not exact integer code lengths for every individual realization.
Headers, model descriptions, dictionaries, carrier parameters, and any
previously unavailable side information must be charged to an actual archive
or transmission. A model known to both parties is explicitly conditioned on;
it has not been proved to cost nothing in every application. No uncomputable
parameter or infinite lookup table is granted as a free decoder.

The underlying finite entropy and lossless-coding framework is classical
[Shannon][shannon]. The displayed carrier identities are direct chain-rule
calculations. They are not measurements of the information content of the
physical universe.

## 2. Controls: sharing can help, do nothing, or hurt

**CAR-03 — PROVED FINITE CONTROLS.** The following examples determine the
scope of the preceding claims.

| Control | Variables and carrier | Exact ideal lengths | Verdict |
|---|---|---|---|
| Shared content | $X_i=Z$, where $Z$ is a uniform $L$-bit string; $C=Z$ | $L_{\rm sep}=mL$, $H(X)=L_C=L$ | Saving $(m-1)L$ |
| Independent null | Independent fair bits $X_1,\ldots,X_m$; $C$ constant | $L_{\rm sep}=H(X)=L_C=m$ | No saving |
| Unnecessarily large carrier | $X_1=X_2=Z$; $Z,U_1,U_2$ independent fair bits; $C=(Z,U_1,U_2)$ | $L_{\rm sep}=2$, $H(X)=1$, $L_C=3$ | Carrier code is worse than both baselines |

For the first example, the decoder receives one $L$-bit value and uses the
known replication rule. That comparison presumes a receiver that can retain
shared information. Requiring separate receivers with no shared state would
change the decoding interface and its resource constraints.

For the third example, $H(C\mid X)=2$ and
$\operatorname{TC}(X\mid C)=0$. The extra latent bits explain the entire
two-bit excess over the ideal joint code.

### An information saving does not determine the required coupling

Let $B$ be a fair bit. Compare

$$
(X_1,X_2)=(B,B)
\quad\text{and}\quad
(Y_1,Y_2)=(B,1-B).
$$

Both models have marginal entropies $1,1$, joint entropy $1$, and total
correlation $1$. Both admit the one-bit carrier $C=B$. Nevertheless,

$$
\mathbb E[X_1X_2]=\tfrac12,
\qquad
\mathbb E[Y_1Y_2]=0.
$$

**Proof.** The first model has the equiprobable outcomes $00,11$; the
second has $01,10$. Their entropy calculations agree, while the event that
both coordinates equal one occurs only in the first model. QED.

Thus the amount of shared information does not specify whether the particular
overlap needed by a proof is positive. The labeled relation matters.

Higher-order structure can also escape pairwise inspection. If $B_1,B_2$
are independent fair bits and

$$
(X_1,X_2,X_3)=(B_1,B_2,B_1\mathbin{\oplus}B_2),
$$

every pair is independent, but the triple has joint entropy $2$ and total
correlation $1$. No claim of mutual independence follows from pairwise
independence alone.

## 3. Finite algorithms, model costs, and representation invariance

Shannon entropy concerns a declared probability law. For one particular
finite record, prefix Kolmogorov complexity provides a different comparison.

Fix a universal prefix machine and a finite auxiliary input $a$. Write
$K(x\mid a)$ for conditional prefix complexity. All constants below are
independent of the particular data, but may depend on the fixed machine and
fixed decoding or translation routines.

**CAR-04 — CLASSICAL DESCRIPTION PRINCIPLES, elementary consequences.**
Suppose a fixed computable decoder reconstructs $x$ from a carrier $c$,
a residual record $r$, and $a$. Then

$$
\boxed{
K(x\mid a)
\le
K(c\mid a)+K(r\mid c,a)+O(1).
}
$$

**Proof.** Concatenate a self-delimiting program producing $c$ with a
self-delimiting conditional program producing $r$, then apply the fixed
decoder. QED.

If the decoding rule itself varies with the data, its description must be
included. This is an upper bound from a two-part program; it is not an
unqualified exact chain-rule equality.

Now let $E$ be a fixed computable re-encoding with a fixed computable inverse
on its range. Then

$$
K(E(x)\mid a)\le K(x\mid a)+O(1),
\qquad
K(x\mid a)\le K(E(x)\mid a)+O(1),
$$

and hence

$$
\boxed{
K(E(x)\mid a)=K(x\mid a)+O(1).
}
$$

**Proof.** Append the fixed forward translator in one direction and the fixed
inverse translator in the other. QED.

A lossless change from labeled records to a carrier description therefore
cannot yield an unbounded intrinsic advantage over the best unrestricted
program descriptions in a computationally equivalent language. It can yield
large savings against explicit tables, independently decoded records, limited
model classes, or implementations that fail to reuse their common structure.
It can also change runtime, memory locality, and query cost; none of those
costs is controlled by the preceding unbounded-time description-length
identity.

The two-part model/data viewpoint is developed in
[Gács, Tromp, and Vitányi][algorithmic-statistics]. Prefix complexity,
computable translation, invariance, and the limits of computing shortest
descriptions are treated in [Gács's notes][gacs]. No algorithm for finding a
globally shortest carrier is supplied here.

### A finite description of growing arithmetic records

Let $A_M$ be a fixed canonical finite record containing the labels
$0,\ldots,M$, their addition and multiplication tables for arguments in that
range, and their primality bits. The output format includes enough information
to recover $M$.

A single program computes $A_M$ from $M$, using ordinary finite arithmetic
and trial division. Therefore

$$
K(A_M\mid M)=O(1),
\qquad
K(A_M)=K(M)+O(1).
$$

The reverse bound in the second equality follows because $M$ is recoverable
from $A_M$.

This formalizes one useful sense in which the carrier's rules can be stored
once while its observed region grows. The record contains finitely decidable
data; it does not contain every true sentence about arithmetic. A short
generator supplies neither a short running time nor a proof of a universal
prime-distribution statement.

There is no countably additive uniform probability on all of
$\mathbb N$ assigning equal masses to individual integers: a positive common
mass gives an infinite sum, and zero common mass gives total mass zero.
Entropy claims about arithmetic consequently require a declared finite
observation distribution or a justified nonuniform model. Cardinality alone
does not establish the proposed information inequality.

## 4. The anchored carrier fixes the multiplicative embedding

Let

$$
\mathcal H=\ell^2(\mathbb N_{\ge1}),\qquad
S e_n=e_{n+1}.
$$

The vector $e_1$ is cyclic for this unilateral shift:
$e_n=S^{n-1}e_1$.

**CAR-05 — PROVED LOCAL (anchored rigidity and its stability bound).**
Fix an integer $m\ge1$. If a bounded linear operator $V$ satisfies

$$
V e_1=e_m,
\qquad
VS=S^mV,
$$

then

$$
\boxed{V e_n=e_{mn}\quad\text{for every }n\ge1.}
$$

**Proof.** Repeated intertwining gives

$$
V e_n
=
VS^{n-1}e_1
=
S^{m(n-1)}Ve_1
=
S^{m(n-1)}e_m
=
e_{mn}.
$$

The basis vectors span a dense subspace; boundedness makes the operator
uniquely determined on all of $\mathcal H$. QED.

The anchor is essential. For $m\ge2$, the isometry

$$
W_m e_n=e_{m(n-1)+1}
$$

satisfies $W_mS=S^mW_m$, but $W_me_1=e_1\ne e_m$. Intertwining alone
does not determine the intended multiplication operator.

Similarly, any bounded $U$ satisfying

$$
US=SU,\qquad Ue_1=e_1
$$

must equal the identity. Apply the equations to $S^{n-1}e_1$, then use
density. In particular this holds for a unitary relabeling. Retaining both the
successor and the distinguished origin removes this relabeling freedom.

### Approximate compatibility has an explicit finite scope

Suppose instead

$$
\|Ve_1-e_m\|\le\varepsilon,\qquad
\|VS-S^mV\|\le\delta.
$$

For every $n\ge1$,

$$
\boxed{
\|Ve_n-e_{mn}\|
\le
\varepsilon+(n-1)\delta.
}
$$

**Proof.** For $k=n-1$, telescope:

$$
VS^k-S^{mk}V
=
\sum_{j=0}^{k-1}
S^{mj}(VS-S^mV)S^{k-1-j}.
$$

Every shift power has norm one. Apply the identity to $e_1$, bound the sum
by $k\delta$, and add the anchor error. QED.

This is a bound on each basis vector. It must not be reported as the same
operator-norm bound on arbitrary superpositions in a finite window. For
example, a crude bound on the span of $e_1,\ldots,e_M$ incurs an additional
factor $\sqrt M$. A fixed nonzero tolerance also does not imply uniform
closeness at arbitrarily large labels.

### Coherent coordinate transport preserves the observation

For a unitary $U$, transport the entire package:

$$
e'_1=Ue_1,\quad S'=USU^*,\quad V'_m=UV_mU^*,
\quad P'_N=UP_NU^*,\quad J'_N=UJ_NU^*.
$$

The finite window and sum observation are transported as well. Then

$$
P'_NJ'_NP'_N=U(P_NJ_NP_N)U^*
$$

and finite-rank trace invariance gives

$$
\operatorname{Tr}\!\left((P'_NJ'_NP'_N)^2\right)
=
\operatorname{Tr}\!\left((P_NJ_NP_N)^2\right).
$$

A changed answer results when some structure is changed while the intended
additive carrier is retained. It is not produced by a coherent change of
coordinates of the entire model.

The Hilbert basis labels here are alternatives within one carrier. They are
not automatically separate tensor factors, independently sampled random
variables, or independent physical subsystems.

## 5. A joint position–degree source retains the relevant coupling

For $n\ge2$, define the multiplicative degree

$$
\Omega(n)=\max\{r:n=a_1\cdots a_r,\ a_i\ge2\}.
$$

It equals the number of prime factors counted with multiplicity. In
particular, $\Omega(n)=1$ exactly at primes.

For an integer cutoff $X\ge2$, put

$$
Z_X(z,w)=\sum_{n=2}^{X}z^n w^{\Omega(n)}.
$$

The two exponents record ordinary position and multiplicative degree in the
same term.

**CAR-06 — PROVED LOCAL (joint coefficient and wave representation).**
For every integer $N\ge4$ and $X\ge N-2$,

$$
\boxed{
R(N)=[z^Nw^2]\,Z_X(z,w)^2,
}
$$

where $R(N)$ counts ordered ordinary-prime pairs with sum $N$.

**Proof.** A term in the square has exponents
$(a+b,\Omega(a)+\Omega(b))$. Its first exponent equals $N$ precisely at
the desired sum. Both degree terms are at least one, so the second exponent
equals two precisely when both endpoints are prime. Every candidate endpoint
is at most $N-2$. QED.

Equivalently, for the finite wave

$$
\Psi_X(\alpha,\beta)
=
\sum_{n=2}^{X}
e^{2\pi i(n\alpha+\Omega(n)\beta)},
$$

Fourier orthogonality gives

$$
R(N)=\int_0^1\int_0^1
\Psi_X(\alpha,\beta)^2
e^{-2\pi i(N\alpha+2\beta)}
\,d\alpha\,d\beta.
$$

The square is essential. The absolute square records differences
$(a-b,\Omega(a)-\Omega(b))$, rather than the required sums. The unit is
excluded because degree zero combined with degree two would admit a
unit/semiprime pair.

The infinite formal series

$$
Z(z,w)=\sum_{n=2}^{\infty}z^n w^{\Omega(n)}
$$

is well-defined in $\mathbb Z[w][[z]]$. Each coefficient of its square
depends on finitely many summands.

There is no corresponding Euler-product identity in this ordinary additive
variable $z$. The formal product

$$
\prod_{p\text{ prime}}(1-wz^p)^{-1}
$$

counts additive prime partitions, weighted by their number of summands. Its
$z^5w^2$ coefficient is one, from $2+3$, whereas the same coefficient in
$Z$ is zero because $\Omega(5)=1$. The relation $z^az^b=z^{a+b}$ must not
be silently replaced by multiplication of integer labels. This control keeps
the additive and multiplicative roles of the two-variable source explicit.

An undamped infinite wave on the two-torus has not thereby been shown to
converge as an ordinary function. A safe analytic version uses $0<r<1$:

$$
\Psi_r(\alpha,\beta)
=
\sum_{n=2}^{\infty}
r^n e^{2\pi i(n\alpha+\Omega(n)\beta)}.
$$

Absolute uniform convergence follows from $\sum_{n\ge2}r^n<\infty$.
Termwise integration therefore gives

$$
R(N)=r^{-N}\int_0^1\int_0^1
\Psi_r(\alpha,\beta)^2
e^{-2\pi i(N\alpha+2\beta)}
\,d\alpha\,d\beta.
$$

No limit $r\to1$ is needed for this coefficient identity. Fourier conversion
of additive convolution into multiplication is classical circle-method
structure; [Helfgott's primary exposition][helfgott] gives an accessible
account. The additional degree variable preserves a particular joint
observation; it supplies no new lower bound by itself.

### Forgetting position loses the additive question

**CAR-07 — PROVED LOCAL (forgetful-summary obstruction).** On a finite
window,

$$
Z_X(1,w)
=
\sum_r
\#\{2\le n\le X:\Omega(n)=r\}\,w^r
$$

retains only the degree histogram. This summary does not determine $R(N)$.

**Proof by the retained source control.** Let $f$ be the involution from
PFO-13, swapping

$$
(53,9),(59,15),(61,21),(67,25),(71,27),
(73,33),(79,35),(83,39),(89,45),(97,49)
$$

and fixing all other labels. Transport multiplication by

$$
a\odot b=f(f^{-1}(a)f^{-1}(b)).
$$

Its degree is $\Omega_f(n)=\Omega(f^{-1}(n))$. Since $f$ permutes
the window $2,\ldots,98$, the two degree histograms agree:

$$
Z_{98}(1,w)=Z^f_{98}(1,w)
=
25w+34w^2+21w^3+11w^4+4w^5+2w^6.
$$

However,

$$
[z^{100}w^2]Z_{98}^2=12,
\qquad
[z^{100}w^2](Z^f_{98})^2=0.
$$

The ordinary six unordered pairs are
$(3,97),(11,89),(17,83),(29,71),(41,59),(47,53)$.
The transported prime labels in the window are
$\{2\}\cup\{3,5,7,\ldots,49\}$, which contain no ordinary-sum-100 pair.
Thus a function of the shared histogram cannot return both correct answers.
QED.

This is a source-specific distinction rather than a claim that every
single-register observable is insufficient. A labeled position–degree
observation already distinguishes the sources. A list of labeled records
and the joint series encode the same data; both are adequate representations.

For every $X\ge98$, the two sum-100 coefficients remain 12 and 0.
A larger observation window cannot repair that stabilized difference.
Transporting addition coherently would preserve the original answer, as
explained in CAR-05 and PFO-13.

## 6. Scott semantics supplies the finite-to-infinite interface

Let

$$
\overline{\mathbb N}=\mathbb N_0\cup\{\infty\},
\qquad
D=\overline{\mathbb N}^{\mathbb N_0\times\mathbb N_0},
$$

with pointwise order. Regard an element as a nonnegative bivariate coefficient
array. Directed suprema are pointwise. Finite-support arrays with finite
coefficients form a countable compact basis, so this is an algebraic Scott
domain.

At an unfinished coordinate, zero records a current lower bound. It does
not certify that no future contribution exists.

Define Cauchy multiplication by

$$
(A*B)(N,r)
=
\sum_{a=0}^{N}\sum_{b=0}^{r}
A(a,b)B(N-a,r-b),
$$

using $0\cdot\infty=0$.

**CAR-08 — PROVED LOCAL (continuity, least fixed point, and stabilization).**
Cauchy multiplication, squaring, and coefficient evaluation are
Scott-continuous on the declared domains.

**Proof.** Each output coordinate is a finite sum of products. Addition and
multiplication on $\overline{\mathbb N}$ preserve directed suprema. For
multiplication, two finite suprema are attained at a common stage by
directedness. If one supremum is infinite and the other positive, common
stages make their product arbitrarily large. If one is zero, every such
product is zero. Finite sums preserve the same limits. QED.

It follows that

$$
Z=\sup_X Z_X,
\qquad
[z^Nw^2]Z^2
=
\sup_X[z^Nw^2]Z_X^2.
$$

For this arithmetic source, the coefficient is already final at every
$X\ge N-2$.

A finite recursive functional can generate the full source. On functions
$F:\mathbb N_{\ge2}\to D$, ordered pointwise, define

$$
\Phi(F)(n)=z^n w^{\Omega(n)}+F(n+1).
$$

The factorization degree is computed by a finite arithmetic routine for each
input. The functional is Scott-continuous, and

$$
\Phi^t(\bot)(n)
=
\sum_{k=n}^{n+t-1}z^k w^{\Omega(k)}.
$$

Its least fixed point is

$$
F_*(n)=\sum_{k=n}^{\infty}z^k w^{\Omega(k)},
\qquad Z=F_*(2).
$$

Indeed, continuity gives
$\Phi(\sup_t\Phi^t(\bot))=\sup_t\Phi^{t+1}(\bot)$, which is the same
supremum. Every other fixed point dominates every iterate from bottom, hence
dominates this one.

This instantiates the standard domain-theoretic treatment of recursive
definitions and directed approximation described by
[Abramsky and Jung][domains]. It does not assume infinitely many elapsed
computational steps.

A fair, cofinal accumulation of the same source coefficients has the same
supremum. For a target $N$, supplying every relevant label
$2,\ldots,N-2$ fixes the answer. Evaluation order can explain a transient
missing contribution. It cannot turn the stabilized ordinary coefficient 12
at sum 100 into the transported coefficient 0 while preserving the same
joint source.

### Universal positivity is not a finite-prefix observation

**CAR-09 — PROVED LOCAL (observational boundary).** For each fixed $N$,
the condition

$$
[z^Nw^2]A^2>0
$$

is Scott-open. The condition that it holds for every even $N\ge4$ need
not be Scott-open.

**Proof.** For fixed $N$, continuity and the discreteness of finite positive
counts imply that a positive contribution at a directed supremum already
appears at some stage.

For the universal assertion, use the chain

$$
A_X(z,w)=\sum_{n=2}^{X}z^n w.
$$

Its supremum $A=\sum_{n=2}^{\infty}z^n w$ satisfies

$$
[z^Nw^2]A^2=N-3>0
$$

for every $N\ge4$. Each finite $A_X$, however, has zero coefficient
at every $N>2X$. The universal set is therefore not inaccessible by
directed suprema, and is not Scott-open. QED.

This is a limitation of finite-prefix observation on the declared ambient
domain. A finite symbolic proof can exploit the generator and quantify over
all targets; the displayed all-integers example itself has such a proof.
For the genuine arithmetic source, the required uniform argument remains
unproved. Scott continuity supplies the semantics of the observation and its
finite witnesses, not the missing distributional estimate.

## 7. The categorical object should retain its map to the carrier

Fix ordinary $\mathbb N$, its addition, and the inclusion
$i:\mathbb P\hookrightarrow\mathbb N$. Form the ordinary Cartesian product
$\mathbb P\times\mathbb P$ and equip it with the sum map

$$
\sigma=+\circ(i\times i):
\mathbb P\times\mathbb P\longrightarrow\mathbb N.
$$

This is an object over the fixed carrier, in the slice category
$\mathrm{Set}/\mathbb N$. Morphisms in that category commute with the
specified maps to the carrier.

**CAR-10 — PROVED LOCAL IDENTIFICATION; nonemptiness remains OPEN.**
For each $N\ge4$, the pullback along the point selecting $N$ is

$$
\boxed{
\mathcal G_N
=
(\mathbb P\times\mathbb P)\times_{\mathbb N}\{N\}
=
\{(p,q):p,q\text{ prime},\ p+q=N\}.
}
$$

Its cardinality is $R(N)$, equivalently the joint coefficient in CAR-06
and the finite reflection trace from PFO-09.

**Proof.** The defining condition of the pullback is precisely
$\sigma(p,q)=N$. The finite coefficient and reflection formulas count
the same ordered pairs. QED.

The product $\mathbb P\times\mathbb P$ here is formed in ordinary sets
before adding the sum map. The product of two inclusions
$\mathbb P\to\mathbb N$ inside the slice would instead impose equality of
their carrier labels and would answer a different question.

Abstract equivalence of multiplicative categories does not automatically
preserve this specified sum map. Equivalence over the full transported
carrier does preserve the corresponding fibers. This gives a precise
categorical distinction between keeping the embedding and forgetting it.

### The remaining proof obligation

The target is an estimate derived from authentic source relations that
forces

$$
[z^{2n}w^2]Z(z,w)^2=R(2n)>0
$$

for every sufficiently large $n$, with any finite remainder handled
explicitly. The displayed positivity assertion itself is Goldbach-equivalent
and is not promoted to an independent lemma.

A useful candidate must specify a quantitative statistic or decomposition,
prove its bounds without supplying already identified prime pairs as inputs,
and retain enough position–degree information to reject the transported
control. A statistic depending only on the common degree histogram cannot
succeed from those hypotheses. A statistic that distinguishes the sources
passes that necessary discrimination test; it still needs the uniform
estimate.

## Earned scope and validation

The carrier intuition survives as a model-class-relative compression theorem
and as a requirement to retain the arithmetic coupling relevant to the
observation. Three stronger inferences have decisive failure controls:

- Universal strict savings fail on independent observations and unnecessarily
  large carriers.
- Equal compression savings or equal total correlation do not determine
  positive overlap.
- Faithful fixed-point semantics and progressively larger windows do not
  identify different stabilized joint sources.

The written proofs establish the stated local identities and constructions.
[The carrier report](receipts/CARRIER_REPORT.json) records finite executable
checks, source controls, and their exact scope. Its tests do not prove the
remaining universal arithmetic estimate. The earlier validation history in
[VALIDATION.md](VALIDATION.md) remains part of the dossier.

The information and source-faithfulness questions are now separated. Coding
savings can be quantified. The anchored arithmetic carrier can be identified.
The joint source can be observed by a finite recursive program. The
source-derived additive lower bound remains the next mathematical obligation.

## Primary sources

1. Claude E. Shannon, *A Mathematical Theory of Communication* (1948).
   [Primary paper][shannon]. Used for finite entropy and lossless source
   coding; the carrier identities are proved directly above.
2. Péter Gács, John T. Tromp, and Paul M. B. Vitányi,
   *Algorithmic Statistics* (2001). [Author-hosted paper][algorithmic-statistics].
   Used for the distinction between individual data, model descriptions, and
   two-part model-to-data codes.
3. Péter Gács, *Lecture Notes on Descriptional Complexity and Randomness*.
   [Author-hosted notes][gacs]. Used for prefix complexity and fixed
   computable translations.
4. Samson Abramsky and Achim Jung, *Domain Theory* (1994), corrected online
   version. [Authors' text, mirrored PDF][domains]. Definitions 2.1.13 and
   2.1.17, section 2.3, and the product constructions supply the standard
   framework; the coefficient domain and its proofs are explicit here.
5. Harald Helfgott, *The Ternary Goldbach Problem*, MFO Snapshot 3/2014.
   [Author's primary exposition][helfgott]. Used for the classical
   convolution/Fourier connection and the distinction between an exact
   encoding and the estimates needed for a positivity proof.

[shannon]: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
[algorithmic-statistics]: https://homepages.cwi.nl/~paulv/papers/algorithmicstatistics.pdf
[gacs]: https://www.cs.bu.edu/fac/gacs/papers/ait-notes.pdf
[domains]: https://www.cs.famaf.unc.edu.ar/~mpagano/cursos/dominios/libros/abramsky-jung-domain-theory.pdf
[helfgott]: https://publications.mfo.de/bitstream/handle/mfo/429/Snapshot-2014-003-Helfgott.pdf
