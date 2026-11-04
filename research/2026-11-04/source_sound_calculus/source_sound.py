"""Restricted source-sound judgment calculus: recheck every proof node.

Research proof interpreter, NOT a trusted general theorem prover, not Lean, and
NOT external physical attestation. All nonlogical introductions are whitelisted.
Models are declared synthetic finite sources from SUCC's existing observer draft.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parents[1]/'operational_foundations'
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
from operational_probe import DeclaredSource  # reuse sibling research carrier
from lcm_carrier import (bbp_origin,bbp_step,BBPRegister,divisor_join,
                         cyclic_join_finite,CarrierError)

class ProofError(ValueError):
    pass

ARITH='exact-arithmetic'
BBP='source:BBP-four-pole-original-U0=0'

_KINDS=frozenset({'ATOM','IMPLIES','AND','TRACE','CANDIDATES','REFINES',
                  'LCM_JOIN','CYCLIC_GLUE','BBP_REGISTER','JOURNAL','REACHABLE_INVARIANT'})

@dataclass(frozen=True)
class Claim:
    source:str
    kind:str
    data:tuple=()
    def __post_init__(self):
        if type(self.source) is not str or not self.source or self.kind not in _KINDS or type(self.data) is not tuple:
            raise ProofError('typed source, allowed judgement and immutable data required')
        if self.kind in ('IMPLIES','AND') and (len(self.data)!=2 or
          any(type(x) is not Claim or x.source!=self.source for x in self.data)):
            raise ProofError('connectives require two claims over a single source')
        if self.kind=='ATOM' and (len(self.data)!=1 or type(self.data[0]) is not str or not self.data[0]):
            raise ProofError('atomic hypotheses need one explicit nonblank label')


@dataclass(frozen=True)
class Proof:
    rule:str
    conclusion:Claim
    premises:tuple['Proof',...]=()
    inputs:tuple=()
    def __post_init__(self):
        if (type(self.rule) is not str or not self.rule or
                type(self.conclusion) is not Claim or type(self.premises) is not tuple or
                type(self.inputs) is not tuple or any(type(x) is not Proof for x in self.premises)):
            raise ProofError('strict proof tree type expected')


@dataclass(frozen=True)
class Checked:
    conclusion:Claim
    authority:str
    open_hypotheses:frozenset[Claim]
    uses_model:bool
    uses_arithmetic:bool
    nodes:int
    def status(self)->str:
        if self.open_hypotheses:return 'CONDITIONAL'
        if self.uses_model:return 'MODEL_EXACT_NOT_EMPIRICAL'
        return 'EXACT_FINITE_ARITHMETIC_OR_LOGIC'


@dataclass(frozen=True)
class Context:
    models:dict[str,DeclaredSource]=field(default_factory=dict)
    hypotheses:frozenset[Claim]=frozenset()
    def __post_init__(self):
        if type(self.models) is not dict or any(type(k) is not str or type(v) is not DeclaredSource or k!=v.source for k,v in self.models.items()):
            raise ProofError('models must be declared, source-matched finite worlds')
        if not isinstance(self.hypotheses,frozenset) or any(type(c) is not Claim for c in self.hypotheses):
            raise ProofError('explicit source-typed hypotheses only')


class Checker:
    """Closed rules; no arbitrary registration, callback, or empirical promotion.

    A model-wide finite statement is not an unrestricted physical/arithmetical
    theorem. A proof depends on its exact synthetic world and registered rules.
    """
    def __init__(self,context:Context,max_nodes:int=1024):
        if type(context) is not Context or type(max_nodes) is not int or not 1<=max_nodes<=100000:
            raise ProofError('context / finite proof resource budget required')
        self.ctx=context;self.limit=max_nodes

    def check(self,node:Proof)->Checked:
        active=set();seen={};count=0
        def recurse(p:Proof)->Checked:
            nonlocal count
            if type(p) is not Proof:raise ProofError('only checked proof nodes')
            ident=id(p)
            if ident in active:raise ProofError('cyclic proof graph')
            if ident in seen:return seen[ident]
            count+=1
            if count>self.limit:raise ProofError('finite proof budget exceeded')
            active.add(ident)
            pre=[recurse(q) for q in p.premises]
            if any(x.conclusion.source!=p.conclusion.source for x in pre):
                raise ProofError('unproved cross-source transport')
            a=frozenset().union(*(x.open_hypotheses for x in pre))
            model=any(x.uses_model for x in pre)
            arith=any(x.uses_arithmetic for x in pre)
            claim=p.conclusion
            q=p.inputs
            rule=p.rule
            def arity(np:int,nq:int):
                if len(pre)!=np or len(q)!=nq:raise ProofError(f'{rule} premise/payload arity invalid')
            if rule=='ASSUME':
                arity(0,0)
                if claim not in self.ctx.hypotheses:raise ProofError('unregistered source assumption')
                a=frozenset((claim,))
            elif rule=='AND_I':
                arity(2,0)
                if claim.kind!='AND' or claim.data!=(pre[0].conclusion,pre[1].conclusion):
                    raise ProofError('conjunction not justified')
            elif rule=='AND_E':
                arity(1,1)
                if pre[0].conclusion.kind!='AND' or type(q[0]) is not int or q[0] not in (0,1) or claim!=pre[0].conclusion.data[q[0]]:
                    raise ProofError('not a valid conjunction projection')
            elif rule=='IMP_I':
                arity(1,1)
                antecedent=q[0]
                if (type(antecedent) is not Claim or antecedent not in self.ctx.hypotheses or
                        claim.kind!='IMPLIES' or claim.data!=(antecedent,pre[0].conclusion)):
                    raise ProofError('hypothesis and exact implication required')
                a=a-frozenset((antecedent,))
            elif rule=='MP':
                arity(2,0)
                implication=pre[0].conclusion
                if implication.kind!='IMPLIES' or implication.data!=(pre[1].conclusion,claim):
                    raise ProofError('modus ponens premise mismatch')
            elif rule=='MODEL_TRACE':
                arity(0,2)
                if claim.kind!='TRACE' or claim.source not in self.ctx.models:
                    raise ProofError('only declared synthetic source traces permitted')
                start,word=q
                if type(start) is not int or type(word) is not tuple or any(type(z) is not str for z in word):
                    raise ProofError('malformed initial state or operation word')
                try: out,end=self.ctx.models[claim.source].execute(start,word)
                except Exception as e: raise ProofError('invalid model probe execution') from e
                if claim.data!=(start,word,out,end):raise ProofError('claimed trace was not performed in model')
                model=True
            elif rule=='MODEL_JOURNAL':
                arity(1,0)
                tr=pre[0].conclusion
                if tr.kind!='TRACE' or claim.kind!='JOURNAL' or tr.source not in self.ctx.models:
                    raise ProofError('a model journal must be derived from its actual model trace')
                start,word,out,end=tr.data
                entries=tuple((tr.source,act,reading) for act,reading in zip(word,out))
                if claim.data!=(start,entries,end):
                    raise ProofError('journal provenance/outcome mismatch')
                model=True
            elif rule=='MODEL_FILTER':
                arity(1,0)
                tr=pre[0].conclusion
                if tr.kind!='TRACE' or claim.kind!='CANDIDATES' or tr.source not in self.ctx.models:
                    raise ProofError('candidate inference demands a true model trace')
                start,word,out,end=tr.data
                possible=self.ctx.models[tr.source].observed_initials(word,out)
                if claim.data!=(word,out,possible):raise ProofError('model evidence fiber differs')
                model=True
            elif rule=='MODEL_REFINEMENT':
                arity(0,2)
                if claim.kind!='REFINES' or claim.source not in self.ctx.models:raise ProofError('model-specific source required')
                lo,hi=q
                if (type(lo) is not tuple or type(hi) is not tuple or len(lo)!=3 or len(hi)!=3):
                    raise ProofError('explicit tool/depth/budget triples required')
                tl,dl,bl=lo;th,dh,bh=hi
                if (type(tl) is not tuple or type(th) is not tuple or type(dl) is not int or
                        type(dh) is not int or type(bl) is not int or type(bh) is not int or
                        not set(tl)<=set(th) or dl>dh or bl>bh):
                    raise ProofError('missing toolkit inclusion / temporal budget monotonicity')
                try:
                    small=self.ctx.models[claim.source].observation_classes(tl,dl,bl)
                    large=self.ctx.models[claim.source].observation_classes(th,dh,bh)
                except Exception as e: raise ProofError('invalid source probe refinement') from e
                if claim.data!=(lo,hi,small,large) or not all(any(set(x)<=set(y) for y in small) for x in large):
                    raise ProofError('coarse partition fails to contain fine classes')
                model=True
            elif rule=='MODEL_INDUCT':
                arity(0,3)
                if claim.kind!='REACHABLE_INVARIANT' or claim.source not in self.ctx.models:
                    raise ProofError('only model-scoped induction from a verified law')
                initial,toolkit,predicate=q
                src=self.ctx.models[claim.source]
                if (type(initial) is not int or not 0<=initial<src.count or
                        type(toolkit) is not tuple or len(set(toolkit))!=len(toolkit) or
                        type(predicate) is not tuple or len(predicate)!=src.count or
                        any(type(x) is not bool for x in predicate)):
                    raise ProofError('total finite predicate, source and toolkit required')
                try: instruments=tuple(src.instrument(name) for name in toolkit)
                except Exception as e:raise ProofError('undeclared source instrument') from e
                if not predicate[initial]:raise ProofError('initial state does not satisfy invariant')
                if any(predicate[state] and not predicate[ins.successor[state]]
                       for ins in instruments for state in range(src.count)):
                    raise ProofError('source step fails invariant preservation')
                if claim.data!=(initial,toolkit,predicate):
                    raise ProofError('unearned inductive conclusion')
                model=True
            elif rule=='ARITH_LCM':
                arity(0,0)
                if claim.kind!='LCM_JOIN' or claim.source!=ARITH or len(claim.data)!=3:
                    raise ProofError('arithmetic source/type required')
                x,y,L=claim.data
                try: computed=divisor_join(x,y)
                except (CarrierError,TypeError) as e: raise ProofError('invalid divisibility operands') from e
                if type(L) is not int or L!=computed:raise ProofError('LCM least join false')
                arith=True
            elif rule=='ARITH_CYCLIC_GLUE':
                arity(0,0)
                if claim.kind!='CYCLIC_GLUE' or claim.source!=ARITH or len(claim.data)!=6:
                    raise ProofError('cyclic arithmetic source/type required')
                x,y,g,L,ker,image=claim.data
                try: actual=cyclic_join_finite(x,y)
                except (CarrierError,TypeError) as e: raise ProofError('invalid finite gluing') from e
                if (g,L,ker,image)!=(actual.gcd,actual.lcm,actual.kernel_size,actual.image_size):
                    raise ProofError('wrong source overlap / group join')
                arith=True
            elif rule=='BBP_ORIGIN':
                arity(0,0)
                if claim.source!=BBP or claim.kind!='BBP_REGISTER' or claim.data!=(0,1,0,None):
                    raise ProofError('authentic BBP source must start with zero register')
                arith=True
            elif rule=='BBP_STEP':
                arity(1,0)
                if claim.source!=BBP or claim.kind!='BBP_REGISTER' or pre[0].conclusion.kind!='BBP_REGISTER':
                    raise ProofError('original source step requires an authenticated predecessor')
                try:
                    state=BBPRegister(*pre[0].conclusion.data)
                    nxt=bbp_step(state)
                except (CarrierError,ValueError) as e: raise ProofError('invalid BBP register') from e
                if claim.data!=(nxt.time,nxt.clock,nxt.numerator,nxt.last_carry):
                    raise ProofError('unearned BBP successor or dropped literal carry')
                arith=True
            else:
                raise ProofError('unregistered or unsafe inference rule: '+rule)
            res=Checked(claim,'CHECKED_RESEARCH_RULE',a,model,arith,count)
            active.remove(ident)
            seen[ident]=res
            return res
        return recurse(node)
