"""Exact first-jet, primary-part, carry-seam and prime-frame probes.

Research support only. No claim about asymptotic digit distribution.
All arithmetic assertions use Fraction; logarithms have rational enclosures.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import unittest


def floor(x):
    return x.numerator // x.denominator


def frac(x):
    return x - floor(x)


def factor(n):
    if n < 1:
        raise ValueError("positive factorization input required")
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def valuations(x):
    if not x:
        raise ValueError("valuation vector of zero is not finite")
    out = factor(abs(x.numerator))
    for p, exponent in factor(x.denominator).items():
        out[p] = out.get(p, 0) - exponent
    return {p: e for p, e in out.items() if e}


def primary(x, p):
    """Canonical p-primary representative in [0,1), exactly {x}_p."""
    d = x.denominator
    power = 1
    while d % p == 0:
        d //= p
        power *= p
    if power == 1:
        return F(0)
    return F((x.numerator * pow(d, -1, power)) % power, power)


def components(x):
    return {p: primary(x, p) for p in factor(x.denominator)}


def source(n):
    a = 8*n - 7
    return F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)


def potential(a):
    a = F(a)
    return a**4 / ((a+3)**2 * (a+4) * (a+5))


def decreasing_slope(a):
    a = F(a)
    return F(4)/a**2-F(2)/(a+3)**2-F(1)/(a+4)**2-F(1)/(a+5)**2


def second_slope(a):
    a = F(a)
    return F(8)/a**3-F(4)/(a+3)**3-F(2)/(a+4)**3-F(2)/(a+5)**3


@dataclass(frozen=True)
class Jet:
    """a*(1+q*epsilon), epsilon^2=0; a!=0 and q are rational."""
    a: F
    q: F

    def __post_init__(self):
        if self.a == 0:
            raise ValueError("a dual-number unit must have nonzero value")

    def __mul__(self, other):
        return Jet(self.a*other.a, self.q+other.q)

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("integer powers only")
        return Jet(self.a**exponent, exponent*self.q)


def orbit(n, seed=F(0)):
    out = [seed]
    for j in range(1, n+1):
        out.append(16*out[-1]+source(j))
    return out


def log_positive_bounds(x, terms=64):
    """Rational enclosure for log(x), x>=1, from the atanh series."""
    if x < 1:
        raise ValueError("this branch expects x>=1")
    t = (x-1)/(x+1)
    lo = 2*sum((t**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    err = 2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return lo, lo+err


def secant_bounds(n, m, terms=64):
    lo = hi = F(0)
    for j in range(1,n+1):
        a = 8*j-7
        ratio = potential(F(a)+F(1,m))/potential(a)
        l,h = log_positive_bounds(ratio, terms)
        weight = m*16**(n-j)
        lo += weight*l
        hi += weight*h
    return lo,hi


def centered_secant_bounds(n,m,terms=64):
    if m < 2:
        raise ValueError("centered frame requires M>=2")
    lo=hi=F(0)
    for j in range(1,n+1):
        a=8*j-7
        ratio=potential(F(a)+F(1,m))/potential(F(a)-F(1,m))
        l,h=log_positive_bounds(ratio,terms)
        weight=F(m,2)*16**(n-j)
        lo += weight*l
        hi += weight*h
    return lo,hi


def frame_prime_vector(n,m):
    out = {}
    for j in range(1,n+1):
        a=8*j-7
        ratio=potential(F(a)+F(1,m))/potential(a)
        for p,e in valuations(ratio).items():
            out[p] = out.get(p,0)+16**(n-j)*e
    return {p:e for p,e in out.items() if e}


class ExactJetTests(unittest.TestCase):
    def test_jet_product_power_and_inverse(self):
        for a,q in [(F(2,3),F(-7,5)),(F(-11,13),F(2,9)),(F(1),F(0))]:
            z=Jet(a,q)
            self.assertEqual(z*z**-1,Jet(F(1),F(0)))
            self.assertEqual(z**7*z**-3,z**4)
        self.assertNotEqual(Jet(F(1),F(0)),Jet(F(1),F(1)))

    def test_original_four_pole_odd_denominator(self):
        for n in range(-37,81):
            r=source(n)
            rhs=F(4,8*n-7)-F(1,8*n-3)-F(3*n-1,(2*n-1)*(4*n-1))
            self.assertEqual(r,rhs)
            self.assertEqual(r.denominator%2,1)
        self.assertEqual(source(1),F(47,15))

    def test_exact_jet_realization_and_value_blindness(self):
        for seed in (F(0),F(3,7),F(-2,5)):
            z=Jet(F(1),seed)
            u=seed
            for n in range(1,4):
                z=z**16*Jet(potential(8*n-7),source(n))
                u=16*u+source(n)
                self.assertEqual(z.q,u)
                self.assertEqual(valuations(z.a).get(2),-(16**n-1)//3)
        z0=Jet(F(1),F(0))**16*Jet(potential(1),source(1))
        z1=Jet(F(1),F(1,7))**16*Jet(potential(1),source(1))
        self.assertEqual(z0.a,z1.a)
        self.assertNotEqual(z0.q,z1.q)

    def test_primary_reconstruction_and_transport(self):
        for den in range(1,81):
            for num in (-91,-7,-1,0,1,19,113):
                q=F(num,den)
                cs=components(q)
                self.assertEqual(frac(sum(cs.values(),F(0))),frac(q))
                for p,c in cs.items():
                    self.assertEqual(primary(q-c,p),0)
                    self.assertEqual(primary(16*q,p),frac(16*c))

    def test_crt_inverse_mutation_rejected(self):
        q=F(1,15)
        true=frac(primary(q,3)+primary(q,5))
        bad=frac(F(1,3)+F(1,5))
        self.assertEqual(true,q)
        self.assertNotEqual(bad,q)

    def test_local_carry_seam(self):
        for seed in (F(0),F(2,7),F(-13,8),F(17,45)):
            us=orbit(50,seed)
            for n in range(1,len(us)):
                q0,q1=us[n-1],us[n]
                r=source(n)
                ps=set(components(q0))|set(components(r))|set(components(q1))
                s0=sum((primary(q0,p) for p in ps),F(0))
                s1=sum((primary(q1,p) for p in ps),F(0))
                sr=sum((primary(r,p) for p in ps),F(0))
                local=sum(floor(16*primary(q0,p)+primary(r,p)) for p in ps)
                self.assertEqual(r-sr,floor(r-sr))
                stitched=local+int(r-sr)+floor(s1)-16*floor(s0)
                literal=floor(16*frac(q0)+r)
                self.assertEqual(stitched,literal)
                self.assertEqual(floor(q1),16*floor(q0)+literal)

    def test_omitting_seam_is_not_literal_carry(self):
        us=orbit(4)
        failed=False
        for n in range(1,len(us)):
            pset=set(components(us[n-1]))|set(components(source(n)))
            local=sum(floor(16*primary(us[n-1],p)+primary(source(n),p)) for p in pset)
            if local != floor(16*frac(us[n-1])+source(n)):
                failed=True
        self.assertTrue(failed)

    def test_omitted_prime_same_source_aliases(self):
        retained=(2,3,5)
        p=7
        base=orbit(24)
        for a in (1,6,19,73,200):
            shifted=orbit(24,F(a,p**3))
            for x,y in zip(base,shifted):
                for prime in retained:
                    self.assertEqual(primary(x,prime),primary(y,prime))
            self.assertNotEqual(frac(base[13]),frac(shifted[13]))

    def test_every_hex_cylinder_inside_same_retained_fiber(self):
        base=orbit(9)[9]
        p=7
        k=4
        # 7^4 > 16^2: invertible multiplication yields a mesh finer than two hex digits.
        seen={floor(16**2*frac(base+16**9*F(a,p**k))) for a in range(p**k)}
        self.assertEqual(seen,set(range(16**2)))

    def test_prime_frame_factorization(self):
        for n in (1,2,3):
            for m in (1,2,7):
                value=F(1)
                for j in range(1,n+1):
                    a=8*j-7
                    value *= (potential(F(a)+F(1,m))/potential(a))**(16**(n-j))
                self.assertEqual(valuations(value),frame_prime_vector(n,m))

    def test_rational_log_interval_and_forward_precision_bound(self):
        c1=F(6853,1800)
        c2=F(38447,44100)
        self.assertEqual(c1,decreasing_slope(1))
        self.assertEqual(c2,decreasing_slope(2))
        for n in (1,2,3,5,9):
            u=orbit(n)[-1]
            for m in (1,2,7,257):
                lo,hi=secant_bounds(n,m,100)
                lower=c2*16**(n-1)/F(2*m)
                upper=c1*(16**n-1)/F(30*m)
                self.assertGreater(u-hi,0)
                self.assertGreaterEqual(u-hi,lower)
                self.assertLessEqual(u-lo,upper)

    def test_seed_detected_by_nonzero_frame(self):
        m=11
        seed=F(3,7)
        unchanged=F(1)
        shifted=1+seed/F(m)
        self.assertNotEqual(valuations(unchanged),valuations(shifted))
        self.assertEqual(Jet(F(1),F(0)).a,Jet(F(1),seed).a)

    def test_finite_frames_do_not_determine_unrestricted_germ(self):
        # g(u)=1+s*u*(1-M*u) agrees at the two frames but has g'(0)=s.
        for m in (2,11,257):
            seed=F(3,7)
            germ=lambda u: 1+seed*u*(1-m*u)
            self.assertEqual(germ(F(0)),1)
            self.assertEqual(germ(F(1,m)),1)
            h=F(1,2*m)
            # Exact three-point derivative of the quadratic germ, not a
            # floating difference or an untested assigned seed label.
            derived=(4*germ(h)-germ(2*h)-3*germ(F(0)))/(2*h)
            self.assertEqual(derived,seed)
            self.assertNotEqual(derived,0)

    def test_centered_frames_improve_precision_order(self):
        for n in (1,3,7):
            u=orbit(n)[-1]
            for m in (2,7,257):
                lo,hi=centered_secant_bounds(n,m,300)
                lower=second_slope(F(3,2))*16**(n-1)/F(6*m*m)
                upper=second_slope(F(1,2))*(16**n-1)/F(90*m*m)
                self.assertGreater(lo-u,0)
                self.assertGreaterEqual(lo-u,lower)
                self.assertLessEqual(hi-u,upper)


if __name__=="__main__":
    unittest.main(verbosity=2)
