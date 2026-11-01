"""Exact original-source cover audit; polynomial certificates, no float decisions."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

def main():
    z,u,v=s.symbols('z u v')
    A=s.Poly((8*z-7)**4,z); D=s.Poly((8*z-4)**2*(8*z-3)*(8*z-2),z)
    A1=s.Poly(A.as_expr().subs(z,z+1),z); D1=s.Poly(D.as_expr().subs(z,z+1),z)
    R=A.as_expr()/D.as_expr()
    r=4/(8*z-7)-2/(8*z-4)-1/(8*z-3)-1/(8*z-2)
    t=-s.I*(R-1)/(R+1)
    f=A.as_expr()-u*D.as_expr(); g=A1.as_expr()-v*D1.as_expr()
    subs=s.subresultants(f,g,z)
    linear=next(s.Poly(p,z) for p in subs if s.degree(p,z)==1)
    a=s.Poly(linear.coeff_monomial(z),u,v); b=s.Poly(linear.coeff_monomial(1),u,v)
    common=s.gcd(a.content(),b.content()); a=s.Poly(a.as_expr()/common,u,v); b=s.Poly(b.as_expr()/common,u,v)
    def lift(poly):
        out=s.Poly(0,z)
        for (i,j),coef in poly.terms():
            out+=coef*A**i*D**(3-i)*A1**j*D1**(3-j)
        return out
    # Clearing denominators BEFORE expanding prevents rational-expression swell.
    lifted_a,lifted_b=lift(a),lift(b)
    inverse_identity=(s.Poly(z,z)*lifted_a+lifted_b).is_zero
    generic_den_not_zero=not lifted_a.is_zero
    # Cross-check reconstruction at fresh positive, negative and fractional z.
    points=[s.Rational(k,3) for k in range(-13,30) if k not in []]
    checked=[]
    for x in points:
        if D.eval(x)==0 or D1.eval(x)==0: continue
        uv={u:A.eval(x)/D.eval(x),v:A1.eval(x)/D1.eval(x)}
        av=a.as_expr().subs(uv);bv=b.as_expr().subs(uv)
        if av:
            assert s.cancel(-bv/av)==x
            checked.append(str(x))
    disc=s.factor(s.discriminant(f,z))
    rho=s.factor(s.diff(R,z)/(8*R)-r)
    cayley=s.factor(s.I/8*2*s.diff(t,z)/(1+t*t)-r)
    rel=s.Poly(subs[-1],u,v); rel=rel.primitive()[1]
    # Independent elimination determinant, distinct algorithm from subresultants.
    syl=s.zeros(8)
    cf=s.Poly(f,z).all_coeffs();cg=s.Poly(g,z).all_coeffs()
    for i in range(4):
        for j,c in enumerate(cf):syl[i,i+j]=c
        for j,c in enumerate(cg):syl[4+i,i+j]=c
    det_samples=[]
    for uv in [(0,0),(1,1),(2,3),(-2,5),(7,-11)]:
        data={u:uv[0],v:uv[1]}
        det=syl.subs(data).det(); res=subs[-1].subs(data)
        assert det==res
        det_samples.append([*uv,str(det)])
    result={
        'status':'EXACT_POLYNOMIAL_AUDIT', 'sympy_version':s.__version__,
        'dlog_zero':rho==0,'cayley_pullback_zero':cayley==0,
        'discriminant':str(disc),
        'critical_derivative':str(s.factor(s.diff(R,z))),
        'unique_order4_zero':'z=7/8',
        'shifted_zero':'z=-1/8',
        'R_derivative_at_shifted_zero':str(s.factor(s.diff(R,z).subs(z,-s.Rational(1,8)))),
        'linear_subresultant_common_factor_removed':str(common),
        'inverse_numerator_terms':[[list(p),str(-c)] for p,c in b.terms()],
        'inverse_denominator_terms':[[list(p),str(c)] for p,c in a.terms()],
        'cleared_inverse_identity_zero':inverse_identity,
        'inverse_denominator_not_identically_zero':generic_den_not_zero,
        'lifted_inverse_denominator_factorization':str(s.factor(lifted_a.as_expr())),
        'delay_curve_degrees':[rel.degree(u),rel.degree(v)],
        'all_horizon_inverse_chart': {
            'denominator_at_source_zero':str(lifted_a.eval(0)),
            'shifted_cleared_denominator_coefficients_ascending':[str(x) for x in reversed(s.Poly(lifted_a.as_expr().subs(z,z+1),z).all_coeffs())],
            'all_strictly_positive':all(x>0 for x in s.Poly(lifted_a.as_expr().subs(z,z+1),z).all_coeffs()),
            'scope':'z=0 and all real z>=1; source integer n>=0'
        },
        'delay_curve_terms':[[list(p),str(c)] for p,c in rel.terms()],
        'rational_reconstruction_samples':checked,
        'sylvester_determinant_samples':det_samples,
    }
    assert all([rho==0,cayley==0,inverse_identity,generic_den_not_zero])
    dest=Path(__file__).resolve().parent/'receipts'/'cover_certificate.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if 'terms' not in k and 'samples' not in k},indent=2))
if __name__=='__main__':main()
