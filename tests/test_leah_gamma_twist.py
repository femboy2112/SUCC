"""Calibrated exact tests for the centered source-current instrument."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.leah_gamma_twist import (
    centered_path, shell_metrics, shell_antilock_interval, silent_response,
    barycentric_packet,
)
from observational_succ.duck_bbp import forcing, tail_interval
from observational_succ.selected_orbit import SelectedOrbit


class CenteredCurrentTests(unittest.TestCase):
    def test_independent_unwrapped_four_pole_replay(self):
        for seed in (Q(), Q(1,16), Q(1,7), Q(-1,5)):
            path = centered_path(100, seed)
            u, oldj = seed, (seed+Q(1,2)).__floor__()
            for n in range(1,101):
                r = 4*Q(1,8*n-7)-2*Q(1,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
                u = 16*u+r
                j = (u+Q(1,2)).__floor__()
                self.assertEqual(path.residuals[n],u-j)
                self.assertEqual(path.impulses[n],j-16*oldj)
                oldj=j

    def test_selected_orbit_and_rational_alias(self):
        path, alias = centered_path(100), centered_path(100,Q(1,16))
        orbit=SelectedOrbit()
        for n in range(1,101):
            self.assertEqual(path.residuals[n]%1,orbit.state(n))
            self.assertEqual(path.residuals[n],alias.residuals[n])
        self.assertEqual(path.impulses[2:],alias.impulses[2:])
        self.assertNotEqual(path.seed,alias.seed)
        self.assertNotEqual(path.impulses[1],alias.impulses[1])

    def test_bulk_identities_and_endpoint_mutation(self):
        # Arbitrary bounded profiles test actual endpoint algebra, independent
        # of the BBP implementation and including both sharp bulk cases.
        grid=(Q(-1,2),Q(-1,4),Q(),Q(1,4),Q(1,2))
        caught=False
        for v in product(grid,repeat=4):
            e=sum(t*t for t in v[:-1]); delta=v[-1]**2-v[0]**2
            d=sum((16*a-b)**2 for a,b in zip(v,v[1:]))
            minus=sum((a-b)**2 for a,b in zip(v,v[1:]))
            plus=sum((a+b)**2 for a,b in zip(v,v[1:]))
            self.assertEqual(d,225*e+16*minus-15*delta)
            self.assertEqual(d,289*e-16*plus+17*delta)
            self.assertGreaterEqual(d,225*e-Q(15,4))
            self.assertLessEqual(d,289*e+Q(17,4))
            caught |= d!=225*e+16*minus
        self.assertTrue(caught)

    def test_source_correction_and_finite_coercivity(self):
        path=centered_path(200)
        caught=False
        for B in (1,2,3,8,16,37,73,100):
            m=shell_metrics(path,B)
            self.assertLessEqual(m['coercive_lower'],m['innovation_energy'])
            self.assertLessEqual(m['innovation_energy'],m['coercive_upper'])
            delta=Q(15,4*B)+Q(225,4096*B**3)
            self.assertLessEqual(m['integer_energy_error'],delta)
            self.assertLessEqual(abs(m['integer_energy']-m['innovation_energy']),delta)
            self.assertLessEqual(m['impulse_count'],m['integer_energy'])
            self.assertLessEqual(m['integer_energy'],64*m['impulse_count'])
            caught |= m['integer_energy']!=m['innovation_energy']
        self.assertTrue(caught)

    def test_finite_green_response_and_coherent_rational_seed(self):
        H=120
        p=sum((forcing(j)/16**j for j in range(1,H+1)),Q())
        path=centered_path(H,-p)
        self.assertTrue(all(a==0 for a in path.impulses))
        for n in (0,1,8,31,60):
            for L in (0,1,5,13):
                response,boundary=silent_response(path,n,L)
                self.assertEqual(path.residuals[n],response+boundary)
        # Finite coherence has a positive completed tail, not an exact zero seed.
        lo,hi=tail_interval(0,H)
        self.assertEqual(lo,p)
        self.assertGreater(hi-p,0)
        self.assertNotEqual(path.seed,0)

    def test_cosine_transport_and_current_bounds(self):
        path=centered_path(128)
        pi_upper=Q(22,7)
        for B in (8,16,32,64):
            lo,hi=shell_antilock_interval(path,B)
            k=shell_metrics(path,B)['integer_energy']
            delta=Q(15,4*B)+Q(225,4096*B**3)
            lower=Q(8,289*B)*(k-Q(17,4)-delta)-pi_upper/(32*B**2)
            upper=2*pi_upper**2/(225*B)*(k+Q(15,4)+delta)+pi_upper/(32*B**2)
            self.assertLessEqual(lower,lo)
            self.assertLessEqual(hi,upper)
            self.assertGreater(lo,0)

    def test_source_asymptotic_rational_brackets(self):
        for n in range(1,401):
            self.assertGreater(forcing(n),Q(15,64*n*n))
            self.assertLess(forcing(n+1),Q(15,64*n*n))
            lo,hi=tail_interval(n,8)
            self.assertGreaterEqual(n*n*lo,Q(1,64)-Q(1,30*n))
            self.assertLess(n*n*hi,Q(1,64))

    def test_barycentric_signed_response(self):
        from observational_succ.oily_signed_certificate import character_enclosure
        path=centered_path(32)
        for q in (1,2,8,16):
            for h in (1,-1,3,17):
                terms=barycentric_packet(path,16,q,h)
                self.assertEqual(sum(w for w,p in terms),1)
                lo=hi=Q()
                tl=th=Q()
                for w,p in terms:
                    c,_=character_enclosure(p)
                    lo+=w*c.lower; hi+=w*c.upper
                for v in path.residuals[16:32]:
                    c,_=character_enclosure(h*v)
                    tl+=c.lower/16; th+=c.upper/16
                budget=Q(22,7)**2*h*h/(512*q*q)
                self.assertLessEqual(max(abs(lo-th),abs(hi-tl)),budget)

    def test_holographic_ambiguity_overclaim_mutation(self):
        from observational_succ.oily_signed_certificate import character_enclosure
        # h=32,q=1: endpoints have zero gap, interior symmetric pair gap 2.
        response=lambda y: character_enclosure(2*y)[0]
        self.assertEqual(response(Q()).lower,response(Q(1,2)).lower)
        self.assertEqual(response(Q(1)).lower,1)
        self.assertEqual(response(Q(1,4)).upper,-1)
        self.assertEqual(response(Q(3,4)).upper,-1)
        self.assertEqual((Q(1,4)+Q(3,4))/2,Q(1,2))

    def test_domain_guards(self):
        for bad in (-1,True,1.0):
            with self.assertRaises(ValueError): centered_path(bad)
        for bad in (0.1,True,'0'):
            with self.assertRaises(ValueError): centered_path(2,bad)
        with self.assertRaises(ValueError): shell_metrics(centered_path(3),2)
        with self.assertRaises(ValueError): silent_response(centered_path(3),1,4)


if __name__=='__main__': unittest.main()
