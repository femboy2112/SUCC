"""Independent SymPy/mpmath reconstruction. Does NOT import prime_pisot.

Symbolic equalities are exact finite checks. Numerical values are observations,
not interval certificates. Analytic tail inequalities have separate proofs.
Run: python independent_oracle.py > receipts/oracle.json
"""
import json
import platform
import sympy as sp
import mpmath as mp

checks = []

def exact(name, expression):
    if isinstance(expression, sp.MatrixBase):
        ok = all(sp.simplify(v) == 0 for v in expression)
    else:
        ok = sp.simplify(expression) == 0
    if not ok:
        raise AssertionError((name, expression))
    checks.append(name)

# A symbolic companion is transported to a positive stochastic matrix.
b, z = sp.symbols('b z', nonzero=True)
m = b-1/b
A = sp.Matrix([[m, 1], [1, 0]])
T = A/b
c = b**-2
P = (T+c*sp.eye(2))/(1+c)
D = sp.diag(b, 1)
M = sp.Matrix([[1-c, c], [1, 0]])
exact('companion determinant', (sp.eye(2)-z*T).det()-(1-z)*(1+c*z))
exact('positive Markov similarity', D.inv()*T*D-M)
exact('marked projector is idempotent', P*P-P)
exact('marked projector is invariant', T*P-P)
exact('marked projector trace', sp.trace(P)-1)
for k in range(1, 7):
    exact('trace identity k='+str(k), sp.trace(T**k)-(1+(-c)**k))
    exact('source-marked trace k='+str(k), sp.trace(P*T**k)-1)

phi = (1+sp.sqrt(5))/2
b11 = (11+5*sp.sqrt(5))/2
b29 = (29+13*sp.sqrt(5))/2
exact('beta11=phi^5', sp.expand(phi**5-b11))
exact('beta29=phi^7', sp.expand(phi**7-b29))
exact('distinct prime-power histories collide', sp.expand(b11**7-b29**5))

# Independently start from the accepted Pólya channel, not from edge weights.
x = sp.symbols('x')
for dim in range(1, 13):
    p = sp.zeros(dim+1, dim)
    for k in range(dim):
        p[k, k] = sp.Rational(dim-k, dim+1)
        p[k+1, k] = sp.Rational(k+1, dim+1)
    L = sp.eye(dim)-sp.Rational(dim+1, dim)*(p.T*p)
    target = sp.prod(x-sp.Rational(r*(r+1), dim*(dim+1)) for r in range(dim))
    exact('PCR02 characteristic polynomial dim='+str(dim), L.charpoly(x).as_expr()-target)

# Ordinary multivariate power series, independent of Dirichlet convolution code.
x, y = sp.symbols('x y')
free = 1/((1-x)*(1-y))
exact('free connected xy coefficient', sp.diff(sp.log(free), x, y).subs({x: 0, y: 0}))
# With occupation-pair weight q, coefficient xy in log is q-1.
q = sp.symbols('q')
truncated = 1+x+y+q*(x*x+x*y+y*y)
exact('pair penalty connected xy', sp.diff(sp.log(truncated), x, y).subs({x: 0, y: 0})-(q-1))

# A symmetric off-line quartet: s=1/2+w, epsilon=1/4, gamma=2.
u, v, w = sp.symbols('u v w', real=True)
eps, gamma = sp.Rational(1, 4), sp.Integer(2)
f = ((w-eps)**2+gamma**2)*((w+eps)**2+gamma**2)
root = eps+sp.I*gamma
exact('functional-equation counterfeit', f-f.subs(w, -w))
exact('counterfeit root', f.subs(w, root))
droot = sp.simplify(sp.diff(f, w).subs(w, root))
assert droot != 0
holo = sp.expand(f.subs(w, u+sp.I*v))
potential = sp.expand(holo*sp.conjugate(holo))
hess = sp.hessian(potential, (u, v)).subs({u: eps, v: gamma})
exact('stable off-line potential minimum', hess-130*sp.eye(2))
logforce = sp.diff(f, w)/f
exact('log-force has charge, not equilibrium', sp.limit((w-root)*logforce, w, root)-1)
# Reciprocal pairing is not positive unitarity.
U = sp.diag(2, sp.Rational(1, 2))
J = sp.Matrix([[0, 1], [1, 0]])
exact('indefinite reciprocal invariant', U.T*J*U-J)
a, h, d = sp.symbols('a h d', real=True)
G = sp.Matrix([[a, h], [h, d]])
metric_solutions = sp.solve(list(U.T*G*U-G), (a, d), dict=True)
assert metric_solutions == [{a: 0, d: 0}]
checks.append('no positive invariant metric for reciprocal mutant')
# Finite backward-heat flow, with genuinely moving zeros.
t = sp.symbols('t', positive=True)
fheat = w*w-1-2*t
rheat = sp.sqrt(1+2*t)
exact('backward heat equation', sp.diff(fheat, t)+sp.diff(fheat, w, 2))
exact('zero motion is not equilibrium', sp.diff(rheat, t)-1/rheat)

# Positive path measure is also insufficient, even with both xi symmetries.
# G(s)=2+cosh(4(s-1/2)); its positive Fourier measure has weights 2,1/2,1/2.
u0 = sp.log(2+sp.sqrt(3))
wp = (u0+sp.I*sp.pi)/4
exact('positive support has an off-line zero',
      sp.expand_complex(2+(sp.exp(4*wp)+sp.exp(-4*wp))/2))
exact('positive support off-line derivative',
      sp.expand_complex(2*(sp.exp(4*wp)-sp.exp(-4*wp)))+4*sp.sqrt(3))
exact('positive support off-line minimum Hessian scale',
      2*(-4*sp.sqrt(3))**2-96)

# Fresh holdouts fixed in advance; no nontrivial zeta zeros are supplied.
mp.mp.dps = 70
primes = list(sp.primerange(2, 10001))
logp = {p: mp.log(p) for p in primes}
beta = {p: (p+mp.sqrt(p*p+4))/2 for p in primes}
logbeta = {p: mp.log(beta[p]) for p in primes}

def log_ratio(s, cutoff, kind='pisot'):
    out = []
    for p in primes:
        if p > cutoff:
            break
        lq = logbeta[p] if kind == 'pisot' else mp.log(mp.mpf(p)+mp.mpf(1)/p)
        out.append(mp.log1p(-mp.exp(-s*logp[p]))-mp.log1p(-mp.exp(-s*lq)))
    return mp.fsum(out)

points = [mp.mpc('1.5', 0), mp.mpc('0.5', 2), mp.mpc('0.5', 17), mp.mpc('0.75', -11)]
numerical = []
for s in points:
    coarse, fine = log_ratio(s, 100), log_ratio(s, 10000)
    analytic_bound = abs(s)*mp.power(100, -s.real-1)/((s.real+1)*(1-mp.power(2, -s.real)))
    assert abs(fine-coarse) < analytic_bound
    nonpisot = log_ratio(s, 10000, 'rational')
    numerical.append({
        's': str(s), 'C_10000': str(mp.exp(fine)),
        'log_cutoff_discrepancy_100_to_10000': str(abs(fine-coarse)),
        'proved_tail_at_100_evaluated_numerically': str(analytic_bound),
        'non_Pisot_C_10000': str(mp.exp(nonpisot)),
        'no_zero_positions_used': True,
    })

# Independent Euler-factor versus repeated-orbit expansion.
s = mp.mpc('0.5', 17)
series_terms = []
for p in sp.primerange(2, 98):
    xp, yp = mp.exp(-s*logp[p]), mp.exp(-s*logbeta[p])
    xk, yk = xp, yp
    for k in range(1, 321):
        series_terms.append((yk-xk)/k)
        xk, yk = xk*xp, yk*yp
series_error = abs(mp.fsum(series_terms)-log_ratio(s, 97))
assert series_error < mp.mpf('1e-45')

# Generalized Dirichlet trace with original n labels and multiplicity retained.
N = 3000
source_sum = mp.fsum(mp.exp(-2*sum(e*logbeta[p] for p, e in sp.factorint(n).items()))
                     for n in range(1, N+1))
continued_value = mp.zeta(2)*mp.exp(log_ratio(mp.mpf(2), 10000))
clock_tail = 2*mp.power(10000, -3)/(3*(1-mp.mpf(2)**-2))
bound = mp.mpf(1)/N + mp.zeta(2)*mp.expm1(clock_tail)
assert 0 < continued_value-source_sum < bound

result = {
    'authority': 'symbolic finite checks; numerical observations with separately proved analytic tails',
    'imports_primary_module': False,
    'versions': {'python': platform.python_version(), 'sympy': sp.__version__, 'mpmath': mp.__version__},
    'exact_checks_passed': len(checks), 'exact_check_names': checks,
    'collision_source_integers': [11**7, 29**5],
    'counterfeit_root_in_s_plane': '3/4 + 2i',
    'counterfeit_derivative': str(droot),
    'counterfeit_potential_hessian': [[str(z) for z in row] for row in hess.tolist()],
    'numerical_holdouts': numerical,
    'prime_orbit_series_error': str(series_error),
    'dirichlet_trace_s2': {
        'n_cutoff': N, 'prime_cutoff': 10000, 'partial_sum': str(source_sum),
        'zeta_times_C': str(continued_value), 'discrepancy': str(continued_value-source_sum),
        'proved_bound_evaluated_numerically': str(bound),
    },
    'roundoff_certified': False,
    'rh_proved': False,
}
print(json.dumps(result, indent=2))
