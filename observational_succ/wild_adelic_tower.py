"""WILD/ARITHMETIC SUCC: source-qualified circle-cover towers and their invariants.

This is a FINITE SYMBOLIC CERTIFIER of classical infinite tower formulas, not a
numerical model of an Alexander horned sphere or a proof of Weil positivity.

An infinite prime-occurrence conclusion is available ONLY from a declared
symbolic generating law, never from a finite observed prefix. The ambient
3-sphere embedding is an *independent typed contract*: the intrinsic solenoid
alone does not determine its exterior group.

Every arithmetic operation below is exact (integers or Fraction).
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd, lcm, isqrt
from typing import Iterable


class WildTowerError(ValueError):
    pass


def _prime(n: int) -> bool:
    return type(n) is int and n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def _factors(n: int) -> dict[int, int]:
    if type(n) is not int or n < 1:
        raise WildTowerError('positive integer required')
    d, out = 2, {}
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def _vp(n: int, p: int) -> int:
    if not _prime(p) or type(n) is not int or n <= 0:
        raise WildTowerError('positive integer and actual prime required')
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def _nth_prime(k: int) -> int:
    if type(k) is not int or k < 1 or k > 10000:
        raise WildTowerError('1 <= k <= 10000 for this bounded implementation')
    n, count = 2, 0
    while True:
        if _prime(n):
            count += 1
            if count == k:
                return n
        n += 1


def _mod1(x: F) -> F:
    return x % 1


@dataclass(frozen=True)
class TowerLaw:
    """A declared INFINITE mathematical source law (not empirical attestation).

    constant q: q_n=q; factorial q_n=n+1; distinct_primes q_n=p_n;
    prefix_constant q_i=prefix[i-1] initially, then q_i=constant.
    Finite prefixes alone do NOT imply anything about the unspecified tail.
    """
    source_id: str
    epoch: int
    basis: str
    kind: str
    constant: int = 2
    prefix: tuple[int, ...] = ()

    def __post_init__(self):
        if not all(isinstance(x, str) and x.strip() for x in (self.source_id, self.basis)):
            raise WildTowerError('source and basis required')
        if type(self.epoch) is not int or self.epoch < 0:
            raise WildTowerError('nonnegative epoch required')
        if self.kind not in ('constant', 'factorial', 'distinct_primes', 'prefix_constant'):
            raise WildTowerError('a COMPLETE symbolic tail law is mandatory')
        if type(self.constant) is not int or self.constant < 2:
            raise WildTowerError('cover degree must be >=2')
        if any(type(x) is not int or x < 2 for x in self.prefix):
            raise WildTowerError('all finite cover degrees must be >=2')
        if self.kind != 'prefix_constant' and self.prefix:
            raise WildTowerError('unused finite source prefix rejected')

    def degree(self, n: int) -> int:
        if type(n) is not int or n < 1:
            raise WildTowerError('positive level index required')
        if self.kind == 'constant':
            return self.constant
        if self.kind == 'factorial':
            return n + 1
        if self.kind == 'distinct_primes':
            return _nth_prime(n)
        if n <= len(self.prefix):
            return self.prefix[n - 1]
        return self.constant

    def D(self, n: int) -> int:
        if type(n) is not int or n < 0 or n > 10000:
            raise WildTowerError('bounded stage computation: 0<=n<=10000')
        d = 1
        for j in range(1, n+1):
            d *= self.degree(j)
        return d

    def stage_map(self, n: int, k: int) -> int:
        """Z at level n -> Z at deeper level k, multiplier D_k/D_n."""
        if type(n) is not int or type(k) is not int or n < 0 or k < n:
            raise WildTowerError('0 <= n <= k required')
        return self.D(k) // self.D(n)

    def localized_generator(self, n: int) -> F:
        return F(1, self.D(n))

    def localization_value(self, n: int, numerator: int) -> F:
        if type(numerator) is not int:
            raise WildTowerError('integer winding required')
        return numerator * self.localized_generator(n)

    def prime_unbounded(self, p: int) -> bool:
        """Theorem: v_p(D_n) -> infinity iff tail repeats a p-divisible q."""
        if not _prime(p):
            raise WildTowerError('actual prime required')
        if self.kind == 'factorial':
            return True
        if self.kind == 'distinct_primes':
            return False
        return self.constant % p == 0

    def bounded_prime_depth(self, p: int) -> int | None:
        """Supremum of v_p(D_n), or None for unbounded valuation.

        For distinct primes, v_p(D_n) eventually equals 1 for every
        genuine p, despite its appearance at only ONE finite stage.
        """
        if not _prime(p):
            raise WildTowerError('actual prime required')
        if self.prime_unbounded(p):
            return None
        if self.kind == 'distinct_primes':
            return 1
        return sum(_vp(q,p) for q in self.prefix)

    def admits_rational(self, number: F | int) -> bool:
        """Does the rational belong to colim Z --xq--> Z inside Q?

        A finite prefix observation is not supplied as a complete law;
        this conclusion depends on the source's infinite generator.
        """
        if type(number) not in (F, int):
            raise WildTowerError('exact rational required')
        for p, e in _factors(F(number).denominator).items():
            bound = self.bounded_prime_depth(p)
            if bound is not None and e > bound:
                return False
        return True

    def scale_automorphism(self, m: int) -> bool:
        """A_m:z_n->z_n^m is an inverse-limit automorphism iff mG=G."""
        return all(self.prime_unbounded(p) for p in _factors(m))

    def dual_kernel_order(self, m: int) -> int:
        """Size of ker(A_m), from G/mG; prime absent from infinite tail stays."""
        answer = 1
        for p, exponent in _factors(m).items():
            if not self.prime_unbounded(p):
                answer *= p**exponent
        return answer

    def finite_kernel_image_order(self, n: int, k: int, m: int) -> int:
        """Image cardinality of the deeper m-fold circle kernel at level n.

        Every circle stage kernel is mu_m = Z/m. The bonding map from
        stage k to n is multiplication D_k/D_n on Z/m, with image size
             m / gcd(m, D_k/D_n).
        This is exact pro-kernel bookkeeping, NOT an assumption that the
        coordinatewise kernels are globally compatible free choices.
        """
        _factors(m)
        return m // gcd(m, self.stage_map(n, k))

    def kernel_collapse_depth(self, n: int, m: int) -> int:
        """Find a deeper stage where the local kernel image is trivial.
        Such a stage exists for every n iff A_m is a global automorphism.
        """
        k = self.inverse_level(n, m)
        assert self.finite_kernel_image_order(n, k, m) == 1
        return k

    def inverse_level(self, n: int, m: int) -> int:
        """Least deeper coordinate needed for inverse at level n, if legal.

        If A_m is a homeomorphism, some D_k/D_n is divisible by m for each n;
        otherwise NO coherent global inverse is licensed.
        """
        if not self.scale_automorphism(m):
            raise WildTowerError('A_m not invertible on this global source tower')
        if type(n) is not int or n < 0:
            raise WildTowerError('nonnegative stage required')
        factor = 1
        k = n
        while factor % m:
            k += 1
            factor *= self.degree(k)
            if k - n > 10000:
                raise WildTowerError('implementation budget exhausted')
        return k

    def inverse_coordinate(self, n: int, m: int, phases: tuple[F, ...]) -> F:
        """Given compatible target circle phases theta[0..k], produce unique
        preimage theta'_n = (D_k/(m D_n))*theta_k mod 1.
        The inverse needs DEEPER source data, not an arbitrary mth root.
        """
        k = self.inverse_level(n, m)
        if len(phases) <= k:
            raise WildTowerError('deeper source phase required for inverse')
        if not self.compatible_phases(phases):
            raise WildTowerError('fake/incompatible circle source phases')
        scale = self.stage_map(n, k)
        assert scale % m == 0
        return _mod1(F(scale // m)*phases[k])

    def compatible_phases(self, phases: tuple[F, ...]) -> bool:
        if not isinstance(phases, tuple) or not phases:
            return False
        if any(type(x) not in (F, int) or not (F(0) <= x < 1) for x in phases):
            return False
        return all(_mod1(phases[j]*self.degree(j)) == phases[j-1]
                   for j in range(1, len(phases)))

    def real_flow_phases(self, t: F | int, depth: int) -> tuple[F, ...]:
        """Dense Archimedean one-parameter orbit iota(t)."""
        if type(t) not in (int, F):
            raise WildTowerError('exact rational parameter required')
        return tuple(_mod1(F(t, self.D(j))) for j in range(depth+1))

    def scale_phases(self, phases: tuple[F, ...], m: int) -> tuple[F, ...]:
        if not self.compatible_phases(phases):
            raise WildTowerError('source coherence failed')
        _factors(m)
        return tuple(_mod1(m*x) for x in phases)

    def flow_character_phase(self, level: int, winding: int, t: F | int) -> F:
        """Character xi_(winding/D_level) evaluated at iota(t), as R/Z.

        Exact algebra: chi_(r)(iota(t)) = exp(2*pi*i*r*t).
        This is the PURE-POINT character law on the compact solenoid;
        it is emphatically NOT a Lebesgue-Plancherel L2(R) plane wave.
        """
        if type(winding) is not int or type(t) not in (int, F):
            raise WildTowerError('exact character and real-flow rational phase needed')
        return _mod1(F(winding, self.D(level))*F(t))

    def finite_fiber_residues(self, integer: int, depth: int) -> tuple[int, ...]:
        if type(integer) is not int:
            raise WildTowerError('finite fiber index is integral')
        return tuple(integer % self.D(n) for n in range(depth+1))

    def delta_circle_root(self, m: int, r: int, stage: int) -> int:
        """For factorial/universal tower, exact snake-lemma delta:
        mu_m -> Zhat/mZhat = Z/mZ, exp(2pi i*r/m) -> r mod m.
        The lift iota(r/m) has m*lift=iota(r) in the profinite fiber.
        """
        if self.kind != 'factorial':
            raise WildTowerError('this exact Zhat snake contract uses factorial law')
        if type(r) is not int or type(stage) is not int or type(m) is not int or stage < 0 or m < 1:
            raise WildTowerError('integer root and stage required')
        if self.D(stage) % m:
            raise WildTowerError('stage does not resolve Zhat/mZhat')
        return r % m

    def prime_jet(self, p: int, depth: int) -> tuple[int, ...]:
        """Actual prime powers, unlike generic composite covering degrees."""
        if not _prime(p) or type(depth) is not int or depth < 1:
            raise WildTowerError('primitive Euler jet requires a genuine prime')
        return tuple(p**j for j in range(1, depth+1))


@dataclass(frozen=True)
class ExteriorEmbeddingContract:
    """Conditional source contract; no ambient embedding is fabricated.

    'unknotted_torus' means a separately stipulated nested 3D embedding with
    unknotted stages and meridian inclusion multiplication by degree_n.
    This class certifies GROUP ALGEBRA given that geometric input; it does
    NOT certify that particular 3D geometry was built or observed.
    """
    law: TowerLaw
    embedding_id: str
    source_id: str
    epoch: int
    ambient: str

    def __post_init__(self):
        if not isinstance(self.embedding_id, str) or not self.embedding_id.strip():
            raise WildTowerError('named embedding contract required')
        if self.source_id != self.law.source_id or self.epoch != self.law.epoch:
            raise WildTowerError('ambient embedding original-source mismatch')
        if self.ambient not in ('unknotted_torus', 'unspecified'):
            raise WildTowerError('no forged knotting or exterior theorem')

    def meridian_transport(self, stage_from: int, stage_to: int, m: int) -> int:
        if self.ambient != 'unknotted_torus':
            raise WildTowerError('extrinsic meridian source is not supplied')
        if type(m) is not int:
            raise WildTowerError('integer fundamental group generator required')
        return self.law.stage_map(stage_from, stage_to)*m

    def exterior_group_value(self, stage: int, winding: int) -> F:
        if self.ambient != 'unknotted_torus':
            raise WildTowerError('intrinsic tower does not identify its ambient complement')
        return self.law.localization_value(stage, winding)


@dataclass(frozen=True)
class CohomologyWindingCertificate:
    """Cech H^1(Sigma; Z) = colim (Z, x->q_n*x) conditional on
    the standard continuity theorem for inverse limits of compact circles.
    Exact finite stage naturality tests are useful but not a computer proof
    of the external Cech-continuity theorem.
    """
    law: TowerLaw

    def transport(self, stage_from: int, stage_to: int, n: int) -> tuple[int, F]:
        if type(n) is not int:
            raise WildTowerError('integer cohomology generator')
        integer = self.law.stage_map(stage_from, stage_to)*n
        return integer, self.law.localization_value(stage_to, integer)


def fiber_isomorphism_on_finite_stage(law: TowerLaw, n: int, r: int) -> F:
    """Fiber pi_0^-1(1) at level n is Z/D_n, angle r/D_n."""
    if type(r) is not int:
        raise WildTowerError('integer residue needed')
    return _mod1(F(r, law.D(n)))


def rational_folner_energy(steps: Iterable[tuple[F, F]], N: int) -> F:
    """Exact finite support witness for no uniform translation-square gap.

    G includes Z[steps] as subgroup of the rational localization when the
    steps are actually in that G. Given rational translations s_i and
    nonnegative weights w_i, let D=lcm denominators, f_N supported on
    {-N/D,...,N/D}, constant amplitude 1/sqrt(2N+1).
    E_N=sum_i w_i ||f_N - tau_(s_i) f_N||^2 =
      sum_i w_i * 2min(|D s_i|,2N+1)/(2N+1).
    This is an exact *rational* energy ratio; no asserted Weil identification.
    """
    if type(N) is not int or N < 1:
        raise WildTowerError('N>=1 required')
    steps = tuple(steps)
    if not steps:
        return F(0)
    if any(type(step) not in (F, int) or type(weight) not in (F, int) or weight < 0
           for step, weight in steps):
        raise WildTowerError('exact rational nonnegative weighted translations only')
    D = lcm(*(F(step).denominator for step, _ in steps))
    m = 2*N+1
    return sum((F(weight)*F(2*min(abs(D*F(step)),m),m)
                for step, weight in steps), F(0))


def source_qualified_folner_energy(law: TowerLaw, steps: Iterable[tuple[F, F]], N: int) -> F:
    """Folner ratio only for translations actually IN this arithmetic group.

    A fake shift at 1/3 on the dyadic solenoid fails rather than silently
    switching to a larger carrier. This is a source-membership contract.
    """
    steps = tuple(steps)
    for shift, weight in steps:
        if not law.admits_rational(shift):
            raise WildTowerError('requested translation is not in the actual source localization')
    return rational_folner_energy(steps, N)


def finite_arithmetic_no_free_tail(prefix: tuple[int, ...], p: int, r: int) -> dict:
    """Same finite observed degrees, globally DIFFERENT invertibility of A_p.
    Both tails are independently declared source laws, not inferred from prefix.
    """
    if not _prime(p) or not _prime(r) or p == r:
        raise WildTowerError('two distinct true primes required')
    a = TowerLaw('counterfactual', 0, 'angles', 'prefix_constant', p, prefix)
    b = TowerLaw('counterfactual', 0, 'angles', 'prefix_constant', r, prefix)
    n = len(prefix)
    assert tuple(a.degree(k) for k in range(1,n+1)) == tuple(b.degree(k) for k in range(1,n+1))
    assert a.scale_automorphism(p) and not b.scale_automorphism(p)
    return {'matching_prefix':prefix, 'prefix_product':a.D(n),
            'p_invertible_if_p_tail':True, 'p_invertible_if_r_tail':False,
            'source_law_equality_claimed':False}


def unbounded_filling_debt(stage: int, finite_budget: int) -> dict:
    """Abstract toy C_n={k>=n}: nonempty at every n, no global k.

    NOT a construction of the Alexander horned sphere; genuine geometric
    compactness/no-filling theorem is proved separately in the manuscript.
    """
    if type(stage) is not int or type(finite_budget) is not int or stage < 0 or finite_budget < 0:
        raise WildTowerError('nonnegative integers needed')
    return {'stage':stage,'witness_at_stage':stage,
            'bounded_witness_exists':stage<=finite_budget,
            'first_unfillable_stage_for_budget':finite_budget+1,
            'all_finite_stages_admit_some_unbounded_witness':True,
            'one_global_finite_witness_exists':False}


def pinched_tame_arc_inverse_lipschitz_bound(n: int) -> F:
    """EXACT toy lower bound, not an Alexander sphere construction.

    A tame polygonal U-arc sends source parameter endpoints at distance 1
    to (0,0) and (0,2^-n); hence any ambient inverse chart on a metric
    carrier extending the parameterization needs Lip >= 2^n.
    The general topological theorem in the dossier replaces this toy with
    Arzela-Ascoli and ambient homeomorphisms on compact S^3.
    """
    if type(n) is not int or n < 1:
        raise WildTowerError('positive geometric resolution index required')
    return F(2**n)
