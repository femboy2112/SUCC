"""Independent, exact integer BBP block enclosure for a long hexadecimal prefix.

It evaluates the *unchanged* four-pole rational source via its algebraically
identical combined numerator/denominator. No π oracle, floating comparison,
uncertified roundoff, or alteration of the zero-seeded source is involved.

π = Σ_(n>=1) 16^(1-n) r(n), r(n)>0.
For K=N+guard, Q=16^K, L=Σ_(n=1)^K floor(Q*16^(1-n) r(n)),
0 <= Qπ-L < K + (16/15) r(K+1) < K+1 (K>=2).
Thus π ∈ [L/Q,(L+K+1)/Q]. If interval does not cross
an N-hex-digit cell, the first N hexadecimal digits are exact.
"""
from __future__ import annotations
import time


def certified_hex(n:int, guard:int=24):
    if type(n) is not int or n<2 or type(guard) is not int or guard<8:
        raise ValueError('N>=2 and guard>=8')
    K=n+guard
    scale=1<<(4*K)
    power=scale
    value=0
    start=time.monotonic()
    for idx in range(1,K+1):
        numerator=120*idx*idx-89*idx+16
        denominator=(2*idx-1)*(4*idx-1)*(8*idx-7)*(8*idx-3)
        value+=(power*numerator)//denominator
        power>>=4
    assert power==0 or power==1, power
    upper=value+K+1
    # The rational interval is enclosed within the same integer-part and first
    # N fraction-digit cells if integer division by 16^guard matches.
    left=value>>4*guard
    right=upper>>4*guard
    if left!=right:
        raise ArithmeticError('Ambiguous global BBP block, increase guard')
    # 'left' is floor(16^N*pi); subtract its integer part 3*16^N.
    firstdigits=left-(left>>4*n<<4*n)
    s=format(firstdigits,'X').zfill(n)
    if len(s)!=n:
        raise AssertionError('invalid hex digit count')
    return s,{'n':n,'guard':guard,'K':K,'integer_interval_width':K+1,
              'fractional_cell_width':1<<4*guard,'elapsed_s':round(time.monotonic()-start,3)}


if __name__=='__main__':
 import sys
 digits,detail=certified_hex(int(sys.argv[1]));print(detail, digits[:64],digits[-32:])
