"""Independent exact cross-check without importing signed_sieve or using FFT/NTT."""
from math import isqrt
import json

def trialprime(n):
    if n < 2: return False
    return all(n % d for d in range(2,isqrt(n)+1))

def cube_floor(n):
    k=0
    while (k+1)**3 <= n: k+=1
    return k

def audit(limit=8192):
    prime=[trialprime(k) for k in range(limit+1)]
    rough_composites={}
    # Prime- *and* rough-composite source masks recomputed by trial divisor search.
    for z in range(cube_floor(limit)+1):
        small=[p for p in range(2,z+1) if trialprime(p)]
        rough_composites[z]=[not prime[k] and k>=2 and all(k%p for p in small)
                             for k in range(limit+1)]
    first_failure=0
    min_l=None
    for N in range(4,limit+1,2):
        z=cube_floor(N)
        c=rough_composites[z]
        R=sum(prime[a] and prime[N-a] for a in range(2,N-1))
        C=sum(c[a] and c[N-a] for a in range(2,N-1))
        L=R-C
        if min_l is None or L<min_l:min_l=L
        if L<=0 and not first_failure:first_failure=N
    return {"method":"independent trial divisor primality and roughness, direct pair loops",
            "limit":limit,"even_targets":limit//2-1,"least_signed":min_l,
            "first_failure":first_failure}

if __name__=='__main__':
    print(json.dumps(audit(),sort_keys=True))
