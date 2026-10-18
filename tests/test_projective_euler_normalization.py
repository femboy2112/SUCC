"""Exact projective p+1 Euler normalization, source and phase hostile controls."""
import unittest
from fractions import Fraction as Q
from itertools import combinations

from observational_succ.projective_euler_normalization import (
    ProjectiveEulerError, OrientedPrime, ProjectiveCylinder, projective_line,
    projective_orientation_mutation, local_euler_identity,
)
from observational_succ.multiplicative_orientation_gram import (
    mobius_euler_vacuum_certificate,
)


class ProjectiveEulerNormalizationTests(unittest.TestCase):
    def test_projective_line_p_plus_one_independent_count(self):
        for p in (2,3,5,7,11,13):
            observed=projective_line(p)
            brute=set()
            for x in range(p):
                for y in range(p):
                    if (x,y)==(0,0):
                        continue
                    if x:
                        brute.add((1, y * pow(x,-1,p) % p))
                    else:
                        brute.add((0,1))
            self.assertEqual(set(observed),brute)
            self.assertEqual(len(observed),p+1)
            self.assertEqual(sum(int(t==(0,1)) for t in observed),1)

    def test_local_projective_normalization_from_affine_and_boundary(self):
        for p in (2,3,5,7,13):
            state=OrientedPrime(p)
            r=state.receipt()
            self.assertEqual(r['raw_euler_norm_squared'],Q(p+1,p))
            self.assertEqual(r['affine_normalized_amplitude_squared'],Q(p,p+1))
            self.assertEqual(r['boundary_normalized_amplitude_squared'],Q(1,p+1))
            self.assertEqual(r['relative_boundary_over_affine_amplitude_squared'],Q(1,p))
            self.assertEqual(r['boundary_sign'],-1)
            self.assertFalse(r['same_as_archimedean_place'])
            self.assertFalse(r['Connes_trace_proved'])

    def test_finite_mobius_vacuum_cylinder_matches_independent_operator(self):
        for ps in ((2,),(2,3),(2,3,5),(2,3,5,7),(2,3,5,7,11)):
            state=ProjectiveCylinder(tuple(OrientedPrime(p) for p in ps))
            witness=mobius_euler_vacuum_certificate(ps)
            self.assertEqual(state.raw_norm_squared,witness['vacuum_norm_squared'])
            expected=tuple((d,sign,squared/witness['vacuum_norm_squared'])
                           for d,sign,squared in witness['squarefree_vacuum_terms'])
            self.assertEqual(state.squarefree_coefficients(),expected)
            self.assertEqual(sum((v for v,_ in state.distribution().values()),Q(0)),1)
        self.assertEqual(ProjectiveCylinder(tuple(OrientedPrime(p) for p in (2,3,5))).raw_norm_squared,Q(12,5))

    def test_all_cylinder_restrictions_exact(self):
        ps=(2,3,5,7)
        state=ProjectiveCylinder(tuple(OrientedPrime(p) for p in ps))
        for n in range(len(ps)+1):
            for subset in combinations(ps,n):
                r=state.check_consistent_restriction(subset)
                self.assertTrue(r['all_cylinder_masses_match_exactly'])
                self.assertFalse(r['this_proves_analytic_continuation'])
        empty=ProjectiveCylinder(())
        self.assertEqual(empty.distribution(),{(): (Q(1),1)})

    def test_first_two_place_marginals_and_noninteger_typical_carrier(self):
        c=ProjectiveCylinder((OrientedPrime(2),OrientedPrime(3)))
        self.assertEqual(c.distribution(),{
            ():(Q(1,2),1),
            (2,):(Q(1,4),-1),
            (3,):(Q(1,6),-1),
            (2,3):(Q(1,12),1),
        })
        self.assertEqual(c.marginal((2,)),{():Q(2,3),(2,):Q(1,3)})
        self.assertEqual(c.marginal((3,)),{():Q(3,4),(3,):Q(1,4)})

    def test_orientation_sign_mutants_keep_probabilities_but_change_coherence(self):
        for p in (2,3,5):
            r=projective_orientation_mutation(p)
            self.assertTrue(r['same_observational_probabilities'])
            self.assertTrue(r['minus_sign_not_determined_by_p_plus_one'])
            self.assertFalse(r['global_Euler_or_Weil_sign_proved'])
            plus=ProjectiveCylinder((OrientedPrime(p,+1),))
            minus=ProjectiveCylinder((OrientedPrime(p,-1),))
            self.assertEqual(plus.marginal((p,)),minus.marginal((p,)))
            self.assertNotEqual(plus.squarefree_coefficients(),minus.squarefree_coefficients())
            self.assertEqual(plus.raw_norm_squared,minus.raw_norm_squared)

    def test_local_euler_factor_algebra(self):
        for p in (2,3,5,7):
            for s in (1,2,3,4):
                x=local_euler_identity(p,s)
                self.assertTrue(x['same'])
                self.assertEqual(x['lhs'],x['rhs'])
                self.assertTrue(x['global_analytic_residue_not_proved_by_finite_test'])

    def test_negative_source_probes(self):
        for p in (6,4,0,True,Q(3),1.2):
            with self.assertRaises(ProjectiveEulerError):
                OrientedPrime(p)
        for sign in (0,2,True,Q(-1),'minus'):
            with self.assertRaises(ProjectiveEulerError):
                OrientedPrime(3,sign)
        for bad in ('',None,True):
            with self.assertRaises(ProjectiveEulerError):
                OrientedPrime(3,source_id=bad)
        with self.assertRaises(ProjectiveEulerError):
            OrientedPrime(3,epoch=True)
        for ps in ((3,2),(2,2)):
            with self.assertRaises(ProjectiveEulerError):
                ProjectiveCylinder(tuple(OrientedPrime(p) for p in ps))
        with self.assertRaises(ProjectiveEulerError):
            ProjectiveCylinder((OrientedPrime(2,source_id='a'),OrientedPrime(3,source_id='b')))
        with self.assertRaises(ProjectiveEulerError):
            ProjectiveCylinder((OrientedPrime(2,epoch=0),OrientedPrime(3,epoch=1)))
        with self.assertRaises(ProjectiveEulerError):
            ProjectiveCylinder((OrientedPrime(3),None))
        c=ProjectiveCylinder((OrientedPrime(2),OrientedPrime(3)))
        with self.assertRaises(ProjectiveEulerError):
            c.marginal((5,))
        with self.assertRaises(ProjectiveEulerError):
            c.marginal((3,2))
        with self.assertRaises(ProjectiveEulerError):
            local_euler_identity(3,True)


if __name__=='__main__':
    unittest.main()
