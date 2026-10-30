"""Independent SymPy exact source/carry oracle (does not import implementation)."""
from __future__ import annotations
from fractions import Fraction
from math import comb, factorial
import sympy as S

COUNTS={}
def check(x, group):
    if x is not True and x != True:
        raise AssertionError(f'{group}: {x!r}')
    COUNTS[group]=COUNTS.get(group,0)+1

a=S.symbols('a',positive=True)
u=S.symbols('u',real=True)
z=S.symbols('z',real=True)
I=S.I
po=((0,4),(3,-2),(4,-1),(5,-1))
R=lambda x:4/x-2/(x+3)-1/(x+4)-1/(x+5)
Q=lambda x:4-2*S.exp(-3*x)-S.exp(-4*x)-S.exp(-5*x)
alpha=(121-S.sqrt(241))/30
beta=(121+S.sqrt(241))/30
check(S.simplify(R(a)-15*(a+alpha)*(a+beta)/(a*(a+3)*(a+4)*(a+5)))==0,'source_factor')
check(S.simplify(alpha+beta-S.Rational(121,15))==0,'source_roots')
check(S.simplify(alpha*beta-16)==0,'source_roots')
check(S.simplify(S.diff(Q(z),z,2).subs(z,0)+59)==0,'authentic_second_jet')
B=lambda x:1+S.exp(-3*x)+S.exp(-4*x)+S.exp(-5*x)-S.exp(-alpha*x)-S.exp(-beta*x)
check(S.simplify(B(0)-2)==0,'levy_density_jet')
check(S.simplify(S.diff(B(z),z).subs(z,0)+S.Rational(59,15))==0,'levy_density_jet')
# Source Fourier limit with exact symbolic rational coefficient in u=1/a.
w=1-I*z
Ru=lambda ww: (15*ww**2+121*ww*u+240*u**2)/(ww*(ww+3*u)*(ww+4*u)*(ww+5*u))
phi=S.factor(Ru(w)/Ru(1))
base=S.factor(phi.subs(u,0))
first=S.factor(S.diff(phi,u).subs(u,0))
check(S.simplify(base-1/w**2)==0,'fourier_endpoint')
check(S.simplify(first-S.Rational(59,15)*(1-1/w)/w**2)==0,'fourier_first_jet')
check(S.simplify(base.subs(z,1)-I/2)==0,'fourier_right_angle')
check(S.simplify(first.subs(z,1)-S.Rational(59,60)*(1+I))==0,'fourier_right_angle')
check(S.simplify((first/base).subs(z,1)-S.Rational(59,30)*(1-I))==0,'source_log_right_angle')
check(S.simplify((first/base).subs(z,I*(S.sqrt(5)-1)/2)-S.Rational(59,15)*(1-(1+((S.sqrt(5)-1)/2))**-1))==0,'golden_log_jet')
# Source-specific inversion in logarithmic coordinates, including exact bounded twist.
source_ratio=S.factor(R(16/a)/R(a))
expected_ratio=a**3*(a+3)*(a+5)/(4*(3*a+16)*(5*a+16))
check(S.simplify(source_ratio-expected_ratio)==0,'inversion_rational')
twist=S.factor(source_ratio/(a/4)**3)
check(S.simplify(twist-16*(a+3)*(a+5)/((3*a+16)*(5*a+16)))==0,'inversion_rational')
check(S.simplify(twist*twist.subs(a,16/a)-1)==0,'inversion_odd')
check(S.factor(twist-1)==(a-4)*(a+4)/((3*a+16)*(5*a+16)),'inversion_rational')
check(S.simplify((twist-1)/(twist+1)-(a*a-16)/(31*a*a+256*a+496))==0,'inversion_tanh')
check(S.simplify(S.diff(S.log(twist),a).subs(a,4)-S.Rational(1,126))==0,'inversion_slope')
# With x=e^u, tanh(D(4x)/2)=(x^2-1)/(31x^2+64x+31).
x=S.symbols('x',positive=True)
check(S.simplify(((twist-1)/(twist+1)).subs(a,4*x)-(x*x-1)/(31*x*x+64*x+31))==0,'inversion_hyperbolic')
# Exact 16-centred hyperbolic roots and the distinct 241 vs 5 quadratic field.
check(S.simplify((alpha/4)*(beta/4)-1)==0,'logarithmic_root_twist')
check(S.simplify((alpha/4+beta/4)/2-S.Rational(121,120))==0,'logarithmic_root_twist')
check(S.simplify((beta/4-alpha/4)/2-S.sqrt(241)/120)==0,'logarithmic_root_twist')
# Gamma/Mellin order m: exact original four-pole transform and first correction.
for m in range(8):
    for q in (S.Rational(0),S.Rational(1,2),S.Rational(1)):
        wq=1+q
        A=lambda u:sum(c/(wq+S.Integer(d)*u)**(m+1) for d,c in po)
        A1=S.simplify(S.diff(A(u),u).subs(u,0))
        A2=S.simplify(S.diff(A(u),u,2).subs(u,0))
        val=S.factorial(m)*A1/15
        first_m=S.factorial(m)*(A2/2+A1*S.Rational(59,15))/15
        target=S.factorial(m+1)/wq**(m+2)
        correction=-target*S.Rational(59,30)*((m+2)/wq-2)
        check(S.simplify(val-target)==0,'mellin_gamma_moments')
        check(S.simplify(first_m-correction)==0,'mellin_first_jet')
# Actual arithmetic seed mirroring and exact centered carries.
from fractions import Fraction as F
rf=lambda n:F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
for s in (F(),F(-16),F(-1),F(1,15),F(2,7),F(1,256),F(-13,29)):
    X0=F(0);XP=s;XM=-s
    for n in range(1,31):
        r=rf(n)
        previous=X0
        X0=16*X0+r;XP=16*XP+r;XM=16*XM+r
        check(XP-X0==16**n*s,'retarded_seed_transport')
        check(XP+XM==2*X0,'mirror_phase_barycenter')
        lift=16*(previous%1)+r-(X0%1)
        check(lift.denominator==1,'integer_carry_lift')
# Hellinger midpoint exact and strict convex shape on rational holdouts.
for a0 in (F(1),F(7),F(37),F(613)):
    for t0 in (F(0),a0/3,2*a0/5):
        ra=lambda a:F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)
        H2=ra(a0)**2/(ra(a0+t0)*ra(a0-t0))
        check(0<H2<=1,'midpoint_geometry')
        if t0:
            check((1-(t0/a0)**2)**2<H2<(1-(t0/a0)**2)*(1-(t0/(a0+5))**2),'midpoint_geometry')
# Exact Haar-grid oracle for the ternary branch disagreement distribution.
# The half-cell grid misses every boundary when x is a 1/32 multiple,
# hence its counts are EXACT interval lengths, not asymptotic estimates.
for k in range(32):
    x=F(k,32)
    observed={-1:0,0:0,1:0}
    for j in range(32):
        theta=F(2*j+1,64)
        jump=((x+theta)%1)+((x-theta)%1)-2*x
        expected=int(theta>x)-int(theta>=1-x)
        check(jump==expected,'branch_shape_grid')
        observed[int(jump)]+=1
    plus=max(F(0),1-2*x)
    minus=max(F(0),2*x-1)
    for v,prob in ((-1,minus),(0,1-plus-minus),(1,plus)):
        check(F(observed[v],32)==prob,'branch_distribution_exact')
    re=(observed[0]-F(observed[-1]+observed[1],2))/32
    im=(observed[1]-observed[-1])/F(64)
    check(re==1-F(3,2)*abs(1-2*x),'q3_semantic_triangle')
    check(im==(1-2*x)/2,'q3_semantic_triangle')
    check(F(1,2)-im==x,'q3_inversion')
# Möbius-equivalent residue alias controls.
for n in range(16):
    check((16**n*(-1))%1==0 and (16**n*(-16))%1==0,'phase_alias')
    if n>=2:check((16**n*F(1,256))%1==0,'phase_alias')
print('OILY_LOG_INDEPENDENT_EXACT_PASS',sum(COUNTS.values()),sorted(COUNTS.items()))
