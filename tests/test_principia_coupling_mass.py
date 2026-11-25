import unittest
from dataclasses import replace
from fractions import Fraction
from observational_succ.principia_coupling_mass import (
    MassSourceError, make_mass, compress_mass, verify_compressed_mass,
    evaluate_compression, gaussian_shell_coupling,
)


class CoupledMassTests(unittest.TestCase):
    def test_unique_linear_and_pair_fiber_pushforward(self):
        m = make_mass('arith',('p0','p1','p2'),('A','A','B'),
                      (2,-1,3),((1,2,3),(4,5,6),(7,8,9)))
        c = verify_compressed_mass(m,compress_mass(m))
        self.assertEqual(c.classes,('A','B'))
        self.assertEqual(c.linear,(Fraction(1),Fraction(3)))
        self.assertEqual(c.pairing,((Fraction(12),Fraction(9)),(Fraction(15),Fraction(9))))
        self.assertEqual(evaluate_compression(m,c,[4,2],[-1,3]),
                         (Fraction(10),Fraction(12*4*(-1)+9*4*3+15*2*(-1)+9*2*3)))
    def test_same_observed_zero_two_different_signed_histories(self):
        cancel=make_mass('cancel',('a','b'),('0','0'),(1,-1),((1,-1),(-1,1)))
        support=make_mass('noncancel',('a','b'),('0','0'),(1,1),((1,1),(1,1)))
        self.assertEqual(compress_mass(cancel).linear,(Fraction(0),))
        self.assertEqual(compress_mass(cancel).pairing,((Fraction(0),),))
        self.assertEqual(compress_mass(support).linear,(Fraction(2),))
        self.assertEqual(compress_mass(support).pairing,((Fraction(4),),))
        self.assertNotEqual(compress_mass(cancel).source,compress_mass(support).source)
    def test_diagonal_only_loses_coupling(self):
        m=make_mass('two',('a','b'),('zero','zero'),(1,-1),((1,-1),(-1,1)))
        c=compress_mass(m)
        self.assertEqual(c.pairing[0][0],0)
        self.assertEqual(sum(m.pairing[i][i] for i in range(2)),2)
    def test_forged_source_or_pair_coefficients_rejected(self):
        m=make_mass('arith',('p0','p1'),('A','A'),(1,-1),((1,-1),(-1,1)))
        c=compress_mass(m)
        with self.assertRaises(MassSourceError):verify_compressed_mass(m,replace(c,source='fake'))
        with self.assertRaises(MassSourceError):verify_compressed_mass(m,replace(c,linear=(Fraction(1),)))
        with self.assertRaises(MassSourceError):verify_compressed_mass(m,replace(c,pairing=((Fraction(1),),)))
    def test_class_fine_versus_coarse(self):
        m=make_mass('src',('p0','p1'),('A','B'),(2,-3),((1,2),(3,4)))
        c=compress_mass(m)
        self.assertEqual(evaluate_compression(m,c,[3,5]),
                         (Fraction(-9),Fraction(1*9+2*15+3*15+4*25)))
        with self.assertRaises(MassSourceError):evaluate_compression(m,c,[3])
    def test_empty_source_has_zero_mass(self):
        m=gaussian_shell_coupling(3,4)
        c=compress_mass(m)
        self.assertEqual((c.classes,c.linear,c.pairing),((),(),()))
        self.assertEqual(evaluate_compression(m,c,[]),(0,0))
    def test_real_gaussian_theta_fourth_jet_preserves_quadratic(self):
        m=gaussian_shell_coupling(2,4)
        c=verify_compressed_mass(m,compress_mass(m))
        self.assertEqual(len(m.paths),4)
        self.assertEqual(c.linear,(Fraction(-16),))
        self.assertEqual(c.pairing,((Fraction(256),),))
        self.assertEqual(sum(m.pairing[i][i] for i in range(4)),64)
        self.assertEqual(evaluate_compression(m,c,[1]),(-16,256))
    def test_second_jet_zero_due_to_correlated_imaginary_signs(self):
        m=gaussian_shell_coupling(2,2)
        c=compress_mass(m)
        self.assertEqual(c.linear,(Fraction(0),))
        self.assertEqual(c.pairing,((Fraction(0),),))
        self.assertEqual(sum(m.pairing[i][i] for i in range(4)),16)
    def test_nontrivial_source_shift_refused(self):
        m=gaussian_shell_coupling(2,4)
        c=compress_mass(m)
        with self.assertRaises(MassSourceError):verify_compressed_mass(replace(m,classes=('fake',)*4),c)
        with self.assertRaises(MassSourceError):gaussian_shell_coupling(2,3)
    def test_exact_linear_bilinear_mutations(self):
        m=make_mass('s',('p','q'),('A','A'),(Fraction(2,3),Fraction(-1,7)),
                    ((Fraction(4,9),Fraction(-2,21)),(Fraction(-2,21),Fraction(1,49))))
        c=compress_mass(m)
        amp=Fraction(2,3)-Fraction(1,7)
        self.assertEqual(c.linear[0],amp)
        self.assertEqual(c.pairing[0][0],amp*amp)
        for x in (Fraction(0),Fraction(1),Fraction(11,4)):
            self.assertEqual(evaluate_compression(m,c,[x]),(amp*x,amp*amp*x*x))

if __name__=='__main__':unittest.main()
