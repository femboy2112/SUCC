"""Pointed-circle cuts, 16-adic solenoid memories and original BBP time clock.

Research source: SUCC draft PR #319, original four-pole forcing and U0=0.
No normality or real-circle decorrelation follows from the proved 2-adic
isometry/permutation. Exact finite code: standard-library Fraction only.
The sole native source import is the authoritative authentic_r function.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd
from typing import Iterator

from .succ_internal_matrix_walk import authentic_r

RADIX = 16
SOURCE_PASSPORT = 'Coherent-Main-X-original-four-pole-zero-seed'


def _int(value, name, least=0, greatest=1000000):
    if type(value) is not int or not least <= value <= greatest:
        raise ValueError(f'{name} must be an integer in [{least}, {greatest}]')
    return value


def _rat(value, name):
    if type(value) not in (int, Q):
        raise ValueError(f'{name} must be an exact rational (not float/bool)')
    return Q(value)


def _unit(value):
    return _rat(value, 'circle coordinate') % 1


def dyadic_root(index:int, depth:int)->Q:
    """Finite dyadic roots are COUNTABLE over all depths; do not call continuum."""
    _int(index,'dyadic index',0)
    _int(depth,'dyadic depth',0,48)
    return Q(index % (1 << depth),1 << depth)


def circle_distance(x,y)->Q:
    d=abs(_unit(x)-_unit(y))
    return min(d,1-d)


def cut_coordinate(x, anchor=0)->Q:
    """Right-open oriented chart [0,1); not a continuous global inverse."""
    return (_unit(x)-_unit(anchor))%1


def cut_seam_receipt(depth:int)->dict:
    _int(depth,'depth',2,48)
    epsilon=Q(1,1 << depth)
    before,after=epsilon,1-epsilon
    return {'depth':depth,'near_zero':before,'near_one':after,
            'circle_distance':circle_distance(before,after),
            'flat_distance':abs(cut_coordinate(before)-cut_coordinate(after)),
            'same_circle_limit':True,'same_flat_limit':False}


def modadic(x, depth:int)->int:
    """Canonical rational-in-Z2 reduction mod 16^depth. Denominator must be odd."""
    _int(depth,'adic depth',1,10)
    x=_rat(x,'2-adic rational')
    if x.denominator % 2 == 0:
        raise ValueError('even denominator cannot be reduced in Z2')
    m=RADIX**depth
    return (x.numerator*pow(x.denominator,-1,m))%m


def canonical_forcing_odd(n:int)->Q:
    _int(n,'source time',1,10000000)
    x=authentic_r(n)
    if type(x) is not Q or x.denominator%2==0:
        raise ArithmeticError('changed four-pole source or non-odd forcing')
    return x


def source_forcing_polynomial(n:int)->Q:
    """Independent exact, fully canceled four-pole polynomial for crosschecks."""
    _int(n,'source time',1,10000000)
    return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def odd_inverse_circle(x, radix:int=RADIX)->Q:
    _int(radix,'radix',2,1<<20)
    x=_unit(x)
    if gcd(radix,x.denominator)!=1:
        raise ValueError('no uniquely typed inverse on this even-torsion source')
    if not x:
        return Q(0)
    return Q((x.numerator*pow(radix,-1,x.denominator))%x.denominator,x.denominator)


def odd_solenoid_levels(x, depth:int=4)->tuple[Q,...]:
    _int(depth,'history depth',0,10)
    x=_unit(x)
    if x.denominator%2==0:raise ValueError('odd-denominator section only')
    vals=[x]
    for _ in range(depth):vals.append(odd_inverse_circle(vals[-1]))
    for a,b in zip(vals,vals[1:]):
        if (RADIX*b)%1!=a:raise ArithmeticError('solenoid bond failed')
    return tuple(vals)


def torsion_memory_code(x,depth:int)->tuple[int,...]:
    """Cut-based Z16 coordinates: 16^k*x_{-k}-x_0 (mod 16^k)."""
    _int(depth,'history depth',1,10)
    levels=odd_solenoid_levels(x,depth)
    out=[]
    for k in range(1,depth+1):
        value=(RADIX**k)*levels[k]-levels[0]
        if value.denominator!=1:raise ArithmeticError('non-integral memory')
        out.append(int(value)%RADIX**k)
    if any(out[k]%(RADIX**k)!=out[k-1] for k in range(1,depth)):
        raise ArithmeticError('noncompatible 16-adic memory')
    return tuple(out)


def memory_gap_certificate(unwrapped,depth:int=4)->dict:
    """Difference between winding and unique odd-torsion lifts = U in Z2.

    In the chart (t,z), winding([U,0]) has z=floor(U), while torsion
    section at fractional U has z=-numerator/denominator in Z16.
    """
    u=_rat(unwrapped,'unwrapped state')
    if u.denominator%2==0:raise ValueError('odd source denominator required')
    x=u%1
    code=torsion_memory_code(x,depth)
    m=RADIX**depth
    winding=(u.numerator//u.denominator)%m
    torsion=code[-1]
    defect=(winding-torsion)%m
    if defect!=modadic(u,depth):raise ArithmeticError('real/2adic memory gap mismatch')
    return {'unwrapped':u,'circle_phase':x,'depth':depth,
            'winding_memory':winding,'odd_torsion_memory':torsion,
            'gap':defect,'canonical_two_adic_value':modadic(u,depth)}


def cofinal_2_to_16(binary_levels:tuple[Q,...])->tuple[Q,...]:
    if not isinstance(binary_levels,tuple) or not binary_levels or (len(binary_levels)-1)%4:
        raise ValueError('2-adic history length must equal 4k+1')
    x=tuple(_unit(a) for a in binary_levels)
    if any((2*x[j+1])%1!=x[j] for j in range(len(x)-1)):
        raise ValueError('not a dyadic inverse-history')
    return x[::4]


def cofinal_16_to_2(hex_levels:tuple[Q,...])->tuple[Q,...]:
    if not isinstance(hex_levels,tuple) or not hex_levels:
        raise ValueError('nonempty 16-adic inverse-history required')
    a=tuple(_unit(v) for v in hex_levels)
    if any((RADIX*a[i+1])%1!=a[i] for i in range(len(a)-1)):
        raise ValueError('not a 16-adic inverse-history')
    out=[a[0]]
    for b in a[1:]:
        out.extend([(8*b)%1,(4*b)%1,(2*b)%1,b])
    if any((2*out[i+1])%1!=out[i] for i in range(len(out)-1)):
        raise ArithmeticError('failed cofinal dyadic reconstitution')
    return tuple(out)


def seam_memory_glue(z:int,depth:int)->int:
    """(t=1,z) is identified with (t=0,z+1) on the solenoid chart."""
    _int(depth,'depth',1,10)
    _int(z,'memory value',0)
    return (z+1)%(RADIX**depth)


@dataclass(frozen=True)
class CutStep:
    time:int
    anchor:Q
    x:Q
    y:Q
    forcing:Q
    cut_x:Q
    cut_y:Q
    original_carry:int
    cut_carry:int
    seam_x:int
    seam_y:int
    phase_before:Q
    phase_recovered:Q


def cut_step(x,forcing,anchor=0,time:int=0,h:int=1)->CutStep:
    _int(time,'source index',0)
    _int(h if h>=0 else -h,'abs Fourier mode',0,100000000)
    x=_unit(x);r=_rat(forcing,'forcing');a=_unit(anchor)
    y=(RADIX*x+r)%1
    sx,sy=cut_coordinate(x,a),cut_coordinate(y,a)
    d0=0 if x>=a else -1
    d1=0 if y>=a else -1
    carry0=(RADIX*x+r).__floor__()
    shifted=r+15*a
    carrycut=(RADIX*sx+shifted).__floor__()
    if carrycut!=carry0+d1-RADIX*d0:
        raise ArithmeticError('seam cocycle is not source-covariant')
    if (RADIX*sx+shifted-carrycut)!=sy:
        raise ArithmeticError('cut chart dynamics are not exact')
    before=(h*x)%1
    recovered=(h*(a+Q(carrycut+sy-shifted,RADIX)))%1
    if before!=recovered:
        raise ArithmeticError('complex character lost through cut')
    return CutStep(time,a,x,y,r,sx,sy,carry0,carrycut,d0,d1,before,recovered)


def authentic_cut_history(length:int,anchor=0,h:int=1)->tuple[CutStep,...]:
    _int(length,'source prefix',1,5000)
    _int(h if h>=0 else -h,'abs Fourier mode',0,100000000)
    x=Q(0);seq=[]
    for n in range(1,length+1):
        r=canonical_forcing_odd(n)
        step=cut_step(x,r,anchor,n,h)
        seq.append(step);x=step.y
    return tuple(seq)


def seam_coboundary_telescope(steps:tuple[CutStep,...])->dict:
    if not steps:raise ValueError('nonempty source history required')
    if any(steps[k].y!=steps[k+1].x for k in range(len(steps)-1)):
        raise ValueError('disconnected source histories')
    N=len(steps)
    sum_diff=sum(RADIX**(N-1-j)*(s.cut_carry-s.original_carry)
                 for j,s in enumerate(steps))
    boundary=steps[-1].seam_y-RADIX**N*steps[0].seam_x
    if sum_diff!=boundary:raise ArithmeticError('seam gauge not a coboundary')
    return {'length':N,'weighted_carry_change':sum_diff,
            'two_endpoint_boundary':boundary,'ordinary_new_inequality':False}


def source_unwrapped_states(length:int)->tuple[Q,...]:
    _int(length,'state prefix',0,2000)
    out=[Q(0)]
    for n in range(1,length+1):out.append(RADIX*out[-1]+canonical_forcing_odd(n))
    return tuple(out)


def two_adic_isometry_mod(a:int,b:int,depth:int=3)->bool:
    """Proved isometry statement: r(a)-r(b) has same 2-adic valuation as a-b."""
    _int(depth,'precision',1,10)
    _int(a if a>=0 else -a,'first |index|',0)
    _int(b if b>=0 else -b,'second |index|',0)
    m=RADIX**depth
    def extended(x):
        return Q(120*x*x-89*x+16,(2*x-1)*(4*x-1)*(8*x-7)*(8*x-3))
    diff=extended(a)-extended(b)
    if diff.denominator%2==0:raise ArithmeticError('unexpected even denominator')
    if diff==0:return a==b
    def v2(n):
        n=abs(n)
        return (n&-n).bit_length()-1
    return v2(diff.numerator)==v2(a-b)


def time_clock_value(n:int,depth:int=1)->int:
    """F_k(n) = sum_(s<k)16^s r(n-s) mod 16^k; n may be >= k."""
    _int(depth,'hex resolution',1,8)
    _int(n,'time index',depth,10_000_000)
    m=RADIX**depth
    return sum((RADIX**s*modadic(source_forcing_polynomial(n-s),depth)
                for s in range(depth)))%m


def time_clock_certificate(depth:int=1)->dict:
    """Finite enumeration is evidence; paper theorem proves permutation for ALL k."""
    _int(depth,'hex resolution',1,4)
    m=RADIX**depth
    visited={time_clock_value(depth+i,depth) for i in range(m)}
    if len(visited)!=m:raise ArithmeticError('time-clock isometry failed')
    return {'depth':depth,'modulus':m,'distinct_count':len(visited),
            'period':m,'finite_permutation':True,'real_circle_normality_proved':False}


def rational_odd_grid(m:int)->tuple[tuple[Q,...],tuple[Q,...]]:
    """Example circle-Haar grids with non-Haar unique odd-torsion inverse lifts."""
    _int(m,'odd grid depth',1,500000)
    q=RADIX*m+1
    xs=tuple(Q(RADIX*j,q) for j in range(m))
    inv=tuple(Q(j,q) for j in range(m))
    if any(odd_inverse_circle(x)!=y for x,y in zip(xs,inv)):
        raise ArithmeticError('odd-torsion inverse controlled-grid failure')
    return xs,inv


def nonhaar_grid_witness(m:int)->dict:
    """Exact rational lower bound on Re E exp(2 pi i x_inverse) >0.

    x_inverse ∈ [0,1/16].  cos(t) >= 1-t^2/2, pi <22/7;
    hence >= 1 - (2*pi/16)^2/2 > 1 - (22/7)^2/128.
    Ordinary fixed integer circle characters have O_h(1/m) bounds,
    not a uniform in h theorem.
    """
    _int(m,'odd grid depth',1,500000)
    xs,inv=rational_odd_grid(m)
    l=Q(1)-Q(22*22,7*7*128)
    if not Q(0)<l<1:raise ArithmeticError('incorrect cosine certificate')
    return {'depth':m,'odd_conductor':RADIX*m+1,
            'max_inverse_coord':max(inv),
            'fractional_character_real_lower':l,
            'circle_fixed_h_upper_factor':Q(44,7)*(Q(1,2*m)+Q(1,RADIX*m+1)),
            'normality_of_pi_proved':False}


def finite_status():
    return {'cut_is_borel_not_global_continuous':True,
            'solenoid_seam_odometer_is_exact':True,
            'source_two_adic_time_haar':True,
            'selected_real_circle_fourier_cancellation_proved':False,
            'pi_base16_normality_proved':False,
            'RH_proved':False}


def two_adic_character_prefix_upper(horizon:int,depth:int,frequency:int)->Q:
    """EXACT proved |mean nontrivial additive 16^k-adic character| upper.

    U_n mod 16^k permutes all residues in every 16^k-term time block
    starting n>=k. Complete blocks cancel; the early k-1 and incomplete
    late block are paid at unit magnitude. A bound, not a sampled statistic.
    """
    _int(horizon,'horizon',1,10_000_000)
    _int(depth,'modular depth',1,8)
    _int(abs(frequency),'absolute frequency',0)
    m=RADIX**depth
    if frequency %m==0:
        raise ValueError('nontrivial frequency mod 16^k required')
    early=min(horizon,depth-1)
    late=horizon-early
    return min(Q(1),Q(early+late%m,horizon))


def decoy_tail(n:int)->Q:
    """ZERO-SEED NONNORMAL CONTROL: decoy BBP-like positive odd tail.

    D=(2n+1)(4n+1)(8n+1), T_n=(n+1)/D, T0=1.
    The resulting forcing has the original 15/(64n^2) leading term,
    is 2-adically isometric, but the real circle orbit clusters at zero.
    """
    _int(n,'decoy time',0,10_000_000)
    return Q(n+1,(2*n+1)*(4*n+1)*(8*n+1))


def decoy_forcing(n:int)->Q:
    _int(n,'decoy forcing index',1,10_000_000)
    return 16*decoy_tail(n-1)-decoy_tail(n)


def decoy_modular_time_clock(n:int,depth:int)->int:
    _int(depth,'decoy clock depth',1,8)
    _int(n,'decoy time',depth,10_000_000)
    m=16**depth
    return sum((16**s*modadic(decoy_forcing(n-s),depth) for s in range(depth)))%m


def decoy_source_control(depth:int=2)->dict:
    """Finite witness; paper proof yields all-level 2-adic uniformity
    and maximal fixed-real-mode noncancellation for this different source.
    """
    _int(depth,'decoy certificate depth',1,3)
    m=16**depth
    residues=[decoy_modular_time_clock(n,depth) for n in range(depth,depth+m)]
    if len(set(residues))!=m:raise ArithmeticError('decoy isometric clock mismatch')
    if decoy_forcing(1)==canonical_forcing_odd(1):
        raise ArithmeticError('control source not distinct')
    return {'zero_initial_state':True,
            'first_forcing':decoy_forcing(1),
            'authentic_first_forcing':canonical_forcing_odd(1),
            'same_forcing_leading_coefficient':'15/64',
            'strictly_positive_forcing_for_all_n':True,
            'two_adic_isometry_for_all_k':True,
            'depth':depth,'checked_permutation_size':m,
            'real_fourier_average_limit':1,
            'is_original_source':False,
            'pi_normality_from_isometry_proved':False}


def cut_midpoint_character_certificate(step:CutStep,frequency:int,bins:int)->dict:
    """Exact phase comparison, with rational upper using pi<22/7.

    The complete original forcing and selected marked-circle carry stay in
    the midpoint phase; no finite Fourier decay is asserted.
    """
    if not isinstance(step,CutStep):raise ValueError('source cut-step required')
    _int(abs(frequency),'frequency magnitude',0,100000000)
    _int(bins,'number of bins',1,1000000)
    cell=int(bins*step.cut_y)
    midpoint=Q(2*cell+1,2*bins)
    r_a=step.forcing+15*step.anchor
    midpoint_phase=(frequency*(step.anchor+Q(step.cut_carry+midpoint-r_a,RADIX)))%1
    true_phase=(frequency*step.x)%1
    unwrapped_dist=Q(abs(frequency),RADIX)*abs(step.cut_y-midpoint)
    circle_gap=circle_distance(midpoint_phase,true_phase)
    if circle_gap>unwrapped_dist or unwrapped_dist>Q(abs(frequency),2*RADIX*bins):
        raise ArithmeticError('signed cut-midpoint phase transport failed')
    return {'time':step.time,'anchor':step.anchor,'frequency':frequency,
            'bins':bins,'cell':cell,'exact_phase':true_phase,
            'midpoint_phase':midpoint_phase,'phase_circle_distance':circle_gap,
            'maximum_character_chord_distance_upper':Q(22*abs(frequency),7*RADIX*bins),
            'selected_signed_saving_proved':False}
