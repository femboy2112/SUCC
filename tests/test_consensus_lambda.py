"""Independent exact finite controls for SUCC-lambda E consensus and spheres."""
import dataclasses
import itertools
import unittest

from observational_succ.source_lambda import (
    Atlas, Bool, Eq, Forget, Passport, Read, Residue, Select,
    ReportT, Lam, TypeFault, AccessGap, LambdaError,
)
from observational_succ.consensus_lambda import (
    Candidate, ConsensusError, EDevice, EFrame, EObservation, ERelay,
    LambdaPort, MiniPort, World, certify_dual_ports, consensus,
    exact_portfolio, forcing_depth, horned_sphere_consensus_control,
    minimum_consensus_channel,two_chart_cross_energy,
)


P=Passport("consensus-model",7)


def space(n=4):
    return World(P,tuple(Candidate(f"s{i}",i,f"t{i}") for i in range(n)))


def dev(name, ports, *, states=("ready",), initial="ready", moves=None, enabled=None,
        passport=P, non_destructive_source=True):
    return EDevice(name,passport,states,initial,tuple(ports),
                   enabled if enabled is not None else {"ready":tuple(p.name for p in ports)},
                   moves if moves is not None else {},non_destructive_source)


class SourceIndexedConsensusTests(unittest.TestCase):
    def setUp(self):
        self.a=dev("A",(LambdaPort("mod2",Read(2)),))
        self.b=dev("B",(LambdaPort("mod3",Read(3)),))

    def record(self, d, integer, modulus, name):
        return EFrame(d).record(name,atlas=Atlas.from_integer(P,integer,(modulus,)))

    def test_two_partial_observers_jointly_identify_source(self):
        a=self.record(self.a,3,2,"mod2")
        b=self.record(self.b,3,3,"mod3")
        self.assertEqual(consensus(space(),(a,)).compatible,("s1","s3"))
        self.assertEqual(consensus(space(),(b,)).compatible,("s0","s3"))
        result=consensus(space(),(a,b))
        self.assertEqual(result.status,"SOURCE_IDENTIFIED_IN_DECLARED_MODEL")
        self.assertEqual(result.compatible,("s3",))
        self.assertEqual(result.possible_targets,("t3",))
        self.assertFalse(result.establishes_global_truth)
        self.assertFalse(result.physically_authenticated)

    def test_local_positive_consensus_misses_negative_mixed_energy(self):
        from fractions import Fraction
        r=two_chart_cross_energy(1,1,2)
        self.assertTrue(r["both_individual_charts_positive"])
        self.assertFalse(r["whole_joint_operator_positive_semidefinite"])
        self.assertEqual(r["mixed_determinant"],-3)
        self.assertEqual(r["explicit_negative_witness"],(2,-1))
        self.assertEqual(r["witness_energy"],-3)
        self.assertFalse(r["source_is_Suzuki"])
        with self.assertRaises(ConsensusError):
            two_chart_cross_energy(1.0,1,2)
        self.assertTrue(two_chart_cross_energy(Fraction(1,2),2,1)[
            "whole_joint_operator_positive_semidefinite"])

    def test_exact_minimum_two_port_cover(self):
        portfolio=exact_portfolio(space(),(self.a,self.b),radius=0)
        self.assertEqual(portfolio.status,"MODEL_TARGET_SEPARATING_PORTFOLIO")
        self.assertEqual(set(portfolio.selected),{("A","mod2"),("B","mod3")})
        self.assertEqual(portfolio.total_cross_target_pairs,6)
        self.assertFalse(portfolio.executed)

    def test_same_view_unanimity_cannot_identify_hidden_target(self):
        d1=dev("C",(LambdaPort("mod2",Read(2)),))
        d2=dev("D",(LambdaPort("mod2",Read(2)),))
        world=World(P,(Candidate("x",0,"true"),Candidate("y",2,"false")))
        self.assertEqual(forcing_depth(world,(d1,d2),max_radius=0).status,
                         "DARK_UNDER_DECLARED_PORT_FAMILY")
        a=EFrame(d1).record("mod2",atlas=Atlas.from_integer(P,0,(2,)))
        b=EFrame(d2).record("mod2",atlas=Atlas.from_integer(P,2,(2,)))
        result=consensus(world,(a,b))
        self.assertEqual(result.status,"TARGET_UNRESOLVED")
        self.assertEqual(len(result.compatible),2)

    def test_relay_preserves_origin_and_does_not_create_second_read(self):
        obs=self.record(self.a,3,2,"mod2")
        wire=ERelay(obs,"B")
        result=consensus(space(),(obs,wire))
        self.assertEqual(result.report_origins,("A","A"))
        self.assertEqual(result.compatible,("s1","s3"))

    def test_fresh_holdout_portfolio_against_direct_modular_oracle(self):
        # Independent tiny-integer arithmetic checks, not another invocation
        # of SUCC-lambda's AST evaluator or its certificate inspector.
        primes=(2,3,5)
        devices=tuple(dev(f"E{p}",(LambdaPort(f"mod{p}",Read(p)),))
                      for p in primes)
        for horizon in (3,4,7,9):
            world=space(horizon)
            answer=exact_portfolio(world,devices,radius=0)
            self.assertEqual(answer.status,"MODEL_TARGET_SEPARATING_PORTFOLIO")
            picked={int(name[3:]) for _,name in answer.selected}
            def separates(mods):
                return all(any(x%p != y%p for p in mods)
                           for x,y in itertools.combinations(range(horizon),2))
            self.assertTrue(separates(picked))
            self.assertFalse(any(separates(subset)
                for k in range(len(picked))
                for subset in itertools.combinations(primes,k)))

    def test_model_truth_preserved_under_trustworthy_monotone_updates(self):
        world=space(4)
        for true in (0,1,2,3):
            a=self.record(self.a,true,2,"mod2")
            b=self.record(self.b,true,3,"mod3")
            s1=consensus(world,(a,))
            s2=consensus(world,(a,b))
            self.assertIn(f"s{true}",s1.compatible)
            self.assertIn(f"s{true}",s2.compatible)
            self.assertLessEqual(len(s2.compatible),len(s1.compatible))

    def test_wrong_epoch_basis_and_source_rejected(self):
        wrong=Passport("consensus-model",8)
        with self.assertRaises(ConsensusError):
            EFrame(self.a).record("mod2",atlas=Atlas.from_integer(wrong,3,(2,)))
        e=self.record(self.a,3,2,"mod2")
        with self.assertRaises(ConsensusError):
            consensus(World(wrong,(Candidate("x",3,"t"),)),(e,))
        foreign=dev("C",(LambdaPort("mod2",Read(2)),),passport=wrong)
        foreign_observation=EFrame(foreign).record(
            "mod2",atlas=Atlas.from_integer(wrong,3,(2,)))
        with self.assertRaises(ConsensusError):
            consensus(space(),(e,foreign_observation))

    def test_empty_model_is_not_universal_nonexistence(self):
        e1=self.record(self.a,0,2,"mod2")
        e2=self.record(self.b,1,3,"mod3")
        # 0 mod2 and 1 mod3 has solution 4 mod6; finite declared world is 0..3.
        result=consensus(space(),(e1,e2))
        self.assertEqual(result.status,"NO_GLOBAL_SOURCE_IN_DECLARED_MODEL")
        self.assertEqual(result.minimal_inconsistent_indices,(0,1))
        self.assertEqual(result.possible_targets,())
        self.assertFalse(result.establishes_global_truth)

    def test_pairwise_consistent_triple_no_global_gluing(self):
        # For X={0,1,2}, sets {0,2}, {0,1}, {1,2} intersect pairwise
        # but have EMPTY triple intersection. All three claims are individually
        # true observations of *different* possible sources.
        a=dev("A",(LambdaPort("except1",Select(
             Eq(Forget(Read(3)),Residue(3,1)),Bool(False),Bool(True))),))
        b=dev("B",(LambdaPort("except2",Select(
             Eq(Forget(Read(3)),Residue(3,2)),Bool(False),Bool(True))),))
        c=dev("C",(LambdaPort("except0",Select(
             Eq(Forget(Read(3)),Residue(3,0)),Bool(False),Bool(True))),))
        ea=EFrame(a).record("except1",atlas=Atlas.from_integer(P,0,(3,)))
        eb=EFrame(b).record("except2",atlas=Atlas.from_integer(P,0,(3,)))
        ec=EFrame(c).record("except0",atlas=Atlas.from_integer(P,1,(3,)))
        w=space(3)
        self.assertTrue(all(consensus(w,xy).compatible for xy in
                         ((ea,eb),(ea,ec),(eb,ec))))
        result=consensus(w,(ea,eb,ec))
        self.assertEqual(result.status,"NO_GLOBAL_SOURCE_IN_DECLARED_MODEL")
        self.assertEqual(result.minimal_inconsistent_indices,(0,1,2))

    def test_forged_output_and_lineage_rejected(self):
        e=self.record(self.a,3,2,"mod2")
        with self.assertRaises(ConsensusError):
            consensus(space(),(dataclasses.replace(e,output=("report",P,2,0)),))
        with self.assertRaises(ConsensusError):
            consensus(space(),(dataclasses.replace(e,lineage=("external-verified",)),))

    def test_missing_recorded_modulus_remains_access_gap(self):
        with self.assertRaises(AccessGap):
            EFrame(self.a).record("mod2",atlas=Atlas(P,()))
        with self.assertRaises(ConsensusError):
            EFrame(self.a).record("mod2",parent_public_report="0")

    def test_closure_output_cannot_be_consensus_port(self):
        with self.assertRaises(TypeFault):
            dev("bad",(LambdaPort("closure",Lam(ReportT(P,2),Read(2))),))

    def test_distinct_source_ids_same_numeric_address_remain_distinct(self):
        world=World(P,(Candidate("inner-A",1,"yes"),Candidate("inner-B",1,"no")))
        self.assertEqual(consensus(world,(self.record(self.a,1,2,"mod2"),)).status,
                         "TARGET_UNRESOLVED")

    def test_program_budget_does_not_prove_false(self):
        with self.assertRaises(LambdaError):
            dev("broken",(LambdaPort("missing",Read(1)),))

    def test_world_rejects_duplicate_labels_but_allows_hidden_state_aliases(self):
        with self.assertRaises(ConsensusError):
            World(P,(Candidate("x",1,"yes"),Candidate("x",2,"no")))
        World(P,(Candidate("x",1,"yes"),Candidate("y",1,"no")))

    def test_target_constancy_without_full_identity(self):
        world=World(P,(Candidate("x",0,"a"),Candidate("y",2,"a"),
                       Candidate("z",1,"b")))
        result=consensus(world,(self.record(self.a,0,2,"mod2"),))
        self.assertEqual(result.status,"TARGET_CERTIFIED_IN_DECLARED_MODEL")
        self.assertEqual(result.compatible,("x","y"))
        self.assertEqual(result.possible_targets,("a",))

    def test_duplicate_observer_names_rejected_for_portfolio(self):
        with self.assertRaises(ConsensusError):
            exact_portfolio(space(),(self.a,self.a),radius=0)


class EAutomataSphereTests(unittest.TestCase):
    def setUp(self):
        self.a=dev("A",(LambdaPort("mod2",Read(2)),),
                   states=("asleep","awake"),initial="asleep",
                   moves={("asleep","unlock"):"awake"},
                   enabled={"asleep":(),"awake":("mod2",)})
        self.b=dev("B",(LambdaPort("mod3",Read(3)),))

    def test_unlock_is_a_real_finite_action_not_auto_observation(self):
        sphere0=self.a.sphere(0)
        sphere1=self.a.sphere(1)
        self.assertEqual(sphere0.available,())
        self.assertEqual(sphere1.available,(("mod2",("unlock",)),))
        self.assertTrue(sphere1.possible_only)
        with self.assertRaises(AccessGap):
            EFrame(self.a).record("mod2",atlas=Atlas.from_integer(P,3,(2,)))
        actual=EFrame(self.a).succ("unlock")
        self.assertEqual(actual.state,"awake")
        self.assertEqual(actual.path,("unlock",))
        self.assertEqual(actual.record("mod2",atlas=Atlas.from_integer(P,3,(2,))).origin,"A")

    def test_joint_forcing_depth_one(self):
        w=space()
        self.assertEqual(forcing_depth(w,(self.a,self.b),max_radius=0).status,
                         "DEPTH_BUDGET_GAP")
        forced=forcing_depth(w,(self.a,self.b),max_radius=1)
        self.assertEqual(forced.status,"FINITE_FORCING_DEPTH_CERTIFIED")
        self.assertEqual(forced.radius,1)
        self.assertEqual(len(forced.portfolio.selected),2)

    def test_radius_does_not_invent_unavailable_probes(self):
        missing=dev("only1",(LambdaPort("mod2",Read(2)),),
                    states=("a","b"),initial="a",
                    moves={("a","walk"):"b"},
                    enabled={"a":("mod2",),"b":("mod2",)})
        verdict=forcing_depth(space(),(missing,),max_radius=10)
        self.assertEqual(verdict.status,"DARK_UNDER_DECLARED_PORT_FAMILY")
        self.assertIsNone(verdict.radius)

    def test_union_of_incompatible_sphere_branches_is_not_consensus(self):
        e=dev("fork",(LambdaPort("mod2",Read(2)),LambdaPort("mod3",Read(3))),
              states=("root","left","right"),initial="root",
              moves={("root","L"):"left",("root","R"):"right"},
              enabled={"root":(),"left":("mod2",),"right":("mod3",)})
        world=space()
        # The UNION of programs can separate every source pair, but no
        # single lawful final state allows this E to deploy both ports.
        self.assertEqual({name for name,_ in e.sphere(1).available},{"mod2","mod3"})
        self.assertEqual(forcing_depth(world,(e,),max_radius=2).status,
                         "ONE_STATE_PROTOCOL_SATURATED")
        self.assertEqual(exact_portfolio(world,(e,),radius=2).status,
                         "UNJOINTLY_REALIZABLE_PORT_FAMILY")
        left=EFrame(e).succ("L").record(
               "mod2",atlas=Atlas.from_integer(P,3,(2,)))
        right=EFrame(e).succ("R").record(
               "mod3",atlas=Atlas.from_integer(P,3,(3,)))
        with self.assertRaises(ConsensusError):
            consensus(world,(left,right))

    def test_actualized_prefix_paths_can_accumulate_nondestructive_records(self):
        e=dev("walk",(LambdaPort("mod2",Read(2)),LambdaPort("mod3",Read(3))),
              states=("root","middle","end"),initial="root",
              moves={("root","first"):"middle",("middle","second"):"end"},
              enabled={"root":(),"middle":("mod2",),"end":("mod3",)})
        middle=EFrame(e).succ("first")
        later=middle.succ("second")
        a=middle.record("mod2",atlas=Atlas.from_integer(P,3,(2,)))
        b=later.record("mod3",atlas=Atlas.from_integer(P,3,(3,)))
        # Inference accepts actual ordered, nondestructive transcripts;
        # the conservative portfolio planner does not synthesize a schedule.
        self.assertEqual(consensus(space(),(a,b)).compatible,("s3",))
        self.assertEqual(exact_portfolio(space(),(e,),radius=2).status,
                         "UNJOINTLY_REALIZABLE_PORT_FAMILY")

    def test_declared_fabrication_is_not_sensor_approval(self):
        with self.assertRaises(ConsensusError):
            dev("mutating",(LambdaPort("mod2",Read(2)),),non_destructive_source=False)

    def test_worst_case_depth_applies_to_all_target_pairs(self):
        w=World(P,(Candidate("zero",0,"t0"),Candidate("six",6,"t6")))
        self.assertEqual(forcing_depth(w,(self.b,),max_radius=0).status,
                         "DARK_UNDER_DECLARED_PORT_FAMILY")


class ExistingMiniAndWildIntegrationTests(unittest.TestCase):
    def test_source_preserving_matryoshka_miniature_port_and_dual(self):
        try:
            from observational_succ.miniature_carrier import Carrier, Mini
        except ImportError:
            self.skipTest("full SUCC MATRYOSHKA dependency not locally mounted")
        src="consensus-model"
        states=("00","01","10","11")
        a={s:str(1-int(s[0]))+s[1] for s in states}
        b={s:s[0]+str(1-int(s[1])) for s in states}
        parent=Carrier(states,{"a":a,"b":b},{s:s for s in states},("00",),src)
        left=Mini(("0","1"),{"step":{"0":"1","1":"0"}},
                  {"0":"L0","1":"L1"},"0",src)
        right=Mini(("0","1"),{"step":{"0":"1","1":"0"}},
                  {"0":"R0","1":"R1"},"0",src)
        lp=MiniPort("left",parent,left,{s:s[0] for s in states},
                    {"step":("a",)},{s:"L"+s[0] for s in states})
        rp=MiniPort("right",parent,right,{s:s[1] for s in states},
                    {"step":("b",)},{s:"R"+s[1] for s in states})
        self.assertTrue(lp.validate(P)["certified"])
        self.assertTrue(rp.validate(P)["certified"])
        joint=certify_dual_ports(lp,rp,P,("a",),("b",),
                          {s:("L"+s[0],"R"+s[1]) for s in states})
        self.assertTrue(joint["certified_joint_model"])
        world=World(P,tuple(Candidate(s,i,s) for i,s in enumerate(states)))
        la=EFrame(dev("L",(lp,))).record("left",parent_public_report="10")
        ra=EFrame(dev("R",(rp,))).record("right",parent_public_report="10")
        self.assertEqual(len(consensus(world,(la,)).compatible),2)
        self.assertEqual(consensus(world,(la,ra)).compatible,("10",))
        self.assertFalse(joint["two_physical_sensors_proved"])

    def test_exact_receiver_side_zero_error_consensus_compression(self):
        try:
            import observational_succ.interobserver_channels
        except ImportError:
            self.skipTest("full SUCC interobserver channel module not locally mounted")
        world=space(4)
        a=dev("Sender",(LambdaPort("mod3",Read(3)),))
        b=dev("Receiver",(LambdaPort("mod2",Read(2)),))
        result=minimum_consensus_channel(world,a,"mod3",b,"mod2")
        self.assertEqual(result["minimum_codewords"],2)
        self.assertEqual(result["minimum_fixed_width_bits"],1)
        self.assertEqual(result["naive_sender_view_bits"],2)
        self.assertTrue(result["decoder_correct_for_all_declared_sources"])
        self.assertFalse(result["recipient_performed_senders_probe"])

    def test_wrong_source_or_false_mini_report_denied(self):
        try:
            from observational_succ.miniature_carrier import Carrier, Mini
        except ImportError:
            self.skipTest("full SUCC MATRYOSHKA dependency not locally mounted")
        p=Carrier(("0","1"),{"flip":{"0":"1","1":"0"}},
                  {"0":"r0","1":"r1"},("0",),"other")
        m=Mini(("0","1"),{"flip":{"0":"1","1":"0"}},
               {"0":"r0","1":"r1"},"0","other")
        bad=MiniPort("foreign",p,m,{"0":"0","1":"1"},
                     {"flip":("flip",)},{"r0":"r0","r1":"r1"})
        with self.assertRaises(ConsensusError):
            dev("foreign",(bad,))

    def test_individual_factors_do_not_ensure_joint_parent_states(self):
        try:
            from observational_succ.miniature_carrier import Carrier, Mini
        except ImportError:
            self.skipTest("full SUCC MATRYOSHKA dependency not locally mounted")
        states=("00","01","10")
        parent=Carrier(states,{"id":{s:s for s in states}},
                       {s:s for s in states},states,P.source_id)
        l=Mini(("0","1"),{"id":{"0":"0","1":"1"}},
               {"0":"L0","1":"L1"},"0",P.source_id)
        r=Mini(("0","1"),{"id":{"0":"0","1":"1"}},
               {"0":"R0","1":"R1"},"0",P.source_id)
        lp=MiniPort("L",parent,l,{s:s[0] for s in states},
                    {"id":("id",)},{s:"L"+s[0] for s in states})
        rp=MiniPort("R",parent,r,{s:s[1] for s in states},
                    {"id":("id",)},{s:"R"+s[1] for s in states})
        self.assertTrue(lp.validate(P)["certified"])
        self.assertTrue(rp.validate(P)["certified"])
        together=certify_dual_ports(lp,rp,P,("id",),("id",),
                         {s:("L"+s[0],"R"+s[1]) for s in states})
        self.assertFalse(together["certified_joint_model"])
        self.assertEqual(together["status"],"ghost_joint_states")

    def test_horned_sphere_many_abelian_observers_still_blind(self):
        try:
            import observational_succ.wild_embedding_succ
        except ImportError:
            self.skipTest("full SUCC WILD-SUCC dependency not locally mounted")
        r=horned_sphere_consensus_control(3,(1,1,2,3,7))
        self.assertTrue(r["all_observers_blind"])
        self.assertEqual(r["iterated_word_length"],64)
        self.assertEqual(r["lower_central_depth"],8)
        self.assertEqual(r["stage_detector"]["matrix_dimension"],9)
        self.assertTrue(r["no_global_nilpotent_representation_from_stage_detector"])
        r=horned_sphere_consensus_control(3,(1,8))
        self.assertFalse(r["all_observers_blind"])


if __name__ == "__main__":
    unittest.main()
