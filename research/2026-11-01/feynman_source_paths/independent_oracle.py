"""Separately derived exact integer/rational BBP checks, no shared helper imports."""
from fractions import Fraction as F

def source(n):
    numerator=120*n*n-89*n+16
    denominator=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    return F(numerator,denominator)

def matrix_product(m):
    # Multiply source factors in the OPPOSITE direction from the primary loop.
    a=16**m
    b=sum((16**(m-j)*source(j) for j in range(1,m+1)),F(0))
    return a,b

def aggregate_variance(m):
    return sum(256**j for j in range(m))

def path_gaussian_covariance(m,epsilon):
    # Independently propagate variance as a linear noise recurrence.
    v=F(0)
    for _ in range(m):
        v=256*v+epsilon
    return v

def assert_stationarity(n,x,p,epsilon):
    assert len(x)==n+1 and len(p)==n
    for j in range(1,n+1):
        assert x[j]-16*x[j-1]-source(j)==epsilon*p[j-1]
    for j in range(1,n):
        assert p[j-1]==16*p[j]
    return True

def gaussian_packet_offset(n,moment):
    # position operator covariance, independently of original source
    a,b=matrix_product(n)
    return a*moment+b
