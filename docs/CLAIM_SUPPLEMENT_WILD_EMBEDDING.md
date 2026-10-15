# Wild-embedding claim supplements (two distinct lineages)

> **Phoenix II reconciliation note (2026-10-14).** PR #89 (`alexander-horned-source-observer`, parent #84) and PR #90 (`wild-embedding-boundary-descent`, parent #85) independently wrote a `CLAIM_SUPPLEMENT_WILD_EMBEDDING.md`. They are **different results on different modules/receipts** (`wild_embedding_succ.py` / `WILD_EMBEDDING_SUCC_RECEIPT.json` vs. `wild_embedding_probes.py` + `wild_boundary_compression.py` / `WILD_EMBEDDING_BOUNDARY_RECEIPT.json`), so both ledgers are preserved verbatim below as separate sections rather than one overwriting the other. Neither claims RH. The dedicated CI lanes are `.github/workflows/wild-embedding-succ.yml` (#89) and `.github/workflows/wild-embedding-boundary.yml` (#90).

---

## Lineage A (PR #89) — WILD-SUCC source-indexed embedding and infinitely nested holonomy ledger

**Ancestor:** `research/signed-weil-h1-spectral-tail-2026-10-14@526bad9e55ec2506c52b0dc2ac2cf2b4252a2473` (PR #84). Not main; no RH claim or physical wild-space assertion. All full statements and citations: [`ALEXANDER_WILD_SOURCE_GLUING.md`](../research/2026-10-14/ALEXANDER_WILD_SOURCE_GLUING.md).

| ID | Scope and proof-status |
|---|---|
| W1 | Horned sphere intrinsically S², exterior not simply connected yet H₁=0: **CLASSICAL IMPORT** (Alexander 1924; Hatcher 2B.2); exact free-group maps injected: **PROVED LOCAL** |
| W2 | Generator recursively transported to nested commutator; reduced word length 4^k, lower-central depth exactly 2^k; bounded nilpotent probes blind; explicit UT_(2^k+1)(Z) detectors show the depth threshold is sharp while refusing a compatible global nilpotent detector; perfect nontrivial direct limit: **PROVED LOCAL/CLASSICAL Magnus**, finite TESTED |
| W3 | Stagewise S² with source-prime degree-p bonding has Čech H²=Z[P^-1], non-S² global limit; long identical finite prefixes cannot identify tail: **CLASSICAL/TYPED MODEL**, NOT actual horned sphere |
| W4 | Uniform ambient bi-Lipschitz transport and uniform source-sphere convergence force tame global limit; wildness requires conditioning debt. Converse REFUTED by x³ benign limit: **PROVED GENERAL** |
| W5 | Genuine Suzuki first-prime hinge has vanishing raw HS kernel and fixed signed differentiated operator norm; concentrated tent derivative cost diverges: **PARENT IMPORT/TESTED rational surrogate** |
| W6 | Strong self-adjoint + collective compactness implies norm convergence; escaping compact negative rank-one sequence is countermodel: **PROVED GENERAL**, NOT authentic zeta witness |
| W7 | Finite prime-solenoid characters become approximately translation-equivariant Gaussian wavepackets with exact rational `O(T²/N²)` residual and source frequency Gram bound; no uniform all-frequency isometry: **PROVED LOCAL, TESTED** |
| W8 | Exact bounded additive-solenoid Haar-L² to Archimedean Lebesgue-L² intertwiner impossible by spectral-type mismatch: **CLASSICAL IMPORT, independent WA-20 sibling** |
| W9 | Real completed Weil π₁/Holonomy identification, new nonabelian Euler source and global all-test sign: **UNVERIFIED** |

**Important firewall:** Abelianization *preserves* group colimits; missing information is the nonabelian commutator itself. Genuine multiplicative prime operators commute on the full log carrier, so they do not magically realize the horned exterior group. Genuine finite-interval compression may cause noncommutation, but the source-preserving operator identification and Schur inequality remain to be proved. A Gaussian covariance, finite Betti record, group homology, or topological distortion is **not** a PSD original Weil form.

**Repro:** `python -m unittest tests.test_wild_embedding_succ -v`; `python scripts/wild_embedding_succ_probe.py --verify research/2026-10-14/WILD_EMBEDDING_SUCC_RECEIPT.json`. Local finite suite/test count and CI need separate exact-head validation.

---

## Lineage B (PR #90) — Alexander wild-embedding observer descent

**Date:** 2026-10-14. **Research branch:** `research/wild-embedding-boundary-descent-2026-10-14`. **Exact parent:** authentic completed-Weil source hierarchy PR #85 at `dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`. No main merge or new physical-carrier assumption. Complete mathematical derivations and negative controls: [WILD_EMBEDDING_SOURCE_BOUNDARY.md](../research/2026-10-14/WILD_EMBEDDING_SOURCE_BOUNDARY.md).

| ID | Scoped claim | Status and what is NOT inferred |
|---|---|---|
| WES-01 | Homeomorphic abstract S² can have inequivalent complements; intrinsic sphere forgetful functor loses exterior pi1 | CLASSICAL Alexander 1924; exact double-cone Betti/Euler PROVED LOCAL, NOT a 3D embedding |
| WES-02 | Actual Alexander exterior pi1 nontrivial and perfect; every map to solvable group trivial | CLASSICAL original nontriviality + Alexander duality/Hurewicz, explicit deduction; NOT a claim all finite non-solvable probes see it |
| WES-03 | Nested free-group commutator w_k invisible through Magnus degree k yet detectable at k+1 | PROVED LOCAL exact integer/free algebra; toy F2 is NOT the perfect horned exterior group |
| WES-04 | For tame finite sphere approximations Hausdorff→wild limit, fillings of a noncontractible limiting-exterior loop cannot have both uniform clearance and uniform Lipschitz bound | PROVED classical Arzelà–Ascoli consequence under declared assumptions; NO effective bound or physical energy law |
| WES-05 | Source/observer compression defect PA(I-P)BP and three-map coherence | CLASSICAL algebra/PROVED LOCAL exact rational matrix |
| WES-06 | Bulk commuting T and PSD C can have [PTP,PCP]≠0 after compressing original finite cyclic carrier | PROVED LOCAL finite positive sum-of-squares toy; NOT original Gamma kernel or a literal horned 3-space |
| WES-07 | Unitary source-preserving basis re-embedding cannot change negative spectral depth | CLASSICAL invariance/PROVED LOCAL exact two-state signed countermodel; no wild-to-Weil intertwiner |
| WES-08 | Genuine finite-stage 3D wild sphere mesh with proven exterior loop and explicit witness costs | UNVERIFIED / NOT IMPLEMENTED |
| WES-09 | Identification of actual horned sphere complement-group dynamics with completed Weil sign | UNVERIFIED, no authentic source map or positivity theorem |
| RH | Original completed Weil form positive on all proper tests | UNVERIFIED, RH remains open |

**Primary provenance:** J. W. Alexander, PNAS **10** (1924), 8–10, DOI 10.1073/pnas.10.1.8; classical Alexander duality (S² embedded in S³), Hurewicz H₁/abelianization, standard Arzelà–Ascoli/generalized Schoenflies. Prior SUCC #68 already realizes the abstract finite prime-sphere, and sibling #86 already reports a *real* arithmetic prime/Gamma compression interaction; neither is silently merged or recredited.

**Hostile check ledger:** homology-zero ≠ simply-connected; no S3 representation of nontrivial perfect original exterior; F2/S3 Magnus toy ≠ actual exterior; a positive clipped bath + noncommuting clipped shift does NOT imply genuine Weil sign; uniform finite-stage contraction \(\forall n\,\exists H_n\) does not provide a common limit without witness control; source-independent random compression ≠ real prime/arch source; unitary reparametrization never repairs a negative quadratic direction.

**Reproduction:**
```sh
python -m unittest discover -s tests -p 'test_wild_*.py' -v
python -m unittest discover -s tests -p 'test_source_weil_hierarchy.py' -v
python scripts/wild_embedding_boundary_probe.py --verify research/2026-10-14/WILD_EMBEDDING_BOUNDARY_RECEIPT.json
python scripts/verify_provenance.py
```
This is a mathematical and finite-executable calibration, not an empirical physical observer, a Lean certificate of Alexander topology or a genuine RH reduction. Whole-repo CI/dedicated exact-head CI need independent inspection.


### WES-10 — boundary source stability, but no positivity transfer

**PROVED LOCAL conditional norm theorem:** If a verified same-Hilbert-space global source satisfies \(\|C-C_J\|\le\epsilon\) and \(T\) is unitary, then \(\|[PTP,PCP]-[PTP,PC_JP]\|\le2\epsilon\). An exact witnessed finite commutator margin \(m>2\epsilon\) therefore yields a genuine nonzero compressed commutator. The rational five-cycle source toy proves a margin \(m=1\), so a **declared** error \(1/10\) conditionally gives lower bound \(4/5\). Direct rational perturbation controls agree. This is not a sourced enclosure of the real Gamma convolution; the code expressly returns `genuine_arithmetic_gamma_error_verified=False`, `positive_weil_proved=False`. Sibling PR #86 has a separate actual prime/Gamma source boundary study; no unverified identification or sign consequence is imported. Failing to obtain a source-correct same-space \(\epsilon\) is an **access/transport gap**, not proof of the RH sign.


### WES-11 — REFUTED literal wild emergence of Weil-sign negativity

**PROVED CLASSICAL / adversarial correction.** Strong operator limits of positive bounded self-adjoint operators are positive (evaluate every quadratic form). In the stronger operator-norm hierarchy constructed in ancestor PR #85, \(|d_-(G_{a,N})-d_-(G_a)|\le\|G_{a,N}-G_a\|\). Therefore a fixed authentic negative quadratic direction, if it exists, must be present at some sufficiently fine **finite** certified stage; the sign cannot become negative only in the global limit while **all** genuine operator-norm approximants were positive. By contrast, the exterior fundamental group of an embedded sphere **can** change under Hausdorff limits of tame embeddings. An exact \(2\times2\) rational \(\mathrm{diag}(1,-1+1/n)\to\mathrm{diag}(1,-1)\) calibration exhibits finite detectability by n=2. This test does not bound the required n for real zeta. This kills the strongest literal *wild topological discontinuity ⇒ Weil sign discontinuity* shortcut, while preserving the observer-language and nonuniform-contraction insights.
