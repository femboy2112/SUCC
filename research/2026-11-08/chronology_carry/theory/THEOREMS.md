# Carry control variates and the remaining signed estimate

Status: **PROVED PAPER** for the finite algebra and the conditional statements
below. The asymptotic original-zero hypotheses remain **OPEN**. No new
general martingale, Poisson-equation or van der Corput theorem is claimed.
This is a source-labelled composition of those elementary instruments that
does not require the raw phase to be accurately predictable in L1.

Source and proof baseline: parent
`19d98078b60e47092c9b9d050a70b6b7eabb7cd2`, literal

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

The source states are unwrapped rationals. Put
`x_n={U_n}`, `c_n=floor(U_n)-16 floor(U_(n-1))`, and `d_n=c_n mod16`.
The literal c_n is retained in the authenticated history; reduction to d_n
is an explicitly lossy observer. Set `f_n=e(hU_n)`, fixed integer h!=0.
For depth k>=1 and n>=k, the past-carry state is
`w_n=(d_(n-k+1),...,d_n)`. In particular it includes the carry arriving at n,
not an unannounced future digit.

## CCV1. An exact, finite memory Poisson compiler

This assertion is finite algebra for any alphabet size b>=2. On
`S={0,...,b-1}^k`, write `s(w,d)=(w_2,...,w_k,d)`. Define the **reference**
operator and reference mean

\[
(Pv)(w)=b^{-1}\sum_{d=0}^{b-1}v(s(w,d)),\qquad
\mu=b^{-k}\sum_{w\in S}g(w).
\]

For every complex table g, define

\[
\psi=\sum_{j=0}^{k-1}P^j(g-\mu).
\]

Then

\[
P^k g=\mu,\qquad (I-P)\psi=g-\mu,
\qquad \|\psi\|_\infty\le k\|g-\mu\|_\infty.       \tag{CCV1}
\]

**Proof.** After k uniform appends every starting word is forgotten, so
`P^k g` is the uniform average over all words. The finite geometric sum
telescopes to `g-P^k g`. Each P is a sup-norm contraction. These prove all
three statements. No source transition probability or ergodicity is used.
QED.

This gives a finite proof object `(g,mu,psi,P)` for a causal observer. It
does not introduce a new carrier category. The true source history still
restricts by prefixes; the map to w_n and evaluation of the table commute
with reading a sufficient prefix. **P is an analyst's reference operator,
not an asserted stochastic evolution of the exact source.** Calling P the
actual carry law without a separate theorem would reintroduce the forbidden
Haar-seed substitution.

### CCV1-L. A transient literal-carry alphabet removes any representation loss

For the original source at times n>=2, literal carries lie in `{0,...,16}`.
Extend the state space to `Splus={0,...,16}^k`, but let P append each of
`0,...,15` with weight1/16 and append16 with weight0. Its reference mean
is still the uniform average of g over the ordinary16^k words. After k
appends all exceptional16 symbols have been removed, **regardless of the
starting literal state**, so `P^k g=mu` on Splus. The geometric-sum proof
of CCV1 is unchanged. Thus CCV2–4 apply directly to the actual literal
carry path with this kernel, without a modulo projection or exceptional
correction. The state count is17^k. This reference kernel is not asserted
to be the actual carry law; actual transitions may append16.

The alternative residue representation and its explicitly paid correction
are retained in CCV6. They are different finite reference models.

### CCV1-Q. Carry propagation gives a smaller exact quotient

For a literal word v of length k define
`pi(v)=sum_(j=1)^k 16^(k-j) v_j mod q`, q=16^k. This takes the weighted
integer sum BEFORE reduction; it is different from reducing every symbol
modulo16 separately. Exact arithmetic gives

`pi(shift(v,c))=(16 pi(v)+c) mod q`, including c=16.

On `Z/qZ` use the reference operator
`(Pbar u)(s)=16^-1 sum_(d=0)^15 u((16s+d) mod q)`.
Then `(Pbar^k u)(s)=q^-1 sum_t u(t)` for every s, and pullback by pi
intertwines Pbar with the literal operator in CCV1-L. Thus for any table
`g(v)=gbar(pi(v))`, its mean, Poisson potential and signed innovation are
exactly computed on q states; the literal potential is the pullback of the
quotient potential. This is a proved target-sufficient history quotient,
not an assumption that arbitrary literal-history targets descend.

For the source, integer lifts `C_n=floor U_n` obey
`C_n=16 C_(n-1)+c_n`. Therefore `pi(v_n)=C_n mod q`. The compressed
observer retains this integer-lift residue and updates it using the literal
incoming carry; the original unwrapped history and all carries remain
authenticated upstream. It needs4k bits to distinguish all q residues.
For the target `e(h(s+1/2)/q)` with odd h, all q outputs are distinct, so
4k is also the exact worst-case information bound on this declared finite
residue carrier. This is not a lower bound for the singleton, fully known
zero-source history with unlimited replay.

## CCV2. The actual mean is reference mean plus one signed carry innovation

Take ANY deterministic admissible sequence `w_0,...,w_N` of carry words;
the local indices can be a translated original epoch. Put

\[
D_\psi=\frac1N\sum_{n=0}^{N-1}
 [\psi(w_{n+1})-(P\psi)(w_n)],\qquad
E_\psi=\frac{\psi(w_0)-\psi(w_N)}N.
\]

Then, exactly,

\[
\frac1N\sum_{n<N}g(w_n)=\mu+E_\psi+D_\psi.          \tag{CCV2}
\]

**Proof.** Insert CCV1, write
`psi(w_n)-Ppsi(w_n)=psi(w_n)-psi(w_(n+1))`
`+psi(w_(n+1))-Ppsi(w_n)`, and telescope. QED.

If `N(w,d)` counts actual outgoing edges and `N(w)=sum_d N(w,d)`, the same
innovation, for the ordinary b-symbol alphabet, is the SINGLE complex occupation contrast

\[
D_\psi=\sum_{w,d}\left[\frac{N(w,d)}N-
 \frac{N(w)}{bN}\right]\psi(s(w,d)).                 \tag{CCV2b}
\]

For CCV1-L's literal alphabet, the exact replacement is
`Dpsi=sum_(w,d=0..16)[N(w,d)/N-N(w)q(d)/N] psi(shift(w,d))`, where
`q(d)=1/16` for d=0,...,15 and `q(16)=0`. One must not subtract1/16
from the exceptional16 edge. The total-variation bound below then uses
this reference probability q, including its zero mass at16.

It is strictly less information than the whole conditional transition
table. For example, b=2,k=1, `g(0)=1,g(1)=-1`, and an even alternating
word path give mu=0, psi=g, E_psi=0 and D_psi=0. Every occupied row has a
deterministic next symbol and total variation 1/2 from the reference row.
Thus small D_psi does not assert conditional digit independence.

A useful but stronger upper bound is

\[
|D_\psi|\le 2\|\psi\|_\infty
\sum_{w:N(w)>0}\frac{N(w)}N\,
\operatorname{TV}\bigl(N(w,\cdot)/N(w),\mathrm{Unif}_b\bigr).
\]

The signed expression should be retained unless there is an actual bound
on this stronger total-variation statistic. Neither version has been proved
small for the original-zero carries.

## CCV3. Prediction error may be large while its signed residual cancels

Let f_0,...,f_(N-1) be the actual unit phases, choose a table g, and define
`e_n=f_n-g(w_n)`. For `1<=H<=N`, put

\[
C_d=\frac1N\sum_{n=0}^{N-d-1}e_{n+d}\overline{e_n},
\quad 0\le d<H,
\]

and

\[
V_H(e)=\frac{N+H-1}{NH}
\left[C_0+2\sum_{d=1}^{H-1}(1-d/H)\Re C_d\right].
                                                               \tag{CCV3a}
\]

The bracket is nonnegative; there is no deletion of negative cross terms.
Then

\[
\left|\frac1N\sum_{n<N}f_n\right|
\le |\mu+E_\psi+D_\psi|+\sqrt{V_H(e)}
\le |\mu|+\frac{2\|\psi\|_\infty}N+|D_\psi|+
\sqrt{V_H(e)}.                                      \tag{CCV3b}
\]

**Proof with normalization.** Extend e by zero outside `[0,N)`. Each e_n
appears H times in `sum_(t=1-H)^(N-1) sum_(j=0)^(H-1)e_(t+j)`. Cauchy–Schwarz
over these N+H-1 windows gives

\[
H^2\left|\sum_n e_n\right|^2
\le (N+H-1)\sum_{t=1-H}^{N-1}
\left|\sum_{j=0}^{H-1}e_{t+j}\right|^2.
\]

The last sum is
`HN [C0+2 sum_(d=1)^(H-1)(1-d/H) Re C_d]`.
Dividing by `H^2 N^2` proves `|mean e|^2<=V_H(e)` and bracket positivity.
Combine with CCV2. QED.

This is the padded-window identity already used in SUCC's
[`lag_instrument`](../../signed_covariance_round2/lag_instrument.py) and
earlier covariance dossiers, with a frozen carry control variate inserted.
It is not a new exponential-sum theorem. The improvement is the hypothesis
it permits: **a residual can have order-one L1/L2 size and still have a
vanishing signed covariance certificate.** For the exact toy e_n=(-1)^n
and even N, mean|e|=1, whereas even H gives the small boundary-only window
energy. This counterexample proves that demanding L1-small residual is
strictly stronger than the residual premise in CCV3.

The full cross terms of the control variate are load-bearing:

\[
C_d(e)=C_d(f)+C_d(g)-\frac1N\sum_{n<N-d}
\bigl[f_{n+d}\overline{g(w_n)}+
g(w_{n+d})\overline{f_n}\bigr].                       \tag{CCV3c}
\]

Reducing positive prediction error alone does not show that this signed
quantity improves. The zero predictor is an essential benchmark.

## CCV4. A conditional all-epoch gate, and its exact unpaid content

For every fixed h!=0 and every sufficiently large integer A, take the
original source interval `[A,2A)`, N=A. Let `k_A>=1`, let g_A be a declared
carry table, and form mu_A, psi_A, D_A and residual e from the actual source.
Assume there are integers `H_A` with `H_A->infinity`, `H_A/A->0`, such that

\[
|\mu_A|+\|\psi_A\|_\infty/A+|D_A|\longrightarrow0,
\qquad C_{0,A}/H_A\longrightarrow0,
\]

\[
\frac1{H_A}\sum_{d=1}^{H_A-1}(1-d/H_A)
\Re C_{d,A}\longrightarrow0.                         \tag{CCV4}
\]

Then the original dyadic Weyl mean tends to zero for that h. If these
conditions hold for every fixed nonzero integer h, the inherited Green-tail
and Weyl implications give base16 normality of pi.

**Proof.** CCV3a is `(1+(H_A-1)/A)` times
`C0/H_A+(2/H_A)sum weighted Re C_d`, so its nonnegative value tends to zero.
CCV3b now gives the Weyl gate. QED.

For uniformly bounded g_A, C0 is uniformly bounded. A convenient boundary
condition is `k_A ||g_A-mu_A||_infinity=o(A)`. Tables may depend on earlier
source histories. The deterministic inequality does not need statistical
independence. Freezing them before a holdout is an evidence discipline that
prevents a computed small bound from secretly reading the holdout target.

**Logical contribution.** This is a control-variate version of the existing
signed-covariance gate, not a claim of strictly weaker normality assumptions
than Weyl itself. It is strictly weaker than asking the raw residual to
vanish in L1. It transfers a frozen model's contribution to a specified
carry-transition contrast, leaving a specified residual lag average. Both
must receive new original-zero arithmetic bounds. Setting g=0 recovers
the inherited van der Corput gate, so this construction cannot be marketed
as theorem debt paid merely by adding the model.

## CCV5. Under normality, a fixed past-carry predictor cannot reconstruct raw phase

This theorem is an **implication conditional on normality**, not evidence
that pi is normal. Let an original-forcing seed s have completed value
`alpha=s+pi/16` normal in base16. Fix k>=1 and h!=0. Let g_A be any
uniformly bounded sequence of tables on k past carry residues. Then along
the dyadic epochs,

\[
\frac1A\sum_{n=A}^{2A-1}|e(hU_n(s))-g_A(w_n)|^2
=1+16^{-k}\sum_w|g_A(w)|^2+o(1),                    \tag{CCV5a}
\]

where the error is uniform over such bounded tables. In particular the
optimal L2 prediction error over arbitrary fixed-depth tables tends to 1.
For L1,

\[
\liminf_A\inf_g\frac1A\sum_{n=A}^{2A-1}
 |e(hU_n(s))-g(w_n)|\ge1.                            \tag{CCV5b}
\]

The zero table attains error 1 identically, so this infimum tends to 1.
The same conclusions hold for uniformly bounded tables of the **literal**
past carries in `{0,...,16}^k`; the reference sums still range only over
`{0,...,15}^k`. Since `0<r(n)<1` eventually, these are all late literal
carry values. The exceptional value16 is not silently treated as a usual
hexadecimal digit.

**Proof, including literal carry transport.** The exact Green identity gives
`U_n(s)+T_n=16^n alpha`, with `T_n>0` and `T_n->0`. Write
`y_n={16^n alpha}`, `j_n=1[y_n<T_n]` once T_n<1. Then

`x_n=y_n-T_n+j_n`.

If `a_n=floor(16y_(n-1))` is the completed hexadecimal digit, the source
recurrence and `T_n=16T_(n-1)-r(n)` give the exact identity

\[
c_n=a_n+16j_{n-1}-j_n.                              \tag{CCV5c}
\]

Normality implies `A^-1 #{n in [A,2A): y_n<epsilon}->epsilon` for each
fixed epsilon>0. As T_n->0, the upper density of `j_n=1` is at most epsilon
for every epsilon, hence zero. Thus d_n=a_n except on a density-zero set;
for fixed k their words also agree outside density zero. The circle phase
error satisfies `|e(hx_n)-e(hy_n)|<=2pi|h|T_n` even across the coordinate cut.
For literal carry words, exclude also the preceding j-event at each index
in CCV5c. This is still a finite union of density-zero sets and proves the
literal-table extension with the same limiting reference averages.

Normality of alpha means y_(n-k) is equidistributed. The finite partition
`floor(16^k y_(n-k))=w`, followed by `y_n={16^k y_(n-k)}`, therefore gives
the product of uniform word measure and Haar future circle. Its test
functions have only finitely many discontinuities. In particular, uniformly
over the finite set of words,

`freq(w_n=w)->16^-k`,
`mean 1[w_n=w] e(hx_n)->0`.

Expanding the square proves CCV5a, uniformly for bounded table entries.
For an arbitrary finite actual sample, let p_w be its cell weights and m_w
its conditional phase means. The exact projection identity is

`mean |f-g(w)|^2 = 1-sum_w p_w |m_w|^2`
`+sum_w p_w |g(w)-m_w|^2`.

The second summand is the mismatch of the transferred table to the current
sample, not its training error. The empirical L2 optimum in each occupied
cell is m_w; these means tend to zero, proving the optimal-risk statement. For L1,
`|z-g|>=Re[conjugate(z)(z-g)]=1-Re[conjugate(z)g]` for |z|=1.
It suffices to optimize over |g(w)|<=2, since replacing any entry of
modulus>2 by 0 strictly decreases every distance in its cell. The finite
conditional means tending to zero now gives the uniform L1 lower bound.
QED.

This strengthens the interpretation of the old Haar-seed baseline
[HS8–HS12](../../../2026-11-05/history_shell/PROOFS.md): it concerns
one normal selected trajectory, uses the original forcing's literal carries,
and states an asymptotic prediction-risk obstruction. It does not import
an ensemble conclusion into seed zero.

**Folding caveat.** CCV5 does not supply a lower bound on the norm of a
q-replica folded residual at growing prime-order lags. Exactly,

`mean_r |q^-1 sum_j e_(j,r)|^2`
`=q^-2 sum_j mean_r|e_(j,r)|^2`
`+2q^-2 sum_(j<l) Re mean_r e_(j,r) conjugate(e_(l,r))`.

Those cross terms can cancel. Fixed-frequency normality alone does not
control these growing lags, as the existing RE4 countermodel proves. The
new obstruction is for raw fixed-depth prediction; it must not be falsely
applied to every folded model.

## CCV6. Literal carry16 has an explicit source-paid correction

For a late literal-carry table `g:{0,...,16}^k->C`, put G=||g||_infinity
and let g0 be its restriction to ordinary words `{0,...,15}^k`. Use g0
in CCV1's reference compiler and the residue path w_n. If v_n denotes the
literal carry word, then the exact additional term is

\[
\Xi=\frac1N\sum_n[g(v_n)-g_0(w_n)],\qquad
\operatorname{mean}g(v_n)=\mu+E_\psi+D_\psi+\Xi.      \tag{CCV6}
\]

Only words containing a literal16 contribute. If J counts such exceptional
carry indices in the relevant history range, at most kJ words change, so
`|Xi|<=2G kJ/N`. This is a representation correction, not the desired
phase-cancellation estimate.

For the actual original-forcing epoch `[A,2A)`, assume `k<=A-1` so all
relevant transitions have index at least2. A literal16 implies a positive
spill in the inherited **SBA-1/2** theorem. Therefore

\[
|\Xi|\le \frac{2Gk}{A}\,\mathcal K_{2A,1}
=O(Gk/\log A),
\]

where the explicit integer upper bound `mathcal K` is
[`spill_count_upper(2*A)`](../../../../observational_succ/selected_branch_arithmetic.py),
with its complete [source proof](../../../2026-10-26/SELECTED_BRANCH_ARITHMETIC.md).
For bounded G and `k=o(log A)`, this correction vanishes unconditionally.
The inherited gap argument uses the four-pole forcing but also holds for
other seeds with that forcing; it is not a new zero-seed selection theorem.

CCV3–4 apply to the literal predictor by retaining Xi in the model mean and
using residual `f_n-g(v_n)`. Replacing a17-symbol literal table by a16-symbol
reference table without this term would be an accounting error. This finite
observer transport is a paid proof step even though Dpsi and residual signed
covariance remain unpaid.

## CCV7. A causal retrodictive model pays its signed residual unconditionally

This model reads the last k carries to reconstruct a **past** phase. It is
not a successful current-phase predictor and does not contradict CCV5.
It is analytically specified, with no fitted coefficients or holdout input.
Use an original epoch `[A,2A)`, `1<=k<=A-1`, q=16^k, and define

\[
K_n=\sum_{j=1}^k16^{k-j}c_{n-k+j},\qquad
K_n^0=\sum_{j=1}^k16^{k-j}d_{n-k+j},
\]

\[
g_k(v_n)=e\bigl(h(K_n+1/2)/q\bigr),
\]

Here v_n is the literal word and the reference operator is CCV1-L on
Splus, not a projection modulo16. The reference mean mu is zero whenever
q does not divide h; in particular when q>|h|. The reference Poisson
potential satisfies `||psi||_infinity<=k`.
Equivalently, CCV1-Q implements this exact same model and potential on the
q integer-lift residues, since `K_n=C_n-q C_(n-k)` and
`g_k=e(h(C_n+1/2)/q)`. The carry16 information is propagated into the next
higher position before reduction. No exceptional-set estimate is needed.
For the authenticated source, put

\[
\epsilon_A=\pi|h|16^{-k}+\frac{\pi|h|}{32(A-k)^2}.
\]

Then the signed residual has the **unconditional source bound**

\[
\left|\frac1A\sum_{n=A}^{2A-1}[f_n-g_k(v_n)]\right|
\le\frac{2k}A+\epsilon_A.                   \tag{CCV7a}
\]

For every `1<=H<=A`, its padded-window certificate also satisfies

\[
\sqrt{V_H(f-g_k)}\le
\frac{2k}{H}\left(1+\frac{H-1}A\right)
+\sqrt{1+\frac{H-1}A}\,\epsilon_A. \tag{CCV7b}
\]

**Proof of source retrodiction and constants.** Let

`F_n=sum_(j=1)^k 16^(k-j) r(n-k+j)`.

Iterating the exact *fractional* source recurrence, with literal carries
preserved, gives

`x_n=16^k x_(n-k)+F_n-K_n`.

Consequently the literal-carry midpoint phase
`g_literal=e(h(K_n+1/2)/q)` differs from f_(n-k) by at most

`pi |h|/q + 2pi |h| F_n/q`.

By the authenticated source bound from SBA-1,

\[
\frac{F_n}{q}
=\sum_{j=1}^k16^{-j}r(n-k+j)
<\frac{15}{64(n-k)^2}\sum_{j=1}^k16^{-j}
<\frac1{64(A-k)^2}.
\]

This proves the epsilon_A bound without discarding any integer carry.
Put `delta_n=f_(n-k)-g_k(v_n)`. Its pointwise modulus is at most epsilon_A.
Write `f_n-g_k(v_n)=(f_n-f_(n-k))+delta_n`. The mean of the temporal
difference has at most2k uncancelled unit terms, proving CCV7a.

For CCV7b use the exact padded-window Gram norm in CCV3. The sum of
`f_n-f_(n-k)` over ANY contiguous subinterval of the epoch has at most2k
uncancelled unit terms, even for the truncated boundary windows. There are
A+H-1 windows, so their contribution to sqrt(V_H) is at most
`(2k/H)(1+(H-1)/A)`. Convolution by the H-entry indicator has L2 operator
norm at most H: Cauchy–Schwarz within each window and counting every entry
H times proves this directly. The delta contribution is therefore at most
`sqrt(1+(H-1)/A)*sqrt(mean|delta|^2)`. The triangle inequality in the window
Hilbert space proves CCV7b. QED.

If `k_A->infinity`, `k_A/H_A->0`, and `H_A=o(A)`, both
the direct signed residual and the displayed VdC bound tend to zero for
every fixed h. For example, eventually
`k_A=floor(log(log A))`, `H_A=floor(sqrt A)` meet these requirements.
The uniform reference mean is exactly zero once16^k>|h|, and the Poisson
endpoint term tends to zero. **These are paid source-dependent terms.**

### Exact residual debt: Dpsi is now a carry encoding of Weyl

When16^k does not divide h, combining CCV2, mu=0 and CCV7a gives the
stronger comparison

\[
\boxed{|W_A(h;0)-D_{\psi_k,A}|
\le\frac{4k}A+\epsilon_A.}                 \tag{CCV7c}
\]

Thus whenever k_A->infinity and k_A=o(A), the remaining statement
`D_(psi_k,A)->0` is **equivalent to the original fixed-h Weyl gate**.
The source-derived representation now has a proved small signed residual;
this is a concrete proof step, but it has not reduced the outstanding
asymptotic arithmetic claim. Merely computing or learning Dpsi does not
prove its decay. The compressed reference-table growth16^k is only a power of log A for the
suggested k, but finite representation size does not bound its empirical
occupation contrast.

An explicit economical rate is obtained without an ineffective threshold.
For `A>=2`, let k be the least integer with16^k>=A. Then
`1<=k<A`, `A<=16^k<16A`, and for `A>|h|` the reference mean is zero.
CCV7c gives the completely explicit estimate

\[
|W_A-D_{\psi_k,A}|\le
\frac{4\lceil\log_{16}A\rceil+\pi|h|}{A}
+\frac{\pi|h|}{32(A-\lceil\log_{16}A\rceil)^2}
=O_h(\log A/A).                                     \tag{CCV7d}
\]

The exact observer uses4k bits and fewer than16A states. This bounds the
source-to-observer error at every such epoch; it does not bound the
observer's remaining signed mean. The exponentially fading innovation
series in the separate crucible appendix can add an O_h(1/A) finite-to-limit
error at this same k, with its own uniformly proved tail bound.

The distinction from canonical QCO5 compression is precise. g_k is a
causal carry rule fixed independently of observed phase values, so it is
not a linear equivariant analysis of the held-out f-vector. Nevertheless
CCV7c proves a different and explicit equivalence: its one surviving
source occupation contrast retains the full target to a vanishing error.
There is no claim that bypassing QCO5 automatically bypasses circularity.

The same-forcing coherent seed and eventually periodic completed points
remain hostile controls. The local spill argument and retrodictive algebra
also hold there; consequently Dpsi can tend to a unit phase. These controls
do not have the original zero boundary. Excluding them requires exactly
the missing source selection estimate, not another retrodictive identity.
For the coherent seed `s*=-pi/16`, the sharper exact receipt is
`U_n=-T_n`, `C_n=-1`, and `c_(n+1)=15`. Hence its compressed state is
`q-1`, a fixed point under the actual update, and for q not dividing h

`Dpsi=g_k(q-1)=e(-h/(2q))`, of modulus exactly1.

All retrodictive error estimates hold while this retained signal survives.
This is not a rational-principal-part countermodel: its unwrapped states
are irrational, and the exact original zero boundary rejects it.

### Optional residue-memory version

One may instead use `g_k^0(w_n)=e(h(K_n^0+1/2)/q)` and the original16-symbol
kernel. For this different model let
`beta_A=min(1,k mathcal K_(2A,1)/A)`. At most beta_A of the words contain a
literal16, so the L1 and L2 differences between literal and residue model
values are at most2 beta_A and2 sqrt(beta_A). Therefore CCV7a and CCV7c
acquire an extra2 beta_A, and CCV7b's epsilon term becomes
`epsilon_A+2 sqrt(beta_A)`. These bounds vanish at k=o(log A). The loss is
an optional memory projection cost; it is not necessary in the literal
transient-state representation.

## Hostile controls and surviving claim

* Same-forcing coherent seed `s*=-pi/16` has `f_n=e(-hT_n)->1`. If a proposed
  model satisfies `mu+boundary+Dpsi->0`, its residual mean tends to 1 and
  CCV3 forces `liminf V_H>=1`. Thus neither the carry model nor its reference
  transition kernel can certify false cancellation by itself.
* A periodic completed orbit `alpha=j/(16^p-1)` is a separate same-forcing
  control. At h=16^p-1 its full phases tend to 1. All nonzero frequencies
  in the normality gate are essential. These are completed points, not the
  unrelated seed 1/5.
* Deterministic alternating carries can have Dpsi=0 and maximal conditional
  row bias. This is allowed: the premise controls one signed observable.
  Dropping residual covariance would falsely certify arbitrary assigned f=1.
* Replacing g by an oracle fitted to current f can make residuals small;
  the mu/Dpsi costs retain the actual mean. Centering g is not free, because
  it shifts that same amount into the residual.
* Independent observer phase rotations break the complex identities unless
  f, g and psi are transported in the same frame. Magnitudes alone cannot
  reconstruct the signed mixed terms in CCV3c.

The next arithmetic task is to bound the original-zero **signed occupation
contrast Dpsi and innovation lag average jointly**, for a preregistered
family whose reference mean and boundary costs are small. This is a more
appropriate target than making bounded-memory past predictions exact.

**Pi base16 normality: OPEN. RH: OPEN.**
