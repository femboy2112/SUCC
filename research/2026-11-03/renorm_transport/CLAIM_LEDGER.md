# Claim ledger — RENORM transport (draft research; no status promotion)

| ID | Claim | Status | Authority | Boundary / unpaid debt |
|---|---|---|---|---|
| RT-01 | `c_A(h)=c_A(16h)+ε_A(h)` exactly, ∀ integer h, A≥2 | Demonstrated | exact algebra of `U_n=16U_{n-1}+r(n)` | none |
| RT-02 | `\|ε_A(h)\| ≤ 2/A + 15π\|h\|/(4A(8A−15))` | Demonstrated | triangle ineq, `\|sin x\|≤\|x\|`, merged SC-6 `r(n)<15/((8n-7)(8n-6))`; held-out receipt 0 violations, worst ratio 0.9809 | a modulus/transport bound, not cancellation |
| RT-03 | RENORM-2 barrier: ×16 injective ⇒ low band ↔ high band bijection, mass transported | Demonstrated (method obstruction) | injectivity + RT-02 telescoped to freq ~A^{3/2}, error o(1) | NOT a size bound on `c_A`; a no-go for one method |
| — | `Σ_{1≤\|h\|≤q_A²}\|c_A(h)\|² = o(K_A)` (⇔ `J_{A,m_A/2}=o(K_A)` ⇔ `S_N(h)=o(N)` ∀h≠0) | **OPEN** | — | genuine high-frequency signed equidistribution |
| — | π base-16 normality | **OPEN** | — | the above |
| — | RH | **OPEN** (separate program) | — | — |

**Generality boundary (recorded negative):** RT-2 is **not** a source discriminator — a
scaled-forcing mutant `r'(n)=s·r(n)` (s=3,5) also satisfies the bound (verified, `test_renorm_transport`),
because the triangle bound discards the forcing sum's cancellation. RT-1/2/3 are general for any
small-forcing ×16 recurrence; the BBP source enters only the constant, not an exclusion of wrong sources.

**Controls (must break any false positive):** `x=1/5` fixed point (`c_A(h)=e(h/5)`, modulus 1,
no decay); counterseed `s*=−π/16`; same-forcing changed seed. **No Galois average, no
inverse-branch averaging, no Haar assumption, no π digits.** Established constructions; no
original-priority claim.
