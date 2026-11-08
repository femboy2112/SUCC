"""Exact all-continuum-radius test (finite certified). No infinite claim."""
from __future__ import annotations
from fractions import Fraction
from time import perf_counter
from epoch_fejer import circle_states


def max_all_radius_ratio(A: int):
    if type(A) is not int or A < 2: raise ValueError("A integer >=2")
    x = circle_states(2*A)[A:]
    start = perf_counter()
    distances=[]
    for i in range(A):
        for j in range(i):
            d = abs(x[i]-x[j]); distances.append(min(d,1-d))
    distances.sort()
    lower=Fraction(1,A+1)
    cnt=A; pos=0
    while pos<len(distances) and distances[pos]<=lower:
        cnt += 2; pos+=1
    worst = Fraction(cnt-A, A*A*lower)
    at = lower
    while pos<len(distances):
        distance=distances[pos]
        while pos<len(distances) and distances[pos]==distance:
            cnt+=2; pos+=1
        candidate=Fraction(cnt-A,A*A*distance)
        if candidate>worst:
            worst,at=candidate,distance
    assert cnt==A*A
    return {"A":A,"all_radius_bound_K3":worst<=3,"max_K_float_diagnostic":float(worst),
            "max_K_exact_comparison_3":worst<=Fraction(3),
            "max_at_radius_float":float(at), "count_at_half":cnt,
            "pair_count":len(distances), "wall_seconds_diagnostic":round(perf_counter()-start,3)}
