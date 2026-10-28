"""Source-neutral finite carry fibers behind C_(2^k) -> C_2.

The exact sequence is 0 -> C_(2^(k-1)) -> C_(2^k) -> C_2 -> 0.
The carry cocycle is necessary for addition; feasibility alone supplies no
probability or signed circle-phase law. See the 2026-10-26 source dossier.
"""
from fractions import Fraction as Q


def _int(value, name):
    if type(value) is not int:
        raise ValueError(f"{name}: integer required")
    return value


def _bits(bits):
    _int(bits,"bits")
    if not 2 <= bits <= 32:
        raise ValueError("bit depth in [2,32] required")
    return bits


def split_residue(residue: int, bits: int = 4) -> tuple[int,int]:
    """a=2u+b, with u in C_(2^(bits-1)), b in {0,1}."""
    _bits(bits)
    a=_int(residue,"residue") % (1 << bits)
    return a//2,a%2


def join_residue(fiber: int, parity: int, bits: int = 4) -> int:
    _bits(bits)
    _int(fiber,"fiber")
    _int(parity,"parity")
    if parity not in (0,1):
        raise ValueError("parity is 0 or 1")
    return (2*fiber+parity) % (1 << bits)


def carry_cocycle(left: int, right: int) -> int:
    if type(left) is not int or type(right) is not int or left not in (0,1) or right not in (0,1):
        raise ValueError("two binary residues required")
    return left*right


def add_lifts(left: tuple[int,int], right: tuple[int,int], bits: int = 4) -> tuple[int,int]:
    """Actual extension law; omitting bd would change C_(2^k) to a split group."""
    _bits(bits)
    if not isinstance(left,tuple) or not isinstance(right,tuple) or len(left)!=2 or len(right)!=2:
        raise ValueError("two (fiber,parity) tuples required")
    u,b=split_residue(join_residue(*left,bits),bits)
    v,d=split_residue(join_residue(*right,bits),bits)
    return (u+v+carry_cocycle(b,d)) % (1 << (bits-1)), (b+d)%2


def character_phase(residue: int, frequency: int, bits: int = 4) -> Q:
    """Exact rational phase of exp(2*pi*i*h*a/2^bits), not its floating value."""
    _bits(bits)
    a=_int(residue,"residue")
    h=_int(frequency,"frequency")
    return Q((h*a) % (1 << bits),1 << bits)


def character_descends_to_parity(frequency: int, bits: int = 4) -> bool:
    _bits(bits)
    h=_int(frequency,"frequency")
    return h % (1 << (bits-1)) == 0


def section_homomorphism_defects(fiber_choice: int, bits: int = 4) -> tuple[int,int]:
    """Try s(0)=0,s(1)=2t+1. Its s(1)+s(1)-s(0) is always nonzero.

    Return the full-group and fiber defects. This enumerates every section
    when t ranges over the finite fiber; no homomorphic section exists.
    """
    _bits(bits)
    t=_int(fiber_choice,"section fiber") % (1 << (bits-1))
    return (4*t+2) % (1 << bits), (2*t+1) % (1 << (bits-1))


def parity_alias_control() -> dict:
    """Exact h=4 control: delta_0 vs (delta_0+delta_2)/2 on C16.

    Both parity pushforwards are delta_0. Character values at 0 and 2
    are +1 and -1, so their mean squared magnitudes are 1 and 0.
    """
    phases=tuple(character_phase(a,4) for a in (0,2))
    if phases != (Q(0),Q(1,2)):
        raise ArithmeticError("half-turn phase mutation")
    return {"parity_pushforward_equal":True,
            "coherent_squared_magnitude":Q(1),
            "cancelled_squared_magnitude":Q(0),
            "phase_pair":phases,
            "dynamic_source_selected":False}


def even_mode_cross_digit_support() -> tuple[int,...]:
    """Uniform 8-bit words constrained only by parity of bits {0,4,5,6}.

    Every marginal on at most three bits, and each complete four-bit digit,
    is uniform. Its two-digit Fourier coefficient at the EVEN mode h=2 is
    nonzero. This is a finite countermodel, not a mutated authentic orbit.
    """
    return tuple(k for k in range(256)
                 if sum((k>>i)&1 for i in (0,4,5,6)) % 2 == 0)


def even_mode_cyclotomic_coefficients() -> tuple[Q,...]:
    """Exact h=2 mean reduced modulo Phi_128(X)=X^64+1.

    A nonzero degree<64 vector cannot vanish at a primitive 128th root.
    """
    support=even_mode_cross_digit_support()
    counts=[0]*128
    for k in support:
        counts[k%128]+=1
    return tuple(Q(counts[j]-counts[j+64],len(support)) for j in range(64))
