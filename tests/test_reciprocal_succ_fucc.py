"""Hostile finite exact probes for bidirectional arithmetic/Pascal compatibility."""
import unittest
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial

from observational_succ.reciprocal_succ_fucc import (
    ReciprocalSourceError, prime, vstar, reciprocal_braid, residue_clock,
    from_residue_clock, clock_succ, mixed_radix, direct_mixed_radix_change,
    gibbs_unnormalized, oriented_rates, finite_source_edges,
    finite_generator, finite_stationarity, finite_dirichlet_form,
    weighted_affine_diamond, mirror_affine_on_basis,
    pascal_prime_rank, direct_prime_rank, pascal_last_step,
    gibbs_rank_nonprojective, finite_reciprocal_boundary_defect,
    finite_reciprocal_square_on_basis,
)


class ReciprocalBraidTests(unittest.TestCase):
    def test_exact_p_step_pullback_square_all_residue_classes(self):
        for p in (2,3,5,7,11,17):
            for n in range(1,311):
                left,right=reciprocal_braid(n,p)
                self.assertEqual(left,right)
                self.assertEqual(left,(n//p+1) if n%p==0 else None)

    def test_one_succ_step_needs_residue_phase_not_a_naive_quotient(self):
        for p in (2,3,5,7):
            witness=p-1
            self.assertIsNone(vstar(witness,p))
            self.assertEqual(vstar(witness+1,p),1)

    def test_clock_bijection_and_single_step_carry(self):
        for p in (2,3,5,7,11):
            for n in range(1,250):
                q,r=residue_clock(n,p)
                self.assertEqual(from_residue_clock(q,r,p),n)
                self.assertEqual(clock_succ(q,r,p),residue_clock(n+1,p))
                self.assertEqual(residue_clock(p*n,p),(n,p-1))

    def test_quotient_scale_succ_p_preserves_each_clock_phase(self):
        for p in (2,3,5,7):
            for n in range(1,200):
                q,r=residue_clock(n,p)
                self.assertEqual(residue_clock(n+p,p),(q+1,r))

    def test_mixed_radix_clock_change_is_canonical_not_simple_swap(self):
        for p,q in product((2,3,5,7),repeat=2):
            for n in range(1,161):
                (m,s,r),(mm,t,u)=mixed_radix(n,p,q)
                self.assertEqual(m,mm)
                self.assertEqual((t,u),direct_mixed_radix_change(s,r,p,q))
                self.assertEqual(n-1,p*q*(m-1)+p*s+r)
                self.assertEqual(n-1,p*q*(mm-1)+q*t+u)
        self.assertNotEqual(direct_mixed_radix_change(1,1,2,3),(1,1))

    def test_three_prime_clocks_all_permutations_have_same_source_endpoint(self):
        for n in range(1,100):
            reports=[]
            for order in permutations((2,3,5)):
                current=n
                residue_digits=[]
                for p in order:
                    current,r=residue_clock(current,p)
                    residue_digits.append(r)
                R=0
                stride=1
                for p,r in zip(order,residue_digits):
                    R+=stride*r
                    stride*=p
                self.assertEqual(stride,30)
                reports.append((current,R))
                self.assertEqual(30*(current-1)+R+1,n)
            self.assertEqual(len(set(reports)),1)


class GibbsCompatibilityTests(unittest.TestCase):
    def test_reciprocal_detailed_balance_on_both_source_edge_families(self):
        for beta in (2,3,4,6):
            for n in range(1,60):
                for m in (n+1,2*n,3*n,5*n):
                    if m==n:
                        continue
                    up,down=oriented_rates(n,m,beta)
                    self.assertEqual(gibbs_unnormalized(n,beta)*up,
                                     gibbs_unnormalized(m,beta)*down)

    def test_finite_markov_generators_reversible_and_stationary(self):
        for N in (4,9,18,32):
            for beta in (2,3,4):
                report=finite_stationarity(N,(2,3,5),beta)
                self.assertEqual(report['edge_fails'],[])
                self.assertTrue(all(v==0 for v in report['row_sums']))
                self.assertTrue(all(v==0 for v in report['pi_L']))
                self.assertEqual(sum(report['pi']),Q(1))
                self.assertEqual(len(report['edges']),
                                 len(finite_source_edges(N,(2,3,5),beta)))
                matrix=finite_generator(N,(2,3,5),beta)
                for i,j in product(range(N),repeat=2):
                    self.assertEqual(report['pi'][i]*matrix[i][j],
                                     report['pi'][j]*matrix[j][i])

    def test_dirichlet_energy_positive_and_constants_zero(self):
        for beta in (2,3,4):
            for N in (8,13):
                self.assertEqual(finite_dirichlet_form((1,)*N,N,(2,3,5),beta),0)
                data=tuple(Q((i*7)%9-4,i+1) for i in range(N))
                self.assertGreater(finite_dirichlet_form(data,N,(2,3,5),beta),0)

    def test_affine_diamond_is_flat_at_rate_and_amplitude_levels(self):
        for beta in (2,3,4):
            for p in (2,3,5,7):
                for n in range(1,36):
                    a,b,d=weighted_affine_diamond(n,p,beta)
                    self.assertEqual(a,b)
                    self.assertEqual(a,d)

    def test_thermal_p_divisibility_conditional_is_original_gibbs_law(self):
        for beta in (2,3,4):
            for p in (2,3,5,7):
                for n in range(1,80):
                    self.assertEqual(gibbs_unnormalized(p*n,beta)/Q(1,p**beta),
                                     gibbs_unnormalized(n,beta))

    def test_mirror_anti_homomorphism_on_positive_affine_basis(self):
        for beta in (2,4):
            for a,b,c,d in product((1,2,3),(0,1,2),(1,2,3),(0,1)):
                for n in range(1,16):
                    intermediate=c*n+d
                    target=a*intermediate+b
                    directly=mirror_affine_on_basis(target,a*c,a*d+b,beta)
                    first=mirror_affine_on_basis(target,a,b,beta)
                    self.assertIsNotNone(first)
                    second=mirror_affine_on_basis(first[0],c,d,beta)
                    self.assertEqual(directly[0],second[0])
                    self.assertEqual(directly[1],first[1]*second[1])


class PascalPrimeMultisetTests(unittest.TestCase):
    def test_divided_power_creation_recovers_every_occupation_monomial(self):
        for primes in ((2,),(2,3),(2,3,5)):
            for rank in range(0,8):
                for beta in (2,4):
                    self.assertEqual(pascal_prime_rank(primes,rank,beta),
                                     direct_prime_rank(primes,rank,beta))

    def test_exact_three_order_factorial_multiplicity(self):
        lam2,lam3=Q(1,2),Q(1,3)
        total=Q()
        for path in set(permutations((2,2,3))):
            a=Counter()
            product_weight=Q(1)
            for p in path:
                product_weight*=({2:lam2,3:lam3}[p])*(a[p]+1)
                a[p]+=1
            total+=product_weight
        self.assertEqual(total/factorial(3),lam2*lam2*lam3)
        self.assertEqual(total,Q(6)*lam2*lam2*lam3)

    def test_last_step_cotransition_is_occupation_fraction(self):
        for alpha in ((2,1),(1,0,3),(0,0,4,2),(1,1,1,1)):
            q=pascal_last_step(alpha)
            self.assertEqual(sum(q.values(),Q()),Q(1))
            for predecessor,weight in q.items():
                self.assertEqual(sum(predecessor),sum(alpha)-1)
                missing=[i for i in range(len(alpha)) if predecessor[i]!=alpha[i]]
                self.assertEqual(len(missing),1)
                self.assertEqual(weight,Q(alpha[missing[0]],sum(alpha)))

    def test_source_rank_gibbs_conditionals_not_projective_under_pascal_backwards(self):
        direct,backprojected=gibbs_rank_nonprojective((2,3),2)
        self.assertNotEqual(direct,backprojected)
        self.assertGreater(backprojected,direct)

    def test_wrong_poisson_factorials_fail_prime_power_amplitude(self):
        genuine=direct_prime_rank((2,3),2,2)
        self.assertEqual(genuine[(2,0)],Q(1,4))
        self.assertNotEqual(genuine[(2,0)],Q(1,8))
        self.assertEqual(genuine[(1,1)],Q(1,6))

    def test_interaction_potential_can_be_flat_without_being_additive(self):
        def psi(alpha):return Q(1+alpha[0]**2+alpha[0]*alpha[1])
        def w(alpha,i):
            nxt=list(alpha)
            nxt[i]+=1
            return Q(alpha[i]+1,(2,3)[i])*psi(tuple(nxt))/psi(alpha)
        for a,b in product(range(4),repeat=2):
            alpha=(a,b)
            x=(a+1,b)
            y=(a,b+1)
            self.assertEqual(w(alpha,0)*w(x,1),w(alpha,1)*w(y,0))
        self.assertNotEqual(2*w((0,0),0)*w((1,0),1),
                            w((0,0),1)*w((0,1),0))

    def test_fake_composite_generator_is_rejected_as_prime_jet(self):
        self.assertFalse(prime(6))
        with self.assertRaises(ReciprocalSourceError):vstar(12,6)
        with self.assertRaises(ReciprocalSourceError):finite_source_edges(20,(2,6),2)
        with self.assertRaises(ReciprocalSourceError):pascal_prime_rank((2,6),2)

    def test_wrong_types_and_missing_phases_fail_closed(self):
        with self.assertRaises(ReciprocalSourceError):residue_clock(10,4)
        with self.assertRaises(ReciprocalSourceError):from_residue_clock(3,3,3)
        with self.assertRaises(ReciprocalSourceError):direct_mixed_radix_change(3,0,2,3)
        with self.assertRaises(ReciprocalSourceError):oriented_rates(1,2,True)
        with self.assertRaises(ReciprocalSourceError):finite_dirichlet_form((1.,1),2,(2,),2)
        with self.assertRaises(ReciprocalSourceError):mirror_affine_on_basis(3,2,0,beta_even=3)


class SharpReciprocalBoundaryTests(unittest.TestCase):
    def test_rank_one_mixed_adjoint_cutoff_defect_for_every_basis(self):
        for N in range(1,81):
            for p in (2,3,5,7,11):
                defect=finite_reciprocal_boundary_defect(N,p)
                expected=(p*(N//p),N//p+1,Q(-1)) if N>=p else None
                self.assertEqual(defect,expected)
                for n in range(1,N+1):
                    lhs,rhs=finite_reciprocal_square_on_basis(n,N,p)
                    if defect is not None and n==defect[0]:
                        self.assertIsNone(lhs)
                        self.assertEqual(rhs,defect[1])
                    else:
                        self.assertEqual(lhs,rhs)

    def test_sharp_boundary_operator_norm_one_but_strong_zero(self):
        for p in (2,3,5):
            for N in (p,2*p+1,7*p+2):
                src,dst,c=finite_reciprocal_boundary_defect(N,p)
                self.assertEqual(c,Q(-1))
                self.assertGreaterEqual(src,1)
                self.assertLessEqual(src,N)
                self.assertLessEqual(dst,N)
            for fixed in range(1,15):
                for N in range(fixed+p,p*(fixed+3)):
                    defect=finite_reciprocal_boundary_defect(N,p)
                    self.assertTrue(defect is None or defect[0]!=fixed)

    def test_wrong_phase_shift_does_not_have_same_rank_one_repair(self):
        for p in (3,5,7):
            for N in (3*p,4*p):
                witness=p-1
                self.assertIsNone(vstar(witness,p))
                self.assertEqual(vstar(witness+1,p),1)
                self.assertLess(witness+1,N)

    def test_existing_pascal_cotransition_matches_two_prime_occupations(self):
        from observational_succ.pascal_rotated_transport import backward_kernel
        for n in range(1,15):
            for k in range(n+1):
                ours=pascal_last_step((n-k,k))
                theirs=dict(backward_kernel(n,k))
                self.assertEqual({alpha[1]:weight for alpha,weight in ours.items()},
                                 theirs)


if __name__=='__main__':unittest.main()
