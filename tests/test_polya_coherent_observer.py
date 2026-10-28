"""Exact hostile tests for the source-marked lift, independently of SymPy."""
import unittest
from fractions import Fraction as F

from observational_succ.oily_prime_growth_compiler import (
    conditional_split,
    grade_sizebias_ratio,
    naive_polya_amplitude_compression_squared,
    polya_birth,
)
from observational_succ.origin_fiber_arithmetic_observer import d
from observational_succ.polya_coherent_observer import (
    accepted_quadratic,
    distance_from_uniform_ray_squared,
    forbidden_scalar_overlap_squared,
    hahn_eigenvector,
    higher_rank_minimal_environment,
    higher_rank_polya_kernel,
    leakage_quadratic,
    leakage_spectrum,
    minimal_environment_dimension,
    nearest_neighbor_source_flux,
    oily_source_flux,
    polya_coherent_numerator,
    polya_laplacian,
)


class CoherentPolyaTests(unittest.TestCase):
    def test_full_gram_identity_and_original_probability(self):
        for m in range(1, 25):
            b, lap = polya_coherent_numerator(m), polya_laplacian(m)
            for k in range(m):
                # Individual edge norms in the two-dimensional environment.
                stay = F((m-k)**2 + k*(m-k), m*(m+1))
                birth = F((k+1)**2 + (k+1)*(m-k-1), m*(m+1))
                self.assertEqual(birth, polya_birth(m-1, k))
                self.assertEqual(stay + birth, 1)
                for ell in range(m):
                    gram = sum(row[k]*row[ell] for row in b)
                    self.assertEqual(gram + lap[k][ell], m*(m+1) if k == ell else 0)

    def test_uniform_ray_is_exactly_dark_in_auxiliary_channel(self):
        for m in range(1, 40):
            self.assertEqual(leakage_quadratic([1]*m), 0)
            self.assertEqual(accepted_quadratic([1]*m), m)
            self.assertEqual(tuple(sum(row) for row in polya_coherent_numerator(m)),
                             (m,)*(m+1))
            self.assertEqual(naive_polya_amplitude_compression_squared(m-1), F(m,m+1))

    def test_complete_spectrum_with_independent_hahn_vectors(self):
        for m in range(1, 18):
            lap = polya_laplacian(m)
            for r, eigenvalue in enumerate(leakage_spectrum(m)):
                v = hahn_eigenvector(m,r)
                self.assertEqual(v[0], 1)
                for k,row in enumerate(lap):
                    self.assertEqual(sum((a*z for a,z in zip(row,v)),F(0)), r*(r+1)*v[k])
                self.assertEqual(leakage_quadratic(v), eigenvalue*sum(z*z for z in v))

    def test_sharp_gap_and_maximum_controls(self):
        for m in range(2, 21):
            for r in (1,m-1):
                v = hahn_eigenvector(m,r)
                deviation = distance_from_uniform_ray_squared(v)
                self.assertGreater(deviation,0)
                self.assertEqual(leakage_quadratic(v)/deviation, F(r*(r+1),m*(m+1)))
            for seed in range(7):
                v = [F(((k+2)*(seed+3)) % 11 - 5,k+1) for k in range(m)]
                deviation = distance_from_uniform_ray_squared(v)
                loss = leakage_quadratic(v)
                self.assertGreaterEqual(loss,F(2,m*(m+1))*deviation)
                self.assertLessEqual(loss,F(m-1,m+1)*deviation)
                self.assertEqual(loss+accepted_quadratic(v),sum(z*z for z in v))

    def test_no_scalar_edge_phase_can_fix_isometry(self):
        self.assertEqual(minimal_environment_dimension(1),1)
        for m in range(2,35):
            self.assertEqual(minimal_environment_dimension(m),2)
            for k in range(m-1):
                self.assertGreater(forbidden_scalar_overlap_squared(m,k),0)

    def test_full_x_source_covariance_not_uniform_substitution(self):
        for x in (F(1,11),F(1,3),F(2,3),F(9,10),F(1)):
            for j in range(12):
                rows = oily_source_flux(x,j)
                self.assertEqual(sum(t for _,_,t in rows),1)
                for ell,(stay,birth,target) in enumerate(rows):
                    self.assertEqual(target,conditional_split(x,j+1,ell))
                    # Squared row-component norms; the separate radical oracle
                    # constructs amplitudes and checks actual orthogonality.
                    self.assertEqual(stay**2+stay*birth,stay*target)
                    self.assertEqual(birth**2+stay*birth,birth*target)
        self.assertNotEqual(oily_source_flux(F(1,3),4),oily_source_flux(F(1),4))

    def test_probability_amplitude_and_primitive_prime_hostile_controls(self):
        for m in range(2,18):
            alternating = [(-1)**k for k in range(m)]
            self.assertGreater(leakage_quadratic(alternating),0)
            self.assertEqual(distance_from_uniform_ray_squared([F(7,15)]*m),0)
        for j in range(1,10):
            self.assertEqual(d(2**j),j+1)
            self.assertEqual(d(6**j),(j+1)**2)
            self.assertNotEqual(d(6**j),j+1)
        self.assertEqual(grade_sizebias_ratio(F(1,2),0),F(1,2))
        self.assertEqual(grade_sizebias_ratio(F(1,2),2),F(3,2))

    def test_higher_rank_source_and_single_overlap_geometry(self):
        for channels in range(2,6):
            for grade in range(5):
                source,target,p = higher_rank_polya_kernel(grade,channels)
                self.assertEqual(max(sum(a>0 for a in row) for row in p),
                                 higher_rank_minimal_environment(grade,channels))
                self.assertTrue(all(sum(row,F(0))/len(source)==F(1,len(target)) for row in p))
                for k in range(len(source)):
                    self.assertEqual(sum(row[k] for row in p),1)
                    for ell in range(k):
                        self.assertLessEqual(sum(row[k]>0 and row[ell]>0 for row in p),1)

    def test_split_dependent_stopping_preserves_terminal_law_countermodel(self):
        # A flow circulation around the first diamond changes hidden paths,
        # restores ALL grade-two arrival masses, and leaves every stop mass.
        root_to_grade_one = (F(5,12),F(1,3))
        self.assertEqual(sum(root_to_grade_one),F(3,4))  # root stop remains 1/4
        flow = ((F(1,6),F(1,8),F(0)),(F(0),F(1,24),F(1,6)))
        terminal = (F(1,8),F(1,8))
        self.assertEqual(tuple(terminal[k]+sum(flow[k]) for k in range(2)),
                         root_to_grade_one)
        self.assertEqual(tuple(sum(flow[k][ell] for k in range(2)) for ell in range(3)),
                         (F(1,6),)*3)
        hazards=tuple(terminal[k]/root_to_grade_one[k] for k in range(2))
        self.assertEqual(hazards,(F(3,10),F(3,8)))
        self.assertNotEqual(hazards[0],hazards[1])
        self.assertNotEqual(root_to_grade_one,(F(3,8),)*2)

    def test_invalid_and_degenerate_inputs_are_rejected(self):
        for bad in (0,-1,True,F(2),2.0):
            with self.assertRaises(ValueError): polya_laplacian(bad)
        with self.assertRaises(ValueError): nearest_neighbor_source_flux([F(1,2)],[F(1,2)])
        with self.assertRaises(ValueError): nearest_neighbor_source_flux([1],[0])
        with self.assertRaises(ValueError): oily_source_flux(0,0)
        with self.assertRaises(TypeError): leakage_quadratic([0.5])
        with self.assertRaises(ValueError): hahn_eigenvector(3,3)
        with self.assertRaises(ValueError): forbidden_scalar_overlap_squared(1,0)


if __name__ == '__main__':
    unittest.main()
