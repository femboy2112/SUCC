"""Reproduce this research-only finite evidence JSON without a repository checkout."""
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

path=Path(__file__).with_name('prime_cofactor_gamma.py')
spec=importlib.util.spec_from_file_location('prime_cofactor_gamma',path)
f=importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)

def exact(q):
    return str(q.numerator)+'/'+str(q.denominator)


def build():
    primes=[17,41,73,89,97,113,137,193,233,241,257]
    prime_rows=[]
    for p in primes:
        b,last,reentry=f.birth_window(p)
        u=f.original_states(reentry)
        for t in range(last-b+1):
            _,co=f.cofactor_decomposition(p,t,u)
            assert co.denominator%p
            assert f.p_residue(p*u[b+t],p)==4*pow(16,t,p)%p
        k=(p-1)//8
        assert f.p_residue(p*u[reentry],p)==(4*pow(16,3*k,p)-pow(2,-1,p))%p
        prime_rows.append({'p':p,'birth':b,'last_clean':last,
                           'secondary_pole':reentry,'clean_length':3*k,
                           'order_16_mod_p':f.order_of_16(p)})
    hist=[]
    for L in (4,8,16,32):
        n=L*L;m=L+1
        q=f.alpha_cutoff(n)
        bins=f.exact_mesh_occupancy(q,n,m)
        C=f.mesh_collision_energy(bins)
        item={'L':L,'N':n,'M':m,'histogram_exact_counts':bins,
              'collision_exact':exact(C),
              'collision_float_display_only':round(float(C),12)}
        if L<=16:
            item['exact_near_pairs_radius_1_over_M']=f.exact_near_pair_count(q,n,m)
        hist.append(item)
    gamma=[]
    for n in (2,3,4,8,16,32,64,128):
        gap=f.exact_gamma_square_gap(n)
        gamma.append({'n':n,'rational_domination_gap_exact':exact(gap)})
    galois=[]
    for p,T,h in ((17,6,1),(41,8,2),(73,9,3),(113,11,1)):
        a,b=f.galois_energy_pair(p,T,h)
        c=f.galois_direct_mean(p,T,h)
        assert abs(b-c)<1e-7
        galois.append({'p':p,'T':T,'h':h,
                       'selected_norm_square_float_only':round(a/(T*T),9),
                       'galois_mean_norm_square_float_only':round(b/(T*T),9)})
    return {'title':'PGC exact first-birth, integer mesh and Gamma/golden staged receipt',
            'date':'2026-11-02','source':'authentic original signed 4-pole BBP, U0=0',
            'parent_commit':'92f7d4684a1ec68bf0346e0e74ec763e03d8c3b4',
            'precision_note':'All prime and histogram counts / fractions exact; Galois amplitudes and displayed decimal energies floating diagnostics only; no asymptotic claim.',
            'first_pole_prime_windows':prime_rows,
            'source_integer_histograms':hist,
            'gamma_square_domination_rational_gaps':gamma,
            'golden_circle_ring_check_passed_k_1_to_90':all(f.exact_golden_circle_return(k) for k in range(1,91)),
            'numerical_galois_diagnostics':galois}

if __name__=='__main__':
    q=Path(__file__).with_name('FINITE_RECEIPT.json')
    q.write_text(json.dumps(build(),indent=2)+'\n')
    print('wrote:',q,'bytes:',q.stat().st_size)
