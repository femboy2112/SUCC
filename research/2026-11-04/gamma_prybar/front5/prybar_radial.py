"""Reproducible radial saturation and finite-part diagnostics (stdlib, mpmath)."""
from fractions import Fraction as F
import json
from math import isqrt

import mpmath as mp

RADIAL = (2, -2, -1, -2, F(-1, 2), F(-1, 2), F(1, 4), 0)


def tap_sum(k, stop):
    return sum((F(RADIAL[j], 8*k+j+1) for j in range(stop)), F())


def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n)+1))


def mod_unit(x, p):
    return x.numerator * pow(x.denominator, -1, p) % p


def probe():
    u = v = F()
    z = [F()]
    delta_sum = corrected = forcing_sum = F()
    for n in range(1, 304):
        x = 8*n
        original = F(4, x-7)-F(2, x-4)-F(1, x-3)-F(1, x-2)
        dual = F(8, x-6)+F(4, x-5)+F(4, x-4)-F(1, x-1)
        u = 16*u + original
        v = 16*v + dual
        z.append(16*z[-1]+tap_sum(n-1,8))
        delta = v-2*u
        assert delta == -4*z[n]
        assert 0 < z[n] < F(1,32*n+16)
        assert 16*z[n-1]+tap_sum(n-1,8)-F(1,4*(x-1)) != z[n]
        delta_sum += delta
        corrected += delta + F(1,8*n)
        forcing_sum += dual - 2*original
        assert 15*delta_sum == 16*delta - forcing_sum

    for k in (0,1,4,13,47):
        for ell in range(1,9):
            assert (16*z[k]+tap_sum(k,ell)>0) == (ell!=6)

    # Every final p-slot is determined by the integer horizon; the
    # independent oracle is the original/dual rational state above.
    rows = []
    for n in (77,163,303):
        cancels, count = [], 0
        for p in range(isqrt(8*n)+1,8*n-6):
            if not prime(p):
                continue
            m = 8*n//p
            k, idx = divmod(m-1,8)
            ell = idx+1
            j = ((p*ell-1)%8)+1
            t = (m*p+8-j)//8
            chi = 1 if p%8 in (1,7) else -1
            factor = chi**ell * F(2)**((ell+8-j)//2)
            normalizer = factor*(z[k]+tap_sum(k,ell)/16)
            pred = mod_unit(normalizer,p)*pow(16,n-t,p)%p
            assert pred == mod_unit(p*z[n],p)
            if not pred:
                cancels.append(p)
            count += 1
        rows.append(dict(N=n,checked=count,finite_cancellations=cancels))

    with mp.workdps(60):
        root = mp.sqrt(2)
        closed = (mp.pi*(5*root+3)/2 + 15*root*mp.log1p(root)-34*mp.log(2))/120
        digamma = sum(w*(mp.digamma(mp.mpf(j)/8)+mp.euler)
                      for j,w in enumerate((-8,8,4,8,2,2,-1),1))/120
        assert abs(closed-digamma)<mp.mpf('1e-55')
        partial = mp.mpf(corrected.numerator)/corrected.denominator
        assert 0 < closed-partial < mp.mpf('0.001')
        return dict(simple_poles=rows,slots=40,exact_lift_times=303,
                    finite_part=mp.nstr(closed,30),
                    corrected_partial_at_303=mp.nstr(partial,30))

if __name__ == '__main__':
    print(json.dumps(probe(),indent=2,sort_keys=True))
