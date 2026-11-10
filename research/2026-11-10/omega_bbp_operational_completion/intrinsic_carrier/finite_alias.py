"""An exact finite-observer alias for BBP-style positive Mellin kernels.

For every N the source P_epsilon=(1-x)*(M(x)+epsilon*q_N(x**8)) has
identical first N+1 moments to the authentic four-pole BBP source but a
strictly larger infinite completed BBP-type sum. This does NOT change the
canonical four-pole contract; it is an adversarial different source.
"""
from fractions import Fraction


def moment(k):
    """nu_k=integral_0^1 (1-x)*x^(8k) dx."""
    if type(k) is not int or k<0:raise ValueError('k>=0')
    return Fraction(1,(8*k+1)*(8*k+2))


def solve(A,b):
    """Exact rational square Gaussian elimination (independent of sympy)."""
    n=len(b)
    a=[list(A[i])+[b[i]] for i in range(n)]
    for i in range(n):
        pivot=next((k for k in range(i,n) if a[k][i]),None)
        if pivot is None:raise ValueError('singular')
        a[i],a[pivot]=a[pivot],a[i]
        d=a[i][i]
        a[i]=[z/d for z in a[i]]
        for k in range(n):
            if k==i:continue
            c=a[k][i]
            a[k]=[a[k][j]-c*a[i][j] for j in range(n+1)]
    return [a[i][-1] for i in range(n)]


def monic_orthogonal(N):
    """Monic q_N(t) deg N+1 orthogonal to t^0,...,t^N in dnu=(1-x)dx."""
    if type(N)!=int or N<0: raise ValueError('N>=0')
    m=N+1
    gram=[[moment(i+j) for j in range(m)] for i in range(m)]
    rhs=[-moment(i+m) for i in range(m)]
    return solve(gram,rhs)+[Fraction(1)]


def evaluate(c,x):
    return sum((a*x**j for j,a in enumerate(c)),Fraction())


def inner(a,b):
    return sum((a_i*b_j*moment(i+j) for i,a_i in enumerate(a)
                for j,b_j in enumerate(b)), Fraction())


def root_certificate(N):
    """Strict rational lower/upper bounds for changed infinite BBP-type sum.

    Delta=epsilon*int ((1-x)*q_N(x^8)/(1-x^8/16)) dx
         =(16*epsilon/q_N(16))*int (1-x)*q_N(x^8)^2/(16-x^8) dx >0.
    lower < Delta < upper. q_N(16)>0 by the classical orthogonal-polynomial
    roots theorem (positive measure on (0,1)).
    """
    c=monic_orthogonal(N)
    eps=Fraction(1,sum(abs(a) for a in c))
    q16=evaluate(c,16)
    norm2=inner(c,c)
    assert q16>0 and norm2>0 and eps>0
    # q_N monic, all roots in (0,1); and M(x)>4 on [0,1].
    # epsilon*|q(t)|<=1: P_epsilon=(1-x)(M+epsilon q)>0.
    lower=eps*norm2/q16
    upper=Fraction(16,15)*lower
    assert lower<upper
    return {'N':N,'coefficients':c,'epsilon':eps,'q16':q16,
            'L2sq':norm2,'lower_delta_pi':lower,'upper_delta_pi':upper}


def first_moment_differences(N):
    c=monic_orthogonal(N)
    return [sum((a*moment(j+k) for j,a in enumerate(c)),Fraction())
            for k in range(N+3)]


if __name__=='__main__':
    for N in range(6):
        cert=root_certificate(N)
        assert first_moment_differences(N)[:N+1]==[0]*(N+1)
        print(N, 'q(16) bits', cert['q16'].numerator.bit_length(),
              'bound',float(cert['lower_delta_pi']),float(cert['upper_delta_pi']))
