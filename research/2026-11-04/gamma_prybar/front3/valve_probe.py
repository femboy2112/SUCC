"""Exact, standalone positive BBP alias-flow probes. No external digits."""
from fractions import Fraction as F
from math import lcm
import hashlib
import json


def force(n):
    return 4 * F(1, 8*n-7) - 2 * F(1, 8*n-4) - F(1, 8*n-3) - F(1, 8*n-2)


def collapsed(n):
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def digest(x):
    return hashlib.sha256(str(x).encode("ascii")).hexdigest()


def one_epoch(A, K):
    q = 16**K // 2
    M = 2*A
    force_terms = [force(n) for n in range(1, M+1)]
    B = lcm(*(r.denominator for r in force_terms[:A]))
    alpha_M = sum(r / 16**j for j, r in enumerate(force_terms, 1))
    targets = {"coherent": F(0), "periodic": F(1,16**(2*K)-1)}
    seeds = {name: F(round(B*(c-alpha_M)), B) for name, c in targets.items()}
    seeds["original"] = F(0)
    D = lcm(*(r.denominator for r in force_terms))
    out = {}
    for name, seed in seeds.items():
        # Two implementations shared only through the same initial rational.
        integer = seed.numerator * (D // seed.denominator)
        literal = seed
        cloud = []
        for n, f in enumerate(force_terms, 1):
            g = collapsed(n)
            integer = 16*integer + g.numerator*(D//g.denominator)
            literal = 16*literal + f
            assert F(integer,D) == literal
            if A <= n < M:
                cloud.append(integer % D)
        lateral = leakage = predicted_pairs = 0
        for i, x in enumerate(cloud):
            for j, y in enumerate(cloud):
                z = (x-y) % D
                dist = min(z,D-z)
                scaled = 16*z
                pocket = (2*scaled+D)//(2*D)
                weight = max(0,D-q*abs(scaled-pocket*D)) if pocket % 16 else 0
                lateral += weight
                leakage += max(0,D-q*dist)-max(0,D-16*q*dist)
                ri, rj = (A+i)%(2*K), (A+j)%(2*K)
                if name == "periodic" and max(ri,rj) == 2*K-1 and min(ri,rj) <= K-2:
                    assert 2*weight >= D
                    predicted_pairs += 1
        injection, escape = (F(v, D*A*A) for v in (lateral, leakage))
        injection_cap = F(1,K)+F(2,A)+F(16*q,64*A*A)
        assert injection <= injection_cap
        assert escape <= injection_cap + F(2,A)+F(q, A*A)
        if name == "coherent":
            assert not lateral
        if name == "periodic":
            assert predicted_pairs >= 2*(K-1)*(A//(2*K))**2
        out[name] = {"lateral_fraction_sha256": digest(injection),
                     "leakage_fraction_sha256": digest(escape),
                     "lateral_ppm_floor": int(injection*10**6),
                     "leakage_ppm_floor": int(escape*10**6),
                     "certified_periodic_pairs":predicted_pairs}
    return {"A":A, "K":K,"q":q,"B_passes_AS02": B>4*A*A*16**(2*A), "seeds":out}


if __name__ == "__main__":
    print(json.dumps([one_epoch(A,K) for A,K in [(128,2),(160,3),(192,4)]],indent=2))
