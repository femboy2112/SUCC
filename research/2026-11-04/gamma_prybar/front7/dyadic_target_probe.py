"""Outward-rational verification of the moving dyadic target."""
import json
from fractions import Fraction as F
from math import lcm
from hostile_probe import forcing, integer_path


def tail_cap(n):
    return F(1,(8*n+1)*(8*n+2))


def run(T):
    end = 4*T+3
    terms = [F(0)]+[forcing(n) for n in range(1,3*end+1)]
    actual, clocks, _ = integer_path(end)
    target = F(round(16**(3*T)*actual[4*T]/16**(4*T)),16**(3*T))
    next_reset, state, clock = T, F(0), 1
    min_positive = True
    circle_radius_ok = True
    resets = []
    for n in range(1,end+1):
        x = 16*state+terms[n]
        err = F(0)
        if n == next_reset:
            D = clocks[n//2]
            H = sum(terms[n+j]*F(1,16**j) for j in range(1,2*n+1))
            err = -F(round(D*(x+H-16**n*target)),D)
            lower = x+err+H-16**n*target
            radius = F(1,2*D) + F(tail_cap(3*n),16**(2*n))
            assert abs(lower) <= F(1,2*D)
            assert abs(lower+F(tail_cap(3*n),16**(2*n))) <= radius
            if n == T:
                assert abs(err) <= F(1,16**(2*T))+radius
            resets.append(n)
            next_reset *= 2
        state = x+err
        if n < T:
            assert state == actual[n]
        if n >= 3*T:
            assert (16**n*target).denominator==1
            circle_radius_ok &= min(state % 1,1-state%1)<F(1,64)
        clock = lcm(clock,(terms[n]+err).denominator)
        assert clock==clocks[n]
        min_positive &= terms[n]+err > 0
    return {'T':T,'through':end,'designated':resets,'all_forcings_positive':min_positive,
            'all_after_3T_within_1_over_64':circle_radius_ok}


if __name__=='__main__':
    print(json.dumps([run(T) for T in (28,56,112)],indent=2,sort_keys=True))
