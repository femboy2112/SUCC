# Next round — the even-h sub-band, then the x16 ladder contraction

**For:** Codex / Astra (next math round). **Base:** `origin/main` after the Skeleton-Key / Main XII
staging PR merges. **Supersedes the framing of** `handoffs/CODEX_ASTRA_MODERATE_COHERENCE_NEXT_2026-10-26.md`
(that round's "fixed positive-proportion relative loss" target is now **proved insufficient** —
see SK2-A1). **π base-16 normality: OPEN. RH: OPEN (separate).** Focused proof probe, not a round.

## What Main XII settled (reuse, do NOT re-derive)

- **SK2-A1 (proved):** a *fixed* $c<1$ relative block loss on positive density gives only
  $|S_N|\le(1-c')N$ and $R^2_{N,H}=\Theta(H)$ — never $o(1)$. **Sufficiency needs $c=c_N\to1$.**
- **SK2-A2 (proved):** the DC-5 single-$\times16$-step lemma is capped at $a<1/34$ (absolute loss
  $<2/289$); escape needs the joint phase across $\ge2$ consecutive $\times16$ digits.
- **SK2-B/C/D/E/F/G (proved no-gos):** signed pushforward is gate-conservative + positivity-blind;
  CRT occupancy is phase-blind; signed base change holds iff cartesian (ghost-faithfulness
  insufficient); path coherence adds rank 0 (forcing-universal class); the degree-16 geometry is a
  coincidence trap; first-moment / bounded-order occupation-count tomography gives only the trivial
  bound. **SK2-H:** no surveyed classical theorem beats $N-O(\log N)$; van der Corput is circular on
  the $\times16$ orbit (FACT 1: lag-$k$ autocorrelation $=$ Weyl sum at $h\mapsto h(16^k-1)$).

## The one thing to prove (step 1)

On the flat-carry word-measure with $A_N(h)=\langle\text{measure},\kappa_h\rangle$ ($\kappa_h$
unimodular, $\pi$-free), prove the **even-$h$ half** of the §2 gate:

$$ 2\!\!\sum_{h\text{ even},\,1\le h<H_N}\!\!\Big(1-\tfrac{h}{H_N}\Big)\,|A_N(h)|^2=o(1), $$

using **only** the $\le3$-order Walsh/Lucas marginals of the leading flat-carry digit. This is
legitimate exactly for even $h$ because $\widehat g_h(15)=\prod_{i<4}(1-\zeta^{h2^i})=0$ there
(exact, verified $h=0..40$); the order-4 Walsh moment the marginals cannot see is switched off.
A proof **isolates the odd-$h$ order-4 signed band as the sole irreducible obstruction.**

## Step 2 (the live multiplicative route)

Test whether the $\times16$ frequency-ladder contracts:
$\limsup_{h}\lambda_N(h)<1$ where $\lambda_N(h)=|A_N(16h)|/|A_N(h)|$, for the **authentic** orbit,
while **failing** on every counterfeit that must be excluded. A one-step $\lambda<1$ compounds to a
power saving $(1-\delta)^{\sim\log_8 N}=N^{-\gamma}$, which *is* $c_N\to1$. The contraction must be
driven by the $15/64$ four-pole forcing resonance — **not** by $U_0=0$ or the integer carries,
which the hard controls share. Instrument stub: `observational_succ/signed_pushforward.py`
(`weyl_gate_value`, `occupancy_baseline`) + the IMW matrix walk.

## Hard controls (a real proof fails every one for a SOURCE reason)

authentic zero seed + original four-pole; exact forcing + changed seed; zero seed + changed forcing
(SS-08); positive changed forcing preserving all carries/conductor and the $\pi/16$ sum (#304
Control); $\xi=\sum16^{-2^k}$ (Control C, badly-approximable yet non-normal); $p=3,5$
exceptional-pole overlaps; $p\ge7$ clocks; $n^2,n^3$ moving bands; increasing $H_N$; finite-horizon
cut; mutated receipt. **Do not** use the phase-blind occupancy baseline $(H-1)/N$ as a gate value,
and **do not** promote any modulus bound or positivity to a signed saving.

## Falsification / fallbacks

If the even-$h$ band is not $o(1)$ by bounded-order marginals, or $\lambda_N(h)$ does not stay below
1 as $h,N$ grow, the multiplicative route is dead and only two mechanisms remain: signed $L^2$
cross-block cancellation $\sum_{j\neq k}S_{B_j}\overline{S_{B_k}}$, and the Weil/Deligne $\mathbb
F_p$ real-circle transport (**OSP-12 is the mandatory negative control** — its naive relative-trace
transport is already REFUTED).

## Deliverable

Either (a) the even-$h$ fragment proved with a checkable receipt and the controls failing for a
source reason; or (b) the exact obstruction in the odd-$h$ order-4 band plus the smallest next
discriminator. **No** promotion of a modulus/occupancy quantity to a cancellation theorem; **no**
signed saving from positivity or diagram commutation. Categorical apparatus is exhausted for signed
saving (SK2-D); the estimate is arithmetic and must be proved as such.
