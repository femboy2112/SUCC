# Next round — the moderate-coherence inverse theorem (selected-π cancellation)

**For:** Codex / Astra (next math round). **Base:** main after Operation Main XI consolidation.
**Single target:** the one estimate that would close base-16 normality of π. **Status going in:
π normality OPEN, RH OPEN (separate).** This is a focused proof probe, not a consolidation round.

## The one thing to prove

For the **unique authentic BBP orbit** $U_0=0,\ U_{n+1}=16U_n+r(n+1)$,
$r(n)=\tfrac{4}{8n-7}-\tfrac{2}{8n-4}-\tfrac{1}{8n-3}-\tfrac{1}{8n-2}$, prove

$$ \frac1N\sum_{n\le N} e(hU_n)=o(N)\ \text{(i.e. }=o_h(1)\text{ after }/N)\quad\text{for every fixed }h\neq0, $$

equivalently (both reductions already **proved**, do not redo):

- **#293 / SGO-09 (proved):** $\big|\sum_{n\le N}e(h16^{n-1}\pi)-\sum_{n\le N}e(hU_n)\big|<\tfrac{119}{648}|h|$, so normality $\iff$ the display above.
- **The narrowed sufficient gate (open), on the derived flat-carry $b_t=c_t\mathbf 1_{\{Q_t=Q_{t-1}\}}$:** with $H_N=\max(2,1+\lfloor\sqrt{\lfloor\log_2N\rfloor^3}\rfloor)$, $J_N=\min\{J:16^J\ge NH_N^2\}$,
$$ 2\sum_{h=1}^{H_N-1}\Big(1-\tfrac h{H_N}\Big)\Big|\tfrac1N\sum_{n\le N}e\big(h\textstyle\sum_{j=1}^{J_N}16^{-j}b_{n+j}\big)\Big|^2=o(1). $$

## What is already proved (reuse, do not re-derive)

- **DC-1 (#304, paper-proved):** $\big|\sum_{n\le N}e(hU_n)\big|\le N-\tfrac1{1250}\max(0,\lfloor\log_8N\rfloor-\max(J_0,\lceil\log_{64}|h|\rceil))$. This is a **modulus** loss; normalized $\to1$. It is **NOT** the target and must not be cited as cancellation. Uses only $\mu(\pi)<15/2$ (published ZZ $\le7.1032$, arXiv:1912.06345v2); $J_0$ exists but is **not** numerically extracted.
- Transport lemmas SCT-1…4, SP-I4 (comparison between $U$, the flat carrier $Y^{\mathrm{flat}}$, and the Weyl sum) — **asymptotic only; numerically vacuous at every finite $N$ in the receipt** (mode-error $>1$ even at $N=2^{256}$). Use them symbolically, not as finite evidence.

## Why the current method is stuck (the wall to get past)

The finite inverse lemma (DC-5) requires $34a+|h|\cdot\mathrm{range}(r)<1\Rightarrow a<1/34$, so it only
controls an **absolute** per-block loss $\le 8a^2<2/289$, independent of block length. The target needs a
**positive-proportion _relative_ loss on a positive proportion of width-8 blocks** — a *moderate-coherence*
inverse theorem that does not exist on the branch. **That theorem (or a structure-theorem refutation of it) is the deliverable.**

## Two hard constraints the proof must respect

1. **Diophantine input alone cannot suffice (Control C, proved):** $\xi=\sum16^{-2^k}$ has irrationality
   exponent $2$ yet Fourier-sums $N+O_h(\log N)$. The proof **must** use the zero anchor $U_0=0$ and the exact
   integer carries / four-pole source — not merely an irrationality bound.
2. **Do not pursue global Walsh smallness:** the all-frequency Walsh energy is bounded below generically
   ($\ge H^2-1$, no π content). Only the **low-frequency** band of the gate can shrink; target it directly.

## Required hostile controls (a real proof fails every one for a *source* reason)

authentic zero seed + original four-pole; exact forcing + changed seed; zero seed + changed forcing (SS-08);
positive changed forcing preserving all carries/conductor and the $\pi/16$ sum; $p=3,5$ exceptional-pole
overlaps; $p\ge7$ clocks; $n^2$ and $n^3$ moving-frequency bands; increasing $H_N$; finite-horizon cut;
$0/1/\infty$ puncture collision; false source label; mutated receipt.

## Deliverable

Either (a) the moderate-coherence inverse theorem with a checkable receipt and the hostile controls failing for
a source reason, promoting the gate toward proved; or (b) the exact obstruction (a structure theorem showing
where a counterexample must live) plus the smallest next discriminating probe. **No** promotion of a modulus
bound to a cancellation theorem; **no** signed asymptotic saving asserted from positivity or diagram commutation.
Categorical apparatus (see docs/CATEGORICAL_OBSERVER_ATLAS.md) may supply the signed $K\mapsto PKP^*$ obligation
and the observed-conjugacy transport, but the estimate is arithmetic and must be proved as such.
