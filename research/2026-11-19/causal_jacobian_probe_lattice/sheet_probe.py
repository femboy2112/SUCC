"""Finite exact controls for SUCC Fibonacci pulse-sheet Jacobians; not pi normality."""
from math import comb
from itertools import permutations


def sheet(n):
    """Cyclic Fibonacci disturbance Jacobian K=S+S^2, integer entries."""
    return [[int(i == (j+1)%n) + int(i == (j+2)%n)
             for j in range(n)] for i in range(n)]


def det(a):
    total=0
    for p in permutations(range(len(a))):
        s=sum(p[i]>p[j] for i in range(len(a)) for j in range(i+1,len(a)))
        v=1
        for i in range(len(a)): v *= a[i][p[i]]
        total+=(-1 if s%2 else 1)*v
    return total


def run():
    for n in (3,5,6,7,8):
        K=sheet(n)
        # Constant vector: sheet multiplier 2, hence radix 16 only mod 7.
        assert [sum(row) for row in K]==[2]*n
        assert all(sum(row)%7 == 16%7 for row in K)
        assert all(sum(row)%11 != 16%11 for row in K)
        assert all(sum(row)%2 == 0 for row in K)
        if n%2==0:
            alt=[(-1)**j for j in range(n)]
            assert all(sum(K[i][j]*alt[j] for j in range(n))==0 for i in range(n))
            assert det(K)==0
        else:
            assert abs(det(K))==2
    # Sum paths on the triangular sheet along n=x+2y: F_(n+1).
    Fib=[0,1]
    for k in range(2,20): Fib.append(Fib[-1]+Fib[-2])
    for n in range(16):
        coeff=sum(comb(n-y,y) for y in range(n//2+1))
        assert coeff==Fib[n+1]
    print('Fibonacci sheet Jacobian: exact finite controls passed')

if __name__=='__main__': run()
