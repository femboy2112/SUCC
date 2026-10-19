"""INDEPENDENT NUMERICAL SCOUT, NOT A PROOF CERTIFICATE.

Under Mellin logarithmic coordinates the source's leading corner kernel
1/(2(u+v)) becomes convolution 1/(4*cosh((t-s)/2)).
The whole-line L2 norm is pi/2. This discrete numerical power-iteration
calibration is never used to certify the sharp original source theorem.
"""
import argparse
import json
from math import cosh, pi, sqrt


def log_window_scout(horizon, nodes=96, steps=80):
    if horizon <= 0 or nodes < 8 or steps < 1:
        raise ValueError("positive finite scout dimensions required")
    h = horizon/nodes
    x = [(-horizon+(i+0.5)*h) for i in range(nodes)]
    matrix = [[h/(4*cosh((s-t)/2)) for t in x] for s in x]
    v = [1/sqrt(nodes)]*nodes
    for _ in range(steps):
        w = [sum(a*b for a,b in zip(row,v)) for row in matrix]
        length = sqrt(sum(a*a for a in w))
        v = [z/length for z in w]
    top = sum(v[i]*sum(matrix[i][j]*v[j] for j in range(nodes))
              for i in range(nodes))
    return {"log_window":horizon,
            "numerical_top_value":round(top,10),
            "whole_line_analytic_carlemann_constant":round(pi/2,10)}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    v=[log_window_scout(n) for n in (8,16,32,64)]
    if args.verify:
        values=[r["numerical_top_value"] for r in v]
        assert all(0<x<pi/2+1e-4 for x in values)
        assert values==sorted(values)
        assert values[-1]>1.5
    print(json.dumps({"status":"NUMERICAL_HOLDOUT_NOT_PROOF",
        "source_zero_locations_used":False,
        "Carleman_controls":v,
        "RH_proved":False,
        "verification":"PASS" if args.verify else "UNVERIFIED"},sort_keys=True))


if __name__=="__main__":
    main()
