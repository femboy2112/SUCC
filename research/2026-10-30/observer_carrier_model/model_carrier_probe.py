"""Exact finite controls for SUCC observer/carrier model adequacy.

All programs and state laws are DECLARED finite witnesses; none samples pi.
Original BBP signed four poles and authentic U0=0 are untouched.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import log
import unittest

BASE=16
POLES=((4,0),(-2,3),(-1,4),(-1,5))


def bbp_r(n):
    return sum((F(c,8*n-7+d) for c,d in POLES),F(0))


def digit(x):
    return (BASE*x).numerator // (BASE*x).denominator


def T(x):
    y=BASE*x
    return y-digit(x)


def fair_preimages(measure):
    """Apply fair model to a finitely supported probability measure."""
    result=defaultdict(F)
    for y,mass in measure.items():
        for d in range(BASE):
            result[(d+y)/BASE]+=mass/BASE
    return dict(result)


def w1_atomic(p,q):
    """Exact W1 between rational atomic measures on the ordinary interval."""
    atoms=sorted(set(p)|set(q))
    difference=F(0);cost=F(0)
    for j,x in enumerate(atoms[:-1]):
        difference+=p.get(x,F(0))-q.get(x,F(0))
        cost+=abs(difference)*(atoms[j+1]-x)
    assert difference+p.get(atoms[-1],F(0))-q.get(atoms[-1],F(0)) == 0
    return cost


def conditional_entropy_from_orbit(x0,N,visible_future_digits):
    """H(D(x_n) | first k digits of T(x_n)) for an exact finite orbit."""
    groups=defaultdict(lambda:defaultdict(int))
    x=x0
    for _ in range(N):
        d=digit(x);y=T(x)
        label=tuple(_digits(y,visible_future_digits))
        groups[label][d]+=1
        x=y
    entropy=0.0
    for counts in groups.values():
        total=sum(counts.values())
        for count in counts.values():
            p=count/total
            entropy-=(total/N)*p*log(p)
    return entropy


def _digits(x,k):
    for _ in range(k):
        d=digit(x)
        yield d
        x=T(x)


def stationary_bern_kl(p):
    """Fair-branch KL deficit in nats for a full-support Bernoulli digit law."""
    assert sum(p)==1 and all(v>0 for v in p)
    entropy=-sum(float(x)*log(float(x)) for x in p)
    divergence=sum(float(x)*log(BASE*float(x)) for x in p)
    return entropy,divergence


class ObserverCarrierAdequacy(unittest.TestCase):
    def test_exact_radix_inverse_is_a_rechart_not_fairness(self):
        for x in (F(0),F(1,17),F(2,3),F(255,256),F(1,256)):
            d=digit(x);y=T(x)
            self.assertEqual(x,F(d+y,BASE))
            self.assertTrue(0 <= d < BASE)
            self.assertTrue(0 <= y < 1)

    def test_coherent_carrier_invariant_but_fair_model_disagrees(self):
        mu={F(0):F(1)}
        self.assertEqual(T(F(0)),F(0))
        generated=fair_preimages(mu)
        self.assertEqual(len(generated),16)
        self.assertEqual(w1_atomic(mu,generated),F(15,32))
        self.assertNotEqual(mu,generated)

    def test_model_only_iterations_always_approach_haar(self):
        mu={F(0):F(1)}
        for k in range(1,4):
            mu=fair_preimages(mu)
            n=BASE**k
            self.assertEqual(len(mu),n)
            self.assertEqual(set(mu),{F(j,n) for j in range(n)})
            self.assertTrue(all(weight==F(1,n) for weight in mu.values()))
            # Integrate the optimal monotone transport cell-by-cell.
            cost=sum((F(1,2*n*n) for _ in range(n)),F(0))
            self.assertEqual(cost,F(1,2*n))
        self.assertEqual(w1_atomic({F(0):F(1)},{F(1,2):F(1)}),F(1,2))

    def test_fair_operation_contracts_w1_exactly(self):
        p={F(0):F(1)};q={F(1,2):F(1)}
        self.assertEqual(w1_atomic(fair_preimages(p),fair_preimages(q)),
                         w1_atomic(p,q)/16)

    def test_coarse_observer_not_closed_under_radix_dynamics(self):
        x0=F(0);x1=F(1,256)
        self.assertEqual(digit(x0),digit(x1))
        self.assertNotEqual(digit(T(x0)),digit(T(x1)))
        # No deterministic transition on the single observed digit can
        # commute with the true radix-16 carrier transition.

    def test_exact_finite_future_conditioning_changes_with_resolution(self):
        # x=1/257 has exact length-four orbit under multiplication by 16.
        orbit=[];x=F(1,257)
        for _ in range(4):
            orbit.append(x);x=T(x)
        self.assertEqual(x,orbit[0])
        self.assertEqual(len(set(orbit)),4)
        self.assertAlmostEqual(conditional_entropy_from_orbit(F(1,257),4,1),log(2))
        self.assertEqual(conditional_entropy_from_orbit(F(1,257),4,2),0.0)

    def test_two_cycle_invariant_but_not_fair(self):
        a=F(1,17);b=F(16,17)
        self.assertEqual(T(a),b);self.assertEqual(T(b),a)
        mu={a:F(1,2),b:F(1,2)}
        self.assertEqual({T(x) for x in mu},set(mu))
        self.assertGreater(w1_atomic(mu,fair_preimages(mu)),0)
        self.assertEqual(conditional_entropy_from_orbit(a,2,1),0.0)

    def test_full_support_biased_bernoulli_branch_deficit(self):
        probs=(F(1,2),)+(F(1,30),)*15
        h,kl=stationary_bern_kl(probs)
        self.assertGreater(kl,0)
        self.assertLess(h,log(16))
        self.assertAlmostEqual(h+kl,log(16),places=12)
        self.assertEqual(sum(probs),1)

    def test_periodic_zero_bernoulli_deficit_is_log16(self):
        K=[F(1)]+[F(0)]*15
        self.assertAlmostEqual(sum(float(v)*log(16*float(v))
                                   for v in K if v>0),log(16))

    def test_selected_carry_lift_distinguishes_late_circle_alias(self):
        r1=bbp_r(1)
        self.assertEqual(r1,F(47,15))
        x0=F(0);x1=F(1,16)
        y0=16*x0+r1;y1=16*x1+r1
        k0=y0.numerator//y0.denominator
        k1=y1.numerator//y1.denominator
        self.assertEqual((k0,k1),(3,4))
        self.assertEqual(y0-k0,y1-k1)  # circle phase aliases; lifted carries differ

    def test_original_four_pole_source_is_not_a_fair_branch_law(self):
        self.assertEqual(bbp_r(1),F(47,15))
        self.assertEqual(bbp_r(2),F(106,819))
        self.assertGreater(bbp_r(2),0)
        self.assertLess(bbp_r(2),bbp_r(1))

    def test_fiber_property_needs_constancy_on_equal_model_states(self):
        # Abstract factorization lemma, finite witness: P factors through q
        # iff each q-fiber has one and only one P value.
        carrier=[('a',0,True),('b',0,False),('c',1,True)]
        by_model=defaultdict(set)
        for _,m,p in carrier:by_model[m].add(p)
        self.assertEqual(by_model[0],{True,False})
        self.assertFalse(all(len(values)==1 for values in by_model.values()))


if __name__=='__main__':
    unittest.main(verbosity=2)
