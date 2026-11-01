"""Independent Z[t] polynomial oracle for BBP adaptive mirror inequalities.

Uses independent raw integer polynomial multiplication/substitution; no SymPy,
float sampling, or hand-coded expression simplification for a proof certificate.
"""
from __future__ import annotations
from fractions import Fraction as F


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return tuple(p)


def add(a,b):
    return trim([ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                   for i in range(max(len(a),len(b)))])


def neg(a):return tuple(-z for z in a)


def sub(a,b):return add(a,neg(b))


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)


def scale(a,k):return trim([k*v for v in a])


def pow_poly(a,k):
    out=(1,)
    for _ in range(k):out=mul(out,a)
    return out


def shift(a,k):
    """Evaluate polynomial in X at X=t+k; exact arithmetic."""
    out=(0,)
    for v in reversed(a):out=add(mul(out,(k,1)),(v,))
    return out


def verify_coefficients()->dict:
    x=(0,1)
    A=(16,-89,120)
    D=(1,)
    for factor in ((-1,2),(-1,4),(-7,8),(-3,8)):
        D=mul(D,factor)
    nn=pow_poly(x,2)
    low=sub(scale(mul(nn,A),64),scale(D,15))
    high=sub(scale(D,8),scale(mul(nn,A),15))
    high8=sub(scale(D,9),scale(mul(nn,A),32))
    weight=add(pow_poly((-1,1),2),(1,))
    weighted=sub(scale(mul(weight,A),5),D)
    targets={
      'source_lower_n_ge_2':(44553,80434,48328,9664),
      'source_upper_n_ge_2':(576,11364,19418,11511,2296),
      'source_upper_n_ge_8':(248013,442690,147976,18208,768),
      'weighted_lower_n_ge_3':(1090,641,621,435,88),
      'weighted_lower_n_eq_2':723,
    }
    actual={
      'source_lower_n_ge_2':shift(low,2),
      'source_upper_n_ge_2':shift(high,2),
      'source_upper_n_ge_8':shift(high8,8),
      'weighted_lower_n_ge_3':shift(weighted,3),
      'weighted_lower_n_eq_2':shift(weighted,2)[0],
    }
    if actual!=targets:raise ArithmeticError(f'original-source positivity certificates mismatch: {actual}')
    for key,value in actual.items():
        if isinstance(value,tuple) and not all(x>0 for x in value):
            raise ArithmeticError(f'nonpositive coefficient in {key}')
        if isinstance(value,int) and not value>0:raise ArithmeticError(f'nonpositive value in {key}')
    L=F(671,3375)-F(9,128)
    if not L>F(1,8) or not L-L**3/6>F(1,8):
        raise ArithmeticError('strict frame sine constant is not certified')
    return {'status':'EXACT_INTEGER_POLYNOMIAL_CERTIFIED',
            'coefficients':actual,'delta_lower':L,
            'sine_lower_taylor':L-L**3/6,
            'uniform_sine_lower':F(1,8),
            'witnesses':5}

if __name__=='__main__':
    v=verify_coefficients()
    print(v['status'],v['uniform_sine_lower'],v['delta_lower'])
