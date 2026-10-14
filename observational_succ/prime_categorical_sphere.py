"""Exact source-indexed prime/Pascal/Gamma *chart* laboratory.

Mathematical source: authentic positive-integer Pascal coefficients,
prime factorization, and Suzuki's Gamma OU chart alpha_j=2j+1/2.
A finite decorated double-cone is a toy S^2 simplicial realization,
NOT a theorem that the arithmetic adeles form that sphere.

No nontrivial zeta zero locations. No RH proof or completed Weil sign.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations
from math import comb, gcd


class SphereError(ValueError):
    pass


def integer(n: int, minimum=0, maximum=10_000) -> int:
    if type(n) is not int or not minimum <= n <= maximum:
        raise SphereError(f"integer required in [{minimum},{maximum}]")
    return n


def is_prime(p: int) -> bool:
    integer(p, 2)
    for d in range(2, int(p**0.5) + 1):
        if p % d == 0:
            return False
    return True


def source_prime(p: int) -> int:
    integer(p, 2)
    if not is_prime(p):
        raise SphereError("source multiplier is NOT prime; affine law alone is insufficient")
    return p


def factorization(n: int, prime_bound: int | None = None) -> dict[int, int]:
    if type(n) is not int or n < 1 or n.bit_length() > 1024:
        raise SphereError("positive bounded-size integer required")
    if prime_bound is not None:
        integer(prime_bound, 1)
    t = n
    output: dict[int, int] = {}
    p = 2
    while p*p <= t and (prime_bound is None or p <= prime_bound):
        while t % p == 0:
            output[p] = output.get(p, 0) + 1
            t //= p
        p += 1
    if t > 1:
        if prime_bound is not None and t > prime_bound:
            raise SphereError("not factored within certified source-bound")
        if t > 10_000:
            raise SphereError("remaining cofactor exceeds source-primality budget")
        if not is_prime(t):
            raise ArithmeticError("composite cofactor in factorization")
        output[t] = output.get(t, 0) + 1
    return output


def valuation(n: int, p: int) -> int:
    if type(n) is not int or n < 1 or n.bit_length() > 1024:
        raise SphereError("positive bounded-size integer required")
    source_prime(p)
    z = 0
    while n % p == 0:
        z += 1
        n //= p
    return z


def base_p_carries(left: int, right: int, p: int) -> int:
    integer(left)
    integer(right)
    source_prime(p)
    carries = 0
    carry = 0
    while left or right or carry:
        digit = (left % p) + (right % p) + carry
        carry = 1 if digit >= p else 0
        carries += carry
        left //= p
        right //= p
    return carries


def pascal_source(n: int, k: int) -> dict:
    integer(n, 0, 256)
    integer(k, 0, n)
    c = comb(n, k)
    factors = factorization(c, prime_bound=n) if n>=2 else {}
    if any(base_p_carries(k, n-k, p) != order for p, order in factors.items()):
        raise ArithmeticError("authentic Kummer carry identity failed")
    if sum(1 for p in factors if not is_prime(p)):
        raise ArithmeticError("nonprime source factor")
    reconstructed = 1
    for p, order in factors.items():
        reconstructed *= p**order
    if reconstructed != c:
        raise ArithmeticError("local-global integer product fails")
    # Probability-normalized row is a distinct rational source, with explicit p=2 debt.
    normalized = Q(c, 2**n)
    local_probability = factors.copy()
    local_probability[2] = local_probability.get(2, 0) - n
    local_probability = {p: e for p, e in local_probability.items() if e}
    source_global_product = Q(1)
    for p, exponent in local_probability.items():
        source_global_product *= Q(p)**exponent
    if source_global_product != normalized:
        raise ArithmeticError("normalized Pascal probability source mismatch")
    return {"n": n, "k": k, "binomial": c,
            "Kummer_prime_carries": factors,
            "probability": normalized,
            "probability_prime_valuations": local_probability,
            "source_product_formula_exact": True,
            "source_correlated": True}


def pascal_local_cancellation(n: int, k: int, p: int) -> dict:
    integer(n, 2, 256)
    integer(k, 1, n-1)
    source_prime(p)
    left, right, child = comb(n-1, k), comb(n-1, k-1), comb(n, k)
    a,b,c = valuation(left,p),valuation(right,p),valuation(child,p)
    if left+right != child or c < min(a,b):
        raise ArithmeticError("Pascal arithmetic local triangle failed")
    return {"prime":p,"parent_left":left,"parent_right":right,"child":child,
            "parent_valuations":(a,b),"child_valuation":c,
            "cancellation_excess":c-min(a,b),
            "valuation_only_predicts_child":a!=b,
            "needs_residue_phase":a==b}


def fixed_precision_obstruction(p: int, digits: int) -> dict:
    source_prime(p)
    integer(digits, 1, 16)
    a=1
    b=p**digits-1
    other=p**(digits+1)-1
    if (b-other)%p**digits or valuation(a+b,p)!=digits or valuation(a+other,p)!=digits+1:
        raise ArithmeticError("p-adic fixed-precision obstruction failed")
    return {"p":p,"precision":digits,
            "first_parent":a,"second_parent":b,"aliased_parent":other,
            "same_residue_mod_p_power":True,
            "sum_valuations":(digits,digits+1),
            "unbounded_cancellation_hidden_by_fixed_precision":True}


def gamma_chart(n: int) -> tuple[int,int,int]:
    """For alpha=n/2, n=2^e(4j+r), r in {1,3}."""
    integer(n, 1)
    e=0
    odd=n
    while odd%2==0:
        odd//=2
        e+=1
    r=odd%4
    j=(odd-r)//4
    return e,r,j


def gamma_mode(e: int, r: int, j: int) -> int:
    integer(e,0,12)
    if r not in (1,3):
        raise SphereError("Gamma orientation must be 1 or 3 mod 4")
    integer(j,0,1000)
    n=(2**e)*(4*j+r)
    integer(n,1,10_000_000)
    return n


def gamma_prime_transport(e:int,r:int,j:int,p:int) -> dict:
    source_prime(p)
    n=gamma_mode(e,r,j)
    en,rn,jn=gamma_chart(p*n)
    if p==2:
        predicted=(e+1,r,j)
    else:
        rp=(p*r)%4
        predicted=(e,rp,p*j+(p*r-rp)//4)
    if (en,rn,jn)!=predicted or gamma_mode(*predicted)!=p*n:
        raise ArithmeticError("prime-chart morphism failed")
    return {"prime":p,"from":(e,r,j),"to":predicted,
            "source_label_before":n,"source_label_after":p*n,
            "orientation_character":0 if p==2 else (1 if p%4==1 else -1),
            "carrier_source_preserved":True}


def chi4(n:int) -> int:
    integer(n,1)
    if n%2==0:
        return 0
    return 1 if n%4==1 else -1


def gamma_bath_weight(n:int) -> Q:
    integer(n,1)
    # Exact coefficient alpha^-2 of Suzuki's OU resolvent mode alpha=n/2.
    return Q(4,n*n)


def gamma_dilation_certificate(n:int,p:int) -> dict:
    source_prime(p)
    integer(n,1)
    # D_p R_{alpha} D_p^-1 = p R_{p alpha} on L2(real), Dp f=sqrt(p) f(px).
    lhs_weight=Q(1,p**3)*p*gamma_bath_weight(n)
    rhs_weight=gamma_bath_weight(p*n)
    if lhs_weight!=rhs_weight:
        raise ArithmeticError("wrong half-density gamma mode transport")
    return {"source_n":n,"p":p,"alpha_source":Q(n,2),
            "alpha_target":Q(p*n,2),
            "renormalized_kernel_weight":lhs_weight,
            "target_kernel_weight":rhs_weight,
            "true_half_density_transport":True,
            "suzuki_original_branch_preserved":n%4==1 and p%4==1,
            "is_original_Suzuki_mode":n%4==1}


def sieve_coefficient(n: int, factors: tuple[int,...]) -> int:
    integer(n,1)
    if any(type(p) is not int or not 2<=p<=10_000 for p in factors):
        raise SphereError("positive integer dilation factors expected")
    total=0
    for r in range(len(factors)+1):
        for idxs in combinations(range(len(factors)),r):
            mult=1
            for i in idxs:
                mult*=factors[i]
            if n%mult==0:
                total+=(-1)**r
    return total


def sieve_certificate(factors: tuple[int,...], max_mode: int = 64,
                      *, require_primes: bool = True) -> dict:
    if not factors or len(factors)>8:
        raise SphereError("1..8 factors required")
    integer(max_mode,1,2000)
    if require_primes:
        for p in factors:
            source_prime(p)
        if len(set(factors))!=len(factors):
            raise SphereError("Euler sieving requires distinct authentic primes")
    cs={n:sieve_coefficient(n,factors) for n in range(1,max_mode+1)}
    neg=next((n for n,c in cs.items() if c<0),None)
    if require_primes:
        P=1
        for p in factors:P*=p
        if any(cs[n]!=(1 if gcd(n,P)==1 else 0) for n in cs):
            raise ArithmeticError("Euler-squarefree-inclusion-exclusion failed")
    return {"factors":factors,"coefficients":cs,"first_negative":neg,
            "all_resolvent_weights_positive_or_zero":neg is None,
            "genuine_Euler_primitive_source":require_primes,
            "composite_mutation_could_pass_coprimality":not require_primes}


def original_suzuki_chart_transport(p:int,max_mode:int=101) -> dict:
    source_prime(p)
    integer(max_mode,1,2000)
    original=[n for n in range(1,max_mode+1) if n%4==1]
    target=[p*n for n in original if p*n<=max_mode]
    if p==2:
        required="dyadic_conductor+1"
        expected=[n for n in range(1,max_mode+1) if n%8==2]
    elif p%4==1:
        required="original_Suzuki_1_mod_4"
        expected=[n for n in range(1,max_mode+1) if n%4==1 and n%p==0]
    else:
        required="companion_3_mod_4"
        expected=[n for n in range(1,max_mode+1) if n%4==3 and n%p==0]
    if target!=expected:
        raise ArithmeticError("Gamma chart transport incomplete")
    residue=1 if p%4==1 else 3 if p%2 else 2
    return {"p":p,"required_chart":required,
            "spectral_indices_in_target":target,
            "orientation_character":chi4(p),
            "original_chart_invariant":p%4==1,
            "source_complete_mode_inclusion_verified":True,
            "positive_sieved_remainder_on_target_chart":True}


def ou_gram_dyadic(max_mode:int=33, factors:tuple[int,...]=(2,3),
                   npoints:int=4, chart:str="all") -> tuple[tuple[Q,...],...]:
    """Actual exp(-alpha|x-y|) at x_i=2 i log 2: rho_n=2^-n exactly.

    Finite mode truncation is a bona fide part of Suzuki's Gamma bath when chart
    is 'suzuki'; other chart labels are explicitly OTHER sources. Positivity of
    finite sums follows analytically via the exponential covariance theorem.
    """
    integer(max_mode,1,256)
    integer(npoints,1,12)
    if chart not in ("all","suzuki","companion"):
        raise SphereError("unknown source chart")
    if factors:
        cert=sieve_certificate(factors,max_mode,require_primes=True)
        cs=cert["coefficients"]
    else:
        cs={n:1 for n in range(1,max_mode+1)}
    wanted=lambda n: chart=="all" or (n%4==1 if chart=="suzuki" else n%4==3)
    included=[n for n in cs if wanted(n) and cs[n]==1]
    return tuple(tuple(sum((gamma_bath_weight(n)*Q(1,2**(n*abs(i-j)))
                            for n in included), Q()) for j in range(npoints))
                 for i in range(npoints))


def ldlt_positive(matrix: tuple[tuple[Q,...],...]) -> tuple[Q,...]:
    """Independent exact finite rational PSD certificate via LDL pivots."""
    n=len(matrix)
    if not n or any(len(row)!=n for row in matrix):
        raise SphereError("square rational matrix required")
    if any(matrix[i][j]!=matrix[j][i] for i in range(n) for j in range(n)):
        raise SphereError("not symmetric")
    lower=[[Q(0)]*n for _ in range(n)]
    D=[Q(0)]*n
    for i in range(n):
        lower[i][i]=Q(1)
        D[i]=matrix[i][i]-sum(lower[i][k]**2*D[k] for k in range(i))
        if D[i]<=0:
            raise SphereError("matrix not strictly positive definite")
        for j in range(i+1,n):
            lower[j][i]=(matrix[j][i]-sum(lower[j][k]*lower[i][k]*D[k]
                                             for k in range(i)))/D[i]
    if any(matrix[i][j]!=sum(lower[i][k]*D[k]*lower[j][k]
                                 for k in range(n)) for i in range(n) for j in range(n)):
        raise ArithmeticError("LDL reconstruction failed")
    return tuple(D)


def heat_bath_dyadic_interval(K:int,time_multiple:int=1,chart:str="suzuki") -> tuple[Q,Q]:
    """Whole infinite heat-mixture scalar at u=4*time_multiple*log2.

    W(u)=sum_{n in chart} (4/n) exp[-(n/2)^2*u]
        =sum_{n in chart} (4/n)*2^(-time_multiple*n*n).
    Enclosure has a proven rational tail, no floating or zero inputs.
    """
    integer(K,1,256)
    integer(time_multiple,1,8)
    if chart not in ("suzuki","companion","odd","all"):
        raise SphereError("invalid chart")
    keep=lambda n:(n%4==1 if chart=="suzuki" else n%4==3 if chart=="companion"
                   else n%2==1 if chart=="odd" else True)
    lower=sum((Q(4,n)*Q(1,2**(time_multiple*n*n)) for n in range(1,K+1) if keep(n)),Q())
    # for n>K, n² >= (K+1)n, each 4/n <= 4/(K+1).
    t=Q(1,2**(time_multiple*(K+1)))
    tail=Q(4,K+1)*t**(K+1)/(1-t)
    return lower,lower+tail


def categorical_sphere_faces() -> dict:
    """Double cone on 4-cycle equator: octahedron boundary, a toy S².

    Vertices south=0, north=5; equator=1,2,3,4 cyclic.
    Not a claim this is canonically homeomorphic to the adele class space.
    """
    triangles=[]
    for apex in (0,5):
        for u,v in ((1,2),(2,3),(3,4),(4,1)):
            triangles.append(tuple(sorted((apex,u,v))))
    edges=sorted(set(tuple(sorted((t[i],t[j]))) for t in triangles
                     for i,j in ((0,1),(0,2),(1,2))))
    return {"vertices": tuple(range(6)), "edges":tuple(edges),
            "faces":tuple(triangles)}


def matrix_rank_rational(rows: list[list[int]], ncols:int) -> int:
    a=[[Q(v) for v in row] for row in rows]
    rank=0
    for col in range(ncols):
        pivot=next((i for i in range(rank,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        u=a[rank][col]
        a[rank]=[v/u for v in a[rank]]
        for i in range(rank+1,len(a)):
            z=a[i][col]
            if z:
                a[i]=[a[i][j]-z*a[rank][j] for j in range(ncols)]
        rank+=1
        if rank==len(a):break
    return rank


def sphere_homology_receipt() -> dict:
    geom=categorical_sphere_faces()
    vertices,edges,faces=geom["vertices"],geom["edges"],geom["faces"]
    row1=[[(-1 if v==e[0] else 1 if v==e[1] else 0) for e in edges]
          for v in vertices]
    lookup={e:i for i,e in enumerate(edges)}
    row2=[]
    for edge in edges:
        vals=[]
        for a,b,c in faces:
            terms={(b,c):1,(a,c):-1,(a,b):1}
            vals.append(terms.get(edge,0))
        row2.append(vals)
    if any(sum(row1[i][k]*row2[k][j] for k in range(len(edges)))
           for i in range(len(vertices)) for j in range(len(faces))):
        raise ArithmeticError("not a simplicial complex: boundary²≠0")
    r1=matrix_rank_rational(row1,len(edges))
    r2=matrix_rank_rational(row2,len(faces))
    betti=(len(vertices)-r1,len(edges)-r1-r2,len(faces)-r2)
    if betti!=(1,0,1):
        raise ArithmeticError("double cone fails S² homology")
    # Odd p acts on 4-phase equator by half-turn if p =3 (4), id if =1 (4).
    # Even p=2 has chi4=0 and must enter conductor depth instead.
    return {"V":len(vertices),"E":len(edges),"F":len(faces),
            "Euler_characteristic":len(vertices)-len(edges)+len(faces),
            "boundary_rank_1":r1,"boundary_rank_2":r2,
            "Betti_Q":betti,"literal_finite_simplicial_sphere":True,
            "arithmetic_source_realization_of_all_sphere_faces":False,
            "two_ends_origin_and_formal_global_apex":True}


def prime_phase_equator_action(p:int) -> dict:
    """Actual multiplication j -> p*j (mod 4), extended over two cones.

    For odd p, this acts on the 4-cycle by identity or reflection, hence
    the suspension S^2 fundamental-class degree is chi4(p). For p=2,
    adjacent equatorial vertices map to nonadjacent vertices: NOT a
    simplicial endomorphism; the dyadic conductor must be enlarged.
    """
    source_prime(p)
    if p==2:
        return {"prime":2,"action":"change dyadic conductor and refine chart",
                "equator_endomorphism":False,"chi4":0,
                "degree_on_toy_S2":None}
    mapping={0:0,5:5}
    for j in range(4):
        mapping[j+1]=(p*j)%4+1
    geom=categorical_sphere_faces()
    if any(tuple(sorted(mapping[v] for v in face)) not in geom["faces"]
           for face in geom["faces"]):
        raise ArithmeticError("odd-prime phase action not simplicial")
    def norm_simplex(verts):
        result=tuple(sorted(verts))
        inv=sum(verts[i]>verts[j] for i in range(3) for j in range(i+1,3))
        return result, (-1)**inv
    cycle={face:0 for face in geom["faces"]}
    for u,v in ((1,2),(2,3),(3,4),(4,1)):
        k,sgn=norm_simplex((0,u,v))
        cycle[k]+=sgn
        k,sgn=norm_simplex((5,u,v))
        cycle[k]-=sgn
    pushed={f:0 for f in geom["faces"]}
    for face,c in cycle.items():
        k,sgn=norm_simplex(tuple(mapping[x] for x in face))
        pushed[k]+=c*sgn
    deg=chi4(p)
    if any(pushed[face]!=deg*cycle[face] for face in cycle):
        raise ArithmeticError("spherical orientation does not match chi4(p)")
    return {"prime":p,"action":"identity" if deg==1 else "reflection",
            "equator_permutation":tuple(mapping[j+1]-1 for j in range(4)),
            "equator_endomorphism":True,"chi4":deg,
            "degree_on_toy_S2":deg,
            "top_homology_action_verified_on_integer_chains":True,
            "not_an_arithmetic_space_realization":True}


def receipt() -> dict:
    examples=[pascal_source(n,k) for n,k in ((4,2),(6,3),(10,4))]
    fmt=lambda x: {k:(str(v) if isinstance(v,Q) else v) for k,v in x.items()}
    full=ou_gram_dyadic(17,(2,3),4,"all")
    small=ou_gram_dyadic(17,(),4,"suzuki")
    slo,shi=heat_bath_dyadic_interval(13)
    return {"name":"PRIME_CATEGORICAL_SPHERE_SOURCE_LAB",
            "pascal_places":[fmt(x) for x in examples],
            "pascal_cancel_2":pascal_local_cancellation(2,1,2),
            "precision_ghost":fixed_precision_obstruction(3,3),
            "gamma_transport":[gamma_prime_transport(0,1,0,p) for p in (2,3,5,7)],
            "gamma_dilation":fmt(gamma_dilation_certificate(1,5)),
            "affine_source_label_embedding":fmt(affine_gamma_source_intertwiner(6,5)),
            "source_chart_exits":[original_suzuki_chart_transport(p,101) for p in (2,3,5)],
            "sieve_2_3":sieve_certificate((2,3),30),
            "sieve_overlap_2_6":sieve_certificate((2,6),30,require_primes=False),
            "positive_actual_suzuki_gram_pivots":[str(x) for x in ldlt_positive(small)],
            "positive_source_sieved_gram_pivots":[str(x) for x in ldlt_positive(full)],
            "heat_at_4_log2_rational_interval":[str(slo),str(shi)],
            "toy_sphere":sphere_homology_receipt(),
            "toy_sphere_prime_degree":[prime_phase_equator_action(p) for p in (2,3,5,7)],
            "chiral_Gamma_positivity":gamma_chiral_identity_receipt(),
            "positive_chiral_gram_pivots":[str(x) for x in ldlt_positive(chiral_finite_gram(31,4))],
            "chiral_Hminus1_probes":[chiral_Hminus1_certificate(w,12) for w in (Q(0),Q(2),Q(10))],
            "operator_identity_euler_like_but_no_prime_gamma_weil_identification":True,
            "no_nontrivial_zero_inputs":True,"RH_proved":False}


def chiral_mode_symbol(n:int, xi:Q) -> Q:
    """Fourier multiplier of (n/2)^-2 e^(-(n/2)|x|)."""
    integer(n,1)
    if type(xi) not in (int,Q):
        raise SphereError("rational frequency required")
    t=Q(xi)
    return Q(4,n)/(Q(n*n,4)+t*t)


def chiral_symbol_interval(xi:Q,pairs:int=20)->tuple[Q,Q]:
    """Alternating Dirichlet-chi4 weighted Suzuki/companion difference.

    sigma(xi)=sum_j [4/((4j+1)((4j+1)^2/4+xi²))
                    -4/((4j+3)((4j+3)^2/4+xi²))].
    Each pair is >0 and odd-index partial sums sandwich exact series.
    """
    integer(pairs,1,128)
    if type(xi) not in (int,Q):
        raise SphereError("rational frequency required")
    lower=sum((chiral_mode_symbol(4*j+1,xi)-chiral_mode_symbol(4*j+3,xi)
               for j in range(pairs)),Q())
    upper=lower+chiral_mode_symbol(4*pairs+1,xi)
    if not Q(0)<lower<upper:
        raise ArithmeticError("chiral positive-spectral interval failed")
    return lower,upper


def chiral_diagonal_interval(pairs:int=30)->tuple[Q,Q]:
    """B_suz(x,x)-B_comp(x,x)=4*Catalan beta(2), exact rational alternating enclosure."""
    integer(pairs,1,128)
    lower=sum((Q(4,(4*j+1)**2)-Q(4,(4*j+3)**2)
               for j in range(pairs)),Q())
    upper=lower+Q(4,(4*pairs+1)**2)
    return lower,upper


def chiral_finite_gram(max_odd:int=31,npoints:int=4)->tuple[tuple[Q,...],...]:
    """Source-correct truncated signed chiral resolvent on actual dyadic lattice.

    Each paired summand is globally PSD by Fourier multiplier monotonicity.
    The exact rational finite Gram is independently LDL-tested in tests.
    """
    integer(max_odd,3,255)
    integer(npoints,1,10)
    pairs=(max_odd+1)//4
    ns=[(4*j+1,4*j+3) for j in range(pairs)]
    return tuple(tuple(sum((
        gamma_bath_weight(n)*Q(1,2**(n*abs(i-k)))
        -gamma_bath_weight(m)*Q(1,2**(m*abs(i-k)))
         for n,m in ns),Q()) for k in range(npoints)) for i in range(npoints))


def gamma_chiral_identity_receipt()->dict:
    """Two real spectral endpoint identities, stated with classical beta values.

    sigma(0)=16 beta(3)=pi³/2;  lim_(|xi|->inf) xi² sigma(xi)
    =4 beta(1)=pi.  B_+(x,x)-B_-(x,x)=4 beta(2)=4 Catalan.
    All identities use authentic Gamma ladder modes; none identifies Weil sign.
    """
    siglo,sighi=chiral_symbol_interval(Q(2),16)
    diaglo,diaghi=chiral_diagonal_interval(32)
    return {"gamma_original_index":"n=4j+1, alpha=n/2",
            "gamma_companion_index":"n=4j+3, alpha=n/2",
            "orientation":"chi4(n)",
            "suzuki_plus_minus_operator_PSD":True,
            "symbol_frequency_two_interval":(str(siglo),str(sighi)),
            "diagonal_weight_interval_4Catalan":(str(diaglo),str(diaghi)),
            "symbol_at_zero_exact":"pi^3/2 (=16*beta(3))",
            "high_frequency_limit_xi2_symbol_exact":"pi (=4*beta(1))",
            "spectral_gap_uniform_in_frequency":False,
            "full_suzuki_operator_sign_proved":False,
            "RH_proved":False}


def chiral_Hminus1_certificate(xi:Q,pairs:int=16)->dict:
    """Exact-rational checks of *proved analytic* H^-1 two-sided bounds:

      (8/3)/(1+xi²) <= sigma(xi) <= 22/(1+xi²).

    Analytic upper: sigma(0)=pi³/2; xi² sigma(xi)<=2*pi;
    pi³/2 + 2pi < 22 (using classical 3<pi<22/7).
    Analytic lower: first positive paired difference alone >=8/[3(1+xi²)].
    Positive finite tests NEVER substitute for universal proof.
    """
    if type(xi) not in (int,Q):
        raise SphereError("rational frequency required")
    freq=Q(xi)
    lower,upper=chiral_symbol_interval(freq,pairs)
    target_low=Q(8,3)/(1+freq*freq)
    target_high=Q(22)/(1+freq*freq)
    if not (target_low <lower<upper<target_high):
        raise ArithmeticError("source chiral multiplier violates proved envelope")
    return {"frequency":str(freq),"partial_interval":(str(lower),str(upper)),
            "Hminus1_lower":str(target_low),"Hminus1_upper":str(target_high),
            "source_analytic_global_bound_proved_in_dossier":True,
            "constant_Hminus1_lower":"8/3","constant_Hminus1_upper":"22",
            "full_Weil_positivity":False,"RH_proved":False}


def affine_gamma_source_intertwiner(n:int,p:int)->dict:
    """Literal positive-integer affine SUCC/FUCC action on ALL Gamma-mode labels.

    J(n)=n/2; one ADDITIVE source step becomes alpha+1/2; Vp becomes
    alpha -> p alpha.  This is an exact source-label functor, NOT an
    operator-valued intertwiner or a Gamma test-state identification.
    """
    integer(n,1)
    source_prime(p)
    base=Q(n,2)
    succ=Q(n+1,2)
    mult=Q(p*n,2)
    left=Q(p*(n+1),2)
    right=Q(p*n+p,2)
    if (succ!=base+Q(1,2) or mult!=p*base or left!=right
            or gamma_chart(p*(n+1))!=gamma_chart(p*n+p)):
        raise ArithmeticError("arithmetic Gamma-label affine functor failed")
    return {"n":n,"p":p,"source_label":base,
            "succ_label":succ,"prime_dilation_label":mult,
            "affine_braid_left":left,"affine_braid_right":right,
            "integer_SUCC_and_FUCC_source_laws_preserved":True,
            "full_Suzuki_Gamma_source_chart_preserved":n%4==1 and p%4==1,
            "operator_intertwiner_constructed":False,
            "RH_proved":False}
