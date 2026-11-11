"""Hostile semantics tests with a separate named-variable lambda oracle.

These tests refute specific false behavior; no finite test certifies a full
C-monoid, the general lambda calculus, or infinite cofinality.
"""
from fractions import Fraction
import unittest

from observational_succ import c_monoid_succ_embedding as cm
from observational_succ import omega_trace_interpreter as om
from observational_succ import scott_cofinal_schedule as sc


def nv(name):
    return ('v', name)


def na(name, body):
    return ('l', name, body)


def np(fun, arg):
    return ('a', fun, arg)


def free_names(t):
    if t[0] == 'v':
        return {t[1]}
    if t[0] == 'l':
        return free_names(t[2]) - {t[1]}
    return free_names(t[1]) | free_names(t[2])


def named_substitute(t, name, value):
    """Independent named-variable substitution using explicit alpha-renaming."""
    if t[0] == 'v':
        return value if t[1] == name else t
    if t[0] == 'a':
        return np(named_substitute(t[1], name, value),
                  named_substitute(t[2], name, value))
    binder, body = t[1:]
    if binder == name:
        return t
    if binder in free_names(value):
        forbidden = free_names(body) | free_names(value) | {name, binder}
        fresh = 'fresh'
        while fresh in forbidden:
            fresh += '_'
        body = named_substitute(body, binder, nv(fresh))
        binder = fresh
    return na(binder, named_substitute(body, name, value))


def debruijn(t, context=()):
    if t[0] == 'v':
        return cm.V(context.index(t[1])) if t[1] in context else cm.CONST(t[1])
    if t[0] == 'l':
        return cm.ABS(debruijn(t[2], (t[1],)+context))
    return cm.APP(debruijn(t[1], context), debruijn(t[2], context))


def ast_beta_paths(t, prefix=()):
    """Enumerate actual beta redexes in a generic tree, not a chain formula."""
    found = []
    if t.tag == 'APP':
        if t.f.tag == 'ABS':
            found.append(prefix)
        found.extend(ast_beta_paths(t.f, prefix+('f',)))
        found.extend(ast_beta_paths(t.a, prefix+('a',)))
    elif t.tag == 'ABS':
        found.extend(ast_beta_paths(t.body, prefix+('body',)))
    return tuple(found)


def ast_contract_at(t, address):
    if not address:
        result = cm.beta_redex(t)
        if result is None:
            raise ValueError('address is not a beta redex')
        return result
    if address[0] == 'f':
        return cm.APP(ast_contract_at(t.f, address[1:]), t.a)
    if address[0] == 'a':
        return cm.APP(t.f, ast_contract_at(t.a, address[1:]))
    if address[0] == 'body':
        return cm.ABS(ast_contract_at(t.body, address[1:]))
    raise ValueError(address)


class CaptureAvoidanceTests(unittest.TestCase):
    def test_reported_capture_counterexample(self):
        # lambda z. ((lambda x. lambda y. x) z) = lambda z y. z
        term = cm.ABS(cm.APP(cm.ABS(cm.ABS(cm.V(1))), cm.V(0)))
        self.assertEqual(cm.norm(term), cm.ABS(cm.ABS(cm.V(1))))
        self.assertNotEqual(cm.norm(term), cm.ABS(cm.ABS(cm.V(0))))

    def test_binder_removal_shifts_outer_variable(self):
        # lambda z. ((lambda x. z) a) = lambda z. z
        term = cm.ABS(cm.APP(cm.ABS(cm.V(1)), cm.CONST('a')))
        self.assertEqual(cm.norm(term), cm.ID)

    def test_free_variable_remains_free_under_new_lambda(self):
        self.assertEqual(cm.beta_redex(cm.APP(cm.ABS(cm.ABS(cm.V(1))), cm.V(0))),
                         cm.ABS(cm.V(1)))

    def test_named_oracle_with_binders_shadowing_arguments(self):
        values = [nv('z'), nv('y'), na('y', nv('z')),
                  np(nv('z'), nv('y')), na('w', np(nv('y'), nv('w')))]
        bodies = [nv('x'), nv('z'), na('y', nv('x')),
                  na('z', np(nv('x'), nv('z'))),
                  na('y', na('z', np(nv('x'), nv('y')))),
                  na('x', nv('x')), np(nv('x'), na('z', nv('x')))]
        for depth in range(4):
            for body in bodies:
                for value in values:
                    with self.subTest(depth=depth, body=body, value=value):
                        context = tuple(f'outer{i}' for i in range(depth)) + ('z','y')
                        # Both sides are converted only after the independent
                        # named substitution has completed on the oracle side.
                        actual = cm.beta_redex(debruijn(np(na('x',body),value),context))
                        expected = debruijn(named_substitute(body,'x',value),context)
                        self.assertEqual(actual, expected)

    def test_normal_order_discards_divergent_argument(self):
        self_apply = cm.ABS(cm.APP(cm.V(0), cm.V(0)))
        omega = cm.APP(self_apply, self_apply)
        term = cm.APP(cm.ABS(cm.CONST('answer')), omega)
        self.assertEqual(cm.norm(term, limit=1), cm.CONST('answer'))

    def test_one_global_budget_counts_nested_contractions(self):
        a, b = cm.CONST('a'), cm.CONST('b')
        term = cm.PAIR(cm.APP(cm.ID,a), cm.APP(cm.ID,b))
        with self.assertRaises(RuntimeError):
            cm.norm(term, limit=1)
        self.assertEqual(cm.norm(term, limit=2), cm.PAIR(a,b))

    def test_omega_exhaustion_is_not_a_normal_form(self):
        w = cm.ABS(cm.APP(cm.V(0), cm.V(0)))
        with self.assertRaises(RuntimeError):
            cm.norm(cm.APP(w,w), limit=10)

    def test_eta_guard_preserves_bound_dependency(self):
        term = cm.ABS(cm.APP(cm.V(0),cm.V(0)))
        self.assertEqual(cm.norm(term),term)
        self.assertEqual(cm.norm(cm.ABS(cm.APP(cm.V(1),cm.V(0)))),cm.V(0))


class GenuineArithmeticActionsTests(unittest.TestCase):
    def test_source_state_rejects_inexact_or_invalid_carriers(self):
        for n in (-1, True, False, 0.0, '0'):
            with self.subTest(n=n), self.assertRaises(ValueError):
                cm.SuccState(n, Fraction(0))
        for u in (0.1, 0.0, True, '1/2', None):
            with self.subTest(u=u), self.assertRaises(TypeError):
                cm.SuccState(0, u)
        self.assertIs(type(cm.SuccState(0, 1).u), Fraction)
        self.assertEqual(cm.SuccState(2, Fraction(3,7)).u, Fraction(3,7))
        with self.assertRaises(TypeError):
            cm.succ_step((0,0))
        with self.assertRaises(TypeError):
            cm.iterate_bbp_steps((0,0),0)

    def test_forcing_rejects_nonpositive_and_noninteger_indices(self):
        for n in (0, -1, True, False, 1.0, '1'):
            with self.subTest(n=n), self.assertRaises(ValueError):
                cm.forcing(n)
        self.assertEqual(cm.forcing(1),Fraction(47,15))

    def test_church_successor_and_dilation(self):
        for p in (1,2,3,5,7):
            for n in range(6):
                with self.subTest(p=p,n=n):
                    numeral = cm.church_numeral(n)
                    self.assertTrue(cm.eq(cm.APP(cm.CHURCH_SUCC,numeral),
                                          cm.church_numeral(n+1)))
                    self.assertTrue(cm.eq(cm.APP(cm.church_dilation(p),numeral),
                                          cm.church_numeral(p*n)))
                    self.assertTrue(cm.verify_affine_relation(p,n))

    def test_wrong_commuting_law_fails(self):
        for p in (2,3,5):
            n=4
            self.assertNotEqual(cm.dilation_Vp(cm.arithmetic_successor(n),p),
                                cm.arithmetic_successor(cm.dilation_Vp(n,p)))

    def test_bbp_iteration_is_separately_named(self):
        s=cm.SuccState(0,Fraction(0))
        self.assertEqual(cm.iterate_bbp_steps(s,2),cm.succ_step(cm.succ_step(s)))
        with self.assertRaises(ValueError):
            cm.dilation_Vp(s,3)

    def test_nontrivial_pair_retract(self):
        e=cm.pair(cm.PROJ1,cm.PROJ1)
        self.assertTrue(cm.idempotent_retract(e))
        self.assertFalse(cm.idempotent_retract(cm.PROJ1))


class ActualOmegaAddressTests(unittest.TestCase):
    def test_generic_ast_counts_and_contractions(self):
        for k in range(2,9):
            for m in range(1,10):
                with self.subTest(k=k,m=m):
                    chain=om.Term(k,m)
                    self.assertEqual(ast_beta_paths(chain.syntax()),chain.redex_addresses())
                    if m>=2:
                        step=om.contract_leftmost(chain)
                        self.assertEqual(ast_contract_at(chain.syntax(),step.address),
                                         step.after.syntax())

    def test_outer_application_is_not_a_redex(self):
        chain=om.Term(4,3)
        self.assertEqual(chain.redex_addresses(),(('f',),))
        self.assertIsNone(cm.beta_redex(chain.syntax()))
        with self.assertRaises(ValueError):
            ast_contract_at(chain.syntax(),())


class CofinalityTruthStateTests(unittest.TestCase):
    def test_finite_prefix_never_certifies_infinity(self):
        for ns,Ls in [([0]*4,[0]*4),([1,2,3],[1,2,3]),([5,1],[0,8]),([],[])]:
            with self.subTest(ns=ns,Ls=Ls):
                self.assertIsNone(sc.prefix_diagnostics(ns,Ls)['cofinal'])
                with self.assertRaises(TypeError):
                    sc.is_cofinal_schedule(ns,Ls)

    def test_affine_witness_reaches_every_tested_target_minimally(self):
        for schedule in [sc.SEAM_SCHEDULE,sc.AffineSchedule(2,3,1,5),
                         sc.AffineSchedule(0,11,7,2)]:
            self.assertTrue(sc.is_cofinal_schedule(schedule))
            for n,L in [(0,0),(1,1),(7,19),(100,10000),(10**30,10**31)]:
                k=schedule.dominates_after(n,L)
                a,b=schedule.at(k)
                self.assertGreaterEqual(a,n)
                self.assertGreaterEqual(b,L)
                if k:
                    a,b=schedule.at(k-1)
                    self.assertTrue(a<n or b<L)

    def test_bounded_generator_cannot_reach_arbitrary_target(self):
        s=sc.FROZEN_HORIZON_SCHEDULE
        self.assertFalse(sc.is_cofinal_schedule(s))
        with self.assertRaises(ValueError):
            s.dominates_after(1,3)

    def test_unbounded_projections_do_not_imply_cofinal_image(self):
        # Infinite formula s(2k)=(k,0), s(2k+1)=(0,k): both projections
        # contain every natural, while no member dominates (1,1).
        for k in range(100):
            for pair in [(k,0),(0,k)]:
                self.assertFalse(pair[0]>=1 and pair[1]>=1)
        # These finite cases illustrate the algebraic counterexample; the
        # proof is that one coordinate is identically zero at every index.


if __name__=='__main__':
    unittest.main()
