"""Independent focused calibration of Farey height shields; NO global normality claim."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from farey_height_shield import (
    FareyBracket, RationalInterval, CircleBetaSource, BBPFourPoleSource,
    SparseNonnormalSource, MacroObserver, BudgetExhausted, certify_height,
    verify_height_certificate, TranslatedSource, separate_named_reals,
    four_pole,
)


def naive_prefix(n: int, kind: str) -> str:
    from farey_height_shield import source
    s = source(kind)
    f = FareyBracket()
    letters = []
    for _ in range(n):
        q = Q(f.a+f.c, f.b+f.d)
        for depth in range(128):
            if s.interval.hi <= q:
                f = f.run("L",1)
                letters.append("L")
                break
            if s.interval.lo >= q:
                f = f.run("R",1)
                letters.append("R")
                break
            s.refine()
        else:
            raise RuntimeError("naive oracle unavailable")
    return "".join(letters)


class HeightShieldTests(unittest.TestCase):
    def test_farey_denominator_barrier_exact(self):
        bracket = FareyBracket(333,106,355,113)
        self.assertEqual(bracket.denominator_threshold,219)
        self.assertEqual(bracket.width,Q(1,106*113))
        for d in range(1,219):
            lo = (bracket.a*d)//bracket.b
            hi = (bracket.c*d)//bracket.d + 1
            for p in range(lo,hi+1):
                self.assertFalse(bracket.lo<Q(p,d)<bracket.hi)
        with self.assertRaises(ValueError):
            FareyBracket(333,106,355,114)

    def test_source_invariants_geometry_and_original_bbp(self):
        circ = CircleBetaSource()
        bbp = BBPFourPoleSource()
        for _ in range(18):
            old_c, old_b = circ.interval, bbp.interval
            circ.refine()
            bbp.refine()
            self.assertTrue(old_c.lo <= circ.interval.lo < circ.interval.hi < old_c.hi)
            self.assertTrue(old_b.lo < bbp.interval.lo < bbp.interval.hi < old_b.hi)
        self.assertEqual(four_pole(1),Q(47,15))
        for j in range(1,21):
            self.assertGreater(four_pole(j),four_pole(j+1))
        with self.assertRaises(ValueError):four_pole(True)

    def test_canonical_succ_source_when_installed(self):
        try:
            from observational_succ.duck_bbp import forcing
        except ModuleNotFoundError:
            self.skipTest("canonical SUCC package not installed in standalone scratch")
        for j in range(1,80):
            self.assertEqual(four_pole(j),forcing(j))

    def test_compression_and_cross_source_1000(self):
        expected=[("L",6),("R",15),("L",1),("R",7)]
        for kind in ("circle_beta","bbp_four_pole"):
            c=certify_height(1000,kind)
            self.assertTrue(verify_height_certificate(c))
            self.assertEqual(c.steps,29)
            self.assertEqual([(r.arrow,r.count) for r in c.runs],expected)
            self.assertEqual(c.final,(2818,897,355,113))
            self.assertGreater(c.uniform_margin,0)
            self.assertEqual(c.classify(Q(355,113)),"ABOVE_TARGET")
            self.assertEqual(c.classify(Q(333,106)),"BELOW_TARGET")

    def test_no_close_call_forever_at_height_66317(self):
        expected=[("L",6),("R",15),("L",1),("R",292),("L",1),("R",1)]
        for kind in ("circle_beta","bbp_four_pole"):
            c=certify_height(66317,kind)
            self.assertTrue(verify_height_certificate(c))
            self.assertEqual(c.steps,316)
            self.assertEqual([(r.arrow,r.count) for r in c.runs],expected)
            self.assertEqual(c.final,(208341,66317,104348,33215))
            self.assertEqual(c.classify(Q(208341,66317)),"BELOW_TARGET")
            self.assertEqual(c.classify(Q(355,113)),"ABOVE_TARGET")

    def test_height_family_monotonicity(self):
        heights=[1,2,7,10,100,113,218,1000,33215,66317,1000000]
        old=None
        for H in heights:
            c=certify_height(H,"bbp_four_pole")
            self.assertTrue(verify_height_certificate(c))
            b=FareyBracket(*c.final)
            self.assertGreater(b.denominator_threshold,H)
            self.assertLessEqual(c.steps,max(0,H-1))
            if old is not None:
                prior=FareyBracket(*old.final)
                self.assertGreaterEqual(b.lo,prior.lo)
                self.assertLessEqual(b.hi,prior.hi)
            old=c

    def test_exhaustive_bounded_denominator_family(self):
        c=certify_height(30)
        b=FareyBracket(*c.final)
        for denominator in range(1,31):
            for numerator in range(0,5*denominator+1):
                x=Q(numerator,denominator)
                self.assertFalse(b.lo<x<b.hi)
                classification=c.classify(x)
                self.assertEqual(classification,"BELOW_TARGET" if x<=b.lo else "ABOVE_TARGET")

    def test_exact_positive_margin_for_every_low_height_candidate(self):
        for H in (7,100,218):
            c=certify_height(H,"circle_beta")
            x_lo,x_hi=c.final_source_lo,c.final_source_hi
            for denominator in range(1,H+1):
                if denominator>15:break  # low-height exhaustive; general follows Farey lemma
                for numerator in range(2*denominator,5*denominator):
                    x=Q(numerator,denominator)
                    if c.classify(x)=="BELOW_TARGET":
                        self.assertGreaterEqual(x_lo-x,c.uniform_margin)
                    else:
                        self.assertGreaterEqual(x-x_hi,c.uniform_margin)

    def test_macro_replay_matches_one_arrow_at_a_time(self):
        c=certify_height(1000000,"circle_beta")
        expanded="".join(r.arrow*r.count for r in c.runs)
        self.assertEqual(len(expanded),322)
        self.assertEqual(expanded,naive_prefix(322,"bbp_four_pole"))
        self.assertTrue(verify_height_certificate(c))

    def test_budget_exhaustion_is_unknown(self):
        o=MacroObserver("circle_beta")
        o.s=type("RationalMediantSource", (), {
            "stage":0,"interval":RationalInterval(Q(3),Q(4)),
            "refine":lambda self: (setattr(self,"stage",self.stage+1),setattr(self,"interval",RationalInterval(Q(7,2)-Q(1,2**(self.stage+2)),Q(7,2)+Q(1,2**(self.stage+2)))))
        })()
        with self.assertRaises(BudgetExhausted): o.shield(10,max_refinements=12)
        with self.assertRaises(BudgetExhausted):
            separate_named_reals(CircleBetaSource(),CircleBetaSource(),budget=4)

    def test_forged_source_endpoint_and_margin_rejected(self):
        c=certify_height(100,"circle_beta")
        self.assertTrue(verify_height_certificate(c))
        with self.assertRaises(ValueError):
            verify_height_certificate(replace(c,uniform_margin=c.uniform_margin+Q(1,100)))
        r=c.runs[0]
        with self.assertRaises(ValueError):
            verify_height_certificate(replace(c,runs=(replace(r,source_lo=r.source_lo+Q(1,100)),)+c.runs[1:]))
        with self.assertRaises(ValueError):
            verify_height_certificate(replace(c,final=(3,1,22,7)))

    def test_integer_type_boundary(self):
        with self.assertRaises(ValueError):certify_height(True)
        with self.assertRaises(ValueError):certify_height(0)
        with self.assertRaises(ValueError):FareyBracket(3,1,4,True)
        c=certify_height(100)
        with self.assertRaises(ValueError):c.classify(Q(5,101))

    def test_source_agnostic_height_shield_does_not_imply_normality(self):
        s=SparseNonnormalSource()
        for _ in range(3):s.refine()
        self.assertTrue(s.interval.lo<s.interval.hi)
        for H in (100,1000):
            c=certify_height(H,"sparse_nonnormal")
            self.assertTrue(verify_height_certificate(c))
            self.assertGreater(c.uniform_margin,0)
            self.assertEqual(c.classify(Q(3)),"BELOW_TARGET")

    def test_two_computable_real_names_separated_finitely(self):
        delta=Q(1,16**60)
        with self.assertRaises(BudgetExhausted):
            separate_named_reals(BBPFourPoleSource(),
                TranslatedSource(BBPFourPoleSource(),delta),budget=5)
        w=separate_named_reals(BBPFourPoleSource(),
            TranslatedSource(BBPFourPoleSource(),delta),budget=80)
        self.assertEqual(w.relation,"FIRST_BELOW_SECOND")
        self.assertLess(w.first.hi,w.rational_probe)
        self.assertLess(w.rational_probe,w.second.lo)
        self.assertGreater(w.stage,5)
        with self.assertRaises(ValueError):TranslatedSource(BBPFourPoleSource(),0.01)

    def test_full_macro_run_292_and_short_height_shield(self):
        c=certify_height(33215,"bbp_four_pole")
        self.assertTrue(verify_height_certificate(c))
        self.assertEqual([r.count for r in c.runs],[6,15,1,292,1])
        self.assertTrue(c.runs[3].complete_run)
        self.assertLess(c.final_source_stage,15)


if __name__ == "__main__":
    unittest.main()
