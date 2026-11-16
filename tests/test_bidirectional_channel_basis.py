"""Exact hostile and positive controls for two-root observational basis model."""
import itertools
import unittest
from fractions import Fraction

from observational_succ.bidirectional_channel_basis import (
    Channel, HyperCoupling, LaggedForces, Quantity, Unit,
    aphex_style_update, certificate_constant_phase,
    global_fourier_second_moment, observation_rank,
    parity_states, selected_orbit_phase, walsh_coefficients, walsh_inverse_at,
)
from observational_succ.arity_four_bridge import bbp_residue_prefix


class TypedChannelTests(unittest.TestCase):
    def test_units_free_abelian(self):
        m,t,v = (Unit.generator(z) for z in ("mass", "time", "velocity"))
        self.assertEqual((m*t / m),t)
        self.assertEqual(m**-1 * m,Unit())
        self.assertEqual(Unit((("mass", 2), ("time", -1), ("mass", -1))),m/t)
        self.assertEqual(Quantity(2,m)*Quantity(3,t),Quantity(6,m*t))
        with self.assertRaises(TypeError): _ = Quantity(1,m)+Quantity(1,t)
        with self.assertRaises(ValueError): Unit((("",1),))
        with self.assertRaises(TypeError): _ = t**Fraction(1,2)

    def test_hyperedge_units_not_merely_pairwise(self):
        a,b,c,out = (Unit.generator(z) for z in ("A","B","C","O"))
        channels = {k:Channel(k,u) for k,u in (("a",a),("b",b),("c",c),("o",out))}
        x = {k:Quantity(v,channels[k].unit) for k,v in (("a",2),("b",3),("c",5))}
        e = HyperCoupling(("a","b","c"),"o",Quantity(Fraction(1,7),out/(a*b*c)))
        self.assertEqual(e.evaluate(channels,x),Quantity(Fraction(30,7),out))
        with self.assertRaises(TypeError): HyperCoupling(("a","b","c"),"o",Quantity(1,Unit())).evaluate(channels,x)
        with self.assertRaises(ValueError): HyperCoupling(("a","a"),"o",Quantity(1,Unit())).evaluate(channels,x)
        with self.assertRaises(TypeError): e.evaluate(channels,dict(x,b=Quantity(3,a)))

    def test_observation_independence_relative_to_arity(self):
        self.assertEqual(observation_rank([[1,0,0],[0,1,0],[0,0,1]]),3)
        self.assertEqual(observation_rank([[1,0,1],[0,1,1],[1,1,2]]),2)
        self.assertEqual(observation_rank([[1,2],[1,3],[5,8]]),2)
        self.assertEqual(observation_rank([]),0)
        with self.assertRaises(ValueError): observation_rank([[1,2],[1]])
        with self.assertRaises(ValueError): Channel("",Unit())
        with self.assertRaises(ValueError): Channel("x",Unit(),(1,-1,0))


class WalshInteractionTests(unittest.TestCase):
    def test_two_indistinguishable_pairwise_models(self):
        evens=parity_states(3,+1)
        odds=parity_states(3,-1)
        self.assertEqual(len(evens),len(odds))
        w_even=walsh_coefficients(evens)
        w_odd=walsh_coefficients(odds)
        for subset in w_even:
            if len(subset)<3:
                self.assertEqual(w_even[subset],w_odd[subset])
            else:
                self.assertEqual(w_even[subset],-w_odd[subset])
                self.assertEqual(w_even[subset],1)
        self.assertEqual(walsh_inverse_at(w_even,(1,1,1)),Fraction(1,4))
        self.assertEqual(walsh_inverse_at(w_odd,(1,1,1)),0)
        self.assertEqual(walsh_inverse_at(w_even,(-1,1,1)),0)

    def test_all_N_parity_obstruction_and_inversion(self):
        for d in range(1,7):
            for p in (-1,+1):
                rows=parity_states(d,p)
                coefficients=walsh_coefficients(rows)
                self.assertEqual(coefficients[tuple(range(d))],p)
                self.assertEqual(coefficients[()],1)
                for s in coefficients:
                    if 0<len(s)<d:
                        self.assertEqual(coefficients[s],0)
                for point in itertools.product((-1,1),repeat=d):
                    self.assertEqual(walsh_inverse_at(coefficients,point),
                                     Fraction(1,2**(d-1)) if __import__('math').prod(point)==p else 0)
        with self.assertRaises(ValueError): walsh_coefficients([])
        with self.assertRaises(ValueError): walsh_coefficients([[1,1],[-1]])
        with self.assertRaises(ValueError): walsh_inverse_at({():Fraction(1)},(1,1))


class TwoRootTests(unittest.TestCase):
    def test_global_haar_zero_frequency_orthogonality(self):
        for b in (2,3,16):
            for h in (-7,-1,1,4,11):
                for n in range(1,16):
                    self.assertEqual(global_fourier_second_moment(b,h,n),Fraction(1,n))
            self.assertEqual(global_fourier_second_moment(b,0,5),1)
        with self.assertRaises(ValueError): global_fourier_second_moment(1,1,5)

    def test_selected_non_normal_in_global_haar_zero_exception(self):
        for b in (2,3,16):
            n=16
            # 0 is selected, nonnormal, and has W_(N,h)=1 identically.
            self.assertTrue(certificate_constant_phase(selected_orbit_phase(b,0,n),1))
            # Nonzero rational fixed point: T(1/(b-1))=1/(b-1).
            self.assertTrue(certificate_constant_phase(selected_orbit_phase(b,Fraction(1,b-1),n),1))
            self.assertEqual(global_fourier_second_moment(b,1,n),Fraction(1,n))
        with self.assertRaises(ValueError): selected_orbit_phase(16,0,0)
        self.assertFalse(certificate_constant_phase((0,Fraction(1,3)),1))
        self.assertTrue(certificate_constant_phase((0,Fraction(1,3)),3))
        self.assertTrue(certificate_constant_phase((0,Fraction(1,3)),0))

    def test_actual_source_phase_alias_not_source_identity(self):
        z=bbp_residue_prefix(16,0)
        r=bbp_residue_prefix(16,Fraction(1,16))
        self.assertNotEqual(z[0],r[0])
        self.assertEqual(z[1:],r[1:])
        self.assertFalse(certificate_constant_phase(z,1))
        self.assertFalse(certificate_constant_phase(r,1))


class AphexControlTests(unittest.TestCase):
    def test_typed_lagged_force_update(self):
        mass,time,force = (Unit.generator(k) for k in ("mass","time","force"))
        inverse_mass=mass**-1
        dunit=time
        alpha=Quantity(Fraction(1,10),inverse_mass/(dunit*force))
        terms=(LaggedForces(Quantity(2,dunit),(Quantity(3,force),Quantity(-1,force)),Quantity(4,force)),
               LaggedForces(Quantity(5,dunit),(Quantity(-2,force),),Quantity(1,force)))
        self.assertEqual(aphex_style_update(alpha,terms,inverse_mass), Quantity(Fraction(-7,10),inverse_mass))
        with self.assertRaises(TypeError):
            aphex_style_update(alpha,(LaggedForces(Quantity(2,dunit),(Quantity(1,time),),Quantity(1,force)),),inverse_mass)
        with self.assertRaises(TypeError):
            aphex_style_update(Quantity(1,Unit()),terms,inverse_mass)
        with self.assertRaises(ValueError): aphex_style_update(alpha,[],inverse_mass)

    def test_no_provenance_from_matching_pairwise_force_syntax(self):
        # Two source models agree on every scalar/pair moment; an update using
        # only those moments gives the same result, despite different 3-body law.
        evens=walsh_coefficients(parity_states(3,+1))
        odds=walsh_coefficients(parity_states(3,-1))
        pair_features=[(),(0,),(1,),(2,),(0,1),(0,2),(1,2)]
        self.assertEqual([evens[s] for s in pair_features],[odds[s] for s in pair_features])
        self.assertNotEqual(evens[(0,1,2)],odds[(0,1,2)])


if __name__ == '__main__':
    unittest.main()

class FiniteInfiniteNoncommutingLimitTests(unittest.TestCase):
    def test_exact_alias_energy_all_small_sizes(self):
        from observational_succ.bidirectional_channel_basis import (
            finite_grid_fourier_second_moment, grid_alias_closed_form)
        for b in (2,3,4,16):
            for h in (-1,1,5,7):
                if __import__('math').gcd(h,b) !=1:
                    continue
                for n in range(1,15):
                    for k in range(0,8):
                        self.assertEqual(finite_grid_fourier_second_moment(b,h,n,k),
                                         grid_alias_closed_form(b,h,n,k))
        self.assertEqual(finite_grid_fourier_second_moment(16,1,6,3),Fraction(3+9,36))
        self.assertEqual(finite_grid_fourier_second_moment(16,1,6,6),Fraction(1,6))
        self.assertEqual(finite_grid_fourier_second_moment(16,1,6,0),1)
        with self.assertRaises(ValueError): grid_alias_closed_form(16,16,5,6)

    def test_noncommuting_observer_limits_exact_witness(self):
        from observational_succ.bidirectional_channel_basis import finite_grid_fourier_second_moment
        # Fixed finite K=2, temporal length N increases => tends to 1,
        # whereas first increasing K>=N gives exact 1/N => tends to 0.
        for n in (4,8,16,32):
            source_grid = finite_grid_fourier_second_moment(16,1,n,2)
            high_grid = finite_grid_fourier_second_moment(16,1,n,n)
            self.assertEqual(source_grid,Fraction(2+(n-2)**2,n*n))
            self.assertEqual(high_grid,Fraction(1,n))
        self.assertGreater(finite_grid_fourier_second_moment(16,1,32,2),Fraction(3,4))
        self.assertLess(finite_grid_fourier_second_moment(16,1,32,32),Fraction(1,20))

class SourceLockedGridTests(unittest.TestCase):
    def test_grid_partition_on_authentic_bbp_rational_carrier(self):
        from observational_succ.bidirectional_channel_basis import (
            seed_grid_energy_formal, seed_grid_energy_shell_form)
        for B in (2,3,5,7):
            source = bbp_residue_prefix(2*B, 0)
            block = {n:source[n] for n in range(B,2*B)}
            selected = seed_grid_energy_formal(block,16,1,0)
            # Source-selected signed energy retained, no cancellation assumed.
            self.assertEqual(seed_grid_energy_formal(block,16,1,B),selected)
            self.assertEqual(seed_grid_energy_formal(block,16,1,2*B),{Fraction(0):B})
            for K in range(B,2*B+1):
                early,late = seed_grid_energy_shell_form(16,1,B,B,K)
                high = {n:source[n] for n in late}
                composite = {Fraction(0):early}
                if high:
                    for exponent,coeff in seed_grid_energy_formal(high,16,1,0).items():
                        composite[exponent] = composite.get(exponent,0)+coeff
                composite = {x:c for x,c in composite.items() if c}
                self.assertEqual(seed_grid_energy_formal(block,16,1,K),composite)
        with self.assertRaises(ValueError): seed_grid_energy_shell_form(16,16,2,3,2)

    def test_alias_and_null_same_positive_gram_but_not_identical_source(self):
        from observational_succ.bidirectional_channel_basis import seed_grid_energy_formal
        for B in (2,3,5):
            a = bbp_residue_prefix(2*B, 0)
            b = bbp_residue_prefix(2*B, Fraction(1,16))
            self.assertEqual(a[B:2*B],b[B:2*B])
            for K in (0,B,2*B):
                self.assertEqual(seed_grid_energy_formal({n:a[n] for n in range(B,2*B)},16,1,K),
                                 seed_grid_energy_formal({n:b[n] for n in range(B,2*B)},16,1,K))
        null = {n:Fraction(0) for n in range(3,9)}
        self.assertEqual(seed_grid_energy_formal(null,16,1,3),{Fraction(0):36})
        self.assertEqual(seed_grid_energy_formal(null,16,1,9),{Fraction(0):6})
