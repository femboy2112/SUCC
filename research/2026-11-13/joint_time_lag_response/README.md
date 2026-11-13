# Joint time–lag response: coupling, inverse stability, and the remaining arithmetic

Research round, 2026-11-13. **R0 and base-16 normality of pi remain OPEN.**
The round proves a finite target-recovery estimate, closes an explicitly open
analytic distinction in the archive, and improves the source-completion error
for the actual signed lag response. It does not prove a new all-scale Fourier
saving for pi. The proofs are paper proofs with exact computational audits and
same-model review, not external refereeing or Lean certification.

Live main was verified as `db9fb4b84672050efa79b13377f1e73364598a14`.
This branch is a child of unmerged #608 (`7f11088bf5e3d216ca0f6ae57da1544e17c46d1c`).
New siblings #609 (`117d06e126d8ae4fc6d41e3786a3aad350637be6`) and #610
(`00897c94289fc94a491429d4054d548afe20b7c2`) were inspected and are not integrated.
No frozen source, historical claim, main branch, tag, or release is changed.

## A. Reconstructed shape

The full previous-round genealogy remains in
[the parent dossier](../../2026-11-12/leah_gamma_twist/GENEALOGY.md).
This round traced the narrower joint-field lineage rather than claiming another
complete read of the archive. Five consequential connections are:

| Earlier object | Present consequence | Authority boundary |
|---|---|---|
| Source-pointed observation and operational Yoneda | A lag record needs an anchor to recover an absolute phase target | Exact fifteenfold ambiguity was already PSG-11 and sibling #610 OB-02 |
| Signed pushforward and phase-decorated Gram | Keep the signed cross terms in one common clock | A positive Gram matrix alone supplies no saving |
| IAD-01/02 padded window energy | The signed Fejer gate is already schedule-free | This round does not claim that gate as new |
| One common shift orbit and its conjugate tensor | Squared lag magnitudes remain positive definite; absolute aggregates obey a uniform window comparison | New local closure of IAD-02's unresolved absolute-aggregate question; classical tensor mechanism |
| BBP positive Mellin tail and CT-01 moving conductors | The analytic completion error can be made small without lowering arithmetic conductor | Stable transport is proved; real signed cancellation remains missing |

The tensor mechanism has a clear classical ancestor: Tao's
[2021 tensor-power treatment of simultaneous correlation](https://terrytao.wordpress.com/2021/02/27/boosting-the-van-der-corput-inequality-using-the-tensor-power-trick/).
The full finite proof needed here is supplied in [ABSOLUTE_LAGS](ABSOLUTE_LAGS.md).
This attribution is not a claim that Tao's result proves anything about the
selected BBP point.

## B. The precise wall

Retain the exact four-pole forcing and original zero seed:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad Y_n=U_n+T_n=16^n\pi/16.
\]

For a shell of length B, set

\[
c_{B,h}(\ell)=B^{-1}\sum_{n=B}^{2B-1-\ell}e(h(Y_{n+\ell}-Y_n)),\qquad
F_{B,H,h}=H^{-1}+\frac2H\sum_{\ell=1}^{H-1}(1-\ell/H)\Re c_{B,h}(\ell).
\]

The exact inherited gate is

\[
|W_B(h)|^2\le(1+(H-1)/B)F_{B,H,h},\qquad F_{B,H,h}\ge0.
\]

An all-mode bound `F_(B,H(B),h)->0`, with `H(B)->infinity` and `H(B)<=B`,
would prove normality. Across all modes it is already an equivalent formulation.
R0 asks only `Re W_B(1)<=1-eta` on every sufficiently late shell. Neither
estimate is proved here. The remaining obstruction is a **missing arithmetic
proof pathway**, not missing access to the exact source or inability to define
the joint field. Specific observation families also have proved boundaries.

The archive's CT-01 prevents one tempting simplification: for integer stencils
`P_n` of width `o(n)` and subexponential coefficient norm, `P_n(16)!=0` implies
`log den(P_n(E)U_n)=6n+o(n)`. If `P_n(16)=0`, the completed filtered phase is
zero for every seed. Short linear differencing therefore has no polynomial-style
degree descent in this precise conductor sense. This does not exclude nonlinear
filters or inequalities on signed combinations of their outputs.

## C. The source-first, boundary-first, and coupled pictures

The source-first affine recurrence and the real completion commute exactly.
The joint boundary response is

\[
C_h(n,\ell)=e(h(Y_{n+\ell}-Y_n)),\qquad
C_h(n,\ell+m)=C_h(n,\ell)C_h(n+\ell,m).
\]

At fixed lag the correct reference is Haar on the graph `v=16^ell u mod1`.
Its Fourier response is one on `a+16^ell b=0` and zero elsewhere. Coherent
resonances must survive even for a normal point. The empirical weights along
that graph, rather than geometric coverage of it, are the statistical target.

The field is a rank-one phase kernel: `C_h(n,ell)=z_(n+ell) conjugate(z_n)`.
Its common shift realization supplies the coupling needed in the tensor proof.
An initial phase port restores the orientation lost by neutral products.
These are actual maps, not a Lorentzian or gravitational identification.

Two target distinctions are proved in [LAG_COMPLETENESS](LAG_COMPLETENESS.md):

- All Fourier modes at **one fixed nonzero lag** already detect normality.
  An invariant lift of Haar through multiplication by any nonzero integer is
  Haar. The fifteenfold point ambiguity does not leave a hidden non-Haar lift.
- All lags at **only odd Fourier modes** do not suffice. Fair independent
  hexadecimal digits in `{0,8}` give a singular invariant law with every such
  lag response zero, but `Re mu_hat(2)>0.9`. This is a hostile auxiliary law,
  not the zero-selected BBP orbit.

## D. Three explicit next candidates, ranked by direct relevance

1. **A uniform finite-window source gap.** For some fixed integer `H>=2`,
   delta>0 and B0, prove `F^U_(B,H,1)<=1-delta` for every B>=B0. The proved
   transport and padded-window inequality imply R1 and hence R0. This is a
   stronger sufficient condition, not a necessary reformulation of R0;
   nonnormal digit processes can satisfy it. The new ingredient must exclude
   long selected alignment with the fixed-point sectors. The coherent
   counterseed fails it. A proposed explicit B0,delta can be falsified by the
   exact finite instrument; finite success cannot prove the existential claim.

2. **Quantitative failure of prime/cofactor conjugate alignment.** Retain the
   literal factorization `z_n=A_n B_n` on a native prime-birth window. Prove,
   on a positive fraction of every large shell, constants epsilon,delta>0 with
   `|mean A|<=1-epsilon` and
   `|mean[(A-mean A)(B-mean B)]| <= (1-delta)
   sqrt((1-|mean A|^2)(1-|mean B|^2))`.
   The elementary covariance inequality then gives a uniform modulus saving.
   This precise candidate is inherited from sibling #610, not newly proved.
   At the coherent counterseed `B=conjugate(A)`, its strictness fails exactly.
   Prime-only cancellation cannot supply the missing second inequality.

3. **A fixed-lag arithmetic family.** For the actual source, prove for every
   fixed h!=0 that `B^-1 sum_(B<=n<2B)e(h(U_(n+1)-U_n))->0`.
   [LAG_COMPLETENESS](LAG_COMPLETENESS.md) shows that this alone would imply
   normality. Its novelty tax is unpaid: it is equivalent to normality and
   moves the full Fourier family to multiples of 15. It is a compact interface,
   not an additional theorem or an independently justified arithmetic route.

No candidate is ranked as established. The first two require a genuinely new
source-dependent estimate. The third states exactly what an apparently complete
single-lag oracle would still have to prove.

## E. Best actual results

**Finite inverse stability.** Suppose two exact radix orbits obey
`||15*16^n(x-y)||<=epsilon<1/17` for n=0,...,N-1. Then for one k modulo 15,

\[
\left|W_N(x)-e(k/15)W_N(y)\right|
\le\frac{32\pi\epsilon}{225N}(1-16^{-N}).
\]

The coarse anchor `||x-y||<=1/30` forces k=0. The proof lifts the small lag
errors to u_n: `16u_n-u_(n+1)` is an integer of magnitude below one, so it
vanishes. Thus `|u_n|<=epsilon*16^(n-N+1)`; summing the character errors proves
the bound. At epsilon=1/17 the period-two point 1/255 defeats it. One bad
clock also defeats an average-error replacement: y=1/240 versus x=0 has
the coarse initial anchor and identical lag records for every n>=1, but its
mean tends to e(1/15). See [INVERSE_STABILITY](INVERSE_STABILITY.md) for scope.

**An actual consequence of coupling across lag families.** For normalized
autocorrelations c(ell), put

\[
A_H=\frac2H\sum_{\ell=1}^{H-1}(1-\ell/H)|c(\ell)|,\qquad
G_J=\frac1J+\frac2J\sum_{\ell=1}^{J-1}(1-\ell/J)|c(\ell)|^2.
\]

Then `sqrt(G_H)<=sqrt(G_J)+J/H` and
`A_H^2<=(1-1/H)(G_H-1/H)`. In particular if the first J-1 correlations are
at most epsilon in magnitude, `A_H<=J^(-1/2)+epsilon+J/H`.
The proof uses `w tensor conjugate(w)` and the common unitary shift.
Therefore fixed-lag cancellation forces the absolute aggregate to vanish on
**every** diverging schedule. Across all modes and admissible windows, signed
and absolute Fejer decay have the same asymptotic strength. This resolves the
question left open in IAD-02; it does not provide pi's fixed-lag estimates.

**Smaller authentic completion debt.** For every B>=1, 1<=H<=B and integer h,

\[
\boxed{|F^U_{B,H,h}-F^Y_{B,H,h}|
\le\frac{\pi|h|(H^2-1)}{128HB^3}.}
\]

The tail derivative bound `-T'(t)<1/(32t^3)` yields an integrated difference,
then the signed response's error telescopes to its two shell endpoints.
This is an unconditional source-preserving estimate with a complete error
budget. It permits `|h|H/B^3->0`; it does not assert either response shrinks.
The proof, provenance and rational certificate are in
[SOURCE_TRANSPORT](SOURCE_TRANSPORT.md).

## F. The smoking gun and its limitation

The lag coefficients are not independently adjustable spectral lines. They
come from **one shift orbit**, so their squared magnitudes have a common
positive-definite realization. That constraint closes a real archival gap:
fixed-lag information controls every growing aggregate without an invalid
interchange of limits. An arbitrary triangular array fails the same theorem.

This supports the proposed coupling mechanism in a precise, limited way.
It still cannot produce the first arithmetic cancellation input. Moreover a
normal radix orbit can have moving lags with correlation tending to one:
the repeated de Bruijn-stage construction in ABSOLUTE_LAGS proves it.
The useful condition is the aggregate response. Uniform suppression of every
coherent moving ray is unnecessarily strong and false even under normality.

## G. The next decisive strike and verification

Attack candidate 1 with an explicit fixed H, delta and eventual onset, using
the exact source and original zero anchor. The instrument takes B,H,h and
returns rigorous rational enclosures for F^U, F^Y and the completed mean.
It never accepts a caller-supplied claim that the mean is small. A valid
universal source argument should reject the coherent counterseed for a
quantitative source-dependent reason, not simply declare it unauthentic.

**Pass:** a proof of the stated every-large-shell inequality, including its
source dependence and paid endpoints. **Fail:** an exact violating shell
above a claimed explicit onset, or a same-hypothesis hostile source.
**Ambiguous:** favorable finite certificates with no universal argument.
Independent evidence should include a separately checked arithmetic proof or
formalization; same-model re-evaluation does not provide external independence.

The prospective [protocol](PROTOCOL.md), [finite receipt](RESULTS.json),
[source audit](SOURCE_AUDIT.json), [tensor audit](TENSOR_AUDIT.json), native
tests and executable probes preserve the controls and one repaired calibration
failure. See [VALIDATION](VALIDATION.md). Exact final-commit repository gate
outcomes are recorded in the draft PR. This research remains unmerged.
