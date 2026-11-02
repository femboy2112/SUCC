import sympy as s
z,u,v=s.symbols('z u v')
A=(8*z-7)**4;D=(8*z-4)**2*(8*z-3)*(8*z-2);R=A/D
r=4/(8*z-7)-2/(8*z-4)-1/(8*z-3)-1/(8*z-2)
t=-s.I*(R-1)/(R+1)
print('dlog:',s.factor(s.diff(R,z)/(8*R)-r))
print('pullback:',s.factor(s.I/8*2*s.diff(t,z)/(1+t*t)-r))
print('critical:',s.factor(s.diff(R,z)))
print('discriminant:',s.factor(s.discriminant(A-u*D,z)))
print('R(-1/8),derivative:',s.factor(R.subs(z,-s.Rational(1,8))),s.factor(s.diff(R,z).subs(z,-s.Rational(1,8))))
print('translation resultants start',flush=True)
f=A-u*D;g=A.subs(z,z+1)-v*D.subs(z,z+1)
rel=s.factor(s.resultant(f,g,z));print('rel:',rel,flush=True)
subs=s.subresultants(f,g,z)
for poly in subs:
 print('subresultant degrees',s.degree(poly,z),len(str(poly)),flush=True)
linear=[p for p in subs if s.degree(p,z)==1][0]
print('linear subresultant:',s.factor(linear),flush=True)
a=s.factor(s.Poly(linear,z).coeff_monomial(z));b=s.factor(s.Poly(linear,z).coeff_monomial(1))
print('inverse z num:',s.factor(-b));print('inverse z den:',a)
print('exact inverse composition:',s.cancel((-b-z*a).subs({u:R,v:R.subs(z,z+1)})),flush=True)
