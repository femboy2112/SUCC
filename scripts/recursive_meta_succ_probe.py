#!/usr/bin/env python3
"""Zero-network deterministic exact proof receipt for recursive Meta-SUCC.

Run from repository root:
  PYTHONPATH=. python scripts/recursive_meta_succ_probe.py --verify \
     research/2026-10-14/RECURSIVE_META_SUCC_RECEIPT.json
"""
import argparse
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

from observational_succ.recursive_meta_succ import (
    ModelSystem, OrthogonalEdge, OrthogonalMetaGraph, SignedCycle, SignedEdge,
    SignedGraph, SourceWorld, even_parity_world, reconstruction_arity,
    repair_ghost, shadow_system, shift_approximate_invariance,
)


def fraction_repr(x):
    y = F(x)
    return str(y.numerator) if y.denominator == 1 else "%d/%d" % (y.numerator,y.denominator)


def build_receipt():
    world=SourceWorld("model-interactions",0,"fixed-bits",("A","B","C","D"),
                      (("0","1"),)*4,(("0","0","0","1"),("1","1","1","0")))
    m=ModelSystem(world.source_id,0,world.basis,world.coordinates,world.domains,
                  (world.source_law("AB",("A","B")),
                   world.source_law("BC",("B","C")),
                   world.source_law("CD",("C","D"))),world)
    ac=m.strongest_consequence(("A","C"),("AB","BC"),"AC")
    assert m.check_derivation(ac)
    m1=m.with_derived(ac)
    ad=m1.strongest_consequence(("A","D"),("AC","CD"),"AD")
    assert m1.check_derivation(ad)
    m2=m1.with_derived(ad)
    assert m2.joint_candidates() == m.joint_candidates()

    p=even_parity_world(5)
    q=even_parity_world(5,1)
    shadow=shadow_system(p,2)
    assert reconstruction_arity(p)==5 and len(shadow.joint_candidates())==32
    assert all(shadow_system(p,k).joint_candidates()==shadow_system(q,k).joint_candidates()
               for k in range(1,5))
    ghosts=shadow.ghosts()
    repaired,repair=repair_ghost(shadow,ghosts[0],"full-parity-source-law")
    assert len(repaired.joint_candidates())==16

    g=SignedGraph("signed-original",0,"real-orientation",("A","B","C"),
                  (SignedEdge("ab","A","B",1,F(1),"signed-original",0,"real-orientation"),
                   SignedEdge("bc","B","C",1,F(1),"signed-original",0,"real-orientation"),
                   SignedEdge("ca","C","A",-1,F(1),"signed-original",0,"real-orientation")))
    c=SignedCycle("A",(("ab",True),("bc",True),("ca",True)))
    eq={"A":F(1),"B":F(1,3),"C":F(-1,3)}
    assert g.energy(eq)==F(4,3)==g.holonomy_root_lower_bound(c)
    bound=g.explicit_coercivity_constant(c)
    assert bound==F(2,17)
    assert min(g.boolean_frustration(dict(zip(g.vertices,v))) for v in product((-1,1),repeat=3))==F(1)

    I=((F(1),F(0)),(F(0),F(1)))
    H1=((F(1),F(0)),(F(0),F(-1)))
    H2=((F(-1),F(0)),(F(0),F(1)))
    def edge(n,u,v,U):
        return OrthogonalEdge(n,u,v,U,F(1),"joint-original",0,"two-dimensional-orthogonal")
    G=OrthogonalMetaGraph("joint-original",0,"two-dimensional-orthogonal",("R","A","B","C","D"),
                          (edge("ra","R","A",I),edge("ab","A","B",I),edge("br","B","R",H1),
                           edge("rc","R","C",I),edge("cd","C","D",I),edge("dr","D","R",H2)))
    c1=SignedCycle("R",(("ra",True),("ab",True),("br",True)))
    c2=SignedCycle("R",(("rc",True),("cd",True),("dr",True)))
    certificate=G.certify_joint_gap((c1,c2),(F(1),F(1)),F(4))
    assert certificate.full_state_coercivity==F(1,23)
    assert certificate.joint_gram==((F(4),F(0)),(F(0),F(4)))
    first_only_gap_rejected=False
    try:
        G.certify_joint_gap((c1,),(F(1),),F(1))
    except ValueError:
        first_only_gap_rejected=True
    assert first_only_gap_rejected
    return {
        "schema":"succ-recursive-meta-1",
        "date":"2026-10-14",
        "parent_repo":"femboy2112/SUCC",
        "parent_exact_commit":"8ce8ebbc4ea26d6a0f53f1f243a8b9a7932461c0",
        "provenance":"declared mathematical source laws, not physical observations",
        "joint_model_derivations":{
            "original_declared_source_states":len(world.states),
            "base_joint_candidates":len(m.joint_candidates()),
            "AB_BC_implies_AC":[list(t) for t in ac.relation.rows],
            "AC_CD_implies_AD":[list(t) for t in ad.relation.rows],
            "second_recursion_is_conservative":m2.joint_candidates()==m.joint_candidates(),
            "complete_join_witnesses":len(ac.witnesses)+len(ad.witnesses),
            "physically_executed":False,
        },
        "arity_barrier":{
            "parity_bit_count":5,
            "even_source_size":len(p.states),
            "arity_2_candidates":len(shadow.joint_candidates()),
            "arity_2_ghosts":len(ghosts),
            "reconstruction_arity":reconstruction_arity(p),
            "even_odd_indistinguishable_at_all_proper_arities":True,
            "minimum_new_ghost_separating_scope":list(repair.separating_scope),
            "source_repair_candidate_count":len(repaired.joint_candidates()),
        },
        "signed_cycle":{
            "holonomy":g.oriented_cycle(c)[0],
            "resistance":fraction_repr(g.oriented_cycle(c)[1]),
            "sharp_root_energy_minimum":fraction_repr(g.holonomy_root_lower_bound(c)),
            "sharp_attained_energy":fraction_repr(g.energy(eq)),
            "boolean_frustration_minimum":"1",
            "full_3node_coercivity_lower_bound":fraction_repr(bound),
        },
        "joint_orthogonal_meta_meta":{
            "individual_loop_1_holonomy":[[fraction_repr(x) for x in row] for row in H1],
            "individual_loop_2_holonomy":[[fraction_repr(x) for x in row] for row in H2],
            "first_loop_strict_gap_rejected":first_only_gap_rejected,
            "joint_cycle_Gram":[[fraction_repr(x) for x in row] for row in certificate.joint_gram],
            "joint_gap":fraction_repr(certificate.claimed_gap),
            "combined_resistance":fraction_repr(certificate.resistance_total),
            "global_coercivity_constant":fraction_repr(certificate.full_state_coercivity),
            "requires_original_source_operator_identification_for_Weil":True,
        },
        "infinite_dimensional_gap_control":{
            "bilateral_shift_almost_fixed_norm_sq_N_1000":fraction_repr(shift_approximate_invariance(1000)),
            "zero_kernel_implies_uniform_coercivity":False,
        },
        "RH_PROVED":False,
        "new_number_theory_theorem_claimed":False,
        "academic_priority_claimed":False,
        "Lean_kernel_check_claimed":False,
        "external_physical_source_authenticated":False,
        "original_nontrivial_zeta_zero_positions_used":False,
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",help="path to frozen deterministic receipt")
    args=parser.parse_args()
    payload=json.dumps(build_receipt(),sort_keys=True,indent=2,ensure_ascii=False)+"\n"
    if args.verify:
        existing=Path(args.verify).read_text(encoding="utf-8")
        if existing != payload:
            raise SystemExit("RECURSIVE_META_SUCC_RECEIPT_MISMATCH")
        print("RECURSIVE_META_SUCC_SOURCE_RECEIPT_VERIFIED")
    else:
        print(payload,end="")


if __name__=="__main__":
    main()
