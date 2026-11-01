"""Optional independent SymPy exact symbolic oracle for arctan mirror identities."""
from __future__ import annotations
import json
import sympy as s
from pathlib import Path


def run():
    z,t,w,r=s.symbols('z t w r')
    i=s.I
    A=(8*z-7)**4
    D=(8*z-4)**2*(8*z-3)*(8*z-2)
    R=A/D
    fourpole=4/(8*z-7)-2/(8*z-4)-1/(8*z-3)-1/(8*z-2)
    q=s.Rational(106,819)
    c=lambda x:(1+i*x)/(1-i*x)
    rec=lambda x:1/x
    J=lambda x:(q-x)/(1+q*x)
    gamma=(819+106*i)/(819-106*i)
    eta=2/(1+t*t)
    checks=[]
    def chk(name,expr):
        diff=s.cancel(s.together(expr))
        if diff!=0:raise AssertionError(f'{name}: {diff}')
        checks.append(name)
    chk('four original poles dlog',s.diff(R,z)/(8*R)-fourpole)
    chk('original r2 rational',fourpole.subs(z,2)-q)
    chk('reciprocity Cayley',c(rec(t))+1/c(t))
    chk('angular differential reversed',s.diff(rec(t),t)*eta.subs(t,rec(t))+eta)
    chk('positive orientation source pullback',s.diff(-i*(R-1)/(R+1),z)*
        eta.subs(t,-i*(R-1)/(R+1))*i/s.Integer(8)-fourpole)
    chk('rational source mirror Cayley transport',c(J(t))-gamma/c(t))
    chk('source mirror is projective involution',J(J(t))-t)
    chk('square of integer projective matrix',
        (s.Matrix([[-819,106],[106,819]])**2-s.eye(2)*681997)[0,0])
    chk('unit modulus Gaussian rational',s.re(s.expand_complex(gamma))**2+s.im(s.expand_complex(gamma))**2-1)
    chk('circle ×16 mirror central commutator', (gamma/w)**16/(gamma/w**16)-gamma**15)
    chk('rotated mirror cocycle',gamma/(s.exp(2*s.pi*i*r)*w**16)-
        (gamma**(-15)*s.exp(-2*s.pi*i*r))*(gamma/w)**16)
    # Source-specific substitution in the projective rational cover.
    source_t=-i*(R-1)/(R+1)
    chk('source differential involutes',s.diff(1/source_t,z)*
        eta.subs(t,1/source_t)+s.diff(source_t,z)*eta.subs(t,source_t))
    P=s.expand((1+i*t)**16)
    re=s.re(s.expand_complex(P))
    im=s.im(s.expand_complex(P))
    # rational tangent 16 map via binomial even/odd parts
    realpoly=s.expand(sum((-1)**k*s.binomial(16,2*k)*t**(2*k) for k in range(9)))
    imagpoly=s.expand(sum((-1)**k*s.binomial(16,2*k+1)*t**(2*k+1) for k in range(8)))
    chk('projective ×16 reciprocal sign',imagpoly.subs(t,1/t)*realpoly+realpoly.subs(t,1/t)*imagpoly)
    chk('degree16 Cayley identity',c(imagpoly/realpoly)-c(t)**16)
    receipt={"status":"EXACT_SYMBOLIC_CHECKS_PASS","checks":checks,"count":len(checks),
             "q":str(q),"gamma":str(s.expand_complex(gamma))}
    dest=Path(__file__).with_name('SYMBOLIC_RECEIPT.json')
    dest.write_text(json.dumps(receipt,indent=2)+"\n")
    print('ARCTAN_RECIPROCITY_SYMBOLIC_PASS',len(checks))
    return receipt

if __name__=='__main__':run()
