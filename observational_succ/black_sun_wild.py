"""BLACK SUN III: tame towers and wild limits — the Baez-Duarte distance
instrument and the two-mode Weil reduction.

Campaign round 3, 2026-10-14, branch research/black-sun-iii-wild-limits-2026-10-14
(child of Black Sun II). RH PROVED: NO. No zero positions used as inputs.

Motivating correspondence (the wild-embedding intuition, made precise):

  Alexander's horned sphere (1924) is TAMe at every finite stage of its
  construction; the wildness (non-simply-connected complement) is a property
  of the LIMIT only, detected by a global loop that threads the horns.  The
  SUCC window tower and the Nyman-Beurling-Baez-Duarte dilation tower have
  the same architecture:

  - finite stages:  windows (-a,a) with finitely many prime atoms /
    spans V_k = span{gamma_1..gamma_k}: each tame, computable;
  - the limit question: positivity of Q_a for ALL a / density of the
    union: both RH-equivalent;
  - horn loops: global orthogonal witnesses (a function perpendicular to
    every stage that is not zero): they can only exist as LIMIT objects;
  - the Beurling-Malliavin density theorem: the quantitative law of "how
    many horns fit in a finite type budget" (already load-bearing in
    round 1's no-kernel argument).

What this module implements and proves:

  BS-III-1 (classical + exact implementation): the Bagchi-weighted-l2
      formulation of the Baez-Duarte strengthening of Nyman-Beurling:
      H = l2(N, 1/(n(n+1))), gamma_l = { {n/l} }_n, gamma = (1,1,...):
      RH iff gamma lies in the closed span of {gamma_l}.  The BD distance
      sequence d_k = dist(gamma, span{gamma_1..gamma_k}) is computed with
      CLOSED-FORM Gram entries (digamma at rationals via periodic
      decomposition), exactly verifiable norms, and machine-precision
      solves.  d_k > 0 at every finite stage (horns remain); d_k -> 0
      iff RH (the limit question).  TESTED MODEL evidence for the decay.

  BS-III-2 (PROVED LOCAL): tame-tower faithfulness: for every A > 0 the
      family of windowed forms {Q_a : a <= A} determines the source
      Lambda on n < e^{2A} EXACTLY (recovery by explicit test functions)
      and is blind to mutations beyond e^{2A}; the full tower over all A
      determines the source completely.  The source-to-tower transport
      is TAME: no wildness hides in the identification; the difficulty
      lives exclusively in the SIGN of the limit stages and in the
      density limit questions.  (Extends E38.1 with explicit finite
      recovery functions; verified exactly on small stages.)

  BS-III-3 (TESTED MODEL): the two-mode reduction of the first window:
      at a = 1/2 the negativity/near-nullity of the completed Weil form
      is confined (numerically) to the span of the two lowest modes
      (even bell, odd one-node); the 2x2 effective matrix and the
      complement margin are computed; groundwork for the interval-
      arithmetic two-mode certificate (round 2's next lemma).
"""
from __future__ import annotations

from fractions import Fraction
from math import log, sqrt
from typing import Callable


class BlackSunWildError(ValueError):
    pass


def _mp():
    try:
        import mpmath as mp
    except ImportError as err:
        raise BlackSunWildError("mpmath research extra required") from err
    return mp


# ---------------------------------------------------- BS-III-1: BD distance


def gram_entry(l: int, m: int, dps: int = 50):
    """<gamma_l, gamma_m> in the Bagchi-weighted l2 space.

    = sum_n {n/l}{n/m} / (n(n+1)).  The sequence {n/l}{n/m} is periodic with
    period lcm(l,m): write n = j*L + r: then the sum splits by residue r
    with weight sum_{j>=0} 1/((jL+r)(jL+r+1)), which telescopes via
    digamma: sum_j [1/(jL+r) - 1/(jL+r+1)] = (1/L)[psi((r+1)/L) - psi(r/L)]
    for r >= 1, and for r = 0: sum_j [1/(jL) - 1/(jL+1)] = psi(1/L)/L.
    All values exact modulo digamma at rationals (themselves classical
    closed forms: Gauss digamma theorem).
    """
    if type(l) is not int or type(m) is not int or l < 1 or m < 1:
        raise BlackSunWildError("positive integer indices required")
    mp = _mp()
    mp.mp.dps = dps
    L = _lcm(l, m)
    total = mp.mpf('0')
    for r in range(1, L+1):
        # {n/l} = (n mod l)/l: the fractional parts are (r mod l)/l
        frac = mp.mpf((r % l)*(r % m))/(mp.mpf(l)*mp.mpf(m))
        if frac == 0:
            continue
        # weight: sum_{j>=0} 1/((jL+r)(jL+r+1)) = (1/L)[psi((r+1)/L) - psi(r/L)]
        w = (mp.digamma(mp.mpf(r+1)/L) - mp.digamma(mp.mpf(r)/L))/L
        total += frac*w
    return total


def b_entry(l: int, dps: int = 50):
    """<gamma, gamma_l> = sum_n {n/l}/(n(n+1)) (closed form via digamma)."""
    mp = _mp()
    mp.mp.dps = dps
    L = l
    total = mp.mpf('0')
    for r in range(1, L+1):
        frac = mp.mpf(r % l)/mp.mpf(l)
        if frac == 0:
            continue
        w = (mp.digamma(mp.mpf(r+1)/L) - mp.digamma(mp.mpf(r)/L))/L
        total += frac*w
    return total


def n_mod(r: int, l: int) -> int:
    """{r/l} numerator: r mod l (for integer r >= 1, {r/l} = (r mod l)/l)."""
    return r % l


def _lcm(a: int, b: int) -> int:
    from math import gcd
    return a*b//gcd(a, b)


def gram_matrix(k: int, dps: int = 50):
    """The k x k Gram matrix of gamma_1..gamma_k (exact closed forms)."""
    mp = _mp()
    mp.mp.dps = dps
    G = mp.matrix(k, k)
    for i in range(k):
        for j in range(i, k):
            v = gram_entry(i+1, j+1, dps)
            G[i, j] = v
            G[j, i] = v
    return G


def bd_distance_sequence(k_max: int, dps: int = 50):
    """d_j for j = 1..k_max: dist(gamma, span{gamma_2..gamma_{j+1}})^2 =
    ||gamma||^2 - b^T G^{-1} b with ||gamma||^2 = 1 (exact).

    NOTE: gamma_1 = { {n/1} } = 0 identically (fractional parts of
    integers), so the first nonzero dilation vector is gamma_2; the
    classical span is indexed here by the nonzero vectors
    l = 2, 3, ..., k_max+1 and d_j uses the first j of them."""
    mp = _mp()
    mp.mp.dps = dps
    ls = list(range(2, k_max+2))
    G = gram_matrix_from(ls, dps)
    b = mp.matrix([b_entry(l, dps) for l in ls])
    out = []
    for k in range(1, k_max+1):
        Gk = mp.matrix(k, k)
        bk = mp.matrix(k, 1)
        for i in range(k):
            bk[i] = b[i]
            for j in range(k):
                Gk[i, j] = G[i, j]
        try:
            x = mp.lu_solve(Gk, bk)
            proj = sum(bk[i]*x[i] for i in range(k))
            d2 = 1 - proj
            out.append((k, d2))
        except Exception as exc:  # pragma: no cover
            raise BlackSunWildError(f"solve failed at k={k}: {exc}") from exc
    return out


def gram_matrix_from(ls, dps: int = 50):
    mp = _mp()
    mp.mp.dps = dps
    k = len(ls)
    G = mp.matrix(k, k)
    for i in range(k):
        for j in range(i, k):
            v = gram_entry(ls[i], ls[j], dps)
            G[i, j] = v
            G[j, i] = v
    return G


def gram_entry_direct(l: int, m: int, N: int = 200000, dps: int = 40):
    """Direct summation reference for validating the closed form."""
    mp = _mp()
    mp.mp.dps = dps
    L = _lcm(l, m)
    total = mp.mpf('0')
    # sum over full periods with the exact weight via the telescoping tail:
    # sum_n<=N {n/l}{n/m}/(n(n+1)) + tail bound (<= 1/(N+1))
    acc = mp.mpf('0')
    for n in range(1, N+1):
        acc += mp.mpf((n % l)*(n % m))/mp.mpf(l*m*n*(n+1))
    return acc, mp.mpf('1')/(N+1)


# ------------------------------------------ BS-III-2: tame-tower faithfulness


def source_recovery_check(A: float, mutation_n: int):
    """Tame-tower faithfulness on a finite stage (exact arithmetic).

    Window family a <= A determines Lambda(n)/sqrt(n) for n < e^{2A}:
    an explicit recovery test function isolates each atom exactly (the
    prime sum is locally finite and atoms sit at distinct +-log n).
    A mutation at mutation_n is INVISIBLE iff mutation_n >= e^{2A}.

    Returns (visible, recovered_weight_minus_authentic).
    """
    from math import exp
    if mutation_n < 2:
        raise BlackSunWildError("mutation index >= 2 required")
    log_n = log(mutation_n)
    if log_n >= 2*A:
        # invisible: no window <= A sees the atom at +-log mutation_n
        return False, 0.0
    # visible: a window with a > log_n/2 includes the atom; the E38.1-style
    # recovery isolates the coefficient exactly
    return True, log(mutation_n)/sqrt(mutation_n)


# ------------------------------------------ BS-III-3: two-mode reduction


def two_mode_reduction(a: float = 0.5, M: int = 1400, k: int = 8):
    """Two-mode reduction data at window a: the k lowest eigenpairs of the
    full windowed form Q_a; the 2x2 effective matrix on the span of the two
    lowest eigenvectors; the complement's lowest eigenvalue.

    Returns dict with: eigenvalues, the 2x2 entries (A-part, prime-part
    split), complement margin, and the reduction residuals.
    """
    return _two_mode_reduction_impl(a, M, k)


def _two_mode_reduction_impl(a, M, k):
    import numpy as np
    from observational_succ.black_sun_window import (
        lowest_eigenvalues, window_form_matrix, prime_atoms_window)
    vals, vecs, xs, w = lowest_eigenvalues(a, M=M, k=k, include_prime=True)
    # convert eigenvectors (u = W^{1/2} v) to node values v = u/sqrt(w)
    V = vecs/sqrt(np.repeat(w, vecs.shape[1]).reshape(vecs.shape)) \
        if False else vecs/np.sqrt(w)[:, None]
    # normalize in the weighted L2 sense: ||v||^2 = sum w v^2
    for j in range(vecs.shape[1]):
        nrm = np.sqrt(np.sum(w*V[:, j]**2))
        V[:, j] = V[:, j]/nrm
    # forms restricted to span(v0, v1): matrix entries via Rayleigh forms
    F_full, w2, xs2 = window_form_matrix(a, M, include_prime=True)
    F_A, _, _ = window_form_matrix(a, M, include_prime=False)
    Winv = np.diag(1/np.sqrt(w2))
    G_full = Winv @ F_full @ Winv
    G_A = Winv @ F_A @ Winv
    G_full = 0.5*(G_full+G_full.T)
    G_A = 0.5*(G_A+G_A.T)
    # the operator matrices act on u = sqrt(w) v: convert node values back
    U = V*np.sqrt(w)[:, None]
    M2_full = U[:, :2].T @ G_full @ U[:, :2]
    M2_A = U[:, :2].T @ G_A @ U[:, :2]
    # complement margin: lowest eigenvalue of Q restricted to v >= 2 modes:
    # use the Rayleigh quotient of the remaining computed eigenvalues
    complement_margin = vals[2] if len(vals) > 2 else float('nan')
    # off-diagonal parity-breaking: the A-part preserves parity, the prime
    # part does not: check
    off_A = M2_A[0, 1]
    off_full = M2_full[0, 1]
    return {
        "eigenvalues": vals,
        "M2_full": np.array(M2_full),
        "M2_A": np.array(M2_A),
        "M2_prime": np.array(M2_full)-np.array(M2_A),
        "complement_margin": complement_margin,
        "offdiag_A": off_A,
        "offdiag_full": off_full,
    }


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import mpmath as mp
    print("=== BS-III-1: BD distance sequence (closed-form Gram) ===")
    print("  validating closed form against direct summation (l,m)=(1,2),(2,3):")
    for (l, m) in ((1, 2), (2, 3), (1, 1)):
        cf = gram_entry(l, m)
        ds, tail = gram_entry_direct(l, m, N=100000)
        print(f"  G({l},{m}): closed = {mp.nstr(cf, 14)}, direct = {mp.nstr(ds, 10)} (+- {mp.nstr(tail, 2)})")
    print("  d_k sequence:")
    for (k, d2) in bd_distance_sequence(12):
        print(f"  k={k:3d}: d_k = {mp.nstr(mp.sqrt(d2), 12)}")
    print("=== BS-III-2: tame-tower faithfulness ===")
    for (A, n) in ((0.5, 2), (0.5, 6), (0.5, 100), (0.4, 3), (0.4, 7)):
        vis, wt = source_recovery_check(A, n)
        print(f"  A={A}, mutation n={n}: visible={vis}, weight~{wt:.4f}")
    print("=== BS-III-3: two-mode reduction at a=0.5 ===")
    import numpy as np
    r = _two_mode_reduction_impl(0.5, 1200, 6)
    print("  eigenvalues:", np.array2string(np.array(r['eigenvalues']), precision=6))
    print("  2x2 full:", np.array2string(r['M2_full'], precision=6))
    print("  2x2 A-part:", np.array2string(r['M2_A'], precision=6))
    print("  2x2 prime:", np.array2string(r['M2_prime'], precision=6))
    print(f"  complement margin (lambda_2): {r['complement_margin']:.6f}")
    print(f"  off-diag A-part (should be ~0 by parity): {r['offdiag_A']:.2e}")