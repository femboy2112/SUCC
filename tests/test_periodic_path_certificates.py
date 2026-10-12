"""Integer certificates checked against lifted graphs and hostile mutations."""
from collections import deque
from dataclasses import replace
from itertools import product
import json
import unittest

from observational_succ.periodic_path_certificates import (
    CertificateError, SearchBudgetExceeded, PeriodicGraph,
    ConfinementCertificate, TranslationWitness, analyze_periodic,
    verify_confinement, verify_translation, verify_finite_defects,
    transport_confinement, gaussian_sieve, gaussian_exceptions,
    is_gaussian_prime, gaussian_bound, certificate_from_dict,
    search_split_prime_prefix,
)


def actual_component(graph, start, cap):
    """Independent infinite-lattice BFS, stopped by an explicit point cap."""
    seen = {start}
    queue = deque([start])
    while queue and len(seen) <= cap:
        u = queue.popleft()
        for d in graph.steps:
            v = tuple(a+b for a, b in zip(u, d))
            if graph.contains(v) and v not in seen:
                seen.add(v)
                queue.append(v)
    return seen, not queue


class PeriodicCertificates(unittest.TestCase):
    def test_nonzero_quotient_self_loop_is_retained(self):
        graph = PeriodicGraph(1, 1, ((0,),), ((-1,), (1,)))
        witness = analyze_periodic(graph)
        self.assertIsInstance(witness, TranslationWitness)
        self.assertEqual(verify_translation(graph, witness)["word_length"], 1)
        false = ConfinementCertificate(graph.digest, (((0,), (0,)),))
        with self.assertRaises(CertificateError):
            verify_confinement(graph, false)

    def test_parallel_edges_are_distinct(self):
        graph = PeriodicGraph(2, 1, ((0,), (1,)), ((-1,), (1,)))
        self.assertEqual(len(list(graph.edges((0,)))), 2)
        witness = analyze_periodic(graph)
        self.assertIsInstance(witness, TranslationWitness)
        self.assertEqual(abs(verify_translation(graph, witness)["displacement"][0]), 2)

    def test_crossing_cell_seam_can_be_finite(self):
        graph = PeriodicGraph(3, 1, ((0,), (2,)), ((-1,), (1,)))
        certificate = analyze_periodic(graph)
        self.assertEqual(verify_confinement(graph, certificate)["maximum_component_size"], 2)
        self.assertEqual(dict(certificate.potentials), {(0,): (0,), (2,): (-1,)})
        self.assertEqual(actual_component(graph, (0,), 10), ({(0,), (-1,)}, True))

    def test_quotient_cycle_can_have_zero_translation(self):
        graph = PeriodicGraph(7, 1, ((0,), (1,), (2,)), ((-2,), (-1,), (1,), (2,)))
        result = verify_confinement(graph, analyze_periodic(graph))
        self.assertEqual(result["maximum_component_size"], 3)
        self.assertEqual(result["directed_edges"], 6)

    def test_every_small_mask_against_independent_lifted_bfs(self):
        for q in range(1, 6):
            for mask in product((False, True), repeat=q):
                vertices = tuple((r,) for r in range(q) if mask[r])
                for steps in (((-1,), (1,)), ((-2,), (-1,), (1,), (2,))):
                    graph = PeriodicGraph(q, 1, vertices, steps)
                    result = analyze_periodic(graph)
                    if isinstance(result, ConfinementCertificate):
                        claimed = verify_confinement(graph, result)["maximum_component_size"]
                        sizes = []
                        for start in vertices:
                            seen, complete = actual_component(graph, start, len(vertices))
                            self.assertTrue(complete)
                            sizes.append(len(seen))
                        self.assertEqual(max(sizes, default=0), claimed)
                    else:
                        verify_translation(graph, result)
                        seen, complete = actual_component(graph, result.start, 2*len(vertices)+1)
                        self.assertFalse(complete)
                        self.assertGreater(len(seen), len(vertices))

    def test_mutated_potential_and_source_are_rejected(self):
        graph = PeriodicGraph(3, 1, ((0,), (2,)), ((-1,), (1,)))
        good = analyze_periodic(graph)
        for points in (good.potentials[:-1], good.potentials + good.potentials[:1],
                       (((0,), (0,)), ((2,), (2,))),
                       (((0,), (0.0,)), ((2,), (-1,)))):
            with self.assertRaises(CertificateError):
                verify_confinement(graph, replace(good, potentials=points))
        changed = PeriodicGraph(3, 1, ((0,), (1,), (2,)), graph.steps)
        with self.assertRaises(CertificateError):
            verify_confinement(changed, good)

    def test_false_translation_words_are_rejected(self):
        graph = PeriodicGraph(2, 1, ((0,), (1,)), ((-1,), (1,)))
        good = analyze_periodic(graph)
        for word in ((), ((1,),), ((1,), (-1,)), ((2,),)):
            with self.assertRaises(CertificateError):
                verify_translation(graph, replace(good, word=word))

    def test_positive_proof_transports_through_source_refinement(self):
        coarse = PeriodicGraph(3, 1, ((0,), (2,)), ((-1,), (1,)))
        fine = PeriodicGraph(6, 1, ((0,), (2,), (3,), (5,)), coarse.steps)
        cert = transport_confinement(coarse, fine, analyze_periodic(coarse))
        self.assertEqual(verify_confinement(fine, cert)["maximum_component_size"], 2)
        added = PeriodicGraph(6, 1, fine.residues + ((1,),), fine.steps)
        with self.assertRaises(CertificateError):
            transport_confinement(coarse, added, analyze_periodic(coarse))
        larger_steps = PeriodicGraph(6, 1, fine.residues, ((-2,), (-1,), (1,), (2,)))
        with self.assertRaises(CertificateError):
            transport_confinement(coarse, larger_steps, analyze_periodic(coarse))

    def test_finite_defect_gluing_exact_and_deduplicated(self):
        graph = PeriodicGraph(3, 1, ((0,), (2,)), ((-1,), (1,)))
        cert = analyze_periodic(graph)
        report = verify_finite_defects(graph, cert, ((1,),))
        self.assertEqual(report["maximum_component_size"], 5)
        self.assertEqual(report["adjacent_periodic_components"], 2)
        # Two exceptions connect three islands, not four disjoint copies.
        report = verify_finite_defects(graph, cert, ((1,), (4,)))
        self.assertEqual(report["maximum_component_size"], 8)
        self.assertEqual(report["adjacent_periodic_components"], 3)
        self.assertLess(report["maximum_component_size"], report["coarse_degree_bound"])
        for exceptions in (((1,), (1,)), ((0,),)):
            with self.assertRaises(CertificateError):
                verify_finite_defects(graph, cert, exceptions)

    def test_empty_and_no_step_boundaries(self):
        empty = PeriodicGraph(2, 1, (), ((-1,), (1,)))
        self.assertEqual(verify_confinement(empty, analyze_periodic(empty))["maximum_component_size"], 0)
        self.assertEqual(verify_finite_defects(empty, analyze_periodic(empty), ((0,), (1,)))["maximum_component_size"], 2)
        isolated = PeriodicGraph(1, 2, ((0, 0),), ())
        self.assertEqual(verify_confinement(isolated, analyze_periodic(isolated))["maximum_component_size"], 1)

    def test_json_roundtrip_and_bad_rows(self):
        for graph in (gaussian_sieve((2,), 1), gaussian_sieve((2,), 2)):
            proof = analyze_periodic(graph)
            parsed = certificate_from_dict(json.loads(json.dumps(proof.to_dict())))
            self.assertEqual(proof, parsed)
        data = analyze_periodic(gaussian_sieve((2,), 1)).to_dict()
        data["potentials"].append([[0, 0]])
        with self.assertRaises(CertificateError):
            certificate_from_dict(data)
        data["potentials"] = {}
        with self.assertRaises(CertificateError):
            certificate_from_dict(data)
        empty = PeriodicGraph(2, 1, (), ((-1,), (1,)))
        with self.assertRaises(CertificateError):
            verify_confinement(empty, ConfinementCertificate(empty.digest, (None,)))
        with self.assertRaises(CertificateError):
            PeriodicGraph(2, 1, ([0],), ((-1,), (1,)))

    def test_nested_periodic_observers_need_not_find_a_finite_certificate(self):
        # A_n = {2^n | 3x+1} union (2^n Z)^2. Every A_n has an
        # infinite column; intersection over all n is {(0,0)} (proved in dossier).
        previous = None
        for n in range(1, 7):
            q = 2**n
            vertices = tuple((x, y) for x in range(q) for y in range(q)
                             if (3*x+1) % q == 0 or (x, y) == (0, 0))
            graph = PeriodicGraph(q, 2, vertices, ((-1, 0), (0, -1), (0, 1), (1, 0)))
            witness = analyze_periodic(graph)
            self.assertIsInstance(witness, TranslationWitness)
            verify_translation(graph, witness)
            if previous:
                self.assertTrue(all(previous.contains(v) for v in graph.residues))
            previous = graph


class GaussianSourceCertificates(unittest.TestCase):
    def test_prime_classification_and_exception_types(self):
        for z in ((1, 1), (2, 1), (1, -2), (3, 0), (0, -7)):
            self.assertTrue(is_gaussian_prime(z))
        for z in ((0, 0), (1, 0), (2, 0), (5, 0), (3, 3), (4, 2)):
            self.assertFalse(is_gaussian_prime(z))
        self.assertEqual(len(gaussian_exceptions((2,))), 4)
        self.assertEqual(len(gaussian_exceptions((5,))), 8)
        self.assertEqual(len(gaussian_exceptions((3,))), 4)
        self.assertIn((3, 0), gaussian_exceptions((3,)))

    def test_containment_on_fresh_prime_and_composite_box(self):
        primes = (2, 3, 5, 13)
        graph = gaussian_sieve(primes, 1)
        excluded = set(gaussian_exceptions(primes))
        for x in range(-31, 32):
            for y in range(-31, 32):
                z = (x, y)
                if is_gaussian_prime(z):
                    self.assertEqual(not graph.contains(z), z in excluded)
        # Norm divisibility includes both conjugate factors, not one chosen line.
        split = gaussian_sieve((5,), 1)
        self.assertFalse(split.contains((2, 1)))
        self.assertFalse(split.contains((2, -1)))

    def test_gaussian_positive_negative_and_finite_exception_gate(self):
        graph = gaussian_sieve((2,), 1)
        proof = analyze_periodic(graph)
        result = gaussian_bound((2,), 1, proof)
        self.assertEqual(result["sieve"]["maximum_component_size"], 1)
        # Restoring the norm-2 primes must enlarge the upper bound.
        self.assertGreater(result["prime_component_upper_bound"], 1)
        self.assertIsInstance(analyze_periodic(gaussian_sieve((2,), 2)), TranslationWitness)

    def test_split_prime_certificate_and_step_mutation(self):
        graph = gaussian_sieve((5, 13), 1)
        proof = analyze_periodic(graph)
        result = verify_confinement(graph, proof)
        self.assertEqual((result["vertices"], result["maximum_component_size"]), (2304, 580))
        changed = gaussian_sieve((5, 13), 2)
        self.assertIsInstance(analyze_periodic(changed), TranslationWitness)
        with self.assertRaises(CertificateError):
            verify_confinement(changed, proof)

    def test_diagonal_gaussian_certificate(self):
        graph = gaussian_sieve((2, 5, 13), 2)
        result = gaussian_bound((2, 5, 13), 2, analyze_periodic(graph))
        self.assertEqual(result["sieve"]["maximum_component_size"], 580)
        self.assertEqual(result["sieve"]["vertices"], 4608)
        self.assertEqual(result["finite_defects"]["exceptions"], 20)
        self.assertFalse(result["all_step_existence_used_by_verifier"])

    def test_bad_source_and_resource_caps_do_not_become_proofs(self):
        for primes in ((6,), (5, 5), (True,), (1,)):
            with self.assertRaises(CertificateError):
                gaussian_sieve(primes, 1)
        for radius in (1.0, True, -1):
            with self.assertRaises(CertificateError):
                gaussian_sieve((2,), radius)
        with self.assertRaises(SearchBudgetExceeded):
            gaussian_sieve((5, 13), 1, max_cells=4000)
        with self.assertRaises(SearchBudgetExceeded):
            gaussian_sieve((2,), 10000, max_step_box=100)
        # An obviously over-budget enormous source must be rejected before
        # the primality routine could start impractical trial division.
        with self.assertRaises(SearchBudgetExceeded):
            gaussian_sieve((10**100 + 267,), 1, max_cells=1)

    def test_bounded_search_success_and_unresolved_outcomes(self):
        success = search_split_prime_prefix(1, prime_limit=13)
        self.assertEqual(success["status"], "CERTIFICATE_FOUND")
        self.assertEqual(success["rational_primes"], [5, 13])
        limited = search_split_prime_prefix(2, prime_limit=13)
        self.assertEqual(limited["status"], "UNRESOLVED_PRIME_LIMIT")
        capped = search_split_prime_prefix(2, prime_limit=17, max_cells=5000)
        self.assertEqual(capped["status"], "UNRESOLVED_RESOURCE_LIMIT")


if __name__ == "__main__":
    unittest.main()
