"""Source-marked SUCC quaternion gyroscope: exact frame groupoid and BBP phases.

Research only. Uses SUCC's MAIN pure-Fraction Hamilton H algebra; E2 remains a
Q(i)^2 SOURCE, not a quaternion ring. The gyro is a separate observer layer.
Exact: source/carries, rational quaternion frame transports, holonomy, spinor
parity. Trigonometric Bloch values are exploratory floats, not proof intervals.
No theorem here proves the selected real Weyl means tend to zero.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from math import cos, fsum, pi, sin
from observational_succ.hopf_source_exact import H, ONE, I, J, K

PASSPORT = 'original-four-signed-BBP-poles|U0=0|carrier-v1'
BASIS = (I,J,K)


def original_source(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError('source index must be positive integer')
    return (F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))


def original_states(n: int) -> list[F]:
    if type(n) is not int or n < 0:
        raise ValueError('horizon must be nonnegative integer')
    x = F(0)
    out=[x]
    for k in range(1,n+1):
        x=16*x+original_source(k)
        out.append(x)
    return out


def source_phase(u: F, h: int=1) -> F:
    if type(h) is not int or h==0:
        raise ValueError('nonzero integer Fourier frequency required')
    return (F(u)*h)%1


def spinor_lift(u: F, h: int=1) -> F:
    """Exact Spin(2) double-cover angle /pi modulo 2, not modulo 1."""
    if type(h) is not int or h==0:
        raise ValueError('nonzero integer Fourier frequency required')
    return (F(u)*h)%2


def spinor_carry_sign(h: int, carry: int) -> int:
    """e^(i*pi*h*(u+carry))=(-1)^(h*carry)e^(i*pi*h*u)."""
    if type(h) is not int or type(carry) is not int:
        raise ValueError('integer h, carry required')
    return (-1) if (h*carry)%2 else 1


def _unit(q: H) -> H:
    if not isinstance(q,H) or q.norm2()!=1:
        raise ValueError('quaternion source-frame rotation must have exact norm 1')
    return q


@dataclass(frozen=True)
class EFrame:
    name: str
    rotor: H
    passport: str = PASSPORT
    mark: F = F(0)

    def __post_init__(self):
        if not isinstance(self.name,str) or not self.name:
            raise ValueError('observer frame name required')
        _unit(self.rotor)
        object.__setattr__(self,'mark',F(self.mark))
        if self.passport!=PASSPORT or self.mark!=0:
            raise ValueError('source mismatch: original four poles and U0=0 required')


def link(start: EFrame, stop: EFrame) -> H:
    """Groupoid orientation: q_stop * q_start^-1, exact."""
    if start.passport!=stop.passport or start.mark!=stop.mark:
        raise ValueError('source-incompatible E frames')
    return _unit(stop.rotor*start.rotor.conj())


def rotate(q: H, v: H) -> H:
    """Conjugation (not left multiplication): rotates pure quaternion v."""
    _unit(q)
    if v.a != 0:
        raise ValueError('pure quaternion observable required')
    return q*v*q.conj()


def transport(v_start: H, start: EFrame, stop: EFrame) -> H:
    """Carry the same physical vector between two source-aligned frames."""
    return rotate(link(start,stop),v_start)


def rotation_matrix(q: H):
    """Exact 3x3 SO(3) matrix from a unit rational SU(2) rotor."""
    _unit(q)
    columns=[]
    for e in BASIS:
        x=rotate(q,e)
        columns.append((x.b,x.c,x.d))
    return tuple(tuple(columns[c][r] for c in range(3)) for r in range(3))


def spin_vector(angle: F, h: int=1):
    """Exploratory Bloch vector in common carrier, using rational phase mod1."""
    theta = 2*pi*float(source_phase(angle,h))
    return (cos(theta),sin(theta),0.)


def apply_rotor(q: H, vector):
    m=rotation_matrix(q)
    if len(vector)!=3:
        raise ValueError('three-vector required')
    return tuple(sum(m[row][col]*vector[col] for col in range(3))
                 for row in range(3))


def invert_rotor(q: H):
    return _unit(q).conj()


def source_phase_receipt(n: int, u: F, h: int=1) -> dict:
    """Exact frame-FREE commitment to original rational phase at index n.

    A reproducible source-consistency hash, NOT a cryptographic external
    attestation and NOT proof of normality.
    """
    if type(n) is not int or n<0:
        raise ValueError('nonnegative source index required')
    expected=original_states(n)[n]
    if F(u)!=expected:
        raise ValueError('phase does not match original zero-seeded BBP source')
    x=source_phase(u,h)
    text=f'{PASSPORT}|n={n}|h={h}|phase={x.numerator}/{x.denominator}'
    return {'n':n,'h':h,'fraction':x,'digest':sha256(text.encode()).hexdigest(),
            'passport':PASSPORT}


def coherent_mean(vectors):
    """Plain Bloch mean; inputs must have ALREADY been brought to common frame."""
    if not vectors:
        raise ValueError('nonempty vectors required')
    n=len(vectors)
    return tuple(fsum(float(v[j]) for v in vectors)/n for j in range(3))


def spin_purity(vectors):
    """Trace(rho²) for rho=(I+mean Bloch dot Pauli)/2."""
    m=coherent_mean(vectors)
    return (1+sum(v*v for v in m))/2


def common_frame_mean(phases, frames, h=1, reference=0):
    """Transport each time-local E measurement to one authenticated E frame."""
    if len(phases)!=len(frames) or not phases:
        raise ValueError('nonempty aligned phase/frame histories required')
    if not (0 <= reference < len(frames)):
        raise ValueError('reference frame index invalid')
    ref=frames[reference]
    vals=[]
    for u,fr in zip(phases,frames):
        # real-time local observation followed by exact H groupoid transport
        measured=apply_rotor(fr.rotor,spin_vector(u,h))
        vals.append(apply_rotor(link(fr,ref),measured))
    return coherent_mean(vals)


def gyro_energy(states,h=1,frames=None):
    """Generic Bloch norm², equal to |Weyl mean|²; FLOAT diagnostic only."""
    if not states:raise ValueError('nonempty selected source sequence')
    if frames is None:
        frames=[EFrame('common',ONE)]*len(states)
    m=common_frame_mean(states,frames,h)
    return sum(v*v for v in m)


def source_selected_gyro_energy(horizon,h=1,frames=None):
    """Authentic zero-seeded source prefix; phase values cannot be substituted."""
    if type(horizon) is not int or horizon<1:
        raise ValueError('positive original-source horizon required')
    return gyro_energy(original_states(horizon-1),h,frames)


def gram_difference_mod1(u: F,v: F,h=1):
    """Exact cyclotomic phase difference [h(u-v)] in R/Z; frame-free."""
    return source_phase(F(u)-F(v),h)


def gauge_holonomy(a: EFrame,b: EFrame,c: EFrame) -> H:
    """Transport a->b->c->a. An honest shared carrier MUST give 1."""
    return link(c,a)*link(b,c)*link(a,b)


def fake_frame_twirl_vector(v: H) -> H:
    """SOURCE-BLIND quaternion twirl: sends any pure vector to zero!"""
    if v.a!=0:raise ValueError('pure quaternion required')
    return (rotate(ONE,v)+rotate(I,v)+rotate(J,v)+rotate(K,v)).scale(F(1,4))


def exact_sector_imbalance(phases, h, mesh):
    """Exact rational SUCC #478 h-specific bin antiphase mismatch.

    This is source-exact for phases from original_states and remains an
    auxiliary finite arithmetic certificate, not asymptotic cancellation.
    """
    if not phases or type(h) is not int or h==0 or type(mesh) is not int or mesh<2 or mesh&(mesh-1):
        raise ValueError('nonempty phases, nonzero h, power-of-two mesh')
    w=abs(h);v=0
    while w%2==0:
        w//=2;v+=1
    if mesh<2**(v+1):raise ValueError('mesh too coarse for harmonic parity')
    counts=[0]*mesh
    for phase in phases:
        x=F(phase)%1
        counts[mesh*x.numerator//x.denominator]+=1
    t=mesh//2**(v+1)
    mis=sum(abs(counts[a+2*j*t]-counts[a+(2*j+1)*t])
            for a in range(t) for j in range(2**v))
    return F(mis,len(phases))


def exact_gyro_upper_bound(phases,h,mesh):
    """|c_N(h)| <= imbalance + (22/7)*|h|/mesh, rigorous rational bound.

    Uses original sector proof and elementary pi<22/7; bound can exceed 1.
    Caller must separately verify \`phases\` really come from U0=0.
    """
    return exact_sector_imbalance(phases,h,mesh)+F(22*abs(h),7*mesh)


def original_gamma_gyro_purity_error(n: int, h: int) -> F:
    """Rigorous source-specific |purity_U-purity_completed| < 561|h|/(392N).

    For N states n=0..N-1; uses T0=pi/16<11/56 and
    sum_{n>=1}T_n < (1/64)sum n^-2 < 1/32, pi<22/7.
    This is only a transport/error bound, not a decay certificate.
    """
    if type(n) is not int or n<1 or type(h) is not int or h==0:
        raise ValueError('positive horizon and nonzero integer harmonic required')
    return F(561*abs(h),392*n)


def gyro_fejer_excess(phases, mesh: int, frames=None) -> float:
    """(Fejer pair energy -1)/2 as SO(3)-invariant spin purities.

    For even mesh M>=2, use H=M/2-1 and weights (1-2h/M).
    Requires every time-local frame to be transported to the same reference.
    This is a float diagnostic; exact mathematics is in PROOFS.md.
    """
    if type(mesh) is not int or mesh<2 or mesh%2:
        raise ValueError('mesh must be even >=2')
    return fsum((1-F(2*h,mesh))*gyro_energy(phases,h,frames)
                for h in range(1,mesh//2))


def exact_histogram_fejer_majorant(phases,mesh: int):
    """Fully rational upper certificate for mesh Fejer energy from #475.

    Q_(N,mesh)<= (3/2+pi²/6)* E, with E=mesh/N² Σcount².
    Replace pi² by (22/7)²; then gyro_fejer_excess<=(Qupper-1)/2.
    May be an unhelpfully large finite bound; does NOT prove asymptotics.
    """
    if not phases or type(mesh) is not int or mesh<2 or mesh%2:
        raise ValueError('nonempty phases and even mesh>=2 required')
    counts=[0]*mesh
    for phase in phases:
        x=F(phase)%1
        counts[mesh*x.numerator//x.denominator]+=1
    n=len(phases)
    E=F(mesh*sum(c*c for c in counts),n*n)
    upper=(F(3,2)+F(22,7)**2/6)*E
    return {'E_exact':E,'Q_upper':upper,'gyro_excess_upper':(upper-1)/2,
            'n':n,'mesh':mesh,'counts':counts}


@dataclass(frozen=True)
class LinkReceipt:
    """Source-marked exact Spin(3) transport, NOT cryptographic attestation."""
    start: str
    stop: str
    rotor: H
    passport: str=PASSPORT
    mark: F=F(0)

    def __post_init__(self):
        if not self.start or not self.stop:
            raise ValueError('nonempty source and target observers required')
        _unit(self.rotor)
        object.__setattr__(self,'mark',F(self.mark))
        if self.passport!=PASSPORT or self.mark!=0:
            raise ValueError('mismatched original source and zero seed')


def emit_link(a:EFrame,b:EFrame) -> LinkReceipt:
    return LinkReceipt(a.name,b.name,link(a,b),a.passport,a.mark)


def relay_triangle(ab:LinkReceipt,bc:LinkReceipt,ca:LinkReceipt,
                   require_spin:bool=True) -> H:
    """Verify E_A->E_B->E_C->E_A typed source-loop completion.

    A -1 loop is an SO(3)-closed path but NOT an SU(2)-closed lift.
    If exact spin lift is required it must be rejected, not silently reset.
    """
    if (ab.stop!=bc.start or bc.stop!=ca.start or ca.stop!=ab.start
            or len({ab.passport,bc.passport,ca.passport})!=1
            or any(z.mark!=0 for z in (ab,bc,ca))):
        raise ValueError('invalid signed E-tower relay/source overlap')
    hol=ca.rotor*bc.rotor*ab.rotor
    if require_spin:
        if hol!=ONE:raise ValueError('nontrivial SU2 spinor holonomy')
    else:
        if hol not in (ONE,-ONE):
            raise ValueError('nontrivial SO3 frame holonomy')
    return hol


@dataclass(frozen=True)
class Spin2Mark:
    """Exact formal root of unity exp(pi*i*a), a in Q/(2Z).

    Does NOT evaluate cos/sin. Center \`a=1\` is -1, invisible in Bloch SO3.
    Original BBP U_n are rational, so every mark is a finite root of unity.
    """
    angle: F

    def __post_init__(self):
        object.__setattr__(self,'angle',F(self.angle)%2)

    def __mul__(self,other):
        if not isinstance(other,Spin2Mark):return NotImplemented
        return Spin2Mark(self.angle+other.angle)

    def inverse(self):return Spin2Mark(-self.angle)

    def commutator(self,other):
        return self*other*self.inverse()*other.inverse()

    def bloch_phase(self):return self.angle%1


def original_spin2_mark(n: int,h: int=1) -> Spin2Mark:
    if type(h) is not int or h==0 or type(n) is not int or n<0:
        raise ValueError('original source index and nonzero integer h required')
    return Spin2Mark(h*original_states(n)[n])


def e_network_consensus(vertices, relays, root=None, *, require_spin=True):
    """Nonabelian SU2 frame-gluing test over a connected finite E relay graph.

    All edge transports are already declared source-marked LinkReceipts.
    Returns unit-quaternion frames q_v relative to the selected root's q=1.
    Frame gluing is possible iff every closed cycle has holonomy 1.
    With require_spin=False, the center +/-1 is identified (SO3), thereby
    losing the source's spinor carry parity. This is a *certificate check*,
    not evidence that E relays are physically authenticated or pi mixes.
    """
    names=tuple(vertices)
    if not names or len(set(names))!=len(names):
        raise ValueError('distinct nonempty common-carrier E nodes required')
    start=names[0] if root is None else root
    if start not in names:
        raise ValueError('root must be in E network')
    edges={n:[] for n in names}
    for r in relays:
        if not isinstance(r,LinkReceipt):
            raise ValueError('only source-marked quaternion relay accepted')
        if r.start not in edges or r.stop not in edges:
            raise ValueError('relay endpoint not in named E network')
        edges[r.start].append((r.stop,r.rotor))
        edges[r.stop].append((r.start,r.rotor.conj()))
    recovered={start:ONE}
    queue=[start]
    for node in queue:
        for target,edge in edges[node]:
            candidate=edge*recovered[node]
            if target not in recovered:
                recovered[target]=candidate
                queue.append(target)
            elif candidate!=recovered[target]:
                if require_spin or candidate!=-recovered[target]:
                    raise ValueError('inconsistent nonabelian E frame holonomy')
    if len(recovered)!=len(names):
        raise ValueError('source frame relay cover disconnected')
    return recovered
