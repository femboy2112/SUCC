"""Independent rational Legendre contact-projection algebra and no-ghost controls."""
import unittest
from fractions import Fraction as F
from observational_succ.contact_ladder_projection import (
    ContactLadderError,projected_contact_legendre_coefficients,
    projected_contact_gram,projected_contact_trial_gram,
    exact_contact_low4_certificate,
)
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial,poly_primitive_zero_at_left,poly_mul,poly_integral,
)
from observational_succ.direct_quotient_schur import _monomial_gram,_inverse


class SparseVersusDenseExact(unittest.TestCase):
    def test_low_modes_and_contact_zero_space(self):
        result=exact_contact_low4_certificate()
        self.assertTrue(result["source_contact_direction_first_two_zero"])
        self.assertEqual(tuple(result["gram"][i][i] for i in range(4)),
                         (F(0),F(0),F(1,1764),F(1,3564)))

    def test_dense_primitive_projection_independent_oracle(self):
        n=8;a=F(1,2);inverse=_inverse(_monomial_gram(a,3))
        p=[poly_primitive_zero_at_left(legendre_polynomial(k,a),a)
           for k in range(1,n+1)]
        dense=[]
        for i in range(n):
            row=[]
            for j in range(n):
                full=poly_integral(poly_mul(p[i],p[j]),-a,a)
                m=[tuple(poly_integral(poly_mul(poly,tuple([F(0)]*t+[F(1)])),-a,a)
                         for t in range(4)) for poly in (p[i],p[j])]
                projection=sum((m[0][s]*inverse[s][t]*m[1][t]
                                for s in range(4) for t in range(4)),F(0))
                row.append(full-projection)
            dense.append(tuple(row))
        self.assertEqual(projected_contact_gram(n),tuple(dense))

    def test_mixed_parity_and_malformed_input(self):
        v=((F(1),F(0)),(F(0),F(1)),(F(3,7),F(0)),
           (F(0),F(-1,3)),(F(1,5),F(0)),(F(0),F(2,9)))
        K=projected_contact_trial_gram(v)
        self.assertGreater(K[0][0],0)
        self.assertGreater(K[1][1],0)
        self.assertEqual(K[0][1],0)
        with self.assertRaises(ContactLadderError):
            projected_contact_trial_gram(((1,True),))
        with self.assertRaises(ContactLadderError):
            projected_contact_legendre_coefficients(0)


if __name__=="__main__":unittest.main()
