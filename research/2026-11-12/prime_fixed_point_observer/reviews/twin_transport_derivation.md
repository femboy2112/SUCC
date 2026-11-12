# Two-sided transport and retained arithmetic branches

**Date:** 2026-11-12. **Scope:** finite typed linear paths; bounded
operators on the existing arithmetic Hilbert carrier; explicit finite
exact controls. **Status:** elementary proved-local formulas with classical
duality and block-dilation provenance. No academic priority claim.

This audit accompanies [the main construction](../TWIN_OBSERVERS.md) and
the [registered contract](../TWIN_OBSERVER_CONTRACT.md). Its implementation
is [twin_transport.py](../twin_transport.py), with
[13 named tests](../test_twin_transport.py) and the separate literal
oracles in [twin_transport_probe.py](../twin_transport_probe.py).

## 1. The meeting compares present outputs

The hard protocol constraint is that observers compare only their declared
current model outputs at the common meeting event. Earlier observations
were made in different patches and may have different frames. They are
not silently identified or made available to the other observer.

The finite path below is an analyst's model of transport to a selected
meeting fiber. Its forward state and backward dual are already expressed
in that fiber after the declared transport. Proving the same formula for
every possible cut does not give either observer access to outputs at
other cuts or to the other observer's history. `CutProfile` stores all-cut
arrays only for theorem calibration. A runtime meeting uses the selected
current outputs and its prescribed readout.

Likewise, the environment flags in Sections 4–5 are internal state of a
lossless construction. No result here compares those flags across the two
observers. A frame differential must be supplied before any comparison
of historical observations could be meaningful. The main note supplies
the separate present-output frame law.

## 2. Cut pairing needs adjoints, not inverses

Let `N>=0`, let `H_0,...,H_N` be Hilbert spaces, and for `1<=j<=N` let
`A_j:H_(j-1)->H_j` be bounded linear maps. The inner product is conjugate
linear in the first argument and linear in the second. Given boundary
states `a in H_0` and `b in H_N`, define

\[
x_0=a,\qquad x_k=A_k\cdots A_1a,
\qquad y_N=b,\qquad y_k=A_{k+1}^*\cdots A_N^*b.
\]

An empty product is the identity. The states at cut `k` have the same
declared type `H_k`. The reverse observer propagates a dual test. The
definition never requires an inverse of a rank-deficient map.

**TRN-01 — PROVED LOCAL.** For every finite `N`, every such chain, every
boundary pair and every cut,

\[
c_k=\langle y_k,x_k\rangle
=\langle b,A_N\cdots A_1a\rangle.
\]

**Proof:** At consecutive cuts,
`<y_k,x_k>=<A_(k+1)* y_(k+1),x_k>
=<y_(k+1),A_(k+1)x_k>=<y_(k+1),x_(k+1)>`.
Iterate to cut `N`. The zero-arrow case is simply `<b,a>`.

This invariant is a scalar diagnostic. It does not imply `x_k=y_k`.
With the identity arrow on `C^2`, boundaries `(1,0)` and `(0,1)` have
pairing zero at every cut and squared state gap two. With the projection
`A=diag(1,0)`, boundaries `a=(1,1)`, `b=(1,0)` have matching final states,
but their initial state gap is one: the adjoint has not reconstructed the
lost second coordinate.

### A local mismatch has an exact defect

Let another chain `B_j` have exactly the same source and target types.
Use the forward `A` states and backward `B*` tests. Then

\[
\boxed{c_{k+1}-c_k
=\langle y_{k+1},(A_{k+1}-B_{k+1})x_k\rangle.}
\]

Subtract the two adjoint identities at cut `k`. Summing gives

\[
\sum_{k=0}^{N-1}(c_{k+1}-c_k)
=\langle b,(A_N\cdots A_1-B_N\cdots B_1)a\rangle.
\]

This is an error-accounting identity for an analyst or for an appropriately
declared current diagnostic. It is not permission to compare raw historical
observations. One pair of boundary probes can miss a nonzero map defect.
For `A=I`, `B=diag(1,-1)`, the root probe `a=b=(1,0)` has zero defect,
whereas `a=b=(0,1)` gives pairing values `-1,1` and local defect `2`.

## 3. What reversible transport actually proves

**TRN-02 — PROVED LOCAL.** If all `A_j=U_j` are unitary, then

\[
\|x_k-y_k\|=\|U_N\cdots U_1a-b\|
\quad\text{for all }0\le k\le N.
\]

**Proof:** The unitary suffix `R_k=U_N...U_(k+1)` sends `x_k` to the total
forward endpoint and sends `y_k=R_k* b` to `b`. Apply norm preservation.

Consequently exact agreement of complete current vector outputs at one
cut is equivalent to the compatible boundary preparation
`b=U_N...U_1a`. If that preparation is defined using the same total map,
agreement is a consistency consequence; it is not an independent test of
source correctness. A coarse readout can erase a nonzero state difference.
Only the full-state readout has the stated equivalence.

Surjectivity matters. The isometry `A:C->C^2`, `A z=(z,0)`, with `a=1`
and `b=(1,1)` has `A* b=1=a`: current states agree at the initial cut
although the endpoint mismatch `(0,-1)` is nonzero. Replacing “unitary”
with “isometry” would make the theorem false.

## 4. Every current arithmetic return has an explicit lossless extension

Use the already established centered return

\[
T_{q,r}=D_rD_q^*,\quad D_d\varepsilon_k=\varepsilon_{dk},
\quad q>r\ge1,\quad\gcd(q,r)=1,
\]

on `H=l2(N_0)`. It sends `epsilon_(qk)` to `epsilon_(rk)` and kills
the remaining basis vectors. Its initial and final projections are
`P_q=T*T=D_qD_q*` and `P_r=TT*=D_rD_r*`. Their complements are orthogonal
projections, so their own positive square roots.

**TRN-03 — PROVED LOCAL.** The block operator

\[
U_T=\begin{pmatrix}T&I-P_r\\I-P_q&-T^*\end{pmatrix}
\quad\text{on }H\oplus H
\]

is unitary, and for `iota(x)=(x,0)` its compression obeys
`iota* U_T iota=T`.

**Proof:** In `U_T* U_T`, the upper diagonal is
`T*T+(I-P_q)^2=P_q+I-P_q=I`; the lower diagonal is
`(I-P_r)^2+TT*=I-P_r+P_r=I`.
The upper off-diagonal is `T*(I-P_r)-(I-P_q)T*=0`, since both summands
vanish; the other is its adjoint. Computing `U_T U_T*` similarly gives
the identity, using `T(I-P_q)=0` and `(I-P_r)T=0`.

Equivalently, `U_T` is a signed permutation of the full countable basis:

| Input | Condition | Output |
| --- | --- | --- |
| `(epsilon_k,0)` | `q` divides `k` | `(epsilon_(rk/q),0)` |
| `(epsilon_k,0)` | `q` does not divide `k` | `(0,epsilon_k)` |
| `(0,epsilon_k)` | `r` divides `k` | `(0,-epsilon_(qk/r))` |
| `(0,epsilon_k)` | `r` does not divide `k` | `(epsilon_k,0)` |

The first-block output is exhausted by multiples of `r` from the first
input block and nonmultiples of `r` from the second. The second-block
output is exhausted by nonmultiples of `q` from the first and multiples
of `q` from the second. These routes are disjoint; each basis vector has
one signed preimage. This independently establishes surjectivity and
isometry without introducing a finite truncation boundary.

For every `x in H`,

\[
U_T(x,0)=(Tx,(I-P_q)x),\qquad
\|Tx\|^2+\|(I-P_q)x\|^2=\|x\|^2.
\]

A rejected input survives in the auxiliary channel. In particular, for
`T_(3,2)`, input `epsilon_1` is killed by `T` but retained as
`(0,epsilon_1)` by `U_T`. Input at coordinate zero is the nonzero root
vector; it goes to `(epsilon_0,0)`, not to the zero state.

The block construction is the partial-isometry case of the classical
unitary extension discussed in the main note. This proof does not assert
a physical realization of the auxiliary channel.

## 5. Repeating a compression requires an explicit memory protocol

**TRN-04 — PROVED LOCAL counterexample.** For `T=T_(3,2)`,

\[
T^2\varepsilon_1=0,\qquad
\pi_0 U_T^2(\varepsilon_1,0)=\varepsilon_1.
\]

The first enlarged step sends the input to `(0,epsilon_1)`; because 2
does not divide 1, the second sends that retained branch back to the
principal block. Reusing the same auxiliary block is therefore not the
claimed power dilation.

For each step instead introduce a fresh two-state record and define

\[
V_Tx=Tx\otimes|0\rangle+(I-P_q)x\otimes|1\rangle.
\]

`V_T*V_T=T*T+(I-P_q)^2=I`. Extend it by the identity on all old records.
Every step is an isometry. For a finite sequence of returns `T_1,...,T_N`,
induction gives total norm preservation and

\[
\boxed{\text{all-zero record component}=T_N\cdots T_1x.}
\]

The induction takes the zero branch at the next step and leaves every
other record branch present. The program continues each internal branch
through subsequent maps; it does not discard a branch after its first
rejection. Keeping only the all-zero component is an additional
compression, not the complete lossless output. Normalization after such
selection would be an additional operation and is not performed here.

The enlarged representation has `N` record bits after `N` steps. This
resource is part of the construction, not free memory or an infinite
computation completed at a finite meeting. The meeting comparator is
still restricted to its declared present outputs; these internal records
are not pairwise history-comparison data.

### Compression is not an equivalence of the original category

If an isometric embedding `iota` satisfied `U iota=iota T` with unitary
`U`, then `||Tx||=||U iota x||=||x||` for all `x`. The rejected basis
input disproves this for a proper return. The valid block identity is
`iota* U iota=T`, not invariant-subspace intertwining.

Moreover, a unitary satisfying `U^2=U` must be `I`, by multiplying by
`U^-1`. A nontrivial projection cannot be preserved as a distinct unitary
while retaining its idempotent relation. Independently dilating generators
does not automatically preserve their quotient relations. Fresh-record
paths have exactly the compression behavior proved above; no stronger
functorial equivalence is asserted.

## 6. Executable scope and independent controls

The code uses exact real rational amplitudes, where transpose is the
adjoint. The written Hilbert-space proofs hold over complex scalars, but
the code does not claim arbitrary complex arithmetic. Named channel types
prevent accidental composition of equal-dimensional differently named
spaces. A name check by itself does not implement physical frame transport.

The focused suite has 13 tests covering rectangular/singular cut pairing,
unitary boundary agreement, incompatible boundaries, the failure of an
adjoint to be an inverse, a nonsurjective isometry, a root-invisible sign,
retained rejection, both sides of the block inverse, reused-environment
failure, fresh flags, the earlier common-root countermodel, and malformed
input contracts.

The deterministic standalone probe completed **122,975 exact checks**:

- 96 rational chains checked against literal sums over internal indices;
- the exact local-defect and telescoping identities, including a matrix
  mutation not present in the matching chain;
- unitary paths through length 12, with both compatible and mismatched
  endpoint preparations;
- 99 return pairs, including `(29,11)`, `(43,17)`, `(71,29)`, `(101,43)`,
  on 134 basis labels including `104729`;
- a direct signed-permutation oracle for both block directions;
- comparison with the original positive-label arithmetic word
  `V_r`, then `S^(q-r)`, then `V_q*`, before recentering;
- four fresh-record schedules, with 258 sparse sources apiece.

These counts overlap in mathematical provenance. They are implementation
controls, not independent witnesses to a universal arithmetic conjecture.
The displayed universal proofs perform the infinite-dimensional step.
The initial focused run passed all 13 methods in 0.008 seconds; root
integration reruns and their saved receipts are authoritative for the
published tree. No failed implementation run preceded that result.

## 7. Targeted review of the main note

The main note's Sections 4–5 correctly distinguish cut pairing, complete
current-state agreement, one-step compression, retained records and the
failure of automatic categorical equivalence. Their formulas agree with
the derivations above. Its weighted Section 8 estimate is also valid:
for `D>=1` and `C=A-B`,

\[
\|C P_D\|^2\le\sum_{j<D}\|C\varepsilon_j\|^2
\le\frac{\sum_jw_j\|C\varepsilon_j\|^2}{\min_{j<D}w_j}.
\]

The first inequality is the finite column Hilbert-Schmidt bound. Splitting
an input into `P_D x` and its complement gives the stated tail estimate.
It supplies no uniform inverse estimate when the positive weights tend
to zero. No contradiction was found in those targeted sections; this is
a same-model proof audit, not external peer review.

**Verdict:** the proposed larger carrier has an explicit information-
preserving realization for each current arithmetic return, and finite
two-sided transport has exact present-cut invariants. Agreement remains
conditional on boundary preparation, frame transport, and the separating
power of the chosen current output. Neither rejected information retained
elsewhere nor observer symmetry automatically supplies a global arithmetic
proof or a physical collapse event.
