import cmath
import math
import unittest
from fractions import Fraction as F
from order_stat_bridge import (native_law, native_birth, beta_winner_law,
    winner_h, winner_acceptance, winner_birth, evolve, winner_observed,
    loss_observed, discrete_max_law, polya_history, info_bounds)


class OrderStatisticSUCC(unittest.TestCase):
    def test_uniform_native_m1(self):
        for j in range(25):
            self.assertEqual(beta_winner_law(1, j), native_law(j))
            self.assertEqual(evolve(native_law(j), j, native_birth), native_law(j+1))

    def test_winner_beta_binomial_exact(self):
        for m in range(1, 8):
            for j in range(30):
                law = beta_winner_law(m, j)
                self.assertEqual(sum(law), F(1))
                self.assertEqual(law, winner_observed(m, j)[0])
                self.assertEqual(winner_observed(m, j)[1], F(1, m))
                self.assertEqual(law, [winner_h(m,j,k)/F(j+1) for k in range(j+1)])

    def test_h_is_bounded_martingale_and_doob_transform(self):
        for m in range(1, 8):
            for j in range(20):
                for k in range(j+1):
                    h = winner_h(m,j,k)
                    self.assertTrue(0 < h <= m)
                    t = native_birth(j,k)
                    harmonic = (1-t)*winner_h(m,j+1,k) + t*winner_h(m,j+1,k+1)
                    self.assertEqual(h,harmonic)
                    conditioned = t*winner_h(m,j+1,k+1)/h
                    self.assertEqual(conditioned,winner_birth(m,j,k))

    def test_new_polya_birth_transports_selected_marginals(self):
        for m in range(1, 9):
            for j in range(30):
                self.assertEqual(evolve(beta_winner_law(m,j),j,
                    lambda jj,k:winner_birth(m,jj,k)), beta_winner_law(m,j+1))

    def test_fully_balanced_selected_and_rejected_m2(self):
        for j in range(60):
            plus,accept = winner_observed(2,j)
            minus,reject = loss_observed(2,j)
            self.assertEqual(accept, F(1,2))
            self.assertEqual(reject, F(1,2))
            self.assertEqual(sum(minus), F(1))
            self.assertEqual([accept*x+reject*y for x,y in zip(plus,minus)],native_law(j))
            self.assertEqual(minus,plus[::-1])

    def test_full_history_change_of_measure_without_singularity(self):
        for m in range(1,7):
            for j in range(7):
                original = polya_history(j,1)
                winner = polya_history(j,m)
                self.assertEqual(set(original),set(winner))
                self.assertEqual(sum(winner.values()), F(1))
                for w in original:
                    self.assertEqual(winner[w]/original[w],winner_h(m,j,sum(w)))

    def test_finite_kl_stays_bounded(self):
        for m in [2,3,4,7]:
            for j in [1,2,4,10,30,100,400]:
                fwd,reverse=info_bounds(m,j)
                self.assertLessEqual(fwd, math.log(m) + 1e-11)
                self.assertGreaterEqual(reverse, -1e-11)
            fwd,reverse=info_bounds(m,4000)
            self.assertAlmostEqual(fwd, math.log(m)-1+1/m, delta=.003)
            self.assertAlmostEqual(reverse, m-1-math.log(m), delta=.035)

    def test_discrete_max_noncommutes_with_latent_max(self):
        for m in range(2,7):
            for j in range(1,12):
                discrete=discrete_max_law(j,m)
                latent=beta_winner_law(m,j)
                self.assertEqual(sum(discrete),F(1))
                self.assertNotEqual(discrete,latent)
        self.assertEqual(discrete_max_law(1,2)[1], F(3,4))
        self.assertEqual(beta_winner_law(2,1)[1],F(2,3))

    def test_local_char_offaxis_while_info_bounded(self):
        # At j=1 selected (+) amplitudes: 1/3,2/3, zero at exp(2i z log p)=-1/2.
        for p in [2,3,11]:
            L=math.log(p)
            z=math.pi/(2*L)+1j*math.log(2)/(2*L)
            chi=F(1,3)*cmath.exp(-1j*z*L)+F(2,3)*cmath.exp(1j*z*L)
            self.assertLess(abs(chi),2e-12)
            self.assertTrue(z.imag>0)
            self.assertLess(info_bounds(2,1)[0],math.log(2))

    def test_full_source_character_recovered_from_signed_branch(self):
        for j in range(1,18):
            plus,pa=winner_observed(2,j)
            minus,pm=loss_observed(2,j)
            for z in [0.15,0.7,1.11]:
                native=sum(float(x)*cmath.exp(1j*(2*k-j)*z) for k,x in enumerate(native_law(j)))
                got=pa*sum(float(x)*cmath.exp(1j*(2*k-j)*z) for k,x in enumerate(plus))
                got+=pm*sum(float(x)*cmath.exp(1j*(2*k-j)*z) for k,x in enumerate(minus))
                self.assertAlmostEqual(abs(native-got),0,places=12)

    def test_source_relative_pure_amplitude_overlap_persists(self):
        # The coherent path vectors built with sqrt(q_j(k)) retain nonzero
        # source overlap as j -> infinity; contrast the geometric tilt.
        for m in [2,3,4,7]:
            j=1000
            q=beta_winner_law(m,j)
            source=native_law(j)
            affinity=sum(math.sqrt(float(x*y)) for x,y in zip(source,q))
            self.assertAlmostEqual(affinity**2, 4*m/(m+1)**2, delta=.002)

    def test_which_branch_dilation_is_isometry_but_discarding_tag_dephases(self):
        # Two-outcome ancilla W|k> = sqrt(w_k)|k,+> + sqrt(1-w_k)|k,->.
        # W*W=I, so full source is recoverable with the tag kept coherently.
        # On tracing the tag, distinct k coherences are suppressed.
        j=1
        w0=float(winner_acceptance(2,j,0))
        w1=float(winner_acceptance(2,j,1))
        self.assertAlmostEqual(w0,1/3)
        self.assertAlmostEqual(w1,2/3)
        overlap=math.sqrt(w0*w1)+math.sqrt((1-w0)*(1-w1))
        self.assertLess(overlap,1)
        self.assertAlmostEqual(overlap,2*math.sqrt(2)/3)

    def test_high_j_source_selection_not_singular_infinity(self):
        # Contrasts geometric a^k tilt of PR #355: finite limiting RN density m U^(m-1).
        for m in range(2,8):
            for j in [1,10,100,1000]:
                self.assertLessEqual(max(winner_h(m,j,k) for k in range(j+1)),m)
                self.assertEqual(winner_observed(m,j)[1],F(1,m))


if __name__=='__main__':
    unittest.main(verbosity=2)
