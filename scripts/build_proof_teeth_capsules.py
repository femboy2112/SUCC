#!/usr/bin/env python3
"""Bind reviewed worked-example declarations to their current evidence bytes.

This producer is untrusted. Its output records authority; it proves no theorem.
The independent auditor checks declared dependencies/hashes, not proof validity.
"""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.source_proof_certificate import evidence_file

D = "research/2026-10-15/"


def capsule(cid, statement, source, target, operations, observation, topology,
            universal, comparison, hypotheses, evidence, witness, negatives,
            replay, authority="PAPER_PROVED", dependencies=(), mode="THEOREM_UNDER_HYPOTHESES"):
    return dict(claim_id=cid, statement=statement, authority=authority,
                source=source, operations_relations=operations, target_carrier=target,
                observation_morphisms=observation, topology_measure=topology,
                universal_property=universal, comparison_maps=comparison,
                source_identity="Declared mathematical source: "+source,
                source_epoch=0, hypotheses=list(hypotheses), dependencies=list(dependencies),
                scope="UNIVERSAL", conclusion_mode=mode,
                evidence=[evidence_file(ROOT, path, kind) for path, kind in evidence],
                access=dict(permitted_observations=observation, constructible_witness=witness,
                            oracle="None supplied; arbitrary global inputs are not finite programs",
                            probe_discrimination=negatives,
                            proof_theory="Classical mathematics with the listed imports and hypotheses",
                            execution_cost="Finite symbolic proof; executable resource limits stated in modules"),
                adversarial=dict(domain_tests="See exact assumptions and linked tests; source tags are declarations",
                                 negative_examples=negatives,
                                 source_mutations="Epoch/identity mismatch refused; canonical source bytes retained",
                                 replay=replay))


def build():
    spec = D+"SOURCE_PROOF_CERTIFICATE_SPEC.md"
    haar = D+"PROFINITE_HILBERT_RECONSTRUCTION.md"
    obs = D+"MINIMAL_OBSERVATION_CARRIER_THEOREMS.md"
    glue = D+"SOURCE_GLUING_PROOF_TEETH.md"
    schur = D+"FOUR_LOW_SCHUR_CROSSPOLLINATION.md"
    return [
        capsule("PT-G01", "Gr(N,+) is isomorphic to (Z,+); the unit is proper and injective",
                "Natural additive monoid", "Integer additive group", "Pair differences and cancellation",
                "Exact natural pair (a,b)", "Discrete; no analytic completion",
                "Unique extension of monoid homomorphisms to abelian groups", "[(a,b)] maps to a-b",
                ["Target is an abelian group"], [(spec,"PAPER_PROOF"),
                ("observational_succ/edge_carrier_reconstruction.py","SOURCE_CODE")],
                "Integer difference and unique extension", "N itself is not a group; -1 outside unit image",
                "Read PT-G01 proof; python -m unittest discover -s tests -p 'test_edge_carrier_reconstruction.py'"),
        capsule("PH-01", "Normalized quotient pullback is isometric, its adjoint averages fibers, AU=I and E=UA is orthogonal; normalized Fourier refines without a fiber-size factor",
                "Uniform probability cyclic carriers Z/n with n dividing m", "Finite Hilbert spaces and character coordinates",
                "Pullback, normalized average, adjoint, Fourier transform", "All residues of each declared finite carrier",
                "Normalized Haar 1/n on carrier; counting measure on frequencies",
                "Isometric compatible inclusion and split orthogonal projection",
                "q(x)=x mod n; dual injection a->(m/n)a; canonical cyclotomic embedding",
                ["Positive integer moduli", "Common source/epoch", "One declared Fourier sign"],
                [(haar,"PAPER_PROOF"),("observational_succ/profinite_hilbert.py","SOURCE_CODE"),
                 ("tests/test_profinite_hilbert.py","NEGATIVE_CONTROLS")],
                "Exact finite cyclotomic operations", "Wrong average, phase or root embedding fails; nontrivial E is not an invertible route",
                "python -m unittest discover -s tests -p 'test_profinite_hilbert.py'; python scripts/profinite_hilbert_probe.py"),
        capsule("PH-GLOBAL", "Hilbert completion of the cyclic Haar direct limit is L2(Zhat), unitarily ell2(Q/Z); factorial projections converge strongly and ||I-Pk||=1",
                "Profinite integers with compatible residue quotients", "Complete L2(Zhat) and ell2(Q/Z)",
                "Isometric direct limit, Haar integration, Fourier completion", "Cylinder residues; each character has finite conductor",
                "Compact profinite topology and regular probability Haar; Hilbert norm completion",
                "Unique bounded extension of uniformly bounded compatible linear maps into a Hilbert space",
                "Jn f=f composed with residue projection; Fourier labels a/n mod 1",
                ["Classical regular Haar existence", "Density of continuous functions in L2 for regular finite measure",
                 "Hilbert completion theorem"], [(haar,"PAPER_PROOF"),
                 ("observational_succ/profinite_hilbert.py","SOURCE_CODE")],
                "Finite cylinder algorithms and an analytic completion theorem", "Character 1/(2 k!) is invisible at level k!; a fixed prime tower is not cofinal",
                "Read PH density/universal-property proof; python scripts/profinite_hilbert_probe.py", dependencies=("PH-01",)),
        capsule("PT-C02", "For every n>=1, chi4:Z->Z factors through residue modulo n iff 4 divides n",
                "Authentic periodic chi4 integer character", "Reachable residue decoder or collision pair",
                "Integer residue and primitive character table", "x mod n", "Discrete integer/residue topology",
                "Least sufficient modulus in divisibility order is 4", "Decoder r->chi4(r mod 4)",
                ["n is a positive integer", "Target is zero-extended integer chi4, not chi2 on Q2*"],
                [(obs,"PAPER_PROOF"),("observational_succ/tate_chi4.py","SOURCE_CODE"),
                 ("observational_succ/minimal_observation.py","SOURCE_CODE")],
                "For odd n use (0,n); for n=2 mod4 use (1,n+1)", "chi4(2)=0 but the local Hecke chi2(2)=1",
                "python scripts/minimal_observation_probe.py; python -m unittest discover -s tests -p 'test_minimal_observation.py'"),
        capsule("PT-ADELE-NONSPLIT", "A_f/Zhat is Q/Z but its quotient has no additive group section",
                "Finite rational adeles", "Q/Z quotient and additive-section obstruction", "Quotient and principal parts",
                "Finite support of presented nonintegral local principal parts", "Restricted product; discrete quotient",
                "Additive quotient universal property; no split extension", "Principal parts; rational diagonal representatives",
                ["Each Qp has characteristic zero", "Q/Z is nonzero torsion"],
                [(glue,"PAPER_PROOF"),("observational_succ/tate_adele_quotient_descent.py","SOURCE_CODE")],
                "Finite quotient computation exists; additive representative selection does not",
                "Any torsion-to-torsion-free homomorphism is zero; carry breaks a set-theoretic lift",
                "Read nonsplitting proof; python -m unittest discover -s tests -p 'test_proof_gluing.py'"),
        capsule("PT-ALL-COMPRESSIONS", "Every compression of one specified bounded self-adjoint A along the entire dense chain is positive",
                "An arbitrary specified bounded self-adjoint Hilbert operator A", "Universal positivity premise",
                "Orthogonal compression", "All stages, not a finite prefix", "Hilbert norm topology",
                "Premise to be supplied independently", "Pn A Pn on one common source",
                ["One source operator", "All n quantified"], [(glue,"OPEN_PREMISE_DOSSIER")],
                "No universal witness supplied by finite matrix testing", "A negative direction can lie beyond every tested prefix",
                "Inspect the actual all-stage proof if supplied; finite replay cannot discharge this node",
                authority="UNVERIFIED", mode="OPEN_TARGET"),
        capsule("PT-DENSE-POSITIVITY", "For bounded self-adjoint A and Pn->I strongly, positivity of EVERY Pn A Pn implies A>=0",
                "One bounded self-adjoint operator on one Hilbert space", "Global quadratic-form nonnegativity",
                "Compatible orthogonal compression and norm continuity", "Complete increasing dense projector chain",
                "Hilbert norm; bounded operator norm", "Continuous extension from a dense subspace",
                "<Pn x,A Pn x> tends to <x,A x>",
                ["A is bounded and self-adjoint", "Pn converge strongly to I", "ASSUME:PT-ALL-COMPRESSIONS"],
                [(glue,"PAPER_PROOF"),("observational_succ/proof_gluing.py","SOURCE_CODE")],
                "A conditional mathematical proof; no source-specific A positivity inferred",
                "Missing density, unbounded/discontinuous form, different source operators or a finite prefix invalidate inference",
                "Read dense-positivity proof; python -m unittest discover -s tests -p 'test_proof_gluing.py'",
                dependencies=("PT-ALL-COMPRESSIONS",)),
        capsule("PT-SCHUR-OPEN", "At a=1/2, the genuine completed Suzuki four-low Schur form S0=Ainf-R0 is nonnegative",
                "Pinned completed zeta Suzuki source blob 0cc8510b71d178fc79e8d410a86d8b6014cf9178",
                "Original unmodified low Schur sign", "Signed block decomposition, reflection, Douglas range and zero-shift limit",
                "True prime2, real Gamma, both poles, contact and full high response",
                "Mean-zero L2(-1/2,1/2), K=V*V, H1 range controls",
                "Variational shorting, not a bounded inverse of compact D at zero",
                "Source mixed derivative identity and actual low/high Legendre projection",
                ["Source authentication and all analytic domains", "High coercivity does not settle the low sign"],
                [(schur,"OPEN_PROBLEM_AND_BOUND"),(D+"TATE_WEIGHTED_BESSEL_FOUR_SCHUR.md","INHERITED_PROOF"),
                 ("observational_succ/four_low_schur_proof_teeth.py","SOURCE_CODE")],
                "Finite trial responses and rigorous partial bounds; sign certificate absent",
                "Positive A need not give positive A-R0; wrong Gamma/poles and fake composite are refused; auxiliary positive corrections change the form",
                "Read signed-Schur dossier; python scripts/four_low_schur_proof_teeth_probe.py; RH PROVED: NO",
                authority="UNVERIFIED", mode="OPEN_TARGET"),
        capsule("PT-C05", "The arithmetic functional on all autocorrelations in (-a,a) has coarsest sufficient tape restriction to log(q)<2a",
                "Independently mutable real paired coefficients at genuine prime powers", "Arithmetic Weil functional on smooth autocorrelations",
                "Support restriction and smooth two-bump autocorrelation", "Coefficients at prime powers q with log(q)<2a",
                "Cc-infinity tests, ordinary convolution, fixed Gamma/contact/poles",
                "Two tapes give the same full target functional iff their active coordinates agree",
                "f=eta(t+log(q)/2)+eta(t-log(q)/2) isolates the q coordinate",
                ["a>0", "Independent tape mutations are allowed", "Mutants are not asserted to be genuine zeta sources"],
                [(obs,"PAPER_PROOF"),("observational_succ/minimal_weil_window.py","SOURCE_CODE")],
                "Exact rational separation and smooth sensitivity witness for admitted finite budgets",
                "Endpoints and outside atoms invisible; fake composite6 excluded; uncertain log comparisons remain unresolved",
                "python scripts/minimal_observation_probe.py; inspect PT-C05 support proof"),
    ]


if __name__ == "__main__":
    target = ROOT / D / "PROOF_TEETH_CAPSULES.json"
    target.write_text(json.dumps(build(), indent=2, sort_keys=True)+"\n")
    print(target)
