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

## Exact preliminary reduction — one authentic rational orbit, no unresolved phase tail

The same original Coherent Main X four-pole source has a finite rational
unwrapped state $U_0=0$, $U_{n+1}=16U_n+r(n+1)$ and a **source-defined**
positive future Green correction $T_n=\sum_{j\ge1}16^{-j}r(n+j)$.
Their complementary equations imply
$U_n+T_n=16^{n-1}\pi$ for $n\ge1$.
A proved $\ell^1$ bound for the **entire selected tail** gives

$$
\boxed{\sum_{n\ge1}T_n\le\frac{17}{648},\qquad
\left|S_N(h)-\sum_{n=1}^N e^{2\pi i h U_n}\right|
<\frac{119}{648}|h|,\quad
N\ge1,\ h\in\mathbb Z\setminus\{0\}.}
$$

This is a **paper-proved source-authentic continuous-character transport**
with exact rational finite interval instruments; see the
[Signed Gamma–BBP Green dossier](../research/2026-10-25/SIGNED_GAMMA_BBP_GREEN_COHERENCE.md)
and [SGO claim supplement](CLAIM_SUPPLEMENT_SIGNED_GAMMA_BBP.md).
The corresponding normalized Weyl sums differ by $O_h(1/N)$, so
base-16 normality of π is **equivalent** to cancellation of the original
rational $U_n$ phases. It is NOT a proof that these rational phases cancel:
the new target is

$$
\sum_{n=1}^N e^{2\pi i h U_n}=o(N)
\quad\text{for each fixed }h\ne0.
$$

Unlike a single fixed rational approximation of π, $U_n$ is the actual
ever-refined original BBP recurrence; unlike a sampled independent prime
measure, its integer lift, source signs and initial condition are unchanged.
Direct digit indicators are discontinuous and require separate boundary-cell
costs. The Gamma signed moment inequalities **cannot substitute** for this
still-open arithmetic cancellation.

---

## New matrix-valued proof gate — one external successor, retained internal Fourier correlations (IMW)

The authentic exact rational states $U_n$ feed a matrix observer
$v_n=(e(0),e(U_n),\ldots,e((H-1)U_n))$ and its source Gram
$G_{N+1}=G_N+v_{N+1}v_{N+1}^*$, $A_N=G_N/N$.
The **finite algebraic spectral identity**

$$
\boxed{\operatorname{tr}(A_N^2)-H=
2\sum_{j=1}^{H-1}(H-j)|S_N^U(j)/N|^2}
$$

makes exact Fourier cancellation an *internal-matrix* question. If a
growing window $H_N\to\infty$ obeys
$\operatorname{tr}(A_{N,H_N}^2)-H_N=o(H_N)$, then Weyl and the proven
SGO Green-tail source transport imply π base-16 normality. **This
quantitative matrix estimate is OPEN; it is not implied by Gram
positivity or circle symmetry.**

The exact one-step purity differential is a Fejér sum over all
source-selected phase differences with the new $U_{N+1}$. The
frequency-ladder Koopman matrix also has a **provably nonvanishing moving
high-frequency source twist** at scales $n^2$, and the differentiated
matrix at $n^3$; hence fixed finite Fourier matrix convergence cannot be
promoted to uniform operator-norm convergence. These are source-specific
constraints/obstructions, NOT the missing estimate. The
[full IMW dossier](../research/2026-10-25/SUCC_INTERNAL_MATRIX_WALK.md),
[status ledger](CLAIM_SUPPLEMENT_SUCC_INTERNAL_MATRIX.md) and
[research handoff](../research/2026-10-25/ASTRA_MATRIX_WALK_NEXT_MOONSHOT.md)
identify how Pascal, Walsh, cyclotomic and original integer-lift clocks
could try to produce a genuinely new bound without inventing any
independence assumption.

---

## Validated narrower matrix gate — conductor-flat signed innovation (OSP)

The [Spectral Purity dossier](../research/2026-10-25/OPERATION_SPECTRAL_PURITY.md)
proves a source-specific removal at a **prescribed** width. Define the
monotone source conductor, not the last state's reduced denominator, by

$$
Q_n=\operatorname{lcm}_{1\le j\le n}\operatorname{den}(r(j)),\qquad Q_0=1,
\quad H_N=\max\left(2,1+\left\lfloor\sqrt{\lfloor\log_2N\rfloor}\right\rfloor\right).
$$

For $X=8N$, $L=\lfloor\log_2X\rfloor$, $K=\lceil\log_2X\rceil$, put

$$
B_N=\min\left(N,L\lfloor\sqrt X\rfloor+\frac{4(2^K-1)}L\right).
$$

Authentic conductor-growth times inject into odd prime powers at most $8N$.
Elementary Chebyshev counting and $|q-H|\le H(H-1)$ prove

$$
\frac{2}{N^2H_N}
\sum_{\substack{1\le m<N\\Q_{m+1}>Q_m}}m|q_{m,H_N}-H_N|
\le\frac{2(H_N-1)B_N}{N}=o(1).
$$

This is an **unconditional PAPER-PROVED partial-timeline saving**, with exact
finite count and budget instruments. Therefore the surviving sufficient gate is

$$
\boxed{\limsup_{N\to\infty}\frac{2}{N^2H_N}
\sum_{\substack{1\le m<N\\Q_{m+1}=Q_m}}m(q_{m,H_N}-H_N)\le0.}
$$

The discrepancy between this signed flat-step sum and $D_{N,H_N}/H_N$ is
at most $(H_N-1)/N+2(H_N-1)B_N/N$, which tends to zero. Nonnegativity of
$D$ then closes the implication if the boxed estimate is proved.
**The boxed source-selected estimate remains OPEN.** The flat timeline has
weight asymptotic to $N^2/2$; exact source authentication supplies no bound
on its signed correlations by itself.

Additional validated boundaries:

- The unrestricted existence of an arbitrarily slow purity window is
  **equivalent to equidistribution** by an explicit diagonal proof. It is
  not an independent saving. No equivalence to qualitative normality is
  asserted for the particular prescribed rate above.
- A new original-source Green theorem gives
  $|\sqrt{D^U_{N,H}/H}-\sqrt{D^\pi_{N,H}/H}|\le\sqrt{7(H^2-1)/24}/N$,
  so every prescribed $H=o(N)$ transports purity in both directions.
- Relative cyclotomic trace does not bound the selected innovation: actual
  BBP $q_{1,3}>5$ while its new $3^2$-layer trace equals $3$.
- Matching any finite prefix and endpoint jet, all positive moment signs,
  odd denominators and all fixed leading critical bands still permits a
  positive rational nonnormal counterfeit. A separate positive counterfeit
  retains even the entire authentic conductor tower. Both change the
  exact four-pole law; neither refutes normality of the authentic source.

See [OSP-01--14](CLAIM_SUPPLEMENT_SPECTRAL_PURITY.md) for precise authority.
Ten finite real-kernel declarations are Lean-checked; the arithmetic density,
analytic Green transfer, counterfeit existence and infinite-limit implications
are paper proofs. Pi normality remains **OPEN**.

---

## Validated selected loss and wider carry transport (PSF)

The [selected-phase dossier](../research/2026-10-25/PI_SELECTED_PHASE_FORGE.md)
proves a new upper bound on the actual signed sum. For one universal integer
$J_0$, all $N\ge1$ and $h\ne0$ satisfy

$$
|S_N^U(h)|\le N-\frac1{1250}
\max\left(0,\lfloor\log_8N\rfloor-
\max\left(J_0,\lceil\log_{64}|h|\rceil\right)\right).
$$

This **PAPER-PROVED logarithmic absolute loss** uses the authentic zero
anchor and the published bound $\mu(\pi)<15/2$. An almost maximally coherent
$(m,8m]$ block would yield an impermissibly accurate rational approximation
after exact Green cancellation. The numerical onset $J_0$ has not been
extracted. The normalized upper bound tends to one: this is not $o(N)$
cancellation and does not close the matrix gate.

A separate quantitative comparison removes **all conductor-birth carries**
from the derived bounded profile

$$
Y_n=\sum_{j\ge1}16^{-j}c_{n+j}=\{U_n\}+T_n,
\qquad c_n=\lfloor U_n\rfloor-16\lfloor U_{n-1}\rfloor.
$$

Call the censored profile $Y_n^{\rm flat}$, setting only carries with
$Q_k>Q_{k-1}$ to zero. The comparison pays each deleted carry's
$O(\log |h|)$ influence and the entire $O((\log |h|)^2)$ future boundary.
The proved birth count gives vanishing root-spectral error whenever
$\sqrt H\log H=o(\log N)$. One prescribed valid width is

$$
H_N=\max\left(2,1+\left\lfloor
\sqrt{\lfloor\log_2N\rfloor^3}\right\rfloor\right).
$$

At this width, an $o(1)$ normalized purity bound for $Y^{\rm flat}$ would
prove the same for pi. **That source-selected estimate is OPEN.** The
censored sequence is a defined observable of the original source, not an
independently generated or Haar-distributed replacement.

Two additional boundaries are now proved. Genuine sample-clock reweighting
costs at most $\sqrt{H/2}$ times its probability-measure $\ell^1$ change,
so $\sqrt H Q=o(N)$ suffices for its transport. Conversely, positive forcing,
the exact complete carry and conductor tapes, zero initialization and even
the scaled source sum $\pi/16$ admit a nonnormal rational-state control.
Its forcing and Green tail do not vanish. Common carries **plus vanishing
forcing difference** instead force asymptotic phase agreement by the exact
backward recurrence. These statements isolate a real source-map boundary;
none supplies the missing temporal cancellation.

See [PSF-01--14](CLAIM_SUPPLEMENT_PI_SELECTED_PHASE.md) for authority and
counterexamples. The eight new finite Lean declarations do not formalize
the analytic irrationality input or the infinite normality consequence.

---

## Selected inverse-branch gate — actual carry/arrival comparison (#312 continuation)

This continuation is based on #312 at
`0c306a889f425418c29cbea3193205fb80c0575e`, with the carry/packet construction
of sibling #311 inspected at `a34c4484059e667202b97d5ab4102560987b1406`.
The sibling is not merged. Use $y_n=\{U_n\}$ in this section to distinguish
the rational state from the Green-corrected $x_n$ in the common objects.
Put $j_n=\lfloor16y_n\rfloor$, $t_n=\{16y_n\}$ and keep the literal carry
$c_{n+1}=\lfloor U_{n+1}\rfloor-16\lfloor U_n\rfloor$.

**New proved source estimate.** Scaled spills

$$s_k^{(a)}=\lfloor\{16aU_{k-1}\}+a r(k)\rfloor>0$$

force the next $L_a(k)=\max(0,\lfloor\log_{16}(4(k-1)^2/a)\rfloor)$
scaled carries to vanish. Thus their count $K_{N,a}$ on $2\le k\le N+1$
is at most

$$B(N,a)=\min\left(N,R-2+
\left\lceil\frac{N+2-R}{L_a(R)+1}\right\rceil\right),
\qquad R=\max(2,1+\lfloor(aN^2)^{1/4}\rfloor),$$

using $B=N$ if $R>N+1$. This proves $B(N,a_N)=o(N)$ for every prescribed
$a_N=o(N^2)$, without measuring a Fourier coefficient. Let $E,\Delta$ be
the #312 conditional energies for records $(\lfloor Mt_n\rfloor,j_n)$;
let $\widetilde E,\widetilde\Delta$ use the actual arrival records
$(\lfloor My_{n+1}\rfloor,c_{n+1}\bmod16)$. Then, uniformly in $h$,

$$\lvert E-\widetilde E\rvert\le
\frac{4[B(N,1)+B(N,M)]}{N},\qquad
\lvert\Delta-\widetilde\Delta\rvert\le
\frac{32[B(N,1)+B(N,M)]}{N}.$$

Both errors vanish at every preset $M_N=o(N^2)$. At $M=8N^2$, however,
every authentic bin label changes: the exact positive polynomial for
$8N^2r(N+1)-1$ proves $K_{N,8N^2}=N$. The subquadratic guarantee cannot
be extended to every quadratic scale by this argument. This is a statement
about record changes, not an energy lower bound.

**Narrower parity debt.** Prescribe $M_N=\max(2,\lfloor\log_2N\rfloor)$.
The carry-sensitive primitive mass in each actual arrival bin is
$\Phi_b=4/9+\Pr(c_{n+1}\text{ odd}\mid b)/9$. Exactly,

$$\widetilde E_{N,M}(8)=324\sum_b\widetilde p_b(\Phi_b-1/2)^2.$$

Proving this actual conditional variance tends to zero now suffices for
the original parity-energy target, with a proved $O(1/\log N)$ transport
error. **The variance estimate is OPEN**, and parity alone is insufficient
for all branch modes; quarter-turn and higher interactions remain.

**Weaker signed gate retaining cross-bin cancellation.** Put
$\tau_b=(b+1/2)/M$ and

$$\widetilde C_{N,M}(h)=\frac1N\sum_{n=1}^N
e\left(\frac{h(c_{n+1}+\tau_{\lfloor My_{n+1}\rfloor})}{16}\right).$$

The original recurrence proves, for all $N,M\ge1$,

$$\left|\frac1N\sum_{n=1}^Ne(hU_n)-\widetilde C_{N,M}(h)\right|
\le\frac{\pi|h|}{16M}
+\frac{\pi|h|}{8N}\sum_{n=1}^Nr(n+1).$$

Thus a source-derived $\widetilde C_{N,M_N}(h)=o(1)$ for every fixed
$h\ne0$ at the prescribed growing resolution would close normality.
That signed bound is **OPEN**; the displayed comparison is not a saving.

**Validated obstructions.** For the actual minimal odd prefix conductor
$Q_N$, every $M\ge Q_N$ gives $E(h)=1$ and $\Delta=15$. Exact conditioning
cannot inherit the 16-predecessor Haar gap. A fixed changed-seed history
with the *entire original forcing* can cancel any prescribed finite band,
have endpoint irrationality exponent two and donor-level logarithmic
absolute loss, yet have all conditional energies tend to one at every
fine growing resolution. It fails the zero selector; it does not refute
the π target. Neither finite-band tests nor Diophantine type replaces
the remaining selected conditional or signed estimate.

See the [full proofs](../research/2026-10-26/SELECTED_BRANCH_SYNTHESIS.md)
and [authority ledger](CLAIM_SUPPLEMENT_SELECTED_BRANCH.md). The inherited
arbitrary-slow-schedule normality equivalence is explicitly not counted
as new progress. No improvement to the best authentic signed-modulus
order is claimed.

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
must cross the real-circle boundary is a **single sublinear estimate on the
selected signed sum $S_N(h)$** — available in four candidate shapes (A–D), with
E and F explicitly fenced off. Until one of A–D is discharged **unconditionally
and source-faithfully**, π normality is not proved. It is not proved here.
