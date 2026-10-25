# The π Frontier Contract

*Coherent Main X (2026-10-24). The companion to the
[π Gearbox Atlas](PI_GEARBOX_ATLAS.md): the exact open estimates that would close
the base-16 normality of π, each stated with its quantifiers, normalization,
logical target, and current status.*

**Standing status.** Every route below is **OPEN**. This document states *what
must be proved*, not what has been. π normality, its logical independence, RH,
and absolute/decimal normality remain open. Finite numerical agreement is **not**
a certificate; a conditional criterion is **not** its hypothesis.

## Common objects and normalization

Fix the authentic source of the [Atlas §0](PI_GEARBOX_ATLAS.md): $U_0=0$,
$U_{n+1}=16U_n+r(n+1)$, $\alpha=\pi/16=\lim U_n/16^n$. Write $x_t=\{16^{t-1}\pi\}$
for the base-16 orbit point read off the authenticated state at time $t\ge1$
(the certified hex digit of the Atlas). For a fixed nonzero integer $h$ the
relevant **selected signed exponential sum** is

$$S_N(h)\;=\;\sum_{t=1}^{N} e^{2\pi i\,h\,x_t}.$$

By Weyl's criterion, base-16 normality of $\alpha$ is **equivalent** to
$S_N(h)=o(N)$ for every fixed $h\ne0$. The trivial bound is $|S_N(h)|\le N$.
Every route is a different arithmetic handle on *exactly this* cancellation; none
is permitted to replace $x_t$ by an independently sampled surrogate, or to swap
prime-depth, source-time, and completion limits without a theorem controlling the
exchange.

---

## Route A — selected harmonic / cyclotomic saving (#284)

**Statement to prove.** For each fixed nonzero integer $h$, with the authentic
weights $w_{K_N,k}\ge0$ and cyclotomic blocks $W_{k,N}(h)$ of the #284 harmonic
construction,

$$\frac{1}{N}\sum_{k<K_N} w_{K_N,k}\,\bigl|W_{k,N}(h)\bigr|\;\longrightarrow\;0.$$

**Normalization / quantifiers.** $h$ fixed; $N\to\infty$; $K_N$ the branch's
window schedule; weights normalized so the positive Fejér mixture has the proved
source error budget $88/1575$.

**What is already in hand (EXACT/CONDITIONAL).** The positive harmonic Fejér
mixture *has* that proved budget for authenticated growing cyclotomic lags, and
there is an integer critical logarithmic schedule. The naive signed $1/k$ kernel
**fails** positivity (negative at angle $\pi$, $K=4$), so positivity of the
mixture is not automatic and is not the same as cancellation.

**Debt.** Derive an arithmetic estimate **strictly stronger than the trivial
bound** from the original four-pole forcing, the selected initial state, the
signed carries, and controlled time/prime correlations — not a restatement of the
criterion.

**Implication if discharged.** A genuine $o(1)$ here feeds the van der Corput /
Fejér comparison already in the branch into $S_N(h)=o(N)$ for that $h$;
quantified over all $h\ne0$ it yields base-16 normality. **Status: OPEN.**

---

## Route B — prescribed real collision / trimmed joint entropy (#278, SCE-07)

**Statement to prove (collision form).** At scale parameter $c=2/5$, the
prescribed-scale real-cell collision kernel satisfies

$$K_p(1)=p^{\,o(1)}\qquad(\text{SCE-07}),$$

or equivalently the source-authenticated **trimmed** joint real-cell collision
excess of #278 is subexponential.

**Normalization / quantifiers.** $p$ the prime-window parameter $\to\infty$;
collisions counted on the *real* circle cells, with the trimmed joint law (not
the dyadic residue collisions, which are a different quantity).

**What is already in hand (EXACT).** Exact BBP transport costs at most a factor
two; the all-gain stationary-law classification is elementary and needs no entropy
premise; all-rank and source-matching moving-prime controls preserve the scope of
the reduction. The classical upper-only frequency criterion is only a motivation.

**Debt.** Prove the subexponential collision bound **with real-circle, prime-window
coverage** and whatever global transport is needed; dyadic residue collisions do
**not** substitute.

**Implication if discharged.** A subexponential trimmed collision excess bounds
the second moment of the selected occupation, forcing $S_N(h)=o(N)$ through the
#278 reduction. **Status: OPEN.**

---

## Route C — source-selected four-bit Walsh / Fourier jet (#271)

**Statement to prove.** A nontrivial (power-saving) estimate for the **signed
highest-order** four-bit Walsh/Fourier interaction $M_A$ with $A=\{1,2,3,4\}$ in
the exact decomposition

$$16Z-Q_0=\sum_{\varnothing\ne A\subseteq\{1,2,3,4\}} M_A.$$

**Normalization / quantifiers.** The 16-cell Walsh inversion is exact; the target
is the top interaction term over the source window, with the four-pole forcing
entering the Fourier jet at the branch's recorded point.

**What is already in hand (EXACT).** The complete sixteen-cell Walsh inversion,
and an even-parity **countermodel**: all lower-order bit marginals can be uniform
while the four-bit event is biased. Hence half-bit marginal control does **not**
substitute for the top interaction.

**Debt.** Bound the selected signed jet $M_{\{1,2,3,4\}}$ nontrivially; the
highest-order interaction is essential and is where the current error budget is
still unproved.

**Implication if discharged.** Controls the biased four-bit event the countermodel
exhibits, removing the obstruction to digit-block equidistribution at radix $16$.
**Status: OPEN.**

---

## Route D — the missing prime-window interaction (#277/#278/#279)

**Statement to prove.** A power saving for the **selected channel**

$$\sum_{t\in\mathcal{W}_p} e^{2\pi i\,4h\,16^{t}/p}\;e^{2\pi i\,h\,w_t},$$

where $w_t$ is the **actual complementary BBP source** (twisted-pair / Galois
differential), not independently sampled noise, and $\mathcal W_p$ is the genuine
moving prime window.

**Normalization / quantifiers.** $h$ fixed nonzero; $p$ ranging over the prime
family with its exceptional primes ($p=3,5$) and endpoint costs kept; the window
$\mathcal W_p$ transported, not frozen.

**What is already in hand (EXACT).** The genuine source rational function, pole
clocks, Galois differentials, Pascal source differences, and exact literal carry;
and the twisted-pair distinction between cancellation of
$Z_t(a)\overline{Z_t(b)}$ and cancellation of the **selected** channel $Z_t(1)$ —
no Gram/ensemble average may silently select the real channel.

**Debt.** Two separate obligations: (i) prove a power saving for the channel;
(ii) prove **separately** whether the resulting prime-family estimate genuinely
implies Route A or Route B — a saving here does not automatically transfer.

**Implication if discharged.** Only *via* a proved transfer to A or B; on its own
it is a prime-window bound. **Status: OPEN (including the transfer).**

---

## Route E — alternative bases (#270/#276/#280)

**Kept strictly separate.** Base-3 measure rigidity (conditional premise) and the
rational-base $11/10$ signed-decimal Pascal bridge are *distinct* research tracks.

- The dyadic refinement $P_{k+4}\le P_k/16+15N/16$ is proved **in its own domain**
  and does not prove real-circle $1/16$ frequencies.
- The $11/10$ algebra must **not** be promoted to decimal normality.
- No unproved cross-base normality transfer is assumed; primes below 16 are not
  assumed to suffice.

**Status: OPEN; no transfer claimed.**

---

## Route F — RH (separate frontier, #285/#286/#287)

**Kept strictly separate from π.** The completed Euler–Mascheroni / Li / Weil
boundary accounting may be *reused* as infrastructure, but the signed BBP temporal
bound remains a distinct theorem obligation. Explicitly **not** permitted:

- a finite Γ-jet authenticating ζ;
- a finite Li bound proving all-degree Li positivity;
- a positive generic graph / Hilbert kernel identifying the signed Weil form.

**Status: RH OPEN; no normality consequence either direction.**

---

## The one-line verdict

The gears are built and they mesh (Atlas §1–§2, machine-checked). The force that
must cross the real-circle boundary is a **single power-saving estimate on the
selected signed sum $S_N(h)$** — available in four candidate shapes (A–D), with
E and F explicitly fenced off. Until one of A–D is discharged **unconditionally
and source-faithfully**, π normality is not proved. It is not proved here.
