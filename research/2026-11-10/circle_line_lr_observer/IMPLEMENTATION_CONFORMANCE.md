# Independent circle observer implementation conformance

**Date:** 2026-11-11 UTC. **Verdict:** PASS for the specified geometry,
matrix/rotation sources, certified L/R output, and hexadecimal output.

Reviewed file: `circle_line_observer.py`.

```text
SHA256 a7b02e06e5e53a7a9d66b0b2d6fd8b4b0a8529b1fdecdfb995a01bc5cb9239fa
```

This bearing read the implementation and derived the source intervals
separately. It did not edit the implementation, the shared checkout, or a
remote. All arithmetic checks below used Python 3.12.14 `fractions.Fraction`.
The verifier and implementation share that arithmetic library; these are
distinct formula/algorithm checks, not independent hardware or reasoners.

## Mathematical conformance

### 1. Circle, line, and Euclidean measure

The implementation's point map is the second intersection of
`x*x+y*y=1` and `y=t*(x+1)`:

$$
P(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),
\qquad \|P'(t)\|=\frac{2}{1+t^2}.
$$

The interval \([0,1]\) traces a quarter circle. The circumference/diameter
ratio is therefore \(\gamma=4\int_0^1dt/(1+t^2)\), namely geometric pi.
The point, tangent, and speed methods implement these formulas exactly.
Their explicit `Q(t)` conversion also keeps integer parameters exact.

### 2. Beta integral and the positive matrix source

Put \(q(t)=2t(1-t)\) and

$$
W_n=\int_0^1 q(t)^n\,dt
=\frac{2^n(n!)^2}{(2n+1)!},\qquad
W_0=1,\quad \frac{W_n}{W_{n-1}}=\frac{n}{2n+1}.
$$

The integral formula follows by repeated integration by parts for the
integer beta integral. Since \(0\le q(t)\le1/2\), the integrated geometric
series converges with an explicit geometric remainder. Consequently

$$
2\sum_{n\ge0}W_n
=2\int_0^1\frac{dt}{1-2t+2t^2}
=2\int_{-1}^1\frac{du}{1+u^2}
=4\int_0^1\frac{du}{1+u^2}=\gamma.
$$

The substitution in the middle is \(u=2t-1\). This verifies both the
normalization and the connection of the beta source to Euclidean arclength.

For \(k\ge0\), define the shifted tail

$$
T_k=2\sum_{m\ge0}\prod_{j=1}^m\frac{k+j}{2(k+j)+1}.
$$

Every ratio in the product is at least \(1/3\), and is strictly greater
eventually; every ratio is strictly smaller than \(1/2\). Comparing with
the corresponding geometric sums gives

$$
\boxed{3<T_k<4\quad\text{for every }k\ge0.}
$$

The implemented matrix

$$
Z_k=\begin{pmatrix}k&4k+2\\0&2k+1\end{pmatrix}
$$

acts as \(z\mapsto2+kz/(2k+1)\). For
\(A_k=Z_1\cdots Z_k\), direct affine composition gives

$$
A_k(z)=S_k+W_kz,\qquad S_k=2\sum_{n=0}^{k-1}W_n,
\qquad \gamma=S_k+W_kT_k.
$$

Thus `MatrixCircleSource` correctly stores
\((S_k+3W_k,S_k+4W_k)\), a strict enclosure of pi of width \(W_k\).
Removing a common integer scalar by `primitive()` preserves this projective
map. Also \(W_k<2^{-k}\) for \(k\ge1\).

**Nesting nuance:** the first refinement leaves the lower endpoint equal to
3. The upper endpoint decreases strictly at every refinement, and the lower
endpoint increases strictly after that first refinement. The implemented
description "nested enclosures" is correct; "both endpoints improve
strictly at every stage" would be incorrect.

### 3. Rational rotation source

The circle identity \(P(1/2)P(1/3)=(0,1)\), together with the rational
change of coordinate \(t=(1/2+u)/(1-u/2)\), yields

$$
\gamma=4\bigl(A(1/2)+A(1/3)\bigr),\qquad
A(x)=\int_0^x\frac{dt}{1+t^2}.
$$

At stage \(m\), `RotationCircleSource` stores precisely

$$
\ell_m=4\bigl(S_{2m}(1/2)+S_{2m}(1/3)\bigr),\quad
u_m=4\bigl(S_{2m-1}(1/2)+S_{2m-1}(1/3)\bigr),
$$

where \(S_n(x)=\sum_{j=0}^{n-1}(-1)^jx^{2j+1}/(2j+1)\).
The signed finite geometric-series remainder proves strict enclosure and
nesting. The exact width is

$$
u_m-\ell_m=\frac4{4m-1}
\left(2^{-(4m-1)}+3^{-(4m-1)}\right).
$$

This matches the implementation's two-term update and stage numbering.

### 4. L/R decisions, invariants, and productivity

The endpoint tuple begins at \((3,1,4,1)\). Each update is the correct
Stern–Brocot mediant update, preserving \(bc-ad=1\). Matrix endpoint columns
and the residual chart are correctly distinguished in the docstring.

The implemented tests `source.upper <= q` and `source.lower >= q` are sound:
the source interval itself is strict around pi, so equality of a certificate
endpoint with a mediant still gives a strict comparison between pi and that
mediant. No arrow is emitted from an unresolved comparison.

For each mediant \(q\in\mathbb Q\), established irrationality gives
\(q\ne\pi\). Source widths tend to zero, so one of the tests succeeds after
finitely many refinements. Induction proves productivity for every finite
prefix. Each step keeps pi strictly between the endpoints, and after \(k\)
steps the endpoint width is

$$
\frac1{bd}\le\frac1{k+1}.
$$

This is a mathematical productivity proof, not a claim that a finite run
checked an infinity. It allows unbounded integer storage.

### 5. Hexadecimal decisions and productivity

At exponent \(e\), the function refines until the floors of both source
endpoints multiplied by \(16^e\) agree. Their shared value is exactly
\(\lfloor16^e\pi\rfloor\); reduction modulo 16 yields the requested digit.
Since \(16^e\pi\notin\mathbb Z\), shrinking enclosures eventually have
equal floors. Every requested digit therefore terminates.

For general bases, the helper correctly documents its first `digit` as the
units digit and retains the entire scaled integer in `floor`. This resolves
the earlier wording issue for bases 2 and 3. The CLI emits hexadecimal, for
which the initial units digit `3` is also the complete integer part.

## Executed finite checks and receipt

The independent verifier implemented a fresh BBP partial sum with 192 terms.
For its tail it used the simple strict bound

$$
0<\pi-B_N<\frac{64}{15\,16^N}.
$$

Indeed the BBP coefficient is positive: with \(x=8n\), its combined
numerator is \(15x^2+151x+376>0\). It is smaller than 4, so a geometric tail
gives the displayed bound. The classical BBP identity is only a regression
reference here. Neither geometric source nor its proof calls it.

| Executed check | Scope and result |
|---|---|
| Circle equation, secant incidence, speed | 81 reduced rational parameters in [0,1], denominators at most 16; PASS |
| 3–4–5 rotation | Exact quarter turn; PASS |
| Product weights versus beta factorial formula | n=0,...,64; PASS |
| Matrix source against independent affine partial sum | Stages 0,...,320; PASS |
| Rotation source against independent finite-polynomial sums | Stages 1,...,97; PASS |
| Enclosure containment of the independent BBP interval | All tested source stages; PASS |
| Arrow letters, every certificate, determinant, bracketing, width | 512 arrows for each source; PASS |
| Every digit floor and source-stage certificate | 64 fractional hex digits plus integer floor, for each source; PASS |

```text
Python: 3.12.14
BBP terms: 192
512-letter word SHA256:
3a6b7fe8c558ace21eac7f9f71b068fa6eea0bc70f4aa4312c6fecc6408b599d

Hex output:
3.243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89

Matrix source: arrow stage 123; final digit stage 254
Rotation source: arrow stage 30; final digit stage 63
Final endpoint denominator bit lengths: 60, 65
```

The two sources produced the same 512-letter word. A first-letter mutation,
a first-digit mutation, and an offset reference target were rejected by
the corresponding equality/bracketing comparisons. These are calibration
checks for the verifier, not replacements for the analytic proofs above.

### Compact reproduction

Run this from the directory containing the reviewed file. It reproduces the
512-arrow/64-digit cross-check and reconstructs each source certificate
without using the production source's formulas as runtime references.

```python
import hashlib, importlib.util, sys
from fractions import Fraction as F
from pathlib import Path
sys.dont_write_bytecode = True
p = Path('circle_line_observer.py')
assert hashlib.sha256(p.read_bytes()).hexdigest() == (
    'a7b02e06e5e53a7a9d66b0b2d6fd8b4b0a8529b1fdecdfb995a01bc5cb9239fa')
spec = importlib.util.spec_from_file_location('reviewed_observer', p)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
N = 192
B = sum((F(4,8*n+1)-F(2,8*n+4)-F(1,8*n+5)-F(1,8*n+6))/16**n
        for n in range(N))
H = B + F(64,15*16**N)
def matrix_interval(k):
    s,w = F(0),F(1)
    for j in range(1,k+1):
        s += 2*w
        w *= F(j,2*j+1)
    return s+3*w,s+4*w
def rotation_interval(k):
    def S(n,x):
        return sum(((-1)**j*x**(2*j+1)/F(2*j+1)
                    for j in range(n)), F(0))
    return (4*(S(2*k,F(1,2))+S(2*k,F(1,3))),
            4*(S(2*k-1,F(1,2))+S(2*k-1,F(1,3))))
a,b,c,d = 3,1,4,1
word = ''
for k in range(512):
    q = F(a+c,b+d)
    if H < q:
        word += 'L'; c,d = a+c,b+d
    elif B > q:
        word += 'R'; a,b = a+c,b+d
    else:
        raise AssertionError('Insufficient reference precision')
floors = []
for e in range(65):
    lo,hi = B*16**e,H*16**e
    x,y = lo.numerator//lo.denominator,hi.numerator//hi.denominator
    assert x == y
    floors.append(x)
digits = '3.' + ''.join('0123456789ABCDEF'[x % 16] for x in floors[1:])
for name,interval in [('matrix',matrix_interval),('rotations',rotation_interval)]:
    r = m.finite_run(512,64,name)
    assert r['word'] == word and r['hexadecimal'] == digits
    a,b,c,d = 3,1,4,1
    for k,cert in enumerate(r['arrow_certificates'],1):
        q = F(a+c,b+d)
        assert F(cert['mediant']) == q
        lo,hi = interval(cert['source_stage'])
        assert lo < B < H < hi
        if cert['arrow'] == 'L':
            assert hi <= q
            c,d = a+c,b+d
        else:
            assert lo >= q
            a,b = a+c,b+d
        assert cert['endpoints'] == [a,b,c,d]
        assert b*c-a*d == 1 and F(a,b) < B < H < F(c,d)
        assert F(c,d)-F(a,b) <= F(1,k+1)
    for cert,expected in zip(r['digit_certificates'],floors):
        lo,hi = interval(cert['source_stage'])
        lo *= 16**cert['exponent']; hi *= 16**cert['exponent']
        assert lo.numerator//lo.denominator == expected == cert['floor']
        assert hi.numerator//hi.denominator == expected
    print(name, r['arrow_source_stage'], r['final_source_stage'])
print(hashlib.sha256(word.encode()).hexdigest())
print(digits)
```

## Final serialization patch and preserved review history

The initial arithmetic conformance run passed for source SHA256
`36f8a3e518916df6ae51353627d1b3c1d9436429f98a70b48a5cc7e53c530d83`.
That review had also caught the base-2/base-3 integer-part wording issue;
the source now correctly distinguishes a units digit from the full `floor`.
The initial matrix lower-endpoint equality remains the mathematical nesting
nuance recorded above, not a code defect.

The final implementation adds `rational_text`, which falls back to bounded
nine-digit integer chunks if ordinary decimal conversion reaches Python's
integer-string digit cap. This changes serialization, not either source or
the mathematical decisions. The compact 512-arrow/64-digit reproduction
above was rerun against the final hash at the top of this note; word hash,
digits, source stages, and every certificate still matched.

A separate finite regression set the process cap to 640 digits, compared
`rational_text` against uncapped reference strings for zero, positive and
negative small integers, and two fractions containing integers above 739
decimal digits, then compared an entire imported `finite_run(1,400,'matrix')`
against the uncapped run. All five direct cases and the full result matched.
The source reached stage 1595; each final source-fraction string had length
2753. The imported API left the process cap unchanged at 640. The test restored
the original cap afterward. This specifically exercises the new fallback.

## Source precision for the expanding Fourier observer

The proposed precision schedule is correct with the following explicit
indexing and quantifiers. Let \(A\ge1\), \(s\ge0\) be integers, set
\(k=8A+s\), and let \(x_k\) be the midpoint of the matrix source interval.
Its radius is \(\delta_k=W_k/2\), so

$$
|\pi-x_k|<\delta_k<2^{-k-1}.
$$

For the epoch statistic with the repository's \(n-1\) convention,

$$
E_{A,h}(x)=\frac1A\sum_{n=A}^{2A-1}
\exp\bigl(2\pi i h\,16^{n-1}x\bigr),
$$

the elementary character bound
\(|e^{iu}-e^{iv}|\le|u-v|\) gives

$$
|E_{A,h}(\pi)-E_{A,h}(x_k)|
\le\frac{2\pi|h|\delta_k}{15A}
\left(16^{2A-1}-16^{A-1}\right).
$$

Using \(\delta_k<2^{-8A-s-1}\), then dropping the subtracted positive
term and using the independently established \(\pi<4\), yields

$$
\boxed{|E_{A,h}(\pi)-E_{A,h}(x_{8A+s})|
<\frac{|h|}{60A\,2^s}\qquad(h\ne0).}
$$

For \(h=0\), both statistics equal 1 and the error is exactly 0; a strict
upper bound by 0 would be false. The proof works for any fixed nonzero real
\(h\); the Fourier characters of the circle use integer \(h\). If \(h\)
varies, its explicit magnitude remains in the estimate.

If the exponent convention is \(16^n\), the bound is 16 times larger.
The indexing is therefore a load-bearing part of this statement.

This is a concrete sufficient source-stage schedule for uniform finite-epoch
approximation. It does not give cancellation of either epoch average. In
particular, for fixed \(h\) and \(s\), the two averages differ by \(O(1/A)\);
thus cancellation for the moving rational approximants would transfer to the
exact pi orbit if separately proved. The growing-denominator rational epochs
still require that separate estimate. Approximating the complex exponential
numerically also requires its own evaluation-error bound; the inequality
above treats the character evaluations mathematically exactly.

## Limits of this verdict

The finite receipt is evidence about this exact file version and tested
prefixes. The infinite recovery/productivity claims rely on the analytic
source identities, exact-integer semantics, and established irrationality
of pi. No normality, randomness, asymptotic signed cancellation, bounded
memory, or efficient global branch-time bound follows from this receipt.
