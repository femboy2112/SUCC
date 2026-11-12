#!/usr/bin/env python3
"""Independent arithmetic/library route: SymPy isprime + NumPy FFT.
    Does not import production functions; validates sample and Fourier identity.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from sympy import isprime

rec=json.load(open(Path(__file__).with_name('results.json')))
for record in rec['midpoints']:
    n=record['midpoint_n']
    ordered=sum(int(isprime(p) and isprime(2*n-p)) for p in range(2,2*n-1))
    assert ordered==record['ordered_pairs'], (n,ordered,record)
    assert ordered%2==int(isprime(n))
for record in rec['crt_haar_certificates']:
    n,z,block=(record[k] for k in ['n','cutoff','block_size'])
    lp=[int(isprime(j)) for j in range(z+1)]
    selected=[d for d in range(n-z) if all((n*n-d*d)%q for q in range(2,z+1) if lp[q])]
    accum={}
    for d in selected:
        k=d//block
        t=accum.setdefault(k,[0,0,0])
        t[0]+=1;t[1]+=int(isprime(n+d));t[2]+=int(isprime(n-d))
    lb=sum(max(0,A+B-M) for M,A,B in accum.values())
    actual=sum(int(isprime(n+d) and isprime(n-d)) for d in selected)
    assert (lb,actual)==(record['certified_lower_bound'],record['actual_interior_witnesses'])
# Different basis: cyclic DFT of prime mask; no modular alias if M > 4n.
fft_values={}
for n in [10,100,256]:
    M=1
    while M<=4*n: M*=2
    f=np.zeros(M)
    for p in range(2,2*n+1):
        if isprime(p): f[p]=1
    # Our inverse FFT convention is exp(+2pi ikx/M); ifft(fft(f)^2) is convolution.
    corr=np.fft.ifft(np.fft.fft(f)**2)
    got=float(corr[2*n].real)
    expected=next(row['ordered_pairs'] for row in rec['midpoints'] if row['midpoint_n']==n)
    assert abs(got-expected)<1e-7 and abs(corr[2*n].imag)<1e-7, (n,got,expected)
    fft_values[str(n)]={'fft_count':got,'expected_integer':expected,'imag_error':float(corr[2*n].imag)}
with open(Path(__file__).with_name('independent_audit.json'),'w') as f:
    json.dump({'sympy_checked_midpoints':len(rec['midpoints']),
               'sympy_checked_crt_haar_certificates':len(rec['crt_haar_certificates']),
               'numpy_fourier_reconstructions':fft_values,
               'status':'PASS (independent library route, still same operator/team)'},f,indent=2)
print('Independent audit PASS:',len(rec['midpoints']),'prime counts,',
      len(rec['crt_haar_certificates']),'CRT-Haar certificates, FFT cases',list(fft_values))
