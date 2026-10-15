"""Exact independent controls for ambient/wild SUCC source logic."""
import unittest
from fractions import Fraction as Q
from itertools import product
from observational_succ.wild_ambient_succ import (
    AmbientError, SourceFrame, SquareDisk, RectangularThread,
    certified_linking, intrinsic_octahedron, alexander_imported_complement,
    reduce_free, commutator, inverse_word, exponent_vector, expand_stage,
    expand_root, commutator_tower_receipt, a5, ID, compose, invert,
    group_commutator, a5_commutator_witnesses, a5_tower_assignment,
    abelian_character_of_expanded_root, covering_monodromy, cyclic_lift,
    solenoid_cohomology_class, intrinsic_vs_ambient_observer,
    evidence_contract, reflection_positive_no_go,
    compressed_flat_operator_control,a5_holonomy_energy_sign_control,
    a5_conjugacy_invariant_observer,
    generated_a5_subgroup, alexander_a5_finite_quotient,
)

FRAME=SourceFrame('original_Z3_embedding',4,'integer_xyz',1)


class FiniteAmbientLink(unittest.TestCase):
    def disk(self, radius=2, orientation=1):
        return SquareDisk(Q(radius),orientation,FRAME)
    def thread(self,y0,y1,height=1,orientation=1):
        return RectangularThread(Q(y0),Q(y1),Q(height),orientation,FRAME)

    def test_exact_hopf_signed_intersection(self):
        r=certified_linking(self.disk(),self.thread(1,3))
        self.assertEqual(r['linking'],-1)
        self.assertEqual(r['crossings'][0]['xy'],(Q(),Q(1)))
        self.assertEqual(r['crossings'][0]['crossing'],-1)

    def test_exact_unlink_contrast(self):
        self.assertEqual(certified_linking(self.disk(),self.thread(3,5))['linking'],0)
        self.assertEqual(certified_linking(self.disk(),self.thread(-1,1))['linking'],0)
        self.assertEqual(certified_linking(self.disk(),self.thread(-3,3))['linking'],0)

    def test_orientation_sign_vs_absolute_linking(self):
        a=certified_linking(self.disk(),self.thread(1,3))
        b=certified_linking(self.disk(),self.thread(1,3,orientation=-1))
        c=certified_linking(self.disk(orientation=-1),self.thread(1,3))
        self.assertEqual((a['linking'],b['linking'],c['linking']),(-1,1,1))
        self.assertEqual((a['absolute_linking'],b['absolute_linking'],c['absolute_linking']),(1,1,1))

    def test_homothetic_coordinates_are_invariant(self):
        for k in (Q(1,2),Q(1),Q(2),Q(5)):
            self.assertEqual(certified_linking(self.disk(2*k),self.thread(k,3*k,k))['linking'],-1)

    def test_finite_many_exact_mutations(self):
        disk=self.disk()
        for l,r in product(range(-4,5), repeat=2):
            if l>=r or abs(l)==2 or abs(r)==2:continue
            value=certified_linking(disk,self.thread(l,r))['linking']
            # Independent count of the two oriented perpendicular crossings.
            self.assertEqual(value, int(-2<r<2)-int(-2<l<2))

    def test_boundary_contact_is_rejected(self):
        for bad in (-2,2):
            with self.assertRaises(AmbientError):certified_linking(self.disk(),self.thread(bad,5))

    def test_wrong_provenance_epoch_basis_orientation_rejected(self):
        d=self.disk()
        for bad in (SourceFrame('other',4,'integer_xyz'),SourceFrame('original_Z3_embedding',5,'integer_xyz'),
                    SourceFrame('original_Z3_embedding',4,'new_coordinates'),SourceFrame('original_Z3_embedding',4,'integer_xyz',-1)):
            with self.assertRaises(AmbientError):certified_linking(d,RectangularThread(1,3,1,1,bad))

    def test_floating_precision_and_invalid_frames_are_rejected(self):
        for maker in (lambda:SquareDisk(2.0,1,FRAME),lambda:RectangularThread(1,3.0,1,1,FRAME),
                      lambda:SourceFrame('x',True,'b'), lambda:SourceFrame('x',0,'b',0)):
            with self.assertRaises(AmbientError):maker()


class PerfectCommutatorTower(unittest.TestCase):
    def test_reduced_free_group_normal_form(self):
        self.assertEqual(reduce_free((1,2,-2,-1,3,-3,4)),(4,))
        self.assertEqual(inverse_word((1,2,-3)),(3,-2,-1))
        self.assertEqual(commutator((1,),(2,)),(1,2,-1,-2))

    def test_exact_word_length_and_zero_abelianization(self):
        for n in range(1,7):
            a=commutator_tower_receipt(n)
            self.assertEqual(a['word_length'],4**n)
            self.assertTrue(a['free_reduced_nonidentity'])
            self.assertTrue(a['abelian_image_zero'])

    def test_independent_recursive_and_stagewise_expansions(self):
        def independently(i,j,limit):
            if j==limit:return (i+1,)
            x=independently(2*i,j+1,limit)
            y=independently(2*i+1,j+1,limit)
            return x+y+tuple(-k for k in reversed(x))+tuple(-k for k in reversed(y))
        for n in range(5):
            self.assertEqual(expand_root(n),independently(0,0,n))

    def test_short_words_survive_injective_stage_maps(self):
        # Finite adversarial calibration only; general injectivity is proved by free-product normal form.
        for stage in range(3):
            rank=2**stage
            alphabet=tuple(range(1,rank+1))+tuple(-i for i in range(1,rank+1))
            for length in range(1,4):
                for word in product(alphabet,repeat=length):
                    w=reduce_free(word)
                    if w:self.assertTrue(expand_stage(w,stage))

    def test_invalid_word_and_cost_rejected(self):
        for op in (lambda:expand_root(10),lambda:expand_root(-1),lambda:expand_stage((2,),0),
                   lambda:exponent_vector((4,),2),lambda:reduce_free((1,0,-1)),lambda:expand_root(3.0)):
            with self.assertRaises(AmbientError):op()

    def test_a5_group_size_and_commutator_map_is_onto(self):
        self.assertEqual(len(a5()),60)
        tab=a5_commutator_witnesses()
        self.assertEqual(set(tab),set(a5()))
        for p,(left,right) in tab.items():
            self.assertEqual(group_commutator(left,right),p)
        self.assertEqual(compose(p:=a5()[5],invert(p)),ID)

    def test_orthogonal_permutation_oracle(self):
        elements=a5()
        for p,q in product(elements[::5],elements[::7]):
            # Independent action of permutations on a five-symbol state vector.
            v=list(range(5))
            v1=[v[q[i]] for i in range(5)]
            v2=[v1[p[i]] for i in range(5)]
            # v2 applies p then q to observations; evaluate direct composite carefully.
            self.assertEqual(tuple(v2),compose(q,p))

    def test_finite_a5_representation_of_arbitrarily_deep_tower(self):
        for depth in range(7):
            o=a5_tower_assignment(depth)
            self.assertEqual(o['per_level_counts'],tuple(2**k for k in range(depth+1)))
            self.assertTrue(o['root_detected'] and o['all_edge_relations'])
            self.assertFalse(o['representation_of_actual_alexander_exterior_proved'])
            self.assertTrue(o['representation_derived_using_imported_Hatcher_pi1_theorem'])

    def test_independent_word_evaluation_matches_A5_root(self):
        root=(1,2,0,3,4)
        lookup=a5_commutator_witnesses()
        for depth in range(5):
            levels=[(root,)]
            for _ in range(depth):
                levels.append(tuple(c for v in levels[-1] for c in lookup[v]))
            leaves=levels[-1]
            def eval_w(w):
                result=ID
                for signed in w:
                    val=leaves[abs(signed)-1]
                    result=compose(result,val if signed>0 else invert(val))
                return result
            self.assertEqual(eval_w(expand_root(depth)),root)

    def test_every_abelian_character_is_blind(self):
        for n in range(1,6):
            for modulus in (2,3,5,7,17):
                self.assertEqual(abelian_character_of_expanded_root(n,modulus),0)
                weighted=tuple((5*i+3)%modulus for i in range(2**n))
                self.assertEqual(abelian_character_of_expanded_root(n,modulus,weighted),0)

    def test_a5_nonabelian_trace_survives_all_basepoint_conjugations(self):
        o=a5_conjugacy_invariant_observer()
        self.assertEqual((o['root_trace'],o['identity_trace']),(2,5))
        self.assertTrue(o['all_60_conjugations_certified'])
        self.assertTrue(o['class_detects_nonidentity'])
        self.assertFalse(o['real_world_instrument_authentication'])

    def test_four_stage_two_loops_surject_onto_A5(self):
        cert=alexander_a5_finite_quotient()
        self.assertTrue(cert['stage_two_is_surjective'])
        self.assertEqual(cert['stage_two_generated_subgroup_order'],60)
        self.assertEqual(len(cert['stage_two_generators']),4)
        self.assertFalse(cert['actual_wild_geometry_simulated'])

    def test_independent_stage_two_subgroup_oracle_and_negative_controls(self):
        cert=alexander_a5_finite_quotient()
        values={ID}
        seeds=list(cert['stage_two_generators'])
        for _ in range(70):
            nxt=values|{compose(a,b) for a in values for b in seeds}
            if nxt==values:break
            values=nxt
        self.assertEqual(values,set(a5()))
        self.assertEqual(len(generated_a5_subgroup((ID,))),1)
        self.assertEqual(len(generated_a5_subgroup((cert['root'],))),3)
        with self.assertRaises(AmbientError):generated_a5_subgroup(((0,1,2,3,3),))

    def test_mutated_commutator_relation_detected(self):
        root=(1,2,0,3,4)
        l,r=a5_commutator_witnesses()[root]
        self.assertNotEqual(group_commutator(r,l),root)
        self.assertEqual(group_commutator(r,l),invert(root))

    def test_restricted_observer_access_protected(self):
        frame=SourceFrame('abstract_commutator_group',0,'permutation_basis')
        for kind in ('external_Alexander','arith_Weil'):
            with self.assertRaises(AmbientError): evidence_contract(frame,kind,('abstract_A5',))
        self.assertEqual(evidence_contract(frame,'abstract_A5',('abstract_A5',))['kind'],'abstract_A5')


class GlobalTopologyAndRHFirewalls(unittest.TestCase):
    def test_intrinsic_sphere_does_not_determine_ambient_complement(self):
        m=intrinsic_octahedron(); a=alexander_imported_complement(); c=intrinsic_vs_ambient_observer()
        self.assertEqual((m['vertices'],m['edges'],m['faces'],m['euler']),(6,12,8,2))
        self.assertEqual(a['alexander_exterior_H1'],'zero')
        self.assertEqual(a['alexander_exterior_pi1'],'nontrivial_perfect')
        self.assertTrue(c['identical_intrinsic_S2'] and c['different_ambient_exterior'])
        self.assertTrue(a['commutator_tower_is_classical_exterior_pi1_via_Hatcher'])
        self.assertTrue(a['actual_A5_quotient_via_imported_topology'])
        self.assertFalse(a['actual_geometric_horns_constructed'] or c['topology_implies_Weil_positivity'])

    def test_coverage_and_orientation_of_nontrivial_cyclic_covers(self):
        for deg in range(2,11):
            for winding in range(-12,13):
                m=covering_monodromy(deg,winding)
                self.assertEqual(m['trivial'],winding%deg==0)
                self.assertEqual(set(m['sheet_permutation']),set(range(deg)))
                self.assertFalse(m['global_continuous_section_exists'])

    def test_all_finite_rational_lifts_exist_but_cannot_glue(self):
        for deg in range(2,8):
            for k in range(12):
                phase=Q(k,12)
                self.assertEqual(deg*cyclic_lift(phase,deg),phase)
            # At 0 and 1, two real representatives of the SAME circle point,
            # the naive real branch disagrees by 1/deg modulo 1.
            self.assertNotEqual(cyclic_lift(Q(),deg),(Q(1)/deg)%1)

    def test_solenoid_classes_and_degree_morphisms(self):
        for d in (2,3,5):
            for n in range(8):
                for z in (-6,-1,0,1,7):
                    self.assertEqual(solenoid_cohomology_class(z,n,d),
                                     solenoid_cohomology_class(d*z,n+1,d))
            self.assertEqual(solenoid_cohomology_class(1,1,d),Q(1,d))
            self.assertNotEqual(solenoid_cohomology_class(1,1,d).denominator,1)

    def test_false_source_reflection_does_not_force_psd(self):
        a=reflection_positive_no_go()
        self.assertTrue(a['reflection_invariant'] and a['commutes'])
        self.assertLess(a['odd_rayleigh'],0)
        self.assertFalse(a['PSD_forced_by_reflection'] or a['Weil_identification'])

    def test_projected_commutator_is_not_ambient_curvature(self):
        r=compressed_flat_operator_control()
        self.assertTrue(r['full_commutator_zero'])
        self.assertTrue(r['exact_boundary_leakage_identity'])
        self.assertEqual(r['compressed_commutator'],((0,-1,0),(1,0,0),(0,0,0)))
        self.assertFalse(r['projection_commutator_proves_real_wild_embedding'])

    def test_nonabelian_holonomy_psd_does_not_force_signed_form(self):
        r=a5_holonomy_energy_sign_control()
        self.assertTrue(r['root_nonidentity'])
        self.assertTrue(r['fixed_constant_vector'])
        self.assertTrue(r['connection_energy_nonnegative'])
        self.assertEqual(r['source_signed_toy_form'],-5)
        self.assertFalse(r['full_Weil_form_identified'])

    def test_wrong_degree_or_source_rejected(self):
        for op in (lambda:covering_monodromy(1,1),lambda:covering_monodromy(3,0.5),
                   lambda:cyclic_lift(Q(1),2),lambda:solenoid_cohomology_class(1,0,1),
                   lambda:solenoid_cohomology_class(1,1.5,2),lambda:a5_tower_assignment(13)):
            with self.assertRaises(AmbientError):op()

if __name__=='__main__':unittest.main()
