"""Exact local-uniform-rule certificates for shifted Lonely Runner replacements.

The checker is independent of any finite-time cover sampler.  It checks the
finite rational tangent intervals equivalent to locality for affine-in-delta
phases, including all admissible scales and arbitrarily large N.  See the
proof in research/2026-10-28/lonely_runner/BETA_UNIFORM.md. No ordinary LR claim is made.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd,lcm


@dataclass(frozen=True)
class AffineRunner:
    velocity: int
    alpha: F
    beta: F

    def __post_init__(self):
        if type(self.velocity) is not int or self.velocity < 1:
            raise ValueError('positive integer velocity required')
        if type(self.alpha) not in (int,F) or type(self.beta) not in (int,F):
            raise TypeError('exact rational phase coefficients required')
        object.__setattr__(self,'alpha',F(self.alpha)%1)
        object.__setattr__(self,'beta',F(self.beta))


@dataclass(frozen=True)
class UniformRule:
    removed: tuple[int,...]
    rephased: tuple[AffineRunner,...]
    added: tuple[AffineRunner,...]

    def __post_init__(self):
        if any(type(q) is not int or q<2 or q%2 for q in self.removed):
            raise ValueError('removed velocities must be positive even integers')
        if any(x.velocity%2 for x in self.rephased):
            raise ValueError('rephased velocities must be even')
        if any(x.velocity%2==0 for x in self.added):
            raise ValueError('added velocities must be odd')
        all_velocities=self.removed+tuple(x.velocity for x in self.rephased+self.added)
        if len(all_velocities)!=len(set(all_velocities)):
            raise ValueError('velocity labels must be distinct across all rule parts')
        if not self.affected:
            raise ValueError('at least one affected original velocity required')

    @property
    def affected(self):
        return tuple(sorted(self.removed+tuple(x.velocity for x in self.rephased)))

    @property
    def rescuers(self):
        return self.rephased+self.added

    @property
    def gain(self):
        return len(self.removed)-len(self.added)

    @property
    def largest_affected(self):
        return max(self.affected)


def poliakova_rule():
    """Literal Section 3 rule of arXiv:2609.23952v1, not its Table 1 variant."""
    return UniformRule((8,32,192),
        tuple(AffineRunner(q,F(1,2),F(1,2)) for q in (12,24,48,96))+
        tuple(AffineRunner(q,F(0),F(-1)) for q in (16,64)),
        tuple(AffineRunner(q,F(1,4),F(0)) for q in (3,9)))


def responsible_residues(q: int):
    if type(q) is not int or q<2 or q%2:
        raise ValueError('positive even source velocity required')
    return tuple(k for k in range(q) if gcd(k,q//2)==1)


def resonance_interval(q: int, k: int, runner: AffineRunner):
    """Closed z interval where the exactly resonant rescuer lies within delta.

    Nonresonant offsets are not credited: they cannot cover the tangent
    configuration as delta tends to zero. The returned bounds are clipped.
    """
    offset=F(runner.velocity*k,q)+runner.alpha
    if offset.denominator!=1:
        return None
    scale=F(runner.velocity,q)
    left=max(F(-1),(-1-runner.beta)/scale)
    right=min(F(1),(1-runner.beta)/scale)
    return (left,right) if left<=right else None


def coverage_gap(intervals):
    """Return an exact uncovered point in [-1,1], or None for closed coverage."""
    intervals=sorted(intervals)
    if not intervals or intervals[0][0]>-1:
        return F(-1)
    end=intervals[0][1]
    for left,right in intervals[1:]:
        if left>end:
            return (left+end)/2
        end=max(end,right)
    return F(1) if end<1 else None


def check_local_uniform(rule: UniformRule):
    """Return a finite exact proof certificate or first failing residue/interval.

    Universality follows from the dossier theorem; enumerated residue cells
    do not represent sampled physical times or a bounded-N approximation.
    """
    cells=[]
    for q in rule.affected:
        for k in responsible_residues(q):
            cover=[]
            for runner in rule.rescuers:
                interval=resonance_interval(q,k,runner)
                if interval is not None:
                    cover.append({'velocity':runner.velocity,
                                  'left':str(interval[0]),'right':str(interval[1])})
            gap=coverage_gap((F(c['left']),F(c['right'])) for c in cover)
            cells.append({'q':q,'k':k,'cover':cover})
            if gap is not None:
                return {'local_uniform':False,'gain':rule.gain,
                        'largest_affected':rule.largest_affected,'checked_cells':len(cells),
                        'gap':{'q':q,'k':k,'z':str(gap)},'cells':cells}
    return {'local_uniform':True,'gain':rule.gain,
            'largest_affected':rule.largest_affected,'checked_cells':len(cells),'cells':cells}


def circle_distance(value):
    value=F(value)%1
    return min(value,1-value)


def gap_counterexample(rule: UniformRule, q: int, k: int, z):
    """Turn a failed tangent cell into an actual rational N,b=1,t witness.

    All earlier even runners are excluded exactly; the responsible runner q
    is within delta, and every allowed local rescuer is outside delta. The
    witness refutes locality, not necessarily global cover preservation.
    """
    z=F(z)
    if q not in rule.affected or k not in responsible_residues(q) or not -1<=z<=1:
        raise ValueError('valid affected responsible residue and z required')
    bounds=[]
    for velocity in range(2,q,2):
        offset=circle_distance(F(velocity*k,q))
        if not offset:
            raise ValueError('the nominated runner cannot be responsible')
        bounds.append(offset/(abs(F(velocity,q)*z)+1))
    for runner in rule.rescuers:
        offset=circle_distance(F(runner.velocity*k,q)+runner.alpha)
        slope=F(runner.velocity,q)*z+runner.beta
        if offset==0:
            if abs(slope)<=1:
                raise ValueError('point is covered by an exactly resonant rescuer')
            bounds.append(1/(abs(slope)+1))
        else:
            bounds.append(offset/(abs(slope)+1))
    epsilon=min(bounds,default=F(1))
    n=max(rule.largest_affected//2, epsilon.denominator//epsilon.numerator+1)
    delta=F(1,n+1)
    time=(F(k,q)+delta*z/q)%1
    assert delta<epsilon
    assert circle_distance(q*time)<=delta
    assert all(circle_distance(v*time)>delta for v in range(2,q,2))
    assert all(circle_distance(r.velocity*time+r.alpha+r.beta*delta)>delta
               for r in rule.rescuers)
    return {'N':n,'scale':1,'delta':str(delta),'time':str(time),'responsible_velocity':q,
            'responsible_distance':str(circle_distance(q*time)),
            'rescuer_distances':{str(r.velocity):str(circle_distance(
                r.velocity*time+r.alpha+r.beta*delta)) for r in rule.rescuers}}


def resonant_phase_candidates(rule: UniformRule, velocity: int):
    """Finite exact alpha menu sufficient for fixed-support existence (mod 1)."""
    if type(velocity) is not int or velocity<1:
        raise ValueError('positive integer velocity required')
    return tuple(sorted({(-F(velocity*k,q))%1 for q in rule.affected
                         for k in responsible_residues(q)}))


def useful_beta_bound(rule: UniformRule, velocity: int):
    if type(velocity) is not int or velocity<1:
        raise ValueError('positive integer velocity required')
    return F(1)+F(velocity,min(rule.affected))


def binary_ladder_rule(depth: int, removed_exponents):
    """Literal published fixed-phase ladder family; the theorem classifies it.

    Every binary exponent k=3,...,depth+1 is either removed or shifted -delta.
    Tripled powers j=2,...,depth are shifted (1+delta)/2. The tripled terminal
    is removed, and the only added odd velocities are 3 and 9 at phase 1/4.
    """
    if type(depth) is not int or depth<2:
        raise ValueError('integer depth>=2 required')
    removed=tuple(sorted(removed_exponents))
    if len(removed)!=len(set(removed)) or any(type(k) is not int or not 3<=k<=depth+1 for k in removed):
        raise ValueError('distinct binary exponents in 3,...,depth+1 required')
    return UniformRule(tuple(2**k for k in removed)+(3*2**(depth+1),),
        tuple(AffineRunner(3*2**j,F(1,2),F(1,2)) for j in range(2,depth+1))+
        tuple(AffineRunner(2**k,F(0),F(-1)) for k in range(3,depth+2) if k not in removed),
        (AffineRunner(3,F(1,4),F(0)),AffineRunner(9,F(1,4),F(0))))


def binary_ladder_condition(depth: int, removed_exponents):
    rule=binary_ladder_rule(depth,removed_exponents)  # validates the exact family
    removed=set(removed_exponents)
    return depth+1 not in removed and all(k+1 not in removed for k in removed)


def compress_added_velocities(rule: UniformRule):
    """Compress odd additions below m*lcm(affected), preserving all tangent cover.

    For each residue class, replace occupied levels by consecutive lowest
    levels and scale beta by v_new/v_old. This preserves locality by the
    proved iff criterion. Accidental nonresonant finite-delta coverage need
    not be preserved; it is not needed for that theorem.
    """
    if not rule.added:
        return rule
    modulus=lcm(*rule.affected)
    groups={}
    for index,runner in enumerate(rule.added):
        groups.setdefault(runner.velocity%modulus,[]).append((runner.velocity,index))
    result=list(rule.added)
    for residue,old in groups.items():
        for rank,(velocity,index) in enumerate(sorted(old)):
            new_velocity=residue+rank*modulus
            runner=rule.added[index]
            result[index]=AffineRunner(new_velocity,runner.alpha,
                                       F(new_velocity,velocity)*runner.beta)
    return UniformRule(rule.removed,rule.rephased,tuple(result))
