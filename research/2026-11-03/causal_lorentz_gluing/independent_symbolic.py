"""Independent SymPy oracle: no import of the new exact source implementation.

This checks source polynomial, 2-adic forcing parity, Gaussian/real quadratic
transfer, dual metric, the eight-clock Lorentz matrix and beta/gamma values.
It is NOT an independent human referee or all-horizon Weyl certificate.
"""
import json
from sympy import Matrix, Rational as R, Poly, factor, symbols, eye


def proof_checks():
    s,t,x,y = symbols('s t x y')
    m=s**4-s**3+s/2-R(1,4)
    p=(s**2-R(1,2))*(s**2-s+R(1,2))
    assert factor(m-p)==0
    # Correct full source transfer, in a second implementation.
    K=(4*(1-t))/((1-t*t/2)*(1-t+t*t/2))
    P=4-2*t**3-t**4-t**5
    assert factor(K-P/(1-t**8/16))==0
    # Original four-pole indexed forcing, not Mellin coeffs mistaken for complex poles.
    N=120*x*x-89*x+16
    D=(2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
    Rfor=4/(8*x-7)-2/(8*x-4)-1/(8*x-3)-1/(8*x-2)
    assert factor(N/D-Rfor)==0
    # Source injection r is 2-adically isometric: denominator odd and
    # divided numerator difference odd; divided denominator difference even.
    deltaD=Poly(D,x).all_coeffs()
    assert all(int(coef)%2==0 for coef in deltaD[:-1])
    dividedN=(120*(x+y)-89)
    assert int(Poly(dividedN,x,y).coeff_monomial(1))%2==1
    # independently build companion matrix as multiplication by s modulo m.
    T=Matrix([[0,0,0,R(1,4)],
              [1,0,0,-R(1,2)],
              [0,1,0,0],
              [0,0,1,1]])
    assert T**8==eye(4)/16
    assert (T**4)**2==eye(4)/16
    # canonical 8D contragredient doubled state/dual.
    L=Matrix.diag(T,(T.inv()).T)
    J=Matrix.vstack(Matrix.hstack(Matrix.zeros(4),eye(4)),
                    Matrix.hstack(eye(4),Matrix.zeros(4)))
    assert L.T*J*L ==J
    assert L**8==Matrix.diag(eye(4)/16,16*eye(4))
    assert L**4!=Matrix.diag(eye(4)/4,4*eye(4))  # Gaussian half-clock sign
    # Source readout from c_n = tr(w*T^n), with w=-1+2s+2s^2-8s^3.
    w=-eye(4)+2*T+2*T*T-8*T**3
    c=[(w*T**n).trace() for n in range(8)]
    assert c==[4,0,0,-2,-1,-1,0,0]
    eH=(eye(4)+4*T**4)/2
    eG=(eye(4)-4*T**4)/2
    assert eH**2==eH and eG**2==eG and eH*eG==Matrix.zeros(4)
    assert T**4*eH==eH/4 and T**4*eG==-eG/4
    # Lorentz 2-plane after 8 taps; gamma and beta are EXACT rational.
    lam=R(16)
    gamma=(lam+1/lam)/2
    delta=(lam-1/lam)/2
    beta=delta/gamma
    Boost=Matrix([[gamma,delta],[delta,gamma]])
    Eta=Matrix.diag(1,-1)
    assert Boost.T*Eta*Boost==Eta
    assert gamma==R(257,32) and beta==R(255,257)
    assert gamma**2-delta**2==1
    assert (lam-1)/(lam+1)==R(15,17)
    # Independent hyperbolic half-rapidity parameterization from existing SUCC lab.
    h=R(15,17)
    assert beta==2*h/(1+h*h)
    assert gamma==(1+h*h)/(1-h*h)
    return {'minimal_polynomial':str(factor(m)),
            'root_transfer_factorization':True,
            'original_four_poles_preserved':True,
            'source_difference_quotient_mod2_unit':True,
            'eight_step_scalar_return':str(R(1,16)),
            'half_clock_Gaussian_sign':-1,
            'cotangent_split_signature':'(4,4)',
            'source_impulses':[str(v) for v in c],
            'gamma':str(gamma),'beta':str(beta),
            'gamma_beta':str(delta),
            'tanh_half_rapidity':str(h),
            'Lorentz_metric_preserved':True,
            'selected_pi_normality_proved':False}


if __name__=='__main__':
    print(json.dumps(proof_checks(),indent=2,sort_keys=True))
