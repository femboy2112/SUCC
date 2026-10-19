# Institute nucleus: execution and acceptance report

**RH PROVED: NO.** This research increment supplies proved source-descent
theorems, a coherent RH-independent operator paper candidate, an authentic
Gamma-tail improvement, and a checked theorem-contract graph. It does not
establish academic novelty, decide the first Suzuki Schur sign, or complete
the broader institute mission.

## Delivery and source boundary

Branch: `research/institute-nucleus-2026-10-18`, isolated worktree
`/media/leah/SPANKBANK/SUCCYBOI/SUCC-institute`, based directly on default
`main@610efacf02556e1c5922bc5d4e87d0087f19b446`. The submitted Git commit
identifies this report's exact version; delivery head and draft-PR URL are
reported separately after commit. The original worktree and archival sources
are preserved. No merge, release, tag, license change or public-paper
submission is performed.

The [reconstruction](INSTITUTE_RECONSTRUCTION.md) records actual ancestry,
exact heads and captured CI for drafts #153–177. None of those heads was
integrated into main at the captured snapshot. Source copies and common
ancestry are factored before counting evidence. The historical import
manifest's 72 entries and the original signed source blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178` remain unchanged.

## Strongest mathematical results

1. **Lawful causal descent — Lean kernel.** For arbitrary sets and partial
   deterministic labelled actions, a surjective map admits a commuting
   quotient action if and only if projected one-step transitions are constant
   on every fiber. Every accepted finite quotient run then lifts from every
   fixed original representative, preserving the full accepted label word.
   For arbitrary relational transitions and finite words, forward reachability
   is equivalent to one complete source path; a backward exclusion exists
   exactly when no path exists. Edge-preserved source identity propagates.
   [Paper and exact scope](INSTITUTE_CAUSAL_DESCENT.md),
   [eight formal declarations](../../formal/InstituteCausal.lean).

2. **Atomic/Haar classification — paper proved.** For any subset S of primes,
   the restrictions of the multiplication shifts on `ell2(N+)` and the
   normalized cutoff-division isometries on `L2(Zhat,Haar)` admit a nonzero
   bounded adjoint-preserving intertwiner exactly when `sum_(p in S) 1/p`
   converges. In that case the tuples are unitarily equivalent and all such
   intertwiners are classified by their wandering-space maps. In particular,
   every all-prime bounded star-intertwiner in either direction is zero.
   Finite Möbius projections converge strongly to the atomic vacuum and to
   zero on Haar space, respectively; neither convergence is in operator norm.
   [Full proof and prior art](INSTITUTE_ATOMIC_HAAR.md).

3. **Exact replacement interface — paper proved.** Algebraic intertwiners
   `c00 -> Dprime(Zhat)` are classified by distributions supported on the
   profinite units, with `J_eta(e_n)=n^(-1/2)(m_n)_*eta`. The canonical Dirac
   map extends continuously on `sum |a_n|/sqrt(n)<infinity` and on
   `ell2(n^s)` for every s>0. Its unweighted `ell2 -> weak Dprime` graph is
   not closable: harmonic vectors tend to zero while their images tend to
   additive Haar. Transpose actions and test domains are explicit; there is
   no asserted Hilbert adjoint on the distribution space.

4. **Authentic Gamma envelope — paper proved with exact controls.** For every
   J>=1, d=4J+1 and real xi, the original omitted Gamma multiplier satisfies

   ```text
   (1/2)log(1+4xi²/d²) + 8xi²/[d(d²+4xi²)]
       <= m_J(xi) <= (1/2)log(1+4xi²/(d-2)²).
   ```

   Shift 2 is optimal uniformly within this upper-bound family. Consequently
   the tail action is at most `13/[16(d-2)] ||F'||` on zero-extended H1_0,
   or `2/(d-2)² ||F''||` on H2_0, where both value and derivative traces
   vanish. These are derivative-domain estimates, not an L2 spectral gap.
   [Proof, domains and source comparisons](INSTITUTE_ARITHMETIC_ANALYSIS.md).

5. **Actual Schur progress — conditional exact replay.** Keeping the pinned
   PR177 source, all signed channels, trials and finite action residuals fixed,
   the sharper Gamma budget improves each J8 and J24 lower matrix by an exact
   positive scalar multiple of the identity. Both parity lower blocks remain
   negative definite. This is a failed sufficient positivity certificate,
   not negative energy of the actual completed Weil form. The inherited
   source-adapter and all-high K-coercivity premises remain explicit debt.

6. **Fixed-method obstruction — paper proof and exact rational witness.**
   In both J24 parity blocks the retained matrices already satisfy
   `kappa*T11-M11<0`. Since M is positive semidefinite, for every eta>0 and
   every positive semidefinite error allowance D,
   `T-[(1+eta)M+D]/kappa` has a negative first diagonal entry. Thus no positive
   Young parameter or error-budget reduction, even to zero, can certify
   positivity using these same T, M and kappa. The obstruction does not require
   assuming the analytic correctness of the inherited coercivity premise;
   it is an algebraic statement about the retained sufficient-bound family.
   [Exact decomposition](INSTITUTE_GAMMA_ETA_SOURCE.json),
   [parameter search and universal witness](INSTITUTE_GAMMA_ETA_SEARCH.json).

## Validation and independent checks

Receipts include literal commands, versions, timestamps, exit codes, logs,
hashes and dirty-tree status. They are execution observations, not invented
final-commit attestations. Development and metadata-collection failures remain
in the record. Later focused checks cover changes made after full discovery.

| Gate | Actual local result | Receipt |
|---|---|---|
| Source provenance | PASS, 72 preserved entries | [baseline](institute/receipts/baseline-provenance.json) |
| Baseline full Python suite | PASS, 5,056 tests; system mpmath 1.2.1 was below the declared dependency floor | [baseline suite](institute/receipts/baseline-suite.json) |
| Corrected-environment full suite | PASS, 5,102 tests in 553.712 test seconds; Python3.12.3, isolated mpmath1.3.0 | [full-suite receipt](institute/receipts/final-suite.json) |
| Final focused regressions | PASS, 55 tests, including independent J24 decomposition reconstruction | [delivery focused](institute/receipts/delivery-focused.json) |
| Actual theorem graph | PASS, 14 records with unverified dependencies retained | [delivery registry](institute/receipts/delivery-registry.json) |
| Observer and ordinal probes | PASS | [observer](institute/receipts/observer.json), [ordinal](institute/receipts/ordinal.json) |
| New core Lean | PASS, eight declarations; deliberate false proof rejected | [kernel receipt](institute/kernel_receipt.json), [axiom manifest](institute/axioms.json) |
| Existing NoGhost Lean baseline | PASS with false-proof control | [baseline Lean](institute/receipts/baseline-lean.json) |
| Genuine source replay | PASS execution and exact consistency; positivity certificate fails | [J8](INSTITUTE_GAMMA_SCHUR_REPLAY.json), [J24](INSTITUTE_GAMMA_SCHUR_J24.json) |

The Lean source uses no external imports, `sorry`, custom axioms or native
decision shortcuts. Four declarations require no axioms; the others use only
the explicitly reported `propext` and/or `Classical.choice`. Paper functional
analysis has not been promoted to Lean authority.

The [hostile audit](INSTITUTE_HOSTILE_AUDIT.md) independently derived the
operator and causal results, checked exact rational certificates and replayed
the archived J8 source. A kernel-authority comparison bypass was reproduced
and repaired. It also corrected a false global-minimum label, matrix-sign
wording, failure-transcript wording and an experimental domain mismatch.
These are separate implementations/review streams within one model lineage;
they are not external referees or independent mathematical source families.

Hosted CI is a separate gate. Its final-head status is reported from GitHub
after delivery; local success and historical PR checks do not imply it.

## What SUCC gained, and what remains open

The [claim supplement](../../docs/CLAIM_SUPPLEMENT_INSTITUTE.md) and
[machine graph](institute/theorem_registry.json) attach quantified claims to
domains, hypotheses, explicit transports, source Git identities, evidence
hashes, proof authority, prior art, debt and next probes. New guards detect
declared hypothesis loss, carrier/topology changes without proved comparison,
paper-to-kernel authority laundering, stale byte receipts, stale claimed CI
and finite-instance promotion. The checker validates recorded contracts; it
cannot infer omitted semantic dependencies or certify prose truth. Fresh
fixed-source Lean compilation is a distinct action.

Exact source-history primal enumeration and backward exclusion are independent
finite algorithms. Moore refinement and pair-BFS provide counterexample-guided
finite theorem calibration. Neither is a new universal theorem-discovery
algorithm, an unrestricted Farkas solver, or a general stochastic gluing
theorem. The pre-existing EODCS framework is preserved; no broader evolutionary
search extension is claimed in this increment.

Classical: partial-action congruence, relational path gluing, minimization,
Haar scaling, Wold ingredients, convex quadrature and Plancherel. The
infinite-family Wold failure is already in the literature. Project results:
the explicit arithmetic threshold/classification, distribution interface and
nonclosability witness, sharper source-normalized Gamma envelope, exact replay,
and integrated proof-contract checks. Their independent academic novelty and
significance remain unestablished.

Refuted routes include bounded all-prime Hilbert identification; continuous
or closable unweighted Dirac extension; an upper Gamma log envelope with
uniform shift below two; hidden-state splice as one source history; supported
transcript as universally available public policy; and paper comparison as
kernel authority. Each has a proof or retained adversarial receipt.

Remaining obligations include external prior-art/referee scrutiny; formal
measure/operator proofs; genuinely new causal descent beyond the classical
finite deterministic/relational class; a common completed signed trace domain
retaining Gamma, poles, contact, conductor and phase; independent proof of the
inherited all-high K inequalities; and a decisive first-window high-response
bound. All-radii positivity remains an additional, separate problem.

## Next three discriminating experiments

1. Compare the sharp prime-subset and distribution classification with exact
   infinite-isometry/number-theoretic operator prior art, then formalize the
   Haar-null common-kernel theorem. This decides novelty and increases proof
   authority without relying on RH.
2. Audit the inherited K-relative coercivity and source-adapter maps on the
   same primitive domain. A failed premise changes the interpretation of every
   conditional Schur receipt; source hash equality alone cannot settle it.
3. Replace worst-case column error aggregation with a certified source-relative
   residual Gram or a richer legal trial space, including all Gamma and boundary
   channels. Test the actual infinite response before increasing radii.

**Publication readiness:** suitable for a reviewable working-paper draft and
reproducible code submission. Not ready for a novelty-certified journal claim,
an institute-wide completion claim, or an RH announcement.
