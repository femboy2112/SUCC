# Arithmetic coherence: branch sectors and protected logical encodings

**Date:** 2026-11-12. **Continuation parent:** published commit
`e9639c0ddb07385c6000b670d26cf0f7b91dacaa`, content tree
`d591ba032b6b0cef8f62a32100455f9c3857b681`.
**Status:** elementary PROVED LOCAL statements, with exact finite controls.
No physical collapse mechanism, quantum advantage, new prime-pair estimate,
or universal number-theoretic conclusion is claimed.

## 0. What is new and what the meeting may access

[TWIN_OBSERVERS.md](TWIN_OBSERVERS.md) already constructs a reversible
extension of each arithmetic return and a fresh-record isometry for a
finite route. This note determines which source distinctions remain in
the **present arithmetic output after the records are inaccessible**.
It also constructs explicit logical encodings that protect a coherent
state while the carrier really does record an internal branch.

The branch strings below are mathematical labels in an internal register.
They are not histories supplied to the meeting comparator. The comparator
still receives only declared current outputs in one calibrated frame.
A source-to-meeting transport and any change of units or basis must be
justified as in TWIN-01. A decoder is part of the present output protocol;
it does not authorize comparing untransported past observations.

The sharp positive result is that a common **environment state** can carry
branch structure without revealing the protected logical coordinate.
Protecting that coordinate can require a deliberate encoding. It does
not preserve every unencoded natural-number distinction automatically.

## 1. A fresh-record route is a deterministic injection into a larger carrier

Let `H = l2(N_0)` with orthonormal basis `epsilon_k`. For a proper reduced
pair `q > r >= 1`, `gcd(q,r)=1`, use the existing return

\[
T_{q,r}\varepsilon_k=
\begin{cases}\varepsilon_{rk/q},&q\mid k,\\0,&q\nmid k.\end{cases}
\]

Fix a finite prescribed schedule `(q_j,r_j)`, `1 <= j <= N`. A successful
step replaces the current label `x` by `r_j x/q_j` and records zero. A
rejected step leaves `x` intact in the larger carrier and records one.
This is exactly the existing `fresh_flags` protocol, not repeated
postselection on successful returns. Write its final label and record as
`f_N(k)` and `h_N(k) in {0,1}^N`.

**AC-01 — PROVED LOCAL.** The isometry has the basis action

\[
\boxed{W_N\varepsilon_k=
\varepsilon_{f_N(k)}\otimes|h_N(k)\rangle.}
\]

The map `k -> (f_N(k),h_N(k))` is injective. For a fixed record `h`,

\[
f_N(k)=\alpha_h k,
\qquad
\alpha_h=\prod_{j:h_j=0}\frac{r_j}{q_j}>0.
\]

**Proof.** Compose the two alternatives at each step. Given a successful
step's output and its zero flag, recover the preceding label by multiplying
by `q_j/r_j`; given a one flag, retain the label. Reversing all steps
recovers `k`. The multiplier formula follows by multiplying the accepted
ratios. Distinct input basis vectors therefore have orthogonal joint
outputs. Linear extension gives an isometry on the entire Hilbert space.

Let `D_h = {k : h_N(k)=h}`, let `P_h` be its coordinate projection, and
let `K_h epsilon_k = 1_(k in D_h) epsilon_(f_N(k))`. Then

\[
K_h^*K_h=P_h,\qquad \sum_hP_h=I,
\qquad W_N=\sum_hK_h\otimes|h\rangle.
\]

The output ranges of different `K_h` need not be orthogonal. This matters
both for information loss and for the protected encodings below.

## 2. Exact divisibility descriptions of every branch sector

For a proposed record `h`, start with `alpha=1`. Before step `j`, write
the current multiplier as `alpha=a/b` in lowest positive terms and put

\[
s_j=\frac{bq_j}{\gcd(a,q_j)}.
\]

If `h_j=0`, require `s_j | k` and update `alpha <- alpha r_j/q_j`.
If `h_j=1`, require `s_j` not to divide `k` and leave `alpha` unchanged.

**AC-02 — PROVED LOCAL.** These finite divisibility and nondivisibility
conditions describe `D_h` exactly. With

\[
A_h=\operatorname{lcm}\{s_j:h_j=0\},\qquad
\operatorname{lcm}(\varnothing)=1,
\]

one has

\[
D_h=\{k\ge0:A_h\mid k,\ s_j\nmid k\text{ for every }j\text{ with }h_j=1\}.
\]

The sector is empty precisely when one of its rejected-step moduli divides
`A_h`. Otherwise its least positive member is `A_h`. Zero belongs only
to the all-success sector. A certified period of its membership predicate
is `lcm(s_1,...,s_N)`; this need not be the least period.

**Proof.** Inductively, the preceding requirements guarantee that `ak/b`
is an integer. The next acceptance condition is

\[
q_j\mid ak/b
\iff bq_j\mid ak
\iff \frac{bq_j}{\gcd(a,q_j)}\mid k,
\]

because `gcd(a,b)=1`. This proves the sector description by induction.
If a rejected modulus divides `A_h`, every multiple of `A_h` violates
that rejection. If none does, `k=A_h` satisfies all requirements.
All requirements are periodic with the displayed common period.

Thus the internal branch labels have explicit arithmetic content. Calling
them arbitrary environmental noise would lose the actual source relation.
Enumerating all records can still cost up to `2^N` candidate descriptions;
the formula makes no claim that this enumeration is inexpensive.

## 3. What the current output loses when its records are inaccessible

Define the arithmetic-output channel and its record-output complement by

\[
\mathcal E_N(\rho)=\operatorname{Tr}_{\rm record}W_N\rho W_N^*,
\qquad
\mathcal E_N^c(\rho)=\operatorname{Tr}_{H}W_N\rho W_N^*.
\]

**AC-03 — PROVED LOCAL.** On matrix units,

\[
\boxed{\mathcal E_N(|k\rangle\langle\ell|)
=\mathbf1_{h_N(k)=h_N(\ell)}
|f_N(k)\rangle\langle f_N(\ell)|,}
\]

\[
\boxed{\mathcal E_N^c(|k\rangle\langle\ell|)
=\mathbf1_{f_N(k)=f_N(\ell)}
|h_N(k)\rangle\langle h_N(\ell)|.}
\]

**Proof.** Form the rank-one outer product of the two joint outputs in
AC-01 and trace the chosen register. The trace of a basis matrix unit is
one exactly when its two labels agree. Equivalently,
`E_N(rho)=sum_h K_h rho K_h*`. Finite matrix units determine finite-rank
operators; continuity in trace norm extends the identities to trace-class
inputs. These are ordinary reduced-state channels, not a collapse law.

Consequently, the current arithmetic output retains cross terms within
one branch sector and removes cross terms between different records.
It may also identify different original basis inputs, because two sectors
may have the same output label.

**AC-04 — PROVED LOCAL, coordinate-code criterion.** For a set of labels
`A`, the restriction of `E_N` to the coordinate space
`C_A = closure span{epsilon_k:k in A}` is an isometric channel precisely
when all labels in `A` have one common record. The nonzero spaces
`P_h H` are therefore the maximal coherent coordinate sectors.

**Proof.** If all records equal `h`, `K_h` is an isometry on `C_A` and
all other Kraus maps vanish there. Conversely, for `k,l in A` with
different records, the matrix unit `|k><l|` maps to zero. Isometric
conjugation would map it to a nonzero matrix unit between orthogonal
images. Thus no isometric channel on `C_A` exists.

### Two controls prevent confusing purity with preservation

For the single return `(q,r)=(3,2)`:

* `epsilon_3` and `epsilon_6` both record zero and become `epsilon_2`
  and `epsilon_4`. Their superposition retains its relative phase.
* `epsilon_1` and `epsilon_3` record one and zero, becoming different
  output labels `epsilon_1` and `epsilon_2`. Their cross term vanishes
  after the record is traced out.
* `epsilon_2` and `epsilon_3` record one and zero but **both become
  `epsilon_2`**. Every normalized superposition of these two inputs
  yields the same pure arithmetic output. The original two-dimensional
  information has moved into the record register.

The last example gives an exact warning: a pure current output can have
lost the entire logical qubit. A reference entangled with that qubit
becomes correlated with the record, while the arithmetic output is fixed.
Joint access to the enlarged carrier permits applying `W_N*` on its image;
discarded-record access does not. The enlarged state's purity does not
imply preservation of the chosen output's twin correlation.

## 4. A complete constructive family of uncorrected coherent codes

The coordinate-sector criterion is not a classification of arbitrary
logical encodings. Different record sectors may be combined coherently
so that the record state is independent of the protected logical value.

Write `Q_h = K_h K_h*` for the projection onto the output range of `K_h`.
Choose coefficients `c_h` with `sum_h |c_h|^2=1` and a closed output
subspace

\[
L\subseteq\bigcap_{h:c_h\ne0}\operatorname{Ran}Q_h.
\]

Define the input encoding

\[
\boxed{J_c\phi=\sum_h c_hK_h^*\phi\quad(\phi\in L),
\qquad |\eta_c\rangle=\sum_hc_h|h\rangle.}
\]

**AC-05 — PROVED LOCAL, common-range encoding and converse.** The map
`J_c:L->H` is isometric and

\[
\boxed{W_NJ_c\phi=\phi\otimes|\eta_c\rangle,
\qquad \mathcal E_N(J_c\rho J_c^*)=\rho.}
\]

Conversely, every nonzero closed code `C` on which `E_N` is an isometric
channel has this form, with `L` its isometric output and a single fixed
normalized coefficient vector `c`. This characterizes preservation
**without an additional recovery channel**. More general correctable
codes can have a mixed, input-independent environmental state and require
a recovery; they are not classified by this narrower theorem.

**Constructive proof.** The images of `K_h*` lie in mutually orthogonal
`P_h H`. On `L`, every `Q_h` with `c_h != 0` acts as identity. Hence

\[
\|J_c\phi\|^2=\sum_h|c_h|^2\|\phi\|^2=\|\phi\|^2.
\]

Also `K_g K_h*=0` for `g != h`, because their initial sectors differ.
Therefore `K_g J_c phi=c_g Q_g phi=c_g phi`, proving factorization.
The channel identity follows by tracing a fixed unit vector's projector.

**Converse proof.** Suppose `E_N(rho)=V rho V*` on `C`, for an isometry
`V:C->H`. For a unit vector `u in C`, the pure joint state `W_N u` has
pure arithmetic marginal `|Vu><Vu|`; expanding in an orthonormal basis
containing `Vu` forces `W_N u=Vu tensor eta_u`. If `u,v` are orthogonal,
apply the same fact to `(u+v)/sqrt(2)`. Linearity and the orthogonality
of `Vu,Vv` force `eta_u=eta_v`. The one-dimensional case has just one
environment vector; in higher dimension the argument extends through a
basis and then by continuity. Thus one `eta=sum_h c_h|h>` works on all
of `C`, giving `K_h u=c_h Vu`. Whenever `c_h !=0`, `Vu` belongs to
`Ran Q_h`. Finally,

\[
u=\sum_hK_h^*K_hu=\sum_hc_hK_h^*Vu=J_cVu.
\]

Taking `L=V(C)` proves `C=J_c(L)` and the claimed classification.

### An explicit protected arithmetic qubit with two different records

For any proper coprime `q>r`, and every positive `j` not divisible by `q`,
the output `epsilon_(rj)` has an accepted preimage `epsilon_(qj)` and a
rejected preimage `epsilon_(rj)`. For fixed complex `a,b` with
`|a|^2+|b|^2=1`, define

\[
|c_j\rangle=a\varepsilon_{qj}+b\varepsilon_{rj}.
\]

These vectors, indexed by `q`-nondivisible `j`, are orthonormal: the
accepted supports are divisible by `q`, the rejected supports are not,
and each individual multiplier is injective. Their transport is

\[
\boxed{W_1|c_j\rangle=
\varepsilon_{rj}\otimes(a|0\rangle+b|1\rangle).}
\]

In particular, choose `(q,r)=(3,2)`, `a=3/5`, and `b=4/5`:

\[
c_1=(3\varepsilon_3+4\varepsilon_2)/5,
\qquad c_2=(3\varepsilon_6+4\varepsilon_4)/5.
\]

For arbitrary `alpha,beta`,

\[
W_1(\alpha c_1+\beta c_2)
=(\alpha\varepsilon_2+\beta\varepsilon_4)
\otimes(3|0\rangle+4|1\rangle)/5.
\]

Both arithmetic alternatives occur in the encoding, and the carrier
records their amplitudes. The record does not reveal whether the protected
logical coordinate was 1 or 2. Its probabilities `9/25` and `16/25`
remain the same for every logical input. The full record density matrix,
including its off-diagonal entries, is also fixed. Equal record
probabilities alone would be insufficient.

Tensoring the displayed factorization with any reference shows directly
that all input entanglement with that reference is preserved in the
arithmetic output. The present decoder sends `epsilon_2,epsilon_4`
to the two declared logical basis vectors. The encoding and decoder are
explicit parts of the protocol; they do not arise by measuring the
observers' old histories or by identifying unencoded integers 2 and 3.

## 5. Every finite all-success route has an exact coherent encoding

For each prefix, reduce the total accepted ratio:

\[
\alpha_j=\prod_{i=1}^j\frac{r_i}{q_i}=a_j/b_j,
\qquad \gcd(a_j,b_j)=1.
\]

Put

\[
L_N=\operatorname{lcm}(b_1,\ldots,b_N),\qquad
M_N=\alpha_NL_N\in\mathbb N,
\]

with `L_0=M_0=1`. As before, `D_d epsilon_k=epsilon_(dk)`.

**AC-06 — PROVED LOCAL, path-domain formula.** The original compressed
product and its retained-record extension satisfy

\[
\boxed{T_{q_N,r_N}\cdots T_{q_1,r_1}
=D_{M_N}D_{L_N}^*,}
\]

\[
\boxed{W_ND_{L_N}\psi
=D_{M_N}\psi\otimes|0^N\rangle.}
\]

**Proof.** Input `k` survives every compressed step precisely when every
`alpha_j k` is an integer. Indeed, given survival through step `j-1`,
integrality of `r_j alpha_(j-1)k/q_j` is equivalent to `q_j` dividing
the current integer because `q_j,r_j` are coprime. Thus each `b_j`
must divide `k`, or equivalently `L_N | k`. For `k=L_N t` the final
label is `M_N t`; otherwise the compressed product is zero. This is
exactly the first formula. The second follows because all encoded labels
have record `0^N`. Extend from basis vectors by continuity.

This supplies a positive finite-horizon construction. Encode a logical
state by `D_(L_N)`, traverse the specified route, and use `D_(M_N)*`
on the known output range as the present decoder. Any finite logical
dimension is preserved, with an environment fixed at `0^N`. Physical
implementation and its cost remain separate questions. The encoded
labels are rescaled; for a logical prefix of dimension `d`, its largest
source label is `L_N(d-1)`. The source preparation is a real resource.

### The reduced final ratio is not enough

For the route `(2,1)` followed by `(3,2)`, the total ratio is `1/3`, but

\[
L_2=\operatorname{lcm}(2,3)=6,\quad M_2=2,
\quad T_{3,2}T_{2,1}=D_2D_6^*.
\]

Input 3 would produce the integer 1 under the reduced total ratio, yet
the actual first return rejects it. Conversely, for `(3,2)` followed
by `(2,1)`, `L_2=3`, so multiplying the two denominators would wrongly
require divisibility by 6. Intermediate domains are load-bearing path
information, even when the final rational multiplier agrees.

## 6. Fixed-code and infinite-route boundaries

**AC-07 — PROVED LOCAL.** For any prescribed infinite sequence of proper
returns, the finite-prefix success lattices satisfy

\[
L_N\mid L_{N+1},\qquad L_N-M_N\ge N,\qquad L_N\ge N+1,
\]

and

\[
\bigcap_{N\ge0}D_{L_N}H=\mathbb C\varepsilon_0.
\]

**Proof.** The lcm definition gives divisibility. Starting at the least
positive all-success label `L_N`, each successful proper return strictly
decreases a positive integer, by at least one. Its final positive label
is `M_N`, so `L_N-M_N>=N` and `M_N>=1`. No fixed positive integer can
be divisible by all the unbounded `L_N`. Coordinate supports prove the
intersection claim.

There is a corresponding strong-limit theorem for the **compressed**
products `A_N=T_(q_N,r_N)...T_(q_1,r_1)`:

\[
\|(A_N-E_0)x\|^2
=\sum_{t\ge1}|x_{L_Nt}|^2\longrightarrow0,
\qquad \|A_N-E_0\|=1\quad(N<\infty).
\]

The sum is bounded by the square-summable tail from `L_N` onward. The
norm-one witness is `epsilon_(L_N)`. If the input is supported in
`0,...,M`, then `N>=M` gives exact root projection. A nontrivial **fixed**
code cannot remain entirely in the all-success sectors forever; the
finite-horizon encoding in AC-06 changes with the horizon.

This does not imply that every coherent code dies under indefinitely
many retained-record steps. For repeated `(3,2)`, all labels not divisible
by 3 are rejected at every step and remain unchanged. Their common-record
sector preserves arbitrary superpositions. More generally, an initial
positive label `k=3^s u`, `3` not dividing `u`, has `s` initial successes
and then only rejections, with terminal output `2^s u`. Labels with the
same `s` share the entire record. The all-success result concerns the
specific compressed arithmetic route, not every internal record sector.

### Postselection retains a probability and a Schmidt-rank cost

For a normalized input `psi`, the probability of an all-zero record at
horizon `N` is

\[
p_N=\|A_N\psi\|^2
=\sum_{t\ge0}|\psi_{L_Nt}|^2.
\]

It cannot be silently set to one by renormalizing the surviving component.
For a uniform twin on input labels `0,...,d-1`, the all-success probability
and the surviving conditional Schmidt rank are

\[
p_N=\frac{m_N}{d},\qquad
m_N=1+\left\lfloor\frac{d-1}{L_N}\right\rfloor.
\]

This follows by counting the accepted orthogonal Schmidt columns. Once
`L_N>d-1`, only the root remains: the conditional outcome is pure and
has Schmidt rank one, with success probability `1/d`. Thus a clean
meeting produced by selecting the common root is not preservation of
the original twin information. If the prepared prefix excludes zero,
the all-success probability eventually becomes zero instead.

## 7. Verdict, provenance, and next discriminator

**SURVIVES, PROVED LOCAL:** coherent transport can coexist with genuine
carrier interaction. The fixed record must carry no information about
the protected logical state, or a separately specified recovery must
restore that state. AC-05 and AC-06 give explicit arithmetic constructions
with no additional recovery beyond their present range decoder.

**REFUTED by receipts:** current-output purity implies retained source
information; a reduced endpoint multiplier determines a composable route;
every coherent arithmetic code must occupy one literal record sector;
or arbitrarily long successful proper returns preserve one fixed
nontrivial all-success code. The counterexamples and proofs above give
the exact scope of each failure.

These are self-contained arithmetic and linear-algebra derivations.
Their starting implementation is the unchanged `twin_transport.py` and
the preceding TWIN-04 theorem at the continuation parent. Standard
partial-trace and isometric-channel conventions were checked against
John Watrous, [The Theory of Quantum Information, Chapter 2](https://jhwatrous.github.io/TQI.2.pdf),
Section 2.1.3, equations (2.30)-(2.34), Corollary 2.27, and the
isometric-channel examples in Section 2.2.3. That source establishes the
channel formalism; the arithmetic sector and encoding formulas are
derived here. No priority claim is made.

The exact probe compares independent divisibility calculations with the
existing fresh-record implementation, retains the endpoint-ratio and
pure-output countermodels, and checks the protected codes with rational
amplitudes. Its finite counts certify those implementations and examples;
the universal statements depend on the displayed proofs.

**Next lamp:** choose a source-faithful logical observable and a family of
these encodings whose transport/decoding costs are explicit, then prove
that its current output controls the desired arithmetic remainder.
Preserving an arbitrary logical coordinate is not that estimate.
Neither the code construction nor an observer meeting proves Goldbach,
normality of pi, RH, or an objective collapse-at-meeting principle.
