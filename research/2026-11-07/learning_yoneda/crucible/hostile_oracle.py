"""Independent exact controls, reusing existing SUCC finite channel machinery.

Every reported check is finite. Paper statements are in HOSTILE_THEOREMS.md.
No numerical transcendental equality is used to certify a Fourier statement:
homometry uses integer autocorrelations, and finite Haar uses residue counts.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path

from observational_succ.interobserver_channels import (
    InterobserverWorld, ZeroErrorChannelError, exact_minimum_channel,
)
from observational_succ.selected_orbit import SelectedOrbit, green_tail_interval
from observational_succ.adaptive_proof_policy import adaptive_policy_demo


def source(n: int) -> Q:
    """Independent literal four fractions, not duck_bbp's combined formula."""
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def unwrapped(seed: Q, count: int, mutant: bool = False) -> list[Q]:
    values = [Q(seed)]
    for n in range(1, count+1):
        values.append(16*values[-1]+source(n)+(Q(1, 8*n-7) if mutant else 0))
    return values


def c5_source_world():
    """One genuine-forcing step, ten declared seeds, restricted lookup probe.

    s=(e/5+j)/16; transcript=(e+j)%5; completed relative current phase=e/5;
    target=j. This includes the zero source but is not the singleton zero model.
    """
    rows = tuple((e, j, Q(e+5*j, 80)) for e in range(5) for j in range(2))
    world = InterobserverWorld(
        tuple(f"edge{e}:side{j}" for e, j, _ in rows),
        tuple(str((e+j)%5) for e, j, _ in rows),
        tuple(str((unwrapped(s, 1)[1]-source(1))%1) for _, _, s in rows),
        tuple(str(j) for _, j, _ in rows),
    )
    return rows, world


def independent_decoder_possible(world, colors):
    """Enumerate conflicting history pairs; do not call the coloring solver."""
    code = dict(zip(world.sender_alphabet(), colors))
    for i in range(len(world.sources)):
        for j in range(i):
            if (world.receiver_views[i] == world.receiver_views[j]
                and code[world.sender_views[i]] == code[world.sender_views[j]]
                and world.targets[i] != world.targets[j]):
                return False
    return True


def autocorrelation(points, modulus):
    return tuple(sum((a-b)%modulus == d for a in points for b in points)
                 for d in range(modulus))


def bernoulli_cdf_at_hex_rational(p, x):
    """Exact F_p(x) when x has a terminating base-16 expansion."""
    result, prefix, remaining = Q(), Q(1), Q(x)
    for _ in range(100):
        if remaining == 0:
            return result
        remaining *= 16
        digit = remaining.numerator//remaining.denominator
        remaining -= digit
        result += prefix*sum(p[:digit], Q())
        prefix *= p[digit]
    raise ValueError("Only terminating hexadecimal arguments in this oracle")


def adaptive_periodic_impersonation(rounds=7):
    """Certified authentic-alpha interval; no rational replacement of pi.

    This deliberately gives the learner even unwrapped linear probes. Its
    branch rules may be discontinuous. Positive bounded sensor error still
    admits the identical transcript from a periodic completed wrong seed.
    """
    times, slopes, errors, reports = [], [], [], []
    time, previous = 0, Q()
    for j in range(rounds):
        slope = 1+previous.denominator%5
        report = slope*unwrapped(Q(), time)[-1]
        times.append(time)
        slopes.append(slope)
        errors.append(Q(1, 16**(j+3)))
        reports.append(report)
        time += 1+abs(report.numerator)%3
        previous = report
    period = 1
    while any(Q(L*16**t, 2*(16**period-1)) >= epsilon
              for t, L, epsilon in zip(times, slopes, errors)):
        period += 1
    denominator = 16**period-1
    low, high = green_tail_interval(0, period+12)
    midpoint = (low+high)/2
    k = (denominator*midpoint+Q(1, 2)).numerator//(denominator*midpoint+Q(1, 2)).denominator
    if not Q(2*k-1, 2) < denominator*low < denominator*high < Q(2*k+1, 2):
        raise AssertionError("nearest-grid integer is not interval certified")
    beta = Q(k, denominator)
    displacement = max(abs(beta-low), abs(beta-high))
    for t, L, epsilon in zip(times, slopes, errors):
        if not L*16**t*displacement < epsilon:
            raise AssertionError("the periodic clone exceeds the sensor budget")
    return {"rounds": rounds, "times": times, "probe_slopes": slopes,
            "error_budgets": list(map(str, errors)),
            "reports": list(map(str, reports)), "period": period,
            "beta_numerator": k, "beta_denominator": denominator,
            "alpha_interval": [str(low), str(high)],
            "absolute_seed_difference_upper": str(displacement),
            "common_transcript_certified": True,
            "source_family": "all real seeds with original forcing; exact zero tag omitted",
            "normality_of_clone": "NONNORMAL by finite periodic completion"}


def run():
    checks = Counter()

    def require(condition, family):
        if not condition:
            raise AssertionError(family)
        checks[family] += 1

    rows, world = c5_source_world()
    code = exact_minimum_channel(world)
    require(len(set(s for _, _, s in rows)) == 10, "conditional_memory")
    require(rows[0][2] == 0, "conditional_memory")
    require(code.codewords == 3 and code.fixed_width_bits == 2, "conditional_memory")
    require(max(Counter(world.receiver_views).values()) == 2, "conditional_memory")
    for colors in product(range(2), repeat=5):
        require(not independent_decoder_possible(world, colors), "independent_binary_codes")
    require(independent_decoder_possible(world, (0, 1, 0, 1, 2)), "conditional_memory")
    for (e, j, s), transcript, physical, target in zip(
            rows, world.sender_views, world.receiver_views, world.targets):
        require((unwrapped(s, 1)[1]-source(1))%1 == Q(e, 5), "conditional_memory")
        require(code.decode(code.encode(transcript), physical) == target, "conditional_memory")
    conflict = InterobserverWorld(("a", "b"), ("u", "u"), ("p", "p"), ("0", "1"))
    try:
        exact_minimum_channel(conflict)
    except ZeroErrorChannelError:
        require(True, "impossible_access_rejected")
    else:
        raise AssertionError("An inaccessible target was falsely repaired by memory")

    # Exact full lift and original projection: distinct implementations.
    for seed in (Q(0), Q(1, 3), Q(-2, 11), Q(7, 16**5)):
        values = unwrapped(seed, 83)
        reference = SelectedOrbit(seed)
        for n, value in enumerate(values):
            require(value%1 == reference.state(n), "source_cross_implementation")
        for n in (0, 2, 7, 17, 31, 67):
            for d in (1, 3, 7, 11):
                forcing = sum((16**(d-j)*source(n+j) for j in range(1, d+1)), Q())
                require(values[n+d]-16**d*values[n] == forcing, "closed_loop_seed_blind")
    base = unwrapped(Q(0), 12)
    changed = unwrapped(Q(0), 12, mutant=True)
    require(base[0] == changed[0] == 0, "source_mutation")
    require(base[1] != changed[1], "source_mutation")
    require(changed[1]-16*changed[0] != source(1), "source_mutation")

    # Prescribed fresh tail aliases: exact original forcing, changed seed.
    for depth in (2, 5, 7):
        zero = unwrapped(Q(), depth+6)
        shifted = unwrapped(Q(1, 16**depth), depth+6)
        for n in range(depth+7):
            require(shifted[n]-zero[n] == Q(16)**(n-depth), "history_lift")
            require((shifted[n]%1 == zero[n]%1) == (n >= depth), "tail_alias")

    # Coherent beta=0 completion: U=-T. Use proved tail upper bound and pi<22/7.
    coherent_bounds = []
    for epoch in (17, 31, 67):
        for h in (1, 2, 3):
            radius = Q(44*abs(h), 105*(epoch+1)**2)
            require(radius < Q(1, 2), "coherent_noncancellation_bound")
            coherent_bounds.append({"A": epoch, "h": h,
                                    "bound_abs_W_minus_1": str(radius)})
        for n in range(epoch, 2*epoch):
            low, high = green_tail_interval(n, 9)
            require(Q(0) < low < high < Q(1, 15*(n+1)**2), "green_tail_enclosure")

    # Finite periodic completion, h=q is identically one before source tail.
    for period in (1, 2, 3, 5):
        denominator = 16**period-1
        beta = Q(7, denominator)
        for n in range(3*period+1):
            require((16**(n+period)*beta)%1 == (16**n*beta)%1, "periodic_completion")
            require((denominator*16**n*beta)%1 == 0, "periodic_detecting_character")

    # Homometric measures: exact autocorrelation, hence every Fourier magnitude.
    first, second = (0, 1, 4, 6), (0, 1, 3, 7)
    a, b = autocorrelation(first, 12), autocorrelation(second, 12)
    require(a == b, "phase_blind_homometry")
    require(first != second, "phase_blind_homometry")
    require(not any(set(second) == {(sign*x+shift)%12 for x in first}
                    for sign in (-1, 1) for shift in range(12)), "phase_blind_homometry")

    # Independently rotated gauges can manufacture each finite Haar grid.
    for modulus in (7, 11, 17, 31):
        raw = (Q(0),)*modulus
        gauges = tuple(Q(j, modulus) for j in range(modulus))
        readings = tuple((x+g)%1 for x, g in zip(raw, gauges))
        require(len(set(readings)) == modulus, "rotating_gauge")
        require(all((y-g)%1 == x for x, g, y in zip(raw, gauges, readings)), "rotating_gauge")
        require(all((y-g)%1 == 0 for g, y in zip(gauges, readings)), "joint_character_one")

    # Changed-source 2-adic Haar shadow H(n), never claimed original BBP.
    def shadow(n):
        return Q(n, (2*n-1)**4)
    for bits in range(1, 10):
        modulus = 2**bits
        residues = [(shadow(n).numerator*pow(shadow(n).denominator, -1, modulus))%modulus
                    for n in range(modulus)]
        require(sorted(residues) == list(range(modulus)), "padic_shadow")
    require(shadow(0) == 0, "padic_shadow")
    for n in (17, 31, 67, 131):
        require(0 < shadow(n) <= Q(1, n**3), "padic_shadow_real_decay")
        require(shadow(n)-16*shadow(n-1) != source(n), "padic_shadow_wrong_source")

    # CB-3 finite ingredient, not the full nonstationary construction.
    p = [Q(1, 16)]*16
    p[2] += Q(1, 64)
    p[3] -= Q(1, 64)
    for k in range(7):
        x = Q(1, 2*16**k)
        require(bernoulli_cdf_at_hex_rational(p, x) == x, "cb3_lattice_ingredient")
    repeat = sum((x*x for x in p), Q())
    require(repeat == Q(1, 16)+Q(1, 2048), "cb3_repeat_bias")

    # Any finite horizon can be extended by zeros: finite uniformity is no
    # certificate of a tail limit. Exact word frequencies for de Bruijn order 1.
    prefix = tuple(range(16))*7
    require(Counter(prefix) == {d: 7 for d in range(16)}, "finite_to_infinite_quantifier")
    for tail in (16**3, 16**4):
        freq0 = Q(7+tail, len(prefix)+tail)
        require(freq0 > Q(9, 10), "finite_to_infinite_quantifier")

    adaptive = adaptive_policy_demo()
    require(adaptive["adaptive_conditional_original_parity_winning"] and
            not adaptive["any_fixed_two_probe_word_succeeds"], "existing_adaptive_advantage")
    clone = adaptive_periodic_impersonation()
    require(clone["common_transcript_certified"], "adaptive_periodic_impersonation")
    return {
        "status": "CERTIFIED-FINITE exact controls; universal proofs separately scoped",
        "checks": dict(sorted(checks.items())), "total_checks": sum(checks.values()),
        "conditional_memory": {"seeds": [str(s) for _, _, s in rows],
                               "minimum_memory_states": code.codewords,
                               "fixed_width_bits": code.fixed_width_bits,
                               "largest_physical_fiber": 2,
                               "colors": code.colors, "edges": code.confusability_edges},
        "coherent_control": coherent_bounds,
        "homometric_autocorrelation": a,
        "cb3_scope": "finite exact lattice ingredient only; infinite CB-3 inherited paper proof",
        "cb3_repeat_frequency": str(repeat),
        "adaptive_scope": "replay of existing adaptive_proof_policy.py, not a new theorem",
        "adaptive_periodic_clone": clone,
        "new_pi_cancellation_bound": False, "pi_base16_normality": "OPEN", "RH": "OPEN",
    }


if __name__ == "__main__":
    result = run()
    destination = Path(__file__).with_name("finite_receipt.json")
    destination.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, sort_keys=True))
