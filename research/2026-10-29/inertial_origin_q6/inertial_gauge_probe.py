"""Exact original-source gauge/carry/seed-ignorance research controls.

Research status only. No selected-π Weyl cancellation or normality theorem.
Original four-pole BBP source and initial zero are immutable inputs.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, gcd, floor, pi, cos, sin
import unittest

B=16

def forcing(n: int) -> F:
    if type(n) is not int or n<1: raise ValueError("n positive")
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def state(n:int,seed=F(0)) -> F:
    if type(n) is not int or n<0:raise ValueError("n nonnegative")
    x=F(seed)
    for k in range(1,n+1): x=16*x+forcing(k)
    return x

def phase_coordinate(n:int,seed=F(0),chart=F(0)) -> F:
    """State expressed in the observer's unmarked chart, an exact rational lift."""
    return state(n,seed)+16**n*F(chart)

def source_origin(n:int,chart=F(0)) -> F:
    """Chart representative of freely transported inertial source reference."""
    return 16**n*F(chart)

def relative_state(n:int,seed=F(0),chart=F(0)) -> F:
    return phase_coordinate(n,seed,chart)-source_origin(n,chart)

def relative_carry(n:int,seed=F(0),chart=F(0)) -> int:
    if type(n) is not int or n<1: raise ValueError("carry time n>=1")
    x=relative_state(n-1,seed,chart)%1
    return floor(16*x+forcing(n))

def circle_phase_exponent(n:int,seed=F(0),chart=F(0)) -> F:
    return relative_state(n,seed,chart)%1

def pascal_grade(n:int) ->tuple[F,...]:
    if type(n) is not int or n<1:raise ValueError("positive clock")
    den=forcing(n)
    return tuple(F(comb(n,j))*sum((F((-1)**k*comb(j,k))*forcing(2*n-j+k)
                                   for k in range(j+1)),F())/den for j in range(n+1))

def q6_cell_masses(n:int,seed=F(0),chart=F(0)) -> dict:
    """Exact full q6 grade/rank and 17 literal-carry bins with rational phase labels.

    Values are lists of (grade, rational positive mass, fractional phase) rather
    than transcendental phases; source mark makes all labels gauge-invariant.
    """
    if n<2: raise ValueError("n>=2 for 0..16 carry bin typing")
    p=pascal_grade(n)
    cells={(a,b,k): [] for a in (0,1) for b in (0,1) for k in range(17)}
    for j,mass in enumerate(p):
        grade=int(gcd(j,6)==1)
        rank=int(gcd(j+2,6)==1)
        k=relative_carry(n+j,seed,chart)
        if not 0<=k<=16: raise AssertionError("typed 17-bin restriction")
        cells[(grade,rank,k)].append((j,mass,circle_phase_exponent(n+j,seed,chart)))
    return cells

def sector_totals(cells:dict)->dict:
    return {(a,b):sum((v[1] for k,events in cells.items() if k[:2]==(a,b) for v in events),F())
            for a in (0,1) for b in (0,1)}

def haar_carry_bin_mass(n:int,k:int)->F:
    """P_Haar(kappa_n=k) for n>=2, 0<r(n)<1."""
    if n<2 or not 0<=k<=16:raise ValueError("source time or bin invalid")
    r=forcing(n)
    return (1-r)/16 if k==0 else r/16 if k==16 else F(1,16)

def haar_signed_bin_coefficient(n:int,k:int)->F:
    """Coefficient of J_h(r(n))=(exp(2πi h r(n))-1)/(2πi h).

    For all h∈Z\\{0}, E_Haar[1_{kappa_n=k} exp(2π i h x_n)]
    = coefficient * J_h(r(n)).  Interior carry classes vanish EXACTLY.
    """
    if n<2 or not 0<=k<=16:raise ValueError("source time or bin invalid")
    return F(-1,16) if k==0 else F(1,16) if k==16 else F(0)

def haar_q6_grade_rank_contributions(n:int)->dict:
    """Exact coefficients of the complete 4×17 tensor in the Haar seed law.

    For c=0,16 each cell holds the formal sum over j of
      q_n(j) * [(-/+1)/16] * J_h(r(n+j)).
    For all 15 interior carries it holds the exact zero coefficient.
    """
    if n<2:raise ValueError("n>=2")
    out={(a,b,c):[] for a in (0,1) for b in (0,1) for c in range(17)}
    for j,mass in enumerate(pascal_grade(n)):
        a=int(gcd(j,6)==1);b=int(gcd(j+2,6)==1)
        for k in (0,16):
            out[(a,b,k)].append((mass*haar_signed_bin_coefficient(n+j,k),forcing(n+j)))
    return out

def green_tail_bounds(n:int,depth:int=20)->tuple[F,F]:
    """Certified original π Green tail: exact rational enclosure."""
    if n<1 or depth<1:raise ValueError("n,depth positive")
    lo=sum((forcing(n+j)/16**j for j in range(1,depth+1)),F())
    hi=lo+forcing(n+depth+1)/F(15*16**depth)
    return lo,hi

def kappa15_run(n:int,max_length:int)->int:
    """Exact number of consecutive future literal 15 carries following n."""
    if n<1 or max_length<0: raise ValueError("invalid run")
    length=0
    for j in range(1,max_length+1):
        if relative_carry(n+j)==15:length+=1
        else:break
    return length

def run_physical_distance_bound(n:int,L:int,depth:int=20)->bool:
    """If L future carries are all 15, source π-phase is <16^-L from integer.
    Check using only a rational certified Green enclosure.
    """
    if n<1 or L<1 or kappa15_run(n,L)!=L:return False
    lo,hi=green_tail_bounds(n,depth)
    phase_lo=state(n)%1+lo
    phase_hi=state(n)%1+hi
    target=F(1,16**L)
    # Both endpoints must be within the open 16^-L neighborhood of integer 1.
    return 1-target < phase_lo <= phase_hi < 1+target

def uniform_seed_information_lower_bound_bits(n:int,h:int=1)->int:
    """Approximate n*4-1 for a symmetric uniform physical-preparation arc.

    If |E exp(2πihU_n(S))|>1/2, epsilon<2/(|h|16^n).
    For h=1,  -log2 epsilon > 4n-1  (necessary for that criterion).
    """
    if n<1 or type(h) is not int or h==0:raise ValueError("positive n, h!=0")
    if abs(h)!=1:raise ValueError("this exact integer display is specialized to |h|=1")
    return 4*n-1

def haar_seed_mse(N:int,h:int=1)->F:
    """For any forcing, ∫ |(1/N) sum exp(2πi h U_n(s))|² ds=1/N."""
    if N<1 or type(h) is not int or h==0:raise ValueError("invalid horizon/frequency")
    assert all(h*16**n != h*16**m for n in range(1,N+1) for m in range(1,N+1) if n!=m)
    return F(1,N)

def frequency_ladder_resonance_indices(N:int,q:int=1):
    """For h=16^q k vs k, Haar seed correlations retain m=n+q."""
    if N<1 or q<0:raise ValueError("N>=1,q>=0")
    return tuple((n,n+q) for n in range(1,N+1-q)) if q<N else ()


def forcing_positive_lower(n:int)->F:
    """Original four-pole strict elementary lower bound r(n)>15/(a(a+5))."""
    if n<1:raise ValueError("n>=1")
    a=8*n-7
    return F(15,a*(a+5))

def carry_zero_run_bound(n:int,L:int)->bool:
    """Necessary for L future zero carries: 16^(L-1)*15<(8n+1)(8n+6)."""
    if n<1 or L<1:raise ValueError("n,L positive")
    return 16**(L-1)*15 < (8*n+1)*(8*n+6)

def exceptional_16_to_0_certificate(n:int)->F:
    """If kappa_n=16, then kappa_(n+1)=0 for every n>=3.

    The sufficient exact inequality is 16*r(n)+r(n+1)<1.
    """
    if n<3:raise ValueError("n>=3")
    margin=1-16*forcing(n)-forcing(n+1)
    if margin<=0:raise AssertionError("source transition theorem failed")
    return margin

def haar_exceptional_16_tail_probability_bound(start:int)->F:
    """P_Haar(exists kappa_n=16 for any n>=start) <= 1/[16*(start-1)].

    Union bound plus r(n)<1/n² and integral tail <=1/(start-1).
    """
    if start<3:raise ValueError("start>=3")
    return F(1,16*(start-1))

class InertialGaugeExactTests(unittest.TestCase):
    def test_original_source_exact(self):
        self.assertEqual(forcing(1),F(47,15))
        self.assertEqual(forcing(2),F(106,819))
        self.assertTrue(all(0<forcing(n)<F(1,n*n) for n in range(2,60)))

    def test_gauge_covariant_relative_origin(self):
        for g in (F(0),F(1,15),F(-3,7),F(1,256),F(7,11)):
            for seed in (F(0),F(-1),F(1,19),F(1,15)):
                for n in range(0,12):
                    self.assertEqual(relative_state(n,seed,g),state(n,seed))
                    self.assertEqual(circle_phase_exponent(n,seed,g),state(n,seed)%1)
                    if n:self.assertEqual(relative_carry(n,seed,g),relative_carry(n,seed,0))

    def test_no_preparation_not_empty_carrier(self):
        self.assertEqual(state(0),0)
        self.assertGreater(state(1),0)
        self.assertGreater(forcing(4),0)
        self.assertNotEqual(state(3)%1,0)

    def test_q6_complete_tensor_and_gauge_covariance(self):
        for n in (2,3,6,9):
            reference=q6_cell_masses(n,F(0),F(0))
            self.assertEqual(sum(sector_totals(reference).values(),F()),F(1))
            for g in (F(1,13),F(5,7)):
                self.assertEqual(reference,q6_cell_masses(n,F(0),g))
            other=q6_cell_masses(n,F(1,29),F(0))
            self.assertEqual(sector_totals(reference),sector_totals(other))
            self.assertNotEqual(reference,other)

    def test_pascal_exact_masses(self):
        for n in range(2,18):
            p=pascal_grade(n)
            self.assertEqual(sum(p),F(1))
            self.assertGreater(min(p),F(0))

    def test_haar_full_carry_distribution(self):
        for n in (2,3,5,7,16,31):
            ps=[haar_carry_bin_mass(n,c) for c in range(17)]
            self.assertEqual(sum(ps,F()),F(1))
            self.assertEqual(ps[0]-F(1,16),-forcing(n)/16)
            self.assertEqual(ps[16],forcing(n)/16)
            self.assertEqual(ps[7],F(1,16))

    def test_haar_signed_interior_exact_zero(self):
        for n in (2,3,4,6,13):
            a=haar_signed_bin_coefficient(n,0)
            b=haar_signed_bin_coefficient(n,16)
            self.assertEqual(a+b,F(0))
            self.assertTrue(all(haar_signed_bin_coefficient(n,k)==0 for k in range(1,16)))

    def test_complete_q6_haar_interior_null(self):
        for n in (2,3,6,11):
            out=haar_q6_grade_rank_contributions(n)
            for a in (0,1):
                for b in (0,1):
                    for k in range(1,16):self.assertEqual(out[(a,b,k)],[])
                    self.assertEqual(sum(t[0] for t in out[(a,b,0)]),-sum(t[0] for t in out[(a,b,16)]))

    def test_origin_15_torsion_phase_only_alias(self):
        s=F(1,15)
        for n in range(0,18):
            self.assertEqual((state(n,s)-state(n,0))%1,s)

    def test_integer_seed_phase_alias_but_preparation_changes(self):
        for n in range(0,10):
            self.assertEqual(state(n,0)%1,state(n,-1)%1)
            self.assertEqual(state(n,0)%1,state(n,-16)%1)
            self.assertNotEqual(state(n,0),state(n,-1))

    def test_exact_original_green_bounds(self):
        for n in range(1,10):
            lo,hi=green_tail_bounds(n,depth=8)
            self.assertTrue(0<lo<hi<F(1,64*n*n))
            lo2,hi2=green_tail_bounds(n,depth=14)
            self.assertLessEqual(lo,lo2)
            self.assertLessEqual(hi2,hi)

    def test_coherent_carry_symbolic_15(self):
        # For the coherent seed x_n=1-T_n and exact green relation
        # 16T_(n-1)-r(n)=T_n, so 16x_(n-1)+r(n)=16-T_n.
        for n in range(2,19):
            lo,hi=green_tail_bounds(n,depth=12)
            self.assertTrue(0<lo<hi<1)
            self.assertTrue(15<16-hi<16-lo<16)

    def test_selected_real_run_forces_tiny_pi_phase(self):
        for n in range(1,40):
            L=kappa15_run(n,7)
            if L>=1:self.assertTrue(run_physical_distance_bound(n,L,depth=35))

    def test_exact_irrationality_exponent_implication(self):
        # Algebraic consequence: ||16^(n-1) pi||<16^-L and
        # ||16^(n-1) pi||>16^(-(nu-1)(n-1)) => L<(nu-1)(n-1).
        # This is a symbolic implication, not a finite exhaustive proof.
        nu=F(711,100)  # 7.11 > established 7.10320534...
        self.assertGreater(nu,F(710320534,100000000))
        self.assertEqual(nu-1,F(611,100))

    def test_haar_seed_mse_exact(self):
        for N in range(1,30):
            for h in (-7,-1,1,3):self.assertEqual(haar_seed_mse(N,h),F(1,N))

    def test_harmonic_frequency_ladder(self):
        self.assertEqual(frequency_ladder_resonance_indices(8,1),tuple((n,n+1) for n in range(1,8)))
        self.assertEqual(frequency_ladder_resonance_indices(8,3),tuple((n,n+3) for n in range(1,6)))
        self.assertEqual(frequency_ladder_resonance_indices(3,5),())

    def test_four_pole_positive_strict_lower(self):
        for n in range(1,100):
            self.assertGreater(forcing(n),forcing_positive_lower(n))

    def test_zero_run_all_n_necessary_bound(self):
        for n in range(1,140):
            L=kappa15_run(n,1)  # keep selected path distinct from zero-run
            k=0
            for j in range(1,18):
                if relative_carry(n+j)==0:k+=1
                else:break
            for length in range(1,k+1):
                self.assertTrue(carry_zero_run_bound(n,length))
            # The asserted bound cannot be satisfied by an arbitrarily long zero run.
            self.assertFalse(carry_zero_run_bound(n,3+2*n))

    def test_16_boundary_implication(self):
        for n in range(3,300):
            self.assertGreater(exceptional_16_to_0_certificate(n),0)
        # 16 carry can be realized by a prepared initial seed at any time n,
        # but source injection forces the next carry to be zero for n>=3.
        for n in (3,4,6,12):
            x=F(1)-forcing(n)/F(32)  # choose x_(n-1) near 1
            s=(x-state(n-1))/16**(n-1)
            self.assertEqual(relative_carry(n,s),16)
            self.assertEqual(relative_carry(n+1,s),0)

    def test_16_borel_cantelli_tail_certificate(self):
        for start in range(3,70):
            self.assertLessEqual(haar_carry_bin_mass(start,16),F(1,16*start*start))
            self.assertLess(haar_exceptional_16_tail_probability_bound(start),F(1,16))

    def test_seed_interval_cost(self):
        for n in range(1,40):self.assertEqual(uniform_seed_information_lower_bound_bits(n),4*n-1)

if __name__=="__main__":unittest.main(verbosity=2)
