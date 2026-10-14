"""Independent finite oracles for source/model graph, rational identity, compactness boundary."""
import unittest
from fractions import Fraction as F
from itertools import product, combinations
from random import Random
from observational_succ.global_model_sandwich import (
    SourceChart,ModelArrow,FiniteModelGraph,SandwichError,RationalChart,
    rational_global_identity,poly_eval,poly_add,poly_scale,poly_mul,
    symmetric_finite_sample_mutant,harmonic,prime_current_coefficients,
    finite_part_observation,laurent_log_derivative_germ,noncompact_parity_alias,demo_receipt,
    factorial_succ_coefficients,divisor_jet_coefficients,factorial_prime_sandwich
)


def graph(reports, source="S", arrow=()):
    n=len(reports[0])
    return FiniteModelGraph(source,0,"basis-v1",tuple("s"+str(i) for i in range(n)),
         tuple(SourceChart("q"+str(i),source,0,"basis-v1",tuple(q)) for i,q in enumerate(reports)),
         tuple(arrow))

class FiniteSourceGraphTests(unittest.TestCase):
    def test_complete_binary_pair_is_only_jointly_decidable(self):
        g=graph((("0","0","1","1"),("0","1","0","1")))
        t=("0","1","1","0")
        self.assertFalse(g.certify_target(t,("q0",)).identified)
        self.assertEqual(g.certify_target(t,("q0",)).collision,("s0","s1"))
        self.assertFalse(g.certify_target(t,("q1",)).identified)
        cert=g.certify_target(t,("q0","q1"))
        self.assertTrue(cert.identified)
        self.assertEqual(g.minimal_contexts(t),(("q0","q1"),))
        self.assertEqual(cert.physical_implementation_verified,False)
        self.assertEqual(len(cert.decoder),4)

    def test_proper_subset_and_constant_target(self):
        g=graph((("a","b","b"),("x","x","y")))
        self.assertEqual(g.minimal_contexts(("same",)*3),((),))
        self.assertEqual(g.minimal_contexts(("0","1","1")),(("q0",),))
        self.assertFalse(g.certify_target(("0","1","2"),("q0",)).identified)
        self.assertTrue(g.certify_target(("0","1","2"),("q0","q1")).identified)

    def test_all_complete_three_source_reports_against_independent_pair_oracle(self):
        source=("s0","s1","s2")
        all_reports=list(product("01",repeat=3))
        for q,r,t in product(all_reports,all_reports,all_reports):
            g=graph((q,r))
            for names in ((),("q0",),("q1",),("q0","q1")):
                cert=g.certify_target(t,names)
                # Explicit index-based oracle, independent from graph.report and decoder implementation
                indices=[int(nm[1:]) for nm in names]
                oracle=all(any((q,r)[a][i]!=(q,r)[a][j] for a in indices) or t[i]==t[j]
                           for i in range(3) for j in range(3))
                self.assertEqual(cert.identified,oracle)
                if not cert.identified:
                    i=source.index(cert.collision[0]);j=source.index(cert.collision[1])
                    self.assertNotEqual(t[i],t[j])
                    self.assertTrue(all((q,r)[a][i]==(q,r)[a][j] for a in indices))

    def test_source_derived_arrow_and_composite(self):
        s=("s0","s1","s2","s3")
        a=SourceChart("bits","S",0,"v",("00","01","10","11"))
        b=SourceChart("left","S",0,"v",("0","0","1","1"))
        c=SourceChart("constant","S",0,"v",("x",)*4)
        edges=(ModelArrow("bits","left",(("00","0"),("01","0"),("10","1"),("11","1"))),
               ModelArrow("left","constant",(("0","x"),("1","x"))))
        g=FiniteModelGraph("S",0,"v",s,(a,b,c),edges)
        self.assertEqual(dict(g.transport(("bits","left","constant"))),dict.fromkeys(a.image,"x"))
        self.assertEqual(dict(g.transport(("bits","left"))),{"00":"0","01":"0","10":"1","11":"1"})
        with self.assertRaises(SandwichError):g.transport(("constant","bits"))

    def test_false_source_arrows_and_malformed_origins_rejected(self):
        g=graph((("0","1"),("a","b")))
        arrow=ModelArrow("q0","q1",(("0","a"),("1","a")))
        with self.assertRaisesRegex(SandwichError,"false source transport"):
            graph((("0","1"),("a","b")),arrow=(arrow,))
        with self.assertRaises(SandwichError):
            graph((("0","1"),("a","b")),arrow=(ModelArrow("q0","q1",(("0","a"),)),))
        with self.assertRaises(SandwichError):
            FiniteModelGraph("S",0,"basis-v1",("s0","s1"),(
                SourceChart("x","other-source",0,"basis-v1",("a","b")),))
        with self.assertRaises(SandwichError):
            FiniteModelGraph("S",0,"basis-v1",("s0","s1"),(
                SourceChart("x","S",1,"basis-v1",("a","b")),))
        with self.assertRaises(SandwichError):g.certify_target(("0",),("q0",))
        with self.assertRaises(SandwichError):g.certify_target(("0","1"),("q0","q0"))

    def test_minimal_contexts_fresh_random_source_tables(self):
        rng=Random(16931)
        for _ in range(170):
            charts=tuple(tuple(str(rng.randrange(3)) for _ in range(4)) for j in range(3))
            tgt=tuple(str(rng.randrange(2)) for _ in range(4))
            g=graph(charts)
            oracle=[]
            for length in range(4):
                oracle=[q for q in combinations(range(3),length) if all(
                    tgt[i]==tgt[j] or any(charts[k][i]!=charts[k][j] for k in q)
                    for i in range(4) for j in range(4))]
                if oracle:break
            self.assertEqual(g.minimal_contexts(tgt),tuple(tuple("q"+str(k) for k in t) for t in oracle))

class AlgebraicGlobalCertificateTests(unittest.TestCase):
    def test_exact_rational_identity_including_removable_singularity(self):
        a=RationalChart((-1,0,1),(-1,1))
        b=RationalChart((1,1),(1,))
        c=rational_global_identity(a,b)
        self.assertTrue(c["equal_on_common_domain"])
        self.assertEqual(c["cross_polynomial"],(F(0),))
        with self.assertRaises(SandwichError):a.value(1)
        self.assertEqual(b.value(1),2)
        self.assertEqual(a.value(2),3)

    def test_nonidentity_returns_exact_witness(self):
        a=RationalChart((1,0,1),(1,1))
        b=RationalChart((2,1),(2,1))
        r=rational_global_identity(a,b)
        self.assertFalse(r["equal_on_common_domain"])
        x,aa,bb=r["witness"]
        self.assertEqual(aa,a.value(x));self.assertEqual(bb,b.value(x))
        self.assertNotEqual(aa,bb)

    def test_exhaustive_small_polynomials_independent_integer_samples(self):
        polys=[tuple(F(x) for x in p) for p in product((-1,0,1),repeat=3)]
        for p,q in product(polys,repeat=2):
            if p==(F(0),)*3 and q==(F(0),)*3:continue
            diff=poly_add(p,poly_scale(q,-1))
            self.assertEqual(diff==(F(0),),all(poly_eval(p,x)==poly_eval(q,x) for x in range(3)))
        self.assertEqual(poly_mul((1,1),(1,-1)),(F(1),F(0),F(-1)))
        with self.assertRaises(SandwichError):RationalChart((1,),(0,))
        with self.assertRaises(SandwichError):RationalChart((1.1,),(1,))

    def test_symmetric_entire_mutants_match_arbitrary_finite_samples_but_zero_offline(self):
        for xs in ((),(F(0),),(F(0),F(1)),(F(1,2),F(3,2),F(-2)),tuple(F(k,3) for k in range(8))):
            w=symmetric_finite_sample_mutant(xs)
            p=w["polynomial"]
            for x in xs:self.assertEqual(poly_eval(p,x),1)
            self.assertEqual(poly_eval(p,w["off_line_zero"]),0)
            self.assertEqual(poly_eval(p,w["mirror_zero"]),0)
            for k in range(-7,8):self.assertEqual(poly_eval(p,k),poly_eval(p,1-k))
            self.assertFalse(w["authentic_zeta_source"])

class ArithmeticConstantAndDarknessTests(unittest.TestCase):
    def test_exact_harmonic_finite_values(self):
        self.assertEqual(harmonic(1),1)
        self.assertEqual(harmonic(5),F(137,60))
        for n in range(1,35):self.assertEqual(harmonic(n+1)-harmonic(n),F(1,n+1))
        with self.assertRaises(SandwichError):harmonic(0)

    def test_prime_current_exact_coefficient_oracle_from_prime_powers(self):
        for limit in range(2,120):
            c=dict(prime_current_coefficients(limit))
            brute={}
            for n in range(2,limit+1):
                for p in range(2,n+1):
                    if any(p%d==0 for d in range(2,p)):continue
                    m=p
                    while m<n:m*=p
                    if m==n:
                        brute[p]=brute.get(p,F(0))+F(1,n)
                        break
            self.assertEqual(c,brute)
        self.assertEqual(dict(prime_current_coefficients(12))[2],F(1,2)+F(1,4)+F(1,8))
        self.assertNotIn(6,dict(prime_current_coefficients(100)))

    def test_additive_factorial_vs_multiplicative_prime_jet_identity_all_cutoffs(self):
        for n in range(1,205):
            a=dict(factorial_succ_coefficients(n))
            b=dict(divisor_jet_coefficients(n))
            self.assertEqual(a,b)
            self.assertTrue(factorial_prime_sandwich(n)["same_formal_log_factorial"])
            for p,k in a.items():
                m=p;oracle=0
                while m<=n:
                    oracle+=n//m;m*=p
                self.assertEqual(k,oracle)
            self.assertEqual(factorial_prime_sandwich(n)["fake_composite_six_produces_extra_log6_multiplicity"],n//6)

    def test_fake_composite_as_new_source_generator_breaks_factorial_coupling(self):
        for n in (6,7,12,19,35,100):
            original=dict(divisor_jet_coefficients(n))
            fake2=dict(original)
            fake3=dict(original)
            fake2[2]+=n//6  # treating an independent log(6) as log(2)+log(3)
            fake3[3]+=n//6
            actual=dict(factorial_succ_coefficients(n))
            self.assertNotEqual(fake2,actual)
            self.assertNotEqual(fake3,actual)
        self.assertEqual(factorial_prime_sandwich(5)["fake_composite_six_produces_extra_log6_multiplicity"],0)
        with self.assertRaises(SandwichError):factorial_prime_sandwich(0)

    def test_two_independent_finite_part_scale_shifts(self):
        u=finite_part_observation(100,1,1)
        a=finite_part_observation(100,2,3)
        from math import log
        self.assertAlmostEqual(a["sum"]-u["sum"],-log(6),places=12)
        self.assertFalse(u["source_calibrated"])
        self.assertFalse(u["global_limit_certified"])
        with self.assertRaises(SandwichError):finite_part_observation(12,0,1)

    def test_laurent_prime_current_germ_exact_and_mutants(self):
        for c,d in product((F(-2),F(0),F(1,3),F(2)),(F(-1,2),F(0),F(3))):
            r=laurent_log_derivative_germ(c,d)
            self.assertEqual((r["pole"],r["constant"],r["linear"]),(1,-c,c*c-2*d))
            self.assertTrue(r["finite_part_cancelled_with_original_constant"])
        with self.assertRaises(SandwichError):laurent_log_derivative_germ(0.577,0)

    def test_discrete_noncompact_parity_has_no_finite_uniform_probe(self):
        for probes in ((),(0,1,2),(5,7,8,3),tuple(range(100))):
            r=noncompact_parity_alias(probes)
            self.assertNotIn(r["even"],probes);self.assertNotIn(r["odd"],probes)
            self.assertEqual(r["even"]%2,0);self.assertEqual(r["odd"]%2,1)
            self.assertTrue(r["both_all_zero_reports"])
        with self.assertRaises(SandwichError):noncompact_parity_alias((-1,))

    def test_scientific_receipt_stops_short_of_unsupported_claims(self):
        r=demo_receipt()
        self.assertEqual(r["status"],"EXACT_FINITE_MODEL_SANDWICH_RECEIPT")
        self.assertFalse(r["finite_model"]["individual_A_identifies_XOR"])
        self.assertTrue(r["finite_model"]["joint_identifies_XOR"])
        self.assertFalse(r["finite_model"]["physical_joint_access_verified"])
        self.assertFalse(r["truth_gates"]["global_source_completeness_verified"])
        self.assertFalse(r["truth_gates"]["RH_or_Weil_positivity_proved"])
        self.assertEqual(r["symbolic_global_identity"]["cross_polynomial"],["0"])

if __name__=="__main__":unittest.main()
