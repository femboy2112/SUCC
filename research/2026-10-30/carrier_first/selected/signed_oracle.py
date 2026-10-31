"""Distinct pi/Green numerical route for the full CRT product holdouts."""
from pathlib import Path
from fractions import Fraction as Q
import json
import mpmath as mp


def main():
    data=json.loads((Path(__file__).parent/'receipts/signed-data.json').read_text())
    maxn=max(row['A']+row['L'] for row in data['rows'])
    mp.mp.dps=2*maxn+160
    r=lambda n:4/mp.mpf(8*n-7)-2/mp.mpf(8*n-4)-1/mp.mpf(8*n-3)-1/mp.mpf(8*n-2)
    tail=lambda n:mp.fsum(r(n+j)*mp.power(16,-j) for j in range(1,100))
    rows=[]
    for row in data['rows']:
        p,A,L,h=row['p'],row['A'],row['L'],row['h']
        # At first p-pole encounter the source coefficient is4 (p=1 mod8)
        # or−1 (p=5 mod8), and the encountered denominator is exactly p.
        c=4 if p%8==1 else -1
        full=[];primary=[]
        for n in range(A,A+L):
            a=(c*pow(16,n-A,p))%p
            prim=mp.mpf(a)/p
            orbit=mp.frac(mp.power(16,n-1)*mp.pi)-tail(n)
            cofiber=orbit-prim
            full.append(mp.exp(2j*mp.pi*h*prim)*mp.exp(2j*mp.pi*h*cofiber))
            primary.append(mp.exp(2j*mp.pi*h*prim))
        fullmag=abs(mp.fsum(full)/L)**2
        primmag=abs(mp.fsum(primary)/L)**2
        for key,value in [('full_squared_interval',fullmag),('primary_squared_interval',primmag)]:
            lo,hi=(mp.mpf(x)/mp.power(2,row['bits']) for x in row[key])
            assert lo<value<hi,(p,h,key,mp.nstr(value,45))
        rows.append({'p':p,'h':h,'full_squared':mp.nstr(fullmag,35),
                     'primary_squared':mp.nstr(primmag,35),'inside_integer_intervals':True})
    print(json.dumps({'status':'PASS','precision_dps':mp.mp.dps,'rows':rows,
                      'authority':'numerical independent route; interval theorem is separately derived'},indent=2))


if __name__=='__main__':main()
