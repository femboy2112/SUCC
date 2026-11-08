"""Preregistered finite BBP return-energy diagnostics, explicitly noncertifying complex numerics."""
import json
from fractions import Fraction
from series_split import (exact_original_states,phases,shadow_states,
    completed_beta_one_fifth,direct_energy,global_mean,spectral_energy,
    martingale_budget,triad_budget,fejer_energy,normalized_lag,
    gamma_harmonic_truncation_factor,original_forcing)


def bbp_case(Q,M,h):
    z=phases(exact_original_states(Q*M),h)
    base,increment,levels=martingale_budget(z,Q.bit_length()-1)
    return {
        'Q':Q,'M':M,'h':h,'N':Q*M,
        'W_abs':abs(global_mean(z)),
        'W_sq':abs(global_mean(z))**2,
        'R':direct_energy(z,Q),
        'spectral_R':spectral_energy(z,Q),
        'fejer_R':fejer_energy(z,Q),
        'martingale_increments':increment,
        'within_between_budget':triad_budget(z,Q),
        'lag_real_means':[normalized_lag(z,Q,d).real for d in range(1,M)],
    }

def run():
    p=257;n=33;L=4
    zz=exact_original_states(n+L+1)
    difference=zz[n+L]-zz[n]
    distance=min(difference%1,(-difference)%1)
    assert original_forcing(n).denominator%p==0
    assert all(original_forcing(j).denominator%p for j in range(n+1,n+L+1))
    assert difference.denominator%p!=0
    assert Fraction(42,100)<distance<Fraction(43,100)
    ghost=phases(shadow_states(8*40),1)
    periodic=completed_beta_one_fifth(8*6,1)
    data={
        'claim_scope':'OBSERVED-FINITE only; complex amplitudes use stdlib floating point',
        'preregistered_original':[bbp_case(Q,M,h) for Q,M,h in [(4,5,1),(8,6,1),(16,5,2)]],
        'controls':{
            'periodic_beta_1_5_energy':direct_energy(periodic,8),
            'shadow_H_8x40_energy':direct_energy(ghost,8),
            'gamma_harmonic_fixed_20_truncation_constant_Q_1024_M_2048':gamma_harmonic_truncation_factor(1024,2048,20,20),
        },
        'postregistration_source_resonance_257':{
            'p':p,'first_pole_index':n,'local_order':L,
            '16_order_congruence':pow(16,L,p),
            'same_p_local_phase':difference.denominator%p !=0,
            'real_separation_exact_window':['42/100','43/100'],
            'real_separation_float':float(distance),
        },
    }
    print(json.dumps(data,sort_keys=True,indent=2))

if __name__=='__main__':run()
