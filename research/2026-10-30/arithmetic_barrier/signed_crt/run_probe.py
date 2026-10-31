"""Run declared joint-phase probes, keeping certified and numerical output distinct."""
from fractions import Fraction as F
from math import ceil, sqrt, pi
import cmath
import hashlib
import json
from signed_crt import (orbit,first_period,order,prime,nearest_complement,
    twist_energy_certificate,char_sum_box,magnitude_interval,variation_interval,
    interaction_interval,coherent_dyadic_control,trig_interval)

HOLDOUT=(521,541,569,577,601,613,617,641,653,673)


def outward(interval,digits=12):
    q=10**digits
    return [str(F((interval[0]*q).__floor__(),q)),str(F((interval[1]*q).__ceil__(),q))]


def decimal_view(interval):
    return [float(interval[0]),float(interval[1])]


def phases_hash(values):
    data='\n'.join(str(q) for q in values).encode()
    return hashlib.sha256(data).hexdigest()


def numerical_fourier_diagnostics(phases,primary,cofiber,h):
    # Diagnostic only. Every source input remains an exact rational; conversion
    # occurs only after reduction modulo one. No floating result is a proof.
    w=[cmath.exp(2j*pi*float((h*v)%1)) for v in cofiber]
    f=[cmath.exp(2j*pi*float((h*v)%1)) for v in primary]
    L=len(w)
    what=[sum(w[j]*cmath.exp(-2j*pi*k*j/L) for j in range(L))/L for k in range(L)]
    # f Fourier with opposite sign implements the exact finite Fourier identity.
    fsum=[sum(f[j]*cmath.exp(2j*pi*k*j/L) for j in range(L)) for k in range(L)]
    reconstruction=sum(a*b for a,b in zip(what,fsum))
    full=sum(a*b for a,b in zip(f,w))
    partial=0j;maximum=0
    for a in f:
        partial+=a;maximum=max(maximum,abs(partial))
    variation=sum(abs(b-a) for a,b in zip(w,w[1:]))
    return {'authority':'ordinary floating diagnostic only',
            'wiener_norm':sum(abs(z) for z in what),
            'gauss_wiener_upper':sqrt(primary[0].denominator)*sum(abs(z) for z in what),
            'fourier_reconstruction_error':abs(reconstruction-full),
            'max_primary_partial_sum':maximum,
            'partial_summation_upper':maximum*(1+variation),
            'length':L}


def main():
    all_values=orbit(400)
    rows=[]
    for p in (13,17,29,37,41,73,97,257)+HOLDOUT:
        assert prime(p) and p%4==1
        b,phases,primary,cofiber=first_period(p,all_values)
        for h in (1,3):
            full=magnitude_interval(char_sum_box(phases,h))
            marginal=magnitude_interval(char_sum_box(primary,h))
            variation=variation_interval(cofiber,h)
            E=interaction_interval(phases,h)
            row={'p':p,'class8':p%8,'h':h,'birth':b,'length':len(phases),
                 'family':'fresh_holdout' if p in HOLDOUT else 'discovery_replay',
                 'source_phase_sha256':phases_hash(phases),
                 'full_modulus':outward(full),'primary_modulus':outward(marginal),
                 'cofiber_variation':outward(variation),'interaction_E':outward(E),
                 'marginal_plus_one_refuted':full[0]>marginal[1]+1,
                 'cofiber_V_le_4_refuted':variation[0]>4,
                 'eligible_for_interaction_candidate':len(phases)**2>=p,
                 'interaction_E_ge_quarter_certified':E[0]>=F(1,4),
                 'numerical_fourier_diagnostic':numerical_fourier_diagnostics(phases,primary,cofiber,h)}
            rows.append(row)
    energy=[]
    for p in (13,17,29,37,41,73):
        _,phases,_,_=first_period(p,all_values)
        cert=twist_energy_certificate(phases,p)
        cert['p']=p;cert['step']=str(cert['step'])
        energy.append(cert)
    c=coherent_dyadic_control(80,120,8)
    cphases=c.pop('changed_phases');c.pop('original_phases')
    c['source_control']='changed dyadic seed; integrated #259/#266 mechanism reproduced'
    c['full_modulus']=outward(magnitude_interval(char_sum_box(cphases)))
    c['interaction_E']=outward(interaction_interval(cphases))
    c={k:(str(v) if isinstance(v,F) else v) for k,v in c.items()}
    restoration=[]
    p=97;_,_,primary,_=first_period(p,all_values)
    for D in (2**8,2**20):
        rebuilt=[];errs=[]
        for mark in primary:
            b,z=nearest_complement(mark.numerator,p,D)
            rebuilt.append((mark+F(b,D))%1);errs.append(abs(z))
        restoration.append({'p':p,'D':D,'length':len(rebuilt),
            'max_circle_distance':str(max(errs)),
            'bound':str(F(p-1,2*p*D)),
            'full_modulus':outward(magnitude_interval(char_sum_box(rebuilt)))})
    eligible=[r for r in rows if r['family']=='fresh_holdout' and r['eligible_for_interaction_candidate']]
    out={'status':'PASS finite certificates; infinite selected interaction OPEN',
         'source':'authentic four-pole BBP, U0=0 except explicitly typed controls',
         'trig_authority':'exact rational Machin bounds + Taylor/Lagrange + outward rounding',
         'discovery_domain':'eligible primes below 500; h=1,2,3,5,16 floating exploratory scan',
         'holdout_primes':HOLDOUT,'rows':rows,'twist_energy_certificates':energy,
         'near_restoration_controls':restoration,'dyadic_control':c,
         'holdout_interaction_candidate':{'eligible_cases':len(eligible),
             'certified_passes':sum(r['interaction_E_ge_quarter_certified'] for r in eligible),
             'infinite_status':'OPEN; finite pass does not promote conjecture'}}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
