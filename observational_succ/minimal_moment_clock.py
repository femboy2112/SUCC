"""Smallest alias-free modular frame for exact high circle Fourier moments.

Exact finite optimization, not an inference about the selected pi trajectory.
The unit-clock option preserves the multiplier as a permutation.
"""
from math import gcd
from .minimal_circle_carry import occupancies

def minimum_moment_clock(base,length,degree,*,require_unit=False,
                         max_modulus=12000,max_states=130000):
    """Smallest integer q reproducing the Haar 2k moment on the full q-grid.

    Precisely: all distinct k-term base-b frequencies remain distinct mod q.
    Requires b>=2, N>=1, k<=b. The search exhausts every smaller
    admissible q>=the necessary count of source multisets.
    """
    if (type(base) is not int or base<2 or type(length) is not int
            or length<1 or type(degree) is not int or not 0<=degree<=base
            or type(max_modulus) is not int or max_modulus<2
            or type(max_states) is not int or max_states<1):
        raise ValueError("invalid source or clock parameters")
    src=list(occupancies(length,degree))
    if len(src)>max_states:
        raise ValueError("finite source budget exceeded")
    addresses=tuple(sum(v*base**j for j,v in enumerate(a)) for a in src)
    if len(set(addresses))!=len(src):
        raise AssertionError("no-carry source integer addresses must be distinct")
    for modulus in range(max(2,len(src)),max_modulus+1):
        if require_unit and gcd(modulus,base)!=1:
            continue
        if len({x%modulus for x in addresses})==len(src):
            return modulus,len(src)
    raise ValueError("no exact moment clock inside the declared search budget")
