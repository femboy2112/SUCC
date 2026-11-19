# Forward causal 2–3–5 observers: Fibonacci, BBP, and local arithmetic dynamics

**Research continuation, 18 November 2026.** Based on Main XXVI at
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`. Original signed BBP source and zero
seed retained. **R0, base-16 pi normality, Collatz and RH remain OPEN.**

The user's central correction is operational: the observer moves forward inside
the carrier, retaining a model of the past. A report that repeats is not a return
to an earlier causal state. This dossier makes that distinction explicit while
completing a precise Fibonacci realization of two-/three-period reports with
five-coordinate dynamics.

## What was established

Let A=[[1,1],[1,0]]. The polynomial maps

\[
(a,b)\longmapsto(a^2,ab,b^2)
\longmapsto(a^4,a^3b,a^2b^2,ab^3,b^4)
\]

give exact forward two-, three-, and five-coordinate observation systems.
After two native Fibonacci updates the five-coordinate matrix is

\[
\mathbf T=\operatorname{Sym}^4(A^2)=
\begin{pmatrix}
16&32&24&8&1\\8&20&18&7&1\\4&12&13&6&1\\
2&7&9&5&1\\1&4&6&4&1
\end{pmatrix}.
\]

Its local periods are proved for every positive a,b,c:

| Report | Exact matrix and e0-orbit period |
| --- | --- |
| modulo 2^a | 3 times 2^max(a-3,0) |
| modulo 3^b | 2 times 3^(b-1) |
| modulo 5^c | 5^c |

Thus one five-coordinate forward Fibonacci carrier has a 3-cycle modulo 2,
a 2-cycle modulo 3, and a 5-cycle modulo 5. The construction establishes this
specific interpretation of the proposed (2,3,5) corner; permutation of the
numbers by itself was never a proof of existence.

There is a structural reason for the fifth prime: the Fibonacci polynomial
t^2-t-1 has discriminant 5. Its reductions at 2 and 3 give the semisimple
three- and two-cycle operators above; at 5, T is a single size-five unipotent
Jordan block. The proof uses (T-I)^5=0 and (T-I)^4 e0 nonzero modulo 5.
These five polynomial coordinates remain constrained by their two-coordinate
origin; they are not five independent physical degrees of freedom.

At a>=4,b>=2 the binary and ternary reported phases must agree modulo 6.
Only one sixth of independently chosen phase pairs can occur along the same
integer clock. Along the explicit later times d=6^m,

\[
v_2(\mathbf T^d-I)=m+3,\quad v_3(\mathbf T^d-I)=m+1,
\quad\mathbf T^d\equiv\mathbf T\ne I\pmod5.
\]

Matrix valuation means the minimum entry valuation. Both local observers see
arbitrarily close returns, while the fifth-prime report remains nontrivial.
The real spectral radius is phi^(8d), and the elapsed native Fibonacci time is
2d. These are demonstrably different observations of one forward computation.

The six-to-five symmetric-square reduction is integral for this particular
Fibonacci matrix, including at 2 and 3. A tempting contrary argument from the
denominator 3 in a universal GL2 decomposition is defeated by the explicit
integral splitting. The exact maps and that counterexample are retained.

## The connection to the authentic BBP work

The unchanged source polynomial is

\[
Q(t)=4-2t^3-t^4-t^5=(1-t)H(t),\quad
H(t)=4+4t+4t^2+2t^3+t^4.
\]

For M=A^(-1), R a five-cycle, and V0 its four-dimensional sum-zero subspace,

\[
\operatorname{tr}\mathbf T=F_{10}=55
=\det H(M)=\det(H(R)|_{V_0}).
\]

This joins the earlier sister-chat source/pentagon calculation to the new
five-channel carrier through a classical Fibonacci character. It is a scalar
identity, not an identification of the underlying state spaces.

For every stride d not divisible by 5 and null depth k>=0,

\[
\frac{\det[H(M)(I-M^{8d})^k]}
{\det[H(R)(I-R^{8d})^k|_{V_0}]}
=(-F_{4d}^{\,2})^k.
\]

This generalizes the earlier (-9)^k identity. At d=6^m, m>=1, the ratio's
valuations are 2k(m+4) at 2 and 2k(m+1) at 3, while its real magnitude grows.
If 5 divides d and k>0, the denominator determinant vanishes and the ratio is
undefined. The source filter requires observed samples through n+kd; early
evaluation from the known source law is a prediction, not a future observation.

The source mutation H+t^4 changes the base norms to 116 and 16, but preserves
the normalized null-depth multiplier. This control identifies exactly which
part uses the original source coefficients.

### An actual forward source map

SUCC's existing local source maps are

\[
[U_n]_{2^a}=\Phi_a(n),\qquad
[120n^2-89n+16]_{3^b}=C_b(n).
\]

Both are compatible clock bijections. The second is a cleared forcing
numerator; it is not U_n reduced in Z_3. Inverting them recovers
n modulo 2^a3^b. Applying the displayed Fibonacci matrix at that recovered
clock produces a compatible five-channel observer with the exact forward law.
At a>=4,b>=2 it is exactly 24-to-1 on the source clock labels.

This is the concrete source-to-observer map missing from a numerical analogy.
It also exposes its limitation: the map factors through the clock, so it cannot
manufacture real-phase information.

## What the moving observer requires for real phases

The synthesis proves two complementary results.

First, for the **actual zero-seeded** source and every fixed finite joint local
clock, no fixed report function can track e(hU_n) indefinitely with limsup error
less than sin(pi/17), for any nonzero integer h. The same applies to a finite-state,
time-homogeneous observer driven only by those fixed-resolution periodic labels.
This is a direct joint-place extension of SUCC's existing expanding-circle gap
lemma. A finite-dimensional state of unlimited precision, an unbounded clock,
or an increasingly refined model is outside that finite-state theorem.

Second, after changing the rational seed, any prescribed finite carry-residue
word can coexist with arbitrarily deep simultaneous 2-adic and 3-adic agreement,
including the entire finite transcript of an adaptive local observer. The
forcing and clock stay identical. The seed is built from a finite rational BBP
prefix, with no pi oracle. An exact U0=0 certificate immediately rejects it.

These results locate the burden on the observer's retained model: source origin,
height/denominator information, winding and sufficient clock resolution. The
local periods do not replace those data. Infinite repeated phase separation is
proved; positive lower shell density is still missing.
The explicit irrational sum16^(-j!) separates infinitely often while having
whole late shells approaching phase alignment, so that missing density step
cannot follow from irrationality alone.

## Collatz and RH: precise connections

Subtract two same-path rational affine trajectories. Their difference is
multiplied by the product of the chronological slopes. This gives the exact
local precision table:

| System | Slope after N steps | Binary precision change | Ternary precision change |
| --- | --- | --- | --- |
| BBP, same forcing times | 16^N | +4N | 0 |
| Shortcut Collatz, one realized parity word with s odd steps | 3^s/2^N | -N | +s |

The real error multipliers are the displayed slopes. For these slopes only,
the real, binary and ternary absolute values have product 1. The offsets and
state denominators require their own information; other primes cannot be
discarded. Collatz words 10 and 01 have equal slope 3/4 but distinct offsets
and residue cylinders. Binary branch admissibility is part of the theorem.

The existing Collatz valuation claim needs an odd-step hypothesis: all-zero
words have zero offset, so its finite v3 assertion does not apply. This dossier
records that qualification and regression without rewriting the historical
source. The positive-cycle conclusion survives.

Tao's actual Collatz proof provides a relevant analytic template: binary
valuation statistics feed a ternary affine process, and the hard result is
conditional fine-scale mixing and its transport. Its stationary ternary law is
not Haar. It proves an almost-all statement in logarithmic density, not Collatz
for every positive integer. No theorem transferring it to the selected BBP orbit
is claimed.

For RH, genuine local prime sources combine in the completed explicit formula.
The two-prime Euler product has coefficient 1 at 6; its logarithm has no new
primitive mixed source at 6. A false Euler factor at 6 changes that coefficient
to 2. At a fixed admissible test function, holding Gamma/pole terms fixed, the
four-cell prime-side contrast Q23-Q2-Q3+Qempty is zero by additivity. Correlations
created by a shared test space or optimization do not create a new prime.
Identifying a generic positive observer kernel with the completed Weil form
and proving its global sign remain separate unpaid obligations.

## Navigation and reproduction

The directly related [sister PR666 synthesis](SISTER_666_BRIDGE.md), read after
it appeared during this run, strengthens the scalar source match to
T=Sym4(I+Q(M)) modulo5 for the literal signed BBP polynomial. It also connects
the complementary identity H(M)K(M)=16I-M^8, K(M)=3M, and the exact omitted
boundary 16^L U_(n-L). Its earlier state/frame/readout counts remain explicitly
distinct from the present local cycle construction.

* [Fibonacci proof and local periods](FIBONACCI_LOCAL_BRIDGE.md)
* [Source map, memory theorem, and pi dependency cut](THEOREMS.md)
* [Constructive mixed-place shadows](CAUSAL_SHADOWS.md)
* [Collatz/RH derivations and primary references](COLLATZ_RH_TRANSLATION.md)
* [Claim ledger](CLAIMS.md)
* [Validation and evidence scope](VALIDATION.md)
* [Original conversation artifacts](inputs/)

Run from the repository root:

```sh
export PYTHONPATH="$PWD"
python -m unittest discover -s tests -p 'test_causal_235*.py' -v
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The focused suite checks 29 methods. Original input probes are preserved byte
for byte and replayed separately. Validation details report what actually ran;
they do not certify an infinite statistical theorem or academic novelty.
Full-suite provenance tests require full Git history. The initial 14,505-test
run had two environment errors; after restoring history and the documented
import path, all 17 tests in the affected modules passed. The original and
repair logs are both preserved in VALIDATION.md's evidence map.
