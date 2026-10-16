# SUCC Carrier Proof Certificate v1

**Status: implemented integrity/dependency interface, with separately proved
worked mathematical examples.** The schema is not a theorem prover and is not
claimed universal. A source identifier is a declaration; a content hash binds
bytes; a Lean proof establishes its exact type in its axiom environment. These
three checks have different conclusions. RH PROVED: NO.

## Data and replay boundary

`observational_succ/source_proof_certificate.py` implements `audit_capsules`.
Each capsule records these mandatory fields:

- Mathematical data: claim ID and statement, source/category, operations and
  relations, target carrier, observation morphisms, topology/measure, universal
  property, comparison maps, hypotheses, dependency claim IDs, quantifier scope.
- Authority: one of CLASSICAL_IMPORTED, PAPER_PROVED, LEAN_KERNEL_PROVED,
  EXACT_FINITE_CHECK, TESTED_MODEL, UNVERIFIED, REFUTED; evidence paths and SHA256;
  for Lean, exact declaration names plus source, compiler receipt and axiom manifest.
- Access: source identity and epoch, permitted observations, constructible witness,
  available/required oracle, probe discrimination, proof theory, execution/cost.
- Adversarial evidence: validity-domain checks, negative examples, source mutations,
  and a replay procedure. Failed gluing, wrong normalizations and singular ranges
  are evidence, not anomalies to delete.

Conclusions have independent modes: THEOREM_UNDER_HYPOTHESES, INSTANCE_ONLY,
OPEN_TARGET or COUNTEREXAMPLE. EXACT_FINITE_CHECK and TESTED_MODEL cannot be
universal proof authority. Dependency cycles and missing nodes fail. An unresolved,
refuted or model-only dependency cannot silently become an established premise:
a proved conditional must explicitly retain `ASSUME:<claim_id>` in its hypotheses.
Such a conditional does not discharge that premise or assert the applied target.
An UNVERIFIED claim must remain OPEN_TARGET, and an OPEN_TARGET cannot wear a
proved authority label. The compatibility rule is checked in both directions.

Dependency edges mean use of the referenced conclusion. Open premise debt is
propagated transitively through conditional intermediates: a consumer of a
theorem assuming U must itself retain `ASSUME:U`. Ordinary written hypotheses
are also unioned across the dependency graph in `retained_hypotheses`. This
conservative interface has no semantic premise-discharge rule. Referencing a
conditional proposition as a proposition, rather than applying its conclusion,
requires a separately written theorem type and review; it cannot be inferred by
dropping the assumption at an edge. The independent audit found the missing
transitive check and a contradictory open/proved label in the initial version;
both failures are preserved with regression tests.

The auditor returns `STRUCTURE_AND_BYTES_VALID`, the *recorded* authority and
retained/open premises. It returns `semantic_authority_issued: null` and
`theorems_proved_by_this_audit: []`. An attacker can write a false paper or forged
transcript and compute its hash; this checker cannot turn it into a theorem.
Paper review must examine the derivation; Lean replay must actually invoke the
pinned kernel and inspect `#print axioms`; finite certificates need independent
arithmetic replay. The source-to-target semantic comparison remains a separate
obligation even after Lean succeeds. Completeness of the declared dependency
list is a separate semantic review obligation: metadata checks cannot discover
unstated assumptions in arbitrary prose. Commands in JSON are descriptive and are
never executed as arbitrary shell text.

The finite observation compiler DOES verify a mathematical certificate for its
entire declared finite table: it replays the factorization square or the explicit
collision. That bounded exact checker is not generalized to arbitrary analysis.
Likewise gluing grammar compatibility is an executable type/debt check, not a
proof that supplied hypotheses or source labels are true.

## PT-G01: the group-completion worked capsule

Let M=(N,+,0). On N×N set (a,b)~(c,d) iff a+d=c+b. This is an equivalence
relation: reflexivity and symmetry are immediate; transitivity follows by
cancelling the shared middle natural number in the two summed equations.
Addition [(a,b)]+[(c,d)]=[(a+c,b+d)] is well-defined because equivalent-pair
equations add. [(0,0)] is the identity and −[(a,b)]=[(b,a)]. Therefore the
quotient is an abelian group. The map [(a,b)]↦a−b is a well-defined bijective
group homomorphism onto Z: equality of differences is exactly the relation,
and every integer is a difference of naturals. The unit i(a)=[(a,0)] is
injective by cancellation and is not onto, since −1 has no natural preimage.

For any abelian group G and monoid homomorphism f:N→G, define
fbar([(a,b)])=f(a)−f(b). The equivalence relation makes this well-defined;
it is a homomorphism and fbar∘i=f. Every class is i(a)−i(b), so this extension
is unique. Thus Gr(N)≅Z by the universal property. The corresponding one-object
categories have endomorphism composition given by addition; formally inverting
the generating loop yields B(Z). B(N) itself is not equivalent to B(Z):
an equivalence would preserve invertibility, while its successor is not invertible.

This is a classical theorem with the complete elementary proof above. The
existing `edge_carrier_reconstruction.py` implements finite exact charts;
these charts do not prove the infinite universal property by enumeration.

## Worked capsule inventory

The machine-readable `PROOF_TEETH_CAPSULES.json` retains separate entries for:

1. PT-G01, one-loop group completion, PAPER_PROVED / classical integration.
2. Finite cyclic normalized Fourier pullback and quotient retraction,
   PAPER_PROVED plus EXACT_FINITE_CHECK receipts and the separately identified
   Lean finite-retract theorem where actually compiled.
3. Profinite Hilbert reconstruction, PAPER_PROVED with classical regular Haar,
   density and Hilbert-completion imports stated; no arbitrary global point
   becomes finitely programmable.
4. PT-C02, chi4 minimum residue observation, PAPER_PROVED; finite replay reports
   only its explicit decoder/witness and exact source bridge.
5. Finite-adele nonsplitting, PAPER_PROVED; finite quotient computation remains
   available but no additive representative selector can exist.
6. Source-preserved bounded self-adjoint positivity along a dense projector
   chain, a conditional PAPER_PROVED theorem; every finite stage's positivity
   is a quantified hypothesis, not inferred from a checked prefix.
7. Genuine four-low Suzuki Schur sign at a=1/2, UNVERIFIED / OPEN_TARGET.
   High coercivity and positive low compression are premises already proved
   in the source dossiers. They do not discharge the low Schur sign.

Additional formal and exact examples may be separate capsules rather than
promoting an entire paper because one of its algebraic sublemmas compiled.
The live axiom manifest and theorem types determine the precise formal scope.

## Independent replay

Run `python scripts/source_proof_certificate_probe.py` for structure/hash checks;
its output expressly makes no new theorem claim. Run the commands in each
capsule's replay field in the declared environment, and inspect the linked
proof and assumptions. The round's validation receipt records actual exit
codes, interpreter/compiler versions and source digests; historical CI is never
substituted. A source-file edit invalidates its capsule hash until reviewed and
re-recorded. Negative tests retain forged authority, missing premises, cycles,
unreachable artifacts and evidence path escape.
