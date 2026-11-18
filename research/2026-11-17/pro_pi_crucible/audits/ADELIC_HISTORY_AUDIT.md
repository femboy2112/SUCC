# Pinned audit of the adelic BBP draft at 97c7433

## Scope and verdict

Read-only source reviewed: commit
`97c7433371feca631991a1b8227b656e92e4abcb`, parent
`16d04ab58e213e75ab47e61a170138196dbcd292`, on the newly visible remote branch
`research/pi-normality-crucible-frontier-2026-11-17`.
The branch name and manuscript attribution do not establish model authorship.

The source-specific 2-adic null-seed conclusion survives after an explicit
sign repair. The octic partial-fraction matrix is correct. Its two published
BBP formulas have the stated common real period and null backward seed.
Neither statement bounds the real terminal carry word or any signed Weyl sum.

Three exact errors were found:

1. The derivative and primitive in equation ANC7 have the wrong sign for the
   first logarithmic term. At zero the printed derivative is `-1/2`, whereas
   the displayed series derivative is zero.
2. The equality in ANC13 between `4(alpha_3-alpha_4)` and the Gaussian weighted
   residue sum is false on the declared eight-dimensional domain. That sum
   equals `4 alpha_3`.
3. ANC12's asserted preservation of the *reduced* terminal denominator is false
   already at `B=3`: the proposed shadow cancels a factor `3` of the authentic
   denominator.

The claimed all-B shadow construction also invokes an unproved asymptotic for
the **reduced** denominator. A divisibility envelope does not establish that
asymptotic. Prime/cofactor details and the separate Borwein computations are
being audited by the parent and the prime-arithmetic agent; this note does not
claim to have rerun those suites.

The original-source R0 and full-normality verdicts remain **OPEN**, as the
draft itself ultimately states. A successful source fingerprint is not a
quantitative obstruction to low domain-wall density.

## Pinned files and receipt

All files are relative to `femboy2112/SUCC` at the pinned commit above.

| File | Git blob |
|---|---|
| `research/2026-11-17/causal_clock_scrambling/ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md` | `379c014f8ebdf7df82d433f26659660942fa1bbf` |
| `research/2026-11-17/causal_clock_scrambling/ADELIC_BBP_NULL_SEED_VALIDATION.md` | `ee830a4b5ed721d81db4e681e3a2e07199800f25` |
| `observational_succ/adelic_bbp_normality_crucible.py` | `ad61a1fd4ac15820e81a0a8aef8fd6101434bb0b` |
| `tests/test_adelic_bbp_normality_crucible.py` | `8072237302a3042a74b1ad29d994fdf229d90b22` |

The exact calibration is reproducible with:

```sh
python3 /workspace/scratch/d2afcbfb001f/history_scratch/audit_97c7433.py
```

Executed successfully; exit code `0`. Its JSON output is preserved as
`ADELIC_97c7433_RECEIPT.json`. This script imports no repository modules. It uses
SymPy for exact rational-function identities and `Fraction` for the minimal
denominator counterexample. No repository file, worktree, branch, or remote was
modified. No full test suite or Lean verification was run by this audit.

## A. The null-seed theorem: exact repair and surviving proof

Write

\[
A(v)=1-2v+2v^2,\quad B(v)=1-2v^2,\quad
C(v)=1-v+iv,\quad D(v)=1-v-iv.
\]

For the series displayed in ANC7,

\[
G(v)=\sum_{m\ge0}16^m\left(
\frac{4v^{8m+7}}{8m+7}-\frac{2v^{8m+4}}{8m+4}
-\frac{v^{8m+3}}{8m+3}-\frac{v^{8m+2}}{8m+2}\right),
\]

the correct rational derivative is

\[
G'(v)=\frac{4v^6-2v^3-v^2-v}{1-16v^8}
=-\frac{v}{2A(v)}-\frac{v}{2B(v)}.
\]

The correct primitive, normalized to zero at zero, is

\[
\boxed{G(v)=-\frac18\log\frac{A(v)}{B(v)}
-\frac1{8i}\log\frac{C(v)}{D(v)}.}
\]

Thus the **first** log sign must change; changing only the second sign does
not repair the identity. The exact rational residual between the authentic
derivative and the printed derivative is

\[
-\frac{2v^2-4v+1}
 {2(2v^2-1)(2v^2-2v+1)},
\]

which is `1/2` at zero. The corrected residual is identically zero.

This repair retains the null-seed result without an appeal to unspecified
analytic continuation. In `Q_2(i)`, on the closed unit disk in `v`, the log
power series of `A`, `B`, `C`, and `D` converge uniformly:

\[
|A-1|_2,|B-1|_2\le\tfrac12,
\qquad |C-1|_2,|D-1|_2\le2^{-1/2}<1.
\]

The generating series also converges uniformly there. Hence its formal
identity may be evaluated at `v=1`. Both ratios become `-1`, and the convergent
2-adic logarithm satisfies `log_2(-1)=0`. Consequently

\[
\sum_{m\ge0}16^m r_1(-m)=-G(1)=0.
\]

The primitive printed in the draft actually belongs to the second BBP source:
its derivative is

\[
\frac{4v^5+2v^4+2v^3-1/2}{1-16v^8}
=\frac14\left(\frac{2v-1}{A(v)}+\frac{2v}{B(v)}\right)
-\frac1{4A(v)}.
\]

The same convergent-log evaluation proves the second source's backward seed
is zero. This validates the restricted r1/r2 period-seed calculation below
after the formula correction.

### What uniqueness does and does not establish

The authentic forcing has no pole on `Z_2`, and its poles are at 2-adic
distance at least `2` from that ring. The translates `r_1(z-m)` are therefore
uniformly analytic on each fixed disk of radius strictly between `1` and `2`.
The series

\[
\mathfrak U_2(z)=\sum_{m\ge0}16^m r_1(z-m)
\]

is analytic on such disks and bounded on `Z_2`. If two bounded solutions on
all `Z_2` differ by `H`, then `H(z)=16^j H(z-j)` for every `j`; boundedness
forces `H=0`. Hence the bounded analytic section is unique, and

\[
U_N(s)=\mathfrak U_2(N)+16^N s
\]

for a `Q_2` seed `s`, because the section's seed is zero.

Every `Z_2` seed nevertheless gives a bounded **forward sequence**: multiplication
by `16` contracts. The selection criterion is exact membership in the full
analytic section, not forward boundedness or convergence toward that section.
The real seed `-pi/16` has no canonical specified image in `Q_2`; the draft's
identity should not silently identify those distinct field elements. The
literal seed `0` is common to the two fields without this problem.

## B. Octic period coordinates: valid matrix, wrong character equality

The eight columns of matrix ANC10 were checked by substituting each monomial
`1,t,...,t^7` into the partial-fraction identity ANC9. All eight rational
identities hold exactly. The boundary-null polynomial and decomposition

\[
Q_1=Q_{\alpha_3}+Q_{\rm null}/4,
\qquad Q_2=Q_{\alpha_3}-Q_{\rm null}/4
\]

are consistent with that matrix.

However, its row for `alpha_3` gives

\[
\frac12\sum_{a=1}^8 W_a\operatorname{Im}(1+i)^a
=4\alpha_3,
\]

whereas

\[
4(\alpha_3-\alpha_4)=2W_2-8W_6.
\]

These are different linear functionals. The minimal counterexample is
`Q(t)=1`, for which `W=(1/8,0,...,0)` and

\[
\alpha_3=\alpha_4=1/64,
\qquad 4(\alpha_3-\alpha_4)=0,
\qquad \frac12\sum W_a\operatorname{Im}(1+i)^a=1/16.
\]

The code implements the Gaussian weighted sum, while its docstring repeats
the false equality. The focused tests evaluate the character only on a
restricted set where `alpha_4=0`, so they cannot expose this error. On the
span of `r1`, `r2`, and rational coboundaries, the two definitions agree and
the stated character values `1,1,0` survive.

The seven-coordinate quotient is a valid algebraic quotient by the displayed
one-dimensional null line. It does not by its construction prove that this
line is the entire rational kernel of the scalar real integration map;
such a stronger reading would require accounting for all relations among the
remaining real period constants. No such independence claim is used here.

### Correct restricted period-seed statement

Take rational `lambda_1,lambda_2` and `h in Q(z)` with no integer poles and
`h(infinity)=0`, and set

\[
r=\lambda_1r_1+\lambda_2r_2+16h(n)-h(n+1).
\]

The real forward sum telescopes to

\[
x_\infty(r)=(\lambda_1+\lambda_2)\pi/16+h(1).
\]

The backward coboundary partial sum is exactly

\[
\sum_{m=0}^M16^m\{16h(-m)-h(1-m)\}
=16^{M+1}h(-M)-h(1).
\]

The boundary term tends to zero 2-adically. Indeed rational-function values
at the negative integers have 2-adic growth at most polynomial in `M`,
whereas `|16^{M+1}|_2` decays geometrically. Therefore

\[
\mathfrak U_2^{(r)}(0)=-h(1)\in\mathbb Q.
\]

Only because this backward value is proved rational can it be transported
canonically into `R` and added to `x_infinity`. The displayed "adelic sum"
must not be interpreted as adding arbitrary real and 2-adic scalars.

The draft assumes merely that `h` is regular at integers `n<=1`. That leaves
the forward forcing potentially undefined: `h(n)=1/(n-2)` meets that stated
condition and `h(infinity)=0`, but `r(1)` contains the pole `h(2)`. Requiring
regularity at all integers used by either series repairs the domain.

For nonzero `lambda_1+lambda_2`, this restricted class has an irrational
completed endpoint. That excludes exact rational locking. It does not
exclude irrational sources with cold shells or establish R0.

## C. Carry congruence and the false exact-denominator shadow claim

The late-shell congruence ANC18 is valid for the authentic source:

\[
U_{2B}=16^B U_B+\sum_{m=0}^{B-1}16^m r(2B-m),
\qquad C_{2B}\equiv\sum_{m=0}^{B-1}16^m r(2B-m)-u_{2B}
\pmod{16^B\mathbb Z_{(2)}}.
\]

This follows already from 2-adic integrality and the finite recurrence. It
does not require the new null-seed theorem. The missing input is a bound on
the fractional remainder's coupled real and 2-adic behavior; writing that
remainder in the congruence does not supply such a bound.

For ANC12, the exact authentic state at `N=6` is

\[
U_6=80827484660698633414/24536311574775.
\]

At `B=3`, the uncollided product is

\[
\Pi_6^*=19\cdot23\cdot29\cdot37\cdot41=19224941.
\]

The proposed construction gives

\[
R_6^\sharp=67379365062,
\quad C_6^\sharp=3293184,
\quad \gcd(R_6^\sharp,Q_6)=3.
\]

Consequently

\[
V_6^\sharp=26934196254814399554/8178770524925,
\qquad\operatorname{den}(V_6^\sharp)=Q_6/3\ne Q_6.
\]

This counterexample still fits in the required unit interval, preserves the
stated late-shell 2-adic congruence and uncollided prime principal parts, and
has `D_3=J_3=0`. Thus it isolates exactly the failed denominator assertion.
The original shadow test checks `B=(2,4,8,12)` and **never asserts equality of
the reduced denominators**, although its comment says this is preserved.

There is also an all-B gap: the implication

\[
\Pi_N^*\mid Q_N\mid\mathcal L_N,
\quad \log\Pi_N^*\sim(8/3)N,
\quad\log\mathcal L_N\sim6N
\]

does not give `log Q_N ~ 6N`. In particular it does not alone prove
`16^B Pi_(2B)^* < Q_(2B)` for every `B>=2`. The validation document's wording
that an asymptotic was "verified through N=80" is finite observation, and
the statement that the inequality was verified for all `B>=2` needs a
universal proof not present in the finite test.

Finally, a one-stage shadow tests implications from the preserved partial
terminal signatures over an enlarged class of rational states. It is not an
authentic zero-seeded four-pole history. The shadow changes the terminal
circle-kernel responses themselves, so it cannot refute every proof that
uses those responses. Nor does attaching the authentic source's period
character to an unrelated terminal clone establish a coherent history for
the clone. The valid obstruction is narrower than the draft's universal
"any purported proof" wording.

## D. Hostile division, chronology, and novelty boundary

The old two-formula counterfeit `TFL-01` remains a counterexample to the old
generic implication from nonzero pole-orbit residues to R0. A new linear
character that vanishes on it does not refute that counterexample. It
identifies a stronger source condition under which this particular exact
rational lock is excluded. The scalar period identity shows why.

This new invariant does not exclude sparse irrational failures of R0. The
2-adic section does not provide a signed real Fourier estimate. The finite
carry congruence retains the full difficulty in `u_(2B)`. No stable map from
Mellin/Gamma transport to real-circle cancellation is proved in the four
reviewed files.

The closed-form Borwein autocorrelation and Parseval/Cauchy-Schwarz transfer
deserve credit as instrument refinements; the parent and prime-arithmetic
agent are auditing their formulas. The concurrent direct semiconcavity/
inverse proof in `BORWEIN_L2_OPTIONAL_APPENDIX.md` also reaches the sharp
`V^(1/5)` exponent and includes an explicit positive sharpness family. The
existence of either instrument does not establish decay of the authentic
source's energy.

## E. Claim ledger and validation boundary

| Claim | Audit status | Boundary |
|---|---|---|
| ANC7 as printed | Refuted | Exact derivative mismatch, already at zero |
| Authentic 2-adic null seed | Disclosed after repair | Correct formal identity and convergent 2-adic evaluation above |
| Unique bounded analytic section on all `Z_2` | Disclosed | Does not select a seed by forward boundedness alone |
| ANC10 partial-fraction matrix | Disclosed / exact calibration passed | All eight rational-function basis identities |
| ANC13 two character definitions agree in eight dimensions | Refuted | `Q(t)=1` counterexample |
| Restricted r1/r2 period-seed identity | Disclosed after domain repair | No integer poles; rational cross-field seed value |
| ANC12 preserves reduced `Q_(2B)` | Refuted | `B=3`, denominator loses factor `3` |
| ANC12 universal fit from claimed growth | UNVERIFIED in reviewed proof | Envelope alone does not prove actual-denominator asymptotic |
| Original-source domain-wall coercivity / R0 | Open | No all-late-shell arithmetic lower bound |
| Authentic swept energy tends to zero / normality | Open | No signed source cancellation estimate |

The remote validation's 15-test receipt was read, not rerun. Its statement
that all tests use exact rational arithmetic is too broad: the Fourier-floor
test evaluates `math.pi` and `math.sin` in floating point for harmonics 1–50.
The analytic Fourier-floor argument can stand on its own, but those finite
floating-point checks should be labeled as such. The printed sign identity,
general character equality, and exact-denominator preservation were not
tested by that suite. The audit's exact probes above specifically reach
those three previously unchecked assertions.
