# Claim ledger — RENORM transport (draft research; no status promotion)

| ID | Claim | Status | Authority | Boundary / unpaid debt |
|---|---|---|---|---|
| RT-01 | `c_A(h)=c_A(16h)+ε_A(h)` exactly, ∀ integer h, A≥2 | Demonstrated | exact algebra of `U_n=16U_{n-1}+r(n)` | none |
| RT-02 | `\|ε_A(h)\| ≤ 2/A + 15π\|h\|/(4A(8A−15))` | Demonstrated | triangle ineq, `\|sin x\|≤\|x\|`, merged SC-6 `r(n)<15/((8n-7)(8n-6))`; held-out receipt 0 violations, worst ratio 0.9809 | a modulus/transport bound, not cancellation |
| RT-00 | sufficiency chain is one-directional: `band⟹J⟹E⟹normal`; only `normal⟺S_N=o(N)` is a biconditional | Demonstrated | SC-8/SC-3/#476 + #293/SGO-09; generic converse `J⟹band` refuted by equally-spaced cloud (J=1, band=2q) | the universal converse is false; a BBP-specific converse is neither claimed nor needed |
| RT-03 | RENORM-2 barrier (**corrected**): **common-depth** ×16 is injective ⇒ low band → *distinct* high band ≤A^{3/2}, each modulus preserved up to o(1), mass relocated not killed | Demonstrated (method obstruction) | common depth `j=⌊log₁₆(A^{3/2}/H)⌋` + corrected geometric accumulation `2j/A+π\|h\|(16^j−1)/(4A(8A−15))`; 0 violations, worst 0.923 | NOT a size bound on `c_A`; a no-go for the "iterate ×16 until small" method |
| — | `Σ_{1≤\|h\|≤q_A²}\|c_A(h)\|² = o(K_A)` **⟹** `J_{A,m_A/2}=o(K_A)` **⟹** π normal **⟺** `S_N(h)=o(N)` ∀h≠0 (only the last arrow is ⟺) | **OPEN** | — | genuine high-frequency signed equidistribution |
| — | π base-16 normality | **OPEN** | — | the above |
| — | RH | **OPEN** (separate program) | — | — |

**Generality boundary (recorded negative):** RT-2 is **not** a source discriminator — a
scaled-forcing mutant `r'(n)=s·r(n)` (s=3,5) also satisfies the bound (verified, `test_renorm_transport`,
control C2). The sharp reason: with `U_0=0`, linearity gives `U'_n=s·U_n` exactly, so
`c'_A(h)=c_A(s h)` — the mutant is the genuine orbit at rescaled frequency (identity gap `0.0`, worst
ratio `0.730`). RT-1/2/3 are general for any small-forcing ×16 recurrence; the BBP source enters only
the constant, not an exclusion of wrong sources.

**Controls (must break any false positive):** `x=1/5` fixed point (`c_A(h)=e(h/5)`, modulus 1,
no decay); counterseed `s*=−π/16`; same-forcing changed seed. **No Galois average, no
inverse-branch averaging, no Haar assumption, no π digits.** Established constructions; no
original-priority claim.
