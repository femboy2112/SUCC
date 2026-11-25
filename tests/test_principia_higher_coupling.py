import unittest
from fractions import Fraction
from observational_succ.principia_coupling_mass import (
    MassSourceError, pushforward_tensor, evaluate_tensor,
    mass_from_causal_memory, compress_mass, verify_compressed_mass,
)

from observational_succ.principia_causal_memory import carrier, initial_memory, future_quotient

class HigherCouplingTests(unittest.TestCase):
    def test_three_way_parity_invisible_to_pairwise_source_marginals(self):
        even=tuple((a,b,c) for a in range(2) for b in range(2) for c in range(2) if (a+b+c)%2==0)
        odd=tuple((a,b,c) for a in range(2) for b in range(2) for c in range(2) if (a+b+c)%2==1)
        # Every single-coordinate and pair-coordinate counting marginal agrees.
        for axis in range(3):
            self.assertEqual({v:sum(x[axis]==v for x in even) for v in (0,1)},
                             {v:sum(x[axis]==v for x in odd) for v in (0,1)})
        for i in range(3):
            for j in range(i+1,3):
                self.assertEqual({(a,b):sum((x[i],x[j])==(a,b) for x in even) for a in (0,1) for b in (0,1)},
                                 {(a,b):sum((x[i],x[j])==(a,b) for x in odd) for a in (0,1) for b in (0,1)})
        E=pushforward_tensor(('0','1'),3,((t,1) for t in even))
        O=pushforward_tensor(('0','1'),3,((t,1) for t in odd))
        self.assertNotEqual(E,O)
        self.assertEqual(len(E),4)
        self.assertEqual(len(O),4)
        features=tuple((('0',1),('1',-1)) for _ in range(3))
        self.assertEqual(evaluate_tensor(('0','1'),3,((t,1) for t in even),features),4)
        self.assertEqual(evaluate_tensor(('0','1'),3,((t,1) for t in odd),features),-4)
    def test_all_proper_marginals_are_blind_to_unbounded_parity_order(self):
        from itertools import combinations, product
        from collections import Counter
        for rank in range(2,8):
            even=tuple(x for x in product((0,1),repeat=rank) if sum(x)%2==0)
            odd=tuple(x for x in product((0,1),repeat=rank) if sum(x)%2==1)
            for size in range(rank):
                for subset in combinations(range(rank),size):
                    self.assertEqual(Counter(tuple(x[j] for j in subset) for x in even),
                                     Counter(tuple(x[j] for j in subset) for x in odd))
            sign=lambda x: (-1)**sum(x)
            self.assertEqual(sum(sign(x) for x in even),2**(rank-1))
            self.assertEqual(sum(sign(x) for x in odd),-2**(rank-1))

    def test_source_memory_to_exact_signed_kernel_preserves_zero(self):
        c=carrier('minimal',('w0','w1'),('q',),('noop',),('q','q'),('0',),('same','same'),(('q',),),costs=(0,))
        m=initial_memory(c,'0')
        q=future_quotient(c)
        self.assertEqual(len(set(q.colors)),1)
        coupled=mass_from_causal_memory(c,m,q,(1,-1),((1,-1),(-1,1)))
        compressed=verify_compressed_mass(coupled,compress_mass(coupled))
        self.assertEqual((compressed.linear,compressed.pairing),((Fraction(0),),((Fraction(0),),)))
        enhanced=mass_from_causal_memory(c,m,q,(1,1),((1,1),(1,1)))
        cert=compress_mass(enhanced)
        self.assertEqual(cert.linear,(Fraction(2),))
        self.assertEqual(cert.pairing,((Fraction(4),),))
        with self.assertRaises(MassSourceError):mass_from_causal_memory(c,m,q,(1,),((1,),))

    def test_arbitrary_arity_compression_exact(self):
        classes=('A','A','B')
        entries=(((0,1,2),2),((1,0,2),-1),((2,2,2),4))
        self.assertEqual(pushforward_tensor(classes,3,entries),
                         ((('A','A','B'),Fraction(1)),(('B','B','B'),Fraction(4))))
        f=tuple({'A':Fraction(a),'B':Fraction(b)}.items() for a,b in ((1,2),(3,-1),(2,5)))
        self.assertEqual(evaluate_tensor(classes,3,entries,f),
                         Fraction(1*1*3*5+4*2*(-1)*5))
        with self.assertRaises(MassSourceError):pushforward_tensor(classes,3,(((3,1,2),1),))


if __name__=='__main__':unittest.main()
