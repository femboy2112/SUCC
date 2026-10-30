"""SUCC research-only Kepler III: exact four-pole BBP selected carry geometry.

No pi-normality claim. Mathematical constants and original U_0=0 unchanged.
Tests use exact Fraction arithmetic. Normality countermodels are conceptual,
not an assertion that the authentic zero seed lies in a generic source law.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, gcd, floor, log, pi, cos, sin
import unittest


def forcing(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError("positive original BBP source index")
    a = 8*n-7
    return F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)


def positive_regroup(n: int) -> F:
    a=8*n-7
    return F(6,a*(a+3))+F(4,a*(a+4))+F(5,a*(a+5))


def green_bounds(n:int, depth:int=28)->tuple[F,F]:
    if type(n) is not int or n<1 or type(depth) is not int or depth<1:
        raise ValueError("n,depth positive ordinary integers")
    low=sum((F(1,16**j)*forcing(n+j) for j in range(1,depth+1)), F())
    high=low+F(1,16**depth)*forcing(n+depth+1)/15
    return low,high


def base16_exponent(n:int)->int:
    """Largest L >=0 such that 16**L <= n*n, by integer arithmetic."""
    if type(n) is not int or n<1: raise ValueError("n positive")
    L=0
    while 16**(L+1)<=n*n: L+=1
    return L


def no_carry_word_bounds(n:int,L:int,depth:int=28)->tuple[F,F]:
    """Haar mass B of zero-carry word at times n+1..n+L.

    B=16^-L*(1+T_{n+L})-T_n, when B>0; bounds enclose this
    expression without taking a numeric value for pi.
    """
    if type(L) is not int or L<0:raise ValueError("L nonnegative")
    if L==0:return F(1),F(1)
    tnlo,tnhi=green_bounds(n,depth)
    tllo,tlhi=green_bounds(n+L,depth)
    scale=F(1,16**L)
    return scale*(1+tllo)-tnhi, scale*(1+tlhi)-tnlo


def exact_correction_at_circle(v:F,t:F,r:F)->bool:
    """Pure-circle phase v at time n, its tail T_n=t and forcing r_n=r."""
    if not (0<t and 0<r and t+r<1 and 0<=v<1):
        raise ValueError("must be a legitimate bounded shrinking-target instance")
    xprevious=((v-t-r)/16)%1
    digit=int(16*xprevious)
    corrected=int(16*xprevious+r)
    assert corrected-digit in (0,1)
    return corrected!=digit


def two_step_symbolic_current(d:int,k:int,v:F)->tuple[F,...]:
    """For a signed phase monomial v, exact per-carry divergence."""
    if not 0<=d<=15 or k not in (d,d+1):raise ValueError("source carry")
    event=k-d
    return tuple((int(k==c)-int(d==c))*v -
                 event*(int(d+1==c)-int(d==c))*v for c in range(17))


def original_history(N:int,seed:F=F(0))->tuple[F,...]:
    x=seed%1
    out=[x]
    for n in range(1,N+1):
        x=(16*x+forcing(n))%1
        out.append(x)
    return tuple(out)


def original_carry(n:int,history)->tuple[int,int,int]:
    d=int(16*history[n-1]);k=int(16*history[n-1]+forcing(n))
    return d,k,k-d


def pascal_packet(n:int)->tuple[F,...]:
    """Inherited authentic source, finite Pascal law (research PR #370)."""
    den=forcing(n)
    return tuple(F(comb(n,j))*sum(((-1)**k*comb(j,k)*forcing(2*n-j+k)
                                  for k in range(j+1)),F())/den
                 for j in range(n+1))


def q6_cells(j:int)->tuple[int,int]:
    return int(gcd(j,6)==1),int(gcd(j+2,6)==1)


def q6_carry_current(n:int,history):
    """Exact four-cell x 17-bin signed source-current conservation.

    Uses arbitrary rational marks 1+fractional selected phase; the same
    identity applies coefficientwise to exp(2pi i h x) for every integer h.
    """
    q=pascal_packet(n)
    before={(a,b,c):F() for a in (0,1) for b in (0,1) for c in range(17)}
    after=before.copy(); edge=before.copy()
    for j,w in enumerate(q):
        m=n+j;d,k,event=original_carry(m,history)
        a,b=q6_cells(j)
        mark=history[m]+1
        before[(a,b,d)]+=w*mark
        after[(a,b,k)]+=w*mark
        if event:
            edge[(a,b,d+1)]+=w*mark
            edge[(a,b,d)]-=w*mark
    assert all(after[k]-before[k]==edge[k] for k in before)
    return before,after,edge


def machin_pi_bounds(K:int)->tuple[F,F]:
    """Explicit rational Machin interval, independent of BBP/carry source."""
    if K<1:raise ValueError("positive arctan depth")
    def atan_series(q):
        return sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(K)),F())
    mid=16*atan_series(5)-4*atan_series(239)
    err=F(16,(2*K+1)*5**(2*K+1))+F(4,(2*K+1)*239**(2*K+1))
    return mid-err,mid+err


def mod1_interval(a:F,b:F)->tuple[F,F]:
    fa=a.numerator//a.denominator
    fb=b.numerator//b.denominator
    if fa!=fb:raise ArithmeticError("uncertified mod1 crossing: refine source")
    return a-fa,b-fb


def target_cylinder(n:int,depth:int=38)->tuple[int,int]:
    """An exact base-16 cylinder contained strictly in [T_n,T_n+r_n).

    The cylinder's last-point inclusion is checked against outward Green
    bounds, using Fraction calculations, not a guessed pi expansion.
    """
    tl,th=green_bounds(n,depth)
    r=forcing(n)
    K=1
    while F(1,16**K)>r/20:K+=1
    lower=tl+r/3
    upper=th+2*r/3
    k=(lower*16**K).__ceil__()
    assert F(k,16**K)>tl and F(k+1,16**K)<upper
    assert F(k+1,16**K)<tl+r
    return k,K



def exact_inner_target(n:int,depth:int=32)->tuple[F,F]:
    """Rational interval certified inside the *true* original window I_n."""
    tl,th=green_bounds(n,depth)
    r=forcing(n)
    lo=th+r/4
    hi=tl+3*r/4
    assert 0<lo<hi<1 and lo>th and hi<tl+r
    assert hi-lo>r/3
    return lo,hi


def ceil_fraction(v:F)->int:
    return -((-v.numerator)//v.denominator)


def adversarial_correction_seed(num_events:int=30)->tuple[F,list[tuple[int,F,F]]]:
    """Build nested rational intervals for beta = pi+16*physical_seed.

    Every beta in the final interval realizes original four-pole correction
    events at all returned n. A nested infinite limit yields E(N)~
    (log(16)/2)*N/log(N), proving sharpness of all-seed sparsity.
    """
    if type(num_events) is not int or num_events<1:raise ValueError("positive count")
    n=8
    jl,jh=exact_inner_target(n)
    lo,hi=jl/16**(n-1),jh/16**(n-1)
    events=[(n,lo,hi)]
    for _ in range(num_events-1):
        r=forcing(n)
        gap=1
        while 16**gap*r<8:gap+=1
        m=n+gap
        kl,kh=exact_inner_target(m)
        Q=16**(m-1)
        j=ceil_fraction(Q*lo-kl)
        newlo=(j+kl)/Q
        newhi=(j+kh)/Q
        assert lo<=newlo<newhi<=hi
        lo,hi=newlo,newhi
        n=m
        events.append((n,lo,hi))
    return (lo+hi)/2, events


class ExactSelectedPhaseTests(unittest.TestCase):
    def test_source_contract_and_strict_bounds(self):
        self.assertEqual(forcing(1),F(47,15))
        for n in range(3,80):
            self.assertEqual(forcing(n),positive_regroup(n))
            self.assertGreater(forcing(n),F(15,64*n*n))
            self.assertLess(forcing(n),F(1,2*n*n))
            low,high=green_bounds(n)
            self.assertGreater(low,0)
            self.assertLess(high,F(1,(8*n+1)**2))

    def test_target_geometry_exact_over_grid(self):
        for n in (2,3,8,16,40):
            r=forcing(n);tl,th=green_bounds(n,28)
            t=(tl+th)/2
            self.assertLess(t+r,1)
            for k in range(261):
                v=F(k,261)
                self.assertEqual(exact_correction_at_circle(v,t,r),t<=v<t+r)

    def test_hardcore_zero_run_for_any_seed(self):
        for n in (3,8,16,40,128,256,1000):
            L=base16_exponent(n)
            x=forcing(n)/2
            for k in range(1,L+1):
                value=16*x+forcing(n+k)
                self.assertLess(value,1)
                x=value

    def test_exact_zero_word_mass_and_info_budget(self):
        for n in (3,8,16,31,64,128,256,1024):
            L=base16_exponent(n)
            blo,bhi=no_carry_word_bounds(n,L)
            self.assertGreater(blo,forcing(n))
            if L>0:self.assertLess(bhi,F(1,16**L))
            conditional_lo=forcing(n)/bhi
            conditional_hi=forcing(n)/blo
            self.assertGreater(conditional_lo,F(15,1024))
            self.assertLess(conditional_hi,1)
            self.assertGreater(F(1,16**L)/forcing(n),1)
            self.assertLess(F(1,16**L)/forcing(n),F(1024,15))

    def test_asymptotic_moving_theta(self):
        for n in (32,128,256,1024):
            L=base16_exponent(n)
            theta=F(n*n,16**L)
            blo,bhi=no_carry_word_bounds(n,L)
            candidate=F(15,1)/(64*theta-1)
            observed_lo=forcing(n)/bhi;observed_hi=forcing(n)/blo
            self.assertLess(abs((observed_lo+observed_hi)/2-candidate),F(1,n))

    def test_circle_current_exact(self):
        for n in (2,3,8,20):
            r=forcing(n)
            for k in range(1,50):
                x=F(k,51)
                d=int(16*x);carry=int(16*x+r)
                mark=F(3*k-27,29)
                self.assertTrue(all(z==0 for z in two_step_symbolic_current(d,carry,mark)))

    def test_q6_full_4x17_rational_current(self):
        hist=original_history(48)
        for n in (3,5,8,12,15):
            b,a,j=q6_carry_current(n,hist)
            self.assertEqual(sum(a.values(),F()),sum(b.values(),F()))
            self.assertEqual(sum(j.values(),F()),F())

    def test_machin_pi_original_zero_seed(self):
        pilo,pihi=machin_pi_bounds(90)
        hist=original_history(45)
        for n in range(2,45):
            ylo,yhi=mod1_interval(16**(n-1)*pilo,16**(n-1)*pihi)
            tl,th=green_bounds(n,60)
            x=hist[n]
            self.assertLess(ylo-th,x)
            self.assertGreater(yhi-tl,x)
            d,k,e=original_carry(n,hist)
            if yhi<tl or ylo>th+forcing(n):
                self.assertEqual(e,0)
            elif ylo>=th and yhi<tl+forcing(n):
                self.assertEqual(e,1)
            else: self.fail("uncertified event: refine intervals")

    def test_target_cylinder_contains_a_realized_event(self):
        for n in (8,32,128,256):
            k,L=target_cylinder(n)
            tl,th=green_bounds(n,40)
            self.assertLess(th,F(k,16**L))
            self.assertLess(F(k+1,16**L),tl+forcing(n))

    def test_borel_cantelli_one_sided_tail(self):
        for N in (3,8,32,128):
            events=sum((forcing(n) for n in range(N,4*N)),F())
            self.assertLess(events,F(1,2*(N-1)))


    def test_constructive_correction_saturation(self):
        beta,events=adversarial_correction_seed(65)
        self.assertEqual(len(events),65)
        self.assertTrue(0<beta<1)
        for n,lo,hi in events:
            self.assertTrue(lo<beta<hi)
            y=(16**(n-1)*beta)%1
            il,ih=exact_inner_target(n)
            self.assertTrue(il<=y<=ih)
            tlo,thi=green_bounds(n)
            self.assertTrue(thi<y<tlo+forcing(n))
        self.assertTrue(events[-1][0]<1000)

    def test_exact_hardcore_pair_exclusion(self):
        for n in (16,64,256,1024):
            L=base16_exponent(n)
            tl,th=green_bounds(n,40)
            v=(tl+th)/2+forcing(n)/2
            self.assertTrue(exact_correction_at_circle(v,(tl+th)/2,forcing(n)))
            for k in range(1,L+1):
                y=(16**k*v)%1
                m=n+k
                u,w=green_bounds(m,40)
                self.assertTrue(y<u or y>=w+forcing(m))

    def test_source_rare_events_and_oily_entropy_constant(self):
        for n in (3,5,16,64,128,1024):
            r=forcing(n)
            L=base16_exponent(n)
            # All exactly rational inequalities imply
            # log(2) < -log(r) - L log(16) < log(1024/15).
            self.assertGreater(F(1,16**L)/r,2)
            self.assertLess(F(1,16**L)/r,F(1024,15))


    def test_correction_forces_actual_pure_base16_zero_block(self):
        for n in (4,16,31,64,128,256,1024):
            L=base16_exponent(n)
            self.assertGreater(L,0)
            lo,hi=green_bounds(n,40)
            # Any point in [T_n,T_n+r_n) works; the worst endpoint is below:
            upper=hi+forcing(n)
            self.assertLess(upper,F(1,n*n))
            for j in range(L):
                self.assertLess(16**j*upper,F(1,16))

    def test_sharp_event_rate_constructed_seed(self):
        import math
        for count in (20,60,160):
            beta,events=adversarial_correction_seed(count)
            n=events[-1][0]
            c=count*math.log(n)/n
            self.assertGreater(c,0.9)
            self.assertLess(c,math.log(16)/2 + 0.01)

    def test_absolute_16_digit_initial_source(self):
        hist=original_history(20)
        self.assertEqual(hist[0],F())
        self.assertEqual(hist[1],F(2,15))
        self.assertEqual(original_carry(1,hist),(0,3,3)) # transient r(1)>1: not a 0/1 correction
        self.assertEqual(original_carry(2,hist)[1],2)


if __name__=="__main__":unittest.main(verbosity=2)
