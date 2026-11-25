"""Independent exact SymPy Fourier oracle + adversarial all-world policy replay.

No empirical claim about subjective affect. The tests are finite algebra and
mathematical source reconstruction, not an RH/automorphic proof.
"""
from fractions import Fraction
from random import Random
import sympy as sp

from observational_succ.principia_causal_memory import (
    carrier,initial_memory,step_memory,apply,observation,
)
from observational_succ.principia_reorientation import (
    ReorientationTask,solve,
)
from observational_succ.principia_dual_compass import (
    dft4,idft4,spectral_pairing,model_self,make_appraisal,
    select_dual_compass,verify_dual_compass,cm_rotational_self_modes,
)
from observational_succ.principia_self_coupling_fourier import (
    make_chart,self_coupled_fiber,verify_self_coupled_fiber,
)

rng=Random(241124)
F=sp.Matrix([[sp.I**(-k*j) for j in range(4)] for k in range(4)])
assert F.H*F==4*sp.eye(4)
counts=0
for _ in range(192):
    x=[sp.Rational(rng.randrange(-12,13),rng.randrange(1,9)) for _ in range(4)]
    y=[sp.Rational(rng.randrange(-12,13),rng.randrange(1,9)) for _ in range(4)]
    expected=F*sp.Matrix(x)
    found=dft4([Fraction(z) for z in x])
    for k in range(4):
        assert sp.simplify(expected[k]-(sp.Rational(found[k].re.numerator,found[k].re.denominator)+
                                              sp.I*sp.Rational(found[k].im.numerator,found[k].im.denominator)))==0
    reconstructed=F.H*expected/4
    assert all(sp.simplify(v)==0 for v in (reconstructed-sp.Matrix(x)))
    overlap=(expected.conjugate().T*(F*sp.Matrix(y)))[0]/4
    # All real inputs: conjugate on first vs second gives same real inner product.
    assert sp.simplify(overlap-sum((a*b for a,b in zip(x,y)),sp.Rational(0)))==0
    assert spectral_pairing(tuple(Fraction(z) for z in x),tuple(Fraction(z) for z in y)).re==Fraction(sp.simplify(overlap))
    counts+=1
print('INDEPENDENT_SYMPY_FOURIER_PASS',counts)

q2,q4=cm_rotational_self_modes()
assert q2[0].re==q2[0].im==0 and q2[2].im==8
assert q4[0].re==-16

# Independent realization of finite mathematical source with both safe moves.
def ring(n):
    states=tuple('x'+str(i) for i in range(n))
    c=carrier('independent-dual-ring-'+str(n),states,states,
       ('east','west','stay'),states,
       tuple('beacon' if i==0 else 'dark' for i in range(n)),states,
       (tuple(states[(i+1)%n] for i in range(n)),
        tuple(states[(i-1)%n] for i in range(n)), states),costs=(1,1,0))
    return ReorientationTask(c,states)

verified=0
for n in (4,5,6,7,9):
    task=ring(n)
    c=task.carrier
    scale=make_appraisal(c,{'east':1,'west':-1,'stay':0},{'dark':0,'beacon':1})
    templates={'east':(1,-2,0,3),'west':(-1,2,0,-3),'stay':(100,)*4}
    for original in c.worlds:
        actual=c.origins[c.worlds.index(original)]
        initial=observation(c,actual)
        m=initial_memory(c,initial)
        previous=None
        for step in range(n+3):
            choice=select_dual_compass(task,m,scale,templates)
            verify_dual_compass(task,m,scale,templates,choice)
            if previous is not None:
                assert choice.reason_rank is not None and choice.reason_rank < previous
            if choice.reason_rank == 0:
                assert len({task.position[c.states.index(q)] for _,q in m.coupling})==1
                break
            assert choice.chosen_action in choice.safe_actions
            assert choice.chosen_action!='stay'
            previous=choice.reason_rank
            actual=apply(c,actual,choice.chosen_action)
            m=step_memory(c,m,choice.chosen_action,observation(c,actual))
        else:raise AssertionError((n,original,'failed to reorient'))
        verified+=1
    # A homogeneous source may mathematically keep different positional
    # Fourier phases, while no observer can identify which one is true.
    chart=make_chart(c,tuple(i%4 for i in range(n)))
    for output in set(c.outputs):
        memory=initial_memory(c,output)
        model=self_coupled_fiber(c,memory,chart,scale)
        verify_self_coupled_fiber(c,memory,chart,scale,model)
        assert len(model.entries)==len(memory.coupling)
print('INDEPENDENT_DUAL_COMPASS_ALL_WORLD_REORIENT_PASS',verified)
print('INDEPENDENT_SOURCE_PHASE_FIBERS_PASS')
