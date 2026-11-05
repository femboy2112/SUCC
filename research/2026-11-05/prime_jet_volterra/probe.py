"""Exact boundary-kernel calibration; actual prime weights are diagnostics."""
from pathlib import Path
import hashlib
import json
import math
import sympy as s

x, y, z = s.symbols('x y z', real=True)


def exact_checks():
    records = []
    for d, a in [(s.Rational(1, 5), s.Rational(4, 5)),
                 (s.Rational(2, 7), s.Rational(5, 7)),
                 (s.Rational(3, 11), s.Rational(10, 11))]:
        D = d+a
        for degree in (1, 2, 4):
            f = x**degree*(D-x)
            p = s.diff(f, x)
            q = -p.subs(x, D-y)
            direct = s.integrate(f*f.subs(x, x+a), (x, 0, d))
            kernel = s.integrate(s.integrate((d-x-y)*p*q,
                                             (y, 0, d-x)), (x, 0, d))
            energy = s.integrate(p*p, (x, 0, D))
            margin = s.factor(d**4*energy**2/12-4*direct**2)
            assert s.simplify(direct-kernel) == 0 and margin >= 0
            records.append(dict(delta=str(d), a=str(a), degree=degree,
                                autocorrelation=str(direct), derivative_energy=str(energy),
                                squared_bound_margin=str(margin)))
    for d, e in [(s.Rational(1, 5), s.Rational(1, 3)),
                 (s.Rational(2, 7), s.Rational(2, 7)),
                 (s.Rational(3, 13), s.Rational(5, 11))]:
        inner = s.integrate(z*(d-z)*(e-z), (z, 0, d))
        assert inner == d**3*(2*e-d)/12
    # Two disjoint polynomial packets: signs and imaginary phase.
    b = x*(1-x)
    mass = s.integrate(b*b, (x, 0, 1))
    cost = 2*s.integrate(s.diff(b, x)**2, (x, 0, 1))
    controls = []
    for phase in (s.Integer(1), s.Integer(-1), s.I):
        jet = -2*s.re(phase)*mass
        assert jet**2 <= cost**2/12
        controls.append(dict(phase=str(phase), jet=str(jet), energy=str(cost)))
    assert [v['jet'] for v in controls] == ['-1/15', '1/15', '0']
    return records, controls


def diagnostic(D, fake=False):
    # Closed-form polynomial f=x(D-x), not a numerical positivity certificate.
    jets = [(math.log(p), math.log(p)/math.sqrt(p))
            for p in (2, 3) if math.log(p) < D]
    if fake:
        jets.append((math.log(2.5), math.log(2.5)/math.sqrt(2.5)))
    jets = [(a, w) for a, w in jets if a < D]
    ds = [(D-a, w) for a, w in jets]
    c2 = sum(w*v*min(d,e)**3*(2*max(d,e)-min(d,e))/12
             for d,w in ds for e,v in ds)
    energy = D**3/3
    # Independent analytic autocorrelation integral for x(D-x).
    g = lambda d: d**3*(5*D**2-5*D*d+d*d)/30
    total = -2*sum(w*g(d) for d,w in ds)
    bound = math.sqrt(c2)*energy
    assert abs(total) <= bound + 1e-14
    return dict(D=D, fake_source=fake, active_shifts=[a for a,w in jets],
                joint_C=math.sqrt(c2), separate_C=sum(w*d*d/math.sqrt(12) for d,w in ds),
                jet=total, bound=bound, scope='binary64 diagnostic; not interval certified')


def main():
    records, controls = exact_checks()
    result = dict(parent='a2905c9e1770fea519193839433bdca4bd29336f',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  exact_records=records, exact_sign_controls=controls,
                  exact_cross_kernel_checks=3,
                  diagnostics=[diagnostic(D, fake) for D in (.8, 1.2, 1.3)
                               for fake in (False, True)],
                  verdict='local analytic bound only; RH OPEN')
    target=Path(__file__).with_name('FINITE_RECEIPT.json')
    if '--verify' in __import__('sys').argv:
        assert json.loads(target.read_text()) == result
        print('PASS: 9 exact polynomial probes, 3 cross-kernels, 3 sign controls, 6 diagnostics')
    else:
        target.write_text(json.dumps(result, indent=2)+'\n')
        print('wrote', target)


if __name__ == '__main__':
    main()
