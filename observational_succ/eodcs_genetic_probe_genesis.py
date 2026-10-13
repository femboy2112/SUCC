"""Evolutionary discovery of *probe syntax*, never proof by fitness.

Initial vocabulary: empty observation word plus typed primitive actions.
Offspring arise by appending/prepending, deleting/replacing, swapping,
or crossing action *words*. The target separating composite is not a
pre-supplied genome. Finite original-source reports verify each proposed
experiment independently of its score; a full pair-state BFS is a
separate bounded-grammar exact fallback and an honest no-path detector.

A dark pair survives all finite available action words. No mutation in
this grammar is permitted to invent an unowned physical instrument.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from random import Random

from .causal_nerode_succ import SourceTransportError
from .eodcs_multi_action_source import (
    ActionSource, shortest_distinguishing_word,
    newly_generated_probe_demo,
)


@dataclass(frozen=True)
class ProbeGenome:
    word: tuple[str, ...]


@dataclass(frozen=True)
class GeneticProbeReceipt:
    seed: int
    source_id: str
    source_epoch: int
    source_basis: str
    target_pair: tuple[str, str]
    grammar_actions: tuple[str, ...]
    maximum_word_length: int
    generations: int
    evaluated_genomes: int
    genetic_verified_separator: tuple[str, ...] | None
    exact_shortest_separator: tuple[str, ...] | None
    genetic_succeeded: bool
    genetic_found_exact_shortest: bool
    bounded_oracle_rescue: bool
    proven_dark_within_declared_action_grammar: bool
    physical_probe_materialized: bool = False


def validate_word(source: ActionSource, genome: ProbeGenome, max_length: int):
    if (type(genome.word) is not tuple
            or len(genome.word) > max_length
            or any(a not in source.actions for a in genome.word)):
        raise SourceTransportError("Genome must inhabit the current owned action grammar")


def mutate(genome: ProbeGenome, actions: tuple[str, ...],
           rng: Random, max_length: int) -> ProbeGenome:
    word=list(genome.word)
    op=rng.randrange(5)
    if (not word or op==0) and len(word)<max_length:
        word.append(rng.choice(actions))
    elif op==1 and len(word)<max_length:
        word.insert(0,rng.choice(actions))
    elif op==2 and word:
        word[rng.randrange(len(word))]=rng.choice(actions)
    elif op==3 and word:
        word.pop(rng.randrange(len(word)))
    elif len(word)>1:
        i=rng.randrange(len(word)-1)
        word[i],word[i+1]=word[i+1],word[i]
    elif len(word)<max_length:
        word.append(rng.choice(actions))
    return ProbeGenome(tuple(word))


def crossover(a: ProbeGenome,b: ProbeGenome,rng: Random,
              max_length:int) -> ProbeGenome:
    left=a.word[:rng.randrange(len(a.word)+1)]
    right=b.word[rng.randrange(len(b.word)+1):]
    return ProbeGenome((left+right)[:max_length])


def genetic_probe_search(source: ActionSource, first: str, second: str, *,
                         seed: int, population: int = 8,
                         generations: int = 6,
                         maximum_word_length: int = 5) -> GeneticProbeReceipt:
    if (type(seed) is not int or type(population) is not int
            or type(generations) is not int or type(maximum_word_length) is not int
            or population < 4 or generations < 1 or not 0 <= maximum_word_length <= 12):
        raise SourceTransportError("Finite genetic search needs explicit legal budgets")
    if first not in source.states or second not in source.states:
        raise SourceTransportError("Genetic experiment lacks a typed source pair")
    rng=Random(seed)
    initial=[ProbeGenome(())]+[
        ProbeGenome((rng.choice(source.actions),)) if maximum_word_length
        else ProbeGenome(())
        for _ in range(population-1)]
    current=tuple(initial)
    evaluated={}
    winner=None

    def score(g:ProbeGenome):
        validate_word(source,g,maximum_word_length)
        w=g.word
        separating=source.observe(first,w)!=source.observe(second,w)
        outputs={source.observe(s,w) for s in source.states}
        return (Q(20*int(separating)+3*len(outputs))-Q(len(w),4),
                separating)

    for _ in range(generations):
        for g in current:
            evaluated.setdefault(g.word,score(g))
        winners=tuple(w for w,(fitness,success) in evaluated.items()
                      if success)
        if winners:
            winner=min(winners,key=lambda w:(len(w),w))
            break
        ranked=sorted(current,key=lambda g:(score(g)[0],-len(g.word),g.word),
                      reverse=True)
        elite=ranked[:max(2,population//3)]
        next_generation=list(elite)
        while len(next_generation)<population:
            if rng.randrange(4)==0:
                child=crossover(rng.choice(elite),rng.choice(elite),
                                rng,maximum_word_length)
            else:
                child=mutate(rng.choice(elite),source.actions,rng,
                             maximum_word_length)
            validate_word(source,child,maximum_word_length)
            next_generation.append(child)
        current=tuple(next_generation)

    # Independent complete pair-state oracle, not the genetic population.
    exact=shortest_distinguishing_word(source,first,second)
    if winner is not None and (
        source.observe(first,winner)==source.observe(second,winner)):
        raise AssertionError("Scoring invented an unverified experiment")
    success=winner is not None
    return GeneticProbeReceipt(
        seed,source.source_id,source.epoch,source.basis,(first,second),
        source.actions,maximum_word_length,generations,len(evaluated),
        winner,exact,success,
        success and exact is not None and len(winner)==len(exact),
        (not success) and exact is not None,
        exact is None,False,
    )


def genetic_probe_demo() -> dict:
    states=("x","y","u","v","c","d")
    src=ActionSource("genetic-supplied-source",0,"typed",states,
                     ("0","0","0","0","0","1"),("A","B"),
                     (("u","v","u","v","c","d"),
                      ("x","y","c","d","c","d")))
    tight=genetic_probe_search(src,"x","y",seed=0,
                               population=5,generations=1)
    seeds=tuple(genetic_probe_search(src,"x","y",seed=k)
                for k in range(20))
    dark_states=("a","b","c","d")
    dark=ActionSource("genetic-dark-control",0,"typed",dark_states,
                      ("0","0","1","1"),("A","B"),
                      (("b","a","d","c"),("a","b","d","c")))
    no_path=genetic_probe_search(dark,"a","b",seed=7)
    if not tight.bounded_oracle_rescue or tight.genetic_succeeded:
        raise AssertionError("One generation cannot construct a two-step word")
    if not no_path.proven_dark_within_declared_action_grammar:
        raise AssertionError("Dark pair cannot be rescued by an imaginary probe")
    return {
        "source_pair":["x","y"],
        "source_derived_exact_shortest_word":list(tight.exact_shortest_separator),
        "tight_budget_genetic_failed":not tight.genetic_succeeded,
        "tight_budget_exact_oracle_rescued":tight.bounded_oracle_rescue,
        "twenty_seeded_genetic_successes":sum(r.genetic_succeeded for r in seeds),
        "twenty_seeded_genetic_failures":sum(not r.genetic_succeeded for r in seeds),
        "every_success_source_verified":all(
            not r.genetic_succeeded or
            src.observe("x",r.genetic_verified_separator)!=
            src.observe("y",r.genetic_verified_separator) for r in seeds),
        "dark_source_finite_grammar_empty":no_path.proven_dark_within_declared_action_grammar,
        "dark_source_external_probe_not_invented":not no_path.physical_probe_materialized,
        "general_automatic_mathematics_invented":False,
    }
