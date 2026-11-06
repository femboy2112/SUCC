"""Scoped exact controls. Signed complex cycle measurements are diagnostics only."""
import math
import unittest
from fractions import Fraction
import adelic_triangle as a

class AdelicSourceTests(unittest.TestCase):
    def test_source_numerator_denominator(self):
        for n in range(1,120):
            self.assertEqual(a.source(n),Fraction(a.numerator(n),a.denominator(n)))
            self.assertEqual(a.denominator(n)%2,1)

    def test_original_zero_seed(self):
        self.assertEqual(a.state(0),0)
        for n in range(1,60):
            self.assertEqual(a.state(n),16*a.state(n-1)+a.source(n))

    def test_odd_denominator_provenance(self):
        for n in range(1,42):
            state=a.state(n)
            self.assertEqual(state.denominator%2,1)
            self.assertTrue(set(a.factorization(state.denominator))<=a.source_prime_support(n))
            self.assertTrue(all(p<=8*n-3 for p in a.factorization(state.denominator)))

    def test_adeles_exact(self):
        for n in range(1,41):
            for h in (-3,1,2):
                x=h*a.state(n)
                self.assertEqual(a.global_odd_fraction(x),x%1)
                self.assertEqual(a.principal_part(x,2),0)

    def test_local_principal_integer_carry_invariance(self):
        for n in (1,2,5,13,29):
            x=a.state(n)
            for p in a.factorization(x.denominator):
                self.assertEqual(a.principal_part(x,p),a.principal_part(x%1,p))

    def test_canonical_minimal_p_examples(self):
        x=Fraction(1,15)
        self.assertEqual(a.principal_part(x,3),Fraction(2,3))
        self.assertEqual(a.principal_part(x,5),Fraction(2,5))
        self.assertEqual((a.principal_part(x,3)+a.principal_part(x,5))%1,x)

    def test_birth_formula_all_p_less_300(self):
        for p in range(7,300):
            if a.is_prime(p):
                n0,n1,c=a.prime_birth(p)
                self.assertEqual((n0,c),a.predicted_prime_birth(p))
                self.assertLess(n0,n1)

    def test_first_pole_val_exact(self):
        for p in range(7,180):
            if a.is_prime(p):
                n0,n1,c=a.prime_birth(p)
                self.assertEqual(a.principal_part(a.state(n0),p),Fraction(c,p))
                if n0>0:self.assertEqual(a.principal_part(a.state(n0-1),p),0)

    def test_plateau_all_p_less_200(self):
        for p in range(7,200):
            if a.is_prime(p):
                n0,n1,c,m,phase=a.birth_plateau(p)
                self.assertEqual(len(phase),n1-n0)
                self.assertEqual(phase[0],c)
                self.assertEqual(phase,[(c*pow(16,t,p))%p for t in range(n1-n0)])

    def test_local_gauss_classical_bound(self):
        for p in (29,37,53,61,101,149,181,197,269,293):
            r=a.local_cycle_probe(p)
            self.assertLess(r['local_abs'],r['gauss_bound']+1e-12)
            self.assertLessEqual(r['order'],r['clean_length'])

    def test_measured_p149_calibration(self):
        r=a.local_cycle_probe(149)
        self.assertAlmostEqual(r['local_abs'],0.10740801825011284,places=10)
        self.assertAlmostEqual(r['real_abs'],0.17040835226954132,places=10)

    def test_fresh_untuned_cycles(self):
        for p in (181,197,269,293):
            r=a.local_cycle_probe(p)
            self.assertTrue(0<=r['local_abs']<=1)
            self.assertTrue(0<=r['real_abs']<=1)

    def test_other_prime_spoofing(self):
        r=a.hostile_compensation(149,1009)
        self.assertLess(r['local_abs'],0.11)
        self.assertGreater(r['adversarial_real_abs'],r['proved_real_lower'])
        self.assertGreater(r['adversarial_real_abs'],0.99)

    def test_other_prime_covariance(self):
        for p in (149,181,197,269,293):
            r=a.prime_phase_covariance(p)
            self.assertLessEqual(r['global_mean_abs'],r['certifiable_bound']+1e-12)
            self.assertLessEqual(r['global_mean_abs'],1+1e-12)

    def test_first_pole_weight_mutation_and_harmonic_mass(self):
        # Controlled mutant 4->5 breaks the sum(weights)==0 source balance.
        def mutated(n):return a.source(n)+Fraction(1,8*n-7)
        self.assertEqual(sum(a.WEIGHTS),0)
        self.assertEqual(sum((5,-2,-1,-1)),1)
        for p in (17,41,73,97):
            n0,n1,c=a.prime_birth(p)
            self.assertEqual(c,4%p)
            v=p*mutated(n0)
            self.assertEqual((v.numerator*pow(v.denominator,-1,p))%p,5%p)
        for n in (1,2,17,200):
            self.assertEqual(mutated(n)-a.source(n),Fraction(1,8*n-7))

    def test_harmonic_mutant_has_logarithmic_growth(self):
        import mpmath as m
        with m.workdps(50):
            # Classical digamma identity, numeric check on non-fit N values.
            for N in (37,1001):
                exact=sum(Fraction(1,8*n-7) for n in range(1,N+1))
                value=m.mpf(exact.numerator)/exact.denominator
                formula=(m.digamma(N+m.mpf(1)/8)-m.digamma(m.mpf(1)/8))/8
                self.assertLess(abs(value-formula),m.mpf('1e-45'))
                # Limiting finite-part constant is -psi(1/8)/8,
                # whose rational digamma includes +gamma/8.
            self.assertLess(abs((m.digamma(100000+m.mpf(1)/8)-m.log(100000))),m.mpf('1e-4'))

    def test_codual_triangle_inversion(self):
        for xyz in [(-7,0,9),(0,0,0),(1,1,1),(11,-13,7)]:
            self.assertEqual(a.edge_inverse(*a.edge_pair_map(*xyz)),xyz)

    def test_parity_defect_exact(self):
        # On F2, edge map has a one-dimensional kernel span(1,1,1).
        mod_classes={}
        for h in (0,1):
            for g in (0,1):
                for p in (0,1):
                    image=tuple(z%2 for z in a.edge_pair_map(h,g,p))
                    mod_classes.setdefault(image,[]).append((h,g,p))
        self.assertEqual(len(mod_classes),4)
        self.assertTrue(all(len(pre)==2 for pre in mod_classes.values()))
        self.assertEqual(mod_classes[(0,0,0)],[(0,0,0),(1,1,1)])
        # det of [[1,1,0],[1,0,1],[0,1,1]] = -2.
        self.assertEqual(1*(0*1-1*1)-1*(1*1-1*0),-2)

    def test_unweighted_harmonic_sum_silver(self):
        import mpmath as m
        with m.workdps(70):
            w=(4,-2,-1,-1);a0=(7,4,3,2)
            dig=-sum(m.mpf(z)/8*m.digamma(1-m.mpf(y)/8) for z,y in zip(w,a0))
            silver=m.pi*(4+5*m.sqrt(2))/16+m.mpf(5)/8*m.log(2)+5*m.sqrt(2)/8*m.log(1+m.sqrt(2))
            self.assertLess(abs(dig-silver),m.mpf('1e-65'))
            N=1000
            partial=sum(m.mpf(a.source(n).numerator)/a.source(n).denominator for n in range(1,N+1))
            # Parent bound r(n)<n^-2 for n>=2, so tail <1/N.
            self.assertTrue(partial<silver<partial+1/m.mpf(N))

if __name__=='__main__':unittest.main()
