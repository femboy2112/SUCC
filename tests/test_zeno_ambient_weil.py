"""Independent exact adversarial tests for Zeno completion and actual source C0."""
import unittest
from fractions import Fraction as Q
from itertools import product
from math import log,cosh,isqrt
from decimal import Decimal, localcontext

from observational_succ.zeno_ambient_weil import (
    ZenoError,SourceFrame,ZenoStage,dichotomy,achilles,sqrt2_completion_chart,
    evaluate_poly, derivative_poly,arrow_derivative_alias,noncommuting_limit_order,
    log2_enclosure,true_carlemann_sample,source_boundary_certificate,
    source_discrete_Carleman_commutator,gamma_H1_signed_error,
    hidden_negative_witness,model_shape_graph,model_proof_path,
    LawEdge,verdict_receipt,
)

class ZenoExact(unittest.TestCase):
    def test_dichotomy_127_exact_tail(self):
        for n in range(128):
            x=dichotomy(n)
            self.assertEqual(x.position+x.tail_upper,1)
            self.assertEqual(x.tail_upper,Q(1,2**n))
            if n:self.assertEqual(x.position-dichotomy(n-1).position,Q(1,2**n))

    def test_achilles_finite_catch_requires_endpoint(self):
        for n in range(16):
            d=achilles(n)
            self.assertEqual(d['elapsed']+d['time_tail_exact'],1)
            self.assertEqual(d['time_tail_exact'],Q(1,10**n))
            self.assertFalse(d['physical_omega_executed'])
            if n:self.assertLess(achilles(n-1)['elapsed'],d['elapsed'])

    def test_achilles_arbitrary_exact_geometric_pursuit(self):
        for gap,speed,slow in ((2,3,1),(Q(2,5),7,0),(Q(19,8),Q(13,4),Q(1,9))):
            for n in (0,1,3,8):
                a=achilles(n,gap,speed,slow)
                self.assertEqual(a['total_catch_time'],Q(gap)/(Q(speed)-Q(slow)))
                self.assertEqual(a['elapsed']+a['time_tail_exact'],a['total_catch_time'])

    def test_sqrt2_nesting_and_irrational_completion(self):
        for n in range(1,40):
            c=sqrt2_completion_chart(n)
            prev=sqrt2_completion_chart(n-1)
            self.assertLessEqual(prev['lower'],c['lower'])
            self.assertLessEqual(c['upper'],prev['upper'])
            self.assertEqual(c['upper']-c['lower'],Q(1,2**n))
            self.assertFalse(c['realization_in_original_Q'])
            self.assertLess(c['lower']**2,2)
            self.assertGreater(c['upper']**2,2)

    def test_arrow_polynomial_duplicate_velocity_witnesses(self):
        for sample in ((Q(-1),Q(0),Q(1)),(Q(1),Q(3)),(Q(-2),Q(0),Q(3),Q(7)),(Q(0),)):
            for pivot in sample:
                t=arrow_derivative_alias(sample,pivot)
                self.assertEqual(evaluate_poly(derivative_poly(t['indistinguishable_motion']),pivot),1)
                for s in sample:self.assertEqual(evaluate_poly(t['indistinguishable_motion'],s),0)

    def test_arrow_mutation_invalid_gauge(self):
        for samples,pivot in (((Q(1),Q(1)),Q(1)),((Q(0),Q(1)),Q(4)),((),Q(0))):
            with self.assertRaises(ZenoError): arrow_derivative_alias(samples,pivot)

    def test_limit_orders_differ_with_finite_positive_entries(self):
        for n,m in product((1,2,17,37),(1,2,7,71)):
            x=noncommuting_limit_order(n,m)
            self.assertEqual(x['entry'],Q(n,n+m))
            self.assertFalse(x['joint_uniform_limit_exists'])
            self.assertNotEqual(x['first_n_then_m'],x['first_m_then_n'])

    def test_zeno_domain_rejects_inexact_inputs(self):
        bad=(True,0.5,1.0,2+0j,'1',None)
        for x in bad:
            with self.assertRaises((ZenoError,TypeError)):
                dichotomy(x)
            with self.assertRaises((ZenoError,TypeError)):
                achilles(1,gap=x)
        with self.assertRaises(ZenoError):sqrt2_completion_chart(1000)

    def test_source_frame_wrong_epoch_and_basis(self):
        a=SourceFrame('zeta',2,'half-density','log-R')
        self.assertTrue(a.match(SourceFrame('zeta',2,'half-density','log-R')))
        self.assertFalse(a.match(SourceFrame('zeta',3,'half-density','log-R')))
        self.assertFalse(a.match(SourceFrame('fake6',2,'half-density','log-R')))
        self.assertFalse(a.match(SourceFrame('zeta',2,'wrong','log-R')))
        with self.assertRaises(ZenoError):SourceFrame('zeta',True,'basis','R')

class SourceCarleman(unittest.TestCase):
    def test_log2_arctanh_enclosure_exact(self):
        prev=None
        with localcontext() as ctx:
            ctx.prec=90
            real_log2=Decimal(2).ln()
        for k in (1,2,3,5,10,20):
            lo,hi=log2_enclosure(k)
            self.assertLess(lo,hi)
            self.assertLess(Decimal(lo.numerator)/Decimal(lo.denominator),real_log2)
            self.assertGreater(Decimal(hi.numerator)/Decimal(hi.denominator),real_log2)
            if prev:self.assertGreaterEqual(lo,prev[0]);self.assertLessEqual(hi,prev[1])
            prev=(lo,hi)

    def test_log2_strict_simple_bound(self):
        lo,hi=log2_enclosure(2)
        self.assertGreater(Q(2,5)*lo,Q(11,40))
        self.assertLess(hi,Q(7,10))
        with self.assertRaises(ZenoError):source_boundary_certificate(1,1)

    def test_C0_true_even_clock_exact_sample(self):
        for k in range(-12,13):
            v=true_carlemann_sample(k)
            self.assertGreater(v,0)
            self.assertEqual(v,Q(2**abs(k),2**(2*abs(k))+1))
            expected=1/(2*cosh(abs(k)*log(2)))
            self.assertAlmostEqual(float(v),expected,places=12)
        self.assertEqual(true_carlemann_sample(0),Q(1,2))
        self.assertEqual(true_carlemann_sample(1),Q(2,5))

    def test_uniform_source_prime_two_commutator_lower(self):
        for a in (Q(7,10),Q(3,4),Q(1),Q(7),Q(100)):
            d=source_boundary_certificate(a,12)
            self.assertGreater(d['commutator_norm_lower'],Q(11,40))
            self.assertTrue(d['true_full_carrier_commutes'])
            self.assertTrue(d['compressed_commutator_strong_to_zero'])
            self.assertFalse(d['compressed_commutator_norm_to_zero'])
            self.assertFalse(d['proved_full_Weil_sign'])
        with self.assertRaises(ZenoError):source_boundary_certificate(Q(1,2))

    def test_exact_sampled_Toeplitz_and_commutator(self):
        for size in range(2,10):
            result=source_discrete_Carleman_commutator(size)
            K=result['Carleman_matrix'];D=result['boundary_commutator']
            self.assertEqual(result['first_boundary_entry'],Q(2,5))
            self.assertEqual(D[-1][-1],-Q(2,5))
            self.assertEqual(K[0][0],Q(1,2))
            for i in range(size):
                for j in range(size):
                    self.assertEqual(K[i][j],K[j][i])
                    self.assertEqual(D[i][j],K[i+1][0] if j==0 and i<size-1 else
                                     -K[size-1][j-1] if i==size-1 and j>0 else Q(0))

    def test_independent_compressed_shift_commutator_oracle(self):
        # Independent index-enumeration of S*K and K*S, not the implementation's matmul.
        for N in (2,3,5,8):
            ans=source_discrete_Carleman_commutator(N)
            K=ans['Carleman_matrix']; D=ans['boundary_commutator']
            for i,j in product(range(N),repeat=2):
                sk= sum((K[m][j] for m in range(N) if m==i+1),Q())
                ks= sum((K[i][m] for m in range(N) if j==m+1),Q())
                self.assertEqual(sk-ks,D[i][j])

    def test_positive_actual_C0_sampled_two_by_two(self):
        K=source_discrete_Carleman_commutator(2)['Carleman_matrix']
        self.assertEqual(K[0][0]*K[1][1]-K[0][1]*K[1][0],Q(9,100))
        self.assertGreater(K[0][0],0)
        # positive C0 still does not sign the full shifted/contact/pole Weil form

    def test_genuine_gamma_signed_error_quadratic(self):
        xs=[gamma_H1_signed_error(J)['epsilon'] for J in (8,16,32,64,128)]
        self.assertTrue(all(x>0 for x in xs))
        self.assertTrue(all(xs[i]>xs[i+1] for i in range(len(xs)-1)))
        self.assertLess(xs[3],Q(1,10000))
        self.assertEqual(gamma_H1_signed_error(64)['epsilon'],Q(2321,33949186))
        self.assertFalse(gamma_H1_signed_error(64)['signed_QJ_proved_positive'])

    def test_hidden_negative_does_not_confuse_original_weil(self):
        for k in (0,1,10,500):
            a=hidden_negative_witness(k)
            self.assertEqual(a['negative_coordinate'],k+1)
            self.assertFalse(a['full_Weil_source'])
            self.assertEqual(a['negative_Rayleigh'],-1)

    def test_false_source_is_rejected(self):
        for x in (1.0,True,Q(1,2),"2"):
            with self.assertRaises(ZenoError):true_carlemann_sample(x)
        with self.assertRaises(ZenoError):source_discrete_Carleman_commutator(1)
        with self.assertRaises(ZenoError):log2_enclosure(0)
        with self.assertRaises(ZenoError):source_boundary_certificate(Q(7,10),0)

class GraphContracts(unittest.TestCase):
    def test_explicit_shape_catalog(self):
        edges=model_shape_graph()
        self.assertGreaterEqual(len(edges),13)
        self.assertTrue(all(edge.proof_family and edge.status for edge in edges))
        self.assertIn('UNVERIFIED',{e.status for e in edges})
        self.assertIn('REFUTED',{e.status for e in edges})
        self.assertIn('CLASSICAL',{e.status for e in edges})

    def test_proved_ambient_reachability(self):
        z=model_proof_path('source_dilations','boundary_leakage')
        self.assertEqual(z['status'],'PROVED_WITH_DECLARED_PREMISES')
        self.assertIn('a>=log2',z['premises'])

    def test_RH_gate_blocked(self):
        self.assertEqual(model_proof_path('prime_Euler_source','global_PSD')['status'],'UNVERIFIED_OR_BLOCKED')
        self.assertEqual(model_proof_path('boundary_leakage','global_PSD')['status'],'UNVERIFIED_OR_BLOCKED')
        self.assertEqual(model_proof_path('prime_Euler_source','global_PSD',assumptions=('true source all-test lower bound',))['status'],'UNVERIFIED_OR_BLOCKED')

    def test_completion_does_not_auto_actualize(self):
        self.assertEqual(model_proof_path('finite_succ','completed_model')['status'],'PROVED_WITH_DECLARED_PREMISES')
        self.assertEqual(model_proof_path('finite_succ','original_carrier_actualized')['status'],'UNVERIFIED_OR_BLOCKED')

    def test_rejects_fabricated_status(self):
        with self.assertRaises(ZenoError):LawEdge('a','b','law','CERTIFIED','paper',())

    def test_exact_receipt_has_no_proof_of_RH(self):
        from observational_succ.zeno_ambient_weil import verdict_receipt
        a=verdict_receipt()
        self.assertFalse(a['RH_PROVED'])
        self.assertFalse(a['PHYSICAL_ACTUALIZATION'])
        self.assertEqual(a['boundary']['strict_norm_lower'],'11/40')
        self.assertEqual(a['true_prime_power_matrix']['first_boundary_entry'],'2/5')
        self.assertEqual(a['graph']['RH_reachable'],'UNVERIFIED_OR_BLOCKED')

if __name__=='__main__':unittest.main()

class ZenoMorphismControls(unittest.TestCase):
    def test_rational_pole_has_no_continuous_real_extension(self):
        from observational_succ.zeno_ambient_weil import zeno_rational_pole
        for n in range(1,51):
            t=zeno_rational_pole(n)
            self.assertLess(t['rational_pole_value'],0)
            self.assertGreater(-t['rational_pole_value'],t['absolute_value_strictly_greater_than'])
            self.assertTrue(t['no_continuous_extension_to_R'])
        with self.assertRaises(ZenoError):zeno_rational_pole(0)

    def test_lipschitz_transport_has_exact_error(self):
        from observational_succ.zeno_ambient_weil import lipschitz_zeno_transport
        for a,b in ((0,0),(Q(7,3),Q(-2)),(-4,11),(Q(1,13),Q(-1,7))):
            for n in (0,1,2,5,11,50):
                r=lipschitz_zeno_transport(n,a,b)
                self.assertEqual(abs(r['finite_value']-r['completed_value']),r['exact_error'])
                self.assertEqual(r['Lipschitz_constant'],abs(Q(a)))
                self.assertFalse(r['physical_actualization_claimed'])
        with self.assertRaises(ZenoError):lipschitz_zeno_transport(2,0.5,1)

    def test_incomplete_arrow_zeno_graph_is_closed(self):
        from observational_succ.zeno_ambient_weil import model_proof_path
        self.assertEqual(model_proof_path('lipschitz_arrow','completion_transport')['status'],'PROVED_WITH_DECLARED_PREMISES')
        self.assertEqual(model_proof_path('pointwise_arrow','completion_transport')['status'],'UNVERIFIED_OR_BLOCKED')

class SourcePoleZeno(unittest.TestCase):
    def test_exact_odd_pole_positive_tail_bounds(self):
        from observational_succ.zeno_ambient_weil import odd_pole_sharp_H1_bounds
        from decimal import Decimal,localcontext
        with localcontext() as ctx:
            ctx.prec=85
            for a in (Q(1,8),Q(1,4),Q(1,2),Q(1),Q(3,2),Q(2)):
                s=odd_pole_sharp_H1_bounds(a,11)
                x=Decimal(a.numerator)/Decimal(a.denominator)
                sinh=(x.exp()-(-x).exp())/2
                cosh=(x.exp()+(-x).exp())/2
                direct=4*(x+sinh)-16*(cosh-1)/x
                lo=s['odd_pole_dual_norm_squared_lower']
                hi=s['odd_pole_dual_norm_squared_upper']
                l=Decimal(lo.numerator)/Decimal(lo.denominator)
                h=Decimal(hi.numerator)/Decimal(hi.denominator)
                self.assertLess(l,direct)
                self.assertGreater(h,direct)
                self.assertEqual(s['negative_rank_one_form_H1_budget_upper'],2*hi)
        with self.assertRaises(ZenoError):odd_pole_sharp_H1_bounds(Q(0))
        with self.assertRaises(ZenoError):odd_pole_sharp_H1_bounds(Q(3))

    def test_first_odd_moment_produces_ninth_order_suppression(self):
        from observational_succ.zeno_ambient_weil import odd_pole_first_moment_null_bound,odd_pole_sharp_H1_bounds
        for a in (Q(1,10),Q(1,4),Q(1,2),Q(1)):
            m=odd_pole_first_moment_null_bound(a)
            raw=odd_pole_sharp_H1_bounds(a,12)
            self.assertGreater(raw['negative_rank_one_form_H1_budget_upper'],m['negative_odd_pole_H1_bound'])
            self.assertEqual(m['codimension'],1)
            self.assertFalse(m['complete_Weil_sign_proved'])
        self.assertLess(odd_pole_first_moment_null_bound(Q(1,2))['negative_odd_pole_H1_bound'],Q(1,1000000))
        with self.assertRaises(ZenoError):odd_pole_first_moment_null_bound(Q(5,4))

    def test_pole_cancellation_is_source_genuine_not_generic_Gram(self):
        from observational_succ.zeno_ambient_weil import model_proof_path
        self.assertEqual(model_proof_path('moment_null_test','negative_pole_budget')['status'],
                         'PROVED_WITH_DECLARED_PREMISES')
        self.assertEqual(model_proof_path('moment_null_test','global_PSD')['status'],
                         'UNVERIFIED_OR_BLOCKED')

class ZenoPluralityAndStadium(unittest.TestCase):
    def test_harmonic_increments_vanish_without_summable_tail(self):
        from observational_succ.zeno_ambient_weil import harmonic_nonzeno_block
        for k in range(12):
            v=harmonic_nonzeno_block(k)
            self.assertGreaterEqual(v['sum'],v['lower'])
            self.assertEqual(v['finite_N'],1<<k)
            self.assertFalse(v['series_converges'])
        with self.assertRaises(ZenoError):harmonic_nonzeno_block(13)

    def test_stadium_frame_keeps_relative_displacement_and_time(self):
        from observational_succ.zeno_ambient_weil import stadium_frame_demo
        for v,t in ((Q(1),Q(1)),(Q(3,2),Q(2,3)),(Q(7,5),Q(0))):
            r=stadium_frame_demo(v,t)
            self.assertEqual(r['A_position']-r['B_position'],2*v*t)
            self.assertEqual(r['relative_speed'],2*v)
        with self.assertRaises(ZenoError):stadium_frame_demo(Q(-1),Q(1))

class TrueSourceParity(unittest.TestCase):
    def test_even_odd_reflection_exact_original_C0_grid(self):
        from observational_succ.zeno_ambient_weil import source_sampled_parity_poles
        for n in (3,5,7,9,13):
            r=source_sampled_parity_poles(n)
            self.assertEqual(r['odd_even_Gamma_cross'],Q(0))
            self.assertGreater(r['positive_even_pole_example'],0)
            self.assertLess(r['negative_odd_pole_example'],0)
            self.assertEqual(r['cosh'][n//2],1)
            self.assertEqual(r['sinh'][n//2],0)
            self.assertTrue(r['total_Weil_Q_signed'])
            self.assertFalse(r['global_sign_proved'])

    def test_parity_source_wrong_shape_rejected(self):
        from observational_succ.zeno_ambient_weil import source_sampled_parity_poles
        for N in (2,4,10,32,True,0):
            with self.assertRaises(ZenoError):source_sampled_parity_poles(N)

class DiscreteStrongNormSource(unittest.TestCase):
    def test_centred_discrete_true_source_escape(self):
        from observational_succ.zeno_ambient_weil import centered_discrete_zeno_commutator
        from itertools import pairwise
        profiles=[centered_discrete_zeno_commutator(r) for r in range(1,16)]
        self.assertTrue(all(p['norm_lower_for_all_radii']==Q(2,5) for p in profiles))
        self.assertTrue(all(p['central_vector_commutator_norm']<p['central_vector_decay_upper'] for p in profiles))
        self.assertTrue(all(a['central_vector_commutator_norm']>b['central_vector_commutator_norm'] for a,b in pairwise(profiles)))
        self.assertTrue(all(p['strong_limit_on_fixed_vectors_zero'] for p in profiles))
        self.assertTrue(all(not p['operator_norm_limit_zero'] for p in profiles))

    def test_discrete_exact_independent_centered_k_index(self):
        from observational_succ.zeno_ambient_weil import centered_discrete_zeno_commutator
        for r in range(1,16):
            p=centered_discrete_zeno_commutator(r)
            independent=Q(2**(r+1),2**(2*r+2)+1)
            self.assertEqual(p['central_vector_commutator_norm'],independent)
            self.assertLess(independent,Q(1,2**(r+1)))
        for r in (0,16,False,1.0):
            with self.assertRaises(ZenoError): centered_discrete_zeno_commutator(r)

class PrimeFamilyZeno(unittest.TestCase):
    def test_true_prime_arctanh_log_enclosures(self):
        from observational_succ.zeno_ambient_weil import prime_log_enclosure
        from decimal import localcontext,Decimal
        with localcontext() as ctx:
            ctx.prec=90
            for p in (2,3,5,7,11,13,17,31,97):
                lo,hi=prime_log_enclosure(p,20)
                real=Decimal(p).ln()
                self.assertLess(Decimal(lo.numerator)/Decimal(lo.denominator),real)
                self.assertGreater(Decimal(hi.numerator)/Decimal(hi.denominator),real)
                self.assertGreater(lo,0)
        for fake in (1,4,6,9,21,False,2.0):
            with self.assertRaises(ZenoError):prime_log_enclosure(fake)

    def test_source_prime_boundary_generalization(self):
        from observational_succ.zeno_ambient_weil import primitive_prime_boundary_certificate
        for p in (2,3,5,7,11,13):
            d=primitive_prime_boundary_certificate(p,Q(4))
            self.assertEqual(d['prime'],p)
            self.assertGreater(d['commutator_norm_lower'],0)
            self.assertFalse(d['operator_norm_limit_zero'])
            self.assertTrue(d['centered_strong_limit_zero'])
            self.assertFalse(d['Weil_positive_proved'])
            if p==2:
                self.assertEqual(d['commutator_norm_lower'],Q(2,5)*d['logp_lower'])
        with self.assertRaises(ZenoError):primitive_prime_boundary_certificate(6,Q(100))
        with self.assertRaises(ZenoError):primitive_prime_boundary_certificate(3,Q(1))
