"""Proof-producing finite cyclic automata from primitive clocks + carry + CRT.

A finite compiled machine is a newly CONSTRUCTED source transition system.
Never claim its higher quotients were already observed in the seed source.
"""
from dataclasses import dataclass
from .source_minimality import SourceLawError, factor


@dataclass(frozen=True)
class ClockCompilerSource:
    primitive_indices: tuple
    source_id: str
    epoch: int = 0
    allow_carry: bool = True
    allow_crt: bool = True

    def __post_init__(self):
        if (type(self.primitive_indices) is not tuple or
            len(self.primitive_indices)>16 or
            tuple(sorted(set(self.primitive_indices)))!=self.primitive_indices or
            any(type(p) is not int or factor(p)!={p:1} for p in self.primitive_indices)):
            raise SourceLawError('sorted primitive quotient indices required')
        if type(self.source_id) is not str or not self.source_id:
            raise SourceLawError('nonempty declared source-id required')
        if type(self.epoch) is not int or self.epoch<0:
            raise SourceLawError('nonnegative source epoch required')
        if type(self.allow_carry) is not bool or type(self.allow_crt) is not bool:
            raise SourceLawError('explicit capability flags required')

    def compile(self, word, *, state_budget=2048):
        if type(word) is not tuple or not word:
            raise SourceLawError('finite nonempty p-power exponent word required')
        if type(state_budget) is not int or not 1<=state_budget<=10000:
            raise SourceLawError('bounded state budget required')
        previous=0
        size=1
        for term in word:
            if type(term) is not tuple or len(term)!=2:
                raise SourceLawError('p-power factor must be a pair')
            p,k=term
            if (type(p) is not int or type(k) is not int or k<1 or p<=previous or
                p not in self.primitive_indices):
                raise SourceLawError('unsupported, duplicate or unordered prime seed')
            if k>1 and not self.allow_carry:
                raise SourceLawError('requires real carry coupling, not free virtual word')
            previous=p
            size*=p**k
            if size>state_budget:
                raise SourceLawError('compiled state count exceeds actual finite budget')
        if len(word)>1 and not self.allow_crt:
            raise SourceLawError('mixed-prime CRT gluing is not source-authorized')
        machine=CompiledClock(tuple(word),size,self.source_id,self.epoch)
        machine.verify()
        return machine


@dataclass(frozen=True)
class CompiledClock:
    factors: tuple
    order: int
    source_id: str
    epoch: int

    @property
    def origin(self):
        return tuple(tuple(0 for _ in range(k)) for p,k in self.factors)

    def successor(self, state):
        if type(state) is not tuple or len(state)!=len(self.factors):
            raise SourceLawError('state shape differs from declared clock source')
        output=[]
        for digits,(p,k) in zip(state,self.factors):
            if type(digits) is not tuple or len(digits)!=k:
                raise SourceLawError('clock digit vector mismatch')
            digits=list(digits)
            if any(type(d) is not int or not 0<=d<p for d in digits):
                raise SourceLawError('clock digit outside finite source')
            for j in range(k):
                if digits[j]+1<p:
                    digits[j]+=1
                    break
                digits[j]=0
            output.append(tuple(digits))
        return tuple(output)

    def state_at(self,t):
        if type(t) is not int or not 0<=t<self.order:
            raise SourceLawError('time outside a single finite observed cycle')
        out=[]
        for p,k in self.factors:
            n=t%(p**k)
            digits=[]
            for _ in range(k):
                digits.append(n%p)
                n//=p
            out.append(tuple(digits))
        return tuple(out)

    def verify(self):
        if not 1<=self.order<=10000:
            raise SourceLawError('invalid declared finite period')
        at=self.origin
        seen=set()
        carries={f'{p}^{j}':0 for p,k in self.factors for j in range(1,k)}
        for t in range(self.order):
            if at in seen or at!=self.state_at(t):
                raise AssertionError('not one coherent full-period successor orbit')
            seen.add(at)
            for coords,(p,k) in zip(at,self.factors):
                for j in range(1,k):
                    if all(coords[i]==p-1 for i in range(j)):
                        carries[f'{p}^{j}']+=1
            at=self.successor(at)
        if at!=self.origin or len(seen)!=self.order:
            raise AssertionError('failed cyclic wrap or coverage')
        for p,k in self.factors:
            for j in range(1,k):
                if carries[f'{p}^{j}']!=self.order//(p**j):
                    raise AssertionError('carry budget disagrees with source trace')
        return {'source_id':self.source_id,'epoch':self.epoch,
                'period':self.order,'primitive_seeds':tuple(p for p,k in self.factors),
                'carry_events_by_level':carries,
                'full_orbit_certified_finite':True,
                'all_power_clocks_already_observed_in_parent_source':False,
                'full_profinite_completion_observed':False}
