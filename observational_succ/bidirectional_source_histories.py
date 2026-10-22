"""Source-certified finite stochastic histories and affine SUCC/FUCC clock transports.

All probabilities are exact Fractions. Paths preserve *source-labelled events*,
not merely source/target states. Multiplicative SUCC/FUCC clock actions are
chosen observation-time charts on one source Markov chain: they are NOT a
physical derivation of prime multiplication from lightning or dielectric media.

The bicausal quotient uses Bayes reverse for one strictly positive declared
source law, not a universal inverse or the Hilbert adjoint V_p^*.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, isqrt


class HistoryTransportError(ValueError):
    """Malformed source, event labels, clock, probability, or observer probe."""


def exact(value):
    if type(value) not in (int, Q):
        raise HistoryTransportError("only exact int/Fraction probabilities")
    return Q(value)


def positive_integer(value, minimum=1):
    if type(value) is not int or value < minimum:
        raise HistoryTransportError("invalid exact positive integer clock")
    return value


def genuine_prime(value):
    return (type(value) is int and value >= 2 and
            all(value % d for d in range(2, isqrt(value)+1)))


@dataclass(frozen=True)
class SourcePath:
    """Contiguous source record, including parallel event labels and all states."""
    start_clock: int
    states: tuple
    labels: tuple[str, ...]

    def __post_init__(self):
        positive_integer(self.start_clock)
        if (type(self.states) is not tuple or not self.states or
                type(self.labels) is not tuple or
                len(self.labels) != len(self.states)-1 or
                any(type(x) is not str or not x for x in self.labels)):
            raise HistoryTransportError("path requires source states and one event label per transition")
        try:
            hash(self.states)
        except TypeError as exc:
            raise HistoryTransportError("source states must be hashable") from exc

    @property
    def end_clock(self):
        return self.start_clock+len(self.labels)

    def extend(self, label, target):
        return SourcePath(self.start_clock,self.states+(target,),self.labels+(label,))

    def prefix(self, clock):
        positive_integer(clock)
        if not self.start_clock <= clock <= self.end_clock:
            raise HistoryTransportError("partial path reversal outside recorded history")
        count=clock-self.start_clock
        return SourcePath(self.start_clock,self.states[:count+1],self.labels[:count])


def affine_backward(path, a, b):
    """Partial archival predecessor of n -> a*n+b, never physical state undo.

    The partial source inverse exists only when endpoint belongs to the exact
    arithmetic image and source clock is inside the *recorded* history.
    """
    positive_integer(a)
    positive_integer(b,0)
    m=path.end_clock
    if m<=b or (m-b)%a:
        return None
    n=(m-b)//a
    if n<path.start_clock:
        return None
    return path.prefix(n)


@dataclass(frozen=True)
class LabelledMarkovSource:
    """Finite 1-based clock with stochastic, explicit original event channels.

    transitions[t][x] contains tuples (label, target_state, exact_probability)
    from clock t+1 to clock t+2. Distinct labels may reach the same target.
    Every source row must have total mass 1; zero-mass source channels are
    omitted, never silently treated as independently witnessed events.
    """
    levels: tuple[tuple, ...]
    transitions: tuple[dict, ...]

    def __post_init__(self):
        if (type(self.levels) is not tuple or not self.levels or
                type(self.transitions) is not tuple or
                len(self.transitions)!=len(self.levels)-1):
            raise HistoryTransportError("finite nonempty levels and adjacent kernels required")
        for level in self.levels:
            if type(level) is not tuple or not level:
                raise HistoryTransportError("each clock level must be nonempty")
            try:
                if len(level)!=len(set(level)):
                    raise HistoryTransportError("duplicate source states in one clock level")
            except TypeError as exc:
                raise HistoryTransportError("unhashable source state") from exc
        for t, rows in enumerate(self.transitions):
            if type(rows) is not dict or set(rows)!=set(self.levels[t]):
                raise HistoryTransportError("every source state requires one normalized event row")
            for source, entries in rows.items():
                if type(entries) is not tuple or not entries:
                    raise HistoryTransportError("each row needs labelled channels")
                pair_ids=set()
                norm=Q()
                for entry in entries:
                    if type(entry) is not tuple or len(entry)!=3:
                        raise HistoryTransportError("event must be (label,target,probability)")
                    label,target,p=entry
                    if (type(label) is not str or not label or
                            target not in self.levels[t+1]):
                        raise HistoryTransportError("source channel or target not authorized")
                    key=(label,target)
                    if key in pair_ids:
                        raise HistoryTransportError("duplicate indistinguishable labelled event")
                    pair_ids.add(key)
                    if exact(p)<=0:
                        raise HistoryTransportError("only strictly positive present events")
                    norm+=exact(p)
                if norm!=1:
                    raise HistoryTransportError("stochastic row must sum to exactly one")

    @property
    def horizon(self):
        return len(self.levels)

    def aggregate_kernel(self,t):
        """Forget event labels, preserving total state-to-state probabilities."""
        if type(t) is not int or not 0<=t<len(self.transitions):
            raise HistoryTransportError("kernel index out of range")
        result={}
        for x, entries in self.transitions[t].items():
            row={y:Q() for y in self.levels[t+1]}
            for label,y,p in entries:
                row[y]+=exact(p)
            result[x]=row
        return result

    def extend(self,distribution,at_clock,to_clock):
        """Extend ALL labelled histories through a specified temporal interval."""
        positive_integer(at_clock)
        positive_integer(to_clock)
        if not at_clock<=to_clock<=self.horizon or type(distribution) is not dict or not distribution:
            raise HistoryTransportError("invalid path distribution or time interval")
        current={}
        for path,weight in distribution.items():
            if (not isinstance(path,SourcePath) or path.end_clock!=at_clock or
                    path.states[-1] not in self.levels[at_clock-1] or exact(weight)<0):
                raise HistoryTransportError("stale path, negative weight, or mismatched clock")
            current[path]=current.get(path,Q())+exact(weight)
        for t in range(at_clock-1,to_clock-1):
            out={}
            for path,weight in current.items():
                if not weight:
                    continue
                for label,target,prob in self.transitions[t][path.states[-1]]:
                    grown=path.extend(label,target)
                    out[grown]=out.get(grown,Q())+weight*exact(prob)
            current=out
        return current

    def segment(self,start_clock,end_clock,source):
        positive_integer(start_clock)
        if (type(end_clock) is not int or start_clock>end_clock or
                end_clock>self.horizon or source not in self.levels[start_clock-1]):
            raise HistoryTransportError("unsupported source clock or state")
        start=SourcePath(start_clock,(source,),())
        return self.extend({start:Q(1)},start_clock,end_clock)

    def route(self,source,schedule):
        """Compose macro and SUCC cuts, retaining every step between cuts."""
        if (type(schedule) is not tuple or not schedule or
                any(type(i) is not int for i in schedule) or
                not 1<=schedule[0]<=schedule[-1]<=self.horizon or
                any(a>=b for a,b in zip(schedule,schedule[1:]))):
            raise HistoryTransportError("clock itinerary must be strictly increasing")
        if source not in self.levels[schedule[0]-1]:
            raise HistoryTransportError("unattested source state")
        dist={SourcePath(schedule[0],(source,),()):Q(1)}
        for a,b in zip(schedule,schedule[1:]):
            dist=self.extend(dist,a,b)
        return dist

    def affine_braid(self,n,p,source):
        """Genuine-prime Vp*S=S^p*Vp on full labelled stochastic paths.

        The multiplication is a CLOCK jump, not an intrinsic prime physical
        action. Equality is equality of measures on ordered source histories,
        not just their endpoint marginal or independently sampled outcomes.
        """
        positive_integer(n)
        if not genuine_prime(p):
            raise HistoryTransportError("only genuine primes in FUCC clock")
        end=p*(n+1)
        if end>self.horizon:
            raise HistoryTransportError("full braid exits observed horizon")
        left=(n,n+1,end)
        right=(n,p*n)+tuple(range(p*n+1,end+1))
        return {"S_then_Vp_schedule":left,"Vp_then_Sp_schedule":right,
                "S_then_Vp_paths":self.route(source,left),
                "Vp_then_Sp_paths":self.route(source,right)}

    def posterior_paths(self,start_clock,end_clock,prior,terminal):
        """Actual Bayes mixture over complete labelled histories at a terminal state."""
        positive_integer(start_clock)
        positive_integer(end_clock)
        if not start_clock<=end_clock<=self.horizon:
            raise HistoryTransportError("posterior requires chronological supported clocks")
        if (type(prior) is not dict or set(prior)!=set(self.levels[start_clock-1]) or
                terminal not in self.levels[end_clock-1]):
            raise HistoryTransportError("wrong source prior or endpoint")
        if (any(exact(v)<0 for v in prior.values()) or
                sum((exact(v) for v in prior.values()),Q())!=1):
            raise HistoryTransportError("prior must be a probability on source states")
        masses={}
        for x,weight in prior.items():
            for path,p in self.segment(start_clock,end_clock,x).items():
                if path.states[-1]==terminal:
                    masses[path]=masses.get(path,Q())+exact(weight)*p
        evidence=sum(masses.values(),Q())
        if not evidence:
            raise HistoryTransportError("terminal observation has zero source probability")
        return {path:m/evidence for path,m in masses.items() if m}

    def marginals(self,prior):
        if type(prior) is not dict or set(prior)!=set(self.levels[0]):
            raise HistoryTransportError("initial probability missing source states")
        first={x:exact(w) for x,w in prior.items()}
        if any(w<0 for w in first.values()) or sum(first.values(),Q())!=1:
            raise HistoryTransportError("incorrect initial law")
        levels=[first]
        for t in range(self.horizon-1):
            nxt={y:Q() for y in self.levels[t+1]}
            for x,weight in levels[-1].items():
                for _,y,p in self.transitions[t][x]:
                    nxt[y]+=weight*exact(p)
            levels.append(nxt)
        return tuple(levels)

    def backwards_events(self,prior):
        """Source-labelled Bayes cotransition, including parallel channels.

        For a supported y at clock t+1, the exact reverse mass for
        (x,label)->y is alpha_t(x)*K_t(x,label,y)/alpha_{t+1}(y).
        This is source-dependent Bayesian reversal, not V_p^* or the physical
        time inverse of a dissipative event.
        """
        alpha=self.marginals(prior)
        reverse=[]
        for t,rows in enumerate(self.transitions):
            new={}
            for y in self.levels[t+1]:
                if not alpha[t+1][y]:
                    continue
                predecessors=[]
                for x in self.levels[t]:
                    for label,z,q in rows[x]:
                        if y==z and alpha[t][x]*exact(q):
                            predecessors.append((x,label,alpha[t][x]*exact(q)/alpha[t+1][y]))
                if sum((r for _,_,r in predecessors),Q())!=1:
                    raise ArithmeticError("source conditional reversal failed to normalize")
                new[y]=tuple(predecessors)
            reverse.append(new)
        return tuple(reverse)

    def pathwise_balance(self,path,prior):
        """Forward-labelled path mass equals reverse-labelled path mass.

        alpha_1(x1)*prod K_i(x_i,label_i,x_{i+1})
        =alpha_T(x_T)*prod R_{i+1}(x_{i+1},(x_i,label_i)).
        The full source labels are essential when parallel edges coexist.
        """
        if not isinstance(path,SourcePath) or path.start_clock!=1 or path.end_clock>self.horizon:
            raise HistoryTransportError("a full source-originating path is required")
        alpha=self.marginals(prior)
        reversals=self.backwards_events(prior)
        forward=alpha[0][path.states[0]]
        backward=alpha[path.end_clock-1][path.states[-1]]
        for t,label in enumerate(path.labels):
            x,y=path.states[t:t+2]
            candidates=[exact(q) for name,target,q in self.transitions[t][x]
                        if name==label and target==y]
            if len(candidates)!=1:
                raise HistoryTransportError("path event not attested by source transition")
            forward*=candidates[0]
            r=[q for old,name,q in reversals[t].get(y,()) if old==x and name==label]
            if not r:
                if forward==0:
                    return {"forward":Q(),"reverse":Q(),"equal":True}
                raise ArithmeticError("no reverse mass for supported history")
            backward*=r[0]
        return {"forward":forward,"reverse":backward,"equal":forward==backward}

    def path_isometry_gram(self,start_clock,end_clock):
        """Exact Gram for formal sqrt(path probability) labelled-history isometry.

        Distinct input states have disjoint FULL records. For a fixed input,
        the diagonal Gram entry is sum of all its outgoing path probabilities.
        This checks norm and orthogonality without floating-point square roots.
        """
        source=self.levels[start_clock-1]
        distributions={x:self.segment(start_clock,end_clock,x) for x in source}
        # Different inputs have orthogonal path records because the initial
        # source state is stored in each record; diagonal is exact total mass.
        return tuple(tuple(sum(distributions[x].values(),Q()) if x==y else Q()
                           for y in source) for x in source)


def endpoint_marginal(path_distribution):
    """Forget chronological labels and intermediate states; typically lossy."""
    result={}
    for path,weight in path_distribution.items():
        result[path.states[-1]]=result.get(path.states[-1],Q())+exact(weight)
    return result


def _partition_ids(values):
    lookup={}
    out=[]
    for value in values:
        try:
            hash(value)
        except TypeError as exc:
            raise HistoryTransportError("observations must be hashable") from exc
        if value not in lookup:
            lookup[value]=len(lookup)
        out.append(lookup[value])
    return tuple(out)


def bicausal_observation_quotient(chain,prior,observations):
    """Coarsest finite partition preserving BOTH forward and Bayes reverse kernels.

    Source law is fixed and strictly positive at EVERY state/time. Starting
    observations and the source's forward/backward rates induce monotone
    partition refinement; source-specific Bayes cotransitions are NOT Vp^*.
    """
    if not isinstance(chain,LabelledMarkovSource) or type(observations) is not tuple or len(observations)!=chain.horizon:
        raise HistoryTransportError("source and one observation table per clock required")
    for t,row in enumerate(observations):
        if type(row) is not dict or set(row)!=set(chain.levels[t]):
            raise HistoryTransportError("observations must cover the exact source")
    alpha=chain.marginals(prior)
    if any(alpha[t][x]<=0 for t,level in enumerate(chain.levels) for x in level):
        raise HistoryTransportError("Bayes reverse requires strictly positive supported marginals")
    K=tuple(chain.aggregate_kernel(t) for t in range(chain.horizon-1))
    R=[]
    for t in range(chain.horizon-1):
        R.append({y:{x:alpha[t][x]*K[t][x][y]/alpha[t+1][y]
                      for x in chain.levels[t]}
                  for y in chain.levels[t+1]})
    ids=tuple(_partition_ids(tuple(row[x] for x in chain.levels[t]))
              for t,row in enumerate(observations))
    initial=ids
    strict_rounds=0
    while True:
        newer=[]
        for t,level in enumerate(chain.levels):
            signature=[]
            for i,x in enumerate(level):
                front=()
                back=()
                if t<chain.horizon-1:
                    front=tuple(sum((K[t][x][y] for j,y in enumerate(chain.levels[t+1])
                                     if ids[t+1][j]==cell),Q())
                                for cell in range(max(ids[t+1])+1))
                if t>0:
                    back=tuple(sum((R[t-1][x][y] for j,y in enumerate(chain.levels[t-1])
                                    if ids[t-1][j]==cell),Q())
                               for cell in range(max(ids[t-1])+1))
                signature.append((ids[t][i],front,back))
            newer.append(_partition_ids(tuple(signature)))
        new_ids=tuple(newer)
        if new_ids==ids:
            break
        if sum(max(v)+1 for v in new_ids)<=sum(max(v)+1 for v in ids):
            raise ArithmeticError("refinement must split, never merge")
        ids=new_ids
        strict_rounds+=1
        if strict_rounds>sum(len(level) for level in chain.levels):
            raise ArithmeticError("finite source refinement did not stabilize")
    return {"partitions":ids,"initial_partitions":initial,"strict_rounds":strict_rounds,
            "source_marginals":alpha,"source_backward":tuple(R),
            "classes":tuple(tuple(tuple(x for i,x in enumerate(level) if ids[t][i]==cell)
                                  for cell in range(max(ids[t])+1))
                            for t,level in enumerate(chain.levels))}


def distinguishable_order_budget(active_events):
    """Lower bound for a faithful terminal register when all orders occur."""
    positive_integer(active_events,0)
    possibilities=factorial(active_events)
    return {"ordered_histories":possibilities,
            "minimal_binary_bits":(possibilities-1).bit_length(),
            "assumption":"all permutations admissible and source order must survive"}


def lift_field_growth_source(base,candidates,steps,epsilon=1):
    """Typed adapter to prior HISTORY-DTN fixed-edge field-guided source.

    The genuine SOURCE of event labels is the one newly inserted candidate
    edge in each subset step. Multiple physical edge orders remain distinct
    even if their final material graphs and boundary observations coincide.
    """
    from .growing_dtn_history import field_weighted_subset_process
    levels, kernels=field_weighted_subset_process(base,candidates,steps,epsilon)
    labelled=[]
    for t,rows in enumerate(kernels):
        table={}
        for source, targets in rows.items():
            events=[]
            for target,weight in targets.items():
                added=target-source
                if len(added)!=1:
                    raise ArithmeticError("previous growth source did not add one labelled edge")
                events.append((next(iter(added)),target,exact(weight)))
            table[source]=tuple(sorted(events,key=lambda ev:ev[0]))
        labelled.append(table)
    return LabelledMarkovSource(levels,tuple(labelled))
