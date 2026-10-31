from fractions import Fraction as Q
import unittest
import resolvent as r


class SourceResolventTests(unittest.TestCase):
    def test_original_four_poles_against_positive_regrouping(self):
        for n in range(1,301):
            a=8*n-7
            self.assertEqual(r.source(n),Q(6,a*(a+3))+Q(4,a*(a+4))+Q(5,a*(a+5)))

    def test_exact_orthogonality(self):
        for d in range(1,9):
            mu=r.moments(2*d+1);p=r.monic_orthogonal(mu,d)
            for j in range(d):
                self.assertEqual(r.inner(p,[Q()]*j+[Q(1)],mu),0)
            self.assertGreater(r.inner(p,p,mu),0)

    def test_certificates_against_separate_exact_series(self):
        lo,hi=r.bbp_interval(75)
        for d in range(1,9):
            c=r.certificate(d)
            self.assertLess(c['lower'],lo)
            self.assertGreater(c['upper'],hi)
            self.assertLess(c['upper']-c['center'],c['uniform_error'])

    def test_fresh_order_certificates(self):
        lo,hi=r.bbp_interval(100)
        for d in (11,14,19):
            c=r.certificate(d)
            self.assertLess(c['lower'],lo)
            self.assertGreater(c['upper'],hi)
            self.assertLess(c['upper']-c['center'],c['uniform_error'])

    def test_gaussian_changed_source_matches_prefix(self):
        for d in (1,2,4,7):
            mu=r.moments(2*d+1);p=r.monic_orthogonal(mu,d)
            fake=r.atomic_moments(p,mu,2*d+8)
            self.assertEqual(fake[:2*d],mu[:2*d])
            self.assertNotEqual(fake[2*d],mu[2*d])
            self.assertTrue(all(x>0 for x in fake))
            self.assertTrue(all(a>b for a,b in zip(fake,fake[1:])))

    def test_zero_seed_and_rational_boundary_for_changed_source(self):
        for d in (1,2,3,5):
            mu=r.moments(2*d+1);p=r.monic_orthogonal(mu,d)
            fake=r.atomic_moments(p,mu,40)
            alpha=r.resolvent(mu,d)
            u=Q();tail=alpha
            budget=r.atomic_tail_budget(mu,d)
            total=Q()
            for n,a in enumerate(fake,1):
                u=16*u+a;tail=16*tail-a;total+=tail
                self.assertEqual(u+tail,16**n*alpha)
                self.assertGreater(tail,0)
                self.assertLess(total,budget)

    def test_mutants_have_their_own_certificates(self):
        for c in ((5,-5,0,0),(3,-2,-1,0)):
            for d in (2,4,6):
                cert=r.certificate(d,c)
                partial=sum((r.source(n,c)/16**n for n in range(1,60)),Q())
                upper=partial+r.source(61,c)/(15*16**60)
                self.assertLess(cert['lower'],partial)
                self.assertGreater(cert['upper'],upper)
                self.assertNotEqual(cert['center'],r.certificate(d)['center'])

    def test_finite_atomic_source_is_exact_at_its_rank(self):
        mu=[2*Q(1,3)**j+Q(7,5)*Q(3,5)**j for j in range(6)]
        p=r.monic_orthogonal(mu,2)
        self.assertEqual(r.inner(p,p,mu),0)
        self.assertEqual(r.resolvent(mu,2),Q(2)/(16-Q(1,3))+Q(7,5)/(16-Q(3,5)))
        with self.assertRaises(StopIteration):r.monic_orthogonal(mu,3)

    def test_seed_translation_is_not_source_identification(self):
        alpha=r.certificate(3)['center']
        for seed in (Q(7,11),Q(1,16),Q(-1,256)):
            self.assertEqual((alpha+seed)-alpha,seed)
            for n in (0,1,7,19):
                self.assertEqual(16**n*(alpha+seed)-16**n*alpha,16**n*seed)

    def test_uniform_budget_improves_raw_same_prefix(self):
        for d in range(1,16):
            raw=r.source(2*d+1)/(15*16**(2*d))
            cert=r.certificate(d)
            self.assertLess(cert['upper']-cert['lower'],raw)

    def test_theta_rational_bounds_decrease_in_lattice_cutoff(self):
        for K in (0,1,4):
            for ell in range(4):
                bounds=[r.theta_germ_tail_bound(M,K,ell) for M in range(1,6)]
                self.assertTrue(all(a>b>0 for a,b in zip(bounds,bounds[1:])))

    def test_input_domain_checks(self):
        with self.assertRaises(ValueError):r.source(0)
        with self.assertRaises(ValueError):r.monic_orthogonal(r.moments(3),2)
        with self.assertRaises(ValueError):r.theta_germ_tail_bound(-1,0)

    def test_prime_germ_positive_exact_countermodels(self):
        from math import factorial
        for K in range(1,13):
            rows=r.prime_jet_fake(K)
            self.assertTrue(all(old+change>0 for _,old,change in rows))
            for k in range(K):
                self.assertEqual(sum((change*j**k for j,_,change in rows),Q()),0)
            next_moment=sum((change*j**K for j,_,change in rows),Q())
            epsilon=rows[0][2]
            self.assertEqual(next_moment,epsilon*(-1)**K*factorial(K))
            # At n=2 the divisor identity would require Lambda(2)=log(2).
            self.assertNotEqual(4*(rows[0][1]+rows[0][2]),1)


if __name__=='__main__':unittest.main()
