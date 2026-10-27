"""Exact recursive 2-adic SUCC gates and denominator-cleared 3-adic BBP geometry.

Research continuation of source-verified draft PR #321. The authoritative
BBP recurrence is imported through the existing bbp_binwindow_conjugacy,
not rewritten. Every result is finite/exact; the ALL-K proof and 3-adic
nonconvergence arguments reside in the accompanying mathematical dossier.

Important types:
 - Phi(n) is an integer in Z/2^K Z (NOT a real-circle phase).
 - A(n) is the cleared-source numerator in Z/3^L Z (NOT U_n in Z_3).
 - Only the combination of these two separately authenticated labels is CRT.
 - Exact arithmetic Haar for these labels implies NO real pi normality.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction

from .bbp_binwindow_conjugacy import (
    BASE, canceled_source_extension, stationary_window,
)

SOURCE_TAG = "original-zero-anchored-four-pole-BBP-plus-cleared-source"


def _integer(value, label: str, minimum: int | None = None, maximum: int | None = None):
    if type(value) is not int:
        raise ValueError(f"{label}: exact integer needed")
    if minimum is not None and value < minimum:
        raise ValueError(f"{label}: below minimum")
    if maximum is not None and value > maximum:
        raise ValueError(f"{label}: above maximum")
    return value


def binary_code(n: int, bits: int) -> int:
    """Phi(n) mod 2**bits, using PR #321's source-authentic infinite past.

    The source's analytic Phi(0)=0 theorem is explicitly inherited; finite
    code does NOT establish its all-infinite counterpart independently.
    """
    _integer(n, "time index", 0, 10**15)
    _integer(bits, "binary depth", 1, 32)
    # Compatible source windows depend only on n modulo 2**bits.  The
    # inherited PR321 adapter deliberately caps rational indices at 10**6.
    # For larger classes, reconstruct EXACTLY the same canceled four-pole
    # source through an independent modular-polynomial evaluator.  Never
    # replace the original forcing with another sequence.
    source_index=n % (1<<bits)
    hex_depth=(bits+3)//4
    if source_index <= 999_999:
        return stationary_window(source_index, hex_depth) % (1<<bits)
    mod=1<<bits
    total=0
    factor=1
    for offset in range(hex_depth):
        t=source_index-offset
        A=120*t*t-89*t+16
        D=(2*t-1)*(4*t-1)*(8*t-7)*(8*t-3)
        if D%2==0:
            raise ArithmeticError("source denominator ceased to be 2-adic unit")
        total=(total+factor*A*pow(D,-1,mod))%mod
        factor*=16
    return total


def shear_bit(bit: int, lower_input: int) -> int:
    """Unique triangular correction f_bit(lower_input).

    For any input n, output bit j equals input bit j XOR f_j(n mod 2^j).
    Isometry proves independence from the higher bits, all depths.
    """
    _integer(bit, "bit", 0, 31)
    _integer(lower_input, "lower input", 0)
    if lower_input >= (1 << bit):
        raise ValueError("lower input has forbidden unreconstructed high bits")
    return (binary_code(lower_input, bit + 1) >> bit) & 1


def binary_inverse_from_gates(output_code: int, bits: int) -> int:
    """Decode the authentic 2-adic time bin one bit at a time.

    This is an effective inverse of Phi mod 2**bits: at each bit only the
    earlier input bits have been read. No brute-force inverse search.
    """
    _integer(bits, "bits", 1, 32)
    _integer(output_code, "output code", 0, (1 << bits) - 1)
    recovered = 0
    for bit in range(bits):
        correction = shear_bit(bit, recovered)
        recovered |= (((output_code >> bit) & 1) ^ correction) << bit
    if binary_code(recovered, bits) != output_code:
        raise ArithmeticError("triangular inverse does not match authentic source")
    return recovered


def shear_truth_table(bit: int):
    """Complete, exact correction truth table. Bounded to avoid exponential use."""
    _integer(bit, "bit", 0, 9)
    return tuple(shear_bit(bit, n) for n in range(1 << bit))


def shear_anf_masks(bit: int) -> tuple[int, ...]:
    """Unique algebraic normal form over F_2, Möbius transform of gates.

    Mask m represents product of Boolean input bits selected by m. The empty
    mask represents the constant 1. Exact finite ANF, NOT a polynomial over Q.
    """
    table = list(shear_truth_table(bit))
    for digit in range(bit):
        for mask in range(1 << bit):
            if mask & (1 << digit):
                table[mask] ^= table[mask ^ (1 << digit)]
    return tuple(mask for mask, coeff in enumerate(table) if coeff)


def evaluate_anf(masks: tuple[int, ...], lower_input: int) -> int:
    """Interpret a finite ANF at one exact bit assignment."""
    _integer(lower_input, "lower input", 0)
    answer = 0
    for mask in masks:
        _integer(mask, "ANF mask", 0)
        if (lower_input & mask) == mask:
            answer ^= 1
    return answer


def first_hex_reflection(n: int) -> int:
    """Source-specific first-level involution Phi(n)=2(n mod2)-n mod16."""
    _integer(n, "index", 0, 100_000_000)
    value = (2 * (n & 1) - n) % 16
    if binary_code(n, 4) != value:
        raise ArithmeticError("mod-16 reflection disagrees with authentic window")
    return value


def conjugated_successor(source_state: int, bits: int) -> int:
    """T_K=Phi_K o (+1) o Phi_K^-1, an exact single-cycle odometer."""
    _integer(bits, "depth", 1, 32)
    _integer(source_state, "state residue", 0, (1 << bits) - 1)
    t = binary_inverse_from_gates(source_state, bits)
    return binary_code((t + 1) % (1 << bits), bits)


def binary_recursion_receipt(bits: int) -> dict:
    _integer(bits, "depth", 1, 12)
    mod = 1 << bits
    forward = tuple(binary_code(n, bits) for n in range(mod))
    if len(set(forward)) != mod or forward[0] != 0:
        raise ArithmeticError("failed 2-adic finite permutation")
    reverse = tuple(binary_inverse_from_gates(y, bits) for y in range(mod))
    if any(reverse[forward[n]] != n for n in range(mod)):
        raise ArithmeticError("inverse recursion does not invert the source")
    if bits <= 8:
        for j in range(bits):
            masks = shear_anf_masks(j)
            for lower in range(1 << j):
                if evaluate_anf(masks, lower) != shear_bit(j, lower):
                    raise ArithmeticError("ANF does not reproduce source shear")
    return {"binary_depth": bits, "states": mod, "bijection": True,
            "inverse_is_bit_recursive": True, "zero_anchor": forward[0] == 0,
            "first_values": list(forward[:16]), "normality_proved": False}


def source_numerator(n: int) -> int:
    _integer(n, "time integer", -10**15, 10**15)
    return 120*n*n - 89*n + 16


def source_denominator(n: int) -> int:
    _integer(n, "time integer", -10**15, 10**15)
    return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)


def regularized_ternary_code(n: int, digits: int) -> int:
    """A(n) modulo 3**digits; A=D*r (NOT U in Z_3)."""
    _integer(n, "index", -10**15, 10**15)
    _integer(digits, "ternary depth", 1, 15)
    if n >= 1:
        if n <= 999_999:
            source=canceled_source_extension(n)
        else:
            source=(Fraction(4,8*n-7)-Fraction(2,8*n-4)
                    -Fraction(1,8*n-3)-Fraction(1,8*n-2))
        if Fraction(source_numerator(n),source_denominator(n))!=source:
            raise ArithmeticError("denominator-cleared source does not match four signed poles")
    return source_numerator(n) % (3**digits)


def ternary_inverse_from_lifts(target: int, digits: int) -> int:
    """Hensel digit-by-digit inverse of the *cleared numerator* A mod 3**L."""
    _integer(digits, "depth", 1, 15)
    modulus = 3**digits
    _integer(target, "target", 0, modulus - 1)
    x = 0
    level = 1
    for _ in range(digits):
        goal = target % (3*level)
        matches = [x + j*level for j in range(3)
                   if source_numerator(x+j*level) % (3*level) == goal]
        if len(matches) != 1:
            raise ArithmeticError("3-adic numerator lost its unit derivative")
        x = matches[0]
        level *= 3
    if source_numerator(x) % modulus != target:
        raise ArithmeticError("3-adic inverse mismatch")
    return x


def pole_root_mod_three(function: str, digits: int) -> int:
    """Unique 3-adic root prefix for the numerator or one BBP denominator."""
    _integer(digits, "depth", 1, 12)
    polys = {
        "numerator": source_numerator,
        "two_n_minus_one": lambda n: 2*n - 1,
        "four_n_minus_one": lambda n: 4*n - 1,
        "eight_n_minus_seven": lambda n: 8*n - 7,
        "eight_n_minus_three": lambda n: 8*n - 3,
    }
    if function not in polys:
        raise ValueError("unrecognized authenticated polynomial form")
    fn = polys[function]
    root, scale = 0, 1
    for _ in range(digits):
        candidates = [root + j*scale for j in range(3)
                      if fn(root+j*scale) % (3*scale) == 0]
        if len(candidates) != 1:
            raise ArithmeticError("root not unique at this Hensel layer")
        root = candidates[0]
        scale *= 3
    return root


def source_pole_residues() -> dict:
    """All four genuine rational/3-adic poles and classical finite residues.

    Derive each residue A(alpha)/D'(alpha) independently from the canceled
    polynomial rather than merely repeating the original four coefficients.
    The sum of signed residues is ZERO although every pole is genuine.
    """
    # Original poles are x=7/8,1/2,3/8,1/4 with residue 4/8,-2/8,-1/8,-1/8.
    factors=((2,-1),(4,-1),(8,-7),(8,-3))
    residues=[]
    for slope,constant in factors:
        alpha=Fraction(-constant,slope)
        derivative_at_pole=Fraction(slope)
        for oslope,oconstant in factors:
            if (oslope,oconstant)!=(slope,constant):
                derivative_at_pole*=oslope*alpha+oconstant
        num=120*alpha*alpha-89*alpha+16
        if not derivative_at_pole or not num:
            raise ArithmeticError("a previously genuine source pole disappeared")
        residues.append((alpha,num/derivative_at_pole))
    if sum((v for _,v in residues),Fraction()) != 0:
        raise ArithmeticError("global BBP pole residues no longer sum to zero")
    return {"poles":tuple(residues),"sum_of_finite_residues":Fraction(0),
            "local_poles_remain":True,"no_3adic_convergence_implication":True}


def ternary_trident(depth: int) -> dict:
    """At mod3 numerator/A and two pole forms align; at mod9 they split."""
    _integer(depth, "precision", 1, 12)
    names = ("numerator", "two_n_minus_one", "eight_n_minus_seven")
    roots = tuple(pole_root_mod_three(name, depth) for name in names)
    if depth == 1 and roots != (2,2,2):
        raise ArithmeticError("mod-3 source-form coincidence changed")
    if depth >= 2 and len(set(x % 9 for x in roots)) != 3:
        raise ArithmeticError("mod-9 trident is not separate")
    return {"depth":depth,"modulus":3**depth,
            "form_names":names,"roots":roots,
            "coincidence_count":1 if depth==1 else 0,
            "independent_copy_baseline":Fraction(1,3**(3*depth)),
            "descriptive_ratio":9 if depth==1 else 0,
            "same_variable_dependence":True,
            "real_circle_pi_normality_proved":False}


def v3_integer(n: int) -> int:
    _integer(n,"valuation argument")
    if not n:
        raise ValueError("3-adic valuation of zero is unbounded")
    n = abs(n)
    val = 0
    while n % 3 == 0:
        n //= 3
        val += 1
    return val


def v3_fraction(numerator: int, denominator: int) -> int:
    _integer(numerator,"fraction numerator")
    _integer(denominator,"fraction denominator")
    return v3_integer(numerator)-v3_integer(denominator)


def backward_three_adic_divergence(depth: int, center: int=0) -> dict:
    """An explicit unbounded 3-adic subsequence in sum 16**s r(center-s).

    For every center in Z_3, choose positive s_j with center-s_j close to
    pole 3/8 mod 3**j. Here center is an integer (finite exact receipt).
    On n=center-s_j ≡0 mod3, A(n) and other factors are 3-adic units,
    and v3(r(n))=-v3(8*n-3)<=-j. As |16|_3=1, terms do NOT tend to zero.
    """
    _integer(depth,"depth",1,13)
    _integer(center,"center",-1_000_000,1_000_000)
    modulus = 3**depth
    target = (3*pow(8,-1,modulus))%modulus
    s = ((center-target)%modulus)+modulus
    n = center-s
    if n%3 or (8*n-3)%modulus:
        raise ArithmeticError("failed 3-adic pole approach")
    A=source_numerator(n)
    D=source_denominator(n)
    if v3_integer(A) != 0:
        raise ArithmeticError("numerator must be 3-adic unit near 3/8")
    valuation = v3_fraction(A,D)
    if valuation > -depth:
        raise ArithmeticError("backward 3-adic term failed to diverge")
    return {"depth":depth,"center":center,"positive_age":s,
            "pole_distance_valuation_at_least":depth,
            "source_term_valuation":valuation,
            "weighted_term_valuation":valuation,
            "convergent_three_adic_past":False}


def crt_time_to_source_pair(n: int, hex_depth: int, ternary_depth: int) -> tuple[int,int]:
    """2-adic BBP state and 3-adic CLEARED numerator from same time."""
    _integer(n,"time",0,10**15)
    _integer(hex_depth,"hex depth",1,6)
    _integer(ternary_depth,"ternary depth",1,10)
    return binary_code(n,4*hex_depth), regularized_ternary_code(n,ternary_depth)


def crt_source_pair_to_time(code_two: int, code_three: int,
                            hex_depth:int,ternary_depth:int) -> int:
    """Constructive Chinese remainder inverse of the joint primal clock."""
    _integer(hex_depth,"hex depth",1,6)
    _integer(ternary_depth,"ternary depth",1,10)
    m2 = 16**hex_depth
    m3 = 3**ternary_depth
    _integer(code_two,"2-adic source code",0,m2-1)
    _integer(code_three,"3-adic cleared numerator code",0,m3-1)
    n2 = binary_inverse_from_gates(code_two,4*hex_depth)
    n3 = ternary_inverse_from_lifts(code_three,ternary_depth)
    n = n2 + m2*((n3-n2)*pow(m2,-1,m3)%m3)
    if crt_time_to_source_pair(n,hex_depth,ternary_depth)!=(code_two,code_three):
        raise ArithmeticError("CRT arithmetic source pair failed")
    return n


@dataclass(frozen=True)
class CRTClockReceipt:
    hex_depth: int
    ternary_depth: int
    time_period: int
    unique_pairs: int
    zero_anchor_two: int
    zero_anchor_three: int
    full_bijection_checked: bool
    zero_selected_real_pi_normality_proved: bool=False


def crt_period_certificate(hex_depth:int, ternary_depth:int,
                           maximum=6000)->CRTClockReceipt:
    _integer(hex_depth,"hex depth",1,5)
    _integer(ternary_depth,"ternary depth",1,8)
    _integer(maximum,"budget",1,100_000)
    modulus = 16**hex_depth * 3**ternary_depth
    if modulus > maximum:
        raise ValueError("finite enumeration exceeds budget; theorem remains all levels")
    pairs={crt_time_to_source_pair(n,hex_depth,ternary_depth)
           for n in range(modulus)}
    if len(pairs)!=modulus:
        raise ArithmeticError("joint prime-source clock lost a residue pair")
    for n in range(modulus):
        a,b=crt_time_to_source_pair(n,hex_depth,ternary_depth)
        if crt_source_pair_to_time(a,b,hex_depth,ternary_depth)!=n:
            raise ArithmeticError("CRT inverse did not recover time")
    a0,b0=crt_time_to_source_pair(0,hex_depth,ternary_depth)
    return CRTClockReceipt(hex_depth,ternary_depth,modulus,len(pairs),a0,b0,True)


def source_status_flags()->dict:
    return {"original_source_unchanged":True,"2adic_triangular_permutation":True,
            "3adic_cleared_numerator_permutation":True,
            "3adic_unweighted_infinite_past_converges":False,
            "finite_CRT_primal_clock":True,
            "2adic_state_equals_3adic_numerator":False,
            "real_pi_base16_normality_proved":False,"RH_proved":False}
