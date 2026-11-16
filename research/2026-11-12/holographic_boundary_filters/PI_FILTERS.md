# A boundary filter aimed directly at the weakest signed pi rung

**Status:** elementary local inequalities and an exact finite experiment.
Uniform R0 and pi base-16 normality remain **OPEN**. This is a target-relative
certificate, not a new proof of an arithmetic asymptotic estimate.

## 1. Keep the actual source and the actual target

Use Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`,
[`duck_bbp.py`](../../../observational_succ/duck_bbp.py) and
[`MAIN_XXV_HANDOFF.md`](../../../docs/MAIN_XXV_HANDOFF.md):

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Let `x=pi/16`, `Y_n=16^n x`, `T_n=sum_(j>=1)16^(-j)r(n+j)`.
The classical BBP identity and exact recurrence give

\[
Y_n=U_n+T_n,\qquad 0<T_n\le\frac{47}{225(n+1)^2}.
\tag{PF1}
\]

The identity with geometric pi is an imported theorem, not established by
the new Python experiment. The tail bound follows from the source inequality
`0<r(m)<=47/(15m^2)` and summing a geometric series. The exact rational
source and these bounds already exist in the pinned repository; they are not
new claims here. The script's combined rational formula is independently
checked against all four signed poles on finite calibration values.

For an integer `B>=1`, define

\[
W_B(1)=\frac1B\sum_{n=B}^{2B-1}e(Y_n),\quad e(t)=e^{2\pi i t},\qquad
\Delta_B=1-\Re W_B(1).
\]

R0 is the assertion `liminf_(B->infinity) Delta_B>0`. This target is weaker
than all-mode Weyl cancellation. It requires the phase origin: a point mass
at `1/15` has a positive signed gap at mode one but Fourier magnitude one.
An unanchored power spectrum cannot distinguish that point mass from the
coherent point mass at zero. Conversely, **if all nonzero Fourier powers of
the selected empirical laws tend to zero, that does suffice for normality**.
The phase-loss counterexamples in this dossier are not a denial of that fact.

## 2. PF-01: a rational minorant and its exact tail payment — PROVED LOCAL

Write `d(t)=dist(t,Z)`, in `[0,1/2]`. Concavity of sine on `[0,pi/2]` and
`sin u<=u` give, for every real `t`,

\[
8d(t)^2\le 1-\cos(2\pi t)\le 2\pi^2d(t)^2.
\tag{PF2}
\]

Also `d` is 1-Lipschitz for the circle metric and `d(x)+d(y)<=1`, hence

\[
|d(x)^2-d(y)^2|\le d_{\mathbb T}(x,y)\le |x-y|.
\tag{PF3}
\]

For `q>=2`, define cells `I_a=[a/q,(a+1)/q)`, `0<=a<q`, and

\[
g_q(t)=8\left[\frac{\min(a,q-a-1)}q\right]^2\quad(t\in I_a).
\tag{PF4}
\]

This is the minimum of `8d(t)^2` on the closed cell. Suppose a source-valid
certificate assigns `c_a` distinct shell indices to cell `I_a`, leaves `u`
indices unresolved, and `sum_a c_a+u=B`. Define

\[
L_{B,q}=\frac1B\sum_a c_a\,8\left[\frac{\min(a,q-a-1)}q\right]^2.
\]

Then

\[
\boxed{\Delta_B\ge
\max\left(0,L_{B,q}-\frac{376}{225(B+1)^2}\right).}
\tag{PF5}
\]

**Proof.** Every resolved index contributes at least its cell minimum to
`8d(U_n)^2`; unresolved indices contribute a nonnegative amount, so discarding
them is safe. By PF3, replacing each `U_n` by `Y_n` costs at most `8T_n`.
Their average is at most `8*47/[225(B+1)^2]` by PF1. Apply the lower half of
PF2 and the unconditional nonnegativity of `Delta_B`. No floating sine,
cosine, pi digits, or statistical assumption is used. QED.

**Error/refinement statement.** For the exact complete counts,
`0<=8d(t)^2-g_q(t)<=8/q`, since `d^2` is 1-Lipschitz. If `q'` is an integer
multiple of `q`, then `g_(q')>=g_q` pointwise. With unresolved intervals the
same monotonicity holds when a refined interval is either uniquely classified
or contained in an unresolved coarse interval: if a coarse interval is
resolved but a refined one straddles a seam, simply discarding the latter
can lose the coarse lower bound. The present experiment has no unresolved
cells; it therefore verifies the uncomplicated exact-refinement case.

For applications that need monotonicity with unresolved mass, keep the
maximum of the coarser certified lower bounds or minimize the minorant over
all cells intersecting each interval. Do not silently assume unresolved
mass vanishes at all future epochs.

**Novelty boundary.** The inequalities are elementary and the tail transfer
is already part of SUCC's architecture. The result of this round is their
integration as a source-bound, phase-anchored, exact target certificate with
an auditable error budget. It is a reformulation/interface for R0; no
independent arithmetic saving has been obtained.

## 3. PF-02: integer enclosure of the expanding source — PROVED LOCAL

Fix a final index `N`, an integer guard `g>=1`, and `S=2^(4N+g)`.
Represent a circular interval by `[a_n/S,(a_n+w_n)/S] modulo one`, with
`0<=a_n<S`, and start with `a_0=w_0=0`. Write

\[
Sr(n)=f_n+\theta_n,\quad f_n=\lfloor Sr(n)\rfloor,\quad 0\le\theta_n<1.
\]

Update

\[
a_n=(16a_{n-1}+f_n)\bmod S,\qquad
w_n=16w_{n-1}+\mathbf1_{\theta_n\ne0}.
\tag{PF6}
\]

**Theorem.** For all `0<=n<=N`, the interval contains `{U_n}` and

\[
0\le w_n\le\frac{16^n-1}{15},\qquad
\frac{w_n}{S}<\frac{2^{-g}}{15}.
\tag{PF7}
\]

**Proof.** If `U_(n-1)=a_(n-1)/S+e+k`, with `0<=e<=w_(n-1)/S`
and integer `k`, then after the step the rounding error is
`16e+theta_n/S`, within the new width. Reducing the lower endpoint changes
only an integer lift. The width inequality follows by induction from
`w_n<=16w_(n-1)+1`. Dividing by `S` proves PF7. This accounts for the source's
exponential sensitivity rather than ignoring it. QED.

The code assigns a cell only if both closed endpoints have the same
unwrapped `q`-cell number in `0,...,q-1`; otherwise it reports unresolved.
This conservative rule handles wraparound and cell seams. At an exact right
endpoint it may withhold a classification, which costs power, not soundness.
Using only the first endpoint would be unsound.

This is not constant-memory or a claimed acceleration theorem. The stored
integers have `4N+g` bits, the experiment advances `N` times, and arithmetic
cost depends on that bit length. A finite low-dimensional update is not an
infinite precision free resource.

## 4. Frozen finite experiment

Inputs were fixed in [PREREGISTRATION.md](PREREGISTRATION.md): calibration
`B=32,64`; evaluation `B=137,271,547,1091`; every `q=16,32,64`; guard 48 bits.
The maximum index is 2181. Source observations come from PF6, never from a
supplied expansion of pi. The exact rational results and full count vectors
are in [PI_RESULTS.json](PI_RESULTS.json).

The following decimals are displays of **rational lower bounds** for
`1-Re W_B(1)`, including the tail payment. They are not estimates of the
actual cosine means.

| B | q=16 | q=32 | q=64 | unresolved cells (all three) |
|---:|---:|---:|---:|---:|
| 32 | 0.519949838 | 0.575858041 | 0.609244271 | 0 |
| 64 | 0.569916971 | 0.638886697 | 0.671113260 | 0 |
| 137 | 0.569939622 | 0.637800024 | 0.666925822 | 0 |
| 271 | 0.581850106 | 0.640833040 | 0.671859620 | 0 |
| 547 | 0.567121949 | 0.627236780 | 0.658958101 | 0 |
| 1091 | 0.522741495 | 0.577307260 | 0.607060640 | 0 |

No grid was tuned after viewing these values. The new evaluation windows
were fixed in this research session; they are not externally blinded
holdouts. Neither their agreement nor the use of exact arithmetic estimates
the probability of R0 being true. The rational certificate is decisive only
for the explicitly enumerated shells.

## 5. The source-specific hole left open

The shortest remaining implication in this interface is

\[
\exists q,c>0,B_0\quad\forall B\ge B_0:\quad L_{B,q}\ge c
\quad\Longrightarrow\quad\mathrm{R0}.
\tag{PF8}
\]

The constants are fixed before sending `B` to infinity. A theorem proving
PF8's premise must use the original-zero arithmetic source. It cannot follow
from recurrence syntax, source reconstruction, positivity, fixed finite
tests, or asymptotic vanishing of the forcing alone. In fact, with exact
counts and variable choice of fixed `q`, PF2--PF4 make this another form of
R0. It is explicitly **not** an independently weaker arithmetic hypothesis.

What has changed is the research instrument: a positive answer can now be
an exact dual certificate for one target, with no need for full phase-law
reconstruction or a poorly conditioned bispectrum inverse near Haar.
One can propose a source-specific inequality for a fixed filter and try to
prove it. Until such an inequality is proved uniformly, the ledger stays
OPEN at R0, all higher signed rungs, and pi normality.

The coherent completed orbit at zero has no positive escape certificate.
A periodic grid can have a positive finite certificate while being
nonnormal. These are deliberate negative controls on the inference from a
finite successful filter to an infinite statistical law.
