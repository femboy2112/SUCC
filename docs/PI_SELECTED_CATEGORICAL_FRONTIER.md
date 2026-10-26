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

This is a **modulus upper bound**. The normalized modulus still tends to $1$. It is **not**
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
3. **Structural ceiling of the current method.** The finite inverse lemma requires
   $34a+\lvert h\rvert\cdot(\text{range }r)<1$, forcing $a<1/34$, so it only controls an
   *absolute* block loss $\le 8a^2<2/289$, independent of block length. Getting $o(N)$ needs a
   positive-proportion *relative* loss on a positive proportion of blocks — a **moderate-coherence
   inverse theorem that does not exist on the branch**.
4. **Diophantine input alone cannot suffice (Control C).** $\xi=\sum 16^{-2^k}$ has irrationality
   exponent $2$ yet Fourier sums $N+O_h(\log N)$. Any extension must use the zero anchor $U_0=0$
   and the actual source, not just an irrationality bound.

## 4. How the categorical apparatus must serve §2 (not replace it)

Category theory here **predicts an obligation or an obstruction** for the §2 estimate; it does
not certify it. The load-bearing constructions (see `docs/CATEGORICAL_OBSERVER_ATLAS.md`) are:

- **Signed-interference pushforward (first-class proof obligation, not an automatic zero).**
  Under a partition coarsening $f$, $z'=P_f z$ and $K'=P_fKP_f^{*}$ with
  $K_{a,b}=z_a\overline{z_b}$. This retains the cross-stratum signs that positive conditional
  energies hide. The *missing signed term* is the typed obligation whose vanishing (in the
  low-frequency band) is exactly §2 — never assumed from positivity.
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

## 6. The single next discriminating probe (Codex/Astra handoff target)

> Prove a **moderate-coherence inverse theorem** for the authentic orbit: a positive-proportion
> *relative* Fourier loss on a positive proportion of width-8 blocks, using the zero anchor
> $U_0=0$ and the exact integer carries — the only identified route past the $a<1/34$ absolute
> ceiling of DC-5. Target the low-frequency band of §2 directly; do not attempt global Walsh
> smallness (Control §3.2) or lean on the Diophantine input alone (Control §3.4).
