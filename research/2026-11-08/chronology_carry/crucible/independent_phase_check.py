"""Separate dyadic modular-source sum and 70-digit interval trigonometry.

Fixed probe times were declared before the held-out source file existed.
`prepare` reads no learned-model code, source receipts, common denominator,
unwrapped hash, carry stream, or inherited Taylor phase evaluator.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import gzip
import json
import time

TIMES = (55003, 55020, 55100, 55736, 82381, 82504, 110004)
FREQUENCIES = (1, 3)
SOURCE_BITS = 192
INTERVAL_DPS = 70


def endpoint_fraction(endpoint):
    sign, mantissa, exponent, bit_count = endpoint
    if not mantissa:
        return Q(0)
    numerator = -mantissa if sign else mantissa
    return Q(numerator * 2**exponent) if exponent >= 0 else Q(numerator, 2**(-exponent))


def interval_record(value):
    lo, hi = map(endpoint_fraction, value._mpi_)
    assert lo <= hi
    return {"lower": str(lo), "upper": str(hi)}


def modular_source_interval(n, bits=SOURCE_BITS):
    """Enclose one exact BBP phase lift, modulo an unknown integer.

    Each term uses a SMALL pole denominator and modular exponentiation.
    Floor each signed rational contribution separately at the fixed scale.
    This is mathematically the BBP finite sum, represented independently of
    the experiment's full common-denominator state recurrence.
    """
    scale = 1 << bits
    lower = 0
    terms = 0
    for j in range(1, n+1):
        for coefficient, pole in ((4, 7), (-2, 4), (-1, 3), (-1, 2)):
            denominator = 8*j-pole
            residue = pow(16, n-j, denominator)
            lower += (scale*coefficient*residue)//denominator
            terms += 1
    # Reducing both endpoints by the SAME integer preserves the whole interval.
    anchor = lower//scale
    return lower-anchor*scale, lower+terms-anchor*scale, scale, terms


def prepare():
    from mpmath.ctx_iv import MPIntervalContext
    iv = MPIntervalContext()
    iv.dps = INTERVAL_DPS
    rows = []
    for n in TIMES:
        start = time.monotonic()
        lo, hi, scale, terms = modular_source_interval(n)
        source_interval = iv.mpf([lo, hi])/scale
        phases = []
        for h in FREQUENCIES:
            argument = 2*h*iv.pi*source_interval
            phases.append({"h": h, "real": interval_record(iv.cos(argument)),
                           "imag": interval_record(iv.sin(argument))})
        rows.append({"time": n, "modular_terms": terms,
                     "source_interval": {"lower": str(Q(lo, scale)),
                                         "upper": str(Q(hi, scale))},
                     "phase_intervals": phases})
        print("independent_phase", n, terms, round(time.monotonic()-start, 3), flush=True)
    return {"schema": "independent-modular-phase-v1",
            "fixed_times": list(TIMES), "fixed_frequencies": list(FREQUENCIES),
            "source_bits": SOURCE_BITS, "interval_dps": INTERVAL_DPS,
            "source_contract": "literal four-pole finite BBP sum; zero seed; 4,-2,-1,-1;7,4,3,2",
            "holdout_file_read": False,
            "independence": "different exact source representation and phase evaluator; shared BBP mathematical ancestry",
            "code_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "rows": rows}


def compare(independent_path, source_path):
    independent_raw = independent_path.read_bytes()
    independent = json.loads(independent_raw)
    source_raw = source_path.read_bytes()
    source = json.loads(gzip.decompress(source_raw) if source_path.suffix == '.gz' else source_raw)
    assert independent['fixed_times'] == list(TIMES)
    assert independent['fixed_frequencies'] == list(FREQUENCIES)
    assert independent['source_bits'] == SOURCE_BITS and independent['interval_dps'] == INTERVAL_DPS
    phase_rows = {r['h']: r for r in source['per_time_phases']}
    # SCALE is the inherited instrument's declared 2^80 integer-box grid.
    # Do not import its evaluator or source implementation to compare endpoints.
    target_scale = 1 << 80
    checks = []
    for row in independent['rows']:
        n = row['time']
        for phase in row['phase_intervals']:
            h = phase['h']
            target = phase_rows[h]['boxes'][n-phase_rows[h]['start']]
            # The experiment's packed Box is [re_lo,re_hi,im_lo,im_hi].
            # Contract schema is checked explicitly; no evaluator is imported.
            assert isinstance(target, list) and len(target) == 4
            assert all(type(v) is int for v in target)
            for component, endpoints in zip(('real', 'imag'), (target[:2],target[2:])):
                lo, hi = Q(phase[component]['lower']), Q(phase[component]['upper'])
                target_lo, target_hi = (Q(v, target_scale) for v in endpoints)
                assert target_lo <= lo <= hi <= target_hi, (n, h, component)
            checks.append({'time': n, 'h': h, 'independent_interval_contained': True})
    return {'status': 'PASS: all independent source-phase intervals contained',
            'source_file_sha256': sha256(source_raw).hexdigest(),
            'independent_prepared_file_sha256': sha256(independent_raw).hexdigest(),
            'code_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
            'component_containments': 2*len(checks), 'phase_checks': checks,
            'scope': 'Fixed selected phase probes; no full source sweep, no independent whole-holdout coefficient or covariance computation.',
            'pi_normality': 'OPEN', 'RH': 'OPEN'}


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=('prepare', 'compare'))
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--independent', type=Path)
    ap.add_argument('--source', type=Path)
    args = ap.parse_args()
    if args.mode == 'prepare':
        result = prepare()
    else:
        if args.independent is None or args.source is None:
            ap.error('compare requires --independent and --source')
        result = compare(args.independent, args.source)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
