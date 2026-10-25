"""Exact Gaussian Gram/vdc calibration and source-error adversarial controls."""
import unittest
from fractions import Fraction as Q
from itertools import product
from math import comb

from observational_succ.harmonic_mirror_succ import harmonic
from observational_succ.pi_harmonic_lag import (
    mixture_weights,lag_kernel,gaussian_correlations,exact_vdc_mixture,
    harmonic_source_error_bound,harmonic_exact_source_error_sum,
    conditional_bbp_fourier_upper,integer_log_16,critical_harmonic_lag_schedule,
    naive_signed_harmonic_symbol_pi,alternating_spectral_symbol_pi,
    last_lag_weight_ratio,
)


class HarmonicLagTests(unittest.TestCase):
    def test_weights_normalized(self):
        for k in range(1,26):
            for beta in (0,1,2,3):
                q=mixture_weights(k,beta)
                self.assertEqual(sum(q),1)
                self.assertTrue(all(v>0 for v in q))
                self.assertEqual(q[-1]/q[0],Q(1,k**beta))

    def test_coefficients_by_independent_block_expansion(self):
        for K in range(1,26):
            weights=lag_kernel(K)
            q=mixture_weights(K)
            for lag,c in enumerate(weights):
                direct=sum((q[L-1]*Q(max(0,L-lag),L*L)
                            for L in range(1,K+1)),Q())
                self.assertEqual(c,direct)
            self.assertEqual(weights[0],sum((Q(1,j*j) for j in range(1,K+1)),Q())/harmonic(K))
            self.assertEqual(weights[0]+2*sum(weights[1:]),1)

    def test_spectral_kernel_at_pi_via_independent_dirichlet_squares(self):
        for K in range(1,40):
            w=lag_kernel(K)
            kernel=w[0]+2*sum(((-1)**k*w[k] for k in range(1,K)),Q())
            direct=sum((Q(1,j**3) for j in range(1,K+1,2)),Q())/harmonic(K)
            self.assertEqual(kernel,direct)
            self.assertEqual(alternating_spectral_symbol_pi(K),direct)
            self.assertGreater(kernel,0)

    def test_naive_harmonic_lag_kernel_is_not_positive(self):
        self.assertEqual(naive_signed_harmonic_symbol_pi(4),Q(-1,6))
        self.assertLess(naive_signed_harmonic_symbol_pi(8),0)

    def test_last_lag_exact_gain_over_fixed_fejer(self):
        for K in range(2,40):
            self.assertEqual(last_lag_weight_ratio(K),Q(1,K)/harmonic(K))
            self.assertLess(last_lag_weight_ratio(K),1)

    def test_positive_square_energy_all_4_root_words(self):
        roots=((1,0),(-1,0),(0,1),(0,-1))
        num=0
        for N in range(1,7):
            for w in product(roots,repeat=N):
                for K in range(1,N+1):
                    lhs,E,rhs=exact_vdc_mixture(w,K)
                    self.assertTrue(Q(0)<=E and lhs<=rhs)
                    num+=1
        self.assertGreater(num,20000)

    def test_positive_mixture_not_stronger_than_optimal_constituent(self):
        # A convex mixture of exact Fejer block energies cannot be less
        # than the minimum individual constituent at the same data.
        vals=tuple(((-1)**i,0) for i in range(40))
        N=len(vals);K=10
        es=[]
        for L in range(1,K+1):
            _,e,_=exact_vdc_mixture(vals,L,0) if L==1 else (Q(),Q(),Q())
            corr=gaussian_correlations(vals,L)
            e=(Q(corr[0],N*L)+sum((Q(2*(L-k),N*L*L)*corr[k]
                                 for k in range(1,L)),Q()))
            es.append(e)
        _,mixture_energy,_=exact_vdc_mixture(vals,K,1)
        self.assertGreaterEqual(mixture_energy,min(es))
        self.assertLessEqual(mixture_energy,max(es))
        self.assertGreater(mixture_energy,min(es))

    def test_general_rational_gaussians_and_beta_exponents(self):
        arrays=( ((Q(1,2),0),(Q(-1,3),Q(2,5)),(0,Q(1,11))),
                ((0,0),(Q(2,3),Q(-7,8)),(0,0)),
                ((7,-11),(-9,4),(0,0),(Q(-1,7),Q(8,13))) )
        for arr in arrays:
            for K in range(1,len(arr)+1):
                for beta in (0,1,2,3):
                    lhs,E,upper=exact_vdc_mixture(arr,K,beta)
                    self.assertLessEqual(lhs,upper)
                    self.assertGreaterEqual(E,0)

    def test_positive_kernel_does_not_imply_mean_cancellation(self):
        arr=tuple((1,0) for _ in range(20))
        for K in range(1,21):
            lhs,E,upper=exact_vdc_mixture(arr,K)
            self.assertEqual(lhs,1)
            self.assertGreaterEqual(upper,1)
            self.assertGreaterEqual(E,Q(1,2))

    def test_periodic_zero_mean_is_not_same_as_normality(self):
        arr=tuple(((-1)**n,0) for n in range(20))
        for K in (2,3,4,8,16,20):
            lhs,E,rhs=exact_vdc_mixture(arr,K)
            self.assertEqual(lhs,0)
            self.assertGreater(E,0)
            self.assertGreaterEqual(rhs,0)

    def test_diagonal_critical_beta_one_vs_two(self):
        for K in (16,64,128):
            d1=lag_kernel(K,1)[0]
            d2=lag_kernel(K,2)[0]
            self.assertGreater(d2,d1)
        self.assertLess(lag_kernel(128,1)[0],Q(1,2))
        self.assertGreater(lag_kernel(128,2)[0],Q(7,10))

    def test_authentic_source_error_weighted_exact_vs_coarse(self):
        for N,K in ((32,3),(64,4),(128,6),(256,8),(512,8),(1024,10)):
            for h in (-3,1,2):
                fine=harmonic_exact_source_error_sum(N,K,h)
                coarse=harmonic_source_error_bound(N,K,h)
                self.assertGreater(fine,0)
                self.assertLess(fine,coarse)

    def test_conditioned_formula_trivial_bounds_cannot_prove_normality(self):
        for N,K in ((30,3),(64,5),(128,6)):
            upper=conditional_bbp_fourier_upper(N,K,1,tuple(Q(N) for _ in range(K-1)))
            self.assertGreaterEqual(upper,1)
            # A fictitious unproved zero bound could yield a smaller RHS;
            # caller MUST authenticate signed special frequency estimates.
            false_bound=conditional_bbp_fourier_upper(N,K,1,tuple(Q() for _ in range(K-1)))
            self.assertLess(false_bound,upper)

    def test_integer_cutoff_exact_resource_budget(self):
        for b in (2,3,4,8,16,32,64,256):
            N=16**b
            K=critical_harmonic_lag_schedule(N)
            self.assertGreaterEqual(K,b)
            self.assertLessEqual(16**K, N*b**3)
            self.assertLessEqual(K,N)
            self.assertLessEqual(16**K,Q(N)*K**3*harmonic(K))

    def test_no_float_in_integer_schedule(self):
        for x in (256,1024,4096,65536,16**8,16**32):
            k=critical_harmonic_lag_schedule(x)
            self.assertLessEqual(16**integer_log_16(x),x)
            self.assertGreater(16**(integer_log_16(x)+1),x)
            self.assertLessEqual(k,x)

    def test_reject_invalid_inputs(self):
        bad=[(mixture_weights,(0,)),(mixture_weights,(2,-1)),
             (lag_kernel,(-1,)),(naive_signed_harmonic_symbol_pi,(1,)),
             (last_lag_weight_ratio,(1,)),
             (harmonic_source_error_bound,(2,3,1)),
             (harmonic_source_error_bound,(4,2,0)),
             (critical_harmonic_lag_schedule,(255,)),
             (gaussian_correlations,(((1,0),(2,0)),3)),
             (exact_vdc_mixture,(((1,0),),2))]
        for f,a in bad:
            with self.assertRaises(ValueError):f(*a)

if __name__=="__main__":unittest.main()
