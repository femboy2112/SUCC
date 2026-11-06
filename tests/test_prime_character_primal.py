"""Exact tests for the source-derived mod8 character quotient and primal BBP.

Fresh p-source holdouts declared in GitHub preregistration, not used to fit
any character weights. No pi normality or external source data inserted.
"""
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from math import gcd, pi, sin, cos, hypot

HERE=Path(__file__).resolve().parents[1] / 'research/2026-11-04/prime_character_primal'
sys.path.insert(0,str(HERE))
import prime_character as m

PRIME_HOLDOUTS=(29,37,43,47,61,67,71,73,83,89,101,103,107,113,127,131,137,139,149,151,157)


def tent(d, q):
    d=Q(d)%1
    d=min(d,1-d)
    return max(Q(0), 1-Q(q)*d)


def J_energy(x, q):
    A=len(x)
    return Q(q,A*A)*sum((tent(a-b,q) for a in x for b in x),Q(0))


class PrimeCharacterPrimalExact(unittest.TestCase):
    def test_01_group_on_every_8_tap_basis(self):
        for a in m.CLASSES:
            for b in m.CLASSES:
                for j in range(8):
                    basis=tuple(Q(int(i==j)) for i in range(8))
                    self.assertEqual(m.shadow(a,m.shadow(b,basis)),m.shadow(a*b%8,basis))

    def test_02_group_characters_are_orthogonal_projectors(self):
        ch=('trivial','chi_minus4','chi_8','chi_minus8')
        for j in range(8):
            e=tuple(Q(int(i==j)) for i in range(8))
            self.assertEqual(sum_vec([m.proj(k,e) for k in ch]),e)
            for k in ch:
                self.assertEqual(m.proj(k,m.proj(k,e)),m.proj(k,e))
                for other in ch:
                    if other!=k:
                        self.assertEqual(m.proj(k,m.proj(other,e)),m.Z8)

    def test_03_character_dimensions(self):
        self.assertEqual(m.character_dimensions(),{'trivial':4,'chi_minus4':2,'chi_8':1,'chi_minus8':1})

    def test_04_source_echo_is_actual_dual_formula(self):
        self.assertEqual(m.shadow(1),m.P)
        self.assertEqual(m.shadow(5),m.P)
        self.assertEqual(m.shadow(3),m.scaled(Q(-1,2),m.DUAL))
        self.assertEqual(m.shadow(7),m.scaled(Q(-1,2),m.DUAL))
        self.assertEqual(m.shadow(3,m.DUAL),m.scaled(-2,m.P))
        self.assertEqual(m.shadow(5,m.DUAL),m.DUAL)

    def test_05_original_angular_and_radial_source_taps(self):
        a,r=m.angle_radial()
        self.assertEqual(a,(Q(2),Q(2),Q(1),Q(0),Q(-1,2),Q(-1,2),Q(-1,4),Q(0)))
        self.assertEqual(r,(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0)))
        self.assertEqual(m.add(a,r),m.P)
        self.assertEqual(m.proj('chi_8',m.P),m.Z8)
        self.assertEqual(m.proj('chi_minus8',m.P),m.Z8)

    def test_06_angular_is_chi4_eigen_and_radial_trivial(self):
        a,r=m.angle_radial()
        for residue in m.CLASSES:
            self.assertEqual(m.shadow(residue,a),m.scaled(m.chi_minus4(residue),a))
            self.assertEqual(m.shadow(residue,r),r)

    def test_07_source_orig_not_altered(self):
        for k in range(1,301):
            self.assertEqual(m.source(k),Q(4,8*k-7)-Q(2,8*k-4)-Q(1,8*k-3)-Q(1,8*k-2))
            self.assertEqual(m.source(k,m.DUAL),Q(8,8*k-6)+Q(4,8*k-5)+Q(4,8*k-4)-Q(1,8*k-1))

    def test_08_independent_prime_residue_all_four_classes(self):
        for p in PRIME_HOLDOUTS:
            for k in (1,2,3):
                if p>8*k:
                    actual=m.direct_p_local_state(p,k)
                    pred=m.prime_quotient_prediction(p,k)
                    self.assertEqual(actual,pred,(p,k))

    def test_09_full_fraction_prime_source_observer(self):
        for p in (29,43,47,61,71,83,103,137,151):
            for k in (1,2):
                actual=m.full_prime_state_residue(p,k)
                self.assertEqual(actual,m.prime_quotient_prediction(p,k))

    def test_10_angular_and_radial_eigen_residue_actual(self):
        a,r=m.angle_radial()
        for p in PRIME_HOLDOUTS:
            for k in (1,2,3):
                if p>8*k:
                    x=m.direct_p_local_state(p,k,a)
                    expected=m._fmod(m.chi_minus4(p%8)*m.state(k,a),p)
                    self.assertEqual(x,expected,(p,k,'angular'))
                    z=m.direct_p_local_state(p,k,r)
                    self.assertEqual(z,m._fmod(m.state(k,r),p),(p,k,'radial'))

    def test_11_angular_odd_denominator_every_source_index(self):
        a,_=m.angle_radial()
        for n in range(1,1025):
            x=m.angular_source_odd(n)
            self.assertEqual(x,m.source(n,a))
            self.assertEqual(x.denominator%2,1)

    def test_12_primitive_state_odd_denominator_and_exact_split(self):
        a,r=m.angle_radial()
        U=Y=Z=V=Q(0)
        for n in range(1,512):
            U=16*U+m.source(n)
            Y=16*Y+m.source(n,a)
            Z=16*Z+m.source(n,r)
            V=16*V+m.source(n,m.DUAL)
            self.assertEqual(Y+Z,U)
            self.assertEqual(4*Y,2*U+V)
            self.assertEqual(4*Z,2*U-V)
            self.assertEqual(Y.denominator%2,1)
            self.assertEqual(U.denominator%2,1)

    def test_13_radial_strict_positive_and_decay(self):
        a,r=m.angle_radial()
        Z=Q(0)
        for n in range(1,1530):
            Z=16*Z+m.source(n,r)
            self.assertGreater(Z,0)
            self.assertLess(Z,m.radial_defect_bound(n))

    def test_14_source_odd_inverse_branch_never_lost(self):
        a,_=m.angle_radial()
        x=Q(0)
        for n in range(1,511):
            x=(16*x+m.source(n,a))%1
            self.assertEqual(x.denominator%2,1)
            previous=m.primal_and_radial(n-1)[0]%1 if n<=45 else None
            if previous is not None:
                z=(x-m.source(n,a))%1
                j=(-z.numerator*pow(z.denominator,-1,16))%16
                self.assertEqual((z+j)/16,previous)

    def test_15_two_state_impulse_and_negative_4_clock(self):
        taps=[m.tap_impulse(None,n) for n in range(40)]
        self.assertEqual(taps[:5],[Q(2),Q(2),Q(1),Q(0),Q(-1,2)])
        for n in range(36):
            self.assertEqual(taps[n+4],-taps[n]/4)
            self.assertEqual(taps[n+2],taps[n+1]-taps[n]/2)

    def test_16_radial_and_angle_state_by_2_independent_recurrences(self):
        for n in (97,191,373):
            ang,rad=m.angle_radial()
            u=m.state(n,m.P);v=m.state(n,m.DUAL)
            y=m.state(n,ang);z=m.state(n,rad)
            self.assertEqual(y,(2*u+v)/4)
            self.assertEqual(z,(2*u-v)/4)
            self.assertLess(z,m.radial_defect_bound(n))

    def test_17_original_epoch_current_transfer_exact_bound(self):
        ang,rad=m.angle_radial()
        for A,q in ((16,2),(32,2),(32,8),(96,2)):
            u=list(m.states(2*A-1,m.P))[A:]
            y=list(m.states(2*A-1,ang))[A:]
            err=abs(J_energy(u,q)-J_energy(y,q))
            self.assertLess(err,m.epoch_triangle_current_error_ceiling(A,q))

    def test_18_base_minus4_series_is_alternating_positive_terms(self):
        pos=[]
        for k in range(40):
            t=m.negative_base4_source_term(k)
            self.assertEqual(t>0,k%2==0)
            pos.append(abs(t))
            if k:
                self.assertLess(pos[k],pos[k-1])
        # The reduced kernel itself proves this series is pi; do not infer
        # that its 40-term value yields any fact about pi's normality.

    def test_19_original_mutant_is_not_frobenius_pure_gaussian(self):
        bad=list(m.P);bad[0]+=1;bad=tuple(bad)
        self.assertNotEqual(m.shadow(5,bad),bad)
        self.assertNotEqual(m.proj('chi_minus4',bad),m.angle_radial()[0])
        self.assertNotEqual(m.proj('trivial',bad),m.angle_radial()[1])

    def test_20_prime_shadow_blind_to_a_rational_wrong_seed(self):
        # A p-integral seed difference contributes p*16^(kp)/5 ==0 mod p
        # while it shifts the real circle by 1/5 (as 16^n=1 mod5).
        for p in (11,13,17,19,29,37,43,47):
            for k in (1,2):
                if p>8*k:
                    true=m.prime_quotient_prediction(p,k)
                    fake=(true+m._fmod(Q(p,5)*16**(k*p),p))%p
                    self.assertEqual(fake,true)
                    self.assertEqual((Q(16)**(k*p)/5)%1,Q(1,5))

    def test_22_prime_transport_for_every_eight_tap_basis(self):
        # The theorem must be a natural action on the whole rational source
        # module, not an identity fitted to the pi coefficients.
        for prime in (11,13,17,19,23,29,31,41):
            for k in (1,2):
                if prime <= 8*k:
                    continue
                for slot in range(8):
                    basis=tuple(Q(int(i==slot)) for i in range(8))
                    self.assertEqual(m.direct_p_local_state(prime,k,basis),
                                     m.prime_quotient_prediction(prime,k,basis),
                                     (prime,k,slot))

    def test_23_primal_prime_pulses_all_signs_and_genuine_recurrence(self):
        for a in m.CLASSES:
            for mul in range(1,125):
                x=m.prime_angular_event_normalizer(a,mul)
                y=m.direct_angular_event_normalizer(a,mul)
                self.assertEqual(x,y,(a,mul))
                self.assertNotEqual(x,0)
                self.assertEqual(1 if x>0 else -1,m.angular_pulse_sign(a,mul))
        # Actual preregistered fresh multiplier holdouts.
        for a in m.CLASSES:
            for mul in (17,37,71,113,191):
                self.assertEqual(m.prime_angular_event_normalizer(a,mul),
                                 m.direct_angular_event_normalizer(a,mul))

    def test_24_independent_angular_integer_lcm_state_horizons(self):
        import math
        angle,_=m.angle_radial()
        for n in (128,257,509,911,1511):
            left=m.state(n,angle)
            A,conductor,right=m.angular_integer_lcm_state(n)
            self.assertEqual(left,right)
            self.assertEqual(Q(A,conductor),left)
            self.assertEqual(conductor%2,1)
            # This is a finite diagnostic, never a proof of the 8N limit.
            self.assertGreater(math.log(right.denominator)/n,7.0)

    def test_25_original_angular_p_local_survival_holdouts(self):
        from math import isqrt
        angle,_=m.angle_radial()
        # Independent sieve: not imported from the prime-Frobenius echo.
        def primes_below(upper):
            sieve=[True]*upper
            sieve[0]=sieve[1]=False
            for d in range(2,isqrt(upper-1)+1):
                if sieve[d]:
                    for j in range(d*d,upper,d):sieve[j]=False
            return (p for p in range(7,upper) if sieve[p])
        for n in (128,257,509):
            genuine=m.state(n,angle)
            tested=0
            for p in primes_below(8*n-6):
                if p*p<=8*n:
                    continue
                ev=m.angular_last_p_event(p,n)
                if ev is None:continue
                observed=m._fmod(p*genuine,p)
                predicted=m.predicted_angular_p_residue(p,n)
                self.assertEqual(observed,predicted,(n,p))
                # These exact heldout horizons happen not to have losses
                # in this simple-pole range; theorem claims large-p asymptotic.
                self.assertNotEqual(observed,0,(n,p))
                tested+=1
            self.assertGreater(tested,100)

    def test_26_character_pulse_mutant_fails_original_primal(self):
        angle,_=m.angle_radial()
        bad=list(angle);bad[0]+=Q(1);bad=tuple(bad)
        self.assertNotEqual(m.shadow(5,bad),bad)
        for a in (3,5,7):
            self.assertNotEqual(m.shadow(a,bad),m.scaled(m.chi_minus4(a),bad))

    def test_21_reject_wrong_legendre_sign(self):
        # Incorrectly fixing chi2=+1 destroys p=3 or 5 class pulse law.
        w=m.P
        for a in (3,5):
            wrong=[]
            for ell in range(1,9):
                j=m.j_of(a,ell)
                wrong.append(Q(2)**((j-ell)//2)*w[j-1])
            self.assertNotEqual(tuple(wrong),m.shadow(a,w))


def sum_vec(rows):
    out=m.Z8
    for v in rows:
        out=m.add(out,v)
    return out


if __name__=='__main__':
    unittest.main()
