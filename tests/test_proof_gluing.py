"""Exact finite guards and hostile controls; universal proofs live in the paper."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product as words

from observational_succ.proof_gluing import (
    ProofDebt, ProofGluingError, FiniteObject, LawfulOperation, CommutingSquare,
    SourceKernel, check_same_joint_law, CompressionStage, PositiveCompressionChain,
    kleene_level_receipt, adele_lift_obstruction,
)
from observational_succ.source_field_inverse_limits import (
    FieldSourcePassport, hidden_coordinate_phantom, noncompact_descending_field,
    remote_negative_sign_shadow, finite_kleene_tree_calibration,
)
from observational_succ.field_limit_trichotomy import (
    bounded_binary_turing_diagonal, kleene_source_tree_accepts,
    noncompact_escape_prefix, phantom_source_prefix,
)
from observational_succ.field_limit_compactness import finite_closed_cylinder_prefix
from observational_succ.swarm_categories import InstrumentArrow
from observational_succ.swarm_probability import StochasticInstrument
from observational_succ.recursive_operator_gluing import principal_minors
from observational_succ.source_field_gluing import (
    recursive_positive_gram_stage, exact_scalar_schur_gluing,
)
from observational_succ.tate_adele_quotient_descent import (
    LocalFractionalAdeleCell, FiniteAdeleCoset, add_cosets,
)
from observational_succ.complex_cauchy_edge import GaussianCauchyRoot2
from observational_succ.edge_carrier_reconstruction import RationalSpan
from observational_succ.finite_quotient_retract import FiniteQuotientRetract
from observational_succ.suzuki_moment_schur import parity_blocks, SchurSourceError


SOURCE = FieldSourcePassport("declared-source", "full-finite-tables", 7)


def silent(obj, table):
    return LawfulOperation(obj, obj, InstrumentArrow(
        obj.size, obj.size, table, ((),), ((),)*obj.size, 0))


def stage(rows, *, source=SOURCE, operator="declared-A", basis="coordinates"):
    return CompressionStage(source, operator, basis, rows)


def coordinate_inclusion(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n+1))


def independent_diagonal(index, steps):
    """Separate decoding and explicit marked-tape implementation, same numbering.

    A calibration bearing, not an independent universality proof.
    """
    diagonal = 0
    while (diagonal+1)*(diagonal+2)//2 <= index:
        diagonal += 1
    code = index-diagonal*(diagonal+1)//2
    states = diagonal-code+1
    choices = [0, 1] + [(write, move, nxt) for write in (0, 1)
                       for move in (-1, 1) for nxt in range(states)]
    table = []
    remainder = code
    for _ in range(2*states):
        remainder, digit = divmod(remainder, len(choices))
        table.append(choices[digit])
    ones, head, state_id = set(range(index)), 0, 0
    for _ in range(steps):
        instruction = table[2*state_id+int(head in ones)]
        if type(instruction) is int:
            return instruction
        write, move, state_id = instruction
        if write:
            ones.add(head)
        else:
            ones.discard(head)
        head += move
    return None


class TypedGrammarTests(unittest.TestCase):
    def setUp(self):
        self.obj = FiniteObject(SOURCE, "two-labelled-states", 2)
        self.flip = silent(self.obj, (1, 0))
        self.reset = silent(self.obj, (0, 0))

    def test_identity_and_associativity_reuse_existing_composer(self):
        identity = LawfulOperation.identity(self.obj)
        self.assertEqual(identity.then(self.flip), self.flip)
        self.assertEqual(self.flip.then(identity), self.flip)
        self.assertEqual(self.flip.then(self.reset).then(self.flip),
                         self.flip.then(self.reset.then(self.flip)))
        self.assertEqual(self.flip.then(self.reset).then(self.flip).instrument.transition, (1, 1))

    def test_exact_square_has_all_carrier_states(self):
        identity = LawfulOperation.identity(self.obj)
        square = CommutingSquare(self.flip, self.flip, identity, identity)
        self.assertEqual(square.unresolved_debts, (ProofDebt.SOURCE_IDENTIFICATION,))

    def test_identical_silent_reports_do_not_hide_noncommuting_carriers(self):
        with self.assertRaisesRegex(ProofGluingError, "source 0"):
            CommutingSquare(self.flip, self.reset, self.reset, self.flip)

    def test_identical_carriers_do_not_hide_changed_report_words(self):
        read = LawfulOperation(self.obj, self.obj,
                               InstrumentArrow(2, 2, (0, 1), ((0,), (1,)), ((0,), (1,)), 1))
        with self.assertRaisesRegex(ProofGluingError, "carrier/report"):
            CommutingSquare(read, self.flip, self.flip, read)

    def test_source_observer_epoch_and_named_carrier_guards(self):
        for wrong in (replace(SOURCE, source="phantom"), replace(SOURCE, epoch=8),
                      replace(SOURCE, observer="marginals-only")):
            other = FiniteObject(wrong, self.obj.carrier, 2)
            with self.assertRaises(ProofGluingError):
                LawfulOperation(self.obj, other, self.flip.instrument)
            with self.assertRaises(ProofGluingError):
                self.flip.then(silent(other, (1, 0)))
        other = replace(self.obj, carrier="different-basis-same-size")
        with self.assertRaises(ProofGluingError):
            self.flip.then(silent(other, (1, 0)))

    def test_missing_states_and_budget_cannot_certify(self):
        with self.assertRaises(ProofGluingError):
            LawfulOperation(self.obj, self.obj, InstrumentArrow.identity(1))
        for bad in (True, 0, 257):
            with self.assertRaises(ProofGluingError):
                FiniteObject(SOURCE, "bad-size", bad)
        with self.assertRaises(ProofGluingError):
            LawfulOperation.identity(True)

    def test_report_budget_checked_before_composition(self):
        letters = tuple((i,) for i in range(17))
        arrow = LawfulOperation(self.obj, self.obj,
                               InstrumentArrow(2, 2, (0, 1), letters, ((0,), (1,)), 1))
        with self.assertRaisesRegex(ProofGluingError, "budget"):
            arrow.then(arrow)


class ProbabilityCouplingTests(unittest.TestCase):
    def kernel(self, rows, *, source=SOURCE):
        return SourceKernel(source, StochasticInstrument(
            "coin-and-state", source.source, "bits", "bits", 2, rows))

    def test_equal_marginals_wrong_joint_coupling_is_rejected(self):
        correlated = (((0, 0, Q(1, 2)), (1, 1, Q(1, 2))),)*2
        anticorrelated = (((0, 1, Q(1, 2)), (1, 0, Q(1, 2))),)*2
        # Both report laws and both post-state laws are exactly uniform.
        for row in correlated[:1]+anticorrelated[:1]:
            self.assertEqual(tuple(sum(p for r, _, p in row if r == bit) for bit in (0, 1)),
                             (Q(1, 2), Q(1, 2)))
            self.assertEqual(tuple(sum(p for _, y, p in row if y == bit) for bit in (0, 1)),
                             (Q(1, 2), Q(1, 2)))
        with self.assertRaisesRegex(ProofGluingError, "coupling"):
            check_same_joint_law(self.kernel(correlated), self.kernel(anticorrelated))

    def test_order_and_split_mass_do_not_change_exact_joint_law(self):
        a = self.kernel((((0, 0, Q(1, 2)), (1, 1, Q(1, 2))),)*2)
        b = self.kernel((((1, 1, Q(1, 2)), (0, 0, Q(1, 4)), (0, 0, Q(1, 4))),)*2)
        self.assertIsNone(check_same_joint_law(a, b))
        self.assertEqual(a.unresolved_debts, (ProofDebt.SOURCE_IDENTIFICATION,))

    def test_joint_composition_retains_report_carrier_correlation(self):
        flip = self.kernel((((0, 1, 1),), ((1, 0, 1),)))
        read = self.kernel((((0, 0, 1),), ((1, 1, 1),)))
        result = flip.then(read)
        self.assertEqual(result.kernel.rows, ((((0, 1), 1, Q(1)),), (((1, 0), 0, Q(1)),)))
        stale = replace(read, source=replace(SOURCE, epoch=8))
        with self.assertRaisesRegex(ProofGluingError, "epoch"):
            flip.then(stale)
        with self.assertRaisesRegex(ProofGluingError, "epoch"):
            check_same_joint_law(read, stale)

    def test_kernel_label_must_match_passport(self):
        a = self.kernel((((0, 0, 1),),))
        with self.assertRaises(ProofGluingError):
            replace(a, source=replace(SOURCE, source="forged-origin"))


class PositivityTransportTests(unittest.TestCase):
    def test_decoder_domination_needs_one_uniform_constant(self):
        # O=diag(1/k), h=I. A fixed C=4 works through dimension 4.
        def domination(n):
            return stage(tuple(tuple(Q(16, (i+1)**2)-1 if i == j else Q()
                                     for j in range(n)) for i in range(n)),
                         operator="16 O*O - I", basis=f"first-{n}")
        chain = PositiveCompressionChain(tuple(domination(n) for n in range(1, 5)),
                                        tuple(coordinate_inclusion(n) for n in range(1, 4)))
        self.assertIn(ProofDebt.ALL_STAGE_POSITIVITY, chain.unresolved_debts)
        with self.assertRaisesRegex(ProofGluingError, "Negative principal minor"):
            PositiveCompressionChain((domination(5),), ())
        # Each finite observation IS invertible, but its inverse norm is N.
        for n in (1, 4, 17, 103):
            self.assertEqual(Q(1) / Q(1, n), n)
            self.assertEqual(Q(1, n) * n, 1)

    def test_finite_haar_multiplication_commutation_depends_on_fiber_gcd(self):
        for fine, coarse, multiplier, expected in ((4, 2, 2, (Q(1, 2), -Q(1, 2))),
                                                  (6, 2, 2, (Q(), Q()))):
            retract = FiniteQuotientRetract(fine, coarse, SOURCE.source, SOURCE.epoch)
            delta = tuple(int(i == 1) for i in range(fine))
            lhs = retract.average(tuple(delta[(multiplier*x+1) % fine] for x in range(fine)))
            avg = retract.average(delta)
            rhs = tuple(avg[(multiplier*x+1) % coarse] for x in range(coarse))
            # 4->2,c=2: lhs=(1,0), rhs=(1/2,1/2).
            # 6->2,c=2: both sides=(1/3,1/3).
            difference = tuple(a-b for a, b in zip(lhs, rhs))
            self.assertEqual(difference, expected)

    def test_parity_reduction_must_reject_actual_off_parity_coupling(self):
        self.assertEqual(parity_blocks(((1, 0), (0, 2)), 2)["odd"], ((1,),))
        with self.assertRaises(SchurSourceError):
            parity_blocks(((1, 2), (2, 1)), 2)

    def test_recursive_source_positive_prefix_with_all_debts_retained(self):
        stages = tuple(stage(recursive_positive_gram_stage(n, Q(1, 3))["finite_G_matrix"],
                             basis=f"first-{n}") for n in range(1, 7))
        chain = PositiveCompressionChain(stages, tuple(coordinate_inclusion(n) for n in range(1, 6)))
        self.assertEqual(chain.unresolved_debts, tuple(ProofDebt))
        # Form compression must NOT accidentally demand operator intertwining:
        self.assertNotEqual(stages[1].coefficients[1][0], 0)

    def test_rotated_rational_isometry(self):
        j = ((Q(3, 5),), (Q(4, 5),))
        high = stage(((2, 0), (0, 3)), basis="fine")
        low = stage(((Q(66, 25),),), basis="rotated-ray")
        self.assertEqual(PositiveCompressionChain((low, high), (j,)).inclusions, (j,))
        with self.assertRaisesRegex(ProofGluingError, "isometric"):
            PositiveCompressionChain((low, high), (((Q(3, 5),), (Q(3, 5),)),))

    def test_wrong_compression_source_epoch_and_operator_rejected(self):
        low, high = stage(((1,),)), stage(((1, 0), (0, 1)))
        for bad in (replace(high, source=replace(SOURCE, epoch=9)),
                    replace(high, source=replace(SOURCE, source="unrelated-gram")),
                    replace(high, source=replace(SOURCE, observer="other-tests")),
                    replace(high, operator="different-A"), stage(((2, 0), (0, 1)))):
            with self.assertRaises(ProofGluingError):
                PositiveCompressionChain((low, bad), (coordinate_inclusion(1),))

    def test_positive_diagonal_does_not_hide_negative_cross_block(self):
        with self.assertRaisesRegex(ProofGluingError, "Negative principal minor"):
            PositiveCompressionChain((stage(((1, -2), (-2, 1))),), ())

    def test_singular_schur_range_failure_reuses_existing_kernel(self):
        bad = exact_scalar_schur_gluing(0, Q(1, 2), 1)
        self.assertFalse(bad["cross_in_parent_range"])
        self.assertEqual(bad["principal_determinant"], -Q(1, 4))
        with self.assertRaisesRegex(ProofGluingError, "Negative principal minor"):
            PositiveCompressionChain((stage(((0,),)), stage(((0, Q(1, 2)), (Q(1, 2), 1)))),
                                     (coordinate_inclusion(1),))
        good = PositiveCompressionChain((stage(((0,),)), stage(((0, 0), (0, 1)))),
                                        (coordinate_inclusion(1),))
        self.assertIn(ProofDebt.ALL_STAGE_POSITIVITY, good.unresolved_debts)

    def test_nondense_chain_can_miss_negative_direction_forever(self):
        # A=diag(1,-1), repeated P=diag(1,0); exact observed compression is [1].
        chain = PositiveCompressionChain((stage(((1,),)),)*3, (((1,),),)*2)
        self.assertIn(ProofDebt.DENSE_PROJECTORS, chain.unresolved_debts)
        self.assertEqual(sum(x*a*x for x, a in zip((0, 1), (1, -1))), -1)

    def test_finite_dense_chain_prefix_misses_remote_negative_direction(self):
        for hidden in (3, 8, 31):
            early = remote_negative_sign_shadow(hidden, hidden)
            later = remote_negative_sign_shadow(hidden+1, hidden)
            self.assertTrue(early["finite_compressions_appear_identical"])
            self.assertTrue(later["negative_direction_is_visible"])
            self.assertFalse(early["uniform_cutoff_independent_of_hidden_index_exists"])

    def test_unbounded_selfadjoint_dense_positive_domain_countermodel(self):
        # Paper D=span(v_n), v_n=e0+e_n/n, A=diag(-1,4*n**4).
        # q(v_i,v_j)=4*i**2 delta_ij - 1; this is a NONorthonormal basis.
        for n in range(1, 7):
            gram = tuple(tuple(Q(4*i*i-1 if i == j else -1)
                               for j in range(1, n+1)) for i in range(1, n+1))
            self.assertTrue(all(d > 0 for _, d in principal_minors(gram)))
            self.assertLessEqual(sum(Q(1, k*k) for k in range(1, n+1)), 2)
        for n in (2, 11, 37):
            self.assertLess(Q(1, n*n), 1)  # ||v_n-e0||^2 -> 0
            self.assertGreater(-1+4*n*n, 0)  # q(v_n) does NOT -> q(e0)=-1

    def test_exact_numbers_shapes_and_debt_override_rejected(self):
        for bad in (((True,),), ((0.5,),), ((1, 2), (0, 1)), (), ((1, 2),)):
            with self.assertRaises(ValueError):
                stage(bad)
        with self.assertRaises(TypeError):
            PositiveCompressionChain((stage(((1,),)),), (), unresolved_debts=())


class ActualKleeneEnumerationTests(unittest.TestCase):
    def test_independent_marked_tape_matches_real_source_enumeration(self):
        for e in range(96):
            for steps in (0, 1, 2, 9, 32):
                self.assertEqual(bounded_binary_turing_diagonal(e, steps),
                                 independent_diagonal(e, steps), (e, steps))

    def test_each_receipt_replays_actual_halts(self):
        for depth in (0, 1, 2, 7, 12, 36, 64):
            receipt = kleene_level_receipt(depth)
            self.assertEqual(receipt.observed_diagonal_halts,
                             tuple((e, b) for e in range(depth)
                                   if (b := independent_diagonal(e, depth)) is not None))
            for k in range(depth+1):
                self.assertTrue(kleene_source_tree_accepts(receipt.prefix[:k]))

    def test_constant_programs_force_opposite_bits(self):
        # e=0 encodes the constant-0 machine; e=35 encodes one-state table 7,
        # whose radix-6 digits are (1,1), so it halts with 1 on either symbol.
        self.assertEqual(independent_diagonal(35, 1), 1)
        receipt = kleene_level_receipt(36)
        self.assertEqual((receipt.prefix[0], receipt.prefix[35]), (1, 0))
        self.assertFalse(kleene_source_tree_accepts((0,)))
        self.assertFalse(kleene_source_tree_accepts((1,)*36))

    def test_exhaustive_small_tree_is_prefix_closed(self):
        for n in range(8):
            survivors = [w for w in words((0, 1), repeat=n) if kleene_source_tree_accepts(w)]
            self.assertTrue(survivors)
            for w in survivors:
                self.assertTrue(all(kleene_source_tree_accepts(w[:k]) for k in range(n+1)))

    def test_synthetic_trace_is_not_the_source_tree(self):
        synthetic = finite_kleene_tree_calibration(1, records=())
        self.assertIn("0", synthetic["last_level_nodes"])
        self.assertFalse(kleene_source_tree_accepts((0,)))
        for invalid in (-1, True, 65, 2.0):
            with self.assertRaises(ProofGluingError):
                kleene_level_receipt(invalid)


class SourceRelativeLimitTests(unittest.TestCase):
    def test_irrational_completion_specimen_has_computable_cauchy_modulus(self):
        for imaginary in (RationalSpan(0, 1), RationalSpan(3, 7), RationalSpan(-4, 9)):
            name = GaussianCauchyRoot2(imaginary)
            for bits in (0, 1, 7, 31, 100):
                # decimal precision = requested binary bits is a computable
                # sufficient modulus: 10^-bits <= 2^-bits, with strict error.
                r = name.stage(bits)
                self.assertLess(r["real_lower"]**2, 2)
                self.assertGreater(r["real_upper"]**2, 2)
                self.assertLessEqual(r["real_error_upper"], Q(1, 2**bits))
                self.assertEqual(r["imaginary"], imaginary.as_fraction())

    def test_adele_rational_lift_torsion_obstruction(self):
        for p in (2, 3, 5, 7):
            for exponent in (1, 2):
                coset = FiniteAdeleCoset((LocalFractionalAdeleCell(p, exponent, 1),))
                r = adele_lift_obstruction(coset)
                self.assertEqual(r.torsion_order, p**exponent)
                self.assertEqual(r.multiplied_lift, 1)
                self.assertEqual((r.torsion_order*r.quotient_class) % 1, 0)
        half = FiniteAdeleCoset((LocalFractionalAdeleCell(2, 1, 1),))
        self.assertEqual(add_cosets(half, half)["result_Q_over_Z"], "0")
        self.assertEqual(half.rational_lift+half.rational_lift, 1)

    def test_mixed_prime_lift_and_zero_class_guard(self):
        coset = FiniteAdeleCoset((LocalFractionalAdeleCell(2, 1, 1),
                                 LocalFractionalAdeleCell(3, 1, 2)))
        r = adele_lift_obstruction(coset)
        self.assertEqual((r.quotient_class, r.torsion_order, r.multiplied_lift), (Q(1, 6), 6, 7))
        with self.assertRaises(ProofGluingError):
            adele_lift_obstruction(FiniteAdeleCoset(()))

    def test_noncompact_escape_cannot_be_a_compactness_certificate(self):
        for h in (1, 4, 13):
            escaping = noncompact_escape_prefix(h)
            witness = escaping["finite_source_witness"]
            self.assertGreaterEqual(witness, h)
            self.assertLess(witness, h+1)  # the next fiber kills THIS witness
            descending = noncompact_descending_field(h)
            self.assertEqual(descending["finite_level_witness"], tuple(range(h-1, -1, -1)))
            self.assertFalse(descending["global_inverse_limit_nonempty"])

    def test_phantom_is_source_failure_even_when_reports_match(self):
        for depth in (1, 2, 3, 4):
            ghost = phantom_source_prefix(depth)
            self.assertEqual(ghost["ghost_finite_source_reports"], ghost["matching_integer_reports"])
            self.assertFalse(ghost["one_original_integer_realizes_all_levels"])
        hidden = hidden_coordinate_phantom(5)
        self.assertNotEqual(hidden["full_actual_prefix"], hidden["full_phantom_prefix"])
        self.assertTrue(hidden["even_reports_equal"])

    def test_closed_cylinder_positive_control_keeps_infinite_debt(self):
        result = finite_closed_cylinder_prefix(((1,), (1, 0), (1, 0, 1)))
        self.assertTrue(result["finite_closed_fibers_have_nonempty_intersection"])
        self.assertFalse(result["finitely_verified_global_source"])
        with self.assertRaises(ValueError):
            finite_closed_cylinder_prefix(((1,), (0, 1)))


if __name__ == "__main__":
    unittest.main()
