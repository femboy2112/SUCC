"""Rigorous finite-only BBP P5 windows: rational Taylor/Machin enclosures."""
from fractions import Fraction as F
from math import factorial
from prime_window import states_through,window,combined_source,source

def atan_bounds(x, terms=15):
    s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    rem=x**(2*terms+1)/F(2*terms+1)
    return (s-rem,s) if terms%2 else (s,s+rem)

def pi_bounds():
    al,au=atan_bounds(F(1,5)); bl,bu=atan_bounds(F(1,239))
    lo,hi=16*al-4*bu,16*au-4*bl
    assert F(3)<lo<hi<F(22,7)
    return lo,hi

def fixed_angle(u,h,pi_mid,bits=32,terms=12):
    q=(h*u)%1
    if q>F(1,2):q-=1
    g=F((q*2**bits).__floor__(),2**bits)
    theta=2*pi_mid*g
    assert abs(theta)<F(22,7)
    cs=sum(((-1)**j*theta**(2*j)/F(factorial(2*j)) for j in range(terms+1)),F(0))
    sn=sum(((-1)**j*theta**(2*j+1)/F(factorial(2*j+1)) for j in range(terms+1)),F(0))
    return cs,sn

def prove_window(p,hs=(1,3,5),bits=32,terms=12):
    a,b,L=window(p)
    ss=states_through(b)
    # Independently check every sampled raw source against combined rational form.
    for n in range(1,b+1):assert source(n)==combined_source(n)
    lo,hi=pi_bounds()
    mid=(lo+hi)/2
    err=(F(22,7)**(2*terms+1)/F(factorial(2*terms+1)) +
         F(22,7)**(2*terms+2)/F(factorial(2*terms+2)) +
         (hi-lo) + F(44,7*2**bits))
    results=[]
    for h in hs:
        re=im=F(0)
        for n in range(a,b+1):
            c,s=fixed_angle(ss[n],h,mid,bits,terms)
            re+=c;im+=s
        bound=(abs(re)+abs(im))/L+2*err
        target=F(1,4)
        assert bound<target
        results.append({'p':p,'h':h,'L':L,'upper_l1':str(F(-(-bound.numerator*10**9//bound.denominator),10**9)),
                        'under_1_8':bound<F(1,8),'under_1_16':bound<F(1,16)})
    return results

if __name__=='__main__':
  import time,json
  t=time.monotonic();out=[]
  for p in [269,373,397,509,997]:
   o=prove_window(p);out+=o
   print('p',p,'elapsed',round(time.monotonic()-t,2),o,flush=True)
  print(json.dumps(out,indent=2))


def certify_both_directions():
    """EXACT-Fraction inequalities: original cofactor can strengthen OR weaken saving."""
    lo,hi=pi_bounds();mid=(lo+hi)/2;bits=32;terms=12
    err=(F(22,7)**(2*terms+1)/F(factorial(2*terms+1)) +
         F(22,7)**(2*terms+2)/F(factorial(2*terms+2)) +
         (hi-lo)+F(44,7*2**bits))
    rows=[]
    for p,h,expected in ((373,1,'joint_larger'),(397,3,'joint_smaller')):
        a,b,L=window(p);us=states_through(b)
        fr=fi=pr=pi=F(0)
        for n in range(a,b+1):
            c,s=fixed_angle(us[n],h,mid,bits,terms);fr+=c;fi+=s
            c,s=fixed_angle(-F(pow(16,n-a,p),p),h,mid,bits,terms)
            pr+=c;pi+=s
        fr/=L;fi/=L;pr/=L;pi/=L
        if expected=='joint_larger':
            gap=abs(fi)-err-(abs(pr)+abs(pi)+2*err)
        else:
            gap=abs(pr)-err-(abs(fr)+abs(fi)+2*err)
        assert gap>0,(p,h,expected)
        rows.append({'prime':p,'h':h,'strict_order':expected,
                     'certified_gap_lower':str(F(gap.numerator*10**9//gap.denominator,10**9)),
                     'method':'real-component lower vs other-vector L1 upper; exact outward intervals'})
    return rows


def certify_holdout_directions():
    """Finite signed comparison AFTER preregistered holdouts; signs not predicted."""
    lo,hi=pi_bounds();mid=(lo+hi)/2;bits=32;terms=12
    err=(F(22,7)**(2*terms+1)/F(factorial(2*terms+1)) +
         F(22,7)**(2*terms+2)/F(factorial(2*terms+2)) +
         (hi-lo)+F(44,7*2**bits))
    rows=[]
    for p,h,direction in ((1013,1,'joint_smaller'),(1021,5,'joint_larger')):
        a,b,L=window(p);us=states_through(b)
        fr=fi=pr=pi=F(0)
        for n in range(a,b+1):
            c,s=fixed_angle(us[n],h,mid,bits,terms);fr+=c;fi+=s
            c,s=fixed_angle(-F(pow(16,n-a,p),p),h,mid,bits,terms)
            pr+=c;pi+=s
        fr/=L;fi/=L;pr/=L;pi/=L
        def lower_sq(r,i):
            return max(F(0),abs(r)-err)**2+max(F(0),abs(i)-err)**2
        def upper_sq(r,i):
            return (abs(r)+err)**2+(abs(i)+err)**2
        gap=(lower_sq(fr,fi)-upper_sq(pr,pi) if direction=='joint_larger' else
             lower_sq(pr,pi)-upper_sq(fr,fi))
        assert gap>0,(p,h)
        rows.append({'prime':p,'h':h,'strict_order':direction,
                     'certified_squared_gap_lower':str(F(gap.numerator*10**9//gap.denominator,10**9)),
                     'method':'two-component rational square-norm lower vs upper intervals'})
    return rows
