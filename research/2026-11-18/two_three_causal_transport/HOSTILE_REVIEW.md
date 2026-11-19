# Hostile review: causal memory, cyclic source filters, and exact probes

**Verdict:** the reviewed formulas and stated domains survived the checks
below. No all-shell signed estimate, normality proof, positive-integer Collatz
termination proof, or RH implication has been established. This review is an
additional same-model bearing with separately entered calculations; it is not
an independent mathematical referee or a formal proof-assistant certificate.

## Scope inspected

* `CYCLIC_SOURCE_FILTERS.md`, sections1–8.
* `BBP_CAUSAL_MEMORY.md`, including the compact modulus-9 height proof.
* `COLLATZ_INTERFACE.md` and the inherited joint-local-clock boundary.
* `probe.py` and `tests/test_bbp_two_three_causal_transport.py` as present at
  review time: the integrated probe had eight focused unittest cases.

The reviewer did not modify those files or run the repository-wide suite.
The root agent owns the suite and its separately scoped validation receipt.

## 1. Formula and type audit

### Cyclic source filter

Checked the literal factorization

`Q=(1-t)H`, `H=4+4t+4t²+2t³+t⁴=(t²+2)(t²+2t+2)`.

The determinant proof correctly uses all m-th roots for the cyclic matrix,
with the odd/even distinction for squaring roots. Its positivity and oddness
are valid for every m>=1. The direct reduction `H(S_m)=S_m^4 mod2` supplies
the all-size binary invertibility and maximum-norm isometry independently of
the explicit determinant expression.

The displayed polynomial inverses for m3 and m5 are exact. Because their
matrix numerators are the adjugates and the gcd of their entries is one, the
Smith argument using the penultimate determinantal divisor is valid. The
inverse precision costs are sharp: the cited primitive numerator columns
produce nonzero input residues whose outputs vanish to the claimed prime
depth. The interpretation is worst-case precision for the declared channel
map, not a probabilistic claim about the actual orbit.

The prime11 null vector has the correct orientation for the declared
`S e_j=e_(j+1)` convention. The Gram eigenvalues, constant eigenvalue225,
augmentation H-determinant 55, and factor norms11 and5 are consistent. The
failure at m3 of the proposed universal Fibonacci determinant law is an exact
counterexample. CRT identifies paired-clock state spaces but supplies no
independence assertion.

### Finite causal versus cyclic operators

For zero-prehistory `L_N`, triangularity gives determinant `4^N` for H and Q.
Their inverses are integral at every odd prime. At2 the reductions are
`L_N^4` and `L_N^4(I+L_N)`; since the latter factor is invertible and commutes
with L_N, both ranks and kernels stated in CSF-04 are correct.

The record interpretation is carefully scoped: cyclic wraparound can replace
a genuine delay with a permutation, but neither operation creates real-circle
normality. Invertibility of `I-L_N` versus the constant-vector kernel of
`I-S_m` is exact. The inverse-polynomial residual under a general shift has
the correct sign and degree8, and is not confined to the starting boundary.

The manuscript distinguishes Mellin exponent increments from chronological
BBP increments: the latter multiply by `t^8`, not t. This distinction is
load-bearing; a polynomial identity on the one-unit exponent subclock is not
automatically an identity on chronological BBP states.

Two narrow wording refinements were sent to the root agent:

1. A descending finite Mellin record represents exponent shift by backshift
   in its interior; its missing boundary moments must be retained explicitly
   for an exact full-record identification.
2. The invisible input count in a prefix of length N is `min(N,4)`, so prose
   saying “four most recent input bits” should qualify N>=4.

These are boundary clarifications, not failures of the displayed rank theorem.

### BBP source height and moving window

The height table's first two rows follow from the q,4q,5q raw pole entries.
Its cancellation row genuinely requires modulus9. The eight stated
contributions exhaust the admitted raw denominators between the given
endpoints. Their sum6 mod9, multiplied by16^n, remains6 mod9. The first
odd-depth denominator is2·3^k at the stated arrival time; the earlier
discarded formula is correctly recorded as false.

The exact identity `U_n-V_(n,L)=16^L U_(n-L)` correctly retains the incoming
state. It proves contraction at2 and retention at3. The zero-boundary case
L=n is explicitly separate. The lower bound `d3(U_t)>(4/9)t`, upper bound8t,
and relative error bound `epsilon/18` have the correct inequality directions.
The statement only refutes a zero-initialized recent-window reconstruction;
it explicitly permits a compressed boundary register or present recomputation
of that state.

### Collatz chronology

The odd-positive domain prevents zero-valuation exceptions. The cylinder
formula and the proof of intermediate legality preserve exact valuations,
not merely divisibility. The last-m ternary-memory law is stated only for
1<=m<=k. Its ordered-word counterexample uses legal positive integer paths.
The prefix-length sharpness proof is separate from the minimal finite output
register count. The 3-adic register requires the source's externally supplied
valuation word; no intrinsic v2 operation on Q3 is assumed.

The conditional Haar ensemble is not substituted for a chosen positive
integer. The all-ones word's negative 2-adic limit is a valid warning against
lifting finite positive realizability to a positive infinite realization.

## 2. Fresh original-source holdout through n=100000

The review used an independently entered integer modular implementation. It
did not import `probe.py`, the proposed height function, or a stored BBP state
table. Starting from zero, it used the four raw fractions with coefficients
`(4,-2,-1,-1)` and offsets `(7,4,3,2)`.

For N=100000, every raw denominator is at most8N and has ternary depth at most
K=12. The computation maintains

`z_n = 3^K U_n mod 3^(K+3)`,

with modulus `14348907`. If `8n-f=3^v d` with3 not dividing d, that source
term contributes

`s 3^(K-v) d^(-1) mod 3^(K+3)`.

Thus no rational reduction or floating-point arithmetic is needed. The
working precision contains enough extra ternary digits to check every
displayed unit and mod9 certificate after rescaling. Every nonzero residue's
valuation is below the working precision, so no zero residue was mistaken
for an exact valuation.

**Executed results:** all99232 indices769<=n<=100000 passed:

* Exact height against all four interval rows.
* The row-specific mod3 or mod9 residue.
* `d3(U_n)>=3`, `(4/9)n<d3(U_n)<=8n`.
* Every first-depth arrival reached within the run.

| Height-table row | Fresh checked indices |
|---|---:|
|1|58173|
|2|8201|
|3|8201|
|4|24657|

First depth arrivals found were

`{1:1,2:2,3:7,4:11,5:61,6:92,7:547,8:821,9:4921,10:7382,11:44287,12:66431}`.

The SHA256 of UTF-8 lines `n:z_n:d3(U_n):row\n` over the fresh holdout is

`e0811bbadd6390808344b197211f12e078535ed244ab7fc0d0adcd3473dff07e`.

This is a finite receipt corroborating the general proof. It does not itself
establish a universal theorem or any real-circle behavior.

### Reproduction of the holdout receipt

```python
from collections import Counter
from hashlib import sha256

N = 100000
K = 0
while 3**(K+1) <= 8*N:
    K += 1
M = 3**(K+3)
z = 0
rows, first = Counter(), {}
receipt = sha256()
for n in range(1, N+1):
    z *= 16
    for f, s in ((7,4),(4,-2),(3,-1),(2,-1)):
        d, v = 8*n-f, 0
        while d % 3 == 0:
            d //= 3
            v += 1
        z += s*3**(K-v)*pow(d, -1, M)
    z %= M
    assert z
    w, vz = z, 0
    while w % 3 == 0:
        w //= 3
        vz += 1
    actual = 3**(K-vz)
    assert K-vz >= 1
    first.setdefault(K-vz, n)
    if n == 1:
        row, predicted = 0, 3
        assert (z//3**(K-1)) % 3 == 1
    else:
        q, j = 9, 1
        while n >= (9*q+7)//8:
            q *= 9
            j += 1
        a,b,c,d,e = (q+7)//8,(q+1)//2,(5*q+3)//8,(3*q+1)//4,(9*q+7)//8
        assert a <= n < e
        if n < b:
            row, predicted = 1, q
            assert (z//3**(K-2*j)) % 3 == 1
        elif n < c:
            row, predicted = 2, q
            assert (z//3**(K-2*j)) % 3 == 2
        elif n < d:
            row, predicted = 3, q//3
            assert (z//3**(K-2*j)) % 9 == 6
        else:
            row, predicted = 4, 3*q
            assert (z//3**(K-2*j-1)) % 3 == 1
    assert actual == predicted
    assert 9*actual > 4*n and actual <= 8*n
    if n >= 769:
        rows[row] += 1
        receipt.update(f'{n}:{z}:{actual}:{row}\n'.encode())
for k, n in first.items():
    expected = (3**k+7)//8 if k % 2 == 0 else (3**k+1)//4
    assert n == expected
assert dict(rows) == {4:24657,1:58173,2:8201,3:8201}
assert receipt.hexdigest() == 'e0811bbadd6390808344b197211f12e078535ed244ab7fc0d0adcd3473dff07e'
```

## 3. Separate filter matrix checks

Constructing `S e_j=e_(j+1 mod m)` directly and using exact SymPy matrices and
Smith normal form over ZZ gave:

| m | Exact determinant | Positive Smith entries exceeding1 |
|---|---:|---|
|2|45|3,15|
|3|45|45|
|5|825|825|
|6|5265|9,585|
|10|1116225|33,33825|
|15|1082196225|1082196225|

These matrices were formed directly from the coefficients of H, not from the
resultant formula. The m2,m3,m5,m6 calculations preceded access to the root's
filter conclusions; m10,m15 were performed during this audit.

For every1<=N<=20, a directly constructed strictly lower shift matrix also
passed exact determinant checks for H(L_N), Q(L_N), and independently entered
Gaussian elimination over F2 confirmed both ranks `max(N-4,0)`.

At review time, the integrated eight-case test file did not explicitly
regress the new nilpotent structural theorem or the full four-stratum height
certificate. The root was informed. This report supplies the independent
executed receipts; any added integrated checks have their own validation
receipt and should not be inferred from this snapshot description.

### Additional cofactor and causal inverse audit

The root subsequently supplied the proposed exact cofactor

`K(t)=4-4t+2t³-t⁴`.

Direct coefficient multiplication confirms

`H(t)K(t)=16-t⁸`.

For nilpotent L_N the inverse is therefore the finite expression

`H(L_N)^(-1) = sum_(j>=0) 16^(-j-1) L_N^(8j) K(L_N)`.

The nonzero terms in successive blocks do not overlap. Their positions and
2-adic coefficient norms are, for block j:

| Position | Coefficient | 2-adic norm |
|---|---|---|
|8j|4/16^(j+1)|2^(4j+2)|
|8j+1|-4/16^(j+1)|2^(4j+2)|
|8j+3|2/16^(j+1)|2^(4j+3)|
|8j+4|-1/16^(j+1)|2^(4j+4)|

Thus, when `N-1=8q+r` with0<=r<=7, the proposed sharp maximum operator norm

`||H(L_N)^(-1)||_2 = 2^(4q+2+1[r>=3]+1[r>=4])`

is correct. The previous complete block has norm at most2^(4q), strictly below
the new block's first coefficient, so no truncated-block edge case is missed.
In particular N=8n gives16^n.

For the real maximum operator norm, each row sum is a partial sum of the
absolute inverse coefficients, and the last row is maximal. The geometric
bound is11/15, with the sharper exact value

`||H(L_(8n))^(-1)||_infinity = (11/15)(1-16^(-n))`.

**Executed independent check:** inverse coefficients were generated by the
triangular recurrence `b_0=1/4`,

`b_r = -(1/4) sum_(k=1)^min(r,4) h_k b_(r-k)`,

using exact Fraction arithmetic, for every1<=N<=160. The resulting vectors
matched the proposed finite geometric expression, sharp binary norm, and
real norm bound at all160 lengths. This computation did not use the proposed
inverse formula to generate the inverse.

At length8, `S_8^8=I` gives the cyclic inverse `K(S_8)/15`, while
`L_8^8=0` gives the causal inverse `K(L_8)/16`. The determinants are
`15^4` and `16^4`, respectively. The causal real norm is11/16 and binary
norm16; the cyclic real norm is11/15 and binary norm1. These are exact
conditioning differences caused by the boundary convention on the declared
filter domain. They are not an asymptotic statement about a BBP orbit.

### Final Fibonacci-module algebra audit

The root supplied the recovered-frame formulas `A=[[1,1],[1,0]]`,
`M=A^(-1)=[[0,1],[1,-1]]`. The complete new Fibonacci manuscript was not yet
present at the time of this algebra check; the statements below report the
independently verified formulas, not a claim to have reviewed unseen prose or
the recovered note's provenance.

The relation `M²+M-I=0` reduces the literal source polynomials to

`H(M)=8I+M=[[8,1],[1,7]]`,

`K(M)=3M=[[0,3],[3,-3]]`,

`Q(M)=7I-6M=[[7,-6],[-6,13]]`.

Direct matrix substitution and exact ZZ Smith normal form confirmed:

| Matrix | Determinant | Positive Smith diagonal |
|---|---:|---|
|H(M)|55|1,55|
|K(M)|-9|3,3|
|Q(M)|55|1,55|

Since M and its inverse are integral, M is an isometry for the maximum norm
at every prime. Hence `||K(M)v||_3=||v||_3/3` for every vector v in Q3².
H(M) and Q(M) have determinant units at3, so they are exact ternary
isometries. Their sharp inverse costs at5 and11 are5 and11, respectively;
their adjugates contain prime-unit entries. These assertions require no
statistical premise.

The cofactor identity remains exact in this representation:

`16I-M⁸=H(M)K(M)=3M H(M)`.

This is a representation on the Fibonacci module
`Z[t]/(t²+t-1)`. It is distinct from the cyclic channel quotient
`Z[t]/(t^m-1)`, the nilpotent causal quotient `Z[t]/t^N`, and the actual
nonautonomous rational BBP state trajectory. Therefore a ternary contraction
of K(M) does not contradict the ternary isometry of the BBP homogeneous
multiplier16. Transporting a conclusion between those domains requires an
explicit source/observer intertwiner; none is supplied by a matrix label
alone.

For the quartic monomial column

`V4(x,y)=(x⁴,x³y,x²y²,xy³,y⁴)^T`,

direct expansion of `V4(A(x,y))` gives the transport matrix

```text
[[1,4,6,4,1],
 [1,3,3,1,0],
 [1,2,1,0,0],
 [1,1,0,0,0],
 [1,0,0,0,0]].
```

Its characteristic polynomial is exactly

`(lambda-1)(lambda²+3lambda+1)(lambda²-7lambda+1)`.

An independent symbolic characteristic-polynomial calculation and625
integer Veronese transport checks, for x,y in[-12,12], passed. The factor
structure also follows from the eigenvalues alpha,beta of A with
`alpha*beta=-1`: the quartic eigenvalues are alpha⁴, -alpha²,1,-beta²,beta⁴.

**Construction guard sent to root:** a quartic observer on two state
coordinates naturally has five channels, and can be evaluated in three
frames. The mere count “two coordinates times three frames” does not force
quartic degree. That degree is an explicit construction choice unless an
additional theorem selects it. The recovered quadratic construction and
its chronological actions must not be silently replaced by unrelated CRT
successor cycles.

### Final Fibonacci manuscript audit

After `FIBONACCI_SOURCE_TRANSPORT.md` was present, the reviewer read the
complete manuscript. The augmentation identity, doubling orientation,
Gram intertwiner, eigenvalue multiplicities, determinant 55^2, both ternary
norm equalities, and quartic eigenvalue proof passed the narrow audit.
The constant channel and selected-source boundaries are explicit. A
pronoun that could have included K(M) in an isometry assertion was clarified
to name H(M) and Q(M). No mathematical correction was required.

## 4. Remaining limits and next discriminator

The mathematical dependence is explicit: the filter polynomial comes from
the authentic BBP source, but the cyclic channel vector is a chosen observer
domain. Its local condition numbers do not automatically become condition
numbers for the real BBP phase orbit. The finite causal operator has a
different boundary condition. Preserving their residual is necessary for
source fidelity, but has not produced the missing signed cancellation.

The strongest unresolved discriminator remains an inequality involving the
authentic ordered real phases and the retained rational boundary, which
cannot also certify the source-matched finite-precision alias controls. More
local determinant, valuation, or unsigned-energy data alone would not close
that implication.
