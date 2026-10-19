"""Independent finite calibrations and fresh authentic source holdouts."""
from fractions import Fraction as F
import json
from pathlib import Path
import unittest
from observational_succ import directional_source_inverse as S


class DirectionalInverseTheorem(unittest.TestCase):
    def test_full_auxiliary_basis_recovers_exact_inverse(self):
        for D in (((F(2),F(0)),(F(0),F(5))),((F(3),F(1)),(F(1),F(4)))):
            k=F(1);I=((F(1),F(0)),(F(0),F(1)))
            C=tuple(tuple(D[i][j]-I[i][j]for j in range(2))for i in range(2))
            Csquared=S.multiply(C,C)
            K=tuple(tuple(k*C[i][j]+Csquared[i][j]for j in range(2))for i in range(2))
            result=S.inverse_correction_lower(K,C,((F(),F()),(F(),F())),k)
            upper=tuple(tuple(I[i][j]-result['correction_lower'][i][j]for j in range(2))for i in range(2))
            self.assertEqual(upper,S.inverse2(D))
            self.assertTrue(result['whole_correction_PSD'])

    def test_low_high_trial_residual_identity_exact(self):
        # A scalar low block, a coupled two-dimensional true high operator.
        D=((F(3),F(1)),(F(1),F(4)));B=(F(2),F(-1));A=F(7)
        inv=S.inverse2(D)
        genuine=A-S.quadratic(inv,B)
        for U in ((F(0),F(0)),(F(2,3),F(-5,7)),(F(-3),F(4))):
            DU=tuple(sum((D[i][j]*U[j]for j in range(2)),F())for i in range(2))
            r=tuple(B[i]-DU[i]for i in range(2))
            trial=A-2*sum((B[i]*U[i]for i in range(2)),F())+S.quadratic(D,U)
            self.assertEqual(trial-S.quadratic(inv,r),genuine)

    def test_finite_positive_compression_cannot_replace_global_gap(self):
        D=((F(2),F(9,5)),(F(9,5),F(2)))
        # The sampled e1 energy is 2>kappa=1 and D itself is positive.
        self.assertTrue(S.psd2(D));self.assertGreater(D[0][0],1)
        # Yet kappa=1 is a false all-high lower; its inverse bound fails.
        self.assertGreater(S.inverse2(D)[1][1],1)

    def test_interval_correction_contains_every_corner_mutant(self):
        K=((F(3),F(1)),(F(1),F(4)))
        V=((F(2),F(1)),(F(1),F(3)));e=F(1,100)
        rad=((e,e),(e,e));lower=S.inverse_correction_lower(K,V,rad,F(1))['correction_lower']
        import itertools
        for signs in itertools.product((-1,1),repeat=4):
            v=tuple(tuple(V[i][j]+signs[2*i+j]*e for j in range(2))for i in range(2))
            true=S.multiply(S.transpose(v),S.multiply(S.inverse2(K),v))
            difference=tuple(tuple(true[i][j]-lower[i][j]for j in range(2))for i in range(2))
            self.assertTrue(S.psd2(difference))

    def test_completion_of_square_excludes_all_response_coefficients(self):
        zero=(F(),F());T=((F(1),F()),(F(),F(1)));M=((F(2),F()),(F(),F(2)))
        K=((F(1),F()),(F(),F(1)));V=((F(1,10),F()),(F(),F(1,10)))
        enclosures=lambda a:tuple(tuple((x,x)for x in row)for row in a)
        out=S.finite_family_obstruction_from_intervals(*map(enclosures,(T,M,K,V)),F(1),(F(1),F(0)))
        self.assertEqual(out['family_upper_bound'],F(-99,100))
        self.assertTrue(out['all_response_matrices_X_excluded'])
        self.assertFalse(out['genuine_source_negative'])
        # An affirmative control prevents a checker that rejects every family.
        out=S.finite_family_obstruction_from_intervals(enclosures(M),enclosures(T),enclosures(K),enclosures(V),F(1),(F(1),F(0)))
        self.assertFalse(out['strict_obstruction'])

    def test_negative_gram_cannot_fake_all_positive_young_obstruction(self):
        # Hostile arithmetic audit's exact counterexample: cap=-I, but
        # eta=2, X=0, P=0 gives L=I because M=-I is NOT a residual Gram.
        I=((F(1),F()),(F(),F(1)))
        T=tuple(tuple(-2*x for x in row)for row in I)
        M=tuple(tuple(-x for x in row)for row in I)
        V=((F(),F()),(F(),F()))
        enclosures=lambda a:tuple(tuple((x,x)for x in row)for row in a)
        self.assertEqual(T[0][0]-3*M[0][0],1)
        with self.assertRaisesRegex(S.DirectionalSourceError,'Gram M>=0'):
            S.finite_family_obstruction_from_intervals(
                *map(enclosures,(T,M,I,V)),F(1),(F(1),F(0)))
        # A genuine semidefinite zero Gram remains admissible.
        result=S.finite_family_obstruction_from_intervals(
            *map(enclosures,(T,V,I,V)),F(1),(F(1),F(0)))
        self.assertTrue(result['strict_obstruction'])

    def test_declared_domains_fail_closed(self):
        for x in (True,1.5,'2'):
            with self.assertRaises(S.DirectionalSourceError):S.exact(x)
        with self.assertRaises(S.DirectionalSourceError):S.inverse2(((1,2),(2,1)))
        with self.assertRaises(S.DirectionalSourceError):S.directional_original_trial(J=0)
        with self.assertRaises(S.DirectionalSourceError):S.directional_original_trial(J=12,sealed_parent=True)
        with self.assertRaises(S.DirectionalSourceError):S.sharp_parent_tail((F(1),),24)

    def test_compact_authentic_all_response_witnesses_and_tampering(self):
        from scripts.directional_source_inverse_probe import verify_compact
        path=Path(__file__).resolve().parents[1]/'research/2026-10-19/DIRECTIONAL_INVERSE_RECEIPT.json'
        data=json.loads(path.read_text())
        checked=verify_compact(data)
        self.assertTrue(all(checked.values()))
        self.assertEqual(len(checked),2)
        self.assertTrue(all(len(b['independent_all_response_obstructions'])==4
                            for b in data['blocks'].values()))
        import copy
        mutant=copy.deepcopy(data)
        first=next(iter(mutant['blocks'].values()))
        first['independent_all_response_obstructions'][0]['family_upper_bound']='1'
        with self.assertRaises(ValueError):verify_compact(mutant)
        mutant=copy.deepcopy(data);mutant['RH_proved']=True
        with self.assertRaises(ValueError):verify_compact(mutant)
        mutant=copy.deepcopy(data);mutant['raw_archive']['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'SHA256'):verify_compact(mutant)
        mutant=copy.deepcopy(data);del mutant['raw_archive']
        with self.assertRaisesRegex(ValueError,'archive provenance'):verify_compact(mutant)

    def test_fresh_source_depth_directions_and_contact_mutant(self):
        result=S.fresh_source_direction_holdout()
        self.assertEqual(result['source_blob'],S.SOURCE_BLOB)
        for row in result['fresh_unfitted_direction_checks']:
            self.assertTrue(row['enclosures_intersect'])
            self.assertTrue(row['wrong_contact_mutant_disjoint'])
            self.assertEqual(row['levels'],(3,4))
        self.assertFalse(result['RH_proved'])


if __name__=='__main__':unittest.main()
