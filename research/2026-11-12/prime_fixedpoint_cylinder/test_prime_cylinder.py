"""Two decompositions where possible; deterministic finite checks, not a universal proof."""
import unittest
from math import prod
from prime_cylinder import (prime_factors, is_prime, omega, defect, divisor_count,
    split_terms, commutator_number_eigenvalue, categorical_walk, first_primes,
    pair_grade, phase_polynomial, exact_phase_average, safe_phase_count,
    witnesses, wiggle_edges, commutator_frobenius_square,
    counterfeit_commutator_no_witness, plaquette_holonomy, prime_birth_commutator)


def independent_sieve(N):
    a=[True]*(N+1)
    a[:2]=[False,False]
    for k in range(2,int(N**.5)+1):
        if a[k]:
            for j in range(k*k,N+1,k): a[j]=False
    return a


class PrimeFixedpointTests(unittest.TestCase):
    def test_coproduct_commutator_and_exact_fixedpoints(self):
        sv=independent_sieve(1200)
        for n in range(1,1201):
            self.assertEqual(commutator_number_eigenvalue(n),len(split_terms(n)))
            self.assertEqual(commutator_number_eigenvalue(n)==0,n==1 or sv[n])
            self.assertEqual(defect(n)==0,n==1 or sv[n])
            self.assertEqual(omega(n),len(prime_factors(n)))
            self.assertEqual(divisor_count(n)-2 if n>1 else 0,len(split_terms(n)))

    def test_reduced_coassociativity_independent_triples(self):
        for n in range(1,150):
            left=[]; right=[]
            for a,b in split_terms(n):
                left.extend((x,y,b) for x,y in split_terms(a))
                right.extend((a,x,y) for x,y in split_terms(b))
            self.assertEqual(sorted(left),sorted(right))

    def test_recursive_semantic_preservation(self):
        for n in range(1,900):
            states=categorical_walk(n)
            self.assertEqual(len(states)-1,max(omega(n)-1,0))
            for m,ctx in states:
                self.assertEqual(m*prod(ctx),n)
            for (m,_),(q,_) in zip(states,states[1:]): self.assertLess(q,m)
            self.assertTrue(states[-1][0]==1 or is_prime(states[-1][0]))
            self.assertEqual(len(states)==1,n==1 or is_prime(n))

    def test_observer_prime_enumeration(self):
        self.assertEqual(first_primes(20),tuple(i for i,v in enumerate(independent_sieve(72)) if v)[:20])

    def test_prime_FUCC_boundary_commutator(self):
        for p in (2,3,5,7,11,13):
            for n in range(1,100):
                self.assertEqual(prime_birth_commutator(n,p),0 if n==1 else 1)

    def test_cylinder_exact_character_and_alias(self):
        self.assertEqual(phase_polynomial(10),{0:2,1:2,2:3,4:2})
        self.assertEqual(phase_polynomial(10,signed=True),{0:4,1:4,2:5,4:4})
        self.assertEqual(exact_phase_average(10,2),7)  # composite alias h=2,4
        for n in range(2,111):
            M=safe_phase_count(n)
            self.assertTrue(all(k<M for k in phase_polynomial(n)))
            self.assertEqual(exact_phase_average(n,M),len(witnesses(n)))
            self.assertEqual(exact_phase_average(n,M,signed=True),len(witnesses(n,signed=True)))
            self.assertEqual(len(witnesses(n,signed=True)),2*len(witnesses(n))-int(is_prime(n)))

    def test_direct_sieve_against_factorization_observer(self):
        sv=independent_sieve(2050)
        for n in [2,3,4,10,32,64,100,256,1024]:
            direct=sum(sv[n+d] and sv[n-d] for d in range(n-1))
            self.assertEqual(direct,len(witnesses(n)))

    def test_wiggle_discrete_commutator(self):
        for n in range(3,110):
            edges=wiggle_edges(n)
            mat=[d for d in range(n-1) if (n+d)%2]
            self.assertEqual(edges,tuple((a,b) for a in mat for b in mat if b==a+2))
            self.assertEqual(commutator_frobenius_square(n),
               sum((pair_grade(n,b)-pair_grade(n,a))**2 for a,b in edges)*2)
        self.assertEqual(counterfeit_commutator_no_witness(),(0,8))

    def test_pure_gauge_flat_plaquettes(self):
        for n in range(3,80):
            for d in range(n-3):
                self.assertEqual(plaquette_holonomy(pair_grade(n,d),
                    pair_grade(n,d+1),pair_grade(n+1,d+1),pair_grade(n+1,d)),0)

if __name__ == '__main__': unittest.main()
