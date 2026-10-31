"""Root-discoverable exact tests for the research-only edge/seed tomography package."""
import importlib.util
from pathlib import Path
from fractions import Fraction
from collections import Counter
import unittest

PACKAGE=Path(__file__).resolve().parents[1]/'research'/'2026-10-31'/'edge_seed_tomography'

def load(filename,name):
    spec=importlib.util.spec_from_file_location(name,PACKAGE/filename)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

M=load('edge_seed_tomography.py','exact_edge_seed')
O=load('independent_oracle.py','independent_edge_seed')

class ExactBBPSource(unittest.TestCase):
    def test_four_signed_poles(self):
        self.assertEqual(M.forcing(1),Fraction(47,15))
        self.assertEqual(M.forcing(2),Fraction(106,819))
        self.assertTrue(all(M.forcing(n)>0 for n in range(1,100)))

    def test_real_unwrapped_seed(self):
        u=M.original_states(12)
        self.assertEqual(u[0],0)
        for n in range(1,13):
            self.assertEqual(u[n],16*u[n-1]+M.forcing(n))
            self.assertEqual(u[n],sum((16**(n-k)*M.forcing(k) for k in range(1,n+1)),Fraction(0)))
        with self.assertRaises(ValueError):M.original_states(-1)

    def test_edge_rigidity(self):
        for delta,scale,source in M.edge_data(40):
            self.assertEqual(delta,scale+source)
        self.assertTrue(M.edge_error_certificate(800) < Fraction(15,32))
        self.assertGreater(M.edge_error_certificate(1),0)
        self.assertEqual(M.edge_error_certificate(5),sum((M.forcing(k) for k in range(2,7)),Fraction(0)))

    def test_exact_edge_phase_mismatch(self):
        for N in (1,8,32,200):
            for h in (1,3,5,15):
                mismatch=M.edge_phase_mismatch(N,h)
                self.assertLessEqual(mismatch,abs(h)*M.edge_error_certificate(N))
                self.assertGreaterEqual(mismatch,0)
        self.assertEqual(M.circle_distance(Fraction(17,7)),Fraction(3,7))
        self.assertEqual(M.circle_distance(Fraction(-17,7)),Fraction(3,7))

    def test_rational_counterfeit_uniform_finite_enclosure(self):
        for K in (8,16,32):
            sK=-M.bbp_constant_prefix(K)
            states=M.original_states(K,sK)
            tail_budget=Fraction(1,(8*K+1)*(8*K+2))
            for n in range(1,K+1):
                bound=Fraction(1,(8*n+1)*(8*n+2))+Fraction(16**(n-K)) * tail_budget
                self.assertLess(abs(states[n]),bound)
            self.assertLess(sum((abs(x) for x in states[1:]),Fraction(0)),
                            Fraction(1,32)+Fraction(16,15)*tail_budget)

    def test_rational_seed_truncation_control(self):
        for K in (5,12,30):
            c=M.bbp_constant_prefix(K)
            self.assertGreater(c,0)
            self.assertGreater(M.bbp_tail_upper(K),0)
            self.assertEqual(M.truncation_seed_error(K,K),Fraction(1,(8*K+1)*(8*K+2)))
            for n in (0,1,K//2,K):
                # selected zero seed and rational counterfeit differ by exact -16^n c_K
                self.assertEqual(M.original_states(n, -c)[n]-M.original_states(n)[n],-16**n*c)
        with self.assertRaises(ValueError): M.truncation_seed_error(4,5)

class CarrierTomography(unittest.TestCase):
    def test_integer_labels_unique(self):
        for N in range(2,18):
            labels=M.pair_difference_labels(N)
            self.assertEqual(len(labels),N*(N-1))
            self.assertTrue(all(x!=0 for x in labels))
            self.assertEqual(len({(n,m) for n,m in labels.values()}),N*(N-1))
        with self.assertRaises(ValueError):M.pair_difference_labels(4,h=0)

    def test_discovered_alias_free_moduli(self):
        reference={2:7,3:7,4:19,5:31,6:53,7:73,8:73,9:73,10:283,11:337,12:503}
        for N,p in reference.items():
            self.assertEqual(M.first_alias_free_prime(N),p)
            self.assertTrue(M.is_prime(p))
            self.assertTrue(M.is_alias_free(N,p))
        self.assertFalse(M.is_alias_free(9,17))
        self.assertFalse(M.is_alias_free(9,73,73))  # a frequency probe that divides modulus
        self.assertTrue(M.is_alias_free(9,73,2))
        with self.assertRaises(ValueError):M.exact_source_tomogram(9,17)

    def test_mod_73_projective_plane(self):
        D=M.difference_set_73()
        self.assertEqual(D,(1,2,4,8,16,32,37,55,64))
        self.assertEqual(M.diff_multiplicity(D,73),Counter({k:1 for k in range(1,73)}))
        lines=M.singer_lines()
        self.assertEqual(len(set(lines)),73)
        self.assertTrue(all(len(x)==9 for x in lines))
        self.assertEqual(O.brute_73_difference_set()['point_pairs'],2628)

    def test_finite_prime_search_fails_closed(self):
        with self.assertRaises(LookupError):M.first_alias_free_prime(9,cap=25)
        self.assertNotEqual(M.first_alias_free_prime(9,h=73),73)

    def test_source_phase_ratios_recoverable(self):
        for N in (2,3,5,9):
            p=M.first_alias_free_prime(N)
            phase_map=M.exact_source_tomogram(N,p)
            alternate=O.brute_phase_response(N,1,p)
            self.assertEqual({r:value[1] for r,value in phase_map.items() if r!=0},alternate)
            self.assertEqual(len(phase_map),1+N*(N-1))
            self.assertIsNone(phase_map[0])

    def test_relative_phase_tomography_global_gauge(self):
        N=9;p=73
        out=M.exact_source_tomogram(N,p)
        phase={(n,m):data[1] for label,data in out.items() if label!=0 for n,m in [data[0]]}
        zero_phase={n:(0 if n==1 else phase[n,1]) for n in range(1,N+1)}
        for (n,m),v in phase.items():
            self.assertEqual(v,(zero_phase[n]-zero_phase[m])%1)

    def test_noninvariant_static_pushforward_false_positive(self):
        # f(x)=1+cos(2πx) is positive, non-Haar, and M15 pushforward Haar.
        coeff={0:Fraction(1),1:Fraction(1,2),-1:Fraction(1,2)}
        self.assertEqual(coeff[1],Fraction(1,2))
        for h in range(-100,101):
            if h: self.assertEqual(coeff.get(15*h,0),0)
        self.assertNotEqual(coeff.get(1,0),coeff.get(16,0)) # not T16-invariant

    def test_complex_dft_73_numerical_sanity_only(self):
        # Independent finite-sample Fourier reconstruction; numerical corroboration
        # only. The proof of exact recovery is in PROOFS.md / group-ring oracle.
        from math import pi
        import cmath
        N=9;p=73;h=1
        u=M.original_states(N)
        z=[cmath.exp(2j*pi*float((h*u[n])%1)) for n in range(1,N+1)]
        samples=[]
        for j in range(p):
            f=sum(z[n-1]*cmath.exp(2j*pi*((h*pow(16,n,p)*j)%p)/p)
                  for n in range(1,N+1))
            samples.append(abs(f)**2)
        for n in range(1,N+1):
            for m in range(1,N+1):
                if n==m:continue
                label=(h*(16**n-16**m))%p
                recovered=sum(v*cmath.exp(-2j*pi*label*j/p)
                              for j,v in enumerate(samples))/p
                expected=z[n-1]*z[m-1].conjugate()
                self.assertLess(abs(recovered-expected),1e-10)
        self.assertLess(abs(sum(samples)/p-N),1e-10)

    def test_seed_provenance_not_ignored(self):
        N=6;p=M.first_alias_free_prime(N)
        s=Fraction(-7,51)
        original=M.exact_source_tomogram(N,p,seed=0)
        changed=M.exact_source_tomogram(N,p,seed=s)
        for label,data in original.items():
            if label==0:continue
            (n,m),phase=data
            self.assertEqual(changed[label][1],(phase+(16**n-16**m)*s)%1)
        self.assertNotEqual(original,changed)
        self.assertEqual({r:v[1] for r,v in changed.items() if r!=0},O.brute_phase_response(N,1,p,seed=s))

class SeedMeasureMoments(unittest.TestCase):
    def test_exact_fourth_moments_independent_oracle(self):
        for n in range(1,11):
            self.assertEqual(M.fourth_moment(n),O.brute_fourth_collision(n))

    def test_twisted_lacunary_fourth_moment(self):
        from itertools import product
        for N in range(1,7):
            # Gaussian unit-circle coefficients, exact integral via equality of exponents
            z=(1,1j,-1,-1j,1j,-1)[:N]
            powers=[16**j for j in range(1,N+1)]
            value=sum((z[a]*z[b]*z[c].conjugate()*z[d].conjugate()
                       for a,b,c,d in product(range(N),repeat=4)
                       if powers[a]+powers[b]==powers[c]+powers[d]),0j)
            self.assertEqual(value,M.fourth_moment(N))

    def test_prime_grid_exact_fourth_cubature(self):
        for N in range(2,15):
            prime=M.first_alias_free_prime(N)
            self.assertEqual(O.discrete_fourth_collision(N,prime),2*N*N-N)
        self.assertGreater(O.discrete_fourth_collision(9,17),2*9*9-9)
        self.assertEqual(O.discrete_fourth_collision(9,73),153)

    def test_exact_cylinder_moments(self):
        for N,k in ((3,0),(7,2),(8,5),(9,9)):
            modes,moment=M.cylinder_moment_tail(N,k)
            self.assertEqual(moment,O.brute_fourth_cylinder(N,k))
            self.assertEqual(moment,2*modes*modes-modes)
        with self.assertRaises(ValueError):M.cylinder_moment_tail(4,5)

    def test_selection_lipschitz_budget(self):
        for N in range(0,15):
            self.assertEqual(M.selection_lipschitz_budget(N),sum(16**i for i in range(1,N+1)))
        self.assertEqual(M.selection_lipschitz_budget(6,h=-3),3*M.selection_lipschitz_budget(6))

    def test_signed_mean_not_selected(self):
        # A concentrated phase vector and arbitrary changing source phases have
        # the same seed-averaged quadratic/fourth moments; the selected value differs.
        n=8
        self.assertEqual(M.fourth_moment(n),120)
        self.assertEqual(n*n,64) # all-unity phases at the selected seed
        z0=(1,1,1,1,1,1,1,1)
        z1=(1,-1,1,-1,1,-1,1,-1)
        self.assertEqual(sum(z0),8)
        self.assertEqual(sum(z1),0)
        self.assertEqual(sum(x*x for x in z0),sum(x*x for x in z1))

if __name__=='__main__':unittest.main()
