"""Exact CRT/character checks, and hostile higher Fermat stage."""
import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import fermat_unit_bridge as s

class CRTBridgeTests(unittest.TestCase):
    def test_first_two_odd_primes_and_phi_plateau(self):
        self.assertEqual(s.units(15),(1,2,4,7,8,11,13,14))
        self.assertEqual(s.totient(3),2)
        self.assertEqual(s.totient(4),2)
        self.assertEqual(s.totient(15),8)
        self.assertEqual(s.totient(16),8)
        self.assertEqual(s.totient(255),128)
        self.assertEqual(s.totient(256),128)

    def test_group_isomorphism_all_units(self):
        for x in s.units(15):
            y=s.unit15_to16(x)
            self.assertEqual(s.unit16_to15(y),x)
            for a in s.units(15):
                self.assertEqual(s.unit15_to16((a*x)%15),
                                 s.unit15_to16(a)*y%16)
        self.assertEqual([s.unit15_to16(x) for x in s.units(15)],
                         [1,11,9,5,3,15,13,7])

    def test_eight_character_orthogonality(self):
        import cmath
        chars=[(u,v) for u in (0,1) for v in range(4)]
        for u,v in chars:
            for u2,v2 in chars:
                val=sum((complex(*s.character15(u,v,x))*
                          complex(*s.character15(u2,v2,x)).conjugate()
                         for x in s.units(15)))
                self.assertEqual(val,8 if (u,v)==(u2,v2) else 0)

    def test_higher_fermat_stage_totient_not_unit_isomorphism(self):
        orders15=s.finite_multiplicative_orders(15)
        orders16=s.finite_multiplicative_orders(16)
        self.assertEqual(sorted(orders15.values()),sorted(orders16.values()))
        self.assertEqual(max(s.finite_multiplicative_orders(255).values()),16)
        self.assertEqual(max(s.finite_multiplicative_orders(256).values()),64)
        self.assertEqual(s.fermat_stage(1),(3,4))
        self.assertEqual(s.fermat_stage(2),(15,16))
        self.assertEqual(s.fermat_stage(3),(255,256))
        self.assertEqual(s.fermat_stage(4),(65535,65536))

    def test_group_bridge_is_not_integer_alphabet_conjugacy(self):
        # Eight units per group, but full alphabets have 15 vs 16 letters.
        self.assertNotEqual(len(range(15)),len(range(16)))
        self.assertEqual(s.totient(15),s.totient(16))
        # Addition crosses the unit boundary; it is not a ring isomorphism.
        self.assertEqual((1+1)%15,2)
        self.assertEqual(s.unit15_to16(2),11)
        self.assertNotEqual(s.unit15_to16(2),(s.unit15_to16(1)+1)%16)
        # Base 16 multiplication is zero modulo 16, not a unit group action.
        for x in s.units(16):self.assertEqual(16*x%16,0)


    def test_complete_16_digit_hybrid_character_chart(self):
        B=s.hybrid_basis16()
        self.assertEqual((len(B),len(B[0])),(16,16))
        G=s.basis_gram16()
        for i in range(16):
            for j in range(16):
                self.assertEqual(G[i][j],(8 if i==j else 0,0))
        # Nonunit sector is NOT discarded. Every even digit has 8 nonzero
        # Walsh coefficients; every odd digit has 8 Gaussian CRT coefficients.
        for digit in range(16):
            self.assertEqual(sum(B[i][digit]!=(0,0) for i in range(16)),8)
        for i in range(8):
            self.assertEqual(sum(B[i][digit]!=(0,0) for digit in range(16)),8)
        for i in range(8,16):
            self.assertEqual(sum(B[i][digit]!=(0,0) for digit in range(16)),8)

    def test_hybrid_digit_reconstruction_exact(self):
        B=s.hybrid_basis16()
        values=tuple((k*k-3*k+1,k%3-1) for k in range(16))
        vhat=[s.sum_gaussian(s.gaussian_mul(B[i][j],values[j]) for j in range(16))
              for i in range(16)]
        for j in range(16):
            recovered=s.sum_gaussian(s.gaussian_mul(s.gaussian_conj(B[i][j]),vhat[i])
                                     for i in range(16))
            self.assertEqual(recovered,(8*values[j][0],8*values[j][1]))

    def test_validation(self):
        for x in (0,3,5,6,9,10,12):
            with self.assertRaises(ValueError):s.unit15_to16(x)
        for x in (0,2,4,6,8,10,12,14):
            with self.assertRaises(ValueError):s.unit16_to15(x)
        for k in (-1,0,6):
            with self.assertRaises(ValueError):s.fermat_stage(k)

if __name__=='__main__':unittest.main(verbosity=2)
