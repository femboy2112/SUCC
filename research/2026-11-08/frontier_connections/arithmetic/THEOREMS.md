# Parabola tomography and the full mixed-quadratic budget

**Status:** PAPER PROVED for MQ1–MQ5; certified finite source application in
[the receipt](MIXED_QUADRATIC_1103.json). The identities are classical finite
Fourier/restriction/phase-retrieval mathematics, applied here to the exact
folded BBP complement. Worldwide novelty is not claimed. None is an
original-zero signed decay theorem.

Fix an odd prime p, a nonempty set S⊆F_p of size m, and arbitrary complex
B(x), extended by zero off S. Put

    C(a,b) = (1/m) sum_(x in S) B(x) e_p(-a x²-b x),
    E = (1/m) sum |B(x)|²,     F4 = sum |B(x)|⁴.

For the SUCC clean clock, S=xi<16>, B is the authenticated folded complement
at a fixed nonzero integer frequency h. Then C(0,-h)=W, the actual signed
mean. This exact identity retains the complementary phase; no seed ensemble
or independent replacement is made.

## MQ1. Exact second and fourth moments, with a phase-blindness obstruction

For every a∈F_p,

    sum_b |C(a,b)|² = p E/m.

Over the complete two-dimensional menu,

    sum_(a,b) |C(a,b)|⁴ = (p²/m⁴)(2m²E²-F4).          (MQ1)

Consequently the number of coefficients with |C(a,b)|≥τ>0 is at most

    p²(2m²E²-F4)/(m⁴ τ⁴).

**Proof.** Additive-character orthogonality in b gives the second moment.
For the fourth, expanding the four factors and summing a,b leaves exactly

    x1+x2=x3+x4,   x1²+x2²=x3²+x4².

Since 2 is invertible, the sums and products of the two pairs agree. Thus
{x1,x2}={x3,x4} as multisets. The two permutations contribute twice the
square of sum|B|²; x1=x2 was counted twice and must be subtracted once.
This proves the identity, and the threshold count follows by positivity. QED.

**Boundary.** Both moments depend only on the magnitudes |B(x)|. They are
unchanged by arbitrary independently chosen phase rotations at the points.
In particular, B(x)=e_p(-h x) has |W|=1 and exactly the same global moment
values as every other unit-valued B on the same S. The small *fraction* of
large coefficients furnished by MQ1 cannot exclude the one selected
coefficient C(0,-h). This is an explicit counterexample to converting average
parabola curvature/restriction control into original-zero cancellation.
There is also an amplitude-matched control for every actual B:
`B_coh(x)=|B(x)|e_p(-h x)` has exactly the same E,F4 and all pointwise
magnitudes, but `W_coh=mean|B|>=E` when |B|<=1. Thus even learning the
entire amplitude profile cannot supply signed cancellation. These arbitrary
B controls are mathematical observer controls, not claimed alternative
authentic zero-BBP histories.

Characteristic 2 is excluded essentially: S=F_2,B=1 has weighted pair
collision count8, while the displayed odd-characteristic diagonal formula
would give6.

**Classical provenance.** Mockenhaupt–Tao, *Restriction and Kakeya phenomena
for finite fields*, §5 Lemma5.1 and the polynomial-curve discussion establish
the corresponding even-moment collision method. Their n=2 dimensional curve
is the parabola here. We give the exact weighted diagonal correction needed
by this application, without importing any unresolved restriction conjecture.
[Original paper](https://arxiv.org/pdf/math/0204234).

## MQ1b. The same phase-blindness holds at every polynomial degree

For integer D>=1 with p>D, define

    C_D(a1,...,aD)=mean_S B(x)e_p(-sum_(j=1)^D aj x^j).

Then exactly

    sum_(a in F_p^D) |C_D(a)|^(2D)
      = (p^D/m^(2D)) sum_(k:S->N, sum k=D)
          [D!/product_x k(x)!]^2 product_x |B(x)|^(2k(x)).

**Proof.** Character orthogonality makes the first D power sums of two
ordered D-tuples agree. Since 1,...,D are invertible in F_p, Newton's
identities determine all elementary symmetric polynomials; the tuples are
the same multiset. A multiset with multiplicity vector k has
D!/product k! orderings on each side. The product of B-values and their
conjugates is the displayed product of magnitudes. QED.

This is the exact weighted moment-curve version of the same classical
Mockenhaupt–Tao §5 argument, not a new restriction result. It shows that
merely enlarging the polynomial dictionary and averaging its critical even
moment still discards every pointwise phase. Higher degree does not repair
that particular loss of source-selected information. It does not assert
that every spectral statistic or every higher moment is phase-blind.

## MQ2. Retaining the complete intensity chart recovers signed cross terms

Let J(a,b)=|C(a,b)|² and

    Jhat(s,t) = (1/p²) sum_(a,b) J(a,b)e_p(a s+b t).

For t≠0, put x=(s/t+t)/2 and y=(s/t-t)/2 in F_p. Then

    Jhat(s,t) = B(x) conjugate(B(y))/m².             (MQ2)

At t=0, Jhat(0,0)=E/m and Jhat(s,0)=0 for s≠0.

**Proof.** Expand |C|² and sum characters. The surviving equations are
x-y=t and x²-y²=s. For t≠0 they uniquely solve to the indicated x,y.
For t=0 only x=y and s=0 survive. QED.

If B has at least three nonzero entries, the full intensity chart determines
B up to one common phase. Its off-diagonal products identify the nonzero
support and determine each diagonal through

    |B(x)|² = |K(x,y) K(x,z)/K(y,z)|,
    K(x,y)=B(x)conjugate(B(y)),

where x,y,z are distinct nonzero-support points. Choose one B(x) positive
real to recover the others from K. With only one nonzero entry, its position
is invisible; with two, interchanging the two magnitudes can preserve the
cross product and total energy. Thus the rank/support premise is essential.

**Interpretation.** Averaging all intensities to one or two energy scalars
throws away the phase information that the labeled two-dimensional chart
retains. This supplies a precise observer-memory connection, not a
normality theorem: the target intensity J(0,-h)=|W|² was already one of the
measurements. Tomographic invertibility does not make that measurement small.
The matrix K is positive semidefinite rank one by construction; PSD alone
does not force its pairing with the coherent target to vanish.

The complete quadratic bases on F_p also give the classical prime-dimensional
mutually unbiased construction: within fixed a they are orthogonal; between
distinct a their normalized overlap has magnitude1/sqrt(p), by the elementary
quadratic Gauss sum. This is a mathematical measurement-design connection,
not physical quantum dynamics, Born-rule inference, or a computational
quantum speedup. Restricting those bases to S destroys exact orthogonality,
so one must use SUCC's actual subgroup bounds instead of importing full-field
frame constants. [Wootters–Fields original paper](https://doi.org/10.1016/0003-4916(89)90322-9).

## MQ3. Lawful affine chart transport and the limitation of invariant summaries

For u≠0 and v,c,d,e∈F_p, let S'=uS+v and

    B'(y)=e_p(c y²+d y+e) B((y-v)/u).

A change of variables gives exactly

    C'(a,b)= e_p((c-a)v²+(d-b)v+e)
             C((a-c)u², u[b-d+2(a-c)v]).             (MQ3)

Thus the labeled intensity chart transports by the displayed permutation.
The multiset of intensities, its maximum and its global moments are invariant.
A linear phase twist shifts the target coefficient within this chart.
Therefore an invariant summary cannot distinguish where the source-selected
resonance sits. If the observer changes coordinates, it must transport the
source label and target label as well. For a subgroup coset and c≠0, the controls `B0=e_p(-h x)` and
`B1=e_p((c-h)x)` therefore have the same *entire unordered* intensity
multiset, while their target magnitudes are respectively1 and at most
min(1,sqrt(p)/m). This makes the lost source/target label a quantified
obstruction even when the observer retains more than global moments.
The formula authorizes a change of observation chart only; it does not authorize changing the BBP source or
claiming that B's actual temporal evolution is a quadratic twist.

## MQ4. The full quadratic dictionary has the same CB1 dual certificate

Assume now m>2, S=xi<16>, and |B|≤1. Let

    phi_(a,b)(x)=e_p(a x²+b x),
    w_(a,b)=min(1,sqrt(p)/m)             if a=0,b≠-h,
            min(1,2sqrt(p)/m)           if a≠0.

The only omitted pair is (0,-h), the resonant atom r=e_p(-h x).
These weights are valid PR8 arithmetic bounds, since hX+aX²+bX has degree
one or two and degree<m. An arbitrary constant polynomial term is absorbed
in the coefficient. Define

    M = max_(a,b)!=(0,-h) |C(a,b)|/w_(a,b).

For every complex R, arbitrary complex coefficients c_(a,b), and
V=Rr+sum c_(a,b)phi_(a,b), set rho=mean_S|B-V|. The existing CB1 proof gives

    rho + sum w_(a,b)|c_(a,b)|
       >= (E-|W|²)/(max(1,M)+|W|).                  (MQ4)

Thus a certified upper bound on all p²-1 nonresonant correlations gives a
bound on the entire mixed-quadratic model class, including dense adaptive
fits and an unrestricted resonant coefficient. This uses the ORIGINAL
atom-by-atom PR8 budget. It does not rule out an improved budget that keeps
cancellation between coefficients before taking absolute values, nor any
higher-degree dictionary. The finite floor is not an asymptotic lower bound.

## MQ5. A direct integer contraction certificate, independent of the FFT

The inherited exact source boxes and rational Taylor root-of-unity enclosures
are quantized to Gaussian integer centers with denominator Q=2^26. Suppose
B's common complex L1 radius is R_B/Q; each root's is T/Q. Let C_B be the
maximum center L1 numerator. Multiplication by the quadratic root, followed
by coordinatewise downward rounding to denominator Q, gives radius

    R_P/Q,  R_P=2R_B+ceil(T C_B/Q)+2.

Indeed, the exact root has L1 norm≤2. Split the product difference into the
root times B's error and the root's error times B's center; rounding two
coordinates costs less than2/Q. Let C_P be the maximum product-center L1
numerator and C_R the maximum root-center L1 numerator.

For every a,b, the integer matrix contractions compute the real and imaginary
center sums exactly with denominator m Q². Their error has common L1 bound

    epsilon = 2R_P/Q + T C_P/Q².                    (MQ5)

The argument is the same split, this time leaving the final products at
exact denominator Q² and averaging over m terms. Since each individual
complex product has L1 norm≤C_P C_R, the explicit check

    m C_P C_R < 2^63-1

bounds every matrix-contraction partial sum, every intermediate coordinate
sum/difference and final L1 norm, preventing signed-int64 overflow. The
input multiplication is separately checked by C_B C_R<2^63-1. Modular index
products and array dimensions are bounded by the finite source parameters.
The implementation executes these checks before every block contraction.

For the linear row, Python arbitrary-precision squares and integer square
roots give its maximum modulus upper bound. Over all a≠0 rows, we use the
larger exact maximum L1 center norm plus epsilon. This is deliberately a
valid nonsharp upper bound, never mislabeled an exact modulus maximum.
All final weights, M and MQ4 floors use rational outward arithmetic.

This instrument shares the original source receipts and Taylor phase
primitive with prior work. Its independent contribution is the full-menu
integer matrix algorithm, its explicit error/range proof, and direct phase
checks at both reported extrema and preregistered coefficient pairs.
