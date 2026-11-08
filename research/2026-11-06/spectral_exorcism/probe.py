"""Original-source Fejer spectral-ray and clock energy diagnostics. FLOAT ONLY."""
from fractions import Fraction
from math import pi, cos
from cmath import exp
import json

def original(N):
    x=Fraction(0); xs=[x]
    for n in range(1,N):
        r=Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        v=16*x+r; x=v-v.numerator//v.denominator
        xs.append(x)
    return xs

def spectrum(xs,N,H):
    vals=[]
    for h in range(1,H+1):
        w=sum(exp(2j*pi*h*float(x)) for x in xs[:N])/N
        vals.append(abs(w)**2)
    return {'unweighted_float':round(2*sum(vals),10),
            'fejer_float':round(1+2*sum((1-(h+1)/(H+1))*vals[h] for h in range(H)),10)}

def wavelet(xs,N):
    f=[exp(2j*pi*float(x)) for x in xs[:N]]
    m=N.bit_length()-1; E=[]
    for k in range(m+1):
        Q=1<<k; M=N//Q
        E.append(sum(abs(sum(f[j+t*Q] for t in range(M))/M)**2 for j in range(Q))/Q)
    return {'E0_float':round(E[0],12),
            'increments_float':[round(E[k+1]-E[k],9) for k in range(m)],
            'escape_float':round(1-E[0],12)}

def run():
    xs=original(1024)
    result={'status':'OBSERVED FINITE FLOAT DIAGNOSTICS ONLY',
            'source':'authentic four-pole','literal_U0':'0',
            'spectra':[],'wavelet':[],'periodic_fejer':[],'normality':'OPEN'}
    for N in (256,512,1024):
        result['spectra'].append({'N':N,'H':{str(H):spectrum(xs,N,H) for H in (8,16,32)}})
        shadow=[Fraction(n,(2*n-1)**4) for n in range(N)]
        periodic=[Fraction(pow(16,n,17),17) for n in range(N)]
        for kind,ys in [('original',xs),('shadow',shadow),('periodic',periodic)]:
            data=wavelet(ys,N);data.update(N=N,kind=kind)
            assert abs(sum(data['increments_float'])-data['escape_float'])<1e-7
            result['wavelet'].append(data)
    for H in (16,256,4096):
        # Exact period-two orbit is ±1/17; only final trigonometry is float.
        energy=1+2*sum((1-h/(H+1))*cos(2*pi*h/17)**2 for h in range(1,H+1))
        result['periodic_fejer'].append({'H':H,'energy_float':round(energy,8)})
    return result

if __name__=='__main__': print(json.dumps(run(),indent=2,sort_keys=True))
