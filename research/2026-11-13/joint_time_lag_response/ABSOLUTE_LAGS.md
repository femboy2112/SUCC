# Absolute lag averages: a tensor lift closes the schedule question

**Status: PROVED LOCAL.** Complete elementary proofs below; same-model research
and audit, not independent external refereeing. No statistical estimate for the
original zero-seeded BBP source is proved. No claim of mathematical priority.

## The precise archival question

The baseline is Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`, with the
previous round at `7f11088bf5e3d216ca0f6ae57da1544e17c46d1c`.
The frozen dossier
`research/2026-11-11/innovation_arithmetic_decoupling/THEOREMS.md`, IAD-02,
already proves schedule-freeness of the **signed** Fejer response. Its
Consequences 2, lines 140--143 at this baseline, leaves undecided whether the
absolute-value aggregate is strictly stronger. The present theorem resolves
that distinction: for the actual autocorrelation family, the absolute aggregate
also vanishes on **every** diverging window schedule under normality. No uniform
bound on the largest individual growing-lag coefficient is needed.

The instrument is the tensor-square lift of the same shift orbit. This preserves
the positive-definite constraint between different lag coefficients. Treating
them as an arbitrary triangular array would lose precisely that constraint.
The tensor/Schur method itself is classical. A primary exposition of its use
to couple families of correlations is Terence Tao,
[Boosting the van der Corput inequality using the tensor power trick](https://terrytao.wordpress.com/2021/02/27/boosting-the-van-der-corput-inequality-using-the-tensor-power-trick/)
(27 February 2021). The claim here is the explicit finite estimate and its
resolution of this archive's stated schedule question, not invention of that
general method.

## AL-01. Finite tensor window inequality

Let `v` be a nonzero complex sequence of finite support on the integers, and set

\[
 S=\sum_n|v_n|^2,\qquad
 c(\ell)=S^{-1}\sum_n v_{n+\ell}\overline{v_n},\qquad c(0)=1.
\]

For positive integers `H,J`, with `J <= H`, define

\[
 A_H=\frac2H\sum_{\ell=1}^{H-1}
       \left(1-\frac\ell H\right)|c(\ell)|,
 \qquad
 G_J=\frac1J+\frac2J\sum_{\ell=1}^{J-1}
       \left(1-\frac\ell J\right)|c(\ell)|^2.
\]

Write `H=kJ+r`, where `0 <= r < J`. Then

\[
\boxed{\sqrt{G_H}\le\frac{kJ}{H}\sqrt{G_J}+\frac rH
       \le\sqrt{G_J}+\frac JH.}\tag{AL1}
\]

Moreover,

\[
\boxed{A_H^2\le\left(1-\frac1H\right)
                \left(G_H-\frac1H\right).}\tag{AL2}
\]

In particular,

\[
\boxed{A_H\le\sqrt{1-1/H}
       \left(\sqrt{G_J}+J/H\right).}\tag{AL3}
\]

If `|c(ell)| <= epsilon` for `1 <= ell < J`, this implies the fully finite bound

\[
 A_H\le J^{-1/2}+\epsilon+J/H.\tag{AL4}
\]

**Proof.** Work in `ell^2(Z)` with the unitary shift `U`. Let `w=v/sqrt(S)`.
In the Hilbert tensor product with the conjugate Hilbert space, put
`q=w tensor conjugate(w)` and `V=U tensor conjugate(U)`. Then `||q||=1`, and

\[
 \langle V^\ell q,q\rangle=|c(\ell)|^2.
\]

Thus direct expansion gives

\[
 G_H=\left\|\frac1H\sum_{j=0}^{H-1}V^jq\right\|^2.
\]

Split the sum into `k` blocks of length `J` and one remainder of length `r`.
Every complete block has norm `J sqrt(G_J)`, since it is a unitary translate
of the first one; the remainder has norm at most `r`. The triangle inequality
proves AL1. This argument is finite, with no spectral limit or interchange.

For AL2 use weighted Cauchy--Schwarz with
`w_ell=(2/H)(1-ell/H)`, `1 <= ell < H`. Their sum is `1-1/H`, and
`sum w_ell |c(ell)|^2=G_H-1/H`. AL3 follows by dropping the nonnegative
subtracted term and applying AL1. Finally
`G_J <= 1/J+(1-1/J)epsilon^2 <= 1/J+epsilon^2`, proving AL4. QED.

**Scope.** The tensor lift is a proof device, not an extra observation port. It
uses squared magnitudes of the same already available lag coefficients.
The conclusion is about their weighted average, not their maximum.

## AL-02. Every absolute schedule follows from fixed-lag cancellation

Let `v^(N)` be any sequence of nonzero finite vectors, and let `c_N` be their
normalized autocorrelations as above. Suppose

\[
 \forall\ell\ge1:\quad c_N(\ell)\longrightarrow0.
\]

Then for **every** integer schedule `H(N) -> infinity`,

\[
 \frac2{H(N)}\sum_{\ell=1}^{H(N)-1}
 \left(1-\frac\ell{H(N)}\right)|c_N(\ell)|\longrightarrow0.\tag{AL5}
\]

**Proof.** Fix `J`. The hypothesis gives `G_(N,J) -> 1/J`. AL3 therefore
gives `limsup_N A_(N,H(N)) <= 1/sqrt(J)`. Let `J` tend to infinity after this
limsup. This order of limits proves AL5 without exchanging them. QED.

This is a consequence of the common positive-definite realization of all
lags. It is false for an arbitrary bounded triangular array. For example,
put `c_N(0)=1`, `c_N(ell)=0` for `1 <= ell < floor(sqrt(N))`, and
`c_N(ell)=1` for `floor(sqrt(N)) <= ell < N`. Every fixed nonzero lag tends
to zero, but `A_(N,N) -> 1`. These arrays are not autocorrelations of finite
vectors: AL1 would be violated. This is a useful mutation control.

## AL-03. Application to the authentic time--lag field

For any real `x`, retain the completed orbit `Y_n=16^n x`, and for a fixed
nonzero integer `h` let

\[
 z_n=e(hY_n),\qquad
 c_{N,h}(\ell)=\frac1N\sum_{n=0}^{N-\ell-1}
                    z_{n+\ell}\overline{z_n}\quad(0\le\ell<N),
\]

with `c=0` at larger positive lags. This is precisely the autocorrelation of
the zero-padded finite vector `z_0,...,z_(N-1)`, divided by its squared norm `N`.
Define `A_(N,H,h)` by AL-01. For **every prescribed** integer schedule
`1 <= H(N) <= N`, `H(N) -> infinity`, the following are equivalent:

1. `x` is normal in base 16.
2. For every nonzero integer `h`, `A_(N,H(N),h) -> 0`.

If (1) holds, (2) holds simultaneously for every such schedule.

**Proof of necessity.** For each fixed `h != 0` and `ell >= 1`, the frequency
`h(16^ell-1)` is a fixed nonzero integer. Normality and the classical Weyl
criterion give `c_(N,h)(ell) -> 0`; omitting the last `ell` terms costs at
most `ell/N`. Apply AL-02.

**Proof of sufficiency.** Expanding zero-padded length-`H` windows and applying
Cauchy--Schwarz gives the standard exact finite inequality

\[
 \left|\frac1N\sum_{n<N}z_n\right|^2
 \le\left(1+\frac{H-1}{N}\right)
 \left[\frac1H+\frac2H\sum_{\ell=1}^{H-1}
       \left(1-\frac\ell H\right)\Re c_{N,h}(\ell)\right]
 \le 2\left(H^{-1}+A_{N,H,h}\right).
\]

Indeed `H sum z_n` is the sum of `N+H-1` padded windows, and the sum of their
squared moduli is `NH^2` times the bracket. Under (2), every nonzero Weyl
mean vanishes. Weyl's criterion and the radix-orbit characterization of
normality finish the proof. QED.

**Source status.** Substituting `x=pi/16`, `Y_n=U_n+T_n`, preserves exactly
the original zero-seeded BBP source. The hypothesis (2) has not been proved
for that source. AL-03 is an analytic equivalence, not a proof of normality
or R0. Its new local contribution is closing the absolute-versus-signed
schedule question, not making the arithmetic premise easier by assertion.

**Why the admissibility restriction matters.** If `H=N^2`, even the coherent
sequence `z_n=1` has `A_(N,H) <= N/H -> 0`. Thus an arbitrarily oversized
window cannot certify cancellation; the prefactor in the finite inequality
must be retained. The stated converse uses `H <= N` for exactly this reason.

## AL-04. The archived Basel-weighted formulation also closes

Use exactly the positive weights of IAD-01:
`p_n=n^(-2)/omega_B` on `[B,2B)`, `v_n=p_n e(hY_n)`,
`S=sum |v_n|^2`, `sigma_B=B S`, so `1 <= sigma_B <= 2`.
The absolute analogue of the archived signed response is

\[
 R^{\rm abs}_{B,L,h}=\frac{2B}{L}\sum_{\ell=1}^{L-1}
 \left(1-\frac\ell L\right)
 \left|\sum_n v_{n+\ell}\overline{v_n}\right|
 =\sigma_B A_L.
\]

Normality makes each fixed normalized correlation tend to zero: the fixed
mode is again `h(16^ell-1)`, and Abel summation with the monotone weights
`p_n p_(n+ell)=O(B^-2)` gives a raw sum `o(B^-1)`; division by `S >= 1/B`
gives `o(1)`. AL-02 and `sigma_B <= 2` therefore imply

\[
 R^{\rm abs}_{B,L(B),h}\longrightarrow0
 \quad\text{for every }L(B)\longrightarrow\infty.
\]

Conversely, when `1 <= L(B) <= B`, this all-mode absolute estimate implies
the signed estimate through `R <= R^abs`; IAD-01's finite inequality and the
already imported Basel--Tauberian/Weyl bridge give normality. Thus the
absolute aggregate left unresolved in IAD-02 has the same all-mode
asymptotic strength as its signed counterpart. A termwise absolute bound
can still have much worse finite constants and rates; this theorem does
not recover the efficiency of signed cancellation in a finite calculation.

## Hostile distinctions: one mode, maxima, and rates

### A single vanishing mean does not suffice

For the auxiliary sequence `z_n=e(n alpha)`, `alpha` not an integer,
the first mean tends to zero, while for `H <= N`

\[
 |c_N(\ell)|=1-\ell/N,\qquad
 A_{N,H}=\frac{H-1}{H}-\frac{H^2-1}{3HN}.
\]

Thus `A -> 1` whenever `H -> infinity`, `H/N -> 0`. The complex signed
response nevertheless tends to zero by geometric-series cancellation.
This is an auxiliary temporal sequence, not an asserted BBP completion.

There is also a radix-compatible control. Form the base-16 digit word by
concatenating, for `j=1,2,...`, the blocks `0^j 1^j ... 14^j`, and let its
value be `y`. Its orbit measure tends to the uniform measure on the 15
fixed points `k/15`, `0 <= k <= 14`. To verify this, discard a fixed number
`K` of positions at each block boundary; elsewhere the next `K` digits
are constant and the phase is within `16^-K` of the indicated fixed point.
Boundary density tends to zero, and the proportions of the 15 block types
tend to `1/15`. First let the observed length tend to infinity, then let
`K` grow. Consequently the mode-1 Weyl mean tends to zero, while every
fixed-lag correlation tends to one. On schedules `H(N) -> infinity`,
`H(N)=o(sqrt(N))`, the same boundary count gives `A_(N,H,1) -> 1`.
As a same-forcing BBP example its seed is `s=y-pi/16`; it fails exact
original-zero authentication. This is not a counterexample about pi.

### Aggregate cancellation does not require a small growing-lag maximum

Let `D_j` be a cyclic base-16 de Bruijn word of order `j`, of period
`p_j=16^j`, and concatenate the stages `D_j` repeated `16^(j^2)` times.
Call the resulting number `y`. It is normal. For every fixed word length
`k`, each complete period in stages `j >= k` has exactly the uniform
frequency. An incomplete period costs at most `p_j` positions; the total
length of earlier stages is at least `16^(j^2-j)`, so
`p_j/(earlier length) -> 0`. Stage boundaries and the finitely many early
stages also have vanishing density. These estimates apply at every prefix,
which proves normality, not merely normality along stage endpoints.

At the end `N_j` of stage `j`, the current stage occupies proportion tending
to one, while `p_j/N_j -> 0`. For times with at least `p_j+j` digits left
in that stage, the phases at times `n` and `n+p_j` share their first `j`
digits. Hence, for every fixed `h`,

\[
 c_{N_j,h}(p_j)\longrightarrow1.
\]

Thus even a normal radix orbit can have individual growing-lag responses
arbitrarily close to perfect coherence. Since
`p_j=N_j^(1/(j+1)+o(1))`, these lags eventually lie below `N_j^a` for every
fixed `a>0`. The average in AL-03 still tends to zero. The distinction
between a maximum and a weighted aggregate is essential.

No universal quantitative decay rate follows from the qualitative theorem:
its proof first fixes `J`, then requires the unknown finite set of fixed-lag
coefficients to become small. For the authenticated pi orbit that is still
an unpaid arithmetic estimate.

## Claim ledger and decisive probes

| Claim | Status | What it buys | Next falsifier |
|---|---|---|---|
| AL-01 finite tensor inequality | PROVED LOCAL | An exact bound using finitely many fixed-lag magnitudes | A finite vector violating AL1 or AL2 |
| AL-02 every absolute schedule | PROVED LOCAL | A limit theorem with the required lag coupling retained | A positive-definite autocorrelation family contradicting AL3 |
| AL-03/04 all-mode normality equivalence | PROVED LOCAL, using the existing classical bridges | Resolves the explicit IAD-02 absolute-aggregate question | A gap in the fixed-frequency or weighted Abel transport |
| Uniform maximum follows from normality | REFUTED | Eliminates an unnecessarily strong target | The de Bruijn-stage construction above |
| Original BBP absolute or signed saving | OPEN | Would give the corresponding Weyl/R0 consequence | Source-specific proof or rigorously certified refutation of proposed constants |

The independent executable [tensor_audit.py](tensor_audit.py) uses finite
vectors with entries `+1` and `-1`. Their correlations, absolute correlations,
`A_H`, and `G_H` are rational. AL2 is then an exact rational comparison. AL1 is checked
without evaluating a square root: for `a=(kJ/H)^2 G_J`, `b=(r/H)^2`,
compare `G_H <= a+b` first; if false, the equivalent remaining check is
`(G_H-a-b)^2 <= 4ab`. The cases include `H=1`, `J=H`, `J` dividing `H`, and
padded windows longer than the vector. The actual execution passed **1,164
AL1 comparisons and 414 AL2 comparisons** over 60 deterministic sign vectors,
with lengths from 1 through 89. The non-positive-definite mutation was rejected:
`G_100=829/1000 > G_10=1/10`, despite `10` dividing `100`.

Run `python research/2026-11-13/joint_time_lag_response/tensor_audit.py`.
The exact output is retained in [TENSOR_AUDIT.json](TENSOR_AUDIT.json), including
the input-generation parameters and a hash of the generated sign vectors.
No production module is imported. This is a separate implementation check,
not independent reasoner evidence. A computation verifies the formulas only;
the proofs above carry their universal quantifiers.
