# Position, transformation, and coherence

**Date:** 2026-11-12. **Companion:** [return-path contract](PATH_FAMILY_CONTRACT.md).
**Verdict:** the useful hierarchy is between states, transformations, and
compatibility of transformations. Quaternion coordinates and the categorical
pentagon illustrate different aspects of that hierarchy. They do not establish
a universal rule assigning a new kind of dynamics to each successive integer.
All group and coherence results cited below are classical; academic novelty is
not claimed.

## 1. Three quantities that must be kept separate

A position in Euclidean `d`-space is a vector `x` in `R^d`. A rigid motion is
a transformation `x -> R x + t`, where `R` belongs to `SO(d)` and `t` belongs
to `R^d`. The coordinates used to *store* that transformation need not be a
minimal set of independent parameters.

| Space dimension `d` | Position / translation parameters | Rotation parameters | Rigid-motion parameters |
| --- | --- | --- | --- |
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |
| 5 | 5 | 10 | 15 |

Here rotations preserve orientation; discrete reflections do not add a
continuous degree of freedom. The formulas are

\[
\dim SO(d)=\frac{d(d-1)}2,\qquad
\dim SE(d)=d+\frac{d(d-1)}2=\frac{d(d+1)}2.
\]

**MOT-01 — CLASSICAL, with local derivation.** Differentiate `R(t)^T R(t)=I`
at `R(0)=I`. Its tangent `A` satisfies `A^T+A=0`: diagonal entries vanish,
and each of the `d(d-1)/2` entries above the diagonal is free. Conversely,
`exp(tA)` is orthogonal with determinant one for every real skew-symmetric
`A`, giving the local rotation parameters. A rigid motion additionally has
the independent translation vector `t`. For the group-dimension statement,
see Vincent Bouchard's official [Lie groups notes, Example 4.1.9](https://sites.ualberta.ca/~vbouchar/MAPH464/section-Lie-groups.html).

No extra coordinate is necessary merely to move: `x(t)=x_0+t v` is already
a motion in `R^d`. Observation is another question. For example, three exact
distances to noncollinear coplanar landmarks in `R^3` generally leave two
mirror-related positions. With landmarks `(0,0,0)`, `(1,0,0)`, `(0,1,0)`, the
positions `(0,0,1)` and `(0,0,-1)` have identical squared ranges `(1,2,2)`.
Triangulation, parallax, and range measurements have different data and
nondegeneracy requirements. A bare numeral three does not specify those.

## 2. What the quaternion's fourth coordinate does

Write a quaternion as

\[
q=w+x\mathbf i+y\mathbf j+z\mathbf k,
\qquad w^2+x^2+y^2+z^2=1.
\]

The unit constraint defines the three-dimensional sphere `S^3` in `R^4`.
Thus four stored real numbers have **three independent continuous
parameters**. A three-dimensional vector is identified with an imaginary
quaternion, and rotation is

\[
v\longmapsto qv q^{-1}.
\]

Both `q` and `-q` induce the same map. Unit quaternions form
`Spin(3) = SU(2)` and give a two-to-one covering of `SO(3)`. This is a
global representation with a constraint and a sign redundancy, not a fourth
physical displacement direction or a fourth rotation degree of freedom.
Rotation matrices provide another representation. These statements and the
quaternion multiplication convention are described in John Baez's authored
[quaternion exposition](https://math.ucr.edu/home/baez/octonions/conway_smith/),
the paragraphs beginning “As a vector space” through the double-cover
construction. **MOT-02 — CLASSICAL.**

There is a useful *path* feature. For a fixed unit imaginary quaternion `u`,

\[
q(\theta)=\cos(\theta/2)+u\sin(\theta/2)
\]

continuously lifts rotation by angle `theta`. At angle `2*pi`, the spatial
orientation has returned to its start, while the chosen lift has reached
`-1`; at `4*pi`, the lift returns to `1`. The explicit endpoints are exact.
One can therefore retain information about a continuous transport path that
is absent from its final orientation alone. This is a statement about the
chosen covering representation. It supplies neither a physical hidden
dimension nor a quantum mechanism.

### An exact order-sensitive witness

The quarter-turn intuition can be tested without square roots or floating
point. Take the rational unit quaternions

\[
q=\frac35+\frac45\mathbf i,\qquad
r=\frac35+\frac45\mathbf j.
\]

Using `ij=k=-ji`,

\[
qr=\frac{9+12\mathbf i+12\mathbf j+16\mathbf k}{25},\qquad
rq=\frac{9+12\mathbf i+12\mathbf j-16\mathbf k}{25}.
\]

These are neither equal nor negatives of one another. Their conjugation
actions on `i` differ:

\[
(qr)\mathbf i(qr)^{-1}
=\frac{-175\mathbf i+576\mathbf j+168\mathbf k}{625},
\]
\[
(rq)\mathbf i(rq)^{-1}
=\frac{-175\mathbf i-600\mathbf k}{625}.
\]

**MOT-03 — PROVED LOCAL by displayed multiplication.** The witness shows
why a transformation model must retain composition order. Merely observing
`ij=-ji` would be an insufficient rotation witness: `k` and `-k` represent
the same spatial rotation. The finite probe retains that negative control.

## 3. Generalization has more than one possible meaning

The faithful general lesson is: specify the configuration space, the allowed
transformations, and the action relating the two. Their dimensions and
representations can then be derived. The dimensions in the first table
already disprove a universal “one extra independent coordinate for movement”
rule, for this precise rigid-motion interpretation. They do not refute every
possible future meaning of “successive number layers.” Such a meaning needs
its own objects and comparison maps.

Several classical extensions answer different questions:

- Affine motion in `R^d` can be stored as a `(d+1)`-by-`(d+1)` homogeneous
  matrix, acting on `(x,1)`. The last coordinate is fixed; it is not an
  independent physical dimension. For rigid motion the matrix is
  `[[R,t],[0,1]]`, and its product records `R_1 R_2` and `R_1 t_2+t_1`.
- Spin groups provide covering groups for rotations. In four dimensions,
  **two** unit quaternions act by `v -> q_L v q_R^{-1}`, with the common
  sign pair giving the same rotation. This has six continuous parameters,
  matching `SO(4)`. The same Baez source explicitly states this double cover.
- Clifford algebras organize rotations in arbitrary dimension. Their
  ambient algebra size and spin-group dimension are different quantities.
  Under the convention `v^2=-||v||^2`, Baez's authored
  [Clifford-algebra section](https://math.ucr.edu/home/baez/octonions/node6.html)
  defines the algebra and explains how it generalizes quaternion algebra.

These constructions can be useful design languages for a carrier. Choosing
one is additional mathematical structure; it cannot be inferred solely from
the primality or magnitude of the carrier's integer label. **MOT-04 — exact
counterexample to the stated dimension rule, with an interpretation boundary.**

## 4. A precise place where five enters: the pentagon

There is a different classical construction particularly close to the
intuition of several inner routes that must agree. For four objects
`A,B,C,D`, binary combination has exactly five parenthesizations:

\[
(((AB)C)D),\quad ((A(BC))D),\quad A((BC)D),\quad
A(B(CD)),\quad (AB)(CD).
\]

In a monoidal category, changing parentheses uses a specified natural
isomorphism

\[
\alpha_{A,B,C}:(A\otimes B)\otimes C\longrightarrow
A\otimes(B\otimes C).
\]

The **pentagon condition** compares two composites from the completely
left-associated product to the completely right-associated product:

\[
\begin{aligned}
&\alpha_{A,B,C\otimes D}\circ\alpha_{A\otimes B,C,D}\\
={}&(1_A\otimes\alpha_{B,C,D})\circ
\alpha_{A,B\otimes C,D}\circ
(\alpha_{A,B,C}\otimes1_D).
\end{aligned}
\]

The first route has two reassociations; the second has three. The five
parenthesizations are the vertices of the comparison pentagon. This is
the two-dimensional associahedron for four factors. No object has been
identified with the integer prime 5 by this construction.

**MOT-05 — CLASSICAL.** See Etingof, Gelaki, Nikshych, and Ostrik,
[*Tensor Categories*, Definition 1.1.1, equation (1.1.2)](https://math.mit.edu/~etingof/tenscat.pdf).
Emily Riehl's [*Category Theory in Context*, Exercise 3.3.ii and
Epilogue E.2](https://emilyriehl.github.io/files/context.pdf) gives the
five-parenthesization example and the coherence perspective. No new monoidal
structure on the arithmetic return-path family is asserted here; its tensor
operation, associators, unit, and coherence proofs would first have to be
specified.

### Local compatibility can fail globally

There is an exact adversarial example. Over real or complex vector spaces,
let `alpha` be the standard tensor reassociation and replace every component
by `alpha'=-alpha`. Each component remains an invertible linear map, and the
family remains natural: multiplying both sides of a naturality square by
the same scalar preserves equality.

However, the two-edge pentagon route now acquires sign `(-1)^2=+1`, and the
three-edge route acquires `(-1)^3=-1`. Their outputs disagree on every
nonzero simple tensor for which the tensor product is nonzero, for example
on the tensor of four unit vectors in four one-dimensional spaces. Thus
these local isomorphisms fail the pentagon and do not define a monoidal
category. **MOT-06 — PROVED LOCAL countermodel.**

This is directly relevant to a proposed family of inner arithmetic loops:
assigning an equivalence to each local piece does not, by itself, prove that
the equivalences respect all composites. It is the comparison diagram that
adds a test. For a family of `k` inputs, the number of ordered full binary
parenthesizations follows the recurrence

\[
C_0=1,\qquad C_{j+1}=\sum_{i=0}^{j}C_i C_{j-i}.
\]

The root split supplies this recurrence, so three, four, and five inputs
give respectively `2,5,14` parenthesizations. The next layer is already
fourteen, not six. A coherent hierarchy can exist without following the
sequence of consecutive integers as its complexity count.

## 5. Executable scope and claim ledger

`motion_probe.py` uses exact rational quaternion arithmetic and explicit
finite tuple reassociation. It checks norm-preserving rotation matrices,
their group-action composition, sign redundancy, the order-sensitive witness,
the failed half-turn witness, five parenthesizations and their pentagon graph,
the two reassociation routes, and the sign-mutation failure. Its output is
`receipts/MOTION_REPORT.json`; only an actual run can certify those finite
checks. No floating-point calculation is used.

| Claim | Status | Boundary / next falsifier |
| --- | --- | --- |
| MOT-01 | CLASSICAL; local dimension derivation supplied | Position, rotation, and full rigid motion are different spaces. |
| MOT-02 | CLASSICAL covering representation | Four quaternion coordinates do not imply four rotation degrees of freedom. |
| MOT-03 | PROVED LOCAL exact order-sensitive witness | Compare actions, because quaternion inequality alone can be a sign redundancy. |
| MOT-04 | REFUTED for the universal extra-coordinate dimension rule | A separately defined successive-layer hypothesis remains to be stated. |
| MOT-05 | CLASSICAL pentagon for four inputs | No link to primality, and no arithmetic monoidal structure yet specified. |
| MOT-06 | PROVED LOCAL sign-mutated associator countermodel | Any proposed gluing must be checked on actual composite maps. |

The useful next question for the arithmetic dossier is whether its chosen
return maps carry enough shared-source composition data to distinguish an
authentic family from a locally indistinguishable counterfeit. Quaternion
and pentagon examples explain why retaining path order and compatibility is
valuable; they supply no missing prime-pair estimate themselves.
