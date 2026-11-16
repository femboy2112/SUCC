# Return paths: independent category and operator audit

**Date:** 2026-11-12. **Scope:** the candidate in
[PATH_FAMILY_CONTRACT.md](../PATH_FAMILY_CONTRACT.md), read independently of
the constructor implementation. **Verdict:** the proposed family has an
exact arithmetic profile. Yoneda can link its forward routes to the whole
object, but reconstruction from return values or from only proper lower
representables requires additional hypotheses and fails in specific forms.
The result is an elementary construction; no academic novelty is claimed.

## 1. The typed forward category

Let `C` have positive integers as objects and

\[
 C(m,n)=\{(a,b):a\in\mathbb N_{>0},\ b\in\mathbb N_0,
                  \ am+b=n\}.
\]

A morphism retains the entire affine rule `x -> ax+b`, not just its value at
the distinguished source object. If `f=(a,b):m->n` and `g=(c,d):k->m`, set

\[
f\circ g=(ac,ad+b):k\longrightarrow n.
\]

Associativity follows either from substitution of functions or from expanding
the two coefficient pairs. The identity is `(1,0)`. Every morphism satisfies
`m<=n`; an endomorphism requires `am+b=m`, hence `a=1,b=0`. Consequently
there are no nonidentity directed loops or nonidentity isomorphisms in `C`.

The Hilbert assignment sends every object to the shared
`H=l2(N_{>0})` and `(a,b)` to `S^b V_a`. It is functorial because
`V_a S^d = S^(ad) V_a`. It can instead be regarded as a functor into pointed
Hilbert spaces by sending `m` to `(H,e_m)`; the arrow carries `e_m` to `e_n`.
Neither presentation makes this representation a fully faithful Yoneda
embedding. A return by `V_n*` uses an additional bounded partial inverse,
outside the forward category. The operator loop and the forward categorical
arrow therefore have different types that must remain explicit.

The divisor category is different again: a prime object has no proper
intermediate factorization of its arrow `1->p`. An additive/multiplicative
route family does not refute multiplicative irreducibility.

## 2. Literal histories, affine maps, and return channels differ

Use successor and all multiplications `V_d`, `d>=2`, as primitive growth
arrows, excluding identity steps. Every such step strictly increases the
positive source label, so there are finitely many histories from 1 to any
fixed `n`. Quotienting histories by their actual affine action identifies
words using, among other equations,

\[
V_dV_e=V_{de},\qquad V_dS=S^dV_d.
\]

At 5 there are **seven histories**, **five affine maps**, and **four
nontrivial return operators** under these conventions. For example,

\[
SV_2S=S^3V_2,\qquad SV_2V_2=SV_4.
\]

The first equation identifies the histories with vertex traces
`1->2->4->5` and `1->2->3->4->5`. Conversely, `SV_2S` and `SV_2V_2`
have the *same* trace `1->2->4->5` but different first-arrow labels. Their
actions are `2m+3` and `4m+1`, respectively; at source 2 they give 7 and 9.
Forgetting those labels loses source information.

Each affine arrow `1->n` is uniquely

\[
F_{n,a}=S^{n-a}V_a,\qquad 1\le a\le n.
\]

The direct arrow `V_n` gives `V_n*V_n=I`; removing it leaves the four
nontrivial channels at 5. Choosing only prime multiplier generators changes
the number of histories, while retaining these affine maps because composite
multipliers factor. These counts are properties of the chosen presentation,
not an intrinsic decomposition of the numeral 5 into seven entities.

## 3. Exact operator derivation

For `n>=2` and `1<=a<n`, literal multiplication, succession, and partial
division give

\[
R_{n,a}e_m=V_n^*S^{n-a}V_ae_m
=\begin{cases}
e_{1+a(m-1)/n},& n\mid a(m-1),\\
0,&\text{otherwise}.
\end{cases}
\]

Put `g=gcd(n,a)`, `u=a/g`, `v=n/g`; then `gcd(u,v)=1` and `u<v`.
Define the pointed dilation `W_d e_m=e_{1+d(m-1)}`. The operator is

\[
R_{n,a}=W_uW_v^*,\qquad
R_{n,a}^*R_{n,a}=W_vW_v^*.
\]

Thus its initial space is spanned by labels congruent to 1 modulo `v`.
For every integer `r>=1`, coprimality shows

\[
R_{n,a}^{\,r}=W_{u^r}W_{v^r}^*,\qquad
\|(R_{n,a}^{\,r}-E_{11})x\|^2
=\sum_{k\ge1}|x_{1+v^r k}|^2\longrightarrow0.
\]

The limit uses the square-summable tail and `v>=2`. Every fixed vector
therefore lies in `Ce_1`, and the unit is fixed. The norm error is exactly
one: input `e_{1+v^r}` has output `e_{1+u^r}`, orthogonal to the unit.
These facts hold for composites as well as primes.

At prime 5, every proper `a` is coprime to 5, so the four channels have the
same initial space, labels `1 mod 5`. At source 6 their outputs, in order
`a=1,2,3,4`, are `e_2,e_3,e_4,e_5`. At composite 6, channel `a=3`
admits source 3 and returns `e_2`, while channel `a=1` rejects that source.
This is a concrete failure of the common-domain property.

## 4. Family observation and primality boundary

Define the finite positive operator

\[
K_n=\sum_{a=1}^{n-1}R_{n,a}^*R_{n,a}.
\]

For fixed `m`, let `d=gcd(n,m-1)`. The condition `n|a(m-1)` is equivalent
to `(n/d)|a`. Exactly `d-1` such positive multiples lie below `n`. Hence

\[
\boxed{K_ne_m=(\gcd(n,m-1)-1)e_m.}
\]

In particular, `K_n/(n-1)` is a positive contraction. It is a projection
if `n` is prime, because every eigenvalue is zero or one. Conversely, if
`n` is composite and `d` is a proper divisor with `1<d<n`, the input
`e_{1+d}` has eigenvalue `(d-1)/(n-1)` strictly between zero and one.
Thus projection is equivalent to primality for all `n>=2`.

Grouping channels by reduced denominator gives another exact description:

\[
K_n=\sum_{\substack{q\mid n\\q>1}}\varphi(q)W_qW_q^*.
\]

For each divisor `q>1`, the possible `a` with `n/gcd(n,a)=q` are exactly
`a=(n/q)u`, where `1<=u<q` and `gcd(u,q)=1`, giving `phi(q)` channels.
This is classical divisor counting expressed through the shared carrier.
It does not give an asymptotic improvement over ordinary primality methods.

The normalization and exclusion of `a=n` are load-bearing: including the
identity adds `I` to `K_n`, and the displayed projection criterion with
normalization `n-1` fails even on the unit at prime 5. The empty `n=1`
family does not support that normalization.

## 5. What Yoneda links, and what it does not infer

The representable presheaf of `n` is

\[
h_n(m)=C(m,n),\qquad |h_n(m)|=\lfloor n/m\rfloor.
\]

An arrow `g:k->m` acts by precomposition: `h_n(g)(f)=f g`. The Yoneda
lemma identifies natural transformations `h_m -> h_n` with arrows `m->n`.
Consequently each route `f:1->n` really does provide a natural map
`h_1 -> h_n`, sending every incoming test arrow to its composite with `f`.
The compatibility with precomposition is the content of the link.

The classical references are Emily Riehl's author-hosted
[Category Theory in Context](https://emilyriehl.github.io/files/context.pdf),
Theorem 2.2.4 and Corollary 2.2.8. The version inspected has 299 PDF pages;
the statements occur on printed pages 61 and 64. Definition 6.5.11, printed
page 247, characterizes dense probes through full faithfulness of restricted
Yoneda. Definition 2.4.2 and Example 2.4.6 describe categories of elements
and slices. No source PDF is redistributed here.

Several distinct reconstructions must not be conflated:

1. **Object label from root-set cardinality.** In this already specified
   category, `|h_n(1)|=n`, so the cardinality identifies the integer label.
   It would be false to claim the root data conveys nothing.
2. **All arrows and their composition.** The restricted functor `C(1,-)`
   is faithful: a morphism `(a,b):m->n` sends root-route index `r` to `ar`,
   and its value at `r=1` identifies `a`, then `b=n-am`. It is not full.
   The root sets for object 2 admit four set endomorphisms, while `C(2,2)`
   contains only the identity. In particular swapping the two root routes
   fails naturality against `S:1->2`: the identity of object 2 pulls back
   to `S`, whereas the swap sends that route to `V_2`.
3. **Values of return loops at the unit.** Every `R_{n,a}e_1=e_1`, so
   those values alone forget the different operators, domains, and labels.
4. **A genuine representation theorem.** Full representables determine
   objects up to isomorphism. A smaller test family can suffice, but that
   requires an appropriate proved density/full-faithfulness assertion.

The category of elements of `h_n` is the slice `C/n`: its objects are
routes `m->n`, and its arrows compare factorizations. This provides a useful
organization of the family. It has terminal object `(n,id_n)`. Reconstructing
`h_n` from the full canonical diagram therefore already includes `h_n`
itself, and is not a theorem that proper inner loops suffice.

There is a sharp obstruction to that stronger interpretation in this
category. **No colimit of a diagram consisting only of representables
`h_m` with `m<n` can equal `h_n`.** Evaluate the presheaves at object `n`.
Every such `h_m(n)` is empty; their pointwise colimit is empty. But
`h_n(n)={id_n}` is not empty. The proper lower objects cannot supply the
missing identity test. A different category, a specified coverage or
descent condition, or additional generators would require a new argument.

Finally, a presheaf of sets does not itself carry sums of arrows. Coherent
amplitudes require a declared linearization, scalar field, representation,
and measurement frame. Yoneda does not supply those choices automatically.

## 6. A phase counterfeit that passes the family profile

Let `D` be the diagonal unitary that negates `e_3` and fixes every other
basis vector. At `n=5` replace only `R_{5,1}` by
`R'_{5,1}=D R_{5,1}`. Keep the other three channels and the common output
frame unchanged.

Every initial projection remains identical, since
`(DR)*DR=R*R`. Every unit anchor is unchanged because `D e_1=e_1`.
The changed channel has the same strong limit `E_11`: its iterates have
the same supported input labels and output magnitudes as the authentic
channel, so the tail proof applies. Its fixed space is still `Ce_1`.

Nevertheless the coherent observation changes. For the normalized source

\[
x=(3e_6+4e_{11})/5,\qquad
C=(R_{5,1}+R_{5,2})/2,\quad
C'=(DR_{5,1}+R_{5,2})/2,
\]

direct calculation gives

\[
Cx=\tfrac3{10}e_2+\tfrac7{10}e_3+\tfrac25e_5,
\qquad
C'x=\tfrac3{10}e_2-\tfrac1{10}e_3+\tfrac25e_5.
\]

Thus

\[
\boxed{\|Cx\|^2=37/50,\qquad \|C'x\|^2=13/50,}
\qquad
\tfrac14\|R_{5,1}x\|^2+\tfrac14\|R_{5,2}x\|^2=1/2.
\]

The separate intensity remains `1/2` for the altered family too. Both `C`
and `C'` are contractions, since each averages two contractions. The minus
sign is a declared relative phase in a shared basis, not an inferred quantum
mechanism. A simultaneous global change of output basis on every channel
would leave these norms invariant; this control changes one route relative
to the others. The example proves that `K_n`, local anchors, and strong
limits do not authenticate full path coupling.

## 7. Executed independent finite audit

`return_paths_independent_audit.py` imports no return-path implementation.
It evaluates literal generator words and their reversed adjoints, compares
them with a separately written reduced-fraction formula, and checks the
gcd family diagonal. It also enumerates strict-growth histories, verifies
typed affine composition and associativity, and executes the category and
phase counterexamples above.

The actual run completed with **353,330 checks, PASS**, recorded in
[RETURN_PATH_INDEPENDENT_AUDIT.json](../receipts/RETURN_PATH_INDEPENDENT_AUDIT.json).
The prefix uses `2<=n<=64` and source labels `1..130`; holdout target labels
are `67,97,101,121,143,169,221,257`. Named mutation controls reject a lost
`m-1` offset, rounded division, an included identity channel, and a composite
common-domain claim. These are finite implementation checks. The universal
results above depend on the displayed proofs, and same-model code review
is not an independent external proof witness.

## Verdict and next discriminating question

**SURVIVES — PROVED LOCAL:** exact return operators, gcd profile, prime
projection criterion, all-channel unit fixation and strong convergence.

**SURVIVES — CLASSICAL specialization:** Yoneda links each forward path
through a natural transformation once the category and precomposition are
declared.

**FAILS in the specified forms:** unit-return values or the diagonal family
profile determine all coupling; a root-set bijection is automatically
natural; proper lower representables alone glue to the whole `h_n`.
The explicit witnesses and empty evaluation at `n` are the receipts.

The next useful question is which phase-calibrated cross-channel products
are forced by authentic source composition and what further arithmetic
information they control. This audit supplies no source-specific uniform
prime-pair remainder estimate and does not close the existing open frontier.
