"""Exact finite checks for S1--S5; analytic proofs are in the dossier.

No third-party dependency, fitting, pi digit input, or approximate arithmetic
enters these tests. Executing finite tests does not prove analytic continuation.
"""
from fractions import Fraction as F
from math import comb, factorial
import unittest

B = (7, 4, 3, 2)
C = (4, -2, -1, -1)
RHO = F(7, 8)


def source(n, u=F(0), weights=C):
    if n < 1:
        raise ValueError("Natural clock must be positive")
    return sum((F(c, 1) / (8*n-b+u) for b, c in zip(B, weights)), F(0))


def residue(j, u=F(0), weights=C):
    if j < 1:
        raise ValueError("Grade must be positive")
    return sum((c*(F(b)-u)**(j-1) for b, c in zip(B, weights)), F(0)) / 8**j


def residue_derivative(j, ell, u=F(0)):
    if ell > j-1:
        return F(0)
    return (F((-1)**ell * factorial(j-1), factorial(j-1-ell)*8**j)
            * sum((c*(F(b)-u)**(j-1-ell) for b,c in zip(B,C)), F(0)))


def source_trunc(n, jmax, u=F(0)):
    return sum((residue(j,u)/n**j for j in range(1,jmax+1)), F(0))


def source_remainder(n, jmax, u=F(0)):
    return sum((F(c,8)*((F(b)-u)/8)**jmax
                / (n**jmax * (n-(F(b)-u)/8))
                for b,c in zip(B,C)), F(0))


def lifted(nmax, seed=F(0), jmax=None):
    value = seed
    for n in range(1,nmax+1):
        forcing = source(n) if jmax is None else source_trunc(n,jmax)
        value = 16*value + forcing
    return value


def solve(matrix, rhs):
    a = [[F(x) for x in row]+[F(y)] for row,y in zip(matrix,rhs)]
    n = len(a)
    if any(len(row)!=n+1 for row in a):
        raise ValueError("Square system required")
    for j in range(n):
        pivot = next((i for i in range(j,n) if a[i][j]), None)
        if pivot is None:
            raise ValueError("Singular system")
        a[j],a[pivot] = a[pivot],a[j]
        q = a[j][j]
        a[j] = [x/q for x in a[j]]
        for i in range(n):
            if i!=j:
                q=a[i][j]
                a[i]=[x-q*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]


def determinant(matrix):
    a=[[F(x) for x in row] for row in matrix]
    det=F(1)
    n=len(a)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:
            return F(0)
        if pivot!=j:
            det=-det
            a[pivot],a[j]=a[j],a[pivot]
        p=a[j][j]
        det*=p
        for i in range(j+1,n):
            q=a[i][j]/p
            a[i]=[x-q*y for x,y in zip(a[i],a[j])]
    return det


def moments(weights=C):
    return [sum(c*b**k for b,c in zip(B,weights)) for k in range(8)]


def annihilator(mu):
    return solve([[mu[i+j] for j in range(4)] for i in range(4)],
                 [-mu[i+4] for i in range(4)]) + [F(1)]


class SpectralSourceTests(unittest.TestCase):
    def test_source_is_original_four_pole(self):
        self.assertEqual(source(1),F(47,15))
        for n in range(1,80):
            a=8*n-7
            positive=F(6,a*(a+3))+F(4,a*(a+4))+F(5,a*(a+5))
            self.assertEqual(source(n),positive)

    def test_first_residue_polynomials(self):
        for u in (F(0),F(1,3),F(-2,5),F(4,7)):
            self.assertEqual(residue(1,u),0)
            self.assertEqual(residue(2,u),F(15,64))
            self.assertEqual(residue(3,u),(151-30*u)/512)
            self.assertEqual(residue(4,u),(1209-453*u+45*u*u)/4096)

    def test_geometric_source_remainder(self):
        for n in (1,2,7,29,101):
            for jmax in (1,2,3,8,21):
                for u in (F(0),F(2,3),F(-3,7)):
                    self.assertEqual(source(n,u)-source_trunc(n,jmax,u),
                                     source_remainder(n,jmax,u))

    def test_pascal_translation(self):
        for j in range(1,25):
            for u,v in ((F(0),F(1,3)),(F(2,7),F(-3,5)),(F(-3),F(7))):
                moved=sum((comb(j-1,r-1)*(-v/8)**(j-r)*residue(r,u)
                           for r in range(1,j+1)),F(0))
                self.assertEqual(moved,residue(j,u+v))

    def test_pascal_composition(self):
        # Matrix composition checked independently of residue values.
        for j in range(1,18):
            for r in range(1,j+1):
                u,v=F(2,3),F(-5,7)
                direct=comb(j-1,r-1)*(-(u+v)/8)**(j-r)
                composition=sum((comb(j-1,k-1)*(-v/8)**(j-k)
                                 *comb(k-1,r-1)*(-u/8)**(k-r)
                                 for k in range(r,j+1)),F(0))
                self.assertEqual(direct,composition)

    def test_all_order_source_derivative(self):
        for j in range(2,20):
            for ell in range(0,j+2):
                u=F(3,11)
                expected=(F((-1)**ell*factorial(j-1),
                            8**ell*factorial(j-1-ell))*residue(j-ell,u)
                          if ell<j else F(0))
                self.assertEqual(residue_derivative(j,ell,u),expected)

    def test_rightmost_source_derivative_residue(self):
        for ell in range(9):
            for j in range(1,ell+2):
                self.assertEqual(residue_derivative(j,ell),0)
            expected=F((-1)**ell*factorial(ell+1)*15,8**ell*64)
            self.assertEqual(residue_derivative(ell+2,ell),expected)

    def test_exact_moments_and_hankel(self):
        mu=moments()
        self.assertEqual(mu,[0,15,151,1209,8995,64905,461611,3259089])
        h=[[mu[i+j] for j in range(4)] for i in range(4)]
        self.assertEqual(determinant(h),-115200)
        vandermonde=[[F(b)**k for b in B] for k in range(4)]
        self.assertEqual(determinant(h),
                         determinant(vandermonde)**2*4*(-2)*(-1)*(-1))

    def test_prony_reconstruction_without_pole_input(self):
        # Annihilator uses only moments, not pole positions.
        poly=annihilator(moments())
        self.assertEqual(poly,[168,-206,89,-16,1])
        recovered=[x for x in range(-20,21)
                   if sum(poly[k]*x**k for k in range(5))==0]
        self.assertEqual(recovered,[2,3,4,7])
        weights=solve([[F(b)**k for b in recovered] for k in range(4)],moments()[:4])
        self.assertEqual(weights,[-1,-1,-2,4])

    def test_prony_mutation_and_rank_control(self):
        changed=moments()
        changed[7]+=1
        self.assertNotEqual(annihilator(changed),[168,-206,89,-16,1])
        rank3=moments((4,-2,-1,0))
        h=[[rank3[i+j] for j in range(4)] for i in range(4)]
        self.assertEqual(determinant(h),0)
        with self.assertRaises(ValueError):
            annihilator(rank3)

    def test_source_mutant_same_leading_residue(self):
        mutant=(5,-5,0,0)
        self.assertEqual(residue(2,weights=mutant),residue(2))
        self.assertNotEqual(residue(3,weights=mutant),residue(3))
        self.assertNotEqual(source(1,weights=mutant),source(1))

    def test_positive_residue_bounds(self):
        for j in range(2,150):
            aj=residue(j)
            self.assertGreaterEqual(aj,F(15,56)*RHO**(j-1))
            self.assertLess(aj,F(1,2)*RHO**(j-1))

    def test_exact_first_time_tail(self):
        for jmax in range(1,80):
            tail=(4*RHO**jmax-F(1,2)*F(1,2)**jmax
                  -F(1,5)*F(3,8)**jmax-F(1,6)*F(1,4)**jmax)
            self.assertEqual(source(1)-source_trunc(1,jmax),tail)

    def test_finite_time_precision_cost(self):
        for n in (1,2,3,8,17,32):
            for jmax in (1,2,4,9,24):
                error=lifted(n)-lifted(n,jmax=jmax)
                scale=16**n*RHO**jmax
                self.assertGreaterEqual(error,F(15,112)*scale)
                self.assertLess(error,F(4,15)*scale)

    def test_exact_seed_separation(self):
        for n in range(1,25):
            for seed in (F(1,7),F(-3,5),F(2)):
                self.assertEqual(lifted(n,seed)-lifted(n),16**n*seed)


if __name__ == '__main__':
    unittest.main(verbosity=2)
