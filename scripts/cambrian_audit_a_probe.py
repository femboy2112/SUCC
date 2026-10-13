#!/usr/bin/env python3
"""Independent hostile probes for Cambrian C, B, and stochastic transport.

No E arithmetic proof is audited by this script. Infinite theorems retain
their paper or Lean authority; exact finite controls are not universal proofs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import permutations, product
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.cambrian_stochastic_transport import (
    JointInstrument, joint_descent, source_filter, observer_filter, push_reports,
)
from observational_succ.causal_nerode_succ import SourceChart
from observational_succ.voltage_cover_synthesis import PermutationGraph


def load_module(root: Path, filename: str, name: str):
    path = root / "observational_succ" / filename
    spec = importlib.util.spec_from_file_location("observational_succ." + name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, path


def powerset(items):
    return tuple(frozenset(x for x, bit in zip(items, bits) if bit)
                 for bits in product((0, 1), repeat=len(items)))


def c_histories(C):
    spaces = (("old0", "old1"), ("new0", "new1"), ("end",))
    relation_options = [powerset(tuple(product(spaces[t], spaces[t+1]))) for t in (0, 1)]
    receipts_options = [powerset(space) for space in spaces]
    count = 0
    for relations in product(*relation_options):
        for receipts in product(*receipts_options):
            source = C.FiniteHistorySystem(spaces, relations, receipts, "audit-changing-type")
            raw = tuple(path for path in product(*spaces)
                        if all(path[t] in receipts[t] for t in range(3))
                        and all((path[t], path[t+1]) in relations[t] for t in range(2)))
            assert set(source.prefix_paths(2)) == set(raw)
            for d in range(3):
                prefix = tuple(path for path in product(*spaces[:d+1])
                               if all(path[t] in receipts[t] for t in range(d+1))
                               and all((path[t], path[t+1]) in relations[t] for t in range(d)))
                assert source.support_history()[d] == frozenset(p[-1] for p in prefix)
            count += 1
    # Each edge has receipt-compatible witnesses, but no common middle one.
    relation = (frozenset({("old0", "new0")}), frozenset({("new1", "end")}))
    system = C.FiniteHistorySystem(spaces, relation, tuple(frozenset(s) for s in spaces), "audit-no-glue")
    assert all(relation) and not system.prefix_paths(2)
    # All-depth existence is not survival of EVERY initial member.
    live_dead = C.FiniteHistorySystem((("dead", "live"),) * 4,
                    (frozenset({("live", "live")}),) * 3,
                    (frozenset({"dead", "live"}),) * 4, "audit-initial-quantifier")
    assert live_dead.prefix_paths(3) == (("live", "live", "live", "live"),)
    # Compact X=[0,1] and identity graph, but NONCLOSED receipts C_t=(0,1/(t+1)].
    # Every prefix has an exact rational constant witness. The intersection
    # of every C_t is empty by the Archimedean property, proved in the dossier.
    compact_receipt_checks = 0
    for N in range(1, 65):
        witness = Q(1, N+1)
        assert all(0 < witness <= Q(1, t+1) for t in range(N+1))
        compact_receipt_checks += 1
    return {"exhaustive_changing_type_systems": count,
            "independent_cartesian_paths_agree": True,
            "nonempty_pairwise_relations_without_joint_history": [sorted(r) for r in relation],
            "null_relations_and_empty_receipts_included": True,
            "every_initial_state_survives_mutant_refuted": True,
            "compact_but_nonclosed_receipt_prefix_checks": compact_receipt_checks}


def c_covers(C):
    perms = tuple(permutations(range(3)))
    count = 0
    for p, q in product(perms, repeat=2):
        graph = PermutationGraph(("r",), (("r", "r", p), ("r", "r", q)), 3)
        for x in range(3):
            seen, todo = {x}, [x]
            for y in todo:
                for z in (p[y], q[y], p.index(y), q.index(y)):
                    if z not in seen:
                        seen.add(z)
                        todo.append(z)
            centralizers = tuple(d for d in perms if all(d[g[y]] == g[d[y]]
                                                        for g in (p, q) for y in seen)
                                 and {d[y] for y in seen} == seen)
            # On a proper orbit multiple full-X permutations may restrict
            # to the same actual deck transformation; quotient those duplicates.
            decks = {tuple(d[y] for y in sorted(seen)) for d in centralizers}
            report = C.orbit_section_cover(graph, x)
            assert report["minimum_degree_for_this_section"] == len(seen)
            assert report["orbit_cover_deck_group_order"] == len(decks)
            count += 1
    graph = PermutationGraph(("r",), (("r", "r", (1, 0, 2)), ("r", "r", (0, 2, 1))), 3)
    result = C.orbit_section_cover(graph, 0)
    assert result["orbit_cover_deck_group_order"] == 1
    assert result["constructed_section_deck_invariant"]
    assert not result["constructed_section_descends_to_base"]
    return {"two_generator_three_label_cases": count,
            "independent_orbit_and_centralizer_agree": True,
            "nonregular_counterexample": result}


def b_targets(B):
    # Independent finite polynomial transfer via direct Chebyshev recurrence
    # at exact rational x and logistic f(x).  Pair inverse roots below use
    # rational preimages x,1-x, not square-root numerical evaluation.
    def T(k, z):
        if k == 0:
            return Q(1)
        old, new = Q(1), z
        for _ in range(1, k):
            old, new = new, 2*z*new-old
        return new
    mode_checks = 0
    for x in (Q(1, 7), Q(2, 9), Q(3, 8), Q(1, 2), Q(5, 6)):
        y = 4*x*(1-x)
        for k in range(17):
            direct = (T(k, 1-2*x)+T(k, 2*x-1))/2
            expected = T(k//2, 1-2*y) if k % 2 == 0 else Q(0)
            assert direct == expected
            assert T(k, 1-2*y) == T(2*k, 1-2*x)
            mode_checks += 1
    # Truncating the infinite eigenfunction is NOT itself an eigenfunction:
    # its omitted tail must be paid.  Exact coefficient accounting checks it.
    truncation_checks = 0
    for lam in (Q(1, 3), Q(2, 3), Q(7, 8)):
        for J in range(1, 13):
            values = {2**j: lam**j for j in range(J)}
            transferred = B.transfer(values, 1)
            residual = {k: transferred.get(k, 0)-lam*v for k, v in values.items()}
            assert {k: v for k,v in residual.items() if v} == {2**(J-1): -lam**J}
            assert sum(values.values(), Q(0)) + lam**J/(1-lam) == 1/(1-lam)
            truncation_checks += 1
    # Fresh alternating bounded-surplus subsequence: clocks both diverge,
    # yet one geometric target retains a positive fixed residual subsequence.
    lam = Q(2, 3)
    alternating = [(10*t + (t if t % 2 else 0), 10*t) for t in range(1, 13)]
    residuals = [lam**max(n-m, 0)/(1-lam) for n,m in alternating]
    assert all(residuals[i] == 3 for i in range(1, 12, 2))
    # Universal iff must not be applied to each polynomial/constant separately.
    assert B.advancing({1: Q(1)}, 10, 9) == {}
    assert B.advancing({0: Q(5)}, 9, 10) == {0: Q(5)}
    # For any fixed depth d there is a normalized mean-zero polynomial target
    # preserving sup norm: L^d psi_(2^d)=psi_1. No unit-ball uniform decay.
    for d in (0, 1, 5, 40, 91):
        assert B.transfer({2**d: Q(1)}, d) == {1: Q(1)}
    return {"exact_rational_Chebyshev_inverse_checks": mode_checks,
            "lacunary_truncation_tail_checks": truncation_checks,
            "alternating_clocks": alternating, "geometric_residuals": residuals,
            "bounded_surplus_individual_polynomial_completes": True,
            "constant_target_needs_mean_subtraction": True,
            "operator_unit_ball_uniform_decay_refuted": True,
            "universal_fixed_continuous_target_iff_not_refuted": True}


def chart(epoch, reports):
    return SourceChart("audit-st-source", epoch, "audit-basis",
                       tuple("s"+str(i) for i in range(len(reports))), tuple(reports))


def rational_laws(size, denominator):
    return tuple(tuple(Q(a, denominator) for a in xs)
                 for xs in product(range(denominator+1), repeat=size) if sum(xs) == denominator)


def stochastic_all_prior():
    rows = rational_laws(4, 3)
    count = 0
    # Weak prior-specific uniform average always descends to one row, but
    # all-prior descent detects exactly equal rows within the hidden fiber.
    for p, q in product(rows, repeat=2):
        inst = JointInstrument("audit-all-prior", chart(0, ("o", "o")),
                               chart(1, ("x", "y")), ("a", "b"), (p, q))
        cert = joint_descent(inst)
        delta_results = tuple(source_filter(inst, prior, receipt)
                              for prior in ((Q(1), Q(0)), (Q(0), Q(1)))
                              for receipt in ("a", "b"))
        # Joint law can be reconstructed from conditional law AND evidence;
        # impossible events contribute a zero slice.
        rebuilt = []
        for i in range(2):
            reconstructed = [Q(0)]*4
            for z in range(2):
                event = delta_results[2*i+z]
                if event.posterior:
                    for j,v in enumerate(event.posterior):
                        reconstructed[2*j+z] = event.evidence*v
            rebuilt.append(tuple(reconstructed))
        assert tuple(rebuilt) == (p, q)
        assert cert.descended == (p == q)
        count += 1
    # Hidden-state-dependent action chooses different individually lawful
    # kernels. Their union is not one coarse-history-measurable instrument.
    p = (Q(1), Q(0), Q(0), Q(0))
    q = (Q(0), Q(0), Q(1), Q(0))
    A = JointInstrument("audit-action-A", chart(0,("o","o")),chart(1,("x","y")),("a","b"),(p,p))
    B = JointInstrument("audit-action-B", A.before,A.after,A.receipts,(q,q))
    hidden_selection = JointInstrument("audit-hidden-selector", A.before,A.after,A.receipts,(p,q))
    assert joint_descent(A).descended and joint_descent(B).descended
    assert not joint_descent(hidden_selection).descended
    return {"denominator_three_row_pairs": count,
            "all_delta_priors_joint_law_converse_agrees": True,
            "prior_specific_averaging_not_sufficient": True,
            "hidden_selector_breaks_descent_of_individually_lawful_actions": True}


def adaptive_stochastic():
    # Genuine observable-history-measurable policy. Both source hidden rows
    # lump correctly, while the next selected action depends on prior receipt.
    prior = (Q(1,3), Q(1,6), Q(1,2))
    reports = ("a", "a", "b")
    kernels = (
        ((Q(1,8),Q(1,8),Q(1,8),Q(1,8),Q(1,4),Q(1,4)),
         (Q(1,4),Q(0),Q(0),Q(1,4),Q(1,4),Q(1,4)),
         (Q(1,8),Q(1,8),Q(1,8),Q(1,8),Q(1,2),Q(0))),
        ((Q(1,3),Q(0),Q(0),Q(1,3),Q(0),Q(1,3)),
         (Q(0),Q(1,3),Q(1,3),Q(0),Q(0),Q(1,3)),
         (Q(1,6),Q(1,6),Q(1,6),Q(1,6),Q(1,6),Q(1,6))),
    )
    paths = []
    for history in product(("z", "w"), repeat=5):
        raw = list(prior)
        coarse = push_reports(chart(0,reports), prior)
        likelihood = Q(1)
        action_trace = []
        for t,z in enumerate(history):
            action = 0 if t == 0 else (history[t-1] == "w")
            action_trace.append(int(action))
            inst = JointInstrument("audit-action-"+str(action),chart(t,reports),chart(t+1,reports),
                                   ("z","w"),kernels[action])
            assert joint_descent(inst).descended
            coarse_result = observer_filter(inst,coarse,z)
            likelihood *= coarse_result.evidence
            zi = ("z","w").index(z)
            raw = [sum((raw[i]*kernels[action][i][2*j+zi] for i in range(3)),Q(0))
                   for j in range(3)]
            mass = sum(raw,Q(0))
            assert mass == likelihood
            if not mass:
                assert coarse_result.posterior is None
                break
            coarse = coarse_result.posterior
            direct = tuple(sum((raw[i] for i,r in enumerate(reports) if r==report),Q(0))/mass
                           for report in ("a","b"))
            assert coarse == direct
        paths.append({"history":history,"actions":action_trace,"likelihood":likelihood})
    return {"observable_history_adaptive_paths": len(paths), "raw_unnormalized_path_oracle_agrees": True,
            "path_results":paths, "hidden_source_selector_excluded":True}


def conditional_tv():
    rows = rational_laws(4, 6)
    count, unequal, saturations = 0, 0, 0
    for p,q in product(rows,repeat=2):
        epsilon = sum((abs(a-b) for a,b in zip(p,q)),Q(0))/2
        # Cell order (x,event),(y,event),(x,complement),(y,complement).
        alpha,beta = sum(p[:2],Q(0)),sum(q[:2],Q(0))
        if not alpha or not beta:
            continue
        distance = sum((abs(p[i]/alpha-q[i]/beta) for i in range(2)),Q(0))/2
        stronger = min(Q(1),epsilon/max(alpha,beta))
        assert distance <= stronger <= epsilon/min(alpha,beta)
        count += 1
        unequal += alpha != beta
        saturations += alpha != beta and distance == stronger and distance > 0
    # Unequal event masses achieve the sharper bound exactly, with <1 error.
    p = (Q(1,3),Q(0),Q(2,3),Q(0))
    q = (Q(1,3),Q(1,3),Q(1,3),Q(0))
    eps = sum(abs(a-b) for a,b in zip(p,q))/2
    alpha,beta = Q(1,3),Q(2,3)
    distance = Q(1,2)
    assert eps==Q(1,3) and distance == eps/max(alpha,beta)
    return {"positive_event_pair_checks":count,"unequal_mass_checks":unequal,
            "unequal_mass_saturations_of_improved_bound":saturations,
            "improved_bound":"min(1, epsilon/max(alpha,beta))",
            "sharp_example":{"p":p,"q":q,"epsilon":eps,"alpha":alpha,"beta":beta,
                             "conditional_TV":distance,"old_bound":eps/min(alpha,beta),
                             "new_bound":eps/max(alpha,beta)},
            "original_ST7_bound_valid":True}


def encode(value):
    if isinstance(value,Q):
        return str(value)
    if isinstance(value,dict):
        return {str(k):encode(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):
        return [encode(v) for v in value]
    return value


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--geometry",type=Path)
    parser.add_argument("--chaos",type=Path)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    croot=args.geometry or (ROOT if (ROOT/"observational_succ/cambrian_c_geometry.py").exists() else ROOT.parent/"c_geometry")
    broot=args.chaos or (ROOT if (ROOT/"observational_succ/cambrian_b_chaos.py").exists() else ROOT.parent/"b_chaos")
    C,cpath=load_module(croot,"cambrian_c_geometry.py","_audit_c")
    B,bpath=load_module(broot,"cambrian_b_chaos.py","_audit_b")
    paths=(cpath,bpath,ROOT/"observational_succ/cambrian_stochastic_transport.py",Path(__file__).resolve())
    hashes={str(p):sha256(p.read_bytes()).hexdigest() for p in paths}
    result={"schema":"succ-cambrian-audit-a-v1","executor":"/root/arithmetic; separate hostile pass",
            "E_research_not_self_audited":True,"python":platform.python_version(),
            "source_sha256":hashes,"C_history":c_histories(C),"C_cover":c_covers(C),
            "B_targets":b_targets(B),"ST1_all_prior":stochastic_all_prior(),
            "ST3_adaptive":adaptive_stochastic(),"ST7_conditional_TV":conditional_tv()}
    assert hashes == {str(p):sha256(p.read_bytes()).hexdigest() for p in paths}, "Sources changed during audit"
    result["source_hashes_unchanged_during_probe"]=True
    text=json.dumps(encode(result),indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end="")


if __name__=="__main__":
    main()
