"""Finite exact Möbius/BBP Gram witness with explicitly noncertifying diagnostics.

Run: python scripts/mobius_refined_matrix_probe.py --verify
This never downloads data, infers pi digits or claims normality.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from math import lcm

from observational_succ.succ_internal_matrix_walk import authentic_r
from observational_succ.mobius_refined_matrix import (
    authentic,from_forcing,build,coarsen,invert_atom,energies,variance,
    conditioned_innovation,pole_count,pole_crt_sieve,valuation,
)


def run():
    N=32
    t=authentic(N)
    conductor=1
    forces=[]
    for n in range(1,N+1):
        q=lcm(conductor,authentic_r(n).denominator)
        forces.append(Q(16,conductor)-Q(1,q))
        conductor=q
    fake=from_forcing(tuple(forces),"CONTROL:locked-conductor")
    zero=from_forcing((Q(0),)*N,"CONTROL:zero")
    receipt={"source":t.source_id,"N":N,"authenticated":t.validate(),
             "normality_proved":False,
             "evaluation_authority":"finite mpmath diagnostic only",
             "prefix_sha256":hashlib.sha256("".join(
                 f"{v.n}:{v.forcing}:{v.state}:{v.carry}\n"
                 for v in t.points).encode()).hexdigest()}
    for key,history in (("bbp",t),("conductor_locked_control",fake),
                        ("zero_forcing_control",zero)):
        a=build(history,3,(),0)
        b=build(history,3,(3,5),1)
        assert coarsen(b,3,(),0)==a
        assert all(invert_atom(b,atom)==B for atom,B in b.blocks.items())
        g,c=energies(b,1)
        assert g==energies(a,1)[0]
        assert c-energies(a,1)[1]==variance(b,a,1)
        q,_=conditioned_innovation(history,3,(3,5),1)
        receipt[key]={
            "coarse_atoms":len(a.blocks),"refined_atoms":len(b.blocks),
            "global_energy_numeric":str(g.evaluation(65).real)[:22],
            "conditional_energy_numeric":str(c.evaluation(65).real)[:22],
            "selected_innovation_numeric":str(q.evaluation(65).real)[:22]}
    receipt["exceptional_3"]=[valuation(authentic_r(i).denominator,3)
                               for i in (2,8)]
    receipt["exceptional_5"]=[valuation(authentic_r(i).denominator,5)
                               for i in (4,24)]
    receipt["p7_count_N77"]=pole_count(77,7)[0]
    receipt["p7_p11_sieve"]=pole_crt_sieve(77,(7,11))
    return receipt


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",action="store_true",
                        help="replay exact identities; numerical fields remain diagnostics")
    parser.parse_args()
    print(json.dumps(run(),indent=2,sort_keys=True))
