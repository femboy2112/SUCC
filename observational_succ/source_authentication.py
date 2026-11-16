"""Exact finite source-authentication interface; model/record separation.

Requires a declared joint source law, a registered action contract, and actual
readouts. Probabilistic calibration is conditional on a source model; SHA-256
commitments only bind a realized pseudorandom/OS-random tape to its replay.
No physical source-law certification or omniscient hidden-state probe is claimed.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from itertools import product

from observational_succ.recursive_observer import (
    JointInstrument, initial_pairs, update_current, update_pair, rational,
)

Q = Fraction
ACTIONS = ("sense", "flip", "reset")
CREDITS = {"sense": 2, "flip": 1, "reset": 4}


def source_instruments(accuracy: Q):
    """Predeclared joint J: read-old bit and optionally flip/reset current."""
    p = rational(accuracy)
    if not 0 < p < 1:
        raise ValueError("Require nondegenerate rational read accuracy")
    out = []
    for action in ACTIONS:
        nout = 1 if action == "flip" else 2
        table = [[[Q(0) for _ in range(nout)] for _ in range(2)]
                 for _ in range(2)]
        for x in range(2):
            if action == "flip":
                table[x][1-x][0] = Q(1)
            else:
                nxt = x if action == "sense" else 0
                table[x][nxt][x] = p
                table[x][nxt][1-x] = Q(1)-p
        out.append(JointInstrument(
            tuple(tuple(tuple(c) for c in row) for row in table),
            Q(CREDITS[action]), "registered-"+action))
    return tuple(out)


def choose_registered_action(turn: int, model_current: tuple[Q,Q]) -> str:
    """Public predictable policy; uses no latent bit or revealed tape."""
    if type(turn) is not int or turn < 0:
        raise ValueError("turn must be nonnegative int")
    if len(model_current) != 2 or sum(model_current, Q(0)) != 1:
        raise ValueError("belief must be normalized")
    if turn > 0 and turn % 5 == 4:
        return "flip" if model_current[1] >= Q(1,2) else "reset"
    return "sense"


@dataclass
class ModelEvidence:
    """Fitted nowhere: both model kernels are frozen before the trace."""
    alternative: Q = Q(3,4)
    null: Q = Q(1,2)

    def __post_init__(self):
        self.instruments = (source_instruments(self.alternative),
                            source_instruments(self.null))
        self.beliefs = [(Q(1,2), Q(1,2)), (Q(1,2), Q(1,2))]
        self.pair_beliefs = [initial_pairs((Q(1,2),Q(1,2))) for _ in range(2)]
        self.likelihoods = [Q(1), Q(1)]
        self.credit_total = 0
        self.records = []

    def action(self) -> str:
        return choose_registered_action(len(self.records), self.beliefs[0])

    def predictive(self, action: str) -> tuple[tuple[Q,...], tuple[Q,...]]:
        i = ACTIONS.index(action)
        laws = []
        for prior, insts in zip(self.beliefs, self.instruments):
            inst = insts[i]
            preds = tuple(update_current(prior,inst,o)[0]
                          for o in range(inst.output_count))
            assert sum(preds,Q(0)) == 1
            laws.append(preds)
        return tuple(laws)

    def record(self, action: str, outcome: int):
        if action != self.action():
            raise ValueError("Action not selected by recorded policy")
        if type(outcome) is not int:
            raise ValueError("Outcome must be a typed integer")
        i = ACTIONS.index(action)
        prior_predictions = self.predictive(action)
        beliefs_new = []
        for m, (belief, insts) in enumerate(zip(self.beliefs,self.instruments)):
            z,b = update_current(belief,insts[i],outcome)
            z_pair,pair_next = update_pair(self.pair_beliefs[m],insts[i],outcome)
            if z == 0 or b is None:
                raise ValueError("An actually recorded outcome was outside model support")
            if z_pair != z or pair_next is None or any(
                  sum((pair_next[u][xp] for u in range(2)),Q(0)) != b[xp]
                  for xp in range(2)):
                raise ArithmeticError("Retrospective and current filters disagree")
            self.pair_beliefs[m] = pair_next
            self.likelihoods[m] *= z
            beliefs_new.append(b)
        self.beliefs=beliefs_new
        self.credit_total += CREDITS[action]
        e=self.likelihoods[0]/self.likelihoods[1]
        self.records.append({"action":action,"outcome":outcome,
                             "p_alt":prior_predictions[0],
                             "p_null":prior_predictions[1],
                             "evidence":e})
        return e

    @property
    def e_value(self):
        return self.likelihoods[0]/self.likelihoods[1]

    def original_posterior(self, model=0):
        b=self.pair_beliefs[model]
        return tuple(sum(row,Q(0)) for row in b)


def fixed_policy_null_census(depth=6, threshold=Q(4)):
    """Exact E_null L_n=1 and Ville event bound under adaptive actions.

    Full finite transcript tree, no Monte Carlo and no source-state access.
    """
    if type(depth) is not int or not 0 <= depth <= 11:
        raise ValueError("Depth capped to prevent exponential work")
    seen_nodes=0
    cross_probability=Q(0)
    expectation=Q(0)
    def walk(model, n, null_mass, crossed):
        nonlocal seen_nodes, expectation, cross_probability
        if n == depth:
            seen_nodes+=1
            expectation += null_mass*model.e_value
            if crossed:cross_probability+=null_mass
            return
        a=model.action()
        q=model.predictive(a)[1]
        for o,p in enumerate(q):
            if p == 0: continue
            import copy
            child=copy.deepcopy(model)
            child.record(a,o)
            walk(child,n+1,null_mass*p,crossed or child.e_value>=threshold)
    walk(ModelEvidence(),0,Q(1),Q(1)>=threshold)
    return {"depth":depth,"endpoints":seen_nodes,
            "null_E_L":expectation,
            "null_cross_probability":cross_probability,
            "ville_cap":Q(1)/threshold}


def brier_binary(prediction_one: Q, outcome: int) -> Q:
    if type(outcome) is not int or outcome not in (0,1):
        raise ValueError("binary output")
    p=rational(prediction_one)
    if not Q(0)<=p<=Q(1):raise ValueError("valid probability")
    return (p-Q(outcome))**2 + ((Q(1)-p)-(Q(1)-Q(outcome)))**2


def predictive_equivalence_by_history(models, action_words, outcome_words):
    """Finite supplied-family check; not universal closure beyond supplied words."""
    return all(models[0](a,o)==models[1](a,o)
               for a,o in zip(action_words,outcome_words))


def field_axes(*, source_exists=None, source_attested=None, target_descends=None,
               finite_query_program=None, global_witness_proved=None,
               no_computable_witness_proved=None, phantom_original_lift=None):
    """Conservative evidence ledger; no simulated probabilities for truth.

    None = not established; proven mathematical source facts are distinct
    from actual physical correspondence. Labels are non-exclusive diagnostics.
    """
    inputs=locals().copy()
    if any(not (v is None or type(v) is bool) for v in inputs.values()):
        raise ValueError("Evidence axes must be bool or unknown")
    conflicts=[]
    if source_exists is False and global_witness_proved is True:
        conflicts.append("global existence and global witness contradict")
    if no_computable_witness_proved and finite_query_program:
        conflicts.append("computable and noncomputable witness contradict for same target/toolkit")
    if source_attested and source_exists is False:
        conflicts.append("attested existent source and source nonexistence contradict")
    if conflicts:
        return {"verdict":"INCOHERENT","reasons":tuple(conflicts),"axes":inputs}
    modes=[]
    if source_exists is False:modes.append("FuckedField/nonexistence")
    if target_descends is False:modes.append("FuckedField/nonidentifiability")
    if phantom_original_lift is True:modes.append("FuckedField/phantom-source-map")
    if global_witness_proved and no_computable_witness_proved:
        modes.append("IdealHardField")
    if finite_query_program and source_exists is True and target_descends is not False:
        modes.append("SimpleField/model-relative")
    if not modes:modes.append("UNRESOLVED/toolkit-relative")
    return {"verdict":"MULTI_AXIS","modes":tuple(modes),"axes":inputs,
            "physical_source_certified":source_attested is True}


def tagged_source_transcript(visible: int, hidden_tag: int, actions: tuple[str, ...]):
    """A truly unobservable tag persists through permitted read/flip actions."""
    if visible not in (0,1) or hidden_tag not in (0,1):
        raise ValueError("two binary source coordinates")
    current=(visible,hidden_tag)
    record=[]
    for action in actions:
        if action=='read':
            record.append(current[0])
        elif action=='flip':
            current=(1-current[0],current[1])
            record.append(None)
        else:
            raise ValueError("No hidden-tag probe is lawful")
    return tuple(record), current


def delayed_mutant(horizon: int, alternative: bool):
    """First horizon observations identical; differs exactly on next event."""
    if type(horizon) is not int or not 0<=horizon<=10000:
        raise ValueError("bounded horizon")
    return tuple([0]*horizon+[1 if alternative else 0])
