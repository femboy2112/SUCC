# Terminal winding erasure near the literal zero seed

Independent adversarial derivation for PR #657, 2026-11-16. The authentic source
and its literal zero seed are **not** refuted. The construction below changes
the seed by an explicitly nonzero dyadic rational depending on the shell.

## 1. Exact theorem

Let `b >= 2` be an integer and `r(n)` any fixed rational forcing. Write

\[
U_0(s)=s,\qquad U_n(s)=bU_{n-1}(s)+r(n),\qquad
U_n(s)=U_n(0)+b^n s.
\]

For each integer B >= 1, decompose the authentic terminal value as

\[
U_{2B}(0)=C_B+v_B,\qquad C_B\in\mathbb Z,\quad 0\le v_B<1.
\]

Define the Euclidean remainder and a strictly positive integer

\[
D_B=C_B\bmod b^B\in\{0,\ldots,b^B-1\},\qquad M_B=D_B+b^B,
\]

and change the seed to

\[
\boxed{s_B=-M_B/b^{2B}.}
\tag{E1}
\]

Then

\[
\boxed{b^{-B}\le |s_B|<2b^{-B},\qquad s_B\ne0,\qquad s_B\to0.}
\tag{E2}
\]

The altered terminal value is exactly

\[
U_{2B}(s_B)=b^B\bigl(\lfloor C_B/b^B\rfloor-1\bigr)+v_B.
\tag{E3}
\]

Its last B integer radix digits have been erased; its fractional part is
unchanged. Define the same terminal norm on the changed trajectory,

\[
R_A(s)=\frac1A\sum_{k=1}^A\|U_{2A}(s)/b^k\|_{\mathbb T}^2.
\]

Since `v_B/b^k < 1/b <= 1/2`, all distances at A=B are ordinary distances
to zero. The geometric sum therefore gives the exact formula

\[
\boxed{
R_B(s_B)=\frac{v_B^2(1-b^{-2B})}{(b^2-1)B}
<\frac1{(b^2-1)B}.}
\tag{E4}
\]

For the original radix 16, the upper constant is `1/255`.
No floating phase approximation or digit-normality hypothesis enters E1–E4.

## 2. What is preserved, and what changes

The full forcing `r(n)` is identical at every time. For all n >= 0,

\[
U_n(s_B)-U_n(0)=-M_B b^{n-2B}.
\tag{E5}
\]

For n >= 2B this is an integer. The complete circle orbit therefore rejoins
exactly at time 2B and stays identical afterward. When the common forcing has
a convergent completed tail T_n, the completed phases also satisfy

\[
e(U_n(s_B)+T_n)=e(U_n(0)+T_n),\qquad n\ge2B.
\tag{E6}
\]

At n=2B the full fractional part, reduced rational denominator, and reduced
numerator modulo that denominator are unchanged. For b=16, E5 is dyadic at
every clock. Thus **every odd-primary component of the rational class in Q/Z
is unchanged at every clock**. More explicitly, for an odd prime p and a
rational `a/(p^e d)` with `p` coprime to d, its p-primary component is

\[
\frac{a d^{-1}\bmod p^e}{p^e}\pmod1.
\]

Adding a dyadic rational has zero p-primary component. Every character
depending only on this component is therefore identical. Equivalently the
class in Q_p/Z_p is unchanged for every odd p. This statement does **not** say
that the full p-adic values, arbitrary p-adic residues, the 2-primary channel,
integer winding, or literal seed are unchanged.

If the original U_n has odd reduced denominator q_n, as for BBP, adding E5
preserves its entire odd reduced denominator at every clock: for n<2B, write
E5=m/2^j; the common numerator `a 2^j + m q_n` is coprime to q_n whenever
`a/q_n` is reduced. New powers of 2 may appear. For n>=2B the complete reduced
denominator is the same.

The exact source selector rejects the construction immediately because E2
gives U_0(s_B) != 0. The theorem is a counterexample to **seed-blind uniform
coercivity**, not to the source-selected R0 conjecture.

## 3. Finite observations and the quantifier boundary

For every fixed finite H,

\[
\max_{0\le n\le H}|U_n(s_B)-U_n(0)|<2b^{H-B}\longrightarrow0.
\tag{E7}
\]

Thus the changed histories approach the authentic history on every fixed
finite set of clocks, while their own moving shell has E4's vanishing norm.

On the other hand, for every fixed B and every A>=2B, E5 divided by b^k
is an integer at the terminal clock 2A for all k<=A. Hence

\[
\boxed{R_A(s_B)=R_A(0)\quad(A\ge2B).}
\tag{E8}
\]

Each one of these rationally perturbed histories has exactly the same eventual
terminal norm sequence as the authentic history. It is incorrect to infer that
any one fixed seed s_B is an asymptotic counterexample to R0.

Write `L=liminf_{A->infinity} R_A(0)`, an unknown nonnegative number for pi.
For fixed A the finite norm is continuous in s, so

\[
\lim_{B\to\infty}R_A(s_B)=R_A(0),\qquad
\liminf_{A\to\infty}R_A(s_B)=L\quad\text{for each fixed B},
\]

while E4 gives `lim_{B->infinity} R_B(s_B)=0` along the diagonal. The two
iterated liminf limits over A and B both equal L. **This is a nonuniform
diagonal limit; it is not an unconditional noncommutation of those two
iterated limits.**

A genuine order distinction can instead be expressed using an infimum over
nearby b-adic seeds. For any epsilon>0 put

\[
S_\epsilon=\{s\in\mathbb Z[1/b]:0<|s|<\epsilon\}.
\]

Every fixed s in this set has `R_A(s)=R_A(0)` for all sufficiently large A
(its denominator is killed when A is large enough). But for each sufficiently
large A, the seed s_A belongs to S_epsilon and satisfies E4. Therefore

\[
\boxed{
\inf_{s\in S_\epsilon}\liminf_{A\to\infty}R_A(s)=L,
\qquad
\liminf_{A\to\infty}\inf_{s\in S_\epsilon}R_A(s)=0.}
\tag{E9}
\]

If R0 is true, L>0 and these expressions differ. Without a proof of R0, no
strict inequality between them is claimed. Regardless of L, there is no
positive lower bound uniform over all sufficiently late shells and all
arbitrarily small nonzero b-adic seeds.

## 4. Optional dyadic refinement of the terminal residual

For any integer L>=0, set `Q=b^L`,

\[
a_{B,L}=\lfloor Qv_B\rfloor,\qquad
s_{B,L}=-\frac{M_B+a_{B,L}/Q}{b^{2B}},\qquad
w_{B,L}=v_B-a_{B,L}/Q.
\]

Then `0<=w_{B,L}<b^{-L}`, the same strict seed bounds E2 hold, and

\[
R_B(s_{B,L})=
\frac{w_{B,L}^2(1-b^{-2B})}{(b^2-1)B}
<\frac{b^{-2L}}{(b^2-1)B}.
\tag{E10}
\]

The proof is the same geometric calculation. All odd-primary components at
every clock remain unchanged for b=16. The complete circle orbit rejoins by
time `2B+L`, since the changed seed has denominator dividing `b^{2B+L}`.
The corresponding terminal norms agree with the authentic ones for every
`A>=2B+L`.

For L=0 this is exactly E1–E8 and preserves the terminal fractional part.
For L>0 it generally changes that fractional part and can introduce powers of
2 into the terminal denominator; those stronger L=0 preservation statements
must not be transferred. The completed phase also contains T_(2B), so E10's
arbitrarily fine **raw rational norm** is not by itself the same bound on the
completed shell energy. The unchanged positive tail must still be paid.

For the original BBP source that payment is explicit. Since
`T_(2B)<1/(256B^2)`, the completed shell energy of this changed seed obeys

\[
\mathcal A_B(s_{B,L})
\le\frac{2\pi^2(w_{B,L}+T_{2B})^2(1-16^{-2B})}{255B}
<\frac{2\pi^2(16^{-L}+1/(256B^2))^2}{255B}.
\tag{E11}
\]

The first inequality uses `1-cos(2 pi t)<=2 pi^2 t^2` and the same geometric
sum, so no circle-branch assumption is needed. Taking L=B produces an
`O(B^{-5})` completed-energy family while retaining `s_(B,B)->0` and all
odd-primary source components. The selected literal zero still rejects it.

E10 implies that, for any fixed epsilon>0 and every sufficiently large B,
`inf_{s in S_epsilon} R_B(s)=0` already on that finite shell: let L tend to
infinity. The infimum need not be attained. This strengthens E9's right-hand
identity without determining the authentic value L.

## 5. Novelty and prior work

The archive already proves finite-window coherence with dyadic changed seeds
and unchanged odd-primary components: `research/2026-10-30/arithmetic_barrier/
signed_crt/JOINT_SIGNED_CRT.md`, SC-05, credits the earlier October 24 result.
The old construction uses seeds close to -pi/16; the present specialized
construction uses s_B->0, erases only a terminal winding block, preserves the
terminal fractional value exactly, and supplies the explicit new-metric E4.
It is a sharpened specialization of an inherited obstruction. No worldwide
mathematical novelty is claimed. It does not give an unconditional saving for
the original zero seed.

The nearest-integer current comparison, the bulk constants 225 and 289,
current-density equivalence to R0, negative Green profile, finite terminal-root
counterseeds and logarithmic-rate trap are already established in
`research/2026-11-12/leah_gamma_twist/INVERSE_R0.md` and `HOSTILE.md`.

## 6. Audit of the inherited VFM bridge

The ten `test_virtual_form_metric.py` tests were rerun independently and pass.
The paper calculations of the `1/255` squared geometric factor, the source
tail envelope, the `8` and `2 pi^2` torus-energy comparison, and the error
`rho_B=8r(2B+1)/(225B)` all survive line-by-line audit. They establish the
claimed R0 equivalence but not its lower bound.

At the starting head, the manuscript's introductory claim numbering was
inconsistent with its body (the endpoint continuation corrects it):
the bridge is VFM-05, finite observations VFM-07, the topology obstruction
VFM-08, and conditional normality comparison VFM-09. There is no body VFM-10.
This is an indexing correction; the audited theorem statements are unaffected.

Independent symbolic source calibration gives

\[
\frac1{(8n+1)(8n+2)}-\frac{r(n+1)}{15}
=\frac{352n^2+432n+131}
 {30(2n+1)(4n+1)(4n+3)(8n+1)(8n+5)}>0.
\]

The numerator of `r(n)-r(n+1)` after substitution `n=k+1`, with the positive
denominator retained, is
`122880 k^5 + 662016 k^4 + 1360896 k^3 + 1330440 k^2 + 620136 k + 110709`.
This proves strict decrease for n>=1, and with positivity gives the strict
geometric tail bound `0<T_n<r(n+1)/15`.
