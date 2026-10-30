"""Read recorded witnesses, reconstruct by SymPy; no production import.

An independent computational route, not an independent human/model referee.
"""
from pathlib import Path
import json
import sympy as s

def run():
    data=json.loads((Path(__file__).resolve().parents[1]/'receipts/period-probe.log').read_text())
    z=s.Symbol('z');x=s.Symbol('x');rows=[]
    original=4-2*z**3-z**4-z**5
    for row in data['planned']+data['fresh_holdouts']:
        m,N=row['m'],row['N']
        # Integrate expanded polynomials, instead of factorial Beta moments.
        moments=[s.integrate(s.expand(z**(8*(j+1))*(1-z)**(m+1)),(z,0,1))
                 for j in range(2*N+1)]
        coeff=list(s.Matrix(N,N,lambda i,j:moments[i+j]).inv()*
                   s.Matrix([-moments[i+N] for i in range(N)])) if N else []
        coeff+=[s.Integer(1)]
        assert coeff==[s.Rational(v) for v in row['p']]
        p=sum(c*z**(8*i) for i,c in enumerate(coeff))
        R=z*(1-z)**(m+1)*p
        eps=s.Rational(row['epsilon'])
        D=s.Poly(s.expand((16-z**8)*s.diff(R,z)),z)
        mutant=s.Poly(original+eps*D.as_expr(),z)
        assert list(reversed(mutant.all_coeffs()))==[s.Rational(v) for v in row['source_coefficients']]
        assert s.integrate(s.diff(R,z),(z,0,1))==0
        # Direct unrolled source sum, distinct from recursive producer orbit.
        for n in (1,N+1,N+4):
            force=lambda k:sum(c/s.Integer(i+8*k-7) for (i,),c in D.terms())
            unrolled=eps*sum(16**(n-k)*force(k) for k in range(1,n+1))
            boundary=eps*8*n*s.integrate(s.expand(z**(8*n-1)*R),(z,0,1))
            assert unrolled==boundary
        rows.append({'m':m,'N':N,'polynomial_degree':mutant.degree(),
                     'symbolic_period':'0','unrolled_cases':3,'status':'PASS'})
    print(json.dumps({'sympy':s.__version__,'implementation':'symbolic integration and matrix inverse; no producer imports',
                      'rows':rows,'status':'PASS'},indent=2))

if __name__=='__main__':run()
