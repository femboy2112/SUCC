"""Exact inertial common-carrier top and hostile controls; float trig diagnostic."""
import importlib.util
import math
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
from observational_succ.hopf_source_exact import H, ONE, I, J, K
P=Path(__file__).resolve().parents[1]/'research'/'2026-11-03'/'inertial_gyro'/'gyroscope.py'
S=importlib.util.spec_from_file_location('succ_gyro',P)
g=importlib.util.module_from_spec(S);sys.modules[S.name]=g;S.loader.exec_module(g)


def qx():return H(F(3,5),F(4,5),0,0)
def qy():return H(F(5,13),0,F(12,13),0)
def qz():return H(F(3,5),0,0,F(4,5))


class SourceCarrier(unittest.TestCase):
    def test_original_four_poles_and_literal_zero(self):
        self.assertEqual(g.original_source(1),F(47,15))
        u=g.original_states(64)
        self.assertEqual(u[0],0)
        for n in range(1,65):
            self.assertEqual(u[n],16*u[n-1]+g.original_source(n))
            self.assertEqual(u[n].denominator%2,1)

    def test_original_e_receiver_exact_cross_check(self):
        P2=Path(__file__).resolve().parents[1]/'research'/'2026-11-03'/'stationary_e2_gamma'/'stationary_e_observer.py'
        spec=importlib.util.spec_from_file_location('succ_stationary_cross',P2)
        import sys
        old=importlib.util.module_from_spec(spec);sys.modules[spec.name]=old
        spec.loader.exec_module(old)
        U=g.original_states(24)
        for n in range(25):
            self.assertEqual(U[n],old.observer_at(n).original_U)

    def test_source_attested_frame_free_receipts(self):
        U=g.original_states(18)
        for h in (1,2,16):
            for n in (0,1,3,8,16):
                a=g.source_phase_receipt(n,U[n],h)
                b=g.source_phase_receipt(n,U[n],h)
                self.assertEqual(a,b)
                self.assertEqual(a['fraction'],(h*U[n])%1)
        with self.assertRaises(ValueError):g.source_phase_receipt(4,U[4]+F(1,73))

    def test_spinor_carry_never_forget_parity(self):
        for h in (1,2,3,16):
            for carry in (-3,-2,-1,0,1,2,3):
                base=F(2,7)
                sign=g.spinor_carry_sign(h,carry)
                a=g.spinor_lift(base,h)
                b=g.spinor_lift(base+carry,h)
                self.assertEqual(g.source_phase(base,h),g.source_phase(base+carry,h))
                self.assertEqual((b-a)%2,(0 if sign==1 else 1))


class ExactInertialFrames(unittest.TestCase):
    def test_noncommuting_orthogonal_frame_carrier(self):
        self.assertEqual(qx().norm2(),1)
        self.assertEqual(qy().norm2(),1)
        self.assertNotEqual(qx()*qy(),qy()*qx())
        self.assertEqual(qx()*qx().conj(),ONE)

    def test_reject_invalid_rotor_and_wrong_mark(self):
        with self.assertRaises(ValueError):g.EFrame('bad',H(2))
        with self.assertRaises(ValueError):g.EFrame('gamma-gain-is-not-unit',H(F(1,2),F(1,2)))
        with self.assertRaises(ValueError):g.EFrame('bad',ONE,mark=F(1,5))
        with self.assertRaises(ValueError):g.EFrame('bad',ONE,passport='other source')

    def test_static_frame_groupoid_exact_composition(self):
        A=g.EFrame('A',ONE);B=g.EFrame('B',qx());C=g.EFrame('C',qy())
        self.assertEqual(g.link(B,C)*g.link(A,B),g.link(A,C))
        self.assertEqual(g.gauge_holonomy(A,B,C),ONE)
        self.assertEqual(g.gauge_holonomy(C,A,B),ONE)
        self.assertEqual(g.link(B,A),g.link(A,B).conj())

    def test_exhaustive_frame_rotation_preserves_exact_dot(self):
        vec=[I,J,K,I+J,(I-J).scale(F(3,5))]
        for rotor in (ONE,qx(),qy(),qz(),qx()*qy(),qy()*qx()):
            for a in vec:
                for b in vec:
                    u=g.rotate(rotor,a);v=g.rotate(rotor,b)
                    self.assertEqual((u*v).a,(a*b).a)
                    self.assertEqual(u.norm2(),a.norm2())

    def test_R_is_exact_special_orthogonal_without_euler_angles(self):
        for rotor in (ONE,qx(),qy(),qz(),qx()*qy(),qy()*qx()):
            R=g.rotation_matrix(rotor)
            for i in range(3):
                for j in range(3):
                    self.assertEqual(sum(R[k][i]*R[k][j] for k in range(3)),F(i==j))
            self.assertEqual(sum(R[0][i]*(R[1][(i+1)%3]*R[2][(i+2)%3]-
                 R[1][(i+2)%3]*R[2][(i+1)%3]) for i in range(3)),1)

    def test_source_phase_gram_exact_mod1_is_frame_independent(self):
        U=g.original_states(30)
        for h in (1,3,16):
            for n,m in ((0,1),(2,7),(7,12),(24,30)):
                d=g.gram_difference_mod1(U[n],U[m],h)
                self.assertEqual(d,(h*(U[n]-U[m]))%1)

    def test_three_source_linked_observers_agree_on_gyro_coherence(self):
        U=g.original_states(36)[:36]
        fr=[g.EFrame('A',ONE),g.EFrame('B',qx()),g.EFrame('C',qy())]
        for h in (1,2,3,16):
            expected=g.gyro_energy(U,h)
            for stride in (1,2,3):
                chosen=[fr[(i*stride)%3] for i in range(len(U))]
                for ref in (0,1,2):
                    m=g.common_frame_mean(U,chosen,h,ref)
                    self.assertAlmostEqual(sum(v*v for v in m),expected,places=11)

    def test_naive_time_varying_frame_creates_false_haar(self):
        # Physical orbit all at phase 0 (maximally coherent), camera basis toggles.
        base=[I for _ in range(8)]
        frames=[g.EFrame('E0',ONE) if n%2==0 else g.EFrame('E1',K)
                for n in range(8)]
        measured=[g.rotate(f.rotor,v) for f,v in zip(frames,base)]
        naive=sum((q.b for q in measured),F())/8
        self.assertEqual(naive,0)
        corrected=[g.transport(v,f,frames[0]) for v,f in zip(measured,frames)]
        self.assertEqual(corrected,base)
        self.assertEqual(sum((q.b for q in corrected),F())/8,1)

    def test_quaternion_frame_twirling_false_uniformity(self):
        for v in (I,J,K,I+J,(I-J+K).scale(F(1,3))):
            self.assertEqual(g.fake_frame_twirl_vector(v),H())
        # Haar twirl of a coherent top does not say the original top is Haar.

    def test_antipodal_mean_has_no_gimbal_singularity(self):
        U=[F(0),F(1,2)]
        self.assertLess(g.gyro_energy(U,1),1e-25)
        self.assertAlmostEqual(g.spin_purity([g.spin_vector(q) for q in U]),.5,places=12)


class OriginalSourceFiniteCertificates(unittest.TestCase):
    def test_source_specific_exact_sector_bounds(self):
        U=g.original_states(1023)
        for A,M,h in ((64,16,1),(128,64,2),(256,64,3),(512,256,16)):
            values=U[A:2*A]
            b=g.exact_gyro_upper_bound(values,h,M)
            numeric=g.gyro_energy(values,h)**.5
            self.assertLessEqual(numeric,float(b)+1e-10)

    def test_wrong_source_moment_rejected(self):
        U=g.original_states(15)
        with self.assertRaises(ValueError):g.source_phase_receipt(5,U[5]+F(1,3))

    def test_exact_marked_source_constructor_not_fake_data(self):
        u=g.original_states(35)[:35]
        for h in (1,2,16):
            self.assertAlmostEqual(g.source_selected_gyro_energy(35,h),g.gyro_energy(u,h),places=12)
        with self.assertRaises(ValueError):g.source_selected_gyro_energy(0)

    def test_gyro_spin_purity_is_weyl_energy_plus_half(self):
        for phases in ([F(0)]*16,[F(j,16) for j in range(16)],
                       g.original_states(32)[:32]):
            vectors=[g.spin_vector(p) for p in phases]
            energy=g.gyro_energy(phases)
            self.assertAlmostEqual(2*g.spin_purity(vectors)-1,energy,places=12)

if __name__=='__main__':unittest.main()


class GyroFejerBridge(unittest.TestCase):
    def test_original_gamma_purity_error_decreases_inverse_horizon(self):
        self.assertEqual(g.original_gamma_gyro_purity_error(1,1),F(561,392))
        self.assertEqual(g.original_gamma_gyro_purity_error(32,3),F(1683,12544))
        for n in (8,16,32,64):
            self.assertLess(g.original_gamma_gyro_purity_error(2*n,1),
                            g.original_gamma_gyro_purity_error(n,1))

    def test_gamma_rational_finite_complete_gyro_error(self):
        P2=Path(__file__).resolve().parents[1]/'research'/'2026-11-03'/'stationary_e2_gamma'/'stationary_e_observer.py'
        spec=importlib.util.spec_from_file_location('succ_gamma_complete_cross',P2)
        old=importlib.util.module_from_spec(spec)
        sys.modules[spec.name]=old
        spec.loader.exec_module(old)
        for N in (16,32,64):
            u=g.original_states(N-1)
            alpha=old.source_alpha_B(N+8)
            completed=[16**n*alpha for n in range(N)]
            for h in (1,3):
                x=g.gyro_energy(u,h)
                y=g.gyro_energy(completed,h)
                self.assertLess(abs((1+x)/2-(1+y)/2),
                                float(g.original_gamma_gyro_purity_error(N,h))+1e-10)

    def test_fejer_gram_and_frame_invariance_float(self):
        U=g.original_states(64)[:64]
        frames=[g.EFrame('A',ONE),g.EFrame('B',qx()),g.EFrame('C',qy())]
        for M in (4,8,16,32):
            baseline=g.gyro_fejer_excess(U,M)
            shifted=g.gyro_fejer_excess(U,M,[frames[i%3] for i in range(len(U))])
            self.assertAlmostEqual(baseline,shifted,places=12)
            direct=sum((1-2*h/M)*g.gyro_energy(U,h) for h in range(1,M//2))
            self.assertAlmostEqual(baseline,direct,places=12)

    def test_exact_source_histogram_bounds_gyro_invariant(self):
        U=g.original_states(128)
        for A,M in ((32,8),(64,16),(128,32)):
            phases=U[:A]
            d=g.exact_histogram_fejer_majorant(phases,M)
            self.assertEqual(d['E_exact'],F(M*sum(x*x for x in d['counts']),A*A))
            self.assertLessEqual(g.gyro_fejer_excess(phases,M),
                                 float(d['gyro_excess_upper'])+1e-10)

    def test_gimbal_fake_haar_and_finite_twirl_not_a_source_proof(self):
        coherent=[F(0)]*32
        top=g.gyro_fejer_excess(coherent,16)
        self.assertEqual(top,3.5)
        self.assertAlmostEqual(g.gyro_energy(coherent),1)
        self.assertEqual(g.fake_frame_twirl_vector(I),H())

class ExactRelayTopology(unittest.TestCase):
    def test_three_Es_accept_source_linked_triangle(self):
        A=g.EFrame('A',ONE);B=g.EFrame('B',qx());C=g.EFrame('C',qy())
        ab=g.emit_link(A,B);bc=g.emit_link(B,C);ca=g.emit_link(C,A)
        self.assertEqual(g.relay_triangle(ab,bc,ca),ONE)
        with self.assertRaises(ValueError):
            g.relay_triangle(bc,ab,ca)

    def test_central_minus_one_is_detected_not_gimbal_lock(self):
        A=g.EFrame('A',ONE);B=g.EFrame('B',qx());C=g.EFrame('C',qy())
        ab=g.emit_link(A,B);bc=g.emit_link(B,C);ca=g.emit_link(C,A)
        mutated=g.LinkReceipt(ca.start,ca.stop,-ca.rotor)
        self.assertEqual(g.relay_triangle(ab,bc,mutated,require_spin=False),-ONE)
        with self.assertRaises(ValueError):g.relay_triangle(ab,bc,mutated,require_spin=True)
        self.assertEqual(g.rotate(-ONE,I),I)

    def test_bogus_relay_fails_source_or_cocycle(self):
        A=g.EFrame('A',ONE);B=g.EFrame('B',qx());C=g.EFrame('C',qy())
        ab=g.emit_link(A,B);bc=g.emit_link(B,C);ca=g.emit_link(C,A)
        wrong=g.LinkReceipt(ca.start,ca.stop, qz()*ca.rotor)
        with self.assertRaises(ValueError):g.relay_triangle(ab,bc,wrong,require_spin=False)
        with self.assertRaises(ValueError):g.LinkReceipt('C','A',ONE,passport='changed forcing')

class SourceSpinTorusNoGo(unittest.TestCase):
    def test_original_spin2_marks_are_abelian_exact(self):
        for h in (1,2,3,16):
            marks=[g.original_spin2_mark(n,h) for n in range(16)]
            for a in marks:
                for b in marks:
                    self.assertEqual(a*b,b*a)
                    self.assertEqual(a.commutator(b),g.Spin2Mark(0))

    def test_spin2_central_minus_one_invisible_to_bloch_phase(self):
        self.assertNotEqual(g.Spin2Mark(0),g.Spin2Mark(1))
        self.assertEqual(g.Spin2Mark(0).bloch_phase(),g.Spin2Mark(1).bloch_phase())
        self.assertEqual(g.Spin2Mark(F(1,7))*g.Spin2Mark(F(13,7)),g.Spin2Mark(0))

    def test_observer_noncommuting_rotations_are_external_to_source_torus(self):
        a=qx();b=qy()
        self.assertNotEqual(a*b,b*a)
        actual=g.original_spin2_mark(8,1)
        other=g.original_spin2_mark(15,1)
        self.assertEqual(actual.commutator(other),g.Spin2Mark(0))
        # A change of observer reference does NOT change the source's
        # formal abelian phase path or create a source-specific mixing gap.

class GeneralInertialRelayDescent(unittest.TestCase):
    def test_multinode_noncommuting_E_frame_consensus(self):
        frames=[g.EFrame('A',ONE),g.EFrame('B',qx()),
                g.EFrame('C',qy()),g.EFrame('D',qx()*qy())]
        relays=[g.emit_link(frames[i],frames[j]) for i,j in
                ((0,1),(1,2),(2,3),(3,0),(0,2),(1,3))]
        agreed=g.e_network_consensus([f.name for f in frames],relays)
        self.assertEqual(agreed,{f.name:f.rotor for f in frames})
        self.assertEqual(g.e_network_consensus([f.name for f in frames],relays,root='B')['B'],ONE)

    def test_rational_E_network_source_holonomy_mutation_fails(self):
        frames=[g.EFrame('A',ONE),g.EFrame('B',qx()),
                g.EFrame('C',qy()),g.EFrame('D',qx()*qy())]
        edges=[(0,1),(1,2),(2,3),(3,0),(0,2)]
        relays=[g.emit_link(frames[i],frames[j]) for i,j in edges]
        e=relays[-1]
        bad=g.LinkReceipt(e.start,e.stop,-e.rotor)
        with self.assertRaises(ValueError):g.e_network_consensus([x.name for x in frames],relays[:-1]+[bad])
        # Projection to SO3 loses the -1 spinor holonomy, exactly as expected.
        self.assertEqual(len(g.e_network_consensus([x.name for x in frames],relays[:-1]+[bad],require_spin=False)),4)
        e2=relays[-1]
        wrong=g.LinkReceipt(e2.start,e2.stop,qz()*e2.rotor)
        with self.assertRaises(ValueError):g.e_network_consensus([x.name for x in frames],relays[:-1]+[wrong],require_spin=False)

    def test_network_cover_missing_E_is_rejected(self):
        a=g.EFrame('A',ONE);b=g.EFrame('B',qx())
        with self.assertRaises(ValueError):g.e_network_consensus(['A','B','C'],[g.emit_link(a,b)])
        with self.assertRaises(ValueError):g.e_network_consensus(['A','A'],[])
        with self.assertRaises(ValueError):g.e_network_consensus(['A'],[],root='Z')
