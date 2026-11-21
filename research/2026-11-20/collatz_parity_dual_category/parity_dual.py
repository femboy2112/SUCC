"""Exact finite certificates for the hexadecimal parity/Collatz dual presentation.

Original mathematics: classical Bernstein--Lagarias 2-adic conjugacy, Monks--Yazinski
complement autoconjugacy. Here we implement finite quotient arithmetic, BBP source
intervals, and the four-step/one-digit intertwinement. No Collatz/normality claim.
"""
from fractions import Fraction


def shortcut(n: int) -> int:
    """Shortcut Collatz C(n) on ordinary integers, including signed controls."""
    return (3 * n + 1) // 2 if n & 1 else n // 2


def parity_address(n: int, bits: int) -> int:
    """First 'bits' Collatz parities as low-to-high binary bits, exact finite."""
    if not isinstance(bits, int) or bits < 0:
        raise ValueError('bits must be nonnegative')
    addr = 0
    for j in range(bits):
        addr |= (n & 1) << j
        n = shortcut(n)
    return addr


def inverse_parity_mod(address: int, bits: int) -> int:
    """Bernstein inverse Phi(address) modulo 2**bits (exact modular arithmetic).

    Formula: -sum(2**j/3**(rank_of_one_bit_j)) over 1-bit positions j.
    All denominators 3**k are units in Z_2. Zero bits beyond 'bits' do
    not affect the residue.
    """
    if not isinstance(bits, int) or bits < 0:
        raise ValueError('bits must be nonnegative')
    mod = 1 << bits
    k = 0
    value = 0
    for j in range(bits):
        if (address >> j) & 1:
            k += 1
            value -= (1 << j) * pow(3, -k, mod)
    return value % mod


def inverse_parity_reverse_mod(address: int, bits: int) -> int:
    """Independent inverse by composing lawful 2-adic Collatz inverse branches.

    A prescribed first parity 0 has inverse y -> 2y; parity 1 has inverse
    y -> (2y-1)/3. Each composition gains one 2-adic precision digit.
    """
    if not isinstance(bits, int) or bits < 0:
        raise ValueError('bits must be nonnegative')
    mod = 1 << bits
    inv3 = pow(3, -1, mod)
    state = 0  # arbitrary terminal lift; the prefix erases it mod 2**bits
    for j in reversed(range(bits)):
        bit = (address >> j) & 1
        state = ((2 * state - 1) * inv3 if bit else 2 * state) % mod
    return state


def four_step_branch(a: int) -> tuple[int,int,int,int]:
    """Return (parity_word, odd_count, affine_intercept, C**4(a))."""
    state = a
    bits = []
    for _ in range(4):
        bits.append(state & 1)
        state = shortcut(state)
    s = sum(bits)
    b = sum((1 << j) * 3 ** sum(bits[l] for l in range(j + 1, 4))
            for j in range(4) if bits[j])
    word = sum(bits[j] << j for j in range(4))
    assert (3 ** s * a + b) % 16 == 0
    assert state == (3 ** s * a + b) // 16
    return word, s, b, state


def parity_word_table() -> tuple[int,...]:
    """Map input residue a mod16 to first four parity bits as a nibble."""
    return tuple(parity_address(a, 4) for a in range(16))


def hex_word_to_address(digits: str) -> int:
    """Chronological hexadecimal digits become LOW-to-HIGH 2-adic nibbles."""
    return sum(int(ch,16) << (4*j) for j,ch in enumerate(digits))


def bbp_forcing(n: int) -> Fraction:
    if not isinstance(n,int) or n < 1:
        raise ValueError('positive BBP source time required')
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def bbp_prefix_interval(terms: int) -> tuple[Fraction,Fraction]:
    """Strict safe interval for x=pi/16, conditional on classical BBP identity."""
    if terms < 1:
        raise ValueError('terms must be positive')
    partial = sum((bbp_forcing(j) / 16**j for j in range(1,terms+1)),Fraction())
    upper = partial+bbp_forcing(terms+1) / (15*16**terms)
    return partial,upper


def bbp_hex_prefix(digits: int, terms: int | None = None) -> str:
    """Certify finite BBP prefix by exact endpoint floors; fail if not resolved."""
    if digits < 1:
        raise ValueError('positive digits required')
    terms = terms if terms is not None else digits
    a,b=bbp_prefix_interval(terms)
    lo = (a*16**digits).__floor__()
    hi = (b*16**digits).__floor__()
    if lo != hi:
        raise ValueError('BBP interval insufficient to certify prefix')
    return format(lo,f'0{digits}X')


def bbp_collatz_seed_residue(digits: int = 12, terms: int | None = None) -> tuple[str,int,int]:
    """Certified π/16 prefix -> parity address -> 2-adic Collatz seed residue."""
    s=bbp_hex_prefix(digits,terms)
    addr=hex_word_to_address(s)
    m=4*digits
    seed=inverse_parity_mod(addr,m)
    assert inverse_parity_reverse_mod(addr,m)==seed
    assert parity_address(seed,m)==addr
    return s,addr,seed


def complement_parity_address(address: int, bits: int) -> int:
    """Full symbolic hex-mirror / 2-adic parity complement, truncated."""
    mask=(1<<bits)-1
    return (-1-address)&mask


def transported_omega_mod(a: int, bits: int) -> int:
    """Monks--Yazinski involution Omega modulo 2**bits."""
    q=parity_address(a,bits)
    return inverse_parity_mod(complement_parity_address(q,bits),bits)


if __name__ == '__main__':
    digits, addr, seed=bbp_collatz_seed_residue()
    print('pi/16 hex prefix:',digits)
    print('parity address mod 2**48:',f'{addr:012X}')
    print('2-adic Collatz seed mod 2**48:',f'{seed:012X}')
    print('4-bit Q table:',parity_word_table())
