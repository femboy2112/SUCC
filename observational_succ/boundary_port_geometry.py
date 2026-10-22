"""Exact boundary-port completion for anchored finite resistor networks.

Research-only rational source model. A fixed finite family of candidate edge ports
is sufficient to transport all fixed positive conductance additions without
reconstructing the original interior Laplacian. This is classical Schur/Woodbury
algebra, not physical plasma electrodynamics or an identifiability claim.

Provenance: extends SUCC HISTORY-DTN #237 / source histories #239 without
editing their imported or historical files. No empirical source is authenticated.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q


class PortSourceError(ValueError):
    """Invalid rational source, contact graph, or incomplete inverse witness."""


def rat(x):
    if type(x) not in (int, Q):
        raise PortSourceError("Only exact integers or Fraction, never float/bool")
    return Q(x)


def matrix(A):
    return tuple(tuple(rat(z) for z in row) for row in A)


def inverse(A):
    """Independent exact Gauss-Jordan grounded inverse."""
    n = len(A)
    if not n or any(len(row) != n for row in A):
        raise PortSourceError("Square grounded matrix required")
    M = [[rat(A[i][j]) for j in range(n)] + [Q(int(i == j)) for j in range(n)]
         for i in range(n)]
    for k in range(n):
        pivot = next((r for r in range(k, n) if M[r][k]), None)
        if pivot is None:
            raise PortSourceError("Interior not connected to grounded boundary")
        M[k], M[pivot] = M[pivot], M[k]
        t = M[k][k]
        M[k] = [v/t for v in M[k]]
        for i in range(n):
            if i == k:
                continue
            t = M[i][k]
            M[i] = [x-t*y for x, y in zip(M[i], M[k])]
    return matrix(row[n:] for row in M)


def mm(A, B):
    if not A or not B or len(A[0]) != len(B):
        raise PortSourceError("Incompatible matrix shapes")
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))), Q())
                       for j in range(len(B[0]))) for i in range(len(A)))


def tr(A):
    return tuple(tuple(row[j] for row in A) for j in range(len(A[0])))


def dot(v, w):
    return sum((a*b for a, b in zip(v, w)), Q())


def zero(n, m):
    return tuple(tuple(Q() for _ in range(m)) for _ in range(n))


@dataclass(frozen=True)
class Network:
    vertices: tuple[str, ...]
    boundary: tuple[str, ...]
    edges: tuple[tuple[str, str, Q], ...]

    def __post_init__(self):
        if (not self.vertices or len(self.vertices) != len(set(self.vertices))
                or not self.boundary or len(self.boundary) != len(set(self.boundary))
                or not set(self.boundary) <= set(self.vertices)):
            raise PortSourceError("Distinct labeled vertices and nonempty boundary needed")
        for a,b,g in self.edges:
            if a not in self.vertices or b not in self.vertices or a == b or rat(g) <= 0:
                raise PortSourceError("Positive non-loop conductance, known vertices")
        if self.interior:
            inverse(self._parts()[2])

    @property
    def interior(self):
        return tuple(v for v in self.vertices if v not in self.boundary)

    def laplacian(self):
        n = len(self.vertices)
        L = [[Q() for _ in range(n)] for _ in range(n)]
        pos = {v:i for i,v in enumerate(self.vertices)}
        for a,b,c in self.edges:
            i,j,g = pos[a],pos[b],rat(c)
            L[i][i] += g; L[j][j] += g
            L[i][j] -= g; L[j][i] -= g
        return matrix(L)

    def _parts(self):
        L = self.laplacian()
        B = tuple(self.vertices.index(v) for v in self.boundary)
        I = tuple(self.vertices.index(v) for v in self.interior)
        Lbb = matrix(tuple(L[i][j] for j in B) for i in B)
        Lbi = matrix(tuple(L[i][j] for j in I) for i in B)
        A = matrix(tuple(L[i][j] for j in I) for i in I)
        return Lbb,Lbi,A

    def dt_n(self):
        Lbb,Lbi,A = self._parts()
        if not self.interior:
            return Lbb
        P = mm(mm(Lbi,inverse(A)),tr(Lbi))
        return matrix(tuple(Lbb[i][j]-P[i][j] for j in range(len(Lbb))) for i in range(len(Lbb)))

    def add(self, port: tuple[str,str], strength):
        if len(port) != 2 or port[0] == port[1] or any(v not in self.vertices for v in port):
            raise PortSourceError("Port is a distinct oriented pair on the source")
        g=rat(strength)
        if g <= 0:
            raise PortSourceError("Only strictly positive increments supported")
        return Network(self.vertices,self.boundary,self.edges+((port[0],port[1],g),))


@dataclass(frozen=True)
class PortFrame:
    """The finite source-dependent response jet (Lambda,W,R) on fixed ports.

    Lambda: BxB DtN. W: BxM voltage-drop port coefficients.
    R: MxM grounded interior Green Gram matrix. W and R are INTERNAL
    completion data, not automatically measurable boundary quantities.
    """
    boundary: tuple[str,...]
    ports: tuple[tuple[str,str],...]
    Lambda: tuple[tuple[Q,...],...]
    W: tuple[tuple[Q,...],...]
    R: tuple[tuple[Q,...],...]

    @classmethod
    def from_network(cls, net:Network, ports:tuple[tuple[str,str],...]):
        if not ports or any(len(p)!=2 or p[0]==p[1] or any(v not in net.vertices for v in p) for p in ports):
            raise PortSourceError("At least one genuine fixed labeled edge port required")
        B,I = net.boundary,net.interior
        nb,ni,m=len(B),len(I),len(ports)
        Lbb,Lbi,A = net._parts()
        Qinv=inverse(A) if ni else ()
        inc_B=tuple(tuple(Q(int(v==a)-int(v==b)) for a,b in ports) for v in B)
        inc_I=tuple(tuple(Q(int(v==a)-int(v==b)) for a,b in ports) for v in I)
        if ni:
            X=mm(Qinv,inc_I)
            W=matrix(tuple(inc_B[i][j]-sum((Lbi[i][k]*X[k][j] for k in range(ni)),Q())
                           for j in range(m)) for i in range(nb))
            R=mm(tr(inc_I),X)
        else:
            W=inc_B; R=zero(m,m)
        return cls(B,ports,net.dt_n(),W,R)

    def update(self, idx:int, strength):
        if type(idx) is not int or not 0<=idx<len(self.ports):
            raise PortSourceError("Fixed source port index required")
        g=rat(strength)
        if g<=0:
            raise PortSourceError("Positive increment required")
        m=len(self.ports); nb=len(self.boundary)
        r=self.R[idx][idx]
        denom=1+g*r
        if denom<=0:
            raise PortSourceError("Port update lost positive anchored source")
        c=g/denom
        col=tuple(self.W[i][idx] for i in range(nb))
        Lambda=matrix(tuple(self.Lambda[i][j]+c*col[i]*col[j] for j in range(nb)) for i in range(nb))
        W=matrix(tuple(self.W[i][j]-c*col[i]*self.R[idx][j] for j in range(m)) for i in range(nb))
        R=matrix(tuple(self.R[i][j]-c*self.R[i][idx]*self.R[idx][j] for j in range(m)) for i in range(m))
        return PortFrame(self.boundary,self.ports,Lambda,W,R)

    def reverse_recorded_update(self, idx:int, strength):
        """Algebraic reverse of a KNOWN source event, not reverse physical time.

        Only a labelled event with known original positive increment g has a
        determined inverse on its attainable image. Given the final port jet,
        the backward Woodbury coefficient is -g/(1-g*Rprime[e,e]).
        No reconstruction is licensed from Lambda alone or without the log.
        """
        if type(idx) is not int or not 0<=idx<len(self.ports):
            raise PortSourceError("Recorded source event index required")
        g=rat(strength)
        if g<=0:
            raise PortSourceError("Recorded positive source increment required")
        den=1-g*self.R[idx][idx]
        if den<=0:
            raise PortSourceError("Reverse candidate violates grounded positivity")
        c=-g/den
        m=len(self.ports);nb=len(self.boundary)
        col=tuple(self.W[i][idx] for i in range(nb))
        Lambda=matrix(tuple(self.Lambda[i][j]+c*col[i]*col[j] for j in range(nb)) for i in range(nb))
        W=matrix(tuple(self.W[i][j]-c*col[i]*self.R[idx][j] for j in range(m)) for i in range(nb))
        R=matrix(tuple(self.R[i][j]-c*self.R[i][idx]*self.R[idx][j] for j in range(m)) for i in range(m))
        return PortFrame(self.boundary,self.ports,Lambda,W,R)

    def reorient(self, index:int):
        """Reverse one port; Lambda invariant, oriented internal signatures conjugate."""
        if type(index) is not int or not 0<=index<len(self.ports):
            raise PortSourceError("Fixed source port index required")
        s=tuple(-1 if i==index else 1 for i in range(len(self.ports)))
        ports=tuple((b,a) if i==index else (a,b) for i,(a,b) in enumerate(self.ports))
        W=matrix(tuple(v*s[j] for j,v in enumerate(row)) for row in self.W)
        R=matrix(tuple(v*s[i]*s[j] for j,v in enumerate(row)) for i,row in enumerate(self.R))
        return PortFrame(self.boundary,ports,self.Lambda,W,R)


def diamond(g=0):
    g=rat(g)
    if g<0:
        raise PortSourceError("Nonnegative hidden bridge allowed")
    edges=(("L","u",Q(1)),("u","R",Q(1)),("L","v",Q(1)),("v","R",Q(1)))
    if g:
        edges+=("u","v",g),
    return Network(("L","R","u","v"),("L","R"),edges)


def diamond_contact_response(a,g):
    """Exact two-terminal effective conductance after known L-u addition."""
    a,g=rat(a),rat(g)
    if a<0 or g<0:
        raise PortSourceError("Nonnegative intervention and hidden bridge")
    return ((2*a+4)*g+3*a+4)/((a+4)*g+2*a+4)


def diamond_bridge_inverse(a,C):
    """One active contact response reconstructs hidden bridge g, IF family known."""
    a,C=rat(a),rat(C)
    if a<=0:
        raise PortSourceError("Zero contact does not identify hidden bridge")
    den=(a+4)*C-(2*a+4)
    if not den:
        raise PortSourceError("Unbounded bridge limit, not a finite source witness")
    g=((3*a+4)-(2*a+4)*C)/den
    if g<0 or diamond_contact_response(a,g)!=C:
        raise PortSourceError("Response outside declared nonnegative-bridge family")
    return g


def two_contact_gain_inverse(g1,d1,g2,d2):
    """Two reset contact strengths identify A=(w.f)^2 and r, if A>0."""
    g1,d1,g2,d2=map(rat,(g1,d1,g2,d2))
    if not (g1>0 and g2>0 and g1!=g2 and d1>0 and d2>0):
        raise PortSourceError("Two distinct positive strengths and nonzero gains needed")
    y1,y2=g1/d1,g2/d2
    slope=(y2-y1)/(g2-g1)
    intercept=y1-slope*g1
    if intercept<=0 or slope<0:
        raise PortSourceError("Not a passive rank-one contact response")
    A=1/intercept
    r=slope/intercept
    if any((g*A/(1+g*r)!=d for g,d in ((g1,d1),(g2,d2)))):
        raise PortSourceError("Invalid fit")
    return (A,r)


def action_descent(states,observations,actions):
    """The observed action descends iff observation equality is a congruence.

    Returns (transition_on_observation, None) or (None, typed obstruction).
    Source event labels are NOT inferred from coincidental observed endpoints.
    """
    if len(states)!=len(set(states)) or not states or set(observations)!=set(states):
        raise PortSourceError("Distinct states and complete typed observations required")
    if not actions or any(set(row)!=set(states) or any(y not in states for y in row.values()) for row in actions.values()):
        raise PortSourceError("Every authorized action must be total on declared states")
    induced={}
    for label,T in sorted(actions.items()):
        for x in states:
            key=(label,observations[x]); val=observations[T[x]]
            if key in induced and induced[key]!=val:
                witness=next(z for z in states if observations[z]==observations[x]
                             and observations[T[z]]==induced[key])
                return None,(label,witness,x,induced[key],val)
            induced[key]=val
    return induced,None


def future_safe_partition(states,observations,actions):
    """Finite Moore/source-fiber refinement, including empty word.

    Iterates until stable. Class identifiers use deterministic source order;
    no claim of physically complete sensor provenance is implied.
    """
    if (not states or len(states)!=len(set(states)) or set(states)!=set(observations)
            or not actions or any(set(row)!=set(states) or any(y not in states for y in row.values()) for row in actions.values())):
        raise PortSourceError("Finite total deterministic source required")
    def rank(inputs):
        ids={}; out={}
        for state in states:
            key=inputs[state]
            if key not in ids:ids[key]=len(ids)
            out[state]=ids[key]
        return out
    cls=rank(observations)
    history=[cls]
    while True:
        nxt=rank({x:(cls[x],tuple((a,cls[T[x]]) for a,T in sorted(actions.items()))) for x in states})
        if nxt==cls:
            break
        cls=nxt;history.append(cls)
        if len(history)>len(states):
            raise ArithmeticError("Finite partition refinement failed to terminate")
    return {"classes":cls,"rounds":len(history)-1,"history":tuple(history),
            "minimal_observable_state_count":len(set(cls.values()))}


def hidden_contact_defect(frame:PortFrame, hidden:int, contact:int, z, a):
    """Exact matrix defect: invisible source edge z then visible contact a.

    Requires w_hidden=0 on ALL boundary drives. Return exact difference
    between (hidden then contact) and (contact alone); not a wave/retardation.
    At small z,a its first nonzero possible monomial is z*a^2, coefficient
    R[hidden,contact]^2 * outer(w_contact,w_contact).
    """
    if any(v for v in (frame.W[i][hidden] for i in range(len(frame.boundary)))):
        raise PortSourceError("Hidden port must be boundary-invisible at baseline")
    if hidden==contact:
        raise PortSourceError("Two distinct source interventions required")
    z,a=rat(z),rat(a)
    if z<=0 or a<=0:
        raise PortSourceError("Positive experimental increments only")
    before=frame.update(contact,a).Lambda
    after=frame.update(hidden,z).update(contact,a).Lambda
    q=frame.R[hidden][contact]
    r=frame.R[contact][contact]
    s=frame.R[hidden][hidden]
    d=1+z*s
    rp=r-z*q*q/d
    coefficient=a*a*z*q*q/(d*(1+a*r)*(1+a*rp))
    expect=tuple(tuple(coefficient*frame.W[i][contact]*frame.W[j][contact]
                       for j in range(len(frame.boundary)))
                 for i in range(len(frame.boundary)))
    observed=tuple(tuple(after[i][j]-before[i][j] for j in range(len(frame.boundary)))
                   for i in range(len(frame.boundary)))
    if observed!=expect:
        raise ArithmeticError("Hidden source / mixed susceptibility transport failed")
    third=tuple(tuple(2*q*q*frame.W[i][contact]*frame.W[j][contact]
                      for j in range(len(frame.boundary)))
                for i in range(len(frame.boundary)))
    return {"observed_exact_defect":observed,"source_formula":expect,
            "cubic_coefficient":tuple(tuple(q*q*frame.W[i][contact]*frame.W[j][contact]
                                             for j in range(len(frame.boundary)))
                                      for i in range(len(frame.boundary))),
            "mixed_third_derivative_at_zero":third,
            "first_hidden_variation_at_zero":zero(len(frame.boundary),len(frame.boundary)),
            "mixed_second_at_zero":zero(len(frame.boundary),len(frame.boundary)),
            "physical_wake_or_Cherenkov_proved":False}
