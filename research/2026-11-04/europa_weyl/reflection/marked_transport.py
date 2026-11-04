"""Finite signed arithmetic -> selected orbit and marked orbit -> source tests."""
from fractions import Fraction as F
from math import comb
import json

from referee_probe import chi, log_vector


def signed_tape(nmax):
    values = [{} for _ in range(nmax+1)]
    for n in range(2,nmax+1):
        factors = log_vector(n)
        if len(factors)==1 and chi(n):
            p = next(iter(factors))
            values[n] = {p: chi(n)}
    return values


def reconstruct_coefficients(rows):
    """Read b(d) in the rational basis of log primes. Recover Dirichlet a(n)."""
    a = [F(0), F(1)]
    for n in range(2,len(rows)):
        tmp = {}
        for d in range(2,n+1):
            if n % d == 0:
                for p,v in rows[d].items():
                    tmp[p] = tmp.get(p,0) + v * a[n//d]
        factors = log_vector(n)
        p0 = next(iter(factors))
        c = tmp.get(p0,0) / F(factors[p0])
        assert all(tmp.get(p,0) == c*factors.get(p,0) for p in tmp.keys()|factors.keys())
        a.append(c)
    return a


def orbit_from_beta(n):
    a = reconstruct_coefficients(signed_tape(8*n-1))
    deg = 8*n-2
    q = [a[l+1] - F(sum((-1)**j*comb(8*n,j)*a[l+1-j] for j in range(l+1)),16**n) for l in range(deg+1)]
    taps = [4*(-1)**j*sum(comb(l,j)*q[l] for l in range(j,deg+1)) for j in range(deg+1)]+[F(0)]
    return [F(0)] + [16**(k-1)*sum(taps[j]/(j+1) for j in range(8*k)) for k in range(1,n+1)]


ANG = (F(2),F(2),F(1),F(0),F(-1,2),F(-1,2),F(-1,4),F(0))


def direct(n,seed=F(0)):
    ys = [seed]
    for k in range(n):
        ys.append(16*ys[-1]+sum(w/(8*k+j) for j,w in enumerate(ANG,1)))
    return ys


def recover_taps(start,phases):
    """Eliminate the rational Cauchy system. Inputs are exact circle coordinates."""
    matrix = []
    for i in range(8):
        row = [F(1,8*(start+i)+j) for j in range(1,9)]
        row.append((phases[i+1]-16*phases[i])%1)
        matrix.append(row)
    for j in range(8):
        pivot = matrix[j][j]
        matrix[j] = [v/pivot for v in matrix[j]]
        for k in range(8):
            if j != k:
                scale = matrix[k][j]
                matrix[k] = [u-scale*v for u,v in zip(matrix[k],matrix[j])]
    return tuple(row[-1] for row in matrix)


if __name__=='__main__':
    shifts=[]
    for start in (4,18,37):
        ys = [y%1 for y in direct(start+8)[start:]]
        other = [y%1 for y in direct(start+8,F(1,5))[start:]]
        assert recover_taps(start, ys) == recover_taps(start,other) == ANG
        assert ys[0] != other[0]
        assert recover_taps(start,list(reversed(ys))) != ANG
        shifts.append(start)
    lengths=[]
    for n in (6,18,35):
        assert orbit_from_beta(n) == direct(n)
        lengths.append(n)
    print(json.dumps({'ordered_windows':shifts,'full_rational_histories_from_beta':lengths,
                      'seed_blindness_verified':True,'reverse_order_mutation_rejected':True},indent=2))
