# Selected-phase forge: an actual signed saving and the carry information that survives

**Result:** the authentic zero-initial BBP orbit has a proved logarithmic
**absolute** loss from maximal Fourier reinforcement. A quantitative carry
transport also removes all conductor-birth carries at a prescribed width
growing like $(\log N)^{3/2}$. Neither result proves spectral purity or
base-16 normality of pi. The surviving signed estimate remains **OPEN**.

## 1. Live provenance and selected front

This round fetched all remote branches, fast-forward checked the prior
Spectral Purity checkout, and opened the isolated branch
`research/pi-selected-phase-forge-2026-10-25` at live PR #301 head
`b792caae40dfe777cf7e9d3301b61f1ac0adac41`. That head contains PR #298 and
its conductor-growth removal theorem. Main remained
`1e3a453e869992961bc2d7f3bb6f2f1ddab38854`.

The [remote baseline](selected_phase_validation/remote_baseline.json)
records heads, discussions and CI for #297--#302. The most useful sibling
input was #297's inverse-coherence theorem. The sibling #299 supplies a
clock comparison and an initial-state control to strengthen. Their code was
not merged: #299 and #301 use the same module name for different instruments.
Each new implementation records its exact originating source and rederives
the required narrow interface. #300's target/access distinction and #302's
boundary analysis do not themselves estimate selected Weyl cancellation.

The primary source remains precisely

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

## 2. The new unconditional signed upper bound

There is one integer $J_0$ such that for every $N\ge1$ and every nonzero
integer $h$,

$$
\boxed{
|S_N^U(h)|\le N-\frac1{1250}
\max\left(0,\lfloor\log_8N\rfloor-
\max\left(J_0,\lceil\log_{64}|h|\rceil\right)\right).
}
$$

The [complete proof](BBP_DIOPHANTINE_COHERENCE.md) widens the source block
to $(m,8m]$. Extreme coherence would force an inverse seed arc. Exact Green
cancellation turns that arc into a rational approximation to pi of error
less than $16^{-8m}$ and denominator $15|h|16^m$. The published
[Zeilberger--Zudilin bound](https://arxiv.org/abs/1912.06345v2)
$\mu(\pi)<15/2$ excludes this for all sufficiently large $m$, uniformly
over $1\le|h|\le m^2$. Disjoint geometric blocks then supply the displayed
all-$N$ bound. No independence, Haar averaging, or digit-frequency premise
is used.

The arithmetic constants and finite inverse certificates are explicit.
The existence of $J_0$ is proved, but its numerical value is **not extracted**.
An executable budget with a supplied threshold remains conditional.

For fixed $h$ this is $|S_N^U(h)|\le N-(\log_8N)/1250+O_h(1)$.
It bounds the actual selected sum, not a conjugate average. However, its
normalized upper bound still tends to one. Even uniformly up to the
prescribed width $H_N=1+\lfloor\sqrt N\rfloor$, the resulting spectral
upper bound remains of order $H_N$, not $o(1)$.

This limitation is structural for the Diophantine input alone: the sparse
number $\sum_{k\ge0}16^{-2^k}$ has irrationality exponent two but Fourier
sum $N+O_h(\log N)$. With a changed initial state it also follows the exact
BBP forcing. The missing source ingredient must distinguish the original
zero-selected trajectory in the regime of **moderate** coherence, beyond
the constant absolute-loss premise of the inverse theorem.

## 3. Removing arithmetic births from the observable, with every boundary paid

Let $c_n=\lfloor U_n\rfloor-16\lfloor U_{n-1}\rfloor$ and let $Q_n$ be
the monotone common forcing conductor. The bounded carry profile is exactly

$$
Y_n=\sum_{j\ge1}16^{-j}c_{n+j}=\{U_n\}+T_n.
$$

Set the carry to zero only at times with $Q_k>Q_{k-1}$, and call the resulting
profile $Y_n^{\rm flat}$. This is a derived observable of the original
source, not a replacement forcing. The
[sparse-carry theorem](BBP_SPARSE_CARRY_TRANSPORT.md) controls each erased
carry's influence by a saturated character estimate. Its total past cost
is $O(\log |h|)$ and the entire unobserved future costs $O((\log |h|)^2)$.
Uniform truncation errors are explicit.

Combining this with the proved $O(N/\log N)$ authentic birth count gives
vanishing root-spectral transport error whenever
$\sqrt H\log H=o(\log N)$. In particular it works at the predetermined
width

$$
H_N=\max\left(2,1+\left\lfloor
\sqrt{\lfloor\log_2N\rfloor^3}\right\rfloor\right).
$$

This is wider than the $H=o(\log N)$ budget for directly deleting birth
terms from the innovation sum. It proves that purity of this derived
flat-carry profile would transfer to the authentic pi orbit at that width.
It does not prove the profile is pure. The new arithmetic saving is the
proved comparison error, not a renamed cancellation premise.

## 4. Sharper transport and stronger hostile controls

The [clock theorem](BBP_CLOCK_TRANSPORT.md) proves the sharp inequality

$$
|\sqrt{E_H(\mu)}-\sqrt{E_H(\nu)}|
\le\sqrt{H/2}\,\|\mu-\nu\|_1,\qquad E_H=D/H.
$$

Hence genuine sample rebalancing on a period-$Q$ clock transports purity
under $\sqrt H\,Q=o(N)$, improving the earlier sufficient condition
$HQ=o(N)$. A grid-measure control attains the constant exactly. The balanced
energy itself remains unbounded by this comparison.

Two stronger source-map controls identify what these comparisons cannot do:

1. A rational changed seed retains the full exact forcing and arbitrary
   specified finite p-adic state precision at **every** time, yet produces
   near-maximal coherence on any selected finite late window, for every
   partition and every probability weighting. It fails exact $U_0=0$ and
   may introduce new conductor places. The seed depends on the window.
2. The [positive carry control](BBP_POSITIVE_CARRY_CONTROL.md) is one fixed
   all-time changed forcing. It retains the zero anchor, every authentic
   integer carry, the entire common-conductor tower, strictly positive
   forcing, and even the scaled sum $\pi/16$. Nevertheless its fractional
   states tend to zero with a proved $O(n^{-2})$ bound. Its forcing has
   limsup at least one and its Green tail has limsup at least $1/16$.
   Those nonvanishing tails are the exact failed hypotheses. This is not
   a nonnormal pi digit orbit.

The companion backward-rigidity theorem proves that common carries plus
forcing difference tending to zero force phase difference tending to zero.
The positive control therefore cannot silently acquire the authentic
vanishing-forcing assumption as an extra preserved feature.

## 5. Authority and the next quantitative obligation

The [PSF claim ledger](../../docs/CLAIM_SUPPLEMENT_PI_SELECTED_PHASE.md)
separates classical inputs, paper proofs, exact finite instruments,
conditional numerical thresholds, refuted shortcuts and open estimates.
Eight finite declarations were actually checked by the pinned Lean kernel:
integer branch uniqueness, backward telescoping/endpoint transport, scalar
block-deficit summation and two rational margins. The complex inverse
argument, Diophantine theorem, asymptotics, and pi normality are not Lean
claims. Three paired false-theorem controls were rejected.

Workers share a model family and repository lineage. Different derivations,
exact implementations and held-out inputs improve verification but do not
constitute external mathematical refereeing. The independent classical
input is explicitly cited and is not relabelled a new SUCC theorem.
The contact is the literal source; source-map substitutions and proof
survival are audited separately; commitment to normality supplies no evidence.

The remaining sufficient gate is a source-derived $o(1)$ normalized purity
estimate on the prescribed flat-carry profile, or the earlier signed
conductor-flat innovation estimate. The new logarithmic absolute saving
does not discharge either. A next argument must control moderate coherence
using the original numerator evolution and exact zero selector, with the
transport costs above and the two different counterfeit families retained.

See the [validation record](PI_SELECTED_PHASE_VALIDATION.md) for actual
commands, failures, commits and delivery scope. No merge or release is made.
The [closed-round handoff](PI_SELECTED_PHASE_HANDOFF.md) states the remaining
finite dyadic-carrier gate and proves why global Walsh energy cannot be
used as its smallness bound.
