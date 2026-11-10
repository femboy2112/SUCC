"""Deterministic finite receipts for all-scale BBP frame gluing (research only).

Run from repository root:
  python research/2026-11-08/scale_adelic_thermal_gluing/receipt.py

The JSON values for complex phase diagnostics are floating observations, NOT
rigorous enclosures or source-selected asymptotic cancellation certificates.
"""
from __future__ import annotations
import cmath
import json
import math
from fractions import Fraction
from pathlib import Path

from observational_succ.duck_bbp import forcing
from observational_succ.adelic_scale_gluing import (
 source_defect,normalized_defect,harmonic_coefficient,
 rational_second_order_residual,residual_bound,
 finite_place_valuations,finite_place_product,source_counterseed,
 weyl_variation_upper,
)

DEST=Path(__file__).with_name("FINITE_RECEIPT.json")


def _is_prime(p: int) -> bool:
    if p<2: return False
    for d in range(2,math.isqrt(p)+1):
        if p%d==0: return False
    return True


def p_primary_channels(epoch: int,p:int)->list[tuple[int,int,int]]:
    """Independent term-by-term original three-positive-channel p-residues.

    This does not import sibling PR #554. Reject all p^2 pole collisions.
    """
    if epoch<16 or not _is_prime(p) or p%8!=1 or not 9*epoch <= 4*p <=10*epoch:
        raise ValueError("requires an actual balanced p≡1 mod8 epoch")
    k=(p-1)//8
    if not (k+1<=epoch<4*k+1<5*k+1<6*k+1<2*epoch<=k+1+p):
        raise ValueError("all four source births must occur within the actual epoch")
    if 8*(2*epoch-1)-2>=p*p:
        raise ValueError("p squared pole interference is not admitted")
    z=[0,0,0]; results=[]
    for n in range(1,2*epoch):
        a=8*n-7
        taps=[[(2,a),(-2,a+3)],[(1,a),(-1,a+4)],[(1,a),(-1,a+5)]]
        for d, terms in enumerate(taps):
            inc=0
            for coeff,den in terms:
                if den%p==0:
                    reduced=den//p
                    if reduced%p==0: raise ValueError("p^2 pole not supported")
                    inc+=coeff*pow(reduced,-1,p)
            z[d]=(16*z[d]+inc)%p
        if n>=epoch: results.append(tuple(z))
    return results


def exact_residue_oracle(epoch:int,p:int)->bool:
    """Independent Fraction recursion for each original source channel."""
    # Independent rational full-epoch residue check, all original times.
    watch=set(range(epoch,2*epoch))
    z=[Fraction(0),Fraction(0),Fraction(0)]
    true=p_primary_channels(epoch,p)
    for n in range(1,2*epoch):
        a=8*n-7
        f3=2*(Fraction(1,a)-Fraction(1,a+3))
        f4=Fraction(1,a)-Fraction(1,a+4)
        f5=Fraction(1,a)-Fraction(1,a+5)
        for d,r in enumerate((f3,f4,f5)):z[d]=16*z[d]+r
        if n in watch:
            c=[]
            for v in z:
                w=p*v
                if w.denominator%p==0: raise ValueError("not p-integral")
                c.append((w.numerator*pow(w.denominator,-1,p))%p)
            if tuple(c)!=true[n-epoch]:
                raise AssertionError((n,tuple(c),true[n-epoch]))
    return True


def _x_states(endpoint:int)->list[Fraction]:
    """Canonical original source, reduced modulo one after every exact step."""
    val=Fraction(0); out=[val]
    for n in range(1,endpoint):
        val=(16*val+forcing(n))%1
        out.append(val)
    return out


def _complex_phase(q:Fraction)->complex:
    return cmath.exp(2j*math.pi*float(q%1))


def _order16(p:int)->int:
    if math.gcd(p,16)!=1:raise ValueError
    y=16%p
    m=1
    while y!=1:
        m+=1;y=(y*16)%p
    return m


def _subgroup_delta(p:int)->float:
    m=_order16(p)
    orbit=[pow(16,j,p) for j in range(m)]
    return max(abs(sum(cmath.exp(2j*math.pi*((c*x)%p)/p) for x in orbit)/m) for c in range(1,p))


def _profile(epoch:int,p:int,h:int):
    C=p_primary_channels(epoch,p)
    x=_x_states(2*epoch)
    a=[cmath.exp(2j*math.pi*((h*sum(cc))%p)/p) for cc in C]
    b=[_complex_phase(h*(x[n]-Fraction(sum(C[n-epoch]),p))) for n in range(epoch,2*epoch)]
    u=[_complex_phase(h*x[n]) for n in range(epoch,2*epoch)]
    if max(abs(a[i]*b[i]-u[i]) for i in range(epoch))>1e-11:
        raise AssertionError("real/prime transport failed")
    running=0j; prefix=0.
    for v in a:
        running+=v;prefix=max(prefix,abs(running))
    observed=abs(sum(u))/epoch
    bv=sum(abs(b[i+1]-b[i]) for i in range(epoch-1))
    bound=weyl_variation_upper(prefix,tuple(b))
    if observed>bound+1e-10:raise AssertionError((observed,bound))
    delta=_subgroup_delta(p)
    envelope=epoch*delta+4*math.sqrt(p)*(2+math.log(_order16(p)))
    if prefix>envelope+1e-9: raise AssertionError("four-stage Gauss envelope")
    return {"epoch":epoch,"prime":p,"h":h,"order":_order16(p),
        "measured_subgroup_delta":format(delta,'.9f'),
        "four_stage_prefix_envelope":format(envelope,'.9f'),
        "signed_real_mean_abs":format(observed,'.12f'),
        "prime_prefix_max":format(prefix,'.9f'),
        "complement_total_variation":format(bv,'.9f'),
        "abel_upper":format(bound,'.12f'),
        "source_phase_products_match":True,
        "p_primary_fraction_oracle":exact_residue_oracle(epoch,p),
        "asymptotic_claim":False}


def build_receipt()->dict:
    entries=[]
    for n in (1,2,16,64,256,1024):
        for k in (1,2,4,16):
            r=normalized_defect(n,k)
            err=abs(rational_second_order_residual(n,k))
            if err>residual_bound(n):raise AssertionError((n,k,err))
            entries.append({"n":n,"k":k,"beta":str(harmonic_coefficient(k)),
                 "normalized_ratio":str(r) if n<=2 and k<=2 else format(float(r),'.12f'),
                 "second_order_bound_pass":True})
    places=[]
    for (n,k) in ((1,1),(2,2),(4,3)):
        x=source_defect(n,k)
        vp=finite_place_valuations(x)
        if finite_place_product(x)*x!=1:raise AssertionError
        places.append({"n":n,"k":k,"positive_rational_defect":str(x),
            "p_valuations":{str(p):v for p,v in vp.items()},
            "rational_product_formula_exact":True})
    copies=[]
    for A in (8,16,32):
        s,upper=source_counterseed(A)
        # Direct original unwrapped recurrence, no circle-residue ambiguity.
        v=Fraction(0);real=[]
        for n in range(1,2*A):
            v=16*v+forcing(n)
            if n>=A: real.append(v+16**n*s)
        observed=sum((abs(u) for u in real),Fraction(0))/A
        if observed>upper:raise AssertionError((A,observed,upper))
        copies.append({"epoch":A,"seed_dyadic":True,
            "real_mean_abs_bound":str(upper),
            "observed_mean_abs":format(float(observed),'.12f'),
            "all_odd_prime_local_source_defects_unchanged":True,
            "one_seed_for_all_epochs":False})
    profiles=[_profile(32,73,1),_profile(80,193,1),_profile(100,233,2)]
    return {"name":"scale-adelic-thermal-gluing","date":"2026-11-08",
      "source":"canonical four-pole zero-seed BBP; duck_bbp.forcing",
      "classification":"exact arithmetic + scoped finite float phase diagnostics",
      "pi_normality":"OPEN", "rational_scale_samples":entries,
      "finite_place_exact":places,"hostile_dyadic_epoch_seeds":copies,
      "balanced_epoch_source_profiles":profiles,
      "warnings":["finite complex and logarithmic diagnostics are not interval certificates",
                  "prime-clock asymptotic is imported from draft PR #554, not recomputed",
                  "no source-selected signed covariance decay is established"]}


def main():
    receipt=build_receipt()
    content=json.dumps(receipt,sort_keys=True,indent=2)+"\n"
    DEST.write_text(content,encoding="utf-8")
    print("RECEIPT OK", DEST, "bytes",len(content),"balanced probes",len(receipt['balanced_epoch_source_profiles']))
    for v in receipt['balanced_epoch_source_profiles']:
        print(v)


if __name__=="__main__":main()
