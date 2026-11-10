# Signed covariance and finite parity convention audit

**Audited parent:** PR #576, `afabc458323ef2e3a20ce2bae77239c4190819c5`.
**Scope:** exact finite algebra in `signed_covariance_decomposition.py`, the
meaning of its returned quantities, and transport between the PPP integer
parity convention and the first fractional hexadecimal digit. These are local
repairs; no original-zero cancellation estimate follows from them.

## 1. Three implementation defects

The parent module advertised exact rational output, but `/ N` on integer sums
produced Python floats. Its frozen sample had size 512 and happened to give
dyadic values exactly representable in binary, so the existing comparison with
`Fraction` did not expose the carrier error.

Use these three rows, with `s=a*b`:

| Row | a | b | eps |
|---|---|---|---|
| 0 | 1 | 1 | 0 |
| 1 | 1 | -1 | 1 |
| 2 | -1 | 1 | 1 |

They distinguish the following quantities:

| Observable | Exact value | Parent behavior |
|---|---|---|
| `Cov(a,b)` | `-4/9` | Returned the float `-0.4444444444444444` |
| Parity mean `P=E[a*b]` | `-1/3` | `two_fiber_table['P']` returned `1/3`, the different observable `E[b]` |
| Boundary correction to covariance | `-4/3` | Returned approximately `-4/9`, computing `Cov(a*b,eps)` instead |

The repaired module constructs every mean with `Fraction(sum, count)`. The key
`P` now means the parity mean and `complement_mean` separately exposes `E[b]`.
For the historical 512-row count table, the incorrect `P` was `1/128`, whereas
the parity mean is `5/128`; no existing test had asserted that key.

The only callers of `tail_boundary_coupling` found in the repository were in
this module's own test surface. Its name is retained, but its docstring now
states the exact intended removal operation. Put

```math
c=b(-1)^{\varepsilon}.
```

Thus `c` removes the supplied boundary correction from the complementary
sign. Because `eps` is a bit,

```math
b-c=2b\varepsilon,
\qquad
\operatorname{Cov}(a,b)-\operatorname{Cov}(a,c)
=2\operatorname{Cov}(a,b\varepsilon).
```

That is the repaired function's result. The old expression
`Cov(a*b,eps)` was neither this difference nor the covariance asserted in the
first line of the old docstring. Globally flipping every correction would be
a different operation; the repaired API explicitly means **removing** them.

The sample constructor now rejects values outside the exact declared sign/bit
carrier and inconsistent `s != a*b`; empty input is rejected. Conditional
two-fiber means require both source-sign fibers to be populated. These checks
do not establish BBP/CRT provenance: the caller must still supply the genuine
source-labelled rows. Replaying the frozen aggregate counts with `eps=0` is a
synthetic algebra test, not a fresh source reconstruction or a measurement of
the boundary frequency.

## 2. Finite parity conventions must be transported

PPP-02 and `bbp_parity_pressure.SourceParity.completed_parity` use the integer
parity of the completed source. For `n>=1`, write

```math
y_n=U_n+T_n=16^{n-1}\pi,
\qquad
s_n=(-1)^{\lfloor y_n\rfloor}.
```

The Cayley/Fourier observer instead uses the first fractional hexadecimal digit:

```math
f(t)=(-1)^{\lfloor16t\rfloor},
\qquad
f(\{y_n\})=s_{n+1}.
```

Indeed, `y_(n+1)=16*y_n`, and the difference between
`floor(16*y_n)` and `floor(16*{y_n})` is the even integer `16*floor(y_n)`.
Therefore the two finite means on the same index interval satisfy

```math
\frac1A\sum_{n=A}^{2A-1}f(\{y_n\})
-\frac1A\sum_{n=A}^{2A-1}s_n
=\frac{s_{2A}-s_A}{A}.
```

The absolute endpoint payment is at most `2/A`. At `A=1` this bound is attained:
`floor(pi)=3` has sign `-1`, whereas the first fractional hexadecimal digit is
2 and has sign `+1`. The tests certify this through the exact source adapters;
they do not import a numerical pi digit oracle.

The original-zero asymptotic parity targets are equivalent after this endpoint
payment. Finite PPP/TFH counts and the new finite observer mean are not generally
equal. To transport the signed factorization `s_n=a_n*b_n`, shift **all** source,
prime and complementary labels to `n+1`; changing only `s_n` while retaining
the old labels would break the source map. Alternatively keep the integer
convention and carry the displayed endpoint term.

## 3. Remaining mathematical boundary

The algebraic split

```math
\operatorname{Cov}(a,b)
=\operatorname{Cov}(a,b\varepsilon)
+\operatorname{Cov}(a,b(1-\varepsilon))
```

is exact but provides no cancellation by itself. A small **width** for the source
tail does not imply a small **frequency** of boundary crossings. That frequency
needs a source-sensitive occupation estimate, as in the separate boundary
certificate. The historical wording that the boundary event is automatically
rare is not justified by the tail bound alone.

The masked quantity `b*(1-eps)` also still depends on `eps`; calling it entirely
finite CRT data loses that dependence. To isolate the genuinely finite
complement `c`, use `Cov(a,b)=Cov(a,c)+2*Cov(a,b*eps)`, with the source adapter
providing the formula for `c` independently of the future tail.

The F-10 coefficient derivation in the active arithmetic dossier also had a
sign typo. With `z=exp(-2*pi*i*m/16)` and `m!=0`, interval integration supplies
`(1-z)/(2*pi*i*m)`, not `(z-1)/(2*pi*i*m)`. This factor is corrected; the already
stated coefficient `16/(pi*i*m)` on `m=8 mod 16` is retained. The zero-frequency
coefficient is zero by the equal positive and negative interval lengths.

## 4. Verification receipt

Executed after the repair:

```sh
python -m unittest tests.test_signed_covariance_decomposition -v
```

**10 tests PASS:** the five retained tests plus five hostile cases. In
particular, the new tests exhaust all 512 three-row `(a,b,eps)` models and compare
against an independent pair-difference covariance identity,

```math
\operatorname{Cov}(a,b)
=\frac1{2N^2}\sum_{i,j}(a_i-a_j)(b_i-b_j).
```

They also check a five-row anticorrelated model, invalid carriers, empty
conditioning fibers, exact boundary-removal differences, and the source-index
transport at `n=1,...,9` and epochs `A=1,2,3,4`. The three-row models deliberately
use a nondyadic denominator; the old float implementation fails that control.

Repository-wide and hosted validation are recorded separately. The finite
identities do not certify original-zero parity balance, normality, or a uniform
Fourier truncation estimate.
