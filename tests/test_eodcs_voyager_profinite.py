"""Independent Voyager source, finite-horizon debt and completion crucible."""
import unittest
from fractions import Fraction as Q
from itertools import product
from random import Random

from observational_succ.voyager_profinite_frontier import (
    VoyagerError,TraceSource,eventual_zero_lift,all_one,powers_of_two_pulse,
    power_two_period_refutation,incompatible_pulse_with_finite_machine,
    finite_model_critical_probe_witnesses,finite_trace_projective_tower,
    ideal_eventual_zero_stage,truncated_ultrametric,
    power_two_gap_memory_lower_bound,voyager_demo,
)


def brute_source_run(machine,steps,start=None):
    """An unrelated direct index recurrence; never call TraceSource.trace."""
    states=machine.states
    succ=dict(zip(states,machine.successor))
    outputs=dict(zip(states,machine.output))
    state=machine.initial if start is None else start
    ans=[]
    for _ in range(steps):
        ans.append(outputs[state])
        state=succ[state]
    return tuple(ans)


class TestVoyagerFiniteSource(unittest.TestCase):
    def test_both_exact_stream_sources_and_scope(self):
        for h in range(0,30):
            s=eventual_zero_lift(tuple([1]*h))
            self.assertEqual(s.trace(h),tuple([1]*h))
            self.assertEqual(s.trace(h+7)[h:],(0,)*7)
            self.assertEqual(s.eventual_period(),(h,1))
            self.assertFalse(s.source_authenticated)
        # Critical counter-control: the all-true stream IS produced by
        # a legitimate ONE-state finite automaton, but is NOT eventually
        # zero. Do not conflate the source classes.
        ones=TraceSource("all-one-machine",0,"binary",("q",),(1,),("q",),"q")
        self.assertEqual(ones.trace(100), (1,)*100)
        self.assertEqual(ones.eventual_period(),(0,1))

    def test_complete_finite_source_nested_stage_projection_is_surjective(self):
        rng=Random(62204)
        for case in range(125):
            n=rng.randrange(1,10)
            states=tuple("s"+str(i) for i in range(n))
            output=tuple(rng.randrange(2) for _ in states)
            successor=tuple(rng.choice(states) for _ in states)
            m=TraceSource("finite-"+str(case),7,"binary",states,output,
                          successor,states[0])
            tower=finite_trace_projective_tower(m,13)
            sizes=tower["stage_sizes"]
            self.assertEqual(sizes[0],1)
            self.assertEqual(len(sizes),14)
            self.assertTrue(tower["projection_surjective"])
            self.assertTrue(all(a<=b<=n for a,b in zip(sizes,sizes[1:])))
            self.assertEqual(set(brute_source_run(m,6,start=s) for s in states),
                             set(m.trace(6,start=s) for s in states))

    def test_unbounded_eventual_zero_family_all_finite_stage_prefixes(self):
        for h in range(0,11):
            words=ideal_eventual_zero_stage(h)
            self.assertEqual(len(words),2**h)
            self.assertTrue(all(eventual_zero_lift(w).trace(h)==w for w in words))
            if h>0:
                all_below=ideal_eventual_zero_stage(h-1)
                self.assertEqual(set(w[:-1] for w in words),set(all_below))

    def test_target_powers_two_pulse_never_has_an_eventual_period(self):
        rng=Random(28)
        inputs=[(0,1),(0,2),(10,3),(100,17),
                (2**17,2**16)]
        inputs.extend((rng.randrange(0,50000),rng.randrange(1,900))
                      for _ in range(250))
        for n,p in inputs:
            cert=power_two_period_refutation(n,p)
            a,b=cert["witness_time"],cert["shifted_time"]
            self.assertGreaterEqual(a,n)
            self.assertEqual(a&(a-1),0)
            self.assertTrue(a>a-1>=0)
            self.assertTrue(a<b<2*a)
            self.assertLessEqual(b-a,p)
            self.assertEqual((powers_of_two_pulse(a),
                              powers_of_two_pulse(b)),(1,0))
            self.assertTrue(cert["periodicity_refuted"])

    def test_finite_machine_eventual_period_versus_raw_state_oracle(self):
        rng=Random(319)
        for trial in range(170):
            n=rng.randrange(1,10)
            states=tuple(str(i) for i in range(n))
            trans=tuple(rng.choice(states) for _ in states)
            obs=tuple(rng.randrange(2) for _ in states)
            m=TraceSource("seed"+str(trial),0,"binary",states,obs,trans,
                          states[0])
            for initial in states:
                mu,p=m.eventual_period(start=initial)
                self.assertTrue(0<=mu<n and 1<=p<=n)
                self.assertLessEqual(mu+p,n)
                path=[]
                at=initial
                for _ in range(n+5):
                    path.append(at)
                    at=trans[states.index(at)]
                self.assertEqual(path[mu],path[mu+p])
                self.assertEqual(path[mu:mu+p],
                                 list(dict.fromkeys(path[mu:mu+p])))
                trace=brute_source_run(m,mu+5*p+3,start=initial)
                self.assertTrue(all(trace[t]==trace[t+p]
                                    for t in range(mu,mu+4*p+2)))

    def test_each_arbitrary_finite_source_state_has_a_finite_pulse_falsifier(self):
        rng=Random(771)
        for trial in range(85):
            n=rng.randrange(1,10)
            states=tuple("x"+str(i) for i in range(n))
            m=TraceSource("finite"+str(trial),0,"binary",states,
                          tuple(rng.randrange(2) for _ in states),
                          tuple(rng.choice(states) for _ in states),
                          states[0])
            cert=finite_model_critical_probe_witnesses(m,powers_of_two_pulse)
            self.assertEqual(cert["refuting_probe_count"],n)
            self.assertTrue(cert["exact_source_trace_oracle"])
            self.assertEqual({s for s,t in cert["probe_times"]},set(states))
            # Independently reconstruct output without using the method
            # that selected the witness.
            for s,t in cert["probe_times"]:
                actual=brute_source_run(m,t+1,start=s)[t]
                self.assertNotEqual(actual,powers_of_two_pulse(t))

    def test_pulse_gap_memory_lower_bound_grows_with_observation_horizon(self):
        for k in range(1,8):
            p=2**k
            horizon=2*p+1
            prefix=tuple(powers_of_two_pulse(i) for i in range(horizon))
            source=eventual_zero_lift(prefix)
            cert=power_two_gap_memory_lower_bound(source,k)
            self.assertEqual(cert["source_horizon"],horizon)
            self.assertEqual(cert["pulse_gap"],p)
            self.assertEqual(cert["certified_minimum_states"],p)
            self.assertTrue(cert["all_gap_states_pairwise_distinct"])
            actual_states=tuple(source.trace_state(t) for t in
                                range(p+1,2*p+1))
            self.assertEqual(len(set(actual_states)),p)
            self.assertGreaterEqual(len(source.states),p)

    def test_memory_debt_does_not_apply_when_mutated_source_lacks_pulse(self):
        p=8
        bits=tuple(powers_of_two_pulse(i) for i in range(2*p+1))
        bad=list(bits);bad[p+3]=1
        source=eventual_zero_lift(tuple(bad))
        with self.assertRaises(VoyagerError):
            power_two_gap_memory_lower_bound(source,3)

    def test_truncated_cantor_ultrametric_triangle_and_prefix_resolution(self):
        words=tuple(product((0,1),repeat=5))
        d=truncated_ultrametric
        for a in words:
            self.assertEqual(d(a,a),0)
            for b in words:
                self.assertEqual(d(a,b),d(b,a))
                self.assertEqual(d(a,b)==0,a==b)
                for c in words:
                    self.assertLessEqual(d(a,c),max(d(a,b),d(b,c)))
        self.assertEqual(d((0,0,0,0,0),(0,0,0,0,1)),Q(1,16))
        self.assertEqual(d((0,0,0,0,0),(1,0,0,0,0)),Q(1))

    def test_source_provenance_and_resource_invalid_mutations(self):
        with self.assertRaises(VoyagerError):
            eventual_zero_lift((0,False,1))
        with self.assertRaises(VoyagerError):
            eventual_zero_lift((1,),source_id="")
        with self.assertRaises(VoyagerError):
            ideal_eventual_zero_stage(14)
        with self.assertRaises(VoyagerError):
            power_two_period_refutation(0,0)
        with self.assertRaises(VoyagerError):
            truncated_ultrametric((1,0),(1,))
        with self.assertRaises(VoyagerError):
            all_one(-1)
        with self.assertRaises(VoyagerError):
            powers_of_two_pulse(-3)
        with self.assertRaises(VoyagerError):
            TraceSource("s",0,"b",("a",), (0,),("missing",),"a")
        with self.assertRaises(VoyagerError):
            TraceSource("s",0,"b",("a",), (0,),("a",),"a",
                        source_authenticated=True)

    def test_exact_reproducible_voyager_science_receipt(self):
        r=voyager_demo()
        self.assertEqual(r["status"],
                         "EXACT_VOYAGER_OBSERVATIONAL_COMPLETION_BOUNDARY")
        self.assertTrue(r["actual_sampled_source_matches_prefix"])
        self.assertEqual(r["power_two_finite_horizon_debt"]["state_lower_bound"],8)
        self.assertEqual(r["power_two_finite_horizon_debt"]["source_horizon"],17)
        self.assertFalse(r["eventual_zero_family"][
            "all_one_global_profile_realized_by_eventually_zero_source"])
        self.assertFalse(r["scope"]["every_profinite_thread_is_original_state"])
        self.assertFalse(r["scope"]["arithmetic_RH_or_Weil_positivity_proved"])


if __name__=="__main__":
    unittest.main()
