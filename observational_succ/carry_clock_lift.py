"""Causal carry-coupling for rooted finite cyclic automata.

The skew-product C_m x C_p is a genuinely new phase-coupled clock,
not the uncoupled diagonal product and not an inference from finite access.
"""
from dataclasses import dataclass
from math import gcd
from .source_minimality import modulus, SourceLawError, rooted_diagonal_orbit


@dataclass(frozen=True)
class CarryClock:
    base_period: int
    counter_period: int
    carry_amount: int=1

    def __post_init__(self):
        modulus(self.base_period,150)
        modulus(self.counter_period,150)
        if type(self.carry_amount) is not int or not 0 <= self.carry_amount <= 200:
            raise SourceLawError('exact nonnegative carry amount required')
        if self.base_period*self.counter_period > 3000:
            raise SourceLawError('finite machine budget exceeded')

    def step(self,state):
        if type(state) is not tuple or len(state)!=2:
            raise SourceLawError('state must be a tuple (low, high)')
        x,y=state
        m,p=self.base_period,self.counter_period
        if type(x) is not int or type(y) is not int or not(0<=x<m and 0<=y<p):
            raise SourceLawError('state outside declared finite source')
        # SOURCE ACTION: the high counter advances only after a full lower lap.
        return ((x+1)%m, (y+self.carry_amount*(x==m-1))%p)

    def orbit(self):
        s=(0,0)
        out=[]
        while s not in out:
            out.append(s)
            s=self.step(s)
        if s!=(0,0): raise AssertionError('map did not return to rooted origin')
        return tuple(out)

    def period(self):
        return self.base_period*self.counter_period//gcd(self.counter_period,self.carry_amount)

    def certificate(self):
        orbit=self.orbit()
        theoretical=self.period()
        if len(orbit)!=theoretical:
            raise AssertionError('carry-period theorem failed finite check')
        if any(self.step(orbit[i])!=orbit[(i+1)%len(orbit)] for i in range(len(orbit))):
            raise AssertionError('carry dynamics not cyclic on its rooted orbit')
        return {"base":self.base_period,"counter":self.counter_period,
                "carry":self.carry_amount,"full_state_space":self.base_period*self.counter_period,
                "rooted_period":theoretical,"total_components":gcd(self.counter_period,self.carry_amount),
                "faithful_full_lift":theoretical==self.base_period*self.counter_period,
                "projection_to_base_is_successor_equivariant":True}


def carry_vs_uncoupled(m,p):
    coupled=CarryClock(m,p).certificate()
    independent=rooted_diagonal_orbit(m,p)
    return {"coupled_period":coupled['rooted_period'],
            "uncoupled_period":independent['diagonal_period'],
            "carry_is_strict_lift":coupled['rooted_period']>independent['diagonal_period']}
