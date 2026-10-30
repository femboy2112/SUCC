"""Predeclared exact signed probes; numeric Fourier norms are diagnostic only."""
from fractions import Fraction as F
import cmath
import hashlib
import json
from math import pi, sqrt
from signed_transport import (
    AUTH, forcing, orbit, split_primary, projected_history, order16, birth,
    energy_interval, minimum_energy_certificate, universal_floor_certificate,
    tail_difference_interval, energy_of_intervals, decimal_bracket, fc,
)

FRESH = (701,709,733,757,769,773,797,809,821,829,853,857)


def complex_turn(q):
    return cmath.exp(2j*pi*float(q % 1))


def row(p, h, values):
    b, L = birth(p), order16(p)
    phases = values[b:b+L]
    prim, cof = zip(*(split_primary(v, p) for v in phases))
    energy = tuple(x/(L-1) for x in energy_interval(phases, h))
    expected = 4 if p % 8 == 1 else -1
    assert all(a == F(expected*pow(16,j,p) % p,p) for j,a in enumerate(prim))
    assert len(set(prim)) == L
    return {'p':p,'h':h,'birth':b,'L':L,'eligible':L*L>=p,
            'energy':decimal_bracket(energy,24),
            'quarter_verdict': 'PASS' if energy[0]>=F(1,4) else
                               'FAIL' if energy[1]<F(1,4) else 'AMBIGUOUS',
            'primary_and_cofiber_retained': True,
            'phase_sha256': hashlib.sha256('\n'.join(map(str,phases)).encode()).hexdigest()}


def completion(p,h,values):
    b,L = birth(p),order16(p)
    prim,cof = zip(*(split_primary(v,p) for v in values[b:b+L]))
    f = [complex_turn(h*a) for a in prim]
    w = [complex_turn(h*v) for v in cof]
    wh = [sum(w[j]*complex_turn(F(-k*j,L)) for j in range(L))/L for k in range(L)]
    ff = [sum(f[j]*complex_turn(F(k*j,L)) for j in range(L)) for k in range(L)]
    direct = sum(x*y for x,y in zip(f,w))
    reconstructed = sum(x*y for x,y in zip(wh,ff))
    wiener = sum(map(abs,wh))
    V = sum(abs(a-b) for a,b in zip(w,w[1:]))
    bound = sqrt(p)*wiener
    return {'p':p,'h':h,'L':L,'actual_modulus':abs(direct),
            'wiener':wiener,'sqrtp_wiener_bound':bound,'bound_below_L':bound<L,
            'cofiber_variation':V,'reconstruction_residual':abs(direct-reconstructed),
            'authority':'floating-point diagnostic, not certificate'}


def energy_control(name, phases, h=1, kind='finite rational orbit'):
    E = tuple(x/(len(phases)-1) for x in energy_interval(phases,h))
    return {'name':name,'h':h,'samples':len(phases),'mean_energy':decimal_bracket(E,24),
            'kind':kind,'quarter_verdict':'PASS' if E[0]>=F(1,4) else
                      'FAIL' if E[1]<F(1,4) else 'AMBIGUOUS'}


def prefix_constant(digits):
    z = 0
    for d in digits:
        z = 16*z+d
    return F(z,16**len(digits))


def debruijn(k,n):
    a = [0]*(k*n+1)
    seq = []
    def db(t,p):
        if t>n:
            if n%p==0:seq.extend(a[1:p+1])
        else:
            a[t]=a[t-p];db(t+1,p)
            for j in range(a[t-p]+1,k):
                a[t]=j;db(t+1,t)
    db(1,1)
    return seq


def control_orbits(A=20,L=64):
    end = A+L
    values = orbit(end+16)
    controls = [energy_control('authentic',values[A:A+L+1])]
    for name,seed in [('exact circle alias',F(1,16)),('constant rational twist',F(1,15))]:
        v = orbit(end,seed)
        controls.append(energy_control(name,v[A:A+L+1]))
        assert energy_interval(v[A:A+L+1]) == energy_interval(values[A:A+L+1])
    M = end+8
    q = sum((forcing(n)/16**n for n in range(1,M+1)),F())
    seed = -F((q*16**M).__floor__(),16**M)
    dyad = orbit(M+3,seed)
    base = orbit(M+3)
    assert all(split_primary(x,13)[0]==split_primary(y,13)[0]
               for x,y in zip(dyad,base))
    assert dyad[M:] == base[M:]
    controls.append(energy_control('dyadic coherent finite window',dyad[A:A+L+1],
                     kind='same forcing; eventual exact circle alias; no asymptotic failure claim'))
    coherent = energy_of_intervals([tail_difference_interval(n) for n in range(A,A+L)])
    controls.append({'name':'coherent same-forcing seed -pi/16','mean_energy':
        decimal_bracket(tuple(x/L for x in coherent),30),'kind':'rigorous Green intervals'})
    for name,c in [('wrong ratio',(5,-2,-1,-1)),('same ratio',(4,-3,-1,0)),
                   ('positive p2 precision-5 age mutant',tuple(a+128*b for a,b in zip(AUTH,(1,-3,1,1))))]:
        v = orbit(end,coefficients=c)
        controls.append(energy_control(name,v[A:A+L+1],kind='changed source'))
    null = orbit(end,coefficients=(-8,8,4,8,2,2,-1,0),offsets=tuple(range(1,9)))
    controls.append(energy_control('seven-pole zero-seed null source',null[A:A+L+1],kind='changed source; coherent characters'))
    for name,fun in [('Gamma-rank fake',lambda n:F(15,(8*n-7)**2)),
        ('higher-jet matched fake',lambda n:forcing(n)+sum((F(c,8*n-7+j) for j,c in enumerate((1,-3,3,-1))),F()))]:
        v=[F()]
        for n in range(1,end+1):v.append((16*v[-1]+fun(n))%1)
        controls.append(energy_control(name,v[A:A+L+1],kind='changed positive source'))
    for c in (3,5,2):
        terms=[];power=c
        while power <= end+64:
            terms.append(F(1,power*16**power));power*=c
        alpha=sum(terms,F())
        phases=[(16**n*alpha)%1 for n in range(A,A+L+1)]
        controls.append(energy_control('Stoneham conductor '+str(c),phases,
            kind='rational truncation; omitted phase <= 2*16^-64, known classification from parent'))
    digits=[0]*(end+128)
    p=1
    while p<=len(digits):digits[p-1]=1;p*=2
    alpha=prefix_constant(digits)
    controls.append(energy_control('Kempner sparse radix16 construction',[(16**n*alpha)%1 for n in range(A,A+L+1)],kind='finite truncation; sparse nonnormal control'))
    seq=debruijn(16,2)
    numerator=prefix_constant(seq)*16**len(seq)
    alpha=F(numerator,16**len(seq)-1)
    controls.append(energy_control('periodic de Bruijn order2',[(16**n*alpha)%1 for n in range(A,A+L+1)],kind='exact periodic nonnormal source'))
    digits=[];k=1
    while len(digits)<end+128:
        digits.extend(int(x,16) for x in format(k,'x'));k+=1
    alpha=prefix_constant(digits)
    controls.append(energy_control('Champernowne radix16',[(16**n*alpha)%1 for n in range(A,A+L+1)],kind='finite truncation; classical normal control'))
    # Biased Bernoulli is an expectation, never a fabricated sampled worldline.
    real=(fc.SCALE,fc.SCALE);imag=(0,0)
    for k in range(1,17):
        rr=(0,0);ii=(0,0)
        for d in range(16):
            pr=F(1,2) if d==0 else F(1,30)
            cc,ss=fc.character(F(15*d,16**k))
            rr=fc.add(rr,fc.mul(fc.interval(pr),cc));ii=fc.add(ii,fc.mul(fc.interval(pr),ss))
        real,imag=fc.add(fc.mul(real,rr),fc.neg(fc.mul(imag,ii))),fc.add(fc.mul(real,ii),fc.mul(imag,rr))
    error=2*fc.PI_HI*15/16**16
    E=(1-F(real[1],fc.SCALE)-error,1-F(real[0],fc.SCALE)+error)
    controls.append({'name':'biased Bernoulli P(0)=1/2, others=1/30','mean_energy':decimal_bracket(E,24),
        'kind':'stationary expectation with rigorously bounded infinite product tail; not sample path',
        'quarter_verdict':'PASS' if E[0]>=F(1,4) else 'AMBIGUOUS'})
    return controls


def main():
    end=max(460,max(birth(p)+order16(p) for p in FRESH))
    values=orbit(end+1)
    rows=[row(p,h,values) for p in (13,73)+FRESH for h in (1,3,7)]
    projected=[]
    for p in (2,3,5,7,13,19,73):
        pp,vv=projected_history(300,p)
        for n,u in enumerate(values[:301]):
            assert split_primary(u,p)==(pp[n],vv[n])
        projected.append({'p':p,'times':301})
    assert split_primary(values[10],19)[0]==0
    assert split_primary(values[16],19)[0]==0
    assert split_primary(values[17],19)[0]!=0
    assert split_primary(values[274],73)[0]==0
    minima=[]
    for A,L in [(32,16),(64,32),(128,64),(256,128),(383,71)]:
        for h in (1,3,7):
            c=minimum_energy_certificate(A,L,h)
            reference=c['asymptotic_reference']
            low,high=c['mean_minimum']
            ratio=(low/(fc.PI_HI**2*h*h*reference/512),high/(fc.PI_LO**2*h*h*reference/512))
            E,floor=universal_floor_certificate(values,A,L,h)
            assert E[0]>=floor[1]
            minima.append({'A':A,'L':L,'h':h,'unwrap':c['unwrap'],
                'mean_minimum':decimal_bracket(c['mean_minimum'],40),
                'mean_coherent':decimal_bracket(c['mean_coherent'],40),
                'ratio_to_leading_asymptotic':decimal_bracket(ratio,24),
                'zero_seed_mean_energy':decimal_bracket(tuple(x/L for x in E),24),
                'universal_floor_sum':decimal_bracket(floor,40)})
    output={'status':'EXECUTED_FINITE_CERTIFICATES','SC06_status':'OPEN',
            'source':'authentic four poles; U0=0 unless explicitly typed control',
            'interval_authority':'inherited PR399 96-bit outward Machin/Taylor instrument',
            'cofiber_recurrence':projected,'SC06_rows':rows,
            'minimization_certificates':minima,
            'completion':[completion(p,h,values) for p in (13,29,73,701,709,733) for h in (1,3,7)],
            'controls':control_orbits()}
    print(json.dumps(output,indent=2))


if __name__=='__main__':main()
