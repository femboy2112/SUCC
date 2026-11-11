# Cursed categorical computation, round II

## Aim and exact boundary

The second round asks for more than an amusing encoding: turn computational arrows into numbers, open those numbers into families or categories, and retain coherent arrows between the resulting objects. This archive records several exact answers, distinguishes the different equivalences, and identifies the remaining statistical obligation.

The conventions, authenticated four-pole source, and status vocabulary are those of [ROUND_I.md](ROUND_I.md). In particular $P_\infty=\pi/16$, while $\sum_{n\ge1}16^{-(n-1)}r(n)=\pi$. The proofs below establish algebraic and categorical statements. They do not establish a complete SUCC C-monoid compiler, base-16 normality, original-zero parity balance, or RH.

The accompanying [round_ii_probe.py](round_ii_probe.py) is a standalone standard-library probe. Its fresh output is [round_ii_receipt.json](round_ii_receipt.json). Earlier conversational checks are historical evidence, not silently counted as new runs.

## II.1. Idempotent arrow-numbers become objects, families, and categories

### The general equivalence

Let $M$ be a monoid. In its Karoubi envelope $\operatorname{Kar}(\mathbf BM)$:

- an object is $e\in M$ with $e^2=e$;
- an arrow $a:e\to f$ satisfies $a=fae$;
- composition is monoid multiplication, so $b\circ a=ba$;
- the identity at $e$ is $e$, not necessarily the unit of $M$.

The corner equation is equivalent to $fa=a=ae$. Send $e$ to the principal right $M$-set $eM$, and send $a:e\to f$ to

$$
L_a:eM\longrightarrow fM,\qquad x\longmapsto ax.
$$

**PROVED:** this is an equivalence onto the full subcategory of right $M$-sets consisting of the sets $eM$ for idempotent $e$. It is fully faithful because every equivariant map $F:eM\to fM$ is determined by $a=F(e)$:

$$
F(em)=F(e)m=am,\qquad fa=a,\qquad ae=F(ee)=F(e)=a.
$$

Conversely, every $a=fae$ supplies such a map. Composition and identities follow immediately. This proves the equivalence for every monoid, without assuming finiteness or a lambda interpretation.

### Opening the family into a category over the original monoid

Define $\mathcal E_e$ with objects $x\in eM$. An arrow labelled $m$ from $x$ to $y$ exists exactly when $x=ym$. Composition uses the product of labels. There is a projection $\mathcal E_e\to\mathbf BM$ remembering each label. The map $L_a$ gives a functor over $\mathbf BM$:

$$
x\longmapsto ax,\qquad (x\xrightarrow{m}y)\longmapsto(ax\xrightarrow{m}ay).
$$

Conversely, a functor over $\mathbf BM$ must preserve these action equations, and therefore corresponds to an equivariant map. Consequently the same Karoubi category is equivalent to the full subcategory of $\mathbf{Cat}/\mathbf BM$ on the objects $\mathcal E_e\to\mathbf BM$.

**The base-preservation condition is essential.** This is not a claim about all functors between the underlying categories after forgetting their labels. The monoid action is the information that makes the reconstruction faithful.

### A complete numerical example

Let $T_3$ be the monoid of all functions $\{0,1,2\}\to\{0,1,2\}$. Encode $(t_0,t_1,t_2)$ by $t_0+3t_1+9t_2$. Composition is digit substitution, not ordinary integer multiplication. The identity is $21=(0,1,2)$.

Consider

$$
e=18=(0,0,2),\quad f=12=(0,1,1),\quad
a=9=(0,0,1),\quad b=24=(0,2,2).
$$

Then

$$
e^2=e,\quad f^2=f,\quad ba=e,\quad ab=f.
$$

Thus $a:e\to f$ and $b:f\to e$ are inverse arrows in the Karoubi envelope, although neither is a permutation of the original three-element set. Their families are

$$
18T_3=\{0,2,6,8,18,20,24,26\},
$$

$$
12T_3=\{0,1,3,4,9,10,12,13\}.
$$

An idempotent number has become an eight-element family, and the other arrow-numbers become mutually inverse equivariant maps between those families. The probe enumerates all 27 functions, all ten idempotents, and all 348 typed Karoubi arrows.

For every $N\ge1$, the analogous image construction gives

$$
\operatorname{Kar}(\mathbf B T_N)
\simeq\mathrm{FinSet}_{1\le|X|\le N}.
$$

Proof: $e$ goes to its nonempty image. An arrow $a=fae$ restricts to a map $\operatorname{im}e\to\operatorname{im}f$, and any such map $h$ extends uniquely to the corner arrow $he$. Every cardinality $1,\ldots,N$ is the image of an idempotent. This completion need not be equivalent to the original one-object category.

### Lambda semantics and the equality boundary

For a beta-lambda theory, UniMath identifies the Karoubi envelope of the unary substitution monoid with Scott's retract category and proves the requisite Cartesian closed structure. This is a classical/formalized bridge under its stated assumptions. It is not the assertion that an arbitrary numerical monoid has a CCC completion.

Finite syntax can be Gödel-coded effectively. Semantic beta equality cannot be replaced by equality of raw syntax codes; a canonical effective representative for every beta-equivalence class would decide an undecidable equality problem. The finite $T_3$ model avoids that issue and demonstrates the mechanism, but it does not certify a faithful full SUCC lambda compiler.

**Job:** make retract types and their coherent maps explicit rather than hiding them inside an untyped carrier. **Hostile checks:** identity $e$ must not be replaced by the ambient unit; arbitrary category maps must not replace maps over $\mathbf BM$; syntax equality must not replace semantic equality.

## II.2. The actual affine clock monoid becomes numbers and arithmetic families

Let

$$
M=\{(a,b):a\ge1,\ b\ge0\},\qquad
(a,b)(c,d)=(ac,ad+b).
$$

This is composition of maps $n\mapsto an+b$. It has the bijective positive-integer code

$$
\operatorname{code}(a,b)=2^{a-1}(2b+1).
$$

To decode $c\ge1$, put $a=1+v_2(c)$ and $b=(c/2^{a-1}-1)/2$. Transporting the monoid product through this bijection defines an exact numerical operation $\odot$. For $D_2=(2,0)$ and $S=(1,1)$,

$$
\operatorname{code}(D_2)=2,\quad\operatorname{code}(S)=3,
\quad 2\odot3=10,\quad3\odot2=6.
$$

The distinction records $D_2S=S^2D_2$, not $D_2S=SD_2$. Ordinary integer multiplication would erase it.

For $g=(a,b)$, its principal right ideal has the explicit arithmetic membership rule

$$
gM=\{(A,B):a\mid A,\ B\ge b,\ B\equiv b\pmod a\}.
$$

The affine monoid is left cancellative: equality $gx=gy$ forces $x=y$. Hence $q_g:M\to gM$, $x\mapsto gx$, is an isomorphism of right $M$-sets.

Every equivariant map $gM\to hM$ therefore has the unique form

$$
F_k^{g,h}(gx)=hkx,\qquad k\in M.
$$

If $F_l^{h,j}$ follows it, the composite is $F_{lk}^{g,j}$. Thus the category $\mathcal R(M)$ of principal right ideals and all equivariant maps is equivalent to $\mathbf BM$: the regular right action is a fully faithful one-object subcategory and every $gM$ is isomorphic to it.

There is an important information-loss boundary. The *inclusion* $i_g:gM\hookrightarrow M$ retains the original affine arrow:

$$
L_g=i_gq_g.
$$

All the ideals are abstractly isomorphic; their embeddings distinguish the clock operations. This is the same structural warning as the source-gauge groupoid in round I: the ambient labels and observations are part of the intended object.

The affine monoid itself has only the identity idempotent. Indeed $(a^2,ab+b)=(a,b)$ forces $a=1,b=0$. Its Karoubi envelope therefore does not manufacture the richer retract types of the preceding section. The two constructions solve different problems and must not be conflated.

**Job:** an exact, decidable numerical presentation of the clock category already acting on the authenticated BBP carrier. **Boundary:** the source action remains a representation, with source-specific observers still required. **Next test:** preserve the ideal inclusions and source evaluator under any proposed equivalence.

## II.3. Splitting an affine arrow reveals a sparse Möbius inverse

The affine monoid has finite decomposition sets. If $g=(A,B)$ and $xy=g$, write $x=(a,b)$ and $y=(c,d)$. Then

$$
a\mid A,\quad c=A/a,\quad d\in\{0,\ldots,\lfloor B/a\rfloor\},\quad b=B-ad.
$$

Therefore the incidence coproduct

$$
\Delta[g]=\sum_{xy=g}[x]\otimes[y]
$$

is a finite sum. Coassociativity follows because both repeated splittings enumerate all triples with product $g$. For numerical code $10$, the five ordered pairs of factor codes are

$$
(1,10),\ (10,1),\ (2,3),\ (3,6),\ (5,2).
$$

A factorization into nonidentity arrows has length at most $\lfloor\log_2 A\rfloor+B$: each factor with slope at least two consumes multiplicative slope, and each remaining nonidentity translation contributes at least one to the final translation. This supplies local finite length for the convolution inverse.

Let $\zeta$ have coefficient one on every affine arrow. Its inverse has the surprisingly sparse formula

$$
\boxed{\mu_{\mathrm{Aff}}(a,b)
=\mu_{\mathbb N}(a)\left(\mathbf1_{b=0}-\mathbf1_{b=a}\right).}
$$

**PROVED.** In the locally finite formal convolution algebra, write $D_a=(a,0)$ and $S=(1,1)$. Every arrow has a unique form $S^bD_a$, so

$$
\zeta=\left(\sum_{b\ge0}S^b\right)\left(\sum_{a\ge1}D_a\right).
$$

The first factor has inverse $1-S$, and the second has inverse $\sum_{a\ge1}\mu_{\mathbb N}(a)D_a$. Reverse the order of inverses:

$$
\zeta^{-1}
=\left(\sum_a\mu_{\mathbb N}(a)D_a\right)(1-S).
$$

Because $D_aS=(a,a)$, its coefficients are exactly the boxed formula. The argument is coefficientwise: it does not assume convergence of an analytic Dirichlet series.

The tempting alternative with $\mathbf1_{b=1}$ in place of $\mathbf1_{b=a}$ is false because it commutes the noncommuting factors. The probe rejects it at $(2,1)$, checks both inverse orders, and independently computes the recursive convolution inverse on a declared finite grid.

**Job:** invert affine aggregation while preserving order, distinguishing direct clock contributions from accumulated ones. This is a derived specialization of incidence algebra, not a priority claim. **Boundary:** sparse algebraic coefficients do not imply small source-selected Fourier sums. **Next test:** identify an actual affine aggregation in the observer and verify that inversion retains the required source and boundary data.

## II.4. A broken inverse generates all finite rational linear algebra

Let

$$
\mathcal A=\mathbb Q\langle S,T\mid TS=1\rangle,
\qquad P=1-ST.
$$

This is the linear algebra generated by the bicyclic relation. Define

$$
E_{ij}=S^iPT^j,\qquad i,j\ge0.
$$

From $P^2=P$, $PS=0$, and $TP=0$, one gets

$$
E_{ij}E_{kl}=\delta_{jk}E_{il}.
$$

In the unilateral-shift representation, $E_{ij}e_k=\delta_{jk}e_i$, proving linear independence. Put

$$
P_n=\sum_{i=0}^{n-1}E_{ii}=1-S^nT^n,\qquad P_0=0.
$$

The equality telescopes. For all $m,n\ge0$,

$$
P_m\mathcal A P_n
\cong\operatorname{Mat}_{m\times n}(\mathbb Q).
$$

Every corner element is determined by its finite matrix entries in the faithful shift representation, and every matrix is a finite linear combination of the $E_{ij}$ with $i<m,j<n$. The category with objects $P_n$, corner morphisms, and identities $P_n$ is consequently equivalent to finite-dimensional rational vector spaces and linear maps, including the zero-dimensional object.

**PROVED:** this equivalence uses linearization and corners. It is not an equivalence between the bare two-generator monoid and all vector spaces. It also requires an infinite ambient representation: on a finite-dimensional space, $TS=I$ forces both maps to be invertible and $ST=I$, killing $P$.

**Job:** compile the six-cell oscillator, finite wavelet transforms, rational observer operators, and their compositions into shifts plus a single boundary defect. **Hostile control:** a bilateral shift or a finite-dimensional exact inverse pair makes $P=0$. **Next test:** preserve the coefficient signs, source inputs, and observer norm rather than inferring statistical cancellation from the availability of a matrix language.

## II.5. Integer arrows open into whole family categories

Let $\mathrm{Mat}_{\mathbb N}$ have objects $n\ge0$ and $m\times n$ matrices as arrows $n\to m$. Encode a typed matrix by

$$
E(A:n\to m)=2^n3^m\prod_{k=0}^{mn-1}p_{k+3}^{A_k+1},
$$

using row-major order and $p_3=5$. Dimensions retain empty matrices; the $+1$ retains zero entries. Unique prime factorization gives an effective inverse on valid codes. Transporting matrix multiplication gives a category of integer arrows isomorphic to $\mathrm{Mat}_{\mathbb N}$.

Now open object $n$ into $\mathcal F_n=\mathrm{FinSet}^n$, and open the arrow into

$$
F_A:\mathcal F_n\to\mathcal F_m,\qquad
F_A(X)_j=\coprod_i[A_{ji}]\times X_i.
$$

Distributivity and reassociation give $F_BF_A\cong F_{BA}$ with their canonical coherence. Every finite-coproduct-preserving functor between these family categories has this form up to natural isomorphism: the elementary families $e_i$ generate every object by finite coproducts, and the coefficient family is $F(e_i)$.

It follows that

$$
\mathrm{Mat}_{\mathbb N}\simeq
\left(\mathrm{FinSet}^n,\ 
\text{finite-coproduct-preserving functors modulo natural isomorphism}\right).
$$

This includes $n=0$: a functor out of the empty-family category that preserves the initial object is forced to choose the initial family.

Keeping coefficient sets rather than just their sizes gives higher arrows. Every family of maps $[A_{ji}]\to[B_{ji}]$ determines a natural transformation $F_A\Rightarrow F_B$, and every natural transformation is so determined by its values on the elementary families. There are

$$
\prod_{j,i}B_{ji}^{A_{ji}}
$$

such transformations, with $0^0=1$. This is a bicategorical version of the construction; natural-isomorphism classes recover the ordinary matrix category.

For

$$
A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
B=\begin{pmatrix}2&0\\1&1\end{pmatrix},
\qquad BA=\begin{pmatrix}2&4\\1&3\end{pmatrix},
$$

the codes are $573873300$, $644143500$, and $261373463851500$. The first opens into $(X,Y)\mapsto(X\amalg Y\amalg Y,Y)$.

The same construction is the span description of matrix arithmetic. A finite span $X\leftarrow S\to Y$ has entries $|S_{yx}|$; composition by the pullback $S\times_YT$ yields fibers $\coprod_y S_{yx}\times T_{zy}$. Consequently isomorphism classes of finite spans give the matrix category. Actual witness sets retain the identities of paths whose cardinalities become coefficients.

**Job:** exact finite transfer operators and witness-preserving execution composition. **Boundary:** taking cardinality forgets witness identity; signed cancellation requires an explicit signed extension; a data join supplies no independence assumption. **Next test:** compare labeled witness fibers before and after a proposed arithmetic aggregation.

## II.6. The four-pole source as a signed groupoid

For a finite cyclic group $C_k$, its one-object classifying groupoid $BC_k$ has cardinality $1/k$. Use a sign grading, with all morphisms preserving that grading. At clock $n\ge1$, take four even copies of $BC_{8n-7}$ and the odd part

$$
2BC_{8n-4}\amalg BC_{8n-3}\amalg BC_{8n-2}.
$$

The signed cardinality is exactly $r(n)$. These are ordinary finite groupoids carrying a declared sign; a “negative object” is not being asserted to exist.

The recurrence also lifts formally: take sixteen copies of the previous signed family and add the current one, beginning with the empty family at clock zero. Signed cardinality then gives $U_n=16U_{n-1}+r(n)$ exactly.

For the completed source, weight the $n$th signed groupoid by the Cartesian factor $BC_{16^{n-1}}$. Both the even and odd sums converge absolutely, and their difference is

$$
\sum_{n\ge1}16^{-(n-1)}r(n)=\pi.
$$

Using $BC_{16^n}$ instead would give $\pi/16$. This explicit normalization is part of the source contract.

**PROVED:** these signed-cardinality identities. **REFUTED:** equal cardinality implies groupoid equivalence. The groupoids $BC_4$ and $B(C_2\times C_2)$ both have cardinality $1/4$, but their automorphism groups are not isomorphic: one contains an element of order four and the other does not.

**Job:** a categorical source passport retaining denominator groups, multiplicities, signs, and clocks before numerical evaluation. **Boundary:** re-encoding the BBP sum does not create a statistical theorem, and signed cardinality is not a complete invariant. **Next test:** require any proposed cancellation to be realized by structure-preserving maps or a separately justified numerical estimate.

## II.7. FRACTRAN: one integer as the complete register state

A FRACTRAN program is an ordered finite list of positive rational numbers. At each step it multiplies the current positive integer by the first fraction which leaves an integer; if none applies it halts. In prime coordinates,

$$
v_p(Nr)=v_p(N)+v_p(r).
$$

The integrality guard is the nonnegativity of the resulting exponents. For the finite prime set $P$ appearing in the program, the map

$$
\mathbb N_0^P\longrightarrow\{\text{positive $P$-smooth integers}\},
\qquad(x_p)\longmapsto\prod_pp^{x_p}
$$

is an isomorphism of the guarded transition graphs. It induces an isomorphism of their free path categories, including the complete execution trace. This is stronger and more precise than merely saying both formalisms can compute.

The one-fraction program $[3/2]$ sends $2^a3^b$ to $3^{a+b}$ in exactly $a$ steps. For example, $72\to108\to162\to243$ performs $3+2=5$ in prime exponents.

Priority is indispensable. Starting at one,

$$
[2,1/2]:\quad1\to2\to4\to8\to\cdots,
$$

whereas

$$
[1/2,2]:\quad1\to2\to1\to2\to\cdots.
$$

The fractions commute numerically, but their guarded execution does not. Replacing a trace by the product of its fraction labels loses loops, duration, and the applicability conditions.

Conway's original paper contains PRIMEGAME, a decimal-pi-digit PIGAME, and a universal program. Those are classical results with the paper's input and output conventions. Their existence does not provide a source-preserving SUCC compiler or a complexity advantage. In particular, exact pi digit computation does not prove any asymptotic digit statistic.

**Job:** a minimal arithmetic compilation target with explicit state and branch guards. **Next test:** translate a bounded authenticated observer program with trace-level correspondence, preserving the seed and rejecting priority mutations.

## II.8. Numbers as divisor categories, and Möbius as a mixed interaction probe

Let $\mathcal D$ have positive integers as objects and a unique arrow $m\to n$ when $m\mid n$. Prime valuations give an isomorphism with finitely supported prime-exponent vectors ordered coordinatewise. In particular,

$$
\operatorname{Div}(n)\cong\prod_{p\mid n}[0,v_p(n)].
$$

For coprime $m,n$, divisors split as a product; without coprimality they do not. The smallest control is $\operatorname{Div}(4)$, with three objects, against $\operatorname{Div}(2)^2$, with four.

The numerical multiplication monoid has the factorization coproduct $\Delta[n]=\sum_{ab=n}[a]\otimes[b]$. If $F_k(n)$ counts ordered factorizations into $k$ factors greater than one, then

$$
\mu_{\mathbb N}(n)=\sum_{k\ge0}(-1)^kF_k(n).
$$

This follows from the coefficientwise geometric-series inverse of the all-arrows convolution element. For $12$, the nonzero counts are $(F_1,F_2,F_3)=(1,4,3)$, giving zero; for $30$ they are $(1,6,6)$, giving $-1$.

For every arithmetic sequence $a$,

$$
(\mu*a)(n)=\prod_{p\mid n}(I-E_p)a(n),\qquad E_pa(n)=a(n/p),
$$

with each distinct prime shifted once. Hence

$$
(\mu*a)(6)=a(6)-a(3)-a(2)+a(1)
$$

is a complete four-cell mixed difference. A constant plus a sum of functions of individual prime coordinates has zero mixed difference for this contrast, and more generally for a contrast involving at least two distinct primes. A verified nonzero value in that domain therefore refutes that separable model. The restriction matters: for the one-prime example $a(n)=v_2(n)$, $(\mu*a)(2)=1$ although the model uses just one coordinate. This is the structural role of the source-interaction calculation in the intrinsic-Hamiltonian work; no statistical independence follows from prime-coordinate factorization alone.

The exact simplicial relationship is also useful: lower décalage of the multiplication-monoid nerve is the divisibility nerve, via

$$
(x_0,\ldots,x_k)\longmapsto
[x_0\mid x_0x_1\mid\cdots\mid x_0x_1\cdots x_k].
$$

It is not an equivalence between the bare one-object multiplication category and the divisibility category; their endomorphism sets already distinguish them.

One further algebraic guard: the displayed divisor coproduct together with ordinary basis multiplication $[a][b]=[ab]$ is not automatically a bialgebra. At $p^2$, $\Delta[p]^2$ has coefficient two on $[p]\otimes[p]$, while $\Delta[p^2]$ has coefficient one. Any Hopf-algebra claim must specify a compatible multiplication or normalization.

**Job:** categorical decomposition, divisor-aggregation inversion, and complete prime-interaction contrasts. **Next test:** apply the contrast with every required cell and retain source labels; do not infer factor independence from a product coordinate system.

## II.9. Two cheap no-go results that keep the bonus honest

### Ordinary multiplication cannot faithfully encode noncommuting arrows

If an injective map $c:M\to(\mathbb N_{>0},\times)$ preserved composition, then

$$
c(ab)=c(a)c(b)=c(b)c(a)=c(ba),
$$

so $ab=ba$. A noncommutative monoid cannot have such an encoding. The numerical categories here use a transported operation, typed matrix composition, or guarded execution. They do not claim ordinary multiplication preserves arbitrary computation order.

### Every whole cut category is contractible

For an arrow $g:A\to B$, let $\operatorname{Cut}(g)$ have objects factorizations $g=vu$, and a morphism between cuts given by $h$ with $u'=hu$ and $v=v'h$. It has initial cut $(\operatorname{id}_A,g)$ and terminal cut $(g,\operatorname{id}_B)$. Its nerve is therefore contractible.

Thus an invariant that only sees the ordinary homotopy type of this *whole* cut category cannot distinguish the numerical arrows. Interesting information may remain in labels, the projection to the original category, graded nondegenerate factorizations, or a separately specified proper-cut construction. The Möbius formulas above use that additional graded decomposition data; they are not Euler characteristics of an unqualified contractible whole-cut category.

## II.10. What a pair-cancellation certificate must actually prove

For a fixed nonzero integer $h$ and source-selected phases, put

$$
z_n=\exp\left(2\pi i h16^{n-1}\pi\right),\qquad n\ge1.
$$

Partition a finite index set of size $N$ into disjoint pairs $\mathcal P$ and unmatched indices $R$. The triangle inequality gives the exact certificate

$$
\left|\frac1N\sum_nz_n\right|
\le\frac{|R|}{N}+
\frac1N\sum_{\{n,m\}\in\mathcal P}|z_n+z_m|.
$$

If the phase difference of a pair is within $\varepsilon_{nm}$ of a half-integer modulo one, then $|z_n+z_m|\le2\pi\varepsilon_{nm}$, so

$$
\left|\frac1N\sum_nz_n\right|
\le\frac{|R|}{N}+\frac{2\pi}{N}
\sum_{\{n,m\}\in\mathcal P}\varepsilon_{nm}.
$$

**PROVED_CONDITIONAL:** sufficiently small unmatched mass and total pair defect imply cancellation. This is a certificate schema, not a claim that the authenticated orbit admits a source-derived family with those bounds. Selecting pairs after inspecting the target phases merely to minimize the defect does not pay that arithmetic debt.

An exact antipodal scheme is impossible on the authentic orbit. For distinct $n,m$ and nonzero integer $h$, $z_m=-z_n$ would imply

$$
h(16^{m-1}-16^{n-1})\pi\in\mathbb Z+\frac12,
$$

which makes $\pi$ rational. Hence every successful pairing argument must pay a nonzero approximation error; it cannot rest on an exact involution of antipodal pi phases.

Positive and negative calibrations are immediate. On the uniform sixteen-point grid with $h=8$, neighboring points have phases $+1,-1$ and pair exactly. On a coherent zero-phase control, every phasor is $1$ and every pair defect equals two. Both cases pass or fail the certificate for the correct reason.

The analogous CDF identity is the adjacent-block formula retained from round I:

$$
D_{2M}=\frac{D^-+D^+}{2}-\Omega_M.
$$

It measures actual cancellation rather than a categorical representation of it. The probe checks its pointwise rational identity, while the needed source-selected all-epoch bound remains **OPEN**.

## II.11. Earned outcome and next discriminator

The round produces exact equivalences to retract families, affine ideal actions, finite rational linear algebra, and finite-family functors; an explicit affine Möbius inverse; and concrete compilation and cancellation-certificate mechanisms. These statements are useful even if no further normality progress follows. They recover and sharpen the first round's small categorical machines without pretending that a change of coordinates supplies a missing estimate.

The strongest immediate discriminator is a source-preserving candidate for a pair map or signed-overlap estimate, compared against zero forcing, coherent wrong seeds, pole mutants, and the joining controls. Its required output is an actual bound on pair defects or signed overlap. A faithful compiler, an exact categorical equivalence, and a perfect finite algebra receipt are prerequisites for trustworthy computation; they do not replace that bound.
