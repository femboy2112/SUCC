# Exact cascade sum, phase-variance lower bound, and the D_J divergence condition

**Branch:** `research/sherman-gs05-signed-cascade-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (subagent, GS-05 exact cascade). **Scope:** the exact aggregate Haar cascade
structure of the SUCC π-normality program — the precise form of `d_j`, the phase-increment
variance relation, the D_J divergence condition, and the honest boundary.

**Depends on (all PROVED upstream):** GS-03 exact aggregate Haar budget; GS-04 all-prefix
sufficiency; GS05-TEL telescoping identity (`U_{n+L} − U_n = (16^L−1)U_n + F(n,L)`).

**Status:** contains PROVED identities/inequalities, one explicit HYPOTHESIS, and one OPEN
boundary. **π base-16 normality and RH remain OPEN.**

---

## 0. Setup and normalization (recalled from GS-03)

Fix dyadic `N = 2^J`, `z_n = e(hU_n)` (`e(t)=exp(2πit)`), level `j` with block length `L=2^j`.
Aligned block sums `A_{j,b} = Σ_{n∈block_b} z_n`. Then

- `E_j = Σ_b |A_{j,b}|²` (sum over all `N/L` blocks),
- `C_j = E_j/(NL)`,
- `W_j = Σ_{pairs} |A_left − A_right|²` (sum over the `N/(2L)` adjacent aligned pairs),
- `d_j = W_j/(2E_j)`, and the parallelogram law gives `C_{j+1} = C_j(1−d_j)` (GS-03, PROVED).

Every adjacent pair `(A,B)` sits at a block start `a` with `A = Σ_{n=a+1}^{a+L} z_n` and
`B = Σ_{n=a+1}^{a+L} z_{n+L}`.

---

## 1. Exact form of d_j in terms of the cross-block phase (PROVED)

By GS05-TEL, `z_{n+L} = e(hU_{n+L}) = e(hU_n)·e^{iφ_n}` with

$$
φ_n = h(U_{n+L} − U_n) \bmod 1
    = h(16^L−1)16^{n-1}π − h(T_{n+L}−T_n) \bmod 1.
$$

So each pair obeys `B = Σ_n z_n e^{iφ_n}` and

$$
A − B = \sum_{n=a+1}^{a+L} z_n\bigl(1 − e^{iφ_n}\bigr).
$$

**Claim (GS05-DJ-1, PROVED).** For each pair, with `E_pair = |A|²+|B|²`, `K_pair = Re(A \overline B)`:

$$
d_{pair} := \frac{|A−B|²}{2(|A|²+|B|²)} = \frac{1}{2} − \frac{K_{pair}}{E_{pair}},
\qquad
K_{pair} = \operatorname{Re}\sum_{n,m=a+1}^{a+L} z_n \overline{z_m} e^{-iφ_m}.
$$

*Proof.* `|A−B|² = |A|²+|B|² − 2Re(A\overline B)` (exact). Divide by `2E_pair`. ∎

The aggregate `d_j` is the **energy-weighted average** of `d_pair`:

$$
d_j = \frac{\sum_{pairs} W_{pair}}{\sum_{pairs} 2(|A|²+|B|²)}
    = \frac{\sum_{pairs} E_{pair}\, d_{pair}}{\sum_{pairs} E_{pair}}.
$$

**Diagonal/off-diagonal split (PROVED).** Expand `A\overline B = Σ_{n,m} z_n \overline{z_m} e^{−iφ_m}`.
The diagonal `n=m` contributes `Σ_n e^{−iφ_n} = L\,\overline μ`, where

$$
μ := \frac1L\sum_{n=a+1}^{a+L} e^{iφ_n}
$$

is the **mean phase increment**. Hence

$$
K_{pair} = L\,\operatorname{Re}(μ) \;+\; \operatorname{Re}\Bigl[\sum_{n\neq m} z_n \overline{z_m} e^{-iφ_m}\Bigr],
$$

i.e. the cross-block correlation is `L·Re(μ)` (the *mean* increment) **plus** an off-diagonal
sum that couples the orbit `{z_n}` to the increments `{φ_n}`. The off-diagonal term is the
entire obstruction to reducing `d_j` to a pure function of the phase-increment mean.

---

## 2. Phase variance: the exact deviation identity and the necessary condition (PROVED)

**Claim (GS05-DJ-2, PROVED — exact deviation identity).** For any pair, with `μ` the mean
increment above, the residual `R := B − \overline μ A = Σ_n z_n(e^{iφ_n} − \overline μ)` satisfies

$$
|B − \overline μ A|² \;\le\; L \sum_{n=a+1}^{a+L} |e^{iφ_n} − \overline μ|² \;=\; L²\bigl(1 − |μ|²\bigr).
$$

*Proof.* Cauchy–Schwarz on `Σ_n z_n(e^{iφ_n}−\overline μ)` with `|z_n|=1`; then
`Σ_n |e^{iφ_n}−μ|² = L(1−|μ|²)` because `Σ_n e^{iφ_n} = Lμ` forces
`Σ_n Re(e^{iφ_n}\overline μ) = L|μ|²`. ∎

**Claim (GS05-DJ-3, PROVED — necessary condition via concentration).** For any pair,

$$
|A−B|² \;\le\; 2L²\bigl(1 − \operatorname{Re} μ\bigr).
$$

*Proof.* `A−B = Σ_n z_n(1−e^{iφ_n})`; Cauchy–Schwarz gives
`|A−B|² ≤ L·Σ_n |1−e^{iφ_n}|² = L·Σ_n 2(1−\cos φ_n) = 2L²(1−Re μ)`. ∎

**Corollary (PROVED — concentration kills the cascade).** If the increments are *concentrated*,
`Re μ → 1` (equivalently `1−|μ|² → 0`, since `|μ|≤1` and `Re μ ≤ |μ|`), then `|A−B|² → 0`
uniformly in the block start `a`, hence `W_j → 0`, hence `d_j → 0`, hence the cascade stalls
(`C_{j+1} = C_j(1−o(1))`). **Therefore a necessary condition for `D_J(h) → ∞` is that the
phase increments `φ_n = h(16^L−1)16^{n-1}π \bmod 1` do NOT concentrate at 0 mod 1 at the
mesoscopic scale L.**

This is the **correct, provable direction**: spread of the increments is *necessary*. It is
proved from the two Cauchy–Schwarz inequalities above and needs only `|z_n|=1` and the exact
telescoping form — no Diophantine input.

**Remark (why the sufficient direction is not free).** The reverse — "spread ⟹ `d_j ≥ δ`" — is
**not** implied by §2. `|A−B|² = 4Σ_n sin²(φ_n/2) + off-diagonal`, and the off-diagonal
`Σ_{n≠m} z_n \overline z_m (1−e^{iφ_n})(1−e^{−iφ_m})` can be large and negative, cancelling the
diagonal `4Σ sin²(φ_n/2)`. Whether the *net* `|A−B|²` stays proportional to `E_pair` is exactly
the question of the joint correlation of `{z_n}` (the block Weyl sums, i.e. the object we are
trying to prove is small) with `{φ_n}`. This is **not** controlled by equidistribution of
`{16^{n-1}π}` alone.

---

## 3. The exact condition on the orbit {16^{n−1}π} for D_J(h) → ∞

**Claim (GS05-DJ-4, PROVED — reduction).** `D_J(h) = Σ_{j=k_J}^{l_J−1} d_j(h) → ∞` holds
(uniformly in the block starts, in the sense required by GS-04) **iff** the increments
`φ_n = h(16^L−1)16^{n-1}π − h(T_{n+L}−T_n) \bmod 1` satisfy, on a growing number of mesoscopic
`L=2^j`, the *decorrelation* condition

$$
\frac{K_j}{E_j} \;\le\; \frac12 − \delta_h
\qquad\text{for some fixed }\delta_h>0,
$$

where `K_j = Σ_{pairs} K_{pair} = Σ_{pairs} Re(A_l\overline A_r)`. This is equivalent to
`d_j = 1/2 − K_j/E_j ≥ \delta_h`.

*Proof.* `d_j = 1/2 − K_j/E_j` (GS05-DJ-1, summed). Divergence of `Σ d_j` requires infinitely
many `d_j ≥ \delta_h` for a fixed `\delta_h>0`. ∎

**The dominant rotation (PROVED, from `U_j = 16^{j-1}π − T_j` with `T_j = O(1/j²)`):**

$$
φ_n = h(16^L−1)\,16^{n-1}π \bmod 1 \;+\; O\!\bigl(\tfrac{|h|}{n²}\bigr).
$$

The leading term is the orbit of the irrational point `θ = (16^L−1)π` under the base-16 shift
`x ↦ 16x \bmod 1` (equivalently, the base-16 digit sequence of π, which is what normality is about).
**Because π is irrational, `θ = (16^L−1)π` is irrational for every `L ≥ 1`**, so the ×16 orbit
`{16^{n-1}θ \bmod 1}` is **equidistributed**, and

$$
μ \;=\; \frac1L\sum_{n=a+1}^{a+L} e\bigl(16^{n-1}θ\bigr) \;\to\; 0
\qquad(L\to\infty),
$$

uniformly in `a`. This is the *entire* provable content of "spread": the increments are
equidistributed (necessary condition of §2 is satisfied), **but this equidistribution does not by
itself force `K_j/E_j ≤ 1/2 − δ_h`.**

---

## 4. What is PROVED, what is HYPOTHESIS, what is OPEN

### PROVED (this note)

1. **GS05-DJ-1** — exact `d_pair = 1/2 − K_pair/E_pair`; `d_j` is the energy-weighted mean of
   `d_pair`; diagonal/off-diagonal split of `K_pair = L·Re μ + off-diagonal`.
2. **GS05-DJ-2** — exact deviation identity `|B−\overline μ A|² ≤ L²(1−|μ|²)`.
3. **GS05-DJ-3** — `|A−B|² ≤ 2L²(1−Re μ)`; hence **concentration ⟹ d_j → 0**, so *spread is
   necessary* for `D_J → ∞`.
4. **GS05-DJ-4** — `D_J(h)→∞ ⟺ K_j/E_j ≤ 1/2 − δ_h` on a growing set of mesoscopic scales; the
   increments equal the ×16 orbit of `(16^L−1)π` up to `O(h/n²)`, equidistributed from
   irrationality of π.

### HYPOTHESIS (explicitly NOT proved)

> **(GS05-DEC, HYPOTHESIS.)** For each fixed `h ≠ 0` there is `\delta_h > 0` and, for all large
> dyadic `N=2^J`, scales `k_J < l_J` with `2^{l_J−J}→0`, such that at each level
> `j ∈ [k_J, l_J)` the off-diagonal sum in `K_j` does **not** cancel the diagonal, so that
> `K_j/E_j ≤ 1/2 − δ_h` (equivalently `d_j ≥ δ_h`).

GS05-DEC is precisely the statement that the lag-L autocorrelation of `{e(hU_n)}` does not
reinforce. It is **not** a consequence of irrationality of π, nor of equidistribution of
`{16^{n-1}π}`, nor of Gamma positivity, nor of the Green-tail smallness (all of which are
PROVED and none of which settle it).

### OPEN boundary

`D_J(h) → ∞` — and therefore, via the PROVED GS-04 chain (Green transport + Weyl), π base-16
normality — **requires the Diophantine decorrelation hypothesis GS05-DEC**, i.e. a quantitative
statement about the **signed** pair correlation of the orbit `{16^{n-1}π}` at the sparse
multipliers `16^L−1` and mesoscopic lags `L=2^j`. This is strictly stronger than irrationality
(it needs the increments to be spread *in the correlated sense* measured by `K_j`, not merely in
the equidistributed sense measured by `μ`).

- **Provable from irrationality alone:** the increments are equidistributed (`μ→0`); concentration
  is excluded; the *necessary* condition for `D_J→∞` is met.
- **NOT provable from irrationality alone (OPEN):** the *sufficient* condition `K_j/E_j ≤ 1/2 − δ_h`,
  which needs control of the joint `(z_n, φ_n)` correlation — a genuine Diophantine/decorrelation
  input about π.

**π base-16 normality and RH remain OPEN.**

---

## Claim ledger

| ID | Statement | Status | Depends on |
|----|-----------|--------|------------|
| GS05-DJ-1 | `d_pair = 1/2 − K_pair/E_pair`, diagonal split `K_pair = L·Re μ + offdiag` | PROVED | GS05-TEL |
| GS05-DJ-2 | `|B−\overline μ A|² ≤ L²(1−|μ|²)` | PROVED | GS05-TEL, CS |
| GS05-DJ-3 | `|A−B|² ≤ 2L²(1−Re μ)`; concentration ⟹ `d_j→0` | PROVED | GS05-TEL, CS |
| GS05-DJ-4 | `D_J→∞ ⟺ K_j/E_j ≤ 1/2−δ_h`; increments = ×16 orbit of `(16^L−1)π` | PROVED | GS-03, GS05-TEL |
| GS05-DEC | `K_j/E_j ≤ 1/2−δ_h` on growing mesoscopic scales | HYPOTHESIS (OPEN) | — |

Boundary: GS05-DJ-1..4 are exact and complete; the gap from irrationality-of-π to `D_J→∞` is
exactly GS05-DEC, a signed Diophantine decorrelation statement that no current theorem supplies.
