"""Optional independent SymPy exact rational/digamma audit; not a Lean certificate."""
import sympy as s
z=s.symbols('z')
a=[s.Rational(1,8),s.Rational(1,2),s.Rational(5,8),s.Rational(3,4)]
c=[4,-2,-1,-1]
d=[s.Rational(c[i])*(1-a[i]) for i in range(4)]
r=(120*z*z-89*z+16)/((2*z-1)*(4*z-1)*(8*z-7)*(8*z-3))
assert s.factor(r-sum(s.Rational(c[i],8)/(z-1+a[i]) for i in range(4)))==0
assert s.simplify(sum(d)/8-s.Rational(15,64))==0
r_difference=s.factor(z*r-s.Rational(15,64)/z)
assert s.together(r_difference-(9664*z**3-9656*z**2+3090*z-315)/(64*z*(2*z-1)*(4*z-1)*(8*z-7)*(8*z-3)))==0
K=s.expand_func(-sum(d[i]*s.digamma(a[i]) for i in range(4))/8)
silver=(s.Rational(27,128)+s.Rational(31,128)*s.sqrt(2))*s.pi+s.Rational(39,32)*s.log(2)+s.Rational(31,64)*s.sqrt(2)*s.log(1+s.sqrt(2))
B=s.expand(K-s.Rational(15,64)*s.EulerGamma)
# Strictly positive real log ratio, sqrt(2): CAS's raw log is simplified by exact real-log law.
raw_log=s.Rational(31,128)*s.sqrt(2)*s.log((2+s.sqrt(2))/(2-s.sqrt(2)))
assert s.simplify((2+s.sqrt(2))/(2-s.sqrt(2))-(1+s.sqrt(2))**2)==0
Braw=(s.Rational(27,128)+s.Rational(31,128)*s.sqrt(2))*s.pi+s.Rational(39,32)*s.log(2)+raw_log
assert s.simplify(s.expand_log(B,force=True)-s.expand_log(Braw,force=True))==0
# The verified positive ratio identity implies log(ratio)=2log(1+sqrt(2)); no forced CAS logcombine.
print('PASS exact original 4-pole rational identity')
print('PASS first-moment rational coefficient 15/64')
print('PASS positive-difference numerator polynomial')
print('PASS complete weighted digamma identity and gamma coefficient')
print('PASS exact silver-ratio residual with real-log positive arguments')
print('B =',s.N(B,40))
