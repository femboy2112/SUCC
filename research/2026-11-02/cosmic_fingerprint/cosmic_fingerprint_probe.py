#!/usr/bin/env python3
"""Exact finite calibrations for causal-foreground and reference interferometry.

All identities use Q(i), integer causal frequencies, and exact group-ring
coefficients.  No pi digits, trig floats, or assumption of normality.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from collections import defaultdict
from math import isqrt
import unittest


@dataclass(frozen=True)
class G:
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))

    def __add__(self, other):
        if isinstance(other, (int, F)): other = G(other)
        return G(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.a, -self.b)

    def __sub__(self, other):
        return self + -G(other) if isinstance(other, (int,F)) else self + -other

    def __mul__(self, other):
        if isinstance(other, (int, F)): other = G(other)
        return G(self.a*other.a - self.b*other.b,
                 self.a*other.b + self.b*other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        assert isinstance(other, (int,F)) and other != 0
        return G(self.a/F(other), self.b/F(other))

    def conj(self):
        return G(self.a, -self.b)

    def abs2(self):
        return self.a*self.a + self.b*self.b


ZERO = G(0)
ONE = G(1)
I = G(0, 1)
UNITS = (ONE, -ONE, I, -I, G(F(3,5), F(4,5)),
         G(F(5,13), -F(12,13)))
assert all(z.abs2() == 1 for z in UNITS)


def phases(M: int, offset: int = 0) -> list[G]:
    return [UNITS[(5*n + offset) % len(UNITS)] for n in range(M)]


def field(z: list[G], base=16, start=1) -> dict[int,G]:
    return {base**(start+n): x for n,x in enumerate(z)}


def ring_multiply(left: dict[int,G], right: dict[int,G]):
    out = defaultdict(lambda: ZERO)
    for a,x in left.items():
        for b,y in right.items():
            out[a+b] = out[a+b] + x*y
    return dict(out)


def ring_conjugate(polynomial: dict[int,G]):
    return {-k:v.conj() for k,v in polynomial.items()}


def intensity_unscaled(z: list[G], base=16, start=1):
    p = field(z,base,start)
    return ring_multiply(p,ring_conjugate(p))


def centered_covariance(z: list[G],w: list[G],base=16,start=1) -> G:
    assert len(z) == len(w) and all(q.abs2()==1 for q in z+w)
    M = len(z)
    a = intensity_unscaled(z,base,start)
    c = intensity_unscaled(w,base,start)
    return sum((x*y.conj() for k,x in a.items() if k and (y:=c.get(k)) is not None), ZERO)/(M*M)


def overlap(z:list[G], w:list[G]) -> G:
    assert len(z)==len(w)
    return sum((a*b.conj() for a,b in zip(z,w)),ZERO)


def phased_mixed_intensity(z:list[G], w:list[G], v:G) -> F:
    assert v.abs2()==1
    return sum(((a+v*b).abs2() for a,b in zip(z,w)),F(0))


def closure(z:list[G], idx=(0,1,2)) -> G:
    i,j,k=idx
    vis=lambda a,b:z[a]*z[b].conj()
    return vis(i,j)*vis(j,k)*vis(k,i)


def rank2_closure(z:list[G],w:list[G],lam:F,idx=(0,1,2)) -> G:
    i,j,k=idx
    vis=lambda a,b: lam*z[a]*z[b].conj()+(1-lam)*w[a]*w[b].conj()
    return vis(i,j)*vis(j,k)*vis(k,i)


class CosmicFingerprintExact(unittest.TestCase):
    def test_exact_Qi_arithmetic_and_normalization(self):
        for x in UNITS:
            self.assertEqual(x*x.conj(),ONE)
        self.assertEqual((G(F(3,5),F(4,5))*G(F(5,13),-F(12,13))).abs2(),1)

    def test_causal_sidonic_frequency_uniqueness(self):
        for b in (2,3,5,16):
            for M in (2,3,5,9):
                freqs={}
                for n in range(1,M+1):
                    for m in range(1,M+1):
                        if n==m: continue
                        f=b**n-b**m
                        self.assertNotIn(f,freqs)
                        freqs[f]=(n,m)
                self.assertEqual(len(freqs),M*(M-1))

    def test_monopole_and_auto_power_are_phase_blind(self):
        for b in (2,16):
            for M in range(2,12):
                for z in ([ONE]*M,phases(M,1),phases(M,2)):
                    spec=intensity_unscaled(z,b)
                    self.assertEqual(spec[0],G(M))
                    self.assertEqual(len(spec),M*(M-1)+1)
                    for k,v in spec.items():
                        if k:self.assertEqual(v.abs2(),1)
                    centered=sum((v.abs2() for k,v in spec.items() if k),F(0))/M**2
                    self.assertEqual(centered,F(M-1,M))

    def test_matched_centered_cross_equals_squared_temporal_overlap(self):
        for b in (2,3,16):
            for M in range(2,12):
                for z,w in ((phases(M,1),[ONE]*M),
                            (phases(M,1),phases(M,3)),
                            ([ONE]*M,[ONE]*M)):
                    measured=centered_covariance(z,w,b)
                    expected=G(F(overlap(z,w).abs2()-M,M*M))
                    self.assertEqual(measured,expected)
                    self.assertEqual(measured.b,0)

    def test_reference_contrast_is_exact_weyl_modulus_squared(self):
        for M in range(2,20):
            z=phases(M)
            C=centered_covariance(z,[ONE]*M)
            S=sum(z,ZERO)
            self.assertEqual(C,G(F(S.abs2()-M,M*M)))
            self.assertGreaterEqual(C.a,F(-1,M))
            self.assertLessEqual(C.a,F(M-1,M))
            self.assertEqual(centered_covariance([ONE]*M,[ONE]*M),G(F(M-1,M)))

    def test_two_phase_stepped_global_nonnegative_intensities(self):
        for M in range(1,18):
            for z,w in ((phases(M,1),[ONE]*M),
                        (phases(M,3),phases(M,2)),
                        ([ONE]*M,[ONE]*M)):
                S=overlap(z,w)
                base=2*M
                i0=phased_mixed_intensity(z,w,ONE)
                i90=phased_mixed_intensity(z,w,I)
                self.assertGreaterEqual(i0,0)
                self.assertGreaterEqual(i90,0)
                self.assertEqual(i0-base,2*S.a)
                self.assertEqual(i90-base,2*S.b)
                recovered=G((i0-base)/2,(i90-base)/2)
                self.assertEqual(recovered,S)

    def test_all_rank_one_closure_phases_are_trivial(self):
        for M in (3,4,7,11):
            for z in ([ONE]*M,phases(M,1),phases(M,3)):
                for i in range(M-2):
                    self.assertEqual(closure(z,(i,i+1,i+2)),ONE)

    def test_mixed_component_can_have_nontrivial_closure(self):
        z=[ONE,ONE,ONE]
        w=[ONE,I,G(F(3,5),F(4,5))]
        val=rank2_closure(z,w,F(1,5))
        self.assertEqual(val,G(F(93,125),-F(24,625)))
        self.assertNotEqual(val.b,0)
        self.assertEqual(rank2_closure(z,w,F(1,2)).b,0)

    def test_translate_one_source_vs_translate_both(self):
        # Exact group-ring gauge: shifting seed by rational s multiplies
        # the nth field coefficient by exp(2pi i b^n s). Choose s=1/4,
        # b=2, producing phases in {1,-1,i,-i} exactly.
        b=2;sden=4; M=6
        twiddle={0:ONE,1:I,2:-ONE,3:-I}
        t=[twiddle[(b**(n+1))%sden] for n in range(M)]
        z=phases(M,1)
        w=[ONE]*M
        shifted=[a*u for a,u in zip(z,t)]
        shifted_ref=[a*u for a,u in zip(w,t)]
        self.assertEqual(overlap(shifted,shifted_ref),overlap(z,w))
        self.assertEqual(centered_covariance(shifted,shifted_ref,base=b),
                         centered_covariance(z,w,base=b))
        # A reference held at the authentic seed origin is NOT gauge blind.
        self.assertNotEqual(overlap(shifted,w),overlap(z,w))

    def test_two_channel_component_separation_rank(self):
        z=phases(6,1);ref=[ONE]*6
        # Y1 = signal + template; Y2 = 2*signal + 3*template.
        y1=[a+b for a,b in zip(z,ref)]
        y2=[2*a+3*b for a,b in zip(z,ref)]
        self.assertEqual([3*a-b for a,b in zip(y1,y2)],z)
        self.assertEqual([b-2*a for a,b in zip(y1,y2)],ref)
        # Identical channel mixtures have a nontrivial kernel.
        self.assertEqual([2*a for a in y1],
                         [2*a+2*b for a,b in zip(z,ref)])

    def test_source_phase_template_drifts_have_uniform_bound(self):
        # Deterministic |z_n|=|t_n|=1 and |1-t_n|<=epsilon_n.
        for M in range(2,16):
            z=phases(M,1);t=phases(M,2)
            baseline=sum(z,ZERO);mixed=overlap(z,t)
            defect=baseline-mixed
            budget=sum((F(1)-q.a for q in t),F(0))
            self.assertLessEqual(defect.abs2(),2*budget*M)
            # The stronger exact Euclidean norm inequality follows from C-S.

    def test_prefix_bandwidth_cannot_see_last_phase(self):
        for b in (2,3,16):
            for M in range(2,10):
                z=phases(M,1);v=z[:-1]+[-z[-1]]
                a=intensity_unscaled(z,b)
                c=intensity_unscaled(v,b)
                band=(b-1)*b**(M-1)
                self.assertEqual({k:x for k,x in a.items() if abs(k)<band},
                                 {k:x for k,x in c.items() if abs(k)<band})
                self.assertNotEqual(a,c)

    def test_background_residual_L2_stability(self):
        # A known real residual epsilon(s)=a*e(k s)+a*e(-k s).
        # The matched-filter error obeys |<epsilon,A_w>| <=
        # ||epsilon||_2 sqrt((M-1)/M), independently of signal phases.
        for b in (2,3,16):
            for M in (2,3,5,9):
                z=phases(M,1);w=[ONE]*M
                original=centered_covariance(z,w,b)
                k=b**M-b**(M-1)
                amp=F(1,17)
                error_spec={k:G(amp),-k:G(amp)}
                ref=intensity_unscaled(w,b)
                noise_overlap=sum((a*ref[-kk].conj()
                                   for kk,a in error_spec.items()),ZERO)/M
                self.assertEqual(noise_overlap,G(2*amp/M))
                self.assertEqual((original+noise_overlap-original).a,2*amp/M)
                # ||epsilon||² = 2amp², ||A_w||²=(M-1)/M
                self.assertLessEqual((2*amp/M)**2,
                                     2*amp*amp*F(M-1,M))

    def test_p257_inherited_certified_source_vs_coherent_shadow_contrast(self):
        # Inherited original BBP source (SPP-10, PR #459) has certified
        # |S|/96<1/16 on n=33..128 for h=1; this test does not reprove it.
        M=96
        original_strict_upper=F(1,16)**2-F(1,M)
        self.assertEqual(original_strict_upper,-F(5,768))
        # Coherent shadow n>=33 has d_n<1/(8*n+1)^2. For h=1,
        # the uniform phase distance to e(2/15) is < 2pi/265².
        # Use the rational upper 2pi<44/7 to make a strict guarantee.
        epsilon=F(44,7*265**2)
        coherent_lower=(1-epsilon)**2-F(1,M)
        self.assertGreater(coherent_lower,F(989,1000))
        self.assertLess(original_strict_upper,F(0))
        self.assertGreater(coherent_lower,F(0))

    def test_certified_foreground_noise_robust_p257_sign_gap(self):
        # CF-06 supplies |deltaC|<=||eta||_2 ||A_beacon||_2<||eta||_2.
        # Exact source certificate inherited SPP-10, not refitted here.
        sigma=F(1,512)
        original_upper=-F(5,768)+sigma
        shadow_lower=F(989,1000)-sigma
        self.assertEqual(original_upper,-F(7,1536))
        self.assertLess(original_upper,0)
        self.assertGreater(shadow_lower,F(987,1000))

    def test_coherent_reference_has_maximum_alignment(self):
        for M in range(2,15):
            z=[ONE]*M
            self.assertEqual(centered_covariance(z,z),G(F(M-1,M)))
            self.assertEqual(phased_mixed_intensity(z,z,ONE),4*M)
            self.assertEqual(phased_mixed_intensity(z,z,I),2*M)

if __name__=='__main__':
    unittest.main(verbosity=2)
