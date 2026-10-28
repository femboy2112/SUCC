"""A finite PRIOR over phase hypotheses of the original eight-tap BBP chiral shell.

The ORIGINAL physical source has phase zero, not random phase. This prior
only describes an observer who has not yet received the distinguishing
source receipts. It does not randomize U0=0 or the four BBP forcing poles.

The exact original taps shrink by 16**(-floor(n/8)), so an activity-only
sensor that sees infinitesimal nonzero taps assumes unlimited resolution or
a declared gain/pumping system. A fixed absolute detection floor eventually
returns zero under every phase hypothesis.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import log

TAPS=(F(4),F(0),F(0),F(-2),F(-1),F(-1),F(0),F(0))
ACTIVE=tuple(int(x!=0) for x in TAPS)


def _prior(prior):
    if len(prior)!=8:
        raise ValueError('eight source-phase hypotheses are required')
    result=tuple(F(p) for p in prior)
    if any(p<0 for p in result) or sum(result,F())!=1:
        raise ValueError('valid normalized phase prior required')
    return result


def uniform_phase_prior():
    return (F(1,8),)*8


def predicted_activity(phase:int, time:int)->int:
    if type(phase) is not int or not 0<=phase<8 or type(time) is not int or time<0:
        raise ValueError('phase index 0..7 and nonnegative receipt time required')
    return ACTIVE[(phase+time)%8]


def posterior_phase(prior, evidence, flip_probability=F(0)):
    """Exact Bayes prior update from chronological nonzero/zero source taps.

    Evidence is list/tuple of (source_time, observed_bit). The noise is
    stipulated conditionally independent across observed receipts. No
    information is available without an actual receipt (time, outcome).
    """
    masses=list(_prior(prior))
    err=F(flip_probability)
    if not 0<=err<=F(1,2):
        raise ValueError('sensor flip probability must be in [0,1/2]')
    for t,y in evidence:
        if type(y) is not int or y not in (0,1):
            raise ValueError('observed activity must be one of {0,1}')
        for k in range(8):
            masses[k] *= (1-err) if predicted_activity(k,t)==y else err
    total=sum(masses,F())
    if total==0:
        raise ValueError('evidence impossible under supplied prior/sensor')
    return tuple(m/total for m in masses)


def minimum_identifying_horizon()->int:
    """Earliest n when every source phase has distinct n-bit activity word."""
    for n in range(1,9):
        words={tuple(predicted_activity(phase,t) for t in range(n)) for phase in range(8)}
        if len(words)==8:
            return n
    raise ArithmeticError('eight periodic tap shifts not distinguishable')


def phase_hamming_distance(a:int,b:int)->int:
    return sum(predicted_activity(a,t)!=predicted_activity(b,t) for t in range(8))


def expected_log_odds_gain_per_period(actual:int,other:int,flip_probability) -> float:
    """Expected log Bayes factor in one full source period (natural logs).

    Positive for 0<epsilon<1/2 and distinguishable phase classes. This is
    NOT a universal proof of observer optimality; it assumes a calibrated
    binary sensor and independent repeated source receipts.
    """
    e=F(flip_probability)
    if not 0<e<F(1,2):
        raise ValueError('expected log gain requires nondegenerate sensor')
    return phase_hamming_distance(actual,other)*float(1-2*e)*log(float((1-e)/e))


def authentic_chiral_tap(index:int)->F:
    """Exact signed original contracting eight-shell source coefficient."""
    if type(index) is not int or index < 0:
        raise ValueError('nonnegative signed source index required')
    k,j=divmod(index,8)
    return TAPS[j] / 16**k


def resolved_activity(phase:int,time:int, absolute_floor=F(0)) -> int:
    """Exact thresholded original source activity, no free reamplification.

    A nonzero coefficient with absolute value <= floor cannot be distinguished
    from zero by the declared sensor; floor=0 is an ideal exact sensor.
    """
    tap=authentic_chiral_tap(phase+time)
    floor=F(absolute_floor)
    if floor<0:
        raise ValueError('resolution floor must be nonnegative')
    return int(abs(tap)>floor)


def guaranteed_silence_cycle(absolute_floor)->int:
    """A sufficient finite eight-shell cycle beyond which ALL phases silent.

    For k>=K, 4/16**k<=floor. For any phase shift 0..7,
    every source index >=8K lies in a cycle k>=K.
    """
    floor=F(absolute_floor)
    if floor<=0:
        raise ValueError('strictly positive floor required')
    k=0
    while F(4,16**k)>floor:
        k+=1
    return k
