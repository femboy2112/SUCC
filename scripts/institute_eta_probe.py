"""Bounded authentic J24 source replay, then exact Young-parameter search.

No source run per parameter. The full decomposition is preserved so each
matrix and the stronger direction-level obstruction can be reconstructed.
All failures concern these sufficient bounds, never the genuine Weil sign.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]
# Squared exact Schur witnesses exceed Python's default 4300-digit print
# limit. This bounded local certificate has a 50000-digit serialization cap.
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(50000)
sys.path.insert(0, str(ROOT))
from scripts.institute_schur_probe import PR177_COMMIT, gamma_coefficients
SOURCE_CACHE_SHA256='0a24144e8a22178296ad314e846ea13ab41a67efc291a42b6764f73d61e0d7aa'


def psd(m):
    return m[0][0] >= 0 and m[1][1] >= 0 and m[0][0]*m[1][1] >= m[0][1]**2


def quadratic(m, c):
    return sum((c[i]*m[i][j]*c[j] for i in range(2) for j in range(2)), Q())


def lower(T, M, kappa, errors, eta, theta=None):
    if eta <= 0 or (theta is not None and theta <= 0):
        raise ValueError("strictly positive Young parameters required")
    if theta is None:
        e = sum((x*x for x in errors), Q())
        diagonal = (e, e)
    else:
        diagonal = (errors[0]**2*(1+theta), errors[1]**2*(1+1/theta))
    return tuple(tuple(T[i][j] - ((1+eta)*M[i][j] +
                ((1+1/eta)*diagonal[i] if i == j else 0))/kappa
                for j in range(2)) for i in range(2))


def triangle_obstruction(T, M, kappa, errors, c):
    """Exact negativity of T[c]-(sqrt(M[c])+sum|ci|ei)^2/kappa.

    No sqrt rounding: if H>=0, compare H² with 4 M[c] e[c]².
    This is failure of a conservative lower bound, not of the source form.
    """
    m = quadratic(M, c)
    if m < 0:
        raise ArithmeticError("residual Gram must be positive semidefinite")
    e = sum((abs(c[i])*errors[i] for i in range(2)), Q())
    H = kappa*quadratic(T, c) - m - e*e
    gap = 4*m*e*e - H*H
    fail = H < 0 or (H >= 0 and gap > 0)
    return {"direction": c, "source_energy_lower": quadratic(T,c),
            "finite_residual_norm_squared":m, "error_norm_upper":e,
            "retained_energy_minus_nominal_residual_over_kappa":quadratic(T,c)-m/kappa,
            "nominal_gap_kappa_t_minus_m":kappa*quadratic(T,c)-m,
            "nominal_residual_already_obstructs":kappa*quadratic(T,c)<m,
            "H":H, "four_m_e_squared_minus_H_squared":gap,
            "triangle_certificate_strictly_negative":fail,
            "genuine_source_negative":False}


def scan(T, M, kappa, errors):
    parameters = tuple(Q(2)**i for i in range(-7, 8))
    results = []
    best = None
    for eta in parameters:
        for theta in (None,) + parameters:
            matrix = lower(T,M,kappa,errors,eta,theta)
            score = min(matrix[i][i]-abs(matrix[i][1-i]) for i in range(2))
            result = {"eta":eta,"theta":theta,"PSD":psd(matrix),
                      "gershgorin_lower_floor_1e12":Q(score.numerator*10**12//score.denominator,10**12)}
            results.append(result)
            if best is None or score > best[0]:
                best = (score, {**result,"exact_lower_matrix":matrix})
    directions = [(Q(1),Q(0)), (Q(0),Q(1))]
    directions += [(Q(1),Q(i,8)) for i in range(-64,65) if i]
    witnesses = [triangle_obstruction(T,M,kappa,errors,c) for c in directions]
    failures = [w for w in witnesses if w["triangle_certificate_strictly_negative"]]
    # Keep all exact failing directions and one full exact certificate. The
    # full source decomposition permits reproduction of every other entry.
    return {"grid":results,"grid_has_PSD_lower":any(x["PSD"] for x in results),
            "best_gershgorin_lower":best[1],
            "direction_count":len(directions),
            "triangle_failing_directions":[w["direction"] for w in failures],
            "triangle_obstruction_witness":failures[0] if failures else None,
            "all_scalar_Young_parameters_obstructed":bool(failures)}


def calibrate():
    T=((Q(5),Q(0)),(Q(0),Q(5)))
    M=((Q(1),Q(0)),(Q(0),Q(1)))
    # The scalar identity is embedded with errors (1,0), and check e1.
    errors=(Q(1),Q(0))
    assert lower(T,M,Q(1),errors,Q(1,4))[0][0] < 0
    assert lower(T,M,Q(1),errors,Q(1))[0][0] > 0
    good=triangle_obstruction(T,M,Q(1),errors,(Q(1),Q(0)))
    bad=triangle_obstruction(((Q(3),Q(0)),(Q(0),Q(3))),M,Q(1),errors,(Q(1),Q(0)))
    assert not good["triangle_certificate_strictly_negative"]
    assert bad["triangle_certificate_strictly_negative"]
    return {"eta_choice_can_change_sufficient_sign":True,
            "triangle_obstruction_positive_and_negative_controls":True}


def child(archive_root, resume_source=None):
    import resource
    import time
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (240,240))
    sys.path.insert(0,archive_root)
    from observational_succ import original_continuum_residual as R
    from observational_succ import clamped_k_residual_bridge as B
    started=time.monotonic()
    if resume_source:
        if hashlib.sha256(Path(resume_source).read_bytes()).hexdigest()!=SOURCE_CACHE_SHA256:
            raise ValueError('source cache digest mismatch; rerun exact archived source')
        baseline=json.loads(Path(resume_source).read_text())
        assert baseline['frozen_source_git_blob']==R.SOURCE_SHA
        assert (baseline['source_J'],baseline['finite_Gamma_Taylor_M'],baseline['polar_Taylor_P'])==(24,192,18)
    else:
        baseline=R.source_residual_schur_trial(J=24,M=192,P=18,fit=True,eta=Q(1,4))
        Path('/tmp/succ-institute-eta-source-f309d910-J24M192.json').write_text(json.dumps(baseline,default=str))
    cache=Path(resume_source) if resume_source else Path('/tmp/succ-institute-eta-source-f309d910-J24M192.json')
    previous=json.loads((ROOT/'research/2026-10-18/INSTITUTE_GAMMA_SCHUR_J24.json').read_text())['source_Schur_replay']
    blocks={}
    for parity,data in baseline['four_original_parity_Schur_blocks'].items():
        kappa=Q(data['source_kappa'])
        M=tuple(tuple(Q(v) for v in row)for row in data['surrogate_QE_action_residual_gram_exact'])
        assert psd(M)
        energy=tuple(tuple(tuple(Q(v)for v in entry)for entry in row)
                     for row in data['genuine_signed_qJ_intervals'])
        radii=tuple(sum(((energy[i][j][1]-energy[i][j][0])/2 for j in range(2)),Q())for i in range(2))
        tail=tuple(tuple(Q(v)for v in row)for row in data['genuine_infinite_Gamma_tail_lower_Gram'])
        if not data['source_tail_matrix_is_PSD']:
            tail=((Q(0),Q(0)),(Q(0),Q(0)))
        T=tuple(tuple(sum(energy[i][j])/2+tail[i][j]-(radii[i]if i==j else 0)
                      for j in range(2))for i in range(2))
        errors=[]
        for index,coeff,finite in zip(data['indices'],data['fitted_high_coefficients'],data['finite_source_action_error_each']):
            h=R.high_boundary_match(index,Q(coeff))['h']
            assert all(B.value(p,e)==0 for p in (h,B.derivative(h))for e in (-Q(1,2),Q(1,2)))
            constants=gamma_coefficients(24)
            h1=constants['new_H1']*B.sqrt_up(R.derivative_norm_squared(h))
            h2=constants['selected_H2']*B.sqrt_up(R.norm_squared(B.derivative(B.derivative(h))))
            errors.append(Q(finite)+min(h1,h2))
        same=lower(T,M,kappa,errors,Q(1,4))
        old=tuple(tuple(Q(v)for v in row)for row in previous['parity_comparison'][parity]['new_lower'])
        assert same==old, 'source decomposition must exactly reproduce sealed J24 receipt'
        blocks[parity]={"source_energy_lower_matrix":T,"continuum_residual_Gram":M,
            "source_kappa":kappa,"combined_action_errors":errors,
            "fitted_high_coefficients":data['fitted_high_coefficients'],
            "baseline_eta_quarter_matches_prior_receipt_exactly":True,
            **scan(T,M,kappa,errors)}
    return {"source_commit":PR177_COMMIT,"source_blob":R.SOURCE_SHA,
        "J":24,"M":192,"P":18,"source_evaluations_this_run":0 if resume_source else 1,
        "resumed_source_decomposition":str(resume_source) if resume_source else None,"blocks":blocks,
        "source_decomposition_sha256":hashlib.sha256(cache.read_bytes()).hexdigest(),
        "calibration":calibrate(),"seconds":time.monotonic()-started,
        "peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "source_coercivity_authority":"INHERITED_SOURCE_CONDITIONAL",
        "genuine_S4_sign_decided":False,"RH_proved":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--child',help=argparse.SUPPRESS)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--self-test',action='store_true')
    parser.add_argument('--resume-source',type=Path)
    args=parser.parse_args()
    if args.self_test:
        print(json.dumps(calibrate()));return
    if args.child:
        print(json.dumps(child(args.child,args.resume_source),default=str,sort_keys=True));return
    archive=subprocess.run(['git','archive',PR177_COMMIT,'observational_succ'],check=True,stdout=subprocess.PIPE).stdout
    with tempfile.TemporaryDirectory(prefix='succ-institute-eta-')as tmp:
        with tarfile.open(fileobj=io.BytesIO(archive))as tar:
            if any(not(m.name=='observational_succ'or m.name.startswith('observational_succ/'))or '..'in Path(m.name).parts for m in tar.getmembers()):
                raise ValueError('unexpected archive member')
            tar.extractall(tmp)
        command=[sys.executable,str(Path(__file__).resolve()),'--child',tmp]
        if args.resume_source:command+=['--resume-source',str(args.resume_source.resolve())]
        run=subprocess.run(command,
            stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=270,cwd=tmp)
        if run.returncode:
            sys.stderr.write(run.stderr)
            raise RuntimeError(f"bounded source child failed: exit {run.returncode}")
        data=json.loads(run.stdout)
    output=json.dumps(data,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(output)
    print(output,end='')


if __name__=='__main__':
    main()
