# Dedekind–Yoneda: an irrational number as a coherent family of rational probes

Date: 2026-11-10 (user timezone). Additive Round III research note.

**Verdict:** the categorical construction is exact. Rational probes recover the
ordered real line fully faithfully; Isbell double conjugacy reconstructs its
Dedekind–MacNeille completion; labelled rational enclosure diagrams provide a
computation interface. These are classical constructions assembled for SUCC,
not a proof of normality or a way to compute arbitrary real numbers.

## 1. Hole contract and the category being constructed

**Target.** Construct a category of irrational values whose objects and arrows
can be recovered exactly from rational or naturally encoded observations, and
exhibit a coherent computation graph for values with effective presentations.

**Truth states.** The equivalences and elementary proofs below are `PROVED` in
ordinary classical mathematics, not newly formalized. In the repository's
ledger vocabulary, the cited established constructions are `CLASSICAL`, the
displayed derivations and concrete examples are `PROVED LOCAL`, and the
`VERIFIED_FINITE` probe receipt is a `TESTED MODEL` result. These local labels do
not promote any existing global ledger claim. Their use as a source-preserving
SUCC compiler is `OPEN` until its source and observer contracts are separately
established.

**Ambient category.** Write $\mathbb R_{\le}$ for the thin category whose objects
are real numbers and which has exactly one arrow $x\to y$ when $x\le y$, and no
arrow otherwise. Composition is transitivity; identities are reflexivity. Let
$\mathbb I_{\le}$ be its full subcategory on irrational numbers. This choice
records order comparisons; it does not pretend that a thin category contains
every computational program with those values.

The rationals form the thin category $\mathbb Q_{\le}$. The strict relation $<$
alone does **not** define a category on the rationals: it omits identities. Every
presheaf below is indexed by the category using $\le$.

**Why use all reals as the arithmetic ambient?** Irrationals are not closed under
addition or multiplication: $\sqrt2+(-\sqrt2)=0$ and $(\sqrt2)^2=2$. The irrational
subcategory is a useful classification, while arithmetic operates in the ambient
real category or on its cut representations.

The arrow variance must also be respected: addition is monotone in both
arguments, negation is a functor $\mathbb R_{\le}^{\mathrm{op}}\to\mathbb R_{\le}$,
and multiplication is monotone in both arguments on the nonnegative domain.
Multiplication on all signed reals is not a functor from the product of their
usual order categories merely because it is a well-defined arithmetic function.

**Novelty tax.** This is a representation and certificate architecture, not a
new theorem about $\pi$. Its concrete benefit is an exact account of which
rational observations determine a value, which maps preserve that account, and
which erased labels or absent moduli make a computation unsound. The missing
statistical estimates of the authenticated BBP orbit remain separate.

**Cheapest falsifiers.** Delete rational labels; confuse strict and closed cuts
at a rational endpoint; claim a finite probe list determines a real; replace a
certified shrinking enclosure sequence by merely nested intervals of positive
limiting width; or silently promote a set-theoretic locator into an algorithm.
Each fails below with an explicit receipt.

## 2. Rational restricted Yoneda is fully faithful

Let $i:\mathbb Q_{\le}\hookrightarrow\mathbb R_{\le}$ be the inclusion. For
$x\in\mathbb R$, define the restricted Yoneda nerve

$$
N_x(q)=\mathbb R_{\le}(i(q),x)
=\begin{cases}\{*\},&q\le x,\\\varnothing,&q>x.\end{cases}
$$

For $q\le r$, the restriction $N_x(r)\to N_x(q)$ is the unique possible map.
Thus $N_x:\mathbb Q_{\le}^{\mathrm{op}}\to\mathbf{Set}$ is a subterminal
presheaf. Its support is the closed rational cut

$$
C_x=\{q\in\mathbb Q:q\le x\}.
$$

### Proposition D1 (`PROVED`)

For every pair of real numbers $x,y$,

$$
\operatorname{Nat}(N_x,N_y)
\cong\mathbb R_{\le}(x,y).
$$

**Proof.** Between two subterminal presheaves there is at most one natural
transformation. There is one exactly when their supports satisfy
$C_x\subseteq C_y$: all necessary component functions then exist and every
naturality square commutes because its target has at most one element. If
$x\le y$, this inclusion holds. If $x>y$, choose a rational $q$ with
$y<q<x$. Then $N_x(q)$ is inhabited and $N_y(q)$ is empty, so no component map
exists. Hence a transformation exists exactly when $x\le y$. Composition and
identities are automatically respected. $\square$

Consequently, $N:\mathbb R_{\le}\to[\mathbb Q_{\le}^{\mathrm{op}},\mathbf{Set}]$
is fully faithful, and it restricts fully faithfully to $\mathbb I_{\le}$.
An irrational value is therefore recoverable from an entire rational probe
profile, including every order arrow to every other value.

This is an equivalence with the **essential image of those profiles**, not an
equivalence between the real numbers and the countable rational category.

## 3. Open cuts are rounded colimits of rational Yoneda objects

The usual strict lower cut is

$$
L_x=\{q\in\mathbb Q:q<x\},\qquad
J_x(q)=\begin{cases}\{*\},&q<x,\\\varnothing,&q\ge x.\end{cases}
$$

Exactly the argument of D1 proves
$\operatorname{Nat}(J_x,J_y)\cong\mathbb R_{\le}(x,y)$.
However, $J_x$ is not literally the restricted ordinary Yoneda presheaf when
$x$ is rational: $N_x(x)=\{*\}$ while $J_x(x)=\varnothing$.

For irrational $x$ the two profiles coincide, because no rational equals $x$.
For rational $r$, the ordinary representable is
$y_{\mathbb Q}(r)(q)=[q\le r]$, not $[q<r]$.

### Proposition D2 (`PROVED`)

In the presheaf category,

$$
J_x\cong\operatorname*{colim}_{r\in\mathbb Q,\ r<x}y_{\mathbb Q}(r),
$$

where the index category uses the usual rational order.

**Proof.** The index category is nonempty and directed. At a rational probe $q$,
the diagram consists of empty sets or singletons, and its colimit is inhabited
exactly when some rational $r<x$ satisfies $q\le r$. This is equivalent to $q<x$:
the forward implication is transitivity, and the reverse follows by choosing
$q<r<x$. All inhabited components are identified in the colimit by directedness.
Presheaf colimits are pointwise, so this identifies the entire presheaf. $\square$

### Corollary D3 (`PROVED`): rational observations glue exactly

For every presheaf $F:\mathbb Q_{\le}^{\mathrm{op}}\to\mathbf{Set}$,
$\operatorname{Nat}(J_x,F)$ is naturally the set of families

$$
(u_q)_{q<x},\qquad u_q\in F(q),
$$

satisfying, for every $q\le r<x$,

$$
F(q\le r)(u_r)=u_q.
$$

**Proof.** A natural transformation out of a colimit is a compatible family of
maps out of its diagram objects. Yoneda identifies
$\operatorname{Nat}(y_{\mathbb Q}(q),F)$ with $F(q)$ and identifies the compatibility
maps with the displayed restriction maps. Equivalently, the result is the limit
of the restricted contravariant diagram $F$ over
$(\mathbb Q_{<x})^{\mathrm{op}}$. $\square$

This is a precise sense in which an irrational endpoint is assembled from
compatible rational observations. The universal property does not say that an
observer can inspect the whole infinite family in finite time.

## 4. The category hidden in a cut must retain its projection

The category of elements of $J_x$ is the rational lower category

$$
\mathcal E_x=\mathbb Q_{<x},\qquad
p_x:\mathcal E_x\hookrightarrow\mathbb Q_{\le}.
$$

Its objects are labelled rational probes $q<x$. It has one arrow $q\to r$ when
$q\le r$. For $x\le y$, inclusion gives a functor
$\mathcal E_x\to\mathcal E_y$ over $\mathbb Q_{\le}$.

Conversely, a functor over $\mathbb Q_{\le}$ must send an object labelled $q$ to
that same rational label. Such a functor exists exactly when $L_x\subseteq L_y$,
and is unique. Therefore

$$
\mathbb R_{\le}
\simeq
\{p_x:\mathcal E_x\to\mathbb Q_{\le}:x\in\mathbb R\}
\subseteq\mathbf{Cat}/\mathbb Q_{\le},
$$

where the right side is the full subcategory on these objects. The usual
presheaf/category-of-elements equivalence is stated in the
[Stacks Project, Lemma 4.38.6](https://stacks.math.columbia.edu/tag/02Y2);
the argument here spells it out for these particular thin categories.

### Hostile control D4 (`PROVED`): the unlabelled category forgets the number

For every finite real $x$, the bare order $\mathbb Q_{<x}$ is countable, dense,
and has neither a least nor a greatest element. Any two such orders are
isomorphic by the usual back-and-forth construction: enumerate both sets,
alternately extend a finite order-preserving partial bijection to the next
unused element on either side, and use density and the absence of endpoints
to choose its image between its finitely many neighbours. The union is an
order isomorphism.

Thus all the bare categories $\mathcal E_x$ are equivalent to one another.
For a completely explicit pair, the translation $q\mapsto q+1$ is an order
isomorphism $\mathcal E_{\sqrt2}\cong\mathcal E_{\sqrt2+1}$, but is not a functor
over the fixed rational base: it changes every label.

**Receipt:** forgetting $p_x$ identifies distinct real values. The same failure
can erase the distinction between rational and irrational endpoints. This is
the Dedekind analogue of forgetting the source and observer decorations from
an abstractly isomorphic carrier.

## 5. Isbell conjugacy computes the cut's double boundary

For a subset $A\subseteq\mathbb Q$, define its rational upper bounds and, for
$B\subseteq\mathbb Q$, its rational lower bounds by

$$
A^u=\{u\in\mathbb Q:\forall a\in A,\ a\le u\},\qquad
B^l=\{l\in\mathbb Q:\forall b\in B,\ l\le b\}.
$$

They form an order-reversing Galois connection:

$$
A\subseteq B^l\quad\Longleftrightarrow\quad B\subseteq A^u.
$$

The composite $c(A)=A^{ul}$ is extensive, monotone, and idempotent.

**Proof.** Extensivity is the definition of upper bound. If $A\subseteq A'$,
then $(A')^u\subseteq A^u$, hence $A^{ul}\subseteq(A')^{ul}$. Finally
$(A^{ul})^u=A^u$: every element of $A^{ul}$ lies below every element of $A^u$,
while $A\subseteq A^{ul}$ gives the reverse inclusion of upper-bound sets.
Applying lower bounds gives idempotence. $\square$

Here is the categorical version. For a downset $A$, let $F_A$ be its subterminal
presheaf. Define its Isbell conjugate by

$$
F_A^\vee(q)=\operatorname{Nat}(F_A,y_{\mathbb Q}(q)).
$$

This set is a singleton exactly when $A\subseteq\downarrow q$, which means
$q\in A^u$. It is therefore the subterminal covariant functor supported on
$A^u$. Conjugating back gives

$$
F_A^{\vee\vee}(p)
=\operatorname{Nat}(F_A^\vee,\mathbb Q_{\le}(p,-))
=[p\in A^{ul}].
$$

So **the Isbell double-conjugate operator is literally the operation “take all
upper bounds, then all their lower bounds.”** Its fixed points are the
Dedekind–MacNeille cuts. This is the poset specialization treated by
[Avery and Leinster, Examples 3.3 and 6.10](https://www.pure.ed.ac.uk/ws/portalfiles/portal/207987727/2102.08290_1_.pdf).
The idempotence and completeness just proved are special to this setting;
iterated conjugacy of arbitrary Set-valued functors on arbitrary categories
does not generally stabilize after two steps.

### Proposition D5 (`PROVED`): exact completion and irrational subcategory

Let

$$
\operatorname{MN}(\mathbb Q)=\{A\subseteq\mathbb Q:A=A^{ul}\},
$$

ordered by inclusion. Then

$$
\operatorname{MN}(\mathbb Q)\cong[-\infty,+\infty]_{\le},
$$

with $-\infty\leftrightarrow\varnothing$, $+\infty\leftrightarrow\mathbb Q$,
and $x\leftrightarrow C_x$. Moreover,

$$
\mathbb I_{\le}\cong
\{A:\varnothing\ne A\ne\mathbb Q,\ A=A^{ul},\ A\text{ has no greatest element}\}.
$$

**Proof.** If a nonempty fixed set $A$ is proper, then $A^u$ is nonempty:
otherwise $A^{ul}=\mathbb Q$. Thus $A$ has a finite real supremum $x$.
Its rational upper bounds are exactly the rationals $u\ge x$, so the lower
bounds of those are precisely the rationals $q\le x$. Hence $A=C_x$.
Conversely, rational density directly gives $C_x^{ul}=C_x$. The empty and full
cases follow from the unboundedness of $\mathbb Q$. Order preservation and
reflection are D1. If $x$ is rational, $C_x$ has greatest element $x$. If $C_x$
has a greatest element $r$, its supremum is $r$, so $x=r$ is rational. This
proves the irrational characterization. $\square$

When using this as a construction of the real line, one can instead define
the finite proper fixed cuts first; the preceding argument then identifies
that construction with any independently constructed complete real line.

### Endpoint mutation: open and closed cuts must not be conflated

For a rational $r$,

$$
\{q:q<r\}^{ul}=\{q:q\le r\}.
$$

The double conjugate adds the rational endpoint. Thus a strict rational lower
cut is not a MacNeille fixed point. For an irrational endpoint there is no
rational point to add. All **strict** lower real cuts have no greatest element;
that property distinguishes irrationality only for the **closed fixed cuts**
used in D5.

### Proposition D6 (`PROVED`): the completion's universal property

Meets and joins of fixed cuts are

$$
\bigwedge_i A_i=\bigcap_i A_i,\qquad
\bigvee_i A_i=\left(\bigcup_i A_i\right)^{ul}.
$$

Every fixed cut is both a join and a meet of embedded rational elements:

$$
A=\bigvee_{q\in A}\downarrow q
=\bigcap_{u\in A^u}\downarrow u.
$$

**Proof.** Fixed points of an extensive monotone idempotent closure operator
are closed under intersections. The closure of a union is their least closed
upper bound. The first density identity uses downward closure of $A$; the
second is its fixed-point equation. Empty joins and meets include the two
infinities. $\square$

More precisely, suppose a complete lattice $K$ contains an order-embedded copy
$j:\mathbb Q\to K$ and every $z\in K$ satisfies

$$
z=\bigvee_{j(q)\le z}j(q)
=\bigwedge_{z\le j(u)}j(u).
$$

Then $z\mapsto A_z=\{q:j(q)\le z\}$ is an order isomorphism
$K\cong\operatorname{MN}(\mathbb Q)$.

**Proof.** Join density implies
$A_z^u=\{u:z\le j(u)\}$; meet density then implies $A_z^{ul}=A_z$.
Join density also proves that $A_z\subseteq A_w$ iff $z\le w$. For a fixed cut
$A$, put $z=\bigvee_{q\in A}j(q)$. Then $A\subseteq A_z$. If $r\in A_z$,
each $u\in A^u$ gives $j(r)\le z\le j(u)$, so $r\in A^{ul}=A$.
Thus $A_z=A$, proving surjectivity and the claimed inverse. $\square$

This is a join-and-meet density characterization. It is not a claim that every
monotone rational map extends to a map preserving arbitrary joins and meets.
For example, the rational step map $q\mapsto0$ for $q<0$ and $q\mapsto1$ for
$q\ge0$ already fails to preserve the existing rational supremum
$\sup\{q:q<0\}=0$.

## 6. The computation graph is a graph of certified intervals

Let $\mathcal B$ have objects rational pairs $(a,b)$ with $a<b$, and one arrow

$$
(a,b)\longrightarrow(c,d)\quad\text{iff}\quad a\le c<d\le b.
$$

An arrow means “refine this enclosure.” Let $\mathcal B_x$ be the full
subcategory on enclosures with $a<x<b$. It is directed: two such intervals
have an intersection still containing $x$, and there is a rational interval
strictly around $x$ inside that intersection.

Let $\mathbf{IR}$ be the poset of nonempty compact real intervals, ordered by
reverse inclusion. A nonempty directed family has supremum its intersection:
the finite-intersection property inside any one compact member gives a
nonempty intersection, which is again a compact interval.

### Proposition D7 (`PROVED`)

The diagram $(a,b)\mapsto[a,b]$ from $\mathcal B_x$ to $\mathbf{IR}$ has colimit
$[x,x]$. A nested sequence of strict rational enclosures $[a_n,b_n]$ with
$b_n-a_n\to0$ is cofinal in $\mathcal B_x$ and has the same colimit.

**Proof.** The intersection of all rational enclosures of $x$ contains $x$.
If $y\ne x$, rational density supplies an enclosure containing $x$ but not
$y$, so the intersection is $\{x\}$. For cofinality, fix $a<x<b$ and let
$\delta=\min(x-a,b-x)>0$. Once $b_n-a_n<\delta$, the enclosure containing $x$
is contained in $(a,b)$. All later intervals are refinements, so the relevant
comma category is nonempty and directed. The same argument proves the
intersection is a singleton. $\square$

The colimit is taken in the **interval information order**, not in
$\mathbf{Set}$. It is a mathematical description of a limiting value, not an
assertion that an infinite computation has finished.

Two different shrinking enclosure algorithms for the same real are cofinal
in the same $\mathcal B_x$. Their finite certificates can be compared through
common refinements. This preserves the value while allowing different schedules;
it says nothing by itself about their running times or digit statistics.

There is an explicit coherent comparison diagram. Given strict names
F(n)=(a_n,b_n) and G(m)=(c_m,d_m) of the same x, define

$$
H(n,m)=\bigl(\max(a_n,c_m),\,\min(b_n,d_m)\bigr).
$$

Because both intervals strictly contain x, H has positive width and is a
functor from the product order on natural-number pairs into B_x. The
inclusions give natural transformations F composed with the first projection
-> H and G composed with the second projection -> H. All refinement squares
commute because this target category is thin. For the BBP and Machin names,
their separate identities with pi justify the shared x; finite overlap alone
would not prove equality of the limits. This supplies actual maps connecting
two computation schedules while retaining their rational labels.

For a genuine partial-information object, the two bounding sides may leave a
nonzero gap. Nested intervals $[0,1+1/n]$ have limiting interval $[0,1]$, not
a real point. Directedness alone does not supply convergence to a value.

## 7. A square root becomes integer comparisons

For $q=p/s$ with $p\in\mathbb Z$, $s\in\mathbb N_{>0}$,

$$
q<\sqrt2\quad\Longleftrightarrow\quad
(p<0)\ \lor\ (p^2<2s^2),
$$

and

$$
\sqrt2<q\quad\Longleftrightarrow\quad
(p>0)\ \land\ (2s^2<p^2).
$$

Every rational cut query is therefore answered by exact integer arithmetic.
Equality cannot occur: if a reduced positive fraction satisfied $p^2=2s^2$,
then $p$ would be even, and substitution would force $s$ even, contradicting
coprimality.

An explicit computation path is

$$
k_n=\left\lfloor\sqrt{2\cdot4^n}\right\rfloor,\qquad
a_n=k_n/2^n,\quad b_n=(k_n+1)/2^n.
$$

Integer square root computes $k_n$ without a floating-point approximation of
$\sqrt2$. We have $a_n^2<2<b_n^2$, $b_n-a_n=2^{-n}$, and the intervals are
nested because $k_{n+1}$ is either $2k_n$ or $2k_n+1$. D7 then supplies the
exact limiting value and schedule coherence.

This is a useful compiler target: a real value is reconstructed by an infinite
profile, while each demanded finite rational observation has a terminating
integer certificate in this particular example. It is not a construction of
a terminating comparison algorithm for arbitrary real presentations.

## 8. Lower cuts, located cuts, and an actual computation oracle

The computational distinction is essential. A constructive Dedekind real uses
two inhabited rounded predicates $L,U\subseteq\mathbb Q$, where

$$
q\in L\ \Longleftrightarrow\ \exists r\in L,\ q<r,
\qquad
q\in U\ \Longleftrightarrow\ \exists r\in U,\ r<q.
$$

They also satisfy separation
$l<u$ for $l\in L,u\in U$, and locatedness

$$
p<q\quad\Longrightarrow\quad (p\in L)\ \lor\ (q\in U).
$$

Here $L$ is the strict lower side and $U$ the strict upper side. A rounded lower
cut alone can describe one-sided information; it does not in general provide
effective upper bounds or a computable real. Dropping locatedness can leave an
interval. The relationship between these cut pairs and interval information is
developed by [Paul Taylor, Cuts and intervals, Section 2](https://www.paultaylor.eu/~pt/ASD/dedras/cutintvl).

A **locator** supplies an actual branch for each $p<q$:

$$
\operatorname{loc}_x(p,q)\in\{\text{a certificate of }p<x\}
\;\sqcup\;
\{\text{a certificate of }x<q\}.
$$

Both answers may be valid, so a locator is extra presentation structure.
[Booij, Definition 3.1.1 and the discussion immediately following it](https://arxiv.org/pdf/1805.06781)
carefully distinguishes this structure from mere locatedness and from Turing
computability. In particular, a set-theoretically existing locator need not be
computable.

### Proposition D8 (`PROVED`): a computable locator yields effective enclosures

Assume a terminating computable locator and a supplied certified rational
enclosure $a<x<b$. Set

$$
p=a+(b-a)/3,\qquad q=a+2(b-a)/3.
$$

If the locator returns $p<x$, replace $(a,b)$ by $(p,b)$. Otherwise it returns
$x<q$; replace $(a,b)$ by $(a,q)$. Each step is a certified refinement of width
$2/3$ times the previous width. Consequently, a prescribed rational accuracy
is reached after an explicitly bounded number of steps.

Conversely, suppose an algorithm supplies rationals $r_n$ with certified error
$|x-r_n|\le2^{-n}$. For $p<q$, choose $n$ with $2^{1-n}<q-p$ and set
$\varepsilon=2^{-n}$. If $r_n-\varepsilon>p$, return $p<x$. Otherwise
$x\le r_n+\varepsilon\le p+2\varepsilon<q$, so return $x<q$.
This constructs a computable locator. $\square$

This avoids deciding the exact equality of a real and a rational. It also
separates a proved, terminating finite query from an unsupported claim that
every infinite cut is computable.

## 9. Natural-number coding and arithmetic of the probe families

Every rational has a unique reduced presentation $p/s$ with $s>0$. Encode
$p$ by the zigzag function $z(p)=2p$ for $p\ge0$ and $z(p)=-2p-1$ otherwise.
Then use the Cantor pairing function

$$
\langle a,b\rangle=(a+b)(a+b+1)/2+b
$$

to encode $p/s$ by $\langle z(p),s-1\rangle$. The valid reduced codes form a
decidable subset of $\mathbb N$. Rational order becomes the integer test
$ps'\le p's$ for denominators $s,s'>0$. Hence the rational probe category has
a completely numerical presentation, and interval nodes and arrows can be
encoded by further pairing.

The real $x$ is represented by a **family of natural-number codes**, such as
$\{\operatorname{code}(q):q<x\}$, with its inherited arrows. It is not, in
general, represented by a single finite integer. There are only countably many
finite programs and uncountably many real numbers.

Arithmetic can be expressed through rational witnesses. For strict lower cuts,

$$
L_{x+y}
=\{q\in\mathbb Q:\exists a\in L_x,\exists b\in L_y,\ q<a+b\}.
$$

**Proof.** A witness gives $q<a+b<x+y$. If $q<x+y$, choose a positive real
$\delta$ with $2\delta<x+y-q$, then rational $x-\delta<a<x$ and
$y-\delta<b<y$. Their sum exceeds $q$. $\square$

Negation exchanges the two strict sides:

$$
L_{-x}(q)=U_x(-q),\qquad U_{-x}(q)=L_x(-q).
$$

Thus addition is a rational witness-joining operation and negation reveals why
one-sided information is insufficient for general effective arithmetic. These
are exact cut formulas; no claim is made that arbitrary uncomputable membership
predicates can be evaluated by a finite program.

## 10. Finite probes, receipts, and the SUCC acceptance boundary

### Proposition D9 (`PROVED`): a finite threshold battery cannot identify an irrational

Let $S\subset\mathbb Q$ be finite and $x$ irrational. If $S$ is nonempty, set
$d=\min_{q\in S}|x-q|>0$. Every real $y$ with $|y-x|<d$ gives exactly the same
strict threshold answers on $S$. For empty $S$ the assertion is immediate.
Therefore a finite threshold profile leaves an interval of possible values.

An exact probe control uses $x=\sqrt2$ and $y=\sqrt2+1/1024$. The rational
probes $q=k/8$ for $-32\le k\le32$ cannot distinguish them. But the fresh probe
$q=1449/1024$ does:

$$
\sqrt2<1449/1024<\sqrt2+1/1024.
$$

Both inequalities reduce to integer squares. Full Yoneda profiles distinguish
the values; this finite profile does not. No calibrated finite pass becomes
equality of all profiles.

The companion `dedekind_order_probe.py` checks finite closure laws, a mutation
showing that a union of closed cuts may require closure, rational-code
roundtrips, exact square-root refinements, the locator refinement protocol,
and the deliberately indistinguishable finite profile followed by its
separating probe. It is a finite regression instrument, not a proof of the
infinite theorems.

**Execution receipt (`VERIFIED_FINITE` / `TESTED MODEL`).** The command

```sh
python -W error research/2026-11-10/cursed_categorical_computation/round_iii_dedekind/dedekind_order_probe.py
```

completed successfully with status `PASS`. It checked 4,416 Galois-connection
pairs across a six-element chain, a four-element diamond, and a three-element
antichain; 77 pairs of completed-lattice elements; 1,187 rational-code
roundtrips; 2,209 integer order comparisons; 128 dyadic square-root enclosures;
and two different 80-step locator schedules. All three intended mutations
were rejected: omission of closure after union, acceptance of a nonreduced
rational code, and identification of real values from the 65-probe finite
profile. The full repository suite and formal proof compilation were not run
for this standalone note.

For SUCC, the concrete acceptance contract is:

1. Bind every enclosure to the authentic source, literal seed, and exact index.
2. Carry rational endpoints and proofs of refinement through each computation.
3. State an effective accuracy budget whenever an observer asks for a discrete
   output or an interval narrower than a specified threshold.
4. Keep the rational labels and source projection when comparing categories.
5. Require a separate theorem for an asymptotic signed statistic. Equality of
   limiting values and coherence of computation schedules do not provide it.

**Dominance boundary.** This construction improves the semantics of exact real
observation: it exposes erased labels, one-sided information, rational endpoint
errors, and missing effective moduli. It does not control the empirical
distribution of the selected real's digits. The next useful probe is whether
the authenticated BBP evaluator can emit and compose these certificates without
changing the requested observable or silently granting it extra precision.

## 11. Compact claim ledger

| Claim | Status | Supporting boundary |
|---|---|---|
| Rational restricted Yoneda preserves and reflects every real order arrow | `PROVED` | D1; all rational probes |
| Strict cuts are directed colimits of rational representables | `PROVED` | D2; pointwise presheaf colimits |
| Maps from an endpoint profile are compatible rational sections | `PROVED` | D3; colimit universal property and Yoneda |
| Forgetting rational labels preserves the value | `REFUTED` | D4; translated distinct cuts have isomorphic bare categories |
| Isbell double conjugacy equals rational upper/lower-bound closure | `PROVED` | Section 5; subterminal functors on a poset |
| Closed fixed cuts recover extended reals; nonprincipal finite cuts recover irrationals | `PROVED` | D5; classical identification |
| The completion is characterized by complete join-and-meet density | `PROVED` | D6; stated hypotheses |
| Shrinking certified rational paths are cofinal and recover their endpoint | `PROVED` | D7; interval information order |
| A computable locator plus an initial enclosure gives effective approximation | `PROVED` | D8; explicit ternary algorithm |
| A finite rational threshold profile identifies an irrational | `REFUTED` | D9; exact displaced-square-root control |
| Every cut or abstract locator is computable | `REFUTED` | Countability and the property/structure distinction |
| This construction proves original-zero parity balance or $\pi$ normality | `OPEN` | No source-selected signed estimate supplied |

## Primary-source provenance

- Tom Avery and Tom Leinster, *Isbell conjugacy and the reflexive completion*,
  Theory and Applications of Categories 36(12), 306–347 (2021).
  [Paper record](https://arxiv.org/abs/2102.08290),
  [inspected author PDF](https://www.pure.ed.ac.uk/ws/portalfiles/portal/207987727/2102.08290_1_.pdf).
  Relevant parts: Examples 3.3, 6.10–6.11 and 8.6. No general-category
  completeness or unrestricted functoriality is imported.
- Paul Taylor, *Cuts and intervals*, Section 2 of the author's abstract Stone
  duality development: [primary text](https://www.paultaylor.eu/~pt/ASD/dedras/cutintvl).
  Used to audit the strict-cut, locatedness, and interval-information conventions.
- Auke B. Booij, *Extensional constructive real analysis via locators*,
  Mathematical Structures in Computer Science 31(1), 64–88 (2021).
  [Paper record](https://arxiv.org/abs/1805.06781),
  [inspected v5 PDF](https://arxiv.org/pdf/1805.06781).
  Definition 3.1.1 and its adjacent discussion separate locatedness, locator
  structure, and computability. The elementary ternary protocol here is given
  with its own proof.
- Stacks Project, [Lemma 4.38.6](https://stacks.math.columbia.edu/tag/02Y2) and
  [Example 4.38.5](https://stacks.math.columbia.edu/tag/04TM): presheaves and
  categories fibred in sets.

All source claims were checked against the primary texts during this round.
The displayed proofs and exact examples are supplied in this note for audit;
the sources are not treated as a substitute for matching hypotheses.
