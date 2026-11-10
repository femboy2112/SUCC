"""SUCC pinbed energy / exact near-return research probe.

Finite arithmetic controls.  This is NOT a proof of pi normality.
All equality/inequality assertions below use Fraction.
"""
from fractions import Fraction as Q

def frac(x):
    return x % 1

def dtorus(x, y):
    delta = abs(frac(x) - frac(y))
    return min(delta, 1 - delta)

def orbit(seed, start, size, base=16):
    return [frac(seed * base**n) for n in range(start, start + size)]

def pin_energy(values, q):
    assert q >= 2
    N = len(values)
    return Q(q, N*N) * sum(
        (max(Q(0), 1 - q * dtorus(x,y)) for x in values for y in values),
        Q(0))

def source_return_energy(seed, A, q):
    N = A
    s = Q(A)
    for lag in range(1, A):
        for n in range(A, 2*A-lag):
            x = frac((16**lag-1)*16**n*seed)
            s += 2*max(Q(0), 1-q*min(x,1-x))
    return q*s/(A*A)

def forcing(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)

def finite_state(n):
    u = Q()
    for j in range(1,n+1):
        u = 16*u + forcing(j)
    return u

def finite_completed(n,L):
    return 16**n*sum((forcing(j)/16**j for j in range(1,L+1)), Q())

def verify():
    seeds = [Q(0),Q(1,255),Q(1,257),Q(int("0123456789ABCDEF",16),16**16-1)]
    checked = 0
    for a in seeds:
        for A in [8,16,24]:
            xs = orbit(a,A,A)
            for q in [8,16,64]:
                assert pin_energy(xs,q) == source_return_energy(a,A,q)
                assert pin_energy(xs,q) >= 1
                checked += 1

    # A fixed nonnormal orbit has pin energy growing with q.
    for q in [32,64,256]:
        xs=orbit(Q(1,255),16,16)
        assert pin_energy(xs,q) == Q(q,2)

    # Source truncation is an exact positive correction.
    for A in [3,5]:
        for L in [2*A,2*A+4]:
            xs=[frac(finite_state(n)) for n in range(A,2*A)]
            ys=[frac(finite_completed(n,L)) for n in range(A,2*A)]
            shifts = [
                sum((Q(16)**(n-j)*forcing(j) for j in range(n+1,L+1)), Q())
                for n in range(A,2*A)]
            assert all(frac(xs[i]+shifts[i]) == ys[i] for i in range(A))
            for q in [4,8,16]:
                assert abs(pin_energy(xs,q)-pin_energy(ys,q)) <= 2*q*q*max(shifts)
                checked += 1
    # Exact two-index source-cocycle sheet. Verified for raw rational BBP.
    for n in range(1,9):
        for lag in range(1,7):
            d = finite_state(n+lag) - finite_state(n)
            d_next = finite_state(n+lag+1) - finite_state(n+1)
            assert d_next == 16*d + forcing(n+lag+1) - forcing(n+1)
            # Exact finite-horizon completion (no irrational oracle).
            horizon = n + lag + 4
            y_d = finite_completed(n+lag,horizon)-finite_completed(n,horizon)
            y_dnext = finite_completed(n+lag+1,horizon)-finite_completed(n+1,horizon)
            assert y_dnext == 16*y_d
            checked += 1

    print(f"Exact rational probes: {checked} comparison cases PASSED")
    print("Period-2 coherent orbit pin energies:",
          [(q,str(pin_energy(orbit(Q(1,255),16,16),q)))
           for q in (32,64,256)])
    print("Scope: finite identities and wrong-seed controls only; NO pi asymptotics.")

if __name__=="__main__":
    verify()