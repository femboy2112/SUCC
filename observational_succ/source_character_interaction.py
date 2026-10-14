"""χ4 conductor/parity source extension of the all-place SUCC interaction model.

The primitive odd character mod 4 provides a genuinely different Gamma chart.
The theta/Poisson relation and Dirichlet L functional equation are classical
analytic theorems, imported with stated source normalization. Every arithmetic
coefficient and tail bound below is computed in exact rational arithmetic.
RH or any generalized RH is NOT proved.
"""
from __future__ import annotations

from fractions import Fraction as Q
from .source_model_interaction import (
    SourceInteractionError, _nat, _rational, _prime, _ceil,
    exponential_moment_tail,
)


def character_four(n:int)->int:
    if type(n) is not int or not -10**12<=n<=10**12:
        raise SourceInteractionError('bounded signed integer source needed')
    r=n%4
    return 0 if r%2==0 else (1 if r==1 else -1)


def gauss_sum_four()->dict:
    """Exact finite Gaussian-integer Gauss sum = 2i; odd root number = 1."""
    roots=((1,0),(0,1),(-1,0),(0,-1))
    real=sum(character_four(a)*roots[a][0] for a in range(4))
    imag=sum(character_four(a)*roots[a][1] for a in range(4))
    if (real,imag)!=(0,2):
        raise ArithmeticError('finite Dirichlet Gauss sum wrong')
    return {'primitive_conductor':4,'parity':'odd',
            'gauss_sum_real':real,'gauss_sum_imag':imag,
            'normalized_root_number':'1',
            'arch_gamma_factor':'(4/pi)^((s+1)/2)*Gamma((s+1)/2)'}


def local_chi4_euler(p:int,s:int,depth:int)->dict:
    p=_prime(p)
    s=_nat(s,1,12)
    depth=_nat(depth,0,100)
    chi=character_four(p)
    x=Q(chi,p**s)
    partial=sum((x**k for k in range(depth+1)),Q())
    full=1/(1-x)
    tail=x**(depth+1)/(1-x)
    if partial+tail!=full:
        raise ArithmeticError('character Euler shell incoherent')
    return {'prime':p,'chi4_prime_value':chi,'s':s,'depth':depth,
            'partial':str(partial),'tail':str(tail),'full':str(full),
            'signed_tail_not_a_positive_measure':chi==-1,
            'primitive_euler_place':True}


def chi4_pair_cancellation(n:int)->dict:
    """Wrong EVEN parity deletes the entire odd-character theta source."""
    n=_nat(n,1,100000)
    if character_four(n)+character_four(-n)!=0:
        raise ArithmeticError('odd character parity failed')
    weighted=n*character_four(n)-n*character_four(-n)
    return {'n':n,'unweighted_pair_sum':0,
            'odd_weighted_pair_sum':weighted,
            'unweighted_global_signed_theta_identically_zero':True,
            'correct_theta_uses_n_times_character':True}


def signed_theta_tail(sigma_min:int|Q,sigma_max:int|Q,
                      modes:int,endpoint:int,derivative:int=0,steps:int=128)->dict:
    """Rational uniform vertical-strip bound for completed Dirichlet beta.

    Beta completion has no pole zero-mode; odd theta uses n*chi4(n).
    The analytic theta-to-L interaction is an imported Poisson theorem.
    """
    lo,hi=_rational(sigma_min),_rational(sigma_max)
    if lo>hi or lo<-40 or hi>40:
        raise SourceInteractionError('ordered bounded real strip required')
    N=_nat(modes,1,64)
    T=_nat(endpoint,1,1000)
    r=_nat(derivative,0,2)
    B=max(0,_ceil((hi-1)/2),_ceil(-lo/2))
    m=B+r
    err=Q(1,2**r)*(
        4*(N+2)*exponential_moment_tail(Q(3*(N+1)**2,4),1,m,steps)
        +8*exponential_moment_tail(Q(3,4),T,m,steps))
    return {'primitive_conductor':4,'epsilon_parity':1,
            'sigma_min':str(lo),'sigma_max':str(hi),
            'N':N,'T':T,'derivative':r,'power_envelope':B,
            'rational_upper':str(err),
            'uniform_all_imaginary_ordinates':True,
            'not_a_finite_interval_quadrature_certificate':True}


def chi4_analytic_source_rules()->dict:
    """Exact formal theorem claims with classical Poisson imported as hypothesis."""
    c=gauss_sum_four()
    return {'character':'chi4 odd primitive modulo 4',
            'local_Euler':'product_(p odd) (1-chi4(p)*p^(-s))^(-1), Re s>1',
            'one_real_place_gamma':'(4/pi)^((s+1)/2)*Gamma((s+1)/2)',
            'signed_theta':'sum_(n in Z) n*chi4(n)*exp(-pi*n^2*t/4)',
            'theta_modular':'Theta_chi4(t)=t^(-3/2)*Theta_chi4(1/t)',
            'completed_entire':'Lambda_chi4(s)=1/2*int_1^inf Theta_chi4(t)*(t^((s-1)/2)+t^(-s/2)) dt',
            'functional_equation':'Lambda_chi4(s)=Lambda_chi4(1-s)',
            'finite_Gauss_normalized_epsilon':c['normalized_root_number'],
            'completed_positive_for_real_s':True,
            'beta_at_zero':'1/2',
            'negative_odd_trivial_zeros_simple':True,
            'first_trivial_zero_derivative':'beta_prime(-1)=2*beta(2)/pi',
            'bridge_to_PR68_chiral_diagonal':'k_chiral(0)=4*beta(2)=2*pi*beta_prime(-1)',
            'all_analytic_statements_require_classical_Poisson_import':True,
            'no_Gamma_or_Weil_source_changed':True,
            'GRH_proved':False}


def character_receipt()->dict:
    return {'source':chi4_analytic_source_rules(),
            'Euler_p3':local_chi4_euler(3,2,5),
            'Euler_p5':local_chi4_euler(5,2,5),
            'Euler_p2':local_chi4_euler(2,2,5),
            'incorrect_even_parity':chi4_pair_cancellation(3),
            'theta_tail_critical':signed_theta_tail(0,1,4,18),
            'theta_tail_derivative':signed_theta_tail(-2,3,4,18,1),
            'no_nontrivial_zero_positions_input':True,
            'original_zeta_RH_proved':False,'generalized_RH_proved':False}
