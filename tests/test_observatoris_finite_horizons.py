"""OPUS III finite-horizon theorems FH-1..FH-14: exact positive, negative,
mutation and holdout tests, with exhaustive small-model searches that could
have falsified each horizon constant.  Finite searches are evidence for the
declared finite models only; the general statements are proved in
research/2026-11-14/principia_observatoris_second_forge/agents/OPUS_III_HORIZON_HUNTER.md.
"""
import random
import unittest
from fractions import Fraction as F
from itertools import combinations, product

from observational_succ.observatoris_finite_horizons import (
    QQ, GF, HorizonError, WeightedAutomaton, all_machine_rhos, all_rhos,
    annihilates, berlekamp_massey, canonical_rho, certifier_counterexample,
    char_poly, companion_automaton, conservative_learner_trace, counter_gate,
    det, deterministic_generative_hmm, deterministic_pa,
    eventually_constant_in_class, extremal_linear_pair, extremal_machine_pair,
    fool_protocol_on_founding_pair, founding_b, founding_b_order, generate,
    hankel_rank, harmonic, harmonic_mimic, harmonic_mimic_deviation,
    hilbert_det_closed_form, impulse, lcp, linear_complexity_bruteforce,
    machine_rho, max_agreement_bruteforce, max_agreement_of_distinct, max_first_difference,
    mind_changes, modulus_limit_interval, monic_polys, moore_exhaustive_max,
    pointer_member, pointer_protocol, poly_lcm_degree, poly_mul,
    poly_recurrence_class_gf, poly_recurrence_extremal, randomized_error_sum,
    recurrence_class_gf, rho_first_difference, rho_prefix, run_protocol,
    shortest_distinguishing_length, symbol_ever_appears, wa_first_difference,
    wa_first_difference_bruteforce, worst_case_limit_oscillation,
)


def mat_mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def markov(A, B, C, count):
    out, P = [], B
    for _ in range(count):
        out.append(tuple(tuple(r) for r in mat_mul(C, P)))
        P = mat_mul(A, P)
    return out


# ---------------------------------------------------------------- FH-1/2
class ReadoutImpossibilityTests(unittest.TestCase):
    """FH-1 (deterministic adaptive) and FH-2 (randomised)."""

    def protocols(self):
        def fixed(ask, coins=()):
            return "LIMIT" if all(ask(i) == F(1, i + 1) for i in (0, 3, 17)) else "FINITE"

        def adaptive(ask, coins=()):
            i = 0
            while ask(i) > F(1, 40):          # reads until the value is small
                i = 2 * i + 1
            return "LIMIT" if ask(i + 5) == F(1, i + 6) else "FINITE"

        def value_steered(ask, coins=()):
            v = ask(2)
            k = int(1 / v) * 7               # next index depends on an answer
            return "LIMIT" if ask(k) == F(1, k + 1) else "FINITE"
        return (fixed, adaptive, value_steered)

    def test_every_terminating_adaptive_protocol_is_fooled(self):
        for proto in self.protocols():
            r = fool_protocol_on_founding_pair(proto)
            self.assertTrue(r["same_transcript"])
            self.assertEqual(r["decision_a"], "LIMIT")
            # b_H nevertheless breaks the law at H+1 and has limit 1
            b = founding_b(r["H"], r["H"] + 3)
            self.assertNotEqual(b[r["H"] + 1], F(1, r["H"] + 2))

    def test_pointer_class_refutes_existential_pair_condition_for_adaptive(self):
        # weak condition: every finite Q admits two members equal on Q with
        # different target -- verified exhaustively for Q inside [0,7]
        for size in range(0, 5):
            for Q in combinations(range(8), size):
                k = max(Q, default=0) + 1           # pointer beyond Q
                x, y = pointer_member(k, 0), pointer_member(k, 1)
                self.assertTrue(all(x(i) == y(i) for i in Q))
        # ... yet a 2-query adaptive protocol decides the target exactly
        for k in range(40):
            for bit in (0, 1):
                dec, asked = run_protocol(pointer_protocol, pointer_member(k, bit))
                self.assertEqual(dec, bit)
                self.assertEqual(asked, (0, k + 1))

    def test_randomised_error_sum_is_at_least_one(self):
        def rnd(ask, coins):
            idx = sum(c << i for i, c in enumerate(coins))       # 0..7
            return "LIMIT" if ask(idx) == F(1, idx + 1) else "FINITE"
        a = lambda i: F(1, i + 1)
        for H in (7, 8, 30):            # every coin-run on a queries <= 7
            b = lambda i, H=H: F(1, i + 1) if i <= H else F(1)
            s = randomized_error_sum(rnd, a, b, "LIMIT", "FINITE", 3)
            self.assertGreaterEqual(s, 1)
        # MUTATION: if H is allowed below the query range the bound may fail
        b3 = lambda i: F(1, i + 1) if i <= 3 else F(1)
        self.assertLess(randomized_error_sum(rnd, a, b3, "LIMIT", "FINITE", 3), 1)

    def test_bounded_family_mutation_is_decidable(self):
        # dropping 'H unbounded': for H <= 9 one query at 10 decides
        for H in range(10):
            self.assertNotEqual(founding_b(H, 11)[10], harmonic(11)[10])


# ------------------------------------------------------------------ FH-3
class LinearRecurrenceHorizonTests(unittest.TestCase):

    def test_extremal_pair_all_fields_and_degenerate_cases(self):
        for field in (QQ, GF(2), GF(3), GF(5)):
            for n in range(0, 7):
                for m in range(0, 7):
                    if n == m == 0:
                        with self.assertRaises(HorizonError):
                            extremal_linear_pair(0, 0, 4, field)
                        continue
                    e = extremal_linear_pair(n, m, n + m + 8, field)
                    self.assertTrue(annihilates(e["poly_a"], e["a"], field))
                    self.assertTrue(annihilates(e["poly_b"], e["b"], field))
                    self.assertEqual(len(e["poly_a"]) - 1, n)
                    self.assertEqual(len(e["poly_b"]) - 1, m)
                    self.assertEqual(lcp(e["a"], e["b"]), n + m - 1)

    def test_exhaustive_gf2_gf3_gf5_horizon_is_exactly_n_plus_m(self):
        cases = [(2, n, m) for n in range(1, 5) for m in range(n, 5)]
        cases += [(3, n, m) for n in range(1, 3) for m in range(n, 3)]
        cases += [(5, 1, 1), (5, 1, 2)]
        for p, n, m in cases:
            G = GF(p)
            L = p ** (n + m)       # pigeonhole: equal on p^(n+m) terms => equal
            S = recurrence_class_gf(G, n, L)
            T = recurrence_class_gf(G, m, L)
            self.assertEqual(max_agreement_of_distinct(S, T), n + m - 1, (p, n, m))

    def test_restricted_polynomial_families_follow_max_lcm_degree(self):
        # FH-3b: invertible (no nilpotent part) recurrences over GF(2)
        G = GF(2)
        for n, m in ((1, 1), (1, 2), (2, 2), (1, 3), (2, 3)):
            P = [q for d in range(n + 1) for q in monic_polys(d, G, invertible=True)]
            Q = [q for d in range(m + 1) for q in monic_polys(d, G, invertible=True)]
            predicted = max(poly_lcm_degree(p, q, G) for p in P for q in Q)
            L = 2 ** (n + m)
            S = recurrence_class_gf(G, n, L, invertible=True)
            T = recurrence_class_gf(G, m, L, invertible=True)
            self.assertEqual(max_agreement_of_distinct(S, T) + 1, predicted, (n, m))
        self.assertEqual(max_agreement_of_distinct(
            recurrence_class_gf(G, 1, 4, invertible=True),
            recurrence_class_gf(G, 1, 4, invertible=True)) + 1, 1)   # anomaly: not 2

    def test_sorted_neighbour_agreement_matches_bruteforce(self):
        r = random.Random(5)
        for _ in range(60):
            S = {tuple(r.randrange(3) for _ in range(6)) for _ in range(r.randint(1, 12))}
            T = {tuple(r.randrange(3) for _ in range(6)) for _ in range(r.randint(1, 12))}
            self.assertEqual(max_agreement_of_distinct(S, T), max_agreement_bruteforce(S, T))

    def test_small_integer_exhaustive_over_Q(self):
        vals = (-1, 0, 1)
        for n, m in ((1, 1), (1, 2), (2, 2)):
            W = 3 * (n + m) + 6
            S = {generate(c, i, W) for c in product(vals, repeat=n) for i in product(vals, repeat=n)}
            T = {generate(c, i, W) for c in product(vals, repeat=m) for i in product(vals, repeat=m)}
            self.assertLessEqual(max_agreement_of_distinct(S, T), n + m - 1)

    def test_mutation_short_horizon_and_non_monic(self):
        for n, m in ((1, 1), (2, 3), (4, 4)):
            e = extremal_linear_pair(n, m, n + m + 2)
            k = n + m - 1      # a checker using horizon n+m-1 declares equality...
            self.assertEqual(e["a"][:k], e["b"][:k])
            self.assertNotEqual(e["a"], e["b"])  # ...wrongly
        # non-monic 'recurrence' 0*s(k+1) = 0*s(k) is satisfied by everything
        self.assertTrue(annihilates((0, 0), harmonic(20)))

    def test_bm_matches_independent_bruteforce_holdout(self):
        r = random.Random(20261114)
        for field in (QQ, GF(3)):
            for _ in range(150):
                s = [field.coerce(r.randint(-2, 2)) for _ in range(r.randint(0, 9))]
                L, c = berlekamp_massey(s, field)
                self.assertEqual(L, linear_complexity_bruteforce(s, field))
                self.assertEqual(generate(c, s[:L], len(s), field), tuple(s))

    def test_holdout_large_orders(self):
        for n, m in ((10, 13), (17, 3), (0, 21)):
            e = extremal_linear_pair(n, m, n + m + 4)
            self.assertEqual(lcp(e["a"], e["b"]), n + m - 1)
            d = tuple(x - y for x, y in zip(e["a"], e["b"]))
            self.assertLessEqual(berlekamp_massey(d)[0], n + m)


# ------------------------------------------------------------------ FH-4
class LTIMarkovTests(unittest.TestCase):

    def companion_system(self, coeffs, init):
        L = len(coeffs)
        A = [[F(0)] * L for _ in range(L)]
        for i in range(L - 1):
            A[i][i + 1] = F(1)
        A[L - 1] = [F(c) for c in coeffs]
        B = [[F(v)] for v in init]
        C = [[F(1)] + [F(0)] * (L - 1)]
        return A, B, C

    def test_siso_extremal_pair_realised_with_dims_n_and_m(self):
        for n, m in ((1, 1), (2, 3), (3, 3), (4, 2)):
            e = extremal_linear_pair(n, m, n + m + 3)
            sys_a = self.companion_system([-x for x in e["poly_a"][:-1]], e["a"][:n])
            sys_b = self.companion_system([-x for x in e["poly_b"][:-1]], e["b"][:m])
            ha = [h[0][0] for h in markov(*sys_a, n + m + 3)]
            hb = [h[0][0] for h in markov(*sys_b, n + m + 3)]
            self.assertEqual(tuple(ha), e["a"])
            self.assertEqual(tuple(hb), e["b"])
            self.assertEqual(lcp(ha, hb), n + m - 1)

    def test_cayley_hamilton_and_kronecker_scalar(self):
        r = random.Random(1114)
        for _ in range(25):
            n = r.randint(1, 4)
            A = [[F(r.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
            B = [[F(r.randint(-2, 2))] for _ in range(n)]
            C = [[F(r.randint(-2, 2)) for _ in range(n)]]
            h = [x[0][0] for x in markov(A, B, C, 2 * n + 6)]
            L, _ = berlekamp_massey(h)
            self.assertLessEqual(L, n)                       # Cayley-Hamilton
            self.assertEqual(hankel_rank(h, n + 3), L)       # Kronecker (scalar)

    def test_mimo_zero_padding_keeps_horizon_sharp(self):
        n, m = 3, 2
        e = extremal_linear_pair(n, m, n + m + 2)
        pad = lambda v: ((v, F(0)), (F(0), F(0)), (F(0), F(0)))      # 3x2 outputs
        Ha, Hb = [pad(v) for v in e["a"]], [pad(v) for v in e["b"]]
        self.assertEqual(lcp(Ha, Hb), n + m - 1)
        r = random.Random(77)
        A = [[F(r.randint(-1, 1)) for _ in range(3)] for _ in range(3)]
        Bm = [[F(r.randint(-1, 1)) for _ in range(2)] for _ in range(3)]
        Cm = [[F(r.randint(-1, 1)) for _ in range(3)] for _ in range(2)]
        hs = markov(A, Bm, Cm, 12)
        for i in range(2):
            for j in range(2):
                self.assertLessEqual(berlekamp_massey([h[i][j] for h in hs])[0], 3)

    def test_feedthrough_convention_costs_one_more_parameter(self):
        n, m = 2, 3
        e = extremal_linear_pair(n, m, n + m + 3)
        Da = Db = F(5)                       # equal feedthrough h_0 = D
        ha, hb = (Da,) + e["a"], (Db,) + e["b"]
        self.assertEqual(lcp(ha, hb), n + m)    # (D,CB,CAB,...) needs n+m+1 terms


# ------------------------------------------------------------------ FH-5
class LimitIdentificationTests(unittest.TestCase):

    def test_exhaustive_learner_stabilises_by_2d_with_at_most_2d_changes(self):
        for p, nmax in ((2, 4), (3, 2)):
            G = GF(p)
            worst = {}
            for s in recurrence_class_gf(G, nmax, 4 * nmax + 4):
                d = berlekamp_massey(s, G)[0]
                tr = conservative_learner_trace(s, G)
                truth = tr[-1]
                self.assertEqual(generate(truth[0], truth[1], len(s), G), s)
                stab = max((t for t in range(len(tr)) if tr[t] != truth), default=-1) + 1
                mc = len(mind_changes(tr))
                self.assertLessEqual(stab, 2 * d)
                self.assertLessEqual(mc, 2 * d)
                w = worst.setdefault(d, [0, 0])
                w[0], w[1] = max(w[0], stab), max(w[1], mc)
            for d, (stab, mc) in worst.items():   # OBSERVED: both bounds attained
                self.assertEqual((stab, mc), (2 * d, 2 * d))

    def test_no_learner_is_right_on_both_extremal_sequences_at_2d_minus_1(self):
        for d in range(1, 6):
            # Repaired after adversarial review (the earlier assertion could not
            # fail).  The claim quantifies over ALL learners; a learner is a
            # function of the prefix, so the falsifiable content is that two
            # DISTINCT members of LR_d share the prefix of length 2d-1.
            e = extremal_linear_pair(d, d, 2 * d + 2)
            a, b = list(e["a"]), list(e["b"])
            self.assertEqual(a[:2 * d - 1], b[:2 * d - 1])
            self.assertNotEqual(a[2 * d - 1], b[2 * d - 1])
            self.assertLessEqual(berlekamp_massey(a)[0], d)
            self.assertLessEqual(berlekamp_massey(b)[0], d)

    def test_every_halting_certifier_is_unsound(self):
        x = generate((F(1), F(1)), (F(0), F(1)), 40)        # Fibonacci, order 2
        for t in range(0, 30):                               # certifier halts at t
            y = certifier_counterexample(x, t)
            self.assertEqual(y[:t], x[:t])
            self.assertNotEqual(y[t], x[t])
            self.assertLessEqual(berlekamp_massey(y)[0], 2 + t + 1)  # still in LR

    def test_adversary_forces_any_number_of_mind_changes(self):
        for k in range(1, 5):
            N = [2 * 3 ** i for i in range(k)]
            L = 2 * N[-1] + 4
            x = [F(0)] * L
            for Ni in N:
                x[Ni] = F(1)
            self.assertGreaterEqual(len(mind_changes(conservative_learner_trace(x))), k)


# ------------------------------------------------------------------ FH-6
class FoundingPairInLinearTheoryTests(unittest.TestCase):

    def test_hilbert_determinants_cauchy_formula_nonzero(self):
        for N in range(1, 11):
            Hm = [[F(1, i + j + 1) for j in range(N)] for i in range(N)]
            self.assertEqual(det(Hm), hilbert_det_closed_form(N))
            self.assertNotEqual(hilbert_det_closed_form(N), 0)
        for N in range(1, 13):
            self.assertEqual(berlekamp_massey(harmonic(2 * N))[0], N)  # full complexity

    def test_order_of_b_H_is_H_plus_2(self):
        for H in range(0, 16):
            b = founding_b(H, 2 * H + 12)
            self.assertEqual(berlekamp_massey(b)[0], founding_b_order(H))
            if H >= 1:
                ann = poly_mul((0,) * (H + 1) + (1,), (-1, 1))      # x^{H+1}(x-1)
                self.assertTrue(annihilates(ann, b))

    def test_dimension_n_mimic_agrees_exactly_2n_terms(self):
        for n in range(1, 10):
            x = harmonic_mimic(n, 2 * n + 1)
            a = harmonic(2 * n + 1)
            self.assertEqual(lcp(x, a), 2 * n)
            self.assertEqual(a[2 * n] - x[2 * n], harmonic_mimic_deviation(n))
            self.assertLessEqual(berlekamp_massey(harmonic_mimic(n, 2 * n + 6))[0], n)
            self.assertEqual(harmonic_mimic_deviation(n),
                             hilbert_det_closed_form(n + 1) / hilbert_det_closed_form(n))

    def test_declared_dimension_admits_b_H_iff_H_le_n_minus_2(self):
        # Repaired after adversarial review: the order is now MEASURED from the
        # data by Berlekamp-Massey instead of read from the closed form, and the
        # case H = 0 (order 1) is included.
        for H in range(0, 12):
            length = 2 * (H + 2) + 4
            data = [F(1, k + 1) if k <= H else F(1) for k in range(length)]
            order = berlekamp_massey(data)[0]
            self.assertEqual(order, founding_b_order(H))
            for n in range(1, 9):
                self.assertEqual(order <= n, H == 0 or H <= n - 2)


# ------------------------------------------------------------------ FH-7
class AutonomousMachineTests(unittest.TestCase):

    def test_rho_enumeration_equals_machine_enumeration(self):
        self.assertEqual(all_rhos(3, (0, 1)), all_machine_rhos(3, (0, 1)))
        self.assertEqual(all_rhos(2, "abc"), all_machine_rhos(2, "abc"))

    def test_exhaustive_horizon_is_n_plus_m_minus_1(self):
        R = {n: all_rhos(n, (0, 1)) for n in range(1, 7)}
        for n in range(1, 7):
            for m in range(n, 7):
                if n + m <= 10:
                    self.assertEqual(max_first_difference(R[n], R[m]), n + m - 2, (n, m))
        R3 = {n: all_rhos(n, (0, 1, 2)) for n in range(1, 5)}
        for n in range(1, 5):
            for m in range(n, 5):
                if n + m <= 7:
                    self.assertEqual(max_first_difference(R3[n], R3[m]), n + m - 2)

    def test_extremal_machine_pair_and_mutation(self):
        for n in range(1, 10):
            for m in range(1, 10):
                e = extremal_machine_pair(n, m)
                r1 = machine_rho(*e["machine_n"])
                r2 = machine_rho(*e["machine_m"])
                k = rho_first_difference(r1, r2)
                self.assertEqual(k, n + m - 2)
                # MUTATION: a checker with horizon n+m-2 declares them equal
                self.assertEqual(rho_prefix(r1, n + m - 2), rho_prefix(r2, n + m - 2))

    def test_hyperplane_lemma_difference_has_linear_complexity_le_n_plus_m_minus_1(self):
        R = {n: all_rhos(n, (0, 1)) for n in range(1, 5)}
        for n in range(1, 5):
            for m in range(n, 5):
                worst = 0
                for x in R[n]:
                    for y in R[m]:
                        d = [F(u - v) for u, v in zip(rho_prefix(x, 2 * (n + m) + 2),
                                                      rho_prefix(y, 2 * (n + m) + 2))]
                        worst = max(worst, berlekamp_massey(d)[0])
                self.assertEqual(worst, n + m - 1)

    def test_k_bit_counter_hides_first_deviation_until_2k_minus_1(self):
        for k in range(0, 8):
            delta, out = counter_gate(k)
            r = machine_rho(delta, out)
            zero = canonical_rho((), (0,))
            self.assertEqual(rho_first_difference(r, zero), 2 ** k - 1)
            self.assertEqual(rho_first_difference(r, zero), len(delta) + 1 - 2)

    def test_symbol_search_bound_is_n(self):
        for n in range(1, 6):
            for pre, cyc in all_rhos(n, (0, 1)):
                appears = 1 in pre or 1 in cyc
                self.assertEqual(appears, 1 in rho_prefix((pre, cyc), n))
        delta, out = counter_gate(3)          # chain: '1' first at index n-1
        self.assertTrue(symbol_ever_appears(delta, out, 0, 1))
        self.assertNotIn(1, rho_prefix(machine_rho(delta, out), 7))


# ------------------------------------------------------------------ FH-8
class MooreMealyTests(unittest.TestCase):

    def test_exhaustive_two_letter_machines(self):
        self.assertEqual(moore_exhaustive_max(2, 2, 2, "moore"), 0)
        self.assertEqual(moore_exhaustive_max(3, 2, 2, "moore"), 1)
        self.assertEqual(moore_exhaustive_max(2, 2, 2, "mealy"), 1)
        self.assertEqual(moore_exhaustive_max(3, 2, 2, "mealy"), 2)

    def test_random_holdout_and_chain_sharpness(self):
        r = random.Random(4242)
        for N in (4, 5, 6):
            for _ in range(400):
                delta = [tuple(r.randrange(N) for _ in range(2)) for _ in range(N)]
                out = [r.randrange(2) for _ in range(N)]
                mout = [tuple(r.randrange(2) for _ in range(2)) for _ in range(N)]
                for s, t in combinations(range(N), 2):
                    d = shortest_distinguishing_length(delta, out, s, t, "moore")
                    self.assertTrue(d is None or d <= N - 2)
                    d = shortest_distinguishing_length(delta, mout, s, t, "mealy")
                    self.assertTrue(d is None or d <= N - 1)
            # sharpness: disjoint union of the FH-7 extremal pair (n+m = N)
            e = extremal_machine_pair(N - 2, 2)
            d1, o1 = e["machine_n"]
            d2, o2 = e["machine_m"]
            delta = [(q,) for q in d1] + [(q + len(d1),) for q in d2]
            out = list(o1) + list(o2)
            self.assertEqual(shortest_distinguishing_length(delta, out, 0, len(d1), "moore"), N - 2)
            mealy_out = [(o,) for o in out]
            self.assertEqual(shortest_distinguishing_length(delta, mealy_out, 0, len(d1), "mealy"), N - 1)


# ------------------------------------------------------------------ FH-9
class WeightedAutomatonTests(unittest.TestCase):

    def rand_wa(self, r, n, letters="xy"):
        v = lambda: F(r.randint(-2, 2), r.randint(1, 2))
        return WeightedAutomaton([v() for _ in range(n)],
                                 {a: [[v() for _ in range(n)] for _ in range(n)] for a in letters},
                                 [v() for _ in range(n)])

    def test_span_algorithm_matches_bruteforce_and_bound(self):
        r = random.Random(31)
        for _ in range(120):
            n, m = r.randint(1, 3), r.randint(1, 3)
            A, B = self.rand_wa(r, n), self.rand_wa(r, m)
            k, w = wa_first_difference(A, B)
            self.assertEqual(k, wa_first_difference_bruteforce(A, B, n + m + 1))
            if k is not None:
                self.assertLessEqual(k, n + m - 1)
                self.assertNotEqual(A.value(w), B.value(w))

    def test_one_letter_extremal_attains_n_plus_m_minus_1(self):
        for n in range(1, 6):
            for m in range(1, 6):
                e = extremal_linear_pair(n, m, 1)
                full = extremal_linear_pair(n, m, n + m)
                A = companion_automaton([-x for x in e["poly_a"][:-1]], full["a"][:n])
                B = companion_automaton([-x for x in e["poly_b"][:-1]], full["b"][:m])
                self.assertEqual(wa_first_difference(A, B)[0], n + m - 1)
                self.assertFalse(A.is_rabin_pa() and B.is_rabin_pa())   # mutation witness

    def test_rabin_pa_bound_is_n_plus_m_minus_2(self):
        for n in range(1, 6):
            for m in range(1, 6):
                e = extremal_machine_pair(n, m)
                A = deterministic_pa(*e["machine_n"])
                B = deterministic_pa(*e["machine_m"])
                self.assertTrue(A.is_rabin_pa() and B.is_rabin_pa())
                self.assertEqual(wa_first_difference(A, B)[0], n + m - 2)
        r = random.Random(99)
        vals = [F(0), F(1, 3), F(1, 2), F(1)]

        def rpa(n):
            mats = {}
            for a in "xy":
                M = []
                for _ in range(n):
                    cut = sorted(r.choice(vals) for _ in range(n - 1))
                    pts = [F(0)] + cut + [F(1)]
                    M.append([pts[j + 1] - pts[j] for j in range(n)])
                mats[a] = M
            al = [F(1)] + [F(0)] * (n - 1)
            return WeightedAutomaton(al, mats, [r.choice(vals) for _ in range(n)])
        for _ in range(300):
            n, m = r.randint(1, 3), r.randint(1, 3)
            A, B = rpa(n), rpa(m)
            self.assertTrue(A.is_rabin_pa() and B.is_rabin_pa())
            k, _ = wa_first_difference(A, B)
            self.assertTrue(k is None or k <= n + m - 2)

    def test_genuinely_stochastic_sharp_examples(self):
        A = WeightedAutomaton([1, 0], {"x": [[F(1, 4), F(3, 4)], [0, 1]], "y": [[0, 1], [1, 0]]}, [0, F(1, 4)])
        B = WeightedAutomaton([1, 0], {"x": [[F(1, 4), F(3, 4)], [F(1, 2), F(1, 2)]], "y": [[0, 1], [1, 0]]}, [0, F(1, 4)])
        self.assertTrue(A.is_rabin_pa() and B.is_rabin_pa())
        self.assertEqual(wa_first_difference(A, B), (2, ("x", "x")))
        self.assertEqual((A.value("xx"), B.value("xx")), (F(15, 64), F(9, 64)))
        H1 = WeightedAutomaton([F(1, 2), F(1, 2)],
                               {"a": [[0, F(1, 2)], [0, F(1, 4)]], "b": [[F(1, 4), F(1, 4)], [F(1, 2), F(1, 4)]]}, [1, 1])
        H2 = WeightedAutomaton([F(1, 4), F(3, 4)],
                               {"a": [[0, 0], [F(1, 4), F(1, 4)]], "b": [[F(1, 2), F(1, 2)], [0, F(1, 2)]]}, [1, 1])
        self.assertTrue(H1.is_generative_hmm() and H2.is_generative_hmm())
        self.assertEqual(wa_first_difference(H1, H2)[0], 3)
        self.assertEqual(wa_first_difference_bruteforce(H1, H2, 4), 3)

    def test_generative_hmm_deterministic_extremal_attains_n_plus_m_minus_1(self):
        for n in range(1, 6):
            for m in range(1, 6):
                e = extremal_machine_pair(n, m)
                A = deterministic_generative_hmm(*e["machine_n"], (0, 1))
                B = deterministic_generative_hmm(*e["machine_m"], (0, 1))
                self.assertTrue(A.is_generative_hmm() and B.is_generative_hmm())
                self.assertEqual(wa_first_difference(A, B)[0], n + m - 1)


# ------------------------------------------------------------------ FH-10
class ModulusOscillationTests(unittest.TestCase):
    MUS = {"harmonic": lambda k: F(1, k + 1), "geometric": lambda k: F(1, 2 ** k),
           "square": lambda k: F(1, (k + 1) ** 2), "flat": lambda k: F(1)}

    def test_exhaustive_grid_fibre_interval_exact(self):
        grid = [F(v, 4) for v in range(-4, 5)]
        for name, mu in self.MUS.items():
            for N in (1, 2, 3):
                for prefix in product(grid, repeat=N):
                    I = modulus_limit_interval(prefix, mu)
                    if I is None:
                        continue
                    lo, hi = I
                    self.assertLessEqual(lo, hi)
                    self.assertLessEqual(hi - lo, worst_case_limit_oscillation(N, mu))
                    for L in (lo, hi, (lo + hi) / 2):
                        self.assertTrue(eventually_constant_in_class(prefix, L, mu))
                    for L in (lo - F(1, 64), hi + F(1, 64)):
                        self.assertFalse(eventually_constant_in_class(prefix, L, mu))
                const = modulus_limit_interval((F(0),) * N, mu)
                self.assertEqual(const[1] - const[0], 2 * mu(N - 1))     # attained

    def test_mutation_mu_N_instead_of_mu_N_minus_1(self):
        mu = self.MUS["harmonic"]
        for N in range(1, 8):
            lo, hi = modulus_limit_interval((F(0),) * N, mu)
            self.assertGreater(hi - lo, 2 * mu(N))

    def test_founding_pair_under_harmonic_modulus(self):
        mu = self.MUS["harmonic"]
        for N in range(1, 12):
            self.assertEqual(modulus_limit_interval(harmonic(N), mu), (F(0), F(2, N)))
        self.assertTrue(eventually_constant_in_class(founding_b(0, 1), 1, mu))
        self.assertTrue(eventually_constant_in_class(founding_b(1, 2), 1, mu))
        self.assertEqual(modulus_limit_interval(founding_b(1, 2), mu), (F(0), F(1)))
        for H in range(2, 15):
            b = founding_b(H, H + 2)
            self.assertGreater(abs(b[H] - b[H + 1]), mu(H))          # modulus violated

    def test_without_modulus_any_limit_extends_any_prefix(self):
        huge = lambda k: F(10 ** 9)
        I = modulus_limit_interval(harmonic(5), huge)
        self.assertGreater(I[1] - I[0], 10 ** 9)


# ------------------------------------------------------------- FH-11/12
class TopologyAndHierarchyTests(unittest.TestCase):

    def test_impulse_class_certifiable_but_no_uniform_horizon(self):
        for N in range(1, 30):
            x, y = impulse(N, N + 2), impulse(N + 1, N + 2)
            self.assertEqual(lcp(x, y), N)            # no uniform horizon
            first_one = x.index(1)                     # certifier: halt at first 1
            self.assertEqual(first_one, N)
        zero = (F(0),) * 40                            # adding 0: 0 is a limit point
        self.assertEqual(lcp(zero, impulse(39, 40)), 39)

    def test_pi03_reduction_formula(self):
        def y(z, K):
            pairs = [(m, n) for s in range(K) for m in range(s + 1) for n in [s - m]]
            return [F(1, 2 ** k) + (F(1, m + 1) if z(m, n) else 0) for k, (m, n) in enumerate(pairs[:K])]
        ev_zero = lambda m, n: n < 3            # every row eventually 0
        bad_row = lambda m, n: m == 2           # row 2 infinitely often 1
        yz, yb = y(ev_zero, 300), y(bad_row, 300)
        self.assertTrue(all(v > 0 for v in yz + yb))
        self.assertLess(max(yz[250:]), F(1, 2 ** 200) + F(1, 10))
        self.assertGreaterEqual(max(yb[250:]), F(1, 3))


# ------------------------------------------------------------------ FH-14
class PolynomialRecurrenceTests(unittest.TestCase):

    def test_exhaustive_finite_field_horizon_d_plus_2(self):
        for p, d in ((5, 1), (5, 2), (7, 1), (7, 2)):
            G = GF(p)
            S = poly_recurrence_class_gf(G, d, p * p + 1)   # pigeonhole on (x_k, y_k)
            self.assertEqual(max_agreement_of_distinct(S, S), d + 1, (p, d))

    def test_rational_extremal_and_mutation(self):
        for d in range(1, 7):
            x, y = poly_recurrence_extremal(d, d + 4)
            self.assertEqual(lcp(x, y), d + 1)
            self.assertEqual(x[:d + 1], y[:d + 1])    # horizon d+1 would be fooled


if __name__ == "__main__":
    unittest.main()
