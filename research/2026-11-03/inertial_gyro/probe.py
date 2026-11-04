"""Preregistered source-selected inertial gyro finite holdouts, exact where stated.

Usage: python research/2026-11-03/inertial_gyro/probe.py [--verify]
No pi digits, no random seed, no new Haar theorem; numeric gyroscope finite only.
"""
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from observational_succ.hopf_source_exact import H,ONE,I,J,K
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('source_marked_gyro',ROOT/'gyroscope.py')
g=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=g
spec.loader.exec_module(g)


def raw_fraction_sha(q):
    q=F(q)
    return hashlib.sha256(f'{q.numerator}/{q.denominator}'.encode('ascii')).hexdigest()


def run():
    frames=[g.EFrame('A',ONE),g.EFrame('B',H(F(3,5),F(4,5),0,0)),
            g.EFrame('C',H(F(5,13),0,F(12,13),0))]
    U=g.original_states(384)
    rows=[]
    for N in (96,192,384):
        phases=U[:N]
        pair_sha={f'{a}:{b}':raw_fraction_sha(g.gram_difference_mod1(U[a],U[b],1))
                  for a,b in [(0,N-1),(N//3,2*N//3)]}
        proof=g.exact_histogram_fejer_majorant(phases,32)
        hum=[]
        pattern=[frames[n%3] for n in range(N)]
        for h in (1,2,16):
            base=g.gyro_energy(phases,h)
            refs=[sum(x*x for x in g.common_frame_mean(phases,pattern,h,j))
                  for j in range(3)]
            assert all(abs(v-base)<5e-12 for v in refs)
            hum.append({'h':h,'identity_coherence_sq_float':round(base,12),
                        'max_frame_difference_float':round(max(abs(v-base) for v in refs),15),
                        'three_frame_comparison_pass':True})
        obs=g.gyro_fejer_excess(phases,32)
        assert obs<=float(proof['gyro_excess_upper'])+1e-10
        rows.append({'N':N,'source_phase_difference_hashes':pair_sha,
                     'collision_energy_exact':str(proof['E_exact']),
                     'Fejer_Q_upper_exact':str(proof['Q_upper']),
                     'gyro_fejer_excess_float':round(obs,12),
                     'gyro_fejer_majorant_pass':True,
                     'harmonics':hum})
    # Same four-pole source, but DIFFERENT rational finite initial seed.
    B=384
    alpha=sum((g.original_source(k)/16**k for k in range(1,B+1)),F(0))
    other_seed=F(1,5)-alpha
    other=[U[n]+16**n*other_seed for n in range(B//2,B)]
    coherence=g.gyro_energy(other,1)
    assert coherence>0.999
    # SO3-closed but SU2-nonclosed source relay
    a,b,c=frames
    r1=g.emit_link(a,b);r2=g.emit_link(b,c);r3=g.emit_link(c,a)
    twisted=g.LinkReceipt('C','A',-r3.rotor)
    assert g.relay_triangle(r1,r2,twisted,require_spin=False)==-ONE
    try:
        g.relay_triangle(r1,r2,twisted,require_spin=True)
        raise AssertionError('wrongly accepted central -1 spinor loop')
    except ValueError:pass
    return {'date':'2026-11-03','parent_sha':'a5ea2c51446feb1e48099f18730fc60fa2f45d8e',
            'source':'original signed 4-pole BBP, zero seed, actual rational U_n',
            'exact_gyro_frames':'common source labelled SU2 quaternion groupoid, main H algebra',
            'observations_float_only':'coherence and Fejer energy use math.cos/sin; no numerical asymptotic certificate',
            'rows':rows,
            'wrong_seed_control':{'different_seed':'1/5 - alpha_384',
                                  'last_192_coherence_sq_float':round(coherence,12),
                                  'greater_than_0_999':True},
            'central_sign_control':{'SO3_closed_SU2_holonomy':'-1',
                                    'rejected_by_spin_lift':True},
            'unverified':'original selected all-scale Fourier/Weyl cancellation and pi normality'}


if __name__=='__main__':
    result=run()
    receipt=ROOT/'HOLDOUTS.json'
    if '--verify' in sys.argv:
        assert receipt.exists() and json.loads(receipt.read_text())==result
        print('3/3 exact-source original gyro horizons REPLAY PASS')
    else:
        receipt.write_text(json.dumps(result,indent=2)+'\n')
        print('wrote',receipt)
    print(json.dumps(result,indent=2))
