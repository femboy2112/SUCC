# Coherent frames, permanent local locking, and finite causal slices

**Date:** 2026-11-19. **Status:** paper deductions within the literal BBP source
contract; no claim of academic priority or of a new signed statistical estimate.
The exact constructions below implement the owner's correction: a local observer
may remain locked while its retained relation to the source frame carries motion.
R0 and base-16 normality of pi remain **OPEN**.

## FA-01. The two coordinates and their actual agreement law

For every integer `n >= 1`, retain

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_{n+1}=16U_n+r(n+1).
\]

Write `e(t)=exp(2*pi*i*t)`, with `t` measured in turns, and set

\[
x=\sum_{j\ge1}16^{-j}r(j)=\pi/16,\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad Y_n=16^nx=U_n+T_n.
\]

The source identity, positive decreasing forcing, and bound
`0 < T_n < r(n+1)/15` are inherited from the authenticated source, as recorded in
[`docs/PI_NORMALITY_FRONTIER.md`](../../../../docs/PI_NORMALITY_FRONTIER.md).
They are not inferred from the new observer.

The canonical moving coordinates are `(c_n,v_n)=(U_n,T_n)`. Their exact update is

\[
F_n(c,v)=(16c+r(n+1),\;16v-r(n+1)).
\]

Addition `a(c,v)=c+v` satisfies

\[
a\circ F_n=16a,\qquad
Da=(1\;1),\qquad Da\,DF_n=16Da.
\]

Thus the two compensating source terms cancel in the objective coordinate. The
ambient two-coordinate derivative is `16 I_2`; its determinant is not a claim of
two independent degrees of freedom on the selected source trajectory. The kernel
of `Da` consists of simultaneous changes `(delta,-delta)`.

More generally, for any real sequence of chart origins `c_n`, define

\[
v_n=Y_n-c_n,\qquad b_n=c_{n+1}-16c_n.
\]

Then `v_(n+1)=16v_n-b_n`. Replacing the chart by `c'_n=c_n+d_n` changes
`v'_n=v_n-d_n` and `b'_n=b_n+d_(n+1)-16d_n`. Keeping the old compensation after
an arbitrary moving change of chart would be a different, generally false model.
These are exact real-lift identities before reduction modulo one.

**Proof.** Substitute the definitions into the recurrence and the addition map.
The Jacobian identity is its derivative. No limiting or statistical assertion is
used. **Verdict:** PROVED LOCAL; next falsifier is an omitted compensation term.

## FA-02. An expanding Jacobian and an indefinitely locked local display coexist

The recurrence

\[
v_{n+1}=16v_n-r(n+1)
\]

has exactly one forward-bounded real solution: `v_n=T_n`. Every other solution is
`T_n+16^n a` for a nonzero real constant `a`, and is unbounded. Meanwhile `T_n`
tends to zero. Hence an expanding scalar Jacobian `16` does not prevent a
particular authenticated local coordinate from converging to a fixed display.

**Proof.** The tail definition gives the stated recurrence. The difference of any
two solutions is multiplied by sixteen at every step. The original tail is
bounded and tends to zero; the nonzero homogeneous difference is unbounded.

For any fixed display cell `[0,epsilon)` of positive width, the completed local
coordinate eventually remains in that cell forever. There is also an exactly
locked, completely causal rational display: the observer computes `U_n` from its
source journal and displays `U_n-U_n=0` at every time. Its estimate of the completed
source phase is `e(h U_n)`, with the positive tail paid as an error.

The finite display is not the observer's entire memory. At every finite time the
source journal and integer state are finite objects, but their sizes may grow.
A theorem about a fixed finite-state machine cannot silently be applied to this
observer with growing integer registers. Conversely, a display which discards
the journal cannot claim that it still authenticates the full causal history.

**Verdict:** permanent local locking is compatible with the literal source.
What remains open is the compensated signed chronological estimate, not the
impossibility of every locally locked view.

## FA-03. The analytic boundary condition has finite rational realizations

For each finite horizon `M >= 0`, impose the terminal local condition
`v_(M|M)=0`, and define for `0 <= n <= M`

\[
v_{n\mid M}=\sum_{j=n+1}^{M}16^{n-j}r(j),\qquad
q_{n\mid M}=U_n+v_{n\mid M}=16^{n-M}U_M.
\]

All these numbers are rational, constructed from the source prefix through `M`.
They satisfy exactly

\[
v_{n+1\mid M}=16v_{n\mid M}-r(n+1),\qquad
q_{n+1\mid M}=16q_{n\mid M},
\]

and the refinement identities

\[
v_{n\mid M+1}-v_{n\mid M}
=q_{n\mid M+1}-q_{n\mid M}
=16^{n-M-1}r(M+1).
\]

Their exact completion defect is

\[
\boxed{Y_n-q_{n\mid M}=T_n-v_{n\mid M}=16^{n-M}T_M.}
\]

In particular, `v_(0|M)=P_M` tends to `x`, and

\[
\max_{0\le n\le M}|Y_n-q_{n\mid M}|=T_M
<r(M+1)/15\longrightarrow0.
\]

**Proof.** Expand `U_M` with the affine recurrence and split the finite sum at
`n`. Splitting the infinite tail at `M-n` gives the completion defect. The
maximum follows because `16^(n-M) <= 1`, with equality at `n=M`.

The backward expression is postprocessing of information acquired by horizon
`M`, not a claim that the physical source clock runs backward. The endpoint is
selected by a precise analytic boundary condition (absence of the growing
homogeneous mode); every finite boundary problem has a source-rational solution.
The classical BBP evaluation identifies the resulting endpoint with `pi/16`.

This establishes finite-slice/source-frame agreement. Agreement by itself does
not prescribe the empirical distribution of the completed phases.

## FA-04. A finite five-channel anchor, with no completed-real oracle

Declare the four-pole counterfactual family

\[
r_{\mathbf c}(j)=\sum_{a=1}^{4}\frac{c_a}{8j-d_a},
\qquad (d_1,d_2,d_3,d_4)=(7,4,3,2),\qquad U_0(\mathbf c,s)=s.
\]

The selected member is `c=(4,-2,-1,-1), s=0`. At a finite horizon `M`, choose four
distinct positive integer probe times `t_i <= M` and write

\[
C_{ia}=\frac1{8t_i-d_a},\qquad
P_M(\mathbf c)=\sum_{j=1}^{M}16^{-j}r_{\mathbf c}(j).
\]

A genuinely finite observer is

\[
\mathcal O_M(\mathbf c,s)=
\left(r_{\mathbf c}(t_1),\ldots,r_{\mathbf c}(t_4),
16^{-M}U_M(\mathbf c,s)\right).
\]

Its Jacobian in variables `(c_1,c_2,c_3,c_4,s)` is

\[
D\mathcal O_M=
\begin{pmatrix}C&0\\
\nabla_{\mathbf c}P_M&1\end{pmatrix},
\qquad\det D\mathcal O_M=\det C\ne0.
\]

The Cauchy determinant is nonzero because the four probe times and the four poles
are separately distinct and no denominator vanishes. The inverse recovers

\[
\mathbf c=C^{-1}(\text{four innovations}),\qquad
s=16^{-M}U_M-P_M(\mathbf c).
\]

Using `U_M` without normalization multiplies the determinant by `16^M`. Wrapping
the normalized anchor modulo one aliases seeds differing by an integer. Wrapping
the unnormalized state `U_M` aliases the finer seed shifts `k/16^M`, because
`U_M+k` has the same fractional part. Either replacement loses exact seed
authentication. Full integer winding is part of the contract.

The limit `s+x(c)` is not an additional measured input. It is the completion of
the fifth finite coordinate with the appropriate source-tail bound. The stated
positive BBP tail bound applies to the selected coefficient vector, not
automatically to every counterfactual vector.

This five-parameter inverse problem is distinct from the five quartic Fibonacci
readouts of a two-dimensional state. A nonzero Jacobian of this source/seed
identification map does not assert five independent physical degrees of freedom
or a probability law on parameters. With the literal source and seed already
known, it is a sensitivity and authentication instrument.

## FA-05. Quantitative transport of fixed signed probes

Fix `h` in `Z \ {0}` and let

\[
W_B(h)=\frac1B\sum_{n=B}^{2B-1}e(hY_n).
\]

For every moving chart, the exact observable is the compensated product

\[
e(hY_n)=e(hc_n)e(hv_n).
\]

It is invariant under the paired change `c_n -> c_n+d_n`,
`v_n -> v_n-d_n`. Neither factor's chronological mean is invariant by itself.
Products must be formed before averaging; multiplying separate mean factors
would discard their source-selected dependence.

Suppose a finite realization supplies real lifted estimates `c_hat_n, v_hat_n`
with `|(c_hat_n+v_hat_n)-Y_n| <= delta_n`. Then

\[
\left|W_B(h)-\frac1B\sum_{n=B}^{2B-1}
e(h\widehat c_n)e(h\widehat v_n)\right|
\le\frac{2\pi|h|}{B}\sum_{n=B}^{2B-1}\delta_n.
\]

**Proof.** Use `|e(a)-e(b)| <= 2*pi*|a-b|` at every term and then the triangle
inequality. A certified circle-distance bound can replace the real lifted bound
for this single character; it cannot replace integer winding for seed recovery
or subsequent division by powers of sixteen.

Two entirely explicit realizations follow.

### Same-time causal observation

Choose `c_hat_n=U_n, v_hat_n=0`. Then

\[
\left|W_B(h)-\frac1B\sum_{n=B}^{2B-1}e(hU_n)\right|
<\frac{2\pi|h|}{15}r(B+1).
\]

This is a uniform shell error tending to zero. The local displayed coordinate
is exactly zero throughout this computation.

### One terminal source slice

At any horizon `M >= 2B`, form `q_(n|M)=U_M/16^(M-n)` and let

\[
W_B^{[M]}(h)=\frac1B\sum_{n=B}^{2B-1}e(hq_{n\mid M}).
\]

The exact geometric sum gives

\[
\begin{split}
|W_B(h)-W_B^{[M]}(h)|
&\le\frac{2\pi|h|T_M}{B}\,
\frac{16^{B-M}(16^B-1)}{15}\\
&<\frac{2\pi|h|r(M+1)}{225B}\,16^{2B-M}.
\end{split}
\]

In particular, at `M=2B` let

\[
\widehat W_B(h)=\frac1B\sum_{k=1}^{B}e(hU_{2B}/16^k).
\]

FA-03 gives the sharper bound

\[
\boxed{|W_B(h)-\widehat W_B(h)|
\le\frac{2\pi|h|T_{2B}}{15B}(1-16^{-B})
<\frac{2\pi|h|}{225B}r(2B+1).}
\]

Here the inequality uses the exact geometric sum
`sum_(k=1)^B 16^(-k)=(1-16^(-B))/15`. Since the authentic forcing is `O(n^-2)`,
the last error is `O_h(B^-3)`. This terminal readout and its source-tail logic
are inherited interfaces from the existing terminal-observer program, now
attached explicitly to the five-channel frame contract; they are not presented
as newly discovered normality criteria.

If a reconstructed terminal real lift has error `Delta_B`, the same calculation
adds at most `2*pi*|h|*Delta_B/(15B)`. This statement needs the real lift:
retaining only `U_(2B) mod 1` does not control `Delta_B` and does not justify the
bound. With source authentication and complete winding, even bounded terminal
rounding error has a vanishing averaged effect. It does not make the terminal
integer's digits known or statistically balanced.

### Frequency range and extra source depth

For an explicitly declared frequency range `1 <= |h| <= H_B`, and a desired
positive error `epsilon_B`, an extra source horizon `L_B >= 0` with

\[
16^{L_B}\ge
\frac{8H_B\,r(2B+1)}{225B\,\epsilon_B}
\]

is sufficient at `M=2B+L_B`. The proof uses monotonicity of `r`, the general
bound above, and `2*pi < 8`; choose `L_B=0` when the displayed right side is
at most one. This avoids using an uncertified numerical value of pi in the
precision rule. For polynomial frequency growth and inverse-polynomial error,
`L_B=O(log B)` suffices. This is an approximation-depth statement, not a
cancellation theorem uniform in those growing frequencies.

Additional terminal reconstruction error has a separate cost. If the lifted
terminal estimate at this general `M` is accurate to `Delta_M`, replace `T_M`
by `T_M+Delta_M` in the first bound. Prime-resolution repair must certify this
lifted error, or recover the terminal rational exactly. A modular phase alone
does not do so. The extra horizon and its source samples are charged as latency:
the observer reports the earlier shell after those samples have arrived.

### Locking transfer

If a local coordinate approaches a constant in the averaged circle sense,

\[
\frac1B\sum_{n=B}^{2B-1}\|v_n-\theta\|_{\mathbb T}\longrightarrow0,
\]

then for each fixed `h`

\[
W_B(h)-e(h\theta)\frac1B\sum_{n=B}^{2B-1}e(hc_n)\longrightarrow0.
\]

The proof is the same Lipschitz estimate. Locking transfers the statistical
burden to the retained chart origin; it does not remove it. In the canonical
chart, `theta=0` and `c_n=U_n`.

## FA-06. Adaptive precision is allowed; silently changing the time measure is not

Prime depth, source-probe times, and reconstruction precision may adapt to the
retained history. For signed Weyl reports, fix the frequency `h`, chronological
shell, normalizing count, and interpretation of unresolved observations before
inspecting the signed result. Store the actual source time of every advance.
The literal source index and an internal computational waiting/acceptance index
need not be the same clock.

The following finite identity states the exact cost of skipped source times.
For a subset `A` of the `B` chronological indices with size `m>0`, define
`W_A=(1/m) sum_(n in A) z_n`, where `|z_n|=1`. Then

\[
W_B=\frac mB W_A+\frac1B\sum_{n\notin A}z_n,\qquad
|W_B-W_A|\le2(1-m/B).
\]

Consequently:

- To transfer `W_A -> 0` without controlling the complement, require
  `m/B -> 1`. A fixed positive accepted fraction is insufficient for full
  cancellation.
- For a one-sided R0 certificate, if `Re W_A <= 1-eta` and `m/B >= d>0`, then
  `Re W_B <= 1-d*eta`. A positive accepted density can suffice when its density
  and its signed gap are themselves proved on every late shell.
- If reconstruction succeeds only on `A`, its certified average phase error
  on accepted points must also be charged. With estimates of modulus at most
  one on the failed points, a conservative full-shell error is the accepted
  Lipschitz error plus `2(B-m)/B`.

**Proof.** Split the full sum over accepted and omitted indices. The first
inequality uses modulus at most one for both means. The R0 inequality uses
`Re z_n <= 1` on every omitted term. No probabilistic independence or optional
stopping assumption is used.

A concrete selection control: in a sequence alternating `+1,-1`, accepting
only `+1` produces reported mean one although the full even-length mean is zero.
Conversely, a sequence with a cancelling half and an all-`+1` half can have an
accepted mean zero and a full mean one half. A phase-dependent “go” criterion
cannot evade these exact accounting identities.

Adaptive prime repair should therefore refine the observer until the declared
reconstruction error is paid, while retaining every chronological term. A
rank repair is not a signed-result acceptance rule. Failure to resolve is an
explicit missing term with a charged weight, not evidence of cancellation.

## FA-07. The two limits and the remaining theorem

The finite-slice limit in FA-03 identifies the endpoint and the source orbit.
It is a limit in reconstruction depth. The empirical limit

\[
\frac1B\sum_{n=B}^{2B-1}\delta_{\{Y_n\}}
\]

is a limit in chronological sampling length. The former does not force the
latter to be Haar. FA-05 supplies sufficient uniform error control to transport
an independently established estimate across these limits; it does not supply
the estimate.

For example, the source-selected finite-slice premise

\[
\exists\eta>0,\ B_0:\quad
\Re\widehat W_B(1)\le1-\eta\quad\text{for every }B\ge B_0
\]

would yield R0 after paying the explicit vanishing error. The numerical margin
may be reduced, for example to `eta/2`, beyond a large enough horizon. For full
normality, the required premise is

\[
\forall h\in\mathbb Z\setminus\{0\}:\qquad
\widehat W_B(h)\longrightarrow0.
\]

These are transport targets, not newly proved bounds and not claims that an
equivalent restatement is an arithmetic advance. Finitely many fixed probes,
including `h=1`, are diagnostics for their stated modes. They do not establish
all-mode Weyl cancellation. A source-derived estimate must control the actual
signed phase/cofactor and integer-winding history of the original zero seed.

The geometric statement of the same boundary is useful. Form the joint empirical
law of `(c_n mod 1,v_n mod 1)`. Addition pushes it to the source-phase empirical
law. When `v_n -> 0`, every weak subsequential joint limit is supported on
`v=0`, but its `c` marginal can still be any surviving source-phase limit.
Replacing a time-dependent chart by one fixed pushforward would discard the
compensator and is unjustified.

## Crucible and claim boundaries

| Proposed inference | Receipt / valid scope | Verdict |
|---|---|---|
| Jacobian expansion forbids a locally locked authentic observer | `T_(n+1)=16T_n-r(n+1)` and `T_n -> 0`; the raw causal chart displays zero exactly | REFUTED |
| Retained moving-frame agreement survives at every finite horizon | FA-01 and FA-03 exact identities, with explicit completion defect | PROVED LOCAL |
| Four innovations plus a finite normalized state identify source coefficients and seed in the declared family | FA-04 Cauchy inverse, integer lift retained | PROVED LOCAL |
| A nonzero identification Jacobian proves normality | The Jacobian is independent of the selected seed; same forcing with `s=-x` has an identically zero completed orbit | REFUTED |
| Zero seed, shrinking local tail and coherent finite reconstruction force normality for arbitrary sources | The explicit rational endpoint control below has all three and an eventually locked completed orbit | REFUTED; this mutant is not the original four-pole source |
| Complete finite-slice agreement alone yields a uniform late-shell signed saving for pi | The missing inequality in FA-07 has not been derived | OPEN |
| Accepted-time cancellation implies chronological cancellation | FA-06 exact omitted-weight identity and the half-accepted counterexample | REFUTED without coverage/complement control |
| A fixed finite-state obstruction rules out all finite observers with growing memory | Their state spaces and resource quantifiers differ | No such inference is licensed |

The same-forcing wrong-seed control is rejected by the exact fifth-channel seed
test, but shows why Jacobian rank and coherent transport are insufficient by
themselves. The rational seed alias `s=1/16` can share all later completed circle
phases with the original while still failing exact zero-seed authentication.

A useful explicit boundary-condition control is

\[
\widetilde T_n=\frac1{64(n+1)^2},\qquad
\widetilde r(n)=\frac1{4n^2}-\frac1{64(n+1)^2},\qquad
\widetilde U_n=\frac{16^n}{64}-\widetilde T_n.
\]

It has literal zero seed, positive strictly decreasing forcing, the same leading
coefficients `r_tilde(n) ~ 15/(64n^2)` and `T_tilde(n) ~ 1/(64n^2)`, exact
finite-slice agreement, and the same expanding state Jacobian. Nevertheless its
endpoint is `1/64` and its completed phases are exactly one from `n=2` onward.
To verify positivity, use `16/n^2 > 1/(n+1)^2`; to verify decrease, differentiate
the real extension and use `32/n^3 > 2/(n+1)^3`. The recurrence follows directly
from `r_tilde(n)=16 T_tilde(n-1)-T_tilde(n)`, and weighted telescoping gives the
endpoint. This control changes the forcing and is not a counterexample to a
statement that genuinely uses the entire original four-pole source.

The existing factorial-sparse irrational and matched finite-source controls
remain necessary against claims based only on productivity, finitely many
reports, positivity, or infinitely recurring separation.

**Next discriminating obligation:** derive a uniform signed bound on the
compensated, chronologically weighted output of the literal source. The frame
construction now specifies exactly what data and approximation costs such a
bound must retain. Further rank improvements alone do not close that edge.
