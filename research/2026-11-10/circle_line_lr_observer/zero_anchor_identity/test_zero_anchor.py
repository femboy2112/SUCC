"""Exact local probes for SUCC's proposed source-selected identity kernel.

No general normality proof; these tests certify finite semantics only.
"""
import unittest
from fractions import Fraction as Q

import zero_anchor as z


class ZeroAnchorTests(unittest.TestCase):
    def test_four_poles_and_canonical_factorization(self):
        for n in range(1,40):
            self.assertEqual(z.r(n),z.r_factored(n))
            self.assertGreater(z.r(n),z.r(n+1))
            self.assertGreater(z.r(n),0)
        self.assertEqual(z.r(1),Q(47,15))
        with self.assertRaises(ValueError):z.r(True)

    def test_source_interval_effective_shrinking(self):
        old=z.bbp_x(0)
        for n in range(1,32):
            box=z.bbp_x(n)
            self.assertLess(old.lo,box.lo)
            self.assertGreater(old.hi,box.hi)
            self.assertLess(box.width,Q(1,16**n))
            self.assertEqual(box.width,z.r(n+1)/Q(15*16**n))
            old=box

    def test_distinct_geometric_and_bbp_rational_names(self):
        self.assertNotEqual(z.circle_x(1),z.bbp_x(1))
        for depth in range(0,35):
            a,b=z.circle_x(depth),z.bbp_x(depth)
            self.assertLess(max(a.lo,b.lo),min(a.hi,b.hi))
        result=z.certify_root(Q(1,10**15),max_depth=80)
        self.assertLess(result['intersection'].width,Q(1,10**15))
        self.assertLess(result['bbp'].lo,result['geometry'].hi)
        self.assertLess(result['geometry'].lo,result['bbp'].hi)

    def test_finite_budget_is_unknown_not_false(self):
        with self.assertRaises(z.Unresolved):z.certify_root(Q(1,16**99),max_depth=2)
        with self.assertRaises(z.Unresolved):z.rational_probe(Q(1,5),max_depth=0)
        with self.assertRaises(TypeError):z.rational_probe(0.2)

    def test_rational_queries_split(self):
        for q,answer in [(Q(1,5),'ABOVE_ROOT'),(Q(3,16),'BELOW_ROOT'),
                         (Q(355,1808),'ABOVE_ROOT'),(Q(1818,9259),'BELOW_ROOT')]:
            status,stage=z.rational_probe(q,max_depth=100)
            self.assertEqual(status,answer)
            self.assertGreaterEqual(stage,0)

    def test_affine_source_state_and_recovery(self):
        seeds=(z.ZERO,z.RATIONAL_ALIAS,z.COHERENT_WRONG,
               z.AffineX(Q(4,9),Q(7,11)),z.AffineX(Q(-8,7),Q(13,19)))
        for seed in seeds:
            for n in range(15):
                u=z.state(n,seed)
                self.assertEqual(z.recovered_seed(n,u),seed)
                self.assertEqual(z.next_state(n,u),z.state(n+1,seed))
                self.assertEqual(u+z.future_tail(n),z.complete(n,seed))

    def test_affine_clock_arrows_preserve_unique_zero_and_cohere(self):
        for n in range(0,6):
            for seed in (z.ZERO,z.RATIONAL_ALIAS,z.COHERENT_WRONG):
                u=z.state(n,seed)
                for a,b,c,d in ((2,3,3,1),(5,0,2,4),(3,7,1,5)):
                    mid,stage=z.affine_clock(n,u,c,d)
                    finish=z.affine_clock(mid,stage,a,b)
                    direct=z.affine_clock(n,u,a*c,a*d+b)
                    self.assertEqual(finish,direct)
                    self.assertEqual(z.recovered_seed(direct[0],direct[1]),seed)
                # Prime/ordinary successor square D_p S=S^p D_p.
                for p in (2,3,5):
                    left=z.affine_clock(n+1,z.next_state(n,u),p,0)
                    dn,dstate=z.affine_clock(n,u,p,0)
                    self.assertEqual(left,(dn+p,z.state(dn+p,seed)))
        with self.assertRaises(ValueError):z.affine_clock(0,z.state(0),0,1)

    def test_source_zero_anchor_and_wrong_seed(self):
        self.assertTrue(z.ZERO.is_zero)
        self.assertFalse(z.RATIONAL_ALIAS.is_zero)
        self.assertFalse(z.COHERENT_WRONG.is_zero)
        for n in range(10):
            self.assertEqual(z.complete(n,z.COHERENT_WRONG),z.ZERO)
            self.assertEqual(z.recovered_seed(n,z.state(n,z.COHERENT_WRONG)),z.COHERENT_WRONG)
            self.assertNotEqual(z.state(n,z.COHERENT_WRONG),z.state(n,z.ZERO))
        with self.assertRaises(ValueError):z.certify_phase(3,seed=z.COHERENT_WRONG)
        with self.assertRaises(ValueError):z.certify_phase(3,seed=z.RATIONAL_ALIAS)

    def test_eventual_alias_classification(self):
        self.assertEqual(z.eventual_phase_alias(z.ZERO,z.ZERO),0)
        self.assertEqual(z.eventual_phase_alias(z.ZERO,z.RATIONAL_ALIAS),1)
        self.assertEqual(z.eventual_phase_alias(z.ZERO,z.AffineX(Q(1,256),Q(0))),2)
        self.assertEqual(z.eventual_phase_alias(z.ZERO,z.AffineX(Q(1,32),Q(0))),2)
        self.assertEqual(z.eventual_phase_alias(z.ZERO,z.AffineX(Q(13),Q(0))),0)
        self.assertIsNone(z.eventual_phase_alias(z.ZERO,z.COHERENT_WRONG))
        self.assertIsNone(z.eventual_phase_alias(z.ZERO,z.AffineX(Q(1,17),Q(0))))
        self.assertIsNone(z.eventual_phase_alias(z.ZERO,z.AffineX(Q(1,17),Q(2,3))))

    def test_irrational_symbolic_coordinates_not_general_equality(self):
        with self.assertRaises(TypeError):z.AffineX(Q(0),0)
        with self.assertRaises(TypeError):z.state(1,Q(0))
        with self.assertRaises(ValueError):z.AffineX(Q(1),Q(0)).bounds(z.bbp_x(2))
        root=z.AffineX(Q(0),Q(1)).bounds(z.bbp_x(2))
        minus=z.AffineX(Q(0),Q(-1)).bounds(z.bbp_x(2))
        self.assertEqual(minus.lo,-root.hi)
        self.assertEqual(minus.hi,-root.lo)

    def test_phase_carries_and_bounds(self):
        prefix=z.exact_hex_prefix(18)
        self.assertEqual(''.join('0123456789ABCDEF'[d] for d in prefix[:16]),'3243F6A8885A308D')
        certs=z.certify_phase_window(18,max_depth=80)
        for n,c in enumerate(certs):
            self.assertEqual(c.k,int(''.join('0123456789ABCDEF'[d] for d in prefix[:n]),16) if n>=1 else 0)
            self.assertLess(Q(0),c.phase.lo)
            self.assertLess(c.phase.hi,Q(1))
            self.assertLess(c.phase.width,Q(1,16))
            self.assertLess(Q(0),c.future_tail.lo)
            self.assertEqual(c.source_lift.lo-c.k,c.phase.lo)
            self.assertEqual(c.source_lift.hi-c.k,c.phase.hi)
            self.assertEqual((16*c.phase.lo).numerator//(16*c.phase.lo).denominator,
                             (16*c.phase.hi).numerator//(16*c.phase.hi).denominator)

    def test_hex_prefix_and_word_counters(self):
        self.assertEqual(z.exact_hex_prefix(1),(3,))
        self.assertEqual(z.exact_hex_prefix(4),(3,2,4,3))
        for length in (1,2,3):
            counts=z.finite_word_counts(48,length)
            self.assertEqual(sum(counts.values()),48)
            self.assertTrue(all(len(word)==length for word in counts))

    def test_smooth_phase_error_transfer_and_shrinking(self):
        for N,h in [(2,1),(11,8),(17,-3)]:
            a=z.weyl_budget(N,h,N)
            b=z.weyl_budget(N,h,N+4)
            self.assertGreater(a,b)
            self.assertGreater(b,0)
            self.assertLess(b,Q(1,16))
        self.assertEqual(z.weyl_budget(12,0,15),0)
        self.assertLess(z.epoch_weyl_budget(17,8,38),z.epoch_weyl_budget(17,8,34))
        self.assertLess(z.ratio_fiber_budget(11,8,30),z.ratio_fiber_budget(11,8,25))
        with self.assertRaises(ValueError):z.ratio_fiber_budget(3,8,8)

    def test_source_completion_tail_budget(self):
        for n in range(1,15):
            box=z.bbp_x(50)
            t=z.future_tail(n).bounds(box)
            self.assertGreater(t.lo,0)
            self.assertLess(t.hi,z.r(n+1)/15)
        self.assertLess(z.source_completion_budget(40,8),z.source_completion_budget(20,8))

    def test_rational_haar_identity_magnitude(self):
        self.assertEqual(z.haar_defect((Q(0),)),Q(15,32))
        self.assertEqual(z.haar_defect((Q(1,2),)),Q(1,4))
        for phases in ((Q(1,5),),(Q(1,4),Q(3,4)),(Q(3,16),Q(4,16),Q(13,16))):
            self.assertGreaterEqual(z.haar_defect(phases),0)
            self.assertLessEqual(z.haar_defect(phases),1)

    def test_signed_overlap_nonnegative_and_calibrated(self):
        for M in (1,2,4,6):
            a=z.signed_overlap_receipt(M,max_depth=80)
            self.assertEqual(a.entire,(a.early+a.late)/2-a.overlap)
            self.assertGreaterEqual(a.overlap,0)
            self.assertLessEqual(a.certified_lower,a.certified_upper)
            certs=[z.certify_phase(n,max_depth=90) for n in range(2*M)]
            # Refine the *same* source to deeper intervals and compare two independent
            # rational shadow values; both errors must cover their common true value.
            l=42
            deep=[]
            for n in range(2*M):
                box=z.bbp_x(l)
                lo,hi=16**n*box.lo,16**n*box.hi
                deep.append((lo+hi)/2-certs[n].k)
            deep=tuple(deep)
            omega2=(z.haar_defect(deep[:M])+z.haar_defect(deep[M:]))/2-z.haar_defect(deep)
            self.assertLessEqual(abs(a.overlap-omega2),a.overlap_error+Q(1,16**(35-2*M)))

    def test_haar_branch_seam_is_not_globally_lipschitz(self):
        eps=Q(1,65536)
        left,right=Q(1,16)-eps,Q(1,16)+eps
        shifted1=tuple((left+Q(a,16))%1 for a in range(16))
        shifted2=tuple((right+Q(a,16))%1 for a in range(16))
        from zero_anchor import _cdf_distance
        self.assertGreater(_cdf_distance(shifted1,shifted2),Q(1,32))
        self.assertLess(right-left,Q(1,10000))
        # This is why signed_overlap_receipt verifies 1/16 digit charts first.


    def test_overlap_direct_signed_cdf_independent_replay(self):
        from itertools import chain
        def atom_law(phases):
            return (tuple(phases),tuple((z0+Q(a,16))%1 for z0 in phases for a in range(16)))
        def signed_cdf(phases,t):
            pos,neg=atom_law(phases)
            return Q(sum(x<=t for x in pos),len(pos))-Q(sum(x<=t for x in neg),len(neg))
        for M in (1,2,3):
            certs=z.certify_phase_window(2*M)
            first=tuple(c.phase.mid for c in certs[:M])
            second=tuple(c.phase.mid for c in certs[M:])
            places=sorted(set(chain.from_iterable(atom_law(first)+atom_law(second))))
            direct=Q(0)
            for left,right in zip(places,places[1:]):
                t=(left+right)/2
                a,b=signed_cdf(first,t),signed_cdf(second,t)
                if a*b<0:direct+=(right-left)*min(abs(a),abs(b))
            self.assertEqual(direct,z.signed_overlap_receipt(M).overlap)

    def test_local_cdf_transport_error_with_fresh_phase_refinement(self):
        from zero_anchor import _cdf_distance
        for N in (3,8,17):
            certs=z.certify_phase_window(N)
            coarse=tuple(c.phase.mid for c in certs)
            refined=[]
            for c in certs:
                box=z.bbp_x(N+35)
                refined.append((16**c.n*(box.lo+box.hi))/2-c.k)
            refined=tuple(refined)
            error=sum((c.midpoint_error for c in certs),Q(0))/N
            d1=z.haar_defect(coarse)
            d2=z.haar_defect(refined)
            self.assertLessEqual(abs(d1-d2),2*error+Q(1,16**25))

    def test_source_guard_rejects_forged_inputs(self):
        with self.assertRaises(ValueError):z.bbp_x(-1)
        with self.assertRaises(ValueError):z.certify_phase(True)
        with self.assertRaises(ValueError):z.weyl_budget(True,8,12)
        with self.assertRaises(TypeError):z.weyl_budget(2,True,12)
        with self.assertRaises(ValueError):z.certify_root(Q(0))
        with self.assertRaises(ValueError):z.Interval(Q(2),Q(1))


if __name__=='__main__':unittest.main()
