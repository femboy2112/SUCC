# WILD-SUCC — source-indexed embedding and infinitely nested holonomy ledger

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
