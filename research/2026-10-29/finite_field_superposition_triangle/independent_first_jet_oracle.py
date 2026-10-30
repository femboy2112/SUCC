"""Independent SymPy oracle for the finite-source triangle, no module import.

All symbolic assertions are exact. Finite-n comparisons are observations only.
"""
import sympy as sp


def main():
    z=sp.symbols('z', real=True)
    a=sp.symbols('a', positive=True)
    n=sp.symbols('n', positive=True)
    y=sp.symbols('y', positive=True)
    u=z-1
    b=2-z
    Q=lambda x:4-2*sp.exp(-3*x)-sp.exp(-4*x)-sp.exp(-5*x)
    R=lambda t:4/t-2/(t+3)-1/(t+4)-1/(t+5)
    assert sp.simplify(R(a)-(15*a*a+121*a+240)/(a*(a+3)*(a+4)*(a+5)))==0
    assert sp.diff(Q(y),y).subs(y,0)==15
    assert sp.diff(Q(y),y,2).subs(y,0)==-59
    # Positive distinct source with identical first two endpoint derivatives.
    q_hidden_mutant = Q(y)*(1 + y**2/(1+y**2))
    assert sp.diff(q_hidden_mutant,y).subs(y,0)==15
    assert sp.diff(q_hidden_mutant,y,2).subs(y,0)==-59
    assert sp.simplify(q_hidden_mutant-Q(y)) != 0
    # Native clock a=8n-7; latent Y=aX tends to Gamma(2,1).
    # For the exact four-pole normalized field the first density correction
    # at order 1/n is (59/240)(2-y) times y*exp(-y).
    # The binomial-probe first correction is
    # (z-1)*(7*y/8-y**2/2) -(z-1)**2*y**2/2.
    weighted = u*(sp.Rational(7,8)*y -y**2/2) - u**2*y**2/2 + sp.Rational(59,240)*(2-y)
    expectation = sp.integrate(y*sp.exp(-b*y)*weighted,(y,0,sp.oo),conds='none')
    exact = (1-z)*(511*z-302)/(120*(2-z)**4)
    assert sp.simplify(expectation-exact)==0
    assert sp.simplify(exact.subs(z,0)+sp.Rational(151,960))==0
    assert sp.simplify(exact.subs(z,1))==0
    # Original, Gamma-matched mutant and exact 59 source separation.
    fake_integrand=weighted-sp.Rational(59,240)*(2-y)
    fake=sp.integrate(y*sp.exp(-b*y)*fake_integrand,(y,0,sp.oo),conds='none')
    assert sp.simplify(exact-fake-sp.Rational(59,120)*(1-z)/(2-z)**3)==0
    a0=sp.integrate((1-1/(2-z)**2)/(1-z),(z,0,1))
    coeff=sp.integrate(-exact/(1-z),(z,0,1))
    fake_coeff=sp.integrate(-fake/(1-z),(z,0,1))
    assert sp.simplify(a0-sp.Rational(1,2)-sp.log(2))==0
    assert coeff==-sp.Rational(49,320)
    assert fake_coeff==sp.Rational(1,32)
    assert coeff-fake_coeff==-sp.Rational(59,320)
    # The same two-channel PGF has interior fixed point (3-sqrt(5))/2.
    p=(3-sp.sqrt(5))/2
    assert sp.simplify(1/(2-p)**2-p)==0
    # The integrated grade observation gives a SECOND gamma/golden contrast.
    lam=(sp.sqrt(5)-1)/2
    derived = 1+sp.log(2)-sp.EulerGamma -1/(1+2*lam)**2
    grade_sum = 1+sp.log(2)-sp.EulerGamma - lam**2/(2-lam)**2
    assert sp.simplify(derived-grade_sum)==0
    print('PASS exact symbolic independent first-jet, source-mutant, harmonic, golden and grade-contrast identities')
    print('Original harmonic first jet:',coeff, 'Gamma-matched fake:',fake_coeff)


if __name__=='__main__':
    main()
