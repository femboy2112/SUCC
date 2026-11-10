import unittest
from fractions import Fraction as Q
from moment_memory import *


class MomentMemoryTests(unittest.TestCase):
    def test_newton_against_direct_atom_powers(self):
        for q in range(1,7):
            for case in range(4):
                atoms=[unit(Q(j-case,case+2)) for j in range(q)]
                direct=moments(atoms,32)
                self.assertEqual(reconstruct_moments(direct[1:q+1],32),direct)

    def test_pair_mean_closure_and_antipodal_alias(self):
        for a in range(-4,5):
            for b in range(-4,5):
                atoms=[unit(Q(a,3)),unit(Q(b,5))]
                s=mean(atoms)
                if s!=ZERO:
                    self.assertEqual(pair_moment_from_mean(s,16),moments(atoms,16)[16])
        self.assertEqual(mean([ONE,neg(ONE)]),ZERO)
        self.assertEqual(mean([unit(Q(1,2)),neg(unit(Q(1,2)))]),ZERO)
        self.assertNotEqual(power(ONE,16),power(unit(Q(1,2)),16))
        with self.assertRaises(ZeroDivisionError):pair_moment_from_mean(ZERO,16)

    def test_even_half_moment_chart(self):
        for q in (2,4,6,8):
            for case in range(7):
                atoms=[unit(Q(j-case,case+3)) for j in range(q)]
                prefix=moments(atoms,q)[1:]
                coefficients=newton_coefficients(prefix)
                if coefficients[q//2]!=ZERO:
                    self.assertEqual(even_half_coefficients(prefix[:q//2]),coefficients)
        # Unit-root polynomial Z^4-Z^3-Z+1: moments M1=M2=1/4.
        with self.assertRaises(ZeroDivisionError):
            even_half_coefficients([(Q(1,4),Q(0)),(Q(1,4),Q(0))])

    def test_extra_moment_removes_antipodal_alias(self):
        for k in range(-4,5):
            a=unit(Q(k,3));atoms=[a,neg(a)]
            direct=moments(atoms,32)
            self.assertEqual(reconstruct_moments(direct[1:3],32),direct)

    def test_no_uniform_conditioning(self):
        a=(Q(3,5),Q(4,5))
        for N in (100,1000,10000):
            s=(Q(1,N),Q(0));t=scale(a,Q(1,N))
            output=sub(pair_moment_from_mean(s,16),pair_moment_from_mean(t,16))
            # Exact finite witnesses to growing error amplification.
            self.assertGreater(norm2(output),100*norm2(sub(s,t)))
            self.assertGreater(norm2(output),Q(1,10))

    def test_exact_chronology_radius(self):
        for a in range(5):
            z,w=unit(Q(a,3)),unit(Q(2*a+1,4))
            f,g=unit(Q(a+1,7)),unit(Q(a+2,9))
            plus,minus,c,r2=chronology_predictions(z,w,f,g)
            self.assertEqual(norm2(sub(plus,c)),r2)
            self.assertEqual(norm2(sub(minus,c)),r2)
            self.assertEqual(r2,norm2(sub(power(z,16),power(w,16)))*norm2(sub(f,g))/16)
        plus,minus,c,r2=chronology_predictions(ONE,ONE,unit(1),unit(2))
        self.assertEqual(plus,minus);self.assertEqual(r2,0)

    def test_hypothesis_rejections(self):
        with self.assertRaises(ValueError):newton_coefficients([])
        with self.assertRaises(ValueError):moments([(Q(2),Q(0))],2)
        with self.assertRaises(ValueError):forcing_difference_bound(0,1)
        with self.assertRaises(ValueError):power(ONE,-1)

    def test_deterministic_source_replay_is_singleton(self):
        from observational_succ.selected_orbit import SelectedOrbit
        first=SelectedOrbit();second=SelectedOrbit()
        actual=(first.state(11),first.state(16))
        replay=(second.state(11),second.state(16))
        self.assertEqual(actual,replay)
        self.assertNotEqual(actual[0],actual[1])
        # Unlimited zero-source replay excludes the swapped assignment.
        admissible=[candidate for candidate in (actual,tuple(reversed(actual))) if candidate==replay]
        self.assertEqual(len(admissible),1)


if __name__=='__main__':unittest.main()
