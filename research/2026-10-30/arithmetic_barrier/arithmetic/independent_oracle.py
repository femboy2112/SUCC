"""Separate executable derivation: imports no campaign/parent arithmetic helper.

One agent/reasoner, distinct implementation. Universal authority is the paper
proof; these are exact finite checks and raw modular witnesses only.
"""
from datetime import datetime, timezone
from fractions import Fraction as R
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys
import time


def residue(x, m):
    return x.numerator*pow(x.denominator, -1, m) % m


def selected(n, c, offsets=(1,4,5,6)):
    result = R()
    # Unrolled polynomial rather than transport.py's recurrence.
    for j in range(n):
        forcing = sum((R(v)/(8*j+d) for d, v in zip(offsets, c)), R())
        result += 16**(n-j-1)*forcing
    return result


def independent_case(p, a, k, c):
    Q = p**a
    cls = Q % 8
    lastq = 8*k-(2 if cls in (1,5) else 1)
    lastdelta = (Q*lastq) % 8
    N = (Q*lastq-lastdelta)//8+1
    assert p > lastq and 8*N-2 < Q*p
    A,B,C,D = map(R, c)
    support, coeff = {
        1: ((1,4,5,6), (A,B,C,D)),
        5: ((1,4,5,6), (-4*C,B,-A/4,D)),
        3: ((2,3,4,7), (-8*D,A,-2*B,C)),
        7: ((2,3,4,7), (32*D,16*C,8*B,A)),
    }[cls]
    predicted = sum((R(v)*16**(k-j-1)/(8*j+d)
                     for j in range(k) for d,v in zip(support,coeff)), R())
    direct = Q*selected(N,c)
    assert residue(direct, p) == residue(predicted,p)
    derivative = sum((R(v)*16**(k-j-1)*(lastq-(8*j+d))/(8*j+d)
                      for j in range(k) for d,v in zip(support,coeff)), R())
    next_sum = R()
    for j in range(N):
        for d,v in zip((1,4,5,6),c):
            den=8*j+d
            if den % (p**(a-1)) == 0 and den % Q != 0:
                next_sum += R(v)*16**(N-j-1)/(den//p**(a-1))
    chi = 1 if p % 8 in (1,7) else -1
    theta = (chi*2**((p-1)//2)-1)//p
    lifted = predicted + p*(theta*derivative+next_sum)
    assert residue(direct,p*p)==residue(lifted,p*p)
    return dict(p=p, exponent=a, k=k, Q_class8=cls, native_time=N,
                source_mod_p=residue(direct,p), source_mod_p2=residue(direct,p*p),
                shadow_mod_p2=residue(predicted,p*p), theta_mod_p=theta%p,
                derivative_mod_p=residue(derivative,p), next_layer_mod_p=residue(next_sum,p))


def main():
    started=datetime.now(timezone.utc).isoformat()
    tick=time.monotonic()
    authentic=(4,-2,-1,-1)
    families=(authentic,(5,-2,-1,-1),(4,0,-1,0),(5,7,2,-3),
              (R(1,2),R(-2,3),R(7,5),R(-11,4)))
    primes=(131,137,139,149,151,157,163,167,173,179,181,191,193,197,199)
    cases=[(p,1,k) for p in primes for k in (1,2,4)]
    cases += [(13,1,1),(19,1,1),(7,2,1),(11,2,1),(13,2,1),(17,2,1),
              (19,2,2),(23,2,2),(11,3,1),(7,4,1)]
    rows=[]
    comparisons=0
    for p,a,k in cases:
        for c in families:
            row=independent_case(p,a,k,c)
            comparisons += 1
            if c==authentic:
                rows.append(row)
    births=[]
    for p,maxa in ((3,6),(5,4),(7,4),(11,3),(13,2),(17,2),(19,2)):
        for a in range(1,maxa+1):
            Q=p**a
            if Q%8==1:
                n=(Q+7)//8; expected=R(4)
            elif Q%8==5:
                n=(Q+3)//8;expected=R(-1)
            else:
                n=(Q+1)//4;expected=R(-1,2)
            u=selected(n,authentic)
            actual=residue(Q*u,p)
            assert actual==residue(expected,p) and actual!=0
            births.append(dict(p=p,exponent=a,time=n,scaled_residue=actual,valuation=-a))
    packet19=[]
    for n in range(5,18):
        u=selected(n,authentic)
        present=u.denominator%19==0
        assert present==(n<10 or n>=17)
        packet19.append(dict(n=n,conductor19_present=present,scaled_residue=residue(19*u,19)))
    null_births=[]
    Z=(-8,8,4,8,2,2,-1,0)
    for p,maxa in ((3,6),(5,4),(7,4),(11,3),(13,2),(17,2)):
        for a in range(1,maxa+1):
            Q=p**a
            if Q<7:
                continue
            n=(Q+7)//8
            e=selected(n,Z,tuple(range(1,9)))
            actual=residue(Q*e,p)
            assert actual==Z[Q%8-1]%p and actual!=0
            assert -R(1,8*n+1)<e<0
            null_births.append(dict(p=p,exponent=a,time=n,scaled_residue=actual,
                                   valuation=-a,strict_signed_tail_bound=True))
    source_dir=Path(__file__).resolve().parent
    script_hashes={name:sha256((source_dir/name).read_bytes()).hexdigest()
                   for name in ('transport.py','test_transport.py','independent_oracle.py')}
    result=dict(status='PASS',authority='finite exact arithmetic; paper proof separate',
                independent_reasoner=False,imports_primary_implementation=False,
                started_utc=started,elapsed_seconds=time.monotonic()-tick,
                python=sys.version,git_head=subprocess.check_output(
                    ['git','rev-parse','HEAD'],text=True).strip(),
                command='python research/2026-10-30/arithmetic_barrier/arithmetic/independent_oracle.py',
                source_sha256=script_hashes,fresh_primes=list(primes),
                coefficient_families=[[str(x) for x in c] for c in families],
                exact_shadow_and_lift_cases=comparisons,authentic_rows=rows,
                birth_rows=births,packet19_rows=packet19,null_source_birth_rows=null_births,
                negative_controls={'naive_p2_p13_k1_discrepancy':65,
                  'p73_k4_primary_residue':residue(selected(4,authentic),73),
                  'p47_native_return_k1_residue':residue(selected(1,authentic),47),
                  'p47_native_return_k2_residue':residue(selected(2,authentic),47)})
    assert residue(13*selected(10,authentic)-selected(1,authentic),169)==65
    assert selected(274,authentic).denominator%73!=0
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
