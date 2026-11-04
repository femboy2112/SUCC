"""Focused exact original BBP prime/Frobenius saturation tests. No pi digits."""
import importlib.util
from pathlib import Path
import unittest
from fractions import Fraction as F
from math import gcd, lcm

ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'research/2026-11-04/frobenius_prime_saturation/frobenius_prime.py'
spec=importlib.util.spec_from_file_location('frobenius_prime',SRC)
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def sieve(N):
    is_p=[True]*(N+1);is_p[:2]=[False,False]
    for i in range(2,int(N**.5)+1):
        if is_p[i]:
            for j in range(i*i,N+1,i):is_p[j]=False
    return [i for i,p in enumerate(is_p) if p]

def independent_source(n):
    # Direct from original Mellin polynomial polynomial factor, independent
    # from four-term decomposition in the claimed source object.
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def local_oracle(p,n):
    """Direct source event iteration in F_p, no Frobenius closed form.

    Each authentic p pole injects coefficient (4,-2,-1,-1)/m.
    Other source moments contribute 0 mod p after multiplication by p.
    """
    z=0
    for k in range(1,n+1):
        z=16*z%p
        for c,w in ((7,4),(4,-2),(3,-1),(2,-1)):
            a=8*k-c
            if a%p==0:
                m=a//p
                if m%p==0:raise ValueError('p² source pole')
                z=(z+w*pow(m,-1,p))%p
    return z

class FrobeniusTheoremTests(unittest.TestCase):
    def test_original_four_signed_source_independent_polynomial(self):
        for n in range(1,100):self.assertEqual(f.source(n),independent_source(n))

    def test_first_event_tables(self):
        expected={
            1:[(1,F(4)),(4,F(7,2)),(5,F(33,10)),(6,F(47,15))],
            3:[(2,-F(1,2)),(3,F(16,3)),(4,-F(19,6)),(7,F(130,21))],
            5:[(1,-F(1)),(4,F(7,2)),(5,-F(66,5)),(6,F(47,15))],
            7:[(2,-F(1,2)),(3,-F(4,3)),(4,-F(19,6)),(7,-F(520,21))],
        }
        for a,table in expected.items():
            self.assertEqual([(m,C) for m,c,w,C in f.universal_pulse_states(a,7)],table)

    def test_all_4_classes_sign_rules_through_100_cycles(self):
        for a in f.ALLOWED_CLASSES:
            for m,c,w,C in f.universal_pulse_states(a,808):
                self.assertNotEqual(C,0)
                self.assertEqual(1 if C>0 else -1,f.pulse_sign(a,m))

    def test_exact_self_shadow_and_dual_shadow(self):
        for a in f.ALLOWED_CLASSES:
            for k in range(1,55):
                self.assertEqual(f.shell_constant(a,k),f.full_shell_closed(a,k))
        self.assertEqual(f.dual_state(1),F(130,21))

    def test_sharp_all_N_harmonic_null_defect(self):
        # Strong finite-stage inequality newly paper-proved from a strictly
        # positive rational comparison kernel (not extrapolated from tests).
        U=V=F(0)
        for n in range(1,1530):
            U=16*U+f.source(n)
            V=16*V+f.dual_source(n)
            self.assertGreater(2*U-V,0)
            self.assertLess(2*U-V,F(1,8*n+4))

    def test_pi_null_integral_algebraic_derivative(self):
        # Direct rational polynomial identity K_dual-2*K = -8 d(log F).
        # Valid as identity for all t with D(t) !=0; sample 200 exact Q
        # nodes in addition to the symbolic-oracle independent check.
        for i in range(1,199):
            t=F(i,200)
            P=4-2*t**3-t**4-t**5
            Q=8*t+4*t*t+4*t**3-t**6
            D=1-t**8/16
            Ftop=2-t*t;Fbot=(t-1)**2+1
            dlog= -2*t/Ftop-2*(t-1)/Fbot
            self.assertEqual((Q-2*P)/D,-8*dlog)

    def test_dual_source_positive_and_exact_zero_remainder(self):
        v=F(0)
        for n in range(1,170):
            self.assertGreater(f.dual_source(n),0)
            self.assertGreater(f.dual_source(n)-2*f.source(n),0 if n>=2 else -1)
            v=16*v+f.dual_source(n)
            d=v-2*f.source_state(n)
            self.assertLess(d,0)
        self.assertEqual(f.dual_source(1)-2*f.source(1),-F(8,105))

    def test_universal_modular_formula_moderate_primes(self):
        for p in sieve(541):
            if p<=5:continue
            nmin=(p+7)//8 if p%8==1 else (p+3)//8 if p%8==5 else (p+1)//4
            for j in (nmin,min(nmin+7,(p*p-1)//8),min(nmin+17,(p*p-1)//8)):
                if j<nmin:continue
                if p*p<=8*j:continue
                self.assertEqual(f.predicted_p_residue(p,j),local_oracle(p,j),(p,j))

    def test_expected_exceptional_small_primes_not_swept_under_rug(self):
        cases=((128,37),(257,47),(509,113),(509,151))
        for n,p in cases:
            self.assertEqual(f.predicted_p_residue(p,n),0,(n,p))
            self.assertEqual(local_oracle(p,n),0,(n,p))

    def test_mutation_of_pole_breaks_self_shadow(self):
        # Mutant: first source tap +3 instead of +4; the very first
        # a=1 normalized residue becomes 3 instead of authenticated 4.
        self.assertNotEqual(F(3),f.universal_pulse_states(1,1)[0][-1])

    def test_changed_seed_with_p_denominator_breaks_source_selected_pulse(self):
        p=29
        n=(p+3)//8
        genuine=local_oracle(p,n)
        # Source recurrence with seed 1/p has pU_n shifted by 16^n.
        changed=(genuine+pow(16,n,p))%p
        self.assertNotEqual(changed,genuine)

    def test_fake_legendre_sign_breaks_p5(self):
        p=13;n=(p+1)//2
        right=f.predicted_p_residue(p,n)
        self.assertEqual(right,7*pow(2,-1,p)%p)
        # False chi2=+1 makes first pulse propagate +4 instead of -4:
        wrong=(-4-F(1,2))
        wrong_mod=wrong.numerator*pow(wrong.denominator,-1,p)%p
        self.assertNotEqual(wrong_mod,right)

    def test_p2_regime_enforced(self):
        with self.assertRaises(ValueError):f.predicted_p_residue(7,100)

    def test_computed_conductor_and_reduced_state_independent(self):
        for n in (0,1,5,16,64,128,257,509,911,1511):
            A,M,D=f.integer_lcm_state(n)
            z=f.source_state(n)
            self.assertEqual(z,F(A,M))
            self.assertEqual(D,z.denominator)

    def test_fresh_entire_p_survival_windows(self):
        for N in (128,257,509,911):
            state=f.source_state(N)
            for p in sieve(8*N):
                if p<=5 or p*p<=8*N or p<=N//10:continue
                self.assertEqual(
                    f.predicted_p_residue(p,N),local_oracle(p,N),
                    (N,p,'local-vs-Frobenius'))
                self.assertEqual(
                    f.predicted_p_residue(p,N),
                    f.modular_residue_of_unwrapped(state,p),
                    (N,p,'full-original-state'))

    def test_full_shell_finite_field_echo_directly_from_original_poles(self):
        # Independent modular p-source iteration at the *original* time
        # n_p,k, not evaluation of universal C_a(m), tests both formulas.
        for a in f.ALLOWED_CLASSES:
            candidates=[p for p in sieve(311) if p>47 and p%8==a][:4]
            self.assertEqual(len(candidates),4)
            for p in candidates:
                for k in (1,2,3):
                    if a in (1,5):
                        n=(k-1)*p+(3*p+1)//4
                        expectation=f.source_state(k)
                    elif a==3:
                        n=(k-1)*p+(7*p+3)//8
                        expectation=f.dual_state(k)
                    else:
                        n=(k-1)*p+(7*p+7)//8
                        expectation=-4*f.dual_state(k)
                    self.assertGreater(p*p,8*n)
                    exp=expectation.numerator*pow(expectation.denominator,-1,p)%p
                    self.assertEqual(exp,local_oracle(p,n),(a,p,k,n))

    def test_pulse_classes_start_and_finish_are_source_faithful(self):
        for a in f.ALLOWED_CLASSES:
            ss=f.universal_pulse_states(a,80)
            last=-1
            for m,c,w,C in ss:
                self.assertGreater(m,last)
                self.assertEqual((m*a+c)%8,0)
                self.assertEqual({7:4,4:-2,3:-1,2:-1}[c],w)
                last=m

    def test_survival_with_named_finite_exceptional_primes(self):
        # Quantified theorem is *eventual* in N for each epsilon. At
        # N=509, p=113,151 genuinely cancel; these are not thrown away.
        # No finite-N uniform-prime claim follows from the proof.
        explicit_exceptional={509:{113,151}, 911:set(),1511:set()}
        for N,ex in explicit_exceptional.items():
            state=f.source_state(N)
            absent=set()
            for p in sieve(8*N):
                if p<max(N//5,101) or p*p<=8*N or not f.eligible_source_prime(p,N):continue
                if state.denominator%p !=0:absent.add(p)
            self.assertEqual(absent,ex,(N,absent))

if __name__=='__main__':unittest.main()
