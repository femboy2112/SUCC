"""Exact controls and explicitly numerical finite Jacobi Hamiltonians.

H_g=diag(log n)+g(S+S*) on positive integers. Infinite spectral and
entanglement statements are proved in INTERACTING_ARITHMETIC_TFD.md;
finite eigensolver outputs are not interval certificates.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial, isfinite

from .unit_prime_succ import SourceError, integer


def _q(x):
    if type(x) is not int and not isinstance(x, Q):
        raise SourceError("Exact integer/Fraction parameter required")
    return Q(x)


def adjacency_walks(start, steps, cutoff=None):
    """Exact A^steps|start>; cutoff=None is the actual half-line carrier."""
    integer(start, 1, 10000); integer(steps, 0, 100)
    if cutoff is not None:
        integer(cutoff, start, 10000)
    state = {start: 1}
    for _ in range(steps):
        nxt = defaultdict(int)
        for n, count in state.items():
            if n > 1:
                nxt[n-1] += count
            if cutoff is None or n < cutoff:
                nxt[n+1] += count
        state = dict(nxt)
    return state


def unitary_minor_series(order=8):
    """D(t)=sum c_k (it)^k for ψ=(|1>+|2>)/sqrt(2), through order.

D=a_1*a_6-a_2*a_3 is a v2/odd-factor Schmidt minor. Each coefficient
uses exact half-line walk counts, not a fitted finite numerical evolution.
"""
    integer(order, 0, 30)
    walks = []
    for k in range(order+1):
        a, b = adjacency_walks(1, k), adjacency_walks(2, k)
        walks.append({n: a.get(n, 0)+b.get(n, 0) for n in set(a) | set(b)})
    return tuple(sum((Q(walks[j].get(1, 0)*walks[k-j].get(6, 0)
                          -walks[j].get(2, 0)*walks[k-j].get(3, 0),
                          2*factorial(j)*factorial(k-j)) for j in range(k+1)), Q())
                 for k in range(order+1))


def adjacency_minor_lower_bound(t):
    """Paper-proved bound |D(t)| >= |t|/2-16*t^2; may be negative."""
    t = abs(_q(t))
    return t/2-16*t*t


def interacting_minor_lower_bound(g, t):
    """Paper-proved conservative bound for exp(it H_g), all real g,t."""
    a, t = abs(_q(g)), abs(_q(t))
    return a*t/2-(13*a*a+12*a+3)*t*t


def certified_linear_entropy_bound(g, t, adjacency_only=False):
    """Exact lower bound on 1-tr(rho_v2^2) for the specified initial ray."""
    bound = (adjacency_minor_lower_bound(t) if adjacency_only
             else interacting_minor_lower_bound(g, t))
    return 2*max(Q(), bound)**2


def cutoff_first_leakage(support_max, cutoff):
    """First power at which a half-line walk can escape the finite cutoff."""
    integer(support_max, 1, 10000); integer(cutoff, support_max, 10000)
    return cutoff-support_max+1


def _finite_inputs(cutoff, g, beta=None):
    integer(cutoff, 2, 512)
    if isinstance(g, bool) or not isfinite(float(g)):
        raise SourceError("Finite real coupling required")
    if beta is not None and (isinstance(beta, bool) or not isfinite(float(beta)) or beta <= 0):
        raise SourceError("Positive finite inverse temperature required")


def finite_hamiltonian(cutoff, g):
    """Floating finite compression, NOT a certified infinite operator."""
    _finite_inputs(cutoff, g)
    import numpy as np
    h = np.diag(np.log(np.arange(1, cutoff+1, dtype=float)))
    off = np.full(cutoff-1, float(g))
    return h+np.diag(off, 1)+np.diag(off, -1)


def finite_thermal_diagnostics(cutoff, g, beta):
    """Numerical Gibbs/TFD using actual eigenvectors and right conjugation.

The coefficient matrix C of sum_j sqrt(w_j)|u_j>⊗|bar(u_j)>
is U diag(sqrt(w)) U*, and the left reduced matrix is C C*.
"""
    _finite_inputs(cutoff, g, beta)
    import numpy as np
    from scipy.linalg import expm
    from .arithmetic_entanglement import prime_split
    h = finite_hamiltonian(cutoff, g)
    energies, basis = np.linalg.eigh(h)
    shifted = np.exp(-float(beta)*(energies-energies[0]))
    weights = shifted/shifted.sum()
    log_partition = float(-beta*energies[0]+np.log(shifted.sum()))
    rho = (basis*weights)@basis.conj().T
    tfd = (basis*np.sqrt(weights))@basis.conj().T
    independent = expm(-float(beta)*(h-energies[0]*np.eye(cutoff)))
    independent /= np.trace(independent)
    coords = [prime_split(n) for n in range(1, cutoff+1)]
    nk = max(k for k, _ in coords)+1
    odds = sorted({m for _, m in coords})
    odd_index = {m: j for j, m in enumerate(odds)}
    full = np.zeros((nk, len(odds), nk, len(odds)), dtype=complex)
    for i, (k, m) in enumerate(coords):
        for j, (ell, r) in enumerate(coords):
            full[k, odd_index[m], ell, odd_index[r]] = rho[i, j]
    left = np.einsum('abcb->ac', full)
    right = np.einsum('abad->bd', full)
    defect = full.reshape(nk*len(odds), nk*len(odds))-np.kron(left, right)
    logs = np.log(np.arange(1, cutoff+1))
    return {
        "status": "NUMERICAL OBSERVATION",
        "cutoff": cutoff, "g": float(g), "beta": float(beta),
        "min_eigenvalue": float(energies[0]),
        "log_partition": log_partition,
        "max_eigenvalue_comparison_defect": float(np.max(np.abs(energies-logs))-2*abs(g)),
        "tfd_norm_squared": float(np.vdot(tfd, tfd).real),
        "tfd_reduction_defect": float(np.linalg.norm(tfd@tfd.conj().T-rho)),
        "independent_expm_defect": float(np.linalg.norm(independent-rho)),
        "prime_product_frobenius_defect": float(np.linalg.norm(defect)),
        "finite_prefix_induces_correlations_even_at_g_zero": True,
        "infinite_trace_certified_by_this_computation": False,
        "mixed_state_entanglement_certified": False,
    }
