#!/usr/bin/env python3
"""Build Round-II records; only the existing structural auditor is invoked."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.source_proof_certificate import audit_capsules, evidence_file


def capsule(cid, statement, path, hypotheses=(), deps=(), authority="PAPER_PROVED"):
    opened = authority == "UNVERIFIED"
    return dict(
        claim_id=cid, statement=statement, source="Explicit mathematical source in the linked theorem dossier",
        operations_relations="Bounded linear observation and source-preserving form operations, as typed in the theorem",
        target_carrier="The stated image, Hilbert low carrier or scalar quadratic report",
        observation_morphisms="Actual O or orthogonal P specified in the exact theorem",
        topology_measure="Declared Hilbert/subspace norms; Euclidean rational metric for finite instances",
        universal_property="Factorization/envelope property only with the stated assumptions",
        comparison_maps="Source-specific maps in the proof; no arbitrary isomorphism supplies arithmetic identification",
        source_identity="SUCC Observer Schur Round II mathematical dossier", source_epoch=0,
        hypotheses=list(hypotheses), dependencies=list(deps), authority=authority,
        scope="UNIVERSAL", conclusion_mode="OPEN_TARGET" if opened else "THEOREM_UNDER_HYPOTHESES",
        evidence=[evidence_file(ROOT, path, "OPEN_DOSSIER" if opened else "PAPER_DERIVATION")],
        access=dict(permitted_observations="Declared source maps only",
                    constructible_witness="Exact finite witnesses where supplied; no general effective infinite minimizer",
                    oracle="No nontrivial zeta-zero oracle; no implicit access to unobserved coordinates",
                    probe_discrimination="Explicit exact counterexamples and retained source/range gates",
                    proof_theory="Classical paper proof; separate Lean terms and finite executions",
                    execution_cost="Explicit finite budgets; no uniform infinite decision procedure inferred"),
        adversarial=dict(domain_tests="Singular blocks, actual versus closure range, source and metric binding",
                         negative_examples="Cross-term, compact inverse, nonattainment and relative residual failures",
                         source_mutations="Changed source labels/hashes do not certify source semantics",
                         replay="Read the linked proof; replay the named exact probe and formal receipt separately"))


def main():
    base = "research/2026-10-16/"
    obs, compact, source, discovery = [base+x for x in (
        "OBSERVER_SCHUR_THEOREMS.md", "COMPACT_SOURCE_GALERKIN.md",
        "OBSERVER_SCHUR_SOURCE.md", "OBSERVER_DISCOVERY_EXPERIMENT.md")]
    records = [
        capsule("OS-ENERGY", "Quadratic energy factors through linear O iff ker O lies in its Hermitian radical",
                obs, ("Real or complex vector space, linear O, Hermitian form",)),
        capsule("OS-ENVELOPE", "The reduced Schur form equals the finite fiber infimum; attainment needs actual D range",
                obs, ("Bounded self-adjoint G, D>=0", "Ran(B*) subset actual Ran(sqrt(D))")),
        capsule("OS-CONTRACTION", "S0>=0 iff norm(C A^-1/2)<=1, with two sectors under source parity",
                obs, ("A>=alpha I for alpha>0", "The same G and P commute with the reflection"), ("OS-ENVELOPE",)),
        capsule("OS-COMPACT", "Compact source compression converges in operator norm; the Suzuki Legendre bound is source-relative",
                compact, ("Compact operator and strongly convergent orthogonal projections",
                          "Quantitative Suzuki specialization uses the pinned signed derivative enclosure")),
        capsule("OS-RANGE-OPEN", "Actual Suzuki target residual columns belong to closure of the high response range in the relative norm",
                compact, authority="UNVERIFIED"),
        capsule("OS-RELATIVE-APPROX", "Dense high trial spaces approximate the target in relative residual norm if the range-closure premise holds",
                compact, ("ASSUME:OS-RANGE-OPEN", "Source residual operator is bounded and trials have dense union"), ("OS-RANGE-OPEN",)),
        capsule("OS-APPROX-CONSUMER", "The same conditional approximation theorem preserves range debt when used downstream",
                compact, ("ASSUME:OS-RANGE-OPEN",), ("OS-RELATIVE-APPROX",)),
        capsule("OS-ANSATZ-FAILURE", "Every declared degree-eight even response fails the specified sufficient certificate",
                source, ("Pinned original source, radius1/2, trial U(P2) in span(P6,P8)",
                         "The exact tested kappa range and whole-source interval proof in the dossier")),
        capsule("OS-NESTED-ENVELOPE", "Compatible finite Schur envelopes associate with all PSD and range obligations retained",
                discovery, ("Same finite source, nested observations, both staged PSD and cross-range conditions",)),
        capsule("OS-SCHUR-OPEN", "The original unmodified four-low signed short S0 is nonnegative at radius1/2",
                source, authority="UNVERIFIED"),
    ]
    audit = audit_capsules(records, ROOT)
    path = ROOT / base / "OBSERVER_SCHUR_CAPSULES.json"
    path.write_text(json.dumps(records, indent=2)+"\n")
    (ROOT / base / "observer_schur_receipts/capsule-audit.json").write_text(json.dumps(audit, indent=2)+"\n")
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
