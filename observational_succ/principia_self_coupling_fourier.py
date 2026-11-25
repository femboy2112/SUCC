"""Exact self-in-carrier Fourier fibers for a finite source-coupled observer.

The observer may know an action/observation history and its mathematical source
model while NOT knowing its real current position. Store ONE candidate spatial
phase-coded path for EVERY still-possible original world. No source world gets
a privileged 'actual' spectral phase without a discriminating observation.
"""
from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
import json

from .principia_causal_memory import (
    Carrier, CausalMemory, apply, observation, passport, verify_memory,
)
from .principia_dual_compass import (
    CompassError, AppraisalContract, appraisal_trace, dft4, idft4,
    GaussianRational, verify_appraisal,
)


@dataclass(frozen=True)
class SpatialChart4:
    source: str
    coordinates: tuple[int,...]  # state -> cyclic spatial atlas Z/4
    name: str = 'four-cell-observer-spatial-chart'


def make_chart(c:Carrier,coordinates)->SpatialChart4:
    passport(c)
    values=tuple(coordinates)
    if len(values)!=len(c.states) or any(type(x) is not int or not 0<=x<4 for x in values):
        raise CompassError('missing or illegal self-carrier spatial coordinates')
    return SpatialChart4(passport(c),values)


def verify_chart(c:Carrier, chart:SpatialChart4)->None:
    if chart != make_chart(c,chart.coordinates):
        raise CompassError('source/carrier spatial chart mismatch')


def chart_signature(c:Carrier, chart:SpatialChart4,scale:AppraisalContract)->str:
    verify_chart(c,chart)
    verify_appraisal(c,scale)
    return sha256(json.dumps((passport(c),chart.coordinates,scale.action_values,
                              scale.report_values),separators=(',',':')).encode()).hexdigest()


@dataclass(frozen=True)
class CandidateSelfPath:
    original_world: str
    current_state: str
    spatial_trace: tuple[int,int,int,int]
    modes: tuple[GaussianRational,...]


@dataclass(frozen=True)
class SelfCouplingFiber:
    source: str
    memory_source: str
    entries: tuple[CandidateSelfPath,...]


def self_coupled_fiber(c:Carrier,m:CausalMemory,chart:SpatialChart4,
                        scale:AppraisalContract)->SelfCouplingFiber:
    rows=verify_memory(c,m)
    mark=appraisal_trace(c,m,scale)
    lookup=dict(zip(c.states,chart.coordinates))
    survivors={w:q for w,q in rows}
    entries=[]
    for w,start in zip(c.worlds,c.origins):
        if w not in survivors:
            continue
        # Replay every action as a counterfactual of the same actually observed
        # history. Never read inaccessible hidden state from the true carrier.
        slots=[0,0,0,0]
        current=start
        slots[lookup[current]]+=1  # source-labelled original-position anchor
        for event, signed in zip(m.steps,mark):
            current=apply(c,current,event.action)
            if observation(c,current)!=event.outcome:
                raise CompassError('candidate source violates retained observation')
            slots[lookup[current]]+=1+signed
        if current!=survivors[w]:
            raise CompassError('candidate source lost its causal memory coupling')
        values=tuple(slots)
        entries.append(CandidateSelfPath(w,current,values,dft4(values)))
    return SelfCouplingFiber(chart_signature(c,chart,scale),m.source,tuple(entries))


def verify_self_coupled_fiber(c:Carrier,m:CausalMemory,chart:SpatialChart4,
                              scale:AppraisalContract,fiber:SelfCouplingFiber)->SelfCouplingFiber:
    expected=self_coupled_fiber(c,m,chart,scale)
    if fiber!=expected:
        raise CompassError('invented actual phase or erased a possible self-source')
    for entry in fiber.entries:
        if any(z.im for z in idft4(entry.modes)):
            raise CompassError('spatial phase encoding became non-real')
        if tuple(int(z.re) for z in idft4(entry.modes))!=entry.spatial_trace:
            raise CompassError('phase lost self-trajectory information')
    return fiber
