"""Exact finite quantum-graph / Haar / lattice gauge bridges for SUCC.

Finite-group edge subdivision is a Haar-L2 isometry; conditional expectation
is exactly internal-vertex gauge averaging. Physical loop additions differ from
pure gauge refinement. A finite Z2 plaquette supplies an exact graph-counted
Hamiltonian, a path-sum/matrix correspondence and a *finite* reflection Gram.

No continuum, compact simple gauge group, Osterwalder-Schrader field theory,
Yang-Mills mass gap, RH or pi normality is proved by this module.

For the SUCC sibling carrier and S3 group definitions see
``observational_succ.yang_mills_gauge_oracle`` (draft PR #614).
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import comb
from typing import Sequence


class QuantumGaugeError(ValueError):
    """Inexact input, malformed finite group, or an unproved transport claim."""


def _nat(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise QuantumGaugeError(f"expected exact integer >= {minimum}")
    return n


def _rat(v) -> Q:
    if type(v) not in (int, Q):
        raise QuantumGaugeError("rational certificate requires int/Fraction, not bool/float")
    return Q(v)


def _vec(v: Sequence, count: int) -> tuple[Q, ...]:
    if not isinstance(v, (tuple, list)) or len(v) != count:
        raise QuantumGaugeError(f"expected exactly {count} rational components")
    return tuple(_rat(x) for x in v)


@dataclass(frozen=True)
class FiniteGaugeGroup:
    """A complete finite group table, with all group axioms checked."""
    name: str
    multiplication: tuple[tuple[int, ...], ...]
    unit: int

    def __post_init__(self):
        n = len(self.multiplication)
        if (type(self.name) is not str or not self.name or not 2 <= n <= 8
                or type(self.multiplication) is not tuple or
                any(type(row) is not tuple or len(row) != n for row in self.multiplication)
                or type(self.unit) is not int or not 0 <= self.unit < n
                or any(type(x) is not int or not 0 <= x < n
                       for row in self.multiplication for x in row)):
            raise QuantumGaugeError("finite Cayley table of order 2..8 required")
        for a in range(n):
            if self.mul(a, self.unit) != a or self.mul(self.unit, a) != a:
                raise QuantumGaugeError("malformed identity")
            if not any(self.mul(a, b) == self.unit and self.mul(b, a) == self.unit
                       for b in range(n)):
                raise QuantumGaugeError("missing inverse")
            for b in range(n):
                for c in range(n):
                    if self.mul(self.mul(a, b), c) != self.mul(a, self.mul(b, c)):
                        raise QuantumGaugeError("nonassociative table")

    @property
    def order(self) -> int:
        return len(self.multiplication)

    def mul(self, a: int, b: int) -> int:
        return self.multiplication[a][b]

    def inv(self, a: int) -> int:
        return next(b for b in range(self.order) if
                    self.mul(a, b) == self.unit and self.mul(b, a) == self.unit)

    def conj(self, k: int, a: int) -> int:
        return self.mul(self.mul(k, a), self.inv(k))


def cyclic_group(q: int) -> FiniteGaugeGroup:
    _nat(q, 2)
    if q > 8:
        raise QuantumGaugeError("bounded group order <=8 for exact finite probe")
    return FiniteGaugeGroup(f"Z/{q}", tuple(tuple((a+b) % q
                                                   for b in range(q)) for a in range(q)), 0)


def s3_group() -> FiniteGaugeGroup:
    """Use the *previous SUCC Yang-Mills module*, not a guessed S3 table."""
    from .yang_mills_gauge_oracle import S3_ELEMENTS, S3_ID, compose_s3
    g = tuple(S3_ELEMENTS)
    idx = {a: i for i, a in enumerate(g)}
    return FiniteGaugeGroup("SUCC-S3", tuple(tuple(idx[compose_s3(a, b)]
                                            for b in g) for a in g), idx[S3_ID])


@dataclass(frozen=True)
class HaarSubdivision:
    """Coarse G edge and fine GxG two-edge graph with normalized Haar.

    Jf(a,b) = f(ab). J*F(g) = avg_a F(a,a^-1*g).
    P=JJ*=internal-vertex gauge average; D=I-P is a pure-gauge
    *representation detail* (not a physical excitation) on this subdivision.
    Endpoint gauge frames are fixed: internal singlets are not the same as
    fully gauging both original endpoint vertices.
    Finite real rationals; complex linear extension is algebraic.
    """
    group: FiniteGaugeGroup

    @property
    def m(self):
        return self.group.order

    def pullback(self, coarse: Sequence) -> tuple[Q, ...]:
        f = _vec(coarse, self.m)
        return tuple(f[self.group.mul(a,b)] for a in range(self.m)
                     for b in range(self.m))

    def adjoint(self, fine: Sequence) -> tuple[Q, ...]:
        F = _vec(fine, self.m**2)
        return tuple(sum((F[a*self.m+self.group.mul(self.group.inv(a),g)]
                          for a in range(self.m)), Q()) / self.m
                     for g in range(self.m))

    def gauge_action(self, fine: Sequence, k: int) -> tuple[Q, ...]:
        F = _vec(fine, self.m**2)
        if type(k) is not int or not 0 <= k < self.m:
            raise QuantumGaugeError("invalid declared internal-vertex gauge element")
        return tuple(F[self.group.mul(a,self.group.inv(k))*self.m
                       +self.group.mul(k,b)]
                     for a in range(self.m) for b in range(self.m))

    def average(self, fine: Sequence) -> tuple[Q, ...]:
        F = _vec(fine, self.m**2)
        return tuple(sum((self.gauge_action(F,k)[i] for k in range(self.m)), Q())/self.m
                     for i in range(self.m**2))

    def project(self, fine: Sequence) -> tuple[Q, ...]:
        return self.pullback(self.adjoint(fine))

    def detail(self, fine: Sequence) -> tuple[Q, ...]:
        F = _vec(fine, self.m**2)
        p = self.project(F)
        return tuple(x-y for x,y in zip(F,p))

    @staticmethod
    def inner(a: Sequence, b: Sequence) -> Q:
        if not isinstance(a,(tuple,list)) or not isinstance(b,(tuple,list)) or len(a)!=len(b) or not a:
            raise QuantumGaugeError("vectors require same nonzero dimension")
        return sum((x*y for x,y in zip(_vec(a,len(a)),_vec(b,len(b)))),Q())/len(a)

    def exact_receipt(self, f: Sequence, F: Sequence) -> dict:
        f,F = _vec(f,self.m),_vec(F,self.m**2)
        Jf,EF,PF,DF = self.pullback(f),self.adjoint(F),self.project(F),self.detail(F)
        assert self.inner(f,f)==self.inner(Jf,Jf)
        assert self.inner(Jf,F)==self.inner(f,EF)
        assert self.adjoint(Jf)==f
        assert self.average(F)==PF
        assert self.project(PF)==PF
        assert self.inner(F,F)==self.inner(PF,PF)+self.inner(DF,DF)
        assert self.inner(PF,DF)==0
        assert self.adjoint(DF)==tuple(Q() for _ in range(self.m))
        return {"group":self.group.name,"group_order":self.m,
                "coarse_dimension":self.m,"fine_dimension":self.m**2,
                "internal_gauge_invariant_dimension":self.m,
                "pure_gauge_detail_dimension":self.m**2-self.m,
                "physical_norm":str(self.inner(PF,PF)),
                "gauge_detail_norm":str(self.inner(DF,DF)),
                "haar_isometry":True,"gauge_average_equals_orthogonal_projection":True}


def gauge_invariant_density_not_physical() -> dict:
    """A *density twirl* is not the Gauss-law singlet projector.

    For Z2 subdivision an odd state changes sign under internal k=1;
    its density |odd><odd| is unchanged by conjugation. Yet P|odd>=0.
    This is a hostile exact quantum-record semantics control.
    """
    h = HaarSubdivision(cyclic_group(2))
    odd = tuple(Q(1 if a==0 else -1,2) for a in range(2) for _ in range(2))
    assert sum(v*v for v in odd)==1
    assert tuple(-v for v in odd)==h.gauge_action(odd,1)
    rho = tuple(tuple(odd[i]*odd[j] for j in range(4)) for i in range(4))
    transformed = h.gauge_action(odd,1)
    twisted = tuple(tuple(transformed[i]*transformed[j] for j in range(4)) for i in range(4))
    proj = h.project(odd)
    assert rho==twisted and all(x==0 for x in proj)
    # Projection is self-adjoint for both normalized and counting inner products.
    return {"density_trace":str(sum(rho[i][i] for i in range(4))),
            "twirled_density_unchanged":True,"gauge_odd_vector_physical_norm":str(sum(x*x for x in proj)),
            "density_twirl_does_not_enforce_gauss_law":True}


def new_cycle_haar_detail(q: int=2) -> dict:
    """Adding an INDEPENDENT Wilson cycle gives a physical, not gauge, detail.

    After tree gauge fixing, coarse quotient G, fine quotient GxG.
    Jf(x,y)=f(x), E averages y. A nonzero y-dependent mean-zero
    detail survives the physical gauge quotient. Uses Z/2 for signs.
    """
    if q != 2:
        raise QuantumGaugeError("explicit signed-cycle witness uses Z/2")
    f = (Q(2),Q(-1))
    Jf = (f[0],f[0],f[1],f[1])
    d = (Q(1),Q(-1),Q(1),Q(-1))
    full = tuple(x+y for x,y in zip(Jf,d))
    E = tuple((full[2*x]+full[2*x+1])/2 for x in range(2))
    assert E==f
    assert HaarSubdivision.inner(d,d)==1
    assert HaarSubdivision.inner(Jf,d)==0
    assert HaarSubdivision.inner(full,full)==HaarSubdivision.inner(f,f)+1
    return {"coarse_gauge_quotient_dimension":2,"fine_gauge_quotient_dimension":4,
            "physical_new_detail_dimension":2,"exhibited_detail_norm": "1",
            "different_from_pure_subdivision":True}


def conditional_haar_energy(counts: Sequence, q: int, parents: int) -> dict[str,Q|int]:
    """Word-Haar/conditional L2 energy: SUCC successor junction at q=16.

    Counts indexed x*q+a, x in q^parents cylinder words.
    E_{k+1}-E_k = q^(k+1) sum (p(x,a)-p(x)/q)^2 >=0.
    """
    _nat(q,2);_nat(parents)
    if q>16 or parents>5:
        raise QuantumGaugeError("finite wavelet budget exceeded")
    n=(q**(parents+1))
    if not isinstance(counts,(tuple,list)) or len(counts)!=n or any(type(x) is not int or x<0 for x in counts):
        raise QuantumGaugeError("one nonnegative integer for every word cylinder")
    N=sum(counts)
    if N==0:
        raise QuantumGaugeError("nonempty empirical law required")
    p=tuple(Q(c,N) for c in counts)
    coar=tuple(sum(p[x*q+a] for a in range(q)) for x in range(q**parents))
    coarse=q**parents*sum((z*z for z in coar),Q())-1
    fine=q**(parents+1)*sum((z*z for z in p),Q())-1
    detail=q**(parents+1)*sum(((p[x*q+a]-coar[x]/q)**2
                                for x in range(q**parents) for a in range(q)),Q())
    assert detail>=0 and detail==fine-coarse
    return {"q":q,"parents":parents,"sample_count":N,"E_parent":coarse,
            "E_child":fine,"wavelet_detail_energy":detail}


def simultaneous_conjugacy_orbits(g: FiniteGaugeGroup, cycles: int=2) -> tuple[tuple[tuple[int,...], ...], ...]:
    """Gauge invariant graph-state classes: G^b modulo one shared conjugation.

    Works on loop *tuples*. Separate single-loop traces are not enough.
    """
    _nat(cycles,1)
    if cycles>3 or g.order**cycles>1000:
        raise QuantumGaugeError("declared finite graph quotient budget exceeded")
    remaining=set(product(range(g.order),repeat=cycles))
    orbits=[]
    while remaining:
        start=min(remaining)
        orb=tuple(sorted({tuple(g.conj(k,x) for x in start) for k in range(g.order)}))
        if not set(orb)<=remaining:
            raise ArithmeticError("overlap among purported disjoint gauge orbits")
        remaining-=set(orb)
        orbits.append(orb)
    return tuple(orbits)


def burnside_conjugation_orbits(g:FiniteGaugeGroup, cycles:int=2)->int:
    _nat(cycles,1)
    return sum(sum(g.mul(k,x)==g.mul(x,k) for x in range(g.order))**cycles
               for k in range(g.order))//g.order


def z2_plaquette_gauge_transform(state:int, vertex:int) -> int:
    """4-cycle vertices indexed v=0..3; star flips adjacent edges v-1 and v."""
    _nat(state);_nat(vertex)
    if state>=16 or vertex>=4:raise QuantumGaugeError("4-edge/4-vertex lattice only")
    return state ^ (1<<vertex) ^ (1<<((vertex-1)%4))


def z2_electric_magnetic_apply(psi:Sequence, lam:Q=Q(1)) -> tuple[Q,...]:
    """(H psi)(state) = sum_e (psi(state)-psi(state xor 2^e))
       + lam*(1-(-1)^Wilson_parity(state))*psi(state).
    This is the finite Z2 Kogut-Susskind-style gauge model, not continuum YM.
    """
    vals=_vec(psi,16)
    lam=_rat(lam)
    if lam<0:raise QuantumGaugeError("positive magnetic coupling")
    return tuple(sum((vals[x]-vals[x ^ (1<<e)] for e in range(4)),Q())
                 +lam*(2 if x.bit_count()%2 else 0)*vals[x] for x in range(16))


def z2_physical_matrix(lam:Q=Q(1)) -> tuple[tuple[Q,Q],tuple[Q,Q]]:
    """Derive the reduced quantum Hamiltonian by counting graph transitions.

    Gauge orbit basis |even>,|odd> is uniform on 8 states per parity.
    For each normalized class vector, amplitudes are 1/sqrt(8); this
    ratio cancels in matrix entries, leaving exact integer counts.
    """
    lam=_rat(lam)
    if lam<0:raise QuantumGaugeError("positive coupling required")
    classes=[tuple(x for x in range(16) if x.bit_count()%2==p) for p in (0,1)]
    if any(len(c)!=8 for c in classes):raise ArithmeticError("gauge quotient wrong size")
    basis=[tuple(Q(int(x in c)) for x in range(16)) for c in classes]
    images=[z2_electric_magnetic_apply(v,lam) for v in basis]
    matrix=tuple(tuple(sum((images[j][x] for x in classes[i]),Q())/8
                       for j in range(2)) for i in range(2))
    assert matrix==((Q(4),Q(-4)),(Q(-4),Q(4+2*lam)))
    # Every local gauge star acts identically on every physical basis vector.
    for v in range(4):
        for c in classes:
            if {z2_plaquette_gauge_transform(x,v) for x in c}!=set(c):
                raise ArithmeticError("gauge invariant state lost")
    return matrix


def physical_spectral_receipt(lam:Q=Q(1)) -> dict:
    lam=_rat(lam)
    M=z2_physical_matrix(lam)
    tr=M[0][0]+M[1][1]
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    discr=tr*tr-4*det
    assert discr==4*(lam*lam+16)
    if det < 0 or M[0][0]<0:
        raise ArithmeticError("finite electric+magnetic Hamiltonian not PSD")
    return {"physical_dimension":2,"matrix":[[str(z) for z in r] for r in M],
            "trace":str(tr),"determinant":str(det),
            "discriminant":str(discr),"formal_gap":"2*sqrt(lambda^2+16)",
            "lambda":"%s"%lam,"continuum_mass_gap_claimed":False}


def _mul(A: tuple[tuple[Q,...], ...],B: tuple[tuple[Q,...],...])->tuple[tuple[Q,...],...]:
    if not A or not B or len(A[0])!=len(B):raise QuantumGaugeError("matrix shape mismatch")
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),Q())
                       for j in range(len(B[0]))) for i in range(len(A)))


def _power(A:tuple[tuple[Q,...],...],n:int)->tuple[tuple[Q,...],...]:
    _nat(n)
    if n>20:raise QuantumGaugeError("finite reflection/power budget")
    d=len(A)
    if not d or any(len(r)!=d for r in A):raise QuantumGaugeError("square transfer matrix required")
    out=tuple(tuple(Q(int(i==j)) for j in range(d)) for i in range(d))
    for _ in range(n):out=_mul(out,A)
    return out


def path_sum(A: Sequence, bra: Sequence, ket: Sequence, steps:int) -> Q:
    """Direct computational path sum of *amplitudes*, equal to <bra,A^steps ket>.

    Graph paths retain signs. Counting trajectories as probabilities would
    be a FALSE quantum bridge; amplitudes may interfere destructively.
    """
    _nat(steps)
    if steps>7:raise QuantumGaugeError("bounded finite path expansion")
    d=len(A)
    if type(A) not in (tuple,list) or not 2<=d<=4 or any(len(row)!=d for row in A):
        raise QuantumGaugeError("small square matrix required")
    M=tuple(_vec(row,d) for row in A)
    v,w=_vec(bra,d),_vec(ket,d)
    total=Q()
    for path in product(range(d),repeat=steps+1):
        z=v[path[-1]]*w[path[0]]
        for j in range(steps):z*=M[path[j+1]][path[j]]
        total+=z
    matrix=_power(M,steps)
    check=sum((v[i]*matrix[i][j]*w[j] for i in range(d) for j in range(d)),Q())
    if total!=check:raise ArithmeticError("graph path expansion is not linear algebra")
    return total


def finite_reflection_gram(times:Sequence[int]=(0,1,2),
                           test_vectors:Sequence[Sequence]=((1,0),(0,1),(1,1))) -> dict:
    """Finite reflection-style Gram K^(ti+tj) for K=I-H/16, lambda=1.

    For symmetric positive K, <f_i,K^(ti+tj)f_j>
    =<K^ti f_i,K^tj f_j>; manifestly PSD.
    NOT full 4D OS positivity or reconstruction.
    """
    H=z2_physical_matrix(Q(1))
    K=tuple(tuple(Q(int(i==j))-H[i][j]/16 for j in range(2)) for i in range(2))
    assert K[0][1]==K[1][0]
    assert K[0][0]>0 and K[0][0]*K[1][1]-K[0][1]*K[1][0]>0
    if (not isinstance(times,(tuple,list)) or not times or len(times)>5 or
            len(times)!=len(test_vectors)):
        raise QuantumGaugeError("matched 1..5 times and test vectors")
    at=[]
    for t,v in zip(times,test_vectors):
        _nat(t)
        v=_vec(v,2)
        P=_power(K,t)
        at.append(tuple(sum((P[i][j]*v[j] for j in range(2)),Q()) for i in range(2)))
    gram=tuple(tuple(sum((at[i][h]*at[j][h] for h in range(2)),Q())
                     for j in range(len(at))) for i in range(len(at)))
    for i in range(len(at)):
        for j in range(len(at)):
            v,w=_vec(test_vectors[i],2),_vec(test_vectors[j],2)
            P=_power(K,times[i]+times[j])
            direct=sum((v[a]*P[a][b]*w[b] for a in range(2) for b in range(2)),Q())
            if direct!=gram[i][j]:raise ArithmeticError("reflected Hilbert Gram mismatch")
    # Gram PSD proved by square decomposition, not numerical eigensolver.
    return {"transfer_matrix":[[str(x) for x in row] for row in K],
            "gram":[[str(x) for x in row] for row in gram],
            "reflected_positive_by_factorization":True,
            "full_OS_QFT_claimed":False}


def toy_wilson_factor_graph(positive_weight:Q=Q(3), negative_weight:Q=Q(1)) -> dict:
    """A single Z2 plaquette: factor-graph sum = exact quotient Wilson sum.

    A positive Euclidean *toy* Wilson weight is assigned by closed-loop parity.
    Distinguish normalized Haar measure (uniform on all 16 configurations)
    from the *interacting* source-selected Gibbs law. Not SU(2) in 4D.
    """
    plus,minus=_rat(positive_weight),_rat(negative_weight)
    if plus<=0 or minus<=0:raise QuantumGaugeError("strictly positive source weights required")
    weights=tuple(plus if x.bit_count()%2==0 else minus for x in range(16))
    Z=sum(weights,Q())/16
    class_sum=tuple(sum((weights[x] for x in range(16) if x.bit_count()%2==p),Q())
                    for p in (0,1))
    assert class_sum==(8*plus,8*minus) and Z==(plus+minus)/2
    wilson=sum(((-1 if x.bit_count()%2 else 1)*weights[x] for x in range(16)),Q())/16/Z
    assert wilson==(plus-minus)/(plus+minus)
    for v in range(4):
        for x in range(16):
            assert weights[x]==weights[z2_plaquette_gauge_transform(x,v)]
    return {"Haar_normalized_partition":str(Z),
            "gauge_orbit_weights":(str(plus),str(minus)),
            "Gibbs_orbit_probabilities":(str(plus/(plus+minus)),str(minus/(plus+minus))),
            "wilson_loop_expectation":str(wilson),
            "gauge_invariant":True,"interacting_law_is_Haar":plus==minus}


def two_plaquette_source_transport(plus:Q=Q(3), minus:Q=Q(1)) -> dict:
    """Exact failure of naively transporting a Wilson source through refinement.

    Fine model has two independent Z2 loop signs with unchanged local weight
    ratio plus:minus. Coarse loop observable is their product. Haar measures
    push forward correctly, but *interacting Gibbs measures* do not generally
    preserve the same bare coupling. Example 3:1 has TV defect 1/8.
    This is an abstract finite factor-graph/RG countermodel, not a 4D YM RG.
    """
    plus,minus=_rat(plus),_rat(minus)
    if plus<=0 or minus<=0:raise QuantumGaugeError("positive Wilson weights required")
    Z=plus+minus
    p,q=plus/Z,minus/Z
    coarse=(p,q)
    fine_pushed=(p*p+q*q,2*p*q)
    variation=(abs(fine_pushed[0]-p)+abs(fine_pushed[1]-q))/2
    assert sum(fine_pushed,Q())==1
    return {"coarse_law":tuple(str(x) for x in coarse),
            "fine_product_pushforward":tuple(str(x) for x in fine_pushed),
            "source_transport_TV_defect":str(variation),
            "coarse_wilson_mean":str(p-q),
            "fine_pushed_wilson_mean":str((p-q)**2),
            "Haar_reference_commutes":plus==minus,
            "bare_action_reuse_is_exact":variation==0}


def subdivision_edge_mode_entanglement(g:FiniteGaugeGroup) -> dict:
    """Maximally entangled link-pair embedding of ONE physical link basis state.

    In the standard counting-orthonormal link bases, the gauge-invariant
    embedding of |g> is (1/sqrt(m))*sum_a |a>|a^-1 g>.
    Its link-factorized reduced density is I/m (purity 1/m), even though
    the *coarse* state is pure and carries one open-link label.
    Full endpoint Gauss constraints must be handled in a larger graph.
    This is kinematical edge-mode entanglement and depends on factorization;
    NOT interaction-induced particles, wormholes, or a mass-gap theorem.
    Density coefficients and purity are computed exactly without sqrt(m).
    """
    if not isinstance(g,FiniteGaugeGroup):raise QuantumGaugeError("declared finite group required")
    m=g.order
    q=g.unit
    # Coefficient matrix C_ab=1/sqrt(m) if a*b=q, else 0.
    # Return rho_A=C C^* by counting exact overlap and dividing by m.
    rho=tuple(tuple(Q(sum(g.mul(a,b)==q and g.mul(a2,b)==q
                             for b in range(m)),m)
                    for a2 in range(m)) for a in range(m))
    expected=tuple(tuple(Q(int(i==j),m) for j in range(m)) for i in range(m))
    assert rho==expected
    purity=sum((rho[i][j]*rho[j][i] for i in range(m) for j in range(m)),Q())
    assert purity==Q(1,m)
    return {"group":g.name,"refined_link_factor_reduced_purity":str(purity),
            "coarse_pure_state_purity":"1","Schmidt_rank":m,
            "formal_entropy":"log(%d)"%m,
            "entanglement_created_by_subdivision_in_extended_link_tensor_factorization":True,
            "physical_purity_not_lost":True}


def haar_poincare_transfer(a:Q, scale:str="linear") -> dict:
    """Exact two-state Haar-wavelet Rayleigh control of PHYSICAL-scale saving.

    T=[[1-eps,eps],[eps,1-eps]] is a symmetric stochastic contraction with
    constant vacuum 1 and unique centered Haar wavelet (1,-1).
    <w,(I-T)w>/<w,w> = 2 eps.
    For eps=a/4: this divided by physical spacing a is 1/2.
    For eps=a^2: divided by a is 2a -> 0, despite finite positivity.
    The actual source of a 4D Wilson transfer operator is NOT supplied.
    """
    a=_rat(a)
    if not 0<a<=Q(1,4) or scale not in ("linear","quadratic"):
        raise QuantumGaugeError("rational spacing 0<a<=1/4 and declared scaling required")
    eps=a/4 if scale=="linear" else a*a
    T=((1-eps,eps),(eps,1-eps))
    wavelet=(Q(1),Q(-1))
    tw=tuple(sum((T[i][j]*wavelet[j] for j in range(2)),Q()) for i in range(2))
    norm=HaarSubdivision.inner(wavelet,wavelet)
    energy=HaarSubdivision.inner(wavelet,tuple(wavelet[i]-tw[i] for i in range(2)))
    ratio=energy/norm
    assert ratio==2*eps
    assert tuple(sum(row,Q()) for row in T)==(1,1)
    assert 0<1-2*eps<1
    return {"spacing":str(a),"family":scale,
            "wavelet_Poincare_constant":str(ratio),
            "physical_scale_normalized_margin":str(ratio/a),
            "excited_transfer_eigenvalue":str(1-ratio),
            "actual_YM_source_bound":False}
