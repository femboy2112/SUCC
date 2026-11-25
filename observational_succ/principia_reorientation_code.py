"""Source-faithful error-correcting observational navigation for fixed action words.

An exact finite Hamming separation theorem. Bounded adversarial observation
errors (substitutions) are assumptions, not estimated statistical rates.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from typing import Sequence

from .principia_causal_memory import apply, observation
from .principia_reorientation import (
    ReorientationTask, ReorientationError, target, task_passport, validate_task,
)


@dataclass(frozen=True)
class LocalCode:
    source: str
    actions: tuple[str, ...]
    signatures: tuple[tuple[str, str, tuple[str, ...]], ...]  # world, target, reports
    min_target_distance: int | None


def hamming(a: Sequence[str], b: Sequence[str]) -> int:
    if len(a) != len(b):
        raise ReorientationError('incomparable report horizons')
    return sum(x != y for x,y in zip(a,b))


def make_local_code(task: ReorientationTask, actions: Sequence[str]) -> LocalCode:
    validate_task(task)
    c=task.carrier
    actions=tuple(actions)
    if any(a not in c.actions for a in actions):
        raise ReorientationError('unlicensed intervention in local code')
    rows=[]
    for w,q0 in zip(c.worlds,c.origins):
        state=q0
        responses=[observation(c,state)]
        for a in actions:
            state=apply(c,state,a)
            responses.append(observation(c,state))
        rows.append((w,target(task,(w,state)),tuple(responses)))
    distances=tuple(hamming(a[2],b[2]) for a,b in combinations(rows,2) if a[1]!=b[1])
    return LocalCode(task_passport(task),actions,tuple(rows),min(distances) if distances else None)


def verify_local_code(task: ReorientationTask, code: LocalCode) -> LocalCode:
    if code.source != task_passport(task):
        raise ReorientationError('unverified localization source/chart')
    if code != make_local_code(task,code.actions):
        raise ReorientationError('forged observational signatures or distance')
    return code


def guaranteed_error_budget(task: ReorientationTask, code: LocalCode) -> int | None:
    """Exact maximum number of arbitrary substitutions correctable for TARGET.

    None means target already constant across all original sources (no
    discrimination needed). A value -1 means even noiseless target recovery
    is not guaranteed by this fixed word.
    """
    verify_local_code(task,code)
    d=code.min_target_distance
    return None if d is None else (d-1)//2


def decode_with_bounded_errors(task: ReorientationTask, code: LocalCode,
                                observed: Sequence[str], max_errors: int) -> str:
    """Decode position/original source modulo declared target, else reject.

    This is a deterministic decoding rule over candidate source trajectories.
    No guarantee applies when more than max_errors actual sensor errors occur.
    """
    verify_local_code(task,code)
    if type(max_errors) is not int or max_errors < 0:
        raise ReorientationError('negative or ill-typed observation-error budget')
    observed=tuple(observed)
    if len(observed) != len(code.actions)+1:
        raise ReorientationError('truncated or extended local observation history')
    survivors={t for _,t,sig in code.signatures if hamming(sig,observed)<=max_errors}
    if len(survivors)!=1:
        raise ReorientationError('not uniquely source-locatable under declared error bound')
    return next(iter(survivors))
