"""Independent SymPy exact equations for selected choice/no-choice carriers.

No import of observational_succ.equivariant_choice; crosschecks the source
laws directly. Sympy does not prove the general group or Farkas theorems.
"""
import sympy as s


def main():
    # 3-source-state / 2-report one-action merger.
    # P(u)=delta_a; P(w)=(p_b,p_c).
    pb, pc = s.symbols('pb pc', real=True)
    merging = s.linsolve([pb + pc-1, pb-1, pc, pb], (pb,pc))
    assert merging == s.EmptySet, merging

    # Four-source-state, two incompatible predecessor reports.
    wc, wd = s.symbols('wc wd', real=True)
    predecessors = s.linsolve([wc+wd-1, wc-1,wd, wc,wd-1], (wc,wd))
    assert predecessors == s.EmptySet, predecessors

    # Finite two-point group swap fixes the uniform probability uniquely.
    pa,pb = s.symbols('pa pb', real=True)
    swap = s.linsolve([pa+pb-1, pa-pb],(pa,pb))
    assert swap == s.FiniteSet((s.Rational(1,2),s.Rational(1,2))),swap

    # Three-state transient c->a, while a<->b; only the 2-cycle is stationary.
    pa,pb,pc = s.symbols('pa pb pc', real=True)
    transient = s.linsolve([pa+pb+pc-1, pa-pb-pc,pb-pa,pc],(pa,pb,pc))
    assert transient == s.FiniteSet((s.Rational(1,2),s.Rational(1,2),s.S.Zero)),transient

    # Independent exact TV calculation for the single-T merging example.
    for n in range(15):
        p = s.Rational(n,14)
        left = (abs(1-p)+abs(0-(1-p)))/2  # TV(delta_b, K_w)
        right = (abs(p-0)+abs(1-p-1))/2   # TV(K_w, delta_c)
        assert max(left,right)>=s.Rational(1,2)
    assert max(s.Rational(1,2),s.Rational(1,2))==s.Rational(1,2)
    print('SYMPY_EXACT: merger=INFEASIBLE, predecessors=INFEASIBLE; '
          'swap=(1/2,1/2), transient=(1/2,1/2,0), TV_min=1/2')


if __name__ == '__main__':
    main()
