"""Exact finite blindness countermodel for global positivity inference.

Q_plus(x) = sum |x_i|^2 and Q_minus(x) = Q_plus(x) - 2|x_M|^2
are two bounded Hermitian forms on ell²(N). For every finite K<M
they agree on the K-coordinate observation subspace. But Q_minus(e_M)=-1.
The proof is elementary; these are countermodels, NOT Weil forms.
No zero, prime or zeta input is used.
"""
from __future__ import annotations
from fractions import Fraction as Q


class PropertyObstructionError(ValueError):
    pass


def _natural(n: int, lo: int = 1) -> int:
    if type(n) is not int or not lo <= n <= 200_000:
        raise PropertyObstructionError("bounded positive integer required")
    return n


def quadratic_value(vector: tuple[Q, ...], negative_index: int | None = None) -> Q:
    """Real rational finite-support quadratic form. Indices are 1-based."""
    if type(vector) is not tuple or any(type(x) not in (int,Q) for x in vector):
        raise PropertyObstructionError("exact finite real rational tuple required")
    if negative_index is not None:
        _natural(negative_index)
    positive = sum((Q(v)*Q(v) for v in vector), Q())
    defect = Q(0) if negative_index is None or negative_index > len(vector) else Q(2)*Q(vector[negative_index-1])**2
    return positive-defect


def invisible_negative_direction(K: int, M: int | None = None) -> dict:
    """Exact witness that one finite positive Gram corner says nothing globally.

    For any K and any M>K, both operators have the same first K by K
    compression I_K; the second operator has an eigenvalue -1 at e_M.
    Both are bounded and self-adjoint of norm 1 on ell²(N).
    """
    K = _natural(K)
    M = _natural(K+1 if M is None else M)
    if M<=K:
        raise PropertyObstructionError("negative direction must be unobserved")
    observed = tuple(Q(1 if i==j else 0) for i in range(K) for j in range(K))
    unit = tuple(Q(0) for _ in range(M-1))+(Q(1),)
    if quadratic_value(unit) != 1 or quadratic_value(unit,M) != -1:
        raise ArithmeticError("incorrect countermodel witness")
    return {
        "observed_horizon":K,
        "unseen_direction":M,
        "positive_compression_gram":tuple(str(v) for v in observed),
        "negative_compression_gram":tuple(str(v) for v in observed),
        "observed_corners_identical":True,
        "positive_form_value_at_unseen_unit":"1",
        "negative_form_value_at_unseen_unit":"-1",
        "both_bounded_selfadjoint_norm_one":True,
        "global_positivity_decidable_from_these_observations":False,
        "source_attested":False,
        "Weil_form_identified":False,
        "nontrivial_zeta_zeros_read":False,
        "RH_proved":False,
    }
