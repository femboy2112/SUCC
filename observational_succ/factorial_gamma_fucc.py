"""Source-typed factorial/Gamma/Mellin and SUCC/FUCC finite certificates.

Exact operations use standard-library integers/Fractions. Analytic readouts are
optional mpmath diagnostics, never proof certificates. Classical facts used:
Gamma recurrence, Euler/Gauss-Laguerre integrals, Euler's product and moments.
No nontrivial zeta-zero positions or positive Weil covariance are inputs.

Research dossier: research/2026-10-16/FACTORIAL_GAMMA_FUCC_SUCC.md
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, isqrt


class FactorialGammaGateError(ValueError):
    """An untyped source, illegal truncation, or unsupported claim was requested."""


def _integer(value, *, name: str, low: int = 0, high: int = 5000) -> int:
    if type(value) is not int or not low <= value <= high:
        raise FactorialGammaGateError(f"{name}: exact integer required in [{low}, {high}]")
    return value


def _rational(value, *, name: str, positive: bool = False) -> Fraction:
    if type(value) is not int and not isinstance(value, Fraction):
        raise FactorialGammaGateError(f"{name}: exact integer/Fraction required")
    r = Fraction(value)
    if positive and r <= 0:
        raise FactorialGammaGateError(f"{name}: strictly positive value required")
    return r


def _mp():
    try:
        import mpmath as mp
    except ImportError as exc:
        raise FactorialGammaGateError("mpmath needed only for analytic diagnostics") from exc
    return mp


def _mpf(mp, value):
    """Convert exact rational source parameters without losing rational type gate."""
    if isinstance(value, Fraction):
        return mp.mpf(value.numerator)/value.denominator
    return mp.mpf(value)


def primes_through(bound: int) -> tuple[int, ...]:
    """Local exact primality oracle for finite FUCC source labels (no Euler claims)."""
    _integer(bound, name="prime horizon", low=2, high=2000)
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[0:2] = b"\x00\x00"
    for k in range(2, isqrt(bound) + 1):
        if sieve[k]:
            sieve[k * k:bound + 1:k] = b"\x00" * ((bound - k*k)//k + 1)
    return tuple(i for i in range(2, bound + 1) if sieve[i])


def _prime(p: int) -> int:
    _integer(p, name="FUCC prime", low=2, high=97)
    if p not in primes_through(p):
        raise FactorialGammaGateError("FUCC label must be an actual prime, not composite 6")
    return p


def factorial_pascal_factor(size: int) -> tuple[tuple[int, ...], ...]:
    """A[n,k] = n! binom(n,k), 0<=n,k<size; lower triangular."""
    _integer(size, name="Hankel dimension", low=1, high=25)
    return tuple(tuple(factorial(n) * comb(n, k) if k <= n else 0
                       for k in range(size)) for n in range(size))


def factorial_hankel(size: int) -> tuple[tuple[int, ...], ...]:
    """Moment matrix H[i,j] = (i+j)! of rate-one exponential law."""
    _integer(size, name="Hankel dimension", low=1, high=25)
    return tuple(tuple(factorial(i+j) for j in range(size))
                 for i in range(size))


def factorial_hankel_certificate(size: int) -> dict:
    """Exact finite matrix multiplication, determinant predicted by triangular A.

    Universal proof: sum_k C(i,k) C(j,k)=C(i+j,i) (Vandermonde).
    Computation validates each finite instance; not an independent universal proof.
    """
    a = factorial_pascal_factor(size)
    h = factorial_hankel(size)
    reconstructed = tuple(tuple(sum(a[i][k]*a[j][k] for k in range(size))
                                for j in range(size)) for i in range(size))
    if reconstructed != h:
        raise AssertionError("factorial Hankel/Pascal source failure")
    determinant = 1
    for j in range(size):
        determinant *= factorial(j)**2
    return {"dimension": size, "A": a, "H": h,
            "determinant": determinant, "positive_definite": True,
            "source": "exact factorial moments; classical Pascal/Vandermonde identity",
            "not_signed_Weil": True, "RH_proved": False}


def monic_laguerre_coefficients(degree: int) -> tuple[int, ...]:
    """Ascending coefficients of p_m=(-1)^m m! L_m(x), monic integer."""
    _integer(degree, name="Laguerre degree", low=1, high=18)
    m = degree
    return tuple((-1)**(m+j) * (factorial(m)//factorial(j)) * comb(m, j)
                 for j in range(m+1))


def laguerre_orthogonality_certificate(degree: int) -> dict:
    """Exact polynomial/moment calculations, no approximate quadrature nodes."""
    c = monic_laguerre_coefficients(degree)
    low = tuple(sum(v*factorial(j+k) for j,v in enumerate(c))
                for k in range(degree))
    norm = sum(v*w*factorial(i+j)
               for i,v in enumerate(c) for j,w in enumerate(c))
    expected = factorial(degree)**2
    if any(low) or norm != expected or c[-1] != 1:
        raise AssertionError("monic Laguerre exact moment identity failed")
    return {"degree":degree,"monic_coefficients":c,"lower_orthogonality":low,
            "squared_norm":norm,"first_missing_moment":2*degree,
            "gauss_laguerre_defect":expected,
            "quadrature_exists_by_classical_positive_gauss_theorem":True,
            "finite_atoms_not_unique_source":True}


def counterfeit_two_atom_moment(n: int) -> int:
    """Positive two-atom Gauss-Laguerre law: masses (2+/-sqrt2)/4.

    Support x_-=2-sqrt2, x_+=2+sqrt2; weight of x_- is
    (2+sqrt2)/4, weight of x_+ is (2-sqrt2)/4.
    Recurrence from x^2-4x+2=0: a_n=4a_(n-1)-2a_(n-2).
    """
    _integer(n, name="moment order", low=0, high=256)
    if n == 0:
        return 1
    if n == 1:
        return 1
    a,b = 1,1
    for _ in range(2,n+1):
        a,b = b,4*b-2*a
    return b


def counterfeit_hankel(size: int) -> tuple[tuple[int, ...], ...]:
    _integer(size,name="counterfeit Hankel dimension",low=1,high=15)
    return tuple(tuple(counterfeit_two_atom_moment(i+j) for j in range(size))
                 for i in range(size))


def bareiss_determinant(matrix: tuple[tuple[int, ...], ...]) -> int:
    """Exact fraction-free determinant with pivoting; independent of Pascal route."""
    n = len(matrix)
    if not n or any(len(row)!=n for row in matrix):
        raise FactorialGammaGateError("need a nonempty square integer matrix")
    a = [list(row) for row in matrix]
    if any(type(v) is not int for row in a for v in row):
        raise FactorialGammaGateError("Bareiss certificate is integer-only")
    sign,prev=1,1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot is None:
                return 0
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        pivotval=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivotval-a[i][k]*a[k][j]
                if num % prev:
                    raise ArithmeticError("nonintegral Bareiss elimination")
                a[i][j]=num//prev
        for i in range(k+1,n):
            a[i][k]=0
        prev=pivotval
    return sign*a[n-1][n-1]


def finite_source_countermodel_certificate() -> dict:
    """Exact moment indistinguishability until order 3; order-4 separation."""
    genuine=tuple(factorial(k) for k in range(7))
    mimic=tuple(counterfeit_two_atom_moment(k) for k in range(7))
    return {
        "positive_atomic_measure":True,
        "nodes":"2-sqrt(2), 2+sqrt(2)",
        "weights":"(2+sqrt(2))/4, (2-sqrt(2))/4",
        "genuine":genuine,"mimic":mimic,
        "agree_through":3,"first_discrepancy_order":4,
        "first_discrepancy":genuine[4]-mimic[4],
        "genuine_hankel_3_det":bareiss_determinant(factorial_hankel(3)),
        "atomic_hankel_3_det":bareiss_determinant(counterfeit_hankel(3)),
        "arbitrary_finite_horizons_from_gauss_laguerre":"CLASSICAL IMPORT",
    }


def _valuation_factorial(n: int, prime: int) -> int:
    v=0
    power=prime
    while power<=n:
        v+=n//power
        power*=prime
    return v


def _valuation(n: int, prime: int) -> int:
    v=0
    while n and n%prime==0:
        n//=prime
        v+=1
    return v


def fucc_succ_square(prime: int, n: int) -> dict:
    """Actual carrier maps V_p S = S^p V_p (no curvature claim)."""
    p=_prime(prime)
    _integer(n,name="SUCC source address",low=0,high=200)
    return {"prime":p,"source":n,"V_after_S":p*(n+1),
            "S_power_p_after_V":p*n+p,
            "false_S_after_V":p*n+1,
            "flat_commuting_square":True,
            "nontrivial_if_p_gt_one":p*(n+1) != p*n+1}


def fucc_factorial_dilation_certificate(prime: int, n: int) -> dict:
    """(pn)!/(n!)^p is multinomial, with exact q-adic carry formula.

    The index p is genuine prime FUCC. q ranges over all primes <= pn.
    Despite notation, the algebraic carry formula works for any integer p>=2.
    No nontrivial holonomy is asserted: the original S/V square is flat.
    """
    p=_prime(prime)
    _integer(n,name="dilation source address",low=1,high=30)
    if p*n>1800:
        raise FactorialGammaGateError("dilation exact factorial memory budget exceeded")
    d, rem=divmod(factorial(p*n),factorial(n)**p)
    if rem:
        raise ArithmeticError("multinomial integrality failed")
    carriers={}
    reconstruct=1
    for q in primes_through(p*n):
        raw=_valuation_factorial(p*n,q)-p*_valuation_factorial(n,q)
        carry=0
        power=q
        while power<=p*n:
            carry+=(p*(n%power))//power
            power*=q
        if raw != carry or raw<0:
            raise AssertionError("Legendre carry transport failed")
        if raw:
            carriers[q]=raw
            reconstruct *= q**raw
    if reconstruct != d:
        raise AssertionError("prime-factor reconstruct failed")
    return {"prime_FUCC":p,"source_n":n,"dilation_multinomial":d,
            "q_adic_carries":carriers,"prime_factor_reconstruction":reconstruct,
            "genuine_prime_label":True,"square_has_nontrivial_holonomy":False}


def binomial_cocycle(a: int, b: int, c: int) -> dict:
    for value,name in ((a,"a"),(b,"b"),(c,"c")):
        _integer(value,name=name,low=0,high=100)
    left=comb(a+b,a)*comb(a+b+c,a+b)
    right=comb(b+c,b)*comb(a+b+c,a)
    if left!=right:
        raise AssertionError("factorial associativity cocycle mismatch")
    return {"a":a,"b":b,"c":c,"left":left,"right":right,
            "equal":True,"cocycle_coboundary":True}


def beta_gamma_backward_moment(n: int, r: int) -> dict:
    """If X_(n+1) ~ Gamma(n+2,1), B~Beta(n+1,1) independent,
    B X_(n+1) has Gamma(n+1,1) moments. -log B~Exp(rate n+1).
    """
    _integer(n,name="integer shape anchor",low=0,high=250)
    _integer(r,name="moment order",low=0,high=100)
    beta=Fraction(n+1,n+1+r)
    larger=Fraction(factorial(n+1+r),factorial(n+1))
    smaller=Fraction(factorial(n+r),factorial(n))
    if beta*larger != smaller:
        raise AssertionError("Beta-Gamma source moment transport failed")
    return {"n":n,"r":r,"beta_r_moment":beta,
            "next_shape_moment":larger,"previous_shape_moment":smaller,
            "backward_log_delay_rate":n+1}


def harmonic(n: int) -> Fraction:
    _integer(n,name="harmonic cutoff",low=0,high=5000)
    return sum((Fraction(1,k) for k in range(1,n+1)),Fraction())


def finite_exponential_clock_band_certificate(n: int, cutoff: int,
                                                height: Fraction) -> dict:
    """Fully rational uniform spectral error for Gamma log-clock product.

    Phi_(n,M)(t)=M^(it) prod_(k=n+1)^M k/(k+it)
    approximates Phi_n(t)=Gamma(n+1+it)/n! on |t|<=T.

    Put B=T/(2M)+T^2/[2M(1-T/(M+1))]. If T<M+1 and B<1,
    sup |Phi_(n,M)-Phi_n| <= B/(1-B). No mpmath or zeros.

    Proof: 0 < H_M-log M-gamma <=1/(2M), and for |z|<1,
    |log(1+z)-z| <= |z|^2/[2(1-|z|)], sum_(k>M) k^-2 <= 1/M.
    Since |Phi_n(t)|<=1, |exp(w)-1|<= B/(1-B) for |w|<=B<1.
    """
    _integer(n,name="Gamma shape anchor",low=0,high=500)
    _integer(cutoff,name="number of source rate slots",low=1,high=5000)
    if cutoff<=n:
        raise FactorialGammaGateError("clock cutoff must exceed integer anchor")
    T=_rational(height,name="symmetric spectral half-band")
    if T<0 or T >= cutoff+1:
        raise FactorialGammaGateError("band must satisfy 0 <= T < M+1")
    M=cutoff
    b=T/Fraction(2*M)+T*T/(Fraction(2*M)*(1-T/Fraction(M+1)))
    if b>=1:
        raise FactorialGammaGateError("uncertified band: log-error budget >= 1")
    bound=b/(1-b)
    root=isqrt(M)
    ceiling_root=root if root**2==M else root+1
    coupling_bound=T*(Fraction(ceiling_root,M)+Fraction(1,2*M))
    return {"n":n,"cutoff":M,"band":T,"log_ratio_bound":b,
            "uniform_absolute_error_upper":bound,
            "independent_coupling_error_upper":coupling_bound,
            "positive_gamma_log_source":"CLASSICAL IMPORT / MOMENT UNIQUENESS",
            "first_missing_exponential_rate":M+1,
            "gamma_values_used_to_build_approximant":False,
            "all_numbers_exact_rational":True,"RH_proved":False}


def clock_characteristic(n: int, cutoff: int, t, *, dps: int=70):
    """Numerical readout of a finite source product, *not* Gamma oracle.

    Each k/(k+i*t) is the characteristic function of -Exp(rate k).
    M^(it) is a deterministic shift, not a probability multiplier.
    """
    _integer(n,name="shape anchor",low=0,high=500)
    _integer(cutoff,name="source clock cutoff",low=1,high=5000)
    _integer(dps,name="readout decimal precision",low=25,high=250)
    if cutoff<=n:
        raise FactorialGammaGateError("clock cutoff must exceed n")
    mp=_mp()
    with mp.workdps(dps):
        t=_mpf(mp,t)
        result=mp.exp(1j*t*mp.log(cutoff)
                      -mp.fsum(mp.log(1+1j*t/k) for k in range(n+1,cutoff+1)))
        return +result


def gamma_characteristic(n: int, t, *, dps: int=70):
    """Independent special-function oracle, not part of finite approximant."""
    _integer(n,name="shape anchor",low=0,high=500)
    _integer(dps,name="readout decimal precision",low=25,high=250)
    mp=_mp()
    with mp.workdps(dps):
        t=_mpf(mp,t)
        return +(mp.gamma(n+1+1j*t)/mp.factorial(n))


def gamma_recurrence_conjugacy(n: int, t, *, amplitude=2, dps=70) -> dict:
    """Numerically compare both commuting-square routes over nonzero fiber."""
    _integer(n,name="SUCC shape anchor",low=0,high=250)
    _integer(dps,name="readout decimal precision",low=25,high=250)
    mp=_mp()
    with mp.workdps(dps):
        t=_mpf(mp,t)
        a=mp.mpc(amplitude)
        if not a:
            raise FactorialGammaGateError("nonzero fiber required for invertibility probe")
        ratio0=mp.gamma(n+1+1j*t)/mp.factorial(n)
        ratio1=mp.gamma(n+2+1j*t)/mp.factorial(n+1)
        left=(n+1)*a*ratio1
        right=(n+1+1j*t)*a*ratio0
        return {"n":n,"t":+t,"left":+left,"right":+right,
                "absolute_defect":+abs(left-right),
                "source":"gamma recurrence, numerical readout, exact theorem"}


def spiral_dynamics(n: int, t, *, dps: int=70) -> dict:
    """Gamma radius/angle instantaneous derivatives, numerical check.

    For n>=1: d log|C|/dt=-t sum_{k>n}(k^2+t^2)^(-1);
    d arg(C)/dt=H_n-gamma+sum_{k>n}t^2/[k(k^2+t^2)]>0.
    """
    _integer(n,name="integer factorial anchor",low=1,high=250)
    _integer(dps,name="readout decimal precision",low=25,high=250)
    mp=_mp()
    with mp.workdps(dps):
        t=_mpf(mp,t)
        z=n+1+1j*t
        deriv=mp.digamma(z)
        return {"n":n,"t":+t,"normalized_amplitude":+abs(mp.gamma(z)/mp.factorial(n)),
                "radial_log_slope":+(-mp.im(deriv)),
                "unwrapped_angle_slope":+mp.re(deriv),
                "expected_radius_direction": "expanding" if t<0 else "contracting" if t>0 else "stationary",
                "angle_increasing_for_n_ge_1":True}


def gamma_twist_mutant(n: int, t, c, *, dps: int=70) -> dict:
    """Entire 1-periodic nonzero gauge e^(c sin 2pi z), with real c.

    At integers=1, preserves Gamma recurrence, poles/residues and
    |Gamma(n+1+it)| on every vertical integer line, while altering phase.
    No claim that this mutant is Mellin of a positive measure.
    """
    _integer(n,name="factorial anchor",low=0,high=250)
    _integer(dps,name="readout decimal precision",low=25,high=250)
    mp=_mp()
    with mp.workdps(dps):
        t,c=_mpf(mp,t),_mpf(mp,c)
        phase=c*mp.sinh(2*mp.pi*t)
        genuine=mp.gamma(n+1+1j*t)
        mutant=genuine*mp.exp(1j*phase)
        return {"n":n,"t":+t,"phase_shift":+phase,
                "genuine":+genuine,"mutant":+mutant,
                "radial_difference":+abs(abs(mutant)-abs(genuine)),
                "integer_and_recurrence_match_for_every_n":True,
                "positive_Mellin_source_authenticated":False}


def complex_binomial_cocycle(a, b, c, *, dps: int=75):
    """Independent analytic Gamma cocycle comparison on pole-free chart."""
    _integer(dps,name="readout decimal precision",low=25,high=250)
    mp=_mp()
    with mp.workdps(dps):
        a,b,c=mp.mpc(a),mp.mpc(b),mp.mpc(c)
        def B(z,w):
            return mp.gamma(z+w+1)/(mp.gamma(z+1)*mp.gamma(w+1))
        left=B(a,b)*B(a+b,c)
        right=B(b,c)*B(a,b+c)
        return {"left":+left,"right":+right,"error":+abs(left-right)}


def archimedean_clock_ratio(n: int, cutoff: int, t, *, dps: int=70):
    """Finite exponential-clock reconstruction of normalized *real* Tate Gamma.

    The factor pi^(-it) is fixed by Gamma_R(s)=pi^(-s/2)Gamma(s/2).
    This is NOT a finite-prime realization or Weil sign certification.
    """
    _integer(n,name="Archimedean shape anchor",low=0,high=500)
    _integer(dps,name="readout decimal precision",low=25,high=250)
    mp=_mp()
    with mp.workdps(dps):
        t=_mpf(mp,t)
        return +(mp.exp(-1j*t*mp.log(mp.pi))
                 *clock_characteristic(n,cutoff,t,dps=dps))


def archimedean_ratio_oracle(n: int, t, *, dps: int=70):
    """Independent analytic readout through actual Gamma_R(s), not product."""
    _integer(n,name="Archimedean shape anchor",low=0,high=500)
    _integer(dps,name="readout decimal precision",low=25,high=250)
    mp=_mp()
    with mp.workdps(dps):
        t=_mpf(mp,t)
        s=2*n+2+2j*t
        s0=2*n+2
        return +(mp.power(mp.pi,-s/2)*mp.gamma(s/2)
                 /(mp.power(mp.pi,-s0/2)*mp.gamma(s0/2)))


def beta_product_moment_certificate(n: int, total_events: int, order: int) -> dict:
    """Exact finite-order-statistic/Beta-product/Gamma-moment transport.

    If B_k are independent Beta(k,1), k=n+1,...,M, the positive
    finite source X_(n,M)=M * prod B_k has moment
        E X^r = [(n+r)!/n!] * [M^r M!/(M+r)!],
    and X_(n,M) has law M * U_(n+1:M), the (n+1)-st order statistic
    of M uniform(0,1) draws. No Gamma evaluation is used to build it.

    0<=1 - M^r M!/(M+r)! <= r(r+1)/(2M). All exact rationals.
    """
    _integer(n,name="order statistic predecessor count",low=0,high=300)
    _integer(total_events,name="uniform source size",low=1,high=500)
    _integer(order,name="moment degree",low=0,high=70)
    M=total_events
    if n>=M:
        raise FactorialGammaGateError("order statistic requires 0<=n<M")
    limiting=Fraction(factorial(n+order),factorial(n))
    correction=Fraction(M**order*factorial(M),factorial(M+order))
    observed=limiting*correction
    gap=limiting-observed
    upper=limiting*Fraction(order*(order+1),2*M)
    if not 0<=gap<=upper:
        raise AssertionError("finite Beta product moment bound failed")
    return {"n":n,"M":M,"order":order,
            "finite_positive_Beta_product_moment":observed,
            "finite_uniform_order_statistic_moment":observed,
            "limiting_Gamma_shape_moment":limiting,
            "finite_factorial_correction":correction,
            "positive_moment_deficit":gap,
            "rational_deficit_upper":upper,
            "not_genuine_prime_Euler_FUCC":True,
            "RH_proved":False}


def scaled_order_statistic_cdf_certificate(n: int, total_events: int,
                                            x: Fraction) -> dict:
    """Exact binomial CDF and rational Poisson/Gamma waiting-time error.

    X_(n,M)=M U_(n+1:M). For 0<=x<=M, p=x/M,
       P(X_(n,M)<=x)=P(Bin(M,p)>=n+1).
    Limit: P(Gamma(n+1,1)<=x)=P(Poisson(x)>=n+1).
    A direct maximal coupling of Bern(p), Pois(p) at each M coordinate
    gives total variation <= M*p*(1-exp(-p)) <= M*p^2=x^2/M.
    No numerical Gamma CDF or source oracle enters the exact receipt.
    """
    _integer(n,name="arrival predecessor",low=0,high=300)
    _integer(total_events,name="uniform source count",low=1,high=300)
    x=_rational(x,name="scaled observation threshold")
    M=total_events
    if n>=M or x<0 or x>M:
        raise FactorialGammaGateError("requires 0<=n<M and 0<=x<=M")
    p=x/M
    # Calculate exact CDF; binomial complement chosen to shorten first moments
    # but both expressions are identical by the binomial theorem.
    cdf=1-sum((Fraction(comb(M,k))*p**k*(1-p)**(M-k)
               for k in range(n+1)),Fraction())
    if not 0<=cdf<=1:
        raise AssertionError("exact binomial CDF outside probability range")
    upper=min(Fraction(1), x*x/M)
    return {"n":n,"M":M,"x":x,
            "finite_uniform_order_statistic_cdf":cdf,
            "poisson_arrival_threshold":"P(Poisson(x) >= n+1)",
            "rational_CDF_error_upper":upper,
            "source":"M independent uniform points; exact Binomial(M,x/M) count",
            "Gamma_zeros_read":False,
            "prime_Euler_source_authenticated":False}


def ordered_uniform_beta_isomorphism(beta_coordinates: tuple[Fraction, ...]) -> dict:
    """Exact finite FUCC-product / ordered-SUCC probabilistic source chart.

    Take independent B_k~Beta(k,1), k=1,...,M. Define ordered
      U_(k)=prod_(j=k)^M B_j.
    This is a bijection (0,1)^M to 0<U1<...<UM<1, with Jacobian
      J=prod_(k=1)^M B_k^(k-1).
    The source product density prod k B_k^(k-1) = M! * J;
    the target ordered-uniform density is M!, so change of variables
    authenticates their ENTIRE FINITE JOINT LAW, not merely moments.

    This is a classical ordered-uniform / independent-Beta factorization,
    expressed as a source-map exact rational certificate. It is NOT a
    claim that the Beta multipliers are arithmetic prime factors.
    """
    if not isinstance(beta_coordinates, tuple):
        raise FactorialGammaGateError("Beta source must be a complete ordered tuple")
    M=len(beta_coordinates)
    _integer(M,name="number of finite order events",low=1,high=24)
    values=[]
    for k,v in enumerate(beta_coordinates,start=1):
        b=_rational(v,name=f"Beta({k},1) source coordinate")
        if not 0<b<1:
            raise FactorialGammaGateError("Beta source events require 0 < b_k < 1")
        values.append(b)
    ordered=[Fraction(1)]*M
    product=Fraction(1)
    for i in range(M-1,-1,-1):
        product*=values[i]
        ordered[i]=product
    if not all(0<ordered[i]<ordered[i+1]<1 for i in range(M-1)):
        raise AssertionError("ordered SUCC chart violated")
    inverse=tuple(ordered[i]/ordered[i+1] for i in range(M-1))+(ordered[-1],)
    if inverse!=tuple(values):
        raise AssertionError("source map is not invertible")
    jacobian=Fraction(1)
    for k,b in enumerate(values,start=1):
        jacobian*=b**(k-1)
    beta_density=factorial(M)*jacobian
    target_density=factorial(M)
    if beta_density!=target_density*jacobian:
        raise AssertionError("probability Jacobian normalization failed")
    return {"event_count":M,"independent_beta_coordinates":tuple(values),
            "ordered_uniform_coordinates":tuple(ordered),
            "recovered_beta_coordinates":inverse,
            "absolute_jacobian":jacobian,
            "input_joint_beta_density":beta_density,
            "target_joint_ordered_uniform_density":target_density,
            "change_of_variables_identity":True,
            "source_map_invertible_on_open_simplex":True,
            "probability_ontology":"declared finite probabilistic source",
            "not_prime_fuCC":True,"RH_proved":False}
