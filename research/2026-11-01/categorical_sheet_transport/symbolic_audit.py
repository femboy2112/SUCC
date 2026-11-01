"""Optional independent SymPy audit of the source-cover and delay identities.

Not required by the stdlib tests. No finite sampling is promoted to an
all-horizon proof: symbolic residuals are rational-function identities.
"""
import importlib.util
import json
from pathlib import Path
import sys
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cst_symbolic_ops',HERE/'sheet_transport.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
z,u,v,t=s.symbols('z u v t')
A=(8*z-7)**4;D=(8*z-4)**2*(8*z-3)*(8*z-2);R=A/D
r=4/(8*z-7)-2/(8*z-4)-1/(8*z-3)-1/(8*z-2)
a=sum(c*u**i*v**j for i,j,c in m.A_TERMS)
b=sum(c*u**i*v**j for i,j,c in m.B_TERMS)
curve=sum(c*u**i*v**j for i,j,c in m.CURVE_TERMS)
p=A-u*D;q=A.subs(z,z+1)-v*D.subs(z,z+1)
sub=s.subresultants(p,q,z)
class Checks(dict):
    def __setitem__(self,key,value):
        print(key,value,file=sys.stderr,flush=True)
        super().__setitem__(key,bool(value))
checks=Checks()
checks['original_dlog']=s.cancel(s.diff(R,z)/(8*R)-r)==0
checks['subresultant_linear']=s.expand(sub[-2]-2**42*(8*a*z+b))==0
checks['resultant_curve']=s.Poly(sub[-1],u,v).primitive()[1].as_expr()==curve
checks['inverse_rational_identity']=s.factor(s.together((8*a*z+b).subs({u:R,v:R.subs(z,z+1)})))==0
checks['non_descent_derivative']=s.diff(R,z).subs(z,-s.Rational(1,8))==s.Rational(59392,1125)
disc=s.factor(s.discriminant(p,z))
checks['quartic_discriminant']=disc==5566277615616*u**3*(32*u**2-2507*u-18432000)
checks['branch_values_distinct']=s.discriminant(32*u**2-2507*u-18432000,u)!=0
T=-s.I*(R-1)/(R+1)
checks['circle_angular_pullback']=s.factor(s.together(s.I*s.diff(T,z)/(4*(1+T**2))-r))==0
# Trace identity: sum_i 1/(z_i-1)=-p_z(1)/p(1), away from exceptional fibers.
trace=-s.diff(p,z).subs(z,1)/p.subs(z,1)
pushed=trace/(128*u)
checks['first_contour_pushforward']=s.cancel(pushed-(208*u-2)/(8*u*(1-480*u)))==0
checks['first_contour_residue']=s.residue(pushed,u,s.Rational(1,480))==s.Rational(47,240)
num=s.fraction(s.cancel(a.subs({u:R,v:R.subs(z,z+1)})))[0]
coeffs=s.Poly(num.subs(z,t+1),t).all_coeffs()
checks['positive_time_inverse_chart']=len(coeffs)==19 and all(c>0 for c in coeffs)
checks['curve_irreducible_Q']=len(s.factor_list(curve)[1])==1 and s.factor_list(curve)[1][0][1]==1
# Marked frame g(z)=(z-1)/(z+1); g S g^-1 is not S.
g=lambda z:(z-1)/(z+1)
gi=lambda w:(1+w)/(1-w)
w=s.symbols('w')
sg=s.cancel(g(gi(w)+1))
checks['frame_conjugacy']=s.cancel(sg.subs(w,g(z))-g(z+1))==0
checks['frame_is_not_fixed_source_symmetry']=s.cancel(sg-(w+1))!=0
result={'sympy_version':s.__version__,'checks':checks,'passed':sum(checks.values()),
        'total':len(checks),'discriminant':str(disc),'frame_successor':str(sg),
        'scope':'exact polynomial/rational identities; no Lean or normality proof'}
print(json.dumps(result,indent=2))
if not all(checks.values()):raise SystemExit(1)
