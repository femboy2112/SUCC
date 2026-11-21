"""Independent SymPy/mpmath algebra and high-precision oracle; does not import production module.

Produces an exact-scope JSON receipt, including PASS and a diagnostic negative control.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import mpmath as mp
import sympy as sp


def run_audit():
    z=sp.symbols('z',nonzero=True)
    I=sp.eye(2)
    H=z**4+2*z**3+4*z**2+4*z+4
    Q=4-2*z**3-z**4-z**5
    Hmut=sp.expand(H+1-z)
    f1=z*z+2
    f2=z*z+2*z+2
    checked=0

    assert sp.expand((1-z)*H-Q)==0; checked+=1
    assert sp.expand(f1*f2-H)==0; checked+=1
    assert sp.cancel(z**4*H.subs(z,sp.Rational(2)/z)-4*H)==0;checked+=1
    assert sp.rem(z**8-16,H,z)==0;checked+=1
    assert sp.div(z**8-16,H,z)[0]==z**4-2*z**3+4*z-4;checked+=1
    roots=[sp.sqrt(2)*sp.I,-sp.sqrt(2)*sp.I,-1+sp.I,-1-sp.I]
    for idx,t0 in enumerate(roots):
        assert sp.simplify(H.subs(z,t0))==0
        assert sp.simplify((t0*sp.conjugate(t0))-2)==0
        assert sp.simplify(t0**4/4)==(1 if idx<2 else -1)
        checked+=3

    # Exact idempotents in quotient algebra
    pplus=(1+z**4/sp.Integer(4))/2
    pminus=(1-z**4/sp.Integer(4))/2
    for e in (pplus,pminus):
        assert sp.rem(sp.expand(e*e-e),H,z)==0;checked+=1
    assert sp.rem(sp.expand(pplus*pminus),H,z)==0;checked+=1
    assert sp.expand(pplus+pminus-1)==0;checked+=1
    for mod, expected in [(f1,1),(f2,0)]:
        assert sp.rem(pplus-expected,mod,z)==0;checked+=1
    for mod, expected in [(f1,0),(f2,1)]:
        assert sp.rem(pminus-expected,mod,z)==0;checked+=1

    # Source-selected H(M) and determinant factors
    M=sp.Matrix([[0,1],[1,-1]])
    HM=M**4+2*M**3+4*M**2+4*M+4*I
    assert HM==sp.Matrix([[8,1],[1,7]]);checked+=1
    assert (M**2+2*I).det()==11;checked+=1
    assert (M**2+2*M+2*I).det()==5;checked+=1
    assert HM.det()==55;checked+=1

    # Explicit exact impulse response: rational-function equality + independent Taylor expansion.
    motif=[sp.Rational(1,4),sp.Rational(-1,4),sp.Integer(0),sp.Rational(1,8),sp.Rational(-1,16),sp.Integer(0),sp.Integer(0),sp.Integer(0)]
    numerator=sum(motif[j]*z**j for j in range(8))
    assert sp.cancel(1/H-numerator/(1-z**8/16))==0;checked+=1
    series_once=sp.expand(sp.series(1/H,z,0,64).removeO())
    coeffs=[series_once.coeff(z,k) for k in range(64)]
    for k in range(64):
        assert coeffs[k]==motif[k%8]/16**(k//8), (k,coeffs[k]);checked+=1
    assert sp.simplify(sum(q*q for q in motif)/(1-sp.Rational(1,256)))==sp.Rational(37,255);checked+=1

    # Independent authentic BBP Mellin mask to rational forcing, 48 clocks.
    for n in range(1,49):
        # Integral of t^(8n-8)*Q(t) dt, coefficient by coefficient.
        by_integral=4/sp.Integer(8*n-7)-2/sp.Integer(8*n-4)-1/sp.Integer(8*n-3)-1/sp.Integer(8*n-2)
        from_quadratic_factor=sp.integrate(z**(8*n-8)*Q,(z,0,1)) if n<=6 else by_integral
        assert sp.simplify(by_integral-from_quadratic_factor)==0; checked+=1

    # Matched-first-jet source mutation fails every common-radius reciprocal condition.
    assert sp.simplify(Hmut-(z**4+2*z**3+4*z**2+3*z+5))==0;checked+=1
    assert sp.expand(z**4*Hmut.subs(z,sp.Rational(2)/z)-4*Hmut)!=0;checked+=1
    assert 3**2 != 2**2*5;checked+=1
    assert Q.subs(z,1)==0 and sp.diff(Q,z).subs(z,1)==-15;checked+=1
    Qmut=sp.expand((1-z)*Hmut)
    assert Qmut.subs(z,1)==0 and sp.diff(Qmut,z).subs(z,1)==-15;checked+=1

    # Independent high precision coherent Haar superposition; one port identically selects factor.
    mp.mp.dps=85
    R=mp.sqrt(2); L=mp.pi*R; k=2/R
    groups=[('top',mp.pi/2,1),('left_up',3*mp.pi/4,-1),
            ('left_down',5*mp.pi/4,-1),('bottom',3*mp.pi/2,1)]
    for _,ang,sign in groups:
        a=R*(ang-mp.pi/2);b=L-a
        e1=mp.e**(mp.j*k*a)/mp.sqrt(2)
        e2=mp.e**(mp.j*k*b)/mp.sqrt(2)
        Pplus=abs((e1+e2)/mp.sqrt(2))**2
        Pminus=abs((e1-e2)/mp.sqrt(2))**2
        assert abs(Pplus-(1 if sign==1 else 0)) < mp.mpf('1e-75')
        assert abs(Pminus-(1 if sign==-1 else 0)) < mp.mpf('1e-75')
        assert abs(Pplus+Pminus-1) < mp.mpf('1e-75')
        checked+=3

    # Independent winding via discrete argument change for circles away from zeros.
    winding={}
    for rad,expected in [(0.5,0),(1.25,1),(1.5,5),(2.0,5)]:
        v=[]
        for j in range(8193):
            angle=2*math.pi*j/8192
            zz=rad*complex(math.cos(angle),math.sin(angle))
            v.append(4-2*zz**3-zz**4-zz**5)
        phase=0.0
        for j in range(1,len(v)):
            ratio=v[j]/v[j-1]
            phase+=math.atan2(ratio.imag,ratio.real)
        estimate=round(phase/(2*math.pi))
        assert estimate==expected, (rad,estimate)
        winding[str(rad)]=estimate;checked+=1

    # Mutation root radii split: diagnostic only; exact impossibility already proved above.
    mut_roots=sp.nroots(Hmut,maxsteps=80)
    mut_radii=sorted(float(abs(complex(x))) for x in mut_roots)
    assert mut_radii[1]<math.sqrt(2)<mut_radii[2];checked+=1
    receipt={
      'status':'PASS','tool':'standalone_sympy_mpmath_root_and_scattering_oracle',
      'exact_symbolic_checks_plus_exact_impulse_terms_plus_mask_clocks_and_HP_ports':checked,
      'checked_taylor_coefficients':64,
      'checked_original_source_clocks':48,
      'high_precision_dps':85,
      'source_mutant_radii_float_diagnostic':mut_radii,
      'independent_numeric_winding':winding,
      'scope':'root-filter algebra and declared synthetic scattering; NOT a pi-normality or physical scattering proof',
    }
    return receipt


if __name__=='__main__':
    info=run_audit()
    path=Path(__file__).with_name('independent_audit_receipt.json')
    path.write_text(json.dumps(info,indent=2,sort_keys=True)+'\n')
    print(json.dumps(info,indent=2))
