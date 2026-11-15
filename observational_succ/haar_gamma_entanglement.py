"""Exact quantum/Haar/Gamma source-instrument bridge in a declared 2-qubit model.

Mathematical models ONLY, not measured physical reality or an ER=EPR metric.
All comparisons use Gaussian rational exact arithmetic; no floating-point tests.
Physical outcome records and source-calibrated channels remain independent gates.

The SUCC radix-16 digit-parity character h=8, (-1)^a, becomes Pauli Z on
our two selected digit states |0>,|1>. An X/Y probe is a *new physical
complementary basis*, not postprocessing of the classical digit-Haar table.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from typing import Iterable

@dataclass(frozen=True)
class GQ:
    re: F = F(0)
    im: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 're', F(self.re))
        object.__setattr__(self, 'im', F(self.im))
    def __add__(self, o):
        z=to_gq(o); return GQ(self.re+z.re,self.im+z.im)
    def __radd__(self, o): return self+o
    def __neg__(self):return GQ(-self.re,-self.im)
    def __sub__(self,o):return self+(-to_gq(o))
    def __rsub__(self,o):return to_gq(o)-self
    def __mul__(self,o):
        z=to_gq(o);return GQ(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    def __rmul__(self,o):return self*o
    def conjugate(self):return GQ(self.re,-self.im)
    def abs2(self):return self.re*self.re+self.im*self.im
    def __truediv__(self,o):
        z=to_gq(o)
        if not z.abs2():raise ZeroDivisionError('zero Gaussian rational')
        a=self*z.conjugate();return GQ(a.re/z.abs2(),a.im/z.abs2())
    def __pow__(self,n:int):
        if type(n) is not int:raise TypeError('integer powers only')
        if n<0:return (GQ(1)/self)**(-n)
        result=GQ(1);base=self
        while n:
            if n&1:result=result*base
            base=base*base;n//=2
        return result

def to_gq(x):
    if isinstance(x,GQ):return x
    if isinstance(x,(F,int)) and not isinstance(x,bool):return GQ(F(x))
    raise TypeError('Only exact rational and Gaussian rational scalars are accepted')

O=GQ(0);I=GQ(1);J=GQ(0,1)

def gamma_phase(depth:int,omega:F|int=1)->GQ:
    """E[e^-i omega T] for T~Gamma(depth,1), depth integer, incl delta_0."""
    if type(depth) is not int or depth<0:raise ValueError('nonnegative integer Gamma depth')
    if type(omega) not in (int,F):raise ValueError('exact rate frequency')
    return (I+J*omega)**(-depth)

def sector_state(coherence:GQ):
    """rho_gamma on |00>,|11>. Physical when |gamma|<=1."""
    g=to_gq(coherence)
    if g.abs2()>1:raise ValueError('coherence violates positivity')
    r=[[O for _ in range(4)] for _ in range(4)]
    r[0][0]=GQ(F(1,2));r[3][3]=GQ(F(1,2))
    r[0][3]=g/2;r[3][0]=g.conjugate()/2
    return tuple(tuple(z for z in row) for row in r)

def matmul(a,b):
    n=len(a);m=len(b[0]);k=len(b)
    if not n or any(len(row)!=k for row in a) or any(len(row)!=m for row in b):raise ValueError('matrix dimensions')
    return tuple(tuple(sum((a[i][q]*b[q][j] for q in range(k)),O) for j in range(m)) for i in range(n))
def matadd(a,b):return tuple(tuple(x+y for x,y in zip(ar,br)) for ar,br in zip(a,b))
def adjoint(a):return tuple(tuple(a[j][i].conjugate() for j in range(len(a))) for i in range(len(a[0])))
def kron(a,b):return tuple(tuple(a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])] for j in range(len(a[0])*len(b[0]))) for i in range(len(a)*len(b)))
def trace(a):return sum((a[i][i] for i in range(len(a))),O)
def expectation(rho,observable):return trace(matmul(rho,observable))
def reduced_b(rho):return tuple(tuple(sum((rho[2*a+b][2*a+c] for a in (0,1)),O) for c in (0,1)) for b in (0,1))

PAULI={
    'I':((I,O),(O,I)),
    'X':((O,I),(I,O)),
    'Y':((O,-J),(J,O)),
    'Z':((I,O),(O,-I)),
}

def joint_pauli(rho,left,right):
    return expectation(rho,kron(PAULI[left],PAULI[right]))

def local_projective_a(rho,basis:str,outcome:int):
    """(outcome probability, conditional receiver B state), selective A probe.

    Incoherent with outcome => returns (0,None). B local marginal without
    the classical A outcome is ALWAYS computed separately, not replaced by this.
    """
    if basis not in ('X','Y','Z') or type(outcome) is not int or outcome not in (-1,1):raise ValueError('basis and signed outcome')
    p=tuple(tuple((PAULI['I'][i][j]+outcome*PAULI[basis][i][j])/2 for j in (0,1)) for i in (0,1))
    K=kron(p,PAULI['I'])
    unnorm=matmul(matmul(K,rho),adjoint(K))
    b=reduced_b(unnorm)
    prob=trace(b)
    if prob.im or prob.re<0:raise ArithmeticError('not a quantum effect probability')
    return prob.re, (tuple(tuple(v/prob.re for v in row) for row in b) if prob.re else None)

def nonselective_b(rho,basis:str):
    """Receiver state after forgetting the local A measurement outcome."""
    acc=((O,O),(O,O))
    for s in (-1,1):
        p,b=local_projective_a(rho,basis,s)
        if b is not None:acc=matadd(acc,tuple(tuple(p*z for z in row) for row in b))
    return acc

def gamma_dephase(rho_coherence:GQ,depth:int,omega:F|int=1):
    """Gamma-average of local A phase U_t=diag(1,e^{i omega t})."""
    return sector_state(rho_coherence*gamma_phase(depth,omega))

def co_moving_gauge_sector(coherence:GQ):
    """U_t on A and conjugate U_t on B fix the entire marked bond sector."""
    return sector_state(coherence)

def marked_digit_haar_parity(digit:int)->int:
    """The exact SUCC radix-16 h=8 Fourier/Walsh character on a digit."""
    if type(digit) is not int or not 0<=digit<16:raise ValueError('one hexadecimal digit')
    return 1 if digit%2==0 else -1

def signed_haar_bond_contrast(g:GQ):
    """(diagonal Haar ZZ, complementary XX, complementary XY)."""
    r=sector_state(g)
    return joint_pauli(r,'Z','Z'),joint_pauli(r,'X','X'),joint_pauli(r,'X','Y')

def chsh_optimum_squared(g:GQ)->F:
    """Horodecki optimal squared CHSH for marked Bell-dephasing family."""
    if g.abs2()>1:raise ValueError('nonphysical coherence')
    return 4*(1+g.abs2())

def ppt_negative_minor(g:GQ)->F:
    """2x2 principal minor of rho^partial_transpose_B: -|gamma|²/4."""
    return -g.abs2()/4

def outcome_product_plus_probability(g:GQ,which:str='XY')->F:
    """Probability product of +/-1 outcomes is +1 for chosen joint Pauli."""
    r=sector_state(g)
    if which not in ('ZZ','XX','XY'):raise ValueError('authored joint Haar/complementary probe')
    corr=joint_pauli(r,which[0],which[1])
    if corr.im:raise ArithmeticError('Hermitian expectation must be real')
    return (1+corr.re)/2

def fresh_repetition_bayes(n:int,correct_model:GQ,wrong_model:GQ,which:str):
    """Posterior after n independent positively scored fresh preparations.

    This is NOT multiplying repeated views of the same retained report.
    Equal priors and predeclared source laws for *fresh* copies only.
    """
    if type(n) is not int or n<0:raise ValueError('fresh-copy count')
    p=outcome_product_plus_probability(correct_model,which)**n
    q=outcome_product_plus_probability(wrong_model,which)**n
    return p/(p+q) if p+q else None

def suite_certificate(depth:int=2,omega:F|int=1):
    """Compact verified rational claims, not physical measurement."""
    g=gamma_phase(depth,omega)
    r=sector_state(g)
    return {'gamma':g,'haar_ZZ':joint_pauli(r,'Z','Z'),'haared_XX':joint_pauli(r,'X','X'),
            'haared_XY':joint_pauli(r,'X','Y'), 'bob':reduced_b(r),
            'b_after_X':nonselective_b(r,'X'),'chsh_sq':chsh_optimum_squared(g),
            'ppt_minor':ppt_negative_minor(g)}

def radix16_haar_parity(prefix:tuple[int,...],word:tuple[int,...])->int:
    """Normalized depth-|prefix| local radix-16 h=8 child-character wavelet.

    Normalized in L² of uniform base-16 cylinder measure. It is a single
    16-child Haar subband, not the full family of 15 subbands.
    """
    if type(prefix) is not tuple or type(word) is not tuple:
        raise ValueError('finite digit words must be tuples')
    if len(word)<=len(prefix):raise ValueError('at least one child digit required')
    if any(type(v) is not int or not 0<=v<16 for v in (*prefix,*word)):
        raise ValueError('valid digits 0..15 required')
    if word[:len(prefix)] != prefix:return 0
    return 4**len(prefix)*marked_digit_haar_parity(word[len(prefix)])

def uniform_haar_response(responses, *, prefix:tuple=()):
    """Source-average one-level Haar response from 16 *counterfactual* modes.

    Access to all modes is a model assumption; a single destructive copy
    does not authorize counterfactual simultaneous measurement.
    """
    if len(responses)!=16 or any(type(v) not in (int,F) or not 0<=v<=1 for v in responses):
        raise ValueError('one rational response probability per child')
    return sum((F(v)*radix16_haar_parity(prefix,prefix+(a,)) for a,v in enumerate(responses)),F(0))/16

def policy_haar_experiment(responses,policy,*,prefix:tuple=()):
    """Expectation of raw and propensity-corrected signed Haar reports.

    Draw a~policy (known prior history), then binary outcome with success
    probability responses[a]; HT estimator is psi(a)*Y/(16*policy[a]).
    If a policy assigns zero to any child, full Haar target NOT identified.
    """
    if len(policy)!=16 or any(type(v) not in (int,F) or v<=0 for v in policy) or sum(map(F,policy),F(0))!=1:
        raise ValueError('strictly positive normalized action probabilities')
    target=uniform_haar_response(responses,prefix=prefix)
    raw=sum((F(policy[a])*F(responses[a])*radix16_haar_parity(prefix,prefix+(a,)) for a in range(16)),F(0))
    adjusted=sum((F(policy[a])*F(responses[a])*radix16_haar_parity(prefix,prefix+(a,))/(16*F(policy[a])) for a in range(16)),F(0))
    assert adjusted==target
    return {'target':target,'raw_policy_weighted':raw,'propensity_corrected':adjusted}
