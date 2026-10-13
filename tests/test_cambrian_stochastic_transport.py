"""Independent fine-source oracles and calibrated weaker-contract mutants."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.causal_nerode_succ import SourceChart, SourceTransportError
from observational_succ.cambrian_stochastic_transport import (
    JointInstrument, joint_descent, source_filter, observer_filter,
    push_reports, filter_history,
)


def chart(epoch, reports):
    return SourceChart("cambrian-source", epoch, "declared-basis",
                       tuple("s" + str(i) for i in range(len(reports))), reports)


class JointStochasticTransportTests(unittest.TestCase):
    def test_exhaustive_rational_joint_laws_against_event_oracle(self):
        rows = [tuple(Q(x, 2) for x in xs)
                for xs in product(range(3), repeat=4) if sum(xs) == 2]
        cases = 0
        for q0, q1 in product((('a', 'a'), ('a', 'b')), repeat=2):
            for a, b in product(rows, repeat=2):
                src = JointInstrument('joint', chart(0, q0), chart(1, q1),
                                      ('z', 'w'), (a, b))
                # Independent dictionary accumulation using source event atoms.
                atom_rows = []
                for row in (a, b):
                    atoms = {}
                    for t, z in product(range(2), range(2)):
                        event = (q1[t], ('z', 'w')[z])
                        atoms[event] = atoms.get(event, Q(0)) + row[2*t+z]
                    atom_rows.append(atoms)
                expected = q0[0] != q0[1] or atom_rows[0] == atom_rows[1]
                cert = joint_descent(src)
                self.assertEqual(cert.descended, expected)
                if expected:
                    for numerator in range(5):
                        prior = (Q(numerator, 4), Q(4-numerator, 4))
                        for z in ('z', 'w'):
                            event_weights = {
                                r: sum((prior[s] * atom_rows[s][(r, z)]
                                        for s in range(2)), Q(0))
                                for r in set(q1)}
                            mass = sum(event_weights.values(), Q(0))
                            coarse = observer_filter(src, push_reports(src.before, prior), z)
                            fine = source_filter(src, prior, z)
                            self.assertEqual(coarse.evidence, mass)
                            self.assertEqual(fine.evidence, mass)
                            expected_post = (tuple(event_weights[r]/mass
                                                   for r in src.after.image()) if mass else None)
                            self.assertEqual(coarse.posterior, expected_post)
                            if mass:
                                self.assertEqual(push_reports(src.after, fine.posterior), expected_post)
                cases += 1
        self.assertEqual(cases, 400)

    def test_same_support_and_same_marginals_do_not_descend_joint_law(self):
        src = JointInstrument('correlation-mutation', chart(0, ('a', 'a')),
                              chart(1, ('x', 'y')), ('z', 'w'),
                              ((Q(3,8),Q(1,8),Q(1,8),Q(3,8)),
                               (Q(1,8),Q(3,8),Q(3,8),Q(1,8))))
        cert = joint_descent(src)
        self.assertFalse(cert.descended)
        self.assertEqual(source_filter(src, (Q(1),Q(0)), 'z').posterior, (Q(3,4),Q(1,4)))
        self.assertEqual(source_filter(src, (Q(0),Q(1)), 'z').posterior, (Q(1,4),Q(3,4)))
        self.assertEqual(len(set(pair for _, pair in cert.repaired_reports)), 2)

    def test_same_normalized_posterior_does_not_preserve_evidence(self):
        src = JointInstrument('likelihood-mutation', chart(0, ('a','a')),
                              chart(1, ('x',)), ('z','w'),
                              ((Q(1,4),Q(3,4)),(Q(3,4),Q(1,4))))
        first = source_filter(src, (Q(1),Q(0)), 'z')
        second = source_filter(src, (Q(0),Q(1)), 'z')
        self.assertEqual(first.posterior, second.posterior)
        self.assertNotEqual(first.evidence, second.evidence)
        self.assertFalse(joint_descent(src).descended)

    def test_arbitrarily_small_joint_error_can_leave_full_conditional_debt(self):
        for denominator in (2, 7, 101, 10007):
            epsilon = Q(1, denominator)
            rows = ((epsilon, 1-epsilon, Q(0), Q(0)),
                    (Q(0), 1-epsilon, epsilon, Q(0)))
            src = JointInstrument('rare-receipt', chart(0,('a','a')),
                                  chart(1,('x','y')), ('rare','common'), rows)
            joint_tv = sum(abs(x-y) for x,y in zip(*rows))/2
            a = source_filter(src,(Q(1),Q(0)),'rare')
            b = source_filter(src,(Q(0),Q(1)),'rare')
            conditioned_tv = sum(abs(x-y) for x,y in zip(a.posterior,b.posterior))/2
            self.assertEqual(joint_tv, epsilon)
            self.assertEqual(conditioned_tv, 1)
            self.assertEqual(conditioned_tv, joint_tv/min(a.evidence,b.evidence))
        for alpha, beta in ((Q(1,3),Q(2,3)),(Q(1,19),Q(17,19))):
            rows = ((alpha, 1-alpha, Q(0), Q(0)),
                    (alpha, 1-beta, beta-alpha, Q(0)))
            src = JointInstrument('unequal-masses',chart(0,('a','a')),
                                  chart(1,('x','y')),('rare','common'),rows)
            a=source_filter(src,(Q(1),Q(0)),'rare')
            b=source_filter(src,(Q(0),Q(1)),'rare')
            joint_tv=sum(abs(x-y) for x,y in zip(*rows))/2
            conditioned_tv=sum(abs(x-y) for x,y in zip(a.posterior,b.posterior))/2
            self.assertEqual(conditioned_tv,joint_tv/max(a.evidence,b.evidence))

    def test_source_changing_histories_against_direct_path_enumeration(self):
        # Different hidden rows aggregate to one lawful report/receipt row.
        reports = ('a','a','b')
        rows = ((Q(1,8),Q(1,8),Q(1,8),Q(1,8),Q(1,4),Q(1,4)),
                (Q(1,4),Q(0),Q(0),Q(1,4),Q(1,4),Q(1,4)),
                (Q(1,8),Q(1,8),Q(1,8),Q(1,8),Q(1,2),Q(0)))
        instruments = tuple(JointInstrument('step-'+str(t), chart(t,reports),
                                            chart(t+1,reports), ('z','w'), rows)
                            for t in range(4))
        prior = (Q(1,3),Q(1,6),Q(1,2))
        for receipts in product(('z','w'), repeat=4):
            fine_mass = {i:p for i,p in enumerate(prior)}
            for receipt in receipts:
                zi = ('z','w').index(receipt)
                fine_mass = {j:sum((p*rows[i][2*j+zi]
                                     for i,p in fine_mass.items()), Q(0))
                             for j in range(3)}
            evidence = sum(fine_mass.values(), Q(0))
            oracle = tuple(sum((p for i,p in fine_mass.items() if reports[i]==r),Q(0))/evidence
                           for r in ('a','b'))
            result = filter_history(instruments, prior, receipts)
            self.assertEqual(result['likelihood'], evidence)
            self.assertEqual(result['posterior'], oracle)

    def test_impossible_receipt_is_not_an_arbitrary_posterior(self):
        src = JointInstrument('null',chart(0,('a',)),chart(1,('a',)),
                              ('z','w'),((Q(1),Q(0)),))
        r = filter_history((src,), (Q(1),), ('w',))
        self.assertFalse(r['possible'])
        self.assertEqual(r['likelihood'], 0)
        self.assertIsNone(r['posterior'])

    def test_partial_source_and_stale_history_are_rejected(self):
        src = JointInstrument('partial',chart(0,('a',)),chart(1,('a',)),
                              ('z',),((Q(1),),),False)
        self.assertTrue(joint_descent(src).descended)
        self.assertFalse(joint_descent(src).source_class_certified)
        with self.assertRaises(SourceTransportError):
            observer_filter(src,(Q(1),),'z')
        first = JointInstrument('first',chart(0,('a',)),chart(1,('a',)),
                                ('z',),((Q(1),),))
        with self.assertRaises(SourceTransportError):
            filter_history((first,first),(Q(1),),('z','z'))

    def test_float_unnormalized_negative_and_cross_source_laws_rejected(self):
        for row in ((1.0,), (Q(2),), (Q(-1),)):
            with self.assertRaises(SourceTransportError):
                JointInstrument('bad',chart(0,('a',)),chart(1,('a',)),('z',),(row,))
        alien = SourceChart('different-source',1,'declared-basis',('s0',),('a',))
        with self.assertRaises(SourceTransportError):
            JointInstrument('bad',chart(0,('a',)),alien,('z',),((Q(1),),))
