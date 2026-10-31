"""Separate direct rational recurrence and high-precision Fourier implementation.

Does not import the interval engine. Numerical implementation check, not a new
proof certificate. Exact selected rational phases require no supplied pi.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps=85
HERE=Path(__file__).resolve().parent


def main():
    data=json.loads((HERE/'receipts/oracle-cases-data.json').read_text())
    xs=[]
    u=F(0)
    for n in range(1,max(row['N'] for row in data['rows'])+1):
        u=(16*u+F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))%1
        xs.append(u)
    rows=[]
    for row in data['rows']:
        N,H=row['N'],row['H']
        total=mp.mpf(1)
        for h in range(1,H):
            z=sum(mp.exp(2j*mp.pi*h*x.numerator/x.denominator) for x in xs[:N])/N
            total+=2*mp.mpf(H-h)/H*abs(z)**2
        low=mp.mpf(row['dyadic_lower'])/2**row['denominator_power_two']
        high=mp.mpf(row['dyadic_upper'])/2**row['denominator_power_two']
        assert low<total<high,(row,total)
        rows.append({'N':N,'H':H,'value':mp.nstr(total,45),
                     'interval_width':mp.nstr(high-low,10)})
    print(json.dumps({'status':'PASS','authority':'separate implementation; numerical calibration only',
                      'dps':mp.mp.dps,'rows':rows},indent=2))


if __name__=='__main__':main()
