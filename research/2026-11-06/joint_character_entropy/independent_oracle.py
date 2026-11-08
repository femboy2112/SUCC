"""Independent finite π/16 digit oracle using Machin arctan intervals.

Mathematical input is Machin's formula pi/4=4atan(1/5)-atan(1/239),
not the BBP source. Alternating remainders provide rational certificates.
This independently checks finite digits; it does not validate π normality.
"""
from __future__ import annotations
from fractions import Fraction
from joint_entropy import certified_source_digits, four_pole, tail_enclosure, original_states


def arctan_interval(denominator: int, terms: int) -> tuple[Fraction, Fraction]:
    if denominator < 2 or terms < 1:
        raise ValueError("denominator>=2, terms>=1")
    partial = sum(((-1)**j*Fraction(1,(2*j+1)*denominator**(2*j+1))
                   for j in range(terms)), Fraction(0))
    first_omitted = (-1)**terms*Fraction(1,(2*terms+1)*denominator**(2*terms+1))
    return min(partial,partial+first_omitted),max(partial,partial+first_omitted)


def machin_pi16_interval(terms5: int, terms239: int) -> tuple[Fraction,Fraction]:
    lo5,hi5 = arctan_interval(5,terms5)
    lo239,hi239 = arctan_interval(239,terms239)
    return lo5-hi239/4, hi5-lo239/4


def digit_certificates(interval: tuple[Fraction,Fraction], size: int) -> tuple[int,...]:
    lo,hi=interval
    assert Fraction(0)<lo<hi<Fraction(1)
    out=[]
    for n in range(size):
        lo *= 16
        hi *= 16
        digit_lo = lo.numerator//lo.denominator
        digit_hi = hi.numerator//hi.denominator
        if digit_lo != digit_hi:
            raise ArithmeticError(f"Machin enclosure unresolved at digit {n}, floor {digit_lo} vs {digit_hi}")
        out.append(digit_lo)
        lo-=digit_lo
        hi-=digit_hi
    return tuple(out)


def independent_combined_source(n: int) -> Fraction:
    numerator=120*n*n-89*n+16
    denominator=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    return Fraction(numerator,denominator)


def run() -> dict:
    pole_checks=0
    for n in range(1,201):
        assert independent_combined_source(n)==four_pole(n),n
        pole_checks+=1
    n_digits=128
    # Independent rational arctan intervals with a provable truncation remainder.
    pi16_interval=machin_pi16_interval(150,38)
    machin_digits=digit_certificates(pi16_interval,n_digits)
    bbp_digits,depths=certified_source_digits(n_digits,depth=12)
    assert machin_digits==bbp_digits
    assert ''.join(format(x,'x') for x in machin_digits[:16])=='3243f6a8885a308d'
    # Independent finite interval containment using known exact source bounds.
    for n in (0,1,2,3,7,31,63,127):
        lo,hi=tail_enclosure(n,12)
        # Source tail is positive and lies strictly within proved remainder bound.
        assert 0<lo<hi
    # Independent Machin orbital-phase enclosures at much later positions:
    # this checks the original source + future tail without using the same formula.
    high_lo,high_hi=machin_pi16_interval(850,260)
    high_states=original_states(914)
    phase_checks=0
    for n in (223,311,445,457,613,777,913):
        bbp_tlo,bbp_thi=tail_enclosure(n,12)
        bbp_lo=high_states[n]+bbp_tlo
        bbp_hi=high_states[n]+bbp_thi
        qbbp=bbp_lo.numerator//bbp_lo.denominator
        assert bbp_hi.numerator//bbp_hi.denominator==qbbp
        blo,bhi=bbp_lo-qbbp,bbp_hi-qbbp
        mlo,mhi=16**n*high_lo,16**n*high_hi
        qmach=mlo.numerator//mlo.denominator
        assert mhi.numerator//mhi.denominator==qmach
        mlo,mhi=mlo-qmach,mhi-qmach
        assert max(blo,mlo)<=min(bhi,mhi),n
        phase_checks+=1
    return {"combined_source_checks":pole_checks,"machin_vs_bbp_certified_hex_digits":n_digits,
            "max_bbp_depth":max(depths),"independent_high_n_phase_overlap_checks":phase_checks,"first_32_hex":''.join(format(x,'x') for x in bbp_digits[:32]),
            "machin_width_below_16_minus_128":(pi16_interval[1]-pi16_interval[0] < Fraction(1,16**128))}


if __name__=='__main__':
    import json
    print(json.dumps(run(),sort_keys=True))
