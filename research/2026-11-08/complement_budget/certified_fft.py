"""Integer FFT with a proved common complex L1 error radius.

Centers have denominator SCALE. Every arithmetic operation below is integer;
phase() supplies inherited outward rational Taylor enclosures. This is a finite
certificate, not a floating FFT error estimate. See THEOREMS.md, CB-FFT.
"""
from functools import lru_cache
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT), str(HERE.parent / 'covariance_forge')]
from intervals import SCALE, phase


def ceildiv(a, b):
    return -((-a) // b)


def center(box):
    a = (box.re.lo + box.re.hi) // 2
    b = (box.im.lo + box.im.hi) // 2
    radius = max(a-box.re.lo, box.re.hi-a) + max(b-box.im.lo, box.im.hi-b)
    return (a, b), radius


def multiply(a, b):
    # Each coordinate is rounded downward, costing <2/SCALE in complex L1.
    return ((a[0]*b[0]-a[1]*b[1]) // SCALE,
            (a[0]*b[1]+a[1]*b[0]) // SCALE)


@lru_cache(maxsize=2)
def roots(n, sign):
    values = [center(phase(sign*j, n)) for j in range(n//2)]
    return tuple(v[0] for v in values), max((v[1] for v in values), default=0)


def fft(values, radius=0, sign=-1):
    """Unnormalized DFT on a power-of-two length, common L1 error radius."""
    n = len(values)
    if not n or n & (n-1) or sign not in (-1, 1) or radius < 0:
        raise ValueError('power-of-two length, nonnegative radius, sign +/-1 required')
    a = list(values)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    ws, rw = roots(n, sign)
    length = 2
    while length <= n:
        bound = max(abs(x)+abs(y) for x, y in a)
        radius = 3*radius + ceildiv(rw*bound, SCALE) + 2
        half, stride = length//2, n//length
        for start in range(0, n, length):
            for j in range(half):
                u = a[start+j]
                v = multiply(ws[j*stride], a[start+j+half])
                a[start+j] = (u[0]+v[0], u[1]+v[1])
                a[start+j+half] = (u[0]-v[0], u[1]-v[1])
        length *= 2
    return a, radius


class PrimeDFT:
    """Bluestein DFT for arbitrary length p; no primality assumption needed."""
    def __init__(self, p):
        if type(p) is not int or p < 2:
            raise ValueError('integer length >=2 required')
        self.p = p
        self.n = 1 << (2*p-2).bit_length()
        self.chirp = [center(phase(-j*j, 2*p)) for j in range(p)]
        b = [(0, 0)] * self.n
        radius = 0
        for j in range(p):
            (x, y), r = self.chirp[j]
            b[j] = (x, -y)
            if j:
                b[self.n-j] = (x, -y)
            radius = max(radius, r)
        self.fb, self.rb = fft(b, radius)

    def transform(self, values, radius=0):
        if len(values) != self.p or radius < 0:
            raise ValueError('matching length and nonnegative radius required')
        a = [(0, 0)] * self.n
        ra = 0
        for j, value in enumerate(values):
            w, rw = self.chirp[j]
            a[j] = multiply(value, w)
            ra = max(ra, 2*radius + ceildiv(rw*(abs(value[0])+abs(value[1])), SCALE)+2)
        fa, ra = fft(a, ra)
        ba = max(abs(x)+abs(y) for x, y in fa)
        bb = max(abs(x)+abs(y) for x, y in self.fb)
        product_radius = ceildiv(ra*bb + self.rb*ba + ra*self.rb, SCALE) + 2
        fc = [multiply(x, y) for x, y in zip(fa, self.fb)]
        conv, rc = fft(fc, product_radius, sign=1)
        rc = ceildiv(rc, self.n) + 2
        out = []
        rout = 0
        for j in range(self.p):
            value = (conv[j][0]//self.n, conv[j][1]//self.n)
            w, rw = self.chirp[j]
            out.append(multiply(value, w))
            rout = max(rout, 2*rc+ceildiv(rw*(abs(value[0])+abs(value[1])), SCALE)+2)
        return out, rout
