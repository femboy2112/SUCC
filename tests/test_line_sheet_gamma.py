"""Exact and exploratory regression for SUCC LS-01..LS-14.

Mathematical universal estimates are proved in PROOFS.md, not by finite tests.
"""
import cmath
import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'research'/'2026-11-02'/'line_sheet_gamma'/'line_sheet.py'
S=importlib.util.spec_from_file_location('succ_line_sheet_2026',P)
ls=importlib.util.module_from_spec(S);S.loader.exec_module(ls)


def unit(q):
    q%=1
    return cmath.exp(2j*math.pi*float(q))


class GammaLineSheetTests(unittest.TestCase):
    def test_four_source_poles_original(self):
        for n in range(1,101):
            self.assertEqual(ls.original_source(n), Fraction(120*n*n-89*n+16,
                (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
        self.assertEqual(ls.original_states(1)[0],0)

    def test_exact_kernel_factorization_rational(self):
        for d in range(2,40):
            for a in range(d+1):
                self.assertTrue(ls.kernel_polynomial_identity(Fraction(a,d)))

    def test_kernel_endpoints_exact_rational(self):
        q=ls.endpoint_rational_certificates()
        self.assertEqual(q['q_at_11_over_20'],Fraction(4950,326599))
        self.assertTrue(q['q_below_1_over_64'])
        self.assertEqual(q['L5'],Fraction(305,13824))
        self.assertTrue(q['L5_above_1_over_48'])
        self.assertEqual(q['L6'],Fraction(1,64))
        self.assertEqual(q['R_half'],Fraction(3,16))

    def test_sheet_boundary_expansion_exact(self):
        c=ls.exact_kernel_coefficients()
        for i in (0,1,2,3):
            self.assertEqual(c['gamma_sheet'][i]-c['source'][i],
                             c['sheet_minus_source'][i])
        self.assertEqual(2*c['sheet_minus_source'][2],c['laplace_cubic_gap'])
        self.assertEqual(c['laplace_cubic_gap'],Fraction(13,1536))

    def test_all_four_regions_float_calibration_only(self):
        for t in (.001,.01,.1,.5,1,2,3,3.9,4,4.25,4.5,4.9,5,
                  5.1,5.4,5.9,6,6.01,7,8,10,16,24,32,64,128):
            q=ls.bbp_sheet_source_kernel(t)
            g=ls.sheet_kernel_numeric(t,512)
            self.assertGreater(g,q)
            if t<=6:
                self.assertGreaterEqual(ls.small_sheet_lower(t)+1e-13,q)
            else:
                self.assertGreaterEqual(ls.long_sheet_lower(t)+1e-13,q)

    def test_strict_kernel_bounds_large_t_float(self):
        for t in (6,8,10,20,30,40,80):
            self.assertGreaterEqual(ls.long_sheet_lower(t),math.exp(-t/8)/30)

    def test_laplace_to_original_gamma_tail_finite(self):
        # Paper proof establishes the equality for every real s; finite
        # integer checks here use the original rational source series.
        for n in (1,2,4,8,16,32,128,256):
            T=sum((ls.original_source(n+j)/16**j for j in range(1,26)),Fraction())
            D=sum(1/j for j in range(1,n+1))-math.log(n)-0.5772156649015328606
            self.assertLess(float(T),D*D/16)
            self.assertGreater(float(T),0)


class SourceMultiprimeTests(unittest.TestCase):
    def test_multiple_original_births_cover_entire_epochs(self):
        for A in (16,32,64,128):
            ps=ls.epoch_prime_family(A)
            self.assertGreater(len(ps),0)
            for p in ps:
                k=(p-1)//8
                self.assertLessEqual(k+1,A)
                self.assertGreaterEqual(4*k,2*A-1)

    def test_exact_simultaneous_crt_source_chart(self):
        for A in (16,32,64):
            ps=ls.epoch_prime_family(A)
            U=ls.original_states(2*A-1)
            for n in range(A,2*A):
                factors,co=ls.simultaneous_prime_cofactor(n,ps,U[n])
                self.assertEqual(U[n],co+sum((Fraction(a,p) for p,a in factors),Fraction()))
                self.assertTrue(all(co.denominator%p for p in ps))
                for p,a in factors:
                    self.assertEqual(a,ls.prime_birth_residue(p,n))
                    pu=p*U[n]
                    self.assertNotEqual(pu.denominator%p,0)
                    self.assertEqual(pu.numerator*pow(pu.denominator,-1,p)%p,a)

    def test_exact_multi_galois_pair_character(self):
        ps=[17,41]
        self.assertEqual(ls.galois_pair_character(ps,0),1)
        self.assertEqual(ls.galois_pair_character(ps,1),Fraction(1,16*40))
        for d in range(1,20):
            q=ls.galois_pair_character(ps,d)
            # product is over exact Ramanujan sums: +/-1/(p-1) or 1.
            expected=Fraction(1)
            for p in ps:
                if (pow(16,d,p)-1)%p:
                    expected*=Fraction(-1,p-1)
            self.assertEqual(q,expected)

    def test_galois_joint_mean_vs_direct_automorphisms_float(self):
        # p=17 and 41 share a 3-time original source clean interval 6..8.
        ps=[17,41];ids=list(range(6,9));U=ls.original_states(8)
        terms=[]
        for n in ids:
            f,co=ls.simultaneous_prime_cofactor(n,ps,U[n])
            terms.append((f,co))
        predicted=0j
        for a,(pairs_a,co_a) in enumerate(terms):
            for b,(pairs_b,co_b) in enumerate(terms):
                predicted+=unit(co_a-co_b)*float(ls.galois_pair_character(ps,abs(ids[a]-ids[b])))
        observed=0.
        for u17 in range(1,17):
            for u41 in range(1,41):
                z=0j
                for pairs,co in terms:
                    z+=unit(co+Fraction(u17*pairs[0][1],17)+Fraction(u41*pairs[1][1],41))
                observed+=abs(z)**2
        self.assertAlmostEqual(predicted.real,observed/(16*40),places=9)
        self.assertAlmostEqual(predicted.imag,0,places=9)

    def test_product_short_lag_witness_and_prime_divisor_count(self):
        for A in (64,128,256):
            ps=ls.epoch_prime_family(A)
            for d in range(1,min(6,A)):
                k=ls.galois_pair_character(ps,d)
                nonalias=ls.short_lag_nonaliases(ps,d)
                self.assertEqual(abs(k), math.prod(Fraction(1,p-1)
                    for p in ps if pow(16,d,p)!=1))
                self.assertLessEqual(len(ps)-nonalias,
                                     d*math.log(16)/math.log(4*A)+1e-10)

    def test_fake_cofactor_trap_without_original_law(self):
        A=32;ps=ls.epoch_prime_family(A);Q=1+1000*math.prod(ps)
        for n in range(A,2*A):
            co,delta=ls.coherent_counterfeit(n,ps,Q)
            self.assertTrue(all(co.denominator%p for p in ps))
            self.assertLessEqual(abs(delta),Fraction(1,2*Q))
        # Even many exact prime clocks do not force selected real decorrelation.


class RelaxedCollisionTests(unittest.TestCase):
    def test_exact_original_self_scale_baseline(self):
        known={8:Fraction(7,4),16:Fraction(17,8),32:Fraction(13,8),
               64:Fraction(55,32),128:Fraction(55,32),256:Fraction(63,32)}
        for A,expected in known.items():
            counts,c=ls.source_selfscale_collision(A)
            self.assertEqual(c,expected)
            self.assertEqual(sum(counts),A)

    def test_source_counterseed_coherent_energy(self):
        for A in (8,32,128):
            # Completed real counterseed q=1/5 is fixed under 16 mod 5.
            counts=[0]*A;counts[A//5]=A
            self.assertEqual(Fraction(sum(x*x for x in counts),A),A)

    def test_quantitative_finite_minkowski_upper_bound(self):
        # Finite check of UNIVERSAL norm gluing, not proof of o(log A).
        for L in (8,16,32):
            N=L*L;M=L+1
            alpha=sum((ls.original_source(j)/16**j for j in range(1,N+1)), Fraction())
            counts=[0]*M
            a=alpha.numerator%alpha.denominator;d=alpha.denominator
            for _ in range(N):
                counts[(M*a)//d]+=1
                a=(a*16)%d
            B=Fraction(M*sum(c*c for c in counts),N*N)
            A0=1<<(M-1).bit_length()
            Cstar=max(ls.source_selfscale_collision(A)[1]
                for A in (1<<j for j in range(A0.bit_length()-1,N.bit_length())) if A<N)
            rhs=(2*M**1.5/N+6*math.sqrt(float(Cstar))
                 +(3*math.sqrt(2)/(1-2**-.5))*math.sqrt(M*float(Cstar)/N))
            self.assertLessEqual(math.sqrt(float(B)),rhs+1e-9)


if __name__=='__main__':unittest.main()
