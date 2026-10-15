"""One arithmetic object: origin contact discrepancy is EXACT Neumann metric.

From Suzuki Eq (8.2) and distributional -g''=W:
  W_c = W + c delta_0,
  g_c(t)=g(t)-c*|t|/2,
  (G_c-G)|L2_0 = c*(-Delta_N)^-1 = c*K_a,
  Q_Wc(v) = Q_W(v)+c||v||²,
  generalized Rayleigh(G_c,K)=Rayleigh(G,K)+c.

The mathematical lemma is classical (Weil/Suzuki derivatives) with a
new-to-SUCC direct Connes normalization interpretation. Exact finite
rational independent proofs below are sanity checks, not a global
adelic trace or unconditional Weil positivity proof.
"""
from __future__ import annotations
from fractions import Fraction as F

class ContactTransportError(ValueError): pass

def q(x):
    if type(x) not in (int,F):
        raise ContactTransportError("exact original rational test only")
    return F(x)

def original_source_neumann_gate():
    """Replay first-window genuine Neumann and high K source, no sign proof."""
    from .one_object_source_residual import authenticated_first_window_gate
    from . import suzuki_moment_schur as schur
    gate=authenticated_first_window_gate()
    if gate["radius"]!=F(1,2):
        raise ContactTransportError("source interval changed")
    K=schur.low_inverse_neumann(F(1,2),2)
    if K!=((F(1,30),F()),(F(),F(1,210))):
        raise ContactTransportError("original raw Legendre Neumann metric drift")
    return {
       "original_weil_source":gate["source"],
       "source_sha":gate["original_suzuki_git_blob"],
       "radius":F(1,2),
       "raw_legendre_first_two_K":K,
       "contact_delta0_maps_to_relative_K":True,
       "finite_prime_Euler_source_unchanged_under_contact_mutation":True,
       "contact_normalization_from_Tate_Connes_glued":False,
       "signed_schur_positivity_proved":False,
       "rh_proved":False
    }

def _steps(a,values):
    a=q(a)
    if not 0<a<=2 or type(values) is not tuple or not 2<=len(values)<=12:
        raise ContactTransportError("rational radius and finite original step source")
    u=tuple(q(v) for v in values)
    if not any(u) or sum(u)!=0:
        raise ContactTransportError("nonzero original mean-zero test required")
    return a,u

def neumann_antiderivative_energy(a,values):
    """Exact integral ||int_{-a}^x u||_L2² via piecewise linear SUCC."""
    a,u=_steps(a,values)
    h=2*a/len(u)
    result=F();cum=F()
    for v in u:
        result+=h*cum*cum+h*h*cum*v+h**3*v*v/3
        cum+=h*v
    if cum!=0 or result<=0:
        raise ArithmeticError("mean-zero Neumann source positive proof failed")
    return result

def signed_absolute_kernel_energy(a,values):
    """Independent exact -1/2 double integral |x-y| u(x)u(y)."""
    a,u=_steps(a,values);h=2*a/len(u)
    diag=sum((v*v*h**3/3 for v in u),F())
    crossed=2*sum((u[i]*u[j]*(j-i)*h**3
                   for i in range(len(u)) for j in range(i+1,len(u))),F())
    return -(diag+crossed)/2

def contact_shift_certificate(a,values,c):
    """Identity tested both via antiderivatives and source pair kernel.

    Here c is a deliberate contact MUTATION. c=0 is the original source,
    c!=0 must NEVER be silently identified with arithmetic zeta.
    """
    c=q(c);a,u=_steps(a,values)
    K=neumann_antiderivative_energy(a,u)
    signed=signed_absolute_kernel_energy(a,u)
    if K!=signed:raise ArithmeticError("contact-to-Neumann isometry failed")
    return {
       "source":"DECLARED_CONTACT_DELTA0_MUTATION_OF_WEIL",
       "radius":a,"cells":len(u),"contact_mutation":c,
       "original_mean_zero_energy":K,
       "independent_signed_kernel_energy":signed,
       "difference_in_signed_Suzuki_form":c*signed,
       "difference_in_Weil_test_form":c*K,
       "same_off_identity_Weil_distribution":True,
       "original_zeta_contact_authentic":c==0,
       "Connes_off_identity_trace_sufficient_to_pin_contact":False,
       "rh_proved":False
    }

def generalized_rayleigh_shift(G,K,vector,c):
    """Exact finite generalized source spectral offset, including sign."""
    from .one_object_relative_residual import matrix,quadratic,psd,positive_definite,add
    G=matrix(G,square=True);K=matrix(K,square=True)
    c=q(c);v=tuple(q(x) for x in vector)
    if len(G)!=len(K) or len(v)!=len(G) or not positive_definite(K) or not any(v):
        raise ContactTransportError("positive genuine-like metric finite toy only")
    Kg=quadratic(K,v)
    before=quadratic(G,v)/Kg
    after=quadratic(add(G,K,c),v)/Kg
    if after-before!=c:raise ArithmeticError("contact generalized shift false")
    return {
      "source":"FINITE_DECLARED_GENERALIZED_METRIC_TOY",
      "before":before,"after":after,"exact_shift":c,
      "off_identity_trace_identifies_shift":False,
      "genuine_completed_zeta_Weil_gram_authentic":False,
      "rh_proved":False
    }


def contact_moment_boundary_channels(c):
    """Same contact discrepancy creates exactly TWO high/low K boundary couplings.

    At genuine a=1/2 and moment cut P=Legendre 1..30:
      K_(29,31)=-1/906948; K_(30,32)=-1/999180
    in UNNORMALIZED Legendre coordinates. Original source high G>=k K,
    so wrong contact c merely yields D_c >= (k+c) QKQ; it
    need NOT retain a positive relative high gap when k+c<=0.
    Off-identity Connes fixed-point traces cannot see this c.

    Rank of Q K P is exactly 2 for c!=0; the contact correction
    to B is c QKP, NOT an all-low diagonal shift alone.
    """
    c=q(c)
    profile=original_source_neumann_gate()
    from . import suzuki_moment_schur as schur
    boundary=schur.inverse_neumann_boundary_channels(F(1,2),rank=30)
    expect=((29,31,"-1/906948"),(30,32,"-1/999180"))
    if boundary["K_low_high_cross_rank"]!=2 or boundary["channels"]!=expect:
        raise ContactTransportError("authentic Neumann boundary source changed")
    kap=F(369,10000)
    new_gap=kap+c
    return {
      "source":"ORIGINAL_ZETA_SUZUKI_PLUS_DECLARED_CONTACT_GAUGE",
      "radius":F(1,2),
      "original_suzuki_git_blob":profile["source_sha"],
      "original_high_gap_kappa":kap,
      "contact_discrepancy":c,
      "mutated_relative_high_gap_lower":new_gap,
      "strict_relative_high_gap_from_this_bound":new_gap>0,
      "boundary_neumann_channels":tuple((i,j,F(z)*c)
                                       for i,j,z in boundary["channels"]),
      "K_cross_rank_if_contact_discrepancy_nonzero":2 if c else 0,
      "original_zeta_normalization_preserved":c==0,
      "finite_moment_Schur_cross_unchanged_under_wrong_contact":c==0,
      "Connes_off_identity_normalizes_contact":False,
      "completed_weil_global_positive_proved":False,
      "rh_proved":False
    }
