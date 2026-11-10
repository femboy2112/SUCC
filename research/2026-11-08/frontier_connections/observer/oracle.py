"""Source-exact and interval checks of equal-weight observer closure.

This is an independent reduced-Fraction source construction, with a separate
unwrapped recurrence and literal carry hash. Phase boxes reuse the dossier's
existing proved interval primitive. Historical windows are NOT fresh data.
"""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import argparse
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(ROOT/'research/2026-11-08/covariance_forge'))
sys.path.insert(0,str(ROOT/'research/2026-11-08/signal_frontier/prime_resonance'))
from intervals import Box,Interval,ONE,ZERO,SCALE,mean,phase,pi_box,ceildiv
from pr_resonance import order16,source_xi
from observational_succ.selected_orbit import SelectedOrbit,four_pole_forcing
from observational_succ.duck_bbp import forcing
from moment_memory import forcing_difference_bound


def phase_q(t):
    return phase(t.numerator,t.denominator)


def divide_interval(a,b):
    if b.lo<=0:raise ValueError('positive denominator enclosure required')
    corners=[Q(x*SCALE,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
    lo,hi=min(corners),max(corners)
    return Interval(lo.numerator//lo.denominator,ceildiv(hi.numerator,hi.denominator))


def divide_box(a,b):
    return Box(divide_interval(a.re,b),divide_interval(a.im,b))


def pair_closure(s,k):
    product=divide_box(s*s,s.norm_squared())
    if k==0:return Box(ONE)
    previous,current=Box(ONE),s
    two=Box(Interval.ratio(2))
    for _ in range(2,k+1):
        previous,current=current,two*s*current-product*previous
    return current


def power(z,k):
    answer=Box(ONE)
    while k:
        if k&1:answer=answer*z
        z=z*z;k//=2
    return answer


def overlap(a,b):
    return a.re.overlaps(b.re) and a.im.overlaps(b.im)


def hash_fraction(digest,value):
    digest.update((hex(value.numerator)+'/'+hex(value.denominator)+'\n').encode())


def source_case(p,h,counts):
    L=(p-1)//4;m=order16(p);n0=L+1
    assert L==2*m
    xi=source_xi(p)
    orbit=SelectedOrbit()
    U=Q(0);phase_state=Q(0);integer=0
    history=sha256();carries=sha256();angles=[]
    for n in range(1,2*L+1):
        assert forcing(n)==four_pole_forcing(n)
        U=16*U+forcing(n)
        assert U.denominator%2
        next_phase=16*phase_state+forcing(n)
        carry=next_phase.numerator//next_phase.denominator
        phase_state=next_phase-carry
        integer=16*integer+carry
        assert U==integer+phase_state and phase_state==orbit.state(n)
        hash_fraction(history,U);carries.update((str(carry)+'\n').encode())
        counts['exact_unwrapped_recurrence_and_carry_checks']+=1
        if n>=n0:
            x=xi*pow(16,n-n0,p)%p
            # Independent canonical p-primary projection from the reduced fraction.
            v=phase_state.denominator
            assert v%p==0 and v%(p*p)!=0
            cofactor=v//p
            actual_x=phase_state.numerator*pow(cofactor,-1,p)%p
            assert actual_x==x
            t=(phase_state-Q(x,p))%1
            assert t.denominator%2
            angles.append((h*t)%1)
            counts['actual_principal_parts']+=1
    rows=[];smallest=None;max_radius_upper=Q(0);max_denominator_bits=0
    for r in range(m):
        t1,t2=angles[r],angles[r+m]
        delta=(t2-t1)%1
        assert delta.denominator%2 and delta!=Q(1,2)
        distance=abs(delta-Q(1,2))
        assert distance>=Q(1,2*delta.denominator)
        max_denominator_bits=max(max_denominator_bits,delta.denominator.bit_length())
        z,w=phase_q(t1),phase_q(t2)
        s=mean([z,w])
        assert s.norm_squared().lo>0
        lower=Q(s.norm_squared().lo,SCALE)
        smallest=lower if smallest is None else min(smallest,lower)
        exact_sixteenth=mean([phase_q(16*t1),phase_q(16*t2)])
        decoded=pair_closure(s,16)
        assert overlap(exact_sixteenth,decoded)
        counts['nonzero_first_moment_closures']+=1
        counts['odd_denominator_antipodal_exclusions']+=1
        if r==m-1:continue
        n=n0+r;f,g=forcing(n+1),forcing(n+m+1)
        assert (angles[r+1]-16*t1-h*f)%1==0
        assert (angles[r+m+1]-16*t2-h*g)%1==0
        ff,fg=phase_q(h*f),phase_q(h*g)
        zp,wp=power(z,16),power(w,16)
        yplus=mean([zp*ff,wp*fg]);yminus=mean([wp*ff,zp*fg])
        actual=mean([phase_q(angles[r+1]),phase_q(angles[r+m+1])])
        assert overlap(yplus,actual)
        center=mean([yplus,yminus])
        radius2=(yplus-yminus).norm_squared().divide(4)
        # Separate factorized formula and exact rational source bound.
        factorized=(zp-wp).norm_squared()*(ff-fg).norm_squared()
        factorized=factorized.divide(16)
        assert radius2.overlaps(factorized)
        assert (actual-center).norm_squared().overlaps(radius2)
        delta_forcing=abs(f-g)
        cap=forcing_difference_bound(n+1,m)
        assert delta_forcing<=cap
        upper=Q(pi_box().hi,SCALE)*abs(h)*cap
        assert Q(radius2.hi,SCALE)<=upper*upper
        max_radius_upper=max(max_radius_upper,Q(radius2.hi,SCALE))
        counts['source_chronology_radius_certificates']+=1
        counts['exact_individual_phase_cocycles']+=2
    return {'p':p,'h':h,'m':m,'q':2,'n0':n0,'last':2*L,
            'minimum_folded_modulus_squared_lower':str(smallest),
            'maximum_chronology_radius_squared_upper':str(max_radius_upper),
            'maximum_difference_denominator_bits':max_denominator_bits,
            'unwrapped_sha256':history.hexdigest(),'carry_sha256':carries.hexdigest()}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=HERE/'RECEIPT.json')
    args=parser.parse_args()
    counts={name:0 for name in ('exact_unwrapped_recurrence_and_carry_checks',
            'actual_principal_parts','nonzero_first_moment_closures',
            'odd_denominator_antipodal_exclusions','source_chronology_radius_certificates',
            'exact_individual_phase_cocycles','exact_forcing_difference_bounds')}
    for n in range(1,101):
        for m in (1,2,3,7,16,31):
            assert 0<forcing(n)-forcing(n+m)<=forcing_difference_bound(n,m)
            counts['exact_forcing_difference_bounds']+=1
    rows=[source_case(p,h,counts) for p in (41,73,137,281) for h in (1,3,5)]
    dependencies=[HERE/'moment_memory.py',HERE/'THEOREMS.md',HERE/'oracle.py',
                  ROOT/'observational_succ/selected_orbit.py',ROOT/'observational_succ/duck_bbp.py',
                  ROOT/'research/2026-11-08/covariance_forge/intervals.py',
                  ROOT/'research/2026-11-08/signal_frontier/prime_resonance/pr_resonance.py']
    payload={'status':'CERTIFIED-FINITE','pi_normality':'OPEN','RH':'OPEN',
             'baseline':'525d7c87dd1016aeeea4ac9cd1366cbb935a0441',
             'data_scope':'historical finite windows; no fresh-data or asymptotic claim',
             'counts':counts,'source_cases':rows,
             'dependencies':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in dependencies}}
    args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'counts':counts,'source_cases':len(rows),'output':str(args.output)},sort_keys=True))


if __name__=='__main__':main()
