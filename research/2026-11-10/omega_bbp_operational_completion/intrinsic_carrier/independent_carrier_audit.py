"""Independent SymPy/MPMath confirmation; not a second external referee.

Forms projections directly from physical basis coordinates rather than calling
intrinsic_carrier.py and checks finite spectra, boundary and signed alias.
"""
import sympy as s
import mpmath as mp


def avg_blocks(p,N):
    M=s.zeros(N)
    for first in range(p,N+1,p):
        if first+p-1>N:break
        for i in range(first,first+p):
            for j in range(first,first+p):M[i-1,j-1]=s.Rational(1,p)
    return M


def main():
    t=s.Symbol('t')
    for p in (2,3,4,5,7):
        u=s.ones(p,1)/s.sqrt(p)
        P=u*u.T;Q=s.zeros(p);Q[0,0]=1
        C=P*Q-Q*P
        char=C.charpoly(t).as_expr().factor()
        assert s.simplify(char-t**(p-2)*(t**2+s.Rational(p-1,p*p)))==0
        assert s.simplify(C**3+s.Rational(p-1,p*p)*C)==s.zeros(p)
    N=23
    C=avg_blocks(2,N)*avg_blocks(3,N)-avg_blocks(3,N)*avg_blocks(2,N)
    for st,en,lam in [(1,5,s.Rational(5,36)),(6,11,s.Rational(2,9)),
                      (12,17,s.Rational(2,9)),(18,23,s.Rational(2,9))]:
        J=C[st-1:en,st-1:en]
        assert J.charpoly(t).as_expr().factor()==(t**(J.rows-2)*(t**2+lam)).factor()
    # First finite Mellin ghost: q_0(z)=z-1/45, integral (1-x)*q(x^8)=0.
    x=s.Symbol('x')
    q=x**8-s.Rational(1,45)
    assert s.integrate((1-x)*q,(x,0,1))==0
    # High precision completion discrepancy agrees with strict rational bounds.
    mp.mp.dps=65
    eps=mp.mpf(45)/46
    numerical=mp.quad(lambda x:eps*(1-x)*(x**8-mp.mpf(1)/45)/(1-x**8/16),[0,1])
    assert mp.mpf('0.00018496846')<numerical<mp.mpf('0.00019729970')
    print('INDEPENDENT PASS: p=2,3,4,5,7 spectral polynomials; 5+3*6 exact boundary/bulk;')
    print('  finite Mellin null moment, strict positive completion defect:',mp.nstr(numerical,22))


if __name__=='__main__':main()
