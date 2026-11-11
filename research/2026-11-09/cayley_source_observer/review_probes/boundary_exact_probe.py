"""Preserved boundary-review probe; rerun from the repository root.

The body is copied from the previously executed inline review command.
Run without Python -O: assertions are the deliberate finite probe gates.
"""
from fractions import Fraction as F
from math import floor

if not __debug__:
    raise RuntimeError("This review probe must run with assertions enabled")


def dist(x, c=F(0)):
    y = (x-c) % 1
    return min(y, 1-y)


def arc(x, c, r):
    return dist(x, c) < r


cases = 0
for t0 in (F(0), F(1, 32), F(1, 16), F(1, 5), F(5, 17), F(7, 113)):
    for A in (1, 2, 7, 64):
        ts = [t0]
        for _ in range(A):
            ts.append(16*ts[-1] % 1)
        us = [8*t % 1 for t in ts]
        nu = lambda pred: F(sum(pred(u) for u in us[:-1]), A)
        b, q = [], []
        for j in range(5):
            r = F(1, 4*16**j)
            v = nu(lambda u: arc(u, F(0), r))
            w = nu(lambda u: arc(u, F(1, 2), r))
            b.append(v+w)
            q.append(v-w)
        assert b[0] <= 1
        for j in range(4):
            r = F(1, 4*16**j)
            rnext = r/16
            e = F(int(arc(us[-1], F(0), r))-int(arc(us[0], F(0), r)), A)
            omitted = nu(lambda u: arc(16*u % 1, F(0), r) and not (
                arc(u, F(0), rnext) or arc(u, F(1, 2), rnext)))
            assert b[j+1] == (b[j]+q[j])/2+e-omitted
        for J in range(5):
            upper = b[0]/2**J+sum(q[j]/2**(J-j) for j in range(J)) \
                + F(2, A)*(1-F(1, 2**J))
            assert b[J] <= upper
            d = F(1, 32*16**J)
            cuts = [F(j, 16) for j in range(16)]
            strip = F(sum(min(dist(t, c) for c in cuts) < d for t in ts[:-1]), A)
            assert b[J] == strip
        cases += 1

for H in range(300):
    K = (H+8)//16
    L = 64*K-F(512*K*K, H+1)
    direct = sum(32*(1-F(abs(m), H+1))
                 for m in range(-H, H+1) if m % 16 == 8)
    assert L == direct and L <= 2*(H+1)
    if H % 16 == 15:
        assert L == 2*(H+1)

for A in range(1, 25):
    for L in (2*A-1, 2*A, 2*A+3):
        B = F(4, 15*(L+1)**2*16**L)
        direct = sum(16**n*B for n in range(A, 2*A))/A
        assert direct == B*16**A*(16**A-1)/F(15*A)
        if L == 2*A:
            assert direct == F(4)*(1-F(1, 16**A))/F(225*A*(2*A+1)**2)
        if L == 2*A-1:
            assert direct == (16-F(16, 16**A))/F(225*A**3)

print({'exact_finite_recursion_cases': cases, 'lip_cutoffs': 300,
       'source_width_cases': 72, 'status': 'PASS',
       'boundary_convention': 'open'})
