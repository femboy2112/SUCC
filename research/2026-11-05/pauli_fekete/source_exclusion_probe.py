"""Exact BBP source / finite Fourier-frame / Fekete-exclusion probes.

Research-only: float logs/cosines are diagnostics, not proof certificates.
No input π digits. Source states are exact unwrapped fractions until phase reduction.
"""
from fractions import Fraction as F
from math import pi, sin, log, sqrt, cos
from cmath import exp

TAPS = (F(4), F(0), F(0), F(-2), F(-1), F(-1), F(0), F(0))

def source(n):
    return sum((w/F(8*(n-1)+j) for j,w in enumerate(TAPS,1)),F(0))

def source_independent(n):
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def original_epoch(A):
    u=F()
    out=[]
    for n in range(1,2*A):
        rn=source(n)
        assert rn==source_independent(n)
        u=16*u+rn
        if n>=A:out.append(u%1)
    assert len(out)==A
    return out

def coherent_epoch(A):
    # s*=-pi/16 completed orbit = -T_n; no π digit input.
    return [(-sum((F(1,16**k)*source(n+k) for k in range(1,41)),F()))%1
            for n in range(A,2*A)]

def e(x):
    return exp(2j*pi*float(x%1))

def distance(x,y):
    d=(x-y)%1
    if d>F(1,2):d=1-d
    return 2*sin(pi*float(d))

def energy(xs):
    N=len(xs)
    vals=[distance(xs[i],xs[j]) for i in range(N) for j in range(i+1,N)]
    assert min(vals)>0
    return 2*sum(map(log,vals))/(N*N)

def mode(xs,h):
    return sum((e(h*x) for x in xs),0j)/len(xs)

def frame_purity(xs,M):
    N=len(xs)
    gram=[]
    for j in range(M):
      row=[]
      for k in range(M):
        row.append(sum((e((j-k)*x) for x in xs),0j)/(N*M))
      gram.append(row)
    observed=sum(abs(gram[j][k])**2 for j in range(M) for k in range(M))
    rhs=1/M+(2/M**2)*sum((M-h)*abs(mode(xs,h))**2 for h in range(1,M))
    assert abs(observed-rhs)<1e-11,(observed,rhs)
    return rhs

def positive_kernel(xs):
    N=len(xs)
    r=1-1/N
    # Exact pairwise formula of convergent Fourier sum over all h>=1.
    output=0.
    for i in range(N):
      for j in range(N):
        d=distance(xs[i],xs[j]) if i!=j else 0.
        output+=-0.5*log((1-r)**2+r*d*d)
    output/=N*N
    E=energy(xs)
    sharp=-E+(1-1/N)*log(2/(1+r))+log(N)/N
    assert output<=sharp+1e-10,(output,sharp)
    for h in (1,2,3):
      assert (r**h/h)*abs(mode(xs,h))**2<=sharp+1e-10
    return output,sharp

def test():
    for A in (9,17,33):
        orig=original_epoch(A)
        wrong=coherent_epoch(A)
        print('epoch',A)
        for label,xs in [('BBP zero seed',orig),('coherent wrong seed',wrong),
                         ('regular roots',[F(j,A) for j in range(A)]),
                         ('half-circle',[F(j,2*A) for j in range(A)])]:
            E=energy(xs)
            assert E<=log(A)/A+1e-10
            P3,P5=frame_purity(xs,3),frame_purity(xs,5)
            K,R=positive_kernel(xs)
            print(label,'E=',round(E,9),'|c1|=',round(abs(mode(xs,1)),9),
                  'frame3=',round(P3,9),'frame5=',round(P5,9),
                  'kernelBoundGap=',round(R-K,9))
            if label=='regular roots':
              assert abs(E-log(A)/A)<1e-11
              assert abs(mode(xs,1))<1e-11
            if label=='coherent wrong seed':
              # Uses the source-specific global tail inequality T_n<1/(64n^2)
              rhs=(A-1)/A*(log(pi/32)-2*log(A))
              assert E<rhs,(A,E,rhs)
        print('---')
    print('SOURCE_EXCLUSION_FRESH_HOLDOUTS_PASS')

if __name__=='__main__':test()
