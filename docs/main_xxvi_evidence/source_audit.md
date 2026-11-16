# Main XXVI immutable-source audit

Audit boundary: donor commits #646 a991aa8ada68f5fa9d18bbc6fb6aaf2da842b281; #648 9d1a2bf6c3ed8c767003bc78f366269b8b3f48cc; #649 55236438e6f38dadcb207011ff3bc7086d41fea0; #651 94c7252ac7db3c8b14229544087119bd9cc01933; #653 fb3a685e40798417077ba548cda62f10eff0cb41; #654 595c4e8f64b5a3578f343d486eb98c2440bd7ef1. Read AGENTS.md, docs/METHOD.md and provenance/IMPORT_MANIFEST.json first. All source reads used immutable Git blobs; shared integration checkout was not modified. Same-model audit, not independent external refereeing or formal-kernel certification.

## Required repairs

1. **Refuted target-change assertion.** `research/2026-11-15/bbp_chiral_holonomy/THEOREMS.md:199` currently says the g(n)=2n² mutation changes the real source/π target and is not another representation of the same trajectory. Replace that sentence with: “The mutation changes the forcing presentation and destroys the original four-pole source passport, but does not change the completed real π orbit: the telescoping correction has total sum zero, and the genuine mutated tail is T̃_n=T_n−2n². Thus Ũ_n+T̃_n=U_n+T_n. It is a different source presentation of the same completed target, not an authenticated original BBP forcing. The refuted target-change reading is retained in the Main XXVI claim supplement and donor history.” Retain the valid commutator counterexample and its arithmetic tests. #651 PS-07 already supplies the correct derivation.

2. **Impossible completed-phase discriminator.** `research/2026-11-15/bbp_gamma_mellin_phase_bridge/THEOREMS.md:188` says an estimate “must separate original zero seed from coherent wrong seed and the #648 coboundary mutant.” Repair to distinguish the two kinds of control: “It must distinguish the original zero seed from the coherent wrong seed. For the g(n)=2n² coboundary, it must either preserve its completed-circle conclusion under the explicit gauge transport or state an original-forcing hypothesis that makes the estimate inapplicable; identical completed orbits cannot be separated by any completed-phase-only detector.” Apply the same distinction in `NEXT.md:11` and `bbp_chiral_holonomy/THEOREMS.md:205`. The existing NEXT wording “fail or be inapplicable” can survive if inapplicability explicitly means failure of the original source passport. Also amend `bbp_random_norm_weaving/OBSERVATION_PROTOCOL.md:26` so “failing for ... chirality mutant” refers to the source-dependent hypothesis/readout, rather than the shared completed-circle target. The primary signed arithmetic objective can remain source-specific; target separation cannot be its coboundary control.

3. **Lag-zero boundary.** `research/2026-11-15/bbp_pi_slot_lifting/THEOREMS.md:160` introduces nonnegative ℓ but (PS12) claims strict positivity. Change to “For positive integer lag ℓ”; optionally add “At ℓ=0 the norm is exactly zero.” No mathematical asymptotic or code change needed.

## Exact gauge derivation and limits

For any real sequence g with g(0)=0 and g(N)/16^N→0, define r̃(n)=r(n)+g(n)−16g(n−1). Finite telescoping gives Ũ_n=U_n+g(n) and P̃_N−P_N=g(N)/16^N. Thus x̃=x. For fixed n and finite J, the tail correction is exactly

`Σ_(j=1)^J 16^(−j)[g(n+j)−16g(n+j−1)] = −g(n)+16^(−J)g(n+J)`.

The last term tends to zero, hence T̃_n=T_n−g(n) and the completed real lifts coincide. Integer-valued g additionally preserves the uncompleted real circle phase and reduced odd denominator; it changes the integer winding. For g(n)=2n², the mod-16 return jet adds 4n, changing the source commutator from −I to +I. Therefore original chirality is source-presentation-dependent, not a completed-target invariant. The polynomial mutation loses original positive/decaying forcing; its tail need not retain the positive Green moment model. Do not substitute the original positive T_n for the genuinely mutated T̃_n.

## BC-0 origin proof review

The #646 paper proof is sound under the standard convergent 2-adic logarithm homomorphism in K=Q₂(√2,i):

- `(z²−2)(z²+2)(z²−2z+2)(z²+2z+2)=z⁸−16` enumerates all eight roots.
- Four roots annihilate Q; the pair 1±i has torsion logarithm zero; the pair ±√2 has the same weight αQ(α)=−16 and logarithms summing to log₂(−1)=0.
- Expanding `αQ(α)log₂(1−α)` and root filtering reproduces the four original signed poles with factor 1/128.
- All root logarithms converge since v₂(α)=1/2>0. The finite sum and convergent series interchange is legitimate.

The independent symbolic checks and finite modular checks are supporting calibration, not a substitute for the paper logarithm argument. Do not promote this to Lean or external-peer-review status. The stable holonomy congruences also have a finite source truncation proof that does not depend on BC-0.

## Claims that survive within scope

Inherited theorem: exact source identities, integer-winding attachment, BC-0 as a paper result, finite holonomy congruences and source-loop chirality with the explicit original-forcing passport.

Inherited transport/instrument: #649 shared-threshold source moment compiler and common-versus-independent reference distinctions; #651 exact source-resolvent realization, Poisson complex phase estimator and its variance; #654 continuous-depth source difference square and Gamma/Green asymptotics, including signed source-tail cancellation at moving frequencies.

Source-only Gamma attenuation does not imply completed π cancellation. A same-forcing seed s=−x gives U_n(s)=−T_n and completed phase identically zero while all forcing-only moment/Gamma windows remain identical. #654 GM-07 is a valid moving-frequency tail result: p=k+2, h_B/B^p=c_B→∞, c_B/B→0 implies the source-tail mean is O(c_B⁻¹+c_B/B). Multiplication by the unresolved rational history phase can undo that cancellation; this neither supplies fixed-frequency Weyl decay nor R0.

#653's dominant least-rate forcing channel yields a valid nonvanishing/right-half-plane multiplier argument; its positive rate-mixture upper Gamma envelope is separate. Nonzero forcing transforms cannot be transferred by positivity to a coherent mixture of complex Green transforms. Its resonance residual is an auxiliary source result; the unwrapped orbit and seed are not encoded by a forcing-only transform. No further contradictory target promotion found in the sampled load-bearing statements.

Equivalent instrument: all-harmonic weighted Weyl energies and their finite-expected-cost stochastic readouts remain equivalent tests whose required asymptotic decay is open. No proof status promotion follows from target access or variance control.

Refuted inference: interchange E and exp/floor, erase the integer winding before 2-adic observation, identify independent-time random references with common-reference experiments, or identify source presentation chirality with completed-circle geometry.

## Validation actually executed

Evidence JSON: `source_audit_evidence.json` alongside this report. Donor modules and tests were loaded directly from Git blobs into memory, using the actual original test source, without writing to the integration checkout.

- 220 donor tests passed, zero failures/errors, 11.195 seconds (full output in JSON). Modules cover #646 source circle, #648 loop/chirality, #649 weaving, #651 π-slot, #653 disintegration and #654 Gamma plus signed-shell code.
- Separate pure-Fraction implementation: 129 prefix/recurrence cases; 80 exact finite-tail-remainder cases; original U₁=47/15 has full arithmetic residue 1 mod 16, but reducing its fractional part first changes that residue and its first real digit is 2.
- Separate SymPy algebra: Q factorization, complete eight-root polynomial, four vanishing Q roots, ±√2 weights, 20 exact root-filter coefficient checks.
- Separate 64-depth finite modular origin checks pass; no finite-to-infinite inference claimed.

These replays validate donor blobs, not the exact final combined tree. Root must rerun applicable focused tests after repairs and the mandatory complete integration gates.

## Remaining arithmetic dependency cut

No new original-zero all-large-shell signed estimate is established by this audit. Retain the original source/seed/rational winding tuple and ask for a source-selected uniform positive margin in an existing calibrated fixed-frequency carry/interference detector. #651 gives exact rational-plus-tail phase transport and #654 controls the tail at its own source scales; the missing edge is the signed rational history restriction, not another positive marginal identity. The coboundary control tests passport/gauge handling; the coherent wrong seed remains the decisive control against an unsupported source-only-to-orbit implication.

## Applied repair and combined-working-tree retest

The six research documents above were repaired in the combined checkout. The refuted target-change claim remains quoted and ledger-labeled; the refuted same-target discriminator and lag-zero endpoint are explicitly preserved as corrections. `tests/test_main_xxvi_source_transport.py` adds seven independent exact regressions, importing no research implementation.

`source_audit_retest.json` records eight actual commands on the repaired combined working tree: 7 new regressions and 231 existing source tests (35 circle/temporal, 26 loop, 20 chiral, 35 randomized weaving, 53 pi-slot, 28 disintegration, 34 Gamma/Green). **238 tests passed, no failures/errors.** The receipt includes repaired-file hashes and the starting Git HEAD. This focused working-tree receipt does not replace full validation of the final immutable integration candidate. `git diff --check` and the corrected chiral claim-ledger JSON parse also passed.
