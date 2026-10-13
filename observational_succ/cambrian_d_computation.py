"""CAMBRIAN D: exact finite computational research instruments.

Declared simulator laws only. Memory birth is provided by a generic residual
split metaconstructor; evolutionary word selection receives separate credit.
Existing Moore minimization and rational Hankel rank are reused as verifiers.
No physical source authentication, universal learning, or novelty claim.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from random import Random

from .eodcs_multi_action_source import ActionSource, action_congruence
from .eodcs_genetic_probe_genesis import genetic_probe_search
from .carrier_hankel_bounds import hankel, rank
from .noncommuting_proof_transport import FiniteCarrier, Instrument


def partial_source(outputs, actions, transitions, *, source_id="partial"):
    """Totalize partial actions when enabled menus are observable.

    None denotes a disabled action. A distinct failure sink preserves the
    legality trace. This adapter is NOT licensed when menus/failure are hidden.
    Context/source types can be included in the supplied output labels.
    """
    n = len(outputs)
    if (not n or len(actions) != len(transitions)
            or any(type(o) not in (str,int) for o in outputs)
            or any(len(row) != n for row in transitions)
            or any(t is not None and (type(t) is not int or not 0 <= t < n)
                   for row in transitions for t in row)):
        raise ValueError("Malformed finite partial source")
    states = tuple(str(i) for i in range(n)) + ("disabled",)
    reports = tuple(repr((outputs[i], tuple(row[i] is not None
                                           for row in transitions)))
                    for i in range(n)) + ("FAILURE",)
    maps = tuple(tuple("disabled" if t is None else str(t) for t in row)
                 + ("disabled",) for row in transitions)
    return ActionSource(source_id, 0, "observable-enabledness", states,
                        reports, tuple(actions), maps)


def exhaustive_partitions(n):
    """All set partitions as restricted-growth strings; independent oracle."""
    if type(n) is not int or not 1 <= n <= 8:
        raise ValueError("Declared exhaustive partition budget is 1..8 states")
    def extend(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for label in range(max(prefix) + 2):
            yield from extend(prefix + [label])
    yield from extend([0])


def exhaustive_minimum_quotient(source):
    """Enumerate EVERY partition, retaining all output/action congruences."""
    states = source.states
    valid, tested = [], 0
    for partition in exhaustive_partitions(len(states)):
        tested += 1
        mapping = dict(zip(states, partition))
        if all(source.report(s) == source.report(t) and all(
                mapping[source.step(s, a)] == mapping[source.step(t, a)]
                for a in source.actions)
               for s, t in product(states, repeat=2) if mapping[s] == mapping[t]):
            valid.append(partition)
    best = min(valid, key=lambda p: (len(set(p)), p))
    return {"classes": len(set(best)), "partition": best,
            "partitions_checked": tested, "lawful_partitions": len(valid)}


@dataclass(frozen=True)
class MemoryBirth:
    source: ActionSource
    probes: tuple[tuple[str, ...], ...]
    signatures: tuple[tuple[str, ...], ...]
    classes: tuple[tuple[str, ...], ...]
    class_count_history: tuple[int, ...]
    obstructions: tuple[dict, ...]
    genetic_successes: int
    deterministic_repairs: int

    def predictive_class(self, state):
        return next(i for i, block in enumerate(self.classes) if state in block)

    def prediction(self, class_index, action):
        block = self.classes[class_index]
        targets = {self.predictive_class(self.source.step(s, action)) for s in block}
        if len(targets) != 1:
            raise AssertionError("Memory representation failed causal descent")
        return next(iter(targets))


def construct_memory(source, *, genetic_seed=None):
    """Counterexample-guided birth of a finite predictive state type.

    Initial grammar contains current report only. The declared metagrammar
    introduces tuple-valued residual signatures and finite transition tables.
    It does not pre-list the correct counter, graph, or automaton. Full source
    tables are privileged model-validation access, not observer measurements.
    """
    probes = [()]
    counts, obstructions = [], []
    successes = repairs = 0
    while True:
        signatures = {s: tuple(source.observe(s, w) for w in probes)
                      for s in source.states}
        counts.append(len(set(signatures.values())))
        bad = next(((s, t, a) for s, t in combinations(source.states, 2)
                    if signatures[s] == signatures[t] for a in source.actions
                    if signatures[source.step(s, a)] != signatures[source.step(t, a)]),
                   None)
        if bad is None:
            break
        s, t, action = bad
        j = next(i for i in range(len(probes)) if
                 signatures[source.step(s, action)][i] !=
                 signatures[source.step(t, action)][i])
        forced_word = (action,) + probes[j]
        word = forced_word
        mechanism = "obstruction-prefix-constructor"
        if genetic_seed is not None:
            trial = genetic_probe_search(source, s, t,
                seed=genetic_seed + len(obstructions), population=8,
                generations=4, maximum_word_length=len(source.states))
            if trial.genetic_succeeded:
                word = trial.genetic_verified_separator
                mechanism = "evolutionary-word-selection"
                successes += 1
            else:
                repairs += 1
        else:
            repairs += 1
        if word in probes or source.observe(s, word) == source.observe(t, word):
            raise AssertionError("Invalid representation birth witness")
        obstructions.append({"states": (s, t), "action": action,
            "forced_separator": forced_word, "chosen_separator": word,
            "selection": mechanism,
            "metagrammar_supplies_memory_type": True})
        probes.append(word)
        if len(probes) > len(source.states):
            raise AssertionError("Each repair must split a finite residual class")
    groups = {}
    for s in source.states:
        groups.setdefault(signatures[s], []).append(s)
    return MemoryBirth(source, tuple(probes), tuple(signatures[s] for s in source.states),
        tuple(tuple(b) for b in groups.values()), tuple(counts), tuple(obstructions),
        successes, repairs)


def arbitrary_holdout(seed, n):
    """Reachable finite source: one cycle action plus independently random map."""
    rng = Random(seed)
    states = tuple(str(i) for i in range(n))
    outputs = [str(rng.randrange(2)) for _ in states]
    outputs[0], outputs[-1] = "0", "1"
    transitions = (tuple(str((i+1) % n) for i in range(n)),
                   tuple(str(rng.randrange(n)) for _ in states))
    return ActionSource("heldout-%s-%s" % (seed, n), 0, "declared-simulator",
                        states, tuple(outputs), ("advance", "twist"), transitions)


def memory_validation(source, *, genetic_seed=None):
    birth = construct_memory(source, genetic_seed=genetic_seed)
    exact = exhaustive_minimum_quotient(source)
    classical = action_congruence(source)
    if (len(birth.classes) != exact["classes"]
            or {frozenset(b) for b in birth.classes} !=
               {frozenset(b) for b in classical.equivalence_classes}):
        raise AssertionError("Independent minimum memory oracle disagreed")
    checked = 0
    for state in source.states:
        for length in range(5):
            for word in product(source.actions, repeat=length):
                model = birth.predictive_class(state)
                actual = state
                for a in word:
                    model = birth.prediction(model, a)
                    actual = source.step(actual, a)
                if source.report(birth.classes[model][0]) != source.report(actual):
                    raise AssertionError("Fresh action-history forecast failed")
                checked += 1
    splits = max(sum(source.report(block[0]) == label for block in birth.classes)
                 for label in set(source.outputs))
    return {"source_id": source.source_id, "source_states": len(source.states),
        "source_outputs": source.outputs, "source_actions": source.actions,
        "source_transitions": source.transitions,
        "class_counts": birth.class_count_history,
        "minimal_predictive_classes": len(birth.classes),
        "minimum_fixed_memory_bits": (len(birth.classes)-1).bit_length(),
        "supplemental_bits_given_current_report": (splits-1).bit_length(),
        "obstructions": birth.obstructions, "probe_words": birth.probes,
        "genetic_successes": birth.genetic_successes,
        "deterministic_repairs": birth.deterministic_repairs,
        "exhaustive_partition_oracle": exact, "forecast_checks": checked}


@dataclass(frozen=True)
class HistoryPredictor:
    """A generated memory interface: finite output and action tables."""
    alphabet: tuple[str, ...]
    outputs: tuple[str, ...]
    transitions: tuple[tuple[int, ...], ...]
    initial: int

    def run(self, word):
        state=self.initial
        for action in word:
            state=self.transitions[self.alphabet.index(action)][state]
        return self.outputs[state]


def learn_history_memory(alphabet, membership, equivalence, *, max_rounds=100):
    """Angluin-style closed/consistent observation table, Moore-output variant.

    The learner receives only alphabet, word->report calls and an exact
    hypothesis->counterexample teacher. It receives no source cardinality,
    source states, transition arrays, or family formula. Reset-access and the
    equivalence teacher are mathematical assumptions, not supplied hardware.
    A max-rounds stop returns an access/resource gap, never a certificate.
    """
    if (not alphabet or len(set(alphabet))!=len(alphabet)
            or type(max_rounds) is not int or max_rounds<1):
        raise ValueError("Finite alphabet and positive synthesis budget required")
    prefixes=[()];suffixes=[()];answers={};counterexamples=[];closures=consistencies=0
    def ask(word):
        if word not in answers:answers[word]=membership(word)
        return answers[word]
    def row(word):return tuple(ask(word+e) for e in suffixes)
    for iteration in range(max_rounds):
        while True:
            rows={row(s) for s in prefixes}
            missing=next((s+(a,) for s in prefixes for a in alphabet
                          if row(s+(a,)) not in rows),None)
            if missing is not None:
                prefixes.append(missing);closures+=1;continue
            mismatch=next(((s,t,a) for s,t in combinations(prefixes,2)
                           if row(s)==row(t) for a in alphabet
                           if row(s+(a,))!=row(t+(a,))),None)
            if mismatch is not None:
                s,t,a=mismatch
                j=next(j for j in range(len(suffixes)) if
                       row(s+(a,))[j]!=row(t+(a,))[j])
                suffix=(a,)+suffixes[j]
                if suffix in suffixes:raise AssertionError("Consistency repair failed to add information")
                suffixes.append(suffix);consistencies+=1;continue
            break
        distinct=list(dict.fromkeys(row(s) for s in prefixes))
        representatives=[next(s for s in prefixes if row(s)==r) for r in distinct]
        transitions=tuple(tuple(distinct.index(row(s+(a,))) for s in representatives)
                          for a in alphabet)
        model=HistoryPredictor(tuple(alphabet),tuple(ask(s) for s in representatives),
                               transitions,distinct.index(row(())))
        witness=equivalence(model)
        if witness is None:
            return model,{"status":"EXACT_TEACHER_CERTIFIED", "membership_queries":len(answers),
                "equivalence_queries":iteration+1,"counterexamples":counterexamples,
                "closure_repairs":closures,"consistency_repairs":consistencies,
                "prefixes":prefixes,"suffixes":suffixes,
                "hidden_state_table_given_to_learner":False,
                "exact_counterexample_teacher_assumed":True,
                "reset_access_assumed":True}
        if ask(witness)==model.run(witness):raise AssertionError("Teacher returned false counterexample")
        counterexamples.append(witness)
        for length in range(len(witness)+1):
            if witness[:length] not in prefixes:prefixes.append(witness[:length])
    return None,{"status":"UNRESOLVED_RESOURCE_BUDGET","membership_queries":len(answers),
                 "counterexamples":counterexamples}


def declared_history_teacher(source, initial):
    """Private finite source-side teacher; learner sees callable interfaces only."""
    if initial not in source.states:raise ValueError("Unknown prepared initial state")
    def membership(word):return source.observe(initial,word)
    def equivalence(model):
        from collections import deque
        queue=deque([(initial,model.initial,())]);seen={(initial,model.initial)}
        while queue:
            actual,predicted,word=queue.popleft()
            if source.report(actual)!=model.outputs[predicted]:return word
            for i,action in enumerate(source.actions):
                pair=(source.step(actual,action),model.transitions[i][predicted])
                if pair not in seen:
                    seen.add(pair);queue.append((pair[0],pair[1],word+(action,)))
        return None
    return membership,equivalence


def history_learning_validation(source):
    membership,equivalence=declared_history_teacher(source,source.states[0])
    queried=set()
    def recorded_membership(word):
        queried.add(word)
        return membership(word)
    model,receipt=learn_history_memory(source.actions,recorded_membership,equivalence)
    if model is None:raise AssertionError("Finite holdout synthesis exhausted its declared budget")
    oracle=exhaustive_minimum_quotient(source)
    # Validation family guarantees all source states reachable from first state.
    if len(model.outputs)!=oracle["classes"]:raise AssertionError("History learner failed minimum-state oracle")
    checked=0
    for length in (7,8):
        for word in product(source.actions,repeat=length):
            if word in queried:continue
            if model.run(word)!=source.observe(source.states[0],word):
                raise AssertionError("New longer history falsified the learned model")
            checked+=1
    return {"source_id":source.source_id,"learned_predictive_states":len(model.outputs),
            "learning":receipt,"heldout_word_checks":checked,
            "heldout_words_exclude_membership_training_queries":True,
            "independent_minimum_state_oracle":oracle["classes"],
            "predicted_outputs":model.outputs,"predicted_transitions":model.transitions}


def bayesian_calibration(copies=8, balanced_pairs=8):
    """Exact finite worlds; posterior is model-conditional, never truth score."""
    if type(copies) is not int or copies < 1 or type(balanced_pairs) is not int or balanced_pairs < 1:
        raise ValueError("Positive observation counts required")
    correct = Q(3, 4)
    naive = Q(3**copies, 1+3**copies)
    # On a shared-latent yes transcript, H is still Bernoulli(3/4).
    risk = lambda forecast, truth: truth*(1-forecast)**2 + (1-truth)*forecast**2
    misspecified = Q(16**balanced_pairs, 16**balanced_pairs+9**balanced_pairs)
    prediction = (1-misspecified)*Q(1,10) + misspecified*Q(1,5)
    stopped = []
    for k in range(3):
        stopped.append((0,)*k + (1,))
    stopped.append((0,0,0))
    total, calibrated_risk = Q(0), Q(0)
    rows = []
    for trace in stopped:
        laws = [p**sum(trace)*(1-p)**(len(trace)-sum(trace))
                for p in (Q(3,4), Q(1,4))]
        prob = sum(laws)/2
        posterior = laws[0]/sum(laws)
        total += prob
        calibrated_risk += prob*risk(posterior, posterior)
        rows.append({"stopped_trace": trace, "mixture_probability": prob,
                     "posterior_H": posterior})
    if total != 1:
        raise AssertionError("Stopped experiment did not partition source worlds")
    return {"shared_latent_copies": copies, "correct_posterior_H": correct,
        "naive_iid_posterior_H": naive,
        "correct_conditional_brier": risk(correct,correct),
        "naive_conditional_brier": risk(naive,correct),
        "brier_regret": (naive-correct)**2,
        "likelihood_interval_posterior": (Q(2,3),Q(5,6)),
        "misspecified_balanced_pairs": balanced_pairs,
        "misspecified_model_02_posterior": misspecified,
        "misspecified_predictive_probability": prediction,
        "true_heldout_probability": Q(1,2),
        "misspecified_heldout_brier": risk(prediction,Q(1,2)),
        "correct_heldout_brier": Q(1,4),
        "adaptive_stopping": rows, "stopping_calibrated_brier": calibrated_risk}


def optimal_cost(field, target, costs, horizon):
    """Finite-horizon worst-case Bellman; original/current pairs are preserved."""
    if (type(horizon) is not int or horizon < 0 or len(target) != field.count
            or set(costs) != {a.name for a in field.actions}
            or any(type(v) not in (int,Q) or v <= 0 for v in costs.values())):
        raise ValueError("Explicit positive costs, target and finite horizon required")
    @lru_cache(None)
    def solve(belief, remaining):
        if len({target[original] for original, current in belief}) == 1:
            return (Q(0), None)
        if remaining == 0:
            return (None, None)
        choices = []
        for action in field.actions:
            if not all(action.enabled[current] for original,current in belief):
                continue
            groups = {}
            for original, current in belief:
                outcome, after = action.step(current)
                groups.setdefault(outcome, []).append((original, after))
            children = [solve(tuple(sorted(set(group))), remaining-1)[0]
                        for group in groups.values()]
            if all(c is not None for c in children):
                choices.append((Q(costs[action.name])+max(children), action.name))
        return min(choices) if choices else (None,None)
    root = tuple((s,s) for s in range(field.count))
    result = solve(root,horizon)
    return {"worst_case_cost": result[0], "first_action": result[1],
            "cached_belief_horizon_pairs": solve.cache_info().currsize}


def exhaustive_strategy_oracle(field, target, costs, horizon):
    """Generate complete public strategy trees, then simulate all sources.

    No Bellman recurrence, belief memoization, or minimization during tree
    construction. Globally impossible outcome branches are retained; this is
    deliberately independent and exponentially expensive at declared scope.
    """
    if not 0 <= horizon <= 3:
        raise ValueError("Exhaustive strategy-tree budget is horizon <=3")
    @lru_cache(None)
    def trees(depth):
        answer = [None]  # terminate without claiming a particular target
        if depth:
            children = trees(depth-1)
            for action in field.actions:
                alphabet = tuple(sorted(set(action.outputs)))
                for subtrees in product(children, repeat=len(alphabet)):
                    answer.append((action.name, tuple(zip(alphabet, subtrees))))
        return tuple(answer)
    best, checked, valid = None, 0, 0
    for tree in trees(horizon):
        checked += 1
        leaves, expenditures, lawful = {}, [], True
        for original in range(field.count):
            current, node, transcript, paid = original, tree, (), Q(0)
            while node is not None:
                name, branches = node
                action = field.action(name)
                if not action.enabled[current]:
                    lawful = False
                    break
                outcome,current = action.step(current)
                paid += costs[name]
                transcript += ((name,outcome),)
                node = dict(branches)[outcome]
            if not lawful:
                break
            if transcript in leaves and leaves[transcript] != target[original]:
                lawful = False
                break
            leaves[transcript] = target[original]
            expenditures.append(paid)
        if lawful:
            valid += 1
            value = max(expenditures)
            best = value if best is None else min(best,value)
    return {"worst_case_cost": best, "trees_enumerated": checked,
            "valid_trees": valid}


def destructive_greedy_countermodel():
    """Gain/cost likes cheap read-and-destroy; complete source proof cannot."""
    enabled = (True,)*3
    return FiniteCarrier(3, (
        Instrument("cheap",(0,1,1),(0,1,1),enabled),
        Instrument("full",(0,1,2),(0,1,2),enabled)),
        "greedy-destruction", "original-state"), ("0","1","2"), {"cheap":Q(1),"full":Q(5)}


def evaluate_depth_two_genome(field, target, costs, genome, sources=None):
    """Evaluate one typed policy genome independently on source trajectories.

    Root action index, then one STOP(-1)/action index per public outcome.
    Second-level actions end in STOP. No source ID is exposed to the policy.
    """
    alphabet=tuple(sorted({v for a in field.actions for v in a.outputs}))
    if (len(genome)!=1+len(alphabet) or not 0<=genome[0]<len(field.actions)
            or any(not -1<=x<len(field.actions) for x in genome[1:])):
        raise ValueError("Malformed depth-two public policy genome")
    sources=range(field.count) if sources is None else sources
    root=field.actions[genome[0]]
    leaves,paid={},[]
    for original in sources:
        if not root.enabled[original]:return None,(original,)
        first,after=root.step(original)
        spend=Q(costs[root.name]);trace=((root.name,first),)
        child_index=genome[1+alphabet.index(first)]
        if child_index!=-1:
            child=field.actions[child_index]
            if not child.enabled[after]:return None,(original,)
            second,after=child.step(after)
            spend+=costs[child.name];trace+=((child.name,second),)
        if trace in leaves and leaves[trace][0]!=target[original]:
            return None,(leaves[trace][1],original)
        leaves[trace]=(target[original],original);paid.append(spend)
    return max(paid),None


def genetic_cost_policy(field,target,costs,*,seed,population=4,generations=3):
    """Budgeted mutation/crossover of typed depth-two public policy syntax."""
    if (type(seed) is not int or type(population) is not int or population<2
            or type(generations) is not int or generations<1):
        raise ValueError("Declared genetic policy budgets required")
    rng=Random(seed)
    width=1+len({v for a in field.actions for v in a.outputs})
    initial=(0,)+(-1,)*(width-1)
    current=[initial]*population
    evaluated={}
    for _ in range(generations):
        for genome in current:
            evaluated[genome]=evaluate_depth_two_genome(field,target,costs,genome)[0]
        ranked=sorted(current,key=lambda g:(evaluated[g] is None,
                         evaluated[g] if evaluated[g] is not None else Q(10**6),g))
        elite=ranked[:2]
        offspring=elite[:]
        while len(offspring)<population:
            if rng.randrange(3)==0:
                cut=rng.randrange(width)
                child=elite[0][:cut]+elite[1][cut:]
            else:
                child=list(rng.choice(elite));i=rng.randrange(width)
                child[i]=rng.randrange(len(field.actions)) if i==0 else rng.randrange(-1,len(field.actions))
                child=tuple(child)
            offspring.append(child)
        current=offspring
    valid=[(value,genome) for genome,value in evaluated.items() if value is not None]
    best=min(valid) if valid else (None,None)
    return {"seed":seed,"evaluated_genomes":len(evaluated),
            "best_verified_cost":best[0],"best_genome":best[1],
            "exhaustive_rescue_used":False}


def cegis_cost_policy(field,target,costs):
    """Complete bounded grammar enumerator with independent source counterexamples.

    Explicit exhaustive candidate search receives CEGIS credit; genetic search
    receives none. First valid candidate need not be globally cost-optimal on
    arbitrary fields; optimality is separately checked in the countermodel.
    """
    width=len({v for a in field.actions for v in a.outputs})
    grammar=tuple((root,)+tail for root in range(len(field.actions))
                  for tail in product(range(-1,len(field.actions)),repeat=width))
    examples=[0];witnesses=[];checked=0
    while True:
        fitting=[]
        for g in grammar:
            checked+=1
            value,_=evaluate_depth_two_genome(field,target,costs,g,examples)
            if value is not None:fitting.append((value,g))
        if not fitting:return {"best_verified_cost":None,"counterexamples":witnesses,"candidate_evaluations":checked}
        _,candidate=min(fitting)
        value,witness=evaluate_depth_two_genome(field,target,costs,candidate)
        if witness is None:
            return {"best_verified_cost":value,"genome":candidate,
                    "counterexamples":witnesses,"candidate_evaluations":checked,
                    "grammar_size":len(grammar),
                    "global_cost_optimality_without_oracle_claimed":False}
        unseen=next((s for s in witness if s not in examples),None)
        if unseen is None:raise AssertionError("CEGIS counterexample already fitted")
        examples.append(unseen);witnesses.append(unseen)


def similarity_control(count=9):
    """Non-diagonal independent recurrence for a rational similarity twin."""
    # T=[[1,1],[0,1]]: A'=T diag(1/2,1/3) T^-1, b'=Tb, c'=cT^-1.
    x,y=Q(2),Q(1)
    outputs=[]
    for _ in range(count):
        outputs.append(x)
        x,y=Q(1,2)*x-Q(1,6)*y,Q(1,3)*y
    return tuple(outputs)


def linear_moments(diagonal, b, c, count):
    if len(diagonal) != len(b) or len(b) != len(c):
        raise ValueError("Aligned diagonal linear source required")
    return tuple(sum((Q(ci)*Q(bi)*Q(ai)**n for ai,bi,ci in zip(diagonal,b,c)),Q(0))
                 for n in range(count))


def hidden_mode_receipt():
    """A hidden unreachable mode becomes observable under a new input."""
    diagonal = (Q(1,2),Q(1,3),Q(3,4))
    old = linear_moments(diagonal,(1,1,0),(1,1,1),9)
    new = linear_moments(diagonal,(0,0,1),(1,1,1),9)
    minimal = linear_moments(diagonal[:2],(1,1),(1,1),9)
    block = tuple(tuple(samples[i+j] for samples in (old,new) for j in range(3))
                  for i in range(3))
    return {"old_input_moments":old, "new_input_moments":new,
        "minimal_two_state_moments":minimal,
        "old_input_rank":rank(hankel(old,4,4)),
        "augmented_input_block_rank":rank(block),
        "all_time_old_input_equality":True,
        "new_input_exposes_hidden_mode":new[0] != 0}


def resource_receipt(width=4, delay=19):
    """Communication collision proof and explicit delayed one-probe witness."""
    if type(width) is not int or not 1 <= width <= 8 or type(delay) is not int or delay < 0:
        raise ValueError("Declared finite resources required")
    strings = tuple(product((0,1),repeat=width))
    edges = []
    for s,t in combinations(strings,2):
        i = next(j for j in range(width) if s[j] != t[j])
        edges.append((s,t,i))
    states=tuple(str(i) for i in range(delay+2))
    source=ActionSource("delayed-pulse-%d"%delay,0,"stationary-clock",states,
        tuple("1" if i==delay else "0" for i in range(delay+2)),
        ("advance",),(tuple(str(min(i+1,delay+1)) for i in range(delay+2)),))
    observations=tuple(source.observe("0",("advance",)*i) for i in range(delay+3))
    first=next(i for i,v in enumerate(observations) if v!="0")
    if first!=delay:raise AssertionError("Delayed witness source failed")
    return {"source_strings":len(strings), "pair_collision_witnesses":edges,
        "one_way_zero_error_fixed_bits_lower_bound":width,
        "minimum_messages":2**width, "individual_answer_bits":1,
        "delayed_source": {"one_at_time":delay,"zero_elsewhere":True,
                           "observed_prefix":observations,"source_state_count":len(states)},
        "all_zero_target_refutation_probes":1,
        "shortest_refuting_unary_word_length":first,
        "sequential_action_cost":delay,
        "random_access_cost_if_licensed":1,
        "computability_from_supplied_delay":True,
        "uniform_bound_from_certificate_cardinality":False}
