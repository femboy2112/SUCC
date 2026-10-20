"""Mason-Stothers (polynomial abc) as a Proof Forge certificate.

THEOREM (Stothers 1981 / Mason 1984 -- CLASSICAL, not original to SUCC).
Let K be a field and A,B,C in K[x] nonzero, pairwise coprime, not all constant,
with A + B = C, and suppose char K = 0 (or char K > max degree). Then

        max(deg A, deg B, deg C) <= deg rad(ABC) - 1,

where rad(P) is the product of the distinct monic irreducible factors of P
(= the squarefree part P / gcd(P, P')).

PRINCIPAL INVARIANT: the Wronskian W = A'B - AB'. Because A+B=C it also equals
A'C - AC' and -(B'C - BC'); all three pairwise Wronskians agree up to sign. In
char 0, W != 0 (W=0 <=> (A/B)'=0 <=> A/B constant <=> all constant, excluded),
and for every irreducible P we get v_P(W) >= v_P(ABC) - 1, hence
(ABC)/rad(ABC) | W. Degree comparison on W (deg W <= deg A + deg B - 1 and its
two cyclic forms) then yields the bound.

This module represents each proof step as an *independently checkable* claim
with an exact computational oracle (sympy over an exact field), plus the exact
counterexamples when a hypothesis is dropped, including the characteristic-p
collapse A=x^p, B=1, C=(x+1)^p where W vanishes identically.

The SUCC contribution is the proof-certificate representation only; the
mathematics is classical. Status: CLASSICAL. RH/abc for integers: untouched and
OPEN (see `integer_transfer_obstruction`). No float is ever a certificate.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import sympy as sp


class MasonStothersError(ValueError):
    pass


# --------------------------------------------------------------------------
# exact polynomial helpers (sympy Poly over an exact field)
# --------------------------------------------------------------------------

def _poly(expr, x, domain):
    p = sp.Poly(expr, x, domain=domain)
    return p


def poly_derivative(P: sp.Poly) -> sp.Poly:
    return P.diff(P.gens[0])


def wronskian(A: sp.Poly, B: sp.Poly) -> sp.Poly:
    """W(A,B) = A'B - AB' as an exact Poly."""
    return poly_derivative(A) * B - A * poly_derivative(B)


def poly_radical(P: sp.Poly, x, domain) -> Tuple[sp.Poly, int]:
    """Return (rad, deg rad): product of distinct monic irreducible factors.

    Computed as the squarefree part P / gcd(P, P') (valid in char 0 and when
    char > degree); made monic. Degree of the radical is exact.
    """
    if P.is_zero:
        raise MasonStothersError("radical of the zero polynomial is undefined")
    Pp = poly_derivative(P)
    if Pp.is_zero:
        # char p case where P' == 0 (e.g. P = x^p): gcd(P,P')=P, squarefree
        # part collapses. Signal degenerate radical by returning P made monic.
        g = P
    else:
        g = sp.gcd(P, Pp)
    rad = P.quo(g)
    rad = rad.monic()
    return rad, rad.degree()


def pairwise_coprime(polys: List[sp.Poly]) -> bool:
    for i in range(len(polys)):
        for j in range(i + 1, len(polys)):
            if sp.gcd(polys[i], polys[j]).degree() > 0:
                return False
    return True


# --------------------------------------------------------------------------
# the certificate
# --------------------------------------------------------------------------

@dataclass
class ProofStep:
    claim: str
    ok: bool
    detail: str = ""


@dataclass
class MasonStothersCertificate:
    degrees: Dict[str, int]
    deg_rad_ABC: int
    max_deg: int
    bound_rhs: int                   # deg rad(ABC) - 1
    W_is_zero: bool
    wronskian_forms_agree: bool
    divisibility_holds: bool         # (ABC)/rad(ABC) | W
    bound_holds: bool                # max deg <= deg rad(ABC) - 1
    steps: List[ProofStep] = field(default_factory=list)
    hypotheses_ok: bool = True
    note: str = ""

    @property
    def verified(self) -> bool:
        return (self.hypotheses_ok and not self.W_is_zero
                and self.wronskian_forms_agree and self.divisibility_holds
                and self.bound_holds)

    def as_record(self) -> Dict[str, object]:
        return {
            "degrees": dict(self.degrees),
            "deg_rad_ABC": self.deg_rad_ABC,
            "max_deg": self.max_deg,
            "bound_rhs": self.bound_rhs,
            "W_is_zero": self.W_is_zero,
            "wronskian_forms_agree": self.wronskian_forms_agree,
            "divisibility_holds": self.divisibility_holds,
            "bound_holds": self.bound_holds,
            "hypotheses_ok": self.hypotheses_ok,
            "verified": self.verified,
            "note": self.note,
            "steps": [(s.claim, s.ok, s.detail) for s in self.steps],
        }


def mason_stothers_certificate(A_expr, B_expr, C_expr=None, *, x=None,
                               domain=sp.QQ, require_hypotheses: bool = True
                               ) -> MasonStothersCertificate:
    """Build an exact Mason-Stothers certificate for A + B = C over `domain`.

    If C_expr is None it is taken as A+B. `domain` is an exact sympy field
    (QQ default; use sp.GF(p) for characteristic p to exhibit the collapse).
    With require_hypotheses=False the degenerate/counterexample cases are still
    reported (verified will be False), which is how the char-p and
    coprimality-failure controls are exercised.
    """
    x = x or sp.Symbol("x")
    A = _poly(A_expr, x, domain)
    B = _poly(B_expr, x, domain)
    C = _poly(C_expr if C_expr is not None else A_expr + B_expr, x, domain)
    steps: List[ProofStep] = []

    # --- hypotheses ---
    nonzero = not (A.is_zero or B.is_zero or C.is_zero)
    sum_ok = (A + B - C).is_zero
    not_all_const = max(A.degree(), B.degree(), C.degree()) > 0
    coprime = pairwise_coprime([A, B, C])
    hyp_ok = nonzero and sum_ok and not_all_const and coprime
    steps.append(ProofStep("A,B,C nonzero", nonzero))
    steps.append(ProofStep("A + B = C", sum_ok))
    steps.append(ProofStep("not all constant", not_all_const))
    steps.append(ProofStep("pairwise coprime", coprime))
    if require_hypotheses and not hyp_ok:
        raise MasonStothersError(
            f"hypotheses failed: nonzero={nonzero} sum={sum_ok} "
            f"not_all_const={not_all_const} coprime={coprime}"
        )

    # --- Wronskian + its three forms (coherence of the invariant) ---
    W_ab = wronskian(A, B)
    W_ac = wronskian(A, C)
    W_bc = wronskian(B, C)
    # expected: W_ab == W_ac == -W_bc  (since A+B=C)
    forms_agree = (W_ab - W_ac).is_zero and (W_ab + W_bc).is_zero
    steps.append(ProofStep("W(A,B)=W(A,C)=-W(B,C)", forms_agree,
                           "three Wronskian forms agree up to sign"))
    W_zero = W_ab.is_zero
    steps.append(ProofStep("W != 0 (needs char 0 / char>deg)", not W_zero,
                           "W=0 is exactly the char-p / linear-dependence collapse"))

    # --- radical and divisibility ---
    ABC = A * B * C
    try:
        rad, deg_rad = poly_radical(ABC, x, domain)
    except MasonStothersError:
        rad, deg_rad = None, -1
    # M = ABC / rad(ABC) = product P^{v_P-1}; claim M | W
    divis = False
    if rad is not None and not W_zero:
        M = ABC.quo(rad)
        # claim is M | W, i.e. W mod M == 0 (NOT M mod W). deg M <= deg W always.
        divis = W_ab.rem(M).is_zero if not M.is_zero else False
        steps.append(ProofStep("(ABC)/rad(ABC) | W", divis,
                               f"deg M={M.degree()}, deg W={W_ab.degree()}"))
    else:
        steps.append(ProofStep("(ABC)/rad(ABC) | W", False,
                               "skipped: W=0 or radical undefined"))

    # --- degree comparison ---
    degs = {"A": A.degree(), "B": B.degree(), "C": C.degree()}
    max_deg = max(degs.values())
    bound_rhs = deg_rad - 1 if deg_rad >= 0 else -10**9
    bound_holds = max_deg <= bound_rhs
    steps.append(ProofStep("max deg <= deg rad(ABC) - 1", bound_holds,
                           f"max_deg={max_deg}, deg_rad-1={bound_rhs}"))

    note = ""
    if W_zero:
        note = ("Wronskian vanishes: the proof mechanism has collapsed "
                "(characteristic-p freshman's-dream regime or linear dependence). "
                "The degree bound is NOT asserted here.")
    return MasonStothersCertificate(
        degrees=degs, deg_rad_ABC=deg_rad, max_deg=max_deg, bound_rhs=bound_rhs,
        W_is_zero=W_zero, wronskian_forms_agree=forms_agree,
        divisibility_holds=divis, bound_holds=bound_holds, steps=steps,
        hypotheses_ok=hyp_ok, note=note,
    )


# --------------------------------------------------------------------------
# the honest integer-transfer obstruction (abc stays OPEN)
# --------------------------------------------------------------------------

def integer_transfer_obstruction() -> Dict[str, str]:
    """Why the Wronskian proof does NOT transfer to the integers (abc OPEN).

    Returns a structured statement of the obstruction. This is an *account*, not
    a theorem; no integer abc result is claimed.
    """
    return {
        "claim_status": "abc for integers is OPEN; no analogue is proved here",
        "obstruction_1_no_derivation": (
            "Every ring derivation D: Z -> Z is identically zero. D(1)=D(1*1)="
            "2D(1) forces D(1)=0, and additivity forces D(n)=0 for all n. So the "
            "Wronskian W = a'b - ab' is identically 0 over Z -- the invariant that "
            "carries the whole polynomial proof simply does not exist."
        ),
        "obstruction_2_no_size_drop": (
            "deg plays the role of the archimedean valuation at infinity, and the "
            "polynomial proof crucially uses deg(P') = deg(P) - 1: differentiation "
            "drops size by exactly one while respecting Leibniz. There is no "
            "operation on Z that reduces log|n| by a bounded amount while obeying a "
            "product rule. log|n| is the integer analogue of deg, but nothing plays "
            "the role of d/dx."
        ),
        "obstruction_3_p_derivations_are_local": (
            "Buium p-derivations delta_p (delta_p(x) = (x^p - (something))/p) give an "
            "arithmetic differential calculus, but they are p-adic and see one prime "
            "at a time; there is no single global object playing the role of the "
            "Wronskian whose archimedean size is controlled. The arithmetic "
            "derivative n' (p'=1, Leibniz) exists but has no deg-drop property and "
            "can grow, so it yields no Mason-Stothers analogue either."
        ),
        "consequence": (
            "Mason-Stothers is a one-page theorem; integer abc is a famous open "
            "problem precisely because the derivation/size-drop mechanism has no "
            "faithful archimedean integer counterpart."
        ),
    }
