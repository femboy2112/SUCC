"""Exact finite calibration for MOVING_FREQUENCY; no numerical π input."""
from fractions import Fraction as F
from itertools import combinations

COEFFICIENTS = (4, -2, -1, -1)
OFFSETS = (1, 4, 5, 6)
SIGNED_CONSTANT = F(81, 34694450)
LAG_CONSTANT = F(225, 32768 * 289)


def source(k, coefficients=COEFFICIENTS):
    if k < 1:
        raise ValueError('positive source index required')
    return sum((F(c, 8*(k-1)+d) for c, d in zip(coefficients, OFFSETS)), F())


def orbit(stop, seed=F()):
    values = [F(seed)]
    for k in range(1, stop+1):
        values.append(16*values[-1]+source(k))
    return values


def distance(x):
    q = F(x) % 1
    return min(q, 1-q)


def deficit_lower(phases):
    """N-|sum e(x)| >= (8/N) sum_{i<j} ||x_i-x_j||², exactly."""
    phases = list(phases)
    if not phases:
        raise ValueError('nonempty phases required')
    return F(8, len(phases))*sum((distance(a-b)**2
        for a, b in combinations(phases, 2)), F())


def lag_energy_lower(values, a, h):
    return sum((8*distance(h*(values[n+1]-values[n]))**2
                for n in range(a, 2*a)), F())


def green_interval(n, terms=16):
    lo = sum((F(1,16**j)*source(n+j) for j in range(1,terms+1)), F())
    # Remaining geometric weights total 16^-terms/15; source is decreasing.
    return lo, lo+F(1,15*16**terms)*source(n+terms+1)


def run():
    rows = []
    for a in (4,12,28,44,76):
        vals = orbit(2*a)
        for h in ((a*a+1)//2, 3*a*a//4, a*a):
            phases = [h*vals[n] for n in range(a,2*a+1)]
            source_phases = [h*source(n+1) for n in range(a,2*a)]
            source_lower = deficit_lower(source_phases)/289
            actual_lower = deficit_lower(phases)
            assert source_lower >= SIGNED_CONSTANT*a
            assert actual_lower >= SIGNED_CONSTANT*a
            rows.append({'A':a,'h':h,'exact_source_deficit_lower':str(source_lower),
                'exact_selected_deficit_lower':str(actual_lower),
                'theorem_lower':str(SIGNED_CONSTANT*a)})
    return {'status':'PASS','rows':rows,'scope':'finite exact lower bounds; theorem is paper'}


if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
