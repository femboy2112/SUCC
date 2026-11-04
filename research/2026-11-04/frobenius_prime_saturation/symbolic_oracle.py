"""Independent SymPy source-identity oracle; exact symbolic, no pi digits."""
from __future__ import annotations
import sympy as s


def verify():
    x,k,t=s.symbols('x k t', positive=True, real=True)
    source=4/(8*x-7)-2/(8*x-4)-1/(8*x-3)-1/(8*x-2)
    twin=8/(8*x-6)+4/(8*x-5)+4/(8*x-4)-1/(8*x-1)
    assert s.factor(source)==(120*x*x-89*x+16)/((2*x-1)*(4*x-1)*(8*x-7)*(8*x-3))
    P=4-2*t**3-t**4-t**5
    Pstar=8*t+4*t**2+4*t**3-t**6
    F=(2-t*t)/((t-1)**2+1)
    assert s.simplify((Pstar-2*P)/(1-t**8/s.Integer(16))+8*s.diff(F,t)/F)==0
    assert F.subs(t,0)==F.subs(t,1)==1
    assert s.expand((Pstar-2*P)+(t*t+2)*(t*t-4*t+2)*(t*t+2*t+2))==0
    assert s.limit(x* (twin-2*source),x,s.oo)==s.Rational(15,8)
    assert s.limit(x*x*(twin-2*source-s.Rational(15,8)/x),x,s.oo)==s.Rational(53,64)
    # Strict all-real s>=2 rational upper: d(s)<15/[8(s-1/2)].
    numerator=s.together(s.Rational(15,8)/(x-s.Rational(1,2))-(twin-2*source)).as_numer_denom()[0]
    denominator=s.together(s.Rational(15,8)/(x-s.Rational(1,2))-(twin-2*source)).as_numer_denom()[1]
    # Clear any common symbolic constant/positive factors by substituting
    # x=y+2 and checking all polynomial coefficients nonnegative.
    y=s.symbols('y',nonnegative=True)
    poly=s.Poly(s.expand(numerator.subs(x,y+2)),y)
    assert all(c>0 for c in poly.all_coeffs())
    assert all(s.factor(denominator.subs(x,n))>0 for n in (2,3,5,13))

    # Derive each complete shell using only symbolic source pulse factors.
    classes={
      1: (1,((1,7,4),(4,4,-2),(5,3,-1),(6,2,-1))),
      3: (-1,((2,2,-1),(3,7,4),(4,4,-2),(7,3,-1))),
      5: (-1,((1,3,-1),(4,4,-2),(5,7,4),(6,2,-1))),
      7: (1,((2,2,-1),(3,3,-1),(4,4,-2),(7,7,4))),
    }
    for a,(chi,ev) in classes.items():
        # Previous shell endpoint is at event 8k+offset_last.
        prev=(8*k+ev[-1][0],ev[-1][1],0)
        later=[(8*k+8+m,c,w) for m,c,w in ev]
        A=s.Integer(1);B=s.Integer(0)
        for cur in later:
            m0,c0,_=prev
            m,c,w=cur
            dm=s.simplify(m-m0);dc=c-c0
            assert (dm+dc)%2==0
            factor=s.Rational(2)**((dm+dc)/2) *chi**dm
            A=s.simplify(factor*A)
            B=s.simplify(factor*B+s.Rational(w)/m)
            prev=cur
        expected=source.subs(x,k+2) if a in (1,5) else twin.subs(x,k+2)
        if a==7:expected*=-4
        assert A==16,(a,A)
        assert s.factor(B-expected)==0,(a,s.factor(B-expected))
    return {'symbolic_original_pole':True,'global_dual_null_exact_derivative':True,
            'all_four_full_shell_symbolic_recurrences':True,
            'dual_source_leading_asymptotics':True}

if __name__=='__main__':
    print('SYMBOLIC_FROBENIUS_PRIME_PASS',verify())
