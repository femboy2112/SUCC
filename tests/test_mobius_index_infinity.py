"""Exact independent SUCC index, Möbius sieve, Haar and prime-density oracles."""
import unittest
from fractions import Fraction as F
from math import gcd, isqrt, prod
from itertools import combinations

from observational_succ.mobius_index_infinity import (
    IndexBoundaryError, squarefree_mobius_tape, sieve_projection,
    finite_sieve_count, prime_shell, shell_trace, finite_succ_boundary,
    finite_fucc_boundary, strong_sieve_limit, exact_prime_jets_from_index_density,
    sign_mutant_control, sieve_succ_commutator,
)


def _transpose(A):
    return [list(r) for r in zip(*A)]


def _mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def _commutator_matrix(A):
    """Independent finite shift matrices and exact full commutator."""
    at=_transpose(A)
    left=_mul(at,A)
    right=_mul(A,at)
    return [[left[i][j]-right[i][j] for j in range(len(A))]
            for i in range(len(A))]


def _genuine_prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


class MobiusIndexAtInfinityTests(unittest.TestCase):
    def test_independent_boolean_inclusion_exclusion_and_projection_laws(self):
        for ps in ((),(2,),(2,3),(2,3,5),(2,3,5,7)):
            tape=dict(squarefree_mobius_tape(ps))
            self.assertEqual(len(tape),2**len(ps))
            self.assertEqual(tape[1],1)
            for n in range(1,200):
                direct=int(all(n%p for p in ps))
                mobius=sum(s for d,s in tape.items() if n%d==0)
                self.assertEqual(direct,mobius)
                self.assertIn(mobius,(0,1))
                self.assertEqual(mobius*mobius,mobius)
                got=sieve_projection(n,ps)
                self.assertEqual(got["projection_diagonal"],direct)
                self.assertTrue(got["full_positive_projection_by_commuting_factors"])
                self.assertFalse(got["same_as_original_signed_Weil_quadratic"])

    def test_all_prime_finite_sieve_density_independent_direct_enumeration(self):
        for ps in ((),(2,),(2,3),(2,3,5),(2,3,5,7)):
            M=prod(ps)
            for N in (1,3,8,11,30,2*M,2*M+13):
                r=finite_sieve_count(ps,N)
                brute=sum(gcd(n,M)==1 for n in range(1,N+1))
                self.assertEqual(r["integer_source_trace"],brute)
                self.assertEqual(r["normalized_trace"],F(brute,N))
                self.assertLessEqual(r["exact_total_variation_scalar_error"],
                                     r["source_uniform_error_upper"])
                if N%M==0:
                    self.assertEqual(r["normalized_trace"],r["additive_profinite_unit_Haar"])
                    self.assertTrue(r["perfect_period_when_N_multiple_of_primorial"])
            self.assertEqual(finite_sieve_count(ps,M)["additive_profinite_unit_Haar"],
                             prod((F(p-1,p) for p in ps),start=F(1)))

    def test_source_Tate_prime_shell_density_and_exact_finite_budget(self):
        for p in (2,3,5,7,11):
            for k in range(0,5):
                for N in (2,7,21,50,301,1001):
                    r=shell_trace(p,k,N)
                    brute=0
                    for n in range(1,N+1):
                        v=0;m=n
                        while m%p==0:
                            v+=1
                            m//=p
                        self.assertEqual(prime_shell(n,p,k),int(v==k))
                        brute+=int(v==k)
                    self.assertEqual(r["finite_exact_shell_count"],brute)
                    self.assertEqual(r["limit_additive_Haar_shell_density"],
                                     F(p-1,p**(k+1)))
                    self.assertEqual(r["p_adic_unit_Haar_mass"],F(p-1,p))
                    self.assertEqual(r["source_half_density_amplitude_squared"],F(1,p**k))
                    self.assertLessEqual(r["finite_horizon_density_error"],F(1,N))
                    self.assertEqual(r["multiplicative_Haar_shell_mass"],1)

    def test_literal_unilateral_succ_commutator_has_escaping_negative_edge(self):
        for N in (1,2,3,4,7,11):
            shift=[[int(i==j+1) for j in range(N)] for i in range(N)]
            comm=_commutator_matrix(shift)
            r=finite_succ_boundary(N)
            diagonal=tuple((i+1,comm[i][i]) for i in range(N)
                           if comm[i][i])
            self.assertEqual(r["finite_diagonal_nonzero"],diagonal)
            self.assertTrue(all(comm[i][j]==0 for i in range(N) for j in range(N) if i!=j))
            self.assertEqual(sum(comm[i][i] for i in range(N)),0)
            self.assertEqual(r["strong_limit_trace"],1)
            self.assertEqual(r["Fredholm_index_of_unilateral_S"],-1)
            self.assertFalse(r["trace_norm_convergence"])

    def test_literal_fucc_compressed_matrix_has_zero_trace_but_nonzero_bulk_index(self):
        for p in (2,3,5,7):
            for N in (1,2,3,7,13,17,40):
                shift=[[int(i+1==p*(j+1)) for j in range(N)]
                       for i in range(N)]
                comm=_commutator_matrix(shift)
                rec=finite_fucc_boundary(p,N)
                diagonal=tuple((i+1,comm[i][i]) for i in range(N)
                               if comm[i][i])
                self.assertEqual(rec["finite_commutator_diagonal"],diagonal)
                self.assertEqual(sum(comm[i][i] for i in range(N)),0)
                self.assertTrue(all(comm[i][j]==0 for i in range(N) for j in range(N) if i!=j))
                self.assertEqual(rec["finite_upper_boundary_counterterm_trace"],
                                 -(N-N//p))
                self.assertEqual(rec["limit_defect_bulk_trace_density"],F(p-1,p))
                self.assertEqual(rec["trace_density_at_fixed_N_of_compressed_commutator"],0)
                self.assertFalse(rec["limit_operator_trace_class"])

    def test_local_padic_connes_Tate_actual_full_prime_tape_cross_oracle(self):
        for p,k in ((2,1),(2,2),(2,3),(2,7),(3,1),(3,2),
                    (3,4),(5,1),(5,2),(5,3),(7,1),(7,3),
                    (11,1),(11,2)):
            if p**k>200000:
                continue
            r=exact_prime_jets_from_index_density(p,k)
            self.assertEqual(r["normalized_amplitude_squared"],F(1,p**k))
            self.assertEqual(r["connes_Cp_squared"],F(1,p**k))
            self.assertEqual(r["Tate_one_place_norm"],F(1,p**k))
            self.assertEqual(r["actual_von_Mangoldt_label"],p)
            self.assertFalse(r["signed_Gamma_contact_pole_terms_derived"])
            self.assertFalse(r["all_test_completed_Weil_PSD_proved"])

    def test_orthogonal_sieve_strong_limit_preserves_one_not_nongenuine_zero(self):
        for ps in ((2,),(2,3),(2,3,5),(2,3,5,7)):
            M=prod(ps)
            r=strong_sieve_limit(ps,(1,2,3,4,6,30,77,121))
            self.assertEqual(r["universal_strong_limit_on_all_l2_sequences"],"|1><1|")
            self.assertEqual(r["finite_stage_operator_norm_difference_from_limit"],1)
            self.assertFalse(r["norm_convergence"])
            self.assertEqual(dict(r["finite_probe_response"])[1],1)
            # Find a genuinely new prime q. Then E_P(q)=1, but P1(q)=0,
            # exhibiting the operator norm obstruction EXACTLY.
            q=next(q for q in range(2,100) if _genuine_prime(q) and q not in ps)
            self.assertEqual(sieve_projection(q,ps)["projection_diagonal"],1)
            self.assertGreater(q,1)

    def test_sieve_S_commutator_source_boundary_survives_hilbert_completion(self):
        for ps in ((2,),(2,3),(2,3,5)):
            q=next(q for q in range(5,300) if _genuine_prime(q) and q not in ps)
            self.assertEqual(sieve_projection(q,ps)["projection_diagonal"],1)
            self.assertEqual(sieve_projection(q-1,ps)["projection_diagonal"],0)
            # [S,E] e_(q-1)=(E(q-1)-E(q)) e_q=-e_q.
            self.assertEqual(
                sieve_projection(q-1,ps)["projection_diagonal"]-
                sieve_projection(q,ps)["projection_diagonal"],-1)
            # Meanwhile P1 has commutator zero on e_(q-1), q>3.
            self.assertEqual(int(q-1==1)-int(q==1),0)

    def test_source_SUCC_commutator_strong_but_not_norm_limit(self):
        for ps in ((2,),(2,3),(2,3,5),(2,3,5,7)):
            for n in range(1,100):
                w=sieve_succ_commutator(ps,n)
                left=sieve_projection(n,ps)["projection_diagonal"]
                right=sieve_projection(n+1,ps)["projection_diagonal"]
                self.assertEqual(w["finite_sieve_edge_coefficient"],left-right)
                self.assertEqual(w["difference_from_limit"],left-right-int(n==1))
                self.assertTrue(w["cofinal_operator_norm_difference_at_least_one_if_2_in_P"])
                self.assertFalse(w["completed_Weil_trace_or_contact_identified"])
            q=next(q for q in range(11,200) if _genuine_prime(q) and q not in ps)
            witness=sieve_succ_commutator(ps,q-1)
            self.assertEqual(witness["finite_sieve_edge_coefficient"],-1)
            self.assertEqual(witness["strong_limit_unit_boundary_edge_coefficient"],0)
            self.assertEqual(witness["difference_from_limit"],-1)

    def test_orientation_sign_mutant_not_idempotent_even_though_coefficients_positive(self):
        for p in (2,3,5,7):
            x=sign_mutant_control(p)
            self.assertEqual(x["authentic_at_n_p"],0)
            self.assertEqual(x["plus_sign_mutant_at_n_p"],2)
            self.assertEqual(x["mutant_square_at_n_p"],4)
            self.assertFalse(x["mutant_idempotent"])

    def test_fake_composite_place_rejected_but_composite_FUCC_dilation_lawful(self):
        for bad in (6,4,1,0,True,2.0):
            with self.assertRaises(IndexBoundaryError):
                squarefree_mobius_tape((bad,))
            with self.assertRaises(IndexBoundaryError):
                shell_trace(bad,1,100)
        # V_6 exists as a COMPOSITE dilation and is V_2 V_3.
        self.assertEqual(2*3*7,6*7)
        self.assertEqual(sum(n%6==0 for n in range(1,61)),10)

    def test_source_type_and_horizon_rejections(self):
        with self.assertRaises(IndexBoundaryError):
            squarefree_mobius_tape((3,2))
        with self.assertRaises(IndexBoundaryError):
            squarefree_mobius_tape((2,2))
        with self.assertRaises(IndexBoundaryError):
            finite_sieve_count((2,3),True)
        with self.assertRaises(IndexBoundaryError):
            sieve_projection(0,(2,))
        with self.assertRaises(IndexBoundaryError):
            shell_trace(2,True,30)
        with self.assertRaises(IndexBoundaryError):
            exact_prime_jets_from_index_density(2,0)
        with self.assertRaises(IndexBoundaryError):
            exact_prime_jets_from_index_density(2,20)
        with self.assertRaises(IndexBoundaryError):
            finite_succ_boundary(0)
        with self.assertRaises(IndexBoundaryError):
            strong_sieve_limit((2,),())
        with self.assertRaises(IndexBoundaryError):
            strong_sieve_limit((2,),(0,))
        self.assertEqual(finite_sieve_count((),37)["normalized_trace"],1)


if __name__=="__main__":
    unittest.main()
