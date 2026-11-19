# Live sister-work synthesis: the literal source generates the fifth-prime block

PR [666](https://github.com/femboy2112/SUCC/pull/666) appeared while this
operation was validating. Its head is pinned at
`7d2648374a9123e433c6d62c0a88933194a361c7`. The overview, Fibonacci source
transport proof, and causal-memory proof were read directly. Their blob
identities are in `validation/source_map.json`. This note imports their stated
algebra with attribution and checks the new operator-level connection below;
it does not merge that branch or borrow its test results.

## 1. One authentic polynomial identity, three different representations

Keep the literal signed source

\[
Q(t)=4-2t^3-t^4-t^5=(1-t)H(t),\qquad
H(t)=4+4t+4t^2+2t^3+t^4.
\]

The complementary filter in PR666 is

\[
K(t)=(2-t^2)(t^2-2t+2)=4-4t+2t^3-t^4,
\qquad H(t)K(t)=16-t^8.
\]

This inherited polynomial identity can be checked by direct multiplication.
For every square matrix X it yields H(X)K(X)=16I-X^8. The representation
and its boundary determine what the right side means:

| Declared representation | Relation | Exact product |
| --- | --- | --- |
| Eight-channel cyclic shift S | S^8=I | H(S)K(S)=15I |
| Eight-entry causal backshift L with zero prehistory | L^8=0 | H(L)K(L)=16I |
| Fibonacci inverse model M=A^(-1) | M^2+M=I | H(M)K(M)=3(I+7M) |

Thus 15=3*5 versus 16=2^4 is an exact boundary-dependent arithmetic effect.
The first two rows are finite channel filters, not the chronological BBP orbit.
The third uses an algebraic inverse inside a model, not a backward physical
transition. PR666 proves stronger all-block Smith-form statements for its
declared filters; those results are referenced, not independently certified here.

Reducing modulo M^2+M-I gives the FST-01 identities from that branch:

\[
H(M)=8I+M,\qquad K(M)=3M,\qquad Q(M)=7I-6M.
\]

Since M and its inverse are integer unimodular, M is a maximum-norm isometry
over every Q_p. The determinants of H(M) and Q(M) are 55, so both are isometries
at 2 and 3. K(M) is a binary isometry and satisfies exactly

\[
\|K(M)v\|_3=\tfrac13\|v\|_3.
\]

The ternary contraction belongs to the specified complementary operator.
It cannot be assigned to Q(M), to the entire Fibonacci system, or to the
actual BBP real orbit. The determinant also retains prime 11; the arithmetic
inventory is not exhausted by the labels 2,3,5.

## 2. New synthesis: the signed source and the same five-dimensional Jordan block

Work over F_5 and use exactly the matrices in the present Fibonacci note.
Since M=A-I,

\[
H(M)=A+7I\equiv A-3I=:N,
\qquad Q(M)=13I-6A\equiv-N.
\]

Here N=[[3,1],[1,2]], N^2=0 and N is nonzero of rank one. Also A^2=-I+N
over F_5. The fourth symmetric power removes the scalar minus sign, giving

\[
\boxed{
T\bmod5=\operatorname{Sym}^4(I-H(M))
       =\operatorname{Sym}^4(I+Q(M)).}
\]

This identifies an actual operator obtained from the **literal signed BBP
polynomial**, evaluated on the declared Fibonacci module, whose quartic
action is the same fifth-prime dynamics. It strengthens the scalar norm/trace
match to a modulo-5 operator identity. The previous finite-difference proof
then gives (T-I)^5=0 and (T-I)^4 e0=(4,3,1,2,4), so T has one size-five
unipotent Jordan block.

No BBP chronological state-to-Fibonacci conjugacy follows. Polynomial
evaluation at M remains a chosen representation, and the source-clock map
in THEOREMS.md still factors through recovered time. The operator identity
supplies no signed real-phase estimate. A numerical relabeling of the earlier
state/frame/readout counts would not establish this identity; the displayed
maps and the modulo-5 reduction do.

**The modulus cannot be silently lifted.** In entry (0,0) modulo25, T is16,
whereas Sym4(I-H(M)) is1 and Sym4(I+Q(M)) is21. The displayed source/operator
identity is specifically over F5. The all-depth period theorem for T remains
valid independently; it does not extend this equality.

**Source mutation is decisive.** For Htilde=H+t^4 and
Qtilde=(1-t)Htilde, direct evaluation gives I+Qtilde(M)=N modulo5. Its fourth
symmetric power has rank one and square zero. The authentic T is invertible
of order five, so the same source mutation that broke the scalar55 match also
breaks this operator identity.

The exact polynomial product, all three matrix reductions, and the boxed
literal-source identity are checked by `probe_discriminant.py`. The source
mutation and wrong-clock controls remain in the unchanged 29-test focused suite.

## 3. The moving boundary is a sufficient state, not a request to store all history

The sister causal-memory proof keeps the original zero-seeded source and
defines a trailing window V_(n,L) that drops the incoming state U_(n-L).
Finite recurrence unwinding gives exactly

\[
U_n=16^L U_{n-L}+V_{n,L}.
\]

Its omitted term shrinks at 2 because U_(n-L) is 2-adically integral, while
multiplication by 16^L leaves its ternary norm unchanged. The sister proof
uses the inherited ternary-height theorem to quantify the remaining error.
The identity and local norm statements follow directly from the same affine
precision law proved in this dossier; the sharper all-time height estimates
retain their prior provenance.

Retaining or recomputing the appropriate boundary state repairs the window.
It does not require storage of every event. Computing a past boundary now is
exactly the user's internal-model distinction: a present computation about a
past state, without a reversed carrier transition.

Together, the sister branch identifies what a causal truncation drops; this
branch identifies what the finite local clock factor forgets, and gives exact
mixed-place histories on which those reports cannot choose the real carry word.
The remaining pi target must constrain actual source-selected real phases with
the retained boundary. Both branches leave the all-shell signed inequality open.

## Pinned source proofs

- [Fibonacci source transport, FST-01 and FST-02](https://github.com/femboy2112/SUCC/blob/7d2648374a9123e433c6d62c0a88933194a361c7/research/2026-11-18/two_three_causal_transport/FIBONACCI_SOURCE_TRANSPORT.md)
- [BBP causal memory, sections 1–3](https://github.com/femboy2112/SUCC/blob/7d2648374a9123e433c6d62c0a88933194a361c7/research/2026-11-18/two_three_causal_transport/BBP_CAUSAL_MEMORY.md)

The factorial sparse-digit countermodel in this dossier also occurs in the
sister note and in earlier SUCC firewall work. It is a calibrated classical
boundary control, not a claimed new number-theoretic discovery.
