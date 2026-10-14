"""Independent exact controls for Pascal Hopf, orientation, boundary and Gamma."""
from __future__ import annotations

import unittest
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, isqrt

from observational_succ.pascal_rotated_transport import (
    PascalTransportError,UnitFrame,SyntheticPascalReceipt,
    FractionalGammaSUCC,gamma_succ_convolution_moment,
    discrete_wait_probability,discrete_wait_survival,colored_poisson_prefactor,
    count_by_time,time_of_event,count_time_adjunction,
    exp_minus_rational_bracket,continuous_wait_survival_bracket,
    binomial_poisson_total_variation_bound,dual_count_time_certificate,
    antipode_cancellation,apply_pascal,backward_kernel,bayes_backwards_from_p,bounded,
    check_synthetic_receipt,commutator_witness,coproduct_divided,
    coproduct_monomial,cyclic_convolve,divided_power_product,
    evaluate_extension_fiber,exact,factorial_moment, falsely_commutative_sum,
    formal_path_monomials,forward_binomial,group_word_sum,
    generalized_binomial,generalized_pascal_prefix,binomial_absolute_tail_enclosure,
    matmul,matrix_apply,mixture_binomial,ordered_word_fiber,laguerre_two_atom_moment,
    parity_character,pascal_matrix,project_backwards,
    residue_walk_law,rotate_clockwise,shift_moment_recurrence,
    shifted_atomic_moment,shifted_exponential_moment,
    triple_split_coefficient,unrotate_clockwise,weighted_adjoint,weighted_pair,
)
from observational_succ.structural_coupling import discover_couplings


class TestPascalAlgebra(unittest.TestCase):
    def test_pascal_row_recurrence_all_cells(self):
        f=UnitFrame(Q(1,3),Q(5,7))
        for n in range(1,17):
            for k in range(n+1):
                cell=f.cell(n,k)
                parents=f.parents(n,k)
                self.assertEqual(cell.multiplicity, sum(p.multiplicity for p in parents))
                self.assertEqual(cell.address,(n-k)*f.a+k*f.b)
                for parent in parents:
                    self.assertIn(cell.address-parent.address,(f.a,f.b))
        self.assertEqual(f.parents(0,0),())

    def test_formal_vs_specialized_alias(self):
        alias=UnitFrame(2,2,source_id='s',basis_id='b')
        self.assertNotEqual(formal_path_monomials(5)[1][0], formal_path_monomials(5)[2][0])
        witness=alias.collapse_witness(5)
        self.assertIsNotNone(witness)
        self.assertNotEqual(witness[0].k,witness[1].k)
        self.assertEqual(witness[0].address,witness[1].address)
        self.assertIsNone(UnitFrame(2,3).collapse_witness(5))

    def test_triple_coassociativity_independent_splits(self):
        checked=0
        for n in range(13):
            for a in range(n+1):
                for b in range(n-a+1):
                    c=n-a-b
                    l=triple_split_coefficient(n,a,b,c,'left')
                    r=triple_split_coefficient(n,a,b,c,'right')
                    self.assertEqual(l,r)
                    self.assertEqual(l,factorial(n)//(factorial(a)*factorial(b)*factorial(c)))
                    checked+=1
        self.assertGreater(checked,450)

    def test_antipode_and_divided_power_coefficients(self):
        self.assertEqual(antipode_cancellation(0),1)
        for n in range(1,25):self.assertEqual(antipode_cancellation(n),0)
        for n in range(15):
            self.assertEqual(coproduct_monomial(n), formal_path_monomials(n))
            self.assertEqual(len(coproduct_divided(n)),n+1)
            for j in range(n+1):
                self.assertEqual(divided_power_product(j,n-j),comb(n,j))
                self.assertEqual(coproduct_divided(n)[j][1],1)

    def test_pascal_matrices_inverse_composition(self):
        for d,e in ((Q(1),Q(-1)),(Q(1,3),Q(2,5)),(Q(0),Q(7))):
            a=pascal_matrix(9,d)
            b=pascal_matrix(9,e)
            self.assertEqual(matmul(a,b),pascal_matrix(9,d+e))
            self.assertEqual(matmul(a,pascal_matrix(9,-d)),pascal_matrix(9,0))

    def test_finite_difference_binomial_inverse(self):
        for moments in ((0,1,2,3,4,5),(3,-1,1,0,7,-9),(1,0,0,0,0,0)):
            for d in (Q(1),Q(2,3),Q(-2)):
                self.assertEqual(apply_pascal(apply_pascal(moments,d),-d),tuple(map(Q,moments)))

    def test_generalized_pascal_rational_time_and_signed_rows(self):
        for s in (Q(-1,2),Q(0),Q(1,2),Q(2),Q(7,3)):
            for k in range(1,18):
                self.assertEqual(generalized_binomial(s+1,k),
                                 generalized_binomial(s,k)+generalized_binomial(s,k-1))
        for n in range(9):
            for k in range(19):
                self.assertEqual(generalized_binomial(n,k),Q(comb(n,k) if k<=n else 0))
        self.assertEqual(generalized_binomial(Q(1,2),2),Q(-1,8))
        self.assertNotEqual(generalized_binomial(Q(1,2),5),Q(0))
        # A real noninteger row is no longer a counting/probability object.

    def test_exact_generalized_tail_against_sqrt_holdout(self):
        s=Q(1,2);z=Q(1,2);cutoff=18
        series=generalized_pascal_prefix(s,cutoff,z)
        radius=binomial_absolute_tail_enclosure(s,cutoff,z)
        scale=10**12
        lower=isqrt(3*scale**2//2)
        low=Q(lower,scale);high=Q(lower+1,scale)
        self.assertTrue(low*low<=Q(3,2)<high*high)
        self.assertLess(series-radius,high)
        self.assertGreater(series+radius,low)
        self.assertLess(radius,Q(1,10**6))
        with self.assertRaises(PascalTransportError):
            binomial_absolute_tail_enclosure(s,cutoff,Q(1))
        with self.assertRaises(PascalTransportError):
            binomial_absolute_tail_enclosure(Q(-2),cutoff,Q(1,2))

    def test_exponential_generating_intertwiner(self):
        seq=(Q(3),Q(-1,2),Q(7,5),Q(0),Q(4))
        for d in (Q(-1),Q(2,3),Q(5)):
            out=apply_pascal(seq,d)
            for n in range(len(seq)):
                by_product=sum((seq[k]*d**(n-k)/Q(factorial(k)*factorial(n-k)) for k in range(n+1)),Q(0))
                self.assertEqual(out[n]/Q(factorial(n)),by_product)


class TestDualAndBoundary(unittest.TestCase):
    def test_finite_literal_90_degree_rotation(self):
        for N in range(13):
            xy=set()
            for n in range(N+1):
                for k in range(n+1):
                    p=rotate_clockwise(n,k,N)
                    self.assertEqual(unrotate_clockwise(*p,N),(n,k))
                    xy.add(p)
            self.assertEqual(xy,{(x,y) for x in range(N+1) for y in range(N-x+1)})
        self.assertNotEqual(rotate_clockwise(2,1,6),rotate_clockwise(2,1,7))

    def test_weighted_adjoint_is_not_inversion(self):
        P=pascal_matrix(5,Q(2,3))
        weights=(Q(1),Q(2),Q(1,3),Q(4),Q(5),Q(7))
        T=weighted_adjoint(P,weights)
        u=(Q(1),Q(0),Q(3),Q(-2),Q(5),Q(0))
        v=(Q(1),Q(2),Q(-1),Q(3),Q(0),Q(5))
        self.assertEqual(weighted_pair(matrix_apply(P,u),v,weights),
                         weighted_pair(u,matrix_apply(T,v),weights))
        self.assertNotEqual(T,pascal_matrix(5,Q(-2,3)))
        self.assertNotEqual(T,weighted_adjoint(P,(Q(1),)*6))

    def test_bayesian_backtransport_all_rational_sources(self):
        for p in (Q(0),Q(1),Q(1,5),Q(2,3),Q(1,2)):
            self.assertEqual(forward_binomial(0,p),(Q(1),))
            for n in range(1,17):
                row=forward_binomial(n,p)
                self.assertEqual(sum(row),1)
                self.assertEqual(project_backwards(row),forward_binomial(n-1,p))
                for k in range(n+1):
                    self.assertEqual(sum(w for _,w in backward_kernel(n,k)),1)

    def test_backward_same_but_forward_not_identified(self):
        for n in range(1,12):
            self.assertNotEqual(forward_binomial(n,Q(1,3)),forward_binomial(n,Q(2,3)))
            for k in range(n+1):
                self.assertEqual(bayes_backwards_from_p(n,k,Q(1,3)),
                                 bayes_backwards_from_p(n,k,Q(2,3)))
                self.assertEqual(bayes_backwards_from_p(n,k,Q(1,3)),backward_kernel(n,k))
        # Construct two different source laws at the same fixed vertex with
        # identical cotransitions; shape alone does not select a top boundary.
        self.assertEqual(backward_kernel(4,2),((1,Q(1,2)),(2,Q(1,2))))

    def test_nontrivial_mixture_is_projectively_consistent(self):
        mixed=((Q(2,5),Q(1,4)),(Q(3,5),Q(3,4)))
        for n in range(1,13):
            self.assertEqual(project_backwards(mixture_binomial(n,mixed)),mixture_binomial(n-1,mixed))
            self.assertEqual(sum(mixture_binomial(n,mixed)),Q(1))
        self.assertNotEqual(mixture_binomial(3,mixed),forward_binomial(3,Q(11,20)))

    def test_semantic_unit_collapse_is_not_boundary_identification(self):
        f=UnitFrame(3,3)
        self.assertEqual(len({cell.address for cell in f.row(8)}),1)
        self.assertNotEqual(forward_binomial(8,Q(1,3)),forward_binomial(8,Q(2,3)))
        # Address-all-one does not entitle a unique hidden Bernoulli p.


class TestNoncommutingFibre(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.groups=discover_couplings(4,2).candidates
        cls.abelian=tuple(g for g in cls.groups if g.is_abelian())
        cls.noncomm=tuple(g for g in cls.groups if not g.is_abelian())

    def test_explicit_two_step_commutator(self):
        self.assertEqual(len(self.abelian),2)
        self.assertEqual(len(self.noncomm),2)
        for g in self.abelian:self.assertIsNone(commutator_witness(g))
        for g in self.noncomm:
            ab,ba=commutator_witness(g)
            self.assertNotEqual(ab,ba)
            self.assertEqual(sum(n for _,n in evaluate_extension_fiber(g,2,1)),2)
            self.assertEqual(len(evaluate_extension_fiber(g,2,1)),2)

    def test_pascal_fibres_are_ordered_word_partitions(self):
        for n in range(9):
            all_words=set()
            for k in range(n+1):
                words=ordered_word_fiber(n,k)
                self.assertEqual(len(words),comb(n,k))
                all_words.update(words)
            self.assertEqual(all_words,set(product(('A','B'),repeat=n)))

    def test_commuting_binomial_collapse_and_noncommuting_no_go(self):
        for g in self.abelian:
            for n in range(8):
                self.assertEqual(group_word_sum(g,n),falsely_commutative_sum(g,n))
                for k in range(n+1):
                    hist=evaluate_extension_fiber(g,n,k)
                    self.assertEqual(len(hist),1)
                    self.assertEqual(hist[0][1],comb(n,k))
        for g in self.noncomm:
            self.assertNotEqual(group_word_sum(g,2),falsely_commutative_sum(g,2))
            self.assertEqual(group_word_sum(g,0),falsely_commutative_sum(g,0))

    def test_noncommuting_histograms_sum_correct_multiplicity(self):
        for g in self.groups:
            for n in range(6):
                all_ends={}
                for k in range(n+1):
                    for element,m in evaluate_extension_fiber(g,n,k):
                        all_ends[element]=all_ends.get(element,0)+m
                self.assertEqual(tuple(sorted(all_ends.items())),group_word_sum(g,n))
                self.assertEqual(sum(all_ends.values()),2**n)


class TestSpectralAndGamma(unittest.TestCase):
    def test_group_algebra_cyclic_semigroup_exact(self):
        for q in (2,3,5):
            for p in (Q(0),Q(1,3),Q(3,4),Q(1)):
                a,b=1,2
                for n in range(5):
                    for m in range(5):
                        self.assertEqual(cyclic_convolve(residue_walk_law(n,q,a,b,p),
                                                         residue_walk_law(m,q,a,b,p)),
                                         residue_walk_law(n+m,q,a,b,p))

    def test_parity_character_is_spectral_eigenvalue(self):
        for a,b in ((1,2),(0,1),(-3,2)):
            for p in (Q(0),Q(1,2),Q(2,3),Q(1)):
                for n in range(12):
                    r=residue_walk_law(n,2,a,b,p)
                    self.assertEqual(r[0]-r[1],parity_character(n,a,b,p))

    def test_shifted_gamma_moment_by_two_proofs(self):
        for d in (Q(0),Q(1,2),Q(2),Q(-3,2)):
            for rate in (Q(1),Q(2),Q(3,2)):
                seq=tuple(factorial_moment(n,rate) for n in range(11))
                shifted=apply_pascal(seq,d)
                for n in range(len(seq)):
                    self.assertEqual(shifted[n],shifted_exponential_moment(n,d,rate))
                    self.assertEqual(shifted[n],shift_moment_recurrence(n,d,rate))
                    if d==0:self.assertEqual(shifted[n],Q(factorial(n))/rate**n)

    def test_pascal_geometry_does_not_select_gamma(self):
        for d in (Q(0),Q(1),Q(2,3)):
            atomic=tuple(shifted_atomic_moment(n,d) for n in range(9))
            gamma=tuple(shifted_exponential_moment(n,d) for n in range(9))
            self.assertEqual(atomic,apply_pascal((Q(1),)*9,d))
            self.assertEqual(gamma,apply_pascal(tuple(map(factorial,range(9))),d))
            self.assertNotEqual(atomic[2],gamma[2])

    def test_positive_two_atom_source_mimics_first_four_gamma_moments(self):
        self.assertEqual(tuple(laguerre_two_atom_moment(n) for n in range(4)),(1,1,2,6))
        self.assertEqual(laguerre_two_atom_moment(4),20)
        self.assertNotEqual(laguerre_two_atom_moment(4),factorial(4))
        for n in range(2,14):
            self.assertEqual(laguerre_two_atom_moment(n),
                             4*laguerre_two_atom_moment(n-1)-2*laguerre_two_atom_moment(n-2))

    def test_source_scale_changes_gamma_transport(self):
        for rate in (Q(1),Q(2),Q(3,2)):
            for n in range(7):
                self.assertEqual(factorial_moment(n,rate)*rate**n,factorial(n))
        self.assertNotEqual(factorial_moment(3,1),factorial_moment(3,2))


class TestSourceControls(unittest.TestCase):
    def test_receipt_provenance_and_epoch(self):
        frame=UnitFrame(Q(2,3),Q(-3,5),'origin','basis',5)
        r=SyntheticPascalReceipt('origin','basis',5,('A','B','A'),Q(11,15))
        self.assertTrue(check_synthetic_receipt(frame,r))
        with self.assertRaises(PascalTransportError):
            check_synthetic_receipt(frame,SyntheticPascalReceipt('forged','basis',5,r.action_word,r.observed_address))
        with self.assertRaises(PascalTransportError):
            check_synthetic_receipt(frame,SyntheticPascalReceipt('origin','basis',5,r.action_word,Q(3)))
        with self.assertRaises(PascalTransportError):
            SyntheticPascalReceipt('origin','basis',5,(),Q(0),origin='physical_verified')

    def test_malformed_inputs_rejected(self):
        bad=((lambda:exact(.5)),(lambda:bounded(-1)),(lambda:UnitFrame(1,.5)),
             (lambda:UnitFrame(1,2,'','b')),(lambda:forward_binomial(3,Q(2))),
             (lambda:backward_kernel(0,0)),(lambda:project_backwards((Q(1,2),Q(1,3)))),
             (lambda:mixture_binomial(3,((Q(1,2),Q(1,3)),))),
             (lambda:weighted_adjoint(pascal_matrix(2),(1,0,1))),
             (lambda:rotate_clockwise(2,3,3)),(lambda:ordered_word_fiber(11,5)),
             (lambda:factorial_moment(4,0)),(lambda:residue_walk_law(4,0,1,2,Q(1,2))),
             (lambda:parity_character(3,1,2,Q(-1,2))),
             (lambda:bayes_backwards_from_p(3,2,Q(0))))
        for broken in bad:
            with self.subTest(name=str(broken)):
                with self.assertRaises(PascalTransportError):broken()


if __name__=='__main__':unittest.main()


class TestIndependentAnalyticAndReceipt(unittest.TestCase):
    def test_two_atom_surd_oracle_independent_of_recurrence(self):
        # Each pair encodes a+b*sqrt(2); use an independent multiplication
        # implementation rather than the recurrence under test.
        def mult(x,y):
            return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
        def power(x,n):
            val=(Q(1),Q(0))
            for _ in range(n):val=mult(val,x)
            return val
        lo=(Q(2),Q(-1));hi=(Q(2),Q(1))
        wlo=(Q(1,2),Q(1,4)); whi=(Q(1,2),Q(-1,4))
        for n in range(13):
            a=mult(wlo,power(lo,n));b=mult(whi,power(hi,n))
            self.assertEqual(a[1]+b[1],0)
            self.assertEqual(a[0]+b[0],laguerre_two_atom_moment(n))

    def test_real_Mellin_incomplete_gamma_holdout(self):
        try:import mpmath as mp
        except ImportError:self.skipTest('optional mpmath not installed')
        with mp.workdps(55):
            for raw_s,d,rate in ((Q(-1,2),Q(1,2),Q(1)),
                                 (Q(1,3),Q(1,2),Q(3,2)),
                                 (Q(5,2),Q(2),Q(2)),
                                 (Q(0),Q(0),Q(1))):
                s=mp.mpf(raw_s.numerator)/raw_s.denominator
                da=mp.mpf(d.numerator)/d.denominator
                r=mp.mpf(rate.numerator)/rate.denominator
                integral=mp.quad(lambda t: r*mp.exp(-r*t)*(t+da)**s,[0,1,mp.inf])
                completed=mp.exp(r*da)*r**(-s)*mp.gammainc(s+1,r*da,mp.inf)
                self.assertLess(abs(integral-completed),mp.mpf('1e-34'))
                if raw_s.denominator==1 and raw_s>=0:
                    expected=shifted_exponential_moment(int(raw_s),d,rate)
                    exact_mp=mp.mpf(expected.numerator)/expected.denominator
                    self.assertLess(abs(integral-exact_mp),mp.mpf('1e-34'))

    def test_frozen_receipt_recomputation(self):
        from pathlib import Path
        import json
        from scripts.pascal_rotated_transport_probe import receipt
        path=Path(__file__).resolve().parents[1]/'research'/'2026-10-14'/'PASCAL_ROTATED_RECEIPT.json'
        self.assertEqual(receipt(),json.loads(path.read_text(encoding='utf8')))
        data=receipt()
        self.assertTrue(data['boundary']['same_reverse_different_forward'])
        self.assertTrue(data['couplings']['nonabelian_pascal_scalar_collapse_fails'])
        self.assertEqual(data['gamma']['first_exp_vs_2atom_disagreement'],4)
        self.assertTrue(data['gamma']['tail_interval_overlaps_exact_sqrt_bracket'])


class TestPascalPoissonGammaOperationalRotation(unittest.TestCase):
    def test_discrete_count_to_wait_duality_exact(self):
        for events in (1,2,3,5):
            for p in (Q(1,4),Q(1,2),Q(2,3),Q(1)):
                self.assertEqual(discrete_wait_survival(0,events,p),1)
                for m in range(1,31):
                    event=discrete_wait_probability(m,events,p)
                    independent=discrete_wait_survival(m-1,events,p)-discrete_wait_survival(m,events,p)
                    self.assertEqual(event,independent)
                    self.assertTrue(Q(0)<=event<=1)
        self.assertEqual(discrete_wait_survival(20,3,Q(0)),Q(1))
        self.assertEqual(discrete_wait_probability(5,3,Q(0)),Q(0))

    def test_poisson_coloring_reconstructs_pascal_row(self):
        for n in range(13):
            for mean in (Q(0),Q(1,2),Q(1)):
                for p in (Q(1,3),Q(2,3)):
                    joint=sum((colored_poisson_prefactor(n,k,mean,p) for k in range(n+1)),Q(0))
                    self.assertEqual(joint,mean**n/Q(factorial(n)))
                    self.assertEqual(tuple(colored_poisson_prefactor(n,k,mean,p)
                                           for k in range(n+1)),
                                     tuple(mean**n/Q(factorial(n))*a for a in forward_binomial(n,p)))

    def test_rational_exponential_survival_and_variation_bound(self):
        for t in (Q(0),Q(1,4),Q(1,2),Q(1)):
            low,high=exp_minus_rational_bracket(t,22)
            self.assertLessEqual(low,high)
            self.assertLessEqual(high-low,Q(1,10**17))
        for n in (1,2,3,4):
            for m in (4,8,16,32,64):
                cert=dual_count_time_certificate(m,n,Q(1),22)
                self.assertTrue(cert['rigorous_comparison_pass'])
                self.assertEqual(cert['tv_bound'],Q(1,m))
            self.assertLessEqual(continuous_wait_survival_bracket(n,Q(1))[0],
                                 continuous_wait_survival_bracket(n,Q(1))[1])
        with self.assertRaises(PascalTransportError):
            dual_count_time_certificate(3,2,Q(4))
        with self.assertRaises(PascalTransportError):
            exp_minus_rational_bracket(Q(2))

    def test_poisson_survival_limit_is_not_gamma_without_source(self):
        # The same finite Pascal counting algebra allows a different p.
        # p=1/2 at arbitrarily many slots is not p=(lambda*t)/m and does
        # NOT converge to a fixed finite-intensity Poisson count at t=1.
        self.assertLess(discrete_wait_survival(60,3,Q(1,2)),Q(1,100000))
        self.assertGreater(discrete_wait_survival(60,3,Q(1,60)),Q(1,2))


class TestCountTimeAdjunction(unittest.TestCase):
    def test_all_small_sorted_source_paths(self):
        for n in range(1,6):
            for t in product(range(4),repeat=n):
                if tuple(sorted(t))!=t:continue
                path=tuple(Q(v,2) for v in t)
                for now in (Q(0),Q(1,2),Q(1),Q(3,2),Q(2)):
                    for k in range(1,n+1):
                        self.assertTrue(count_time_adjunction(path,now,k))
                        self.assertEqual(time_of_event(path,k)<=now,count_by_time(path,now)>=k)
        self.assertTrue(count_time_adjunction((Q(1),Q(1),Q(1)),Q(1),3))
        with self.assertRaises(PascalTransportError):
            count_by_time((Q(2),Q(1)),Q(2))
        with self.assertRaises(PascalTransportError):
            time_of_event((Q(1),),2)


class TestFractionalGammaSuccSemigroup(unittest.TestCase):
    def test_moment_pascal_hopf_convolution_exact(self):
        for rate in (Q(1),Q(2),Q(3,2)):
            for a,b in ((Q(0),Q(1)),(Q(1),Q(1)),(Q(1,2),Q(1,2)),
                        (Q(1,3),Q(2,5)),(Q(3,2),Q(5,4))):
                x=FractionalGammaSUCC(a,rate)
                y=FractionalGammaSUCC(b,rate)
                z=x.compose(y)
                for n in range(15):
                    self.assertEqual(gamma_succ_convolution_moment(x,y,n),z.moment(n))
                    self.assertEqual(x.compose(y).moment(n),y.compose(x).moment(n))
                self.assertEqual(z.shape,a+b)

    def test_zero_shape_and_integer_erlang_anchor(self):
        for rate in (Q(1),Q(5,2)):
            zero=FractionalGammaSUCC(Q(0),rate)
            self.assertEqual(zero.moment(0),1)
            for n in range(1,8):self.assertEqual(zero.moment(n),0)
            one=FractionalGammaSUCC(Q(1),rate)
            for n in range(12):self.assertEqual(one.moment(n),Q(factorial(n))/rate**n)
            three=one.compose(one).compose(one)
            self.assertEqual(three.shape,3)
            self.assertEqual(three.moment(1),Q(3)/rate)
            self.assertEqual(three.moment(2),Q(12)/rate**2)

    def test_symbolic_laplace_semigroup_and_wrong_rate(self):
        x=FractionalGammaSUCC(Q(1,2),Q(2))
        y=FractionalGammaSUCC(Q(3,2),Q(2))
        base,power=x.laplace_signature(Q(2,3))
        self.assertEqual(base,Q(3,4))
        self.assertEqual(power,Q(1,2))
        self.assertEqual(x.compose(y).laplace_signature(Q(2,3)),(Q(3,4),Q(2)))
        with self.assertRaises(PascalTransportError):
            x.compose(FractionalGammaSUCC(Q(1,2),Q(3)))
        with self.assertRaises(PascalTransportError):
            gamma_succ_convolution_moment(x,FractionalGammaSUCC(Q(1),Q(3)),2)
        with self.assertRaises(PascalTransportError):
            FractionalGammaSUCC(Q(-1,2))

    def test_fractional_gamma_density_laplace_analytic_holdout(self):
        try:import mpmath as mp
        except ImportError:self.skipTest('optional mpmath absent')
        with mp.workdps(50):
            for shape,rate,u in ((Q(1,2),Q(1),Q(1)),
                                 (Q(3,2),Q(2),Q(1,3)),
                                 (Q(5,4),Q(3),Q(2))):
                alpha=mp.mpf(shape.numerator)/shape.denominator
                lam=mp.mpf(rate.numerator)/rate.denominator
                un=mp.mpf(u.numerator)/u.denominator
                normalizer=lam**alpha/mp.gamma(alpha)
                density=lambda t:normalizer*t**(alpha-1)*mp.exp(-lam*t)
                mgf=mp.quad(lambda t: density(t)*mp.exp(-un*t),[0,1,mp.inf])
                expected=(lam/(lam+un))**alpha
                self.assertLess(abs(mgf-expected),mp.mpf('1e-21'))
