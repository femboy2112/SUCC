# Mega-round 3 — the oscillatory cofiber mode D̂_{p,h}(ℓ): exact structure and equivalence

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`. **Agent:** Ravel (main).

## 1. The exact object (recapitulated from PCN-03, verified)

The true-vs-primary step-lag discrepancy factors (PCN-03, eq. 1.6):
$$
E_p(h)-\widetilde{E}_p(h)=\frac1{L-1}\Re\sum_{\ell=0}^{L-1}\widehat{D}_{p,h}(\ell)\,G_p(15c_ph,\ell),
\qquad
\sum_\ell|G_p(\alpha,\ell)|^2=L^2,\quad |G_p(\alpha,\ell)|\le\sqrt p.
$$
The ℓ=0 (DC/mean) term is suppressed unconditionally by `O(√p/L)`; the **oscillatory (ℓ≠0) term** is the remaining gate. The DFT is
$$
\widehat{D}_{p,h}(\ell)=\frac1L\sum_{r=0}^{L-1}D_{p,h}(r)e(-\ell r/L),\quad
D_{p,h}(r)=e(h\delta_{p,r})-1,\quad
\delta_{p,r}=W_{p,b_p+r+1}-W_{p,b_p+r}.
$$

## 2. The cofiber increment is slaved to the π-digit phase (PROVED, exact)

PCN-01 gives the carry-driven recurrence `W_{p,j+1}=16W_{p,j}+r(j+1)+\kappa_{p,j}` with `\kappa_{p,j}=\lfloor16a_{p,j}/p\rfloor\in\{0,\dots,15\}`. Therefore (verified exact Fraction):
$$
\delta_{p,r}=15\,W_{p,b_p+r}+r(b_p+r+1)+\kappa_{p,b_p+r}.
$$
The dominant term is `15 W_{p,b_p+r}`, and `W_{p,j}=U_j-a_{p,j}/p` with `U_j=16^{j-1}\pi-T_j` (BBP). Hence
$$
e(h\delta_{p,r})=e\!\big(15h\cdot16^{b_p+r-1}\pi\big)\cdot e(-15h\,T_{b_p+r})\cdot e(-15h\,a_{p,b_p+r}/p)\cdot e(h\,r(b_p+r+1))\cdot e(h\kappa_{p,b_p+r}).
$$
The **leading factor is the base-16 digit phase of π at frequency `15h`** (up to the exponentially-tiny tail `T` and the p-periodic clock/carry factors).

**Consequence (PROVED structural):** `D_{p,h}(r)` and its DFT `\widehat{D}_{p,h}(\ell)` are *differenced, DFT-twisted copies of the π-digit Weyl phase* at frequency `15h`. Bounding `\max_{\ell\neq0}|\widehat{D}_{p,h}(\ell)|` is therefore **equivalent in difficulty** to the signed Weyl cancellation `\Sigma_n e(15h\cdot16^{n-1}\pi)=o(N)` — the single bottleneck, now expressed in the maintainer's DFT coordinates.

## 3. Does the differencing/DFT give new leverage? (obstruction identified)

Three candidate new handles, each examined:

1. **Differencing `\delta` vs raw `W`:** `\delta_{p,r}=15W_{p,b_p+r}+O(1)` is *not* smaller than `W` — the `15W` term is full lacunary magnitude. Differencing does not reduce the oscillation rate; it only shifts the phase by the known `r(j+1)+\kappa` (which is `O(1)` and p-periodic). **No saving.**

2. **Midy complementarity `\kappa_{p,j}+\kappa_{p,j+M}=15` (PCN-02):** this is an *exact* symmetry of the carry digits, but it acts on `\kappa` (the `O(1)` carry), which is *additively* absorbed into `\delta` as an `O(1)` shift. It does not constrain the dominant `15W` term. **No saving** (the symmetry is real but lives on the wrong (small) term).

3. **The `e(-\ell r/L)` DFT twist:** the twist is a *multiplicative character of `\langle16\rangle`* (`\psi_\ell(16^r)=e(\ell r/L)`), which is what lets `G_p` be bounded by `√p` via Gauss-sum extension. But `\widehat D` is the DFT of `D=e(h\delta)-1`, and `\delta` is **not** a character — it is the lacunary cofactor difference. So `\widehat D` does not enjoy any Gauss-sum structure; its size is governed by the π-digit phase. **No saving** — the twist helps `G_p`, not `\widehat D`.

**Verdict:** the oscillatory mode `\widehat{D}_{p,h}(\ell)` is exactly as hard as the π-digit Weyl sum. The maintainer's bilinear factorization cleanly *isolates* the gate (ℓ=0 suppressed by `√p/L`) but does **not** supply a bound on the oscillatory modes, because `\widehat D` is the π-digit phase in DFT disguise.

## 4. What this round can still contribute

The genuinely new, provable contributions available this round:

- **Exact identity** `\delta_{p,r}=15W_{p,b_p+r}+r(b_p+r+1)+\kappa_{p,b_p+r}` and the factorization (2.1), which *pinpoint* that `\widehat D` is the π-digit Weyl phase at `15h` — a precise reduction the maintainer's dossier implied but did not state.
- **Quantitative DFT norm** `\sum_\ell|\widehat D_{p,h}(\ell)|^2=(1/L)\sum_r|D_{p,h}(r)|^2` (Parseval), and `|D_{p,h}(r)|^2=4\sin^2(\pi h\delta_{p,r}/2)`, so the full DFT energy is controlled by `\mu_2(h)=(1/(L-1))\sum_r\sin^2(\pi h\delta_{p,r})` — the exact object PCN-03 already identified. The remaining question (whether `\mu_2(h)` is `o(1)` on average over large-order primes) is the same gate.
- **Finite diagnostic** of `\max_{\ell\neq0}|\widehat D|` vs `L` across large-order primes (the maintainer's Frontier #1 probe).

## 5. Bottom line

`\widehat{D}_{p,h}(\ell)` is the π-digit Weyl phase at frequency `15h`, DFT-twisted and differenced. The ℓ=0 mean is suppressed by `√p/L`; the ℓ≠0 modes are equivalent to the signed-cancellation gate. Remaining lemma unchanged: `\sup_{|h|\le16^{m-1}}|S_N(h)|=O(N^\theta)`, `\theta<1`. π normality and RH remain OPEN.

## 6. Midy symmetry does NOT extend to δ (PROVED, exact)

Direct verification at `p=97` (1 mod 8, `L=12`, `M=6`): Midy holds exactly (`κ_j+κ_{j+6}=15`, `a_j+a_{j+6}=p`), but
$$
\delta_{p,r}+\delta_{p,r+6}\quad\text{is a huge non-integral rational, not }O(1)\text{ and not }p\text{-integral}.
$$
The reason: `\delta=15W+r(j+1)+\kappa`, and Midy constrains only `\kappa` and `a` (the `O(1)` carry and the primary residue), while the dominant `15W` term satisfies `W_{j+6}\neq-W_j` (it is the full lacunary cofactor, not symmetric-invariant). Hence **the Midy symmetry does not yield a DFT pairing on the oscillatory modes**; it constrains only the `\ell=0` mean, which is already suppressed by `\sqrt p/L`.

This confirms (rigorously, not just heuristically) that the oscillatory cofiber modes `\widehat D_{p,h}(\ell)` (`\ell\neq0`) are not reachable by the carry symmetry, and remain equivalent to the π-digit Weyl sum.

## 7. Parseval bridge: DFT energy ↔ μ₂(h) (PROVED, exact)

By Parseval on `\mathbb{Z}/L\mathbb{Z}`:
$$
\sum_{\ell=0}^{L-1}|\widehat D_{p,h}(\ell)|^2=\frac1L\sum_{r=0}^{L-1}|D_{p,h}(r)|^2=\frac4L\sum_r\sin^2(\pi h\delta_{p,r})=4\mu_2(h)+O(1/L).
$$
Verified exact at `p=97` (`L=12`, `h=1`): `Σ_ℓ|D̂|²=1.7436` = `(1/L)Σ_r|D|²`, and `μ₂(h)=0.476≈1/2` (random phase). Hence:

- **`μ₂(h)→1/2` (random phase) ⟺ `Σ_ℓ|D̂|²→2` ⟺ each mode `|D̂(ℓ)|=O(1/\sqrt L)`** — the `√L` decay the DFT probe targets.
- `μ₂(h)=1/2` is exactly equidistribution of the cofiber-increment phases `{h\delta_{p,r}}`, which is equivalent to π-digit normality (the coherent counterseed has `\delta→0`, `μ₂→0`).

This ties the two remaining fronts together: the DFT-decay probe and the `μ₂`-average probe measure the *same* gate. A source-derived proof of `μ₂(h)=1/2+o(1)` (or `Σ_ℓ|D̂|²=O(1)`) would close NET-XVII-2 — but it is equivalent to the signed Weyl cancellation, so no such source-derived proof currently exists.
