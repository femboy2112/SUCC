"""Exact hostile checks for finite gauge L2 / SUCC graph-quantum duality.

No test here asserts 4D continuum YM, Wightman axioms, or a mass gap.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.ym_quantum_graph_duality import (
    QuantumGaugeError, FiniteGaugeGroup, cyclic_group, s3_group,
    HaarSubdivision, gauge_invariant_density_not_physical,
    new_cycle_haar_detail, conditional_haar_energy,
    simultaneous_conjugacy_orbits, burnside_conjugation_orbits,
    z2_plaquette_gauge_transform, z2_electric_magnetic_apply,
    z2_physical_matrix, physical_spectral_receipt,
    path_sum, finite_reflection_gram, toy_wilson_factor_graph,
    two_plaquette_source_transport, subdivision_edge_mode_entanglement,
    haar_poincare_transfer,
)
from observational_succ.yang_mills_gauge_oracle import (
    S3_ELEMENTS, compose_s3, s3_subdivision_square, nonabelian_trace_counterexample,
)


class GroupAuthority(unittest.TestCase):
    def test_original_succ_s3_composition_is_used(self):
        g=s3_group()
        index={x:i for i,x in enumerate(S3_ELEMENTS)}
        self.assertEqual(g.order,6)
        for a,b in product(range(6),repeat=2):
            self.assertEqual(S3_ELEMENTS[g.mul(a,b)],compose_s3(S3_ELEMENTS[a],S3_ELEMENTS[b]))

    def test_mutated_tables_and_float_source_rejected(self):
        with self.assertRaises(QuantumGaugeError):
            FiniteGaugeGroup('bad',((0,1),(1,1)),0)
        with self.assertRaises(QuantumGaugeError):
            FiniteGaugeGroup('bad',((0,1),(0,1)),0)
        with self.assertRaises(QuantumGaugeError):
            cyclic_group(True)
        with self.assertRaises(QuantumGaugeError):
            cyclic_group(9)
        h=HaarSubdivision(cyclic_group(2))
        with self.assertRaises(QuantumGaugeError): h.pullback((0.5,0))
        with self.assertRaises(QuantumGaugeError): h.adjoint((0,1,2))
        with self.assertRaises(QuantumGaugeError): h.gauge_action((0,1,2,3),2)

    def test_nonabelian_ordered_path_associativity(self):
        g=s3_group()
        f=tuple(Q(i*i-3*i) for i in range(6))
        for a,b,c in product(range(6),repeat=3):
            left=f[g.mul(g.mul(a,b),c)]
            right=f[g.mul(a,g.mul(b,c))]
            self.assertEqual(left,right)
        # Reverse-path multiplication is not a harmless chart change.
        a,b=S3_ELEMENTS[1],S3_ELEMENTS[3]
        if compose_s3(a,b)==compose_s3(b,a):
            a,b=(1,0,2),(0,2,1)
        self.assertNotEqual(compose_s3(a,b),compose_s3(b,a))


class HaarQuantumBridge(unittest.TestCase):
    def test_isometry_adjoint_naturality_orthogonality_all_groups(self):
        for g in (cyclic_group(2),cyclic_group(3),s3_group()):
            m=g.order;h=HaarSubdivision(g)
            f=tuple(Q(i*i+2) for i in range(m))
            F=tuple(Q((i*17)%19-7,3) for i in range(m*m))
            receipt=h.exact_receipt(f,F)
            self.assertEqual(receipt['internal_gauge_invariant_dimension'],m)
            self.assertEqual(receipt['pure_gauge_detail_dimension'],m*(m-1))
            for k in range(m):
                self.assertEqual(h.gauge_action(h.project(F),k),h.project(F))
                self.assertEqual(h.project(h.gauge_action(F,k)),h.project(F))

    def test_projection_basis_exact_trace_rank_s3(self):
        h=HaarSubdivision(s3_group());m=6
        trace=Q()
        for i in range(m*m):
            basis=tuple(Q(int(j==i)) for j in range(m*m))
            P=h.project(basis)
            trace+=P[i]
            self.assertEqual(P,h.average(basis))
            self.assertEqual(h.adjoint(h.detail(basis)),(Q(),)*m)
        self.assertEqual(trace,m)

    def test_adjoint_is_unique_normalized_haar_fiber_average(self):
        g=s3_group();h=HaarSubdivision(g);m=g.order
        F=tuple(Q(i*i-5*i+9,7) for i in range(m*m))
        EF=h.adjoint(F)
        for x in range(m):
            independent=Q()
            count=0
            for a,b in product(range(m),repeat=2):
                if g.mul(a,b)==x:
                    independent+=F[a*m+b]
                    count+=1
            self.assertEqual(count,m)
            self.assertEqual(EF[x],independent/m)

    def test_pure_gauge_haar_detail_killed_by_projection(self):
        h=HaarSubdivision(cyclic_group(2))
        F=(Q(1),Q(1),Q(-1),Q(-1))
        self.assertEqual(h.project(F),(Q(),)*4)
        self.assertEqual(h.detail(F),F)
        self.assertEqual(h.inner(F,F),1)

    def test_density_twirling_does_not_impose_gauss_law(self):
        out=gauge_invariant_density_not_physical()
        self.assertEqual(out['density_trace'],'1')
        self.assertEqual(out['gauge_odd_vector_physical_norm'],'0')
        self.assertTrue(out['twirled_density_unchanged'])

    def test_gauge_invariant_positive_control(self):
        h=HaarSubdivision(cyclic_group(2))
        F=tuple(Q(1) if (a+b)%2==0 else Q(-1) for a in range(2) for b in range(2))
        self.assertEqual(h.project(F),F)
        self.assertEqual(h.detail(F),(Q(),)*4)

    def test_real_physical_cycle_detail_survives(self):
        out=new_cycle_haar_detail()
        self.assertEqual(out['physical_new_detail_dimension'],2)
        self.assertEqual(out['exhibited_detail_norm'],'1')

    def test_entanglement_is_tensor_factorization_dependent(self):
        for g in (cyclic_group(2),cyclic_group(3),s3_group()):
            out=subdivision_edge_mode_entanglement(g)
            self.assertEqual(Q(out['refined_link_factor_reduced_purity']),Q(1,g.order))
            self.assertEqual(out['coarse_pure_state_purity'],'1')
            self.assertEqual(out['Schmidt_rank'],g.order)

    def test_haar_word_energy_matches_independent_conditional_sum(self):
        for q,k in ((2,1),(3,1),(16,1),(2,3)):
            counts=tuple((i*i+7*i+4)%17 for i in range(q**(k+1)))
            got=conditional_haar_energy(counts,q,k)
            N=sum(counts)
            parents=[sum(counts[x*q:(x+1)*q]) for x in range(q**k)]
            independent=Q(q**(k+1),N*N)*sum(
                (Q(counts[x*q+a])-Q(parents[x],q))**2
                for x in range(q**k) for a in range(q))
            self.assertEqual(got['wavelet_detail_energy'],independent)
            self.assertEqual(got['E_child']-got['E_parent'],independent)

    def test_uniform_haar_zero_and_concentrated_countercontrol(self):
        self.assertEqual(conditional_haar_energy((1,1,1,1),2,1)['wavelet_detail_energy'],0)
        self.assertEqual(conditional_haar_energy((4,0,0,0),2,1)['wavelet_detail_energy'],2)
        with self.assertRaises(QuantumGaugeError):conditional_haar_energy((0,0,0,0),2,1)
        with self.assertRaises(QuantumGaugeError):conditional_haar_energy((1,1,1,False),2,1)
        with self.assertRaises(QuantumGaugeError):conditional_haar_energy((1,1),2,1)

    def test_joint_holonomy_quotient_11_and_trace_counterexample(self):
        g=s3_group()
        orbits=simultaneous_conjugacy_orbits(g,2)
        self.assertEqual(len(orbits),11)
        self.assertEqual(burnside_conjugation_orbits(g,2),11)
        self.assertEqual(sum(map(len,orbits)),36)
        self.assertEqual(sorted(x for orb in orbits for x in orb),sorted(product(range(6),repeat=2)))
        bad=nonabelian_trace_counterexample()
        self.assertEqual(bad['trace_first'],bad['trace_second_other'])
        self.assertNotEqual(bad['trace_product_control'],bad['trace_product_other'])


class ConstructiveHamiltonian(unittest.TestCase):
    def test_4_cycle_physical_gauge_orbits_have_8_states(self):
        for parity in (0,1):
            seen={x for x in range(16) if x.bit_count()%2==parity}
            self.assertEqual(len(seen),8)
            for k in range(4):
                self.assertEqual({z2_plaquette_gauge_transform(x,k) for x in seen},seen)

    def test_exact_gauge_hamiltonian_commutes_with_every_site_star(self):
        for lam in (Q(),Q(1,2),Q(2)):
            for basis_index in range(16):
                psi=tuple(Q(int(i==basis_index)) for i in range(16))
                source=z2_electric_magnetic_apply(psi,lam)
                for vertex in range(4):
                    U=tuple(psi[z2_plaquette_gauge_transform(x,vertex)] for x in range(16))
                    lhs=z2_electric_magnetic_apply(U,lam)
                    rhs=tuple(source[z2_plaquette_gauge_transform(x,vertex)] for x in range(16))
                    self.assertEqual(lhs,rhs)

    def test_exact_hamiltonian_from_graph_matches_matrix(self):
        self.assertEqual(z2_physical_matrix(),((Q(4),Q(-4)),(Q(-4),Q(6))))
        self.assertEqual(z2_physical_matrix(Q(0)),((Q(4),Q(-4)),(Q(-4),Q(4))))
        self.assertEqual(z2_physical_matrix(Q(3,2)),((Q(4),Q(-4)),(Q(-4),Q(7))))
        for l in (Q(),Q(1),Q(3,2)):
            M=z2_physical_matrix(l)
            for x,y in product(range(-3,4),repeat=2):
                form=x*(M[0][0]*x+M[0][1]*y)+y*(M[1][0]*x+M[1][1]*y)
                self.assertEqual(form,4*(x-y)**2+2*l*y*y)

    def test_spectral_discriminant_exact_but_not_continuum(self):
        got=physical_spectral_receipt(Q(1))
        self.assertEqual(got['trace'],'10')
        self.assertEqual(got['determinant'],'8')
        self.assertEqual(got['discriminant'],'68')
        self.assertFalse(got['continuum_mass_gap_claimed'])
        with self.assertRaises(QuantumGaugeError):z2_physical_matrix(-1)
        with self.assertRaises(QuantumGaugeError):z2_physical_matrix(0.1)

    def test_graph_path_sum_exact_for_signed_interference(self):
        H=z2_physical_matrix(Q(1))
        for steps in range(6):
            for bra,ket in [((1,0),(1,0)),((1,0),(0,1)),((1,1),(1,-1))]:
                self.assertIsInstance(path_sum(H,bra,ket,steps),Q)
        # Two opposite signed paths cancel in this 2x2 amplitude graph.
        A=((Q(1),Q(1)),(Q(1),Q(-1)))
        self.assertEqual(path_sum(A,(1,0),(0,1),2),Q())
        self.assertEqual(sum(abs(A[0][k]*A[k][1]) for k in range(2)),2)
        with self.assertRaises(QuantumGaugeError):path_sum(A,(1,0),(1,0),8)

    def test_independent_graph_hamiltonian_walk_expansion(self):
        H=z2_physical_matrix()
        # Off-diagonal -4 is exactly four distinct graph edge flips.
        self.assertEqual(H[0][1],-sum((Q(1) for _ in range(4)),Q()))
        self.assertEqual(path_sum(H,(1,0),(0,1),2),-40)
        self.assertEqual(path_sum(H,(1,0),(0,1),0),0)

    def test_positive_transfer_and_finite_reflection_gram(self):
        out=finite_reflection_gram()
        self.assertTrue(out['reflected_positive_by_factorization'])
        self.assertFalse(out['full_OS_QFT_claimed'])
        self.assertEqual(out['transfer_matrix'],[['3/4','1/4'],['1/4','5/8']])
        # Gram quadratic is a direct sum of two squares.
        gram=tuple(tuple(Q(x) for x in row) for row in out['gram'])
        for coeff in product(range(-2,3),repeat=3):
            form=sum((gram[i][j]*coeff[i]*coeff[j] for i in range(3) for j in range(3)),Q())
            self.assertGreaterEqual(form,0)

    def test_reflection_mutants_are_rejected_or_distinguished(self):
        # Direct Gram R_01=+1/4. Flipping its sign alone is not the same
        # authenticated transport, even when a PSD matrix could result.
        original=finite_reflection_gram()
        self.assertEqual(original['gram'][0][1],'1/4')
        for vectors in (((1,0),(0,1)),((1,1),(1,-1))):
            a=finite_reflection_gram(times=(0,1),test_vectors=vectors)
            self.assertTrue(a['reflected_positive_by_factorization'])
        with self.assertRaises(QuantumGaugeError):finite_reflection_gram(times=(0,1),test_vectors=((1,0),))
        with self.assertRaises(QuantumGaugeError):finite_reflection_gram(times=(0,1),test_vectors=((1,0),(0.5,1)))

    def test_haar_poincare_margin_has_distinct_cutoff_scaling(self):
        for n in (4,5,8,13,20):
            a=Q(1,n)
            strong=haar_poincare_transfer(a,"linear")
            weak=haar_poincare_transfer(a,"quadratic")
            self.assertEqual(Q(strong["physical_scale_normalized_margin"]),Q(1,2))
            self.assertEqual(Q(weak["physical_scale_normalized_margin"]),2*a)
            self.assertLessEqual(Q(weak["physical_scale_normalized_margin"]),Q(1,2))
            self.assertFalse(strong["actual_YM_source_bound"])
        with self.assertRaises(QuantumGaugeError):haar_poincare_transfer(Q(1,2))
        with self.assertRaises(QuantumGaugeError):haar_poincare_transfer(Q(1,8),"forged")

    def test_single_wilson_loop_factor_graph_vs_quotient(self):
        result=toy_wilson_factor_graph()
        self.assertEqual(result['Haar_normalized_partition'],'2')
        self.assertEqual(result['Gibbs_orbit_probabilities'],('3/4','1/4'))
        self.assertEqual(result['wilson_loop_expectation'],'1/2')
        self.assertFalse(result['interacting_law_is_Haar'])
        self.assertTrue(toy_wilson_factor_graph(Q(1),Q(1))['interacting_law_is_Haar'])

    def test_interacting_wilson_source_reuse_fails_while_haar_survives(self):
        result=two_plaquette_source_transport()
        self.assertEqual(result['source_transport_TV_defect'],'1/8')
        self.assertEqual(result['fine_product_pushforward'],('5/8','3/8'))
        self.assertEqual(result['fine_pushed_wilson_mean'],'1/4')
        self.assertFalse(result['bare_action_reuse_is_exact'])
        self.assertTrue(two_plaquette_source_transport(Q(1),Q(1))['bare_action_reuse_is_exact'])
        with self.assertRaises(QuantumGaugeError):two_plaquette_source_transport(Q(-1),Q(1))


if __name__=='__main__':
    unittest.main()
