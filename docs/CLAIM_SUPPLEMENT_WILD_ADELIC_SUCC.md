# Claim supplement: WILD ADELIC SUCC — arithmetic coverings and ambient wildness

**Branch:** `research/wild-adelic-embedding-solenoid-2026-10-14`; parent `PR #86 @205ffd020dd2a320eeac70a91a2a2700c969c048`. Do not merge into main without independent review. **RH PROVED: NO.** Theorems are source-conditional; no ambient 3D embedding is computer-built here.

| Claim | Precise scope | Status | Verification and boundary |
| --- | --- | --- | --- |
| WA-01 | `Σ_q=lim←(S¹,z↦z^q_n)` and `G_q=⋃D_n⁻¹ Z`, source-indexed `q_n>=2` | CLASSICAL DEFINITIONS / IMPLEMENTED | Exact rational stage products; source/epoch validated |
| WA-02 | `Čech H¹(Σ_q,Z)=colim(Z,×q_n)=G_q`, `Σ_q=Pontryagin dual G_q` | CLASSICAL + EXACT FINITE COEFFICIENTS | Continuity of Čech and duality are external theorems, NOT Lean-proved by code |
| WA-03 | Real dense flow `ι(t)_n=e^(2πit/D_n)`, complete profinite fiber `lim Z/D_n`, cofinal factorial fiber `Zhat` | CLASSICAL / PROVED PAPER | Tests verify compatible rational phase examples |
| WA-04 | `A_m(z)_n=z_n^m` globally invertible iff `v_p(D_n)→∞` for every `p|m` | CLASSICAL / PROVED PAPER | Exact finite inverse depths, multiplicative controls; rational `q_n=6` allowed as covering but not Euler prime |
| WA-05 | `|ker A_m|=∏_{p|m, v_p(D_n) bounded}p^{v_p(m)}` | CLASSICAL / PROVED PAPER | Exact factor counts for dyadic/factorial/distinct-prime/prefix laws |
| WA-06 | Global inverse coordinate `y_n=z_k^(D_k/(mD_n))`, `m|D_k/D_n` | PROVED LOCAL | 5-level and cross-depth exact rational-phase tests; finite stage alone ambiguous |
| WA-06B | Pro-kernel system `K_(n,m)=μ_m` has maps `×(D_k/D_n)` and image size `m/gcd(m,D_k/D_n)`; global kernel is inverse limit; arithmetic tails determine collapse | PROVED PAPER (ELEMENTARY) / EXACT TESTED | Source-stable depths; distinct-prime early-collapse/global-kernel counterexample; direct König surjectivity proof; no Pontryagin dependency for WA-04 |
| WA-07 | Factorial `D_n=(n+1)!` yields `G_q=Q`, `Σ_Q=Qhat`, fiber `Zhat` | CLASSICAL / PROVED PAPER | Every denominator divides a factorial, exact arithmetic |
| WA-08–10 | `Σ_Q=(R×Zhat)/anti-diagonal Z`, connecting `δ_m:μ_m≅Zhat/mZhat`, `δ(e^(2πir/m))=r mod m` | CLASSICAL EXACT SEQUENCE / PROVED PAPER | Exact rational residues; independent sign and quotient convention |
| WA-11 | `A_m τ_t = τ_(mt) A_m` on complete source | PROVED PAPER | Exact coordinate algebra; no nontrivial unitary frustration implied |
| WA-12 | Standard nested **unknotted** torus embeddings with specified winding give `π1(exterior)=G_q` | EXTERNAL GEOMETRIC THEOREM + EXACT COEFFICIENT CERTIFICATE | Conner–Meilstrup–Repovš (2015); code refuses absent embedding source |
| WA-13 | Prime automorphism ↔ intrinsic Čech `p`-divisibility ↔ extrinsic abelian exterior `p`-divisibility ↔ unbounded source `p`-valuation | PROVED PAPER WITH CLASSICAL IMPORTS | EXTRINSIC implication conditional on unknotted embedding, fails without it |
| WA-14–15 | Uniformly bi-equicontinuous tame ambient charts have tame Hausdorff limit; if limit wild, bilipschitz condition number must diverge | PROVED PAPER (ARZELÀ–ASCOLI) | Polygon U-arc *analogy* exact, NOT Alexander geometry or physical energy law |
| WA-16 | `π1(∪ increasing open spaces)=colim π1` with compatible common basepoint | CLASSICAL | Compact loops+homotopies; no universal finite blindness from wildness |
| WA-17 | Finite rational source translations admit normalized Følner witnesses with exact energy `2Σw min(|Ds|,2N+1)/(2N+1)→0` | PROVED LOCAL | Exact `Fraction` proof; NOT authentic signed Weil and cannot imply RH |
| WA-18 | Same abstract solenoid can have different complement `π1` under different ambient embeddings | EXTERNAL THEOREM / NEGATIVE CONTROL | Conner–Meilstrup–Repovš (2015) includes abelian and nonabelian exteriors |
| WA-19 | Source-indexed additive solenoid = one **additive** adelic-class host; identity with multiplicative idele/Weil sign | ADDITIVE CLASSICAL / SIGN BRIDGE **UNVERIFIED** | Source-correct pole, Gamma, conductor, prime-power, half-density and fake-6 controls still required |

**Exact artifacts:** `observational_succ/wild_adelic_tower.py`, `tests/test_wild_adelic_tower.py`, `scripts/wild_adelic_tower_probe.py`, and `research/2026-10-14/WILD_ADELIC_SUCC_RECEIPT.json`. The deterministic receipt is a finite algebra audit, not a topological proof checker. Full manuscript: `research/2026-10-14/WILD_ARITHMETIC_COMPLETION.md`. Source originals preserved. Academic novelty unverified; no theorem-priority claim.

**Next genuine moonshot:** prove a source-correct additive-to-multiplicative analytic/trace bridge from `Σ_Q` to the completed signed Weil form, on an explicitly identified common core. The arithmetic solenoid itself is a classical object; do not call it a Hilbert–Pólya operator or assume its positive Gram certifies ζ-zero positions.
