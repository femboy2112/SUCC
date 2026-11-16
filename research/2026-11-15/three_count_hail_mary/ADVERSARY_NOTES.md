# Three-count budget: clock orientation and typed finite shadows

**Independent adversary lane, 2026-11-15.** Parent commit:
`bf27f7ec8e757482613808bff693ba520ac13b3b`. This first pass consulted the
parent dossier and the hole contract, but no other new agent report.

**Verdict.** The three-count inequality is sound. Its proposed positive
lower bound contains a clock/carry orientation requirement that is stronger
than the selected carry-density conclusion. An explicit period-four word
has uniform carry residues and selected density `1/2`, but three-count mean
`-1/4`. Frame rotation removes that orientation penalty only by returning
to an unknown carry marginal. A new exact rational finite-shadow theorem
shows that the original forcing, rational finite states, and arbitrarily
deep fixed dyadic agreement with the canonical trajectory allow **any
prescribed finite carry-residue word** when the seed is permitted to change.
This rules out seed-uniform bounded-drift proofs; it does not rule out an
estimate that uses the exact zero seed.

The results below are elementary proved identities or scoped controls.
They do not establish the positive-density theorem for the original source.

## 1. The budget is one signed clock/carry statistic

Keep the exact source and definitions in `HOLE_CONTRACT.md`. Write
`c=C_n mod4`, `j=J_n=n mod4`, and `k=K_n=(j-c) mod4`. The inherited
three-count summand is

\[
q(j,k)=\mathbf1_{j=k=0}+\mathbf1_{k=1}
       -\mathbf1_{j<2,k<2}.
\]

Substitution gives the exact function

\[
\boxed{\ell(j,c)=\mathbf1_{j=2,c=1}
                  +\mathbf1_{j=3,c=2}
                  -\mathbf1_{j=1,c=1}.}\tag{A1}
\]

Its table, with clock classes in rows and carry classes in columns, is

\[
\begin{array}{c|rrrr}
 j\backslash c&0&1&2&3\\\hline
0&0&0&0&0\\
1&0&-1&0&0\\
2&0&1&0&0\\
3&0&0&1&0
\end{array}.
\]

Thus on every integer shell, without a boundary error,

\[
\boxed{L_B=\Pr_B(n=2\bmod4,C_n=1\bmod4)
 +\Pr_B(n=3\bmod4,C_n=2\bmod4)
 -\Pr_B(n=1\bmod4,C_n=1\bmod4).}\tag{A2}
\]

This cancellation means that the three separate mass estimates are one
sufficient way to pay the budget, not three independent necessities.
In particular, the authentic clock being uniform does not imply that its
joining with the carries is suitably oriented.

For complete four-step blocks the exact score is

\[
\ell_{4m+1}+\ell_{4m+2}+\ell_{4m+3}+\ell_{4m+4}
=\mathbf1_{C_{4m+3}=2}
 +\mathbf1_{C_{4m+1}\ne1,C_{4m+2}=1}
 -\mathbf1_{C_{4m+1}=1,C_{4m+2}\ne1},\tag{A3}
\]

where all carry equalities in (A3) are modulo four. The negative term is a
specific one-step loss of carry class one, at a declared clock phase. This
is a temporal probe that a proposed causal estimate must address.

## 2. Exact Fourier content and the clock correction

Let `i=sqrt(-1)` and use the explicitly oriented transform

\[
\widehat\ell(a,b)=\frac1{16}
 \sum_{j,c=0}^3\ell(j,c)i^{-aj-bc},\qquad a,b\in\mathbb Z/4\mathbb Z.
\]

Then

\[
16\widehat\ell(a,b)
=-i^{-a-b}+i^{-2a-b}+i^{-3a-2b},\tag{A4}
\]

and the coefficient matrix is

\[
16\widehat\ell=
\begin{pmatrix}
1&-1&1&-1\\
-1+2i&1&1&-1-2i\\
1&1-2i&-3&1+2i\\
-1-2i&-1+2i&1&1
\end{pmatrix}.
\]

Define the source-attached twisted sums

\[
M_B(a,b)=\frac1B\sum_{B\le n<2B}i^{an+bC_n}.
\]

Every coefficient is nonzero. However the obligation asks for only one
real linear combination, not that all twelve non-clock modes separately
vanish. Summing the four `b=0` terms exactly gives

\[
\boxed{L_B=\frac1{16}+\frac{t_{B\bmod4}}{16B}
 +\sum_{a=0}^3\sum_{b=1}^3\widehat\ell(a,b)M_B(a,b),
 \quad(t_0,t_1,t_2,t_3)=(0,-5,6,-3).}\tag{A5}
\]

The last sum is real by conjugate pairing. Equation (A5) identifies the
signed temporal Fourier combination that would have to be controlled; it
does not derive its cancellation from the source. A result for the
untwisted carry marginal alone leaves the `a!=0` clock correlations unpaid.

An alternative exact split uses `p_{2,B}=Pr_B(C_n=2 mod4)` and

\[
\Xi_B=\frac{p_{2,B}}4-\Pr_B(n=3\bmod4,C_n=2\bmod4)
 +\Pr_B(n=1\bmod4,C_n=1\bmod4)
 -\Pr_B(n=2\bmod4,C_n=1\bmod4).
\]

Then `L_B=p_{2,B}/4-Xi_B`. A source lower bound `p_2>=rho` and a one-sided
clock-bias bound `Xi<=rho/4-delta` suffice. Neither estimate follows from
the finite Fourier identity.

## 3. A negative cycle despite uniform carry residues

Use the established exact completion and tail bound

\[
\alpha=\pi/16,\quad
P_N=\sum_{m=1}^N16^{-m}r(m),\quad
T_n=16^n(\alpha-P_n),\quad
0<T_n<\frac1{64n^2}\quad(n\ge1).
\tag{A6}
\]

The bound is inherited from `../carry_quadrature_assault/WINDING_PACKETS.md`,
Section 1, where it is proved by a positive polynomial identity.

For a real changed seed `s=beta-alpha`, the **unchanged forcing** gives

\[
U_n(s)=16^n\beta-T_n.
\]

Choose the rational completed endpoint

\[
\beta=0.\overline{5674}_{16}
      =\frac{\mathtt{0x5674}}{16^4-1}.
\]

Every fractional part `{16^n beta}` lies between `4/15` and `7/15`.
Since `T_n<1/64`, subtraction never crosses an integer for `n>=1`.
Consequently `C_n(s) mod4` follows `(1,2,3,0)` as `n` follows
`(1,2,3,0) mod4`. The carry marginal is exactly uniform on each complete
four-step block and

\[
\boxed{\lim_{B\to\infty}d_B(s)=\frac12,
       \qquad\lim_{B\to\infty}L_B(s)=-\frac14.}\tag{A7}
\]

Here `L_B(s)` in the real enlarged family is explicitly the statistic (A2).
It is not silently called a dyadic cofactor statistic: `s=beta-alpha` is
irrational, and these finite states are outside the exact rational carrier.
For the constant word `4`, the analogous endpoint is `beta=4/15` and both
`d_B(s)` and `L_B(s)` are zero. The word `5444` gives `d=1/4,L=-1/4`.
The word `4567` gives uniform carry residues but `L=1/2`.

**Scope of refutation.** Uniform carry marginals, the same four poles,
and positive source tails do not force this
specific signed clock/carry mean across the enlarged seed family. The
original zero seed is absent from these controls. They do not refute the
zero-seed assertion. Section 4 repairs the rational and dyadic typing for
arbitrarily long finite controls, without changing that scope.

## 4. New exact control: arbitrary finite words at any fixed dyadic precision

**Theorem A-FS (proved).** For every integer `N>=1`, every integer `L>=2`,
and every prescribed word

\[
(c_1,\ldots,c_N)\in\{0,1,2,3\}^N,
\]

there is an explicitly constructible rational seed
`s=s(N,L,c) in 2^L Z_(2)` such that the exact original four-pole recurrence
has:

1. rational odd-denominator states at every time;
2. `U_n(s)-U_n(0)=16^n s`, and thus
   `U_n(s)=U_n(0) mod 2^(L+4n)` for every `n>=0`;
3. `floor(U_n(s))=c_n mod4` for every `1<=n<=N`;
4. genuine cofactor residues `K_n=[U_n(s)-floor(U_n(s))]_4=(n-c_n) mod4`
   throughout that finite horizon;
5. reduced rational height at most `2^(L+4N+8)+1`.

Here `Z_(2)` denotes rational numbers with odd reduced denominator. The
quantifiers are **for every horizon and precision there exists a seed**.
There is no assertion that a single rational seed realizes every horizon.

### Constructive proof without a pi-value oracle

Let `d_n=4+c_n`, form the base-sixteen integer

\[
D=\sum_{n=1}^N d_n16^{N-n},\qquad
\beta=\frac{D}{16^N-1}=0.\overline{d_1\ldots d_N}_{16}.
\]

Then every shift of beta has fractional part in `[4/15,7/15]`, and the
last digit of `floor(16^n beta)` is `d_n` for `1<=n<=N`.
Compute the **finite rational** BBP prefix `P_(N+1)`. Set

\[
Q=2^{L+4N+8}+1,\qquad
m=\left\lfloor\frac{(\beta-P_{N+1})Q}{2^L}+\frac12\right\rfloor,
\qquad s=\frac{2^L m}{Q}.\tag{A8}
\]

The denominator `Q` is odd, so `s in 2^L Z_(2)`. Rounding gives

\[
|s-(\beta-P_{N+1})|\le\frac{2^{L-1}}Q
 <\frac{16^{-N}}{512}.
\]

By (A6),

\[
0<\alpha-P_{N+1}
 <\frac{16^{-(N+1)}}{64(N+1)^2}
 \le\frac{16^{-N}}{4096}.
\]

Hence

\[
\boxed{|s-(\beta-\alpha)|<\frac{16^{-N}}{256}.}\tag{A9}
\]

Writing `epsilon=s-(beta-alpha)`, for `1<=n<=N` one has

\[
U_n(s)=16^n\beta-T_n+16^n\epsilon,
\qquad |16^n\epsilon|<1/256.
\]

The fractional part before the small correction has the explicit margins

\[
\frac4{15}-\frac1{64}-\frac1{256}>0,
\qquad
\frac7{15}+\frac1{256}<1.
\]

Therefore `floor(U_n(s))=floor(16^n beta)` throughout the required horizon.
The source recurrence and its authentic mod-four clock prove the dyadic
claims. Finally `0<s<1`: the source bounds give
`0<P_(N+1)<alpha<47/240+1/1024<1/5`, while beta is at least `4/15`,
and the rounding error is less than `1/512`. Thus the unreduced numerator
is positive and smaller than `Q`, proving the height bound. All operations
in (A8) use rational arithmetic and the original finite BBP source.

### Relation to prior work and exact boundary

`../../2026-11-14/seed_source_rank/SEED_ADMISSIBILITY_THEOREMS.md`, Section 4,
already proves a finite rational shadow from `s_N=-P_N`. The additions here
are arbitrary carry-residue words, arbitrary prescribed fixed dyadic
precision, genuine odd-denominator cofactor typing, and an explicit linear
bit-length height bound. Academic priority is not claimed.

This theorem shows that fixed-depth dyadic observations plus the unchanged
forcing cannot distinguish the desired finite carry behavior from an
arbitrary one when the origin is known only modulo that depth. The exact
condition `s=0` immediately distinguishes them. It does not establish
non-normality or anti-lock failure for any **one fixed rational** seed.

## 5. The obstruction to uniform bounded potentials

Suppose a proposed argument asserts, for every rational seed in the above
class and every sufficiently late `n`,

\[
\ell_n(s)\ge\delta
 +V_{n+1}(U_{n+1}(s))-V_n(U_n(s))-e_n(s),\tag{A10}
\]

with `delta>0`, uniformly bounded `|V_n|<=M`, a common onset, and
`sum_(B<=n<2B) e_n(s)=o(B)` **uniformly over these seeds**.

Choose arbitrarily large `B` divisible by four and apply Theorem A-FS with
`N=2B`, the negative word `c_n=n mod4`, and any fixed desired precision `L`.
Then the left shell sum is exactly `-B/4`, but summing (A10) forces

\[
-\frac B4\ge\delta B-2M-o(B),
\]

a contradiction. The all-zero carry word similarly rules out a uniform
positive drift for the selected gate itself. The stronger negative cycle
also defeats a uniform nonnegative drift for this particular budget.

This is a precise architecture obstruction, not an impossibility theorem
for using potentials. A zero-seed-only potential, seed-dependent onset,
non-uniform error, or potential whose boundary cost grows with the seed
height can escape it. For the negative word any valid (A10) must pay a
potential boundary of magnitude at least `(delta+1/4)B-o(B)`. Since the
constructed seed has logarithmic height `O(L+B)`, growth with seed
description length is one explicit place where this cost may live.

## 6. Rotating and reflecting the certificate

For any empirical law of `(J,K)`, define four rotations

\[
q_t(J,K)=q(J-t,K-t),\qquad t=0,1,2,3,
\]

with all arguments reduced modulo four. These preserve `C=J-K mod4`, so
each remains a valid pointwise lower certificate for the selected gate.
From (A1),

\[
\boxed{\sum_{t=0}^3q_t(J,K)=\mathbf1_{C=2}.}\tag{A11}
\]

The sum is nonnegative, but it need not be positive: the entire mass may
have `C=0` or `C=3`, or may occupy only selected residue one. Thus a lower
bound for `Pr_B(C=2)` makes some rotated certificate positive, while the
rotation attaining the maximum may depend on `B`.

The reflection `(J,K)->(-J,1-K)` sends `C` to `3-C` and preserves the
selected set `{1,2}`. Define the other four valid certificates

\[
q_t^*(J,K)=q(-J-t,1-K-t).
\]

They sum to `1_(C=1)`. Consequently the eight-certificate identity is

\[
\boxed{\sum_{t=0}^3\{q_t(J,K)+q_t^*(J,K)\}
       =\mathbf1_{C\in\{1,2\}}.}\tag{A12}
\]

Let `M_B` be the maximum of the eight empirical certificate means. Then

\[
\boxed{\frac{d_B}{8}\le M_B\le d_B.}\tag{A13}
\]

Therefore `liminf_B M_B>0` is **equivalent** to positive lower selected
shell density. It is a strictly more permissive diagnostic than demanding
positivity in the original fixed frame. The period `5674` is an explicit
witness that the latter can fail while (A13) succeeds. This repair adds no
source proof by itself; it removes an unnecessary choice of clock origin
from a sufficient certificate. Requiring one preselected frame to work on
every large shell is not justified by (A13).

## 7. Receipts, next probe, and claim status

An inline Python audit, run in this worktree with exact `Fraction`
arithmetic, checked:

- all sixteen collapsed table entries;
- all thirty-two rotation and reflection identities;
- 504 finite rational itinerary positions, for `N in {8,16,32}`,
  `L in {2,8,32}`, and negative-uniform, zero-gate, and nonconstant words;
- the exact recurrence difference, dyadic divisibility at depth `L+4n`,
  literal floor residues, and genuine cofactor reduction at every position;
- all sixteen Gaussian-integer Fourier coefficients and all sixteen
  synthesis values.

All checks passed. One independently reproducible seed from (A8), for
`N=8,L=2,c_n=n mod4`, is

\[
s=\frac{621721628472}{4398046511105}.
\]

Its denominator has 43 bits. These finite checks calibrate the explicit
formula; the universal finite-horizon theorem rests on the displayed bounds.
No full repository test or new original-source numerical holdout was run
by this lane; the parent owns those validations.

**Next useful attack.** Work with (A2) or the frame envelope (A13), and seek
an inequality that explicitly charges the exact zero origin. A proposed
source contraction or positive energy drift must predict why the
finite-height shadows lose that estimate, with the difference appearing
in an exact boundary term or in a stated seed-dependent constant. For the
fixed original frame, (A3) identifies the precise loss transition that
must be offset; for the frame envelope, the source only needs a positive
selected marginal. The latter avoids proving unnecessary clock balance.

| Claim | Status | Boundary |
|---|---|---|
| Collapsed budget, Fourier expansion, and clock correction | Disclosed: elementary proof | Does not estimate the source sums |
| Uniform carry marginal implies positive fixed-frame budget | Refuted by period `5674` | Enlarged real seed family; finite rational typed shadows supplied |
| Arbitrary finite carry words with any fixed dyadic precision | Disclosed: constructive theorem A-FS | Seed depends on horizon and precision |
| Uniform bounded positive-drift architecture over those seeds | Refuted by A-FS and telescoping | Zero-seed-only or non-uniform methods survive |
| Eight-frame envelope equivalent to selected density | Disclosed: pointwise identity | Equivalent target, not a source theorem |
| Original zero-seeded eventual budget or selected density | Open | No source-selected asymptotic lower bound is proved here |

## 8. Second-pass audit: seam-matched tail transfer and its sharp rate

**Provenance of this section.** The first-pass results above were completed
before the parent requested this independent check of the translator's
tail-mask proposal and the constructor's sparse-marker proposal. Their
formulas were supplied in the parent's message. This section verifies those
formulas by a separate digit argument; it is not an independent source
family and does not establish the canonical source asymptotics.

### All endpoints: exact seam-matched bound

For any fixed real completed endpoint `beta`, set

\[
Q_n=\lfloor16^n\beta\rfloor,\quad x_n=\{16^n\beta\},\quad
C_n=\lfloor16^n\beta-T_n\rfloor,
\quad b_n=\mathbf1_{x_n<T_n}.
\]

Since `0<T_n<1`, one has exactly `C_n=Q_n-b_n` for `n>=1`.
The strict inequality is essential: `x_n=T_n` gives no borrow. Use the
canonical hex digits `a_n=Q_n-16Q_(n-1) in {0,...,15}`; terminating
expansions use eventual zero digits, so no representation ambiguity enters.

Consider any clock-dependent mask `f_j(c)` on modulo-four carries with

\[
f_j(0)=f_j(3)\quad\hbox{for every }j,\qquad
D_f=\max_{j,c}|f_j(c-1)-f_j(c)|.
\]

On a shell `B<=n<2B`, put

\[
m_B=\lfloor\log_{16}(64B^2)\rfloor\ge1.
\]

A changed mask value requires both a borrow and `Q_n mod4!=0`; at the
modulo-four seam, the mask values are equal. Thus the current digit `a_n`
is nonzero. A borrow implies

\[
x_n<T_n<\frac1{64B^2}\le16^{-m_B},
\]

which forces `a_(n+1)=...=a_(n+m_B)=0`. Every other changed-mask position
must lie at least `m_B+1` indices later. A set with this spacing in an
integer interval of length `B` has size at most

\[
\boxed{1+\left\lfloor\frac{B-1}{m_B+1}\right\rfloor
       =\left\lceil\frac B{m_B+1}\right\rceil.}\tag{A14}
\]

Consequently

\[
\boxed{\left|\frac1B\sum_{B\le n<2B}
 [f_{n\bmod4}(C_n)-f_{n\bmod4}(Q_n)]\right|
 \le\frac{D_f}{B}
 \left(1+\left\lfloor\frac{B-1}{m_B+1}\right\rfloor\right).}\tag{A15}
\]

This holds for every integer `B>=1`, every real endpoint, and the same
literal BBP tail. Both the selected gate and all eight certificates in
Section 6 are seam matched with `D_f=1`. Thus they admit a uniform
`O(1/log B)` completed-digit transfer, even if the raw borrow count itself
has positive density.

**Seam mutation control.** At `beta=0`, `Q_n=0` and `C_n=-1` at every
positive time. The non-seam-matched mask `f(c)=1_(c=0)` differs by one
everywhere. Hence the seam hypothesis cannot simply be dropped. For
time-dependent masks this example need not defeat each special average
whose clock coefficients cancel, but it decisively defeats a universal
vanishing-error theorem without seam matching.

### A single endpoint attaining the logarithmic order

Let `A=1024/15`, set `n_1=2`, and recursively choose

\[
q_k=\min\{q\in4\mathbb N_{>0}:16^q-1>A(n_k+1)^2\},
\qquad n_{k+1}=n_k+q_k,
\qquad \beta=\sum_{k\ge1}16^{-n_k}.\tag{A16}
\]

The gap sequence is nondecreasing because its threshold increases with
`n_k`. It tends to infinity and satisfies
`q_k=2 log_16(n_k)+O(1)`. Every marker index is `2 mod4`; its digit is one,
and all nonmarker digits are zero. The endpoint is irrational because it
has infinitely many markers and unbounded zero gaps, so its digit sequence
cannot be eventually periodic.

At a marker, monotonicity of the future gaps gives

\[
\{16^{n_k}\beta\}
\le\sum_{h\ge1}16^{-h q_k}
=\frac1{16^{q_k}-1}
<\frac{15}{1024(n_k+1)^2}<T_{n_k}.\tag{A17}
\]

The final strict lower bound is the inherited BBP source-tail bound from
`../carry_quadrature_assault/SOURCE_EXCITATION.md`, Section 2. Therefore
every marker borrows. Its completed carry residue is one, its raw residue
is zero, and its clock is two, so its completed budget score is `+1` and
its raw score is zero. At a nonmarker the completed residue is zero and
the raw residue is zero or three; both budget scores are zero. Hence

\[
L_B^{\mathrm{raw}}(\beta)=0,\qquad
L_B^{\mathrm{completed}}(\beta)
=\frac1B\#\{k:B\le n_k<2B\}.\tag{A18}
\]

On this shell the consecutive marker gaps are
`2 log_16 B+O(1)` uniformly; the two endpoint gaps contribute only `O(1)`
markers. It follows that

\[
\boxed{L_B^{\mathrm{completed}}(\beta)
       -L_B^{\mathrm{raw}}(\beta)
       =\frac{1+o(1)}{2\log_{16}B}.}\tag{A19}
\]

Thus the logarithmic order in the universal mask-transfer estimate is
sharp, even for one fixed endpoint. It is not a claim of rate sharpness
for the authentic endpoint `alpha=pi/16`. Here the forcing is unchanged
and the seed is changed to `beta-alpha`. This seed is nonzero: (A16)
gives `beta<=16^(-2)/(1-16^(-4))<1/16`, whereas
`alpha>P_1=47/240>1/16`. Its rationality is **not** determined merely from
the irrationality of both endpoints, and no rational cofactor typing is
asserted for this sharpness example.

**Audit verdict.** The seam-matched transfer, strict-boundary convention,
integer spacing count, and stated logarithmic sharpness construction all
survive this independent derivation. The minimal-multiple rule in (A16)
is needed for the claimed rate; arbitrary oversized gaps would still
force borrowing but could make the discrepancy much smaller.
