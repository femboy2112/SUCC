"""Integer Fibonacci probe clocks with exact Q(sqrt5) labels.

Source states and Fourier rectangles are inherited from the authenticated
source instrument. No floating point determines a phase cell.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import cmp_to_key
from hashlib import sha256
from math import isqrt
from pathlib import Path
import argparse
import json
import random
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(HERE.parent))
from source_probe import (Box,Interval,SCALE,ZERO,ONE,phase,mean,pi_box,
                         select,common_history,direct_modular_residue,
                         principal_pair,matched_seed,circular_discrepancy,sinc_squared)


def sign_surd(a,b):
    """Sign of a+b*sqrt(5), for exact rational a,b."""
    if a==0:return (b>0)-(b<0)
    if b==0:return (a>0)-(a<0)
    if a>0 and b>0:return 1
    if a<0 and b<0:return -1
    d=a*a-5*b*b
    return ((d>0)-(d<0))*(1 if a>0 else -1)


@dataclass(frozen=True)
class Golden:
    a:Q=Q(0)
    b:Q=Q(0)
    def __add__(self,other):
        if not isinstance(other,Golden):other=Golden(Q(other))
        return Golden(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self):return Golden(-self.a,-self.b)
    def __sub__(self,other):return self+-as_golden(other)
    def __rsub__(self,other):return as_golden(other)+-self
    def __mul__(self,other):
        other=as_golden(other)
        return Golden(self.a*other.a+5*self.b*other.b,self.a*other.b+self.b*other.a)
    __rmul__=__mul__
    def __truediv__(self,n):return Golden(self.a/n,self.b/n)
    def __pow__(self,n):
        if type(n) is not int or n<0:raise ValueError('nonnegative integer exponent required')
        out=Golden(Q(1)); x=self
        while n:
            if n&1:out=out*x
            x=x*x;n//=2
        return out
    def sign(self):return sign_surd(self.a,self.b)
    def encode(self):return {'rational':str(self.a),'sqrt5_coefficient':str(self.b)}


def as_golden(x):return x if isinstance(x,Golden) else Golden(Q(x))
ALPHA=Golden(Q(-1,2),Q(1,2))


def fibonacci(k):
    if type(k) is not int or k<0:raise ValueError('nonnegative integer index required')
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a


def golden_floor(j):
    if type(j) is not int or j<0:raise ValueError('nonnegative integer tick required')
    return (isqrt(5*j*j)-j)//2


def clock_position(j):return j*ALPHA-golden_floor(j)


def exact_label(r,p,M,j):
    """floor(M*(r/p - {j alpha})) mod M, using integer comparisons."""
    if not (type(r)is int and type(p)is int and 0<=r<p and type(M)is int and M>0):
        raise ValueError('canonical residue and positive integer grid/cells required')
    v=golden_floor(j)
    a=2*M*r+M*p*(j+2*v);b=-M*p*j;d=2*p
    low,high=-M-1,M+1
    while high-low>1:
        mid=(low+high)//2
        if sign_surd(a-d*mid,b)>=0:low=mid
        else:high=mid
    return low%M


def golden_discrepancy(k):
    q=fibonacci(k)
    if q<1:raise ValueError('positive clock length required')
    points=sorted((clock_position(j) for j in range(q)),
                  key=cmp_to_key(lambda a,b:(a-b).sign()))
    low=high=Golden()
    for j,x in enumerate(points):
        left=Golden(Q(j,q))-x;right=Golden(Q(j+1,q))-x
        if (left-low).sign()<0:low=left
        if (right-high).sign()>0:high=right
    return high-low


def alpha_interval(bits=160):
    d=1<<bits;s=isqrt(5*d*d)
    return Q(s-d,2*d),Q(s+1-d,2*d)


def clock_bound(k):
    q=fibonacci(k);p=fibonacci(k-1)
    lo,hi=alpha_interval()
    tlo,thi=q*lo-p,q*hi-p
    magnitude=max(abs(tlo),abs(thi))
    return Q(1,q)+Q(q-1,q)*magnitude


def cell_product(a,b,labels,M):
    if not a or len(a)!=len(b) or len(a)!=len(labels) or type(M) is not int or M<1:
        raise ValueError('equal nonempty samples and positive cell count required')
    if any(type(label) is not int or not 0<=label<M for label in labels):
        raise ValueError('canonical cell labels required')
    counts=[0]*M; sa=[Box() for _ in range(M)];sb=[Box() for _ in range(M)]
    for x,y,label in zip(a,b,labels):
        counts[label]+=1;sa[label]=sa[label]+x;sb[label]=sb[label]+y
    return sum(( (sa[i]*sb[i]).divide(counts[i]) for i in range(M) if counts[i]),Box()).divide(len(a))


def source_probe(A):
    p,order=select(A);data=common_history(2*A-1,A)
    den=data['denominator'];residues=data['residues']
    for n in (A,A+A//2,2*A-1):assert residues[n-A]==direct_modular_residue(n,den)
    pairs=[principal_pair(r,den,p) for r in residues]
    assert all(d==p for _,d in pairs)
    local=[r for r,_ in pairs]; D=circular_discrepancy(local,p)
    primes=tuple(sorted({3,5,7,11,p}))
    seed,_,_=matched_seed(data,A,32,Q(1,2**20),primes)
    shift=seed.numerator*pow(16,A,seed.denominator)%seed.denominator
    shadow=[]
    for r in residues:
        shadow.append(r*seed.denominator+shift*den)
        shift=16*shift%seed.denominator
    shadow_den=den*seed.denominator
    assert all(principal_pair(r,shadow_den,p)==pair for r,pair in zip(shadow,pairs))
    indices=(7,10,13);sizes={fibonacci(k):k for k in indices};qmax=max(sizes)
    labels={M:[[exact_label(r,p,M,j) for r in local] for j in range(qmax)] for M in (4,16)}
    rows=[]
    for h in (1,3):
        a=[phase(h*r,p) for r in local]
        families=[('original_zero',[phase(h*r,den) for r in residues]),
                  ('matched_wrong_seed',[phase(h*r,shadow_den) for r in shadow]),
                  ('synthetic_conjugate',[Box(ONE)]*A)]
        for family,z in families:
            b=[v*x.conjugate() for v,x in zip(z,a)]; W=mean(z);marginal=mean(a)*mean(b)
            for M in (4,16):
                lam=sinc_squared(h,M);total=Box()
                for j in range(qmax):
                    total=total+cell_product(a,b,labels[M][j],M)
                    q=j+1
                    if q not in sizes:continue
                    k=sizes[q];F=total.divide(q); error=F-W*Box(lam)
                    budget=2*abs(h)*D+4*abs(h)*clock_bound(k)
                    bound=pi_box()*Interval.ratio(budget.numerator,budget.denominator)
                    assert error.norm_squared().hi<=bound.square().lo
                    rows.append({'family':family,'h':h,'M':M,'k':k,'q':q,
                                 'W':W.as_dict(),'finite_clock_response':F.as_dict(),
                                 'lambda':lam.as_list(),'calibration_error':error.as_dict(),
                                 'proved_bound':bound.as_list(),'certified_within_bound':True,
                                 'covariance':(W-marginal).as_dict(),
                                 'retained_covariance':(F-marginal).as_dict()})
    return {'A':A,'p':p,'order16':order,'scale':SCALE,'circular_discrepancy':str(D),
            'source':{key:data[key] for key in ('last','unwrapped_sha256','carry_sha256')},
            'independent_modular_checks':3,'source_data_overlap':'Parent origin probe uses the same epochs',
            'labels':'exact Q(sqrt5), independent integer sign comparisons',
            'matched_seed':{'numerator_hex':hex(seed.numerator),'denominator_hex':hex(seed.denominator),
                            'fixed_across_epochs':False,'matched_primes':list(primes)},'rows':rows}


def phase_at_interval(lo,hi):
    if lo>hi:raise ValueError('ordered rational phase interval required')
    z=phase(lo.numerator,lo.denominator)
    width=hi-lo
    radius=pi_box()*Interval.ratio(2*width.numerator,width.denominator)
    box=Interval(-radius.hi,radius.hi)
    return z+Box(box,box)


def frame_checks():
    rng=random.Random(609711);lo,hi=alpha_interval();rows=[]
    for k in (7,9,11):
        q=fibonacci(k)
        for H in (1,2,4):
            tau=pi_box()*Interval.ratio(2*H,q)
            if tau.hi>=SCALE:continue
            phases={m:[phase_at_interval(*sorted((m*j*lo,m*j*hi))) for j in range(q)]
                    for m in range(-H,H+1)}
            signals=[[(Q(int(m==H)),Q(0)) for m in range(-H,H+1)],
                     [(Q(1,2*H+1),Q(0)) for m in range(-H,H+1)],
                     [(Q(1 if m%2==0 else -1,5),Q(m,7)) for m in range(-H,H+1)],
                     [(Q(rng.randrange(-3,4),7),Q(rng.randrange(-3,4),11)) for _ in range(2*H+1)]]
            for index,coeffs in enumerate(signals):
                norm=sum((a*a+b*b for a,b in coeffs),Q())
                if not norm:continue
                boxes=[Box(Interval.ratio(a.numerator,a.denominator),Interval.ratio(b.numerator,b.denominator)) for a,b in coeffs]
                sampled=[sum((c*phases[m][j] for c,m in zip(boxes,range(-H,H+1))),Box()) for j in range(q)]
                energy=sum((z.norm_squared() for z in sampled),ZERO).divide(q)
                ni=Interval.ratio(norm.numerator,norm.denominator)
                lower=(ONE-tau).square()*ni;upper=(ONE+tau).square()*ni
                assert energy.lo>=lower.hi and energy.hi<=upper.lo
                rows.append({'k':k,'q':q,'H':H,'signal':index,'coefficient_norm_squared':str(norm),
                             'energy':energy.as_list(),'lower':lower.as_list(),'upper':upper.as_list(),
                             'certified':True})
    return rows


def run_oracle():
    returns=[];checks=0
    for k in range(2,21):
        q=fibonacci(k);p=fibonacci(k-1)
        exact=q*ALPHA-p;expected=((-1)**(k-1))*ALPHA**k
        assert exact==expected;assert (1-q*(ALPHA**k)).sign()>0
        D=golden_discrepancy(k)
        upper=Golden(Q(1,q))+Q(q-1,q)*(ALPHA**k)
        assert (upper-D).sign()>=0
        returns.append({'k':k,'q':q,'return':exact.encode(),'discrepancy':D.encode(),'bound':upper.encode()})
        checks+=3
    # A differently computed rational bracket certifies all labels.
    alo,ahi=alpha_interval()
    labels_checked=0
    for p in (7,19,41):
        for M in (1,4,16):
            for j in (0,1,2,7,54,232):
                flo=(j*alo).__floor__();fhi=(j*ahi).__floor__();assert flo==fhi
                for r in range(p):
                    low=M*(Q(r,p)-j*ahi+flo);high=M*(Q(r,p)-j*alo+flo)
                    if low.__floor__()!=high.__floor__():
                        assert j==0 # exact rational boundary handled directly
                        expected=(M*Q(r,p)).__floor__()%M
                    else:expected=low.__floor__()%M
                    assert exact_label(r,p,M,j)==expected;labels_checked+=1
    A={0,1,4,6};B={0,1,3,7}
    def differences(S):
        out=[0]*12
        for x in S:
            for y in S:out[(x-y)%12]+=1
        return out
    assert differences(A)==differences(B)
    assert all({(s*x+t)%12 for x in A}!=B for s in (-1,1) for t in range(12))
    frames=frame_checks()
    return {'status':'PASS','code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'exact_return_and_discrepancy_checks':checks,'exact_label_checks':labels_checked,
            'returns':returns,'frame_certificate_count':len(frames),'frame_certificates':frames,
            'homometric':{'first':sorted(A),'second':sorted(B),'directed_difference_counts':differences(A),
                          'translation_or_reflection':False},
            'phase_gauge_control':'Independent shift -j alpha clusters all origins at0; discrepancy1',
            'scope':'Exact algebra and outward finite certificates; no source decay or Lean claim'}



def summarize(output):
    oracle=json.loads((output/'ORACLE.json').read_text())
    summary={'exact_return_discrepancy_checks':oracle['exact_return_and_discrepancy_checks'],
             'exact_partition_labels':oracle['exact_label_checks'],
             'frame_interval_certificates':oracle['frame_certificate_count'],
             'source_cases':0,'parent_W_matches':0,'examples':[]}
    for A in (149,673):
        path=output/f'SOURCE_{A}.json'
        if not path.exists():continue
        data=json.loads(path.read_text())
        parent=json.loads((HERE.parent/f'results/origin_{A}.json').read_text())
        lookup={(row['family'],row['h']):row['W'] for row in parent['rows']}
        summary['source_cases']+=len(data['rows'])
        for row in data['rows']:
            assert row['W']==lookup[row['family'],row['h']]
            summary['parent_W_matches']+=1
            if row['M']==16 and row['q']==233 and row['h']==1:
                def midpoint(z):
                    return [(z[t][0]+z[t][1])/(2*data['scale']) for t in ('re','im')]
                summary['examples'].append({'A':A,'family':row['family'],
                    'W_midpoint':midpoint(row['W']),
                    'F_midpoint':midpoint(row['finite_clock_response']),
                    'calibration_error_midpoint':midpoint(row['calibration_error'])})
    summary['authority']='Midpoints are descriptive only; source/frame JSON contains outward certificates. All source Weyl rectangles match the independently run parent origin instrument.'
    (output/'SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--source',action='store_true')
    args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    result=run_oracle()
    (args.output/'ORACLE.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('exact clock oracle and',result['frame_certificate_count'],'interval frame certificates pass',flush=True)
    if args.source:
        for A in (149,673):
            result=source_probe(A)
            (args.output/f'SOURCE_{A}.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
            print(A,len(result['rows']),'source clock certificates pass',flush=True)
    summarize(args.output)


if __name__=='__main__':main()
