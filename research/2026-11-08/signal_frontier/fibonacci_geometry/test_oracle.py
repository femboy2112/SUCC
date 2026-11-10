from fractions import Fraction as Q
import unittest
from oracle import CQ, rational_rotation, calibrate, points, fibonacci, alpha_power, belief_adapter

class GeometryTests(unittest.TestCase):
    def test_blind_recovery(self):
        c,g,rho=CQ(2,-3),CQ(4,1),rational_rotation(Q(2,7))
        got=calibrate(points(c,g,rho))
        self.assertEqual((got['center'],got['gain'],got['return']),(c,g,rho))
    def test_no_radius_from_clock(self):
        rho=rational_rotation(Q(1,3))
        a=calibrate(points(CQ(0),CQ(1),rho));b=calibrate(points(CQ(8),CQ(2),rho))
        self.assertEqual(a['return'],b['return'])
        self.assertNotEqual(a['curvature_squared'],b['curvature_squared'])
    def test_orientation_alias(self):
        rho=rational_rotation(Q(3,4));a=points(CQ(),CQ(2),rho);b=tuple(z.conj() for z in a)
        self.assertEqual([(x-y).norm2() for x in a for y in a],[(x-y).norm2() for x in b for y in b])
        self.assertNotEqual(calibrate(a)['return'],calibrate(b)['return'])
    def test_fibonacci_return(self):
        for k in (2,3,8,21,55):
            self.assertEqual(tuple((-1)**(k-1)*v for v in alpha_power(k)),(-fibonacci(k-1),fibonacci(k)))
    def test_history_memory(self):
        game,_=belief_adapter();self.assertEqual(game.rank(),3)
        root=game.root
        for _ in range(3):root=game.options(root)['read'][0][1]
        self.assertEqual(game.goal(root),'0')
        self.assertEqual({s for _,s in root},{game.field.count-1})
    def test_singular_return_rejected(self):
        with self.assertRaises(ValueError):calibrate((CQ(1),CQ(1),CQ(1)))
        with self.assertRaises(ValueError):calibrate((CQ(0),CQ(1),CQ(2)))
    def test_wrong_gain_not_a_phase_transport(self):
        c,g=CQ(2),CQ(3,1);rho=rational_rotation(Q(1,2));cal=calibrate(points(c,g,rho))
        z=rational_rotation(Q(2,3));new_frame=CQ(0,1)
        wrong=(c+new_frame*g*z-cal['center'])/cal['gain']
        self.assertNotEqual(wrong,z)

if __name__=='__main__':unittest.main()
