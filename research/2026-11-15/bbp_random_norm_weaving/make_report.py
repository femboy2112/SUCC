"""Immutable-boundary finite smoke receipts, never universal π-normality evidence."""
import json, math, random, statistics
from fractions import Fraction
from pathlib import Path
import mpmath as mp
from weaving_probe import (source_random_channels,source_probabilities,shared_source_clicks,
                           two_time_chiral_phases,two_path_probability,
                           shared_norm_product,original_jet_direct,lifted_original_states,
                           chiral_jet, chiral_source_partial,bbp_source_partial, stopped_source_click, disk_weave)
mp.mp.dps=85
Q=lambda t:4-2*t**3-t**4-t**5
Ipi=mp.quad(lambda t:Q(t)/(16-t**8),[0,1])
Ichi=mp.quad(lambda t:Q(t)*(16+t**8)/(256+t**16),[0,1])
D=Ipi-Ichi
assert abs(Ipi-mp.pi/16)<mp.mpf('1e-80')
assert D>0
p=float(D)
source=lifted_original_states(285)
jet={str(n):original_jet_direct(source,n,1) for n in range(5,13)}
assert all(jet[str(n)]==chiral_jet(n) for n in range(5,13))
jet_256={str(n):original_jet_direct(source,n,2) for n in range(5,11)}
assert all(jet_256[str(n)]==chiral_jet(n) for n in range(5,11))

# Fresh/preregistered finite smoke locations (NOT a blind validation of π normality)
positions=[(n,h) for n,h in [(5,1),(9,1),(17,1),(29,2)]]
finite=[]
for n,h in positions:
    z=mp.frac(mp.power(16,n)*mp.pi/16)
    z_f=float(z)
    a,b=two_time_chiral_phases(n,z_f,h)
    t0=two_path_probability(a,b,0.)
    ti=two_path_probability(a,b,math.pi/2)
    phase=b*a.conjugate()
    target=-complex(math.cos(2*math.pi*255*h*z_f),math.sin(2*math.pi*255*h*z_f))
    assert abs(phase-target)<2e-11
    finite.append({'n':n,'h':h,'z_float_smoke':z_f,'p_in_phase':t0,
                   'p_quadrature':ti,'source_phase_real':phase.real,
                   'source_phase_imag':phase.imag,'source_reference_error':abs(phase-target)})

# Deliberately finite MC ONLY; extremely rare defect cannot be validated
# by these finite samples. The probability is certified analytically via integrals.
rng=random.Random(202611151706)
mcN=24000
clicked_pi=0; clicked_chi=0; defect_hits=0
for _ in range(mcN):
    t=rng.random(); U=[rng.random() for _ in range(6)]; w=rng.random()
    c0,c1=shared_source_clicks(t,U,w)
    clicked_pi+=c0;clicked_chi+=c1;defect_hits+=c0-c1
assert clicked_pi>=clicked_chi

# Fresh rows for the finite geometric stopping construction.
rng2=random.Random(2026111504)
geoN=62000
geometric_hits=sum(stopped_source_click(rng2) for _ in range(geoN))
assert abs(geometric_hits/geoN-float(Ipi))<.012

# Same-random-disk vs fresh-angle comparison on an actual finite BBP circle tap.
n_ref,h_ref=9,1
z_ref=float(mp.frac(mp.power(16,n_ref)*mp.pi/16))
a_ref,b_ref=two_time_chiral_phases(n_ref,z_ref,h_ref)
rng3=random.Random(2026111534)
shared=0j; fresh=0j
phase_rows=32000
for _ in range(phase_rows):
    u1,u2=rng3.random(),rng3.random()
    shared += shared_norm_product(u1,u2,a_ref,b_ref)
    x1,y1,_,_=disk_weave(u1,u2)
    x2,y2,_,_=disk_weave(rng3.random(),rng3.random())
    fresh += (complex(x2,y2)*b_ref)*(complex(x1,y1)*a_ref).conjugate()
shared=shared/phase_rows;fresh=fresh/phase_rows
assert abs(2*shared-b_ref*a_ref.conjugate())<.018
assert abs(fresh)<.018

summary={
 'status':'finite smoke and exact symbolic or analytic identities; π base-16 normality OPEN',
 'basis':'original immutable four-pole r, zero seed; declared external iid uniform observer',
 'original_pi16_mp':mp.nstr(Ipi,52), 'chiral_twist_mp':mp.nstr(Ichi,52),
 'defect_probability_mp':mp.nstr(D,52),
 'positive_defect_lower_bound':'829/40212480',
 'joint_moment_defect':'-34/45','third_joint_cumulant':'-1/45',
 'jet_mod16_q16':jet,'jet_mod16_q256':jet_256,
 'finite_circle_probe_smoke':finite,
 'geometric_stopped_mc_not_certificate':{
     'seed':2026111504,'rows':geoN,'click_hits':geometric_hits,
     'click_fraction':geometric_hits/geoN,'exact_probability':mp.nstr(Ipi,35)
 },
 'time_coherent_phasor_smoke_not_certificate':{
     'seed':2026111534,'rows':phase_rows,'source_n':n_ref,'h':h_ref,
     'shared_product_real':shared.real,'shared_product_imag':shared.imag,
     'fresh_product_real':fresh.real,'fresh_product_imag':fresh.imag,
     'target_real':(b_ref*a_ref.conjugate()).real,
     'target_imag':(b_ref*a_ref.conjugate()).imag,
 },
 'monte_carlo_not_certificate':{
   'seed':202611151706,'rows':mcN,'pi_click_fraction':clicked_pi/mcN,
   'chiral_click_fraction':clicked_chi/mcN,
   'rare_defect_hits':defect_hits,
   'expected_rare_hits':mcN*p,
   'warning':'A zero-hit run is entirely compatible with the exact rare-event probability.'
 }
}
Path('FINITE_REPORT.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print('Original π/16:',summary['original_pi16_mp'])
print('Chiral twist:',summary['chiral_twist_mp'])
print('Rare defect probability:',summary['defect_probability_mp'])
print('Exact clock jets pass q=16,256')
print('Finite MC:',mcN,'rows; rare defect hits',defect_hits)
print('Geometric MC:',geoN,'rows;',geometric_hits,'π-clicks')
print('Temporal shared 2E product:',2*shared,'target:',b_ref*a_ref.conjugate(),'fresh:',fresh)
