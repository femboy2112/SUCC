"""Ordinal SUCC observer reports and the SECOND-ORDER Suzuki/Weil seam.

THIS MODULE DOES NOT EXECUTE AN INFINITE ORDINAL STAGE.

The mathematical observational diagram is

    O_2 --SUCC--> O_3 --SUCC--> ... --limit at omega--> O_omega
                         --formal report at omega+1--> Weil/Suzuki kernel

O_omega is a FILTERED COLIMIT of compatible prefixes, not a physical
observer returning after infinitely much elapsed time. Omega+1 names a
mathematical postprocessing operation, not a finite computational step.
For any bounded rational set of query times, arithmetic prime-event data
stabilize EXACTLY after a computable finite SUCC horizon. The archimedean
term is a separate, explicitly declared classical analytic model.

The correlation kernel K(t,u)=Psi(t)+Psi(u)-Psi(t-u) has
    d_t d_u K = Psi''(t-u) = Weil distribution
in the distributional sense (Masatoshi Suzuki, JLMS 2023).
A finite rectangle difference of K is an observed covariance-of-
increments PROBE, not a proof of nonnegative covariance.

That positivity (for all test functions) is RH-equivalent. Even
pointwise Psi>=0 and pointwise Psi''>=0 do NOT imply it.

Exact Fraction models give falsifiers independent of zeta zero data.
The finite source path can be supplied by an Engine journal;
unactualized future events must NOT be used as observations.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping


class OrdinalObservationError(ValueError):
    """A causal, finite resource, ordinal, or analytic boundary was violated."""


def _q(raw):
    if type(raw) is int or isinstance(raw, Fraction):
        return Fraction(raw)
    raise OrdinalObservationError("Ordinal query times and coefficients require exact rationals")


def _n(n, *, least=2, most=256):
    if type(n) is not int or not least <= n <= most:
        raise OrdinalObservationError(f"Stage must be an exact integer in [{least},{most}]")
    return n


def _query(q):
    t=_q(q)
    if abs(t)>5:
        raise OrdinalObservationError("Finite rational observer query limited to |t|<=5")
    return t


def _mp():
    try:
        import mpmath
    except ImportError as exc:
        raise OrdinalObservationError("mpmath required for archimedean response") from exc
    return mpmath


def _mpq(mp,q):
    z=_q(q)
    return mp.mpf(z.numerator)/z.denominator


def _ceil(q):
    v=_q(q)
    return -(-v.numerator//v.denominator)


def exact_bounded_time_horizon(times):
    """A proof-carrying WHOLE INTEGER ceiling for every named kernel query.

    For |t|<=M with rational M, exp(|t|)<=e^ceil(M)<3^ceil(M)
    when M>0. Consequently N=3^ceil(M) *certainly* contains ALL
    prime events needed at t, u and t-u. No floating exp/log
    threshold is consulted, so an event can never be lost to rounding.

    This is deliberately conservative and is NOT a bound on Gamma
    truncation: the classical archimedean term remains an explicitly
    modeled analytic response at each stage.
    """
    ts=tuple(_query(t) for t in times)
    if not ts:
        raise OrdinalObservationError("At least one finite rational observation time required")
    if len(ts)>10:
        raise OrdinalObservationError("Observation query budget exceeded (10)")
    M=max([abs(t) for t in ts]+[abs(t-u) for t in ts for u in ts])
    N=1 if M==0 else 3**_ceil(M)
    return {"rational_times":ts,
            "max_observable_log_displacement":M,
            "certified_source_SUCC_horizon":max(2,N),
            "derivation":"exp(M) < 3^ceil(M), proven from e<3",
            "archimedean_window_already_completed":True,
            "full_omega_stage_was_not_executed":True}


@dataclass(frozen=True)
class OrdinalFiniteStage:
    """SUCC observation stage n, preserving the complete coefficient prefix.

    Only n+1 is an accepted successor. A compatible family of these
    stages may have a mathematical colimit at omega; no finite instance
    pretends to represent O_omega.
    """
    n: int
    source: tuple[Fraction,...]
    head: str | None = None

    @classmethod
    def from_prefix(cls,source: Mapping[int,object],horizon,*,head=None):
        from .gamma_interferometer import GammaInterferometer,InterferometerError
        try:
            snapshot=GammaInterferometer.from_prefix(source,horizon,trace_head=head)
        except (InterferometerError,TypeError,ValueError) as exc:
            raise OrdinalObservationError("Requires complete actualized source prefix") from exc
        return cls(snapshot.horizon,snapshot.coefficients,snapshot.trace_head)

    @classmethod
    def from_engine(cls,engine,horizon=None):
        from .gamma_interferometer import GammaInterferometer,InterferometerError
        try:
            snap=GammaInterferometer.from_engine(engine,horizon)
        except (InterferometerError,TypeError,ValueError) as exc:
            raise OrdinalObservationError("Unactualized or incomplete source") from exc
        return cls(snap.horizon,snap.coefficients,snap.trace_head)

    @classmethod
    def genuine(cls,n):
        _n(n)
        return cls.from_prefix({k:1 for k in range(1,n+1)},n)

    def successor(self, coefficient, *, head=None):
        _n(self.n+1)
        v=_q(coefficient)
        return OrdinalFiniteStage(self.n+1,self.source+(v,),head)

    def restrict(self,smaller):
        _n(smaller,most=self.n)
        return OrdinalFiniteStage(smaller,self.source[:smaller+1],None)

    def agrees_with_earlier(self,older):
        if not isinstance(older,OrdinalFiniteStage):
            raise OrdinalObservationError("Compare only ordinal source snapshots")
        if older.n>self.n or self.source[:older.n+1]!=older.source:
            raise OrdinalObservationError("Finite observation histories are not compatible")
        return True

    def connected_pair_curvature(self,p,q):
        """Exact SECOND-ORDER arithmetic interaction between two prime probes.

        For distinct primes p,q, Dirichlet-log at n=pq gives
           b(pq)=a(pq)-a(p)a(q).
        This measures what the composite observation contributes BEYOND
        the two already observed primitive channels. It is NOT a
        covariance sign theorem, and it uses only data through pq.
        A fake a(6)=2 yields b(6)=1; genuine ζ yields 0.
        """
        from .arithmetic import factorization
        if type(p) is not int or type(q) is not int or p==q or min(p,q)<2:
            raise OrdinalObservationError("Require two distinct genuine prime labels")
        if factorization(p)!=((p,1),) or factorization(q)!=((q,1),):
            raise OrdinalObservationError("An independent probe requires primitive primes")
        if p*q>self.n:
            raise OrdinalObservationError("Composite correlation needs an actualized product event")
        observed=self.source[p*q]
        factorized=self.source[p]*self.source[q]
        residual=observed-factorized
        if self._gamma_snapshot().connected[p*q]!=residual:
            raise ArithmeticError("Local interaction differs from exact Dirichlet-log coefficient")
        return {
            "primes":(p,q),
            "composite_index":p*q,
            "observed":observed,
            "independent_prediction":factorized,
            "connected_second_order_residual":residual,
            "source_head":self.head,
            "scope":"arithmetic connected interaction; NOT full Weil covariance"
        }

    def semantic_log_partition_hessian(self,p,q):
        """Exact FINITE observer information geometry in prime-valuation features.

        Declare a model of observer belief, NOT an empirical brain theory:
          Z(theta_p,theta_q)=Σ_(n<=N) a(n)
               exp(theta_p v_p(n)+theta_q v_q(n)).
        At theta=0:
           Hessian(log Z)=Cov_pi(v_p,v_q), pi(n)=a(n)/Σa.
        Every nonnegative source therefore generates a PSD covariance,
        INCLUDING invalid fake a(6)=2. The geometry reads source
        changes but does NOT select Weil-positive arithmetic.
        """
        from .arithmetic import factorization
        if type(p) is not int or type(q) is not int or p==q or min(p,q)<2:
            raise OrdinalObservationError("Two distinct prime-valued semantic features required")
        if factorization(p)!=((p,1),) or factorization(q)!=((q,1),):
            raise OrdinalObservationError("Semantic valuation features must be prime generators")
        weights=self.source[1:]
        if any(v<0 for v in weights) or not sum(weights)>0:
            raise OrdinalObservationError(
                "A positive observer probability model cannot have negative weights")
        Z=sum(weights)
        def valuation(n,prime):
            k=0
            while n%prime==0:
                n//=prime
                k+=1
            return Fraction(k)
        labels=tuple(range(1,self.n+1))
        f=tuple(valuation(n,p) for n in labels)
        g=tuple(valuation(n,q) for n in labels)
        mean_f=sum((w*x for w,x in zip(weights,f)),Fraction())/Z
        mean_g=sum((w*y for w,y in zip(weights,g)),Fraction())/Z
        vff=sum((w*(x-mean_f)**2 for w,x in zip(weights,f)),Fraction())/Z
        vgg=sum((w*(y-mean_g)**2 for w,y in zip(weights,g)),Fraction())/Z
        vfg=sum((w*(x-mean_f)*(y-mean_g)
                 for w,x,y in zip(weights,f,g)),Fraction())/Z
        det=vff*vgg-vfg*vfg
        if min(vff,vgg,det)<0:
            raise ArithmeticError("A positive finite semantic measure lost its covariance PSD")
        return {
            "primes":(p,q),
            "partition_Z_at_zero":Z,
            "mean_prime_valuations":(mean_f,mean_g),
            "Hessian_log_Z":((vff,vfg),(vfg,vgg)),
            "determinant":det,
            "is_positive_semidefinite":True,
            "source_matches_zeta_prefix":all(v==1 for v in weights),
            "scope":"positive semantic observer information geometry, NOT identified with Weil"
        }

    def _gamma_snapshot(self):
        from .gamma_interferometer import GammaInterferometer
        return GammaInterferometer.from_prefix(
            {n:self.source[n] for n in range(1,self.n+1)},self.n,
            trace_head=self.head
        )

    def report(self,times,*,dps=60):
        """Omega+1-style report on a FINITE window, with explicit horizon.

        Only constructs an accessible finite restriction of the
        would-be omega+1 Weil/Suzuki report. Gamma's completed
        archimedean term is a separate classical analytic input.
        """
        w=exact_bounded_time_horizon(times)
        need=w["certified_source_SUCC_horizon"]
        if self.n<need:
            raise OrdinalObservationError(
                f"Observer stage {self.n} cannot read full prime wavefront requiring {need}")
        mp=_mp()
        with mp.workdps(dps):
            snap=self._gamma_snapshot()
            ts=w["rational_times"]
            psi={}
            for t in set(ts)|{t-u for t in ts for u in ts}|{Fraction(0)}:
                psi[t]=snap.at_time(abs(_mpq(mp,t)),dps=dps)["psi"]
            matrix=tuple(
                tuple(+(psi[t]+psi[u]-psi[t-u]) for u in ts)
                for t in ts
            )
            return {
                "ordinal_stage":"finite successor n",
                "formal_limit_stage":"omega = union/colimit of compatible records",
                "formal_report_stage":"omega+1 = mathematical postprocessing, NOT physical return",
                "finite_query_times":tuple(str(x) for x in ts),
                "source_horizon":self.n,
                "stabilization_horizon":need,
                "trace_head":self.head,
                "source_matches_zeta_prefix":snap.matches_zeta_prefix,
                "archimedean_term":"Suzuki exact classical Gamma+poles; not observed finite gamma cutoff",
                "kernel":matrix,
                "status":"FINITE_RESTRICTION_OF_ORDINAL_WEIL_REPORT_NOT_A_PSD_CERTIFICATE",
            }

    def rectangle_increment(self,t,u,h,k,*,dps=60):
        """Second mixed finite SUCC difference of the arithmetic report.

        Requires all four corners and their differences in actualized
        rational observation horizon. No positivity assumed.
        """
        t,u,h,k=map(_q,(t,u,h,k))
        if not h>0 or not k>0:
            raise OrdinalObservationError("Require positive finite difference increments")
        times=(t,t+h,u,u+k)
        grid=self.report(times,dps=dps)
        mat=grid["kernel"]
        # positions [t,t+h,u,u+k] with mixed finite difference
        return +(mat[1][3]-mat[1][2]-mat[0][3]+mat[0][2])


def quartic_observer_report():
    """Proof that nonnegative data and positive local second derivative
    fail to make the global observer's cross-correlation positive.

    Psi(t)=t^4, Psi''(t)=12t^2>=0.
    Times ±1: K = [[2,-14],[-14,2]], det=-192.
    Vector (1,1) has *negative* energy -24.
    All arithmetic here is exact Fraction.
    """
    f=lambda t: _q(t)**4
    k=lambda t,u: f(t)+f(u)-f(t-u)
    a,b=Fraction(1),Fraction(-1)
    m=((k(a,a),k(a,b)),(k(b,a),k(b,b)))
    return {
        "psi_at_1":f(a),"psi_second_derivative_at_1":Fraction(12),
        "kernel":m,"determinant":m[0][0]*m[1][1]-m[0][1]*m[1][0],
        "quadratic_vector_ones":sum(m[i][j] for i in range(2) for j in range(2)),
        "source":"counterexample to pointwise curvature implies correlation PSD",
    }


def exact_polynomial_rectangle(t,u,h,k):
    """Derive K_{quartic}'s mixed finite difference in TWO INDEPENDENT ways.

    Identity for any even Psi:
      Δ_t^h Δ_u^k K(t,u) =
         Psi(t+h-u)+Psi(t-u-k)-Psi(t+h-u-k)-Psi(t-u).
    This is the exact second-order observed-interaction probe, and
    equals hk Psi''(t-u)+O(hk(h+k)) when smooth.
    """
    t,u,h,k=map(_q,(t,u,h,k))
    if h<=0 or k<=0:
        raise OrdinalObservationError("Finite differences require positive h and k")
    psi=lambda z:z**4
    K=lambda x,y:psi(x)+psi(y)-psi(x-y)
    corners=K(t+h,u+k)-K(t+h,u)-K(t,u+k)+K(t,u)
    relative=psi(t+h-u)+psi(t-u-k)-psi(t+h-u-k)-psi(t-u)
    assert corners==relative
    return {"corners":corners,"relative":relative,
            "local_second_derivative":12*(t-u)**2,
            "normalized":corners/(h*k)}


def oscillator_observer_report(times,*,dps=65):
    """Positive observable trajectory Psi(t)=1-cos(t) explicitly in R².

    phi(t)=(cos t-1,sin t);
    K(t,u)=phi(t)·phi(u)=Psi(t)+Psi(u)-Psi(t-u).
    Psi''(t-u)=cos(t-u), which can be NEGATIVE pointwise despite
    a PSD stationary covariance kernel.
    """
    ts=tuple(_q(t) for t in times)
    if not ts or len(ts)>12:
        raise OrdinalObservationError("1..12 rational observation times expected")
    mp=_mp()
    with mp.workdps(dps):
        vectors=[(mp.cos(_mpq(mp,t))-1,mp.sin(_mpq(mp,t))) for t in ts]
        K=tuple(tuple(+(v[0]*w[0]+v[1]*w[1]) for w in vectors)
                for v in vectors)
        psi=lambda t:1-mp.cos(t)
        independent=tuple(
            tuple(+(psi(_mpq(mp,t))+psi(_mpq(mp,u))
                     -psi(_mpq(mp,t-u))) for u in ts)
            for t in ts)
        discrepancy=max(abs(K[i][j]-independent[i][j])
                        for i in range(len(ts)) for j in range(len(ts)))
        return {"kernel":K,"independent_k":independent,
                "identity_error":+discrepancy,
                "negative_pointwise_curvature_allowed":True,
                "source":"exact 2-dimensional positive feature embedding, NOT zeta"}


def synthetic_ordinal_semantics(horizon):
    """A FINITE demonstrator of the formal omega -> omega+1 distinction.

    Each stage n gives one additional observation; the
    mathematical union O_omega can be specified intensionally
    without computing the infinite run. Its K report is a
    separate universal predicate over finite test families.
    """
    _n(horizon)
    return {
        "finite_stage_count_observed":horizon,
        "last_physical_SUCC_stage":horizon,
        "omega":"limit ordinal, not a largest finite stage",
        "omega_plus_one":"successor of FORMALLY completed history, not an executable finish line",
        "completed_source_identity":"infinite compatible coefficient diagram",
        "report_property":"for all finite test sets, Suzuki K has nonnegative Gram",
        "report_property_is_RH_equivalent":True,
        "report_property_proved":False,
        "omega_computation_executed":False,
    }



def harmonic_number(n):
    """Exact finite sum H_N=Σ_(k=1)^N 1/k, a rational SUCC history."""
    if type(n) is not int or not 1<=n<=4096:
        raise OrdinalObservationError("Harmonic observational horizon must be 1..4096")
    return sum((Fraction(1,k) for k in range(1,n+1)),Fraction())


def harmonic_half_density_observer(n,local_horizon):
    """A concrete quantum-Hilbert OBSERVER whose normal state has no ω-vector limit.

    Let s=1/2+it and H_N=Σ_(k<=N)1/k. In H_N=span(e_1,...,e_N):
      |Omega_N(s)> = H_N^(-1/2) Σ_(k<=N) k^(-s)|k>.
    Its norm is exactly 1, independent of t.
    For fixed M<=N, <Omega_N|P_M|Omega_N> = H_M/H_N -> 0
    because H_N diverges. Each finite state is valid but there is no
    normalized STRONG limit vector in ℓ²: it converges WEAKLY to 0.
    The expectation of I remains 1. (Limits DO NOT commute.)

    This exact model is NOT a factual theory of a human brain and is
    completely source-inert: it proves no Weil sign or RH assertion.
    """
    if type(n) is not int or not 2<=n<=4096:
        raise OrdinalObservationError("Finite Hilbert observer stage must be 2..4096")
    if type(local_horizon) is not int or not 1<=local_horizon<=n:
        raise OrdinalObservationError("Fixed finite local projector horizon must be <= stage")
    hn=harmonic_number(n)
    hm=harmonic_number(local_horizon)
    return {
        "stage":n,"local_probe_M":local_horizon,
        "harmonic_source_normalization":hn,
        "local_harmonic_mass":hm,
        "finite_projector_expectation":hm/hn,
        "identity_expectation":Fraction(1),
        "finite_vector_norm_squared":Fraction(1),
        "phase_independent_local_expectations":True,
        "infinite_vector_summable":False,
        "theorem":"weak limit zero; no nonzero normalized strong omega-limit vector",
        "Weil_identification_proved":False,
    }


def harmonic_dyadic_divergence_certificate(k):
    """Exact dyadic proof H_(2^k)>=1+k/2 -> infinity.

    Group integers into (2^(j-1),2^j] for 1<=j<=k.
    Each block contains 2^(j-1) numbers, all <=2^j,
    so its reciprocal sum >=1/2. The statement applies
    to all k; this implementation checks one exact finite stage.
    """
    if type(k) is not int or not 0<=k<=12:
        raise OrdinalObservationError("Dyadic witness index must be 0..12")
    n=2**k
    mass=harmonic_number(n)
    lower=Fraction(1)+Fraction(k,2)
    assert mass>=lower
    return {
        "k":k,"stage_N":n,
        "exact_H_N":mass,
        "provable_lower_bound":lower,
        "bound_diverges_as_k_grows":True,
        "physical_infinite_time_executed":False,
    }


def mellin_hilbert_threshold(sigma):
    """Norm convergence criterion for naive arithmetic Hilbert amplitude.

    |Phi_s> = Σ_(n>=1) n^(-s)|n>, with s=sigma+i*t.
    Norm²=Σ n^(-2sigma)=ζ(2sigma), converging EXACTLY when
    sigma>1/2; at sigma=1/2 logarithmic harmonic divergence.

    This normalizability line coincides with RH's symmetry line
    but it is an elementary p-series statement and NEVER
    establishes a Weil-positive form or zero locations.
    """
    q=_q(sigma)
    return {
        "real_part":q,
        "sum_of_squared_amplitudes_finite":q>Fraction(1,2),
        "is_critical_harmonic_boundary":q==Fraction(1,2),
        "critical_line_normalization":"sum(n^-1) diverges",
        "scope":"elementary Hilbert p-series threshold, RH-INERT"
    }
