"""RH-facing hostile controls: local signs and analytic finite reports are insufficient."""
import unittest
from fractions import Fraction as F
from observational_succ.field_analytic_shadow_countermodel import symmetric_jet_with_forced_offline_zero

class MoonshotFirewallTests(unittest.TestCase):
    def test_pointwise_nonnegative_kernel_does_not_imply_psd(self):
        xs=(F(0),F(1))
        K=tuple(tuple((x+y)**2 for y in xs) for x in xs)
        self.assertTrue(all(a>=0 for row in K for a in row))
        self.assertEqual(K,((F(0),F(1)),(F(1),F(4))))
        self.assertEqual(K[0][0]*K[1][1]-K[0][1]*K[1][0],-1)
        v=(F(3),F(-1))
        energy=sum(v[i]*K[i][j]*v[j] for i in range(2) for j in range(2))
        self.assertEqual(energy,-2)

    def test_finite_reflection_symmetric_analytic_shadow_misses_real_zeros(self):
        r=symmetric_jet_with_forced_offline_zero(8)
        self.assertEqual(len(r['coefficients'])>9,True)
        self.assertFalse(r['actual_Riemann_xi_used_or_modified'])
        self.assertEqual(r['zero_real'],F(1,4))

    def test_analytic_countermodel_not_entitled_to_fake_euler_source_label(self):
        r=symmetric_jet_with_forced_offline_zero(2)
        self.assertNotIn('Euler product',r)
        self.assertNotIn('Weil sign',r)

if __name__=='__main__':unittest.main()
