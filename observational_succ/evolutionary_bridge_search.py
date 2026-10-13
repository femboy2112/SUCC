"""Bounded typed genetic search over as-yet-unknown finite categorical bridges.

Population fitness is HEURISTIC. A proposal never becomes a proof until a
separate finite source-table validation and exact pullback verifier succeed.
Exhaustive search is an optional independent bounded-grammar optimality oracle.
Mutations/crossovers change program syntax; they cannot rewrite source events.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import permutations, product
from random import Random
from .relational_model_genetics import (
    Port, Capsule, PairedSourceTable, BridgeCandidate, GeneticsError, pullback,
    transport_capsule, emergent_dependencies, functional_dependencies, project,
)


@dataclass(frozen=True)
class Genome:
    """A candidate map and candidate parents, NOT a mathematical certificate."""
    permutation: tuple[str,...]
    use_left: bool
    use_right: bool


@dataclass(frozen=True)
class RankedGenome:
    genome: Genome
    fitness: Q
    matches: int
    source_violations: int
    merged_rows: int
    new_relations: tuple[tuple[str,str,tuple[tuple[str,str],...]],...]
    certified_by_source_table: bool
    verified_pullback: bool


@dataclass(frozen=True)
class GeneticSearchReport:
    best: RankedGenome
    proposed: int
    generations: int
    discovered_verified_bridge: BridgeCandidate|None
    exhaustive_optimum: Q|None
    genetic_reached_bounded_optimum: bool|None
    full_source_certification: bool
    exact_derived_model: Capsule|None


def evaluate(genome: Genome, left:Capsule, right:Capsule,
             source:PairedSourceTable) -> RankedGenome:
    """Predeclared finite scoring rule; source violations disqualify certification."""
    if (left.source_id,left.epoch,left.basis)!=(source.source_id,source.epoch,source.basis):
        raise GeneticsError('Left model not sourced to observation table')
    if (right.source_id,right.epoch,right.basis)!=(source.source_id,source.epoch,source.basis):
        raise GeneticsError('Right model not sourced to observation table')
    if len(genome.permutation)!=len(source.left_port.domain) or set(genome.permutation)!=set(source.right_port.domain):
        raise GeneticsError('Genetic mutation broke finite bijection type')
    mapping=tuple(zip(source.left_port.domain,genome.permutation))
    check=dict(mapping)
    matches=sum(check[l]==r for _,l,r in source.observations)
    bad=len(source.observations)-matches
    valid=bad==0
    merged_rows=0
    emergent=()
    proved=False
    if genome.use_left and genome.use_right:
        proposed=BridgeCandidate(source.source_id,source.epoch,source.basis,
                                 source.left_port,source.right_port,mapping,
                                 len(source.observations),source.complete_source_class)
        migrated=transport_capsule(right,proposed)
        r=pullback(left,migrated)
        if r.merged is not None:
            merged_rows=len(r.merged.rows)
            emergent=emergent_dependencies(left,migrated,r.merged)
            proved=bool(emergent) and valid and source.complete_source_class
    # Fitness is for search priority, never an authority for mathematical truth.
    # Rewards source matching + genuinely new expressible cross-family relations.
    # Invalid source-bridges may still rank, but cannot receive proof status.
    score=Q(4*matches-9*bad+7*int(bool(emergent))
            +5*int(proved)-int(genome.use_left)-int(genome.use_right))
    return RankedGenome(genome,score,matches,bad,merged_rows,emergent,
                        valid and source.complete_source_class,proved)


def mutate(g:Genome,rng:Random)->Genome:
    perm=list(g.permutation)
    op=rng.randrange(4)
    if op==0 and len(perm)>1:
        a,b=rng.sample(range(len(perm)),2)
        perm[a],perm[b]=perm[b],perm[a]
    elif op==1:
        return Genome(g.permutation,not g.use_left,g.use_right)
    elif op==2:
        return Genome(g.permutation,g.use_left,not g.use_right)
    else:
        if len(perm)>1:
            a,b=rng.sample(range(len(perm)),2)
            perm[a],perm[b]=perm[b],perm[a]
    return Genome(tuple(perm),g.use_left,g.use_right)


def crossover(a:Genome,b:Genome,rng:Random)->Genome:
    """Typed crossover preserves a whole bijection gene, never splits its map."""
    return Genome(a.permutation if rng.randrange(2) else b.permutation,
                  a.use_left if rng.randrange(2) else b.use_left,
                  a.use_right if rng.randrange(2) else b.use_right)


def _key(item:RankedGenome):
    return (-item.fitness,-int(item.certified_by_source_table),
            -len(item.new_relations),item.genome.permutation,
            not item.genome.use_left,not item.genome.use_right)


def _complete_oracle(left,right,source,*,max_genomes=256):
    total=2**2
    for j in range(1,len(source.right_port.domain)+1):total*=j
    if total>max_genomes:return None
    all_scores=(evaluate(Genome(tuple(perm),a,b),left,right,source)
                for perm in permutations(source.right_port.domain)
                for a,b in product((False,True),repeat=2))
    return sorted(all_scores,key=_key)[0]


def evolve_bridges(left:Capsule,right:Capsule,source:PairedSourceTable,
                   *,seed:int=0,population:int=18,generations:int=16,
                   exact_bounded_oracle:bool=True)->GeneticSearchReport:
    if (type(population) is not int or population<4 or population>256 or
        type(generations) is not int or generations<1 or generations>100 or
        type(seed) is not int):
        raise GeneticsError('Finite reproducible evolutionary resource bounds required')
    rng=Random(seed)
    dom=source.right_port.domain
    current=[Genome(tuple(rng.sample(list(dom),len(dom))),
                    bool(rng.randrange(2)),bool(rng.randrange(2)))
             for _ in range(population)]
    evaluated={}
    for generation in range(generations):
        for g in current:
            if g not in evaluated:evaluated[g]=evaluate(g,left,right,source)
        winners=sorted((evaluated[g] for g in current),key=_key)
        elite=[v.genome for v in winners[:max(2,population//4)]]
        # Elitism retains the best known research branch.
        current=elite[:]
        while len(current)<population:
            a,b=rng.choice(elite),rng.choice(elite)
            child=crossover(a,b,rng)
            if rng.randrange(5)!=0:
                child=mutate(child,rng)
            current.append(child)
    for g in current:
        if g not in evaluated:evaluated[g]=evaluate(g,left,right,source)
    best=sorted(evaluated.values(),key=_key)[0]
    oracle=_complete_oracle(left,right,source) if exact_bounded_oracle else None
    certified=None;derived=None
    if best.certified_by_source_table and best.genome.use_left and best.genome.use_right:
        mapping=tuple(zip(source.left_port.domain,best.genome.permutation))
        certified=BridgeCandidate(source.source_id,source.epoch,source.basis,
                                  source.left_port,source.right_port,mapping,
                                  len(source.observations),source.complete_source_class)
        translated=transport_capsule(right,certified)
        f=pullback(left,translated)
        if f.merged is None or not best.verified_pullback:
            raise ArithmeticError('A claimed genetic proof lacks its exact pullback')
        derived=f.merged
    return GeneticSearchReport(best,len(evaluated),generations,certified,
                               oracle.fitness if oracle else None,
                               best.fitness==oracle.fitness if oracle else None,
                               source.complete_source_class,derived)


def grow_new_model(joined:Capsule,from_port:str,to_port:str,*,name='discovered-invariant') -> Capsule:
    """Verified syntactic GRAMMAR GROWTH: new two-port model is a projection.

    This relation need not occur in any input capsule; its proof is exactly
    model projection, not genetic fitness or guessed truth about the world.
    """
    dep=next(((u,v,m) for u,v,m in functional_dependencies(joined)
              if (u,v)==(from_port,to_port)),None)
    if dep is None:raise GeneticsError('The requested new arrow is not a theorem')
    ports=tuple(p for n in (from_port,to_port) for p in joined.ports if p.name==n)
    return Capsule(name,'derived-by-fiber-product',joined.source_id,joined.epoch,
                   joined.basis,ports,project(joined,(from_port,to_port)),
                   parents=joined.parents,features=joined.features|frozenset({'learned-arrow'}))


def genetic_discovery_demo(seed:int=5)->dict:
    from .relational_model_genetics import binary_capsule, bridge_repair_demo
    source='declared-affine-source'
    left=binary_capsule('clock','clock',source,'x','y',1)
    right=Capsule('thermal','thermal',source,0,'binary-v1',
                  (Port('temperature_code',('cold','warm')),Port('z',('0','1'))),
                  (('cold','1'),('warm','0')))
    table=PairedSourceTable(source,0,'binary-v1',Port('y',('0','1')),
                            Port('temperature_code',('cold','warm')),
                            (('s0','0','cold'),('s1','1','warm')),True)
    run=evolve_bridges(left,right,table,seed=seed)
    if run.exact_derived_model is None or not run.best.new_relations:
        raise AssertionError('Typed search failed to discover any new bridge')
    new=grow_new_model(run.exact_derived_model,'x','z')
    new_relation=project(new,('x','z'))
    return {'heuristic_best_fitness':str(run.best.fitness),
            'genetic_candidates_evaluated':run.proposed,
            'bounded_grammar_optimum_achieved':run.genetic_reached_bounded_optimum,
            'sourced_bridge':dict(run.discovered_verified_bridge.mapping),
            'grown_new_model':new.name,
            'new_cross_model_relation':new_relation,
            'relation_proved_by_exact_finite_projection':True,
            'new_relation_not_in_the_input_module_schemas':True,
            'probabilistic_fitness_is_not_a_proof':True,
            'physical_source_authenticated':False}


def ternary_fusion_demo(seed:int=0)->dict:
    """A second, nonbinary construction: invent a 3-value semantic bridge.

    Mechanical modulo-3 successor and thermal three-state code overlap along
    y, creating x=z in Z/3. The bridge is not supplied to the genetic genome;
    a finite COMPLETE declared source table decides its validity.
    """
    src='declared-ternary-source'
    d=('0','1','2'); heat=('cold','warm','hot')
    mechanical=Capsule('cyclic-clock','cyclic',src,0,'mod3-v1',
                       (Port('x',d),Port('y',d)),
                       tuple((str(i),str((i+1)%3)) for i in range(3)),
                       features=frozenset({'cyclic','succ'}))
    thermal=Capsule('thermal-labels','thermal',src,0,'mod3-v1',
                    (Port('temp',heat),Port('z',d)),
                    (('cold','2'),('warm','0'),('hot','1')),
                    features=frozenset({'thermal','three-state'}))
    table=PairedSourceTable(src,0,'mod3-v1',Port('y',d),Port('temp',heat),
                            (('s0','0','cold'),('s1','1','warm'),('s2','2','hot')),True)
    report=evolve_bridges(mechanical,thermal,table,seed=seed,
                          population=22,generations=22)
    actual=report.exact_derived_model
    genetic_success=actual is not None
    bridge=report.discovered_verified_bridge
    if actual is None:
        # Heuristic evolutionary search can converge to a LOCAL optimum.
        # This is a genuine, reproducible failure on some seeds. With only
        # 24 genotypes a separately exhaustive search can find an exact
        # source-checked repair, but it must NEVER be called genetic success.
        opt=_complete_oracle(mechanical,thermal,table,max_genomes=256)
        if opt is None or not opt.certified_by_source_table or not opt.verified_pullback:
            raise GeneticsError('No bounded-grammar certified synthesis')
        mapping=tuple(zip(table.left_port.domain,opt.genome.permutation))
        bridge=BridgeCandidate(table.source_id,table.epoch,table.basis,
                               table.left_port,table.right_port,mapping,
                               len(table.observations),True)
        translated=transport_capsule(thermal,bridge)
        joined=pullback(mechanical,translated)
        if joined.merged is None:
            raise ArithmeticError('Exhaustive witness violated source semantics')
        actual=joined.merged
    derived=grow_new_model(actual,'x','z',name='born-mod3-relation')
    return {'discovered_bridge':dict(bridge.mapping),
            'new_mod3_invariant':project(derived,('x','z')),
            'generated_new_port_relation':derived.name,
            'grammar_size':24,
            'genetic_succeeded':genetic_success,
            'bounded_oracle_rescue_used':not genetic_success,
            'bounded_optimum_verified':report.genetic_reached_bounded_optimum,
            'source_claim_class_conditional':True,
            'novelty_of_formal_mathematics_claimed':False}
