"""Independent exact finite checks for a Poisson-potential regret theorem.

Uses no SUCC production imports and no floating-point arithmetic.
Finite checks calibrate formulas; the infinite theorem is in the companion note.
"""
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path


def point(t):
    t = F(t)
    return ((1-t*t)/(1+t*t), 2*t/(1+t*t))


def kernel(z, w):
    # Dot-product formula is independent of production chord-distance code.
    return F(3)/(5-4*(z[0]*w[0]+z[1]*w[1]))


def energy(path):
    return sum((kernel(z,w) for z in path for w in path), F(0))/len(path)**2


def mean_potential(path, z):
    return sum((kernel(z,w) for w in path), F(0))/len(path)


def main():
    pool = (point(0), point(1), point(-1), (F(-1),F(0)), point(F(1,2)))
    probes = pool + (point(F(-2,3)), point(F(3,5)), point(F(5,3)))
    local_checks = identity_checks = regret_checks = 0
    for size in range(1,5):
        for path in product(pool, repeat=size):
            e = energy(path)
            assert e >= 1
            for z in probes:
                d = mean_potential(path,z)-1
                assert d*d <= 2*(e-1)
                local_checks += 1
            signed = F(0)
            positive = F(0)
            for n in range(1,size):
                a = sum((kernel(path[n],w) for w in path[:n]),F(0))-n
                signed += a
                positive += max(F(0),a)
                assert a*a <= 2*n*n*(energy(path[:n])-1)
                regret_checks += 1
            assert e == 1+F(2,size)+F(2,size*size)*signed
            assert e <= 1+F(2,size)+F(2,size*size)*positive
            identity_checks += 1

    z=point(0)
    e=energy((z,))
    d=mean_potential((z,),z)-1
    assert d*d == 2*(e-1)  # Sharp constant 2.
    assert not d*d <= F(199,100)*(e-1)  # Mutated bound rejected.
    antipodes=(point(0),(F(-1),F(0)))
    truncated=sum((1+a[0]*b[0]+a[1]*b[1] for a in antipodes for b in antipodes),F(0))/4
    assert truncated==1 and energy(antipodes)==F(5,3)
    receipt={
        "status":"VERIFIED_FINITE",
        "scope":"Rational circle samples of size 1..4; five-point sample pool; eight probes",
        "local_potential_bound_checks":local_checks,
        "energy_regret_identity_checks":identity_checks,
        "individual_regret_bound_checks":regret_checks,
        "sharp_constant_mutation_rejected":True,
        "truncated_kernel_false_haar_control_rejected":True,
        "pi_normality_claim":False,
        "independent_of_SUCC_imports":True,
        "sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
