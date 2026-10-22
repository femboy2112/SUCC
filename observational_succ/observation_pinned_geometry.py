"""Reality-calibrated arithmetic source -> intrinsic p-adic geometry (exact finite oracles).

Conditional mathematics only: a *source-faithful, oriented*, procyclic,
compatible p-power ring quotient tower identifies Z_p and its ball tree.
The projective 2-channel lift gives the genuine PGL2(Q_p) Bruhat--Tits tree.
An empirical finite observation *alone* cannot certify the tower axioms,
physical spacetime, a holographic quantum state, or signed Weil positivity.

No floating arithmetic. Imported theoretical results are attributed in dossier.
"""
from __future__ import annotations

from fractions import Fraction
from math import isqrt


class ObservationContractError(ValueError):
    """Missing source calibration, invalid place, topology, or instrument."""


def _int(n, minimum=None):
    if type(n) is not int or (minimum is not None and n < minimum):
        raise ObservationContractError("integer of the specified range required")
    return n


def prime(p):
    return type(p) is int and p >= 2 and all(p % d for d in range(2,isqrt(p)+1))


def _p(p):
    if not prime(p):
        raise ObservationContractError("genuine prime place required")
    return p


def _level(k, max_level=10):
    _int(k,1)
    if k > max_level:
        raise ObservationContractError("finite oracle resource bound exceeded")
    return k


def qphase(n,p,k):
    """Actual source n mod p^k, negative source integers also supported."""
    _int(n);_p(p);_level(k)
    return n % (p**k)


def src_affine_phase(n,a,b,p,k):
    """SUCC (1,1), FUCC (q,0) source-natural at every quotient level."""
    _int(n);_int(a,1);_int(b,0)
    return qphase(a*n+b,p,k)


def phase_affine(r,a,b,p,k):
    _int(r);_int(a,1);_int(b,0);_p(p);_level(k)
    if not 0 <= r < p**k:
        raise ObservationContractError("phase outside specified source quotient")
    return (a*r+b)%(p**k)


def parent(p,k,r):
    _p(p);_level(k);_int(r,0)
    if r>=p**k:
        raise ObservationContractError("invalid current congruence cell")
    return (k-1,r%(p**(k-1)))


def children(p,k,r):
    """The *full* p-adic rooted ball tree, not three manually chosen rays."""
    _p(p);_int(k,0)
    if k>9 or type(r) is not int or not 0<=r<p**k:
        raise ObservationContractError("invalid source cell or resource bound")
    return tuple((k+1, r+j*p**k) for j in range(p))


def haar_mass(p,k):
    _p(p);_int(k,0)
    if k>40:
        raise ObservationContractError("finite Haar oracle level too large")
    return Fraction(1,p**k)


def valuation_diff(n,m,p):
    """v_p(n-m), None if equal (infinite order)."""
    _int(n);_int(m);_p(p)
    v=0
    x=abs(n-m)
    if not x:return None
    while x%p==0:
        v+=1
        x//=p
    return v


def haar_calibrated_distance(n,m,p):
    """Haar mass of smallest common p-adic ball (a chosen metric convention)."""
    v=valuation_diff(n,m,p)
    return Fraction(0) if v is None else Fraction(1,p**v)


def truncated_distance_report(n,m,p,k):
    """Finite observation cannot resolve separations beyond depth k."""
    _level(k)
    v=valuation_diff(n,m,p)
    if v is None or v>=k:
        return {"kind":"unresolved", "distance_upper_bound":Fraction(1,p**k)}
    return {"kind":"exact", "distance":Fraction(1,p**v)}


def multiplier_image_count(m,p,k):
    """Number of outcomes of x -> mx on ring Z/p^k.

    Genuine primitive generator status is a SEPARATE source check.
    """
    _int(m,1);_p(p);_level(k)
    v=0
    t=m
    while t%p==0:
        t//=p
        v+=1
    return p**max(k-v,0)


def multiplier_kernel_count(m,p,k):
    _int(m,1);_p(p);_level(k)
    return p**k//multiplier_image_count(m,p,k)


def projective_first_shell(p):
    """P^1(F_p): represented by z in Fp and infinity (None)."""
    _p(p)
    return tuple(range(p))+(None,)


def projective_succ(point,p):
    _p(p)
    if point is None: return None
    _int(point,0)
    if point>=p:raise ObservationContractError("point outside P^1(Fp)")
    return (point+1)%p


def projective_multiplier(point,q,p):
    """Only p-adic units act on the same *root shell* by invertible reduction."""
    _p(p);_int(q,1)
    if q%p==0:
        raise ObservationContractError("nonunit dilation MOVES the root vertex; not a root-shell permutation")
    if point is None:return None
    _int(point,0)
    if point>=p:raise ObservationContractError("point outside P1(Fp)")
    return (q*point)%p


def matrix_affine(a,b):
    _int(a,1);_int(b,0)
    return ((a,b),(0,1))


def matrix_compose(A,B):
    if any(len(row)!=2 for row in A+B):
        raise ObservationContractError("2x2 matrix required")
    return tuple(tuple(sum(A[i][l]*B[l][j] for l in range(2))
                       for j in range(2)) for i in range(2))


def projective_matrix_point(matrix,point,p):
    """Independent homogeneous-coordinate oracle for GL2(Zp) shell action."""
    _p(p)
    a,b=matrix[0]; c,d=matrix[1]
    det=a*d-b*c
    if det%p==0:raise ObservationContractError("matrix not invertible modulo p")
    x,y=(1,0) if point is None else (point,1)
    u=(a*x+b*y)%p
    v=(c*x+d*y)%p
    if v==0:return None
    return (u*pow(v,-1,p))%p


def first_shell_cycle_fingerprint(p):
    _p(p)
    actual={x:projective_succ(x,p) for x in projective_first_shell(p)}
    assert actual[None] is None
    orbit=[0]
    while len(orbit)<p:
        orbit.append(actual[orbit[-1]])
    assert set(orbit)==set(range(p)) and actual[orbit[-1]]==0
    return {"root_degree":p+1,"fixed_directions":(None,),
            "nonfixed_cycle":tuple(orbit),"period":p}


def axis_vertex(p,k):
    """Full BT axis [Zp * p^k e1 + Zp * e2], k any integer."""
    _p(p);_int(k)
    return (Fraction(p)**k,Fraction(1))


def axis_distance(p,i,j):
    """Graph distance of diagonal lattice homothety classes on standard axis."""
    _p(p);_int(i);_int(j)
    return abs(i-j)


def dilation_root_displacement(q,p):
    """Translation distance in BT of diag(q,1) at the root = |v_p(q)|."""
    _int(q,1);_p(p)
    v=0
    while q%p==0:
        q//=p;v+=1
    return v


def canonical_fixed_ray(p,k):
    """Unique p^k-phase fixed by x -> p*x: phase 0; shifted n-1 coordinate -1."""
    _p(p);_level(k)
    if p**k > 10000:
        raise ObservationContractError("exact fixed-phase census exceeds budget")
    return {"integer_phase":0,"shifted_phase":p**k-1,
            "fixed_phases":tuple(r for r in range(p**k) if (p*r-r)%(p**k)==0)}


def oriented_cycle_probe(phase_labels,candidate_primes,source_id,instrument_id):
    """Faithful-clock OBSERVATION CONTRACT, not a physical measurement by code.

    Require at least 2 complete cycles with source labels, full discriminable
    states, and a repeated deterministic single-event phase transition.
    Caller must independently verify sensor fidelity, reset, and drift.
    """
    if not source_id or not instrument_id or not isinstance(source_id,str) or not isinstance(instrument_id,str):
        raise ObservationContractError("physical source and calibrated instrument identities required")
    if type(phase_labels) not in (tuple,list) or len(phase_labels)<5:
        raise ObservationContractError("2 full repeated clock cycles required")
    labels=tuple(phase_labels)
    try: distinct=len(set(labels))
    except TypeError as e:raise ObservationContractError("hashable phase reports required") from e
    candidates=tuple(_p(p) for p in candidate_primes)
    if not candidates or len(set(candidates))!=len(candidates):
        raise ObservationContractError("nonempty distinct candidate prime family required")
    found=[]
    for p in candidates:
        if len(labels)<2*p+1 or len(set(labels[:p]))!=p or labels[p]!=labels[0]:
            continue
        if all(labels[i]==labels[i%p] for i in range(len(labels))):
            found.append(p)
    if len(found)!=1:
        raise ObservationContractError("no uniquely supported faithful primitive clock in declared family")
    return {"selected_p":found[0],"source_id":source_id,"instrument_id":instrument_id,
            "scope":"conditional finite phase observation; not whole-system source authentication",
            "full_infinite_tower_empirically_verified":False}


def counterfeit_extension_orders(p,K,alien_prime=None):
    """Compatible source ring moduli equal p^k through K, diverge afterwards.

    The infinite inverse system from this coherent divisible list is NOT
    the strict p-power tower. This witnesses finite observation insufficiency.
    """
    _p(p);_int(K,1)
    if K>9:raise ObservationContractError("finite mutation depth too high")
    other=(3 if p!=3 else 2) if alien_prime is None else _p(alien_prime)
    if other==p:raise ObservationContractError("mutation needs independent new prime")
    actual=tuple(p**k for k in range(1,K+3))
    mutant=tuple(p**k if k<=K else p**k*other for k in range(1,K+3))
    if not all(mutant[i+1]%mutant[i]==0 for i in range(len(mutant)-1)):
        raise ArithmeticError("counterexample must itself be a lawful inverse system")
    return actual,mutant


def hidden_four_state_alias():
    """Exact finite observer limitation: C4 observed through parity mimics C2."""
    true_states=tuple(n%4 for n in range(9))
    observed=tuple(n%2 for n in true_states)
    return {"true_period":4,"reported_period":2,"hidden_states":true_states,
            "reported_states":observed,"observer_faithful":False}


def equal_first_shell_distinct_ring_witness(p):
    """Z/p² versus F_p[t]/(t²): same residue cardinality, different characteristic.

    Both rings have p² elements and reduce to Fp, hence the SAME first-shell
    P^1(Fp) fingerprint. The independently measured p-fold unit sum at depth
    two and the image rank of multiplication-by-p separate them exactly.
    """
    _p(p)
    return {
        "residue_field_order":p,
        "first_shell_degree":p+1,
        "second_level_cardinality_each":p*p,
        "integer_ring_char":p*p,
        "equal_characteristic_ring_char":p,
        "integer_ring_p_times_one":p,
        "equal_characteristic_ring_p_times_one":0,
        "integer_ring_mul_p_image_count":p,
        "equal_characteristic_ring_mul_p_image_count":1,
        "first_shell_cannot_distinguish":True,
        "second_level_source_probe_distinguishes":True,
    }
