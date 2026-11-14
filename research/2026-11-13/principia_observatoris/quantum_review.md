# Quantum/classical workstream review

## Scope and provenance

Read in the local PR #618 descendant: `AGENTS.md`, `docs/METHOD.md`, all nine sections of `research/2026-11-13/causal_relevance_proximity/RESEARCH_NOTE.md`, `observational_succ/quantum_records.py`, `tests/test_quantum_records.py`, existing O03 and PBR-05 ledger entries. The written result is `docs/principia_observatoris/05_effective_classicality.md`. Existing originals are unchanged.

This is a same-model workstream, not external independent peer review. No proof-assistant verification or empirical quantum experiment is claimed.

## Derived theorems and truth debt

| ID | Proven statement | Load-bearing assumption | What remains unpaid |
|---|---|---|---|
| PO-C1 | Individual Heisenberg instrument components preserve D iff compressed state q has a unique stochastic instrument quotient; all adaptive finite transcripts descend | Fixed finite-dimensional commutative D; all outcomes, actions and density states; CP and TP normalization | Source authenticity, access, possible alternative classical realizations |
| PO-C2 | Uniform one-step compressed-law error ε yields transcript TV error ≤Nε for every policy of ≤N steps | Uniformity over all density states and allowed actions, nonnegative normalized comparison kernels | Constructing a sharp source-specific ε |
| PO-C2a | All-state one-step error bound iff a finite family of signed Hermitian defects is bounded by 2εI | Authenticated finite channel matrices; all sign vectors | Efficient certificates and external source authentication |
| PO-C3 | Pointwise fixation of D is equivalent to nonselective q-nondisturbance, preserved by every future D-closed protocol | Outcome ignored; same subsequent policy; future closure | Stronger selective/state nondisturbance |
| PO-C4 | Local trace-preserving channels do not alter remote marginals | Tensor-factor localization, no communicated outcome or later coupling | No new physical result; already PBR-05 |

Proofs use explicit trace duality, separation by pure states, and an l1 telescoping inequality. Classical ingredients are attributed; internal novelty is a unified theorem-and-countermodel interface, not a priority claim.

## Sharp controls for the constructive laboratory

All matrices here are rational (Kraus vectors may contain radicals, but no radical is needed for the map).

- P0=diag(1,0), P1=diag(0,1), Q±=(1/2)[[1,±1],[±1,1]].
- Positive descent: Z branches ρ↦P_iρP_i. On q=(ρ00,ρ11), K_0=[[1,0],[0,0]], K_1=[[0,0],[0,1]]. Any allowed adaptive sequence matches classical branching.
- Positive stochastic control: Λ(ρ)=(2/3)ρ+(1/3)XρX induces [[2/3,1/3],[1/3,2/3]]. Compose with Z.
- Mutation C-X1: Φ±(ρ)=tr(Q±ρ)P0. Sum dual preserves D, individual duals do not. Inputs Q+ and Q− share q=(1/2,1/2) but produce (1,0) and (0,1). Expected rejection if a verifier requires outcome-wise closure.
- Effect-only mutation: one-outcome H channel has effect I, yet H*P0H=Q+∉D. Use HρH=(1/2)H0ρH0, H0=[[1,1],[1,-1]], to stay rational.
- Hidden coherence: Q+ and I/2 have identical complete Z/bitflip/phase transcript laws. Hadamard then Z gives plus/zero probability 1 versus 1/2.
- Disturbance: ignored Z sends Q+ to I/2; diagonal is unchanged, X-plus probability changes 1→1/2.
- No signal: Bell density (1/2)[[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]. Local ignored Z leaves B diagonal (1/2,1/2), while conditioned branches give P0 or P1. A branch probability cannot be silently treated as a sender-controlled action.
- Chaotic classical control: doubling map with x=0,y=2^−(N+1) and threshold 1/2 gives first distinct readout at n=N. Mathematical classicality survives long-horizon prediction failure.
- Shortcut control: classical XOR gate from x to y at arbitrary assigned separation L violates any chart-based one-step locality inference without a finite-propagation premise.

## Primary-source audit

Retrieved on 2026-11-13 (client date):

1. Davies–Lewis publisher page, DOI 10.1007/BF01647093; abstract confirms instrument/sequential-measurement provenance. Full subscription text not used.
2. Carlen–Maas author-hosted PDF, `https://www.janmaas.org/wp-content/uploads/2016/09/2016-Carlen-Maas.pdf`, §4 and Theorem 4.2: invariant commutative subalgebra gives a classical Markov chain under its stated semigroup conditions. The manuscript's instrument extension is derived directly; it is not attributed verbatim to their theorem.
3. Watrous author-hosted chapter `https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf`, standard definitions. No copies added to repository.

This bounded search establishes close classical antecedents, not originality. Statements from search summaries were not used as load-bearing proof premises.

## Audit questions

1. Does any branch normalization divide by zero? No; the proofs propagate unnormalized PSD branches, including zero branches.
2. Do adaptive actions undermine equivalence? No; along each transcript they select the same next matrix, and policy randomness has the same weights.
3. Is nonselective channel closure enough? No; C-X1 decisively refutes it.
4. Does initial readout-law equality suffice? No; H followed by Z refutes it.
5. Is algebra closure necessary for all possible classical models? Not claimed. It is equivalent to the specified q-state Markov quotient on all density states.
6. Does finite-dimensionality imply finite memory cost for arbitrary protocols? Not claimed. The theorem is a finite-horizon semantic law; policy execution/resource assumptions remain separate.
7. Are the geometric and classicality claims conflated? No. Arbitrary classical XOR shortcuts and chaotic readouts separate them.

Executable results, if added by the integration agent, must be recorded by command and current-tree scope in the main validation record. This file does not assert those runs.

## Workstream execution receipt

On the local PR #618 descendant, the command

```sh
python -m unittest discover -s tests -p 'test_quantum_records.py' -v
```

completed with **5 tests in 0.004s, OK**, exit 0. This is the existing finite quantum-record regression, not a test of physical source authenticity.

A separate one-off standard-library Fraction implementation compared 12,096 quantum/coarse branch vectors: six rational initial states, 16 feedback policies, all binary histories through depth six, using Z and the 1/3 bit-flip-then-Z instrument. Every vector agreed exactly. It also checked the two reset outcomes for Q±, ignored-Z disturbance Q+→I/2, Hadamard exposure Q±→P0/P1, and the existing Z adapter. This finite exploratory run is reported as **observed calibration**, not a retained standalone executable or universal proof. The durable verifier below separately supplies an exhaustive matrix-certificate check.

The source and documentation matrices were reviewed for memory typing: composing one-step maps assumes H includes needed memory, or that reduced dynamics has a justified composable instrument law. Omitting environmental memory is not licensed by the theorem.

PO-C2a adds an exact finite certificate for C2's uniform premise: l1 duality reduces all density-state tests to 2^(m|O|) semidefinite inequalities. This is a proved finite reduction, not an empirical tomography claim. The integrated laboratory need not exhaust it for the universal paper derivation to hold, but any claimed executable certificate must retain every required sign.

## Durable PO-C2a exact certificate

Command run successfully (exit 0):

```sh
python research/2026-11-13/principia_observatoris/quantum_certificate_probe.py --output research/2026-11-13/principia_observatoris/receipts/quantum_certificate.json
```

Observed output: **64 sign matrices**, three accepted positive certificates (Z ε=0; 1/3-bitflip-then-Z ε=0; reset-X ε=1/2), the false reset-X ε=1/3 certificate rejected, and three invalid instrument/kernel controls rejected. Each case exhausts its 16 sign vectors and retains each bound matrix and all principal minors. At the false epsilon the witness determinant is exactly **−5/9**. Exact states Q± attain error **1/2**, so that is the optimum for the declared reset comparison kernel.

The receipt pins the executable SHA-256 and retains all sign matrices, defects, failures and rational outputs. The checker is restricted to real 2×2 matrices and diagonal coarse algebra; it does not claim to implement general complex Hermitian certificates. Under the proved C2a reduction these exact matrix certificates are all-state statements for the displayed finite maps, not finite state-sample extrapolations.

Following same-model review, the random-policy proof explicitly conditions on the entire private seed independent of the initial carrier, proves the deterministic-policy identity/bound, then averages. This avoids an unjustified conditional independence claim about controller memory after observing outcomes.
