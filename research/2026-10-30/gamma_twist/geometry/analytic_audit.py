"""Additional hostile and analytic checks, independent of geometry_probe."""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as s
import mpmath as mp

mp.mp.dps=80
root=Path(__file__).resolve().parent
x,n,z=s.symbols('x n z',positive=True)
u=s.symbols('u',positive=True)
A=s.Rational(151,240);B=s.Rational(403,1920)
# Exact Mellin differentiation: normalized source expansion before selecting
# s=0 gives the first two log moments, independently of the paper's digamma list.
v=s.symbols('v')
mellin=(s.gamma(v+2)+u*A*s.gamma(v+3)+u*u*B*s.gamma(v+4))/(1+2*A*u+6*B*u*u)
logjet=s.series(s.diff(mellin,v).subs(v,0)+s.log(1-s.Rational(7,8)*u),u,0,3).removeO()
assert s.simplify(logjet.coeff(u,1)+s.Rational(59,240))==0
assert s.simplify(logjet.coeff(u,2)+s.Rational(3601,28800))==0
alpha=-s.Rational(1231,240)+s.Rational(2671,1200)*s.sqrt(5)
beta=s.Rational(6031,80)-s.Rational(12139211,360000)*s.sqrt(5)
omega2=s.simplify(-s.Rational(3601,28800)-beta)
assert s.simplify(omega2-(-s.Rational(2174761,28800)+s.Rational(12139211,360000)*s.sqrt(5)))==0

qpoly=4-2*x**3-x**4-x**5
same=2+s.Rational(11,4)*x**3-s.Rational(1,2)*x**4-s.Rational(17,4)*x**5
assert s.div(same,1-x)[1]==0
samequot=s.Poly(s.div(same,1-x)[0],x)
assert all(v>0 for v in samequot.all_coeffs())
mutants={
 'authentic':(4,-2,-1,-1),
 'wrong_ratio':(5,-2,-1,-1),
 'same_ratio_rank1':(4,0,-1,0),
 'same_ratio_rank2':(s.Rational(2),s.Rational(11,4),s.Rational(-1,2),s.Rational(-17,4)),
 'age_t128':(132,-386,127,127),
}
source_rows=[]
for label,cs in mutants.items():
    kernel=sum(c*s.exp(-d*x) for d,c in zip((0,3,4,5),cs))
    jets=[s.diff(kernel,x,j).subs(x,0) for j in range(4)]
    src=sum(c/(8*n-7+d) for d,c in zip((0,3,4,5),cs))
    source_rows.append(dict(source=label,jets=list(map(str,jets)),source17=str(src.subs(n,17)),
                            J_fixed=bool(cs[0]==-4*cs[2])))
assert source_rows[1]['J_fixed'] is False
assert source_rows[2]['J_fixed'] is True
assert source_rows[3]['jets'][:2]==['0','15']
assert source_rows[3]['jets'][2]!='-59'

# Matrix commutator route, independent from pointwise affine composition.
a,b=s.symbols('a b')
Ma=s.Matrix([[16,a],[0,1]]);Mb=s.Matrix([[16,b],[0,1]])
comm=s.simplify(Ma*Mb*Ma.inv()*Mb.inv())
assert comm==s.Matrix([[1,15*(b-a)],[0,1]])

# Direct log observer special-function formula and positive quadrature.
raw=json.loads((root/'receipts/exact-probe.log').read_text())
obs=[]
for nn in (17,31,53,89):
    aa=8*nn-7
    cs=(4,-2,-1,-1);ds=(0,3,4,5)
    rr=sum(mp.mpf(c)/(aa+d) for c,d in zip(cs,ds))
    logexact=-mp.euler-sum(mp.mpf(c)*mp.log1p(mp.mpf(d)/aa)/(aa+d) for c,d in zip(cs,ds))/rr
    if nn in (17,89):
        qfun=lambda yy:2*(-mp.expm1(-3*yy/aa))+(-mp.expm1(-4*yy/aa))+(-mp.expm1(-5*yy/aa))
        integral=mp.quad(lambda yy:mp.exp(-yy)*qfun(yy)*mp.log(yy)/(aa*rr),[0,1,4,16,mp.inf])
        assert abs(logexact-integral)<mp.mpf('1e-65')
    r=next(v for v in raw['root_enclosures'] if v['n']==nn and v['source']=='authentic')
    lo,hi=F(r['lower']),F(r['upper'])
    qr=(mp.mpf(lo.numerator)/lo.denominator+mp.mpf(hi.numerator)/hi.denominator)/2
    lam=(mp.sqrt(5)-1)/2
    omega=logexact-qr
    omega1=mp.mpf(293)/60-mp.mpf(2671)/1200*mp.sqrt(5)
    pred2=-mp.mpf(2174761)/28800+mp.mpf(12139211)/360000*mp.sqrt(5)
    scaled=nn*nn*(omega-(lam-mp.euler)-omega1/nn)
    obs.append(dict(n=nn,log_observer=mp.nstr(logexact,35),omega=mp.nstr(omega,35),
                    omega_scaled_second=mp.nstr(scaled,30),predicted_second=mp.nstr(pred2,30),
                    second_residual=mp.nstr(scaled-pred2,25)))

# A genuine fractional periodic gauge destroys eventual log-convexity; old
# functional ratio and all integer samples remain identical. Numerical check
# is a witness calibration; the theorem uses periodicity and a limiting proof.
curvature=[]
for tt,eps in ((mp.mpf('50.5'),mp.mpf(1)),(mp.mpf('1000.5'),mp.mpf('0.000001'))):
    curv=sum(c*mp.polygamma(1,tt+mp.mpf(d)/8) for c,d in zip((4,-2,-1,-1),(1,4,5,6)))
    gauge_curv=curv-2*eps*mp.pi**2
    assert curv>0 and gauge_curv<0
    curvature.append(dict(t=mp.nstr(tt),epsilon=mp.nstr(eps),authentic=mp.nstr(curv,35),
                          perturbed=mp.nstr(gauge_curv,35)))

# Divisor orders have integer residues. Exact exponentiated monodromy is 1;
# a half-rank reweighting at a simple zero would instead change the object.
orders={s.Rational(-1,8):-4,s.Rational(-1,2):2,s.Rational(-5,8):1,s.Rational(-3,4):1}
for center,order in orders.items():
    assert s.exp(2*s.pi*s.I*order)==1
assert s.exp(s.pi*s.I)==-1

print(json.dumps(dict(status='PASS',authority='exact algebra plus labeled numerical holdouts',
    source_mutants=source_rows,log_first=str(logjet.coeff(u,1)),log_second=str(logjet.coeff(u,2)),
    omega_second=str(omega2),omega_holdouts=obs,periodic_gauge_curvature=curvature,
    affine_matrix_commutator=str(comm),gamma_divisor_orders={str(k):v for k,v in orders.items()},
    gamma_multiplicative_monodromy='1',half_rank_simple_zero_monodromy='-1, changed auxiliary object'),indent=2))
