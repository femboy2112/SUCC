"""Exact closure/hidden-state controls for Cambrian assignments 31--36.

Classical finite linear systems and explicit mathematical countermodels.  No
physical source authentication, empirical cognition, NS regularity or RH claim.
Only integer/Fraction coordinates are accepted; all tests use exact arithmetic.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .dynamic_boundary_inverse import mat, mm, rank, tr
from .quantum_records import Instrument


class ClosureError(ValueError):
    """The declared rational source/interface is malformed."""


def vector(xs):
    if not xs or any(type(x) is not int and not isinstance(x, Q) for x in xs):
        raise ClosureError("A nonempty exact rational vector is required")
    return tuple(Q(x) for x in xs)


def mv(a, x):
    if len(a[0]) != len(x):
        raise ClosureError("Matrix/vector shapes differ")
    return tuple(sum((v*w for v, w in zip(row, x)), Q(0)) for row in a)


def add(*xs):
    if not xs or any(len(x) != len(xs[0]) for x in xs):
        raise ClosureError("Vector shapes differ")
    return tuple(sum((x[i] for x in xs), Q(0)) for i in range(len(xs[0])))


def identity(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def power(a, n):
    if type(n) is not int or n < 0:
        raise ClosureError("Power must be a nonnegative integer")
    out = identity(len(a))
    for _ in range(n):
        out = mm(out, a)
    return out


def iszero(a):
    return all(x == 0 for row in a for x in row)


def finite_closure_obstruction(states, actions, project, step):
    """Witness failure of q step_a = reduced_step_a q on a COMPLETE finite carrier.

    None proves only this supplied finite table. Availability must be common:
    every supplied action must have a total transition on every supplied state.
    """
    states, actions = tuple(states), tuple(actions)
    if not states:
        raise ClosureError("The declared carrier must be nonempty")
    table = {}
    for s in states:
        for a in actions:
            target = step(s, a)
            if target not in states:
                raise ClosureError("The table is not a total endomorphism")
            key = (project(s), a)
            result = project(target)
            if key in table and table[key][1] != result:
                return (table[key][0], s, a, table[key][1], result)
            table[key] = (s, result)
    return None


@dataclass(frozen=True)
class BlockSystem:
    """x'=Ax+Bz+Eu, z'=Cx+Dz+Hu (prime means one discrete successor).

    Same matrices also specify continuous derivative dynamics in the paper
    theorem; this executable class implements discrete successors only.
    """
    A: tuple
    B: tuple
    C: tuple
    D: tuple
    E: tuple
    H: tuple

    def __post_init__(self):
        for name in ("A", "B", "C", "D", "E", "H"):
            object.__setattr__(self, name, mat(getattr(self, name)))
        r, h, m = len(self.A), len(self.D), len(self.E[0])
        required = {"A": (r, r), "B": (r, h), "C": (h, r),
                    "D": (h, h), "E": (r, m), "H": (h, m)}
        for name, shape in required.items():
            a = getattr(self, name)
            if (len(a), len(a[0])) != shape:
                raise ClosureError("Incompatible block dimensions: " + name)

    @property
    def hidden_dimension(self):
        return len(self.D)

    def step(self, x, z, u):
        x, z, u = vector(x), vector(z), vector(u)
        return (add(mv(self.A, x), mv(self.B, z), mv(self.E, u)),
                add(mv(self.C, x), mv(self.D, z), mv(self.H, u)))

    def simulate(self, x0, z0, inputs):
        x, z = vector(x0), vector(z0)
        xs, zs = [x], [z]
        for u in inputs:
            x, z = self.step(x, z, u)
            xs.append(x); zs.append(z)
        return tuple(xs), tuple(zs)

    def kernel(self, k, *, input_kernel=False):
        return mm(mm(self.B, power(self.D, k)), self.H if input_kernel else self.C)

    def memory_successor(self, xs, inputs, z0):
        """Eliminate z, using actual resolved history x_0,...,x_n and u_0,...,u_n."""
        if not xs or len(xs) != len(inputs):
            raise ClosureError("Supply one input per resolved state through n")
        n = len(xs) - 1
        terms = [mv(self.A, vector(xs[-1])), mv(self.E, vector(inputs[-1])),
                 mv(mm(self.B, power(self.D, n)), vector(z0))]
        for j in range(n):
            terms.append(mv(self.kernel(n-1-j), vector(xs[j])))
            terms.append(mv(self.kernel(n-1-j, input_kernel=True), vector(inputs[j])))
        return add(*terms)

    def closure_certificate(self):
        """Finite exact criterion; universality follows from the dossier proof.

        Full hidden-initial domain: closure iff B=0. Zero-hidden-initial domain:
        closure with Ax+Eu iff BD^k C = BD^k H = 0 for 0<=k<h.
        """
        coefficients = tuple((self.kernel(k), self.kernel(k, input_kernel=True))
                             for k in range(self.hidden_dimension))
        return {"all_hidden_initial_closure": iszero(self.B),
                "zero_hidden_initial_closure": all(iszero(c) and iszero(h)
                                                   for c, h in coefficients),
                "coefficients": coefficients,
                "physical_source_identity_proved": False}


def scalar_hankel_rank(system, depth):
    if type(depth) is not int or depth < 1:
        raise ClosureError("Positive Hankel depth required")
    if len(system.A) != 1:
        raise ClosureError("This helper is scalar only")
    return rank(tuple(tuple(system.kernel(i+j)[0][0] for j in range(depth))
                      for i in range(depth)))


def quantum_backaction_witness():
    """Equal Z POVM, unequal source-changing channels and future Z records."""
    p0, p1 = mat(((1, 0), (0, 0))), mat(((0, 0), (0, 1)))
    reset1 = mat(((0, 1), (0, 0)))
    luders = Instrument("cambrian_f_luders", (("0", p0), ("1", p1)))
    reset = Instrument("cambrian_f_reset", (("0", p0), ("1", reset1)))
    first = luders.probabilities(p1)
    _, after_luders = luders.event(p1, "1")
    _, after_reset = reset.event(p1, "1")
    return {"same_initial_outcome_law": first == reset.probabilities(p1),
            "first_law": first,
            "same_povm": all(mm(tr(k), k) == mm(tr(l), l)
                             for (_, k), (_, l) in zip(luders.outcomes, reset.outcomes)),
            "future_luders_Z": luders.probabilities(after_luders),
            "future_reset_Z": luders.probabilities(after_reset),
            "reset_state": after_reset,
            "record_only_is_causally_sufficient": False}


def rational_null_rays(spatial_dimension=3):
    if type(spatial_dimension) is not int or spatial_dimension < 1:
        raise ClosureError("Positive spatial dimension required")
    out = []
    for i in range(spatial_dimension):
        for sign in (-1, 1):
            v = [Q(1)] + [Q(0)]*spatial_dimension
            v[i+1] = Q(sign); out.append(tuple(v))
    for i in range(spatial_dimension):
        for j in range(i+1, spatial_dimension):
            v = [Q(1)] + [Q(0)]*spatial_dimension
            v[i+1], v[j+1] = Q(3, 5), Q(4, 5)
            out.append(tuple(v))
    return tuple(out)


def null_probe_constraint_rank(spatial_dimension=3):
    rays = rational_null_rays(spatial_dimension)
    d = spatial_dimension + 1
    coords = tuple((i, j) for i in range(d) for j in range(i, d))
    constraints = tuple(tuple(v[i]*v[j]*(1 if i == j else 2)
                              for i, j in coords) for v in rays)
    return rank(constraints), len(coords)


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), Q(0))


def leray(k, v):
    k, v = vector(k), vector(v)
    if len(k) != len(v) or dot(k, k) == 0:
        raise ClosureError("Leray mode must be nonzero and dimension compatible")
    q = dot(k, v)/dot(k, k)
    return tuple(x - q*y for x, y in zip(v, k))


def fluid_high_high_witness(n):
    """Exact 2D incompressible Fourier triad, cutoff |k|<=1, n>=2.

    w=(0,1)cos(nx)+(1,-n)cos(nx+y).  P w=0, yet the q=(0,1)
    sine coefficient of Leray P div(w tensor w) is (-1/2,0).
    This is an instantaneous closure obstruction, not a PDE solver.
    """
    if type(n) is not int or n < 2:
        raise ClosureError("Integer n>=2 required for the strict unresolved modes")
    k, ell = (n, 0), (n, 1)
    a, b, q = (Q(0), Q(1)), (Q(1), Q(-n)), (0, 1)
    # cos(k) sin(ell) contributes +sin(ell-k)/2; cos(ell) sin(k) -sin(ell-k)/2.
    nonlinear_sine = tuple((-dot(a, ell)*b[i] + dot(b, k)*a[i])/2 for i in range(2))
    projected = leray(q, nonlinear_sine)
    return {"k": k, "ell": ell, "a": a, "b": b,
            "incompressible": dot(k, a) == dot(ell, b) == 0,
            "resolved_velocity_zero": dot(k, k) > 1 and dot(ell, ell) > 1,
            "low_mode": q, "raw_advection_sine": nonlinear_sine,
            "leray_advection_sine": projected,
            "resolved_acceleration_sine": tuple(-x for x in projected)}


def maxwell_symbol_square(xi, speed):
    """Real frequency symbol S=[[0,c^2 cross(xi)],[-cross(xi),0]]."""
    x, y, z = vector(xi)
    c = vector((speed,))[0]
    if c <= 0 or x*x+y*y+z*z == 0:
        raise ClosureError("Nonzero spatial frequency and positive speed required")
    cross = mat(((0, -z, y), (z, 0, -x), (-y, x, 0)))
    s = tuple(tuple(Q(0) if (i < 3) == (j < 3) else
                    c*c*cross[i][j-3] if i < 3 else -cross[i-3][j]
                    for j in range(6)) for i in range(6))
    return s, mm(s, s)


def finite_query_rival(queried):
    """Two computable Boolean sequences agree on a supplied finite query set.

    The true sequence is all ones; the rival has one zero outside the set.  The
    result is an access theorem, and makes no claim of arithmetic unprovability.
    """
    if any(type(n) is not int or n < 0 for n in queried):
        raise ClosureError("Natural query coordinates required")
    q = frozenset(queried)
    j = 0
    while j in q:
        j += 1
    return {"queried": tuple(sorted(q)), "rival_zero_at": j,
            "all_observed_bits": tuple(1 for _ in sorted(q)),
            "same_finite_transcript": True,
            "universal_certification_from_this_transcript": False}


def attention_policy_step(state, action="attend", *, source_bit=1):
    """Declared phenomenological toy: (belief,protection) -> new modeled state.

    A 'release' intervention changes policy state; it does not manufacture a
    source observation. The probe reveal is physically available throughout.
    """
    if state not in ((0, 0), (0, 1), (1, 0), (1, 1)) or source_bit not in (0, 1):
        raise ClosureError("Finite typed attention state required")
    belief, protected = state
    if action == "release":
        return belief, 0
    if action != "attend":
        raise ClosureError("Unknown action")
    return (belief if protected else source_bit), protected


def attention_witness():
    states = ((0, 0), (0, 1), (1, 0), (1, 1))
    obstruction = finite_closure_obstruction(states, ("attend",),
                                            lambda s: s[0], attention_policy_step)
    return {"belief_only_obstruction": obstruction,
            "physical_probe_available": True,
            "source_map_correct_by_construction": True,
            "protected_next": attention_policy_step((0, 1)),
            "released_then_next": attention_policy_step(attention_policy_step((0, 1), "release")),
            "empirical_cognitive_claim": False,
            "diagnostics_are_not_aggregated": True}
