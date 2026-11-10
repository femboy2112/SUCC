"""Independent exact lifting/source checks and numerical bound corroboration."""
import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import sys

from pr_resonance import classify, clock, eligible, evaluate, order16, select_prime, source_xi

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT))


def long_division(coefficients,p,m,c):
    """Independent monic polynomial division, not exponent-block reduction."""
    out=[x%p for x in coefficients]
    while len(out)>m:
        v=out.pop()
        out[len(out)-m]=(out[len(out)-m]+v*c)%p
    while len(out)>1 and out[-1]==0:out.pop()
    return out


def walk_order(p):
    x=16%p;m=1
    while x!=1:x=x*16%p;m+=1
    return m


def source_checks(counts):
    sys.path.insert(0,str(ROOT/'research/2026-11-08/covariance_forge'))
    from source import common_history,direct_modular_residue,principal_pair
    primes=(4201,4217,4337)
    last=max((p-1)//2 for p in primes)
    data=common_history(last,0)
    for p in primes:
        L=(p-1)//4;xi=source_xi(p)
        for n in range(L+1,2*L+1):
            a,d=principal_pair(data['residues'][n],data['denominator'],p)
            assert Q(a,d)==Q(xi*pow(16,n-L-1,p)%p,p)
            counts['source_principal_part_checks']+=1
        for n in (L+1,2*L):
            assert direct_modular_residue(n,data['denominator'])==data['residues'][n]
            counts['independent_direct_source_sums']+=1
    return {'primes':list(primes),'last':last,'unwrapped_sha256':data['unwrapped_sha256'],
            'carry_sha256':data['carry_sha256'],
            'builder_sha256':sha256((ROOT/'research/2026-11-08/covariance_forge/source.py').read_bytes()).hexdigest(),
            'scope':'shared exact common-denominator builder; separate direct modular sums and new clock formula'}


def run():
    import mpmath as mp
    mp.mp.dps=80
    counts=Counter()
    rows=[]
    for p in (17,41,73,137,281):
        m=order16(p);q=(p-1)//m
        assert m==walk_order(p)
        for xi in (1,3):
            support=clock(p,xi);c=pow(xi,m,p)
            for h in (1,3):
                for D in range(0,min(6,m)):
                    # Fixed deterministic coefficient construction, no fitting.
                    P=[(11*j*j+7*j+3)%p for j in range(D+1)]
                    if D==0:P=[3]
                    # Guarantee degree D for D>=2, retaining linear exception control.
                    if D>=2:P[-1]=1
                    combined=P+[0]*max(0,2-len(P));combined[1]+=h
                    result=classify(P,p,xi,h)
                    remainder=result['remainder']
                    assert remainder==long_division(combined,p,m,c)
                    counts['independent_polynomial_divisions']+=1
                    for x in support:
                        assert evaluate(combined,x,p)==evaluate(remainder,x,p)
                        counts['quotient_evaluation_checks']+=1
                    hist=Counter(evaluate(remainder,x,p) for x in support)
                    full=Counter(evaluate(remainder,xi*pow(t,q,p)%p,p) for t in range(p))
                    expected=Counter({key:q*v for key,v in hist.items()})
                    expected[evaluate(remainder,0,p)]+=1
                    assert full==expected
                    counts['exact_power_lifting_histograms']+=1
                    val=sum((v*mp.exp(2j*mp.pi*k/p) for k,v in hist.items()),mp.mpc(0))/m
                    actualD=result['degree']
                    bound=mp.mpf(1) if actualD==0 else min(mp.mpf(1),actualD*mp.sqrt(p)/m)
                    assert abs(val)<=bound+mp.mpf('1e-70')
                    counts['numerical_weil_corroborations']+=1
                    rows.append({'p':p,'xi':xi,'h':h,'input_degree':D,'reduced_degree':actualD,
                                 'abs_mean':mp.nstr(abs(val),25),'upper_bound':mp.nstr(bound,25),
                                 'scope':'80-digit corroboration; not an interval or proof'})
                for c0 in (0,1,p-1):
                    P=[c0-c,-h]+[0]*(m-2)+[1]
                    result=classify(P,p,xi,h)
                    assert result['resonant'] and result['constant_phase_numerator']==c0
                    assert {(h*x+evaluate(P,x,p))%p for x in support}=={c0}
                    counts['hidden_alias_controls']+=1
            # Formal mixtures retain two opposed resonant atoms, cancelling them
            # before charging one nonresonant atom. Integer root coefficients exact.
            h=1
            atoms=([2,-h],[2,-h],[0,0,1])
            weights=(1,-1,1)
            direct=Counter()
            retained=Counter();nonres=Counter()
            for P,w in zip(atoms,weights):
                result=classify(P,p,xi,h)
                for x in support:direct[(h*x+evaluate(P,x,p))%p]+=w
                target=retained if result['resonant'] else nonres
                if result['resonant']:target[result['constant_phase_numerator']]+=w*m
                else:
                    for x in support:target[evaluate(result['remainder'],x,p)]+=w
            assert all(direct[k]==retained[k]+nonres[k] for k in range(p))
            assert all(v==0 for v in retained.values())
            counts['signed_mixture_identities']+=1
    # Larger authenticated source cosets make every degree2/3/5 test nontrivial.
    for p in (4201,4217,4337):
        m=order16(p);xi=source_xi(p);q=(p-1)//m;support=clock(p,xi)
        for h in (1,3):
            for D in (2,3,5):
                P=[0,-h]+[0]*(D-2)+[1]
                result=classify(P,p,xi,h)
                assert result['degree']==D and D*D*p<m*m
                remainder=result['remainder']
                hist=Counter(evaluate(remainder,x,p) for x in support)
                full=Counter(evaluate(remainder,xi*pow(t,q,p)%p,p) for t in range(p))
                expected=Counter({key:q*v for key,v in hist.items()})
                expected[evaluate(remainder,0,p)]+=1
                assert full==expected
                counts['exact_source_coset_power_lifting_histograms']+=1
                val=sum((v*mp.exp(2j*mp.pi*k/p) for k,v in hist.items()),mp.mpc(0))/m
                bound=D*mp.sqrt(p)/m
                assert abs(val)<=bound+mp.mpf('1e-70')
                counts['nonvacuous_source_weil_corroborations']+=1
                rows.append({'p':p,'xi':xi,'h':h,'input_degree':D,'reduced_degree':D,
                             'abs_mean':mp.nstr(abs(val),25),'upper_bound':mp.nstr(bound,25),
                             'scope':'80-digit nonvacuous source-coset corroboration; not an interval or proof'})
    selections=[]
    for A in (137,1050,1051,1201,1601,2203,3001):
        p=select_prime(A)
        # Slow independent primality and order enumeration.
        candidates=[]
        for q in range(17,4*A+1,8):
            if all(q%d for d in range(2,isqrt(q)+1)):
                m=walk_order(q)
                if m*m>q*4**isqrt(q.bit_length()):candidates.append(q)
                counts['independent_selector_candidates']+=1
        assert p==(max(candidates) if candidates else None)
        row={'A':A,'p':p,'split':'holdout' if A in (1601,2203,3001) else 'development'}
        if p:
            m=order16(p);L=(p-1)//4
            overlap=max(0,min(2*A,2*L+1)-max(A,L+1))
            eps=Q(2)-2*Q(overlap,max(A,L))
            assert eps<=Q(4*(A-L),A)
            row.update(m=m,L=L,k=isqrt(p.bit_length()),eps_exact=str(eps),
                       local_degree_one_squared_cap=str(min(Q(1),Q(p,m*m))))
        selections.append(row)
    source=source_checks(counts)
    imports=json.loads((HERE/'SOURCE_IMPORTS.json').read_text())
    return {'status':'exact finite algebra and source checks; numerical bounds separately scoped',
            'counts':dict(counts),'selections':selections,'source':source,'numerical_rows':rows,
            'imports_read':imports,'pi_base16_normality':'OPEN','RH':'OPEN'}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'counts':result['counts'],'output':str(args.output),'selections':result['selections']},sort_keys=True))
