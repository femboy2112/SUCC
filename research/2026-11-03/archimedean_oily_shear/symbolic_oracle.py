"""Independent SymPy rational certificate for selected original BBP Gamma shape.

This checks rational identities only; it does not prove pi normality.
"""
import sympy as s


def run():
    t,n=s.symbols('t n')
    base=(2-t*t)*((1-t)**2+1)
    den=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    r=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
    p=4-2*t**3-t**4-t**5
    eight=1-t**8/16
    h=(2-t*t)/((1-t)**2+1)
    radial=2-2*t-t*t-2*t**3-t**4/2-t**5/2+t**6/4
    checks={
      'original_four_poles_exact':s.cancel(r-(120*n*n-89*n+16)/den)==0,
      'original_beta_kernel':s.cancel(p/(16-t**8)-(1-t)/base)==0,
      'factorized_transfer':s.cancel(p/eight-16*(1-t)/base)==0,
      'source_positive_beta_defect':s.expand((base-1)-(1-t)*(t**3-t*t-t+3))==0,
      'radial_null_derivative':s.cancel(radial/eight-2*s.diff(s.log(h),t))==0,
      'beta_cap_derivative_polynomial_positive':s.Poly(
          s.expand((8*n+1)**2*(8*n+2)**2-256*n**3*(16*n+3)),n).all_coeffs()==[2304,832,96,4],
    }
    if not all(checks.values()):raise AssertionError('failed exact identity: '+str(checks))
    return checks


if __name__=='__main__':
    for k,v in run().items():print(('PASS' if v else 'FAIL')+' '+k)
