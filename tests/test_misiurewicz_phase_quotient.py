"""Hostile exact postcritical Markov core, entropy and phase quotient tests."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from random import Random
import unittest

from observational_succ.logistic_observer_tree import Source
from observational_succ.misiurewicz_phase_quotient import (
    MisiurewiczError, CubicElement, ONE, ZERO, ALPHA, INV_ALPHA,
    CRITICAL, MAXIMUM, LOW, FIXED, BOUNDARIES, CELLS, EXPECTED_A,
    PARRY_ROWS, PARRY_PRIOR, cubic_at, isolate_alpha, f,
    postcritical_orbit_certificate, markov_adjacency, phase, legal_path,
    sign_algebraic, compare_algebraic, classify_actual_cell, actual_source_cells,
    path_count, path_entropy_bits, propagate_parry, phase_parry_receipt,
    dual_phase_correlation, alternate_stationary_symbolic_source,
    PhaseReceipt, verify_E_Eprime_phase,
)


def polynomial_independent_remainder(coeffs):
    """Independent monic polynomial long division by x³−2x²−4x−8."""
    vec=[F(c) for c in coeffs]
    while len(vec)>3:
        top=vec[-1]
        k=len(vec)-4
        vec[k]+=8*top
        vec[k+1]+=4*top
        vec[k+2]+=2*top
        vec.pop()
    return tuple(vec+[F(0)]*(3-len(vec)))


class ExactAlgebraTests(unittest.TestCase):
    def test_strict_rational_root_bracket(self):
        lo,hi=isolate_alpha()
        self.assertTrue(F(3)<lo<hi<F(4))
        self.assertTrue(cubic_at(lo)<0<cubic_at(hi))
        self.assertLess(hi-lo,F(1,10**11))

    def test_p_polynomial_has_positive_derivative_for_r_gt_two(self):
        for x in (F(2001,1000),F(5,2),F(3),F(4),F(20)):
            self.assertGreater((3*x+2)*(x-2),0)

    def test_bad_exact_cubic_constructor_rejected(self):
        for wrong in ((),(1,2),(1,2,3,4),[1,2,3],(F(1),1.5,0),(True,0,0)):
            with self.assertRaises(MisiurewiczError):CubicElement(wrong)
        with self.assertRaises(MisiurewiczError):ONE/0
        with self.assertRaises(MisiurewiczError):ONE/0.5
        with self.assertRaises(MisiurewiczError):ONE**(-1)

    def test_exact_minimal_polynomial_zero(self):
        self.assertEqual(ALPHA**3-2*ALPHA**2-4*ALPHA-8,ZERO)
        self.assertEqual(ALPHA*INV_ALPHA,ONE)
        self.assertEqual(INV_ALPHA.as_strings(),('-1/2','-1/4','1/8'))

    def test_algebraic_postcritical_orbit_genuinely_exact(self):
        d=postcritical_orbit_certificate()
        self.assertTrue(d['inverse_alpha_exact'])
        self.assertTrue(d['minimum_polynomial_remainder_zero'])
        self.assertEqual(f(CRITICAL),MAXIMUM)
        self.assertEqual(f(MAXIMUM),LOW)
        self.assertEqual(f(LOW),FIXED)
        self.assertEqual(f(FIXED),FIXED)
        self.assertNotEqual(LOW,FIXED)
        self.assertNotEqual(MAXIMUM,FIXED)

    def test_invariant_interval_and_ordering_certified_from_root_range(self):
        lo,hi=isolate_alpha()
        self.assertTrue(F(1,hi)<F(1,2)<1-F(1,lo))
        self.assertTrue(1-F(1,hi)<lo/4)
        # exact identity (r/4)-(1-1/r)=(r-2)^2/(4r)
        self.assertEqual(MAXIMUM-FIXED,(ALPHA-2)**2*INV_ALPHA/4)

    def test_additive_field_laws(self):
        a=ALPHA+F(2)
        b=ALPHA**2-F(3)
        self.assertEqual(a-b,a+(-b))
        self.assertEqual(3*a+4*a,7*a)
        self.assertEqual(a*ZERO,ZERO)
        self.assertEqual(a*ONE,a)

    def test_seeded_cubic_ring_operations_independent_oracle(self):
        rng=Random(80343)
        for _ in range(240):
            a=tuple(F(rng.randint(-5,5),rng.randint(1,6)) for _ in range(3))
            b=tuple(F(rng.randint(-5,5),rng.randint(1,6)) for _ in range(3))
            aa=CubicElement(a)
            bb=CubicElement(b)
            full=[F(0)]*5
            for i in range(3):
                for j in range(3):
                    full[i+j]+=a[i]*b[j]
            self.assertEqual((aa*bb).coeffs,polynomial_independent_remainder(full))
            self.assertEqual((aa+bb).coeffs,tuple(x+y for x,y in zip(a,b)))

    def test_associative_nontrivial_multiplication(self):
        rng=Random(2462)
        for _ in range(80):
            values=[CubicElement(tuple(F(rng.randint(-3,3)) for _ in range(3)))
                    for _ in range(3)]
            a,b,c=values
            self.assertEqual((a*b)*c,a*(b*c))
            self.assertEqual(a*(b+c),a*b+a*c)

    def test_rigorous_algebraic_signs_without_float_evaluation(self):
        self.assertEqual(sign_algebraic(ZERO),0)
        self.assertEqual(sign_algebraic(ONE),1)
        self.assertEqual(sign_algebraic(-ONE),-1)
        self.assertEqual(compare_algebraic(INV_ALPHA,CRITICAL),-1)
        self.assertEqual(compare_algebraic(CRITICAL,FIXED),-1)
        self.assertEqual(compare_algebraic(FIXED,MAXIMUM),-1)
        self.assertEqual(compare_algebraic(LOW,LOW),0)
        self.assertEqual(compare_algebraic(ALPHA,F(19,5)),-1)

    def test_rigorous_real_source_classification(self):
        self.assertEqual(classify_actual_cell(F(2,5)),0)
        self.assertEqual(classify_actual_cell(F(3,5)),1)
        self.assertEqual(classify_actual_cell(F(4,5)),2)
        for state in BOUNDARIES:
            with self.assertRaises(MisiurewiczError):classify_actual_cell(state)
        for state in (F(0),F(1),F(1,10)):
            with self.assertRaises(MisiurewiczError):classify_actual_cell(state)

    def test_real_sources_are_not_just_abstract_symbol_words(self):
        for x in (F(2,5),F(3,5),F(4,5)):
            cells=actual_source_cells(x,7)
            self.assertEqual(len(cells),8)
            self.assertTrue(legal_path(cells))
            for a,b in zip(cells,cells[1:]):
                self.assertNotEqual(phase(a),phase(b))
        with self.assertRaises(MisiurewiczError):actual_source_cells(CRITICAL,2)

    def test_exact_source_merge_under_real_misiurewicz_parameter(self):
        a=CubicElement.coerce(F(2,5))
        b=CubicElement.coerce(F(3,5))
        self.assertEqual(classify_actual_cell(a),0)
        self.assertEqual(classify_actual_cell(b),1)
        self.assertNotEqual(a,b)
        self.assertEqual(f(a),f(b))
        self.assertEqual(f(a),ALPHA*F(6,25))
        self.assertEqual(classify_actual_cell(f(a)),2)
        self.assertEqual(actual_source_cells(a,5)[1:],actual_source_cells(b,5)[1:])

    def test_rational_mutant_does_not_obey_critical_orbit_identity(self):
        for r in (F(3),F(16,5),F(19,5),F(4)):
            q=r/4
            x2=r*q*(1-q)
            self.assertNotEqual(x2,F(1,r))


class ExactTopologicalMarkovTests(unittest.TestCase):
    def test_true_endpoint_image_derivation(self):
        self.assertEqual(tuple((f(a),f(b)) for a,b in CELLS),
                         ((FIXED,MAXIMUM),(MAXIMUM,FIXED),(FIXED,LOW)))

    def test_exact_markov_graph(self):
        self.assertEqual(markov_adjacency(),EXPECTED_A)
        self.assertEqual(markov_adjacency(),((0,0,1),(0,0,1),(1,1,0)))
        self.assertEqual(sum(sum(row) for row in markov_adjacency()),4)

    def test_char_polynomial_independent_determinants(self):
        # det(lambda I - A) = lambda(lambda²-2), eigenvalues 0,±sqrt(2).
        a=EXPECTED_A
        def determinant3(mat):
            return sum(sign*mat[0][i]*mat[1][j]*mat[2][k]
                       for i,j,k,sign in ((0,1,2,1),(1,2,0,1),(2,0,1,1),
                                           (0,2,1,-1),(1,0,2,-1),(2,1,0,-1)))
        for v in range(-7,8):
            mat=[[v*int(i==j)-a[i][j] for j in range(3)] for i in range(3)]
            self.assertEqual(determinant3(mat),v*(v*v-2))

    def test_every_legal_edge_flips_phase(self):
        for source,row in enumerate(EXPECTED_A):
            for target,allowed in enumerate(row):
                if allowed:
                    self.assertNotEqual(phase(source),phase(target))

    def test_invalid_cell_and_path_controls(self):
        for x in (-1,3,True,F(0),0.0,'A'):
            with self.assertRaises(MisiurewiczError):phase(x)
        with self.assertRaises(MisiurewiczError):legal_path(())
        self.assertFalse(legal_path((0,1)))
        self.assertFalse(legal_path((2,2)))
        self.assertTrue(legal_path((0,2,1,2,0,2)))

    def test_exact_full_branch_second_return(self):
        self.assertEqual([EXPECTED_A[0][2],EXPECTED_A[1][2]], [1,1])
        self.assertEqual(EXPECTED_A[2][:2],(1,1))
        # f²(I0)=f²(I1)=[LOW,FIXED], each monotone onto the full left band.
        for i in (0,1):
            source_range=CELLS[i]
            doubled=(f(f(source_range[0])),f(f(source_range[1])))
            self.assertEqual(set(doubled),{LOW,FIXED})

    def test_paths_exact_enumeration_independent_oracle(self):
        for start in (0,1,2):
            for n in range(12):
                count=0
                for tail in product((0,1,2),repeat=min(n,8)):
                    if n<=8 and legal_path((start,)+tail):
                        count+=1
                if n<=8:
                    self.assertEqual(count,path_count(start,n))
                self.assertEqual(path_count(start,n),1<<path_entropy_bits(start,n))

    def test_exact_entropy_budget_fresh_bit_every_other_step(self):
        for n in range(0,30):
            self.assertEqual(path_entropy_bits(0,n),n//2)
            self.assertEqual(path_entropy_bits(2,n),(n+1)//2)
            self.assertEqual((path_entropy_bits(0,n)+path_entropy_bits(2,n)),n)

    def test_graph_mutation_crosses_phase_law(self):
        # Non-source fake extra A->B edge would make 'phase flips' false.
        mutant=[list(row) for row in EXPECTED_A]
        mutant[0][1]=1
        self.assertTrue(any(phase(i)==phase(j) for i,row in enumerate(mutant)
                            for j,allowed in enumerate(row) if allowed))


class ParrySourceTests(unittest.TestCase):
    def test_source_parry_rows(self):
        self.assertEqual(PARRY_ROWS,({2:F(1)},{2:F(1)},{0:F(1,2),1:F(1,2)}))
        self.assertEqual(PARRY_PRIOR,(F(1,4),F(1,4),F(1,2)))
        for row in PARRY_ROWS:
            self.assertEqual(sum(row.values(),F(0)),1)

    def test_parry_stationarity_exact(self):
        for n in (0,1,2,3,7,14):
            self.assertEqual(propagate_parry(dict(enumerate(PARRY_PRIOR)),n),PARRY_PRIOR)

    def test_coarse_E_period_survives_exact_source_prior_ablation(self):
        # The chosen microscopic symbolic prior is not needed for the phase
        # law. All p in (0,1) retain positive micro metric entropy, although
        # only p=1/2 is the Parry max-entropy source.
        for p in (F(1,5),F(1,3),F(2,5),F(1,2),F(3,4)):
            r=alternate_stationary_symbolic_source(p)
            self.assertEqual(r["stationary_prior"],(p/2,(1-p)/2,F(1,2)))
            self.assertEqual(r["stationary_phase_probabilities"],(F(1,2),F(1,2)))
            self.assertEqual(r["phase_covariance_lag_even"],F(1,4))
            self.assertEqual(r["phase_covariance_lag_odd"],-F(1,4))
            self.assertTrue(r["microscopic_entropy_strictly_positive"])
            self.assertFalse(r["source_law_is_identified_natural_acim"])
        self.assertEqual(alternate_stationary_symbolic_source(F(1,2))["stationary_prior"],PARRY_PRIOR)

    def test_degenerate_symbolic_measure_destroys_metric_entropy_not_topology(self):
        for p in (0,1):
            r=alternate_stationary_symbolic_source(p)
            self.assertFalse(r["microscopic_entropy_strictly_positive"])
            self.assertEqual(r["stationary_phase_probabilities"],(F(1,2),F(1,2)))
            self.assertEqual(r["phase_covariance_lag_even"],F(1,4))
            self.assertEqual(r["phase_covariance_lag_odd"],-F(1,4))
            self.assertEqual(markov_adjacency(),EXPECTED_A)
        for p in (F(-1,100), F(101,100),0.1,True):
            with self.assertRaises(MisiurewiczError):alternate_stationary_symbolic_source(p)

    def test_phase_never_mixes_from_known_start(self):
        for n in range(16):
            left=propagate_parry({0:1},n)
            right=propagate_parry({2:1},n)
            if n%2==0:
                self.assertEqual(sum(left[:2]),1)
                self.assertEqual(right[2],1)
            else:
                self.assertEqual(left[2],1)
                self.assertEqual(sum(right[:2]),1)

    def test_two_step_ranks_and_paths(self):
        self.assertEqual(propagate_parry({0:1},2),(F(1,2),F(1,2),F(0)))
        self.assertEqual(propagate_parry({1:1},2),(F(1,2),F(1,2),F(0)))
        self.assertEqual(propagate_parry({2:1},2),(F(0),F(0),F(1)))
        self.assertNotEqual(propagate_parry({0:1},19),PARRY_PRIOR)

    def test_relative_entropy_versus_phase_zero_entropy(self):
        receipt=phase_parry_receipt(14)
        self.assertEqual(receipt['expected_fresh_symbol_bits_per_step'],F(1,2))
        self.assertEqual(receipt['coarse_phase_entropy_rate_bits'],0)
        self.assertEqual(receipt['stationary_phase_masses'],(F(1,2),F(1,2)))
        self.assertTrue(receipt['phase_alternates_for_every_legal_nondisputed_path'])

    def test_bad_parry_priors_are_rejected(self):
        for law in ({}, {3:1}, {0:F(1,2)}, {0:-1,1:2}, {0:1.0},{True:F(1)}):
            with self.assertRaises(MisiurewiczError):propagate_parry(law,3)
        for time in (-1,1001,1.5,True):
            with self.assertRaises(MisiurewiczError):propagate_parry({0:1},time)

    def test_stale_phase_source_or_wrong_time_rejected(self):
        s=Source('single-algebraic-logistic',11)
        a=PhaseReceipt(s,0,0)
        b=PhaseReceipt(s,1,2)
        self.assertTrue(verify_E_Eprime_phase(a,b)['phase_valid'])
        with self.assertRaises(MisiurewiczError):
            verify_E_Eprime_phase(a,PhaseReceipt(Source('single-algebraic-logistic',12),1,2))
        with self.assertRaises(MisiurewiczError):
            verify_E_Eprime_phase(b,a)
        with self.assertRaises(MisiurewiczError):
            verify_E_Eprime_phase(a,PhaseReceipt(s,1,1))
        with self.assertRaises(MisiurewiczError):PhaseReceipt(s,-1,0)
        with self.assertRaises(MisiurewiczError):PhaseReceipt('raw-name',0,0)

    def test_dual_E_long_range_phase_correlation_and_declared_parity(self):
        for n in range(0,52):
            r=dual_phase_correlation(n)
            self.assertEqual(r['raw_phase_covariance'], F((-1)**n,4))
            self.assertEqual(r['parity_transport_sign'],(-1)**n)
            self.assertEqual(r['transported_phase_covariance'],F(1,4))
            self.assertEqual(r['raw_phase_mutual_information_bits'],1)
            self.assertEqual(r['phase_entropy_rate_bits'],0)
            self.assertEqual(r['conditional_micro_entropy_rate_bits_under_Parry'],F(1,2))
        with self.assertRaises(MisiurewiczError):dual_phase_correlation(-1)
        with self.assertRaises(MisiurewiczError):dual_phase_correlation(True)

    def test_dual_E_phase_covariance_independent_two_source_oracle(self):
        for n in range(0,32):
            joint=[]
            for phase0 in (0,1):
                future=phase0^(n&1)
                joint.append((phase0,future,F(1,2)))
            ex=sum((p*x for x,y,p in joint),F(0))
            ey=sum((p*y for x,y,p in joint),F(0))
            exy=sum((p*x*y for x,y,p in joint),F(0))
            self.assertEqual(exy-ex*ey,dual_phase_correlation(n)['raw_phase_covariance'])

    def test_phase_periodicity_refutes_strong_mixing_for_this_source(self):
        # The phase=0 set has measure 1/2 and 2n-return overlap 1/2,
        # unlike 1/4 expected in a strongly mixing source as n->infinity.
        for n in (10,100,1000):
            r=dual_phase_correlation(n)
            self.assertEqual(r['raw_phase_covariance'],F(1,4))
            self.assertNotEqual(r['raw_phase_covariance'],F(0))

    def test_phase_agreement_does_not_recover_micro_path(self):
        s=Source('source',1)
        a=PhaseReceipt(s,0,2)
        c=PhaseReceipt(s,2,2)
        receipt=verify_E_Eprime_phase(a,c)
        self.assertEqual(receipt['lag'],2)
        self.assertFalse(receipt['complete_micro_path_recovered'])
        self.assertEqual(path_count(2,2),2)
        self.assertTrue(legal_path((2,0,2)))
        self.assertTrue(legal_path((2,1,2)))

    def test_boundary_fixed_point_prevents_global_flipping_phase(self):
        self.assertEqual(f(FIXED),FIXED)
        # Any globally defined {0,1}-valued phi with phi(f(x))=1-phi(x)
        # at FIXED would demand phi(FIXED)=1-phi(FIXED), impossible.
        for label in (0,1):
            self.assertNotEqual(label,1-label)


if __name__=='__main__':
    unittest.main()
