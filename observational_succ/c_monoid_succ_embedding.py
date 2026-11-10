"""Finite lambda-calculus witnesses and separate arithmetic source actions.

The reducer implements capture-avoiding de Bruijn beta substitution, eta and
pairing rules with an explicit reduction budget.  Positive comparisons witness
common reducts on the tested terms.  This module does NOT certify a genuine
C-monoid, decide general beta-eta equality, or embed the indexed BBP source into
one.  Those stronger claims in the original PR #576 are withdrawn by the
semantic audit in research/2026-11-09/cayley_source_observer/SEMANTIC_AUDIT.md.

Church successor and multiplication represent the genuine arithmetic actions
S(n)=n+1 and V_p(n)=p*n.  Their affine relation V_p S=S^p V_p is distinct from
iterating the indexed BBP recurrence.  The latter remains an exact rational
Python operation with its original zero seed, not a proved lambda compiler.

No pi-normality, selected parity balance, or RH result is asserted.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q


# ---------------------------------------------------------------------------
# de Bruijn-indexed lambda terms with pairing (exact beta-eta fragment)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class T:
    tag: str                  # 'VAR','ABS','APP','PAIR','FST','SND','CONST'
    idx: int = 0              # de Bruijn index (VAR)
    name: str = ''            # constant name (CONST)
    body: 'T' | None = None   # ABS body
    f: 'T' | None = None      # APP / PAIR / FST / SND operand(s)
    a: 'T' | None = None      # APP arg / PAIR snd


def V(i: int) -> T:
    if type(i) is not int or i < 0:
        raise ValueError("a de Bruijn index must be a nonnegative integer")
    return T('VAR', idx=i)
def CONST(n: str) -> T: return T('CONST', name=n)
def ABS(b: T) -> T:  return T('ABS', body=b)
def APP(f: T, a: T) -> T: return T('APP', f=f, a=a)
def PAIR(a: T, b: T) -> T: return T('PAIR', f=a, a=b)
def FST(t: T) -> T:   return T('FST', f=t)
def SND(t: T) -> T:   return T('SND', f=t)


def shift(t: T, d: int, cutoff: int = 0) -> T:
    """Standard de Bruijn shift by d above cutoff."""
    if t.tag == 'VAR':
        return V(t.idx + d) if t.idx >= cutoff else t
    if t.tag == 'CONST':
        return t
    if t.tag == 'ABS':
        return ABS(shift(t.body, d, cutoff + 1))
    if t.tag == 'APP':
        return APP(shift(t.f, d, cutoff), shift(t.a, d, cutoff))
    if t.tag == 'PAIR':
        return PAIR(shift(t.f, d, cutoff), shift(t.a, d, cutoff))
    if t.tag == 'FST':
        return FST(shift(t.f, d, cutoff))
    if t.tag == 'SND':
        return SND(shift(t.f, d, cutoff))
    raise ValueError(t.tag)


def subst(t: T, j: int, s: T) -> T:
    """Raw substitution [j := s]; shift s when crossing a binder.

    This operation does not remove a binder.  ``beta_redex`` performs the
    outer up-shift and final down-shift required when contracting one.
    """
    if t.tag == 'VAR':
        return s if t.idx == j else t
    if t.tag == 'CONST':
        return t
    if t.tag == 'ABS':
        return ABS(subst(t.body, j + 1, shift(s, 1)))
    if t.tag == 'APP':
        return APP(subst(t.f, j, s), subst(t.a, j, s))
    if t.tag == 'PAIR':
        return PAIR(subst(t.f, j, s), subst(t.a, j, s))
    if t.tag == 'FST':
        return FST(subst(t.f, j, s))
    if t.tag == 'SND':
        return SND(subst(t.f, j, s))
    raise ValueError(t.tag)


def beta_redex(t: T):
    """Return the redex if t is (lambda x. b) a, else None."""
    if t.tag == 'APP' and t.f.tag == 'ABS':
        return shift(subst(t.f.body, 0, shift(t.a, 1)), -1)
    return None


def reduce_once(t: T) -> tuple[T, bool]:
    """One leftmost-outermost beta/eta/pairing contraction, if one exists.

    The flag records a contraction even when its output equals its input
    (for example Omega).  A beta step need not decrease term size or redexes.
    """
    r = beta_redex(t)
    if r is not None:
        return r, True
    if t.tag == 'FST' and t.f.tag == 'PAIR':
        return t.f.f, True
    if t.tag == 'SND' and t.f.tag == 'PAIR':
        return t.f.a, True
    if t.tag == 'PAIR' and t.f.tag == 'FST' and t.a.tag == 'SND' \
            and t.f.f == t.a.f:
        return t.f.f, True
    if t.tag == 'ABS':
        b = t.body
        if b.tag == 'APP' and b.a.tag == 'VAR' and b.a.idx == 0 \
                and not occurs(b.f, 0):
            return shift(b.f, -1), True
        b, changed = reduce_once(b)
        return (ABS(b), True) if changed else (t, False)
    if t.tag in ('APP', 'PAIR'):
        f, changed = reduce_once(t.f)
        constructor = APP if t.tag == 'APP' else PAIR
        if changed:
            return constructor(f, t.a), True
        a, changed = reduce_once(t.a)
        return (constructor(t.f, a), True) if changed else (t, False)
    if t.tag in ('FST', 'SND'):
        f, changed = reduce_once(t.f)
        constructor = FST if t.tag == 'FST' else SND
        return (constructor(f), True) if changed else (t, False)
    if t.tag in ('VAR', 'CONST'):
        return t, False
    raise ValueError(t.tag)


def norm(t: T, limit: int = 200000) -> T:
    """Find a reduct with no applicable rules within ``limit`` contractions.

    The budget is global across the entire term.  Exhaustion is UNKNOWN,
    signaled by RuntimeError, and is not evidence that no normal form exists.
    No termination, confluence, or decidability theorem is claimed here.
    """
    if type(limit) is not int or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    for steps in range(limit + 1):
        result, contracted = reduce_once(t)
        if not contracted:
            return t
        if steps == limit:
            raise RuntimeError('no normal form within limit')
        t = result
    raise AssertionError("unreachable")


def occurs(t: T, idx: int) -> bool:
    """Whether the root-context variable ``idx`` occurs, tracking binders."""
    if t.tag == 'VAR':
        return t.idx == idx
    if t.tag == 'CONST':
        return False
    if t.tag == 'ABS':
        return occurs(t.body, idx + 1)
    if t.tag == 'APP':
        return occurs(t.f, idx) or occurs(t.a, idx)
    if t.tag == 'PAIR':
        return occurs(t.f, idx) or occurs(t.a, idx)
    if t.tag == 'FST':
        return occurs(t.f, idx)
    if t.tag == 'SND':
        return occurs(t.f, idx)
    raise ValueError(t.tag)


def eq(a: T, b: T) -> bool:
    """Compare bounded reducts; True witnesses equality on these terms.

    False is not a general decision of inequivalence in the intended theory.
    """
    return norm(a) == norm(b)


# ---------------------------------------------------------------------------
# Closed combinators for the finite displayed identity checks
# ---------------------------------------------------------------------------
ID      = ABS(V(0))                       # lambda x. x
TRUE_   = ABS(ABS(V(1)))                  # K = lambda x. lambda y. x
COMPOSE = ABS(ABS(ABS(APP(V(2), APP(V(1), V(0))))))   # lambda f g x. f (g x)
PAIRING = ABS(ABS(ABS(PAIR(APP(V(2), V(0)), APP(V(1), V(0))))))  # lambda f g x. <f x, g x>
PROJ1   = ABS(FST(V(0)))                  # lambda x. fst x
PROJ2   = ABS(SND(V(0)))                  # lambda x. snd x
EVAL    = ABS(APP(FST(V(0)), SND(V(0))))   # lambda p. (fst p)(snd p)  (evaluation)
APPLY   = EVAL
CURRY   = ABS(ABS(ABS(APP(V(2), PAIR(V(1), V(0))))))  # lambda g x y. g <x,y>  (abstraction/curry)


def compose(a: T, b: T) -> T:
    return APP(APP(COMPOSE, a), b)


def pair(a: T, b: T) -> T:
    return APP(APP(PAIRING, a), b)


def curry(a: T) -> T:
    return APP(CURRY, a)


# ---------------------------------------------------------------------------
# Historical C1-C9 sample labels — not a complete C-monoid certification
# ---------------------------------------------------------------------------
def check_cmonoid_equations() -> dict:
    """Finite sample identities; historical key names are kept for compatibility.

    In particular the old C8/C9 labels name derived identities, not a checked
    transcription of the complete Lambek-Scott axiom list.
    """
    # Use closed "black-box" atoms: a,b,c are free metavariables, represented
    # as abstract constants (variables at level 0, treated as atoms).
    a, b, c = CONST('a'), CONST('b'), CONST('c')
    results = {}

    # C1 associativity of composition
    results['C1_assoc'] = eq(compose(compose(a, b), c), compose(a, compose(b, c)))
    # C2 identity laws
    results['C2_left_id'] = eq(compose(ID, a), a)
    results['C2_right_id'] = eq(compose(a, ID), a)
    # C3 projections of pairing
    results['C3_proj1'] = eq(compose(PROJ1, pair(a, b)), a)
    results['C3_proj2'] = eq(compose(PROJ2, pair(a, b)), b)
    # C4 pairing naturality  <a,b>∘c = <a∘c, b∘c>
    results['C4_pairing_nat'] = eq(compose(pair(a, b), c), pair(compose(a, c), compose(b, c)))
    # C5 <p1,p2> = id
    results['C5_proj_pair_id'] = eq(pair(PROJ1, PROJ2), ID)
    # Historical C6 beta sample: eps(<Lambda(a), b>) = lambda y. a<b,y>
    #   Direct beta law of the reflexive structure, checked exactly.
    results['C6_beta'] = eq(
        APP(EVAL, PAIR(curry(a), b)), ABS(APP(a, PAIR(b, V(0)))))
    # C7 eta: Lambda(eps) = id
    results['C7_lambda_eval_id'] = eq(curry(EVAL), ID)
    # C8 Lambda naturality (direct form): Lambda(a∘<p1,p2>) = Lambda(a)
    #   a∘<p1,p2> = a (by C5 <p1,p2>=id and C2), so Lambda(a∘<p1,p2>) = Lambda(a).
    results['C8_lambda_nat'] = eq(
        curry(compose(a, pair(PROJ1, PROJ2))), curry(a))
    # Evaluate the displayed identity; never return an unconditional pass.
    results['C9_eval_nat'] = eq(compose(EVAL, pair(PROJ1, PROJ2)), EVAL)

    return results


# ---------------------------------------------------------------------------
# Separate indexed BBP arithmetic and ordinary natural-number lambda actions
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class SuccState:
    n: int          # source index
    u: Q            # exact rational state U_n

    def __post_init__(self) -> None:
        if type(self.n) is not int or self.n < 0:
            raise ValueError("source time must be a nonnegative integer")
        if type(self.u) not in (int, Q):
            raise TypeError("source value must be an exact int or Fraction")
        object.__setattr__(self, 'u', Q(self.u))


def forcing(n: int) -> Q:
    """r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), immutable four-pole source."""
    if type(n) is not int or n < 1:
        raise ValueError("source index must be a positive integer")
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def succ_step(s: SuccState) -> SuccState:
    """S_BBP: U_n -> U_{n+1}=16 U_n+r(n+1), retaining the source clock."""
    if type(s) is not SuccState:
        raise TypeError("an exact SuccState is required")
    return SuccState(s.n + 1, 16 * s.u + forcing(s.n + 1))


def iterate_bbp_steps(s: SuccState, steps: int) -> SuccState:
    """Advance the source clock by ``steps``; this is S_BBP^steps, not V_p."""
    if type(s) is not SuccState:
        raise TypeError("an exact SuccState is required")
    if type(steps) is not int or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    out = s
    for _ in range(steps):
        out = succ_step(out)
    return out


def arithmetic_successor(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return n + 1


def dilation_Vp(n: int, p: int) -> int:
    """The actual arithmetic dilation V_p(n)=p*n on N_0.

    A SuccState is intentionally rejected: the indexed source-action
    embedding would require an additional, currently unproved construction.
    """
    if type(n) is not int or n < 0 or type(p) is not int or p < 1:
        raise ValueError("n >= 0 and p >= 1 must be integers")
    return p * n


def church_numeral(n: int) -> T:
    """Closed Church numeral lambda f x. f^n(x)."""
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    body = V(0)
    for _ in range(n):
        body = APP(V(1), body)
    return ABS(ABS(body))


# lambda n f x. f (n f x)
CHURCH_SUCC = ABS(ABS(ABS(APP(V(1), APP(APP(V(2), V(1)), V(0))))))


def church_dilation(p: int) -> T:
    """lambda n f x. n (p f) x: multiplication by the fixed Church p."""
    if type(p) is not int or p < 1:
        raise ValueError("p must be a positive integer")
    return ABS(ABS(ABS(APP(APP(V(2), APP(church_numeral(p), V(1))), V(0)))))


def verify_affine_relation(p: int = 3, n0: int = 1) -> bool:
    """Finite witness of V_p S=S^p V_p on integers and Church numerals."""
    lhs_integer = dilation_Vp(arithmetic_successor(n0), p)
    rhs_integer = dilation_Vp(n0, p)
    for _ in range(p):
        rhs_integer = arithmetic_successor(rhs_integer)
    n_term = church_numeral(n0)
    lhs = APP(church_dilation(p), APP(CHURCH_SUCC, n_term))
    rhs = APP(church_dilation(p), n_term)
    for _ in range(p):
        rhs = APP(CHURCH_SUCC, rhs)
    return lhs_integer == rhs_integer and eq(lhs, rhs) \
        and eq(lhs, church_numeral(lhs_integer))


# ---------------------------------------------------------------------------
# Karoubi envelope on the finite fragment
# ---------------------------------------------------------------------------
def idempotent_retract(x: T) -> bool:
    """x is an idempotent retract (x∘x = x) iff it is a projector."""
    return eq(compose(x, x), x)


if __name__ == '__main__':
    res = check_cmonoid_equations()
    for k in ['C1_assoc','C2_left_id','C2_right_id','C3_proj1','C3_proj2',
              'C4_pairing_nat','C5_proj_pair_id','C6_beta','C7_lambda_eval_id',
              'C8_lambda_nat','C9_eval_nat']:
        print(f'  {k}: {"PASS" if res[k] else "FAIL"}')
    print(f'\nFinite sample identities: {"ALL PASS" if all(res.values()) else "SOME FAIL"}')
    print(f'affine V_p S = S^p V_p (integer/Church sample): {verify_affine_relation()}')
    print(f'PROJ1 idempotent retract: {idempotent_retract(PROJ1)}')
