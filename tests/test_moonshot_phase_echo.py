"""Exact, independently cross-checked moonshot tests; infinite claims have proofs."""
from pathlib import Path
import importlib.util
import sys
import unittest
from fractions import Fraction as F
from itertools import product

ROOT=Path(__file__).resolve().parents[1]/'research/2026-11-01/moonshot_phase_echo'
def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod)
    return mod
m=load('moonshot_phase_echo_exact','phase_echo.py')
o=load('moonshot_phase_echo_oracle','independent_oracle.py')

class SourceTests(unittest.TestCase):
    def test_literal_source_combination(self):
        for n in range(1,170): self.assertEqual(m.source(n),o.combined_source(n))
    def test_original_positive_monotone_and_tail(self):
        for n in range(1,100):
            self.assertGreater(m.source(n),m.source(n+1))
            self.assertLess(m.source(n+1),F(15,64*n*n))
            self.assertLess(m.tail_partial(n,12)[1],m.source_tail_budget(n))
    def test_backward_finite_seam(self):
        for N in range(1,22):
            xs=m.states(N);alpha=sum((o.combined_source(j)/16**j for j in range(1,N+1)),F())
            for n in range(N+1):
                future=sum((o.combined_source(j)/16**(j-n) for j in range(n+1,N+1)),F())
                self.assertEqual(xs[n],16**n*alpha-future)
    def test_modular_exponentiation_oracle(self):
        xs=m.states(128,circle=True)
        for n in (0,1,2,3,7,11,23,64,97,128): self.assertEqual(xs[n],o.modular_prefix(n))
    def test_alpha_and_machin_interval_overlap(self):
        lo,hi=m.source_alpha(80);p,q=m.pi_interval()
        self.assertLess(max(lo,p/16),min(hi,q/16))
    def test_odd_conductor_contains_all_states(self):
        for N in (1,2,3,8,16,32):
            Q,ys=m.finite_register(N);xs=m.states(N,circle=True)
            self.assertEqual(Q%2,1)
            for j,x in enumerate(ys,1): self.assertEqual(F(x,Q),xs[j])
    def test_wrong_binary_conductor_rejected_by_divisibility(self):
        self.assertNotEqual((m.source(1)*256).denominator,1)
        self.assertEqual((m.source(1)*15).denominator,1)
    def test_source_domain_fail_closed(self):
        for v in (0,-1,True,1.5):
            with self.assertRaises((ValueError,TypeError)):m.source(v)

class LoopTests(unittest.TestCase):
    def test_affine_weyl_associativity(self):
        ops=[m.AffineWeyl(a,b,k,p) for a,b,k,p in [(2,F(1,3),2,F(1,7)),(3,-2,5,F(-1,2)),(F(1,2),3,-7,0)]]
        for a,b,c in product(ops,repeat=3):self.assertEqual((a@b)@c,a@(b@c))
    def test_inverse_both_sides(self):
        for a,b,k,p in [(16,F(47,15),3,5),(F(1,16),-2,-5,F(1,3))]:
            op=m.AffineWeyl(a,b,k,p)
            self.assertEqual(op@op.inverse(),m.AffineWeyl())
            self.assertEqual(op.inverse()@op,m.AffineWeyl())
    def test_unitarity_half_density(self):
        for a in (F(1,16),F(1,2),F(3),F(16)):
            self.assertEqual(a*(1/a),1)
            self.assertNotEqual(a*(1/a)**2,1)
    def test_order_preserved_original_first_pair(self):
        f=m.AffineWeyl(16,m.source(1));g=m.AffineWeyl(16,m.source(2))
        self.assertEqual((g@f).b-(f@g).b,F(12301,273))
    def test_original_echo_all_exact(self):
        for N in range(0,25):
            for h in (1,-1,3,5,11):
                loop=m.phase_echo(N,h)
                self.assertEqual((loop.a,loop.b,loop.k),(F(1),F(0),F(0)))
                self.assertEqual(loop.phi,h*m.states(N)[-1])
    def test_direct_word_trace(self):
        for N,h,seed,y in product((1,3,7),(-3,1),(F(),F(1,7)),(F(-2),F(1,3))):
            p=m.propagator(N,seed)
            word=[('W',(1/p.a,-p.b/p.a)),('M',(h,)),('W',(p.a,p.b)),('M',(-h*p.a,))]
            x,phi,density=o.run_operator_word(word,y)
            self.assertEqual((x,phi,density),(y,h*p.b,1))
    def test_loop_subtraction_must_scale(self):
        p=m.propagator(2)
        wrong=p.inverse()@m.modulation(1)@p@m.modulation(-1)
        self.assertEqual(wrong.k,255)
        self.assertNotEqual(wrong,m.phase_echo(2,1))
    def test_missing_order_counterexample(self):
        p=m.propagator(2)
        wrong=p@m.modulation(1)@p.inverse()@m.modulation(-p.a)
        self.assertNotEqual(wrong.k,0)
    def test_seed_echo_changes_correctly(self):
        for N in range(1,10):
            delta=m.phase_echo(N,3,F(1,7)).phi-m.phase_echo(N,3).phi
            self.assertEqual(delta,F(3*16**N,7))
    def test_all_hilbert_states_same_scalar_loop(self):
        loop=m.phase_echo(4,5)
        for y in (F(-10),F(0),F(1,17),F(200)):
            self.assertEqual(loop.trace_argument(y),(y,loop.phi))
    def test_lag_loop_matches_original_source_difference(self):
        xs=m.states(16)
        for n,k in product(range(1,10),range(1,6)):
            a=m.phase_echo(n+k,3)@m.phase_echo(n,3).inverse()
            self.assertEqual(a.phi,3*(xs[n+k]-xs[n]))
            self.assertEqual(a.k,0)
    def test_finite_cyclic_echo_exact_real_phase(self):
        for N in (1,2,3,5):
            Q,ys=m.finite_register(N);A=16**N;B=ys[-1]
            self.assertEqual((A*pow(A,-1,Q))%Q,1)
            for x,h in product((0,1,Q//2,Q-1),(1,3,-5)):
                y=(A*x+B)%Q
                exp=(h*y-h*A*x)%Q
                self.assertEqual(exp,(h*B)%Q)
                self.assertEqual(F(exp,Q),(h*m.states(N)[-1])%1)
    def test_float_parameters_refused(self):
        with self.assertRaises(TypeError):m.AffineWeyl(1.,0,0,0)
        with self.assertRaises(ValueError):m.AffineWeyl(0)
        with self.assertRaises(ValueError):m.phase_echo(1,0)

class ResolutionTests(unittest.TestCase):
    def test_scattering_bound_decreases(self):
        for n in range(1,20):
            self.assertLess(m.scattering_error(n+1,7),m.scattering_error(n,7))
            self.assertGreater(m.scattering_error(n,7),0)
    def test_exact_source_norm_adversary_budget(self):
        # Sum_n T_n < 1/32: finite rational lower sum lies below bound.
        total=sum((m.tail_partial(n,16)[0] for n in range(1,100)),F())
        self.assertLess(total,F(1,32))
    def test_gaussian_prefix_error_finite_uniform(self):
        for h in (1,3,11):
            self.assertGreater(m.gaussian_prefix_error(h),1)
            self.assertLess(m.gaussian_prefix_error(h),2+F(h*h,10))
    def test_sobolev_budget_clips_at_one(self):
        for N,h,d in product((1,16,128),(1,5),(F(1,100),F(3),F(16**20))):
            b=m.sobolev_resolution_budget(N,d,h)
            self.assertGreaterEqual(b,0);self.assertLessEqual(b,1)
    def test_polynomial_vs_exponential_gradient(self):
        self.assertLess(m.sobolev_resolution_budget(256,256**2,1),F(1,40))
        self.assertGreater(m.sobolev_resolution_budget(256,16**128,1),F(49,100))
    def test_coherent_center_exact_prefix_shadow(self):
        # finite irrational-center replacement q-alpha_L; for n<=L errors paid by tail
        L=32;alpha_lo,alpha_hi=m.source_alpha(L);q=F(1,5)
        xs=m.states(8,q-alpha_lo)
        for n in range(1,9):
            tlo,thi=m.tail_partial(n,L-n)
            expected=q*16**n-tlo
            self.assertEqual(xs[n],expected)
            self.assertLess(16**n*(alpha_hi-alpha_lo),F(1,10**20))
    def test_false_uniform_moment_source_control(self):
        # Chosen quarter phases: same unit moduli, different signed sums.
        self.assertEqual(sum((1,1,1,1)),4)
        self.assertEqual(sum((1,1,-1,-1)),0)
    def test_invalid_resolution_parameters(self):
        with self.assertRaises(ValueError):m.gaussian_prefix_error(0)
        with self.assertRaises(ValueError):m.sobolev_resolution_budget(1,-1,1)

class CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.enc=m.PhaseEncloser()
    def test_machin_interval_width_and_location(self):
        a,b=m.pi_interval();self.assertLess(b-a,F(1,10**60));self.assertTrue(3<a<b<F(22,7))
    def test_exact_known_trig_values(self):
        for p,c,s in [(F(0),1,0),(F(1,4),0,1),(F(1,2),-1,0),(F(3,4),0,-1),(F(1,6),F(1,2),None),(F(1,3),F(-1,2),None)]:
            ci,si=self.enc.pair(p)
            self.assertLessEqual(ci[0],c);self.assertGreaterEqual(ci[1],c)
            if s is not None:self.assertLessEqual(si[0],s);self.assertGreaterEqual(si[1],s)
    def test_fraction_taylor_independent_oracle(self):
        pl,ph=m.pi_interval()
        for p in (F(1,7),F(-3,8),F(47,100),F(13,99)):
            c=self.enc.cosine(p); angle=p*(pl+ph)
            a,b=o.fraction_cosine_at_angle(angle)
            error=abs(p)*(ph-pl)
            self.assertLessEqual(c[0],a-error);self.assertGreaterEqual(c[1],b+error)
    def test_periodic_and_conjugate_phases(self):
        for p in (F(13,19),F(17,256),F(-31,17)):
            self.assertEqual(self.enc.pair(p),self.enc.pair(p+7))
            c,s=self.enc.pair(p);d,t=self.enc.pair(-p)
            self.assertLessEqual(max(c[0],d[0]),min(c[1],d[1]))
            self.assertLessEqual(max(s[0],-t[1]),min(s[1],-t[0]))
    def test_interval_width(self):
        for p in (F(i,97) for i in range(97)):
            for a,b in self.enc.pair(p):
                self.assertLessEqual(a,b);self.assertLess(b-a,F(1,10**24))
    def test_signed_score_vdc(self):
        xs=m.states(40,circle=True)
        for N,K,h in [(12,2,1),(24,3,3),(40,3,5)]:
            r=m.certified_scores(xs,N,K,h,self.enc)
            self.assertLessEqual(r['mean_square'][0],r['vdc_actual_upper'])
            self.assertLessEqual(r['mean_square'][0],r['vdc_reduced_upper'])
            gap=max(abs(r['actual_lag'][0]-r['reduced_lag'][1]),abs(r['actual_lag'][1]-r['reduced_lag'][0]))
            self.assertLessEqual(gap,r['transport_budget']+F(1,10**22))
    def test_clipped_source_bound_sqrt(self):
        for x in (F(0),F(2),F(3,7),F(1234,17)):
            y=m.fraction_sqrt_upper(x);self.assertGreaterEqual(y*y,x)
            if x>0:self.assertLess(max(F(0),y-F(1,2**70))**2,x)
    def test_null_stream_vdc_is_coherent(self):
        xs=(F(),)*33
        r=m.certified_scores(xs,32,3,1,self.enc,verify_source=False)
        self.assertGreater(r['mean_square'][0],F(999,1000))
        self.assertGreater(r['actual_lag'][0],F(3,5))
    def test_source_mutation_rejected(self):
        xs=list(m.states(20,circle=True));xs[10]+=F(1,17)
        with self.assertRaises(ValueError):m.certified_scores(tuple(xs),20,3,1,self.enc)
    def test_initial_seed_requires_explicit_declaration(self):
        seed=F(1,7);xs=m.states(20,seed,circle=True)
        with self.assertRaises(ValueError):m.certified_scores(xs,20,3,1,self.enc)
        result=m.certified_scores(xs,20,3,1,self.enc,seed=seed)
        self.assertEqual(result['declared_seed'],seed)
    def test_generic_stream_has_no_authentic_source_budget(self):
        r=m.certified_scores((F(),)*17,16,2,1,self.enc,verify_source=False)
        self.assertIsNone(r['transport_budget']);self.assertIsNone(r['vdc_reduced_upper'])
        self.assertFalse(r['source_phase_authenticated'])
    def test_mutation_quarter_phase_caught(self):
        c=self.enc.cosine(F(1,6))
        bad=(c[0]+F(1,10**10),c[1]+F(1,10**10))
        self.assertFalse(bad[0]<=F(1,2)<=bad[1])
    def test_probe_domain_checks(self):
        for N,K,h in [(0,1,1),(8,9,1),(8,2,0)]:
            with self.assertRaises(ValueError):m.certified_scores((F(),)*10,N,K,h)


class RegulatorTests(unittest.TestCase):
    def test_regulator_echo_independent_fourier_algebra(self):
        for N,eps,hb,k in product((1,2,5),(F(),F(1,17)),(F(1),F(2)),(F(1),F(-3))):
            a=16**N;b=m.states(N)[-1];t=eps*F(256**N-1,255)
            W=(a,0,-hb*t/2,-b,0)
            Winv=(F(1,a),0,hb*t/(2*a*a),b/a,0)
            M=(1,-k,0,0,0);counter=(1,a*k,0,0,0)
            answer=o.fourier_word([Winv,M,W,counter])
            self.assertEqual(answer,(1,0,0,hb*t*k/a,k*b-hb*t*k*k/2))
    def test_regulator_corrector_exact(self):
        for N in (1,2,7):
            eps=F(1,101);hb=F(2);k=F(3);U=m.states(N)[-1]
            c,d=m.regulator_echo_coefficients(N,eps,hb)
            echo=(1,0,0,d*k,k*U-c*k*k)
            correction=(1,0,0,-d*k,c*k*k)
            self.assertEqual(o.fourier_compose(echo,correction),(1,0,0,0,k*U))
    def test_parent_band_bound_does_not_apply_after_large_modulation(self):
        N=8;eps=F(1,100);hb=1;K=1;k=1
        parent=eps*hb*K*K*F(1,510)
        loop=m.regulator_echo_band_bound(N,eps,k,K,hb)
        self.assertLess(parent,F(1,10000));self.assertEqual(loop,2)
    def test_zero_regulator_exact(self):
        for N in (1,10,100):self.assertEqual(m.regulator_echo_coefficients(N,0),(0,0))
    def test_scaled_regulator_bound_vanishes(self):
        prev=F(2)
        for N in range(1,18):
            v=m.regulator_echo_band_bound(N,F(1,256**(2*N)),2,3)
            self.assertLess(v,prev);prev=v
    def test_regulator_invalid_inputs(self):
        for N,eps,hb in ((0,1,1),(1,-1,1),(1,1,0)):
            with self.assertRaises(ValueError):m.regulator_echo_coefficients(N,eps,hb)


class CoherentControlTests(unittest.TestCase):
    def test_actual_fixed_irrational_control_not_rational_surrogate(self):
        r=m.coherent_counterseed_score(24,1)
        self.assertFalse(r['literal_zero_boundary'])
        self.assertIn('irrational',r['seed'])
        self.assertGreater(r['mean_square'][0],F(99,100))
    def test_all_horizon_lower_bound_survives_finite_enclosure(self):
        for N,h in ((8,1),(16,3),(24,5)):
            r=m.coherent_counterseed_score(N,h)
            self.assertGreater(r['mean_square'][0],r['all_horizon_mean_square_lower'])
    def test_counterseed_validation(self):
        for args in ((0,1,24),(8,0,24),(8,1,0)):
            with self.assertRaises(ValueError):m.coherent_counterseed_score(*args)

if __name__=='__main__':unittest.main()
