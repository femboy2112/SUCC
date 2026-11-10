from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parent))
import carry_only_innovation as ci


class CarryOnlyInnovationTests(unittest.TestCase):
    def test_literal_propagation_and_endpoint_timing(self):
        carries=[3,4,16,0,7,1]
        rows=ci.counts_from_carries(carries,3,6,(1,2))
        C=0;states=[]
        for d in carries:C=16*C+d;states.append(C)
        for k,row in rows.items():
            self.assertEqual(row['start'],states[2] % 16**k)
            self.assertEqual(row['end'],states[5] % 16**k)
            self.assertEqual(sum(row['joint'].values()),3)
            for n in range(3,6):
                self.assertGreater(row['joint'][(states[n-1] % 16**k,carries[n])],0)
        self.assertEqual(rows[2]['start'],80)

    def test_guards_and_direct_formula(self):
        with self.assertRaises(ValueError):ci.counts_from_carries([3,17],1,2)
        with self.assertRaises(ValueError):ci.counts_from_carries([3,0],1,2,(4,))
        row=ci.counts_from_carries([3,4,16,0,7,1],2,6,(1,))[1]
        with self.assertRaises(ValueError):ci.evaluate_counts(row,0,5)
        with self.assertRaises(ValueError):ci.evaluate_counts(row,16,5)
        result=ci.evaluate_counts(row,1,5)
        self.assertEqual(result['interior_transitions'],4)
        self.assertEqual(result['literal16_transition_count'],1)


if __name__=='__main__':unittest.main()
