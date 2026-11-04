"""Deliberately separate exact algebra/partition oracle for shifted BBP currents.

Does not import the primary selected_current implementation. No pi digits.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import lcm


def independent_collapsed_r(n):
    if type(n) is not int or n<1:raise ValueError('source time')
    return Q(120*n*n - 89*n + 16,
             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def finite_source_epoch(A):
    if type(A) is not int or A<1:raise ValueError('positive A')
    tape=[independent_collapsed_r(n) for n in range(1,2*A)]
    D=1
    for z in tape:D=lcm(D,z.denominator)
    assert D%2
    v=0
    out=[]
    for n,z in enumerate(tape,1):
        v=(16*v+z.numerator*(D//z.denominator))%D
        if n>=A:out.append(Q(v,D))
    return tuple(out)


def independent_shift_integral(cloud,m):
    if type(m) is not int or m<1 or not cloud:raise ValueError('mesh/cloud')
    values=tuple(Q(z)%1 for z in cloud)
    # Bin labels change only when one point hits any translated cell edge.
    edges={Q(0),Q(1)}
    for z in values:
        for j in range(m):edges.add((Q(j,m)-z)%1)
    edges=sorted(edges)
    N=len(values)
    integral=Q(0)
    for i in range(len(edges)-1):
        a,b=edges[i:i+2]
        shift=(a+b)/2
        bins={}
        for z in values:
            w=(m*((z+shift)%1))//1
            bins[w]=bins.get(w,0)+1
        integral+=(b-a)*Q(m*sum(c*c for c in bins.values()),N*N)
    return integral


def check_declared_holdouts():
    import importlib.util
    from pathlib import Path
    path=Path(__file__).with_name('selected_current.py')
    spec=importlib.util.spec_from_file_location('selected_current_source',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for n in (1,2,3,7,17,49,89):
        assert independent_collapsed_r(n)==module.source_force(n)
    for A in (12,24,40,80,160):
        own=finite_source_epoch(A)
        assert own==module.source_epoch(A)
        if A<=24:
            for m in (4,8,16):
                assert independent_shift_integral(own,m)==module.translated_energy(own,m)
    return {'independent_source': 'collapsed A/D plus integer common modulus',
            'origin_integral': 'piecewise exact partition; no triangular pair formula',
            'status':'PASS', 'pi_digits_instrument':False}

if __name__=='__main__':
    import json
    print(json.dumps(check_declared_holdouts(),indent=2))
