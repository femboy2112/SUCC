"""Focused exact tests: no full SUCC CI or zero-seed Weyl theorem claimed."""
import sys
import unittest
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research/2026-10-29/golden_gamma_farey_twist'))
import twist_probe as p

class TestArithmeticRotation(unittest.TestCase):
    def test_matrix_squared(self):
        self.assertEqual(p.matmul(p.D,p.D),((0,-2),(2,0)))
        self.assertEqual(p.det(p.D),2)
        self.assertEqual(p.det(p.A),1)
    def test_primitive_odd_twist(self):
        count=0
        for a in range(-27,28):
            for b in range(-27,28):
                if gcd(a,b)!=1:continue
                count+=1
                self.assertEqual(p.gcd_twist((a,b)),2 if a%2 and b%2 else 1)
        self.assertGreater(count,1800)
    def test_nonprimitive_input_rejected(self):
        with self.assertRaises(ValueError):p.gcd_twist((3,3))
    def test_pure_parity_classes(self):
        classes=[(0,1),(1,0),(1,1)]
        self.assertEqual([p.gcd_twist(v) for v in classes],[1,1,2])
    def test_coprime_transform_group(self):
        for a,b in [(1,0),(0,1),(1,1),(5,8),(-8,13)]:
            self.assertTrue(p.primitive(p.act(p.A,(a,b))))

class TestArithmeticTiling(unittest.TestCase):
    def test_farey_triangle_and_mediant(self):
        a,b=(0,1),(1,1)
        m=p.farey_mediant(a,b)
        self.assertEqual(m,(1,2))
        self.assertTrue(p.farey_neighbor(a,m))
        self.assertTrue(p.farey_neighbor(m,b))
    def test_triangle_transport(self):
        v=[(0,1),(1,1),(1,0)]
        for k in range(1,12):
            v=[p.act(p.A,x) for x in v]
            self.assertTrue(all(p.primitive(x) for x in v))
            self.assertTrue(all(p.farey_neighbor(v[i],v[(i+1)%3]) for i in range(3)))
    def test_rank_positive_totient_cototient(self):
        for q in range(1,75):
            self.assertEqual(p.totient(q)+p.cototient(q),q)
            self.assertGreaterEqual(p.totient(q),1)
            rp,rc=p.ranks((1,q))
            self.assertEqual(rp+rc,q+2)
            self.assertGreaterEqual(min(rp,rc),1)
        self.assertEqual(p.ranks((1,1)),(2,1))
    def test_totient_reference(self):
        self.assertEqual([p.totient(q) for q in [1,2,3,4,5,6,8,9,10,12]],[1,1,2,2,4,2,4,6,4,4])
    def test_farey_mutation_rejected(self):
        with self.assertRaises(ValueError):p.farey_mediant((1,2),(1,4))
    def test_edge_beta_gluing(self):
        for a,b in [(2,1),(3,5),(7,3),(1,1)]:
            for k in range(1,6):
                edge=p.beta_edge_moment(a,b,k)
                self.assertEqual(edge,Q(p.rising(a,k),p.rising(a+b,k)))
                # Third Gamma shape does not affect the normalized edge ratio.
                for third in (1,2,19):
                    self.assertEqual(edge,p.beta_edge_moment(a,b,k))
                    # Dirichlet faces themselves do change with the third rank.
                    self.assertEqual(sum(p.dirichlet_moment((a,b,third),tuple(int(i==j) for i in range(3))) for j in range(3)),1)
    def test_beta_invalid(self):
        with self.assertRaises(ValueError):p.beta_edge_moment(0,2,1)
    def test_gamma_harmonic_jet(self):
        self.assertEqual(p.gamma_rank_harmonic(2),Q(1))
        self.assertEqual(p.gamma_rank_harmonic(4),Q(11,6))
        with self.assertRaises(ValueError):p.gamma_rank_harmonic(0)

class TestOilyMobius(unittest.TestCase):
    def test_mobius_values(self):
        self.assertEqual([p.mobius(i) for i in range(1,11)],[1,-1,-1,0,-1,1,-1,0,0,1])
    def test_tight_defect_interval(self):
        a,b=p.deficit_interval(21)
        self.assertLess(b-a,Q(1,10**10))
        self.assertTrue(a<Q(106819927058651,10**15)<b)
    def test_defect_intervals_nested(self):
        for n in [3,5,7,9,11,13]:
            lo,hi=p.deficit_interval(n)
            lo2,hi2=p.deficit_interval(n+2)
            self.assertLess(lo,hi)
            self.assertLessEqual(lo,lo2)
            self.assertLessEqual(hi2,hi)
    def test_probability_bruteforce_controls(self):
        # Directly enumerate original two-channel geometric packet probability.
        total=Q(0); lost=Q(0)
        N=17
        for k in range(N):
            for j in range(N):
                m=Q(1,2**(k+j+2))
                if gcd(k,j)==1:
                    total+=m
                    if k%2 and j%2:lost+=m
        a,b=p.deficit_interval(23)
        self.assertLess(lost,b)
        self.assertLess(a-lost,Q(1,2**(N-3)))
        self.assertLess(lost,total)
    def test_primitive_probability_bounds(self):
        lo,hi=p.primitive_pair_interval(40)
        self.assertTrue(lo<Q(466907700496,10**12)<hi)
        defect_lo,defect_hi=p.deficit_interval(25)
        self.assertLess(defect_hi,lo)
    def test_totient_heat_exact_coefficients(self):
        for n in range(1,160):
            self.assertEqual(p.twist_totient_coeff(n),p.twist_coeff_by_mobius(n))
            self.assertEqual(p.twist_totient_coeff(n),p.totient(n)*(2 if n%2==0 else 1))
    def test_independent_positive_heat_certificate(self):
        for N in [3,7,11,17,25]:
            a,b=p.totient_heat_interval(N)
            c,d=p.deficit_interval(N)
            self.assertLess(a,d)
            self.assertGreater(b,c)
            self.assertLessEqual(b-a,Q(1,1))
        x,y=p.totient_heat_interval(30)
        self.assertLess(y-x,Q(1,10**15))
    def test_heat_coefficient_rejects_primitive_mutation(self):
        self.assertEqual(p.twist_totient_coeff(5),4)
        self.assertEqual(p.twist_totient_coeff(6),4)
        self.assertNotEqual(p.twist_totient_coeff(6),p.totient(6))
    def test_tail_bound_rejects_mutation(self):
        self.assertGreater(p.deficit_term(1),0)
        self.assertLess(p.deficit_term(3),0)
        self.assertLess(p.deficit_term(5),0)

class TestOriginalArithmetic(unittest.TestCase):
    def test_exact_forcing_four_poles(self):
        self.assertEqual(p.fourpole_forcing(1),Q(47,15))
        self.assertEqual(p.fourpole_forcing(2),Q(106,819))
    def test_literal_zero_seed_prefix(self):
        orbit=p.zero_seed_orbit(6)
        self.assertEqual(orbit[0],0)
        self.assertEqual([p.literal_carry(t)%16 for t in orbit[1:3]],[3,2])
    def test_orbit_recurrence(self):
        orbit=p.zero_seed_orbit(12)
        for t in range(1,13):self.assertEqual(orbit[t],16*orbit[t-1]+p.fourpole_forcing(t))
    def test_eisenstein_positive_nonzero_spectral_coefficients(self):
        vals=[p.discrete_eisenstein_harness(k,1.0) for k in range(1,12)]
        self.assertTrue(all(z>0 for z in vals))
        self.assertTrue(all(a>b for a,b in zip(vals,vals[1:])))
        self.assertAlmostEqual(vals[0],0.019739290926850938,places=14)
    def test_sigma_divisor(self):
        self.assertEqual(p.eisenstein_sigma_minus3(1),1)
        self.assertEqual(p.eisenstein_sigma_minus3(2),Q(9,8))
        self.assertEqual(p.eisenstein_sigma_minus3(6),Q(1)+Q(1,8)+Q(1,27)+Q(1,216))
        with self.assertRaises(ValueError):p.eisenstein_sigma_minus3(0)

if __name__=='__main__':unittest.main()
