"""Finite structural coupling discovery with source-relative observation gates.

This is a DECLARED finite mathematical laboratory.  It enumerates group
extensions C_k -> A -> C_q, not arbitrary mathematical structures, and uses
exact source-model tables.  A mathematical prediction is never an executed
physical observation.  The class of models and primitive actions is stipulated.

Two different coupling mechanisms are explored:
  * an action rho: C_q -> Aut(C_k), and
  * a normalized twisted 2-cocycle f: C_q x C_q -> C_k.

All arithmetic is exact.  Group-extension classification is classical.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from math import gcd
from typing import Mapping, Sequence

Element = tuple[int, int]  # (kernel coordinate, quotient coordinate)


class CouplingError(ValueError):
    """Bad mathematical source, inadmissible operation, or forged receipt."""


class OutOfModel(CouplingError):
    """An observation has zero likelihood in the stipulated candidate family."""


def _is_int(x: object) -> bool:
    return type(x) is int


@dataclass(frozen=True)
class CyclicExtension:
    """C_k ⋊_{rho,f} C_q in a fixed, explicitly labelled extension frame.

    Multiplication (b,x)*(c,y) = (b + rho(x)c + f(x,y), x+y).
    The cocycle MUST satisfy the twisted 2-cocycle equation; we do not repair
    an invalid table by silently changing the underlying source group.
    """

    kernel: int
    quotient: int
    multiplier: int
    cocycle: tuple[int, ...]  # row-major, including zero row/column

    def __post_init__(self) -> None:
        k, q, g, f = self.kernel, self.quotient, self.multiplier, self.cocycle
        if not all(_is_int(a) for a in (k, q, g)) or not 2 <= k <= 12 or not 2 <= q <= 12:
            raise CouplingError("Finite cyclic kernel and quotient (2..12) required")
        if not _is_int(g) or not 1 <= g < k or gcd(k, g) != 1 or pow(g, q, k) != 1:
            raise CouplingError("The quotient generator must act by an automorphism of order dividing q")
        if type(f) is not tuple or len(f) != q*q or any(not _is_int(t) or not 0 <= t < k for t in f):
            raise CouplingError("Complete exact residue-valued cocycle table required")
        if any(f[x*q] != 0 or f[x] != 0 for x in range(q)):
            raise CouplingError("The cocycle must be normalized at the identity")
        for x, y, z in product(range(q), repeat=3):
            lhs = f[x*q+y] + f[((x+y)%q)*q+z]
            rhs = pow(g, x, k)*f[y*q+z] + f[x*q+(y+z)%q]
            if (lhs-rhs) % k:
                raise CouplingError("Twisted cocycle / associativity equation fails")

    @property
    def identity(self) -> Element:
        return (0, 0)

    @property
    def elements(self) -> tuple[Element, ...]:
        return tuple(product(range(self.kernel), range(self.quotient)))

    def multiply(self, a: Element, b: Element) -> Element:
        self.check_element(a)
        self.check_element(b)
        u, x = a
        v, y = b
        return ((u + pow(self.multiplier, x, self.kernel)*v
                 + self.cocycle[x*self.quotient+y]) % self.kernel,
                (x+y) % self.quotient)

    def check_element(self, v: Element) -> None:
        if (type(v) is not tuple or len(v) != 2 or
                not all(_is_int(i) for i in v) or
                not 0 <= v[0] < self.kernel or not 0 <= v[1] < self.quotient):
            raise CouplingError("Action/state outside the declared common extension carrier")

    def right_step(self, state: Element, action: Element) -> Element:
        return self.multiply(state, action)

    def element_order(self, element: Element) -> int:
        self.check_element(element)
        state = self.identity
        for n in range(1, self.kernel*self.quotient + 1):
            state = self.multiply(state, element)
            if state == self.identity:
                return n
        raise AssertionError("Cocycle-checked finite group unexpectedly lacked inverses")

    def order_histogram(self) -> tuple[tuple[int, int], ...]:
        orders = [self.element_order(t) for t in self.elements]
        return tuple((n, orders.count(n)) for n in sorted(set(orders)))

    def is_abelian(self) -> bool:
        return all(self.multiply(x, y) == self.multiply(y, x)
                   for x in self.elements for y in self.elements)


def normalized_cocycle(kernel: int, quotient: int, nonzero: Sequence[int]) -> tuple[int, ...]:
    """Interpret (q-1)^2 entries; normalization fills the zero row/column."""
    if not _is_int(kernel) or not _is_int(quotient) or kernel < 2 or quotient < 2:
        raise CouplingError("Invalid extension dimensions")
    if len(nonzero) != (quotient-1)**2 or any(not _is_int(a) or not 0 <= a < kernel for a in nonzero):
        raise CouplingError("Malformed nonzero cocycle cells")
    f = [0] * quotient**2
    t = iter(nonzero)
    for x in range(1, quotient):
        for y in range(1, quotient):
            f[x*quotient+y] = next(t)
    return tuple(f)


def _multipliers(kernel: int, quotient: int) -> tuple[int, ...]:
    if not all(_is_int(v) for v in (kernel, quotient)) or min(kernel, quotient) < 2:
        raise CouplingError("Invalid dimensions")
    return tuple(g for g in range(1, kernel)
                 if gcd(g, kernel) == 1 and pow(g, quotient, kernel) == 1)


def gauge_change(c: CyclicExtension, cochain: tuple[int, ...]) -> CyclicExtension:
    """f -> f + delta(t), with canonical source/quotient-identical isomorphism.

    Phi_t(b,x)=(b-t(x),x) is a homomorphism FROM f TO f+delta(t).
    It does not identify the external labels without a justified calibration.
    """
    k, q = c.kernel, c.quotient
    if type(cochain) is not tuple or len(cochain) != q or cochain[0] != 0 or any(
        not _is_int(v) or not 0 <= v < k for v in cochain
    ):
        raise CouplingError("Normalized cochain with exact residues required")
    f = tuple((c.cocycle[x*q+y] + cochain[x]
               + pow(c.multiplier, x, k)*cochain[y]
               - cochain[(x+y)%q]) % k
              for x in range(q) for y in range(q))
    return CyclicExtension(k, q, c.multiplier, f)


def gauge_map(c: CyclicExtension, cochain: tuple[int, ...], a: Element) -> Element:
    """Explicit isomorphism into gauge_change(c,cochain)."""
    c.check_element(a)
    if type(cochain) is not tuple or len(cochain) != c.quotient or cochain[0] != 0 or any(
        not _is_int(v) or not 0 <= v < c.kernel for v in cochain
    ):
        raise CouplingError("Malformed gauge map")
    return ((a[0]-cochain[a[1]]) % c.kernel, a[1])


def verify_gauge_map(c: CyclicExtension, cochain: tuple[int, ...]) -> bool:
    target = gauge_change(c, cochain)
    return all(gauge_map(c, cochain, c.multiply(x, y)) ==
               target.multiply(gauge_map(c, cochain, x), gauge_map(c, cochain, y))
               for x in c.elements for y in c.elements)


def gauge_key(c: CyclicExtension) -> tuple[int, int, int, tuple[int, ...]]:
    """Canonical REPRESENTATIVE of a framed extension, not group isomorphism."""
    if c.kernel**(c.quotient-1) > 30000:
        raise CouplingError("Gauge orbit exceeds the declared exact enumeration budget")
    forms = (gauge_change(c, (0,)+bits).cocycle
             for bits in product(range(c.kernel), repeat=c.quotient-1))
    return (c.kernel, c.quotient, c.multiplier, min(forms))


def lift_wrap(c: CyclicExtension) -> int:
    """Kernel coordinate of the qth power of the named quotient lift (0,1).

    This is a framed measurement prediction, not gauge-invariant as an integer.
    """
    x = c.identity
    for _ in range(c.quotient):
        x = c.multiply(x, (0,1))
    if x[1] != 0:
        raise AssertionError("Quotient generator did not return to the kernel")
    return x[0]


def cyclic_norm(kernel: int, quotient: int, multiplier: int) -> int:
    """N_g = 1+g+...+g^(q-1) mod k, exactly."""
    if (not all(_is_int(a) for a in (kernel, quotient, multiplier)) or
            not 2 <= kernel <= 12 or not 2 <= quotient <= 12 or
            not 1 <= multiplier < kernel or gcd(multiplier, kernel) != 1 or
            pow(multiplier, quotient, kernel) != 1):
        raise CouplingError("Invalid quotient action for cyclic norm")
    return sum(pow(multiplier,i,kernel) for i in range(quotient)) % kernel


def cohomology_signature(c: CyclicExtension) -> tuple[int,int]:
    """(rho, lift-wrap coset) modulo changes of the quotient generator lift.

    For fixed kernel/quotient identity frame, classical H^2(C_q,C_k)_rho
    equals Fix(rho) / Norm(C_k); the representative is the smallest residue
    of the N_g coset containing the q-fold quotient lift.
    """
    k = c.kernel
    t = lift_wrap(c)
    n = cyclic_norm(k,c.quotient,c.multiplier)
    if (c.multiplier-1)*t % k:
        raise AssertionError("Lift wrap violates action-invariance relation")
    return (c.multiplier, min((t+n*s)%k for s in range(k)))


def theoretical_extension_count(kernel: int, quotient: int, multiplier: int) -> int:
    """Independent cyclic cohomology cardinality: |Fix(g)|/|N_g(C_k)|."""
    n = cyclic_norm(kernel, quotient, multiplier)
    fixed = {t for t in range(kernel) if (multiplier-1)*t % kernel == 0}
    norm_image = {(n*s)%kernel for s in range(kernel)}
    if not norm_image.issubset(fixed) or len(fixed)%len(norm_image):
        raise AssertionError("Cyclic norm incompatible with quotient action")
    return len(fixed)//len(norm_image)


@dataclass(frozen=True)
class Discovery:
    candidates: tuple[CyclicExtension, ...]  # one per normalized gauge orbit
    raw_cocycles: int
    actions: tuple[int, ...]


def discover_couplings(kernel: int, quotient: int, *, max_tables: int = 30000) -> Discovery:
    """Enumerate ALL normalized twisted cocycles, modulo normalized 1-cochains.

    This is complete ONLY within the declared finite cyclic-by-cyclic extension
    grammar and fixed identity action on kernel/quotient labels.  Syntax
    duplicates in a gauge orbit are never treated as independent hypotheses.
    """
    if not all(_is_int(n) for n in (kernel, quotient, max_tables)) or max_tables < 1:
        raise CouplingError("Integer dimensions and positive search cap required")
    if not 2 <= kernel <= 12 or not 2 <= quotient <= 12:
        raise CouplingError("Kernel/quotient outside finite generator scope")
    actions = _multipliers(kernel, quotient)
    table_count = len(actions) * kernel**((quotient-1)**2)
    if table_count > max_tables:
        raise CouplingError("Search grammar exceeds the declared exact enumeration budget")
    representatives: dict[tuple[int, int, int, tuple[int, ...]], CyclicExtension] = {}
    raw = 0
    for g in actions:
        for cells in product(range(kernel), repeat=(quotient-1)**2):
            try:
                c = CyclicExtension(kernel, quotient, g,
                                    normalized_cocycle(kernel, quotient, cells))
            except CouplingError:
                continue
            raw += 1
            key = gauge_key(c)
            representatives[key] = CyclicExtension(*key)
    return Discovery(tuple(representatives[k] for k in sorted(representatives)), raw, actions)


def groups_isomorphic(left: CyclicExtension, right: CyclicExtension) -> bool:
    """Small-group exhaustive homomorphism oracle; NOT a polynomial algorithm.

    Checks all bijections with matching element orders and their multiplication
    tables.  Does not preserve the named kernel/quotient arrows, unlike gauge.
    Restricted to <=9 elements to make completeness an executable assertion.
    """
    n = left.kernel * left.quotient
    if right.kernel * right.quotient != n:
        return False
    if n > 9:
        raise CouplingError("Exact group-isomorphism oracle limited to order <=9")
    if left.order_histogram() != right.order_histogram():
        return False
    sl, sr = left.elements, right.elements
    idx_l, idx_r = {v:i for i,v in enumerate(sl)}, {v:i for i,v in enumerate(sr)}
    tab_l = tuple(tuple(idx_l[left.multiply(x,y)] for y in sl) for x in sl)
    tab_r = tuple(tuple(idx_r[right.multiply(x,y)] for y in sr) for x in sr)
    o_l = tuple(left.element_order(x) for x in sl)
    o_r = tuple(right.element_order(x) for x in sr)
    mapping = {0:0}
    used = {0}

    def consistent() -> bool:
        for i, u in mapping.items():
            for j, v in mapping.items():
                result = tab_l[i][j]
                if result in mapping and mapping[result] != tab_r[u][v]:
                    return False
        return True

    def dfs() -> bool:
        if len(mapping) == n:
            return consistent()
        unused_src = [i for i in range(1,n) if i not in mapping]
        s = min(unused_src, key=lambda i: (sum(1 for j in range(1,n)
                      if j not in used and o_l[i] == o_r[j]), i))
        for t in range(1,n):
            if t not in used and o_l[s] == o_r[t]:
                mapping[s] = t
                used.add(t)
                if consistent() and dfs():
                    return True
                used.remove(t)
                del mapping[s]
        return False
    return dfs()


def abstract_isomorphism_classes(candidates: Sequence[CyclicExtension]) -> tuple[tuple[int, ...], ...]:
    """Partition indices by unrestricted group isomorphism (<=9 states)."""
    remaining = set(range(len(candidates)))
    blocks = []
    while remaining:
        i = min(remaining)
        block = tuple(j for j in sorted(remaining)
                      if groups_isomorphic(candidates[i], candidates[j]))
        blocks.append(block)
        remaining.difference_update(block)
    return tuple(blocks)


@dataclass(frozen=True)
class ObserverContract:
    """Licensed mathematical action alphabet, not an authenticated apparatus."""
    source_id: str
    basis_id: str
    epoch: int
    actions: tuple[Element, ...]
    readout: str  # quotient / kernel / full
    costs: tuple[Fraction, ...] = ()  # empty explicitly means unit action cost

    def __post_init__(self) -> None:
        if not self.source_id or not self.basis_id or not _is_int(self.epoch) or self.epoch < 0:
            raise CouplingError("Source/basis/epoch provenance is mandatory")
        if (type(self.actions) is not tuple or not self.actions or
                any(type(a) is not tuple or len(a) != 2 or not all(_is_int(v) for v in a)
                    for a in self.actions) or len(set(self.actions)) != len(self.actions)):
            raise CouplingError("Declare distinct, actually licensed mathematical action labels")
        if self.readout not in ("quotient", "kernel", "full"):
            raise CouplingError("Unknown / unlicensed observation interface")
        if (type(self.costs) is not tuple or (self.costs and len(self.costs) != len(self.actions))
            or any((type(v) is not int and not isinstance(v, Fraction)) or v <= 0
                   for v in self.costs)):
            raise CouplingError("Declare exact positive per-action cost or explicit unit-cost default")


def _check_contract(candidates: Sequence[CyclicExtension], contract: ObserverContract) -> None:
    if not candidates:
        raise CouplingError("A nonempty finite candidate source class is required")
    k, q = candidates[0].kernel, candidates[0].quotient
    if any(c.kernel != k or c.quotient != q for c in candidates):
        raise CouplingError("Candidates do not share a common typed carrier")
    if len(set(candidates)) != len(candidates):
        raise CouplingError("Repeated syntactic candidate would double-count prior mass")
    if len({gauge_key(c) for c in candidates}) != len(candidates):
        raise CouplingError("Gauge-equivalent candidate duplication would distort model weights")
    for a in contract.actions:
        candidates[0].check_element(a)


def _readout(c: CyclicExtension, state: Element, mode: str):
    if mode == "quotient":
        return state[1]
    if mode == "kernel":
        return state[0]
    return state


@dataclass(frozen=True)
class PolicyLeaf:
    value: str


@dataclass(frozen=True)
class PolicyNode:
    action: Element
    branches: tuple[tuple[object, "Policy"], ...]


Policy = PolicyLeaf | PolicyNode


@dataclass(frozen=True)
class Plan:
    status: str
    depth: int | None
    policy: Policy | None
    horizon: int
    # A bounded failure is never promoted to an all-time impossibility.


def _normalize_targets(candidates: Sequence[CyclicExtension], targets: Sequence[str]):
    if len(targets) != len(candidates) or any(type(t) is not str or not t for t in targets):
        raise CouplingError("Each candidate needs an explicit target label")


def winning_policy(candidates: Sequence[CyclicExtension], contract: ObserverContract,
                   targets: Sequence[str], max_depth: int) -> Plan:
    """Complete finite-horizon AND/OR policy search over PUBLIC outcomes.

    A policy chooses actions based only on previous outcomes.  There are no
    hypothetical resets, no knowledge of which hidden candidate is true, and
    no forgotten branch: all possible output branches must win.
    Iterative deepening returns a minimal worst-case number of actions.
    """
    _check_contract(candidates, contract)
    _normalize_targets(candidates, targets)
    if not _is_int(max_depth) or not 0 <= max_depth <= 64:
        raise CouplingError("Finite nonnegative horizon <=64 required (resource bound)")
    belief = tuple((i, c.identity) for i, c in enumerate(candidates))

    def search(belief, remaining, memo):
        key = (belief, remaining)
        if key in memo:
            return memo[key]
        labels = {targets[i] for i, _ in belief}
        if len(labels) == 1:
            return PolicyLeaf(next(iter(labels)))
        if remaining == 0:
            return None
        for a in contract.actions:
            branches = {}
            for i, current in belief:
                c = candidates[i]
                nxt = c.right_step(current, a)
                report = _readout(c, nxt, contract.readout)
                branches.setdefault(report, []).append((i, nxt))
            children = []
            for outcome, child_belief in sorted(branches.items(), key=lambda kv: repr(kv[0])):
                child = search(tuple(child_belief), remaining-1, memo)
                if child is None:
                    break
                children.append((outcome, child))
            else:
                result = PolicyNode(a, tuple(children))
                memo[key] = result
                return result
        memo[key] = None
        return None

    for depth in range(max_depth + 1):
        policy = search(belief, depth, {})
        if policy is not None:
            return Plan("DECISIVE_IN_DECLARED_MODEL", depth, policy, max_depth)
    return Plan("UNRESOLVED_WITHIN_HORIZON", None, None, max_depth)


def replay_policy(policy: Policy, c: CyclicExtension, contract: ObserverContract) -> tuple[str, tuple]:
    """Independent replay against one model, recording actual simulated actions."""
    state = c.identity
    record = []
    node = policy
    while isinstance(node, PolicyNode):
        c.check_element(node.action)
        if node.action not in contract.actions:
            raise CouplingError("Unlicensed action in alleged proof policy")
        state = c.right_step(state, node.action)
        outcome = _readout(c, state, contract.readout)
        record.append((node.action, outcome))
        choices = dict(node.branches)
        if outcome not in choices:
            raise CouplingError("Winning policy omitted a lawful source outcome")
        node = choices[outcome]
    return node.value, tuple(record)



def gauge_transported_transcripts(c: CyclicExtension, cochain: tuple[int, ...],
                                  contract: ObserverContract,
                                  word: Sequence[Element]) -> tuple[tuple, tuple]:
    """Compare the same experiment UNDER a genuine frame/gauge transport.

    Source state x, action a, and target readout are all transported through
    Phi_t.  For the target presentation q'(Phi_t(x)) := q(x).  The two full
    transcript sequences then agree by the group homomorphism identity.

    Keeping action labels or readout coordinates FIXED instead is a different
    operational experiment and can produce different reports.  Existence of
    this mathematical isomorphism does not authenticate an apparatus map.
    """
    if any(a not in contract.actions for a in word):
        raise CouplingError("Word contains an action absent from the licensed frame")
    target = gauge_change(c, cochain)
    src = c.identity
    dst = target.identity
    left = []
    right = []
    for a in word:
        src = c.right_step(src, a)
        dst = target.right_step(dst, gauge_map(c, cochain, a))
        left.append(_readout(c, src, contract.readout))
        # Phi_t^-1(b,x)=(b+t(x),x); this is a transported target sensor.
        preimage = ((dst[0]+cochain[dst[1]])%c.kernel,dst[1])
        right.append(_readout(c, preimage, contract.readout))
    return tuple(left), tuple(right)


def quotient_darkness_certificate(candidates: Sequence[CyclicExtension],
                                  contract: ObserverContract) -> bool:
    """UNBOUNDED no-go from algebra, not from a finite search horizon.

    Every right multiplication by (b,x) updates the quotient coordinate
    y -> y+x mod q, independent of the action rho or cocycle f.
    Therefore all admitted models have the SAME quotient report on every
    finite action word and every adaptive PUBLIC policy.  This only proves
    inability to distinguish model-dependent labels, not global model falsity.
    """
    _check_contract(candidates, contract)
    return contract.readout == "quotient"


@dataclass(frozen=True)
class EventReceipt:
    source_id: str
    basis_id: str
    epoch: int
    action: Element
    observed: object
    origin: str = "declared_simulation"  # never authenticated by this field


def simulate_trace(c: CyclicExtension, contract: ObserverContract,
                   actions: Sequence[Element]) -> tuple[EventReceipt, ...]:
    """Synthetic source oracle for TESTS; does not make an event physical."""
    state = c.identity
    rows = []
    for j, a in enumerate(actions):
        if a not in contract.actions:
            raise CouplingError("Unavailable synthetic action")
        state = c.right_step(state, a)
        rows.append(EventReceipt(contract.source_id, contract.basis_id,
                                 contract.epoch+j, a,
                                 _readout(c, state, contract.readout)))
    return tuple(rows)


def exact_posterior(candidates: Sequence[CyclicExtension], contract: ObserverContract,
                    prior: Sequence[Fraction], events: Sequence[EventReceipt]) -> tuple[Fraction, ...]:
    """Conditional Bayesian weights over one representative per gauge orbit.

    The supplied events must be independently audited for source authenticity;
    software source/version fields are not such an audit.  For exact deterministic
    laws, each compatible candidate's likelihood is 1 and the others 0.
    """
    _check_contract(candidates, contract)
    if len(prior) != len(candidates) or any(
        (type(v) is not int and not isinstance(v, Fraction)) or v < 0 for v in prior
    ):
        raise CouplingError("One exact nonnegative prior per candidate required")
    weights = tuple(Fraction(v) for v in prior)
    if sum(weights, Fraction(0)) != 1:
        raise CouplingError("Priors must be normalized")
    states = [c.identity for c in candidates]
    for j, event in enumerate(events):
        if (event.source_id != contract.source_id or event.basis_id != contract.basis_id or
                event.epoch != contract.epoch+j or event.action not in contract.actions):
            raise CouplingError("Wrong causal action/source/basis/epoch receipt")
        predictions = []
        for i, c in enumerate(candidates):
            states[i] = c.right_step(states[i], event.action)
            predictions.append(_readout(c, states[i], contract.readout))
        live = [w if predictions[i] == event.observed else Fraction(0)
                for i, w in enumerate(weights)]
        evidence = sum(live, Fraction(0))
        if evidence == 0:
            raise OutOfModel("The observed history has zero probability under every live model")
        weights = tuple(w/evidence for w in live)
    return weights


@dataclass(frozen=True)
class ActionValue:
    action: Element
    target_gini_gain: Fraction
    declared_cost: Fraction
    gain_per_cost: Fraction


def rank_actions_by_target_gain(candidates: Sequence[CyclicExtension],
                                contract: ObserverContract,
                                targets: Sequence[str],
                                prior: Sequence[Fraction],
                                events: Sequence[EventReceipt] = ()) -> tuple[ActionValue, ...]:
    """Exact one-step target-Gini information-gain heuristic, NOT a proof policy.

    Evaluates only declared model-conditioned forward laws.  Correctly
    conditions on the RECEIPTS' causal history, then takes the expectation
    over possible next public outcomes.  Never treats identical repetitions
    as independent source events, and does not grant access to missing probes.
    """
    _check_contract(candidates, contract)
    _normalize_targets(candidates, targets)
    weights = exact_posterior(candidates, contract, prior, events)
    states = [c.identity for c in candidates]
    for ev in events:
        for i,c in enumerate(candidates):
            states[i] = c.right_step(states[i], ev.action)

    def masses(terms):
        grouped = {}
        for label, w in terms:
            grouped[label] = grouped.get(label, Fraction(0)) + w
        return grouped

    def gini(terms):
        group=masses(terms)
        return Fraction(1) - sum((v*v for v in group.values()),Fraction(0))

    base=gini(zip(targets, weights))
    choices=[]
    for j,action in enumerate(contract.actions):
        branches={}
        for i,c in enumerate(candidates):
            new = c.right_step(states[i], action)
            output = _readout(c,new,contract.readout)
            branches.setdefault(output,[]).append((targets[i],weights[i]))
        residual=Fraction(0)
        for pairs in branches.values():
            chance=sum((w for _,w in pairs), Fraction(0))
            if chance:
                residual += chance * gini((label,w/chance) for label,w in pairs)
        gain=base-residual
        cost=Fraction(contract.costs[j]) if contract.costs else Fraction(1)
        choices.append(ActionValue(action,gain,cost,gain/cost))
    return tuple(sorted(choices,key=lambda c:(-c.gain_per_cost,c.action)))


def transcript_signature(candidates: Sequence[CyclicExtension], contract: ObserverContract,
                         word: Sequence[Element]) -> tuple[tuple[object, ...], ...]:
    """Deterministic prediction of all reports; not an executed experiment."""
    _check_contract(candidates, contract)
    result = []
    for c in candidates:
        current = c.identity
        obs = []
        for a in word:
            if a not in contract.actions:
                raise CouplingError("Unlicensed action word")
            current = c.right_step(current, a)
            obs.append(_readout(c, current, contract.readout))
        result.append(tuple(obs))
    return tuple(result)
