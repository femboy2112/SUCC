"""Exact history-dependent Dirichlet-to-Neumann and dual-time growth laboratory.

Boundary voltage/current maps are finite passive resistor networks; all
conductances, transition probabilities and probes use Fraction.  The temporal
SUCC/FUCC bridge is explicitly two *different* compatibilities:
(1) forward/backward conditional Markov messages on the SAME growing graph;
(2) the genuine arithmetic affine braid and partial backwards prime shifts.
No prime arithmetic is derived from dielectric breakdown, no physical wave
response is assumed, and no RH / completed-Weil theorem is claimed.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from math import isqrt

from .dynamic_boundary_inverse import RCNetwork, inv, quad, submatrix


class GrowthContractError(ValueError):
    """Invalid exact network, history, stochastic kernel, or arithmetic input."""


def rational(value):
    if type(value) not in (int, F):
        raise GrowthContractError("Only exact int/Fraction values (not float/bool)")
    return F(value)


@dataclass(frozen=True)
class ConductiveState:
    """Fixed vertices/electrodes; strictly positive undirected conductances."""
    vertices: tuple[str, ...]
    boundary: tuple[str, ...]
    edges: tuple[tuple[str, str, F], ...]

    def __post_init__(self):
        if (type(self.vertices) is not tuple or type(self.boundary) is not tuple
                or type(self.edges) is not tuple):
            raise GrowthContractError("Network declarations must be tuples")
        try:
            RCNetwork("growing_DtN", self.vertices, self.boundary, self.edges)
        except (ValueError, TypeError) as error:
            raise GrowthContractError(str(error)) from error

    def network(self):
        return RCNetwork("growing_DtN", self.vertices, self.boundary, self.edges)

    def response(self):
        """Lambda=L_BB-L_BI L_II^{-1} L_IB, all over Q."""
        return self.network().response(0)

    def potential(self, boundary_voltages):
        """Unique harmonic potential, each interior component electrode-anchored."""
        if (type(boundary_voltages) is not tuple or
                len(boundary_voltages) != len(self.boundary)):
            raise GrowthContractError("A voltage is needed for each electrode")
        f = tuple(rational(x) for x in boundary_voltages)
        L = self.network().laplacian()
        ix = {v: j for j, v in enumerate(self.vertices)}
        B = tuple(ix[v] for v in self.boundary)
        I = tuple(ix[v] for v in self.vertices if v not in self.boundary)
        values = dict(zip(self.boundary, f))
        if I:
            Ai = inv(submatrix(L, I, I))
            rhs = tuple(-sum((L[i][b]*f[j] for j, b in enumerate(B)), F())
                        for i in I)
            for k, v in enumerate(self.vertices):
                if v not in values:
                    j = I.index(ix[v])
                    values[v] = sum((Ai[j][i]*rhs[i] for i in range(len(I))), F())
        return values

    def energy(self, boundary_voltages):
        if type(boundary_voltages) is not tuple or len(boundary_voltages) != len(self.boundary):
            raise GrowthContractError("A voltage is needed for each electrode")
        return quad(self.response(), tuple(rational(x) for x in boundary_voltages))

    def with_edge(self, a, b, conductance):
        """Physical edge conductance INCREMENT, aggregating existing pairs."""
        g = rational(conductance)
        if g <= 0 or a == b or a not in self.vertices or b not in self.vertices:
            raise GrowthContractError("New edge increment must be positive, non-loop and sourced")
        current = {frozenset((x, y)): (x, y, rational(c)) for x, y, c in self.edges}
        key = frozenset((a, b))
        if key in current:
            x, y, old = current[key]
            current[key] = (x, y, old + g)
        else:
            order = {v: i for i, v in enumerate(self.vertices)}
            x, y = sorted((a, b), key=lambda v: order[v])
            current[key] = (x, y, g)
        positions = {v: i for i, v in enumerate(self.vertices)}
        edges = tuple(sorted(current.values(), key=lambda item: (positions[item[0]], positions[item[1]])))
        return ConductiveState(self.vertices, self.boundary, edges)

    def edge_update(self, a, b, conductance):
        """Rank-one DtN gain and independent recomputation as exact Fractions.

        Let H map electrode data to the old harmonic solution, b_e the
        oriented incidence vector, r=b_e,I^T L_II^-1 b_e,I, w=H^T b_e.
        Then Delta Lambda = g/(1+g*r) ww^T.  This is an identity of
        finite linear resistor networks, not an inferred law of plasma.
        """
        g = rational(conductance)
        successor = self.with_edge(a, b, g)
        H = tuple(self.potential(tuple(F(j == k) for j in range(len(self.boundary))))
                  for k in range(len(self.boundary)))
        w = tuple(v[a] - v[b] for v in H)
        interior = tuple(v for v in self.vertices if v not in self.boundary)
        d = tuple(F(int(v == a) - int(v == b)) for v in interior)
        r = F()
        if interior:
            L = self.network().laplacian()
            positions = tuple(self.vertices.index(v) for v in interior)
            Ainv = inv(submatrix(L, positions, positions))
            r = sum((d[i]*Ainv[i][j]*d[j]
                     for i in range(len(d)) for j in range(len(d))), F())
        factor = g/(1 + g*r)
        predicted = tuple(tuple(factor*x*y for y in w) for x in w)
        old, new = self.response(), successor.response()
        observed = tuple(tuple(new[i][j]-old[i][j] for j in range(len(old)))
                         for i in range(len(old)) for _ in (0,))
        return {"edge": (a, b), "increment": g, "dirichlet_resistance": r,
                "voltage_drop_vector": w, "rank_one_factor": factor,
                "predicted_delta": predicted, "observed_delta": observed,
                "exact_match": predicted == observed, "successor": successor}

    def adaptive_edge(self, a, b, base, voltages, sensitivity=1):
        """Declared material-memory toy: g=base*(1+kappa*(phi_a-phi_b)^2)."""
        z, k = rational(base), rational(sensitivity)
        if z <= 0 or k < 0:
            raise GrowthContractError("Positive base and nonnegative sensitivity required")
        phi = self.potential(voltages)
        g = z*(1 + k*(phi[a]-phi[b])**2)
        return self.with_edge(a, b, g), g


def replay(initial, steps):
    """Preserve the ordered provenance instead of just the terminal graph."""
    if type(steps) is not tuple:
        raise GrowthContractError("Chronological events must form a tuple")
    states = [initial]
    for event in steps:
        if type(event) is not tuple or len(event) != 3:
            raise GrowthContractError("Each actualized event must be (a,b,increment)")
        states.append(states[-1].with_edge(*event))
    return tuple(states)


def exact_forward_backward(layers, kernels, initial, success):
    """Two-sided reconciliation of a finite growing-state Markov process.

    alpha_{t+1}=alpha_t K_t; beta_t=K_t beta_{t+1}.
    Hence sum alpha_t beta_t = Z independently of t, and whenever
    alpha_{t+1}(y)>0 the Bayes reverse is alpha_t(x) K(x,y)/alpha_{t+1}(y).
    This is a dual probabilistic process, NOT the prime FUCC operator V_p.
    """
    if (type(layers) is not tuple or not layers or type(kernels) is not tuple
            or len(kernels) != len(layers)-1):
        raise GrowthContractError("Finite nonempty time layers with adjacent kernels required")
    if any(type(level) is not tuple or not level or len(level) != len(set(level)) for level in layers):
        raise GrowthContractError("Layers must consist of unique finite states")
    a = {x: rational(initial.get(x, 0)) for x in layers[0]}
    if set(initial) - set(layers[0]) or any(v < 0 for v in a.values()) or sum(a.values()) != 1:
        raise GrowthContractError("Initial distribution must normalize")
    alphas = [a]
    for t, kernel in enumerate(kernels):
        if set(kernel) != set(layers[t]):
            raise GrowthContractError("Every source state needs a stochastic row")
        following = {y: F() for y in layers[t+1]}
        for x, row in kernel.items():
            if set(row)-set(following) or any(rational(v)<0 for v in row.values()):
                raise GrowthContractError("Kernel support/probabilities invalid")
            if sum((rational(v) for v in row.values()), F()) != 1:
                raise GrowthContractError("Kernel rows must sum exactly to one")
            for y, weight in row.items():
                following[y] += alphas[-1][x]*rational(weight)
        alphas.append(following)
    if set(success)-set(layers[-1]):
        raise GrowthContractError("Terminal predicate outside declared states")
    beta = {x: rational(success.get(x, 0)) for x in layers[-1]}
    if any(v not in (0, 1) for v in beta.values()):
        raise GrowthContractError("Success terminal values must be 0 or 1")
    betas = [None]*len(layers)
    betas[-1] = beta
    for t in reversed(range(len(kernels))):
        betas[t] = {x: sum((rational(y)*betas[t+1][z]
                            for z, y in kernels[t][x].items()), F())
                    for x in layers[t]}
    overlaps = tuple(sum((alphas[t][x]*betas[t][x] for x in layers[t]), F())
                     for t in range(len(layers)))
    if any(z != overlaps[0] for z in overlaps):
        raise ArithmeticError("Backward and forward descriptions disagree")
    reverse = []
    conditioned = []
    for t, kernel in enumerate(kernels):
        reverse.append({y:{x:(alphas[t][x]*rational(kernel[x].get(y,0))/alphas[t+1][y]
                              if alphas[t+1][y] else F()) for x in layers[t]}
                        for y in layers[t+1] if alphas[t+1][y]})
        conditioned.append({x:{y:(rational(w)*betas[t+1][y]/betas[t][x]
                                  if betas[t][x] else F())
                               for y, w in kernel[x].items()}
                            for x in layers[t] if betas[t][x]})
    return {"alpha": tuple(alphas), "beta": tuple(betas), "overlap": overlaps,
            "event_probability": overlaps[0], "bayes_reverse": tuple(reverse),
            "success_conditioned": tuple(conditioned)}


def field_weighted_subset_process(base, candidates, steps, epsilon=1):
    """Canonical fixed-edge SUBSET growth; full field recomputed at each step.

    Candidate labels map to (u,v,g); weights epsilon+Delta(phi)^2.
    This declared baseline tests history vs endpoint *without* wave physics.
    The graph state is sufficient because candidate gains are fixed.
    """
    eps = rational(epsilon)
    if eps <= 0 or type(candidates) is not dict or not 1 <= len(candidates) <= 6:
        raise GrowthContractError("Positive epsilon and 1..6 candidate events required")
    if type(steps) is not int or not 0 <= steps <= len(candidates):
        raise GrowthContractError("Invalid finite advancement depth")
    labels = tuple(sorted(candidates))
    if any(type(label) is not str or not label or
           type(edge) is not tuple or len(edge) != 3
           for label, edge in candidates.items()):
        raise GrowthContractError("Exact unique labelled candidate edges required")
    for edge in candidates.values():
        base.with_edge(*edge)
    levels = tuple(tuple(frozenset(c) for c in combinations(labels, t))
                   for t in range(steps+1))
    kernels = []
    for t in range(steps):
        kernel = {}
        for chosen in levels[t]:
            network = base
            for label in sorted(chosen):
                network = network.with_edge(*candidates[label])
            phi = network.potential(tuple(F(i==len(base.boundary)-1)
                                          for i in range(len(base.boundary))))
            weights = {label: eps+(phi[candidates[label][0]]-phi[candidates[label][1]])**2
                       for label in labels if label not in chosen}
            normalizer = sum(weights.values(), F())
            kernel[chosen] = {chosen|{label}: weight/normalizer
                              for label,weight in weights.items()}
        kernels.append(kernel)
    return levels, tuple(kernels)


def prime_clock_square(n, p):
    """Actual V_p S=S^p V_p and the adjoint backwards equality on basis.

    V_p^*|m> is zero for p nondividing m; S^*|1> is zero.
    Zero is represented by None. This is *not* a physical time reversal.
    """
    if type(n) is not int or n < 1 or type(p) is not int or p < 2 or any(
            p % j == 0 for j in range(2, isqrt(p)+1)):
        raise GrowthContractError("Genuine prime p and positive integer source needed")
    endpoint_a = p*(n+1)
    endpoint_b = p*n+p
    return {"start": n, "prime": p, "via_Vp_S": endpoint_a,
            "via_Sp_Vp": endpoint_b,
            "backward_Sstar_Vpstar": endpoint_a//p-1,
            "backward_Vpstar_Sstar_p": (endpoint_a-p)//p,
            "equal": endpoint_a == endpoint_b}


def prime_adjoint_on_basis(m, p):
    """Partial inverse; undivisible indices are annihilated, never rounded."""
    if type(m) is not int or m < 1 or type(p) is not int or p < 2 or any(
            p % j == 0 for j in range(2, isqrt(p)+1)):
        raise GrowthContractError("Positive integer and genuine prime required")
    return m//p if m%p == 0 else None


def history_affine_square(states, n, p):
    """Same *source-recorded history*, two affine clock itineraries.

    Position n>=1 observes snapshot G_{n-1}. These are arithmetic sampling
    operators on a chosen history fiber, not physical prime-mediated growth.
    Their equal endpoints do not imply identical intermediate observations.
    """
    clock = prime_clock_square(n, p)
    end = clock["via_Vp_S"]
    if type(states) is not tuple or not states or any(
            not isinstance(s, ConductiveState) for s in states):
        raise GrowthContractError("Nonempty source-recorded graph history required")
    if end > len(states):
        raise GrowthContractError("Both affine routes require an observed endpoint")
    a = (n, n+1, end)
    b = (n,) + tuple(range(p*n, end+1))
    return {"S_then_Vp_indices": a, "Vp_then_Sp_indices": b,
            "S_then_Vp_responses": tuple(states[j-1].response() for j in a),
            "Vp_then_Sp_responses": tuple(states[j-1].response() for j in b),
            "terminal_equal": states[a[-1]-1].response()==states[b[-1]-1].response(),
            "arithmetic_source": "chosen integer sampling clock; not prime dynamics of wood"}
