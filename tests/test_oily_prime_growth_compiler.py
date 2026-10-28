import unittest
from fractions import Fraction as F
from observational_succ import oily_prime_growth_compiler as m

class ExactOilyCausalCompiler(unittest.TestCase):
    def test_endpoint_packets(self):
        for j in range(0,35):
            self.assertEqual(m.oily_grade(1,j),F(j+1,2**(j+2)))
            for k in range(j+1):
                self.assertEqual(m.oily_joint(1,j,k),F(1,2**(j+2)))

    def test_source_parameters(self):
        for x in [F(0),F(1,13),F(1,4),F(1,2),F(3,4),F(1)]:
            u,v=m.rates(x)
            self.assertEqual(u+v,x)
            self.assertEqual(u-v,x*(1-x))
            self.assertGreaterEqual(u,v)
            self.assertLessEqual(u,F(1,2))

    def test_survival_exact(self):
        for x in [F(0),F(1,10),F(1,3),F(1,2),F(5,6),F(1)]:
            for j in range(0,15):
                s=m.grade_survival(x,j)
                self.assertGreaterEqual(s,0)
                self.assertEqual(s-m.oily_grade(x,j),m.grade_survival(x,j+1))
                if s: self.assertTrue(0<=m.stop_probability(x,j)<=1)

    def test_birth_cdf_unique_all_x(self):
        for x in [F(1,20),F(1,5),F(1,2),F(9,10),F(1)]:
            for j in range(0,16):
                for k in range(j+1):
                    a=m.unique_local_birth_probability(x,j,k)
                    self.assertEqual(a,m.unique_birth_cdf(x,j,k))
                    self.assertTrue(0<=a<=1)

    def test_sequential_full_packet(self):
        for x in [F(0),F(1,16),F(1,2),F(5,7),F(1)]:
            out=m.sequential_joint_oily(x,12)
            for j in range(13):
                for k in range(j+1):
                    self.assertEqual(out[j,k],m.oily_joint(x,j,k))
            self.assertEqual(sum(out.values(),F(0)),1-m.grade_survival(x,13))

    def test_polya_critical(self):
        for j in range(0,22):
            self.assertEqual(m.stop_probability(1,j),m.critical_oily_stop(j))
            for k in range(j+1):
                self.assertEqual(m.unique_local_birth_probability(1,j,k),m.polya_birth(j,k))

    def test_zeta_polya_joint(self):
        for q in [F(1,2),F(1,3),F(2,5),F(1,7)]:
            joint=m.sequential_joint_zeta(q,14)
            for (j,k),v in joint.items():
                self.assertEqual(v,m.zeta_prime_joint(q,j,k))
            self.assertEqual(sum(joint.values(),F(0)),1-q**15)

    def test_oily_vs_single_zeta_local_size_bias(self):
        for q in [F(1,2),F(1,3),F(3,4)]:
            for j in range(20):
                for k in range(j+1):
                    self.assertEqual(m.oily_balanced_joint(q,j,k),
                                     m.zeta_prime_joint(q,j,k)*m.grade_sizebias_ratio(q,j))

    def test_stop_hazard_comparison(self):
        for q in [F(1,2),F(1,3),F(3,4)]:
            for j in range(16):
                self.assertLess(m.balanced_stop(q,j),1-q)
                if q==F(1,2):
                    self.assertEqual(m.balanced_stop(q,j),m.critical_oily_stop(j))

    def test_alternate_latent_history_same_terminal_packet(self):
        # Construct a DIFFERENT history: sample terminal J=2 and K uniform
        # on {0,1,2} at the source; perform a first-channel birth first iff
        # the already-sampled K is >=1. This reaches each K exactly, but the
        # intermediate first-step law is 2/3, whereas the online source-local
        # Pólya transition has 1/2. Identical terminal packet law does not
        # uniquely determine private ordered histories without the stated
        # source-local conditions.
        self.assertEqual(sum((m.critical_joint(2,k) for k in range(3)),F(0)),F(3,16))
        self.assertEqual(F(2,3),sum((F(1,3) for k in (1,2)),F(0)))
        self.assertNotEqual(F(2,3),m.polya_birth(0,0))

    def test_wrong_constant_stop_changes_oily_source(self):
        self.assertEqual(m.critical_joint(0,0),F(1,4))
        self.assertNotEqual(m.critical_joint(0,0),F(1,2)) # geometric stop

    def test_naive_amplitude_loss_and_exact_gamma_telescoping(self):
        for j in range(0,35):
            self.assertEqual(set(m.amplitude_row_sums(j)),{F(j+1,j+2)})
            self.assertEqual(m.naive_polya_amplitude_compression_squared(j),F(j+1,j+2))
            self.assertEqual(m.terminal_coherence_product(j),F(1,j+1))

    def test_all_prime_prior_finite_cutoff(self):
        for beta in range(2,7):
            for cutoff in [2,3,7,31,127]:
                self.assertEqual(m.zeta_prime_tail_coupling_bound(beta,cutoff),F(1,(beta-1)*cutoff**(beta-1)))
                self.assertTrue(0<m.zeta_prime_tail_coupling_bound(beta,cutoff)<1)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):m.rates(F(2))
        with self.assertRaises(ValueError):m.unique_local_birth_probability(0,0,0)
        with self.assertRaises(ValueError):m.stop_probability(-1,0)
        with self.assertRaises(ValueError):m.sequential_joint_zeta(1,4)
        with self.assertRaises(TypeError):m.rates(0.5)

if __name__=='__main__': unittest.main()
