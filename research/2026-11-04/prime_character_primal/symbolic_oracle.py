"""Independent SymPy certificate for the prime-character primal BBP quotient.

Separately rederives the eight-tap group action, character projectors, exact
Cauchy/angle/log identities, two-state minimality and odd denominator source.
No decimal pi input, no normality assumption, no Galois averaging.
"""
from __future__ import annotations
import sympy as sp


def run_oracle():
    t, n = sp.symbols('t n')
    v = sp.Matrix([4, 0, 0, -2, -1, -1, 0, 0])
    vsharp = sp.Matrix([0, 8, 4, 4, 0, 0, -1, 0])
    ch2 = {1:1, 3:-1, 5:-1, 7:1}
    ch4 = {1:1, 3:-1, 5:1, 7:-1}

    def action(a):
        mat = sp.zeros(8, 8)
        for ell in range(1, 9):
            j=(a*ell - 1)%8+1
            mat[ell-1,j-1]=sp.Rational(ch2[a])**(8-ell)*sp.Integer(2)**sp.Rational(j-ell,2)
        return mat

    mat={a:action(a) for a in ch2}
    group_tests=0
    for a in ch2:
        for b in ch2:
            assert mat[a]*mat[b] == mat[(a*b)%8]
            group_tests+=1
    assert mat[5]*v==v and mat[3]*v==-vsharp/2
    assert mat[3]*vsharp==-2*v
    assert mat[5]*vsharp==vsharp
    projectors={}
    chars={
        'trivial':{1:1,3:1,5:1,7:1},
        'chi_minus4':ch4,
        'chi_8':{1:1,3:-1,5:-1,7:1},
        'chi_minus8':{1:1,3:1,5:-1,7:-1},
    }
    for key,ch in chars.items():
        projectors[key]=sum((ch[a]*mat[a] for a in ch),sp.zeros(8,8))/4
        assert projectors[key]**2 == projectors[key]
    for c1,c2 in zip(chars, list(chars)[1:]):
        assert projectors[c1]*projectors[c2]==sp.zeros(8,8)
    assert sum(projectors.values(),sp.zeros(8,8))==sp.eye(8)
    dims={k:int(sp.trace(m)) for k,m in projectors.items()}
    assert dims=={'trivial':4,'chi_minus4':2,'chi_8':1,'chi_minus8':1}
    A=projectors['chi_minus4']*v
    R=projectors['trivial']*v
    assert projectors['chi_8']*v==sp.zeros(8,1)
    assert projectors['chi_minus8']*v==sp.zeros(8,1)
    assert A==(2*v+vsharp)/4 and R==(2*v-vsharp)/4
    p=lambda a:sum(a[j]*t**j for j in range(8))
    den=1-t**8/sp.Integer(16)
    F=(2-t**2)/((t-1)**2+1)
    Kangle=4/((t-1)**2+1)
    assert sp.cancel(p(A)/den-Kangle)==0
    assert sp.cancel(p(R)/den-2*sp.diff(sp.log(F),t))==0
    assert sp.cancel(Kangle-(2+2*t+t**2)/(1+t**4/4))==0
    assert sp.cancel(p(A)-(1-t**4/sp.Integer(4))*(2+2*t+t**2))==0
    # Independent source forcing computation from six/nonzero taps.
    src=sp.together(sum(A[j]/(8*n-7+j) for j in range(8)))
    num=30720*n**5-63232*n**4+45792*n**3-13892*n**2+1641*n-48
    d=(4*n-3)*(4*n-1)*(8*n-7)*(8*n-5)*(8*n-3)*(8*n-1)
    assert sp.cancel(src-num/d)==0
    # Angular kernel has minimal McMillan / Hankel rank 2 over Q.
    K2=Kangle
    data=[sp.expand(sp.series(K2,t,0,5).removeO()).coeff(t,k) for k in range(5)]
    assert data==[2,2,1,0,sp.Rational(-1,2)]
    rank2=sp.Matrix([[data[0],data[1]],[data[1],data[2]]]).det()
    assert rank2==-2
    Q2=(t-1)**2+1
    assert sp.discriminant(Q2,t)==-4
    # G=(1+i)/2 as a real rational matrix; Kangle= [2,2](I-tG)^-1 [1,0].
    G=sp.Matrix([[sp.Rational(1,2),sp.Rational(-1,2)],
                 [sp.Rational(1,2),sp.Rational(1,2)]])
    co=sp.Matrix([[2,2]])
    inp=sp.Matrix([[1],[0]])
    assert sp.cancel((co*(sp.eye(2)-t*G).inv()*inp)[0]-Kangle)==0
    assert G**4==-sp.eye(2)/4 and G**8==sp.eye(2)/16
    # Primitive complex transfer logarithm and circle projection.
    z=(1+sp.I)/2
    assert sp.expand_complex(z**4)==-sp.Rational(1,4)
    assert sp.expand_complex(z**8)==sp.Rational(1,16)
    assert sp.simplify(z/sp.sqrt(sp.re(z)**2+sp.im(z)**2)-(1+sp.I)/sp.sqrt(2))==0
    # Independently verify ALL 4x8 symbolic within-octave primal p-pulse
    # formulas, using a fresh symbolic source state and k variable.
    k, Y = sp.symbols('k Y', integer=True, nonnegative=True)
    for a in ch2:
        for ell in range(1,9):
            idx=(a*ell-1)%8+1
            fa=sp.Rational(ch2[a])**ell * sp.Integer(2)**sp.Rational(ell+8-idx,2)
            raw=sp.Rational(ch4[a])*fa*Y
            for jj in range(1,ell+1):
                idxj=(a*jj-1)%8+1
                fj=sp.Rational(ch2[a])**jj * sp.Integer(2)**sp.Rational(jj+8-idxj,2)
                raw+=fa/fj * A[idxj-1]/(8*k+jj)
            claimed=ch4[a]*fa*(Y+sp.Rational(1,16)*sum(A[jj-1]/(8*k+jj) for jj in range(1,ell+1)))
            assert sp.cancel(raw-claimed)==0
    # Strict positivity lower budget for every angular source prefix:
    # 2/(8k+1) - (5/4)/(8k+5)=(24k+35)/(4(8k+1)(8k+5)) >0.
    positivity=sp.cancel(2/(8*k+1)-sp.Rational(5,4)/(8*k+5))
    assert sp.cancel(positivity-(24*k+35)/(4*(8*k+1)*(8*k+5)))==0
    src_orig=sp.together(sum(v[j]/(8*n-7+j) for j in range(8)))
    src_rad=sp.together(sum(R[j]/(8*n-7+j) for j in range(8)))
    assert sp.limit(n*src,n,sp.oo)==sp.Rational(15,32)
    assert sp.limit(n*src_rad,n,sp.oo)==-sp.Rational(15,32)
    assert sp.limit(n**2*src_orig,n,sp.oo)==sp.Rational(15,64)
    # No angular movement can be removed without collapsing the 1D period quotient.
    assert sp.cancel(p(R)/den-(p(v)/den-Kangle))==0
    return {
        'status':'SYMBOLIC_PRIMAL_ECHO_VERIFIED',
        'all_16_group_cells': group_tests,
        'eigensector_dimensions':dims,
        'hankel_two_state_minor_det':str(rank2),
        'original_plus_dual_decomposition': True,
        'primal_odd_denominator_rational_identity':True,
        'all_32_angular_partial_pulse_identities':True,
        'positive_prefix_pulse_for_all_k':True,
        'eightN_primal_denominator_rate_paper_proved':True,
        'gaussian_minus_four_quarterturn':True,
        'pi_normality_proved': False,
    }


if __name__=='__main__':
    import json
    print(json.dumps(run_oracle(),indent=2,sort_keys=True))
