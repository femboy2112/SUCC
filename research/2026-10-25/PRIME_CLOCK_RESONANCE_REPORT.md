# Prime-clock resonance: exact compression and the sharp forcing-only boundary

Date: 2026-10-25. Parent: PR #296 at
`461942c0bf616518e668d236d1c6b1596665a7dd`; main observed at
`1e3a453e869992961bc2d7f3bb6f2f1ddab38854`. This is a separate research
branch, independent of the concurrent Fejer/Gram-purity attack. No merge.

**Result:** new exact gcd compression, a source-forced coherence gap with
order-optimal countercontrols, and a fresh-prime obstruction to naive lag
descent. **The requested authentic signed decay is NOT proved. Pi normality
and RH remain OPEN.** Scholarly novelty is unverified; all novelty here means
new relative to the inspected repository, not a priority claim.

## 1. Hole contract and recovered baseline

The unchanged source is

$$
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
$$

For prime p=8m+1, n0=m+1, D=3m, L=ord_p(16), L divides m. In this
entire first-birth window,

$$U_{n0+t}=4\cdot16^t/p+w_t\pmod1,\quad
u_t=e(4h16^t/p),\quad v_t=e(hw_t),\quad W_p(h)=\sum_{t<D}u_tv_t.$$

The target remains `W_p(h)/D -> 0` for every fixed nonzero h on a
relative-scale-covering good-prime family. The selected initial state, every
four-pole forcing value, integer lift, and complementary phase are required.
An arbitrary correlated weight is outside BGK's hypotheses. This is a
pathway gap in source-selected arithmetic cancellation, not a proved
independence/undecidability result.

**Baseline reproduced:** 34 native tests across gearbox source integration,
prime-window projection, signed interval certificates and internal-matrix
integration passed. No shims represented the BBP carriers. The parent hosted
CI had three successful workflows and one **cancelled** full validation run;
the latter is not evidence of passing. Full checks of this branch are recorded
separately in `PRIME_RESONANCE_VALIDATION.md`.

The attachment's proposed period compression was already MP-04, and uniform
twisted BGK cancellation was already CSI-01/02. Both are inherited. The
finite Lean work in this round adds checked generic finite reindexing, not a
new analytic estimate. The collision plan's `E=o(log N)` is sufficient but
stronger than the existing entropy target `E=N^{o(1)}` at prescribed depth.
See the [literature/coverage audit](PRIME_RESONANCE_LITERATURE_COVERAGE.md)
and [collision audit](BBP_RESONANCE_COLLISION_AUDIT.md).

The shortest dependency chain is: authentic source and covering windows;
then a signed selected-source estimate (OPEN); then the existing scale-four
descent, Green transfer, and Weyl criterion. Merely expressing the open
estimate as J, a Fourier norm, or a collision energy does not close this edge.

## 2. PRK-01: exact gcd collapse of the synchronized projection

Let Q_s be conditional averaging over indices congruent modulo s in Z/DZ,
where s divides D. For d and L dividing D, put g=gcd(d,L). Then

$$Q_dQ_L=Q_LQ_d=Q_g.$$

**Proof:** Q_s averages translations by the subgroup s Z/DZ. Composing the
two uniform subgroup averages gives the uniform average over their sum,
which is g Z/DZ. Each element of the sum has the same number of preimages
under addition, namely the cardinality of the intersection. Equivalently,
count the two congruence fibers. All divisibility hypotheses are essential;
arbitrary truncated windows are excluded.

Since Q_L u=u, self-adjointness gives Q_d u=Q_g u. With the **bilinear**
pairing B(a,b)=D^-1 sum a_t b_t, the real averaging matrices imply

$$B(Q_du,Q_dv)=B(Q_gu,Q_gv),\qquad
J_{p,d}(h)=B(u-Q_gu,Q_Lv-Q_gv)=J_{p,g}(h).$$

Thus changing a synchronized d while preserving gcd(d,L) leaves the
actual low term and J **exactly unchanged**. Extra residues relatively
prime to L do not buy another cancellation channel. Example: p=113,
L=7,D=42,d=3 has exactly the same selected J as d=1.

The canonical three-sector decomposition is

$$v=Q_gv+(Q_L-Q_g)v+(I-Q_L)v.$$

These sectors are pairwise orthogonal for the normalized complex Hilbert
inner product. The last cannot couple to any L-periodic clock. The middle
has the sharp Cauchy--Schwarz estimate

$$|J_{p,d}(h)|^2\le
\|u-Q_gu\|_2^2\,\|(Q_L-Q_g)v\|_2^2.$$

Its source energy is no larger than the original PSC high-mode dispersion
`||(I-Q_d)v||²`, since Q_L(I-Q_d)=Q_L-Q_g is a contraction. The dimensions
are L-g for the remaining sector and D-L for invisible information. The
period-lcm(d,L) construction in the attachment is valid but retains extra
information that is also invisible after coupling to u.

**Meaning of minimal:** Q_L retains exactly the information needed for
coupling to *every* L-periodic observable. For one specified u, a rank-one
functional already contains W; calling that functional a new estimate would
be circular. No decay of the retained energy or signed J is claimed. Even
an independently sampled uniform-circle complement would have expected
`||Q_Lv||²=1/B`, B=D/L, so energy decay need not occur when B stays bounded.
Haar expectation is only a hostile comparison, never the authentic source.

Implementation uses exact Q[Q/Z] PhasePoly identities, not floating roots.
These formal equalities descend to actual complex characters. Nonzero formal
polynomials need not have nonzero complex evaluations; that converse is never
used. The passport reconstructs the full rational prefix from U0=0 and checks
each primary and complementary coordinate. Source labels alone have no force.

## 3. PRK-02: a genuine forcing-imposed gap from maximal resonance

This theorem applies to the authentic source and, more generally, every
initial state following the same exact forcing. Write z_t=e(h X_(n0+t)),
A=D^-1 sum z_t, and f_t=e(h r(n0+t+1)), 0<=t<D-1. Then
z_(t+1)=z_t^16 f_t. Set K=D-1 and V=K^-1 sum |f_t-mean(f)|². We prove

$$1-|A|\ge\frac{K}{578D}V
\ge\frac{8}{289D(D-1)}
\sum_{i<j}\|h(r(n0+i+1)-r(n0+j+1))\|_{\mathbb R/\mathbb Z}^{2}.$$

**Proof:** choose a unit c in the direction of A, or any unit c if A=0.
Then sum |z_t-c|²=2D(1-|A|). The unit-circle power inequality gives
`|f_t-c^(-15)| <= |z_(t+1)-c|+16|z_t-c|`. Weighted Cauchy--Schwarz
`(a+16b)² <= 17a²+272b²`, summed over t, bounds the squared forcing
distances by 289 sum |z_t-c|². Variance minimizes squared distance to a
constant, so KV has that upper bound. Finally
`V=K^-2 sum_(i<j)|f_i-f_j|²` and
`|e(a)-e(b)| >= 4||a-b||` prove the rational second inequality.

For every fixed nonzero h and every eligible p with m>=11 and m²>=|h|,

$$\boxed{1-|W_p(h)/D|\ge\frac{h^2}{1331712m^4}.}$$

**Explicit constants:** take the m forcing samples n=m+2,...,2m+1 and
the m samples n=3m+1,...,4m. IMW-04's all-index source inequalities give

$$r(2m+1)-r(3m+1)\ge
\frac{25}{768m^2}-\frac7{40m^3}\ge\frac1{64m^2}.$$

All source differences are less than 15/(64m²), so the hypotheses on h
prevent wrapping. There are m² cross-pairs, giving the constant above.
For fixed finite p and sufficiently enormous h, rational phases can all
alias to integers; the tests explicitly demonstrate this. The quantifiers
cannot be interchanged.

This removes **perfect coherence**, and quantifies its impossibility for
the actual four-pole source. It does not exclude resonance at, for example,
normalized magnitude 1/2. The upper bound `1-c/m^4` tends to one, not zero.
It is deliberately not advertised as progress proving W=o(D).

## 4. PRK-04: the m^-4 boundary is optimal without the initial selector

The [adversarial dossier](BBP_RESONANCE_OBSTRUCTIONS.md) constructs for
each p an entirely rational initial state c_p with odd denominator coprime
to p. It uses only the finite original state U_(4m), not supplied pi digits:

$$q=2pm^2 16^{4m}+1,\qquad
c_p=\text{nearest }a/q\text{ to }-U_{4m}/16^{4m},\qquad
X_n=U_n+16^n c_p.$$

Every forcing step is authentic, and the full p-primary birth clock is
unchanged. All complementary denominators remain odd and p-free. On the
whole window, |X_n|<1/(32m²), and

$$1-\left|\frac1{3m}\sum_{n=m+1}^{4m}e(hX_n)\right|
<\frac{121h^2}{6272m^4}.$$

Together with PRK-02 this pins the smallest possible modulus deficit over
this enlarged initial-state class to order m^-4. The construction changes
**exactly the initial-state authentication gate**. Other primes' residue
histories can change. A different c_p is selected for each window; this is
not a fixed rational counterexample to pi normality or Hypothesis A.

The stronger asymptotic coefficient, proved in the companion dossiers, is
`m^4(1-|A_changed|) -> 3*pi^2*h^2/131072`. Its proof is a uniform source-tail
expansion and a Riemann-sum variance calculation, not extrapolated numerics.
The fully source-authenticated case c=0 remains outside this obstruction's
conclusion. Any successful stronger cancellation argument must use how that
specific state is selected, or some property that genuinely fails here.

### A second-round inverse theorem makes the surviving mechanism explicit

Let a>0 be rational, T=D-1, and
`34a+|h|(r(m+2)-r(4m))<1`. If the window's normalized modulus deficit is
at most 8a²/D, its starting circle phase must lie in one of 15|h| arcs with

$$\text{center}_j=\frac{j}{15|h|}
-\sum_{k=1}^{T}16^{-k}r(n0+k),\qquad
R=\frac{32a+|h|r(4m)}{15|h|16^T}.$$

The [full finite proof](BBP_RESONANCE_OBSTRUCTIONS.md) first bounds every
phase's displacement from the character mean. The interval-width hypothesis
then forces a single integer branch in the lifted recurrence. Solving that
recurrence backwards gives these exact rational centers and radius. This
classifies a source-compatible mechanism of extreme resonance with exponential
initial-phase precision. At order-m^-4 deficit its radius is
O_h(16^(-3m)m^(-3/2)).

The actual source starts outside these arcs at the recorded finite holdouts;
the same-forcing tuned controls lie inside. Neither the converse nor
all-prime avoidance is claimed. This theorem requires deficit O(1/D) or
smaller, so it does not classify the full nonvanishing-correlation regime.
It is an exact inverse estimate, not a probability argument based on the
arcs' tiny total length.

## 5. PRK-05/06: lag differentiation has a source cost, not automatic descent

The [lag dossier](BBP_RESONANT_LAG_DESCENT.md) proves the full birth-cut
formula for P(E)=product(E^k-1). Every such nonempty filter retains the
state multiplier P(16)>0. A fresh q=1 mod8 born at its final endpoint has
primary residue exactly 4. In the authentic source itself, U6-U4 removes
the 17-primary clock while retaining the fresh 41-primary residue 4.

The new mixed-tail bound is useful and uniform in all positive lags:

$$|P(E)T_n|<\min\left\{\frac1{(8n+1)(8n+2)},
\frac{8^s(\prod_i k_i)(s+1)!}{\prod_{a=1}^{s+2}(8n+a)}\right\}.$$

It transports the differentiated source to completed-circle frequency
hP(16). Cancellation at that growing frequency remains unproved. Eliminating
one prime while introducing fresh primes is not a conductor descent theorem.

## 6. Collision bearing and adversarial coverage

The [collision dossier](BBP_RESONANCE_COLLISION_AUDIT.md) gives an explicit
finite Fourier-ladder inequality with all recurrence and cell errors paid.
It also rounds anti-phases on each authentic complementary denominator's
own grid. No larger denominator or new prime is needed to make every fake
phase occupy the same polynomial-scale cell. That control fails the actual
recurrence; denominator growth alone therefore cannot supply anti-concentration.

Controls cover: exact anti-phase; odd p-free rational approximations;
same forcing with altered initial state; one changed impulse with unchanged
tail; small orders; unsynchronized d; exceptional primes 3 and 5;
wrong signed forcing; large-period weights; a deterministic finite Haar-grid
analogue in the replay; and increasing authentic windows with no fitted rate.
None is relabelled an authentic source. No finite trend proves decay.

## 7. Next dependency cut and cross-session use

The exact new interface to the Gram session is the selected Fourier window
W and its gcd-reduced interaction, with the pre-existing O_h(m^-2) normalized
Green transfer and the correctly quantified scale-four coverage. The new
gap is a strict *lower bound on the deficit from one*, not an upper bound
tending to zero for a Fourier coefficient; it cannot close spectral purity.

The next decisive target is an estimate depending on the true zero-initial
prefix and its cross-time numerators: either signed J on the reduced L-g
sector, or the more permissive prescribed-scale trimmed collision estimate.
A candidate must simultaneously reject the odd same-forcing selector control
and the allowed-conductor counterfeit for an explicit mathematical reason.
Trying additional d with the same gcd, repeating twisted BGK, or calling an
old-prime cancellation a global conductor descent now has a precise failure
receipt. This is the earned boundary, not a claim that no further proof exists.
