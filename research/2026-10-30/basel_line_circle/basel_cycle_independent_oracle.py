"""Separate SymPy/mpmath oracle for Basel/native-source arithmetic circle.

This is a finite observer model, not a BBP digit/GR/normality theorem.
Requires sympy and mpmath; independent expanded source exercised locally.
"""
import sympy as s
import mpmath as mp

a,n,z=s.symbols('a n z',positive=True)
R=4/a-2/(a+3)-1/(a+4)-1/(a+5)
w=s.factor(a*a*R/15)
lp=(121+s.sqrt(241))/30
lm=(121-s.sqrt(241))/30
assert s.simplify(w-a*(a+lp)*(a+lm)/((a+3)*(a+4)*(a+5)))==0
tau=w-1
D=s.factor(-tau*(n*n-1)/(12*n*(1+tau*(n-1)/n)))
assert s.limit(D.subs(a,8*n-7),n,s.oo)==s.Rational(59,1440)
mut=a/(a+3)
Dm=s.factor(-(mut-1)*(n*n-1)/(12*n*(1+(mut-1)*(n-1)/n)))
assert s.limit(Dm.subs(a,8*n-7),n,s.oo)==s.Rational(1,32)

q=(s.Rational(1,8),(151+s.sqrt(241))/240,(151-s.sqrt(241))/240)
r=(s.Rational(1,2),s.Rational(5,8),s.Rational(3,4))
co=(s.Rational(15,32),(2651-19*s.sqrt(241))/231360,
    (2651+19*s.sqrt(241))/231360)
assert s.simplify(sum(q)-sum(r))==-s.Rational(59,120)
assert s.simplify(sum(co)-s.Rational(59,120))==0
assert s.simplify(1/w-1-sum(v/(n-1+t) for v,t in zip(co,q)).subs(n,(a+7)/8))==0

for N in range(3,8):
    weights=[s.Rational(i+2,i+1) for i in range(N)]
    B=s.zeros(N,N)
    for i in range(N-1):
        B[i,i]=1
        B[i,i+1]=-1
    B[N-1,N-1]=1
    B[N-1,0]=-z
    H=B.T.subs(z,1/z)*s.diag(*weights)*B
    assert s.simplify(H.det()-s.prod(weights)*(2-z-1/z))==0

mp.mp.dps=65
qq=[mp.mpf(str(s.N(x,70))) for x in q]
rr=[mp.mpf(str(s.N(x,70))) for x in r]
cc=[mp.mpf(str(s.N(x,70))) for x in co]
constant=mp.fprod(mp.gamma(x) for x in rr)/mp.fprod(mp.gamma(x) for x in qq)
renorm=-mp.fsum(b*mp.digamma(x) for b,x in zip(cc,qq))
assert abs(constant-mp.mpf('0.2005503081493097580951525434314'))<mp.mpf('1e-31')
assert abs(renorm-mp.mpf('3.9660550275954530132984554216965'))<mp.mpf('1e-31')

for N in (10,100,1000):
    W=mp.fprod(mp.gamma(N+x)/mp.gamma(x) for x in qq)*mp.fprod(mp.gamma(x)/mp.gamma(N+x) for x in rr)
    assert abs(W/(constant*N**(-mp.mpf(59)/120))-1)<mp.mpf(2)/N
    excess=mp.fsum(b*(mp.digamma(N+x)-mp.digamma(x)) for b,x in zip(cc,qq))
    assert abs(excess-mp.mpf(59)/120*mp.log(N)-renorm)<mp.mpf(1)/N

lam=2/(1+mp.sqrt(5))
assert abs((1-mp.euler)-(1+lam)**(-2)-(lam-mp.euler))<mp.mpf('1e-60')
assert abs(mp.polygamma(1,2)-(mp.zeta(2)-1))<mp.mpf('1e-60')
for t in (mp.mpf(1)/7,mp.mpf(2)/9):
    rhs=1/(mp.gamma(1+t)*mp.gamma(1-t))
    assert abs(rhs-mp.sin(mp.pi*t)/(mp.pi*t))<mp.mpf('1e-60')
print("Independent symbolic/Gamma/Basel/source oracle PASS")
print("C_w =",mp.nstr(constant,40))
print("C_res =",mp.nstr(renorm,40))
