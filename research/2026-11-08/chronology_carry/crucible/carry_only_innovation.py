"""Postregistration EI1 observer verification on the existing source holdout.

The preparation uses literal carries and source labels only. Actual unit
phases are accessed in a separate comparison command, after preparation.
All finite character arithmetic uses 70-digit mpmath intervals.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import gzip
import json

from independent_phase_check import endpoint_fraction, interval_record

DEPTHS=(1,2,3)
FREQUENCIES=(1,3)
DPS=70


def read_source(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),sha256(raw).hexdigest()


def counts_from_carries(carries,n0,last,depths=DEPTHS):
    if not 1<=n0<last or len(carries)!=last:
        raise ValueError('complete prefix and nonempty interior transitions required')
    if not depths or any(type(k) is not int or k not in DEPTHS for k in depths):
        raise ValueError('declared bounded depths1,2,3 required')
    if any(type(c) is not int or not 0<=c<=16 for c in carries):
        raise ValueError('original zero-source literal carries0..16 required')
    rows={k:{'k':k,'M':16**k,'current':Counter(),'arrival':Counter(),
             'joint':Counter(),'start':None,'end':None} for k in depths}
    states={k:0 for k in depths}
    for n,d in enumerate(carries,1):
        for k in depths:
            old=states[k]
            new=(16*old+d) % rows[k]['M']
            if n0+1<=n<=last:
                row=rows[k]
                row['current'][old]+=1
                row['arrival'][new]+=1
                row['joint'][(old,d)]+=1
            states[k]=new
            if n==n0:rows[k]['start']=new
            if n==last:rows[k]['end']=new
    for row in rows.values():
        assert sum(row['current'].values())==last-n0
        assert sum(row['arrival'].values())==last-n0
        assert sum(row['joint'].values())==last-n0
    return rows


def complex_record(z):
    return {'real':interval_record(z.real),'imag':interval_record(z.imag)}


def contains_zero(x):
    lo,hi=map(endpoint_fraction,x._mpi_)
    return lo<=0<=hi


def evaluate_counts(row,h,N):
    from mpmath.ctx_iv import MPIntervalContext
    if type(h) is not int or h==0 or h % row['M']==0 or N<=0:
        raise ValueError('nonzero nonresonant integer frequency and positive normalization required')
    iv=MPIntervalContext();iv.dps=DPS
    k,M=row['k'],row['M']
    cache={}
    def e(n,d=M):
        fraction=Q(n,d) % 1
        if fraction not in cache:
            angle=2*iv.pi*iv.mpf(fraction.numerator)/fraction.denominator
            cache[fraction]=iv.cos(angle)+iv.j*iv.sin(angle)
        return cache[fraction]
    def zero():return iv.mpc(0)
    A=[]
    for j in range(k+1):
        A.append(sum((e(h*(2*a+1),2*M) for a in range(16**j)),zero())/16**j)
    assert contains_zero(A[k].real) and contains_zero(A[k].imag)
    levels=[]
    total=zero()
    coefficient_checks=[]
    for j in range(k):
        arrival=sum((count*e(h*16**j*s) for s,count in row['arrival'].items()),zero())/N
        reference_phase=sum((count*e(h*16**(j+1)*s) for s,count in row['current'].items()),zero())/N
        piece=A[j]*arrival-A[j+1]*reference_phase
        total+=piece
        levels.append({'j':j,'actual_arrival_character':complex_record(arrival),
                       'reference_character':complex_record(reference_phase),
                       'signed_contribution':complex_record(piece)})
        reference_average=sum((e(h*16**j*d) for d in range(16)),zero())/16
        difference=A[j+1]-A[j]*reference_average
        assert contains_zero(difference.real) and contains_zero(difference.imag)
        coefficient_checks.append(complex_record(difference))
    # Independent Poisson identity check, using g and endpoint psi only AFTER
    # the explicit innovation mean has been evaluated and retained above.
    gmean=sum((count*e(h*(2*s+1),2*M) for s,count in row['current'].items()),zero())/N
    def psi(s):
        return sum((A[j]*e(h*16**j*s) for j in range(k)),zero())
    endpoint=(psi(row['end'])-psi(row['start']))/N
    identity=gmean+endpoint
    difference=total-identity
    assert contains_zero(difference.real) and contains_zero(difference.imag)
    def eta(s,d):
        return sum((A[j]*e(h*16**j*(16*s+d))-A[j+1]*e(h*16**(j+1)*s)
                    for j in range(k)),zero())
    sampled_reference=[]
    for s in sorted({0,1,M-1,max(0,M-16)}):
        average=sum((eta(s,d) for d in range(16)),zero())/16
        assert contains_zero(average.real) and contains_zero(average.imag)
        sampled_reference.append({'state':s,'reference_average':complex_record(average)})
    coherent=eta(M-1,15)-e(-h,2*M)
    assert contains_zero(coherent.real) and contains_zero(coherent.imag)
    joint_records=[[s,d,count] for (s,d),count in sorted(row['joint'].items())]
    return {'h':h,'k':k,'memory_bits':4*k,'residue_states':M,
            'normalization':N,'interior_transitions':sum(row['current'].values()),
            'first_state':row['start'],'last_state':row['end'],
            'literal16_transition_count':sum(c for (s,d),c in row['joint'].items() if d==16),
            'joint_counts_sha256':sha256(json.dumps(joint_records,separators=(',',':')).encode()).hexdigest(),
            'explicit_innovation_mean':complex_record(total),'level_contributions':levels,
            'poisson_mean_check':complex_record(identity),
            'poisson_identity_difference':complex_record(difference),
            'interior_retrodictive_mean':complex_record(gmean),'poisson_endpoint':complex_record(endpoint),
            'reference_coefficient_identities':coefficient_checks,
            'sampled_reference_zero':sampled_reference,
            'all_states_reference_zero_scope':'Exact EI1 coefficient identities prove zero for every state; four states additionally evaluated.',
            'coherent_control_difference':complex_record(coherent),
            'phase_cache_entries':len(cache)}


def prepare(source_path):
    source,source_hash=read_source(source_path)
    contract='4,-2,-1,-1; poles7,4,3,2; literal U0=0'
    if source['source']['source_contract']!=contract:
        raise ValueError('source signature mismatch')
    carries=source['source']['carries']
    digest=sha256(b'floor(U_n)-16floor(U_(n-1))\0')
    for carry in carries:digest.update(str(carry).encode()+b'\n')
    assert digest.hexdigest()==source['source']['carry_sha256']
    n0,last,N=source['n0'],source['last'],source['L']
    assert last-n0+1==N
    counts=counts_from_carries(carries,n0,last)
    rows=[]
    for h in FREQUENCIES:
        for k in DEPTHS:
            rows.append(evaluate_counts(counts[k],h,N))
            print('carry_only_innovation',h,k,'done',flush=True)
    return {'schema':'carry-only-EI1-holdout-v1','source_file_sha256':source_hash,
            'source_contract':contract,'carry_sha256':digest.hexdigest(),
            'n0':n0,'last':last,'N':N,'frequencies':list(FREQUENCIES),
            'depths':list(DEPTHS),'interval_dps':DPS,'rows':rows,
            'full_source_phases_used':False,
            'scope':'Postregistration verification on the same holdout; carry-only formula, no fitting, no fresh predictive experiment.',
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'pi_normality':'OPEN','RH':'OPEN'}


def compare(prepared_path,source_path):
    from mpmath.ctx_iv import MPIntervalContext
    iv=MPIntervalContext();iv.dps=DPS
    raw=prepared_path.read_bytes();prepared=json.loads(raw)
    source,source_hash=read_source(source_path)
    assert source_hash==prepared['source_file_sha256']
    N,n0=prepared['N'],prepared['n0']
    def qinterval(record):
        lo,hi=Q(record['lower']),Q(record['upper'])
        a=iv.mpf(lo.numerator)/lo.denominator
        b=iv.mpf(hi.numerator)/hi.denominator
        return iv.mpf([a.a,b.b])
    def zinterval(record):return iv.mpc(qinterval(record['real']),qinterval(record['imag']))
    targets={}
    for row in source['per_time_phases']:
        assert row['start']==n0 and len(row['boxes'])==N
        totals=[sum(box[c] for box in row['boxes']) for c in range(4)]
        targets[row['h']]=iv.mpc(iv.mpf(totals[:2])/(N*2**80),iv.mpf(totals[2:])/(N*2**80))
    rows=[]
    for row in prepared['rows']:
        h,k=row['h'],row['k']
        innovation=zinterval(row['explicit_innovation_mean'])
        difference=targets[h]-innovation
        distance=iv.sqrt(difference.real**2+difference.imag**2)
        epsilon=iv.pi*abs(h)/16**k+iv.pi*abs(h)/(32*(n0-k)**2)
        budget=iv.mpf(4*k+1)/N+epsilon
        dlo,dhi=map(endpoint_fraction,distance._mpi_)
        blo,bhi=map(endpoint_fraction,budget._mpi_)
        assert dhi<=blo,(h,k,dhi,blo)
        rows.append({'h':h,'k':k,'memory_bits':4*k,
                     'W_mean_from_raw_phases':complex_record(targets[h]),
                     'innovation_mean':row['explicit_innovation_mean'],
                     'difference_modulus':interval_record(distance),
                     'source_proved_budget':interval_record(budget),
                     'observed_difference_below_proved_budget':True,
                     'difference_diagnostic':float(dhi),'budget_diagnostic':float(bhi)})
        print('carry_source_comparison',h,k,float(dhi),float(bhi),flush=True)
    return {'status':'PASS: direct carry-only innovations agree within proved source/endpoint budget',
            'prepared_file_sha256':sha256(raw).hexdigest(),'source_file_sha256':source_hash,
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'rows':rows,'last_unobserved_transition':'omitted, last unit phase charged1/N',
            'scope':'Same-holdout postregistration instrument check; no decay extrapolation.',
            'pi_normality':'OPEN','RH':'OPEN'}


if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('prepare','compare'))
    ap.add_argument('--source',type=Path,required=True);ap.add_argument('--prepared',type=Path)
    ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    if args.mode=='prepare':result=prepare(args.source)
    else:
        if args.prepared is None:ap.error('compare requires --prepared')
        result=compare(args.prepared,args.source)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
