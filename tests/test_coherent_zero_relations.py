"""Independent exact checks of multibasis zero certificates and orbit obstructions."""
import random
import unittest
from fractions import Fraction as Q

from observational_succ.coherent_zero_relations import (
    Poly,ZeroDomainError,ZeroRelation,ZeroRoute,ZeroProof,
    bbp_zero_balance,bbp_finite_positive_kernel,finite_coboundary,
    CycleObstruction,CoboundarySolution,base16_graph,digit_discrepancy,
    finite_orbit_sum,BoundaryRelation,finite_prefix_coboundary,finite_coboundary_minimax,
)


class PolynomialZeroCertificates(unittest.TestCase):
    def test_multibasis_bbp_balance_not_just_numerical(self):
        proof=bbp_zero_balance()
        self.assertTrue(proof.check())
        self.assertFalse(proof.inconsistent_unit_witness)
        self.assertEqual(proof.target.variables,('t','P','Q'))
        # Independent rational evaluation of BOTH original chart constraints.
        for t in (Q(-2),Q(0),Q(1,6),Q(1,3),Q(2,3),Q(1),Q(3)):
            A=4-2*t**3-t**4-t**5
            B=(t*t+2)*(t*t+2*t+2)
            self.assertEqual(proof.target.at((t,A,B)),0)
        with self.assertRaises(ZeroDomainError):
            proof.target+proof.routes[0].relation.expression

    def test_false_signed_pole_mutation_rejected_algebraically(self):
        proof=bbp_zero_balance()
        first,second=proof.routes
        signed=('t','P')
        t,p=Poly.var(signed,'t'),Poly.var(signed,'P')
        fake=ZeroRelation(first.relation.source_id,'mutant-fourth-pole',
                          p-(4-2*t**3-t**4-2*t**5))
        mutant=ZeroProof(proof.source_id,proof.target,
                  (ZeroRoute(fake,first.images,first.multiplier),second))
        with self.assertRaisesRegex(ZeroDomainError,'not a polynomial identity'):
            mutant.check()

    def test_same_basis_random_point_evaluation_and_substitution(self):
        names=('u','v')
        u,v=Poly.var(names,'u'),Poly.var(names,'v')
        source=(u+v)**3-(u**3+3*u**2*v+3*u*v**2+v**3)
        self.assertTrue(source.is_zero)
        tgt=('x',)
        x=Poly.var(tgt,'x')
        assert source.substitute((x+2,2*x-3)).is_zero
        rng=random.Random(171)
        for _ in range(50):
            a,b=Q(rng.randint(-8,8),rng.randint(1,9)),Q(rng.randint(-8,8),rng.randint(1,9))
            self.assertEqual(((u+v)**3).at((a,b)),(a+b)**3)

    def test_source_mismatch_and_route_mismatch_fail_closed(self):
        proof=bbp_zero_balance()
        a,b=proof.routes
        counterfeit=ZeroRelation('other-BBP-source','positive-factor',b.relation.expression)
        wrong=ZeroProof(proof.source_id,proof.target,
                       (a,ZeroRoute(counterfeit,b.images,b.multiplier)))
        with self.assertRaisesRegex(ZeroDomainError,'mixed original-source'):
            wrong.check()
        with self.assertRaises(ZeroDomainError):
            b.relation.expression.substitute((a.images[0],))

    def test_inconsistent_zero_relations_yield_unit_obstruction(self):
        names=('x',)
        x=Poly.var(names,'x')
        one=Poly.const(names,1)
        r1=ZeroRelation('impossible-source','chart-0',x)
        r2=ZeroRelation('impossible-source','chart-1',x-1)
        p=ZeroProof('impossible-source',one,
                    (ZeroRoute(r1,(x,),one),ZeroRoute(r2,(x,),-one)))
        self.assertTrue(p.check())
        self.assertTrue(p.inconsistent_unit_witness)
        # At any rational x, both generators cannot vanish simultaneously.
        for a in (Q(-1),Q(0),Q(1),Q(7,4)):
            self.assertNotEqual((x.at((a,)),(x-1).at((a,))),(0,0))

    def test_positive_factor_requires_ordered_chart(self):
        for t in (Q(0),Q(1,10),Q(1,2),Q(7,8),Q(1)):
            P=bbp_finite_positive_kernel(t)
            self.assertGreaterEqual(P,0)
            self.assertEqual(P,4-2*t**3-t**4-t**5)
            if t<1:self.assertGreater(P,0)
        with self.assertRaises(ZeroDomainError):
            bbp_finite_positive_kernel(Q(3,2))


class CoboundaryAndNormalityFirewall(unittest.TestCase):
    def test_finite_cohomological_equation_if_cycle_sums_vanish(self):
        T=(1,2,0,4,3)
        g=(Q(5),Q(9),Q(-2),Q(3),Q(11))
        f=tuple(g[i]-g[T[i]] for i in range(len(T)))
        s=finite_coboundary(T,f)
        self.assertIsInstance(s,CoboundarySolution)
        self.assertTrue(s.exact)
        self.assertTrue(all(s.potential[i]-s.potential[T[i]]==f[i] for i in range(len(T))))
        for start in range(len(T)):
            for h in (0,1,2,3,5,17):
                v,end=finite_orbit_sum(T,f,start,h)
                self.assertEqual(v,s.potential[start]-s.potential[end])

    def test_periodic_fixed_point_obstructs_uniform_digit_zero(self):
        for m in (7,11,13,17):
            T=base16_graph(m)
            f=digit_discrepancy(m)
            self.assertEqual(T[0],0)
            self.assertEqual(f[0],Q(15,16))
            outcome=finite_coboundary(T,f)
            self.assertIsInstance(outcome,CycleObstruction)
            self.assertNotEqual(outcome.signed_sum,0)
            self.assertEqual(sum(f[x] for x in outcome.cycle),outcome.signed_sum)

    def test_every_finite_prefix_has_zero_identity_but_not_sublinear(self):
        for length in (1,5,17,32):
            samples=(Q(1),)*length
            g=finite_prefix_coboundary(samples)
            self.assertEqual(g[0],0)
            self.assertEqual(g[-1],length)
            self.assertEqual((g[-1]-g[0])/length,1)

    def test_sharp_minimax_coboundary_cycle_obstruction(self):
        for m in (7,11,17):
            T=base16_graph(m)
            f=digit_discrepancy(m)
            certificate=finite_coboundary_minimax(T,f)
            self.assertEqual(certificate.optimal_uniform_residual,Q(15,16))
            self.assertEqual(certificate.residual[0],Q(15,16))
            self.assertEqual(certificate.potential[0]-certificate.potential[T[0]],0)
            for i in range(m):
                self.assertEqual(certificate.potential[i]-certificate.potential[T[i]]+
                                 certificate.residual[i],f[i])
            self.assertEqual(max(abs(v) for v in certificate.residual),
                             certificate.optimal_uniform_residual)

    def test_cycle_mean_bound_is_globally_sharp(self):
        T=(1,2,0,4,3,0)
        f=tuple(map(Q,(2,3,7,-2,6,9)))
        cert=finite_coboundary_minimax(T,f)
        self.assertEqual(cert.optimal_uniform_residual, Q(4))
        # Mean of (2,3,7) is 4; mean (-2,6) is 2; transient 9 is absorbed.
        self.assertEqual(cert.residual[5],0)
        self.assertTrue(all(cert.potential[i]-cert.potential[T[i]]+
                            cert.residual[i]==f[i] for i in range(len(T))))

    def test_finite_cohomology_invalid_inputs(self):
        with self.assertRaises(ZeroDomainError):finite_coboundary((1,2),(Q(0),Q(0)))
        with self.assertRaises(ZeroDomainError):finite_coboundary((0,),(.1,))
        with self.assertRaises(ZeroDomainError):base16_graph(1)
        with self.assertRaises(ZeroDomainError):finite_orbit_sum((0,),(1,),0,-1)


class BoundaryArithmetic(unittest.TestCase):
    def test_two_complementary_bounds_can_cancel(self):
        a=BoundaryRelation('Q:BBP','rational-moment',Q(1,3),Q(1,2),Q(1,6))
        b=BoundaryRelation('Q:BBP','rational-moment',Q(2,3),Q(1,2),Q(1,6))
        result=a.add(b)
        self.assertEqual(result.left,result.right)
        self.assertEqual(result.cap,Q(1,3))  # triangle bound is valid but not sharp
        self.assertEqual(a.scale(-2).cap,Q(1,3))

    def test_wrong_source_chart_or_invalid_tail_rejected(self):
        a=BoundaryRelation('authentic','real',Q(1),Q(1),Q(0))
        b=BoundaryRelation('counterfeit','real',Q(1),Q(1),Q(0))
        c=BoundaryRelation('authentic','p-adic',Q(1),Q(1),Q(0))
        for x in (b,c):
            with self.assertRaises(ZeroDomainError):a.add(x)
        with self.assertRaises(ZeroDomainError):BoundaryRelation('a','b',Q(1),Q(2),Q(1,2))
        with self.assertRaises(ZeroDomainError):BoundaryRelation('a','b',Q(1),Q(1),Q(-1))


if __name__=='__main__':unittest.main()
