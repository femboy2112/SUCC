"""Independent exact integration controls for isolated prime hinges.

The triangle oracle uses bivariate monomials and simplex moments, not the
production response primitives. The derivative oracle uses direct integrals
and rational interpolatory quadrature, exact for the declared degree. SymPy
adds a separate symbolic Fourier/boundary check when installed.
"""
import importlib.util
import unittest
from fractions import Fraction as Q
from math import comb, factorial

from observational_succ import prime_wavefront_geometry as W
from observational_succ import suzuki_legendre_source as L
from observational_succ import source_weil_hierarchy as S


def _multiply(left, right):
    out = {}
    for (i, j), c in left.items():
        for (k, l), d in right.items():
            out[i+k, j+l] = out.get((i+k, j+l), Q()) + c*d
    return out


def _affine_polynomial(p, constant, s_coeff, t_coeff):
    result = {}
    power = {(0, 0): Q(1)}
    for c in p:
        for key, d in power.items():
            result[key] = result.get(key, Q()) + c*d
        power = _multiply(power, {(0, 0): constant, (1, 0): s_coeff, (0, 1): t_coeff})
    return result


def triangle_pair(a, b, p, q, *, kernel_power=1):
    """Independent exact integral over both triangles |x-y|>b.

    x=-a+b+s+t, y=-a+s, s,t>=0, s+t<=2a-b; then swap x,y.
    kernel_power=0 gives an active-indicator pair; =2 gives squared hinge.
    """
    delta = max(Q(), 2*a-b)
    def oriented(p, q):
        product = _multiply(_affine_polynomial(p, -a+b, 1, 1),
                            _affine_polynomial(q, -a, 1, 0))
        return sum((c*Q(factorial(i)*factorial(j+kernel_power),
                        factorial(i+j+kernel_power+2))*delta**(i+j+kernel_power+2)
                    for (i, j), c in product.items()), Q())
    return oriented(p, q)+oriented(q, p)


def direct_integral(p, left, right):
    return sum((Q(c)*(right**(i+1)-left**(i+1))/Q(i+1) for i, c in enumerate(p)), Q())


def direct_derivative(a, p, hinge, x):
    b, c = hinge.threshold, hinge.weight
    left = direct_integral(p, -a, x-b) if x-b > -a else Q()
    right = direct_integral(p, x+b, a) if x+b < a else Q()
    return c*(left-right)


def exact_interpolatory_integral(function, left, right, degree):
    """Integrate via exact Lagrange weights; no production polynomial calls."""
    if degree == 0:
        return (right-left)*function((left+right)/2)
    nodes = tuple(left+(right-left)*Q(i, degree) for i in range(degree+1))
    result = Q()
    for i, node in enumerate(nodes):
        basis = [Q(1)]
        denominator = Q(1)
        for j, other in enumerate(nodes):
            if i == j:
                continue
            new = [Q()]*(len(basis)+1)
            for k, c in enumerate(basis):
                new[k] -= other*c
                new[k+1] += c
            basis = new
            denominator *= node-other
        result += function(node)*direct_integral(basis, left, right)/denominator
    return result


def independent_derivative_gram(a, columns, hinges, output_modes=()):
    projection = []
    for p in columns:
        terms = []
        for n in output_modes:
            # Shared Legendre convention only; coefficients use triangle oracle.
            legendre = L.legendre_polynomial(n, a)
            coefficient = sum((h.weight*triangle_pair(a, h.threshold, legendre, p)
                               for h in hinges), Q())*Q(2*n+1)/(2*a)
            terms.append((coefficient, legendre))
        projection.append(terms)
    def derivative(i, x):
        raw = sum((direct_derivative(a, columns[i], h, x) for h in hinges), Q())
        return raw-sum((c*sum((k*v*x**(k-1) for k, v in enumerate(p) if k), Q())
                        for c, p in projection[i]), Q())
    breaks = sorted({-a, a} | {z for h in hinges for z in (h.threshold-a, a-h.threshold)
                              if -a < z < a})
    degree = 2*max(max(len(p) for p in columns), max(output_modes, default=0))
    return tuple(tuple(sum((exact_interpolatory_integral(
        lambda x: derivative(i, x)*derivative(j, x), left, right, degree)
        for left, right in zip(breaks, breaks[1:])), Q())
        for j in range(len(columns))) for i in range(len(columns)))


class ExactHingeTests(unittest.TestCase):
    def test_hs_and_derivative_hs_triangle_oracle(self):
        for a in (Q(1, 2), Q(2, 3)):
            for b in (Q(), a/2, a, 3*a/2, 2*a, 3*a):
                for c in (Q(-2, 3), Q(), Q(3, 2)):
                    h = W.Hinge(b, c)
                    delta = max(Q(), 2*a-b)
                    self.assertEqual(W.hinge_hs_inner(a, h, h), c*c*delta**4/6)
                    self.assertEqual(W.hinge_hs_inner(a, h, h),
                                     c*c*triangle_pair(a, b, (1,), (1,), kernel_power=2))
                    self.assertEqual(W.hinge_hs_inner(a, h, h, derivative=True),
                                     c*c*triangle_pair(a, b, (1,), (1,), kernel_power=0))

    def test_matrix_independent_triangles(self):
        columns = ((1,), (Q(1, 3), -2, Q(3, 2)), (0, 0, 0, 1))
        for a in (Q(1, 2), Q(3, 4)):
            for b in (Q(), a/3, a, 4*a/3, 2*a, 3*a):
                h = W.Hinge(b, Q(-2, 3))
                expected = tuple(tuple(h.weight*triangle_pair(a, b, p, q)
                                       for q in columns) for p in columns)
                self.assertEqual(W.hinge_matrix(a, columns, columns, (h,)), expected)

    def test_reuse_correlation_kernel(self):
        a = Q(1, 2)
        for i, j in ((1, 1), (1, 4), (2, 4), (3, 5)):
            p, q = L.legendre_polynomial(i, a), L.legendre_polynomial(j, a)
            for b in (Q(), Q(1, 5), Q(2, 3), Q(1)):
                self.assertEqual(W.hinge_matrix(a, (p,), (q,), (W.Hinge(b),))[0][0],
                                 L.poly_eval(L.prime_hinge_integral_polynomial(i, j, a), b))

    def test_derivative_gram_independent_quadrature(self):
        columns = ((1,), (0, 1), (Q(1, 3), -2, 0, 1))
        a = Q(1, 2)
        hinges = (W.Hinge(Q(1, 4), -2), W.Hinge(Q(2, 3), Q(3, 2)))
        for modes in ((), (0,), (1, 2), (0, 1, 2, 3, 4)):
            self.assertEqual(W.derivative_gram(a, columns, hinges, output_modes=modes),
                             independent_derivative_gram(a, columns, hinges, modes))

    def test_second_weak_derivative_is_sum_of_shifts(self):
        a, p = Q(3, 4), (Q(2, 7), Q(-1, 3), Q(4, 5), Q(2))
        for b in (Q(), Q(1, 3), a, Q(6, 5), 2*a):
            h = W.Hinge(b, Q(-3, 7))
            second = W.hinge_response(a, p, h).weak_derivative().weak_derivative()
            for l, r in zip(second.breaks, second.breaks[1:]):
                for ratio in (Q(1, 4), Q(2, 3)):
                    x = l+(r-l)*ratio
                    expected = sum((h.weight*sum((c*y**i for i, c in enumerate(p)), Q())
                                    for y in (x-b, x+b) if -a < y < a), Q())
                    self.assertEqual(second.value(x), expected)

    def test_weak_identity_including_endpoint_terms(self):
        a = Q(1, 2)
        response = W.hinge_response(a, (1, -2, 3), W.Hinge(Q(2, 3), -2))
        second = W.zero_extension_second_derivative(response)
        for test in ((1,), (0, 1), (0, 0, 1), (1, -3, 2, 0, 4)):
            derivative2 = tuple(k*(k-1)*v for k, v in enumerate(test) if k >= 2) or (0,)
            direct = response.inner(W.polynomial_on_interval(derivative2, a))
            self.assertEqual(second.pair_polynomial(test), direct)
        self.assertTrue(any(dp for _, _, dp in second.atoms))

    def test_hinge_prime_form_sign_by_integration_by_parts(self):
        a, b = Q(1, 2), Q(2, 3)
        v = (Q(1, 4), Q(), Q(-1))  # zero traces
        u = (Q(), Q(-2))
        form = W.hinge_matrix(a, (u,), (u,), (W.Hinge(b),))[0][0]
        overlap = exact_interpolatory_integral(
            lambda x: (a*a-x*x)*(a*a-(x+b)**2), -a, a-b, 4)
        self.assertEqual(form, -2*overlap)
        self.assertLess(form, 0)  # positive hinge values do not imply PSD

    def test_projection_orders_are_distinct_for_actual_hinge(self):
        a, hinges, p = Q(1, 2), (W.Hinge(Q(2, 3)),), (0, 1)
        correct = W.derivative_response(a, p, hinges, output_modes=(1, 2))
        commuted = W.derivative_response(a, p, hinges, derivative_modes=(1, 2))
        difference = correct.add(commuted, -1)
        self.assertGreater(difference.inner(difference), 0)

    def test_after_derivative_projection_gram_identity(self):
        a, p, hinges = Q(1, 2), (1, -1, 2), (W.Hinge(Q(1, 3)),)
        raw = W.derivative_response(a, p, hinges)
        projected = W.project_legendre(raw, (0, 1, 2, 3))
        residual = W.derivative_response(a, p, hinges, derivative_modes=(0, 1, 2, 3))
        self.assertEqual(raw.inner(raw), projected.inner(projected)+residual.inner(residual))

    def test_hs_projection_audit_independent_bivariate_integration(self):
        # Direct 2D polynomial integration on both triangles and the middle
        # strip via SymPy is covered below; this independent column expansion
        # covers the finite-rank correction with exact quadrature Grams.
        a, b, modes = Q(1, 2), Q(2, 3), (0, 1, 2)
        audit = W.projection_hs_audit(a, (W.Hinge(b),), modes)
        columns = tuple(L.legendre_polynomial(n, a) for n in modes)
        gram = independent_derivative_gram(a, columns, (W.Hinge(b),))
        expected_input = (2*a-b)**2-sum((gram[i][i]*Q(2*n+1)/(2*a)
                                        for i, n in enumerate(modes)), Q())
        self.assertEqual(audit['D_T_Q_HS_squared'], expected_input)
        # Independently reproduced by the symbolic 2D integration below.
        self.assertEqual(audit['D_Q_T_Q_HS_squared'], Q(44211169, 1953045675))

    def test_projection_after_output_can_amplify_hinge_derivative_input_tail(self):
        audit = W.projection_hs_audit(Q(1, 2), (W.Hinge(0),), (0, 1, 2, 3, 4))
        self.assertGreater(audit['D_Q_T_Q_HS_squared'], audit['D_T_Q_HS_squared'])
        self.assertLess(audit['Q_D_T_Q_HS_squared'], audit['D_T_Q_HS_squared'])

    def test_mixed_signed_hinges_and_refinement(self):
        a, hinges = Q(1, 2), (W.Hinge(Q(1, 4), -1), W.Hinge(Q(3, 4), 2))
        audit = W.projection_hs_audit(a, hinges, (0, 1))
        self.assertGreaterEqual(audit['D_Q_T_Q_HS_squared'], 0)
        f = W.hinge_sum_response(a, (1, -2), hinges)
        other = W.PiecewisePolynomial((-a, Q(), a), ((Q(1),), (Q(1),)))
        self.assertEqual(f.add(other).integral(), f.integral()+2*a)

    def test_boundary_atoms_and_zero_frequency(self):
        f = W.clipped_hinge(Q(3, 2), W.Hinge(Q(2, 3), 2))
        distribution = W.zero_extension_second_derivative(f)
        self.assertEqual(distribution.atoms, ((Q(-3, 2), Q(-2), Q(5, 3)),
                                              (Q(-2, 3), Q(2), Q()),
                                              (Q(2, 3), Q(2), Q()),
                                              (Q(3, 2), Q(-2), Q(-5, 3))))
        self.assertEqual(distribution.pair_polynomial((1,)), 0)
        self.assertEqual(f.integral(), Q(25, 18))
        self.assertEqual(distribution.pair_polynomial((0, 0, 1)), 2*f.integral())

    def test_boundary_and_coincident_edge_cases(self):
        for b in (Q(), Q(1), Q(2)):
            f = W.clipped_hinge(1, W.Hinge(b))
            d = W.zero_extension_second_derivative(f)
            for p in ((1,), (0, 1), (0, 0, 1)):
                self.assertEqual(d.pair_polynomial(p), (2*f.integral() if len(p) == 3 else 0))
        with self.assertRaises(W.WavefrontGeometryError):
            W.PiecewisePolynomial((0, 1, 2), ((0,), (1,))).weak_derivative()

    def test_fail_closed_input_validation(self):
        for call in (lambda: W.Hinge(0.5), lambda: W.Hinge(-1), lambda: W.Hinge(True),
                     lambda: W.hinge_response(0, (1,), W.Hinge(1)),
                     lambda: W.hinge_response(1, (), W.Hinge(1)),
                     lambda: W.derivative_gram(1, ((1,),), (), output_modes=(1, 1)),
                     lambda: W.derivative_gram(1, ((1,),), (), derivative_modes=(True,)),
                     lambda: W.PiecewisePolynomial((0, 0), ((1,),)),
                     lambda: W.polynomial_on_interval((1,), 1).value(2),
                     lambda: W.polynomial_on_interval((1,), 1).inner(W.polynomial_on_interval((1,), 2))):
            with self.assertRaises(W.WavefrontGeometryError):
                call()


class SourceTests(unittest.TestCase):
    def test_source_geometry_and_authentic_matrix(self):
        geometry = W.source_prime_geometry(Q(1, 2))
        self.assertEqual(geometry['source_blob'], '0cc8510b71d178fc79e8d410a86d8b6014cf9178')
        self.assertEqual(tuple(a['n'] for a in geometry['atoms']), (2,))
        self.assertFalse(geometry['full_signed_source_included'])
        self.assertFalse(geometry['RH_proved'])
        matrix = W.source_prime_matrix(Q(1, 2), (1, 2, 3), (1, 2, 3))
        for i in range(3):
            for j in range(3):
                older = L.authentic_first_prime_low_entry(i+1, j+1)
                current = matrix[i][j]
                self.assertLessEqual(max(older.lo, current.lo), min(older.hi, current.hi))
                self.assertEqual(current, matrix[j][i])
        self.assertLess(matrix[0][0].hi, 0)

    def test_full_bounded_tape_validation_even_for_invisible_fake6(self):
        mutants = (S.AUTHENTIC_TAPE+((6, 6),), S.AUTHENTIC_TAPE[1:],
                   S.AUTHENTIC_TAPE+((2, 2),), ((2, 3),)+S.AUTHENTIC_TAPE[1:])
        for tape in mutants:
            with self.assertRaises(S.WeilHierarchyError):
                W.source_prime_geometry(Q(1, 4), tape=tape)
        self.assertGreater(S.log_iv(6).lo, 1)

    def test_half_density_and_clock_mutants_rejected(self):
        for kwargs in ({'half_density': Q(2, 3)}, {'clock_scale': Q(1, 2)},
                       {'clock_scale': 2}, {'half_density': 0.5}):
            with self.assertRaises(W.WavefrontGeometryError):
                W.source_prime_geometry(Q(1, 2), **kwargs)

    def test_source_power_clock_and_weight(self):
        geometry = W.source_prime_geometry(1)
        self.assertEqual(tuple(a['n'] for a in geometry['atoms']), (2, 3, 4, 5, 7))
        atom = next(a for a in geometry['atoms'] if a['n'] == 4)
        self.assertEqual(atom['prime'], 2)
        self.assertEqual(atom['threshold'], S.log_iv(4))
        self.assertEqual(atom['weight'], S.log_iv(2)*S.sqrt_inverse(4))
        self.assertGreater(atom['threshold'].lo, S.log_iv(2).hi)

    def test_prime_free_window_and_limits(self):
        self.assertEqual(W.source_prime_geometry(Q(1, 4))['atoms'], ())
        self.assertEqual(W.source_prime_matrix(Q(1, 4), (1,), (1,))[0][0], S.iv(0))
        with self.assertRaises(W.WavefrontGeometryError):
            W.source_prime_geometry(2)
        with self.assertRaises(W.WavefrontGeometryError):
            W.source_prime_matrix(Q(1, 2), (0,), (1,))

    def test_true_prime_only_projection_bound(self):
        bound = W.source_first_prime_projection_bound()
        self.assertTrue(bound['strict_contraction_certified_this_prime_only'])
        self.assertFalse(bound['universal_output_projection_contraction'])
        self.assertFalse(bound['full_signed_source_included'])
        self.assertLess(bound['D_Q_G2_Q_HS_squared_upper'], bound['D_G2_HS_squared_interval'].lo)
        self.assertGreater(bound['threshold_error_upper'], 0)


@unittest.skipUnless(importlib.util.find_spec('sympy'), 'optional independent SymPy oracle unavailable')
class SymbolicOracleTests(unittest.TestCase):
    def test_symbolic_finite_window_fourier_and_boundary_law(self):
        import sympy as sp
        r, xi = sp.symbols('r xi', real=True, nonzero=True)
        length, b = sp.symbols('L b', positive=True)
        direct = 2*sp.integrate((r-b)*sp.cos(xi*r), (r, b, length))
        closed = 2*((length-b)*sp.sin(xi*length)/xi+(sp.cos(xi*length)-sp.cos(xi*b))/xi**2)
        self.assertEqual(sp.simplify(direct-closed), 0)
        boundary_law = 2*sp.cos(xi*b)-2*sp.cos(xi*length)-2*(length-b)*xi*sp.sin(xi*length)
        self.assertEqual(sp.simplify(-xi**2*closed-boundary_law), 0)
        self.assertEqual(sp.simplify(sp.limit(closed, xi, 0)-(length-b)**2), 0)

    def test_symbolic_projected_derivative_hs_independent_integral(self):
        import sympy as sp
        x, y = sp.symbols('x y', real=True)
        a, b = sp.Rational(1, 2), sp.Rational(2, 3)
        # Independent direct symbolic T P_n(x), without production responses.
        modes = (0, 1, 2)
        basis = [sp.legendre(n, 2*x) for n in modes]
        norms = [sp.Rational(1, 2*n+1) for n in modes]
        image_left = [sp.integrate((y-x-b)*p.subs(x, y), (y, x+b, a)) for p in basis]
        image_right = [sp.integrate((x-y-b)*p.subs(x, y), (y, -a, x-b)) for p in basis]
        cells = ((-a, a-b, image_left), (a-b, b-a, [sp.S(0)]*3), (b-a, a, image_right))
        matrix = [[sum(sp.integrate(p*images[j], (x, l, r)) for l, r, images in cells)
                   for j in modes] for p in basis]
        # Derivative correction C = D(QTQ-T), integrated against raw Dk and itself.
        correction_squared = sp.S(0)
        cross = sp.S(0)
        for xl, xr, ximages in cells:
            for yl, yr, yimages in cells:
                correction = -sum(sp.diff(basis[i], x)*yimages[i].subs(x, y)/norms[i]
                                  +sp.diff(ximages[i], x)*basis[i].subs(x, y)/norms[i] for i in modes)
                correction += sum(sp.diff(basis[i], x)*matrix[i][j]*basis[j].subs(x, y)/(norms[i]*norms[j])
                                  for i in modes for j in modes)
                correction_squared += sp.integrate(sp.integrate(sp.expand(correction**2), (y, yl, yr)), (x, xl, xr))
                if xl == b-a and yl == -a:
                    cross += sp.integrate(sp.integrate(correction, (y, -a, x-b)), (x, b-a, a))
                if xl == -a and yl == b-a:
                    cross -= sp.integrate(sp.integrate(correction, (y, x+b, a)), (x, -a, a-b))
        exact = sp.factor((2*a-b)**2+2*cross+correction_squared)
        audit = W.projection_hs_audit(Q(1, 2), (W.Hinge(Q(2, 3)),), modes)
        self.assertEqual(Q(int(sp.numer(exact)), int(sp.denom(exact))), audit['D_Q_T_Q_HS_squared'])


if __name__ == '__main__':
    unittest.main()
