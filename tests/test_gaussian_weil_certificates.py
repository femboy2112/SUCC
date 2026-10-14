"""Independent rational, negative-model and signed-source Gaussian Weil probes."""
import unittest
from fractions import Fraction as F
from observational_succ import gaussian_weil_certificates as g


class ExactSphere(unittest.TestCase):
    def test_distances_and_order(self):
        self.assertEqual(g.ORDER,("N","S","E0","E1","E2","E3"))
        self.assertEqual(g.covariance("N","S"),F(1,4))
        self.assertEqual(g.covariance("N","E0"),F(1,2))
        self.assertEqual(g.covariance("E0","E2"),F(1,4))
        self.assertEqual(g.covariance("E0","E1"),F(1,2))

    def test_ldl_exact(self):
        self.assertEqual(g.ldl_pivots(g.gram()),
                         (F(1),F(15,16),F(3,5),F(7,12),F(15,28),F(39,80)))
        for subset in (("N","S"),("E0","E1"),("E0","E1","E2")):
            self.assertTrue(all(d>0 for d in g.ldl_pivots(g.gram(subset))))

    def test_full_eigenbasis(self):
        K=g.gram()
        pairs=[
            (F(13,4),(1,1,1,1,1,1)),
            (F(3,4),(1,-1,0,0,0,0)),
            (F(3,4),(0,0,1,0,-1,0)),
            (F(3,4),(0,0,0,1,0,-1)),
            (F(1,4),(0,0,1,-1,1,-1)),
            (F(1,4),(-2,-2,1,1,1,1))]
        for eigenvalue,v in pairs:
            self.assertEqual(tuple(sum(K[i][j]*v[j] for j in range(6))
                                   for i in range(6)),
                             tuple(eigenvalue*x for x in v))
        self.assertEqual(F(13,4)*F(3,4)**3*F(1,4)**2,F(351,4096))

    def test_posterior_variances(self):
        values=[g.posterior(("E0","E1","E2","E3")[:j],[0]*j,"N")[1]
                for j in range(1,5)]
        self.assertEqual(values,[F(3,4),F(2,3),F(7,12),F(5,9)])
        self.assertTrue(all(a>b>0 for a,b in zip(values,values[1:])))

    def test_posterior_noise_and_boundary(self):
        self.assertEqual(g.posterior(["N"],[F(7,3)],"N"),(F(7,3),F(0)))
        self.assertEqual(g.posterior(["N"],[F(7,3)],"N",F(1)),(F(7,6),F(1,2)))
        self.assertEqual(g.posterior([],[],"N"),(F(0),F(1)))

    def test_prime_chart_orientation_not_radii(self):
        for p in (3,5,7,11,13,17,19):
            action=g.prime_chart_action(p)
            self.assertEqual(len(set(action.values())),6)
            for u in g.ORDER:
                for v in g.ORDER:
                    self.assertEqual(g.covariance(action[u],action[v]),g.covariance(u,v))
            self.assertEqual(g.oriented_area(action),1 if p%4==1 else -1)

    def test_composite_and_dyadic_mutants(self):
        for p in (2,4,6,9,15,1,0,-3):
            with self.assertRaises(g.GaussianSourceError):g.prime_chart_action(p)
        self.assertEqual(g.oriented_area(g.equator_action(9)),1)
        self.assertLess(len(set(g.equator_action(6).values())),6)

    def test_malformed_or_negative_noise(self):
        cases=[
            lambda:g.covariance("ghost","N"),
            lambda:g.gram(["N","N"]),
            lambda:g.posterior(["N","N"],[1,2],"S"),
            lambda:g.posterior(["N"],[],"S"),
            lambda:g.posterior(["N"],[1],"S",F(-1)),
        ]
        for f in cases:
            with self.assertRaises(g.GaussianSourceError):f()


class SignedWeilBridge(unittest.TestCase):
    def test_hidden_negative_rank_one(self):
        for n in range(2,8):
            for observed in range(1,n):
                A=g.rank_one_hidden_sign(n,observed)
                self.assertEqual(A[observed][observed],-1)
                for i in range(observed):
                    for j in range(observed):
                        self.assertEqual(A[i][j],int(i==j))

    def test_gamma_rational_tail(self):
        self.assertEqual(g.gamma_tail(1),F(9,25))
        self.assertEqual(g.gamma_tail(2),F(13,81))
        for J in range(2,45):
            self.assertLess(g.gamma_tail(J),g.gamma_tail(J-1))
            direct=sum((F(4,(4*j+1)**2) for j in range(J,500)),F(0))
            self.assertLess(direct,g.gamma_tail(J))

    def test_operator_error_joint_limit_and_guards(self):
        for J in (2,6,14):
            for N in (8,16,32):
                A=g.step_operator_error(F(1,5),J,N,F(7))
                self.assertGreater(A,0)
                self.assertLess(g.step_operator_error(F(1,5),J,N*2,F(7)),A)
                self.assertLess(g.step_operator_error(F(1,5),J*2,N,F(7)),A)
        with self.assertRaises(g.GaussianSourceError):g.gamma_tail(0)
        with self.assertRaises(g.GaussianSourceError):g.step_operator_error(F(1,5),2,1,F(7))

    def test_parent_psi_vs_suzuki_g_contact(self):
        try:import mpmath as mp
        except ImportError:self.skipTest("optional mpmath")
        from observational_succ.completed_weil_transport import screw_potential_J
        mp.mp.dps=64
        for R in (mp.mpf("0.12"),mp.mpf("0.79"),mp.mpf("1.3")):
            for J in (2,6,12):
                psi=screw_potential_J(R,J,dps=64)
                gJ=g.signed_suzuki_g(R,J,dps=64)
                SJ=mp.fsum(mp.mpf(2)/(4*j+1)-mp.mpf(1)/(2*j+1) for j in range(J))
                correction=R*(mp.pi/4+mp.log(2)/2-SJ)
                self.assertLess(abs(psi+gJ-correction),mp.mpf("1e-55"))

    def test_signed_step_mean_zero_is_not_sign_certificate(self):
        try:import mpmath as mp
        except ImportError:self.skipTest("optional mpmath")
        a=mp.mpf("0.2"); J=12; N=5
        M=g.centered_screw_matrix(a,J,N,dps=60)
        for i in range(N):
            self.assertLess(abs(sum(M[i,j] for j in range(N))),mp.mpf("1e-50"))
        L=g.signed_lipschitz(a,J,dps=60)
        self.assertGreater(L,0)
        self.assertGreater(g.step_operator_error(a,J,N,L),0)


if __name__=="__main__": unittest.main()
