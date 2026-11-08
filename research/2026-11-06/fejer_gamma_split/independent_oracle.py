"""Independent exact rational + Gaussian integer test (does not import series_split)."""
from fractions import Fraction as F
import json

# Rational complex (pair) arithmetic is implemented independently of the finite Fourier code.
def mult(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def add(a,b): return(a[0]+b[0],a[1]+b[1])
def sq(a):return a[0]*a[0]+a[1]*a[1]

def run():
    checks=0
    for Q in (2,4,8):
        for M in (1,2,3,5,7):
            phases=[(F(((n*n+3*n+1)%7)-3,4), F(((3*n*n+2)%9)-4,8)) for n in range(Q*M)]
            fibers=[]
            for a in range(Q):
                v=(F(),F())
                for t in range(M):v=add(v,phases[a+t*Q])
                fibers.append((v[0]/M,v[1]/M))
            direct=sum((sq(v) for v in fibers),F())/Q
            double=F()
            for a in range(Q):
                for t in range(M):
                    for s in range(M):
                        product=mult(phases[a+t*Q],conj(phases[a+s*Q]))
                        double+=product[0]/(Q*M*M)
            assert direct==double
            # Parallelogram identity exact, and martingale energy increments exact.
            mean=(sum((x[0] for x in phases),F())/(Q*M),sum((x[1] for x in phases),F())/(Q*M))
            between=sum((sq((x[0]-y[0],x[1]-y[1])) for x in fibers for y in fibers),F())/(2*Q*Q)
            within=sum((sq((phases[a+t*Q][0]-phases[a+s*Q][0],phases[a+t*Q][1]-phases[a+s*Q][1]))
                        for a in range(Q) for t in range(M) for s in range(M)),F())/(2*Q*M*M)
            total=sum((sq(x) for x in phases),F())/(Q*M)
            assert sq(mean)+between+within==total
            assert direct==sq(mean)+between
            checks+=3
    # Independent source oracle: combined polynomial A/D, not the main four-fraction function.
    def source(n):
        return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    for p,n,L,left,right in ((149,19,37,F(45,100),F(46,100)),
                              (257,33,4,F(42,100),F(43,100))):
        state=F(); stored={0:state}
        for j in range(1,n+L+1):
            state=(16*state+source(j))%1
            stored[j]=state
        assert pow(16,L,p)==1
        assert source(n).denominator%p==0
        assert all(source(j).denominator%p for j in range(n+1,n+L+1))
        delta=stored[n+L]-stored[n]
        assert delta.denominator%p!=0
        distance=min(delta%1,(-delta)%1)
        assert left<distance<right
        checks+=1
    print(json.dumps({'independent_exact_rational_checks':checks,'cases':17,'result':'PASS'}))

if __name__=='__main__':run()
