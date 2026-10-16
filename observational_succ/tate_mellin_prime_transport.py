"""Source-labelled Gamma x prime-FUCC Mellin transport (RH NOT proved).

Two proven approximation charts use one declared Gaussian Tate target:
  (a) finite Beta/exponential clocks (same probabilistic source coordinates),
  (b) normalized, finite, positive logarithmic Dirac quadrature.
The arithmetic source consists only of authentic prime valuations.  On
Re(s)=2(n+1)>1 the completed factor Gamma_R(s) zeta(s) is a positive Mellin
transform; this *cannot* be promoted to the signed Weil form.

All reported *analytic bounds* are Fraction-valued and derived from rational
inequalities, not evaluations of Gamma, zeta, pi, or their unknown zeros.
Numerical readouts (mpmath) are separate, non-certified diagnostics.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial

from .factorial_gamma_fucc import finite_exponential_clock_band_certificate


class TateMellinSourceError(ValueError):
    """Invalid source/provenance, unsupported chart or uncertified budget."""


def _int(x, name, low, high):
    if type(x) is not int or not low <= x <= high:
        raise TateMellinSourceError(f"{name} requires an integer in {low}..{high}")
    return x


def _rat(x, name, *, positive=False, nonnegative=False):
    if type(x) not in (int, F):
        raise TateMellinSourceError(f"{name} must be an exact integer/Fraction")
    v = F(x)
    if (positive and v <= 0) or (nonnegative and v < 0):
        raise TateMellinSourceError(f"{name} outside admissible sign/domain")
    return v


def primes_upto(bound: int):
    _int(bound, "prime horizon", 2, 3000)
    sieve = bytearray([1]) * (bound + 1)
    sieve[0:2] = b"\x00\x00"
    for k in range(2, int(bound**0.5) + 1):
        if sieve[k]:
            sieve[k*k:bound+1:k] = b"\x00" * ((bound-k*k)//k+1)
    return tuple(k for k in range(2, bound+1) if sieve[k])


def exp_taylor_lower(x, terms=16):
    """Exact rational P_terms(x) <= exp(x) for x>=0."""
    x = _rat(x, "positive exponential argument", nonnegative=True)
    _int(terms, "Taylor order", 1, 40)
    return sum((x**j / factorial(j) for j in range(terms+1)), F(0))


def dirac_probability_band_certificate(n, mesh, left, right, height,
                                       *, taylor_order=16):
    """Exact-rational absolute-error bound for finite positive log-clock.

    g_a(u)=exp(a*u-exp(u)), a=n+1, C=int(g_a)=n!.
    Finite source: P(J=j) proportional to g_a(jd), left<=j<=right.
    Its characteristic function, after the deterministic -log pi shift,
    approximates Gamma_R(2a+2it)/Gamma_R(2a) for |t|<=T.

    Quadrature: |d sum_Z g_a(jd)e^(itjd) - Gamma(a+it)|
       <= d (2a+|t|) Gamma(a).
    Left tail: <= exp(a Ld)/a <= 1/(a P_N(-a Ld)).
    Right tail: <= n! 2^a exp(-exp(Rd)/2), valid Rd>=a-1.
       Use exp(Rd) >= P_N(Rd) and exp(x) >= P_N(x).
    Normalize by finite DC: (d(4a+T)+2delta)/(1-2ad-delta).
    No floating-point assumption is involved in these inequalities.
    """
    _int(n, "factorial anchor", 0, 12)
    d = _rat(mesh, "positive Dirac mesh", positive=True)
    T = _rat(height, "spectral half-band", nonnegative=True)
    _int(left, "negative source boundary", -60000, -1)
    _int(right, "positive source boundary", 1, 60000)
    if left >= right or right-left > 50000:
        raise TateMellinSourceError("finite source clock budget exceeded")
    _int(taylor_order, "Taylor order", 2, 36)
    a = n+1
    if right*d < a-1:
        raise TateMellinSourceError("right-side g_a must be decreasing")

    left_rel = 1/(F(factorial(a))*exp_taylor_lower(-a*left*d,taylor_order))
    inside = exp_taylor_lower(right*d,taylor_order)/2
    right_rel = F(2**a)/exp_taylor_lower(inside,taylor_order)
    delta = left_rel + right_rel
    zero_error_relative = 2*a*d + delta
    if zero_error_relative >= 1:
        raise TateMellinSourceError("not enough retained source for a certified DC denominator")
    err = (d*(4*a+T) + 2*delta)/(1-zero_error_relative)
    return {
        "n": n,"sigma":2*a,"mesh":d,"left":left,"right":right,
        "source_event_count": right-left+1,"spectral_half_band":T,
        "left_tail_over_gamma_upper":left_rel,
        "right_tail_over_gamma_upper":right_rel,
        "combined_relative_tail_upper":delta,
        "lower_normalization_relative_to_n_factorial":1-zero_error_relative,
        "uniform_normalized_gamma_error_upper":err,
        "numerically_evaluated_source_weights_certified":False,
        "mathematical_exact_finite_source_bound":True,
        "probability_source":"normalized Gaussian log lattice; deterministic -log(pi) phase",
        "RH_proved":False,
    }


def prime_euler_certificate(cutoff: int, max_exponent: int, sigma: int):
    """Exact rational uniform characteristic-function Euler truncation.

    At integer sigma>1, independent K_p~Geom(q_p=p^-sigma).
    Finite source K_p conditioned to 0..K has weights proportional q_p^k.
    TV coupling error per p = q_p^(K+1), omitted-prime TV <=
    sum_(m>P) m^-sigma <= P^(1-sigma)/(sigma-1).
    Spectral error <=2 times the total probability of a coupling mismatch.
    """
    _int(cutoff, "prime cutoff", 2, 3000)
    _int(max_exponent, "prime-power cutoff", 0, 16)
    _int(sigma, "absolute-convergence abscissa", 2, 30)
    ps = primes_upto(cutoff)
    local = 2*sum((F(1,p**(sigma*(max_exponent+1))) for p in ps),F())
    tail = F(2, (sigma-1)*cutoff**(sigma-1))
    return {
        "cutoff":cutoff,"max_exponent":max_exponent,"sigma":sigma,
        "prime_labels":ps,"prime_count":len(ps),
        "finite_prime_power_truncation_upper":local,
        "omitted_prime_tail_upper":tail,
        "uniform_euler_characteristic_error_upper":local+tail,
        "weights_are_positive":True,
        "source_family":"authentic primes only, independent geometric valuation clocks",
        "zero_positions_are_inputs":False,"RH_proved":False,
    }


def completed_mellin_band_certificate(n, mesh, left, right, height,
                                      prime_cutoff, prime_power_cutoff,
                                      beta_cutoff, *,taylor_order=16):
    """Certified uniform approximation to Lambda(2a+2it)/Lambda(2a).

    Lambda(s)=Gamma_R(s) zeta(s), sigma=2a>=2, |t|<=T.
    Real place: independent finite Beta/Exp chart and finite Dirac chart.
    Finite-prime source: authentic truncated geometric valuations.
    Product of finite *positive* Fourier sources is positive definite.
    Each chart bound and triangle bound are rational and universal on band.
    Nothing is proved for Re(s)<=1 or for signed Weil positivity.
    """
    dirac=dirac_probability_band_certificate(n,mesh,left,right,height,
                                              taylor_order=taylor_order)
    beta=finite_exponential_clock_band_certificate(n,beta_cutoff,
                                                   _rat(height,"spectral band",nonnegative=True))
    euler=prime_euler_certificate(prime_cutoff,prime_power_cutoff,2*(n+1))
    bd=dirac["uniform_normalized_gamma_error_upper"]
    bb=beta["uniform_absolute_error_upper"]
    be=euler["uniform_euler_characteristic_error_upper"]
    return {
        "n":n,"sigma":2*(n+1),"height":F(height),
        "dirac_gamma_error":bd,"beta_gamma_error":bb,
        "euler_prime_error":be,
        "dirac_vs_beta_uniform_error_upper":bd+bb,
        "completed_dirac_error_upper":bd+be,
        "completed_beta_error_upper":bb+be,
        "prime_power_mutation_controls_required":True,
        "completed_object":"Gamma_R(s) zeta(s), normalized at sigma>1, not xi or Weil",
        "finite_probabilistic_sources":True,
        "fourier_gram_psd_only_for_positive_source":True,
        "signed_Weil_sign_identified":False,"RH_proved":False,
    }


def finite_prime_coefficients(cutoff:int,max_exponent:int,
                               *,fake_six=False,wrong_two=False):
    """Finite Dirichlet convolution; returns exact labels for hostile mutants.

    For the authentic finite prime source each generated n has coefficient 1,
    because prime-power factorization is unique. The fake base 6 duplicates
    the coefficient at 6 (2*3=6), a source-mutation detector.
    The wrong-two factor uses alpha_2=3/2 instead of 1, remaining positive.
    Mutation mode intentionally never authenticates itself as Euler prime data.
    """
    _int(cutoff,"coefficient prime horizon",3,97)
    _int(max_exponent,"coefficient prime power depth",1,6)
    if type(fake_six) is not bool or type(wrong_two) is not bool:
        raise TateMellinSourceError("explicit Boolean source mutations required")
    labels=list(primes_upto(cutoff))
    if fake_six:
        labels.append(6)
    if (max_exponent+1)**len(labels)>200000:
        raise TateMellinSourceError("unbounded Dirichlet coefficient box: resource budget exceeded")
    out={1:F(1)}
    for base in labels:
        alpha=F(3,2) if (wrong_two and base==2) else F(1)
        next_out={}
        for n,weight in out.items():
            for k in range(max_exponent+1):
                address=n*base**k
                next_out[address]=next_out.get(address,F(0))+weight*alpha**k
        out=next_out
    if not fake_six and not wrong_two and any(v!=1 for v in out.values()):
        raise AssertionError("fundamental theorem of arithmetic violated")
    return {
        "coefficients":out,
        "authentic_prime_labels": not fake_six and not wrong_two,
        "source_mutations":tuple(name for name,yes in
                    (("fake_composite_6",fake_six),("alpha_2=3/2",wrong_two)) if yes),
        "positive_coefficients": all(v>0 for v in out.values()),
        "no_claim_of_Weil_positivity":True,
    }


def mutant_source_discriminator(cutoff=3,max_exponent=2):
    true=finite_prime_coefficients(cutoff,max_exponent)["coefficients"]
    fake=finite_prime_coefficients(cutoff,max_exponent,fake_six=True)["coefficients"]
    wrong=finite_prime_coefficients(cutoff,max_exponent,wrong_two=True)["coefficients"]
    def first_diff(other):
        return next((n for n in sorted(set(true)|set(other))
                     if true.get(n,F(0)) != other.get(n,F(0))),None)
    return {
        "fake_six_first_difference":first_diff(fake),
        "fake_six_true_coefficient_at_6":true.get(6,F(0)),
        "fake_six_mutant_coefficient_at_6":fake.get(6,F(0)),
        "changed_two_first_difference":first_diff(wrong),
        "changed_two_mutant_coefficient_at_2":wrong.get(2,F(0)),
        "fake_sources_still_positive":all(v>0 for v in fake.values()) and
                                        all(v>0 for v in wrong.values()),
        "positivity_does_not_authenticate_Euler":True,
    }


def prime_escape_certificate(cutoff:int,threshold:int):
    """Rational *upper bounds* on mass below threshold for 0<sigma<=1.

    A product N_P cannot be <=X if any prime p>X has K_p>=1.
    For authentic untruncated geometric clocks, P(K_p=0)=1-p^-sigma
        <=1-1/p for 0<sigma<=1.
    For truncated K>=1, P(K_p=0)<=p/(p+1) for same sigma range.
    Thus these rational products bound P(N_P<=X) for ALL 0<sigma<=1.
    Since sum_p 1/p diverges, both bounds ->0 for fixed X, P->inf.
    No tight limiting positive Euler measure exists on finite log addresses.
    """
    _int(cutoff,"prime escape horizon",2,3000)
    _int(threshold,"finite integer observation threshold",1,cutoff)
    ps=tuple(p for p in primes_upto(cutoff) if p>threshold)
    untruncated=F(1)
    positive_finite=F(1)
    for p in ps:
        untruncated *= F(p-1,p)
        positive_finite *= F(p,p+1)
    return {
        "cutoff":cutoff,"integer_threshold":threshold,
        "tested_primes":len(ps),
        "all_sigma_in_open_0_to_1_untruncated_mass_upper":untruncated,
        "all_sigma_in_open_0_to_1_finite_geometric_mass_upper":positive_finite,
        "global_escape_as_cutoff_grows":"classical divergence of sum_p(1/p)",
        "weak_limit_probability_on_finite_log_carrier":False,
        "observer_boundary":"positive-Euler-probability representation only",
        "RH_undecidable_or_impossible":False,
    }


def archimedean_parity_and_pole_firewall(n=0):
    """Exact shape/moment and xi-pole-factor negative-control diagnostics.

    Normalized Gamma_R(s) at s0=2n+2 has pi*E[x^2]=n+1.
    Odd real test |x|e^-pi*x² changes to Gamma_R(s+1), so
    pi*E[x²]=n+3/2. Changing pi to 2pi halves pi*E[x²].
    Pole-removal scalar P(s)=s(s-1)/2 normalized at s0=2:
    |P(2+2i)/P(2)|^2 = 10 >1, so the scalar multiplier is NOT
    a characteristic function by itself. This does not diagnose full xi.
    """
    _int(n,"Tate parity anchor",0,25)
    return {
        "even_pi_scaled_second_moment":F(n+1),
        "odd_pi_scaled_second_moment":F(2*n+3,2),
        "wrong_2pi_scaled_second_moment":F(n+1,2),
        "xi_scalar_pole_removal_at_sigma2_t1_modulus_squared":F(10),
        "xi_scalar_is_itself_positive_characteristic":False,
        "therefore_completed_xi_is_not_positive_characteristic":"NOT_ESTABLISHED",
        "signed_completed_Weil_not_constructed":True,
        "RH_proved":False,
    }


def _mp():
    try:
        import mpmath as mp
    except ImportError as e:
        raise TateMellinSourceError("mpmath required for numerical readout only") from e
    return mp


def _mpfrac(mp,q):
    z=F(q)
    return mp.mpf(z.numerator)/z.denominator


def finite_completed_characteristic(n, t, *, chart="beta", cutoff=500,
                                    mesh=F(1,150),left=-1000,right=1000,
                                    prime_cutoff=47,max_exponent=5,dps=65):
    """Evaluate declared finite positive source; NUMERICAL, not interval certified.

    Each term is constructed from either (a) finite independent exponentials
    / Beta(k,1) with the SAME finite source law, or (b) independent positive
    Dirac lattice samples.  Arithmetic valuations are genuine primes only.
    Gamma and zeta oracles are NOT inputs to the finite source construction.
    """
    _int(n,"shape anchor",0,12)
    _int(dps,"decimal precision",30,150)
    _int(prime_cutoff,"prime cutoff",2,3000)
    _int(max_exponent,"prime-power depth",0,16)
    mp=_mp()
    with mp.workdps(dps):
        t=mp.mpf(t)
        if chart=="beta":
            _int(cutoff,"Beta product cutoff",n+1,5000)
            phi=mp.exp(1j*t*mp.log(cutoff)-
                       mp.fsum(mp.log(1+1j*t/k) for k in range(n+1,cutoff+1)))
        elif chart=="dirac":
            d=F(mesh)
            _rat(d,"positive Dirac mesh",positive=True)
            _int(left,"finite lattice L",-60000,-1)
            _int(right,"finite lattice R",1,60000)
            if right-left>50000:
                raise TateMellinSourceError("finite lattice resource budget exceeded")
            dd=_mpfrac(mp,d)
            a=n+1
            weights=[mp.exp(a*j*dd-mp.exp(j*dd)) for j in range(left,right+1)]
            phi=mp.fsum(weights[j-left]*mp.exp(1j*t*j*dd)
                        for j in range(left,right+1))/mp.fsum(weights)
        else:
            raise TateMellinSourceError("chart must be 'beta' or 'dirac'")
        real_factor=mp.exp(-1j*t*mp.log(mp.pi))*phi
        sigma=2*(n+1)
        euler=mp.mpc(1)
        for p in primes_upto(prime_cutoff):
            terms=[mp.power(p,-sigma*k)*mp.exp(-2j*t*k*mp.log(p))
                   for k in range(max_exponent+1)]
            weights=mp.fsum(mp.power(p,-sigma*k)
                            for k in range(max_exponent+1))
            euler*=mp.fsum(terms)/weights
        return +(real_factor*euler)


def completed_characteristic_oracle(n,t,*,dps=75):
    """Analytic independent oracle used ONLY at Re(s)>1, no zero lookup."""
    _int(n,"shape anchor",0,12)
    _int(dps,"decimal precision",30,150)
    mp=_mp()
    with mp.workdps(dps):
        tt=mp.mpf(t)
        sigma=2*(n+1)
        s=sigma+2j*tt
        return +(mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)
                /(mp.power(mp.pi,-sigma/2)*mp.gamma(sigma/2)*mp.zeta(sigma)))


def finite_prime_jet_cumulants(prime_cutoff:int, sigma:int, jet_depth:int):
    """Exact q-rational labels behind logarithmic FUCC/prime-power jets.

    For q=p^-sigma, -d_s log(1-p^-s)^(-1) =
       (log p) q/(1-q) = (log p) sum_(k>=1) q^k.
    The variance of geometric K_p is q/(1-q)^2; the second log
    cumulant multiplies (log p)^2. All q coefficients are rational.
    The finite omitted jet mass after depth K is q^(K+1)/(1-q).
    Not a signed completed Weil distribution; sigma>1 only.
    """
    _int(prime_cutoff,"prime cumulant cutoff",2,3000)
    _int(sigma,"positive Euler convergence abscissa",2,30)
    _int(jet_depth,"prime jet truncation depth",1,30)
    rows=[]
    for p in primes_upto(prime_cutoff):
        q=F(1,p**sigma)
        first=q/(1-q)
        finite=sum((q**k for k in range(1,jet_depth+1)),F())
        tail=q**(jet_depth+1)/(1-q)
        second=q/(1-q)**2
        if first != finite+tail:
            raise ArithmeticError("prime FUCC jet exact-series identity failed")
        rows.append({"prime":p,"coefficient_of_log_prime":first,
                     "coefficient_of_log_prime_squared_in_variance":second,
                     "finite_prime_power_weights":tuple(q**k for k in range(1,jet_depth+1)),
                     "truncated_log_prime_tail":tail})
    return {"sigma":sigma,"prime_cutoff":prime_cutoff,"jet_depth":jet_depth,
            "rows":tuple(rows),
            "logarithmic_generator":"-E'_P(s)/E_P(s) = sum_(p,k) log(p)*p^(-k*s)",
            "source_label":"authentic p^k=FUCC valuation jets; exact rational coefficients",
            "does_not_supply_Weil_sign":True}


def compact_weil_prime_jet_source(max_integer:int):
    """Exact finite carrier of genuine half-density prime-power impulses.

    The source distribution acts on compact log-support tests:
      sum_{p^k<=N} log(p)/sqrt(p^k) * f(k*log(p)), N=floor(exp(L)).
    We store weights SYMBOLICALLY, never use approximate log/sqrt values
    as exact certificates. Full Weil includes gamma, pole, contact, signs.
    """
    _int(max_integer,"compact prime-power address cutoff",2,200000)
    if max_integer>3000:
        raise TateMellinSourceError("raise certified prime sieve budget first")
    out=[]
    for p in primes_upto(max_integer):
        k=1
        power=p
        while power<=max_integer:
            out.append((power,p,k))
            k+=1
            power*=p
    out.sort()
    return {
        "max_integer":max_integer,
        "prime_power_impulses":tuple({"n":m,"prime":p,"exponent":k,
            "half_density_weight":f"log({p})/sqrt({m})",
            "log_address":f"{k}*log({p})"} for m,p,k in out),
        "count":len(out),"fake_composite_six_present":False,
        "zero_ordinate_input":False,
        "full_signed_Weil_form_obtained":False,
    }


def finite_hyperbolic_succ_fucc_certificate(horizon:int, sigma:int):
    """Exact finite N-prefix <-> valuation-vector carrier isomorphism.

    H_N(s)=sum_{1<=n<=H}n^-s equals the sum over ALL prime valuation
    vectors alpha with prod p^alpha<=H, via unique factorization.
    Rectangular p<=P, k<=K and hyperbolic product<=H are different
    admissible finite source domains. No exponential-size grid is assumed.
    """
    _int(horizon,"finite SUCC natural horizon",2,1200)
    _int(sigma,"exact Dirichlet weight abscissa",2,12)
    ps=primes_upto(horizon)
    address_to_vector={}
    vector_to_address={}
    normalizer=F(0)
    for n in range(1,horizon+1):
        remaining=n
        vec=[]
        for p in ps:
            if p*p>remaining:
                break
            if remaining%p:
                continue
            k=0
            while remaining%p==0:
                remaining//=p
                k+=1
            vec.append((p,k))
        if remaining>1:
            vec.append((remaining,1))
        vec=tuple(vec)
        product=1
        for p,k in vec:
            product*=p**k
        if product !=n or vec in vector_to_address:
            raise ArithmeticError("SUCC<->prime valuation bijection failed")
        address_to_vector[n]=vec
        vector_to_address[vec]=n
        normalizer+=F(1,n**sigma)
    if len(vector_to_address)!=horizon:
        raise ArithmeticError("unexpected hyperbolic valuation carrier size")
    # Every valuation vector in the declared hyperbolic cone is represented,
    # since its product is a natural number <= horizon. Surjectivity is formal.
    return {
        "horizon":horizon,"sigma":sigma,
        "natural_address_count":len(address_to_vector),
        "unique_valuation_vector_count":len(vector_to_address),
        "SUCC_Dirichlet_partition_exact":normalizer,
        "FUCC_hyperbolic_partition_exact":normalizer,
        "all_prime_factors_authentic":True,
        "natural_address_6":address_to_vector.get(6),
        "natural_address_horizon":address_to_vector[horizon],
        "no_box_cutoff_conflation":True,
        "zero_position_input":False,
    }


def natural_succ_dirichlet_band_certificate(horizon:int,sigma:int):
    """Independent finite-natural-prefix Dirichlet characteristic bound.

    D_H(s)=sum_{n<=H}n^-s, A_H=D_H(sigma)>0. For Re(s)=sigma>1,
    omitted absolute tail <= H^(1-sigma)/(sigma-1), giving
    sup_t |D_H(s)/A_H-zeta(s)/zeta(sigma)| <=2*tail/A_H.
    All quantities in the upper bound are rational.
    """
    c=finite_hyperbolic_succ_fucc_certificate(horizon,sigma)
    normalizer=c["SUCC_Dirichlet_partition_exact"]
    tail=F(1,(sigma-1)*horizon**(sigma-1))
    return {
        "horizon":horizon,"sigma":sigma,
        "normalizer":normalizer,
        "omitted_integer_tail_upper":tail,
        "uniform_arithmetic_characteristic_error_upper":2*tail/normalizer,
        "exact_finite_hyperbolic_FUCC_equals_SUCC":True,
        "positive_natural_zeta_source":True,
        "RH_proved":False,
    }


def euler_vs_succ_carrier_certificate(horizon:int, sigma:int,
                                      prime_cutoff:int,max_exponent:int):
    """Proved uniform discrepancy bound for two differently truncated
    authentic source representations of the SAME Euler-zeta law.
    """
    c=natural_succ_dirichlet_band_certificate(horizon,sigma)
    e=prime_euler_certificate(prime_cutoff,max_exponent,sigma)
    return {
        "natural_horizon":horizon,"prime_cutoff":prime_cutoff,
        "max_exponent":max_exponent,"sigma":sigma,
        "uniform_zeta_source_discrepancy_upper":
             c["uniform_arithmetic_characteristic_error_upper"]+
             e["uniform_euler_characteristic_error_upper"],
        "hyperbolic_cutoff_equals_rectangular_cutoff":False,
        "independent_finite_source_decomposition_check":True,
        "zero_ordinate_input":False,
    }


def natural_succ_characteristic(horizon:int,sigma:int,t,*,dps=65):
    """Numerical finite SUCC-prefix oracle; not interval-arithmetic proof."""
    _int(horizon,"natural SUCC prefix",2,1200)
    _int(sigma,"positive zeta domain",2,12)
    _int(dps,"numeric precision",30,150)
    mp=_mp()
    with mp.workdps(dps):
        t=mp.mpf(t)
        s=sigma+2j*t
        return +(mp.fsum(mp.power(n,-s) for n in range(1,horizon+1))/
                 mp.fsum(mp.power(n,-sigma) for n in range(1,horizon+1)))


def finite_euler_characteristic(prime_cutoff:int,max_exponent:int,
                                 sigma:int,t,*,dps=65):
    """Numerical authentic finite-prime-jet oracle, no global zeta call."""
    _int(prime_cutoff,"prime cutoff",2,3000)
    _int(max_exponent,"prime-power depth",0,16)
    _int(sigma,"abscissa",2,30)
    _int(dps,"numerical precision",30,150)
    mp=_mp()
    with mp.workdps(dps):
        t=mp.mpf(t)
        out=mp.mpc(1)
        for p in primes_upto(prime_cutoff):
            top=mp.fsum(mp.power(p,-(sigma+2j*t)*k)
                        for k in range(max_exponent+1))
            bottom=mp.fsum(mp.power(p,-sigma*k)
                           for k in range(max_exponent+1))
            out*=top/bottom
        return +out


def finite_hyperbolic_prime_coupling(horizon:int,sigma:int,p:int,q:int):
    """Exact SUCC-window-induced correlation of prime FUCC activation.

    Source N|N<=H has weight n^-sigma / sum_(m<=H)m^-sigma.
    At infinite N under sigma>1, distinct prime activation events are
    independent. A finite hyperbolic SUCC horizon couples them, and the
    covariance differs from zero by at most 3*tail/A_H. This follows
    from total-variation conditioning and 0<=probabilities<=1.
    """
    c=natural_succ_dirichlet_band_certificate(horizon,sigma)
    _int(p,"prime activation label p",2,97)
    _int(q,"prime activation label q",2,97)
    if p==q or p not in primes_upto(p) or q not in primes_upto(q):
        raise TateMellinSourceError("require two DISTINCT genuine prime labels")
    normal=c["normalizer"]
    def mass(divisor):
        return sum((F(1,n**sigma) for n in range(1,horizon+1)
                    if n%divisor==0),F())/normal
    pa,pb,pab=mass(p),mass(q),mass(p*q)
    cov=pab-pa*pb
    tv_bound=c["omitted_integer_tail_upper"]/normal
    if abs(cov)>3*tv_bound:
        raise AssertionError("finite conditioned prime covariance bound failed")
    return {
        "SUCC_horizon":horizon,"sigma":sigma,"prime_p":p,"prime_q":q,
        "p_active_probability":pa,"q_active_probability":pb,
        "joint_active_probability":pab,
        "finite_SUCC_coupling_covariance":cov,
        "absolute_covariance_upper":3*tv_bound,
        "infinite_genuine_zeta_law_covariance":F(0),
        "independence_requires_full_positive_zeta_law":True,
        "source_label":"finite SUCC hyperbolic prefix vs FUCC prime events",
    }


def finite_mellin_gram_transport_certificate(frequencies:tuple,
                                            chart_error,
                                            certified_half_band):
    """Exact spectral-norm error on a declared finite positive Mellin basis.

    Entries K_ij=E exp(i*(t_i-t_j)*W); source Gram is PSD, since
    K=E vv*. If |psi_chart(t)-psi_target(t)|<=eps on |t|<=T,
    pairwise differences inside band give |Delta K_ij|<=eps and
    ||Delta K||_op<=||Delta K||_F<=r*eps. This *never* certifies a
    signed Weil/Suzuki Gram identification.
    """
    if type(frequencies) is not tuple:
        raise TateMellinSourceError("frequency basis must be an ordered tuple")
    if not 1 <= len(frequencies) <= 20:
        raise TateMellinSourceError("frequency basis dimension out of budget")
    tt=tuple(_rat(t,"finite Mellin frequency") for t in frequencies)
    eps=_rat(chart_error,"analytic certified error",nonnegative=True)
    band=_rat(certified_half_band,"certified band",nonnegative=True)
    if any(abs(x-y)>band for x in tt for y in tt):
        raise TateMellinSourceError("test basis exceeds proved difference band")
    return {
        "frequencies":tt,"dimension":len(tt),
        "source_gram_kernel":"K_ij = E exp(i*(t_i-t_j)*W)",
        "operator_error_upper":len(tt)*eps,
        "finite_source_gram_positive_semidefinite":True,
        "target_gram_positive_semidefinite_for_sigma_gt_one":True,
        "completed_signed_Weil_gram_identified":False,
        "RH_proved":False,
    }
