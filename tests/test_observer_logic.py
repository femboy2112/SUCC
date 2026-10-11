"""Structural soundness tests for finite Gödel syntax and proof checking.

This is not a mechanized PA or Gödel incompleteness proof. It verifies
the actual computable ingredients: injective coding, capture-avoiding
substitution, syntactic diagonal fixed-point, finite proof validity,
and a fail-closed boundary against unauthorized omega/reflection rules.
"""
import unittest

from observational_succ.observer_logic import (
    LogicBoundaryError, Term, Formula, Var, Num, Zero, Succ, Add,
    Multiply, Eq, Pred, Falsum, Not, And, Implies, Forall, Exists,
    term_variables, all_variable_names, free_variables,
    substitute_term, substitute_formula,
    godel_code, decode_godel, diagonal_syntax, diagonalize_formula_code,
    Theory, ProofStep, FiniteProof, check_finite_proof,
    encode_proof, decode_proof, verifies_proof_code,
)


class ObserverSyntaxTests(unittest.TestCase):
    def test_real_first_order_syntax_is_validated_and_immutable(self):
        z=Zero()
        x=Var("x")
        t=Add(Succ(x),Multiply(Num(2),z))
        f=Forall("x",Eq(t,t))
        self.assertEqual(term_variables(t),frozenset({"x"}))
        self.assertEqual(free_variables(f),frozenset())
        self.assertEqual(all_variable_names(f),frozenset({"x"}))
        for bad in (
            lambda:Term("unknown",()),
            lambda:Term("var",("0bad",)),
            lambda:Term("numeral",("00",)),
            lambda:Formula("predicate",("X",("not a term",))),
            lambda:Pred("wrong-name!",Num(1)),
            lambda:Num(-1),
            lambda:Var(""),
            lambda:Eq(x,"x"),
        ):
            with self.assertRaises(LogicBoundaryError):
                bad()
        with self.assertRaises(Exception):
            x.kind="spoofed"

    def test_godel_code_is_reversible_and_injective(self):
        cases=[
            Zero(),Var("x"),Num(0),Num(10),Succ(Num(0)),
            Add(Var("x"),Num(3)),
            Pred("P",Num(0)),Pred("P",Num(1)),Not(Pred("P",Num(1))),
            Forall("x",Pred("P",Var("x"))),
            Exists("x",Pred("P",Var("x"))),
            Implies(Pred("P",Num(0)),Pred("Q",Num(1))),
            Falsum(),
        ]
        encoded=[godel_code(z) for z in cases]
        self.assertEqual(len(encoded),len(set(encoded)))
        for obj,n in zip(cases,encoded):
            self.assertEqual(decode_godel(n),obj)
            self.assertEqual(godel_code(decode_godel(n)),n)
        for bad in (0,-1,1,256,12345,True,1.0):
            with self.assertRaises(LogicBoundaryError):
                decode_godel(bad)
        with self.assertRaises(LogicBoundaryError):
            godel_code("a formula typed as a string")

    def test_substitution_is_capture_avoiding(self):
        formula=Forall("y",Pred("Rel",Var("x"),Var("y")))
        change=substitute_formula(formula,"x",Var("y"))
        self.assertEqual(change.kind,"forall")
        self.assertNotEqual(change.args[0],"y")
        self.assertEqual(free_variables(change),frozenset({"y"}))
        self.assertEqual(change.args[1],
                         Pred("Rel",Var("y"),Var(change.args[0])))
        inner=Forall("y",And(Pred("R",Var("x"),Var("y")),
                              Exists("y",Pred("R",Var("x"),Var("y")))))
        changed=substitute_formula(inner,"x",Var("y"))
        self.assertEqual(free_variables(changed),frozenset({"y"}))
        self.assertNotEqual(changed.args[0],"y")
        self.assertNotEqual(changed.args[1].args[1].args[0],"y")
        # Bound x must NEVER be replaced as if observed free data.
        closed=Forall("x",Pred("P",Var("x")))
        self.assertEqual(substitute_formula(closed,"x",Num(6)),closed)
        self.assertEqual(substitute_term(Add(Var("x"),Num(1)),
                                         "x",Num(3)),
                         Add(Num(3),Num(1)))

    def test_diagonal_lemma_syntax_skeleton_is_really_self_indexed(self):
        """Finite genuine diagonalization, NOT an object-level PA proof."""
        template=Not(Pred("ProvableCode",Var("x")))
        cert=diagonal_syntax(template)
        self.assertTrue(cert.verify())
        self.assertEqual(free_variables(cert.sentence),frozenset())
        self.assertEqual(
            cert.expected_consequent,
            Not(Pred("ProvableCode",Num(cert.sentence_code))))
        self.assertEqual(
            diagonalize_formula_code(cert.theta_code),cert.sentence_code)
        self.assertEqual(godel_code(cert.theta),cert.theta_code)
        self.assertEqual(godel_code(cert.sentence),cert.sentence_code)
        self.assertNotEqual(cert.theta_code,cert.sentence_code)
        self.assertFalse(cert.representability_in_PA_proved)
        self.assertFalse(cert.object_language_equivalence_proved)
        # The meta-level formula and consequent need not be syntactically
        # equal: the standard theorem requires representable substitution.
        self.assertNotEqual(cert.sentence,cert.expected_consequent)
        other=diagonal_syntax(Pred("Witness",Var("x")))
        self.assertTrue(other.verify())
        self.assertNotEqual(cert.sentence_code,other.sentence_code)

    def test_diagonal_inputs_cannot_smuggle_closed_formula(self):
        for bad in (Pred("P",Num(5)), Pred("P",Var("y")),
                    Pred("P",Var("x"),Var("y"))):
            with self.assertRaises(LogicBoundaryError):
                diagonal_syntax(bad)
        with self.assertRaises(LogicBoundaryError):
            diagonalize_formula_code(godel_code(Pred("P",Num(1))))
        with self.assertRaises(LogicBoundaryError):
            diagonalize_formula_code(godel_code(Num(1)))


class FiniteProofCheckerTests(unittest.TestCase):
    def setUp(self):
        self.a=Pred("A",Num(0))
        self.b=Pred("B",Num(0))
        self.imp=Implies(self.a,self.b)
        self.theory=Theory("T_base",frozenset((self.a,self.imp)))

    def test_modus_ponens_proved_and_code_reversible(self):
        proof=FiniteProof((
            ProofStep(self.a,"axiom"),
            ProofStep(self.imp,"axiom"),
            ProofStep(self.b,"modus_ponens",(0,1)),
        ))
        self.assertTrue(check_finite_proof(self.theory,proof))
        enc=encode_proof(proof)
        self.assertEqual(decode_proof(enc),proof)
        self.assertTrue(verifies_proof_code(self.theory,enc,self.b))
        self.assertFalse(verifies_proof_code(self.theory,enc,self.a))
        self.assertFalse(verifies_proof_code(
            Theory("T_smaller",frozenset((self.a,))),enc,self.b))

    def test_closed_axioms_and_fake_proof_disallowed(self):
        with self.assertRaises(LogicBoundaryError):
            Theory("Bad",frozenset((Pred("P",Var("x")),)))
        bad=FiniteProof((
            ProofStep(self.a,"axiom"),
            ProofStep(self.imp,"axiom"),
            ProofStep(self.b,"modus_ponens",(1,0)),
        ))
        with self.assertRaises(LogicBoundaryError):
            check_finite_proof(self.theory,bad)
        self.assertFalse(verifies_proof_code(self.theory,encode_proof(bad),self.b))
        with self.assertRaises(LogicBoundaryError):
            check_finite_proof(self.theory,FiniteProof((
                ProofStep(self.b,"axiom"),
            )))
        with self.assertRaises(LogicBoundaryError):
            check_finite_proof(self.theory,FiniteProof((
                ProofStep(self.a,"axiom",(0,)),
            )))

    def test_universal_instantiation_requires_a_valid_general_axiom(self):
        allphi=Forall("x",Pred("Observable",Var("x")))
        goal=Pred("Observable",Num(7))
        t=Theory("General",frozenset((allphi,)))
        p=FiniteProof((
            ProofStep(allphi,"axiom"),
            ProofStep(goal,"forall_elim",(0,),Num(7)),
        ))
        self.assertTrue(check_finite_proof(t,p))
        bad=FiniteProof((
            ProofStep(allphi,"axiom"),
            ProofStep(Pred("Observable",Num(8)),"forall_elim",(0,),Num(7)),
        ))
        with self.assertRaises(LogicBoundaryError):
            check_finite_proof(t,bad)

    def test_forall_intro_rejects_generalizing_ones_own_observation(self):
        fact=Pred("Observed",Var("x"))
        t=Theory("Noaxioms",frozenset())
        good=FiniteProof((
            ProofStep(fact,"assumption"),
            ProofStep(Forall("y",fact),"forall_intro",(0,)),
        ))
        self.assertTrue(check_finite_proof(t,good,assumptions=(fact,)))
        bad=FiniteProof((
            ProofStep(fact,"assumption"),
            ProofStep(Forall("x",fact),"forall_intro",(0,)),
        ))
        with self.assertRaises(LogicBoundaryError):
            check_finite_proof(t,bad,assumptions=(fact,))
        with self.assertRaises(LogicBoundaryError):
            check_finite_proof(t,good)  # an assumption does not prove a theorem

    def test_omega_and_reflection_are_not_hidden_finite_rules(self):
        for unearned in ("omega","reflect","semantic_report","true_by_observation",
                         "infinite_limit","godel_diagonal"):
            p=FiniteProof((ProofStep(self.b,unearned),))
            with self.assertRaises(LogicBoundaryError):
                check_finite_proof(self.theory,p)
            self.assertFalse(verifies_proof_code(self.theory,encode_proof(p),self.b))

    def test_proof_coding_rejects_malformed_and_future_ancestry(self):
        p=FiniteProof((ProofStep(self.a,"axiom",(1,)),))
        with self.assertRaises(LogicBoundaryError):
            check_finite_proof(self.theory,p)
        for bad in (0,-2,1.2,godel_code(self.a)):
            with self.assertRaises(LogicBoundaryError):
                decode_proof(bad)
        with self.assertRaises(LogicBoundaryError):
            FiniteProof(())
        with self.assertRaises(LogicBoundaryError):
            ProofStep(self.a,"axiom",(True,))
        self.assertFalse(verifies_proof_code(self.theory,31,self.a))


if __name__=="__main__":
    unittest.main()
