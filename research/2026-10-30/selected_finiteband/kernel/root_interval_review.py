"""Complementary same-model review of root certified_band.py.

The module under test is imported to run it. Reference rational arithmetic and
Machin bounds below do not call its source, tail, trig or interval primitives.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import importlib.util
import json
import mpmath as mp

ROOT=Path(__file__).resolve().parent.parent/'certified_band.py'
spec=importlib.util.spec_from_file_location('under_review',ROOT)
u=importlib.util.module_from_spec(spec)
spec.loader.exec_module(u)
mp.mp.dps=120


def atan_interval(q,bits):
    total=F(0); j=0
    while True:
        term=F(1,(2*j+1)*q**(2*j+1))
        if term<F(1,2**(bits+32)):
            remainder=(-1)**j*term
            return min(total,total+remainder),max(total,total+remainder)
        total+=(-1)**j*term
        j+=1


def source(n):
    return 4*F(1,8*n-7)-2*F(1,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def in_box(q,box):
    return box[0]*q.denominator<=q.numerator*u.S<=box[1]*q.denominator


def main():
    floor_cases=0
    vals=[F(-17,9),F(-1,3),F(0),F(2,7),F(11,2)]
    for a in vals:
        for b in vals:
            ia=u.fraction(a.numerator,a.denominator)
            ib=u.fraction(b.numerator,b.denominator)
            assert in_box(a+b,u.add(ia,ib))
            assert in_box(a*b,u.mul(ia,ib))
            assert in_box(a*a,u.square(ia))
            assert in_box(a/7,u.div(ia,7))
            floor_cases+=4
    machin=[]
    for bits in (97,193,389,521):
        a,b=atan_interval(5,bits); c,d=atan_interval(239,bits)
        ml,mh=16*a-4*d,16*b-4*c
        lo,hi=u.pi_interval(bits)
        assert F(lo,2**bits)<ml<mh<F(hi,2**bits)
        machin.append({'bits':bits,'bbp_width_units':hi-lo})
    powers=[]
    for ar,ai,den in ((3,4,5),(-3,4,5),(5,-12,13),(7,24,25)):
        z=(u.fraction(ar,den),u.fraction(ai,den))
        pr,pi,pd=1,0,1
        count=0
        for rb,ib in u.unit_powers(z,1002):
            pr,pi,pd=pr*ar-pi*ai,pr*ai+pi*ar,pd*den
            assert in_box(F(pr,pd),rb) and in_box(F(pi,pd),ib)
            count+=1
        powers.append({'unit':[ar,ai,den],'exact_powers_checked':count})
    for j,(c,s) in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
        rb,ib=u.trig((j*u.S//4,j*u.S//4))
        assert in_box(F(c),rb) and in_box(F(s),ib)
    for k in (-7,-1,1,5,13,29):
        x=F(k,31)
        box=u.fraction(x.numerator,x.denominator)
        rb,ib=u.trig(box)
        v=2*mp.pi*mp.mpf(x.numerator)/x.denominator
        assert mp.mpf(rb[0])/u.S<=mp.cos(v)<=mp.mpf(rb[1])/u.S
        assert mp.mpf(ib[0])/u.S<=mp.sin(v)<=mp.mpf(ib[1])/u.S
    tail_rows=[]
    for n in (1,7,31,97,257):
        lo=sum((source(n+j)/16**j for j in range(1,49)),F(0))
        hi=lo+source(n+49)/(15*16**48)
        a,b=u.tail_interval(n)
        assert F(a,u.S)<=lo<hi<=F(b,u.S)
        tail_rows.append({'n':n,'root_width_units':b-a})
    state=F(0)
    for n,box in u.selected_intervals(53):
        state=(16*state+source(n))%1
        assert any(in_box(state+j,box) for j in (-1,0,1))
    energies=[]
    for row in u.energies([11,23],[7,19]):
        N,H=row['N'],row['H']
        state=F(0); xs=[]
        for n in range(1,N+1):
            state=(16*state+source(n))%1
            xs.append(mp.mpf(state.numerator)/state.denominator)
        value=1+2*sum(mp.mpf(H-h)/H*abs(sum(mp.exp(2j*mp.pi*h*x) for x in xs)/N)**2
                      for h in range(1,H))
        assert mp.mpf(row['dyadic_lower'])/u.S<value<mp.mpf(row['dyadic_upper'])/u.S
        energies.append({'N':N,'H':H,'value':mp.nstr(value,35),
                         'enclosure_width_units':int(row['dyadic_upper'])-int(row['dyadic_lower'])})
    print(json.dumps({'status':'PASS','reviewed_code_sha256':hashlib.sha256(ROOT.read_bytes()).hexdigest(),
       'exact_interval_operations':floor_cases,'independent_Machin':machin,
       'rational_unit_powers':powers,'exact_special_trig_points':4,
       'high_precision_trig_points':6,'independent_tail_enclosures':tail_rows,
       'exact_original_states':53,'energy_enclosures':energies,
       'authority':'same-model complementary review; high precision checks not independent proof'},indent=2))


if __name__=='__main__':main()
