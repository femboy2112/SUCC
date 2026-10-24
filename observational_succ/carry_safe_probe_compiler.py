"""Adaptive weighted-minimax probe compiler for finite source-controlled carriers.

Johann's survey of the laboratory found two adjacent solvers and one gap:
``adaptive_proof_policy.solve_adaptive_claim`` plans an adaptive separating
policy minimizing worst-case STEP COUNT (unit cost); ``online_source_games.
minimum_probe_repair`` minimizes a weighted cost over a FIXED (non-adaptive)
probe bundle. Neither does adaptive planning with per-probe WEIGHTED costs.
This module is that fusion.

Input (the carry-safe probe-compilation problem):
  * a FiniteCarrier with source-dependent (deterministic) probe transitions,
  * a finite predeclared candidate-source family,
  * a per-probe cost (positive Fraction) -- authenticated instruments,
  * a target labeling to certify (e.g. the hidden residue),
  * optionally a prior over sources (for the expected-cost mode).
Output (CompilerVerdict):
  * an adaptive probe policy (belief -> (probe, cost)),
  * the exact predicted response partitions (belief -> {outcome: child belief}),
  * the worst-case (or weighted expected) minimax cost,
  * a separation certificate validated by simulation on every source, OR
  * an impossibility certificate: a differently-targeted source pair that is
    aliased under every probe word.

Correctness is pinned three ways: (a) with unit costs and worst-case mode the
value equals solve_adaptive_claim's rank (the existing engine); (b) the policy
is re-simulated on every source; (c) an INDEPENDENT brute-force DFS minimax
oracle must return the same optimal cost on small systems. Reuses the belief
semantics of adaptive_proof_policy verbatim (``_options``/``_terminal``/
``_belief``). No physical/quantum/RH conclusion follows.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Mapping, Optional

from observational_succ.noncommuting_proof_transport import (
    FiniteCarrier, Instrument, _sources,
)
from observational_succ.adaptive_proof_policy import (
    _belief, _options, _terminal, solve_adaptive_claim,
)


class ProbeCompilerError(ValueError):
    """Malformed costs, sources, target, prior, or an unseparable closure."""


def _check_costs(field, cost):
    if type(cost) is not dict:
        raise ProbeCompilerError("cost must be a dict name->Fraction")
    names = {a.name for a in field.actions}
    out = {}
    for a in field.actions:
        c = cost.get(a.name)
        if not isinstance(c, (int, Q)) or isinstance(c, bool) or c <= 0:
            raise ProbeCompilerError(f"positive exact cost required for probe {a.name!r}")
        out[a.name] = Q(c)
    if set(cost) - names:
        raise ProbeCompilerError("cost names must be declared probes")
    return out


# ---------------------------------------------------------------------------
# the belief closure (shared with adaptive_proof_policy)
# ---------------------------------------------------------------------------

def _closure(field, sources, max_beliefs):
    root = _belief((s, s) for s in sources)
    beliefs = [root]
    seen = {root}
    options = {}
    i = 0
    while i < len(beliefs):
        b = beliefs[i]
        i += 1
        options[b] = _options(field, b)
        for branches in options[b].values():
            for _, child in branches:
                if child not in seen:
                    if len(seen) >= max_beliefs:
                        raise ProbeCompilerError("belief closure exceeded budget")
                    seen.add(child)
                    beliefs.append(child)
    return root, beliefs, options


def _source_mass(belief, prior):
    return sum((prior[s] for s, _ in belief), Q(0))


# ---------------------------------------------------------------------------
# the weighted-minimax value iteration (the novel core)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CompilerVerdict:
    target_id: str
    mode: str
    root: tuple
    cost: Optional[Q]                     # None iff not winning
    winning: bool
    policy: tuple                          # ((belief, probe, cost), ...)
    partitions: tuple                      # ((belief, ((outcome, child), ...)), ...)
    impossibility: Optional[tuple]         # (source_a, source_b, reason) or None


def solve_weighted_adaptive(field, cost, sources, target, *, target_id,
                            mode="worstcase", prior=None, max_beliefs=4096):
    """Compile the cost-optimal adaptive separating policy (see module docstring)."""
    _sources(field, sources)
    cost = _check_costs(field, cost)
    if (type(target) is not tuple or len(target) != field.count
            or any(type(v) is not str for v in target)
            or not isinstance(target_id, str) or not target_id):
        raise ProbeCompilerError("one target label per carrier state required")
    if mode not in ("worstcase", "expected"):
        raise ProbeCompilerError("mode must be 'worstcase' or 'expected'")
    if mode == "expected":
        if type(prior) is not dict or set(prior) != set(sources):
            raise ProbeCompilerError("expected mode needs a prior over exactly the sources")
        pr = {s: Q(prior[s]) for s in sources}
        if any(v <= 0 for v in pr.values()) or sum(pr.values()) != 1:
            raise ProbeCompilerError("prior must be positive and sum to 1")
    else:
        pr = None

    root, beliefs, options = _closure(field, sources, max_beliefs)
    terminal = {b: _terminal(b, target) for b in beliefs}
    value = {b: (Q(0) if terminal[b] is not None else None) for b in beliefs}
    choice = {}

    def aggregate(b, branches):
        child_vals = [value[child] for _, child in branches]
        if any(v is None for v in child_vals):
            return None
        if mode == "worstcase":
            return max(child_vals)
        mass = _source_mass(b, pr)
        return sum((_source_mass(child, pr) / mass) * value[child]
                   for _, child in branches)

    # monotone value iteration; converges in <= |beliefs| sweeps for positive costs
    for _ in range(len(beliefs) + 2):
        changed = False
        for b in beliefs:
            if terminal[b] is not None:
                continue
            best = None
            best_name = None
            for name, branches in options[b].items():
                agg = aggregate(b, branches)
                if agg is None:
                    continue
                total = cost[name] + agg
                if best is None or total < best:
                    best, best_name = total, name
            if best is not None and (value[b] is None or best < value[b]):
                value[b], choice[b] = best, best_name
                changed = True
        if not changed:
            break
    else:
        raise ProbeCompilerError("value iteration did not converge (bug)")

    winning = value[root] is not None
    policy = tuple(sorted((b, choice[b], value[b]) for b in choice))
    partitions = tuple(sorted(
        (b, tuple(sorted((o, c) for o, c in
                         sum((list(br) for br in options[b].values()), []))))
        for b in beliefs))
    impossibility = None
    if not winning:
        impossibility = _impossibility_certificate(field, sources, target)
    return CompilerVerdict(target_id, mode, root, value.get(root), winning,
                           policy, partitions, impossibility)


def _impossibility_certificate(field, sources, target):
    """A differently-targeted source pair aliased under every probe word.

    Two sources are separable iff some action word makes their outputs differ;
    computed by BFS over current-state pairs. The first unseparable pair with
    differing target labels is the impossibility receipt.
    """
    from collections import deque
    for i, s in enumerate(sources):
        for t in sources[i + 1:]:
            if target[s] == target[t]:
                continue
            # BFS over (state_s, state_t); separable if outputs ever differ
            queue = deque([(s, t)])
            seen = {(s, t)}
            separable = False
            while queue:
                x, y = queue.popleft()
                for a in field.actions:
                    if not (a.enabled[x] and a.enabled[y]):
                        # availability asymmetry would separate; same availability continues
                        if a.enabled[x] != a.enabled[y]:
                            separable = True
                            break
                        continue
                    ox, nx = a.step(x)
                    oy, ny = a.step(y)
                    if ox != oy:
                        separable = True
                        break
                    if (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
                if separable:
                    break
            if not separable:
                return (s, t, "aliased: identical outputs under every probe word")
    return None


def simulate_policy(field, verdict, cost, source, target):
    """Re-run the compiled policy on one source; return (label, total_cost, trace).

    Validates that the policy certifies the correct target label, that each
    simulated causal event is consistent with the response partition, and
    accumulates the declared probe costs. For worst-case mode the returned
    total is <= verdict.cost (the worst-case bound).
    """
    if not verdict.winning:
        raise ProbeCompilerError("no winning policy to simulate")
    cost = _check_costs(field, cost)
    pol = {b: name for b, name, _ in verdict.policy}
    belief, state, total, trace = verdict.root, source, Q(0), []
    for _ in range(len(verdict.policy) + 1):
        label = _terminal(belief, target)
        if label is not None:
            if label != target[source]:
                raise ProbeCompilerError("policy certified the wrong target")
            return label, total, tuple(trace)
        if belief not in pol:
            raise ProbeCompilerError("missing winning continuation")
        name = pol[belief]
        branches = dict(_options(field, belief)[name])
        obs, nxt = field.action(name).step(state)
        if obs not in branches or (source, nxt) not in branches[obs]:
            raise ProbeCompilerError("impossible simulated event")
        trace.append((name, obs))
        total += cost[name]
        belief, state = branches[obs], nxt
    raise ProbeCompilerError("policy did not terminate within its own rank")


# ---------------------------------------------------------------------------
# independent brute-force minimax oracle (different algorithm: DFS, cycle-cut)
# ---------------------------------------------------------------------------

def bruteforce_worstcase_cost(field, cost, sources, target, *, max_beliefs=4096):
    """Independent DFS minimax: min over probes of cost + max over outcomes.

    Revisiting a belief on the current path can only add positive cost, so it
    is cut (returns infinity). This is a structurally different algorithm from
    the value iteration in :func:`solve_weighted_adaptive`; agreement on the
    root cost is a genuine cross-check.
    """
    _sources(field, sources)
    cost = _check_costs(field, cost)
    root = _belief((s, s) for s in sources)

    def best(belief, on_path):
        label = _terminal(belief, target)
        if label is not None:
            return Q(0)
        if belief in on_path or len(on_path) > max_beliefs:
            return None                       # infinity: revisiting cannot help
        nxt = on_path | {belief}
        options = _options(field, belief)
        candidate = None
        for name, branches in options.items():
            child_costs = [best(child, nxt) for _, child in branches]
            if any(c is None for c in child_costs):
                continue
            total = cost[name] + max(child_costs)
            if candidate is None or total < candidate:
                candidate = total
        return candidate

    return best(root, frozenset())


# ---------------------------------------------------------------------------
# concrete arithmetic instances (ties to FSO-01 and an impossibility case)
# ---------------------------------------------------------------------------

def residue_observer_carrier(p):
    """Finite carrier: states {0..2p-1} index n=state+1; probe S reads the

    quotient block of n and advances n->n+1. Sources are the first block
    {0..p-1} (n in 1..p), hidden residue r=state. Target = the residue label.
    S is enabled wherever n+1 stays in range (n <= 2p-1), which covers every
    source plus its p-1 successors.
    """
    if type(p) is not int or p < 2:
        raise ProbeCompilerError("modulus p >= 2 required")
    size = 2 * p
    # n = state + 1; quotient block = (n-1)//p = state//p ; output that block
    outputs = tuple(state // p for state in range(size))
    transitions = tuple(min(state + 1, size - 1) for state in range(size))
    enabled = tuple(state + 1 < size for state in range(size))
    field = FiniteCarrier(size, (Instrument("S", outputs, transitions, enabled),),
                          "residue-observer", f"carry-safe-p{p}")
    sources = tuple(range(p))                 # residues 0..p-1 in block 0
    target = tuple(str(state % p) for state in range(size))
    return field, sources, target


def aliased_carrier():
    """Two differently-targeted sources aliased under the only probe.

    States 0,1 both self-loop under 'R' with output 0; their targets differ.
    No probe word separates them -> impossibility certificate.
    """
    outputs = (0, 0)
    transitions = (0, 1)
    enabled = (True, True)
    field = FiniteCarrier(2, (Instrument("R", outputs, transitions, enabled),),
                          "aliased", "impossible-v1")
    sources = (0, 1)
    target = ("A", "B")
    return field, sources, target


def residue_certification_cost(p, probe_cost=Q(1)):
    """Worst-case cost to certify the hidden residue on the quotient-only carrier.

    Computed three independent ways (value iteration, the existing unit-cost
    engine, and the brute-force DFS), which agree. The compiler's probe is
    observe-then-advance, so each probe makes an observation and THEN applies S.
    The exact relationship to FSO-01 (verified in
    :func:`pairwise_cost_is_fso_advance_plus_warmup`):

        probe cost to separate residues r<s  =  (p - s) + 1
                                             =  FSO-01 advance length  +  1,

    the +1 being the uninformative k=0 warm-up observation. Hence:

      * the hardest pair (residues 0,1) costs (p-1)+1 = p;
      * full residue-REGISTER certification also costs p (the warm-up is shared,
        then one residue peels off per subsequent probe).

    So the probe compiler reproduces FSO-01's advance length p-1 up to the
    single, honestly-accounted observe-then-advance warm-up.
    """
    field, sources, target = residue_observer_carrier(p)
    cost = {"S": Q(probe_cost)}
    full = solve_weighted_adaptive(field, cost, sources, target,
                                   target_id="hidden-residue")
    unit = solve_adaptive_claim(field, sources, target, target_id="hidden-residue")
    brute = bruteforce_worstcase_cost(field, cost, sources, target)
    pair = solve_weighted_adaptive(field, cost, (0, 1), target,
                                   target_id="hidden-residue")
    return {
        "winning": full.winning,
        "full_register_cost": full.cost,          # probe_cost * p
        "unit_rank": unit.rank,                   # p
        "bruteforce_cost": brute,                 # probe_cost * p (independent)
        "hardest_pair_cost": pair.cost,           # probe_cost * p = (p-1)+1
        "fso_advance_plus_warmup": p,             # (p-1) + 1
    }


def pairwise_cost_is_fso_advance_plus_warmup(p):
    """Exact Phase-5<->Phase-2 tie: for every residue pair r<s on the carrier,

    the unit probe cost equals min_separation(r+1, s+1, p) + 1 (FSO-01 advance
    length plus the one observe-then-advance warm-up). Returns a dict
    (r,s) -> (probe_cost, fso_advance_plus_one); all entries must be equal pairs.
    """
    from observational_succ.future_sufficient_information import min_separation
    field, _, target = residue_observer_carrier(p)
    out = {}
    for r in range(p):
        for s in range(r + 1, p):
            v = solve_weighted_adaptive(field, {"S": Q(1)}, (r, s), target,
                                        target_id="hidden-residue")
            advance = min_separation(r + 1, s + 1, p)      # = p - s
            out[(r, s)] = (v.cost, advance + 1)
    return out
