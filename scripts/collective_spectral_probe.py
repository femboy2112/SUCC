#!/usr/bin/env python3
"""Deterministic signed spectral receipt; optional isolated pinned PR137 replay."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('collective_spectral_lane', ROOT/'observational_succ/collective_spectral.py')
C = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = C
SPEC.loader.exec_module(C)
PIN = '95dbf40553e54c901e9998e14b1b9d67298fa89e'
PACKET = 'research/2026-10-16/arithmetic_resonance_receipts/resolvent-final-py313-packet.json'
SOURCE_BLOB = '0cc8510b71d178fc79e8d410a86d8b6014cf9178'
ORIGIN = 'dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc'
CHANNELS = ('both signed poles', 'contact', 'true prime-2 half density', 'one real Gamma tower')
DOSSIERS = ('research/2026-10-16/COMPACT_SOURCE_GALERKIN.md',
            'research/2026-10-16/FRACTIONAL_SOURCE_RANGE_AUDIT.md',
            'research/2026-10-16/AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md',
            'reviews/2026-10-16_OPTIMAL_RESIDUAL_COROLLARY_AUDIT.md',
            'research/2026-10-16/ARITHMETIC_RESONANCE_MEGA_ROUND.md',
            'provenance/IMPORT_MANIFEST.json')


def serial(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, C.Gaussian):
        return {'real': str(x.real), 'imag': str(x.imag)}
    if isinstance(x, C.Interval):
        return [str(x.lower), str(x.upper)]
    if isinstance(x, dict):
        return {str(k): serial(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [serial(v) for v in x]
    return x


def git(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def pinned_bytes(root, path):
    expected = git(root, 'show', PIN+':'+path)
    if (root/path).read_bytes() != expected:
        raise C.SpectralError('pinned file drift: '+path)
    return expected


def verify_pin(root):
    if git(root, 'rev-parse', 'HEAD').decode().strip() != PIN:
        raise C.SpectralError('sibling HEAD differs from pinned PR137')
    records = git(root, 'ls-tree', '-rz', PIN, 'observational_succ').split(b'\0')
    checked = 0
    for record in records:
        if not record:
            continue
        header, path = record.split(b'\t', 1)
        name = path.decode()
        if not name.endswith('.py'):
            continue
        raw = (root/name).read_bytes()
        digest = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if digest != header.split()[2].decode():
            raise C.SpectralError('pinned Python dependency drift: '+name)
        checked += 1
    return {'commit': PIN, 'python_files_checked': checked,
            'documents': {p: hashlib.sha256(pinned_bytes(root, p)).hexdigest()
                          for p in (PACKET,)+DOSSIERS}}


def coordinates(target='S0-odd-normalized-spectrum'):
    return C.Coordinates(SOURCE_BLOB, ORIGIN, F(1, 2),
                         ('P1(2t)', 'P2(2t)', 'P3(2t)', 'P4(2t)'),
                         CHANNELS, (F(1, 3), F(1, 5), F(1, 7), F(1, 9)), target)


def algebra_report():
    from dataclasses import replace
    g = C.HermitianForm(((1, 2), (2, 1)))
    x, y = (1, 0), (0, 1)
    required = tuple(C.combine(x, y, a) for a in (1, -1, C.Gaussian(0, 1), C.Gaussian(0, -1)))
    apparatus = C.QuadraticApparatus(g, required)
    recovered = C.complex_polarization(apparatus.measure, x, y)
    if recovered != C.Gaussian(2) or g.quadratic((1, -1)) != -2:
        raise ArithmeticError('signed calibration failed')
    imaginary = C.HermitianForm(((1, C.Gaussian(0, 2)), (C.Gaussian(0, -2), 1)))
    if C.complex_polarization(imaginary.quadratic, x, y) != C.Gaussian(0, 2):
        raise ArithmeticError('complex convention failed')
    ctx = coordinates()
    bound = C.Bound(ctx, C.Interval(-1, 1), 'inherited', frozenset({'PR137-source', 'PR137-coercivity'}))
    refined = C.Bound(ctx, C.Interval(-F(1, 2), F(1, 3)), 'new-derivation', frozenset({'PR137-source', 'new-code'}))
    rejected = []
    mutations = {'source': replace(ctx, source_blob='fake-source'),
                 'radius': replace(ctx, radius=F(9, 16)),
                 'basis': replace(ctx, basis=tuple(reversed(ctx.basis))),
                 'channels': replace(ctx, channels=CHANNELS[:-1]),
                 'metric': replace(ctx, metric_diagonal=(F(1),)*4),
                 'target': replace(ctx, target='S-epsilon'),
                 'convention': replace(ctx, convention='conjugate-first')}
    for name, mutated in mutations.items():
        try:
            C.intersect_bounds((bound, replace(refined, coordinates=mutated)))
        except C.SpectralError:
            rejected.append(name)
        else:
            raise ArithmeticError('typed mutation accepted: '+name)
    return {'schema': 'COLLECTIVE_SPECTRAL_EXACT_V1',
            'G': ((1, 2), (2, 1)), 'private_diagonals': (g.quadratic(x), g.quadratic(y)),
            'q_plus': g.quadratic((1, 1)), 'q_minus': g.quadratic((1, -1)),
            'recovered_pairing': recovered,
            'complex_sign_control': C.complex_polarization(imaginary.quadratic, x, y),
            'intersection': C.intersect_bounds((bound, refined)), 'rejected_mutations': rejected,
            'conditional_witness_budgets': [C.negative_witness_budget(d) for d in (F(1, 10), F(1, 100), F(1, 1000))],
            'hidden_soft_modes': [C.hidden_soft_mode(n) for n in (4, 20, 100)],
            'status': 'EXACT_FINITE_TESTS_AND_CONDITIONAL_PAPER_THEOREMS',
            'actual_source_negative_direction_found': False}


def psd2(a):
    return a[0][1] == a[1][0] and a[0][0] >= 0 and a[1][1] >= 0 and a[0][0]*a[1][1] >= a[0][1]**2


def sector_lower(form, modes):
    ix = tuple(j-1 for j in modes)
    w = tuple(F(1, 2*j+1) for j in modes)
    block = tuple(tuple(form[i][j] for j in ix) for i in ix)
    def slack(c):
        return tuple(tuple(block[i][j]-(c*w[i] if i == j else 0) for j in range(2)) for i in range(2))
    lo, hi = -F(16), F(16)
    if not psd2(slack(lo)) or psd2(slack(hi)):
        raise ArithmeticError('lower bracket not initialized')
    for _ in range(40):
        mid = (lo+hi)/2
        if psd2(slack(mid)):
            lo = mid
        else:
            hi = mid
    z = slack(lo)
    return {'lower_cap': lo, 'slack': z, 'diagonals': (z[0][0], z[1][1]),
            'determinant': z[0][0]*z[1][1]-z[0][1]**2, 'exact_PSD': psd2(z)}


def exact_derivative_moments(A, gamma_modes=20):
    """Integrate g'_J against exact antisymmetric correlation polynomials.

    All exponential/log/contact/half-density constants are outward intervals
    from pinned source code. No sampled moment and no zero input is used.
    """
    L = A.L
    source = A.verify_runtime_source()
    add, scale, mul = L.interval_add, L.interval_scale, L.interval_mul
    def constant(q):
        return F(q), F(q)
    def exponential_pair(poly, alpha):
        alpha = F(alpha)
        if not alpha:
            return constant(L.poly_integral(poly, 0, 1))
        e = L.tight_exp_neg(abs(alpha), 100)
        if alpha < 0:
            e = F(1)/e[1], F(1)/e[0]
        aa, bb = 1/alpha, -1/alpha
        total_a = total_b = F()
        for k, c in enumerate(poly):
            if k:
                aa, bb = k*aa/alpha, (k*bb-1)/alpha
            total_a += c*aa
            total_b += c*bb
        return add(constant(total_a), scale(e, total_b))
    log2 = L.tight_log2(100)
    invsqrt2 = source.sqrt_inverse(2)
    prime_weight = mul(log2, (invsqrt2.lo, invsqrt2.hi))
    contact = source.contact_iv()
    def prime_integral(poly):
        primitive = (F(),)+tuple(c/F(i+1) for i, c in enumerate(poly))
        return add(constant(L.poly_eval(primitive, 1)), scale(L.interval_poly_eval(primitive, log2), -1))
    def moment(poly):
        pole = add(scale(exponential_pair(poly, -F(1, 2)), -2),
                   scale(exponential_pair(poly, F(1, 2)), 2))
        cg = scale((contact.lo, contact.hi), L.poly_integral(poly, 0, 1)/2)
        prime = mul(prime_weight, prime_integral(poly))
        gamma = constant(0)
        for n in range(gamma_modes):
            d = 4*n+1
            gamma = add(gamma, scale(exponential_pair(poly, F(d, 2)), -F(2, d)))
        total = add(add(pole, cg), add(prime, gamma))
        return {'correlation_polynomial': poly, 'pole': pole, 'contact': cg,
                'prime2': prime, 'Gamma_finite': gamma, 'moment': total}
    records = []
    for j in range(1, 5):
        records.append([moment(C.derivative_correlation_polynomial(j, k)) for k in range(4)])
    # A separate endpoint route for int h_j, including both endpoint terms.
    # GP_j(1/2)=int_0^1 g_J(r)P_j(1-2r)dr. The constant kernel channels
    # integrate to zero because these polynomials have mean zero.
    from math import comb
    endpoint_checks = []
    for j in range(1, 5):
        coeff = L.legendre_polynomial(j, F(1))
        poly = tuple(sum((coeff[k]*comb(k, t)*(-2)**t for k in range(t, len(coeff))), F())
                     for t in range(len(coeff)))
        if L.poly_integral(poly, 0, 1):
            raise ArithmeticError('boundary polynomial lost mean-zero identity')
        pole = scale(add(exponential_pair(poly, -F(1, 2)), exponential_pair(poly, F(1, 2))), -4)
        cg = scale((contact.lo, contact.hi), L.poly_integral((F(),)+poly, 0, 1)/2)
        hinge = add(prime_integral((F(),)+poly), scale(mul(log2, prime_integral(poly)), -1))
        prime = mul(prime_weight, hinge)
        gamma = constant(0)
        for n in range(gamma_modes):
            d = 4*n+1
            gamma = add(gamma, scale(exponential_pair(poly, F(d, 2)), F(4, d*d)))
        endpoint_moment = scale(add(add(pole, cg), add(prime, gamma)), 1-(-1)**j)
        direct = records[j-1][0]['moment']
        if max(endpoint_moment[0], direct[0]) > min(endpoint_moment[1], direct[1]):
            raise ArithmeticError('endpoint versus correlation source moment disagreement')
        endpoint_checks.append({'mode': j, 'two_endpoint_moment': endpoint_moment,
                                'correlation_moment': direct, 'intervals_overlap': True})
    return records, endpoint_checks


def source_report(root):
    before = verify_pin(root)
    # Execute sibling package in this isolated subprocess, never overlay its files.
    sys.path.insert(0, str(root))
    from observational_succ import arithmetic_resolvent as A
    from observational_succ.compact_galerkin import source_legendre_bound
    from observational_succ.four_low_schur_proof_teeth import certified_scalar_improvement
    packet = json.loads(pinned_bytes(root, PACKET))
    if (packet['sourceidentity']['git_blob'] != SOURCE_BLOB or
        packet['sourceidentity']['source_commit'] != ORIGIN or
        tuple(packet['sourceidentity']['channels']) != CHANNELS or
        F(packet['radius']) != F(1, 2) or
        packet['basis'] != 'unnormalized P1(2t), P2(2t), P3(2t), P4(2t)' or
        packet['Wmetric'] != [[str(F(1, 2*i+3) if i == j else F()) for j in range(4)] for i in range(4)]):
        raise C.SpectralError('pinned receipt mathematical identity mismatch')
    print('Replaying signed norm/coercivity source certificates', file=sys.stderr, flush=True)
    inherited = certified_scalar_improvement()
    compression = source_legendre_bound(20)
    print('Recomputing original derivative cells: J=20, grid=512', file=sys.stderr, flush=True)
    raw = A.certified_zero_trial_lower(20, 512)
    coarse_columns = [C.projected_column_bound(c['mode'], c['positive_half_midpoint_intervals'],
                                        raw['grid'], raw['BV_Lipschitz']) for c in raw['columns']]
    exact_moments, endpoint_checks = exact_derivative_moments(A, raw['gamma_modes'])
    columns = [C.refine_projected_column(c, tuple(C.Interval(*m['moment']) for m in row))
               for c, row in zip(coarse_columns, exact_moments)]
    for c, original in zip(columns, raw['columns']):
        if c['finite_J_energy_upper'] != original['finite_J_whole_interval_energy_upper']:
            raise ArithmeticError('independent whole-cell energy replay disagrees')
    eta = raw['sectors']['odd']['whole_Gamma_derivative_operator_tail']
    caps = C.projected_response_caps(columns, eta, raw['kappa'])
    alower = tuple(tuple(F(z) for z in row) for row in packet['A_lower_form'])
    # Fresh independent source-entry replay of the inherited low lower form.
    low_entries = tuple(tuple(A.truncated_entry(i, j, 512) for j in range(1, 5)) for i in range(1, 5))
    if A.interval_majorants(low_entries)[0] != alower:
        raise ArithmeticError('pinned low form differs from fresh source evaluation')
    lower = tuple(tuple(alower[i][j]-(caps['odd' if i%2 == 0 else 'even']['R0_operator_upper_cap']/F(2*i+3)
                                     if i == j else 0) for j in range(4)) for i in range(4))
    sectors = {}
    for name, modes in (('odd', (1, 3)), ('even', (2, 4))):
        old_response = F(packet['lower_response_caps'][name]['R0_operator_upper_cap'])
        if old_response != raw['sectors'][name]['R0_operator_upper_cap']:
            raise ArithmeticError('inherited cell response cap replay mismatch')
        old_form = tuple(tuple(F(z) for z in row) for row in packet['exactlower'])
        old_lo = sector_lower(old_form, modes)
        new_lo = sector_lower(lower, modes)
        upper = F(packet['two_sector_operator_upper_caps'][name]['operator_upper_cap'])
        upper_form = tuple(tuple(F(z) for z in row) for row in packet['exactupper'])
        upper_slack = tuple(tuple((upper*F(1, 2*i+1) if i == j else 0)-upper_form[i-1][j-1]
                                  for j in modes) for i in modes)
        if not psd2(upper_slack):
            raise ArithmeticError('inherited upper scalar certificate rejected')
        ctx = coordinates('S0-'+name+'-normalized-spectrum')
        intersection = C.intersect_bounds((
            C.Bound(ctx, C.Interval(old_lo['lower_cap'], upper), 'PR137', frozenset({'PR137-source', 'high-coercivity'})),
            C.Bound(ctx, C.Interval(new_lo['lower_cap'], upper), 'projected-derivative',
                    frozenset({'PR137-source', 'high-coercivity', 'independent-cell-moments'}))))
        sectors[name] = {'old_R0_cap': old_response, 'new_R0_cap': caps[name]['R0_operator_upper_cap'],
                         'strict_response_improvement': caps[name]['R0_operator_upper_cap'] < old_response,
                         'old_lower': old_lo, 'new_lower': new_lo, 'unchanged_upper': upper,
                         'upper_slack': upper_slack, 'upper_slack_exact_PSD': True,
                         'intersection': intersection}
    loaded = {}
    for name, module in sorted(sys.modules.items()):
        if name == 'observational_succ' or name.startswith('observational_succ.'):
            path = Path(module.__file__).resolve()
            relative = str(path.relative_to(root))
            loaded[relative] = hashlib.sha256(pinned_bytes(root, relative)).hexdigest()
    after = verify_pin(root)
    if before != after:
        raise C.SpectralError('pinned source changed during execution')
    return {'schema': 'COLLECTIVE_SPECTRAL_PINNED_SOURCE_V1', 'source_pin': before,
            'source_tree_stable': True, 'loaded_dependencies_sha256': loaded,
            'source_identity': packet['sourceidentity'], 'radius': F(1, 2), 'basis': packet['basis'],
            'inherited_kappa_replay': inherited, 'compression_theorem_enclosure_replay': compression,
            'fresh_derivative_cell_receipt': raw, 'projected_columns': columns,
            'failed_coarse_projection_columns': coarse_columns,
            'exact_signed_derivative_moments': exact_moments, 'endpoint_moment_crosscheck': endpoint_checks,
            'projected_response': caps, 'fresh_A_lower_form': alower, 'improved_S0_lower_form': lower,
            'sectors': sectors,
            'upper_authority': 'PINNED_PR137_TRIAL_RECEIPT_AND_EXACT_SCALAR_PSD_RECHECK; trial integration not rerun',
            'lower_authority': 'FRESH_EXACT_SOURCE_CELLS_PLUS_NEW_CONDITIONAL_PAPER_PROOF',
            'analytic_debts': ['Inherited whole-high coercivity and square-root range',
                               'Source identification and continuum inequalities are paper proofs',
                               'No effective dense-range rate or actual-source sign',
                               'No Lean extraction or kernel proof for this lane'],
            'source_sign': 'OPEN', 'actual_source_negative_direction_found': False,
            'independent_source_count': 1, 'zero_coordinates_used': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--source', action='store_true')
    parser.add_argument('--source-child', type=Path, help=argparse.SUPPRESS)
    parser.add_argument('--source-root', type=Path, default=ROOT.parent/'SUCC-arithmetic-resonance')
    args = parser.parse_args()
    if args.source_child:
        result = source_report(args.source_child.resolve())
    else:
        result = algebra_report()
        if args.source:
            proc = subprocess.run([sys.executable, '-I', str(Path(__file__).resolve()),
                                   '--source-child', str(args.source_root.resolve())],
                                  stdout=subprocess.PIPE, text=True, check=True)
            result['arithmetic_experiment'] = json.loads(proc.stdout)
    encoded = json.dumps(serial(result), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(encoded)
        print(str(args.output))
    else:
        print(encoded, end='')


if __name__ == '__main__':
    main()
