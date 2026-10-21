# Duck → Gamma → genuine primes → digits: conditional contingency audit

Date: 2026-10-21. Baseline: PR #232 at
`9894d39250021bbbc2615c33dee0d286ddf0950f`.
Owner: cloud conditional-source lane. No archived source is changed.

## Verdict and exact hole contract

**SURVIVES, PROVED LOCAL (paper; external dependencies below):** a quantified
Chebyshev estimate gives an explicit approximation to the actual constant
π from genuine prime powers, and consequently an explicit **difference bound**
between two finite base-16 Fourier means. RH supplies one declared Chebyshev
estimate. This is a source-sensitive conditional implication, but neither
Fourier mean is proved to cancel. The prime cutoff needed by this route grows
exponentially with the digit horizon.

**SURVIVES, PROVED LOCAL (paper, conditional):** integer ABC gives a lower bound
for a primitive integer residual attached to a rational approximation and a
base-b prefix. The missing quantitative input is a *joint* approximation and
radical estimate, stated below. ABC is never applied to an irrational residual.

**REFUTED:** even the optimal irrationality exponent 2 does not force base-16
normality. A published theorem on the Thue–Morse constant supplies an explicit
countermodel. A weaker anti-long-run consequence does survive.

**UNVERIFIED:** RH, ABC, or RH+ABC imply source-specific π Fourier cancellation.
There is no proof or refutation of that implication here. No axiom equivalent
to normality is introduced as a discovered geometric principle.

The load-bearing hole is control of the signed phases
`exp(2π i h 16^j π)` averaged over j, not construction of arbitrarily accurate
approximants to π. The discarded dependency is any purported automatic arrow
from small scalar approximation error, finite irrationality exponent, or
one-variable prime counting to cancellation of these expanding phases.

Formal status of this entire dossier: **not Lean formalized**. The executable
objects below are exact rational finite checks; they do not grant formal or
source authority. This lane adds no Lean axiom and registers no proof checker.

## 1. The authentic classical source bridge

For real s>1 the absolutely convergent Euler product and logarithmic expansion
give

\[
 \zeta(s)=\prod_p(1-p^{-s})^{-1},\qquad
 \log\zeta(s)=\sum_p\sum_{k\ge1}\frac1{k p^{ks}}
             =\sum_{n\ge2}\frac{\Lambda(n)}{n^s\log n}.
\]

Absolute convergence follows, for example, by bounding the double sum by
`(1-2^{-s})^{-1} sum_{n>=2} n^{-s}`. Thus taking logarithms and regrouping
are analytic identities here, not formal Euler-product guesses. At s=2,
Euler's classical value is ζ(2)=π²/6.

The conventional completed function is

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad \xi(2)=\zeta(2)/\pi=\pi/6.
\]

This keeps the Gamma factor, the polynomial completing the poles, and the
archimedean normalization. The geometric constant also occurs in
Γ(1/2)=√π and the Wallis identity
`π/2 = product_{n>=1} 4n²/(4n²-1)`. These classical identities identify the
same constant; their mere coexistence is not a digit-distribution theorem.
We use no nontrivial zeta-zero ordinates as construction inputs. An imported
RH-to-prime theorem may itself use explicit formulas and verified zero data;
that is an external proof dependency, not a new source reconstruction here.

Source mutations are decisive:

* Treating 6 as an additional prime multiplies the s=2 Euler product by
  `(1-6^{-2})^{-1}=36/35`, changing the reconstructed constant by √(36/35).
* At n=4 the genuine logarithmic weight is `1/(2·4²)=1/32`. Dropping the
  exponent factor 1/k doubles this atom to 1/16.
* Omitting π^{-s/2} from ξ produces ξ_fake(2)=ζ(2)=π²/6, not π/6.

None of these modified objects is entitled to retain the original completed
zeta identity or an RH error estimate. Exact atom tests also distinguish a
finite atom mutation `+1/36` from adding an entire fake Euler factor.

## 2. RH environment: a genuine π-specific finite Fourier bound

### 2.1 Quantified premise and theorem

Let X>1 and C>0 be real. Put

\[
 \psi(u)=\sum_{p^k\le u}\log p,\quad
 S(X)=\sum_{p^k\le X}\frac1{k p^{2k}},\quad
 J(X)=\int_X^\infty\frac{du}{u^2\log u}.
\]

The cutoff convention is `p^k <= X`, including a prime power at the boundary.
Assume the quantified premise

\[
 \tag{Psi(C,X)}
 \forall u\in\mathbb R,\ u\ge X:\quad
 |\psi(u)-u|\le C\sqrt u(\log u)^2.
\]

Then

\[
 \tag{R1}
 \left|\log(\pi^2/6)-S(X)-J(X)\right|
 \le \epsilon_C(X):=
 \frac{C}{X^{3/2}}\left(\frac73\log X+\frac{14}{9}\right).
\]

**Proof.** Write R(u)=ψ(u)-u and f(u)=1/(u² log u). Stieltjes integration
by parts on `(X,T]`, followed by T→∞, gives

\[
 \sum_{n>X}\frac{\Lambda(n)}{n^2\log n}-J(X)
 =-R(X)f(X)-\int_X^\infty R(u)f'(u)\,du.
\]

The boundary at infinity vanishes under Psi(C,X). The boundary at X uses
the right-continuous ψ(X), precisely matching the excluded tail atom n=X.
Since

\[
 -f'(u)=u^{-3}\left(\frac2{\log u}+\frac1{(\log u)^2}\right),
\]

the absolute error is at most

\[
 C X^{-3/2}\log X
 +C\int_X^\infty u^{-5/2}(2\log u+1)\,du
 =C X^{-3/2}\left(\frac73\log X+\frac{14}{9}\right).
\]

The integral evaluation follows from
`∫_X^∞ u^{-5/2} du = (2/3)X^{-3/2}` and
`∫_X^∞ u^{-5/2} log u du = X^{-3/2}((2/3)log X+4/9)`.
This proves R1. □

The primary result used to instantiate the premise is Lee–Nosal,
**arXiv:2312.05628v4, Theorem 1.2, 2 October 2025**: under RH,

\[
 |\psi(u)-u|\le
 \frac{\sqrt u\log u(\log u-\log\log u)}{8\pi}
 \quad (u\ge101).
\]

Since π>3 and log log u>0 here, it implies Psi(1/24,X) for every X≥101.
The version is pinned: earlier versions had different thresholds. This is an
imported conditional theorem, not a locally reproduced analytic proof.

### 2.2 Transport to the digit orbit with all constants

Define the genuine-source approximant

\[
 a_X=\sqrt6\exp\big((S(X)+J(X))/2\big).
\]

If ε=ε_C(X)≤1 then R1 gives

\[
 |a_X-\pi|\le\pi(e^{\epsilon/2}-1)\le4\epsilon.
\]

Indeed, the ratio a_X/π lies between e^{-ε/2} and e^{ε/2}; the mean-value
bound `e^{ε/2}-1 <= ε e^{1/2}/2 <= ε`, together with π<4, suffices.

For every N≥1 and nonzero integer h define

\[
 W_{N,h}(\alpha)=\frac1N\sum_{j=0}^{N-1}
                 \exp(2\pi i h16^j\alpha).
\]

The chord bound `|exp(iu)-exp(iv)|<=|u-v|` yields the explicit theorem

\[
 \tag{R2}
 |W_{N,h}(\pi)-W_{N,h}(a_X)|
 \le\min\left\{2,
 \frac{32|h|\epsilon_C(X)(16^N-1)}{15N}\right\}.
\]

This uses 2π<8 and `sum_{j<N}16^j=(16^N-1)/15`; it is valid for every
allowed X,N,h, with no hidden constant dependence on X or N.

Under RH, fixed h and `X_N=16^{aN}` with any fixed a>2/3 make this difference
tend to zero exponentially. At the critical exponent a=2/3 the stated upper
bound is only O_h(1); taking
`X_N=16^{2N/3}N^η` for any fixed η>0 makes it O_{h,η}(N^{-3η/2}).
These statements follow by direct substitution into R2; the ε≤1 condition
holds for all sufficiently large N. The bounds extend to rounded-up integer
cutoffs with harmless constants. Fixed X and N→∞ give no useful transfer
from this error budget. Saturation at 2 is a failure of this sufficient bound,
not a lower bound for the actual difference.

**What remains.** We have no estimate tending to zero for
`|W_{N,h}(a_{X_N})|`. The triangle inequality cannot turn a difference bound
into cancellation. Asking for cancellation of these exponentially accurate
approximants for every h is simply an equivalent analytic target after R2;
we record it as the target, not as an independently justified hypothesis.

### 2.3 Exact executable envelope and an unconditional comparison

For integer X≥101 the code replaces log X by `bit_length(X)` and √X by
`isqrt(X)` in the denominator. Since log X<bit_length(X) and
isqrt(X)≤√X, the rational value

\[
 \widehat\epsilon_C(X)=
 \frac{C((7/3)\operatorname{bitlength}(X)+14/9)}{X\lfloor\sqrt X\rfloor}
\]

is a valid upper bound. No floating-point logarithm is certified. The object
returns a **conditional budget**, not an evaluation of J or a_X, not an
authentication of RH, and not a Fourier cancellation certificate.

RH is not needed merely to approximate π. For integer M≥1, the integral
test gives

\[
 \frac1{M+1}\le\zeta(2)-\sum_{n=1}^M\frac1{n^2}\le\frac1M.
\]

Put `z_M=sum_{n<=M}1/n²+(1/M+1/(M+1))/2` and `b_M=sqrt(6z_M)`.
Then

\[
 |z_M-\zeta(2)|\le\frac1{2M(M+1)},\qquad
 |b_M-\pi|=\frac{6|z_M-\zeta(2)|}{b_M+\pi}
 \le\frac1{M(M+1)}.
\]

Consequently an unconditional analogue of R2 is
`|W_{N,h}(π)-W_{N,h}(b_M)| <= min(2,8|h|(16^N-1)/(15NM(M+1)))`.
This even gives a stronger cutoff exponent for this different representation.
Thus R1 is a genuine RH-dependent prime-source statement, but is not claimed
as a computational advance, as a necessary use of RH, or as an escape from
the cancellation obstruction. It is a precisely scoped cross-source bridge.

## 3. ABC environment: the residual that ABC actually controls

Assume integer ABC in the following quantified form for a fixed ε>0:
there is K_ε>0 such that for every pair of coprime positive integers U,V,
with D=|U−V|>0 and H=max(U,V),

\[
 \tag{ABC_ε}
 H\le K_\epsilon\operatorname{rad}(UVD)^{1+\epsilon}.
\]

This is the usual primitive triple `min(U,V)+D=H`. Pairwise coprimality
implies `rad(UVD)=rad(UV)rad(D)`, and rad(D)≤D. Therefore

\[
 \tag{A1}
 D\ge\frac{H^{1/(1+\epsilon)}}
 {K_\epsilon^{1/(1+\epsilon)}\operatorname{rad}(UV)}.
\]

Now fix positive integers p,q,A, integer b≥2 and integer n≥0. Put

\[
 g=\gcd(pb^n,qA),\quad U=pb^n/g,\quad V=qA/g,
 \quad H=\max(U,V),\quad D=|U-V|>0.
\]

Since gcd(U,V)=1,

\[
 \tag{A2}
 \left|\frac pq-\frac A{b^n}\right|
 =\frac{gD}{qb^n}
 \ge B:=\frac{gH^{1/(1+\epsilon)}}
 {qb^nK_\epsilon^{1/(1+\epsilon)}\operatorname{rad}(UV)}.
\]

If an independently certified bound `|π-p/q|<=e` is also available, reverse
triangle inequality gives

\[
 \tag{A3}
 |\pi-A/b^n|\ge\max(0,B-e).
\]

For a prefix A/b^n followed by r zeros, its error is at most b^{-n-r}.
Thus `B-e>b^{-n-r}` forbids that proposed run. This is an actual conditional
digit consequence when the indicated budgets are supplied, not a statement
that those budgets hold for π at all n.

**Missing lemma and boundary.** If
`H^{1/(1+ε)} <= K_ε^{1/(1+ε)} rad(UV)`, A1 is no stronger than the
unconditional integer fact D≥1. A useful application requires a π-specific
sequence of p/q, simultaneous approximation errors e, and reduced radicals
rad(UV) small enough that B−e is positive on the desired digit scales.
BBP extraction supplies a rational expansion, not this joint low-radical
property. ABC supplies no bound directly for `|b^nπ-A|`, since this is not
an integer ABC triple. Nor does A3 control frequencies of general blocks.

The exact helper implements ε=1, squares A1/A2, and **checks the ABC premise
for the particular finite triple supplied**. Its constant K is caller data;
passing one triple never asserts existence of a universal K. False premises
and D=0 are rejected. For example p/q=22/7, A/b^n=314/100 have g=2,D=1:
forgetting primitive normalization would change the claimed residual.

## 4. RH+ABC environment and the actual arithmetic obstruction

RH and ABC have separate roles here. RH supplies Psi(C,X) and the genuine
prime approximation R1. ABC constrains normalized residuals between rational
numbers as in A2. Combining them does not automatically supply rational
numerators/denominators for a_X with small radical: a_X includes an exponential
and an integral. Rational enclosure of a_X is possible, but its denominator
choice and radical must then be audited. Choosing a fine grid does not make
the approximation simultaneously low-radical after subtraction of a prefix.

Even GRH-style estimates for primes in fixed arithmetic progressions would
be a different input from RH for ζ. BBP denominator classes `8k+r` and the
weights `16^{n-k} modulo (8k+r)` vary with both k and the digit horizon n.
A fixed-modulus prime estimate does not control these composite denominators,
their modular powers, or the nonlinear exponential of their summed fractions.
This is a quantified missing bridge, not evidence of a logical impossibility
of any future RH/ABC implication.

The current **verdict-changing task** for this lane is modest and noncircular:
construct a specific family of π rational approximants with a proved error
and a proved radical estimate strong enough to make A3 improve D≥1 for a
growing digit range. That would yield genuine new restrictions even before
any normality theorem. Its failure would not refute normality.

## 5. A decisive negative control and the surviving anti-run theorem

Let t_0=0, t_{2k}=t_k, t_{2k+1}=1−t_k, the Thue–Morse sequence. For every
integer b≥2 define `ξ_b=sum_{k>=0} t_k b^{-k}`. Bugeaud (2011), main theorem,
proves its irrationality exponent is exactly 2. In base 16 its digits are
only 0 and 1. Irrationality ensures no terminating-expansion ambiguity;
digit 2 has limiting frequency zero, so ξ_16 is not base-16 normal.
This refutes **optimal irrationality exponent ⇒ base-16 normality**.
It does not refute a π-specific implication using additional structure.

For b=2 even balanced single-digit frequencies do not repair the route.
No three consecutive Thue–Morse digits are all equal: every consecutive
triple contains a pair indexed 2k,2k+1, whose digits are complementary.
Thus the words 000 and 111 never occur. The executable control independently
constructs the first 4096 digits both by bit parity and by substitution
`0→01, 1→10`. These finite checks corroborate the construction; the general
forbidden-word argument is the proof. The imported exponent-2 theorem is
not claimed to be checked by that census.

A useful weakening survives. Define the irrationality exponent μ(α) using
infinitely many rational approximations. If α is irrational and ν>μ(α),
there exists c_ν>0 such that for every integer p and positive integer q,

\[
 |\alpha-p/q|\ge c_\nu q^{-\nu}.
\]

To justify the global constant, the definition excludes violations of
`|α-p/q|>=q^{-ν}` for all sufficiently large reduced q; the finitely many
remaining reduced denominators have a positive minimum scaled error.
Passing to an unreduced q can only decrease q^{-ν}. If r zeros follow
position n in the canonical base-b expansion, its prefix A/b^n satisfies
`|α-A/b^n|<=b^{-n-r}`. Therefore

\[
 \tag{D1}
 r\le(\nu-1)n-\log_b c_\nu.
\]

For a run of b−1 use the adjacent upper rational `(A+1)/b^n`; the same
estimate follows. Apply to the fractional part if α has an integer part.
Zeilberger–Zudilin's published bound μ(π)≤7.103205334137… permits ν=7.104,
and hence a π-specific linear anti-run bound with an unspecified constant.
We do not assert that this 2020 bound is the newest available bound.
D1 is far weaker than normality and is consistent with the countermodel.

## 6. Source, proof, and claim dependency ledger

Source status σ and proof status φ are independent. `IDENTIFIED` below means
the stated source and precise object were inspected, not that an arbitrary
receipt authenticates a theorem in the running Python process.

| Local claim | Exact dependencies | σ | φ and scope |
|---|---|---|---|
| Euler log at 2 and ξ(2)=π/6 | genuine primes; classical ζ(2), Γ(1), completed normalization | IDENTIFIED classical definitions | CLASSICAL; not Lean checked here |
| R1 | quantified Psi(C,X), absolutely convergent Euler log | IDENTIFIED prime source | PROVED LOCAL paper conditional on Psi |
| RH instance of R1 | Lee–Nosal v4 Thm 1.2, RH | IDENTIFIED pinned manuscript | CLASSICAL imported conditional + local deduction |
| R2 | R1, exponential Lipschitz bound, exact geometric sum | same actual π source | PROVED LOCAL paper; difference only |
| A1–A3 | ABC_ε; exact primitive normalization; independently supplied π approximation for A3 | exact integer residual; π link conditional | PROVED LOCAL paper conditional |
| Thue–Morse obstruction | Bugeaud main theorem; omitted-digit argument | IDENTIFIED published theorem | REFUTED general implication; no π-specific refutation |
| D1 | irrational α and ν>μ(α) | arbitrary source; published π specialization | PROVED LOCAL paper / CLASSICAL method |
| π base-16 cancellation | no proved dependency closes this row | actual source named | UNVERIFIED |

No result in this table is promoted beyond its weakest premise. The numerical
helpers are TESTED MODEL evidence for finite exact arithmetic only. They have
immutable returned records and strict type guards; their statuses explicitly
exclude universal ABC, RH, and cancellation certification. Direct construction
of a Python record is not proof authority and no consumer may treat it as such.

## 7. Reproduction, independent checks, and next falsifiers

Run from the repository root:

```sh
python -m unittest discover -s tests -p 'test_duck_source_bridge.py' -v
python scripts/duck_source_bridge_probe.py
```

The test suite checks genuine prime-power support against independent SymPy
factorization, exact exponent weights and composite controls, rational error
budgets, primitive residual bounds against independently factored radicals,
zero/false ABC-premise rejection, and independent Thue–Morse constructions.
The receipt records implementation/test/dossier hashes and reproducible exact
outputs. The receipt itself is not an authenticated formal build receipt.
Root owns full repository validation. A separate cloud referee independently
rederived R1's right-continuous boundary term and constants, R2's constant and
cutoff regime, A1–A3's primitive normalization, and the unconditional comparison.
That referee also inspected Lee–Nosal v4 and the Thue–Morse source theorem.
Their 2026-10-21 verdict was that these paper statements survive with their
declared scope. This is a separate same-model derivation and external-source
comparison, **not** a human external referee or Lean verification.

Immediate adversarial targets are the Stieltjes boundary convention at a prime
power, coefficients 7/3 and 14/9, gcd normalization in A2, and the exponential
cutoff needed by R2. Check the signed tail formula independently before treating
R1 as reviewed. A useful future formalization is R2 as a generic finite-sum
Lipschitz theorem, then a separate Stieltjes analytic development; do not create
a Lean axiom asserting the unproved cancellation.

## 8. Prior art and inspected references

The ingredients are classical. R1 is an elementary partial-summation consequence
with explicit constants; R2 is elementary precision propagation; A1–A3 are
straight deductions from ABC; D1 is a standard approximation argument.
This is **new-to-project synthesis**, with no claim of academic originality.
The strongest negative result here rests on a published independent theorem,
not agreement among assistant reports. Our own paper derivations require the
separate referee review recorded by the campaign coordinator.

1. E. S. Lee and P. Nosal, *Sharper bounds for the error in the prime number
   theorem assuming the Riemann Hypothesis*, [arXiv:2312.05628v4](https://arxiv.org/html/2312.05628v4),
   Theorem 1.2, 2 October 2025. Exact version inspected. The authors' analytic
   proof is imported, not reproduced or formalized here.
2. Y. Bugeaud, *On the rational approximation to the Thue–Morse–Mahler numbers*,
   Ann. Inst. Fourier 61 (2011), 2065–2076,
   [DOI 10.5802/aif.2666](https://doi.org/10.5802/aif.2666),
   [primary PDF](https://www.numdam.org/item/10.5802/aif.2666.pdf), main theorem
   in §2. Full mathematical statement inspected; no article copy is committed.
3. D. Zeilberger and W. Zudilin, *The irrationality measure of π is at most
   7.103205334137…*, Moscow J. Combin. Number Theory 9 (2020), 407–419,
   [authors' page and manuscript](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html).
4. NIST DLMF, [§25.2](https://dlmf.nist.gov/25.2),
   [§25.4](https://dlmf.nist.gov/25.4), [§25.6](https://dlmf.nist.gov/25.6),
   [§5.4](https://dlmf.nist.gov/5.4): authoritative classical definitions,
   normalization and special values. These are identity references, not
   sources of a normality theorem.

Access and provenance distinction: source URLs, DOI, manuscript version and
theorem locations are pinned above. No cryptographic hash of a downloaded
publisher PDF is claimed. The local reproducibility receipt hashes only the
repository files it actually reads.
