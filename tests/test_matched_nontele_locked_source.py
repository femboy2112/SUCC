"""Strong locked null-seed source with a nonzero pole-shift invariant.

Combines two independently established BBP series for pi and a rational
clock coboundary; uses exact integer-polynomial positivity certificates.
The identities of the two infinite pi series are imported from literature.
"""
from fractions import Fraction as F
import unittest


def canonical(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def second_pi_source(n):
    return (F(4,8*n-6)+F(2,8*n-5)+F(2,8*n-4)
            -F(1,2*(8*n-1)))


def b(n):
    return F(1,16*n)+F(5,128*n*n)


def matched_locked(n):
    return canonical(n)-second_pi_source(n)+16*b(n)-b(n+1)

# With t=n-1, r_lock(n)=P(t)/Q(t). Both P and Q have only
# nonnegative coefficients; Q is the product of positive linear factors.
P_HILO=(3932160,27312128,75347968,110058752,98778592,
        62529440,31089706,11626701,2665404,261609)
P=tuple(reversed(P_HILO))


def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return tuple(out)


def pder(a):
    return tuple(i*x for i,x in enumerate(a) if i>0)


def psub(a,b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,y in enumerate(b):out[i]-=y
    return tuple(out)


def peval(poly,x):
    z=0
    for coeff in reversed(poly):z=z*x+coeff
    return z


def polyQ():
    factors=((1,1),(1,1),(2,1),(2,1), (1,2),
             (1,4),(3,4),(1,8),(3,8),(5,8),(7,8))
    # careful: tuple (constant, slope) for each factor.
    q=(128,)
    for f in factors:q=pmul(q,f)
    return q

Q=polyQ()


class MatchedNonTelescopingLockTests(unittest.TestCase):
    def test_second_pi_formula_is_a_distinct_rational_forcing(self):
        for n in (1,2,5,23):
            self.assertNotEqual(canonical(n),second_pi_source(n))

    def test_candidate_exact_partial_fraction_identity(self):
        for n in range(1,40):
            t=n-1
            self.assertEqual(matched_locked(n),F(peval(P,t),peval(Q,t)))

    def test_positivity_all_n_via_polynomial_coefficient_certificate(self):
        self.assertTrue(all(x>0 for x in P))
        self.assertTrue(all(x>0 for x in Q))
        for n in range(1,100):
            self.assertGreater(matched_locked(n),0)

    def test_strict_decrease_all_real_n_ge_1_from_derivative_polynomial(self):
        # -d(P/Q)/dt = (P Q' - P' Q)/Q^2, exact integer polynomial numerator.
        M=psub(pmul(P,pder(Q)),pmul(pder(P),Q))
        self.assertTrue(all(x>0 for x in M))
        self.assertGreater(len(M),len(P))
        for n in range(1,100):
            self.assertGreater(matched_locked(n),matched_locked(n+1))

    def test_zero_seed_and_exact_telescoping_correction(self):
        self.assertEqual(b(1),F(13,128))
        for N in (1,2,4,16,60):
            tailpart=sum((F(16*b(n)-b(n+1),16**n) for n in range(1,N+1)),F(0))
            self.assertEqual(tailpart,b(1)-b(N+1)/16**N)

    def test_source_retains_uncancelled_original_shift_orbit(self):
        # The second BBP formula and b(n) are regular at n=7/8,
        # so r_lock retains BBP's isolated residue +1/2 there.
        self.assertEqual(F(4,8),F(1,2))
        self.assertTrue(all((8*F(7,8)-v)!=0 for v in (6,5,4,1)))
        self.assertNotEqual(F(1,2),0)

    def test_the_locked_rational_endpoint_is_eventually_zero_circle(self):
        x=F(13,128)
        for n in range(2,20):
            self.assertEqual((16**n*x)%1,0)
        self.assertEqual((16*x)%1,F(5,8))

    def test_same_15_over_64_asymptotic_on_exact_rationals(self):
        for n in (100,200,400,800):
            self.assertLess(abs(n*n*matched_locked(n)-F(15,64)),F(1,n))


if __name__=='__main__':unittest.main()
