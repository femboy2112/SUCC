# The selected-π categorical frontier

**Status:** research frontier map. **π base-16 normality: OPEN. RH: OPEN (separate program).**
This document is the single front-page statement of *exactly* what is proved, what is the
narrowest remaining open estimate, and how the categorical apparatus is meant to attack it.
It supersedes nothing in `docs/PI_FRONTIER_CONTRACT.md` and `docs/PI_GEARBOX_ATLAS.md`; it
narrows them to the current leading route (#304 selected-phase forge) and records the honest
limitations found under adversarial review.

No claim here promotes a modulus bound to a cancellation theorem, or positivity/formal
coherence to a signed asymptotic saving. Every load-bearing line carries its status.

## 0. The exact source contract (do not alter)

Single authentic BBP recurrence:

$$ r(n)=\frac{4}{8n-7}-\frac{2}{8n-4}-\frac{1}{8n-3}-\frac{1}{8n-2},\qquad U_0=0,\qquad U_{n+1}=16U_n+r(n+1). $$

All $U_n$ are unwrapped exact rationals; the real-circle observations are $x_n=\{U_n\}$.
Literal integer carries and the common forcing conductor belong to the source, not metadata.

**Reduction (proved, #293 / SGO-09).** For all $N\ge 1$ and $h\neq 0$,

$$ \left\lvert \sum_{n\le N} e\!\left(h\,16^{n-1}\pi\right) - \sum_{n\le N} e(hU_n)\right\rvert < \tfrac{119}{648}\,\lvert h\rvert . $$

Hence **π is base-16 normal $\iff$ $\widehat S_N(h)=\sum_{n\le N} e(hU_n)=o(N)$ for every fixed nonzero integer $h$.**
This is an elementary, $O_h(1)$ Weyl-level transport (hand-re-derived); it supplies the
*equivalence*, not any cancellation. The Gamma / signed-moment machinery on #293 is **not**
load-bearing for this bridge (SGO-12 is itself a no-go: summable amplitudes cannot create
$N$-scale cancellation).

## 1. What is proved on the leading route (#304)

**DC-1 — all-$N$ logarithmic absolute loss (paper-proved; hand-verified given $\mu(\pi)<15/2$).**
There exists an integer $J_0$ such that for all $N\ge 1$ and all $h\neq 0$,

$$ \left\lvert \sum_{n\le N} e(hU_n)\right\rvert \;\le\; N-\frac{1}{1250}\,\max\!\Big(0,\ \lfloor\log_8 N\rfloor-\max(J_0,\ \lceil\log_{64}\lvert h\rvert\rceil)\Big). $$

This is a **modulus upper bound**. The normalized upper bound tends to $1$. It is **not**
$S_N(h)=o(N)$ and the branch says so (`CLAIM_SUPPLEMENT_PI_SELECTED_PHASE.md`, PSF-14 OPEN).

- **Role of $\mu(\pi)$.** Enters only through DC-2 (existence of a rational $C\in(0,1]$ with
  $\lvert\pi-p/q\rvert\ge C q^{-15/2}$). The published input is $\mu(\pi)\le 7.103205334137$
  (Zeilberger–Zudilin, [arXiv:1912.06345v2](https://arxiv.org/abs/1912.06345v2)); only the
  exponent $<15/2$ is used. A tighter bound attributed to a 2026 Bai preprint in the prep
  handoff (not independently verified here) is **not** needed and must not silently replace the
  published input. Width-8 blocks are essential (width-4 fails the 15/2 margin).
- **$J_0$ is NOT effective.** Existence is proved; the numeric value is *not* extracted
  (`bbp_diophantine_coherence.py` `threshold_numerically_certified=False`;
  `PI_FRONTIER_CONTRACT.md`; `exact_receipt.json`). Any explicit-rate statement that cites a
  numeric $J_0$ is currently unsupported. ($C=1\Rightarrow J_0=2$ is a *conjecture*, uncertified.)
- **Lean.** `formal/SelectedPhase.lean` kernel-checks 8 finite scalar declarations only. The
  complex inverse argument, the Diophantine theorem, and normality are **not** in Lean.

## 2. The narrowed open gate (this is the whole game)

**October 26 staged improvement over DC-1 (after #310).** The
[integer-branch coercivity proof](../research/2026-10-26/OILY_DIRECT_ARITHMETIC.md)
improves the absolute block loss from `1/1250` to `1/29`. There exists one
unspecified integer `J_1` such that, for all `N>=1` and all nonzero integer `h`,

$$
|S_N^U(h)|\le N-\frac1{29}\max\left(0,\lfloor\log_8N\rfloor-
\max(J_1,1+\lceil\log_{64}|h|\rceil)\right).
$$

The new finite argument charges different integer branches to total squared
phase error through the adjacent coefficient norm `546=16²+17²+1`.
It retains the authentic zero selector and the published irrationality input.
At fixed frequency the logarithmic coefficient is larger by `1250/29`;
the onset is not numerically extracted and differs from the prior theorem's.
This is **a constant improvement only**. The normalized upper bound still
tends to one, and the gate below remains open. Nine finite Lean declarations
cover quadratic/rational steps; they do not formalize the analytic theorem.

On the **derived flat-carry signal** $b_t=c_t\,\mathbf 1_{\{Q_t=Q_{t-1}\}}$ with

$$ H_N=\max\!\big(2,\,1+\lfloor\sqrt{\lfloor\log_2 N\rfloor^{3}}\rfloor\big),\qquad J_N=\min\{J:16^J\ge N H_N^2\}, $$

prove for the unique original-source orbit

$$ 2\sum_{h=1}^{H_N-1}\Big(1-\tfrac{h}{H_N}\Big)\left\lvert\frac1N\sum_{n\le N} e\!\Big(h\sum_{j=1}^{J_N}16^{-j}b_{n+j}\Big)\right\rvert^{2}=o(1). $$

Confirmed to match the code (`bbp_sparse_carry_transport.py`). Under the branch's paid
transport lemmas (SCT-1…4, SP-I4) this is **equivalent** to the selected low-frequency
compression target; it is **not** a consequence of formal coherence. Proving it (uniformly in
$h<H_N$, which is *stronger* than fixed-$h$ Weyl) implies normality via transport $+$ Weyl.

## 3. Honest limitations (found under adversarial review — preserve these)

1. **The sparse-carry transport budget is asymptotic-only and numerically vacuous at every
   finite $N$ in the receipt.** `mode_error_upper` $=6.13/3.88/1.25$ at $N=2^{16},2^{64},2^{256}$
   (each $>1$; a single normalized mode is $\le 1$); `root_energy_error^2_upper`$=6420$ at
   $N=2^{256}$, above the trivial maximum $H_N-1=4096$. The result "removes all conductor-birth
   carries" is a true statement about $N\to\infty$ with **no usable finite-$N$ content**, and
   the slow $t^{-1/4}$ rate means the gate cannot be numerically corroborated at any accessible
   $N$. (This vacuity was not previously stated in the dossier; it is recorded here.)
2. **The Walsh-energy "obstruction" is generic.** It is a fact about *any* $N$-point multiset
   in $\mathbb Z/M$ (Parseval: $\sum_{s\neq0}\omega_s^2\ge M/N-1\ge H^2-1$), using **no π data**.
   It rules out one strategy (global Walsh smallness at this conductor schedule); it is **not**
   evidence against the gate (the gate uses $h<H_N$ Fourier modes — a different character set)
   and gives no smallness criterion.
3. **Structural ceiling of the earlier coordinatewise method.** The DC-5 finite inverse lemma requires
   $34a+\lvert h\rvert\cdot(\text{range }r)<1$, forcing $a<1/34$, so it only controls an
   *absolute* block loss $\le 8a^2<2/289$, independent of block length. This cannot yield
   $o(N)$ by additive block bounds. Even a fixed relative loss is insufficient (§3.5);
   an additional signed or cumulative estimate has to be proved.
   The post-#310 total-energy argument above escapes this coordinatewise ceiling
   and raises the block loss to `1/29`; it still controls only constant absolute
   loss on each growing block, so the order-of-growth obstruction survives.
4. **Diophantine input alone cannot suffice (Control C).** $\xi=\sum 16^{-2^k}$ has irrationality
   exponent $2$ yet Fourier sums $N+O_h(\log N)$. Any extension must use the zero anchor $U_0=0$
   and the actual source, not just an irrationality bound.
5. **A fixed positive-proportion relative block loss is insufficient (Main XII, SK2-A1, proved).**
   For every fixed $c\in(0,1)$ and every positive-density set of width-8 blocks,
   $|S_B(h)|\le(1-c)|B|$ gives by the triangle inequality only $|S_N(h)|\le(1-c')N$ (linear) and
   permits the §2 upper envelope $(1-c)^2(H_N-1)=\Theta(H_N)$, rather than proving it small.
   For a uniform mode bound $|A_N(h)|\le1-c_N$, sufficiency requires the stronger rate
   $H_N(1-c_N)^2\to0$; merely $c_N\to1$ does not suffice for the growing-band gate.
   A genuine signed or multiscale estimate must supply this saving. The DC-5 single-step
   lemma is moreover capped at $a<1/34$ with an
   *absolute* loss $<2/289$ (SK2-A2); escape needs the joint phase across $\ge2$ consecutive
   $\times16$ steps.
6. **The occupancy baseline is not the gate (Main XII, SK2-TRAP, proved).** The rational
   $(\mathrm{purity}.\mathrm{coefficient}(0)-H)/H=(H-1)/N$ from the window compression is
   phase-*blind* (identical for the authentic orbit and the non-normal $\xi=\sum16^{-2^k}$); it is
   **not** the §2 Weyl statistic (which is the *evaluated* complex quantity and separates the
   authentic orbit from counterfeits). A rational "$R^2$" read off a coefficient is the collision
   baseline, never the gate. See `observational_succ/signed_pushforward.py`.
7. **The proposed raw frequency ladder is a time shift (October 26 audit).** At fixed $h$,
   $A_N(16h)-A_N(h)=O_h(1/N)$ for the authentic source; an explicit moving-band bound is
   $(2+\sqrt{105|h|/8})/N$. Thus a uniform ratio below one already implies bounded
   unnormalized sums. For fixed $N$, the literal unbounded-$h$ ratio target is false:
   multiples of the exact common denominator make both averages equal to one.
   See `observational_succ/ladder_shift_audit.py` and the source-bridge dossier below.
8. **Even frequencies retain cross-digit high-order terms (October 26 audit).** Vanishing of
   the top Walsh coefficient of one digit does not remove the fourth-order terms of a
   multi-digit word. The exact two-digit law with parity constraint on bits $\{0,4,5,6\}$
   has all joint marginals of order at most three uniform, and both complete digit
   marginals uniform, but a nonzero Fourier coefficient at $h=2$. The earlier
   marginal-only even-band shortcut is refuted; additional source-time joint laws are needed.

The new [logarithmic source bridge](../research/2026-10-26/OILY_MACARONI_SOURCE_BRIDGE.md)
proves exact Gamma-mixture and BBP/Euler error comparisons. It supplies no selected
signed saving. A source-relative log phase has harmonic mean drift but only a summable
$O_t(n^{-2})$ coherence loss. A changing frequency `t_n=16 pi k n` does give auxiliary
circle cancellation `Theta_n(k)=O_k(1/n)` with an explicit leading coefficient, using
the exact uniform-unit-cell factor of the source. A rational nonnormal uniform-cell
control matches the first two moments AND this auxiliary cancellation. The DC-1
modulus frontier remains unchanged.

The [four-pole atomic continuation](../research/2026-10-26/FOUR_POLE_ATOMIC_SUBSTRATE.md)
now supplies two rational quadratic coefficient atoms, their exact signed eight-step
return, a global Mobius mirror, and positive binary polynomial layers with the sharp
uniform relative defect `rho_M=(M+2)/2^(M+1)`. These are a finite realization of the
source kernel with an explicit approximation budget. Four-dimensional minimality
applies to the kernel's coefficient sequence, not to the arithmetic tail sequence.
The endpoint layer PGF `G(z)=1/(2-z)^2` selects `q*=lambda^2`, giving the exact graded
offset `E log Y_n-q*=(lambda-gamma)-eta_n`. Pairing layers changes q*; even changing
only the first two packets changes q* while preserving every approximation of depth
at least two. Thus this construction derives the golden reference for the specified
packet law, and refutes its invariance under forgetting that law. Its authentic endpoint
joint law is independent in the limit; a Gamma-Poisson coupling with the same marginals
is a different model. None of these results pays the selected signed estimate.

## 4. How the categorical apparatus must serve §2 (not replace it)

Category theory here **predicts an obligation or an obstruction** for the §2 estimate; it does
not certify it. The load-bearing constructions (see `docs/CATEGORICAL_OBSERVER_ATLAS.md`) are:

- **Signed-interference pushforward (first-class proof obligation, not an automatic zero).**
  Under a partition coarsening $f$, $z'=P_f z$ and $K'=P_fKP_f^{*}$ with
  $K_{a,b}=z_a\overline{z_b}$. This retains the cross-stratum signs that positive conditional
  energies hide. The *missing signed term* is the typed obligation whose vanishing (in the
  low-frequency band) is exactly §2 — never assumed from positivity.
  **Discharged (Main XII, SK2-B/SK2-D) as a NEGATIVE theorem:** $K\mapsto P_fKP_f^{*}$ is an exact
  coarsening-*invariant* base change ($|S_N(h)|^2=\sum_A|S_A|^2+\sum_{A\neq B}S_A\overline{S_B}$ is
  conserved), so it is gate-conservative and positivity-blind; the authentic cross term is
  sign-indefinite. The *one* genuinely new (classical) product is a firewall sharpening: signed
  amplitude base change holds for every amplitude **iff the square is cartesian** (Mackey);
  ghost/realization-faithfulness is necessary but **not** sufficient (the redundant-realizer square
  passes the ghost firewall yet breaks signed transport, defect $-e(1/3)$). A saving still requires
  a source-derived within-cell coherent-energy bound, which category theory does not supply.
  Implemented + tested: `observational_succ/signed_pushforward.py`.
- **Observed time-dependent conjugacy.** $g_n(x)=x-U_n$ conjugates the forced
  $T_n(x)=16x+r(n+1)$ to bare $x\mapsto 16x$, but **transports the observable** $e(hx)\mapsto
  e(h(y+U_n))$. A bare dynamical isomorphism that erases the selected phase is *not* a
  source-faithful observational equivalence. Negative theorem (kept; dense-subgroup-of-forcing-
  differences argument in the #302/#304 functor-obstruction tests, not re-derived here): no
  nonconstant continuous time-*independent* $F$ intertwines every authentic nonautonomous $T_n$
  with one fixed map.
- **Finite source-indexed Beck–Chevalley (reuse PR #194).** Formal pullback equality does not
  guarantee actual-source realization; the realization firewall (`realization_firewall_breaks`)
  is the typed witness that a flat square can hide the defect.

A "category score", a matching numerical invariant, a KZ-associator/$\zeta(2)$ appearance, or a
positive Gram is **not** the theorem and does not authenticate a BBP functor.

## 5. Required hostile regimes (a proof must fail every countermodel for a *source* reason)

Authentic zero seed + original four-pole; exact forcing + changed seed; zero seed + changed
forcing (SS-08); positive changed forcing preserving all carries/conductor and even the $\pi/16$
sum (#304 Control); $p=3,5$ exceptional-pole overlaps; $p\ge7$ source clocks; both $n^2$ and
$n^3$ moving-frequency bands; increasing $H_N$; finite-horizon source cut; $0/1/\infty$ puncture
collision; false source label; mutated receipt. Success must be forced by an explicit source
law, never a hard-coded name or opaque equality.

## 6. The next discriminating construction (updated October 26)

Construct an observable-preserving interface between the **relative** source Mellin factor
and a declared signed, joint carry observable, retaining the exact four poles, $U_0=0$ and
the integer lift. Begin with two hexadecimal digits and compute every cross-digit Walsh
coefficient that survives for the requested frequency; marginal balance is insufficient.
The relative Mellin factor and the proved moving-frequency source-circle observable
Theta_n are explicitly given in the source-bridge dossier. The missing construction
must transport the latter's auxiliary cancellation to the actual selected observable.
A scalar normalizer, the raw $\times16$ ratio, or the unit-cell cancellation alone cannot
do so: the new uniform-cell rational control passes all these auxiliary asymptotics.

The first acceptance gate is an explicit intertwining/transport identity with its residual
bound, tested against both matched-moment rational controls, including the uniform-cell
law, and the exact-forcing changed-seed control. A normality conclusion additionally requires a proved all-$N$ signed estimate;
restating §2 in Mellin notation pays no proof debt. No claim is made that the remaining
candidate routes exhaust possible mathematics.

The finite polynomial compiler gives a second exact interface. Its rational realizations
obey a proved phase-transport budget of
`28|h| rho_M (16^N-1)/(15N)`. The sufficient schedule
`M_N=4N+2 ceil(log_2(N+2))` makes this budget vanish for fixed h. Every fixed depth has
a rational total and is nonnormal at a depth-dependent frequency, so the depth and time
limits must remain separate. Any successful use must retain the full atom output,
harmonic observation, zero selector and depth schedule. The common denominator,
positive metric contraction and endpoint PGF alone do not give arithmetic cancellation.

Full handoff: [atoms, finite realization and selected phase](../handoffs/FOUR_POLE_ATOMIC_NEXT_2026-10-26.md),
with the earlier [relative phase and carry obligations](../handoffs/OILY_MACARONI_RELATIVE_PHASE_NEXT_2026-10-26.md) retained.

**Current staged continuation:** [Oily carry/resonance synthesis](../research/2026-10-26/OILY_CARRY_RESONANCE_SYNTHESIS.md)
and [next execution handoff](../handoffs/OILY_CARRY_RESONANCE_NEXT_2026-10-26.md).
The literal carry-translated primitive character exposes a growing alias, and
the full endpoint packet convolution has inverse `(2I-S)^2`.
The genuine centered third cumulant has leading coefficient `8/81` at order
`(8n)^-2`, while all higher fixed-order leading mixed cumulants are gamma-free.
These source-typed identities and the degree-17 seed-character restriction
do not pay the remaining signed arithmetic estimate.
