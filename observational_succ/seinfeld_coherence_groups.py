"""Finite Seinfeld SUCC coherence groups, checkpoint memory and source selectors.

Theorems are elementary finite disintegration, group-character factorization,
strong lumpability, and orthogonal martingale increments.  The reference law
is expressly declared, never substituted for the selected BBP time orbit.
The authentic source is imported from SUCC only in original_parity_checkpoint.

No quantum path integral, source-specific signed cancellation, or pi normality
is proved.  See research/2026-10-26/SEINFELD_COHERENCE_GROUPS.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import gcd

RADIX = 16


def _natural(x, minimum=0, maximum=100_000):
    if type(x) is not int or not minimum <= x <= maximum:
        raise ValueError(f"exact integer in [{minimum},{maximum}] required")
    return x


def _fraction(x):
    if type(x) not in (int, F):
        raise ValueError("exact rational required, not bool/float")
    return F(x)


def phase_group_modulus(h: int) -> int:
    """Minimal quotient Z/16 -> Z/d through which chi_h factors.

    Chi_h(j)=exp(2pi i h j /16); equality of two character values iff
    j congruent to k modulo d=16/gcd(16,h), including h=0 (d=1).
    """
    _natural(abs(h))
    return RADIX // gcd(RADIX, h)


def phase_groups(h: int) -> tuple[tuple[int, ...], ...]:
    d = phase_group_modulus(h)
    return tuple(tuple(j for j in range(RADIX) if j % d == c) for c in range(d))


def phase_partition_certificate(h: int) -> dict:
    """Exact modular character factorization; no complex rounding."""
    d = phase_group_modulus(h)
    groups = phase_groups(h)
    if any((h*(a-b)) % RADIX for group in groups for a in group for b in group):
        raise ArithmeticError("phase not constant on declared coherence fiber")
    candidates = (1, 2, 4, 8, 16)
    valid = [m for m in candidates if all((h*(a-b)) % RADIX == 0
              for a in range(RADIX) for b in range(RADIX) if a % m == b % m)]
    if min(valid) != d:
        raise ArithmeticError("phase quotient not minimal")
    return {"h": h, "modulus": d, "groups": groups,
            "minimal": True, "selected_phase_cancellation_proved": False}



def grouped_phase_amplitudes(probabilities, group_labels, phase_residues) -> dict:
    """Exact signed finite path-sum pushforward, BEFORE cyclotomic evaluation.

    The input is a declared working/selected probability distribution over
    histories, and a group label + actual character-phase exponent for each
    history.  Retain the full Q[Z/16] residue vector within each group.
    This is *not* a 16th-root-of-unity zero calculation: evaluating the vector
    in Q(zeta_16) is a separate map (see native lambda_source_duality).
    Group totals preserve the formal phase polynomial exactly. Replacing the
    resulting vector by its positive total mass would erase signed data.
    """
    count=len(probabilities)
    if not count or len(group_labels)!=count or len(phase_residues)!=count:
        raise ValueError("one weight, group label and phase per finite history")
    weights=tuple(_fraction(x) for x in probabilities)
    if any(x<0 for x in weights) or sum(weights)!=1:
        raise ValueError("nonnegative exactly normalized working law required")
    if any(type(p) is not int for p in phase_residues):
        raise ValueError("exact integer Fourier phase residues required")
    try:
        groups=tuple(dict.fromkeys(group_labels))
    except TypeError as exc:
        raise ValueError("hashable coherence labels required") from exc
    sums={g:[F()]*RADIX for g in groups}
    for weight,label,phase in zip(weights,group_labels,phase_residues):
        sums[label][phase % RADIX]+=weight
    values={g:tuple(sums[g]) for g in groups}
    total=tuple(sum((values[g][i] for g in groups),F()) for i in range(RADIX))
    if sum(total)!=1:
        raise ArithmeticError("path selection mass lost under quotient")
    return {"groups":values,"total":total,
            "complex_amplitude_preserved_formally":True,
            "cyclotomic_cancellation_proved_by_formal_zero":False,
            "pi_normality_proved":False}


def parity_evaluate_amplitude(vector) -> F:
    """Evaluate one formal residue vector at genuine chi_8(j)=(-1)^j."""
    if len(vector)!=RADIX:
        raise ValueError("a 16-coordinate formal phase vector required")
    return sum((_fraction(x) if j%2==0 else -_fraction(x)
                for j,x in enumerate(vector)),F())


def prefix_information(depth: int, observed: int) -> dict:
    """Exactly decompose log likelihood of selecting one 16-ary history.

    Reference: uniform on 16^depth complete paths; realized posterior is
    a single path.  Coherence quotient reveals only its first `observed`
    digits. KL values are logarithms of the returned exact integer bases:
      log(16^depth) = log(16^observed)+log(16^(depth-observed)).
    This is finite chain rule and not a stochastic source dynamics claim.
    """
    _natural(depth, 1, 1000)
    _natural(observed, 0, depth)
    n_paths = RADIX**depth
    group_mass_inv = RADIX**observed
    conditional_mass_inv = RADIX**(depth-observed)
    if group_mass_inv*conditional_mass_inv != n_paths:
        raise ArithmeticError("checkpoint information chain rule failed")
    return {"reference_paths": n_paths,
            "global_kl_log_base": n_paths,
            "checkpoint_kl_log_base": group_mass_inv,
            "unresolved_fiber_kl_log_base": conditional_mass_inv,
            "likelihood_second_moment": n_paths,
            "selected_weyl_saving_proved": False}


def reference_checkpoint_energy(horizon: int, revealed: int, frequency: int) -> F:
    """For F=(1/N)sum_{k=1}^N chi_h(J_k), iid Haar digits.

    E_ref |E[F | first revealed digits]|^2 = revealed/N^2 for 16∤h.
    This is not an estimate on one original-source selected history.
    """
    _natural(horizon, 1)
    _natural(revealed, 0, horizon)
    _natural(abs(frequency))
    if frequency % RADIX == 0:
        return F(1)
    return F(revealed, horizon*horizon)


def constant_selected_checkpoint(horizon: int, revealed: int) -> F:
    """All-zero realized 16-ary path has reference-backpropagated M_t=t/N."""
    _natural(horizon, 1)
    _natural(revealed, 0, horizon)
    return F(revealed, horizon)


def conditional_parity_checkpoint(counts) -> dict:
    """Global and working Fourier energy at h=8, exact rational.

    Rows are conditioning groups; columns are actual selected digit 0..15.
    Global = |E chi_8|^2; working = E |E[chi_8|group]|^2;
    gap = Var(E[chi_8|group])>=0. Refined conditioning increases energy,
    which is a bookkeeping identity and not a pi normality estimate.
    """
    if type(counts) not in (tuple,list) or not counts:
        raise ValueError("nonempty conditional branch count table required")
    rows=tuple(tuple(row) for row in counts)
    if any(len(row)!=RADIX or any(type(v) is not int or v<0 for v in row) for row in rows):
        raise ValueError("16 exact nonnegative integer counts per row")
    N=sum(sum(row) for row in rows)
    if N==0:
        raise ValueError("nonempty selected sample required")
    parity_differences=tuple(sum(row[::2])-sum(row[1::2]) for row in rows)
    global_energy=F(sum(parity_differences)**2,N*N)
    working_energy=sum((F(v*v,N*sum(row)) for v,row in zip(parity_differences,rows)
                       if sum(row)),F())
    gap=working_energy-global_energy
    if gap<0:
        raise ArithmeticError("conditional expectation norm declined")
    return {"observations":N, "global_energy":global_energy,
            "working_energy":working_energy, "checkpoint_information_energy":gap,
            "proves_source_mixing":False}


def quotient_transition(carrier, labels, transition):
    """Strong lumpability test for an exact finite stochastic operator.

    Rows transition[x][y] are rational probabilities. The pushforward to
    group labels is an operator iff *every* state in a group gives the
    same mass to each target group. A failed test returns a counter-witness,
    not a guessed quotient kernel. No unique physical dynamics asserted.
    """
    n=len(carrier)
    if not 1 <= n <= 128 or len(set(carrier)) != n:
        raise ValueError("1..128 distinct source states required")
    if len(labels) != n or len(transition)!=n:
        raise ValueError("one label/kernel row per declared state")
    matrix=tuple(tuple(_fraction(x) for x in row) for row in transition)
    if any(len(row)!=n or min(row)<0 or sum(row)!=1 for row in matrix):
        raise ValueError("rows must be nonnegative exact probability vectors")
    classes=tuple(dict.fromkeys(labels))
    first={c:next(i for i,a in enumerate(labels) if a==c) for c in classes}
    def projected(i):
        return tuple(sum((matrix[i][j] for j in range(n) if labels[j]==c),F()) for c in classes)
    rows={c:projected(i) for c,i in first.items()}
    for i,c in enumerate(labels):
        if projected(i) != rows[c]:
            return {"lumpable":False,"counterexample_state":carrier[i],
                    "counterexample_state_group":c,
                    "expected_group_row":rows[c],"actual_group_row":projected(i),
                    "pi_normality_proved":False}
    return {"lumpable":True,"group_labels":classes,
            "quotient_transition":tuple(rows[c] for c in classes),
            "pi_normality_proved":False}


def polya_working_weights(history: tuple[int,...]) -> tuple[F,...]:
    """16-color Pólya-urn working probabilities after a *declared* history."""
    if type(history) is not tuple or any(type(j) is not int or not 0<=j<RADIX for j in history):
        raise ValueError("finite 16-branch path tuple required")
    counts=[0]*RADIX
    for j in history: counts[j]+=1
    return tuple(F(1+c,RADIX+len(history)) for c in counts)


def polya_reference_likelihood(history: tuple[int,...]) -> F:
    """Exact RN weight of declared Pólya history relative to iid Haar.

    L_N = prod_{t=0}^{N-1}16*(1+N_{J_{t+1}}(t))/(16+t).
    Under reference iid digit measure E_ref L_N=1 (finite martingale).
    """
    if type(history) is not tuple or any(type(j) is not int or not 0<=j<RADIX for j in history):
        raise ValueError("finite 16-branch history tuple required")
    counts=[0]*RADIX
    result=F(1)
    for step,j in enumerate(history):
        result*=F(RADIX*(1+counts[j]),RADIX+step)
        counts[j]+=1
    return result


def polya_fourier_second_moment(horizon:int, frequency:int=1)->F:
    """Classical 16-color unit-prior Pólya ensemble E |A_N(h)|^2.

    Uniform single-time marginal does not imply realization cancellation:
    for 16∤h, E |A_N|²=(N+16)/(17N) -> 1/17.
    This is a *countermodel*; SUCC's BBP dynamics is not a Pólya urn.
    """
    _natural(horizon,1)
    _natural(abs(frequency))
    return F(1) if frequency%RADIX==0 else F(horizon+RADIX, (RADIX+1)*horizon)


def source_parity_checkpoint(horizon:int, bins:int=4)->dict:
    """Exact selected BBP history adapter, no substituted packet law.

    Only uses the repository's authoritative rational history and digit-bin
    table. This reports actual parity energies, **not a priori decay**.
    """
    _natural(horizon,1,1999)
    _natural(bins,1,4096)
    from .lambda_source_duality import original_history, branch_defect
    states=original_history(horizon)
    defect=branch_defect(states,bins)
    result=conditional_parity_checkpoint(defect.counts)
    if result["working_energy"]!=defect.exact_parity_energy():
        raise ArithmeticError("authentic conditional parity mismatch")
    return {"source":"original-four-pole-zero-initial",
            "horizon":horizon,"bins":bins,"result":result,
            "source_specific_saving_proved":False}


def testable_status():
    return {"finite_group_disintegration":True,"checkpoint_memory":True,
            "polya_reference_countermodel":True,
            "source_selected_fourier_energy_saving":False,
            "pi_base16_normality_proved":False}
