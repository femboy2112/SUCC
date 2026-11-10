"""Exact model-law checks and outward original-source moment certificates.

Reuses the existing 80-bit phase instrument; separately evaluated pair sums
check folded energies. No source asymptotic is inferred from these windows.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt
from itertools import permutations
from pathlib import Path
import argparse
import json
import sys

from model import (ROOT, clock, exact_source_angles, law_defects, orbit,
                   order16, rigidity_hypotheses, transform)

sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(ROOT/'research/2026-11-08/covariance_forge'))
from intervals import Box, Interval, SCALE, ZERO, ONE, phase, mean, pi_box
from observational_succ.duck_bbp import forcing


def norm_box(z):
    norm=z.norm_squared()
    lo=isqrt(max(0,norm.lo)*SCALE)
    hi=isqrt(max(0,norm.hi)*SCALE)
    if hi*hi<max(0,norm.hi)*SCALE:hi+=1
    return Interval(lo,hi)


def scalar_mean(values):
    values=list(values)
    return sum(values,ZERO).divide(len(values))


def power(z,k):
    out=Box(ONE)
    while k:
        if k&1:out=out*z
        z=z*z;k//=2
    return out


def contains_zero(z):
    return z.re.lo<=0<=z.re.hi and z.im.lo<=0<=z.im.hi


def exact_models(counts):
    rows=[]
    state=772031
    for p in (41,73,137,281):
        m=order16(p)
        for D in (1,2,3):
            for K in (1,2,3):
                if K*D>=m:continue
                for case in range(12):
                    polys=[]
                    while len(polys)<K:
                        coeff=[]
                        for d in range(D+1):
                            state=(1664525*state+1013904223)%2**32
                            coeff.append(state%p)
                        if D>1:coeff[-1]=1+state%(p-1)
                        coeff=tuple(coeff)
                        if coeff not in polys:polys.append(coeff)
                    assert rigidity_hypotheses(polys,p)
                    weights=[Q(j+1,K*(K+1)//2) for j in range(K)]
                    defects=law_defects(polys,weights,p)
                    avg=sum(defects)/m
                    nonlinear=any(poly[0] or any(poly[d] for d in range(2,len(poly))) for poly in polys)
                    if nonlinear:
                        lower=min(weights)*(1-Q(K*D,m))
                        assert avg>=lower
                        counts['exact_TV_lower_bounds']+=1
                    if not avg:
                        assert not nonlinear
                        counts['exact_rigidity_survivors']+=1
                    counts['exact_model_transition_checks']+=m
                    rows.append({'p':p,'D':D,'K':K,'case':case,'mean_TV':str(avg),
                                 'nonlinear_or_offset':nonlinear})
        for d in (2,3):
            polys=orbit([0]*d+[1],p)
            weights=[Q(1,len(polys))]*len(polys)
            assert all(v==0 for v in law_defects(polys,weights,p))
            assert not rigidity_hypotheses(polys,p)
            counts['nonlinear_full_orbit_controls']+=1
    # Direct circle exponent histograms, independent of polynomial law helper.
    # Union of third and fifth roots: fixed under16, first sum zero by grouping.
    angles=[Q(j,3) for j in range(3)]+[Q(j,5) for j in range(5)]
    assert Counter(angles)==Counter((16*t)%1 for t in angles)
    z=mean(phase(t.numerator,t.denominator) for t in angles)
    assert contains_zero(z)
    counts['finite_law_zero_moment_controls']+=1
    # A two-atom first-moment zero is not moment16 zero.
    first=mean([phase(0),phase(1,2)])
    sixteenth=mean([phase(0),phase(16,2)])
    assert contains_zero(first) and sixteenth.re.lo>0
    counts['failed_first_moment_closure_controls']+=1
    return rows


def macroscopic_model_checks(counts):
    """Independent rational lower bounds on exact finite transport problems.

    No source history is built at this larger prime. Rational-angle chords
    satisfy |e(t)-1|>=4||t||. Enumerating the K! matchings computes the exact
    transportation cost for this rational lower-cost matrix, hence a rigorous
    lower bound on the true circle W1 cost. This is not the theorem formula.
    """
    p=1000249;m=order16(p);D=2
    xi=__import__('model').source_xi(p)
    sqrt_upper=isqrt(p)+1
    # Dyadic grouping proves H_N<=bit_length(N), avoiding a huge denominator.
    H_upper=((p-1)//2).bit_length()
    delta_upper=min(Q(1),Q(D*sqrt_upper,m))
    d_upper=Q(1,p)+delta_upper*H_upper
    rows=[]
    for K in (1,2,3):
        assert K*D<m
        a=max(Q(0),1-K*d_upper-Q(1,m))
        predicted=Q(1,K*K)*a*a
        assert predicted>0
        perms=list(permutations(range(K)))
        coefficients=[pow(16,j,p) for j in range(K)]
        for anchored in (False,True):
            N=7*p
            anchors=list(range(1,K+1)) if anchored else [0]*K
            total_min_cost=0
            witness_total_distance=0
            x=xi
            for r in range(m):
                x2=x*x%p
                nxt=[(anchors[i]*p+7*coefficients[i]*256*x2)%N for i in range(K)]
                pushed=[(16*anchors[j]*p+7*coefficients[j]*16*x2)%N for j in range(K)]
                cost=[]
                for u in nxt:
                    row=[]
                    for v in pushed:
                        distance=(u-v)%N
                        row.append(min(distance,N-distance))
                    cost.append(row)
                if r<m-1:
                    total_min_cost+=min(sum(cost[i][perm[i]] for i in range(K)) for perm in perms)
                    witness_total_distance+=min(cost[K-1])
                x=x*16%p
            assert x==xi
            actual_lower=Q(4*total_min_cost,N*K*m)
            witness_lower=Q(4*witness_total_distance,N*K*m)
            assert actual_lower>=predicted
            assert witness_lower>=predicted
            counts['nonvacuous_macroscopic_model_bounds']+=1
            counts['exact_small_transport_problems']+=m-1
            rows.append({'p':p,'m':m,'K':K,'D':D,'phase_anchors':'e((j+1)/7)' if anchored else 'all1',
                         'delta_rational_upper':str(delta_upper),'harmonic_sum_upper':H_upper,
                         'd_grid_upper':str(d_upper),'theorem_lower':str(predicted),
                         'exact_chord_lower_transport':str(actual_lower),
                         'independent_nearest_atom_lower':str(witness_lower),
                         'source_history_constructed':False})
    return rows


def source_rows(counts):
    rows=[];sources=[]
    for p in (577,1201,2689,4201):
        data=exact_source_angles(p)
        m,L,q,n0=data['m'],data['L'],data['q'],data['n0']
        angles=data['angles']
        counts['exact_source_cocycle_checks']+=L-1
        counts['source_principal_part_checks']+=L
        counts['independent_direct_source_sums']+=3
        exact_force_sum=sum((forcing(n+1) for n in range(n0,2*L)),Q())
        for h in (1,3):
            b=[phase((h*t).numerator,(h*t).denominator) for t in angles]
            b16=[phase((16*h*t).numerator,(16*h*t).denominator) for t in angles]
            B=[mean(b[r+j*m] for j in range(q)) for r in range(m)]
            B16=[mean(b16[r+j*m] for j in range(q)) for r in range(m)]
            defect=scalar_mean(norm_box(B[(r+1)%m]-B16[r]) for r in range(m))
            forcing_cost=pi_box()*Interval.ratio(2*abs(h)*exact_force_sum.numerator,L*exact_force_sum.denominator)
            bound=forcing_cost+Interval.ratio(2,L)
            assert defect.hi<=bound.lo
            counts['outward_moment_transport_bounds']+=1
            # Independent pair-difference summation checks replica energy.
            pair=Box()
            for r in range(m):
                for j in range(q):
                    for k in range(q):
                        t=h*(angles[r+j*m]-angles[r+k*m])
                        pair=pair+phase(t.numerator,t.denominator)
            pair=pair.divide(m*q*q)
            energy=scalar_mean(z.norm_squared() for z in B)
            assert energy.overlaps(pair.re) and pair.im.lo<=0<=pair.im.hi
            counts['independent_pair_energy_equalities']+=1
            variance=ONE-energy
            closure=scalar_mean(norm_box(B[(r+1)%m]-power(B[r],16)) for r in range(m))
            closure_bound=bound+variance*Interval.ratio(120)
            assert closure.hi<=closure_bound.lo
            counts['outward_variance_closure_bounds']+=1
            # Full Weyl phase = local times complementary phase; compare direct.
            folded=mean(phase(h*data['support'][r],p)*B[r] for r in range(m))
            direct=mean(phase(h*t,data['denominator']) for t in data['residues'])
            assert contains_zero(folded-direct)
            counts['direct_vs_folded_Weyl_equalities']+=1
            # Exact raw/folded squared-error identity with the periodic model1.
            raw_error=scalar_mean((z-Box(ONE)).norm_squared() for z in b)
            predicted=variance+scalar_mean((z-Box(ONE)).norm_squared() for z in B)
            assert raw_error.overlaps(predicted)
            counts['outward_replica_variance_equalities']+=1
            rows.append({'p':p,'m':m,'L':L,'q':q,'h':h,
                         'moment_transport_error':defect.as_list(),
                         'moment_transport_bound':bound.as_list(),
                         'forcing_cost':forcing_cost.as_list(),
                         'replica_energy':energy.as_list(),
                         'independent_pair_energy':pair.as_dict(),
                         'replica_variance':variance.as_list(),
                         'folded_zero_model_L1':scalar_mean(norm_box(z) for z in B).as_list(),
                         'nonlinear_first_moment_closure_error':closure.as_list(),
                         'variance_closure_bound':closure_bound.as_list(),
                         'Weyl':direct.as_dict(),
                         'raw_squared_error_model_one':raw_error.as_list(),
                         'variance_plus_folded_squared_error':predicted.as_list()})
        sources.append({key:data[key] for key in ('p','m','L','q','n0','unwrapped_sha256','carry_sha256')})
    return rows,sources


def run():
    counts=Counter()
    model_rows=exact_models(counts)
    macroscopic_rows=macroscopic_model_checks(counts)
    rows,sources=source_rows(counts)
    return {'status':'exact finite model algebra and outward source moment certificates',
            'counts':dict(counts),'scale':SCALE,'model_rows':model_rows,'macroscopic_model_rows':macroscopic_rows,'source_rows':rows,
            'sources':sources,'source_contract':'literal U0=0, four signed BBP poles, chronological unwrapped/carry hashes',
            'data_scope':'fixed regression windows; not new independent holdouts',
            'dependencies':{str(path.relative_to(ROOT)):sha256(path.read_bytes()).hexdigest()
                            for path in (ROOT/'observational_succ/duck_bbp.py',
                                         ROOT/'research/2026-11-08/covariance_forge/source.py',
                                         ROOT/'research/2026-11-08/covariance_forge/intervals.py',
                                         ROOT/'research/2026-11-08/signal_frontier/prime_resonance/pr_resonance.py',
                                         Path(__file__).with_name('model.py'))},
            'pi_base16_normality':'OPEN','RH':'OPEN'}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=run()
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'counts':result['counts'],'source_windows':len(result['sources']),
                      'output':str(args.output)},sort_keys=True))
