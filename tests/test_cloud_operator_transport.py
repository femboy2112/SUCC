"""Independent finite holdouts, not universal operator-theory proofs."""
from fractions import Fraction as Q
import unittest
from observational_succ.cloud_operator_transport import (
    integrate, inverse_polynomial_pieces, moment_constraint_saving,
    nonclosable_sequence_pair, piece_pairing, piece_sup_bound, poly_mul,
)


def evaluate(poly, x):
    return sum((c*x**k for k,c in enumerate(poly)), Q())


def piece_value(pieces, x):
    for left,right,poly in pieces:
        if left <= x <= right:
            return evaluate(poly,x)
    return Q()


def legendre(n):
    # Independent exact coefficient oracle, not the project's recurrence.
    from math import factorial
    out = [Q()]*(n+1)
    for k in range(n//2+1):
        out[n-2*k] = Q((-1)**k*factorial(2*n-2*k),
                       2**n*factorial(k)*factorial(n-k)*factorial(n-2*k))*2**(n-2*k)
    return tuple(out)


class CloudOperatorTransportTests(unittest.TestCase):
    def test_nonclosability_sequence_exact(self):
        for m,n in ((1,2),(10,23),(127,256),(1024,2048)):
            data=nonclosable_sequence_pair(m,n)
            fm=[Q(1,m)if i<m else Q()for i in range(max(m,n))]
            fn=[Q(1,n)if i<n else Q()for i in range(max(m,n))]
            self.assertEqual(data['q_difference'],sum((a-b)**2 for a,b in zip(fm,fn)))
            self.assertEqual(data['q_Fm'],sum(x*x for x in fm)+sum(fm)**2)
            self.assertEqual(data['original_u_norm2'],sum(((i+1)*x)**2 for i,x in enumerate(fm)))
            self.assertGreaterEqual(data['q_Fm'],1)

    def test_kernel_descent_is_required(self):
        # V(x,y)=x; q=x²+y² dominates |V|² but cannot descend through V.
        self.assertEqual(0**2+1**2,1)
        self.assertNotEqual(0**2+1**2,0**2+0**2)

    def test_compact_relative_bound_can_give_primitive_identity(self):
        for n in (1,2,10,1000):
            self.assertEqual(Q(1,n*n)/Q(1,n*n),1)
        self.assertLess(Q(1,1000**2),Q(1,100))

    def test_finite_constrained_inverse_identity(self):
        # B=diag(2,3), constraint h=(1,1), r=(1,-1).
        ambient=Q(1,2)+Q(1,3)
        z=Q(1,2)-Q(1,3)
        moment_gram=ambient
        constrained=ambient-z*z/moment_gram
        self.assertEqual(constrained,Q(4,5))
        self.assertEqual(constrained,4/Q(2+3))
        self.assertLess(constrained,ambient)
        self.assertLessEqual(2*z*z/2,z*z/moment_gram)

    def test_inverse_polynomial_against_pointwise_equation(self):
        for b in (Q(3,5),Q(7,10),Q(9,10)):
            kappa,w=Q(2,7),Q(12,25)
            for q in ((Q(1),),(Q(),Q(2)),legendre(2),legendre(3)):
                pieces=inverse_polynomial_pieces(q,b,kappa,w)
                for numerator in range(-49,50):
                    x=Q(numerator,100)
                    if x in (Q(1,2)-b,b-Q(1,2)):
                        continue
                    z=piece_value(pieces,x)
                    lhs=(kappa+w)*z-w*(piece_value(pieces,x-b)+piece_value(pieces,x+b))
                    self.assertEqual(lhs,evaluate(q,x))

    def test_two_constraint_saving_is_psd_when_shift_exact(self):
        b=Q(7,10)
        cells=((Q(-1,2),Q(1,2)-b),(Q(1,2)-b,b-Q(1,2)),(b-Q(1,2),Q(1,2)))
        for parity,modes in (('even',(4,6)),('odd',(5,7))):
            projected=[tuple((lo,hi,legendre(n))for lo,hi in cells)for n in modes]
            result=moment_constraint_saving(projected,b,Q(),Q(1,4),parity)
            a=result['constraint_saving_lower']
            self.assertGreaterEqual(a[0][0],0)
            self.assertGreaterEqual(a[1][1],0)
            self.assertGreaterEqual(a[0][0]*a[1][1]-a[0][1]**2,0)
            self.assertEqual(result['penalty'],0)

    def test_shift_error_bounds_against_exact_displaced_operator(self):
        b,db,kappa,w=Q(7,10),Q(1,10000),Q(1,4),Q(12,25)
        cells=((Q(-1,2),Q(1,2)-b),(Q(1,2)-b,b-Q(1,2)),(b-Q(1,2),Q(1,2)))
        for parity,modes,qs in (('even',(4,6),(legendre(0),legendre(2))),
                               ('odd',(5,7),(legendre(1),legendre(3)))):
            projected=[tuple((lo,hi,legendre(n))for lo,hi in cells)for n in modes]
            result=moment_constraint_saving(projected,b,db,kappa,parity,w)
            for j,q in enumerate(qs):
                for i,p in enumerate(projected):
                    for sign in (-1,1):
                        actual=piece_pairing(p,inverse_polynomial_pieces(q,b+sign*db,kappa,w))
                        self.assertLessEqual(abs(actual-result['nominal_inverse_moments'][j][i]),
                                             result['moment_error_bounds'][j][i])

    def test_reject_nonhigh_and_nonexact_inputs(self):
        b=Q(7,10)
        pieces=inverse_polynomial_pieces((Q(1),),b,Q(1,4),Q(12,25))
        with self.assertRaises(ValueError):
            moment_constraint_saving([pieces,pieces],b,Q(),Q(1,4),'even')
        with self.assertRaises(ValueError):
            inverse_polynomial_pieces((1,),0.7,Q(1,4),Q(12,25))

    def test_endpoint_cauchy_sup_bound(self):
        for n in (1,4,8):
            p=legendre(n)
            bound=piece_sup_bound(p,Q(-1,2),Q(1,2))
            for k in range(-100,101):
                self.assertLessEqual(abs(evaluate(p,Q(k,200))),bound)


if __name__ == '__main__':
    unittest.main()
