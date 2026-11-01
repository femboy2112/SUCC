"""Independent algorithms; shared BBP mathematics, NOT a blind external reviewer."""
from fractions import Fraction as F
from math import factorial


def combined_source(n):
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def modular_prefix(n):
    """Modular exponentiation per summand + balanced sum, no forward recurrence."""
    parts=[]
    for j in range(1,n+1):
        r=combined_source(j)
        d=r.denominator
        parts.append(F((pow(16,n-j,d)*r.numerator)%d,d))
    while len(parts)>1:
        parts=[(parts[j]+parts[j+1])%1 if j+1<len(parts) else parts[j]
               for j in range(0,len(parts),2)]
    return parts[0] if parts else F()


def run_operator_word(operations, y):
    """Trace argument and phase directly through a word, no group multiplication."""
    x=F(y); phase=F(); density_square=F(1)
    for kind, args in operations:  # operators listed leftmost to rightmost
        if kind=='M':
            phase+=F(args[0])*x
        elif kind=='W':
            a,b=map(F,args)
            x=(x-b)/a; density_square/=a
        else:
            raise ValueError('unknown primitive')
    return x,phase,density_square


def fraction_cosine_at_angle(angle, terms=36):
    """Slow exact Fraction Taylor, distinct from fixed-point recurrence."""
    x=F(angle)
    value=sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(terms)),F())
    error=abs(x)**(2*terms)/factorial(2*terms)
    return value-error,value+error


def gaussian_window_numeric(N,m,h,phases=None):
    import mpmath as mp
    with mp.workdps(70):
        total=mp.mpc(0)
        for n in range(1,N+1):
            z=1 if phases is None else mp.exp(2j*mp.pi*h*mp.mpf(phases[n].numerator)/phases[n].denominator)
            total+=z*mp.exp(-2*mp.pi**2*h*h*mp.mpf(16)**(2*(n-m)))
        return total


def fourier_compose(left,right):
    """(a,c,q2,q1,q0): exp(i(q2*k²+q1*k+q0))*f(a*k+c).

    Argument tracing rather than the position-space AffineWeyl algebra.
    """
    a,c,p2,p1,p0=map(F,left); b,d,q2,q1,q0=map(F,right)
    return (b*a,b*c+d,p2+q2*a*a,p1+2*q2*a*c+q1*a,
            p0+q2*c*c+q1*c+q0)


def fourier_word(ops):
    result=(F(1),F(),F(),F(),F())
    for op in reversed(ops):result=fourier_compose(op,result)
    return result
