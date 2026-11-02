"""Focused exact research regressions (not a pi-normality proof)."""
import importlib.util
import math
import unittest
from fractions import Fraction
from pathlib import Path

_PATH=(Path(__file__).resolve().parents[1] / 'research' / '2026-11-02'
       / 'prime_cofactor_gamma_golden' / 'prime_cofactor_gamma.py')
_SPEC=importlib.util.spec_from_file_location('prime_cofactor_gamma',_PATH)
f=importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(f)


class OriginalPrimeSourceTests(unittest.TestCase):
    def test_original_four_pole_numerator(self):
        for n in range(1,201):
            self.assertEqual(f.bbp_r(n),
                Fraction(120*n*n-89*n+16,
                         (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
            self.assertGreater(f.bbp_r(n),0)

    def test_source_selected_U0_and_recurrence(self):
        v=f.original_states(200)
        self.assertEqual(v[0],0)
        for n in range(1,len(v)):
            self.assertEqual(v[n],16*v[n-1]+f.bbp_r(n))
            if n<=20:
                self.assertEqual(v[n],16**n*f.alpha_cutoff(n))

    def test_birth_clean_window_and_pintegral_cofactor(self):
        for p in (17,41,73,89,97,113,137,193,233,241,257):
            k=(p-1)//8
            b,last,reset=f.birth_window(p)
            self.assertEqual((b,last,reset),(k+1,4*k,4*k+1))
            u=f.original_states(reset)
            for t in range(3*k):
                a,co=f.cofactor_decomposition(p,t,u)
                self.assertEqual(a+co,u[b+t])
                self.assertNotEqual(co.denominator%p,0)
                self.assertEqual(f.p_residue(p*u[b+t],p),4*pow(16,t,p)%p)

    def test_exact_first_secondary_pole_impulse(self):
        for p in (17,41,73,97,113,137,193,233,241,257):
            k=(p-1)//8
            b,last,reset=f.birth_window(p)
            u=f.original_states(reset)
            # at n=4k+1: term -2/(4p) contributes -1/2 to pU modulo p
            res=f.p_residue(p*u[reset],p)
            expected=(4*pow(16,3*k,p)-pow(2,-1,p))%p
            self.assertEqual(res,expected)

    def test_prime_cofactor_integer_carry_is_exact(self):
        for p in (17,41,73,89,97,113):
            b,last,_=f.birth_window(p)
            u=f.original_states(last)
            for s,t in ((0,1),(1,3),(0,min(3*(p-1)//8-1,7))):
                a=f.prime_cofactor_pair_certificate(p,s,t,u)
                self.assertNotEqual(a['q']%p,0)
                self.assertEqual(a['distance'], f.exact_phase_distance(u[b+t]-u[b+s]))
                self.assertEqual(a['joint_numer']%p,
                        a['prime_numer']*a['q']%p)

    def test_nonalias_prime_birth_is_not_real_separation(self):
        p=73
        u=f.original_states(22)
        a=f.prime_cofactor_pair_certificate(p,0,4,u)
        self.assertNotEqual(a['prime_numer']%p,0)
        self.assertGreater(a['distance'],0)
        self.assertLess(a['distance'],Fraction(1,2))

    def test_cyclotomic_galois_orthogonality_two_methods(self):
        for p,t,h in ((17,6,1),(41,8,2),(73,9,3),(113,11,1)):
            u=f.original_states((p-1)//8+t)
            selected,mean=f.galois_energy_pair(p,t,h,u)
            direct=f.galois_direct_mean(p,t,h,u)
            self.assertAlmostEqual(mean,direct,places=8)
            self.assertGreaterEqual(selected,0)
            self.assertGreaterEqual(mean,0)

    def test_order_alias_examples_and_subgroup(self):
        for p in (17,41,73,89,97,113,137,193,233,241,257):
            d=f.order_of_16(p)
            self.assertEqual(pow(16,d,p),1)
            self.assertEqual((p-1)%d,0)
        self.assertEqual(f.order_of_16(257),4)

    def test_counterfeit_pfree_real_embedding_is_coherent(self):
        for p,T,H,Q in ((17,6,3,1001),(41,9,5,4101),(73,11,6,7301)):
            if Q%p==0:Q+=1
            fake=f.fake_cofactor(p,T,H,Q)
            self.assertTrue(all(v.denominator%p for v in fake))
            self.assertTrue(all(f.exact_phase_distance(Fraction(4*16**t,p)+fake[t])
                                <=Fraction(1,2*Q) for t in range(T)))
            q=float(Q)
            self.assertGreater(1+H*(1-math.pi*H/q)**2, 1+H/2)


class ExactSingleMeshTests(unittest.TestCase):
    def test_integer_modular_orbit(self):
        q=Fraction(1,7)
        self.assertEqual([a for a,_ in f.modular_orbit(q,9)],
                         [1,2,4,1,2,4,1,2,4])

    def test_rational_mesh_counts_and_near_pair_relation(self):
        for L in (3,4,8,16):
            N=L*L;M=L+1
            q=f.alpha_cutoff(N)
            counts=f.exact_mesh_occupancy(q,N,M)
            self.assertEqual(sum(counts),N)
            self.assertLessEqual(sum(x*x for x in counts),
                                 f.exact_near_pair_count(q,N,M))
            C=f.mesh_collision_energy(counts)
            self.assertGreaterEqual(C,1)

    def test_fejer_vs_mesh_inequality_numerical(self):
        C=f.fejer_mesh_majorant_constant()
        self.assertGreater(C,3.8)
        for q,N,M in [(Fraction(1,5),20,6),
                      (Fraction(1,7),21,8),
                      (f.alpha_cutoff(16),16,5),
                      (f.alpha_cutoff(64),64,9),
                      (f.alpha_cutoff(256),256,17)]:
            lhs=f.fejer_energy_numeric(q,N,M-1)
            rhs=C*float(f.mesh_collision_energy(f.exact_mesh_occupancy(q,N,M)))
            self.assertLess(lhs,rhs+1e-10)

    def test_coherent_seed_fails_mesh_cap(self):
        for L in (4,8,16):
            q=Fraction(1,5)
            N=L*L;M=L+1
            C=f.mesh_collision_energy(f.exact_mesh_occupancy(q,N,M))
            self.assertEqual(C,M)

    def test_exact_checkpoint_histogram_small(self):
        reported={4:Fraction(145,128),8:Fraction(2682,2048),
                  16:Fraction(68408,65536)}
        for L,approx in reported.items():
            N=L*L;M=L+1
            obs=f.mesh_collision_energy(f.exact_mesh_occupancy(f.alpha_cutoff(N),N,M))
            self.assertEqual(obs,approx)


class GoldenGammaDefectTests(unittest.TestCase):
    def test_euler_em_bound_implies_global_BBP_square_domination(self):
        for n in list(range(2,400))+[500,1000,4096,32768]:
            self.assertGreater(f.exact_gamma_square_gap(n),0)
            self.assertEqual(f.exact_gamma_square_gap(n)>0,
                             96*n**3-152*n**2+2>0)

    def test_golden_exact_circle_return(self):
        for k in range(1,91):
            self.assertTrue(f.exact_golden_circle_return(k))
        self.assertEqual(f.fib(10),55)

    def test_gamma_shell_negative_with_inverse_golden_ratio(self):
        # This numerical test checks a finite classical limit, not a new bound.
        eta=(math.sqrt(5)-1)/2
        shells=[f.finite_harmonic_shell(k) for k in range(7,16)]
        self.assertTrue(all(x<0 for x in shells))
        self.assertLess(abs(shells[-1]/shells[-2]-eta),0.005)

    def test_original_BBP_tail_leading_coefficient_finite_oracle(self):
        for n in (128,256,512,1024):
            partial=sum((f.bbp_r(n+j)/16**j for j in range(1,21)),Fraction(0))
            limit=float(partial)*n*n
            self.assertLess(abs(limit-1/64),0.002)
            tail_bound=f.gamma_tail_upper(n+20)/16**20
            self.assertLess(float(tail_bound),1e-22)


if __name__=='__main__':
    unittest.main()
