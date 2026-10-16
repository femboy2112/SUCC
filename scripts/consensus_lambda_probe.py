"""Deterministic finite E consensus and depth receipt; no physical or RH authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

from observational_succ.source_lambda import Passport,Atlas,Read
from observational_succ.consensus_lambda import (
    Candidate,World,LambdaPort,EDevice,EFrame,ERelay,consensus,
    exact_portfolio,forcing_depth,two_chart_cross_energy,
    minimum_consensus_channel,horned_sphere_consensus_control,
)


def main():
    p=Passport("example-consensus-source",0)
    w=World(p,tuple(Candidate(f"s{k}",k,f"source-{k}") for k in range(4)))
    e1=EDevice("E1",p,("locked","open"),"locked",
        (LambdaPort("mod2",Read(2)),),
        {"locked":(),"open":("mod2",)},
        {("locked","unlock"):"open"})
    e2=EDevice("E2",p,("ready",),"ready",
        (LambdaPort("mod3",Read(3)),),{"ready":("mod3",)},{})
    forcing=forcing_depth(w,(e1,e2),max_radius=1)
    assert forcing.status=="FINITE_FORCING_DEPTH_CERTIFIED" and forcing.radius==1
    e1record=EFrame(e1).succ("unlock").record("mod2",atlas=Atlas.from_integer(p,3,(2,)))
    e2record=EFrame(e2).record("mod3",atlas=Atlas.from_integer(p,3,(3,)))
    combined=consensus(w,(e1record,e2record))
    assert combined.compatible==("s3",)
    remote=consensus(w,(e1record,ERelay(e1record,"E2")))
    assert remote.compatible==("s1","s3")
    interference=two_chart_cross_energy(1,1,2)
    assert interference["mixed_determinant"]==-3 and interference["witness_energy"]==-3
    # Full-repository-only integrations are optional in this isolated harness;
    # their absence stays named, never represented as success.
    try:
        channel=minimum_consensus_channel(w,e1,"mod2",e2,"mod3",radius=1)
    except ImportError:
        channel={"status":"NOT_RUN_MISSING_FULL_REPOSITORY_DEPENDENCY"}
    try:
        wild=horned_sphere_consensus_control(3,(1,2,3,7))
    except ImportError:
        wild={"status":"NOT_RUN_MISSING_FULL_REPOSITORY_DEPENDENCY"}
    receipt={
        "parent_branch":"research/succ-lambda-observation-calculus-2026-10-16",
        "model_source":p.source_id,"model_epoch":p.epoch,
        "finite_access_sphere_radius":forcing.radius,
        "optimal_portfolio":[list(x) for x in forcing.portfolio.selected],
        "portfolio_activations":[[a,b,list(path)] for a,b,path in forcing.portfolio.activation_paths],
        "joint_consensus":combined.status,
        "joint_candidates":list(combined.compatible),
        "relayed_same_evidence_candidates":list(remote.compatible),
        "local_diagonal_positive_but_joint_negative":not interference["whole_joint_operator_positive_semidefinite"],
        "exact_cross_energy":str(interference["witness_energy"]),
        "receiver_channel":channel,
        "wild_blindspot":wild,
        "actual_physical_source_authenticated":False,
        "global_source_identified":False,
        "completed_Weil_form_identified":False,
        "RH_proved":False,
    }
    print(json.dumps(receipt,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
