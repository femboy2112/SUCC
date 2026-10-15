"""BLACK SUN C-track: Collatz additive/multiplicative defect dictionary.

Campaign: Operation Black Sun, 2026-10-14.

Exact finite-arithmetic objects, no probabilistic heuristics:

  BS-C1 (PROVED LOCAL, defect cocycle): for a parity word
      eps in {0,1}^m with k = sum eps_j and
      c_eps = sum_{j: eps_j=1} 2^j 3^{K_j},  K_j = sum_{l>j} eps_l,
      the shortcut map satisfies
          2^m T^m(n) = 3^k n + c_eps,
      and an m-cycle through n exists iff
          n (2^m - 3^k) = c_eps,  i.e.  n = c_eps / (2^m - 3^k) > 0.

  BS-C2 (PROVED LOCAL, valuation dictionary): with D = 2^m - 3^k,
      v_3(c_eps) = 0 (the last one contributes 2^{j*} not divisible by 3,
      all earlier ones are divisible by 3), and v_3(D) = 0 (2^m = +-1 mod 3).
      Hence v_3(n) = 0 for every element of every Collatz cycle: no cycle
      element is divisible by 3.  For p >= 5, p != 2,3:
          v_p(n) = v_p(c_eps) - v_p(D),
      with {(m,k): v_p(D) >= j} an explicit p-adic lattice coset
      (example p=5: v_5(D)>=1 iff m == 3k mod 4, since 2 generates (Z/5)*
      and 3 = 2^3 there).

  BS-C3 (PROVED LOCAL, finite chart): the parity chart chi_m:
      Z/2^m -> (Z/2)^m is a bijection: exactly one residue class per
      parity word.  NO-GHOST scope: the 2-adic conjugacy to the shift lives
      on Z_2; the Archimedean descent condition n > c_eps/(2^m-3^k) does
      NOT transport along it; termination is exactly the statement that
      the good-word half-lines cover all positive integers.

No Collatz claim is made beyond these exact statements.
"""
from __future__ import annotations


class BlackSunCTrackError(ValueError):
    pass


def shortcut_step(n: int) -> int:
    """T(n) = n/2 if even else (3n+1)/2."""
    if type(n) is not int or n <= 0:
        raise BlackSunCTrackError("positive integer required")
    return n//2 if n % 2 == 0 else (3*n+1)//2


def iterate_word(n: int, eps: list[int]) -> tuple[int, int]:
    """Apply T per eps (eps_j=1 means odd step at position j); returns
    (T^m(n), actual parity mismatch count) for validation."""
    m = len(eps)
    cur = n
    mism = 0
    for j in range(m):
        par = cur % 2
        if par != eps[j]:
            mism += 1
        cur = shortcut_step(cur)
    return cur, mism


def defect_cocycle(eps: list[int]) -> tuple[int, int, int]:
    """(m, k, c_eps): 2^m T^m(n) = 3^k n + c_eps for any n realizing eps."""
    m = len(eps)
    k = sum(eps)
    c = 0
    for j in range(m):
        if eps[j]:
            K_j = sum(eps[j+1:])
            c += (2**j) * (3**K_j)
    return m, k, c


def forced_word_map(n, eps: list[int]):
    """The ALGEBRAIC branch composition over Fractions: eps_j=1 applies the
    affine odd branch (3x+1)/2 even if x is even (unrealizable off-orbit);
    eps_j=0 applies x/2.  Returns a Fraction.  The cocycle identity
    2^m (word map)(x) = 3^k x + c_eps holds for this composition as an
    identity of affine maps over Q; realizability is the additional
    integrality/parity condition."""
    from fractions import Fraction
    cur = Fraction(n)
    for e in eps:
        cur = (3*cur+1)/2 if e else cur/2
    return cur


def verify_defect_cocycle(eps: list[int], n0: int) -> bool:
    """Exact check: 2^m T^m(n) == 3^k n + c_eps on an actual realizing orbit."""
    m, k, c = defect_cocycle(eps)
    cur, mism = iterate_word(n0, eps)
    if mism:
        # the word must be the actual parity sequence of n0
        return False
    return (2**m)*cur == (3**k)*n0 + c


def cycle_equation(m: int, k: int, c: int) -> tuple[bool, int]:
    """Positive integer m-cycle exists for (m,k,c) iff 2^m > 3^k and
    (2^m - 3^k) | c; returns (exists, n)."""
    D = 2**m - 3**k
    if D <= 0 or c <= 0:
        return False, 0
    if c % D:
        return False, 0
    return True, c//D


def v_p(n: int, p: int) -> int:
    if type(n) is not int or type(p) is not int or p < 2 or n == 0:
        raise BlackSunCTrackError("bad input")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def valuation_dictionary(eps: list[int]) -> dict:
    """Exact dictionary for the cycle candidate n = c_eps/(2^m-3^k)."""
    m, k, c = defect_cocycle(eps)
    D = 2**m - 3**k
    out = {"m": m, "k": k, "c": c, "D": D,
           "v3_c": v_p(c, 3), "v3_D": v_p(D, 3) if D else None,
           "realizable_positive": D > 0 and c % D == 0}
    if out["realizable_positive"]:
        n = c//D
        out["n"] = n
        out["v3_n"] = v_p(n, 3)
        out["divisible_by_3"] = n % 3 == 0
    return out


def p_lattice_coset(p: int, j: int = 1) -> dict:
    """The p-adic lattice condition {(m,k): 2^m == 3^k mod p^j}.

    Returns generator-based description: 2 = g^u, 3 = g^v in (Z/p^j)* when
    both lie in a common cyclic subgroup; the condition is the linear
    congruence u*m == v*k (mod ord(g)).
    """
    if type(p) is not int or p < 5 or p in (2, 3):
        raise BlackSunCTrackError("prime p >= 5 required")
    # check p prime
    for d in range(2, int(p**0.5)+1):
        if p % d == 0:
            raise BlackSunCTrackError("p must be prime")
    mod = p**j
    # discrete log table of (Z/mod)* is cyclic for odd prime powers
    g = 2
    # find a generator
    phi = mod - mod//p
    def order(x):
        o = 1
        cur = x % mod
        while cur != 1:
            cur = cur*x % mod
            o += 1
            if o > phi:
                return None
        return o
    gen = None
    for cand in range(2, mod):
        if order(cand) == phi:
            gen = cand
            break
    if gen is None:
        return {"p": p, "j": j, "cyclic_generator": None}
    # indices of 2 and 3: dlog[gen^e] = e for e = 0..phi-1
    cur = 1
    dlog = {}
    for e in range(phi):
        dlog[cur] = e
        cur = cur*gen % mod
    u, v = dlog.get(2), dlog.get(3)
    return {"p": p, "j": j, "generator": gen, "u=dlog(2)": u,
            "v=dlog(3)": v, "phi": phi,
            "condition": (f"{u}*m == {v}*k (mod {phi})"
                          if u is not None and v is not None else None)}


def no_small_cycles(M: int) -> tuple[bool, list]:
    """Exact finite certificate: no positive integer m-cycle with m <= M
    except the trivial cycle through n=1 (which has k ones in its word).

    Enumerates all parity words of length m (m <= M), solves the cycle
    equation exactly.  Returns (ok, nontrivial_cycles_found).
    """
    if type(M) is not int or M < 1 or M > 26:
        raise BlackSunCTrackError("1 <= M <= 26 (exact enumeration bound)")
    found = []
    for m in range(1, M+1):
        for mask in range(2**m):
            eps = [(mask >> j) & 1 for j in range(m)]
            mk, k, c = defect_cocycle(eps)
            D = 2**mk - 3**k
            if D <= 0:
                continue
            if c % D == 0:
                n = c//D
                if n > 0:
                    # verify: does this word actually realize a cycle at n?
                    cur, mism = iterate_word(n, eps)
                    if mism == 0 and cur == n:
                        found.append((m, k, n))
    # the trivial cycle: n=1: 1 -> 2 -> 1: word (1,0) length 2: T(1)=2, T(2)=1
    ok = all(n == 1 or n == 2 for (_, _, n) in found)
    return ok, found


if __name__ == "__main__":
    ok, found = no_small_cycles(18)
    print("no nontrivial cycles m<=18:", ok, "found:", found)
    print("p=5 lattice:", p_lattice_coset(5))
    print("valuation dictionary of the trivial cycle word (1,0):",
          valuation_dictionary([1, 0]))