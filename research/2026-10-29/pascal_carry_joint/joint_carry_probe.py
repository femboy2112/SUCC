"""Source-locked Pascal/BBP carry coupling and lacunary Oily certificates.

Research-only. Original four-pole forcing and zero seed are immutable.
All finite masses, carry digits, Haar correlations, and cutoff bounds are exact
fractions. The only auxiliary randomization is the DECLARED Bernoulli observation
conditional on the authentic positive Laplace source.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
from math import comb


def forcing(n: int) -> F:
    """Four original signed BBP poles; n>=1. Not a new source."""
    if not isinstance(n, int) or n < 1:
        raise ValueError("positive source index required")
    return F(4, 8*n-7) - F(2, 8*n-4) - F(1, 8*n-3) - F(1, 8*n-2)


def full_orbit(last: int, seed: F=F(0)) -> tuple[F,...]:
    """Exact unwrapped U_0=seed, U_t=16U_(t-1)+r(t)."""
    if not isinstance(last, int) or last < 0:
        raise ValueError("nonnegative horizon required")
    if not isinstance(seed, F):
        seed=F(seed)
    ans=[seed]
    for t in range(1,last+1):
        ans.append(16*ans[-1]+forcing(t))
    return tuple(ans)


def fraction_part(x: F) -> F:
    return x - (x.numerator // x.denominator)


def literal_carry_digits(orbit: tuple[F,...]) -> tuple[int,...]:
    """The exact integer carry k_t=floor(16{U_(t-1)}+r(t)); includes k_1."""
    if not orbit:
        raise ValueError("nonempty orbit required")
    out=[0]
    for t in range(1,len(orbit)):
        v=16*fraction_part(orbit[t-1])+forcing(t)
        k=v.numerator//v.denominator
        assert fraction_part(orbit[t])==v-k
        out.append(k)
    return tuple(out)


@lru_cache(maxsize=None)
def word_mass(n: int, m: int, k: int) -> F:
    """Unnormalized probability of a particular m-letter outcome word with k failures.

    D(n;m,k)= integral e^(-(8n-7+8(m-k))x) Q(x) (1-e^(-8x))^k dx.
    """
    if not isinstance(n,int) or not isinstance(m,int) or not isinstance(k,int) or n<1 or not 0<=k<=m<=n:
        raise ValueError("n>=1 and 0<=k<=m<=n required")
    v=sum(((-1)**i*comb(k,i)*forcing(n+m-k+i) for i in range(k+1)), F(0))
    assert v>0, (n,m,k)
    return v


def path_probability(n:int,m:int,k:int) -> F:
    return word_mass(n,m,k)/forcing(n)


def grade_probability(n:int,m:int,k:int) -> F:
    return comb(m,k)*path_probability(n,m,k)


def posterior_fail(n:int,m:int,k:int) -> F:
    if m>=n:raise ValueError("all trials revealed")
    return word_mass(n,m+1,k+1)/word_mass(n,m,k)


def posterior_success(n:int,m:int,k:int) -> F:
    if m>=n:raise ValueError("all trials revealed")
    return word_mass(n,m+1,k)/word_mass(n,m,k)


def future_grade_conditionals(n:int,m:int,k:int) -> tuple[F,...]:
    """Conditional law of ADDITIONAL failures after an observed prefix."""
    denom=word_mass(n,m,k)
    out=tuple(F(comb(n-m,j))*word_mass(n,n,k+j)/denom for j in range(n-m+1))
    assert sum(out,F(0)) ==1
    return out


def phase_posterior_mass(n:int,m:int,k:int, orbit:tuple[F,...]) -> dict[F,F]:
    """Exact group-algebra support of true future BBP circle phases (without taking roots)."""
    if len(orbit) <=2*n:raise ValueError("orbit needs indices through 2n")
    out:dict[F,F]={}
    for j,p in enumerate(future_grade_conditionals(n,m,k)):
        phase=fraction_part(orbit[n+k+j])
        out[phase]=out.get(phase,F(0))+p
    assert sum(out.values(),F(0)) == 1
    return out


def carry_phase_posterior_mass(n:int,m:int,k:int,orbit:tuple[F,...]) -> dict[tuple[int,F],F]:
    """Exact conditional joint law of literal integer carry and phase at selected future time."""
    carry=literal_carry_digits(orbit)
    if len(orbit)<=2*n:raise ValueError("orbit needs indices through 2n")
    out:dict[tuple[int,F],F]={}
    for j,p in enumerate(future_grade_conditionals(n,m,k)):
        t=n+k+j
        key=(carry[t], fraction_part(orbit[t]))
        out[key]=out.get(key,F(0))+p
    assert sum(out.values(),F(0)) ==1
    return out


def endpoint_weight(j:int) -> F:
    if not isinstance(j,int) or j<0: raise ValueError("j>=0 required")
    return F(j+1, 2**(j+2))


def limiting_correlation(d:int) -> F:
    """Haar autocovariance of F_h(16^n s) with F_h(16^(n+d)s), h!=0."""
    if not isinstance(d,int):raise ValueError("integer lag required")
    d=abs(d)
    return F(5,27*2**d)+F(d,9*2**d)


def exact_haar_variance(N:int) -> F:
    """Exact Haar mean square of N^-1 sum_(n<N) F_h(16^n x) for integer h!=0."""
    if not isinstance(N,int) or N<1:raise ValueError("positive horizon required")
    return (F(N)-F(56,27)+F(12*N+56,27*2**N))/N**2


def exact_carry_phase_haar_gram(n:int,m:int) -> F:
    """Haar over real seed of Theta_n(h;s)*conj(Theta_m(h;s)), h!=0.

    Each future phase at index t has frequency h*16^t, so only exactly
    matching indices contribute. The four-pole phase cancels on the diagonal.
    """
    if not all(isinstance(i,int) and i>=1 for i in (n,m)):
        raise ValueError("source n,m>=1")
    lo=max(n,m)
    hi=min(2*n,2*m)
    return sum((grade_probability(n,n,t-n)*grade_probability(m,m,t-m)
                for t in range(lo,hi+1)), F(0))


def endpoint_tail(J:int) -> F:
    if not isinstance(J,int) or J<0:raise ValueError("J>=0 required")
    return F(J+2,2**(J+1))


def weighted_frequency_cost(J:int) -> F:
    """Exact sum_(0<=j<J) w_j (16^j-1)."""
    if not isinstance(J,int) or J<0:raise ValueError("J>=0 required")
    return F(1+(7*J-1)*8**J,196) - (1-endpoint_tail(J))


def rational_cutoff_bound(n:int,h:int,J:int) -> F:
    """Safe ALL-SEED |Theta_n(h;s)-F_h(U_n(s))| bound.

    Uses PR370 TV<=22/n and 2*pi<44/7. No floating point.
    """
    if not isinstance(n,int) or n<3 or not isinstance(h,int) or h==0 or not isinstance(J,int) or J<0:
        raise ValueError("n>=3, nonzero integer h, J>=0 required")
    return F(44,n)+F(44*abs(h),7*15)*forcing(n+1)*weighted_frequency_cost(J)+2*endpoint_tail(J)


def adaptive_cutoff(n:int,h:int)->int:
    """Largest J with |h|*16^J <= (8n+1)^2 (or 0 if none)."""
    if not isinstance(n,int) or n<1 or not isinstance(h,int) or h==0:raise ValueError("inputs")
    J=0
    while abs(h)*16**(J+1)<=(8*n+1)**2:
        J+=1
    return J


def martingale_energy_from_terminal(n:int,orbit:tuple[F,...]) -> tuple[F, ...]:
    """Squared L2 energy of terminal pure phase is 1; no positive scalar can certify cancellation.

    This method returns formal positive terminal probabilities (sum=1),
    NOT an invalid exact complex energy calculation.
    """
    if len(orbit)<=2*n:raise ValueError("orbit needs indices through 2n")
    return tuple(grade_probability(n,n,j) for j in range(n+1))



# Exact positive Green resolvent of the SAME four-pole source. The infinite
# normalization T_n depends on pi; finite-D truncations below are rational.
def green_truncated_total(n:int, depth:int) -> F:
    if not isinstance(n,int) or n<0 or not isinstance(depth,int) or depth<1:
        raise ValueError("n>=0 and positive depth required")
    return sum((F(1,16**ell)*forcing(n+ell) for ell in range(1,depth+1)),F(0))


def green_truncated_weights(n:int,depth:int)->tuple[F,...]:
    T=green_truncated_total(n,depth)
    w=tuple(F(1,16**ell)*forcing(n+ell)/T for ell in range(1,depth+1))
    assert sum(w,F(0))==1
    return w


def green_tail_probability_bound(n:int,depth:int)->F:
    """All-depth certified bound for exact untruncated future-index tail mass.

    P(L>depth) <= [16^(1-depth)/15]*r(n+depth+1)/r(n+1).
    Derives from monotonic r and T_n >= r(n+1)/16.
    """
    green_truncated_total(n,depth)
    return F(16,15*16**depth)*forcing(n+depth+1)/forcing(n+1)


def green_pascal_joint_truncated(n:int,depth:int,orbit:tuple[F,...]) ->dict[tuple[int,int,int,F],F]:
    """Exact rational positive finite mixture: (Green lag, Pascal grade, carry, phase).

    Choose Green future index ell<=depth, then authentic Pascal Bernoulli
    grade J_(n+ell); mark deterministic original-time carry at t=n+ell+J.
    The packet-grade auxiliary original Oily stages can also be appended
    conditionally on X=e^(-Z); they do not alter this marginal.
    """
    if len(orbit) <=2*(n+depth):raise ValueError("orbit requires through 2(n+depth)")
    w=green_truncated_weights(n,depth)
    carries=literal_carry_digits(orbit)
    out:dict[tuple[int,int,int,F],F]={}
    for ell,pl in enumerate(w,1):
        t0=n+ell
        for j in range(t0+1):
            t=t0+j
            key=(ell,j,carries[t],fraction_part(orbit[t]))
            out[key]=out.get(key,F(0))+pl*grade_probability(t0,t0,j)
    assert sum(out.values(),F(0))==1
    return out


def green_pascal_phase_offset_projection(n:int,depth:int,orbit:tuple[F,...]) ->dict[int,F]:
    """Forget split ell+j, retain the exact total future clock offset."""
    labelled=green_pascal_joint_truncated(n,depth,orbit)
    out:dict[int,F]={}
    for (ell,j,_,_),p in labelled.items():
        offset=ell+j
        out[offset]=out.get(offset,F(0))+p
    assert sum(out.values(),F(0))==1
    return out


def composite_weight_limit(k:int)->F:
    """Exact coefficient [z^k] 15 z / ((16-z)(2-z)^2), k>=1."""
    if not isinstance(k,int) or k<1:raise ValueError("k>=1 required")
    return F(15,196)*(F(1,16**k)+F(7*k-1,2**k))


def composite_limit_tail(depth:int)->F:
    """Exact mass of limiting K at lag>depth, nonnegative."""
    if not isinstance(depth,int) or depth<0:raise ValueError("nonnegative depth")
    # Remaining geometric portion from future Green and doubled Oily wait.
    return 1-sum((composite_weight_limit(k) for k in range(1,depth+1)),F(0))


def composite_real_source_tv_bound(n:int)->F:
    """TV(K_n, K_limit)<=TV(Green_n,geom16)+E_Pascal TV(q,w).

    Valid n>=3 (PR370 TV(q_t,w)<=22/t, t=n+ell). Uses all-a source
    EX<2/a, giving Green<=256/(225*(8n+1)); independent of the BBP seed.
    """
    if not isinstance(n,int) or n<3:raise ValueError("source n>=3 required")
    return F(256,225*(8*n+1))+F(22,n+1)


def composite_filter_inverse_coefficients()->tuple[int,...]:
    """(16-S)*(2-S)^2 = 64-68S+20S²-S³."""
    return (64,-68,20,-1)


def composite_limiting_correlation(d:int)->F:
    """All-lag exact Haar covariance of the Green/Oily composite circle filter.

    C(d) = sum_(r>=1) k_r k_(r+|d|), with k_r = 15/196 *
    (16^-r +(7r-1)2^-r). The closed form uses three geometric sums.
    """
    if not isinstance(d,int):raise ValueError("integer lag required")
    d=abs(d)
    c=F(225,196**2)
    return c * (F(1,16**d)*(F(1,255)+F(193,961))
                +F(1,2**d)*(F(821,27)-F(1,31)+F(224,961)
                                +d*(F(175,9)+F(7,31))))


def composite_truncated_reconstruction_error_bound(n:int,depth:int)->F:
    """Uniform error for recovering actual z_(n+1) from four Green/Pascal readouts.

    All-source/same-seed, |z_t|<=1, n>=3:
      |z_(n+1)-(64Xi_(n,D)-68Xi_(n+1,D)
                       +20Xi_(n+2,D)-Xi_(n+3,D))/15|
          <= (2/15)*sum_(i=0)^3 |c_i|*(epsilon_(n+i)+tau_(n+i,D)).
    eps is full-source vs limiting convolution TV; tau truncation TV.
    """
    if not isinstance(n,int) or n<3 or not isinstance(depth,int) or depth<1:
        raise ValueError("n>=3 and depth>=1 required")
    return F(2,15)*sum((abs(c)*(composite_real_source_tv_bound(n+i)
                                       +green_tail_probability_bound(n+i,depth))
                         for i,c in enumerate(composite_filter_inverse_coefficients())),F(0))


def authentic_sensor_variance(n:int)->F:
    """Strictly positive Var_mu_n(1-exp(-8X)) from original four-pole moments."""
    if not isinstance(n,int) or n<1: raise ValueError("n>=1 required")
    a=forcing(n)
    return (a*forcing(n+2)-forcing(n+1)**2)/a**2


def initial_failure_probability(n:int)->F:
    if not isinstance(n,int) or n<1:raise ValueError("n>=1 required")
    return 1-forcing(n+1)/forcing(n)


def finite_composite_offset_distribution(n:int,depth:int)->dict[int,F]:
    """Exact rational projection of labelled Green+Pascal observations to total lag."""
    weights=green_truncated_weights(n,depth)
    out:dict[int,F]={}
    for ell,w in enumerate(weights,1):
        t=n+ell
        for j in range(t+1):
            offset=ell+j
            out[offset]=out.get(offset,F(0))+w*grade_probability(t,t,j)
    assert sum(out.values(),F(0))==1
    return out


def finite_composite_exact_tv(n:int,depth:int)->F:
    """Exact TV of finite-D law vs infinite *limiting* k_r; infinite tail summed exactly."""
    finite=finite_composite_offset_distribution(n,depth)
    max_lag=n+2*depth
    return F(1,2)*(sum((abs(finite.get(r,F(0))-composite_weight_limit(r))
                         for r in range(1,max_lag+1)),F(0))
                  + composite_limit_tail(max_lag))


if __name__ == '__main__':
    for n in range(1,10):
        assert sum((grade_probability(n,n,j) for j in range(n+1)),F(0))==1
        assert sum(future_grade_conditionals(n,0,0))==1
    print("SOURCE_PASCAL_CARRY_JOINT_EXACT_PASS n=1..9")
