"""Finite-observer reconstruction and local Tate Fourier interface.

SOURCE / PROOF BOUNDARY
- Theorem (classical): Hom_Q-alg(colim Q^(Z/m), Q) ~= lim Z/m ~= Zhat,
  using ALL source-compatible quotient models, not a finite list.
- Every locally constant compactly supported Q_p test admits an exact
  finite chart p^-r Z_p / p^s Z_p. Chart Fourier and Parseval are exact
  cyclotomic identities with self-dual additive Haar vol(Z_p)=1.
- Archimedean R and the full adelic Poisson/Weil positivity do NOT follow
  from inverse limits of finite discrete quotients or from the code here.
- Source labels are mathematical declarations, NOT physical attestation.
- No zeta zero positions are inputs and RH is NOT proved.

See research/2026-10-15/OBSERVER_TATE_ATOMIC_RECONSTRUCTION.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, gcd

from .finite_fourier_carrier import CyclotomicElement, exact_dft
from .diagonal_adele_zeta import prime


class AtomicDescentError(ValueError):
    """Malformed source quotient, test chart or noncommuting observation square."""


def _integer(x, floor=0, ceiling=2048) -> int:
    if type(x) is not int or not floor <= x <= ceiling:
        raise AtomicDescentError("Exact bounded integer required")
    return x


def _rational(x) -> Q:
    if type(x) not in (int, Q):
        raise AtomicDescentError("Exact rational source value required")
    return Q(x)


@dataclass(frozen=True)
class StageCharacter:
    """Q-algebra hom Q^(Z/m) -> Q encoded on ALL atomic idempotents.

    Each atom e_j satisfies e_j^2=e_j, e_j e_k=0 if j!=k,
    and sum_j e_j=1. Therefore a UNITAL algebra hom into a field
    sends exactly one idempotent to 1 and all others to 0.
    This is the actual object->model->model-of-model reconstruction
    at each stage; it is NOT a physical event observation.
    """
    modulus: int
    atomic_evaluations: tuple[Q, ...]

    def __post_init__(self):
        _integer(self.modulus, 2, 256)
        if (type(self.atomic_evaluations) is not tuple
                or len(self.atomic_evaluations) != self.modulus):
            raise AtomicDescentError("Every atomic stage event must be represented")
        if any(type(x) not in (int, Q) or Q(x) not in (0, 1)
               for x in self.atomic_evaluations):
            raise AtomicDescentError("An algebra character preserves idempotents")
        if sum(self.atomic_evaluations, Q()) != 1:
            raise AtomicDescentError("A unital multiplicative model picks ONE source atom")

    @classmethod
    def evaluation(cls, modulus: int, residue: int) -> "StageCharacter":
        _integer(modulus, 2, 256)
        _integer(residue, 0, modulus-1)
        return cls(modulus, tuple(Q(int(i == residue)) for i in range(modulus)))

    @property
    def reconstructed_residue(self) -> int:
        return self.atomic_evaluations.index(1)

    def evaluate(self, values: tuple[int|Q, ...]) -> Q:
        if type(values) is not tuple or len(values) != self.modulus:
            raise AtomicDescentError("Unspecified or incomplete observer test algebra")
        return sum((Q(a)*_rational(v)
                    for a, v in zip(self.atomic_evaluations, values)), Q())

    def project_to(self, coarse_modulus: int) -> "StageCharacter":
        _integer(coarse_modulus, 2, self.modulus)
        if self.modulus % coarse_modulus:
            raise AtomicDescentError("Not a lawful source quotient")
        values = tuple(
            sum((self.atomic_evaluations[j] for j in range(self.modulus)
                 if j % coarse_modulus == a), Q())
            for a in range(coarse_modulus)
        )
        return StageCharacter(coarse_modulus, values)


@dataclass(frozen=True)
class ObserverLimitReceipt:
    moduli: tuple[int,...]
    residues: tuple[int,...]
    stage_algebra_chars: int
    compatible_idempotent_tests: int
    source_tag: str
    exact_finite_snapshot: bool = True
    entire_infinite_inverse_limit_constructed_by_finite_code: bool = False
    actual_integer_source_authenticated: bool = False
    archimedean_completed: bool = False
    RH_proved: bool = False


def reconstruct_from_model_models(
        stages: tuple[StageCharacter,...],
        source_tag: str = "DECLARED_ARITHMETIC_QUOTIENTS") -> ObserverLimitReceipt:
    """Verify ALL finite pullback squares, reconstruct unique stage points.

    The infinite theorem ranges over a COFINAL directed family of moduli.
    A finite prefix receipt cannot certify the entire inverse limit, nor
    distinguish integer source identity from a nonintegral profinite point.
    """
    if (type(stages) is not tuple or not 1 <= len(stages) <= 12
            or any(not isinstance(s, StageCharacter) for s in stages)
            or type(source_tag) is not str or not source_tag):
        raise AtomicDescentError("Declared nonempty typed recursive stage tower required")
    count = 0
    for i in range(1, len(stages)):
        low, high = stages[i-1], stages[i]
        if high.modulus <= low.modulus or high.modulus % low.modulus:
            raise AtomicDescentError("Non-increasing or nondivisible observer growth")
        try:
            lowered = high.project_to(low.modulus)
        except AtomicDescentError:
            raise
        if lowered != low:
            raise AtomicDescentError("Model-of-model naturality/source square failed")
        count += low.modulus
    return ObserverLimitReceipt(
        tuple(z.modulus for z in stages),
        tuple(z.reconstructed_residue for z in stages),
        len(stages), count, source_tag
    )


def factorial_observer_moduli(level: int) -> tuple[int,...]:
    """Cofinal moduli n!, n>=2, finite check length=1..4 (2,6,24,120)."""
    _integer(level, 1, 4)
    return tuple(factorial(n) for n in range(2, level+2))


def ghost_profinite_residue(modulus: int) -> int:
    """Coherent profinite point: 2-primary coordinate 1, every odd p=0.

    x mod 2^v2(modulus)=1; x mod odd-part(modulus)=0.
    By CRT this makes a coherent family for EVERY even modulus. It is
    NOT the image of an integer: an integer with zero in every 3^k
    quotient must be 0, contradicting its odd 2-adic coordinate 1.
    Each finite prefix is compatible with some integer representative.
    """
    _integer(modulus, 2, 4096)
    if modulus % 2:
        raise AtomicDescentError("The declared ghost control includes a 2-primary probe")
    q = modulus
    twos = 1
    while q % 2 == 0:
        twos *= 2
        q //= 2
    return (q * pow(q, -1, twos)) % modulus


def profinite_ghost_prefix(level: int) -> ObserverLimitReceipt:
    mods = factorial_observer_moduli(level)
    stages = tuple(StageCharacter.evaluation(m,ghost_profinite_residue(m))
                   for m in mods)
    return reconstruct_from_model_models(stages,source_tag="CRT_COHERENT_NONINTEGER_PROFINITE_POINT")


def integer_source_prefix(integer: int, level: int) -> ObserverLimitReceipt:
    if type(integer) is not int:
        raise AtomicDescentError("A declared integer source must be an integer")
    mods = factorial_observer_moduli(level)
    return reconstruct_from_model_models(tuple(
        StageCharacter.evaluation(m,integer % m) for m in mods),
        source_tag="DECLARED_INTEGER_EMBEDDED_IN_PROFINITE")


def embed_cyclotomic(z: CyclotomicElement, large_modulus: int) -> CyclotomicElement:
    """Canonical Q(zeta_m) -> Q(zeta_N), zeta_m := zeta_N^(N/m)."""
    _integer(large_modulus, 2, 100)
    if (not isinstance(z,CyclotomicElement)
            or large_modulus % z.modulus):
        raise AtomicDescentError("Fourier character phases lack common source clock")
    ratio = large_modulus//z.modulus
    accum = CyclotomicElement.scalar(large_modulus, 0)
    for i,c in enumerate(z.polynomial):
        if c:
            accum=accum+CyclotomicElement.root(large_modulus,i*ratio).scale(c)
    return accum


def normal_fourier_naturality(coarse: tuple[int|Q,...],
                             finer_modulus: int) -> dict:
    """Fourier commutes with lawful observation refinement.

    For m|N, lifted f_N(x)=f_m(x mod m), normalized Fourier yields
      F_N(f_N)(k)=0 unless k multiple N/m;
      F_N(f_N)((N/m)ell) = embed(F_m(f_m)(ell)).
    Actual outputs are in exact Q(zeta_N); no float phase comparisons.
    A composite observation modulus is permitted: it is not an Euler prime.
    """
    if type(coarse) is not tuple:
        raise AtomicDescentError("Finite original source values must be a tuple")
    m=len(coarse)
    _integer(m,2,48)
    _integer(finer_modulus, m+1, 72)
    if finer_modulus % m:
        raise AtomicDescentError("Observers not related by genuine residue reduction")
    xs=tuple(_rational(z) for z in coarse)
    q=finer_modulus//m
    large=tuple(xs[i % m] for i in range(finer_modulus))
    old=tuple(x.scale(Q(1,m)) for x in exact_dft(xs))
    new=tuple(x.scale(Q(1,finer_modulus)) for x in exact_dft(large))
    for k,value in enumerate(new):
        expect = (embed_cyclotomic(old[k//q],finer_modulus)
                  if k%q==0 else CyclotomicElement.scalar(finer_modulus,0))
        if value!=expect:
            raise ArithmeticError("Finite Fourier/Haar pullback naturality failed")
    return {"old_modulus":m,"new_modulus":finer_modulus,
            "old_reduction":tuple(i%m for i in range(finer_modulus)),
            "dual_frequency_factor":q,
            "all_frequencies_checked":finer_modulus,
            "natural_Fourier_square":True,
            "equal_self_dual_Haar_ratios":True,
            "composite_residue_modulus_allowed":True,
            "composite_Euler_place_claimed":False,
            "Archimedean_place_identified":False,
            "RH_proved":False}


@dataclass(frozen=True)
class PadicBruhatChart:
    """Chart for Q_p: p^-r Z_p / p^s Z_p, with r,s>=0 and r+s>0.

    Support x=p^-r a, a mod p^(r+s), and constant on p^sZ_p.
    Haar vol(Z_p)=1 => vol(p^sZ_p)=p^-s. Additive dual chart
    is p^-sZ_p / p^rZ_p; Fourier is self-dual with this normalization.
    """
    p: int
    support_depth: int
    precision_depth: int

    def __post_init__(self):
        if (type(self.p) is not int or not prime(self.p)
                or type(self.support_depth) is not int
                or type(self.precision_depth) is not int
                or not 0<=self.support_depth<=5
                or not 0<=self.precision_depth<=5
                or self.support_depth+self.precision_depth<1):
            raise AtomicDescentError("Declare actual local p and bounded two-sided chart")
        if self.p**(self.support_depth+self.precision_depth)>32:
            raise AtomicDescentError("Exact cyclotomic chart budget N<=32")

    @property
    def modulus(self) -> int:
        return self.p**(self.support_depth+self.precision_depth)

    @property
    def cell_Haar_volume(self) -> Q:
        return Q(1,self.p**self.precision_depth)

    @property
    def dual(self) -> "PadicBruhatChart":
        return PadicBruhatChart(self.p,self.precision_depth,self.support_depth)

    def values(self, raw: tuple[int|Q,...]) -> tuple[Q,...]:
        if type(raw) is not tuple or len(raw)!=self.modulus:
            raise AtomicDescentError("All locally constant p-adic source cells required")
        return tuple(_rational(z) for z in raw)


def local_tate_fourier(chart: PadicBruhatChart,
                       values: tuple[int|Q,...]) -> tuple[CyclotomicElement,...]:
    """Haar-correct finite Tate Fourier on actual p-adic Schwartz chart.

    Fourier fhat(y_b)=p^-s sum_(a mod p^(r+s)) f_a exp(2pi i ab/N),
    y_b=p^-s b; dual chart has support depth s and precision depth r.
    """
    if not isinstance(chart,PadicBruhatChart):
        raise AtomicDescentError("Genuine p-adic chart is mandatory")
    raw=chart.values(values)
    return tuple(v.scale(chart.cell_Haar_volume) for v in exact_dft(raw))


def _complex_forward(chart: PadicBruhatChart,
                     z: tuple[CyclotomicElement,...]) -> tuple[CyclotomicElement,...]:
    if len(z)!=chart.modulus or any(v.modulus!=chart.modulus for v in z):
        raise AtomicDescentError("Frequency source phases not in one p-adic chart")
    n=chart.modulus
    ans=[]
    for k in range(n):
        t=CyclotomicElement.scalar(n,0)
        for a,val in enumerate(z):
            if val.polynomial!=(Q(0),):
                t=t+val*CyclotomicElement.root(n,a*k)
        ans.append(t.scale(chart.cell_Haar_volume))
    return tuple(ans)


def _conjugate(z: CyclotomicElement) -> CyclotomicElement:
    n=z.modulus
    total=CyclotomicElement.scalar(n,0)
    for i,v in enumerate(z.polynomial):
        if v:
            total=total+CyclotomicElement.root(n,-i).scale(v)
    return total


def tate_local_inversion_and_parseval(chart: PadicBruhatChart,
                                      values: tuple[int|Q,...]) -> dict:
    """Exact double Fourier f(-x) and L2 Plancherel, cyclotomic arithmetic.

    Fully finite chart algebra, theorem extends to all Bruhat-Schwartz
    functions since every such Q_p test belongs to some p^-r/p^s chart.
    No zero data, adelic Poisson theorem or global Euler product.
    """
    source=chart.values(values)
    fhat=local_tate_fourier(chart,source)
    twice=_complex_forward(chart.dual,fhat)
    n=chart.modulus
    expected=tuple(CyclotomicElement.scalar(n,source[(-k)%n]) for k in range(n))
    if twice!=expected:
        raise ArithmeticError("Tate finite local Fourier involution failed")
    original_energy=sum((z*z for z in source), Q())*chart.cell_Haar_volume
    output_energy=CyclotomicElement.scalar(n,0)
    for z in fhat:
        output_energy=output_energy+z*_conjugate(z)
    output_energy=output_energy.scale(chart.dual.cell_Haar_volume)
    if output_energy!=CyclotomicElement.scalar(n,original_energy):
        raise ArithmeticError("Tate local Haar Plancherel failed")
    return {"prime":chart.p,"support_depth":chart.support_depth,
            "precision_depth":chart.precision_depth,"modulus":n,
            "additive_cell_Haar_volume":str(chart.cell_Haar_volume),
            "dual_cell_Haar_volume":str(chart.dual.cell_Haar_volume),
            "Fourier_involution_reflection":True,
            "Plancherel_on_original_local_source":True,
            "local_test_space":"p^-r Z_p / p^s Z_p",
            "full_padic_Schwartz_Bruhat_via_inductive_charts":"CLASSICAL_THEOREM_NOT_COMPUTED_IN_FULL",
            "adelic_global_Poisson_imported":False,
            "RH_proved":False}


def refine_local_precision(chart: PadicBruhatChart,
                           raw: tuple[int|Q,...]) -> dict:
    """Test p^s -> p^(s+1) constancy refinement and dual support projection."""
    old=chart.values(raw)
    new_chart=PadicBruhatChart(chart.p,chart.support_depth,chart.precision_depth+1)
    newer=tuple(old[i%chart.modulus] for i in range(new_chart.modulus))
    new_fourier=local_tate_fourier(new_chart,newer)
    old_fourier=local_tate_fourier(chart,old)
    factor=chart.p
    for k,v in enumerate(new_fourier):
        expected = (embed_cyclotomic(old_fourier[k//factor],new_chart.modulus)
                    if k%factor==0 else
                    CyclotomicElement.scalar(new_chart.modulus,0))
        if v!=expected:
            raise ArithmeticError("Local Tate Fourier precision/refinement square failed")
    return {"old_chart":(chart.p,chart.support_depth,chart.precision_depth),
            "new_chart":(new_chart.p,new_chart.support_depth,new_chart.precision_depth),
            "source_cells_copied":True,
            "dual_frequency_support_included_exactly":True,
            "finite_Fourier_naturality":True,"RH_proved":False}


def refine_local_support(chart: PadicBruhatChart,
                         raw: tuple[int|Q,...]) -> dict:
    """Test p^-r support -> p^-(r+1) support enlargement, zero extend."""
    old=chart.values(raw)
    new_chart=PadicBruhatChart(chart.p,chart.support_depth+1,chart.precision_depth)
    n=chart.modulus
    f=[Q() for _ in range(new_chart.modulus)]
    for a,value in enumerate(old):
        f[chart.p*a]=value
    new_fourier=local_tate_fourier(new_chart,tuple(f))
    old_fourier=local_tate_fourier(chart,old)
    for k,v in enumerate(new_fourier):
        expected=embed_cyclotomic(old_fourier[k%n],new_chart.modulus)
        if v!=expected:
            raise ArithmeticError("Local Tate Fourier support/refinement square failed")
    return {"old_chart":(chart.p,chart.support_depth,chart.precision_depth),
            "new_chart":(new_chart.p,new_chart.support_depth,new_chart.precision_depth),
            "source_support_extended_by_zero":True,
            "dual_periodicity_exact":True,"finite_Fourier_naturality":True,
            "RH_proved":False}


def local_padic_real_boundary_no_go() -> dict:
    """Exact topological boundary, not a computational failure.

    Inverse limits of finite discrete sets are compact, totally
    disconnected. A connected noncompact real line cannot be such a
    space. To get Q_p require also inductive support enlargement,
    and for R require an independent analytic uniform/Cauchy topology.
    """
    return {"profinite_compact_and_totally_disconnected":True,
            "real_line_connected_and_noncompact":True,
            "real_is_pure_finite_inverse_limit":False,
            "p_adic_full_local_field_is_just_a_compact_residue_tower":False,
            "finite_local_plus_Arch_Tate_completed":False,
            "RH_proved":False}



def exact_local_biaxial_diamond(chart: PadicBruhatChart,
                               raw: tuple[int|Q,...]) -> dict:
    """Proof instrument: support-growth and precision-growth commute STRICTLY.

    Two construction paths (r,s)->(r+1,s)->(r+1,s+1)
    and (r,s)->(r,s+1)->(r+1,s+1) give IDENTICAL source functions
    on p^-(r+1)Zp / p^(s+1)Zp, then identical Fourier values.

    This is the actual two-dimensional recursive model-of-model
    coherence law for local compact support AND local resolution.
    """
    if not isinstance(chart,PadicBruhatChart):
        raise AtomicDescentError("Original rational-place p-adic chart required")
    source=chart.values(raw)
    p=chart.p;n=chart.modulus
    target=PadicBruhatChart(p,chart.support_depth+1,
                           chart.precision_depth+1)
    # support then precision: f_r(pa)=f(a), zeros otherwise,
    # then repeat values modulo p*n
    support_vals=[Q() for _ in range(p*n)]
    for a,v in enumerate(source):
        support_vals[p*a]=v
    result_A=tuple(support_vals[k%(p*n)] for k in range(p*p*n))
    # precision then support: f_s(a)=f(a mod n); then insert at p*a
    precision_vals=tuple(source[k%n] for k in range(p*n))
    support_prec=[Q() for _ in range(p*p*n)]
    for a,v in enumerate(precision_vals):
        support_prec[p*a]=v
    result_B=tuple(support_prec)
    if result_A!=result_B:
        raise ArithmeticError("Tate p-adic support/precision model cube failed")
    Fa=local_tate_fourier(target,result_A)
    Fb=local_tate_fourier(target,result_B)
    if Fa!=Fb:
        raise ArithmeticError("Tate p-adic Fourier dual cube failed")
    return {"prime":p,"base_chart":(chart.support_depth,chart.precision_depth),
            "terminal_chart":(target.support_depth,target.precision_depth),
            "all_terminal_cells_verified":target.modulus,
            "strict_source_diamond_commutes":True,
            "dual_Fourier_diamond_commutes":True,
            "source_map_adequate_to_full_adele":False,
            "RH_proved":False}


def exact_crt_product_fourier(
        a_prime:int, a_exponent:int,
        b_prime:int, b_exponent:int,
        a_values:tuple[int|Q,...], b_values:tuple[int|Q,...]) -> dict:
    """Exact Fourier tensor square at TWO genuine, distinct finite places.

    CRT x=a_coord * E_a + b_coord * E_b mod N, with
       E_a=b*inv(b mod a), E_b=a*inv(a mod b).
    The DUAL Fourier frequency is NOT naively (k mod a,k mod b):
       k_a=k*inv(b mod a) mod a,
       k_b=k*inv(a mod b) mod b.
    Those inverse transports are SOURCE-NECESSARY. A stage N which is
    composite is a legitimate joint observer quotient, not an Euler p=N.

    Computes all N Fourier coefficients by two mathematically distinct
    routes, in exact Q(zeta_N), no floating phases or RH zero inputs.
    """
    _integer(a_prime,2,11);_integer(b_prime,2,11)
    _integer(a_exponent,1,4);_integer(b_exponent,1,4)
    if not prime(a_prime) or not prime(b_prime) or a_prime==b_prime:
        raise AtomicDescentError("Two DISTINCT genuine finite Euler places required")
    a,b=a_prime**a_exponent,b_prime**b_exponent
    N=a*b
    if N>36:
        raise AtomicDescentError("CRT exact cyclotomic proof budget N<=36")
    if type(a_values) is not tuple or type(b_values) is not tuple:
        raise AtomicDescentError("Complete original residue source tables required")
    if len(a_values)!=a or len(b_values)!=b:
        raise AtomicDescentError("CRT source tensor factors have wrong cardinalities")
    fa=tuple(_rational(v) for v in a_values)
    fb=tuple(_rational(v) for v in b_values)
    inv_b=pow(b,-1,a)
    inv_a=pow(a,-1,b)
    source=tuple(fa[x%a]*fb[x%b] for x in range(N))
    global_spec=tuple(z.scale(Q(1,N)) for z in exact_dft(source))
    disagreement_naive=0
    for k in range(N):
        # The correct local tensor path, transported to one common phase root.
        ca=(k*inv_b)%a
        cb=(k*inv_a)%b
        tA=CyclotomicElement.scalar(N,0)
        for u,weight in enumerate(fa):
            tA=tA+CyclotomicElement.root(N,b*ca*u).scale(weight)
        tA=tA.scale(Q(1,a))
        tB=CyclotomicElement.scalar(N,0)
        for v,weight in enumerate(fb):
            tB=tB+CyclotomicElement.root(N,a*cb*v).scale(weight)
        tB=tB.scale(Q(1,b))
        if global_spec[k]!=tA*tB:
            raise ArithmeticError("CRT source Fourier tensor transport violated")
        # Wrong transport: naively k mod a,b, not the dual CRT idempotents.
        wrongA=CyclotomicElement.scalar(N,0)
        for u,weight in enumerate(fa):
            wrongA=wrongA+CyclotomicElement.root(N,b*(k%a)*u).scale(weight)
        wrongA=wrongA.scale(Q(1,a))
        wrongB=CyclotomicElement.scalar(N,0)
        for v,weight in enumerate(fb):
            wrongB=wrongB+CyclotomicElement.root(N,a*(k%b)*v).scale(weight)
        wrongB=wrongB.scale(Q(1,b))
        if global_spec[k]!=wrongA*wrongB:
            disagreement_naive+=1
    return {"actual_distinct_Euler_primes":(a_prime,b_prime),
            "observation_moduli":(a,b),"joint_CRT_modulus":N,
            "correct_dual_transports":(inv_b,inv_a),
            "global_dual_frequencies_verified":N,
            "exact_CRT_Fourier_product":True,
            "naive_frequency_transport_disagreement_count":disagreement_naive,
            "joint_composite_modulus_not_a_primitive_Euler_place":True,
            "global_adelic_Poisson_not_constructed":True,
            "RH_proved":False}
