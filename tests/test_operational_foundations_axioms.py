"""Finite exact controls for operational foundation proposal, not physical data."""
import importlib.util
import unittest
from pathlib import Path

P=Path(__file__).resolve().parents[1]/"research"/"2026-11-04"/"operational_foundations"/"operational_probe.py"
spec=importlib.util.spec_from_file_location("operational_probe",P)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class OperationalAxiomControls(unittest.TestCase):
    def setUp(self):
        self.occlusion=m.DeclaredSource('synthetic-occlusion',2,(
            m.Instrument('see',('red-box','red-box'),(0,1)),
            m.Instrument('tag',('original','replacement'),(0,1),2),
        ))

    def test_permanence_is_toolkit_relative(self):
        s=self.occlusion
        self.assertEqual(s.observation_classes(('see',),4),((0,1),))
        self.assertEqual(s.observation_classes(('see','tag'),1),((0,),(1,)))
        self.assertEqual(s.observation_classes(('see','tag'),1,budget=1),((0,1),))
        self.assertEqual(s.observation_classes(('see','tag'),1,budget=2),((0,),(1,)))

    def test_past_witness_retained_when_models_revised(self):
        h=(('src','probe1','value1'),)
        h2=m.append_witness(h,'src','probe2','value2')
        self.assertEqual(h,h2[:-1])
        self.assertEqual(len(h),1)
        with self.assertRaises(m.ContractError):m.append_witness(h,'','probe2','value2')

    def test_composition_and_prefix_refinement(self):
        s=m.DeclaredSource('finite-switch',2,(
            m.Instrument('flip',('before0','before1'),(1,0)),
            m.Instrument('look',('0','1'),(0,1)),
        ))
        words=((),('flip',),('look',),('flip','look'))
        for initial in (0,1):
            for a in words:
                for b in words:
                    for c in words:
                        ra,xa=s.execute(initial,a)
                        rb,xb=s.execute(xa,b)
                        rc,xc=s.execute(xb,c)
                        self.assertEqual(s.execute(initial,a+b+c),(ra+rb+rc,xc))
        s=self.occlusion
        self.assertEqual(s.observed_initials(('see',),('red-box',)),(0,1))
        self.assertEqual(s.observed_initials(('see','tag'),('red-box','original')),(0,))

    def test_induction_not_from_finite_sample(self):
        for k in (0,1,2,8,32,255):
            a,b=m.bounded_induction_countermodel(k)
            self.assertEqual(a[:k+1],b[:k+1])
            self.assertNotEqual(a[k+1],b[k+1])

    def test_classical_measurement_order_not_quantum_specific(self):
        s=m.DeclaredSource('classical-bit-reset',2,(
            m.Instrument('write0',('ok','ok'),(0,0)),
            m.Instrument('write1',('ok','ok'),(1,1)),
            m.Instrument('read',('0','1'),(0,1)),
        ))
        self.assertEqual(s.trace(0,('write0','write1','read')),('ok','ok','1'))
        self.assertEqual(s.trace(0,('write1','write0','read')),('ok','ok','0'))

    def test_zero_boundary_no_mixing(self):
        s=m.DeclaredSource('pure16-zero',2,(m.Instrument('step',('0','1'),(0,1)),))
        self.assertEqual(s.trace(0,('step',)*6),('0',)*6)

    def test_invalid_claims_fail_closed(self):
        with self.assertRaises(m.ContractError):
            m.DeclaredSource('x',2,(m.Instrument('a',('x','x'),(0,3)),))
        with self.assertRaises(m.ContractError):self.occlusion.trace(3,('see',))
        with self.assertRaises(m.ContractError):self.occlusion.observed_initials(('see',),('x','y'))
        with self.assertRaises(m.ContractError):self.occlusion.signature(0,('fake',),1)

    def test_visible_identity_is_not_source_attestation(self):
        s=self.occlusion
        self.assertEqual(s.trace(0,('see',)),s.trace(1,('see',)))
        self.assertNotEqual(s.trace(0,('tag',)),s.trace(1,('tag',)))


if __name__=="__main__":unittest.main()
