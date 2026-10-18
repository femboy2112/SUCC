"""Independent prime-tree counting, Tate ideles, and Connes local half-density tests."""
import unittest
from fractions import Fraction as Q

from observational_succ.radial_projective_trace_bridge import (
    RadialTraceError, sphere_size, radial_squared_amplitude,
    radial_adjacency_coeff_square, radial_boundary_defect,
    tree_adjacency_sign_transport, independent_three_route_prime_jet,
    independent_ball_sphere_oracle, rooted_ball_vertices,
    classical_tate_positive_euler_crosscheck,
)


class PrimeTreeRadialTraceTests(unittest.TestCase):
    def test_bruteforce_tree_ball_spheres_independently(self):
        for p,depth in ((2,5),(3,4),(5,3)):
            rec=independent_ball_sphere_oracle(p,depth)
            self.assertTrue(rec['source_tree_counts_match'])
            self.assertFalse(rec['infinite_tree_constructed_by_finite_run'])
            self.assertEqual(rec['brute_spheres'][0],1)
            self.assertEqual(rec['brute_spheres'][1],p+1)
            for k in range(2,depth+1):
                self.assertEqual(rec['brute_spheres'][k],p*rec['brute_spheres'][k-1])

    def test_actual_combinatorial_adjacency_against_radial_coefficient(self):
        # Brute tree, not merely invoking sphere-size closed formula.
        for p in (2,3):
            layers=rooted_ball_vertices(p,4)
            for k in (1,2,3):
                layer_set=set(layers[k])
                lower=layers[k-1]
                higher=layers[k+1]
                descendants={child[:-1]:0 for child in layer_set}
                for child in layer_set:
                    descendants[child[:-1]]+=1
                if k==1:
                    self.assertEqual(descendants[layers[0][0]],p+1)
                else:
                    self.assertTrue(all(descendants[v]==p for v in lower))
                self.assertTrue(all(v[:-1] in layer_set for v in higher))
                self.assertEqual(radial_adjacency_coeff_square(p,k-1,k),
                                 (p+1 if k==1 else p))

    def test_p_plus_one_normalized_nonbacktracking_shell_matches_powers(self):
        for p in (2,3,5,7,11):
            for k in (1,2,3,4,5,6):
                rec=radial_squared_amplitude(p,k)
                self.assertEqual(rec['sphere_cardinality'],(p+1)*p**(k-1))
                self.assertEqual(rec['normalized_amplitude_squared'],Q(1,p**k))
                self.assertEqual(rec['inverse_sphere_amplitude_squared'],Q(1,(p+1)*p**(k-1)))
                self.assertFalse(rec['full_Connes_trace_obtained'])
            self.assertEqual(sphere_size(p,0),1)

    def test_exact_triple_radial_connes_tate_one_place(self):
        for p in (2,3,5,7):
            for k in (1,2,3,4):
                r=independent_three_route_prime_jet(p,k,epoch=2)
                self.assertTrue(r['exact_local_three_route_agreement'])
                self.assertEqual(r['BT_radial_squared'],Q(1,p**k))
                self.assertEqual(r['Tate_single_place_idele_norm'],Q(1,p**k))
                self.assertEqual(r['Connes_off_identity_half_density_squared'],Q(1,p**k))
                self.assertFalse(r['Weil_sign_proved'])

    def test_genuine_PGL2_radial_boundary_defect_is_signed(self):
        for p in (2,3,5,11):
            r=radial_boundary_defect(p)
            self.assertEqual(r['first_radial_coefficient_square'],p+1)
            self.assertEqual(r['all_later_coefficient_squares'],p)
            self.assertEqual(r['squared_weight_mismatch'],1)
            self.assertTrue(r['difference_is_rank_two'])
            self.assertTrue(r['boundary_defect_has_positive_and_negative_directions'])
            self.assertFalse(r['canonical_Connes_identity_contact_identified'])
            for k in (0,1,2,3):
                a=tree_adjacency_sign_transport(p,k)
                self.assertEqual(a['conjugated_edge_sign'],-1)
                self.assertTrue(a['squared_positive_quadratic_invariant'])
                self.assertFalse(a['adjacency_itself_positive_definite'])

    def test_local_Tate_Euler_source_versus_all_negative_twist(self):
        for p in (2,3,5):
            for beta in (2,3,4):
                rec=classical_tate_positive_euler_crosscheck(p,beta)
                self.assertTrue(rec['actual_source_equal_to_positive'])
                self.assertFalse(rec['actual_source_equal_to_negative'])
                self.assertNotEqual(rec['negative_twist_factor'],rec['Tate_actual_local_factor'])

    def test_fake_place_depth_and_source_mutants(self):
        for bad in (1,0,4,6,True,2.4):
            with self.assertRaises(RadialTraceError):
                sphere_size(bad,2)
        for bad in (True,-1,2.4,65):
            with self.assertRaises(RadialTraceError):
                radial_squared_amplitude(2,bad)
        with self.assertRaises(RadialTraceError):
            radial_squared_amplitude(2,0)
        with self.assertRaises(RadialTraceError):
            rooted_ball_vertices(7,3)
        with self.assertRaises(RadialTraceError):
            independent_three_route_prime_jet(2,1,source_id="")
        with self.assertRaises(RadialTraceError):
            independent_three_route_prime_jet(2,1,epoch=True)
        with self.assertRaises(RadialTraceError):
            classical_tate_positive_euler_crosscheck(2,1)


if __name__=="__main__":
    unittest.main()
