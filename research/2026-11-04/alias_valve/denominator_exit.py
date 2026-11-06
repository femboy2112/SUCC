"""An elementary source-specific upper envelope for finite alias-valve escape."""
from __future__ import annotations
from math import lcm
from alias_valve import force_closed, orbit, source_conductor, escape_depth


def envelope(A:int)->int:
    if not isinstance(A,int) or A<2: raise ValueError("A>=2")
    M=1
    for k in range(1,16*A+1): M=lcm(M,k)
    return 15*M


def verify_original_epoch(A:int,q:int)->dict:
    cap=envelope(A)
    states=orbit(2*A-1)
    # All source factors and all original zero-seeded states divide the cap.
    assert all(cap%force_closed(n).denominator==0 for n in range(1,2*A))
    assert all(cap%x.denominator==0 for x in states)
    D=source_conductor(2*A-1)
    assert cap%D==0
    L=escape_depth(cap,q)
    assert 16**L*q>=D
    return {"A":A,"q":q,"source_conductor_bits":D.bit_length(),
            "envelope_bits":cap.bit_length(),"guaranteed_depth":L}
