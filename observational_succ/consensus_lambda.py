"""Source-indexed consensus of finite SUCC-lambda observers and E action ladders.

Every source is a DECLARED finite candidate, not a physical authenticated state.
An E sphere is an action-budget accessibility ball, not a prime/topological S².
Potential sphere access is not a performed action; relays are not new probes.
Model-target factorization is not completed Weil positivity or RH.

This module composes the source_lambda finite-effect calculus with declared
finite automata and the existing MATRYOSHKA proof-carrying miniature interface.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, product
from typing import Mapping

from .source_lambda import (
    AccessGap, Atlas, BoolT, BudgetGap, Execution, PairT, Passport,
    Report, ReportT, ResidueT, TypeFault, check, execute,
)


class ConsensusError(ValueError):
    """Malformed model, source context, or claimed observation."""


def _label(s: str, where: str) -> str:
    if type(s) is not str or not s or len(s) > 128:
        raise ConsensusError(f"{where} must be a nonempty bounded label")
    return s


def _ground(t: object) -> bool:
    if isinstance(t, PairT):
        return _ground(t.left) and _ground(t.right)
    return isinstance(t, (BoolT, ResidueT, ReportT))


def _wire(value: object) -> object:
    """Finite ground-value signature: typed report semantics, not path identity."""
    if isinstance(value, Report):
        return ("report", value.passport, value.modulus, value.value)
    if type(value) is bool:
        return ("bool", value)
    if type(value) is int:
        return ("int", value)
    if type(value) is str:
        return ("str", value)
    if type(value) is tuple:
        return ("pair", tuple(_wire(v) for v in value))
    raise ConsensusError("non-ground output cannot be an observer consensus report")


@dataclass(frozen=True)
class Candidate:
    name: str
    integer: int
    target: str

    def __post_init__(self):
        _label(self.name, "candidate")
        if type(self.integer) is not int:
            raise ConsensusError("candidate arithmetic label requires exact integer")
        _label(self.target, "original source target")


@dataclass(frozen=True)
class World:
    passport: Passport
    candidates: tuple[Candidate, ...]

    def __post_init__(self):
        if not isinstance(self.passport, Passport) or type(self.candidates) is not tuple:
            raise ConsensusError("world needs an explicit passport and candidate tuple")
        if not 1 <= len(self.candidates) <= 32 or any(
                not isinstance(c, Candidate) for c in self.candidates):
            raise ConsensusError("finite nonempty candidate universe required (at most 32)")
        names = [c.name for c in self.candidates]
        if len(set(names)) != len(names):
            raise ConsensusError("candidate identities must be distinct")
        # Equal integer labels are *allowed*: the target can depend on hidden
        # source state not observable by modular lambda expressions.


@dataclass(frozen=True)
class LambdaPort:
    name: str
    term: object

    def validate(self, passport: Passport):
        _label(self.name, "lambda port")
        j = check(self.term, passport)
        if not _ground(j.type):
            raise TypeFault("consensus port cannot return an unexecuted closure")
        return j

    def predict(self, candidate: Candidate, passport: Passport):
        j = self.validate(passport)
        atlas = Atlas.from_integer(passport, candidate.integer, tuple(sorted(j.may_read)))
        return _wire(execute(self.term, atlas).value)


@dataclass(frozen=True)
class MiniPort:
    """Port realized by an authenticated-*in-model* MATRYOSHKA factor.

    The public parent report and its declared translation are all this port
    exposes. Hidden decoder states cannot themselves be counted as readings.
    Physical implementation, calibration and cross-device joint feasibility
    remain independent gates.
    """
    name: str
    parent: object
    mini: object
    decoder: Mapping[str, str]
    macros: Mapping[str, tuple[str, ...]]
    public_map: Mapping[str, str]

    def validate(self, passport: Passport):
        _label(self.name, "miniature port")
        from .miniature_carrier import Carrier, Mini, compile_factor
        if not isinstance(self.parent, Carrier) or not isinstance(self.mini, Mini):
            raise ConsensusError("miniature port requires the real MATRYOSHKA contracts")
        if self.parent.source_id != passport.source_id or self.mini.source_id != passport.source_id:
            raise ConsensusError("miniature source namespace conflicts with lambda passport")
        receipt = compile_factor(self.parent, self.mini, self.decoder,
                                 self.macros, public_map=self.public_map)
        if not receipt["certified"]:
            raise ConsensusError(f"parent-to-mini action/report square failed: {receipt['reason']}")
        return receipt

    def predict(self, candidate: Candidate, passport: Passport):
        self.validate(passport)
        if candidate.name not in self.parent.states:
            raise ConsensusError("candidate missing from miniature parent carrier")
        return _wire(self.public_map[self.parent.reports[candidate.name]])


def certify_dual_ports(left: MiniPort, right: MiniPort, passport: Passport,
                       left_word: tuple[str, ...], right_word: tuple[str, ...],
                       public_pair: Mapping[str, tuple[str, str]]) -> dict:
    """Reuses the MATRYOSHKA source-joint and noninterference gates."""
    from .miniature_carrier import compile_dual_product
    left.validate(passport)
    right.validate(passport)
    if left.parent != right.parent:
        raise ConsensusError("a common parent is required for a joint miniature certificate")
    receipt = compile_dual_product(left.parent, left.mini, right.mini,
                left.decoder, right.decoder, left_word, right_word, public_pair)
    return {"certified_joint_model": bool(receipt["certified"]),
            "status": receipt["kind"] if receipt["certified"] else receipt["reason"],
            "original_source_authenticated": False,
            "two_physical_sensors_proved": False}


Port = LambdaPort | MiniPort


@dataclass(frozen=True)
class ESphere:
    radius: int
    state_paths: tuple[tuple[str, tuple[str, ...]], ...]
    available: tuple[tuple[str, tuple[str, ...]], ...]
    possible_only: bool = True


@dataclass(frozen=True)
class EDevice:
    name: str
    passport: Passport
    states: tuple[str, ...]
    initial: str
    ports: tuple[Port, ...]
    enabled: Mapping[str, tuple[str, ...]]
    moves: Mapping[tuple[str, str], str]
    non_destructive_source: bool = True

    def __post_init__(self):
        _label(self.name, "E identity")
        if not isinstance(self.passport, Passport):
            raise ConsensusError("E must have an explicit common-source passport")
        if not self.non_destructive_source:
            raise ConsensusError("destructive source operations need original/current belief transport")
        if (type(self.states) is not tuple or not self.states or
                any(type(s) is not str or not s for s in self.states) or
                len(set(self.states)) != len(self.states) or self.initial not in self.states):
            raise ConsensusError("finite E action-state carrier and prepared initial state required")
        if type(self.ports) is not tuple or not self.ports:
            raise ConsensusError("E must declare one or more typed observation ports")
        names = [p.name for p in self.ports]
        if len(set(names)) != len(names):
            raise ConsensusError("ambiguous same-name E observation ports")
        if set(self.enabled) != set(self.states):
            raise ConsensusError("complete finite E state visibility atlas required")
        for state in self.states:
            allowed = self.enabled[state]
            if type(allowed) is not tuple or len(set(allowed)) != len(allowed) or any(
                    p not in names for p in allowed):
                raise ConsensusError("invalid finite E port menu")
        for (state,action),dest in self.moves.items():
            if state not in self.states or dest not in self.states:
                raise ConsensusError("E transition outside declared action carrier")
            _label(action,"E transition")
        for p in self.ports:
            p.validate(self.passport)

    def port(self, name: str) -> Port:
        for p in self.ports:
            if p.name == name:
                return p
        raise AccessGap("no such declared E port")

    def state_after(self, path: tuple[str, ...]) -> str:
        if type(path) is not tuple:
            raise ConsensusError("E path must be immutable action word")
        state = self.initial
        for action in path:
            dest = self.moves.get((state,action))
            if dest is None:
                raise AccessGap(f"no lawful E transition from {state} via {action}")
            state=dest
        return state

    def sphere(self, radius: int) -> ESphere:
        """Minimal-cost reachable E states and ports at action length <= radius.

        Exact finite BFS; counts counterfactual accessible programs, NOT events.
        """
        if type(radius) is not int or not 0 <= radius <= 1000:
            raise ConsensusError("finite nonnegative integer accessibility radius required")
        q=deque(((self.initial,()),))
        states={self.initial:()}
        while q:
            state,path=q.popleft()
            if len(path)>=radius:
                continue
            for (old,action),new in sorted(self.moves.items()):
                if old==state and new not in states:
                    nextpath=path+(action,)
                    states[new]=nextpath
                    q.append((new,nextpath))
        available={}
        for state,path in sorted(states.items(),key=lambda t:(len(t[1]),t[1],t[0])):
            for name in self.enabled[state]:
                available.setdefault(name,path)
        return ESphere(radius,tuple(sorted(states.items())),tuple(sorted(available.items())))


@dataclass(frozen=True)
class EFrame:
    device: EDevice
    path: tuple[str, ...] = ()

    def __post_init__(self):
        if not isinstance(self.device, EDevice):
            raise ConsensusError("E frame must carry a typed miniature/observer device")
        self.device.state_after(self.path)

    @property
    def state(self) -> str:
        return self.device.state_after(self.path)

    def succ(self, action: str) -> "EFrame":
        return EFrame(self.device,self.path+(_label(action,"E action"),))

    def record(self, port_name: str, *, atlas: Atlas | None = None,
               parent_public_report: str | None = None) -> "EObservation":
        if port_name not in self.device.enabled[self.state]:
            raise AccessGap("port not enabled at E's actualized finite ladder position")
        port=self.device.port(port_name)
        if isinstance(port,LambdaPort):
            if parent_public_report is not None or not isinstance(atlas,Atlas):
                raise ConsensusError("lambda probe requires recorded atlas, not a guessed readout")
            if atlas.passport != self.device.passport:
                raise ConsensusError("lambda observation source/epoch/basis mismatch")
            run=execute(port.term,atlas)
            return EObservation(self,port_name,_wire(run.value),atlas,None,
                      tuple(f"replay:recorded:{n}" for n in run.observed))
        if isinstance(port,MiniPort):
            if atlas is not None or parent_public_report is None:
                raise ConsensusError("miniature requires a declared parent public outcome")
            if parent_public_report not in port.public_map:
                raise AccessGap("public parent report does not license the miniature report")
            return EObservation(self,port_name,_wire(port.public_map[parent_public_report]),
                None,parent_public_report,("replay:declared_parent_public_report",
                   "derived:certified_miniature_public_map"))
        raise ConsensusError("unknown port kind")


@dataclass(frozen=True)
class EObservation:
    frame: EFrame
    port_name: str
    output: object
    atlas: Atlas | None
    parent_public_report: str | None
    lineage: tuple[str, ...]

    @property
    def origin(self):
        return self.frame.device.name


@dataclass(frozen=True)
class ERelay:
    evidence: EObservation
    receiver: str

    def __post_init__(self):
        if not isinstance(self.evidence,EObservation):
            raise ConsensusError("relay must carry original observation and provenance")
        _label(self.receiver,"testimony recipient")

    @property
    def origin(self):
        return self.evidence.origin


@dataclass(frozen=True)
class Consensus:
    status: str
    compatible: tuple[str, ...]
    possible_targets: tuple[str, ...]
    report_origins: tuple[str, ...]
    minimal_inconsistent_indices: tuple[int, ...] | None
    model_only: bool = True
    physically_authenticated: bool = False
    establishes_global_truth: bool = False
    RH_proved: bool = False


def _verified(evidence: EObservation | ERelay, passport: Passport) -> EObservation:
    r=evidence.evidence if isinstance(evidence,ERelay) else evidence
    if not isinstance(r,EObservation):
        raise ConsensusError("evidence must be a recorded replay or provenance-preserving relay")
    if r.frame.device.passport != passport:
        raise ConsensusError("source identity/epoch/basis mismatch between E reports")
    replay=r.frame.record(r.port_name,atlas=r.atlas,
                        parent_public_report=r.parent_public_report)
    if replay != r:
        raise ConsensusError("source report, lineage or action path was forged")
    return r


def _predict(port: Port, world: World, candidate: Candidate):
    return port.predict(candidate,world.passport)


def _survivors(world: World, events: tuple[EObservation, ...]) -> tuple[str,...]:
    return tuple(c.name for c in world.candidates if all(
        _predict(e.frame.device.port(e.port_name),world,c)==e.output for e in events))


def consensus(world: World, evidence: tuple[EObservation | ERelay, ...]) -> Consensus:
    """Original-source model fiber intersection; no self-certified actual world."""
    if type(evidence) is not tuple or len(evidence)>18:
        raise ConsensusError("finite recorded event tuple required, <=18")
    if not isinstance(world,World):
        raise ConsensusError("declared source world required")
    events=tuple(_verified(e,world.passport) for e in evidence)
    # Same E identity must preserve one actual prefix-comparable action history.
    # Two incompatible branches of a potential sphere are NOT a joint execution.
    for i,first in enumerate(events):
        for second in events[:i]:
            if first.origin != second.origin:
                continue
            if first.frame.device != second.frame.device:
                raise ConsensusError("one E identity cannot carry two conflicting automata")
            a,b=first.frame.path,second.frame.path
            if not (a[:len(b)]==b or b[:len(a)]==a):
                raise ConsensusError("incompatible E action branches cannot be jointly actualized")
    # Two distinct observer tapes claiming incompatible residues for the same
    # source cannot be silently 'repaired' by inventing a new source state.
    survivors=_survivors(world,events)
    targets=tuple(sorted(set(c.target for c in world.candidates if c.name in survivors)))
    core=None
    if not survivors:
        for k in range(1,len(events)+1):
            for indices in combinations(range(len(events)),k):
                if not _survivors(world,tuple(events[i] for i in indices)):
                    core=indices
                    break
            if core is not None:
                break
        status="NO_GLOBAL_SOURCE_IN_DECLARED_MODEL"
    elif len(survivors)==1:
        status="SOURCE_IDENTIFIED_IN_DECLARED_MODEL"
    elif len(targets)==1:
        status="TARGET_CERTIFIED_IN_DECLARED_MODEL"
    else:
        status="TARGET_UNRESOLVED"
    return Consensus(status,survivors,targets,tuple(e.origin for e in events),core)


@dataclass(frozen=True)
class Portfolio:
    status: str
    selected: tuple[tuple[str,str], ...]
    observed_cross_target_pairs: int
    total_cross_target_pairs: int
    uncovered_pairs: tuple[tuple[str,str], ...]
    activation_paths: tuple[tuple[str,str,tuple[str,...]], ...]
    model_only: bool=True
    executed: bool=False


def _candidate_pairs(world: World):
    return tuple((a,b) for a,b in combinations(world.candidates,2)
                 if a.target!=b.target)


def _accessible(devices: tuple[EDevice,...],radius:int):
    if type(devices) is not tuple or any(not isinstance(d,EDevice) for d in devices):
        raise ConsensusError("finite observer device tuple required")
    if len({d.name for d in devices})!=len(devices):
        raise ConsensusError("observer identity collision (votes cannot multiply a source)")
    out=[]
    for d in devices:
        for name,path in d.sphere(radius).available:
            out.append((d,name,path))
    return tuple(out)


def exact_portfolio(world: World, devices: tuple[EDevice,...], *,
                    radius:int, max_programs:int=15,
                    max_joint_states:int=512) -> Portfolio:
    """Exact finite source-target separation by JOINTLY admissible E menus.

    One reachable terminal operational state is selected for each E. All
    selected ports of a given E must be enabled at that SAME state. A union
    of mutually exclusive action-sphere branches is not lawful consensus.
    This one-terminal-state rule is conservative: genuine sequential schedules
    could reveal more, but require explicit original/current state transport.
    """
    if not isinstance(world, World):
        raise ConsensusError("declared finite model required")
    if type(max_programs) is not int or not 0<=max_programs<=20:
        raise ConsensusError("finite portfolio enumeration limit required")
    if type(max_joint_states) is not int or not 1<=max_joint_states<=100000:
        raise ConsensusError("finite joint configuration budget required")
    # Check the complete declared E network even if radius=0 reaches no ports.
    if type(devices) is not tuple or any(not isinstance(d,EDevice) for d in devices):
        raise ConsensusError("typed E device tuple required")
    if len({d.name for d in devices})!=len(devices):
        raise ConsensusError("E identity collision")
    if any(d.passport!=world.passport for d in devices):
        raise ConsensusError("different E source/epoch/basis cannot be pooled")
    pairs=_candidate_pairs(world)
    pair_ids=tuple((a.name,b.name) for a,b in pairs)
    complete=frozenset(range(len(pairs)))
    sphere_states=tuple(d.sphere(radius).state_paths for d in devices)
    count=1
    for s in sphere_states:
        count*=len(s)
    if count>max_joint_states:
        return Portfolio("RESOURCE_BUDGET_GAP",(),0,len(pairs),pair_ids,())
    # Cache source-semantic distinctions by program identity, not by votes.
    cover_cache={}
    def covered(d,name):
        key=(d.name,name)
        if key not in cover_cache:
            port=d.port(name)
            cover_cache[key]=frozenset(i for i,(a,b) in enumerate(pairs) if
                      _predict(port,world,a)!=_predict(port,world,b))
        return cover_cache[key]

    best=None
    total_available=frozenset()
    for selection in product(*sphere_states):
        options=[]
        for d,(state,path) in zip(devices,selection):
            for name in d.enabled[state]:
                options.append((d,name,path,covered(d,name)))
        total_available=total_available.union(*(o[3] for o in options))
        if len(options)>max_programs:
            return Portfolio("RESOURCE_BUDGET_GAP",(),len(total_available),
                            len(pairs),tuple(pair_ids[i] for i in complete-total_available),())
        # Only examine combinations capable of beating current best.
        end_size=len(options) if best is None else min(len(options),len(best)-1)
        for k in range(end_size+1):
            winner=None
            for indices in combinations(range(len(options)),k):
                union=frozenset().union(*(options[i][3] for i in indices))
                if union==complete:
                    winner=tuple(options[i] for i in indices)
                    break
            if winner is not None:
                best=winner
                break
    if best is not None:
        chosen=tuple((d.name,name) for d,name,_,_ in best)
        paths=tuple((d.name,name,path) for d,name,path,_ in best)
        return Portfolio("MODEL_TARGET_SEPARATING_PORTFOLIO",chosen,
                        len(pairs),len(pairs),(),paths)
    missing=tuple(pair_ids[i] for i in complete-total_available)
    return Portfolio("DARK_WITH_THIS_ACCESSIBLE_PORT_FAMILY" if missing else
                     "UNJOINTLY_REALIZABLE_PORT_FAMILY",(),len(total_available),
                     len(pairs),missing,())


@dataclass(frozen=True)
class ForcingDepth:
    status:str
    radius:int|None
    portfolio:Portfolio
    searched_through:int
    model_only:bool=True
    RH_proved:bool=False


def forcing_depth(world:World, devices:tuple[EDevice,...], *,
                  max_radius:int=5, max_programs:int=15)->ForcingDepth:
    """Finite inverse-Ramsey-style upper/lower access-depth certificate."""
    if type(max_radius) is not int or not 0<=max_radius<=1000:
        raise ConsensusError("finite radius budget required")
    result=None
    for r in range(max_radius+1):
        result=exact_portfolio(world,devices,radius=r,max_programs=max_programs)
        if result.status=="MODEL_TARGET_SEPARATING_PORTFOLIO":
            return ForcingDepth("FINITE_FORCING_DEPTH_CERTIFIED",r,result,r)
        if result.status=="RESOURCE_BUDGET_GAP":
            return ForcingDepth("RESOURCE_BUDGET_GAP",None,result,r)
    # A shortest path to any reachable finite automaton state uses at most
    # |Q|-1 edges. If reached, the finite action closure is exhausted.
    complete=all(max_radius>=len(d.states)-1 for d in devices)
    if complete:
        if result.status == "DARK_WITH_THIS_ACCESSIBLE_PORT_FAMILY":
            status="DARK_UNDER_DECLARED_PORT_FAMILY"
        else:
            # An actually executed sequential path can sometimes accumulate
            # non-destructive reports across multiple states. That is a
            # DIFFERENT protocol and has not been optimized or refuted here.
            status="ONE_STATE_PROTOCOL_SATURATED"
    else:
        status="DEPTH_BUDGET_GAP"
    return ForcingDepth(status,None,result,max_radius)


def horned_sphere_consensus_control(depth:int, nilpotent_classes:tuple[int,...])->dict:
    """An existing WILD-SUCC counterexample to same-kind observer consensus.

    The stage-k finite nilpotent witness does not define a representation of
    the perfect direct-limit exterior group (indeed no nontrivial solvable image
    does); it calibrates stage sensitivity only.
    """
    from .wild_embedding_succ import nilpotent_visibility,meridian_report,unitriangular_meridian
    if type(nilpotent_classes) is not tuple or not nilpotent_classes:
        raise ConsensusError("nonempty tuple of finite nilpotent observer classes required")
    stage=meridian_report(depth)
    classes=tuple(nilpotent_visibility(depth,j) for j in nilpotent_classes)
    all_blind=all(c["nilpotent_probe_cannot_detect"] for c in classes)
    detector=unitriangular_meridian(depth) if depth<=4 else None
    return {"depth":depth,"iterated_word_length":stage["free_word_length"],
       "lower_central_depth":stage["lower_central_depth"],
       "all_observers_blind":all_blind,
       "stage_detector":detector,
       "no_global_nilpotent_representation_from_stage_detector":True,
       "consensus_is_not_source_authentication":True,"RH_proved":False}


def minimum_consensus_channel(world:World,
            sender:EDevice, sender_port:str,
            receiver:EDevice,receiver_port:str,*,radius:int=0)->dict:
    """Target-specific zero-error testimony with receiver-side information.

    The exact chromatic code is delegated to existing interobserver_channels;
    source-effect predictions are generated by SUCC-lambda and/or MATRYOSHKA.
    Distinct E names do NOT prove independent physical sensors.
    """
    from .interobserver_channels import InterobserverWorld, exact_minimum_channel
    if sender.name==receiver.name or sender.passport!=world.passport or receiver.passport!=world.passport:
        raise ConsensusError("distinct source-coherent observers required for receiver-side code")
    for device,name in ((sender,sender_port),(receiver,receiver_port)):
        if name not in dict(device.sphere(radius).available):
            raise AccessGap("receiver/sender program outside its declared finite access sphere")
    if len(world.candidates)>24:
        raise ConsensusError("finite exact channel solver accepts <=24 source candidates")
    # repr is injective on our typed exact ground-output algebra in this
    # admitted grammar. Same source/probe cannot gain an extra degree by naming.
    u=tuple(repr(_predict(sender.port(sender_port),world,c)) for c in world.candidates)
    v=tuple(repr(_predict(receiver.port(receiver_port),world,c)) for c in world.candidates)
    model=InterobserverWorld(tuple(c.name for c in world.candidates),u,v,
                             tuple(c.target for c in world.candidates))
    from .interobserver_channels import ZeroErrorChannelError
    try:
        code=exact_minimum_channel(model)
    except ZeroErrorChannelError as exc:
        raise AccessGap("declared joint views cannot decode target: " + str(exc)) from exc
    return {"status":"MODEL_OPTIMAL_ZERO_ERROR_CONSENSUS_MESSAGE",
        "minimum_codewords":code.codewords,
        "minimum_fixed_width_bits":code.fixed_width_bits,
        "naive_sender_view_bits":(len(code.sender_alphabet)-1).bit_length(),
        "sender_alphabet_size":len(code.sender_alphabet),
        "decoder_correct_for_all_declared_sources":all(
               code.decode(code.encode(a),b)==c.target for a,b,c in
               zip(u,v,world.candidates)),
        "source_coherent":True,"original_source_authenticated":False,
        "recipient_performed_senders_probe":False,
        "no_RH_sign_authority":True}


def two_chart_cross_energy(a, b, c) -> dict:
    """Cross-observer signed Gram control, exact model arithmetic only.

    Each individual chart reports positive diagonal energy, but omitted mixed
    coupling may make the joint form negative. A target sign cannot be
    certified from chart-local positivity votes. Not the Suzuki source.
    """
    from fractions import Fraction as Q
    from .source_lambda import signed_witness
    if any(type(x) not in (int,Q) for x in (a,b,c)):
        raise ConsensusError("exact integer/rational chart coefficients required")
    a,b,c=Q(a),Q(b),Q(c)
    if a<=0 or b<=0:
        raise ConsensusError("strictly positive individual chart energies required")
    matrix=((a,c),(c,b))
    # Negative Schur => exact explicit witness v=(c,-a).
    vector=(c,-a)
    checked=signed_witness(matrix,vector)
    determinant=a*b-c*c
    if (checked.energy<0)!=(determinant<0):
        raise AssertionError("exact 2x2 Schur sign identity failed")
    return {"both_individual_charts_positive":True,
            "whole_joint_operator_positive_semidefinite":determinant>=0,
            "mixed_determinant":determinant,
            "explicit_negative_witness":vector if determinant<0 else None,
            "witness_energy":checked.energy,
            "requires_cross_chart_measurement":True,
            "source_is_Suzuki":False,"RH_proved":False}
