"""Exact exploratory graph probes for the authentic four-pole BBP source.

Scope: symbolic algebra, holonomic identity, pole proliferation, and a hostile
normality model. No claim of source-selected signed cancellation.
Requires SymPy. Run: python bbp_graph_shapes_probe.py
"""
from fractions import Fraction
from math import prod
import sympy as sp

x, z, n = sp.symbols('x z n')
P = (1-x)*(x*x+2)*(x*x+2*x+2)
D8 = 16-x**8
D4 = (2-x*x)*(x*x-2*x+2)


def r(nn):
    assert nn >= 0
    return (Fraction(4, 8*nn+1)-Fraction(2,8*nn+4)
            -Fraction(1,8*nn+5)-Fraction(1,8*nn+6))


def omega_holonomic_rhs_coefficient(nn):
    return 8*(120*nn*nn + 151*nn + 47)


def decimated_poles(k):
    return {Fraction(-a,8*16**k) for a in (1,4,5,6)}


def verify():
    checks = {}
    checks['eightfold_factorization'] = sp.expand(D8 - D4*(x*x+2)*(x*x+2*x+2)) == 0
    checks['four_pole_source'] = sp.expand(P - (4-2*x**3-x**4-x**5)) == 0
    K_original = sp.cancel(P/(1-x**8/16))
    K_reduced = 16*(1-x)/D4
    checks['analytic_root_reduction'] = sp.cancel(K_original-K_reduced)==0
    Phi = 4*sp.atan(x-1)+2*sp.log((2-x*x)/(x*x-2*x+2))
    checks['exact_primitive'] = sp.cancel(sp.diff(Phi,x)-K_reduced)==0
    checks['endpoint_log_vanishes'] = sp.simplify(Phi.subs(x,1))==0 and sp.simplify(Phi.subs(x,0)+sp.pi)==0
    res = sp.factor(sp.resultant(P,1-z*x**8,x))
    checks['resonance_resultant'] = sp.expand(res-(1-z)*(1-16*z)**4)==0
    checks['resonance_gcd_1over16'] = sp.degree(sp.gcd(P,1-x**8/16),x)==4
    checks['other_interior_nonresonance'] = all(sp.degree(sp.gcd(P,1-q*x**8),x)==0 for q in [sp.Rational(1,4),sp.Rational(1,8),sp.Rational(1,17),sp.Rational(1,32),sp.Rational(1,100)])
    checks['holonomic_coefficient_exact'] = all(prod(8*nn+a for a in (1,4,5,6))*r(nn) == omega_holonomic_rhs_coefficient(nn) for nn in range(400))
    theta = lambda a: z*sp.diff(a,z)
    LL=lambda a,b:sp.cancel(8*theta(a)+b*a)
    rhs=0
    for a,c in zip((1,4,5,6),(4,-2,-1,-1)):
        f=1/(1-z)
        for b in (1,4,5,6):
            if b!=a: f=LL(f,b)
        rhs+=c*f
    checks['holonomic_operator'] = sp.cancel(rhs-8*(16*z*z+177*z+47)/(1-z)**3)==0
    sets=[decimated_poles(k) for k in range(25)]
    checks['disjoint_decimation_poles'] = all(not sets[j]&sets[k] for j in range(len(sets)) for k in range(j+1,len(sets)))
    # Stronger hostile polynomial: same fourfold resonance AND endpoint zero,
    # positive kernel with quadratic-decay moments, unique BBP-type fixed point,
    # yet integral rational 1 and nonnormal selected zero-seed orbit.
    dlog = -2*x/(2-x*x)-(2*x-2)/(x*x-2*x+2)
    K_fake = 2*(1-x)+sp.Rational(1,10)*(4*x-2+dlog)
    H = 38-34*x-x*x+17*x**3-8*x**4
    P_fake = sp.cancel((1-x**8/16)*K_fake)
    checks['fake_source_polynomial'] = sp.denom(P_fake)==1
    checks['fake_source_exact_factor'] = sp.cancel(P_fake-(1-x)*(x*x+2)*(x*x+2*x+2)*H/80)==0
    checks['fake_resonance_degree_four'] = sp.degree(sp.gcd(P_fake,1-x**8/16),x)==4
    checks['fake_integral_rational_one'] = sp.integrate(K_fake,(x,0,1))==1
    checks['fake_endpoint_zero'] = K_fake.subs(x,1)==0
    # For 0 <= x <= 1, H >= 38-34*x-x² >= 3 since 17*x³-8*x⁴ >= 0.
    # Therefore K_fake=(1-x)*H/[5(2-x²)((x-1)²+1)] >= 0, strictly before 1.
    checks['fake_positive_factor_certificate'] = sp.cancel(K_fake-((1-x)*H/(5*D4)))==0
    # Two-cycle alpha=1/255 under multiplication by 16 mod 1:
    alpha=Fraction(1,255)
    T=lambda a: (16*a)%1
    checks['two_cycle'] = T(alpha)!=alpha and T(T(alpha))==alpha
    for rho in (Fraction(1,2),Fraction(3,4),Fraction(99,100)):
        w0=1/(1+rho);w1=rho/(1+rho)
        # fixed point (1-rho)delta_alpha + rho T_*nu = nu
        checks[f'periodic_resolvent_{rho}'] = (w0==(1-rho)+rho*w1 and w1==rho*w0 and w0+w1==1)
    assert all(checks.values()), {k:v for k,v in checks.items() if not v}
    print('Exact BBP computational graph: all',len(checks),'assertion families PASS')
    print('Source resonance resultant =',res)
    print('Reduced root =',sp.factor(K_reduced))
    print('Holonomic identity: Π(8θ+a) Φ(z) = 8(16z²+177z+47)/(1-z)³')
    print('Disjoint decimated source pole sets:',len(sets))
    print('Hostile resonance source P_fake(x) =',sp.factor(P_fake))
    print('Its analytic fixed point integral =',sp.integrate(K_fake,(x,0,1)), '; endpoint zero and positive on [0,1)')
    print('Nonnormal 2-cycle alpha=1/255 has Fourier mode h=255 identically 1')
    print('No π normality/parity decay has been proved.')

if __name__ == '__main__':
    verify()
