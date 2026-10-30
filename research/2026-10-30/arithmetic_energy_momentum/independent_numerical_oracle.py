"""Separate mpmath quadrature of original four-pole source and its clock mass.
Numbers are high-precision *holdouts*, not universal proof certificates.
"""
import mpmath as mp
mp.mp.dps=65

def Q(x):return -2*mp.expm1(-3*x)-mp.expm1(-4*x)-mp.expm1(-5*x)
def R(a):return 4/a-2/(a+3)-1/(a+4)-1/(a+5)
def check(a):
 a=mp.mpf(a)
 # Use the physical positive integrand, independent of the rational formula.
 f=lambda x:mp.exp(-a*x)*Q(x)
 knots=[0,1/a,4/a,16/a,mp.inf]
 moments=[mp.quad(lambda x, k=k: x**k*f(x),knots) for k in (0,1,2)]
 z,ex1,ex2=moments
 assert mp.almosteq(z,R(a),rel_eps=mp.mpf('1e-48'))
 mean=ex1/z; var=ex2/z-mean**2
 M=a*mean; rho=mean**2/var
 assert 1<M<2 and 1<rho<2
 tp=mp.mpf('0.5')*mp.phi**2
 tm=mp.mpf('0.5')/mp.phi**2
 E=a*mean*(tp+tm)
 P=a*mean*(tp-tm)
 C=tp*tm*a*a*var
 assert mp.almosteq(E*E-P*P,M*M,rel_eps=mp.mpf('1e-43'))
 assert mp.almosteq(E*E-P*P,4*rho*C,rel_eps=mp.mpf('1e-43'))
 print(f'a={int(a):>5}  M(a)={mp.nstr(M,21)}  rho(a)={mp.nstr(rho,21)}  boosted E^2-P^2={mp.nstr(E*E-P*P,21)}')

for a in (1,9,17,73,257):check(a)
lam=1/mp.phi
zp=1-lam**3
zm=-lam
thp=mp.phi**2/2
thm=lam**2/2
d=1+thp*(1-zp)+thm*(1-zm)
assert mp.almosteq(d,mp.phi,rel_eps=mp.mpf('1e-60'))
assert mp.almosteq(d**-2,lam**2,rel_eps=mp.mpf('1e-60'))
print('exact golden dual-laplace identity checked at 65 decimal precision')
print('INDEPENDENT QUADRATURE ORACLE PASSED')
