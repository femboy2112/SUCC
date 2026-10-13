"""Opaque-label holdouts for object-language growth and law discovery.

Simulator coordinates are NEVER passed to the learner. The learner sees a finite
transition table and readout; it constructs separating experiment words, a minimal
quotient, and an action-composition object. Generic word/center/order mining is
predeclared; the resulting nonabelian law is not supplied as a target expression.
Classical finite Heisenberg-type behavior, not a newly discovered theorem for humanity.
"""
from __future__ import annotations
from dataclasses import replace
from hashlib import sha256
from itertools import product
from random import Random
from .evolving_observer_categories import (
    FiniteDynamics, Action, Readout, Experiment, SynthesisError,
    discover_representation, verify_quotient, transformation_monoid,
    first_defect, observed_partition,
)


def hidden_carrier(prime: int, label_seed: int, *, extra_access: bool = False):
    """The generator owns the latent coordinates; downstream learning never does."""
    if prime < 2 or any(prime % k == 0 for k in range(2, prime)) or prime > 7:
        raise SynthesisError('This holdout suite uses small authentic prime clocks')
    raw = list(product(range(prime), repeat=3))
    Random(label_seed).shuffle(raw)
    index = {state: i for i, state in enumerate(raw)}
    def alpha(v):
        x, y, z = v
        return ((x+1) % prime, y, (z+y) % prime)
    def beta(v):
        x, y, z = v
        return (x, (y+1) % prime, z)
    actions = [Action('a', tuple(index[alpha(v)] for v in raw)),
               Action('b', tuple(index[beta(v)] for v in raw))]
    if extra_access:
        actions.append(Action('new_sensor_act', tuple(index[(v[2], v[1], v[0])] for v in raw)))
    opaque_id = sha256(repr((prime, label_seed)).encode()).hexdigest()[:16]
    source = FiniteDynamics('opaque-holdout-'+opaque_id, 0, 'finite-generator-v1',
                            tuple(actions), (Readout('r', tuple(v[2] for v in raw)),))
    return source, tuple(raw)


def _compose(f, g):
    return tuple(g[f[x]] for x in range(len(f)))


def permutation_order(f, *, bound=4096):
    identity = tuple(range(len(f)))
    current = identity
    for k in range(1, bound+1):
        current = _compose(current, f)
        if current == identity:
            return k
    raise SynthesisError('UNRESOLVED_ELEMENT_ORDER')


def mine_generic_laws(q):
    """No prime, latent coordinates or desired relation is an input here."""
    monoid = transformation_monoid(q)
    identity = monoid['identity']
    if not monoid['is_group']:
        return {'size': len(monoid['elements']), 'group': False, 'central_commutator': None}
    a, b = q.actions[0].after, q.actions[1].after
    commutator = _compose(_compose(_compose(a, b), monoid['inverses'][a]), monoid['inverses'][b])
    central = commutator in monoid['center']
    oa, ob, oh = (permutation_order(x) for x in (a, b, commutator))
    def powers(f, order):
        ans = [identity]
        for _ in range(1, order):
            ans.append(_compose(ans[-1], f))
        return ans
    normal_forms = {_compose(_compose(ai, bj), hk)
                    for ai, bj, hk in product(powers(a, oa), powers(b, ob), powers(commutator, oh))}
    return {'size': len(monoid['elements']), 'group': True,
            'center_size': len(monoid['center']),
            'generators_commute': _compose(a, b) == _compose(b, a),
            'central_commutator': central, 'commutator_is_identity': commutator == identity,
            'orders': [oa, ob, oh],
            'normal_form_count': len(normal_forms),
            'normal_form_complete': normal_forms == set(monoid['elements']),
            'normal_form_unique': len(normal_forms) == oa*ob*oh}


def withheld_path_check(source, q, seed):
    """A separate finite path oracle on words NOT used to grow the readout basis."""
    rng = Random(seed)
    qa = {a.name: a.after for a in q.actions}
    qr = q.readouts[0].values
    checks = 0
    for length in (13, 29, 67):
        for _ in range(12):
            word = tuple(rng.choice(source.actions).name for _ in range(length))
            state = rng.randrange(source.count)
            coarse = q.labels[state]
            for action in word:
                coarse = qa[action][coarse]
            if qr[coarse] != source.readouts[0].values[source.run(state, word)]:
                raise AssertionError('Fresh word prediction failed')
            checks += 1
    return checks


def discovery_case(prime, label_seed, *, seed=42):
    source, latent = hidden_carrier(prime, label_seed)
    baseline_tests = (Experiment((), 'r'),)
    failed = first_defect(source, baseline_tests)
    if failed is None:
        raise AssertionError('The no-growth ablation should expose missing dynamic state')
    q = discover_representation(source, seed=seed)
    laws = mine_generic_laws(q)
    fresh_checks = withheld_path_check(source, q, label_seed+1000)
    # Audit only, after learning: check which latent coordinates were recoverable.
    hidden_sizes = sorted({q.labels.count(k) for k in set(q.labels)})
    latent_pair = {}
    for i, (_, y, z) in enumerate(latent):
        if q.labels[i] in latent_pair and latent_pair[q.labels[i]] != (y, z):
            raise AssertionError('Discovered quotient does not match independent source derivation')
        latent_pair[q.labels[i]] = (y, z)
    # A new physical action is NOT silently admitted into an old certificate.
    changed, _ = hidden_carrier(prime, label_seed, extra_access=True)
    stale_rejected = False
    try:
        verify_quotient(changed, q)
    except SynthesisError:
        stale_rejected = True
    expanded = discover_representation(changed, seed=seed)
    return {'prime_for_audit_only': prime, 'source_states': source.count,
            'initial_observation_states': len(set(observed_partition(source, baseline_tests))),
            'discovered_states': q.states, 'fiber_sizes': hidden_sizes,
            'invented_experiments': [list(t.word)+[t.readout] for t in q.tests],
            'strict_refinement_counts': list(q.block_counts),
            'learned_obstructions': len(q.witnesses),
            'archived_bad_proposals_pruned': sum(not admitted for _, admitted in q.candidate_trace),
            'generic_discovered_laws': laws, 'fresh_word_checks': fresh_checks,
            'changed_toolkit_rejected': stale_rejected, 'expanded_toolkit_states': expanded.states,
            'source_coordinates_given_to_learner': False,
            'full_declared_transition_oracle_used': True,
            'physical_source_authenticated': False,
            'unknown_theorem_for_humanity_claimed': False}
