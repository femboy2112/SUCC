# Astra Ultra ← Carry-Safe Observer integration handoff (2026-10-23)

**From:** Claude carry-safe round, branch `research/carry-safe-observer-proof-forge-2026-10-23`, head `94000224e09a0a25bfd1a553a21a3ae63eb6801c`, forked from **Reality Pin** `5e2ba04c8b4ab627b6b0add588609c347346a1a2` (PR #244). **Not merged. No main change. No push without maintainer authorization.**

**To:** the parallel Astra Ultra session (infinite-dimensional Hilbert transport, pointed factorial-clock limits, continuum heat-kernel/Γ reconstruction, source-preserving adelic correspondences, the signed Weil/Suzuki problem).

This session built the **finite, exact, source-faithful laboratory** so Astra can test its infinite hypotheses without re-deriving prime-clock carry laws. The two branches share the same GitHub repo but are **not synchronized**; import this work as below, do not assume our states are merged.

Firewall held throughout: **RH_PROVED: NO.** No positive Hilbert overlap is promoted to completed-Weil positivity; no physical observer is asserted from the source algebra.

---

## 1. Proven identities (exact statements, domains, status, entry points)

All on the one-based carrier ℋ=ℓ²(ℕ_{≥1}), S|n⟩=|n+1⟩, V_p|n⟩=|pn⟩. Coordinates n=q(m-1)+r+1, 0≤r<q, m≥1.

| Identity | Statement | Status | Entry point |
|---|---|---|---|
| Polyphase bijection | n↔(m,r); carry successor (m,r)→(m,r+1) or (m+1,0) | PROVED LOCAL + **Lean** | `carry_safe_polyphase.polyphase_coords / polyphase_succ / carry_successor_holds` |
| Cuntz relations | U_{q,r}U_{q,s}^*=δ, Σ_r U_{q,r}U_{q,r}^*=I on ℋ (q≥2) | infinite CLASSICAL (Cuntz 1977); finite defect PROVED LOCAL | `carry_safe_polyphase.cuntz_relations` (returns exact `CuntzDefect`) |
| Prime embedding | V_p = U_{p,p-1}; V_pS = S^pV_p | PROVED LOCAL | `carry_safe_polyphase.prime_fucc_embedding` |
| Mixed radix | U_{p,r}U_{q,s}=U_{pq,ps+r}; n-factor little-endian | PROVED LOCAL + **Lean** | `carry_safe_polyphase.mixed_radix_compose / two_factor_compose` |
| Future insufficiency | largest S-stable refinement of O_p=ceil(n/p) is identity; sharp length p-1 | PROVED LOCAL + **Lean** | `future_sufficient_information.fso01_certificate / min_separation` |
| Source tomography | σ=log(q13/q15)/log(5/3), a=q13·3^σ, λ=q23/a | PROVED LOCAL (certified interval) | `source_controlled_tomography.identify_parameters / identify_sigma_interval` |
| Hilbert overlap | ⟨h_{pM},V_p u_M⟩=p^{-1/2}, ‖V_p u_M−h_{pM}‖²=2(1−p^{-1/2}) | PROVED LOCAL (exact) | `residue_hilbert_defect.diagnostics` |
| Prime-power / vMangoldt | p^{-r/2}; [log N,V_p]=(log p)V_p; log p/p^{r/2}=Λ(p^r)/√(p^r) | PROVED LOCAL + **firewall** | `residue_hilbert_defect.von_mangoldt_reconstruction / weil_firewall` |
| Adaptive weighted minimax | adaptive probe policy minimizing weighted/expected cost | PROVED LOCAL (3-way) | `carry_safe_probe_compiler.solve_weighted_adaptive` |

Lean theorems (choice-free `[propext, Quot.sound]`, no sorry/axiom): `formal/CarrySafePolyphase.lean` — `polyphase_reconstruct`, `carry_no_wrap`, `carry_wrap`, `mixed_radix_compose`, `fso01_insufficiency`. Receipt `formal/carry_safe_lean_receipt.json`; re-verify with `python scripts/verify_carry_safe_lean.py`.

## 2. Source-preservation contracts (what survives which map)

| Map | source labels | SUCC/FUCC action | carry register | inner product | Fourier phase | causal history | future probes | finite-horizon compression | observable equivalence |
|---|---|---|---|---|---|---|---|---|---|
| W_q (polyphase) | ✓ | S ↦ carry automaton | **exposes** r | unitary (clean prefix) | n/a | ✓ | ✓ | isometry; unhit slots when N≢0 mod q | preserves (bijection) |
| U_{q,r} isometry | ✓ | V_p=U_{p,p-1} | r is the label | isometry (U^*U=I) | n/a | ✓ | ✓ | completeness defect rank N−qD | injective |
| O_p quotient (lossy) | ✓ | S only | **discards** r | — | — | ✓ | **breaks** after ≤p-1 S | n/a | collapses block of size p, then recovered by S |
| V_p dilation on uniform block | ✓ | V_p | r=p-1 sector | overlap p^{-1/2} (NOT 1) | — | ✓ | — | — | — |
| character state g_k | ✓ | — | — | amp p^{-1/2} | **phase ω^{kr} determines r iff gcd(k,p)=1** | — | — | — | magnitude blind to r |

Rule of thumb for Astra: **a map that forgets the residue register is future-unsafe under unrestricted S** (CSO-05). Magnitude-only observables are residue-blind; the residue lives in the *phase* (coprime character) or is recovered by ≤p-1 successor advances.

## 3. Decisive counterexamples (smallest exact witnesses)

- **FSO-01 sharp witness:** n=1,n=2 at modulus p — O_p agrees, but O_p(1+(p-1))≠O_p(2+(p-1)) i.e. O_p(p)=1≠2=O_p(p+1). Invalidates "quotient observation is future-sufficient."
- **Cuntz finite-horizon defect:** q=3, D=5, N=20 → I−ΣUU^* = projection onto {16..20}, rank 5 ≠ 0. Invalidates "a finite compression satisfies the infinite completeness relation."
- **Counterfeit V_6:** invisible to {⟨2|K|3⟩,⟨1|K|3⟩,⟨1|K|5⟩}, visible only at ⟨1|K|6⟩. Dual: b(6)=a(6)−a(2)a(3)=1 for a(6)=2. Invalidates "a fixed coprime probe set authenticates the source."
- **Phase collapse off coprimality:** (p,k)=(4,2) gives overlaps (½,−½,½,−½); residues 0,2 and 1,3 share a phase. Invalidates "any nonzero character recovers the residue."
- **Overlap ≠ 1:** ⟨h,V_p u⟩=p^{-1/2}<1 for p≥2. Invalidates "dilation preserves the uniform state / no information is lost."
- **Primality not from magnitude:** composite m gives overlap m^{-1/2}, same form as a prime. Invalidates "a positive overlap magnitude authenticates primality."
- **Cost law:** full residue-register certification costs p, not p-1 (one warm-up + p-1 peels). Corrects the naive pairwise-length expectation.

## 4. Infinite-dimensional proof obligations (for Astra; no finite→∞ transport assumed)

Each finite result below becomes a theorem **only** with an explicit topology, domain and convergence mode — stated, not assumed:

- **O-IDO-1 (Cuntz faithfulness).** The finite U_{q,r} satisfy the exact relations; that the generated C*-algebra on ℋ is a faithful, simple O_q is CLASSICAL (Cuntz) but **not code-established here**. Obligation: cite/prove faithfulness in the completed C*-norm, with the horizon defect → 0 in the strong (not norm) topology.
- **O-IDO-2 (half-density limit).** V_p u_M overlaps are exact at finite M. Obligation: identify the weak/strong limit of the normalized arithmetic vectors on the critical half-density (cf. FOUNDATIONS §4: norm-1 vectors can converge weakly to 0). State the topology before any "V_p overlap → …" claim.
- **O-IDO-3 (von-Mangoldt → Weil).** log p/p^{r/2}=Λ(p^r)/√(p^r) is the prime-side building block. Obligation: the **completed** signed Weil distribution needs the Γ-factor, the pole term and the archimedean completion with a *proved* inversion; **positivity does not transfer from the finite positive overlaps** (firewall). This is the open RH-interface, untouched here.
- **O-IDO-4 (adelic carry).** Mixed-radix composition is a finite base change (not CRT for non-coprime moduli). Obligation: a source-preserving adelic/profinite limit of the carry tower needs the inverse-limit topology and a proved compatibility (Astra's `finite_adele_localization`/`profinite_hilbert` lineage).

## 5. Source access boundaries (math alphabet vs physical instrument)

Five-level firewall (`source_controlled_tomography.ACCESS_LADDER`), only **level 1** satisfied: (1) mathematical matrix elements — provided; (2) source-labelled state preparation; (3) coherent superposition/polarization measurement; (4) physically calibrated instrument; (5) independent empirical authentication — all require external authority and are **refused** by `assert_mathematical_only`. The source algebra is not evidence that a physical observer can implement its operators.

## 6. Conflict-free integration instructions

- **Branch head:** `94000224e09a0a25bfd1a553a21a3ae63eb6801c` on `research/carry-safe-observer-proof-forge-2026-10-23`, parent `5e2ba04` (PR #244). 9 commits, additive only.
- **File inventory (new, self-owned):**
  - `observational_succ/carry_safe_polyphase.py` (sha256 d645376a6795bd89…)
  - `observational_succ/future_sufficient_information.py` (6edb449603d40619…)
  - `observational_succ/source_controlled_tomography.py` (85a6c9c1ec3057e3…)
  - `observational_succ/residue_hilbert_defect.py` (2e5ba936a985f789…)
  - `observational_succ/carry_safe_probe_compiler.py` (3fb196e586c9a137…)
  - `formal/CarrySafePolyphase.lean` (51d34f39c2ac317d…), `scripts/verify_carry_safe_lean.py`, `formal/carry_safe_lean_receipt.json`
  - `tests/test_carry_safe_{polyphase,probe_compiler,hostile}.py`, `tests/test_{future_sufficient_information,source_controlled_tomography,residue_hilbert_defect}.py`
  - `docs/CLAIM_SUPPLEMENT_CARRY_SAFE_OBSERVER.md`, this handoff.
- **Only shared central file touched:** `docs/CLAIM_NAMESPACE_REGISTRY.json` — one **additive** namespace object (CSO). If Astra also appended a namespace, resolve by union (keep both objects); no existing row is rewritten.
- **Import without disturbing Astra:** `from observational_succ import carry_safe_polyphase, future_sufficient_information, source_controlled_tomography, residue_hilbert_defect, carry_safe_probe_compiler`. All reuse existing modules (`reciprocal_succ_fucc`, `future_safe_quotient`, `reality_pin_arithmetic`, `arithmetic_interactions`, `adaptive_proof_policy`, `noncommuting_proof_transport`); none are modified.
- **Tests / hashes:** `python -m unittest tests.test_carry_safe_polyphase tests.test_future_sufficient_information tests.test_source_controlled_tomography tests.test_residue_hilbert_defect tests.test_carry_safe_probe_compiler tests.test_carry_safe_hostile` → 96 exact. Lean: `python scripts/verify_carry_safe_lean.py` → PASS (receipt pins the source sha256). Gates: `verify_provenance.py` VERIFIED, `unregistered_prefix_collisions()==[]`.
- **Do not** merge either session's branch into the other, rewrite archival originals, or change main without maintainer authorization. The sessions share a repo, not a state.
