"""Exact two-sinc Borwein leakage probes for zero-seeded BBP circle orbit.

All finite arithmetic exact; convergence/normality claims require independent
analytic proofs and the missing all-shell lower/difference estimates.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, pi
import unittest

DELTA=F(1,18)
A=1-DELTA
C=F(1,2)/A**2
HAAR=F(256,7803)


def torus(x):
    r=F(x)%1
    return min(r,1-r)


def leak(theta):
    gap=max(torus(theta)-DELTA,F(0))
    return C*gap*gap


def forcing(n):
    if n<1: raise ValueError('n>=1')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


@lru_cache(None)
def terminal(N):
    U=F(0)
    for n in range(1,N+1):U=16*U+forcing(n)
    return U


def shell_phases(B):
    U=terminal(2*B)
    return tuple((U/16**k)%1 for k in range(1,B+1))


def swept(values, origin=F(0)):
    return sum((leak(x-origin) for x in values),F(0))/len(values)


def shadow_energy(B,origin=F(0)):
    return swept(shell_phases(B),origin)


def shadow_error_bound(B):
    # L=2*C*(1/2-DELTA)=144/289; T_(2B) < r(2B+1)/15.
    return F(16,7225*B)*forcing(2*B+1)


def supremum_exact(values):
    """Exact sup over a circle origin of |mean leak(phase-origin)-HAAR|.

    Its piecewise quadratic knots are all source phases +/- delta or 1/2.
    Each quadratic vertex is rational and can be checked exactly.
    """
    vals=tuple(F(x)%1 for x in values)
    knots={F(0),F(1)}
    for x in vals:
        for sh in (F(0),DELTA,-DELTA,F(1,2)):
            knots.add((x+sh)%1)
    pts=sorted(knots)
    maxerr=F(0)
    for aa,bb in zip(pts[:-1],pts[1:]):
        mid=(aa+bb)/2
        half=(bb-aa)/2
        va=swept(vals,aa)-HAAR
        vm=swept(vals,mid)-HAAR
        vb=swept(vals,bb)-HAAR
        quad=(va+vb-2*vm)/(2*half*half)
        lin=(vb-va)/(2*half)
        candidates=[va,vm,vb]
        if quad:
            vertex=mid-lin/(2*quad)
            if aa<=vertex<=bb:
                candidates.append(swept(vals,vertex)-HAAR)
        for q in candidates:maxerr=max(maxerr,abs(q))
    return maxerr


def borwein_first_leak_probability():
    widths=[F(1,2*j+1) for j in range(1,8)]
    excess=sum(widths)-1
    assert 0<excess<2*min(widths)
    denominator=factorial(len(widths))
    for width in widths:denominator*=2*width
    return 2*excess**len(widths)/denominator


class BorweinBbpSweepTests(unittest.TestCase):
    def test_borwein_first_strict_support_escape_volume(self):
        self.assertEqual(borwein_first_leak_probability(),
            F(6879714958723010531,467807924720320453655260875000))
        self.assertLess(sum((F(1,2*j+1) for j in range(1,7))),1)
        self.assertGreater(sum((F(1,2*j+1) for j in range(1,8))),1)

    def test_two_sinc_leak_is_quadratic_rational_hinge(self):
        self.assertEqual(C,F(162,289))
        self.assertEqual(C*F(4,9)**2,F(32,289))
        self.assertEqual(2*C*F(4,9)**3/3,HAAR)
        for d in (F(0),F(1,25),DELTA,F(1,17),F(1,15),F(1,3),F(1,2)):
            expected=C*max(d-DELTA,F(0))**2
            self.assertEqual(leak(d),expected)
            self.assertEqual(leak(1-d),expected)

    def test_fixed_threshold_below_dynamical_barrier(self):
        self.assertLess(DELTA,F(1,17))
        threshold=F(35,612)  # midpoint of 1/18 and 1/17
        self.assertTrue(DELTA<threshold<F(1,17))
        self.assertEqual(threshold-DELTA,F(1,612))
        self.assertEqual(leak(F(1,17)),C*F(1,306)**2)
        self.assertGreater(leak(F(1,17)),0)
        self.assertEqual(leak(0),0)

    def test_cold_run_uses_exact_radix_expansion(self):
        threshold=F(35,612)
        coldcap=F(256,255)*threshold**2
        for L in (1,2,3,10):
            x=threshold/F(2*16**(L-1))
            orbit=[torus(16**j*x) for j in range(L)]
            self.assertTrue(all(d<threshold for d in orbit))
            self.assertLess(sum((d*d for d in orbit),F(0)),coldcap)
            self.assertEqual(orbit[-1],threshold/2)

    def test_borwein_energy_is_bounded_by_phase_energy(self):
        for x in (F(0),F(1,17),F(1,15),F(1,7),F(13,37)):
            for B in (4,8,16,32):
                vals=[(16**n*x)%1 for n in range(B,2*B)]
                j=swept(vals)
                e=sum((torus(y)**2 for y in vals),F(0))/B
                self.assertLessEqual(j,C*e)

    def test_original_zero_seed_rational_shadow_and_tail(self):
        for B in (4,8,16,32,64,128):
            u=terminal(2*B)
            direct=sum((forcing(n)*16**(2*B-n) for n in range(1,2*B+1)),F(0))
            self.assertEqual(u,direct)
            self.assertGreater(shadow_energy(B),0)
            self.assertLess(shadow_error_bound(B),F(1,10**3))

    def test_origin_sweep_has_exact_rational_maximum(self):
        for x in (F(0),F(1,17),F(1,15),F(3,7)):
            vals=[(16**n*x)%1 for n in range(8,16)]
            sup=supremum_exact(vals)
            self.assertGreaterEqual(sup,abs(swept(vals,F(0))-HAAR))
            self.assertGreaterEqual(sup,abs(swept(vals,F(1,7))-HAAR))
            self.assertGreater(sup,0)
        for B in (4,8,16,32):
            vals=shell_phases(B)
            sup=supremum_exact(vals)
            self.assertGreater(sup,0)
            self.assertGreaterEqual(sup,abs(swept(vals,F(0))-HAAR))

    def test_fourier_transfer_never_zero(self):
        # For k=2*pi*h, hat(L)(h)=4*C[(4/9)*(-1)^h/k²+sin(k/18)/k³].
        # |(4/9)k|>1 for every integer h!=0 (since pi>3).
        from math import sin
        for h in range(1,201):
            k=2*pi*h
            transfer=4*float(C)*(float(F(4,9))*(-1)**h/k**2 + sin(k/18)/k**3)
            self.assertNotEqual(transfer,0)
            self.assertGreater(transfer*(-1)**h,0)
            lb=4*float(C)*(float(F(4,9))*k-1)/k**3
            self.assertGreaterEqual(abs(transfer)+1e-17,lb)

    def test_locked_and_nonunit_fixed_orbits_are_separated(self):
        for x in (F(0),F(1,15),F(1,17)):
            vals=[(16**n*x)%1 for n in range(16,32)]
            score=swept(vals)
            if x==0:self.assertEqual(score,0)
            else:self.assertGreater(score,0)
            self.assertGreater(supremum_exact(vals),0)

if __name__=='__main__':unittest.main()
