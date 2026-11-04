"""Rebuild the exact finite witness JSON. Invoke from this directory."""
import hashlib
import json
from math import gcd
from pathlib import Path
from fractions import Fraction
from finite_weyl import coordinate, trajectory


def receipt():
    prefixes = []
    for t in (13,29,47):
        m, xs = trajectory(t)
        a = (t+1)//2
        support = len(set(xs[a:2*a]))
        prefixes.append({
            "horizon": t, "conductor": str(m), "last_coordinate": str(coordinate(xs[-1],m)),
            "epoch": [a,2*a-1], "epoch_support": support,
            "trace_distance_lower_bound": str(1-Fraction(support,m)),
        })
    return {
        "preregistration_sha256": hashlib.sha256(Path("PREREGISTRATION.md").read_bytes()).hexdigest(),
        "prefixes": prefixes,
        "dual_towers": [{"M":m,"N":m*d,"additive_section_exists":gcd(m,d)==1,
                         "rotated_embedded_subgroup_mass":str(Fraction(1,d))}
                        for m in (5,9,15) for d in (3,5)],
        "source": "4ff640637d18b8161599402f7c6ba23388a63652/PQ-4",
        "authority": "finite exact rational probes; see WEYL_CONDUCTOR.md for paper proofs",
    }


if __name__ == "__main__":
    print(json.dumps(receipt(),indent=2,sort_keys=True))
