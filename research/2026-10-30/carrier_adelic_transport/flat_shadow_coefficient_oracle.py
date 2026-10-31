"""Independent linear-coefficient oracle for the flat-source shadow.

The constructor works with formal source symbols x_1,x_2,... and a moving
terminal horizon. It does not construct the forcing from F1. Exact rational
evaluation then compares it with the separately implemented repository API.
The analytic continuation and exponential-character inequality remain paper
arguments; this oracle checks their algebraic and positive-budget inputs.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import importlib.util
import json
import unittest

_here=Path(__file__).resolve()
_candidates=(_here.with_name('flat_shadow.py'),
             _here.parents[2]/'SUCC/research/2026-10-30/carrier_adelic_transport/flat_shadow.py')
ROOT_SOURCE=next((p for p in _candidates if p.is_file()),None)
if ROOT_SOURCE is None:
    raise FileNotFoundError('Place this oracle beside flat_shadow.py or in the audit workspace.')
spec=importlib.util.spec_from_file_location('root_flat_shadow',ROOT_SOURCE)
root=importlib.util.module_from_spec(spec)
spec.loader.exec_module(root)


def combine(left,right,scale=F(1)):
    out=dict(left)
    for t,c in right.items():
        out[t]=out.get(t,F(0))+scale*c
        if not out[t]:
            del out[t]
    return out


def initial_polynomial(radix,prefix,depth):
    return {t:F(radix)**(-t) for t in range(1,prefix+depth+1)}


def residual_polynomial(n,radix,prefix,depth):
    # Terminal source index remains fixed, then advances by TWO per frame.
    last=prefix+depth+2*max(0,n-prefix)
    return {t:F(radix)**(n-t) for t in range(n+1,last+1)}


def state_polynomial(n,radix,prefix,depth):
    initial={t:c*radix**n for t,c in initial_polynomial(radix,prefix,depth).items()}
    return combine(initial,residual_polynomial(n,radix,prefix,depth),F(-1))


def forcing_polynomial(n,radix,prefix,depth):
    return combine(state_polynomial(n,radix,prefix,depth),
                   state_polynomial(n-1,radix,prefix,depth),F(-radix))


def evaluate(poly,source):
    return sum((c*source(t) for t,c in poly.items()),F(0))


def grouped_source(n,u=F(0)):
    a=F(8*n-7)+u
    return F(6)/(a*(a+3))+F(4)/(a*(a+4))+F(5)/(a*(a+5))


class CoefficientOracle(unittest.TestCase):
    def test_formal_zero_and_prefix(self):
        for b in (2,3,16,31):
            for m,k in ((0,1),(1,4),(7,2),(13,5)):
                self.assertEqual(state_polynomial(0,b,m,k),{})
                for n in range(1,m+1):
                    self.assertEqual(forcing_polynomial(n,b,m,k),{n:F(1)})

    def test_formal_terminal_support_and_weights(self):
        # No numerical source properties can conceal a coefficient error.
        for b in (2,3,16,31):
            for m,k in ((0,1),(2,3),(9,2)):
                for n in (m+1,m+2,m+7,m+19):
                    ell=k+n-m-1
                    expected={n:F(1),n+ell:-F(b)**(-ell),
                              n+ell+1:-F(b)**(-ell-1)}
                    self.assertEqual(forcing_polynomial(n,b,m,k),expected)

    def test_weighted_telescope_at_formal_level(self):
        for b in (2,16):
            for m,k in ((0,1),(3,5),(11,2)):
                for horizon in (1,m+1,m+8,m+23):
                    accumulated={}
                    for n in range(1,horizon+1):
                        accumulated=combine(accumulated,forcing_polynomial(n,b,m,k),F(b)**(-n))
                    difference=combine(initial_polynomial(b,m,k),accumulated,F(-1))
                    expected={t:c*F(b)**(-horizon)
                              for t,c in residual_polynomial(horizon,b,m,k).items()}
                    self.assertEqual(difference,expected)

    def test_compare_repository_api_on_fresh_shifted_cases(self):
        for m,k in ((0,2),(5,4),(12,3)):
            for u in (F(-7,8),F(2,9),F(7,10)):
                src=lambda t:grouped_source(t,u)
                q=evaluate(initial_polynomial(16,m,k),src)
                self.assertEqual(q,root.boundary(m,k,u))
                for n in (1,m+1,m+3,m+11,m+31):
                    self.assertEqual(evaluate(forcing_polynomial(n,16,m,k),src),root.shadow_source(n,m,k,u))
                    self.assertEqual(evaluate(state_polynomial(n,16,m,k),src),root.orbit(n,m,k,u))

    def test_positive_generic_source_controls(self):
        for src in (lambda n:F(1,n*n),lambda n:F(1,n*(n+1)),grouped_source):
            for b in (2,3,16):
                for m,k in ((0,1),(4,2),(9,3)):
                    for n in (m+1,m+4,m+16):
                        changed=evaluate(forcing_polynomial(n,b,m,k),src)
                        relative=(src(n)-changed)/src(n)
                        self.assertGreater(changed,0)
                        self.assertGreater(relative,0)
                        self.assertLess(relative,F(b)**(-k)*(1+F(1,b)))

    def test_nonincreasing_plateau_requires_nonstrict_bound(self):
        # Receipt for the hypothesis clarification in the review.
        src=lambda n:F(1) if n<=3 else F(9,n*n)
        changed=evaluate(forcing_polynomial(1,2,0,1),src)
        self.assertEqual(changed,F(1,4))
        self.assertEqual((src(1)-changed)/src(1),F(3,4))

    def test_rational_l1_budget_for_signed_failure(self):
        for m,k in ((0,1),(4,3),(15,2)):
            for u in (F(-7,8),F(0),F(7,8)):
                src=lambda t:grouped_source(t,u)
                cutoff=24
                finite=F(0)
                q=evaluate(initial_polynomial(16,m,k),src)
                h=q.denominator
                for n in range(1,cutoff+1):
                    d=evaluate(residual_polynomial(n,16,m,k),src)
                    state=evaluate(state_polynomial(n,16,m,k),src)
                    self.assertGreater(d,0)
                    self.assertLess(d,F(1,64*n*n))
                    self.assertEqual((h*(state+d)).denominator,1)
                    finite+=d
                # The proven bound d_n<1/(64 n²) gives tail <1/(64 cutoff).
                self.assertLess(finite+F(1,64*cutoff),F(1,32))

    def test_mutated_terminal_term_breaks_endpoint_certificate(self):
        b,m,k=16,3,2
        for n in (4,8,17):
            correct=forcing_polynomial(n,b,m,k)
            last=max(correct)
            mutated=dict(correct)
            mutated[last]=-mutated[last]
            self.assertNotEqual(correct,mutated)
            delta=evaluate(combine(mutated,correct,F(-1)),grouped_source)
            self.assertGreater(delta,0)
            # An omitted or flipped last coefficient is visible before limits.
            self.assertNotEqual(evaluate(mutated,grouped_source),root.shadow_source(n,m,k))

    def test_entire_remainder_is_not_equal_germ(self):
        m,k=4,3
        for spectral_s in (-8,-1,0,3):
            for u in (F(-2,3),F(0),F(4,5)):
                src=lambda t:grouped_source(t,u)
                first=F(0)
                for n in range(m+1,m+15):
                    defect=evaluate(forcing_polynomial(n,16,m,k),src)-src(n)
                    self.assertLess(defect,0)
                    first+=F(n)**(-spectral_s)*defect
                self.assertLess(first,0)


if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(CoefficientOracle)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    receipt={
        'tests_run':result.testsRun,
        'failures':len(result.failures),
        'errors':len(result.errors),
        'root_source':str(ROOT_SOURCE),
        'root_source_sha256':hashlib.sha256(ROOT_SOURCE.read_bytes()).hexdigest(),
        'oracle_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'authority':'Exact finite rational and formal coefficient checks; analytic limits established by paper proofs.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
