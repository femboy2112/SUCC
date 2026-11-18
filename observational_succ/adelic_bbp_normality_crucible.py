"""Adelic BBP Period-Seed Duality, Iwasawa 2-Adic Null-Seed Coherence,
Octic CRT Period Quotient, Four-Class Terminal Prime Survival, and the
Closed-Form Parseval-Cauchy-Schwarz Borwein Normality Crucible.

All computations use exact standard-library rational (Fraction) and integer
arithmetic. Finite certificates verify exact algebraic/number-theoretic
identities and countermodels; the universal all-late-shell R0 and full
base-16 pi normality limits remain OPEN.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, isqrt

from observational_succ.borwein_quantitative_certificate import (
    DELTA,
    FOURIER_FLOOR as CHATGPT_FOURIER_FLOOR,
    HAAR_MEAN,
    U,
    _rational_sqrt_upper,
    autocorrelation,
    original_energy,
    original_phases,
    shadow_tail,
    source_r,
    torus,
)

# Sharp Fourier floor: for |h|=1, sin(pi/9)/(2*pi) < 1/18 so 4/9 - sin(pi/9)/(2*pi) > 7/18 > 13/36;
# for |h|>=2, 4/9 - 1/(2*pi*|h|) >= 4/9 - 1/(4*pi) > 4/9 - 1/12 = 13/36.
# With pi < 22/7, (162/289)*(13/36)/(22/7)^2 = 5733/279752 = (13/10) * (2205/139876).
SHARP_FOURIER_FLOOR = F(5733, 279752)
BORWEIN_AUTOCORR_DENOM = 11275335


def v2_int(n):
    """Exact 2-adic valuation v_2(n) for nonzero integer n."""
    if type(n) is not int or n == 0:
        raise ValueError("nonzero int required for v2_int")
    m = abs(n)
    return (m & -m).bit_length() - 1


def v2_fraction(q):
    """Exact 2-adic valuation v_2(q) for nonzero rational q."""
    q = F(q)
    if q == 0:
        raise ValueError("nonzero Fraction required for v2_fraction")
    return v2_int(q.numerator) - v2_int(q.denominator)


def source_r_any_int(k):
    """Authentic four-pole BBP rational forcing r_1(k) at any integer k in Z.

    Notice that 8k-7, 8k-4=4(2k-1), 8k-3, 8k-2=2(4k-1) never vanish on Z,
    and after combining -2/(8k-4) - 1/(8k-2) = -(3k-1)/((2k-1)(4k-1)),
    every denominator factor is odd for all k in Z.
    """
    if type(k) is not int:
        raise ValueError("integer clock k required")
    return F(4, 8 * k - 7) - F(2, 8 * k - 4) - F(1, 8 * k - 3) - F(1, 8 * k - 2)


def source_r_factored(k):
    """Combined rational form (120 k^2 - 89 k + 16)/((2k-1)(4k-1)(8k-7)(8k-3))."""
    if type(k) is not int:
        raise ValueError("integer clock k required")
    num = 120 * k * k - 89 * k + 16
    den = (2 * k - 1) * (4 * k - 1) * (8 * k - 7) * (8 * k - 3)
    return F(num, den)


def source_r2_any_int(k):
    """Second published base-16 BBP pi formula r_2(k) at any integer k in Z."""
    if type(k) is not int:
        raise ValueError("integer clock k required")
    return F(4, 8 * k - 6) + F(2, 8 * k - 5) + F(2, 8 * k - 4) - F(1, 2 * (8 * k - 1))


def source_r_flat(n):
    """TFL-01 Two-BBP-Formula Locked Countermodel r_flat(n) for n >= 1."""
    if type(n) is not int or n < 1:
        raise ValueError("positive integer clock n >= 1 required")
    b_n = F(1, 16 * n) + F(5, 128 * n * n)
    b_next = F(1, 16 * (n + 1)) + F(5, 128 * (n + 1) * (n + 1))
    return source_r_any_int(n) - source_r2_any_int(n) + 16 * b_n - b_next


def z2_mod(q, hex_digits):
    """Reduce a 2-adically integral Fraction q in Z_{(2)} modulo 16^hex_digits."""
    if type(hex_digits) is not int or hex_digits < 1:
        raise ValueError("positive hex_digits required")
    q = F(q)
    if q.denominator % 2 == 0:
        raise ValueError("q is not in Z_{(2)}: even reduced denominator")
    mod = 16 ** hex_digits
    return (q.numerator * pow(q.denominator, -1, mod)) % mod


def backward_2adic_section(z, hex_digits, r_func=source_r_any_int):
    """Compute U_2(z) = sum_{m=0}^{hex_digits-1} 16^m r_func(z - m) mod 16^hex_digits."""
    if type(z) is not int or type(hex_digits) is not int or hex_digits < 1:
        raise ValueError("integer z and positive hex_digits required")
    mod = 16 ** hex_digits
    total = 0
    for m in range(hex_digits):
        term = z2_mod(r_func(z - m), hex_digits - m)
        total = (total + (term << (4 * m))) % mod
    return total


# Exact 8x8 Octic CRT Partial-Fraction / Period Matrix M_inv:
# Maps monomial coefficients c = (c_1, ..., c_8)^T of Q(t) = sum_{a=1}^8 c_a t^{a-1} mod (16 - t^8)
# (where c_a = 8 * W_a(r) for the coboundary-invariant shift-orbit residues W_a(r))
# to (alpha_1, beta_1, alpha_2, beta_2, alpha_3, beta_3, alpha_4, beta_4)^T in:
# Q(t)/(16 - t^8) = (alpha_1 + beta_1 t)/(2 - t^2)
#                 + (alpha_2 + beta_2 t)/(t^2 + 2)
#                 + (alpha_3 + beta_3 (1 - t))/(t^2 - 2t + 2)
#                 + (alpha_4 + beta_4 (t + 1))/(t^2 + 2t + 2).
OCTIC_PARTIAL_FRACTION_MATRIX = (
    (F(1, 32), F(0), F(1, 16), F(0), F(1, 8), F(0), F(1, 4), F(0)),
    (F(0), F(1, 32), F(0), F(1, 16), F(0), F(1, 8), F(0), F(1, 4)),
    (F(1, 32), F(0), F(-1, 16), F(0), F(1, 8), F(0), F(-1, 4), F(0)),
    (F(0), F(1, 32), F(0), F(-1, 16), F(0), F(1, 8), F(0), F(-1, 4)),
    (F(1, 64), F(1, 32), F(1, 32), F(0), F(-1, 16), F(-1, 8), F(-1, 8), F(0)),
    (F(1, 64), F(0), F(-1, 32), F(-1, 16), F(-1, 16), F(0), F(1, 8), F(1, 4)),
    (F(1, 64), F(-1, 32), F(1, 32), F(0), F(-1, 16), F(1, 8), F(-1, 8), F(0)),
    (F(1, 64), F(0), F(-1, 32), F(1, 16), F(-1, 16), F(0), F(1, 8), F(-1, 4)),
)

# Canonical 8-slot vectors c = (c_1, ..., c_8) = 8 * (W_1, ..., W_8):
C_R1 = (F(4), F(0), F(0), F(-2), F(-1), F(-1), F(0), F(0))
C_R2 = (F(0), F(4), F(2), F(2), F(0), F(0), F(-1, 2), F(0))
C_ALPHA3 = (F(2), F(2), F(1), F(0), F(-1, 2), F(-1, 2), F(-1, 4), F(0))
C_NULL = (F(8), F(-8), F(-4), F(-8), F(-2), F(-2), F(1), F(0))


def octic_partial_fraction_coords(c_vec):
    """Apply OCTIC_PARTIAL_FRACTION_MATRIX to 8-vector c = 8 * W(r)."""
    if len(c_vec) != 8:
        raise ValueError("8-component vector required")
    c = tuple(F(x) for x in c_vec)
    return tuple(
        sum(row[j] * c[j] for j in range(8))
        for row in OCTIC_PARTIAL_FRACTION_MATRIX
    )


def octic_period_quotient(c_vec):
    """Return the 7-component Period Quotient P(r) and 1D Null Coordinate Pi_null(r).

    P(r) = (alpha_1, beta_1 + beta_3, alpha_2, beta_2, alpha_3, alpha_4, beta_4)
    Pi_null(r) = (beta_3 - beta_1) / 2.
    """
    a1, b1, a2, b2, a3, b3, a4, b4 = octic_partial_fraction_coords(c_vec)
    period_7 = (a1, b1 + b3, a2, b2, a3, a4, b4)
    pi_null = (b3 - b1) / 2
    return period_7, pi_null


def gaussian_octic_pi_character_from_W(w_vec):
    """Compute Omega_pi(r) = (1/2) sum_{a=1}^8 W_a(r) Im((1+i)^a).

    Weights Im((1+i)^a)/2 for a=1..8 are (1/2, 1, 1, 0, -2, -4, -4, 0).
    Equals 4 * (alpha_3(r) - alpha_4(r)), normalized so Omega_pi(r_1) = 1.
    """
    if len(w_vec) != 8:
        raise ValueError("8-component shift-orbit residue vector W required")
    weights = (F(1, 2), F(1), F(1), F(0), F(-2), F(-4), F(-4), F(0))
    return sum(w * F(val) for w, val in zip(weights, w_vec))


def _is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def terminal_uncollided_primes(N):
    """Return the four-class uncollided prime list P_N^* for horizon N >= 1.

    Each entry is (p, mod8_class, m_p, pole_coeff) where:
    - p in (4N, 8N-3] with p == 1 mod 8: m_p = (p+7)//8, pole_coeff = F(4)
    - p in (4N, 8N-3] with p == 5 mod 8: m_p = (p+3)//8, pole_coeff = F(-1)
    - p in (8N/3, 4N-1] with p == 3, 7 mod 8: m_p = (p+1)//4, pole_coeff = F(-1, 2)
    """
    if type(N) is not int or N < 1:
        raise ValueError("positive integer horizon N required")
    records = []
    for p in range(4 * N + 1, 8 * N - 2):
        if _is_prime(p):
            r8 = p % 8
            if r8 == 1:
                records.append((p, r8, (p + 7) // 8, F(4)))
            elif r8 == 5:
                records.append((p, r8, (p + 3) // 8, F(-1)))
    lo_37 = (8 * N) // 3 + 1
    for p in range(lo_37, 4 * N):
        if _is_prime(p):
            r8 = p % 8
            if r8 in (3, 7):
                records.append((p, r8, (p + 1) // 4, F(-1, 2)))
    return tuple(records)


def verify_terminal_prime_survival(N):
    """Verify exact p^1 || Q_N, residue formula, and absence of p == 3,7 mod 8 in (4N, 8N-3]."""
    u_n = U(N)
    num = u_n.numerator
    den = u_n.denominator
    records = terminal_uncollided_primes(N)
    for p, _r8, m_p, c_a in records:
        if den % p != 0 or den % (p * p) == 0:
            return False
        q_prime = den // p
        lhs = (num * pow(q_prime, -1, p)) % p
        c_mod = (c_a.numerator * pow(c_a.denominator, -1, p)) % p
        rhs = (c_mod * pow(16, N - m_p, p)) % p
        if lhs != rhs:
            return False
    # Also check that no prime p in (4N, 8N-3] with p == 3, 7 mod 8 divides Q_N
    for p in range(4 * N + 1, 8 * N - 2):
        if _is_prime(p) and (p % 8 in (3, 7)):
            if den % p == 0:
                return False
    return True


def octave_split_lcm(N):
    """Compute L_N = lcm({m <= 8N-3 : m == 1,5 mod 8} U {m <= 4N-1 : m == 3,7 mod 8})."""
    if type(N) is not int or N < 1:
        raise ValueError("positive integer horizon N required")
    val = 1
    for m in range(1, 8 * N - 2, 2):
        if (m % 8 in (1, 5)) or (m <= 4 * N - 1 and m % 8 in (3, 7)):
            val = (val * m) // gcd(val, m)
    return val


def adelic_carry_congruence_components(B):
    """Return (C_2B_mod, late_shell_2adic_mod, u_2B_2adic_mod) modulo 16^B."""
    if type(B) is not int or B < 1:
        raise ValueError("positive integer B required")
    u_2b = U(2 * B)
    mod = 16 ** B
    c_2b = u_2b.numerator // u_2b.denominator
    u_frac = u_2b - c_2b
    c_mod = c_2b % mod
    late_2adic = sum(
        (z2_mod(source_r_any_int(2 * B - m), B - m) << (4 * m)) % mod
        for m in range(B)
    ) % mod
    u_frac_2adic = z2_mod(u_frac, B)
    return c_mod, late_2adic, u_frac_2adic


def closed_form_borwein_autocorrelation(t):
    """Closed-form 3-branch piecewise quintic formula for K(t) = (L * L)(t) on T.

    Denominator is 11275335 = 5 * 3 * 9 * 289^2. Breakpoints on [0, 1/2] are 1/9 and 4/9.
    """
    d = torus(t)
    if d <= F(1, 9):
        num = (
            24576
            - 414720 * d ** 2
            + 933120 * d ** 3
            - 524880 * d ** 4
            - 118098 * d ** 5
        )
    elif d <= F(4, 9):
        num = (
            24574
            + 90 * d
            - 416340 * d ** 2
            + 947700 * d ** 3
            - 590490 * d ** 4
        )
    else:
        num = (
            65534
            - 368550 * d
            + 827820 * d ** 2
            - 918540 * d ** 3
            + 459270 * d ** 4
        )
    return num / BORWEIN_AUTOCORR_DENOM


def closed_form_borwein_energy(phases):
    """Compute exact V_B = int_T (J_hat_B(a) - ell_0)^2 da via the 3-branch polynomial."""
    ps = tuple(F(x) % 1 for x in phases)
    n = len(ps)
    if n < 1:
        raise ValueError("nonempty phases required")
    diag = n * F(24576, BORWEIN_AUTOCORR_DENOM)
    off = F(0)
    for i in range(n):
        pi = ps[i]
        for j in range(i + 1, n):
            off += closed_form_borwein_autocorrelation(pi - ps[j])
    return (diag + 2 * off) / (n * n) - HAAR_MEAN ** 2


def sharp_weyl_bound_from_energy(B, h, q=None):
    """Upgraded rational Weyl bound using SHARP_FOURIER_FLOOR = 5733/279752."""
    if type(h) is not int or h == 0:
        raise ValueError("nonzero harmonic integer required")
    v = original_energy(B)
    q = _rational_sqrt_upper(v) if q is None else F(q)
    if q < 0 or q * q < v:
        raise ValueError("q must certify sqrt(energy)")
    return min(F(1), F(h * h, 1) * (q + shadow_tail(B)) / SHARP_FOURIER_FLOOR)


def sharp_parseval_discrepancy_bound(B, H, q=None):
    """Upgraded Erdos-Turan discrepancy bound via Parseval + Cauchy-Schwarz.

    Wait: by Parseval on the true orbit,
      2 * sum_{h=1}^H |L_hat(h)|^2 |W_B(h)|^2 <= V_B^true <= (sqrt(V_B) + eps_B)^2.
    Using |L_hat(h)| >= c_*^sharp / h^2 and Cauchy-Schwarz on sum_{h=1}^H |W_B(h)| / h:
      sum_{h=1}^H |W_B(h)| / h
        <= sqrt(sum_{h=1}^H h^2) * sqrt(sum_{h=1}^H |W_B(h)|^2 / h^4)
        <= sqrt(H(H+1)(2H+1)/12) * (sqrt(V_B) + eps_B) / c_*^sharp.
    Improves ChatGPT's O(H^2 (sqrt(V_B)+eps_B)) bound to O(H^(3/2) (sqrt(V_B)+eps_B))
    and exponent 1/3 to 2/5.
    """
    if type(H) is not int or H < 1:
        raise ValueError("positive cutoff H required")
    v = original_energy(B)
    q = _rational_sqrt_upper(v) if q is None else F(q)
    if q < 0 or q * q < v:
        raise ValueError("q must certify sqrt(energy)")
    cs_sq = F(H * (H + 1) * (2 * H + 1), 12)
    cs_upper = _rational_sqrt_upper(cs_sq)
    return F(3, H + 1) + F(3, 1) * cs_upper * (q + shadow_tail(B)) / SHARP_FOURIER_FLOOR


def domain_wall_counts(u_val, B):
    """Compute (D_B, J_B) on the last B hexadecimal digits of floor(u_val) (TW-01)."""
    if type(B) is not int or B < 1:
        raise ValueError("positive integer B required")
    u_val = F(u_val)
    c_int = u_val.numerator // u_val.denominator
    # d_k is the k-th backward hex digit: floor(C / 16^(k-1)) mod 16 for k=1..B
    digits = [(c_int >> (4 * (k - 1))) & 0xF for k in range(1, B + 1)]
    d_b = sum(1 for d in digits if 1 <= d <= 14)
    j_b = sum(
        1
        for i in range(B - 1)
        if (digits[i], digits[i + 1]) in ((0, 15), (15, 0))
    )
    return d_b, j_b


def construct_adelic_crt_shadow(B):
    """Construct the ANC-12 Adelic CRT Shadow rational V_2B^sharp for shell B >= 2.

    For B >= 2, Q_2B = den(U_2B(0)) factors into the uncollided prime product
    Pi_2B^* = prod_{p in P_2B^*} p and the collided odd cofactor Q_coll = Q_2B // Pi_2B^*.
    Wait: to zero out C_2B^sharp mod 16^B while keeping:
      (1) exact denominator Q_2B,
      (2) exact uncollided prime residues V_2B^sharp == U_2B(0) mod p Z_{(p)} for all p in P_2B^*,
      (3) exact 2-adic late-shell congruence V_2B^sharp == U_2B(0) mod 16^B Z_{(2)},
    we set C_2B^sharp = C_2B - (C_2B mod 16^B) + 16^B * k_shift, where k_shift is chosen
    so that the numerator N_sharp = C_2B^sharp * Q_2B + R_sharp satisfies both:
      N_sharp == N_2B (mod Pi_2B^*)  and  0 < R_sharp < Q_2B  with gcd(R_sharp, Q_2B) == 1
    or simply construct V_2B^sharp = (C_2B - (C_2B mod 16^B)) + u_2B + delta_crt.
    Wait: if we keep the EXACT numerator residue R_2B = N_2B mod Q_2B (which automatically
    preserves Q_2B and EVERY odd-prime residue mod Q_2B, including all p in P_2B^*!),
    changing C_2B to C_2B^sharp = C_2B - (C_2B mod 16^B) shifts V_2B by -(C_2B mod 16^B)
    (which alters V_2B mod 16^B Z_{(2)}).
    Conversely, if we also preserve V_2B^sharp == U_2B(0) mod 16^B Z_{(2)} AND C_2B^sharp == 0 mod 16^B,
    then R_sharp = N_sharp mod Q_2B must satisfy:
      R_sharp == N_2B (mod 16^B)  AND  R_sharp == N_2B (mod Pi_2B^*).
    Since gcd(16^B, Pi_2B^*) == 1, by CRT there is a unique residue class
      R_0 in [0, 16^B * Pi_2B^* - 1]
    satisfying both congruences! Whenever 16^B * Pi_2B^* <= Q_2B (or by adding multiples),
    R_0 lies strictly inside [0, Q_2B - 1], giving a fractional part u_sharp = R_0 / Q_2B in [0, 1)!
    """
    if type(B) is not int or B < 1:
        raise ValueError("positive integer B required")
    u_2b = U(2 * B)
    n_2b = u_2b.numerator
    q_2b = u_2b.denominator
    c_2b = n_2b // q_2b
    mod_2 = 16 ** B
    records = terminal_uncollided_primes(2 * B)
    pi_star = 1
    for p, *_ in records:
        pi_star *= p
    # CRT combine x == n_2b (mod mod_2) and x == n_2b (mod pi_star)
    # Wait: since BOTH congruences have target n_2b, n_2b itself satisfies both!
    # So the general solution is R_sharp = (n_2b % (mod_2 * pi_star)) + t * (mod_2 * pi_star)!
    modulus = mod_2 * pi_star
    r_sharp = n_2b % modulus
    # Then C_sharp = (n_2b - r_sharp) // modulus * pi_star has C_sharp * q_2b + r_sharp:
    # We want V_sharp = C_sharp + r_sharp / q_2b with C_sharp == 0 (mod 16^B)
    # and V_sharp == U_2B (mod 16^B Z_{(2)}) and q_2b * V_sharp == n_2b (mod pi_star)!
    # Check: V_sharp = r_sharp / q_2b (so C_sharp = 0, provided 0 <= r_sharp < q_2b):
    # Wait: for V_sharp = r_sharp / q_2b to satisfy V_sharp == U_2B (mod 16^B Z_{(2)}),
    # we need r_sharp == q_2b * U_2B = n_2b (mod 16^B), which holds by definition of r_sharp!
    # And for q_2b * V_sharp == n_2b (mod pi_star), we need r_sharp == n_2b (mod pi_star),
    # which ALSO holds by definition of r_sharp = n_2b % (16^B * pi_star)!
    # And if r_sharp < q_2b (which holds whenever 16^B * pi_star <= q_2b, i.e. for all B >= 3!),
    # then floor(V_sharp) = 0, so C_sharp = 0, D_B = J_B = 0, and R_B(V_sharp) < 1/(255 B)!
    c_high = (c_2b >> (4 * B)) << (4 * B)
    v_sharp = F(c_high, 1) + F(r_sharp, q_2b)
    return {
        "B": B,
        "Q_2B": q_2b,
        "Pi_2B_star": pi_star,
        "Q_coll": q_2b // pi_star,
        "mod_2_times_Pi_star": modulus,
        "fits_in_single_unit_interval": r_sharp < q_2b,
        "V_sharp": v_sharp,
    }
