# Adversarial boundary of the zero-anchored Lambda–Haar compiler

**Date:** 2026-11-10. **Audited repository base:**
`50481e49592af00d87c602f671a28f3503709de0` (the integration candidate in
PR #584). **Status:** the mathematical propositions below have direct paper
proofs. The separate exact-rational run in Section 7 calibrates the source
countermodel; it is not the proof of its infinite claims. The constructor and
this audit use the same model family, so their agreement is not external
refereeing or a Lean certificate.

**Verdict:** the proposed source-selected contraction for the exact original
BBP source and literal zero seed remains OPEN. Several tempting universal
routes to it are REFUTED below. Exact source authentication survives these
controls and must reject the altered source or altered seed at the indicated
gate.

## 1. Fix the observable before asking it to contract

Write

\[
T(x)=\{16x\},\qquad B_a(y)=\frac{a+y}{16},\qquad
C\nu=\frac1{16}\sum_{a=0}^{15}(B_a)_*\nu,\qquad Q=C T_*.
\]

All distances in this document are ordinary interval Wasserstein distance on
the hexadecimal chart \([0,1)\), not shortest-arc circle distance. In
particular,

\[
Q\mu=\frac1{16}\sum_{a=0}^{15}(x\mapsto\{x+a/16\})_*\mu.
\]

The distinction between \(C\) and \(Q\) is essential. \(C\) adds a new
uniform leading digit to a tail law; \(Q\) replaces the actual first digit
uniformly while keeping the actual next-tail law. The repository's
[recursive Haar theorem](../../2026-11-09/recursive_haar_pinbed/THEOREMS.md)
already has this distinction correct.

For an actual orbit \(z_{n+1}=Tz_n\), let

\[
\mu_N=\frac1N\sum_{n=0}^{N-1}\delta_{z_n},\qquad
d_N=W_1(\mu_N,Q\mu_N),\qquad e_N=W_1(\mu_N,\lambda).
\]

The endpoint transport satisfies
\(W_1(T_*\mu_N,\mu_N)\le 1/N\). Coupling inverse branches with the same
digit gives \(W_1(C\nu,C\eta)\le W_1(\nu,\eta)/16\), and
\(C\lambda=\lambda\). Thus

\[
\boxed{\frac{15}{16}e_N-\frac1{16N}\le d_N
\le\frac{17}{16}e_N+\frac1{16N}.}
\tag{A1}
\]

For the lower inequality, use
\(e_N\le d_N+(e_N+1/N)/16\); for the upper inequality use
\(d_N\le e_N+(e_N+1/N)/16\). No continuity assumption at hexadecimal
cuts, ergodicity assumption, or asymptotic interchange is needed.

Consequently, \(d_N\to0\) is equivalent to equidistribution of this orbit,
and hence to its base-16 normality. The statistical defect is a genuine
normality observable, not an authentication error.

## 2. An unspecified vanishing remainder is equivalent to the destination

**Proposition A2 (PROVED PAPER).** Let \((d_N)\) be a bounded nonnegative
sequence and fix any \(0\le\theta<1\). The following are equivalent:

1. \(d_N\to0\).
2. There exist \(N_0\ge2\) and nonnegative \(\varepsilon_N\to0\) such that
   \(d_N\le\theta d_{\lfloor N/2\rfloor}+\varepsilon_N\) for every
   \(N\ge N_0\).
3. The particular residual sequence
   \(\max\{d_N-\theta d_{\lfloor N/2\rfloor},0\}\) tends to zero.

**Proof.** For 2 implies 1, let \(L=\limsup_Nd_N<\infty\). The sequence
\(\lfloor N/2\rfloor\) visits every sufficiently large positive integer,
so taking upper limits gives \(L\le\theta L\), hence \(L=0\). For 1
implies 2, simply choose \(\varepsilon_N=d_N\). For the equivalence with
3, the displayed positive residual itself supplies 2, and it is bounded by
\(d_N\) when 1 holds. QED.

For the exact BBP orbit, A1 therefore makes the existence-only contraction
statement another equivalent normality criterion. This does not refute a
useful **source-derived estimate with an independently proved remainder**.
It specifies what that proof must contain. Computing the smallest residual
on observed epochs and naming it an error bound does not prove it vanishes.
Neither an observed fitted exponent nor an adjustable error constant pays
the all-epoch obligation.

### An unavoidable finite-sample error floor

There is also a concrete restriction on how strong a valid remainder can
be. Every probability law supported on at most \(N\) points satisfies

\[
W_1(\mu,\lambda)\ge\frac1{4N}.
\]

To see this, use the one-dimensional quantile formula. If the atoms have
masses \(w_1,\ldots,w_p\), the quantile function is constant on successive
intervals of those lengths. On an interval of length \(w_i\), the integral
of its distance to the identity is minimized by the midpoint constant and
equals \(w_i^2/4\). Thus the distance is at least
\(\sum_iw_i^2/4\ge1/(4p)\ge1/(4N)\).

Applying A1 to any actual length-\(N\) radix-16 orbit now yields

\[
\boxed{d_N\ge\frac{11}{64N}.}
\tag{A2a}
\]

**Proposition A2b (PROVED PAPER).** No actual radix-16 orbit can satisfy
the proposed dyadic contraction for all large \(N\) with
\(0\le\theta<1/2\) and \(\varepsilon_N=o(1/N)\). More generally, any
such valid remainder must obey

\[
\boxed{\limsup_{N\to\infty}N\varepsilon_N
\ge\frac{11}{64}(1-2\theta).}
\tag{A2b}
\]

**Proof.** On a dyadic subsequence \(N_k=2^kM\) beyond the stated starting
epoch, put \(a_k=N_kd_{N_k}\). The proposed recurrence implies

\[
a_k\le2\theta a_{k-1}+N_k\varepsilon_{N_k},
\qquad a_k\ge11/64.
\]

Since \(2\theta<1\), a vanishing input would force \(a_k\to0\), a
contradiction. If \(E=\limsup_NN\varepsilon_N<\infty\), iteration gives
\(\limsup_ka_k\le E/(1-2\theta)\), proving A2b. If \(E=\infty\), the
bound is automatic. QED.

In particular, importing the analytic tail contraction factor
\(\theta=1/16\) while paying only a source-tail error \(O(N^{-2})\)
cannot work: it violates A2a for **every** actual orbit, including a normal
one. Statistical sampling owes a separate error payment. The elementary
floor alone leaves a sufficiently large \(O(1/N)\) remainder undecided.
The stronger classical sequence-discrepancy theorem audited in
[CONSTRUCTION.md, “Classical discrepancy restricts the possible remainder”](CONSTRUCTION.md#classical-discrepancy-restricts-the-possible-remainder)
excludes **every** all-epoch \(O(1/N)\) remainder when \(\theta<1/2\):
such a recurrence would bound \(Nd_N\), while the imported theorem forces
\(N W_1(\mu_N,\lambda)\) to be unbounded. That imported result is due to
Kritzinger and Pillichshammer, Theorem 1 at \(d=1,p=1\),
[DOI 10.1007/s00013-021-01688-9](https://doi.org/10.1007/s00013-021-01688-9).
An independently justified \(O(N^{-1/2})\) remainder remains compatible
with both obstructions. Neither obstruction proves such a remainder for
the authentic source.

**Specific protocol extrapolation: REFUTED for every exact orbit.** The
candidate

\[
d_{2M}\le\frac1{16}d_M+\frac1{15M}
\tag{A2c}
\]

cannot hold for every sufficiently large \(M\). Indeed, with \(N=2M\)
its error is \(\varepsilon_N=2/(15N)\), whereas A2b requires

\[
\limsup_NN\varepsilon_N\ge\frac{11}{64}\left(1-\frac18\right)
=\frac{77}{512}>\frac2{15},
\qquad \frac{77}{512}-\frac2{15}=\frac{131}{7680}>0.
\]

Only the dyadic subsequence is needed: iteration of A2c would give
\(\limsup_kN_kd_{N_k}\le16/105<11/64\). Thus every exact orbit violates
A2c at arbitrarily large epochs. A finite pass of this protocol does not
support an all-epoch extrapolation; the universal statement already has
this analytic refutation. Larger independently justified statistical errors
remain possible, and the general exact-BBP source-selected contraction
remains OPEN.

## 3. A zero-seeded positive source that matches every power asymptotic

The generic affine source laws from
[the source-clock action](../../2026-11-09/cayley_source_observer/AFFINE_SOURCE_ACTION.md)
do not identify the source by themselves. The following control is more
discriminating than replacing the source by zero: it keeps an arbitrary
exact BBP prefix, positivity, and every coefficient of the BBP asymptotic
expansion in inverse powers of the clock.

Keep the authentic rational function

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
P_n=\sum_{j=1}^n16^{-j}r(j).
\]

For \(n\ge1\) define the finite rational tail

\[
q_n=\sum_{j=1}^{n}16^{-j}r(n+j).
\]

For each fixed integer \(L\ge1\), declare a different source

\[
r^{[L]}(n)=
\begin{cases}
r(n),&n\le L,\\
16q_{n-1}-q_n,&n>L.
\end{cases}
\]

Cancellation of the common terms in the two finite tails gives the exact
closed form, valid for \(n>L\),

\[
\boxed{r^{[L]}(n)=r(n)-16^{1-n}r(2n-1)-16^{-n}r(2n).}
\tag{A3}
\]

**Proposition A3 (PROVED PAPER).** This altered source has all of the
following properties:

- Its first \(L\) terms agree exactly with the authentic source.
- Every term is positive and rational.
- \(r^{[L]}(n)-r(n)=O(16^{-n}n^{-2})\). In particular, the two sources
  agree to every algebraic asymptotic order, including
  \(n^2r^{[L]}(n)\to15/64\).
- Its literal zero-seeded completed value is
  \(\alpha^{[L]}=P_{2L}\in\mathbb Q\), and is therefore nonnormal in
  base 16.
- Zero recovery, source-clock naturality, and the unique bounded analytic
  tail fixed point all remain valid for this declared altered source.

**Proof.** Positivity and strict monotonicity of the authentic source follow
from its exact positive Laplace representation

\[
r(n)=\int_0^\infty e^{-(8n-7)t}
\bigl(4-2e^{-3t}-e^{-4t}-e^{-5t}\bigr)\,dt.
\]

The parenthesized factor is strictly positive for \(t>0\), since each of
the three subtracted exponentials is smaller than one. For \(n>L\ge1\),
both \(r(2n-1)\) and \(r(2n)\) are smaller than \(r(n)\), whereas
\(16^{1-n}+16^{-n}=17\cdot16^{-n}<1\). Thus A3 is strictly positive.
The inherited bound \(r(m)\le47/(15m^2)\) gives the explicit error

\[
0<r(n)-r^{[L]}(n)
\le\frac{799}{15(2n-1)^2}\,16^{-n},\qquad n>L.
\tag{A4}
\]

This is smaller than every inverse power of \(n\). The source has the
same complete asymptotic expansion in such powers, although it is **not**
the same rational function: the exponential corrections in A3 are real
source changes.

Let \(U^{[L]}_0=0\) and
\(U^{[L]}_n=16U^{[L]}_{n-1}+r^{[L]}(n)\). At clock \(L\),

\[
16^{-L}\bigl(U^{[L]}_L+q_L\bigr)
=P_L+16^{-L}q_L=P_{2L}.
\]

For every \(n>L\), the defining telescoping relation gives

\[
U^{[L]}_n+q_n
=16\bigl(U^{[L]}_{n-1}+q_{n-1}\bigr).
\]

Since \(q_n\to0\), telescoping the convergent series proves

\[
\sum_{n\ge1}16^{-n}r^{[L]}(n)=P_{2L},\qquad
U^{[L]}_n+q_n=16^nP_{2L}\quad(n\ge L).
\tag{A5}
\]

The rational completed orbit is eventually periodic. Its limiting empirical
law is finite and atomic. That law cannot be Lebesgue measure. Alternatively,
it is stationary, and if its \(Q\)-defect vanished, A1 at stationarity
would force it to be Lebesgue measure, a contradiction. Thus its limiting
statistical defect is strictly positive.

The zero-recovery identity and bounded-tail contraction are generic affine
identities for a specified bounded rational source, so they hold for
\(r^{[L]}\) exactly as they do for \(r\). QED.

**Scope.** A3 refutes any universal normality theorem relying only on a
literal zero seed, these generic computation laws, source positivity,
finitely many exact forcing values, and even the complete power-asymptotic
expansion. It does not refute a theorem using the exact four-pole source
identity globally. This altered formula is outside the compiler's fixed
source grammar and contract; it cannot be substituted for the declared
`forcing:n` primitive. Runtime checks authenticate each source output
actually used against the literal four-pole formula. If an undeclared
runtime replacement agrees at every queried clock and changes only later
terms, a finite run cannot detect the unqueried change. A source-label hash
alone is not a proof of global functional equality. A3 is an explicit hostile
object, not a proposed
replacement source or a claim about the digits of π.

## 4. Same source, arbitrarily close seeds, and arbitrarily long shadows

Now keep the **exact authentic source** and put \(\alpha=\pi/16\).
The completed orbit for seed \(s\) is

\[
z_n(s)=\{16^n(\alpha+s)\}.
\]

For each \(L\ge1\), let

\[
a_L=16^{-L}\lfloor16^L\alpha\rfloor,\qquad s_L=a_L-\alpha.
\]

Then \(-16^{-L}<s_L<0\), the completed expansion begins with the first
\(L\) digits of \(\alpha\), and it is identically zero from clock \(L\)
onward. Therefore

\[
\mu_N(s_L)\longrightarrow\delta_0,\qquad
d_N(s_L)\longrightarrow W_1(\delta_0,Q\delta_0)=\frac{15}{32}.
\tag{A6}
\]

These seeds are **irrational**, because \(a_L\) is rational and
\(\alpha\) is irrational. A6 must not be reported as a theorem producing
nonnormal rational perturbations of π. A symbolic representation
\(a_L-\alpha\) gives a mathematical control; it does not make that seed
an exact rational input to the compiler.

For any finite \(N\ge L\), however, choose a rational seed in the nonempty
interval

\[
s\in\bigl(s_L,s_L+16^{-(N+k)}\bigr),\qquad k\ge2.
\tag{A7}
\]

Density of the rationals guarantees such seeds. With
\(e=\alpha+s-a_L\), the completed phases satisfy

\[
0<z_n(s)=16^ne<16^{-k}\qquad(L\le n\le N).
\tag{A8}
\]

Also \(e<16^{-L}\), so the first \(L\) digits agree with those of
\(\alpha\). This is an arbitrarily long **finite** nonnormal shadow with
the exact original source and an exact rational seed. It makes no assertion
about the limiting statistics of that fixed rational seed. For sufficiently
large \(N\), A7 lies entirely below zero, so these controls are nonzero.

**Constructive rational choice.** This does not require an oracle for the
real number \(\alpha\). Refine the BBP rational interval
\([A,B]\ni\alpha\) until \(a_L\) is certified by an unambiguous radix
cut and \(B-A<t\), where \(t=16^{-(N+k)}\). Then the exact rational
choice

\[
s=a_L+\frac t2-\frac{A+B}{2}
\]

satisfies
\(a_L<A+s\le\alpha+s\le B+s<a_L+t\), proving A7–A8 with a
finite certificate. Refinement terminates because the BBP tail bound tends
to zero and irrational \(\alpha\) is not a radix endpoint. This is a
finite source-bound computation, not a statistical limit theorem.

Every such seed is still detected exactly:

\[
16^{-n}U_n(s)-P_n=s\ne0.
\]

Multiple beta-reduction paths can agree perfectly on this nonzero value.
They cannot preserve the zero-authentication certificate, because that
certificate is an exact equality. Exact equality to zero on the rational
input carrier is decidable; this result is not an undecidability claim.

## 5. No contraction remainder uniform on a seed neighborhood

**Proposition A5 (PROVED PAPER).** For any \(\delta>0\) and any fixed
\(0\le\theta<1\), there do not exist a common \(N_0\) and a sequence
\(\varepsilon_N\to0\) such that

\[
d_N(s)\le\theta d_{\lfloor N/2\rfloor}(s)+\varepsilon_N
\]

holds for every rational \(s\) with \(|s|<\delta\) and every
\(N\ge N_0\).

**Proof.** Choose \(L\) with \(16^{-L}<\delta/2\). For every sufficiently
large even \(N\), choose a rational seed as in A7. It lies inside the
specified neighborhood. Set \(\eta=16^{-k}\) and \(c=15/32\). For
\(m=N\) and \(m=N/2\), at most the first \(L\) observations are outside
\((0,\eta)\). Coupling the others to zero gives

\[
W_1(\mu_m,\delta_0)\le L/m+\eta.
\]

For \(0\le x<1/16\), couple \(Q\delta_x\) with \(Q\delta_0\) using
the same translation index: none of the sixteen points crosses the interval
cut, and every displacement is \(x\). For the first \(L\) observations,
use the universal bound one. Therefore

\[
W_1(Q\mu_m,Q\delta_0)\le L/m+\eta,
\qquad |d_m-c|\le2(L/m+\eta).
\]

It follows that

\[
\boxed{
d_N(s)-\theta d_{N/2}(s)
\ge(1-\theta)\frac{15}{32}
 -(2+4\theta)\frac{L}{N}-2(1+\theta)16^{-k}.}
\tag{A9}
\]

Choose \(k\) so the last term is smaller than one quarter of the positive
constant, then take even \(N\) arbitrarily large so the middle term and
\(\varepsilon_N\) are each smaller than one quarter of it. This
contradicts the proposed uniform inequality. QED.

**Boundary.** The seed in A9 may depend on \(N\). The result rules out a
remainder and starting epoch that are uniform on a neighborhood; it does
not rule out pointwise bounds depending on a fixed seed, and it does not
rule out an estimate restricted to the exact singleton \(s=0\). Any proof
that replaces exact zero authentication by an arbitrarily small tolerance
must confront this obstruction.

## 6. Beta reduction cannot erase a semantic statistical defect

Suppose a compiler has a sound denotation map and a beta step satisfies
\(\llbracket t\rrbracket=\llbracket t'\rrbracket\). If both terms
denote the same completed orbit window, then they have the same empirical
law and the same exact \(d_N\). A strict decrease in the statistical
defect therefore cannot follow from syntax reduction alone. It must follow
from an additional mathematical theorem relating different observation
windows or exploiting the exact source.

Likewise, replacing \(\mu\) by \(Q\mu\) makes its conditional symmetry
defect vanish because \(Q^2=Q\), but changes the observed measure. It is
not a sound reduction of a non-Haar orbit to Haar. The analytic tail
operator's \(1/16\) contraction concerns approximation error to a unique
tail; it is not automatically a contraction of the orbit statistic.

The operational compiler should consequently keep distinct outputs for:

- validity of finite beta reduction and alternative evaluation paths;
- exact global source identity and exact recovered seed;
- certified completion intervals and digit-cut resolution;
- a finite statistical defect enclosure;
- an all-epoch analytic estimate, when a separate proof exists.

## 7. Reproducible calibration and claim ledger

The executable replay is [adversarial_probe.py](adversarial_probe.py). Run
`python research/2026-11-10/zero_anchored_lambda_haar/adversarial_probe.py`
from the repository root. It exits nonzero on failure and prints a JSON
receipt with counts, rejection results, and SHA-256 bindings for the four
implementation files used. It also includes positive controls, so a
verifier that rejects every input cannot pass the forgery probe.

An exact `Fraction` replay used \(L\in\{1,2,3,7,16\}\) and clocks
\(1\) through \(40\). It checked 200 source cases: positivity, agreement
with the authentic source exactly on the declared prefix, the finite-sum
identity \(P_L+16^{-L}q_L=P_{2L}\), and A5's completion identity at all
clocks \(n\ge L\). All assertions passed. This was a new local replay,
not an inherited test receipt. The commands use only the unchanged exact
source oracle:

```python
from fractions import Fraction as F
from observational_succ.duck_bbp import forcing

def p(n):
    return sum((forcing(j) / 16**j for j in range(1, n + 1)), F())

def q(n):
    return sum((forcing(n + j) / 16**j for j in range(1, n + 1)), F())

def altered(n, L):
    if n <= L:
        return forcing(n)
    return (forcing(n) - forcing(2*n - 1) / 16**(n - 1)
            - forcing(2*n) / 16**n)

for L in (1, 2, 3, 7, 16):
    alpha = p(2*L)
    assert alpha == p(L) + q(L) / 16**L
    u = F()
    for n in range(1, 41):
        r = altered(n, L)
        assert r > 0
        assert (r == forcing(n)) == (n <= L)
        u = 16*u + r
        if n >= L:
            assert u + q(n) == 16**n * alpha
```

Two further new exact-rational calibrations passed:

- The constructive seed of Section 4 was enclosed using 71 source terms at
  \(L=4,N=64,k=3\). The interval certified the chosen hexadecimal prefix,
  a nonzero negative rational seed of magnitude below \(16^{-4}\), and
  \(\alpha+s\in(a_L,a_L+16^{-67})\).
- The quantization floor and A2a were checked for all windows
  \(1\le N\le64\) of seven exact rational orbits with initial phases
  \(0,1/3,1/17,7/31,1/16,15/16,137/991\): 448 cases passed using
  `canonical_law`, `digit_averaging_law`, `interval_w1`, and
  `interval_w1_haar`. These cases are calibration of the paper proof,
  not an independently implemented Wasserstein routine.

| Claim | Status | Boundary / next discriminator |
|---|---|---|
| Correct \(Q=C T_*\), two-sided A1, and normality equivalence | PROVED PAPER; inherited inverse-branch proof audited | Interval metric and actual orbit endpoint required |
| Existence-only dyadic contraction is equivalent to defect decay | PROVED PAPER (A2) | Need a source-derived independently bounded remainder |
| Any actual orbit has \(d_N\ge11/(64N)\); \(\theta<1/2\) needs the A2b remainder floor | PROVED PAPER | Refutes transfer of \(1/16\) analytic contraction with only \(O(N^{-2})\) tail error |
| \(d_{2M}\le d_M/16+1/(15M)\) at every sufficiently large epoch | REFUTED for every exact orbit (A2c) | Error constant \(2/15\) falls below the necessary \(77/512\) |
| All-epoch contraction with \(\theta<1/2\) and any \(O(1/N)\) remainder | REFUTED by CLASSICAL IMPORT + corollary in CONSTRUCTION.md | The sequence-discrepancy obstruction is stronger than the elementary finite-sample floor |
| Zero seed, generic reduction laws, positivity, prefix agreement and all power asymptotics force normality | REFUTED by A3–A5 | Altered formula is outside the fixed source contract; finite checking cannot inspect an unqueried change |
| Arbitrarily small same-source irrational seeds can give eventually-zero completed paths | PROVED PAPER (A6) | Exact zero gate rejects them |
| Rational seeds can shadow those paths for arbitrarily long finite windows | PROVED PAPER (A7–A8) | No conclusion about their infinite statistics |
| Vanishing contraction remainder uniform on a rational seed neighborhood | REFUTED by A9 | A pointwise singleton-zero estimate remains possible |
| Sound beta rewriting itself decreases an unchanged orbit's exact defect | REFUTED by equality of denotations | Need an analytic theorem acting across observation windows |
| Original-zero exact-BBP dyadic statistical contraction | OPEN | Prove an explicit all-epoch signed source estimate; A2 forbids circular residual fitting |

All new controls leave the frozen source and prior archival files unchanged.
The strongest surviving route uses the literal global source identity,
exact zero selection, and a separately justified signed estimate. The
compiler makes those obligations auditable; the controls explain why its
successful authentication cannot substitute for the missing estimate.

## 8. Hostile Python-object compiler audit

**Observed before hardening in this research round.** Structural dataclass
equality was initially used to bind a program to its regenerated source code
and a certificate to its replay. Python strings can be subclassed with
custom equality, so that comparison alone was not a sound admission check
for arbitrary in-process objects. The following concrete replay succeeded
against the initial implementation:

```python
from dataclasses import replace
from fractions import Fraction as Q
from observational_succ import zero_anchored_lambda as z
from observational_succ import c_monoid_succ_embedding as lc

class PretendEqual(str):
    def __eq__(self, other):
        return True
    def __ne__(self, other):
        return False
    __hash__ = str.__hash__

cert = z.certify_state(z.SourceState(0, Q()))
forged = replace(cert, status=PretendEqual("NORMALITY_PROVED"))
# Initial implementation incorrectly accepted this forged status.
z.verify_source_certificate(forged)

p = z.compile_term(z.Literal(Q(5)))
forged_program = replace(p, code=lc.CONST(PretendEqual("q:0/1")))
# Initial implementation returned 0 with FINITE_REDUCTION_VERIFIED,
# although the declared source term was the literal 5.
z.run(forged_program)
```

The second case is a wrong-denotation witness, not merely a cosmetic status
issue. Its scope is hostile Python objects; ordinary JSON strings do not
carry executable equality methods. The repair is to validate the exact
allowed types and recursive target-node fields before any structural
comparison, including exact plain strings for statuses, source digests and
type names. It must preserve both cases as rejection regressions. This
section preserves the discovered failure mechanism.

**Repair independently replayed.** On the corrected compiler file with
SHA-256
`262c1b4b1b3bbc672e72a10742c6d5f4b9547e13f064b14e4c5b573307c3f7cd`,
the adversarial replay rejected both the forged source-certificate status
and the wrong-denotation target, each with `CompilerError`. The unmodified
source certificate and literal-five program both passed their positive
controls. Read-only inspection confirmed that exact recursive target-field
validation and exact status/passport/type-name checks precede structural
equality. The JSON replay also passed all 200 altered-source cases, 176
completion identities, 448 quantization cases, and 61 certified finite
shadow phase windows; its exact-zero gate rejected the rational shadow.
This verifies the discovered regression's repair, not immunity to arbitrary
future mutations or a statistical contraction theorem.
