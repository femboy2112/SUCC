"""Source-grounded finite Omega/Haar -> unitary quantum toy model.

All arithmetic BBP data is delegated to the audited omega_haar.py sibling.
Complex amplitudes are finite Hilbert-space simulations, NOT claims of
physical hardware, speedup, MERA, parity cancellation, or pi normality.
The exact orientation witness uses fractions before float conversion.
"""

from __future__ import annotations

from cmath import exp, pi
from fractions import Fraction
from math import cos, sin, sqrt

from omega_haar import (Q, block_forcing, commutator, energy,
                        grouped_fold, source, source_block)


GAMMA = sqrt(2) / 3


def _dyadic_length(n: int) -> None:
    if n < 2 or (n & (n - 1)):
        raise ValueError("signal length must be a power of two >= 2")


def haar_analyze(data: tuple[complex, ...]) -> tuple[complex, ...]:
    """N-dimensional orthonormal multiscale Haar, ordered coarse -> details.

    It is NOT the same operator as a Walsh H^{tensor m} transform.
    """
    _dyadic_length(len(data))
    arr = list(data)
    details = []
    while len(arr) > 1:
        coarse, fine = [], []
        for i in range(0, len(arr), 2):
            coarse.append((arr[i] + arr[i+1]) / sqrt(2))
            fine.append((arr[i] - arr[i+1]) / sqrt(2))
        details.append(fine)
        arr = coarse
    return tuple(arr + [v for level in reversed(details) for v in level])


def haar_synthesize(coeffs: tuple[complex, ...]) -> tuple[complex, ...]:
    _dyadic_length(len(coeffs))
    arr = list(coeffs[:1])
    pos = 1
    while len(arr) < len(coeffs):
        fine = coeffs[pos:pos + len(arr)]
        if len(fine) != len(arr):
            raise ValueError("malformed Haar coefficient array")
        out = []
        for a, d in zip(arr, fine):
            out.extend(((a + d) / sqrt(2), (a - d) / sqrt(2)))
        pos += len(arr)
        arr = out
    return tuple(arr)


def walsh_hadamard(data: tuple[complex, ...]) -> tuple[complex, ...]:
    """H^{tensor m} on a length-2^m amplitude register."""
    _dyadic_length(len(data))
    out = list(data)
    half = 1
    while half < len(out):
        for start in range(0, len(out), 2*half):
            for j in range(half):
                a, b = out[start+j], out[start+j+half]
                out[start+j], out[start+j+half] = ((a+b)/sqrt(2), (a-b)/sqrt(2))
        half *= 2
    return tuple(out)


def group_butterfly(data: tuple[complex, ...], group: int, inverse=False) -> tuple[complex, ...]:
    """Orthogonal analysis/synthesis on chronological 2- and 3-blocks.

    Group=3 requires a three-dimensional orthogonal butterfly, not a
    single-qubit H. Both preserve detail slots; no projection occurs.
    """
    if group not in (2, 3) or len(data) % group:
        raise ValueError("requires a multiple of group=2 or 3")
    if group == 2:
        mat = ((1/sqrt(2), 1/sqrt(2)), (1/sqrt(2), -1/sqrt(2)))
    else:
        mat = ((1/sqrt(3), 1/sqrt(3), 1/sqrt(3)),
               (1/sqrt(2), -1/sqrt(2), 0.),
               (1/sqrt(6), 1/sqrt(6), -2/sqrt(6)))
    if inverse:
        mat = tuple(tuple(mat[j][i] for j in range(group)) for i in range(group))
    out = []
    for offset in range(0, len(data), group):
        chunk = data[offset:offset+group]
        out.extend(sum((m*v for m,v in zip(row,chunk)), 0j) for row in mat)
    return tuple(out)


def projected_by_measurement(data: tuple[complex, ...], group: int) -> tuple[complex, ...]:
    """Postselected (unnormalized) low-pass component U^* Π U.

    Deliberately nonunitary and not a trace-preserving quantum channel.
    """
    a = list(group_butterfly(data, group))
    for i in range(len(a)):
        if i % group:
            a[i] = 0j
    return group_butterfly(tuple(a), group, inverse=True)


def skew_exp_rotation(data: tuple[float, ...], time: float) -> tuple[float, ...]:
    """exp(time*C) in R^6, with C=[P2,P3], gamma=sqrt(2)/3.

    C is real skew-adjoint; exp(time*C) is a real orthogonal/unitary gate.
    On the 2D active plane this is an ordinary rotation.
    """
    if len(data) != 6:
        raise ValueError("expected six amplitudes")
    cv = tuple(float(x) for x in commutator(data))
    ccv = tuple(float(x) for x in commutator(cv))
    a, b = sin(GAMMA*time)/GAMMA, (1-cos(GAMMA*time)) / GAMMA**2
    return tuple(float(x)+a*c+b*cc for x,c,cc in zip(data,cv,ccv))


def chirality_exact(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> Fraction:
    """Expected value of sigma_y tensor (i C) on |0,a>+|1,b>.

    With the concatenated real vector normalized to unit 2-norm, the exact
    quantum expectation is 2<a,Cb>/(||a||^2+||b||^2).
    No nonzero one-window expectation is possible for real a since C*=-C.
    """
    if len(a) != 6 or len(b) != 6:
        raise ValueError("expected six-dimensional vectors")
    denom = energy(a) + energy(b)
    if not denom:
        raise ValueError("zero state")
    area = sum((x*y for x,y in zip(a,commutator(b))),Fraction())
    return 2*area/denom


def chirality_matrix() -> tuple[tuple[complex, ...], ...]:
    """12x12 Hermitian observable sigma_y tensor i[P2,P3]."""
    columns = [commutator(tuple(Fraction(int(i==j)) for i in range(6))) for j in range(6)]
    c = [[complex(columns[j][i]) for j in range(6)] for i in range(6)]
    # sigma_y tensor iC = [[0, C], [-C, 0]], real symmetric because C^T=-C.
    return tuple(tuple((0j if (i < 6) == (j < 6) else
                        (c[i][j-6] if i<6 else -c[i-6][j]))
                       for j in range(12)) for i in range(12))


def chirality_direct(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> float:
    """Independent direct 12x12 matrix contraction for calibrated finite data."""
    vals = tuple(float(x) for x in a+b)
    denom = sum(x*x for x in vals)
    if not denom:
        raise ValueError("zero state")
    mat = chirality_matrix()
    return (sum(vals[i]*mat[i][j]*vals[j] for i in range(12) for j in range(12))/denom).real


def source_chirality(n: int, *, mutate=False) -> Fraction:
    return chirality_exact(source_block(n, mutate=mutate),source_block(n+1, mutate=mutate))


def parity_character_state() -> tuple[float, ...]:
    """The parity character is H^4|0001>, with LSB at right."""
    return tuple(float(z.real) for z in walsh_hadamard(tuple(1.+0j if k==1 else 0j
                                                             for k in range(16))))


def fiber_parity_overlap(values: tuple[complex, ...]) -> complex:
    """<chi_8|v> for 16 raw amplitudes; equals 4 times H_8(v)."""
    if len(values) != 16:
        raise ValueError("requires all sixteen inverse branches")
    chi = parity_character_state()
    return sum(chi[k]*values[k] for k in range(16))


def bbp_prefix(horizon: int) -> Fraction:
    if horizon < 1:
        raise ValueError("horizon>=1")
    return sum((Q**(j+1) * source(j) for j in range(horizon)),Fraction())


def circle_fraction(value: Fraction) -> Fraction:
    return value - value.numerator // value.denominator


def exact_rational_phase_state(A: int, L: int, h: int, *, seed=Fraction(0)) -> tuple[complex,...]:
    """Finite-phase oracle state for n in [A,2A), using one common BBP horizon L.

    It is a mathematical amplitude model; no efficient quantum state-preparation
    circuit and no exact pi oracle are provided. Original zero seed is default.
    """
    _dyadic_length(A)
    if L < 2*A or not isinstance(seed,Fraction) or not isinstance(h,int):
        raise ValueError("L >= 2A, rational seed and integer frequency required")
    p = bbp_prefix(L)
    out=[]
    for n in range(A,2*A):
        phase = circle_fraction((16**n)*(seed+p)*h)
        out.append(exp(2j*pi*float(phase))/sqrt(A))
    return tuple(out)


def weyl_mean_and_zero_probability(state: tuple[complex,...]) -> tuple[complex, float]:
    """With state preloaded, H^m's zero-outcome probability is |Weyl mean|^2."""
    _dyadic_length(len(state))
    mean = sum(state)/sqrt(len(state))
    circuit = walsh_hadamard(state)
    return mean, abs(circuit[0])**2


def completed_phase_tail_bound(L: int, n: int) -> Fraction:
    """Strict upper bound for 16^n(P_infinity-P_L), L>=1, n>=0.

    R(j)=integral x^(8j) P(x), with
    0<=P(x)=(1-x)(x^2+2)(x^2+2x+2)<=15(1-x).
    Therefore R(j)<15/((8j+1)(8j+2)), and geometric summation gives
       0 < 16^n(P_inf-P_L) < 16^(n-L)/((8L+1)(8L+2)).
    This is a *strict analytic certificate*, not a floating-point interval.
    """
    if L < 1 or n < 0:
        raise ValueError("L>=1 and n>=0")
    return Fraction(16)**(n-L) / ((8*L+1)*(8*L+2))


def finite_phase_mean_error_bound(A: int, L: int, h: int) -> Fraction:
    """Bound on |mean(e(h Y_n))-mean(e(h Z_n,L))|, n in [A,2A).

    The rational upper bound uses 2*pi < 44/7 and avoids float underflow.
    For h fixed and L=2A this is O(h/A^2). It does NOT control
    discontinuous digit indicators without a boundary-strip certificate.
    """
    _dyadic_length(A)
    if L < 2*A or not isinstance(h,int):
        raise ValueError("L>=2A and h integer")
    return Fraction(44, 7) * abs(h) * completed_phase_tail_bound(L, 2*A-1)


def finite_hadamard_probability_error_bound(A: int, L: int, h: int) -> Fraction:
    """|Pr(0...0)exact - Pr(0...0)prefix| <= 2*mean phase error."""
    return min(Fraction(1), 2*finite_phase_mean_error_bound(A,L,h))


def coarse_instrument_isometry(data: tuple[complex,...], group: int):
    """One-ancilla isometry |0>P|x> + |1>(I-P)|x>.

    Returns two *unnormalized coherent branches*. Both are required for an
    invertible embedding. Measuring/ignoring the ancilla loses coherence.
    """
    low = projected_by_measurement(data,group)
    detail = tuple(x-y for x,y in zip(data,low))
    return low,detail


def heralded_minus_probability(values: tuple[Fraction,...]) -> Fraction:
    """Unconditional minus-port probability of the two-route heralded echo.

    Begin with |+> (v/||v||), apply low-pass P2P3 on arm 0 and P3P2 on
    arm 1, retaining loss in environment flags and postselecting success.
    Hadamard on the path qubit yields minus amplitude C v/(2||v||).
    """
    if len(values)!=6 or energy(values)==0:
        raise ValueError("six nonzero amplitudes required")
    return energy(commutator(values))/(4*energy(values))


def chirality_evolve(state: tuple[complex,...], time: float) -> tuple[complex,...]:
    """Explicit 12x12 unitary exp(-it sigma_y tensor iC).

    Uses the exact minimal polynomial H^3=(2/9)H. Can be padded by four
    inert basis states to act on four address/control qubits (dim 16).
    """
    if len(state)!=12:
        raise ValueError("state must have 12 amplitudes")
    mat=chirality_matrix()
    def op(x):
        return tuple(sum((mat[i][j]*x[j] for j in range(12)),0j) for i in range(12))
    hy=op(state)
    hhy=op(hy)
    a=(cos(GAMMA*time)-1)/GAMMA**2
    b=-1j*sin(GAMMA*time)/GAMMA
    return tuple(state[i]+a*hhy[i]+b*hy[i] for i in range(12))


def branch_character_state(m: int) -> tuple[complex,...]:
    """Unit 4-qubit character eigenstate |chi_m> of branch increment mod 16."""
    return tuple(exp(2j*pi*(m%16)*k/16)/4 for k in range(16))


def branch_increment(state: tuple[complex,...]) -> tuple[complex,...]:
    """Unitary S|k>=|k+1 mod16>; 4-bit reversible add-one operation."""
    if len(state)!=16:
        raise ValueError("requires four-qubit, 16-dimensional branch register")
    return tuple(state[(k-1)%16] for k in range(16))


def controlled_increment_minus_probability(state: tuple[complex,...]) -> float:
    """Control S by path qubit initialized |+>, then H and measure |- >.

    Exact expression: ||(I-S)|psi>||^2/4. A character eigenstate
    with m=8 gives one, with m=0 gives zero. Not a pi-digit statistic.
    """
    shifted=branch_increment(state)
    return sum(abs(x-y)**2 for x,y in zip(state,shifted))/4


def chirality_second_moment(a: tuple[Fraction,...], b: tuple[Fraction,...]) -> Fraction:
    """<sigma_y tensor iC squared> = (||Ca||²+||Cb||²)/total norm²."""
    denom=energy(a)+energy(b)
    if len(a)!=6 or len(b)!=6 or not denom:
        raise ValueError("two nonzero six-entry history windows required")
    return (energy(commutator(a))+energy(commutator(b)))/denom


def controlled_increment_gate_schedule(control: int, k: int) -> int:
    """Boolean truth-table for the 4-,3-,2-,1-control X schedule in CIRCUIT.qasm.

    Apply target bits from high to low so each carry test uses original
    lower bits. No unknown quantum state is copied or deleted.
    """
    if control not in (0,1) or not (0 <= k < 16):
        raise ValueError("control bit and four-bit branch label required")
    bits=[(k>>i)&1 for i in range(4)]
    for target in (3,2,1,0):
        if control and all(bits[i] for i in range(target)):
            bits[target] ^= 1
    return sum(bit<<i for i,bit in enumerate(bits))
