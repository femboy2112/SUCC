"""Exact certificates for the authentic Suzuki Gamma tail.

The universal inequalities are proved in INSTITUTE_ARITHMETIC_ANALYSIS.md.
The finite prefix oracle is a separate rational calibration, not a substitute
for that proof. No zeros, floating point, or presumed Weil positivity enter.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import io


SOURCE_BLOB = "0cc8510b71d178fc79e8d410a86d8b6014cf9178"
SOURCE_PATH = "observational_succ/source_weil_hierarchy.py"
PR177_COMMIT = "f309d9104ba480c1999c962af1df7c50f19e1bfe"


def rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer/Fraction required")
    return Q(value)


def cutoff(value):
    if type(value) is not int or value < 1:
        raise ValueError("J must be a positive integer")
    return value


def log_interval(value, terms=64):
    """Independent outward rational log via dyadic reduction and atanh."""
    value = rational(value)
    if value <= 0 or type(terms) is not int or terms < 1:
        raise ValueError("positive log argument and positive term count")
    if value < 1:
        lower, upper = log_interval(1 / value, terms)
        return -upper, -lower

    def unit(x):
        z = (x - 1) / (x + 1)
        total = sum((2 * z ** (2 * k + 1) / (2 * k + 1)
                     for k in range(terms)), Q())
        remainder = 2 * z ** (2 * terms + 1) / (
            (2 * terms + 1) * (1 - z * z))
        return total, total + remainder

    power = 0
    while value >= 2:
        value /= 2
        power += 1
    lo, hi = unit(value)
    l2, u2 = unit(Q(2))
    return lo + power * l2, hi + power * u2


def logarithm_linear_certificate():
    """Certify log(1+y²) <= 13y/16 for every y>=0 by calculus.

    F'= (13y²-32y+13)/(16(1+y²)). Its only positive local
    minimum is (16+sqrt(87))/13. Enclose that point independently.
    """
    left, right = Q(1948, 1000), Q(1949, 1000)
    polynomial = lambda y: 13 * y * y - 32 * y + 13
    assert left > Q(16, 13)
    assert polynomial(left) < 0 < polynomial(right)
    _, log_upper = log_interval(1 + right * right)
    margin = Q(13, 16) * left - log_upper
    assert margin > Q(1, 100)
    return {"local_minimum_left": left, "local_minimum_right": right,
            "positive_local_minimum_margin": margin,
            "constant": Q(13, 16)}


def gamma_coefficients(J):
    """Certified H1/H2 action coefficients; H2 assumes zero extension H²."""
    J = cutoff(J)
    d = 4 * J + 1
    old_h1 = Q(1, d) + Q(4, d * d)
    old_h2 = Q(2, d * d) + Q(16, d ** 3)
    h1 = Q(13, 16 * (d - 2))
    midpoint_h2 = Q(2, (d - 2) ** 2)
    return {"J": J, "d": d, "old_H1": old_h1, "new_H1": h1,
            "old_H2": old_h2, "midpoint_H2": midpoint_h2,
            "selected_H2": min(old_h2, midpoint_h2),
            "H1_improvement_fraction": 1 - h1 / old_h1,
            "H2_improvement_fraction": 1 - min(old_h2, midpoint_h2) / old_h2}


def gamma_prefix(J, count, frequency):
    J = cutoff(J)
    if type(count) is not int or count < 0:
        raise ValueError("nonnegative prefix count")
    x = rational(frequency)
    return sum((16 * x * x / (Q(4 * j + 1) *
                ((4 * j + 1) ** 2 + 4 * x * x))
                for j in range(J, J + count)), Q())


def independent_tail_interval(J, frequency, prefix=1024):
    """Prefix plus monotone integral test, separate from midpoint convexity."""
    J = cutoff(J)
    x = rational(frequency)
    total = gamma_prefix(J, prefix, x)
    d = 4 * (J + prefix) + 1
    loglo, loghi = log_interval(1 + 4 * x * x / (d * d))
    next_term = gamma_prefix(J + prefix, 1, x)
    return total + loglo / 2, total + loghi / 2 + next_term


def logarithmic_envelope(J, frequency):
    J = cutoff(J)
    x = rational(frequency)
    d = 4 * J + 1
    lower, _ = log_interval(1 + 4 * x * x / (d * d))
    _, upper = log_interval(1 + 4 * x * x / ((d - 2) ** 2))
    # Convex trapezoidal inequality supplies the extra half first term.
    return lower / 2 + gamma_prefix(J, 1, x) / 2, upper / 2


def source_identity(root=None):
    root = Path(root) if root else Path(__file__).resolve().parents[1]
    content = (root / SOURCE_PATH).read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
    if blob != SOURCE_BLOB:
        raise ValueError("original signed source blob mismatch")
    return {"path": SOURCE_PATH, "git_blob": blob,
            "source_parameter": "d_j=4j+1; alpha_j=d_j/2; one real Gamma"}


def receipt():
    calibration = []
    for J in (1, 2, 8, 24):
        for x in (Q(0), Q(1, 100), Q(1), Q(7), Q(100)):
            lo, hi = independent_tail_interval(J, x)
            elo, ehi = logarithmic_envelope(J, x)
            assert elo <= hi and lo <= ehi
            if x:
                # Stronger independent check: the complete prefix-oracle
                # upper itself fits inside both proved derivative budgets.
                coeff = gamma_coefficients(J)
                assert hi <= coeff["new_H1"] * abs(x)
                assert hi <= coeff["selected_H2"] * x * x
            calibration.append({"J": J, "frequency": str(x),
                                "independent_interval_inside_derivative_bounds": True})
    return {"source": source_identity(),
            "linear_log_certificate": logarithm_linear_certificate(),
            "coefficient_comparison": [gamma_coefficients(J) for J in (1, 2, 4, 8, 24, 64)],
            "independent_prefix_calibrations": calibration,
            "authority": "PAPER_PROOF_PLUS_EXACT_RATIONAL_CERTIFICATES",
            "full_S4_sign_decided": False, "RH_proved": False}


def replay_pr177(J=8, M=80):
    """Read-only exact archive replay; capped at 1 GiB and 240 CPU seconds.

    Reuse a single original source evaluation, then recompute only its
    changed error budget on identical rational fitted trials. Archive code
    is never installed into this branch. Source-conditional authority stays.
    """
    cutoff(J)
    if J > 24 or type(M) is not int or not 1 <= M <= 256:
        raise ValueError("bounded replay requires J<=24 and 1<=M<=256")
    archive = subprocess.run(
        ["git", "archive", PR177_COMMIT, "observational_succ"],
        check=True, stdout=subprocess.PIPE).stdout
    root = Path(__file__).resolve().parents[1]
    program = r'''
import json, resource, sys, time
import mpmath
from fractions import Fraction as Q
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
resource.setrlimit(resource.RLIMIT_CPU, (240, 240))
sys.path.insert(0, sys.argv[1])
from observational_succ import original_continuum_residual as R
from observational_succ import clamped_k_residual_bridge as B
sys.path.insert(0, sys.argv[2])
from scripts.institute_schur_probe import gamma_coefficients, PR177_COMMIT
started = time.monotonic()
J, M = int(sys.argv[3]), int(sys.argv[4])
old = R.source_residual_schur_trial(J=J, M=M, P=18, fit=True)
comparison = {}
for parity, data in old["four_original_parity_Schur_blocks"].items():
    old_epsilon_sq = Q(0)
    new_epsilon_sq = Q(0)
    tail_detail = []
    for index, coeff, finite, oldtail in zip(
        data["indices"], data["fitted_high_coefficients"],
        data["finite_source_action_error_each"],
        data["genuine_omitted_Gamma_action_error_each"]):
        h = R.high_boundary_match(index, Q(coeff))["h"]
        assert all(B.value(p,e)==0 for p in (h,B.derivative(h))
                   for e in (-Q(1,2),Q(1,2)))
        constants = gamma_coefficients(J)
        new_h1 = constants["new_H1"] * B.sqrt_up(R.derivative_norm_squared(h))
        new_h2 = constants["selected_H2"] * B.sqrt_up(
            R.norm_squared(B.derivative(B.derivative(h))))
        newtail = min(new_h1, new_h2)
        oldtail, finite = Q(oldtail), Q(finite)
        assert R.authentic_Gamma_tail_action_dual(h,J)["selected"] == oldtail
        assert newtail <= oldtail
        old_epsilon_sq += (finite + oldtail)**2
        new_epsilon_sq += (finite + newtail)**2
        tail_detail.append({"mode":index,"old_action_upper":str(oldtail),
                            "new_action_upper":str(newtail)})
    # eta=1/4 in the archived run: only the paid tail uncertainty changes.
    gain = 5*(old_epsilon_sq-new_epsilon_sq)/Q(data["source_kappa"])
    before = [[Q(v) for v in row] for row in
              data["genuine_source_2x2_Schur_Loewner_lower"]]
    after = [[before[i][j]+(gain if i==j else 0) for j in range(2)]
             for i in range(2)]
    def psd(m):
        return m[0][0]>=0 and m[1][1]>=0 and m[0][0]*m[1][1]>=m[0][1]**2
    assert gain >= 0
    comparison[parity]={"positive_Loewner_gain_scalar":str(gain),
        "strict_gain":gain>0,
        "old_lower":before,"new_lower":after,
        "old_lower_PSD":psd(before),"new_lower_PSD":psd(after),
        "same_source_same_trial_same_finite_action":True,"tail_actions":tail_detail}
result={"archive_commit":PR177_COMMIT,"source_blob":R.SOURCE_SHA,
    "J":J,"M":M,"P":18,"eta":"1/4",
    "parity_comparison":comparison,"seconds":time.monotonic()-started,
    "source_coercivity_authority":"INHERITED_SOURCE_CONDITIONAL",
    "all_four_sign_certified":all(v["new_lower_PSD"] for v in comparison.values()),
    "RH_proved":False,"python":sys.version,"mpmath":mpmath.__version__,
    "peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    "address_space_limit_bytes":1024**3,"cpu_limit_seconds":240}
print(json.dumps(result,default=str,sort_keys=True))
'''
    with tempfile.TemporaryDirectory(prefix="succ-institute-pr177-") as tmp:
        # The Git archive is locally produced from a fixed reviewed commit.
        with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
            if any(not (m.name == "observational_succ" or
                        m.name.startswith("observational_succ/"))
                   or ".." in Path(m.name).parts for m in tar.getmembers()):
                raise ValueError("unexpected archive member")
            tar.extractall(tmp)
        child = subprocess.run([sys.executable, "-c", program, tmp, str(root), str(J), str(M)],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, timeout=270, cwd=tmp)
        return json.loads(child.stdout)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--replay-pr177", action="store_true")
    parser.add_argument("--gamma-cutoff", type=int, default=8)
    parser.add_argument("--taylor-degree", type=int, default=80)
    args = parser.parse_args()
    data = receipt()
    if args.replay_pr177:
        data["source_Schur_replay"] = replay_pr177(args.gamma_cutoff, args.taylor_degree)
    output = json.dumps(data, indent=2, sort_keys=True, default=str) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
