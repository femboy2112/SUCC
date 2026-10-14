"""Source-typed wild-embedding laboratory for Observational SUCC.

Three independently typed layers:
  - exact finite PL Hopf/unlink ambient intersection certificates;
  - free-group commutator tower and a consistent finite A5 representation;
  - finite-sheet circle covers, their monodromy and solenoidal cohomology.

The actual Alexander horned sphere exterior is an EXTERNAL topological theorem,
not a constructed geometric source in this module. No relation to Weil-form
positivity or RH is claimed. This module uses no numerical probability or zeros.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import permutations
from functools import lru_cache


class AmbientError(ValueError):
    """A proposed source, probe, or mathematical transport lacks its contract."""


def exact(x):
    if type(x) not in (int, Q):
        raise AmbientError('Coordinates and certificates require exact rational values')
    return Q(x)


@dataclass(frozen=True)
class SourceFrame:
    source_id: str
    epoch: int
    basis_id: str
    ambient_orientation: int = 1

    def __post_init__(self):
        if (type(self.source_id) is not str or not self.source_id or
            type(self.epoch) is not int or self.epoch < 0 or
            type(self.basis_id) is not str or not self.basis_id or
            type(self.ambient_orientation) is not int or abs(self.ambient_orientation) != 1):
            raise AmbientError('Source/epoch/basis/orientation must be exact and declared')

    def check(self, other:'SourceFrame'):
        if not isinstance(other,SourceFrame) or self != other:
            raise AmbientError('Transport across source, epoch, basis or orientation is unlicensed')


@dataclass(frozen=True)
class SquareDisk:
    radius: Q
    orientation: int
    source: SourceFrame

    def __post_init__(self):
        if not isinstance(self.source,SourceFrame):
            raise AmbientError('An authenticated mathematical source frame is required')
        r = exact(self.radius)
        if r <= 0 or type(self.orientation) is not int or self.orientation not in (-1, 1):
            raise AmbientError('A positive exact spanning disk and oriented boundary required')
        object.__setattr__(self, 'radius', r)

    def boundary(self):
        r = self.radius
        return ((-r,-r,Q()),(r,-r,Q()),(r,r,Q()),(-r,r,Q()))


@dataclass(frozen=True)
class RectangularThread:
    y_low: Q
    y_high: Q
    height: Q
    orientation: int
    source: SourceFrame

    def __post_init__(self):
        if not isinstance(self.source,SourceFrame):
            raise AmbientError('An authenticated mathematical source frame is required')
        yl,yh,h = (exact(x) for x in (self.y_low,self.y_high,self.height))
        if not yl < yh or h <= 0 or type(self.orientation) is not int or self.orientation not in (-1,1):
            raise AmbientError('Simple oriented transverse rectangular curve required')
        object.__setattr__(self, 'y_low',yl)
        object.__setattr__(self, 'y_high',yh)
        object.__setattr__(self, 'height',h)

    def vertices(self):
        l,h,z=self.y_low,self.y_high,self.height
        raw=((Q(),l,-z),(Q(),h,-z),(Q(),h,z),(Q(),l,z))
        return raw if self.orientation==1 else tuple(reversed(raw))


def certified_linking(disk: SquareDisk, thread: RectangularThread):
    """Exact linking as signed transverse intersections with an oriented square.

    Restricted to the stated disjoint embedded polygon models. The classical
    intersection/linking theorem, not a projected crossing heuristic, is used.
    """
    disk.source.check(thread.source)
    r=disk.radius
    if any(abs(y)==r for y in (thread.y_low,thread.y_high)):
        raise AmbientError('A crossing on the spanning-disk boundary is invalid')
    polygon=thread.vertices()
    contacts=[]
    for i,u in enumerate(polygon):
        v=polygon[(i+1)%len(polygon)]
        z0,z1=u[2],v[2]
        if not z0*z1<0:
            continue
        fraction=-z0/(z1-z0)
        x=u[0]+fraction*(v[0]-u[0]);y=u[1]+fraction*(v[1]-u[1])
        if abs(x)==r or abs(y)==r:
            raise AmbientError('Nontransverse contact on disk boundary')
        if abs(x)<r and abs(y)<r:
            contacts.append({'edge':i,'xy':(x,y),'crossing':1 if z1>z0 else -1})
    signed=disk.orientation*sum(z['crossing'] for z in contacts)
    return {'linking':signed,'absolute_linking':abs(signed),
            'disk_orientation':disk.orientation,'thread_orientation':thread.orientation,
            'crossings':tuple(contacts),'source':disk.source.source_id,
            'certified_scope':'disjoint_oriented_PL_rectangle_and_square'}


def intrinsic_octahedron():
    """The standard 8-face PL sphere; does not construct a wild embedding."""
    vertices=tuple(range(6))
    opposite=((0,1),(2,3),(4,5))
    faces=tuple(tuple(pair[i] for pair,i in zip(opposite,which))
                for which in ((a,b,c) for a in (0,1) for b in (0,1) for c in (0,1)))
    edges=set()
    for f in faces:
        for i in range(3):
            edges.add(tuple(sorted((f[i],f[(i+1)%3]))))
    if (len(vertices),len(edges),len(faces))!=(6,12,8):
        raise AssertionError('Internal combinatorial octahedron construction invalid')
    return {'vertices':len(vertices),'edges':len(edges),'faces':len(faces),
            'euler':len(vertices)-len(edges)+len(faces),
            'intrinsic_class':'PL_S2','ambient_embedding_not_determined':True}


def alexander_imported_complement():
    """A theorem dependency, not an executed Alexander-horn embedding proof."""
    return {'intrinsic':'S2','standard_exterior_pi1':'trivial',
            'alexander_exterior_pi1':'nontrivial_perfect',
            'alexander_exterior_H1':'zero',
            'ambient_equivalence':'obstructed_by_pi1',
            'theorem_source':'Alexander_1924_Hatcher_ch1_and_Alexander_duality',
            'status':'EXTERNAL_CLASSICAL_NOT_CODE_DERIVED',
            'commutator_tower_is_classical_exterior_pi1_via_Hatcher':True,
            'actual_A5_quotient_via_imported_topology':True,
            'physical_A5_probe_realized':False,
            'actual_geometric_horns_constructed':False}


def inverse_word(word):
    return tuple(-x for x in reversed(tuple(word)))


def reduce_free(word):
    out=[]
    for x in word:
        if type(x) is not int or x==0:
            raise AmbientError('Free-group word needs nonzero signed generator integers')
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)


def commutator(x,y):
    x=reduce_free(x);y=reduce_free(y)
    return reduce_free(x+y+inverse_word(x)+inverse_word(y))


def exponent_vector(word, rank):
    if type(rank) is not int or rank<1:
        raise AmbientError('Positive finite rank required')
    vector=[0]*rank
    for x in reduce_free(word):
        if abs(x)>rank:
            raise AmbientError('Generator outside stage carrier')
        vector[abs(x)-1]+=1 if x>0 else -1
    return tuple(vector)


def expand_stage(word,stage):
    """Canonical F_(2^stage) -> F_(2^(stage+1)), each x_i -> [y_2i,y_2i+1]."""
    if type(stage) is not int or not 0<=stage<=14:
        raise AmbientError('Stage must be finite nonnegative integer under execution budget')
    out=[]
    for signed in reduce_free(word):
        if abs(signed)>2**stage:
            raise AmbientError('Generator not in declared domain stage')
        i=abs(signed)-1
        base=commutator((2*i+1,), (2*i+2,))
        out.extend(base if signed>0 else inverse_word(base))
    return reduce_free(out)


def expand_root(depth,max_letters=65536):
    """Exact fully expanded commutator: finite word length 4^depth."""
    if type(depth) is not int or type(max_letters) is not int or depth<0 or 4**depth>max_letters:
        raise AmbientError('Requested expansion exceeds declared finite causal budget')
    word=(1,)
    for j in range(depth):
        word=expand_stage(word,j)
    if len(word)!=4**depth:
        raise AssertionError('Unexpected cancellation in disjoint-support tower')
    return word


def commutator_tower_receipt(depth,max_letters=65536):
    w=expand_root(depth,max_letters)
    return {'stage':depth,'leaf_generators':2**depth,'word_length':len(w),
            'expected_word_length':4**depth,
            'free_reduced_nonidentity':bool(w),
            'abelian_image_zero':all(x==0 for x in exponent_vector(w,2**depth)),
            'head':w[:min(12,len(w))],'tail':w[-min(12,len(w)):],
            'intrinsic_source':'free_commutator_tower_not_alexander_pi1'}


Permutation=tuple[int,...]
ID=(0,1,2,3,4)


def compose(x:Permutation,y:Permutation)->Permutation:
    if len(x)!=5 or len(y)!=5:
        raise AmbientError('Only S5 permutations supported')
    return tuple(x[y[i]] for i in range(5))


def invert(x:Permutation)->Permutation:
    if len(x)!=5 or set(x)!=set(range(5)):
        raise AmbientError('Invalid permutation')
    q=[0]*5
    for i,j in enumerate(x):q[j]=i
    return tuple(q)


def group_commutator(x:Permutation,y:Permutation)->Permutation:
    return compose(compose(compose(x,y),invert(x)),invert(y))


@lru_cache(maxsize=1)
def a5():
    elements=tuple(p for p in permutations(range(5))
                   if sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2==0)
    if len(elements)!=60:raise AssertionError('A5 order mismatch')
    return elements


@lru_cache(maxsize=1)
def a5_commutator_witnesses():
    """3600 exact checks certify surjectivity of the commutator map for A5."""
    samples={}
    for x in a5():
        for y in a5():
            samples.setdefault(group_commutator(x,y),(x,y))
    if len(samples)!=60:
        raise AssertionError('A5 commutator map was not surjective')
    return samples


def a5_tower_assignment(depth,root=(1,2,0,3,4),max_nodes=8191):
    """Coherent finite restriction of an infinite recursively defined homomorphism.

    A5 witnesses exist for every element; the finite lookup defines assignments
    at every depth, with a single constant-size mathematical rule table.
    """
    if type(depth) is not int or depth<0 or (2**(depth+1)-1)>max_nodes:
        raise AmbientError('Finite A5 observation budget exceeded')
    if root not in a5():
        raise AmbientError('Root is not an actual A5 permutation')
    cert=a5_commutator_witnesses()
    levels=[(root,)]
    for j in range(depth):
        nxt=[]
        for z in levels[-1]:
            left,right=cert[z]
            if group_commutator(left,right)!=z:raise AssertionError('Lookup corruption')
            nxt.extend((left,right))
        levels.append(tuple(nxt))
    return {'depth':depth,'nodes':2**(depth+1)-1,
            'root':root,'root_detected':root!=ID,
            'all_edge_relations':all(group_commutator(*cert[z])==z for row in levels[:-1] for z in row),
            'per_level_counts':tuple(len(row) for row in levels),
            'trivial_abelian_character_on_root':depth>=1,
            'representation_is_of_abstract_direct_limit':True,
            'representation_of_actual_alexander_exterior_proved':False,
            'representation_derived_using_imported_Hatcher_pi1_theorem':True,
            'independently_verified_geometry':False,
            'actual_weil_form_positive_proved':False}


def abelian_character_of_expanded_root(depth, modulus, weights=None):
    if type(modulus) is not int or modulus<=1:
        raise AmbientError('Finite scalar-character group must be nontrivial')
    w=expand_root(depth)
    if weights is None:weights=tuple(range(2**depth))
    if type(weights) is not tuple or len(weights)!=2**depth or any(type(k)is not int for k in weights):
        raise AmbientError('One declared phase for every generator required')
    return sum(a*b for a,b in zip(exponent_vector(w,2**depth),weights))%modulus


def covering_monodromy(degree,winding):
    if type(degree) is not int or degree<=1 or type(winding)is not int:
        raise AmbientError('Nontrivial finite-sheet covering and integer loop winding required')
    return {'sheets':degree,'winding':winding,
            'sheet_permutation':tuple((i+winding)%degree for i in range(degree)),
            'trivial':winding%degree==0,
            'global_continuous_section_exists':False}


def cyclic_lift(t,degree):
    """Set-theoretic root in [0,1), NOT a globally continuous circle section."""
    t=exact(t)
    if not 0<=t<1 or type(degree)is not int or degree<1:
        raise AmbientError('Rational circle phase must lie in [0,1), degree positive')
    return t/degree


def solenoid_cohomology_class(value,stage,degree=2):
    """A class in colim(Z --degree--> Z), embedded in Z[1/degree]."""
    if type(value)is not int or type(stage)is not int or stage<0 or stage>100 or type(degree)is not int or degree<=1:
        raise AmbientError('Typed integral Cech class and positive finite stage required')
    return Q(value,degree**stage)


def intrinsic_vs_ambient_observer():
    a=intrinsic_octahedron(); external=alexander_imported_complement()
    return {'identical_intrinsic_S2':a['intrinsic_class']=='PL_S2' and external['intrinsic']=='S2',
            'different_ambient_exterior':True,
            'ambient_difference_is_imported_topology':True,
            'homology_H1_distinguishes_alexander_exterior':False,
            'abelian_complex_phase_distinguishes_alexander_exterior':False,
            'nonabelian_invariant_needed_to_detect_this_example':True,
            'topology_implies_Weil_positivity':False}


def evidence_contract(source:SourceFrame,kind:str,available:tuple[str,...]):
    if kind not in ('intrinsic','PL_link','abstract_A5','external_Alexander','arith_Weil'):
        raise AmbientError('Unknown evidence kind')
    if kind not in available:
        raise AmbientError('Unavailable ambient instrument cannot be simulated as an observation')
    return {'source':source.source_id,'epoch':source.epoch,'basis':source.basis_id,
            'kind':kind,'status':'MATHEMATICAL_DECLARED_SOURCE_NOT_REAL_INSTRUMENT'}


def reflection_positive_no_go():
    """Commutation with reflection R=diag(1,-1) is compatible with negative Q."""
    r=((1,0),(0,-1));q=((1,0),(0,-1))
    mul=lambda a,b:tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return {'commutes':mul(r,q)==mul(q,r), 'reflection_invariant':mul(r,mul(q,r))==q,
            'even_rayleigh':q[0][0],'odd_rayleigh':q[1][1],
            'PSD_forced_by_reflection':False,'Weil_identification':False}


def compressed_flat_operator_control():
    """Commuting full-carrier maps can acquire a projected commutator.

    Exact algebraic negative control for treating SUCC's projection leakage as
    an intrinsic nonflat/wild ambient holonomy. No relation to original zeta
    operators is asserted for this finite rational model.
    """
    def mm(x,y):
        return tuple(tuple(sum(x[i][k]*y[k][j] for k in range(3))
                           for j in range(3)) for i in range(3))
    def add(x,y,sign=1):
        return tuple(tuple(x[i][j]+sign*y[i][j] for j in range(3)) for i in range(3))
    A=((0,1,1),(1,0,0),(1,0,2))
    K=mm(A,A)
    P=((1,0,0),(0,1,0),(0,0,0))
    I=((1,0,0),(0,1,0),(0,0,1))
    R=add(I,P,-1)
    full=add(mm(A,K),mm(K,A),-1)
    PA=mm(mm(P,A),P)
    PK=mm(mm(P,K),P)
    compressed=add(mm(PA,PK),mm(PK,PA),-1)
    leakage=add(mm(mm(mm(mm(P,K),R),A),P),
                mm(mm(mm(mm(P,A),R),K),P),-1)
    if compressed != leakage:
        raise AssertionError('Projection identity failure')
    return {'full_commutator_zero':full==((0,0,0),)*3,
            'compressed_commutator':compressed,
            'nonzero_only_after_compression':compressed!=((0,0,0),)*3,
            'exact_boundary_leakage_identity':compressed==leakage,
            'projection_commutator_proves_real_wild_embedding':False}


def a5_holonomy_energy_sign_control():
    """A valid nonabelian positive connection energy is NOT a Weil-positive form."""
    root=(1,2,0,3,4)
    constant=(1,1,1,1,1)
    moved=tuple(constant[root[i]] for i in range(5))
    energy=sum((a-b)**2 for a,b in zip(constant,moved))
    negative_source_shift=energy-sum(t*t for t in constant)
    return {'group':'A5','root_nonidentity':root!=ID,
            'fixed_constant_vector':moved==constant,
            'connection_energy_nonnegative':energy>=0,
            'source_signed_toy_form':negative_source_shift,
            'full_Weil_form_identified':False}


def a5_conjugacy_invariant_observer(root=(1,2,0,3,4)):
    """Finite conjugacy-invariant trace, suitable for change-of-basepoint gauge.

    5-dimensional permutation representation of A5, tr(P_g)=#fixed points.
    This finite algebraic readout is NOT an authorized sensor of R^3.
    """
    if root not in a5():
        raise AmbientError('A5 gauge observer requires a genuine even permutation')
    tr=sum(root[i]==i for i in range(5))
    for gauge in a5():
        conjugate=compose(compose(gauge,root),invert(gauge))
        if sum(conjugate[i]==i for i in range(5))!=tr:
            raise AssertionError('A5 trace was not gauge invariant')
    return {'root_trace':tr,'identity_trace':5,'class_detects_nonidentity':tr!=5,
            'all_60_conjugations_certified':True,
            'basepoint_change_invariance':'conjugacy_only',
            'real_world_instrument_authentication':False}
