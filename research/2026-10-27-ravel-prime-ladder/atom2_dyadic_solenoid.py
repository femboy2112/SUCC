"""Atom 2: the dyadic solenoid — exact finite<->global correspondence.

Author: Ravel (building on Atom 1 = first_atom.py, Z_2, dual Z[1/2]/Z).
Date: 2026-10-27. Branch: research/prime-ladder-ravel-audit-2026-10-27.

Object:
    Dyadic solenoid  X = (R x Z_2) / Delta Z.
    Character group  X^ = Z[1/2]  (the dyadic rationals — FULL group, NOT mod Z).
    Finite layers     L_n = Z/2^n  (2-adic coordinate mod 2^n), characters
                      chi_a(x) = e(a x / 2^n),  a in Z/2^n.

Correspondence (the payload, proved locally):
    global dyadic  t = m/2^k  ->  finite char  Phi_n(t)(x) = e(t x)  on L_n.
    surjective at every n  (a in Z/2^n lifts to t = a/2^n),
    cofinal (the tower L_n), injective in the inverse limit
    (t == t' at all levels  =>  t - t' in cap_n 2^n Z = {0}).

Discipline (AGENTS.md): exact Fraction arithmetic only, NO floats.  Status labels
honest: CLASSICAL for the Pontryagin dual identifications, PROVED LOCAL for the
correspondence.  NO claim about equidistribution/normality/pi-orbit invariance —
this is a structural isomorphism of observables only.
"""

from fractions import Fraction
import itertools


def e_ratio(p: Fraction, q: int) -> str:
    """Render a rational p (mod 1) as a string 'num/q' for exact display (no float)."""
    p = p % 1
    num = p.numerator
    den = p.denominator
    # rescale to denominator q
    return f"{num * (q // den)}/{q}"


def finite_char_values(a: int, n: int) -> list:
    """Values of chi_a on L_n = Z/2^n, as exact fractions ax/2^n mod 1."""
    q = 2 ** n
    return [Fraction((a * x) % q, q) for x in range(q)]


def global_char_values(t: Fraction, n: int) -> list:
    """Restriction of global dyadic char e(t x) to L_n = Z/2^n, exact."""
    q = 2 ** n
    return [Fraction((t * x) % 1) for x in range(q)]


def restrict_signature(t: Fraction, n: int) -> int:
    """The finite character index a in Z/2^n that Phi_n(t) equals.

    Phi_n(t)(x) = e(t x) on x in Z/2^n.  This equals chi_a with a = t mod 2^n,
    where t = m/2^k.  Write t = m/2^k, then t * 2^n mod 2^n = m*2^{n-k} mod 2^n
    (for k <= n; if k > n the char still lands in Z/2^n by reducing).
    """
    q = 2 ** n
    # a = t * q mod q (exact, integer-valued result)
    a = (t * q) % q
    return int(a)


def check_surjectivity(n: int) -> bool:
    """Every finite char a in Z/2^n is reached from a global dyadic t = a/2^n."""
    q = 2 ** n
    reached = set()
    for a in range(q):
        t = Fraction(a, q)          # global dyadic
        reached.add(restrict_signature(t, n))
    return reached == set(range(q))


def check_injectivity_in_limit(K: int) -> bool:
    """Distinct dyadics t in [0,1) with denominator dividing 2^K have distinct
    finite signatures (Phi_n(t))_{n<=K}; i.e. injectivity up to level K."""
    q = 2 ** K
    sigs = {}
    for m in range(q):
        t = Fraction(m, q)
        sig = tuple(restrict_signature(t, n) for n in range(1, K + 1))
        if sig in sigs and sigs[sig] != t:
            return False
        sigs[sig] = t
    return len(sigs) == q


def cofinality_union(K: int) -> int:
    """Size of the nested union of level-n dyadic subgroups up to level K,
    intersected with [0,1):  | union_{n<=K} (1/2^n)Z mod 1 | = 2^K."""
    vals = set()
    for n in range(1, K + 1):
        q = 2 ** n
        for m in range(q):
            vals.add(Fraction(m, q))
    return len(vals)


def main() -> None:
    print("=== ATOM 2: dyadic solenoid — exact finite<->global correspondence ===")
    print("X = (R x Z_2)/Delta Z,  X^ = Z[1/2],  finite layers L_n = Z/2^n.")
    print("All arithmetic exact (fractions.Fraction); no floats.")
    print()

    # 1. Exhibit a finite layer and its characters.
    n_demo = 3
    print(f"Finite layer L_{n_demo} = Z/2^{n_demo}: characters chi_a(x) = e(a x/2^{n_demo}):")
    for a in range(2 ** n_demo):
        vals = finite_char_values(a, n_demo)
        print(f"  a={a}: " + " ".join(
            f"{v.numerator}/{v.denominator}" for v in vals))
    print()

    # 2. Surjectivity: every finite char lifts to a global dyadic char.
    print("--- Surjectivity (every finite char lifts to a global dyadic char) ---")
    surj_ok = True
    for n in range(1, 9):
        ok = check_surjectivity(n)
        surj_ok &= ok
        print(f"  n={n}: |Z/2^n| = {2**n}, reached from global dyadic = {2**n}, "
              f"surjective = {ok}")
    print(f"  ALL surjective: {surj_ok}")
    print()

    # 3. Injectivity in the inverse limit (distinct dyadics -> distinct signatures).
    print("--- Injectivity in the inverse limit (distinct global -> distinct finite signature) ---")
    inj_ok = True
    for K in range(1, 9):
        ok = check_injectivity_in_limit(K)
        inj_ok &= ok
        print(f"  K={K}: {2**K} dyadics -> {2**K} distinct signatures, injective = {ok}")
    print(f"  ALL injective: {inj_ok}")
    print()

    # 4. Cofinality: the nested union of level subgroups.
    print("--- Cofinality (nested union of level-n dyadic subgroups) ---")
    for K in range(1, 9):
        sz = cofinality_union(K)
        print(f"  K={K}: | union of (1/2^n)Z for n<=K, mod 1 | = {sz} (== 2^K = {2**K}: {sz == 2**K})")
    print()

    # 5. Explicit round-trip example: finite -> global -> finite.
    print("--- Round-trip example (finite -> global -> finite) ---")
    for (a, n) in [(5, 3), (7, 4), (1, 8)]:
        t = Fraction(a, 2 ** n)
        back = restrict_signature(t, n)
        print(f"  finite char a={a} on Z/2^{n} -> global t={t} -> restrict -> a={back} "
              f"(round-trip: {back == a})")
    print()

    # 6. Explicit injectivity witness: t=1/4 vs t=1/8 differ at level 3.
    t1, t2 = Fraction(1, 4), Fraction(1, 8)
    s1 = [restrict_signature(t1, n) for n in range(1, 5)]
    s2 = [restrict_signature(t2, n) for n in range(1, 5)]
    print("Injectivity witness: t=1/4 and t=1/8")
    print(f"  signature(1/4) = {s1}")
    print(f"  signature(1/8) = {s2}")
    print(f"  distinct at some level <=4: {s1 != s2}")
    print()

    # Summary / boundary.
    print("=== VERDICT ===")
    print(f"  Surjectivity (n=1..8):       {surj_ok}")
    print(f"  Injectivity in limit (K=1..8): {inj_ok}")
    print("  STATUS: PROVED LOCAL (correspondence, elementary + exact finite check).")
    print("  Dual identifications (X^=Z[1/2], L_n^=Z/2^n): CLASSICAL (Pontryagin).")
    print("  BOUNDARY: structural isomorphism of observables ONLY —")
    print("  no equidistribution / normality / pi-orbit-invariance claim is made.")


if __name__ == "__main__":
    main()
