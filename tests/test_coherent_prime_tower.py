"""Independent exact finite controls for the infinite positive-affine tower proof."""
from __future__ import annotations
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.coherent_prime_tower import (
    PAIRS, NORMALS, TowerContractError, level_size, arithmetic_digits,
    source_index, affine_endpoint, affine_cutoff, affine_coefficients,
    affine_adjoint_coefficients, prefix_composition_oracle, exit_defect,
    sample_dirichlet, inverse_dirichlet_samples, lattice_ray_cosets,
    ray_distance, encoded_basis, decoded_two_ray, boundary_affine,
    boundary_affine_adjoint, two_ray_mirror_numerators,
    encoded_refinement_oracle, source_boundary_exit, prime,
)


class ExactPositiveAffineTower(unittest.TestCase):
    def test_full_affine_semigroup_through_3_to_81(self):
        for level in (1, 2, 3, 4):
            for a,b,c,d in product((1,2,3,5), (0,1,2), (1,2,3), (0,1,3)):
                self.assertEqual(prefix_composition_oracle(level,a,b,c,d),3**level)

    def test_succ_prime_braid_exact_each_level(self):
        for level in range(1,6):
            for p in (2,3,5,7):
                self.assertEqual(prefix_composition_oracle(level,p,0,1,1),3**level)

    def test_different_primes_and_succ_powers_commute_correctly(self):
        for level in range(1,4):
            N=level_size(level)
            for p,q in product((2,3,5),(2,3,5)):
                for n in range(1,N+1):
                    a=affine_cutoff(n,level,p*q,0)
                    b=affine_cutoff(n,level,q*p,0)
                    self.assertEqual(a,b)
            for a,b in product(range(5),repeat=2):
                self.assertEqual(prefix_composition_oracle(level,1,a,1,b),N)

    def test_finite_matrix_action_and_adjoint_are_honest(self):
        for level in (1,2,3):
            N=level_size(level)
            vec=tuple(F((i*7+3)%11-5,i+1) for i in range(N))
            for a,b in ((1,1),(2,0),(3,0),(2,5),(1,0)):
                w=affine_coefficients(vec,a,b)
                z=affine_adjoint_coefficients(vec,a,b)
                expected=tuple(vec[(n-b)//a-1] if (n-b)%a==0 and n>b and (n-b)//a>=1 else F()
                               for n in range(1,N+1))
                self.assertEqual(w,expected)
                expected_adj=tuple(vec[a*n+b-1] if a*n+b<=N else F()
                                   for n in range(1,N+1))
                self.assertEqual(z,expected_adj)
                self.assertEqual(sum((x*y for x,y in zip(w,vec)),F()),
                                 sum((x*y for x,y in zip(vec,z)),F()))

    def test_prefix_inclusion_has_exact_boundary_exit_not_strict_naturality(self):
        for k in (1,2,3):
            N=3**k
            data=source_boundary_exit(k,1,1)
            self.assertIn((N,N+1),data['witnesses'])
            self.assertEqual(data['operator_norm'],1)
            self.assertFalse(data['operator_norm_convergence_claimed'])
            for n,f in data['witnesses']:
                self.assertTrue(N<f<=3*N)
            self.assertIn((N,2*N),exit_defect(k,2,0))

    def test_no_source_reentry_for_positive_affine_maps_but_adjoint_defect(self):
        for level in (1,2,3):
            N=3**level
            self.assertIsNone(affine_cutoff(N,level,1,1))
            self.assertEqual(affine_coefficients((F(),)*(N-1)+(F(1),),1,1),(F(),)*N)
            self.assertEqual(affine_adjoint_coefficients((F(1),)+(F(),)*(N-1),1,1),(F(),)*N)
            self.assertFalse(affine_coefficients((F(1),)+(F(),)*(N-1),2,0)==(F(),)*N)

    def test_source_must_be_authenticated_exact_and_well_typed(self):
        self.assertTrue(prime(2) and prime(3))
        self.assertFalse(prime(4) or prime(True))
        for inp in ((F(1),3.2),):
            with self.assertRaises(TowerContractError):
                affine_coefficients(inp,1,1)
        with self.assertRaises(TowerContractError):
            affine_cutoff(True,1,1,1)
        with self.assertRaises(TowerContractError):
            arithmetic_digits(0,2)
        with self.assertRaises(TowerContractError):
            affine_endpoint(3,0,0)


class ExactAnalyticTower(unittest.TestCase):
    def test_base3_digits_source_bijection_and_refinement(self):
        for level in range(1,5):
            N=level_size(level)
            decoded={source_index(arithmetic_digits(n,level)) for n in range(1,N+1)}
            self.assertEqual(decoded,set(range(1,N+1)))
            if level<4:
                for n in range(1,N+1):
                    self.assertEqual(arithmetic_digits(n,level+1),
                                     arithmetic_digits(n,level)+(0,))

    def test_finite_exact_analytic_samples_and_inversion(self):
        for level in (1,2):
            N=level_size(level)
            vec=tuple(F((i*5+1)%7-3,i+1) for i in range(N))
            samples=sample_dirichlet(vec)
            self.assertEqual(inverse_dirichlet_samples(samples),vec)
            for a,b in ((1,1),(2,0),(3,0)):
                self.assertEqual(inverse_dirichlet_samples(sample_dirichlet(
                    affine_coefficients(vec,a,b))),affine_coefficients(vec,a,b))

    def test_analytic_evaluation_commutes_with_source_zero_extension(self):
        for level in (1,2):
            N=level_size(level)
            vec=tuple(F((-1)**n,n) for n in range(1,N+1))
            extended=vec+(F(),)*(2*N)
            self.assertEqual(sample_dirichlet(extended,exponents=N),
                             sample_dirichlet(vec))


class ExactPadicGeometry(unittest.TestCase):
    def test_three_2adic_lattice_rays_are_nested_actual_classes(self):
        for branch in range(3):
            for depth in range(1,6):
                points=lattice_ray_cosets(depth,branch)
                self.assertEqual(len(points),2**depth)
                self.assertIn((0,0),points)
                if depth>1:
                    prior=lattice_ray_cosets(depth-1,branch)
                    mask=2**(depth-1)
                    self.assertEqual({(x%mask,y%mask) for x,y in points},prior)
        self.assertEqual(len(set(lattice_ray_cosets(1,i) for i in range(3))),3)
        self.assertEqual(NORMALS,((1,0),(0,1),(1,1)))

    def test_ray_distances_and_geometry_selection_are_explicit(self):
        for a,b in product(range(3),repeat=2):
            for r,s in product(range(1,5),repeat=2):
                d=ray_distance(a,r,b,s)
                self.assertEqual(d,abs(r-s) if a==b else r+s)
                self.assertEqual(d,ray_distance(b,s,a,r))
        self.assertEqual(ray_distance(0,0,2,5),5)
        with self.assertRaises(TowerContractError):
            lattice_ray_cosets(0,1)


class ExactCodeTower(unittest.TestCase):
    def test_level_k_code_is_isometry_and_nested_with_bell_vacuum(self):
        for level in (1,2,3):
            N=level_size(level)
            words=[set(encoded_basis(level,n)) for n in range(1,N+1)]
            self.assertTrue(all(len(v)==N for v in words))
            self.assertEqual(len(set.union(*words)),N*N)
            self.assertTrue(all(not(words[i]&words[j]) for i in range(N)
                                for j in range(i+1,N)))
            if level<3:
                for n in range(1,N+1):
                    self.assertEqual(encoded_refinement_oracle(level,n),(3*N,True))

    def test_any_pair_reconstructs_all_logical_basis_and_all_ancilla(self):
        for level in (1,2,3):
            N=level_size(level)
            for pair in PAIRS:
                lost=({0,1,2}-set(pair)).pop()
                for n in range(1,N+1):
                    seen=set()
                    for word in encoded_basis(level,n):
                        ds,ks=decoded_two_ray(pair,word)
                        self.assertEqual(source_index(ds),n)
                        self.assertEqual(ks,word[lost])
                        seen.add(ks)
                    self.assertEqual(len(seen),N)

    def test_arithmetic_ops_are_two_ray_boundary_reconstructible(self):
        for level in (1,2,3):
            for pair in PAIRS:
                for n in range(1,level_size(level)+1):
                    for word in encoded_basis(level,n):
                        for a,b in ((1,1),(2,0),(3,0),(1,2),(2,1)):
                            src=affine_cutoff(n,level,a,b)
                            image=boundary_affine(pair,word,a,b)
                            if src is None:
                                self.assertIsNone(image)
                            else:
                                self.assertIn(image,encoded_basis(level,src))
                                missing=({0,1,2}-set(pair)).pop()
                                self.assertEqual(image[missing],word[missing])
                                self.assertEqual(boundary_affine_adjoint(pair,image,a,b),word)

    def test_boundary_braid_on_full_computational_bases_not_only_code(self):
        level=2
        for pair in PAIRS:
            for visible0,visible1 in product(product(range(3),repeat=2),repeat=2):
                word=[(0,0)]*3
                word[pair[0]]=visible0
                word[pair[1]]=visible1
                word=tuple(word)
                for p in (2,3,5):
                    after_s=boundary_affine(pair,word,1,1)
                    lhs=boundary_affine(pair,after_s,p,0) if after_s else None
                    after_p=boundary_affine(pair,word,p,0)
                    rhs=boundary_affine(pair,after_p,1,p) if after_p else None
                    self.assertEqual(lhs,rhs)

    def test_two_sided_thermal_mirror_exact_at_three_and_nine(self):
        for level in (1,2):
            for beta in (2,4):
                for p in (2,3,5):
                    for lp,rp in product(PAIRS,repeat=2):
                        left,right=two_ray_mirror_numerators(level,p,lp,rp,beta_even=beta)
                        self.assertEqual(left,right,(level,beta,p,lp,rp))
                        self.assertEqual(len(left),((3**level)//p)*(3**(2*level)))

    def test_nondiagonal_logical_density_two_ray_erasure_is_exact(self):
        for level in (1,2):
            N=level_size(level)
            second=min(N,4)
            rho={(1,1):F(1,2),(second,second):F(1,2),
                 (1,second):F(1,4),(second,1):F(1,4)}
            for pair in PAIRS:
                missing=({0,1,2}-set(pair)).pop()
                reduced={}
                for (i,j),coeff in rho.items():
                    for a in encoded_basis(level,i):
                        for b in encoded_basis(level,j):
                            if a[missing]==b[missing]:
                                key=(tuple(a[r] for r in pair),
                                     tuple(b[r] for r in pair))
                                reduced[key]=reduced.get(key,F())+coeff/N
                for (a,b),val in reduced.items():
                    ds_a,ka=decoded_two_ray(pair,tuple(
                        a[pair.index(r)] if r in pair else (0,)*level
                        for r in range(3)))
                    ds_b,kb=decoded_two_ray(pair,tuple(
                        b[pair.index(r)] if r in pair else (0,)*level
                        for r in range(3)))
                    i,j=source_index(ds_a),source_index(ds_b)
                    self.assertEqual(val,rho.get((i,j),F())/N if ka==kb else F())
                self.assertEqual(len([v for v in reduced.values() if v]),4*N)

    def test_fixed_source_operator_eventually_reappears_after_boundary_exit(self):
        self.assertIsNone(affine_cutoff(3,1,1,1))
        for level in (2,3):
            self.assertEqual(affine_cutoff(3,level,1,1),4)
            for pair in PAIRS:
                for word in encoded_basis(level,3):
                    self.assertIn(boundary_affine(pair,word,1,1),encoded_basis(level,4))

    def test_arbitrary_code_placement_has_no_canonical_geometry(self):
        self.assertNotEqual(ray_distance(0,1,1,1),ray_distance(0,4,1,1))
        for level in (2,3):
            self.assertEqual(len(encoded_basis(level,1)),len(encoded_basis(level,level_size(level))))

    def test_mutant_two_leg_code_does_not_recover_every_erasure(self):
        def mutant(i):
            return tuple((j,(j+i)%3,(j+i)%3) for j in range(3))
        observed1={(a[1],a[2]) for a in mutant(0)}
        observed2={(a[1],a[2]) for a in mutant(1)}
        self.assertEqual(observed1,observed2)

    def test_no_uniform_bounded_depth_local_representation_even_for_prime_actions(self):
        for r in range(1,4):
            n=3**r
            k=r+3
            source=arithmetic_digits(n,k)
            for a,b in ((1,1),(2,0),(3,0),(5,0),(7,0),(11,0)):
                dest=affine_endpoint(n,a,b)
                target=arithmetic_digits(dest,k)
                changed=[j for j in range(r,k) if source[j]!=target[j]]
                self.assertTrue(changed,(n,a,b,source,target))
                j=changed[0]
                from observational_succ.arithmetic_epr_star import codeword
                self.assertFalse(set(codeword(source[j]))&set(codeword(target[j])))

    def test_explicit_source_tail_error_budget_for_beta2_prime_shift(self):
        for k,p in ((2,2),(3,2),(3,3)):
            N=level_size(k)
            M=N//p
            source=tuple(F(1,n) for n in range(1,2*N+1))
            true={p*n:source[n-1] for n in range(1,len(source)+1)}
            cutoff={p*n:source[n-1] for n in range(1,len(source)+1) if p*n<=N}
            residual=sum(((true.get(y,F())-cutoff.get(y,F()))**2
                          for y in set(true)|set(cutoff)),F())
            tail=sum((source[n-1]**2 for n in range(M+1,len(source)+1)),F())
            self.assertLessEqual(residual,4*tail)

    def test_finite_depth_cannot_implement_full_S_or_Vp_with_norm_convergence(self):
        for level in range(1,6):
            N=level_size(level)
            self.assertIsNone(affine_cutoff(N,level,1,1))
            self.assertEqual(affine_endpoint(N,1,1),N+1)
            self.assertEqual(source_boundary_exit(level,1,1)['operator_norm'],1)


if __name__=='__main__':
    unittest.main()
