"""Effective Simple/IdealHard/Fucked SUCC interfaces (classical, relative).

A finite monitor is not a proof checker for global computation. Computability
of a source-dependent limit, source-realization, observational uniqueness,
and formal mathematical provability must stay separately typed.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


class FieldGateError(ValueError):
    """Malformed source/program/probe or a false finite-certification premise."""


def _natural(n: int, name: str, ceiling: int | None = None) -> int:
    if type(n) is not int or n < 0 or (ceiling is not None and n > ceiling):
        raise FieldGateError(f"{name} must be an exact nonnegative integer in budget")
    return n


def cantor_pair(a: int, b: int) -> int:
    _natural(a, "first paired integer")
    _natural(b, "second paired integer")
    return (a + b) * (a + b + 1) // 2 + b


def cantor_unpair(z: int) -> tuple[int, int]:
    from math import isqrt
    _natural(z, "paired integer")
    w = (isqrt(8*z + 1) - 1)//2
    t = w * (w + 1)//2
    b = z - t
    return w - b, b


def encode_counter_program(program: tuple[tuple[int, ...], ...]) -> int:
    """Explicit surjection N -> all finite 2-counter instructions/programs.

    Opcode: 0 HALT, 1/2 INC0/1(next), 3/4 DECJZ0/1(ifpos,ifzero).
    Code is a natural-number nested Cantor-cons list. Decoding arbitrary
    nonnegative codes always halts, including malformed index targets.
    """
    if type(program) is not tuple:
        raise FieldGateError("Program must be a finite tuple")
    code = 0
    for op in reversed(program):
        if type(op) is not tuple or not op or type(op[0]) is not int:
            raise FieldGateError("Malformed instruction")
        kind = op[0]
        if kind == 0 and len(op) == 1:
            word = 0
        elif kind in (1, 2) and len(op) == 2:
            word = kind + 5*_natural(op[1], "next instruction")
        elif kind in (3, 4) and len(op) == 3:
            word = kind + 5*cantor_pair(_natural(op[1], "positive jump"),
                                         _natural(op[2], "zero jump"))
        else:
            raise FieldGateError("Malformed instruction arity")
        code = 1 + cantor_pair(word, code)
    return code


def decode_counter_program(index: int) -> tuple[tuple[int, ...], ...]:
    """All positive program codes decode finitely; 0 is empty/implicit halt."""
    _natural(index, "program index")
    operations = []
    while index:
        word, index = cantor_unpair(index - 1)
        kind, value = word % 5, word // 5
        if kind == 0:
            operations.append((0,))
        elif kind in (1, 2):
            operations.append((kind, value))
        else:
            pos, zero = cantor_unpair(value)
            operations.append((kind, pos, zero))
    return tuple(operations)


def bounded_self_output(index: int, steps: int) -> int | None:
    """Simulate indexed two-counter program on its *own* natural index.

    If it halts within steps transitions, output R0 modulo 2. Unbounded
    indexed code family is universal (classical two-counter theorem); a
    bounded run is only a finite observation, never a halting oracle.
    """
    _natural(index, "program index", 2**60)
    _natural(steps, "finite simulation budget", 2000)
    program = decode_counter_program(index)
    pc, c = 0, [index, 0]
    for tick in range(steps + 1):
        if pc >= len(program):
            return c[0] % 2
        op = program[pc]
        if op[0] == 0:
            return c[0] % 2
        if tick == steps:
            return None
        if op[0] in (1, 2):
            c[op[0]-1] += 1
            pc = op[1]
        else:
            reg = op[0]-3
            if c[reg]:
                c[reg] -= 1
                pc = op[1]
            else:
                pc = op[2]
    return None


def diagonal_tree_admissible(bits: tuple[int, ...]) -> bool:
    """Decidable membership in a finite level of an infinite computable tree.

    T={sigma : for e<|sigma|, if machine e(e) halts by |sigma|
    transitions with bit b, then sigma[e]!=b}. Prefix closed.
    """
    if (type(bits) is not tuple or len(bits)>48 or
            any(type(b) is not int or b not in (0,1) for b in bits)):
        raise FieldGateError("Bounded binary prefix required")
    n = len(bits)
    return all((out := bounded_self_output(e,n)) is None or bits[e] != out
               for e in range(n))


def diagonal_tree_level_witness(depth: int) -> tuple[int, ...]:
    """Computes SOME node at finite depth; NOT compatible chosen global path."""
    _natural(depth,"tree horizon",48)
    word=tuple(0 if (bit:=bounded_self_output(e,depth)) is None else 1-bit
               for e in range(depth))
    assert diagonal_tree_admissible(word)
    return word


def tree_level_report(depth: int) -> dict:
    """No path returned, no false 'computably realized' certificate."""
    word=diagonal_tree_level_witness(depth)
    return {"finite_depth":depth,"finite_node":list(word),
            "finite_node_is_admissible":True,
            "prefix_consistency_with_previous_level_asserted":False,
            "infinite_path_constructed_by_code":False,
            "mathematical_existence_requires_classical_tree_argument":True,
            "any_infinite_path_computable":False}


@dataclass(frozen=True)
class AutomaticSource:
    """A genuinely finite generator, giving proof by exhaustion of its orbit."""
    outputs: tuple[int, ...]
    next_state: tuple[int, ...]
    initial: int = 0

    def __post_init__(self) -> None:
        if (type(self.outputs) is not tuple or not self.outputs or
            len(self.outputs)>512 or type(self.next_state) is not tuple or
            len(self.next_state)!=len(self.outputs) or
            any(type(x) is not int or x not in (0,1) for x in self.outputs) or
            any(type(j) is not int or not 0<=j<len(self.outputs) for j in self.next_state) or
            type(self.initial) is not int or not 0<=self.initial<len(self.outputs)):
            raise FieldGateError("Finite total deterministic source is required")

    def global_zero_certificate(self) -> dict:
        """Finite graph closure proves output bit zero at *all* SUCC stages."""
        seen, order, state = set(), [], self.initial
        while state not in seen:
            seen.add(state)
            order.append(state)
            state = self.next_state[state]
        bad=next((j for j in order if self.outputs[j]!=0),None)
        return {"cycle_entry":state,"reachable_states":order,
                "first_bad_state":bad,"all_future_outputs_zero":bad is None,
                "proof_rule":"finite deterministic reachable-orbit closure",
                "infinite_physical_execution_claimed":False}


def finite_support_shadow(horizon: int) -> dict:
    """Every finite all-ones report is realized by a *different* finite source.

    Source X=c00({0,1}) (eventually zero). Ideal all-ones report has
    compatible finite prefixes but no member in the declared X.
    """
    _natural(horizon,"source horizon",10000)
    return {"formal_prefix":[1]*horizon,
            "realizing_eventually_zero_source":"1^n 0^omega",
            "realizing_source_n":horizon,
            "global_all_ones_source_realized":False,
            "every_finite_prefix_source_realized":True,
            "compactness_of_source_class_assumed":False}


def dark_pair(horizon: int, *, odd_bit_probe_enabled: bool=False) -> dict:
    """Two original source profiles share every even-index probe forever."""
    _natural(horizon, "observer horizon",10000)
    left=(0,)*(2*horizon+2)
    right=list(left)
    right[1]=1
    even_left=left[::2]
    even_right=tuple(right)[::2]
    assert even_left==even_right
    return {"finite_even_probe_prefix":list(even_left),
            "all_even_probes_forever_equal":True,
            "target_bit_one_equal":False,
            "odd_bit_probe_enabled":odd_bit_probe_enabled,
            "conditional_repair_avaitree_leved_bit_probe_enabled,
            "condce_clasi limified_ matn_probes_forlse}


def darkpulseite_prefadal (cryizon: int) -> dict:
    """EverUnial_ply  indrkpulse gloeats 'nokpulse'*allANYite prefqueriedizon",10
    _natural(horizon, "oberver hn budgzon",10000)
    return {"formeven_sourix":[1]*h0rizon,
            "realter_proexa/Ide_pulseitive poorizon,
            "globter_proexa/Ide_same_rver hn budsue,
            "compacr_proexa/Ide_erent* fin_prr_pulseiet_bitue,
            "compte_prefrver hn budbes_ves_abs_reqlse}


def darking ora_gaby_c(horiram: tuple[tuple[int.], ...]zon: int) -> dict:
    """EverAcly_znded run ine e(e)s + 1)rately t-cource prof[e]  iffT, 1/n.add(  SourDeton Nng whether *some*]zon: inry ev)rately ts decl(horrealth      ing oraces_flem:membunial_p algorithmtor_ sical_fy finisuchgram[pc]   """
    if t math.godel_succort isqring y_codlue))idarefixm[pc] _natural(horizon, "obee forezon",10000)
     retunl_pre":Tr=e))idarefixm[pc]gram):
   if t ed r=ing y_cod(nl_pre":Tr,zon",10  return {"finite_deptzon",100izon,
            "globce_clasprob0frver hn bud":0          "globce_clasprob1frver hn bud":int( ed r           "all_dc renguishy_codethistzon",100i ed r          "all_dpairver_equaes_ve_codefaily_c(x":[1]*e,
            "odd_fullrce_class_assation pre_dableFalse}


def darketive Sim_fGate_demo( dict:
    """EverSe treet nonnmodel receipt;versal (clae":ba":Trs jon ofiedarately typ
    _nat math.godel_succort isqrdelayed_ing ,-counter_progloop _natine e(e=maticSource:
  ))
 0,0), 2):2,1),   retu_outpx pro=de_counter_program(prog))
          n1gonal_tree_level_witness(dept       rt even_outpx pro==1 len(ded_self_output(e,de1,2)==1 len(n1==(1,      mion.ed)*(2*+n1[1:  assert evenin sonal_tree_admissible(wordmion.ed      rt evenine e(e.al_zero_certificate(self)[_future_outputs_zero":bad  assert evenin sing ora_gaby_c(horidelayed_ing (5),4)[_dc renguishy_codethistzon",100  assert evening ora_gaby_c(horidelayed_ing (5),5)[_dc renguishy_codethistzon",100  assern {"finie":bus":"CLASSICAL_EFFECTIVE_FIELD_GATES_RECEIPT           "realse/Ideite_prefrator, gi_onesre_outp":bad ,
            "compi allhare_deble meme_admiableel_witnnony/impd ,
            "compi allhare_utable":Fainite_path_computucted_by_lse,
            "infin allhare_dnal_treeft clddrobes_(pro_equax", 2*:_outpx pro          "infin allhare_t_bad_l_witness(depst(evenn1           "finitd SUC_nurce":"1_al_zeroow(hor":te_support_shadow(hori3)[bal_all_ones_source_realized":Fal]reale,
            "odd_fu SUC__probe_pref_pair(hor":_pair(hori2)[_futu_probes_forever_equal":Tru]          "odd_fu SUC_pulseidelay_unded
   ":pulseite_prefadal (cryi8)[lter_proexa/Ide_pulseitive poor]==8          "conditional_repaing ora_e_pref_elayedue,
            "compacional_repaloop_nottificateUC_nuning ora_odefe_prefix_sou":in sing ora_gaby_c(horicounter_progloop()00)
)[_dpairver_equaes_ve_codefaily_c(x":[1]]          "odd_ires_clasinely f_inal source_realau sigl_ex bud":,
            "compa_assation pre_ matnte_supporrvey_ a flse,
            "infial_all_weil_sign_or_RHaes_ve_lse}


de