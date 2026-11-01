"""Reproduce preregistered finite certificates, one horizon per invocation."""
from pathlib import Path
import sys, importlib.util, json, time
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
m=load('moonshot_probe_exact','phase_echo.py')
o=load('moonshot_probe_oracle','independent_oracle.py')

def encode(x):
    if isinstance(x,F):return {'numerator':str(x.numerator),'denominator':str(x.denominator)}
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def clock(N):
    K=0;x=1
    while 4*x<=N:x*=4;K+=1
    return max(1,K)

def main():
    start=time.monotonic(); N=int(sys.argv[1]) if len(sys.argv)>1 else 384
    if N not in (48,96,384,768,1537,3072):raise ValueError('not preregistered')
    xs=m.states(N,circle=True);enc=m.PhaseEncloser();records=[];oracle=[]
    for n in (1,2,23,N):
        ok=xs[n]==o.modular_prefix(n)
        if not ok:raise AssertionError(('independent source mismatch',n))
        oracle.append({'n':n,'modular_exponentiation_matches':ok})
    harmonics=(int(sys.argv[2]),) if len(sys.argv)>2 else (1,3,5,7,11)
    if any(h not in (1,3,5,7,11) for h in harmonics):raise ValueError("not preregistered harmonic")
    for h in harmonics:
        r=m.certified_scores(xs,N,clock(N),h,enc)
        if r['mean_square'][0] > r['vdc_actual_upper']:raise AssertionError('VdC violation')
        r['scope']='CALIBRATION' if N<384 else 'PREREGISTERED_HOLDOUT';records.append(r)
        print(json.dumps({'N':N,'h':h,'K':r['K'],'L':[float(x) for x in r['reduced_lag']],
                          'actual':[float(x) for x in r['actual_lag']],
                          'square':[float(x) for x in r['mean_square']],
                          'vdc_upper':float(r['vdc_actual_upper'])}),flush=True)
    payload={'status':'COMPLETED_FINITE_ONLY','base':'661553f182c425b06b5339ed02d7739a0ae72380',
             'arithmetic':'Fraction + outward fixed-point Taylor; no floats used for verdicts',
             'pi_source':'Machin identity + rational alternating remainders','bits':90,'terms':30,
             'records':records,'independent_source_checks':oracle,
             'elapsed_seconds_observed':time.monotonic()-start}
    suffix=f'_h{harmonics[0]}' if len(harmonics)==1 else ''
    out=ROOT/f'CERTIFICATE_N{N}{suffix}.json';out.write_text(json.dumps(encode(payload),indent=2))
    print('COMPLETED',N,len(records),'records',round(time.monotonic()-start,3),flush=True)

if __name__=='__main__':main()
