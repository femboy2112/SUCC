"""Exact controls for the declared two-qubit instrument model."""
from fractions import Fraction as Q
from itertools import product, combinations
import unittest

from observational_succ import haar_quantum_instruments as q
from observational_succ.quantum_records import Instrument, measure_x, measure_z


COHERENCES = (Q(-1), Q(-3, 4), Q(-1, 3), Q(0), Q(1, 5), Q(2, 3), Q(3, 4), Q(1))
BLOCH = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1),
         (Q(3, 5), Q(4, 5)), (Q(-3, 5), Q(4, 5)), (Q(2, 5), Q(-1, 5)))
AXES = ((0, 1), (1, 0), (Q(3, 5), Q(4, 5)), (Q(-3, 5), Q(4, 5)))


def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def mix(states, weights):
    return tuple(tuple(sum(weight*state[i][j] for state, weight in zip(states, weights))
                       for j in range(len(states[0]))) for i in range(len(states[0])))


def pure_density(amplitudes):
    norm = sum(x*x for x in amplitudes)
    return tuple(tuple(Q(x*y, norm) for y in amplitudes) for x in amplitudes)


def instruments():
    return (
        Instrument("Identity", (("keep", ((1, 0), (0, 1))),)),
        Instrument("BitFlip", (("flip", ((0, 1), (1, 0))),)),
        measure_x(), measure_z(),
        Instrument("ZReset", (("zero", ((1, 0), (0, 0))),
                              ("one", ((0, 1), (0, 0))))),
        Instrument("WeakZ", (("first", ((Q(3, 5), 0), (0, Q(4, 5)))),
                             ("second", ((Q(4, 5), 0), (0, Q(3, 5)))))),
        Instrument("AmplitudeDamping", (("keep", ((1, 0), (0, Q(3, 5)))),
                                       ("jump", ((0, Q(4, 5)), (0, 0))))),
    )


def state_grid():
    states = [q.coherence_state(c) for c in COHERENCES]
    states.extend((q.tensor_state(q.qubit_state(0, 1), q.qubit_state(0, -1)),
                   q.tensor_state(q.qubit_state(Q(3, 5), Q(4, 5)),
                                  q.qubit_state(Q(2, 5), Q(-1, 5))),
                   q.tensor_state(q.qubit_state(0, 0), q.qubit_state(1, 0))))
    states.append(mix((states[-2], q.coherence_state(Q(3, 4))), (Q(2, 3), Q(1, 3))))
    return states


class CoherenceAndWitnessTests(unittest.TestCase):
    def test_candidate_density_and_purity(self):
        for c in COHERENCES:
            rho = q.coherence_state(c)
            self.assertEqual(q.validate_density(rho), rho)
            self.assertEqual(trace(rho), 1)
            purity = sum(rho[i][j]*rho[j][i] for i in range(4) for j in range(4))
            self.assertEqual(purity, (1+c*c)/2)

    def test_classical_mixture_is_exactly_dephased_family(self):
        zero = pure_density((1, 0, 0, 0))
        one = pure_density((0, 0, 0, 1))
        self.assertEqual(q.coherence_state(0), mix((zero, one), (Q(1, 2), Q(1, 2))))

    def test_marginals_do_not_identify_coherence(self):
        for c in COHERENCES:
            for keep in ("alice", "bob"):
                self.assertEqual(q.partial_trace(q.coherence_state(c), keep), q.qubit_state(0, 0))

    def test_correlations_keep_the_signed_phase(self):
        for c in COHERENCES:
            rho = q.coherence_state(c)
            self.assertEqual(q.bipartite_expectation(rho, q.X, q.X), c)
            self.assertEqual(q.bipartite_expectation(rho, q.Z, q.Z), 1)
            self.assertEqual(q.bipartite_expectation(rho, q.X, q.Z), 0)
            self.assertEqual(q.bipartite_expectation(rho, q.Z, q.X), 0)
            self.assertEqual(q.two_axis_score(rho), 1+abs(c))

    def test_all_declared_axis_probabilities(self):
        for c, alice, bob in product(COHERENCES, AXES, AXES):
            probabilities = q.joint_axis_probabilities(q.coherence_state(c), alice, bob)
            correlation = c*alice[0]*bob[0]+alice[1]*bob[1]
            self.assertEqual(sum(probabilities.values()), 1)
            for a, b in product((1, -1), repeat=2):
                self.assertEqual(probabilities[a, b], (1+a*b*correlation)/4)

    def test_separable_bound_on_product_grid_and_mixtures(self):
        states = [q.qubit_state(*coordinates) for coordinates in BLOCH]
        for alice, bob in product(states, repeat=2):
            self.assertLessEqual(q.two_axis_score(q.tensor_state(alice, bob)), 1)
        products = [q.tensor_state(states[i], states[-i-1]) for i in range(len(states))]
        for left, right in combinations(products, 2):
            self.assertLessEqual(q.two_axis_score(mix((left, right), (Q(1, 3), Q(2, 3)))), 1)
        for coordinates in ((0, 1), (1, 0), (Q(3, 5), Q(4, 5))):
            state = q.qubit_state(*coordinates)
            self.assertEqual(q.two_axis_score(q.tensor_state(state, state)), 1)

    def test_partial_transpose_is_independent_entanglement_control(self):
        for c in COHERENCES:
            rho = q.coherence_state(c)
            transpose_b = tuple(tuple(rho[2*(i//2)+(j%2)][2*(j//2)+(i%2)]
                                      for j in range(4)) for i in range(4))
            if c == 0:
                self.assertEqual(q.validate_density(transpose_b), rho)
            else:
                vector = (0, 1, -1 if c > 0 else 1, 0)
                quadratic = sum(vector[i]*transpose_b[i][j]*vector[j]
                                for i in range(4) for j in range(4))
                self.assertEqual(quadratic, -abs(c))
                with self.assertRaises(q.QuantumInstrumentError):
                    q.validate_density(transpose_b)

    def test_witness_is_sufficient_not_necessary(self):
        rotated_bell = pure_density((1, 1, 1, -1))
        self.assertEqual(q.two_axis_score(rotated_bell), 0)
        self.assertEqual(q.chsh_value(rotated_bell, alice_axes=((1, 0), (0, 1))), Q(14, 5))

    def test_phase_erasure_and_duplicated_axis_mutants(self):
        self.assertEqual(q.two_axis_score(q.coherence_state(-1)), 2)
        wrong_signed_score = (q.bipartite_expectation(q.coherence_state(-1), q.X, q.X)
                              +q.bipartite_expectation(q.coherence_state(-1), q.Z, q.Z))
        self.assertEqual(wrong_signed_score, 0)
        self.assertNotEqual(q.bipartite_expectation(q.coherence_state(1), q.X, q.X),
                            q.bipartite_expectation(q.coherence_state(0), q.X, q.X))
        product_zero = pure_density((1, 0, 0, 0))
        duplicated_axis_score = 2*abs(q.bipartite_expectation(product_zero, q.Z, q.Z))
        self.assertEqual(duplicated_axis_score, 2)
        self.assertEqual(q.two_axis_score(product_zero), 1)


class LocalInstrumentTests(unittest.TestCase):
    def test_no_signalling_for_all_complete_instruments_and_both_sides(self):
        for rho, instrument, side in product(state_grid(), instruments(), ("alice", "bob")):
            remote = "bob" if side == "alice" else "alice"
            branches = q.apply_local_instrument(rho, instrument, side)
            self.assertEqual(sum(branch.probability for branch in branches), 1)
            for branch in branches:
                self.assertGreaterEqual(branch.probability, 0)
                if branch.posterior is not None:
                    self.assertEqual(trace(branch.posterior), 1)
            after = q.discard_local_outcomes(rho, instrument, side)
            self.assertEqual(q.partial_trace(after, remote), q.partial_trace(rho, remote))

    def test_unequal_product_marginals_prevent_side_swap_vacuity(self):
        alice = q.qubit_state(Q(3, 5), Q(4, 5))
        bob = q.qubit_state(Q(2, 5), Q(-1, 5))
        rho = q.tensor_state(alice, bob)
        self.assertEqual(q.partial_trace(rho, "alice"), alice)
        self.assertEqual(q.partial_trace(rho, "bob"), bob)
        self.assertNotEqual(alice, bob)

    def test_same_z_conditioning_for_classical_and_entangled_sources(self):
        for c in COHERENCES:
            rho = q.coherence_state(c)
            for label, z in (("zero", 1), ("one", -1)):
                branch = q.postselect_local_outcome(rho, measure_z(), label)
                self.assertEqual(branch.probability, Q(1, 2))
                self.assertEqual(q.partial_trace(branch.posterior), q.qubit_state(0, z))
        # In particular, a pure conditional Bob state occurs at separable c=0.
        self.assertEqual(q.two_axis_score(q.coherence_state(0)), 1)

    def test_x_conditioning_resolves_the_coherent_sign(self):
        for c in COHERENCES:
            for label, sign in (("plus", 1), ("minus", -1)):
                branch = q.postselect_local_outcome(q.coherence_state(c), measure_x(), label)
                self.assertEqual(branch.probability, Q(1, 2))
                self.assertEqual(q.partial_trace(branch.posterior), q.qubit_state(sign*c, 0))

    def test_ignored_z_measurement_changes_joint_state_but_not_bob(self):
        for c in COHERENCES:
            after = q.discard_local_outcomes(q.coherence_state(c), measure_z())
            self.assertEqual(after, q.coherence_state(0))
        self.assertNotEqual(q.coherence_state(1), q.coherence_state(0))

    def test_nonunital_channel_preserves_remote_marginal(self):
        damping = instruments()[-1]
        after = q.discard_local_outcomes(q.coherence_state(Q(3, 4)), damping)
        self.assertEqual(q.partial_trace(after, "alice"), ((Q(41, 50), 0), (0, Q(9, 50))))
        self.assertEqual(q.partial_trace(after, "bob"), q.qubit_state(0, 0))

    def test_unequal_branch_weights_and_postselection_mutants(self):
        rho, damping = q.coherence_state(0), instruments()[-1]
        keep = q.postselect_local_outcome(rho, damping, "keep")
        jump = q.postselect_local_outcome(rho, damping, "jump")
        self.assertEqual((keep.probability, jump.probability), (Q(17, 25), Q(8, 25)))
        self.assertEqual(q.partial_trace(keep.posterior), ((Q(25, 34), 0), (0, Q(9, 34))))
        self.assertEqual(q.partial_trace(jump.posterior), q.qubit_state(0, -1))
        unweighted = mix((keep.posterior, jump.posterior), (Q(1, 2), Q(1, 2)))
        self.assertEqual(q.partial_trace(unweighted), ((Q(25, 68), 0), (0, Q(43, 68))))
        self.assertNotEqual(q.partial_trace(unweighted), q.partial_trace(rho))
        unnormalized = mix((keep.posterior,), (keep.probability,))
        self.assertEqual(trace(unnormalized), Q(17, 25))
        with self.assertRaises(q.QuantumInstrumentError):
            q.validate_density(unnormalized)

    def test_zero_probability_outcome_is_not_an_observed_event(self):
        with_zero = Instrument("WithZero", (("never", ((0, 0), (0, 0))), ("keep", ((1, 0), (0, 1)))))
        branches = q.apply_local_instrument(q.coherence_state(1), with_zero)
        self.assertEqual(branches[0].probability, 0)
        self.assertIsNone(branches[0].posterior)
        with self.assertRaises(q.QuantumInstrumentError):
            q.postselect_local_outcome(q.coherence_state(1), with_zero, "never")
        with self.assertRaises(q.QuantumInstrumentError):
            q.postselect_local_outcome(q.coherence_state(1), with_zero, "missing")

    def test_trace_decreasing_filter_cannot_masquerade_as_complete(self):
        with self.assertRaises(ValueError):
            Instrument("Incomplete", (("keep", ((1, 0), (0, Q(3, 5)))),))

    def test_rotated_rank_one_projectors_form_a_complete_instrument(self):
        for axis in AXES:
            plus, minus = q.xz_projectors(*axis)
            self.assertEqual(trace(plus), 1)
            self.assertEqual(trace(minus), 1)
            for projector in (plus, minus):
                square = tuple(tuple(sum(projector[i][k]*projector[k][j] for k in range(2))
                                     for j in range(2)) for i in range(2))
                self.assertEqual(square, projector)
            instrument = Instrument("Rotated", (("plus", plus), ("minus", minus)))
            after = q.discard_local_outcomes(q.coherence_state(Q(3, 4)), instrument)
            self.assertEqual(q.partial_trace(after), q.qubit_state(0, 0))


class BellAndClassicalControls(unittest.TestCase):
    def test_shared_two_signs_reproduce_all_restricted_bell_data(self):
        axes = {"X": (1, 0), "Z": (0, 1)}
        for alice, bob in product(axes, repeat=2):
            self.assertEqual(q.shared_sign_probabilities(alice, bob),
                             q.joint_axis_probabilities(q.coherence_state(1), axes[alice], axes[bob]))
        for x, z in product((1, -1), repeat=2):
            with self.assertRaises(q.QuantumInstrumentError):
                q.qubit_state(x, z)  # Classical table is not a trusted local qubit state.

    def test_all_sixteen_deterministic_chsh_tables(self):
        scores = [a0*b0+a0*b1+a1*b0-a1*b1
                  for a0, a1, b0, b1 in product((1, -1), repeat=4)]
        self.assertEqual(len(scores), 16)
        self.assertEqual(set(scores), {-2, 2})
        self.assertEqual(max(abs(score) for score in scores), 2)

    def test_rational_rotated_chsh_positive_negative_and_null_controls(self):
        for c in COHERENCES:
            self.assertEqual(q.chsh_value(q.coherence_state(c)), (8+6*c)/5)
        self.assertEqual(q.chsh_value(q.coherence_state(0)), Q(8, 5))
        self.assertEqual(q.chsh_value(q.coherence_state(Q(3, 4))), Q(5, 2))
        self.assertEqual(q.chsh_value(q.coherence_state(1)), Q(14, 5))
        self.assertEqual(q.chsh_value(q.coherence_state(-1), alice_axes=((0, 1), (-1, 0))), Q(14, 5))
        self.assertLessEqual(q.chsh_value(q.coherence_state(Q(1, 5))), 2)
        self.assertGreater(q.two_axis_score(q.coherence_state(Q(1, 5))), 1)

    def test_classical_conditional_belief_matches_separable_remote_update(self):
        classical_joint = {(0, 0): Q(1, 2), (1, 1): Q(1, 2)}
        probability = sum(p for (a, _), p in classical_joint.items() if a == 0)
        bob_zero = sum(p for (a, b), p in classical_joint.items() if a == b == 0)/probability
        self.assertEqual(bob_zero, 1)
        branch = q.postselect_local_outcome(q.coherence_state(0), measure_z(), "zero")
        self.assertEqual(branch.probability, probability)
        self.assertEqual(q.partial_trace(branch.posterior)[0][0], bob_zero)

    def test_classical_read_and_reset_changes_the_joint_distribution(self):
        reset = instruments()[4]
        after = q.discard_local_outcomes(q.coherence_state(0), reset)
        expected = q.tensor_state(q.qubit_state(0, 1), q.qubit_state(0, 0))
        self.assertEqual(after, expected)
        self.assertNotEqual(after, q.coherence_state(0))
        self.assertEqual(q.partial_trace(after), q.qubit_state(0, 0))

    def test_noncommuting_classical_stochastic_disturbances(self):
        reset = ((1, 1), (0, 0))  # Column stochastic: reset to zero.
        flip = ((0, 1), (1, 0))
        prior = (Q(1, 2), Q(1, 2))
        def act(kernel, probability):
            return tuple(sum(kernel[i][j]*probability[j] for j in range(2)) for i in range(2))
        self.assertEqual(act(reset, act(flip, prior)), (1, 0))
        self.assertEqual(act(flip, act(reset, prior)), (0, 1))
        self.assertTrue(all(sum(kernel[i][j] for i in range(2)) == 1
                            for kernel in (reset, flip) for j in range(2)))

    def test_equal_energy_different_coherence_and_energy_offset_control(self):
        number = ((0, 0), (0, 1))
        for c in (0, 1):
            rho = q.coherence_state(c)
            energy = q.bipartite_expectation(rho, number, q.I)+q.bipartite_expectation(rho, q.I, number)
            self.assertEqual(energy, 1)
            shifted = ((17, 0), (0, 18))
            shifted_energy = q.bipartite_expectation(rho, shifted, q.I)+q.bipartite_expectation(rho, q.I, number)
            self.assertEqual(shifted_energy, 18)
        self.assertEqual(q.two_axis_score(q.coherence_state(0)), 1)
        self.assertEqual(q.two_axis_score(q.coherence_state(1)), 2)


class ExactDomainTests(unittest.TestCase):
    def test_invalid_coherence_and_nonexact_values(self):
        for value in (-2, 2, Q(1001, 1000), True, 0.5, "1"):
            with self.assertRaises(q.QuantumInstrumentError):
                q.coherence_state(value)
        for value in (True, 0.5):
            with self.assertRaises(q.QuantumInstrumentError):
                q.qubit_state(value, 0)

    def test_density_guards_include_higher_principal_obstruction(self):
        bad = ((Q(1, 3), Q(-1, 4), Q(-1, 4), 0),
               (Q(-1, 4), Q(1, 3), Q(-1, 4), 0),
               (Q(-1, 4), Q(-1, 4), Q(1, 3), 0), (0, 0, 0, 0))
        self.assertEqual(trace(bad), 1)
        self.assertTrue(all(bad[i][i]*bad[j][j]-bad[i][j]**2 >= 0
                            for i in range(4) for j in range(i+1, 4)))
        with self.assertRaises(q.QuantumInstrumentError):
            q.validate_density(bad)
        for bad in (((0, Q(1, 2)), (Q(1, 2), 1)),
                    ((1, 1), (0, 0)), ((1, 0), (0, 1)),
                    ((1.0, 0), (0, 0)), ((True, 0), (0, 0)),
                    ((1,),), ((1, 0),)):
            with self.assertRaises(q.QuantumInstrumentError):
                q.validate_density(bad)

    def test_axis_side_observable_and_setting_guards(self):
        rho = q.coherence_state(0)
        for axis in ((0, 0), (Q(1, 2), Q(1, 2)), (True, 0), (1.0, 0)):
            with self.assertRaises(q.QuantumInstrumentError):
                q.xz_projectors(*axis)
        with self.assertRaises(q.QuantumInstrumentError):
            q.partial_trace(rho, "unknown")
        with self.assertRaises(q.QuantumInstrumentError):
            q.bipartite_expectation(rho, ((0, 1), (0, 0)), q.I)
        with self.assertRaises(q.QuantumInstrumentError):
            q.chsh_value(rho, alice_axes=((1, 0),))
        with self.assertRaises(q.QuantumInstrumentError):
            q.joint_axis_probabilities(rho, (1, 0, 0), (0, 1))
        with self.assertRaises(q.QuantumInstrumentError):
            q.shared_sign_probabilities("Y", "X")

    def test_bounded_complete_outcome_family(self):
        zeros = tuple((f"zero_{j}", ((0, 0), (0, 0))) for j in range(16))
        maximum = Instrument("Maximum", (("keep", ((1, 0), (0, 1))),)+zeros[:15])
        self.assertEqual(len(q.apply_local_instrument(q.coherence_state(0), maximum)), 16)
        oversized = Instrument("Oversized", (("keep", ((1, 0), (0, 1))),)+zeros)
        with self.assertRaises(q.QuantumInstrumentError):
            q.apply_local_instrument(q.coherence_state(0), oversized)
        with self.assertRaises(q.QuantumInstrumentError):
            q.apply_local_instrument(q.coherence_state(0), object())


if __name__ == "__main__":
    unittest.main()
