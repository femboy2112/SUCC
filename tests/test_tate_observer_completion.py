"""Source-typed finite model-of-model → p-adic Fourier and global-limit controls."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.tate_observer_completion import (
    AtomicDescentError, StageCharacter, factorial_observer_moduli,
    reconstruct_from_model_models, integer_source_prefix,
    ghost_profinite_residue, profinite_ghost_prefix, embed_cyclotomic,
    normal_fourier_naturality, PadicBruhatChart,
    local_tate_fourier, tate_local_inversion_and_parseval,
    refine_local_precision, refine_local_support,
    local_padic_real_boundary_no_go, exact_local_biaxial_diamond,
    exact_crt_product_fourier,
)
from observational_succ.finite_fourier_carrier import CyclotomicElement


class AtomicFiniteObserverDualityTests(unittest.TestCase):
    def test_all_finite_algebra_characters_are_unique_stage_evaluations(self):
        for modulus in (2,3,4,6,8,12,24):
            for residue in range(modulus):
                c=StageCharacter.evaluation(modulus,residue)
                self.assertEqual(c.reconstructed_residue,residue)
                for k in range(modulus):
                    self.assertEqual(c.evaluate(tuple(int(j==k) for j in range(modulus))),
                                     int(residue==k))
                self.assertEqual(c.evaluate(tuple(Q(3*i-1,7) for i in range(modulus))),
                                 Q(3*residue-1,7))

    def test_recursive_model_algebra_exact_source_growth(self):
        self.assertEqual(factorial_observer_moduli(4),(2,6,24,120))
        for source in (-211,-51,-1,0,1,7,24,211):
            r=integer_source_prefix(source,4)
            self.assertEqual(r.moduli,(2,6,24,120))
            self.assertEqual(r.residues,tuple(source%m for m in r.moduli))
            self.assertEqual(r.compatible_idempotent_tests,2+6+24)
            self.assertFalse(r.entire_infinite_inverse_limit_constructed_by_finite_code)
            self.assertFalse(r.actual_integer_source_authenticated)
            self.assertFalse(r.archimedean_completed)
            self.assertFalse(r.RH_proved)

    def test_coarse_observation_alias_repaired_by_fine_lawful_probe(self):
        one=StageCharacter.evaluation(4,1)
        three=StageCharacter.evaluation(4,3)
        self.assertEqual(one.project_to(2),three.project_to(2))
        self.assertNotEqual(one,three)
        self.assertEqual(one.evaluate((0,1,0,0)),1)
        self.assertEqual(three.evaluate((0,1,0,0)),0)

    def test_profinite_point_coherent_but_no_original_integer_source(self):
        prefix=profinite_ghost_prefix(4)
        self.assertEqual(prefix.residues,(1,3,9,105))
        for n in (2,6,24,120,720):
            r=ghost_profinite_residue(n)
            self.assertEqual(r%(2**((n & -n).bit_length()-1)),1%(n&-n))
            odd=n//(n&-n)
            self.assertEqual(r%odd,0)
        self.assertEqual(prefix.source_tag,"CRT_COHERENT_NONINTEGER_PROFINITE_POINT")
        # The theorem uses ALL 3^k coordinates, not a finite 4-stage disproof.
        self.assertFalse(prefix.actual_integer_source_authenticated)

    def test_higher_stage_not_lawful_if_source_models_disagree(self):
        with self.assertRaises(AtomicDescentError):
            reconstruct_from_model_models((
                StageCharacter.evaluation(2,1),
                StageCharacter.evaluation(6,0)))
        with self.assertRaises(AtomicDescentError):
            reconstruct_from_model_models((
                StageCharacter.evaluation(2,1),
                StageCharacter.evaluation(8,1),
                StageCharacter.evaluation(6,1)))
        with self.assertRaises(AtomicDescentError):
            StageCharacter(4,(Q(1,2),Q(1,2),0,0))
        with self.assertRaises(AtomicDescentError):
            StageCharacter(4,(1,1,0,0))
        with self.assertRaises(AtomicDescentError):
            StageCharacter(4,(0,0,0,0))
        with self.assertRaises(AtomicDescentError):
            StageCharacter.evaluation(4,True)

    def test_not_every_source_profile_is_a_quasi_ontic_witness(self):
        p=integer_source_prefix(17,3)
        q=profinite_ghost_prefix(3)
        self.assertEqual(p.moduli,q.moduli)
        self.assertTrue(p.exact_finite_snapshot)
        self.assertTrue(q.exact_finite_snapshot)
        self.assertFalse(p.actual_integer_source_authenticated)
        self.assertFalse(q.actual_integer_source_authenticated)
        self.assertNotEqual(p.residues,q.residues)


class ExactFourierObserverNaturality(unittest.TestCase):
    def test_finite_source_refinement_commutes_with_all_dual_frequencies(self):
        for m,n,values in (
            (2,4,(1,-1)),
            (2,6,(2,3)),
            (3,6,(1,2,-2)),
            (3,9,(1,-2,4)),
            (4,8,(1,0,2,-1)),
            (4,12,(0,3,-2,1)),
            (6,12,(0,2,-1,3,1,-2)),
            (6,24,(2,-1,0,3,1,-2)),
            (8,24,(1,0,2,0,-1,1,0,4)),
        ):
            receipt=normal_fourier_naturality(values,n)
            self.assertEqual(receipt["all_frequencies_checked"],n)
            self.assertEqual(receipt["dual_frequency_factor"],n//m)
            self.assertTrue(receipt["natural_Fourier_square"])
            self.assertFalse(receipt["composite_Euler_place_claimed"])
            self.assertFalse(receipt["RH_proved"])

    def test_root_embedding_preserves_cyclotomic_relation(self):
        for small,large in ((2,4),(3,6),(4,8),(6,24)):
            x=embed_cyclotomic(CyclotomicElement.root(small,1),large)
            self.assertEqual(x*x,embed_cyclotomic(CyclotomicElement.root(small,2),large))
            self.assertEqual(x*embed_cyclotomic(CyclotomicElement.root(small,small-1),large),
                             CyclotomicElement.scalar(large,1))

    def test_unrelated_observers_and_forged_phase_refused(self):
        with self.assertRaises(AtomicDescentError):
            normal_fourier_naturality((1,2,3),8)
        with self.assertRaises(AtomicDescentError):
            normal_fourier_naturality((True,2),4)
        with self.assertRaises(AtomicDescentError):
            normal_fourier_naturality((1,2),4.0)
        with self.assertRaises(AtomicDescentError):
            embed_cyclotomic(CyclotomicElement.root(4,1),6)


class LocalTateSchwartzBruhatChartTests(unittest.TestCase):
    def test_exact_original_self_dual_prime_unit_ball(self):
        for p in (2,3,5):
            c=PadicBruhatChart(p,0,1)
            # f=1_Zp on chart Zp/pZp; fhat=1_Zp in dual p^-1Zp/Zp
            values=(1,)*p
            spec=local_tate_fourier(c,values)
            self.assertEqual(spec[0],CyclotomicElement.scalar(p,1))
            self.assertTrue(all(z==CyclotomicElement.scalar(p,0) for z in spec[1:]))
            self.assertTrue(tate_local_inversion_and_parseval(c,values)["Plancherel_on_original_local_source"])

    def test_exact_dual_chart_of_zp_ball_with_both_support_descriptions(self):
        for p in (2,3,5):
            c=PadicBruhatChart(p,1,0)
            f=(1,)+(0,)*(p-1) # p^-1 a in Zp iff a divisible p
            spec=local_tate_fourier(c,f)
            self.assertTrue(all(z==CyclotomicElement.scalar(p,1) for z in spec))
            self.assertEqual(c.dual.support_depth,0)
            self.assertEqual(c.dual.precision_depth,1)
            self.assertTrue(tate_local_inversion_and_parseval(c,f)["Fourier_involution_reflection"])

    def test_exact_involution_reflection_and_parseval_on_nonsymmetric_tests(self):
        for p,r,s in ((2,0,2),(2,1,1),(2,2,0),(2,1,2),(2,2,1),
                      (3,0,1),(3,1,0),(3,1,1),(5,0,1),(5,1,0)):
            chart=PadicBruhatChart(p,r,s)
            n=chart.modulus
            v=tuple(Q((3*k*k+2*k-5)%11-4,k+1) for k in range(n))
            out=tate_local_inversion_and_parseval(chart,v)
            self.assertEqual(out["modulus"],n)
            self.assertTrue(out["Fourier_involution_reflection"])
            self.assertTrue(out["Plancherel_on_original_local_source"])
            self.assertFalse(out["adelic_global_Poisson_imported"])

    def test_exact_precision_and_support_refinements_both_commute(self):
        for p,r,s in ((2,0,1),(2,1,0),(2,1,1),(2,0,2),
                      (3,0,1),(3,1,0),(3,1,1)):
            c=PadicBruhatChart(p,r,s)
            if c.modulus*p>32:
                continue
            v=tuple(Q((k*k+3*k+1)%7-3,5) for k in range(c.modulus))
            left=refine_local_precision(c,v)
            right=refine_local_support(c,v)
            self.assertTrue(left["finite_Fourier_naturality"])
            self.assertTrue(right["finite_Fourier_naturality"])
            self.assertTrue(left["dual_frequency_support_included_exactly"])
            self.assertTrue(right["dual_periodicity_exact"])

    def test_incorrect_finite_haar_normalization_breaks_parseval(self):
        # p=2,r=1,s=0: dual cells have measure 1/2, not original cell 1.
        c=PadicBruhatChart(2,1,0)
        F=local_tate_fourier(c,(1,0))
        original=Q(1)
        true=sum((z*_conj_example(z) for z in F),
                 CyclotomicElement.scalar(2,0)).scale(c.dual.cell_Haar_volume)
        wrong=sum((z*_conj_example(z) for z in F),
                  CyclotomicElement.scalar(2,0)).scale(c.cell_Haar_volume)
        self.assertEqual(true,CyclotomicElement.scalar(2,original))
        self.assertNotEqual(wrong,true)

    def test_false_primitive_six_and_untyped_phase_rejected(self):
        for args in ((6,1,0),(1,1,0),(4,1,0),(2,0,0),
                     (2,-1,1),(2,1,-1),(2,6,1),(True,1,0),
                     (2,True,1),(2,1,True)):
            with self.assertRaises(AtomicDescentError):
                PadicBruhatChart(*args)
        c=PadicBruhatChart(2,1,1)
        with self.assertRaises(AtomicDescentError):
            local_tate_fourier(c,(0,1,2))
        with self.assertRaises(AtomicDescentError):
            local_tate_fourier(c,(0,1,2,0.25))

    def test_finite_model_cannot_reconstruct_real_archimedean_by_inverse_limit(self):
        w=local_padic_real_boundary_no_go()
        self.assertTrue(w["profinite_compact_and_totally_disconnected"])
        self.assertTrue(w["real_line_connected_and_noncompact"])
        self.assertFalse(w["real_is_pure_finite_inverse_limit"])
        self.assertFalse(w["finite_local_plus_Arch_Tate_completed"])
        self.assertFalse(w["RH_proved"])



class RecursiveTwoDimensionalObserverCoherenceTests(unittest.TestCase):
    def test_local_support_precision_biaxial_square_is_not_only_pairwise(self):
        for p,r,s in ((2,0,1),(2,1,0),(2,0,2),(2,1,1),(3,0,1),(3,1,0)):
            chart=PadicBruhatChart(p,r,s)
            v=tuple(Q((k*k+2*k-3)%7-3,5) for k in range(chart.modulus))
            result=exact_local_biaxial_diamond(chart,v)
            self.assertTrue(result["strict_source_diamond_commutes"])
            self.assertTrue(result["dual_Fourier_diamond_commutes"])
            self.assertEqual(result["all_terminal_cells_verified"],chart.p**2*chart.modulus)
            self.assertFalse(result["source_map_adequate_to_full_adele"])
            self.assertFalse(result["RH_proved"])
        with self.assertRaises(AtomicDescentError):
            exact_local_biaxial_diamond(PadicBruhatChart(3,1,1),(1,)*9) # 81 cells >32

    def test_crt_dual_pairing_requires_true_inverse_character_transport(self):
        for p,ep,q,eq,a,b in (
            (2,1,3,1,(1,-1),(2,0,-1)),
            (2,2,3,1,(1,-2,3,0),(1,2,-2)),
            (2,1,5,1,(1,2),(3,0,1,-1,2)),
            (3,1,2,2,(2,1,-1),(1,0,2,-2)),
            (3,1,5,1,(1,0,2),(0,1,-1,3,2)),
            (2,2,5,1,(0,-2,3,1),(3,1,0,-1,2)),
        ):
            result=exact_crt_product_fourier(p,ep,q,eq,a,b)
            self.assertTrue(result["exact_CRT_Fourier_product"])
            self.assertEqual(result["global_dual_frequencies_verified"],len(a)*len(b))
            self.assertEqual(result["actual_distinct_Euler_primes"],(p,q))
            self.assertTrue(result["joint_composite_modulus_not_a_primitive_Euler_place"])
            self.assertFalse(result["RH_proved"])
        # k must be carried to CRT dual inverse phase, not copied by coordinate.
        bad=exact_crt_product_fourier(2,1,3,1,(1,-1),(2,0,-1))
        self.assertGreater(bad["naive_frequency_transport_disagreement_count"],0)

    def test_crt_wrong_prime_and_source_tensor_mutants_rejected(self):
        for args in (
            (6,1,3,1,(1,)*6,(1,)*3),
            (2,1,2,1,(1,2),(1,2)),
            (2,1,3,1,(1,2,3),(1,0,2)),
            (2,1,3,1,(1,2),(1,2,0.5)),
            (2,2,11,1,(1,)*4,(1,)*11),
            (True,1,3,1,(1,2),(1,2,3)),
        ):
            with self.assertRaises(AtomicDescentError):
                exact_crt_product_fourier(*args)


def _conj_example(z:CyclotomicElement)->CyclotomicElement:
    t=CyclotomicElement.scalar(z.modulus,0)
    for j,c in enumerate(z.polynomial):
        t=t+CyclotomicElement.root(z.modulus,-j).scale(c)
    return t


if __name__=="__main__":
    unittest.main()
