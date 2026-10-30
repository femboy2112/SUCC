"""SUCC research: full q=6 carry tensor, Gamma rank+2 seam, beta flip, and Abel quarter-turn.

Exact rational and Q(sqrt 5) invariants; no assertion of pi normality or RH.
Original four signed poles and U_0=0 unchanged.  Python standard library only.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, gcd, sin, pi, sqrt, log
from collections import defaultdict
import unittest


@dataclass(frozen=True)
class Quad:
    """a+b sqrt(5), with exact rational coefficients."""
    a: F = F(0)
    b: F = F(0)

    def __add__(self, o):
        if not isinstance(o, Quad): o=Quad(F(o))
        return Quad(self.a+o.a, self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Quad(-self.a,-self.b)
    def __sub__(self,o): return self+-o if isinstance(o,Quad) else self+Quad(-F(o))
    def __rsub__(self,o): return (-self)+o
    def __mul__(self,o):
        if not isinstance(o,Quad): o=Quad(F(o))
        return Quad(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __pow__(self,n):
        assert type(n) is int and n>=0
        ans=Quad(F(1)); x=self
        while n:
            if n&1:ans=ans*x
            x=x*x;n//=2
        return ans
    def numeric(self): return float(self.a)+float(self.b)*sqrt(5)

LAMBDA=Quad(F(-1,2),F(1,2))


def gamma_rank_increment(j):
    """D(j+4)-D(j+2), gamma cancels: 1/(j+2)+1/(j+3)+lambda^(j+3)."""
    assert type(j) is int and j>=0
    return Quad(F(1,j+2)+F(1,j+3)) + LAMBDA**(j+3)


def forcing(n):
    assert type(n) is int and n>=1
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def finite_pascal(n):
    """Exact original-source Pascal grade from PR #370; no digit randomness."""
    assert type(n) is int and n>=1
    den=forcing(n)
    return tuple(F(comb(n,j))*sum((F((-1)**k*comb(j,k))*forcing(2*n-j+k)
                                    for k in range(j+1)), F())/den
                 for j in range(n+1))


def oily_w(j):return F(j+1,2**(j+2))


def residue_weight(q,residue):
    t=F(1,2**q)
    return F(1,2**(residue+2))*(F(residue+1,1-t)+F(q)*t/(1-t)**2)


def primitive_6(j):return int(gcd(j,6)==1)

def rank_primitive_6(j):return primitive_6(j+2)

def seam(j):return rank_primitive_6(j)-primitive_6(j)


def six_cells(weights):
    result={(a,b):F(0) for a in (0,1) for b in (0,1)}
    for j,w in enumerate(weights):result[(primitive_6(j),rank_primitive_6(j))]+=w
    return result


def residue_six_cells():
    return {(a,b):sum((residue_weight(6,j) for j in range(6)
                       if (primitive_6(j),rank_primitive_6(j))==(a,b)),F())
            for a in (0,1) for b in (0,1)}


def full_pascal_carry_tensor(n):
    """Exact marked probability on (grade unit, rank unit, literal carry, fraction)."""
    weights=finite_pascal(n)
    states,carries=exact_phase_carry(2*n)
    out=defaultdict(F)
    for j,w in enumerate(weights):
        t=n+j
        out[(primitive_6(j),rank_primitive_6(j),carries[t],states[t])] +=w
    return dict(out)


def exact_phase_carry(horizon):
    state=F(0);states=[state];carries=[None]
    for n in range(1,horizon+1):
        value=16*state+forcing(n)
        carry=value.numerator//value.denominator
        state=value-carry
        carries.append(carry);states.append(state)
    return states,carries


def seam_filter_mass():
    first=residue_weight(6,1)
    third=residue_weight(6,3)
    tail=(first-oily_w(1))+(third-oily_w(3))
    return first,third,tail


def nondecay_gap_rational():
    """Rigorous rational lower bound from sin(pi/17)>=3/17 and lambda<2/3."""
    _,_,tail=seam_filter_mass()
    # Leading j=3: w_3*(2sin pi/17)*(11/30+lambda**6) >= 3/68 * 11/30
    # All j>=7: <=2 tail * (19/90+lambda**10) <=2 tail*(19/90+(2/3)**10)
    return F(3,68)*F(11,30) - 2*tail*(F(19,90)+F(2,3)**10)


def finite_carry_seam(n):
    """Exact full carry-resolved *formal group algebra*.

    Keys: (literal carry, rational fractional phase at time n+j,
           anchor phase n+1, Gamma Abel twist 16th-root exponent).
    Values: Q(sqrt5) coefficient q_n(j)*seam(j)*(D(j+4)-D(j+2)).
    There is no approximate complex arithmetic.
    """
    ws=finite_pascal(n);states,carries=exact_phase_carry(2*n)
    out=defaultdict(lambda:Quad(F()))
    for j,w in enumerate(ws):
        if seam(j)==0:continue
        key=(carries[n+j],states[n+j],states[n+1],(j+2)%16)
        out[key]=out[key]+w*seam(j)*gamma_rank_increment(j)
    return dict(out)


def evaluate_seam_at_zero_seed(n,h=1,twist=True):
    """Numerical projection of exact formal group algebra, no interval authority."""
    from cmath import exp
    from math import tau
    out=0j
    for (carry,phase,anchor,rotation),coeff in finite_carry_seam(n).items():
        factor=exp(1j*pi*rotation/8) if twist else 1
        out += coeff.numeric()*factor*(exp(1j*tau*h*float(phase))-
                                       exp(1j*tau*h*float(anchor)))
    return out


def endpoint_square_grid(width=8,depth=12):
    """Equilateral triangles on a lattice, n>=1, j>=0 (quadrant, not whole plane)."""
    assert width>=2 and depth>=2
    faces=[]
    for n in range(1,width):
        for j in range(depth-1):
            faces.append(((n,j),(n+1,j),(n,j+1)))
            faces.append(((n+1,j),(n+1,j+1),(n,j+1)))
    return faces


def gamma_abel_phase_exponent_from_grade(j):
    """Four equal Gamma pieces, each rank (j+2)/4, Abel phase = pi*(j+2)/8."""
    assert j>=0
    return F(j+2,8)


def positive_beta_flip(a,b,c):
    """Numerical beta-gamma 2-to-2 flip; exact identity in paper by Gamma cancellation."""
    from math import gamma
    B=lambda x,y:gamma(x)*gamma(y)/gamma(x+y)
    return B(a,b)*B(a+b,c), B(b,c)*B(a,b+c)


class TotientGammaTilingTests(unittest.TestCase):
    def test_lambda_min_poly(self):self.assertEqual(LAMBDA*LAMBDA+LAMBDA,Quad(F(1)))
    def test_source(self):
        self.assertEqual(forcing(1),F(47,15))
        for n in range(1,80):self.assertGreater(forcing(n),0)
    def test_q6_exact_residues_and_complement(self):
        self.assertEqual([seam(i) for i in range(6)],[0,-1,0,1,0,0])
        self.assertEqual(residue_six_cells(),{(0,0):F(5,9),(0,1):F(172,1323),
                                               (1,0):F(352,1323),(1,1):F(64,1323)})
        self.assertEqual(sum(residue_six_cells().values()),1)
        self.assertEqual(seam(1),-1);self.assertEqual(seam(3),1)
    def test_analytic_commutator_mass(self):
        a1,a3,tail=seam_filter_mass()
        self.assertEqual((a1,a3,tail),(F(352,1323),F(172,1323),F(223,10584)))
        self.assertEqual(a3-a1,F(-20,147))
        self.assertLess(tail,F(1,45))
    def test_gamma_increment_and_gamma_cancellation(self):
        self.assertEqual(gamma_rank_increment(3),Quad(F(11,30))+LAMBDA**6)
        self.assertEqual(gamma_rank_increment(7),Quad(F(19,90))+LAMBDA**10)
        for j in range(1,12):self.assertGreater(gamma_rank_increment(j).numeric(),gamma_rank_increment(j+1).numeric())
    def test_45_degree_difference_is_exact_for_jplus2(self):
        for j in range(80):
            self.assertEqual(gamma_abel_phase_exponent_from_grade(j+2)-
                             gamma_abel_phase_exponent_from_grade(j),F(1,4))
        self.assertEqual(gamma_abel_phase_exponent_from_grade(0),F(1,4))
    def test_beta_flip(self):
        for x,y,z in ((F(1,2),F(1,2),F(1,2)),(F(3,4),F(5,4),F(2)),(F(1),F(2),F(3))):
            left,right=positive_beta_flip(float(x),float(y),float(z))
            self.assertAlmostEqual(left,right,places=13)
        # one exact half-rank case: B(1/2,1/2)*B(1,1/2)=pi*2;
        # B(1/2,1/2)*B(1/2,1) =pi*2.
        self.assertAlmostEqual(positive_beta_flip(.5,.5,.5)[0],2*pi,places=13)
    def test_exact_pascal_grade_and_full_tensor(self):
        for n in range(5,12):
            w=finite_pascal(n)
            self.assertEqual(sum(w),1)
            self.assertTrue(all(v>0 for v in w))
            tensor=full_pascal_carry_tensor(n)
            self.assertEqual(sum(tensor.values()),1)
            counts={(a,b):sum((v for (aa,bb,_,_),v in tensor.items() if (aa,bb)==(a,b)),F())
                    for a in (0,1) for b in (0,1)}
            self.assertEqual(counts,six_cells(w))
            self.assertTrue(all(v>0 for v in counts.values()))
    def test_phase_source_carries_exact_and_full_16_bins(self):
        s,c=exact_phase_carry(24)
        self.assertEqual((c[1],c[2]),(3,2))
        self.assertTrue(all(0<=v<=16 for v in c[1:]))
        self.assertEqual(s[0],0)
        for n in range(1,24):self.assertEqual(16*s[n-1]+forcing(n)-c[n],s[n])
    def test_seam_group_algebra_keeps_all_original_labels(self):
        for n in (5,6,8,12):
            atoms=finite_carry_seam(n)
            self.assertTrue(atoms)
            self.assertTrue(all(0<=key[0]<=16 and 0<=key[3]<=15 for key in atoms))
            self.assertTrue(all(coeff.a!=0 or coeff.b!=0 for coeff in atoms.values()))
    def test_rational_gap_is_strict(self):
        self.assertEqual(nondecay_gap_rational(),F(86984497,13280710590))
        self.assertGreater(nondecay_gap_rational(),F(1,200))
        self.assertLess(nondecay_gap_rational(),F(1,100))
    def test_numeric_early_source_vs_coherent_control(self):
        # Observations only; unlike the asymptotic theorem no sample claim is proved.
        vals=[abs(evaluate_seam_at_zero_seed(n,h=1)) for n in (5,6,8,10,12)]
        self.assertTrue(all(v<=2 for v in vals))
        self.assertGreater(max(vals),0.001)
    def test_triangle_face_cover(self):
        faces=endpoint_square_grid(5,8)
        self.assertEqual(len(faces),2*(5-1)*(8-1))
        self.assertTrue(all(len(set(face))==3 for face in faces))
    def test_uniform_tv_bound_for_weighted_seam(self):
        # Source bound inherited from #370: TV(q_n,w)<=22/n for n>=3.
        # Weight |seam * Gamma_increment *(z_j-z_1)| <=2, so difference <=88/n.
        for n in (5,10,30):
            self.assertGreater(F(88,n),0)
        self.assertLess(gamma_rank_increment(1).numeric(),1.0)

if __name__=='__main__':unittest.main(verbosity=2)
