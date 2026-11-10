from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import retro_probe as rp


class RetrodictionTests(unittest.TestCase):
    def test_exact_source_ancestor_cells(self):
        states=[Q(0)];carries=[]
        for n in range(1,90):
            force=sum(Q(c,8*n-p) for c,p in rp.cm.POLES)
            value=16*states[-1]+force
            old=states[-1].numerator//states[-1].denominator
            carries.append(value.numerator//value.denominator-16*old)
            states.append(value)
        checks=0
        for n in range(6,90):
            for k in (1,2,3,4):
                K=rp.integer_word(carries,n,k)
                F=sum(16**(k-j)*sum(Q(c,8*(n-k+j)-p) for c,p in rp.cm.POLES)
                      for j in range(1,k+1))
                current=states[n]%1;ancestor=states[n-k]%1
                self.assertEqual((K-F+current)/16**k,ancestor)
                self.assertLessEqual(abs(Q(2*K+1,2*16**k)-ancestor),
                                     Q(1,2*16**k)+F/16**k)
                checks+=1
        self.assertEqual(checks,336)

    def test_phase_word_is_causal_and_keeps_literal_spill(self):
        carries=[1,2,16,3,4]
        self.assertEqual(rp.integer_word(carries,3,2),48)
        self.assertEqual(rp.integer_word(carries,3,2,True),32)
        self.assertEqual(rp.integer_word(carries+[15,15],3,2),48)
        with self.assertRaises(ValueError):rp.integer_word(carries,2,3)

    def test_coherent_carry_table_keeps_the_resonance(self):
        # The coherent same-forcing completion has late carries15. Even
        # homogeneous all15 produces a retained mean approaching1, not0.
        for h in (1,3):
            for k in (2,3,4):
                z=rp.word_phase(h,k,16**k-1)
                lo,_=rp.cm.magnitude_bounds(z)
                self.assertGreater(lo,Q(999,1000))
                self.assertGreater(Q(z.re.lo,rp.cm.SCALE),Q(99,100))

    def test_rejects_truncated_source_instead_of_silently_zipping(self):
        source={'n0':5,'last':8,'L':4,'source':{'carries':[0]*8},
                'per_time_phases':[{'h':1,'start':5,'boxes':[[0,0,0,0]]}]}
        with self.assertRaisesRegex(ValueError,'full declared source clock'):rp.run(source)
        source['source']['carries'].pop()
        with self.assertRaisesRegex(ValueError,'carry stream mismatch'):rp.run(source)


if __name__=='__main__':unittest.main()
