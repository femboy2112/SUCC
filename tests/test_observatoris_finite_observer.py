"""OPUS I finite-observer lab: exhaustive small models, mutations and holdouts.

Every exhaustive loop below could have falsified the corresponding theorem of
research/2026-11-14/principia_observatoris_second_forge/agents/OPUS_I_FINITE_OBSERVER.md.
"""
import random
import unittest
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb

from observational_succ import carrier_relative_targets as crt
from observational_succ.observatoris_finite_observer import (
    BOTTOM, FiniteCarrier, Network, ObserverError,
    agreement_horizon, ball_horizon, ball_pair_points, ball_points,
    behaviour_blocks, cancellation_pair, certification_cost, certifies_absence,
    class_identifies_graph, class_injective, class_nondisturbing, clamp_criterion,
    commuting_idempotent, core, destructive_abc, enumerate_carriers,
    enumerate_networks, essential, execute_policy, exhaustive_minimum_certifying,
    experiment, first_disagreement, free_observability, gating_network,
    general_ball_horizon, general_essential, general_horizon, independent_extension,
    interaction_horizon, jet_predict, k_blocks, minimal_cancellation_pair,
    mobius_coefficients, mobius_degree, monotone_table, network_data,
    nondisturbing_abc, poly_eval, quotient, range_gate_network, readout_swap,
    realized_contexts, reconstruct_core, reset_and_readout, response_table,
    restrict, same_partition, separately_but_not_jointly, sharp_pair,
    split_instrument, synthesize,
    target_access, taylor_jet, to_carrier_relative, toolkit_reduct_cores,
    transcript, transport_coefficients, variable_degree, words,
)


def distinct_cores(n_max, instruments):
    out = set()
    for n in range(1, n_max + 1):
        for c in enumerate_carriers(n, instruments):
            out.add(core(c))
    return sorted(out, key=lambda k: (k.size, repr(k.rows)))


def random_carrier(rng, n, p, r=2, partial=False):
    names = tuple("abcd"[:p])
    readout = tuple(tuple(rng.randrange(r) for _ in range(n)) for _ in range(p))
    trans = tuple(tuple(None if partial and rng.random() < 0.25 else rng.randrange(n)
                        for _ in range(n)) for _ in range(p))
    return FiniteCarrier(n, names, readout, trans, rng.randrange(n))


# --------------------------------------------------------------------------
# A1: kernel, core, identification, reconstruction, toolkit monotonicity
# --------------------------------------------------------------------------

class KernelAndCore(unittest.TestCase):

    def test_malformed_kernels_rejected(self):
        bad = [
            lambda: FiniteCarrier(0, ("a",), ((),), ((),)),
            lambda: FiniteCarrier(1, ("a", "a"), ((0,), (0,)), ((0,), (0,))),
            lambda: FiniteCarrier(1, ("a",), ((0.5,),), ((0,),)),
            lambda: FiniteCarrier(1, ("a",), ((BOTTOM,),), ((0,),)),
            lambda: FiniteCarrier(2, ("a",), ((0, 1),), ((0, 2),)),
            lambda: FiniteCarrier(2, ("a",), ((0, 1),), ((0, 1),), 5),
        ]
        for make in bad:
            with self.assertRaises(ObserverError):
                make()

    def test_partition_matches_existing_carrier_relative_targets(self):
        """Independent implementation cross-check against the attributed module."""
        rng = random.Random(1114)
        for _ in range(300):
            c = random_carrier(rng, rng.randrange(1, 7), rng.randrange(1, 4), rng.randrange(1, 4))
            theirs = crt.behavioral_partition(to_carrier_relative(c))
            owner = {x: i for i, b in enumerate(theirs) for x in b}
            ours = behaviour_blocks(c)
            self.assertTrue(same_partition(ours, tuple(owner[x] for x in range(c.size))))

    def test_k_equivalence_is_bounded_word_agreement(self):
        rng = random.Random(7)
        for _ in range(60):
            c = random_carrier(rng, rng.randrange(1, 5), 2)
            for k in range(4):
                blocks = k_blocks(c, k)
                for x in range(c.size):
                    for y in range(c.size):
                        same = all(transcript(c, w, x) == transcript(c, w, y)
                                   for w in words(c.instruments, k))
                        self.assertEqual(same, blocks[x] == blocks[y])

    def test_identification_bound_exhaustive_and_sharp(self):
        """FO-2a/b: distinct cores of sizes n,m disagree by length n+m-1; n+m-2 attained."""
        for instruments, n_max in ((("a",), 4), (("a", "b"), 3)):
            cores = distinct_cores(n_max, instruments)
            L_max = 2 * n_max - 1
            word_list = list(words(instruments, L_max))
            vecs = [tuple(response_table(k.carrier(), L_max)[w] for w in word_list) for k in cores]
            best = {}
            for L in range(L_max + 1):
                cut = sum(len(instruments) ** i for i in range(1, L + 1))
                groups = {}
                for k, v in zip(cores, vecs):
                    groups.setdefault(v[:cut], []).append(k.size)
                for sizes in groups.values():
                    if len(sizes) < 2:
                        continue
                    s = sorted(sizes)
                    self.assertGreaterEqual(s[0] + s[1], L + 2, "bound n+m-1 violated")
                    counts = {}
                    for size in s:
                        counts[size] = counts.get(size, 0) + 1
                    for a in counts:
                        for b in counts:
                            if a < b or (a == b and counts[a] >= 2):
                                best[(a, b)] = max(best.get((a, b), -1), L)
            for n in range(1, n_max + 1):
                for m in range(n, n_max + 1):
                    self.assertEqual(best[(n, m)], n + m - 2, (instruments, n, m))

    def test_sharp_family_all_small_sizes(self):
        for n in range(1, 8):
            for m in range(1, 8):
                a, b = sharp_pair(n, m)
                self.assertEqual((core(a).size, core(b).size), (n, m))
                self.assertEqual(agreement_horizon(a, b), n + m - 2)
                self.assertEqual(len(first_disagreement(a, b)), n + m - 1)

    def test_same_responses_iff_equal_canonical_cores_with_unique_isomorphism(self):
        rng = random.Random(11)
        pool = [random_carrier(rng, rng.randrange(1, 5), 2, partial=rng.random() < .4)
                for _ in range(150)]
        pool += [c.at(x) for c in pool[:20] for x in range(c.size)]
        for c1 in pool[:90]:
            for c2 in pool[:90]:
                self.assertEqual(first_disagreement(c1, c2) is None, core(c1) == core(c2))
        for c in pool[:40]:
            k = core(c)
            self.assertEqual(core(k.carrier()), k)  # the core is its own core
            isos = 0
            for perm in permutations(range(k.size)):
                if perm[0] != 0:
                    continue
                ok = all(k.rows[s][0] == k.rows[perm[s]][0] and
                         all(perm[k.rows[s][1][a]] == k.rows[perm[s]][1][a]
                             for a in range(len(k.instruments)))
                         for s in range(k.size))
                isos += ok
            self.assertEqual(isos, 1)

    def test_reconstruction_exhaustive(self):
        """FO-2c: lengths <= 2n-1 rebuild the core for every source with core <= n."""
        cases = [(("a",), n) for n in (1, 2, 3, 4)] + [(("a", "b"), n) for n in (1, 2)]
        for instruments, n in cases:
            for c in enumerate_carriers(n, instruments):
                data = response_table(c, 2 * n - 1)
                self.assertEqual(reconstruct_core(instruments, data, n), core(c))
        rng = random.Random(3)
        all3 = list(enumerate_carriers(3, ("a", "b")))
        for c in rng.sample(all3, 2500):
            self.assertEqual(reconstruct_core(c.instruments, response_table(c, 5), 3), core(c))

    def test_reconstruction_mutations(self):
        # Data length 2n-2 cannot suffice: the sharp pair shares it.
        for n in range(2, 6):
            a, b = sharp_pair(n, n)
            self.assertEqual(response_table(a, 2 * n - 2), response_table(b, 2 * n - 2))
            self.assertNotEqual(core(a), core(b))
        # A false size bound can return a smaller consistent machine (no magic detection).
        a, b = sharp_pair(3, 2)
        wrong = reconstruct_core(("a",), response_table(a, 3), 2)
        self.assertEqual(wrong, core(b))
        self.assertNotEqual(wrong, core(a))
        # Missing datum is refused.
        data = response_table(a, 5)
        del data[("a",) * 5]
        with self.assertRaises(ObserverError):
            reconstruct_core(("a",), data, 3)

    def test_partial_carriers_reduce_to_totalized_cores(self):
        cs = []
        for n in (1, 2):
            opts = list(product([None] + list(range(n)), repeat=n))
            for t1, t2 in product(opts, repeat=2):
                for r1, r2 in product(product((0, 1), repeat=n), repeat=2):
                    cs.append(FiniteCarrier(n, ("a", "b"), (r1, r2), (t1, t2), 0))
        cores = {}
        for c in cs:
            cores.setdefault(core(c), c)
        reps = list(cores.items())
        for (k1, c1), (k2, c2) in combinations(reps, 2):
            h = agreement_horizon(c1, c2)
            self.assertIsNotNone(h)
            self.assertLessEqual(h, k1.size + k2.size - 2)
        for c in cs[:400]:
            k = core(c)
            self.assertEqual(reconstruct_core(c.instruments, response_table(c, 2 * k.size - 1), k.size), k)

    def test_unreachable_and_merged_states_are_invisible(self):
        base = FiniteCarrier(1, ("a",), ((0,),), ((0,),))
        unreachable = FiniteCarrier(2, ("a",), ((0, 1),), ((0, 1),))
        merged_swap = FiniteCarrier(2, ("a",), ((0, 0),), ((1, 0),))
        for c in (unreachable, merged_swap):
            self.assertIsNone(first_disagreement(base, c))
            self.assertEqual(core(base), core(c))
        # the hidden state count differs, so it is NOT a response invariant
        self.assertNotEqual(base.size, merged_swap.size)


class ToolkitMonotonicity(unittest.TestCase):

    def test_reduct_core_identity_exhaustive(self):
        """FO-3: core_A(M) = core(core_{A+B}(M)|A); sizes monotone; partition refines."""
        for n in (1, 2, 3):
            for c in enumerate_carriers(n, ("a", "b")):
                left, right = toolkit_reduct_cores(c, ("a",))
                self.assertEqual(left, right)
                self.assertLessEqual(left.size, core(c).size)
                fine, coarse = behaviour_blocks(c), behaviour_blocks(restrict(c, ("a",)))
                for x in range(n):
                    for y in range(n):
                        if fine[x] == fine[y]:
                            self.assertEqual(coarse[x], coarse[y])

    def test_new_readout_exposes_hidden_distinction(self):
        c = FiniteCarrier(2, ("a", "b"), ((0, 0), (0, 1)), ((0, 1), (0, 1)), 0)
        old = restrict(c, ("a",))
        self.assertIsNone(first_disagreement(old.at(0), old.at(1)))
        self.assertEqual(first_disagreement(c.at(0), c.at(1)), ("b",))

    def test_pure_intervention_exposure_needs_three_states(self):
        c = FiniteCarrier(3, ("a", "b"), ((0, 0, 1), (0, 0, 0)), ((0, 1, 2), (0, 2, 2)), 0)
        old = restrict(c, ("a",))
        self.assertIsNone(first_disagreement(old.at(0), old.at(1)))
        self.assertEqual(first_disagreement(c.at(0), c.at(1)), ("b", "a"))
        # exhaustive minimality: on 2 states a constant-readout b never exposes anything
        for c2 in enumerate_carriers(2, ("a", "b")):
            if len(set(c2.readout[1])) != 1:
                continue
            old = restrict(c2, ("a",))
            if first_disagreement(old.at(0), old.at(1)) is None:
                self.assertIsNone(first_disagreement(c2.at(0), c2.at(1)))

    def test_readout_disturbance_pairing_redundant_for_core_only(self):
        """FO-1: splitting (o,t) into measure-only + act-only keeps the core partition."""
        for n in (1, 2, 3):
            for c in enumerate_carriers(n, ("a",)):
                s = split_instrument(c, "a")
                self.assertTrue(same_partition(behaviour_blocks(c), behaviour_blocks(s)))
                self.assertEqual(set(range(n)) & set(_reach(c)), set(_reach(s)) & set(range(n)))
        abc = destructive_abc()
        split = split_instrument(split_instrument(abc, "a"), "b")
        self.assertTrue(same_partition(behaviour_blocks(abc), behaviour_blocks(split)))
        self.assertFalse(free_observability(abc).accessible)
        self.assertTrue(free_observability(split).accessible)


def _reach(c):
    from observational_succ.observatoris_finite_observer import reachable
    return reachable(c)


# --------------------------------------------------------------------------
# A2: interaction-order horizons
# --------------------------------------------------------------------------

def all_functions(k, m):
    return product(range(m), repeat=1 << k)


class InteractionHorizon(unittest.TestCase):

    def test_mobius_inversion_unique_exhaustive(self):
        for k, m in ((1, 3), (2, 3), (3, 2)):
            seen = set()
            for f in all_functions(k, m):
                for c0 in range(1 << k):
                    co = mobius_coefficients(f, k, c0, m)
                    self.assertEqual(synthesize(co, k, c0, m), f)
                    if c0 == 0:
                        seen.add(co)
            self.assertEqual(len(seen), m ** (1 << k))  # bijective, hence unique

    def test_essential_iff_coefficient_and_horizon_equals_ball(self):
        """FO-4 exhaustively over k=3 into Z/2 and k=2 into Z/3, every baseline."""
        for k, m in ((3, 2), (2, 3), (2, 4)):
            for f in all_functions(k, m):
                for c0 in range(1 << k):
                    for j in range(k):
                        h = interaction_horizon(f, k, c0, j, m)
                        self.assertEqual(h is not None, essential(f, k, j))
                        self.assertEqual(h, ball_horizon(f, k, c0, j))
                        for r in range(k + 1):
                            ext = independent_extension(f, k, c0, j, r)
                            if h is None or r < h:
                                self.assertIsNotNone(ext)
                                self.assertFalse(essential(ext, k, j))
                                for x in ball_points(k, r, c0):
                                    self.assertEqual(ext[x], f[x])
                            else:
                                self.assertIsNone(ext)

    def test_and_gate_invisible_below_order_k(self):
        for k in range(1, 6):
            f = tuple(int(x == (1 << k) - 1) for x in range(1 << k))
            zero = tuple(0 for _ in range(1 << k))
            for j in range(k):
                self.assertEqual(interaction_horizon(f, k, 0, j), k)
                self.assertEqual(interaction_horizon(f, k, (1 << k) - 1, j), 1)
            for x in ball_points(k, k - 1, 0):
                self.assertEqual(f[x], zero[x])

    def test_first_order_data_are_the_degree_one_part(self):
        rng = random.Random(5)
        for _ in range(200):
            k = rng.randrange(1, 5)
            f = tuple(rng.randrange(-3, 4) for _ in range(1 << k))
            c0 = rng.randrange(1 << k)
            co = mobius_coefficients(f, k, c0)
            self.assertEqual(co[0], f[c0])
            for j in range(k):
                self.assertEqual(co[1 << j], f[c0 ^ (1 << j)] - f[c0])

    def test_baseline_transport_formula(self):
        """FO-5 exhaustively (k=3, Z/3) and on random Z-valued functions."""
        for f in all_functions(3, 3):
            a0 = mobius_coefficients(f, 3, 0, 3)
            for shift in range(8):
                self.assertEqual(transport_coefficients(a0, 3, shift, 3),
                                 mobius_coefficients(f, 3, shift, 3))
        rng = random.Random(9)
        for _ in range(300):
            k = rng.randrange(1, 6)
            f = tuple(rng.randrange(-5, 6) for _ in range(1 << k))
            b, s = rng.randrange(1 << k), rng.randrange(1 << k)
            self.assertEqual(transport_coefficients(mobius_coefficients(f, k, b), k, s),
                             mobius_coefficients(f, k, b ^ s))

    def test_horizon_range_and_degree_invariance(self):
        for f in all_functions(3, 2):
            co0 = mobius_coefficients(f, 3, 0, 2)
            for j in range(3):
                if not essential(f, 3, j):
                    continue
                dj = variable_degree(co0, j)
                hs = []
                for c0 in range(8):
                    co = mobius_coefficients(f, 3, c0, 2)
                    self.assertEqual(variable_degree(co, j), dj)
                    self.assertEqual(mobius_degree(co), mobius_degree(co0))
                    hs.append(interaction_horizon(f, 3, c0, j, 2))
                self.assertEqual(min(hs), 1)
                self.assertLessEqual(max(hs), dj)

    def test_upper_horizon_not_always_attained(self):
        """REFUTES 'max over baselines of h_j equals deg_j' (receipt, GF(2), k=3).

        f = x3 + x1*x2*x3 = x3 * NAND(x1, x2): deg_3 = 3 but h_3(c) <= 2 at every c.
        """
        f = (0, 0, 0, 0, 1, 1, 1, 0)
        co0 = mobius_coefficients(f, 3, 0, 2)
        self.assertEqual([S for S in range(8) if co0[S]], [4, 7])
        self.assertEqual(variable_degree(co0, 2), 3)
        hs = [interaction_horizon(f, 3, c0, 2, 2) for c0 in range(8)]
        self.assertEqual(hs, [1, 1, 1, 2, 1, 1, 1, 2])
        strict = sum(1 for g in all_functions(3, 2) for j in range(3) if essential(g, 3, j)
                     and max(interaction_horizon(g, 3, c0, j, 2) for c0 in range(8))
                     < variable_degree(mobius_coefficients(g, 3, 0, 2), j))
        self.assertEqual(strict, 192)  # of 720 essential (f, j) pairs

    def test_certification_cost_exhaustive(self):
        """FO-6: exact minimum 2*sum_{i<d} C(k-1,i) evaluations (GF(2), GF(3))."""
        for k in range(1, 5):
            for d in range(0, k + 1):
                for j in {0, k - 1}:
                    self.assertEqual(exhaustive_minimum_certifying(k, d, j, 2),
                                     2 * sum(comb(k - 1, i) for i in range(d)))
        for k in range(1, 4):
            for d in range(0, k + 1):
                self.assertEqual(exhaustive_minimum_certifying(k, d, 0, 3), certification_cost(k, d))
        self.assertEqual(certification_cost(5, 5), 32)

    def test_naive_dimension_count_is_only_half(self):
        for k in range(1, 7):
            for d in range(1, k + 1):
                dim_p = sum(comb(k, i) for i in range(d + 1))
                dim_j = sum(comb(k - 1, i) for i in range(d + 1))
                self.assertEqual(2 * (dim_p - dim_j), certification_cost(k, d))

    def test_unrestricted_class_needs_every_point(self):
        for k in range(1, 5):
            full = tuple(range(1 << k))
            self.assertTrue(certifies_absence(full, k, k, 0, 2))
            for drop in full:
                self.assertFalse(certifies_absence(tuple(x for x in full if x != drop), k, k, 0, 2))

    def test_order_r_ball_certifies_degree_d_iff_r_ge_d(self):
        for k in range(1, 5):
            for d in range(1, k + 1):
                for r in range(0, k + 1):
                    for c0 in (0, (1 << k) - 1):
                        self.assertEqual(certifies_absence(ball_points(k, r, c0), k, d, 0, 2), r >= d)

    def test_finite_value_sets_reduce_to_anchored_subcubes(self):
        vs = ((0, 1, 2), (0, 1, 2))
        ctxs = list(product(*vs))
        for outs in product((0, 1), repeat=9):
            table = dict(zip(ctxs, outs))
            for b in ctxs:
                for j in range(2):
                    h = general_horizon(table, vs, b, j)
                    self.assertEqual(h, general_ball_horizon(table, vs, b, j))
                    self.assertEqual(h is not None, general_essential(table, vs, j))
        vs3 = ((0, 1, 2), (0, 1), (0, 1))
        rng = random.Random(2)
        ctx3 = list(product(*vs3))
        for _ in range(300):
            table = {c: rng.randrange(3) for c in ctx3}
            b = rng.choice(ctx3)
            for j in range(3):
                self.assertEqual(general_horizon(table, vs3, b, j), general_ball_horizon(table, vs3, b, j))

    def test_class_prior_can_lower_the_detection_order(self):
        """The horizon is prior-free; a model-class prior can beat it."""
        g = (0, 1, 0, 2)  # x1 + x1*x2 over Z, index bit0 = x1, bit1 = x2
        self.assertEqual(interaction_horizon(g, 2, 0, 1), 2)
        zero = (0, 0, 0, 0)
        # order-1 data at baseline 0 already separate g from 0, and every nonzero
        # member of the class {0, g} depends on x2:
        self.assertNotEqual(g[1], zero[1])
        self.assertTrue(essential(g, 2, 1))

    def test_polynomial_jets_and_mutations(self):
        rng = random.Random(4)
        for _ in range(60):
            d = rng.randrange(0, 4)
            poly = {}
            for e in product(range(d + 1), repeat=2):
                if sum(e) <= d:
                    poly[e] = Q(rng.randrange(-4, 5), rng.randrange(1, 4))
            base = (Q(rng.randrange(-3, 4)), Q(rng.randrange(-3, 4), 2))
            jet = taylor_jet(poly, base, d)
            for _ in range(5):
                h = (Q(rng.randrange(-5, 6), 3), Q(rng.randrange(-5, 6)))
                self.assertEqual(jet_predict(jet, h), poly_eval(poly, (base[0] + h[0], base[1] + h[1])))
            # mutation: add (x - base_0)^(d+1); same order-d jet, different contrast
            mjet = taylor_jet(_add_flat(poly, base, d), base, d)
            self.assertEqual(mjet, jet)
            self.assertNotEqual(poly_eval(_add_flat(poly, base, d), (base[0] + 1, base[1])),
                                poly_eval(poly, (base[0] + 1, base[1])))
        cube = {(1, 1, 1): Q(1)}
        self.assertEqual({a: v for a, v in taylor_jet(cube, (0, 0, 0), 2).items()}, {})
        grad = taylor_jet(cube, (1, 1, 1), 1)
        self.assertEqual([grad[(1, 0, 0)], grad[(0, 1, 0)], grad[(0, 0, 1)]], [1, 1, 1])


def _add_flat(poly, base, d):
    """poly + (x - base_0)^(d+1), expanded: same d-jet at base, different contrast."""
    out = dict(poly)
    for i in range(d + 2):
        e = (i, 0)
        out[e] = out.get(e, Q(0)) + comb(d + 1, i) * (-Q(base[0])) ** (d + 1 - i)
    return out


# --------------------------------------------------------------------------
# A3: wiring is not a response invariant
# --------------------------------------------------------------------------

BIN = (0, 1)


class HiddenWiring(unittest.TestCase):

    def test_two_path_cancellation_and_minimal_repair(self):
        n1, n0 = cancellation_pair()
        self.assertEqual(n1.response(("x",), "y"), n0.response(("x",), "y"))
        self.assertNotEqual(n1.essential_graph(), n0.essential_graph())
        self.assertTrue(n1.has_essential_path("x", "y"))
        self.assertFalse(n0.has_essential_path("x", "y"))
        do_z1 = [experiment({"x": 1, "z1": 0}, ["y"])]
        self.assertNotEqual(network_data(n1, do_z1), network_data(n0, do_z1))
        read_z1 = [experiment({"x": 1}, ["z1"])]
        self.assertNotEqual(network_data(n1, read_z1), network_data(n0, read_z1))
        # but neither single repair identifies the class (FO-9 needs full clamping)
        n2 = Network([("x", BIN, (), {(): 0}), ("z1", BIN, ("x",), lambda x: x),
                      ("z2", BIN, ("x",), lambda x: x),
                      ("y", (-1, 0, 1), ("z1", "z2"), lambda a, b: 0)])
        self.assertEqual(network_data(n1, read_z1), network_data(n2, read_z1))
        self.assertNotEqual(n1.essential_graph(), n2.essential_graph())

    def test_one_hidden_node_suffices_with_direct_edge(self):
        n1, n0 = minimal_cancellation_pair()
        self.assertEqual(n1.response(("x",), "y"), n0.response(("x",), "y"))
        self.assertTrue(n1.has_essential_path("x", "y"))
        self.assertNotEqual(n1.essential_graph(), n0.essential_graph())

    def test_binary_chain_composes_exhaustively(self):
        """FO-8a: x -> z -> y, binary z: an essential path forces net dependence."""
        sk = (("x", BIN, ()), ("z", BIN, ("x",)), ("y", (0, 1, 2), ("z",)))
        for net in enumerate_networks(sk):
            r = net.response(("x",), "y")
            if net.has_essential_path("x", "y"):
                self.assertNotEqual(r[(0,)], r[(1,)])

    def test_monotone_gating_minimal_sizes(self):
        """FO-8b: monotone gating -- constant gate on a direct edge (1 hidden node);
        a path through a hidden node needs 2 binary hidden nodes; ternary range gate needs 1."""
        sk1 = (("x", BIN, ()), ("z", BIN, ("x",)), ("y", BIN, ("x", "z")))
        direct_gates = 0
        for net in enumerate_networks(sk1, monotone_table):
            r = net.response(("x",), "y")
            g = net.essential_graph()
            if ("x", "z") in g and ("z", "y") in g:  # a path THROUGH the hidden node
                self.assertNotEqual(r[(0,)], r[(1,)])
            if ("x", "y") in g and r[(0,)] == r[(1,)]:
                direct_gates += 1   # constant hidden gate kills a direct essential edge
        self.assertEqual(direct_gates, 4)
        sk2 = (("x", BIN, ()), ("z1", BIN, ("x",)), ("z2", BIN, ("x", "z1")),
               ("y", BIN, ("x", "z1", "z2")))
        hits = [net for net in enumerate_networks(sk2, monotone_table)
                if net.has_essential_path("x", "y")
                and len(set(net.response(("x",), "y").values())) == 1]
        self.assertTrue(hits)
        g = gating_network()
        self.assertTrue(g.has_essential_path("x", "y"))
        self.assertEqual(set(g.response(("x",), "y").values()), {0})
        for n in g.nodes:
            self.assertTrue(monotone_table(n, [g.values[p] for p in g.parents[n]], g.tables[n]))
        rg = range_gate_network()
        self.assertTrue(rg.has_essential_path("x", "y"))
        self.assertEqual(set(rg.response(("x",), "y").values()), {0})
        # signed-cancellation-free: every table is monotone in the declared orders
        for n in rg.nodes:
            self.assertTrue(monotone_table(n, [rg.values[p] for p in rg.parents[n]], rg.tables[n]))

    def test_realized_context_lemma(self):
        sk = (("r", BIN, ()), ("u", BIN, ("r",)), ("v", BIN, ("r", "u")))
        nets = list(enumerate_networks(sk))
        exps = _experiment_universe(sk)
        rng = random.Random(21)
        for _ in range(200):
            fam = tuple(rng.sample(exps, rng.randrange(1, 6)))
            net = rng.choice(nets)
            for node in ("u", "v"):
                rc = realized_contexts(net, fam, node)
                spec = []
                for n in net.nodes:
                    t = dict(net.tables[n])
                    if n == node:
                        for ctx in t:
                            if ctx not in rc and not _evaluated_anywhere(net, fam, node, ctx):
                                t[ctx] = 1 - t[ctx]
                    spec.append((n, net.values[n], net.parents[n], t))
                self.assertEqual(network_data(Network(spec), fam), network_data(net, fam))

    def test_identifiability_criterion_exhaustive_class(self):
        """FO-9: graph identified for the whole class iff the clamp criterion holds."""
        sk = (("r", BIN, ()), ("u", BIN, ("r",)), ("v", BIN, ("r", "u")))
        nets = list(enumerate_networks(sk))
        self.assertEqual(len(nets), 128)
        exps = _experiment_universe(sk)
        required = [experiment({"r": a}, ["u"]) for a in BIN] + \
                   [experiment({"r": a, "u": b}, ["v"]) for a in BIN for b in BIN]
        families = [tuple(required)]
        families += [tuple(x for x in required if x != drop) for drop in required]
        rng = random.Random(1114)
        for _ in range(250):
            fam = set(rng.sample(exps, rng.randrange(1, 12)))
            if rng.random() < 0.5:
                fam |= set(rng.sample(required, rng.randrange(3, 7)))
            families.append(tuple(sorted(fam)))
        agree_true = 0
        for fam in families:
            ok, _ = class_identifies_graph(nets, fam)
            self.assertEqual(ok, clamp_criterion(sk, fam))
            agree_true += ok
        self.assertGreater(agree_true, 0)
        self.assertTrue(class_identifies_graph(nets, tuple(required))[0])
        for drop in required:
            self.assertFalse(class_identifies_graph(nets, tuple(x for x in required if x != drop))[0])

    def test_full_readout_without_clamps_fails(self):
        sk = (("r", BIN, ()), ("u", BIN, ("r",)), ("v", BIN, ("r", "u")))
        nets = list(enumerate_networks(sk))
        observe_all = (experiment({}, ["r", "u", "v"]),)
        self.assertFalse(class_identifies_graph(nets, observe_all)[0])


def _experiment_universe(sk):
    names = [n for n, _, _ in sk]
    exps = []
    for modes in product(("read", "hide", 0, 1), repeat=len(names)):
        clamps = {n: m for n, m in zip(names, modes) if m in (0, 1)}
        reads = [n for n, m in zip(names, modes) if m == "read"]
        exps.append(experiment(clamps, reads))
    return exps


def _evaluated_anywhere(net, fam, node, ctx):
    for clamps, reads in fam:
        cl = dict(clamps)
        if node in cl:
            continue
        st = net.evaluate(cl)
        if tuple(st[p] for p in net.parents[node]) == ctx:
            return True
    return False


# --------------------------------------------------------------------------
# A4: free (single-copy) observability
# --------------------------------------------------------------------------

class FreeObservability(unittest.TestCase):

    def test_destructive_abc_negative_control(self):
        abc = destructive_abc()
        self.assertEqual(len(set(behaviour_blocks(abc))), 3)  # algebra dimension 3
        self.assertTrue(commuting_idempotent(abc))           # refutes C+I => free
        self.assertFalse(free_observability(abc).accessible)
        P = {0: 0, 1: 0, 2: 1}
        self.assertFalse(target_access(abc, P).accessible)
        cr = to_carrier_relative(abc)
        tgt = crt.Target(cr.source, "isC", (Q(0), Q(0), Q(1)))
        self.assertIsNotNone(crt.first_step_erasure_obstruction(cr, tgt))

    def test_positive_controls(self):
        for c, injective in ((nondisturbing_abc(), True), (reset_and_readout(), False),
                             (readout_swap(), True)):
            res = free_observability(c)
            self.assertTrue(res.accessible)
            self.assertEqual(class_injective(c), injective)
            blocks = behaviour_blocks(c)
            for x in range(c.size):
                self.assertEqual(execute_policy(c, res.policy, x), blocks[x])
        self.assertFalse(class_nondisturbing(readout_swap()))

    def test_sufficient_conditions_and_converse_failures_exhaustive(self):
        stats = dict(nd=0, inj=0, free_not_inj=0, ci_not_free=0, free=0)
        for n in (1, 2, 3):
            for c in enumerate_carriers(n, ("a", "b")):
                res = free_observability(c)
                blocks, q, _, _ = quotient(c)
                if res.accessible:
                    stats["free"] += 1
                    self.assertLessEqual(res.depth, q * (q - 1) // 2)
                    for x in range(n):
                        self.assertEqual(execute_policy(c, res.policy, x), blocks[x])
                if class_nondisturbing(c):
                    stats["nd"] += 1
                    self.assertTrue(res.accessible)
                    sig = {}
                    for x in range(n):
                        sig.setdefault(transcript(c, c.instruments, x), set()).add(blocks[x])
                    self.assertTrue(all(len(s) == 1 for s in sig.values()))
                if class_injective(c):
                    stats["inj"] += 1
                    self.assertTrue(res.accessible)
                    self.assertLessEqual(res.depth, (q - 1) * (q - 1))
                elif res.accessible:
                    stats["free_not_inj"] += 1
                if commuting_idempotent(c) and not res.accessible:
                    stats["ci_not_free"] += 1
        self.assertGreater(stats["free_not_inj"], 0)
        self.assertGreater(stats["ci_not_free"], 0)

    def test_free_implies_every_algebra_target_accessible(self):
        rng = random.Random(8)
        for _ in range(150):
            c = random_carrier(rng, rng.randrange(1, 5), rng.randrange(1, 4))
            blocks = behaviour_blocks(c)
            ks = sorted(set(blocks[x] for x in range(c.size)))
            free = free_observability(c).accessible
            self.assertEqual(free, target_access(c, {x: blocks[x] for x in range(c.size)}).accessible)
            if free:
                for bits in product((0, 1), repeat=len(ks)):
                    P = {x: bits[ks.index(blocks[x])] for x in range(c.size)}
                    self.assertTrue(target_access(c, P).accessible)

    def test_targetwise_access_does_not_compose(self):
        """FO-10d receipt: all 8 Boolean targets on {A,B,C} accessible, class not."""
        c = separately_but_not_jointly()
        S = (0, 1, 2)
        self.assertEqual(len(set(behaviour_blocks(c))), 4)
        for bits in product((0, 1), repeat=3):
            res = target_access(c, dict(zip(S, bits)), S)
            self.assertTrue(res.accessible)
            for x in S:
                self.assertEqual(execute_policy(c, res.policy, x), bits[x])
        self.assertFalse(free_observability(c, S).accessible)
        self.assertFalse(class_injective(c))

    def test_cross_check_with_existing_bounded_planner(self):
        rng = random.Random(1)
        for _ in range(120):
            c = random_carrier(rng, rng.randrange(2, 5), 2)
            cr = to_carrier_relative(c)
            vals = tuple(rng.randrange(2) for _ in range(c.size))
            ours = target_access(c, dict(enumerate(vals)))
            theirs = crt.plan_target(cr, crt.Target(cr.source, "P", tuple(map(Q, vals))), 8)
            if ours.accessible and ours.depth <= 8:
                self.assertEqual(theirs.worst_cost, ours.depth)
            else:
                self.assertIsNone(theirs.policy)

    def test_target_not_constant_on_class_is_refused(self):
        c = FiniteCarrier(2, ("a",), ((0, 0),), ((0, 1),))
        self.assertFalse(target_access(c, {0: 0, 1: 1}).accessible)


if __name__ == "__main__":
    unittest.main()
