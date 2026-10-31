"""Separate rational cofiber computation and 85-digit signed product sums."""
from fractions import Fraction as F
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=85


def primary(x,p):
    d=x.denominator;v=1
    while d%p==0:d//=p;v*=p
    return F((x.numerator*pow(d,-1,v))%v,v) if v>1 else F(0)


def phase(x):
    x=x%1
    return mp.exp(2j*mp.pi*mp.mpf(x.numerator)/x.denominator)


def main():
    data=json.loads((Path(__file__).parent/'receipts/signed-windows-data.json').read_text())
    last=max(r['birth']+r['length']-1 for r in data['rows'])
    u=F(0);states=[u]
    for n in range(1,last+1):
        u=(16*u+F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))%1
        states.append(u)
    rows=[]
    for row in data['rows']:
        p,h,b,L=(row[k] for k in ('p','h','birth','length'))
        product=mp.mpc(0);direct=mp.mpc(0);prime_only=mp.mpc(0)
        for n in range(b,b+L):
            a=primary(states[n],p);v=states[n]-a
            assert v.denominator%p!=0
            product+=phase(h*a)*phase(h*v)
            direct+=phase(h*states[n]);prime_only+=phase(h*a)
        assert abs(product-direct)<mp.mpf('1e-75')
        q=abs(product/L)**2
        assert mp.mpf(row['dyadic_lower'])/2**data['bits']<q<mp.mpf(row['dyadic_upper'])/2**data['bits']
        rows.append({'p':p,'h':h,'full_squared_modulus':mp.nstr(q,40),
                     'primary_only_squared_modulus':mp.nstr(abs(prime_only/L)**2,24),
                     'factorization_error':mp.nstr(abs(product-direct),10)})
    print(json.dumps({'status':'PASS','authority':'separate numeric oracle, not asymptotic proof',
                      'dps':mp.mp.dps,'rows':rows},indent=2))


if __name__=='__main__':main()
