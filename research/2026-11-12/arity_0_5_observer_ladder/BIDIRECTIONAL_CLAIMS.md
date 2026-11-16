# Bidirectional channels continuation — claim ledger and next probe

**Main XXV / PR #604 draft; no merges authorized in this work.** All statuses refer to explicit declared domains; same-model derivations are not external review.

| ID | Claim | Status / evidence | Falsifier or next obligation |
|---|---|---|---|
| BDR-01 | Local/root and global/root define a *proposed* observer filtration on an unchanged source | CONJECTURE, design | Need operational functors/adjunctions with exact source and preserved readouts; no scalar proof-hardness universal theorem |
| BDR-02 | Typed products conserve the free-abelian dimensional signature, and rank_Q tests relative finite independence | PROVED LOCAL elementary algebra; exact Python | A change of observation family changes rank; metadata grades are not complexity bounds |
| BDR-03 | Every proper subset of a d-bit parity-conditioned distribution is uniform; full d-th Walsh moment distinguishes + and - | CLASSICAL / PROVED LOCAL; exact d<=6 controls | Correlated histories behind pairwise interfaces may evade a pairwise-marginal oracle assumption |
| BDR-04 | For b>=2, h nonzero, ∫|W_(N,h)|² Haar=1/N | CLASSICAL / PROVED LOCAL all-N | Source 0 violates any attempt to infer a bound at a selected x |
| BDR-05 | For grid G_K and gcd(h,b)=1, E_(K,N)=[min(K,N)+max(N-K,0)^2]/N²; K/N limits do not commute | PROVED LOCAL all-N,K; exact finite controls | K fixed then N large yields 1; K large first yields 0; other grid families not automatically equivalent |
| BDR-06 | Finite source-seed grid energy for authentic BBP is the exact signed group-algebra sum over congruent time frequencies | PROVED LOCAL direct character orthogonality; finite BBP exact phases | Source-agnostic positivity cannot bound the surviving high-index signed sum |
| BDR-07 | For shell [B,2B), coprime h, grid K≤B energy equals selected |W_B(h)|²; K≥2B equals 1/B | PROVED LOCAL by BDR-06 | No automatic source-selected estimate; K must grow to 2B to remove tail for free |
| BDR-08 | Aphex equation has typed local-delayed interaction-system interpretation | HYPOTHESIS (semantics), PROVED LOCAL for one chosen algebraic model | Historical symbols/time-index not defined; alternative interpretations possible |
| BDR-09 | The equation itself is specifically a Fourier transform law / proves SUCC dynamics | UNVERIFIED | Printed formula has no explicit Fourier transform; spectrogram art is separate |
| BDR-10 | Pairwise moments plus all lower arity probes determine source's d-way defect | REFUTED | ± parity source at d=3 (and every d>=2) |
| BDR-11 | One shared common eigenvector exists for all representation operators | UNVERIFIED generally and FALSE for arbitrary noncommuting operators | Pauli X and Z admit no common nonzero eigenvector; need declared operator family and joint eigenspace |
| BDR-12 | Authentic π R0, base-16 normality, Goldbach, RH follow | OPEN | Need genuine source-selected signed all-large-shell estimate, etc. |

## Next verdict-changing probe

1. Make the `Y_x` rational-cut/zero-anchor source module and the new channel hypergraph into an actual *diagram* with explicitly typed horizontal maps and vertical forgetful/completion maps. Use the existing `operational_yoneda_descent` and `beck_chevalley_source` implementations, not an incompatible category core. Preserve literal U0=0 and the completed orbit correction.
2. Define exactly which combinations of source-labelled operations produce channel grades. Compute minimal separating arity on hostile parity/periodic/rational alias sources before calling the rank a hardness scale.
3. Search for a source-derived estimate of `Re W_B(1)≤1−η` for all B≥B0 on the true π source. The new seed-grid formula makes the deficit explicit: prove a source-specific signed tail saving with bounds and adversarial counterseeds. Neither finite cross validation nor general L² positivity suffices.
4. Construct a *declared transport* from the finite rational formal-group-ring phases to spectral/Walsh coordinates; retain off-diagonal negative terms until the last step. Verify phase orientation, double counting and lag before applying constructive GNS or Fourier transformation.
5. As a negative control for "universal eigenvector", test one noncommuting pair (Pauli X,Z) and prove no common eigenline. Try replacing the phrase by a joint source-fixed representation diagram, or a family of compatible observation fibers.

## Reproducibility

Isolated local staging: CPython 3.13.5, stdlib only, `python -m unittest discover -s tests -p 'test_bidirectional_channel_basis.py' -v`: **14 passed / 0 skipped**. Existing arity focused tests: **26 run / 25 pass / 1 skipped** (canonical selected-orbit source comparison unavailable in the isolated staging overlay). Group-algebra coefficients are exact `Fraction` phase labels; they have not been evaluated as interval-certified complex numbers. Continuous Haar `1/N` and grid formulas are paper proofs backed by exact finite controls; there is no finite computational proof of π-normality.

After pushing, rerun `AGENTS.md` mandatory provenance, full unittest, observer foundations and ordinal probes on the *exact* pushed head. CI statuses are commit-specific; do not treat an earlier green run as new green evidence.
