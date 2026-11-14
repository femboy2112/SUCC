"""Exact finite tests for observer-relative choice, equivariance and history."""
from fractions import Fraction
from itertools import combinations, product
import unittest


def joint_report(x, probes):
    return tuple(p(x) for p in probes)


def indistinguishable_pairs(states, probes):
    return tuple((x, y) for x, y in combinations(states, 2)
                 if joint_report(x, probes) == joint_report(y, probes))


def minimal_separating_subfamily(states, probes):
    for k in range(len(probes) + 1):
        for indices in combinations(range(len(probes)), k):
            family = tuple(probes[i] for i in indices)
            if not indistinguishable_pairs(states, family):
                return indices
    return None


def support_fibers(states, report):
    values = sorted({report(x) for x in states})
    return {v: tuple(x for x in states if report(x) == v) for v in values}


def posterior(prior, report, observed):
    numer = {x: p for x, p in prior.items() if report(x) == observed}
    denom = sum(numer.values(), Fraction(0))
    if denom == 0:
        raise ValueError('observed report has zero prior mass')
    return {x: p / denom for x, p in numer.items()}


def uniform_kernel(fibers):
    return {y: {x: Fraction(1, len(xs)) for x in xs} for y, xs in fibers.items()}


def check_section(fibers, section):
    return all(section[y] in xs for y, xs in fibers.items())


def check_stochastic_section(fibers, kernel):
    return all(sum(kernel[y].values(), Fraction(0)) == 1
                   and set(kernel[y]).issubset(set(xs))
                   and all(w >= 0 for w in kernel[y].values())
               for y, xs in fibers.items())


def has_equivariant_section(fibers, group_actions):
    """All choices enumerated exactly, not just one candidate."""
    ys = tuple(fibers)
    for chosen in product(*(fibers[y] for y in ys)):
        section = dict(zip(ys, chosen))
        if all(action(section[y]) == section[y] for action in group_actions for y in ys):
            return True
    return False


def has_single_copy_policy_for_target(states, target, instruments):
    """Exact finite reachability game on beliefs (original, current).

    A policy wins only if all outcome branches terminate in a belief whose
    ORIGINAL target is known. Least fixed point avoids false cyclic wins.
    """
    initial = frozenset((x, x) for x in states)
    reachable = {initial}
    successors = {}
    todo = [initial]
    while todo:
        belief = todo.pop()
        all_actions = []
        for read, nxt in instruments:
            parts = {}
            for original, current in belief:
                parts.setdefault(read(current), set()).add((original, nxt(current)))
            outcomes = tuple(frozenset(piece) for piece in parts.values())
            all_actions.append(outcomes)
            for next_belief in outcomes:
                if next_belief not in reachable:
                    reachable.add(next_belief)
                    todo.append(next_belief)
        successors[belief] = all_actions
    winning = {belief for belief in reachable if len({target(orig) for orig, _ in belief}) == 1}
    while True:
        add = {belief for belief in reachable - winning
               if any(all(next_belief in winning for next_belief in action)
                      for action in successors[belief])}
        if not add:
            return initial in winning
        winning |= add


class ChoiceProbeTests(unittest.TestCase):
    def test_two_bit_probes_separate_only_jointly(self):
        X = tuple(range(4))
        first = lambda x: x // 2
        second = lambda x: x % 2
        self.assertEqual(minimal_separating_subfamily(X, (first, second)), (0, 1))
        self.assertEqual(len(indistinguishable_pairs(X, (first,))), 2)
        self.assertEqual(len(indistinguishable_pairs(X, (second,))), 2)
        self.assertEqual(len(indistinguishable_pairs(X, (first, second))), 0)

    def test_no_probe_does_not_prevent_ordinary_set_choice(self):
        fibers = support_fibers(('a', 'b'), lambda _: 'one')
        self.assertTrue(check_section(fibers, {'one': 'a'}))
        self.assertTrue(check_section(fibers, {'one': 'b'}))
        self.assertEqual(indistinguishable_pairs(('a', 'b'), (lambda _: 0,)), (('a', 'b'),))

    def test_swap_action_blocks_equivariant_point_selector(self):
        fibers = {'orbit': ('a', 'b')}
        swap = lambda x: {'a': 'b', 'b': 'a'}[x]
        self.assertFalse(has_equivariant_section(fibers, (lambda x:x, swap)))
        self.assertTrue(check_section(fibers, {'orbit': 'a'}))
        self.assertNotEqual(swap('a'), 'a')

    def test_uniform_stochastic_section_respects_swap(self):
        fibers = {'orbit': ('a', 'b')}
        K = uniform_kernel(fibers)
        self.assertTrue(check_stochastic_section(fibers, K))
        self.assertEqual(K['orbit'], {'a': Fraction(1,2), 'b': Fraction(1,2)})
        self.assertEqual(K['orbit']['a'], K['orbit']['b'])

    def test_asymmetric_prior_no_informative_probe(self):
        r = lambda _: 0
        p = posterior({'a': Fraction(1,4), 'b': Fraction(3,4)}, r, 0)
        self.assertEqual(p, {'a': Fraction(1,4), 'b': Fraction(3,4)})
        u = posterior({'a': Fraction(1,2), 'b': Fraction(1,2)}, r, 0)
        self.assertNotEqual(p, u)

    def test_current_identity_probe_cannot_recover_merged_history(self):
        histories = ('a_then_c', 'b_then_c')
        now = lambda _: 'c'
        self.assertEqual(indistinguishable_pairs(histories, (now, now)),
                         (('a_then_c', 'b_then_c'),))
        self.assertEqual(posterior({histories[0]: Fraction(2,3),
                                    histories[1]: Fraction(1,3)}, now, 'c'),
                         {histories[0]: Fraction(2,3), histories[1]: Fraction(1,3)})

    def test_destructive_counterexample_single_copy(self):
        X = ('A', 'B', 'C')
        a = (lambda x: 1 if x == 'A' else 0, lambda x:'A')
        b = (lambda x: 1 if x == 'B' else 0, lambda x:'A')
        self.assertFalse(has_single_copy_policy_for_target(X, lambda x:x=='C', (a,b)))
        self.assertEqual(minimal_separating_subfamily(X,(a[0],b[0])), (0,1))

    def test_nondisturbing_repairs_single_copy(self):
        X = ('A', 'B', 'C')
        a = (lambda x: 1 if x == 'A' else 0, lambda x:x)
        b = (lambda x: 1 if x == 'B' else 0, lambda x:x)
        self.assertTrue(has_single_copy_policy_for_target(X, lambda x:x=='C', (a,b)))

    def test_nontrivial_action_without_an_observer_probe(self):
        X=('a','b')
        swap=lambda x: {'a':'b','b':'a'}[x]
        self.assertEqual(swap(swap('a')), 'a')
        self.assertEqual(indistinguishable_pairs(X, (lambda _:0,)), (('a','b'),))

    def test_noninvariant_source_distribution_is_not_forced_uniform(self):
        X=('a','b')
        p=posterior({'a':Fraction(1,10),'b':Fraction(9,10)}, lambda _:1, 1)
        self.assertEqual(p['a'],Fraction(1,10))
        self.assertNotEqual(p['a'],Fraction(1,2))


if __name__=='__main__':
    unittest.main(verbosity=2)
