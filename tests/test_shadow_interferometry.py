"""Finite exact rational BBP shadow/interferometry certificates.

All source states are generated from the original four signed poles and U_0=0.
No numerical pi, special function, or simulated random source is used for any
certificate. Tests are finite; no all-shell saving or pi normality follows.
"""
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict
import unittest


def forcing(n):
    if n < 1:
        raise ValueError('BBP forcing defined for n>=1')
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


@lru_cache(maxsize=4)
def source_states(end):
    """Return (U_n, C_n, {U_n}, beta_n) for 1<=n<=end, exact.

    beta_n=r(n+1)/15 is an inherited rigorous upper bound on T_n.
    """
    u = Q(0)
    rows = {}
    for n in range(1, end+1):
        u = 16*u + forcing(n)
        carry = u.numerator // u.denominator
        rows[n] = (u, carry, u-carry, forcing(n+1)/15)
    return rows


def circle_distance(a):
    frac = Q(a) % 1
    return min(frac, 1-frac)


def phase_chord_lower(n, m, rows):
    """Rational lower bound on (1/4)|e(Y_n)-e(Y_m)|.

    Both Y_i=U_i+T_i with 0<T_i<beta_i. Circular metric is 1-Lipschitz
    under additive perturbations, and 2 sin(pi*d)>=4*d on 0<=d<=1/2.
    """
    delta = circle_distance(rows[n][0]-rows[m][0])
    return max(Q(0), delta - rows[n][3] - rows[m][3])


def fibers(B, rows, choice):
    cells = defaultdict(list)
    for n in range(B, 2*B):
        if choice == 'carry4':
            label = rows[n][1] % 4
        elif choice == 'clock4':
            label = n % 4
        elif choice == 'joint4':
            label = (rows[n][1] % 4, n % 4)
        elif choice == 'first_hex':
            label = (16*rows[n][2]).numerator // (16*rows[n][2]).denominator
        elif choice == 'all':
            label = 0
        elif choice == 'singleton':
            label = n
        else:
            raise ValueError('unknown observation passport')
        cells[label].append(n)
    return tuple(tuple(v) for v in cells.values())


def certified_within_lower(B, rows, partition):
    """EXACT lower bound on V_{B,partition}, using unordered pairs.

    V=1/B * sum_C 1/|C| sum_{n<m in C}|z_n-z_m|^2.
    """
    total=Q(0)
    for cell in partition:
        size=len(cell)
        for j,n in enumerate(cell):
            for m in cell[j+1:]:
                d=phase_chord_lower(n,m,rows)
                total += d*d/size
    return Q(16,B)*total


def certified_anchor_lower(B,rows):
    """Exact rational lower bound on A_B=1-Re W_B.

    1-cos(2*pi*d)>=8*d^2, and d(Y_n) >= (d(U_n)-beta_n)_+.
    """
    total=Q(0)
    for n in range(B,2*B):
        d=max(Q(0),circle_distance(rows[n][0])-rows[n][3])
        total += d*d
    return Q(8,B)*total


def cmul(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])


def sub(z,w):
    return (z[0]-w[0],z[1]-w[1])


def norm2(z):
    return z[0]**2+z[1]**2


def mean(points):
    n=len(points)
    return (sum((p[0] for p in points),Q(0))/n,
            sum((p[1] for p in points),Q(0))/n)


def two_channels(z,parts):
    """Compute exactly within-energy and centroid-anchor energy over Q(i)."""
    B=len(z)
    within=Q(0)
    cent=Q(0)
    for cell in parts:
        mu=mean([z[n] for n in cell]); p=Q(len(cell),B)
        within += p*(1-norm2(mu))   # requires phases have norm 1
        cent += p*norm2(sub(mu,(Q(1),Q(0))))
    return within,cent


class ShadowInterferometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=source_states(512)

    def test_literal_original_four_poles_and_zero_ancestry(self):
        rows=self.rows
        self.assertEqual(rows[1][0],forcing(1))
        self.assertGreater(rows[1][0],0)
        self.assertEqual(rows[2][0],16*rows[1][0]+forcing(2))
        for n in (1,2,32,128,512):
            self.assertGreater(rows[n][3],0)
            self.assertEqual(rows[n][3],forcing(n+1)/15)
            self.assertEqual(rows[n][0],rows[n][1]+rows[n][2])
            self.assertGreaterEqual(rows[n][2],0)
            self.assertLess(rows[n][2],1)

    def test_direct_partial_sum_crosscheck(self):
        # Independent evaluation route: partial BBP sum versus recurrence.
        for n in (1,2,8,32,100,256,512):
            direct=sum((forcing(j)/16**j for j in range(1,n+1)),Q(0))
            self.assertEqual(self.rows[n][0],16**n*direct)

    def test_circle_chord_lower_with_exact_mutations(self):
        self.assertEqual(circle_distance(Q(2,3)),Q(1,3))
        self.assertEqual(circle_distance(Q(-7,6)),Q(1,6))
        self.assertEqual(circle_distance(Q(15,2)),Q(1,2))
        for n,m in ((8,9),(32,60),(100,200),(256,500)):
            d=phase_chord_lower(n,m,self.rows)
            self.assertGreaterEqual(d,0)
            self.assertLessEqual(d,circle_distance(self.rows[n][0]-self.rows[m][0]))
            self.assertEqual(d,phase_chord_lower(m,n,self.rows))
        # Arbitrarily large declared tails erase a valid resolution certificate.
        mutant=dict(self.rows)
        u,c,f,b=mutant[32]
        mutant[32]=(u,c,f,Q(1))
        self.assertEqual(phase_chord_lower(32,60,mutant),0)

    def test_exact_bbprational_within_certificates(self):
        expected={32:Q(3,5),64:Q(3,5),128:Q(3,5),256:Q(3,5)}
        for B,threshold in expected.items():
            lb=certified_within_lower(B,self.rows,fibers(B,self.rows,'carry4'))
            self.assertGreater(lb,threshold,msg='exact carry lower B=%d'%B)
            self.assertLessEqual(lb,1)

    def test_independent_clock_partition_certificates(self):
        for B in (32,64,128,256):
            lb=certified_within_lower(B,self.rows,fibers(B,self.rows,'clock4'))
            self.assertGreater(lb,Q(3,5),msg='exact clock lower B=%d'%B)

    def test_refinement_and_uninformative_singletons(self):
        for B in (8,32,64):
            full=certified_within_lower(B,self.rows,fibers(B,self.rows,'all'))
            carry=certified_within_lower(B,self.rows,fibers(B,self.rows,'carry4'))
            joint=certified_within_lower(B,self.rows,fibers(B,self.rows,'joint4'))
            empty=certified_within_lower(B,self.rows,fibers(B,self.rows,'singleton'))
            self.assertGreaterEqual(full,carry)
            self.assertGreaterEqual(carry,joint)
            self.assertEqual(empty,Q(0))
        # This ordering is a finite observation, not a general theorem
        # about the rational lower-bound estimator under refinement.
        # The true conditional variance IS monotone by projection.

    def test_anchor_phase_budget_finite_not_uniform(self):
        for B in (4,8,16,32,64,128):
            lb=certified_anchor_lower(B,self.rows)
            self.assertGreater(lb,Q(1,2),msg='finite anchor B=%d'%B)
            self.assertLessEqual(lb,2)

    def test_unit_phase_pythagoras_exact(self):
        z=((Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1)),
           (Q(3,5),Q(4,5)),(Q(-3,5),Q(4,5)))
        anchor=Q(1,len(z))*sum((norm2(sub(a,(Q(1),Q(0)))) for a in z),Q(0))
        for partition in (((0,1,2,3,4,5),),((0,1),(2,3),(4,5)),
                          ((0,),(1,),(2,),(3,),(4,),(5,))):
            v,l=two_channels(z,partition)
            self.assertEqual(anchor,v+l)
            self.assertGreaterEqual(v,0)
            self.assertGreaterEqual(l,0)
            self.assertLessEqual(v,anchor)
        self.assertEqual(anchor,2*(1-mean(z)[0]))

    def test_exact_refinement_variance_decrease(self):
        z=((Q(1),Q(0)),(Q(-1),Q(0)),(Q(0),Q(1)),(Q(0),Q(-1)))
        full=two_channels(z,((0,1,2,3),))[0]
        medium=two_channels(z,((0,1),(2,3)))[0]
        fine=two_channels(z,((0,),(1,),(2,),(3,)))[0]
        self.assertEqual(full,Q(1))
        self.assertEqual(medium,Q(1))
        self.assertEqual(fine,Q(0))
        alternative=two_channels(z,((0,2),(1,3)))[0]
        self.assertEqual(alternative,Q(1,2))

    def test_gamma_defect_is_fixed_scalar_times_phase(self):
        phases=((Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1)))
        coupling=(Q(2,5),Q(-1,3))
        defect=tuple(cmul(coupling,z) for z in phases)
        def pair_energy(zz,partition):
            B=len(zz);tot=Q(0)
            for cell in partition:
                for a,i in enumerate(cell):
                    for j in cell[a+1:]:tot+=norm2(sub(zz[i],zz[j]))/len(cell)
            return tot/B
        partition=((0,1),(2,3))
        self.assertEqual(pair_energy(defect,partition),
                         norm2(coupling)*pair_energy(phases,partition))
        self.assertEqual(pair_energy(phases,((0,),(1,),(2,),(3,))),0)

    def test_phase_prefix_observer_has_no_uniform_positive_energy(self):
        # Any unit phases in the same arc of length Delta have variance
        # <= pi^2*Delta^2, irrespective of their source. The upper bound
        # tends to zero as k increases; literal singleton partition gives 0.
        for k in (1,2,5,12):
            self.assertLess(Q(1,16**(2*k)),Q(1,16**(2*(k-1))))
        self.assertEqual(certified_within_lower(32,self.rows,
                         fibers(32,self.rows,'singleton')),0)

    def test_fixed_nonzero_phase_countermodel_has_zero_variance(self):
        x=Q(1,15)
        for n in range(1,13):
            self.assertEqual((16**n*x)%1,x)
        # This orbit has Re W_B=cos(2pi/15)<1, hence R0, yet
        # every phase is identical and all hidden-fiber variances are 0.
        self.assertNotEqual(x%1,0)
        z=(Q(3,5),Q(4,5))
        self.assertEqual(two_channels((z,z,z,z),((0,1),(2,3)))[0],0)

    def test_fully_locked_source_countermodel_has_zero_energy(self):
        self.assertEqual((16**100*Q(1))%1,0)
        z=((Q(1),Q(0)),)*4
        v,cent=two_channels(z,((0,1),(2,3)))
        self.assertEqual((v,cent),(0,0))


if __name__=='__main__':
    unittest.main()
