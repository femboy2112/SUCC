"""Independent exact local audit: prime-only rational Fourier camouflage.
Trial-division primality, ordinary loops, no SUCC helper imports.
This is finite evidence, not a Goldbach theorem.
"""
import json
from math import gcd, isqrt

def is_prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))

def run():
    N = 4200
    M = 420
    base = {k for k in range(2, N + 1) if is_prime(k)}
    witnesses = [(a, N - a) for a in range(2, N // 2 + 1)
                 if a in base and N - a in base]
    removed = {a for a, b in witnesses}
    fake = base - removed
    tail = [k for k in range(N + 1, 45000) if is_prime(k)]
    matches = {u: [k for k in tail if k % M == u]
               for u in set(k % M for k in removed)}
    used = set()
    for d in sorted(removed):
        k = next(k for k in matches[d % M] if k not in used)
        used.add(k)
        fake.add(k)
    original_hist = [sum(k % M == r for k in base) for r in range(M)]
    mutant_hist = [sum(k % M == r for k in fake) for r in range(M)]
    assert original_hist == mutant_hist
    assert len(base) == len(fake) == 574
    assert len(witnesses) == 165
    assert not any((N - k) in fake for k in fake if 2 <= N - k)
    z = 0
    while (z + 1) ** 3 <= N:
        z += 1
    composites = {k for k in range(2, N + 1) if not is_prime(k)
                  and all(k % l for l in range(2, z + 1) if is_prime(l))}
    cc = sum((N - a) in composites for a in composites if N - a >= 2)
    original_R = sum((N - a) in base for a in base if N - a >= 2)
    fake_R = sum((N - a) in fake for a in fake if N - a >= 2)
    assert (original_R, cc, fake_R) == (330, 50, 0)
    local = {}
    for m in (2, 6, 12, 30):
        units = [u for u in range(m) if gcd(u, m) == 1]
        counts = [sum((u + v) % m == r for u in units for v in units)
                  for r in range(m)]
        assert sum(counts) == len(units) ** 2
        local[str(m)] = counts
    return {
        "method": "independent trial division; exact residue histograms",
        "N": N, "M": M, "source_prime_count": len(base),
        "Goldbach_unordered_original": len(witnesses),
        "Goldbach_unordered_mutant": 0, "all_modes_q_le_7_equal": True,
        "rough_semiprime_pairs_ordered": cc,
        "original_signed_margin": original_R - cc,
        "mutant_signed_margin": fake_R - cc,
        "cyclic_local_counts": local,
    }

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
