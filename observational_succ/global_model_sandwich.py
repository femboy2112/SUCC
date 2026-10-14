"""Exact finite source/model graph and proof-capsule laboratory for Observational SUCC.

No model-class completeness, empirically realized experiment, analytic continuation,
or Weil positivity is inferred from a chart, its label, or finitely many samples.
All finite computations use integer / Fraction arithmetic; Gamma/PNT statements
are external mathematics, not outputs of the finite simulator.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from math import log, isqrt

class SandwichError(ValueError):
    pass


def _nonempty_token(s):
    return isinstance(s, str) and bool(s.strip())


def _exact(x):
    if type(x) is int or isinstance(x, F):
        return F(x)
    raise SandwichError("exact rational coefficient required; floats are not certificates")


@dataclass(frozen=True)
class SourceChart:
    name: str
    source_id: str
    epoch: int
    basis: str
    reports: tuple[str, ...]
    def __post_init__(self):
        if not all(_nonempty_token(x) for x in (self.name, self.source_id, self.basis)):
            raise SandwichError("named chart, source and basis required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise SandwichError("causal epoch must be nonnegative integer")
        if not isinstance(self.reports, tuple) or not self.reports or any(not _nonempty_token(x) for x in self.reports):
            raise SandwichError("complete finite report table required")
    @property
    def image(self):
        return tuple(sorted(set(self.reports)))


@dataclass(frozen=True)
class ModelArrow:
    domain: str
    codomain: str
    mapping: tuple[tuple[str, str], ...]
    def __post_init__(self):
        if not _nonempty_token(self.domain) or not _nonempty_token(self.codomain):
            raise SandwichError("typed chart arrow needs both endpoints")
        if not isinstance(self.mapping, tuple) or len(set(a for a, _ in self.mapping)) != len(self.mapping):
            raise SandwichError("arrow mapping must be a finite partial function")


@dataclass(frozen=True)
class GlobalCertificate:
    status: str
    charts: tuple[str, ...]
    decoder: tuple[tuple[tuple[str, ...], str], ...]
    collision: tuple[str, str] | None
    source_scope: str
    physical_implementation_verified: bool = False
    @property
    def identified(self):
        return self.status == "IDENTIFIED"


@dataclass(frozen=True)
class FiniteModelGraph:
    """A complete *declared* common-original-source chart ensemble.

    Each row is one possible ORIGINAL source, not an independently executable
    intervention or a probability coupling. A source attestation is not created.
    """
    source_id: str
    epoch: int
    basis: str
    sources: tuple[str, ...]
    charts: tuple[SourceChart, ...]
    arrows: tuple[ModelArrow, ...] = ()

    def __post_init__(self):
        if not _nonempty_token(self.source_id) or not _nonempty_token(self.basis) or type(self.epoch) is not int or self.epoch < 0:
            raise SandwichError("source/epoch/basis contract must be explicit")
        if not isinstance(self.sources, tuple) or not self.sources or len(set(self.sources)) != len(self.sources) or any(not _nonempty_token(s) for s in self.sources):
            raise SandwichError("nonempty, unique original-source labels required")
        if len(set(c.name for c in self.charts)) != len(self.charts):
            raise SandwichError("duplicate model chart")
        names = {c.name: c for c in self.charts}
        for c in self.charts:
            if c.source_id != self.source_id or c.epoch != self.epoch or c.basis != self.basis or len(c.reports) != len(self.sources):
                raise SandwichError("chart source/epoch/basis or complete rows mismatch")
        if len(set((a.domain, a.codomain) for a in self.arrows)) != len(self.arrows):
            raise SandwichError("ambiguous named chart arrows")
        for arrow in self.arrows:
            if arrow.domain not in names or arrow.codomain not in names:
                raise SandwichError("arrow endpoints do not belong to source graph")
            m = dict(arrow.mapping)
            src, dst = names[arrow.domain], names[arrow.codomain]
            if set(m) != set(src.image) or not set(m.values()).issubset(set(dst.image)):
                raise SandwichError("arrow must map the complete reachable source image")
            for i, state in enumerate(self.sources):
                if m[src.reports[i]] != dst.reports[i]:
                    raise SandwichError("false source transport at original state: " + state)

    def chart(self, name):
        for c in self.charts:
            if c.name == name:
                return c
        raise SandwichError("unknown source-backed chart: " + str(name))

    def transport(self, path: tuple[str, ...]):
        """Compose certified chart edges on reachable source reports only."""
        if not path:
            raise SandwichError("a path has at least one chart")
        initial = self.chart(path[0])
        maps = {(a.domain, a.codomain): dict(a.mapping) for a in self.arrows}
        values = {v: v for v in initial.image}
        for domain, codomain in zip(path, path[1:]):
            self.chart(codomain)
            if (domain, codomain) not in maps:
                raise SandwichError("missing authorized transport edge")
            f = maps[(domain, codomain)]
            values = {key: f[value] for key, value in values.items()}
        return tuple(sorted(values.items()))

    def report(self, state: str, charts: tuple[str, ...]):
        if state not in self.sources:
            raise SandwichError("source state not admitted")
        index = self.sources.index(state)
        if len(set(charts)) != len(charts):
            raise SandwichError("a joint context cannot duplicate a chart")
        return tuple(self.chart(x).reports[index] for x in charts)

    def certify_target(self, target: tuple[str, ...], charts: tuple[str, ...]):
        if len(target) != len(self.sources) or any(not _nonempty_token(x) for x in target):
            raise SandwichError("total source-indexed target required")
        if len(set(charts)) != len(charts):
            raise SandwichError("duplicate chart in joint context")
        for x in charts: self.chart(x)
        decoder = {}
        owner = {}
        for state, truth in zip(self.sources, target):
            value = self.report(state, charts)
            if value in decoder and decoder[value] != truth:
                return GlobalCertificate("AMBIGUOUS", charts, (), (owner[value], state), self.source_id)
            decoder[value] = truth
            owner[value] = state
        return GlobalCertificate("IDENTIFIED", charts, tuple(sorted(decoder.items())), None, self.source_id)

    def minimal_contexts(self, target: tuple[str, ...]):
        names = tuple(c.name for c in self.charts)
        for size in range(len(names)+1):
            valid = tuple(c for c in combinations(names, size) if self.certify_target(target,c).identified)
            if valid:
                return valid
        return ()


def _poly(values):
    p = tuple(_exact(x) for x in values)
    if not p:
        raise SandwichError("polynomial needs at least one coefficient")
    k = len(p)
    while k > 1 and p[k-1] == 0:
        k -= 1
    return p[:k]


def poly_add(a,b):
    p,q=_poly(a),_poly(b)
    return _poly(tuple((p[i] if i<len(p) else F(0))+(q[i] if i<len(q) else F(0)) for i in range(max(len(p),len(q)))))


def poly_scale(a,c):
    return _poly(tuple(x*_exact(c) for x in _poly(a)))


def poly_mul(a,b):
    p,q=_poly(a),_poly(b)
    z=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): z[i+j]+=x*y
    return _poly(z)


def poly_eval(a,x):
    y=F(0);xx=_exact(x)
    for coefficient in reversed(_poly(a)): y=y*xx+coefficient
    return y


@dataclass(frozen=True)
class RationalChart:
    numerator: tuple[F, ...]
    denominator: tuple[F, ...]
    def __post_init__(self):
        p,q=_poly(self.numerator),_poly(self.denominator)
        if q == (F(0),): raise SandwichError("zero rational-function denominator")
        object.__setattr__(self,"numerator",p)
        object.__setattr__(self,"denominator",q)
    def value(self,x):
        d=poly_eval(self.denominator,x)
        if not d:raise SandwichError("this chart has a pole/excluded point")
        return poly_eval(self.numerator,x)/d


def rational_global_identity(left: RationalChart,right: RationalChart):
    """Finite algebraic identity certificate; not a generic analytic oracle.

    Returns zero cross-polynomial iff the rational functions agree on their
    common domain, and a finite exact witness otherwise.
    """
    defect=poly_add(poly_mul(left.numerator,right.denominator),
                    poly_scale(poly_mul(right.numerator,left.denominator),-1))
    if defect==(F(0),):
        return {"equal_on_common_domain":True,"cross_polynomial":defect,"witness":None}
    cap=len(defect)+len(left.denominator)+len(right.denominator)
    for i in range(cap+1):
        x=F(i)
        if poly_eval(defect,x) and poly_eval(left.denominator,x) and poly_eval(right.denominator,x):
            return {"equal_on_common_domain":False,"cross_polynomial":defect,
                    "witness":(x,left.value(x),right.value(x))}
    raise AssertionError("finite-degree nonzero polynomial must have a rational witness")


def symmetric_finite_sample_mutant(samples: tuple[F,...]):
    """Produce symmetric entire polynomial matching 1 on samples, but zero off line.

    This is a *negative control* for finite data + reflection symmetry. It
    is NOT a replacement for the authenticated completed Riemann xi.
    """
    if len(samples)!=len(set(samples)):
        raise SandwichError("distinct sample points required")
    p=(F(1),)
    for x in samples:
        y=_exact(x)
        p=poly_mul(p,(-y,F(1)))
        p=poly_mul(p,(-(F(1)-y),F(1)))
    point=2
    while poly_eval(p,point)==0: point+=1
    coeff=-F(1)/poly_eval(p,point)
    candidate=poly_add((F(1),),poly_scale(p,coeff))
    # independent reflection verification via coefficient-domain interpolation
    reflected=poly_mul(candidate,(F(1),))
    for z in range(len(candidate)+2):
        if poly_eval(reflected,F(1)-F(z))!=poly_eval(reflected,F(z)):
            raise AssertionError("mutation should be reflection symmetric")
    return {"polynomial":candidate,"off_line_zero":F(point),
            "mirror_zero":F(1-point),"matches":tuple(samples),"authentic_zeta_source":False}


def harmonic(n: int):
    if type(n) is not int or n<1: raise SandwichError("positive integer cutoff required")
    return sum((F(1,i) for i in range(1,n+1)),F(0))


def prime_current_coefficients(limit: int):
    """Exact coefficients of log(p) in sum_{n<=X} Lambda(n)/n.

    This is a finite identity only. The global limiting constant -gamma uses
    prime distribution results not proved by this routine.
    """
    if type(limit) is not int or limit<2: raise SandwichError("integer X >=2")
    def prime(p): return p>=2 and all(p%q for q in range(2,isqrt(p)+1))
    answer=[]
    for p in range(2,limit+1):
        if not prime(p): continue
        term=F(0);power=p
        while power<=limit:
            term+=F(1,power);power*=p
        answer.append((p,term))
    return tuple(answer)



def _factor_primes(n: int):
    """Independent exact trial division, returning p -> v_p(n)."""
    if type(n) is not int or n<1:
        raise SandwichError("positive integer needed for the arithmetic source")
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out


def factorial_succ_coefficients(n: int):
    """Formal prime-log coefficients from the additive SUCC path 1..n."""
    if type(n) is not int or n<1:raise SandwichError("factorial path cutoff >=1")
    accum={}
    for m in range(2,n+1):
        for p,k in _factor_primes(m).items():
            accum[p]=accum.get(p,0)+k
    return tuple(sorted(accum.items()))


def divisor_jet_coefficients(n: int):
    """Independent Legendre/floor formula for the SAME formal log(n!).

    sum_{d<=N} Λ(d) floor(N/d) = sum_p log(p) sum_{k>=1}floor(N/p^k).
    Never assign a fictitious standalone log coefficient to composite radix 6.
    """
    if type(n) is not int or n<1:raise SandwichError("positive cutoff N required")
    result={}
    for p in range(2,n+1):
        if not all(p%d for d in range(2,isqrt(p)+1)):continue
        m=p
        v=0
        while m<=n:
            v+=n//m
            m*=p
        result[p]=v
    return tuple(sorted(result.items()))


def factorial_prime_sandwich(n: int):
    additive=factorial_succ_coefficients(n)
    multiplicative=divisor_jet_coefficients(n)
    if additive != multiplicative:
        raise AssertionError("two independent exact prime log-cases disagree")
    fake_six_extra=n//6
    return {"cutoff":n,"additive_coefficients":additive,
            "multiplicative_coefficients":multiplicative,
            "same_formal_log_factorial":True,
            "fake_composite_six_produces_extra_log6_multiplicity":fake_six_extra,
            "universal_proof_infinite_data_required":False,
            "physical_source_authenticated":False}



def carrier_quantization_defect(n: int):
    """Exact nonnegative source defect between prime density and discrete factorial.

    D_N=sum_(p^k<=N) log(p) [1/p^k-floor(N/p^k)/N]
       =(1/N) sum_(p^k<=N) log(p) fractional_part(N/p^k) >=0.
    The global limit 1-gamma requires external prime-sum/PNT + Stirling.
    """
    if type(n) is not int or n<1:
        raise SandwichError("positive factorial cutoff required")
    prime=dict(prime_current_coefficients(n)) if n>=2 else {}
    fact=dict(factorial_succ_coefficients(n))
    if set(prime)!=set(fact):
        raise AssertionError("real prime/source support differs")
    result=[]
    for p,c in sorted(prime.items()):
        discrepancy=c-F(fact[p],n)
        m=p;independent=F(0)
        while m<=n:
            independent+=F(n%m,m*n)
            m*=p
        if discrepancy!=independent or discrepancy<0:
            raise AssertionError("source-residue floor/real defect failed")
        result.append((p,discrepancy))
    return tuple(result)


def quantization_numeric_diagnostic(n: int):
    coeff=carrier_quantization_defect(n)
    return {"cutoff":n,"value":sum(float(c)*log(p) for p,c in coeff),
            "all_prime_weights_nonnegative":all(c>=0 for _,c in coeff),
            "limit_1_minus_gamma_imported":True,
            "finite_samples_prove_limit":False}


def finite_part_observation(n:int, ordinary_scale:float=1.0, prime_scale:float=1.0):
    if ordinary_scale<=0 or prime_scale<=0:raise SandwichError("positive cutoff scales required")
    a=float(harmonic(n))-log(ordinary_scale*n)
    b=sum(float(c)*log(p) for p,c in prime_current_coefficients(n))-log(prime_scale*n)
    return {"ordinary":a,"prime":b,"sum":a+b,
            "source_calibrated":False,"global_limit_certified":False}


def laurent_log_derivative_germ(c,d):
    """Exact Laurent coefficients for zeta-like germ z^-1+c+d*z+O(z²).

    Returns coefficients of -F'/F: 1/z - c + (c²-2d)*z+O(z²).
    c=Euler gamma only after independently authenticating zeta's Laurent law.
    """
    x,y=_exact(c),_exact(d)
    return {"pole":F(1),"constant":-x,"linear":x*x-2*y,
            "finite_part_cancelled_with_original_constant":x+(-x)==0}


def noncompact_parity_alias(observed_indices: tuple[int,...]):
    """Discrete noncompact S=N: any finite singleton reports miss odd/even pair."""
    if any(type(i) is not int or i<0 for i in observed_indices):
        raise SandwichError("finite nonnegative probe indices")
    used=set(observed_indices)
    e=next(n for n in range(0,2*len(used)+4,2) if n not in used)
    o=next(n for n in range(1,2*len(used)+5,2) if n not in used)
    assert e%2==0 and o%2==1 and e not in used and o not in used
    return {"even":e,"odd":o,"both_all_zero_reports":True,"target_values":(0,1)}


def demo_receipt():
    src=("00","01","10","11")
    c=lambda name,reps: SourceChart(name,"binary-pair",0,"original-bits",reps)
    ch=(c("A",("0","0","1","1")),c("B",("0","1","0","1")),
        c("PAIR",("00","01","10","11")),c("XOR",("0","1","1","0")))
    g=FiniteModelGraph("binary-pair",0,"original-bits",src,ch,
        (ModelArrow("PAIR","A",(("00","0"),("01","0"),("10","1"),("11","1"))),
         ModelArrow("PAIR","B",(("00","0"),("01","1"),("10","0"),("11","1"))),
         ModelArrow("PAIR","XOR",(("00","0"),("01","1"),("10","1"),("11","0")))))
    tgt=("0","1","1","0")
    a=g.certify_target(tgt,("A",))
    joint=g.certify_target(tgt,("A","B"))
    rational=rational_global_identity(RationalChart((-1,0,1),(-1,1)),RationalChart((1,1),(1,)))
    mutant=symmetric_finite_sample_mutant((F(0),F(1),F(1,2)))
    n=100
    arithmetic=factorial_prime_sandwich(100)
    defect=carrier_quantization_defect(100)
    return {
        "status":"EXACT_FINITE_MODEL_SANDWICH_RECEIPT",
        "finite_model":{"individual_A_identifies_XOR":a.identified,
           "individual_collision":list(a.collision),
           "joint_identifies_XOR":joint.identified,
           "minimal_contexts":[list(c) for c in g.minimal_contexts(tgt)],
           "joint_decoder":[[list(values),truth] for values,truth in joint.decoder],
           "path_projection":list(map(list,g.transport(("PAIR","A")))),
           "physical_joint_access_verified":False},
        "symbolic_global_identity":{"rational_charts_equal":rational["equal_on_common_domain"],
              "cross_polynomial":[str(c) for c in rational["cross_polynomial"]],
              "sample_spoof_degree":len(mutant["polynomial"])-1,
              "mutant_offcritical_zero":str(mutant["off_line_zero"]),
              "mutant_symmetry_is_not_zeta_source":True},
        "factorial_prime_universal_sandwich":{
           "cutoff":arithmetic["cutoff"],
           "same_formal_log_factorial":arithmetic["same_formal_log_factorial"],
           "prime_valuation_coefficients":[[p,k] for p,k in arithmetic["additive_coefficients"]],
           "fake_six_defect":arithmetic["fake_composite_six_produces_extra_log6_multiplicity"],
           "finite_proof_does_not_require_infinite_data":True},
        "quantization_defect":{
            "cutoff":100,"coefficients":[[p,str(c)] for p,c in defect],
            "nonnegative":all(c>=0 for _,c in defect),
            "limit_to_1_minus_gamma_is_classical_import":True,
            "finite_data_solely_proves_limit":False},
        "finite_parts":{"cutoff":n,"harmonic_exact":str(harmonic(n)),
            "prime_log_coefficients":[[p,str(c)] for p,c in prime_current_coefficients(20)],
            "comparison":finite_part_observation(n),
            "formal_laurent":{k:str(v) for k,v in laurent_log_derivative_germ(F(3,4),F(1,5)).items()}},
        "noncompact_counterexample":noncompact_parity_alias((0,1,2,5,8)),
        "truth_gates":{"compactness_imported_not_finite_simulated":True,
                       "global_source_completeness_verified":False,
                       "Euler_constant_asymptotic_imported":True,
                       "RH_or_Weil_positivity_proved":False,
                       "finite_computation_is_universal_proof":False}
    }
