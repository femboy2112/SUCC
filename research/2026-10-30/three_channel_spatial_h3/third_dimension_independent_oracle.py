"""Independent symbolic and quadrature source controls for SUCC 3-channel H3.

Not part of the stdlib exact-unit-test implementation. Uses SymPy/mpmath.
"""
import sympy as S
import mpmath as mp

A,d,t=S.symbols('A d t',positive=True)
R=lambda x: 4/x-2/(x+3)-1/(x+4)-1/(x+5)
assert S.factor(R(A))==(15*A*A+121*A+240)/(A*(A+3)*(A+4)*(A+5))
q=S.series(R(1/t),t,0,5).removeO().expand()
assert q.coeff(t,2)==15 and q.coeff(t,3)==-59 and q.coeff(t,4)==243

H=S.cancel(R(A*d)/R(A))
Hfake=d**(-2)
coeff=S.simplify(S.diff(S.cancel(H.subs(A,1/t)-Hfake),t).subs(t,0))
assert S.simplify(coeff-59*(d-1)/(15*d**3))==0

# Independent 3rd cumulant from source log normalizer
assert S.simplify(-A**3*S.diff(S.log(15)-2*S.log(A)-S.Rational(59,15)/A,A,3)
                  -(4-S.Rational(118,5)/A))==0

mp.mp.dps=58
Rmp=lambda a:mp.mpf(4)/a-mp.mpf(2)/(a+3)-mp.mpf(1)/(a+4)-mp.mpf(1)/(a+5)
Qmp=lambda x:-2*mp.expm1(-3*x)-mp.expm1(-4*x)-mp.expm1(-5*x)
zs=[mp.mpf('0.4'),mp.mpf('0.7'),mp.mpf('0.9')]
C=sum(1-z for z in zs);den=1+C
asym=mp.mpf(59)*C/(120*den**3)
errs=[]
for n in (30,100,300):
    a=8*n-7
    likelihood=lambda y:mp.fprod(z+(1-z)*mp.exp(-8*y/a) for z in zs)**n
    original=mp.quad(lambda y:mp.exp(-y)*likelihood(y)*Qmp(y/a)/a/Rmp(a),[0,mp.inf])
    fake=mp.quad(lambda y:mp.exp(-y)*likelihood(y)*y,[0,mp.inf])
    err=abs(n*(original-fake)-asym)
    errs.append(err)
    print('n=',n,'original-minus-fake scaled',mp.nstr(n*(original-fake),22),'jet error',mp.nstr(err,13))
assert errs[0]>errs[1]>errs[2] and errs[2]<mp.mpf('0.00004')

L=(mp.sqrt(5)-1)/2
for theta in (1,3):
    c=1+theta
    Z=1-mp.euler+mp.log(c)-(1+c*L)**(-2)
    mean=theta*(3-2*mp.euler+2*mp.log(c)-2*(1+c*L)**(-3))/Z
    total=mp.mpf(0);ms=mp.mpf(0)
    for s in range(300):
        D=mp.digamma(s+2)-(L**(s+2))
        prob=(s+1)*mp.mpf(theta)**s/(c**(s+2))
        total+=prob*D
        ms+=s*prob*D
    assert abs(total-Z)<mp.mpf('1e-28')
    assert abs(ms/total-mean)<mp.mpf('1e-24')
    print('clock',theta,'Oily Z',mp.nstr(Z,20),'mean',mp.nstr(mean,20))

# Three source atoms generate a nontrivial angular drift with coefficient 164/225.
beta=[S.Rational(6,15),S.Rational(4,15),S.Rational(5,15)]
shifts=[3,4,5]
mean_shift=sum(b*d for b,d in zip(beta,shifts))
var_shift=sum(b*(d-mean_shift)**2 for b,d in zip(beta,shifts))
assert mean_shift==S.Rational(59,15)
assert var_shift==S.Rational(164,225)
print('angular shift variance exact =',var_shift,'rank2 metric coefficient=',2*var_shift)
print('Independent symbolic and quadrature oracle PASS')

# Source-native fixed-budget angular contact step is summable as n increases.
source_marks=lambda a:[mp.mpf(c*d)/(a*(a+d)*Rmp(a)) for c,d in ((2,3),(1,4),(1,5))]
angular_target=mp.sqrt(82)/60
angular_errors=[]
for n in (20,100,1000):
    p=source_marks(8*n-7);q=source_marks(8*n+1)
    affinity=sum(mp.sqrt(x*y) for x,y in zip(p,q))
    distance=2*mp.sqrt(2)*mp.acos(min(mp.mpf(1),affinity))
    angular_errors.append(abs(n*n*distance-angular_target))
    print('n=',n,'n² angular Fisher step',mp.nstr(n*n*distance,23))
assert angular_errors[0]>angular_errors[1]>angular_errors[2]
assert angular_errors[2]<mp.mpf('0.00005')
