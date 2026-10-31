"""Separate symbolic and Machin/Green routes; imports no front implementation.

Shared model authorship is explicit; this is computational method separation.
"""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import hashlib,json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

root=Path(__file__).resolve().parent
probe=json.loads((root/'probe_receipt.json').read_text())
M=S.Matrix([[1,1],[1,0]])
A=M-16*S.eye(2)
assert A.det()==239
normal=smith_normal_form(A,domain=S.ZZ)
assert sorted(abs(int(normal[i,i])) for i in range(2))==[1,239]
lam=(S.sqrt(5)-1)/2
symbolic_lags=[]
for k in (3,4,8,13,21,31,37):
    fk=int((M**k)[0,1]); prev=int((M**(k-1))[0,1])
    assert S.simplify(fk*lam-prev-(-1)**(k-1)*lam**k)==0
    symbolic_lags.append(k)

# Hensel: enumerate all239 next digits, instead of the derivative algorithm.
x=16; modulus=239
for recorded in probe['hensel_roots']:
    assert (recorded['root'],recorded['modulus'])==(x,modulus)
    options=[x+modulus*d for d in range(239)
             if ((x+modulus*d)**2-(x+modulus*d)-1)%(modulus*239)==0]
    assert len(options)==1
    x=options[0];modulus*=239

# Different source representation: collapse the four poles into one rational.
def r(n):
    a=8*n-7
    return Q(15*a*a+121*a+240,a*(a+3)*(a+4)*(a+5))

# Direct unrolled Green prefix, not a recurrence update.
def state(n):return sum((16**(n-j)*r(j) for j in range(1,n+1)),Q())
for n in list(range(0,61))+[89,137]:
    assert state(n+2)-state(n+1)-240*state(n)==15*r(n+1)+r(n+2)
assert state(60).denominator%239==0
v=239*state(60)
assert v.numerator*pow(v.denominator,-1,239)%239==119

# Rigorous fixed-point alternating arctangent enclosures.
# Every retained reciprocal term is bracketed by two adjacent scaled integers.
def atan_interval(p,scale):
    total_lo=total_hi=0
    power=p; j=0
    while True:
        den=(2*j+1)*power
        q=scale//den
        if q==0:break
        if j%2==0:total_lo+=q;total_hi+=q+1
        else:total_lo-=q+1;total_hi-=q
        power*=p*p;j+=1
    # Alternating remainder has sign(-1)^j, magnitude less than1/scale.
    if j%2==0:total_hi+=1
    else:total_lo-=1
    return Q(total_lo,scale),Q(total_hi,scale),j

max_n=max(v['stop_exclusive'] for v in probe['selected_windows'])
scale=2**(4*max_n+256)
a,b,j5=atan_interval(5,scale)
c,d,j239=atan_interval(239,scale)
pi_lo,pi_hi=16*a-4*d,16*b-4*c
assert pi_lo<pi_hi
assert pi_hi-pi_lo<Q(1,2**(4*max_n+200))

def tail(n,terms=24):
    lo=sum((r(n+j)*Q(1,16**j) for j in range(1,terms+1)),Q())
    return lo,lo+r(n+terms+1)*Q(1,15*16**terms)

cached_tails={n:tail(n) for n in range(13,max_n+1)}
rows=[]
for rec in probe['selected_windows']:
    count=0; ambiguous=0
    for n in range(rec['start'],rec['stop_exclusive']):
        h=rec['h']
        a,b=cached_tails[n];c,d=cached_tails[n+1]
        lower=h*(15*16**(n-1)*pi_lo+a-d)
        upper=h*(15*16**(n-1)*pi_hi+b-c)
        floor_lo=lower.numerator//lower.denominator
        floor_hi=upper.numerator//upper.denominator
        # Interval endpoints might cross integers; such cases need splitting.
        # None do here; we refuse to classify any that would.
        if floor_lo!=floor_hi:ambiguous+=1;continue
        lo,hi=lower-floor_lo,upper-floor_hi
        if lo>=Q(1,20) and hi<=Q(19,20):count+=1
        elif hi<Q(1,20) or lo>Q(19,20):pass
        else:ambiguous+=1
    assert ambiguous==0
    assert count==rec['slips']
    rows.append(dict(k=rec['k'],h=rec['h'],slips=count,ambiguous=ambiguous))

out=dict(status='PASS',authority='Separate symbolic and exact Machin/Green implementations; shared model',
    smith_diagonal=[1,239],symbolic_golden_lag_cases=symbolic_lags,
    direct_unrolled_source_cases=63,hensel_bruteforce_levels=5,
    machin_terms={'p5':j5,'p239':j239},machin_precision_bits=4*max_n+256,
    tail_terms=24,rigorous_selected_window_rows=rows,
    compared_probe_sha256=hashlib.sha256((root/'probe_receipt.json').read_bytes()).hexdigest())
(root/'oracle_receipt.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rigorous_selected_window_rows'},indent=2))
print('All29 exact selected window counts separately certified.')
