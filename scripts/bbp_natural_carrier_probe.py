#!/usr/bin/env python3
"""Reproduce exact N-carrier BBP results and deliberate counterexamples."""
from __future__ import annotations

import json
from fractions import Fraction as Q
from math import comb

from observational_succ.bbp_natural_carrier import (
    ORIGIN, exact_forcing, forcing_numerator, forcing_denominator,
    NaturalBBPState, machine_step, orbit_prefix, cantor_pair, cantor_unpair,
    encode_state, decode_state, encoded_machine_step, dyadic_view,
    dyadic_observer_step, source_tail_enclosure, alpha_enclosure,
    certified_hex_digit,
)
from observational_succ.pi_joint_prime_carrier import (
    forcing as original_four_poles, local_primary, joint_circle,
)


def assert_exact(count: int = 150) -> dict:
    tally = {"forcing": 0, "orbit": 0, "dyadic": 0,
             "prime_torsion": 0, "encoded": 0, "digits": 0,
             "pascal": 0, "negative_controls": 0}
    prefix = orbit_prefix(count+1)
    for n in range(1,count+1):
        assert exact_forcing(n)==original_four_poles(n)
        tally["forcing"]+=1
    for n in range(count):
        s, nxt = prefix[n], prefix[n+1]
        assert nxt==machine_step(s)
        assert nxt.rational==16*s.rational+original_four_poles(n+1)
        assert nxt.denominator % 2
        tally["orbit"]+=3
        assert decode_state(encode_state(s))==s
        assert encoded_machine_step(encode_state(s))==encode_state(nxt)
        tally["encoded"]+=2
        for depth in (1,2,4,7,12,19):
            assert dyadic_view(nxt,depth)==dyadic_observer_step(n,dyadic_view(s,depth),depth)
            tally["dyadic"]+=1
        for p in (2,3,5,7,11,13,17):
            assert local_primary(nxt.rational,p)==(
                16*local_primary(s.rational,p)+local_primary(exact_forcing(n+1),p))%1
            tally["prime_torsion"]+=1
    for n in range(33):
        s = prefix[n]
        assert joint_circle(s.rational)==s.rational%1
        tally["prime_torsion"]+=1
        degree = min(n, 10)
        vals = prefix[n-degree:n+1]
        left=sum(((-1)**(degree-j)*comb(degree,j)*vals[j].rational
                  for j in range(degree+1)),Q())
        right=sum(((-1)**(degree-j)*comb(degree,j)*Q(vals[j].numerator,vals[j].denominator)
                   for j in range(degree+1)),Q())
        assert left==right
        tally["pascal"]+=1
    for n in list(range(64))+[73,89,100,127,149]:
        s = prefix[n]
        answer = certified_hex_digit(n, 24)
        assert answer is not None
        tail_lo, tail_hi = source_tail_enclosure(n, answer[1])
        assert tail_lo < tail_hi
        a = 16*(s.rational+tail_lo)
        b = 16*(s.rational+tail_hi)
        assert a.numerator//a.denominator==b.numerator//b.denominator
        assert answer[0]==(a.numerator//a.denominator)%16
        al,ah=alpha_enclosure(n)
        assert al==s.rational/16**n and ah>al
        tally["digits"]+=4
    # Explicit non-autonomous/missing-time failure of a naked T16 circle.
    assert ((16*ORIGIN.rational)%1)!=(machine_step(ORIGIN).rational%1)
    tally["negative_controls"]+=1
    # Circle data alone cannot support division by five without the lift.
    u,v=Q(1,7),Q(8,7)
    assert u%1==v%1 and (u/5)%1 !=(v/5)%1
    tally["negative_controls"]+=1
    # Global p2-integral inverse /16 is NOT total on all noncanonical states.
    backward=(Q(0)-exact_forcing(1))/16
    assert backward.denominator%2==0
    tally["negative_controls"]+=1
    return {"scope":"finite_exact_checks_not_normality_proof",
            "n_states":count,"assertions":sum(tally.values()),"counts":tally,
            "first_eight_hex_digits_alpha":"".join(
                format(certified_hex_digit(n,24)[0], 'X') for n in range(8)),
            "first_three_unnormalized_pairs":[
                {"n":s.time,"a":s.numerator,"b":s.denominator}
                for s in prefix[:3]],
            "pi_normality":"OPEN"}


if __name__=="__main__":
    print(json.dumps(assert_exact(),indent=2,sort_keys=True))
