# A number as a family of source-linked return paths

**Date:** 2026-11-12. **Starting point:** [triadic transport](TRIADIC_TRANSPORT.md).
**Contract:** [PATH_FAMILY_CONTRACT.md](PATH_FAMILY_CONTRACT.md).
**Verdict:** a precise version of the proposed family exists. Its common
return domains give an elementary prime/composite criterion. Coherent
superposition and Yoneda reconstruction require additional, explicitly
retained data. These are local constructions using classical arithmetic and
category theory; no academic priority or algorithmic improvement is claimed.

## 1. What is being decomposed?

The numeral 5 is prime in the multiplicative sense. That does not prevent
several additive/multiplicative routes from reaching its source label. We
decompose a family of operations associated with 5, not its prime
factorization. The chosen operations matter: in the pure divisibility poset
there is just one arrow `1 -> 5`, and no nontrivial return arrow.

Here the carrier is `H = l2(N_{>0})`, with orthonormal basis `e_m` and the
authentic operators

\[
S e_m=e_{m+1},\qquad V_a e_m=e_{am},\qquad V_1=I.
\]

The adjoint `V_n*` divides a basis label by `n` when divisible and gives zero
otherwise. It is a partial inverse, not a reversible dilation on the entire
carrier. The zero output records rejection by its domain condition.

For `n >= 2`, the forward affine operations that send source one to source
`n` have the canonical forms

\[
F_{n,a}=S^{n-a}V_a,\qquad 1\le a\le n,
\qquad F_{n,a}e_m=e_{am+n-a}.
\]

Returning by `V_n*` gives

\[
\boxed{R_{n,a}=V_n^*S^{n-a}V_a.}
\]

Every one of these closes at the unit: `R_{n,a}e_1=e_1`. The endpoint
`a=n` is `V_n*V_n=I` and carries no contraction. Unless explicitly stated,
the return family below uses only `1 <= a < n`.

## 2. Five has four nontrivial canonical return channels

For `n=5` these are:

| Multiplier a | A canonical route from 1 to 5 | Return operation |
| --- | --- | --- |
| 1 | `1 -> 2 -> 3 -> 4 -> 5`, all successor | `V_5* S^4` |
| 2 | `1 -> 2` by multiplication, then three successors | `V_5* S^3 V_2` |
| 3 | `1 -> 3` by multiplication, then two successors | `V_5* S^2 V_3` |
| 4 | `1 -> 4` by multiplication, then one successor | `V_5* S V_4` |

Append the division arrow `5 -> 1` to each displayed route. There is also
the trivial `1 -> 5 -> 1` multiplication/adjoint route, which acts as `I`.
This definition gives `n-1` nontrivial channels for every `n >= 2`. In
particular, 3 already has two channels, and 4 has three. Five does not
initiate the existence of families.

A canonical operation is not the same thing as a literal history. For
example,

\[
S V_2 S=S^3V_2,\qquad S V_2V_2=SV_4,
\]

using `V_2 S=S^2 V_2` and `V_2V_2=V_4`. Different words can therefore
have the same source action. Conversely, the two words `S V_2 S` and
`S V_2 V_2` have the same vertex trace `1 -> 2 -> 4 -> 5`, but act on a
general label as `2m+3` and `4m+1`. A picture that drops arrow labels loses
that distinction. With `S` and every `V_d`, `d>=2`, as primitive growth
arrows, there are seven literal histories from 1 to 5 and five affine
operations. The finite path enumeration in the category audit checks this
convention explicitly; changing the primitive arrows changes that count.

## 3. Exact return law and its infinite boundary

**RPF-01 — PROVED LOCAL.** For all `n>=2`, `1<=a<n`, and `m>=1`,

\[
R_{n,a}e_m=
\begin{cases}
e_{1+a(m-1)/n},&n\mid a(m-1),\\
0,&\text{otherwise}.
\end{cases}
\]

**Proof.** The three operators send `m` successively to `am`, then
`am+n-a=n+a(m-1)`, then divide that label by `n` if possible.

Put `g=gcd(n,a)`, `q=n/g`, and `r=a/g`; thus `gcd(q,r)=1` and `q>r>=1`.
Define the pointed dilation

\[
W_d e_m=e_{1+d(m-1)}.
\]

Then

\[
\boxed{R_{n,a}=W_rW_q^*,\qquad
R_{n,a}e_{1+qk}=e_{1+rk}\quad(k\ge0).}
\]

Its initial projection is `D_q=W_q W_q*`, the indicator of labels congruent
to one modulo `q`. Its range projection is `D_r`. In particular,
`R*R=D_q` and `RR*=D_r`. These are exact partial isometries; their input
and output domains need not coincide.

**RPF-02 — PROVED LOCAL.** For every positive integer `j`,

\[
R_{n,a}^{\,j}=W_{r^j}W_{q^j}^*,\qquad
\|(R_{n,a}^{\,j}-E_{11})x\|^2
=\sum_{k\ge1}|x_{1+q^jk}|^2\longrightarrow0.
\]

For the power formula, the second step can occur precisely when `q` divides
the first surviving `k`, since `q,r` are coprime; induction gives the
formula. For the limit, the displayed sum is bounded by the square-summable
tail beyond `q^j`. Thus every proper return has fixed space `C e_1` and
powers converging strongly to `E_11`. This is not operator-norm convergence:
the unit vector `e_(1+q^j)` has error norm one at time `j`. No finite basis
test proves the strong-limit statement.

No nonunit basis label ever reaches `e_1` under these powers. It follows
smaller admissible labels until a domain condition fails. The strong limit
is a partial-operator statement, not a deterministic particle flow carrying
every input to the unit.

## 4. What primality contributes to the family

**RPF-03 — PROVED LOCAL.** A number `n>=2` is prime exactly when all of its
proper return channels have the same initial domain `D_n`.

If `n=p` is prime, every `1<=a<p` is coprime to `p`, so `q=p` throughout.
For `p=5`,

\[
\boxed{R_{5,a}e_{1+5k}=e_{1+ak},\qquad 1\le a\le4.}
\]

All four channels accept labels `1,6,11,16,...`; at input 6 they produce
`e_2,e_3,e_4,e_5` respectively. Their common input lattice is the special
prime feature, not the existence or count of the channels.

If `n` is composite, choose a proper divisor `d` with `1<d<n` and set
`a=d`. Its denominator is `q=n/d<n`, so its domain strictly contains
`D_n`. For example, the five channels at `n=6` have denominators

\[
(q_{6,1},q_{6,2},q_{6,3},q_{6,4},q_{6,5})=(6,3,2,3,6).
\]

More generally, the possible denominators are exactly the divisors `q>1`
of `n`, with multiplicity `phi(q)`: fixing `q` means writing
`a=(n/q)r` with `1<=r<q` coprime to `q`. This is a divisor profile expressed
through return domains. It is equivalent to familiar gcd information and
does not claim a new fast primality test.

## 5. A single positive observation of the whole family

Retain a register identifying the route and stack the return maps:

\[
\mathcal R_nx=\bigoplus_{a=1}^{n-1}R_{n,a}x,
\qquad K_n=\mathcal R_n^*\mathcal R_n
=\sum_{a=1}^{n-1}R_{n,a}^*R_{n,a}.
\]

**RPF-04 — PROVED LOCAL.** For every `m>=1`,

\[
\boxed{K_n e_m=(\gcd(n,m-1)-1)e_m.}
\]

**Proof.** Each summand contributes one exactly when `n` divides
`a(m-1)`. Write `h=gcd(n,m-1)`. This condition is equivalent to
`n/h` dividing `a`; the allowed values in `1,...,n-1` are
`n/h,2n/h,...,(h-1)n/h`. There are `h-1` of them. The formula also handles
`m=1`, since `gcd(n,0)=n`.

Equivalently,

\[
K_n=\sum_{q\mid n,\ q>1}\varphi(q)D_q.
\]

This identifies the common-carrier family observation with a classical
periodic gcd kernel. It is not an assumption of statistically independent
objects. The cross-route information is retained by `mathcal R_n`; taking
only its Gram operator `K_n` deliberately keeps less information.

There is also an exact version of the earlier wave intuition. Declare the
unit-referenced phase operators

\[
\widehat U_\theta e_m=e^{2\pi i\theta(m-1)}e_m.
\]

A finite geometric sum gives

\[
D_q=\frac1q\sum_{j=0}^{q-1}\widehat U_{j/q},\qquad
K_n=\sum_{q\mid n,\ q>1}\frac{\varphi(q)}q
\sum_{j=0}^{q-1}\widehat U_{j/q}.
\]

Indeed, the average is one when `q` divides `m-1`, and zero otherwise.
Thus a prime return family has one common admission period; a composite
family combines the proper-divisor periods as well. The phase reference at
one is specified, and these are exactly defined Fourier operators, not
unspecified physical radiation. Individual nonzero rational frequencies may
have smaller periods; the common-period statement concerns `D_q` itself.

Set `P_n=K_n/(n-1)`. It is a positive contraction and

\[
\boxed{n\text{ is prime}\quad\Longleftrightarrow\quad P_n^2=P_n.}
\]

For a prime `p`, `P_p=D_p`. For composite `n`, a proper divisor `d`
and source label `m=1+d` give eigenvalue `(d-1)/(n-1)` strictly between
zero and one, refuting idempotence. One complete period suffices to inspect
this operator identity, because its diagonal is `n`-periodic; the universal
claim follows from the arithmetic proof rather than a fixed finite sweep.

| n | Labels m | Diagonal of P_n |
| --- | --- | --- |
| 5 | 1 through 6 | `1,0,0,0,0,1` |
| 6 | 1 through 7 | `1,0,1/5,2/5,1/5,0,1` |

For **every** `n`, `Fix(P_n)` is the range of `D_n`; primality changes
whether there are intermediate eigenvalues, not that fixed space. As a
spectral filter, this observation acts on the input labels `m`, with `n`
held fixed. It must not be confused with the earlier operator whose fixed
labels themselves are the primes.

## 6. Coherent paths require their relative phases

**RPF-05 — PROVED LOCAL construction and countermodel.** A linearized path
family permits

\[
T_c=\sum_a c_aR_{n,a}.
\]

The complex coefficients, source frame, and final observation must be
declared. A bare category supplies composition but does not supply these
amplitudes or their normalization. The measured squared norm expands as

\[
\|T_cx\|^2=
\sum_{a,b}\overline{c_a}c_b
\langle R_{n,a}x,R_{n,b}x\rangle.
\]

The off-diagonal terms are the interference data. If the route register is
retained as an orthogonal label, the squared norm of the direct sum contains
only the diagonal terms. Erasing or comparing routes coherently is an extra
operation. These Hilbert-space identities alone assert no physical quantum
implementation or speedup.

For an exact example let `n=5`,

\[
x=(3e_6+4e_{11})/5,\qquad C=(R_{5,1}+R_{5,2})/2.
\]

The state has unit norm and `C` is a contraction. Direct calculation gives

\[
Cx=(3e_2+7e_3+4e_5)/10,\qquad \|Cx\|^2=37/50.
\]

Now let `D` fix every basis vector except `e_3`, whose sign it reverses,
and replace only `R_{5,1}` by `D R_{5,1}`. Every initial projection
`R*R`, every unit return, the full `K_5`, and the strong unit limits are
unchanged. The last assertion follows because the index map and all
absolute coefficients of every power are unchanged. Nevertheless,

\[
\widetilde Cx=(3e_2-e_3+4e_5)/10,
\qquad\|\widetilde Cx\|^2=13/50.
\]

Both diagonal-only contributions are `1/2`. The cross term is `+6/25`
versus `-6/25`. Therefore even complete return strengths do not reconstruct
the coherent path family. This mutation changes a transport, not merely a
common coordinate convention. If all components and the observation were
changed by a consistent gauge, their observable values would agree.

The arithmetic operations here have real positive matrix entries; no
nontrivial phase is secretly generated by the prime 5. The phase mutation
shows which data an observer must retain when additional transports are
introduced.

## 7. A correctly typed Yoneda link

Define the small category `A` with positive integers as objects and

\[
\operatorname{Hom}_{\mathcal A}(m,n)
=\{(a,b):a\ge1,\ b\ge0,\ am+b=n\}.
\]

An arrow is the entire affine operation, not just its value at one input.
Composition is

\[
(a,b)\circ(c,d)=(ac,ad+b),
\]

and the identity is `(1,0)`. Its operator realization sends `(a,b)` to
`S^bV_a`; the source braid ensures that composition is preserved. Formally
one may send the object `m` to the pointed Hilbert space `(H,e_m)` and use
bounded linear maps that preserve the specified point. This keeps integers,
vectors, and operators as distinct types.

The forward category has no nonidentity descending arrows. The return
`V_n*` belongs to the larger category of pointed Hilbert maps or of partial
source maps; it is not smuggled into `A`. This distinction is necessary when
calling a source trajectory a categorical loop.

**RPF-06 — CLASSICAL theorem with a local application.** The representable
presheaf

\[
h_n(m)=\operatorname{Hom}_{\mathcal A}(m,n)
\]

retains all incoming probes and their precomposition. Yoneda gives

\[
\operatorname{Nat}(h_m,h_n)\cong
\operatorname{Hom}_{\mathcal A}(m,n).
\]

The local proof is short: an arrow `f:m->n` gives the components
`g |-> f o g`. Conversely, a natural transformation `eta` gives
`f=eta_m(id_m)`, and naturality against each `g:x->m` forces
`eta_x(g)=f o g`. These constructions are inverse. This is the exact sense
in which a whole object is linked to its compatible incoming relations.
See Riehl, *Category Theory in Context*, Theorem 2.2.4 and Corollary 2.2.8
([author-hosted text](https://emilyriehl.github.io/files/context.pdf)).

In particular, each individual route `f:1->5` gives a natural transformation
`h_1 -> h_5`. That is already a valid Yoneda link from the route to the whole
representable object. It does not yet express `h_5` as a sum or gluing of
those images.

For this category `|h_n(m)|=floor(n/m)`, and `h_n(1)` has precisely the
`n` canonical affine routes. Its cardinality already identifies `n`
**within this declared model**. It still does not supply the full Yoneda
structure automatically. Restricting probes to the object 1 leaves the
finite set of routes and arbitrary functions between such sets. For `n=2`
there are four functions from this two-element set to itself, while
`Hom_A(2,2)` consists only of the identity. The function that swaps the two
routes cannot extend to a natural transformation: naturality against each
arrow `1->2` would force that arrow to be fixed.

Thus this restricted observation is faithful on arrows but not full. A
smaller family of test objects can suffice in some categories, provided a
full-faithfulness/density argument is proved. The phrase “all probes” is a
safe general theorem, not a claim that every application needs infinitely
many tests. In the present incoming profile for fixed finite `n`, all
components with `m>n` are empty.

The category of incoming arrows is the slice `A/n`, retaining factorizations
between routes. This packages compatibility; it does not assert that some
selected proper loops form a cover or a colimit presentation. Including
the identity `n->n` trivially includes the whole object. Reconstructing it
from a smaller generating diagram requires a separate universal-property
proof. Yoneda also does not turn a set of paths into their coherent sum;
that is the additional linearization in Section 6.

There is an exact obstruction to one especially tempting gluing claim in
this particular forward category. **No diagram made only of representables
`h_m` with `m<n` can have colimit `h_n` in the presheaf category.** Evaluate
the proposed colimit at the test object `n`. Every `h_m(n)` is empty because
there is no descending affine arrow. Their colimit in sets is empty, whereas
`h_n(n)={id_n}`. Presheaf colimits are computed componentwise, giving a
contradiction. This is a boundary of the chosen category, not a prohibition
on a different category with return arrows, an appropriate coverage, or a
separately proved presentation. The enlarged category would need a new
Yoneda analysis; its incoming morphisms are no longer the ones counted here.

## 8. A source counterfeit that preserves all small unit returns

**RPF-07 — PROVED LOCAL countermodel.** Let `f` transpose 11 and 13 and fix
all other labels. Set `F e_m=e_(f(m))` and
`V_d^f=F V_d F*`, while leaving the ordinary successor `S` unchanged.
Use the same return words with these transported multipliers.

For every `2<=n<=10` and every proper `a`, the unit route still closes:
the three source labels involved in the canonical word are `1,a,n`, all
fixed by `f`. The transposition also preserves the arithmetic degree
`Omega`, since 11 and 13 are both prime. Local closure and degree-only
information therefore pass.

At `n=5,m=11`, the four genuine return outputs are `e_3,e_5,e_7,e_9`.
The transported outputs are `e_3,0,0,0`: the multiplier routes for
`a=2,3,4` lead before division to `29,41,53`, none divisible by 5.
Thus the family strengths are 4 versus 1. At `m=13`, the genuine strength
is zero whereas the transported strength is three. A common-source family
probe rejects a source that unit returns alone accept. The explicit
executable receipt is `return_paths_source_probe.py`.

This counterfeit preserves primes as a set. It tests the coupling between
successor and multiplication, not a changed count of ordinary prime pairs.
The separate phase mutation in Section 6 passes even the full `K_5` test.
Consequently the useful hierarchy of observations is: unit closure, domain
profile, and coherent mixed products. Each is stronger in a demonstrated
respect; none is silently identified with the unresolved prime-pair bound.

## 9. Motion and higher coherence

The [motion companion](MOTION_AND_COHERENCE.md) supplies the precise content
of the quaternion comparison. Positions, transformations, coordinate
representations, and coherence between compositions are different objects.
In three-dimensional Euclidean space, positions and translations each have
three degrees of freedom; rotations also have three, while a unit quaternion
stores them in four constrained real coordinates with a two-to-one sign
ambiguity. This does not produce a universal rule `n -> n+1`.

A separate classical appearance of five is Mac Lane's pentagon: four ordered
factors have five parenthesizations, and their reassociation maps must agree
along two alternative routes. Its relation to this project is the demand
for compatible paths. It is not a decomposition theorem for the prime 5.

## 10. Claim ledger and remaining dependency

| Claim | Status and exact scope | Countercontrol / boundary |
| --- | --- | --- |
| RPF-01 | Return law, reduced denominator and partial-isometry domains: PROVED LOCAL | Wrong source offset changes domains; a=n gives I. |
| RPF-02 | Strong unit limit and unique fixed span for each proper return: PROVED LOCAL | Norm error remains one; rejected labels do not travel to 1. |
| RPF-03 | Common return domain iff n is prime; divisor/totient profile: PROVED LOCAL | Composite6 has denominators6,3,2,3,6. |
| RPF-04 | Family Gram equals gcd(n,m-1)-1; normalized idempotence iff prime: PROVED LOCAL | Intermediate composite eigenvalues; fixed space alone is insufficient. |
| RPF-05 | Coherent mixed products carry information absent from strengths: PROVED LOCAL | Exact37/50 versus13/50 sign-transport mutation. |
| RPF-06 | Full Yoneda reconstruction: CLASSICAL; concrete restricted failure: PROVED LOCAL | Root-route cardinality does identify n here, but arbitrary root-set functions do not respect naturality. |
| RPF-07 | Small-unit-loop counterfeit rejected by the family profile: PROVED LOCAL | Swap11/13 preserves degree and all unit returns for n<=10. |
| RPF-08 | A universal successive-number dimension law: UNVERIFIED as an unspecified proposal; the literal n+1 rotation-DOF law is REFUTED | SO(3) has dimension3 and SO(4) has dimension6; see companion. |

The finite probes test implementations and explicit countermodels. The
proofs above establish the stated quantified identities. Same-model agents
and implementations sharing these identities are not independent witnesses
for a conjecture. The new observation repackages gcd structure exactly; it
does not derive a uniform additive prime-pair remainder, and the corresponding
frontier in [NEXT.md](NEXT.md) remains open.
