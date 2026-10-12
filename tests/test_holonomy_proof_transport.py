"""Independent GF(2) geometry controls for oriented, nonflat proof transport."""
from itertools import product
import random
import unittest

from observational_succ.holonomy_proof_transport import (
    FrameTransportError, GL2, IDENTITY, HORIZONTAL, VERTICAL,
    ALL_VECTORS, SquareConnection, certify_path_blind,
    nonflat_square, flat_square, holonomy_proof_demo,
)


def all_gl2_matrices():
    return tuple(GL2(*bits) for bits in product((0,1),repeat=4)
                 if (bits[0]*bits[3]+bits[1]*bits[2])%2==1)


def raw_mul(A,B):
    """Independent list-algebra matrix multiplication over GF(2)."""
    a=[[A.a,A.b],[A.c,A.d]]
    b=[[B.a,B.b],[B.c,B.d]]
    v=[[sum(a[i][k]*b[k][j] for k in (0,1))%2
        for j in (0,1)] for i in (0,1)]
    return GL2(v[0][0],v[0][1],v[1][0],v[1][1])


def inverse_brute(A):
    for B in all_gl2_matrices():
        if raw_mul(A,B)==IDENTITY and raw_mul(B,A)==IDENTITY:
            return B
    raise AssertionError("No inverse for declared GL2")


def independent_pathblind(connection, truth):
    groups={}
    sources=ALL_VECTORS
    for path in ("RU","UR"):
        for source in sources:
            report=connection.local_reading(source,path)
            groups.setdefault(report,set()).add(truth[2*source[0]+source[1]])
    return all(len(labels)==1 for labels in groups.values())


class GF2ConnectionTests(unittest.TestCase):
    def test_group_cardinality_identity_inverse_composition_and_associativity(self):
        group=all_gl2_matrices()
        self.assertEqual(len(group),6)
        for a in group:
            inv=a.inverse()
            self.assertEqual(inv,inverse_brute(a))
            self.assertEqual(a.then(inv),IDENTITY)
            self.assertEqual(inv.then(a),IDENTITY)
            for v in ALL_VECTORS:
                self.assertEqual(a.then(inv).apply(v),v)
                self.assertEqual(a.apply(v),(
                    (a.a*v[0]+a.b*v[1])%2,
                    (a.c*v[0]+a.d*v[1])%2))
            for b in group:
                self.assertEqual(a.then(b),raw_mul(b,a))
                for c in group:
                    self.assertEqual(a.then(b).then(c),
                                     a.then(b.then(c)))

    def test_shears_noncommute_and_relative_holonomy_has_order_three(self):
        connection=nonflat_square()
        result=connection.audit_square()
        self.assertFalse(result["flat"])
        self.assertNotEqual(connection.path("RU"),connection.path("UR"))
        W=connection.holonomy()
        self.assertFalse(W.is_identity)
        self.assertNotEqual(W.then(W),IDENTITY)
        self.assertEqual(W.then(W).then(W),IDENTITY)
        self.assertEqual(
            connection.path("UR"),W.then(connection.path("RU")))
        for source in ALL_VECTORS:
            for direction in ("RU","UR"):
                local=connection.local_reading(source,direction)
                reconstructed=connection.restore_source(local,direction)
                self.assertEqual(reconstructed,source)

    def test_flat_calibration_and_every_binary_claim_invariant(self):
        field=flat_square()
        self.assertTrue(field.audit_square()["flat"])
        self.assertEqual(field.path("RU"),field.path("UR"))
        for truth in product((0,1),repeat=4):
            certificate=certify_path_blind(field,truth,target_id="X")
            self.assertTrue(certificate.invariant_under_holonomy)
            self.assertIsNone(certificate.collision)
            for v in ALL_VECTORS:
                for path in ("RU","UR"):
                    y=field.local_reading(v,path)
                    self.assertEqual(
                        certificate.decode(y,source_id=field.source_id,
                                           basis_id=field.basis_id,
                                           target_id="X"),truth[2*v[0]+v[1]])

    def test_exact_holonomy_invariants_vs_independent_output_fiber_oracle(self):
        field=nonflat_square()
        W=field.holonomy()
        valid=[]
        for truth in product((0,1),repeat=4):
            result=certify_path_blind(field,truth,target_id="target")
            self.assertEqual(result.invariant_under_holonomy,
                             independent_pathblind(field,truth))
            self.assertEqual(result.invariant_under_holonomy,
                             all(truth[2*v[0]+v[1]]==
                                 truth[2*W.apply(v)[0]+W.apply(v)[1]]
                                 for v in ALL_VECTORS))
            if result.invariant_under_holonomy:
                valid.append(truth)
                for v in ALL_VECTORS:
                    for path in ("RU","UR"):
                        y=field.local_reading(v,path)
                        self.assertEqual(result.decode(
                            y,source_id=field.source_id,
                            basis_id=field.basis_id,
                            target_id="target"),truth[2*v[0]+v[1]])
            else:
                (p,x),(q,y)=result.collision
                self.assertEqual(field.local_reading(x,p),
                                 field.local_reading(y,q))
                self.assertNotEqual(truth[2*x[0]+x[1]],truth[2*y[0]+y[1]])
        self.assertEqual(len(valid),4)
        self.assertIn((1,0,0,0),valid)
        self.assertNotIn((0,0,1,1),valid)

    def test_independent_random_nonflat_square_holonomy_targets(self):
        elements=all_gl2_matrices()
        rng=random.Random(130173)
        for case in range(150):
            sample=rng.sample(elements,4)
            sq=SquareConnection(*sample,source_id=f"source{case}",
                                 basis_id="declared-orientation")
            sq.audit_square()
            for bits in product((0,1),repeat=4):
                certificate=certify_path_blind(sq,bits,target_id="T")
                expected=independent_pathblind(sq,bits)
                self.assertEqual(certificate.invariant_under_holonomy,expected)
                if not expected:
                    self.assertIsNotNone(certificate.collision)
                else:
                    for source in ALL_VECTORS:
                        for path in ("RU","UR"):
                            observed=sq.local_reading(source,path)
                            self.assertEqual(certificate.decode(
                                observed,source_id=sq.source_id,
                                basis_id=sq.basis_id,target_id="T"),
                                bits[2*source[0]+source[1]])

    def test_all_binary_claims_decode_when_path_receipt_is_supplied(self):
        field=nonflat_square()
        for labels in product((0,1),repeat=4):
            for path in ("RU","UR"):
                for source in ALL_VECTORS:
                    local=field.local_reading(source,path)
                    reconstructed=field.restore_source(local,path)
                    self.assertEqual(labels[2*reconstructed[0]+reconstructed[1]],
                                     labels[2*source[0]+source[1]])
        with self.assertRaises(FrameTransportError):
            field.path("unrecorded")
        with self.assertRaises(FrameTransportError):
            field.restore_source((0,0),"wrong-path")

    def test_wrong_or_forged_path_metadata_and_nonunit_frames_rejected(self):
        field=nonflat_square()
        target=(1,0,0,0)
        cert=certify_path_blind(field,target,target_id="zero")
        self.assertTrue(cert.invariant_under_holonomy)
        for args in (dict(source_id="forged",basis_id=field.basis_id,
                          target_id="zero"),
                     dict(source_id=field.source_id,basis_id="flipped",
                          target_id="zero"),
                     dict(source_id=field.source_id,basis_id=field.basis_id,
                          target_id="parity")):
            with self.assertRaises(FrameTransportError):
                cert.decode((0,0),**args)
        for mat in ((0,0,0,0),(1,1,1,1),(0,1,0,0),(1,0,0,0)):
            with self.assertRaises(FrameTransportError):
                GL2(*mat)
        for mat in ((True,0,0,1),(1,0,0,2)):
            with self.assertRaises(FrameTransportError):
                GL2(*mat)
        with self.assertRaises(FrameTransportError):
            field.restore_source((True,0),"RU")
        with self.assertRaises(FrameTransportError):
            certify_path_blind(field,("0","1","1","0"),target_id="not-gf2")

    def test_machine_receipt(self):
        x=holonomy_proof_demo()
        self.assertEqual(x["status"],"EXACT_NONFLAT_PROOF_TRANSPORT_GALOIS_GF2")
        self.assertFalse(x["nonflat_holonomy_is_identity"])
        self.assertEqual(x["holonomy_order"],3)
        self.assertTrue(x["path_aware_source_recovered"])
        self.assertFalse(x["first_bit_path_blind_decodable"])
        self.assertTrue(x["is_zero_path_blind_decodable"])
        self.assertEqual(x["invariant_binary_predicates_out_of_16"],4)
        self.assertTrue(x["flat_all_16_predicates_path_blind_decodable"])
        self.assertFalse(x["connection_physically_measured"])
        self.assertFalse(x["quantum_phase_or_RH_theorem_claimed"])


if __name__=="__main__":
    unittest.main()
