"""Reproduce the EXACT finite-Gaussian SUCC receipt. No zeta zero inputs."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from pathlib import Path
from observational_succ import gaussian_weil_certificates as g


def record():
    K=g.gram()
    for row in K:
        assert len(row)==6
    eigenvalues=["13/4","3/4","3/4","3/4","1/4","1/4"]
    pivots=[str(x) for x in g.ldl_pivots(K)]
    variances=[str(g.posterior(g.ORDER[2:2+n],[0]*n,"N")[1])
               for n in range(1,5)]
    result={
        "proof_scope":"EXACT_FINITE_ONLY__RH_NOT_PROVED",
        "source_parent":"9405013730d8b11d016e42736146243a77ff3d5e",
        "sphere_order":list(g.ORDER),
        "gram":[[str(x) for x in r] for r in K],
        "eigenvalues_independent_claim":eigenvalues,
        "ldl_pivots":pivots,
        "north_pole_variance_given_equator":variances,
        "prime_orientations":{str(p):g.oriented_area(g.prime_chart_action(p))
                              for p in (3,5,7,11)},
        "fake_6_orbit_size":len(set(g.equator_action(6).values())),
        "gamma_tail":{"J1":str(g.gamma_tail(1)),"J2":str(g.gamma_tail(2))},
        "bounded_step_example":str(g.step_operator_error(F(1,5),2,10,F(7))),
        "source_signed_form_certificate":"UNVERIFIED",
    }
    assert pivots==["1","15/16","3/5","7/12","15/28","39/80"]
    assert variances==["3/4","2/3","7/12","5/9"]
    assert result["bounded_step_example"]=="1784/10125"
    return result


def main():
    arg=argparse.ArgumentParser()
    arg.add_argument("--verify",type=Path)
    args=arg.parse_args()
    result=record()
    if args.verify:
        assert json.loads(args.verify.read_text(encoding="utf-8"))==result
        print("GAUSSIAN_WEIL_EXACT_RECEIPT_VERIFIED")
    else:
        print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
