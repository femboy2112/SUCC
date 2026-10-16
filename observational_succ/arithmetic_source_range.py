"""Source range audit on (-1/2,1/2); no source replacement or zero input.

The accompanying FRACTIONAL_SOURCE_RANGE_AUDIT.md gives the analytic domains.
Exact rational controls and Fourier multiplier bounds are separate from the
optional numerical discriminator. Neither the finite spectrum nor quadrature
establishes a fractional range, a continuum residual bound, or the Schur sign.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import atan, exp, expm1, isfinite, log, log1p, sinh
from pathlib import Path

from . import suzuki_legendre_source as L
from .tate_suzuki_shorting import verify_original_suzuki_source

SOURCE_BLOB = "0cc8510b71d178fc79e8d410a86d8b6014cf9178"
SOURCE_COMMIT = "dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc"
KAPPA = F(20699, 1000000)  # Inherited theorem, not re-proved by this module.
SOURCE_PATHS = (
    "AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
    "observational_succ/source_weil_hierarchy.py",
    "observational_succ/suzuki_legendre_source.py",
    "observational_succ/signed_gprime_enclosure.py",
    "observational_succ/tate_suzuki_shorting.py",
    "observational_succ/tate_weighted_bessel_four_schur.py",
    "observational_succ/compact_galerkin.py",
    "observational_succ/four_low_schur_proof_teeth.py",
    "research/2026-10-16/COMPACT_SOURCE_GALERKIN.md",
    "research/2026-10-16/OBSERVER_SCHUR_SOURCE.md",
    "research/2026-10-16/OBSERVER_SCHUR_THEOREMS.md",
    "research/2026-10-16/OBSERVER_SCHUR_ROUND_II.md",
    "reviews/2026-10-16_OBSERVER_SCHUR_HOSTILE_AUDIT.md",
)


class SourceRangeError(ValueError):
    pass


def _rational(x):
    if type(x) not in (int, F):
        raise SourceRangeError("exact int/Fraction required; bool/float rejected")
    return F(x)


def _integer(x, low, high):
    if type(x) is not int or not low <= x <= high:
        raise SourceRangeError(f"integer in [{low}, {high}] required")
    return x


def source_snapshot():
    passport = verify_original_suzuki_source()
    root = Path(__file__).resolve().parents[1]
    return dict(passport, origin_commit=SOURCE_COMMIT,
                sha256={p: sha256((root/p).read_bytes()).hexdigest()
                        for p in SOURCE_PATHS})


def gamma_multiplier_enclosure(frequency, terms=32):
    """Exact whole-tower enclosure for m(xi)=sum 16xi²/[d(d²+4xi²)].

    This is the Fourier multiplier of -g_Gamma'' on zero-extended
    primitives, not a Fourier eigenvalue of the compressed interval D.
    Tail: sum_(j>=J) 16xi²/d³ <= 16xi²/d_J³ + 2xi²/d_J².
    """
    xi = _rational(frequency)
    _integer(terms, 1, 4096)
    verify_original_suzuki_source()
    partial = sum((16*xi*xi / (F(4*j+1)*((4*j+1)**2+4*xi*xi))
                   for j in range(terms)), F())
    d = 4*terms+1
    tail = 16*xi*xi/d**3 + 2*xi*xi/d**2
    return {"frequency": xi, "terms": terms, "lower": partial,
            "upper": partial+tail, "tail_upper": tail,
            "authority": "EXACT_RATIONAL_WHOLE_GAMMA_BOUND",
            "compressed_operator_eigenvalue": False}


def logarithmic_band_lower(bands):
    """Exact growing lower bound m((4J+1)/2) >= sum_(j<J) 2/(4j+1)."""
    _integer(bands, 1, 4096)
    return {"frequency": F(4*bands+1, 2), "bands": bands,
            "lower": sum((F(2, 4*j+1) for j in range(bands)), F()),
            "authority": "EXACT_RATIONAL_BOUND_PLUS_PAPER_DIVERGENCE"}


def polynomial_moments(poly, degree):
    _integer(degree, 0, 40)
    p = tuple(_rational(c) for c in poly)
    if not p or len(p) > 42:
        raise SourceRangeError("nonempty bounded polynomial required")
    return tuple(L.poly_integral((F(),)*k+p, -F(1, 2), F(1, 2))
                 for k in range(degree+1))


def primitive_control(mode=5):
    """Exact VQ -> H0^1 intersect M transport for an unnormalized Legendre."""
    _integer(mode, 5, 28)
    u = L.legendre_polynomial(mode, F(1, 2))
    f = L.poly_primitive_zero_at_left(u, F(1, 2))
    return {"mode": mode, "u": u, "primitive": f,
            "primitive_endpoints": (L.poly_eval(f, -F(1, 2)),
                                    L.poly_eval(f, F(1, 2))),
            "u_moments_through_4": polynomial_moments(u, 4),
            "primitive_moments_through_3": polynomial_moments(f, 3),
            "K_energy": L.poly_integral(L.poly_mul(f, f), -F(1, 2), F(1, 2)),
            "authority": "EXACT_POLYNOMIAL_IDENTITY"}


def _legendre_coefficients(poly):
    return {n: (2*n+1)*L.poly_integral(
                L.poly_mul(poly, L.legendre_polynomial(n, F(1, 2))),
                -F(1, 2), F(1, 2)) for n in range(len(poly))}


def _ou_affine(coefficients, d):
    """Exact A+B exp(-d/2) for a polynomial OU self-pair; no constant mode."""
    if coefficients.get(0, F()):
        raise SourceRangeError("this exact control requires mean-zero polynomial")
    a = b = F()
    for i, ci in coefficients.items():
        for j, cj in coefficients.items():
            if not ci or not cj:
                continue
            aa, bb = L.source_ou_pair_affine(i, j, F(1, 2), F(d, 2))
            a += ci*cj*aa
            b += ci*cj*bb
    return a, b


def gamma_primitive_identity(mode=5, rung=0, boundary_mutant=False):
    """Exact affine-exponential IBP identity, with a retained boundary mutant.

    Correct input f=V L_mode has zero traces. Mutant f=L4 has equal
    nonzero traces, so f' still has mean zero but boundary terms survive.
    Values are (A,B) meaning A+B exp(-(4j+1)/2), not float comparisons.
    """
    _integer(mode, 5, 28)
    _integer(rung, 0, 128)
    if type(boundary_mutant) is not bool:
        raise SourceRangeError("explicit boolean mutation flag required")
    verify_original_suzuki_source()
    f = (L.legendre_polynomial(4, F(1, 2)) if boundary_mutant else
         primitive_control(mode)["primitive"])
    u = L.poly_derivative(f)
    d = 4*rung+1
    uf = _ou_affine(_legendre_coefficients(u), d)
    ff = _ou_affine(_legendre_coefficients(f), d)
    norm = L.poly_integral(L.poly_mul(f, f), -F(1, 2), F(1, 2))
    source_energy = tuple(F(4, d*d)*v for v in uf)
    multiplier_energy = (F(4, d)*norm-ff[0], -ff[1])
    return {"mode": mode, "rung": rung, "boundary_mutant": boundary_mutant,
            "endpoints": (L.poly_eval(f, -F(1, 2)), L.poly_eval(f, F(1, 2))),
            "source_energy_affine": source_energy,
            "primitive_energy_affine": multiplier_energy,
            "difference_affine": tuple(a-b for a, b in zip(source_energy, multiplier_energy)),
            "authority": "EXACT_RATIONAL_AFFINE_EXPONENTIAL_IDENTITY"}


@lru_cache(maxsize=1)
def _source_constants():
    verify_original_suzuki_source()
    src = L._pinned_source()
    tau = float(src.log2_iv().mid())
    return float(src.contact_iv().mid()), tau, tau*float(src.sqrt_inverse(2).mid())


def numerical_gprime(r):
    """Full actual g' away from zero, NUMERICAL ONLY. No zero diagonal patch."""
    r = float(r)
    if not isfinite(r) or not 0 < abs(r) <= 1:
        raise SourceRangeError("nonzero finite separation |r|<=1 required")
    c, tau, w = _source_constants()
    z = exp(-abs(r)/2)
    gamma = -(log1p(z)-log(-expm1(-abs(r)/2)))/2-atan(z)
    value = -4*sinh(abs(r)/2)+c/2+gamma+(w if abs(r) > tau else 0)
    return value if r > 0 else -value


def numerical_gamma_offdiagonal(r):
    """h(r)=sum exp(-(4j+1)r/2); positive r, experimental evaluation."""
    r = float(r)
    if not isfinite(r) or r <= 0:
        raise SourceRangeError("positive finite separation required")
    return exp(-r/2)/(-expm1(-2*r))


def weighted_adjoint(kernel, weights):
    """Adjoint of K_ij*w_j in weighted L2, using conjugation explicitly."""
    import numpy as np
    k = np.asarray(kernel)
    w = np.asarray(weights, dtype=float)
    if k.ndim != 2 or k.shape != (len(w), len(w)) or np.any(w <= 0):
        raise SourceRangeError("square kernel and positive quadrature weights required")
    if not np.all(np.isfinite(k)) or not np.all(np.isfinite(w)):
        raise SourceRangeError("finite quadrature data required")
    return k.conj().T*w[None, :]


def numerical_source_grid(rank=16, nodes_per_panel=16):
    """Split adaptive integration of actual g' against modes 0..rank.

    Endpoint rows are included for flux diagnostics, with zero quadrature
    weight. Interior panels split at shifted true prime wavefronts. All
    scipy error estimates are retained as estimates, never enclosures.
    """
    import numpy as np
    from scipy.integrate import quad_vec
    from scipy.special import eval_legendre
    _integer(rank, 6, 48)
    _integer(nodes_per_panel, 8, 96)
    verify_original_suzuki_source()
    _, tau, _ = _source_constants()
    modes = np.arange(rank+1)
    scales = np.sqrt(2*modes+1)
    roots, weights = np.polynomial.legendre.leggauss(nodes_per_panel)
    cuts = [-.5, .5-tau, 0., tau-.5, .5]
    xs, ws = [], []
    for left, right in zip(cuts, cuts[1:]):
        xs.extend((left+right)/2+(right-left)*roots/2)
        ws.extend((right-left)*weights/2)
    interior = len(xs)
    xs.extend([-.5, .5])
    rows, errors = [], []
    for x in xs:
        def integrand(y):
            delta = x-y
            # quad_vec uses interior Gauss nodes on each split segment.
            # An unexpected exact diagonal is an instrument error, not g'(0)=0.
            return numerical_gprime(delta)*eval_legendre(modes, 2*y)*scales
        splits = sorted({-.5, .5, x, *[t for t in (x-tau, x+tau) if -.5 < t < .5]})
        row, err = quad_vec(integrand, -.5, .5, points=splits[1:-1],
                            epsabs=2e-11, epsrel=2e-11)
        rows.append(row)
        errors.append(float(err))
    x = np.asarray(xs[:interior])
    w = np.asarray(ws)
    t = np.asarray(rows[:interior])
    e = eval_legendre(modes[None, :], 2*x[:, None])*scales
    low_moments = e[:, :4].T@(w[:, None]*t)
    projected = t-e[:, :4]@low_moments
    endpoint_basis = eval_legendre(modes[None, :4], np.asarray([-1., 1.])[:, None])*scales[:4]
    endpoint_flux = np.asarray(rows[interior:])-endpoint_basis@low_moments
    positive_modes = np.arange(1, rank+1)
    primitive = (eval_legendre(positive_modes[None, :]+1, 2*x[:, None])-
                 eval_legendre(positive_modes[None, :]-1, 2*x[:, None]))/(2*np.sqrt(2*positive_modes+1))
    raw_g = -primitive.T@(w[:, None]*t[:, 1:])
    t_matrix = e.T@(w[:, None]*t)
    return {"rank": rank, "nodes_per_panel": nodes_per_panel,
            "x": x, "weights": w, "T_columns": t,
            "R_columns": projected, "endpoint_flux": endpoint_flux,
            "G_raw": raw_g, "K": primitive.T@(w[:, None]*primitive),
            "T_skew_defect": float(np.max(np.abs(t_matrix+t_matrix.T))),
            "G_symmetry_defect": float(np.max(np.abs(raw_g-raw_g.T))),
            "basis_orthogonality_defect": float(np.max(np.abs(e.T@(w[:, None]*e)-np.eye(rank+1)))),
            "inner_error_estimates": errors, "rigorous_error_bound": False}


def numerical_range_discriminator(fit, holdout, ranks=(8, 12, 16)):
    """Freeze relative least squares, evaluate fresh grid, retain raw spectra.

    No finite singular value proves the continuum adjoint has a kernel.
    Fractional moments below are finite compressions, not lower/upper
    bounds for the infinite D functional calculus.
    """
    import numpy as np
    if fit["rank"] != holdout["rank"]:
        raise SourceRangeError("fit and holdout maximum ranks must agree")
    outputs = []
    for n in ranks:
        _integer(n, 6, fit["rank"])
        if n > holdout["rank"]:
            raise SourceRangeError("holdout rank too small")
        fit_r = np.sqrt(fit["weights"])[:, None]*fit["R_columns"][:, :n+1]
        check_r = np.sqrt(holdout["weights"])[:, None]*holdout["R_columns"][:, :n+1]
        high = fit_r[:, 5:]
        target = fit_r[:, 1:5]
        u, _, numerical_rank, singular = np.linalg.lstsq(high, target, rcond=1e-12)
        fit_res = target-high@u
        check_res = check_r[:, 1:5]-check_r[:, 5:]@u
        raw = holdout["G_raw"][:n, :n]
        # Preserve raw asymmetry before the numerical self-adjoint projection.
        g = (raw+raw.T)/2
        d, b = g[4:, 4:], g[4:, :4]
        ev, vectors = np.linalg.eigh(d)
        fractional = {}
        if np.min(ev) > 0:
            transformed = vectors.T@b
            for alpha in (.5, .625, .75, 1.):
                vals = np.sum(np.abs(transformed)**2/ev[:, None]**(2*alpha), axis=0)
                fractional[str(alpha)] = vals.tolist()
        outputs.append({"rank": n, "high_columns": n-4,
                        "least_squares_rank": int(numerical_rank),
                        "singular_values": singular.tolist(),
                        "frozen_response": u.tolist(),
                        "response_column_norms": np.linalg.norm(u, axis=0).tolist(),
                        "fit_residual_gram": (fit_res.conj().T@fit_res).real.tolist(),
                        "holdout_residual_gram": (check_res.conj().T@check_res).real.tolist(),
                        "holdout_column_residual_norms": np.linalg.norm(check_res, axis=0).tolist(),
                        "high_G_eigenvalues": ev.tolist(),
                        "finite_fractional_moments": fractional,
                        "fractional_status": "FINITE_COMPRESSION_EXPERIMENT_NOT_RANGE_PROOF",
                        "fit_to_holdout_drift": float(np.linalg.norm(check_res.conj().T@check_res-fit_res.conj().T@fit_res, 2)),
                        "positive_eigenvalues_not_clipped": bool(np.min(ev) > 0)})
    return {"authority": "EXPERIMENT_ONLY", "runs": outputs,
            "fit_grid": grid_summary(fit), "holdout_grid": grid_summary(holdout),
            "range_dense_from_numerics": False, "fractional_power_membership_proved": False,
            "source_S0_sign": "OPEN", "nontrivial_zero_coordinates_used": False}


def grid_summary(grid):
    return {k: grid[k] for k in ("rank", "nodes_per_panel", "T_skew_defect",
                                 "G_symmetry_defect", "basis_orthogonality_defect",
                                 "inner_error_estimates", "rigorous_error_bound")} | {
        "low_endpoint_flux": grid["endpoint_flux"][:, 1:5].tolist()}


def claim_boundaries():
    """Report proof status; no numeric or hash-based promotion of paper claims."""
    return {"adjoint": "PAPER_DERIVED: R_Q*=-Q T|M; T=g' convolution",
            "dense_range": "CONDITIONAL_PAPER_PROOF: genuine source and inherited D>=kappa K_Q",
            "strong_H01_annihilator_regularity_assumed": False,
            "fractional_D_power_above_half": "OPEN; no implication from bounded H1 map",
            "bounded_relative_upper_D_le_CK": "PAPER_REFUTED_FOR_THIS_SOURCE_BY_LOG_MULTIPLIER",
            "quantitative_residual_rate": "OPEN",
            "source_S0_sign": "OPEN", "RH_PROVED": False,
            "kernel_proof": False}
