"""Shadow-SUCC/FUCC: exact source-relative finite empirical inference.

An observation is a linear functional on a single declared rational carrier.
SUCC accumulates actual reported forms, FUCC checks when a proposed source
claim factors through their joint observation map. If it cannot factor,
return two mathematically realisable sources with the SAME observed values
but DIFFERENT target values. Every equality is exact (fractions.Fraction).

This model checks formal reported values, not empirical authenticity. For
nonlinear or source-changing instruments the existing SUCC source-fiber and
coalgebraic interfaces impose additional separate obligations.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence


class ShadowSourceError(ValueError):
    """Unlicensed source, invalid proof or incompatible empirical report."""


def _q(x: object) -> Q:
    if type(x) is int or type(x) is Q:
        return Q(x)
    raise ShadowSourceError("Only exact integers and rational Fractions are certificates")


def _vec(values: Sequence[Q], n: int) -> tuple[Q, ...]:
    if type(values) not in (list, tuple) or len(values) != n:
        raise ShadowSourceError("Expected a complete rational source linear form")
    return tuple(_q(x) for x in values)


def dot(a: Sequence[Q], b: Sequence[Q]) -> Q:
    if len(a) != len(b):
        raise ShadowSourceError("Different source dimensions")
    return sum((x*y for x,y in zip(a,b)), Q(0))


def solve_system(rows: Sequence[Sequence[Q]], values: Sequence[Q],
                 variable_count: int) -> dict:
    """Rational RREF. Return one solution and homogeneous directions or
    an EXACT linear dependency certifying inconsistent constraints.
    """
    if type(variable_count) is not int or not 1 <= variable_count <= 1024:
        raise ShadowSourceError("Bounded positive rational carrier dimension required")
    m = len(rows)
    if len(values) != m:
        raise ShadowSourceError("Linear equation/value lengths mismatch")
    rr = tuple(_vec(row,variable_count) for row in rows)
    vv = tuple(_q(v) for v in values)
    augmented = [[*rr[i],vv[i],*(Q(int(i==j)) for j in range(m))]
                 for i in range(m)]
    pivot_rows = {}
    cursor=0
    for col in range(variable_count):
        target = next((i for i in range(cursor,m) if augmented[i][col]),None)
        if target is None:
            continue
        augmented[cursor],augmented[target]=augmented[target],augmented[cursor]
        mul=augmented[cursor][col]
        augmented[cursor]=[v/mul for v in augmented[cursor]]
        for i in range(m):
            if i==cursor:
                continue
            mul=augmented[i][col]
            if mul:
                augmented[i]=[x-mul*y for x,y in zip(augmented[i],augmented[cursor])]
        pivot_rows[col]=cursor
        cursor+=1
        if cursor==m:
            break
    for row in augmented:
        if all(not v for v in row[:variable_count]) and row[variable_count]:
            coeffs=tuple(row[variable_count+1:])
            if (any(sum((coeffs[i]*rr[i][j] for i in range(m)),Q(0))
                    for j in range(variable_count))
                    or sum((coeffs[i]*vv[i] for i in range(m)),Q(0))==0):
                raise AssertionError("Invalid exact contradiction witness")
            return {"status":"CONTRADICTION", "row_combination":coeffs,
                    "nonzero_value":row[variable_count]}
    solution=[Q(0)]*variable_count
    for col,r in pivot_rows.items():
        solution[col]=augmented[r][variable_count]
    free=[col for col in range(variable_count) if col not in pivot_rows]
    nullspace=[]
    for free_col in free:
        direction=[Q(0)]*variable_count
        direction[free_col]=1
        for col,r in pivot_rows.items():
            direction[col]=-augmented[r][free_col]
        if any(dot(row,direction) for row in rr):
            raise AssertionError("Bad nullspace")
        nullspace.append(tuple(direction))
    if any(dot(row,solution)!=value for row,value in zip(rr,vv)):
        raise AssertionError("Bad rational particular solution")
    return {"status":"CONSISTENT","representative":tuple(solution),
            "nullspace":tuple(nullspace),"rank":len(pivot_rows)}


@dataclass(frozen=True)
class EmpiricalForm:
    """Declared lawful observation; ownership and source are typed metadata.

    No cryptographic or physical authentication is inferred from these strings.
    """
    source_id: str
    source_version: int
    basis_id: str
    name: str
    owner: str
    coefficients: tuple[Q, ...]
    value: Q

    def __post_init__(self):
        if (not all(type(x) is str and x for x in (self.source_id,self.basis_id,
                                                self.name,self.owner))
                or type(self.source_version) is not int or self.source_version < 0):
            raise ShadowSourceError("Each report needs a source, version, basis, probe and owner")
        if type(self.coefficients) is not tuple or not self.coefficients:
            raise ShadowSourceError("Complete nonempty source linear form required")
        object.__setattr__(self,"coefficients",_vec(self.coefficients,len(self.coefficients)))
        object.__setattr__(self,"value",_q(self.value))


@dataclass(frozen=True)
class ShadowCarrier:
    source_id: str
    source_version: int
    basis_id: str
    dimension: int

    def __post_init__(self):
        if (not self.source_id or not self.basis_id or type(self.source_version) is not int
                or self.source_version<0 or type(self.dimension) is not int
                or self.dimension<1 or self.dimension>1024):
            raise ShadowSourceError("Declared nonempty source/version/basis/dimension required")

    def report(self, name: str, owner: str, coefficients: Sequence[Q],
               value: Q) -> EmpiricalForm:
        return EmpiricalForm(self.source_id,self.source_version,self.basis_id,
                             name,owner,_vec(coefficients,self.dimension),value)

    def verify_reports(self, reports: Sequence[EmpiricalForm]) -> tuple[EmpiricalForm,...]:
        observations=tuple(reports)
        for r in observations:
            if not isinstance(r,EmpiricalForm) or (
                r.source_id,r.source_version,r.basis_id) != (
                self.source_id,self.source_version,self.basis_id):
                raise ShadowSourceError("Cannot merge reports from distinct source versions/bases")
            if len(r.coefficients)!=self.dimension:
                raise ShadowSourceError("Source dimension differs from report")
        if len({r.name for r in observations})!=len(observations):
            raise ShadowSourceError("Duplicate named probes: choose explicit distinct source forms")
        return observations

    def fiber(self, reports: Sequence[EmpiricalForm]) -> dict:
        rs=self.verify_reports(reports)
        return solve_system([r.coefficients for r in rs],
                            [r.value for r in rs], self.dimension)

    def shadow_fucc(self,reports:Sequence[EmpiricalForm],
                    target:Sequence[Q]) -> dict:
        """Construct a source-target decoder, or two actual possible
        source vectors casting identical reported shadows with distinct target.
        """
        rs=self.verify_reports(reports)
        target=_vec(target,self.dimension)
        fiber=self.fiber(rs)
        if fiber["status"]=="CONTRADICTION":
            return {"status":"INCONSISTENT_SOURCE","contradiction":fiber,
                    "claim":None}
        # A claim descends iff it annihilates the unseen directions.
        bad=next((h for h in fiber["nullspace"] if dot(target,h)),None)
        if bad is not None:
            x=fiber["representative"]
            y=tuple(u+v for u,v in zip(x,bad))
            if any(dot(r.coefficients,x)!=dot(r.coefficients,y) for r in rs):
                raise AssertionError("Source-alias certificate invalid")
            return {"status":"UNRESOLVED", "witness_source_a":x,
                    "witness_source_b":y,"same_observed_values":tuple(r.value for r in rs),
                    "different_target_values":(dot(target,x),dot(target,y)),
                    "missing_direction":bad,"rank":fiber["rank"]}
        # Solve target as a rational combination of witnessed empirical forms.
        transposed=[tuple(r.coefficients[j] for r in rs) for j in range(self.dimension)]
        if not rs:
            coefficients=() if not any(target) else None
        else:
            combined=solve_system(transposed,target,len(rs))
            coefficients=(combined["representative"] if combined["status"]=="CONSISTENT" else None)
        if coefficients is None:
            raise AssertionError("Annihilator/row-span theorem failed")
        if any(sum((coefficients[i]*rs[i].coefficients[j]
                    for i in range(len(rs))),Q(0))!=target[j]
               for j in range(self.dimension)):
            raise AssertionError("Forged factorization")
        inferred=sum((c*r.value for c,r in zip(coefficients,rs)),Q(0))
        if inferred!=dot(target,fiber["representative"]):
            raise AssertionError("Incorrect original-source proof")
        return {"status":"PROVED","claim":inferred,
                "proof_coefficients":coefficients,
                "source_forms":tuple(r.name for r in rs),
                "source_version":self.source_version,
                "rank":fiber["rank"]}

    def successor(self,reports:Sequence[EmpiricalForm],new_report:EmpiricalForm,
                  target:Sequence[Q]) -> dict:
        rs=self.verify_reports(reports)
        after=self.shadow_fucc(rs+(new_report,),target)
        before=self.shadow_fucc(rs,target)
        if before["status"]=="PROVED" and after["status"]=="CONSISTENT":
            raise AssertionError("Status cannot become consistent")
        if before["status"]=="PROVED" and after["status"]=="UNRESOLVED":
            raise AssertionError("Source-compatible observation lost a true proof")
        return {"before":before,"after":after,
                "epistemic_step_count":1,"new_physical_events":1,
                "source_authentication":"DECLARED, NOT PHYSICALLY ATTESTED"}


def combined_shadow_rank(carrier:ShadowCarrier,
                         bundles:Sequence[Sequence[EmpiricalForm]],target:Sequence[Q]) -> dict:
    """Observer-E glues reports across multiple towers WITHOUT assuming their
    results jointly source-realizable. Joint consistency is checked first.
    """
    flat=tuple(r for bundle in bundles for r in bundle)
    outcome=carrier.shadow_fucc(flat,target)
    return {"result":outcome,"tower_count":len(bundles),
            "total_reports":len(flat),"source_id":carrier.source_id}


def pullback_form(form:Sequence[Q], source_map:Sequence[Sequence[Q]]) -> tuple[Q,...]:
    """Given h:Q^new -> Q^old (matrix old_dim x new_dim),
    transport observational form p to p∘h. No observed value is fabricated.
    """
    if type(source_map) not in (tuple,list) or not source_map:
        raise ShadowSourceError("An explicit nonempty source map is required")
    old_dim=len(source_map)
    form=_vec(form,old_dim)
    if not source_map[0]:
        raise ShadowSourceError("The refined carrier must have positive dimension")
    new_dim=len(source_map[0])
    matrix=tuple(_vec(row,new_dim) for row in source_map)
    return tuple(sum((form[i]*matrix[i][j] for i in range(old_dim)),Q(0))
                 for j in range(new_dim))


def verify_shadow_base_change(probe_forms:Sequence[Sequence[Q]],
                              target:Sequence[Q],
                              source_map:Sequence[Sequence[Q]])->dict:
    """Check that an OLD source-target factorization pulls back along h;
    report whether the reverse inference becomes newly possible on a smaller
    source. A valid algebraic h is not empirical source authentication.
    """
    old_dim=len(source_map)
    if not old_dim:
        raise ShadowSourceError("Source map is absent")
    probes=tuple(_vec(p,old_dim) for p in probe_forms)
    target=_vec(target,old_dim)
    new_probes=tuple(pullback_form(p,source_map) for p in probes)
    new_target=pullback_form(target,source_map)
    def descends(forms,claim,dim):
        if not forms:
            return not any(claim)
        # Row-span property via transposed system.
        mat=[tuple(p[j] for p in forms) for j in range(dim)]
        return solve_system(mat,claim,len(forms))['status']=='CONSISTENT'
    old=descends(probes,target,old_dim)
    new=descends(new_probes,new_target,len(new_target))
    if old and not new:
        raise AssertionError("Legal source pullback destroyed a true polynomial identity")
    return {'old_target_factored':old,'new_target_factored':new,
            'new_target':new_target,'new_probes':new_probes,
            'converse_unjustified':not old and new,
            'physical_source_authentication':False}


def shadow_claim_error_budget(proof_coefficients:Sequence[Q],
                              observation_errors:Sequence[Q])->Q:
    """If target=sum c_i p_i on ORIGINAL carrier and measured values
    each have certified absolute error <=e_i, claim error <=sum|c_i|e_i.
    Errors are supplied premises, not inferred measurements.
    """
    if len(proof_coefficients)!=len(observation_errors):
        raise ShadowSourceError("Proof and observation error budgets differ")
    coeffs=tuple(_q(v) for v in proof_coefficients)
    errors=tuple(_q(v) for v in observation_errors)
    if any(x<0 for x in errors):
        raise ShadowSourceError("Observation absolute-error bounds must be nonnegative")
    return sum((abs(c)*e for c,e in zip(coeffs,errors)),Q(0))


def minimal_shadow_probe_design(forms:Sequence[Sequence[Q]],
                                target:Sequence[Q],*,max_probes:int=12)->dict:
    """Finite target-oriented experimental DESIGN before observing values.
    Enumerate smallest probe family that algebraically determines target;
    does not magically make probes physically available or measured.
    """
    from itertools import combinations
    dimension=len(target)
    target=_vec(target,dimension)
    candidates=tuple(_vec(form,dimension) for form in forms)
    if (type(max_probes) is not int or max_probes<0
            or len(candidates)>max_probes):
        raise ShadowSourceError("Finite probe-subset enumeration budget exceeded")
    for count in range(len(candidates)+1):
        for idx in combinations(range(len(candidates)),count):
            rows=[candidates[j] for j in idx]
            if not rows:
                if not any(target):
                    return {'status':'DESIGN_FOUND','probe_indices':idx,
                            'coefficients':(), 'min_num_probes':0}
                continue
            transposed=[tuple(row[j] for row in rows) for j in range(dimension)]
            result=solve_system(transposed,target,len(rows))
            if result['status']=='CONSISTENT':
                c=result['representative']
                if any(sum((rows[i][j]*c[i] for i in range(len(rows))),Q(0))!=target[j]
                       for j in range(dimension)):
                    raise AssertionError("Bad empirical proof design")
                return {'status':'DESIGN_FOUND','probe_indices':idx,
                        'coefficients':c,'min_num_probes':count}
    return {'status':'UNRESOLVED_MENU','probe_count':len(candidates),
            'source_claim_not_yet_observed':True}


def receding_shadow_escape(stage:int)->dict:
    """Nested closed source-compatible sets X_n={0} U [n,infinity)
    on shared carrier [0,infinity). Their intersection is {0}, but the
    continuous target T(x)=x/(1+x) differs by n/(n+1) at witness x=n.
    All values rational; no physical infinity executed.
    """
    if type(stage) is not int or stage<1:
        raise ShadowSourceError("A positive finite observational stage required")
    return {'stage':stage,'actual_source':Q(0),'witness_source':Q(stage),
            'target_at_actual':Q(0), 'target_at_witness':Q(stage,stage+1),
            'finite_stage_target_not_uniformly_converged':True,
            'mathematical_intersection_all_stages_is_zero':True}
