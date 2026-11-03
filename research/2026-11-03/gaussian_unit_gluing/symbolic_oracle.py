"""Independent SymPy reconstruction of original rational BBP atom algebra.

This is an algebraic comparison against the standard-library Q-quotient oracle;
no claim of external blind mathematical independence or normality.
"""
import sympy as s


def run():
    t,u,n,eps=s.symbols('t u n eps')
    dH=1-t*t/s.Integer(2)
    dG=1-t+t*t/s.Integer(2)
    dmin=s.expand(dH*dG)
    dcancel=s.expand((1+t*t/s.Integer(2))*(1+t+t*t/s.Integer(2)))
    P=4-2*t**3-t**4-t**5
    K=s.factor(P/(1-t**8/s.Integer(16)))
    assert s.factor(K-4*(1-t)/dmin)==0
    assert s.factor(P-4*(1-t)*dcancel)==0
    assert s.factor(K-((4-2*t)/dG-2*t/dH))==0
    m=s.expand((u*u-s.Rational(1,2))*(u*u-u+s.Rational(1,2)))
    H=s.Matrix([[s.Rational(v) for v in row] for row in (
        (4,0,0,-2),(0,0,-2,-1),(0,-2,-1,-1),(-2,-1,-1,0))])
    assert H.det()==4
    EH=s.rem((u+1)*(2*u*u-2*u+1),m,u)
    EG=s.rem(-u*(2*u*u-1),m,u)
    C=s.rem(4*u**4,m,u)
    assert s.rem(C**2-1,m,u)==0
    assert s.rem(EH**2-EH,m,u)==0
    assert s.rem(EG**2-EG,m,u)==0
    assert s.rem(EH*EG,m,u)==0
    assert s.rem(EH+EG-1,m,u)==0
    assert s.rem((2*u*u*EG)**2+EG,m,u)==0
    assert s.rem(u**8-s.Rational(1,16),m,u)==0
    W=-8*u**3+2*u*u+2*u-1
    assert s.rem((W+2*u)*EH,m,u)==0
    assert s.rem((W-2)*EG,m,u)==0
    assert s.rem(W*(-3*u**3+u*u+u/2-s.Rational(1,2))-1,m,u)==0
    # Genuine structural distinction: direct product algebra has idempotents,
    # compositum Q(sqrt2,i) is a field and is NOT the same internal algebra.
    d_int=s.discriminant(4*m,u)
    assert d_int==-2048
    fn=120*n*n-89*n+16
    fd=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    r=s.factor(fn/fd)
    assert s.factor(r-(4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)))==0
    assert s.resultant(fn,fd,n)==-(2**15)*(3**2)*(5**2)
    assert s.discriminant(fd,n)==(2**24)*(3**2)*(5**2)
    # The canonical H/G Mellin channels have opposite leading n^-1
    # coefficients and opposite poles at the 2-adic index t=0.
    htaps=(0,-2,0,-1,0,-s.Rational(1,2),0,-s.Rational(1,4))
    gtaps=(4,2,0,-1,-1,-s.Rational(1,2),0,s.Rational(1,4))
    rH=sum(v/(8*(n-1)+j+1) for j,v in enumerate(htaps))
    rG=sum(v/(8*(n-1)+j+1) for j,v in enumerate(gtaps))
    assert s.factor(rH+rG-r)==0
    assert s.factor(rH+(1/(4*n-3)+1/(4*(2*n-1))+
                        1/(4*(4*n-1))+1/(32*n)))==0
    assert s.limit(n*rH,n,s.oo)==-s.Rational(15,32)
    assert s.limit(n*rG,n,s.oo)==s.Rational(15,32)
    assert s.limit(n*n*(rH+rG),n,s.oo)==s.Rational(15,64)
    assert s.residue(rH,n,0)==-s.Rational(1,32)
    assert s.residue(rG,n,0)==s.Rational(1,32)
    assert s.limit(rH+s.Rational(1,32)/n,n,0)==s.Rational(5,6)
    assert s.limit(rG-s.Rational(1,32)/n,n,0)==-s.Rational(1,14)
    assert s.limit(rH+rG,n,0)==s.Rational(16,21)
    assert s.integrate(-2*t/(1-t*t/s.Integer(2)),(t,0,1))==-2*s.log(2)
    assert s.simplify(s.integrate((4-2*t)/(1-t+t*t/s.Integer(2)),(t,0,1))
                       - (s.pi+2*s.log(2)))==0
    # Distinct source and clock mutation with same first jet and c0:
    dm=s.expand(t*(1-t)**2*dcancel)
    assert dm.subs(t,0)==dm.subs(t,1)==s.diff(dm,t).subs(t,1)==0
    shift=s.integrate(dm,(t,0,1))
    assert shift==s.Rational(67,480)
    assert s.factor((P+eps*dm)/(1-t**8/s.Integer(16))-(K+eps*t*(1-t)**2/dmin))==0
    # Finite mod-13 phase tensor is a separate quotient-level result.
    states=sorted({pow(16,k,13)*pow(5,j,13)%13 for k in range(3) for j in range(4)})
    assert states==list(range(1,13))
    return dict(minimal_degree=4,hankel_determinant=4,
                minimal_integer_discriminant=int(d_int),
                fourpole_resultant=int(s.resultant(fn,fd,n)),
                fourpole_den_discriminant=int(s.discriminant(fd,n)),
                projectors=(str(EH),str(EG)),
                original_K=str(K),
                mutation_integral_shift=str(shift),
                gaussian_mod13_complete=states,
                source_sector_leading_coefficients=['-15/32','15/32'],
                source_two_adic_pole_residues=['-1/32','1/32'],
                source_total_leading_coefficient='15/64',
                integral_channels=['-2*log(2)','pi+2*log(2)'],
                claims_pi_normality=False)

if __name__=='__main__':
    import json
    print(json.dumps(run(),indent=2,sort_keys=True))
