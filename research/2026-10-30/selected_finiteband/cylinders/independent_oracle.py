"""Separate algorithms: Machin intervals, direct impulse residues, Gram polynomials.

No import of cylinder_probe. Same model/context, not an independent referee.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps=90
HERE=Path(__file__).resolve().parent


def atan_interval(q, terms):
    partial=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(terms)),F())
    other=partial+F((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return min(partial,other),max(partial,other)


def pi_interval():
    a,b=atan_interval(5,350)
    c,d=atan_interval(239,110)
    return 16*a-4*d,16*b-4*c


def source_combined(n):
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def exact_stoneham(c, n):
    p=0
    while c**(p+1) <= n:
        p+=1
    if not p:
        return F()
    q=c**p
    numerator=sum(c**(p-k)*pow(16,n-c**k,q) for k in range(1,p+1)) % q
    return F(numerator,q)


def mpf(x):
    return mp.mpf(x.numerator)/x.denominator


def fejer_frequency(points,H):
    total=mp.mpf(1)
    for h in range(1,H):
        mean=sum(mp.exp(2j*mp.pi*h*mpf(x)) for x in points)/len(points)
        total+=2*mp.mpf(H-h)/H*abs(mean)**2
    return total


def run():
    input_path=HERE/'receipts/probe.json'
    receipt=json.loads(input_path.read_text())
    plo,phi=pi_interval()
    assert phi-plo < F(1,16**340)
    # No source recurrence/tail inputs used in this digit implementation.
    lo=(16**320*plo).__floor__()
    hi=(16**320*phi).__floor__()
    assert lo==hi
    hexword=f'{lo % 16**320:0320X}'
    for row in receipt['source_rows']:
        assert hexword[row['A']-1:row['A']-1+row['L']]==row['word']
    source_checks=0
    u=F()
    slips=[]
    for n in range(1,321):
        u=sum((16**(n-k)*source_combined(k) for k in range(1,n+1)),F()) if n<=5 else 16*u+source_combined(n)
        lag=15*u+source_combined(n+1)
        x=lag % 1
        slips.append(min(x,1-x)>F(1,20))
        source_checks+=1
    for row in receipt['source_rows']:
        assert sum(slips[row['A']-1:row['A']-1+row['L']])==row['strict_slips']
    stages=[]
    for c,p in ((3,3),(3,6),(5,4)):
        q=c**p
        counts=Counter(exact_stoneham(c,n) for n in range(q,c*q))
        assert counts=={F(1+c*j,q):c*(c-1) for j in range(q//c)}
        stages.append(dict(c=c,p=p,grid_size=len(counts),multiplicity=c*(c-1)))
    # Root-of-unity kernel identity: coefficients modulo the grid modulus.
    gram_checks=0
    for q in (3,9,25,27,125):
        for H in (2,8,17,32,128):
            differences=Counter((i-j)%q for i in range(H) for j in range(H))
            # Grid average of |sum e(a x)|^2/H has surviving q-divisible differences.
            direct=F(q*differences[0],H)
            formula=q*(1+2*sum((F(H-j*q,H) for j in range(1,(H-1)//q+1)),F()))
            assert direct==formula and direct<=q+H
            gram_checks+=1
    periodic=[]
    for H in (8,17,34,128,257):
        points=[F(1,255),F(16,255)]
        energy=fejer_frequency(points,H)
        kernel=abs(sum(mp.exp(2j*mp.pi*j/17) for j in range(H)))**2/H
        assert abs(energy-(H+kernel)/2)<mp.mpf('1e-78')
        assert energy>=mp.mpf(H)/2-mp.mpf('1e-78')
        if H % 17==0:
            assert abs(energy-mp.mpf(H)/2)<mp.mpf('1e-78')
        periodic.append(dict(H=H,energy=mp.nstr(energy,30),lower=str(F(H,2))))
    stoneham_rows=[]
    for c,N,H in ((3,82,8),(5,251,16),(3,730,32)):
        surrogate=[exact_stoneham(c,n) for n in range(N)]
        p=0
        while c**(p+1)<=N-1:
            p+=1
        last=p+1
        alpha=sum((F(1,c**k*16**(c**k)) for k in range(1,last+1)),F())
        completed=[(16**n*alpha)%1 for n in range(N)]
        a=fejer_frequency(surrogate,H)
        b=fejer_frequency(completed,H)
        finite_bound=F(c)+F(H*(c+c*(c-1)*p),N)
        correction=F(4*(H*H-1),45*(c-1)*N)
        # Tiny omitted positive pulses, bounded independently of float behavior.
        max_omitted=F(16**(N-1),(c-1)*c**last*16**(c**(last+1)))
        omitted_energy=4*mp.pi*(H*H-1)/3*mpf(max_omitted)
        assert a<=mpf(finite_bound)
        assert abs(a-b)+omitted_energy<mp.pi*mpf(correction)
        assert b+omitted_energy<=mpf(finite_bound)+mp.pi*mpf(correction)
        stoneham_rows.append(dict(c=c,N=N,H=H,surrogate_energy=mp.nstr(a,25),
                                completed_truncation_energy=mp.nstr(b,25),
                                upper=mp.nstr(mpf(finite_bound)+mp.pi*mpf(correction),25),
                                omitted_energy_lt_1e_minus_100=omitted_energy<mp.mpf('1e-100')))
    return dict(status='PASS',precision_dps=mp.mp.dps,machin_digits=320,
                independent_source_slip_checks=source_checks,fresh_stages=stages,
                exact_gram_checks=gram_checks,periodic_energy_rows=periodic,
                stoneham_energy_rows=stoneham_rows,
                scope='exact rational identities plus numerical phase checks with declared tail bounds')


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
