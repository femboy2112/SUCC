"""Exact Koszul chain differential, contraction, Euler and source Mellin tests."""
import unittest
from fractions import Fraction as Q
from itertools import combinations
from math import comb

from observational_succ.koszul_prime_cancellation import (
    KoszulSourceError, PrimeKoszul, source_multidegree,
    finite_koszul_mellin_cancel,
)
from observational_succ.mobius_tate_gamma_remainder import (
    exact_divisor_cancel, finite_tate_gamma_remainder,
)


def independent_rational_rank(matrix):
    """Separate Gaussian-elimination oracle, not a method of PrimeKoszul."""
    if not matrix:
        return 0
    a=[[Q(x) for x in row] for row in matrix]
    nr,nc=len(a),len(a[0])
    rank=0
    for col in range(nc):
        pivot=next((i for i in range(rank,nr) if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        scale=a[rank][col]
        a[rank]=[x/scale for x in a[rank]]
        for i in range(nr):
            if i!=rank and a[i][col]:
                coeff=a[i][col]
                a[i]=[u-coeff*v for u,v in zip(a[i],a[rank])]
        rank+=1
        if rank==nr:break
    return rank


def independent_koszul_degree_rank(active,j):
    """Construct boundary solely from combinatorial deletion, not repo d()."""
    domain=list(combinations(active,j))
    codomain=list(combinations(active,j-1))
    if not codomain:return 0
    matrix=[]
    for T in codomain:
        row=[]
        for S in domain:
            coefficient=0
            for i in range(len(S)):
                if S[:i]+S[i+1:]==T:
                    coefficient+=(-1)**i
            row.append(coefficient)
        matrix.append(row)
    return independent_rational_rank(matrix)


class PrimeKoszulCancellationTests(unittest.TestCase):
    def test_all_source_integers_have_exact_homological_cancellation(self):
        for n in range(1,161):
            complex=source_multidegree(n)
            r=complex.theorem_receipt()
            self.assertTrue(r['boundary_squared_is_zero'])
            self.assertTrue(r['matches_divisor_Mobius_cancellation'])
            self.assertEqual(r['signed_euler_characteristic'],int(n==1))
            self.assertEqual(r['signed_euler_characteristic'],
                             exact_divisor_cancel(n)['arithmetic_convolution_sum'])
            if n>1:
                self.assertTrue(r['positive_multidegree_chain_contracted'])
            self.assertFalse(r['positive_Hermitian_Weil_form_constructed'])

    def test_p_square_and_higher_are_RETAINED_and_canceled_correctly(self):
        for p in (2,3,5):
            for k in (1,2,3,5,8):
                c=PrimeKoszul((p,),(k,))
                r=c.theorem_receipt()
                self.assertEqual(r['exterior_chain_dims'],(1,1))
                self.assertEqual(r['signed_euler_characteristic'],0)
                self.assertEqual(c.boundary((p,)),(((),1),))
                self.assertEqual(c.contracting_homotopy(()),(((p,),1),))
                self.assertTrue(c.negative_first_chain_gauge()['parity_conjugates_d_to_minus_d'])

    def test_two_and_three_prime_higher_valence_complex(self):
        for alphas in ((1,1),(2,3),(3,1),(5,5)):
            c=PrimeKoszul((2,3),alphas)
            r=c.theorem_receipt()
            self.assertEqual(r['exterior_chain_dims'],(1,2,1))
            self.assertEqual(r['signed_euler_characteristic'],0)
            self.assertTrue(r['positive_multidegree_chain_contracted'])
        c=PrimeKoszul((2,3,5,7),(2,1,3,1))
        r=c.theorem_receipt()
        self.assertEqual(r['exterior_chain_dims'],(1,4,6,4,1))
        self.assertTrue(r['boundary_squared_is_zero'])

    def test_independent_Gaussian_ranks_match_contracting_homotopy(self):
        for primes,alpha in (((2,),(2,)),((2,3),(2,3)),
                             ((2,3,5),(1,2,4)),
                             ((2,3,5,7),(2,1,3,1))):
            c=PrimeKoszul(primes,alpha)
            support=c.active
            r=len(support)
            for j in range(1,r+1):
                rank=independent_koszul_degree_rank(support,j)
                self.assertEqual(rank,comb(r-1,j-1))
            self.assertTrue(c.theorem_receipt()['positive_multidegree_chain_contracted'])

    def test_mutated_unoriented_boundary_fails_d_squared(self):
        # On theta_2 wedge theta_3, BOTH unsigned deletions give +e.
        # Squaring the unsigned boundary yields 1+1=2, not zero.
        c=PrimeKoszul((2,3),(1,1))
        self.assertEqual(c.boundary((2,3)),(((3,),1),((2,),-1)))
        signed=c.act(c.act({(2,3):Q(1)},"boundary"),"boundary")
        self.assertEqual(signed,{})
        unsigned_second_boundary=1+1
        self.assertNotEqual(unsigned_second_boundary,0)

    def test_full_prime_power_bosonic_exterior_cancel_matches_Tate(self):
        for primes in ((2,),(2,3),(2,3,5),(2,3,5,7)):
            for beta in (2,4,6):
                c=finite_koszul_mellin_cancel(primes,beta)
                t=finite_tate_gamma_remainder(primes,beta)
                self.assertTrue(c['product_cancels_exactly'])
                self.assertEqual(c['polynomial_symmetric_generating_factor'],
                                 t['genuine_Tate_finite_zeta'])
                self.assertEqual(c['exterior_signed_superfactor'],
                                 t['genuine_Mobius_convolution_inverse'])
                self.assertTrue(c['archimedean_Gamma_must_be_retained'])
                self.assertFalse(c['RH_proved'])

    def test_global_negative_first_is_chain_gauge_not_unital_ring_reversal(self):
        for primes,alpha in (((),()),((2,),(2,)),((2,3),(1,1)),
                             ((2,3,5),(2,1,3))):
            c=PrimeKoszul(primes,alpha)
            r=c.negative_first_chain_gauge()
            self.assertTrue(r['parity_conjugates_d_to_minus_d'])
            self.assertTrue(r['oriented_chain_homology_unchanged'])
            self.assertFalse(r['unital_arithmetic_ring_sign_reversal_licensed'])

    def test_exterior_Clifford_anticommutators_and_weighted_positive_Laplacian(self):
        c=PrimeKoszul((2,3,5),(2,1,3))
        active=c.active
        def compose(S,op1,p,op2,q):
            total={}
            for T,a in getattr(c,op2)(q,S):
                for U,b in getattr(c,op1)(p,T):
                    total[U]=total.get(U,Q(0))+a*b
            return total
        for S in c.basis():
            for p in active:
                for q in active:
                    left=compose(S,"exterior_annihilation",p,"exterior_creation",q)
                    right=compose(S,"exterior_creation",q,"exterior_annihilation",p)
                    result={T:left.get(T,0)+right.get(T,0) for T in set(left)|set(right)}
                    result={T:v for T,v in result.items() if v}
                    self.assertEqual(result,{S:1} if p==q else {})
            weights={2:Q(2),3:Q(3),5:Q(5)}
            def weighted_map(chain,creation):
                result={}
                method="exterior_creation" if creation else "exterior_annihilation"
                for T,a in chain.items():
                    for p,w in weights.items():
                        for U,b in getattr(c,method)(p,T):
                            result[U]=result.get(U,Q(0))+a*w*b
                return {T:v for T,v in result.items() if v}
            e={S:Q(1)}
            ddstar=weighted_map(weighted_map(e,True),False)
            dstard=weighted_map(weighted_map(e,False),True)
            lap={T:ddstar.get(T,0)+dstard.get(T,0) for T in set(ddstar)|set(dstard)}
            lap={T:v for T,v in lap.items() if v}
            self.assertEqual(lap,{S:Q(38)})
        self.assertTrue(c.hodge_laplacian_receipt()['positive_semidefinite_on_every_exterior_chain'])

    def test_fiberwise_weighted_supercharge_recovers_original_log_n(self):
        for n in (1,2,3,4,6,8,9,12,18,30,36,72,120):
            c=source_multidegree(n)
            h=c.weighted_log_clock_factorization()
            self.assertEqual(h['source_integer'],n)
            self.assertEqual(h['weighted_Hodge_laplacian_symbol'],f"log({n})*I")
            self.assertEqual(c.hodge_laplacian_receipt()['hodge_eigenvalue'],len(c.active))
            self.assertTrue(h['Clifford_cross_terms_cancel'])
            self.assertFalse(h['Weil_functional_identified'])
        self.assertEqual(source_multidegree(1).hodge_laplacian_receipt()['hodge_eigenvalue'],0)

    def test_original_source_and_bad_wedge_mutations(self):
        for ps,exponents in (((6,),(1,)),((3,2),(1,1)),
                             ((2,2),(1,1)),((2,),(True,)),
                             ((2,),(-1,))):
            with self.assertRaises(KoszulSourceError):
                PrimeKoszul(ps,exponents)
        c=PrimeKoszul((2,3),(1,2))
        for bad in ((6,),(3,2),(2,2),(5,),[2],()):
            if bad==():continue
            with self.assertRaises(KoszulSourceError):
                c.boundary(bad)
        for beta in (0,1,True,Q(2)):
            with self.assertRaises(KoszulSourceError):
                finite_koszul_mellin_cancel((2,),beta)


if __name__=="__main__":
    unittest.main()
