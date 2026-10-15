"""Well-founded ORDINAL ranks for extraordinarily long finite SUCC normalizations.

MATHEMATICAL CLAIMS, NOT RH:
- Finite Cantor-normal-form terms below epsilon_0 have a decidable exact order.
- Goodstein hereditary base-b replacement followed by decrement induces
  STRICT ordinal descent, even if natural numbers grow. The ALL-STAGE proof
  invokes classical well-foundedness of epsilon_0; finite tests don't prove it.
- Lexicographic reset counters are ranked by omega-polynomials and can have
  enormous but finite paths certified from a short source law.
- Ordinal pathwise termination, stochastic almost-sure termination, and
  source Weil quadratic PSD are separate mathematical properties.

No nontrivial zeta zeros or physical measurement inputs. Original ordinals
from ordinal_succ_report.py are FORMAL observer-limit stages; the ranks here
are a DIFFERENT, DECREASING ordinal variant of a terminating protocol.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction as Q
from math import isqrt


class OrdinalDescentError(ValueError):
    """A declared source program, normal form, or causal rank violates its law."""


def _nat(n:int,*,limit:int=1000000)->int:
    if type(n) is not int or not 0<=n<=limit:
        raise OrdinalDescentError("Typed exact nonnegative source integer required")
    return n


@dataclass(frozen=True)
class OrdinalCNF:
    """Finite Cantor normal form sum_i omega^exponent_i * coefficient_i.

    Recursively built terms are ALL < epsilon_0. Comparison is genuine
    ordinal CNF lexicographic comparison, NOT string or finite base-value
    comparison. No actual epsilon_0 value is computed.
    """
    terms: tuple[tuple["OrdinalCNF",int],...]=()

    def __post_init__(self):
        if type(self.terms) is not tuple:
            raise OrdinalDescentError("Exact finite ordinal CNF tuple required")
        for i,item in enumerate(self.terms):
            if (type(item) is not tuple or len(item)!=2
                    or not isinstance(item[0],OrdinalCNF)
                    or type(item[1]) is not int or item[1]<1):
                raise OrdinalDescentError("Ordinal coefficient and exponent typed source")
            if i and not (item[0]<self.terms[i-1][0]):
                raise OrdinalDescentError("CNF exponents must strictly decrease")

    def __lt__(self,other):
        if not isinstance(other,OrdinalCNF):
            return NotImplemented
        for (x,a),(y,b) in zip(self.terms,other.terms):
            if x!=y:return x<y
            if a!=b:return a<b
        return len(self.terms)<len(other.terms)

    def is_zero(self)->bool:
        return not self.terms

    def __str__(self):
        if self.is_zero():return "0"
        chunks=[]
        for exponent,coef in self.terms:
            if exponent.is_zero():
                chunks.append(str(coef))
            else:
                head=("ω" if exponent==ordinal_nat(1)
                      else "ω^("+str(exponent)+")")
                chunks.append(head+("*"+str(coef) if coef!=1 else ""))
        return " + ".join(chunks)


ZERO=OrdinalCNF()


def ordinal_nat(n:int)->OrdinalCNF:
    if type(n) is not int or n<0 or n.bit_length()>1024:
        raise OrdinalDescentError("Finite exact natural ordinal coefficient <=1024 bits")
    return ZERO if n==0 else OrdinalCNF(((ZERO,n),))


def ordinal_monomial(exponent:OrdinalCNF,coefficient:int=1)->OrdinalCNF:
    if not isinstance(exponent,OrdinalCNF) or type(coefficient) is not int or coefficient<=0:
        raise OrdinalDescentError("Source ordinal monomial requires finite CNF and positive count")
    return OrdinalCNF(((exponent,coefficient),))


def ordinal_lex_counters(counters:tuple[int,...])->OrdinalCNF:
    """(c_k,..,c_0) -> omega^k*c_k+...+omega*c_1+c_0."""
    if (type(counters) is not tuple or not 1<=len(counters)<=8
            or any(type(x) is not int or x<0 or x.bit_length()>1024 for x in counters)):
        raise OrdinalDescentError("Finite exact natural lex-counter source required")
    terms=[]
    for power,count in zip(range(len(counters)-1,-1,-1),counters):
        if count:
            terms.append((ordinal_nat(power),count))
    return OrdinalCNF(tuple(terms))


@dataclass(frozen=True)
class Hereditary:
    """Hereditary base expansion; terms=(recursive exponent, digit coefficient).

    Construct ONLY via hereditary_base of exact integers, which certifies
    canonical descending exponents and digits in the current source base.
    """
    terms: tuple[tuple["Hereditary",int],...]=()

    def ordinal(self)->OrdinalCNF:
        return OrdinalCNF(tuple((exponent.ordinal(),digit)
                                for exponent,digit in self.terms))

    def evaluate_at(self,base:int,*,max_bits:int=4096)->int:
        if type(base) is not int or not 2<=base<=512:
            raise OrdinalDescentError("Finite increasing hereditary base 2..512 only")
        if type(max_bits) is not int or not 8<=max_bits<=32768:
            raise OrdinalDescentError("Explicit finite arithmetic resource budget required")
        acc=0
        for exponent,digit in self.terms:
            if type(digit) is not int or not 1<=digit<base:
                raise OrdinalDescentError("Malformed hereditary digit")
            e=exponent.evaluate_at(base,max_bits=max_bits)
            if e>max_bits:
                raise OrdinalDescentError("Finite source exponent exceeds proof budget")
            if e and e*(base.bit_length()-1)>max_bits:
                raise OrdinalDescentError("Goodstein natural replacement would exceed bit budget")
            term=digit*(base**e)
            acc+=term
            if acc.bit_length()>max_bits:
                raise OrdinalDescentError("Goodstein natural replacement resource budget exhausted")
        return acc


def hereditary_base(n:int,base:int)->Hereditary:
    _nat(n,limit=10**10000)
    if type(base) is not int or not 2<=base<=512:
        raise OrdinalDescentError("Canonical hereditary base 2..512 required")
    if n.bit_length()>32768:
        raise OrdinalDescentError("Original source natural exceeds declared resource bound")
    digits=[]
    rest=n
    while rest>0:
        e=0
        power=1
        while power*base<=rest:
            power*=base
            e+=1
        coeff,rest=divmod(rest,power)
        if not 1<=coeff<base:
            raise ArithmeticError("Hereditary source digit outside canonical base")
        digits.append((hereditary_base(e,base),coeff))
    return Hereditary(tuple(digits))


@dataclass(frozen=True)
class GoodsteinStep:
    base:int
    natural_before:int
    natural_after:int
    hereditary_replaced_natural:int
    ordinal_before:OrdinalCNF
    ordinal_after:OrdinalCNF
    rank_strictly_decreased:bool
    natural_value_increased:bool
    original_source_mathematical_only:bool=True
    omega_iteration_executed:bool=False
    RH_proved:bool=False


def goodstein_step(n:int,base:int,*,max_bits:int=4096)->GoodsteinStep:
    """Canonical GOODSTEIN step, actual executable finite exact source.

    Goodstein n>0 in base b:
      hereditary-expansion(n,b) -> replace EVERY base b with b+1
      -> subtract exactly 1.
    The ordinal map replaces b by omega. Base-substitution preserves
    the BEFORE ordinal; subtract 1 strictly decreases it in base b+1.
    The universal assertion uses well-foundedness of epsilon_0.
    """
    _nat(n,limit=10**10000)
    if type(base) is not int or not 2<=base<512:
        raise OrdinalDescentError("Stage base 2<=b<512 required")
    if n==0:
        raise OrdinalDescentError("Terminal zero Goodstein stage has no successor")
    old=hereditary_base(n,base)
    substituted=old.evaluate_at(base+1,max_bits=max_bits)
    after=substituted-1
    new=hereditary_base(after,base+1)
    before_rank=old.ordinal()
    after_rank=new.ordinal()
    if not after_rank<before_rank:
        raise ArithmeticError("Well-founded ordinal Goodstein transition failed")
    return GoodsteinStep(base,n,after,substituted,before_rank,after_rank,
                        True,after>n)


def goodstein_prefix(initial:int,steps:int,*,max_bits:int=4096)->dict:
    """Finite trace, not a false numerical complete termination certificate."""
    _nat(initial,limit=10000)
    _nat(steps,limit=64)
    if initial==0:raise OrdinalDescentError("Nonempty genuine positive source required")
    current=initial
    base=2
    records=[]
    for _ in range(steps):
        if not current:break
        step=goodstein_step(current,base,max_bits=max_bits)
        records.append(step)
        current=step.natural_after
        base+=1
    return {"initial":initial,"source":"STANDARD_HEREDITARY_BASE_SUCC",
            "stages_executed":len(records),
            "natural_values":tuple([initial]+[x.natural_after for x in records]),
            "ordinal_rank_strings":tuple([str(x.ordinal_before) for x in records]+
                                         ([str(records[-1].ordinal_after)] if records else [])),
            "every_executed_transition_strictly_rank_decreases":True,
            "natural_growth_occurred":any(x.natural_value_increased for x in records),
            "last_value":current,"terminal_zero_reached_in_prefix":current==0,
            "unbounded_all_n_termination":
                "CLASSICAL_GOODSTEIN_WELLFOUNDED_EPSILON_0_THEOREM_NOT_FINITE_TRACE",
            "RH_proved":False}


@dataclass(frozen=True)
class HierarchicalCountdown:
    """Exact base-R counter with an ordinal lex rank, no huge trace execution.

    R=2^reset_bits; digits (c_k,..,c_0), 0<=c_i<R, k<=6.
    If c_0>0: decrement it.
    Else borrow from nearest nonzero higher digit, setting every lower
    digit to R-1. This is a SUCC law ranked by Σomega^i c_i.
    It takes EXACTLY V=sum(c_i R^i) steps to terminal 0, regardless
    of length: telescoping the source natural potential V proves count.
    The ordinal proof remains valid for far less uniform source reset
    functions, where this V may not be available.
    """
    digits:tuple[int,...]
    reset_bits:int

    def __post_init__(self):
        if (type(self.reset_bits) is not int or not 1<=self.reset_bits<=512
                or type(self.digits) is not tuple or not 1<=len(self.digits)<=7
                or any(type(x) is not int or not 0<=x<2**self.reset_bits
                       for x in self.digits)):
            raise OrdinalDescentError("Finite hierarchical source with exact bounded digit law")

    @property
    def rank(self)->OrdinalCNF:
        return ordinal_lex_counters(self.digits)

    @property
    def exact_remaining_steps(self)->int:
        base=1<<self.reset_bits
        return sum(c*base**i for c,i in zip(self.digits,range(len(self.digits)-1,-1,-1)))

    def successor(self)->"HierarchicalCountdown":
        if all(x==0 for x in self.digits):
            raise OrdinalDescentError("Terminal source protocol cannot step")
        new=list(self.digits)
        j=max(i for i,v in enumerate(new) if v)
        new[j]-=1
        for k in range(j+1,len(new)):
            new[k]=(1<<self.reset_bits)-1
        nxt=HierarchicalCountdown(tuple(new),self.reset_bits)
        if not nxt.rank<self.rank:
            raise ArithmeticError("Ordinal source rank not strictly decreasing")
        if nxt.exact_remaining_steps!=self.exact_remaining_steps-1:
            raise ArithmeticError("Finite giant path length law not preserved")
        return nxt


def giant_finite_path_certificate(digits:tuple[int,...],reset_bits:int)->dict:
    old=HierarchicalCountdown(digits,reset_bits)
    if not old.exact_remaining_steps:
        raise OrdinalDescentError("Source requested nonempty giant normal path")
    nxt=old.successor()
    return {
        "source":"EXACT_HIERARCHICAL_FINITE_SUCC_RESET_PROTOCOL",
        "state":old.digits,
        "ordinal_rank":str(old.rank),
        "next_state":nxt.digits,
        "next_ordinal_rank":str(nxt.rank),
        "one_step_rank_decreases":True,
        "steps_to_zero_certified_without_execution":old.exact_remaining_steps,
        "steps_bit_length":old.exact_remaining_steps.bit_length(),
        "finite_symbolic_proof_of_all_stages":True,
        "source_transition_law_is_declared":True,
        "path_executed_in_full":False,
        "RH_proved":False,
    }



@dataclass(frozen=True)
class OrdinalProofObligationQueue:
    """A model of finite recursive observer-normalization OBLIGATIONS.

    counts=(high,medium,low); source stages may DISCOVER many lower-priority
    tasks by discharging one higher-priority task. No transition may
    create tasks of the same/higher priority or discard source history.
    Rank ω² high+ω medium+low strictly decreases under these laws,
    even if counts of low tasks expand astronomically.

    This is a theorem about the declared symbolic QUEUE, not a claim
    that all real Tate/Weil problems have such a terminating queue or
    that any completed queue implies the desired arithmetic assertion.
    """
    counts:tuple[int,int,int]
    source_tag:str="DECLARED_SYNTHETIC_OBSERVER_NORMALIZER_NOT_ZETA"

    def __post_init__(self):
        if (type(self.counts) is not tuple or len(self.counts)!=3
                or any(type(v) is not int or v<0 or v.bit_length()>1024
                       for v in self.counts)
                or type(self.source_tag) is not str or not self.source_tag):
            raise OrdinalDescentError("Exact sourced finite proof obligation ranks and source name")

    @property
    def rank(self)->OrdinalCNF:
        return ordinal_lex_counters(self.counts)

    @property
    def finished(self)->bool:
        return self.counts==(0,0,0)

    def discharge_next(self,*,spawn_medium:int=0,
                       spawn_low:int=0)->"OrdinalProofObligationQueue":
        if self.finished:
            raise OrdinalDescentError("Finished queue is terminal; no source step")
        if (type(spawn_medium) is not int or type(spawn_low) is not int
                or min(spawn_medium,spawn_low)<0
                or max(spawn_medium,spawn_low).bit_length()>1024):
            raise OrdinalDescentError("Only finite exact lower-priority obligations may spawn")
        high,mid,low=self.counts
        if high:
            high-=1
            mid+=spawn_medium
            low+=spawn_low
        elif mid:
            if spawn_medium:
                raise OrdinalDescentError("Medium normalizer cannot produce new medium/higher debts")
            mid-=1
            low+=spawn_low
        else:
            if spawn_medium or spawn_low:
                raise OrdinalDescentError("Low normalizer cannot spawn equal/higher source debts")
            low-=1
        result=OrdinalProofObligationQueue((high,mid,low),self.source_tag)
        if any(v.bit_length()>1024 for v in result.counts) or not result.rank<self.rank:
            raise OrdinalDescentError("Source observer normalization cannot prove strict ordinal descent")
        return result


def gigantic_observer_proof_queue(bits:int=256)->dict:
    """A one-step source proof that creates 2^bits LOWER obligations.

    Rank ω² (one high obligation) -> ω + 2^bits (one medium and huge
    finite low list). Decrease is guaranteed by ordinal CNF; we do
    not execute the expansion or claim an authentic Weil sign proof.
    """
    if type(bits) is not int or not 1<=bits<=512:
        raise OrdinalDescentError("Finite symbolic spawn bit budget 1..512")
    parent=OrdinalProofObligationQueue((1,0,0))
    child=parent.discharge_next(spawn_medium=1,spawn_low=1<<bits)
    if not child.rank<parent.rank:
        raise ArithmeticError("Observer recursive rank reset did not decrease")
    return {"normalizer":"SOURCE_DECLARED_THREE_LEVEL_ORDINAL_QUEUE",
            "before_rank":str(parent.rank),
            "after_rank":str(child.rank),
            "spawned_low_count":1<<bits,
            "rank_decreased_strictly":True,
            "source_observer_growth_tasks_can_increase":True,
            "mathematical_no_infinite_strict_descent":"WELLFOUNDED_OMEGA_CUBE",
            "source_completed_Weil_claim_proved":False,
            "RH_proved":False}
