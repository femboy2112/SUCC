"""Independent symbolic + high-precision checks of the two-triangle Fourier source.
Independent from the exact-rational module's implementation; raw validation.
"""
import sympy as S
import mpmath as mp
from fractions import Fraction
from math import gcd

z,w,u=S.symbols('z w u')
d=3-z-w
J=S.factor(-S.Rational(151,120)*(d-1)/d**3+3*(z*(1-z)+w*(1-w))/d**4)
Jpoly=(-511*z**2-511*w**2-302*z*w+1115*(z+w)-906)/(120*d**4)
assert S.simplify(J-Jpoly)==0
parent=(-511*z**2+813*z-302)/(120*(2-z)**4)
assert S.factor(J.subs(w,1)-parent)==0
fake_delta=S.factor(S.Rational(59,120)*(d-1)/d**3)
assert S.factor(fake_delta.subs(w,1)-S.Rational(59,120)*(1-z)/(2-z)**3)==0
assert S.diff(1/d**2,z,w).subs({z:1,w:1})==6
assert S.diff(1/d**2,z).subs({z:1,w:1})==2
assert S.expand((3-z-w)**2)==9-6*z-6*w+z*z+2*z*w+w*w
# Separate ring-algebra exact 36x36 inverse independent of primary Fraction oracle.
A=S.zeros(36)
for j in range(6):
 for k in range(6):
  col=6*j+k
  A[col,col]+=3
  A[6*((j+1)%6)+k,col]-=1
  A[6*j+(k+1)%6,col]-=1
v=S.zeros(36,1);v[0]=1
res=A.inv()*A.inv()*v
p11=sum(res[6*j+k] for j in (1,5) for k in (1,5))
p=sum(res[6*j+k] for j in (1,5) for k in range(6))
assert p11==S.Rational(6533558611,64571925600)
assert p==S.Rational(416,1323)
assert p11-p**2==S.Rational(197519239153,85428657568800)

mp.mp.dps=75

def R(a,fake=False):
 a=mp.mpf(a)
 return mp.mpf(15)/a**2 if fake else mp.mpf(4)/a-mp.mpf(2)/(a+3)-1/(a+4)-1/(a+5)

def H(n,z,w,fake=False):
 a=mp.mpf(8*n-7)
 z,w=mp.mpf(str(z)),mp.mpf(str(w))
 den=R(a,fake)
 def integrand(y):
  x=y/a
  if fake:Q=15*x
  else:
   ex=mp.exp(-x)
   Q=(1-ex)*(4+4*ex+4*ex**2+2*ex**3+ex**4)
  ell=mp.exp(-8*x)
  return mp.exp(-y)*Q/(a*den)*(z+(1-z)*ell)**n*(w+(1-w)*ell)**n
 return mp.quad(integrand,[0,3,15,45,120,mp.inf])

values=[]
for z0,w0 in [('0','0'),('0.5','0.25'),('0.75','0.66666666666666666666666666666666666666666666666666667')]:
 zv=S.Rational(z0);wv=S.Rational(w0);j=S.N(J.subs({z:zv,w:wv}),35)
 j_mp=mp.mpf(str(j))
 for n in (30,90,270):
  orig=H(n,z0,w0)
  fake=H(n,z0,w0,True)
  base=1/(mp.mpf(3)-mp.mpf(z0)-mp.mpf(w0))**2
  obs=n*(orig-base)
  predicted=mp.mpf(str(S.N(J.subs({z:zv,w:wv}),65)))
  delta_pred=mp.mpf(str(S.N(fake_delta.subs({z:zv,w:wv}),65)))
  delta_obs=n*(orig-fake)
  assert abs(obs-predicted)<mp.mpf('3')/n
  assert abs(delta_obs-delta_pred)<mp.mpf('3')/n
  values.append((z0,w0,n,mp.nstr(obs,16),mp.nstr(predicted,16),mp.nstr(delta_obs,16),mp.nstr(delta_pred,16)))
print('SYMPY EXACT: two-variable jet, single-slice, source fingerprint, q6 full rational cyclic ring, multiplier stencil PASS')
print('HIGH PRECISION SOURCE HOLDOUTS (n*(H_n-H_inf), predicted J, n*(orig-fake), predicted source difference)')
for v in values:print(' '.join(map(str,v)))
print('q6 p11',p11,'covariance',p11-p**2,'decimal',S.N(p11-p**2,20))
