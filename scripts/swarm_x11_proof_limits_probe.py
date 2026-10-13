"""Reproducible finite controls for X11; infinite theorems are paper proofs."""
from __future__ import annotations

import json
from dataclasses import replace
from itertools import combinations, permutations, product
from pathlib import Path
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.checkpoint_meta_tower import GroundRule, HornTheory
from observational_succ.swarm_completion import PartialEvidence
from observational_succ.swarm_x11_proof_limits import (
    Certificate, CertificationContext, CertificationError, LicensedRule, LicensedStage,
    all_binary_evidence, certify_finite_source, derive, finite_completions,
    finite_ideals, first_zero_parity_witnesses, observation_atom, restrictions,
    verify_certificate,
)


CONTEXT = CertificationContext("X11-declared-binary-source", "X11-fixed-positive-basis")
ADDRESSES = (2, 7, 19, 43)
RULES = (
    LicensedRule("r0", (observation_atom(2, 1), observation_atom(19, 0)), "alpha"),
    LicensedRule("r1", ("alpha", observation_atom(43, 1)), "goal"),
    LicensedRule("r2", (observation_atom(7, 0),), "goal"),
)


def oracle(stage: LicensedStage) -> bool:
    """Independent closed formula, with no proof-search call."""
    values = dict(stage.evidence.entries)
    return (("r0" in stage.licenses and "r1" in stage.licenses
             and values.get(2) == 1 and values.get(19) == 0 and values.get(43) == 1)
            or ("r2" in stage.licenses and values.get(7) == 0))


def run_probe() -> dict:
    evidence = all_binary_evidence(ADDRESSES)
    licenses = tuple(frozenset(name for name, included in zip(("r0", "r1", "r2"), bits) if included)
                     for bits in product((False, True), repeat=3))
    stages = tuple(LicensedStage(CONTEXT, p, available) for p in evidence for available in licenses)
    receipts = {}
    rule_orders = tuple(permutations(RULES))
    horn = HornTheory(CONTEXT.source_id, CONTEXT.basis_id, (), tuple(
        GroundRule(("license:" + rule.license_id,) + rule.premises, rule.conclusion) for rule in RULES))
    order_checks = 0
    for stage in stages:
        expected = oracle(stage)
        proof = derive(stage, RULES, "goal")
        assert (proof is not None) == expected
        receipts[stage] = proof
        premises = tuple(observation_atom(n, v) for n, v in stage.evidence.entries)
        premises += tuple("license:" + name for name in sorted(stage.licenses))
        assert ("goal" in horn.closure(premises)["closure"]) == expected
        for reordered in rule_orders:
            assert (derive(stage, reordered, "goal") is not None) == expected
            order_checks += 1

    comparable_pairs = 0
    certificate_transports = 0
    for older in stages:
        for newer in stages:
            if newer.extends(older):
                comparable_pairs += 1
                if receipts[older] is not None:
                    assert verify_certificate(receipts[older], newer, RULES)
                    assert receipts[newer] is not None
                    certificate_transports += 1
    assert comparable_pairs == 5 ** len(ADDRESSES) * 3 ** len(RULES)

    p = LicensedStage(CONTEXT, PartialEvidence(((2, 1), (43, 1))), frozenset(("r0",)))
    q = LicensedStage(CONTEXT, PartialEvidence(((19, 0),)), frozenset(("r1",)))
    joined = p.join(q)
    assert derive(p, RULES, "goal") is None and derive(q, RULES, "goal") is None
    proof = derive(joined, RULES, "goal")
    assert proof is not None
    assert not p.extends(q) and not q.extends(p)
    mutation_checks = 0
    for index in range(len(joined.evidence.entries)):
        remaining = PartialEvidence(joined.evidence.entries[:index] + joined.evidence.entries[index + 1:])
        assert not verify_certificate(proof, replace(joined, evidence=remaining), RULES)
        mutation_checks += 1
    for license_id in joined.licenses:
        assert not verify_certificate(proof, replace(joined, licenses=joined.licenses - {license_id}), RULES)
        mutation_checks += 1
    for changed in (CertificationContext("another-source", CONTEXT.basis_id),
                    CertificationContext(CONTEXT.source_id, "another-basis")):
        assert not verify_certificate(proof, replace(joined, context=changed), RULES)
        mutation_checks += 1
    forged = Certificate(joined, "goal", (("goal", "r1", (observation_atom(43, 1),)),))
    assert not verify_certificate(forged, joined, RULES)
    mutation_checks += 1

    small_evidence = all_binary_evidence((2, 7))
    sources = tuple(p for p in small_evidence if len(p.entries) == 2)
    classifier_checks = 0
    classifier_transports = 0
    for size in range(len(sources) + 1):
        for members in combinations(sources, size):
            positive = frozenset(members)
            reports = {p: certify_finite_source(p, sources, positive) for p in small_evidence}
            for p, value in reports.items():
                classifier_checks += 1
                extensions = finite_completions(p, sources)
                expected = {int(source in positive) for source in extensions}
                assert value == (next(iter(expected)) if len(expected) == 1 else None)
                for q in small_evidence:
                    if q.extends(p):
                        if value is not None:
                            assert reports[q] == value
                        classifier_transports += 1

    anti_sources = (PartialEvidence(((2, 0), (7, 1))), PartialEvidence(((2, 1), (7, 0))))
    admissible = tuple(p for p in small_evidence if finite_completions(p, anti_sources))
    ideals = finite_ideals(admissible)
    assert len(admissible) == len(ideals) == 7
    for ideal in ideals:
        union = PartialEvidence.from_mapping({n: v for p in ideal for n, v in p.entries})
        assert frozenset(restrictions(union)) == ideal
    consistent_unrealizable = PartialEvidence(((2, 0),)).join(PartialEvidence(((7, 0),)))
    assert not finite_completions(consistent_unrealizable, anti_sources)
    try:
        certify_finite_source(consistent_unrealizable, anti_sources, frozenset(anti_sources))
    except CertificationError:
        pass
    else:
        raise AssertionError("The empty fiber must not certify either answer")

    rng = random.Random(11013)
    scattered = [(), (2, 7, 19, 43), (0, 99), (4, 18, 87)]
    scattered.extend(tuple(sorted(rng.sample(range(101), rng.randrange(0, 18)))) for _ in range(150))
    for addresses in scattered:
        even, odd = first_zero_parity_witnesses(addresses)
        assert even % 2 == 0 and odd % 2 == 1
        assert all(n < even and n < odd for n in addresses)
        # Exact witnesses x_k(n)=int(n<k), both members of the declared source X.
        assert all(int(n < even) == int(n < odd) == 1 for n in addresses)

    # Finite syntax alone has the continuity property, even for an unsound rule.
    bad_rule = (LicensedRule("bad", (observation_atom(2, 1),), "false-in-all-declared-worlds"),)
    bad_stage = LicensedStage(CONTEXT, PartialEvidence(((2, 1),)), frozenset(("bad",)))
    assert derive(bad_stage, bad_rule, "false-in-all-declared-worlds") is not None

    return {
        "assignment": "SWM-X11",
        "parent_sha": "71eaf11e48ca3ccb349858bba64abf36b59ee6f5",
        "status": "CLASSICAL / PROVED LOCAL; EXACT FINITE CONTROLS",
        "finite_stage_count": len(stages),
        "successful_goal_stages": sum(value is not None for value in receipts.values()),
        "independent_oracle_checks": len(stages),
        "checkpoint_horn_embedding_checks": len(stages),
        "rule_order_checks": order_checks,
        "comparable_stage_pairs": comparable_pairs,
        "certificate_transports": certificate_transports,
        "mutation_rejections": mutation_checks,
        "partial_boolean_classifier_states": classifier_checks,
        "partial_boolean_comparable_pairs": classifier_transports,
        "source_admissible_basis_elements": len(admissible),
        "source_admissible_finite_ideals": len(ideals),
        "scattered_phantom_supports_with_opposite_answers": len(scattered),
        "non_directed_union_can_add_a_conclusion": True,
        "consistent_join_can_lose_source_admissibility": True,
        "syntactic_continuity_does_not_imply_soundness": True,
        "paper_only": ["arbitrary directed joins and ideal completion", "Scott-open converse",
                       "clopen versus partial-Boolean report theorem", "phantom-limit discontinuity",
                       "non-r.e. open-set counterexample"],
        "scope": "Declared finite semantics; no infinite computation, reflection axiom, or RH conclusion",
    }


if __name__ == "__main__":
    print(json.dumps(run_probe(), indent=2, sort_keys=True))
