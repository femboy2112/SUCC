"""Independent d=1 rational reconstruction; imports no analytic implementation."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def r(n):
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def main():
    mass, mean = r(1), r(2)/r(1)
    assert mass == F(47, 15) and mean == F(530, 12831)
    assert 0 < mean < 1
    resolvent = lambda t: mass/(t-mean)
    center = resolvent(16)
    norm = r(3)-r(2)**2/r(1)
    assert norm > 0
    lo = center+norm/(16*(16-mean)**2)
    hi = center+norm/(15*(16-mean)**2)
    trunc = sum((r(n)/16**n for n in range(1, 41)), F())
    tail = r(41)/(15*16**40)
    assert lo < trunc < trunc+tail < hi
    assert 0 < trunc-center < F(188, 225*3600)
    fake = lambda n: mass*mean**(n-1)
    assert fake(1) == r(1) and fake(2) == r(2)
    assert r(3)-fake(3) == norm
    budget = mass*mean/((1-mean)*(16-mean))
    assert budget == (resolvent(1)-16*resolvent(16))/15
    u = F()
    for n in range(1, 65):
        u = 16*u+fake(n)
        assert u == 16**n*center - mass*mean**n/(16-mean)
    p = [F(1, 2)]+[F(1, 30)]*15
    assert sum(p) == 1 and min(p) > 0
    factor = 16*sum(x*x for x in p)
    assert factor == F(64, 15) > 1
    poly = lambda x: x*x-x-3
    assert poly(-2) > 0 > poly(-1)  # conjugate strictly less than -1
    dossier = Path(__file__).resolve().parent.parent/'analytic/ANALYTIC_TRANSPORT.md'
    print(json.dumps(dict(status="PASS", domain="d=1 exact rational crosscheck, not general proof",
        analytic_dossier_sha256=hashlib.sha256(dossier.read_bytes()).hexdigest(),
        source_mass=str(mass), gaussian_node=str(mean), rational_boundary=str(center),
        source_third_deficit=str(norm), exact_tail_budget=str(budget),
        direct_bbp_terms=40, fake_path_checks=64, biased_collision_factor=str(factor),
        non_pisot_negative_root_interval=[-2, -1],
        authority="same-model different implementation; no independent referee"), indent=2))


if __name__ == "__main__":
    main()
