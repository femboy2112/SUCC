"""Actual existing-category integration, never a mock of the upstream core."""
import importlib.util
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]/'research'/'2026-11-01'/'categorical_sheet_transport'
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    return module
m=load('cst_adapter_arithmetic','sheet_transport.py')
a=load('cst_existing_path_adapter','path_adapter.py')
HAS_CORE=importlib.util.find_spec('observational_succ') is not None

@unittest.skipUnless(HAS_CORE,'complete SUCC checkout not mounted; actual category integration not run')
class ExistingCategoryIntegration(unittest.TestCase):
    def setUp(self):self.adapter=a.build_path_adapter(4,m);self.cat=self.adapter.category
    def test_identity_and_actual_source_word(self):
        self.assertEqual(len(self.cat.objects),5)
        self.assertTrue(any(len(self.cat.pretty_path(f))==4 for x in self.cat.objects for f in self.cat.hom(0,x)))
        for x in self.cat.objects:self.assertEqual(self.adapter.image(self.cat.identity(x)),m.Monomial(self.adapter.Q))
        for x in self.cat.objects:
            for f in self.cat.hom(0,x):
                length=len(self.cat.pretty_path(f))
                self.assertEqual(self.adapter.image(f),m.propagator(length,self.adapter.Q))
    def test_composition_preserves_source_order(self):
        for x in self.cat.objects:
            for y in self.cat.objects:
                for z in self.cat.objects:
                    for f in self.cat.hom(x,y):
                        for g in self.cat.hom(y,z):
                            self.assertEqual(self.adapter.image(self.cat.compose(g,f)),self.adapter.image(g).compose(self.adapter.image(f)))
    def test_fourier_natural_transformation(self):
        for x in self.cat.objects:
            for y in self.cat.objects:
                for f in self.cat.hom(x,y):
                    self.assertEqual(self.adapter.fourier_image(f),self.adapter.image(f).fourier())
if __name__=='__main__':unittest.main()
