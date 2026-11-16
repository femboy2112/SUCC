"""Original four-pole BBP: temporal 2-adic/circle signed interferometer.

The source recurrence, its exact Green bounds, and source clock are imported
from the sibling 'probe.py' of SUCC draft #646. There is NO normality claim.
"""
from __future__ import annotations
import cmath
import json
from fractions import Fraction
from math import pi
from pathlib import Path
import probe


def e(turns: float) -> complex:
    return cmath.exp(2j*pi*turns)


def source_mod16(n: int) -> int:
    return probe.stable_clock(n,1)


def source_mod16_formula(n: int) -> int:
    return (-n+2*(n%2))%16


def w(n: int) -> complex:
    # The input is source-derived: this must never be replaced by a guessed clock.
    delta=(source_mod16(n)-source_mod16(n+1))%16
    return e(delta/16)


def w_formula(n: int) -> complex:
    return e(-1/16)*(1j if n%2 else 1)


def source_clock_kernel(k: int, lag: int, a: int, b: int) -> complex:
    q=16**k
    return sum(e((a*probe.stable_clock(n,k)-b*probe.stable_clock(n+lag,k))/q)
               for n in range(q))/q


def phase_rational(x: Fraction, n: int) -> Fraction:
    return (16**n*x)%1


def weyl_shell(B: int, h: int, x: Fraction) -> complex:
    return sum(e(float(h*phase_rational(x,n))) for n in range(B,2*B))/B


def twisted_shell(B: int, h: int, x: Fraction) -> complex:
    return sum(w(n)*e(float(h*phase_rational(x,n)))
               for n in range(B,2*B))/B


def reconstructed_weyl(B: int, h: int, x: Fraction) -> tuple[complex,complex]:
    """Return exact-identity RHS and its finite endpoint correction."""
    omega=e(1/16)
    endpoint=(2/B)*(e(float(h*phase_rational(x,2*B)))
                    -e(float(h*phase_rational(x,B))))
    approx=omega/(1+1j)*(twisted_shell(B,h,x)+twisted_shell(B,16*h,x))
    corrected=approx-1j/(2*(1+1j))*endpoint
    return approx,corrected


def lag_green_finite(n: int, k: int, extra_depth: int = 12) -> bool:
    """Exact rational finite partial analogue of 16^k*T_n = Delta_k+T_(n+k)."""
    source=lambda a:probe.forcing(a)
    delta=sum(Fraction(16)**(k-j)*source(n+j) for j in range(1,k+1))
    t=sum(source(n+j)/16**j for j in range(1,k+extra_depth+1))
    tn=sum(source(n+k+j)/16**j for j in range(1,extra_depth+1))
    return 16**k*t-tn==delta


def temporal_character(B: int, x: Fraction, k: int, lag: int,
                       h: int, j: int, a: int, b: int) -> complex:
    """Two-time REAL phase + two-time original 2-adic source characters."""
    q=16**k
    return sum(e((a*probe.stable_clock(n,k)-b*probe.stable_clock(n+lag,k))/q)
               *e(float(h*phase_rational(x,n)-j*phase_rational(x,n+lag)))
               for n in range(B,2*B))/B


def critical_pulse(B: int) -> dict:
    """Certified finite original-zero critical seam pulse; no long-time inference."""
    k=probe.critical_depth(B)
    q=16**k
    states=probe.lifted_states(2*B-1)
    hits=0
    signed=0
    complex_signed=0j
    max_depth=0
    for n in range(B,2*B):
        packet=probe.certified_prefix(states[n],n,k)
        if q*packet['tail_high']>=1:
            raise ArithmeticError('critical tail violates single-step hypothesis')
        d=packet['increments']
        A=packet['uncompleted']
        if d not in (0,1):
            raise ArithmeticError('unexpected multi-step source seam')
        orient = 1 if A%2==0 else -1
        hits+=d
        signed+=d*orient
        complex_signed+=w(n)*d*orient
        max_depth=max(max_depth,packet['depth'])
    val=complex_signed/B
    return {'B':B,'k':k,'q':q,'seam_hits':hits,'signed_parity':signed,
            'complex_signed_real':round(val.real,12),
            'complex_signed_imag':round(val.imag,12),
            'max_future_terms':max_depth,'pi_normality':'OPEN'}


def make_report() -> dict:
    src_16=[source_mod16(n) for n in range(16)]
    assert src_16==[source_mod16_formula(n) for n in range(16)]
    kernel=source_clock_kernel(1,1,1,1)
    wrong=-e(-1/16)*(1+1j)/2
    return {
      'source':'original zero-seeded four-pole BBP; F(0)=0 paper premise of #646',
      'first_residue_map':src_16,
      'nontrivial_clock_kernel':{'real':round(kernel.real,12),'imag':round(kernel.imag,12)},
      'critical_original_shells':[critical_pulse(B) for B in (8,16,32,64,96)],
      'coherent_wrong_seed_critical_pulse':{'real':round(wrong.real,12),
                                           'imag':round(wrong.imag,12)},
      'signed_mixer_normality_bound':'OPEN',
      'original_pi_normality':'OPEN',
    }


if __name__=='__main__':
    print(json.dumps(make_report(),indent=2,sort_keys=True))
