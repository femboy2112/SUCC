from fractions import Fraction as F
import unittest
from approximate_grids import optimal_radius,stoneham
from signed_transport import orbit


def brute_pair_centers(phases,q):
    points=[(q*x)%1 for x in phases]
    centers={x for x in points}
    for x in points:
        for y in points:
            centers.add(((x+y)/2)%1)
            centers.add(((x+y)/2+F(1,2))%1)
    def dist(x,y):
        d=(x-y)%1
        return min(d,1-d)
    return min(max(dist(x,c) for x in points) for c in centers)/q


class GridTests(unittest.TestCase):
    def test_pair_center_oracle_on_authentic_four_points(self):
        phases=orbit(44)[41:45]
        for q in range(1,15):
            self.assertEqual(optimal_radius(phases,q),brute_pair_centers(phases,q))

    def test_translated_grid_and_aliases(self):
        for q in (1,3,17,29):
            phases=[F(7,31)+F(j,q) for j in range(q)]
            self.assertEqual(optimal_radius(phases,q),0)
            self.assertEqual(optimal_radius(phases,1),F(q-1,2*q))

    def test_stoneham_positive_and_negative_multiplicity(self):
        for c,j in ((3,3),(5,2),(2,5)):
            r=stoneham(c,j)
            self.assertEqual(r['bounded_multiplicity_mechanism'],c in (3,5))


if __name__=='__main__':unittest.main(verbosity=2)
