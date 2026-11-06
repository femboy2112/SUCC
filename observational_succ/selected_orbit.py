"""Shared exact selected-orbit framework for π-frontier research (Main XX).

One place for the objects every selected-orbit probe needs, built on the
formally backed forcing core :mod:`observational_succ.duck_bbp` (its tail
bound is the Lean-checked ``formal/duck_pi`` statement):

* exact reduced states ``x_n = {U_n(s)}`` for a rational seed ``s`` (default
  the literal ``U_0 = 0``), with the original four signed poles;
* source sums ``S_k(n)``, rigorous rational enclosures of the Green tail
  ``T_n``, admissibility of critical carry triples;
* the #522 critical carry bit by its DEFINITION (θ, δ) and by the exact
  carry–interval identity CB-1 (``research/2026-11-05/main_xx_forge``), so
  every caller can cross-check the two;
* the exact innovation ``J_{A,m,k}`` and Weyl coefficients ``c_A(h)``;
* a deterministic receipt writer that records sha256 of the files a result
  depends on and refuses unknown claim-status labels.

Nothing here is evidence of normality.  Finite values are OBSERVED-FINITE.
Irrational seeds (the coherent counterseed ``-π/16``, non-normal
countermodels) are handled in the completed-orbit gauge by callers; this
module keeps rational seeds exact.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Mapping

from observational_succ import duck_bbp

Forcing = Callable[[int], Fraction]

#: docs/METHOD.md ledger labels plus the finer research labels used in dossiers.
STATUS_LABELS = frozenset({
    "CLASSICAL", "PROVED LOCAL", "TESTED MODEL", "HYPOTHESIS", "REFUTED", "UNVERIFIED",
    "PROVED", "PROVED-CONDITIONAL", "EQUIVALENT-REFORMULATION", "CERTIFIED-FINITE",
    "OPEN", "OBSERVED-FINITE", "CONJECTURE",
})


def original_forcing(n: int) -> Fraction:
    """r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), the immutable four-pole source."""
    return duck_bbp.forcing(n)


def four_pole_forcing(n: int, weights=(4, -2, -1, -1), poles=(7, 4, 3, 2)) -> Fraction:
    """Explicit four-pole form (used for pole MUTANT controls only)."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be an integer >= 1")
    return sum((Fraction(w, 8 * n - p) for w, p in zip(weights, poles)), Fraction())


class SelectedOrbit:
    """Exact orbit x_n={U_n(s)}, U_0=s, U_n=16U_{n-1}+r(n), rational seed."""

    def __init__(self, seed: Fraction | int = 0, forcing: Forcing = original_forcing):
        self.seed = Fraction(seed)
        self.forcing = forcing
        self._states = [self.seed % 1]

    def state(self, n: int) -> Fraction:
        if type(n) is not int or n < 0:
            raise ValueError("n must be an integer >= 0")
        while len(self._states) <= n:
            m = len(self._states)
            self._states.append((16 * self._states[-1] + self.forcing(m)) % 1)
        return self._states[n]

    def source_sum(self, k: int, n: int) -> Fraction:
        """S_k(n)=sum_{j=1}^k 16^(k-j) r(n+j); U_{n+k}=16^k U_n+S_k(n)."""
        total = Fraction()
        for j in range(1, k + 1):
            total = 16 * total + self.forcing(n + j)
        return total

    # --- critical carry (PR #522 HS-01/HS-08) -------------------------------
    def carry_by_definition(self, n: int, m: int, k: int) -> tuple[int, Fraction]:
        """(b, δ) from θ={16^(m+k) x_n}, δ={16^m S_k(n)}, b=1[θ+δ>=1]."""
        theta = (16 ** (m + k) * self.state(n)) % 1
        delta = (16 ** m * self.source_sum(k, n)) % 1
        return int(theta + delta >= 1), delta

    def carry_window(self, n: int, m: int, k: int) -> tuple[Fraction, Fraction]:
        """CB-1 window [S_m(n+k), S_{m+k}(n)) (valid when S_{m+k}(n)<1, r>0)."""
        return self.source_sum(m, n + k), self.source_sum(m + k, n)

    def carry_by_window(self, n: int, m: int, k: int) -> tuple[int, Fraction]:
        eps, sigma = self.carry_window(n, m, k)
        if not sigma < 1:
            raise ValueError("CB-1 requires S_(m+k)(n) < 1")
        y = self.state(n + m + k)
        return int(eps <= y < sigma), sigma - eps

    def innovation(self, A: int, m: int, k: int, by: str = "window") -> Fraction:
        """Exact J_{A,m,k}=A^-1 sum_{n=A}^{2A-1}(b-δ)."""
        f = self.carry_by_window if by == "window" else self.carry_by_definition
        total = Fraction()
        for n in range(A, 2 * A):
            b, delta = f(n, m, k)
            total += b - delta
        return total / A

    # --- Weyl coefficients ------------------------------------------------------
    def weyl_coefficient(self, A: int, h: int, dps: int = 40):
        """c_A(h)=A^-1 sum e(h x_n), evaluated with LOCALLY scoped precision."""
        import mpmath as mp
        with mp.workdps(dps):
            acc = mp.mpc(0)
            for n in range(A, 2 * A):
                x = self.state(n)
                acc += mp.expjpi(2 * h * mp.mpf(x.numerator) / x.denominator)
            return acc / A


def green_tail_interval(n: int, depth: int = 12, forcing: Forcing = original_forcing) -> tuple[Fraction, Fraction]:
    """Rigorous rational enclosure of T_n=sum_{j>=1}16^-j r(n+j) (original source)."""
    if forcing is not original_forcing:
        raise ValueError("the analytic tail budget is proved for the original forcing only")
    return duck_bbp.tail_interval(n, depth)


def admissible(A: int, m: int, k: int, depth: int = 12) -> bool:
    """16^(m+k) T_n <= 1 for every n in [A,2A), certified by the upper enclosure."""
    d = m + k
    return all(16 ** d * green_tail_interval(n, depth)[1] <= 1 for n in range(A, 2 * A))


def critical_depths(A: int, depth: int = 12) -> list[int]:
    """All d>=2 with (A, m, d-m) admissible for every split (admissibility depends on d only)."""
    out, d = [], 2
    while admissible(A, 1, d - 1, depth):
        out.append(d)
        d += 1
    return out


def sha256_file(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_receipt(path: str | Path, payload: Mapping, *, claims: Mapping[str, str],
                  depends_on: Iterable[str | Path] = (), root: str | Path = ".") -> dict:
    """Deterministic JSON receipt: payload + claim statuses + sha256 of dependencies.

    ``claims`` maps claim ids to status labels; unknown labels are rejected so
    a receipt can never silently promote a status.  Fractions are serialised
    as exact ``"p/q"`` strings.
    """
    bad = {cid: s for cid, s in claims.items() if s not in STATUS_LABELS}
    if bad:
        raise ValueError(f"unknown status labels: {bad}")
    root = Path(root)

    def enc(v):
        if isinstance(v, Fraction):
            return f"{v.numerator}/{v.denominator}"
        if isinstance(v, Mapping):
            return {str(k): enc(x) for k, x in v.items()}
        if isinstance(v, (list, tuple)):
            return [enc(x) for x in v]
        return v

    doc = {
        "claims": dict(sorted(claims.items())),
        "depends_on": {str(p): sha256_file(root / p) for p in sorted(map(str, depends_on))},
        "payload": enc(payload),
        "pi_normality": "OPEN",
    }
    Path(path).write_text(json.dumps(doc, indent=1, sort_keys=True) + "\n")
    return doc
