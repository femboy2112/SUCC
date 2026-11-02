# FRONT 3 — Large-sieve / second-moment structure, hostile controls, corrected finite calibration

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02` (off `origin/main` `81045770`).
**Agent:** Ravel (main thread). **Scope:** exact second-moment decomposition of the prime-window
sieve object, conductor-based analysis of the off-diagonal, four hostile controls with CORRECT
precision, and a scoped claim ledger. **No normality claim, no unproven bound.** π base-16
normality and RH remain OPEN.

---

## 0. Objects and one exact identity (recapitulated, PROVED)

For a prime $p\equiv 5 \pmod 8$, $5<p\le X$:

$$
a_p=\frac{p+3}{8},\qquad b_p=\frac{p+1}{2}-1,\qquad |W_p|=b_p-a_p+1=\frac{3p+1}{8}.
$$

The window "phase × cofactor" factorization

$$
e\!\left(-\frac{h\,16^{n-a_p}}{p}\right)e(hV_{p,n}),\qquad V_{p,n}=U_n+\frac{16^{n-a_p}}{p}
$$

is the identity $e(hU_n)=e(hU_n)$ in disguise: since $U_n=16^{n-a_p}U_{a_p}+W_{p,n}$ and the two
factors share the radix multiplier $16$, the product collapses to a single term. Verified exactly
(Fraction) for $p=13$, all $n\in[2,6]$: $-16^{n-a_p}/p + V_{p,n} = U_n$ term-by-term. Hence

$$
\boxed{R_p(h)=\sum_{n=a_p}^{b_p}e(hU_n)=S_{b_p}(h)-S_{a_p-1}(h),\qquad S_N(h)=\sum_{n=1}^N e(hU_n).}
$$

$R_p(h)$ is a **suffix block of the authentic Weyl sum**, not a new object. This agrees with the
sibling structural front (`CORE_ANALYSIS.md`, T-3); we now open the square.

---

## 1. Exact second-moment decomposition (PROVED, elementary)

Open $|R_p|^2$ over $n,m\in[a_p,b_p]$ and then sum over $p$:

$$
\sum_{p}|R_p(h)|^2
=\underbrace{\sum_p\sum_{n=m}e(h(U_n-U_m))}_{\text{diagonal }=\sum_p|W_p|}
+\underbrace{\sum_p\sum_{\substack{n\neq m\\ n,m\in[a_p,b_p]}}e(h(U_n-U_m))}_{\text{within-prime off-diagonal}}.
\tag{M1}
$$

Because the windows $\{[a_p,b_p]\}$ **overlap** (a single time $n$ lies in $\sim n/\log n$ windows
$\{p:2n+1\le p\le 8n-3,\ p\equiv5\,(8)\}$), the same ordered pair $(n,m)$ is counted once per
window containing both; the off-diagonal therefore carries a **cross-prime multiplicity**
$\sim\min(n,m)/\log\min(n,m)$ weighting the same two-time phase $e(h(U_n-U_m))$. In full:

$$
\sum_p|R_p(h)|^2=\sum_{n\le m} w_X(n,m)\,e(h(U_n-U_m)),\qquad
w_X(n,m)=\#\{p\le X:\ a_p\le n,m\le b_p,\ p\equiv5\,(8)\},
\tag{M2}
$$

with $w_X(n,n)=|W_p|$ on the diagonal (recovered from $w_X$ by summing the diagonal over $p$).

### 1.1 Diagonal term — corrected constant

$$
\sum_p|W_p|=\sum_{5<p\le X,\ p\equiv5\,(8)}\frac{3p+1}{8}
=\frac38\sum_p p+\frac18\cdot\#\{p\}
=\frac38\cdot\frac{X^2}{8\log X}\Big(1+o(1)\Big)
=\boxed{\frac{3}{64}\frac{X^2}{\log X}\big(1+o(1)\big)}.
\tag{D1}
$$

**Correction to the handoff (and to sibling `CORE_ANALYSIS.md` §3, `FRONT_1_BGK.md` §2.3).** The task
statement and both sibling fronts give $\sum_p|W_p|\sim\frac38 X^2/\log X$ and
$\sum_p|W_p|^2\sim\frac{3}{64}X^3/\log X$. These omit the $\phi(8)=4$ class-density factor: the sum is
over primes $p\equiv5\pmod8$, which form $1/4$ of all primes. The correct constants are

$$
\boxed{\sum_p|W_p|\sim\frac{3}{64}\frac{X^2}{\log X},\qquad
\sum_p|W_p|^2\sim\frac{3}{256}\frac{X^3}{\log X}.}
\tag{D2}
$$

(For the square: $|W_p|^2=\frac{9p^2+6p+1}{64}$, $\sum_p p^2\sim X^3/(3\log X)$ overall, $\times\frac14$
for the class, $\times\frac{9}{64}$ for the leading coefficient $=\frac{9}{64}\frac{X^3}{12\log X}
=\frac{3}{256}\frac{X^3}{\log X}$.) Numerically verified (exact Fraction) to ratio $\to1$ at
$X=10^5$: $1.0409$ for the linear, $1.0204$ for the quadratic — the $o(1)$ is the usual
$1/\log$-type error. The handoff's numbers are $4\times$ and $16\times$ too large respectively.
**Note the handoff's own numbers are also internally inconsistent:** $\frac{3}{64}X^3/\frac{3}{8}X^2
=\frac{X}{8}$ would imply average window length $X/8$, whereas the true average $|W_p|$ is
$\frac{3}{16}X$ — a further $2\times$ mismatch confirming the constants are not self-consistent.

### 1.2 Trivial bound and what $(\log X)^{-\eta}$ means

The trivial bound (every $|R_p|\le|W_p|$, i.e. all phases coherent) is

$$
\sum_p|R_p|^2\le\sum_p|W_p|^2\sim\frac{3}{256}\frac{X^3}{\log X}.
\tag{T}
$$

The conjecture asserts a saving

$$
\sum_p|R_p|^2\ \ll\ \frac{3}{256}\frac{X^3}{\log X}\cdot\frac{1}{(\log X)^{\eta_h}}
\tag{C}
$$

for some $\eta_h>0$. Since the diagonal $\sum_p|W_p|\sim\frac{3}{64}\frac{X^2}{\log X}$ is
$=O(X^2/\log X)\ll X^3/(\log X)^{1+\eta}$, the **entire saving must come from the off-diagonal**:
(C) is equivalent to

$$
\underbrace{\sum_{p}\sum_{n\neq m\in[a_p,b_p]}e(h(U_n-U_m))}_{\text{within-prime}}
+\ \text{(cross-prime multiplicities)}\ \ \ll\ -\Big(1-o(1)\Big)\frac{3}{256}\frac{X^3}{\log X},
\tag{O}
$$

i.e. the off-diagonal (which is real, being $\sum_{n\neq m}2\cos(2\pi h(U_n-U_m))$ for $n<m$)
must itself be $o\!\left(X^3/\log X\right)$, of size at most the trivial bound divided by a log-power.
This happens only if the off-diagonal unit-modulus terms $e(h(U_n-U_m))$ **cancel internally** —
their signed sum is far smaller than their count. **The conjecture's $(\log X)^{-\eta}$ is
therefore exactly a claim of signed cancellation in the two-time phase
$\sum e(h(U_n-U_m))$**, the single bottleneck the entire program targets (cf. `CORE_ANALYSIS.md`,
§3). It is *not* a claim about any new prime-specific structure: the prime windows merely re-weight
the same two-time correlation by $w_X$.

---

## 2. Conductor analysis of the off-diagonal (PROVED, structural)

For fixed lag $L=m-n\ge1$, CG-06 (`arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md`) gives

$$
\boxed{\log\operatorname{den}(U_{n+L}-U_n)=6n+o(n).}
\tag{CG}
$$

Equivalently the reduced denominator of the off-diagonal phase is $\exp(6n+o(n))$. What does this
do to cancellation?

- **It neither forces nor forbids cancellation.** A phase $e(hx)$ with $\operatorname{den}(x)=q$
  can point anywhere on the unit circle; a huge denominator is *compatible with* any real phase
  (the conductor proof itself stresses this). CG-06 is a statement about the *rational grid
  complexity* of the exact orbit, not about the *distribution* of $h(U_n-U_m)\bmod1$.
- **It does exclude one mechanism.** A polynomial-size denominator $q=\mathrm{poly}(n)$ would admit
  a Stoneham-style stage certificate (bounded per-stage multiplicity → signed bound via complete
  periods of a short clock). The exponential conductor **forbids that architecture** (this is the
  TR-03/CG-02 exact-grid obstruction): no fixed lag $\ell$ has a polynomial-period clock. So the
  cheap route — a short-period modular clock whose Gauss sum is $\sqrt p$ — is unavailable for the
  *within-prime off-diagonal*, because the off-diagonal phase is not $p$-periodic in a window-local
  sense; it is the full $U_n-U_m$ difference.
- **What would have to be true for cancellation.** Cancellation in $\sum_{n\neq m}e(h(U_n-U_m))$
  requires the *real-circle* phases of $U_n-U_m$ to be equidistributed (or at least to have
  non-positive signed autocorrelation), which is precisely the Weyl-type fact
  $\sum_{n\le N}e(hU_n)=o(N)$. The conductor $\exp(6n)$ is *consistent with* this (rapidly mixing
  real phases have huge rational complexity) but gives no estimate on its own.

**Bottom line: the exponentially growing conductor is a *negative* result — it rules out the
easy modular-period certificate — and is silent on the actual signed cancellation, which remains
the open Weyl bound.**

---

## 3. Hostile controls — CORRECT precision (OBSERVED FINITE)

### 3.1 Precision discipline

$e(hU_n)$ has phase $hU_n$ with $\operatorname{den}(U_n)=\exp(6n+o(n))$. The phase is computed
**exactly as an integer residue** $k=(h\cdot\text{num}(U_n))\bmod\text{den}(U_n)$, then $\cos,\sin$
evaluated in mpmath at

$$
\mathrm{dps}\ge\frac{6N_{\max}}{\ln10}+60,\qquad N_{\max}=\frac{X+1}{2}-1.
$$

Two independent methods are cross-checked at every $X$: (i) exact residue $e^{2\pi i k/q}$, and
(ii) high-precision float $U_n$ with $e^{2\pi i h U_n}$. Agreement:

| X | $N_{\max}$ | dps | $|e_1-e_2|$ at $n=N_{\max}$ |
|---|---|---|---|
| 256 | 127 | 390 | $9.8\times10^{-280}$ |
| 512 | 255 | 724 | $1.6\times10^{-458}$ |
| 1024 | 511 | 1391 | $1.0\times10^{-817}$ |

The two methods agree to $\sim$$-\mathrm{dps}$ digits, i.e. **exactly**. No coherence artifact.

### 3.2 The four controls, $h=1$

| control | construction (exact) | expected | observed $M/T$ at $X=$ 256 / 512 / 1024 |
|---|---|---|---|
| **authentic** | $U_n$ four-pole, $U_0=0$ | unknown (the target) | **0.01995 / 0.00891 / 0.00353** |
| **(a) coherent** $s^*=-\pi/16$ | $U_n=-T_n$, $T_n=\sum_{j\ge1}16^{-j}r(n+j)>0$, $T_n<(8n+1)^{-2}$ | $e(-hT_n)\to1$ ⇒ $M/T\to1$ | **1.000000 / 1.000000 / 1.000000** |
| **(b) all-zero** forcing | $r(n)\equiv0$ ⇒ $U_n\equiv0$ | $M/T=1$ | **1.000000 / 1.000000 / 1.000000** |
| **(c) Haar (random)** | i.i.d. uniform phases | $M/T\sim 1/\langle|W_p|\rangle$ | **0.01195 / 0.00408 / 0.00116** |
| **(d) $p=257$ clock** | $U_n=4\cdot16^n/257$, $\operatorname{ord}_{257}(16)=4$ | $M/T\to|\text{mean}|^2\approx0.2507$ | **0.25399 / 0.25283 / 0.25166** |

($T=\sum_p|W_p|^2$ is identical across all controls — it depends only on window lengths. $M/T$
is therefore a genuine normalized signed-cancellation measure.)

### 3.3 Does the saving distinguish them? — YES, sharply.

Scaling of $M/T$ under $X\mapsto 2X$ (doubling ratios):

| control | $256\to512$ | $512\to1024$ | verdict |
|---|---|---|---|
| authentic | 2.24 | 2.52 | decays $\approx 1/X$ (i.e. $\sim1/|W_p|$) |
| coherent / allzero | 1.00 | 1.00 | constant 1, no cancellation |
| Haar | 2.93 | 3.50 | decays $\approx1/|W_p|$ (random-phase variance) |
| clock | 1.005 | 1.005 | **constant** $\approx0.254$, partial but *non-decaying* cancellation |

**Three clean separations.**

1. **Coherent & all-zero are saturated at 1** — no saving whatsoever, as required (they *must*
   fail any normality-type criterion).
2. **The clock is constant $\approx1/4$** — the period-4 clock gives a *bounded* partial
   cancellation (full-period mean $\ne0$: residues $\{64,253,193,4\}\bmod257$ have mean magnitude
   $\approx0.5007$, $|\text{mean}|^2=0.25067$), and it **does not decay** with $X$. This is the
   sharpest discriminator: a periodic orbit cannot produce the $(\log X)^{-\eta}$ saving, because
   its $M/T$ is pinned at $|\text{mean}|^2$.
3. **Authentic decays like $1/X$**, statistically indistinguishable from the Haar random seed at
   these ranges, and *much faster* than the conjecture's weak $(\log X)^{-\eta}$.

### 3.4 Brutal honesty about what this proves

- $M/T\sim1/X$ for the authentic orbit is **consistent with normality**, and it is *far stronger*
  than what the conjecture needs. But it is a **finite** observation over $X\le1024$ (44 primes,
  $N_{\max}=511$); it cannot distinguish $1/X$ from $1/(\log X)^{\eta}$, nor from any mild decay,
  and it is **not a proof** of any asymptotic.
- The conjecture's $(\log X)^{-\eta}$ is the *weakest* conceivable saving. The observed decay is
  consistent with the conjecture but does not confirm its sharpness — it suggests the truth is
  stronger (near $1/X$), which is exactly the Weyl bound $S_N(h)=o(N)$ in another shape.
- The controls confirm the **criterion is sound** (it saturates coherent inputs at 1 and pins
  periodic inputs at $|\text{mean}|^2<1$), but no control *proves* the authentic bound. A periodic
  clock with a huge period (e.g. a long-period linear congruential orbit) would also show small
  $M/T$ over a finite range and fool this finite test; only the $X\to\infty$ limit can settle it.

---

## 4. Claim ledger

| ID | Claim | Status | Evidence / obligation |
|---|---|---|---|
| F3-01 | $R_p(h)=\sum_{n=a_p}^{b_p}e(hU_n)$; the clock×cofactor factorization is the identity $e(hU_n)$ | **PROVED** exact elementary | exact Fraction check $p=13$; tower identity $U_n=16^{n-a_p}U_{a_p}+W_{p,n}$ |
| F3-02 | $\sum_p|R_p|^2=\sum_p|W_p|+\sum_p\sum_{n\ne m}e(h(U_n-U_m))$; cross-prime multiplicity $w_X(n,m)$ in (M2) | **PROVED** exact | open the square; window overlap cardinality $\sim n/\log n$ |
| F3-03 | diagonal $\sum_p|W_p|\sim\frac{3}{64}\frac{X^2}{\log X}$; $\sum_p|W_p|^2\sim\frac{3}{256}\frac{X^3}{\log X}$ | **PROVED** (PNT in AP) | corrects handoff's $\frac38,\frac{3}{64}$ (missing $\phi(8)=4$); verified to ratio $\to1$ |
| F3-04 | $(\log X)^{-\eta}$ saving is equivalent to signed cancellation in $\sum e(h(U_n-U_m))$ off-diagonal | **PROVED** (restatement) | diagonal is $O(X^2/\log X)\ll$ trivial bound |
| F3-05 | conductor $\log\mathrm{den}(U_{n+L}-U_n)=6n+o(n)$ neither forces nor forbids off-diagonal cancellation; it *excludes* the polynomial-period Stoneham stage certificate | **PROVED** structural (CG-06) | huge denominator compatible with any real phase; no $p$-periodic window clock |
| F3-06 | coherent $s^*=-\pi/16$ ⇒ $M/T\to1$; all-zero ⇒ $M/T=1$; clock-257 ⇒ $M/T\to0.25067$; Haar ⇒ $M/T\sim1/|W_p|$ | **PROVED** (each control's own arithmetic) | exact $T_n$ tail, exact residue clock, exact Gauss mean |
| F3-07 | authentic $M/T$ decays $\approx1/X$ over $X\le1024$, matches Haar, beats clock and coherent controls | **OBSERVED FINITE** (correct precision, two methods agree) | finite $X\le1024$; cannot be promoted to an asymptotic |
| F3-08 | The conjecture $\sum_p|R_p|^2\ll X^3/(\log X)^{1+\eta}$ is provable by these methods | **UNVERIFIED / OPEN** | no finite control, no conductor argument, proves the Weyl bound $S_N=o(N)$; this *is* the single bottleneck |
| F3-09 | $\pi$ base-16 normality or RH follows from F3-07 | **NOT CLAIMED** | finite; normality & RH OPEN |

---

## 5. Cheapest next step

The decomposition (M2) reduces the conjecture to a **two-time signed correlation bound** with
weight $w_X(n,m)\asymp\min(n,m)/\log\min(n,m)$. The single cheapest falsifiable obligation is
unchanged: exhibit or refute

$$
\sum_{1\le n<m\le N}e(h(U_n-U_m))=o(N^2)
$$

for the authentic orbit — equivalently $S_N(h)=o(N)$ — because (M1)–(M2) and F3-04 show the
prime-window sieve adds *no* new handle beyond this. The controls confirm the criterion separates
coherent/periodic/random inputs; they do not close the authentic gap. **No merge, no push, no
normality claim.**

## 6. Reproducibility

```sh
cd research/2026-11-02/prime_cofactor_attack
python3 front3_compute.py        # writes front3_results.json (exact Fraction + residue phases)
```

Dependencies: stdlib `fractions`, `mpmath`. No floating-point phase input; all phases are exact
integer residues evaluated in mpmath at $\mathrm{dps}\ge6N_{\max}/\ln10+60$.
