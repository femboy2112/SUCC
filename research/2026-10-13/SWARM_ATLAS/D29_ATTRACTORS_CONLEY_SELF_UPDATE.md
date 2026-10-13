# D29 — Attractors, Conley structure, and reconstruction events

## 1. Original question

When an embedded observer updates itself, does it merely deflect an orbit, or reconstruct the map connecting source dynamics to its model? The faithful steelman asks which dynamical invariants survive a lawful observer change. We distinguish a carrier intervention, a report refinement, and an actual change of the source law. These cannot share an unqualified “self-update” theorem.

## 2. Existing mathematical context

[Conley–Easton (1971), §1](https://www.colorado.edu/amath/sites/default/files/attached-files/isolated_invariant_sets_and_isolating_blocks.pdf) supplies isolating neighborhoods and blocks. [Khandhawit–Lin–Sasahira (2018), §4.2](https://msp.org/gt/2018/22-4/gt-v22-n4-p03-s.pdf) records index pairs, pointed quotients, and continuation. [Franks–Richeson, §§2–3](https://arxiv.org/html/math/9910171) explicitly defines complete discrete orbits and filtration pairs; discrete indices additionally retain an index map. These are one classical literature lineage, not three independent proofs of SUCC. This dossier claims no academic novelty.

Repository antecedents separate original/current carriers (`checkpoint_meta_tower.py`), grammar reconstruction (`eodcs_evolutionary_discovery.py`), and hidden-topology ambiguity (`SOURCE_DRIVEN_DYNAMIC_BOUNDARY_REPAIR.md`). They motivate the question; none establishes Conley preservation.

## 3. Proposed SUCC objects

An observer presentation is \((X,\Phi;Y,\Psi;\pi)\), with locally compact metric carriers, continuous **full flows** \(\Phi_t,\Psi_t\), and continuous surjective \(\pi\) satisfying

\[
\pi\Phi_t=\Psi_t\pi\qquad(t\in\mathbb R).
\]

Proper means inverse images of compact sets are compact. Define \(\operatorname{Inv}_\Psi N=\{y:\Psi_t y\in N\text{ for every }t\in\mathbb R\}\). A compact isolating neighborhood satisfies \(\operatorname{Inv}N\subset\operatorname{int}N\). A compact trapping neighborhood is nonempty, forward invariant, and satisfies \(\Psi_TN\subset\operatorname{int}N\) for some \(T>0\). Source tags are declared bookkeeping; a complete transition table is simulator access, not sensor authentication.

## 4. Candidate theorem

**D29-A (CLASSICAL; elementary local derivation).** For every proper presentation and compact isolating \(N\subset Y\),

\[
\operatorname{Inv}_\Phi(\pi^{-1}N)=\pi^{-1}(\operatorname{Inv}_\Psi N),
\]

and \(\pi^{-1}N\) is isolating. If \(N\) is trapping, \(A=\bigcap_{t\ge0}\Psi_tN\) pulls back to the compact trapping attractor \(\pi^{-1}A=\bigcap_{t\ge0}\Phi_t(\pi^{-1}N)\).

**D29-B (CLASSICAL; finite discrete version).** For finite deterministic maps \(f:X\to X,g:Y\to Y\), surjective \(\pi\) with \(\pi f=g\pi\), and every \(N\subset Y\),

\[
\pi(\operatorname{Inv}_f(\pi^{-1}N))=\operatorname{Inv}_gN.
\]

Here Inv uses bi-infinite orbits. The stronger inverse-image equality holds if \(f\) is bijective, but generally fails otherwise. For every \(x\), eventual cycles satisfy \(\pi\Omega_f(x)=\Omega_g(\pi x)\); periods can shrink.

## 5. Proof attempt

For A, an entire source orbit stays in \(\pi^{-1}N\) exactly when its projected orbit stays in \(N\). Properness gives compactness; continuity gives \(\pi^{-1}(\operatorname{int}N)\subset\operatorname{int}(\pi^{-1}N)\), proving isolation. Full time supplies

\[
\Phi_t(\pi^{-1}N)=\pi^{-1}(\Psi_tN):
\]

for the reverse inclusion, apply \(\Phi_{-t}\) and the intertwining identity. Pull back forward invariance, strict trapping, and the intersection. Nested compact trapping images approach their intersection: otherwise a sequence outside an open neighborhood has a convergent subsequence in the intersection, a contradiction.

For B, bi-infinite orbits in finite deterministic graphs lie on cycles: an arbitrarily long backward history repeats, and determinism forces the forward trajectory onto that cycle. Projection carries source cycles into target cycles. Conversely choose a lift of any target cycle; its forward orbit stays over that cycle and eventually reaches a source cycle whose image covers it. This proves the image equality and orbit statement. If \(f\) is a permutation, every point over a target invariant cycle has its entire two-sided orbit over it, proving the stronger equality. These are written proofs; finite enumeration is regression evidence, not universal certification.

## 6. Crucible

**Proper projection changes the index.** On \(X=\mathbb R\times S^1\), let \(\Phi_t(x,\theta)=(e^{-t}x,\theta)\); on \(Y=\mathbb R\), let \(\Psi_t(y)=e^{-t}y\), with \(\pi(x,\theta)=x\). The projection is proper and intertwines. The genuine blocks are \([-1,1]\times S^1\) and \([-1,1]\); their invariant sets are \(\{0\}\times S^1\) and \(\{0\}\). Both have empty exit sets, so index pairs are \((N,\varnothing)\), with a disjoint basepoint added. Their indices are \(S^1_+\) and \(S^0\). Reduced \(H_1\) is respectively \(\mathbb Z\) and zero. Thus the induced quotient map is not a homotopy equivalence.

**Images lose isolation and attraction.** Give \(\mathbb R\sqcup\{p\}\) and \(\mathbb R\) identity flows. The proper surjection is identity on \(\mathbb R\), with \(p\mapsto0\). The open component \(\{p\}\) is an isolated attractor; its image is neither isolated nor attracting, since all neighboring target points remain fixed. Pullback and forward-image assertions differ.

**Nonproperness.** For \(\Phi_t(x,z)=(e^{-t}x,e^tz)\), the same coordinate projection intertwines but pulls the target block back to an unbounded strip. Its invariant set is the noncompact vertical line. The observed sink also hides the source saddle at the origin.

**Noninvertibility.** Take \(f=(1,1),\pi=(0,0),g=(0)\). Then \(\operatorname{Inv}X=\{1\}\), whereas \(\pi^{-1}\operatorname{Inv}Y=X\). A two-cycle projected to a singleton separately erases period. Identity observation with \(f=(1,1)\), wrongly declared \(g=(0,1)\), breaks intertwining at state 0.

## 7. Verdict

SURVIVES: D29-A/B at **CLASSICAL**, with explicit hypotheses and local proofs. FAILS: unrestricted index preservation, forward-image isolation/attraction, and inverse-image equality for noninvertible dynamics, each **REFUTED** by its receipt. The exact probe is **TESTED MODEL**: 5,284 lawful presentations, 35,032 neighborhoods, 20,830 orbit cases, 70,064 independent algorithm comparisons; all 1,954 bijective pullbacks pass, while 8,043 nonbijective cases violate the stronger identity. A separate six-cycle calibration checks all eight target neighborhoods and period reduction 6→3; it is not a blind empirical holdout.

## 8. Remaining obstruction

Real source access, noisy observer maps, and infinite noninvertible semiflows remain outside the proof. The smallest next obstruction is a proposed observer collapse with contractible fibers: require an actual induced index-pair quotient homotopy equivalence before upgrading index preservation. Properness alone already failed. Continuation requires a continuous family with a common isolating neighborhood; a sudden reconstruction event does not supply that hypothesis.

κ is exact simulator contact, φ is hypothesis-relative derivability, σ is declared transition/source mapping, and ρ risk is the commitment to “self-update preserves structure.” Predictive separation uses exact successor tables; no lawful phasor phase or probabilistic truth score is defined. The two finite algorithms share inputs and author, so are implementation checks, not independent source bearings.

## 9. Cross-domain connection with actual maps

Use \(C=\{0,1,2\},f=(0,1,1)\) and old report \(s=(0,1,0)\). States 0 and 2 have the same report but successor reports 0 and 1: no autonomous old transition exists. Reconstruction takes \(q=\mathrm{id}_C\), \(F=f\), and forgetting map \(r=s\), so

\[
qf=Fq,\qquad rq=s.
\]

The old itineraries 000,111,011 certify that all three states require separation in any deterministic refinement preserving \(s\). This is a minimal source/model reconstruction. By contrast, intervening \(\delta(0)=2\) moves a carrier from the 0 basin to the 1 basin without changing \(f\) or repairing the old report. An original-source predicate remains evaluated at the original state. These are actual finite maps connecting causal-carrier and automata-realization viewpoints; no physical discovery claim follows.

## 10. Deliverables

`D29_probe.py` independently implements graph pruning and cycle traversal without importing runtime modules; `D29_RECEIPT.json` preserves exact controls and exhaustive bounded cases. `D29_VALIDATION.json` records commands, exits, hashes, source contact, and inspected antecedents. Immutable source parent: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. Imported foundational dossier: origin commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a`, blob `04408ed96bd369b5063868eb5ad5664824d18043`, byte-equal to the originating repository. New D29 files only; no archive, runtime, shared registry, full suite, compiler, or push changes. Final mathematical acceptance awaits independent crucible and principal review.
