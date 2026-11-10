"""Source Gamma analogue: exact BBP pole checks and hostile 16x16 spectra."""
import unittest
from fractions import Fraction

from observational_succ.bbp_gamma_matrix_deformation import (
    A, POLE_SHIFTS, POLE_WEIGHTS, weighted_harmonic_step,
    rational_pole_step, partial_finite_part, bbp_gamma_digamma,
    bbp_gamma_closed, pole_gamma_coordinate, source_gamma_coefficient,
    q_euler_constant, matrix_source_gamma, transition_counts, row_normalized,
    blocking_kernel, matched_leading_mutation_shift,
)

class BBPGammaSourceTests(unittest.TestCase):
    def test_original_pole_weights(self):
        self.assertEqual(sum(POLE_WEIGHTS), A)
        self.assertEqual(POLE_SHIFTS,(Fraction(1,8),Fraction(1,2),Fraction(5,8),Fraction(3,4)))
        for n in (1,2,3,4,7,16,31,96,255):
            self.assertEqual(weighted_harmonic_step(n),rational_pole_step(n))

    def test_exact_source_plus_gamma(self):
        from mpmath import mp
        with mp.workdps(65):
            g=bbp_gamma_digamma(65)
            g2=bbp_gamma_closed(65)
            self.assertLess(abs(g-g2),mp.mpf('1e-58'))
            self.assertLess(abs(g-mp.mpf('3.3224979111064047565947323878')),mp.mpf('1e-25'))
            self.assertLess(abs(g/A-mp.mpf('14.175991087387326961470858')),mp.mpf('1e-23'))

    def test_gamma_recursion_at_integers(self):
        from mpmath import mp
        with mp.workdps(55):
            for n in (1,2,3,7,16,31):
                delta=pole_gamma_coordinate(n,55)-pole_gamma_coordinate(n-1,55)
                w=weighted_harmonic_step(n)
                exact=mp.mpf(w.numerator)/w.denominator
                self.assertLess(abs(delta+exact),mp.mpf('1e-48'))

    def test_partial_fin_part_positive_and_converges(self):
        b=partial_finite_part(256)
        self.assertGreater(b,0)
        self.assertLess(abs(float(b)+float(A)*0.5772156649015329-float(bbp_gamma_closed(55))),.002)

    def test_exact_q_gamma_not_same_constant(self):
        self.assertAlmostEqual(float(q_euler_constant('0.0625')),0.13189581822239802,places=14)
        self.assertNotAlmostEqual(float(q_euler_constant('0.0625')),float(bbp_gamma_digamma()),places=2)

    def test_first_matrix_coefficient(self):
        self.assertAlmostEqual(float(source_gamma_coefficient(1)),27.75159390688817,places=11)

    def test_mpmath_precision_is_scoped(self):
        from mpmath import mp
        old=mp.dps
        _=bbp_gamma_digamma(70)
        _=source_gamma_coefficient(3,70)
        _=q_euler_constant(Fraction(1,16),70)
        self.assertEqual(mp.dps,old)

    def test_hurwitz_series_scalar_holdout(self):
        from mpmath import mp
        with mp.workdps(65):
            for x in ('0.03125','-0.03125'):
                xx=mp.mpf(x)
                approx=bbp_gamma_digamma(65)+sum((-1)**m*source_gamma_coefficient(m,65)*xx**m for m in range(1,30))
                self.assertLess(abs(approx-pole_gamma_coordinate(xx,65)),mp.mpf('5e-16'))

    def test_haar_matrix_identity(self):
        import numpy as np
        H=np.ones((16,16))/16
        G, tail=matrix_source_gamma(H,terms=8)
        self.assertLess(float(np.linalg.norm(G-float(bbp_gamma_closed())*np.eye(16))),1e-12)
        self.assertEqual(tail,0)

    def test_nilpotent_hides_in_gamma_jordan(self):
        import numpy as np
        H=np.ones((16,16))/16
        u=np.zeros(16);u[0]=1;u[1]=-1
        v=np.zeros(16);v[:3]=[1,1,-2]
        X=np.outer(u,v)/64
        P=H+X
        self.assertLess(float(np.max(np.abs(P@P-H))),1e-15)
        self.assertLess(float(np.max(np.abs(X@X))),1e-15)
        self.assertGreater(float(np.linalg.norm(X,2)),0)
        M,tail=matrix_source_gamma(P,terms=24)
        target=float(bbp_gamma_closed())*np.eye(16)-float(source_gamma_coefficient(1))*X
        self.assertLess(float(np.linalg.norm(M-target,2)),1e-12)
        self.assertGreater(float(np.linalg.norm(M-float(bbp_gamma_closed())*np.eye(16),2)),1.5)
        self.assertLess(tail,0.00001)

    def test_source_gamma_local_two_sided_haar_bound(self):
        import numpy as np
        H=np.ones((16,16))/16
        u=np.zeros(16);u[0]=1;u[1]=-1
        v=np.zeros(16);v[:3]=[1,1,-2]
        # Source-weighted nilpotent probe scaled into the proved 1/32 radius.
        P=H+np.outer(u,v)/256
        x=float(np.linalg.norm(P-H,2))
        self.assertLess(x,1/32)
        G,_=matrix_source_gamma(P,terms=24)
        dev=float(np.linalg.norm(G-float(bbp_gamma_digamma())*np.eye(16),2))
        self.assertGreaterEqual(dev+1e-12,13*x)
        self.assertLessEqual(dev,43*x+1e-12)

    def test_bad_source_matrix_rejected(self):
        import numpy as np
        H=np.eye(16)
        with self.assertRaisesRegex(ValueError,'series'):
            matrix_source_gamma(H)

    def test_blocking_kernel_cocycle_and_q_number(self):
        for u in (Fraction(0),Fraction(1,2),Fraction(1)):
            for g,h in ((1,2),(2,3),(3,1)):
                lhs=blocking_kernel(g+h,u)
                rhs=16**h*blocking_kernel(g,u)+u**(8*g)*blocking_kernel(h,u)
                self.assertEqual(lhs,rhs)
                q=u**8/16
                self.assertEqual(blocking_kernel(g,u),
                                 16**(g-1)*sum((q**j for j in range(g)),Fraction()))

    def test_matched_leading_mutation_finite_shift(self):
        def mutant(n):
            return Fraction(1,10)*(Fraction(1,8*n-7)-2*Fraction(1,8*n-4)
                                   -Fraction(1,8*n-3)+2*Fraction(1,8*n-2))
        approx=sum((n*mutant(n) for n in range(1,500)),Fraction())
        shift=matched_leading_mutation_shift(65)
        self.assertGreater(float(shift),0)
        self.assertLess(abs(float(approx)-float(shift)),.001)
        self.assertAlmostEqual(float(shift),0.06718232134424341,places=12)

    def test_conditional_gamma_does_not_control_first_digit(self):
        import numpy as np
        H=np.ones((16,16))/16
        unequal=np.array([2/17]+[1/17]*15)
        unequal=unequal/unequal.sum()
        pair=unequal[:,None]*H
        self.assertGreater(float(np.max(np.abs(pair-1/256))),.001)
        gam,_=matrix_source_gamma(H)
        self.assertLess(float(np.linalg.norm(gam-float(bbp_gamma_closed())*np.eye(16))),1e-12)

    def test_linear_counts_no_fake_wrap(self):
        C=transition_counts('012345670')
        self.assertEqual(sum(map(sum,C)),8)
        self.assertEqual(C[0][1],1)
        self.assertEqual(C[7][0],1)
        with self.assertRaisesRegex(ValueError,'observed'):
            row_normalized(C)

if __name__=='__main__':unittest.main()
