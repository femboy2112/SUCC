"""Independent exact flat source implementation, separate from epoch_fejer."""
from fractions import Fraction

def pole(n):
    num=120*n*n-89*n+16
    den=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    return Fraction(num,den)

def phase_iter(n):
    q=Fraction(0)
    for i in range(1,n+1): q=(16*q+pole(i))%1
    return q

def check():
    # Check first, middle and later selected zero-seed real phases by closed unwrapped expansion.
    for n in (0,1,2,4,7,11,16,32,64,127,255):
        closed=sum((16**(n-j)*pole(j) for j in range(1,n+1)),Fraction(0))%1
        assert phase_iter(n)==closed,(n,phase_iter(n),closed)
    for A in (1,4,32,128):
        summation=sum((Fraction(1,15*(n+1)**2) for n in range(A,2*A)),Fraction(0))/A
        assert summation<=Fraction(1,30*A*A)
    return {"independent_fraction_checks":11,"independent_mean_tail_checks":4,"status":"PASS"}
if __name__=='__main__':print(check())
