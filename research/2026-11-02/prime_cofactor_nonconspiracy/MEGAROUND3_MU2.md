# MEGAROUND3-MU2 — the cofiber increment energy $\mu_2(h)$: exact computation, scaling, and the firewall

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`
**Agent:** Ravel (main)
**Date:** 2026-11-02
**Status:** computation + analysis complete; **no new unconditional bound claimed**.

---

## 0. What this round establishes (and what it does not)

- **Established (exact finite computation):** over all $210$ primes $p\equiv1\pmod4$, $p<3000$, the cofiber-increment energy
  $$\mu_2(h)=\frac1{L-1}\sum_{r=0}^{L-2}\sin^2\!\big(\pi h\delta_{p,r}/2\big),\qquad L=\operatorname{ord}_p(16),$$
  is **$\approx 1/2$ on average, with no decay in $L$ and no dependence on $h\in\{1,3,5\}$.** The delta-phase $\{\delta_{p,r}\}$ is empirically uniformly distributed $\bmod 1$.
- **Not established (and NOT claimed):** any unconditional *proof* that $\mu_2(h)\to1/2$ or that $\mu_2(h)=o(1)$. The empirical value $1/2$ is precisely the **random-phase signature**, which is *equivalent in difficulty* to the $\pi$-digit Weyl cancellation $S_N(h)=o(N)$ — the open gate. See §4–§5.

**Bottom line (brutal honesty):** $\mu_2(h)\approx1/2$ is *observed* and is the signature of uniform phase; it is **not source-derivable** from any theorem in this dossier, and a *proved* bound of the form $\mu_2(h)\ge c>0$ (or $=1/2+o(1)$) would be exactly as hard as $\pi$ base-16 normality. A bound $\mu_2(h)\le c<1/2$ is **empirically false** on the authentic orbit.

---

## 1. Exact definitions (recapitulated and pinned)

All objects are those of the PCN dossier (verified against `mega_round_engine.py` and `THEOREMS_AND_PROOFS.md` §1.3).

- Authentic BBP orbit: $U_0=0$, $U_{j+1}=16U_j+r(j+1)$, with the four-pole signed forcing
  $$r(n)=\frac{4}{8n-7}-\frac{2}{8n-4}-\frac{1}{8n-3}-\frac{1}{8n-2}.$$
- For $p\equiv1\pmod4$: birth step $b_p=(p+7)/8$ if $p\equiv1\pmod8$ else $(p+3)/8$; birth numerator $c_p=4$ if $p\equiv1\pmod8$ else $p-1$; primary residue $a_{p,j}\equiv c_p\cdot16^{j-b_p}\pmod p$; cofiber $W_{p,j}=U_j-a_{p,j}/p\in\mathbb Z_{(p)}$.
- Carry digit $\kappa_{p,j}=\lfloor16\,a_{p,j}/p\rfloor\in\{0,\dots,15\}$.
- **Cofiber increment (the object):**
  $$\delta_{p,r}:=W_{p,b_p+r+1}-W_{p,b_p+r}=15\,W_{p,b_p+r}+r(b_p+r+1)+\kappa_{p,b_p+r}.$$
  The second equality is the *exact* recurrence identity $W_{j+1}-W_j=15W_j+r(j+1)+\kappa_j$ (PCN-01), verified symbolically and numerically below.
- $D_{p,h}(r)=e(h\delta_{p,r})-1$, $|D_{p,h}(r)|^2=4\sin^2(\pi h\delta_{p,r}/2)$, and by Parseval
  $$\sum_{\ell=0}^{L-1}\big|\widehat D_{p,h}(\ell)\big|^2=\frac1L\sum_{r=0}^{L-2}|D_{p,h}(r)|^2=\frac4L\sum_{r=0}^{L-2}\sin^2(\pi h\delta_{p,r}/2).$$

### 1.1 Normalization flag (important, honest)

The task text defines $\mu_2(h)=\frac1{L-1}\sum_r\sin^2(\pi h\delta_{p,r}/2)$ (argument **halved**), while PCN-03 §1.3 defines $\mu_2(h)=\frac1{L-1}\sum_r\sin^2(\pi h\delta_{p,r})$ (argument **not halved**). These are *different* functionals. We compute **both** and label them unambiguously:

- `mu2_half(h)` $=\frac1{L-1}\sum\sin^2(\pi h\delta_{p,r}/2)$ — matches the task statement and $|D|^2$ via Parseval.
- `mu2_full(h)` $=\frac1{L-1}\sum\sin^2(\pi h\delta_{p,r})$ — matches the PCN-03 §1.3 definition and the engine's `mu2_sum`.

**Empirically both are $\approx1/2$** (see §3), because $\{\delta\}$ is uniform, and for uniform $\delta$, $\int_0^1\sin^2(\pi h x)\,dx=\int_0^1\sin^2(\pi h x/2)\,dx=1/2$ for integer $h$. The distinction does not change the conclusion, but it *must* be flagged: the two formulas are not interchangeable at finite $L$ for fixed phase.

---

## 2. Method (two independent exact engines + cross-validation)

**Method A** — recurrence: $\delta_{p,r}=W_{b_p+r+1}-W_{b_p+r}$, with $W=U-a/p$ built from *exact* `Fraction` rationals (`U` via $U_{j+1}=16U_j+r(j+1)$; `a` via exact modular `pow`).

**Method B** — closed form: $\delta_{p,r}=15W_{b_p+r}+r(b_p+r+1)+\kappa_{b_p+r}$, again all exact `Fraction`.

Both feed `mpmath.sin` at `dps = 2000` (task requires $\ge 6 N_{\max}/2.3=1927.8$, where $N_{\max}=\max_p\operatorname{ord}_p(16)=739$). **Assertion:** `Method A == Method B` exactly (rational equality, not float) for every $(p,r)$; the two $\sin^2$ accumulations agree to $>12$ digits.

**Cross-validation (third party):** for $p=17,h=1$, our `mu2_full` $=0.3069833885$ reproduces exactly the value inferred from the existing `mega_round_engine.py` Cauchy–Schwarz bound $2\sqrt{\frac{L}{L-1}\mu_2}$ (inferred $\mu_2=0.3069833885$). Independent confirmation.

**Receipts (exact):**

| prime $p$ | $p\bmod8$ | $L$ | $b_p$ | $c_p$ | `mu2_half(1)` | `mu2_full(1)` |
|---|---|---|---|---|---|---|
| 17 | 1 | 2 | 3 | 4 | 0.0837619036 | 0.3069833885 |
| 641 | 1 | 16 | 81 | 4 | 0.55396… | (see `mu2_sweep.json`) |
| 677 | 5 | 169 | 85 | 676 | 0.4167644317 | 0.499… |
| 701 | 5 | 175 | 88 | 700 | 0.4851253867 | 0.5… |
| 733 | 5 | 61 | 92 | 732 | 0.4830290605 | 0.5… |
| 739 | 1 | 123 | 93 | 4 | 0.4922114337 | 0.5… |

($p=17$ is degenerate, $L=2$ gives a single increment, hence the small `mu2_half` — not a violation of uniformity, just $n=1$ sample.)

Full per-prime, per-$h$ table: `mu2_sweep.json` (630 rows, `dps=2000`).

---

## 3. Empirical results

$n=210$ primes $p\equiv1\pmod4$, $p<3000$ ($101$ with $p\equiv1\pmod8$, $109$ with $p\equiv5\pmod8$); $h\in\{1,3,5\}$.

| $h$ | `mu2_half` mean | `mu2_half` median | stdev | `mu2_full` mean | median |
|---|---|---|---|---|---|
| 1 | **0.49682** | 0.50219 | 0.0662 | **0.50040** | 0.49838 |
| 3 | **0.50334** | 0.50183 | 0.0480 | **0.50614** | 0.50245 |
| 5 | **0.50414** | 0.50261 | 0.0723 | **0.49278** | 0.49802 |

**Answer to the four sub-questions:**

1. **(a) Average over primes:** $\approx 0.50$ for all $h$ (range $0.493$–$0.506$ across the six cells). **(b) Is it $\sim1/2$ or smaller?** It is $\sim1/2$, i.e. the **random-phase value**, not $o(1)$. **(c) Does it decay with $L$?** **No.** Bucketed by $L\in[0,50),[50,100),[100,200),[200,400),[400,1000)$, the mean `mu2_half` stays within $[0.48,0.51]$ with no monotone trend; Pearson correlation $\rho(\mu_2,L)$ is $+0.057$ ($h{=}1$), $-0.039$ ($h{=}3$), $-0.027$ ($h{=}5$) — all consistent with zero.

2. **$\mu_2(h)\sim1/2$ or $o(1)$?** $\mu_2(h)\sim1/2$. The delta phases $\{\delta_{p,r}\}$ have fractional parts with empirical mean $0.49$–$0.55$ (uniform reference $0.5$) over representative primes ($739,733,701,677,641$). This is the **uniform/random-phase regime**, *not* the coherent counterseed regime.

3. **Is $\mu_2(h)\sim1/2$ provable from the source, or equivalent to $\pi$-digit equidistribution?** See §5 — it is **equivalent in difficulty** to the $\pi$-digit Weyl cancellation, and *not* source-derived. The empirical value is a consistency check, not a theorem.

4. **Contribution to NET-XVII-2:** See §4 — a *proved* small bound would collapse the oscillatory mode; but no such bound is available, and $\mu_2\approx1/2$ is *exactly* the case where the available bounds are **vacuous** (they give $O(1)$, not $o(1)$).

---

## 4. What a bound on $\mu_2(h)$ would contribute to NET-XVII-2 (the bilinear identity)

The exact bilinear identity (PCN-03, eq. 1.6):
$$E_p(h)-\widetilde E_p(h)=\frac1{L-1}\Re\sum_{\ell=0}^{L-1}\widehat D_{p,h}(\ell)\,G_p(15c_ph,\ell),\qquad \sum_\ell|G_p(\alpha,\ell)|^2=L^2,\quad |G_p(\alpha,\ell)|\le\sqrt p.$$

The $\ell=0$ (mean) term is unconditionally suppressed by $O(\sqrt p/L)$. The oscillatory ($\ell\ne0$) term is the gate, and it is bounded by Cauchy–Schwarz + Parseval:
$$\left|\frac1{L-1}\sum_{\ell\ne0}\widehat D_{p,h}(\ell)G_p(\dots,\ell)\right|\le 2\sqrt{\frac{L}{L-1}\,\mu_2(h)},$$
where the relevant $\mu_2$ is the **`mu2_full`** normalization (matching PCN-03 §1.3).

**Precisely what a bound contributes:**

- If $\mu_2(h)=o(1)$ (as $L\to\infty$ over the $100\%$-mass large-order primes), then the *entire* oscillatory cofiber erosion is $o(1)$, and combined with the unconditional $\ell=0$ suppression, $E_p(h)-\widetilde E_p(h)=o(1)$ **unconditionally** — closing NET-XVII-2.
- If $\mu_2(h)\le c<1/2$ (any fixed gap below the random value), one gets a nontrivial (but still $O(1)$) saving on the oscillatory bound, a partial structural result.
- If $\mu_2(h)\ge c>0$ (a *lower* bound, e.g. $\mu_2\to1/2$), this gives **nothing directly** to the erosion bound (which needs $\mu_2$ *small*), but it *certifies* that the cofiber phase is genuinely oscillating (non-conspiratorial) — i.e. it rules out the coherent counterseed at the energy level.

**Is any such bound source-derived or assumed?** **Neither.** The bound $2\sqrt{\frac{L}{L-1}\mu_2(h)}$ is a *conditional* identity (Cauchy–Schwarz + Parseval, both exact and source-derived), but the *value* of $\mu_2(h)$ is **not** bounded by any source theorem. Empirically $\mu_2(h)\approx1/2$, which makes the oscillatory bound $\approx2\sqrt{1\cdot1/2}=\sqrt2=O(1)$ — **vacuous**, i.e. the bound does not decay. To get $o(1)$ one would need $\mu_2(h)=o(1)$, which is **empirically false** on the authentic orbit and would contradict the observed uniformity.

**Firewall (crisp):** The bilinear identity *isolates* the gate into $\mu_2(h)$, but the isolation is the *last* source-derived step. After it, the value of $\mu_2(h)$ is governed by the $\pi$-digit phase (see §5) and is not constrained by any proved estimate.

---

## 5. The firewall: $\mu_2(h)\sim1/2 \iff$ $\pi$-digit equidistribution (the open gate)

### 5.1 Why $\delta$ carries the $\pi$-digit phase

From PCN-01, $W_{p,j}=U_j-a_{p,j}/p$ with $U_j=16^{j-1}\pi-T_j$ (BBP, $T_j$ exponentially tiny). The dominant term of $\delta_{p,r}$ is $15W_{b_p+r}=15U_{b_p+r}-15a_{p,b_p+r}/p$, so
$$e(h\delta_{p,r})=e\big(15h\cdot16^{b_p+r-1}\pi\big)\cdot e(-15h\,T_{b_p+r})\cdot e\big(-15h\,a_{p,b_p+r}/p\big)\cdot e\big(h\,r(b_p+r+1)\big)\cdot e(h\kappa_{p,b_p+r}).$$
The leading factor is the **base-16 digit phase of $\pi$ at frequency $15h$**. Therefore $\{\delta_{p,r}\}$ is a (differenced, $p$-periodically-shifted) copy of the $\pi$-digit phase sequence.

### 5.2 The equivalence

- $\mu_2(h)\sim1/2$ means $\{\delta_{p,r}\}$ is uniformly distributed $\bmod1$ (via the standard fact that for a real sequence $\{x_r\}$, $\frac1n\sum\sin^2(\pi h x_r/2)\to1/2$ for all $h$ iff $\{x_r\}$ is equidistributed). Since $\delta$ is slaved to the $\pi$-digit phase, **uniformity of $\{\delta\}$ is equivalent to uniform distribution of $\{15h\cdot16^{n-1}\pi\}$, i.e. the Weyl criterion** $\sum_{n\le N}e(15h\,16^{n-1}\pi)=o(N)$.
- The counterseed contrast: if $\pi$'s base-16 digits were adversarially structured so that $16^{n-1}\pi$ locked to a coherent phase, then $\delta\approx$ constant, $\sin^2\approx0$, $\mu_2\approx0$. The *observed* $\mu_2\approx1/2$ is the **opposite** of that — it is the uniform-phase, cancelling regime.

**Therefore:** proving $\mu_2(h)\sim1/2$ (or $\ge c>0$ along the authentic orbit) is **equivalent in difficulty to** proving the $\pi$-digit Weyl cancellation $S_N(h)=o(N)$, the single bottleneck that the framework has already identified (MEMORY: the π-normality and RH programs share this one gate). The present computation **confirms the gate is still open and is behaving as random phase**, but does **not** open it.

### 5.3 What the firewall is

The firewall is the boundary between:

- **(a) source-derived, exact, conditional statements** — the recurrence identity, the bilinear identity (1.6), the Gauss bound (1.7), the Parseval reduction of the full DFT energy to $\mu_2(h)$. These are *proved* (Lean 4 + exact `Fraction`). They locate the gate precisely at $\mu_2(h)$ but assign it **no value**.
- **(b) the value of $\mu_2(h)$** — this is $\pi$-digit Weyl cancellation in disguise, **OPEN**. The empirical $1/2$ is evidence (a finite consistency check), *not* a bound, and it is exactly the value for which the conditional bound in (a) is vacuous.

**No theorem in this dossier, and no computation reported here, crosses the firewall.** The honest claim record follows.

---

## 6. Claim ledger (revision-bound)

| ID | Type | Statement | Status | Evidence |
|---|---|---|---|---|
| MU2-1 | exact identity | $\delta_{p,r}=15W_{b_p+r}+r(b_p+r+1)+\kappa_{b_p+r}=W_{b_p+r+1}-W_{b_p+r}$ | **PROVED** (PCN-01) | `mu2_engine.py` method A/B rational equality; `PrimeCofactorCore.lean::scaled_cofiber_step_identity` |
| MU2-2 | exact identity | $\sum_\ell\|\widehat D_{p,h}(\ell)\|^2=\frac4L\sum_r\sin^2(\pi h\delta/2)$ | **PROVED** (Parseval) | PCN-03; exact DFT |
| MU2-3 | exact identity | bilinear identity (1.6), $\sum_\ell\|G_p\|^2=L^2$, $\|G_p\|\le\sqrt p$ | **PROVED LOCAL** | PCN-03, `mega_round_engine.py` |
| MU2-4 | finite computation | over $210$ primes $p<3000$, $h\in\{1,3,5\}$: $\mu_2(h)\approx0.50$, no decay in $L$, no $h$-dependence; $\{\delta\}$ uniform | **CERTIFIED FINITE** | `mu2_sweep.json` (dps=2000, 2 methods, 630 rows) |
| MU2-5 | conditional bound | oscillatory erosion $\le2\sqrt{\frac{L}{L-1}\mu_2(h)}$ | **PROVED conditional** | Cauchy–Schwarz + MU2-2 |
| MU2-6 | equivalence | $\mu_2(h)\to1/2$ (or $\ge c>0$) along authentic orbit $\iff$ $S_N(15h)=o(N)$ | **conjectural equivalence, OPEN** | §5.2 reduction |
| MU2-7 | open | unconditional $\mu_2(h)=o(1)$ or $\le c<1/2$ on large-order primes | **OPEN (empirically FALSE on authentic orbit)** | MU2-4 contradicts $o(1)$/$<1/2$ |
| MU2-8 | open | unconditional $\mu_2(h)\to1/2$ | **OPEN (equivalent to π-normality gate)** | MU2-6 |

**No claim above asserts an unconditional bound on $\mu_2(h)$, nor on $S_N(h)$, nor π-normality, nor RH.**

---

## 7. Cheapest next step

The decisive discriminator is already visible: **$\mu_2(h)$ does not decay with $L$.** The cheapest *falsifiable* next probe (maintainer's Frontier #1, restated) is to compute $\max_{\ell\ne0}\|\widehat D_{p,h}(\ell)\|$ directly versus $L$ across the same large-order primes: if it also flatlines at $O(1)$ (rather than $o(1)$), the oscillatory mode is definitively non-decaying and NET-XVII-2's erosion stays $O(1)$ — consistent with $\mu_2\approx1/2$ — with no new theorem, only the same open gate. This is a ~30-line extension of `mu2_engine.py` and would close the diagnostic loop started in `MEGAROUND3_CORE.md`.

---

## Appendix: reproduction

```
python3 mu2_engine.py            # smoke test p=17
python3 mu2_sweep.py             # full sweep -> mu2_sweep.json (dps=2000, ~20 min)
python3 mu2_analyze.py           # averages, mod-8 split, L-buckets, correlations
```

Engine: `mu2_engine.py` (exact `Fraction` + `mpmath`, two methods, assertions). Sweep: `mu2_sweep.py`. Data: `mu2_sweep.json`. Analysis: `mu2_analyze.py`.
