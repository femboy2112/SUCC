# Carry-safe observer — mathematical proof dossier

Companion to `CLAIM_SUPPLEMENT_CARRY_SAFE_OBSERVER.md` (the ledger) and
`handoffs/ASTRA_ULTRA_CARRY_SAFE_INTEGRATION_2026-10-23.md` (the integration).
This file records the actual derivations. Carrier ℋ=ℓ²(ℕ_{≥1}), S|n⟩=|n+1⟩,
V_p|n⟩=|pn⟩. One-based coordinates: n = q(m-1)+r+1, 0≤r<q, m≥1, so
m-1=⌊(n-1)/q⌋, r=(n-1) mod q. RH_PROVED: NO.

## 1. Polyphase coordinates and controlled carry (CSA-01)

n ↦ (m,r) is a bijection ℕ_{≥1} → ℕ_{≥1}×{0..q-1} (Euclidean division of n-1 by
q). Hence W_q|n⟩=|m⟩⊗|r⟩ is unitary on any clean prefix N=qM; on a partial
prefix it is an isometry missing the tensor slots (M,r>r_max). Successor: if
r<q-1, n+1=q(m-1)+(r+1)+1 → (m,r+1); if r=q-1 then n=qm, n+1=qm+1=q·m+0+1 →
(m+1,0). This is the controlled carry. **Lean:** `polyphase_reconstruct`,
`carry_no_wrap`, `carry_wrap` (the two carry equations are unconditional
arithmetic identities; the hypotheses select the branch).

## 2. Residue isometries and the Cuntz relations (CSA-02)

U_{q,r}|n⟩=|q(n-1)+r+1⟩. Ranges over r are the residue classes of {1..} mod q,
pairwise disjoint and covering ℕ_{≥1}. Therefore on ℋ:
U_{q,r}^*U_{q,s}|n⟩ = U_{q,r}^*|q(n-1)+s+1⟩ is nonzero iff s≡r (mod q), i.e. s=r,
giving |n⟩; so U_{q,r}^*U_{q,s}=δ_{rs}I. And Σ_r U_{q,r}U_{q,r}^* projects onto
∪_r range = ℕ_{≥1} = I. These are the Cuntz relations; {U_{q,r}} generates a
representation of O_q (CLASSICAL, Cuntz 1977; faithful by simplicity).

**Finite horizon (PROVED LOCAL, exact).** Restrict source to {1..D}, target to
{1..N}, N≥qD. Then U^*U=δI still holds exactly (isometry), but Σ_r U_{q,r}U_{q,r}^*
projects onto {1..qD}, so I_N − Σ = projection onto {qD+1..N}, of rank N−qD.
Zero iff N=qD. A finite compression therefore does **not** inherit the infinite
completeness relation without this defect. `cuntz_relations` returns it exactly.

## 3. Prime embedding and braid (CSA-03)

U_{p,p-1}|n⟩=|p(n-1)+(p-1)+1⟩=|pn⟩=V_p|n⟩, so V_p=U_{p,p-1}; the terminal residue
p-1 is forced by the one-based origin (residue 0 gives p(n-1)+1≠pn for n>1).
Braid: V_pS|n⟩=|p(n+1)⟩=|pn+p⟩=S^pV_p|n⟩. A composite "prime" label is rejected.

## 4. Mixed-radix composition (CSA-04)

U_{p,r}U_{q,s}|n⟩ = U_{p,r}|q(n-1)+s+1⟩ = |p(q(n-1)+s)+r+1⟩ =
|pq(n-1)+(ps+r)+1⟩ = U_{pq,ps+r}|n⟩, with 0≤ps+r<pq. Reversed order gives
U_{qp,qr+s}. For k factors (little-endian) R=Σ_i r_i Π_{j<i} q_j. This is a base
change, **not** a CRT split unless gcd=1 (and even then differs from the digit
order). **Lean:** `mixed_radix_compose` (0-based form odx). 

## 5. Minimum future-sufficient information (FSO-01)

Observation O_p(n)=⌈n/p⌉=m discards r.

**Separation lemma.** For x≠y the least k≥0 with O_p(x+k)≠O_p(y+k) is 0 if the
blocks differ, else p−s where r<s are the residues (same block). Proof:
O_p(x+k)=m+⌊(r+k)/p⌋; with r<s, ⌊(s+k)/p⌋ first exceeds ⌊(r+k)/p⌋ at k=p−s
(then s+k=p, r+k=p−(s−r)<p). So k=p−s≤p−1, sharp at (r,s)=(0,1), k=p−1.

**Theorem (identity collapse).** Let ∼ refine O_p-equality and be S-stable. If
x∼y then S^kx∼S^ky for all k, hence O_p(x+k)=O_p(y+k) for all k; for x≠y the
lemma contradicts this at k≤p−1. So ∼ ⊆ identity: the residue register is
necessary. **Lean witness:** `fso01_insufficiency` (O_p agrees at 1,2; differs
at p,p+1). The generic largest-action-stable-congruence engine is CLASSICAL
(`future_safe_quotient.minimize`, Nerode/Moore); the arithmetic theorem is new.

**Toolkit dependence (FSO-04).** "Agree on all words S^k, k≤h" is an
equivalence between O_p-equality (h=0) and identity (h≥p-1); 0<h<p-1 is strictly
between (p=5,h=2: each block → {0,1,2},{3},{4}).

## 6. Source-controlled tomography (SCO-01/02)

K off-diagonals: ⟨2|K|3⟩=λ (S), ⟨1|K|3⟩=3^{-σ}, ⟨1|K|5⟩=5^{-σ} (V-channels).
Scaled readings q_•=a·(·). Then q13/q15=(5/3)^σ ⇒ σ=log(q13/q15)/log(5/3); the
gain a cancels. a=q13·3^σ, λ=q23/a. **Stability:** independent relative errors
≤η multiply the ratio by at most (1+η)/(1-η), so |σ̂−σ|≤log((1+η)/(1-η))/log(5/3),
computed with certified log intervals. Monte-Carlo (seed 20261023, 4M samples/η)
confirmed the empirical max never exceeds the certified bound (tight to ~1e-31).

**Authentication (SCO-03).** An isolated composite V_m is invisible to any entry
whose index pair is coprime to its support but visible at ⟨1|K|m⟩=m^{-σ};
multiplicatively, b(m)=a(m)−Σ a(d)a(m/d) detects it (b(6)=1 for a counterfeit
a(6)=2, vs 0 for genuine zeta). No fixed finite probe set suffices for retuned
counterfeits of unbounded support (complexity prior required).

## 7. Retained vs discarded Hilbert information (HDEF)

u_M=M^{-1/2}Σ_{n≤M}|n⟩; V_p u_M=M^{-1/2}Σ|pn⟩; h_{pM}=(pM)^{-1/2}Σ_{j≤pM}|j⟩.
Decompose h_{pM}=p^{-1/2}Σ_{r=0}^{p-1}h^{(r)} with h^{(r)} the normalized uniform
over residue-r sites (orthonormal). Then V_p u_M = h^{(p-1)} (the terminal
sector), so ⟨h_{pM},V_p u_M⟩=p^{-1/2}, ‖V_p u_M−h_{pM}‖²=2(1−p^{-1/2}),
projection |·|²=1/p, complementary 1−1/p. These are four **distinct** quantities.

**Fourier (HDEF-03).** ⟨h^{(r)}, g_k⟩=p^{-1/2}ω^{kr}: magnitude is residue-blind,
the phase recovers r **iff gcd(k,p)=1** (non-coprime (k,p) collapses residues,
e.g. (4,2)→(½,−½,½,−½)). This is the correctly-scoped Fourier shadow of §5.

**von-Mangoldt (HDEF-04).** For q=p^r the overlap is p^{-r/2}; [log N,V_p]=
(log p)V_p, so log p·p^{-r/2}=Λ(p^r)/√(p^r). **FIREWALL:** this is the prime-side
building block of the explicit formula, NOT the completed signed Weil
distribution (no Γ, pole, archimedean completion, sign). A composite m gives the
same-form m^{-1/2}; **overlap magnitude cannot authenticate primality, and
positivity does not transfer** (FOUNDATIONS §3-4). RH stays open.

## 8. Adaptive weighted-minimax cost law (Phase 5)

On the quotient-observation carrier the probe observes-then-advances. The
adaptive minimax cost to certify the hidden residue register is exactly **p**
(computed three independent ways: value iteration = `solve_adaptive_claim` rank
= brute-force DFS). Reason: the first probe sees every source in block 0
(uninformative warm-up), then one residue peels off per subsequent probe: 1 +
(p−1) = p. For a residue pair r<s the cost is (p−s)+1 =
`min_separation(r+1,s+1,p)` + 1 — the FSO-01 advance length plus the single
warm-up. Expected-cost mode (uniform prior): p=3→8/3, p=4→13/4, p=5→19/5. This
**corrects** the naive expectation that the cost equals the pairwise length p−1.

## Boundaries (what is NOT established)

Infinite-dimensional transport, faithfulness in the completed C*-norm, the
half-density weak/strong limit, the Γ/pole/archimedean completion, signed Weil
positivity, and any physical realizability of the operators — all open and
listed as obligations O-IDO-1..4 in the Astra handoff. A finite Lean fact about
Nat maps is not a theorem about unbounded Hilbert operators.
