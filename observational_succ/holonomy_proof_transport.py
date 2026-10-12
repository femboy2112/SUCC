"""Exact two-path GF(2)^2 proof transport with declared nonflat holonomy.

A source vector is transported by invertible LOCAL frame maps around a
two-dimensional square. The two routes have identical endpoint coordinate
location but may produce different mathematical coordinates. A path-specific
inverse always exists; a single path-blind decoder exists for a claimed
predicate iff the predicate is invariant under the DECLARED relative
holonomy. Matrices and orientation are explicit; this is NOT quantum phase,
complex holonomy, curved physical space or RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product


class FrameTransportError(ValueError):
    """Invalid matrix, vector, path or source-relative target."""


BitVector = tuple[int,int]
ALL_VECTORS: tuple[BitVector, ...] = ((0,0),(0,1),(1,0),(1,1))


def _bit(x:int) -> int:
    if type(x) is not int or x not in (0,1):
        raise FrameTransportError("Require an exact GF(2) bit")
    return x


def _vec(v:BitVector) -> BitVector:
    if type(v) is not tuple or len(v)!=2:
        raise FrameTransportError("Require 2-vector over GF(2)")
    return (_bit(v[0]),_bit(v[1]))


@dataclass(frozen=True)
class GL2:
    """Invertible 2x2 matrix over GF(2), row-major."""
    a:int
    b:int
    c:int
    d:int

    def __post_init__(self) -> None:
        for x in (self.a,self.b,self.c,self.d):
            _bit(x)
        if (self.a*self.d+self.b*self.c)%2 != 1:
            raise FrameTransportError("Only invertible, source-faithful frames")

    def apply(self, v:BitVector) -> BitVector:
        x,y=_vec(v)
        return ((self.a*x+self.b*y)%2,(self.c*x+self.d*y)%2)

    def then(self, after:"GL2") -> "GL2":
        """Apply self THEN after; after * self, preserving path order."""
        if not isinstance(after,GL2):
            raise FrameTransportError("Need matching declared frame")
        return GL2(
            (after.a*self.a+after.b*self.c)%2,
            (after.a*self.b+after.b*self.d)%2,
            (after.c*self.a+after.d*self.c)%2,
            (after.c*self.b+after.d*self.d)%2,
        )

    def inverse(self) -> "GL2":
        """Inverse since determinant is one; minus equals plus in GF(2)."""
        return GL2(self.d,self.b,self.c,self.a)

    @property
    def is_identity(self) -> bool:
        return self == IDENTITY


IDENTITY=GL2(1,0,0,1)
HORIZONTAL=GL2(1,1,0,1)
VERTICAL=GL2(1,0,1,1)


def _addr(v:BitVector)->int:
    x,y=_vec(v)
    return 2*x+y


@dataclass(frozen=True)
class SquareConnection:
    """Explicit oriented square connection with two paths from SW to NE.

    RU = north_right * east_bottom (east then north)
    UR = east_top * north_left (north then east)
    Relative holonomy W = RU^{-1} * UR, acting on SOURCE coordinates.
    """
    east_bottom:GL2
    north_right:GL2
    north_left:GL2
    east_top:GL2
    source_id:str
    basis_id:str

    def __post_init__(self) -> None:
        if (not all(isinstance(m,GL2) for m in (
                self.east_bottom,self.north_right,
                self.north_left,self.east_top))
                or not isinstance(self.source_id,str) or not self.source_id
                or not isinstance(self.basis_id,str) or not self.basis_id):
            raise FrameTransportError("Connection requires valid oriented edges and source")

    def path(self,which:str) -> GL2:
        if which=="RU":
            return self.east_bottom.then(self.north_right)
        if which=="UR":
            return self.north_left.then(self.east_top)
        raise FrameTransportError("Only declared oriented square paths exist")

    def holonomy(self)->GL2:
        """W=RU^{-1} UR. Reverse comparison would give W^{-1}."""
        return self.path("UR").then(self.path("RU").inverse())

    def local_reading(self,source:BitVector,which:str)->BitVector:
        return self.path(which).apply(source)

    def restore_source(self,local:BitVector,which:str)->BitVector:
        return self.path(which).inverse().apply(local)

    def audit_square(self)->dict:
        ru,ur=self.path("RU"),self.path("UR")
        w=self.holonomy()
        if w.then(ru)!=ur:
            raise ArithmeticError("Holonomy transport factorization failed")
        for v in ALL_VECTORS:
            for p in ("RU","UR"):
                if self.restore_source(self.local_reading(v,p),p)!=v:
                    raise ArithmeticError("Path-aware exact inverse failed")
        return {
            "east_then_north": [ru.a,ru.b,ru.c,ru.d],
            "north_then_east": [ur.a,ur.b,ur.c,ur.d],
            "relative_holonomy": [w.a,w.b,w.c,w.d],
            "flat": w.is_identity,
        }


@dataclass(frozen=True)
class PathBlindVerdict:
    source_id:str
    basis_id:str
    target_id:str
    invariant_under_holonomy:bool
    decoder:tuple[tuple[BitVector,int],...]
    collision:tuple[tuple[str,BitVector],tuple[str,BitVector]]|None

    def decode(self,report:BitVector,*,source_id:str,basis_id:str,
               target_id:str)->int:
        if (source_id,basis_id,target_id)!=(
                self.source_id,self.basis_id,self.target_id):
            raise FrameTransportError("Source/basis/claim contract changed")
        if not self.invariant_under_holonomy:
            raise FrameTransportError("No path-blind decoder for this claim")
        table=dict(self.decoder)
        v=_vec(report)
        if v not in table:
            raise FrameTransportError("Unrepresented local reading")
        return table[v]


def certify_path_blind(connection:SquareConnection,
                       target:tuple[int,int,int,int], *,
                       target_id:str) -> PathBlindVerdict:
    """All-vector theorem: path-blind t iff t(Wv)=t(v) for W=RU^-1 UR.

    Require EXACT source class ALL GF2^2, no artificial prior narrowing.
    A witness gives SAME endpoint report, opposite true original labels,
    with distinct routes and distinct source vectors. Sending the route
    repairs because both path matrices are invertible.
    """
    if type(target) is not tuple or len(target)!=4 or any(
            type(x) is not int or x not in (0,1) for x in target):
        raise FrameTransportError("Predicate needs four declared GF2 labels")
    if not isinstance(target_id,str) or not target_id:
        raise FrameTransportError("Declare a target ID")
    W=connection.holonomy()
    invariant=all(target[_addr(W.apply(v))]==target[_addr(v)]
                  for v in ALL_VECTORS)
    dec={}
    origins={}
    collision=None
    for p in ("RU","UR"):
        for source in ALL_VECTORS:
            y=connection.local_reading(source,p)
            truth=target[_addr(source)]
            if y in dec and dec[y]!=truth and collision is None:
                collision=(origins[y],(p,source))
            dec[y]=truth
            origins.setdefault(y,(p,source))
    if (collision is None)!=invariant:
        raise ArithmeticError("Holonomy invariance/fiber theorem contradicted")
    return PathBlindVerdict(
        connection.source_id,connection.basis_id,target_id,invariant,
        tuple(sorted(dec.items())) if invariant else (),collision)


def nonflat_square()->SquareConnection:
    return SquareConnection(
        HORIZONTAL,VERTICAL,VERTICAL,HORIZONTAL,
        "GF2-square-connection","oriented-edges-v1")


def flat_square()->SquareConnection:
    return SquareConnection(
        HORIZONTAL,IDENTITY,IDENTITY,HORIZONTAL,
        "GF2-square-connection","oriented-edges-v1")


def holonomy_proof_demo()->dict:
    nonflat=nonflat_square()
    flat=flat_square()
    witness=nonflat.audit_square()
    if witness["flat"] or not flat.audit_square()["flat"]:
        raise ArithmeticError("Nonflat/flat calibration failed")
    W=nonflat.holonomy()
    if W.is_identity or not W.then(W).then(W).is_identity:
        raise ArithmeticError("Expected nontrivial order-three holonomy missing")
    first=certify_path_blind(nonflat,(0,0,1,1),target_id="original-first-bit")
    zero=certify_path_blind(nonflat,(1,0,0,0),target_id="original-is-zero")
    if first.invariant_under_holonomy or not zero.invariant_under_holonomy:
        raise ArithmeticError("Failed target-dependent holonomy transport test")
    correct_source_recovery=True
    for vector in ALL_VECTORS:
        for p in ("RU","UR"):
            correct_source_recovery &= (
                nonflat.restore_source(nonflat.local_reading(vector,p),p)
                == vector)
    invariant_predicates=0
    for labels in product((0,1),repeat=4):
        result=certify_path_blind(nonflat,labels,target_id="predicate")
        invariant_predicates+=result.invariant_under_holonomy
        flat_control=certify_path_blind(flat,labels,target_id="predicate")
        if not flat_control.invariant_under_holonomy:
            raise ArithmeticError("Flat square should transport every claim")
    if invariant_predicates!=4:
        raise ArithmeticError("Holonomy orbit count or predicates is incorrect")
    if first.collision is None:
        raise ArithmeticError("Noninvariant first-coordinate target lacks witness")
    collision=first.collision
    return {
        "status":"EXACT_NONFLAT_PROOF_TRANSPORT_GALOIS_GF2",
        "orientation":"relative W=RU^-1 * UR on original source coordinates",
        "RU_matrix":witness["east_then_north"],
        "UR_matrix":witness["north_then_east"],
        "holonomy_matrix":witness["relative_holonomy"],
        "nonflat_holonomy_is_identity":False,
        "holonomy_order":3,
        "path_aware_source_recovered":correct_source_recovery,
        "first_bit_path_blind_decodable":first.invariant_under_holonomy,
        "first_bit_collision_paths":[collision[0][0],collision[1][0]],
        "same_local_report_opposite_source_target":True,
        "is_zero_path_blind_decodable":zero.invariant_under_holonomy,
        "invariant_binary_predicates_out_of_16":invariant_predicates,
        "flat_all_16_predicates_path_blind_decodable":True,
        "unnamed_path_not_guaranteed_to_reconstruct_all_truths":True,
        "connection_physically_measured":False,
        "quantum_phase_or_RH_theorem_claimed":False,
    }
