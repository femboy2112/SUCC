"""Observer-relative coherence: exact finite line/circle bridge probes and bounded falsifiers.

The full Busy Beaver theorem and compactness facts are paper proofs, not finite
algorithms. No finite result here establishes normality, physical observability,
or nonhalting of a machine that has not yet halted.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import lcm


def exact(value):
    if type(value) not in (int, Q):
        raise TypeError('Exact int or Fraction required; no floats')
    return Q(value)


def circle_bridge(x: int | Q, winding: int) -> Q:
    """Continuous group map R -> R/Z, x |-> winding*x mod 1."""
    if type(winding) is not int:
        raise TypeError('Integer winding required')
    return (winding * exact(x)) % 1


def finite_bridge_passport(probes: tuple[int | Q, ...]) -> dict:
    """A constructive rival consistent with EVERY declared finite rational probe.

    Both bridges commute with the 16-fold circle successor. The alternate
    winding is NOT a genuine original-source completion, merely a rival map.
    """
    if type(probes) is not tuple or not probes:
        raise ValueError('Declare nonempty finite probe tuple')
    samples = tuple(exact(q) for q in probes)
    M = lcm(*(v.denominator for v in samples))
    alt = M + 1
    witness = Q(1, 2 * M)
    for x in samples:
        if circle_bridge(x, 1) != circle_bridge(x, alt):
            raise ArithmeticError('Incorrect lcm or observer probe')
    if (circle_bridge(witness, alt) - circle_bridge(witness, 1)) % 1 != Q(1, 2):
        raise ArithmeticError('False distinguishing witness')
    return {
        'source_probe_count': len(samples), 'M': M,
        'rival_winding': alt, 'distinguishing_probe': witness,
        'distinguishing_phase_difference': Q(1, 2),
        'all_declared_rational_probes_agree': True,
        'both_maps_continuous_homomorphisms': 'PROVED_FOR_ALL_X',
        'both_commute_with_times16': 'PROVED_FOR_ALL_X',
        'candidate_is_original_global_bridge': False,
        'global_bridge_identified_by_finite_probes': False,
    }


def independent_congruence_check(x: int | Q, denominator_lcm: int) -> bool:
    """Alternate integer-divisibility oracle, not via circle_bridge."""
    z=exact(x)
    if type(denominator_lcm) is not int or denominator_lcm<1:
        raise ValueError('Positive integer M required')
    return (z.numerator * denominator_lcm) % z.denominator == 0


def original_fourpole(n: int) -> Q:
    if type(n) is not int or n<1:
        raise ValueError('Authentic BBP index n>=1 required')
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def original_prefix_probes(N:int)->tuple[Q,...]:
    """Pairs of real-circle observations and forcing, original U0=0."""
    if type(N) is not int or not 1<=N<=512:
        raise ValueError('Finite original-source horizon 1..512')
    u=Q(0); out=[]
    for n in range(1,N+1):
        r=original_fourpole(n)
        u=16*u+r
        out.extend((r,u%1))
    return tuple(out)


def integer_ring_phase_oracle(N:int) -> tuple[Q,...]:
    """Independent constant-modulus ring for authentic BBP phase prefixes."""
    if type(N) is not int or not 1<=N<=512:
        raise ValueError('Finite original-source horizon 1..512')
    forcings=tuple(original_fourpole(j) for j in range(1,N+1))
    D=lcm(*(r.denominator for r in forcings))
    if D%2 != 1:
        raise ArithmeticError('Authentic BBP conductor must be odd')
    residue=0; phases=[]
    for r in forcings:
        residue=(16*residue+r.numerator*(D//r.denominator))%D
        phases.append(Q(residue,D))
    return tuple(phases)


def bounded_machine_run(rules:dict, *, initial_ones:int=0, max_steps:int) -> dict:
    """Execute a small explicitly GIVEN binary TM for a finite step budget.

    State starts 0; missing rule is an ERROR, not a halting condition.
    Rule (state,read)->(write,move,next_state); next_state=-1 halts.
    This is not a universal halting decider or a Busy Beaver evaluator.
    """
    if type(initial_ones) is not int or not 0<=initial_ones<=10000 or type(max_steps) is not int or not 0<=max_steps<=100000:
        raise ValueError('Valid bounded machine resources required')
    if type(rules) is not dict or not rules:
        raise ValueError('Explicit complete reachable machine table required')
    tape={j:1 for j in range(initial_ones)}
    head=state=0
    for step in range(1,max_steps+1):
        read=tape.get(head,0)
        if (state,read) not in rules:
            raise ValueError('Missing reachable transition is not a halting proof')
        write,move,next_state=rules[(state,read)]
        if write not in (0,1) or move not in (-1,1) or type(next_state) is not int or next_state< -1:
            raise ValueError('Malformed transition')
        if write:tape[head]=1
        else:tape.pop(head,None)
        if next_state==-1:
            return {'status':'REFUTED_NONHALTING','first_observed_halt_step':step,
                    'budget':max_steps,'nonhalting_proved':False,
                    'exact_full_runtime':step}
        head+=move;state=next_state
    return {'status':'UNVERIFIED_AFTER_BUDGET','first_observed_halt_step':None,
            'budget':max_steps,'nonhalting_proved':False,
            'exact_full_runtime':None}


def finite_switch_survival(horizon:int,switch_at:int)->dict:
    """Moving alternative switches from zeros to ones AFTER observation horizon."""
    if type(horizon) is not int or type(switch_at) is not int or horizon<0 or switch_at<0:
        raise ValueError('Nonnegative finite horizon and transition index')
    return {'horizon':horizon,'switch_at':switch_at,
            'observed_all_zero':switch_at>horizon,
            'finite_source_witness':switch_at if switch_at>horizon else None,
            'one_finite_switch_source_valid_for_all_horizons':False,
            'infinite_never_switch_exists_in_declared_finite_switch_class':False}


def hidden_bridge_reports(action_word:tuple[int,...],hidden_left:int,hidden_right:int)->dict:
    """A toolkit-blind hidden tag; flip visible state only; declare new probe."""
    if type(action_word) is not tuple or any(type(b) is not int or b not in (0,1) for b in action_word) or any(type(t) is not int or t not in (0,1) for t in (hidden_left,hidden_right)):
        raise ValueError('Bounded exact visible flip actions and hidden bits required')
    observed=sum(action_word)%2
    return {'visible_reports':(observed,observed),
            'hidden_probe_reports':(hidden_left,hidden_right),
            'visible_indistinguishable':True,
            'target_identifiable_if_hidden_bits_differ':False,
            'new_hidden_probe_would_separate':hidden_left!=hidden_right}


def _is_prime(n: int) -> bool:
    if n < 2:return False
    if n % 2 == 0:return n == 2
    p=3
    while p*p<=n:
        if n%p==0:return False
        p+=2
    return True


def original_future_prime_discriminator(N:int)->dict:
    """Find a genuine future original four-pole denominator distinguishing b1.

    Dirichlet guarantees infinitely many p == 1 (mod 8); this bounded
    implementation is an exact finite certificate only for N<=512.
    A p>8N-2 is not a factor of ANY original forcing denominator up to N.
    Hence not a factor of any state denominator U_j (j<=N), and p at
    n=(p+7)/8 has original pole 4/p with no other p-pole.
    """
    if type(N) is not int or not 1<=N<=512:
        raise ValueError('Finite authentic source horizon 1..512')
    probes=original_prefix_probes(N)
    old=finite_bridge_passport(probes)
    p=8*((8*N-2)//8+1)+1
    while p<=8*N-2 or not _is_prime(p):
        p+=8
    n=(p+7)//8
    if n<=N:
        raise ArithmeticError('Future probe is not chronologically future')
    r=original_fourpole(n)
    M=old['M']
    if M%p==0 or (r.denominator%p)!=0 or (M*r)%1 == 0:
        raise ArithmeticError('Expected authentic prime-birth discriminator fails')
    return {'observed_through':N,'selected_future_prime':p,
            'new_original_source_time':n,'old_conductor':M,
            'new_source_forcing':r,
            'new_phase_shift_under_alternative':(M*r)%1,
            'old_source_prefix_compatible':True,
            'new_source_probe_refutes_rival':True,
            'busy_beaver_hardness_inferred':False}
