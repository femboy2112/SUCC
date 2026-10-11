"""Lambert-W as a finite-SUCC inverse chart and rooted-tree path completion.

Three distinct operations MUST remain separate:
  1. exact factorial/SUCC and prime valuations (integer witness),
  2. real W_0 inversion of the leading Stirling bulk (approximate seed),
  3. formal rooted-tree recursion whose infinite EGF selects -W_0(-z).

The W inversion is NOT a Gamma inverse, cannot reconstruct hidden
multiplicative histories from scalar mass alone, and does not read the
Euler-connected n=6 source or the completed Weil form. RH remains open.

Only trusted integer/Fraction inputs are accepted on the exact paths.
mpmath is imported lazily for analytic seeds and numeric calibrations.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import Mapping

from .gamma_succ_path import FactorialSuccPath


class LambertPathError(ValueError):
    """The declared branch, exact source or horizon was violated."""


def _stage(n, *, low=1, high=256, name="stage"):
    if type(n) is not int:
        raise LambertPathError(f"{name} must be an exact integer")
    if not low <= n <= high:
        raise LambertPathError(f"{name} outside declared {low}..{high} budget")
    return n


def _fraction(x):
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    raise LambertPathError("Source coefficients must be exact int/Fraction; no floats")


def _mp():
    try:
        import mpmath
    except ImportError as exc:
        raise LambertPathError("Install mpmath for analytic W evaluations") from exc
    return mpmath


def principal_bulk_inverse(y, *, dps=60):
    """Solve y=x(log x-1) with x>e and y>0 using W_0(y/e).

    This is the leading Stirling chart, NOT Gamma inversion.
    """
    mp=_mp()
    with mp.workdps(dps):
        y=mp.mpf(y)
        if not mp.isfinite(y) or y<=0:
            raise LambertPathError("Principal positive-mass chart requires finite y>0")
        return +mp.exp(1+mp.lambertw(y/mp.e,0)).real


def bulk_branches(y, *, dps=60):
    """For -1<y<0, the Stirling bulk has two distinct real preimages.

    y=x(log x-1). Branch 0 yields 1<x<e; branch -1 yields 0<x<1.
    For y=-1 both meet at x=1. Neither is the Gamma recursion.
    """
    mp=_mp()
    with mp.workdps(dps):
        y=mp.mpf(y)
        if not mp.isfinite(y) or not (-1<=y<0):
            raise LambertPathError("Two real branches require -1<=y<0")
        if y == -1:
            return (mp.mpf(1),mp.mpf(1))  # exact fold; avoid branch-roundoff
        result=[]
        for k in (0,-1):
            w=mp.lambertw(y/mp.e,k)
            if abs(mp.im(w))>mp.power(10,-(dps//2)):
                raise LambertPathError("A real W branch was not obtained")
            x=mp.exp(1+mp.re(w))
            result.append(+x)
        return tuple(result)


@dataclass(frozen=True)
class FactorialInverseCertificate:
    """Exact discrete conclusion, even when the W seed was approximate."""

    target: int
    stage: int
    lower_factorial: int
    upper_factorial: int
    lambert_seed: str
    seed_stage: int
    succ_steps_corrected: int
    prime_valuation: tuple[tuple[int,int], ...]

    def verify(self):
        return (
            type(self.target) is int
            and self.stage>=1
            and self.lower_factorial==factorial(self.stage)
            and self.upper_factorial==factorial(self.stage+1)
            and self.lower_factorial<=self.target<self.upper_factorial
            and self.prime_valuation == (
                FactorialSuccPath(self.stage).prime_tower_exponents()
                if self.stage>=2 else ()
            )
        )

    def report(self):
        if not self.verify():
            raise LambertPathError("Exact SUCC/factorial witness invalid")
        return {
            "status":"exact_discrete_inverse_after_succ_correction",
            "factorial_interval":[str(self.lower_factorial),str(self.upper_factorial)],
            "target":str(self.target),
            "rank":self.stage,"w_seed":self.lambert_seed,
            "integer_seed":self.seed_stage,
            "succ_steps_corrected":self.succ_steps_corrected,
            "retained_prime_valuations":list(map(list,self.prime_valuation)),
            "scope":"rank of integer mass, not inverse Gamma or Weil positivity",
        }


def invert_factorial_mass(target, *, max_stage=256, dps=60):
    """Use W as a non-certificate seed; restore SUCC until EXACT factorial bracket.

    Returns unique stage N>=1 with N!<=target<(N+1)!. For target=1 choose
    N=1 despite the 0!=1 convention. A W rounding error cannot invalidate
    the exact result: both inequalities are independently verified.
    """
    _stage(max_stage,low=2,name="maximum factorial horizon")
    if type(target) is not int or target<1:
        raise LambertPathError("Target must be an exact positive integer")
    if target>=factorial(max_stage+1):
        raise LambertPathError("Target requires an index beyond the declared budget")
    if target==1:
        seed=1
        seed_text="not used at the zero logarithmic mass"
    else:
        mp=_mp()
        with mp.workdps(dps):
            y=mp.log(target)
            x=principal_bulk_inverse(y,dps=dps)
            seed_text=mp.nstr(x,25)
            seed=max(1,min(max_stage,int(mp.floor(x))))
    n=seed
    while factorial(n)>target:
        n-=1
    while factorial(n+1)<=target:
        n+=1
    trace=(FactorialSuccPath(n).prime_tower_exponents() if n>=2 else ())
    result=FactorialInverseCertificate(
        target,n,factorial(n),factorial(n+1),seed_text,seed,
        abs(seed-n),trace
    )
    if not result.verify():
        raise ArithmeticError("Failed exact factorial/SUCC inverse")
    return result


def gamma_bulk_defect(n, *, dps=60):
    """Positive Stirling residual log(n!)-n(log n-1), not lost in W seed."""
    _stage(n,low=2)
    mp=_mp()
    with mp.workdps(dps):
        return +(mp.log(factorial(n)) - n*(mp.log(n)-1))


def gamma_defect_succ(n, *, dps=60):
    """EXACT analytic identity: delta_(n+1)-delta_n = 1-n log(1+1/n)."""
    _stage(n,low=2)
    mp=_mp()
    with mp.workdps(dps):
        return +(1 - n*mp.log1p(mp.mpf(1)/n))


def rooted_tree_coefficients(n, *, overrides: Mapping[int,object] | None=None):
    """Finite ordinary power-series coefficients of T=z exp(T), via SUCC.

    In its labeled-species meaning T=X*SET(T); EGF coefficients are
    t_n=n^(n-1)/n!.  This method uses only the recurrence
      t_(n) = 1/(n-1) sum_(k=1)^(n-1) k t_k t_(n-k)
    (from exp(T)'=T'exp(T)), NOT the closed Cayley formula.

    Mutations alter explicit source stages; the corresponding functional
    residual must be checked, never assumed to remain zero.
    """
    _stage(n,low=1,high=128,name="tree SUCC horizon")
    if overrides is None:
        overrides={}
    if not isinstance(overrides,Mapping) or len(overrides)>n:
        raise LambertPathError("Sparse stage mutation map required")
    injected={}
    for k,v in overrides.items():
        _stage(k,low=2,high=n,name="mutated tree stage")
        injected[k]=_fraction(v)
    coeff=[Fraction(0),Fraction(1)]
    for m in range(2,n+1):
        q=sum((Fraction(k)*coeff[k]*coeff[m-k] for k in range(1,m)),
              Fraction(0))/ (m-1)
        coeff.append(injected.get(m,q))
    return tuple(coeff)


def tree_functional_residual(coefficients, stage):
    """At z^n, T-z exp(T) = t_n - (1/(n-1))Σ k t_k t_(n-k).

    A source mutation at its first stage generates a nonzero exact residual.
    """
    if not isinstance(coefficients,tuple) or len(coefficients)<2:
        raise LambertPathError("Expected finite coefficient tuple")
    _stage(stage,low=1,high=len(coefficients)-1,name="tree coefficient index")
    if stage==1:
        return _fraction(coefficients[1])-1
    t=coefficients
    expected=sum((Fraction(k)*t[k]*t[stage-k] for k in range(1,stage)),
                 Fraction())/(stage-1)
    return _fraction(t[stage])-expected


def rooted_tree_succ_ratio(n):
    """t_(n+1)/t_n = ((n+1)/n)^(n-1) -> e, EXACT as a Fraction."""
    _stage(n,high=127,name="tree successor index")
    return Fraction((n+1)**(n-1),n**(n-1))


def leaf_only_extension_count(n):
    """Naive SUCC: attach new label n+1 as LEAF to existing rooted tree.

    This misses trees in which the new label is the root or an internal
    vertex. The full rooted tree count is (n+1)^n > n^n.
    """
    _stage(n,high=127,name="leaf-only stage")
    return n**n


def rooted_tree_count(n):
    _stage(n,high=128,name="rooted tree stage")
    return n**(n-1)


def tree_series_vs_lambert(z, n, *, dps=70, coefficients=None):
    """Compare finite tree-generated series to principal analytic branch.

    Rational 0<z<=1/3 ensures z<1/e. No zero locations are read.
    """
    q=_fraction(z)
    if not Fraction(0)<q<=Fraction(1,3):
        raise LambertPathError("Use certified safe real z in (0,1/3]")
    _stage(n,high=128,name="finite rooted-tree series horizon")
    a=coefficients or rooted_tree_coefficients(n)
    if not isinstance(a,tuple) or len(a)<=n:
        raise LambertPathError("Insufficient source coefficient horizon")
    mp=_mp()
    with mp.workdps(dps):
        zz=mp.mpf(q.numerator)/q.denominator
        partial=mp.fsum(
            (mp.mpf(a[k].numerator)/a[k].denominator)*zz**k
            for k in range(1,n+1)
        )
        analytic=-mp.lambertw(-zz,0)
        rejected_branch=-mp.lambertw(-zz,-1)
        return {
            "truncation":+partial,
            "principal_limit":+analytic,
            "other_real_branch":+rejected_branch,
            "absolute_error":+abs(partial-analytic),
            "scope":"numerical calibration; analytic continuation not inferred from finitely many terms",
        }
